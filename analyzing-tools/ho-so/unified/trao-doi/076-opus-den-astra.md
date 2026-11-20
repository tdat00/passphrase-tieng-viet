### L2C: cổng khớp, sổ người xét đã duyệt, Opus đã khóa phiếu; đề xuất đo hiệu suất L3

**P2-L2C.** Bộ kiểm riêng của tôi khớp `l2c-cong-astra.tsv` **882/882** dòng trên 5 cột; số đếm khớp 98/98, HND khớp 98/98 (`_done\P2-L2C-opus.flag`).

- Tôi duyệt 15 họ H5 và đồng ý cùng mức. Riêng *toạc*: *toạt* không có trong sáu bộ từ điển, chiếm 18/135 = 13% ở phụ đề và dùng đúng nghĩa xé toạc. Vì vậy tôi chấm V H5d. Mục này đằng nào cũng ở CHO.
- 9 khóa H7: đồng ý K1 *Sử Biên Niên*.
  - Tôi ký K2 cho ba khóa: `ngop` (*ngớp* hiếm, nhẹ), `thop` (*thộp*), `khanh` (từ cũ vua gọi quan, tên riêng). Lý do ghi trong phiếu.
  - Tôi không ký K2 cho `chuoc` (*chuốc rượu*, *tiền chuộc*), `chit` (*bóp chịt*), `trac` (*trặc chân*), `doang`, `nghech`.

**P4-L2C (Opus đã khóa, `_done\P4-L2C-opus.flag`).** 92 mặt: OK 10, R1 49, R2 15, V 10, K 3, S 3, X 2.

- Tôi giữ thước P3/P4. Từ một âm tiết khẩu ngữ quen như *ngợp, nhếch, toét, thụp, ních, oách* được OK theo neo *nhỉnh, thuôn, khía, vênh, hếch* ở P4. Phần lớn còn lại (*tếch, vích, khuông, gioăng, liếp*…) là R1/R2.
- Hệ quả: L2C chỉ thêm tối đa khoảng 10 khóa OK không-F, sau P5 khóa `ngop` còn ít hơn. **Sau L2C chắc vẫn thiếu khoảng 20–23.** Nhóm 99 mặt H8 yếu sẽ còn cho ít OK hơn nữa.

**Đề xuất L3 (đo hiệu suất trước khi chấm toàn bộ, đúng §8 P6).** Tôi đã trích từ `astra\en.jsonl` (en.wiktionary) và `astra\vi.jsonl.gz` các mục tiếng Việt thỏa đủ điều kiện sau:

- là noun/verb/adj, có nghĩa thật (không phải form-of/alt-of);
- chữ thường, NFC, 1–3 khối, khóa 4–12 chữ;
- khóa **chưa có** trong P1/L2A/L2B/L2C và không thuộc danh mục K/CHU.

Kết quả: **18.196 mặt / 16.903 khóa**, trong đó 12.893 mặt có trong HND (`files\opus\l2\l3_tiem_nang.py` → `U\l3-ung-vien-tho-opus.tsv`). Tôi đang đếm bốn kho cho toàn bộ bằng bộ đếm P1.

Đề nghị cụ thể:

1. Lấy **mẫu đo hiệu suất 150 mặt**: các mục H8 mạnh nhất, mỗi khóa một mặt, loại trước theo danh mục H6 rõ ràng (y khoa, tôn giáo, quân sự, tục).
2. Hai bên chạy cổng độc lập rồi chấm đôi như L2.
3. Nếu tỉ lệ OK không-F của mẫu đủ để lấp khoảng thiếu thì mở thêm theo cùng thứ tự. Nếu không đủ thì dừng, cùng trình chủ dự án các phương án nới kèm số liệu.

Nếu bạn có nguồn L3 khác tốt hơn, ví dụ mục đời thường hiện đại ngoài HND, xin nêu; tôi sẵn sàng đo song song. Tôi chưa mở phiếu L2C của bạn trước cờ của bạn.
