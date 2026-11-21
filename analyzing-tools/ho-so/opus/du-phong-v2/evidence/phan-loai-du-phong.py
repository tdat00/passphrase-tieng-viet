"""Bước 4: phân bậc 205 từ dự phòng (A/B/C/D) từ bảng sự kiện và ghi chú tay của Opus.

    python phan-loai-du-phong.py
Đọc evidence/du-phong-205-su-kien.tsv, evidence/bien-the-du-phong-205.tsv, evidence/du-phong-205-hnd.tsv;
ghi ../du-phong-205-phan-loai-opus.tsv và in tóm tắt.

Bậc (xét theo thứ tự D > C > B > A):
  D  Không dùng: trùng một từ với mục khác theo H5 (biến thể khác khóa) — "không bao giờ nhận cả hai".
  C  Yếu: chứng liệu H8 yếu hoặc tổng chứng liệu ≤ 3, hoặc dễ lẫn với một mục chính/dự phòng khác khóa, hoặc
     họ chính tả chưa đăng ký cần đo. Dùng sau A/B cùng ngăn.
  B  Dùng được sau khi có nghĩa: chưa có câu giải nghĩa (cần lượt viết sạch, D6, D7).
  A  Sẵn sàng thay: có câu đạt D6 (P0) và D7, chứng liệu mạnh, không vướng điểm nào ở trên.
"""
import collections
from chung import *

out_utf8()
su = rd(HERE / "du-phong-205-su-kien.tsv", True)
hnd = {r["tu"]: r for r in rd(HERE / "du-phong-205-hnd.tsv", True)}

# Ghi chú tay (lời của Opus). Mỗi mục: (bậc tối thiểu, mã vấn đề, mô tả, xác minh V=đã kiểm bằng dữ liệu / A=giả định cần SA kia xác nhận)
TAY = {
    "hì hụi": ("D", "H5_BIEN_THE_CHINH", "Cùng một từ với hì hục (đang ở danh sách chính), khác khóa (hihui/hihuc); H5c không nhận cả hai. Đếm sạch: hì hụi 0/0, hì hục 0/3 (phụ đề/web)", "V số đếm; A cùng từ"),
    "tròng trành": ("D", "H5_BIEN_THE_CHINH", "Cùng một từ với chòng chành (đang ở danh sách chính), đổi tr/ch ở cả hai âm tiết nên quét 6.1 (đổi một chỗ) bỏ sót. Đếm sạch: 2/1 so với 3/6", "V số đếm; A cùng từ"),
    "nhão nhẹt": ("D", "H5_HO_MOI_THIEU_DU_LIEU", "Cùng một từ với nhão nhoẹt (cũng là dự phòng), khác khóa. Không dạng nào chiếm ≥ 95%: phụ đề 9 so với 6 (thêm 5 của nhão nhoét cùng khóa), web 0 so với 1 (thêm 1); web cả họ dưới 20 lượt. H5c loại cả hai nếu hai SA đăng ký họ", "V số đếm; A cùng từ"),
    "nhão nhoẹt": ("D", "H5_HO_MOI_THIEU_DU_LIEU", "Như nhão nhẹt", "V số đếm; A cùng từ"),
    "chọc lét": ("D", "H5_HO_MOI_THIEU_DU_LIEU", "Cùng một từ với thọc lét, chọc léc, thọc léc (cả ba có trong HND), khác khóa; chọc lét chỉ có 5/0 lượt sạch (phụ đề/web) nên không thể đạt ≥ 95% với ≥ 20 lượt ở cả hai kho (H5c)", "V HND, số đếm; A cùng từ"),
    "chán phèo": ("D", "H5_HO_MOI_THIEU_DU_LIEU", "Cùng một từ với chán phè (HND 22K), khác khóa; chán phèo có 20/0 lượt sạch nên web thiếu dữ liệu, H5c không nhận", "V HND, số đếm; A cùng từ"),
    "loằng ngoằng": ("C", "H5_HO_CHUA_DO", "HND có dạng loằn ngoằn (khác khóa) chưa từng được đếm; cần xác nhận có phải cùng từ và đo trước khi dùng", "V HND; A cùng từ"),
    "lỗi hẹn": ("C", "DE_LAN_CHINH", "Dễ lẫn với lỡ hẹn (danh sách chính, 23/3 lượt) cả nghĩa lẫn âm; khác khóa (loihen/lohen)", "V có mặt; A mức dễ lẫn"),
    "trở lên": ("C", "DE_LAN_CHINH", "Khác trở nên (danh sách chính) chỉ ở l/n; lỗi l/n giữa hai từ này rất hay gặp nên dễ gõ nhầm khóa", "V có mặt; A mức dễ lẫn"),
    "lời lỗ": ("C", "GAN_NGHIA_DU_PHONG", "Gần nghĩa với lỗ lãi (dự phòng); chọn lỗ lãi trước vì chứng liệu mạnh hơn", "V"),
    "mỏng tanh": ("C", "GAN_NGHIA_DU_PHONG", "Gần nghĩa với mỏng dính (dự phòng); chọn mỏng dính trước vì chứng liệu mạnh hơn", "V"),
}
NOTE = {
    "cười mỉm": "Cặp đảo với mỉm cười (chính); đã trừ 5 điểm theo S3", "dịu hiền": "Cặp đảo với hiền dịu (chính); đã trừ 5 điểm",
    "đầy tràn": "Cặp đảo với tràn đầy (chính); đã trừ 5 điểm", "leo dây": "Cặp đảo với dây leo (chính), khác nghĩa; đã trừ 5 điểm",
    "mong nhớ": "Cặp đảo với nhớ mong (chính); đã trừ 5 điểm", "nặng cân": "Cặp đảo với cân nặng (chính), khác nghĩa; đã trừ 5 điểm",
    "ngả nghiêng": "Cặp đảo với nghiêng ngả (chính); đã trừ 5 điểm", "ngóng trông": "Cặp đảo với trông ngóng (chính); đã trừ 5 điểm",
    "no ấm": "Cặp đảo với ấm no (chính); đã trừ 5 điểm", "xầm xì": "Cặp đảo với xì xầm (chính); đã trừ 5 điểm",
    "thật ra": "Cặp thật/thực với thực ra (dự phòng); tiền lệ: chính có cả thật sự/thực sự", "thực ra": "Cặp thật/thực với thật ra (dự phòng)",
    "lộp bộp": "Gần nghĩa và gần âm với lộp độp (dự phòng)", "lộp độp": "Gần nghĩa và gần âm với lộp bộp (dự phòng)",
    "lỗ lãi": "Gần nghĩa với lời lỗ (dự phòng)", "mỏng dính": "Gần nghĩa với mỏng tanh (dự phòng)",
    "làm cỗ": "K2 (làm cỏ) đã đủ hai chữ ký", "ăn nhịp": "Ngoại lệ H8 (0/0/0/0) có hai chữ ký; dùng thì M4 = 1",
    "vậy nên": "Khóa vaynen trùng vảy nến (bệnh); PPM gộp 0,25 dưới mốc còi 0,3, P2 H7 đạt", "thay lông": "Khóa trùng thay lòng; không thuộc nhóm đỏ",
    "vô tình": "Khóa trùng vô tính; không thuộc nhóm đỏ", "phất phơ": "Còi H7 (phật phờ, 0 PPM) đã đóng",
    "dễ ợt": "Họ dễ ợt/dể ợt cùng khóa, trừ 5 điểm H5d", "sẩy chân": "Cờ HAI_NGHIA đã đóng ở D7",
    "xin chào": "H3 theo Wiktionary (không có trong HND)", "chút": "Khóa trùng chụt (tiếng hôn), không thuộc nhóm đỏ",
    "ăn trầu": "Đã xét nhóm 7: trầu cau là tục truyền thống, không phải thuốc lá hay chất gây nghiện theo bảng H6",
    "đầy tháng": "Đã xét nhóm 4: dịp mừng trẻ, không phải tang lễ", "đầy năm": "Đã xét nhóm 4: dịp mừng trẻ, không phải tang lễ",
}
rows = []
for r in su:
    w = r["tu"]
    ev = sum(int(r[k] or 0) for k in ("sub_sach", "web_sach", "leipzig", "tatoeba"))
    van_de, xm = [], []
    bac = "A"
    if w in TAY:
        b, ma, mo, x = TAY[w]
        bac = b
        van_de.append(f"{ma}: {mo}")
        xm.append(x)
    if r["H8"] in ("YEU", "KHONG") or ev <= 3:
        if bac not in ("D",):
            bac = "C"
        van_de.append(f"CHUNG_LIEU_YEU: H8 {r['H8']}, tổng chứng liệu {ev} (phụ đề/web sạch, Leipzig, Tatoeba)")
        xm.append("V")
    if r["giai_nghia"] != "CO" and bac == "A":
        bac = "B"
    if w in NOTE and NOTE[w]:
        van_de.append("GHI_CHU: " + NOTE[w])
    # kiểm lại luật cứng tự động
    k = r["khoa"]
    kiem = []
    kiem.append("H1H2:DAT" if 4 <= int(r["so_chu"]) <= 12 and 1 <= int(r["so_khoi"]) <= 3 else "H1H2:TRUOT")
    kiem.append("H4:DAT" if not r["trung_khoa_chinh"] else "H4:TRUNG")
    kiem.append("K012:DAT" if not r["khoa_bi_chan"] else "K012:" + r["khoa_bi_chan"])
    kiem.append("H5_DA_DANG_KY:" + ("DAT" if not any(x in r["ho_chinh_ta"] for x in (":LOAI", ":CHO")) else "TRUOT"))
    kiem.append("H3:" + ("HND " + hnd[w]["hnd"].replace(";", ",") if hnd[w]["hnd"] else "Wiktionary (P2)"))
    ngan = r["ngan"]
    thay = "1 trong 7.699 suất OK không-F (trừ 14 mục chủ dự án giữ)" if ngan == "OK_KHONG_F" else "1 trong 77 suất lớp F (Q3 ≤ 77)"
    thieu = []
    if bac == "D":
        thieu.append("Không dùng; lập biên bản khấu trừ có hai chữ ký (H5)")
    else:
        if r["giai_nghia"] != "CO":
            thieu.append("Câu giải nghĩa: lượt viết sạch, D6 (P0), D7")
        if w in TAY and TAY[w][1] == "H5_HO_CHUA_DO":
            thieu.append("Đăng ký và đo họ chính tả (H5)")
        thieu.append("Khi dùng: chạy lại P6 (ngăn, hạng), thêm dòng D8, đổi trạng thái trong labels.tsv, --phat-hanh toàn bộ, hai bộ kiểm")
    d7 = r["D7_luot_cuoi"]
    rows.append({
        "stt": r["stt"], "tu": w, "khoa": k, "so_chu": r["so_chu"], "so_khoi": r["so_khoi"], "lop": r["lop"], "ngan": ngan,
        "hang_trong_ngan_P0": r["hang_trong_ngan_P0"], "F": r["F"], "diem": r["diem"],
        "sub_sach": r["sub_sach"], "web_sach": r["web_sach"], "leipzig": r["leipzig"], "tatoeba": r["tatoeba"], "H8": r["H8"],
        "chu_ky": r["chu_ky"], "giai_nghia": r["giai_nghia"], "luot_viet": r["luot_viet"], "D6": r["D6"],
        "D7": ("CO_PHIEU:" + d7) if d7 else ("" if r["giai_nghia"] == "CO" else "CHUA"), "co": r["co_giai_nghia"],
        "sha256_giai_nghia": r["sha256_giai_nghia"], "kiem_lai": ";".join(kiem), "bac": bac, "thay_duoc": thay,
        "van_de": " | ".join(van_de), "con_thieu": "; ".join(thieu), "xac_minh": ";".join(xm) if xm else "V",
    })

header = list(rows[0].keys())
write_tsv(OUT / "du-phong-205-phan-loai-opus.tsv", header, rows)
c = collections.Counter((r["ngan"], r["bac"]) for r in rows)
print("bậc × ngăn:", sorted(c.items()))
print("bậc:", collections.Counter(r["bac"] for r in rows))
for b in "DCB":
    print(b, [r["tu"] for r in rows if r["bac"] == b])
