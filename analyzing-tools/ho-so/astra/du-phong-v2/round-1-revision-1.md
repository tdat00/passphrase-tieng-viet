# Dự phòng v2 — nhật ký sửa 1

**SA-Astra, 20/11/2026. Status: Draft (round 1).** Đầu vào: `O\round-1-review-drafts.md`; giữ base `cefb993`. `AT = analyzing-tools`; `U = AT\ho-so\unified`; `O = AT\ho-so\opus\du-phong-v2`; `E = AT\ho-so\astra\du-phong-v2\evidence`.

## Đã áp

| Nhóm | Thay đổi |
|---|---|
| Q-dpv2-2/3 | Nhận chữ ký Opus cho ba D; tám mục sắc thái về A; TT2 rút, S4 giữ nguyên. Ghi T-dpv2-4/5 |
| Q-dpv2-4 | Phương án 2: 46 L3b và chạng vạng không tính HM; giờ cao điểm giữ phản đối H2. Ghi T-dpv2-6 |
| Q-dpv2-5 | Nhận đồng thuận K1 cho toàn khóa baotu. **Astra đồng ký K2 “không tự động chặn” cho tanso/vaynen**; không suy không đỏ từ việc dưới ngưỡng. Ghi T-dpv2-7 và hai dòng chữ ký riêng |
| Q-dpv2-6 | **Nhận phương án 1 cho cả sáu mục**. Tái kiểm 12 phiếu P4 (10 OK, 2 R1), không có phản biện trong bảng đã lưu; quan ngại mới chưa đủ H9. Giữ cờ rà H6 trước khi dùng, không tuyên bố mọi ngữ cảnh đều lành. Ghi T-dpv2-8 |
| TSV dự phòng | Cập nhật 11 dòng cũ và vậy nên; ghi đúng ý kiến mới của Opus, chữ ký/việc thiếu; giữ 37 mục chưa nghĩa |
| TSV HM | Sửa ý kiến Opus ở sáu H6, không chép lý do giữ ngoài của Astra làm ý kiến Opus. Giữ 285 dòng hồ sơ; **237 được tính, 48 không tính**; bao tử LOAI_K1; tần số K2 đủ hai chữ ký |
| Report/plan | Giữ Draft; ghi Opus đã review changes requested; lưu lịch sử trước/sau, N cố định 237, nhánh HM chưa thẩm định bỏ; thêm T-dpv2-4..8 với người quyết định SA-Opus + SA-Astra, ngày 2026-11-20, source commit `pending` |
| Q-dpv2-1 | Tính lại độc lập 632 cặp H5/474 từ chính và 1.177 cặp H7/634 khóa, khớp tập. Thêm phạm vi/chi phí, nhấn mạnh không phải số lỗi/nhóm đỏ đã xác nhận |
| Kiểm/giới hạn | Thêm build --check trên tài liệu đã sửa, CRLF; đối chiếu lỗi build toàn-LF ở nền và bản sửa; giữ hai tài liệu lưu trữ cùng quyết định 10 ngoài phạm vi |
| Để sau | Thêm OI-BANG-PHAT-HANH: đăng ký họ/baotu khi được giao; họ chòng chành/tròng trành cần quyết định riêng vì tác động C5 ở chính |

Các sửa số liệu/khóa/chữ ký được kiểm từ tệp/mã, không chỉ dựa vào lời review. PPM khảo sát H7 ghi mẫu số mục 0; mã H8 dùng tập luật P2. Giữ các evidence cũ như ảnh chụp lịch sử, không đổi tên cột cũ rồi che sự khác biệt.

## Điểm không nhận nguyên trạng và ca mới

- **G5, móng/mông:** đồng ý đây là cách đọc về bộ phận cơ thể thông thường, không tự là nghĩa người lớn.
- **G5, ngoại trừ/ngoại trú:** **chưa nhận “không phải bệnh nên không đỏ”**. H6.5 còn có y khoa chuyên biệt; từ điển có nghĩa điều trị của toàn mục và P7 từng loại nội trú theo H6.5. Đối chứng ngoại trú có 9/325 lượt sạch, PPM khoảng 1,215. Chưa có tỷ lệ nghĩa y khoa riêng, nên không tự kết luận K1; đề nghị **C/CHO_H7**, giữ Opus A và mở **Q-dpv2-7** để Opus phản hồi trước khi gửi supervisor.
- Vì ca mới, mốc đã thống nhất sau 11 sửa cũ là A149/B36/C14/D6, nhưng bản hiện tại ghi **A148/B36/C14/D6 + 1 CHO_HOA**. N HM vẫn 237. Không xóa bất đồng để đạt đúng tổng mà review cũ dự kiến.
- Không gọi 1.177 đối chứng là 1.177 còi đỏ bị bỏ sót hoặc khẳng định nguyên nhân bộ lọc khi chưa truy được mã/ngữ nghĩa. Đã kiểm khớp số lượng và tập, không kiểm xong nghĩa của toàn bộ.
- Không đưa đoạn trả lời các câu đã đóng vào tệp câu hỏi: yêu cầu là **chỉ câu còn mở**. Quyết định nằm trong plan/report. Câu hỏi trước khi rút được lưu trong `revision-1-question-history.json` vì nháp trước chưa commit.

## Bằng chứng mới và kiểm

- `E\revision-1-audit.py`, `revision-1-audit.json`, `revision-1-audit-inputs.json`: số phạm vi, hai bộ mẫu số, hash legacy.
- `E\revision-1-h7-counts.tsv`, `revision-1-h6-six-votes.tsv`: số đo và pointer phiếu gốc.
- `E\revision-1-chu-ky-astra.tsv`: hai chữ ký K2; trỏ chữ ký Opus tại review dòng 95.
- `E\revision-1-h7-ngoaitru.tsv`: nhận định mới, chưa kết luận K1; nguồn từ vựng chỉ lưu URL/revision và loại nghĩa, không lưu định nghĩa.
- `E\revision-1-artifacts.tsv`: danh mục hồ sơ dự kiến đưa Git, không gồm cache/nguồn thô.
- `E\joint-build.py --prove` và `joint-proof.json/log`: mô phỏng trong bộ nhớ, kiểm cả build trên tài liệu đã sửa, số dòng/trạng thái và byte bảo vệ.

**Còn mở:** Q-dpv2-1 (owner, tác vụ hậu kiểm riêng) và Q-dpv2-7 (supervisor SA-Fable nếu chưa hòa H7 sau phản hồi Opus). Không sửa WordListAnalyze.md, README phát hành, hai HTML, nguồn từ, tài liệu lưu trữ hoặc tệp của Opus; không commit/push.

## Ghi nhận Lượt duyệt 2 — 20/11/2026

**accept.** Astra nhận toàn bộ §D của Opus: đóng Q-dpv2-7 bằng T-dpv2-9, ngoại trừ C/CHO_H7, không dùng trước khi đo tỷ lệ nghĩa điều trị ở web và hai SA ký mức K. Không ghi K2 đã ký chỉ vì Opus nghiêng K2.

Đã cập nhật năm bản nháp và bộ dựng: **A148/B36/C15/D6**, không còn CHO_HOA; HM vẫn **237/285 dòng hồ sơ**. Tệp câu hỏi chỉ giữ Q-dpv2-1 (owner); lịch sử Q7 lưu trong `revision-1-question-history.json`. Giữ `Status: Draft (round 1)`, thêm OI-H7-NGOAITRU; chưa mở đo, thay từ hoặc ghi bảng phát hành. Đã khôi phục chi tiết nguồn ở ba D và bỏ tiền tố “Astra:” lặp theo các gợi ý nhỏ.

## Ghi nhận trả lời chủ — 21/11/2026

**accept.** Đã đối chiếu Answer “3” ngày 20/11/2026 tại `1734b43`: việc rà/thay chính được chuyển sang yêu cầu riêng, không làm trong dự phòng v2. Ghi **D-dpv2-5**, cập nhật phạm vi ngoài/việc bàn giao/rủi ro/phases; các nguồn Decisions còn chờ commit đổi sang `1734b43`.

Q-dpv2-1 đã đóng, tệp câu hỏi ghi “Không còn câu hỏi mở”; đầy đủ Q&A còn trong Git tại commit trên. Giữ `Status: Draft (round 1)`, A148/B36/C15/D6 và N=237; không khởi động rà/đo, viết nghĩa hay thay chính.

## Ghi nhận Lượt duyệt 3 — 21/11/2026

**accept.** Đúng là phép rút gọn trước đây làm mất lý do C/D. Đã thêm `ghi_chu` vào hai bảng hồ sơ và quy tắc sao chép nguyên sang bảng công bố; dùng đúng 30 văn bản dự phòng và 8 văn bản HM tại §D của Opus. Bảng cảnh báo §11 có 21 dòng C/D, cột Lý do; thêm T10 kiểm phép chiếu công bố (30/175 và 8/229), không chỉ bảng hồ sơ.

Đã kiểm tổng chứng liệu và các cặp theo S4. Giữ nguyên văn ghi chú, bổ sung chú giải: “chứng liệu yếu” không tự đổi mã H8; “lượt sạch” H5 chỉ hai kho OPUS; “dùng … trước” phản ánh hạng S4 hiện tại, không ban hành TT2. Các nhận định ngôn ngữ vẫn là nhận định đã thống nhất, không là số liệu gõ sai.

Nhận các gợi ý ghi số cuối vào manifest, thêm tiêu đề/pointer Q&A, và yêu cầu công việc riêng phải cập nhật §11–§12/TSV/manifest nếu đổi từ. Chưa đổi quy ước đường dẫn trong TSV. Giữ Draft, A148/B36/C15/D6, N=237 và byte chính; không thực hiện yêu cầu riêng.
