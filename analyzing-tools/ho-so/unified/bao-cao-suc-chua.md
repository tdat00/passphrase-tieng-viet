# Báo cáo sức chứa P6 (C13)

*Lập bởi Opus ngày 19/11/2026. Hai chương trình độc lập phải cho cùng kết quả: Opus `files\opus\p4\p6_opus.py --du-phong chat`; Astra `U\p6-tinh-doc-lap-astra.py`. Phần đối chiếu cuối do Astra xác nhận ở `_done\P6-astra.flag`.*

## 1. Đầu vào

| Thành phần | Tệp | Số khóa | Ghi chú |
|---|---|---:|---|
| L1 (rổ P1 sau P2, P4/H9, P5) | `p6-dau-vao.tsv` | 9.552 | `p4-nhan-sau-H9.tsv` cộng `ket-qua-chon.tsv` |
| L2A | `l2-nhan-sau-H9-opus.tsv` (trùng byte bản Astra) | 321 | 167 OK, 154 R1 |
| L2B | `l2b-nhan-sau-H9-opus.tsv` (trùng byte) | 148 | 51 OK, 97 R1 |
| L2C | `l2c-nhan-sau-H9-opus.tsv` (trùng byte) | 51 | 8 OK, 43 R1 |
| L3 (mẫu ưu tiên Wiktionary) | `l3-nhan-sau-H9-opus.tsv` | 111 | 102 OK, 9 R1 |
| Khấu trừ có biên bản | `p6-khau-tru-cuoi.tsv` | −27 | Xem mục 4 |
| **Pool vào P6** | | **10.156** | Mỗi khóa một mặt chữ |

Số đếm bốn kho lấy từ `bang-khoa-chung.tsv` cho L1 và từ bảng ứng viên của từng lô bổ sung. Phần OPUS của các bảng này đã được Opus đếm lại độc lập và khớp 100%.

## 2. Ngăn và cửa sức chứa

| Ngăn | Pool | Danh sách chính | Dự phòng |
|---|---:|---:|---:|
| OK không-F | 7.977 | 7.699 | 278 |
| OK-F | 318 | 77 | 22 |
| R1 không-F | 1.839 | 0 | 0 |
| R1-F | 22 | 0 | 0 |
| **Tổng** | **10.156** | **7.776** | **300** |

- **Danh sách chính 7.776 = 7.699 OK không-F + 77 OK-F.**
  - Có đủ 14 mục chủ dự án giữ: *mặt trời, mặt trăng, trái đất, ngân hà, công chúa, hoàng tử, hoàng hậu, mồ hôi, ruồi, gián, chào cờ, ròng rọc, dép lê, bánh chưng*.
  - Không có *bướm, buồm, chim, chìm*.
- **Dự phòng 300 khóa khác nhau**, mỗi khóa có một suất thay hợp ngăn:
  - 278 OK không-F thay OK không-F;
  - 22 OK-F thay 22 trong 77 suất F.
  - Luật đã ký "dự phòng R1 chỉ thay mục R1" được giữ nguyên. Danh sách chính không có R1, nên không dùng dự phòng R1.
- **C13 đạt.** Điều kiện thực tế là OK không-F ≥ 7.922, tức 7.699 + 300 − 77. Pool có 7.977, **dư 55**.
- Chính và dự phòng không trùng khóa. Không mục nào bị khấu trừ còn nằm trong hai danh sách.

## 3. Hạn mức

| # | Hạn mức | Ngưỡng | Thực tế |
|---|---|---|---:|
| Q1 | R2 | 0 | 0 |
| Q2 | R1 | ≤ 388 | 0 |
| Q3 | Lớp F | ≤ 77 | 77 |
| Q4 | K2 chưa đủ hai chữ ký | 0 | 0 |

## 4. Diễn biến và khấu trừ

| Bước | OK không-F | Dự phòng | Thiếu |
|---|---:|---:|---:|
| L1 | 7.674 | 102 | 198 suất |
| + L2A | 7.841 | 219 | 81 |
| + L2B | 7.892 | 270 | 30 |
| + L2C | 7.900 | 278 | 22 |
| + L3 | 8.002 | 300 | 0 |
| − khấu trừ H5 liên tầng (8) | 7.995 | 300 | 0 |
| − khấu trừ sau lượt đọc toàn bộ (19) | **7.977** | **300** | **0** |

Khấu trừ có biên bản trong `p6-khau-tru-cuoi.tsv` (27 mục, hai bên ký):

- **H5 liên tầng (8)** dùng bằng chứng mới thu ở L3, áp đúng H5f đã ký:
  - họ *cà phê / cafe, café*: *cà phê, cà phê đen, cà phê sữa, cà phê trứng, thìa cà phê*. Chỉ tính khung tiếng Việt rõ (uống, ly, tách, quán…), cận dưới ở phụ đề vẫn trên 10%. Hai tên giống cây *cà phê chè, cà phê vối* giữ R1.
  - họ *buýt / bus*: *buýt, xe buýt, ô tô buýt*.
- **Sau lượt đọc toàn bộ 7.776 + 300 dòng (19).** Astra đọc trọn, đề nghị có chứng cứ mẫu ngữ cảnh; Opus lấy mẫu riêng và đồng ý cả 19:
  - nghĩa còn dùng phổ biến thuộc nhóm đỏ H6:
    - *bánh bèo* (lóng chê người);
    - *nóng bỏng, thèm muốn, vuốt ve* (tình dục);
    - *tin mừng, thần tượng, tạ ơn* (tôn giáo);
    - *giáp, chinh phục* (vũ khí, chinh chiếm);
    - *cườm, gây sốt, nghẹt* (bệnh, triệu chứng);
    - *tước* (tước vị, tước quyền);
    - *rình rập* (theo dõi người);
  - đề tài giới, theo đoạn "Danh tính" của H6: *nam tính, nữ tính*;
  - H5 nhất quán với các họ đã xử ở L2C: *quần soóc, tập dượt, xe goòng*. *Xe goòng* là R1, vốn không vào bản chính.

Bản L1/L2/L3 lịch sử giữ nguyên SHA. Khấu trừ chỉ áp ở đầu vào P6 cuối.

## 5. Đầu ra

| Tệp | Nội dung | SHA-256 |
|---|---|---|
| `danh-sach-chon.txt` | 7.776 từ theo O1, UTF-8, LF, có LF cuối | `dfcf4ba63624b0a4cfc92945e22568b0b878e0caf3da4ed83e388fa25a73d4ee` |
| `du-phong.txt` | 300 từ theo O1 | `31647c0b3d984bda3d7f430914bea37ae14ed46cac447128006b9e026fc82496` |
| `xep-hang.tsv` | 10.156 mục: đủ F, G, T, điểm; cột `vao` = CHINH/DU_PHONG/- | `c357aa0523a2527ba5cb118e796146d22ea7e491064c84e969bd0d8dece0aba3` |

Kiểm tự động trên hai danh sách:

- đúng số dòng; NFC; chữ thường; không `-`; một dấu cách giữa các khối;
- không trùng mặt chữ, không trùng khóa; khóa ≥ 4 chữ;
- không BOM, không CR;
- giao giữa danh sách chính và dự phòng bằng 0.

Nguồn của danh sách chính: L1 7.455, L2A 164, L2B 51, L2C 4, L3 102. Nguồn của dự phòng: L1 296, L2C 4.
