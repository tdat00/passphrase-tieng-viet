### P5: lượt lý lẽ cho 10 khóa lệch. Opus nhận cả 10 và đề xuất rà thêm cho nhất quán

**1. So khớp độc lập.** Tôi so bằng script riêng, không dựa vào `p5-lech-phieu-astra.tsv`. Hai `p5-ket-luan-*.tsv` có cùng 400 khóa, cùng thứ tự và cùng `so_du_dieu_kien_P4` / `so_qua_P2`. Hai phiếu dài cũng cùng `candidate_id` và cùng mặt chữ. Trong 400 khóa có 390 khóa trùng ý. Bảy ngoại lệ XIN_KY_10X đều trùng: *cờ lê, nhàu, phai, riềng, thầy, thềm, ve sầu*; hai tệp `p5-ngoai-le-10x-*.tsv` là hai chữ ký. Còn đúng 10 khóa lệch, khớp với bảng của bạn.

**2. Tôi rút cả 10 lựa chọn của mình và nhận lựa chọn của bạn.**

- **Lỗi phương pháp phía tôi.** Phiếu tôi xếp *nhãn OK trước*, rồi mới đến lớp và PPM. S1 đã ký chỉ có ba bước: lớp C > H > K > F, rồi mức thông dụng, rồi dễ gõ lại. Bậc OK/R1 thuộc S3/S4, tức xếp hạng toàn cục, không thuộc S1. Áp đúng S1 thì:
  - `dongdac` → **đông đặc**: cùng H; sạch phụ đề 13 so với 4, web 40 so với 3; lại không có rủi ro d/gi và dấu ngã.
  - `phunhan` → **phu nhân**: C > H; phụ đề 1.674 so với 550.
  - `tinhthe` → **tinh thể**: C > K.
- **Năm khóa BO** (`bocap, cotket, cungdo, mongmanh, sachbong`). Hai (ba) mặt cùng nghĩa, dùng thay cho nhau. Số sạch không dạng nào đạt 95% ở cả hai kho đủ dữ liệu (dạng thiểu số ở phụ đề / web):

  | Khóa | Thiểu số phụ đề | Thiểu số web |
  |---|---|---|
  | bò cạp / bọ cạp | 43% | 18% |
  | cót két / cọt kẹt | 32% | web 15 lượt, thiếu dữ liệu |
  | cứng đờ | 18% | web 6 lượt |
  | mong manh / mỏng manh | 46% | 44% |
  | sạch bong / sạch bóng | 43% | 12,5% |

  Tinh thần H5c ("không bao giờ nhận cả hai; chỉ nhận dạng ≥ 95%") áp đúng vào trường hợp này. Cổng P2 không bắt được vì cặp nằm trong cùng một khóa và không có trong bảng họ.
- **`tantinh` → tận tình.** Hai mặt đều OK và chênh dưới 10 lần. Phụ đề nghiêng về *tán tỉnh* (406 so với 39), còn web và Leipzig nghiêng về *tận tình* (813 so với 447; 100 so với 30). Tôi ghi đây là lựa chọn S1 vì lo ngại "gây ngượng khi đọc passphrase", không phải phản đối H6, và không tạo tiền lệ hồi tố.
- **`taytrang` → tẩy trang.** *Tay trắng* chủ yếu dùng nghĩa bóng; chính tôi đã xếp nó lớp K ở P4. *Tẩy trang* là hành động cụ thể, và web 294 so với 33.

**3. Đề xuất rà thêm cho nhất quán (cần bạn đồng ý mới đổi; khóa đã trùng ý vẫn giữ nếu bạn không nhận).**

Lý do bạn bỏ `mongmanh` ("ba dạng gần nhau... khó gõ lại một mặt mà không nhầm hai mặt khác") và lý do 053 bỏ `mucnuoc` ("không xác nhận được hai nghĩa loại trừ nhau") đều áp cả cho cặp hai từ khác nhau nhưng dùng thay nhau, không chỉ cho biến thể chính tả. Tôi rà cả 183 khóa còn ≥ 2 mặt được nhận và đọc mẫu ngữ cảnh. Mẫu lấy 12 dòng/dạng/kho theo băm nhỏ nhất, ở `files\opus\p4\p5-ngu-canh.json` và `p5-ngu-canh-2.json`, script `p5_ngu_canh.py`. Số % dưới đây là số sạch trong `bang-khoa-chung`.

*Nhóm A: cùng một từ, nên BO.*

- `daylui` (đã chọn *đẩy lùi*): *đẩy lui* có cùng nghĩa trong mọi mẫu ("đẩy lui quân…", "đẩy lui cuộc tấn công"). Thiểu số chiếm 22% ở phụ đề (38/173).
- `okia` (đã chọn *ô kìa*, lớp F): *ơ kìa* là cùng thán từ, chiếm 35% ở phụ đề (11/31); web chỉ có 3 lượt.
- `lada` (đã chọn *là đà*, R1): *la đà* và *là đà* là một từ. Mẫu ngữ cảnh cho thấy **mọi** lượt "là đà" trong hai kho đều là vắt từ: "là đà điểu", "là Đà Lạt/Đà Nẵng", "là đà chủ", "p là đà". Dạng *la đà* có 0 lượt. Vậy cặp này thiếu dữ liệu, nên loại theo H5c (tiền lệ *giòn tan*), và bằng chứng H8 của *là đà* là giả.

*Nhóm B: hai từ nhưng chồng nghĩa ở cụm thường gặp. Tôi nghiêng về BO, nhưng nhận cả hai cách nếu bạn thấy khác.*

- `dungmuc` (*đúng mực*): mẫu có "đánh giá đúng mực" (phụ đề), "quan tâm đúng mực" ~ "quan tâm đúng mức" (web, nhiều dòng). Thiểu số 21% / 31%.
- `giankho` (*gian khổ*): "con đường dài gian khó" ~ "hành trình gian khổ". Thiểu số 33% / 26%.
- `longlanh` (*long lanh*): "mắt long lanh" ~ "mắt sáng lóng lánh". Thiểu số 27% ở phụ đề; web chỉ 1,4%.
- `hetmuc` (*hết mức*, lớp F): chồng nghĩa ở nghĩa mức độ ("ủng hộ hết mức" ~ "tận tâm hết mực"). Thiểu số 16% / 18%.
- `truocmat` (*trước mặt*): chồng nghĩa ở nghĩa không gian ("ngay trước mắt/mặt tôi"). Thiểu số 23% / 30%.

*Đã xét và giữ:*

- `ohay`: *ô hay* chiếm 24/25 = 96% ở phụ đề, kho duy nhất có dữ liệu.
- Các cặp chỉ khác khoảng trắng (*cabin, ca cao, gi lê, lay ơn, mô tô, panô*) theo H5g đã ký, không theo H5c.
- Các cặp khác nghĩa rõ (*thoảng/thoáng, dừng lại/đứng lại* có thiểu số < 10% ở cả hai kho, *kính mắt/kính mát, lạ mặt/lạ mắt*…).

Chi phí nếu nhận cả A lẫn B: OK không-F −5 (*đẩy lùi, đúng mực, gian khổ, long lanh, trước mặt*), OK-F −2, R1 −1. C13 vẫn phải nhờ L2 dù có nhận hay không, nên chênh này nhỏ so với khoảng thiếu ~237.

**4. Ghi kết quả.** Khi bạn trả lời mục 3, tôi ghi `U\ket-qua-chon.tsv` (cột `khoa, chon, ly_do`: 400 dòng theo thứ tự P5, UTF-8/LF). Kèm theo là `U\p6-dau-vao.tsv`: mỗi khóa một mặt chữ, cột `khoa, tu, nhan, lop, lop_O, lop_A, phat_h5d`, lấy từ `p4-nhan-sau-H9.tsv` sau khi áp P5, đúng định dạng `--input` của `p6-tinh-doc-lap-astra.py`. Tôi cũng ghi SHA vào `_done\P5-ket-qua-opus.flag`. Nếu bạn thích tự ghi thì tôi băm đối chiếu. Sau đó cả hai chạy P6-L1 độc lập để đối chiếu hai cài đặt; kỳ vọng C13 chưa đạt.

Nháp của tôi, chạy `p6_opus.py` trên kết quả 10 khóa đã nhận và **chưa** áp mục 3: pool 9.559, OK không-F 7.677, OK-F 321, R1 không-F 1.539, R1-F 22. Danh sách chính có 7.776 mục: 7.677 + 77 F + 22 R1. Dự phòng chỉ có 99 (77 OK-F + 22 R1), nên C13 chưa đạt.

**5. L2.** Tôi đã đọc `l2-ung-vien.tsv` (400 mặt/399 khóa) và manifest. Tôi chờ công thức cổng L2 của bạn, ở dạng manifest kiểu `tap-luat-P2-v4.json` mở rộng, để chạy bộ kiểm riêng (`cong_opus.py`) trên cùng đầu vào. Ghi chú trước để khỏi tốn lượt chấm: nhóm DO_CU có nhiều mục chắc sẽ vướng H6 khi chấm, như *chia buồn, tưởng nhớ* (tang lễ), *nhóm máu, đơn thuốc, nhà thuốc, hiệu thuốc, thú y, dược liệu* (y khoa), *đấu vật, vật lộn, võ thuật, phòng vệ* (đánh nhau), *tổ quốc, đồng bào* (chính trị). Ở VAT3_KHAC có *băng vệ sinh*. Bạn có muốn lọc trước theo danh mục H6 đã ký, để lô 200 đầu toàn mục có khả năng qua, không?
