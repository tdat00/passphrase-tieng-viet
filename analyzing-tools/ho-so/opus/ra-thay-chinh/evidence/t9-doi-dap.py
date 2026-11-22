"""T9, lượt đối đáp: bảng hợp nhất phía SA-Opus (hợp của 14 cặp Opus và 63 cặp/59 khóa Astra, ca H5c từ vào, phết,
chữ ký thầy, sửa tài liệu). Ghi ../t9-doi-dap.tsv.

Cột ky: Y = Opus ký K2 "không tự động chặn" cho đúng cách đọc ở dòng; N = không ký (K0, K1, loại H5, việc sửa); - = không cần.
Chạy: python -X utf8 -B t9-doi-dap.py
"""
from chung import AT, HERE, OUT, key, out_utf8, rd, write_tsv

out_utf8()
A = AT / "ho-so" / "astra" / "ra-thay-chinh"
ast = [r for r in rd(A / "t9-soat-toan-tap.tsv") if r["trang_thai"] == "CHO_DOI_DAP"]
op = {(r["tu"], r["doc_khac"]): r for r in rd(HERE / "t9-phan-quyet.tsv", mine=True)}
assert len(ast) == 63 and len({r["khoa"] for r in ast}) == 59

DAC_BIET = {  # (từ, cách đọc): (ý Opus, đề xuất chung, ký, lý do)
    ("phết", "phẹt"): ("K0 (nhận)", "K0: THAY phết, chặn phet", "N",
                      "Nhận phản đối của Astra: Kaikki VI:37654 ghi động từ thô tục chỉ việc thải phân; K0 bất kể tần suất (TC:161). "
                      "Khác bĩnh (chu-ky.tsv:134–135, không mang nhãn tục). Chữ ký cũ của phết chỉ xét phét/phệt"),
    ("cau có", "cầu cơ"): ("K1 (nhận)", "K1: THAY cau có, chặn cauco", "N",
                          "Nhận phản đối của Astra: số sạch 47/1, PPM 0,69 vượt cả từ chính 0,52; gọi hồn là việc về người chết; "
                          "số thô của Opus lẫn nhu cầu cơ bản nhưng số sạch vẫn có còi"),
    ("tụ tập", "tu tập"): ("K2 (giữ)", "TRANH_CHAP: trình chủ dự án", "Y",
                          "Tu hành là nghĩa tôn giáo nhẹ, không phải nghi lễ tang hay thần linh; tỉ lệ 0,12. Theo luật chung K1 chỉ cho "
                          "nghĩa đỏ nặng; chủ dự án đã giữ các cách đọc G3 nhẹ (thị trưởng, triều)"),
    ("tử tế", "tư tế"): ("K2 (giữ)", "TRANH_CHAP: trình chủ dự án", "Y",
                        "Chức sắc tôn giáo, nghĩa nhẹ; tỉ lệ 0,073; Astra ký K2 cho ma sơ là danh xưng người tu cùng loại"),
    ("cuống", "cương"): ("K2", "K2 nếu Astra nhận; nếu Astra xếp K0: trình chủ dự án", "Y",
                        "EN:15144 chỉ ghi 'erect' với nhãn trang trọng, không nhãn tục; cương đứng riêng phần lớn là dây cương, cương quyết, "
                        "đề cương, kim cương. Không phải nghĩa phụ tục phổ biến kiểu bướm, chim (TC:162)"),
    ("lông", "lồng"): ("K2", "K2 nếu Astra nhận; nếu Astra xếp K0: trình chủ dự án", "Y",
                      "EN:25441 ghi lồng là cách viết theo giọng Nam của một từ tục, nhãn lóng; không phải nghĩa của từ lồng trong từ điển. "
                      "Người đọc khóa long thấy lông, lồng (cái lồng), lòng, lỏng. Không phổ biến như bướm, chim (TC:162)"),
    ("chính đáng", "chính đảng"): ("K2", "K2", "Y", "Đồng ý Astra: chính trị, 6/48, dưới hai mốc"),
    ("bảng", "băng"): ("K2", "K2, phạm vi gồm băng (đạn, đảng) và báng", "Y",
                      "Đồng ý Astra: hai dòng hiệu lực mới của bảng phải giữ phạm vi băng của hai dòng cũ đã THAY_THE"),
    ("thổi", "thoi"): ("K2", "K2, mở rộng chữ ký sẵn có của thổi", "Y", "Đồng ý Astra: đánh mạnh là nghĩa phụ; thoi chủ yếu là con thoi"),
    ("nghệ", "nghề"): ("K2", "K2", "Y", "Nghĩa phụ 'thông thạo' mang nhãn thô tục ở VI:36995 nhưng nghĩa không tục hay tình dục; nghề nghiệp áp đảo"),
    ("thưởng", "thượng"): ("K2", "K2", "Y", "Nghĩa phụ thô tục ở VI:38436 hiếm so với thượng (cao nhất, thượng hạng); không phổ biến như chim, bướm (TC:162)"),
    ("tận tình", "tán tỉnh"): ("K2", "K2", "Y", "Tán tỉnh là làm quen, không phải tình dục hay thao túng; không thuộc nhóm đỏ nặng dù số cao"),
    ("tuột", "tướt"): ("K2", "K2", "Y", "Chứng bệnh trẻ nhỏ, 3/0; không phải từ tục hay tên chất thải; như tiền lệ bĩnh"),
}
rows = []
for r in ast:
    w, x = r["tu"], r["doi_chung"]
    if (w, x) in DAC_BIET:
        yo, dx, ky, ly = DAC_BIET[(w, x)]
    else:
        yo, dx, ky = "K2", "K2", "Y"
        ly = "Đồng ý Astra: cách đọc hiếm hoặc nghĩa đỏ nhẹ, không chắc; ký đúng đối chứng"
        if (w, x) in op and op[(w, x)]["phan_quyet"] == "K2_DE_XUAT":
            ly = "Hai bên cùng đề xuất K2: " + op[(w, x)]["ly_do"]
    rows.append({"khoa": r["khoa"], "tu_chinh": w, "cach_doc": x, "nguon": f"A:{r['stt']}" + (" O:t9-phan-quyet" if (w, x) in op else ""),
                 "y_opus": yo, "y_astra": r["ket_luan_Astra"], "de_xuat_chung": dx, "ky": ky, "ly_do": ly})
co_ast = {(r["tu"], r["doi_chung"]) for r in ast}
CHI_OPUS = {  # cặp Opus nêu mà Astra không phản đối riêng (Astra: 3.793 cặp không phản đối)
    ("đuôi", "đượi"): ("K2", "GIU: K2 (Astra ký hoặc xếp không đỏ; cả hai cách đều giữ đuôi)", "Y",
                      "Nói lái của đĩ, không mang nhãn tục; theo tiền lệ bình/bĩnh. Khác phẹt (động từ thô tục có trong từ điển)"),
    ("song ngữ", "song ngư"): ("K2", "GIU: K2 hoặc không đỏ", "Y", "Cung hoàng đạo; tiền lệ hoàng đạo"),
    ("tung", "tửng"): ("K2", "GIU: K2 hoặc không đỏ", "Y", "Phần lớn số là tưng tửng"),
    ("mằn mặn", "man man"): ("K2", "GIU: K2 hoặc không đỏ", "Y", "Số web phần lớn là chữ tiếng Anh"),
    ("liễu", "liêu"): ("K2", "GIU: K2 hoặc không đỏ", "Y", "Số gồm quan liêu, liêu xiêu, họ Liêu"),
    ("công cộng", "công công"): ("KHONG_DO", "KHONG_DO", "-", "Như hoàng hậu, công chúa (TC:145)"),
}
for (w, x), (yo, dx, ky, ly) in CHI_OPUS.items():
    assert (w, x) not in co_ast
    rows.append({"khoa": key(w), "tu_chinh": w, "cach_doc": x, "nguon": "O:t9-phan-quyet", "y_opus": yo,
                 "y_astra": "KHONG_PHAN_DOI", "de_xuat_chung": dx, "ky": ky, "ly_do": ly})
KHAC = [
    ("buonthiu", "buồn thiu", "buồn thỉu", "A:t9-soat-toan-tap.md H5", "LOAI c (nhận)", "LOAI_H5C",
     "LOAI c thiếu dữ liệu: rút từ vào, lấp theo hàng đợi; đăng ký họ", "N",
     "Nhận: VI:272859 ghi 'như buồn thiu' (dạng chuẩn ngang hàng, TC:115–118); 9/0 và 0/0 lượt, dưới 20; như bồ kết, rau dền ở đợt này"),
    ("iuxiu", "ỉu xìu", "ỉu xịu", "A:t9-soat-toan-tap.md H5", "LOAI c (nhận)", "LOAI_H5C",
     "LOAI c thiếu dữ liệu: rút từ vào, lấp theo hàng đợi; đăng ký họ", "N", "Nhận: VI:111007 ghi 'như ỉu xìu'; 6/0 và 1/0 lượt, dưới 20"),
    ("daingoang", "dài ngoằng", "dài ngoẵng", "A:t9-soat-toan-tap.md H5", "KHAC_TU", "CAN_XAC_NHAN", "KHAC_TU: giữ", "-",
     "VI:270194 định nghĩa riêng (nét vướng víu), không dẫn về dài ngoằng: khác từ, không lập họ"),
    ("lubu", "lu bù", "lu bu", "A:t9-soat-toan-tap.md H5", "KHAC_TU", "CAN_XAC_NHAN", "KHAC_TU: giữ", "-",
     "VI:267595 dẫn lu bu về bận, không về lu bù; lù bù (HND) là nghĩa khác (bù xù)"),
    ("thay", "thầy", "-", "A:chu-ky.tsv:2152–2154", "Nhận", "SUA", "Sửa chu-ky.tsv: đổi dòng 2154 (Opus, chu-ky-bo-sung) sang THAY_THE; "
     "kiểm mọi K2 đúng một dòng hiệu lực mỗi SA", "-", "Đúng: thầy có ba dòng CO (Astra 1, Opus 2); kiểm T4 của Opus chỉ đếm người ký nên sót"),
    ("-", "WordListAnalyze.md:9101", "-", "A:t9-soat-toan-tap.md", "Nhận", "SUA",
     "Sửa: K0 là nghĩa tục, tình dục người lớn hoặc chỉ chất thải, bất kể tần suất", "-", "Đúng theo TC:161"),
    ("-", "WordListAnalyze.md:9124", "-", "A:t9-soat-toan-tap.md", "Nhận", "SUA", "Sửa: 237 nhãn K2 mới (238 khóa ký, bảng đã có K2 từ trước)", "-",
     "Đã kiểm: labels.tsv có 237 nhãn K2 mới so với HEAD; bảng đã mang K2"),
]
for k, w, x, ng, yo, ya, dx, ky, ly in KHAC:
    rows.append({"khoa": k, "tu_chinh": w, "cach_doc": x, "nguon": ng, "y_opus": yo, "y_astra": ya, "de_xuat_chung": dx, "ky": ky, "ly_do": ly})
write_tsv(OUT / "t9-doi-dap.tsv", list(rows[0].keys()), rows)
from collections import Counter
c = Counter(r["de_xuat_chung"].split(":")[0].split(",")[0].split(" ")[0] for r in rows)
print(len(rows), "dòng;", dict(c), "; Opus ký K2:", sum(r["ky"] == "Y" for r in rows))
