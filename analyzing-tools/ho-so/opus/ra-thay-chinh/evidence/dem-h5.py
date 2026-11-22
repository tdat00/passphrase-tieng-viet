"""H5: đếm lại mọi dạng của 632 cặp (từ chính, dạng kia) trong bien-the-chinh-tho.tsv trên hai kho,
theo ranh giới của ho-so/opus/h5/recount_h5.py (luật H5, tieu-chi-thong-nhat.md mục H5).

    set HND_DIR=<ngoài repo: Viet11K.txt … Viet74K.txt>       (gắn cờ "nghi vắt từ")
    set KHO_DIR=<ngoài repo: sub-vi.txt.gz, web-vi.txt.gz>   (OpenSubtitles v2018 mono vi; CCAligned v1 mono vi)
    set NGU_CANH=<ngoài repo: tệp JSON mẫu ngữ cảnh để đọc kiểm>
    python dem-h5.py  ->  dem-h5.tsv, dem-h5.log
    (CAP_H5=<tệp cặp tu/bien_the> và RA_H5=<tên đầu ra> để đếm danh sách cặp khác, ví dụ cap-h5b.tsv -> dem-h5b)

- Chỉ ghép âm tiết liền nhau trong một đoạn không có dấu câu; thanh điệu được chuẩn hóa theo âm tiết
  (hoà = hòa) để hai cách đặt dấu đếm chung.
- "Nghi vắt từ": âm tiết trái + âm tiết đầu, hoặc âm tiết cuối + âm tiết phải, là một từ hai âm tiết trong HND.
  Số "sạch" không tính các lượt này (chỉ áp cho dạng nhiều âm tiết).
- Phụ đề: mọi dòng (chính sách cũ) và dòng khác nhau (độ nhạy). Web: dòng khác nhau.
Chỉ ghi số đếm vào repo; mẫu ngữ cảnh chỉ ghi ra NGU_CANH (ngoài repo) và phải xóa sau khi đọc.
"""
import collections
import gzip
import hashlib
import json
import os
import re
import time
import unicodedata as ud
from concurrent.futures import ProcessPoolExecutor

from chung import AT, HERE, HND_DIR, out_utf8, rd, write_tsv

KHO_DIR = os.environ.get("KHO_DIR", "")
NGU_CANH = os.environ.get("NGU_CANH", "")
L = "a-zàáảãạăằắẳẵặâầấẩẫậđèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ"
RUN = re.compile(rf"[{L}]+|[^\s{L}]+")
TONE = {"\u0300": "1", "\u0309": "2", "\u0303": "3", "\u0301": "4", "\u0323": "5"}
K = 30


def canon(s):
    t, base = "0", []
    for ch in ud.normalize("NFD", s):
        if ch in TONE:
            t = TONE[ch]
        else:
            base.append(ch)
    return ud.normalize("NFC", "".join(base)) + t


def tokenize(text):
    ms = list(RUN.finditer(text))
    out = []
    for j, m in enumerate(ms):
        s = m.group(0)
        if s[0].isalpha():
            out.append(canon(s))
        elif s == "-" and 0 < j < len(ms) - 1 and ms[j - 1].end() == m.start() and ms[j + 1].start() == m.end() \
                and ms[j - 1].group(0)[0].isalpha() and ms[j + 1].group(0)[0].isalpha():
            out.append("<HY>")
        else:
            out.append("<P>")
    return out


PAIRS_FILE = os.environ.get("CAP_H5", str(AT / "ho-so/opus/du-phong-v2/evidence/bien-the-chinh-tho.tsv"))
OUT_STEM = os.environ.get("RA_H5", "dem-h5")
PAIRS = [(r["tu"], r["bien_the"]) for r in rd(PAIRS_FILE)]
VARIANTS = {b for _, b in PAIRS}
FORMS = sorted({f for p in PAIRS for f in p})
FTOK = {f: tuple(tokenize(ud.normalize("NFC", f.lower()))) for f in FORMS}
BYFIRST = collections.defaultdict(list)
for _f, _t in FTOK.items():
    BYFIRST[_t[0]].append((_f, _t))
DICT2 = None


def _init():
    global DICT2
    DICT2 = set()
    for name in ("Viet11K", "Viet22K", "Viet39K", "Viet74K"):
        for w in open(HND_DIR / f"{name}.txt", encoding="utf-8"):
            p = ud.normalize("NFC", w.strip().lower()).replace("-", " ").split()
            if len(p) == 2:
                DICT2.add((canon(p[0]), canon(p[1])))


def _bkey(f, src, lineno, i):
    return int.from_bytes(hashlib.blake2b(f"{f}|{src}|{lineno}|{i}".encode(), digest_size=8).digest(), "big")


def _work(job):
    src, batch = job
    cnt = collections.Counter()
    ctx = collections.defaultdict(list)
    for lineno, first, text in batch:
        toks = tokenize(text)
        for i, t in enumerate(toks):
            for f, ft in BYFIRST.get(t, ()):
                n = len(ft)
                if tuple(toks[i:i + n]) != ft:
                    continue
                left = toks[i - 1] if i > 0 and not toks[i - 1].startswith("<") else None
                right = toks[i + n] if i + n < len(toks) and not toks[i + n].startswith("<") else None
                lo = left is not None and n > 1 and (left, ft[0]) in DICT2
                ro = right is not None and n > 1 and (ft[-1], right) in DICT2
                clean = not (lo or ro)
                cnt[(f, "all")] += 1
                cnt[(f, "all_clean")] += clean
                if first:
                    cnt[(f, "dist")] += 1
                    cnt[(f, "dist_clean")] += clean
                    if f in VARIANTS:
                        lst = ctx[(f, "sach" if clean else "vat")]
                        lst.append((_bkey(f, src, lineno, i), text.strip()[:200]))
                        if len(lst) > 4 * K:
                            lst.sort()
                            del lst[K:]
    for k in ctx:
        ctx[k].sort()
        del ctx[k][K:]
    return cnt, dict(ctx)


def scan(src, path, dedupe):
    t0 = time.time()
    sha = hashlib.sha256()
    with open(path, "rb") as fb:
        for block in iter(lambda: fb.read(1 << 22), b""):
            sha.update(block)
    seen = set()
    total = distinct = 0

    def batches():
        nonlocal total, distinct
        buf = []
        with gzip.open(path, "rb") as fz:
            for lineno, raw in enumerate(fz, 1):
                total += 1
                h = hashlib.blake2b(raw.rstrip(b"\r\n"), digest_size=8).digest()
                first = h not in seen
                if first:
                    seen.add(h)
                    distinct += 1
                elif dedupe:
                    continue
                buf.append((lineno, first, ud.normalize("NFC", raw.decode("utf-8", "ignore").lower())))
                if len(buf) >= 20000:
                    yield (src, buf)
                    buf = []
        if buf:
            yield (src, buf)

    cnt, ctx = collections.Counter(), collections.defaultdict(list)
    with ProcessPoolExecutor(14, initializer=_init) as ex:
        for c, x in ex.map(_work, batches(), chunksize=1):
            cnt.update(c)
            for k, v in x.items():
                ctx[k].extend(v)
                ctx[k].sort()
                del ctx[k][K:]
    meta = {"file": os.path.basename(path), "sha256": sha.hexdigest(), "lines": total, "distinct_lines": distinct,
            "seconds": round(time.time() - t0)}
    return meta, cnt, ctx


def main():
    out_utf8()
    mf = json.loads((AT / "manifest.json").read_text(encoding="utf-8"))
    sha_mf = {v["sha256"] for v in mf["nguon_du_lieu"]}
    log, res, ctx_all = [], {}, {}
    for src, name, dedupe in (("sub", "sub-vi.txt.gz", False), ("web", "web-vi.txt.gz", True)):
        meta, cnt, ctx = scan(src, os.path.join(KHO_DIR, name), dedupe)
        meta["khop_manifest"] = meta["sha256"] in sha_mf
        log.append(f"{src}: {json.dumps(meta, ensure_ascii=False)}")
        print(log[-1], flush=True)
        res[src] = cnt
        ctx_all[src] = {f"{f}|{k}": v for (f, k), v in ctx.items()}
    rows = []
    for f in FORMS:
        s, w = res["sub"], res["web"]
        rows.append({"dang": f, "so_am_tiet": len(f.split()),
                     "sub_moi_dong": s[(f, "all")], "sub_moi_dong_sach": s[(f, "all_clean")],
                     "sub_dong_khac_sach": s[(f, "dist_clean")], "web_dong_khac": w[(f, "dist")],
                     "web_dong_khac_sach": w[(f, "dist_clean")]})
    write_tsv(HERE / f"{OUT_STEM}.tsv", list(rows[0].keys()), rows)
    log.append(f"dạng đã đếm: {len(FORMS)} (từ {len(PAIRS)} cặp, {os.path.basename(PAIRS_FILE)})")
    (HERE / f"{OUT_STEM}.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
    if NGU_CANH:
        with open(NGU_CANH, "w", encoding="utf-8") as fo:
            json.dump(ctx_all, fo, ensure_ascii=False)
    print("\n".join(log[-1:]))


if __name__ == "__main__":
    main()
