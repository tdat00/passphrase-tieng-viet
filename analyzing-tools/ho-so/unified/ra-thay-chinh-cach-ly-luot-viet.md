# Rà và thay danh sách chính — nhật ký cách ly các lượt viết sạch (T13)

Người điều phối ghi lại cấu hình của ba lượt viết sạch `rtc-v1`, `rtc-v2`, `rtc-v3` (lô `rtc-lo-01`), theo `huong-dan-giai-nghia.md` mục 12 và kế hoạch mục 7.

- Mỗi lượt là một agent mới, không kế thừa hội thoại (Copilot CLI, agent `general-purpose`, chạy nền): `rtc-v1-writer`, `rtc-v2-writer`, `rtc-v3-writer`.
- Thư mục làm việc nằm ngoài repo, trong thư mục phiên của người điều phối; mỗi thư mục chỉ có ba tệp đầu vào: hướng dẫn (đã bỏ mục 12), `kiem-tra-giai-nghia.py` và lô `lo-01.txt`. Tệp nộp là `lo-01.tsv`.
- Lời nhắc chỉ gồm quy tắc cách ly, đường dẫn thư mục và (với lượt viết lại) đầu mục kèm mã lỗi và chẩn đoán ngắn bằng lời người soát. Không có câu của lượt trước, giải nghĩa cũ, lời từ điển hay chuỗi trùng nguồn.
- Lời nhắc cấm mở, liệt kê hay tìm tệp/thư mục khác, cấm mạng và công cụ tra cứu. Công cụ CLI không chặn cứng quyền đọc tệp, nên cách ly dựa trên lời nhắc và trên việc thư mục chỉ chứa ba tệp; người điều phối không thấy dấu hiệu vi phạm trong các câu trả lời.
- Câu không đạt D6/D7 không lưu trong repo; chỉ lưu băm (log D6) và chẩn đoán của người soát.

## Băm đầu vào của từng lượt

| Lượt | Tệp | Số dòng lô | SHA-256 |
|---|---|---:|---|
| `rtc-v1` | `huong-dan-giai-nghia.md` |  | `6b82e6b8d4b26c5802216200afd2b3713640dd8d477c5c44b1cc05f3a319bd76` |
| `rtc-v1` | `kiem-tra-giai-nghia.py` |  | `3f143e967ce2084cb96f271750c72712015b0fdf3a826826232eadceb9d48581` |
| `rtc-v1` | `lo-01.txt` | 143 | `c47f0fd9d838519fb9beafc3fe26feab51ae90053741692e0c61d12a6a3d1403` |
| `rtc-v2` | `huong-dan-giai-nghia.md` |  | `6b82e6b8d4b26c5802216200afd2b3713640dd8d477c5c44b1cc05f3a319bd76` |
| `rtc-v2` | `kiem-tra-giai-nghia.py` |  | `3f143e967ce2084cb96f271750c72712015b0fdf3a826826232eadceb9d48581` |
| `rtc-v2` | `lo-01.txt` | 48 | `5893959be79445b811bfe0f7cdeca10c66f5d6da0db797e7e3191ca5ad2456ea` |
| `rtc-v3` | `huong-dan-giai-nghia.md` |  | `6b82e6b8d4b26c5802216200afd2b3713640dd8d477c5c44b1cc05f3a319bd76` |
| `rtc-v3` | `kiem-tra-giai-nghia.py` |  | `3f143e967ce2084cb96f271750c72712015b0fdf3a826826232eadceb9d48581` |
| `rtc-v3` | `lo-01.txt` | 10 | `75ab4efeb6e2a3ef48120717463b0aee54b2c80b6f50b5e8f1e5197583e397a6` |

## Chẩn đoán đã gửi cho lượt viết lại

Lời nhắc chung cho cả hai lượt: Mã D6: "câu ở (các) lượt trước quá gần văn bản tham chiếu. Hãy viết với cấu trúc và cách dùng từ khác hẳn cách nói quen thuộc, không theo khuôn từ điển; vẫn đúng nghĩa phổ biến nhất." Các mã khác: "sửa đúng vấn đề được nêu". Danh sách từ và chẩn đoán đúng như trong lời nhắc:

**rtc-v2** (48 từ):

- *áp dụng*: D6
- *ăn tiệm*: D6
- *bày tỏ*: D6
- *bịn rịn*: D6
- *chễm chệ*: HEP — Tư thế này vẫn gặp ở một chỗ ngồi bình thường, không phụ thuộc độ cao hay tính trang trọng.
- *chỗ ngồi*: D6
- *chung tình*: D6
- *cô giáo*: D6
- *côn trùng*: D6
- *cụ thể*: D6
- *cười gượng*: HEP — Một người cũng có thể cố cười vì phép lịch sự, không nhất thiết để giấu cảm xúc.
- *cửu chương*: D6
- *dễ ợt*: HEP — Cách nói nhấn mạnh mức độ dễ chứ không đòi hỏi công sức bỏ ra bằng không.
- *đánh răng*: HEP — Không dùng kem vẫn thực hiện được hành động này.
- *đắc ý*: HEP — Chỉ một kết quả vừa ý cũng đủ, không cần mọi chuyện đều thuận lợi.
- *đầy tháng*: D6
- *đầy tràn*: HEP — Câu buộc phải có thứ chảy ra khỏi vật chứa nên không bao quát cả cách nói về cảm xúc.
- *gặp thời*: RONG — Cơ hội thuận lợi cho một việc cụ thể không có nghĩa là làm bất cứ việc nào cũng dễ.
- *gợi chuyện*: THIEU_NET — Câu mới tả việc bắt chuyện, chưa nêu nét khơi đề tài cho người kia tiếp lời.
- *học tủ*: D6
- *hóng chuyện*: D6
- *khách hàng*: D6
- *lộp bộp*: HEP — Câu giới hạn nguồn âm ở cái vỗ hoặc tiếng nổ, bỏ mất trường hợp các vật rơi chạm bề mặt.
- *lộp độp*: HEP — Vật rắn rơi cũng có thể phát tiếng này, không chỉ có giọt nước.
- *lời lỗ*: VONG — Sau khi nêu chuyện làm ăn, câu vẫn dùng chính hai tiếng của đầu mục để giải thích kết quả.
- *lực lượng*: D6
- *mệt lả*: D6
- *mong nhớ*: HEP — Đối tượng không nhất thiết là một người ở xa; người nói còn có thể mong nhớ quê nhà.
- *mỏng tanh*: HEP — Câu coi khả năng bị rách là nét bắt buộc, không thích hợp với vật liệu cứng.
- *một mình*: D6
- *năm kia*: D6
- *nằm ườn*: D6
- *nặng cân*: D6
- *ngả nghiêng*: HEP — Từ vẫn dùng cho người đang ngồi cười, không nhất thiết người ấy mất thăng bằng.
- *ngắn ngủn*: D6
- *ngân hàng*: D6
- *nhảy sào*: TU_LOAI — Câu gọi tên môn thi thay vì giải thích hành động của người nhảy.
- *nóng ruột*: D6
- *sáng trưng*: HEP — Từ có thể tả riêng một vật rất sáng mà phần còn lại của không gian vẫn tối.
- *số âm*: D6
- *sớm tối*: SAI_NGHIA — Câu đánh đồng hai buổi trong ngày với việc diễn ra liên tục, dù hai cách dùng không luôn tương đương.
- *tạnh ráo*: HEP — Mặt đường còn ướt không có nghĩa là trời chưa tạnh ráo.
- *thay lông*: D6
- *thay thế*: D6
- *tính nết*: D6
- *tương đương*: D6
- *xe điện*: D6
- *xuống cân*: D6

**rtc-v3** (10 từ):

- *ăn tiệm*: HEP — Người được mời dùng bữa ở quán vẫn là ăn tiệm, không nhất thiết phải tự trả tiền.
- *bày tỏ*: D6
- *chễm chệ*: HEP — Câu buộc người ngồi phải giữ lưng thẳng, trong khi dáng ngồi ngả lưng vẫn có thể chễm chệ.
- *chỗ ngồi*: D6
- *khách hàng*: HEP — Câu bỏ sót tổ chức đi mua hàng và người mua dịch vụ của một cá nhân.
- *nằm ườn*: CHU_QUAN — Câu gán tính lười cho người nằm dù họ có thể chỉ đang nghỉ ngơi.
- *ngả nghiêng*: HEP — Câu đòi hỏi chuyển động liên hồi, bỏ sót cách tả những vật đã nghiêng về nhiều phía rồi nằm yên.
- *sớm tối*: HEP — Vế nghĩa thứ hai thu về chuyện có mặt đều đặn, bỏ mất ý suốt ngày, liên tục mà cách dùng này thường mang. / SAI_NGHIA — Vế sau của cờ HAI_NGHIA biến nét thời gian thành sự hiện diện, không giải thích được cách dùng với việc học hành.
- *tạnh ráo*: HEP — Trời vẫn có thể tạnh ráo khi còn nhiều mây, nên không thể bắt buộc bầu trời phải quang.
- *thay thế*: D6
