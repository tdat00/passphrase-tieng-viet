#!/usr/bin/env python3
"""Kiểm danh sách phát hành theo các mục C1–C8 của bộ tiêu chí (xem tieu-chi-thong-nhat.md).

    python check_wordlist.py

Đọc `wordlist.txt`, `labels.tsv`, `blocked_keys.tsv`, `spelling_families.tsv` trong thư mục này
và ba khối danh sách trong repo (`index.html`, `thong-tin.html`, `WordListAnalyze.md` mục 10).
Thoát 1 nếu có LỖI. CẢNH BÁO là chỗ cần người đọc lại, không chặn phát hành.
"""
import csv
import math
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
N = 7776
ALPHABET = "a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y".split()
RANK = {c: i for i, c in enumerate(ALPHABET)}
TONES = {"\u0300": 1, "\u0309": 2, "\u0303": 3, "\u0301": 4, "\u0323": 5}  # huyền hỏi ngã sắc nặng
LETTER = re.compile(r"^[aăâbcdđeêghiklmnoôơpqrstuưvxy]+$")
errors, warnings = [], []


def err(msg):
    errors.append(msg)


def strip(s):
    # Giống hàm bỏ dấu của app: NFD, bỏ dấu kết hợp, đ -> d
    return "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c)).replace("đ", "d").replace("Đ", "D")


def key(w):
    return strip(w).lower().replace(" ", "")


def untone(s):
    # Bỏ dấu thanh nhưng giữ chữ cái (ă, â, ê, ô, ơ, ư, đ)
    return unicodedata.normalize("NFC", "".join(c for c in unicodedata.normalize("NFD", s) if c not in TONES))


def o1(w):
    # O1: so từng âm tiết; trong âm tiết so chữ cái (bảng chữ Việt) rồi so thanh
    out = []
    for syl in w.split(" "):
        tone, base = 0, ""
        for ch in unicodedata.normalize("NFD", syl):
            if ch in TONES:
                tone = TONES[ch]
            else:
                base += ch
        out.append((tuple(RANK[c] for c in unicodedata.normalize("NFC", base)), tone))
    return tuple(out)


def tsv(name):
    with open(HERE / name, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def block(name, start):
    text = (REPO / name).read_text(encoding="utf-8")
    i = text.index(start)
    j = text.index("\n", i) + 1
    return text[j:text.index("```" if start.startswith("```") else "</script>", j)].splitlines()


def main():
    raw = (HERE / "wordlist.txt").read_bytes()
    # C1: mã hóa và định dạng
    if raw.startswith(b"\xef\xbb\xbf"):
        err("C1: wordlist.txt có BOM")
    if b"\r" in raw or not raw.endswith(b"\n"):
        err("C1: wordlist.txt phải dùng LF và có LF cuối")
    text = raw.decode("utf-8")
    if unicodedata.normalize("NFC", text) != text:
        err("C1: wordlist.txt chưa ở dạng NFC")
    lines = text.splitlines()
    if len(lines) != N:
        err(f"C1: có {len(lines)} dòng, cần {N}")
    pairs = []
    for i, line in enumerate(lines, 1):
        p = line.split("|")
        if len(p) != 2 or not p[1].strip():
            err(f"C1: dòng {i} không đúng dạng `từ|giải nghĩa`")
            continue
        pairs.append(p)
    words = [w for w, _ in pairs]

    # C2: H1 hình thức, H2 độ dài
    for w in words:
        blocks = w.split(" ")
        if any(not b or not LETTER.match(untone(b)) for b in blocks):
            err(f"C2: '{w}' có kí tự ngoài chữ cái tiếng Việt viết thường hoặc dấu cách thừa")
        n = len(key(w))
        if not 4 <= n <= 12 or not 1 <= len(blocks) <= 3:
            err(f"C2: '{w}' dài {n} chữ, {len(blocks)} khối (cần 4–12 chữ, 1–3 khối)")

    # C3: H4 duy nhất về mặt chữ và khóa, kể cả sau khi viết hoa chữ đầu
    for label, items in (("mặt chữ", words), ("khóa", [key(w) for w in words]),
                         ("viết hoa", [w[0].upper() + w[1:] for w in words])):
        dup = [x for x, c in Counter(items).items() if c > 1]
        if dup:
            err(f"C3: trùng {label}: {dup[:10]}")

    # C4: thứ tự O1, nhóm chữ cái liền mạch
    for a, b in zip(words, words[1:]):
        if o1(a) >= o1(b):
            err(f"C4: sai thứ tự O1: '{a}' trước '{b}'")
            break
    firsts = [strip(w)[0].upper() for w in words]
    runs = [x for i, x in enumerate(firsts) if i == 0 or x != firsts[i - 1]]
    if len(runs) != len(set(runs)):
        err("C4: nhóm chữ cái đầu không liền mạch")

    # C5: khóa bị chặn, họ chính tả
    keys = {key(w): w for w in words}
    labels_all = {r["tu"]: r for r in tsv("labels.tsv")}
    for r in tsv("blocked_keys.tsv"):
        if r["khoa"] in keys:
            err(f"C5: '{keys[r['khoa']]}' trùng khóa bị chặn {r['khoa']} ({r['ma']})")
    wset = set(words)
    for r in tsv("spelling_families.tsv"):
        hit = [x for x in (r["chuan"], r["bien_the"]) if x in wset]
        if not hit:
            continue
        v = r["ket_luan"]
        if v.startswith("LOAI") or v in ("CHO_LOAI", "CHO_NGHIA", "CHO_SAT_NGUONG"):
            err(f"C5: '{hit[0]}' thuộc họ chính tả {r['chuan']}/{r['bien_the']} ({v})")
        elif "THIEU_DU_LIEU" in v:
            signed = labels_all.get(hit[0], {}).get("chu_ky_hai_ben", "").split(";")
            if "H5" not in signed:
                err(f"C5: '{hit[0]}' thuộc họ thiếu dữ liệu {r['chuan']}/{r['bien_the']} ({v}) mà chưa có hai chữ ký H5")

    # C6: nhãn và hạn mức Q1–Q3
    labels = {w: r for w, r in labels_all.items() if r["trang_thai"] == "CHINH"}
    missing = [w for w in words if w not in labels]
    if missing:
        err(f"C6: thiếu nhãn: {missing[:10]}")
    nhan = Counter(labels[w]["nhan"] for w in words if w in labels)
    lop = Counter(labels[w]["lop"] for w in words if w in labels)
    if nhan.get("R2", 0) or set(nhan) - {"OK", "R1"}:
        err(f"C6: nhãn không hợp lệ: {dict(nhan)}")
    if nhan.get("R1", 0) > 388:
        err(f"C6: Q2 vượt: R1 = {nhan['R1']} > 388")
    if lop.get("F", 0) > 77:
        err(f"C6: Q3 vượt: lớp F = {lop['F']} > 77")

    # C7 (một phần): giải nghĩa không trùng, đúng hình thức tối thiểu
    defs = [d for _, d in pairs]
    dup = [d for d, c in Counter(defs).items() if c > 1]
    if dup:
        err(f"C7: {len(dup)} giải nghĩa trùng nhau")
    for w, d in pairs:
        if len(d) > 110 or not d[0].isupper() or not d.endswith("."):
            err(f"C7: giải nghĩa của '{w}' sai hình thức (≤110 kí tự, chữ hoa đầu, dấu chấm cuối)")

    # C8: đồng bộ ba khối trong repo
    start = '<script type="text/plain" id="wordlist">'
    if [l.strip().rstrip(",") for l in block("index.html", start) if l.strip()] != words:
        err("C8: khối #wordlist của index.html không khớp wordlist.txt")
    if [l.strip() for l in block("thong-tin.html", start) if l.strip()] != lines:
        err("C8: khối #wordlist của thong-tin.html không khớp wordlist.txt")
    doc = (REPO / "WordListAnalyze.md").read_text(encoding="utf-8")
    sec = doc[doc.index("## 10. Danh sách 7.776 từ phát hành"):]
    body = sec[sec.index("```text") + len("```text"):]
    body = body[:body.index("```")]
    if [l for l in body.splitlines() if l] != lines:
        err("C8: bản lưu ở mục 10 của WordListAnalyze.md không khớp wordlist.txt")

    # Thống kê
    blocks = Counter(len(w.split(" ")) for w in words)
    lengths = Counter(len(key(w)) for w in words)
    print(f"Số từ: {len(words)}; {math.log2(max(len(words), 1)):.2f} bit/từ; 6 từ: {6 * math.log2(max(len(words), 1)):.1f} bit")
    print("Số khối: " + ", ".join(f"{k}: {v}" for k, v in sorted(blocks.items())))
    print("Độ dài (chữ): " + ", ".join(f"{k}: {v}" for k, v in sorted(lengths.items())))
    print("Lớp: " + ", ".join(f"{k}: {v}" for k, v in sorted(lop.items())) + "; nhãn: " + ", ".join(f"{k}: {v}" for k, v in nhan.items()))
    for m in warnings:
        print("CẢNH BÁO | " + m)
    for m in errors:
        print("LỖI | " + m)
    print(f"Tổng: {len(errors)} lỗi, {len(warnings)} cảnh báo.")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
