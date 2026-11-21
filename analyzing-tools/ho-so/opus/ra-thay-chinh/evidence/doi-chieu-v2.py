"""Lập trường của Opus sau rà chéo vòng 1 (v2): phán quyết H7 theo khóa và H5 theo cặp ở những chỗ lệch với Astra.

Thước hai trục (round-1-cross-review.md mục 2.1), neo theo các phân xử đã ký: canh-bao-khong-dau.tsv,
blocked_keys.tsv (P2) và chu-ky.tsv.
- Nặng (S1): nghĩa chính của cách đọc thuộc nhóm đỏ H6 theo đúng các ví dụ trong bảng: chết, tang, mai táng, uyển
  ngữ chết; vũ khí, chiến tranh, địch, tấn công; tội phạm, xử phạt, tố tụng, giam giữ; tên bệnh, triệu chứng (H6 ghi
  ngứa ngáy); tình dục, thai nghén; rượu, thuốc lá, cờ bạc (H6 ghi lá bài); đảng phái, bầu cử, quyền lực; thảm họa
  (H6 ghi ngập úng); thần thánh, từ tôn giáo; chửi rủa, miệt thị, chê người (H6 ghi la mắng, tham lam, giả dối).
- Nhẹ (M): đa nghĩa mà nghĩa chính trung tính; chỉ là hình vị trong từ ghép; cụm phải tách ép; tiếng lóng hay chê nhẹ;
  biểu tượng, chức danh (tiền lệ ký: độ dốc ↔ đô đốc "không tự động chặn", canh-bao-khong-dau.tsv:89, tieu-chi-thong-nhat.md:526); dáng điệu, cảm xúc (tiền lệ phân loại K2 chưa ký: đón dâu ↔ đớn đau, mát mắt ↔ mất mặt, canh-bao-khong-dau.tsv:87, :124; K2 chưa đủ hai chữ ký thì không vào bản 1, tieu-chi-thong-nhat.md:164, :525).
- Tự nhiên: r = PPM(cách đọc)/PPM(từ chính) ≥ 0,035. Mốc này nằm giữa các tiền lệ K2 (thây 0,016; bĩnh 0,012;
  bịnh 0,017) và K1 thấp nhất (đường dẫn/đường đạn 0,036; tầng/tang 0,072; phát/phạt 0,138).
- K1 = S1 và r ≥ 0,035. K2 = có nghĩa đỏ nhưng M, hoặc r < 0,035. K2 đã có hai chữ ký giữ nguyên (H9).
"""

_K1_MOI = {  # Opus chuyển sang K1 sau rà chéo
    "nhàu": "nhậu G7, r 12,5", "cuốc": "cược G7, r 32", "chồn": "chôn G4, r 3,2", "than": "thần G4, r 1,8",
    "măng": "mắng G9, r 1,4", "ngọc": "ngốc G9, r 1,5", "đích": "địch G1, r 0,83",
    "giấc": "giặc G1, r 0,36", "kiến": "kiện G2, r 0,43", "ngắt": "ngất G5, r 0,37; ngạt 0,053",
    "ngụm": "ngủm G4, r 0,35", "ngựa": "ngứa G5 (H6 ngứa ngáy), r 0,19", "nhai": "nhãi G9, r 0,33",
    "diều": "điếu G7 r 1,9; điêu G9 r 0,59", "chỏm": "chôm G2 (ăn cắp), r 13,5", "ăn diện": "ân điển G4, r 1,94",
    "dàn ý": "dân ý G3 (trưng cầu), r 5,7", "mời mọc": "moi móc G9, r 0,94", "bà chủ": "bá chủ G3, r 0,18",
    "bảo hành": "bạo hành G1, r 0,050", "báo động": "bạo động G1, r 0,059", "bố mẹ": "bỏ mẹ G9 (chửi), r 0,070",
    "bộ ba": "bỏ bà G9 (chửi), r 0,17", "cộng sự": "công sự G1, r 0,052", "đánh bại": "đánh bài G7, r 0,052",
    "đột phá": "đốt phá G1/G2, r 0,087", "giảm": "giam G2, r 0,099", "gọng": "gông G2, r 0,29",
    "hâm mộ": "hầm mộ G4, r 0,11", "hoa mai": "hoả mai G1 (súng), r 1,37", "hỏi thăm": "hội thẩm G2, r 0,18",
    "làng": "lăng G4 (lăng mộ), r 0,11", "nhốt": "nhọt G5, r 0,047", "thảm": "tham G9 (tham lam), r 0,24",
    "thớt": "thọt G5, r 0,22", "trời": "trói G2, r 0,16",
    "thái": "thai G6, r 1,6",
}
_K2_DA_KY = {
    "bình": "chu-ky.tsv:134–135 (binh, bĩnh)", "thầy": "chu-ky.tsv:2152–2154", "thổi": "chu-ky.tsv:2198–2199",
    "khảm": "chu-ky.tsv:1270–1271 (lý do có nêu nghĩa nhà tù của khám)", "kính": "chu-ky.tsv:1338–1339",
    "di động": "chu-ky.tsv:786–787 (đi đồng); enwiktionary chỉ ghi dialectal, colloquial (rev 84662196)",
    "nướng": "chu-ky.tsv:1831–1832 (nương, nường); Astra nêu ở lượt duyệt 2 (rd2-K2-da-ky.tsv:2)",
    "phết": "chu-ky.tsv:1872–1873 (phét, phệt); Astra nêu ở lượt duyệt 2 (rd2-K2-da-ky.tsv:3)",
}
_K2 = {  # Opus giữ K2; Astra đề nghị K1/K0
    "gián": "M: nghĩa chính của gian là gian nhà, gian hàng; nghĩa dối trá chủ yếu trong từ ghép",
    "chiên": "M: chiến đứng riêng là tiếng lóng (chiến quá); nghĩa chiến tranh cần từ ghép",
    "khiến": "M: khiên là đồ che, không phải vũ khí sát thương", "ngại": "M: ngai (ngai vàng) là biểu tượng",
    "trạm": "M: trẫm là xưng hô cổ, r 0,036 sát mốc; trảm r 0,008", "chồng": "r 0,005", "có mặt": "r 0,008",
    "phòng": "r 0,004", "quên": "r 0,007", "treo": "r 0,005", "theo": "r 0,001", "kiểu": "r 0,002",
    "lo lắng": "r 0,004", "khăn": "r 0,010", "kể cả": "r 0,010", "lưới": "r 0,025", "chốt": "r 0,019",
    "chú ý": "r 0,005", "bản đồ": "r 0,018", "bộ đồ": "r 0,015", "đa năng": "r 0,022", "liên quan": "r 0,003",
    "phòng ngủ": "r 0,031", "quà tặng": "r 0,031; quả tang chỉ trong bắt quả tang", "tung": "r 0,014",
    "vòng": "r 0,017", "đề cử": "dê cụ r 0,005, dưới 0,3", "cò trắng": "M: biểu tượng; tiền lệ ký độ dốc ↔ đô đốc (canh-bao-khong-dau.tsv:89; tieu-chi-thong-nhat.md:526)",
    "nhồi": "M: nhói là cảm giác", "thôn": "M: thộn (ngây thộn), chê nhẹ", "giảng": "M: giàng hiếm, vùng",
    "giao": "M: giáo đa nghĩa", "húng": "M: hung đa nghĩa (màu hung)", "ngao": "M: ngáo, ngạo là lóng/hình vị",
    "nguyên": "M: nguyền, nguyện là hình vị", "sông": "M: sòng là hình vị (sòng bạc), cũng nghĩa sòng phẳng",
    "sàng": "M: sảng chủ yếu trong mê sảng; r 0,038", "thuần": "M: thụ án phải tách ép",
    "xuân": "M: xử án phải tách ép", "tường": "M: tướng đa nghĩa; tiền lệ ký độ dốc ↔ đô đốc (canh-bao-khong-dau.tsv:89; tieu-chi-thong-nhat.md:526)", "choàng": "M: choáng còn nghĩa choáng ngợp",
    "chuông": "M: chưởng (phim chưởng)", "bền bỉ": "M: bên bị là cụm pháp lý hẹp", "ca nhạc": "M: cà nhắc tả dáng đi",
    "cắm đầu": "M: cầm đầu nghĩa chung là đứng đầu", "sân ga": "M: sa ngã là thói xấu nói chung",
    "thị trường": "M: thị trưởng là chức danh", "lề đường": "M: lê dương là tên lịch sử", "làm mẫu": "M: làm màu là lóng",
    "phong bì": "M: phòng bị là đề phòng", "phù dâu": "M: phủ đầu là dằn mặt", "trăng tròn": "M: trắng trợn là trạng từ chê",
    "thắm thiết": "M: thảm thiết tả tiếng khóc; tiền lệ phân loại K2 chưa ký (đón dâu ↔ đớn đau, canh-bao-khong-dau.tsv:87)", "trình diễn": "M: trình diện",
    "nhâm nhi": "M: nhảm nhí chê lời nói, không chê người; tiền lệ phân loại K2 chưa ký (mát mắt ↔ mất mặt, canh-bao-khong-dau.tsv:124)",
    "đông đúc": "M: động dục, động đực; tiền lệ đồng tình/động tình KHONG_TU_DONG",
    "tiệm": "M: tiêm là việc y tế thường ngày (như đánh răng, kính cận ở H6), không phải y khoa chuyên biệt",
    "ngáp": "M, nhận ý Astra: ngập còn nghĩa chìm, ngập việc; H6 chỉ ghi ngập úng",
    "hững hờ": "M: hùng hổ tả dáng điệu (còi tương đối: 0,248 ≥ 0,056 PPM)",
}
H7 = {}
for _w, _y in _K1_MOI.items():
    H7[_w] = ("K1", "đổi sang K1: " + _y)
for _w, _y in _K2_DA_KY.items():
    H7[_w] = ("K2_DA_KY", "giữ K2 đã ký, không có chứng cứ mới: " + _y)
for _w, _y in _K2.items():
    H7[_w] = ("K2", _y)
_K1_RD1 = {  # Opus nhận K1 sau khi đọc phiếu duyệt nháp của Astra (rd1-H7-phan-xu.tsv): nhất quán với các K1 đã
    # đồng thuận và với H6 "không làm sạch nghĩa bằng cách chọn nghĩa phụ lành" (tieu-chi-thong-nhat.md:139)
    "bền bỉ": "bên bị là thuật ngữ tố tụng (nhóm 2 có nhân chứng, vô can); r 0,078",
    "ca nhạc": "cà nhắc tả tật ở chân, nhất quán với thớt/thọt đã đồng thuận K1; r 0,26",
    "cắm đầu": "nghĩa thường gặp của cầm đầu là đứng đầu nhóm làm việc không chính đáng (nhóm 2); r 4,3",
    "choàng": "choáng là triệu chứng (nhóm 5, như ngứa ngáy); không làm sạch bằng nghĩa choáng ngợp; r 4,8",
    "giao": "giáo đứng riêng là vũ khí (nhóm 1); không làm sạch bằng giàn giáo hay hình vị giáo dục; r 0,117",
    "lề đường": "lê dương chỉ lính quân đoàn (nhóm 1, như hậu bị); r 0,13",
    "ngao": "ngạo là khinh người, ngáo là tiếng lóng chê người (nhóm 9), nhất quán với ngọc/ngốc; r 0,77 và 1,05",
    "nguyên": "nguyền là nguyền rủa (nhóm 4, 9), dùng độc lập; r 0,31",
    "nhồi": "nhói là cảm giác đau, nhất quán với ngựa/ngứa (H6 ghi ngứa ngáy); r 0,074",
    "sàng": "sảng là triệu chứng (nhóm 5), nhất quán với mê mẩn/mê man đã đồng thuận K1; r 0,038",
    "sông": "sòng đứng riêng là nơi đánh bạc (nhóm 7 có lá bài, lai rai); không làm sạch bằng sòng phẳng; "
            "r 0,076, giữa tầng/tang 0,072 và phát/phạt 0,138 đã ký K1",
    "thôn": "thộn chê người đần, nhất quán với ngọc/ngốc đã đồng thuận K1; r 0,29",
    "tiệm": "tiêm là thủ thuật y khoa như trồng răng (nhóm 5), khác đánh răng; r 2,58",
}
for _w, _y in _K1_RD1.items():
    H7[_w] = ("K1", "đổi sang K1 sau duyệt nháp vòng 1: " + _y)
_K2_RD1 = {  # Opus vẫn giữ K2 sau duyệt nháp; mỗi lý do dựa vào một tiêu chí K2 đã ký (tieu-chi-thong-nhat.md:167:
    # hiếm, phải tách ép, chỉ khớp một âm tiết, nghĩa đỏ không chắc) và tiền lệ có dòng
    "cò trắng": "nghĩa đỏ không chắc: cờ trắng là biểu tượng (đầu hàng, đình chiến, nghĩa bóng chịu thua), không phải "
                "bạo lực hay vũ khí; tiền lệ: chào cờ không đỏ (H6 nhóm 3), độ dốc ↔ đô đốc ký không tự động chặn "
                "(canh-bao-khong-dau.tsv:89; tieu-chi-thong-nhat.md:526); r 18,9",
    "húng": "nghĩa đỏ không chắc: nghĩa thường gặp của hung là dữ tợn hay màu hung; tính dữ không có trong ví dụ của nhóm "
            "1 (bạo lực, vũ khí, quân sự) hay nhóm 9 (thô lỗ, la mắng); r 10,8",
    "hững hờ": "nghĩa đỏ không chắc: hùng hổ tả dáng điệu hăng; tiền lệ phân loại K2 của cách đọc tả dáng điệu, cảm xúc "
               "(mát mắt ↔ mất mặt, đón dâu ↔ đớn đau, canh-bao-khong-dau.tsv:124, :87); còi tương đối 0,248 ≥ 0,056 PPM",
    "khiến": "nghĩa đỏ không chắc: khiên là đồ che chắn, không gây sát thương; nhóm 1 không loại dao cạo, móng vuốt; r 0,052",
    "lưới": "hiếm so với từ chính: r 0,025, dưới K1 đã ký thấp nhất (đường đạn 0,036), gần K2 đã ký thầy/thây 0,016; "
            "lười là chê nhẹ, khác vô dụng, ăn bám",
    "ngại": "nghĩa đỏ không chắc: ngai là ghế vua, vật thờ; H6 nhóm 3 đã chốt công chúa, hoàng tử, hoàng hậu không đỏ; r 0,25",
    "phòng ngủ": "hiếm so với từ chính: r 0,031 (phòng ngủ rất thông dụng); phòng ngự còn nghĩa thể thao",
    "phù dâu": "nghĩa đỏ không chắc: phủ đầu là ra đòn trước, dằn mặt; không có trong ví dụ nhóm 9; r 0,25",
    "sân ga": "nghĩa đỏ không chắc: sa ngã nói việc sa vào thói xấu, không phải lời chê người hay hành vi nhóm đỏ; r 0,63",
    "thắm thiết": "thảm thiết tả tiếng khóc, nỗi đau; nhóm 9 không loại buồn, khóc; tiền lệ phân loại K2 đón dâu ↔ đớn đau "
                  "(canh-bao-khong-dau.tsv:87); r 0,77",
    "thị trường": "nghĩa đỏ không chắc: thị trưởng là chức danh hành chính; tiền lệ ký chức danh: từ trường ↔ tù trưởng, "
                  "độ dốc ↔ đô đốc không tự động chặn (canh-bao-khong-dau.tsv:214, :89); r 0,070",
    "thuần": "phải tách ép: khóa một khối thuan phải tách thành thu an mới ra thụ án; r 0,081",
    "trạm": "trẫm là xưng hô của vua trong truyện, phim cổ trang, gần nhóm công chúa, hoàng tử đã chốt không đỏ; r 0,036 "
            "sát mốc; trảm hiếm (r 0,008)",
    "trăng tròn": "nghĩa đỏ không chắc: trắng trợn chỉ mức lộ liễu của việc làm, không phải lời chê người; r 0,48",
    "tường": "tiền lệ ký: độ dốc ↔ đô đốc (chức danh quân sự) không tự động chặn (canh-bao-khong-dau.tsv:89; "
             "tieu-chi-thong-nhat.md:526); r 0,093",
    "vòng": "hiếm so với từ chính: r 0,017, ngang K2 đã ký thầy/thây 0,016",
    "xuân": "phải tách ép: khóa một khối xuan phải tách thành xu an mới ra xử án; r 0,064",
}
for _w, _y in _K2_RD1.items():
    H7[_w] = ("K2", "giữ K2 sau duyệt nháp vòng 1: " + _y)
_K1_TT1 = {  # thỏa thuận 1 (D-rtc-5): Opus nhận K1 của Astra (thoa-thuan-1.tsv của hai bên; T-rtc-12)
    "cò trắng": "cờ trắng rất tự nhiên (r 18,9), gắn với chiến sự, đầu hàng; tiền lệ đô đốc là chức danh",
    "sân ga": "sa ngã thường nói sa vào tệ nạn; r 0,63",
    "trăng tròn": "trắng trợn chỉ hành vi ngang ngược, gần nhóm 9; r 0,48",
}
for _w, _y in _K1_TT1.items():
    H7[_w] = ("K1", "thỏa thuận 1, nhận K1: " + _y)
H7["phản bác"] = ("K0", "chấp nhận: phân bắc là chất thải người, có mục vi.wiktionary (rev 1892186)")
H7["tính khí"] = ("K0", "chấp nhận: vi.wiktionary tinh khí trỏ tới tinh dịch (rev 1930782); tinhdich là K0_TU_DIEN")
H7["đồng ý"] = ("KHONG_DO", "đông y là y học cổ truyền, không phải bệnh")
H7["đuốc"] = ("KHONG_DO", "dược là thuốc, dược phẩm; hình vị, không phải bệnh")
H7["sắn dây"] = ("K2", "sửa, nhận ý Astra: sán dây là tên loài; H6 nhóm 10 không loại tên con vật (bọ chét, chuột cống)")
H7["chung cư"] = ("K2", "sửa, nhận ý Astra: chứng cứ là bằng chứng nói chung, không riêng tố tụng như nhân chứng")

H5 = {  # (từ, dạng kia): (lập trường v2, lý do)
    ("dây chun", "dây thun"): ("THAY", "chấp nhận: vi.wiktionary chun 'nghĩa như thun' (rev 2034319), cùng dạng chứng cứ "
                                       "với ngảnh, phất phới, chòng chành; c, phụ đề 7 + 9 < 20"),
    ("dây thun", "dây chun"): ("THAY", "như dây chun/dây thun"),
    ("phí phạm", "phí phạn"): ("THAY", "chấp nhận: vi.wiktionary phí phạn like-entry phí phạm (rev 1314795); c thiếu dữ liệu"),
}
for _p, _y in {("co rúm", "co dúm"): "web 16", ("xù xì", "sù sì"): "phụ đề 8", ("rầm rộ", "rần rộ"): "phụ đề 6",
               ("chơ vơ", "trơ vơ"): "phụ đề 2", ("xập xình", "sập sình"): "phụ đề 8", ("su hào", "xu hào"): "phụ đề 0"}.items():
    H5[_p] = ("THAY", "sửa: dạng kia có trong HND (chữ thường) nên theo tiền lệ là c (spelling_families: 34 c so với 3 d "
                      "khi dạng kia chỉ ở HND 39K/74K); c thiếu dữ liệu (" + _y + ")")
H5[("loay hoay", "lay hoay")] = ("THAY", "sửa: c theo tiền lệ; lay hoay 3/20 phụ đề = 15%, dưới 95% → LOAI_CANH_TRANH")
H5[("lấn át", "lấn áp")] = ("THAY", "giữ: lấn áp 10/75 phụ đề (13,3%), độ nhạy 9/64; c hay d đều loại; ngữ cảnh cùng nghĩa")
H5[("cải xoong", "cải soong")] = ("THAY", "đo đủ dạng phân cách theo H5f (tieu-chi-thong-nhat.md:127), evidence/dem-h5f.tsv: "
                                          "phụ đề cải xoong 4 + cải-xoong 0 + cảixoong 0, phía cải soong 0 → tổng 4 < 20, "
                                          "thiếu dữ liệu; web 42/0. f xử như c → loại (tiền lệ soong/xoong LOAI_CANH_TRANH)")
H5[("già dặn", "già giặn")] = ("THAY", "vòng chung: enwiktionary già dặn rev 80169171 ghi alternative form of già giặn; "
                                      "c, web 4 + 1 < 20 (Astra và Opus cùng kết luận)")
H5[("thiện chí", "thiện trí")] = ("KHONG", "sửa: thiện trí chỉ có dạng viết hoa trong HND (tên riêng); bỏ đăng ký QUA")
_XB = ("đo đủ dạng phân cách theo H5f (tieu-chi-thong-nhat.md:127), evidence/dem-h5f.tsv: phụ đề mọi dòng sạch xà phòng "
       "181 + xà-phòng 0 + xàphòng 0 = 181, xà bông 51 + xà-bông 57 + xàbông 0 = 108 → 181/289 = 62,6% < 95%; web dòng khác "
       "sạch 3.894 + 0 + 1 = 3.895 so với 318 + 2 + 0 = 320 → 92,4% < 95%; không dạng nào đạt 95% ở cả hai kho → loại cả "
       "hai. Không phụ thuộc bộ lọc (bề mặt: phụ đề 185/293, web 3.981/4.302) hay độ nhạy (phụ đề dòng khác 151/254)")
H5[("xà bông", "xà phòng")] = ("THAY", "quan hệ f do Astra phát hiện; " + _XB)
H5[("xà phòng", "xà bông")] = ("THAY", "như xà bông/xà phòng; " + _XB)
H5[("rầm rầm", "rần rần")] = ("THAY", "nhận phản đối mới của Astra (rd1-H5-phan-xu.tsv:13): enwiktionary rần rần rev 89902128 "
                                     "ghi biến thể phương ngữ của rầm rầm → c; dem-h5.tsv: phụ đề 6/5 (dòng khác 5/5), web "
                                     "sạch 2/5 → cả hai kho < 20, thiếu dữ liệu → loại")
H5[("bít tết", "bíp tết")] = ("CUNG_TU_QUA", "họ đã đăng ký: spelling_families.tsv:258 (c; 183/3 phụ đề, 362/4 web; "
                                           "QUA_RIENG_H5); Astra nhận (rd1-H5-phan-xu.tsv:12)")
for _p, _n in {("buồn lòng", "buồm lòng"): 2, ("tâm trí", "tâm chí"): 3, ("run run", "rung rung"): 4}.items():
    H5[_p] = ("KHONG", f"khác từ; Astra nhận NHAN_KHAC_TU (rd1-H5-quan-he-bo-sung.tsv:{_n})")
for _p, _n in {("chun", "thun"): 5, ("thun", "chun"): 6}.items():
    H5[_p] = ("CHO_H5e", "sửa, nhận ý Astra (rd1-H5-quan-he-bo-sung.tsv:" + str(_n) + "): cùng danh từ dây đàn hồi nên "
                         "không gọi là khác từ hoàn toàn; mặt chữ còn nghĩa khác (chun: co lại; thun: vải thun) → H5e, "
                         "không dùng tỉ lệ thô, đọc mẫu ngữ cảnh theo nghĩa (OI-RTC-H5E); chưa phân định thì chờ")
H5[("qua quýt", "qua quít")] = ("CHO_HO_C", "sửa, nhận ý Astra (cr1-H5b-hop-dong.tsv): quýt có phụ âm cuối t nên không "
                                         "thuộc H5b (vần đúng bằng i hoặc y, ho-so/unified/tap-luat-P2-v4.json:575); xét "
                                         "như họ c riêng, chưa có căn cứ loại; mục dự phòng, không đưa vào khi họ còn chờ")
for _p in [("co rúm", "co dúm"), ("xù xì", "sù sì"), ("rầm rộ", "rần rộ"), ("chơ vơ", "trơ vơ"), ("xập xình", "sập sình"),
           ("su hào", "xu hào"), ("loay hoay", "lay hoay")]:
    H5[_p] = ("THAY_CHO_LOAI", "thỏa thuận 1 (T-rtc-13): không phát hành ở bản này; đăng ký họ với loai_H5 = CHO_LOAI, "
                               "ket_luan = KHONG_PHAT_HANH (tieu-chi-thong-nhat.md:12, :118). Lập trường cũ của Opus: " + H5[_p][1])
RA_V2 = {}
