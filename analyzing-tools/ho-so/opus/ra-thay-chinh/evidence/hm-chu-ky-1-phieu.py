"""Phiếu duyệt của Opus cho đề xuất HM của Astra (chu kỳ D-rtc-8): hm-chu-ky-1-opus.tsv.

Đọc kết quả kiểm dữ liệu (hm-chu-ky-1-opus-kiem.tsv, do hm-chu-ky-1-opus.py sinh) và phiếu của Astra; ghi ý kiến,
chữ ký K2 và nguồn. Chạy: python -X utf8 -B hm-chu-ky-1-phieu.py
"""
from chung import AT, OUT, U, key, out_utf8, rd, write_tsv

out_utf8()
A = AT / "ho-so" / "astra" / "ra-thay-chinh"
KIEM = OUT / "evidence" / "hm-chu-ky-1-opus-kiem.tsv"
OE = "ho-so/opus/ra-thay-chinh/evidence"
RD = "ho-so/astra/ra-thay-chinh"

LY_DO = {
    "ngân hàng": "Không có cách đọc khác cùng khóa (HND, Kaikki, opus-counts). Dịch vụ tài chính, không thuộc nhóm 3 hay 7.",
    "khách hàng": "Không có cách đọc khác cùng khóa. Nghĩa thường.",
    "biển": "Ký K2. Nghĩa chính của biến là đổi khác hay mất đi; lời đuổi 'biến đi' là cách dùng phụ, nhẹ. Biến nhiều hơn biển "
            "(phụ đề 10.287/3.923) nhưng nghĩa chính không đỏ nên không phải K1. Biên, biện, biền không đỏ.",
    "côn trùng": "Không có cách đọc khác cùng khóa. Tên nhóm con vật; nhóm 10 chỉ hạ hạng tên con vật (TC:152).",
    "cô giáo": "Cố giao (1/2) hiếm, không đỏ.",
    "thay thế": "Không có cách đọc khác cùng khóa trong từ điển. Nghĩa thường.",
    "chỗ ngồi": "H5d: chổ ngồi chiếm 3,5% phụ đề (4,1% khi bỏ dòng trùng) và 0,3% web, dưới 5%: qua, không trừ điểm.",
    "một mình": "Lớp K, khóa motminh khác minh (F). Không thuộc nhóm 9 (cô đơn được miễn, TC:151).",
    "bí mật": "Ký K2. Bỉ mặt (khinh, coi thường) chỉ 0/1 lượt sạch; nghĩa chê nhẹ, hiếm hơn hẳn cách đọc chính.",
    "mùa đông": "Mưa dông (0/10) là thời tiết như mưa rào, không thuộc nhóm 8 (TC:150).",
    "tàu điện": "H5c: tàu điện chiếm 98,1% phụ đề và 99,6% web, đạt 95% ở cả hai kho.",
    "cụ thể": "Không có cách đọc khác cùng khóa trong từ điển. Cụ thễ là lỗi gõ, 0/1.",
    "áp dụng": "Không có cách đọc khác cùng khóa. Nghĩa thường.",
    "vận hành": "Ký K2. Vạn hạnh là thuật ngữ Phật học và tên riêng; 0 lượt phụ đề, 95 lượt web (0,4% so với vận hành). "
                "Nhóm 4 chỉ ở nghĩa đạo, hiếm.",
    "việc làm": "Không có cách đọc khác cùng khóa. Lao động, không thuộc nhóm đỏ.",
    "chế tạo": "Không có cách đọc khác cùng khóa. Vũ khí chỉ là một tân ngữ có thể gặp, không phải nghĩa của mục.",
    "lực lượng": "Giữ theo T-dpv2-8: nghĩa của mục là sức mạnh hay tập hợp người nói chung; nghĩa quân sự đến từ bổ ngữ. "
                 "Lực lưỡng (29/182) không đỏ.",
    "chia": "Ký K2, mở rộng chữ ký cũ của khóa chia (hai bên, 19/11/2026) sang chỉa, chía, chị ả. Chĩa không đỏ tự thân "
            "(chữ ký cũ); chỉa cùng đánh giá (Kaikki ghi nghĩa khác, phụ đề dùng như chĩa); chía (17/29) không đỏ; "
            "chị ả (0/0) chê nhẹ, hiếm.",
    "bánh ngọt": "Không có cách đọc khác cùng khóa. Tên món ăn.",
    "đánh răng": "Nhóm 5 miễn rõ (TC:147). Đành rằng (1/3) không đỏ.",
    "xe điện": "Không có cách đọc khác cùng khóa. Tên phương tiện.",
    "bày tỏ": "H5: bầy tỏ và bày tõ chiếm 0,9% phụ đề, 0,2% web: qua cả c và d.",
    "chuyển đổi": "Chuyển dời (4/5) không đỏ.",
    "ngắn gọn": "Ký K2. Ngả ngớn (0/0) nghĩa là không đứng đắn; Kaikki và HND không ghi nghĩa tục hay tình dục người lớn, "
                "nên không K0 (TC:161). Hiếm. Ngả ngốn (1/0) là bừa bộn.",
    "tương đương": "Tương Dương là địa danh, không đỏ.",
}
LOAI = {
    "cơ quan": ("KHONG_CHON_H6", "Đồng ý không chọn. Astra phản đối theo nhóm 3 có căn cứ (nghĩa đơn vị nhà nước, cách dùng "
                "chấp pháp); phản đối còn giữ thì không phát hành (TC:190–191). T-dpv2-8 chỉ giữ cờ rà H6."),
    "mình": ("KHONG_CHON_F", "Đồng ý không chọn: lớp F, F đã đủ 77, mọi ghế cần lấp đều không-F."),
}

kiem = {r["tu"]: (i, r) for i, r in enumerate(rd(KIEM, mine=True), 2)}
astra = list(enumerate(rd(A / "hm-chu-ky-1.tsv"), 2))
ck_dong = [i for i, r in enumerate(rd(U / "chu-ky.tsv"), 2) if r["khoa"] == "chia"]
assert set(LY_DO) == {r["tu"] for _, r in astra}
rows = []
for i, r in astra:
    w = r["tu"]
    ki, k = kiem[w]
    assert k["kiem_du_lieu"] == "DAT", w
    k2 = r["ket_qua_H"] != "DAT_H_ASTRA"
    nguon = f"{OE}/hm-chu-ky-1-opus-kiem.tsv:{ki}; {RD}/hm-chu-ky-1.tsv:{i}"
    if w == "chia":
        nguon += "; ho-so/unified/chu-ky.tsv:" + ",".join(map(str, ck_dong))
    rows.append({"thu_tu": r["thu_tu"], "tu": w, "khoa": key(w), "lop": r["lop"], "de_xuat_astra": r["ket_qua_H"],
                 "y_opus": "DONG_Y", "ky_opus": "Y" if k2 else "-", "ly_do": LY_DO[w], "bang_chung": nguon})
for w, (ma, ly) in LOAI.items():
    rows.append({"thu_tu": "-", "tu": w, "khoa": key(w), "lop": "F" if w == "mình" else "C", "de_xuat_astra": ma,
                 "y_opus": "DONG_Y", "ky_opus": "-", "ly_do": ly, "bang_chung": f"{RD}/hm-chu-ky-1.md"})
write_tsv(OUT / "hm-chu-ky-1-opus.tsv", list(rows[0].keys()), rows)
print(len(rows), "dòng;", sum(r["ky_opus"] == "Y" for r in rows), "chữ ký K2")
