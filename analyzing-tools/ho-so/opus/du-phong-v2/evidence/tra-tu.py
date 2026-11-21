"""Tra nhanh một danh sách từ: có trong danh sách chính, dự phòng, LOAI (D8), rổ P6, bảng P1, các lô L2–L3b, bảng đếm
OPUS hay chưa từng xuất hiện; in lý do ở P2/P4 nếu có. Dùng để tìm ứng viên "chưa từng vào rổ".

    python tra-tu.py <tệp mỗi dòng một từ> <tệp TSV ra>
"""
import collections
import sys
from chung import *

out_utf8()
words = list(dict.fromkeys(lines(sys.argv[1])))
main = {l.split("|")[0] for l in lines(AT / "wordlist.txt")}
res = set(lines(AT / "du-phong.txt"))
ng = {r["tu"]: r for r in rd(AT / "nguon-goc-giai-nghia.tsv")}
xh = {r["tu"]: r for r in rd(U / "xep-hang.tsv")}
p1 = p1_table()
oc = counts_opus()
lots = {}
for f in ["l2-ung-vien.tsv", "l2b-ung-vien.tsv", "l2c-ung-vien.tsv", "l3-ung-vien.tsv", "l2d-ung-vien.tsv", "l3b-de-cu-opus.tsv"]:
    for r in rd(U / f):
        lots[r["tu"]] = f
po = {r["tu"]: r for r in rd(U / "phieu-opus.tsv")}
pa = {r["tu"]: r for r in rd(U / "phieu-astra.tsv")}
allkeys = collections.defaultdict(list)
for w in main:
    allkeys[key(w)].append(("CHINH", w))
for w in res:
    allkeys[key(w)].append(("DU_PHONG", w))
rows = []
for w in words:
    k = key(w)
    where = []
    if w in main:
        where.append("CHINH")
    if w in res:
        where.append("DU_PHONG")
    if w in ng and ng[w]["trang_thai"] == "LOAI":
        where.append("LOAI:" + ng[w]["cong_loai"])
    if w in xh:
        where.append("XEP_HANG:" + xh[w]["nhan"] + "/" + xh[w]["vao"])
    if w in lots:
        where.append("LO:" + lots[w])
    if w in p1:
        p = p1[w]
        where.append(f'P1:{p["nguon"]}:{p["ket_qua_uv_P2"]}:{",".join(p["ly_do_cong"] or [])}')
    if w in po or w in pa:
        where.append(f'P4:O={po.get(w, {}).get("nhan", "")}/{po.get(w, {}).get("cong", "")},A={pa.get(w, {}).get("nhan", "")}/{pa.get(w, {}).get("cong", "")}')
    if w in oc and w not in p1:
        where.append("DEM_OPUS")
    other = [f"{s}:{x}" for s, x in allkeys.get(k, []) if x != w]
    c = oc.get(w, {})
    rows.append({"tu": w, "khoa": k, "so_chu": len(k), "noi_co_mat": "|".join(where) or "CHUA_TUNG_VAO_RO",
                 "trung_khoa": ",".join(other), "sub_sach": c.get("sub_sach", ""), "web_sach": c.get("web_sach", "")})
write_tsv(sys.argv[2], ["tu", "khoa", "so_chu", "noi_co_mat", "trung_khoa", "sub_sach", "web_sach"], rows)
print(len(rows), "từ;", sum(1 for r in rows if r["noi_co_mat"] == "CHUA_TUNG_VAO_RO"), "chưa từng vào rổ")
