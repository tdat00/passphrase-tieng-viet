#!/usr/bin/env python3
"""Đếm lại các họ chính tả H5 theo đúng ranh giới âm tiết, dấu câu và từ.

- Chỉ ghép âm tiết liền nhau trong cùng một đoạn không có dấu câu; gạch nối giữa hai chữ là kí hiệu riêng.
- Lượt "nghi vắt từ": âm tiết trái + âm tiết đầu, hoặc âm tiết cuối + âm tiết phải, tạo thành một từ hai
  âm tiết có trong Viet11K/22K/39K/74K (ví dụ bánh | trưng bày, khả năng | xuất hiện). Áp như nhau cho
  mọi dạng; số "sạch" không tính các lượt này.
- Phụ đề: đếm mọi dòng (chính sách cũ) và đếm dòng khác nhau (độ nhạy). Web: dòng khác nhau (chính sách cũ).
- Lưu mẫu ngữ cảnh bottom-k theo băm để đọc kiểm (không đưa vào repo).

Chạy: python recount_h5.py  (ghi h5/counts.json, h5/contexts.json)
"""
import collections
import gzip
import hashlib
import json
import os
import re
import sys
import time
import unicodedata as ud
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import check_wordlist as cw  # noqa: E402

CORPUS = os.environ.get("CORPUS_DIR", "data")  # thư mục chứa các kho đã tải (không có trong repo)
DISC = os.path.join(os.path.dirname(os.path.dirname(HERE)), "discussion")
L = "a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ"
RUN = re.compile(rf"[{L}]+|[^\s{L}]+")
K = 60  # cỡ mẫu ngữ cảnh mỗi dạng, mỗi lớp (sạch / vắt từ), mỗi kho

EXTRA = [  # (nhóm A, nhóm B, loại); các dạng trong một nhóm chỉ khác dấu phân cách
    (["taxi"], ["tắc xi", "tắc-xi", "tắcxi"], "f"),
    (["radio"], ["ra đi ô", "ra-đi-ô", "rađiô"], "f"),
    (["micrô", "mi-crô", "mi crô"], ["micro"], "f"),
    (["mô tơ", "mô-tơ", "môtơ"], ["motor"], "f"),
    (["sơ mi"], ["sơ-mi", "sơmi"], "g"),
    (["đô la"], ["đô-la", "đôla"], "g"),
    (["bít tết"], ["bít-tết", "bíttết"], "g"),
]


def nfc(s):
    return ud.normalize("NFC", s)


def tokenize(text):
    """Trả về danh sách token: âm tiết (khóa canon), '<HY>' (gạch nối giữa hai chữ) hoặc '<P>' (ranh giới)."""
    ms = list(RUN.finditer(text))
    out = []
    for j, m in enumerate(ms):
        s = m.group(0)
        if s[0].isalpha():
            out.append(cw.canon_syl(s))
        elif s == "-" and 0 < j < len(ms) - 1 and ms[j - 1].end() == m.start() and ms[j + 1].start() == m.end() \
                and ms[j - 1].group(0)[0].isalpha() and ms[j + 1].group(0)[0].isalpha():
            out.append("<HY>")
        else:
            out.append("<P>")
    return out


def form_tokens(form):
    return tuple(tokenize(nfc(form.lower())))


def load_pairs():
    rows = []
    with open(os.path.join(DISC, "ho-chinh-ta-ban-dau.tsv"), encoding="utf-8") as f:
        head = f.readline().rstrip("\n").split("\t")
        for line in f:
            r = dict(zip(head, line.rstrip("\n").split("\t")))
            a, b, t = r["chuan"], r["bien_the"], r["loai_H5"]
            if a == "ô tô":
                rows.append(([a], [b, "ô-tô"], t))
            else:
                rows.append(([a], [b], t))
    return rows + EXTRA


def load_dict2():
    d = set()
    for name in ("Viet11K", "Viet22K", "Viet39K", "Viet74K"):
        with open(os.path.join(HERE, "..", "data", f"{name}.txt"), encoding="utf-8") as f:
            for w in f:
                p = nfc(w.strip().lower()).replace("-", " ").split()
                if len(p) == 2:
                    d.add((cw.canon_syl(p[0]), cw.canon_syl(p[1])))
    return d


PAIRS = load_pairs()
FORMS = sorted({f for a, b, _ in PAIRS for f in a + b})
FTOK = {f: form_tokens(f) for f in FORMS}
BYFIRST = collections.defaultdict(list)
for f, t in FTOK.items():
    BYFIRST[t[0]].append((f, t))
DICT2 = None


def _init():
    global DICT2
    DICT2 = load_dict2()


def _bkey(f, src, lineno, i):
    return int.from_bytes(hashlib.blake2b(f"{f}|{src}|{lineno}|{i}".encode(), digest_size=8).digest(), "big")


def _work(job):
    src, batch = job
    cnt = collections.Counter()   # (form, kind) -> n ; kind in all, all_clean, dist, dist_clean
    why = collections.Counter()   # (form, "trái"/"phải", từ chồng) -> n  (chỉ lượt dòng đầu tiên/khác nhau)
    ctx = collections.defaultdict(list)  # (form, sach|vat) -> [(key, text)]
    for lineno, first, text in batch:
        toks = tokenize(text)
        for i, t in enumerate(toks):
            for f, ft in BYFIRST.get(t, ()):
                n = len(ft)
                if tuple(toks[i:i + n]) != ft:
                    continue
                left = toks[i - 1] if i > 0 and not toks[i - 1].startswith("<") else None
                right = toks[i + n] if i + n < len(toks) and not toks[i + n].startswith("<") else None
                words = [x for x in ft if not x.startswith("<")]
                lo = left is not None and len(words) > 1 and (left, words[0]) in DICT2
                ro = right is not None and len(words) > 1 and (words[-1], right) in DICT2
                clean = not (lo or ro)
                cnt[(f, "all")] += 1
                if clean:
                    cnt[(f, "all_clean")] += 1
                if first:
                    cnt[(f, "dist")] += 1
                    if clean:
                        cnt[(f, "dist_clean")] += 1
                    if lo:
                        why[(f, "trái", left + " " + words[0])] += 1
                    if ro:
                        why[(f, "phải", words[-1] + " " + right)] += 1
                    key = _bkey(f, src, lineno, i)
                    lst = ctx[(f, "sach" if clean else "vat")]
                    lst.append((key, text.strip()[:220]))
                    if len(lst) > 4 * K:
                        lst.sort()
                        del lst[K:]
    for k in ctx:
        ctx[k].sort()
        del ctx[k][K:]
    return cnt, why, dict(ctx)


def scan(src, path, dedupe_web):
    t0 = time.time()
    seen = set()
    total = distinct = 0
    cnt, why = collections.Counter(), collections.Counter()
    ctx = collections.defaultdict(list)
    sha = hashlib.sha256()
    with open(path, "rb") as fb:
        for block in iter(lambda: fb.read(1 << 22), b""):
            sha.update(block)

    def batches():
        nonlocal total, distinct
        buf = []
        with gzip.open(path, "rb") as fz:
            for lineno, raw in enumerate(fz, 1):
                total += 1
                h = hash(raw.rstrip(b"\r\n"))
                first = h not in seen
                if first:
                    seen.add(h)
                    distinct += 1
                elif dedupe_web:
                    continue
                buf.append((lineno, first, nfc(raw.decode("utf-8", "ignore").lower())))
                if len(buf) >= 20000:
                    yield (src, buf)
                    buf = []
        if buf:
            yield (src, buf)

    with ProcessPoolExecutor(14, initializer=_init) as ex:
        for c, w, x in ex.map(_work, batches(), chunksize=1):
            cnt.update(c)
            why.update(w)
            for k, v in x.items():
                lst = ctx[k]
                lst.extend(v)
                lst.sort()
                del lst[K:]
    meta = {"file": os.path.basename(path), "sha256": sha.hexdigest(), "lines": total, "distinct_lines": distinct,
            "seconds": round(time.time() - t0)}
    print(src, meta, flush=True)
    return meta, cnt, why, ctx


def main():
    out = {"pairs": PAIRS, "meta": {}, "counts": {}, "overlap": {}}
    ctx_out = {}
    for src, fn, dd in (("sub", "opensubs-vi.txt.gz", False), ("web", "ccaligned-vi.txt.gz", True)):
        meta, cnt, why, ctx = scan(src, os.path.join(CORPUS, fn), dd)
        out["meta"][src] = meta
        for f in FORMS:
            out["counts"].setdefault(f, {})[src] = {k: cnt[(f, k)] for k in ("all", "all_clean", "dist", "dist_clean")}
            top = collections.Counter({(s, w): n for (ff, s, w), n in why.items() if ff == f})
            out["overlap"].setdefault(f, {})[src] = [[s, w, n] for (s, w), n in top.most_common(15)]
            ctx_out.setdefault(f, {})[src] = {k: [t for _, t in ctx.get((f, k), [])] for k in ("sach", "vat")}
    json.dump(out, open(os.path.join(HERE, "counts.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(ctx_out, open(os.path.join(HERE, "contexts.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print("xong", len(FORMS), "dạng")


if __name__ == "__main__":
    main()
