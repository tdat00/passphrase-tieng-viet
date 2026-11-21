# Ký kế hoạch rà và thay danh sách chính — SA-Opus

**accept** — 22/11/2026, SA-Opus.

**Phạm vi chữ ký:**

- `ho-so/unified/ra-thay-chinh-ke-hoach.md` (`Status: Draft (round 1)`);
- báo cáo chung, tệp câu hỏi và ba TSV `ra-thay-chinh-{h7,h5,thay-the}.tsv`.

Các tệp này ở trạng thái của lượt này: gốc `2cc6aec` cộng phần sửa chưa commit.

**Điều kiện duy nhất (OI-RTC-P6, nghiệm thu T7):**

- SA-Astra chạy chương trình chấm độc lập của mình theo T-rtc-14, trên cùng rổ 10.005 mục (`evidence/xep-lai-rtc.log`).
- Kết quả phải giống của Opus:
  - 116 từ vào như `ra-thay-chinh-thay-the.tsv`;
  - dự bị *cả nghĩ*, rồi *cửu chương*;
  - 25 HM cùng thứ tự.
- Nếu khác, chữ ký này mất hiệu lực và hai SA đối chiếu.

**Đã kiểm trước khi ký:**

- Không còn mục nào cần hai SA thỏa thuận hay chủ dự án quyết:
  - S1–S3, mục mở, Q-rtc-O1, Q-rtc-O2, Q-rtc-A2 và chu kỳ HM đều đã khép;
  - căn cứ: D-rtc-5 đến D-rtc-8, T-rtc-1 đến T-rtc-20.
- Gói K2 đủ hai chữ ký: 238 khóa của danh sách chính và từ vào, 5 khóa HM.
- Sức chứa: 116 ghế. Có 118 dự phòng dùng được (còn 2 dự bị), rồi 25 HM để bù.
- Đã cập nhật nghiệm thu (mục 13), giai đoạn và ước lượng (mục 15), mục mở (mục 12) và tham chiếu (mục 16).
- Bộ kiểm định dạng hồ sơ báo 0 lỗi.

**Orchestrator điền khi commit:** nguồn commit của T-rtc-19 và T-rtc-20 (đang ghi "chờ commit").

**Không chặn Final:**

- OI-RTC-K2-KY: ghép chữ ký vào `chu-ky.tsv` ở gói phát hành;
- Q-rtc-A3: chỉ hỏi khi bản Kaikki đã ghim bị mất.
