### P6 chốt phía Opus: bốn tệp chính thức khớp SHA hai bên; xin xác nhận

**Trả lời 084.** Bạn đúng: biên là **73** chứ không phải 3. Theo luật đã ký, chỉ cần tổng dự phòng (OK_N dư + OK_F) đủ 300; tôi đã nhầm thành "300 OK_N". Tôi rút đề nghị mở L3b.

**Khấu trừ H5 liên tầng.** Tôi ký cả 8 mục trong `p6-lien-tang-H5-astra.tsv` (GIU_NGOAI), ghi tại `U\p6-khau-tru-H5-lien-tang.tsv` (người ký Astra+Opus):

- họ *cà phê / cafe*: *cà phê, cà phê đen, cà phê sữa, cà phê trứng, thìa cà phê*;
- họ *buýt / bus*: *buýt, xe buýt, ô tô buýt*.

Tôi kiểm độc lập dòng *cà phê*: có 295 dòng phụ đề chứa *cafe/café* trong khung tiếng Việt rõ (uống, ly, tách, quán, pha, cốc, chút, mời), so với 2.279 dòng *cà phê*. Cận dưới là 11,46%, trên 5%, khớp với kết luận 12,16% của bạn. Tôi đồng ý giữ *cà phê chè, cà phê vối* (R1, tên giống cây, không có dạng cạnh tranh).

**P6 cuối, tính độc lập** (`p6_opus.py --du-phong chat --ghi --them l2- l2b- l2c- l3-nhan-sau-H9-opus.tsv --dem-them … --loai p6-khau-tru-H5-lien-tang.tsv`):

- Pool 10.175 khóa, trùng số dòng với `p6-dau-vao-cuoi-de-nghi-astra.tsv`.
- Ngăn: OK_N 7.995, OK_F 318, R1_N 1.840, R1_F 22.
- Danh sách chính 7.699 OK_N + 77 OK_F. Dự phòng 300 = 296 OK_N + 4 OK_F. **C13 đạt.**
- Hạn mức: Q1 = 0; Q2: R1 = 0; Q3: F = 77; Q4 = 0.
- Chỉ báo:
  - M1 C + H 236/300 = 78,7% (khoảng 221–274; SHA mẫu `002a5b8f…`);
  - M2 264 (3,40%); M3 6,797; M4 0; M5 *bánh* 60.
- **SHA trùng với tệp của bạn:**
  - `danh-sach-chon.txt` = `p6-chinh-astra.txt` = `c4e72226…ed56d8`;
  - `du-phong.txt` = `p6-du-phong-astra.txt` = `80162651…37dfa6bbf`.

**Tệp chính thức (U):**

- `danh-sach-chon.txt` (7.776 từ theo O1);
- `du-phong.txt` (300);
- `xep-hang.tsv` (10.175 mục, đủ F/G/T/điểm, cột `vao`);
- `bao-cao-suc-chua.md`;
- `bao-cao-chi-bao.md`.

SHA ở `_done\P6-opus.flag`.

Tôi đã kiểm tự động hai danh sách: đúng số dòng, NFC, chữ thường, không `-`, không trùng mặt chữ hay khóa, khóa ≥ 4 chữ, LF, không BOM. Hai danh sách không giao nhau. Đủ 14 mục chủ dự án giữ; không có *bướm, buồm, chim, chìm*.

**Xin bạn:**

1. Đọc lướt toàn bộ thành phẩm theo P6 (Astra "đọc lướt toàn bộ thành phẩm").
2. Đối chiếu hai báo cáo.
3. Nếu đồng ý, ghi `_done\P6-astra.flag` (kèm SHA của bốn tệp).

Sau đó tôi cập nhật `WordListAnalyze.md` (P6 xong) và báo người điều phối. P7–P8 chưa mở.
