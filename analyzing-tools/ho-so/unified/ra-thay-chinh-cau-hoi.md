# Rà và thay danh sách chính — câu hỏi còn mở

Tệp này chỉ ghi các câu hỏi còn mở. Mọi đường dẫn tính từ `analyzing-tools/`.

- **Gửi chủ dự án:** Q-rtc-O2 (4 từ còn lệch sau khi hai SA khép mục mở) và Q-rtc-A2 (lấp ghế khi thiếu dự phòng). Hai câu liên quan nhau, nên trả lời cùng lúc.
- **Đã trả lời:** Q-rtc-O1 (D-rtc-6, commit `0253bb0`).
- **Đã khép bằng thỏa thuận:** Q-rtc-S1, S2, S3 (T-rtc-12 đến T-rtc-14; nội dung cũ ở `7fb17fb`).
- **Chưa kích hoạt:** Q-rtc-A3 (mất nguồn D6 đã ghim), điều kiện ở `ho-so/unified/ra-thay-chinh-ke-hoach.md` mục 12.2.
- **Đã rút:** Q-rtc-A1.

## Q-rtc-O2 — 4 từ chính: thay hay giữ

- **Gửi:** chủ dự án (owner).
- **Người nêu:** SA-Opus, SA-Astra.
- **Ngày:** 21/11/2026.
- **Cần quyết định:** với mỗi từ trong 4 từ dưới đây, thay từ (theo Astra) hay giữ từ (theo Opus).

**Bối cảnh.**

- Hai SA đã khép 282 trong 286 dòng mục mở bằng một lượt đối đáp (T-rtc-15 đến T-rtc-18). Chỉ còn 4 từ lệch.
- Như Q-rtc-O1, mỗi từ khi gõ không dấu có thể đọc thành một từ có nghĩa nhạy cảm.
  - Thay: từ rời danh sách, khóa không dấu bị chặn.
  - Giữ: hai SA ký "không tự động chặn". Opus đã ký; Astra chưa ký.
- Nếu chủ dự án chưa quyết, mặc định là không phát hành, tức là thay (`tieu-chi-thong-nhat.md:167, :190–191`).

| # | Từ chính (khóa → cách đọc nhạy cảm) | Astra: thay, vì | Opus: giữ, vì |
|---|---|---|---|
| 1 | *cần cù* (`cancu` → *căn cứ*: căn cứ quân sự; cũng là "cơ sở, chỗ dựa") | nghĩa quân sự còn dùng phổ biến; *căn cứ* gặp nhiều gấp 49 lần *cần cù* | nghĩa chính là "cơ sở"; căn cứ là nơi đóng quân, cùng loại với *tướng, phòng ngự, khiên* chủ dự án đã cho giữ |
| 2 | *tiền lương* (`tienluong` → *tiên lượng*: dự đoán, tiên lượng bệnh) | là đánh giá y khoa | là dự đoán; không phải tên bệnh, triệu chứng hay thủ thuật |
| 3 | *triệu* (`trieu` → *triều*: triều đình, triều đại; cũng là thủy triều) | triều đại thuộc nhóm chính trị, quyền lực | từ hoàng gia, giống *ngai, trẫm* chủ dự án đã cho giữ |
| 4 | *bạn thân* (`banthan` → *bán thân*: tượng bán thân; nghĩa phụ bán dâm) | Astra đọc 38 dòng phụ đề, thấy ít nhất 3 dòng nghĩa mại dâm | nghĩa chính là nửa người; nghĩa mại dâm là nghĩa phụ, ít gặp; *bạn thân* là từ rất thông dụng |

**Phương án và hệ quả** (số sơ bộ; 118 dự phòng dùng được):

1. **Theo Opus cả 4 từ (giữ):** 116 từ thay, còn 2 dự bị.
2. **Theo Astra cả 4 từ (thay):** 120 từ thay, thiếu 2 ghế; phải có Q-rtc-A2.
3. **Chọn từng từ:** chọn thay k từ thì có 116 + k từ thay; còn 2 − k dự bị (thiếu khi k ≥ 3).

**Đề nghị:** hai SA không có đề nghị chung. Mỗi bên giữ lập trường ở bảng trên.

**Chứng cứ:**

- `ho-so/astra/ra-thay-chinh/khep-muc-mo-1.tsv`, `khep-muc-mo-1.md` (phiếu Astra; *bạn thân*: `ho-so/astra/ra-thay-chinh/evidence/km1-ban-than-id.tsv`);
- `ho-so/opus/ra-thay-chinh/khep-muc-mo-1-opus.tsv`, `khep-muc-mo-1-opus.md` (phiếu Opus);
- `ho-so/unified/ra-thay-chinh-h7.tsv` (trạng thái TRANH_CHAP).

**Bị chặn:** tập ra cuối, gói chữ ký K2, sức chứa.

**Answer (owner, ):**

## Q-rtc-A2 — lấp ghế khi thiếu dự phòng

- **Gửi:** chủ dự án (owner).
- **Người nêu:** SA-Astra, SA-Opus.
- **Ngày:** 21/11/2026.
- **Cần quyết định:** có cho một nguồn từ vào ngoài 118 dự phòng hiện có hay không, và nguồn nào.

**Vì sao hỏi bây giờ** (điều kiện ở kế hoạch mục 12.2):

- Nếu Q-rtc-O2 theo Astra từ 3 từ trở lên thì thiếu ghế ngay trước Final.
- Nếu theo Opus thì còn 2 dự bị. Lượt viết nghĩa mới (D6/D7) thường làm trượt một số từ vào, nên 2 dự bị gần như chắc không đủ. Hỏi bây giờ để không phải dừng lần nữa sau khi chủ dự án duyệt.
- Tính lại thứ tự theo T-rtc-14 chỉ đổi thứ tự trong cùng hàng đợi, không thêm nguồn.
- Dự phòng tầng C đã được tính trong 118. Tầng D trượt luật cứng nên không phải phương án. Khép cổng H5 của *loằng ngoằng* có thể thêm 1 nguồn; đó là việc của hai SA, không cần chủ dự án.

**Phương án và hệ quả:**

1. **Mở một chu kỳ có giới hạn cho từ có thể cân nhắc (HM) nhãn OK:** tối đa 25 từ, theo hạng; kiểm lại H1–H9, viết nghĩa sạch mới, D6/D7/D8 mới, không dùng lại câu cũ. Thêm khoảng 1–3 lượt viết và 2–4 lượt SA. Có đệm cho D6/D7; nhiều HM từng trượt D6 ở P7 nên không bảo đảm đủ.
2. **Nới trần lớp F (77) cho đúng số ghế thiếu**, lấy dự phòng lớp F tầng A. Không tốn chu kỳ HM, nhưng đổi một hạn mức đã ký (Q3) và làm danh sách có thêm hư từ.
3. **Không lấp:** nếu thiếu thì giữ lại đúng số từ cần thay có rủi ro thấp nhất. Trái luật đã ký (TC:167, :190–191), nên hai SA không đề nghị.
4. **Dừng ở phân tích, chưa thay danh sách chính.**

**Đề nghị (hai SA, kế hoạch mục 12.2):** phương án 1.

**Chứng cứ:** `ho-so/opus/ra-thay-chinh/evidence/de-xuat-thay-v2.log` (116 vào, 2 dự bị; nhánh theo Astra thiếu 2); `ho-so/astra/ra-thay-chinh/khep-muc-mo-1.md` (mục "Ảnh hưởng"); `honorable-mentions.tsv`.

**Bị chặn:** sức chứa, lượt viết nghĩa, kế hoạch Final.

**Answer (owner, ):**
