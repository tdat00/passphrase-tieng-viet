"""Quét bổ sung H7 cho bản nháp chung (review bước 3): mọi cách đọc khác (DOC_KHAC trong U/opus-counts.tsv)
cùng khóa với một mục dự phòng hoặc một HM có hồ sơ (bỏ L3b), kèm PPM gộp (trung bình PPM sạch hai kho, mẫu số
tieu-chi-thong-nhat.md:20), cờ còi theo mốc (>= 0,3 hoặc >= PPM gộp của mục) và có/không trong bảng còi.

    python h7-quet-bo-sung.py  ->  h7-quet-bo-sung.tsv

Cột nhom_do_opus là nhận định của Opus sau khi đọc (assumed); bảng chỉ có đầu mục và số đếm.
"""
import csv
from chung import *

out_utf8()
SUB0, WEB0 = 34314528, 149860716
DO = {  # nhận định Opus (assumed) cho các cách đọc khác có nghĩa đỏ hoặc sát nhóm đỏ
    ("baotu", "báo tử"): "H6.4 (thông báo cái chết): đỏ; đề nghị K1",
    ("tanso", "tận số"): "H6.4 (hết số, chết): đỏ nhưng hiếm; K2 không tự động chặn",
    ("vaynen", "vảy nến"): "H6.5 (bệnh da): đỏ nhưng hiếm; K2 không tự động chặn",
    ("mong", "mông"): "bộ phận cơ thể thường dùng, không thuộc nghĩa người lớn; không đỏ",
    ("ngoaitru", "ngoại trú"): "nơi ở/điều trị ngoài; không phải bệnh; không đỏ",
}


def tsv(path):
    return list(csv.DictReader(open(path, encoding="utf-8", newline=""), delimiter="\t"))


def ppm(r):
    return (int(r["sub_sach"]) / SUB0 * 1e6 + int(r["web_sach"]) / WEB0 * 1e6) / 2


oc = tsv(U / "opus-counts.tsv")
cb = {(r["khoa"], r["doc_khac"]) for r in tsv(U / "canh-bao-khong-dau.tsv")}
item = {r["tu"]: ppm(r) for r in oc if r["vai_tro"] == "UNG_VIEN"}
tap = [("DU_PHONG", r) for r in tsv(U / "du-phong-v2-phan-loai.tsv")]
tap += [("HM", r) for r in tsv(U / "du-phong-v2-honorable-mentions.tsv") if r["nhom"] != "L3B_CHUA_CHAM"]
ks = {r["khoa"]: (t, r["tu"]) for t, r in tap}
rows = []
for r in oc:
    if r["vai_tro"] != "DOC_KHAC" or r["khoa"] not in ks:
        continue
    t, w = ks[r["khoa"]]
    p, q = ppm(r), item.get(w, 0.0)
    rows.append({"tap": t, "tu": w, "khoa": r["khoa"], "doc_khac": r["tu"], "ppm_gop_muc": f"{q:.3f}",
                 "ppm_gop_doc_khac": f"{p:.3f}", "dat_moc_coi": "CO" if p >= 0.3 or p >= q else "KHONG",
                 "trong_bang_coi": "CO" if (r["khoa"], r["tu"]) in cb else "KHONG",
                 "nhom_do_opus": DO.get((r["khoa"], r["tu"]), "-")})
rows.sort(key=lambda x: (x["tap"], o1(x["tu"]), o1(x["doc_khac"])))
write_tsv(HERE / "h7-quet-bo-sung.tsv", list(rows[0].keys()), rows)
for t in ("DU_PHONG", "HM"):
    sub = [x for x in rows if x["tap"] == t]
    print(t, "cap", len(sub), "dat_moc", sum(x["dat_moc_coi"] == "CO" for x in sub),
          "trong_bang_coi", sum(x["trong_bang_coi"] == "CO" for x in sub))
for x in rows:
    if x["dat_moc_coi"] == "KHONG":
        print(" duoi_moc:", x["tap"], x["tu"], "->", x["doc_khac"], x["ppm_gop_doc_khac"])
