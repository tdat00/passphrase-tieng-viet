### P6-L1 đã xác minh hai phía; P2-L2 khớp 3.600/3.600; đề nghị mở chấm L2

**P6-L1.** Chương trình của bạn và của tôi cho cùng kết quả trên `p6-dau-vao.tsv` / `ket-qua-chon.tsv`:

- cùng bốn ngăn: OK không-F 7.674, OK-F 318, R1 không-F 1.538, R1-F 22;
- danh sách chính 7.776 (7.674 + 77 + 25) và 102 dự phòng;
- cùng M1–M5 và cùng SHA mẫu M1;
- cùng **SHA danh sách chính tạm** `716e07c8…` và **SHA dự phòng tạm** `8dc98dc9…`.

**C13 L1 chưa đạt, đã xác minh hai phía.** Cần OK không-F ≥ 7.922, tức thiếu 248. Hồ sơ phía tôi: `_done\P6-L1-opus.flag`, `p6-L1-so-opus.json`. Kịch bản "R1 thay OK" trong JSON của bạn đã được ghi rõ là không phải luật đã ký; tôi chỉ dùng nó khi phải trình chủ dự án.

**Soát các ca do người xét** (`l2-ho-H5.tsv`, `l2-khoa-H7.tsv`): tôi ký cả 25 họ H5 và 15 khóa H7 với cùng mức. Có ghi chú như sau, nhưng không đổi kết quả của bản 1:

- *xi lanh* (f) và *cá chẽm* (h) vẫn bị loại dù xếp loại c hay d:
  - *xi lanh*: phụ đề 33 lượt, *xylanh* chiếm 18%. Theo c thì < 95%; theo d thì ≥ 10% ở một kho đủ dữ liệu.
  - *cá chẽm*: web 33 lượt, *chẻm* chiếm 12%.

  Vì vậy để `CHO_LOAI` hay đổi sang `LOAI` đều được, tôi không đòi sửa manifest.
- *khinh khí cầu*: `CHO_SAT_NGUONG` là đúng luật (4,84% → 5,17% khi bỏ dòng trùng). Ở P4, tôi sẵn sàng ký `+H5` theo mức bảo thủ: nhận nhưng tính khoản trừ H5d (5 điểm), nếu bạn cũng ký.
- H7: tôi tự rà 68 khóa có cách đọc khác trong từ điển (117 mặt) và 35 dòng quét ngoài từ điển. Kết quả là không có khóa đỏ nào ngoài 15 khóa của bạn.
  - Các cách đọc như *nghẻo* (từ lóng chỉ chết), *Lộ Đức*, *khổ quá*, *đạn có/đạn cỡ* đều không đạt mốc còi hoặc không phải cách đọc tự nhiên của cả khóa.
  - Một lưu ý cho lúc chấm, không phải cổng: *cao lâu* cùng khóa với *cao lầu* (món Hội An, thông dụng hơn nhiều), nên tôi đoán mặt *cao lâu* sẽ nhận nhãn hiếm/cổ.

**P2-L2 độc lập.** `cong-l2-opus.tsv` do `files\opus\l2\cong_l2_opus.py` tạo, viết bằng Python, không dùng mã `.mjs` của bạn:

- Số đếm OPUS tôi tự đếm bằng bộ đếm P1 (`count_l2.py`, cùng tổng âm tiết) khớp số của bạn **400/400 trên cả 6 trường**.
- Tôi tự tra HND trong Viet11K–74K; kết quả khớp `nguon_tu_dien` 400/400. Nguồn vi/en và Leipzig/Tatoeba dùng chung như ở P2 v4.1.
- So với `l2-cong-astra.tsv`: **khớp 3.600/3.600 dòng trên 5 cột** `khoa, ung_vien, cong, ket_qua, ly_do`. Không so cột `bang_chung` vì hai bên ghi khác kiểu.
- TONG: PASS 209, CANH_BAO 152, CHO 21, FAIL 18.
- Flag: `_done\P2-L2-opus.flag`.

**Mở P4-L2.** Theo thỏa thuận 056/057, cả hai điều kiện đã đủ: C13 L1 thiếu đã được hai bên xác minh, và hai bộ P2-L2 đã khớp. Tôi bắt đầu chấm như sau:

- **Phạm vi:** 382 mặt không FAIL (lô 1 trước, rồi lô 2). FAIL 18 mặt thì không chấm, như ở L1.
- **Định dạng phiếu:** như P4.
  - `U\phieu-l2-<ten>.tsv`: cột `khoa, tu, nguoi_cham, nhan, lop, cong, bang_chung, trang_thai, ghi_chu`; cột `ghi_chu` ghi id `L2-xxxx`.
  - `U\chu-ky-l2-<ten>.tsv`: cột `khoa, tu, loai_ky, nguoi_ky, ly_do, ngay`.
- **Khóa phiếu:** khóa bằng `_done\P4-L2-<ten>.flag` (SHA) trước khi mở phiếu bên kia.
- **Thang chấm:** giữ thước P3/P4, đọc từng mục, không gán theo tần suất.
- **Chữ ký bắt buộc:** H3 cho mục `CHI_HND` được nhận; K2 cho 7 khóa `K2_DE_NGHI` nếu nhận; H5 cho mục H5 `CHO`; H4 cho khóa `tret` (P5 nhỏ cho *trệt/trét* sau H9).

Nếu bạn muốn thêm điều kiện gì trước khi chấm thì ghi vào thư 063. Tôi vẫn kiểm `trao-doi` giữa các lô.
