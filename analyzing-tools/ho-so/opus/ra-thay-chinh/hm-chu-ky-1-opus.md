# Chu kỳ HM có giới hạn — phiếu duyệt của SA-Opus

Ngày duyệt: 22/11/2026. Duyệt `ho-so/astra/ra-thay-chinh/hm-chu-ky-1.{tsv,md}` theo D-rtc-8; đây là lượt đối đáp duy nhất theo D-rtc-5.

**Kết luận:**

- Đồng ý cả 25 HM và hai mục không chọn; ký K2 cho 5 mục.
- Không có điểm lệch, không có câu hỏi cho chủ dự án.
- Phiếu từng mục: `hm-chu-ky-1-opus.tsv` (27 dòng: 25 HM và 2 mục không chọn).

## 1. Kiểm bằng dữ liệu (verified)

- **Hạng:** xếp 130 HM nhãn OK theo `ho-so/unified/xep-hang.tsv`.
  - 27 mục đầu, tới *tương đương* (hạng 1.541), gồm 25 mục đề xuất, *cơ quan* (hạng 120) và *mình* (hạng 1.442, lớp F). Thứ tự khớp.
  - 5 HM nhãn OK lớp F: *mình, làm sao, thường xuyên, cô ta, mặt khác*.
- **Khóa:** không trùng với:
  - 7.776 từ chính sau thay;
  - 89 dự phòng còn lại;
  - 110 khóa chặn cũ;
  - 94 khóa chặn mới (92 khóa của từ ra vì H7, `baotu`, `lamco`).

  25 khóa khác nhau, đều từ 4 chữ cái trở lên.
- **Nhãn:** OK, không lớp F, khớp `honorable-mentions.tsv`. Không mục nào có trong `spelling_families.tsv` hay `ra-thay-chinh-h5.tsv`.
- **Cách đọc cùng khóa:** lấy từ ba nguồn. Chỉ lưu đầu mục và số đếm (`evidence/hm-chu-ky-1-opus-kiem.tsv`).
  - HND: bản tạm ngoài repo, đã xóa sau khi chạy;
  - Kaikki: bản đã ghim, SHA-256 `1f0abd…`;
  - `opus-counts.tsv`.
- **Tính lại S4 theo T-rtc-14** (`evidence/xep-lai-rtc.*`): cùng 25 mục, cùng thứ tự; mục 26 là *giảng viên*.

## 2. Ý kiến

- **20 mục không có cách đọc đỏ:** đồng ý với Astra.
  - H5 *chỗ ngồi* (loại d): dạng lỗi 3,5% ở phụ đề, 0,3% ở web.
  - H5 *tàu điện* (loại c): dạng chính chiếm 98,1% ở phụ đề, 99,6% ở web.
  - H5 *bày tỏ*: dạng khác 0,9% ở phụ đề, 0,2% ở web.

  Cả ba đều đạt luật (TC:124–125).
- **5 K2, ký "không tự động chặn":**
  - *biển* ↔ *biến*;
  - *bí mật* ↔ *bỉ mặt*;
  - *vận hành* ↔ *vạn hạnh*;
  - *chia* ↔ *chĩa, chỉa, chía, chị ả*;
  - *ngắn gọn* ↔ *ngả ngớn, ngả ngốn*.

  Lý do từng mục ở phiếu TSV. Hai mục cần nói thêm:
  - *ngả ngớn*: Kaikki ghi nghĩa "không đứng đắn", không có nghĩa tục hay tình dục người lớn, nên không phải K0 (TC:161). Số lượt sạch: 0/0.
  - *chia*: hai chữ ký cũ ở `ho-so/unified/chu-ky.tsv` (19/11/2026) vẫn hiệu lực cho *chĩa*. Tôi ký thêm phạm vi *chỉa, chía, chị ả*.
- **Không chọn *cơ quan*: đồng ý.**
  - T-dpv2-8 chỉ giữ mục này kèm cờ rà H6.
  - Astra phản đối theo nhóm 3, có căn cứ. Phản đối còn giữ thì không phát hành (TC:190–191).
  - Bỏ mục này không làm thiếu ghế.
- **Không chọn *mình*:** lớp F, F đã đủ 77.

## 3. Tệp

- `hm-chu-ky-1-opus.tsv`;
- `evidence/hm-chu-ky-1-opus.py`, `hm-chu-ky-1-opus.log`, `hm-chu-ky-1-opus-kiem.tsv`;
- `evidence/hm-chu-ky-1-phieu.py`;
- `evidence/xep-lai-rtc.py`, `xep-lai-rtc.tsv`, `xep-lai-rtc.log`.
