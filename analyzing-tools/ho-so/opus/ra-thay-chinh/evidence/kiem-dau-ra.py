"""Kiểm và chuẩn hóa định dạng mọi tệp văn bản trong thư mục ra-thay-chinh của Opus.

    python kiem-dau-ra.py [--sua]

Yêu cầu: UTF-8 không BOM, CRLF, không khoảng trắng cuối dòng, có dòng cuối. --sua: ghi lại tệp sai.
"""
import sys

from chung import OUT, out_utf8

out_utf8()
fix = "--sua" in sys.argv
bad = 0
for p in sorted(OUT.rglob("*")):
    if not p.is_file() or "__pycache__" in p.parts or p.suffix not in (".md", ".py", ".tsv", ".log", ".txt", ".json"):
        continue
    b = p.read_bytes()
    loi = []
    if b.startswith(b"\xef\xbb\xbf"):
        loi.append("BOM")
    t = b.decode("utf-8")
    lines = t.replace("\r\n", "\n").split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    else:
        loi.append("thiếu dòng cuối")
    if "\n" in t.replace("\r\n", ""):
        loi.append("LF lẻ")
    if any(l != l.rstrip(" \t") for l in lines):
        loi.append("khoảng trắng cuối dòng")
    if loi:
        bad += 1
        print(p.relative_to(OUT), ", ".join(loi))
        if fix:
            p.write_bytes(("\r\n".join(l.rstrip(" \t") for l in lines) + "\r\n").encode("utf-8"))
print("tệp lỗi:", bad, "(đã sửa)" if fix and bad else "")
