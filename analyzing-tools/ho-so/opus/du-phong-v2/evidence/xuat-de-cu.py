"""Bước 5: xuất bảng đề cử thêm cuối cùng (../de-cu-them-opus.tsv) từ evidence/de-cu-ung-vien.tsv và de-cu-hnd.tsv.

    python xuat-de-cu.py
"""
import collections
from chung import *

out_utf8()
uv = [r for r in rd(HERE / "de-cu-ung-vien.tsv", True) if not r["loai_vi"]]
hnd = {r["tu"]: r for r in rd(HERE / "de-cu-hnd.tsv", True)}
k132 = {r["tu"]: r for r in rd(U / "p7-v3-khau-tru-132-theo-P0-astra.tsv")}
GHI_CHU = {
    "bao tử": "H7: khóa baotu trùng báo tử (nhóm 4), PPM gộp 0,385 ≥ 0,3 nhưng không có trong canh-bao-khong-dau.tsv: phải đọc K1/K2 trước khi xét lại",
    "tần số": "H7: khóa tanso trùng tận số (cái chết), PPM gộp 0,21 dưới mốc còi; ghi để người đọc biết",
    "phân tử": "Khóa trùng phần tử; không thuộc nhóm đỏ",
    "ớt đỏ": "Cần xét X (tổ hợp tự do) ở P4", "nắng ấm": "Cần xét X (tổ hợp tự do) ở P4",
    "bánh sinh nhật": "12 chữ, đúng mức trần H2", "bánh củ cải": "H8 sát mốc: 15 lượt web sạch (0,100 PPM theo mẫu số 149.860.716; L2D ghi YEU theo mẫu số khác)",
    "chia": "K2 đã đủ hai chữ ký", "con dấu": "Khóa trùng con dâu, còn đâu; lành",
    "chạng vạng": "H5: HND có dạng choạng vạng (khác khóa) chưa từng được đếm; cần đo trước khi xét lại",
}
D7_CHAN = {"côn trùng", "mùa đông", "việc làm", "bánh ngọt", "xe điện", "lục địa", "châu lục", "vuông", "tục ngữ", "chữ hoa"}
rows = []
for r in uv:
    w, g = r["tu"], r["nhom"]
    if g == "DC1":
        ngan = "OK_F" if r["lop"] == "F" else "OK_KHONG_F"
        uu = 2 if (ngan == "OK_F" or r["ly_do_chua_chon"].endswith("DU_PHONG")) else 1
    elif g == "DC2":
        ngan, uu = "R1_KHONG_F", 2
    elif g == "DC3":
        ngan, uu = "CHUA_CHAM", 2
    else:
        ngan, uu = "CHUA_CHAM", 3
    note = []
    if g == "DC1" and w in D7_CHAN:
        note.append("Câu cũ trượt D7 (nội dung); từ không có vấn đề")
    if w in GHI_CHU:
        note.append(GHI_CHU[w])
    h = hnd.get(w, {})
    if g in ("DC1", "DC2"):
        xm = "V: khóa, H1–H4, K0/K1/K2, họ H5 đã đăng ký, số đếm, nhãn và phiếu P4 (hồ sơ); A: lựa chọn đề cử là ý kiến Opus"
    elif g == "DC3":
        xm = "V: khóa, H2, H4, khóa bị chặn, số đếm (l3b-de-cu-opus.tsv), mục Wiktionary; A: nhãn, lớp, H6 (chưa chấm P4)"
    elif g == "DC4":
        xm = "V: khóa, H2, H4, khóa bị chặn, số đếm (l2d-ung-vien.tsv); A: nhãn, lớp, H6, đúng nghĩa ở kho (H8 yếu)"
    else:
        xm = "V: khóa, H2, H4, khóa bị chặn, có trong HND; A: độ thông dụng (chưa đếm), nhãn, lớp, H6"
    rows.append({
        "nhom": g, "uu_tien": uu, "tu": w, "khoa": r["khoa"], "so_chu": r["so_chu"], "so_khoi": r["so_khoi"],
        "nhan": r["nhan"], "lop": r["lop"], "ngan_du_kien": ngan, "F": r["F"], "diem": r["diem"], "hang_xep_hang_v2": r["hang_xep_hang_v2"],
        "phieu_P4": r["phieu"], "sub_sach": r["sub_sach"], "web_sach": r["web_sach"], "leipzig": r["leipzig"], "tatoeba": r["tatoeba"],
        "H8": r["H8"], "hnd": h.get("hnd", ""), "chu_ky": r["chu_ky"], "muc_hnd_cung_khoa": h.get("muc_hnd_cung_khoa", ""),
        "ly_do_chua_chon": r["ly_do_chua_chon"], "dieu_kien_de_xet": r["dieu_kien"], "ghi_chu": " | ".join(note), "xac_minh": xm,
    })
order = {"DC1": 1, "DC2": 2, "DC3": 3, "DC4": 4, "DC5": 5}
rows.sort(key=lambda r: (order[r["nhom"]], -(float(r["diem"]) if r["diem"] else 0), o1(r["tu"])))
for i, r in enumerate(rows, 1):
    r["stt"] = i
header = ["stt"] + [h for h in rows[0] if h != "stt"]
write_tsv(OUT / "de-cu-them-opus.tsv", header, rows)
print(len(rows), collections.Counter((r["nhom"], r["ngan_du_kien"], r["uu_tien"]) for r in rows))
fs = {g: sorted(float(r["F"]) for r in rows if r["nhom"] == g and r["F"] and r["lop"] != "F") for g in ("DC1", "DC2")}
for g, a in fs.items():
    print(g, "F trung vị", a[len(a) // 2], "min", a[0], "n", len(a))
