"""Số liệu phạm vi cho Q-dpv2-1 và độ nhạy mẫu số H8 (review bản nháp chung, bước 3).

    python pham-vi-hau-kiem.py  ->  pham-vi-hau-kiem.log, pham-vi-hau-kiem-h7.tsv

1. H5: số cặp thô của bộ sinh biến thể trên danh sách chính (evidence/bien-the-chinh-tho.tsv).
2. H7: các cách đọc khác (DOC_KHAC trong U/opus-counts.tsv) cùng khóa với một từ chính, có PPM gộp >= 0,3
   (trung bình PPM sạch hai kho, mẫu số mục 0 của tiêu chí, tieu-chi-thong-nhat.md:20) mà không có dòng nào
   trong U/canh-bao-khong-dau.tsv. Đây chỉ là số cặp cần người đọc, không phải kết luận nhóm đỏ.
3. H8: các mục dự phòng/HM có kết quả MANH/YEU khác nhau giữa mẫu số P2 và mẫu số mục 0.
Chỉ đọc; chỉ ghi đầu mục, khóa và số đếm.
"""
import collections
import csv
from chung import *

out_utf8()
log = []
SUB0, WEB0 = 34314528, 149860716  # tieu-chi-thong-nhat.md:20, manifest counter_tokens
SUBP2, WEBP2 = 34329387, 150070912  # U/tap-luat-P2-v4.json tong_am_tiet


def tsv(path):
    return list(csv.DictReader(open(path, encoding="utf-8", newline=""), delimiter="\t"))


bt = tsv(HERE / "bien-the-chinh-tho.tsv")
log.append(f"H5 cặp thô trên danh sách chính: {len(bt)} cặp, {len({r['tu'] for r in bt})} từ chính")

main = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
kmain = {key(w): w for w in main}
cb = tsv(U / "canh-bao-khong-dau.tsv")
cb_pairs = {(r["khoa"], r["doc_khac"]) for r in cb}
oc = tsv(U / "opus-counts.tsv")
ung = collections.defaultdict(float)
for r in oc:
    if r["vai_tro"] == "UNG_VIEN":
        ppm = (int(r["sub_sach"]) / SUB0 * 1e6 + int(r["web_sach"]) / WEB0 * 1e6) / 2
        ung[r["tu"]] = ppm
rows = []
for r in oc:
    if r["vai_tro"] != "DOC_KHAC" or r["khoa"] not in kmain:
        continue
    ppm = (int(r["sub_sach"]) / SUB0 * 1e6 + int(r["web_sach"]) / WEB0 * 1e6) / 2
    tu = kmain[r["khoa"]]
    if ppm >= 0.3 and (r["khoa"], r["tu"]) not in cb_pairs:
        rows.append(dict(zip(["khoa", "tu_chinh", "doc_khac", "ppm_gop_tu_chinh", "ppm_gop_doc_khac", "doc_khac_ge_tu_chinh"],
                             [r["khoa"], tu, r["tu"], f"{ung.get(tu, 0):.4f}", f"{ppm:.4f}",
                              "CO" if ppm >= ung.get(tu, 0) else "KHONG"])))
rows.sort(key=lambda x: o1(x["tu_chinh"]))
write_tsv(HERE / "pham-vi-hau-kiem-h7.tsv", ["khoa", "tu_chinh", "doc_khac", "ppm_gop_tu_chinh", "ppm_gop_doc_khac",
                                             "doc_khac_ge_tu_chinh"], rows)
log.append(f"H7 cách đọc khác cùng khóa từ chính, PPM gộp >= 0,3, không có trong canh-bao-khong-dau.tsv: "
           f"{len(rows)} cặp, {len({x['khoa'] for x in rows})} khóa; trong đó cách đọc khác >= PPM từ chính: "
           f"{sum(1 for x in rows if x['doc_khac_ge_tu_chinh'] == 'CO')}")
log.append(f"canh-bao-khong-dau.tsv: {len(cb)} dòng, {len({r['khoa'] for r in cb})} khóa")


def manh(s, w, le, ta, S, W):
    return s / S * 1e6 >= 0.1 or w / W * 1e6 >= 0.1 or le >= 2 or ta >= 1


def num(x):
    return int(x) if x not in ("-", "", "CHUA_DO") else None


H = tsv(U / "du-phong-v2-honorable-mentions.tsv")
lech = []
for r in H:
    s, w, le, ta = (num(r[c]) for c in ("sub_sach", "web_sach", "leipzig", "tatoeba"))
    if None in (s, w, le, ta):
        continue
    a, b = manh(s, w, le, ta, SUBP2, WEBP2), manh(s, w, le, ta, SUB0, WEB0)
    if a != b:
        lech.append(f"{r['tu']} ({s}/{w}/{le}/{ta}): P2={'MANH' if a else 'YEU'}, muc0={'MANH' if b else 'YEU'}")
log.append(f"H8 HM có số đủ bốn kho: {sum(1 for r in H if None not in (num(r[c]) for c in ('sub_sach', 'web_sach', 'leipzig', 'tatoeba')))}"
           f"; khác kết quả giữa hai mẫu số: {len(lech)} {lech}")
f8 = tsv(HERE / "h8-chinh-thuc.tsv")
cols = f8[0].keys()
log.append("h8-chinh-thuc.tsv cột: " + ",".join(cols))
(HERE / "pham-vi-hau-kiem.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
print("\n".join(log))
