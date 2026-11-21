# Rà và thay danh sách chính — báo cáo chung vòng 1

**Ngày:** 21/11/2026. **Gốc:** `1c3f504`, nhánh `analyze/ra-thay-chinh`. **Soạn:** SA-Opus. **Duyệt:** SA-Astra, lượt 1 và lượt 2 đều "changes requested" (`ho-so/astra/ra-thay-chinh/round-1-review-drafts.md`, mục "Lượt duyệt 2"). Bản này đã sửa theo cả hai lượt, rồi ghi kết quả thỏa thuận của hai SA theo D-rtc-5 (`ho-so/{opus,astra}/ra-thay-chinh/thoa-thuan-*`) và quyết định D-rtc-6 của chủ dự án (`0253bb0`); nhật ký sửa ở `ho-so/opus/ra-thay-chinh/round-1-revision-1.md`.

**Nguồn:**

- hai bản phân tích, hai bản rà chéo, phiếu duyệt nháp của Astra (`ho-so/astra/ra-thay-chinh/evidence/rd1-*`, `rd2-*`);
- ba bảng hợp nhất `ra-thay-chinh-h7.tsv`, `ra-thay-chinh-h5.tsv`, `ra-thay-chinh-thay-the.tsv`, do `ho-so/opus/ra-thay-chinh/evidence/hop-nhat-rtc.py` ghép:
  - phiếu hiện hành của Astra là phiếu mới nhất (rd2, rồi rd1); phiếu v1 và phiếu sau rà chéo chỉ còn ở cột lịch sử;
  - mọi mã được ánh xạ bằng bảng đầy đủ, mã lạ làm script dừng;
  - cột `nguon_*` ghi tệp:dòng của phiếu gốc.

**Viết tắt:** `AT` = `analyzing-tools`; `TC` = `AT/tieu-chi-thong-nhat.md`; `RD` = `ho-so/astra/ra-thay-chinh/evidence/`; r = PPM(cách đọc khác) / PPM(từ chính).

## 1. Tóm tắt

1. **Thay 116 từ chính:** 104 từ hai SA đồng thuận ở thỏa thuận S1–S3, 3 từ theo quyết định của chủ dự án (D-rtc-6) và 9 từ hai SA đồng ý thay khi khép mục mở (T-rtc-15, T-rtc-16).
   - H7, 92 từ: 3 K0 (*phản bác, tính khí, niêu*) và 89 K1. Trong 89 K1 có *thái*, 13 khóa Opus nhận sau duyệt nháp (*bền bỉ, ca nhạc, cắm đầu, choàng, giao, lề đường, ngao, nguyên, nhồi, sàng, sông, thôn, tiệm*), 3 khóa của thỏa thuận (*cò trắng, sân ga, trăng tròn*) và 3 khóa chủ dự án quyết thay (*vòng, thuần, xuân*); thêm *chậm, cổng, mặt nước, thiếu, trán* khi khép mục mở.
   - H5, 24 từ:
     - loại c: *chòng chành, bồ kết, rau dền, ngoảnh, phấp phới, già dặn, dây chun, dây thun, phí phạm, lấn át, rầm rầm*;
     - loại f: *cải xoong, xà bông, xà phòng*, đã cộng dạng phân cách, Astra xác nhận số (C9);
     - CHO_LOAI, không phát hành ở bản này: *co rúm, xù xì, rầm rộ, chơ vơ, xập xình, su hào, loay hoay*.
     - khép mục mở: *chun, thun* (H5e rồi c), *tép riu* (c, thiếu dữ liệu).
2. **Thỏa thuận theo D-rtc-5** (không dùng SA-Fable; `ho-so/{opus,astra}/ra-thay-chinh/thoa-thuan-*`):
   - S1: K1 cho *cò trắng, sân ga, trăng tròn*; K2 (giữ, hai SA ký) cho *húng, hững hờ, phù dâu, thắm thiết* (T-rtc-12);
   - S2: bảy từ CHO_LOAI, không phát hành (T-rtc-13);
   - S3: tính lại S2/S3 theo P6 trên tập ra cuối (T-rtc-14).
3. **Chủ dự án đã trả lời Q-rtc-O1** (D-rtc-6, `0253bb0`):
   - thay *vòng, thuần, xuân* (K1, chặn khóa);
   - giữ *lưới, phòng ngủ, tường, thị trường, khiến, ngại, trạm* (K2, hai SA ký kèm lý do).
4. **Hai SA đã khép mục mở** (T-rtc-15 đến T-rtc-18; `ho-so/astra/ra-thay-chinh/khep-muc-mo-1.*`, `ho-so/opus/ra-thay-chinh/khep-muc-mo-1-opus.*`): 282 trong 286 dòng.
   - 46 khóa H7 chờ: giữ 37 (29 K2 hai bên ký, 8 không đỏ); thay 6; 3 chủ dự án quyết giữ (D-rtc-7).
   - 27 dòng H5: giữ 21; thay *chun, thun, tép riu*; khép 3 dòng đã ra hay không vào.
   - 8 cờ từ vào: giữ 6; không nhận *làm cỗ*, *rướn*.
   - Gói K2 205 khóa: hai bên ký 204; *bạn thân* chủ dự án quyết giữ (D-rtc-7). Tổng chữ ký chung: 238 sau khi Astra ký 4 khóa của D-rtc-7 (T-rtc-20).
   - **Chủ dự án đã trả lời Q-rtc-O2** (D-rtc-7, `2cc6aec`): giữ *cần cù, tiền lương, triệu, bạn thân* (K2; hai SA đã ký).
5. **Mặc định theo hợp đồng đã ký:** từ chính còn tranh chấp hay còn chờ mà không khép được thì không phát hành.
   - K2 chưa đủ hai chữ ký thì không vào bản 1 (TC:167, :202, :525).
   - Phản đối hợp lệ còn giữ sau một lần phản biện thì không phát hành (TC:190–191).
   - "Chờ" là chưa được nhận ở bản 1 (TC:12).
6. **Từ vào** (mô phỏng theo hạng S4 đã khóa; thứ tự cuối tính lại theo T-rtc-14): 118 dự phòng không-F dùng được (120, bỏ *làm cỗ*, *rướn*). Tập 116: 116 từ vào (106 tầng A, 10 tầng C; hạng 8.096–8.245), còn 2 dự bị. Opus đã tính lại theo T-rtc-14 (`ho-so/opus/ra-thay-chinh/evidence/xep-lai-rtc.*`): tập vào và hai dự bị (*cả nghĩ*, rồi *cửu chương*) không đổi; chờ chương trình độc lập của Astra (T7). Vì chỉ còn 2 dự bị, chủ dự án cho mở chu kỳ HM tối đa 25 từ (Q-rtc-A2, D-rtc-8, `2cc6aec`); HM chỉ lấp ghế sau dự phòng (kế hoạch mục 6.1).
   - **Chu kỳ HM đã thỏa thuận (T-rtc-19):** 25 HM theo hạng, đều qua H1–H9; 5 K2 hai SA ký (*biển, bí mật, vận hành, chia, ngắn gọn*); không chọn *cơ quan* (H6 nhóm 3) và *mình* (lớp F).
7. **Báo tử:** không có từ chính nào mang khóa `baotu`; ghi `baotu` K1 (T-dpv2-7).
8. **Chữ ký K2 cũ giữ nguyên (9):** *bình, di động, khảm, kính, nướng, phết, thầy, thổi, trứng*. *gián* giữ theo quyết định 5. OI-RTC-KY-CU đã rút.
9. **D6:** năm nguồn ghim đều có bản đúng byte (C17). D6 chạy trong một vùng riêng ngoài worktree.
10. **Câu hỏi:** không còn câu hỏi mở. Đã trả lời: Q-rtc-O1 (D-rtc-6), Q-rtc-O2 (D-rtc-7), Q-rtc-A2 (D-rtc-8). Q-rtc-A3 chưa kích hoạt. A1 đã rút. Kế hoạch chưa Final: chỉ còn chương trình chấm độc lập của Astra (T7, OI-RTC-P6) và chữ ký kế hoạch của hai SA.

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
| DONG_THUAN_THAY | 89 | Hai bên K0 hoặc K1: thay từ, chặn khóa (gồm 6 khóa của T-rtc-15) |
| CHU_DU_AN_THAY | 3 | *vòng, thuần, xuân*: chủ dự án quyết thay (D-rtc-6) |
| CHU_DU_AN_GIU_DA_KY_PHIEU | 11 | *lưới, phòng ngủ, tường, thị trường, khiến, ngại, trạm* (D-rtc-6) và *cần cù, tiền lương, triệu, bạn thân* (D-rtc-7): chủ dự án quyết giữ; hai SA đã ký K2 |
| GIU_CHU_KY_CU | 9 | K2 đã ký từ trước (C3) |
| GIU_QUYET_DINH_CHU | 1 | *gián* (C4) |
| DONG_THUAN_GIU_DA_KY_PHIEU | 226 | Hai bên giữ, hai SA đã ký K2 trong phiếu khép mục mở (197 khóa của gói, 29 khóa H7 chờ) |
| DONG_THUAN_GIU | 10 | Cách đọc không đỏ: *đồng ý*, *đuốc* và 8 khóa H7 chờ |

**46 khóa H7 chờ đã khép (T-rtc-15):** chi tiết ở `ra-thay-chinh-h7.tsv` (cột `nguon_astra`, `chu_ky_phieu`).

### 3.2. H5 theo cặp (`ra-thay-chinh-h5.tsv`, 65 cặp)

| Trạng thái | Số cặp | Cặp |
|---|---:|---|
| DONG_THUAN_THAY | 17 | Như C10, ba cặp H5f ở C9, *chun*/*thun* (hai chiều) và *tép riu* (T-rtc-16) |
| DONG_THUAN_THAY_CHO_LOAI | 7 | *co rúm, xù xì, rầm rộ, chơ vơ, xập xình, su hào, loay hoay*: CHO_LOAI, không phát hành ở bản này (T-rtc-13) |
| DONG_THUAN_QUA | 15 | Như C12, cộng 4 cặp đạt loại c theo số (T-rtc-16) |
| DONG_THUAN_DA_RA | 2 | *lằng nhằng*/*loằng nhoằng*, *xà bông*/*sà bông*: từ đã ra vì cổng khác |
| DONG_THUAN_KHONG_CHO_VAO | 1 | *qua quýt*/*qua quít*: mục dự phòng, không vào |
| DONG_THUAN_KHAC_TU | 23 | Như C13, cộng 17 dòng khép mục mở (khác từ hay không lập họ, T-rtc-16) |

Các dòng H5 chờ đã khép hết (T-rtc-16).

### 3.3. Thay và vào (`ra-thay-chinh-thay-the.tsv`)

Bảng có bốn vai trò: RA (116), VAO (116), DU_BI (2), HM (25; cột `tang` = HM, D-rtc-8). Từ vào không ghép đôi với từ ra theo dòng: tập vào là 116 mục đầu của thứ tự chọn.

- **Từ ra:** 116: 106 đồng thuận, 7 đồng thuận với nhãn CHO_LOAI, 3 theo D-rtc-6; tất cả ở ngăn OK không-F.
- **Từ vào:** mô phỏng theo hạng S4 đã khóa (`xep-hang.tsv`, cột `hang`); thứ tự cuối tính lại theo T-rtc-14. Bỏ qua:
  - mục F khi F đã đủ 77 (76 mục);
  - tầng D (6 mục);
  - hai cổng còn mở: *loằng ngoằng* (chờ H5), *ngoại trừ* (chờ H7);
  - *qua quýt* (họ c trượt);
  - *làm cỗ*, *rướn* (không nhận ở T-rtc-17).
- **Kết quả:** 116 từ vào (106 A, 10 C; hạng 8.096–8.245); còn 2 dự bị. Sau thay: 7.776 từ, 7.776 khóa, F = 77, R1 = 0. Chủ dự án giữ cả 4 từ của Q-rtc-O2 (D-rtc-7). Đệm thêm: chu kỳ HM tối đa 25 từ (D-rtc-8), xếp sau dự phòng.
- **Nhánh kiểm:**
  - thêm *theo* (lớp F) vào tập ra: 117 ra, 117 vào, F = 77. Hạn mức được cập nhật mỗi lần nhận.
- **Quan hệ với bản nháp trước:** 87 từ vào đầu trùng thứ tự bản nháp trước. 24 từ vào trong kịch bản cũ của Astra là tập con của 87 từ này; giao với 24 từ đầu là 23 (Astra có *nhá nhem*, 24 từ đầu có *làm cỗ*).

**Cờ từ vào:** đã khép (T-rtc-10, T-rtc-17). Giữ *đưa đò, nặng cân, thẳng đơ, thay lông, xoành xoạch, thụp, loáng thoáng, mang máng, xầm xì*; không nhận *làm cỗ*, *rướn*. Đóng riêng cờ không thay cho tái kiểm H1–H9 toàn từ.

## 4. Thỏa thuận và điểm còn lệch

### 4.1. H7: 17 khóa của S1

**Đã thỏa thuận (T-rtc-12):**

- K1, thay: *cò trắng, sân ga, trăng tròn*. Opus nhận K1 của Astra.
- K2, giữ, hai SA ký: *húng, hững hờ, phù dâu, thắm thiết*. Astra nhận K2 của Opus: dáng điệu mạnh, đòn chặn trước hay âm thanh gây thương cảm không tự là bạo lực, thao túng hay cảm xúc đỏ cực mạnh.

**Chủ dự án đã quyết 10 khóa còn lệch (D-rtc-6, `0253bb0`):** thay *vòng, thuần, xuân*; giữ *lưới, phòng ngủ, tường, thị trường, khiến, ngại, trạm* (K2, hai SA ký). Hai lập trường trước quyết định ghi dưới đây. Không ban hành ngưỡng số mới.

- **Opus:** giữ K2. Mỗi khóa dựa vào một tiêu chí K2 đã ký (TC:167) và tiền lệ có dòng:
  - cách đọc hiếm so với từ chính: *vòng* (r 0,017), *lưới* (0,025), *phòng ngủ* (0,031). Tiền lệ: *thầy*/*thây* r 0,016 được ký K2 vì cách đọc hiếm (`chu-ky.tsv:2152–2154`); K1 đã ký thấp nhất là *đường dẫn*/*đường đạn* 0,036 (TC:524);
  - chức danh: *tường*, *thị trường*. Tiền lệ ký không tự động chặn: *độ dốc*/*đô đốc*, *từ trường*/*tù trưởng* (`canh-bao-khong-dau.tsv:89, 214`);
  - phải tách ép: *thuần* (*thụ án*), *xuân* (*xử án*);
  - nghĩa đỏ không chắc: *khiến* (*khiên* là đồ che chắn), *ngại* (*ngai*), *trạm* (*trẫm*; *trảm* r 0,008). Nhóm 3 đã chốt *công chúa, hoàng tử, hoàng hậu* không đỏ (TC:145).
- **Astra:** giữ K1, có nguồn từng khóa (`ho-so/astra/ra-thay-chinh/thoa-thuan-1.tsv`):
  - xét nghĩa nguyên mục thuộc quân sự, quyền lực, tố tụng, tang linh hay lời chê người;
  - PPM cả chuỗi không phải tần suất của nghĩa đỏ, nhưng r thấp cũng không đủ chứng minh cách đọc hiếm;
  - một tiền lệ chức danh không miễn mọi chức danh; khác số khối không tự là tách ép khi cả cụm đã được chứng thực.
- **Hệ quả của D-rtc-6:** 107 từ thay, còn 13 dự bị (sơ bộ). Bảy từ giữ chỉ phát hành khi đủ hai chữ ký K2 (TC:167).

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

### 4.5. Khép mục mở: bốn từ từng lệch, chủ dự án quyết giữ (D-rtc-7)

- **Astra** (`ho-so/astra/ra-thay-chinh/khep-muc-mo-1.*`): thay cả bốn.
  - *cần cù*/*căn cứ*: nghĩa quân sự còn dùng; r 49.
  - *tiền lương*/*tiên lượng*: đánh giá y khoa.
  - *triệu*/*triều*: triều đại thuộc nhóm 3.
  - *bạn thân*/*bán thân*: Astra đọc 38 dòng phụ đề, thấy ít nhất 3 dòng nghĩa mại dâm; đề nghị K1, không K0.
- **Opus** (`ho-so/opus/ra-thay-chinh/khep-muc-mo-1-opus.*`): giữ cả bốn với K2, đã ký.
  - *căn cứ*: nghĩa chính là cơ sở; căn cứ quân sự cùng loại với các cách đọc quân sự chủ dự án đã cho giữ (D-rtc-6).
  - *tiên lượng*: dự đoán, không phải tên bệnh hay thủ thuật.
  - *triều*: từ hoàng gia như *ngai, trẫm* đã cho giữ.
  - *bán thân*: nghĩa chính là nửa người; nghĩa mại dâm là nghĩa phụ; *bạn thân* là từ cốt lõi.
- **Chủ dự án quyết (Q-rtc-O2, D-rtc-7, `2cc6aec`):** giữ cả bốn, K2; hai SA ký "không tự động chặn". Kết quả: 116 từ thay, còn 2 dự bị.

### 4.6. Chu kỳ HM — đã thỏa thuận (T-rtc-19)

- **Astra** (`ho-so/astra/ra-thay-chinh/hm-chu-ky-1.*`): đề xuất 25 HM nhãn OK không-F theo hạng S4 đã khóa (32–1.541). 20 mục đạt; 5 mục Astra ký K2 và chờ Opus. Không chọn *cơ quan* (H6 nhóm 3) và *mình* (lớp F).
- **Opus** (`ho-so/opus/ra-thay-chinh/hm-chu-ky-1-opus.*`): đồng ý cả 25 mục và hai mục không chọn; ký 5 K2.
  - Kiểm lại bằng dữ liệu: tập và thứ tự khớp hạng; khóa không trùng danh sách chính sau thay, 89 dự phòng còn lại, 110 khóa chặn cũ và 94 khóa chặn mới (92 khóa từ ra vì H7, `baotu`, `lamco`); nhãn OK, không lớp F.
  - Cách đọc cùng khóa lấy từ HND, Kaikki và `opus-counts.tsv`; số H5 của Astra đạt luật c/d.
  - *ngả ngớn*: Kaikki và HND không ghi nghĩa tục hay tình dục người lớn, nên không phải K0.
- **Kết quả:** không có điểm lệch, không có câu hỏi cho chủ dự án. Tính lại S4 cho cùng 25 mục, cùng thứ tự.

## 5. Câu hỏi và mục mở

- Câu hỏi: `ra-thay-chinh-cau-hoi.md`.
  - Không còn câu hỏi mở. Đã trả lời: Q-rtc-O1 (D-rtc-6; câu hỏi và câu trả lời ở `0253bb0`), Q-rtc-O2 (D-rtc-7) và Q-rtc-A2 (D-rtc-8) (ở `2cc6aec`). Q-rtc-S1, S2, S3 đã khép bằng thỏa thuận (T-rtc-12 đến T-rtc-14); lập luận từng mục ở `ho-so/{opus,astra}/ra-thay-chinh/thoa-thuan-*`.
  - Chưa kích hoạt: Q-rtc-A3 (kế hoạch mục 12.2).
- Mục mở và quy trình hai SA khép chúng: `ra-thay-chinh-ke-hoach.md` mục 12. OI-RTC-HM đã khép (T-rtc-19); còn OI-RTC-P6 (chương trình chấm của Astra, T7).
- Không còn K0 nào tranh chấp, nên không có câu hỏi K0 cho chủ dự án. Các cách đọc có thể là K0 trong 46 khóa chờ (*ghen*/*ghèn*, *tình tứ*, *trường*/*truồng*) phải xét nguồn trước; nếu hai SA còn tranh cãi một khóa K0 thì gửi chủ dự án (TC:164).
