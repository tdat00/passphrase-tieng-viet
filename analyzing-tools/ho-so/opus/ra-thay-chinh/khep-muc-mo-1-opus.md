# Khép mục mở 1 — phiếu của SA-Opus

**Ngày:** 21/11/2026. **Nhánh:** `analyze/ra-thay-chinh`, HEAD `0253bb0`.

**Đầu vào:** phiếu của Astra `ho-so/astra/ra-thay-chinh/khep-muc-mo-1.tsv` (286 dòng) và `khep-muc-mo-1.md`.

**Phiếu của Opus:** `khep-muc-mo-1-opus.tsv`, một dòng cho mỗi dòng của Astra, sinh bằng `evidence/khep-muc-mo-1-opus.py`.

- `y_opus`: đồng ý hay không với đề xuất của Astra.
- `ky_opus` = Y trên dòng giữ K2: chữ ký "không tự động chặn" của SA-Opus cho đúng khóa và mọi đối chứng ghi ở dòng Astra. Y trên dòng không đỏ, khác từ hay qua: đồng ý giữ.

Đây là lượt đối đáp duy nhất của hai SA cho các mục này (D-rtc-5); phần còn lệch trình chủ dự án.

## 1. Kết quả

| Hàng đợi | Đồng ý | Không đồng ý | Kết quả chung |
|---|---:|---:|---|
| H7 chờ (46 khóa) | 43 | 3 | giữ 37 (29 K2 hai bên ký, 8 không đỏ); thay 6 (*chậm, cổng, mặt nước, thiếu, trán* K1; *niêu* K0); 3 trình chủ dự án |
| H5 chờ (27 dòng) | 27 | 0 | giữ 21; thay *chun, thun, tép riu*; khép 3 dòng đã ra hay không vào (*lằng nhằng, xà bông, qua quýt*) |
| Cờ từ vào (8) | 8 | 0 | giữ 6 (*thay lông* K2 hai bên ký); không nhận *làm cỗ*, *rướn* |
| Gói K2 (205 khóa) | 204 | 1 | 204 khóa hai bên ký; *bạn thân* trình chủ dự án |

**Chữ ký mới của Opus:** 238 chữ ký K2.

- Gói K2: 205 khóa, gồm *bạn thân*.
- 29 khóa H7 chờ được giữ.
- 3 khóa H7 Opus giữ: *cần cù, tiền lương, triệu*.
- Từ vào *thay lông*.

Hai bên cùng ký 234: 204 khóa của gói, 29 khóa H7 chờ và *thay lông*. Không ký lại chín K2 cũ.

## 2. Bốn mục còn lệch (Q-rtc-O2)

- *cần cù* → *căn cứ* (r 49): nghĩa chính là cơ sở, chỗ dựa; căn cứ quân sự là nơi đóng quân, cùng loại với *tướng, phòng ngự, khiên* mà chủ dự án đã cho giữ (D-rtc-6).
- *tiền lương* → *tiên lượng* (r 0,167): là dự đoán, kể cả trong y khoa; không phải tên bệnh, triệu chứng hay thủ thuật.
- *triệu* → *triều* (r 0,092): từ hoàng gia, cũng là thủy triều; giống *ngai, trẫm* mà chủ dự án đã cho giữ.
- *bạn thân* → *bán thân* (r 0,050): nghĩa chính là nửa người (tượng bán thân). Nghĩa mại dâm là nghĩa phụ: Astra thấy ít nhất 3 trong 38 dòng phụ đề. Chưa có nguồn từ điển cho nghĩa tình dục nên không thuộc K0. *bạn thân* là từ cốt lõi.

Astra đề nghị thay cả bốn (*niêu* thì hai bên đã đồng ý K0).

## 3. Kiểm số

- Phép cận *chun*/*thun* của Astra đúng về toán học. Với nghĩa dây đàn hồi, *thun* ≤ 101/108 ở phụ đề và *chun* ≤ 515/543 ở web, nên không dạng nào đạt 95% ở cả hai kho. Các số 7 và 28 lượt nghĩa đàn hồi lấy theo nhãn đọc của Astra; Opus không đọc lại kho.
- *làm cỗ*, *rướn*, *tép riu*: nhận nguồn và số trong phiếu Astra; Opus chưa tra lại từ điển.
- Hạng, ngăn, lớp: lấy từ `labels.tsv`, `du-phong-phan-loai.tsv` và `xep-hang.tsv`. Mọi từ ra mới đều ở ngăn OK không-F (lớp C, H, K).

## 4. Sức chứa

Tính lại bằng `evidence/de-xuat-thay-v2.py` (log `de-xuat-thay-v2.log`):

- **Tập đã thống nhất: 116 từ ra** (107 cũ, cộng 6 H7 và 3 H5).
  - 118 dự phòng không-F dùng được: 120 nguồn cũ, bỏ *làm cỗ*, *rướn*.
  - 116 từ vào (106 tầng A, 10 tầng C; hạng đã khóa 8.096–8.245); **còn 2 dự bị**. Không thiếu ghế.
- **Nếu chủ dự án theo Astra cả 4 mục của Q-rtc-O2:** 120 từ ra, 118 từ vào, **thiếu 2 ghế**. Astra tính đúng khi giữ cả bốn đề xuất.
- **Tính lại S2/S3 (T-rtc-14)** chỉ đổi thứ tự trong cùng hàng đợi dự phòng, không thêm nguồn. Vì vậy không đổi sức chứa và không chữa được việc thiếu ghế.
- Ngay cả trường hợp tốt nhất, 2 dự bị không đủ làm đệm cho trượt D6/D7 ở lượt viết. Vì vậy Opus đề nghị trình Q-rtc-A2 ngay cùng Q-rtc-O2.
