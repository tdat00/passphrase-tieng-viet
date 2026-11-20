#!/usr/bin/env python3
"""D6 cho người soát quyền, không cấp công cụ/hồ sơ này cho người viết.

    python -B d6-kiem.py --input giai-nghia-gop-v1.tsv --log d6-log.tsv --meta d6-run.json
    python -B d6-kiem.py --self-test

Đầu vào TSV tách tab: tu, giai_nghia, các cột bổ sung tùy chọn (lo, luot_viet, co...).
Có thể nêu nhiều tệp gộp hoặc một phần cần tái kiểm, không nhập trùng từ trong cùng lượt.
Không tự tìm tệp, không đọc/ghi vào thư mục lo-XX. Log không chứa giải nghĩa hay dải trùng.
0 = mọi mục PASS; 1 = VIET_LAI; 2 = thiếu/lỗi tham chiếu, dữ liệu hoặc CHUA_KIEM.
D6 là kiểm kỹ thuật, không chứng minh tính nguyên tác; không phát hiện được việc dịch ý.
"""
import argparse
import csv
import difflib
import gzip
import hashlib
import io
import json
import os
import re
import sys
import unicodedata as ud
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

VERSION = "D6-1.0"
SOURCE_IDS = ("OPUS", "ASTRA", "WIKT_VI", "GUIDE", "FAMILIES")
HEADER = ("tu", "lo", "luot_viet", "tep_vao", "dong", "sha256_giai_nghia", "so_token",
          "ket_qua", "ma", "chung_cu", "sha256_bo_tham_chieu", "sha256_script", "run_id")
TONE = "\u0300\u0309\u0303\u0301\u0323"
SEP = re.compile(r"[\s\-\u2010\u2011\u2012\u2013\u2014]+")
FENCE = re.compile(r"^[ \t]*```text[ \t]*$", re.I)
END_FENCE = re.compile(r"^[ \t]*```[ \t]*$")
BREAK = re.compile(r"[.!?…]+[”’»\"')\]]*(?=\s|$)")


class Invalid(Exception):
    """Thông báo không mang văn bản của nghĩa tham chiếu."""


def json_bytes(data):
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(b):
    return hashlib.sha256(b).hexdigest()


def file_hash(p):
    with p.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def safe_path(p):
    p = Path(p).resolve()
    if any(re.fullmatch(r"lo[-_]\d+(?:[-_].*)?", part, re.I) for part in p.parent.parts):
        raise Invalid("THU_MUC_CUA_LUOT_VIET: chỉ được dùng bản gộp ở ngoài các thư mục lô.")
    return p


def tokens(text):
    # isalpha kiểm đúng các loại Unicode L*: số ²/Ⅳ không lọt vào token chữ.
    text = ud.normalize("NFC", ud.normalize("NFC", text).lower())
    return tuple("".join(c if c.isalpha() else " " for c in text).split())


def head_parts(head):
    """Giữ đ và các dấu; chỉ quy đồng hai vị trí của cùng thanh trong oa/oe/uy."""
    parts = []
    for syllable in SEP.split(ud.normalize("NFC", head.lower().strip())):
        if not syllable:
            continue
        groups = []
        for ch in ud.normalize("NFD", syllable):
            if ud.combining(ch) and groups:
                groups[-1] += ch
            else:
                groups.append(ch)
        for i in range(len(groups) - 1):
            a, b = groups[i:i + 2]
            mark = "".join(c for c in a if c in TONE)
            bare = ud.normalize("NFC", "".join(c for c in a + b if c not in TONE))
            if bare in ("oa", "oe", "uy") and len(mark) == 1 and not any(c in TONE for c in b):
                groups[i] = "".join(c for c in a if c not in TONE)
                groups[i + 1] = b + mark
        parts.append(ud.normalize("NFC", "".join(groups)))
    return tuple(parts)


class Families:
    def __init__(self, pairs=()):
        self.parents = {}
        self.max_blocks = 1
        for a, b in pairs:
            aa, bb = head_parts(a), head_parts(b)
            self.max_blocks = max(self.max_blocks, len(aa), len(bb))
            x, y = "".join(aa), "".join(bb)
            if not x or not y:
                raise Invalid("HO_CO_DANG_TRONG")
            ra, rb = self.root(x), self.root(y)
            m = min(ra, rb)
            self.parents[ra] = self.parents[rb] = m
        for k in list(self.parents):
            self.parents[k] = self.root(k)

    def root(self, s):
        seen = []
        while s in self.parents and self.parents[s] != s:
            seen.append(s)
            s = self.parents[s]
        for v in seen:
            self.parents[v] = s
        return s

    @lru_cache(maxsize=131072)
    def keys(self, head):
        parts = head_parts(head)
        if not parts:
            return frozenset()
        joined = "".join(parts)
        direct = self.parents.get(joined, joined)
        # Cùng vị trí thành tố, giữ nguyên phần còn lại: giầy da ~ giày da, không ~ giày vải.
        mapped = []
        i = 0
        while i < len(parts):
            for n in range(min(self.max_blocks, len(parts) - i), 0, -1):
                span = "".join(parts[i:i + n])
                if span in self.parents and n < len(parts):
                    mapped.append(self.parents[span])
                    i += n
                    break
            else:
                mapped.append(parts[i])
                i += 1
        c = "".join(mapped)
        return frozenset((direct, self.parents.get(c, c)))


@dataclass(frozen=True)
class Entry:
    word: str
    gloss: str
    lot: str = ""
    turn: str = ""
    file: str = ""
    line: int = 0


def sentences(s):
    start = 0
    for m in BREAK.finditer(s):
        piece = s[start:m.end()].strip()
        if piece:
            yield piece
        start = m.end()
    if s[start:].strip():
        yield s[start:].strip()


def table_cells(text):
    cells, cell, code, escaped = [], [], False, False
    for c in text.strip().strip("|"):
        if c == "|" and not code and not escaped:
            cells.append("".join(cell).strip())
            cell = []
        else:
            if c == "`" and not escaped:
                code = not code
            cell.append(c)
        escaped = c == "\\" and not escaped
    return cells + ["".join(cell).strip()]


def guide_rows(text):
    """Một đoạn ngắn/câu/ô, không tạo dải nhân tạo nối hai gạch đầu dòng, ô bảng hoặc hai câu."""
    lines = text.splitlines()
    blocks, paragraph = [], []
    first, fenced = 0, False

    def flush():
        if paragraph:
            blocks.append((first, " ".join(paragraph)))
            paragraph.clear()

    for n, line in enumerate(lines, 1):
        v = line.strip()
        if v.startswith("```"):
            flush()
            fenced = not fenced
        elif not v:
            flush()
        elif fenced:
            flush()
            for cell in v.split("\t"):
                blocks.append((n, cell))
        elif v.startswith("|"):
            flush()
            cols = table_cells(v)
            is_sep = lambda c: bool(re.fullmatch(r"[-: ]+", c))
            if all(is_sep(c) for c in cols):
                continue
            if n < len(lines) and lines[n].lstrip().startswith("|") and all(is_sep(c) for c in table_cells(lines[n])):
                continue
            blocks.extend((n, cell) for cell in cols)
        elif re.match(r"^#{1,6}\s+", v):
            flush()  # Tiêu đề là siêu dữ liệu, không phải câu của hướng dẫn.
        elif re.match(r"^(?:[-*+]|\d+[.)])\s+", v):
            flush()
            first = n
            paragraph.append(re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", v))
        else:
            if not paragraph:
                first = n
            paragraph.append(v)
    flush()
    seq = Counter()
    for n, s in blocks:
        s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
        s = s.replace("**", "").replace("`", "")
        for part in sentences(s):
            if tokens(part):
                seq[n] += 1
                yield "", part, f"L{n}.{seq[n]}"


def archive_rows(text, spec, info):
    ls = text.splitlines()
    starts = [i for i, line in enumerate(ls) if FENCE.fullmatch(line)]
    if len(starts) != 1:
        raise Invalid("SO_KHOI_LUU_TRU_KHAC_1")
    i = starts[0]
    stop = next((k for k in range(i + 1, len(ls)) if END_FENCE.fullmatch(ls[k])), None)
    if stop is None:
        raise Invalid("KHOI_LUU_TRU_KHONG_DONG")
    body = ls[i + 1:stop]
    info["body_sha256"] = digest(("\n".join(body) + "\n").encode())
    if info["body_sha256"] != spec["body_sha256"] or len(body) != spec["rows"]:
        raise Invalid("BAM_HOAC_SO_DONG_LUU_TRU_KHAC")
    heads = set()
    for j, line in enumerate(body, 1):
        if line.count("|") != 1:
            raise Invalid("DONG_LUU_TRU_SAI_COT")
        word, gloss = line.split("|")
        if not word.strip() or not gloss.strip() or word in heads:
            raise Invalid("DONG_LUU_TRU_TRONG_HOAC_TRUNG_TU")
        heads.add(word)
        yield word, gloss, f"B{j}"


def wiki_rows(path, counters):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            obj = json.loads(line)
            if not isinstance(obj, dict):
                raise Invalid("WIKT_SAI_SCHEMA")
            if obj.get("lang_code") != "vi":
                continue
            counters["vi_entries"] += 1
            w, senses = obj.get("word"), obj.get("senses", [])
            if not isinstance(w, str) or not w or not isinstance(senses, list):
                raise Invalid("WIKT_SAI_DAU_MUC")
            for i, sense in enumerate(senses, 1):
                if not isinstance(sense, dict) or not isinstance(sense.get("glosses", []), list):
                    raise Invalid("WIKT_SAI_TRUONG_NGHIA")
                for j, gloss in enumerate(sense.get("glosses", []), 1):
                    if not isinstance(gloss, str):
                        raise Invalid("WIKT_NGHIA_KHONG_PHAI_CHUOI")
                    if gloss.strip():
                        yield w, gloss, f"L{n}.S{i}.G{j}"


class Index:
    """Lập chỉ mục lời mới, quét từng đơn vị nguồn một lần. Lưu bằng chứng định vị, không lưu văn bản vào log."""
    def __init__(self, entries, families):
        self.families = families
        self.texts = [tokens(e.gloss) for e in entries]
        self.exact, self.grams, self.same = defaultdict(list), defaultdict(list), defaultdict(list)
        self.hits = [{} for _ in entries]
        for i, (e, t) in enumerate(zip(entries, self.texts)):
            if not t:
                continue
            self.exact[t].append(i)
            for g in dict.fromkeys(t[k:k + 6] for k in range(len(t) - 5)):
                self.grams[g].append(i)
            if len(t) >= 5:
                for fam in families.keys(e.word):
                    self.same[fam].append(i)

    def observe(self, head, t, source, pointer):
        if not t:
            return
        for i in self.exact.get(t, ()):
            self.hits[i].setdefault(("D6A", source), {"ref": pointer})
        for at in range(len(t) - 5):
            for i in self.grams.get(t[at:at + 6], ()):
                self.hits[i].setdefault(("D6B", source), {"ref": pointer, "ref_token": at + 1, "n": 6})
        targets = {i for k in self.families.keys(head) for i in self.same.get(k, ())} if head else ()
        for i in targets:
            u = self.texts[i]
            denom = len(t) + len(u)
            if 200 * min(len(t), len(u)) < 78 * denom:
                continue
            # ratio = 2M/(|u|+|t|); so nguyên để biên đúng 0,78 vẫn bị chặn, không làm tròn trước.
            sm = difflib.SequenceMatcher(None, u, t, autojunk=False)
            numer = 2 * sum(s.size for s in sm.get_matching_blocks())
            if 100 * numer >= 78 * denom:
                key = ("D6C", source)
                old = self.hits[i].get(key)
                if old is None or numer * old["den"] > old["num"] * denom:
                    self.hits[i][key] = {"ref": pointer, "num": numer, "den": denom,
                                         "ratio": f"{numer / denom:.6f}"}

    def reference(self, head, text, source, pointer, canonical):
        t = tokens(text)
        canonical.update(json_bytes([head, t]) + b"\n")
        if not t:
            return 0
        self.observe(head, t, source, pointer)
        # Không bỏ sót nguyên câu ngắn hoặc gần trùng một câu của lời giải dài hơn.
        # Chính bản đầy đủ phía trên vẫn bắt được dải sáu đi qua dấu câu trong cùng một nghĩa.
        if source != "GUIDE":
            for j, part in enumerate(sentences(text), 1):
                u = tokens(part)
                if u and u != t:
                    self.observe(head, u, source, f"{pointer}.C{j}")
        return 1


def load_inputs(paths):
    seen, accepted, file_ids, bad = set(), [], [], {}
    for path in paths:
        p = safe_path(path)
        file_ids.append({"file": p.name, "sha256": file_hash(p)})
        with p.open(encoding="utf-8-sig", newline="") as f:
            r = csv.DictReader(f, delimiter="\t", strict=True)
            if not r.fieldnames or len(set(r.fieldnames)) != len(r.fieldnames) or not {"tu", "giai_nghia"} <= set(r.fieldnames):
                raise Invalid("TSV_VAO_THIEU_HOAC_TRUNG_COT")
            for row in r:
                w, g = row.get("tu"), row.get("giai_nghia")
                if None in row or not isinstance(w, str) or not w or g is None or any(c in w for c in "\r\n\t"):
                    raise Invalid(f"TSV_VAO_HONG:{p.name}:L{r.line_num}")
                if w in seen:
                    raise Invalid(f"TRUNG_DAU_MUC_VAO:{p.name}:L{r.line_num}")
                seen.add(w)
                if not tokens(g):
                    bad[len(accepted)] = "NGHIA_KHONG_CO_TOKEN"
                accepted.append(Entry(w, g, row.get("lo", ""), row.get("luot_viet", ""), p.name, r.line_num))
    if not accepted:
        raise Invalid("KHONG_CO_DONG_DAU_VAO")
    return accepted, file_ids, bad


def execute(entries, manifest, basedir, pins, bad):
    sources, problems, details, refs = {}, [], {}, {}

    def problem(s, e):
        desc = str(e) if isinstance(e, Invalid) else type(e).__name__
        problems.append(f"{s}:{desc}")
        details.setdefault(s, {})["error"] = desc

    try:
        if manifest.get("schema") != 1 or set(manifest["sources"]) != set(SOURCE_IDS):
            raise Invalid("DANH_MUC_NGUON_KHONG_DU")
        for s in SOURCE_IDS:
            spec = manifest["sources"][s]
            p = safe_path(basedir / spec["path"])
            details[s] = {"expected_sha256": spec["sha256"]}
            try:
                h = file_hash(p)
                details[s]["actual_sha256"] = h
                if not re.fullmatch(r"[a-f0-9]{64}", spec["sha256"]) or h != spec["sha256"]:
                    raise Invalid("BAM_KHONG_KHOP")
                if s in pins and spec.get("body_sha256", h) != pins[s]:
                    raise Invalid("KHAC_SNAPSHOT_DA_KY")
                sources[s] = p
            except (OSError, Invalid) as e:
                problem(s, e)
    except (OSError, KeyError, TypeError, Invalid) as e:
        problem("MANIFEST", e)
    pairs = []
    if "FAMILIES" in sources:
        try:
            with sources["FAMILIES"].open(encoding="utf-8", newline="") as f:
                r = csv.DictReader(f, delimiter="\t", strict=True)
                if r.fieldnames != ["dang_A", "dang_B", "can_cu"]:
                    raise Invalid("HO_SAI_COT")
                for v in r:
                    if not v["can_cu"] or None in v:
                        raise Invalid("HO_THIEU_CAN_CU")
                    pairs.append((v["dang_A"], v["dang_B"]))
            if len(pairs) != manifest["sources"]["FAMILIES"]["pairs"]:
                raise Invalid("HO_SAI_SO_LUONG")
            details["FAMILIES"]["pairs"] = len(pairs)
        except (OSError, UnicodeError, KeyError, csv.Error, Invalid) as e:
            problem("FAMILIES", e)
    try:
        ix = Index(entries, Families(pairs))
    except (Invalid, AttributeError) as e:
        problem("FAMILIES", e)
        ix = Index(entries, Families())
    for s in SOURCE_IDS[:-1]:
        if s not in sources:
            continue
        meta = details[s]
        try:
            spec, p = manifest["sources"][s], sources[s]
            hasher = hashlib.sha256()
            cnt = Counter()
            if s in ("ASTRA", "OPUS"):
                refs = archive_rows(p.read_text(encoding="utf-8-sig"), spec, meta)
            elif s == "GUIDE":
                refs = guide_rows(p.read_text(encoding="utf-8-sig"))
            else:
                refs = wiki_rows(p, cnt)
            n = with_tokens = 0
            for w, g, pointer in refs:
                n += 1
                with_tokens += ix.reference(w, g, s, pointer, hasher)
            if n == 0 or with_tokens == 0:
                raise Invalid("TAP_THAM_CHIEU_RONG")
            if s == "WIKT_VI" and (n != spec["glosses"] or spec.get("head_lang") != "vi"):
                raise Invalid("WIKT_SAI_SO_NGHIA_HOAC_NGON_NGU")
            meta.update(**cnt, units=n, units_with_letters=with_tokens, canonical_sha256=hasher.hexdigest())
        except (OSError, EOFError, ValueError, UnicodeError, KeyError, TypeError, Invalid) as e:
            problem(s, e)
    hset = digest(json_bytes({k: {a: v for a, v in d.items() if a in
                  ("actual_sha256", "canonical_sha256", "body_sha256", "pairs", "units")} for k, d in details.items()}))
    rows = []
    for i, (e, t, hits) in enumerate(zip(entries, ix.texts, ix.hits)):
        evidence = {f"{code}:{s}": v for (code, s), v in sorted(hits.items())}
        codes = sorted({code for code, s in hits})
        if problems:
            codes.append("THAM_CHIEU_LOI")
        if i in bad:
            codes.append(bad[i])
        status = "CHUA_KIEM" if problems or i in bad else "VIET_LAI" if codes else "PASS"
        rows.append((e.word, e.lot, e.turn, e.file, e.line, digest(json_bytes(t)), len(t), status,
                     ";".join(codes), json_bytes(evidence).decode(), hset))
    return rows, details, hset, problems


def self_test():
    cases = []

    def ck(name, ok):
        if not ok:
            raise AssertionError(name)
        cases.append(name)

    def c(head, candidate, other, ref, expected, pairs=(), source="OPUS"):
        i = Index([Entry(head, candidate)], Families(pairs))
        i.reference(other, ref, source, "I1", hashlib.sha256())
        codes = {code for code, _ in i.hits[0]}
        ck(f"{len(cases) + 1}:{head}", codes == set(expected))

    c("a", "ĐỎ!", "b", ud.normalize("NFD", "đỏ"), ["D6A"])
    c("a", "đỏ", "b", "do", [])
    c("a", "lá non", "b", "Khác màu. Lá non.", ["D6A"])
    c("a", "bắc lá nâu mềm trời non tím", "b", "cam lá nâu mềm trời non tím", ["D6B"])
    c("a", "bắc lá nâu mềm trời non tím", "b", "cam lá nâu mềm trời non trắng", [])
    c("a", "lá đỏ hoa tươi tán mềm", "a", "lá đỏ quả tươi tán mềm", ["D6C"])
    c("áo giấy", "lá đỏ hoa tươi tán mềm", "áo giấi", "lá đỏ quả tươi tán mềm", ["D6C"],
      [("giấy", "gíấy"), ("gíấy", "giấi")])
    c("hoá màu", "lá đỏ hoa tươi tán mềm", "hóa màu", "lá đỏ quả tươi tán mềm", ["D6C"])
    c("nói thật", "lá đỏ hoa tươi tán mềm", "nội thất", "lá đỏ quả tươi tán mềm", [])
    c("a", "lá đỏ tán mềm", "a", "lá đỏ tán mềm trắng", [])
    ck("chỉ chữ cái", tokens("a²bⅣc_đ.ô") == ("a", "b", "c", "đ", "ô"))
    letters = [chr(0x4e00 + j) for j in range(50)]
    for matches, expected in ((39, True), (38, False)):
        orig = [v if j * matches // 50 < (j + 1) * matches // 50 else chr(0x5200 + j)
                for j, v in enumerate(letters)]
        i = Index([Entry("áo", " ".join(letters))], Families())
        i.observe("áo", tuple(orig), "OPUS", "1")
        ck(f"biên {matches}/50", (("D6C", "OPUS") in i.hits[0]) == expected)
    parsed = list(guide_rows("# Siêu dữ liệu\n\nMột câu. Vế khác.\n\n| H | K |\n|---|---|\n| `da` | `bàn lá` |\n"))
    ck("ô bảng và câu thứ hai", [tokens(g) for _, g, _ in parsed] == [("một", "câu"), ("vế", "khác"), ("da",), ("bàn", "lá")])
    ck("không nhập chung ô", not any(tokens(g) == ("da", "bàn", "lá") for _, g, _ in parsed))
    ck("không gộp đầu mục sau bỏ dấu", not Families().keys("bàn là") & Families().keys("bán lạ"))
    try:
        safe_path(Path("giai-nghia-v1") / "lo-02" / "lo-02.tsv")
    except Invalid:
        ck("chỉ làm việc trên bản gộp", True)
    else:
        ck("chỉ làm việc trên bản gộp", False)
    # Tất cả fixture đều là dữ liệu tự sinh, tái tạo trong RAM, không đụng tới hồ sơ thật.
    from unittest.mock import patch
    fname = {"OPUS": "x-opus", "ASTRA": "x-astra", "FAMILIES": "x-family", "WIKT_VI": "x-wiki", "GUIDE": "x-guide"}
    body = "hoa|Nhành pha sắc tiếp qua sân.\n"
    archive = ("# Mô phỏng\n```text\n" + body + "```\n").encode()
    wiki_raw = [dict(lang_code="en", word="bàn", senses=[{"glosses": ["tên ngoài"]}]),
                dict(lang_code="vi", word="cánh", senses=[{"glosses": ["câu thử riêng"], "examples": [{"text": "không nhập"}]}])]
    buffers = dict(zip(fname.values(), [archive, archive, b"dang_A\tdang_B\tcan_cu\n",
                         gzip.compress(b"\n".join(json_bytes(x) for x in wiki_raw)),
                         "Câu chỉ để thử. Đoạn thứ hai.".encode()]))
    conf = {"schema": 1, "sources": {s: {"path": v, "sha256": digest(buffers[v])} for s, v in fname.items()}}
    for s in ("OPUS", "ASTRA"):
        conf["sources"][s].update(body_sha256=digest(body.encode()), rows=1)
    conf["sources"]["FAMILIES"]["pairs"] = 0
    conf["sources"]["WIKT_VI"].update(head_lang="vi", glosses=1)
    targets = [Entry("g", w) for w in ("không nhập", "đoạn thứ hai", "câu thử riêng", "", "tên ngoài")]

    def mocked_open(p, mode="r", *args, **kwargs):
        if p.name not in buffers:
            raise FileNotFoundError(p.name)
        data = io.BytesIO(buffers[p.name])
        return data if "b" in mode else io.TextIOWrapper(data, encoding=kwargs.get("encoding", "utf-8"))

    gzipopen = gzip.open
    with patch.object(Path, "open", mocked_open), patch.object(gzip, "open", lambda p, *a, **k: gzipopen(io.BytesIO(buffers[p.name]), *a, **k)):
        def sim():
            return execute(targets, conf, Path.cwd(), {}, {3: "NGHIA_KHONG_CO_TOKEN"})
        rows, _, _, err = sim()
        ck("wiki lọc ngôn ngữ và ví dụ, nhận câu guide, mục trống", not err and
           [r[7] for r in rows] == ["PASS", "VIET_LAI", "VIET_LAI", "CHUA_KIEM", "PASS"])
        del buffers[fname["ASTRA"]]
        rows, _, _, err = sim()
        ck("thiếu một nguồn", bool(err) and all(r[7] == "CHUA_KIEM" for r in rows))
        buffers[fname["ASTRA"]] = b"invalid"
        rows, _, _, err = sim()
        ck("sai băm fail-closed", bool(err) and all(r[7] == "CHUA_KIEM" for r in rows))
    print(f"{VERSION}: {len(cases)} ca tổng hợp đạt.")


PINS = {"OPUS": "97d0b2fba487118029a83cd4aebd1c45248c3a1a3a5282cf5bb3ef506e56da0d",
        "ASTRA": "dfd74f433bb77faf2d9033800c58dccdb54adcb5be8a1580ed90cb63c8744f8e",
        "WIKT_VI": "1f0abd21982660b5fc2eff5eb3fbacbed2d9fe8f476af794dbed0d927ffb8187",
        "GUIDE": "9eddcf71042f3c9efefdc90b0b2b3d28756809b8b5c428fda4f94a26a5a5da8f"}


def cli():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--self-test", action="store_true")
    a.add_argument("--input", type=Path, nargs="+")
    a.add_argument("--log", type=Path, default=Path("d6-log.tsv"))
    a.add_argument("--meta", type=Path, default=Path("d6-run.json"))
    ns = a.parse_args()
    if ns.self_test:
        self_test()
        return 0
    if not ns.input:
        a.error("cần --input hoặc --self-test")
    home = Path(__file__).resolve().parent
    manifest_path = home / "d6-tham-chieu.json"
    log, meta = safe_path(ns.log), safe_path(ns.meta)
    if log == meta or {log, meta} & {safe_path(p) for p in [manifest_path, Path(__file__), *ns.input]}:
        raise Invalid("DICH_GHI_TRUNG_NGUON_HOAC_TRUNG_NHAU")
    meta_data = {"version": VERSION, "script_sha256": file_hash(Path(__file__)), "started_utc": datetime.now(timezone.utc).isoformat(),
                 "python": sys.version.split()[0], "unicode": ud.unidata_version, "manifest_sha256": None}
    try:
        doc = json.loads(manifest_path.read_text(encoding="utf-8"))
        meta_data["manifest_sha256"] = file_hash(manifest_path)
    except (OSError, ValueError) as e:
        doc = {}
        meta_data["manifest_error"] = type(e).__name__
    entries, file_ids, bad = load_inputs(ns.input)
    rows, detail, sethash, errs = execute(entries, doc, home, PINS, bad)
    run = digest(json_bytes([VERSION, meta_data["script_sha256"], meta_data["manifest_sha256"], sethash, file_ids]))
    with log.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(HEADER)
        w.writerows((*r, meta_data["script_sha256"], run) for r in rows)
    counts = dict(Counter(r[7] for r in rows))
    codes = Counter(c for r in rows for c in r[8].split(";") if c)
    meta_data.update(run_id=run, sources=detail, input=file_ids, reference_set_sha256=sethash, rows=len(rows), status=counts,
                     codes=dict(codes), issues=errs, log_sha256=file_hash(log), finished_utc=datetime.now(timezone.utc).isoformat())
    meta.write_text(json.dumps(meta_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"rows": len(rows), "statuses": counts, "codes": codes, "issues": errs, "run_id": run}, ensure_ascii=False))
    return 2 if "CHUA_KIEM" in counts else 1 if "VIET_LAI" in counts else 0


if __name__ == "__main__":
    try:
        raise SystemExit(cli())
    except Invalid as exc:
        print("CHUA_KIEM: " + str(exc), file=sys.stderr)
        raise SystemExit(2)