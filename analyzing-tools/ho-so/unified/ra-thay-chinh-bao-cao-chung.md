# Rà và thay danh sách chính — báo cáo chung vòng 1

**Ngày:** 21/11/2026. **Gốc:** `1c3f504`, nhánh `analyze/ra-thay-chinh`. **Soạn:** SA-Opus. **Duyệt:** SA-Astra, lượt 1 và lượt 2 đều "changes requested" (`ho-so/astra/ra-thay-chinh/round-1-review-drafts.md`, mục "Lượt duyệt 2"). Bản này đã sửa theo cả hai lượt, rồi ghi kết quả thỏa thuận của hai SA theo D-rtc-5 (`ho-so/{opus,astra}/ra-thay-chinh/thoa-thuan-*`); nhật ký sửa ở `ho-so/opus/ra-thay-chinh/round-1-revision-1.md`.

**Nguồn:**

- hai bản phân tích, hai bản rà chéo, phiếu duyệt nháp của Astra (`ho-so/astra/ra-thay-chinh/evidence/rd1-*`, `rd2-*`);
- ba bảng hợp nhất `ra-thay-chinh-h7.tsv`, `ra-thay-chinh-h5.tsv`, `ra-thay-chinh-thay-the.tsv`, do `ho-so/opus/ra-thay-chinh/evidence/hop-nhat-rtc.py` ghép:
  - phiếu hiện hành của Astra là phiếu mới nhất (rd2, rồi rd1); phiếu v1 và phiếu sau rà chéo chỉ còn ở cột lịch sử;
  - mọi mã được ánh xạ bằng bảng đầy đủ, mã lạ làm script dừng;
  - cột `nguon_*` ghi tệp:dòng của phiếu gốc.

**Viết tắt:** `AT` = `analyzing-tools`; `TC` = `AT/tieu-chi-thong-nhat.md`; `RD` = `ho-so/astra/ra-thay-chinh/evidence/`; r = PPM(cách đọc khác) / PPM(từ chính).

## 1. Tóm tắt

1. **Hai bên đồng thuận thay 104 từ chính:**
   - H7, 83 từ: 2 K0 (*phản bác, tính khí*) và 81 K1. Trong 81 K1 có *thái*, 13 khóa Opus nhận sau duyệt nháp (*bền bỉ, ca nhạc, cắm đầu, choàng, giao, lề đường, ngao, nguyên, nhồi, sàng, sông, thôn, tiệm*) và 3 khóa của thỏa thuận (*cò trắng, sân ga, trăng tròn*).
   - H5, 21 từ:
     - loại c: *chòng chành, bồ kết, rau dền, ngoảnh, phấp phới, già dặn, dây chun, dây thun, phí phạm, lấn át, rầm rầm*;
     - loại f: *cải xoong, xà bông, xà phòng*, đã cộng dạng phân cách, Astra xác nhận số (C9);
     - CHO_LOAI, không phát hành ở bản này: *co rúm, xù xì, rầm rộ, chơ vơ, xập xình, su hào, loay hoay*.
2. **Thỏa thuận theo D-rtc-5** (không dùng SA-Fable; `ho-so/{opus,astra}/ra-thay-chinh/thoa-thuan-*`):
   - S1: K1 cho *cò trắng, sân ga, trăng tròn*; K2 (giữ, hai SA ký) cho *húng, hững hờ, phù dâu, thắm thiết* (T-rtc-12);
   - S2: bảy từ CHO_LOAI, không phát hành (T-rtc-13);
   - S3: tính lại S2/S3 theo P6 trên tập ra cuối (T-rtc-14).
3. **Câu hỏi cho chủ dự án: Q-rtc-O1**, 10 từ hai SA còn lệch: *khiến, lưới, ngại, phòng ngủ, thị trường, thuần, trạm, tường, vòng, xuân*. Astra muốn thay, Opus muốn giữ.
   - Theo Opus cả 10: 104 từ thay, còn 16 dự bị.
   - Theo Astra cả 10: 114 từ thay, còn 6 dự bị.
4. **Còn chờ, hai SA khép theo kế hoạch mục 12.1:**
   - 46 khóa H7 Astra chờ thêm căn cứ;
   - 27 dòng H5: 14 quan hệ Opus xếp khác từ, 9 cặp từng bị ghép nhầm thành QUA, *chun*/*thun* (hai chiều), *hì hục*/*hì hụi*, *qua quýt*/*qua quít*;
   - 8 trong 11 cờ của từ vào và dự bị (3 cờ đã đóng chung);
   - chữ ký K2 mới cho 198 khóa.
5. **Mặc định theo hợp đồng đã ký:** từ chính còn tranh chấp hay còn chờ mà không khép được thì không phát hành.
   - K2 chưa đủ hai chữ ký thì không vào bản 1 (TC:167, :202, :525).
   - Phản đối hợp lệ còn giữ sau một lần phản biện thì không phát hành (TC:190–191).
   - "Chờ" là chưa được nhận ở bản 1 (TC:12).
6. **Từ vào** (mô phỏng theo hạng S4 đã khóa; thứ tự cuối tính lại theo T-rtc-14): 104 dự phòng đầu (99 tầng A, 5 tầng C; hạng 8.096–8.218). Còn 16 trong 120 nguồn không-F qua lọc sơ bộ. Hỏi Q-rtc-A2 ngay khi kiểm sức chứa trước Final cho thấy thiếu, hoặc khi trượt D6/D7 sau khi chủ dự án duyệt làm thiếu ghế.
7. **Báo tử:** không có từ chính nào mang khóa `baotu`; ghi `baotu` K1 (T-dpv2-7).
8. **Chữ ký K2 cũ giữ nguyên (9):** *bình, di động, khảm, kính, nướng, phết, thầy, thổi, trứng*. *gián* giữ theo quyết định 5. OI-RTC-KY-CU đã rút.
9. **D6:** năm nguồn ghim đều có bản đúng byte (C17). D6 chạy trong một vùng riêng ngoài worktree.
10. **Câu hỏi:** Q-rtc-O1 gửi chủ dự án. Q-rtc-A2, A3 chưa kích hoạt (kế hoạch mục 12.2). A1 đã rút. Kế hoạch chưa Final.

## 2. Kết luận chung

| # | Kết luận | Chứng cứ |
|---|---|---|
| C1 | Đầu vào tái lập đúng: 632 cặp H5 trên 474 từ; 1.177 cặp H7 trên 634 khóa | Hai phân tích độc lập |
| C2 | `baotu` không thuộc danh sách chính; ghi K1 khi triển khai, không có ghế nào phải thay vì báo tử | `AT/blocked_keys.tsv`; `du-phong-v2-ke-hoach.md:422` |
| C3 | Giữ chín chữ ký K2 cũ: *bình, di động, khảm, kính, nướng, phết, thầy, thổi, trứng*. Lý do ký cũ thiếu một mặt chữ (*bịnh, trừng*) không tự là chứng cứ mới; OI-RTC-KY-CU rút. *kinh* đã được nêu trong lý do ký của *kính*. *nướng*, *phết* do Astra phát hiện ở lượt duyệt 2 | `chu-ky.tsv:134–135, 786–787, 1270–1271, 1338–1339, 1831–1832, 1872–1873, 2152–2154, 2198–2199`; `RD/rd1-H7-bo-sung.tsv:4–5`; `RD/rd1-H7-phan-xu.tsv:27`; `RD/rd2-K2-da-ky.tsv:2–3` |
| C4 | *gián* giữ theo quyết định 5; Q-rtc-A1 rút | `WordListAnalyze.md:150`; `RD/cr1-Astra-sua-H7.tsv:7` |
| C5 | K0: *phản bác* ↔ *phân bắc* (chất thải người); *tính khí* ↔ *tinh khí* (vi.wiktionary trỏ tới *tinh dịch*, mà `tinhdich` là K0) | vi.wiktionary rev 1892186, 1930782 |
| C6 | *bố mẹ* ↔ *bỏ mẹ* là K1: nhãn *offensive*, không phải *vulgar*, nên không xếp K0 | enwiktionary rev 84835723 |
| C7 | Astra nhận hướng giữ cho 29 khóa (28 khóa và *kính*); các khóa K2 trong đó vẫn cần đủ hai chữ ký. *đồng ý*, *đuốc*: cách đọc không đỏ | `RD/rd1-H7-phan-xu.tsv` (NHAN_HUONG_GIU_H7, NHAN_K2_CU) |
| C8 | *thái* ↔ *thai* là K1 (Astra nhận). *chung cư*, *sắn dây* là K2 (Astra nhận lập trường Opus) | `RD/rd1-H7-phan-xu.tsv:47`; `RD/rd1-H7-bo-sung.tsv:2–3` |
| C9 | H5f đã đo đủ dạng phân cách. *cải xoong*: phụ đề 4 + 0 + 0 lượt, so với 0 → dưới 20, loại (web 42/0). *xà phòng*: phụ đề 181/289 = 62,6%, web 3.895/4.215 = 92,4%, cả hai dưới 95% → loại cả *xà bông* và *xà phòng*. Kết luận không phụ thuộc bộ lọc nghi vắt từ hay độ nhạy dòng trùng. Astra kiểm lại phép cộng, ngưỡng và hash kho, nhận thay cả ba | `ho-so/opus/ra-thay-chinh/evidence/dem-h5f.tsv`, `cap-h5f.tsv`; TC:127; `RD/rd2-H5-xac-nhan.tsv:2–4` |
| C10 | H5 loại c, thiếu dữ liệu: *chòng chành, bồ kết, rau dền, ngoảnh, phấp phới, già dặn, dây chun, dây thun, phí phạm, rầm rầm*. *lấn át*: lấn áp 10/75 lượt phụ đề (độ nhạy 9/64), c hay d đều trượt | `ra-thay-chinh-h5.tsv`; enwiktionary *già dặn* rev 80169171, *rần rần* rev 89902128 |
| C11 | 8 cặp i/y (H5b) qua. *qua quýt*/*qua quít* không thuộc H5b vì vần có phụ âm cuối; họ c riêng còn chờ nên chưa cho *qua quýt* vào | `ho-so/opus/ra-thay-chinh/evidence/dem-h5b.tsv`; `ho-so/unified/tap-luat-P2-v4.json:575` |
| C12 | 11 cặp QUA thật: 8 H5b, *rong ruổi*, *trưng bày* và *bít tết* (họ đã đăng ký: c, 183/3 phụ đề, 362/4 web, QUA_RIENG_H5). 9 cặp từng ghi QUA do lỗi ghép chuỗi nay về trạng thái chờ | `AT/spelling_families.tsv:258`; `RD/rd1-H5-qua-gia.tsv:2–10` |
| C13 | Khác từ: *bóng láng*/*bóng loáng*, *thiện chí*/*thiện trí*, *buồn lòng*/*buồm lòng*, *tâm trí*/*tâm chí*, *run run*/*rung rung*. 19 đối chứng chỉ là tên riêng viết hoa | `RD/rd1-H5-quan-he-bo-sung.tsv:2–4`; `ra-thay-chinh-h5.tsv` |
| C14 | *chun*/*thun* không phải hai từ khác hẳn: cùng danh từ dây đàn hồi, mặt chữ còn nghĩa khác. Xử theo H5e: đọc mẫu theo nghĩa, chưa phân định thì chờ | `RD/rd1-H5-quan-he-bo-sung.tsv:5–6`; TC:126 |
| C15 | Chữ CHO của bộ sinh không tự là phản đối hợp lệ. Phản đối cần mã cổng, quan hệ, nghĩa hay số cụ thể và người phản đối | TC:180–194 |
| C16 | Mọi từ vào có câu viết sạch mới. Không bù dự phòng về 205 hay 300. Mỗi lần chọn cập nhật F và R1. Nghiệm thu dùng F ≤ 77, không bắt F = 77 | TC:202, 307, 407; `ho-so/unified/p6-tinh-doc-lap-astra.py:12, 83–88` |
| C17 | D6: OPUS và GUIDE khớp băm ở byte checkout (CRLF); ASTRA và FAMILIES khớp ở blob Git (LF); WIKT_VI khớp ở bản lưu ngoài repo (`1f0abd…`, 34.422.366 byte). Vì vậy không chạy D6 bằng cách đổi cả repo sang LF | `AT/d6-tham-chieu.json`; `AT/d6-kiem.py:371–378, 528–531, 545–560` |
| C18 | Sức chứa: 120 dự phòng OK không-F qua lọc sơ bộ (108 A, 12 C). *ngoại trừ* là OK-F nên không trừ khỏi ngăn không-F. Đây chỉ là nguồn sau lọc sơ bộ, chưa khép H1–H9 và nghĩa mới | `AT/du-phong-phan-loai.tsv:94, 125, 148`; `RD/rd1-audit-summary.json` |
| C19 | Thứ tự 120 nguồn theo hạng đã khóa không đổi giữa các bản nháp: tám mục cuối khớp `unprepared_tail` của Astra. Trung vị PPM sạch: tập 87 của bản nháp trước, từ ra 1,706 và từ vào 0,0762 (khớp số của Astra); tập 101, từ ra 1,766 và từ vào 0,0729. Số 0,704/0,070 là của tập 38 cũ | `ho-so/opus/ra-thay-chinh/evidence/hop-nhat-rtc.log` |
| C20 | Bỏ hai lối tắt "r ≥ 0,2" và "khóa một âm tiết luôn là K2" của Opus vòng 1. Mốc 0,035 chỉ là thước đối chiếu tiền lệ của Opus, không phải luật mới | `ho-so/opus/ra-thay-chinh/round-1-cross-review.md` mục 2.1 |

## 3. Tóm tắt từng bảng (chi tiết trong TSV)

### 3.1. H7 theo khóa (`ra-thay-chinh-h7.tsv`, 349 khóa)

| Trạng thái | Số khóa | Ý nghĩa |
|---|---:|---|
| DONG_THUAN_THAY | 83 | Hai bên K0 hoặc K1: thay từ, chặn khóa |
| TRANH_CHAP | 10 | Astra K1, Opus K2: *khiến, lưới, ngại, phòng ngủ, thị trường, thuần, trạm, tường, vòng, xuân* (Q-rtc-O1, chủ dự án quyết) |
| CHO_CAN_CU | 46 | Opus K2 hoặc không đỏ; Astra chờ thêm căn cứ (OI-RTC-H7-CHO) |
| GIU_CHU_KY_CU | 9 | K2 đã ký (C3) |
| GIU_QUYET_DINH_CHU | 1 | *gián* (C4) |
| DONG_THUAN_GIU_CAN_KY_K2 | 198 | Hai bên giữ, gồm 4 khóa S1 của T-rtc-12; còn phải ký K2 mới đủ hai bên (OI-RTC-K2-KY) |
| DONG_THUAN_GIU | 2 | *đồng ý*, *đuốc*: cách đọc không đỏ |

**46 khóa chờ:** *áo ngủ, bảng, bề mặt, bể bơi, cần cù, chậm, chân đất, chậu, chung, cổ đông, công đoạn, cổng, cuống, điểm nhấn, điều hành, đinh, đồ bạc, đông đúc, ghen, họ hàng, hoang đảo, hoang sơ, khác, khuy, làm khó, lỗi thời, mặt nước, nắng, ngáp, nghèo, niêu, nóng, ong thợ, quyển, rãnh, rung động, thiếu, thính, tích, tiền lương, tình tứ, tổng, trán, triệu, trường, vất vả*.

### 3.2. H5 theo cặp (`ra-thay-chinh-h5.tsv`, 65 cặp)

| Trạng thái | Số cặp | Cặp |
|---|---:|---|
| DONG_THUAN_THAY | 14 | Như C10 (gồm *lấn át*) và ba cặp H5f ở C9: *cải xoong*/*cải soong*, *xà bông*/*xà phòng* (hai chiều) |
| DONG_THUAN_THAY_CHO_LOAI | 7 | *co rúm, xù xì, rầm rộ, chơ vơ, xập xình, su hào, loay hoay*: CHO_LOAI, không phát hành ở bản này (T-rtc-13) |
| DONG_THUAN_QUA | 11 | Như C12 |
| DONG_THUAN_KHAC_TU | 6 | Như C13 |
| CHO_CAN_CU | 27 | Xem dưới bảng |

27 cặp chờ căn cứ (OI-RTC-H5-QH, OI-RTC-H5E):

- **Opus xếp QUA, Astra chờ xác nhận quan hệ (9):** *bảng hiệu, cột mốc, hạt dẻ, lằng nhằng*/*loằng nhoằng, lòng vòng, nuốt chửng, theo dõi, thư giãn, xà bông*/*sà bông*.
- **Opus xếp khác từ, Astra chờ nguồn (14):** *bộc phát* (hai cặp), *dí dỏm, giỡn, giun, lăn tăn, lon ton, ọp ẹp, rậm rạp, ròng rã, ru rú, sền sệt, tép riu, xanh*/*sanh*.
- **Còn lại (4):** *chun*/*thun* hai chiều (H5e), *hì hục*/*hì hụi* (T-dpv2-4 không kết luận cặp này), *qua quýt*/*qua quít* (dự phòng, họ c chờ).

Ca chờ quan hệ không làm từ chính rời danh sách khi không có phản đối hợp lệ (C15). Riêng *chun*/*thun* là ca H5e có quan hệ thật, nên phải đọc mẫu.

### 3.3. Thay và vào (`ra-thay-chinh-thay-the.tsv`)

Bảng có bốn vai trò: RA (104), RA_NEU_CHU_DU_AN_THEO_ASTRA (10), VAO (104), DU_BI (16). Từ vào không ghép đôi với từ ra theo dòng: tập vào là 104 mục đầu của thứ tự chọn.

- **Từ ra:** 104 đồng thuận, trong đó 7 từ mang nhãn CHO_LOAI; tất cả ở ngăn OK không-F.
- **Từ vào:** mô phỏng theo hạng S4 đã khóa (`xep-hang.tsv`, cột `hang`); thứ tự cuối tính lại theo T-rtc-14. Bỏ qua:
  - mục F khi F đã đủ 77 (76 mục);
  - tầng D (6 mục);
  - hai cổng còn mở: *loằng ngoằng* (chờ H5), *ngoại trừ* (chờ H7);
  - *qua quýt* (họ c đang chờ).
- **Kết quả:** 104 từ vào (99 A, 5 C; hạng 8.096–8.218); còn 16 dự bị (hạng tới 8.248). Sau thay: 7.776 từ, 7.776 khóa, F = 77, R1 = 0.
- **Nhánh kiểm:**
  - thêm *theo* (lớp F) vào tập ra: 105 ra, 105 vào, F = 77. Hạn mức được cập nhật mỗi lần nhận;
  - Q-rtc-O1 theo Astra cả 10 từ: 114 ra, 114 vào, còn 6 dự bị.
- **Quan hệ với bản nháp trước:** 87 từ vào đầu trùng thứ tự bản nháp trước. 24 từ vào trong kịch bản cũ của Astra là tập con của 87 từ này; giao với 24 từ đầu là 23 (Astra có *nhá nhem*, 24 từ đầu có *làm cỗ*).

**Cờ cần đọc** (cột `can_soat`), phải khép trước Final (OI-RTC-VAO):

- từ vào (9): *đưa đò, làm cỗ, thay lông, mang máng* (cách đọc khác vượt mốc còi); *xoành xoạch, thụp, loáng thoáng, nặng cân, rướn* (đối chứng H5 trong bảng ứng viên của Astra);
- dự bị (2): *xầm xì* (H5), *thẳng đơ* (cách đọc khác).
- **Đã đóng chung 3 cờ** (Astra đề nghị ở `RD/rd2-de-xuat-dong-co.tsv:2–4`, Opus nhận): *đưa đò*/*dưa đỏ* không đỏ; *nặng cân*/*lặng câm* khác từ; *thẳng đơ*/*thang độ* không đỏ. Đóng riêng cờ không thay cho tái kiểm H1–H9 toàn từ.
- **Còn 8 cờ.** *làm cỗ*/*làm cỏ* phải xét cả nghĩa bóng tàn sát của *làm cỏ*, không chỉ nghĩa làm vườn.

## 4. Thỏa thuận và điểm còn lệch

### 4.1. H7: 17 khóa của S1

**Đã thỏa thuận (T-rtc-12):**

- K1, thay: *cò trắng, sân ga, trăng tròn*. Opus nhận K1 của Astra.
- K2, giữ, hai SA ký: *húng, hững hờ, phù dâu, thắm thiết*. Astra nhận K2 của Opus: dáng điệu mạnh, đòn chặn trước hay âm thanh gây thương cảm không tự là bạo lực, thao túng hay cảm xúc đỏ cực mạnh.

**Còn lệch, chủ dự án quyết (Q-rtc-O1):** 10 khóa. Hai bên không ban hành ngưỡng số mới.

- **Opus:** giữ K2. Mỗi khóa dựa vào một tiêu chí K2 đã ký (TC:167) và tiền lệ có dòng:
  - cách đọc hiếm so với từ chính: *vòng* (r 0,017), *lưới* (0,025), *phòng ngủ* (0,031). Tiền lệ: *thầy*/*thây* r 0,016 được ký K2 vì cách đọc hiếm (`chu-ky.tsv:2152–2154`); K1 đã ký thấp nhất là *đường dẫn*/*đường đạn* 0,036 (TC:524);
  - chức danh: *tường*, *thị trường*. Tiền lệ ký không tự động chặn: *độ dốc*/*đô đốc*, *từ trường*/*tù trưởng* (`canh-bao-khong-dau.tsv:89, 214`);
  - phải tách ép: *thuần* (*thụ án*), *xuân* (*xử án*);
  - nghĩa đỏ không chắc: *khiến* (*khiên* là đồ che chắn), *ngại* (*ngai*), *trạm* (*trẫm*; *trảm* r 0,008). Nhóm 3 đã chốt *công chúa, hoàng tử, hoàng hậu* không đỏ (TC:145).
- **Astra:** giữ K1, có nguồn từng khóa (`ho-so/astra/ra-thay-chinh/thoa-thuan-1.tsv`):
  - xét nghĩa nguyên mục thuộc quân sự, quyền lực, tố tụng, tang linh hay lời chê người;
  - PPM cả chuỗi không phải tần suất của nghĩa đỏ, nhưng r thấp cũng không đủ chứng minh cách đọc hiếm;
  - một tiền lệ chức danh không miễn mọi chức danh; khác số khối không tự là tách ép khi cả cụm đã được chứng thực.
- **Hệ quả:** theo Opus, 104 từ thay, còn 16 dự bị; theo Astra, 114 và 6. Chủ dự án chưa quyết thì 10 từ này không phát hành (TC:167, :190–191).

### 4.2. H5: 7 từ của S2 — đã thỏa thuận (T-rtc-13)

- **Kết quả:** ghi CHO_LOAI, không phát hành ở bản này (thay cả bảy). Không bắt buộc tra thêm. Có căn cứ loại d về sau thì vẫn phải đạt hợp đồng đếm, chữ ký khi thiếu dữ liệu và luật CHO_SAT_NGUONG.
- **Hai lập trường trước thỏa thuận:**
  - Opus: đầu mục chữ thường trong HND là căn cứ loại c (TC:116). Tiền lệ: 34 họ c, 3 họ d khi dạng kia chỉ có ở Viet39K/Viet74K (Astra đếm lại: `ho-so/astra/ra-thay-chinh/evidence/rd2-HND-tien-le.tsv`).
  - Astra: có mặt trong HND chưa chứng minh dạng kia là cách viết chuẩn của cùng từ hay là lỗi; chưa có căn cứ thì CHO_LOAI (TC:118).
- **Vì sao thỏa thuận được:** cả hai lập trường đều dẫn tới không phát hành ở bản này (loại c thì trượt; CHO_LOAI thì chưa được nhận, TC:12). Opus nhận nhãn CHO_LOAI.

### 4.3. Thứ tự chọn từ vào — đã thỏa thuận (T-rtc-14)

- Yêu cầu có "P6/P7/phát hành riêng" (`ra-thay-chinh-yeu-cau.md:19`), và P6 chấm mọi mục đã qua cổng (TC:227, :402). Opus nhận tính lại thay cho giữ hạng cũ.
- Rổ chấm: mọi mục qua H1–H9 có nhãn; mục loại ở D6 chỉ bị bỏ lúc chọn, vì D6 là cổng của câu nghĩa ở P7, không phải cổng của từ ở P6.
- S4 mới được khóa một lần trước khi viết nghĩa. Dự bị là phần chưa dùng của cùng hàng đợi, tối đa 25 nếu đủ. Giữ trọng số, ưu tiên tầng và luật hòa.
- Ở tập ra 101, Astra đo được cùng tập vào nhưng đổi thứ tự ở 31 vị trí, gồm dự bị 104/105 (`RD/rd2-audit-summary.json`, `S4_O101`). Danh sách từ vào hiện tại là mô phỏng theo hạng đã khóa; tập vào cuối chạy bằng hai chương trình (T7).

### 4.4. Đính chính đã nhận

**Astra sửa Opus (nhận):**

- lỗi ghép mã H5: `"QUA" in ah` khớp cả CHO_XAC_NHAN_QUAN_HE, tạo 9 đồng thuận QUA giả. Đã thay bằng bảng ánh xạ đủ mã;
- bảng H7 phải dùng phiếu sau duyệt; bỏ cắt lý do; thêm tệp:dòng;
- sức chứa 120, không phải 119; trung vị phải ghi đúng mẫu (C18, C19);
- vòng chọn cũ không giảm `slack_f` mỗi lần nhận (nhánh *theo* cho F152 và 7.775 từ). Đã sửa;
- cờ còi của từ vào không được thêm điều kiện r; hàm H5b phải đúng hợp đồng;
- D6 không chạy được bằng cách đổi cả repo sang LF (C17);
- *mất mặt*, *đớn đau* chỉ là tiền lệ phân loại K2 chưa ký, không phải tiền lệ đã ký giữ;
- quan hệ *chun*/*thun* là H5e, không phải khác từ;
- H5f phải cộng các dạng phân cách: đây là hợp đồng (TC:127), không phải điểm tranh chấp.

**Astra sửa Opus ở lượt duyệt 2 (nhận):**

- *nướng*, *phết* đã có chữ ký K2 cũ (`chu-ky.tsv:1831–1832, 1872–1873`), nên số khóa cần ký mới là 194, không phải 196;
- "chạy lại P6" không được ghi là ngoài phạm vi (mục 4.3);
- Q-rtc-A2 phải hỏi được ngay khi thấy thiếu ghế trước Final, không chờ D6/D7;
- cột `nguon_opus` phải có số dòng của phiếu trong `doi-chieu-v2.py`. Đã bổ sung;
- hàm chọn chỉ kiểm trần R1 388, chưa chặn R1 thay ghế OK; hàm H5b chưa sinh mọi tổ hợp (thiếu *tỷ mỷ* cho *tỉ mỉ*). Đã sửa và thêm phép tự kiểm; kết quả mô phỏng không đổi;
- cờ *làm cỗ*/*làm cỏ* phải xét nghĩa bóng của *làm cỏ*.

**Astra tự sửa ở lượt duyệt 2:** *kinh* đã được nêu trong lý do ký của *kính*; lượt duyệt 1 bỏ sót chữ ký chứ không phải chữ ký thiếu đối chứng.

**Opus sửa Astra (Astra đã nhận):**

- *bít tết* đã đăng ký (C12);
- chữ ký K2 cũ của *kính* giữ nguyên;
- *chung cư*, *sắn dây* là K2.

**Opus tự sửa:** lý do K2 trong bản nháp trước ghi tiền lệ "*đôn đốc*/*đô đốc*". Đúng là *độ dốc*/*đô đốc* (`canh-bao-khong-dau.tsv:89`).

## 5. Câu hỏi và mục mở

- Câu hỏi: `ra-thay-chinh-cau-hoi.md`.
  - Gửi chủ dự án: Q-rtc-O1 (10 từ). Q-rtc-S1, S2, S3 đã khép bằng thỏa thuận (T-rtc-12 đến T-rtc-14); lập luận từng mục ở `ho-so/{opus,astra}/ra-thay-chinh/thoa-thuan-*`.
  - Chưa kích hoạt: Q-rtc-A2, Q-rtc-A3 (kế hoạch mục 12.2).
- Mục mở và quy trình hai SA khép chúng: `ra-thay-chinh-ke-hoach.md` mục 12.
- Không còn K0 nào tranh chấp, nên không có câu hỏi K0 cho chủ dự án. Các cách đọc có thể là K0 trong 46 khóa chờ (*ghen*/*ghèn*, *tình tứ*, *trường*/*truồng*) phải xét nguồn trước; nếu hai SA còn tranh cãi một khóa K0 thì gửi chủ dự án (TC:164).
