"""T9: phán quyết của SA-Opus cho các cặp cùng khóa chưa có phán quyết (t9-soat.tsv) và các cách đọc chỉ có ở Kaikki.

Mã: K1_DE_XUAT, K2_DE_XUAT (Opus ký "không tự động chặn", cần chữ ký Astra), KHONG_DO (không thuộc nhóm đỏ),
KHONG_COI (nhóm đỏ nhưng dưới mốc còi và không thuộc nhóm tự hại, bạo lực, tình dục rõ, K0: TC:160 không bắt phán quyết).
Số đếm lấy từ t9-dem.tsv (hai kho ghim, đếm n-gram như count_corpus.py; có ghi chú khi số bị thổi phồng do ghép qua từ).

Chạy: python -X utf8 -B t9-phan-quyet.py  ->  t9-phan-quyet.tsv
"""
from chung import HERE, out_utf8, rd, write_tsv

out_utf8()
dem = {(r["tu_chinh"], r["doc_khac"]): r for r in rd(HERE / "t9-dem.tsv")}

PQ = {
    # còi theo số (≥ 0,3 PPM hoặc ≥ PPM của từ chính) hoặc nhóm bạo lực/K0: cần phán quyết chung
    ("đuôi", "đượi"): ("K2_DE_XUAT", "K0?", "Nói lái của đĩ, chỉ có ở viwiktionary, không ở HND hay DOC_KHAC; 9 lượt phụ đề, 0 web, "
                       "phần lớn nghi gõ sai được. Theo tiền lệ bình/bĩnh (K2 hai bên ký, chu-ky.tsv:134–135). Nếu Astra giữ K0 thì trình chủ dự án (TC:164)"),
    ("đon đả", "đòn đá"): ("K2_DE_XUAT", "G1", "Đòn đá là tên đòn võ, cụm ghép từ hai tiếng, không có ở HND; 1+1 lượt, từ chính 1+0 lượt "
                          "nên tỉ lệ vô nghĩa. Khác đấm đá (đánh nhau, từ ghép thông dụng, K1)"),
    ("tụ tập", "tu tập"): ("K2_DE_XUAT", "G4", "Tu tập là việc tu hành, nghĩa tôn giáo nhẹ, không phải nghi lễ tang hay thần linh; tỉ lệ 0,12"),
    ("song ngữ", "song ngư"): ("K2_DE_XUAT", "G4", "Chòm sao, cung hoàng đạo; tiền lệ hoang đảo/hoàng đạo (K2)"),
    ("tử tế", "tư tế"): ("K2_DE_XUAT", "G4", "Chức sắc tôn giáo, hay gặp trong phụ đề phim giả tưởng; nghĩa tôn giáo nhẹ; tỉ lệ 0,074"),
    ("chanh", "chảnh"): ("K2_DE_XUAT", "G9", "Lời chê nhẹ (làm cao), khóa một âm tiết; tiền lệ ngốc, nhãi (K2)"),
    ("thú dữ", "thứ dữ"): ("K2_DE_XUAT", "G1", "Cách nói người khó chơi, không phải hành vi bạo lực; số bị thổi phồng bởi thứ dữ liệu, thứ dữ dội"),
    ("tung", "tửng"): ("K2_DE_XUAT", "G5", "Tiếng lóng nhẹ (hơi điên), phần lớn số là tưng tửng; tỉ lệ 0,011; mở rộng chữ ký K2 sẵn có của khóa tung"),
    ("mằn mặn", "man man"): ("K2_DE_XUAT", "G5", "Tiếng lóng nhẹ; số web phần lớn là chữ tiếng Anh man man; nghĩa đỏ không chắc"),
    ("bạn thân", "bán thần"): ("K2_DE_XUAT", "G4", "Á thần trong truyện; tỉ lệ 0,016; mở rộng chữ ký K2 sẵn có của khóa banthan (D-rtc-7)"),
    ("cau có", "cầu cơ"): ("K2_DE_XUAT", "G4", "Trò gọi hồn, mê tín; số bị thổi phồng bởi nhu cầu cơ bản, yêu cầu cơ bản; tiền lệ ngải, nguyền (K2)"),
    ("dài hạn", "đại hãn"): ("K2_DE_XUAT", "G3", "Tước hiệu vua Mông Cổ trong phim lịch sử; tiền lệ triệu/triều (D-rtc-7); mở rộng chữ ký K2 sẵn có của khóa daihan"),
    ("liễu", "liêu"): ("K2_DE_XUAT", "G3", "Tên triều Liêu; số gồm quan liêu, liêu xiêu, tịch liêu, đồng liêu, họ Liêu; nghĩa đỏ không chắc"),
    ("công cộng", "công công"): ("KHONG_DO", "-", "Thái giám, hay bố chồng trong phim Trung Quốc; như hoàng hậu, công chúa (TC:145 không đỏ); "
                                "số bị thổi phồng bởi thành công công việc"),
    # dưới mốc còi, không thuộc nhóm tự hại, bạo lực, tình dục rõ, K0
    ("liệng", "liêng"): ("KHONG_COI", "G7", "Bài liêng: 0 lượt phụ đề, khoảng 5 lượt web; 356/361 lượt phụ đề và 630/655 lượt web của liêng là thiêng liêng"),
    ("linh dương", "linh đường"): ("KHONG_COI", "G4", "1+1 lượt"),
    ("chứng chỉ", "chung chi"): ("KHONG_COI", "G2", "0,22 PPM, dưới 0,3 và dưới từ chính"),
    ("sành ăn", "sân hận"): ("KHONG_COI", "G9", "0,15 PPM"),
    ("mũ nồi", "mụ nội"): ("KHONG_COI", "G9", "2+0 lượt"),
    ("bổ dưỡng", "bố đường"): ("KHONG_COI", "G6", "Tiếng lóng mới, không phải nghĩa tình dục rõ; 0+8 lượt"),
    ("thiện chí", "thiền chỉ"): ("KHONG_COI", "G4", "0+5 lượt"),
    ("thành quả", "thánh quả"): ("KHONG_COI", "G4", "0 lượt"),
    ("hướng dương", "hưởng dương"): ("KHONG_COI", "G4", "0+1 lượt"),
    ("nhân tài", "nhân tai"): ("KHONG_COI", "G8", "0,11 PPM; tỉ lệ 0,028"),
    ("đá tảng", "đa tạng"): ("KHONG_COI", "G5", "0,09 PPM, dưới từ chính"),
    ("mã số", "ma sơ"): ("KHONG_COI", "G4", "4+6 lượt"),
    ("chốt", "chớt"): ("KHONG_COI", "G4", "Cách viết theo giọng của chết; 4+1 lượt"),
    ("tử tế", "tứ tế"): ("KHONG_COI", "G4", "1+0 lượt"),
    ("hóng chuyện", "hồng chuyên"): ("KHONG_COI", "G3", "0,02 PPM, dưới từ chính 0,17"),
    ("riêu", "riệu"): ("KHONG_COI", "G7", "0,08 PPM, dưới từ chính"),
    ("bình dị", "binh di"): ("KHONG_COI", "G1", "Từ Hán Việt cổ về việc quân, không phải hành vi bạo lực; 0+2 lượt"),
    ("quần bò", "quân bộ"): ("KHONG_COI", "G1", "Quân sự cổ; 3+4 lượt"),
    ("tiến bộ", "tiền bộ"): ("KHONG_COI", "G1", "Quân sự cổ; 1+4 lượt"),
    ("cãi cọ", "cai cò"): ("KHONG_COI", "G2", "0 lượt"),
    ("bồi bàn", "bôi bàn"): ("KHONG_COI", "G7", "0+1 lượt"),
    ("băng đô", "bang đỏ"): ("KHONG_COI", "G3", "0 lượt"),
    ("nhà ăn", "nhà ân"): ("KHONG_COI", "G3", "0 lượt"),
    ("nhìn", "nhĩn"): ("KHONG_DO", "-", "Chỉ bộ phận của loài chuột theo một mục Kaikki, không phải nghĩa tình dục người lớn; 2+0 lượt, nghi gõ sai"),
}
KHONG_DO_NHOM = {  # cặp bị bộ lọc bắt hay của từ vào, không thuộc nhóm đỏ
    "tên riêng, địa danh": ["ăn tiệm/an tiêm", "chính cống/chính công", "đại dương/đài dương", "đường cong/dương công",
                           "đường kính/dương kinh", "đường làng/đường lang", "mắc áo/ma cao", "tủ kính/tử kính", "thủ thư/thử thủ"],
    "biến thể, từ tượng thanh, từ thường": [
        "bí bách/bì bạch", "buồn thiu/buồn thỉu", "chấp nhặt/chấp nhất", "chấp nhặt/chắp nhặt", "dài ngoằng/dài ngoẵng",
        "đầy tháng/dây thắng", "đầy tràn/dây trần", "đủng đỉnh/đùng đinh", "đủng đỉnh/đùng đình", "ỉu xìu/ỉu xịu",
        "lỗ lãi/lờ lãi", "lộp bộp/lóp bóp", "lộp bộp/lọp bọp", "lộp bộp/lốp bốp", "lộp độp/lóp đóp", "lộp độp/lọp đọp",
        "lộp độp/lốp đốp", "lu bù/lu bu", "lu bù/lù bù", "lu bù/lú bú", "mụ mị/mủ mỉ", "năm kia/năm kìa", "ve vẩy/ve vảy",
        "xúng xính/xùng xình", "bình tĩnh/bình tinh", "chứng từ/chủng tử", "danh từ/danh tự", "dò la/đố lá", "đám hỏi/đâm hơi",
        "đối đầu/đời đầu", "gối đầu/gội đầu", "quan trọng/quan trong", "tái chế/tài chế", "thủ kho/thủ khố",
        "tiến hành/tiện hành", "tình trạng/tinh tráng", "trấn tĩnh/trấn tinh"],
}
rows = []
for (a, b), (pq, nhom, ly) in PQ.items():
    d = dem.get((a, b))
    rows.append({"tu": a, "doc_khac": b, "nhom": nhom, "ppm_tu": d["ppm_tu"] if d else "-", "ppm_doc": d["ppm_doc"] if d else "-",
                 "ti_le": d["ti_le"] if d else "-", "coi_so": d["coi"] if d else "-", "phan_quyet": pq, "ly_do": ly})
for nhom, cap in KHONG_DO_NHOM.items():
    for c in cap:
        a, b = c.split("/")
        rows.append({"tu": a, "doc_khac": b, "nhom": "-", "ppm_tu": "-", "ppm_doc": "-", "ti_le": "-", "coi_so": "-",
                     "phan_quyet": "KHONG_DO", "ly_do": nhom})
write_tsv(HERE / "t9-phan-quyet.tsv", list(rows[0].keys()), rows)
from collections import Counter
print(Counter(r["phan_quyet"] for r in rows))
