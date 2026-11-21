"""Kiểm đầu ra của Opus (vòng 1): hai bảng TSV và quy ước tệp. Chỉ đọc; thoát 1 nếu có lỗi.

    python kiem-dau-ra.py
"""
import collections
import sys
from chung import *

out_utf8()
err = []
res = lines(AT / "du-phong.txt")
main = [l.split("|") for l in lines(AT / "wordlist.txt")]
main_keys = {key(w) for w, _ in main}
res_keys = {key(w) for w in res}
blocked = {r["khoa"] for r in rd(AT / "blocked_keys.tsv")}
fam_bad = set()
for r in rd(AT / "spelling_families.tsv"):
    if r["ket_luan"].startswith("LOAI") or r["ket_luan"].startswith("CHO"):
        fam_bad |= {r["chuan"], r["bien_the"]}

# 1. Bảng phân loại 205 dự phòng
cls = rd(OUT / "du-phong-205-phan-loai-opus.tsv", True)
if [r["tu"] for r in cls] != res:
    err.append("phân loại: cột từ không trùng du-phong.txt theo đúng thứ tự")
if any(r["bac"] not in "ABCD" or len(r["bac"]) != 1 for r in cls):
    err.append("phân loại: bậc ngoài A/B/C/D")
if any(r["ngan"] not in ("OK_KHONG_F", "OK_F") for r in cls):
    err.append("phân loại: ngăn không hợp lệ")
if any(r["bac"] == "A" and r["giai_nghia"] != "CO" for r in cls):
    err.append("phân loại: bậc A mà chưa có giải nghĩa")
cnt = collections.Counter((r["ngan"], r["bac"]) for r in cls)
print("bậc × ngăn:", dict(sorted(cnt.items())))

# 2. Bảng đề cử thêm
hm = rd(OUT / "de-cu-them-opus.tsv", True)
ks = [key(r["tu"]) for r in hm]
if not 100 <= len(hm) <= 300:
    err.append(f"đề cử: {len(hm)} dòng, ngoài 100–300")
if len(set(ks)) != len(ks):
    err.append("đề cử: trùng khóa trong bảng")
for r, k in zip(hm, ks):
    w = r["tu"]
    if k in main_keys or k in res_keys:
        err.append(f"đề cử: {w} trùng khóa danh sách chính/dự phòng")
    if k in blocked:
        err.append(f"đề cử: {w} trùng khóa bị chặn")
    if not (4 <= len(k) <= 12 and 1 <= len(w.split(" ")) <= 3):
        err.append(f"đề cử: {w} sai độ dài/số khối")
    if w in fam_bad:
        err.append(f"đề cử: {w} thuộc họ chính tả bị loại/chờ")
print("đề cử:", len(hm), dict(collections.Counter(r["nhom"] for r in hm)))

# 3. Không chép câu giải nghĩa nào (chính hay dự phòng) vào hồ sơ của Opus
glosses = {g for _, g in main} | {r["giai_nghia"] for r in rd(U / "p7-v4-du-phong-168-co-nghia-cho-duyet.tsv")}
files = [p for p in OUT.rglob("*") if p.is_file() and not any(part.startswith("_") for part in p.relative_to(OUT).parts)]
for p in files:
    text = p.read_bytes().decode("utf-8", errors="replace")
    hits = [g for g in glosses if len(g) > 25 and g in text]
    if hits:
        err.append(f"{p.name}: có {len(hits)} câu giải nghĩa")

# 4. Quy ước tệp: UTF-8 không BOM, CRLF, dòng cuối, không khoảng trắng cuối dòng
for p in files:
    b = p.read_bytes()
    if b.startswith(b"\xef\xbb\xbf"):
        err.append(f"{p.name}: có BOM")
    if not b.endswith(b"\r\n"):
        err.append(f"{p.name}: không kết thúc bằng CRLF")
    if b.replace(b"\r\n", b"").count(b"\n") or b.replace(b"\r\n", b"").count(b"\r"):
        err.append(f"{p.name}: lẫn kiểu xuống dòng")
    if any(l != l.rstrip() for l in b.decode("utf-8").split("\r\n")):
        err.append(f"{p.name}: có khoảng trắng cuối dòng")
print("tệp đã kiểm:", len(files))
for e in err:
    print("LỖI |", e)
print(f"Tổng: {len(err)} lỗi.")
sys.exit(1 if err else 0)
