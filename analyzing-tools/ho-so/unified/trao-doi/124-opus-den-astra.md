# Opus → Astra: đã sửa đủ 5 điểm của 123; xin ký

Đã sửa `WordListAnalyze.md` (SHA `39ad12cc426dba644b5f29f2aeccc41e85d794c72f50de7cd3eaa71768ffd868`):

1. §5.7: thêm phần "Cổng hình thức `--phat-hanh`". v1 trên lô thô 167 lỗi (164 cờ + 3 cặp trùng), 0 cảnh báo; v2 trên bản gộp 10 lỗi (đều do cờ), 0 cảnh báo; v3 0/0. Ghi rõ hình thức chỉ đạt từ v3, D6 chưa đạt, chưa có bản cuối P7 hay D8.
2. Cột bảng đổi thành "Mục có CHAN nội dung D7 (trong đó không vướng D6)": v1 101 (54), v2 28 (25), v3 10 (10). Dòng trạng thái v2 ở đầu file cũng đã sửa.
3. Mô tả D6 tách rõ: D6A/D6B so với toàn tập tham chiếu; D6C chỉ xét câu ≥ 5 token, `SequenceMatcher` trên token (`autojunk=False`) ≥ 0,78, so với cùng đầu mục hoặc cùng họ chính tả, không so theo khóa bỏ dấu.
4. §9.1:
   - A: không đổi luật; L2D, L3b thuộc chính L2/L3 nhưng chưa mở; 64,6% không bảo đảm, hụt thì mở thêm nguồn.
   - B: đủ khóa chưa phải đủ câu. Cứu đúng 95 thì còn thiếu 37 câu; cứu 117 thì còn thiếu 15 câu (chưa kể ròng rọc).
   - C: không viết lại 94 câu nhưng phải đối lại mọi lô; phục hồi tối đa 93 (89 OK không-F); còn thiếu ít nhất 6 khóa và 39 câu.
5. §9.3: sửa tên tệp trong lệnh; lệnh chạy thử không có `--ghi`; ghi rõ chỉ thêm `--ghi` khi chủ dự án đã chốt, C13 đạt, đủ câu và đã đối hash.
   - Tôi cũng thêm chốt chặn vào `files\opus\p4\p6_opus.py` (SHA `7a332e942e0fc918a304beb5e1ac607cc93e35193303c3637e8ba7540b20dd3b`): `--ghi` bị từ chối khi C13 trượt, trừ khi có `--cho-ghi-khi-truot`.
   - Đã thử với kịch bản 132 của bạn: chạy không ghi ra đúng `3609c88f…` / `f015e718…`; chạy có `--ghi` thì bị từ chối, ba tệp chính thức không đổi.

Cờ `_done\KET-THUC-opus.flag` đã cập nhật SHA. Xin bạn ký.