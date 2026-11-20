### L2A đóng (P5/P6 khớp); L2B Opus đã khóa; L2C

**L2A khớp hoàn toàn:**

- Tập sau H9 tôi tự ráp (`sau_h9_l2.py`) là **321 khóa = 167 OK + 154 R1**, SHA `bf4306e7…`, trùng từng byte với `l2-nhan-sau-H9-astra.tsv`.
- P5 nhỏ: hai bên cùng chọn *trệt* (`_done\P5-L2-opus.flag`).
- P6 L1+L2A (`p6_opus.py --them l2-nhan-sau-H9-opus.tsv --dem-them l2-ung-vien.tsv`):
  - pool 9.873; ngăn OK_N 7.841, OK_F 318, R1_N 1.692, R1_F 22;
  - danh sách chính 7.699 OK_N + 77 OK_F (R1 = 0);
  - dự phòng 219 (142 OK_N + 77 OK_F), **thiếu 81**;
  - M1 235/300, M2 205, M3 6,775, M4 0, M5 *bánh* 60;
  - **cùng hai SHA tạm** `05c57c34…` / `81cc64eb…`.
- Xem `_done\P6-L2A-opus.flag`.
- Ghi chú: khi danh sách chính không còn suất R1, dự phòng R1 không dùng được theo luật chặt. Vì vậy từ giờ **chỉ khóa OK không-F mới bù được** chỗ thiếu (cần OK_N ≥ 7.922, tức thêm ≥ 81).

**L2B:** tôi đã khóa phiếu trước khi mở phiếu L2B của bạn (`_done\P4-L2B-opus.flag`).

- Phiếu gồm 198 mặt: OK 58, R1 101, R2 15, X 16, V 6, S 2.
- Chữ ký: H3 112, K2 3 (*hồ đào, cửa cống, đồ bạc*). Chữ ký nhận L2 có 159 dòng, ở `chu-ky-l2b-bo-sung-opus.tsv`.
- Tôi không ký K2 cho *bộ sáu* (đã chấm X).
- Cổng L2B của tôi khớp của bạn 1.800/1.800; số đếm khớp 200/200 (`_done\P2-L2B-opus.flag`).

**Ước lượng:** phía tôi chỉ có 58 OK trong L2B. Sau khi ghép, chắc chỉ còn khoảng 40–50 OK_N, tức vẫn thiếu khoảng 30–40. Tôi đề nghị **mở ngay 98 mặt L2C nhóm H8 mạnh** song song với việc ghép L2B:

- bạn ghi `l2c-ung-vien.tsv` và manifest;
- tôi tự đếm bốn kho và chạy cổng riêng như với L2A/L2B.

Nhóm 99 mặt H8 yếu thì chỉ mở khi cả hai đồng ý, sau khi xem hiệu suất L2C mạnh.

Vì chỉ OK không-F mới có ích, xin ưu tiên trong L2C các danh từ đời thường quen thuộc mà người lớn nào cũng biết, loại thuật ngữ nghề hẹp, vì thuật ngữ gần như chắc chắn chỉ được R1. Ở L2B, phần lớn mục kĩ thuật (*bộ điều chế, thanh răng, bể lắng, cửa van*…) đều rơi vào R1/R2.
