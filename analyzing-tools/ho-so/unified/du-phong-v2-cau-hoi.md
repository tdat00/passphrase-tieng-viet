# Dự phòng v2 — câu hỏi còn mở, bản sửa 1

**Ngày:** 20/11/2026. **Status: Draft (round 1).** Chỉ giữ câu đang mở cho chủ. Quyết định đã chốt nằm ở Decisions của kế hoạch; mã cũ không dùng lại. Không còn câu hỏi supervisor.

`AT = analyzing-tools`; `U = AT\ho-so\unified`; `O = AT\ho-so\opus\du-phong-v2`; `OE = O\evidence`; `A = AT\ho-so\astra\du-phong-v2`; `E = A\evidence`. Dữ liệu/mã cũ thuộc base `cefb993`; các hồ sơ du-phong-v2 chưa commit có hash trong evidence.

## Q-dpv2-1 — Có mở hậu kiểm riêng cho phát hiện ở danh sách chính?

**Addressee:** owner.
**Raised by:** SA-Opus; SA-Astra đồng ý lưu câu hỏi về công việc tương lai, không chặn phần phân loại hiện tại.
**Date:** 2026-11-20.
**Decision needed:** Chủ chọn chỉ ghi nhận, giao hậu kiểm giới hạn, hay mở một yêu cầu riêng cho rà/thay danh sách chính.

**Context:** danh sách chính và §10 phải giữ nguyên trong đợt này. Hai SA đồng ý họ chòng chành/tròng trành; số sạch 3/6 và 2/1 khiến cả họ không đạt H5c. Chòng chành ở chính, tròng trành ở dự phòng. Hai SA loại hì hụi theo họ hè hụi; không ai kết luận hì hục sai H5.

**Phạm vi và chi phí cần biết:**

- **H5, verified:** bảng sinh thô có **632 cặp có hướng trên 474 từ chính**. Đếm lại khớp; đó không phải 632 họ chính tả đã được xác nhận. Nhiều cặp có thể khác nghĩa hoặc cùng một vấn đề nhìn hai hướng; cần sàng lọc/đọc từng ca.
- **H7, verified:** bảng còi hiện có 227 dòng/117 khóa. Từ dữ liệu DOC_KHAC có **1.177 cặp trên 634 khóa chính**, PPM gộp ≥0,3 và chưa có dòng tương ứng trong bảng còi. Tính lại độc lập cho cùng tập 1.177 ở cả hai bộ mẫu số đang lưu; không có cặp tự so chính nó.
- **Không suy quá số liệu:** chưa xác nhận các 1.177 đối chứng là nhóm đỏ. Đây là quy mô sàng lọc, không phải 1.177 lỗi/còi bắt buộc bị bỏ sót. Báo tử là một ca bỏ sót đã xác nhận; nguyên nhân đầy đủ của lỗ hổng bảng còi cần rà nguồn/mã, không chỉ suy từ việc thiếu dòng.
- **Tác động:** người nhớ dạng tròng trành có thể nhập khóa khác chòng chành. Muốn thay chính vẫn phải có quyết định riêng, đúng ngăn P6 và câu đạt D6/D7/D8.
- **Chi phí, assumed:** chỉ rà một họ đã có nguồn là công việc giới hạn; mở rộng hai bảng là tới 1.809 bản ghi đầu vào cần phân loại, có thể cần đọc ngữ cảnh/đo thêm. Chưa có cơ sở quy thành số giờ, token hay credits. Đề nghị báo khối lượng thực tế sau bước giới hạn, rồi mới xin mở rộng; không tự chạy toàn bộ.

**Evidence:**

- `AT\tieu-chi-thong-nhat.md:103–135`, `:156–168`; `U\opus-counts.tsv:1961`, `:12029`, `:13474`.
- `OE\bien-the-chinh-tho.tsv`; `OE\pham-vi-hau-kiem-h7.tsv`; `OE\pham-vi-hau-kiem.py`.
- `U\canh-bao-khong-dau.tsv`; `U\cong-opus-v4.tsv:4156` và bản Astra cùng dòng cho bao tử H7 PASS lịch sử.
- `E\revision-1-audit.json`, `E\revision-1-audit.py`: số đếm và đối chiếu độc lập, không chỉ chép log Opus.
- `O\round-1-review-drafts.md` §3.1, §3.6, mục thay đổi 8; `A\round-1-revision-1.md`.

**Options:**

1. **Chỉ ghi nhận:** không mở thêm công việc/chi phí; chính vẫn nguyên trạng cùng rủi ro đã nêu; chưa biết bảng còi còn những ca nào.
2. **Hậu kiểm có chốt phạm vi:** bước đầu chỉ đánh giá họ chòng chành/tròng trành, báo bằng chứng và phương án; 632 cặp H5 và 1.177 cặp H7 chỉ mở khi chủ giao tiếp. Không tự thay chính.
3. **Yêu cầu rà/thay chính riêng:** chủ xác nhận phạm vi mới và yêu cầu P6/P7/phát hành; không thực hiện trong kế hoạch dự phòng v2 chỉ phân tích.

**The SAs' recommendation:** Opus chọn 2. Astra vẫn ưu tiên không mở thêm trong đợt này, nhận 2 nếu chủ giao như tác vụ riêng có chốt phạm vi/chi phí. Cả hai không thay chính ngay.

**Blocked:** chỉ việc mở rộng hậu kiểm hoặc thay danh sách chính; phần ghi nhận/phân loại tiếp tục được với byte chính giữ nguyên.

**Answer (owner, 2026-11-20):** 3 — mở yêu cầu riêng để rà/thay danh sách chính, ngoài đợt dự phòng v2 (trả lời qua form `ask_user` lúc 22:40 +07:00).
