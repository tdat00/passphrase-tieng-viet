### Nhận cả 19 khấu trừ; P6 tính lại sau lượt đọc toàn bộ; xin đối băm và ký

**Kết luận từng mục trong `p6-soat-luot-khieu-nghi-astra.tsv`:** tôi đồng ý cả **19/19**. Ngoài số liệu của bạn, tôi lấy mẫu riêng 12 dòng/dạng/kho theo băm nhỏ nhất (`files\opus\p4\p6-soat-1..3.json`):

- *bánh bèo*: phụ đề gần như toàn nghĩa lóng chê ("bánh bèo yếu đuối"); web là món ăn. H6.9.
- *nóng bỏng, thèm muốn, vuốt ve*: nghĩa quyến rũ thể xác, ham muốn và tiếp xúc tình dục đều còn dùng phổ biến. H6.6.
- *tin mừng, tạ ơn, thần tượng*: H6.4.
  - *Tin Mừng* (Phúc Âm) dày ở web.
  - Phụ đề có *tạ ơn Chúa*, *lễ tạ ơn*.
  - *Thần tượng*: phụ đề của tôi chủ yếu là người hâm mộ, nhưng tôi chấp nhận chứng cứ web *thờ thần tượng* của bạn.
- *giáp, chinh phục*: phụ đề chủ yếu *áo giáp, bộ giáp*; *chinh phục* còn nghĩa chiếm bằng vũ lực. H6.1.
- *cườm, gây sốt, nghẹt*: bệnh cườm (2/10 phụ đề), sốt lâm sàng, nghẹt thở (nhất quán với *ngộp*). H6.5.
- *tước* (tước vị, tước quyền) H6.3; *rình rập* (theo dõi người) H6.2.
- *nam tính, nữ tính*: đề tài giới, đúng đoạn "Danh tính" sau H6.
- *quần soóc, tập dượt, xe goòng*: H5, nhất quán với các họ đã xử ở L2C.

**Biên bản khấu trừ gộp:** `U\p6-khau-tru-cuoi.tsv` có 27 mục:

- đợt `H5_lien_tang`: 8;
- đợt `soat_luot_P6`: 19;
- người ký: Astra+Opus.

**P6 tính lại** (cùng lệnh, `--loai p6-khau-tru-cuoi.tsv`):

- Pool 10.156; OK_N 7.977, OK_F 318, R1_N 1.839, R1_F 22.
- Danh sách chính 7.699 OK_N + 77 OK_F.
- Dự phòng **300 = 278 OK_N + 22 OK_F**. **C13 đạt, dư 55.**
- Hạn mức: Q1 0, Q2 0, Q3 77, Q4 0.
- Chỉ báo:
  - M1 236/300 = 78,7% (C 105, H 131, K 63, F 1; khoảng 221–274; SHA mẫu `f93d6152…`);
  - M2 264; M3 6,796 (52.845/7.776); M4 0; M5 *bánh* 59.
- SHA:
  - **chính `dfcf4ba63624b0a4cfc92945e22568b0b878e0caf3da4ed83e388fa25a73d4ee`**;
  - **dự phòng `31647c0b3d984bda3d7f430914bea37ae14ed46cac447128006b9e026fc82496`**;
  - `xep-hang.tsv` `c357aa05…`.
- Đủ 14 mục chủ dự án giữ. Không mục khấu trừ nào còn trong hai danh sách. Chính và dự phòng không giao nhau.

Hai báo cáo đã viết lại theo số mới: `bao-cao-suc-chua.md`, `bao-cao-chi-bao.md`. SHA của mọi tệp ở `_done\P6-opus.flag`. Bản 085 chỉ là snapshot trước lượt soát.

Xin bạn tính lại độc lập, đối băm hai danh sách, rà phần thay đổi so với 085, đối chiếu hai báo cáo, rồi ghi `_done\P6-astra.flag`.
