# Phân tích danh sách từ: phương án ban đầu của Opus (WordListAnalyze-Opus)

> **Trạng thái ngày 20/11/2026:** Đây là phân tích độc lập ban đầu của Opus, **đã được thay** bằng danh sách thống nhất do Opus và Astra cùng xây ([WordListAnalyze.md](WordListAnalyze.md)). Hai trang [`index.html`](index.html) và [`thong-tin.html`](thong-tin.html) dùng danh sách thống nhất (trang thông tin kèm giải nghĩa viết mới); danh sách và giải nghĩa ở mục 10 chỉ còn là bản lưu trữ. Đối chiếu với bản phát hành ở mục [Kết quả cuối cùng](#kết-quả-cuối-cùng).

Tài liệu này ghi lại cách Opus chọn **7.776 từ** cho [Passphrase tiếng Việt](README.md) ở vòng độc lập: phương pháp, cách đánh giá, số liệu từng bước và các sự cố phát sinh. Danh sách được xây dựng ngày 18–19/11/2026 và nằm trong khối `#wordlist` của hai trang HTML cho tới khi danh sách thống nhất thay vào ngày 20/11/2026; bản lưu nguyên văn ở [mục 10](#10-danh-sách-7776-từ).

Mục 1–8 là hồ sơ của phương án ban đầu; chỉ các câu đã lỗi thời được sửa. Các lỗi Astra chỉ ra và Opus xác nhận bằng dữ liệu ghi ở [mục 9](#9-kết-quả-review-chéo). Hai phương án đã được hợp nhất theo một bộ tiêu chí chung: xem [phân tích thống nhất](WordListAnalyze.md), [bộ tiêu chí đã ký](analyzing-tools/tieu-chi-thong-nhat.md) và [phương án của Astra](WordListAnalyze-Astra.md).

## 1. Kết quả

Số liệu ở mục 1–8 là của danh sách Opus ban đầu (mục 10), không phải của bản phát hành.

| Chỉ số | Giá trị |
|---|---|
| Số từ | 7.776 (= 6⁵), không trùng nhau kể cả sau khi bỏ dấu và viết liền |
| Entropy | 12,92 bit/từ; 6 từ ≈ 77,5 bit (bằng danh sách EFF mà Bitwarden dùng) |
| Từ đơn / từ ghép 2 âm tiết | 490 / 7.286 |
| Độ dài khi viết liền | 4–12 chữ cái, trung bình 6,70; không cần dùng tới từ 3 kí tự |
| Giải nghĩa | 7.776/7.776 từ, trung bình 52 kí tự, tự viết (không chép từ điển) |
| Nằm trong bộ 11K / chỉ 22K / chỉ 74K của Hồ Ngọc Đức | 3.071 / 1.861 / 2.844 |
| Tần suất (trung bình 2 kho văn bản, lần/triệu âm tiết) | trung vị 3,62; 10% thấp nhất ≤ 0,26 |

Phân bố độ dài (chữ cái, không tính dấu cách):

| 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|
| 548 | 1.032 | 1.919 | 2.118 | 1.343 | 586 | 177 | 47 | 6 |

Thành phần theo mức đánh giá (xem mục 4.5–4.7):

| Nhóm | Số từ | Ví dụ |
|---|---|---|
| 40 từ mẫu đã được duyệt | 40 | bướm, chảo, diều, cà phê, bánh chưng |
| Điểm 3: rất thông dụng, dễ hình dung | 1.091 | trứng, em bé, hải sản, lễ hội, ruồi |
| Điểm 2: thông dụng | 6.060 | tuần, thanh toán, phong cảnh, kiên nhẫn |
| Điểm 3 hoặc 2, chỉ dễ nhầm hỏi/ngã hoặc có biến thể cũ ít dùng | 290 | sữa tươi, dễ thương, mạnh mẽ, nghỉ ngơi |
| Điểm 1: ít dùng hơn, thiên về văn viết, lấy những từ tần suất cao nhất | 295 | hạ tầng, hiệp hội, điều khoản, thường dân |

## 2. Yêu cầu

Tiêu chí do chủ dự án đặt ra:

1. Từ thông dụng với mọi người, dựa theo từ điển tiếng Việt.
2. Không dùng tên riêng, từ mang nghĩa bạo lực, phản cảm, chỉ bệnh tật… (mở rộng thành mọi chủ đề nhạy cảm).
3. Các từ trùng nhau khi bỏ dấu (*diều/điều*) chỉ lấy một từ.
4. Dài tối thiểu 4 kí tự; chỉ bổ sung từ 3 kí tự nếu không đủ 7.776 từ.
5. Trang [`thong-tin.html`](thong-tin.html) phải có giải nghĩa của từng từ.

Ngoài ra áp dụng các lưu ý ở [README mục 4](README.md#4-lưu-ý-riêng-cho-tiếng-việt): bỏ từ có hai kiểu đặt dấu (*hòa/hoà*), biến thể chính tả (*lý/lí*, *giày/giầy*), ưu tiên từ ít bị viết sai, không chứa `-`.

Các quyết định phát sinh trong quá trình làm (đều được chủ dự án duyệt):

- Duyệt trước 40 từ mẫu (10 từ đơn, 30 từ ghép) rồi mới làm tiếp. 40 từ này được giữ nguyên trong danh sách ở mục 10. Bản phát hành giữ 37 từ; *bướm, cà phê, thước* bị loại theo bộ tiêu chí chung (xem [Kết quả cuối cùng](#kết-quả-cuối-cùng)).
- Khi trùng không dấu, ưu tiên từ cụ thể, dễ hình dung: *bướm* thay vì *buồm*, *diều* thay vì *điều*, *chảo* thay vì *chào*. Về sau chủ dự án quyết bỏ *bướm* và để trống khóa `buom` (xem 9.2).
- Từ ghép lưu có dấu cách (*cà phê*) để trang thông tin dễ đọc. Khi tạo passphrase, app viết liền (*càphê*), hoặc nối bằng dấu phân cách nếu bật "Phân cách từ ghép" (*cà_phê*). Viết hoa và chèn số áp dụng cho cả từ ghép (*Cà_phê7*).

## 3. Nguồn dữ liệu

| Nguồn | Dùng để | Ghi chú |
|---|---|---|
| Danh sách từ của Hồ Ngọc Đức (Free Vietnamese Dictionary Project): Viet11K, Viet22K, Viet74K, qua [duyet/vietnamese-wordlist](https://github.com/duyet/vietnamese-wordlist) | Tập ứng viên: chỉ chọn từ có trong từ điển | GPL. Chỉ dùng để kiểm tra từ có trong từ điển, không lấy giải nghĩa. |
| [OPUS](https://opus.nlpl.eu/) OpenSubtitles v2018, bản tiếng Việt đơn ngữ | Đo độ phổ biến trong lời nói (phụ đề phim) | 5.126.239 câu, 34,3 triệu âm tiết. Chỉ dùng để đếm. |
| OPUS CCAligned v1, bản tiếng Việt đơn ngữ | Đo độ phổ biến trong văn bản web tiếng Việt | 14,9 triệu dòng (10,9 triệu dòng khác nhau), 150 triệu âm tiết. Chỉ dùng để đếm. |

Không có văn bản nào từ các kho trên được đưa vào repo; chỉ dùng số lần xuất hiện để xếp hạng.

## 4. Phương pháp

### 4.1. Từ đơn không đủ, phải dùng từ ghép

Sau khi bỏ dấu và gộp trùng, bộ 22K chỉ còn 1.305 từ đơn khác nhau (718 từ dài ≥4 kí tự, 479 từ 3 kí tự). Cả bộ 74K cũng chỉ có 2.453, phần lớn là âm tiết hiếm. Vì vậy dù bổ sung từ 3 kí tự cũng không thể đủ 7.776 từ đơn, nên danh sách phải gồm thêm từ ghép 2 âm tiết. Từ ghép luôn dài ≥4 kí tự, nên cuối cùng không cần dùng tới từ 3 kí tự.

### 4.2. Tạo ứng viên và lọc tự động

Từ bộ 74K, giữ các mục:

- viết thường (bỏ phần lớn tên riêng), không chứa `-`, gồm 1–2 âm tiết, chỉ có chữ cái tiếng Việt;
- dài ≥4 chữ cái khi viết liền;
- không có âm tiết thuộc các trường hợp hai cách viết: vần `oa`, `oe`, `uy` không có phụ âm cuối mà mang dấu thanh (*hòa/hoà*, *khỏe/khoẻ*, *thủy/thuỷ*); `i/y` sau `h, k, l, m, qu, s, t, v, d, n` (*lý/lí*, *kỹ/kĩ*, *mì/mỳ*); *giày/giầy*, *dày/dầy*.

Kết quả là **45.605 ứng viên** (3.516 từ đơn). Gom các ứng viên có cùng dạng không dấu viết liền thành **37.807 nhóm**; mỗi nhóm chỉ được chọn tối đa một từ, nên danh sách cuối chắc chắn không trùng khi bỏ dấu. Ví dụ, nhóm `chao` gồm *chao, chào, cháo, chão, chạo, chảo*. Nhóm của 40 từ mẫu được cố định, không đánh giá lại.

### 4.3. Đo độ phổ biến

- Từ đơn: số lần xuất hiện của âm tiết. Từ ghép: số lần hai âm tiết đứng liền nhau đúng thứ tự.
- Chuẩn hoá NFC, chữ thường, tính theo lần/triệu âm tiết trong mỗi kho.
- Với CCAligned, mỗi dòng giống hệt nhau chỉ đếm một lần, để bớt ảnh hưởng của nội dung lặp lại trên web (menu, chân trang).
- Điểm phổ biến của một từ là trung bình cộng tần suất ở hai kho. Một nhóm được xếp hạng theo từ có điểm cao nhất trong nhóm.

### 4.4. Chọn tập để đánh giá

- Vòng chính: 14.000 nhóm phổ biến nhất, cộng 2.136 nhóm khác có từ thuộc bộ 11K (để không bỏ sót từ quen thuộc nhưng ít xuất hiện trong kho văn bản), tổng **16.136 nhóm**.
- Vòng mở rộng: thêm **6.000 nhóm** kế tiếp theo tần suất (xem sự cố 6.6).
- Tổng cộng **22.136 nhóm** được đánh giá.

### 4.5. Đánh giá bằng mô hình ngôn ngữ

Các nhóm được chia thành 45 lô khoảng 500 nhóm, giao cho các tác tử LLM chạy song song (GitHub Copilot CLI). Lô được chia xoay vòng theo hạng tần suất, nên lô nào cũng có đủ nhóm phổ biến và ít phổ biến; nhờ vậy cách chấm của các tác tử dễ đồng đều hơn. Mọi tác tử dùng chung một bản hướng dẫn:

- Mỗi nhóm chọn tối đa một từ. Trong các từ thông dụng như nhau, ưu tiên từ cụ thể, dễ hình dung (đồ vật, con vật, cây cối, món ăn, nơi chốn, thiên nhiên > hành động, tính chất > từ trừu tượng, hư từ).
- Chấm **điểm** theo độ phù hợp làm từ cho passphrase (quen thuộc là chính, sau đó đến dễ hình dung):
  - `3`: rất thông dụng, ai cũng biết và dễ hình dung (*bướm, xe đạp, ấm áp*);
  - `2`: rất thông dụng nhưng trừu tượng (*tuy nhiên, kinh nghiệm*), hoặc thông dụng nhưng ít dùng hơn (*kiên nhẫn, ngăn kéo*);
  - `1`: người lớn đa số hiểu nhưng ít dùng, thiên về văn viết (*thanh khiết, mộc mạc*).
- Hoặc **loại cả nhóm** với lý do: `PROPER` (tên riêng, lễ tết, dân tộc…), `VIOLENCE` (bạo lực, vũ khí, chiến tranh, tội phạm, thảm hoạ), `OFFENSIVE` (thô tục, tình dục, xúc phạm, ghê tởm, hoặc khi bỏ dấu đọc thành từ thô tục), `DISEASE` (bệnh tật, thương tích, thuốc, cái chết), `SENSITIVE` (chính trị, tôn giáo, mê tín, luật pháp, rượu bia, ma tuý, cờ bạc, cảm xúc tiêu cực mạnh), `SPELLING` (nhiều cách viết, hay bị viết sai), `RARE` (không đủ thông dụng, cổ, địa phương, chuyên ngành).
- Mỗi tác tử phải chạy script kiểm tra trước khi nộp: đủ số dòng, đúng thứ tự, từ được chọn phải nằm trong nhóm, điểm và lý do hợp lệ.

### 4.6. Vòng hai cho các nhóm bị loại vì chính tả

1.013 nhóm bị loại với lý do `SPELLING` được đánh giá lại (3 lô). Tác tử chọn lại từ, chấm điểm và phân loại rủi ro chính tả:

- `TONE`: chỉ dễ nhầm hỏi/ngã (*sữa/sửa, lỗi/lổi*). Lỗi này không làm sai bản không dấu, vốn là bản người dùng gõ nhiều nhất.
- `RAREVAR`: cách viết còn lại đã cũ hoặc là phương ngữ, ngày nay hầu như không dùng (*giòng, giăng, nhẩy, thày*).
- `OTHER`: hai cách viết đều phổ biến (*từ điển/tự điển, màu/mầu, cám ơn/cảm ơn*), lỗi làm đổi chữ cái (*sử dụng/xử dụng, chuyện/truyện, cập nhật/cập nhập*) hoặc nhầm dấu mũ/dấu thanh khác (*cầu vồng/cầu vòng*). Nhóm này vẫn bị loại.

Từ `TONE`/`RAREVAR` được giữ nhưng bị trừ 0,5 điểm.

### 4.7. Chọn 7.776 từ

1. Giữ 40 từ mẫu đã duyệt.
2. Xếp các từ còn lại theo điểm hiệu dụng: 3 > 2,5 (điểm 3 có rủi ro hỏi/ngã) > 2 > 1,5 > 1 > 0,5. Cùng điểm thì xếp theo độ phổ biến.
3. Lấy từ đầu danh sách cho đủ 7.776. Điểm cắt rơi vào nhóm điểm 1, ở từ *thường dân* (4,95 lần/triệu), nên chỉ 295 từ điểm 1 phổ biến nhất được dùng.

### 4.8. Viết giải nghĩa

7.736 từ (trừ 40 từ mẫu đã có giải nghĩa) được chia thành 20 lô và giao cho các tác tử viết giải nghĩa theo cùng một hướng dẫn:

- tiếng Việt, tự viết, không chép từ điển;
- giải thích nghĩa phổ biến nhất (tối đa hai nghĩa), thường 5–15 từ, không quá 110 kí tự;
- bắt đầu bằng chữ hoa, kết thúc bằng dấu chấm, không chứa `|`, giọng trung tính;
- dùng 40 định nghĩa mẫu làm chuẩn văn phong.

Bước này cũng là một lượt rà soát cuối: tác tử đánh dấu từ nào rõ ràng không phù hợp. Có 5 từ bị đánh dấu, xem sự cố 6.10.

## 5. Cách đánh giá

### 5.1. Kiểm tra tự động

- **Mỗi lô:** script kiểm tra định dạng, số dòng, thứ tự, từ được chọn có nằm trong nhóm không, điểm và mã lý do có hợp lệ không; với giải nghĩa thì kiểm tra độ dài, chữ hoa, dấu chấm, kí tự cấm.
- **Danh sách cuối của phương án này** (kiểm khi danh sách còn nằm trong hai trang HTML): đúng 7.776 từ, ở sẵn dạng NFC; không trùng, kể cả sau khi bỏ dấu và viết liền; mọi từ dài ≥4 chữ cái, viết thường, không chứa `-`, `|` hay tab, không có dấu cách thừa; mọi từ có giải nghĩa hợp lệ; khối `#wordlist` của [`index.html`](index.html) và [`thong-tin.html`](thong-tin.html) khi đó có cùng danh sách, cùng thứ tự alphabet tiếng Việt. App không chuẩn hoá hay lọc lại danh sách lúc chạy, nên các điều kiện này phải đúng ngay trong file.
- **Trên trình duyệt (Edge không giao diện), với danh sách này:** [`index.html`](index.html) báo 7.776 từ, entropy 77,5 bit với 6 từ; [`thong-tin.html`](thong-tin.html) báo tổng cộng 7.776 từ, các trang chữ cái cộng lại đủ 7.776 dòng.

### 5.2. Kiểm tra thủ công (lấy mẫu)

- Đọc lô thử nghiệm đầu tiên, rồi đọc mẫu ngẫu nhiên theo từng mức điểm và từng lý do loại để hiệu chỉnh hướng dẫn (xem 6.4–6.5).
- Quét các từ được giữ có chứa âm tiết nhạy cảm (*chết, máu, súng, bệnh, đảng, phật, dâm, đĩ, rượu, tù*…). Hầu hết là trường hợp vô hại như *ma sát, sư tử, tử tế, phật lòng (= phiền lòng), chào cờ*.
- Quét các từ được chọn mà nhóm không dấu của chúng có chứa từ thô tục hay từ chỉ bệnh (xem 6.10).
- Đọc mẫu giải nghĩa ở từng lô: nội dung đúng, ngắn gọn, văn phong thống nhất. Chỉ một định nghĩa có mốc thời gian (*huyện*), đã sửa lại (6.11).

### 5.3. Số liệu đánh giá

Kết quả của 22.136 nhóm sau mọi vòng đánh giá:

| Kết quả | Số nhóm |
|---|---|
| Giữ, điểm 3 / 2,5 / 2 / 1,5 / 1 / 0,5 | 1.091 / 29 / 6.060 / 261 / 4.022 / 84 |
| Loại vì RARE (không đủ thông dụng) | 5.535 |
| Loại vì SENSITIVE | 1.736 |
| Loại vì VIOLENCE | 1.157 |
| Loại vì DISEASE | 892 |
| Loại vì OFFENSIVE | 592 |
| Loại vì SPELLING (sau vòng hai) | 526 |
| Loại vì PROPER | 149 |
| Loại sau khi rà soát cuối | 2 |

Tỉ lệ nhóm đạt điểm ≥2 giảm dần theo hạng tần suất. Đây là căn cứ để mở rộng vòng đánh giá:

| Hạng tần suất | 0–2k | 2–4k | 4–6k | 6–8k | 8–10k | 10–12k | 12–14k | nhóm 11K còn lại | mở rộng 14k–22k |
|---|---|---|---|---|---|---|---|---|---|
| Đạt điểm ≥2 | 79,5% | 59,6% | 46,4% | 37,9% | 32,6% | 27,8% | 19,4% | 10,9% | khoảng 12–15% |

### 5.4. Entropy và độ nhập nhằng

- Mỗi từ có 12,92 bit vì danh sách không trùng nhau kể cả ở bản không dấu. Công thức entropy của app (`log2(số từ)`) đúng cho cả hai bản có dấu và không dấu.
- **"Phân cách từ ghép"**: khi bật tùy chọn này, từ ghép *A B* + từ *C* và từ *A* + từ ghép *B C* đều thành `A_B_C`. Trên danh sách này, số cặp 2 từ bị nhập nhằng như vậy là 1.581 cặp ở bản có dấu và 20.665 cặp ở bản không dấu, trên tổng số 7.776² ≈ 60,5 triệu cặp (0,034%). Mức giảm entropy không đáng kể (dưới 0,001 bit). Đơn vị của các số này được nêu lại cho đúng ở 9.1, dòng 8.
- Để trống dấu phân cách vẫn có thể gây nhập nhằng như [README](README.md#3-entropy) đã nêu, nên vẫn khuyên luôn dùng dấu phân cách.

## 6. Các sự cố phát sinh và cách xử lý

1. **Từ đơn không đủ 7.776.** Sau khi bỏ dấu và gộp trùng chỉ còn khoảng 1.300 từ đơn thông dụng. Cách xử lý: dùng thêm từ ghép 2 âm tiết. Chủ dự án chọn cách viết liền trong passphrase, lưu có dấu cách để hiển thị, và sau đó thêm tùy chọn "Phân cách từ ghép".
2. **Bộ 11K/22K thiếu cả những từ rất phổ biến** (*máy bay, mặt trời, đồng hồ, bút chì, công viên* chỉ có trong bộ 74K). Không thể dùng các bộ nhỏ làm thước đo độ phổ biến, nên chuyển sang dùng bộ 74K kết hợp tần suất trong kho văn bản.
3. **Trang Leipzig Corpora Collection chặn truy cập tự động** (trang kiểm tra chống bot Anubis). Không cố vượt qua; dùng các kho văn bản của OPUS, vốn được cung cấp để tải về.
4. **Phụ đề phim (chủ yếu dịch từ phim nước ngoài) đếm thiếu từ văn hoá Việt**, ví dụ *rau muống* 0 lần, *bánh chưng* 0,12 lần/triệu. Cách xử lý: thêm kho web CCAligned, và đưa mọi nhóm có từ thuộc bộ 11K vào vòng đánh giá. Một số từ như *rau muống* vẫn ít xuất hiện; chúng có mặt nhờ thuộc 40 từ mẫu.
5. **Lô thử nghiệm đầu tiên** (489 nhóm, khoảng 16 phút) cho thấy điểm 3 được dùng rất dè dặt và lý do SPELLING bị dùng cho cả cặp đảo thứ tự (*ngang dọc / dọc ngang*). Hướng dẫn được bổ sung: SPELLING không áp dụng cho từ đồng nghĩa hay cặp đảo thứ tự.
6. **Thiếu từ điểm cao.** Tỉ lệ đạt điểm ≥2 giảm nhanh theo hạng tần suất; sau vòng chính chỉ có khoảng 6.300 từ đạt điểm ≥2, nếu dừng ở đó thì phải dùng 1.435 từ điểm 1. Cách xử lý: đánh giá thêm 6.000 nhóm (còn cần 583 từ điểm 1), rồi chạy vòng hai cho SPELLING (còn cần 295 từ điểm 1).
7. **Ví dụ trong hướng dẫn quá chặt.** Hướng dẫn ban đầu liệt kê *dòng/giòng, trăng/giăng, nhảy/nhẩy* là biến thể chính tả, khiến các tác tử loại cả *dòng điện, trăng tròn, chạy nhảy, thầy*. Hướng dẫn được sửa cho vòng mở rộng (biến thể cổ hoặc phương ngữ ít dùng không phải lý do để loại), còn các nhóm bị loại trước đó được xét lại ở vòng hai.
8. **Loại quá tay vì hỏi/ngã.** Nhiều từ rất thông dụng bị loại chỉ vì có thể nhầm hỏi/ngã (*sữa tươi, mạnh mẽ, dễ thương, nghỉ ngơi, rực rỡ*). Vì lỗi hỏi/ngã không làm sai bản không dấu, vòng hai giữ lại các từ này nhưng trừ 0,5 điểm; tổng cộng 290 từ được giữ theo cách này.
9. **Bản không dấu có thể đọc thành từ thô tục.** Vì app hiện cả passphrase không dấu, các tác tử đã loại những nhóm mà dạng không dấu trùng với từ tục hay nhạy cảm (*đảm đang/dâm đãng → damdang*, *mái dầm/mại dâm → maidam*, *lợn thịt, cu gáy, chim cu*…).
10. **Từ bị đánh dấu khi viết giải nghĩa** (5 từ). Quy tắc xử lý: chỉ loại khi chính nhóm không dấu của từ đó có chứa từ thô tục.
    - Đã loại *bưởi* (nhóm `buoi` có từ tục *buồi*) và *phích* (nhóm `phich` có từ lóng tục *phịch*), thay bằng hai từ kế tiếp trong danh sách xếp hạng.
    - Giữ *cao lớn, cho dù, khôn lớn*, vì nghĩa xấu chỉ xuất hiện khi tách âm tiết theo cách khác.
    - Giữ *đại dương, bỏ đi, dại khờ*: nhóm không dấu của chúng chỉ có từ hiếm (*đái đường, bố đĩ, đái khó*), và cách đọc tự nhiên vẫn là từ thông dụng.
11. **Định nghĩa có thông tin theo thời điểm.** Giải nghĩa của *huyện* ban đầu có câu "đã bãi bỏ từ năm 2025". Đã sửa thành định nghĩa không phụ thuộc thời gian.
12. **Đọc nhầm file đang ghi dở.** Một lần gộp kết quả bị lỗi vì một tác tử còn đang ghi file đầu ra. Cách xử lý: chỉ gộp khi mọi tác tử đã xong, sau đó chạy lại script kiểm tra.
13. **Đánh giá mang tính chủ quan.** Mỗi tác tử có thể chấm khác nhau một chút, ví dụ *từ từ* được giữ dù bản không dấu `tutu` gần với *tự tử*. Cách giảm thiểu: dùng chung hướng dẫn, chia lô xoay vòng theo tần suất, có script kiểm tra, và một lượt rà soát độc lập lúc viết giải nghĩa.

## 7. Hạn chế và hướng cải thiện

- **Đánh giá bằng LLM:** độ "thông dụng" và "nhạy cảm" là đánh giá chủ quan và có thể còn sót, nhất là khi mỗi nhóm chỉ do một tác tử chấm. Quy trình thống nhất đã cho hai bên chấm độc lập mọi mục (P4) và Astra đọc trọn danh sách trước khi chốt; nhiều mục của phương án này bị loại ở các bước đó, riêng 295 từ điểm 1 (*bá tước, hạ tầng, điều khoản*) chỉ còn 130 từ trong bản phát hành (xem [Kết quả cuối cùng](#kết-quả-cuối-cùng)).
- **Thiên lệch của kho văn bản:** phụ đề là phim dịch, còn CCAligned chủ yếu là trang thương mại, nên từ văn hoá, ẩm thực Việt bị xếp hạng thấp hơn thực tế. Quy trình thống nhất đo thêm Leipzig và Tatoeba, và bổ sung các lô từ đời thường L2–L3.
- **Rủi ro chính tả còn lại:** 290 từ có rủi ro hỏi/ngã hoặc biến thể cũ. Quy trình thống nhất thay mức trừ 0,5 điểm bằng tỉ lệ đo riêng từng kho theo luật H5.
- **Giải nghĩa:** do LLM viết, ngắn gọn và không thay được từ điển; review chéo tìm thấy 38 nghĩa sai hoặc hẹp trong mẫu 360 mục (9.1, dòng 6). Bản phát hành không dùng các giải nghĩa này, vì chủ dự án quyết viết mới toàn bộ (9.2).
- **Khả năng tái lập:** các file trung gian (ứng viên, tần suất, kết quả từng lô) và script xử lý của phương án này không được đưa vào repo. Danh sách thống nhất có công cụ, nhãn, số đếm và hồ sơ làm việc trong [`analyzing-tools/`](analyzing-tools/README.md).

## 8. Tóm tắt quy mô xử lý

| Bước | Quy mô |
|---|---|
| Ứng viên sau lọc tự động | 45.605 từ, 37.807 nhóm không dấu |
| Đếm tần suất | 2 kho văn bản, khoảng 184 triệu âm tiết |
| Đánh giá lượt đầu | 22.136 nhóm, 45 lô |
| Đánh giá lại chính tả | 1.013 nhóm, 3 lô |
| Viết giải nghĩa và rà soát cuối | 7.736 từ, 20 lô |
| Tổng số lượt tác tử LLM | 68 |

## 9. Kết quả review chéo

Astra review mục 1–9 (bản trước khi thêm mục này) và toàn bộ danh sách. Với mỗi nhận xét, Opus kiểm lại bằng dữ liệu (đếm lại, chạy lại script) rồi mới đồng ý hay phản bác. Hai bên dùng kết quả đó để soạn bộ tiêu chí chung trong [phân tích thống nhất](WordListAnalyze.md).

### 9.1. Lỗi và điểm yếu đã xác nhận

| # | Vấn đề | Kiểm chứng | Cách xử lý trong quy trình thống nhất |
|---|---|---|---|
| 1 | **Thứ tự sắp xếp.** Danh sách được xếp kiểu so cả chuỗi chữ trước rồi mới so thanh, giống `Intl.Collator("vi")`. Cách này không theo quy ước so từng âm tiết | Có 1.228 cặp kề nhau bị ngược theo quy ước từng âm tiết, ví dụ *ánh mắt* đứng trước *anh rể*, *ám chỉ* đứng trước *ảm đạm*. Không mất hay thừa từ nào | Quy ước chung so từng âm tiết (O1), kiểm bằng một bộ so tham chiếu riêng |
| 2 | **Lỗi đếm tần suất.** Cụm hai âm tiết được ghép từ mọi âm tiết trên dòng, nên vắt qua dấu câu và ranh giới từ. Âm tiết đứng riêng bị đếm cả những lần nằm trong từ ghép | Đếm lại theo ranh giới âm tiết, dấu câu và từ thì nhiều số đo thay đổi:<br>• lỗi viết *bánh trưng* từ 24% xuống 0%, vì cả 18 lượt là *bánh* đứng trước *trưng bày*;<br>• *năng suất* từ 16,7% xuống 2,2% ở phụ đề;<br>• *súc tích* từ 38,7% xuống 2,5% ở web | Bộ đếm mới có ranh giới; số đếm lại dùng cho bảng khóa chung. Mục một âm tiết đo thêm tỉ lệ đứng độc lập |
| 3 | **Luật `i/y` quá tay.** Quy trình cũ chặn biến thể `i/y` cả sau `d, n, v` | Luật này loại nhầm 368 từ như *vị trí, đơn vị, di chuyển* | Chỉ áp sau `h, k, l, m, s, t, qu` (H5b). Các mục bị loại nhầm được đưa lại vào rổ để xét |
| 4 | **Luật chính tả quá chặt.** Lý do SPELLING được dùng theo cảm tính: 526 nhóm bị loại sau vòng hai | Nhiều từ có tỉ lệ viết sai rất thấp: *sử dụng* 0,1%, *sản xuất* 0,0%, *tập trung* 0,6%, *đặc biệt* 0,4%, *sẵn sàng* 0,7%, *xảy ra* 0,5%. Mức trừ 0,5 điểm cho hỏi/ngã (6.8) chưa được hiệu chuẩn | Quyết theo tỉ lệ đo riêng từng kho, chỉ cho cặp đã xác nhận là cùng một từ (H5). Các nhóm từng bị loại được xét lại |
| 5 | **Sáu mục nên thay** | Astra đề nghị thay:<br>• *la mắng*: gây hấn;<br>• *sống lại*: hồi sinh sau khi chết;<br>• *cô bác*: khóa không dấu đọc thành *cờ bạc*;<br>• *nữ thần*: thần linh;<br>• *điên đầu, xấu xí*: chê bai.<br>Opus đồng ý cả sáu và tự thêm *mũi tên* (vũ khí) | Loại theo nhóm đỏ (H6) và cổng đọc không dấu (H7) |
| 6 | **38 giải nghĩa sai hoặc hẹp**, trong mẫu 360 mục Astra đọc | Ví dụ:<br>• *viết hoa, chữ hoa* nhầm dạng chữ với cỡ chữ;<br>• *sương mù* bị giải là hơi nước;<br>• *cá voi* bị giải như thể loài nào cũng lớn nhất;<br>• *nhập cảnh, tiền túi* bị hiểu hẹp;<br>• *tạm thời* và *nhất thời* dùng chung một câu.<br>Hướng dẫn viết cũ còn khuyến khích né nghĩa nhạy cảm | Chủ dự án quyết viết mới toàn bộ giải nghĩa. Luật mới cấm "làm sạch" nghĩa: nghĩa phổ biến thuộc nhóm đỏ thì gắn cờ và xét lại từ |
| 7 | **Khóa không dấu đọc thành từ nhạy cảm**, kể cả các mục cũng có trong danh sách Astra | Các mục bị nêu: *từ từ* (↔ *tự tử*), *lót dạ* (↔ *lột da*), *đầu đàn, đấu thủ, tư nhân, bàn tính, cổ kính, nhà thơ, thanh thản*. Opus tự rà thêm *bảo thủ* (↔ *báo thù*), *khổ thơ* (↔ *khó thở*), *kinh thành* (↔ *kinh thánh*), *làm dâu* (↔ *làm đau*), *phần đông* (↔ *phản động*), rồi đồng ý thêm *mạnh dạn* (↔ *mảnh đạn*) theo đề nghị của Astra.<br>Theo cổng thống nhất (bản luật v4.1), danh sách này có:<br>• 33 mục thuộc khóa chặn K1;<br>• 16 mục thuộc khóa chặn K0, gồm cả hai khóa `buom`, `chim` theo quyết định của chủ dự án | Cổng đọc không dấu ba mức K0/K1/K2 áp cho mọi mục. Quy tắc ở 6.10 (chỉ loại khi nhóm không dấu có từ thô tục) không đủ |
| 8 | **Số liệu nhập nhằng nêu nhầm đơn vị** (5.4) | 20.665 là số **chuỗi đầu ra** nhập nhằng ở bản không dấu. Mỗi chuỗi ứng với hai lượt chọn có thứ tự, tức 41.330 lượt (0,0684%). Mức hụt là 0,000684 bit cho hai lượt; kết luận "rất nhỏ" vẫn đúng. Bộ kiểm cũ chỉ xét kiểu tách 1+2 ↔ 2+1 | Kiểm tra mới xét mọi vị trí cắt (C9) |
| 9 | **Câu chữ sai ở mục 1 và 4.1** | "Từ ghép luôn ≥ 4 chữ" là sai: *ô tô, y tế* chỉ có 3 chữ. Thành phẩm vẫn đúng vì có phép kiểm ≥ 4. "490 / 7.286" là số mục một khối / hai khối, không phải từ đơn / từ ghép: *radio, karaoke* là một khối | Gọi là "mục một khối", "mục hai khối" |
| 10 | **Quy trình chấm.** Mỗi nhóm chỉ một tác tử chấm, không có phiếu độc lập. Chỉ rà lại 295 mục điểm 1 là không đủ | Đúng | Chấm chéo toàn bộ. Trước đó hiệu chỉnh thang chấm trên mẫu chung: κ = 0,671, đồng thuận 91,33% |
| 11 | **Tái lập và ghi nguồn chưa đủ.** Script và file trung gian không được lưu; nguồn chưa ghi đủ phiên bản và giấy phép | Đúng:<br>• danh sách Hồ Ngọc Đức là GNU GPL v2, bản `688b095`;<br>• OpenSubtitles cần ghi công OpenSubtitles.org và Lison & Tiedemann (2016);<br>• văn bản gốc của CCAligned không phải CC0 | Script, manifest và hồ sơ làm việc đã được đưa vào [`analyzing-tools/`](analyzing-tools/README.md) (kế hoạch gọi là thư mục tools; chủ dự án đổi tên ở quyết định 9). Manifest chỉ chứa nguồn, phiên bản, hash, số đếm và giấy phép |

### 9.2. Những điểm Opus giữ quan điểm

- **Giấy phép giải nghĩa.** Giải nghĩa của Opus được viết khi tác tử chỉ nhận danh sách từ, không có nghĩa từ điển trong lời nhắc. Ngược lại, bản nháp nghĩa của Astra được sinh từ lời nhắc có nghĩa Wiktionary (CC BY-SA). Astra đã xác nhận điểm này. Sau đó chủ dự án quyết viết mới toàn bộ giải nghĩa của danh sách thống nhất, nên giải nghĩa cũ của **cả hai** bên đều không được dùng.
- **Không phủ quyết từ lành vì lý do xa.** Opus giữ:
  - thiên thể: *mặt trời, mặt trăng, trái đất*;
  - nhân vật cổ tích: *công chúa, hoàng tử*;
  - cảm xúc thường ngày: *buồn, khóc, giận dỗi*;
  - từ cơ thể, sinh hoạt: *mồ hôi, ruồi, gián*.

  Chủ dự án đồng ý, và quyết giữ thêm *ngân hà, hoàng hậu, chào cờ*.
- **Từ đời thường thiếu mục Wiktionary vẫn có giá trị.** Ví dụ *đèn bàn, cầu trượt*: có trong Viet74K và có tần suất rõ. Bộ tiêu chí chung nhận cả hai nguồn từ điển (H3).
- **Không bắt buộc bỏ một từ trong cặp vùng miền** (*sách/xách*), và **giữ *ròng rọc, dép lê*** dù vắng ở kho câu nhỏ. Hai bên đồng ý.
- **Hư từ, đại từ phải có giới hạn**, và loại các dãy sinh theo mẫu (*chúng/bọn* + đại từ). Điểm này thành hạn mức Q3 (≤ 1%).

**Những đề xuất Opus đã rút, hoặc chủ dự án quyết khác:**

- nhận *buồm* cho khóa `buom`: chủ dự án quyết để trống khóa;
- dùng từ 3 chữ làm bậc lấp cuối: chủ dự án quyết không dùng;
- nhận mục 4 khối ≤ 12 chữ: không dùng ở bản 1;
- giữ *bướm đêm*: Opus rút ý kiến, vì từ này có nghĩa bóng phổ biến.

### 9.3. Bản lưu trữ ở mục 10

Danh sách ở mục 10 là phương án độc lập của Opus, lưu để đối chiếu. Ở bước P8 (ngày 20/11/2026), danh sách thống nhất đã thay bản này trong [`index.html`](index.html) và [`thong-tin.html`](thong-tin.html).

Theo [cổng tự động thống nhất](analyzing-tools/ho-so/unified/cong-opus-v4.tsv) (bản luật v4.1), 131 mục của danh sách này bị loại ngay và 246 mục ở trạng thái chờ. Mọi mục không bị loại ở cổng đều qua chấm chéo P4. Kết quả của cả 7.776 mục ở mục [Kết quả cuối cùng](#kết-quả-cuối-cùng).

## Kết quả cuối cùng

Ngày 20/11/2026, theo [quyết định 10 của chủ dự án](WordListAnalyze.md#3-quyết-định-của-chủ-dự-án), danh sách thống nhất 7.776 từ được phát hành cùng giải nghĩa viết mới (MIT). [205 từ dự phòng](analyzing-tools/du-phong.txt) ở trạng thái "dự phòng, chưa phân tích", không được phát hành.

**Cách đo.** Opus so cột từ của khối ở mục 10 với [nguồn chuẩn phát hành](analyzing-tools/wordlist.txt): trước hết so nguyên mặt chữ, rồi so khóa của app (NFD, bỏ dấu kết hợp, `đ` → `d`, viết thường, bỏ dấu cách). Với từ không còn trong bản phát hành, điểm dừng và lý do lấy từ hồ sơ: [cổng P2](analyzing-tools/ho-so/unified/cong-opus-v4.tsv), phiếu P4 của [Opus](analyzing-tools/ho-so/unified/phieu-opus.tsv) và [Astra](analyzing-tools/ho-so/unified/phieu-astra.tsv), [phản biện H9](analyzing-tools/ho-so/unified/phan-bien.tsv), [chọn P5](analyzing-tools/ho-so/unified/ket-qua-chon.tsv), [đầu vào P6](analyzing-tools/ho-so/unified/p6-dau-vao.tsv), [xếp hạng P6](analyzing-tools/ho-so/unified/xep-hang.tsv), các biên bản khấu trừ và [hồ sơ nguồn gốc giải nghĩa D8](analyzing-tools/nguon-goc-giai-nghia.tsv). Mỗi từ chỉ tính một lần, ở bước đầu tiên làm nó rời danh sách.

| 7.776 từ của Opus so với bản phát hành | Số từ |
|---|---:|
| Có nguyên mặt chữ trong bản phát hành | **6.318** (81,25%) |
| Khóa vẫn có, nhưng bản phát hành chọn mặt chữ khác | **63** |
| Không còn cả khóa (bị loại) | **1.395** |

- **Phần được giữ.** 6.318 từ này chiếm 81,25% bản phát hành: 3.802 từ chung với Astra (giữ 87,6% trong 4.340 từ chung) và 2.516 từ chỉ Opus chọn (giữ 73,2% trong 3.436). Bản phát hành giữ 37/40 từ mẫu (bỏ *bướm* theo quyết định 2, *cà phê* vì cạnh tranh với *cafe*, *thước* vì khóa `thuoc` đọc thành *thuốc*) và các từ đời thường Opus bảo vệ ở 9.2 như *đèn bàn, cầu trượt, ròng rọc, dép lê, mặt trời, công chúa, mồ hôi*.
- **63 khóa đổi mặt chữ.** 55 khóa do P5 chọn mặt chữ cụ thể hơn hoặc thông dụng hơn theo S1 (*có lẽ* → *cờ lê*, *riêng* → *riềng*, *thấy* → *thầy*, *công tác* → *công tắc*). 8 khóa do mặt chữ của Opus bị loại ở P4: 6 cụm tự do như *cho ăn, ngủ ngon*, 1 từ hiếm, 1 từ vướng chính tả.
- **Phần còn lại của bản phát hành** là 1.395 khóa không có trong danh sách Opus (bằng số từ bị loại, vì hai danh sách cùng có 7.776 khóa): 904 từ chỉ Astra chọn, 168 ứng viên bổ sung ở P1 và 323 từ các lô L2–L3 (*thú cưng, gấu bông, mũ bảo hiểm*).

**1.395 từ bị loại, theo điểm dừng:**

| Điểm dừng | Số từ | Lý do chính |
|---|---:|---|
| Cổng tự động P2 | 131 | 53 vướng cổng đọc không dấu H7: 16 thuộc khóa K0 (kể cả *bướm, chim* và *nhà thơ*, khóa vướng cả K1), 32 chỉ thuộc khóa K1 (*từ từ, lót dạ*), 5 thuộc khóa K2 chưa đủ chữ ký. 36 thuộc các mục đã chốt trong [bộ tiêu chí](analyzing-tools/tieu-chi-thong-nhat.md): 24 mục nhạy cảm đã chốt loại (*la mắng, mũi tên, sống lại*) và 12 dãy *chúng/bọn* + đại từ. 28 vướng chính tả H5. 13 là dãy số (*hai mươi, trăm năm*). 1 thuộc khóa đã bỏ (*ngày giờ*, cùng khóa với *ngày giỗ*) |
| Chấm chéo P4 và phản biện H9 | 530 | 296 nhãn X: cụm tự do, khung câu (*đi vào, con ngựa, cây bút, không thể*). 183 nhãn S (nhóm đỏ): 115 chê bai, miệt thị (*keo kiệt, lười biếng*), 25 chính trị, quyền lực (*quốc gia, hoàng đế*), 15 tôn giáo, số mệnh (*định mệnh, nghi lễ*), 28 thuộc các nhóm khác. 35 nhãn K (đọc không dấu), 13 nhãn V (chính tả), 3 nhãn R2 (hiếm) |
| Chọn trong khóa P5 | 7 | P5 chọn mặt chữ khác (*ngon* → *ngón*, *hướng* → *hương*) hoặc bỏ cả khóa (*hết mức*); về sau các khóa này cũng không vào bản phát hành |
| Xếp hạng P6 | 564 | Qua mọi cổng nhưng không đủ hạng. 288 nhãn R1 (thiên văn viết, chuyên môn): danh sách chính lấy hết mục OK trước nên không còn chỗ cho R1. 200 hư từ lớp F ngoài hạn mức 77 (Q3). 76 mục OK khác dưới điểm cắt. 149 từ trong nhóm này nằm trong 205 dự phòng |
| [Khấu trừ cuối P6](analyzing-tools/ho-so/unified/p6-khau-tru-cuoi.tsv) | 17 | 14 ca H6: nghĩa thuộc nhóm đỏ hoặc đề tài giới (*nóng bỏng, thần tượng, giáp, nam tính*); 3 ca chính tả (*cà phê, xe buýt, tập dượt*) |
| Khấu trừ H6 ở P7 ([v1](analyzing-tools/ho-so/unified/p7-khau-tru.tsv), [v2](analyzing-tools/ho-so/unified/p7-khau-tru-v2.tsv)) | 19 | Nghĩa còn dùng phổ biến thuộc nhóm đỏ, lộ ra khi viết và soát giải nghĩa (*áo mưa, thịt, bóng, thanh toán, đi lại*) |
| [Giải nghĩa mới chưa đạt](analyzing-tools/ho-so/unified/p7-v3-khau-tru-132-theo-P0-astra.tsv) | 127 | Sau hai lượt viết lại, 117 câu vẫn trượt D6 và 10 câu còn lỗi nội dung D7, nên từ bị thay theo luật đã ký (P0). Đây là kết luận về câu giải nghĩa, không phải về bản thân từ |
| **Tổng** | **1.395** | |

Gộp theo nhóm lý do: cụm tự do, khung câu, dãy sinh 321; độ quen thấp (R1, R2) 291; nghĩa nhạy cảm H6 240; hư từ ngoài hạn mức 200; giải nghĩa mới chưa đạt 127; đọc không dấu 89; mục OK dưới điểm cắt 76; chính tả 44; chọn trong khóa 7. Hồ sơ D8 ghi `LOAI` cho 182 từ ở P6–P7, trong đó 163 từ thuộc danh sách này.

**Bài học về phương pháp của Opus:**

- **Có trong từ điển và hay gặp chưa đủ để là một từ.** Lấy mục hai âm tiết của Viet74K rồi xếp theo tần suất cặp âm tiết làm lọt nhiều cụm tự do, khung câu và dãy sinh. Đây là nhóm bị loại lớn nhất (321 từ); khi chấm chéo, chính Opus gắn X cho 274 trong 296 từ bị loại vì nhãn này. Hư từ cũng cần hạn mức cứng từ đầu: thang cũ cho hư từ điểm 2 (*tuy nhiên*), nên 200 hư từ của danh sách nằm ngoài hạn mức 77.
- **Bộ lọc nhạy cảm bị áp quá hẹp.** Các nhóm loại cũ có nêu chính trị, tôn giáo, xúc phạm, nhưng vẫn lọt từ chê bai tính cách (*keo kiệt, lười biếng*), từ về quyền lực, vua chúa (*quốc gia, hoàng đế*) và số mệnh (*định mệnh*). Trong 183 từ bị loại vì nhãn S ở P4, 142 từ chỉ Astra phản đối. Quy tắc 6.10 cũng bỏ sót các khóa đọc thành từ nhạy cảm (*từ từ, lót dạ*). Cần bảng nhóm đỏ có ví dụ loại và không loại, cổng đọc không dấu riêng, và người chấm thứ hai.
- **Chính tả phải đo, và sai lệch có cả hai chiều.** 127 từ mà quy trình cũ đã loại (97 vì SPELLING, 30 vì luật `i/y`) nay qua H5 và có trong bản phát hành (*cập nhật, cà vạt, công ty, quy tắc, di dời*). Ngược lại, 44 từ của danh sách bị loại theo tỉ lệ đo được, như *sữa tươi, rảnh rỗi, mải mê*, vốn được giữ ở vòng hai với mức trừ 0,5 điểm.
- **Thang điểm phân biệt tốt ở đầu, yếu ở đuôi.** Đối chiếu với bảng điểm gốc (hồ sơ làm việc của phương án này, không đưa vào repo vì chứa danh sách ứng viên Hồ Ngọc Đức): bản phát hành giữ 980/1.091 từ điểm 3 (89,8%), 4.945/6.060 từ điểm 2 (81,6%), 226/290 từ được giữ ở vòng hai chính tả, nhưng chỉ 130/295 từ điểm 1 (44,1%). Phần đuôi lấp bằng từ trang trọng là phần yếu nhất; quy trình thống nhất bù bằng cách mở rộng rổ ứng viên đời thường (các lô L2–L3 góp 323 từ cho bản phát hành).
- **Giải nghĩa viết sớm thành ràng buộc khi phải viết lại.** Giải nghĩa cũ của Opus không chép từ điển (9.2) nhưng nằm trong tập tham chiếu D6. Trong bản phát hành, câu giải nghĩa của 2.157/6.318 từ thuộc danh sách này (34,1%) đến từ lượt viết lại, so với 167/1.458 (11,5%) ở các từ khác. 117/122 từ trượt D6 ở lượt cuối là từ Opus; với 100 từ trong số đó, câu mới chạm đúng giải nghĩa cũ của Opus ([log D6 lượt v3](analyzing-tools/ho-so/unified/d6-log-v3.tsv)). Theo [phân tích D6](WordListAnalyze.md#57-p7-viết-mới-giải-nghĩa), số liệu phù hợp với hội tụ văn phong của cùng họ mô hình, không thấy bằng chứng rò nguồn.
- **Một người chấm và không lưu hồ sơ thì lỗi khó lộ.** Lỗi đếm vắt từ, thứ tự sắp xếp và luật `i/y` quá tay chỉ lộ ra khi review chéo và đếm lại (9.1). Quy trình thống nhất chấm đôi mọi mục, dùng hai bộ kiểm độc lập và lưu hồ sơ trong [`analyzing-tools/`](analyzing-tools/README.md).

## 10. Danh sách 7.776 từ

Bản lưu trữ phương án Opus: nguyên văn khối `#wordlist` của [`thong-tin.html`](thong-tin.html) lúc bắt đầu hợp nhất, trước khi danh sách thống nhất thay vào. Gồm 7.776 dòng `từ|giải nghĩa`, theo thứ tự cũ (xem 9.1, dòng 1), cùng thứ tự với khối của [`index.html`](index.html) lúc đó. Khối được giữ nguyên từng byte vì là tập tham chiếu của [bộ kiểm nguồn gốc D6](analyzing-tools/d6-kiem.py) (SHA-256 thân khối, UTF-8, LF, có LF cuối: `97d0b2fba487118029a83cd4aebd1c45248c3a1a3a5282cf5bb3ef506e56da0d`). Mục này **không** cập nhật theo danh sách thống nhất. Danh sách phát hành nằm ở [mục 10 của WordListAnalyze.md](WordListAnalyze.md#10-danh-sách-7776-từ-phát-hành); nguồn chuẩn là [`analyzing-tools/wordlist.txt`](analyzing-tools/wordlist.txt).

```text
á hậu|Người đạt giải nhì hoặc giải ba trong cuộc thi hoa hậu.
á quân|Người hoặc đội đoạt giải nhì trong một cuộc thi.
ai dè|Không ngờ tới, dùng khi sự việc xảy ra trái hẳn với điều mình nghĩ.
ai nấy|Tất cả mọi người được nhắc đến, không trừ một ai.
ai ngờ|Không ai lường trước được, dùng khi điều xảy ra ngoài dự đoán.
album|Tập ảnh đóng thành quyển; cũng chỉ tập hợp nhiều bài hát phát hành cùng nhau.
ám chỉ|Nói bóng gió để ngầm nhắc tới ai hoặc chuyện gì.
ảm đạm|Tối tăm, u buồn, thiếu ánh sáng và sức sống.
am hiểu|Hiểu biết sâu và rõ về một lĩnh vực nào đó.
an bình|Yên ổn, êm đềm, không có biến động hay lo âu.
an khang|Bình yên và mạnh khỏe, thường dùng trong lời chúc dịp Tết.
an lành|Yên ổn, tốt đẹp, không gặp điều gì rủi ro.
an nhàn|Sống thong thả, nhàn hạ, không phải vất vả lo toan.
an tâm|Yên lòng, không còn lo lắng hay băn khoăn.
an toàn|Không gặp nguy hiểm, không bị tổn hại hay mất mát.
an ủi|Nói hoặc làm điều gì đó giúp người khác bớt buồn, bớt lo.
anh cả|Người con trai lớn nhất trong gia đình.
anh chàng|Cách gọi thân mật hoặc vui đùa một người đàn ông trẻ.
anh chị|Những người anh, người chị trong nhà; cũng dùng để gọi lịch sự người lớn hơn mình.
anh đào|Cây có hoa màu hồng nhạt rất đẹp, quả nhỏ màu đỏ ăn được.
anh em|Những người con trai cùng cha mẹ; cũng chỉ bạn bè gắn bó như ruột thịt.
anh hai|Người anh lớn nhất trong nhà, cách gọi phổ biến ở miền Nam.
anh họ|Người anh trong họ hàng, không phải anh ruột.
anh hùng|Người có tài năng và lòng dũng cảm, lập nên công trạng lớn.
ảnh hưởng|Tác động làm thay đổi người hoặc sự việc khác.
ánh mắt|Cái nhìn của đôi mắt, thể hiện cảm xúc hay suy nghĩ.
anh rể|Chồng của chị gái mình.
anh ruột|Người anh trai cùng cha mẹ sinh ra với mình.
ánh sáng|Thứ phát ra từ mặt trời, đèn, lửa, giúp mắt nhìn thấy mọi vật.
anh trai|Người con trai cùng cha mẹ và lớn tuổi hơn mình.
ảo ảnh|Hình ảnh không có thật nhưng mắt tưởng như nhìn thấy, như trên sa mạc.
ào ào|Âm thanh mạnh và liên tục như gió thổi, nước chảy; cũng chỉ việc diễn ra nhanh, dồn dập.
ào ạt|Diễn ra mạnh mẽ, dồn dập và với số lượng lớn.
áo ấm|Đồ mặc dày dặn giúp giữ ấm cơ thể khi trời lạnh.
áo bông|Loại áo ấm có lớp bông dày bên trong, mặc vào mùa đông.
áo choàng|Loại áo rộng, dài, khoác bên ngoài để giữ ấm hoặc làm đẹp.
áo cưới|Váy áo cô dâu mặc trong ngày cưới, thường có màu trắng.
áo dài|Trang phục truyền thống Việt Nam, thân dài, xẻ tà, mặc cùng quần.
áo gió|Áo khoác mỏng, nhẹ, dùng để chắn gió.
áo gối|Lớp vải bọc ngoài cái gối, có thể tháo ra để giặt.
ao hồ|Những vùng nước đọng như ao, hồ trên đất liền nói chung.
áo khoác|Loại áo mặc bên ngoài để giữ ấm hoặc chống nắng, gió.
áo lạnh|Áo dày, giữ ấm cơ thể khi trời rét.
áo len|Loại áo đan bằng sợi len, mặc cho ấm khi trời lạnh.
áo lông|Loại áo ấm làm từ lông thú hoặc có lớp lông vũ bên trong.
áo mưa|Đồ mặc bằng chất liệu không thấm nước, dùng để che mưa.
áo phao|Loại áo ấm phồng, nhồi lông vũ hoặc bông; cũng là áo giúp nổi trên nước.
áo phông|Loại áo cộc tay bằng vải thun, cổ tròn, mặc hằng ngày.
áo quần|Đồ mặc trên người nói chung, gồm áo và quần.
áo tắm|Đồ mặc khi đi bơi hoặc tắm biển.
ảo thuật|Nghệ thuật biểu diễn các trò khéo léo khiến người xem tưởng như phép lạ.
áo thun|Loại áo bằng vải co giãn, thường cộc tay, mặc thoải mái hằng ngày.
ảo tưởng|Suy nghĩ không đúng thực tế, tưởng điều không có là có thật.
ao ước|Mong muốn tha thiết có được điều gì đó.
áo vàng|Chiếc áo màu vàng; trong đua xe đạp là áo của người đang dẫn đầu.
áp chảo|Cách nấu cho món ăn vào chảo nóng ít dầu để mặt ngoài vàng giòn.
áp dụng|Đem cách làm, quy định hay kiến thức vào thực tế.
áp đảo|Vượt trội hẳn, lấn át hoàn toàn bên kia.
áp đặt|Bắt người khác phải làm theo ý mình mà không hỏi ý kiến.
áp lực|Sức ép đè lên người hay vật; cũng chỉ sự căng thẳng trong học tập, công việc.
áp phích|Tranh khổ lớn in hình và chữ, dán nơi công cộng để quảng cáo, thông báo.
áp thấp|Vùng có áp suất không khí thấp, thường gây mưa và gió mạnh.
áy náy|Cảm thấy không yên lòng vì nghĩ mình có lỗi với ai đó.
ăn ảnh|Trông đẹp hơn khi lên ảnh hay lên hình.
ăn bốc|Dùng tay để lấy thức ăn đưa vào miệng, không dùng đũa thìa.
ăn chay|Chỉ dùng các món từ rau củ, đậu, không dùng thịt cá.
ăn chung|Cùng ăn với nhau trong một bữa hoặc chia chung đồ ăn.
ăn cỏ|Nói về loài vật sống nhờ ăn cây cỏ, như trâu, bò, dê.
ăn cưới|Đi dự tiệc mừng đám cưới của người khác.
ăn diện|Thích mặc đẹp, trang điểm, chăm chút vẻ ngoài.
ăn đứt|Hơn hẳn, vượt trội hoàn toàn so với người khác.
ăn gian|Lén làm sai luật để giành phần lợi cho mình.
ăn hàng|Thưởng thức quà vặt, món ngon ở các hàng quán bên đường.
ăn học|Được cho đi học hành để có kiến thức, nghề nghiệp.
ăn hỏi|Lễ nhà trai mang sính lễ đến nhà gái để xin cưới.
ăn khách|Được nhiều người ưa chuộng, bán chạy, đông người xem.
ăn khớp|Phù hợp, vừa vặn với nhau, không vênh lệch.
ăn kiêng|Hạn chế hoặc tránh một số món để giữ dáng hay giữ sức khỏe.
ăn liền|Đồ ăn chế biến sẵn, chỉ cần pha nước sôi là dùng được, như mì gói.
ăn lương|Nhận tiền công hằng tháng từ công việc.
ăn mặc|Cách chọn và mặc quần áo của một người.
ăn mặn|Thích ăn đồ mặn; cũng chỉ ăn thịt cá, trái với ăn chay.
ăn mòn|Làm hao mòn dần bề mặt vật liệu, như gỉ sét làm hỏng kim loại.
ăn mừng|Tổ chức vui chơi để chào đón một thành công hay sự kiện vui.
ăn nhịp|Hòa hợp, phối hợp nhịp nhàng với nhau.
ăn no|Đã ăn đủ, bụng đầy, không còn thấy đói.
ăn nói|Cách nói năng, giao tiếp với người khác.
ăn sáng|Dùng bữa đầu tiên trong ngày vào buổi sáng.
ăn sống|Dùng món chưa qua nấu chín, như rau sống, gỏi cá.
ăn tham|Thích ăn nhiều, muốn giành phần hơn người khác.
ăn theo|Dựa vào cái đã nổi tiếng để hưởng lợi theo.
ăn thịt|Dùng thịt làm món ăn; cũng nói loài vật chuyên săn con khác làm mồi.
ăn tiệc|Dự một bữa tiệc vui, thường có nhiều món ngon.
ăn tiệm|Đi ăn ở quán, nhà hàng thay vì nấu ở nhà.
ăn trầu|Nhai lá trầu cùng cau và vôi, một tập quán xưa của người Việt.
ăn uống|Việc ăn và uống hằng ngày nói chung.
ăn vạ|Làm ầm ĩ, khóc lóc để bắt đền hoặc đòi người khác chiều theo.
ăn vặt|Dùng các món nhỏ ngoài bữa chính, như bánh kẹo, trái cây.
ăn vụng|Lén lút ăn khi không ai thấy.
ăn xôi|Dùng món xôi nếp, thường vào bữa sáng.
ấm áp|Ấm và dễ chịu; cũng chỉ cảm giác được quan tâm, yêu thương.
ầm ầm|Tiếng động to, vang dội liên tiếp, như tiếng sấm hay sóng.
ấm cúng|Không khí gần gũi, thân mật và ấm áp, như trong gia đình.
âm điệu|Sự trầm bổng, nhịp nhàng của giọng nói hoặc bản nhạc.
âm lịch|Lịch tính ngày tháng theo mặt trăng, dùng để xác định Tết và ngày rằm.
ấm lòng|Cảm thấy được an ủi, vui vẻ nhờ được quan tâm.
âm lượng|Độ to nhỏ của âm thanh, như tiếng loa, tiếng ti vi.
âm nhạc|Nghệ thuật dùng âm thanh, giai điệu để thể hiện cảm xúc.
ấm no|Đủ ăn, đủ mặc, cuộc sống không thiếu thốn.
âm thanh|Những gì tai nghe được, như tiếng nói, tiếng nhạc, tiếng động.
âm thầm|Lặng lẽ, không để người khác biết hay chú ý.
ẩm thấp|Có nhiều hơi nước, thiếu nắng và không thoáng, nói về nơi ở.
ẩm thực|Các món ăn và cách ăn uống của một vùng hay một dân tộc.
ấm trà|Bình nhỏ có vòi để pha trà; cũng chỉ trà đã pha trong bình.
ẩm ướt|Có hơi nước, không khô ráo, hơi ướt.
ân cần|Quan tâm chu đáo, nhẹ nhàng và tận tình với người khác.
ẩn danh|Giấu tên, không cho người khác biết mình là ai.
ân hận|Tiếc nuối và day dứt vì đã làm điều không đúng.
ẩn hiện|Lúc thấy lúc không, khi rõ khi mờ.
ẩn náu|Trốn, giấu mình ở nơi kín đáo để không bị phát hiện.
ẩn nấp|Giấu mình sau vật che chắn để tránh bị phát hiện.
ẩn núp|Nấp vào chỗ kín đáo để không ai trông thấy.
ấn phẩm|Sách, báo, tạp chí hay tài liệu được in ra để phát hành.
ẩn số|Số chưa biết cần tìm trong bài toán; cũng chỉ điều còn bí ẩn.
ấn tượng|Cảm nhận, hình ảnh còn đọng lại trong tâm trí; cũng là gây chú ý mạnh.
ấp úng|Nói không nên lời, ngập ngừng vì lúng túng.
ấu thơ|Quãng thời gian còn bé, khi mới là đứa trẻ.
ba ba|Loài rùa sống ở nước ngọt, mai mềm, thịt ăn được.
ba chấm|Dấu câu gồm ba chấm liền nhau, cho biết ý còn bỏ lửng, chưa nói hết.
ba chỉ|Phần thịt lợn ở bụng, có lớp nạc và mỡ xen kẽ nhau.
bà chủ|Người phụ nữ làm chủ một cửa hàng, công ty hoặc gia đình.
ba chục|Số ba mươi, hay dùng khi đếm hàng hóa hoặc nói số tiền.
bà con|Người có quan hệ họ hàng; cũng chỉ người cùng xóm, cùng quê nói chung.
bà hoàng|Người phụ nữ thuộc hoàng tộc; nay hay chỉ người nữ nổi bật nhất trong một lĩnh vực.
bà lão|Người phụ nữ đã cao tuổi, tóc bạc.
ba lô|Túi lớn có hai quai để đeo trên lưng.
ba má|Cha và mẹ, cách gọi phổ biến ở miền Nam.
bà mối|Người phụ nữ đứng ra giới thiệu, se duyên để trai gái nên vợ chồng.
ba mươi|Số liền sau hai mươi chín; cũng chỉ ngày cuối cùng của năm âm lịch.
bà ngoại|Mẹ của mẹ mình.
bà nội|Mẹ của cha mình.
bá tước|Tước vị quý tộc ở châu Âu thời xưa, xếp dưới hầu tước.
bả vai|Phần xương dẹt ở phía sau vai, gần lưng.
bà xã|Cách người chồng gọi vợ mình một cách thân mật.
bạc hà|Cây rau thơm có lá vị the mát, dùng làm gia vị hoặc kẹo.
bác học|Nhà khoa học có kiến thức sâu rộng, nhiều phát minh.
bạch đàn|Cây thân gỗ cao thẳng, lá có mùi thơm, trồng nhiều để lấy gỗ.
bạch kim|Kim loại quý màu trắng bạc, rất bền, dùng làm trang sức.
bài bản|Có phương pháp, quy củ rõ ràng, làm đúng trình tự.
bãi biển|Dải cát ven biển, nơi tắm biển và vui chơi.
bài ca|Tác phẩm có lời để hát, thường mang ý ca ngợi hoặc trữ tình.
bãi cỏ|Khoảng đất rộng mọc đầy cỏ.
bài giải|Phần trình bày cách làm và đáp án của một bài toán, bài tập.
bài giảng|Nội dung thầy cô trình bày để dạy học sinh trong một buổi học.
bài hát|Tác phẩm âm nhạc gồm giai điệu và lời để hát.
bài học|Phần kiến thức được học trong một tiết; cũng chỉ kinh nghiệm rút ra từ thực tế.
bài làm|Phần viết, lời giải học sinh làm ra khi kiểm tra hoặc làm bài tập.
bãi lầy|Vùng đất trũng nhiều bùn nhão, đi vào dễ bị lún.
bài tập|Phần việc được giao để luyện tập kiến thức hoặc rèn luyện cơ thể.
bài thi|Phần làm của thí sinh trong kỳ thi để đánh giá kiến thức.
bài thơ|Tác phẩm văn học viết theo thể thơ, có vần và nhịp điệu.
bài toán|Đề toán yêu cầu tính toán, tìm lời giải; cũng chỉ vấn đề cần giải quyết.
bài văn|Phần viết hoàn chỉnh theo một đề tài, thường làm ở môn ngữ văn.
bài vở|Bài học và bài tập của học sinh nói chung.
bám sát|Theo thật sát, không để rời xa hoặc tách khỏi.
bàn ăn|Chiếc bàn dùng để bày thức ăn và ngồi ăn cơm.
bàn bạc|Cùng nhau trao đổi ý kiến để đi đến quyết định.
bạn bè|Những người bạn nói chung.
bán buôn|Hình thức bán hàng số lượng lớn cho người bán lẻ.
bàn cãi|Tranh luận qua lại, đưa ra ý kiến trái ngược nhau.
bàn chải|Dụng cụ có nhiều sợi lông cứng gắn trên cán, dùng để chải, cọ rửa.
bán chạy|Được nhiều người mua, nhanh hết hàng.
bàn chân|Phần cuối của chân, dùng để đứng và đi.
bản chất|Tính chất cốt lõi, vốn có bên trong của sự vật hay con người.
ban công|Phần sàn nhô ra ngoài tường nhà, có lan can bao quanh.
bàn cờ|Tấm có kẻ ô dùng để bày quân và chơi cờ.
bàn đá|Chiếc bàn làm bằng đá, thường đặt ngoài sân, vườn hoặc công viên.
bán đảo|Vùng đất có ba mặt giáp nước, một mặt nối với đất liền.
bàn đạp|Bộ phận để đặt chân đạp, như ở xe đạp; cũng chỉ chỗ dựa để tiến lên.
bán đắt|Bán với giá cao; cũng chỉ hàng bán chạy, có nhiều người mua.
ban đầu|Lúc mới bắt đầu, thời điểm đầu tiên của một việc.
ban đêm|Khoảng thời gian trời tối, từ lúc mặt trời lặn đến sáng hôm sau.
bản địa|Thuộc về chính vùng đất đó, có sẵn tại chỗ từ lâu.
bạn đọc|Người đọc sách, báo hay tác phẩm nào đó.
bản đồ|Hình vẽ thu nhỏ thể hiện đất đai, sông núi, đường sá của một vùng.
bạn đời|Người vợ hoặc chồng cùng chung sống cả đời.
bàn ghế|Đồ đạc gồm bàn và ghế nói chung.
bạn già|Người bạn thân lâu năm lúc về già; cũng chỉ vợ hoặc chồng khi đã có tuổi.
bàn giao|Giao lại công việc, tài sản cho người khác tiếp nhận và quản lý.
bàn giấy|Chiếc bàn dùng để ngồi viết, làm việc giấy tờ.
bản gốc|Phiên bản đầu tiên, dùng để sao chép ra các bản khác.
bán hàng|Đưa hàng cho khách và nhận tiền, công việc của người buôn bán.
bạn học|Người cùng học một lớp hoặc một trường.
bản in|Tài liệu được in ra từ máy in hoặc nhà in.
bán kết|Vòng đấu ngay trước trận chung kết.
bán kính|Đoạn thẳng nối tâm với một điểm trên đường tròn.
bàn là|Dụng cụ có đáy phẳng được làm nóng để là phẳng quần áo.
bản làng|Làng xóm của đồng bào dân tộc ở vùng núi, vùng cao.
bản lề|Bộ phận nối giúp cánh cửa đóng mở được; cũng chỉ thời điểm chuyển giao.
bàn luận|Trao đổi, nêu ý kiến về một vấn đề.
ban mai|Lúc sáng sớm, khi mặt trời vừa mọc.
ban nãy|Khoảng thời gian vừa mới qua, cách lúc đang nói không lâu.
bản năng|Khả năng tự nhiên có sẵn từ khi sinh ra, không cần học.
ban ngày|Khoảng thời gian có ánh mặt trời, từ sáng đến chiều tối.
bản nhạc|Một tác phẩm âm nhạc, có thể được ghi lại bằng nốt nhạc.
bản nháp|Phần viết thử ban đầu, còn sửa chữa trước khi hoàn chỉnh.
bàn phím|Bộ phận có nhiều phím để gõ chữ, số vào máy tính.
bản quyền|Quyền của tác giả đối với tác phẩm do mình làm ra.
bản sao|Giấy tờ chép hoặc chụp lại giống hệt bản gốc.
bản sắc|Nét đặc trưng riêng tạo nên sự khác biệt của một dân tộc, con người.
bàn tán|Nhiều người cùng nói, xôn xao về một chuyện.
bàn tay|Phần cuối của cánh tay, có năm ngón để cầm nắm.
bản thảo|Bài viết tay hoặc đánh máy của tác phẩm trước khi đem in.
bạn thân|Người bạn gần gũi, gắn bó và tin cậy nhất.
bản tin|Tập hợp tin tức ngắn được phát trên đài, tivi hoặc in ra.
bàn tính|Dụng cụ tính toán có hạt xâu trên que; cũng chỉ việc cùng bàn bạc, tính toán.
bàn tròn|Chiếc bàn có mặt tròn; cũng chỉ buổi thảo luận bình đẳng giữa nhiều người.
bán trú|Hình thức học sinh ở lại trường ăn và ngủ trưa, học cả ngày rồi mới về.
bàn ủi|Dụng cụ được làm nóng để là phẳng quần áo, cách gọi ở miền Nam.
bản vẽ|Hình vẽ thể hiện thiết kế của nhà cửa, máy móc.
bảng|Tấm phẳng để viết, dán thông báo; cũng chỉ hình kẻ ô ghi số liệu.
bảng đen|Tấm bảng màu đen hoặc xanh trong lớp học để viết phấn.
bảng hiệu|Tấm biển ghi tên cửa hàng, công ty treo trước cửa.
bảng màu|Tấm pha màu của họa sĩ; cũng chỉ tập hợp các màu được chọn dùng.
bảng vàng|Bảng ghi tên người thi đỗ hoặc có thành tích xuất sắc để vinh danh.
bánh|Món ăn làm từ bột với nhiều hình dạng, có thể hấp, nướng hoặc rán.
bánh bao|Bánh hấp làm bằng bột mì, vỏ trắng mềm, có nhân thịt.
bánh bèo|Bánh bột gạo hấp trong chén nhỏ, rắc tôm chấy, ăn với nước mắm.
bánh bò|Bánh hấp từ bột gạo ủ men với đường, mềm xốp, có nhiều lỗ nhỏ.
bánh canh|Món ăn nước có sợi bánh to và dai làm từ bột gạo hoặc bột lọc.
bánh chưng|Bánh vuông gói lá dong, nhân đậu xanh và thịt, làm vào dịp Tết.
bánh cuốn|Món bánh bột gạo tráng mỏng, hấp chín, cuộn nhân thịt băm và mộc nhĩ.
bánh dừa|Tên chung các loại bánh làm với cơm dừa hoặc nước cốt dừa, vị thơm béo.
bánh đa|Bánh tráng mỏng từ bột gạo, thường nướng giòn, có khi rắc vừng.
bánh đậu|Bánh làm từ đậu xanh nghiền mịn với đường, thường ăn kèm trà.
bánh đúc|Bánh làm từ bột gạo tẻ quấy với nước vôi trong, để nguội thành tảng mềm mịn.
bánh gối|Bánh vỏ bột mì gấp hình chiếc gối, nhân thịt băm, miến, mộc nhĩ, rán giòn.
bánh kem|Bánh xốp mềm phủ kem bên ngoài, thường dùng trong tiệc sinh nhật.
bánh kẹo|Đồ ăn ngọt gồm các loại bánh và kẹo nói chung.
bánh kẹp|Món bánh có nhân như thịt, rau kẹp giữa hai lớp bánh.
bánh khoai|Bánh làm từ khoai lang hoặc khoai mì, thường chiên hoặc hấp.
bánh ngọt|Các loại bánh có vị ngọt, thường làm từ bột mì, trứng, đường.
bánh nướng|Bánh được làm chín bằng cách nướng, nhất là loại bánh Trung thu.
bánh phồng|Bánh mỏng phơi khô, khi nướng hoặc chiên thì phồng to, giòn xốp.
bánh quẩy|Bánh bột mì chiên phồng, dài và rỗng ruột, hay ăn kèm phở hoặc cháo.
bánh quế|Bánh mỏng, giòn, thường cuộn tròn thành ống, có mùi thơm.
bánh rán|Bánh bột nếp rán vàng, có nhân đậu xanh, vỏ giòn.
bánh răng|Bộ phận hình tròn có răng, ăn khớp nhau để truyền chuyển động trong máy.
bánh sữa|Bánh làm chủ yếu từ sữa và đường, vị ngọt béo, mềm thơm.
bánh tét|Bánh nếp hình trụ dài gói lá chuối, nhân đậu xanh và thịt, phổ biến ở miền Nam dịp Tết.
bánh tôm|Bánh chiên giòn từ bột và khoai lang thái sợi, bên trên đặt con tôm, nổi tiếng ở Hà Nội.
bánh trái|Các loại bánh và hoa quả nói chung.
bánh tráng|Bánh mỏng làm từ bột gạo, phơi khô, dùng để cuốn hoặc nướng.
bánh trôi|Viên bột nếp nhỏ nhân đường phèn, luộc chín nổi lên, hay làm dịp Tết Hàn thực.
bánh xe|Bộ phận hình tròn quay quanh trục giúp xe di chuyển.
bánh xèo|Bánh bột gạo đổ mỏng trên chảo nóng, có nhân tôm, thịt, giá.
bánh xốp|Bánh nhẹ, giòn, có nhiều lớp mỏng xen lớp kem.
bảo ban|Chỉ bảo, khuyên dạy nhau những điều hay lẽ phải.
bao bì|Vỏ hộp, túi hoặc giấy dùng để đóng gói hàng hóa.
bao biện|Viện cớ, giải thích để che lấp lỗi của mình.
bao bọc|Bọc kín xung quanh; cũng chỉ che chở, chăm lo cho người khác.
bao bố|Bao lớn dệt bằng sợi đay hoặc sợi nhựa, dùng đựng gạo, lúa, hàng hóa.
bảo bối|Vật quý giá được giữ gìn cẩn thận; cũng chỉ món đồ thần kỳ.
báo cáo|Trình bày lại kết quả, tình hình công việc cho người khác biết.
bão cát|Gió mạnh cuốn theo nhiều cát bụi, thường có ở sa mạc.
báo chí|Các loại báo và tạp chí nói chung, nơi đưa tin tức.
báo danh|Đăng ký, khai tên để tham gia một kỳ thi hay sự kiện.
bao dung|Rộng lượng, dễ tha thứ và cảm thông với người khác.
bảo dưỡng|Kiểm tra, sửa chữa định kỳ để máy móc, xe cộ hoạt động tốt.
bảo đảm|Cam kết chắc chắn sẽ làm được hoặc giữ đúng lời.
báo động|Tín hiệu cảnh báo khẩn cấp khi có nguy hiểm sắp xảy ra.
báo giá|Đưa ra mức giá của hàng hóa hoặc dịch vụ để khách hàng tham khảo.
bao giờ|Khi nào, lúc nào; dùng để hỏi hoặc nói về thời gian.
bao gồm|Có chứa các phần bên trong, gộp lại thành một tổng thể.
bảo hành|Cam kết sửa chữa miễn phí sản phẩm hỏng trong thời gian nhất định.
bảo hiểm|Hình thức đóng tiền định kỳ để được hỗ trợ khi gặp rủi ro.
báo hiệu|Dùng dấu hiệu để cho biết trước điều gì sắp xảy ra.
bảo hộ|Che chở, giữ cho an toàn, như quần áo bảo hộ khi lao động.
bao la|Rộng lớn mênh mông, không nhìn thấy giới hạn.
bao lâu|Dùng để hỏi khoảng thời gian dài hay ngắn thế nào.
bảo mật|Giữ kín thông tin, không để người ngoài biết hoặc lấy được.
bảo mẫu|Người được thuê để trông nom, chăm sóc trẻ nhỏ.
bào mòn|Làm mòn dần đi do cọ xát, nước chảy hay thời gian.
bào ngư|Loài ốc biển có vỏ dẹt, thịt quý và đắt tiền.
bao nhiêu|Dùng để hỏi số lượng hoặc mức độ là mấy.
bao phủ|Che kín, trùm khắp lên bề mặt của một vùng.
bảo quản|Giữ gìn đồ vật, thực phẩm để không bị hư hỏng.
bao quanh|Vây kín xung quanh một vật hay một nơi.
bao quát|Nhìn hoặc nắm được toàn bộ, đầy đủ mọi mặt.
bao tải|Túi lớn đan bằng sợi dày, dùng để đựng gạo, thóc, hàng hóa.
bảo tàng|Nơi lưu giữ và trưng bày hiện vật có giá trị lịch sử, văn hóa.
bao tay|Đồ bằng vải, len hoặc cao su đeo vào để che kín bàn tay.
bảo thủ|Khư khư giữ ý cũ, không chịu thay đổi hay tiếp thu cái mới.
báo thức|Phát ra âm thanh để đánh thức người ngủ dậy đúng giờ.
báo tin|Thông báo cho người khác biết một tin tức mới.
bảo tồn|Giữ gìn, bảo vệ để không bị mất đi hay hư hại.
bảo trì|Kiểm tra, chăm sóc định kỳ để thiết bị luôn hoạt động tốt.
bảo trọng|Lời dặn hãy giữ gìn sức khỏe và bản thân, thường nói khi chia tay.
bảo trợ|Đứng ra đỡ đầu, giúp đỡ về tiền bạc hoặc tinh thần cho người hay tổ chức.
báo tuyết|Loài báo lông dày màu trắng xám, sống trên núi cao lạnh giá.
bao tử|Dạ dày, nơi chứa và tiêu hóa thức ăn; cũng chỉ rau quả còn rất non.
bảo vật|Đồ vật quý hiếm, có giá trị đặc biệt cần gìn giữ.
bảo vệ|Che chở, giữ cho an toàn; cũng chỉ người canh gác một nơi.
bao xa|Dùng để hỏi khoảng cách xa hay gần đến mức nào.
bát ăn|Chiếc bát dùng để đựng cơm, thức ăn khi ăn.
bạt ngàn|Rộng lớn, trải dài nối tiếp nhau đến tận xa.
bát ngát|Rộng lớn, trải dài tít tắp đến tận chân trời.
báu vật|Vật quý hiếm, có giá trị lớn được gìn giữ cẩn thận.
bày biện|Sắp xếp, trang trí đồ vật cho đẹp mắt.
bay bổng|Nhẹ nhàng như đang bay lên cao; thường nói về cảm xúc, trí tưởng tượng.
bay hơi|Chất lỏng chuyển dần thành hơi và tan vào không khí.
bay lượn|Chuyển động trên không trung, lượn vòng qua lại nhẹ nhàng.
bay màu|Bị phai, nhạt màu đi; cũng nói vui là biến mất hoặc bị xóa sạch.
bảy mươi|Số bằng bảy lần mười, đứng sau sáu mươi chín.
bay nhảy|Đi đây đi đó, hoạt động tự do, không chịu gò bó một chỗ.
bày tỏ|Nói ra cho người khác biết suy nghĩ, tình cảm của mình.
bày trò|Nghĩ ra trò chơi, việc làm mới lạ, đôi khi để nghịch ngợm.
bày vẽ|Làm thêm thứ cầu kỳ, không cần thiết; cũng là chỉ bảo cách làm.
bắc cầu|Xây cầu nối hai bên; cũng chỉ việc làm cầu nối giữa hai người, hai nơi.
băn khoăn|Còn lo nghĩ, phân vân chưa quyết định được.
bằng cấp|Giấy chứng nhận trình độ học vấn đã đạt được.
bằng chứng|Điều, vật dùng để chứng minh một sự việc là có thật.
băng dính|Dải băng mỏng có lớp keo, dùng để dán.
băng giá|Lạnh đến mức nước đóng băng; cũng chỉ thái độ lạnh nhạt.
bằng khen|Giấy khen của cơ quan, nhà trường tặng cho người có thành tích.
bằng không|Nếu không như vậy thì; cũng chỉ kết quả coi như số không, chẳng được gì.
bằng lăng|Cây thân gỗ cho hoa màu tím mọc thành chùm, nở rộ vào mùa hè.
bằng lòng|Đồng ý, chấp nhận; cũng chỉ cảm thấy hài lòng.
bằng nhau|Ngang nhau về số lượng, kích thước hay mức độ.
bằng phẳng|Phẳng đều, không lồi lõm; cũng chỉ cuộc sống êm ả, suôn sẻ.
băng tải|Thiết bị có dải băng chuyển động liên tục để chở hàng hóa, vật liệu.
băng tuyết|Nước đóng thành băng và tuyết phủ trắng khi trời rất lạnh.
bắp cải|Rau có lá cuộn tròn chặt thành bắp, ăn luộc hoặc xào.
bắp chân|Phần thịt nở nang ở phía sau cẳng chân.
bắp đùi|Phần cơ to khỏe ở đùi, phía trên đầu gối.
bắp ngô|Phần quả của cây ngô có nhiều hạt mọc quanh lõi.
bắp tay|Phần thịt nở nang ở cánh tay trên.
bắp thịt|Khối cơ trên cơ thể giúp cử động.
bắt bẻ|Soi mói, vạch lỗi nhỏ để chê trách hoặc làm khó.
bắt cá|Dùng lưới, cần câu hoặc tay để bắt cá dưới nước.
bắt chuyện|Chủ động nói chuyện, làm quen với ai đó.
bắt đầu|Khởi sự, làm bước đầu tiên của một việc.
bắt gặp|Tình cờ nhìn thấy hoặc gặp được.
bắt kịp|Đuổi theo cho bằng, theo kịp người hay việc đi trước.
bắt lấy|Chụp lấy, nắm chặt không để vuột mất.
bắt mắt|Đẹp, nổi bật, dễ thu hút ánh nhìn.
bắt mồi|Con vật rình và chộp lấy thức ăn của nó.
bắt nguồn|Khởi đầu, sinh ra từ một nơi hoặc một nguyên nhân nào đó.
bắt nhịp|Ra hiệu cho mọi người cùng hát đúng nhịp; cũng chỉ việc nhanh chóng hòa nhập.
bắt rễ|Rễ cây bám sâu và phát triển trong đất; cũng chỉ việc bắt đầu gắn bó, ăn sâu.
bắt tay|Nắm tay nhau để chào hỏi; cũng chỉ việc cùng hợp tác.
bậc cửa|Bậc thềm hoặc thanh gỗ chắn ngang ở chân cửa ra vào.
bậc thang|Từng bậc nối tiếp nhau để bước lên xuống; cũng chỉ ruộng bậc thang.
bậc thầy|Người giỏi nhất, rất tài năng trong một lĩnh vực.
bậc thềm|Những bậc đá hoặc gạch ở trước cửa nhà để bước lên.
bấm giờ|Dùng đồng hồ đo thời gian của một hoạt động.
bấm nút|Ấn ngón tay vào nút để điều khiển máy móc.
bẩm sinh|Có sẵn từ lúc mới sinh ra, không phải học.
bận bịu|Có nhiều việc phải làm, không lúc nào rảnh.
bận rộn|Nhiều việc liên tục, luôn chân luôn tay.
bận tâm|Lo nghĩ, để ý đến điều gì đó trong lòng.
bẩn thỉu|Dơ dáy, đầy vết bẩn, không sạch sẽ chút nào.
bâng quơ|Vu vơ, không có mục đích hay đối tượng rõ ràng.
bập bẹ|Nói chưa rõ, chưa sõi như trẻ mới tập nói.
bập bênh|Đồ chơi gồm tấm ván dài đặt trên trụ, hai bên lên xuống luân phiên.
bập bùng|Gợi tả ngọn lửa cháy chập chờn, lúc bùng lên lúc lụi xuống.
bất bình|Không hài lòng, bực tức trước điều sai trái.
bất cẩn|Không cẩn thận, thiếu chú ý nên dễ gây lỗi.
bất chấp|Không để ý, không quan tâm đến khó khăn hay ngăn cản.
bất chợt|Xảy ra thình lình, không báo trước.
bất công|Không công bằng, đối xử thiên vị.
bất cứ|Dùng để chỉ cái nào cũng được, không trừ trường hợp nào.
bật cười|Bất chợt cười thành tiếng vì thấy điều gì đó buồn cười.
bật đèn|Làm cho đèn sáng lên bằng công tắc.
bất động|Hoàn toàn đứng yên, không nhúc nhích.
bất kể|Không tính đến, không cần quan tâm điều kiện gì.
bật khóc|Khóc òa lên đột ngột, không kìm được.
bất lợi|Gây khó khăn, không có lợi cho mình.
bật lửa|Dụng cụ nhỏ cầm tay để tạo ngọn lửa.
bất ngờ|Xảy ra ngoài dự đoán, không ai nghĩ trước.
bất ổn|Không ổn định, có nhiều điều đáng lo.
bất thường|Khác với bình thường, không theo quy luật.
bất tiện|Không thuận lợi, gây phiền phức khi dùng hoặc làm.
bất tử|Tồn tại mãi mãi, không bao giờ mất đi; cũng chỉ được ghi nhớ mãi.
bầu bạn|Làm bạn, ở bên cạnh để chia sẻ cho đỡ cô đơn.
bầu bí|Cây bầu và cây bí nói chung; cũng là cách nói vui về việc mang thai.
bầu chọn|Bỏ phiếu để chọn ra người hoặc thứ mình thích.
bầu dục|Hình thuôn dài như quả trứng; cũng là quả thận động vật dùng làm món ăn.
bầu trời|Khoảng không rộng lớn phía trên mặt đất mà ta nhìn thấy.
bẫy chuột|Dụng cụ đặt mồi để bắt chuột trong nhà.
bây giờ|Thời điểm hiện tại, lúc đang nói.
bấy nhiêu|Số lượng hay mức độ đúng như đã nói đến.
be bé|Hơi nhỏ, có kích thước nhỏ nhắn dễ thương.
bé bỏng|Còn nhỏ bé, non nớt và đáng được yêu thương.
bé con|Cách gọi trìu mến một đứa trẻ nhỏ.
bẻ gãy|Dùng sức làm cho vật gãy rời ra; cũng chỉ việc làm cho thất bại hoàn toàn.
bẻ lái|Xoay tay lái để đổi hướng xe; cũng chỉ thay đổi ý định bất ngờ.
bé nhỏ|Nhỏ nhắn, có vóc dáng hoặc kích thước nhỏ.
béo bở|Mang lại nhiều lợi ích, dễ kiếm lời.
béo ngậy|Vị béo đậm, thơm ngon do có nhiều chất béo.
béo tốt|Mập mạp, khỏe mạnh, trông đầy đặn.
bể bơi|Hồ nước xây nhân tạo để mọi người bơi lội, tập bơi.
bế giảng|Kết thúc năm học hoặc khóa học, thường có buổi lễ tổng kết.
bề mặt|Lớp mặt ngoài cùng, phía trên của một vật.
bề ngang|Chiều rộng của một vật, đo theo hướng nằm ngang.
bề ngoài|Vẻ bên ngoài nhìn thấy được của người hay vật.
bệ phóng|Nơi đặt tên lửa để phóng lên; cũng chỉ nền tảng giúp phát triển.
bê tông|Vật liệu xây dựng trộn từ xi măng, cát, đá và nước, rất cứng khi khô.
bền bỉ|Kiên trì, dẻo dai, làm việc lâu dài không nản.
bến cảng|Nơi tàu biển lớn neo đậu, bốc dỡ hàng hóa.
bên cạnh|Ở sát ngay một bên; cũng có nghĩa là ngoài ra, thêm vào đó.
bền chặt|Gắn bó chắc chắn, khó bị chia cắt.
bên dưới|Ở phía thấp hơn so với một vật nào đó.
bến đò|Nơi đò đỗ để đưa khách qua sông.
bên kia|Phía đối diện, ở phía xa hơn so với mình.
bền lâu|Tồn tại hoặc giữ được trong thời gian dài.
bên lề|Ở phần rìa, mép ngoài; cũng chỉ những chuyện phụ, không chính thức.
bên ngoài|Phía ngoài của một vật hay một nơi; cũng chỉ vẻ bề ngoài.
bên nội|Gia đình, họ hàng phía bố, như ông bà nội, cô, chú, bác.
bến phà|Nơi phà đỗ để chở người và xe qua sông.
bến sông|Chỗ ven sông để thuyền đò neo đậu, người lên xuống.
bến tàu|Nơi tàu thuyền cập bờ để đón trả khách, chất dỡ hàng.
bên trên|Ở phía cao hơn so với một vật nào đó.
bên trong|Phía trong của một vật hay một nơi; cũng chỉ tâm tư, suy nghĩ.
bền vững|Vững chắc, tồn tại lâu dài, không dễ thay đổi.
bến xe|Nơi xe khách, xe buýt đỗ để đón và trả khách.
bênh|Đứng về phía ai đó để bảo vệ, nói đỡ.
bênh vực|Che chở, nói đỡ cho người bị chèn ép hoặc bị oan.
bếp lò|Chỗ đun nấu có lò, thường đốt bằng than hoặc củi.
bếp núc|Công việc nấu nướng trong nhà nói chung.
bí ẩn|Còn giấu kín, chưa ai biết rõ hay giải thích được.
bí bách|Ngột ngạt, tù túng, khó chịu vì không tìm được lối ra.
bí danh|Tên dùng thay cho tên thật để giữ kín danh tính.
bí đao|Quả dài, vỏ xanh có lớp phấn trắng, ruột trắng, thường nấu canh.
bí đỏ|Loại quả to, ruột vàng cam, vị ngọt bùi; còn gọi là bí ngô.
bị động|Bị chi phối, không chủ động được trong hành động.
bí hiểm|Khó hiểu, khó đoán, có vẻ chứa nhiều điều bí ẩn.
bí mật|Điều được giữ kín, không để người khác biết.
bí ngô|Quả to tròn, vỏ cứng, ruột vàng cam, dùng nấu canh hoặc làm bánh.
bi quan|Hay nghĩ về mặt xấu, không tin mọi việc sẽ tốt đẹp.
bí quyết|Cách làm riêng, hiệu quả mà ít người biết.
bịch|Túi nhỏ, thường bằng ni lông, để đựng đồ; cũng là tiếng vật nặng rơi xuống.
biển|Vùng nước mặn mênh mông; cũng chỉ tấm bảng ghi chữ, số như biển số xe.
biển báo|Tấm bảng có hình hoặc chữ đặt bên đường để chỉ dẫn, cảnh báo.
biển cả|Vùng nước mặn bao la, mênh mông không thấy bờ.
biến chuyển|Thay đổi dần từ trạng thái này sang trạng thái khác.
biến cố|Sự việc lớn xảy ra bất ngờ, gây thay đổi quan trọng.
biến dạng|Thay đổi, méo mó hình dạng so với lúc ban đầu.
biên dịch|Dịch văn bản từ ngôn ngữ này sang ngôn ngữ khác.
biến đổi|Thay đổi dần, trở nên khác so với trước.
biến động|Sự thay đổi mạnh, lên xuống thất thường của tình hình, giá cả.
biến hình|Thay đổi từ hình dạng này sang hình dạng khác.
biển khơi|Vùng biển xa bờ, rộng lớn và sâu thẳm.
biên lai|Giấy xác nhận đã nhận tiền hoặc nhận hàng.
biển lặng|Mặt biển yên ả, không có sóng to gió lớn.
biện minh|Đưa ra lý lẽ để giải thích, bào chữa cho việc làm của mình.
biện pháp|Cách làm cụ thể để giải quyết một vấn đề.
biên soạn|Thu thập tài liệu rồi viết, sắp xếp thành sách, giáo trình hay từ điển.
biên tập|Đọc, sửa chữa và hoàn thiện bài viết, sách báo trước khi phát hành.
biến thể|Một dạng khác đi ít nhiều so với dạng gốc ban đầu.
biết|Hiểu rõ, nắm được thông tin hoặc có khả năng làm một việc.
biết bao|Nhiều vô kể, dùng để nhấn mạnh mức độ hoặc cảm xúc.
biệt danh|Tên gọi riêng ngoài tên thật, thường do bạn bè đặt cho vui.
biết đâu|Có khi, có thể như vậy, dùng khi nói về khả năng chưa chắc chắn.
biết điều|Hiểu lẽ phải, cư xử đúng mực và hợp tình.
biết ơn|Ghi nhớ và trân trọng điều tốt người khác đã làm cho mình.
biệt tài|Tài năng đặc biệt, hơn hẳn người khác.
biết thế|Giá mà biết trước như vậy, dùng khi tiếc vì đã không làm khác đi.
biệt thự|Ngôi nhà riêng rộng rãi, đẹp, thường có sân vườn bao quanh.
biết ý|Hiểu được ý muốn của người khác mà không cần nói ra.
biếu|Tặng quà cho người trên để bày tỏ sự quý mến, kính trọng.
biểu cảm|Thể hiện cảm xúc qua nét mặt, giọng nói hoặc cử chỉ.
biểu diễn|Trình bày tiết mục nghệ thuật hay thể thao trước khán giả.
biểu đồ|Hình vẽ dùng cột, đường hoặc hình tròn để thể hiện số liệu.
biểu hiện|Điều thể hiện ra bên ngoài cho thấy tính chất, trạng thái bên trong.
biểu lộ|Để lộ ra, thể hiện tình cảm hay suy nghĩ ra bên ngoài.
biểu mẫu|Mẫu giấy tờ in sẵn các mục để người dùng điền thông tin vào.
biểu tượng|Hình ảnh, vật mang ý nghĩa đại diện cho một điều gì đó.
bình|Đồ đựng có thân phình, miệng nhỏ, như bình hoa, bình nước.
bình an|Yên ổn, mạnh khỏe, không gặp chuyện chẳng lành.
bình chọn|Xem xét rồi bầu, lựa chọn người hoặc thứ tốt nhất.
bình dân|Thuộc về người bình thường trong xã hội; cũng chỉ giá cả rẻ, hợp số đông.
bình đẳng|Mọi người ngang hàng nhau về quyền lợi và nghĩa vụ.
bình lặng|Yên ổn, êm đềm, không có biến động hay xáo trộn.
bình luận|Nêu ý kiến nhận xét, đánh giá về một sự việc.
bình minh|Lúc mặt trời mới mọc, bắt đầu một ngày mới.
bình quân|Mức tính chia đều cho mỗi người hoặc mỗi đơn vị, tức là trung bình.
bình tâm|Lấy lại sự yên tĩnh trong lòng, không còn rối bời.
bình thản|Điềm tĩnh, không lo lắng hay xao động.
bình thường|Không có gì đặc biệt, như mọi khi.
bình tĩnh|Giữ được thái độ điềm đạm, không hoảng hốt hay nóng vội.
bình trà|Đồ dùng có vòi và quai, dùng để pha và rót trà.
bình tưới|Bình có vòi dài, dùng để tưới nước cho cây.
bình xịt|Lọ chứa chất lỏng có nút bấm, phun ra thành tia hoặc màn sương.
bình yên|Êm ả, yên ổn, không có điều gì phiền muộn.
bịt mắt|Dùng khăn hay tay che kín mắt để không nhìn thấy gì.
bịt mũi|Dùng tay hay vật gì che kín mũi, thường để tránh mùi khó chịu.
bít tất|Đồ may bằng sợi mềm để mang ôm lấy bàn chân.
bĩu môi|Trề môi dưới ra để tỏ ý chê bai hoặc không bằng lòng.
bỏ bê|Không chăm lo, để mặc việc hay người mà mình phải quan tâm.
bó buộc|Gò bó, ràng buộc khiến không được tự do.
bỏ chạy|Vội vàng chạy đi khỏi chỗ đang ở, thường vì sợ hãi.
bỏ cuộc|Dừng lại giữa chừng, không cố gắng tiếp tục nữa.
bỏ đi|Rời khỏi một nơi; cũng là vứt bỏ thứ không còn dùng đến.
bỏ hoang|Để đất đai, nhà cửa không ai dùng hay chăm sóc trong thời gian dài.
bỏ học|Thôi hẳn việc đi học; cũng chỉ việc trốn, không đến lớp.
bỏ mặc|Không đoái hoài, để ai đó tự xoay xở một mình.
bọ ngựa|Côn trùng thân dài màu xanh, hai chân trước to khỏe như lưỡi liềm để bắt mồi.
bỏ phí|Để lãng phí, không dùng đến những thứ có ích như thời gian, tiền bạc.
bỏ qua|Không để ý tới, lướt qua; cũng là tha thứ, không chấp lỗi.
bỏ quên|Vô tình để lại đồ vật ở đâu đó mà không nhớ mang theo.
bọ rùa|Côn trùng nhỏ, lưng tròn khum, thường màu đỏ hoặc cam có chấm đen.
bò sát|Nhóm động vật có vảy, máu lạnh như rắn, thằn lằn, rùa.
bò sữa|Giống bò được nuôi chủ yếu để vắt lấy sữa.
bó tay|Đành chịu, không còn cách nào giải quyết.
bò tót|Loài bò rừng to lớn, lông sẫm màu, sống ở rừng núi.
bò tơ|Con bò còn non, thịt mềm và ngọt.
bỏ trống|Để một chỗ, một ô hay một vị trí không có ai hoặc không có gì.
bỏ túi|Cho vào túi, thu về cho mình; cũng chỉ thứ nhỏ gọn, mang theo dễ dàng.
bọ xít|Côn trùng hút nhựa cây, khi bị động vào thì tiết ra mùi hôi.
bói cá|Loài chim nhỏ có mỏ dài, lông xanh biếc, giỏi lao xuống nước bắt cá.
bòn bon|Loại quả mọc thành chùm, vỏ vàng nhạt, ruột trắng, vị ngọt hơi chua.
bon chen|Chen lấn, giành giật để được phần hơn hoặc kiếm lợi.
bọn chúng|Từ chỉ nhóm người được nói tới, thường mang ý xa cách hoặc không ưa.
bọn mình|Cách nói thân mật chỉ nhóm của mình, thường gồm cả người nghe.
bọn nó|Cách gọi suồng sã những người hoặc con vật đang được nhắc tới.
bọn ta|Cách người nói gọi nhóm của mình, giọng thân mật hoặc hơi kẻ cả.
bọn tớ|Cách nói thân mật chỉ nhóm của người nói, không gồm người nghe.
bóng|Quả tròn để chơi thể thao; cũng chỉ hình tối hiện ra khi vật che ánh sáng.
bóng bàn|Môn thể thao dùng vợt đánh quả bóng nhỏ qua lưới trên mặt bàn.
bóng bay|Quả bóng cao su mỏng bơm hơi, nhiều màu sắc, có thể bay lên cao.
bong bóng|Bọt khí tròn, mỏng nổi trên mặt nước; cũng chỉ quả bóng thổi để chơi.
bóng cây|Khoảng râm mát do tán cây che ánh nắng.
bóng chuyền|Môn thể thao hai đội dùng tay đánh bóng qua lưới căng cao.
bóng dáng|Hình dáng thấp thoáng của người hay vật từ xa.
bóng đá|Môn thể thao hai đội dùng chân đưa bóng vào khung thành đối phương.
bóng đèn|Vật bằng thủy tinh phát sáng khi có dòng điện, dùng để chiếu sáng.
bóng điện|Cách gọi khác của bóng đèn, vật phát sáng nhờ dòng điện.
bóng gió|Nói xa xôi, ám chỉ chứ không nói thẳng.
bóng loáng|Sáng bóng, láng mịn đến mức phản chiếu ánh sáng.
bóng mát|Chỗ râm mát được che khỏi ánh nắng.
bóng ném|Môn thể thao hai đội chuyền và ném bóng bằng tay vào khung thành.
bỏng ngô|Món ăn vặt làm từ hạt ngô rang nổ bung, giòn xốp.
bóng râm|Chỗ không có nắng chiếu vì bị vật che khuất.
bóng rổ|Môn thể thao hai đội ném bóng vào rổ treo trên cao.
bóng tối|Tình trạng thiếu ánh sáng, khắp nơi tối om.
bóng tròn|Cách gọi khác của môn bóng đá, đá quả bóng tròn vào khung thành.
boong|Phần sàn lộ thiên trên tàu thủy, nơi hành khách có thể đi lại, ngắm cảnh.
bóp còi|Ấn còi xe cho phát ra tiếng kêu để báo hiệu.
bóp méo|Làm cho biến dạng; cũng chỉ việc cố ý nói sai sự thật.
bọt biển|Miếng xốp mềm, hút nước tốt, dùng để rửa bát hay lau chùi.
bộ ba|Nhóm gồm ba người hoặc ba vật đi cùng nhau.
bộ cánh|Cách nói vui chỉ bộ quần áo đẹp, thường mặc để đi chơi, dự tiệc.
bồ cào|Nông cụ có cán dài và hàng răng thưa, dùng để cào cỏ, vun thóc.
bồ câu|Loài chim hiền, hay được nuôi, là biểu tượng của hòa bình.
bố chồng|Cha của chồng, gọi theo quan hệ của người vợ.
bố cục|Cách sắp xếp, phân chia các phần trong bài viết, bức tranh hay trang giấy.
bộ dạng|Vẻ bề ngoài, dáng điệu của một người ở lúc nào đó.
bổ dưỡng|Có nhiều chất tốt, giúp cơ thể khỏe mạnh.
bộ đàm|Máy liên lạc cầm tay, nói chuyện qua sóng vô tuyến trong phạm vi gần.
bộ đồ|Quần áo mặc cùng nhau thành một bộ, như đồ ngủ, đồ thể thao.
bố già|Cách gọi thân mật người cha đã lớn tuổi; cũng chỉ người có quyền thế, được nể sợ.
bổ ích|Mang lại lợi ích, có giá trị cho hiểu biết hay cuộc sống.
bộ lạc|Nhóm người sống chung, cùng tổ tiên và phong tục, thường thấy thời xa xưa.
bộ lông|Lớp lông phủ khắp thân con vật như chim, chó, mèo.
bộ máy|Hệ thống các bộ phận cùng phối hợp hoạt động, như bộ máy tiêu hóa.
bộ mặt|Khuôn mặt của một người; cũng chỉ diện mạo chung của một nơi.
bố mẹ|Cha và mẹ, hai người sinh ra và nuôi mình khôn lớn.
bộ môn|Một ngành, một môn riêng trong học tập, thể thao hay nghệ thuật.
bộ não|Cơ quan trong hộp sọ, điều khiển suy nghĩ và hoạt động của cơ thể.
bộ nhớ|Phần lưu trữ dữ liệu của máy tính, điện thoại; cũng chỉ khả năng ghi nhớ.
bồ nông|Loài chim nước lớn, mỏ dài có túi da dưới cằm để chứa cá.
bố nuôi|Người đàn ông nhận nuôi dưỡng, chăm sóc mình như con đẻ.
bộ óc|Khả năng suy nghĩ, trí thông minh của con người; cũng là bộ não.
bộ phận|Một phần của tổng thể như máy móc, cơ thể hay cơ quan.
bộ tộc|Cộng đồng gồm nhiều thị tộc cùng tiếng nói, phong tục, sống chung một vùng.
bố trí|Sắp xếp người, đồ vật hay công việc vào chỗ thích hợp.
bố vợ|Cha của vợ, theo cách gọi của người chồng.
bốc đồng|Hành động theo cảm xúc nhất thời, không suy nghĩ kỹ.
bốc hơi|Chất lỏng chuyển dần thành hơi bay lên; cũng chỉ biến mất nhanh không dấu vết.
bộc lộ|Để lộ ra cảm xúc, suy nghĩ hay tính cách vốn giấu kín.
bồi bàn|Người phục vụ khách ăn uống ở nhà hàng, quán ăn.
bồi bổ|Ăn uống, nghỉ ngơi để cơ thể khỏe mạnh, có thêm sức.
bối cảnh|Hoàn cảnh, khung cảnh chung nơi một sự việc hay câu chuyện diễn ra.
bồi dưỡng|Ăn uống thêm cho khỏe; cũng là dạy thêm để nâng cao kiến thức, tay nghề.
bồi đắp|Đắp thêm dần cho dày, cho vững; cũng là vun đắp, nuôi dưỡng tình cảm, kiến thức.
bôi đen|Tô cho đen đi; cũng chỉ thao tác chọn một đoạn chữ trên máy tính.
bồi hồi|Cảm giác xúc động, xao xuyến khi nhớ lại điều gì.
bối rối|Lúng túng, không biết nên làm gì hay nói gì.
bội thu|Thu hoạch được nhiều hơn hẳn so với bình thường.
bồi thường|Trả tiền hoặc đền bù cho người bị thiệt hại do mình gây ra.
bộn bề|Nhiều và ngổn ngang, chồng chất, khó giải quyết hết.
bồn chồn|Trong lòng lo lắng, không yên, như đang chờ đợi điều gì.
bốn mùa|Xuân, hạ, thu, đông; cũng có nghĩa là quanh năm, lúc nào cũng vậy.
bốn mươi|Số đếm bằng bốn lần mười, viết là 40.
bổn phận|Điều mình có trách nhiệm phải làm, như con cái đối với cha mẹ.
bốn phương|Khắp mọi nơi, mọi hướng đông, tây, nam, bắc.
bồn tắm|Vật dụng lớn, lòng sâu trong phòng tắm, chứa nước để nằm ngâm mình.
bồng bềnh|Trôi nổi nhẹ nhàng trên mặt nước hay trong gió; cũng chỉ tóc phồng mềm.
bồng bột|Hăng hái nhất thời, hành động theo cảm xúc, thiếu chín chắn.
bông cải|Rau có phần hoa kết thành chùm to, màu trắng hoặc xanh.
bỗng chốc|Trong khoảnh khắc rất ngắn, đột ngột, không ai lường trước.
bỗng dưng|Tự nhiên xảy ra mà không có lý do hay báo trước.
bông gòn|Sợi bông trắng mềm, dùng để lau, thấm hoặc nhồi gối.
bông hoa|Phần nở ra từ nụ của cây, thường có màu sắc và hương thơm.
bỗng nhiên|Một cách đột ngột, bất ngờ, không ai lường trước được.
bông tai|Đồ trang sức nhỏ xinh đeo ở tai.
bột giặt|Chất tẩy dạng bột, hòa vào nước để giặt sạch quần áo.
bột giấy|Nguyên liệu dạng bột nhão làm từ gỗ, tre, nứa, dùng để sản xuất giấy.
bột lọc|Bột tinh lấy từ củ sắn, khi nấu chín thì trong và dai.
bột nếp|Bột xay từ gạo nếp, nấu chín thì dẻo, dùng làm bánh trôi, bánh chay.
bột ngọt|Gia vị dạng hạt trắng làm món ăn ngọt đậm, còn gọi là mì chính.
bột sắn|Bột làm từ củ sắn, dùng để làm bánh, nấu chè hoặc tạo độ sánh.
bờ biển|Dải đất nơi đất liền tiếp giáp với biển.
bờ đê|Dải đất đắp cao chạy dọc sông để ngăn nước lũ, thường có lối đi trên mặt.
bỡ ngỡ|Ngơ ngác, lúng túng vì còn lạ lẫm, chưa quen.
bờ tường|Bức tường xây quanh nhà, sân vườn hoặc dọc theo lối đi.
bơi ếch|Kiểu bơi sấp, tay và chân co duỗi nhịp nhàng giống con ếch.
bởi lẽ|Từ dùng để nêu nguyên nhân, lý do của điều vừa nói.
bơi lội|Di chuyển trong nước bằng tay chân, vừa là thể thao vừa là vui chơi.
bơi ngửa|Kiểu bơi nằm ngửa trên mặt nước, quạt tay ra sau.
bơi thuyền|Dùng mái chèo khua nước để đẩy thuyền đi tới.
bởi vậy|Từ nối dùng để nêu kết quả, nghĩa là vì thế, cho nên.
bụ bẫm|Béo tròn, da thịt căng mịn và khỏe mạnh, thường nói về trẻ nhỏ.
bù đắp|Đền lại, bổ sung cho những thiếu thốn, mất mát.
bù lại|Đắp vào phần còn thiếu; cũng dùng khi nêu mặt tốt bù cho mặt chưa tốt.
bù nhìn|Hình người giả bằng rơm cắm ngoài đồng để đuổi chim.
bù xù|Tóc hoặc lông rối tung, xù lên, không gọn gàng.
búa tạ|Chiếc búa rất to và nặng, dùng để đập vật cứng.
bụi bặm|Có nhiều bụi bẩn bám vào; cũng chỉ vẻ ngoài phong trần, phóng khoáng.
bụi hồng|Khóm cây hoa hồng mọc sum suê thành bụi.
bụi rậm|Đám cây thấp mọc dày, chen chúc nhau.
búi tóc|Tóc được vấn gọn thành nút tròn trên đầu hoặc sau gáy.
bún bò|Món bún nước dùng ninh từ xương bò, có thịt bò, chả, nổi tiếng nhất là bún bò Huế.
bún chả|Món bún ăn với chả thịt lợn nướng và nước mắm chua ngọt, đặc sản Hà Nội.
bùn lầy|Đất ướt nhão, lầy lội, dễ lún chân.
bủn xỉn|Keo kiệt, tính toán chi li, tiếc từng chút tiền của.
bụng|Phần cơ thể giữa ngực và hông, chứa dạ dày, ruột; cũng chỉ lòng dạ, suy nghĩ.
bùng cháy|Lửa bốc lên mạnh mẽ; cũng chỉ cảm xúc dâng trào.
bụng dạ|Tấm lòng, tính tình của một người; cũng chỉ bộ máy tiêu hóa.
buổi chiều|Khoảng thời gian từ quá trưa đến lúc mặt trời lặn.
buổi sáng|Khoảng thời gian từ lúc trời sáng đến trước buổi trưa.
buổi sớm|Khoảng thời gian đầu ngày, lúc trời vừa sáng.
buổi tối|Khoảng thời gian từ khi trời tối đến lúc đi ngủ.
buổi trưa|Khoảng thời gian giữa ngày, lúc mặt trời lên cao nhất.
buồn|Cảm thấy không vui, lòng nặng trĩu vì điều gì đó.
buồn bã|Cảm thấy buồn nhiều, lộ rõ qua nét mặt và dáng vẻ.
buôn bán|Mua hàng rồi bán lại để kiếm lời.
buồn buồn|Hơi buồn, có chút buồn nhẹ thoáng qua trong lòng.
buồn bực|Vừa không vui vừa bực bội, khó chịu trong lòng.
buồn cười|Gây cảm giác muốn cười vì ngộ nghĩnh, hài hước.
buồn lòng|Không vui trong lòng, thường vì ai đó làm mình phật ý.
buồn ngủ|Cảm thấy mệt, mắt díp lại, muốn được ngủ.
buồn phiền|Lòng nặng trĩu, lo nghĩ vì những chuyện không vui.
buồn rầu|Mang tâm trạng ủ rũ, không vui kéo dài.
buồn tẻ|Đơn điệu, nhạt nhẽo, không có gì thú vị.
buồn thiu|Buồn rầu hiện rõ trên nét mặt, trông ủ rũ.
buồng|Phòng nhỏ trong nhà; cũng chỉ chùm quả lớn như buồng chuối.
buồng lái|Khoang dành cho người điều khiển máy bay, tàu hoặc xe.
buông tay|Thả tay ra, không nắm giữ nữa; cũng chỉ việc từ bỏ, thôi cố gắng.
búp bê|Đồ chơi hình em bé hoặc cô gái nhỏ xinh.
bút bi|Loại bút có viên bi nhỏ ở đầu ngòi để ra mực.
bút chì|Bút có lõi than chì, viết được và tẩy được.
bút dạ|Bút có ngòi bằng dạ hoặc sợi xốp thấm mực, nét viết to và đậm.
bút danh|Tên mà nhà văn, nhà báo dùng khi viết thay cho tên thật.
bút lông|Loại bút có đầu làm bằng lông, dùng để viết thư pháp hay vẽ.
bút máy|Loại bút có ngòi kim loại, bơm mực vào ống bên trong để viết.
bữa ăn|Lần ăn uống vào một thời điểm trong ngày như sáng, trưa, tối.
bừa bãi|Lộn xộn, không ngăn nắp; cũng chỉ làm tùy tiện, không theo quy định.
bừa bộn|Đồ đạc vương vãi lung tung, không gọn gàng.
bữa chính|Bữa ăn quan trọng trong ngày như bữa trưa, bữa tối, có đủ món.
bữa cơm|Lần ăn cơm trong ngày, thường cả nhà quây quần cùng ăn.
bữa tiệc|Buổi ăn uống vui vẻ có nhiều khách, thường để mừng một dịp đặc biệt.
bực bội|Khó chịu, bứt rứt trong lòng vì điều không vừa ý.
bực dọc|Khó chịu, cáu gắt, lộ rõ qua lời nói và nét mặt.
bực mình|Cảm thấy khó chịu, không vui vì việc trái ý.
bực tức|Khó chịu và tức giận vì điều trái ý hoặc bất công.
bức xạ|Năng lượng phát ra và lan truyền dưới dạng tia, sóng, như ánh sáng mặt trời.
bước|Nhấc chân di chuyển tới hoặc lui; cũng chỉ từng giai đoạn của một việc.
bước chân|Sự nhấc chân lên đặt xuống khi đi; cũng chỉ hành trình của một người.
bước đầu|Giai đoạn mở đầu, những việc làm đầu tiên.
bước đi|Cách đi từng bước; cũng chỉ hành động, quyết định trong một việc.
bước qua|Nhấc chân vượt sang bên kia; cũng chỉ vượt qua một giai đoạn.
bước ra|Đi từ trong ra ngoài, rời khỏi một nơi.
bước sóng|Khoảng cách giữa hai đỉnh sóng liền nhau, một khái niệm trong vật lý.
bước tiến|Sự tiến bộ, phát triển hơn so với trước.
bước vào|Đi vào bên trong; cũng chỉ bắt đầu một giai đoạn mới.
bướm|Côn trùng có hai đôi cánh mỏng, nhiều màu sắc, hay bay quanh hoa.
bươm bướm|Tên gọi khác của con bướm, côn trùng có cánh mỏng nhiều màu sắc.
bướng bỉnh|Cứng đầu, không chịu nghe lời người khác.
bưu điện|Nơi nhận gửi thư từ, hàng hóa và chuyển tiền.
bưu kiện|Gói hàng được gửi qua đường bưu điện.
bưu thiếp|Tấm thiếp có hình ảnh, dùng để viết lời chúc gửi đi.
cá biệt|Riêng lẻ, khác hẳn số đông; cũng chỉ học sinh hay vi phạm, khó bảo.
cá bống|Loài cá nhỏ sống ở nước ngọt, đầu to, thường kho ăn.
cá chép|Loài cá nước ngọt vảy to, hay được thả vào dịp tiễn ông Táo.
cá chiên|Món cá rán vàng giòn trong dầu mỡ.
cá chim|Loài cá biển thân dẹt hình thoi, thịt trắng, thơm ngon.
cá chình|Loài cá thân dài như rắn, da trơn, thịt béo ngon.
cà chua|Quả mọng màu đỏ, vị chua nhẹ, dùng nấu canh hoặc làm nước sốt.
cá chuồn|Loài cá biển có vây ngực dài như cánh, có thể bay lướt trên mặt nước.
cá cơm|Loài cá biển nhỏ, thân dài, thường dùng làm nước mắm hoặc phơi khô.
ca dao|Những câu thơ dân gian truyền miệng, thường theo thể lục bát.
cá đồng|Các loại cá sống tự nhiên ở ruộng, ao, mương.
cá đuối|Loài cá biển thân dẹt, rộng như cánh, đuôi dài.
ca hát|Cất tiếng hát để vui chơi hoặc biểu diễn.
cá heo|Thú sống dưới biển, thông minh, thân trơn, hay bơi theo đàn.
cá hồi|Loài cá thịt màu cam hồng, giàu dinh dưỡng, sống ở vùng nước lạnh.
cá hộp|Món cá chế biến sẵn, đóng trong hộp kín để bảo quản lâu.
cà kheo|Đôi gậy dài có chỗ đặt chân, giúp người đứng lên đi cao hơn mặt đất.
cá kho|Món cá nấu với nước mắm, đường cho đến khi thấm, sánh lại.
ca khúc|Bài hát có lời và giai điệu do nhạc sĩ sáng tác.
cá kiếm|Loài cá biển lớn có mỏ dài và nhọn như thanh kiếm.
cá lóc|Cá nước ngọt thân dài, đầu dẹt, thịt chắc, miền Bắc gọi là cá quả.
cá mập|Loài cá biển lớn, hàm răng sắc, bơi rất nhanh.
cá mè|Loài cá nước ngọt thân dẹt, vảy trắng bạc, nhiều xương.
cá mòi|Loài cá biển nhỏ, thường đóng hộp với sốt cà chua.
cá mú|Loài cá biển thân to, thịt trắng chắc, giá khá cao.
ca múa|Hát và múa, nói chung về biểu diễn văn nghệ.
cả nghĩ|Hay suy nghĩ nhiều, để tâm cả những chuyện nhỏ nhặt.
ca ngợi|Nói hoặc viết lời khen tặng điều tốt đẹp của ai, việc gì.
cá ngừ|Loài cá biển lớn, thịt đỏ, thường làm món nướng hoặc đóng hộp.
cá ngựa|Sinh vật biển nhỏ có đầu giống đầu ngựa, bơi đứng.
ca nhạc|Hát và chơi nhạc nói chung, thường là chương trình biểu diễn.
cá nhân|Một người riêng lẻ; cũng chỉ những gì thuộc về riêng mỗi người.
cá nóc|Loài cá biết phồng tròn mình như quả bóng, có chất độc nguy hiểm.
ca nô|Xuồng nhỏ chạy bằng động cơ, đi nhanh trên sông, biển.
cá nục|Cá biển nhỏ thân tròn, thịt chắc, giá rẻ, hay đem kho hoặc chiên.
cà phê|Thức uống pha từ hạt cà phê rang xay, vị đắng, thơm.
cá rô|Loài cá đồng nhỏ, vảy cứng, thịt thơm, hay nấu canh.
cà rốt|Củ dài màu cam, vị ngọt, ăn sống hay nấu chín đều được.
cá sấu|Loài bò sát lớn sống ở sông, đầm, da dày, miệng dài nhiều răng.
cá tầm|Cá nước lạnh cỡ lớn, thân dài, lưng có hàng vảy xương cứng, trứng rất quý.
cá thể|Từng con vật, cây cối hay con người riêng lẻ trong một loài hoặc một nhóm.
cá thu|Loài cá biển thịt chắc, ít xương, thường chiên hoặc kho.
cà tím|Quả dài vỏ màu tím, ruột trắng mềm, thường nướng hoặc xào.
cả tin|Dễ tin người nên hay bị lừa.
cá tính|Nét tính cách riêng, nổi bật của mỗi người.
cá tra|Loài cá da trơn nuôi nhiều ở miền Tây, thịt trắng, xuất khẩu nhiều.
cá trê|Loài cá da trơn, có râu, sống ở ao, ruộng.
cá trích|Loài cá biển nhỏ, thân dẹt, thường muối hoặc đóng hộp.
cá tuyết|Loài cá sống ở biển lạnh, thịt trắng, mềm, giàu dinh dưỡng.
ca từ|Phần lời được viết cho một bài hát.
cá vàng|Loài cá cảnh nhỏ màu vàng cam, thường nuôi trong bể kính.
cá voi|Loài thú lớn nhất sống dưới biển, thở bằng phổi.
cá vược|Cá thân dài, miệng rộng, thịt trắng ngọt, sống ở vùng nước lợ và biển.
cách|Lối, phương pháp để làm một việc; cũng chỉ khoảng xa giữa hai nơi.
cách âm|Ngăn tiếng ồn từ bên ngoài lọt vào hoặc từ trong lọt ra.
cách biệt|Xa cách, tách rời, ít có liên hệ với nhau.
cách điện|Ngăn không cho dòng điện truyền qua, như lớp vỏ nhựa bọc dây điện.
cách nhiệt|Ngăn không cho hơi nóng, hơi lạnh truyền qua.
cách thức|Phương pháp, trình tự để thực hiện một việc.
cách xa|Có khoảng cách lớn, ở xa nhau.
cải bắp|Loại rau có lá cuộn tròn thành bắp to.
cãi cọ|Tranh cãi qua lại với nhau, thường vì những chuyện nhỏ nhặt.
cài đặt|Đưa phần mềm vào máy hoặc thiết lập các thông số để dùng.
cái gì|Từ dùng để hỏi về một sự vật hay sự việc chưa biết.
cãi lộn|Lời qua tiếng lại to tiếng, gay gắt với nhau.
cải lương|Loại hình sân khấu ca kịch của miền Nam, nổi bật với điệu vọng cổ.
cãi nhau|Tranh luận gay gắt vì không đồng ý với nhau.
cải thiện|Làm cho tình hình, chất lượng tốt hơn trước.
cải tiến|Sửa đổi để công cụ, cách làm trở nên tốt hơn.
cãi vã|Lời qua tiếng lại gay gắt, to tiếng giữa hai hay nhiều người.
cải xoong|Rau thân mềm, lá nhỏ tròn, vị hơi hăng, hay xào, nấu canh hoặc ăn lẩu.
cạm bẫy|Đồ đặt sẵn để bắt thú; cũng chỉ mưu mẹo, cám dỗ dễ khiến người ta sa vào.
cảm biến|Bộ phận nhận biết ánh sáng, nhiệt độ, chuyển động rồi báo cho máy.
cám dỗ|Lôi kéo người khác làm điều không nên bằng thứ hấp dẫn.
cam đoan|Khẳng định chắc chắn điều mình nói là đúng và chịu trách nhiệm.
cảm động|Xúc động mạnh trong lòng trước một việc làm hay câu chuyện.
cảm giác|Điều ta cảm nhận được qua giác quan hoặc trong lòng.
cảm hứng|Sự hứng thú, động lực thôi thúc sáng tạo hay làm việc.
cam kết|Hứa chắc chắn sẽ làm, thường có giấy tờ hoặc lời xác nhận rõ ràng.
cảm kích|Xúc động và biết ơn trước việc tốt của người khác.
cảm mến|Có tình cảm quý mến, thiện cảm với ai đó.
cảm nghĩ|Những cảm xúc và suy nghĩ nảy ra trước một sự việc.
cảm nhận|Nhận biết bằng giác quan hay bằng tình cảm của mình.
cảm phục|Khâm phục, xúc động trước tài năng hay đức tính của ai.
cam quýt|Các loại quả có múi như cam, quýt nói chung.
cảm thấy|Nhận ra trong người hoặc trong lòng một điều gì đó.
cảm thông|Hiểu và chia sẻ với hoàn cảnh, cảm xúc của người khác.
cảm tình|Tình cảm quý mến, có thiện ý với ai đó.
cảm tưởng|Suy nghĩ, cảm nhận nảy ra sau khi trải qua việc gì.
cảm ứng|Khả năng nhận biết và phản ứng khi được chạm, như màn hình điện thoại.
cảm xúc|Những rung động trong lòng như vui, buồn, thương, giận.
camera|Thiết bị ghi hình, quay phim, như máy quay an ninh hoặc trên điện thoại.
can đảm|Không sợ khó khăn, nguy hiểm, dám đối mặt.
cạn kiệt|Bị dùng đến hết sạch, không còn lại gì.
can ngăn|Khuyên bảo để ngăn người khác làm điều không nên.
can thiệp|Tham gia vào việc của người khác để tác động, thay đổi kết quả.
cản trở|Gây khó khăn, ngăn không cho tiến lên hay làm được.
cảng|Nơi tàu thuyền ra vào, neo đậu và bốc dỡ hàng.
càng cua|Đôi chân to có kẹp ở phía trước của con cua.
canh|Món ăn nhiều nước nấu với rau, thịt hoặc cá; cũng là trông chừng, giữ gìn.
cảnh báo|Báo trước điều nguy hiểm để mọi người đề phòng.
cạnh bên|Ở ngay sát bên, gần kề.
cánh buồm|Tấm vải lớn căng trên cột thuyền để hứng gió.
canh cải|Món canh nấu với rau cải, thường thêm thịt băm hoặc tôm.
cánh cửa|Tấm gỗ, kính hay sắt đóng mở được ở lối ra vào.
cánh diều|Chiếc diều bay lơ lửng trên trời, hình ảnh quen thuộc của tuổi thơ.
cánh đồng|Khoảng đất rộng lớn dùng để trồng lúa, hoa màu.
cánh gà|Phần cánh con gà, làm món ăn; cũng chỉ hai bên khuất sân khấu.
cảnh giác|Luôn chú ý đề phòng điều xấu có thể xảy ra.
canh giữ|Trông coi, bảo vệ cẩn thận một nơi hay một vật.
cánh hoa|Từng mảnh mỏng, nhiều màu tạo nên bông hoa.
cành lá|Cành cây cùng lá trên đó, nói chung.
cảnh quan|Toàn bộ quang cảnh thiên nhiên hoặc phố xá của một nơi.
cánh quạt|Bộ phận xoay tròn của quạt, máy bay hay tàu, tạo ra luồng gió.
cánh rừng|Khu rừng rộng lớn với nhiều cây cối.
canh tác|Làm đất, trồng trọt và chăm sóc cây trồng.
cánh tay|Phần cơ thể từ vai đến bàn tay.
cạnh tranh|Ganh đua với nhau để giành phần hơn.
cảnh tượng|Hình ảnh, quang cảnh đang diễn ra trước mắt.
cảnh vật|Cây cối, nhà cửa, núi sông nhìn thấy ở một nơi.
cao áp|Có điện áp hoặc áp suất cao, như đường dây cao áp, đèn cao áp.
cao bồi|Người chăn bò cưỡi ngựa ở miền Tây nước Mỹ, đội mũ rộng vành.
cào cào|Côn trùng thân dài màu xanh, chân sau khỏe, hay nhảy trên cỏ.
cao cấp|Thuộc loại tốt nhất, chất lượng cao, thường giá đắt.
cao đẳng|Bậc học sau phổ thông, thời gian học ngắn hơn đại học.
cạo đầu|Làm sạch hết tóc trên đầu bằng dao cạo.
cao điểm|Lúc đông đúc, bận rộn nhất; cũng là điểm đất cao trên địa hình.
cao độ|Độ cao của một điểm hay của âm thanh; cũng chỉ mức rất cao.
cao giá|Có giá bán hoặc giá trị cao; cũng chỉ người tỏ ra kiêu kỳ, khó tiếp cận.
cao hứng|Đang vui, hứng khởi nên bất chợt muốn làm hay nói điều gì.
cao kều|Dáng người cao và gầy, trông lêu nghêu.
cao lớn|Có dáng người to và cao hơn bình thường.
cao nguyên|Vùng đất rộng, khá bằng phẳng, nằm ở trên cao.
cao ốc|Tòa nhà nhiều tầng, cao lớn ở thành phố.
cao ráo|Dáng người cao, thon gọn, ưa nhìn; cũng nói chỗ đất cao, khô thoáng.
cao siêu|Rất cao xa, sâu sắc, khó hiểu với người thường.
cao su|Chất dẻo co giãn tốt, làm từ mủ cây, dùng làm lốp xe, dép.
cao tay|Giỏi giang, khéo léo, hơn người trong cách xử lý việc.
cao tầng|Có nhiều tầng, thường nói về tòa nhà lớn ở thành phố.
cao thủ|Người rất giỏi, tài nghệ hơn hẳn trong một lĩnh vực.
cao thượng|Có tâm hồn và cách cư xử tốt đẹp, vượt lên sự nhỏ nhen.
cao tốc|Tốc độ cao; thường chỉ con đường rộng cho xe chạy nhanh, không giao cắt.
cao trào|Lúc sự việc, cảm xúc lên đến mức mạnh mẽ, căng thẳng nhất.
cạo trọc|Cạo sạch hết tóc trên đầu.
cao tuổi|Đã sống nhiều năm, thuộc lớp người già.
cao vút|Rất cao, vươn thẳng lên trời; cũng tả giọng hát lên rất cao.
cáp điện|Dây dẫn điện gồm nhiều sợi, có vỏ bọc cách điện chắc chắn.
cáp quang|Dây cáp truyền tín hiệu bằng ánh sáng, dùng cho mạng tốc độ cao.
cáp treo|Toa nhỏ chạy trên dây cáp, chở khách lên núi hay qua sông.
cát bụi|Những hạt cát và bụi nhỏ bay theo gió.
cát vàng|Loại cát màu vàng óng, thường có ở bãi biển, lòng sông.
cau có|Nét mặt nhăn nhó, khó chịu, tỏ vẻ bực bội.
cáu gắt|Bực bội và nói năng nặng lời với người khác.
cáu kỉnh|Hay bực tức, khó chịu vì những chuyện nhỏ.
cau mày|Nhíu hai lông mày lại vì khó chịu hoặc suy nghĩ.
càu nhàu|Nói lẩm bẩm tỏ ý bực bội, không bằng lòng.
cày bừa|Làm đất bằng cày và bừa trước khi gieo trồng; chỉ chung việc đồng áng.
cày cấy|Làm ruộng, cày đất và cấy lúa.
cay mắt|Mắt thấy xót, rát, muốn chảy nước vì khói, hành hoặc vì xúc động.
cặm cụi|Chăm chú, miệt mài làm việc một mình.
cắm trại|Dựng lều để ở và vui chơi ngoài trời.
căn bản|Phần nền tảng, quan trọng nhất làm gốc cho mọi thứ.
cằn cỗi|Đất khô xấu, cây cối khó mọc; cũng chỉ sự khô khan, thiếu sức sống.
căn cước|Thông tin để nhận dạng một người, ghi trên thẻ do nhà nước cấp.
căn dặn|Dặn dò kỹ lưỡng để người khác nhớ và làm theo.
căn hộ|Phần nhà riêng cho một gia đình trong tòa chung cư.
căn lều|Chỗ ở tạm làm bằng vải bạt hoặc tre lá.
cắn môi|Dùng răng cắn nhẹ vào môi, thường khi lo lắng hoặc cố nhịn.
căn nhà|Ngôi nhà để một gia đình sinh sống.
cằn nhằn|Nói đi nói lại tỏ ý không hài lòng, khó chịu.
căng buồm|Kéo buồm lên cho căng gió để thuyền ra khơi.
cẳng chân|Phần chân từ đầu gối xuống bàn chân.
căng mọng|Đầy nước, căng tròn và bóng, như quả chín hay đôi môi.
căng thẳng|Trạng thái lo lắng, áp lực, không thoải mái.
cặp đôi|Hai người đi cùng nhau thành một đôi, thường là người yêu.
cặp sách|Túi hoặc cặp đựng sách vở mang đến trường.
cặp tóc|Đồ dùng nhỏ để kẹp giữ tóc cho gọn.
cắt bỏ|Loại đi, bỏ hẳn phần thừa hoặc không cần thiết.
cắt bớt|Bỏ đi một phần cho ngắn hoặc ít lại.
cắt cỏ|Xén cỏ cho ngắn và gọn gàng.
cắt đứt|Làm đứt hẳn; cũng chỉ việc chấm dứt một mối quan hệ.
cắt giảm|Bớt đi, làm giảm số lượng hoặc chi phí.
cắt lời|Ngắt ngang khi người khác đang nói.
cắt ngang|Đi xuyên qua theo chiều ngang; cũng là chen vào làm gián đoạn lời nói.
cắt ngắn|Làm cho ngắn hơn, như tóc, váy hay thời gian.
cắt tỉa|Xén bớt cành lá hay phần thừa cho gọn đẹp.
cắt tóc|Làm tóc ngắn bớt hoặc tạo kiểu tóc mới.
cắt xén|Bớt đi một phần, thường làm cho thiếu sót, không trọn vẹn.
cầm bút|Cầm cây bút để viết; cũng chỉ nghề viết văn, viết báo.
cầm chắc|Nắm thật chặt; cũng có nghĩa là chắc chắn sẽ như vậy.
cầm chân|Giữ lại, làm cho ai đó không đi hay tiến lên được.
cẩm chướng|Loài hoa cánh mép răng cưa, nhiều màu, hay dùng để tặng.
cầm lái|Điều khiển xe, tàu thuyền hay máy bay.
cẩm nang|Sách nhỏ ghi những điều cần biết, hướng dẫn thiết thực.
cầm tay|Nắm lấy tay ai đó; cũng chỉ đồ nhỏ gọn cầm theo được.
cẩm thạch|Loại đá có vân đẹp, dùng để lát nền, tạc tượng hay trang trí.
cân bằng|Trạng thái hai bên ngang nhau, không bị lệch hay nghiêng.
cận cảnh|Hình ảnh chụp hoặc quay ở khoảng cách rất gần.
cần câu|Cây dài có dây và lưỡi, dùng để câu cá.
cần cù|Siêng năng, chăm chỉ làm việc không ngừng.
cân đo|Đo khối lượng và kích thước; cũng chỉ việc tính toán kỹ lưỡng.
cân đối|Các phần hài hòa với nhau, không bên nào quá nhiều hay quá ít.
cận kề|Ở rất gần bên; cũng nói về thời điểm sắp tới.
cân nặng|Khối lượng của người hay vật, đo bằng cân.
cân nhắc|Suy nghĩ kỹ, so sánh lợi hại trước khi quyết định.
cần tây|Loại rau thân dài, giòn, mùi thơm đặc trưng.
cẩn thận|Chú ý kỹ lưỡng để tránh sai sót.
cần thiết|Không thể thiếu, phải có hoặc phải làm.
cẩn trọng|Thận trọng, suy xét kỹ trước khi làm hoặc nói.
cần trục|Máy dùng để nâng và di chuyển vật nặng, hay thấy ở công trường, bến cảng.
cân xứng|Tương xứng, các phần hài hòa và hợp lý với nhau.
cấp bậc|Thứ bậc cao thấp trong một tổ chức.
cấp cao|Ở bậc trên, có vị trí hoặc trình độ cao.
cấp dưới|Người hoặc bộ phận ở vị trí thấp hơn, chịu sự quản lý.
cấp độ|Mức cao thấp khác nhau của một việc, như trong trò chơi.
cấp nước|Đưa nước sạch đến các hộ dân, nhà máy để dùng cho sinh hoạt và sản xuất.
cấp thiết|Rất cần và gấp, phải được giải quyết ngay.
cấp trên|Người hoặc cơ quan ở vị trí cao hơn, có quyền chỉ đạo.
cất cánh|Máy bay hay chim rời mặt đất bay lên.
cất công|Chịu bỏ thời gian, sức lực để làm việc gì cho ai.
cất giữ|Để vào chỗ kín, an toàn để giữ gìn.
cậu bé|Đứa trẻ là con trai, còn nhỏ tuổi.
cầu cảng|Chỗ xây ra sát nước để tàu cập vào bốc dỡ hàng.
cầu chì|Thiết bị nhỏ tự ngắt điện khi dòng điện quá mạnh.
cầu cứu|Kêu gọi, nhờ người khác giúp khi gặp khó khăn.
cầu dao|Thiết bị dùng để đóng hoặc ngắt nguồn điện cho cả nhà hay một khu vực.
câu đố|Lời đố mô tả gián tiếp một vật, người nghe phải đoán ra.
câu đối|Hai câu viết đối nhau về ý và chữ, thường treo dịp Tết.
câu hát|Một câu trong bài hát; cũng chỉ lời ca, tiếng hát nói chung.
cấu hình|Các thông số phần cứng, phần mềm của máy tính, điện thoại.
câu hỏi|Lời nói hay câu viết dùng để hỏi, cần được trả lời.
cầu hôn|Ngỏ lời xin cưới người mình yêu.
cầu lông|Môn thể thao dùng vợt đánh quả cầu qua lưới.
cầu mong|Mong mỏi, ước điều tốt đẹp sẽ đến.
câu nói|Lời một người nói ra, diễn đạt một ý trọn vẹn.
cấu tạo|Các bộ phận tạo nên một vật và cách chúng gắn với nhau.
cầu tàu|Bến làm nhô ra mặt nước để tàu thuyền cập vào.
cẩu thả|Làm qua loa, không cẩn thận, thiếu chu đáo.
cầu thang|Lối đi có nhiều bậc nối các tầng nhà.
câu thơ|Một dòng trong bài thơ, có vần và nhịp điệu.
cầu thủ|Người chơi trong một đội bóng.
cầu toàn|Muốn mọi thứ đều hoàn hảo, không chút sai sót.
cầu treo|Cây cầu được treo bằng dây cáp căng giữa các trụ.
cấu trúc|Cách các phần được sắp xếp và liên kết thành một khối.
cầu trượt|Đồ chơi có mặt dốc trơn để trẻ em trượt xuống.
câu văn|Câu viết trong một bài văn hay tác phẩm, diễn đạt một ý trọn vẹn.
cầu vượt|Cây cầu bắc ngang trên đường để xe hoặc người đi qua.
cầu xin|Khẩn khoản xin người khác giúp đỡ hay tha thứ.
cây bông|Cây trồng lấy xơ trắng trong quả để kéo sợi dệt vải; miền Nam còn gọi cây hoa là cây bông.
cây bụi|Loại cây thấp, nhiều nhánh mọc sát gốc, không có thân chính lớn.
cây bút|Dụng cụ dùng để viết hoặc vẽ.
cây cảnh|Loại cây trồng để trang trí, làm đẹp nhà cửa, sân vườn.
cây cỏ|Các loại cây và cỏ, thực vật nói chung.
cây con|Mầm cây non mới mọc hoặc mới ươm, còn nhỏ.
cây cối|Các loại cây nói chung, mọc ở vườn, rừng hay ven đường.
cây đèn|Đồ dùng có bóng hoặc bấc, dùng để chiếu sáng.
cây điều|Cây trồng lấy hạt, hạt hình quả thận mọc lòi ngoài quả, nhân rang ăn bùi.
cây gỗ|Loài cây thân to, cứng, cho gỗ để làm nhà, đồ đạc.
cây leo|Cây thân mềm, bám vào giàn hay vật khác để vươn lên cao.
cây nến|Thỏi sáp có bấc ở giữa, thắp lên để lấy ánh sáng.
cây nhỏ|Loại cây có kích thước bé, thân thấp hoặc còn non.
cây rơm|Đống rơm chất cao quanh một cây cọc, hay thấy ở sân nhà quê.
cây số|Đơn vị đo đường dài, bằng một nghìn mét; cũng chỉ cột mốc ven đường.
cây trồng|Loại cây do con người gieo trồng, chăm sóc để thu hoạch.
cây viết|Đồ dùng để viết như bút bi, bút mực, cách gọi ở miền Nam.
cây vợt|Dụng cụ có cán cầm, dùng để đánh cầu lông, bóng bàn, quần vợt.
cây xanh|Những loại cây lá xanh trồng để tạo bóng mát, làm đẹp phố phường.
cây xăng|Trạm bán xăng dầu cho xe cộ.
cha anh|Thế hệ đi trước, gồm những người lớn tuổi như cha, anh.
chả cá|Món làm từ thịt cá giã nhuyễn, nặn rồi chiên hoặc nướng.
cha đẻ|Người cha ruột sinh ra mình; cũng chỉ người sáng tạo ra một thứ.
chả giò|Món cuốn bánh tráng với nhân thịt, miến, rau rồi chiên giòn, còn gọi là nem rán.
chà là|Cây họ cọ ở vùng sa mạc, quả nhỏ màu nâu, rất ngọt.
chả lụa|Món giò làm từ thịt lợn giã nhuyễn, gói lá chuối rồi luộc chín, cách gọi ở miền Nam.
cha mẹ|Bố và mẹ, những người sinh thành, nuôi dạy con cái.
cha nuôi|Người đàn ông không sinh ra mình nhưng nhận làm cha và nuôi nấng.
chai|Vật đựng chất lỏng, cổ hẹp, có nút đậy; cũng là chỗ da dày cứng do cọ xát nhiều.
chải chuốt|Sửa soạn kỹ lưỡng đầu tóc, quần áo cho đẹp, gọn gàng.
chạm đất|Rơi hoặc hạ xuống, tiếp xúc với mặt đất.
chạm khắc|Dùng dao, đục tạo hình, hoa văn trên gỗ, đá.
chạm mặt|Tình cờ gặp trực tiếp ai đó, thường là người không muốn gặp.
chán nản|Mất tinh thần, không còn muốn cố gắng nữa.
chán ngán|Cảm thấy mệt mỏi, mất hứng thú vì điều gì kéo dài quá lâu.
chán ngắt|Rất tẻ nhạt, nhàm chán, không có gì thú vị.
chán ngấy|Quá chán vì gặp hay phải làm mãi một việc.
chán phèo|Rất nhạt nhẽo, chẳng có gì hay hay thú vị.
chàng|Người con trai trẻ, thường dùng trong văn thơ hoặc nói vui.
chàng rể|Người con trai lấy con gái của một nhà, xét trong quan hệ với nhà vợ.
chàng trai|Người con trai trẻ tuổi, đang tuổi thanh niên.
chạng vạng|Lúc trời nhá nhem tối, khi mặt trời vừa lặn.
chanh|Quả nhỏ vỏ xanh, vị rất chua, hay dùng pha nước uống.
chảo|Đồ dùng nhà bếp lòng rộng và nông, dùng để rán, xào.
chào cờ|Nghi lễ đứng nghiêm hướng về lá cờ, thường vào sáng thứ Hai ở trường.
chao đảo|Nghiêng ngả, lắc lư mạnh không vững; cũng chỉ tình thế bất ổn.
chào đón|Vui vẻ đón tiếp người hay điều mới đến.
chào đời|Được sinh ra, bắt đầu cuộc sống.
chào hỏi|Nói lời chào, hỏi thăm nhau khi gặp mặt.
chào mào|Chim nhỏ có mào nhọn trên đầu, má đỏ, hót hay, được nhiều người nuôi.
chào mời|Mời khách mua hàng hoặc dùng dịch vụ.
chào mừng|Đón tiếp và bày tỏ niềm vui khi ai đến hoặc có dịp vui.
cháu chắt|Con cháu đời sau nói chung, gồm cả cháu và chắt.
cháu họ|Con của anh chị em họ, hoặc người hàng cháu trong dòng họ.
cháu ngoại|Con của con gái, theo cách gọi của ông bà.
cháu nội|Con của con trai, theo cách gọi của ông bà.
chạy|Di chuyển nhanh bằng chân; cũng chỉ máy móc đang hoạt động.
chạy bàn|Công việc bưng bê, phục vụ khách ở quán ăn, nhà hàng.
chạy đua|Thi chạy với nhau; cũng là cạnh tranh để giành phần hơn.
chạy nhảy|Nô đùa, vận động chân tay thoải mái, nhất là trẻ em khi vui chơi.
chạy quanh|Di chuyển nhanh vòng quanh một nơi hoặc một vật.
chạy theo|Đuổi theo phía sau ai; cũng là cố theo đuổi tiền tài, trào lưu.
chạy thi|Cùng chạy đua với nhau xem ai về đích trước.
chắc|Vững, không lung lay; cũng có nghĩa là có lẽ, có khả năng.
chắc ăn|Cách nói thân mật, nghĩa là chắc chắn được việc, không lo thất bại.
chắc chắn|Vững vàng, bền; cũng có nghĩa là không còn nghi ngờ gì.
chắc hẳn|Hẳn là như thế, gần như không thể khác được.
chắc là|Có lẽ là, theo phỏng đoán thì như vậy.
chắc nịch|Rất chắc, đặc, khỏe; cũng chỉ lời nói dứt khoát, đầy tự tin.
chăm chỉ|Siêng năng, chịu khó làm việc hay học hành đều đặn.
chăm chú|Tập trung nhìn, nghe hay làm một việc, không để ý chuyện khác.
chăm chút|Săn sóc, sửa sang tỉ mỉ đến từng chi tiết nhỏ.
chăm học|Siêng năng, chịu khó trong việc học.
chăm lo|Quan tâm, lo liệu chu đáo cho ai hay việc gì.
chăm sóc|Trông nom, lo cho người, con vật hay cây cối được khỏe, tốt.
chắn bùn|Tấm che phía trên bánh xe để bùn đất không văng lên.
chẵn lẻ|Tính chất của số chia hết cho hai hoặc không chia hết cho hai.
chăn nuôi|Nuôi gia súc, gia cầm như lợn, gà, bò để lấy thịt, trứng, sữa.
chăn thả|Đưa trâu, bò, dê ra đồng cho tự ăn cỏ.
chẳng ai|Không có một người nào cả.
chẳng cần|Không cần thiết, không phải làm việc đó.
chằng chịt|Đan xen dày đặc, chồng chéo lên nhau.
chặng đường|Một quãng đường đi; cũng chỉ một giai đoạn trong cuộc đời.
chẳng hạn|Từ dùng để đưa ra ví dụ minh họa.
chẳng hề|Hoàn toàn không, không chút nào.
chẳng là|Cách mở đầu lời giải thích lý do của sự việc, giống như số là.
chẳng lẽ|Từ dùng để hỏi khi ngạc nhiên, ngờ rằng điều đó khó có thể là thật.
chẳng may|Không may mắn, vô tình xảy ra điều không mong muốn.
chẳng qua|Chỉ là, không có gì hơn; dùng để giải thích nguyên nhân thật.
chẳng sao|Không có vấn đề gì, không đáng lo.
chắp vá|Nối ghép tạm bợ từng mảnh, thiếu đồng bộ.
chặt|Dùng dao cắt mạnh cho đứt; cũng có nghĩa là khít, không lỏng.
chắt chiu|Dành dụm, giữ gìn cẩn thận từng chút một.
chấm|Điểm nhỏ và tròn; cũng là nhúng thức ăn vào nước mắm, muối trước khi ăn.
chấm bài|Đọc bài làm của học sinh để sửa lỗi và cho điểm.
chấm câu|Đặt dấu chấm, dấu phẩy và các dấu câu khác vào đúng chỗ khi viết.
chậm chạp|Làm gì cũng chậm, thiếu nhanh nhẹn.
chầm chậm|Hơi chậm, từ từ, không vội vàng.
châm chọc|Nói khích, trêu chọc làm người khác bực mình.
chấm công|Ghi lại ngày giờ đi làm của người lao động.
chấm dứt|Kết thúc, làm cho dừng hẳn lại.
chấm đen|Điểm nhỏ màu đen; cũng chỉ điều xấu, vết nhơ nhỏ.
chấm điểm|Xem xét bài làm, phần thi rồi cho điểm theo thang đánh giá.
chấm hết|Kết thúc hoàn toàn, không còn gì tiếp theo.
chấm hỏi|Dấu câu đặt cuối câu hỏi, hình móc câu có chấm bên dưới.
chậm lại|Giảm bớt tốc độ, không nhanh như trước.
châm ngôn|Câu nói ngắn gọn, chứa lời khuyên hay bài học sống.
chấm phẩy|Dấu câu gồm một chấm trên một phẩy, dùng ngăn các vế trong câu dài.
chậm rãi|Từ tốn, thong thả, không vội vàng.
chấm than|Dấu câu hình gạch đứng có chấm bên dưới, đặt cuối câu cảm thán, mệnh lệnh.
chấm thi|Đọc và cho điểm các bài thi của thí sinh.
chậm trễ|Không đúng hẹn, muộn hơn thời gian quy định hoặc cần thiết.
chân|Bộ phận dưới cùng của cơ thể dùng để đứng và đi.
chần chừ|Do dự, chưa quyết định ngay, cứ lần lữa.
chân dung|Bức tranh hay ảnh chụp khuôn mặt, hình dáng của một người.
chân đất|Đi chân trần, không mang giày dép.
chân đế|Phần đế ở dưới cùng, đỡ cho đồ vật đứng vững.
chấn động|Rung chuyển mạnh; cũng chỉ sự việc gây xôn xao, bất ngờ lớn.
chân giò|Phần chân của con lợn, hay dùng để luộc, hầm hoặc nấu canh.
chân không|Khoảng trống không có không khí; cũng chỉ đi chân trần, không mang dép.
chân lông|Lỗ rất nhỏ trên da, nơi sợi lông mọc ra và mồ hôi thoát ra.
chân mày|Hàng lông mọc phía trên mắt, còn gọi là lông mày.
chân tay|Tay và chân nói chung; cũng chỉ người thân tín giúp việc.
chân thật|Thật thà, không giả dối, đúng như trong lòng nghĩ.
chân thực|Đúng với sự thật, phản ánh như ngoài đời.
chân tình|Thật lòng, chân thành trong tình cảm, không giả dối.
chân tóc|Phần gốc của sợi tóc, sát với da đầu.
chân trời|Đường xa nhất ta nhìn thấy, nơi trời như giáp với đất hay biển.
chân váy|Loại váy chỉ che từ eo trở xuống, mặc cùng áo rời.
chân vịt|Bộ phận có cánh xoắn quay dưới nước để đẩy tàu, thuyền đi.
chấp|Nhường đối thủ một lợi thế khi thi đấu; cũng là để bụng lỗi nhỏ của người khác.
chập chờn|Lúc có lúc không, lúc rõ lúc mờ, như giấc ngủ không sâu.
chập chững|Bước đi chưa vững như trẻ mới tập đi; cũng chỉ mới bắt đầu làm việc gì.
chấp nhận|Đồng ý nhận hoặc bằng lòng với điều gì đó.
chấp thuận|Đồng ý cho phép, thường là của cấp trên hay cơ quan.
chập tối|Lúc trời vừa mới tối, đầu buổi tối.
chất béo|Thành phần có trong dầu, mỡ, bơ, cung cấp năng lượng cho cơ thể.
chất bổ|Các chất có ích nuôi dưỡng cơ thể khỏe mạnh.
chật chội|Chỗ ở quá hẹp, không đủ rộng rãi.
chật cứng|Đầy kín, không còn chỗ trống nào nữa.
chất dẻo|Vật liệu nhân tạo dễ uốn, đúc thành đồ dùng, còn gọi là nhựa.
chất đạm|Dưỡng chất có nhiều trong thịt, cá, trứng, đậu, giúp cơ thể phát triển.
chất đống|Xếp hoặc dồn lại thành đống lớn.
chất đốt|Những thứ đem đốt để lấy nhiệt đun nấu, như củi, than, ga.
chật hẹp|Không đủ rộng, khó đi lại hoặc khó xoay xở.
chất khí|Dạng vật chất như hơi, không có hình dạng cố định, ví dụ không khí.
chất liệu|Thứ vật liệu dùng để làm ra đồ vật, như vải, gỗ, da.
chất lỏng|Dạng vật chất chảy được, có hình dạng theo vật chứa, như nước, dầu.
chất lượng|Mức độ tốt hay xấu, giá trị của một sản phẩm hay việc làm.
chật ních|Đông nghịt người hoặc đồ, không thể chen thêm được.
chất rắn|Dạng vật chất cứng, có hình dạng nhất định, không chảy, như đá, gỗ.
chật vật|Vất vả, khó khăn mới làm được.
chất xám|Trí tuệ, sự hiểu biết và tài năng suy nghĩ của con người.
chậu|Đồ đựng miệng rộng, lòng nông để rửa, giặt hoặc trồng cây.
châu báu|Vàng bạc, đá quý và những đồ vật quý giá.
chậu cảnh|Chậu dùng để trồng cây cảnh, hoa kiểng.
châu chấu|Côn trùng màu xanh hoặc nâu, chân sau dài, nhảy xa, ăn lá lúa.
chậu hoa|Đồ đựng đất bằng sành, nhựa để trồng hoa trong nhà hay ngoài hiên.
châu lục|Vùng đất liền rộng lớn trên Trái Đất, như châu Á, châu Âu.
châu thổ|Đồng bằng ở vùng cửa sông, do phù sa bồi đắp nên.
che chắn|Dùng vật gì đó để ngăn gió, mưa, nắng hay bụi.
che chở|Bảo vệ, giúp đỡ người yếu hơn tránh khỏi nguy hiểm.
che đậy|Giấu đi, không để người khác biết sự thật hay lỗi lầm.
che khuất|Làm cho một vật bị lấp đi, không còn nhìn thấy được.
che kín|Phủ hết mọi chỗ, không để lộ ra chút nào.
che phủ|Phủ lên trên làm kín cả bề mặt, như mây phủ bầu trời.
chè xanh|Nước uống nấu từ lá chè tươi, màu xanh, vị chát nhẹ; cũng chỉ cây chè.
chén|Bát nhỏ dùng để ăn cơm; cũng là cốc nhỏ để uống trà.
chen chân|Len vào giữa chỗ đông người; cũng chỉ việc cố giành được một chỗ đứng.
chen chúc|Nhiều người hoặc vật dồn sát vào nhau trong chỗ chật.
chen lấn|Xô đẩy nhau để giành chỗ hoặc lên trước.
chèo|Gạt nước bằng mái gỗ dài cho thuyền đi; cũng là một lối hát kịch dân gian Bắc Bộ.
cheo leo|Ở trên cao, chênh vênh, trông nguy hiểm, như vách đá.
chép|Viết lại hoặc sao lại theo một bản có sẵn.
chê bai|Nói xấu, chỉ ra những điểm kém của người hay vật.
chế biến|Làm từ nguyên liệu thô thành món ăn hay sản phẩm.
chế tạo|Làm ra máy móc, dụng cụ từ nguyên vật liệu.
chê trách|Phê phán, trách móc vì cho là có lỗi hay không đúng.
chênh|Lệch, không bằng nhau, bên cao bên thấp.
chênh lệch|Khoảng cách, sự khác biệt giữa hai mức không bằng nhau.
chỉ bảo|Dạy dỗ, hướng dẫn cho người khác biết cách làm.
chỉ cần|Duy nhất cần một điều, không đòi hỏi gì thêm.
chi chít|Nhiều và dày đặc, cái này sát cái kia.
chỉ có|Duy nhất có, ngoài ra không còn ai hay gì khác.
chỉ dẫn|Hướng dẫn cách làm hay đường đi cho người khác.
chị dâu|Vợ của anh trai mình.
chỉ đạo|Hướng dẫn, điều khiển công việc của người dưới quyền.
chỉ định|Chọn và giao cho ai đó một việc hay một vị trí cụ thể.
chị em|Người chị và người em trong nhà; cũng là cách gọi chung giới phụ nữ.
chị gái|Người con gái sinh ra trước mình, cùng cha mẹ.
chi nhánh|Cơ sở trực thuộc của một công ty hay ngân hàng ở nơi khác.
chi phí|Khoản tiền phải bỏ ra để làm một việc gì đó.
chi phối|Có tác động, ảnh hưởng quyết định đến người hoặc việc khác.
chỉ số|Con số dùng để đo, đánh giá mức độ của một thứ.
chi tiết|Phần nhỏ, điểm cụ thể của sự việc hay đồ vật; cũng là tỉ mỉ, đầy đủ.
chi tiêu|Dùng tiền vào các việc trong cuộc sống hằng ngày.
chi trả|Bỏ tiền ra trả cho một khoản phí, dịch vụ hay món hàng.
chỉ trích|Nêu ra lỗi, điểm sai của người khác để phê phán.
chỉ trỏ|Đưa tay chỉ hết chỗ này đến chỗ khác, thường kèm bàn tán.
chia|Tách một thứ ra thành nhiều phần; cũng là phép tính ngược với phép nhân.
chia cắt|Tách rời ra, làm cho không còn liền một khối.
chia đều|Phân cho mọi người phần bằng nhau.
chia hết|Chia một số cho số khác mà kết quả là số nguyên, không còn số dư.
chia nhỏ|Tách ra thành nhiều phần nhỏ hơn.
chia phần|Phân chia cho mỗi người một phần riêng.
chia rẽ|Làm cho mất đoàn kết, tách mọi người thành các phe nhóm riêng.
chia sẻ|Cùng hưởng hoặc cùng gánh vác với người khác; cũng là kể, gửi cho người khác biết.
chia tay|Rời xa nhau, nói lời tạm biệt; cũng là kết thúc một mối quan hệ yêu đương.
chiếc|Từ đứng trước tên đồ vật để chỉ từng cái, như chiếc áo, chiếc xe.
chiêm ngưỡng|Ngắm nhìn với lòng say mê, thán phục.
chiên|Nấu thức ăn trong dầu mỡ nóng cho chín vàng.
chiến lược|Kế hoạch tổng thể, lâu dài để đạt mục tiêu lớn.
chiến thắng|Giành phần thắng, vượt qua đối thủ hoặc khó khăn.
chiêng|Nhạc cụ bằng đồng hình tròn, có núm, đánh kêu vang.
chiết|Cho cành cây ra rễ rồi cắt đem trồng; cũng là rót ra chai, lọ nhỏ hơn.
chiều|Khoảng thời gian từ trưa đến tối; cũng là nuông theo ý người khác.
chiều cao|Khoảng cách từ chân lên đến đỉnh của người hay vật.
chiều chuộng|Nuông theo ý, quan tâm và làm vừa lòng người khác.
chiều dài|Khoảng cách từ đầu này đến đầu kia theo hướng dài nhất.
chiều dọc|Hướng thẳng từ trên xuống dưới hoặc theo chiều dài của vật.
chiều hướng|Xu hướng phát triển, thay đổi của một sự việc.
chiều lòng|Làm theo ý muốn để người khác vui lòng.
chiều mai|Buổi chiều của ngày hôm sau.
chiều nay|Buổi chiều của ngày hôm nay.
chiều ngang|Hướng nằm ngang từ trái sang phải; cũng là bề rộng của vật.
chiếu phim|Cho phim hiện lên màn ảnh để mọi người xem.
chiều qua|Buổi chiều của ngày hôm qua.
chiều rộng|Khoảng cách giữa hai cạnh bên của vật, thường ngắn hơn chiều dài.
chiếu sáng|Làm cho sáng lên nhờ ánh đèn hoặc ánh nắng.
chiều sâu|Khoảng cách từ mặt trên xuống đáy; cũng chỉ sự sâu sắc.
chiều tà|Lúc cuối buổi chiều, khi mặt trời sắp lặn.
chiêu thức|Một thế võ; cũng chỉ cách làm khéo léo để đạt mục đích.
chiều tối|Khoảng thời gian cuối buổi chiều, lúc trời sắp tối.
chim|Động vật có lông vũ, có cánh và mỏ, đẻ trứng, phần lớn biết bay.
chim chóc|Các loài chim nói chung, thường bay hót quanh vườn cây.
chim cút|Loài chim nhỏ, đuôi ngắn, được nuôi để lấy trứng và thịt.
chim én|Loài chim nhỏ cánh dài nhọn, đuôi chẻ đôi, hay bay về báo hiệu mùa xuân.
chim gáy|Loài chim họ bồ câu, lông nâu, cổ có vòng cườm đốm trắng, tiếng gáy trầm.
chìm nghỉm|Lặn mất hẳn dưới nước, không thấy đâu nữa; cũng chỉ bị lu mờ, không ai chú ý.
chim ruồi|Loài chim rất nhỏ, vỗ cánh cực nhanh, hút mật hoa.
chim sẻ|Loài chim nhỏ lông nâu, hay sống gần nhà người, ăn hạt.
chim ưng|Loài chim săn mồi, mắt tinh, móng sắc, bay lượn rất giỏi.
chín|Số liền sau tám; cũng chỉ trái cây đến độ ăn được hay thức ăn đã nấu xong.
chín nhừ|Được nấu rất kỹ, mềm đến mức nát ra.
chính|Quan trọng nhất, là phần cốt lõi; cũng dùng để nhấn mạnh, nghĩa là đúng là.
chính đáng|Hợp lẽ phải, đúng đắn, được mọi người chấp nhận.
chính nghĩa|Lẽ phải, điều đúng đắn và hợp đạo lý.
chinh phục|Vượt qua khó khăn để đạt được; cũng là làm người khác yêu mến, khâm phục.
chính sách|Đường lối, quy định chung do nhà nước hay tổ chức đặt ra.
chính tả|Cách viết chữ đúng theo quy tắc của một ngôn ngữ.
chỉnh tề|Ăn mặc gọn gàng, đầy đủ, nghiêm trang.
chính thống|Được công nhận chính thức, đúng theo truyền thống gốc.
chính thức|Được công nhận đầy đủ theo quy định, không phải tạm thời.
chính xác|Đúng hoàn toàn, không có sai lệch dù nhỏ.
chịu|Đón nhận, gánh lấy điều không mong muốn; cũng là đồng ý, bằng lòng.
chịu chơi|Dám chi tiền, dám làm hết mình cho điều mình thích, không so đo.
chịu đựng|Cố nén lòng chấp nhận điều khó khăn, vất vả mà không than.
chịu khó|Siêng năng, kiên nhẫn, không ngại vất vả khi làm việc.
chịu nhiệt|Không bị hỏng hay biến dạng khi gặp nhiệt độ cao.
chịu thua|Thừa nhận mình thua hoặc không làm nổi, thôi không cố nữa.
cho ăn|Đưa thức ăn cho người hoặc con vật ăn.
cho biết|Nói hoặc báo tin để người khác được biết.
chó bông|Giống chó nhỏ, lông dài và mềm xù như bông, thường nuôi làm cảnh.
chó cảnh|Chó nuôi để làm bạn và ngắm chơi, không dùng để giữ nhà.
cho dù|Từ nối có nghĩa là dẫu, mặc dù điều gì xảy ra đi nữa.
cho đến|Tới tận, kéo dài tới một lúc hay một nơi nào đó.
cho điểm|Đánh giá bài làm hay phần thi bằng con số điểm.
cho là|Nghĩ rằng, đánh giá là như vậy theo ý mình.
chó mực|Con chó có bộ lông đen tuyền.
cho mượn|Đưa đồ cho người khác dùng tạm rồi trả lại sau.
cho nên|Từ nối dùng để nêu kết quả của điều nói trước đó.
cho phép|Đồng ý để ai đó được làm việc gì.
cho rằng|Nêu ý nghĩ, nhận định của mình về một việc.
chó rừng|Loài thú hoang giống chó, sống ở rừng hay đồng cỏ.
chó sói|Loài thú hoang giống chó lớn, sống theo bầy, hay tru vào ban đêm.
cho thuê|Để người khác dùng nhà, xe, đồ vật và trả tiền theo thời gian.
chó vàng|Con chó có bộ lông màu vàng.
cho vay|Đưa tiền hoặc vật cho người khác mượn, hẹn ngày trả lại.
chó xù|Con chó có bộ lông dày, dài và xù lên.
choàng|Khoác vải, áo lên vai hoặc vòng tay ôm qua người khác.
choáng ngợp|Bị cuốn hút, sững sờ trước điều quá lớn lao hay đẹp đẽ.
chọc|Dùng ngón tay hoặc que thọc nhẹ vào; cũng có nghĩa là trêu ghẹo.
chọc ghẹo|Trêu đùa người khác bằng lời nói hay cử chỉ cho vui.
chọc thủng|Làm thủng bằng vật nhọn; trong bóng đá là ghi được bàn vào lưới.
chọc trời|Cao vút như chạm tới trời, thường nói về tòa nhà rất cao.
chọc tức|Cố ý nói hoặc làm điều khiến người khác bực mình.
chói chang|Nắng hoặc ánh sáng rất gắt, chiếu mạnh làm lóa mắt.
chói lọi|Sáng rực đến lóa mắt; cũng chỉ thành tích vẻ vang, rạng rỡ.
chói mắt|Sáng quá mức khiến mắt khó nhìn thẳng.
chói tai|Âm thanh quá to và gắt, nghe rất khó chịu.
chòm sao|Nhóm ngôi sao tạo thành hình dạng, được đặt tên riêng.
chọn lọc|Xem xét kỹ rồi giữ lại những cái tốt nhất, phù hợp nhất.
chọn lựa|Cân nhắc giữa nhiều thứ rồi quyết định lấy cái mình muốn.
chong chóng|Đồ chơi có cánh quạt nhỏ, quay tít khi có gió thổi.
chỗ dựa|Người hoặc điều mình có thể tin cậy, nương tựa khi khó khăn.
chỗ đứng|Nơi để đứng; cũng chỉ vị thế được công nhận, như có chỗ đứng trên thị trường.
chỗ ngồi|Vị trí dành cho một người ngồi, như trên xe hay trong rạp.
chỗ ở|Nơi một người sống và sinh hoạt hằng ngày.
chỗ trống|Nơi còn để không, chưa có người hoặc vật gì chiếm.
chốc lát|Khoảng thời gian rất ngắn, chỉ trong một lúc.
chốc nữa|Sau một lúc ngắn nữa, tính từ lúc đang nói.
chổi|Dụng cụ có cán, bó bằng sợi hoặc lá, dùng để quét nhà.
chối bỏ|Không chịu thừa nhận, gạt điều gì đó ra khỏi mình.
chổi lông|Chổi làm bằng lông gà hoặc lông vịt, dùng để phủi bụi.
chôm chôm|Quả nhiệt đới vỏ đỏ có nhiều lông mềm, cùi trắng ngọt.
chồn|Loài thú nhỏ, thân thon dài, đuôi rậm, hay bắt chuột và gà.
chôn chân|Phải đứng yên hay ở mãi một chỗ, không đi đâu được.
chồn hôi|Loài thú nhỏ lông đen sọc trắng, xịt mùi rất hôi để tự vệ.
chồng|Người đàn ông đã cưới vợ; cũng chỉ nhiều vật xếp lên nhau.
chống ẩm|Ngăn không cho hơi ẩm thấm vào, giữ đồ vật khô ráo.
chồng chất|Dồn nhiều lớp lên nhau, ngày càng nhiều thêm.
chống chọi|Gắng sức đương đầu để vượt qua khó khăn, thời tiết khắc nghiệt.
chồng con|Gia đình riêng của người phụ nữ, gồm chồng và các con.
chống lại|Phản đối, đứng về phía ngược lại hoặc ngăn cản điều gì.
chốt|Thanh nhỏ để cài cửa, giữ cố định; cũng là quyết định dứt khoát.
chợ búa|Chuyện đi chợ, mua bán thức ăn hằng ngày nói chung.
chờ đợi|Ở yên trông cho tới khi ai đó đến hoặc việc gì xảy ra.
chờ mong|Trông ngóng, hy vọng điều mình mong muốn sẽ đến.
chợ nổi|Nơi mua bán họp trên sông bằng ghe thuyền, phổ biến ở miền Tây.
chợ phiên|Chợ chỉ họp vào những ngày nhất định, thường thấy ở vùng núi.
chợ trời|Khu mua bán ngoài trời, chuyên đồ cũ và hàng linh tinh giá rẻ.
chơi chữ|Dùng từ ngữ đồng âm, nhiều nghĩa một cách khéo léo để gây cười.
chơi đùa|Vui chơi, nô giỡn cùng nhau, nhất là trẻ em.
chơi khăm|Bày trò trêu chọc làm người khác bị bẽ mặt.
chơi trội|Cố làm điều khác người để mình nổi bật hơn.
chớp|Ánh sáng lóe trên trời khi có giông; cũng là nhắm mở mắt thật nhanh.
chớp mắt|Nhắm rồi mở mắt thật nhanh; cũng chỉ khoảng thời gian rất ngắn.
chớp nhoáng|Diễn ra cực kỳ nhanh, chỉ trong thoáng chốc.
chú bé|Đứa con trai nhỏ tuổi, gọi một cách thân mật.
chu đáo|Cẩn thận, quan tâm đầy đủ đến mọi chi tiết.
chủ đề|Vấn đề chính được nói tới trong bài viết, câu chuyện hay cuộc trò chuyện.
chủ động|Tự mình quyết định và làm, không chờ ai nhắc hay thúc ép.
chú họ|Em trai họ của bố, cùng dòng họ nhưng không phải em ruột.
chủ ngữ|Thành phần chính của câu, nêu người hay vật được nói tới hoặc làm hành động.
chủ nhà|Người sở hữu ngôi nhà; cũng chỉ bên đứng ra tiếp đón khách.
chủ nhân|Người làm chủ, sở hữu một đồ vật, con vật hay tài sản.
chủ nhật|Ngày cuối cùng trong tuần, thường là ngày nghỉ.
chủ nhiệm|Người phụ trách chính một lớp học, câu lạc bộ hay một đề tài.
chủ quán|Người làm chủ một quán ăn, quán nước hay cửa hàng nhỏ.
chú rể|Người đàn ông trong ngày cưới, sánh đôi với cô dâu.
chú tâm|Dồn hết sự chú ý, tâm trí vào một việc.
chú thích|Lời ghi thêm để giải thích rõ nghĩa của từ, hình ảnh.
chu trình|Chuỗi các bước lặp đi lặp lại theo thứ tự nhất định.
chú ý|Tập trung để ý, lắng nghe hoặc quan sát kỹ.
chủ yếu|Quan trọng nhất, chiếm phần lớn so với những cái khác.
chua|Có vị giống như chanh, giấm hay quả còn xanh.
chua cay|Có vị vừa chua vừa cay; cũng chỉ cảm giác cay đắng, xót xa.
chua ngọt|Có vị vừa chua vừa ngọt hài hòa, như món sườn xào.
chúa tể|Kẻ có quyền lực cao nhất, đứng trên tất cả, như sư tử là chúa tể rừng xanh.
chuẩn|Mức mẫu mực để làm căn cứ so sánh; cũng có nghĩa là đúng, chính xác.
chuẩn bị|Sắp xếp, lo trước mọi thứ cần thiết để sẵn sàng.
chuẩn mực|Điều được coi là đúng đắn, làm mẫu để mọi người noi theo.
chúc|Nói lời mong điều tốt đẹp sẽ đến với người khác.
chúc mừng|Bày tỏ niềm vui với người có việc vui hay thành công.
chúc phúc|Cầu mong may mắn, hạnh phúc cho người khác, nhất là cặp đôi mới cưới.
chúc thọ|Chúc mừng ông bà, người cao tuổi sống lâu, mạnh khỏe.
chúc tụng|Nói nhiều lời chúc tốt đẹp, thường trong tiệc hay dịp lễ.
chui|Cúi người luồn qua chỗ thấp, hẹp; cũng chỉ làm lén lút, không phép.
chùm|Nhiều quả, hoa hoặc vật nhỏ kết lại cùng một cuống, một chỗ.
chun|Có tính co giãn, như dây chun; cũng là co ngắn lại, nhăn lại.
chung|Thuộc về nhiều người cùng có, cùng dùng, không riêng ai.
chúng anh|Cách người nói xưng mình và các anh khác khi nói với người ít tuổi hơn.
chúng cháu|Cách xưng của người nói và các cháu khác với ông bà, cô chú.
chung chung|Không cụ thể, không đi vào điểm chính, khó hiểu rõ.
chúng con|Cách xưng của các con với cha mẹ hoặc người bề trên.
chung cư|Tòa nhà nhiều căn hộ để nhiều gia đình cùng ở.
chúng em|Cách xưng của người nói và các em khác với anh chị, thầy cô.
chung kết|Trận hoặc vòng thi cuối cùng để chọn ra người thắng.
chúng nó|Từ chỉ những người hay vật được nhắc đến, thường dùng thân mật hoặc coi thường.
chung sống|Cùng sống với nhau ở một nơi hoặc trong một gia đình.
chúng ta|Từ chỉ cả người nói và người nghe, tất cả cùng nhau.
chung tình|Một lòng yêu thương một người, không thay đổi.
chúng tôi|Từ người nói dùng để chỉ nhóm mình, không gồm người nghe.
chuối|Quả dài, vỏ vàng khi chín, ruột mềm ngọt, mọc thành nải.
chuối xanh|Quả chuối còn xanh, chưa chín, hay dùng nấu ốc, nấu cá hoặc ăn kèm.
chuồn|Lén lút bỏ đi để tránh mặt hoặc trốn việc.
chuồn chuồn|Côn trùng thân dài, hai đôi cánh mỏng trong, hay bay lượn gần mặt nước.
chuông|Vật bằng kim loại, khi gõ hay lắc phát ra tiếng kêu vang.
chuột|Con vật gặm nhấm nhỏ, đuôi dài; cũng là thiết bị điều khiển máy tính.
chuột bạch|Loại chuột lông trắng, mắt đỏ, nuôi làm cảnh hoặc làm thí nghiệm.
chuột chũi|Con vật nhỏ sống dưới đất, mắt kém, chân trước khỏe để đào hang.
chuột đồng|Loài chuột sống ngoài ruộng, ăn lúa, khoai.
chuột lang|Con vật nhỏ tròn, không đuôi, hiền lành, hay được nuôi làm cảnh.
chuột nhà|Loài chuột nhỏ sống trong nhà ở, hay gặm phá đồ đạc.
chuột nhắt|Loài chuột rất nhỏ, thường sống lẩn trong nhà.
chụp|Ghi hình bằng máy ảnh; cũng là vồ lấy thật nhanh hoặc úp lên trên.
chụp ảnh|Ghi lại khoảnh khắc, cảnh vật bằng máy ảnh hay điện thoại.
chụp đèn|Vật che bên ngoài bóng đèn để hắt ánh sáng và đỡ chói.
chụp hình|Dùng máy ảnh hoặc điện thoại để ghi lại hình ảnh.
chút|Một lượng rất nhỏ, không đáng kể.
chút đỉnh|Cách nói khiêm tốn chỉ một ít, không nhiều.
chút ít|Một phần nhỏ, không nhiều lắm.
chút nào|Dù chỉ một ít, thường dùng trong câu phủ định để nhấn mạnh.
chút nữa|Một lát nữa, sau ít phút; cũng có nghĩa là suýt, gần như.
chút xíu|Một ít rất nhỏ, gần như không đáng kể.
chuyển|Đưa hoặc dời từ chỗ này sang chỗ khác; cũng là thay đổi sang trạng thái khác.
chuyển biến|Thay đổi dần từ trạng thái này sang trạng thái khác.
chuyên cần|Siêng năng, đi học hay đi làm đều đặn, không bỏ buổi.
chuyên chở|Chở người hoặc hàng hóa từ nơi này đến nơi khác.
chuyên dụng|Dùng riêng cho một mục đích hoặc công việc nhất định.
chuyên đề|Vấn đề riêng được chọn để nghiên cứu, học tập hoặc trình bày.
chuyển đổi|Thay đổi từ dạng này sang dạng khác.
chuyển động|Thay đổi vị trí, di chuyển, không đứng yên một chỗ.
chuyên gia|Người có hiểu biết sâu và giỏi về một lĩnh vực.
chuyển giao|Giao lại công việc, tài sản hay kỹ thuật cho người khác.
chuyển hướng|Đổi sang hướng đi hoặc cách làm khác.
chuyển khoản|Gửi tiền từ tài khoản này sang tài khoản khác qua ngân hàng.
chuyên môn|Kiến thức, kỹ năng riêng của một nghề hay lĩnh vực.
chuyên mục|Phần nội dung riêng, ra đều đặn trên báo, đài hay trang mạng.
chuyên ngành|Ngành học hay lĩnh vực hẹp mà một người theo đuổi.
chuyên nghiệp|Làm việc thành thạo, bài bản như người làm nghề thực thụ.
chuyển nhà|Dọn đồ đạc đến ở một nơi mới.
chuyển nhượng|Nhường lại tài sản, quyền sử dụng cho người khác, thường có trả tiền.
chuyện phiếm|Câu chuyện vẩn vơ, nói cho vui và qua thời gian.
chuyên sâu|Đi sâu vào một lĩnh vực, nghiên cứu kỹ lưỡng.
chuyển thể|Viết lại tác phẩm sang hình thức khác, như từ truyện thành phim.
chuyển tiếp|Bước sang giai đoạn kế tiếp; cũng là gửi tiếp thư, tin nhắn cho người khác.
chuyên viên|Người làm công việc chuyên môn trong một cơ quan, tổ chức.
chữ cái|Ký hiệu cơ bản dùng để ghép thành từ, như a, b, c.
chữ hoa|Dạng chữ viết to, dùng ở đầu câu và trong tên riêng.
chữ nghĩa|Con chữ cùng ý nghĩa của nó; nói chung là kiến thức học hành, sách vở.
chứ sao|Lời đáp khẳng định trong văn nói, ý là đương nhiên rồi.
chữ số|Ký hiệu từ 0 đến 9 dùng để viết các con số.
chữ thập|Hình hai nét thẳng cắt nhau vuông góc, giống dấu cộng.
chữ tín|Sự giữ lời hứa, uy tín khiến người khác tin cậy mình.
chữ viết|Hệ thống ký hiệu để ghi lại tiếng nói; cũng chỉ nét chữ mỗi người.
chứa đựng|Mang ở bên trong, bao hàm vật chất hay ý nghĩa, tình cảm.
chưa hề|Không có lần nào cả, cho đến tận bây giờ.
chưa từng|Không một lần nào trải qua hay làm việc đó trước đây.
chức danh|Tên gọi của chức vụ hay vị trí công việc, như giám đốc, giáo sư.
chức năng|Nhiệm vụ hoặc tác dụng riêng của một người, bộ phận hay đồ vật.
chức vụ|Vị trí và trách nhiệm của một người trong cơ quan, tổ chức.
chừng ấy|Ngần ấy, bằng đúng số lượng hay thời gian đã nói ở trên.
chưng cất|Đun chất lỏng cho bay hơi rồi làm ngưng tụ lại để lấy phần tinh khiết.
chững chạc|Đĩnh đạc, điềm tĩnh và ra dáng người lớn, đáng tin cậy.
chứng chỉ|Giấy xác nhận một người đã học xong hoặc đạt trình độ nào đó.
chừng đó|Số lượng hoặc mức độ vừa được nhắc tới, bấy nhiêu đó.
chứng khoán|Giấy tờ có giá như cổ phiếu, trái phiếu, được mua bán trên thị trường.
chứng kiến|Tận mắt nhìn thấy một sự việc đang xảy ra.
chứng minh|Dùng lý lẽ, bằng chứng để cho thấy điều gì là đúng.
chừng mực|Mức độ vừa phải, biết giới hạn, không thái quá.
chừng nào|Từ dùng để hỏi về thời điểm, nghĩa là khi nào, bao giờ.
chứng nhận|Xác nhận chính thức bằng giấy tờ rằng điều gì là đúng.
chứng thực|Xác nhận bản sao, chữ ký là đúng; cũng là chứng minh điều gì có thật.
chứng tỏ|Cho thấy rõ, làm người khác tin vào điều gì đó.
chứng từ|Giấy tờ làm bằng chứng cho việc thu chi, giao dịch, như hóa đơn, biên lai.
chướng mắt|Trông thấy khó chịu, không vừa mắt vì lố lăng, kệch cỡm.
chướng ngại|Vật hay điều cản trở, gây khó khăn cho việc đi lại hoặc làm việc.
chương trình|Các nội dung, hoạt động sắp xếp theo thứ tự; cũng là một phần mềm máy tính.
cỏ cây|Thực vật nói chung, cỏ và cây trong thiên nhiên.
có chuyện|Xảy ra việc gì đó, thường là điều không hay.
có con|Đã sinh hoặc nuôi con, trở thành cha mẹ.
có công|Đã đóng góp, bỏ sức làm nên việc gì có ích.
cỏ dại|Các loại cỏ tự mọc, không ai trồng, hay lấn át cây trồng.
có duyên|Mang nét hấp dẫn, dễ mến một cách tự nhiên.
có điều|Từ nối dùng để nêu một điểm trái lại, nghĩa là nhưng mà.
có giá|Được coi trọng, có giá trị cao, được nhiều người ưa chuộng.
có hạn|Không nhiều, chỉ trong giới hạn nhất định.
có hậu|Kết thúc tốt đẹp, người tốt được đền đáp.
có hiếu|Biết yêu thương, kính trọng và chăm sóc cha mẹ.
có hứng|Cảm thấy thích thú, muốn làm điều gì đó.
có ích|Mang lại lợi ích, giúp được việc gì đó.
cỏ khô|Loại cỏ đã phơi khô, dùng làm thức ăn cho trâu, bò, ngựa.
co lại|Thu nhỏ hoặc ngắn bớt lại, không còn duỗi thẳng.
có lẽ|Từ diễn tả sự phỏng đoán, không hoàn toàn chắc chắn.
có lòng|Tốt bụng, biết quan tâm và nghĩ đến người khác.
có lợi|Mang lại điều tốt hoặc lợi ích cho ai đó.
có mặt|Đang ở tại nơi đó, tham dự vào.
có nghĩa|Mang ý nghĩa, có giá trị; cũng dùng để giải thích, tức là.
có phải|Từ dùng để hỏi xem điều gì đó có đúng không.
co ro|Thu người, co tay chân lại vì lạnh.
co rúm|Thu mình, co người lại vì sợ hãi hoặc lạnh.
cọ rửa|Chà và rửa cho sạch vết bẩn.
có sẵn|Đã có từ trước, không cần làm hay mua thêm.
có tài|Giỏi giang, có năng lực hơn người.
có tiếng|Được nhiều người biết đến, nổi tiếng.
cò trắng|Loài chim lông trắng, chân cao, hay lội ruộng bắt cá.
có tuổi|Đã lớn tuổi, không còn trẻ nữa.
có vẻ|Trông như thế, dường như là vậy.
có vợ|Đã cưới vợ, nói về người đàn ông đã lập gia đình.
coi chừng|Lời nhắc phải cẩn thận, đề phòng điều không hay có thể xảy ra.
coi nhẹ|Xem là không quan trọng, không để tâm nhiều.
coi như|Tạm xem là như vậy, chấp nhận điều đó là đúng.
coi thường|Xem rẻ, không tôn trọng người hoặc việc gì.
coi trọng|Xem là quan trọng, đáng quý và cần chú ý.
compa|Dụng cụ có hai càng, dùng để vẽ đường tròn.
con bé|Cách gọi thân mật một bé gái hoặc cô gái còn nhỏ tuổi.
con bọ|Côn trùng nhỏ, thường có vỏ cứng, bò hoặc bay.
con cả|Người con sinh ra đầu tiên trong gia đình.
con cái|Những người con trong gia đình nói chung.
con cháu|Các thế hệ sau trong gia đình, gồm con và cháu.
con chuột|Loài gặm nhấm nhỏ, đuôi dài; cũng là thiết bị điều khiển máy tính.
con cò|Loài chim chân dài, cổ dài, lông trắng, hay kiếm ăn ở đồng ruộng.
con cưng|Đứa con được cha mẹ yêu chiều hơn cả.
con dâu|Vợ của con trai, xét trong quan hệ với cha mẹ chồng.
con đẻ|Người con do chính mình sinh ra.
con đò|Thuyền nhỏ chở khách qua sông.
con đực|Động vật thuộc giống đực, đối lập với con cái.
con đường|Lối đi lại nối các nơi; cũng chỉ cách thức để đạt mục tiêu.
con gái|Người con thuộc giới nữ; cũng chỉ người phụ nữ còn trẻ.
con heo|Gia súc mình tròn, mõm dài, nuôi để lấy thịt, còn gọi là lợn.
còn lại|Phần vẫn sót lại sau khi đã dùng hoặc bớt đi một phần.
con lắc|Vật treo đung đưa qua lại đều đặn, như trong đồng hồ quả lắc.
con lăn|Vật hình trụ lăn được, dùng để sơn tường hoặc di chuyển đồ.
con lươn|Cá thân dài như rắn, da trơn, sống trong bùn; cũng là dải phân cách giữa đường.
con mắt|Cơ quan để nhìn trên khuôn mặt; cũng chỉ cách nhìn nhận, đánh giá.
con một|Đứa con duy nhất của cha mẹ, không có anh chị em.
còn nguyên|Vẫn giữ y như cũ, chưa bị mất mát, hư hỏng hay thay đổi.
con ngựa|Loài thú lớn chân cao, chạy nhanh, dùng để cưỡi hoặc kéo xe.
con người|Loài có trí tuệ, biết nói và lao động; cũng chỉ tính cách một người.
con quay|Đồ chơi có đầu nhọn, xoay tít trên mặt phẳng.
con rể|Người chồng của con gái, xét trong quan hệ với cha mẹ vợ.
con rối|Hình người hoặc vật được điều khiển bằng dây hay tay để biểu diễn.
con số|Giá trị bằng số chỉ số lượng, kết quả hay thông tin cụ thể.
con sông|Dòng nước lớn tự nhiên chảy dài ra biển hoặc hồ.
con tàu|Phương tiện lớn chạy trên biển hoặc trên đường ray.
còn tiếp|Chưa kết thúc, sẽ có phần tiếp theo.
con tim|Trái tim, thường dùng để nói về tình cảm, cảm xúc.
con trai|Người con thuộc giới nam; cũng chỉ người đàn ông còn trẻ.
con trẻ|Trẻ em, những đứa con còn nhỏ tuổi.
con trỏ|Dấu nhỏ trên màn hình cho biết vị trí đang thao tác.
con út|Người con sinh ra sau cùng trong gia đình.
con ve|Côn trùng kêu ra rả trên cây vào mùa hè.
cotton|Vải dệt từ sợi bông, mềm, mát và thấm mồ hôi tốt.
cô bác|Cách gọi chung những người lớn tuổi đáng kính như cô, bác.
cô bé|Bé gái hoặc thiếu nữ còn nhỏ tuổi.
cổ chân|Chỗ nối giữa bàn chân và cẳng chân.
cố chấp|Khăng khăng giữ ý kiến của mình, không chịu nghe người khác.
cô chú|Cách gọi chung người lớn ngang hàng cha mẹ, như cô và chú.
cô dâu|Người con gái trong ngày cưới của mình.
cổ điển|Theo lối truyền thống, được xem là mẫu mực, có giá trị lâu dài.
cố định|Giữ nguyên ở một chỗ hoặc một mức, không thay đổi, xê dịch.
cố đô|Thành phố từng là kinh đô của một nước trong quá khứ.
cổ động|Reo hò, khích lệ để ủng hộ; cũng là kêu gọi mọi người làm theo.
cô đơn|Một mình, thiếu người bầu bạn, chia sẻ.
cô gái|Người con gái đang tuổi thiếu nữ hoặc còn trẻ.
cố gắng|Bỏ nhiều sức lực và tâm trí để làm cho được một việc.
cô giáo|Người phụ nữ làm nghề dạy học.
cổ họng|Phần bên trong cổ, nơi thức ăn, nước uống và hơi thở đi qua.
cổ hủ|Lạc hậu, giữ khư khư những lề thói cũ không còn hợp thời.
cổ kính|Có vẻ cũ xưa, trang nghiêm và đẹp nhờ đã tồn tại lâu đời.
cô lập|Tách riêng, không cho liên hệ với bên ngoài.
cô nàng|Cách gọi vui, thân mật một cô gái trẻ.
cổ phần|Phần vốn góp vào một công ty, được chia thành nhiều phần bằng nhau.
cổ phiếu|Giấy chứng nhận sở hữu một phần vốn công ty, có thể mua bán.
cô ta|Từ chỉ một người phụ nữ được nhắc tới, hơi xa cách.
cổ tay|Chỗ nối giữa bàn tay và cánh tay, nơi thường đeo đồng hồ.
cổ thụ|Cây to đã sống rất nhiều năm, thân lớn, tán rộng.
cổ tích|Truyện dân gian có yếu tố kỳ ảo, thường kể về người hiền gặp lành.
cố tình|Biết rõ mà vẫn làm, có chủ ý chứ không phải vô tình.
cổ truyền|Có từ lâu đời và được lưu truyền qua nhiều thế hệ.
cố vấn|Người chuyên góp ý, đưa ra lời khuyên cho cá nhân hoặc tổ chức.
cổ vật|Đồ vật có từ thời xa xưa, mang giá trị lịch sử hoặc văn hóa.
cổ vũ|Hò reo, động viên để người khác thêm hăng hái.
cổ xưa|Có từ hoặc thuộc về thời đại đã qua rất lâu.
cộc lốc|Nói ngắn cụt, không có từ lễ phép, nghe thiếu tình cảm.
cối xay|Dụng cụ có hai thớt tròn chồng nhau, quay để xay thóc, ngô.
côn trùng|Loài động vật nhỏ có sáu chân, thân chia ba phần, như ong, kiến.
cổng|Lối ra vào chính có cánh đóng mở; cũng chỉ chỗ cắm dây trên thiết bị.
công bằng|Đối xử ngang nhau, đúng lẽ phải, không thiên vị ai.
công bố|Thông báo chính thức cho mọi người cùng biết.
cổng chào|Cổng trang trí dựng ở lối vào để đón khách hoặc mừng sự kiện.
cồng chiêng|Nhạc cụ bằng đồng hình tròn, đánh thành bộ trong lễ hội ở Tây Nguyên.
công chúa|Con gái của vua, thường xuất hiện trong truyện cổ tích.
công chúng|Đông đảo mọi người trong xã hội.
công chuyện|Việc riêng hoặc việc cần lo liệu, cách nói thông dụng.
công chức|Người làm việc trong cơ quan nhà nước, hưởng lương nhà nước.
công cộng|Thuộc về chung, dành cho mọi người sử dụng.
công cụ|Đồ dùng hay phương tiện giúp làm một việc nào đó.
công dân|Người mang quốc tịch của một nước, có quyền và nghĩa vụ ở nước đó.
công dụng|Tác dụng, lợi ích mà một vật đem lại.
công đoạn|Một bước trong cả quá trình làm ra sản phẩm.
cộng đồng|Nhóm người cùng chung sống hoặc có chung đặc điểm, sở thích, lợi ích.
cống hiến|Đem hết sức lực, tài năng của mình đóng góp cho công việc chung.
cộng hưởng|Dao động mạnh lên khi cùng tần số; cũng chỉ hiệu quả tăng thêm nhờ kết hợp.
cồng kềnh|To, vướng víu, chiếm nhiều chỗ nên khó mang theo hay di chuyển.
công khai|Làm rõ ràng trước mọi người, không giấu giếm.
công lao|Sức lực, đóng góp đã bỏ ra cho một việc lớn.
công lập|Do nhà nước thành lập và quản lý, thường nói về trường học.
công nghệ|Kỹ thuật, máy móc và cách thức dùng để sản xuất hay làm việc.
công nghiệp|Ngành sản xuất hàng hóa bằng máy móc với quy mô lớn.
công nhân|Người lao động làm việc trong nhà máy, công trường.
công ơn|Điều tốt lớn lao người khác đã làm cho mình, cần ghi nhớ.
công phu|Tốn nhiều thời gian, công sức và sự tỉ mỉ.
công sở|Nơi làm việc của cơ quan, văn phòng.
cộng sự|Người cùng làm việc, hợp tác với mình trong một công việc.
công sức|Sức lực và thời gian bỏ ra để làm việc gì.
công tác|Việc được giao làm; cũng chỉ chuyến đi xa vì công việc.
công thức|Biểu thức trong toán học, khoa học; cũng chỉ cách pha chế, nấu một món.
công trình|Nhà cửa, cầu đường được xây dựng; cũng chỉ một tác phẩm nghiên cứu lớn.
công trường|Nơi đang thi công, xây dựng nhà cửa, cầu đường.
công tước|Tước vị quý tộc cao nhất trong hệ thống tước hiệu châu Âu.
công việc|Việc phải làm hằng ngày, thường là nghề nghiệp kiếm sống.
công viên|Khu đất rộng có cây xanh, lối đi và ghế ngồi để mọi người dạo chơi.
cột buồm|Cây cột cao dựng trên thuyền, tàu để treo và căng cánh buồm.
cột cờ|Cây cột cao dựng thẳng để treo lá cờ.
cột đèn|Cột dựng bên đường, có gắn đèn để chiếu sáng ban đêm.
cột điện|Cột cao dựng dọc đường để mắc dây điện.
cột gôn|Cột dọc hai bên khung thành trong môn bóng đá.
cốt lõi|Phần quan trọng nhất, làm nền tảng của một sự việc hay vấn đề.
cột mốc|Cột đánh dấu ranh giới, quãng đường; cũng chỉ sự kiện quan trọng.
cột sống|Chuỗi đốt xương nối nhau dọc giữa lưng, giúp cơ thể đứng thẳng.
cốt thép|Khung thép đặt bên trong bê tông giúp công trình chịu lực tốt.
cột trụ|Cột lớn chống đỡ công trình; cũng chỉ người hay vật làm chỗ dựa chính.
cơ bản|Thuộc phần nền tảng, thiết yếu nhất của một việc.
cơ bắp|Các khối thịt trong cơ thể giúp cử động và tạo sức mạnh.
cơ cấu|Cách sắp xếp các thành phần trong một tổng thể.
cơ chế|Cách thức một hệ thống hoạt động hoặc được vận hành.
cơ giới|Thuộc về máy móc có động cơ, như xe cơ giới, máy móc thay sức người.
cơ học|Ngành vật lý nghiên cứu lực và chuyển động; cũng chỉ cách làm máy móc, rập khuôn.
cơ hội|Dịp thuận lợi để làm được điều mình muốn.
cơ khí|Ngành chế tạo, sửa chữa máy móc và đồ kim loại.
cơ mà|Từ nối trong văn nói, nghĩa là nhưng mà.
cơ quan|Đơn vị làm việc của nhà nước, tổ chức; cũng chỉ bộ phận cơ thể.
cơ sở|Nền tảng, điều làm căn cứ; cũng chỉ một địa điểm, chi nhánh.
cơ thể|Toàn bộ thân người hoặc thân con vật.
cờ tướng|Môn cờ hai người, mỗi bên mười sáu quân, thắng khi chiếu bí tướng.
cờ vây|Trò chơi cờ trên bàn kẻ ô, hai bên đặt quân đen trắng để vây chiếm đất.
cờ vua|Môn cờ quốc tế hai người chơi trên bàn 64 ô, thắng khi chiếu hết vua.
cởi bỏ|Tháo ra và bỏ đi; cũng chỉ việc gạt bỏ điều gò bó, ràng buộc.
cởi mở|Dễ gần, sẵn lòng chia sẻ suy nghĩ và tình cảm với người khác.
cơm cháo|Chuyện ăn uống hằng ngày nói chung; cũng chỉ kết quả, như chẳng nên cơm cháo gì.
cơm cháy|Lớp cơm khô vàng, giòn bám dưới đáy nồi khi nấu.
cơm chiên|Món cơm xào với trứng, rau và thịt trong chảo nóng.
cơm dừa|Phần cùi trắng, béo ngậy bên trong quả dừa.
cơm nắm|Món cơm được nén chặt thành nắm, ăn với muối vừng, tiện mang theo khi đi xa.
cơm nếp|Gạo nếp nấu hoặc đồ chín, hạt dẻo và thơm, nhiều nơi gọi là xôi.
cơm nguội|Phần cơm nấu từ bữa trước, đã để nguội.
cơm nước|Việc nấu nướng, ăn uống hằng ngày nói chung.
cơm rang|Cơm nguội đảo trên chảo với dầu mỡ, trứng và gia vị cho săn, thơm.
cơm tấm|Món cơm nấu từ gạo tấm, ăn với sườn nướng, bì, chả, quen thuộc ở miền Nam.
cụ bà|Người phụ nữ đã già, cách gọi tỏ ý kính trọng.
củ cải|Loại củ to màu trắng, vị ngọt mát, dùng nấu canh hoặc làm dưa.
củ đậu|Củ tròn vỏ vàng nhạt, ruột trắng giòn ngọt mát, thường ăn sống.
cụ già|Người đã rất cao tuổi, gọi với ý kính trọng.
củ hành|Phần củ của cây hành, nhiều lớp, mùi hăng, dùng làm gia vị.
củ khoai|Phần củ ăn được của cây khoai như khoai lang, khoai tây.
cũ mèm|Rất cũ, đã quá quen hoặc dùng lâu, không còn chút mới mẻ.
cú mèo|Loài chim săn mồi ban đêm, mắt to tròn, mặt giống mèo.
cũ nát|Đã cũ lắm và hư hỏng nhiều.
cụ nội|Cha hoặc mẹ của ông nội, bà nội.
cụ ông|Cách gọi kính trọng người đàn ông cao tuổi.
cũ rích|Rất cũ, lỗi thời, đã quá quen thuộc.
cú sút|Pha đá bóng mạnh về phía khung thành.
cụ thể|Rõ ràng, chi tiết, có thể xác định được, không chung chung.
củ tỏi|Phần củ của cây tỏi, gồm nhiều tép nhỏ, mùi hăng, dùng làm gia vị.
cua biển|Loài cua sống ở vùng nước mặn, càng to, thịt chắc và ngon.
của cải|Tiền bạc, tài sản, đồ đạc có giá trị mà người ta sở hữu.
cục bộ|Chỉ ở một phần, một khu vực nhỏ, không phải toàn bộ, như mưa cục bộ.
cục cằn|Thô lỗ, nóng nảy, nói năng hay cáu gắt.
cục cưng|Tiếng gọi âu yếm người mình rất yêu quý, thường là con nhỏ.
cục tác|Tiếng gà mái kêu, nhất là sau khi đẻ trứng.
cúc vàng|Hoa cúc có cánh màu vàng tươi, hay nở vào mùa thu và dịp Tết.
cúi đầu|Hạ đầu xuống để chào hỏi hoặc tỏ ý lễ phép, nhận lỗi.
cụm từ|Nhóm vài từ đi liền với nhau, cùng diễn đạt một ý.
cung cấp|Đưa cho, đáp ứng những thứ người khác cần.
cùng chung|Thuộc về nhiều người, mọi người đều có phần như nhau.
củng cố|Làm cho vững chắc và mạnh hơn trước, như củng cố kiến thức.
cung điện|Tòa nhà lớn, lộng lẫy nơi vua chúa ở và làm việc.
cùng lắm|Nhiều lắm thì, trường hợp xấu nhất cũng chỉ đến mức đó.
cùng lúc|Xảy ra ở một thời điểm như nhau.
cùng nhau|Đi chung, làm chung với người khác.
cũng như|Từ dùng để so sánh hai điều giống nhau hoặc nối thêm ý tương tự.
cũng thế|Giống như vậy, không khác gì.
cung trăng|Mặt trăng, nơi truyện cổ kể có chị Hằng và chú Cuội ở.
cung ứng|Đáp ứng nhu cầu bằng cách cung cấp hàng hóa, vật tư hoặc dịch vụ.
cũng vậy|Tương tự như điều vừa nói, không khác.
cùng với|Đi kèm, chung với người hay vật nào đó.
cuốc|Nông cụ có lưỡi sắt và cán dài, dùng để đào, xới đất.
cuộc đời|Quãng thời gian một người sống, cùng mọi việc họ trải qua.
cuộc đua|Sự tranh tài xem ai nhanh nhất hoặc dẫn đầu.
cuộc họp|Buổi nhiều người gặp nhau để bàn bạc công việc.
cuộc sống|Toàn bộ những hoạt động, sinh hoạt hằng ngày của con người.
cuộc thi|Sự kiện mọi người đua tài để tìm ra người giỏi nhất.
cuộc vui|Buổi vui chơi, tụ tập cùng nhau cho vui vẻ.
cuối cùng|Ở sau chót, không còn gì tiếp theo; cũng nghĩa là rốt cuộc.
cuối tuần|Những ngày cuối của tuần, thường là thứ bảy và chủ nhật.
cuộn|Cuốn tròn lại thành nhiều vòng; cũng chỉ vật được cuốn tròn.
cuồn cuộn|Dâng lên, trào ra mạnh mẽ và liên tục, như nước lũ hay khói.
cuốn hút|Có sức hấp dẫn, lôi kéo sự chú ý của người khác.
cuộn phim|Dải phim cuốn tròn dùng trong máy ảnh hoặc máy chiếu cũ.
cuộn tròn|Cuốn hoặc co mình lại thành hình tròn.
cuống cuồng|Vội vàng, rối rít, không còn bình tĩnh.
cuồng nhiệt|Hăng say, sôi nổi hết mức, như khi cổ vũ thể thao.
cụt hứng|Đang hào hứng thì bỗng mất hứng vì một chuyện bất ngờ.
cử chỉ|Động tác, điệu bộ của tay, đầu hay nét mặt khi giao tiếp.
cư dân|Người sống ở một khu vực nhất định.
cử động|Chuyển động tay chân hoặc một phần cơ thể.
cử nhân|Người đã tốt nghiệp đại học và được cấp bằng.
cứ như|Từ dùng để so sánh, ý nói giống hệt như hoặc tưởng như là.
cử tạ|Môn thể thao nâng thanh tạ nặng từ dưới đất lên cao quá đầu.
cư trú|Sinh sống thường xuyên hoặc tạm thời ở một nơi nhất định.
cứ việc|Lời bảo người khác cứ tự nhiên làm, không cần ngại ngần.
cửa bên|Cửa phụ ở phía cạnh nhà hay xe, không phải cửa chính.
cửa chớp|Cánh cửa có nhiều nan gỗ xếp nghiêng, che nắng mà vẫn thoáng gió.
cửa cuốn|Cửa làm từ các nan kim loại, cuộn lên khi mở, hạ xuống khi đóng.
cửa hàng|Nơi bày và bán hàng hóa cho khách mua.
cửa hiệu|Cửa hàng nhỏ bán hàng hoặc làm dịch vụ, thường ở mặt phố.
cửa khẩu|Nơi qua lại biên giới giữa hai nước, có kiểm soát người và hàng.
cửa kính|Cửa lắp kính trong suốt, cho ánh sáng lọt vào.
cưa máy|Máy cưa chạy bằng động cơ, dùng để cắt cây, xẻ gỗ.
cửa ngõ|Lối ra vào một ngôi nhà; cũng chỉ nơi ra vào quan trọng của một vùng.
cửa nhà|Cửa ra vào của ngôi nhà; cũng chỉ nhà cửa, gia đình nói chung.
cựa quậy|Cử động, nhúc nhích thân mình, không chịu nằm hay ngồi yên.
cửa ra|Lối hoặc cửa để đi ra ngoài, như ở nhà ga, sân bay.
cửa sổ|Khung trống trên tường để đón ánh sáng, gió; cũng chỉ khung hiện trên màn hình.
cửa sông|Chỗ dòng sông chảy ra biển, hồ hoặc một con sông khác.
cửa xe|Cánh cửa ở thân ô tô hay xe buýt để người lên xuống.
cực độ|Ở mức cao nhất, không thể hơn được nữa.
cực nhanh|Nhanh đến mức cao nhất, nhanh hơn hẳn bình thường.
cực nhọc|Vất vả, mệt nhọc vì phải làm nhiều việc nặng.
cực quang|Dải ánh sáng nhiều màu xuất hiện trên bầu trời vùng gần hai cực Trái Đất.
cực tím|Loại tia không nhìn thấy có trong ánh nắng, bước sóng ngắn hơn ánh sáng tím.
cứng|Rắn chắc, khó bẻ cong hay làm lõm, trái với mềm.
cưng chiều|Yêu thương và chiều chuộng hết mực.
cứng đầu|Bướng bỉnh, không chịu nghe lời hay làm theo người khác.
cứng nhắc|Không linh hoạt, cứ theo khuôn mẫu, không biết thay đổi cho phù hợp.
cứng rắn|Kiên quyết, vững vàng, không dễ bị lay chuyển.
cười|Nhoẻn miệng hoặc bật thành tiếng vì vui vẻ, thích thú.
cười cợt|Cười đùa thiếu nghiêm túc, đôi khi có ý trêu chọc.
cười duyên|Cười nhẹ nhàng, có nét dễ thương, cuốn hút.
cười gượng|Cố nở nụ cười dù trong lòng không vui.
cưới hỏi|Việc dạm hỏi và tổ chức đám cưới nói chung.
cười mỉm|Cười nhẹ, khóe môi hơi nhếch lên, không thành tiếng.
cười thầm|Cười trong bụng, không để người khác thấy.
cười vang|Cười to thành tiếng, vang khắp xung quanh.
cưới xin|Chuyện lấy vợ lấy chồng và làm đám cưới nói chung.
cường độ|Mức độ mạnh yếu của một hoạt động hay hiện tượng.
cương quyết|Kiên định, dứt khoát, không chịu thay đổi ý định.
cửu chương|Bảng phép nhân các số từ 2 đến 9, học thuộc ở tiểu học.
cứu giúp|Giúp đỡ người đang gặp khó khăn hoặc nguy hiểm.
cứu tinh|Người hoặc điều đến đúng lúc, giúp thoát khỏi khó khăn.
cứu trợ|Giúp đỡ tiền bạc, vật chất cho người gặp thiên tai, hoạn nạn.
cứu vãn|Cố gắng giữ lại hoặc sửa chữa một tình thế đang xấu đi.
da bò|Lớp da của con bò, thường được thuộc để làm giày, túi, thắt lưng.
da cam|Màu trung gian giữa đỏ và vàng, giống màu vỏ quả cam chín.
da dẻ|Làn da nói chung, nhất là vẻ hồng hào, mịn màng của nó.
da đầu|Lớp da phủ trên đầu, nơi tóc mọc ra.
da gà|Lớp da con gà; cũng chỉ nốt nhỏ nổi trên da khi lạnh hay xúc động.
dạ hội|Buổi tiệc lớn, sang trọng vào buổi tối, thường có khiêu vũ, ca nhạc.
da khô|Làn da thiếu nước và dầu, dễ thô ráp, bong tróc.
dã ngoại|Đi chơi, sinh hoạt ngoài trời ở nơi gần gũi thiên nhiên.
dạ quang|Phát sáng được trong bóng tối, như kim đồng hồ hay sơn đặc biệt.
da trời|Màu xanh lam nhạt giống màu bầu trời lúc trong xanh.
dai dẳng|Kéo dài mãi, lâu không chấm dứt.
dài dòng|Nói hoặc viết dài quá mức cần thiết, rườm rà.
dại dột|Thiếu suy nghĩ, khờ khạo nên dễ làm điều sai.
dài hạn|Kéo dài trong một thời gian lâu, thường nhiều năm.
dài hơi|Kéo dài trong thời gian lâu, đòi hỏi nhiều công sức và bền bỉ.
dại khờ|Ngây thơ, thiếu hiểu biết nên dễ làm điều không khôn ngoan.
dàn dựng|Sắp xếp, tổ chức một vở diễn, bộ phim; cũng là sắp đặt giả như thật.
dán mắt|Nhìn chằm chằm, không rời mắt khỏi thứ gì, như màn hình.
dàn ý|Các ý chính sắp xếp theo thứ tự để làm khung cho bài viết, bài nói.
dang dở|Đang làm nửa chừng thì phải bỏ, chưa hoàn thành.
dáng đi|Kiểu cách, tư thế của một người khi bước đi.
dáng vẻ|Hình dạng bên ngoài cùng cử chỉ, phong thái của người hay vật.
danh bạ|Danh sách tên và số điện thoại hoặc địa chỉ liên lạc.
danh dự|Sự coi trọng của mọi người đối với tư cách, phẩm giá của một người.
danh hài|Nghệ sĩ hài nổi tiếng, được nhiều người yêu mến.
danh hiệu|Tên gọi cao quý được trao để ghi nhận thành tích hay phẩm chất.
danh mục|Bảng kê các mục, các thứ được xếp theo trình tự nhất định.
danh nghĩa|Tư cách đứng ra làm việc gì; cũng chỉ việc có tên gọi mà không có thực chất.
danh ngôn|Câu nói hay, sâu sắc của người nổi tiếng, được nhiều người nhắc lại.
danh sách|Bảng ghi tên người hoặc vật theo một thứ tự.
danh thiếp|Tấm thẻ nhỏ in tên, chức vụ và cách liên lạc của một người.
danh tiếng|Tiếng tăm tốt đẹp được nhiều người biết và khen ngợi.
danh tính|Tên tuổi và các thông tin để nhận biết một người.
danh từ|Từ loại chỉ người, vật, sự việc hay khái niệm.
danh vọng|Tiếng tăm và địa vị cao trong xã hội.
dạo bước|Đi bộ thong thả, thư thái ngắm cảnh.
dao cạo|Dụng cụ có lưỡi sắc, dùng để cạo râu hoặc tóc.
dạo chơi|Đi chơi thong thả đây đó cho thư giãn.
dạo mát|Đi dạo thong thả ở nơi thoáng mát cho thư thái.
dạo quanh|Đi vòng quanh một nơi để ngắm nhìn, xem xét.
dạo trước|Khoảng thời gian trước đây không lâu.
dạy bảo|Chỉ bảo, khuyên răn để người khác biết điều hay lẽ phải.
dạy dỗ|Nuôi dạy, giáo dục con cái hoặc học trò nên người.
dạy đời|Lên giọng khuyên bảo, chỉ trích người khác như thể mình hiểu biết hơn.
dạy học|Làm công việc giảng dạy, truyền kiến thức cho học sinh.
dãy núi|Nhiều ngọn núi nối liền nhau thành hàng dài.
dãy số|Các số được sắp xếp liên tiếp theo một thứ tự hoặc quy luật.
dăm ba|Một vài, số lượng ít, khoảng ba đến năm.
dặn dò|Nhắc nhở kỹ lưỡng điều cần làm hoặc cần nhớ.
dắt tay|Nắm tay người khác để dẫn đi.
dân ca|Bài hát do nhân dân sáng tác và truyền miệng qua nhiều đời.
dân chài|Người sống bằng nghề đánh cá trên sông, biển.
dẫn chứng|Nêu ví dụ, bằng chứng để làm rõ ý mình nói; cũng là ví dụ đó.
dân cư|Những người cùng sinh sống trong một khu vực.
dân dã|Giản dị, mộc mạc, mang nét quen thuộc của làng quê.
dẫn dắt|Chỉ đường, hướng dẫn người khác đi theo; cũng là điều khiển một chương trình.
dần dần|Từng chút một theo thời gian, không đột ngột.
dẫn đầu|Đứng ở vị trí đầu tiên, vượt lên trước những người khác.
dẫn điện|Cho dòng điện chạy qua, như đồng và nhôm dẫn điện tốt.
dẫn đường|Đi trước hoặc chỉ lối để người khác đi đúng đường.
dân gian|Thuộc về đông đảo người dân, được lưu truyền từ đời này sang đời khác.
dân làng|Những người sống trong cùng một làng.
dẫn nhiệt|Cho nhiệt truyền qua, như nồi kim loại dẫn nhiệt tốt.
dân số|Tổng số người sống trong một vùng hay một nước.
dân thường|Người dân bình thường, không có chức vụ hay quyền lực.
dân tình|Người dân, mọi người nói chung, thường dùng khi kể chuyện bàn tán.
dập tắt|Làm cho tắt hẳn lửa; cũng chỉ việc chấm dứt điều gì đang bùng lên.
dầu ăn|Dầu thực vật dùng để chiên, xào, nấu thức ăn.
dấu câu|Các ký hiệu như chấm, phẩy, chấm hỏi dùng khi viết để ngắt câu.
dấu chấm|Dấu câu hình chấm tròn nhỏ, đặt ở cuối câu.
dấu cộng|Ký hiệu hình chữ thập nhỏ, biểu thị phép cộng trong toán học.
dầu dừa|Dầu ép từ cơm dừa, dùng nấu ăn hoặc dưỡng da, tóc.
dấu hiệu|Điều nhìn thấy được, cho biết một sự việc đang hoặc sắp xảy ra.
dấu hỏi|Dấu thanh hình móc câu; cũng chỉ dấu chấm hỏi đặt cuối câu hỏi.
dầu khí|Dầu mỏ và khí đốt nói chung, được khai thác từ lòng đất.
dầu lạc|Dầu ăn ép từ hạt lạc, miền Nam gọi là dầu đậu phộng.
dầu mè|Dầu ép từ hạt mè, mùi thơm đậm, miền Bắc gọi là dầu vừng.
dầu mỡ|Các loại dầu và mỡ nói chung, dùng nấu ăn hoặc bôi trơn máy.
dấu nặng|Dấu thanh hình chấm nhỏ, đặt dưới nguyên âm trong tiếng Việt.
dấu ngã|Dấu thanh hình lượn sóng, đặt trên nguyên âm trong tiếng Việt.
dấu nhân|Kí hiệu của phép nhân, viết như chữ x hoặc một dấu chấm giữa hai số.
dầu nhớt|Dầu đặc dùng để bôi trơn động cơ xe, máy móc.
dấu phẩy|Dấu câu dùng để ngắt quãng giữa các thành phần trong câu.
dấu sắc|Dấu thanh hình nét xiên lên, đặt trên nguyên âm trong tiếng Việt.
dâu tằm|Cây có lá dùng nuôi tằm, quả chín màu tím đen, vị chua ngọt.
dâu tây|Quả nhỏ màu đỏ, hình tim, lấm tấm hạt bên ngoài, vị chua ngọt.
dầu thô|Dầu mỏ vừa khai thác từ lòng đất, chưa qua lọc hay chế biến.
dấu vết|Những gì còn để lại, cho thấy sự việc đã từng xảy ra.
dầu vừng|Dầu ăn ép từ hạt vừng, có mùi thơm đặc trưng, hay dùng trộn gỏi.
dây buộc|Sợi dây dùng để cột, buộc chặt đồ vật hoặc tóc.
dây cáp|Dây to và chắc, gồm nhiều sợi kim loại hoặc lõi dẫn tín hiệu.
dây câu|Sợi dây mảnh buộc lưỡi câu để câu cá.
dây chun|Sợi dây cao su co giãn, dùng để buộc, cột đồ.
dây đàn|Sợi dây căng trên đàn, khi gảy hoặc kéo phát ra âm thanh.
dây đeo|Dây dùng để đeo túi, đồng hồ hay đồ vật lên người.
dây điện|Dây có lõi kim loại bọc nhựa, dùng để dẫn điện.
dây kẽm|Sợi kim loại mảnh mạ kẽm, dùng để buộc, cột hoặc làm hàng rào.
dây leo|Cây thân mềm bò hoặc quấn vào vật khác để vươn lên.
dây lưng|Dải da hoặc vải thắt quanh bụng để giữ quần, còn gọi thắt lưng.
dây nhảy|Sợi dây dài dùng để nhảy qua khi vui chơi hoặc tập thể dục.
dây nhợ|Các loại dây nói chung; cũng chỉ sự dính líu, ràng buộc lằng nhằng.
dây nịt|Đai đeo quanh eo để giữ quần cho chắc, còn gọi là thắt lưng.
dây phơi|Dây căng ngang dùng để phơi quần áo.
dây rợ|Dây buộc các loại nói chung, thường lằng nhằng, rối rắm.
dây thép|Sợi kim loại làm bằng thép, mảnh mà bền chắc.
dây xích|Dây gồm nhiều vòng kim loại móc nối nhau, như xích xe đạp.
dè chừng|Cẩn thận, đề phòng vì chưa thật sự tin tưởng.
dè dặt|Thận trọng, giữ gìn trong lời nói và việc làm.
dẻo dai|Có sức bền, chịu được hoạt động lâu mà không mệt mỏi.
dép lê|Loại dép không có quai sau, xỏ vào là đi, hay dùng ở nhà.
dễ bảo|Ngoan, biết vâng lời và chịu nghe theo sự chỉ bảo.
dễ chịu|Đem lại cảm giác thoải mái; cũng chỉ người tính tình dễ gần.
dễ coi|Có vẻ ngoài ưa nhìn, trông khá đẹp mắt.
dễ dãi|Quá dễ tính, không đòi hỏi chặt chẽ, dễ chấp nhận mọi thứ.
dễ dàng|Không gặp khó khăn, làm được mà không tốn nhiều công sức.
dễ ghét|Có vẻ khiến người ta không ưa; thường dùng để trách yêu, đùa vui.
dễ hiểu|Có thể hiểu được nhanh chóng mà không cần giải thích nhiều.
dễ nghe|Nghe êm tai, thích tai; cũng chỉ lời nói hợp lý, dễ chấp nhận.
dễ ợt|Cách nói thân mật chỉ việc rất dễ, chẳng tốn chút sức nào.
dê rừng|Loài dê sống hoang trên núi đá, leo trèo rất giỏi.
dễ thở|Hít thở thoải mái; cũng chỉ tình hình bớt căng thẳng, đỡ vất vả hơn.
dễ thương|Có vẻ đáng yêu, khiến người khác có cảm tình.
dễ tiêu|Nói về thức ăn được cơ thể tiêu hóa nhanh, không gây nặng bụng.
dễ tính|Tính tình dễ chịu, không khắt khe hay đòi hỏi nhiều.
dịch chuyển|Chuyển từ vị trí này sang vị trí khác.
dịch thuật|Chuyển nội dung từ ngôn ngữ này sang ngôn ngữ khác.
dịch vụ|Công việc phục vụ nhu cầu của khách hàng, như vận chuyển, sửa chữa.
diêm|Que gỗ nhỏ có đầu tẩm thuốc, quẹt vào vỏ hộp để tạo lửa.
diễn biến|Quá trình sự việc xảy ra và thay đổi theo thời gian.
diễn cảm|Thể hiện được cảm xúc qua giọng đọc, lời nói hoặc nét mặt.
diễn đàn|Nơi mọi người phát biểu, trao đổi ý kiến; cũng chỉ trang thảo luận trên mạng.
diễn đạt|Trình bày ý nghĩ, tình cảm bằng lời nói hoặc chữ viết.
diễn giả|Người trình bày, nói chuyện trước đông người tại hội thảo, buổi gặp gỡ.
diễn giải|Trình bày, giải thích rõ ràng một ý hay vấn đề cho người khác hiểu.
diễn hành|Đi thành đoàn, hàng ngũ chỉnh tề qua đường phố trong dịp lễ hội.
diễn kịch|Đóng vai trong một vở kịch; cũng chỉ việc giả vờ, làm bộ.
diện mạo|Vẻ bề ngoài, hình dáng nhìn thấy được của người hay sự vật.
diễn tả|Dùng lời nói, cử chỉ hay hình ảnh để thể hiện ý nghĩ, cảm xúc.
diện tích|Độ rộng của một bề mặt, thường tính bằng mét vuông.
diễn văn|Bài nói soạn sẵn, đọc trong buổi lễ hoặc sự kiện trang trọng.
diễn viên|Người đóng vai trong phim, kịch hoặc chương trình biểu diễn.
diễn xuất|Cách nhập vai và thể hiện nhân vật của diễn viên.
diều|Đồ chơi có khung tre dán giấy hoặc vải, thả bay lên cao nhờ gió.
diều hâu|Loài chim lớn có mỏ quặp, móng sắc, bay lượn trên cao để bắt mồi.
dinh dưỡng|Các chất bổ trong thức ăn mà cơ thể cần để sống và lớn lên.
dinh thự|Ngôi nhà lớn, sang trọng, thường của người giàu có hoặc quan chức.
dịu dàng|Nhẹ nhàng, êm ái, gây cảm giác dễ chịu.
dìu dắt|Nâng đỡ, chỉ bảo để người ít kinh nghiệm tiến bộ dần.
dịu ngọt|Ngọt nhẹ, dễ chịu; cũng chỉ lời nói nhẹ nhàng, êm ái.
dò dẫm|Đi chậm, thăm dò từng bước; cũng chỉ làm thận trọng vì chưa quen.
do dự|Phân vân, ngập ngừng, chưa dám quyết định.
do đó|Từ nối dùng để nêu kết quả của điều vừa nói ở trước.
dò xét|Quan sát, tìm hiểu kỹ một cách kín đáo để biết rõ sự việc.
doanh nghiệp|Đơn vị tổ chức sản xuất, kinh doanh để kiếm lợi nhuận, như công ty.
doanh nhân|Người làm kinh doanh, điều hành việc buôn bán, sản xuất.
doanh số|Tổng lượng hàng bán ra hoặc tổng tiền bán hàng trong một khoảng thời gian.
doanh thu|Tổng số tiền thu được từ việc bán hàng hóa, dịch vụ.
dọc đường|Trên suốt quãng đường đi từ nơi này đến nơi khác.
dõi theo|Chăm chú nhìn theo hoặc quan tâm theo sát từng bước của ai, việc gì.
domino|Trò chơi dùng các quân hình chữ nhật có chấm, xếp nối các ô cùng số chấm.
dọn bàn|Bày bát đũa, thức ăn lên bàn; cũng là thu dọn sau bữa ăn.
dọn dẹp|Thu xếp, lau chùi cho gọn gàng, sạch sẽ.
dọn nhà|Lau chùi, sắp xếp nhà cửa; cũng là chuyển đồ đạc sang chỗ ở mới.
dọn sạch|Thu dọn hết rác hay đồ đạc, không để sót lại gì.
dòng chảy|Khối nước hay chất lỏng chuyển động liên tục theo một hướng.
dỗ dành|Nói ngọt ngào, nhẹ nhàng để người khác nín khóc hoặc nghe theo.
dốc đứng|Con dốc rất cao, gần như thẳng đứng.
dốc sức|Đem toàn bộ sức lực ra để làm một việc.
dồi dào|Có rất nhiều, đầy đủ và không thiếu thốn.
dồn dập|Liên tiếp, dày đặc, cái này nối tiếp cái kia rất nhanh.
dơ bẩn|Không sạch, dính nhiều bụi bặm, vết bẩn.
dở dang|Chưa làm xong, còn đang bỏ giữa chừng.
dỡ hàng|Đưa hàng hóa từ trên xe, tàu, thuyền xuống bến bãi hay kho.
dù cho|Từ nối nêu giả định, ý là bất kể điều gì xảy ra đi nữa.
du dương|Êm ái, trầm bổng và nghe rất dễ chịu, thường nói về âm nhạc.
du hành|Đi một chuyến xa đến nhiều nơi, như du hành vũ trụ.
du học|Ra nước ngoài học tập trong một thời gian.
du khách|Người đến một nơi để tham quan, du lịch.
du lịch|Đi đến nơi khác để tham quan, nghỉ ngơi.
dù rằng|Từ nối nêu một sự thật trái ngược với điều nói sau, giống mặc dù.
dù sao|Dẫu thế nào đi nữa, bất kể tình hình ra sao.
du thuyền|Thuyền lớn, tiện nghi, dùng để đi chơi, du lịch trên biển hay sông.
du xuân|Đi chơi, ngắm cảnh, thăm viếng vào mùa xuân, nhất là dịp Tết.
dũng cảm|Gan dạ, không sợ nguy hiểm, khó khăn.
dụng cụ|Đồ dùng phục vụ một công việc cụ thể, như búa, kéo, thước.
dung dịch|Chất lỏng có một hay nhiều chất khác hòa tan đều trong đó.
dung lượng|Lượng tối đa mà một vật có thể chứa, như bộ nhớ điện thoại.
dung nham|Đá nóng chảy phun ra từ miệng núi lửa.
dung tích|Lượng chất lỏng hay khí mà một vật có thể chứa được.
duy nhất|Chỉ có một, không có cái thứ hai.
duy trì|Giữ cho tiếp tục tồn tại hoặc hoạt động như cũ.
duyên|Nét cuốn hút tự nhiên; cũng chỉ mối gắn kết do số phận sắp đặt.
duyên dáng|Có vẻ đẹp dịu dàng, cuốn hút trong dáng điệu, cử chỉ.
duyên nợ|Mối gắn bó như được số phận sắp đặt giữa người với người hay với nơi chốn.
duyên phận|Mối gắn kết giữa người với người được cho là do số phận định sẵn.
duyên số|Sự gặp gỡ, nên vợ nên chồng được cho là do trời định sẵn.
duyệt|Xem xét để chấp thuận; cũng chỉ việc xem lướt qua các trang mạng.
dự án|Kế hoạch công việc có mục tiêu, thời gian và kinh phí cụ thể.
dư âm|Tiếng còn vang lại sau khi đã dứt; cũng chỉ cảm xúc còn đọng lại.
dự báo|Báo trước điều có thể xảy ra dựa trên tính toán, như thời tiết.
dự bị|Được chuẩn bị sẵn để vào thay khi cần, như cầu thủ ngồi ghế chờ.
dữ dằn|Có vẻ hung hăng, nóng nảy, dễ làm người khác sợ.
dữ dội|Mạnh mẽ và mãnh liệt ở mức rất cao, như cơn bão lớn.
dự định|Tính trước là sẽ làm điều gì trong thời gian tới.
dự đoán|Đoán trước điều có thể xảy ra dựa trên hiểu biết.
dự kiến|Tính trước, định trước điều sẽ làm hoặc sẽ xảy ra.
dữ liệu|Thông tin, số liệu được thu thập và lưu trữ để xử lý.
dư luận|Ý kiến, nhận xét của đông đảo mọi người về một sự việc.
dự phòng|Chuẩn bị sẵn từ trước để dùng khi có sự cố hay thiếu hụt.
dự thi|Tham gia vào một kỳ thi hoặc cuộc thi.
dư thừa|Có nhiều hơn mức cần, còn thừa ra.
dự tính|Tính toán, sắp xếp trước điều mình định làm.
dữ tợn|Có vẻ hung dữ, đáng sợ, như thú dữ.
dự trữ|Cất giữ sẵn một lượng để dùng về sau khi cần.
dưa cải|Món rau cải muối chua, ăn kèm cơm hoặc nấu canh.
dưa chua|Rau cải muối với nước, để lên men có vị chua, ăn kèm cơm.
dưa chuột|Quả dài vỏ xanh, ruột nhiều nước, ăn sống giòn mát.
dựa dẫm|Ỷ lại, trông chờ vào người khác thay vì tự lo.
dưa hấu|Quả to vỏ xanh, ruột đỏ, ngọt và nhiều nước.
dưa leo|Cách gọi ở miền Nam của dưa chuột, quả dài vỏ xanh, giòn mát.
dưa lê|Loại dưa quả nhỏ, vỏ trắng hoặc vàng nhạt, ruột giòn ngọt, thơm.
dưa muối|Rau, củ như cải, cà được ngâm nước muối cho lên men chua.
dừng bước|Ngừng lại, không đi tiếp; cũng chỉ việc bị loại khỏi một cuộc thi.
dừng chân|Ghé lại nghỉ tạm một lúc trên đường đi.
dựng đứng|Thẳng đứng như được dựng lên; cũng chỉ việc bịa đặt chuyện không có.
dừng tay|Ngừng ngay việc đang làm hoặc thôi không làm tiếp.
dưới đây|Ở phần tiếp theo ngay sau, trong bài viết hoặc lời nói.
dương lịch|Lịch tính theo chu kỳ Trái Đất quay quanh Mặt Trời.
dường như|Có vẻ như vậy nhưng chưa chắc chắn.
dương xỉ|Loài cây không hoa, lá xẻ thành nhiều thùy nhỏ, mọc nơi ẩm mát.
dứt điểm|Giải quyết xong hẳn; trong bóng đá là cú sút kết thúc pha tấn công.
dứt khoát|Rõ ràng, quả quyết, không lưỡng lự hay kéo dài.
đá bóng|Chơi bóng đá, dùng chân đưa bóng vào khung thành.
đá cầu|Trò chơi dùng chân tâng quả cầu có gắn lông, không để rơi xuống đất.
đá cuội|Những viên đá nhỏ tròn nhẵn, thường thấy ở lòng suối, bờ sông.
đa dạng|Có nhiều loại, nhiều kiểu khác nhau.
đà điểu|Loài chim lớn nhất, cổ dài, chân khỏe, chạy nhanh nhưng không bay được.
đã đời|Thỏa thích, thoải mái đến mức chán chê.
đá lửa|Loại đá cứng, cọ xát tạo ra tia lửa; cũng là viên nhỏ trong bật lửa.
đa năng|Có nhiều công dụng hoặc khả năng khác nhau.
đá ngầm|Khối đá nằm dưới mặt nước, khó nhìn thấy, tàu thuyền phải tránh.
đa nhiệm|Làm được nhiều việc cùng một lúc.
đa phần|Phần lớn, chiếm hơn một nửa của cái được nói tới.
đã qua|Thuộc về quá khứ, không còn ở hiện tại.
đa số|Số đông, nhiều hơn một nửa trong một tập thể.
đa tài|Giỏi nhiều lĩnh vực, có nhiều tài năng.
đá tảng|Khối đá to và rất nặng.
đã thế|Nếu đã như vậy thì; cũng dùng để nói thêm một điều nữa.
đá vôi|Loại đá màu trắng xám, dùng để nung vôi, tạo nên nhiều hang động.
đại bàng|Loài chim săn mồi lớn, mắt tinh, móng sắc, bay rất cao.
đại diện|Thay mặt cho một người hay một tập thể; cũng chỉ người được cử làm việc đó.
đại dương|Vùng nước mặn mênh mông bao quanh các lục địa trên Trái Đất.
đại gia|Người rất giàu có, sở hữu nhiều tiền bạc và tài sản.
đại học|Bậc học cao sau phổ thông; cũng chỉ trường đào tạo bậc học này.
đãi khách|Mời khách ăn uống, tiếp đón khách chu đáo.
đại khái|Nói qua những nét chính, không đi vào chi tiết.
đại loại|Dùng khi nói chung chung, kiểu như hoặc gần giống như thế.
đại lộ|Con đường lớn và rộng trong thành phố, có nhiều làn xe.
đại số|Môn toán dùng chữ cái và ký hiệu thay cho số để tính toán, giải phương trình.
đại ý|Ý chính, nội dung tóm tắt của một bài văn hay câu chuyện.
đạm bạc|Đơn sơ, giản dị, thường nói về bữa ăn hay lối sống.
đảm bảo|Cam kết chắc chắn, chịu trách nhiệm để việc gì được thực hiện đúng.
đám cưới|Lễ kết hôn có tiệc mừng của cô dâu và chú rể.
đám đông|Nhiều người tụ tập lại một chỗ.
đảm đương|Gánh vác và lo liệu được công việc, nhất là việc nặng hay khó.
đám hỏi|Lễ nhà trai đến nhà gái xin cưới, diễn ra trước đám cưới.
đám mây|Khối hơi nước lơ lửng trên bầu trời.
đam mê|Rất say mê một việc gì, gắn bó và theo đuổi lâu dài.
đảm nhận|Nhận làm và chịu trách nhiệm về một công việc.
đàm phán|Bàn bạc giữa các bên để đi đến thỏa thuận.
đám rước|Đoàn người đi thành hàng trong lễ hội, mang theo cờ, kiệu, đèn.
đàn anh|Người lớn tuổi hơn hoặc vào trước, có kinh nghiệm hơn trong một nhóm.
đàn bà|Người phụ nữ đã trưởng thành.
đàn bầu|Nhạc cụ dân tộc Việt Nam chỉ có một dây, tiếng ngân nga.
đàn em|Những người nhỏ tuổi hơn hoặc vào sau mình.
đàn hạc|Nhạc cụ có khung lớn và nhiều dây, gảy bằng ngón tay.
đàn hát|Vừa chơi đàn vừa ca hát để giải trí.
đàn hồi|Có thể co giãn rồi trở lại hình dạng ban đầu.
đàn ông|Người nam giới đã trưởng thành.
đàn tranh|Nhạc cụ dân tộc thân dài, có nhiều dây, chơi bằng cách gảy.
đan xen|Lồng vào nhau, xen kẽ, khó tách rời.
đáng buồn|Khiến người ta cảm thấy buồn, tiếc nuối.
đáng giá|Có giá trị, xứng với công sức hay tiền bỏ ra.
đáng gờm|Mạnh, giỏi đến mức người khác phải dè chừng.
đàng hoàng|Đứng đắn, tử tế, đúng mực; cũng chỉ đầy đủ, tươm tất.
đáng kể|Khá nhiều, đủ lớn để được chú ý.
đáng khen|Làm tốt, xứng đáng được khen ngợi.
đáng lẽ|Theo lẽ thường thì phải như vậy, nhưng thực tế lại khác.
đáng ngờ|Có điều bất thường khiến người khác nghi ngờ.
đáng thương|Ở hoàn cảnh khó khăn khiến người khác thấy thương xót.
đáng tiếc|Khiến người ta cảm thấy tiếc vì không như mong đợi.
đáng tiền|Xứng với số tiền đã bỏ ra.
đáng tin|Có thể tin tưởng, giao phó việc mà không phải lo.
đãng trí|Hay quên, ít chú ý đến những gì đang diễn ra xung quanh.
đáng yêu|Dễ thương, khiến người khác muốn yêu mến.
đành|Chấp nhận làm điều gì vì không còn cách nào khác.
đánh bại|Thắng đối thủ trong thi đấu hay cuộc đọ sức.
đánh bắt|Dùng lưới, cần câu để bắt cá và hải sản.
đánh bóng|Chà xát cho bề mặt sáng bóng; cũng chỉ việc tô vẽ cho đẹp hình ảnh.
đánh cá|Bắt cá bằng lưới, câu, thường là nghề ở vùng biển, sông nước.
đành chịu|Chấp nhận điều không mong muốn vì không còn cách nào khác.
đánh cờ|Chơi cờ, như cờ tướng, cờ vua.
đánh dấu|Làm ký hiệu để dễ nhận ra hoặc ghi nhớ.
đánh đàn|Chơi nhạc cụ như đàn ghi ta, dương cầm để tạo nên bản nhạc.
đánh đố|Hỏi câu khó để thử trí người khác.
đánh đổi|Chấp nhận mất một thứ để có được thứ khác.
đánh đồng|Coi những cái khác nhau là như nhau.
đánh giá|Xem xét để nhận định giá trị, chất lượng của ai hay cái gì.
đánh hơi|Dùng mũi ngửi để tìm ra dấu vết; cũng chỉ việc sớm nhận ra điều gì.
đánh liều|Liều lĩnh làm dù biết có thể gặp rủi ro.
đành lòng|Cam lòng, nỡ làm điều mà trong lòng không muốn.
đánh lừa|Làm cho người khác tin vào điều không đúng.
đánh máy|Gõ chữ bằng bàn phím máy tính hoặc máy chữ.
đánh mất|Làm mất, để thất lạc thứ gì; cũng chỉ việc mất đi điều quý giá.
đánh phấn|Thoa phấn lên mặt để trang điểm.
đánh răng|Chải răng bằng bàn chải và kem để răng sạch.
đánh rơi|Vô ý làm rơi mất đồ vật.
đánh số|Ghi số thứ tự lên các vật để dễ nhận biết.
đánh thức|Gọi hoặc làm cho người đang ngủ tỉnh dậy.
đánh tráo|Lén thay vật này bằng vật khác để đánh lừa người ta.
đánh trống|Dùng dùi gõ vào mặt trống cho phát ra tiếng.
đánh trứng|Khuấy mạnh trứng cho tan đều hoặc bông lên khi nấu ăn, làm bánh.
đánh vần|Đọc từng chữ cái rồi ghép lại thành tiếng, như trẻ mới học đọc.
đành vậy|Chấp nhận như thế vì không thể khác được.
đào bới|Moi đất lên, lục lọi để tìm kiếm; cũng chỉ việc khơi lại chuyện cũ.
đạo diễn|Người chỉ đạo việc dàn dựng phim, kịch hoặc chương trình biểu diễn.
đạo đức|Các chuẩn mực về điều tốt, điều xấu trong cách sống và cư xử.
đào hoa|Có duyên, được nhiều người khác giới yêu mến.
đảo lộn|Làm mọi thứ thay đổi, xáo trộn, không còn theo trật tự cũ.
đảo ngược|Chuyển sang chiều ngược lại, như đổi đầu thành cuối, trên thành dưới.
đào sâu|Khoét xuống thật sâu; cũng chỉ việc tìm hiểu thật kỹ một vấn đề.
đào tạo|Dạy dỗ, huấn luyện để người học có kiến thức và kỹ năng.
đào tiên|Quả đào thần trong truyện cổ, tương truyền ăn vào sẽ sống lâu.
đáp án|Câu trả lời đúng cho một câu hỏi hay bài tập.
đáp ứng|Làm thỏa mãn yêu cầu hoặc nhu cầu của ai đó.
đặc điểm|Nét riêng giúp phân biệt người, vật này với cái khác.
đặc quyền|Quyền lợi đặc biệt chỉ dành cho một số người hay một nhóm.
đặc sản|Món ăn, sản vật nổi tiếng riêng có của một vùng đất.
đặc sệt|Rất đặc, sánh quánh lại, khó khuấy.
đặc tính|Tính chất riêng, nét đặc trưng của sự vật hay con người.
đắc ý|Vui sướng, hài lòng vì mọi việc được như ý muốn.
đắm mình|Thả mình, hòa trọn vào một nơi, một cảm xúc hay một việc gì.
đằm thắm|Tình cảm sâu sắc, dịu dàng và nồng hậu.
đắng|Có vị như cà phê đen không đường hoặc quả khổ qua.
đằng ấy|Cách gọi thân mật người đang nói chuyện với mình; cũng chỉ phía đó.
đăng cai|Nhận tổ chức một sự kiện lớn tại địa phương hay quốc gia mình.
đẳng cấp|Thứ bậc, trình độ cao thấp; cũng dùng để khen điều gì vượt trội.
đằng này|Phía bên này; cũng là cách tự xưng thân mật của người nói.
đằng sau|Phía sau lưng, phía sau của người hay vật.
đăng tải|Đưa bài viết, hình ảnh lên báo hoặc mạng.
đằng trước|Phía trước mặt, hướng mình đang nhìn hoặc đi tới.
đằng xa|Ở phía xa, chỗ cách mình một quãng khá xa.
đặt chân|Đi tới, có mặt tại một nơi, thường là lần đầu tiên.
đặt cọc|Đưa trước một phần tiền để giữ chỗ hay cam kết sẽ mua.
đắt đỏ|Giá cả nói chung cao, chi phí sinh hoạt tốn kém.
đắt giá|Rất có giá trị, rất quý; cũng nói về điều phải trả giá cao mới có.
đặt hàng|Yêu cầu bên bán chuẩn bị và giao hàng cho mình.
đặt lưng|Nằm xuống nghỉ ngơi một chút cho đỡ mệt.
đặt tên|Chọn một cái tên để gọi người, con vật hay đồ vật.
đắt tiền|Có giá bán cao, phải trả nhiều tiền mới mua được.
đầm ấm|Êm ấm, hòa thuận và yêu thương nhau, thường nói về gia đình.
đấm bóp|Xoa, bóp, vỗ nhẹ lên cơ thể cho đỡ mỏi và thấy dễ chịu.
đậm đà|Có vị đậm và ngon; cũng chỉ tình cảm sâu sắc, thắm thiết.
đầm lầy|Vùng đất trũng ngập nước, nhiều bùn và cỏ cây mọc.
đấm lưng|Dùng nắm tay đập nhẹ lên lưng để xoa bóp cho đỡ mỏi.
đập cánh|Vỗ đôi cánh lên xuống liên tục, như khi chim bay.
đập lúa|Đập bó lúa cho hạt thóc rụng ra khỏi bông.
đập vỡ|Làm một vật vỡ ra thành nhiều mảnh do va chạm mạnh.
đất cát|Đất lẫn nhiều cát; cũng dùng để chỉ đất đai, nhà đất nói chung.
đất đai|Đất nói chung, nhất là đất dùng để ở hoặc trồng trọt.
đất khách|Nơi xa quê hương, không phải quê của mình.
đất liền|Phần đất rộng lớn của lục địa, phân biệt với biển và đảo.
đất nung|Đất sét nặn thành hình rồi nung cho cứng, dùng làm gạch, ngói, đồ gốm.
đất nước|Vùng lãnh thổ cùng con người của một quốc gia.
đất sét|Loại đất mịn, dẻo khi ướt, dùng để nặn đồ gốm, làm gạch.
đầu bảng|Vị trí đứng thứ nhất trong một bảng xếp hạng hay danh sách.
đầu bếp|Người nấu ăn chuyên nghiệp, nhất là trong nhà hàng, khách sạn.
đâu có|Dùng để phủ nhận, nghĩa là không hề như thế.
đầu cuối|Phần đầu và phần cuối của sự việc; cũng chỉ thiết bị ở điểm cuối mạng.
đầu đàn|Con vật dẫn đầu cả đàn; cũng chỉ người giỏi nhất, dẫn dắt một lĩnh vực.
đâu đây|Ở một chỗ nào đó gần quanh mình.
đậu đen|Loại đậu hạt nhỏ vỏ đen, thường dùng nấu chè hoặc nấu nước uống.
đậu đỏ|Loại đậu hạt màu đỏ, thường dùng nấu chè, thổi xôi hoặc làm bánh.
đầu đuôi|Toàn bộ câu chuyện, sự việc từ lúc bắt đầu đến khi kết thúc.
đấu giá|Bán bằng cách để nhiều người trả giá, ai trả cao nhất thì được mua.
đầu giường|Phía giường nơi đặt gối, chỗ kê đầu khi nằm.
đầu gối|Khớp nối giữa đùi và cẳng chân, gập lại khi ngồi xuống.
đậu hũ|Món làm từ đậu nành xay, nấu rồi ép thành khối mềm màu trắng.
đấu loại|Vòng thi đấu để loại bớt người hoặc đội yếu hơn.
đầu lưỡi|Phần chóp của lưỡi; cũng chỉ lời nói ngoài miệng, không thật lòng.
đầu máy|Phần có động cơ kéo cả đoàn tàu; cũng chỉ máy phát băng, đĩa hình.
đầu mối|Nơi các đường giao thông tập trung; cũng chỉ người hay nơi liên hệ chính.
đầu mùa|Khoảng thời gian mới bắt đầu một mùa trong năm hay một vụ thu hoạch.
đậu nành|Loại đậu hạt tròn màu vàng, dùng làm sữa, đậu phụ, nước tương.
đầu óc|Bộ óc, khả năng suy nghĩ và hiểu biết của một người.
đậu phụ|Món ăn màu trắng, mềm, làm từ sữa đậu nành ép thành bánh.
đầu ra|Sản phẩm, kết quả tạo ra từ một quá trình; cũng chỉ nơi tiêu thụ hàng hóa.
đầu tàu|Phần đầu có động cơ kéo đoàn tàu; nghĩa bóng là người dẫn dắt.
đấu thủ|Người tham gia thi đấu trong một môn thể thao hay cuộc thi.
đầu tiên|Trước hết, đứng ở vị trí thứ nhất so với những cái khác.
đầu tóc|Tóc trên đầu nói chung, thường nói về kiểu tóc và sự chải chuốt.
đậu trắng|Loại đậu hạt màu trắng, thường nấu chè hoặc hầm.
đấu trí|Thi thố với nhau bằng trí óc, mưu mẹo.
đầu tư|Bỏ tiền, công sức vào việc gì để mong thu lại lợi ích sau này.
đậu tương|Loại đậu hạt vàng, còn gọi là đậu nành, dùng làm sữa và đậu phụ.
đầu vào|Những thứ đưa vào một quá trình, như nguyên liệu, vốn hoặc dữ liệu.
đậu xanh|Loại đậu hạt nhỏ vỏ xanh, ruột vàng, dùng nấu chè, làm bánh.
đầy ắp|Rất đầy, chứa nhiều đến mức như sắp tràn ra ngoài.
đầy đủ|Có đủ tất cả những gì cần, không thiếu thứ gì.
đẩy mạnh|Thúc đẩy để công việc tiến triển nhanh hơn, mạnh mẽ hơn.
đầy năm|Ngày em bé tròn một tuổi, thường được gia đình làm lễ mừng.
đẩy nhanh|Làm cho công việc tiến triển nhanh hơn.
đẩy tạ|Môn điền kinh dùng tay đẩy quả tạ đi xa nhất có thể.
đầy tháng|Lễ mừng em bé tròn một tháng tuổi.
đầy tràn|Chứa nhiều đến mức trào cả ra ngoài.
đè bẹp|Ép mạnh làm cho dẹt lại; cũng chỉ thắng áp đảo đối phương.
đẻ trứng|Sinh sản bằng cách cho ra trứng, như gà, chim, rùa.
đem theo|Mang theo bên mình khi đi đâu đó.
đem về|Mang từ nơi khác trở về nhà hay về chỗ của mình.
đèn bàn|Chiếc đèn nhỏ đặt trên bàn học hoặc bàn làm việc.
đèn cầy|Cách gọi cây nến ở miền Nam, làm bằng sáp, có bấc ở giữa.
đèn chiếu|Loại đèn rọi ánh sáng mạnh; cũng chỉ máy chiếu hình ảnh lên màn.
đèn chùm|Bộ đèn treo trần gồm nhiều bóng, trang trí lộng lẫy.
đèn dầu|Loại đèn đốt bằng dầu hỏa, dùng khi chưa có điện.
đèn điện|Loại đèn sáng nhờ dòng điện, như bóng đèn tròn, đèn tuýp.
đèn đỏ|Tín hiệu giao thông yêu cầu xe cộ dừng lại.
đèn đóm|Các loại đèn nói chung, hay dùng khi nói về việc bật, tắt đèn.
đen đủi|Gặp nhiều điều không may, xui xẻo.
đèn đuốc|Đèn và đuốc, các thứ để thắp sáng nói chung.
đen kịt|Đen dày đặc, phủ kín một vùng, như mây trước cơn mưa.
đèn lồng|Đèn có khung bọc giấy hoặc vải, thường treo vào dịp lễ hội.
đèn neon|Loại đèn ống phát sáng nhờ khí bên trong, dùng chiếu sáng hoặc làm biển hiệu.
đen ngòm|Đen sâu hun hút, tối om đến mức nhìn không thấy đáy.
đèn ngủ|Loại đèn ánh sáng dịu nhẹ, bật lúc đi ngủ.
đèn nháy|Dây bóng nhỏ nhấp nháy nhiều màu, thường dùng trang trí dịp lễ.
đèn pha|Loại đèn có chùm sáng mạnh, chiếu xa, như đèn phía trước ô tô.
đèn pin|Loại đèn nhỏ cầm tay, dùng pin để chiếu sáng.
đen thui|Đen sạm, thường nói về da bị cháy nắng hoặc đồ bị cháy.
đèn trần|Loại đèn gắn trên trần nhà, chiếu sáng cả căn phòng.
đèn treo|Loại đèn được treo lơ lửng từ trần nhà hay mái hiên.
đèn xanh|Tín hiệu giao thông cho phép đi; cũng chỉ sự đồng ý, cho phép.
đeo đuổi|Kiên trì theo đuổi một mục tiêu hay mơ ước.
đẹp đẽ|Có vẻ đẹp dễ nhìn; cũng chỉ việc làm cao đẹp, đáng quý.
đẹp đôi|Hai người trông rất xứng hợp với nhau, thường nói về cặp yêu nhau.
đẹp mã|Có vẻ ngoài đẹp, ưa nhìn, nhưng chưa chắc bên trong đã tốt.
đẹp mắt|Trông đẹp, nhìn vào thấy dễ chịu và thích thú.
đẹp trai|Có khuôn mặt và vẻ ngoài ưa nhìn, nói về con trai, đàn ông.
đẹp trời|Thời tiết tốt, trời trong, nắng nhẹ và dễ chịu.
đề bài|Nội dung câu hỏi, yêu cầu của một bài tập hay bài thi.
để bụng|Ghi nhớ trong lòng điều phật ý, không chịu bỏ qua.
đề cao|Coi trọng và nêu cao giá trị của ai hay điều gì.
đề cập|Nói đến, nhắc tới một vấn đề trong khi nói hay viết.
để cho|Cho phép, không ngăn cản người khác làm gì; cũng dùng để nêu mục đích.
đề cử|Giới thiệu một người hay tác phẩm để được bầu chọn, xét giải.
đề cương|Bản liệt kê các ý chính, nội dung chính cần học hay cần viết.
để đời|Đáng nhớ mãi, để lại dấu ấn lâu dài về sau.
để lại|Không mang theo mà giữ lại một chỗ, hoặc trao lại cho người sau.
để lộ|Vô tình hay cố ý làm người khác thấy, biết điều đang giấu.
để mà|Cụm từ chỉ mục đích, mang nghĩa cốt để làm việc gì đó.
để mặc|Bỏ đó, không quan tâm hay can thiệp, muốn ra sao thì ra.
để mắt|Chú ý nhìn ngó, trông chừng hoặc quan tâm tới ai, việc gì.
đề nghị|Nêu ý kiến, yêu cầu để người khác xem xét, chấp nhận.
để phần|Giữ lại một phần đồ ăn, đồ dùng cho người chưa có mặt.
đề phòng|Chuẩn bị trước để tránh điều không hay có thể xảy ra.
để sau|Hoãn lại, làm vào lúc khác chứ không phải bây giờ.
đề tài|Chủ đề chính được chọn để viết, nghiên cứu hay bàn luận.
để tâm|Chú ý, quan tâm và suy nghĩ tới điều gì.
để tóc|Nuôi tóc hoặc giữ một kiểu tóc nhất định, như dài hay ngắn.
để trống|Không điền, không đặt gì vào, giữ nguyên chỗ trống.
đệ tử|Học trò theo một vị thầy để học nghề hay học võ.
để yên|Không động chạm, không làm phiền, giữ nguyên như cũ.
đêm hôm|Khoảng thời gian ban đêm, thường đã khuya.
đêm khuya|Thời gian rất muộn trong đêm, khi mọi người đã ngủ.
đêm ngày|Cả ban đêm và ban ngày, liên tục không nghỉ.
đêm tối|Ban đêm không có ánh sáng, trời tối mịt.
đền bù|Trả bằng tiền hay vật để bù cho thiệt hại đã gây ra.
đến cùng|Theo đuổi tới tận lúc kết thúc, không bỏ cuộc giữa chừng.
đền đáp|Đáp lại công ơn, tình cảm của người đã giúp đỡ mình.
đến mức|Tới một mức độ nào đó, thường dùng để nhấn mạnh là rất nhiều.
đến nay|Tính từ một thời điểm trước cho tới bây giờ.
đến nơi|Tới được chỗ cần tới; cũng chỉ việc sắp xảy ra rất gần.
đến tuổi|Đủ tuổi để làm một việc nào đó, như đi học hay nghỉ hưu.
đều đặn|Lặp lại đúng nhịp, đúng giờ, không ngắt quãng.
đều đều|Lặp đi lặp lại một cách đều đặn, không thay đổi.
đều nhau|Ngang bằng nhau, không bên nào hơn hay kém.
đi bộ|Di chuyển bằng chân, không dùng xe.
đi buôn|Làm nghề mua đi bán lại hàng hóa để kiếm lời.
đi chợ|Đến chợ để mua thực phẩm, đồ dùng hằng ngày.
đi chơi|Ra ngoài để vui chơi, thư giãn.
đi dạo|Thong thả tản bộ để ngắm cảnh và thư giãn.
đi đầu|Dẫn đầu, tiên phong làm trước người khác.
đi đôi|Luôn gắn liền với nhau, không tách rời.
đi đứng|Dáng điệu, cách đi lại và đứng của một người.
đi đường|Di chuyển trên đường để tới một nơi nào đó.
đi học|Đến trường để học tập; cũng chỉ việc còn đang là học sinh.
đi họp|Đến dự cuộc họp để bàn bạc công việc.
đi kèm|Gắn liền hoặc có thêm cùng với một thứ chính, như phụ kiện theo máy.
đi khỏi|Rời một nơi nào đó để sang nơi khác.
đi lại|Di chuyển qua lại; cũng chỉ việc qua lại thăm hỏi nhau.
đi làm|Đến chỗ làm việc mỗi ngày; cũng chỉ việc có công ăn việc làm.
đi lên|Di chuyển lên phía trên; cũng chỉ sự tiến bộ, phát triển.
đi nghỉ|Đến nơi khác để thư giãn, nghỉ ngơi trong kỳ nghỉ.
đi qua|Di chuyển ngang qua một nơi nào đó.
đi ra|Rời từ trong ra phía ngoài.
đi tắt|Chọn lối ngắn hơn để đến nơi nhanh hơn.
đi thăm|Đến gặp hỏi han ai đó hoặc ghé thăm một nơi.
đi thẳng|Tiến thẳng về phía trước, không rẽ ngang; cũng chỉ việc tới thẳng nơi cần đến.
đi theo|Bước sau hoặc cùng với ai đó; cũng chỉ việc chọn theo một hướng, một lý tưởng.
đi thi|Tham dự một kỳ thi hoặc cuộc thi.
đi thôi|Lời rủ nhau cùng đi hoặc giục đi nhanh.
đi vào|Bước vào bên trong; cũng chỉ việc bắt đầu làm một việc.
đi vắng|Không có ở nhà vì đã ra ngoài.
đi về|Trở về nhà hoặc nơi xuất phát.
đi vòng|Không đi thẳng mà theo đường vòng để tới nơi.
địa bàn|Khu vực, phạm vi nơi diễn ra một hoạt động nào đó.
đĩa bay|Vật bay hình đĩa, được cho là tàu của người ngoài hành tinh; cũng là đồ chơi ném.
địa cầu|Trái Đất nơi chúng ta sống; cũng chỉ quả cầu mô hình Trái Đất.
địa chất|Ngành khoa học nghiên cứu cấu tạo và sự hình thành của vỏ Trái Đất.
địa chỉ|Thông tin số nhà, tên đường, khu vực để tìm tới hay gửi thư đến.
địa danh|Tên gọi của một nơi như làng, sông, núi, thành phố.
địa điểm|Nơi, chỗ cụ thể xảy ra sự việc hay diễn ra hoạt động.
địa hình|Hình dạng bề mặt đất của một vùng như núi, đồi, đồng bằng.
địa phương|Một vùng, một nơi cụ thể trong nước, phân biệt với cả nước.
đích|Nơi cần đến cuối cùng trong cuộc đua; cũng chỉ mục tiêu hướng tới.
đích thân|Tự mình làm, không nhờ người khác.
đích thực|Thật sự đúng với bản chất, không phải giả.
điểm cao|Kết quả thi hoặc kiểm tra đạt mức tốt.
điểm danh|Gọi tên từng người để kiểm tra ai có mặt, ai vắng.
điềm đạm|Bình tĩnh, nhẹ nhàng, không nóng nảy hay vội vàng.
điểm mù|Vùng người lái xe không nhìn thấy qua gương; cũng chỉ điều mình chưa nhận ra.
điểm số|Con số đánh giá kết quả học tập hay thi đấu.
điểm tâm|Bữa ăn nhẹ vào buổi sáng.
điềm tĩnh|Bình tĩnh, giữ được thái độ ôn hòa trong mọi tình huống.
điểm tựa|Chỗ dựa để đứng vững; cũng chỉ người hay điều giúp mình vững lòng.
điện|Dạng năng lượng chạy qua dây dẫn, làm đèn sáng, máy móc hoạt động.
điện ảnh|Nghệ thuật và ngành làm phim để chiếu cho khán giả xem.
điện áp|Hiệu điện thế giữa hai điểm, đo bằng đơn vị vôn.
điên đảo|Rối tung, đảo lộn hết cả; cũng chỉ bị cuốn hút mạnh đến mất bình tĩnh.
điên đầu|Rối trí, mệt mỏi vì quá nhiều việc hoặc chuyện khó giải quyết.
điển hình|Tiêu biểu, mang đặc điểm rõ nhất của một nhóm.
điền kinh|Nhóm môn thể thao gồm chạy, nhảy và ném.
điện máy|Các đồ dùng chạy bằng điện như tủ lạnh, máy giặt, ti vi.
điện năng|Năng lượng của dòng điện, dùng để chạy máy móc, thắp sáng.
điên rồ|Rất liều lĩnh, khác thường, thiếu suy nghĩ chín chắn.
điện thoại|Thiết bị dùng để gọi, nghe và nhắn tin từ xa.
điển trai|Nói về con trai có gương mặt đẹp, phong cách lịch lãm.
điện trở|Mức cản dòng điện của một vật; cũng chỉ linh kiện tạo ra mức cản đó.
điện tử|Liên quan đến linh kiện, mạch điện như máy tính, điện thoại; cũng chỉ trò chơi trên máy.
điệp khúc|Đoạn nhạc được lặp lại nhiều lần trong bài hát.
điệu bộ|Dáng vẻ, cử chỉ của một người khi nói hay làm gì.
điều chỉnh|Sửa đổi, thay đổi cho phù hợp hoặc chính xác hơn.
điều độ|Có chừng mực và đều đặn, không quá đà.
điều hành|Quản lý, chỉ đạo để công việc hay tổ chức hoạt động trơn tru.
điêu khắc|Nghệ thuật tạc, chạm tượng hoặc hình khối từ gỗ, đá, kim loại.
điều khiển|Làm cho máy móc, xe cộ hoạt động theo ý mình; cũng chỉ việc chỉ huy người khác.
điều khoản|Từng mục, từng điều được ghi trong hợp đồng hay văn bản luật.
điều kiện|Những gì cần có để một việc có thể xảy ra hoặc thực hiện.
điều phối|Sắp xếp, phân công để các bộ phận phối hợp nhịp nhàng.
điều ước|Mong ước thầm kín, hy vọng một ngày sẽ thành sự thật.
đinh|Vật nhọn bằng kim loại, đóng vào gỗ hay tường để giữ, treo đồ.
đỉnh cao|Điểm cao nhất; cũng chỉ mức thành công, tài giỏi cao nhất.
định cư|Đến ở lâu dài, ổn định tại một nơi mới.
định dạng|Cách trình bày, sắp xếp hoặc kiểu lưu trữ của văn bản, tệp tin.
đĩnh đạc|Chững chạc, từ tốn và nghiêm trang trong cử chỉ, lời nói.
đình đám|Rất nổi tiếng, được nhiều người bàn tán.
đỉnh đầu|Chỗ cao nhất ở phía trên của cái đầu.
đinh ghim|Chiếc ghim nhỏ có đầu tròn, dùng để cài, giữ giấy hay vải.
định giá|Ước tính và đưa ra giá trị, giá bán cho một thứ gì.
định hình|Tạo ra hoặc có được hình dạng, đặc điểm rõ ràng, ổn định.
đính hôn|Lễ hứa hôn chính thức giữa hai người trước khi cưới.
định hướng|Xác định phương hướng hay mục tiêu để biết nên đi theo đường nào.
định kiến|Cách nghĩ cố định, thường thiên lệch, về một người hay nhóm người.
định lượng|Xác định số lượng, khối lượng của một thứ gì đó; trái với định tính.
định mệnh|Số phận được cho là đã sắp đặt sẵn, khó thay đổi được.
định mức|Mức quy định về số lượng, chi phí hay thời gian cho một việc.
định nghĩa|Câu giải thích rõ ý nghĩa của một từ hay khái niệm.
đinh ninh|Tin chắc chắn trong lòng, không chút nghi ngờ.
đinh ốc|Chốt kim loại có ren, vặn cùng con tán để giữ chặt các bộ phận.
đinh vít|Chốt kim loại có ren xoắn, dùng tua vít vặn vào gỗ hay tường.
đỏ bừng|Đỏ ửng lên rất rõ, thường nói về khuôn mặt khi ngượng hay nóng.
đỏ chót|Có màu đỏ tươi, rất rực và nổi bật.
đỏ hoe|Hơi đỏ quanh mắt, thường do vừa khóc hoặc thức khuya.
đo lường|Xác định kích thước, khối lượng hay mức độ bằng dụng cụ.
đỏ mặt|Mặt ửng đỏ lên vì ngượng ngùng, xấu hổ hay nóng bức.
đỏ rực|Đỏ tươi và sáng chói như màu lửa.
đọ sức|Thi với nhau xem ai mạnh hơn, ai giỏi hơn.
đỏ thắm|Màu đỏ tươi, đậm và đẹp, như hoa hồng hay môi son.
đỏ ửng|Đỏ hồng lên, thường ở má khi ngượng hay khi nóng.
đoàn kết|Gắn bó, cùng chung sức với nhau vì mục tiêu chung.
đoán mò|Nói bừa một câu trả lời khi không có căn cứ rõ ràng.
đoạn thẳng|Phần đường thẳng được giới hạn bởi hai điểm.
đoán trước|Biết hoặc nghĩ ra điều sẽ xảy ra trước khi nó đến.
đoàn tụ|Gặp lại và sum họp sau thời gian xa cách.
đoạt|Giành lấy được về phần mình, như đoạt giải, đoạt huy chương.
đọc bài|Đọc to hoặc ôn lại nội dung bài học, bài viết.
đói bụng|Cảm giác bụng trống rỗng, rất muốn được ăn.
đòi hỏi|Yêu cầu phải có hoặc phải được làm; cũng chỉ mong muốn quá mức.
đói lả|Đói đến mức mệt rã rời, không còn chút sức nào.
đói meo|Rất đói, bụng trống rỗng vì lâu chưa được ăn.
đom đóm|Côn trùng nhỏ có đuôi phát sáng, bay vào ban đêm.
đòn bẩy|Thanh cứng tựa vào một điểm để nâng vật nặng; nghĩa bóng là động lực.
đón chào|Vui vẻ chào đón ai hoặc điều gì mới đến.
đón dâu|Nhà trai đến nhà gái rước cô dâu về trong ngày cưới.
đòn gánh|Đoạn tre dẹt và dài đặt trên vai để gánh hàng ở hai đầu.
đón nhận|Vui lòng tiếp nhận điều gì đến với mình.
đón tiếp|Ra chào và tiếp đãi khách đến chơi.
đóng chai|Cho đồ uống vào chai và đậy kín để bán hoặc cất giữ.
đóng cửa|Khép cửa lại; cũng chỉ việc cửa hàng, cơ sở ngừng hoạt động.
đóng dấu|In con dấu lên giấy tờ để xác nhận.
đong đưa|Lắc lư nhẹ qua lại; cũng chỉ việc tán tỉnh, lấp lửng về tình cảm.
đóng gói|Cho hàng hóa vào hộp, túi và gói kín cẩn thận.
đóng góp|Bỏ công sức, tiền của hoặc ý kiến vào việc chung.
đóng khung|Lắp khung cho tranh ảnh; cũng chỉ việc giới hạn trong một phạm vi.
đóng kịch|Diễn vai trong vở kịch; cũng chỉ việc giả vờ, không thật lòng.
đóng phim|Tham gia diễn xuất trong một bộ phim.
đóng vai|Nhập vào một nhân vật để diễn; cũng chỉ việc giữ một vai trò.
đồ ăn|Những thứ có thể ăn được, thức ăn nói chung.
độ ẩm|Lượng hơi nước có trong không khí hoặc trong một vật.
độ cao|Khoảng cách từ mặt đất hay mặt nước biển lên tới một điểm.
đồ chơi|Vật dụng làm ra để chơi đùa, nhất là dành cho trẻ em.
đố chữ|Trò chơi đoán chữ qua câu đố, gợi ý hay hình ảnh.
đồ cổ|Vật có từ rất lâu đời, có giá trị lịch sử hay sưu tầm.
đồ da|Các vật dụng làm từ da thuộc, như túi, ví, giày, thắt lưng.
độ dài|Khoảng cách từ đầu này đến đầu kia của một vật.
độ dốc|Mức nghiêng lên hoặc xuống của mặt đường, sườn đồi.
đồ dùng|Các vật dụng phục vụ sinh hoạt, học tập hay làm việc hằng ngày.
đồ đạc|Các vật dụng trong nhà như bàn, ghế, tủ, giường.
đổ đầy|Rót hoặc cho thêm vào cho đến khi không còn chỗ trống.
đồ giả|Hàng làm nhái giống đồ thật nhưng không phải hàng chính gốc.
đồ gốm|Vật dụng làm từ đất sét nặn rồi nung, như bát, chum, bình hoa.
đồ hộp|Thức ăn chế biến sẵn, đóng kín trong hộp để giữ được lâu.
đổ lỗi|Cho rằng người khác có lỗi, đẩy trách nhiệm sang người khác.
đổ mưa|Trời bắt đầu mưa, thường là mưa xuống nhiều và nhanh.
độ này|Khoảng thời gian gần đây cho tới bây giờ.
độ nét|Mức rõ ràng, sắc sảo của hình ảnh trên màn hình hay ảnh chụp.
đồ nghề|Bộ dụng cụ cần thiết dùng cho một nghề hay công việc.
độ nhạy|Mức độ phản ứng nhanh và chính xác của máy móc hay giác quan.
đồ sộ|To lớn, nặng nề và hoành tráng về kích thước hay số lượng.
đồ sứ|Vật dụng làm bằng sứ trắng, mịn và cứng, như bát, đĩa, bình.
đô thị|Khu vực thành phố, thị xã đông dân, nhà cửa san sát.
đồ thừa|Thức ăn còn sót lại sau bữa ăn; cũng chỉ thứ dư ra, không dùng đến.
đồ uống|Các thứ dùng để uống, như nước ép, trà, sữa, nước ngọt.
đồ vật|Vật cụ thể do con người làm ra để sử dụng.
đổ xô|Rất nhiều người cùng kéo đến hay cùng làm một việc.
độc đáo|Mới lạ, riêng biệt, không giống những cái khác.
độc hại|Có thể gây hại cho con người, động vật hay môi trường.
độc lập|Tự đứng vững, không phụ thuộc người khác; cũng chỉ quốc gia tự chủ.
độc nhất|Chỉ có duy nhất một, không có cái thứ hai giống vậy.
độc quyền|Quyền làm hay bán một thứ chỉ dành riêng cho một bên duy nhất.
độc thân|Chưa lập gia đình, chưa có vợ hoặc chồng.
đôi ba|Một vài, số lượng ít, chừng hai ba cái.
đôi bên|Cả hai phía, hai bên có liên quan.
đội bóng|Nhóm cầu thủ cùng thi đấu bóng đá hoặc môn bóng khác.
đổi chác|Trao đổi hàng hóa, đồ vật với nhau, thường không dùng tiền.
đối chiếu|So sánh hai hay nhiều thứ với nhau để tìm điểm giống, khác.
đôi chút|Một ít, ở mức không đáng kể.
đối diện|Ở ngay trước mặt, quay mặt về phía nhau.
đối đáp|Hỏi và trả lời qua lại với nhau, như trong hát giao duyên.
đối đầu|Ở thế đối lập, trực tiếp tranh đua hay chống lại nhau.
đổi đời|Cuộc sống thay đổi hẳn, thường là trở nên khá giả hơn.
đổi giọng|Thay đổi giọng nói hay cách nói, thái độ so với lúc trước.
đội hình|Cách sắp xếp vị trí các thành viên trong một đội.
đổi hướng|Chuyển sang đi theo hướng khác hoặc cách làm khác.
đổi khác|Trở nên khác trước, không còn như cũ.
đôi khi|Thỉnh thoảng mới có, không xảy ra thường xuyên.
đôi lần|Một vài lần, không nhiều.
đối lập|Trái ngược hẳn nhau về tính chất hoặc quan điểm.
đổi lấy|Đưa một thứ đi để nhận lại một thứ khác.
đội lốt|Giả dạng làm người khác để che giấu bản chất thật.
đôi lúc|Có những lúc, thỉnh thoảng mới xảy ra.
đối mặt|Trực tiếp gặp và phải xử lý một người hay một khó khăn.
đổi mới|Thay đổi để tốt hơn, tiến bộ hơn so với trước.
đôi mươi|Tuổi khoảng hai mươi, thời thanh xuân tươi đẹp.
đội ngũ|Tập hợp những người cùng làm một công việc, một lĩnh vực.
đồi núi|Vùng đất cao nhấp nhô gồm cả đồi và núi.
đối phó|Tìm cách xử lý tình huống khó; cũng chỉ làm qua loa cho xong chuyện.
đối phương|Người hoặc bên ở phía đối lập với mình trong thi đấu, tranh luận.
đôi ta|Hai chúng mình, thường dùng giữa hai người yêu nhau.
đối tác|Người hay tổ chức cùng hợp tác làm ăn với mình.
đối thoại|Trao đổi, nói chuyện qua lại giữa hai hay nhiều người.
đối thủ|Người hay đội thi đấu, cạnh tranh với mình.
đổi tiền|Chuyển sang loại tiền khác, như ngoại tệ, tiền lẻ hay tiền mới.
đội trưởng|Người đứng đầu và dẫn dắt một đội, nhóm.
đội tuyển|Đội gồm những người giỏi được chọn ra để đi thi đấu.
đối tượng|Người hoặc vật được nhắm tới, được nói đến trong một việc nào đó.
đối với|Từ dùng để chỉ người hay việc mà lời nói, thái độ hướng tới.
đối xứng|Có hai nửa giống hệt nhau qua một đường thẳng hay điểm ở giữa.
đổi ý|Thay đổi suy nghĩ, quyết định so với lúc đầu.
đốm lửa|Chấm lửa nhỏ cháy lập lòe trong bóng tối.
đồng|Kim loại màu đỏ, dẫn điện tốt; cũng chỉ cánh đồng hoặc đơn vị tiền Việt Nam.
đồng áng|Công việc làm ruộng, cày cấy ngoài đồng nói chung.
đông bắc|Hướng nằm giữa phía đông và phía bắc.
đồng bằng|Vùng đất rộng, thấp và bằng phẳng, thuận lợi để trồng lúa.
đồng bộ|Các phần phù hợp, khớp nhau và hoạt động nhịp nhàng cùng lúc.
đồng ca|Nhiều người cùng hát chung một bài hát.
đồng cảm|Hiểu và chia sẻ được cảm xúc của người khác.
đồng cỏ|Vùng đất rộng có nhiều cỏ mọc, thường để chăn thả gia súc.
đông dân|Có rất nhiều người sinh sống trong một vùng.
đông đảo|Số người rất nhiều, cùng có mặt hoặc tham gia.
động đậy|Cử động nhẹ, nhúc nhích một chút, không nằm yên.
đồng đều|Ngang nhau, giống nhau giữa các phần, không chênh lệch.
đồng đội|Người cùng đội, cùng làm việc hay thi đấu với mình.
đông đủ|Có mặt đầy đủ mọi người, không thiếu ai.
đông đúc|Có rất nhiều người, chen chúc nhau.
đồng giá|Mọi món hàng có chung một mức giá bán.
đồng hành|Cùng đi với nhau; cũng chỉ việc cùng làm, cùng hỗ trợ nhau.
đồng hồ|Dụng cụ đo và chỉ thời gian.
đồng hương|Người cùng quê, cùng một vùng với mình.
đông lạnh|Được làm lạnh tới mức đóng băng để giữ được lâu.
đồng loạt|Tất cả cùng làm một việc vào cùng một lúc.
động lòng|Cảm thấy xúc động, thương cảm trước hoàn cảnh của ai.
động lực|Điều thúc đẩy, tạo sức mạnh để ai đó cố gắng hành động.
đồng lương|Tiền công nhận được nhờ làm việc, thường trả theo tháng.
đông nam|Hướng nằm giữa phía đông và phía nam.
động não|Suy nghĩ, vận dụng trí óc để tìm ra cách giải quyết.
đồng nghĩa|Có ý nghĩa giống hoặc gần giống nhau, thường nói về các từ ngữ.
đồng nghiệp|Người cùng làm việc chung một cơ quan hay cùng nghề.
đồng nhất|Giống hệt nhau, như một, không có gì khác biệt.
đồng phục|Quần áo may cùng kiểu cho học sinh, nhân viên một nơi.
đồng quê|Vùng nông thôn với ruộng đồng, làng xóm yên bình.
đồng ruộng|Vùng đất rộng dùng để trồng lúa và hoa màu.
động tác|Cử động của tay, chân hay cơ thể theo một kiểu nhất định.
đông tây|Phía đông và phía tây; cũng chỉ phương Đông và phương Tây.
đồng thanh|Nhiều người cùng nói hay hô lên một lúc, cùng một lời.
đồng thau|Hợp kim của đồng và kẽm, màu vàng, dùng làm đồ gia dụng, nhạc cụ.
đồng thời|Cùng một lúc; cũng dùng để nối thêm ý, như ngoài ra.
đồng tiền|Tiền bạc nói chung; cũng chỉ đơn vị tiền tệ của một quốc gia.
đồng tình|Tán thành, cùng chung ý kiến với người khác.
động từ|Từ chỉ hành động hay trạng thái, như chạy, ăn, ngủ.
động vật|Sinh vật có thể di chuyển và tự kiếm ăn, như chó, chim, cá.
động viên|Khích lệ, cổ vũ tinh thần để người khác cố gắng hơn.
đồng ý|Chấp nhận, nhận lời hoặc tán thành điều người khác nêu ra.
đột biến|Thay đổi bất ngờ và mạnh; trong sinh học là biến đổi ở gen.
đốt cháy|Dùng lửa làm cho vật bén cháy; cũng chỉ việc tiêu hao năng lượng, mỡ thừa.
đốt đèn|Thắp đèn lên để soi sáng khi trời tối.
đột ngột|Xảy ra rất nhanh, bất ngờ, không báo trước.
đột nhiên|Bỗng nhiên, xảy ra bất ngờ mà không ai đoán trước.
đột phá|Vượt qua giới hạn cũ, tạo ra bước tiến mới rõ rệt.
đỡ đầu|Nhận chăm lo, nâng đỡ và giúp đỡ một người hay một tổ chức.
đời nào|Chẳng bao giờ, dùng để nói chắc chắn việc gì không thể xảy ra.
đời người|Toàn bộ quãng thời gian sống của một con người.
đời sống|Cách sống, sinh hoạt hằng ngày của con người hay sinh vật.
đời thường|Cuộc sống hằng ngày bình dị, bên ngoài công việc hay sân khấu.
đời xưa|Thời xa xưa, những ngày trước đây rất lâu.
đơn ca|Hình thức biểu diễn chỉ có một người hát.
đơn điệu|Lặp đi lặp lại, ít thay đổi nên dễ nhàm chán.
đơn độc|Một mình, không có ai bên cạnh.
đơn giá|Giá tiền cho một đơn vị hàng hóa hay dịch vụ.
đơn giản|Dễ hiểu, dễ làm, không phức tạp.
đơn hàng|Phiếu ghi các món hàng mà khách đặt mua.
đơn lẻ|Riêng một mình, không đi theo nhóm hay bộ.
đơn phương|Chỉ xuất phát từ một bên, như tình cảm không được người kia đáp lại.
đơn sơ|Giản dị, mộc mạc, không cầu kỳ.
đơn thuần|Chỉ có một tính chất, không pha trộn gì thêm.
đu đủ|Quả có ruột vàng cam, vị ngọt, nhiều hạt đen bên trong.
đu đưa|Lắc qua lắc lại nhẹ nhàng khi treo lơ lửng.
đu quay|Trò chơi ở công viên có ghế ngồi quay tròn liên tục.
đùa cợt|Nói đùa, trêu chọc một cách thiếu nghiêm túc.
đùa dai|Trêu đùa quá lâu, kéo dài đến mức người khác khó chịu.
đua đòi|Bắt chước người khác một cách thiếu suy nghĩ, chạy theo sự xa hoa.
đùa giỡn|Vui đùa, trêu chọc nhau cho vui.
đùa nghịch|Chơi đùa, nghịch ngợm, thường nói về trẻ con.
đua ngựa|Môn thi cưỡi ngựa chạy xem ai về đích trước.
đua thuyền|Cuộc thi chèo thuyền xem đội nào về đích trước.
đục ngầu|Rất đục, vẩn nhiều bùn đất, không nhìn thấy đáy.
đun nấu|Nhóm bếp, đun nước và nấu thức ăn nói chung.
đúng đắn|Hợp lý, phù hợp với lẽ phải.
đung đưa|Chuyển động nhẹ qua lại như võng, cành cây trước gió.
đúng giờ|Có mặt hoặc làm việc đúng thời gian đã hẹn.
đúng hạn|Hoàn thành hoặc nộp trong thời hạn quy định.
đúng hẹn|Giữ lời, đến hoặc làm đúng như đã hẹn.
đúng hướng|Đi theo con đường phù hợp, dẫn tới mục tiêu mong muốn.
đúng lúc|Vào thời điểm thích hợp nhất.
đuốc|Bó vật dễ cháy được đốt lên để soi đường.
đuôi|Phần cuối thân con vật, thò ra phía sau; cũng chỉ phần cuối của vật.
đuôi gà|Kiểu buộc tóc túm cao phía sau đầu, trông như đuôi gà.
đuổi kịp|Theo sau và bắt kịp người đi trước.
đuôi sam|Kiểu tóc tết thành dải dài thả sau lưng.
đuổi theo|Chạy theo sau để bắt hoặc để theo kịp.
đứa bé|Em nhỏ còn ít tuổi, cần người lớn chăm sóc.
đưa đò|Chèo đò chở người qua sông.
đưa đón|Chở ai đó đi rồi đón về, như cha mẹ chở con tới trường.
đưa ra|Nêu ra, trình bày; cũng là trao ra cho người khác.
đưa tay|Giơ tay ra phía trước để cầm, chào hoặc giúp đỡ.
đưa tin|Thông báo, truyền đi những sự việc mới xảy ra.
đưa vào|Cho vào bên trong; cũng chỉ việc bắt đầu áp dụng.
đức tính|Nét tính cách tốt đẹp của một người, như thật thà, chăm chỉ.
đứng|Ở tư thế thân thẳng, hai chân chạm đất đỡ cả người.
đừng có|Lời nói để ngăn, bảo ai không được làm việc gì.
đứng dậy|Chuyển từ tư thế ngồi hay nằm sang tư thế đứng.
đứng đầu|Ở vị trí cao nhất, dẫn đầu; cũng chỉ người lãnh đạo một nơi.
đứng im|Giữ nguyên một chỗ, không cử động hay nhúc nhích.
đứng lại|Dừng bước, không đi tiếp nữa.
đứng lên|Chuyển từ ngồi, nằm sang đứng; cũng chỉ việc vượt lên sau vấp ngã.
đứng ra|Tự mình nhận làm, chịu trách nhiệm một việc chung.
đứng thẳng|Giữ lưng và chân thẳng khi đứng, không cúi khom hay nghiêng.
đứng tuổi|Đã có tuổi, không còn trẻ nhưng chưa già.
đứng vững|Giữ thăng bằng chắc chắn, không bị ngã; cũng chỉ việc trụ được trước khó khăn.
đứng yên|Ở nguyên một chỗ, không di chuyển; cũng chỉ sự việc không thay đổi.
được lòng|Nhận được sự yêu mến, tin cậy của người khác.
được mùa|Thu hoạch nhiều, mùa màng bội thu.
được việc|Làm việc giỏi, đáng tin cậy, giao gì cũng hoàn thành.
đười ươi|Loài vượn lớn lông nâu đỏ, tay dài, sống trên cây ở rừng nhiệt đới.
đường|Lối đi để người và xe qua lại; cũng là chất ngọt làm từ mía.
đường bay|Tuyến bay của máy bay giữa hai nơi.
đường băng|Dải đường dài, phẳng ở sân bay cho máy bay cất và hạ cánh.
đường biển|Tuyến đi lại, vận chuyển trên biển bằng tàu thuyền.
đường bộ|Hệ thống đường đi trên đất liền dành cho người và xe cộ.
đường cao|Đoạn thẳng kẻ từ một đỉnh tam giác vuông góc xuống cạnh đối diện.
đường chéo|Đoạn thẳng nối hai góc đối diện của một hình.
đường cong|Nét vẽ hoặc lối đi uốn lượn, không thẳng.
đường dài|Hành trình xa, phải đi mất nhiều thời gian.
đường dẫn|Lối dẫn vào một nơi; trên máy tính là địa chỉ để mở trang hoặc tệp.
đường dây|Hệ thống dây dẫn điện, điện thoại nối giữa các nơi.
đương đầu|Dũng cảm đối mặt với khó khăn, thử thách.
đường đi|Lối để đi từ nơi này đến nơi khác.
đường hầm|Lối đi đào xuyên qua núi hoặc dưới lòng đất.
đường hẻm|Con đường nhỏ hẹp nằm sâu giữa các dãy nhà.
đường kính|Đoạn thẳng qua tâm nối hai điểm trên đường tròn; cũng là loại đường ăn hạt trắng.
đường làng|Con đường nhỏ đi trong làng quê.
đường mòn|Lối đi nhỏ hình thành do nhiều người đi lại lâu ngày.
đường nét|Những nét vẽ, đường viền tạo nên hình dáng.
đương nhiên|Hiển nhiên phải như thế, không cần bàn cãi.
đường nhựa|Con đường được rải lớp nhựa đen, mặt phẳng và chắc.
đường ống|Hệ thống ống dẫn nước, khí hoặc dầu.
đường phèn|Loại đường kết tinh thành cục trong suốt, vị ngọt thanh.
đường phố|Con đường trong thành phố, hai bên có nhà cửa.
đường sắt|Hệ thống ray thép và nhà ga phục vụ tàu hỏa chạy.
đường tàu|Lối ray thép mà tàu hỏa chạy trên đó.
đường tắt|Lối đi ngắn hơn đường chính; cũng chỉ cách làm nhanh hơn bình thường.
đường thẳng|Nét kéo dài theo một hướng, không cong, không gấp khúc.
đường trắng|Loại đường ăn màu trắng, đã được tinh chế từ mía.
đường tròn|Hình gồm các điểm cách đều một tâm.
đường viền|Nét chạy dọc theo mép để trang trí hoặc làm nổi bật hình.
đường vòng|Lối đi vòng xa hơn, không đi thẳng.
đường xa|Quãng đường cách xa, phải đi lâu mới tới.
đứt quãng|Bị ngắt ra từng đoạn, không liên tục.
e ngại|Ngần ngại, lo lắng nên chưa dám nói hay làm.
e rằng|Cách nói tỏ ý lo ngại rằng điều không mong muốn có thể xảy ra.
em bé|Đứa trẻ nhỏ, thường còn ẵm ngửa hoặc mới biết đi.
em chồng|Em trai hoặc em gái của người chồng.
em dâu|Vợ của em trai mình.
em gái|Người con gái sinh sau mình trong cùng gia đình hoặc họ hàng.
em họ|Người cùng họ hàng nhưng khác cha mẹ, vai vế nhỏ hơn mình.
em rể|Người chồng của em gái mình.
em ruột|Người em cùng cha mẹ sinh ra với mình.
em trai|Người con trai sinh sau mình trong cùng gia đình.
em út|Người con nhỏ tuổi nhất trong gia đình.
em vợ|Em trai hoặc em gái của người vợ.
eo biển|Dải biển hẹp nằm giữa hai vùng đất, nối liền hai vùng biển.
ép buộc|Bắt người khác làm điều họ không muốn.
ếch nhái|Các loài lưỡng cư nhỏ nhảy giỏi, sống ở ao, ruộng, kêu vào mùa mưa.
êm ái|Mềm mại, nhẹ nhàng, tạo cảm giác dễ chịu.
êm ấm|Hòa thuận, ấm cúng, thường nói về cuộc sống gia đình.
êm dịu|Nhẹ nhàng và dễ chịu, không gay gắt.
êm đẹp|Tốt đẹp, yên ổn, không có xích mích hay rắc rối.
êm đềm|Yên tĩnh, nhẹ nhàng, trôi qua một cách bình lặng.
êm tai|Nghe nhẹ nhàng, dễ chịu, không chói tai.
êm xuôi|Mọi việc diễn ra suôn sẻ, không gặp trục trặc.
gà con|Gà mới nở, còn nhỏ, toàn thân phủ lông tơ mềm.
gà gáy|Tiếng gà trống gáy; cũng chỉ lúc sáng sớm tinh mơ.
gà mái|Gà cái, được nuôi để đẻ trứng và ấp con.
gà quay|Món gà nguyên con tẩm ướp rồi quay trên lửa cho da vàng giòn.
gà rừng|Loài gà sống hoang trong rừng, nhỏ con, nhanh nhẹn, lông sặc sỡ.
gà tây|Loài gà rất to gốc châu Mỹ, con trống hay xòe đuôi như quạt.
gà trống|Gà đực, mào đỏ, hay gáy vào buổi sáng.
gà vịt|Gà và vịt, chỉ chung các loại gia cầm nuôi trong nhà.
gác lửng|Tầng sàn nhỏ làm thêm ở lưng chừng giữa nền và trần nhà.
gạch|Viên đất nung hoặc xi măng dùng để xây nhà; cũng là kẻ một đường thẳng.
gạch bỏ|Kẻ đường ngang lên chữ viết để xóa, loại bỏ đi.
gạch lát|Loại gạch phẳng dùng để lát nền nhà, sân hoặc lối đi.
gạch men|Loại gạch phủ lớp men bóng, dùng để lát nền hoặc ốp tường.
gạch ngang|Dấu nét ngang ngắn trong văn bản, dùng để nối từ hoặc mở đầu lời thoại.
gai góc|Có nhiều gai; cũng chỉ việc khó khăn, phức tạp hoặc tính cách cứng cỏi, khó gần.
gãi ngứa|Dùng móng tay cào nhẹ lên chỗ da bị ngứa.
gan dạ|Can đảm, không sợ hãi trước khó khăn nguy hiểm.
gan gà|Lá gan của con gà, chế biến thành món ăn như xào, rim.
gán ghép|Cố ghép đôi hai người với nhau; cũng chỉ việc gán cho điều không đúng.
gang|Hợp kim sắt dùng đúc nồi, chảo; cũng là độ dài bàn tay xòe.
gánh|Mang đồ treo ở hai đầu đòn đặt trên vai; cũng là đảm nhận việc nặng.
gánh chịu|Phải nhận lấy và chịu đựng điều không hay hoặc trách nhiệm.
gánh hàng|Đôi quang gánh đựng hàng hóa để đi bán rong.
gánh nặng|Trách nhiệm hoặc nỗi lo lớn mà một người phải mang.
gánh vác|Nhận lấy và đảm đương công việc, trách nhiệm quan trọng.
gáo dừa|Gáo múc nước làm từ nửa vỏ quả dừa khô, có cán cầm.
gạo nếp|Loại gạo hạt trắng đục, nấu lên dẻo, dùng nấu xôi, gói bánh.
gạo tẻ|Loại gạo thường để nấu cơm hằng ngày, không dẻo như gạo nếp.
gào thét|Kêu la rất to và dữ dội; cũng dùng tả tiếng gió, sóng mạnh.
gara|Nhà để ô tô; cũng chỉ xưởng sửa chữa, bảo dưỡng xe.
gạt bỏ|Loại ra, bỏ sang một bên, không để tâm đến nữa.
gay gắt|Quyết liệt, căng thẳng, thiếu ôn hòa; cũng nói nắng nóng rất mạnh.
gay go|Căng thẳng, nhiều khó khăn, khó vượt qua.
gắn liền|Có quan hệ chặt chẽ, khó tách rời nhau.
găng tay|Đồ bằng vải, len hoặc da đeo vào để che, giữ ấm bàn tay.
gặp gỡ|Cùng có mặt để trò chuyện, giao lưu với nhau.
gặp may|Tình cờ được hưởng điều tốt lành.
gặp mặt|Trực tiếp thấy và nói chuyện với nhau.
gặp phải|Bất ngờ vướng vào chuyện khó khăn, không mong muốn.
gắt gao|Rất nghiêm ngặt, quyết liệt, không nới lỏng chút nào.
gắt gỏng|Hay cáu, nói năng to tiếng, khó chịu với người khác.
gặt hái|Thu được thành quả sau quá trình cố gắng; nghĩa gốc là thu hoạch lúa.
gầm gừ|Tiếng kêu trầm trong cổ họng của chó, mèo khi tức giận; cũng chỉ người cáu kỉnh.
gầm rú|Phát ra tiếng gầm to, vang dữ dội như thú lớn hoặc động cơ.
gân bò|Phần gân dai giòn của con bò, thường dùng nấu phở hoặc hầm.
gần đây|Khoảng thời gian vừa mới qua; cũng chỉ nơi ở cách không xa.
gần gũi|Có quan hệ thân thiết, gắn bó; cũng chỉ điều quen thuộc, giản dị.
gần như|Xấp xỉ, chỉ thiếu một chút nữa là đúng hoàn toàn.
gần xa|Khắp mọi nơi, cả chỗ gần lẫn chỗ xa.
gấp đôi|Nhiều bằng hai lần; cũng là gập một vật thành hai nửa.
gấp gáp|Vội vàng, khẩn trương vì còn ít thời gian.
gập ghềnh|Mặt đường cao thấp, lồi lõm, không bằng phẳng, khó đi.
gật đầu|Cúi đầu xuống rồi ngẩng lên để tỏ ý đồng ý hoặc chào.
gật gù|Gật đầu nhẹ nhiều lần, tỏ ý đồng tình hoặc thích thú.
gấu chó|Loài gấu nhỏ nhất, lông đen, ngực có mảng lông vàng hình chữ U.
gấu đen|Loài gấu lông đen, ngực thường có vệt lông sáng hình trăng khuyết.
gâu gâu|Từ mô phỏng tiếng chó sủa.
gấu mèo|Loài thú nhỏ lông xám, có vệt đen quanh mắt như đeo mặt nạ, đuôi khoang.
gấu trúc|Loài gấu lông trắng đen, sống ở Trung Quốc, chủ yếu ăn tre trúc.
gầy còm|Gầy gò, nhỏ thó, trông thiếu sức sống.
gầy nhom|Rất gầy, trông như chỉ có da bọc xương.
gây sốt|Thu hút sự quan tâm, bàn tán rầm rộ của nhiều người trong một thời gian.
gầy yếu|Thân hình gầy, sức khỏe kém, trông thiếu sức lực.
ghen|Khó chịu khi người yêu để ý người khác hoặc thấy ai hơn mình.
ghép|Nối, gắn các phần riêng lẻ lại với nhau thành một.
ghép cặp|Xếp hai người hoặc hai vật thành một đôi.
ghép đôi|Xếp hai người hay hai vật thành một cặp; cũng là mai mối.
ghế dài|Ghế có mặt ngồi dài, đủ chỗ cho nhiều người cùng ngồi.
ghế dựa|Loại ghế có chỗ tựa lưng phía sau.
ghế đẩu|Ghế nhỏ, không có lưng tựa, mặt ngồi tròn hoặc vuông.
ghê gớm|Ở mức rất cao, đáng nể hoặc đáng sợ; cũng chỉ người rất lợi hại.
ghế mây|Ghế đan bằng sợi mây, nhẹ và thoáng.
ghế phụ|Ghế kê thêm khi thiếu chỗ; cũng chỉ ghế ngồi cạnh người lái xe.
ghế tựa|Ghế có phần lưng cao để tựa vào khi ngồi.
ghế vải|Ghế có khung gấp gọn được, mặt ngồi bằng vải căng.
ghế xoay|Ghế có trục giúp mặt ngồi xoay tròn, hay dùng ở văn phòng.
ghi âm|Thu lại âm thanh, giọng nói bằng thiết bị để nghe lại.
ghi bàn|Đưa bóng vào lưới đối phương để có điểm, nhất là trong bóng đá.
ghi chép|Viết lại những điều nghe, thấy hoặc cần nhớ.
ghi chú|Viết thêm vài dòng để nhắc nhở hoặc giải thích; cũng là dòng chữ đó.
ghi đông|Thanh tay lái phía trước của xe đạp, xe máy.
ghi hình|Quay lại hình ảnh bằng máy quay hoặc điện thoại.
ghi nhận|Công nhận công sức, thành tích của ai; cũng là ghi lại điều đã thấy.
ghi nhớ|Giữ kỹ trong trí nhớ, không để quên.
ghi rõ|Viết rõ ràng, cụ thể để người khác dễ đọc, dễ hiểu.
ghi tên|Viết tên mình vào danh sách để đăng ký tham gia.
ghim|Kim nhỏ hoặc kẹp nhỏ dùng cài giữ giấy, vải; cũng là cài, gắn cố định.
giá bán|Số tiền người bán đưa ra cho một món hàng.
giả bộ|Làm ra vẻ như thật để người khác tin.
giá cả|Mức giá của hàng hóa, dịch vụ nói chung.
gia cầm|Các loài chim được nuôi trong nhà như gà, vịt, ngan.
gia cố|Làm cho nhà cửa, công trình chắc chắn và chịu lực tốt hơn.
gia công|Làm hàng theo đơn đặt của người khác; cũng là chế biến, xử lý vật liệu.
giả dạng|Đóng giả thành người khác để không bị nhận ra.
già dặn|Chín chắn, có nhiều kinh nghiệm hơn so với tuổi.
giả dối|Không thật lòng, hay nói dối, lừa người khác.
gia dụng|Dùng hằng ngày trong gia đình, như nồi cơm điện, quạt máy.
gia đình|Những người cùng chung sống, gắn bó như ông bà, cha mẹ, con cái.
gia hạn|Kéo dài thêm thời hạn đã định, như hạn thẻ hay hợp đồng.
giá lạnh|Rất lạnh, rét buốt, thường nói về thời tiết mùa đông.
giá mà|Lời bày tỏ mong ước về điều không có thật hoặc đã lỡ.
giá như|Lời bày tỏ tiếc nuối, mong một điều đã xảy ra khác đi.
già nua|Đã rất già, mang dáng vẻ yếu ớt, cằn cỗi.
giá rét|Trời lạnh buốt, nhiệt độ xuống rất thấp.
giá sách|Kệ có nhiều ngăn để đặt sách.
gia súc|Các loài thú được nuôi trong nhà như trâu, bò, lợn.
gia sư|Người dạy kèm học sinh tại nhà.
gia tài|Toàn bộ của cải của một người hoặc gia đình.
giả tạo|Không tự nhiên, cố làm ra vẻ để che giấu thật lòng.
gia tăng|Tăng thêm, nhiều lên so với trước.
giá thành|Tổng chi phí bỏ ra để làm ra một sản phẩm hay dịch vụ.
gia tộc|Những gia đình cùng chung một dòng họ, cùng tổ tiên.
giá trị|Mức độ quý báu, hữu ích của một thứ; cũng là số tiền nó đáng.
gia truyền|Được truyền lại từ đời này sang đời khác trong một gia đình.
gia trưởng|Người đứng đầu gia đình; thường chỉ người áp đặt, độc đoán trong nhà.
giả tưởng|Được tưởng tượng ra, không có thật, như phim, truyện về thế giới kỳ ảo.
giá vẽ|Khung có chân để đặt tranh khi vẽ.
giả vờ|Làm ra vẻ như thật, dù thực ra không phải vậy.
già yếu|Tuổi đã cao, sức khỏe yếu đi.
giác quan|Các cơ quan giúp cảm nhận thế giới như mắt, tai, mũi, lưỡi, da.
giải|Phần thưởng cho người thắng cuộc thi; cũng là tìm lời đáp cho bài toán.
giải cứu|Cứu ra khỏi tình trạng nguy hiểm hay khó khăn.
giải đáp|Trả lời, giải thích những thắc mắc.
giai điệu|Chuỗi âm thanh cao thấp nối nhau, tạo nên phần chính của bài hát.
giai đoạn|Một khoảng thời gian trong quá trình phát triển của sự việc.
giải khát|Uống cho đỡ khát, thường bằng nước mát hoặc đồ uống ngọt.
giải lao|Nghỉ ngơi ngắn giữa giờ học hay giờ làm.
giải mã|Tìm ra ý nghĩa điều bí ẩn, hoặc đổi mật mã thành nội dung đọc được.
giải nghĩa|Nói rõ nghĩa của từ ngữ hay câu văn cho người khác hiểu.
giải nhiệt|Làm cho bớt nóng, mát người, như uống nước mát hay đi bơi.
giải pháp|Cách giải quyết một vấn đề khó khăn.
giải quyết|Tìm cách làm cho xong, xử lý ổn thỏa một việc.
giải tán|Thôi tụ họp, mỗi người đi một ngả; cũng là xóa bỏ một tổ chức.
giải thích|Nói rõ lý do, ý nghĩa để người khác hiểu.
giải thoát|Làm cho thoát khỏi sự ràng buộc hay tình trạng khó chịu.
giải thưởng|Phần thưởng trao cho người đạt thành tích trong cuộc thi.
giải trí|Nghỉ ngơi, vui chơi cho thư giãn đầu óc.
giảm|Làm cho ít đi, nhỏ đi hoặc thấp xuống so với trước.
giảm bớt|Làm cho ít đi, nhẹ đi một phần so với trước.
giảm dần|Ít đi từng chút một theo thời gian.
giám đốc|Người đứng đầu, điều hành một công ty hay cơ quan.
giảm giá|Hạ giá bán xuống thấp hơn mức ban đầu.
giám hiệu|Ban lãnh đạo nhà trường, gồm hiệu trưởng và các phó hiệu trưởng.
giám khảo|Người chấm điểm, đánh giá bài thi hay phần thi.
giảm nhẹ|Làm cho bớt nặng nề, bớt nghiêm trọng.
giám sát|Theo dõi, kiểm tra xem công việc có làm đúng không.
giảm sút|Kém đi, đi xuống so với trước, như sức khỏe hay kết quả.
giám thị|Người coi thi; cũng là người theo dõi nề nếp học sinh ở trường.
giảm thiểu|Làm giảm đến mức thấp nhất có thể.
giảm tốc|Làm cho tốc độ chậm lại, thường nói về xe cộ.
gián|Côn trùng có cánh màu nâu bóng, hay sống ở chỗ ẩm, tối trong nhà.
gián đoạn|Bị ngắt quãng giữa chừng, không liền mạch.
gian hàng|Khu vực nhỏ để bày bán hàng trong chợ, hội chợ hay siêu thị.
gian nan|Khó khăn, vất vả, nhiều thử thách.
gián tiếp|Thông qua người hay vật trung gian, không trực tiếp.
giảng|Giải thích, trình bày bài học hay một vấn đề cho người khác hiểu.
giảng dạy|Dạy và truyền đạt kiến thức cho học sinh, sinh viên.
giảng đường|Phòng học lớn ở trường đại học, nơi nhiều sinh viên nghe giảng.
giảng giải|Giải thích kỹ lưỡng, cặn kẽ để người khác hiểu.
giảng viên|Người dạy ở trường đại học, cao đẳng.
giao|Trao vật hay việc cho người khác nhận lấy hoặc phụ trách.
giao dịch|Việc mua bán, trao đổi hay chuyển tiền giữa các bên.
giao diện|Phần hiện trên màn hình để người dùng thao tác với máy, ứng dụng.
giao du|Kết bạn, qua lại và chơi với người khác.
giáo dục|Dạy dỗ, rèn luyện để con người phát triển về trí tuệ và nhân cách.
giao hưởng|Bản nhạc lớn do dàn nhạc nhiều nhạc cụ cùng trình diễn.
giao hữu|Thi đấu để thắt chặt tình hữu nghị, không nặng về thắng thua.
giao kèo|Thỏa thuận hay lời cam kết giữa các bên với nhau.
giáo khoa|Chỉ sách học chính thức dùng trong nhà trường.
giao lộ|Nơi hai hay nhiều con đường gặp nhau.
giao lưu|Gặp gỡ, trao đổi để hiểu biết và học hỏi lẫn nhau.
giao nhận|Việc giao và nhận hàng hóa, giấy tờ giữa các bên.
giáo sư|Chức danh cao nhất dành cho nhà khoa học, giảng viên đại học.
giao thiệp|Tiếp xúc, quan hệ qua lại với mọi người trong xã hội.
giao thông|Việc đi lại, vận chuyển người và hàng hóa trên đường.
giao tiếp|Trò chuyện, trao đổi thông tin, tình cảm với người khác.
giáo trình|Tài liệu dạy học được soạn cho một môn hay một khóa học.
giáo viên|Người dạy học ở trường phổ thông hoặc mầm non.
giáp|Ở sát bên cạnh, như nhà giáp chợ; cũng chỉ áo giáp che chắn cơ thể.
giàu|Có nhiều tiền của; cũng chỉ có nhiều thứ gì đó, như giàu tình cảm.
giàu có|Có rất nhiều tiền bạc, tài sản, cuộc sống sung túc.
giàu sang|Vừa có nhiều của cải vừa có địa vị cao trong xã hội.
giàu sụ|Rất giàu, có rất nhiều tiền của.
giằng co|Kéo qua kéo lại giữa hai bên, chưa bên nào hơn.
giặt|Làm sạch quần áo, vải vóc bằng nước và xà phòng.
giặt khô|Cách giặt dùng hóa chất thay nước, thường cho đồ len, dạ dễ hỏng.
giặt là|Làm sạch rồi ủi phẳng quần áo; cũng chỉ dịch vụ làm việc này.
giấc|Một lần ngủ liền mạch từ lúc thiếp đi đến khi tỉnh dậy.
giấc mộng|Những gì thấy trong khi ngủ; cũng chỉ ước vọng lớn lao, đẹp đẽ.
giấc mơ|Những hình ảnh thấy được khi ngủ; cũng chỉ ước mơ, khát vọng.
giấc ngủ|Khoảng thời gian ngủ, lúc cơ thể và đầu óc được nghỉ ngơi.
giận dỗi|Tỏ ra hờn giận, không vui để người khác chú ý, dỗ dành.
giận hờn|Giận dỗi, tỏ ý không vui với người mình thân thiết.
giật gân|Gây cảm giác mạnh, kích thích tò mò, như tin tức giật gân.
giật lùi|Đi lùi về phía sau; cũng chỉ sự tụt lại, kém hơn trước.
giật mình|Bất ngờ hoảng hốt vì tiếng động hay chuyện xảy ra đột ngột.
giấy|Vật liệu mỏng làm từ bột gỗ hoặc tre, dùng để viết, in, gói.
giấy ăn|Loại giấy mềm, mỏng dùng để lau miệng, lau tay khi ăn.
giấy bạc|Tờ tiền giấy; cũng chỉ lá nhôm mỏng dùng gói thức ăn.
giấy báo|Tờ thông báo gửi đến người nhận; cũng chỉ giấy in báo, báo cũ.
giấy bọc|Giấy dùng để gói, bọc đồ vật hoặc bọc sách vở.
giấy gói|Loại giấy dùng để bọc quà hoặc gói đồ vật.
giấy in|Loại giấy trắng dùng để in tài liệu bằng máy in.
giấy khen|Giấy chứng nhận khen thưởng vì có thành tích tốt.
giây lát|Khoảng thời gian rất ngắn, chỉ trong chốc lát.
giấy lộn|Giấy cũ đã viết hoặc dùng rồi, không còn cần nữa.
giấy mời|Thiếp hoặc tờ giấy ghi lời mời đến dự một buổi lễ, cuộc họp.
giấy nhám|Loại giấy phủ lớp hạt ráp, dùng để chà nhẵn bề mặt gỗ, kim loại.
giấy nháp|Giấy dùng để viết thử, tính toán trước khi viết chính thức.
giấy phép|Văn bản do cơ quan có thẩm quyền cấp, cho phép làm một việc.
giây phút|Khoảng thời gian ngắn, thường là thời khắc đáng nhớ.
giấy thiếc|Lá kim loại mỏng như giấy, sáng bạc, dùng gói đồ ăn hoặc nướng.
giấy tờ|Các loại giấy có giá trị pháp lý như hồ sơ, chứng từ, căn cước.
giấy vẽ|Loại giấy dày, mặt nhẵn, dùng để vẽ tranh.
giấy vụn|Những mẩu giấy nhỏ vụn hoặc giấy cũ bỏ đi.
giẻ lau|Mảnh vải cũ dùng để lau chùi.
gieo|Rải hạt giống xuống đất cho nảy mầm, mọc thành cây.
gieo trồng|Rải hạt giống, trồng cây con để chăm sóc và thu hoạch.
giếng|Hố đào sâu xuống lòng đất để lấy nước ngầm dùng hằng ngày.
giếng khoan|Loại giếng làm bằng cách khoan ống sâu xuống đất rồi bơm nước ngầm lên.
gìn giữ|Chăm lo bảo vệ cẩn thận để còn được lâu dài.
gió giật|Gió thổi mạnh từng cơn đột ngột rồi lại yếu đi.
giò heo|Phần chân con heo, hay dùng để hầm, luộc hoặc nấu bánh canh.
giò lụa|Món làm từ thịt lợn giã nhuyễn, gói lá chuối rồi luộc chín.
gió mây|Gió và mây trên trời, thường gợi cảnh thiên nhiên bay bổng.
gió mùa|Gió thổi theo mùa, đổi hướng giữa mùa hè và mùa đông.
gió xoáy|Luồng gió xoay tròn rất mạnh, cuốn theo bụi và vật nhẹ.
giỏi|Có khả năng học tập hoặc làm việc tốt hơn mức bình thường.
giỏi giang|Có năng lực, tháo vát, làm tốt được nhiều việc.
giọng|Tiếng phát ra khi nói, hát; cũng chỉ cách phát âm của từng vùng.
giọng điệu|Cách nói thể hiện thái độ, cảm xúc của người nói hoặc người viết.
giọng hát|Chất giọng và cách thể hiện của một người khi cất tiếng hát.
giọng nói|Âm thanh riêng của mỗi người phát ra khi nói chuyện.
giọt|Lượng nhỏ chất lỏng tụ lại thành hạt tròn, rơi xuống hoặc đọng lại.
giọt nắng|Tia nắng nhỏ lọt qua kẽ lá, cách nói giàu hình ảnh trong văn thơ.
giọt sương|Hạt nước nhỏ li ti đọng trên lá, cỏ vào ban đêm hoặc sáng sớm.
giống hệt|Y như nhau, không có điểm nào khác biệt.
giống như|Dùng để so sánh, chỉ hai sự vật có nét tương tự nhau.
giờ ăn|Khoảng thời gian dành cho bữa ăn trong ngày.
giờ chơi|Khoảng nghỉ giữa các tiết học để học sinh vui chơi, thư giãn.
giờ đây|Vào lúc này, ở thời điểm hiện tại so với trước kia.
giờ giấc|Thời gian biểu cho việc ăn, ngủ, làm việc trong ngày nói chung.
giờ nghỉ|Khoảng thời gian tạm dừng học hoặc làm việc để nghỉ ngơi.
giờ phút|Khoảnh khắc, thời điểm, thường là lúc quan trọng hay đáng nhớ.
giới hạn|Mức hoặc phạm vi không được vượt qua; cũng là việc đặt ra mức ấy.
giới thiệu|Làm cho người khác biết đến một người, một vật hoặc một điều gì đó.
giun|Con vật nhỏ thân dài, mềm, không chân, thường sống trong đất ẩm.
giun đất|Loài giun sống trong đất, đào hang giúp đất tơi xốp.
giúp|Góp sức làm cho người khác đỡ vất vả hoặc đạt được việc.
giúp đỡ|Góp công sức, tiền bạc hoặc tinh thần để người khác vượt qua khó khăn.
giúp ích|Mang lại lợi ích, có ích cho ai hoặc việc gì.
giúp sức|Góp thêm sức lực để hỗ trợ người khác.
giúp việc|Làm việc nhà thuê cho gia đình khác; cũng chỉ người làm nghề này.
giữ chặt|Cầm hoặc nắm thật chắc, không để tuột hay rời ra.
giữ chân|Tìm cách làm cho người khác ở lại, không rời đi, như giữ chân khách hàng.
giữ gìn|Chăm sóc, bảo vệ cẩn thận để không bị hư hỏng hay mất đi.
giữ lại|Không bỏ đi mà để lại bên mình; cũng là không cho ai rời đi.
giữ lời|Làm đúng như điều mình đã hứa với người khác.
giữ nguyên|Để y như cũ, không thay đổi gì.
giữ nhiệt|Làm cho nhiệt độ bên trong không bị thất thoát, như bình giữ nhiệt.
giữ trẻ|Trông nom, chăm sóc trẻ nhỏ thay cho cha mẹ.
giữ vững|Bảo vệ cho chắc chắn, ổn định, không để lung lay hay suy giảm.
giữa|Chỗ ở khoảng trung tâm, cách đều hai bên hoặc hai đầu.
giữa chừng|Lúc việc đang làm dở, chưa đến hồi kết thúc.
giường|Đồ dùng có mặt phẳng kê cao để nằm ngủ.
gò bó|Bị ràng buộc, hạn chế, không được tự do thoải mái.
gõ cửa|Đập nhẹ tay vào cánh cửa để báo cho người bên trong biết.
gõ kiến|Loài chim có mỏ cứng, hay mổ vào thân cây để tìm sâu.
gò má|Phần xương nhô cao ở hai bên má, ngay dưới mắt.
góc cạnh|Có nhiều góc và cạnh rõ nét; cũng chỉ các khía cạnh của một vấn đề.
góc độ|Cách nhìn, khía cạnh để xem xét vấn đề; cũng là độ lớn của một góc.
góc nhà|Khoảng nhỏ trong nhà, nơi hai bức tường gặp nhau.
góc nhọn|Góc nhỏ hơn góc vuông, tức là dưới chín mươi độ.
góc phố|Chỗ hai con phố gặp nhau; cũng chỉ một khoảng nhỏ trên phố.
góc quay|Vị trí và hướng đặt máy khi quay phim hoặc chụp ảnh.
góc vuông|Loại góc bằng chín mươi độ, như các góc của hình vuông.
gói ghém|Thu xếp, bọc lại đồ đạc cho gọn gàng; cũng là chi tiêu tằn tiện.
gọi là|Có tên là, được xem là; cũng dùng khi nói làm chút ít cho có.
gom góp|Thu nhặt dần từng ít một để có nhiều.
gọn gàng|Ngăn nắp, sạch sẽ, không bừa bộn.
gọn nhẹ|Nhỏ, nhẹ, dễ mang theo; cũng là đơn giản, không rườm rà.
góp mặt|Có mặt, tham gia vào một sự kiện hay hoạt động.
góp phần|Đóng góp một phần công sức vào việc chung hoặc thành quả chung.
góp sức|Bỏ công sức cùng mọi người làm việc chung.
góp vui|Cùng tham gia cho cuộc vui thêm phần vui vẻ.
góp ý|Nêu ý kiến của mình để giúp người khác làm tốt hơn.
gót chân|Phần tròn ở phía sau cùng của bàn chân.
gồ ghề|Bề mặt lồi lõm, chỗ cao chỗ thấp, không bằng phẳng.
gỗ lim|Loại gỗ quý rất cứng và nặng, màu nâu sẫm, bền lâu.
gốc gác|Nguồn gốc xuất thân, quê quán của một người.
gốc rễ|Phần gốc và rễ của cây; cũng chỉ nguyên nhân sâu xa của sự việc.
gối đầu|Kê đầu lên một vật khi nằm; cũng chỉ chiếc gối để kê đầu.
gối ôm|Gối dài để ôm khi nằm ngủ.
gối tựa|Gối dùng để kê lưng hoặc tựa khi ngồi.
gỡ rối|Tháo những chỗ bị rối ra; cũng là giúp giải quyết điều khó khăn, vướng mắc.
gợi chuyện|Mở lời, khơi ra câu chuyện để người khác cùng trò chuyện.
gợi ý|Nêu ra một ý nhỏ để người khác dựa vào mà suy nghĩ, lựa chọn.
gợn sóng|Mặt nước lăn tăn những làn sóng nhỏ; cũng chỉ tóc hơi xoăn nhẹ.
guốc|Dép đế gỗ hoặc đế cao, có quai ngang để xỏ chân.
gừng|Cây có củ vị cay nồng, thơm, dùng làm gia vị và giữ ấm cơ thể.
gương|Vật có mặt nhẵn bóng để soi; cũng chỉ người, việc tốt đáng noi theo.
gượng ép|Miễn cưỡng, bị ép buộc nên thiếu tự nhiên.
gượng gạo|Thiếu tự nhiên, như phải cố gắng làm cho có.
gương mặt|Khuôn mặt của một người; cũng chỉ người nổi bật trong một lĩnh vực.
gương mẫu|Có lời nói, việc làm tốt đáng để người khác noi theo.
gương sáng|Người hoặc việc làm tốt, đáng để người khác noi theo.
hạ cánh|Đáp xuống mặt đất, nói về máy bay hoặc chim.
hạ giá|Giảm giá bán xuống thấp hơn trước.
hạ giọng|Nói nhỏ lại, giọng nhẹ nhàng và êm hơn.
ha ha|Từ mô phỏng tiếng cười to, vui vẻ, sảng khoái.
hả hê|Vui sướng, thỏa mãn khi được như ý muốn.
hà mã|Loài thú rất to sống ở sông hồ châu Phi, miệng rộng, da dày.
hạ màn|Kéo màn xuống để kết thúc buổi diễn; cũng là kết thúc một sự kiện.
há miệng|Mở rộng miệng ra, như khi ngáp hoặc khi ăn.
hạ mình|Tự hạ thấp địa vị, lòng tự trọng để chiều theo người khác.
hạ tầng|Hệ thống công trình phục vụ chung như đường sá, điện, nước, viễn thông.
hạ thấp|Làm cho thấp xuống; cũng là coi thường, xem nhẹ giá trị.
hải âu|Loài chim biển cánh dài, bay lượn giỏi trên mặt biển.
hải cẩu|Thú biển thân tròn, bơi giỏi, chân như mái chèo, thường sống ở vùng lạnh.
hai chấm|Dấu câu gồm hai chấm xếp chồng, đặt trước lời giải thích hoặc liệt kê.
hải đảo|Những hòn đảo nằm ngoài biển khơi.
hải đăng|Tháp đèn cao ven biển, chiếu sáng để tàu thuyền định hướng ban đêm.
hài hước|Vui nhộn, có khả năng làm người khác bật cười.
hài kịch|Vở kịch hoặc bộ phim có nội dung gây cười.
hài lòng|Cảm thấy vừa ý, thỏa mãn với điều gì đó.
hai mươi|Số đếm bằng hai lần mười, tức là 20.
hải ngoại|Nước ngoài, những nơi xa quê hương ở bên kia biển.
hải sản|Tôm, cá, cua, mực và các sản vật khác đánh bắt từ biển.
hải sâm|Động vật biển thân mềm hình ống dài, được dùng làm món ăn bổ dưỡng.
hàm lượng|Lượng một chất có trong một hỗn hợp hay hợp chất.
ham mê|Rất thích và say mê một việc gì đó.
hàm răng|Toàn bộ các chiếc răng mọc trên hai hàm trong miệng.
hạn chế|Giới hạn, không cho vượt quá; cũng chỉ điểm còn yếu, thiếu sót.
hạn hẹp|Ít ỏi, nhỏ hẹp, có giới hạn.
hang|Khoảng rỗng sâu trong núi đá hoặc dưới đất; cũng là nơi ở của thú.
hàng ăn|Quán bán đồ ăn, nơi phục vụ bữa ăn cho khách.
hàng đầu|Ở vị trí dẫn đầu, quan trọng hoặc xuất sắc nhất.
hang động|Khoảng rỗng lớn trong lòng núi đá, thường có thạch nhũ đẹp.
hàng không|Ngành vận chuyển người và hàng hóa bằng máy bay.
hàng loạt|Số lượng nhiều, xảy ra cùng lúc hoặc cùng một kiểu.
hạng mục|Từng phần việc, từng công trình nhỏ trong một dự án lớn.
hạng nặng|Thuộc loại nặng, cỡ lớn, như máy móc hạng nặng hay võ sĩ hạng nặng.
hạng nhất|Thứ hạng cao nhất, đứng đầu trong một cuộc thi hay xếp loại.
hàng nước|Quán nhỏ ven đường bán nước chè, nước ngọt và quà vặt.
hàng quán|Các cửa hàng, quán ăn uống nói chung.
hàng rào|Dãy cây, tre, lưới hoặc tường thấp dựng quanh để ngăn khu đất.
hàng rong|Hàng hóa mang đi bán dạo khắp phố, không bày ở cửa hàng cố định.
hàng thịt|Chỗ bán thịt ở chợ hoặc cửa hàng chuyên bán thịt.
hàng vạn|Số lượng rất lớn, lên đến nhiều chục nghìn.
hàng xóm|Người sống ở nhà gần bên cạnh nhà mình.
hành|Cây rau có lá hình ống, mùi thơm hăng, dùng làm gia vị.
hãnh diện|Tự hào, vui sướng vì có điều tốt đẹp.
hành động|Việc làm cụ thể để đạt một mục đích nào đó.
hành hoa|Hành lá nhỏ, lá xanh rỗng, thái nhỏ rắc vào món ăn cho thơm.
hành khách|Người đi trên tàu, xe, máy bay nhưng không phải người lái.
hanh khô|Thời tiết khô, ít hơi ẩm, da dễ nứt nẻ.
hạnh kiểm|Đánh giá về đạo đức, tư cách của học sinh.
hành lang|Lối đi dài và hẹp nối các phòng trong một tòa nhà.
hạnh nhân|Hạt có vỏ cứng, vị béo bùi, dùng để ăn hoặc làm bánh.
hạnh phúc|Trạng thái vui sướng, mãn nguyện trong cuộc sống.
hành ta|Loại hành củ nhỏ, vỏ đỏ tím, thơm, thường phi lên làm gia vị.
hành tây|Củ tròn nhiều lớp, vị hăng ngọt, dùng để nấu ăn.
hành tinh|Thiên thể lớn quay quanh một ngôi sao, như Trái Đất quay quanh Mặt Trời.
hành tỏi|Hành và tỏi, hai thứ gia vị quen thuộc trong bếp.
hành trang|Đồ đạc mang theo khi đi xa; cũng chỉ vốn hiểu biết cho tương lai.
hành trình|Chuyến đi dài, qua nhiều nơi để đến một đích nào đó.
hảo hạng|Chất lượng tốt nhất, thuộc loại thượng hạng.
hão huyền|Viển vông, xa rời thực tế, không thể thành sự thật.
háo hức|Rất mong chờ, nóng lòng muốn được làm điều gì.
hào hứng|Vui vẻ, phấn khởi và rất muốn tham gia.
hao mòn|Giảm dần, mòn đi theo thời gian vì sử dụng nhiều.
hào nhoáng|Bóng bẩy, rực rỡ bên ngoài nhưng có khi không thực chất.
hào phóng|Rộng rãi, sẵn lòng cho người khác tiền bạc, của cải.
hào quang|Vầng sáng tỏa ra xung quanh; cũng chỉ vinh quang, danh tiếng.
hạt cơm|Từng hạt nhỏ của cơm đã nấu chín.
hạt cườm|Hạt nhỏ có lỗ xâu, nhiều màu, dùng kết vòng hoặc đính trang trí.
hạt dẻ|Hạt có vỏ nâu bóng, ruột bùi, thường rang lên để ăn.
hạt điều|Hạt cong hình móc, vị béo bùi, thường rang muối để ăn.
hạt giống|Hạt dùng để gieo trồng thành cây mới.
hạt mưa|Giọt nước nhỏ từ trên trời rơi xuống khi mưa.
hạt ngọc|Viên ngọc nhỏ quý giá; cũng ví hạt gạo hay điều rất quý.
hát ru|Cất giọng nhẹ nhàng, êm ái để dỗ em bé ngủ.
hạt tiêu|Hạt nhỏ vị cay nồng, xay ra dùng làm gia vị.
hát vang|Cất tiếng hát to, vang khắp nơi.
háu ăn|Thèm ăn, lúc nào cũng muốn ăn nhiều và ăn nhanh.
hay dở|Cái hay và cái dở, điều tốt và điều chưa tốt.
hay hay|Khá hay, khá thú vị, gây chút thích thú.
hay ho|Thú vị, đáng chú ý, thường dùng trong câu phủ định hoặc câu hỏi.
hay không|Cụm từ cuối câu dùng để hỏi xem điều gì có đúng, có xảy ra.
hay là|Từ dùng để nêu một lựa chọn khác hoặc đưa ra đề nghị.
hay quên|Thường xuyên không nhớ việc cần làm hay đồ cần mang.
hăm hở|Hăng hái, nóng lòng bắt tay vào việc.
hẳn hoi|Đầy đủ, đàng hoàng, đúng như cần có, như ăn mặc hẳn hoi.
hẳn là|Dùng khi đoán điều gì đó gần như chắc chắn đúng.
hắn ta|Đại từ chỉ người thứ ba, thường mang ý xa cách hoặc xem thường.
hăng hái|Nhiệt tình, tích cực, sẵn sàng làm việc.
hăng say|Làm việc say mê, miệt mài, đầy nhiệt huyết.
hâm mộ|Yêu thích và ngưỡng mộ một người hoặc một điều gì.
hầm ngầm|Đường hoặc phòng xây dưới lòng đất.
hâm nóng|Đun lại cho nóng thức ăn đã nguội; cũng là làm cho sôi động trở lại.
hân hạnh|Cảm thấy vui và vinh dự, thường nói khi làm quen.
hấp dẫn|Lôi cuốn, thu hút sự chú ý, yêu thích.
hấp tấp|Vội vàng, thiếu bình tĩnh, làm không cẩn thận.
hậu cần|Công việc lo cơ sở vật chất như ăn uống, chỗ ở, phương tiện cho một hoạt động.
hậu đậu|Vụng về, hay làm rơi vỡ, làm hỏng việc.
hầu hết|Gần như tất cả, chỉ trừ một số ít.
hậu hĩnh|Rộng rãi, nhiều hơn mức bình thường, thường nói về tiền thưởng, quà.
hậu mãi|Các dịch vụ chăm sóc khách hàng sau khi bán như bảo hành, sửa chữa.
hầu như|Gần như hoàn toàn, hiếm có ngoại lệ.
hậu quả|Kết quả không hay do một việc làm trước đó gây ra.
hậu trường|Phía sau sân khấu, nơi diễn viên chuẩn bị; cũng chỉ những việc không công khai.
hậu vệ|Cầu thủ chơi ở tuyến sau, có nhiệm vụ phòng ngự.
hé mở|Mở ra một chút; cũng là để lộ dần thông tin.
hẹn hò|Gặp gỡ, đi chơi riêng với nhau, thường là giữa hai người đang tìm hiểu.
hẻo lánh|Xa xôi, vắng vẻ, ít người qua lại.
hẹp hòi|Không rộng lượng, hay tính toán, so đo với người khác.
hệ số|Số nhân kèm theo một đại lượng; cũng là mức tính quy đổi, như hệ số lương.
hệ thống|Tập hợp nhiều phần liên kết với nhau thành một khối thống nhất.
hết cách|Không còn cách nào để giải quyết.
hết cỡ|Đến mức cao nhất có thể, không thể hơn được nữa.
hết hơi|Mệt đến mức thở không ra hơi; cũng là đã cố gắng hết sức.
hết lòng|Đem hết tình cảm và sức lực để làm, để giúp.
hết mình|Dốc hết sức lực, nhiệt tình cho việc gì.
hết mức|Đến mức cao nhất có thể.
hết sạch|Không còn lại chút gì.
hết sức|Rất, vô cùng; cũng là dùng hết sức lực.
hiếm|Ít thấy, khó tìm, không có nhiều.
hiếm có|Ít khi có được, rất đặc biệt và đáng quý.
hiếm hoi|Rất ít ỏi, ít khi xảy ra hoặc ít khi có.
hiểm trở|Địa hình khó đi, nhiều núi cao, vực sâu, dốc đứng.
hiền|Tính nết dịu dàng, ôn hòa, không dữ dằn hay làm hại ai.
hiện có|Đang có sẵn vào thời điểm hiện tại, như số hàng hiện có.
hiện diện|Có mặt ở một nơi hoặc trong một sự việc nào đó.
hiền dịu|Hiền lành, nhẹ nhàng và dễ mến.
hiện đại|Mới mẻ, tiên tiến, thuộc về thời nay.
hiện giờ|Vào lúc này, ngay thời điểm đang nói.
hiền hậu|Hiền lành, tốt bụng và phúc hậu.
hiền lành|Tính tình hiền hậu, không làm hại ai.
hiện nay|Trong khoảng thời gian bây giờ, thời đại ngày nay.
hiển nhiên|Rõ ràng đến mức ai cũng thấy, không cần chứng minh.
hiện tại|Thời gian đang diễn ra, lúc bây giờ.
hiển thị|Làm hiện lên trên màn hình để người dùng nhìn thấy.
hiện thực|Điều có thật trong đời sống, không phải tưởng tượng.
hiền từ|Nhân hậu, dịu dàng, giàu lòng thương yêu người khác.
hiện tượng|Sự việc xảy ra trong tự nhiên hay xã hội mà ta quan sát được.
hiệp hội|Tổ chức gồm nhiều người hoặc đơn vị cùng ngành nghề, lập ra vì lợi ích chung.
hiểu|Nắm được ý nghĩa, lý do hay bản chất của một điều gì đó.
hiểu biết|Có nhiều kiến thức, nắm rõ nhiều điều; cũng chỉ vốn kiến thức đó.
hiểu chuyện|Biết điều, biết suy nghĩ cho người khác dù còn nhỏ tuổi.
hiếu động|Thích chạy nhảy, vận động, khó ngồi yên một chỗ.
hiếu học|Ham học, thích tìm tòi hiểu biết.
hiếu khách|Thích đón tiếp, đãi khách chu đáo và niềm nở.
hiểu lầm|Nắm sai ý người khác hoặc sai bản chất sự việc.
hiệu lực|Tác dụng thực tế; cũng chỉ giá trị thi hành, như hợp đồng có hiệu lực.
hiệu năng|Khả năng làm việc, mức hiệu quả hoạt động của máy móc, hệ thống.
hiệu phó|Người giúp hiệu trưởng điều hành công việc của nhà trường.
hiệu quả|Kết quả tốt đạt được so với công sức bỏ ra.
hiệu sách|Cửa hàng bán sách, báo và đồ dùng học tập.
hiếu thảo|Biết yêu thương, kính trọng và chăm sóc cha mẹ, ông bà.
hiếu thắng|Lúc nào cũng muốn hơn người, muốn phần thắng về mình.
hiểu thấu|Nắm được rất sâu và rõ, đến tận tâm tư hay bản chất.
hiệu trưởng|Người đứng đầu, quản lý một trường học.
hiệu ứng|Kết quả của một tác động; cũng chỉ kỹ xảo hình ảnh, âm thanh.
hình|Dáng vẻ bên ngoài của vật; cũng chỉ bức ảnh hoặc hình vẽ.
hình ảnh|Hình của người, vật được chụp, vẽ lại hoặc hiện ra trong đầu.
hình bóng|Dáng hình của một người, thường in sâu trong ký ức.
hình cầu|Khối tròn đều về mọi phía, như quả bóng.
hình dạng|Dáng vẻ, hình thể bên ngoài của sự vật.
hình dung|Tưởng tượng ra trong đầu hình ảnh của sự vật.
hình học|Môn toán nghiên cứu về điểm, đường, mặt và các hình khối.
hình mẫu|Người hoặc vật tiêu biểu để người khác noi theo.
hình như|Có vẻ như, dùng khi nói điều mình không chắc chắn.
hình nón|Khối có đáy tròn, nhọn dần lên đỉnh, như chiếc nón lá.
hình thang|Tứ giác có hai cạnh đối diện song song với nhau.
hình thành|Dần dần được tạo nên và có hình dáng rõ ràng.
hình thoi|Tứ giác có bốn cạnh dài bằng nhau.
hình thù|Hình dạng bên ngoài, thường là lạ mắt, khó tả.
hình thức|Vẻ bề ngoài của sự vật; cũng là cách thức thực hiện một việc.
hình tròn|Hình phẳng có mọi điểm trên đường viền cách đều tâm.
hình trụ|Khối có hai đáy tròn bằng nhau, như cái lon nước.
hình tượng|Hình ảnh tiêu biểu, mang ý nghĩa đặc biệt trong nghệ thuật hay đời sống.
hình vẽ|Tranh, hình tạo ra bằng bút, màu trên giấy hoặc bề mặt khác.
hình vuông|Tứ giác có bốn cạnh bằng nhau và bốn góc vuông.
hít hà|Hít hơi liên tục vì cay, vì lạnh hoặc vì thấy thơm ngon.
họ hàng|Những người có quan hệ máu mủ hoặc thông gia với nhau.
hò hẹn|Hẹn gặp nhau, thường là giữa những người yêu nhau.
hò hét|Kêu la to, ầm ĩ, thường khi cổ vũ hoặc thúc giục.
họ ngoại|Họ hàng về phía mẹ, gồm ông bà ngoại, cậu, dì.
họ nội|Họ hàng về phía bố, cùng một dòng họ với mình.
hò reo|Cùng nhau la lên vui mừng, phấn khởi.
hoa chuối|Bắp chuối, cụm hoa màu tím đỏ của cây chuối, hay thái làm nộm, gỏi.
hoa cúc|Loài hoa nhiều cánh nhỏ, thường màu vàng, nở nhiều vào mùa thu.
hoa đào|Loài hoa màu hồng nở vào mùa xuân, đặc trưng cho Tết ở miền Bắc.
hoa đăng|Đèn hoa nhiều màu, thường thả trôi trên sông trong lễ hội.
hoa giấy|Cây leo có hoa mỏng như giấy, nhiều màu, thường trồng ở cổng nhà.
hoa hậu|Danh hiệu dành cho người đẹp nhất trong một cuộc thi sắc đẹp.
hoa hồng|Loài hoa cánh mềm, hương thơm, thân có gai.
hoa huệ|Loài hoa màu trắng, cành dài, mùi thơm ngát, hay tỏa hương về đêm.
hoa khôi|Cô gái đẹp nhất, nổi bật nhất trong một tập thể hay cuộc thi.
hoa lá|Hoa và lá cây nói chung, thường gợi cảnh vật tươi đẹp.
hoa lài|Hoa nhài, hoa nhỏ màu trắng, rất thơm, hay dùng ướp trà.
hoa lan|Loài hoa quý, dáng đẹp, nhiều màu, hay được trồng làm cảnh.
hoa mai|Loài hoa thường có năm cánh màu vàng, nở rộ dịp Tết ở miền Nam.
hoa nhài|Loài hoa nhỏ màu trắng, rất thơm, hay dùng để ướp trà.
hoa quả|Các loại trái cây ăn được nói chung.
hoa sen|Loài hoa mọc dưới ao đầm, cánh hồng hoặc trắng, lá to tròn.
hoa sữa|Hoa nhỏ màu trắng ngà mọc thành chùm, hương nồng, nở cuối thu ở Hà Nội.
hoa tai|Đồ trang sức đeo ở tai, thường bằng vàng, bạc.
hoa văn|Hình vẽ, họa tiết trang trí trên đồ vật hoặc vải vóc.
hoài|Mãi, kéo dài liên tục không dứt; cũng là uổng phí.
hoài bão|Mong ước, ý định lớn lao, tốt đẹp ấp ủ trong lòng.
hoài cổ|Yêu thích, nhớ tiếc những gì thuộc về ngày xưa.
hoài niệm|Nhớ lại với nhiều cảm xúc về những điều đã qua.
hoãn|Dời lại vào một thời điểm muộn hơn.
hoàn cảnh|Tình hình, điều kiện sống xung quanh một người hoặc một việc.
hoàn chỉnh|Đầy đủ các phần, không thiếu sót gì.
hoàn hảo|Tốt đến mức không có điểm nào để chê.
hoan hô|Reo lên để khen ngợi, cổ vũ hoặc tán thành.
hoàn lại|Trả lại cho người khác cái đã nhận hoặc đã mượn.
hoàn tất|Làm xong toàn bộ, không còn phần nào dở dang.
hoàn thành|Làm xong trọn vẹn một việc hoặc nhiệm vụ.
hoàn thiện|Làm cho đầy đủ, tốt đẹp hơn; cũng chỉ trạng thái đã đầy đủ, tốt đẹp.
hoàn toàn|Đầy đủ, trọn vẹn; cũng dùng để nhấn mạnh mức độ tuyệt đối.
hoàn trả|Trả lại đầy đủ tiền hoặc vật đã vay, đã thu.
hoang|Bỏ không, không ai ở hay chăm sóc; cũng là tiêu xài phung phí.
hoàng cung|Cung điện nơi vua và gia đình nhà vua sinh sống.
hoang dã|Thuộc về thiên nhiên chưa bị con người khai phá, như rừng rậm, thú rừng.
hoang dại|Mọc hoặc sống tự do ngoài thiên nhiên, chưa được con người thuần hóa.
hoang đảo|Hòn đảo không có người sinh sống.
hoàng đế|Vị vua đứng đầu một nước, thường là nước lớn.
hoang đường|Vô lý, không có thật, khó tin.
hoàng gia|Gia đình của nhà vua, gồm vua và những người thân.
hoàng hậu|Người vợ chính thức của nhà vua.
hoàng hôn|Lúc mặt trời lặn, bầu trời ngả màu vàng đỏ trước khi tối.
hoang mạc|Vùng đất rộng lớn, khô cằn, rất ít mưa và ít cây cối.
hoang mang|Lo lắng, bối rối, không biết nên tin hay làm gì.
hoang phí|Tiêu xài lãng phí, không biết tiết kiệm.
hoang sơ|Còn nguyên vẻ tự nhiên, chưa bị con người tác động nhiều.
hoàng thượng|Cách bề tôi xưng hô tôn kính với nhà vua thời phong kiến.
hoàng tử|Con trai của nhà vua, hay xuất hiện trong truyện cổ tích.
hoang vắng|Vắng vẻ, ít hoặc không có người qua lại.
hoành thánh|Món bánh vỏ bột mì mỏng gói nhân thịt, luộc ăn với nước dùng hoặc chiên giòn.
hoành tráng|To lớn, đồ sộ và gây ấn tượng mạnh.
hoạt bát|Nhanh nhẹn, nói năng lưu loát, vui vẻ.
hoạt động|Vận động, làm việc hoặc vận hành; cũng chỉ những việc làm có tổ chức.
hoạt hình|Loại phim làm từ hình vẽ hoặc mô hình được cho chuyển động.
hoặc|Từ dùng để nêu một trong nhiều khả năng có thể chọn.
hoặc là|Từ nối dùng để đưa ra một khả năng khác để lựa chọn.
học bạ|Sổ ghi kết quả học tập và rèn luyện của học sinh.
học bổng|Tiền thưởng hoặc hỗ trợ cho người học giỏi hay có hoàn cảnh khó khăn.
hóc búa|Rất khó, phức tạp, khó tìm ra cách giải quyết.
học đường|Trường học, môi trường học tập nói chung.
học hành|Việc học tập, đi học nói chung.
học hỏi|Tìm hiểu, tiếp thu kiến thức và kinh nghiệm từ người khác.
học lại|Ôn lại bài cũ; cũng là phải học lần nữa vì chưa đạt yêu cầu.
học lực|Năng lực và kết quả học tập của học sinh.
học phí|Khoản tiền người học phải đóng cho trường, lớp.
học sinh|Người đang đi học ở trường phổ thông.
học tập|Tiếp thu kiến thức và rèn luyện kỹ năng qua việc học.
học thuật|Thuộc về nghiên cứu khoa học, kiến thức chuyên sâu có hệ thống.
học thức|Vốn kiến thức có được nhờ học tập.
học trò|Người theo học một thầy, cô; học sinh nói chung.
học tủ|Chỉ học vài phần đoán sẽ ra thi, bỏ qua các phần khác.
học vấn|Trình độ hiểu biết có được qua việc học.
học việc|Làm việc ở một nơi để học nghề.
học viên|Người theo học một khóa học, lớp học.
hỏi han|Hỏi thăm, quan tâm đến tình hình của người khác.
hỏi nhỏ|Hỏi khẽ, hỏi riêng để người khác không nghe thấy.
hỏi thăm|Hỏi để biết tình hình, sức khỏe của ai đó vì quan tâm.
hóm hỉnh|Hài hước một cách thông minh, tinh nghịch.
hòm thư|Thùng để bỏ thư; cũng chỉ hộp thư điện tử.
hòn bi|Viên tròn nhỏ bằng thủy tinh hoặc sắt, trẻ em dùng để chơi.
hòn đảo|Vùng đất nổi lên giữa biển hoặc sông hồ, có nước bao quanh.
hòn ngọc|Viên đá quý; cũng chỉ nơi rất đẹp và quý giá.
hỏng bét|Hỏng hết, thất bại hoàn toàn, không cứu vãn được.
hóng chuyện|Tò mò nghe ngóng chuyện của người khác.
hỏng hóc|Máy móc, đồ dùng bị trục trặc, không hoạt động bình thường.
hóng mát|Ra chỗ thoáng đãng để hưởng gió mát.
họp báo|Buổi gặp gỡ các nhà báo để công bố thông tin.
họp hành|Việc hội họp nói chung, thường hàm ý họp nhiều.
họp mặt|Gặp gỡ đông đủ để chuyện trò, thăm hỏi nhau.
hộ chiếu|Giấy tờ do nhà nước cấp để công dân đi ra nước ngoài.
hồ hởi|Vui vẻ, phấn khởi, lộ rõ ra bên ngoài.
hồ lô|Quả bầu thắt eo ở giữa, vỏ khô dùng làm bình đựng nước.
hổ mang|Loài rắn có thể dựng đầu và bành cổ ra khi bị đe dọa.
hồ sơ|Tập giấy tờ, tài liệu về một người hoặc một việc.
hỗ trợ|Giúp đỡ thêm về công sức, tiền bạc hoặc phương tiện.
hội chợ|Nơi tập trung nhiều gian hàng để mua bán, giới thiệu sản phẩm, vui chơi.
hội diễn|Cuộc biểu diễn văn nghệ có nhiều đơn vị tham gia.
hồi đầu|Lúc mới bắt đầu, thời gian đầu.
hội đồng|Nhóm người được giao cùng bàn bạc, quyết định một việc.
hối hả|Vội vàng, tất bật, nhanh chóng.
hồi hộp|Lo lắng, mong chờ, tim đập nhanh khi chờ đợi điều gì.
hồi hương|Trở về quê hương sau thời gian sống xa.
hối lỗi|Thấy mình sai và muốn sửa chữa.
hồi nãy|Lúc trước đó một chút, cách nói phổ biến ở miền Nam.
hội nghị|Cuộc họp lớn có nhiều người tham dự để bàn bạc việc chung.
hội ngộ|Gặp lại nhau sau thời gian xa cách.
hội nhập|Tham gia và hòa vào một cộng đồng, tổ chức hay nền kinh tế rộng lớn hơn.
hồi phục|Trở lại trạng thái bình thường sau khi bị yếu hoặc hư hại.
hồi sinh|Sống lại hoặc có sức sống mạnh mẽ trở lại.
hội thảo|Cuộc họp để trao đổi, thảo luận về một chủ đề chuyên môn.
hội thi|Cuộc thi có nhiều người tham gia, thường mang tính giao lưu.
hội thoại|Cuộc trò chuyện giữa hai hay nhiều người.
hối thúc|Giục giã người khác làm nhanh hơn.
hối tiếc|Tiếc vì đã làm hoặc đã không làm điều gì.
hồi trước|Khoảng thời gian trước đây, ngày xưa.
hội trường|Phòng lớn dùng để họp hoặc tổ chức sự kiện.
hội tụ|Cùng tập trung về một điểm; cũng chỉ nhiều điều tốt cùng có ở một nơi.
hồi tưởng|Nhớ lại những chuyện đã qua.
hội viên|Thành viên của một hội hoặc câu lạc bộ.
hôm kia|Ngày trước hôm qua, tức cách hôm nay hai ngày.
hôm nào|Một ngày nào đó chưa định rõ; cũng dùng để hỏi về một ngày.
hôm nay|Ngày hiện tại, ngày đang diễn ra.
hôm nọ|Một ngày trước đây không lâu.
hôm qua|Ngày liền trước ngày hôm nay.
hôm sau|Ngày tiếp theo sau một ngày được nói đến.
hôm trước|Ngày liền trước đó; cũng chỉ một ngày nào đó đã qua.
hỗn độn|Bừa bãi, lẫn lộn nhiều thứ, không có thứ tự.
hỗn hào|Ăn nói, cư xử vô lễ với người lớn tuổi hoặc người trên.
hổn hển|Thở gấp, dồn dập vì mệt.
hỗn hợp|Nhiều thứ khác nhau được trộn lẫn vào nhau.
hôn lễ|Lễ cưới, nghi lễ kết hôn của hai người.
hỗn loạn|Lộn xộn, mất trật tự, không theo quy củ.
hôn nhân|Quan hệ vợ chồng được xác lập khi hai người kết hôn.
hồn nhiên|Ngây thơ, tự nhiên, không giả tạo.
hồng|Màu đỏ nhạt pha trắng; cũng chỉ hoa hồng hoặc quả hồng.
hồng hạc|Loài chim chân dài, cổ cong, lông màu hồng, sống thành đàn ở đầm nước.
hống hách|Cậy quyền thế, ra oai, coi thường người khác.
hồng hào|Da dẻ có màu hồng tươi, trông khỏe mạnh.
hồng ngoại|Loại tia không nhìn thấy, nằm ngoài ánh sáng đỏ, dùng trong điều khiển từ xa, sưởi ấm.
hồng ngọc|Loại đá quý có màu đỏ tươi, dùng làm trang sức.
hồng nhung|Giống hoa hồng màu đỏ thẫm, cánh mượt như nhung.
hộp số|Bộ phận trong xe, máy dùng để thay đổi tốc độ và lực truyền từ động cơ.
hộp thoại|Khung nhỏ hiện trên màn hình máy tính để thông báo hoặc hỏi người dùng.
hộp thư|Hộp gắn trước nhà để nhận thư; cũng chỉ nơi lưu thư điện tử.
hơi hơi|Có một chút, ở mức độ nhẹ, không nhiều.
hời hợt|Nông cạn, không sâu sắc, thiếu quan tâm.
hơi lạnh|Khí lạnh tỏa ra; cũng là cảm thấy lạnh ở mức nhẹ.
hơi nước|Nước ở thể khí, bốc lên khi đun nóng hoặc bay hơi.
hơi thở|Không khí hít vào, thở ra qua mũi, miệng.
hơn cả|Vượt lên trên tất cả, ở mức cao nhất.
hờn dỗi|Giận và tỏ ra không vui để người khác dỗ dành.
hơn hẳn|Vượt trội rõ rệt so với cái khác.
hơn hết|Nhiều hơn hoặc quan trọng hơn tất cả những điều khác.
hớn hở|Vui mừng lộ rõ trên nét mặt.
hơn là|Dùng để so sánh, chọn cái này thay vì cái kia.
hơn nữa|Từ nối dùng để thêm một ý bổ sung cho điều vừa nói.
hơn thua|So bì xem ai hơn ai kém, tranh nhau phần hơn.
hợp ca|Nhiều người cùng hát chung một bài.
hợp chất|Chất được tạo thành từ hai hay nhiều nguyên tố hóa học kết hợp với nhau.
hợp đồng|Văn bản ghi thỏa thuận về quyền lợi và trách nhiệm giữa các bên.
hớp hồn|Cuốn hút mạnh, làm người khác say mê ngây ngất.
hợp kim|Vật liệu gồm kim loại trộn với kim loại hay chất khác, như thép, đồng thau.
hợp lệ|Đúng với thể lệ, quy định đã đặt ra nên được chấp nhận.
hợp nhất|Gộp nhiều tổ chức hoặc bộ phận lại thành một khối chung.
hợp tác|Cùng góp sức làm việc với nhau vì một mục đích chung.
hú hồn|Thốt lên khi vừa thoát một phen sợ hãi, may mà không sao.
hu hu|Tiếng khóc to, nức nở.
huấn luyện|Dạy và cho luyện tập để thành thạo một kỹ năng.
hun khói|Để thực phẩm trong khói một thời gian cho khô và thơm.
húng|Tên gọi chung một số loại rau thơm như húng lủi, húng quế, hay ăn sống.
hùng mạnh|Rất mạnh, có sức mạnh to lớn.
húng quế|Rau thơm lá xanh, thân tím, mùi nồng, hay ăn kèm phở.
huống chi|Từ nối, ý nói điều sau càng hiển nhiên hơn điều vừa nói trước.
hút bụi|Dùng máy hút để làm sạch bụi bẩn trên sàn, thảm.
hụt hẫng|Cảm giác chơi vơi, thất vọng vì điều mong đợi không như ý.
hụt hơi|Thở không kịp, bị thiếu hơi khi chạy hoặc khi hát.
hút mật|Ong, bướm hút lấy mật ngọt trong hoa.
huy chương|Vật bằng kim loại trao cho người đạt thành tích hoặc có công.
huy động|Tập hợp, điều động người, tiền của, phương tiện cho một công việc.
huy hiệu|Vật nhỏ có hình biểu tượng của một tổ chức, thường cài lên áo.
huy hoàng|Rực rỡ, lộng lẫy, thường nói về thời kỳ vẻ vang, thịnh vượng.
huyện|Đơn vị hành chính cũ dưới tỉnh, gồm nhiều xã.
huyền bí|Bí ẩn, khó hiểu, khó giải thích.
huyền thoại|Câu chuyện kỳ lạ truyền lại từ xa xưa; cũng chỉ người lừng danh.
huynh đệ|Anh và em; thường chỉ những người coi nhau như anh em ruột.
huỳnh quang|Hiện tượng phát sáng của một số chất khi bị chiếu tia, như đèn huỳnh quang.
huýt sáo|Chụm môi thổi hơi ra thành tiếng kêu như tiếng chim.
hư hại|Bị hỏng hóc, tổn thất một phần, không còn nguyên vẹn.
hư hỏng|Bị hỏng, không dùng được nữa; cũng chỉ người có lối sống xấu.
hứa hẹn|Nói trước rằng mình sẽ làm điều gì; cũng chỉ có triển vọng tốt đẹp.
hừng hực|Nóng rực như lửa bốc lên; cũng chỉ khí thế sôi nổi, mạnh mẽ.
hứng khởi|Cảm thấy phấn chấn, hăng hái và muốn bắt tay vào làm ngay.
hứng thú|Cảm giác thích thú, muốn tìm hiểu hoặc tham gia vào việc gì đó.
hướng|Phía, chiều mà vật quay về hoặc đi tới; cũng là quay về phía đó.
hướng dẫn|Chỉ bảo cách làm để người khác làm theo.
hướng dương|Loài hoa to màu vàng, hay quay theo mặt trời, hạt rang ăn được.
hướng nghiệp|Giúp học sinh tìm hiểu và chọn nghề phù hợp với mình.
hướng ngoại|Tính cách thích giao tiếp, cởi mở, năng động với mọi người.
hướng nội|Tính cách trầm lặng, thích yên tĩnh, ít giao tiếp, hay suy nghĩ.
hương sen|Mùi thơm nhẹ, thanh mát của hoa sen.
hương thơm|Mùi thơm dễ chịu tỏa ra từ hoa, đồ ăn hay nước hoa.
hưởng thụ|Tận hưởng những điều thú vị, sung sướng trong cuộc sống.
hưởng ứng|Đồng tình và tích cực tham gia theo lời kêu gọi.
hươu|Thú ăn cỏ chân dài, con đực có sừng nhiều nhánh.
hươu nai|Các loài thú ăn cỏ chân dài, chạy nhanh, con đực thường có sừng phân nhánh.
hữu cơ|Có nguồn gốc từ sinh vật; thường chỉ rau quả trồng không dùng hóa chất.
hữu dụng|Dùng được vào việc cụ thể và mang lại lợi ích thiết thực.
hữu ích|Mang lại lợi ích, giúp ích được cho người khác hoặc cho công việc.
ích lợi|Điều tốt, giá trị mà một việc hay một vật mang lại.
im ắng|Yên tĩnh, vắng vẻ, không nghe thấy tiếng động nào.
im bặt|Đột ngột im lặng hẳn, không còn chút tiếng động.
im lặng|Không nói gì, không lên tiếng; cũng chỉ nơi không có tiếng động.
in ảnh|Chuyển ảnh đã chụp ra giấy ảnh để cầm xem hoặc lưu giữ.
in ấn|Công việc in sách báo, tài liệu, bao bì bằng máy in nói chung.
inch|Đơn vị đo chiều dài, bằng 2,54 cm, hay dùng để chỉ cỡ màn hình.
inh ỏi|Âm thanh to, vang lên liên tục, nghe chói tai khó chịu.
ít khi|Hiếm có dịp, không xảy ra thường xuyên.
ít nhất|Mức tối thiểu, không thể thấp hơn được nữa.
ít nhiều|Không nhiều thì ít, ở một mức độ nào đó.
ít nói|Tính trầm lặng, không hay nói chuyện nhiều.
ít nữa|Chẳng bao lâu nữa, trong thời gian sắp tới.
ít ỏi|Chỉ có rất ít, không được bao nhiêu.
ít ra|Ở mức tối thiểu, dù sao thì cũng còn được như thế.
ỉu xìu|Mềm oặt, không còn giòn; cũng chỉ vẻ buồn rầu, chán nản.
kaki|Loại vải dày, dệt chéo, bền chắc, hay dùng may quần áo.
karaoke|Hình thức giải trí hát theo nhạc đệm, lời bài hát hiện trên màn hình.
kẽ hở|Khe nhỏ giữa hai vật; cũng chỉ chỗ sơ suất dễ bị lợi dụng.
kẽ nứt|Đường nứt nhỏ và hẹp trên tường, mặt đất hoặc đá.
kẽ răng|Khe hở nhỏ giữa hai chiếc răng nằm cạnh nhau.
kém cạnh|Thua kém, không bằng người khác về mặt nào đó.
kém cỏi|Năng lực, trình độ yếu, thua kém người khác.
kem cốc|Món kem đựng trong cốc nhỏ, ăn bằng thìa.
kem que|Món kem đông lạnh có que gỗ cắm giữa để cầm ăn.
kem sữa|Món kem làm từ sữa, mát lạnh, có vị ngọt và béo.
kèm theo|Đi cùng, gửi thêm hoặc đính thêm vào cái chính.
kén chọn|Chọn lựa kỹ càng, khắt khe, khó vừa ý.
kéo căng|Giằng hai đầu ra cho thẳng, không để chùng hay nhăn.
kẹo chanh|Loại kẹo có vị chua ngọt và mùi thơm của chanh.
kéo co|Trò chơi dân gian, hai đội nắm dây kéo về hai phía.
kéo dài|Làm cho dài thêm; cũng chỉ diễn ra trong thời gian lâu.
keo kiệt|Hà tiện quá mức, không muốn chi tiêu hay chia sẻ cho ai.
kéo lê|Lôi một vật trượt sát trên mặt đất theo sau mình.
kẹo mút|Viên kẹo gắn trên que nhỏ để cầm, ngậm mút dần.
kéo theo|Dẫn tới một việc khác xảy ra tiếp theo.
kẹp tóc|Đồ nhỏ dùng để kẹp, giữ tóc gọn gàng.
kẹt cứng|Bị mắc chặt không nhúc nhích được, thường nói về xe cộ tắc đường.
kể cả|Tính luôn vào, bao gồm cả người hoặc vật được nhắc đến.
kế hoạch|Những việc dự định làm, được sắp xếp theo trình tự và thời gian.
kể lại|Thuật lại cho người khác nghe chuyện đã xảy ra.
kể lể|Nói dài dòng, nhiều chi tiết, thường để than phiền.
kể ra|Nêu ra từng điều một; cũng dùng mở đầu một nhận xét, nghĩa là xét ra thì.
kế thừa|Tiếp nhận và phát huy những gì người trước để lại.
kế tiếp|Tiếp theo ngay sau cái vừa nói đến.
kế toán|Công việc ghi chép, tính toán thu chi tiền bạc của một đơn vị.
kể từ|Bắt đầu tính từ một thời điểm nào đó.
kền kền|Loài chim lớn, đầu và cổ trụi lông, thường ăn xác thú vật.
kênh|Đường dẫn nước do người đào; cũng chỉ một đài phát sóng trên truyền hình.
kênh đào|Đường thủy lớn do con người đào để tàu thuyền qua lại.
kênh rạch|Hệ thống kênh và sông nhỏ chằng chịt, nhất là ở miền Tây.
kết bạn|Làm quen và trở thành bạn của nhau.
kết cấu|Cách sắp xếp, tổ chức các bộ phận tạo thành một tổng thể như công trình, bài văn.
kết dính|Làm cho các phần bám chặt vào nhau; cũng chỉ sự gắn bó trong tập thể.
kết đôi|Ghép thành một đôi, thường nói về hai người yêu nhau.
kết hôn|Chính thức trở thành vợ chồng.
kết hợp|Gộp, phối hợp nhiều thứ lại với nhau cho hiệu quả hơn.
kết luận|Ý kiến, nhận định rút ra cuối cùng sau khi xem xét.
kết nối|Nối liền lại với nhau; cũng chỉ giữ liên lạc, gắn bó.
kết quả|Cái đạt được sau một quá trình làm việc, học tập.
kết thúc|Đi tới phần cuối cùng, chấm dứt hẳn.
kêu ca|Phàn nàn, than phiền về điều mình không vừa ý.
kêu gào|Gào lên thật to để gọi ai hoặc để than vãn.
kêu gọi|Hô hào, mời gọi mọi người cùng tham gia làm việc gì.
kêu la|Gọi to, la lớn tiếng ầm ĩ để gây chú ý hoặc than vãn.
khá giả|Có của ăn của để, đời sống tương đối dư dả.
kha khá|Ở mức tương đối khá, tạm được hoặc hơi nhiều.
khả năng|Năng lực làm được việc gì; cũng chỉ điều có thể xảy ra.
khả quan|Có chiều hướng tốt, đáng mừng và đáng hài lòng.
khả thi|Có thể làm được, thực hiện được trong thực tế.
khác|Không giống; cũng chỉ người hoặc vật còn lại ngoài cái đã nói.
khác biệt|Có những điểm không giống nhau rõ rệt.
khác gì|Cách nói ý hai thứ giống nhau, chẳng khác chút nào.
khác nhau|Không giống nhau giữa hai hay nhiều người, vật.
khác thường|Lạ, không giống như bình thường vẫn thấy.
khác xa|Chênh lệch rất nhiều, gần như không giống chút nào.
khách|Người từ nơi khác đến thăm; cũng chỉ người mua hàng, dùng dịch vụ.
khách hàng|Người mua hàng hoặc sử dụng dịch vụ của một cửa hàng, công ty.
khách khứa|Những người khách đến nhà nói chung, thường là đông người.
khách mời|Người được mời đến dự một buổi lễ, bữa tiệc hay sự kiện.
khách quan|Dựa vào sự thật, không bị tình cảm hay ý riêng chi phối.
khách sạn|Nơi có nhiều phòng cho khách thuê để nghỉ ngơi, lưu trú.
khách sáo|Quá giữ phép lịch sự xã giao, thiếu sự tự nhiên thân mật.
khai giảng|Bắt đầu năm học hoặc khóa học mới, thường có buổi lễ chào mừng.
khai mạc|Chính thức mở đầu một hội nghị, cuộc thi hay lễ hội.
khái niệm|Ý hiểu chung, cơ bản về một sự vật hay vấn đề.
khai phá|Mở mang vùng đất hoang hoặc tìm tòi trong lĩnh vực còn mới mẻ.
khái quát|Nêu những ý chính, tổng quát, không đi vào chi tiết.
khai sinh|Đăng ký em bé mới sinh với chính quyền; cũng chỉ sự ra đời của điều gì.
khai thác|Lấy tài nguyên từ thiên nhiên; cũng chỉ tận dụng cái sẵn có để sinh lợi.
khai trương|Mở cửa hàng, công ty lần đầu để bắt đầu buôn bán, kinh doanh.
khảm|Gắn những mảnh xà cừ, đá quý vào mặt đồ vật thành hình trang trí.
khám phá|Tìm ra điều mới mẻ hoặc điều trước đó chưa ai biết.
khán đài|Khu có bậc ghế cao dần cho người xem ở sân vận động.
khán giả|Người xem biểu diễn, xem phim hoặc xem thi đấu.
khan hiếm|Có rất ít, không đủ so với nhu cầu nên khó tìm.
khán phòng|Phòng lớn có nhiều hàng ghế cho người xem biểu diễn.
kháng khuẩn|Có khả năng ngăn vi khuẩn phát triển, như xà phòng kháng khuẩn.
khang trang|Rộng rãi, đẹp đẽ và ngăn nắp, thường nói về nhà cửa.
khánh thành|Làm lễ mừng công trình vừa xây xong, đưa vào sử dụng.
khao|Mời mọi người ăn uống để mừng một dịp vui của mình.
khảo cổ|Ngành đào bới, nghiên cứu di vật xưa để tìm hiểu quá khứ.
khao khát|Mong muốn tha thiết, mạnh mẽ được có hoặc được làm điều gì.
khảo sát|Đi xem xét, thu thập thông tin thực tế để nắm rõ tình hình.
khát|Cảm giác muốn uống nước; cũng chỉ mong muốn rất mãnh liệt.
khát nước|Cổ họng khô, cơ thể cần được uống nước.
khát vọng|Mong ước lớn lao, mạnh mẽ hướng tới điều tốt đẹp.
khay|Đồ dùng mặt phẳng, có gờ thấp quanh viền, để bưng hoặc bày đồ.
khắc nghiệt|Rất khó chịu đựng, gay gắt, thường nói về thời tiết, điều kiện sống.
khắc phục|Vượt qua khó khăn hoặc sửa chữa những sai sót, hư hỏng.
khắc sâu|Ghi nhớ thật sâu trong lòng, khó có thể quên.
khăn|Tấm vải dùng để lau, quàng cổ hoặc đội đầu.
khăn ăn|Miếng vải hoặc giấy nhỏ dùng lau miệng, lau tay trong bữa ăn.
khăn bàn|Tấm vải trải trên mặt bàn để trang trí và giữ sạch.
khăn choàng|Tấm khăn lớn quấn quanh cổ hoặc phủ lên vai cho ấm.
khăn gói|Đồ đạc gói ghém mang theo người khi đi xa.
khăn lau|Miếng vải dùng để lau chùi bàn ghế, bát đĩa, đồ vật.
khăn mặt|Tấm vải bông nhỏ, mềm, dùng để rửa và lau mặt.
khăn quàng|Tấm vải quấn quanh cổ cho ấm; cũng chỉ khăn đỏ của đội viên.
khăn tay|Mảnh vải nhỏ, mỏng, bỏ túi để lau tay, lau mặt.
khăn tắm|Tấm vải bông lớn và dày, dùng lau khô người sau khi tắm.
khẳng định|Nói chắc chắn điều gì là đúng; cũng chỉ chứng tỏ được giá trị bản thân.
khăng khăng|Một mực giữ ý kiến của mình, không chịu thay đổi.
khắp|Trải ra mọi chỗ, không bỏ sót nơi nào.
khắp nơi|Ở tất cả mọi chỗ, mọi chốn xung quanh.
khấm khá|Có của ăn của để, cuộc sống khá giả hơn trước.
khâm phục|Kính trọng và nể phục tài năng hoặc đức tính của ai.
khẩn cấp|Rất gấp, cần được xử lý ngay lập tức.
khẩn trương|Làm nhanh, gấp rút, không để chậm trễ.
khập khiễng|Bước đi cao thấp không đều; cũng chỉ sự so sánh không cân xứng, thiếu hợp lý.
khâu|Dùng kim chỉ nối vải với nhau; cũng chỉ một bước trong công việc.
khẩu hiệu|Câu ngắn gọn, dễ nhớ, nêu mục tiêu hoặc kêu gọi mọi người.
khẩu phần|Lượng thức ăn chia cho mỗi người trong một bữa hay một ngày.
khẩu trang|Miếng vải che mũi và miệng để chắn bụi, giữ vệ sinh.
khâu vá|May và vá lại quần áo bằng kim chỉ.
khen|Nói lời đánh giá tốt về một người hay việc làm nào đó.
khen ngợi|Nói lời tốt đẹp để tỏ ý đánh giá cao, tán thưởng ai.
khen thưởng|Tuyên dương và trao phần thưởng cho người có thành tích tốt.
khéo|Giỏi làm các việc tinh tế; cũng chỉ biết cư xử, ăn nói dễ nghe.
khéo léo|Làm hoặc nói một cách tinh tế, nhẹ nhàng và hiệu quả.
khéo tay|Giỏi làm các việc thủ công cần sự tỉ mỉ của đôi tay.
khép|Đóng lại hoặc thu cho sát vào nhau, như khép cửa, khép chân.
khép kín|Đóng kín, tự đủ trong một khối; cũng chỉ người ít giao tiếp, cởi mở.
khép lại|Đóng lại; cũng chỉ kết thúc một sự kiện hay giai đoạn.
khét|Mùi bốc lên khi đồ vật bị cháy, bị sém.
khi ấy|Vào lúc đó, thời điểm vừa được nhắc tới.
khỉ đột|Loài vượn lớn nhất, thân to khỏe, lông đen, sống trong rừng châu Phi.
khí hậu|Thời tiết đặc trưng của một vùng trong thời gian dài.
khi nào|Cụm từ dùng để hỏi về thời điểm xảy ra một việc.
khi nãy|Lúc vừa qua, ngay trước thời điểm đang nói không lâu.
khí quyển|Lớp không khí dày bao quanh Trái Đất.
khí thế|Tinh thần mạnh mẽ, hăng hái của một tập thể.
khi xưa|Thời gian đã qua từ lâu, những ngày trước đây.
khía cạnh|Một mặt, một phương diện của sự việc hay vấn đề.
khích|Dùng lời nói để kích thích, thúc người khác làm việc gì, như nói khích.
khích lệ|Động viên, cổ vũ tinh thần để ai đó cố gắng hơn.
khiêm nhường|Nhã nhặn, không tự đề cao mình, sẵn sàng nhường người khác.
khiêm tốn|Không khoe khoang, không tự đề cao mình; cũng chỉ ở mức nhỏ, vừa phải.
khiến|Làm cho người khác cảm thấy hoặc làm điều gì; cũng nghĩa là sai bảo.
khiêng|Hai hay nhiều người cùng nhấc một vật nặng lên và mang đi.
khiếu|Khả năng tự nhiên, sẵn có về một lĩnh vực, như có khiếu vẽ.
khiếu nại|Đề nghị người có trách nhiệm xem xét lại việc mình cho là sai, gây thiệt thòi.
khiêu vũ|Nhảy theo điệu nhạc, thường từng đôi nam nữ với nhau.
khít|Sát vào nhau, vừa vặn, không còn kẽ hở.
khó bảo|Bướng bỉnh, không chịu nghe lời người khác dạy bảo.
kho báu|Nơi cất giấu nhiều vàng bạc, châu báu quý giá.
khó chịu|Cảm thấy không thoải mái trong người hoặc trong lòng.
khó chơi|Không dễ gần, khó hòa hợp; cũng chỉ đối thủ khó đối phó.
khó coi|Trông không đẹp mắt hoặc không hợp lẽ, gây chướng mắt.
khó hiểu|Không dễ nắm được ý, phải suy nghĩ nhiều mới hiểu ra.
khó khăn|Có nhiều trở ngại, vất vả, không thuận lợi.
khò khò|Tiếng ngáy đều đều phát ra khi ngủ say.
khó nghĩ|Phân vân, khó quyết định vì có nhiều điều phải cân nhắc.
khó nhằn|Cách nói chỉ việc khó làm, khó giải quyết, như bài toán hóc búa.
khó nói|Ngại mở lời vì chuyện tế nhị hoặc không biết nói sao.
khó tả|Không thể dùng lời để diễn tả cho hết.
kho tàng|Nơi cất giữ của cải; cũng chỉ vốn quý tích lũy lâu đời của một dân tộc.
khó tin|Không dễ tin là có thật vì quá bất ngờ.
khó tính|Hay đòi hỏi, khắt khe, khó làm cho vừa lòng.
khoa|Bộ phận chuyên môn trong trường đại học hoặc bệnh viện.
khoa học|Hệ thống hiểu biết về tự nhiên và xã hội có được nhờ nghiên cứu.
khoác|Mặc hoặc choàng áo bên ngoài; cũng chỉ quàng tay lên vai người khác.
khoác lác|Nói phóng đại, khoe khoang quá xa sự thật.
khoác tay|Vòng cánh tay mình vào tay người khác khi đi cùng.
khoai|Tên gọi chung các loại cây có củ ăn được như khoai lang, khoai tây.
khoái chí|Rất thích thú, hả hê trong lòng.
khoái khẩu|Hợp khẩu vị, là món mình rất thích ăn.
khoai lang|Củ vỏ đỏ tím hoặc vàng, ruột ngọt bùi, thường luộc hoặc nướng.
khoai môn|Củ to, ruột trắng có vân tím, nấu chín dẻo bùi, hay nấu chè, canh.
khoai mỡ|Loại củ ruột tím hoặc trắng, nấu canh thì sánh, còn gọi là khoai tím.
khoai sọ|Loại khoai củ tròn nhỏ, vỏ có lông, ruột dẻo, hay dùng nấu canh.
khoai tây|Củ vỏ mỏng màu vàng nâu, hay dùng để chiên, xào hoặc nấu canh.
khoan|Tạo lỗ bằng mũi nhọn xoay tròn; cũng là lời bảo người khác chờ chút.
khoan dung|Rộng lượng, sẵn lòng tha thứ cho lỗi lầm của người khác.
khoan đã|Lời bảo người khác tạm dừng lại, chờ thêm một chút.
khoang|Phần không gian rỗng bên trong tàu, xe, máy bay hoặc cơ thể.
khoảng cách|Độ xa giữa hai điểm, hai vật; cũng chỉ sự xa cách giữa người với người.
khoáng chất|Chất có sẵn trong tự nhiên như sắt, canxi, cần thiết cho cơ thể.
khoảng chừng|Từ dùng khi ước lượng, ý nói gần đúng với con số nêu ra.
khoáng sản|Tài nguyên nằm trong lòng đất như than, sắt, vàng, dầu mỏ.
khoảng trống|Chỗ còn để trống, chưa có gì lấp vào.
khoanh|Vẽ vòng tròn bao quanh; cũng chỉ một lát tròn được cắt ra.
khoanh tay|Bắt chéo hai tay trước ngực; cũng chỉ đứng nhìn mà không làm gì.
khoanh tròn|Vẽ một vòng tròn quanh chữ hoặc số để đánh dấu.
khoanh vùng|Xác định và giới hạn một khu vực để theo dõi hoặc xử lý.
khóc|Chảy nước mắt khi buồn, xúc động hoặc quá vui.
khóc lóc|Rơi nước mắt nhiều, kéo dài, thường vừa khóc vừa kể lể.
khóc nhè|Trẻ con khóc dai, mè nheo để được chiều.
khóc thầm|Khóc lặng lẽ một mình, không để ai biết.
khoe|Cho người khác thấy cái mình có để được chú ý, khen ngợi.
khoe khoang|Hay nói nhiều về cái hay của mình để người khác thán phục.
khoe mẽ|Phô trương, khoe khoang vẻ bề ngoài cho người khác thấy.
khoét|Đục hoặc cắt sâu vào để tạo thành lỗ hay chỗ lõm.
khói|Đám hơi màu xám hay trắng bốc lên khi có vật cháy.
khóm|Cụm cây nhỏ mọc sát nhau thành bụi; ở miền Nam cũng chỉ quả dứa.
khô cằn|Đất khô, cứng, thiếu nước và chất màu nên khó trồng trọt.
khô cứng|Khô và cứng lại, không còn mềm; cũng chỉ sự thiếu linh hoạt.
khô héo|Cây cối mất nước, lá úa vàng, quắt lại.
khô khốc|Khô hẳn, không còn chút nước; cũng chỉ giọng nói cộc, thiếu tình cảm.
khô ráo|Không bị ẩm ướt, khô và thoáng sạch.
khổ sở|Chịu nhiều vất vả, cực nhọc cả về thể xác lẫn tinh thần.
khổ tâm|Buồn phiền, day dứt trong lòng vì điều khó xử.
khổ thơ|Nhóm vài câu thơ liền nhau tạo thành một đoạn trong bài thơ.
khôi hài|Có tính chất hài hước, làm người khác bật cười.
khối lượng|Lượng vật chất của một vật; cũng chỉ số lượng công việc nhiều hay ít.
khôi phục|Làm cho trở lại tình trạng tốt như trước.
khôn|Biết suy xét, xử sự đúng đắn và có lợi cho mình.
khôn khéo|Biết suy xét và khéo léo trong cách ăn nói, cư xử.
khôn lớn|Lớn lên và trưởng thành, hiểu biết hơn trước.
khôn ngoan|Sáng suốt, biết suy tính và xử sự hợp lý.
không|Từ dùng để phủ định; cũng chỉ số 0 hoặc trạng thái trống rỗng.
không chuyên|Không phải dân nhà nghề, chỉ làm theo sở thích.
không chừng|Cách nói ý có thể xảy ra như vậy, biết đâu đấy.
không dám|Không đủ can đảm để làm; cũng là lời khiêm tốn khi được cảm ơn.
không đâu|Vu vơ, không có lý do; cũng là lời phủ định nhẹ nhàng.
không gian|Khoảng rộng bao la chứa mọi vật; cũng chỉ chỗ hay khoảng trống.
không hề|Từ nhấn mạnh ý hoàn toàn không, chưa từng có.
không kể|Không tính vào, để riêng ra ngoài phần đang nói.
không khí|Hỗn hợp khí quanh ta để hít thở; cũng chỉ bầu cảm xúc ở một nơi.
không lẽ|Cách hỏi tỏ ý nghi ngờ, không muốn tin điều đó là thật.
khổng lồ|To lớn hơn hẳn mức bình thường, rất đồ sộ.
không ngờ|Không nghĩ trước được là sẽ xảy ra như vậy.
không ngừng|Diễn ra liên tục, không lúc nào dừng lại.
không những|Từ nối, thường đi cùng mà còn để nêu thêm một ý nữa.
không phải|Cách nói để phủ nhận, cho biết điều gì đó không đúng.
không sao|Lời trấn an, ý nói ổn cả, không có gì phải lo.
không thể|Không có khả năng làm được, hoặc chắc chắn không xảy ra.
không trung|Khoảng không rộng lớn ở trên cao, phía trên mặt đất.
không tưởng|Chỉ có trong tưởng tượng, không thể thực hiện được.
khờ dại|Ngây thơ, thiếu hiểu biết nên dễ bị lừa hoặc làm điều dại dột.
khờ khạo|Ngờ nghệch, chậm hiểu và vụng về trong cư xử.
khơi dậy|Làm cho cảm xúc, ước mơ hay ký ức đang ngủ yên trỗi dậy.
khởi đầu|Lúc mới bắt đầu, bước đầu tiên của một việc.
khởi động|Làm cho máy bắt đầu chạy; cũng chỉ vận động nhẹ trước khi tập.
khởi hành|Bắt đầu lên đường để đi đến một nơi khác.
khởi nghiệp|Bắt đầu gây dựng công việc kinh doanh của riêng mình.
khớp|Chỗ nối giữa các xương; cũng chỉ ăn khớp, vừa vặn với nhau.
khớp xương|Chỗ hai xương nối với nhau, giúp cơ thể cử động linh hoạt.
khu nhà|Một cụm nhà nằm gần nhau trong cùng một khu vực.
khu phố|Khu dân cư gồm nhiều dãy phố, nhà ở thuộc một phường trong thành phố.
khu vực|Một vùng đất hoặc phạm vi có ranh giới nhất định.
khuân vác|Mang vác đồ vật nặng bằng vai hay lưng, thường để kiếm sống.
khuất|Bị che lấp nên không nhìn thấy được, như mặt trời khuất sau núi.
khuấy|Dùng thìa, đũa đảo đều trong nước cho tan hoặc trộn lẫn.
khuấy đảo|Làm sôi động, náo nhiệt cả một nơi; cũng là gây xáo trộn.
khuấy động|Làm cho không khí trở nên sôi nổi, náo nhiệt hơn.
khúc|Một đoạn ngắn cắt ra từ vật dài; cũng chỉ một bài hát, bản nhạc.
khúc cua|Đoạn đường uốn cong, xe cộ phải đổi hướng khi đi qua.
khúc khích|Tiếng cười nhỏ, cố nén lại, bật ra từng tràng vui vẻ.
khung|Bộ phận cứng làm sườn để đỡ hoặc bao quanh một vật, như khung ảnh.
khung cảnh|Toàn bộ cảnh vật bày ra trước mắt ở một nơi.
khung cửa|Phần khung bao quanh, giữ cánh cửa ra vào hoặc cửa sổ.
khủng long|Nhóm bò sát khổng lồ sống từ thời xa xưa, nay đã tuyệt chủng.
khung thành|Cầu môn trong bóng đá, nơi thủ môn đứng bảo vệ.
khuôn|Vật có hình dạng sẵn để đổ, đúc hoặc ép ra sản phẩm giống nhau.
khuôn khổ|Phạm vi, giới hạn được đặt ra; cũng chỉ hình dáng, kích cỡ nhất định.
khuôn mặt|Toàn bộ phần mặt của một người cùng các đường nét riêng.
khuôn mẫu|Mẫu chuẩn để làm theo; cũng chỉ lối làm cứng nhắc, rập khuôn.
khuôn viên|Khu đất bao quanh một tòa nhà, trường học hay cơ quan.
khuy áo|Cúc nhỏ đính trên áo, cài vào lỗ để đóng áo lại.
khuya|Lúc đã muộn về đêm, gần hoặc quá nửa đêm.
khuya khoắt|Lúc đêm đã muộn lắm, mọi người thường đã ngủ.
khuyên|Nói cho người khác biết nên làm điều gì tốt; cũng chỉ vòng nhỏ đeo tai.
khuyên bảo|Ân cần chỉ bảo, góp ý cho ai nên làm gì cho đúng.
khuyến cáo|Lời khuyên, cảnh báo của cơ quan, chuyên gia về điều nên hoặc không nên làm.
khuyến khích|Động viên, tạo điều kiện để người khác cố gắng làm việc gì.
khuyến nghị|Đề xuất, khuyên nên làm theo một cách nào đó, thường mang tính chuyên môn.
khuyên nhủ|Nhẹ nhàng khuyên răn bằng lời lẽ thân tình, tha thiết.
khuyên răn|Khuyên bảo, nhắc nhở để người khác tránh làm điều sai.
khuyết điểm|Điểm còn thiếu sót, chưa tốt ở người hoặc vật.
khuynh hướng|Chiều hướng mà sự việc hay suy nghĩ của con người nghiêng về.
khứ hồi|Cả lượt đi lẫn lượt về, thường nói về vé tàu xe, máy bay.
khư khư|Giữ chặt, không chịu buông ra; cũng chỉ sự cố chấp, không đổi ý.
khử mùi|Làm mất hoặc làm giảm mùi hôi khó chịu.
kia kìa|Lời chỉ cho người khác nhìn thấy cái gì ở đằng xa.
kịch|Loại hình sân khấu, diễn viên đóng vai để kể một câu chuyện.
kịch bản|Bản viết sẵn lời thoại, tình tiết cho phim hoặc vở diễn.
kịch câm|Loại kịch chỉ diễn bằng cử chỉ, nét mặt, không có lời.
kích cỡ|Độ to nhỏ, dài ngắn của đồ vật, như cỡ quần áo, giày dép.
kích hoạt|Làm cho thiết bị, tài khoản hay chức năng bắt đầu hoạt động.
kích thước|Độ lớn của vật, đo bằng chiều dài, rộng, cao.
kịch tính|Có nhiều tình tiết gay cấn, hồi hộp, bất ngờ.
kiếm|Tìm để có được thứ mình cần; cũng chỉ thanh gươm dài thời xưa.
kiếm ăn|Tìm thức ăn; cũng chỉ làm lụng để có cái ăn qua ngày.
kiếm chuyện|Cố ý gây sự, bắt bẻ để làm phiền người khác.
kiểm chứng|Đối chiếu với thực tế để xác nhận điều gì là đúng hay sai.
kiếm cớ|Tìm lý do để làm hoặc để từ chối việc gì.
kiểm định|Kiểm tra và đánh giá xem có đạt tiêu chuẩn chất lượng hay không.
kiếm lời|Mua bán hoặc đầu tư để thu về tiền lãi.
kiểm soát|Theo dõi, quản lý để mọi thứ nằm trong giới hạn cho phép.
kiếm sống|Làm việc để có tiền lo cho cuộc sống hằng ngày.
kiểm toán|Kiểm tra, xác nhận tính đúng đắn của sổ sách, báo cáo tài chính.
kiểm tra|Xem xét để biết tình trạng, chất lượng; cũng chỉ bài thi ở trường.
kiến|Côn trùng nhỏ sống thành đàn đông, chăm chỉ tha mồi về tổ.
kiên cường|Vững vàng, không chịu khuất phục trước khó khăn, thử thách.
kiến đen|Loài kiến nhỏ thân màu đen, hay bò thành đàn tìm đồ ngọt.
kiên định|Vững vàng giữ ý chí, quan điểm của mình, không dao động.
kiến đỏ|Loài kiến màu đỏ, hay làm tổ trên cây, cắn khá đau.
kiện hàng|Gói hàng được đóng gói cẩn thận để gửi hoặc vận chuyển.
kiến lửa|Loài kiến nhỏ màu nâu đỏ, đốt rất rát và ngứa.
kiên nhẫn|Bình tĩnh, bền bỉ chờ đợi hoặc làm tiếp, không nóng vội.
kiên quyết|Dứt khoát làm theo ý đã định, không lay chuyển.
kiến tạo|Xây dựng nên cái mới; trong bóng đá là tạo cơ hội cho đồng đội ghi bàn.
kiến thức|Những hiểu biết có được nhờ học tập và trải nghiệm.
kiên trì|Bền bỉ theo đuổi đến cùng, không bỏ cuộc giữa chừng.
kiến trúc|Nghệ thuật thiết kế, xây dựng nhà cửa và công trình.
kiêng|Tránh không ăn hoặc không làm điều gì vì sức khỏe hay phong tục.
kiêng cữ|Tránh không ăn hoặc không làm những điều được cho là có hại cho mình.
kiêng khem|Tránh ăn uống hoặc làm những gì không tốt cho sức khỏe.
kiệt sức|Mệt lả đến mức không còn chút sức lực nào.
kiệt tác|Tác phẩm nghệ thuật xuất sắc, có giá trị rất cao.
kiểu|Dạng, mẫu riêng của một vật; cũng chỉ cách làm, cách nói riêng.
kiểu cách|Cách cư xử, ăn nói màu mè, không tự nhiên.
kiêu căng|Tự cho mình hơn người nên tỏ ra coi thường người khác.
kiểu dáng|Hình dáng bên ngoài được thiết kế của một sản phẩm.
kiểu mẫu|Mẫu mực, tốt đẹp, đáng để mọi người noi theo.
kiêu ngạo|Tự đề cao bản thân quá mức, xem nhẹ người xung quanh.
kim chi|Món rau cải muối cay nổi tiếng của Hàn Quốc.
kim cương|Loại đá quý rất cứng, trong suốt, lấp lánh khi gặp ánh sáng.
kim giây|Kim dài và mảnh nhất trên mặt đồng hồ, nhích từng giây.
kim loại|Nhóm chất như sắt, đồng, nhôm, thường cứng, sáng bóng và dẫn điện.
kim tuyến|Sợi mỏng óng ánh màu vàng hoặc bạc, dùng để trang trí.
kín đáo|Không để lộ ra ngoài, không phô trương.
kín mít|Đóng kín hoàn toàn, không có lấy một kẽ hở.
kín tiếng|Ít khi nói ra chuyện riêng, giữ bí mật kỹ.
kính|Đồ đeo mắt hoặc tấm thủy tinh trong suốt; cũng nghĩa là tôn trọng.
kính cận|Loại kính đeo giúp người cận thị nhìn rõ vật ở xa.
kính chào|Lời chào trang trọng, thể hiện sự lễ phép, tôn trọng.
kính chúc|Lời chúc trang trọng, thường gửi tới người trên.
kinh doanh|Sản xuất, buôn bán hàng hóa hoặc dịch vụ để kiếm lời.
kính đen|Kính có tròng màu tối, đeo để che nắng.
kinh điển|Tiêu biểu, có giá trị lâu dài, được coi là mẫu mực.
kinh đô|Thành phố nơi nhà vua đóng đô thời phong kiến.
kinh giới|Loại rau thơm lá có răng cưa, mùi thơm dịu, ăn kèm bún, nem, gỏi.
kinh khủng|Rất đáng sợ hoặc rất tệ; cũng dùng để nhấn mạnh mức độ cực kỳ cao.
kính lão|Kính đeo giúp người lớn tuổi nhìn rõ chữ ở gần.
kính lúp|Dụng cụ có mặt kính lồi, giúp phóng to vật nhỏ để dễ quan sát.
kính mát|Loại kính đeo có tròng sẫm màu để che nắng và bụi.
kính mến|Vừa kính trọng vừa yêu mến, thường dành cho thầy cô, người lớn.
kính nể|Vừa tôn trọng vừa nể phục vì tài năng hay nhân cách.
kinh ngạc|Rất ngạc nhiên, sửng sốt trước điều không ngờ tới.
kinh nghiệm|Hiểu biết, kỹ năng có được nhờ đã từng trải qua thực tế.
kính phục|Tôn trọng và khâm phục ai đó từ đáy lòng.
kính râm|Mắt kính tròng tối màu, đeo để đỡ chói khi trời nắng.
kinh tế|Hoạt động sản xuất, buôn bán của một nước; cũng chỉ tiết kiệm, ít tốn kém.
kinh thành|Thành phố nơi vua ở và đóng đô thời phong kiến.
kính thưa|Lời mở đầu trang trọng khi phát biểu trước mọi người.
kính trọng|Tôn trọng và quý mến người trên hoặc người đáng nể.
kính yêu|Vừa kính trọng vừa yêu thương sâu sắc.
kịp thời|Đúng lúc cần, không chậm trễ.
la bàn|Dụng cụ có kim nam châm luôn chỉ hướng bắc nam.
la cà|Đi chơi lang thang, ghé chỗ này chỗ kia, không vội về.
lá cờ|Tấm vải có màu sắc, hình riêng, tượng trưng cho một nước hay tổ chức.
lá dứa|Lá cây dài màu xanh, mùi thơm, dùng tạo màu và hương cho bánh, xôi, chè.
lạ đời|Kỳ quặc, trái với lẽ thường, ít ai gặp.
lá gan|Cơ quan lớn trong bụng giúp lọc chất độc; cũng chỉ lòng can đảm.
la hét|Kêu to, gào lên ầm ĩ vì sợ, giận hoặc phấn khích.
lạ hoắc|Hoàn toàn lạ, chưa từng thấy hay biết bao giờ.
là lạ|Hơi lạ, có gì đó khác thường một chút.
lạ lẫm|Mới mẻ, chưa quen thuộc, khiến thấy bỡ ngỡ.
la liệt|Nằm hoặc bày ra rất nhiều, ở khắp mọi chỗ.
lá lốt|Lá cây hình tim, mùi thơm hăng, dùng cuốn thịt nướng hoặc nấu canh.
lạ lùng|Rất khác thường, khiến người ta ngạc nhiên.
la mắng|Mắng mỏ to tiếng khi không vừa ý với ai.
lạ mắt|Trông mới và khác thường, gây chú ý khi nhìn.
lạ miệng|Món ăn mới, khác thường, ăn thấy thích vì chưa quen.
lá sen|Chiếc lá to, tròn của cây sen, thường dùng gói xôi, gói cốm.
lạ thường|Khác hẳn bình thường, đến mức đáng ngạc nhiên.
lạc đà|Loài thú lớn có bướu trên lưng, sống ở sa mạc, chịu khát giỏi.
lác đác|Rải rác thưa thớt, chỗ này một ít, chỗ kia một ít.
lạc đề|Nói hoặc viết ra ngoài nội dung, chủ đề được yêu cầu.
lạc đường|Không tìm được đường đúng, không biết phải đi lối nào.
lạc hậu|Cũ kỹ, chậm tiến, thua kém so với thời đại.
lạc hướng|Đi sai phương hướng; cũng chỉ việc suy nghĩ, làm việc sai mục tiêu.
lạc lõng|Lẻ loi, không hòa hợp với những người hoặc thứ xung quanh.
lạc lối|Đi nhầm đường; cũng chỉ việc sa vào con đường sai trái.
lạc quan|Luôn tin tưởng, nhìn mọi việc theo hướng tốt đẹp.
lách|Luồn người qua chỗ chật hẹp, đông đúc; cũng chỉ khéo né tránh quy định.
lạch bạch|Dáng đi chậm, lắc lư nặng nề như con vịt.
lách cách|Tiếng kim loại hoặc vật cứng va chạm nhẹ vào nhau liên tiếp.
lách tách|Tiếng nổ nhỏ, giòn và liên tiếp, như củi cháy hoặc mưa rơi.
lái đò|Người chèo, điều khiển con đò chở khách qua sông.
lải nhải|Nói đi nói lại mãi một điều khiến người nghe khó chịu.
lại nữa|Thêm lần nữa, thường tỏ ý chán vì việc cứ lặp lại; cũng là thêm vào đó.
lái xe|Điều khiển cho xe chạy; cũng chỉ người làm nghề cầm lái.
làm ăn|Lao động để kiếm sống; thường chỉ việc buôn bán, kinh doanh.
làm ẩu|Làm cẩu thả, qua loa, không cẩn thận.
làm bài|Giải bài tập hoặc trả lời câu hỏi trong bài thi.
làm bạn|Kết thân và trở thành bạn của ai đó.
làm bếp|Đảm nhận việc nấu nướng trong nhà hoặc ở quán ăn.
làm biếng|Lười, không muốn bỏ công sức làm việc.
làm bộ|Giả vờ như thật; cũng chỉ làm ra vẻ ta đây.
làm cho|Khiến ai hoặc việc gì trở nên như thế; cũng chỉ làm việc cho người khác.
làm chủ|Sở hữu, đứng đầu công việc làm ăn; cũng chỉ tự điều khiển được bản thân.
làm công|Đi làm thuê cho người khác để nhận tiền công.
làm cơm|Nấu nướng chuẩn bị một bữa ăn, thường để mời khách.
làm dáng|Chăm chút, sửa sang vẻ ngoài cho đẹp để người khác chú ý.
làm dâu|Về sống bên nhà chồng với vai trò con dâu sau khi cưới.
làm dịu|Khiến cho bớt căng thẳng, bớt gay gắt hoặc dễ chịu hơn.
làm đổ|Vô ý khiến đồ vật ngã xuống hoặc nước bên trong tràn ra.
làm đồng|Ra ruộng cày cấy, chăm lúa và làm các việc nhà nông.
làm gì|Cụm từ để hỏi về việc đang làm; cũng dùng để phủ định, như làm gì có.
làm giàu|Buôn bán, làm ăn để có thêm của cải, trở nên giàu có.
làm giúp|Thay người khác thực hiện một phần việc của họ.
làm gương|Cư xử tốt để người khác nhìn vào mà noi theo.
làm hỏng|Gây ra hư hại khiến đồ vật hoặc công việc không còn tốt.
làm hư|Gây hỏng đồ vật; cũng chỉ chiều chuộng quá khiến trẻ hư.
làm khách|Đến chơi nhà người khác với tư cách là khách; cũng chỉ thái độ khách sáo, ngại ngùng.
làm khó|Cố ý gây khó khăn, trở ngại cho người khác.
làm lại|Bắt tay vào thực hiện thêm lần nữa, thường từ đầu, cho tốt hơn.
làm lạnh|Hạ nhiệt độ của vật hoặc không khí xuống cho mát, cho lạnh.
làm lễ|Tiến hành một nghi thức trang trọng nhân dịp đặc biệt.
làm liều|Hành động bừa, không cân nhắc dù biết có thể gặp rủi ro.
làm lơ|Giả như không thấy, không biết để khỏi phải để ý.
làm lụng|Làm việc vất vả, chăm chỉ để kiếm sống.
làm mẫu|Thực hiện trước để người khác làm theo; cũng là tạo dáng cho người vẽ, chụp ảnh.
làm mối|Đứng ra giới thiệu hai người quen nhau để tiến tới yêu đương, cưới hỏi.
làm nên|Tạo dựng được thành quả lớn; cũng chỉ việc thành đạt trong cuộc sống.
làm ngơ|Cố tình tỏ ra không thấy, không biết để khỏi phải bận tâm.
lảm nhảm|Nói lẩm bẩm những câu không rõ ràng, chẳng có ý nghĩa.
làm nũng|Nhõng nhẽo, tỏ vẻ đáng yêu để được chiều chuộng.
làm ồn|Gây tiếng động lớn, ầm ĩ, ảnh hưởng người xung quanh.
làm phiền|Quấy rầy, gây phiền hà khiến người khác mất thời gian hoặc khó chịu.
làm quen|Bắt chuyện, tiếp xúc để quen biết ai; cũng là tập cho quen với điều mới.
làm ra|Tạo ra hoặc sản xuất được thứ gì đó; cũng chỉ việc kiếm ra tiền.
làm ruộng|Làm nghề trồng lúa và hoa màu trên đồng ruộng.
làm sao|Từ dùng để hỏi bằng cách nào; cũng để hỏi có chuyện gì xảy ra.
làm theo|Thực hiện đúng như lời dặn, hướng dẫn hoặc như người khác đã làm.
làm thuê|Nhận làm công việc cho người khác để lấy tiền công.
làm tiệc|Chuẩn bị và tổ chức một bữa tiệc.
làm tổ|Chim hoặc con vật kết, đắp chỗ ở để đẻ trứng, nuôi con.
làm trò|Biểu diễn trò vui cho người xem; cũng chỉ cử chỉ lố lăng để gây cười.
làm tròn|Hoàn thành đầy đủ, chu đáo; cũng là lấy số gần đúng cho gọn, bỏ phần lẻ.
làm việc|Dùng sức lực, trí óc để làm một công việc, thường để kiếm sống.
làm vườn|Trồng trọt, chăm sóc cây cối, rau hoa trong vườn.
làm xong|Hoàn thành công việc, không còn gì phải làm thêm.
lan can|Hàng rào thấp chắn ở ban công, cầu thang, thành cầu.
lan man|Nói hoặc viết dài dòng, hết chuyện này sang chuyện khác, thiếu tập trung.
làn sóng|Đợt sóng nước nhấp nhô; cũng chỉ một trào lưu lan rộng trong xã hội.
lan tràn|Loang rộng ra khắp nơi, khó mà ngăn chặn được.
lan truyền|Truyền đi rộng ra nhiều người, nhiều nơi.
làng|Khu dân cư ở nông thôn, gồm nhiều gia đình sống quây quần.
láng giềng|Người, nhà hoặc nước ở gần bên cạnh nhau.
làng mạc|Các làng xóm ở vùng nông thôn nói chung.
lãng phí|Tiêu dùng tiền bạc, thời gian, công sức một cách phí phạm, vô ích.
lãng quên|Không còn nhớ đến, để mờ dần theo thời gian.
lang thang|Đi đây đi đó, không có mục đích rõ ràng.
lảng tránh|Cố ý tránh né, không muốn gặp hoặc không muốn nói đến.
lảng vảng|Đi lại quanh quẩn gần một nơi, không rõ mục đích.
làng xóm|Làng và xóm, cộng đồng những người sống gần nhau ở nông thôn.
lạnh|Có nhiệt độ thấp, khiến cơ thể thấy rét.
lạnh buốt|Rất lạnh, cái lạnh thấm vào da thịt gây tê buốt.
lạnh cóng|Rét đến mức chân tay tê cứng, khó cử động.
lạnh giá|Rét buốt, nhiệt độ xuống rất thấp như mùa đông.
lành lặn|Còn nguyên vẹn, không bị rách, vỡ hay sứt mẻ gì.
lạnh lẽo|Rét và vắng vẻ, thiếu hơi ấm, gợi cảm giác cô quạnh.
lanh lợi|Nhanh nhẹn, sáng dạ và ứng xử khéo léo.
lạnh lùng|Tỏ ra thờ ơ, ít cảm xúc, không thân thiện với người khác.
lành mạnh|Tốt cho thể chất và tinh thần, không có điều xấu hay có hại.
lạnh ngắt|Nguội hẳn, rét buốt, không còn chút hơi ấm nào.
lạnh nhạt|Thờ ơ, hờ hững, không còn thân mật như trước.
lạnh tanh|Lạnh lẽo, vắng vẻ; cũng chỉ thái độ thờ ơ, không chút tình cảm.
lao công|Người làm công việc quét dọn, giữ vệ sinh nơi công cộng.
lảo đảo|Đi đứng nghiêng ngả, không vững như sắp ngã.
lao động|Làm việc bằng chân tay hoặc trí óc để tạo ra của cải.
lão làng|Người lâu năm, giàu kinh nghiệm trong một nghề hay lĩnh vực.
lau chùi|Dùng khăn lau, cọ cho sạch bụi bẩn.
lavabo|Bồn rửa tay, rửa mặt gắn trên tường trong nhà tắm.
lắc đầu|Quay đầu sang hai bên để tỏ ý không đồng ý, từ chối.
lắc lư|Nghiêng qua nghiêng lại nhẹ nhàng, liên tục.
lăn bánh|Bánh xe bắt đầu quay, xe khởi hành và chạy đi.
lặn lội|Vất vả vượt đường xa, khó khăn để đến nơi hoặc lo liệu việc gì.
lăn tăn|Gợn sóng nhỏ li ti trên mặt nước; cũng chỉ sự băn khoăn, đắn đo.
lặng im|Không nói, không phát ra tiếng động nào.
lặng lẽ|Âm thầm, yên lặng, không gây chú ý.
lắng nghe|Chú ý nghe kỹ để hiểu điều người khác nói.
lằng nhằng|Rắc rối, dây dưa, không rõ ràng, khó dứt ra.
lắp đặt|Gắn, đặt thiết bị vào đúng chỗ để sử dụng.
lắp ghép|Ráp các bộ phận, mảnh rời lại với nhau thành vật hoàn chỉnh.
lặt vặt|Nhỏ nhặt, nhiều thứ linh tinh, không quan trọng.
lẩm bẩm|Nói nhỏ trong miệng, chỉ mình nghe rõ.
lẩm cẩm|Hay nói và làm những điều lẫn lộn, không đâu vào đâu, thường do tuổi già.
lấm lem|Bị dính bẩn, nhem nhuốc khắp người.
lấm tấm|Có nhiều chấm nhỏ li ti rải rác trên bề mặt.
lấn át|Vượt trội, đè lên làm cho cái khác bị lu mờ.
lẫn lộn|Trộn vào nhau, không phân biệt rõ cái nào với cái nào.
lần lượt|Theo thứ tự, cái này xong rồi mới đến cái kia.
lần mò|Dò dẫm từng chút để tìm kiếm hoặc đi trong bóng tối.
lẫn nhau|Qua lại giữa hai hay nhiều bên với nhau, như giúp đỡ nhau.
lấn sân|Làm thêm việc ở lĩnh vực khác với nghề chính của mình.
lẩn tránh|Tránh mặt, lánh đi để không phải gặp hoặc đối mặt.
lẩn trốn|Trốn vào chỗ kín để người khác không tìm thấy.
lâng lâng|Cảm giác nhẹ nhàng, bồng bềnh như đang bay, thường khi rất vui.
lập công|Làm được việc có ích, đạt thành tích được ghi nhận; trong bóng đá là ghi bàn.
lấp lánh|Phát ra ánh sáng nhỏ lóe lên liên tục, long lanh đẹp mắt.
lấp ló|Lúc ẩn lúc hiện, chỉ lộ ra một phần.
lập luận|Đưa ra lý lẽ có hệ thống để chứng minh một ý kiến.
lập nghiệp|Gây dựng sự nghiệp riêng, tự làm ăn để có cuộc sống ổn định.
lập trình|Viết mã, câu lệnh để máy tính thực hiện công việc.
lập tức|Ngay khi đó, không chần chừ, không chậm trễ.
lật đật|Vội vàng, hấp tấp; cũng là đồ chơi đáy tròn, đẩy ngã lại tự đứng dậy.
lật ngược|Đảo mặt dưới lên trên; cũng chỉ việc xoay chuyển hẳn tình thế.
lật tẩy|Vạch trần, làm lộ ra mánh khóe hay điều đang che giấu.
lật úp|Lật ngược lại, mặt trên quay xuống dưới.
lâu bền|Bền chắc, tồn tại hoặc giữ được trong thời gian dài.
lâu đài|Tòa nhà lớn, nguy nga, thường là nơi ở của vua chúa, quý tộc.
lâu đời|Có từ rất lâu, truyền qua nhiều thế hệ.
lâu lâu|Thỉnh thoảng, cách một khoảng thời gian mới có một lần.
lâu nay|Trong suốt một thời gian dài tính đến bây giờ.
lâu năm|Đã tồn tại hoặc gắn bó trong nhiều năm.
lâu ngày|Trải qua nhiều ngày, một khoảng thời gian dài.
lấy chồng|Người con gái kết hôn, về sống với chồng.
lấy cớ|Viện ra một lý do để biện minh hoặc né tránh việc gì.
lấy được|Giành, nhận được thứ mình cần; cũng chỉ việc cố làm cho bằng được.
lấy lại|Nhận về hoặc khôi phục cái đã mất, đã cho mượn.
lấy lòng|Làm vừa ý người khác để được họ quý mến.
lầy lội|Đường sá nhiều bùn nhão, ướt, khó đi.
lấy nhau|Hai người cưới nhau, trở thành vợ chồng.
lấy vợ|Người đàn ông kết hôn, cưới một người làm vợ.
lẻ loi|Một mình, cô đơn, không có ai bên cạnh.
lẽ nào|Từ đặt đầu câu hỏi để tỏ ý không tin, cho rằng điều đó vô lý.
lẽ phải|Điều đúng đắn, hợp đạo lý mà mọi người đều thừa nhận.
lẽ ra|Theo lẽ thường thì phải như vậy, nhưng thực tế lại khác.
lẻ tẻ|Rời rạc, rải rác từng ít một, không tập trung.
lém lỉnh|Nhanh nhẹn, hóm hỉnh, hay pha trò tinh nghịch.
lén lút|Giấu giếm, làm vụng trộm để người khác không biết.
leng keng|Tiếng kim loại va vào nhau nghe trong và vui tai.
leo dây|Bám vào sợi dây để trèo lên cao, một môn rèn luyện thể lực.
lẽo đẽo|Đi theo sau một cách chậm chạp, dai dẳng không rời.
leo thang|Bước lên cầu thang; cũng chỉ mức độ ngày càng tăng cao.
leo trèo|Bám tay chân để đưa người lên chỗ cao.
lép vế|Ở thế yếu hơn, bị người khác lấn át.
lễ cưới|Buổi lễ tổ chức để chúc mừng đôi trai gái thành vợ chồng.
lễ độ|Có thái độ, lời nói lịch sự, đúng mực với mọi người.
lề đường|Phần mép hai bên con đường, sát với vỉa hè.
lễ hội|Dịp vui chung của cộng đồng, có nghi lễ và nhiều hoạt động vui chơi.
lê la|Ngồi la cà hết chỗ này đến chỗ khác, mất nhiều thời gian.
lê lết|Bước đi chậm chạp, khó nhọc như phải kéo lê thân mình.
lề mề|Chậm chạp, kéo dài thời gian, làm việc không dứt khoát.
lễ phép|Cư xử kính trọng, ngoan ngoãn với người lớn.
lệ phí|Khoản tiền phải nộp khi làm thủ tục hoặc dùng dịch vụ công.
lễ tân|Người hoặc bộ phận đón tiếp, hướng dẫn khách ở cơ quan, khách sạn.
lệch|Nghiêng về một phía, không ngay ngắn; cũng chỉ sự chênh nhau, sai khác.
lên án|Phê phán gay gắt, cho là sai trái và đáng chê trách.
lên bờ|Từ dưới nước hoặc trên thuyền bước lên đất liền.
lên cao|Di chuyển lên chỗ cao hơn; cũng chỉ sự tăng lên, như giá cả lên cao.
lên cân|Cân nặng của cơ thể tăng thêm.
lên chức|Được đề bạt lên vị trí, chức vụ cao hơn.
lên đường|Bắt đầu chuyến đi, rời nơi đang ở để đi xa.
lên giá|Giá cả tăng lên, đắt hơn so với trước đó.
lên lớp|Được học lớp trên sau khi hết năm học; cũng chỉ việc giảng bài trên lớp.
lên mặt|Tỏ ra kiêu ngạo, tự cho mình hơn người khác.
lên mây|Cảm giác sung sướng, lâng lâng như bay bổng; cũng chỉ giá cả tăng vọt.
lên men|Biến đổi nhờ vi sinh vật, như khi làm sữa chua, muối dưa.
lên ngôi|Bắt đầu làm vua; cũng chỉ việc trở nên nổi bật, được ưa chuộng.
lên tiếng|Nói ra ý kiến, quan điểm của mình về một việc.
lệnh|Điều cấp trên yêu cầu phải làm theo; cũng chỉ câu lệnh cho máy tính.
lêu lổng|Ham chơi, không chịu học hành hay làm việc gì.
lịch|Bảng ghi ngày, tháng trong năm; cũng chỉ thời gian biểu sắp sẵn.
lịch lãm|Có phong cách sang trọng, từng trải và cư xử tinh tế.
lịch sự|Cư xử nhã nhặn, đúng phép tắc, tôn trọng người khác.
lịch trình|Kế hoạch sắp xếp thời gian, địa điểm cho chuyến đi hay công việc.
liếc|Đưa mắt nhìn nhanh sang một bên.
liếc mắt|Đưa mắt nhìn sang một cách nhanh và kín đáo.
liềm|Nông cụ có lưỡi cong như trăng khuyết, dùng gặt lúa, cắt cỏ.
liền|Ngay lập tức; cũng chỉ nối sát với nhau, không đứt quãng.
liên doanh|Hai hay nhiều bên cùng góp vốn để kinh doanh chung, thường có bên nước ngoài.
liên đoàn|Tổ chức liên kết nhiều hội, đoàn thể cùng loại, như liên đoàn bóng đá.
liên hệ|Giữ liên lạc với ai; cũng chỉ mối quan hệ giữa các sự việc.
liên hoan|Bữa tiệc vui chung của một tập thể nhân dịp đặc biệt.
liên kết|Gắn bó, nối với nhau thành một khối; cũng chỉ đường dẫn trên mạng.
liên lạc|Giữ thông tin qua lại với nhau bằng thư, điện thoại.
liên miên|Kéo dài liên tiếp, hết đợt này đến đợt khác.
liên quan|Có dính dáng, có mối quan hệ với nhau.
liên tiếp|Nối tiếp nhau, cái này vừa xong đến cái khác.
liên tục|Diễn ra không ngừng, không bị gián đoạn.
liên tưởng|Từ việc này nghĩ ngay đến việc khác có điểm giống hoặc gần gũi.
liệt kê|Kể ra lần lượt từng thứ một.
liễu|Cây có cành mềm rủ xuống, lá dài thon, hay trồng ven hồ.
liều lĩnh|Dám làm việc mạo hiểm mà không lường hết hậu quả.
lim dim|Mắt khép hờ, không nhắm hẳn, như sắp ngủ.
linh cảm|Cảm nhận trước điều sắp xảy ra mà không giải thích được.
linh cẩu|Loài thú hoang ở châu Phi, tiếng kêu nghe như tiếng cười.
linh chi|Loại nấm quý, thân cứng, thường dùng để pha nước uống bồi bổ.
linh động|Không cứng nhắc, biết xử lý tùy theo hoàn cảnh.
linh hoạt|Nhanh nhẹn, dễ thay đổi cho phù hợp với tình hình.
linh kiện|Bộ phận nhỏ dùng để lắp ráp máy móc, thiết bị điện tử.
lỉnh kỉnh|Nhiều đồ đạc lặt vặt, cồng kềnh, mang vác vướng víu.
linh tinh|Lặt vặt, lộn xộn nhiều thứ; cũng chỉ nói hay làm lung tung.
líu lo|Tiếng chim hót hoặc tiếng nói trong trẻo, ríu rít liên tiếp.
lò cò|Nhảy bằng một chân; cũng là trò chơi nhảy ô của trẻ em.
lo lắng|Không yên lòng vì sợ có điều không hay xảy ra.
lọ lem|Lem luốc vì dính nhọ nồi; cũng là tên cô gái hiền trong truyện cổ tích.
lo liệu|Sắp xếp, tính toán để mọi việc được ổn thỏa.
lo ngại|E rằng điều không tốt có thể xảy ra nên thấy bất an.
lo nghĩ|Băn khoăn, suy tính nhiều vì lo lắng cho việc gì.
lò rèn|Xưởng nung nóng kim loại rồi đập thành nông cụ, đồ dùng.
lò sưởi|Chỗ đốt lửa hoặc thiết bị tỏa nhiệt để làm ấm phòng.
lo xa|Tính trước, chuẩn bị sẵn cho những việc có thể xảy ra về sau.
lò xo|Dây kim loại cuộn xoắn, đàn hồi, bị nén hay kéo xong thì bật lại.
loại|Nhóm có chung đặc điểm; cũng nghĩa là gạt bỏ ra ngoài.
loại bỏ|Bỏ đi, gạt ra những thứ không cần thiết hoặc không phù hợp.
loại hình|Kiểu, dạng chung của một hoạt động hay sự vật.
loài người|Toàn thể con người trên Trái Đất nói chung.
loại trừ|Gạt ra ngoài, không tính đến trong số đang xét.
loạn xạ|Lộn xộn, hỗn loạn, không theo trật tự nào.
loãng|Có nhiều nước, ít chất hòa tan; cũng chỉ không khí thưa.
loạng choạng|Đi đứng không vững, người nghiêng ngả như sắp ngã.
loang lổ|Có nhiều mảng màu, vết loang không đều trên bề mặt.
loáng thoáng|Thấp thoáng, không rõ ràng; cũng chỉ lưa thưa, rải rác.
loanh quanh|Đi quanh quẩn ở một chỗ; cũng chỉ nói vòng vo.
loạt|Nhiều cái cùng loại nối tiếp nhau thành một chuỗi.
loay hoay|Xoay xở mãi mà chưa làm xong việc.
loằng ngoằng|Nhiều đường cong queo, rối rắm, khó theo dõi.
lòng đào|Trứng luộc chín vừa tới, lòng đỏ còn mềm và sánh.
lòng đất|Phần nằm sâu bên dưới bề mặt đất.
lòng đỏ|Phần tròn màu vàng cam ở giữa quả trứng.
lòng đường|Phần giữa của con đường, dành cho xe cộ đi lại.
lỏng lẻo|Không chặt, không khít; cũng chỉ sự quản lý, quan hệ thiếu chặt chẽ.
lóng ngóng|Vụng về, lúng túng, không biết làm sao cho đúng.
lòng sông|Phần trũng nằm giữa hai bờ sông, nơi nước chảy qua.
lòng thành|Tấm lòng chân thật, ngay thẳng dành cho người khác.
lòng tin|Sự tin tưởng, tin cậy dành cho ai hoặc điều gì.
lòng trắng|Phần trong suốt bao quanh lòng đỏ trứng, nấu chín thì có màu trắng.
long trọng|Được tổ chức trang nghiêm, chu đáo và đầy đủ nghi thức.
lòng vòng|Đi hoặc nói quanh co, vòng vèo, không vào thẳng vấn đề.
lót dạ|Ăn chút ít cho đỡ đói, chưa phải bữa chính.
lót lòng|Ăn chút gì vào buổi sáng sớm cho ấm bụng.
lỗ chỗ|Có nhiều lỗ nhỏ hoặc vết lõm rải rác trên bề mặt.
lộ diện|Xuất hiện, để lộ mặt ra cho mọi người thấy.
lỗ hổng|Chỗ trống bị khuyết; cũng chỉ phần thiếu sót, như lỗ hổng kiến thức.
lỗ lãi|Thua lỗ hay có lãi trong buôn bán, kinh doanh.
lỗ mũi|Hai lỗ nhỏ ở mũi, nơi không khí đi vào khi thở.
lỗ rốn|Vết lõm nhỏ giữa bụng, nơi cuống rốn rụng đi sau khi sinh.
lỗ tai|Phần lỗ ở tai dẫn âm thanh vào trong; cũng dùng chỉ cái tai.
lỗ thủng|Chỗ bị thủng xuyên qua trên bề mặt của một vật.
lộ trình|Con đường đi đã định sẵn; cũng chỉ kế hoạch thực hiện theo từng bước.
lỗ vốn|Thu về ít hơn số tiền đã bỏ ra để buôn bán, làm ăn.
lôi cuốn|Có sức hấp dẫn, khiến người khác bị thu hút theo.
lối đi|Đường nhỏ dành để đi lại; cũng chỉ hướng đi, cách làm riêng.
lôi kéo|Rủ rê, thuyết phục người khác theo mình hoặc tham gia việc gì.
lỗi lầm|Những việc làm sai, điều sai sót mình đã mắc phải.
lồi lõm|Bề mặt chỗ nhô lên, chỗ lõm xuống, không bằng phẳng.
lối ra|Cửa hoặc con đường để đi ra ngoài.
lối sống|Cách sống, thói quen sinh hoạt của một người hoặc một nhóm.
lối thoát|Đường để ra khỏi nơi nguy hiểm; cũng chỉ cách gỡ khi gặp bế tắc.
lỗi thời|Không còn hợp với thời nay, đã cũ, lạc hậu.
lối vào|Cửa hoặc đường để đi vào bên trong.
lốm đốm|Có nhiều chấm, vết nhỏ khác màu xen lẫn nhau.
lộn ngược|Bị đảo đầu xuống dưới, đáy lên trên, ngược với bình thường.
lộn nhào|Lộn người một vòng qua đầu; cũng chỉ ngã chúi đầu xuống.
lộn xộn|Bừa bãi, không gọn gàng, không có trật tự.
lông|Sợi nhỏ mọc trên da người và thú, hoặc phủ trên mình chim.
lông bông|Không có việc làm ổn định, sống rong chơi, vô định.
lồng đèn|Đèn khung tre bọc giấy màu, thắp nến bên trong, trẻ em rước dịp Trung thu.
lông lá|Có nhiều lông mọc rậm rạp trên mình, trên tay chân.
lộng lẫy|Đẹp rực rỡ, sang trọng, nổi bật.
lông mày|Hàng lông ngắn mọc thành vệt cong ở phía trên mắt.
lồng tiếng|Thu giọng nói thay cho nhân vật trong phim, phim hoạt hình.
lông tơ|Sợi lông rất mảnh, mềm và mịn, như ở gà con, trên má em bé.
lông vũ|Bộ lông của loài chim, mỗi chiếc có cuống giữa và hai bên tơ mảnh.
lộp bộp|Tiếng kêu như hạt mưa to rơi trên lá hoặc mái tôn.
lộp độp|Tiếng kêu đều đều của những giọt nước rơi xuống mái nhà, mặt lá.
lột vỏ|Bóc bỏ lớp vỏ bên ngoài của trái cây, tôm, trứng.
lột xác|Trút bỏ lớp da, vỏ cũ để lớn lên; cũng chỉ sự thay đổi hoàn toàn.
lơ đễnh|Không chú ý, không tập trung vào việc đang làm.
lờ đờ|Chậm chạp, mắt thiếu tinh nhanh vì mệt hoặc buồn ngủ.
lỡ hẹn|Không đến được đúng như đã hẹn với ai.
lơ là|Thiếu chú ý, không chăm chút, xem nhẹ việc cần làm.
lỡ lời|Vô ý nói ra điều không nên nói.
lơ lửng|Treo hay trôi giữa khoảng không, không bám vào đâu.
lỡ miệng|Buột miệng nói ra điều lẽ ra phải giữ kín hoặc không nên nói.
lờ mờ|Không rõ nét, chỉ thấy hoặc hiểu một cách mơ hồ.
lời chúc|Câu nói bày tỏ mong muốn tốt đẹp dành cho người khác.
lợi dụng|Tận dụng thời cơ; thường chỉ việc dựa vào người khác để mưu lợi riêng.
lời giải|Cách giải và đáp án cho một bài toán, câu đố.
lợi hại|Cái lợi và cái hại; cũng chỉ người hay vật rất giỏi, đáng gờm.
lời hứa|Điều đã nói ra và cam kết sẽ làm.
lợi ích|Điều có lợi, mang lại tác dụng tốt.
lời khen|Câu nói ghi nhận, đánh giá tốt về ai hoặc việc gì.
lời khuyên|Ý kiến góp cho người khác để họ làm điều tốt hơn.
lời lẽ|Cách dùng từ ngữ, câu chữ khi nói hoặc viết.
lời lỗ|Tiền lãi hoặc tiền thua lỗ khi làm ăn, mua bán.
lợi nhuận|Khoản tiền lời thu được sau khi trừ mọi chi phí.
lời nói|Những điều nói ra bằng miệng để diễn đạt ý nghĩ.
lợi thế|Điều kiện thuận lợi giúp hơn người khác.
lời văn|Cách dùng từ ngữ, câu chữ trong một bài viết.
lởm chởm|Nhô lên không đều, gồ ghề, nhọn hoắt.
lớn lao|To lớn, quan trọng, có ý nghĩa sâu rộng.
lớn lên|Phát triển, trưởng thành dần theo thời gian.
lớn mạnh|Phát triển to hơn, vững vàng và mạnh hơn.
lợn rừng|Loài lợn hoang sống trong rừng, lông cứng, có răng nanh dài.
lớn tiếng|Nói to giọng, gắt gỏng, thường khi cãi nhau hoặc bực tức.
lớn tuổi|Đã có nhiều tuổi, không còn trẻ.
lớp áo|Áo mặc theo từng lớp trong, ngoài; cũng chỉ vẻ ngoài mới được khoác lên.
lớp học|Nhóm học sinh học cùng nhau; cũng chỉ phòng dùng để dạy học.
lớp sơn|Màng sơn phủ bên ngoài tường, đồ vật để bảo vệ và trang trí.
lu bù|Rất nhiều và liên tục, hết việc này đến việc khác.
lu mờ|Trở nên mờ nhạt, kém nổi bật so với trước hoặc với cái khác.
lúa mạch|Cây lương thực vùng ôn đới, hạt dùng làm bột, ngũ cốc, mạch nha.
lúa nếp|Giống lúa cho hạt gạo nếp dẻo thơm, dùng nấu xôi, làm bánh.
luân lưu|Lần lượt thay phiên nhau; trong bóng đá là loạt sút phạt đền phân thắng thua.
luận văn|Bài nghiên cứu viết ra để bảo vệ khi tốt nghiệp đại học, cao học.
lục địa|Vùng đất liền rất rộng lớn trên trái đất, như châu Á, châu Phi.
lúc đó|Vào thời điểm đã nhắc đến, thường là trong quá khứ.
lục giác|Hình phẳng có sáu cạnh và sáu góc, như ô tổ ong.
lục lạc|Chuông nhỏ hình tròn, có hạt bên trong, rung kêu leng keng.
lục lọi|Bới tìm khắp nơi, lật tung đồ đạc để tìm kiếm.
lúc này|Vào thời điểm hiện tại, ngay bây giờ.
lùi bước|Lui về phía sau; cũng chỉ việc nản lòng, chịu thua trước khó khăn.
lủi thủi|Lặng lẽ một mình, trông lẻ loi, buồn bã.
lung lay|Bị lay động, không còn đứng vững chắc; cũng chỉ niềm tin bị dao động.
lủng lẳng|Treo đung đưa, lơ lửng ở trên cao.
lung linh|Ánh sáng lấp lánh, chập chờn trông rất đẹp mắt.
lung tung|Lộn xộn, bừa bãi, không theo trật tự nào.
luộc|Nấu chín thức ăn trong nước sôi.
luộm thuộm|Ăn mặc hoặc sắp xếp bừa bộn, thiếu gọn gàng.
luôn luôn|Vào mọi lúc, lúc nào cũng như thế.
luôn tiện|Nhân lúc đang làm việc này thì làm thêm việc khác.
luống cuống|Lúng túng, cuống quýt, không biết xử lý thế nào.
luyện|Tập đi tập lại nhiều lần cho thật thành thạo một kỹ năng.
luyện tập|Tập đều đặn, thường xuyên để giỏi hơn hoặc khỏe hơn.
luyến tiếc|Tiếc nuối, không muốn rời xa điều đã qua.
lựa chọn|Xem xét rồi lấy ra cái phù hợp nhất trong nhiều cái.
lửa trại|Đống lửa lớn đốt ngoài trời để mọi người quây quần, sinh hoạt.
lứa tuổi|Khoảng tuổi gần nhau của một nhóm người, như tuổi học trò.
lực lượng|Tập hợp người hoặc sức mạnh được tổ chức để làm một nhiệm vụ chung.
lưng|Phần thân phía sau, từ vai xuống đến hông.
lưng chừng|Ở khoảng giữa, chưa tới nơi hoặc chưa xong hẳn.
lửng lơ|Ở lưng chừng, không rõ ràng dứt khoát, như câu trả lời lửng lơ.
lưới|Đồ đan bằng sợi thành nhiều mắt, dùng để đánh cá hoặc che chắn.
lười biếng|Không chịu làm việc, ngại khó, ngại vất vả.
lưỡi câu|Móc nhỏ bằng kim loại, có ngạnh, gắn mồi để câu cá.
lưới điện|Hệ thống đường dây và trạm dẫn điện từ nhà máy đến nơi sử dụng.
lưỡi liềm|Phần lưỡi cong bằng sắt của chiếc liềm gặt lúa; cũng tả hình trăng non.
lười nhác|Ngại làm, không chịu chăm chỉ, chỉ thích nghỉ ngơi.
lưới sắt|Tấm đan bằng dây thép thành ô, dùng để rào, che chắn.
lượm|Cúi xuống nhặt lấy vật đang nằm dưới đất.
lươn|Con vật thân dài như rắn, da trơn, màu vàng nâu, sống dưới bùn.
lượn lờ|Đi qua đi lại nhiều lần, chậm rãi quanh một chỗ.
lượn sóng|Có hình uốn cong nhấp nhô như những con sóng.
lương|Tiền công trả định kỳ cho người làm việc, thường theo tháng.
lương bổng|Tiền lương và các khoản thu nhập từ công việc.
lương khô|Thức ăn khô ép thành bánh, để được lâu, tiện mang khi đi xa.
lưỡng lự|Do dự, chưa quyết định được nên làm thế nào.
lượng mưa|Tổng lượng nước mưa rơi xuống một vùng trong một khoảng thời gian.
lương tâm|Tiếng nói bên trong giúp con người phân biệt điều đúng, điều sai.
lương thiện|Hiền lành, ngay thẳng, không làm điều gian dối.
lương thực|Các loại thức ăn chính như gạo, ngô, khoai, sắn.
lướt|Đi qua thật nhanh và nhẹ; cũng chỉ việc xem nhanh tin tức trên mạng.
lướt ván|Môn thể thao đứng trên tấm ván trượt theo sóng biển.
lưu bút|Những dòng viết để lại làm kỉ niệm cho nhau, nhất là khi chia tay mái trường.
lưu động|Di chuyển từ nơi này sang nơi khác, không cố định một chỗ.
lưu giữ|Giữ gìn, cất lại để không bị mất hoặc bị quên.
lưu huỳnh|Nguyên tố hóa học dạng chất rắn màu vàng, khi cháy có mùi hắc, dùng làm diêm.
lưu loát|Nói hoặc viết trôi chảy, mạch lạc, không vấp váp.
lưu luyến|Quyến luyến, không nỡ rời xa người hoặc nơi chốn.
lưu lượng|Lượng nước, xe cộ hoặc dữ liệu đi qua một nơi trong một khoảng thời gian.
lưu niệm|Để lại làm kỷ niệm, giúp nhớ về một người, một nơi hay một dịp.
lưu thông|Di chuyển thông suốt, không bị tắc, như xe cộ, hàng hóa, dòng nước.
lưu trữ|Cất giữ tài liệu, dữ liệu có hệ thống để dùng về sau.
lưu ý|Chú ý, để tâm đến điều quan trọng; cũng là nhắc người khác chú ý.
má hồng|Đôi má ửng hồng; cũng chỉ phấn tô cho má thêm hồng.
mà lại|Từ nối để bổ sung thêm một ý, thường nhấn mạnh sự bất ngờ.
ma mút|Loài voi cổ đã tuyệt chủng, lông dày, ngà dài và cong.
ma sát|Lực cản sinh ra khi hai bề mặt cọ xát vào nhau.
mã số|Dãy số riêng dùng để nhận biết, phân biệt người hoặc vật.
ma trận|Bảng các số xếp theo hàng và cột trong toán học; cũng chỉ thứ chằng chịt, rối rắm.
mã vạch|Dãy vạch đen trắng in trên hàng hóa, máy quét đọc được.
mách|Báo cho người khác biết; thường là kể lỗi của ai với người lớn.
mạch điện|Hệ thống dây dẫn và linh kiện nối với nhau cho dòng điện chạy qua.
mạch lạc|Rõ ràng, có thứ tự, ý nọ nối ý kia chặt chẽ.
mách lẻo|Hay kể chuyện riêng, lỗi nhỏ của người này cho người khác biết.
mạch nước|Dòng nước chảy ngầm dưới đất, có thể phun lên thành nguồn.
mái ấm|Gia đình, ngôi nhà nơi có tình thương và sự yên ổn.
mái bằng|Kiểu nhà có mái đổ bê tông phẳng, không dốc.
mái che|Tấm che phía trên để chắn nắng, mưa cho sân, lối đi.
mái chèo|Dụng cụ bằng gỗ, cán dài, đầu dẹt, dùng để chèo thuyền.
mái hiên|Phần mái nhô ra phía trước cửa nhà để che nắng mưa.
mãi mãi|Không bao giờ dừng, kéo dài đến vô cùng.
mải mê|Say sưa với một việc đến mức quên cả chuyện khác.
mải miết|Làm liên tục, chăm chú không ngừng nghỉ.
mài mòn|Làm hao mòn dần do cọ xát lâu ngày.
mai mối|Việc giới thiệu, se duyên cho trai gái quen nhau để tiến tới hôn nhân.
mái ngói|Phần mái nhà lợp bằng những viên ngói đất nung.
mái nhà|Phần che phía trên cùng của ngôi nhà; cũng chỉ gia đình, tổ ấm.
mai sau|Khoảng thời gian về sau, trong tương lai.
mái tóc|Toàn bộ tóc trên đầu một người.
mái tôn|Phần mái được lợp bằng các tấm tôn kim loại mỏng, có sóng.
mai vàng|Cây mai cho hoa vàng rực, được trưng bày nhiều dịp Tết ở miền Nam.
màn ảnh|Tấm màn chiếu phim; cũng chỉ ngành điện ảnh nói chung.
màn cửa|Tấm vải treo ở cửa sổ, cửa ra vào để che nắng, che chắn.
màn đêm|Bóng tối bao phủ khi trời về đêm.
màn hình|Mặt kính hiển thị hình ảnh của tivi, máy tính, điện thoại.
mang cá|Bộ phận ở hai bên đầu cá, giúp cá thở dưới nước.
mãng cầu|Tên gọi ở miền Nam của quả na, vỏ có nhiều mắt, ruột trắng ngọt.
mang lại|Đem đến cho ai điều gì đó, như niềm vui, lợi ích.
mạng lưới|Hệ thống nhiều điểm nối với nhau chằng chịt như tấm lưới.
mang máng|Nhớ hoặc biết một cách lờ mờ, không rõ ràng.
mạng nhện|Lưới tơ mảnh do con nhện giăng để bắt mồi.
mang ơn|Chịu ơn người khác và luôn ghi nhớ điều đó.
mang tên|Được đặt tên gọi là, hoặc được đặt theo tên của ai đó.
mạnh|Có sức khỏe, sức lực lớn; cũng chỉ mức độ cao, tác động lớn.
mạnh bạo|Không sợ sệt, dám làm, dám nói.
mạnh dạn|Tự tin, không rụt rè khi nói hoặc làm điều gì.
mảnh dẻ|Có dáng người thon nhỏ, trông mềm mại, yếu ớt.
mảnh đất|Một khoảng đất nhất định; cũng chỉ vùng đất, quê hương gắn bó.
mảnh ghép|Từng miếng nhỏ để ghép lại với nhau thành hình hoàn chỉnh.
mảnh khảnh|Có dáng người gầy, thanh và trông mảnh dẻ.
mãnh liệt|Rất mạnh mẽ, dồn dập, thường nói về tình cảm hay ý chí.
mảnh mai|Thon thả, thanh nhỏ và có vẻ yếu mềm, thường nói về dáng người.
mạnh mẽ|Có sức mạnh lớn; cũng chỉ tính cách cứng cỏi, vững vàng.
manh mối|Dấu vết, chi tiết giúp lần ra sự thật của một việc.
mạnh tay|Làm dứt khoát, không nương nhẹ; cũng chỉ việc tiêu tiền thoải mái.
mãnh thú|Loài thú dữ, to khỏe như hổ, báo, sư tử.
mảnh vỡ|Phần nhỏ còn lại khi một vật bị vỡ ra.
mảnh vụn|Những mẩu nhỏ vỡ ra hoặc còn sót lại từ một vật.
mạo hiểm|Dám làm việc nguy hiểm, có thể gặp rủi ro.
mát dịu|Mát mẻ và êm dịu, dễ chịu.
mát lành|Mát mẻ, trong lành, tốt cho sức khỏe.
mát mắt|Nhìn thấy dễ chịu, thích mắt, cảm giác dịu mát.
mát mẻ|Có nhiệt độ dễ chịu, không nóng, gió nhẹ.
mát rượi|Mát lạnh, cảm giác dễ chịu lan khắp người.
mau chóng|Nhanh, xảy ra trong một thời gian ngắn.
mau lẹ|Nhanh nhẹn, làm việc nhanh chóng, không chậm trễ.
mau mau|Lời giục làm nhanh lên, đừng chậm trễ.
màu nước|Loại màu vẽ hòa với nước, tạo nét vẽ trong, nhẹ nhàng.
máy ảnh|Thiết bị dùng để chụp và lưu giữ hình ảnh.
máy bay|Phương tiện bay trên không, chở người và hàng hóa.
máy bơm|Thiết bị hút và đẩy nước hoặc chất lỏng từ nơi này sang nơi khác.
máy cày|Phương tiện có động cơ dùng để cày, xới đất ruộng.
máy cắt|Thiết bị dùng để cắt vật liệu như cỏ, gỗ, kim loại.
máy chủ|Hệ thống máy tính mạnh, cung cấp dữ liệu, dịch vụ cho máy khác qua mạng.
máy dệt|Thiết bị dùng để đan các sợi thành tấm vải.
máy dò|Thiết bị giúp phát hiện vật bị che khuất, chôn giấu như kim loại.
máy đào|Phương tiện có cánh tay dài và gầu, dùng để đào đất ở công trình.
máy gặt|Thiết bị cơ giới dùng để cắt và thu hoạch lúa trên ruộng.
máy giặt|Thiết bị điện giặt quần áo tự động.
máy hàn|Thiết bị dùng nhiệt hoặc điện để nối kim loại lại với nhau.
máy in|Thiết bị in chữ, hình ảnh từ máy tính ra giấy.
máy kéo|Phương tiện có động cơ khỏe, dùng để kéo xe chở hàng, nông cụ.
máy khâu|Dụng cụ dùng kim chỉ để khâu, may vải nhanh hơn tay.
máy khoan|Dụng cụ có mũi xoay, dùng tạo lỗ trên tường, gỗ, kim loại.
máy lạnh|Thiết bị làm mát không khí trong phòng, còn gọi là điều hòa.
may mà|Nhờ gặp điều may nên tránh được chuyện không hay.
máy may|Dụng cụ dùng kim chỉ để may quần áo, còn gọi là máy khâu.
may mặc|Công việc, ngành nghề sản xuất quần áo.
may mắn|Gặp được điều tốt lành, thuận lợi một cách tình cờ.
máy móc|Các loại máy nói chung; cũng chỉ cách làm cứng nhắc, rập khuôn.
máy quét|Thiết bị chuyển giấy tờ, hình ảnh thành dữ liệu trong máy tính.
may ra|Có lẽ, nếu thuận lợi thì có thể được như mong muốn.
may rủi|Điều tốt hay xấu xảy ra tình cờ, không đoán trước được.
máy tính|Thiết bị điện tử để tính toán, xử lý thông tin, chạy các chương trình.
máy ủi|Phương tiện có lưỡi gạt lớn phía trước, dùng để san phẳng mặt đất.
may vá|Công việc khâu, may quần áo và vá chỗ rách.
máy xay|Thiết bị điện để xay nhỏ thực phẩm, làm sinh tố, nghiền hạt.
máy xúc|Phương tiện có gầu lớn dùng để xúc đất, đá, cát.
mắc áo|Đồ dùng có móc để treo quần áo cho phẳng.
mắc bẫy|Bị dính vào bẫy; cũng chỉ bị lừa vào tình thế bất lợi.
mặc cả|Trả giá qua lại khi mua bán để được giá vừa ý.
mắc cạn|Tàu thuyền bị kẹt ở chỗ nước nông, không đi tiếp được.
mắc cỡ|Cảm thấy ngượng ngùng, e thẹn; cũng là tên loài cây lá khép lại khi bị chạm.
mặc dù|Từ nối dùng để nêu một điều trái ngược với sự việc ở vế sau.
mắc kẹt|Bị giữ lại hoặc vướng vào chỗ nào đó, không thoát ra được.
mặc kệ|Để mặc, không quan tâm hay can thiệp vào.
mắc lỗi|Phạm sai sót, làm điều không đúng khi làm việc gì.
mắc lừa|Bị người khác đánh lừa, tin vào điều không đúng.
mắc phải|Gặp phải hoặc vướng vào điều không hay như lỗi, sai lầm.
mắm muối|Mắm, muối và gia vị nói chung; cũng chỉ việc thêm thắt cho câu chuyện.
mắm tôm|Loại mắm làm từ tôm tép nhỏ giã nhuyễn ủ muối, mùi nồng, hay chấm bún đậu.
mặn mà|Đậm đà, có duyên; cũng chỉ tình cảm thắm thiết, nồng hậu.
mằn mặn|Có vị hơi mặn, mặn nhẹ.
măng|Mầm non của cây tre, nứa, mọc lên từ gốc, dùng làm món ăn.
măng cụt|Loại quả vỏ dày màu tím sẫm, ruột trắng chia múi, vị ngọt chua.
măng khô|Măng tre luộc rồi phơi khô, khi dùng ngâm mềm để nấu canh, hầm.
mắng mỏ|La rầy, trách móc ai đó bằng lời lẽ nặng nề.
măng tây|Loại rau thân non mọc thẳng, màu xanh, ăn giòn ngọt.
mặt bằng|Khoảng đất, diện tích dùng để xây dựng hay kinh doanh; cũng chỉ mức chung.
mắt cá|Chỗ xương nhô lên ở hai bên cổ chân.
mặt đất|Bề mặt của đất, nơi con người và muôn loài sinh sống.
mặt đường|Phần bề mặt của con đường, nơi xe cộ và người đi lại.
mặt hàng|Từng loại hàng hóa được bày bán.
mặt khác|Cụm từ nối để nêu thêm một khía cạnh khác của vấn đề.
mắt kính|Tròng kính lắp vào gọng; cũng chỉ chiếc kính đeo mắt.
mặt mày|Khuôn mặt và vẻ mặt của một người nói chung.
mặt mũi|Khuôn mặt nói chung; cũng chỉ thể diện, danh dự của một người.
mặt nạ|Vật che mặt để hóa trang, bảo vệ hoặc dưỡng da.
mặt nước|Lớp bề mặt phía trên của nước ở ao, hồ, sông, biển.
mặt phẳng|Bề mặt bằng phẳng, không lồi lõm; khái niệm cơ bản trong hình học.
mặt phố|Phần nhà hay đất nằm sát đường phố, thuận tiện buôn bán.
mặt trái|Mặt phía sau, không phải mặt chính; cũng chỉ mặt xấu của sự việc.
mặt trăng|Thiên thể quay quanh Trái Đất, chiếu sáng bầu trời ban đêm.
mặt trời|Ngôi sao chiếu sáng và sưởi ấm Trái Đất vào ban ngày.
mắt xích|Vòng nhỏ nối với nhau tạo thành dây xích; cũng chỉ một khâu trong chuỗi.
mầm non|Chồi cây mới nhú; cũng chỉ trẻ nhỏ hoặc bậc học trước tiểu học.
mâm xôi|Loại quả mọng nhỏ màu đỏ, vị chua ngọt; cũng chỉ mâm đựng xôi.
mập mạp|Béo tròn, trông khỏe mạnh, hay dùng khi nói về trẻ nhỏ.
mấp mô|Lồi lõm, không bằng phẳng, thường nói về mặt đường.
mất công|Tốn thời gian, sức lực vào việc gì, nhiều khi không có kết quả.
mật độ|Mức dày hay thưa của người hoặc vật trên một diện tích.
mất giá|Bị giảm giá trị so với trước, thường nói về tiền hoặc hàng hóa.
mật hoa|Chất lỏng ngọt trong hoa, ong bướm hút để làm thức ăn.
mất hút|Biến mất hẳn, không còn thấy dấu vết đâu nữa.
mật khẩu|Chuỗi ký tự bí mật dùng để đăng nhập hoặc mở khóa.
mất lòng|Làm người khác không vui, phật ý vì lời nói hay việc làm.
mật mã|Hệ thống ký hiệu hoặc con số bí mật dùng để giữ kín thông tin.
mất mùa|Thu hoạch kém vì cây trồng bị hỏng hoặc cho năng suất thấp.
mật ong|Chất lỏng sánh, ngọt, màu vàng do ong làm ra từ mật hoa.
mất sức|Bị hao tổn sức lực, cảm thấy mệt và yếu đi.
mất vui|Làm cho cuộc vui hoặc không khí bớt vui, mất hứng.
mấu chốt|Điểm quan trọng nhất, có tính quyết định trong một vấn đề.
mẫu đơn|Loài hoa to, nhiều cánh, sắc rực rỡ; cũng chỉ tờ đơn in sẵn để điền.
mẫu giáo|Bậc học dành cho trẻ khoảng ba đến sáu tuổi, trước lớp một.
mẫu mã|Hình dáng, kiểu dáng bên ngoài của sản phẩm.
mẫu mực|Chuẩn mực, đáng để người khác học tập và noi theo.
mẫu số|Số nằm dưới gạch ngang của một phân số.
mâu thuẫn|Trái ngược nhau, không thống nhất; cũng chỉ sự xích mích giữa người với người.
mẫu vật|Vật thật được lấy làm mẫu để nghiên cứu, trưng bày.
mây mù|Sương và mây dày đặc khiến trời âm u, khó nhìn xa.
mây trắng|Những đám mây màu trắng trôi trên bầu trời.
mây tre|Đồ thủ công đan từ sợi mây và cây tre như rổ, giỏ, bàn ghế.
mây xanh|Mây trên bầu trời xanh cao; cũng ví nơi rất cao, như được khen lên mây xanh.
mẹ cha|Cha và mẹ, những người sinh ra và nuôi dưỡng mình.
mẹ chồng|Người mẹ của chồng, theo cách gọi của người vợ.
mẹ con|Người mẹ cùng với đứa con của mình.
mẹ kế|Vợ sau của cha, không phải mẹ ruột của mình.
mẹ nuôi|Người phụ nữ nhận nuôi và chăm sóc mình như con ruột.
mẹ vợ|Người mẹ của vợ, theo cách gọi của người chồng.
mèo chuột|Con mèo và con chuột; cũng chỉ trò đuổi bắt, vờn nhau.
mèo hoang|Con mèo không có chủ, sống tự do, lang thang ngoài đường.
meo meo|Tiếng kêu của con mèo.
méo mó|Bị biến dạng, không còn tròn, thẳng như ban đầu.
mèo rừng|Loài mèo hoang dã sống trong rừng, to và dữ hơn mèo nhà.
mét khối|Đơn vị đo thể tích, bằng khối lập phương cạnh một mét.
mét vuông|Đơn vị đo diện tích, bằng hình vuông cạnh một mét.
mê cung|Nơi có nhiều lối đi chằng chịt, rất dễ lạc.
mề gà|Dạ dày của con gà, dai và giòn, dùng để nấu ăn.
mê hoặc|Làm cho người khác say mê, bị cuốn hút đến mất tỉnh táo.
mê mẩn|Say mê đến mức quên hết mọi thứ xung quanh.
mê mệt|Say đắm, thích đến mức quên cả mọi thứ khác.
mê tít|Rất thích thú, say mê không rời.
mềm dẻo|Mềm và dễ uốn mà không gãy; cũng chỉ cách xử sự linh hoạt.
mềm lòng|Dễ xúc động, dễ bị lay chuyển mà thay đổi ý định.
mềm mại|Mềm và mịn, tạo cảm giác dễ chịu khi chạm vào.
mềm mỏng|Nhẹ nhàng, khéo léo trong lời nói và cách cư xử.
mềm nhũn|Mềm đến mức nhão ra, không còn giữ được hình dạng.
mềm yếu|Yếu đuối, thiếu cứng rắn, dễ bị cảm xúc chi phối.
mệnh giá|Giá trị ghi trên tờ tiền, đồng xu hoặc giấy tờ có giá.
mệnh lệnh|Lời yêu cầu do cấp trên đưa ra, bắt buộc phải làm theo.
mênh mông|Rộng lớn bao la, không thấy bờ bến.
mệt lả|Mệt đến mức người rã rời, không còn sức.
mệt lử|Mệt rũ người, như không còn chút sức lực nào.
mệt mỏi|Cảm thấy kiệt sức, uể oải, không muốn làm gì.
mệt nhoài|Mệt rã rời sau khi làm việc vất vả.
mệt nhọc|Mệt vì phải làm việc vất vả, tốn nhiều sức.
mỉa mai|Nói ngược ý để chê bai, châm chọc một cách kín đáo.
micro|Thiết bị thu âm thanh để khuếch đại hoặc ghi âm, hay dùng khi hát, phát biểu.
miến|Loại sợi khô làm từ bột dong hoặc đậu, nấu chín thì trong và dai.
miễn cưỡng|Làm một cách gượng ép, không thật lòng muốn.
miễn là|Chỉ cần đạt được điều kiện ấy là được.
miễn phí|Không mất tiền, không phải trả phí.
miễn sao|Chỉ cần đạt được mục đích, làm cách nào cũng được.
miệng|Bộ phận trên mặt dùng để ăn, nói; cũng chỉ phần mở ra của đồ vật.
miếng ăn|Phần thức ăn nhỏ; cũng chỉ cái ăn để sống hằng ngày.
miệt mài|Chăm chú làm liên tục, say mê không nghỉ.
miêu tả|Dùng lời nói, chữ viết vẽ lại hình ảnh, đặc điểm của sự vật.
mỉm cười|Cười nhẹ nhàng, môi hơi cong lên, không thành tiếng.
mịn màng|Mịn và mượt, sờ vào thấy êm, thường nói về làn da.
mình|Từ tự xưng thân mật, như tôi; cũng chỉ thân thể con người.
minh bạch|Rõ ràng, công khai, không có gì mờ ám.
minh mẫn|Đầu óc sáng suốt, nhanh nhạy, nhớ tốt.
mini|Có kích thước nhỏ gọn, thu nhỏ hơn loại thường.
mít ướt|Hay khóc nhè, dễ rơi nước mắt dù chuyện nhỏ.
mò mẫm|Lần dò tìm trong bóng tối; cũng chỉ việc tự tìm tòi không ai chỉ.
mỏ neo|Vật nặng bằng sắt thả xuống nước để giữ tàu thuyền đứng yên.
mỏ vịt|Phần miệng dẹt và cứng của con vịt; cũng chỉ vật có hình như thế.
móc câu|Lưỡi sắt nhỏ uốn cong có ngạnh, dùng để mắc mồi câu cá.
mọc răng|Răng bắt đầu nhú lên khỏi lợi, thường ở trẻ nhỏ.
mọi khi|Như các lần trước, như thường lệ.
mỏi mắt|Mắt mệt, nhức vì nhìn lâu; cũng chỉ việc chờ đợi rất lâu.
mọi ngày|Những ngày bình thường khác, như vẫn thường thấy.
món ăn|Thức ăn đã được nấu nướng, chế biến theo một cách riêng.
món canh|Thức ăn nấu có nhiều nước với rau, thịt hoặc cá, ăn kèm cơm.
món hàng|Một thứ hàng hóa cụ thể được bày bán hoặc đã mua.
móng|Lớp sừng cứng ở đầu ngón tay, chân; cũng là phần nền dưới của nhà.
mong chờ|Ngóng đợi, mong cho điều gì sớm xảy ra.
mong đợi|Trông chờ điều gì đó sẽ đến hoặc xảy ra.
mong muốn|Điều mình ước ao và hy vọng có được.
mong ngóng|Trông chờ, đợi mãi một người hay một tin tức.
móng ngựa|Phần sừng cứng ở chân ngựa; cũng chỉ miếng sắt hình chữ U đóng vào đó.
mong nhớ|Nhớ nhung và mong được gặp lại.
mọng nước|Căng tròn, chứa nhiều nước, thường nói về trái cây.
mong sao|Ước gì, rất mong cho điều tốt đẹp sẽ xảy ra.
mỏng tanh|Rất mỏng, mỏng như có thể rách bất cứ lúc nào.
móng tay|Lớp sừng mỏng, cứng ở đầu các ngón tay.
mong ước|Điều ấp ủ, ao ước muốn có được trong tương lai.
móng vuốt|Phần sừng nhọn, cong và sắc ở chân thú hoặc chim.
mọt sách|Người rất ham đọc sách, suốt ngày vùi đầu vào sách vở.
mô hình|Vật thu nhỏ làm giống vật thật; cũng chỉ một cách tổ chức mẫu.
mồ hôi|Nước tiết ra qua da khi trời nóng hoặc khi vận động.
mô phỏng|Bắt chước, làm lại giống như thật để thử nghiệm hoặc học tập.
mô tả|Nói hoặc viết ra để người khác hình dung rõ người, vật, sự việc.
mốc meo|Bị mốc nhiều, lên lớp mốc xanh trắng vì để lâu.
môi giới|Người làm trung gian giúp hai bên gặp nhau, mua bán, thuê mướn.
mỗi một|Từng cái, từng người riêng lẻ trong một nhóm.
môi trường|Toàn bộ thiên nhiên và điều kiện xung quanh nơi con người sinh sống.
môn học|Một lĩnh vực kiến thức được dạy riêng ở trường, như toán, văn.
mộng mơ|Hay mơ tưởng đến những điều đẹp đẽ, lãng mạn.
một cách|Cụm từ đặt trước tính từ để chỉ cách thức làm việc gì.
một chiều|Chỉ theo một hướng, như đường một chiều; cũng chỉ cách nhìn phiến diện.
một chút|Lượng rất ít hoặc khoảng thời gian rất ngắn.
một hơi|Liền một lèo, không dừng lại giữa chừng.
một ít|Lượng nhỏ, không nhiều lắm.
một khi|Từ nối nêu điều kiện, khi việc này xảy ra thì việc sau sẽ theo.
một lát|Khoảng thời gian ngắn, chừng ít phút.
một lần|Chỉ xảy ra một bận; cũng chỉ một dịp nào đó trong quá khứ.
một lúc|Khoảng thời gian ngắn; cũng chỉ cùng một thời điểm.
một mạch|Liền từ đầu đến cuối, không ngừng nghỉ.
một mặt|Cụm từ nêu một khía cạnh của vấn đề, thường đi với mặt khác.
một mình|Chỉ có riêng bản thân, không có ai bên cạnh.
một số|Vài cái, vài người trong nhiều, số lượng không xác định rõ.
một tay|Tự mình làm hết mọi việc, không nhờ ai giúp.
một vài|Số lượng ít, khoảng hai ba cái hoặc hai ba người.
mờ ám|Không minh bạch, có vẻ khuất tất, đáng ngờ.
mờ ảo|Mờ mờ, không rõ ràng, tạo vẻ huyền ảo.
mở cửa|Mở cánh cửa ra; cũng chỉ cửa hàng, cơ quan bắt đầu hoạt động.
mở đầu|Phần bắt đầu của một việc, bài viết hay câu chuyện.
mở đường|Làm ra con đường mới; cũng chỉ tạo điều kiện cho việc bắt đầu.
mơ hồ|Không rõ ràng, khó hiểu, không chắc chắn.
mở màn|Bắt đầu một buổi biểu diễn hay một sự kiện.
mơ màng|Nửa tỉnh nửa mê; cũng chỉ trạng thái thả hồn theo suy nghĩ.
mở máy|Bật cho máy móc, thiết bị bắt đầu chạy.
mở mắt|Nâng mí mắt lên để nhìn, thường là lúc thức dậy.
mở miệng|Hé miệng ra; thường chỉ việc bắt đầu nói điều gì.
mờ mịt|Tối mờ, không nhìn rõ; cũng chỉ tương lai không rõ ràng.
mơ mộng|Hay nghĩ đến những điều đẹp đẽ, xa vời thực tế.
mờ nhạt|Không rõ nét, nhạt nhòa, ít gây chú ý.
mở ra|Làm cho cái đang đóng thành mở; cũng chỉ bắt đầu điều mới.
mở rộng|Làm cho rộng hơn, lớn hơn về phạm vi hoặc quy mô.
mờ sáng|Lúc trời mới hửng sáng, cảnh vật còn mờ mờ.
mở tiệc|Tổ chức một bữa tiệc để ăn mừng hay chiêu đãi.
mở toang|Mở rộng hết cỡ, không khép lại chút nào.
mở tung|Mở mạnh ra hết cỡ, thật rộng.
mơ ước|Điều mong muốn tha thiết, hy vọng đạt được.
mời chào|Mời mọc, chào khách để họ mua hàng hay dùng dịch vụ.
mới cứng|Còn mới tinh, như vừa mới mua về.
mới đầu|Lúc ban đầu, khi sự việc vừa bắt đầu.
mới đây|Cách đây không lâu, gần với hiện tại.
mới lạ|Mới xuất hiện và khác thường, gây tò mò, thích thú.
mới mẻ|Lạ và tươi mới, chưa từng có hoặc chưa quen thuộc trước đó.
mời mọc|Mời người khác nói chung, thường nhiều lần và ân cần.
mới nguyên|Còn mới, chưa dùng đến hoặc chưa bị thay đổi gì.
mới tinh|Rất mới, chưa hề được dùng đến.
mới toanh|Mới hoàn toàn, trông sáng bóng như vừa mua về.
mù mịt|Tối tăm, bụi hay sương dày đặc, không nhìn rõ; cũng chỉ tương lai chưa rõ.
mù mờ|Không rõ ràng, hiểu biết lơ mơ, không chắc chắn.
mũ nồi|Mũ tròn, mềm, không vành, thường đội lệch trên đầu.
mua bán|Việc trao đổi hàng hóa bằng tiền giữa người mua và người bán.
mùa đông|Thời gian lạnh nhất trong năm, sau mùa thu, trước mùa xuân.
mùa gặt|Thời gian thu hoạch lúa chín trên đồng.
mùa hạ|Khoảng thời gian nóng nhất trong năm, giữa mùa xuân và mùa thu.
mua hàng|Bỏ tiền ra để có được hàng hóa.
mùa hè|Khoảng thời gian nóng nhất trong năm, có nắng gắt, học sinh được nghỉ.
mùa khô|Thời gian trong năm ít mưa, trời nắng ráo, hanh khô.
mùa lạnh|Thời kỳ trong năm có thời tiết lạnh, thường là mùa đông.
mùa màng|Cây trồng, lúa má và việc thu hoạch theo từng vụ nói chung.
múa rối|Nghệ thuật dùng tay, que, dây điều khiển con rối để diễn tích truyện.
mua sắm|Bỏ tiền chọn lựa, sắm sửa các thứ đồ dùng cần thiết.
mùa thi|Khoảng thời gian diễn ra các kỳ thi, nhất là thi tốt nghiệp, đại học.
mùa thu|Thời gian sau mùa hè, trời mát dịu, lá cây chuyển vàng và rụng.
mùa vụ|Thời gian gieo trồng và thu hoạch của một loại cây trong năm.
mua vui|Tìm cách tạo niềm vui, giải trí cho mình hoặc người khác.
mùa xuân|Mùa đầu tiên trong năm, trời ấm áp, cây cối đâm chồi.
mục đích|Điều mong muốn đạt được khi làm một việc gì đó.
mục lục|Danh sách các phần, chương kèm số trang trong cuốn sách.
mục nát|Hư hỏng, mủn ra vì để lâu ngày, thường nói về gỗ.
mục tiêu|Điều mình hướng tới và muốn đạt được.
múi giờ|Vùng trên trái đất dùng chung một giờ chuẩn.
mùi khét|Mùi của vật bị cháy, nồng và khó chịu.
mũi khoan|Đầu nhọn có rãnh xoắn lắp vào máy khoan để tạo lỗ.
mủi lòng|Cảm thấy xúc động, thương cảm đến muốn khóc.
mũi nhọn|Đầu nhọn của vật; cũng chỉ lĩnh vực, lực lượng chủ chốt đi đầu.
mũi tên|Que nhọn bắn đi bằng cung; cũng là ký hiệu chỉ hướng.
mùi thơm|Hương dễ chịu tỏa ra từ hoa, món ăn hay nước hoa.
mũm mĩm|Béo tròn, trông đáng yêu, nhất là trẻ nhỏ.
mùn cưa|Bột gỗ vụn rơi ra khi cưa gỗ.
muối|Chất tinh thể vị mặn, dùng nêm thức ăn; cũng là ướp mặn để giữ lâu.
muối ăn|Loại hạt mặn màu trắng dùng để nêm nếm món ăn hằng ngày.
muối biển|Hạt mặn thu được khi phơi cho nước biển bay hơi.
muối tiêu|Muối trộn hạt tiêu xay để chấm; cũng chỉ mái tóc lốm đốm bạc.
muôn đời|Mãi mãi, suốt mọi thời đại về sau.
muông thú|Các loài thú và chim chóc sống trong tự nhiên nói chung.
mưa đá|Hiện tượng những hạt băng nhỏ rơi từ trên trời xuống khi giông.
mưa gió|Thời tiết có mưa và gió; cũng chỉ hoàn cảnh vất vả.
mưa nắng|Mưa và nắng; cũng chỉ sự vất vả, dãi dầu.
mưa phùn|Những hạt nước rất nhỏ như bụi bay, thường có vào cuối đông, đầu xuân.
mưa rào|Cơn mưa to đến bất chợt rồi tạnh nhanh, hay có vào mùa hè.
mưa tuyết|Hiện tượng tuyết rơi từ trên trời xuống ở xứ lạnh.
mức độ|Độ cao thấp, nhiều ít hay nặng nhẹ của một sự việc.
mức lương|Số tiền lương được trả theo tháng hoặc theo công việc.
mực nang|Loài mực thân dày, có mai cứng bên trong, thịt giòn ngọt.
mực ống|Loại mực thân dài hình ống, thịt dày, dùng làm món ăn.
mức sống|Mức độ đầy đủ về vật chất và tinh thần trong cuộc sống.
mừng|Vui vì có điều tốt lành xảy ra; cũng chỉ việc chúc mừng.
mừng công|Tổ chức ăn mừng khi hoàn thành việc lớn hoặc giành thắng lợi.
mừng rỡ|Vui mừng lộ rõ ra bên ngoài.
mừng tuổi|Chúc Tết và tặng tiền lì xì vào dịp năm mới.
mười lăm|Số đứng sau mười bốn, trước mười sáu.
mượn|Lấy đồ của người khác dùng tạm rồi sẽ trả lại.
mương|Đường dẫn nước nhỏ đào để tưới tiêu cho đồng ruộng.
mướp|Cây leo, quả dài màu xanh, ruột mềm, thường nấu canh.
mướp đắng|Quả có vỏ sần sùi, vị đắng, miền Nam gọi là khổ qua.
mượt|Mềm, trơn và bóng, sờ vào thấy êm tay.
mượt mà|Mềm mại, trơn láng; cũng chỉ giọng hát, câu văn uyển chuyển.
mứt kẹo|Các loại mứt và kẹo, đồ ngọt hay bày mời khách dịp Tết.
mưu mẹo|Cách khôn khéo, mẹo hay để đạt được mục đích.
mưu mô|Có nhiều mánh khóe, tính toán để lừa người khác.
na ná|Hơi giống nhau, gần giống nhưng không hoàn toàn.
nam châm|Vật có khả năng hút sắt và một số kim loại khác.
nam giới|Đàn ông, con trai nói chung, phân biệt với nữ giới.
nam nữ|Cả nam và nữ, đàn ông và phụ nữ nói chung.
nam sinh|Học sinh hoặc sinh viên là con trai.
nam tính|Vẻ mạnh mẽ, cứng cỏi thường thấy ở đàn ông.
nản chí|Mất ý chí, không muốn tiếp tục cố gắng.
nan hoa|Những thanh nhỏ nối từ trục ra vành bánh xe đạp, xe máy.
nản lòng|Mất tinh thần, chán nản khi gặp khó khăn.
nàng dâu|Người phụ nữ về làm vợ, trong quan hệ với gia đình nhà chồng.
nàng thơ|Người phụ nữ khơi nguồn cảm hứng sáng tác cho nghệ sĩ.
nàng tiên|Cô gái xinh đẹp có phép màu trong truyện cổ tích.
nanh|Chiếc răng nhọn và dài nằm hai bên hàm của thú.
não bộ|Bộ phận trong đầu điều khiển suy nghĩ và hoạt động của cơ thể.
nào đó|Chỉ một người, vật hoặc lúc chưa được nói rõ.
náo động|Xôn xao, ồn ào, làm mất sự yên tĩnh.
nào là|Từ dùng để kể ra nhiều thứ liên tiếp, nhấn mạnh là có rất nhiều.
náo loạn|Ồn ào, lộn xộn, mất hết trật tự.
nào ngờ|Không ngờ tới, không hề nghĩ sự việc lại xảy ra như vậy.
náo nhiệt|Đông vui, ồn ào, sôi động.
nạo vét|Lấy bùn đất ở đáy sông, kênh, cống để dòng chảy được thông sâu.
nạp điện|Đưa điện vào pin hoặc ắc quy để dùng dần.
nãy giờ|Khoảng thời gian từ lúc nãy cho tới bây giờ.
nảy lửa|Rất gay gắt, căng thẳng, như cuộc tranh luận hay trận đấu quyết liệt.
nảy mầm|Hạt giống bắt đầu nhú ra mầm non khi gặp đủ nước và hơi ấm.
này nọ|Thứ này thứ khác, đủ chuyện linh tinh không kể hết.
nảy sinh|Bắt đầu xuất hiện, thường nói về ý nghĩ, tình cảm hay vấn đề mới.
nắm bắt|Hiểu nhanh và nắm được; cũng là tận dụng kịp thời cơ hội.
nắm chắc|Hiểu thật rõ, biết vững vàng; cũng là cầm giữ thật chặt.
nằm dài|Duỗi người ra nghỉ một cách thoải mái, không làm gì.
nắm giữ|Cầm giữ, có trong tay hoặc có quyền quản lý.
năm học|Khoảng thời gian học tập trong một năm, thường bắt đầu vào tháng chín.
nằm im|Ở yên một chỗ, không nhúc nhích.
năm kia|Năm trước năm ngoái, tức là cách đây hai năm.
nắm lấy|Cầm chặt lấy; cũng là tận dụng ngay một cơ hội.
nằm mơ|Thấy những hình ảnh, câu chuyện trong lúc ngủ; cũng chỉ mong điều viển vông.
năm mới|Thời điểm một năm vừa bắt đầu, dịp mọi người chúc mừng nhau.
năm mươi|Số đếm bằng năm lần mười.
năm nay|Chỉ năm hiện tại, năm đang diễn ra.
nằm ngang|Ở vị trí song song với mặt đất, không đứng dọc.
nằm nghiêng|Nằm với thân người quay sang một bên trái hoặc phải.
năm ngoái|Chỉ năm liền trước năm hiện tại.
nằm ngủ|Ngả lưng xuống để ngủ, nghỉ ngơi.
nằm ngửa|Ngả lưng xuống, mặt và bụng hướng lên trên.
năm nhuận|Năm có thêm một ngày hoặc một tháng so với năm bình thường.
năm qua|Chỉ năm vừa trải qua hoặc khoảng một năm gần đây.
nằm sấp|Úp bụng và mặt xuống dưới, lưng hướng lên trên.
nắm tay|Cầm tay người khác; cũng chỉ bàn tay co các ngón lại.
năm tháng|Khoảng thời gian dài trôi qua trong đời người.
năm tới|Chỉ năm tiếp theo, ngay sau năm hiện tại.
nằm ườn|Nằm dài ra một cách lười biếng, chẳng muốn làm gì.
nắm vững|Hiểu thấu đáo, thông thạo kiến thức hoặc kỹ năng.
nằm xuống|Ngả người, đặt lưng xuống giường hoặc mặt đất.
năm xưa|Thời gian đã qua từ lâu, những năm trước đây.
nắng|Ánh sáng và hơi nóng của mặt trời chiếu xuống.
nặng cân|Có trọng lượng lớn, cân lên thấy nặng.
năng động|Nhanh nhẹn, linh hoạt, hoạt bát và sáng tạo.
nắng gắt|Ánh nắng rất mạnh và nóng, chiếu chói chang.
năng khiếu|Khả năng bẩm sinh giỏi về một lĩnh vực nào đó.
nặng lời|Nói những lời gay gắt, khó nghe.
năng lực|Khả năng làm việc và hoàn thành công việc.
năng lượng|Sức mạnh như điện, nhiệt giúp máy móc chạy; cũng chỉ sức sống dồi dào.
nắng mưa|Lúc nắng lúc mưa; cũng chỉ những vất vả, đổi thay của cuộc đời.
nằng nặc|Một mực đòi cho bằng được, nhất quyết không chịu thôi.
nặng nề|Rất nặng, gây mệt nhọc; cũng chỉ không khí ngột ngạt, căng thẳng.
nặng nhẹ|Mức độ nặng hay nhẹ; cũng chỉ lời trách móc, nói nặng lời với ai.
nặng nhọc|Vất vả, tốn nhiều sức lực.
năng nổ|Hăng hái, nhiệt tình, tích cực trong công việc.
nắng ráo|Trời có nắng, khô ráo, không mưa.
nặng trĩu|Rất nặng, làm cành hay vật oằn xuống; cũng chỉ lòng nhiều lo âu.
nấc cụt|Hiện tượng bật ra tiếng nấc từng hồi ngoài ý muốn.
nấm hương|Loại nấm mũ nâu, có mùi thơm, thường phơi khô để nấu ăn.
nấm mốc|Loại nấm rất nhỏ mọc trên thức ăn hay đồ vật để lâu, ẩm ướt.
nấm rơm|Loại nấm nhỏ màu xám, mọc trên rơm rạ ẩm, ăn ngọt và thơm.
nấn ná|Cố nán lại, chần chừ chưa muốn đi hoặc chưa làm.
nâng cao|Làm cho cao hơn hoặc tốt hơn trước.
nâng cấp|Cải tiến để tốt hơn hoặc hiện đại hơn.
nâng đỡ|Đỡ cho khỏi ngã; cũng là giúp đỡ người khác tiến bộ.
nâng niu|Giữ gìn, chăm chút một cách nhẹ nhàng, trân trọng.
nấu ăn|Làm các món ăn cho bữa cơm hằng ngày.
nấu bếp|Làm công việc nấu nướng; cũng chỉ người nấu ăn chuyên nghiệp.
nấu cơm|Đun gạo với nước cho chín thành cơm.
nâu đen|Màu nâu sẫm, gần như màu đen.
nâu nâu|Có màu hơi nâu, nhạt và không đậm lắm.
nấu nướng|Công việc chế biến, làm chín các món ăn nói chung.
né tránh|Cố tránh đi, không muốn đối mặt hay gặp gỡ.
nem chua|Món thịt lợn sống trộn bì và thính, gói lá rồi ủ cho lên men chua.
nét chữ|Hình dáng chữ viết tay riêng của mỗi người.
nét mặt|Vẻ mặt thể hiện cảm xúc, tâm trạng.
nét vẽ|Đường do bút tạo nên trên tranh; cũng chỉ cách vẽ riêng của một người.
nể mặt|Vì tôn trọng một người mà chiều theo hoặc bỏ qua chuyện gì.
nể nang|Vì nể người khác mà ngại nói thẳng hay ngại từ chối.
nếm trải|Tự mình trải qua để biết vui buồn, khó khăn.
nền móng|Phần chịu lực dưới cùng của công trình; cũng chỉ cơ sở ban đầu.
nền tảng|Cơ sở vững chắc làm chỗ dựa cho sự phát triển.
nên thơ|Đẹp và lãng mạn, gợi cảm xúc như một bài thơ.
nếp cẩm|Loại gạo nếp hạt màu tím than, thơm dẻo, dùng nấu xôi hay chè.
nếp nhăn|Đường gấp trên da hoặc vải khi bị nhàu, co lại.
nếp sống|Cách sống, thói quen sinh hoạt đã thành nền nếp.
nếu cần|Trong trường hợp cần thiết.
nếu không|Trong trường hợp ngược lại, khi điều đó không xảy ra.
nếu mà|Cách nói thân mật để đặt giả thiết, giống như giả sử.
nếu như|Dùng để nêu một giả thiết hoặc một điều kiện.
nếu vậy|Trong trường hợp đúng là như thế.
ngã ba|Nơi ba con đường gặp nhau; nghĩa bóng là lúc phải chọn một hướng đi.
ngả lưng|Nằm xuống nghỉ một lát cho đỡ mệt.
ngả nghiêng|Nghiêng bên này ngả bên kia, không đứng thẳng được.
ngã tư|Chỗ hai con đường cắt nhau, tạo thành bốn ngả.
ngà voi|Chiếc răng dài, cong, màu trắng chìa ra hai bên miệng voi.
ngạc nhiên|Lấy làm lạ vì điều xảy ra không như mình nghĩ.
ngại|Không muốn làm vì thấy phiền hoặc e dè.
ngại ngần|Còn băn khoăn, e dè, chưa muốn làm hay nói điều gì.
ngái ngủ|Còn lơ mơ, chưa tỉnh hẳn vì vừa mới ngủ dậy.
ngại ngùng|Rụt rè, e dè, không mạnh dạn.
ngai vàng|Chiếc ghế dành riêng cho vua ngồi; cũng chỉ ngôi vua.
ngàn năm|Khoảng thời gian một nghìn năm; thường dùng để chỉ sự lâu dài mãi mãi.
ngang|Theo chiều nằm từ bên này sang bên kia, trái với dọc.
ngang bằng|Bằng nhau, không ai hơn ai; cũng chỉ phẳng, không nghiêng.
ngang bướng|Cứng đầu, không chịu nghe lời ai.
ngang dọc|Theo cả chiều ngang lẫn chiều dọc; cũng chỉ sự tung hoành khắp nơi.
ngang hàng|Cùng một mức, một vị trí như nhau.
ngang ngửa|Tương đương nhau, khó phân biệt hơn kém.
ngang nhau|Bằng nhau về mức độ, số lượng hay sức lực.
ngành|Lĩnh vực hoạt động chuyên môn, như ngành y, ngành giáo dục.
ngành nghề|Các lĩnh vực công việc và nghề nghiệp nói chung.
ngạo mạn|Kiêu căng, coi thường người khác.
ngào ngạt|Mùi thơm lan tỏa nồng nàn khắp nơi.
ngáp|Há to miệng hít một hơi dài khi buồn ngủ hay mệt.
ngày|Khoảng thời gian hai mươi bốn giờ; cũng chỉ lúc trời sáng.
ngay cả|Từ dùng để nhấn mạnh, có nghĩa là kể cả điều ít ai ngờ.
ngày càng|Mỗi ngày một hơn, tăng dần theo thời gian.
ngày đêm|Cả ban ngày lẫn ban đêm, liên tục không ngừng.
ngày giờ|Thời gian cụ thể tính theo ngày và giờ.
ngày hội|Dịp tổ chức lễ hội, vui chơi đông người.
ngày kia|Hôm sau ngày mai, tức hai ngày nữa.
ngày lễ|Dịp kỷ niệm một sự kiện quan trọng, thường được nghỉ làm.
ngày mai|Hôm tiếp sau ngày hôm nay; cũng chỉ tương lai.
ngày mùa|Thời gian gặt hái, thu hoạch lúa.
ngày nay|Thời đại hiện nay, khoảng thời gian bây giờ.
ngày ngày|Mỗi ngày, ngày nào cũng thế.
ngay ngắn|Thẳng hàng, gọn gàng, đúng chỗ, không xiêu vẹo.
ngày rằm|Ngày mười lăm âm lịch, khi trăng tròn và sáng nhất trong tháng.
ngày sau|Thời gian về sau, trong tương lai.
ngày sinh|Ngày tháng năm một người chào đời.
ngày tháng|Thời gian nói chung, tính theo ngày và tháng.
ngay thật|Thật thà, thẳng thắn, không gian dối.
ngày thường|Những ngày bình thường, không phải lễ, Tết hay cuối tuần.
ngày trước|Thời gian đã qua, hồi trước đây.
ngày vui|Ngày có chuyện vui, đặc biệt là đám cưới.
ngày xuân|Những ngày của mùa xuân, nhất là dịp Tết; cũng chỉ thời tuổi trẻ.
ngày xưa|Thời gian đã qua từ rất lâu.
ngắm|Nhìn lâu, chăm chú để thưởng thức vẻ đẹp.
ngắm nghía|Nhìn đi nhìn lại thật kỹ một vật vì thích thú hoặc để xem xét.
ngắn|Có chiều dài nhỏ hoặc thời gian ít hơn bình thường.
ngăn cách|Chia tách, làm cho hai bên không liền nhau.
ngăn cản|Chặn lại, không cho người khác làm việc gì.
ngăn cấm|Không cho phép làm việc gì.
ngăn chặn|Không để điều xấu xảy ra hoặc lan rộng thêm.
ngắn gọn|Ít lời mà đủ ý, không dài dòng.
ngắn hạn|Chỉ kéo dài trong một thời gian ngắn.
ngăn kéo|Hộc đựng đồ trong bàn, tủ, kéo ra đẩy vào được.
ngăn nắp|Gọn gàng, đồ đạc được xếp đặt có thứ tự.
ngắn ngủi|Quá ngắn, trôi qua rất nhanh.
ngắn ngủn|Ngắn quá mức, trông cũn cỡn và không cân đối.
ngăn ngừa|Chặn trước để điều xấu không xảy ra.
ngắt|Làm đứt bằng tay, như ngắt hoa; cũng chỉ cắt đứt, dừng lại.
ngắt lời|Chen vào khi người khác đang nói, làm họ dừng lại.
ngắt quãng|Bị dừng giữa chừng rồi mới tiếp tục, không liền mạch.
ngâm nga|Hát hoặc đọc khẽ, kéo dài giọng một cách thong thả.
ngấm ngầm|Âm thầm, kín đáo, không để lộ ra ngoài.
ngẫm nghĩ|Suy nghĩ chậm rãi và kỹ lưỡng về một điều gì đó.
ngâm thơ|Đọc thơ với giọng kéo dài, trầm bổng theo một làn điệu riêng.
ngân hà|Dải sáng gồm vô số ngôi sao trên bầu trời đêm.
ngân hàng|Nơi nhận gửi tiền, cho vay và làm các dịch vụ về tiền.
ngân nga|Âm thanh hoặc giọng hát kéo dài, vang lên trầm bổng và êm tai.
ngần ngại|Chần chừ, e ngại, chưa dám làm.
ngân sách|Khoản tiền dự tính để chi tiêu trong một thời gian.
ngẩng đầu|Nâng đầu lên, nhìn lên phía trên.
ngẩng mặt|Ngước mặt lên cao; cũng chỉ sự tự tin, không phải xấu hổ với ai.
ngập ngừng|Nói hay làm còn do dự, ngắt quãng, chưa dứt khoát.
ngất ngây|Say mê, thích thú đến mức như mê đi.
ngẫu hứng|Nảy ra bất chợt, không dự tính trước.
ngấu nghiến|Ăn vội vàng, nhai nuốt rất nhanh; cũng chỉ đọc say mê.
ngẫu nhiên|Tình cờ xảy ra, không định trước.
ngây ngô|Khờ khạo, ngờ nghệch, thiếu hiểu biết.
ngây thơ|Trong sáng, hồn nhiên, chưa hiểu nhiều về cuộc đời.
nghe đồn|Biết được điều gì qua lời truyền miệng, chưa chắc đúng.
nghe được|Có thể nhận ra âm thanh bằng tai; cũng chỉ ở mức tạm chấp nhận được.
nghe lời|Làm theo lời dặn bảo của người khác.
nghe ngóng|Chú ý lắng nghe, dò hỏi để nắm tình hình.
nghe nói|Biết được điều gì qua lời kể của người khác.
nghe thấy|Nhận biết được âm thanh bằng tai.
nghe theo|Làm theo ý kiến, lời khuyên của ai đó.
nghe tin|Nhận được thông tin, tin tức về việc gì.
nghe trộm|Lén nghe chuyện của người khác khi họ không biết.
nghẹn|Bị vướng thức ăn ở cổ, khó nuốt; cũng chỉ xúc động đến khó nói.
nghẹt|Bị tắc, bị bít kín không thông, như ống nước bị nghẹt; cũng chỉ chật kín người.
nghệ|Cây có củ màu vàng cam, dùng làm gia vị hoặc làm đẹp.
nghề nghiệp|Công việc chuyên môn mà một người làm để sinh sống.
nghệ nhân|Người có tay nghề cao trong một nghề thủ công hoặc nghệ thuật.
nghệ thuật|Hoạt động sáng tạo ra cái đẹp như hội họa, âm nhạc; cũng chỉ sự khéo léo.
nghênh ngang|Điệu bộ ngang tàng, không coi ai ra gì; cũng chỉ đồ đạc chắn ngang lối đi.
nghêu|Loài vật có hai mảnh vỏ cứng, sống vùi trong cát biển, dùng làm món ăn.
nghi|Ngờ rằng có điều gì đó không đúng hoặc không thật.
nghỉ chân|Dừng lại nghỉ một lúc trong khi đang đi đường.
nghỉ đông|Kỳ nghỉ học hoặc nghỉ làm vào dịp mùa đông.
nghỉ hè|Kỳ nghỉ dài vào mùa hè của học sinh.
nghỉ hưu|Thôi làm việc khi đến tuổi theo quy định và nhận lương hưu.
nghĩ lại|Suy xét thêm lần nữa, có thể đổi ý so với lúc đầu.
nghi lễ|Các nghi thức, thủ tục được tiến hành trang trọng trong một buổi lễ.
nghị luận|Bàn bạc, phân tích để làm rõ một vấn đề; cũng là một kiểu bài văn.
nghị lực|Sức mạnh tinh thần giúp vượt qua khó khăn.
nghỉ mát|Đi đến nơi mát mẻ để nghỉ ngơi, thư giãn vào mùa nóng.
nghi ngờ|Không tin hẳn, cho rằng có thể có điều không đúng.
nghỉ ngơi|Tạm dừng làm việc để thư giãn, lấy lại sức.
nghỉ phép|Được phép tạm nghỉ làm trong một số ngày mà vẫn giữ chỗ làm.
nghĩ ra|Tìm ra được ý tưởng hoặc cách giải quyết nhờ suy nghĩ.
nghỉ tay|Tạm dừng việc đang làm một lúc để nghỉ ngơi cho đỡ mệt.
nghĩ thầm|Suy nghĩ trong lòng mà không nói ra cho ai biết.
nghi thức|Các bước, lễ nghi được làm theo quy định trong một buổi lễ.
nghỉ trưa|Ngả lưng hoặc chợp mắt một lát vào buổi trưa để lấy lại sức.
nghỉ việc|Thôi làm ở nơi đang làm việc; cũng là tạm không đi làm trong một thời gian.
nghĩa|Nội dung, ý được diễn đạt; cũng chỉ tình cảm, lẽ phải giữa người với người.
nghĩa bóng|Ý nghĩa ẩn dụ, suy ra từ nghĩa gốc của từ ngữ.
nghĩa đen|Nghĩa gốc, trực tiếp của từ ngữ, không theo lối ví von.
nghĩa là|Cụm từ dùng để giải thích rõ hơn điều vừa nói.
nghĩa tình|Tình cảm gắn bó, thủy chung và biết ơn giữa người với người.
nghĩa vụ|Việc mà mỗi người bắt buộc phải làm theo trách nhiệm.
nghịch|Hay làm trò, đùa phá; cũng chỉ trái ngược nhau.
nghịch ngợm|Hiếu động, hay bày trò, đùa phá.
nghiêm|Đứng đắn, chặt chẽ, không đùa cợt; cũng là tư thế đứng thẳng.
nghiêm chỉnh|Đứng đắn, đúng mực và làm đúng quy định.
nghiêm nghị|Có vẻ mặt, thái độ nghiêm trang và đứng đắn, khiến người khác nể.
nghiễm nhiên|Coi như điều đương nhiên, tự nhiên mà có được, không cần bàn cãi.
nghiêm trọng|Rất nặng nề, có thể gây hậu quả lớn.
nghiêm túc|Đứng đắn, chú tâm, không đùa cợt khi làm việc.
nghiền|Làm cho nát vụn ra bằng cách ép hoặc xay; cũng chỉ rất mê thứ gì.
nghiên cứu|Tìm hiểu kỹ lưỡng để biết thêm hoặc phát hiện điều mới.
nghiền nát|Ép, xay cho vỡ vụn ra thành mảnh rất nhỏ.
nghiến răng|Cắn chặt, cọ hai hàm răng vào nhau, có khi vô thức lúc ngủ.
nghiêng|Lệch về một bên, không thẳng đứng.
nghiêng ngả|Lắc lư, đổ qua đổ lại không đứng vững, như cây trước gió.
nghiệp dư|Không chuyên, làm vì yêu thích chứ không phải nghề chính.
nghiệp vụ|Kiến thức, kỹ năng chuyên môn của một nghề.
nghìn|Số bằng mười lần một trăm.
ngõ cụt|Lối đi không có lối ra ở phía cuối; cũng chỉ tình thế bế tắc.
ngõ hẻm|Lối đi nhỏ và hẹp len giữa các dãy nhà.
ngỏ lời|Mở lời nói ra một đề nghị, lời nhờ cậy hay tình cảm của mình.
ngõ ngách|Những lối đi nhỏ, hẹp và quanh co; cũng chỉ mọi chỗ, kể cả nơi khuất.
ngọ nguậy|Cựa quậy, động đậy liên tục, không chịu nằm hay ngồi yên.
ngỏ ý|Cho người khác biết điều mình mong muốn hoặc định làm.
ngoài|Phía bên kia giới hạn, không ở trong; cũng có nghĩa là trừ ra.
ngoại cỡ|Có kích thước lớn hơn hẳn cỡ thông thường.
ngoài cùng|Nằm ở vị trí xa nhất về phía bên ngoài.
ngoại hình|Vẻ bề ngoài của một người như dáng người, khuôn mặt.
ngoài khơi|Vùng biển cách xa bờ.
ngoại lệ|Trường hợp riêng, không theo quy tắc chung.
ngoài mặt|Bề ngoài thể hiện ra, có thể khác với suy nghĩ thật.
ngoại ngữ|Tiếng của nước ngoài, không phải tiếng mẹ đẻ.
ngoại nhập|Được mua và đưa về từ nước ngoài, nói về hàng hóa.
ngoại ô|Vùng ven, nằm sát bên ngoài thành phố.
ngoại quốc|Quốc gia khác, không phải nước của mình.
ngoài ra|Cụm từ dùng để nói thêm điều khác, bên cạnh điều đã nêu.
ngoài rìa|Ở phần mép phía ngoài; cũng chỉ bị gạt ra, không được tham gia.
ngoại thành|Vùng nằm ngoài khu nội thành của một thành phố.
ngoại thất|Phần bên ngoài của nhà cửa, xe cộ cùng cách trang trí phía ngoài.
ngoài trời|Nơi không có mái che, ở bên ngoài nhà.
ngoại trừ|Không tính đến, để riêng ra khỏi số còn lại.
ngoan|Biết vâng lời, cư xử dễ thương, không quấy phá.
ngoan cố|Cố chấp, khăng khăng không chịu thay đổi dù đã sai.
ngoạn mục|Đẹp mắt, hấp dẫn, khiến người xem thích thú.
ngoan ngoãn|Biết nghe lời, cư xử lễ phép, dễ bảo.
ngoảnh lại|Quay đầu nhìn về phía sau; cũng chỉ việc nhìn lại quãng thời gian đã qua.
ngoặc đơn|Cặp dấu ngoặc tròn dùng để kẹp phần giải thích thêm trong câu.
ngoặc kép|Cặp dấu câu dùng để trích lời nói hay nhấn mạnh một từ.
ngọc|Đá quý có màu đẹp, dùng làm đồ trang sức.
ngọc bích|Loại ngọc màu xanh biếc, trong và đẹp, dùng làm trang sức.
ngọc lan|Cây có hoa màu trắng hoặc vàng nhạt, rất thơm.
ngóc ngách|Những chỗ nhỏ hẹp, khuất khúc khó thấy.
ngọc trai|Viên tròn, bóng, hình thành trong con trai, dùng làm trang sức.
ngói|Tấm đất nung dùng để lợp mái nhà.
ngòi bút|Đầu nhọn của cây bút, nơi mực chảy ra; cũng chỉ tài viết văn.
ngon|Có vị hấp dẫn, ăn uống thấy thích thú.
ngón cái|Ngón to và mập nhất của bàn tay hoặc bàn chân.
ngón chân|Từng phần nhỏ, dài ở đầu bàn chân.
ngọn cỏ|Phần đầu trên cùng của cây cỏ.
ngọn đèn|Chiếc đèn tỏa ánh sáng, thường dùng trong văn chương.
ngọn đuốc|Bó vật dễ cháy được đốt lên để soi sáng.
ngon giấc|Ngủ say và sâu, không bị thức giấc giữa chừng.
ngọn gió|Luồng gió thổi tới, thường dùng trong văn thơ.
ngon lành|Ngon và hấp dẫn; cũng chỉ việc làm dễ dàng, trơn tru.
ngọn lửa|Phần lửa bốc lên khi cháy, có ánh sáng và hơi nóng.
ngon miệng|Ăn thấy ngon, thấy thích, ăn được nhiều.
ngon ngọt|Ngon và ngọt; thường chỉ lời nói dễ nghe để dỗ dành.
ngọn nguồn|Nơi bắt đầu của dòng sông; cũng chỉ nguyên nhân sâu xa của sự việc.
ngón tay|Từng phần nhỏ, dài ở đầu bàn tay, cử động linh hoạt.
ngón trỏ|Ngón tay nằm cạnh ngón cái, thường dùng để chỉ.
ngón út|Ngón nhỏ nhất, nằm ở rìa ngoài bàn tay hoặc bàn chân.
ngóng chờ|Mong mỏi chờ đợi ai đó đến hoặc điều gì đó xảy ra.
ngóng trông|Mong mỏi, hướng mắt trông đợi người thân hay tin tức từ xa.
ngọt|Có vị như đường hay mật; cũng chỉ lời nói dịu dàng, dễ nghe.
ngọt bùi|Vị ngọt và bùi; thường chỉ niềm vui, hạnh phúc được sẻ chia cùng nhau.
ngọt dịu|Có vị ngọt nhẹ, dễ chịu, không gắt; cũng chỉ lời nói êm ái.
ngọt lịm|Ngọt đậm và dễ chịu, như tan dần trong miệng.
ngọt ngào|Ngọt và dễ chịu; cũng chỉ tình cảm, lời nói dịu dàng, êm ái.
ngổ ngáo|Có vẻ bướng bỉnh, ngang tàng, không biết sợ ai.
ngộ nghĩnh|Dễ thương và hay hay một cách lạ mắt, thường nói về trẻ nhỏ.
ngộ nhận|Hiểu sai, nhận định nhầm về một điều gì.
ngồi bệt|Ngồi thẳng xuống đất hoặc sàn nhà, không cần ghế hay chiếu.
ngồi dậy|Từ tư thế nằm chuyển sang tư thế ngồi.
ngồi không|Ngồi yên không làm việc gì, rảnh rỗi.
ngôi nhà|Công trình xây dựng để con người ở và sinh hoạt.
ngôi sao|Thiên thể tự phát sáng trên bầu trời; cũng chỉ người nổi tiếng.
ngồi xổm|Ngồi co gối, chỉ có hai bàn chân chạm đất.
ngổn ngang|Nhiều thứ nằm bừa bộn, lộn xộn; cũng chỉ lòng dạ rối bời.
ngôn ngữ|Hệ thống tiếng nói và chữ viết để con người giao tiếp.
ngỗng|Loài gia cầm cùng họ với vịt, cổ dài, kêu to.
ngỗng trời|Loài chim lớn giống ngỗng, sống hoang dã, hay bay thành đàn theo mùa.
ngột ngạt|Khó thở vì thiếu không khí; cũng chỉ bầu không khí căng thẳng.
ngơ ngác|Lạ lẫm, bối rối, không hiểu chuyện gì đang xảy ra.
ngỡ ngàng|Bất ngờ, sững sờ trước điều không ngờ tới.
ngớ ngẩn|Khờ khạo, thiếu suy nghĩ, nói hoặc làm điều vô lý.
ngờ ngợ|Thấy hơi quen hoặc hơi nghi nhưng chưa dám chắc chắn.
ngũ cốc|Các loại hạt ăn được như lúa, ngô, lúa mì.
ngủ dậy|Thức giấc và ra khỏi giường sau giấc ngủ.
ngủ đông|Trạng thái nghỉ ngơi kéo dài qua mùa đông của một số loài vật.
ngủ gật|Thiếp đi trong chốc lát khi đang ngồi, đầu gật gù.
ngủ gục|Thiếp đi trong tư thế ngồi, đầu gục xuống bàn.
ngủ ngày|Đi ngủ vào ban ngày thay vì buổi tối như thường lệ.
ngủ ngon|Có giấc ngủ say và dễ chịu; cũng là lời chúc buổi tối.
ngủ nhờ|Tạm ngủ lại ở nhà người khác khi không về được chỗ mình.
ngủ quên|Lỡ ngủ quá giờ nên quên mất việc cần làm.
ngủ say|Chìm sâu vào giấc ngủ, khó bị đánh thức.
ngủ trưa|Chợp mắt một giấc ngắn vào buổi trưa.
ngụ ý|Ý muốn nói được ẩn kín bên trong lời nói.
ngụm|Lượng nước hay đồ uống vừa một lần hớp vào miệng.
nguội lạnh|Đã mất hết hơi nóng; cũng chỉ tình cảm phai nhạt, thờ ơ.
nguồn|Nơi bắt đầu của dòng sông, suối; cũng chỉ nơi cung cấp thứ gì.
nguồn điện|Nơi cung cấp điện cho máy móc, thiết bị hoạt động.
nguồn gốc|Nơi hoặc điều mà từ đó một người, vật bắt đầu có.
nguồn lực|Những gì có thể huy động để làm việc, như con người, tiền bạc, vật tư.
nguồn sáng|Vật tự phát ra ánh sáng, như Mặt Trời, ngọn nến, bóng đèn.
nguồn tin|Người hoặc nơi cung cấp tin tức, thông tin.
nguy cơ|Khả năng xảy ra điều xấu, điều nguy hiểm.
nguy hiểm|Có thể gây ra tai nạn hoặc thiệt hại.
nguy nga|To lớn, lộng lẫy và tráng lệ, thường nói về công trình.
nguyên|Còn đủ, chưa bị mất mát hay thay đổi; cũng chỉ người từng giữ một chức vụ.
nguyên âm|Âm phát ra khi luồng hơi qua miệng không bị cản, như a, e, o.
nguyên bản|Bản gốc ban đầu, chưa bị sửa đổi hay dịch.
nguyên chất|Không pha trộn với chất nào khác.
nguyên do|Lý do gây ra hoặc dẫn đến một sự việc.
nguyên liệu|Vật liệu ban đầu dùng để chế biến hay sản xuất.
nguyên mẫu|Mẫu đầu tiên làm ra để thử nghiệm; cũng chỉ người thật được đưa vào truyện.
nguyên nhân|Điều làm nảy sinh ra một sự việc, hiện tượng nào đó.
nguyên tắc|Điều cơ bản đã định ra, phải tuân theo khi làm việc.
nguyên tố|Chất đơn giản chỉ gồm một loại nguyên tử, như sắt, đồng, vàng.
nguyên tử|Hạt cực nhỏ cấu tạo nên vật chất, gồm hạt nhân và lớp vỏ điện tử.
nguyên vẹn|Còn đầy đủ, không bị hư hỏng hay sứt mẻ.
nguyện vọng|Điều mong muốn, ước ao được thực hiện.
nguyệt quế|Cây cảnh hoa trắng nhỏ, rất thơm; vòng lá nguyệt quế là biểu tượng chiến thắng.
ngữ pháp|Các quy tắc về cách dùng từ và đặt câu trong một ngôn ngữ.
ngữ văn|Môn học về tiếng Việt và văn học ở nhà trường.
ngựa|Thú lớn chân cao, chạy nhanh, nuôi để cưỡi hoặc kéo xe.
ngựa gỗ|Đồ chơi hình con ngựa làm bằng gỗ, trẻ em cưỡi để bập bênh.
ngựa ô|Con ngựa có bộ lông màu đen tuyền.
ngựa vằn|Loài ngựa hoang ở châu Phi, lông có sọc đen trắng.
ngửi|Hít vào bằng mũi để nhận biết mùi.
ngừng|Thôi không tiếp tục làm, dừng lại.
ngưng tụ|Hơi chuyển thành chất lỏng, như hơi nước đọng thành giọt khi gặp lạnh.
ngược|Theo chiều trái lại, đối nghịch với hướng thông thường.
ngược chiều|Đi theo hướng trái với hướng quy định hoặc với người khác.
ngược dòng|Đi theo hướng trái với dòng nước chảy; cũng chỉ quay về quá khứ.
ngược đời|Trái với lẽ thường, khác người.
ngược gió|Đi hoặc chuyển động theo hướng ngược với chiều gió thổi.
ngược lại|Trái với điều vừa nói; cũng chỉ quay trở lại.
ngược xuôi|Đi lại tất bật khắp nơi, lúc lên lúc xuống để lo toan công việc.
người|Sinh vật có trí khôn, biết nói và lao động; cũng chỉ thân thể.
người cá|Nhân vật trong truyện, nửa trên là người, nửa dưới là đuôi cá.
người dưng|Người không có quan hệ họ hàng, thân thích gì với mình.
người đẹp|Người con gái có nhan sắc xinh đẹp.
người già|Người lớn tuổi, đã sống lâu năm.
người hầu|Người làm công việc phục vụ trong nhà người khác.
người hùng|Người dũng cảm, làm việc lớn lao được mọi người ngưỡng mộ.
người lạ|Người mình chưa từng quen biết.
người làm|Người được thuê để làm việc, nhất là giúp việc trong gia đình.
người lớn|Người đã trưởng thành, không còn là trẻ con.
người máy|Máy được lập trình để làm việc thay người, có khi trông giống người.
người mẫu|Người trình diễn quần áo hoặc làm mẫu để chụp ảnh, vẽ tranh.
người mình|Người cùng phe, cùng nhóm hoặc cùng quê hương, đất nước với mình.
người ngoài|Người không thuộc gia đình hay nhóm của mình.
người nhà|Người trong gia đình, họ hàng thân thuộc.
người quen|Người mình đã biết và có quan hệ quen biết.
người ta|Những người khác nói chung; cũng chỉ một người được nhắc tới.
người thân|Người có quan hệ ruột thịt hoặc gắn bó gần gũi.
người thợ|Người làm nghề lao động bằng tay, có tay nghề.
người thường|Người bình thường, không có gì đặc biệt.
người xưa|Những người sống ở thời trước, ông cha ta.
người yêu|Người mình yêu và có quan hệ tình cảm.
ngượng|Cảm thấy xấu hổ, không tự nhiên trước người khác.
ngưỡng cửa|Thanh ngang ở chân khung cửa; cũng chỉ bước đầu của giai đoạn mới.
ngưỡng mộ|Kính phục và yêu mến ai đó.
ngượng nghịu|Lúng túng, thiếu tự nhiên trong cử chỉ, lời nói.
ngượng ngùng|Có vẻ e thẹn, xấu hổ, không tự nhiên.
nhà ăn|Phòng lớn để mọi người ăn chung ở trường học, cơ quan, nhà máy.
nhà báo|Người làm nghề viết tin, bài cho báo chí.
nhà bếp|Gian phòng dùng để nấu nướng, chuẩn bị bữa ăn.
nhà chồng|Gia đình bên chồng của người phụ nữ đã kết hôn.
nhà cửa|Nhà để ở và mọi thứ thuộc về ngôi nhà nói chung.
nhà ga|Nơi tàu hỏa hoặc máy bay dừng đón, trả khách và hàng hóa.
nhà gái|Gia đình, họ hàng bên cô dâu trong việc cưới hỏi.
nhà giáo|Người làm nghề dạy học.
nhà giàu|Gia đình hoặc người có nhiều tiền của.
nhà gỗ|Ngôi nhà được dựng chủ yếu bằng gỗ.
nhà hàng|Nơi kinh doanh nấu và bán các món ăn, đồ uống.
nhà hát|Công trình lớn dùng để biểu diễn ca nhạc, kịch, múa.
nhà khách|Nơi dành để đón tiếp và cho khách ở lại.
nhà kho|Nơi cất giữ hàng hóa, đồ đạc.
nhà kính|Nhà làm bằng kính hoặc nhựa trong để trồng cây.
nhà lá|Ngôi nhà đơn sơ có mái lợp bằng lá, như lá dừa, lá cọ.
nhà máy|Nơi có nhiều máy móc để sản xuất hàng hóa.
nhà ngói|Ngôi nhà có mái lợp bằng ngói, thường vững chãi hơn nhà tranh.
nhã nhặn|Lịch sự, hòa nhã trong cách nói năng và cư xử.
nhà nông|Người làm nghề nông, sống bằng trồng trọt và chăn nuôi.
nhà ở|Ngôi nhà dùng làm nơi sinh sống của con người.
nhà riêng|Nơi ở riêng của một người hay một gia đình, khác với nơi làm việc.
nhà rông|Ngôi nhà chung cao lớn, mái dốc của buôn làng Tây Nguyên, dùng để hội họp.
nhà sách|Cửa hàng bán sách, báo và đồ dùng học tập.
nhà sàn|Kiểu nhà dựng trên các cột cao, sàn cách mặt đất, phổ biến ở miền núi.
nhà tắm|Phòng dùng để tắm rửa, vệ sinh cá nhân.
nhà thầu|Cá nhân hoặc công ty nhận thi công công trình, dự án theo hợp đồng.
nhà thơ|Người chuyên sáng tác thơ ca.
nhà tôi|Ngôi nhà của tôi; cũng là cách gọi vợ hoặc chồng mình với người khác.
nhà trai|Gia đình, họ hàng bên chú rể trong việc cưới hỏi.
nhà tranh|Ngôi nhà đơn sơ, mái lợp bằng cỏ tranh, rơm hoặc lá.
nhà trẻ|Nơi trông giữ, chăm sóc trẻ nhỏ khi bố mẹ đi làm.
nhà trọ|Chỗ thuê phòng để ở tạm, thường dành cho sinh viên hoặc người đi làm xa.
nhà trường|Trường học nói chung, gồm cả thầy cô và ban giám hiệu.
nhà văn|Người chuyên viết truyện, tiểu thuyết và các tác phẩm văn học.
nhà vợ|Gia đình bên vợ, gồm bố mẹ và anh chị em của vợ.
nhà vua|Người đứng đầu một vương quốc, trị vì theo chế độ quân chủ.
nhà vườn|Ngôi nhà có vườn cây bao quanh; cũng chỉ người làm nghề trồng cây, hoa trái.
nhà xe|Chỗ để xe cộ; cũng chỉ hãng hoặc chủ xe khách chở người.
nhà xưởng|Công trình rộng lớn dùng để sản xuất, chế tạo hàng hóa.
nhạc|Âm thanh có giai điệu, nhịp điệu, được sáng tác để nghe hoặc hát theo.
nhạc công|Người chơi nhạc cụ, biểu diễn trong ban nhạc hay dàn nhạc.
nhạc cụ|Dụng cụ dùng để tạo ra âm nhạc như đàn, sáo, trống.
nhạc nhẹ|Dòng nhạc phổ thông có giai điệu êm ái, dễ nghe, dễ thuộc.
nhạc phẩm|Một tác phẩm âm nhạc, như một bài hát hay bản nhạc.
nhạc sống|Âm nhạc được ca sĩ, nhạc công biểu diễn trực tiếp, không phát từ bản thu.
nhạc trưởng|Người chỉ huy dàn nhạc; cũng chỉ người dẫn dắt, điều phối cả nhóm.
nhạc viện|Trường chuyên đào tạo về âm nhạc.
nhai|Nghiền thức ăn trong miệng bằng răng.
nhai lại|Nhai lần nữa thức ăn đã nuốt, như trâu bò; cũng chỉ nói lặp lại.
nhàm chán|Lặp đi lặp lại, không có gì mới nên gây chán.
nham thạch|Đá nóng chảy phun ra từ miệng núi lửa.
nhan đề|Tên đặt cho một cuốn sách, bài viết hay tác phẩm.
nhàn hạ|Rảnh rỗi, thong thả, không phải làm việc vất vả.
nhãn hiệu|Tên gọi hoặc dấu hiệu riêng giúp phân biệt hàng hóa của từng nhà sản xuất.
nhàn nhã|Thong thả, thư thái, không phải bận rộn vất vả.
nhan nhản|Có rất nhiều, gặp ở khắp nơi, đâu đâu cũng thấy.
nhàn rỗi|Không có việc gì phải làm, có nhiều thời gian thong thả.
nhan sắc|Vẻ đẹp khuôn mặt của người phụ nữ.
nhánh|Phần nhỏ tách ra từ thân cây, dòng sông hay con đường chính.
nhanh chóng|Mau lẹ, diễn ra trong thời gian ngắn.
nhanh gọn|Nhanh và gọn gàng, không rườm rà.
nhanh lẹ|Di chuyển hoặc làm việc nhanh và gọn, không chậm chạp.
nhanh nhạy|Nhanh và nhạy bén trong việc nắm bắt, phản ứng.
nhanh nhẹn|Hoạt bát, cử động và làm việc nhanh.
nhanh tay|Thao tác bằng tay nhanh; cũng chỉ hành động kịp thời, không chậm trễ.
nhanh trí|Suy nghĩ nhanh, biết ứng phó kịp thời.
nhào lộn|Xoay lộn người trên không hoặc trên mặt đất, như diễn viên xiếc.
nhào nặn|Trộn và nặn vật liệu mềm thành hình; cũng chỉ việc rèn giũa, tạo dựng.
nháo nhào|Chạy tán loạn, xô đẩy nhau một cách hỗn loạn và vội vã.
nhão nhẹt|Mềm nhão quá mức, bết dính lại, trông không ngon mắt.
nhão nhoẹt|Rất nhão, mềm bết và dính, không còn giữ được hình dạng.
nhát gan|Dễ sợ hãi, thiếu can đảm.
nhạt nhẽo|Quá nhạt, không có vị; cũng chỉ người hay chuyện kém thú vị.
nhau|Từ chỉ quan hệ qua lại giữa hai hay nhiều người, vật.
nhàu nát|Nhăn nhúm, dúm dó và cũ nát, không còn phẳng phiu.
nháy|Chớp mắt thật nhanh để ra hiệu; cũng chỉ đèn lóe sáng rồi tắt.
nhạy bén|Nhanh nhạy, sớm nhận ra và phản ứng kịp với tình hình.
nhạy cảm|Dễ cảm nhận, dễ xúc động; cũng chỉ vấn đề tế nhị, dễ gây tranh cãi.
nhảy cao|Môn điền kinh chạy lấy đà rồi bật người vượt qua xà ngang.
nhảy cẫng|Bật nhảy lên vì quá vui mừng hoặc phấn khích.
nhảy cóc|Bật người lên từng bước như con cóc; cũng chỉ việc bỏ qua các bước trung gian.
nhảy cỡn|Tung tăng nhảy nhót vì vui sướng, thường nói về trẻ con hay con vật.
nhảy dây|Trò chơi bật nhảy qua sợi dây được quay vòng liên tục.
nhảy dù|Rời máy bay trên cao rồi bung dù để từ từ hạ xuống đất.
nháy mắt|Chớp một bên mắt để ra hiệu; cũng chỉ khoảnh khắc rất ngắn.
nhảy múa|Cử động thân thể nhịp nhàng theo điệu nhạc để vui chơi hay biểu diễn.
nhảy nhót|Chạy nhảy tung tăng không ngừng; cũng chỉ việc khiêu vũ cho vui.
nhảy vọt|Tăng lên hoặc tiến bộ rất nhanh, vượt hẳn trong thời gian ngắn.
nhảy xa|Môn điền kinh chạy lấy đà rồi bật người về phía trước thật xa.
nhắc lại|Nói lại điều đã nói hoặc làm lại thêm lần nữa.
nhắc nhở|Nói cho người khác nhớ, chú ý để làm hoặc sửa.
nhắm|Khép mi mắt lại; cũng là hướng vào một mục tiêu nào đó.
nhắm mắt|Khép hai mắt lại; cũng chỉ việc làm ngơ, coi như không thấy.
nhăn mặt|Co nét mặt lại vì khó chịu hoặc không vừa ý.
nhăn nheo|Có nhiều nếp nhăn, không phẳng, như da người già.
nhăn nhó|Nét mặt cau có, tỏ vẻ khó chịu hoặc bực bội.
nhắn nhủ|Dặn dò, khuyên bảo ân cần với người khác.
nhắn tin|Gửi lời nhắn bằng chữ qua điện thoại hoặc mạng.
nhặt|Cầm vật ở dưới đất lên; cũng là lựa bỏ phần hỏng của rau.
nhấc bổng|Nâng hẳn người hay vật lên khỏi mặt đất một cách nhẹ nhàng.
nhầm lẫn|Hiểu sai hoặc làm sai, tưởng cái này là cái kia.
nhâm nhi|Ăn hoặc uống từng chút một, chậm rãi để thưởng thức.
nhẫn|Vòng nhỏ đeo ở ngón tay để làm đẹp hoặc làm kỷ niệm.
nhân ái|Giàu lòng yêu thương, quan tâm đến người khác.
nhân bản|Tạo ra bản sao giống hệt bản gốc; cũng chỉ tinh thần coi trọng con người.
nhận biết|Nhìn, nghe mà biết và phân biệt được.
nhân cách|Phẩm chất, tư cách đạo đức của mỗi con người.
nhân công|Người lao động làm thuê; cũng chỉ sức lao động nói chung.
nhẫn cưới|Chiếc nhẫn cô dâu và chú rể trao cho nhau trong lễ cưới.
nhận dạng|Xác định người hay vật dựa vào hình dáng, đặc điểm bên ngoài.
nhân danh|Lấy danh nghĩa của một người hay tổ chức để nói hoặc làm việc gì.
nhận diện|Dựa vào đặc điểm để biết được đó là ai, là cái gì.
nhân dịp|Vào lúc có sự kiện hay cơ hội nào đó, như lễ, Tết.
nhân đạo|Có lòng thương người, biết tôn trọng và giúp đỡ con người.
nhận định|Đưa ra ý kiến đánh giá hoặc dự đoán về một vấn đề.
nhân hậu|Hiền lành, tốt bụng và giàu lòng thương người.
nhân loại|Toàn thể loài người trên Trái Đất.
nhận lời|Đồng ý với lời mời hoặc lời đề nghị của người khác.
nhân lực|Nguồn lao động, sức người dùng vào công việc.
nhấn mạnh|Nói rõ, làm nổi bật một ý để người khác chú ý.
nhẫn nại|Kiên trì, bền bỉ chịu đựng khó khăn, không nóng vội.
nhẫn nhịn|Cố nén giận, chịu đựng để tránh xảy ra xích mích.
nhân nhượng|Chịu nhường một phần để giữ hòa khí hoặc đạt được thỏa thuận.
nhận ra|Thấy, hiểu hoặc nhớ ra được điều gì, người nào.
nhân sâm|Loại cây có rễ quý, thường dùng làm thuốc bổ.
nhân sự|Người làm việc trong cơ quan; cũng chỉ việc tuyển dụng, quản lý nhân viên.
nhân tài|Người có tài năng nổi bật, có ích cho xã hội.
nhân tạo|Do con người làm ra, không có sẵn trong tự nhiên.
nhận thấy|Thấy được, biết được qua quan sát hoặc suy nghĩ.
nhận thức|Sự hiểu biết về thế giới xung quanh; cũng là hiểu ra điều gì đó.
nhân tiện|Tiện lúc đang làm việc này thì làm thêm việc khác.
nhân tố|Yếu tố góp phần tạo nên kết quả; cũng chỉ người có vai trò quan trọng.
nhân từ|Hiền hậu, thương người và dễ tha thứ.
nhân văn|Thuộc về văn hóa con người; thể hiện sự tôn trọng, yêu thương con người.
nhân vật|Người được miêu tả trong truyện, phim; cũng chỉ người có vai trò nổi bật.
nhận việc|Đồng ý làm hoặc bắt đầu đi làm một công việc.
nhân viên|Người làm việc cho một cơ quan, công ty hoặc cửa hàng.
nhận xét|Nêu ý kiến đánh giá về người hoặc sự việc.
nhập|Đưa vào, gộp vào; cũng là đưa hàng hóa từ nơi khác về.
nhập cảnh|Đi vào lãnh thổ của một nước khác qua cửa khẩu hoặc sân bay.
nhập học|Bắt đầu vào học ở một trường.
nhập hội|Gia nhập, trở thành thành viên của một hội, nhóm.
nhập khẩu|Mua hàng hóa từ nước ngoài đưa về trong nước.
nhấp nháy|Lóe sáng rồi tắt liên tục; cũng chỉ mắt chớp liên hồi.
nhấp nhô|Lúc cao lúc thấp nối tiếp nhau, không đều, như sóng.
nhập tâm|Ghi nhớ sâu vào trong đầu đến mức thuộc lòng, khó quên.
nhập vai|Hóa thân vào một nhân vật khi diễn kịch, đóng phim hoặc chơi trò chơi.
nhất định|Chắc chắn như vậy, không thay đổi; cũng chỉ một mức cụ thể nào đó.
nhất là|Dùng để nêu điều nổi bật hơn cả so với những điều khác.
nhất quán|Trước sau như một, không mâu thuẫn hay thay đổi.
nhất quyết|Quyết tâm giữ ý định, không chịu thay đổi.
nhất thiết|Bắt buộc phải có hoặc phải làm, không thể khác.
nhất thời|Chỉ trong một thời gian ngắn, không lâu dài.
nhật thực|Hiện tượng Mặt Trăng che khuất Mặt Trời khi nhìn từ Trái Đất.
nhất trí|Cùng một ý kiến, đồng lòng với nhau.
nhẹ dạ|Dễ tin lời người khác nên dễ bị lừa.
nhẹ nhàng|Không nặng nề; cũng chỉ cử chỉ, lời nói êm dịu, từ tốn.
nhè nhẹ|Ở mức khẽ khàng, êm dịu, không mạnh.
nhẹ nhõm|Cảm thấy thoải mái, thanh thản khi đã hết lo âu.
nhe răng|Hé môi để lộ hàm răng ra, thường khi cười toe toét.
nhẹ tay|Làm khẽ khàng, không dùng nhiều sức; cũng chỉ xử phạt không nặng.
nheo|Khép hờ mắt lại cho hẹp, thường khi nhìn chói hay để ra hiệu.
nhét|Đút, ấn vật gì vào chỗ chật hoặc khe hẹp.
nhếch mép|Kéo khóe miệng lệch lên một bên, thường để cười nhạt hoặc tỏ ý chê.
nhếch nhác|Bẩn thỉu, lôi thôi, không gọn gàng.
nhện|Con vật nhỏ có tám chân, biết giăng tơ bắt mồi.
nhí nhảnh|Vui tươi, hồn nhiên, hay cười nói, thường nói về trẻ em, thiếu nữ.
nhích|Dịch chuyển một chút; cũng chỉ tăng lên chút ít.
nhiệm vụ|Công việc được giao và phải hoàn thành.
nhiên liệu|Chất đốt để tạo nhiệt hoặc năng lượng như xăng, than, củi.
nhiếp ảnh|Nghề hoặc nghệ thuật chụp ảnh.
nhiệt|Hơi nóng, mức nóng của vật hay môi trường.
nhiệt điện|Điện được sản xuất bằng cách đốt than, dầu hoặc khí để tạo nhiệt.
nhiệt độ|Mức nóng hay lạnh của vật hoặc không khí.
nhiệt đới|Vùng khí hậu nóng nằm hai bên đường xích đạo.
nhiệt huyết|Lòng hăng hái, say mê và nhiệt tình.
nhiệt kế|Dụng cụ dùng để đo nhiệt độ của cơ thể hay không khí.
nhiệt liệt|Rất sôi nổi, mạnh mẽ, thường nói về sự hoan nghênh, chào mừng.
nhiệt tình|Hăng hái, sốt sắng và hết lòng với công việc hay người khác.
nhiều|Có số lượng lớn, không ít.
nhiều chuyện|Hay xen vào chuyện người khác, thích bàn tán.
nhiều lời|Hay nói dông dài, nói quá nhiều.
nhím|Thú nhỏ có bộ lông cứng nhọn như gai phủ trên lưng.
nhím biển|Động vật sống ở biển, thân tròn phủ đầy gai, còn gọi là cầu gai.
nhìn|Đưa mắt hướng về phía nào đó để thấy.
nhìn chung|Xét một cách tổng quát, không đi vào chi tiết.
nhịn đói|Chịu không ăn dù đang đói.
nhìn nhận|Xem xét để đánh giá; cũng là thừa nhận một điều gì đó.
nhìn thấy|Dùng mắt nhận ra được người hoặc vật.
nhịp|Sự lặp lại đều đặn theo thời gian của âm thanh hay chuyển động.
nhịp điệu|Sự nhanh chậm, mạnh nhẹ lặp lại có quy luật trong âm nhạc, thơ ca.
nhịp độ|Mức độ nhanh hay chậm của một hoạt động.
nhịp nhàng|Đều đặn, ăn khớp với nhau theo nhịp.
nhỏ bé|Có kích thước nhỏ; cũng chỉ ít giá trị, không đáng kể.
nhỏ con|Có thân hình nhỏ, thấp bé.
nhỏ giọt|Chảy ra từng giọt một; cũng chỉ cho từng chút một, không đủ.
nhỏ hẹp|Có diện tích hoặc phạm vi bé, không rộng rãi.
nhỏ lửa|Để lửa yếu khi đun nấu cho món ăn chín từ từ.
nhỏ mọn|Ít ỏi, không đáng kể; cũng chỉ tính hẹp hòi, hay chấp nhặt.
nhỏ người|Có vóc dáng bé nhỏ, không cao lớn.
nhỏ nhắn|Có dáng vẻ bé xinh, gọn gàng, dễ thương.
nhỏ nhặt|Vụn vặt, ít quan trọng, không đáng để ý.
nhỏ nhẹ|Nói năng khẽ khàng, dịu dàng và từ tốn.
nhỏ nhen|Hẹp hòi, hay để bụng và tính toán những chuyện vặt.
nho nhỏ|Hơi nhỏ, nhỏ nhắn xinh xắn.
nhỏ tuổi|Còn ít tuổi, trẻ hơn so với người khác.
nhỏ xíu|Có kích thước rất bé, bé tí tẹo.
nhóc|Cách gọi thân mật hoặc trêu đùa một đứa trẻ.
nhóc con|Đứa trẻ còn bé, thường được gọi đùa hoặc thân mật.
nhóm|Tập hợp một số người hoặc vật; cũng là làm cho lửa bắt cháy.
nhóm trưởng|Người đứng đầu, phụ trách một nhóm.
nhọn|Có đầu hoặc mũi thon nhỏ lại và sắc.
nhón chân|Kiễng gót lên, đứng hoặc bước đi bằng đầu các ngón chân.
nhọn hoắt|Rất nhọn, đầu nhỏ và sắc như mũi kim.
nhõng nhẽo|Hay làm nũng, đòi người khác chiều chuộng, thường nói về trẻ con.
nhổ neo|Kéo neo lên để tàu thuyền rời bến, bắt đầu chuyến đi.
nhồi|Nhét cho đầy chặt vào bên trong; cũng là nhào trộn bột.
nhồi nhét|Nhét vào thật nhiều; cũng chỉ bắt học quá nhiều trong thời gian ngắn.
nhộn nhịp|Đông vui, náo nhiệt, có nhiều người qua lại.
nhốt|Giữ người hoặc con vật trong chỗ kín, không cho ra ngoài.
nhờ cậy|Trông mong vào người khác để được giúp đỡ.
nhờ có|Được ai đó hoặc điều gì đó giúp mà có kết quả tốt.
nhớ đời|Khó quên suốt đời, thường nói về bài học hay kỷ niệm sâu sắc.
nhớ lại|Gợi lại trong đầu những điều đã qua.
nhớ mong|Nhớ nhung và mong mỏi được gặp lại người thân yêu.
nhớ nhà|Mong về nhà, nghĩ nhiều đến gia đình khi phải ở xa.
nhớ nhung|Luôn nghĩ đến và mong gặp người đang ở xa.
nhớ ơn|Luôn ghi nhớ và biết ơn người đã giúp đỡ mình.
nhớ ra|Chợt nghĩ lại được điều tưởng đã quên.
nhớ thương|Luôn nghĩ đến ai đó với tình cảm yêu thương, quyến luyến.
nhờ vả|Cậy người khác giúp đỡ mình, thường là nhiều lần.
nhớp nháp|Dính dáp, ẩm ướt, gây cảm giác khó chịu khi chạm vào.
nhợt nhạt|Có màu nhạt, thiếu tươi tắn, thường nói về nước da.
nhu cầu|Điều cần có hoặc mong muốn được đáp ứng.
nhuận|Có thêm ngày hoặc tháng so với thường lệ, như năm nhuận, tháng nhuận.
nhúc nhích|Cử động nhẹ, chuyển động chút ít.
nhúm|Lượng nhỏ vừa cầm được giữa mấy đầu ngón tay.
nhún nhảy|Cử động người lên xuống nhịp nhàng theo điệu nhạc, vẻ vui tươi.
nhún vai|Nhô hai vai lên rồi hạ xuống, tỏ ý không biết hoặc không quan tâm.
nhúng|Cho vật vào chất lỏng một lúc rồi nhấc ra.
nhuộm|Làm cho thấm màu, đổi màu bằng thuốc hoặc chất màu.
nhuộm màu|Làm cho vải, tóc hoặc vật gì đó có màu mới.
nhút nhát|Rụt rè, hay e sợ, không mạnh dạn.
nhuyễn|Mềm và mịn, nhỏ đều do được nghiền kỹ; cũng chỉ rất thành thạo.
như cũ|Giống hệt trước đây, không có gì thay đổi.
như là|Giống với, tựa như; cũng dùng để đưa ra ví dụ.
như nhau|Giống hệt nhau, ngang bằng, không có gì khác biệt.
như sau|Dùng để giới thiệu những điều sắp được nói hoặc liệt kê tiếp theo.
như thế|Theo cách đó, giống điều vừa được nói đến.
như thường|Vẫn bình thường như mọi khi, không có gì thay đổi.
như vậy|Giống điều vừa nói; cũng dùng để rút ra kết luận.
như ý|Đúng với điều mình mong muốn.
nhựa|Chất dẻo dùng làm nhiều đồ vật; cũng là chất lỏng tiết ra từ cây.
nhựa đường|Chất màu đen, dẻo, dùng để rải mặt đường.
nhưng mà|Từ nối hai ý trái ngược nhau, thường dùng trong lời nói.
nhược điểm|Mặt yếu kém, chỗ còn hạn chế của người hoặc vật.
nhường|Để phần của mình cho người khác hoặc cho họ làm trước.
nhượng bộ|Chịu lùi một bước, chấp nhận một phần yêu cầu của người khác.
nhường nhịn|Chịu thiệt, nhún nhường để giữ hòa thuận với người khác.
niềm nở|Vui vẻ, nhiệt tình khi tiếp đón người khác.
niêm phong|Đóng kín và dán tem, đóng dấu để không ai được tự ý mở.
niềm tin|Sự tin tưởng vào người hoặc điều gì đó.
niềm vui|Cảm giác vui vẻ, hạnh phúc trong lòng.
niêu|Nồi nhỏ bằng đất nung, dùng để nấu cơm, kho cá.
nịnh|Khen quá lời để lấy lòng người khác.
nịnh nọt|Khen quá lời, chiều theo ý người khác để lấy lòng.
níu kéo|Cố giữ lại người hoặc điều đang muốn rời xa mình.
no đủ|Có đủ ăn đủ mặc, cuộc sống không thiếu thốn.
no nê|Ăn no đầy đủ, thỏa thích.
nọc độc|Chất độc do rắn, ong, bọ cạp tiết ra để tự vệ hoặc bắt mồi.
nóc nhà|Phần cao nhất của mái nhà; cũng là cách gọi vui người vợ trong gia đình.
nói bừa|Nói không suy nghĩ, không có căn cứ, nghĩ gì nói nấy.
nói chơi|Đùa cho vui bằng lời, không nghiêm túc.
nói chung|Xét chung mọi mặt, không đi vào từng trường hợp.
nói chuyện|Trò chuyện, trao đổi với nhau bằng lời.
nói dối|Cố ý nói sai sự thật để người khác tin.
nói đùa|Bông đùa, nói cho vui chứ không thật lòng.
nói giỡn|Nói đùa cho vui, không có ý nói thật.
nói khoác|Nói phóng đại, khoe khoang quá xa so với sự thật.
nói không|Từ chối dứt khoát, không chấp nhận điều gì.
nói lên|Bày tỏ ra bằng lời; cũng là cho thấy, phản ánh điều gì.
nói năng|Cách dùng lời lẽ khi giao tiếp với người khác.
nói ngọt|Dùng lời dịu dàng, dễ nghe để người khác vui lòng hoặc nghe theo.
nói nhảm|Buông những lời vô nghĩa, không có căn cứ.
nói nhỏ|Hạ thấp giọng, chỉ đủ cho người gần bên nghe.
nói riêng|Xét riêng một phần cụ thể, đối lập với khi nói chung.
nói rõ|Trình bày cụ thể, dễ hiểu để người khác nắm được.
nói suông|Chỉ hứa hẹn bằng lời mà không làm thật.
nói thẳng|Thẳng thắn bày tỏ điều mình nghĩ, không vòng vo.
nói thầm|Thì thào thật khẽ, chỉ người sát bên mới nghe.
noi theo|Làm theo gương tốt của người khác.
nói xấu|Kể điều không hay về người khác sau lưng họ.
nón lá|Nón hình chóp nhọn kết bằng lá, dùng để che nắng che mưa.
non nớt|Còn non trẻ, chưa nhiều kinh nghiệm, chưa chín chắn.
non sông|Núi và sông, thường dùng để chỉ đất nước, quê hương.
nóng|Có nhiệt độ cao; cũng chỉ tính dễ nổi giận.
nóng bỏng|Rất nóng; cũng chỉ vấn đề đang được quan tâm, gay gắt.
nóng bức|Thời tiết nóng và ngột ngạt, gây khó chịu.
nóng bừng|Thấy nóng ran lên đột ngột, thường ở mặt khi ngượng hoặc xúc động.
nóng chảy|Tan thành chất lỏng khi bị đun đến nhiệt độ cao.
nóng giận|Bực tức, dễ mất bình tĩnh trong lúc nhất thời.
nóng hổi|Còn nóng vì vừa nấu xong; cũng chỉ tin tức rất mới.
nóng lòng|Sốt ruột, mong mỏi điều gì đến thật nhanh.
nóng nảy|Dễ nổi cáu, thiếu bình tĩnh khi gặp chuyện không vừa ý.
nòng nọc|Con non của ếch nhái, sống dưới nước, có đuôi.
nóng nực|Trời nóng, oi ả khiến người ta khó chịu.
nóng ruột|Sốt ruột, bồn chồn, lo lắng không yên khi chờ đợi điều gì.
nóng sốt|Còn nóng vì vừa mới làm xong; cũng chỉ tin tức mới, thời sự.
nóng tính|Tính tình dễ cáu gắt, dễ nổi giận.
nóng vội|Muốn làm thật nhanh, thiếu kiên nhẫn và bình tĩnh.
nô đùa|Chơi đùa vui vẻ, chạy nhảy cùng nhau.
nỗ lực|Cố gắng hết sức mình để đạt được điều mong muốn.
nổ máy|Khởi động cho động cơ xe, máy móc bắt đầu chạy.
nổi bật|Dễ thấy, khác hẳn và hơn những cái xung quanh.
nội bộ|Phạm vi bên trong một tổ chức, tập thể, không phải người ngoài.
nổi cáu|Bỗng nhiên bực tức, cáu gắt.
nối dài|Kéo dài thêm bằng cách gắn thêm một đoạn.
nội dung|Những gì được nói, viết hoặc chứa đựng bên trong.
nội địa|Thuộc phạm vi trong nước, không phải nước ngoài.
nối đuôi|Nối tiếp nhau thành hàng dài, cái sau sát cái trước.
nồi hầm|Loại nồi dùng để hầm, ninh thức ăn cho mềm nhừ.
nồi hấp|Loại nồi có ngăn để làm chín thức ăn bằng hơi nước.
nồi hơi|Thiết bị đun nước thành hơi nóng để chạy máy hoặc cấp nhiệt.
nối liền|Gắn liền các phần lại với nhau thành một.
nội ngoại|Họ hàng cả bên cha lẫn bên mẹ.
nỗi niềm|Những tâm tư, tình cảm sâu kín chất chứa trong lòng.
nồi niêu|Nồi, niêu và các đồ dùng để nấu nướng nói chung.
nổi nóng|Mất bình tĩnh, bộc lộ cơn giận ra ngoài.
nội tâm|Thế giới suy nghĩ và cảm xúc bên trong mỗi con người.
nội thành|Khu vực trung tâm bên trong thành phố.
nội thất|Đồ đạc và cách bài trí bên trong ngôi nhà.
nổi tiếng|Được rất nhiều người biết đến và nhắc tới.
nối tiếp|Tiếp theo ngay sau, liên tục không đứt quãng.
nổi trội|Vượt hơn hẳn những người hoặc vật khác.
nội trú|Ăn ở ngay tại trường học hoặc cơ quan, không về nhà hằng ngày.
nôm na|Cách nói hoặc viết giản dị, mộc mạc, dễ hiểu.
nôn nóng|Sốt ruột, muốn việc gì xảy ra ngay.
nồng ấm|Ấm áp và thân thiết, đầy tình cảm.
nông cạn|Không sâu; cũng chỉ suy nghĩ, hiểu biết hời hợt.
nông dân|Người sống bằng nghề làm ruộng, trồng trọt, chăn nuôi.
nồng độ|Lượng một chất có trong dung dịch hoặc hỗn hợp, đậm hay loãng.
nồng nàn|Đậm đà, sâu sắc, thường nói về hương thơm hay tình cảm.
nồng nặc|Mùi bốc lên rất mạnh, thường gây khó chịu.
nông nghiệp|Ngành sản xuất trồng trọt và chăn nuôi.
nồng nhiệt|Sôi nổi, đầy nhiệt tình và chân thành.
nông nổi|Suy nghĩ hời hợt, hành động bồng bột, thiếu chín chắn.
nông sản|Sản phẩm thu được từ trồng trọt, chăn nuôi như lúa gạo, rau, trái cây.
nông thôn|Vùng quê, nơi người dân chủ yếu làm nông nghiệp.
nông trại|Khu đất rộng dùng để trồng trọt, chăn nuôi.
nốt nhạc|Ký hiệu ghi cao độ và trường độ của âm thanh trong bản nhạc.
nốt ruồi|Chấm nhỏ màu nâu hoặc đen trên da.
nở hoa|Nụ bung cánh thành hoa; cũng chỉ sự phát triển tốt đẹp.
nở rộ|Hoa nở nhiều cùng một lúc; cũng chỉ phát triển mạnh, xuất hiện nhiều.
nới lỏng|Làm cho bớt chặt; cũng chỉ giảm bớt quy định, hạn chế.
nụ cười|Vẻ tươi tắn trên môi khi cười.
núi băng|Khối băng khổng lồ trôi nổi trên biển ở vùng lạnh.
núi lửa|Ngọn núi có miệng phun ra dung nham, tro và khí nóng.
núi non|Những dãy núi cao thấp nối tiếp nhau.
núi rừng|Vùng có nhiều núi và rừng cây.
nũng nịu|Làm nũng, nói giọng nhõng nhẽo để được chiều.
nuôi|Cho ăn uống, chăm sóc để người hoặc con vật lớn lên.
nuôi dưỡng|Chăm sóc cho lớn lên; cũng là vun đắp tình cảm, ước mơ.
nuôi nấng|Chăm lo, nuôi dạy con cái cho đến khi khôn lớn.
nuôi sống|Lo cái ăn, cái mặc để ai đó có thể sống.
nuối tiếc|Tiếc mãi điều đã qua hoặc đã bỏ lỡ.
nuôi trồng|Chăn nuôi và trồng trọt, như nuôi tôm cá, trồng rau quả.
nuông chiều|Chiều theo mọi ý thích của ai, thường là quá mức.
nuốt|Đưa thức ăn hay nước uống từ miệng xuống dạ dày.
nuốt chửng|Đưa cả miếng to xuống bụng ngay mà không nhai.
nút áo|Khuy nhỏ dùng để cài hai vạt áo lại với nhau.
nút bấm|Phím nhỏ ấn vào để bật, tắt hoặc điều khiển thiết bị.
nữ giới|Những người thuộc giới tính nữ nói chung.
nữ hoàng|Người phụ nữ làm vua; cũng chỉ người phụ nữ nổi bật nhất một lĩnh vực.
nữ sinh|Học sinh hoặc sinh viên là con gái.
nữ thần|Vị thần là nữ trong truyền thuyết; cũng chỉ cô gái rất xinh đẹp.
nữ tính|Vẻ dịu dàng, mềm mại thường thấy ở phụ nữ.
nữ trang|Đồ trang sức của phụ nữ như nhẫn, dây chuyền, bông tai.
nửa chừng|Đang ở giữa quá trình, việc làm còn dở dang chưa xong.
nửa đêm|Khoảng giữa đêm, vào lúc gần mười hai giờ khuya.
nửa đường|Khoảng giữa quãng đường đi; cũng chỉ việc đang làm dở chưa xong.
nửa ngày|Một nửa của ngày, tức buổi sáng hoặc buổi chiều.
nửa vời|Làm không đến nơi đến chốn, thiếu triệt để.
nực cười|Đáng buồn cười vì kỳ quặc hoặc vô lý.
nước|Chất lỏng trong suốt, không màu, cần cho sự sống; cũng chỉ một quốc gia.
nước cam|Đồ uống vắt hoặc ép từ quả cam tươi.
nước canh|Phần nước trong bát canh, thường dùng để chan cơm.
nước cất|Loại nước rất tinh khiết, thu được bằng cách đun sôi rồi ngưng tụ hơi.
nước chanh|Đồ uống pha từ nước cốt chanh với đường và nước.
nước chấm|Loại nước pha sẵn để chấm thức ăn, như nước mắm, xì dầu.
nước cốt|Phần nước đặc vắt lần đầu từ nguyên liệu, như cốt dừa, cốt chanh.
nước cờ|Một lần đi quân khi chơi cờ; cũng chỉ một bước tính toán khôn khéo.
nước dùng|Phần nước ninh từ xương, thịt để chan vào phở, bún, miến.
nước dừa|Phần nước ngọt mát chứa trong quả dừa.
nước đá|Những khối nước đông cứng vì lạnh, dùng để làm mát đồ uống.
nước ép|Thức uống làm bằng cách ép trái cây hoặc rau lấy nước.
nước hoa|Chất lỏng có mùi thơm, xịt lên người hoặc quần áo.
nước khoáng|Loại nước tự nhiên chứa nhiều chất khoáng, thường đóng chai để uống.
nước lã|Nước tự nhiên chưa đun sôi, chưa pha thêm gì.
nước lạnh|Loại nước có nhiệt độ thấp, không được đun nóng.
nước lọc|Loại nước sạch đã đun sôi để nguội hoặc đã qua lọc, dùng để uống.
nước máy|Nguồn nước sạch do nhà máy xử lý, dẫn theo đường ống đến từng nhà.
nước mắm|Nước chấm làm từ cá ủ muối, vị mặn đậm, dùng để nêm và chấm.
nước mặn|Loại nước có vị mặn, như nước biển.
nước mắt|Chất lỏng chảy ra từ mắt khi khóc hoặc bị cay mắt.
nước mưa|Lượng nước từ trên trời rơi xuống khi có mưa.
nước ngầm|Nguồn nước tích tụ trong các lớp đất đá dưới lòng đất.
nước ngoài|Quốc gia khác, không phải nước mình.
nước ngọt|Loại nước không mặn như ở sông, hồ; cũng chỉ đồ uống có ga, vị ngọt.
nước nôi|Nước uống và nước dùng nói chung trong sinh hoạt hằng ngày.
nước rút|Giai đoạn cuối cần tăng tốc; cũng chỉ lúc nước lũ rút xuống.
nước sạch|Loại nước không bị ô nhiễm, an toàn để ăn uống, sinh hoạt.
nước trà|Thức uống pha từ lá trà, vị chát nhẹ, thơm.
nướng|Làm chín thức ăn bằng cách để gần lửa hoặc than nóng.
nứt nẻ|Có nhiều vết nứt nhỏ, như đất khô hay da bị khô.
oải hương|Cây hoa nhỏ màu tím, rất thơm, dùng làm tinh dầu.
oi bức|Nóng nực, ngột ngạt, không có gió.
om sòm|Ồn ào, ầm ĩ, làm người xung quanh khó chịu.
óng ánh|Sáng lấp lánh, phản chiếu ánh sáng rất đẹp mắt.
ong bướm|Ong và bướm; nghĩa bóng chỉ chuyện yêu đương lả lơi, không nghiêm túc.
ong chúa|Con ong cái lớn nhất trong tổ, chuyên đẻ trứng.
ong mật|Loài ong được nuôi để lấy mật.
ong thợ|Những con ong làm nhiệm vụ kiếm mật, xây tổ và chăm ong non.
ong vàng|Loài ong thân màu vàng có sọc đen, thường làm tổ trên cây.
ọp ẹp|Cũ kỹ, lỏng lẻo, lung lay, không còn chắc chắn.
ổ cắm|Thiết bị gắn trên tường hay dây điện để cắm phích lấy điện.
ô liu|Loại quả nhỏ màu xanh hoặc đen, dùng ép dầu hoặc ngâm để ăn.
ô long|Loại trà lên men một phần, hương thơm, vị đậm đà.
ô mai|Món ăn vặt làm từ quả mơ, mận, sấu tẩm đường, gừng, muối.
ô nhiễm|Môi trường bị làm bẩn bởi rác thải, khói bụi, hóa chất.
ô vuông|Hình vuông nhỏ, như các ô trên giấy kẻ hoặc bàn cờ.
ốc đảo|Vùng có nước và cây xanh giữa sa mạc.
ốc sên|Con vật nhỏ có vỏ xoắn trên lưng, bò rất chậm.
ôi chao|Tiếng thốt lên khi ngạc nhiên, xúc động hoặc thán phục.
ôm ấp|Giữ chặt trong vòng tay một cách trìu mến; cũng chỉ nuôi giữ mơ ước trong lòng.
ôm đồm|Nhận làm quá nhiều việc cùng lúc, đến mức khó làm tốt.
ôm hôn|Vòng tay ôm và hôn để bày tỏ tình yêu thương.
ồn ào|Có nhiều tiếng động lớn, gây mất yên tĩnh.
ổn áp|Thiết bị giữ cho điện áp ổn định; cũng là cách nói vui nghĩa là ổn, được.
ổn định|Giữ được trạng thái vững vàng, ít thay đổi hay xáo trộn.
ôn luyện|Học lại kiến thức cũ và làm bài luyện tập để chuẩn bị thi.
ôn tập|Học lại những gì đã học để nhớ lâu và hiểu sâu hơn.
ôn thi|Học lại bài cũ để chuẩn bị cho kỳ thi.
ông bà|Cha mẹ của bố hoặc mẹ mình; cũng chỉ tổ tiên nói chung.
ông bầu|Người đứng ra quản lý, đầu tư cho ca sĩ, đội bóng hay đoàn nghệ thuật.
ông cha|Những thế hệ đi trước, tổ tiên của mình.
ống chân|Phần chân phía trước, từ đầu gối xuống đến cổ chân.
ống chỉ|Lõi tròn nhỏ dùng để quấn sợi chỉ may.
ông cụ|Cách gọi kính trọng dành cho người đàn ông lớn tuổi.
ống dẫn|Đường ống dùng để đưa nước, khí hay chất lỏng đi nơi khác.
ông già|Người đàn ông lớn tuổi; cũng là cách gọi thân mật người cha.
ống hút|Que nhỏ, rỗng ruột, dùng để hút nước uống từ cốc, chai.
ống khói|Trụ rỗng cao dẫn khói từ bếp lò hay nhà máy thoát lên trời.
ống kính|Bộ phận có thấu kính của máy ảnh, máy quay để thu hình.
ông lão|Người đàn ông tuổi đã cao, hay gặp trong truyện kể.
ống nghe|Dụng cụ bác sĩ dùng để nghe tiếng tim, phổi; cũng là phần nghe của điện thoại bàn.
ống nghiệm|Lọ thủy tinh nhỏ, dài, dùng đựng hóa chất trong phòng thí nghiệm.
ông ngoại|Người cha của mẹ mình.
ống nhòm|Dụng cụ có hai ống kính để nhìn rõ vật ở xa.
ông nội|Người cha của bố mình.
ống quần|Phần hình ống của chiếc quần, bao quanh mỗi bên chân.
ống sáo|Nhạc cụ hình ống có khoét lỗ, thổi hơi vào để tạo ra tiếng.
ống tay|Phần của áo bao quanh cánh tay, còn gọi là tay áo.
ông xã|Cách vợ gọi chồng một cách thân mật.
ở lại|Tiếp tục ở chỗ cũ, không rời đi.
ở riêng|Ra sống tách khỏi gia đình bố mẹ, tự lo nhà cửa.
ở trọ|Thuê phòng ở tạm tại nhà người khác, thường trả tiền theo tháng.
ớt bột|Gia vị làm từ ớt khô xay nhỏ, có màu đỏ và vị cay.
ớt ngọt|Loại ớt quả to, không cay, có nhiều màu, ăn như rau.
phá bĩnh|Cố ý gây rối, làm hỏng việc hay cuộc vui của người khác.
phá bỏ|Dỡ đi hoặc loại bỏ hẳn cái cũ, cái gây cản trở.
phá cách|Làm khác đi, không theo khuôn mẫu quen thuộc để tạo nét riêng.
pha chế|Trộn các nguyên liệu theo công thức để làm đồ uống hoặc thuốc.
phá của|Làm hư hỏng đồ đạc hoặc tiêu xài phung phí tiền của.
phá đám|Cố ý làm hỏng cuộc vui hay việc của người khác.
phá hỏng|Làm cho đồ vật hay công việc bị hư, không dùng được nữa.
pha lê|Loại thủy tinh cao cấp, trong suốt, lấp lánh, dùng làm đồ trang trí.
pha loãng|Thêm nước hoặc chất lỏng để làm cho bớt đặc.
pha trò|Nói hoặc làm điều buồn cười để mọi người vui.
pha trộn|Trộn lẫn nhiều thứ khác nhau với nhau.
phá vỡ|Làm vỡ tan ra; cũng chỉ vượt qua kỷ lục hay làm mất sự yên ổn.
phác thảo|Vẽ hoặc viết sơ qua những nét chính trước khi làm kỹ.
phải|Đúng, không sai; cũng chỉ phía ngược với bên trái, hoặc việc bắt buộc làm.
phải chăng|Vừa phải, hợp lý về giá cả; cũng dùng để hỏi khi phỏng đoán điều gì.
phái đẹp|Cách gọi thân mật, mang ý khen, chỉ phụ nữ nói chung.
phải lòng|Đem lòng yêu thích, say mê một người.
phai màu|Màu sắc nhạt dần đi, không còn tươi như lúc đầu.
phai mờ|Mờ dần, không còn rõ nét; cũng chỉ ký ức dần bị quên.
phai nhạt|Mờ dần, nhạt dần theo thời gian, như màu sắc hay tình cảm.
phải rồi|Câu đáp đồng ý, xác nhận điều vừa nói là đúng.
phải trái|Điều đúng và điều sai, lẽ phải nói chung.
phạm lỗi|Làm sai quy định, luật chơi, nhất là trong thi đấu thể thao.
phản bác|Đưa ra lý lẽ để bác bỏ ý kiến của người khác.
phản cảm|Gây cảm giác khó chịu, không ưa cho người khác.
phản chiếu|Hắt lại ánh sáng hoặc hình ảnh, như mặt gương, mặt nước.
phản diện|Nhân vật xấu, đối lập với nhân vật chính trong truyện, phim.
phán đoán|Dựa vào điều đã biết để đoán và nhận định sự việc.
phản đối|Không đồng ý và lên tiếng hay hành động chống lại.
phản hồi|Đáp lại, trả lời hoặc góp ý về điều đã nhận được.
phản lực|Lực đẩy ngược chiều do khí phụt mạnh ra sau, giúp máy bay bay nhanh.
phàn nàn|Nói ra sự không hài lòng, kêu ca về điều gì đó.
phản ứng|Cách đáp lại khi gặp việc gì; cũng chỉ sự biến đổi hóa học.
phản xạ|Phản ứng tự động, nhanh của cơ thể; cũng chỉ ánh sáng, âm thanh dội lại.
phán xét|Đánh giá, kết luận ai đó đúng hay sai, tốt hay xấu.
phanh|Bộ phận giúp xe chạy chậm lại hoặc dừng hẳn.
phanh phui|Làm lộ ra cho mọi người biết điều sai trái đang bị che giấu.
phao|Vật nổi giúp người không bị chìm; cũng chỉ tài liệu mang lén vào phòng thi.
pháo bông|Pháo khi đốt tỏa tia sáng nhiều màu như bông hoa, dùng trong dịp lễ.
phao câu|Phần thịt nhô lên ở cuối mình gà, vịt, nơi mọc lông đuôi.
pháo hoa|Pháo bắn lên trời nổ thành chùm sáng rực rỡ vào dịp lễ, Tết.
phát|Trao, chia cho từng người; cũng chỉ truyền âm thanh, hình ảnh qua sóng.
phát âm|Cách đọc, nói thành tiếng các âm và các từ.
phát biểu|Nói lên ý kiến, suy nghĩ của mình trước nhiều người.
phát bóng|Đưa bóng vào cuộc để bắt đầu hay tiếp tục lượt chơi trong trận đấu.
phát đạt|Làm ăn ngày càng thịnh vượng, thu được nhiều lợi nhuận.
phạt đền|Quả sút phạt từ chấm mười một mét vào khung thành trong bóng đá.
phát điện|Tạo ra dòng điện bằng máy phát hoặc nhà máy điện.
phạt góc|Cú đá bóng từ góc sân khi đội phòng ngự để bóng ra đường biên ngang.
phát hành|Đưa sách báo, phim, bài hát hoặc tiền ra lưu hành rộng rãi.
phát hiện|Tìm ra, nhận ra điều chưa ai biết hoặc đang bị che giấu.
phát huy|Làm cho điều hay, điều tốt sẵn có mạnh hơn và có ích hơn.
phát minh|Tìm ra hoặc tạo ra điều mới có giá trị, trước đó chưa ai biết.
phát sáng|Tự tỏa ra ánh sáng, như đom đóm hay bóng đèn.
phát sinh|Nảy ra, xuất hiện thêm điều trước đó chưa có.
phát sóng|Truyền chương trình ti vi, đài qua sóng để mọi người xem và nghe.
phát tài|Làm ăn gặp may, kiếm được nhiều tiền của.
phát thanh|Truyền tin tức, âm nhạc qua sóng đài để mọi người nghe.
phát triển|Lớn lên, mở rộng hoặc tiến bộ dần theo hướng tốt hơn.
phẳng|Bề mặt bằng, không lồi lõm, không gồ ghề.
phẳng lặng|Yên ả, êm đềm, không xáo trộn, như mặt hồ không gợn sóng.
phẳng phiu|Thẳng thớm, không một nếp nhăn, như quần áo vừa được là kỹ.
phẩm chất|Những đức tính tốt bên trong con người; cũng chỉ chất lượng của hàng hóa.
phấn|Thỏi dùng để viết bảng; cũng chỉ bột mịn thoa lên da khi trang điểm.
phân biệt|Nhận ra chỗ khác nhau giữa các thứ; cũng chỉ đối xử không công bằng.
phân bón|Chất bón vào đất giúp cây trồng lớn nhanh, tốt hơn.
phân bố|Rải ra hoặc có mặt ở nhiều nơi khác nhau, như dân cư, cây cối.
phân cách|Ngăn ra, tách riêng thành từng bên hay từng phần.
phấn chấn|Tinh thần lên cao, thấy hăng hái, đầy sức sống.
phân chia|Chia ra thành nhiều phần hoặc chia cho nhiều người.
phân công|Giao cho mỗi người một phần việc cụ thể.
phần cứng|Các bộ phận có thể sờ thấy của máy tính, như màn hình, bàn phím.
phấn đấu|Cố gắng hết sức để đạt được mục tiêu.
phần đông|Số đông người, đa số trong một tập thể.
phấn hoa|Bột nhỏ li ti trong nhị hoa, giúp cây kết hạt.
phấn khích|Hào hứng, kích động mạnh vì điều gì đó thú vị.
phấn khởi|Vui mừng, hào hứng vì có điều tốt đẹp xảy ra.
phân loại|Xếp các thứ thành từng nhóm theo đặc điểm giống nhau.
phần lớn|Phần chiếm hơn một nửa của toàn bộ.
phân luồng|Chia dòng xe cộ hoặc người đi theo các hướng khác nhau cho khỏi tắc.
phấn màu|Phấn có nhiều màu, dùng để vẽ hoặc viết bảng.
phần mềm|Các chương trình chạy trên máy tính, điện thoại.
phần nào|Một phần, ở mức độ nhất định chứ không hoàn toàn.
phần nhiều|Hầu hết, đa số trong những người hay vật được nói tới.
phân nửa|Khoảng một nửa của tổng số hay của toàn bộ.
phân phát|Chia và trao tận tay cho từng người, như quà hay tài liệu.
phân phối|Chia và đưa hàng hóa, của cải đến những nơi cần dùng.
phấn rôm|Bột mịn, thơm, xoa lên da cho khô thoáng, hay dùng cho trẻ em.
phân số|Số viết dưới dạng tử số trên mẫu số, như một phần hai.
phân tách|Chia một thứ ra thành từng phần riêng biệt.
phân tán|Tản ra nhiều nơi, không tập trung một chỗ.
phân tâm|Không tập trung được vì bị điều khác làm chú ý.
phần thưởng|Thứ được trao để khen người có thành tích tốt.
phân tích|Xem xét kỹ từng phần để hiểu rõ bản chất sự việc.
phần trăm|Đơn vị chỉ tỉ lệ so với một trăm phần, ký hiệu %.
phân tử|Hạt nhỏ nhất của một chất, gồm các nguyên tử liên kết với nhau.
phân vân|Chưa quyết được vì còn băn khoăn giữa nhiều lựa chọn.
phân vùng|Chia một khu vực hay ổ đĩa máy tính thành nhiều vùng riêng.
phật ý|Không vừa lòng, hơi giận vì lời nói, việc làm của người khác.
phẩy|Dấu câu nhỏ dùng để ngắt ý trong câu; cũng dùng để tách phần thập phân.
phép|Sự đồng ý cho ai làm việc gì, như được nghỉ; cũng chỉ phép màu.
phép chia|Cách tính tìm xem số này chứa bao nhiêu lần số kia.
phép cộng|Cách tính gộp các số lại với nhau để ra tổng.
phép đo|Việc dùng dụng cụ để xác định độ dài, khối lượng hay nhiệt độ.
phép nhân|Cách tính cộng lặp lại một số nhiều lần để ra tích.
phép tắc|Những quy định, lễ nghi mà mọi người cần tuân theo.
phép thuật|Khả năng làm những điều kỳ diệu như trong truyện cổ tích.
phép tính|Việc tính toán với các con số để tìm ra kết quả.
phép toán|Thao tác tính trên các số, như cộng, trừ, nhân, chia.
phép trừ|Phép tính lấy một số bớt đi một số khác.
phê bình|Chỉ ra cái sai để góp ý sửa chữa; cũng chỉ nhận xét về tác phẩm.
phê duyệt|Người có thẩm quyền xem xét và đồng ý cho thực hiện.
phế liệu|Đồ cũ, vật liệu bỏ đi có thể thu gom để tái chế.
phê phán|Chỉ ra và chê trách cái sai, cái xấu.
phết|Quét một lớp mỏng lên bề mặt; trong khẩu ngữ còn có nghĩa là khá, lắm.
phễu|Dụng cụ miệng loe rộng, đáy có ống nhỏ, dùng để rót chất lỏng.
phi công|Người được đào tạo để điều khiển máy bay.
phi cơ|Tên gọi khác của máy bay, phương tiện bay trên bầu trời.
phí của|Dùng của cải một cách lãng phí, không đáng.
phi lao|Cây thân gỗ cao, lá nhỏ như kim, hay trồng ven biển để chắn gió cát.
phi ngựa|Cưỡi ngựa cho chạy thật nhanh.
phí phạm|Dùng tiền bạc, thời gian, đồ đạc vào việc không đáng, gây lãng phí.
phi thuyền|Con tàu dùng để bay vào không gian vũ trụ.
phi thường|Vượt xa mức bình thường, rất đặc biệt.
phía|Một bên hay một hướng so với vị trí nào đó.
phiền|Làm mất thời gian, gây bất tiện cho người khác; cũng là buồn lòng.
phiên âm|Ghi lại cách đọc của từ ngữ bằng chữ cái hoặc ký hiệu.
phiên bản|Một bản của sản phẩm hay phần mềm, có điểm khác so với bản trước.
phiên dịch|Chuyển lời nói từ ngôn ngữ này sang ngôn ngữ khác.
phiền hà|Gây rắc rối, mất thời gian và tốn công sức.
phiền lòng|Cảm thấy buồn hoặc không vui trong lòng vì chuyện gì đó.
phiền phức|Rắc rối, gây nhiều bất tiện.
phiền toái|Rắc rối, gây khó chịu, bực mình.
phiếu|Tờ giấy nhỏ ghi thông tin, dùng để nhận hàng, mua hàng hoặc bầu chọn.
phiêu lưu|Đi đến những nơi xa lạ, trải qua nhiều điều mạo hiểm, thú vị.
phim|Tác phẩm gồm hình ảnh động và âm thanh, chiếu trên màn ảnh.
phim ảnh|Các bộ phim và nghệ thuật điện ảnh nói chung.
phim trường|Nơi dựng cảnh để quay phim.
phin|Dụng cụ nhỏ có lỗ lọc, dùng để pha cà phê nhỏ giọt.
phó phòng|Người giữ chức vụ phụ tá, đứng sau trưởng phòng trong cơ quan.
phòng|Khoảng ngăn riêng trong nhà; cũng chỉ việc lo trước để tránh điều xấu.
phòng ăn|Phòng kê bàn ghế dùng để ăn uống.
phong bì|Bao giấy dùng để đựng thư; cũng chỉ tiền mừng bỏ trong đó.
phong cách|Cách ăn mặc, nói năng, làm việc mang nét riêng của mỗi người.
phong cảnh|Cảnh vật thiên nhiên như núi, sông, đồng ruộng bày ra trước mắt.
phòng chờ|Nơi có ghế cho hành khách ngồi đợi, như ở sân bay, nhà ga.
phóng đại|Làm cho hình ảnh to hơn thật; cũng chỉ nói quá sự thật.
phỏng đoán|Đoán dựa trên vài dấu hiệu, chưa chắc chắn.
phong độ|Vẻ ngoài đĩnh đạc, lịch lãm; cũng chỉ mức thi đấu, làm việc gần đây.
phòng đợi|Phòng có chỗ ngồi để mọi người chờ đến lượt mình.
phòng học|Căn phòng dùng để dạy và học.
phòng họp|Căn phòng dành cho việc gặp gỡ, bàn bạc công việc.
phòng khách|Phòng để tiếp khách và cả nhà ngồi chơi, trò chuyện.
phòng khi|Để sẵn sàng nếu có chuyện bất ngờ xảy ra.
phóng khoáng|Tính tình rộng rãi, thoải mái, không câu nệ.
phong lan|Loài lan sống bám trên thân cây, hoa đẹp, thường được treo làm cảnh.
phòng ngủ|Phòng có giường để ngủ và nghỉ ngơi.
phòng ngừa|Làm trước để ngăn điều xấu không xảy ra.
phòng ốc|Các phòng, buồng trong nhà hay cơ quan nói chung.
phong phú|Nhiều và đa dạng, có đủ các loại khác nhau.
phóng sự|Bài báo hay chương trình ghi lại chân thực một sự việc có thật.
phòng thân|Chuẩn bị sẵn để tự lo cho mình khi gặp khó khăn, nguy hiểm.
phong thư|Bì giấy đựng lá thư để gửi đi.
phòng tối|Phòng kín không lọt ánh sáng, dùng để tráng rửa phim ảnh.
phòng trà|Nơi khách vừa uống nước vừa nghe ca sĩ hát nhạc sống.
phong trào|Hoạt động được nhiều người cùng hưởng ứng, tham gia rộng rãi.
phong tục|Thói quen, nếp sống lâu đời được cộng đồng gìn giữ.
phỏng vấn|Hỏi chuyện ai đó để lấy thông tin, đưa tin hoặc tuyển chọn.
phóng viên|Người đi tìm hiểu, thu thập tin tức để viết bài cho báo, đài.
phóng xe|Cho xe chạy thật nhanh trên đường.
phổ biến|Có ở nhiều nơi, nhiều người biết; cũng chỉ truyền đạt cho mọi người.
phố phường|Phố xá đông đúc, nhộn nhịp ở thành thị.
phổ quát|Chung cho tất cả, đúng với mọi nơi, mọi người.
phổ thông|Thông dụng, ai cũng biết; cũng chỉ bậc học từ lớp 1 đến lớp 12.
phô trương|Cố ý bày ra cho người khác thấy để khoe khoang.
phố xá|Đường phố cùng nhà cửa, cửa hàng ở thành thị nói chung.
phổi|Cơ quan trong lồng ngực giúp cơ thể hít thở.
phối hợp|Cùng nhau làm, kết hợp nhịp nhàng để đạt mục đích chung.
phối màu|Kết hợp các màu với nhau sao cho hài hòa, đẹp mắt.
phồng tôm|Bánh mỏng làm từ bột trộn tôm, rán lên thì phồng to và giòn.
phờ phạc|Mệt mỏi đến mức mặt mày hốc hác, trông bơ phờ.
phơi bày|Để lộ rõ cho mọi người thấy điều vốn bị che giấu.
phơi nắng|Để ra ngoài nắng cho khô hoặc cho ấm.
phớt lờ|Cố tình làm như không nghe, không thấy.
phụ bếp|Người giúp việc cho đầu bếp trong nhà hàng, quán ăn.
phù dâu|Cô gái đi cạnh, giúp đỡ cô dâu trong lễ cưới.
phụ đạo|Dạy thêm, kèm thêm cho học sinh ngoài giờ học chính.
phụ đề|Dòng chữ hiện trên màn hình, ghi lời thoại của phim.
phụ gia|Chất thêm vào thực phẩm hoặc vật liệu để cải thiện chất lượng.
phụ giúp|Giúp đỡ thêm một phần công việc cho người khác.
phù hiệu|Dấu hiệu nhỏ may hoặc đeo trên áo để cho biết trường, đơn vị.
phù hợp|Vừa vặn, hợp với yêu cầu hay hoàn cảnh.
phụ huynh|Cha mẹ hoặc người nuôi dạy học sinh.
phụ kiện|Đồ đi kèm hay trang trí thêm, như ốp điện thoại, túi, vòng tay.
phụ lòng|Làm cho người đã tin tưởng, giúp đỡ mình phải thất vọng.
phu nhân|Cách gọi trang trọng vợ của người có địa vị, chức vụ.
phụ nữ|Người thuộc giới nữ đã trưởng thành.
phũ phàng|Lạnh lùng, tàn nhẫn, không chút nể nang tình cảm.
phụ phí|Khoản tiền phải trả thêm ngoài giá chính.
phù rể|Chàng trai đi cạnh, giúp đỡ chú rể trong lễ cưới.
phù sa|Đất cát mịn do nước sông chở theo, bồi đắp cho ruộng bãi màu mỡ.
phủ sóng|Sóng điện thoại, truyền hình truyền tới và dùng được ở một vùng.
phụ tá|Người giúp việc, hỗ trợ cho người phụ trách chính.
phụ thuộc|Dựa vào hay chịu chi phối bởi người, vật khác, không tự chủ.
phụ trách|Chịu trách nhiệm trông coi, điều hành một việc.
phụ trợ|Có tác dụng giúp thêm, hỗ trợ cho phần chính.
phụ tùng|Các bộ phận rời để thay thế, lắp ráp cho máy móc, xe cộ.
phúc|Điều may mắn, tốt lành mà con người có được.
phục cổ|Làm theo kiểu xưa hoặc làm cho đồ cũ trở lại như xưa.
phục hồi|Làm cho trở lại trạng thái tốt như trước.
phúc lợi|Những quyền lợi, chế độ tốt mà người lao động được hưởng.
phục tùng|Chịu nghe theo, làm theo mệnh lệnh của người khác.
phục vụ|Làm việc để đáp ứng nhu cầu của người khác, như bưng bê cho khách.
phủi|Dùng tay hay khăn gạt nhẹ cho sạch bụi.
phun|Đẩy chất lỏng hay hơi bắn mạnh ra thành tia hoặc hạt nhỏ.
phun trào|Núi lửa đẩy mạnh dung nham, tro bụi từ lòng đất ra ngoài.
phung phí|Tiêu xài tiền bạc, của cải bừa bãi, không biết tiết kiệm.
phút|Đơn vị đo thời gian, bằng sáu mươi giây.
phút giây|Khoảnh khắc ngắn ngủi, thường gắn với kỷ niệm đáng nhớ.
phức hợp|Gồm nhiều phần khác nhau gộp lại thành một tổng thể.
phức tạp|Gồm nhiều phần, rắc rối, khó hiểu hay khó giải quyết.
phượng|Cây cao, hoa đỏ rực nở vào mùa hè, gắn với tuổi học trò.
phương án|Cách làm, kế hoạch được đưa ra để giải quyết một việc.
phương châm|Nguyên tắc chính định hướng cho cách sống, cách làm việc.
phương đông|Hướng mặt trời mọc; cũng chỉ các nước châu Á nói chung.
phượng hoàng|Loài chim quý trong truyền thuyết, tượng trưng cho điều tốt lành.
phương hướng|Hướng đông, tây, nam, bắc; cũng chỉ mục tiêu và cách làm.
phương pháp|Cách làm có trình tự để đạt được mục đích.
phương thức|Cách thức, hình thức tiến hành một việc, như cách thanh toán.
phương tiện|Cái dùng để làm một việc, nhất là xe cộ để đi lại.
phương trình|Đẳng thức toán học có ẩn số cần tìm giá trị.
piano|Đàn dương cầm, có hàng phím trắng đen, chơi bằng cách bấm phím.
quà bánh|Bánh kẹo và các món ăn vặt nói chung.
quà biếu|Món quà đem tặng để tỏ lòng quý mến hoặc biết ơn.
quả bóng|Vật hình tròn, thường bơm hơi, dùng để chơi thể thao.
quà cáp|Quà biếu, quà tặng nói chung.
quả cân|Khối kim loại có khối lượng chuẩn, đặt lên cân để đo.
quả chuông|Vật bằng kim loại hình loa úp, gõ hay lắc vào thì kêu ngân vang.
quả dâu|Quả mọng nhỏ màu đỏ hoặc tím, vị chua ngọt, như dâu tây, dâu tằm.
quá đà|Không kìm lại kịp nên vượt quá mức hợp lý.
quá đáng|Vượt quá mức hợp lý, khiến người khác phật lòng.
quả đất|Trái Đất, hành tinh nơi con người sinh sống.
qua đường|Đi băng sang bên kia đường; cũng chỉ người tình cờ đi ngang qua.
quá giờ|Đã vượt qua thời gian quy định.
quá hạn|Đã vượt quá thời hạn được quy định hoặc cho phép.
quả khô|Trái cây đã phơi hoặc sấy khô để ăn dần.
quá khứ|Thời gian đã qua và những chuyện đã xảy ra.
quả là|Dùng để khẳng định điều gì đúng thật như thế.
qua lại|Đi đi về về nhiều lần; cũng chỉ sự giao thiệp, thăm hỏi nhau.
quả lắc|Bộ phận đung đưa qua lại đều đặn trong đồng hồ treo tường.
quá lắm|Vượt quá mức chấp nhận được, khiến người khác khó chịu.
qua loa|Làm sơ sài, đại khái, không cẩn thận.
qua mặt|Vượt lên trước người khác; cũng chỉ giấu giếm, đánh lừa ai đó.
quá mức|Vượt quá giới hạn, mức độ thông thường.
quá sức|Vượt quá sức lực, khả năng của mình.
quả tạ|Khối kim loại nặng dùng để tập thể lực hay thi cử tạ.
quá tải|Vượt quá sức chứa hoặc khả năng chịu đựng cho phép.
quá tay|Lỡ làm mạnh hơn hay cho nhiều hơn mức cần thiết.
quả thật|Dùng để nhấn mạnh rằng điều vừa nói là đúng sự thật.
quả thực|Từ dùng để xác nhận điều nói ra hoàn toàn có thật.
quả tim|Bộ phận trong ngực bơm máu đi khắp cơ thể; cũng tượng trưng cho tình yêu.
quá trình|Chuỗi diễn biến, các bước của sự việc theo thời gian.
quá trớn|Đùa giỡn hay hành động vượt quá giới hạn cho phép.
quai|Phần để cầm, xách hay đeo của đồ vật như túi, giỏ, dép.
quái đản|Kỳ quặc, quái gở, khác người một cách khó hiểu.
quai hàm|Phần xương hàm ở hai bên má, cử động khi nhai, nói.
quái lạ|Rất lạ, khác thường đến mức khó hiểu.
quai nón|Dây đeo của chiếc nón, vòng qua cằm để giữ nón.
quái vật|Con vật kỳ dị, to lớn, đáng sợ trong truyện, phim.
quán ăn|Cửa hàng bán đồ ăn cho khách ngồi ăn tại chỗ.
quan điểm|Ý kiến, cách nhìn của một người khi xem xét vấn đề.
quan hệ|Sự liên quan, gắn bó giữa người với người hay giữa các sự vật.
quan họ|Lối hát dân ca đối đáp giữa nam và nữ của vùng Kinh Bắc.
quan niệm|Cách nhìn nhận, hiểu về một vấn đề, thường đã thành nếp nghĩ.
quán nước|Quán nhỏ bán nước uống và đồ ăn vặt.
quán quân|Người hoặc đội giành giải nhất trong cuộc thi.
quan sát|Nhìn kỹ để theo dõi và tìm hiểu sự vật.
quan tâm|Để ý, lo lắng, chăm sóc đến ai hoặc việc gì.
quản trị|Điều hành, quản lý công việc của một tổ chức, hệ thống.
quán trọ|Nhà cho khách đi đường thuê ở tạm, nghỉ qua đêm.
quan trọng|Có ý nghĩa, ảnh hưởng lớn, không thể xem nhẹ.
quán xá|Các quán hàng nói chung, như quán ăn, quán nước.
quảng bá|Giới thiệu rộng rãi về một nơi, sản phẩm hay hình ảnh để nhiều người biết.
quang cảnh|Toàn bộ cảnh vật, cảnh tượng bày ra trước mắt ở một nơi.
quảng cáo|Giới thiệu sản phẩm, dịch vụ để thu hút người mua.
quang đãng|Trời trong xanh, sáng sủa, thoáng mát, không có mây mù.
quang học|Ngành vật lý nghiên cứu ánh sáng và các hiện tượng liên quan.
quảng trường|Khoảng đất rộng ở thành phố để mọi người tụ họp, dạo chơi.
quanh|Ở vòng ngoài, bao xung quanh một vật hay một nơi.
quanh co|Uốn lượn vòng vèo, không thẳng; cũng chỉ nói vòng vo, không thật lòng.
quanh năm|Suốt cả năm, lúc nào cũng vậy.
quanh quẩn|Đi lại loanh quanh trong một phạm vi hẹp.
quạt|Đồ dùng tạo ra gió cho mát, như quạt tay, quạt điện.
quạt bàn|Quạt điện nhỏ, đặt trên bàn để làm mát.
quạt điện|Quạt chạy bằng điện, có thể để bàn, đứng hoặc treo tường.
quạt giấy|Quạt cầm tay làm bằng giấy dán trên nan, có thể xếp gọn.
quạt gió|Thiết bị tạo luồng gió để làm mát hay thông hơi.
quạt máy|Cách gọi quạt điện ở miền Nam, có cánh quay nhờ động cơ.
quát mắng|Lớn tiếng la rầy, trách móc ai đó.
quát tháo|La mắng ầm ĩ, to tiếng với người khác.
quạt trần|Quạt gắn trên trần nhà, cánh dài quay tạo gió mát.
quay cuồng|Quay tít, đảo lộn liên tục; cũng chỉ bận rộn đến rối tung.
quay đi|Xoay người hoặc mặt sang hướng khác.
quay lại|Trở về chỗ cũ hoặc xoay người nhìn ra phía sau.
quay lưng|Xoay lưng lại phía ai; cũng chỉ bỏ mặc, không đoái hoài nữa.
quay phải|Xoay người hoặc rẽ sang phía bên tay phải.
quay phim|Ghi lại hình ảnh chuyển động bằng máy quay.
quay vòng|Xoay tròn thành vòng; cũng chỉ luân phiên, lần lượt lặp lại.
quăng|Vung tay ném mạnh một vật ra xa.
quần|Đồ mặc che phần dưới cơ thể, có hai ống chân.
quần áo|Đồ mặc trên người nói chung.
quần bò|Quần may bằng vải bò dày, thường màu xanh.
quân cờ|Từng con cờ dùng để đi trong một ván cờ.
quần đảo|Nhóm nhiều đảo nằm gần nhau trên biển.
quần đùi|Quần ngắn trên đầu gối, mặc ở nhà hay khi chơi thể thao.
quẩn quanh|Đi lại loanh quanh một chỗ, mãi không thoát ra được.
quần quật|Làm việc vất vả liên tục, không lúc nào ngơi tay.
quấn quýt|Luôn gắn bó, quây quần bên nhau, không muốn rời xa.
quần tây|Quần âu ống dài, kiểu dáng lịch sự, thường mặc đi làm, đi học.
quân tử|Người có nhân cách cao thượng, sống đàng hoàng, đáng kính.
quần vợt|Môn thể thao dùng vợt đánh bóng qua lưới.
quầy|Bàn dài để bày bán hàng hoặc tiếp khách, như chỗ thu ngân.
quây quần|Tụ họp đông đủ, gần gũi bên nhau, như cả nhà sum họp.
quấy rầy|Làm phiền khiến người khác không được yên.
que diêm|Que gỗ nhỏ có đầu thuốc, quẹt vào vỏ hộp để tạo lửa.
quen biết|Đã gặp và biết nhau từ trước.
quen mặt|Đã gặp nhiều lần nên trông thấy là nhận ra.
quen quen|Hơi quen, hình như đã gặp hay thấy ở đâu đó.
quen tay|Đã làm nhiều lần nên thao tác thành thạo, tự nhiên.
quen thuộc|Đã biết rõ, gặp nhiều lần nên rất gần gũi.
quét|Dùng chổi gom bụi rác cho sạch; cũng chỉ lướt máy qua để dò, đọc mã.
quét dọn|Quét và sắp xếp cho nhà cửa sạch sẽ, gọn gàng.
quét sạch|Quét cho hết rác; cũng chỉ loại bỏ hoàn toàn.
quê hương|Nơi mình sinh ra, lớn lên hoặc gắn bó sâu nặng.
quê nhà|Quê hương, nơi gia đình mình sinh sống lâu đời.
quê quán|Nơi gốc gác của gia đình, dòng họ, thường ghi trong giấy tờ.
quên|Không nhớ ra được điều đã biết hoặc cần làm.
quên bẵng|Hoàn toàn không còn nhớ tới trong một thời gian dài.
quên béng|Hoàn toàn không nhớ ra, quên mất lúc nào không hay.
quên khuấy|Bỗng nhiên không nhớ gì đến việc cần làm, quên bẵng đi.
quốc gia|Đất nước có lãnh thổ, dân cư và chính quyền riêng.
quốc lộ|Đường lớn do nhà nước quản lý, nối các tỉnh với nhau.
quốc tế|Thuộc về nhiều nước hoặc giữa các nước với nhau.
quyển|Từ dùng để chỉ từng cuốn sách, vở.
quyên góp|Cùng đóng góp tiền, đồ để giúp người gặp khó khăn.
quyền hạn|Phạm vi những việc một người được phép làm theo chức vụ.
quyền lợi|Những lợi ích mà một người được hưởng theo quy định.
quyền lực|Sức mạnh, khả năng điều khiển, chi phối người khác.
quyền năng|Sức mạnh và khả năng lớn lao, có thể làm được nhiều điều.
quyến rũ|Có sức hấp dẫn mạnh mẽ, làm người khác say mê, thích thú.
quyết|Đã định chắc sẽ làm, không thay đổi ý định.
quyết định|Lựa chọn dứt khoát cách làm sau khi đã cân nhắc.
quyết đoán|Dám đưa ra quyết định nhanh và dứt khoát.
quyết liệt|Mạnh mẽ, dứt khoát đến cùng, không nhân nhượng.
quyết tâm|Kiên định, không lùi bước để làm cho bằng được.
quýt|Quả họ cam, nhỏ, vỏ mỏng dễ bóc, vị ngọt hơi chua.
ra đi|Rời khỏi nơi đang ở để đến nơi khác, thường là đi xa.
ra đời|Được sinh ra; cũng chỉ một vật, một tổ chức lần đầu xuất hiện.
ra hiệu|Dùng cử chỉ, ánh mắt hay âm thanh để báo cho người khác biết.
ra khơi|Đưa thuyền rời bến ra biển xa, thường để đánh bắt cá.
ra lệnh|Yêu cầu người khác bắt buộc phải làm theo điều mình nói.
ra mắt|Xuất hiện lần đầu trước công chúng; cũng chỉ lần đầu gặp nhà người yêu.
rã rời|Mệt mỏi đến mức chân tay như muốn rời ra.
ra sao|Dùng để hỏi tình hình, kết quả của việc gì diễn ra thế nào.
ra sức|Dốc hết sức lực để làm việc gì.
ra vào|Đi vào và đi ra một nơi, thường là nhiều lần.
ra vẻ|Cố tỏ ra bên ngoài như mình là người thế này thế kia.
rác thải|Những thứ bỏ đi sau khi dùng, cần được thu gom, xử lý.
rách|Bị toạc ra, thủng, không còn lành lặn, thường nói về vải, giấy.
rách nát|Bị hư hỏng nhiều chỗ, cũ kỹ, tơi tả.
rạch ròi|Phân định rõ ràng, minh bạch từng điều.
radio|Máy thu sóng để nghe tin tức, âm nhạc từ các đài phát thanh.
rái cá|Loài thú nhỏ sống ven nước, bơi giỏi, ăn cá.
rám nắng|Da sạm màu đi do phơi nắng nhiều.
rạn nứt|Có vết nứt nhỏ; cũng chỉ tình cảm bắt đầu sứt mẻ, không còn gắn bó.
ràng buộc|Bó buộc, giữ lại khiến không được tự do.
rạng đông|Lúc bình minh, ánh sáng đầu tiên xuất hiện ở phía đông.
rạng rỡ|Tươi sáng, rực rỡ, thường nói về nụ cười hay gương mặt vui vẻ.
rạng sáng|Lúc trời vừa mới hửng sáng.
rành|Hiểu rất rõ, thông thạo một việc hay một nơi nào đó.
rành mạch|Rõ ràng từng điều, dễ hiểu, không lẫn lộn.
rảnh rang|Thong thả, không bận bịu việc gì.
rành rọt|Rõ ràng, mạch lạc, từng điều một đều dễ hiểu.
rảnh rỗi|Không có việc phải làm, có nhiều thời gian trống.
rảnh tay|Không phải cầm nắm hay bận làm gì nên có thể làm việc khác.
rào chắn|Vật dựng lên để ngăn lối đi hay bảo vệ một khu vực.
rào rào|Tiếng động đều và dồn dập, như tiếng mưa rơi, lá xào xạc.
rạp hát|Nơi có sân khấu để biểu diễn ca nhạc, kịch cho khán giả xem.
rạp xiếc|Nơi biểu diễn xiếc, thường có sân khấu tròn ở giữa.
rau cải|Các loại rau họ cải, lá xanh, dùng để luộc, xào, nấu canh.
rau cần|Loại rau thân rỗng, mọc ở ruộng nước, có mùi thơm riêng.
rau câu|Loại tảo biển dùng nấu thạch; cũng chỉ món thạch mát làm từ nó.
rau cỏ|Các loại rau ăn hằng ngày nói chung.
rau dền|Loại rau lá màu xanh hoặc đỏ tía, thường dùng nấu canh.
rau dưa|Rau và dưa muối; cũng chỉ bữa ăn đạm bạc, đơn giản.
rau đậu|Các loại rau và đậu dùng làm thức ăn nói chung.
rau má|Cây thân bò, lá tròn nhỏ, dùng ăn sống hoặc xay làm nước uống.
rau mùi|Rau thơm lá nhỏ có răng cưa, hay rắc lên món ăn, còn gọi là ngò.
rau muống|Rau thân rỗng, lá dài, thường luộc hoặc xào.
rau quả|Các loại rau và trái cây dùng làm thực phẩm nói chung.
rau răm|Loại rau thơm lá nhọn, vị cay nồng, hay ăn kèm trứng vịt lộn.
rau sạch|Rau được trồng an toàn, không dùng hóa chất độc hại.
rau sống|Các loại rau ăn tươi không nấu chín, dùng kèm món khác.
rau thơm|Các loại rau có mùi thơm, ăn sống kèm món ăn như húng, tía tô.
rau xanh|Các loại rau lá màu xanh dùng làm thức ăn hằng ngày.
rắc rối|Phức tạp, khó giải quyết; cũng chỉ chuyện phiền phức.
rắn chắc|Cứng cáp, khỏe mạnh, không mềm yếu.
rắn độc|Loài rắn có nọc độc, cần tránh xa khi gặp.
rắn nước|Loài rắn hiền, không độc, sống ở ao hồ, đồng ruộng và hay bắt cá.
răng|Phần cứng màu trắng mọc trong miệng, dùng để cắn, nhai.
răng cửa|Những chiếc răng ở phía trước, dùng để cắn thức ăn.
răng hàm|Răng to ở phía trong, dùng để nghiền nhai thức ăn.
răng khôn|Răng hàm mọc muộn nhất, thường ở tuổi trưởng thành.
răng nanh|Răng nhọn nằm giữa răng cửa và răng hàm.
răng sữa|Những chiếc răng đầu tiên của trẻ nhỏ, sau này sẽ thay bằng răng mới.
râm mát|Có bóng cây che, mát mẻ và dễ chịu.
râm ran|Âm thanh vang lên đều đều và rộn rã khắp nơi, như tiếng ve kêu.
rậm rạp|Cây cối mọc dày đặc, um tùm.
rầm rầm|Âm thanh to, mạnh, vang dội liên tiếp.
rầm rộ|Diễn ra sôi nổi, ồn ào với quy mô lớn.
râu dê|Chòm râu thưa và dài ở cằm, giống râu con dê.
râu mép|Phần râu mọc ở phía trên môi trên của đàn ông.
rầu rĩ|Buồn bã kéo dài, vẻ mặt ủ ê, không vui.
râu ria|Râu mọc quanh miệng, cằm; cũng chỉ những điều phụ, không quan trọng.
rẻ mạt|Giá rất thấp, thấp đến mức gần như không đáng gì.
rẻ tiền|Giá thấp; cũng chỉ thứ kém chất lượng, tầm thường.
rèn luyện|Tập luyện nhiều lần để có thói quen, kỹ năng hay sức khỏe tốt.
reo hò|Cùng hô to, la lên vì vui mừng hoặc để cổ vũ.
reo mừng|Kêu lên vui sướng khi nhận được tin vui hay điều tốt lành.
rì rào|Tiếng nhỏ, đều đều như tiếng gió thổi qua lá, sóng vỗ.
rỉ tai|Ghé sát tai người khác để nói nhỏ điều gì.
riêng|Chỉ thuộc về một người, một việc, không chung với ai khác.
riêng biệt|Tách hẳn ra, không lẫn hay chung với cái khác.
riêng lẻ|Từng cái tách biệt, không gộp chung thành nhóm.
riêng rẽ|Tách ra từng người, từng cái, không chung với nhau.
riêng tư|Thuộc về đời sống cá nhân, không muốn người khác biết hay xen vào.
riêu|Món canh có vị chua, nấu bằng cua giã nhỏ hoặc cá, thường thêm cà chua.
riêu cua|Món canh nấu từ cua đồng giã lọc, gạch cua nổi thành từng mảng.
rình|Nấp kín, lặng lẽ chờ thời cơ để xem hay bắt, như mèo đợi chuột.
rình mò|Lén lút theo dõi, dò xét để biết chuyện của người khác.
rình rập|Lén lút chờ sẵn, theo dõi để chực hành động.
ríu rít|Tiếng chim hay tiếng nói liên tục, trong trẻo và vui vẻ.
rõ nét|Hiện ra rõ ràng, sắc nét, dễ nhận thấy.
rõ ràng|Dễ thấy, dễ hiểu, không gây nghi ngờ hay nhầm lẫn.
rõ rệt|Thể hiện rất rõ, ai cũng dễ dàng nhận ra.
róc rách|Tiếng nước chảy nhẹ, đều qua khe đá.
rón rén|Đi nhẹ nhàng, khẽ khàng để không gây tiếng động.
rong chơi|Đi chơi đây đó thong thả, không bận tâm việc gì.
ròng rã|Kéo dài liên tục trong suốt một thời gian dài.
rong rêu|Rong và rêu, những loài cây nhỏ mọc ở nơi ẩm ướt hay dưới nước.
ròng rọc|Bánh xe có rãnh luồn dây, dùng để kéo vật nặng lên dễ hơn.
rong ruổi|Đi liên tục qua nhiều nơi, trên những chặng đường dài.
rối bời|Rối tung lên; cũng chỉ lòng dạ ngổn ngang, không yên.
rối bù|Tóc hoặc sợi rối tung, xù lên, không gọn gàng.
rồi đây|Trong thời gian sắp tới, sau này.
rối nước|Nghệ thuật múa rối truyền thống biểu diễn trên mặt nước.
rối rắm|Lộn xộn, chằng chịt, khó gỡ ra hay khó hiểu.
rối rít|Liên tục, vội vã vì quá mừng hay quá lo.
rồi sao|Câu hỏi về điều xảy ra tiếp theo, đôi khi tỏ ý thách thức.
rối tung|Bị rối và lộn xộn hết cả lên.
rộn rã|Vui tươi, náo nức, nhiều âm thanh vang lên liên tiếp.
rộn ràng|Vui tươi, nhộn nhịp, náo nức trong lòng hay trong không khí.
rồng|Con vật truyền thuyết thân dài có vảy, biết bay, tượng trưng cho sức mạnh.
rộng lớn|Có diện tích, quy mô rất lớn.
rộng lượng|Dễ tha thứ, bao dung, không chấp nhặt.
rộng mở|Mở ra rộng rãi, thoáng đãng; cũng chỉ sẵn lòng đón nhận điều mới.
rộng rãi|Có nhiều khoảng trống, thoáng đãng; cũng chỉ người hào phóng.
rồng rắn|Trò chơi dân gian, trẻ em nối đuôi nhau thành hàng dài uốn lượn.
rời bỏ|Đi khỏi, không ở lại hay gắn bó với nơi đó, người đó nữa.
rời rạc|Tách rời nhau, không liền mạch, thiếu gắn kết.
rơi vãi|Rơi ra rải rác mỗi chỗ một ít.
rơm rạ|Thân và gốc cây lúa còn lại sau khi gặt, phơi khô.
ru ngủ|Hát ru, vỗ về cho trẻ ngủ; cũng chỉ làm người khác lơ là, mất cảnh giác.
rủ rê|Mời gọi, lôi kéo người khác cùng làm gì.
rủi ro|Điều không may có thể xảy ra, gây thiệt hại.
run rẩy|Run lên từng chập vì lạnh, sợ hay xúc động.
run run|Hơi run, rung khẽ, thường do lạnh, sợ hay xúc động.
rung chuyển|Rung mạnh, lay động cả một vùng rộng lớn.
rung động|Rung nhẹ liên tục; cũng chỉ lòng xao xuyến, cảm động trước ai, điều gì.
rùng mình|Bỗng run lên một cái vì lạnh hoặc sợ hãi.
rung rinh|Rung nhẹ, đung đưa qua lại một cách khẽ khàng.
ruồi|Côn trùng nhỏ có cánh, hay bay đậu vào thức ăn.
ruồi muỗi|Ruồi và muỗi, những loài côn trùng nhỏ hay gây phiền toái.
ruộng|Đất trồng lúa hay hoa màu, thường có bờ bao quanh.
ruộng đất|Đất đai dùng để trồng trọt nói chung.
ruộng lúa|Mảnh ruộng được cày cấy để trồng lúa.
ruộng muối|Khu đất bằng ven biển để phơi nước biển làm muối.
ruột|Bộ phận trong bụng giúp tiêu hóa thức ăn; cũng chỉ phần lõi bên trong.
ruột thịt|Cùng chung dòng máu, có quan hệ gia đình rất gần.
ruột xe|Săm xe, ống cao su chứa hơi nằm bên trong lốp xe.
rút gọn|Làm cho ngắn gọn, đơn giản hơn mà vẫn giữ ý chính hoặc giá trị.
rút lại|Lấy lại lời nói, ý kiến đã đưa ra; cũng chỉ co ngắn lại.
rút lui|Lùi lại, thôi không tham gia hay tiến tới nữa.
rút ngắn|Làm cho ngắn hơn về độ dài hoặc thời gian.
rụt rè|Ngại ngùng, e dè, không dám mạnh dạn nói hay làm.
rút thăm|Bốc ngẫu nhiên một lá thăm để chọn người hay chia lượt.
rút tiền|Lấy tiền ra từ tài khoản ngân hàng hay cây ATM.
rửa ảnh|In ảnh từ phim hay tệp ảnh ra giấy ảnh.
rửa sạch|Dùng nước kỳ cọ cho hết bụi bẩn.
rực lửa|Đỏ rực như lửa cháy; cũng chỉ nhiệt huyết, sôi nổi mãnh liệt.
rực rỡ|Sáng chói, nhiều màu tươi đẹp; cũng chỉ thành công nổi bật.
rừng|Vùng đất rộng có nhiều cây cối mọc tự nhiên.
rừng già|Rừng lâu năm, cây to cao, chưa bị con người chặt phá.
rừng núi|Vùng đất có nhiều rừng cây và đồi núi.
rừng rậm|Rừng có cây cối mọc dày đặc, khó đi lại.
rừng rú|Rừng rậm hoang vu, ít người qua lại.
rừng xanh|Núi rừng xanh tươi, hoang sơ, có nhiều cây cối và muông thú.
rước|Đón về trang trọng; cũng chỉ cầm đèn, cờ đi thành đoàn trong lễ hội.
rước đèn|Trẻ em cầm đèn lồng đi thành đoàn vào đêm Trung thu.
rườm rà|Dài dòng, nhiều chi tiết thừa, không gọn.
sa mạc|Vùng đất rộng rất khô hạn, nhiều cát, ít mưa và cây cối.
sách|Tập giấy in chữ, hình, đóng lại thành quyển để đọc.
sạch bách|Sạch trơn, không còn sót lại chút gì.
sạch đẹp|Gọn gàng, không bụi bẩn và trông dễ chịu, ưa nhìn.
sạch sẽ|Không có bụi bẩn, gọn gàng, ngăn nắp.
sách vở|Đồ dùng học tập gồm các loại sách và vở; cũng chỉ kiến thức nặng lý thuyết.
sải cánh|Dang rộng đôi cánh; cũng là độ dài từ mút cánh này sang mút cánh kia.
sai lầm|Điều làm sai, không đúng, gây hậu quả không tốt.
sai lệch|Không đúng, lệch khỏi chuẩn hoặc sự thật.
sai trái|Trái với lẽ phải và đạo đức, không nên làm.
sàn diễn|Mặt sàn nơi người mẫu, nghệ sĩ trình diễn trước khán giả.
san hô|Sinh vật nhỏ sống ở biển, tạo thành những rạn đá nhiều màu sắc.
san lấp|Đổ đất cát để lấp đầy và làm phẳng chỗ trũng.
sản lượng|Số lượng sản phẩm làm ra trong một khoảng thời gian nhất định.
sàn nhà|Mặt nền phía dưới trong nhà, nơi người đi lại, kê đồ đạc.
sàn nhảy|Khu vực có mặt sàn rộng để mọi người cùng khiêu vũ.
sản phẩm|Thứ được làm ra từ lao động, sản xuất để dùng hoặc bán.
san sẻ|Chia bớt cho người khác cùng hưởng hoặc cùng gánh vác.
sáng|Phần đầu của ngày, từ lúc trời rạng đến gần trưa; cũng là có nhiều ánh sáng.
sáng bóng|Sạch và bóng loáng, phản chiếu được ánh sáng.
sáng chế|Tạo ra cách làm hay vật dụng mới chưa từng có; cũng chỉ chính phát minh đó.
sáng chói|Rực rỡ đến lóa mắt; cũng chỉ thành tích nổi bật, xuất sắc.
sáng giá|Nổi bật và có triển vọng, được nhiều người đánh giá cao.
sảng khoái|Thấy khoan khoái, dễ chịu và tỉnh táo trong người.
sáng kiến|Ý tưởng mới giúp công việc được làm tốt hơn, hiệu quả hơn.
sáng lập|Đứng ra gây dựng một tổ chức, công ty hay phong trào từ đầu.
sàng lọc|Chọn lọc kỹ để loại bớt cái không đạt, giữ lại cái phù hợp.
sáng mai|Buổi sáng của ngày hôm sau.
sang năm|Năm tới, tức là năm liền sau năm nay.
sáng qua|Buổi sáng của ngày hôm qua.
sáng rực|Tỏa ánh sáng mạnh, rực rỡ khắp xung quanh.
sáng sớm|Lúc đầu buổi sáng, khi trời vừa hửng.
sáng sủa|Nhiều ánh sáng, thoáng đãng; cũng chỉ vẻ mặt tươi tỉnh, dễ mến.
sáng suốt|Nhìn nhận rõ ràng, đúng đắn và biết quyết định khôn ngoan.
sáng tác|Tạo ra tác phẩm nghệ thuật như thơ, truyện, bài hát, tranh vẽ.
sáng tạo|Nghĩ ra cái mới hoặc cách làm mới, không rập khuôn theo cái cũ.
sáng tỏ|Trở nên rõ ràng, dễ hiểu, không còn điều gì thắc mắc.
sang trọng|Đẹp, lịch sự và đắt tiền, toát lên vẻ quý phái.
sáng trưng|Được chiếu sáng rõ khắp mọi chỗ, thường nhờ nhiều đèn.
sảnh|Gian phòng rộng ở lối vào của tòa nhà, khách sạn, nơi đón khách.
sành ăn|Biết thưởng thức và phân biệt món ngon dở rất tinh tế.
sành điệu|Hợp thời trang, có gu và biết chọn những thứ đang thịnh hành.
sành sỏi|Am hiểu và có nhiều kinh nghiệm về một lĩnh vực nào đó.
sành sứ|Đồ gốm làm bằng sành và sứ như bát, đĩa, bình hoa.
sao băng|Vệt sáng vụt qua bầu trời đêm khi thiên thạch rơi vào khí quyển.
sao biển|Động vật biển thân dẹt hình ngôi sao, thường có năm cánh.
sao chép|Chép lại hoặc tạo bản giống hệt bản gốc.
sao cho|Làm thế nào để đạt được điều mong muốn, dùng để nêu mục đích.
sao chổi|Thiên thể có đuôi sáng dài, bay quanh Mặt Trời.
sao không|Dùng để hỏi lý do vì sao không làm, hoặc gợi ý nên làm.
sáo trúc|Ống sáo làm từ cây trúc, thổi ra tiếng trong trẻo.
sao vậy|Câu hỏi có chuyện gì xảy ra hay vì lý do gì.
sạp hàng|Chỗ bày bán hàng trong chợ, thường là bục hay giá gỗ kê cao.
sáp ong|Chất dẻo màu vàng do ong tiết ra để xây tổ, dùng làm nến, mỹ phẩm.
sát cánh|Kề vai bên nhau, cùng làm việc và vượt qua khó khăn.
sau cùng|Ở vị trí cuối, đứng sau tất cả những cái khác.
sau đây|Phần ngay tiếp theo, điều sắp được nói hoặc làm.
sau đó|Khoảng thời gian tiếp theo ngay sau việc vừa nhắc đến.
sau lưng|Ở phía sau người; cũng chỉ lúc người đó vắng mặt, không biết.
sáu mươi|Số bằng sáu lần mười, viết là 60.
sau này|Khoảng thời gian về sau, trong tương lai.
say đắm|Yêu hay thích say sưa, đắm chìm, không dứt ra được.
say mê|Thích thú, ham mê đến mức quên cả mọi thứ khác.
sắc bén|Cắt rất ngọt; cũng chỉ đầu óc, lời lẽ nhanh nhạy và đúng trọng tâm.
sắc đẹp|Vẻ đẹp về ngoại hình của một người.
sắc mặt|Vẻ mặt và màu da trên mặt, cho thấy tâm trạng hay sức khỏe.
sặc sỡ|Có nhiều màu sắc tươi, nổi bật, đập vào mắt.
sắc tố|Chất tạo nên màu sắc cho da, tóc, lá cây và nhiều sinh vật.
sắm sửa|Mua sắm, chuẩn bị đồ dùng cần thiết, nhất là vào dịp lễ Tết.
sắm vai|Đóng một vai trong kịch, phim; cũng là nhận lấy một vai trò nào đó.
săn đón|Niềm nở, ân cần đón tiếp; cũng chỉ việc được nhiều người tìm đến.
sẵn lòng|Vui vẻ đồng ý làm điều gì, không chút ngần ngại.
săn lùng|Ra sức tìm kiếm khắp nơi để có cho bằng được.
sắp đặt|Bố trí, sắp xếp mọi thứ theo một trật tự hoặc kế hoạch.
sắp sửa|Chuẩn bị xảy ra hoặc sẽ làm ngay trong chốc lát.
sắt thép|Kim loại cứng như sắt, thép nói chung; cũng chỉ ý chí cứng cỏi, vững vàng.
sắt vụn|Đồ sắt cũ, hỏng hoặc mảnh vụn, thường gom bán để tái chế.
sấm chớp|Tiếng nổ rền và ánh chớp lóe sáng trên trời khi có giông.
sấm sét|Tiếng nổ lớn kèm tia điện rất mạnh phóng xuống từ đám mây giông.
sầm uất|Đông người qua lại, buôn bán tấp nập.
sân bãi|Khu đất rộng dùng để chơi thể thao, đỗ xe hoặc chứa hàng.
sân bay|Nơi máy bay cất cánh, hạ cánh và đón trả hành khách.
sân bóng|Khoảng đất rộng có kẻ vạch và khung thành, dùng để chơi bóng đá.
sân chơi|Khoảng sân để trẻ em vui chơi; cũng chỉ nơi mọi người cùng giao lưu, thi tài.
sân cỏ|Bãi đất phủ cỏ, thường dùng để đá bóng; cũng chỉ môn bóng đá nói chung.
sân khấu|Bục cao nơi diễn viên, ca sĩ biểu diễn trước khán giả.
sân sau|Khoảng đất trống phía sau ngôi nhà, thường để phơi đồ, trồng cây.
sần sùi|Có nhiều nốt lồi lõm, sờ vào thấy ráp, không nhẵn.
sân thượng|Khoảng trống trên nóc nhà, có thể lên phơi đồ, trồng cây, hóng mát.
sâu bọ|Tên gọi chung các loài côn trùng nhỏ như kiến, ruồi, cào cào.
sâu đậm|Rất sâu sắc và bền chặt, như tình cảm hay ấn tượng khó phai.
sâu nặng|Tình cảm sâu sắc và gắn bó bền chặt.
sầu riêng|Quả to, vỏ đầy gai nhọn, múi vàng béo ngậy, mùi rất nồng.
sâu róm|Con sâu có nhiều lông dài, đụng vào da dễ bị ngứa.
sâu sắc|Hiểu và nghĩ thấu đáo đến tận cùng; cũng chỉ tình cảm rất sâu nặng.
sâu xa|Ẩn sâu bên trong, phải suy nghĩ kỹ mới thấy hết được.
sấy tóc|Làm khô tóc bằng hơi nóng, thường dùng máy sấy.
se lạnh|Hơi lạnh nhẹ, thường vào lúc chớm sang thu hoặc đông.
se sẻ|Chim sẻ, loài chim nhỏ lông nâu, hay sống gần nhà người.
sền sệt|Hơi đặc, sánh lại, không còn loãng.
shop|Cửa hàng nhỏ, thường bán quần áo, mỹ phẩm hay đồ dùng.
siêng|Chịu khó, hay làm, không ngại việc.
siêng năng|Chăm chỉ và chịu khó, làm việc, học tập đều đặn không lười biếng.
siêu|Vượt xa mức bình thường, cực kỳ; cũng là ấm đất nhỏ có cán để sắc thuốc.
siêu nhân|Nhân vật có sức mạnh phi thường trong phim, truyện; cũng khen người cực giỏi.
siêu sao|Ngôi sao cực kỳ nổi tiếng trong ngành giải trí hoặc thể thao.
siêu thị|Cửa hàng lớn bày bán nhiều loại hàng, khách tự chọn rồi trả tiền ở quầy.
siêu tốc|Có tốc độ cực nhanh, như loại ấm điện đun sôi nước chỉ trong vài phút.
sinh|Đẻ ra con; cũng chỉ làm nảy ra, tạo ra điều gì mới.
sinh ba|Ba đứa trẻ cùng được mẹ sinh ra trong một lần.
sinh đôi|Hai đứa trẻ cùng một mẹ, được sinh ra trong cùng một lần.
sinh động|Đầy sức sống, gợi hình rõ nét và cuốn hút người xem, người nghe.
sinh hoạt|Những việc thường ngày như ăn, ngủ, làm việc; cũng chỉ buổi họp tập thể.
sinh học|Môn khoa học nghiên cứu về sự sống của sinh vật.
sinh mạng|Sự sống của một con người, thứ quý giá nhất cần được bảo vệ.
sinh nhật|Ngày kỷ niệm ngày ra đời của một người.
sinh ra|Được mẹ đẻ ra, bắt đầu một cuộc đời; cũng chỉ làm nảy ra điều gì.
sinh sống|Sống và làm ăn ở một nơi nào đó.
sinh thái|Mối quan hệ giữa sinh vật với nhau và với môi trường sống.
sinh tố|Đồ uống xay từ trái cây với đá, sữa; cũng là tên gọi khác của vitamin.
sinh tồn|Duy trì sự sống, tồn tại được trong điều kiện khó khăn.
sinh vật|Những vật có sự sống như con người, động vật, cây cối, vi khuẩn.
sinh viên|Người đang theo học ở trường đại học hoặc cao đẳng.
so bì|Hay so sánh hơn thiệt với người khác vì sợ mình bị kém phần.
sò huyết|Loại sò nhỏ vỏ có khía, thịt màu đỏ, thường nướng hoặc luộc ăn.
so le|Không ngang hàng nhau, chỗ cao chỗ thấp hoặc lệch nhau xen kẽ.
so sánh|Xem xét hai hay nhiều thứ để thấy chỗ giống và khác nhau.
so với|Đặt bên cạnh cái khác để đối chiếu, xem hơn hay kém.
soạn|Sắp xếp, chuẩn bị sẵn đồ đạc; cũng là viết ra bài, văn bản, bản nhạc.
soạn thảo|Viết và trình bày một văn bản như thư, hợp đồng, báo cáo.
soát vé|Kiểm tra vé của hành khách hoặc khán giả trước khi cho vào.
sóc chuột|Con vật nhỏ giống sóc, lưng có sọc, có túi má để đựng hạt.
soda|Nước có ga sủi bọt, thường pha với chanh hoặc siro thành đồ uống mát.
son phấn|Son môi và phấn, những thứ dùng để trang điểm.
song ca|Hai người cùng hát chung một bài, khi hát đối đáp, khi hòa giọng.
sóng gió|Gió to và sóng lớn; thường chỉ những khó khăn, trắc trở trong đời.
song ngữ|Dùng cùng lúc hai ngôn ngữ, như sách in cả tiếng Việt và tiếng Anh.
sòng phẳng|Rõ ràng, công bằng trong chuyện tiền bạc, không ai thiệt ai.
song sinh|Được cùng một mẹ sinh ra trong một lần, như anh chị em sinh đôi.
song song|Hai đường luôn cách đều, không bao giờ gặp nhau; cũng chỉ việc cùng diễn ra một lúc.
sọt rác|Giỏ hoặc thùng nhỏ dùng để đựng rác.
số âm|Giá trị nhỏ hơn 0, viết có dấu trừ đứng trước.
số chẵn|Số chia hết cho 2, như 0, 2, 4, 6, 8.
số dư|Khoản tiền còn lại trong tài khoản; cũng là phần thừa ra trong phép chia.
số đông|Phần lớn người trong một tập thể hay xã hội.
số hiệu|Con số hoặc ký hiệu để phân biệt, như số hiệu chuyến bay.
số ít|Lượng nhỏ, phần ít; trong ngữ pháp là dạng chỉ một người hay một vật.
số không|Con số 0, biểu thị không có gì cả.
số liệu|Các con số được ghi nhận, dùng để tính toán hay đánh giá.
số lượng|Mức nhiều hay ít của người, vật, tính bằng con số.
số mệnh|Những điều được tin là đã định sẵn cho cuộc đời mỗi người.
số một|Con số 1; cũng chỉ người, vật đứng đầu, giỏi nhất.
số nhiều|Lượng lớn, phần đông; trong ngữ pháp là dạng chỉ từ hai người, vật trở lên.
số phận|Cuộc đời may rủi, sướng khổ mà mỗi người gặp phải.
sổ sách|Các loại sổ ghi chép nói chung, nhất là sổ ghi thu chi, kế toán.
sổ tay|Cuốn sổ nhỏ mang theo để ghi chép; cũng chỉ sách hướng dẫn ngắn gọn.
sôi động|Nhộn nhịp, náo nhiệt, có nhiều hoạt động diễn ra.
sôi nổi|Hăng hái, náo nhiệt, mọi người đều hào hứng tham gia.
sông|Dòng nước lớn chảy tự nhiên, đổ ra biển hoặc hồ.
sông băng|Khối băng rất lớn ở núi cao hay vùng cực, trôi chậm như một dòng sông.
sống còn|Hết sức quan trọng, quyết định việc còn hay mất của một điều gì.
sống động|Tràn đầy sức sống, như đang diễn ra thật trước mắt.
sống lại|Hồi sinh, có lại sự sống; cũng chỉ kỷ niệm hiện về rõ nét.
sống lưng|Phần dọc giữa lưng, nơi có xương cột sống chạy qua.
sống mũi|Phần nhô cao chạy dọc từ giữa hai mắt xuống đầu mũi.
sông ngòi|Tên gọi chung các dòng sông, kênh rạch trong một vùng.
sông núi|Núi và sông; thường dùng để chỉ đất nước, quê hương.
sông nước|Cảnh vùng có nhiều sông và kênh rạch, gắn với cuộc sống trên mặt nước.
sốt ruột|Nóng lòng, bồn chồn vì mong đợi hoặc lo lắng.
sơ bộ|Bước đầu, còn qua loa, chưa đi vào chi tiết.
sơ chế|Làm sạch, cắt gọt nguyên liệu trước khi nấu hoặc chế biến tiếp.
sơ đẳng|Ở mức đơn giản và cơ bản nhất.
sơ đồ|Hình vẽ đơn giản cho thấy cách bố trí hoặc mối liên hệ giữa các phần.
sơ hở|Chỗ thiếu cẩn thận, lơ là khiến người khác dễ lợi dụng.
sở hữu|Có quyền làm chủ, nắm giữ một tài sản hay vật gì đó.
sơ qua|Một cách ngắn gọn, khái quát, chưa đi vào chi tiết.
sơ sinh|Vừa mới chào đời, như em bé trong những tuần đầu tiên.
sở thích|Những việc mình yêu thích và hay làm lúc rảnh rỗi.
sở thú|Vườn nuôi nhiều loài thú để mọi người đến tham quan.
sở trường|Khả năng, việc làm mà mình giỏi và thành thạo nhất.
sớm muộn|Trước sau gì cũng xảy ra, chỉ là chuyện thời gian.
sớm tối|Từ sáng đến tối, ý nói lúc nào cũng vậy, ngày nào cũng thế.
sơn ca|Loài chim nhỏ hót rất hay, thường vừa bay vút lên cao vừa hót.
sơn dầu|Loại màu vẽ pha với dầu; cũng chỉ tranh vẽ bằng loại màu này.
sơn mài|Lối làm tranh, đồ mỹ nghệ bằng nhiều lớp sơn ta rồi mài cho bóng.
studio|Phòng được trang bị để chụp ảnh, quay phim hoặc thu âm.
su hào|Rau có củ tròn phình ra từ thân, vỏ xanh nhạt, thường xào, luộc, nấu canh.
su su|Quả xanh nhạt, hình như quả lê, vỏ có gai mềm, thường luộc hoặc xào.
súc miệng|Ngậm nước rồi khua trong miệng cho sạch, sau đó nhổ ra.
sủi bọt|Nổi lên nhiều bọt nhỏ, như nước sôi hay nước có ga.
sủi cảo|Món bánh gốc Hoa, vỏ bột mỏng gói nhân thịt tôm, ăn với nước dùng.
sui gia|Quan hệ giữa cha mẹ hai bên khi con cái lấy nhau, cách gọi ở miền Nam.
sung sức|Đang ở lúc khỏe mạnh, dồi dào năng lượng nhất.
sung sướng|Cảm thấy rất vui và hạnh phúc, đầy đủ mọi bề.
sung túc|Có của cải đầy đủ, đời sống dư dả, không thiếu thốn.
suối|Dòng nước nhỏ chảy tự nhiên, thường từ núi đồi đổ xuống.
suối khoáng|Dòng nước từ lòng đất chảy ra, chứa nhiều chất khoáng, thường dùng để tắm, ngâm.
suốt|Liên tục trong cả một khoảng thời gian, từ đầu đến cuối.
suốt đời|Trong cả cuộc đời, từ nay cho đến mãi về sau.
suy diễn|Từ điều đã biết mà lập luận ra điều khác; cũng là tự nghĩ thêm quá mức.
suy đoán|Dựa vào dấu hiệu để đoán điều chưa biết chắc.
suy giảm|Giảm sút dần về mức độ, chất lượng hoặc số lượng.
suy luận|Dựa vào điều đã biết để lập luận, rút ra kết luận mới.
suy ngẫm|Nghĩ đi nghĩ lại thật kỹ để hiểu sâu một điều gì đó.
suy nghĩ|Dùng trí óc để xem xét, cân nhắc một vấn đề.
suy tính|Cân nhắc, tính toán kỹ trước khi làm việc gì.
suy yếu|Trở nên yếu dần, kém mạnh mẽ hơn trước.
sự cố|Việc bất ngờ xảy ra gây trục trặc, hỏng hóc.
sử học|Ngành nghiên cứu các sự kiện và quá trình phát triển trong quá khứ.
sự kiện|Việc quan trọng hoặc đáng chú ý đã hoặc sẽ diễn ra.
sứ mệnh|Nhiệm vụ lớn lao, quan trọng được giao phó.
sự nghiệp|Công việc lâu dài mà một người theo đuổi và gây dựng.
sư phụ|Người thầy truyền dạy võ nghệ hoặc tay nghề cho học trò.
sự thật|Điều có thật, đúng như đã xảy ra.
sự thực|Điều đúng với thực tế, không phải bịa đặt.
sự tích|Truyện kể giải thích nguồn gốc của một sự vật hay phong tục từ xưa.
sư tử|Thú lớn họ mèo, lông vàng nâu, con đực có bờm dày quanh cổ.
sự việc|Chuyện đã hoặc đang xảy ra mà người ta nói tới.
sữa bột|Loại sữa đã được làm khô thành bột, pha với nước để uống.
sữa chua|Món làm từ sữa lên men, vị chua nhẹ, thường ăn lạnh.
sữa đặc|Loại sữa đã cô bớt nước và thêm đường, sánh và rất ngọt.
sữa đậu|Thức uống từ hạt đậu nành xay, lọc lấy nước và nấu chín.
sửa đổi|Thay đổi một vài chỗ cho hợp lý hơn, như nội quy, luật lệ.
sửa lại|Chỉnh lại cho đúng hoặc cho tốt hơn trước.
sửa lỗi|Tìm và chữa những chỗ sai, chỗ hỏng cho đúng.
sửa sai|Nhận ra và khắc phục việc mình đã làm chưa đúng.
sửa sang|Tu bổ, trang trí lại cho gọn đẹp hơn, nhất là nhà cửa.
sửa soạn|Chuẩn bị chu đáo, sắp xếp đồ đạc hoặc chải chuốt trước khi đi đâu.
sữa tươi|Loại sữa bò, sữa dê dạng lỏng, chưa cô đặc hay sấy thành bột.
sức bền|Khả năng chịu đựng, hoạt động liên tục lâu mà không bị mệt.
sức chứa|Lượng người hoặc vật tối đa mà một nơi có thể chứa được.
sức ép|Lực đè lên vật; cũng chỉ áp lực buộc phải làm theo điều gì.
sức hút|Sự lôi cuốn khiến người khác chú ý, muốn đến gần.
sức lực|Năng lượng của cơ thể dùng để làm việc, vận động.
sức mạnh|Khả năng mạnh mẽ về thể chất hoặc tinh thần để làm được việc lớn.
sức nặng|Độ nặng của vật; cũng chỉ mức quan trọng, sức thuyết phục của lời nói.
sức sống|Năng lượng giúp sinh vật sống và phát triển mạnh mẽ, tươi tắn.
sừng|Phần cứng nhọn mọc trên đầu một số con vật như trâu, bò, dê.
sửng sốt|Rất ngạc nhiên, bất ngờ đến mức sững người.
sững sờ|Lặng người đi vì quá bất ngờ hoặc xúc động.
sừng trâu|Cặp sừng cứng, cong và dài trên đầu con trâu.
sưởi nắng|Phơi mình dưới nắng cho ấm người, nhất là vào ngày lạnh.
sườn|Phần hai bên thân có các xương cong; cũng chỉ mặt dốc của núi đồi.
sương|Những hạt nước rất nhỏ đọng trên lá hoặc lơ lửng trong không khí.
sương giá|Lớp hơi nước đóng băng trắng trên mặt đất, cây cỏ khi trời rất lạnh.
sương mai|Những giọt sương đọng trên lá cỏ lúc sáng sớm.
sương mù|Hơi nước dày đặc sát mặt đất, làm mờ tầm nhìn.
sướt mướt|Khóc nhiều, nước mắt dầm dề; cũng chỉ lối viết, hát quá ủy mị.
sứt mẻ|Bị vỡ mất một mảnh nhỏ ở mép; cũng chỉ tình cảm bị rạn nứt.
sưu tầm|Tìm tòi, gom góp những thứ quý hoặc mình yêu thích, như tem, tiền xu.
sưu tập|Gom góp nhiều vật cùng loại thành bộ để lưu giữ; cũng chỉ bộ vật đó.
tả cảnh|Dùng lời văn miêu tả lại phong cảnh, một dạng bài tập làm văn.
tã lót|Miếng vải hay giấy mềm lót cho em bé để giữ vệ sinh.
tạ ơn|Bày tỏ lòng biết ơn một cách trang trọng.
tác dụng|Kết quả, ảnh hưởng mà một vật hoặc việc làm mang lại.
tác động|Gây ảnh hưởng, làm cho người hoặc vật khác thay đổi.
tác giả|Người viết ra hoặc sáng tạo nên một tác phẩm.
tác hại|Ảnh hưởng xấu, sự thiệt hại do một việc gây ra.
tác nhân|Yếu tố hay người gây ra một tác động, một sự thay đổi.
tác phẩm|Sản phẩm sáng tạo như bài văn, bức tranh, bản nhạc.
tác phong|Cách ăn mặc, đi đứng, làm việc thể hiện nề nếp của một người.
tách|Làm cho rời ra, không còn dính liền; cũng chỉ cái chén nhỏ có quai.
tách biệt|Riêng ra, cách xa, không gần gũi hay liên quan với xung quanh.
tách rời|Rời ra, không còn gắn liền với nhau.
tài ba|Có tài năng giỏi hơn người, rất xuất sắc.
tái chế|Xử lý đồ cũ, phế liệu để làm thành vật dùng được.
tài chính|Những việc liên quan đến tiền bạc, thu chi của cá nhân hay tổ chức.
tại chỗ|Ngay ở nơi đang diễn ra sự việc, không đi nơi khác.
tài giỏi|Có năng lực và làm việc giỏi giang.
tai hại|Gây ra thiệt hại, đem lại hậu quả xấu.
tài hoa|Có tài năng nổi bật, nhất là về nghệ thuật, văn chương.
tái hợp|Sum họp, về lại với nhau sau thời gian xa cách.
tài khoản|Nơi ghi tiền gửi ở ngân hàng; cũng chỉ thông tin đăng nhập trên mạng.
tài liệu|Giấy tờ, sách vở chứa thông tin dùng để học tập, tham khảo.
tai mèo|Tai của con mèo; cũng chỉ loại đá vôi lởm chởm, sắc nhọn ở vùng núi.
tài năng|Khả năng đặc biệt, giỏi hơn người; cũng chỉ người có tài.
tai nghe|Thiết bị nhỏ đeo vào tai để nghe âm thanh.
tái ngộ|Gặp lại nhau sau một thời gian xa cách.
tài nguyên|Của cải có sẵn trong thiên nhiên như đất, nước, rừng, khoáng sản.
tại nhà|Ở ngay trong nhà mình, không phải đi đâu.
tài sản|Của cải, tiền bạc, nhà cửa thuộc quyền sở hữu của ai đó.
tại sao|Từ dùng để hỏi lý do, nguyên nhân.
tái tạo|Làm cho có lại hoặc tạo ra lại như ban đầu.
tài tình|Khéo léo và giỏi giang đến mức đáng khâm phục.
tải trọng|Sức nặng mà xe, cầu hay công trình phải chịu hoặc chở được.
tài trợ|Bỏ tiền hoặc của để hỗ trợ cho một hoạt động, chương trình.
tài tử|Diễn viên điện ảnh nổi tiếng; cũng chỉ người làm việc theo kiểu nghiệp dư.
tài xế|Người lái xe ô tô, xe khách theo nghề.
tạm biệt|Lời chào khi chia tay, mong sẽ gặp lại.
tam giác|Hình có ba cạnh và ba góc.
tám mươi|Con số 80, bằng tám lần mười.
tàm tạm|Tạm được, không tốt lắm mà cũng không tệ.
tạm thời|Chỉ trong một thời gian ngắn, không lâu dài.
tản bộ|Đi bộ thong thả để thư giãn, hít thở không khí.
tán chuyện|Nói chuyện phiếm, vui vẻ cho qua thời gian.
tán gẫu|Nói chuyện linh tinh, vui vẻ cho đỡ buồn.
tàn nhang|Những đốm nhỏ màu nâu trên da, thường thấy ở mặt.
tan rã|Rời ra từng phần, không còn gắn kết thành một khối.
tán thành|Đồng ý, ủng hộ một ý kiến hoặc việc làm.
tàng hình|Ẩn đi để không ai nhìn thấy được.
tạnh|Mưa đã ngừng hẳn, trời thôi không mưa nữa.
tạnh ráo|Hết mưa và trời đã khô ráo.
táo bạo|Dám nghĩ dám làm những việc khó, mạo hiểm.
tạo dựng|Gây dựng, xây dựng nên từ đầu.
tạo hình|Làm ra hình dáng, dáng vẻ cho một vật hoặc nhân vật.
tào lao|Vớ vẩn, linh tinh, không có ý nghĩa gì.
tạo thành|Làm nên, hợp lại để thành một thứ gì đó.
tạp chất|Chất lạ lẫn vào làm cho vật không còn tinh khiết.
tạp chí|Ấn phẩm ra định kỳ, có nhiều bài viết về một chủ đề.
tạp dề|Tấm vải đeo trước người để giữ quần áo sạch khi nấu nướng.
tàu bay|Cách gọi dân dã, xưa cũ của máy bay.
tàu bè|Các loại tàu, thuyền đi lại trên mặt nước nói chung.
tàu biển|Phương tiện lớn đi lại trên biển để chở người hoặc hàng hóa.
tàu điện|Phương tiện chở khách chạy bằng điện trên đường ray.
tàu thuyền|Những phương tiện như tàu, thuyền dùng để đi lại trên sông, biển.
taxi|Xe ô tô chở khách theo cuốc, tính tiền theo quãng đường.
tay áo|Phần của chiếc áo bao lấy cánh tay.
tay cầm|Bộ phận để cầm nắm của đồ vật; cũng chỉ thiết bị điều khiển trò chơi.
tay chân|Hai tay và hai chân nói chung, các chi của cơ thể.
tay lái|Bộ phận để điều khiển hướng đi của xe; cũng chỉ người lái xe.
tay nghề|Trình độ, kỹ năng làm một nghề.
tay phải|Cánh tay ở bên phải cơ thể; cũng chỉ người trợ thủ đắc lực.
tay trái|Cánh tay bên trái cơ thể; nghề tay trái là việc làm thêm ngoài nghề chính.
tay vịn|Thanh để vịn tay ở cầu thang, ghế hay lan can.
tắc kè|Loài bò sát giống thằn lằn nhưng to hơn, kêu thành tiếng vang.
tắc nghẽn|Bị ứ lại, không thông, như xe cộ kẹt cứng trên đường.
tăm bông|Que nhỏ có quấn bông ở đầu, dùng để vệ sinh tai, mũi.
tắm giặt|Việc tắm rửa thân thể và giặt giũ quần áo nói chung.
tắm gội|Tắm rửa thân thể và gội đầu cho sạch sẽ.
tắm hơi|Ngồi trong phòng hơi nóng để ra mồ hôi, giúp thư giãn.
tắm nắng|Phơi người dưới ánh nắng mặt trời cho ấm hoặc rám da.
tắm rửa|Dùng nước làm sạch thân thể nói chung.
tắm táp|Việc tắm nói chung, thường nói một cách vui vẻ, thoải mái.
tăng cường|Làm cho mạnh hơn, nhiều hơn hoặc tốt hơn.
tăng giá|Giá bán cao lên so với trước.
tăng giảm|Lúc nhiều lên, lúc ít đi, thay đổi lên xuống.
tăng tốc|Làm cho chạy nhanh hơn, đẩy nhanh tốc độ.
tăng trưởng|Lớn lên, phát triển thêm về quy mô, số lượng.
tắt tiếng|Bị mất giọng, không nói ra tiếng; cũng chỉ việc tắt âm thanh.
tẩm bổ|Ăn uống những món bổ dưỡng để khỏe mạnh.
tẩm bột|Lăn hoặc nhúng thực phẩm vào bột trước khi chiên.
tấm chắn|Vật phẳng dùng để che, ngăn bụi, gió hoặc nước bắn vào.
tầm cỡ|Quy mô, mức độ lớn lao hay quan trọng của một người, một việc.
tâm điểm|Điểm ở chính giữa; cũng chỉ nơi thu hút mọi sự chú ý.
tấm gương|Mặt kính để soi; cũng chỉ người có đức tính tốt đáng noi theo.
tâm hồn|Thế giới tình cảm, suy nghĩ bên trong của mỗi người.
tâm huyết|Toàn bộ tình cảm và sự nhiệt tình dồn vào một việc.
tấm lòng|Tình cảm chân thành, lòng tốt dành cho người khác.
tấm lợp|Vật liệu dạng tấm dùng để che mái nhà, như tôn hay ngói nhựa.
tầm mắt|Khoảng xa mà mắt có thể nhìn tới.
tầm nhìn|Khoảng xa mắt nhìn tới được; cũng chỉ khả năng nhìn xa trông rộng.
tâm sự|Kể cho người khác nghe những điều thầm kín trong lòng.
tầm tã|Mưa to kéo dài không ngớt; cũng chỉ nước mắt tuôn rơi nhiều.
tầm tay|Khoảng cách mà tay có thể với tới.
tầm thường|Bình thường, không có gì nổi bật hay đặc sắc.
tâm trạng|Trạng thái cảm xúc vui buồn trong lòng vào một lúc nào đó.
tâm trí|Trí óc và tình cảm, những gì ta đang nghĩ và cảm nhận.
tâm tư|Những suy nghĩ, tình cảm sâu kín trong lòng.
tầm vóc|Vóc dáng, chiều cao của người; cũng chỉ tầm cỡ, mức độ lớn lao.
tận cùng|Chỗ cuối cùng, xa nhất hoặc mức sâu nhất.
tận dụng|Dùng hết mọi thứ có được, không để lãng phí.
tân gia|Dịp mừng về nhà mới, thường có bữa tiệc mời người thân, bạn bè.
tận hưởng|Vui hưởng trọn vẹn niềm vui, điều tốt đẹp.
tận mắt|Chính mắt mình nhìn thấy, không qua người khác.
tần số|Số lần lặp lại của một hiện tượng trong một đơn vị thời gian.
tận tay|Đưa trực tiếp tới tay người nhận.
tận tâm|Hết lòng, chu đáo với công việc hoặc mọi người.
tận tình|Hết lòng giúp đỡ, chu đáo và nhiệt tình.
tấn tới|Tiến bộ, ngày càng khá hơn trong học tập hay công việc.
tân trang|Sửa sang, làm cho đồ vật hoặc nhà cửa trông mới lại.
tầng|Mỗi lớp của một ngôi nhà cao; cũng chỉ các lớp chồng lên nhau.
tầng hầm|Phần nhà xây chìm dưới mặt đất, thường làm chỗ để xe.
tầng lớp|Nhóm người trong xã hội có cùng địa vị, hoàn cảnh.
tập dượt|Luyện đi luyện lại nhiều lần trước khi biểu diễn hay thi đấu.
tập đoàn|Tổ chức kinh doanh lớn, gồm nhiều công ty liên kết với nhau.
tập đọc|Môn học giúp học sinh nhỏ luyện đọc đúng và đọc hay.
tập hợp|Gom lại, tụ lại một chỗ; cũng chỉ một nhóm gồm nhiều thứ.
tập huấn|Học và rèn luyện ngắn ngày để nắm vững kỹ năng, nghiệp vụ.
tập luyện|Rèn luyện thường xuyên để giỏi hơn, khỏe hơn.
tấp nập|Đông người qua lại, nhộn nhịp và sôi động.
tập quán|Thói quen, nếp sống lâu đời của một cộng đồng.
tập sự|Làm thử một thời gian để học việc trước khi chính thức.
tập thể|Nhóm người cùng sinh hoạt hoặc làm việc chung với nhau.
tập vở|Các loại vở, sổ dùng để ghi chép, học bài của học sinh.
tất bật|Bận rộn, vội vã lo nhiều việc cùng một lúc.
tất cả|Toàn bộ, không sót người hay vật nào.
tất nhiên|Đương nhiên, chắc chắn phải như vậy, không có gì lạ.
tất niên|Dịp cuối năm, thường có bữa tiệc liên hoan tiễn năm cũ.
tật xấu|Thói quen không tốt, cần sửa bỏ.
tây bắc|Hướng nằm giữa phía tây và phía bắc.
tây nam|Hướng nằm giữa phía tây và phía nam.
tẩy rửa|Làm sạch vết bẩn bằng nước và chất tẩy.
tẩy trang|Lau sạch lớp phấn son trang điểm trên mặt.
tẻ ngắt|Buồn tẻ, chẳng có gì vui hay thú vị.
tẻ nhạt|Buồn tẻ, nhàm chán, không có gì hấp dẫn.
tem thư|Mẩu giấy nhỏ in hình, dán lên phong bì để trả cước gửi thư.
tệ bạc|Đối xử tệ, không có tình nghĩa với người từng tốt với mình.
tế bào|Đơn vị nhỏ nhất cấu tạo nên cơ thể sinh vật.
tê giác|Thú lớn da dày, có một hoặc hai sừng trên mũi.
tệ hại|Rất xấu, rất kém, gây hậu quả không tốt.
tế nhị|Khéo léo, ý tứ trong lời nói và cách cư xử.
tê tê|Thú nhỏ có vảy cứng phủ khắp mình, ăn kiến, hay cuộn tròn lại.
tên gọi|Từ dùng để gọi một người, một vật hay một nơi.
tên riêng|Cái tên đặt cho riêng một người, một nơi, thường viết hoa.
tên sách|Tên gọi in trên bìa của một cuốn sách.
tên thật|Họ tên khai sinh thật sự, không phải biệt danh hay nghệ danh.
tên tuổi|Họ tên và tuổi của một người; cũng chỉ danh tiếng, tiếng tăm.
thả bộ|Đi bộ thong thả, chậm rãi để thư giãn.
thả ga|Thoải mái, tha hồ làm gì đó mà không cần giữ gìn hay hạn chế.
tha hồ|Được thoải mái làm theo ý thích, không bị giới hạn.
thà là|Chọn điều này còn hơn phải chịu điều kia.
thả lỏng|Để cơ thể hoặc tinh thần thư giãn, không căng thẳng; cũng là nới lỏng ra.
tha lỗi|Bỏ qua, không trách phạt lỗi lầm của người khác.
thà rằng|Dùng để nói chọn cách này còn hơn cách kia, dù không thật sự muốn.
thả sức|Được tự do làm điều mình thích, không bị gò bó.
tha thứ|Không còn để bụng lỗi lầm của ai, bỏ qua và cho họ cơ hội.
thác|Chỗ dòng nước từ trên cao đổ mạnh xuống.
thạch|Món tráng miệng mềm và trong, nấu từ rau câu hoặc bột, ăn mát lạnh.
thạch anh|Loại khoáng vật cứng, thường trong suốt, dùng làm trang sức, đồng hồ.
thạch cao|Chất khoáng màu trắng, dùng làm trần nhà, tượng và khuôn đúc.
thạch đen|Món thạch màu đen nấu từ cây sương sáo, ăn mát.
thạch sùng|Con vật nhỏ giống thằn lằn, hay bám trên tường nhà để bắt muỗi, côn trùng.
thách thức|Khó khăn lớn cần vượt qua; cũng là thách người khác làm điều gì.
thái|Cắt thịt, rau củ thành từng lát mỏng hoặc sợi nhỏ.
thái độ|Cách nghĩ, cách cư xử thể hiện ra bên ngoài với người hoặc việc.
thái quá|Quá mức bình thường, vượt quá chừng mực.
thảm|Tấm dệt dày trải trên sàn để trang trí hay lau chân; cũng chỉ tình cảnh rất tệ.
tham chiếu|Xem và đối chiếu với tài liệu khác để làm căn cứ.
tham dự|Có mặt và góp phần vào một buổi lễ, cuộc họp, cuộc thi.
thảm đỏ|Tấm thảm màu đỏ trải lối đi để đón khách quý ở các sự kiện lớn.
tham gia|Cùng góp mặt, góp sức vào một hoạt động hay tổ chức.
thám hiểm|Đi đến nơi xa lạ, khó khăn để tìm hiểu, khám phá.
tham khảo|Xem thêm tài liệu, ý kiến khác để học hỏi, đối chiếu.
tham lam|Muốn có thật nhiều cho riêng mình, không biết thế nào là đủ.
thám tử|Người chuyên điều tra, tìm manh mối để làm sáng tỏ sự việc.
tham vọng|Ước muốn đạt được những điều lớn lao như quyền lực, danh vọng.
than|Chất đen dùng làm nhiên liệu đốt; cũng là kêu ca, phàn nàn.
than củi|Củi gỗ được đốt âm ỉ cho thành cục đen, dùng để nướng, đun nấu.
than đá|Khoáng chất màu đen đào từ mỏ dưới lòng đất, dùng làm chất đốt.
thản nhiên|Bình thản, không tỏ ra lo lắng hay bối rối.
than phiền|Kêu ca, phàn nàn vì không hài lòng.
than thở|Nói ra nỗi buồn, nỗi khổ của mình cho người khác nghe.
than vãn|Kêu ca, kể lể mãi về những điều không vừa ý.
thang|Dụng cụ có nhiều bậc ngang, dùng để trèo lên xuống chỗ cao.
tháng ba|Tháng thứ ba trong năm, sau tháng hai.
tháng bảy|Tháng thứ bảy của năm, nằm giữa tháng sáu và tháng tám.
tháng chạp|Tháng mười hai, tháng cuối cùng của năm âm lịch.
tháng chín|Tháng thứ chín trong năm, mùa tựu trường của học sinh.
tháng giêng|Tháng đầu tiên theo âm lịch, mở đầu bằng Tết Nguyên đán.
tháng hai|Tháng thứ hai trong năm, ngắn nhất, chỉ có 28 hoặc 29 ngày.
thang máy|Buồng chở người, hàng hóa lên xuống các tầng của tòa nhà.
tháng một|Tháng đầu tiên của năm dương lịch; theo âm lịch là tháng thứ mười một.
tháng mười|Tháng thứ mười trong năm, sau tháng chín.
tháng năm|Tháng thứ năm trong năm; cũng chỉ quãng thời gian dài đã qua.
tháng ngày|Khoảng thời gian dài đã sống, đã trải qua.
tháng sáu|Tháng thứ sáu trong năm, lúc học sinh bắt đầu nghỉ hè.
tháng tám|Tháng thứ tám trong năm; rằm tháng tám âm lịch là Tết Trung thu.
tháng tư|Tháng thứ tư trong năm, sau tháng ba.
thành|Tường cao bao bọc để bảo vệ một nơi; cũng có nghĩa là trở nên, biến thành.
thanh bình|Yên ổn và êm đềm, cuộc sống không xáo trộn.
thành công|Đạt được kết quả như mong muốn.
thành đạt|Đạt được thành công và có chỗ đứng vững vàng trong sự nghiệp.
thành khẩn|Thật lòng và chân thành, nhất là khi nhận lỗi.
thành kiến|Cách nhìn định sẵn, thường không tốt và khó thay đổi về người hay việc gì.
thành lập|Lập nên một tổ chức, công ty, câu lạc bộ mới.
thanh lịch|Trang nhã, lịch sự trong cách ăn mặc, nói năng.
thanh long|Quả vỏ đỏ hồng có tai xanh, ruột trắng hoặc đỏ, lấm tấm hạt đen nhỏ.
thành ngữ|Cụm từ cố định quen dùng, mang nghĩa bóng, như nước đổ lá khoai.
thanh nhạc|Nghệ thuật ca hát, sử dụng giọng hát của con người.
thanh niên|Người trẻ đã trưởng thành, đang ở độ tuổi sung sức.
thành phẩm|Sản phẩm đã làm xong, sẵn sàng để sử dụng hoặc bán.
thành phần|Những phần, những chất cùng tạo nên một tổng thể.
thành phố|Khu đô thị lớn, đông dân, nhiều nhà cửa và hoạt động buôn bán.
thành quả|Kết quả tốt có được nhờ công sức bỏ ra.
thành ra|Dẫn đến kết quả là, vì thế mà.
thanh thản|Nhẹ nhõm, yên ổn trong lòng, không lo nghĩ.
thành thạo|Giỏi và quen tay, làm việc gì cũng trơn tru.
thành thật|Ngay thẳng, nói đúng điều mình nghĩ, không giả dối.
thành thị|Vùng thành phố, thị xã đông dân, trái với nông thôn.
thảnh thơi|Nhàn nhã, thoải mái, không bận rộn hay lo nghĩ.
thành tích|Kết quả tốt đạt được trong học tập, công việc, thể thao.
thanh toán|Trả tiền cho hàng hóa, dịch vụ hoặc khoản nợ.
thành tựu|Kết quả lớn đạt được sau quá trình nỗ lực lâu dài.
thành viên|Người thuộc về một nhóm, gia đình hay tổ chức.
thanh xuân|Quãng thời gian tuổi trẻ đẹp đẽ nhất của đời người.
tháo|Gỡ hoặc cởi ra những gì đang được lắp, buộc, đóng vào.
tháo dỡ|Gỡ bỏ, tách rời các bộ phận của một công trình hay máy móc.
tháo gỡ|Giải quyết khó khăn, vướng mắc; cũng là gỡ rời từng phần ra.
thảo luận|Cùng nhau trao đổi, bàn bạc ý kiến về một vấn đề.
thảo mộc|Cây cỏ nói chung, nhất là loại dùng làm thuốc, gia vị hay pha trà.
thảo nào|Từ nói khi chợt hiểu ra lý do của một việc, nghĩa như hèn chi, bảo sao.
thảo nguyên|Vùng đồng cỏ rộng lớn, bằng phẳng, ít cây to.
tháo rời|Gỡ ra thành từng bộ phận riêng lẻ.
thao tác|Các động tác, bước làm theo trình tự khi làm việc hoặc sử dụng máy móc.
thao thức|Trằn trọc, không ngủ được vì lo nghĩ hoặc mong nhớ.
tháp|Công trình kiến trúc cao, thon dần lên phía đỉnh.
tháp nước|Bồn chứa nước đặt trên chân đế cao để cấp nước cho cả khu vực.
thau|Chậu rộng miệng dùng để đựng nước, rửa, giặt.
thay đổi|Làm cho khác đi hoặc trở nên khác trước.
thay lông|Rụng lớp lông cũ và mọc lông mới, thường gặp ở chim, thú.
thay mặt|Đại diện, đứng ra nói hoặc làm thay cho người khác hay tập thể.
thay phiên|Lần lượt người này rồi người kia cùng làm một việc.
thay thế|Đưa người hay vật khác vào chỗ cũ để làm thay.
thắc mắc|Có điều chưa hiểu, muốn hỏi để được giải đáp.
thăm hỏi|Đến thăm hoặc hỏi han để bày tỏ sự quan tâm đến ai đó.
thăm nom|Đến thăm hỏi và chăm sóc người khác.
thăm thú|Đi đến nơi này nơi khác để xem, ngắm cảnh cho biết.
thằn lằn|Loài bò sát nhỏ, có bốn chân và đuôi dài, hay sống trong bụi cây.
thắng bại|Kết quả hơn thua cuối cùng của một cuộc thi đấu.
thăng bằng|Trạng thái giữ vững, không bị nghiêng ngả hay ngã.
thằng bé|Cách gọi thân mật một đứa con trai còn nhỏ.
thăng chức|Được đưa lên một chức vụ cao hơn trong công việc.
thắng cuộc|Giành chiến thắng trong một cuộc thi hay trò chơi.
thẳng đơ|Thẳng cứng ra, không cử động, không uốn cong.
thẳng đứng|Vuông góc với mặt đất, hướng từ dưới lên trên.
thẳng hàng|Xếp đều trên cùng một đường thẳng, không lệch.
thăng hoa|Chất rắn chuyển thẳng thành hơi; cũng chỉ lúc cảm hứng dâng cao.
thắng lợi|Kết quả tốt đẹp, đạt được mục tiêu sau khi cố gắng.
thẳng tắp|Rất thẳng, kéo dài một mạch không cong chút nào.
thẳng thừng|Nói thẳng ra, dứt khoát, không nể nang hay vòng vo.
thăng tiến|Tiến lên vị trí cao hơn trong công việc, sự nghiệp.
thẳng tính|Tính tình ngay thẳng, nghĩ sao nói vậy.
thăng trầm|Lúc lên lúc xuống, lúc thịnh lúc suy trong cuộc đời hay sự việc.
thắp sáng|Làm cho sáng lên bằng đèn, nến; cũng nghĩa là khơi dậy niềm hy vọng.
thắt chặt|Buộc cho thật chặt; cũng là làm cho gắn bó hoặc nghiêm ngặt hơn.
thắt lưng|Dây đeo ngang bụng để giữ quần; cũng chỉ phần eo của cơ thể.
thắt nút|Buộc dây lại thành nút cho chặt.
thẩm định|Xem xét kỹ để đánh giá chất lượng, giá trị hay tính đúng đắn.
thầm lặng|Lặng lẽ, âm thầm, không phô trương cho người khác biết.
thâm nhập|Đi sâu vào bên trong một nơi hay một lĩnh vực để tìm hiểu, hoạt động.
thâm niên|Số năm đã làm việc trong một nghề hay ở một nơi.
thẩm thấu|Chất lỏng ngấm dần qua một lớp màng; cũng chỉ việc tiếp thu, thấm dần.
thầm thì|Nói nhỏ nhẹ, chỉ đủ cho người bên cạnh nghe thấy.
thấm thía|Hiểu và cảm nhận sâu sắc, như thấm vào tận lòng.
thần bí|Bí ẩn, khó hiểu, như ẩn chứa điều gì huyền diệu bên trong.
thần đồng|Đứa trẻ có tài năng đặc biệt, giỏi hơn hẳn so với tuổi.
thân hình|Hình dáng cơ thể con người, như cao, thấp, gầy, đầy đặn.
thân mật|Gần gũi, thân thiết và không khách sáo.
thân mến|Gần gũi và quý mến, hay dùng mở đầu thư gửi người quen.
thân mình|Phần cơ thể của người hay vật; cũng chỉ chính bản thân mình.
thân quen|Gần gũi và quen thuộc từ lâu.
thần thái|Vẻ toát ra từ gương mặt, ánh mắt và cử chỉ của một người.
thân thể|Toàn bộ cơ thể của con người.
thân thiện|Dễ gần, cởi mở và tử tế với mọi người.
thân thiết|Rất gần gũi, gắn bó với nhau.
thần thoại|Truyện kể xa xưa về các vị thần, anh hùng, giải thích nguồn gốc vạn vật.
thân thuộc|Gần gũi, quen thuộc như người trong nhà.
thần tiên|Các vị thần và tiên trong truyện cổ; cũng chỉ cảnh đẹp, sung sướng như cõi tiên.
thận trọng|Cẩn thận, suy nghĩ kỹ trước khi nói hoặc làm.
thần tượng|Người được hâm mộ say mê, như ca sĩ, diễn viên hay vận động viên nổi tiếng.
thân yêu|Gần gũi và hết mực yêu quý.
thấp bé|Có dáng người thấp và nhỏ con.
thập cẩm|Gồm nhiều thứ khác nhau trộn lẫn, như chè thập cẩm, bánh thập cẩm.
thập niên|Khoảng thời gian kéo dài mười năm liền nhau.
thập phân|Cách đếm theo cơ số mười, như trong số có phần lẻ sau dấu phẩy.
thấp thoáng|Lúc ẩn lúc hiện, khi thấy khi không, không rõ ràng.
thấp thỏm|Lo lắng, không yên lòng vì đang chờ đợi điều gì.
thật|Đúng với sự thực, không giả dối; cũng dùng để nhấn mạnh, nghĩa là rất.
thất bại|Không đạt được điều mong muốn, không thành công.
thất hứa|Không làm đúng như điều mình đã hứa.
thật là|Từ dùng để nhấn mạnh cảm xúc, nghĩa như quả thật, rất là.
thất lạc|Bị mất, không biết đang ở đâu, không tìm thấy.
thật lòng|Thành thật, xuất phát từ đáy lòng, không giả dối.
thật ra|Từ dùng khi nói ra sự thật, thường khác với điều người khác nghĩ.
thật sự|Đúng là như vậy, có thật chứ không giả; cũng dùng để nhấn mạnh.
thật tâm|Thật lòng, xuất phát từ tấm lòng chân thành.
thật thà|Ngay thẳng, không biết nói dối hay lừa lọc ai.
thất thường|Lúc thế này lúc thế khác, không theo một quy luật nào.
thật tình|Chân thành, đúng như lòng mình nghĩ; cũng dùng khi muốn nói thẳng.
thất vọng|Buồn vì điều mình mong đợi đã không xảy ra.
thấu hiểu|Hiểu rõ và sâu sắc tâm tư, hoàn cảnh của người khác.
thấy|Nhận biết được bằng mắt; cũng là cảm nhận hoặc nhận ra điều gì.
thầy cô|Những người dạy học, gồm cả thầy giáo và cô giáo.
thầy giáo|Người đàn ông làm nghề dạy học.
thầy trò|Người dạy và người học; cũng chỉ mối quan hệ gắn bó giữa hai bên.
thẻ đỏ|Tấm thẻ trọng tài giơ lên để buộc cầu thủ phạm lỗi nặng rời sân.
thẻ vàng|Tấm thẻ trọng tài giơ lên để nhắc nhở, cảnh cáo cầu thủ phạm lỗi.
thèm|Rất muốn ăn, uống hoặc có được điều gì đó.
thèm muốn|Ao ước, khao khát muốn có được điều gì đó.
thèm thuồng|Rất thèm, rất muốn được ăn hoặc có một thứ gì đó.
thẹn|Ngượng ngùng, xấu hổ trước người khác.
then chốt|Quan trọng nhất, giữ vai trò quyết định trong một việc.
thẹn thùng|Ngượng ngùng, e lệ, hay đỏ mặt trước người khác.
theo|Đi ở phía sau hoặc đi cùng ai; cũng là làm đúng như, dựa vào điều gì.
theo dõi|Chú ý quan sát thường xuyên để biết diễn biến của sự việc.
theo đuổi|Kiên trì hướng tới một mục tiêu, ước mơ; cũng là tìm cách chinh phục người mình thương.
theo kịp|Đuổi bằng được người đi trước; cũng là bắt nhịp, hiểu được cái mới.
theo như|Dựa vào, căn cứ vào lời nói hay tài liệu nào đó.
thép|Kim loại rất cứng và bền, làm từ sắt pha thêm một ít cacbon.
thét|Kêu, gào lên thật to và vang.
thế chấp|Dùng tài sản như nhà, đất để bảo đảm cho một khoản vay.
thể chất|Sức khỏe và sự phát triển của cơ thể.
thế chứ|Lời khen hoặc đồng tình, ý nói phải như vậy mới đúng, mới hay.
thể diện|Danh dự và hình ảnh của mình trước mặt người khác.
thể dục|Các bài tập vận động giúp cơ thể khỏe mạnh.
thế gian|Cõi đời, nơi con người đang sống.
thế giới|Toàn bộ trái đất cùng các nước và con người; cũng chỉ một lĩnh vực riêng.
thế hệ|Lớp người cùng độ tuổi, sống trong cùng một thời kỳ.
thể hiện|Bày tỏ, cho người khác thấy qua lời nói, hành động hoặc tác phẩm.
thể hình|Hình dáng cơ thể; cũng chỉ môn tập luyện cho cơ bắp săn chắc, cân đối.
thế là|Từ nối nói lên kết quả của việc vừa kể, giống như vậy là.
thể lệ|Những quy định đặt ra cho một cuộc thi hoặc hoạt động.
thể loại|Kiểu, dạng riêng của tác phẩm nghệ thuật như phim hành động, nhạc trẻ, truyện cười.
thể lực|Sức khỏe, sức mạnh và độ dẻo dai của cơ thể.
thế mà|Từ nối nêu điều trái với mong đợi, giống như vậy mà.
thế mạnh|Điểm mạnh, lợi thế hơn hẳn người khác hoặc nơi khác.
thế nào|Từ dùng để hỏi về cách thức, tình trạng hay tính chất của sự việc.
thế nhưng|Từ nối nêu ý trái ngược với ý trước, giống như nhưng mà.
thế rồi|Từ nối kể việc xảy ra tiếp theo, giống như sau đó.
thể thao|Các môn rèn luyện thân thể và thi đấu như bóng đá, bơi lội.
thế thì|Từ nối nêu kết luận từ điều vừa nói, giống như vậy thì.
thề thốt|Thề hứa đủ điều để người khác tin mình.
thể tích|Lượng không gian mà một vật chiếm chỗ, đo bằng lít hoặc mét khối.
thể xác|Phần thân thể con người, phân biệt với tinh thần, tâm hồn.
thêu|Dùng kim chỉ tạo hình, hoa văn trên vải.
thêu ren|Nghề thủ công dùng kim chỉ tạo hoa văn, đường viền trang trí trên vải.
thêu thùa|Công việc khâu thêu bằng kim chỉ nói chung, thường do người khéo tay làm.
thi công|Tiến hành xây dựng một công trình theo bản thiết kế.
thi cử|Các kỳ thi trong học tập nói chung.
thi đấu|Tranh tài với nhau trong một cuộc thi, nhất là thể thao.
thí điểm|Làm thử ở một phạm vi nhỏ trước khi áp dụng rộng rãi.
thi đua|Cùng nhau cố gắng, đua sức làm tốt hơn để đạt thành tích cao.
thị giác|Khả năng nhìn thấy bằng mắt, một trong năm giác quan.
thì giờ|Thời gian dành cho việc gì đó.
thị lực|Mức độ nhìn rõ của mắt, sức nhìn của mỗi người.
thí nghiệm|Làm thử để kiểm tra, quan sát một hiện tượng, nhất là trong khoa học.
thi nhau|Cùng đua nhau làm một việc, người này tiếp người kia.
thì ra|Hóa ra, lúc này mới vỡ lẽ là.
thí sinh|Người tham gia một kỳ thi hoặc cuộc thi.
thi tài|Cùng nhau trổ tài, so tài để xem ai giỏi hơn.
thì thào|Nói rất nhỏ, chỉ đủ người bên cạnh nghe.
thì thầm|Nói khẽ, nhỏ nhẹ vào tai nhau.
thi thoảng|Lâu lâu mới có một lần, không thường xuyên.
thi thử|Làm bài thi để làm quen, luyện tập trước kỳ thi thật.
thị thực|Giấy phép do một nước cấp để người nước ngoài được vào nước đó.
thị trấn|Khu dân cư nhỏ hơn thành phố, thường là trung tâm của một huyện.
thị trường|Nơi hoặc môi trường diễn ra việc mua bán hàng hóa.
thi tuyển|Kỳ thi để chọn ra người đủ điều kiện vào trường hay vào làm.
thị xã|Đô thị lớn hơn thị trấn nhưng nhỏ hơn thành phố.
thìa|Đồ dùng có cán và lòng nông để xúc thức ăn.
thìa canh|Loại thìa cỡ lớn để múc canh; cũng là đơn vị đong trong nấu ăn.
thích|Cảm thấy ưa, muốn gần hoặc muốn làm điều gì đó.
thích hợp|Phù hợp, đúng với yêu cầu hoặc hoàn cảnh.
thích nghi|Thay đổi để sống và phát triển được trong điều kiện mới.
thích thú|Cảm thấy vui và hứng thú.
thích ứng|Điều chỉnh bản thân cho hợp với hoàn cảnh, môi trường mới.
thiếc|Kim loại màu trắng bạc, mềm, dễ nóng chảy, thường dùng để hàn.
thiện|Tốt lành, hay làm điều tốt cho người khác, trái với ác.
thiện cảm|Tình cảm tốt, ấn tượng dễ chịu đối với ai đó.
thiên hà|Hệ thống khổng lồ gồm hàng tỉ ngôi sao, như dải Ngân Hà.
thiên nga|Chim lớn cổ dài, lông thường trắng, bơi lượn duyên dáng trên mặt hồ.
thiên nhiên|Toàn bộ núi sông, cây cỏ, muông thú có sẵn, không do con người làm ra.
thiên tài|Tài năng đặc biệt xuất sắc, hơn hẳn người thường; cũng chỉ người có tài đó.
thiên thạch|Khối đá từ ngoài vũ trụ bay vào và rơi xuống Trái Đất.
thiên văn|Ngành khoa học nghiên cứu các vì sao, hành tinh và vũ trụ.
thiêng liêng|Cao quý và đáng trân trọng hết mực, như tình cảm gia đình, quê hương.
thiệp|Tấm bìa trang trí đẹp, ghi lời mời hay lời chúc mừng.
thiệt|Bị mất phần, chịu thua kém; trong tiếng miền Nam cũng có nghĩa là thật.
thiết bị|Máy móc, dụng cụ dùng cho một công việc nhất định.
thiết kế|Lên ý tưởng, vẽ mẫu trước khi làm ra một sản phẩm, công trình.
thiết lập|Gây dựng nên một điều mới; cũng là cài đặt chế độ cho máy móc, điện thoại.
thiệt thòi|Chịu phần kém hơn, mất mát so với người khác.
thiết thực|Có ích thật sự, sát với nhu cầu thực tế.
thiết yếu|Rất cần thiết, không thể thiếu cho cuộc sống hằng ngày.
thiếu|Không đủ so với mức cần có; cũng là không có, vắng mặt.
thiếu hụt|Bị hụt đi, không đủ so với số lượng cần có.
thiếu nhi|Trẻ em nói chung, nhất là các em ở tuổi đi học.
thiếu niên|Người đang ở tuổi mới lớn, lớn hơn nhi đồng nhưng chưa thành thanh niên.
thiếu nữ|Cô gái trẻ ở độ tuổi mới lớn, chưa lập gia đình.
thím|Vợ của chú, tức vợ của em trai bố.
thính|Nghe hoặc ngửi rất nhạy; cũng là bột gạo rang thơm dùng làm nem, làm mồi câu.
thính giả|Người nghe đài, nghe nhạc hoặc nghe nói chuyện.
thính giác|Khả năng nghe được âm thanh bằng tai.
thịnh hành|Được nhiều người ưa chuộng, phổ biến rộng rãi trong một thời gian.
thình lình|Bất ngờ, đột ngột, không báo trước.
thình thịch|Tiếng đập mạnh và liên tiếp, như tim đập hay tiếng bước chân nặng.
thỉnh thoảng|Lâu lâu mới có một lần, không thường xuyên.
thịnh vượng|Giàu có, phát triển mạnh mẽ và sung túc.
thịt|Phần nạc và mỡ của con vật như lợn, bò, gà, dùng để nấu ăn.
thịt băm|Phần thịt đã được băm hoặc xay nhỏ, dùng làm nhân, nấu canh hay rán.
thịt kho|Món thịt nấu với nước mắm, đường cho đậm và mềm.
thịt nạc|Phần thịt đỏ, không có mỡ.
thịt nướng|Món thịt được nướng chín trên than hoặc lửa, thơm và ngon.
thịt quay|Món thịt heo được quay chín vàng, lớp da giòn rụm.
thịt thăn|Phần thịt nạc mềm nằm dọc hai bên sống lưng con vật.
thỏ rừng|Loài thỏ sống hoang dã trong rừng, chạy rất nhanh.
thoa|Bôi nhẹ một lớp mỏng lên da hoặc bề mặt, như kem, dầu.
thoải mái|Dễ chịu, thư thái, không bị gò bó.
thoáng|Rộng rãi, có gió lùa mát mẻ; cũng là lướt qua rất nhanh trong chốc lát.
thoáng đãng|Rộng rãi, mát mẻ, không bị che chắn.
thoáng khí|Có không khí lưu thông dễ dàng, không bị bí hơi.
thoáng qua|Lướt qua rất nhanh, chỉ thấy hoặc cảm nhận trong chốc lát.
thoang thoảng|Mùi hương nhẹ, lúc có lúc không, chỉ thoảng qua.
thoát|Ra khỏi được nơi hoặc tình cảnh khó khăn, nguy hiểm.
thoát hiểm|Ra khỏi nơi nguy hiểm một cách an toàn và kịp thời.
thoát khỏi|Ra được khỏi nơi gò bó hay tình cảnh khó khăn.
thóc|Hạt lúa còn nguyên vỏ trấu.
thóc gạo|Lúa và gạo nói chung, lương thực chính hằng ngày.
thóc lúa|Hạt lúa chưa xay; cũng chỉ lương thực nói chung.
thói quen|Việc làm lặp lại nhiều lần thành nếp, khó bỏ.
thon thả|Dáng người mảnh mai, gọn gàng và cân đối.
thong thả|Chậm rãi, ung dung, không vội vàng.
thô lỗ|Cư xử cộc cằn, thiếu lịch sự.
thô sơ|Đơn giản, làm chưa khéo, chưa có kỹ thuật hiện đại.
thổi|Đẩy hơi mạnh ra từ miệng, hoặc gió lùa qua; cũng có nghĩa là nấu cơm.
thôi miên|Đưa người vào trạng thái nửa tỉnh nửa mê để gợi ý; cũng chỉ sức cuốn hút mãnh liệt.
thôi nôi|Lễ mừng em bé tròn một tuổi, thường có trò cho bé bốc đồ vật.
thổi phồng|Bơm hơi cho căng to lên; cũng nghĩa là nói quá so với sự thật.
thôi thì|Đành chấp nhận như vậy, dùng khi đổi ý hay chịu nhượng bộ.
thôi thúc|Giục giã từ bên trong, khiến mình muốn làm ngay điều gì.
thôn|Khu dân cư nhỏ ở nông thôn, thuộc một xã, như làng.
thôn quê|Vùng làng mạc, đồng ruộng ở nông thôn.
thông|Cây gỗ cao có lá hình kim, quả hình nón; cũng là đi qua được, không bị tắc.
thông báo|Báo cho mọi người biết một tin, một việc.
thông cảm|Hiểu và chia sẻ với hoàn cảnh, cảm xúc của người khác.
thông cáo|Văn bản thông báo chính thức cho mọi người cùng biết.
thông dụng|Được dùng phổ biến, rộng rãi.
thông điệp|Lời nhắn hoặc ý tưởng mà ai đó muốn gửi gắm tới người khác.
thông gia|Hai gia đình trở thành họ hàng nhờ con cái kết hôn với nhau.
thông gió|Làm cho không khí lưu thông, gió ra vào dễ dàng.
thông hơi|Giúp hơi nóng, khí bên trong thoát ra ngoài dễ dàng.
thống kê|Thu thập, đếm và sắp xếp số liệu để tìm hiểu một vấn đề.
thông minh|Nhanh hiểu, nhạy bén và biết xử lý vấn đề giỏi.
thống nhất|Hợp lại thành một khối; cũng là đồng ý với nhau, có chung ý kiến.
thông qua|Chấp thuận một quyết định sau khi xem xét; cũng có nghĩa là qua, nhờ vào.
thông số|Các con số cho biết đặc điểm, tính năng của máy móc, thiết bị.
thông suốt|Không bị ách tắc, đi lại dễ dàng; cũng là hiểu rõ và đồng tình.
thông thái|Hiểu biết rộng và sâu về nhiều lĩnh vực.
thông thạo|Hiểu biết rõ và sử dụng giỏi, như một ngôn ngữ hay một vùng đất.
thông thoáng|Rộng rãi và mát, không bị bít kín; cũng chỉ thủ tục dễ dàng, đơn giản.
thông thường|Bình thường, hay gặp, không có gì đặc biệt.
thông tin|Những tin tức, hiểu biết được truyền đạt cho người khác.
thơ ấu|Quãng đời còn nhỏ tuổi, lúc còn là trẻ con.
thơ ca|Các tác phẩm văn chương có vần điệu như thơ, ca dao nói chung.
thở dài|Đẩy ra một hơi thở dài, thường khi buồn, mệt hoặc chán nản.
thở dốc|Hít thở gấp và mạnh, thường sau khi chạy hay làm việc nặng.
thợ điện|Người làm nghề lắp đặt và sửa chữa đường dây, thiết bị điện.
thợ hàn|Người làm nghề nối các tấm kim loại lại với nhau bằng nhiệt.
thợ lặn|Người làm nghề lặn sâu dưới nước để làm việc hay tìm kiếm.
thợ may|Người làm nghề cắt và may quần áo.
thợ mỏ|Người làm việc khai thác than, quặng trong hầm mỏ.
thợ mộc|Người làm nghề đóng đồ gỗ như bàn, ghế, tủ, giường.
thơ mộng|Đẹp nhẹ nhàng, gợi cảm xúc lãng mạn như trong thơ.
thơ ngây|Trong sáng, hồn nhiên, chưa hiểu nhiều về cuộc đời.
thờ ơ|Lạnh nhạt, không quan tâm, không để ý đến.
thở phào|Thở ra một hơi dài nhẹ nhõm khi hết lo lắng.
thở ra|Đẩy hơi từ trong phổi ra ngoài qua mũi hoặc miệng.
thợ rèn|Người làm nghề nung nóng sắt rồi đập thành nông cụ, đồ dùng.
thợ sơn|Người làm nghề sơn tường, nhà cửa hoặc đồ vật.
thơ văn|Thơ và văn, các tác phẩm văn chương nói chung.
thời buổi|Giai đoạn đang sống, với những đặc điểm riêng của nó.
thời cơ|Lúc thuận lợi để làm một việc gì đó.
thời đại|Một giai đoạn dài trong lịch sử có đặc điểm riêng.
thời điểm|Một lúc, một mốc thời gian xác định nào đó.
thời gian|Sự trôi qua liên tục của giây phút, ngày tháng; cũng chỉ một khoảng lâu hay mau.
thời giờ|Khoảng thời gian dành cho một việc gì đó.
thời hạn|Khoảng thời gian được định sẵn để hoàn thành việc gì.
thời khắc|Một thời điểm cụ thể, thường là lúc quan trọng, đáng nhớ.
thời lượng|Độ dài thời gian dành cho một chương trình, bài học hay hoạt động.
thời nay|Giai đoạn hiện nay, ngày nay, khác với ngày xưa.
thời sự|Tin tức về các sự kiện mới xảy ra trong nước và thế giới.
thời tiết|Tình trạng nắng, mưa, nóng, lạnh của bầu trời ở một nơi và lúc nhất định.
thời trang|Kiểu ăn mặc được nhiều người ưa chuộng trong một thời gian.
thời xưa|Những năm tháng đã qua từ rất lâu, ngày trước.
thơm|Có mùi dễ chịu, dễ ngửi; ở miền Nam còn là tên gọi quả dứa.
thơm lừng|Thơm nồng, mùi hương lan tỏa ra khắp xung quanh.
thơm ngát|Thơm dịu và lan xa, thường nói về hương hoa.
thơm phức|Thơm đậm và hấp dẫn, nhất là mùi đồ ăn vừa nấu xong.
thơm tho|Có mùi thơm dễ chịu, sạch sẽ và tươi mát.
thớt|Tấm gỗ hoặc nhựa dày để kê khi thái, chặt thức ăn.
thu chi|Các khoản tiền nhận vào và tiền tiêu ra.
thủ công|Làm bằng tay, không dùng máy móc; cũng là môn học làm đồ bằng tay.
thu dọn|Dọn dẹp, cất gọn đồ đạc cho ngăn nắp.
thú dữ|Loài thú hoang hung tợn như hổ, báo, sư tử.
thủ đô|Thành phố chính của một nước, nơi đặt các cơ quan đầu não của nhà nước.
thụ động|Không tự chủ động, chỉ làm khi có người khác bảo hoặc tác động.
thu gom|Nhặt nhạnh từ nhiều nơi về một chỗ, như rác, phế liệu.
thu gọn|Làm cho gọn lại, chiếm ít chỗ hơn hoặc ngắn hơn.
thu hẹp|Làm cho hẹp lại, giảm bớt phạm vi hoặc khoảng cách.
thu hoạch|Gặt hái nông sản khi đến mùa; cũng chỉ điều học hỏi được.
thu hồi|Lấy lại cái đã đưa ra, đã phát hành hoặc cho mượn.
thu hút|Lôi cuốn, làm người khác chú ý, muốn đến gần.
thủ khoa|Người đỗ đầu, đạt điểm cao nhất trong một kỳ thi.
thủ môn|Cầu thủ đứng trong khung thành để bắt và chặn bóng.
thu mua|Mua gom hàng hóa, nông sản để bán lại hoặc chế biến.
thu ngân|Việc nhận tiền thanh toán của khách tại quầy; cũng chỉ người làm việc đó.
thu nhặt|Nhặt nhạnh từng thứ một rồi gom lại với nhau.
thú nhận|Nói ra, thừa nhận điều mình đã làm hoặc đã giấu, thường là lỗi lầm.
thu nhập|Tiền kiếm được từ công việc, buôn bán trong một thời gian.
thu nhỏ|Làm cho kích thước nhỏ đi so với ban đầu, như mô hình hay hình ảnh.
thu thập|Tìm và gom lại thông tin, tài liệu, đồ vật.
thú thật|Nói thật lòng, thừa nhận điều mình nghĩ hoặc vẫn giấu kín.
thủ thỉ|Nói nhỏ nhẹ, tâm tình bên tai một cách thân mật.
thủ thuật|Mẹo, cách làm khéo léo để giải quyết việc gì nhanh và hiệu quả.
thủ thư|Người trông coi, quản lý sách và phục vụ bạn đọc trong thư viện.
thủ tục|Các bước, giấy tờ cần làm theo quy định để giải quyết một việc.
thủ vai|Đóng một vai diễn trong phim hoặc vở kịch.
thú vật|Các loài động vật, nhất là loài có bốn chân và có lông.
thú vui|Việc làm mang lại niềm vui, sự thích thú trong lúc rảnh rỗi.
thua|Bị kém hơn, không giành được phần thắng.
thua kém|Không bằng người khác về mặt nào đó.
thua lỗ|Làm ăn bị mất tiền, tiền thu về ít hơn vốn bỏ ra.
thuận|Xuôi theo, không bị cản trở; cũng là đồng ý, bằng lòng.
thuận lợi|Có điều kiện tốt, dễ dàng để làm việc gì.
thuận tay|Quen dùng một bên tay hơn bên kia; cũng là nhân tiện làm luôn.
thuần thục|Làm rất thạo, nhuần nhuyễn nhờ luyện tập nhiều.
thuận tiện|Dễ dàng, tiện lợi, không gặp trở ngại.
thuật ngữ|Từ ngữ chuyên dùng trong một ngành, một lĩnh vực.
thuật toán|Dãy các bước rõ ràng để giải một bài toán, nhất là trên máy tính.
thuê|Trả tiền để được dùng tạm đồ của người khác hoặc nhờ người làm việc.
thuê bao|Người đăng ký dùng một dịch vụ trả phí, như điện thoại, truyền hình.
thuê mướn|Trả tiền để dùng người làm hoặc dùng đồ vật, nhà cửa một thời gian.
thùng|Đồ chứa lớn có thành cao, bằng gỗ, nhựa hoặc kim loại.
thung lũng|Vùng đất thấp nằm giữa các dãy núi, đồi.
thùng rác|Đồ đựng rác thải, đặt trong nhà hoặc ở nơi công cộng.
thùng thư|Hộp đặt trước nhà để nhận thư, hoặc ở bưu điện để gửi thư đi.
thùng xe|Khoang phía sau của xe tải hay ô tô, dùng để chở hàng, chứa đồ.
thuộc lòng|Nhớ kỹ đến mức đọc lại được mà không cần nhìn.
thuốc nhuộm|Chất có màu dùng để nhuộm vải, tóc hay đồ vật.
thuộc tính|Đặc điểm vốn có của một sự vật, giúp phân biệt nó với cái khác.
thụt lùi|Lùi lại phía sau; cũng chỉ việc kém đi, không tiến bộ.
thút thít|Khóc nhỏ, khe khẽ và ngắt quãng từng tiếng.
thuyền|Phương tiện nhỏ đi trên mặt nước, chạy bằng chèo, buồm hoặc máy.
thuyền bè|Các loại thuyền, bè đi lại trên sông nước nói chung.
thuyền buồm|Loại thuyền có cánh buồm, đi được nhờ sức gió.
thuyền máy|Loại thuyền gắn động cơ, chạy bằng máy thay cho chèo.
thuyền rồng|Thuyền có đầu và đuôi trang trí hình rồng, dùng trong lễ hội hay chở khách.
thuyền trưởng|Người chỉ huy cao nhất trên một con tàu, thuyền.
thuyền viên|Người làm việc trên tàu thuyền, dưới quyền thuyền trưởng.
thuyết minh|Giới thiệu, giải thích cho người nghe hiểu; cũng là đọc lời thoại dịch cho phim.
thuyết phục|Dùng lý lẽ để làm người khác tin và đồng ý theo mình.
thuyết trình|Trình bày một vấn đề trước nhiều người, thường kèm hình ảnh minh họa.
thứ ba|Ngày trong tuần, sau thứ hai và trước thứ tư; cũng chỉ vị trí số ba.
thứ bảy|Ngày trong tuần đứng sau thứ sáu và trước chủ nhật.
thứ hai|Ngày đầu của tuần làm việc, sau chủ nhật; cũng chỉ vị trí số hai.
thứ hạng|Vị trí xếp hạng cao hay thấp so với người hoặc đội khác.
thứ lỗi|Tha thứ, bỏ qua lỗi lầm cho người khác.
thư mục|Ngăn dùng để chứa và sắp xếp tệp tin trong máy tính; cũng là danh sách sách, tài liệu.
thứ năm|Ngày trong tuần, sau thứ tư và trước thứ sáu; cũng chỉ vị trí số năm.
thử nghiệm|Làm thử để kiểm tra kết quả trước khi áp dụng rộng rãi.
thư pháp|Nghệ thuật viết chữ đẹp bằng bút lông, thường thấy vào dịp Tết.
thứ sáu|Ngày trong tuần, sau thứ năm và trước thứ bảy; cũng chỉ vị trí số sáu.
thử sức|Tham gia làm thử để xem khả năng của mình đến đâu.
thư tay|Lá thư viết tay hoặc nhờ người cầm đưa tận nơi.
thư thả|Ung dung, chậm rãi, không vội vàng hay gấp gáp.
thử thách|Khó khăn đặt ra để kiểm tra ý chí, năng lực của con người.
thứ tư|Ngày trong tuần, sau thứ ba và trước thứ năm; cũng chỉ vị trí số bốn.
thư viện|Nơi lưu giữ sách báo để mọi người đọc và mượn.
thừa hưởng|Được nhận lại tài sản, tính cách hay truyền thống từ người đi trước.
thừa nhận|Công nhận một điều là đúng hoặc có thật, kể cả lỗi của mình.
thừa sức|Có dư khả năng để làm được một việc.
thừa thãi|Có nhiều hơn mức cần thiết đến mức dư ra.
thưa thớt|Ít và cách xa nhau, không dày đặc.
thức|Ở trạng thái không ngủ, còn tỉnh táo; cũng là dậy sau khi ngủ.
thức ăn|Những thứ dùng để ăn, nuôi sống cơ thể.
thực chất|Bản chất thật bên trong của sự việc, không phải vẻ bề ngoài.
thức dậy|Tỉnh giấc và ra khỏi giường sau khi ngủ.
thực dụng|Chỉ coi trọng lợi ích thiết thực trước mắt.
thực đơn|Danh sách các món ăn, đồ uống của bữa ăn hoặc nhà hàng.
thức giấc|Tỉnh dậy sau giấc ngủ, có khi giữa chừng.
thực hành|Làm thật để áp dụng điều đã học vào việc cụ thể.
thực hiện|Làm cho một kế hoạch, ý tưởng hay lời hứa trở thành sự thật.
thực hư|Cái thật và cái giả của một sự việc, lời đồn.
thực khách|Người đến ăn uống ở nhà hàng, quán ăn.
thực lực|Khả năng, sức mạnh thật sự của một người hay tập thể.
thực phẩm|Các loại đồ ăn như thịt, cá, rau, dùng để nấu nướng.
thực ra|Từ mở đầu để nói lên sự thật, có khi trái với điều vừa tưởng.
thực sự|Có thật, đúng như vậy; cũng dùng để nhấn mạnh mức độ, nghĩa là rất.
thực tại|Những gì đang thực sự tồn tại và diễn ra ở hiện tại.
thực tập|Làm việc thực tế một thời gian để học hỏi và áp dụng kiến thức.
thực tế|Những điều có thật trong cuộc sống; cũng chỉ cách nghĩ sát với đời sống, không viển vông.
thực thể|Cái tồn tại có thật và độc lập, như một vật hay một tổ chức.
thực thi|Đưa luật lệ, kế hoạch hay mệnh lệnh vào thực hiện.
thực thụ|Đúng nghĩa, có đầy đủ tư cách và năng lực, không phải tạm thời.
thực tiễn|Hoạt động và đời sống thực tế, phân biệt với lý thuyết.
thực tình|Đúng như trong lòng mình nghĩ, thành thật, không giả vờ.
thức uống|Các loại nước để uống như nước ngọt, trà, sinh tố.
thực vật|Các loài cây cỏ, rong rêu, sống nhờ ánh sáng, nước và đất.
thước|Dụng cụ có vạch chia, dùng để đo độ dài hoặc kẻ đường thẳng.
thước cuộn|Dụng cụ đo có lá thép mỏng cuộn trong hộp, kéo ra để đo chiều dài.
thước dây|Dụng cụ đo bằng dải vải hoặc nhựa mềm, thường dùng khi may quần áo.
thược dược|Loài hoa có nhiều cánh xếp tầng, nhiều màu, hay được trồng dịp Tết.
thước đo|Dụng cụ dùng để đo; cũng chỉ tiêu chuẩn để đánh giá một điều gì đó.
thước kẻ|Dụng cụ thẳng, có vạch chia, dùng để kẻ đường thẳng và đo độ dài.
thương|Yêu mến, quý và quan tâm đến ai; cũng là cảm thấy tội nghiệp cho ai.
thương cảm|Cảm thấy xót xa, thông cảm với nỗi khổ của người khác.
thường dân|Người dân bình thường, không giữ chức vụ hay quyền lực gì.
thương gia|Người làm nghề buôn bán, kinh doanh, thường ở quy mô lớn.
thương hại|Cảm thấy tội nghiệp cho người gặp cảnh khó khăn, đáng thương.
thường lệ|Như mọi khi, theo thói quen hay quy định vẫn làm từ trước.
thương lượng|Bàn bạc, trao đổi với nhau để đi đến thỏa thuận chung.
thượng lưu|Tầng lớp giàu có, địa vị cao trong xã hội; cũng là đoạn đầu nguồn của con sông.
thương mại|Hoạt động mua bán, trao đổi hàng hóa và dịch vụ.
thương mến|Có tình cảm yêu thương và quý mến dành cho ai đó.
thường ngày|Diễn ra hằng ngày, quen thuộc trong cuộc sống bình thường.
thương nhân|Người làm nghề buôn bán, kinh doanh hàng hóa.
thương nhớ|Nhớ nhung da diết người hoặc nơi mình yêu quý.
thường niên|Diễn ra đều đặn mỗi năm một lần.
thưởng thức|Ăn, nghe hoặc xem chậm rãi để cảm nhận cái ngon, cái hay.
thường thường|Hay xảy ra, phần lớn các lần; cũng chỉ mức vừa phải, không nổi bật.
thường xuyên|Diễn ra nhiều lần, đều đặn và liên tục.
thương yêu|Yêu mến và quan tâm, chăm sóc hết lòng.
tỉa cành|Cắt bớt những cành thừa cho cây gọn và phát triển tốt.
tia sáng|Đường ánh sáng mảnh chiếu ra từ một nguồn sáng.
tía tô|Loại rau thơm có lá màu tím, dùng ăn sống hoặc nấu cháo.
tích|Kết quả của phép nhân; cũng có nghĩa là gom góp, dồn lại dần.
tích cực|Hăng hái, chủ động; cũng chỉ điều tốt, mang lại lợi ích.
tích hợp|Gộp nhiều phần, nhiều chức năng vào trong một thể thống nhất.
tích tắc|Tiếng kêu đều đều của đồng hồ; cũng chỉ khoảnh khắc rất ngắn.
tích trữ|Gom góp và cất giữ để dành dùng về sau.
tích tụ|Dồn lại dần dần qua thời gian thành nhiều hơn.
tiệc|Bữa ăn uống đông vui để mừng một dịp đặc biệt.
tiếc nuối|Buồn và tiếc vì điều tốt đẹp đã mất hoặc đã bỏ lỡ.
tiệc trà|Buổi gặp gỡ thân mật có uống trà, ăn bánh kẹo.
tiệc tùng|Các bữa tiệc, liên hoan ăn uống vui chơi nói chung.
tiệm|Cửa hàng nhỏ buôn bán hoặc làm dịch vụ.
tiềm ẩn|Ẩn giấu bên trong, chưa bộc lộ ra ngoài.
tiềm năng|Khả năng còn ẩn giấu, chưa được phát huy hết.
tiềm thức|Phần ý thức nằm sâu bên trong mà ta không nhận biết rõ.
tiền|Giấy bạc, đồng xu dùng để mua bán, trao đổi.
tiền bạc|Của cải bằng tiền nói chung, dùng để chi tiêu hằng ngày.
tiến bộ|Ngày càng tốt hơn, khá hơn so với trước.
tiền bối|Người đi trước, có nhiều kinh nghiệm hơn trong nghề hoặc lĩnh vực.
tiền cọc|Khoản đưa trước để giữ chỗ hoặc bảo đảm cho một giao dịch.
tiền công|Khoản trả cho người làm thuê để đổi lấy sức lao động.
tiền của|Của cải và tài sản có giá trị nói chung.
tiền cước|Tiền phải trả khi gửi hàng, vận chuyển hoặc dùng điện thoại.
tiện dụng|Dễ dùng, có ích và thuận tiện khi sử dụng.
tiền đạo|Cầu thủ chơi ở hàng trên cùng, có nhiệm vụ ghi bàn.
tiền đề|Điều kiện có trước, làm cơ sở cho một việc khác.
tiến độ|Mức nhanh chậm khi làm một công việc so với kế hoạch.
tiền giấy|Loại tiền in trên giấy hoặc nhựa, khác với tiền xu.
tiến hành|Bắt đầu làm và làm theo kế hoạch.
tiện ích|Lợi ích thiết thực, sự thuận tiện mà một thứ mang lại.
tiền lẻ|Những tờ bạc, đồng xu mệnh giá nhỏ, dùng để trả hay thối lại.
tiện lợi|Thuận tiện, giúp làm việc nhanh và dễ dàng hơn.
tiền lương|Khoản được trả theo tháng hoặc theo kỳ cho người làm việc.
tiền mặt|Tờ bạc và đồng xu cầm trong tay, khác với chuyển khoản hay thẻ.
tiện nghi|Các đồ dùng, thiết bị giúp cuộc sống thoải mái.
tiền nong|Các khoản chi tiêu, tiền bạc nói chung trong cuộc sống hằng ngày.
tiên nữ|Người con gái tiên rất xinh đẹp trong truyện cổ tích.
tiền nước|Khoản phải trả cho lượng nước đã dùng; cũng là tiền đồ uống.
tiên phong|Đi đầu, mở đường cho người khác theo sau.
tiền sử|Thời kỳ rất xa xưa của loài người, khi chưa có chữ viết.
tiền tài|Của cải, tiền bạc, thường gắn với sự giàu sang và danh lợi.
tiện tay|Nhân lúc đang làm thì làm luôn một việc khác.
tiền tệ|Đơn vị tiền chính thức được dùng ở một nước, như đồng Việt Nam.
tiện thể|Nhân dịp làm việc này thì làm thêm việc kia.
tiền thưởng|Khoản được nhận thêm để khen ngợi thành tích.
tiên tiến|Hiện đại, đi trước, vượt hơn so với mức chung.
tiến tới|Đi về phía trước; cũng là hướng đến một mục tiêu sắp đạt.
tiến triển|Thay đổi dần theo hướng tốt hơn.
tiến trình|Quá trình diễn ra theo từng bước của một việc.
tiền túi|Khoản riêng mang theo người để tiêu vặt.
tiền vệ|Cầu thủ chơi ở khu giữa sân, vừa tấn công vừa phòng ngự.
tiếng|Âm thanh nghe được; cũng chỉ ngôn ngữ, hoặc một giờ đồng hồ.
tiếng động|Âm thanh phát ra khi có vật va chạm hay chuyển động.
tiếng kêu|Âm thanh phát ra từ người, con vật hoặc đồ vật.
tiếng lóng|Từ ngữ riêng của một nhóm người, khác với ngôn ngữ chuẩn.
tiếng nói|Âm thanh lời nói của người; cũng chỉ ý kiến, quan điểm.
tiếng ồn|Âm thanh to, hỗn loạn, gây khó chịu.
tiếng tăm|Danh tiếng, sự nổi tiếng được nhiều người biết đến.
tiếng vang|Âm thanh dội lại; cũng chỉ sự ảnh hưởng rộng rãi, được nhiều người biết.
tiếng vọng|Âm thanh dội lại từ xa khi gặp vách đá, tường.
tiếng xấu|Lời đánh giá không tốt về một người, danh tiếng không hay.
tiếp|Nối liền theo sau; cũng là đón và trò chuyện với khách.
tiếp cận|Đến gần để tìm hiểu hoặc làm quen với ai, điều gì.
tiếp diễn|Vẫn còn xảy ra, kéo dài, chưa dừng lại.
tiếp đãi|Đón tiếp và mời khách ăn uống chu đáo.
tiếp đón|Ra đón và tiếp chuyện người đến thăm, đến làm việc.
tiếp khách|Đón, trò chuyện và mời nước người đến chơi nhà.
tiếp nhận|Nhận lấy những gì được gửi đến hay giao cho.
tiếp nối|Nối tiếp theo cái trước, tiếp tục điều đã có.
tiếp sức|Giúp thêm sức lực; cũng là môn chạy thay phiên nhau trao gậy.
tiếp tân|Người đón tiếp và hướng dẫn khách ở khách sạn, công ty.
tiếp theo|Kế ngay sau đó, theo thứ tự lần lượt.
tiếp thị|Các hoạt động quảng bá, giới thiệu để bán sản phẩm.
tiếp thu|Nhận và hiểu được kiến thức, ý kiến của người khác.
tiếp tục|Làm tiếp việc đang dở, không dừng lại.
tiếp viên|Người phục vụ hành khách trên máy bay, tàu xe.
tiếp xúc|Gặp gỡ, giao tiếp với người khác; cũng là chạm vào nhau.
tiết|Khoảng thời gian dạy một bài trên lớp; cũng chỉ thời tiết theo mùa.
tiết kiệm|Dùng tiền bạc, của cải đúng mức, không lãng phí.
tiết lộ|Để lộ ra điều bí mật cho người khác biết.
tiết mục|Một phần biểu diễn trong chương trình văn nghệ.
tiết tấu|Nhịp điệu nhanh chậm, mạnh nhẹ của bản nhạc hoặc câu thơ.
tiệt trùng|Diệt sạch vi khuẩn bằng nhiệt hoặc hóa chất.
tiêu|Hạt nhỏ vị cay thơm dùng làm gia vị; cũng có nghĩa là chi tiền, xài tiền.
tiểu bang|Đơn vị hành chính lớn trong một số nước liên bang, như Mỹ, Úc.
tiêu biểu|Có đặc điểm nổi bật, đại diện cho cả nhóm.
tiêu chí|Điều kiện, dấu hiệu dùng để xét chọn hay đánh giá.
tiêu chuẩn|Mức quy định làm căn cứ để đánh giá, so sánh.
tiêu cực|Không tốt, mang tính chất xấu hoặc bi quan, trái với tích cực.
tiêu dùng|Mua và sử dụng hàng hóa, dịch vụ cho đời sống.
tiêu đề|Tên đặt ở đầu một bài viết, chương sách hay văn bản.
tiêu điểm|Điểm thu hút sự chú ý nhất; cũng là điểm hội tụ ánh sáng của thấu kính.
tiêu hao|Bị mất đi, hao hụt dần như sức lực, năng lượng.
tiểu học|Bậc học đầu tiên, từ lớp một đến lớp năm.
tiểu luận|Bài viết ngắn bàn về một vấn đề, thường là bài tập ở đại học.
tiêu pha|Dùng tiền để mua sắm và chi tiêu cho các việc.
tiểu sử|Bản ghi tóm tắt cuộc đời và sự nghiệp của một người.
tiêu thụ|Bán ra hoặc sử dụng hết hàng hóa, năng lượng.
tiểu thuyết|Truyện dài kể nhiều sự việc, nhân vật một cách chi tiết.
tiểu thương|Người buôn bán nhỏ, thường có sạp hàng ở chợ.
tiêu tiền|Chi tiền để mua sắm hoặc trả cho việc gì đó.
tìm hiểu|Hỏi han, đọc thêm để biết rõ hơn về người hoặc việc gì.
tìm kiếm|Cố gắng tìm cho ra người hoặc vật mình cần.
tìm ra|Phát hiện được điều đang tìm hoặc điều mới.
tìm thấy|Thấy được người hoặc vật mình đang tìm.
tìm tòi|Chịu khó tìm hiểu, khám phá để biết thêm điều mới.
tin cậy|Có thể đặt niềm tin và dựa vào được.
tin chắc|Hoàn toàn tin là đúng, không chút nghi ngờ.
tín dụng|Hình thức vay và cho vay tiền, thường qua ngân hàng.
tin đồn|Chuyện được truyền miệng, chưa biết đúng hay sai.
tín hiệu|Dấu hiệu, âm thanh hay ánh sáng dùng để báo tin.
tin học|Ngành học về máy tính và cách xử lý thông tin.
tin mừng|Thông báo về một điều vui, đáng mừng.
tin tức|Thông tin về những sự việc mới xảy ra.
tin tưởng|Đặt niềm tin và hy vọng vào ai hay điều gì.
tin vui|Lời báo về một chuyện vui, điều tốt lành.
tính|Làm phép toán để ra kết quả; cũng chỉ nết ăn ở, cư xử của một người.
tình bạn|Sự thân thiết, gắn bó giữa những người bạn.
tinh bột|Chất có nhiều trong gạo, khoai, ngô, cung cấp năng lượng cho cơ thể.
tỉnh bơ|Tỏ ra bình thản như không có chuyện gì xảy ra.
tình ca|Bài hát nói về tình yêu đôi lứa.
tính cách|Những nét riêng trong suy nghĩ, cư xử của một người.
tình cảm|Sự yêu thương, quý mến, gắn bó giữa người với người.
tình cảnh|Hoàn cảnh mà một người đang gặp phải, thường là khó khăn.
tính chất|Đặc điểm riêng giúp phân biệt sự vật này với sự vật khác.
tinh chế|Lọc bỏ tạp chất để có sản phẩm sạch, tinh khiết hơn.
tình cờ|Xảy ra một cách ngẫu nhiên, không hẹn trước.
tinh dầu|Chất dầu thơm chiết xuất từ hoa, lá, vỏ cây.
tỉnh dậy|Thức dậy sau giấc ngủ, mở mắt ra.
tình duyên|Duyên phận yêu đương, chuyện tình cảm lứa đôi.
tỉnh giấc|Thức giấc, không còn ngủ nữa, thường là bất chợt.
tình hình|Trạng thái chung và diễn biến của sự việc trong một thời gian.
tình huống|Sự việc xảy ra trong một hoàn cảnh cụ thể, cần xử lý.
tính khí|Cách phản ứng, tính tình thường thấy của một người, như nóng nảy hay ôn hòa.
tinh khiết|Hoàn toàn trong sạch, không lẫn tạp chất.
tĩnh lặng|Yên tĩnh, không có tiếng động hay xáo trộn.
tỉnh lẻ|Các tỉnh nhỏ, ở xa thủ đô và những thành phố lớn.
tính năng|Khả năng, chức năng mà một sản phẩm hay máy móc làm được.
tính nết|Thói quen, cách ăn ở và cư xử thường ngày của một người.
tình nghĩa|Sự gắn bó, thủy chung và biết ơn giữa người với người.
tinh nghịch|Hay nghịch ngợm, đùa vui một cách dễ thương.
tỉnh ngủ|Đã hết buồn ngủ, đầu óc tỉnh táo; cũng chỉ người dễ thức giấc.
tình nguyện|Tự mình muốn làm, không ai ép buộc, thường để giúp người khác.
tinh ranh|Khôn lanh, ranh mãnh, nhiều mẹo vặt.
tỉnh táo|Đầu óc minh mẫn, sáng suốt, không mơ màng.
tinh tế|Khéo léo, nhạy bén, nhận ra được cả những điều nhỏ nhặt.
tỉnh thành|Các tỉnh và thành phố trong cả nước nói chung.
tinh thần|Trạng thái tâm lý, ý chí, cảm xúc của con người, trái với thể xác.
tình thế|Hoàn cảnh chung tại một lúc, thường đòi hỏi phải ứng phó.
tình thương|Lòng thương yêu, quan tâm dành cho người khác.
tình tiết|Những chi tiết, sự việc nhỏ làm nên một câu chuyện.
tinh tinh|Loài vượn lớn, lông đen, rất thông minh, sống ở châu Phi.
tính toán|Làm các phép tính; cũng chỉ việc suy tính, cân nhắc kỹ lưỡng.
tình trạng|Trạng thái, hoàn cảnh hiện tại của người hoặc vật.
tính từ|Loại từ chỉ đặc điểm, tính chất của sự vật, như đẹp, cao.
tinh ý|Nhanh nhạy, dễ nhận ra điều người khác nghĩ hay muốn.
tình yêu|Sự yêu thương sâu sắc, nhất là giữa đôi lứa.
titan|Kim loại nhẹ, cứng, bền, không gỉ, dùng trong máy bay và dụng cụ y tế.
to béo|Có thân hình to lớn và nhiều mỡ, mập mạp.
to con|Có vóc người cao lớn, vạm vỡ.
to đùng|Rất to, lớn hơn hẳn so với mong đợi, gây chú ý.
to gan|Rất gan dạ, dám làm những việc người khác sợ.
to lớn|Rất lớn về kích thước hoặc tầm quan trọng.
tò mò|Muốn biết những điều mới lạ hoặc chuyện của người khác.
tỏ ra|Để lộ ra ngoài qua thái độ, cử chỉ.
to tát|Lớn lao, quan trọng, thường dùng với ý phủ định.
to tiếng|Nói lớn tiếng; cũng chỉ cãi nhau, lời qua tiếng lại.
tỏ tình|Nói cho người mình thích biết tình cảm của mình.
to tướng|Rất to, to hơn bình thường nhiều.
tỏ vẻ|Để lộ ra bên ngoài một thái độ, cảm xúc nào đó.
toán|Môn học về con số, phép tính và hình; cũng chỉ một nhóm nhỏ người.
toàn bộ|Tất cả các phần, không bỏ sót hay trừ ra phần nào.
toàn cảnh|Cảnh nhìn bao quát từ trên cao hay từ xa; cũng chỉ cái nhìn tổng thể.
toàn cầu|Khắp cả thế giới, mọi nơi trên trái đất.
toàn diện|Đầy đủ về mọi mặt, không thiếu khía cạnh nào.
toán đố|Bài toán có lời văn, phải suy nghĩ để tìm ra cách giải.
toán học|Khoa học nghiên cứu về số lượng, hình dạng và các phép tính.
toàn quốc|Khắp cả nước, mọi vùng trong một nước.
toàn thân|Khắp cả cơ thể, từ đầu đến chân.
toàn thể|Tất cả mọi người hoặc mọi bộ phận, không trừ ai.
toàn vẹn|Đầy đủ, nguyên vẹn, không bị thiếu hụt hay hư hại.
tóc bạc|Mái tóc đã chuyển sang màu trắng, thường do tuổi tác.
tóc giả|Bộ tóc làm sẵn để đội lên đầu cho đẹp hoặc hóa trang.
tóc tai|Mái tóc nói chung, thường nói về vẻ gọn gàng hay bù xù.
toe toét|Cười rộng miệng một cách vui vẻ, hồn nhiên.
tỏi tây|Cây giống hành lá nhưng to, thân trắng, lá dẹt, dùng nấu ăn.
tóm lại|Nói gọn lại những ý chính đã nêu.
tóm tắt|Thu gọn, nêu ngắn gọn những ý chính của một nội dung.
tổ ấm|Gia đình đầm ấm, nơi mọi người yêu thương và che chở nhau.
tố chất|Phẩm chất, năng khiếu sẵn có ở một người.
tổ chức|Sắp xếp để thực hiện một việc; cũng chỉ một tập thể có chung mục đích.
tổ hợp|Sự kết hợp nhiều thành phần thành một khối; cũng chỉ nhóm môn thi xét tuyển.
tô màu|Dùng bút màu phủ màu lên tranh vẽ hoặc hình in sẵn.
tổ ong|Ổ của đàn ong, gồm nhiều ô nhỏ sáu cạnh chứa mật và trứng.
tổ tiên|Những người thuộc các thế hệ trước trong gia đình, dòng họ.
tổ trưởng|Người đứng đầu và phụ trách công việc của một tổ, nhóm.
tốc độ|Mức nhanh hay chậm của một chuyển động hoặc công việc.
tốc hành|Chạy rất nhanh, ít dừng dọc đường, như tàu xe chạy suốt.
tối cao|Cao nhất, có quyền lực hoặc vị trí lớn nhất.
tối đa|Mức cao nhất, nhiều nhất có thể đạt được hoặc được cho phép.
tối đen|Đen kịt, không có chút ánh sáng nào, như đêm không trăng.
tối giản|Đơn giản hết mức, chỉ giữ điều cần thiết; cũng chỉ phân số không rút gọn được.
tối mịt|Trời đã tối hẳn, tối đến mức khó nhìn rõ mọi vật.
tối mù|Tối đen, không nhìn rõ gì; cũng chỉ sự mù mịt, khó hiểu.
tội nghiệp|Đáng thương, khiến người khác thấy xót xa, muốn giúp đỡ.
tối om|Rất tối, thường nói về căn phòng hay nơi không bật đèn.
tối qua|Buổi tối của ngày hôm qua.
tối sầm|Bỗng tối lại rất nhanh, như trời sắp mưa; cũng chỉ sắc mặt chợt buồn bực.
tối tăm|Thiếu ánh sáng, âm u; nghĩa bóng chỉ cảnh sống vất vả, chưa thấy tương lai.
tối tân|Hiện đại và mới nhất, thường nói về máy móc, thiết bị.
tồi tệ|Rất xấu, rất kém, khiến người ta không hài lòng.
tối thiểu|Mức thấp nhất, ít nhất có thể hoặc bắt buộc phải có.
tối thui|Tối om, đen kịt, không có chút ánh sáng nào.
tối ưu|Tốt nhất, hiệu quả nhất trong số các lựa chọn có thể có.
tôm càng|Loại tôm sống ở sông, có đôi càng to và dài.
tôm cua|Tôm và cua, các loài thủy sản có vỏ cứng nói chung.
tôm hùm|Loài tôm biển to, vỏ cứng, thịt ngon và đắt tiền.
tôm sú|Loại tôm biển cỡ lớn, vỏ có vằn sẫm, thịt chắc ngọt.
tôm tép|Tôm và tép, các loại tôm nhỏ nói chung.
tôm thẻ|Loại tôm nuôi phổ biến, cỡ vừa, vỏ mỏng màu trắng xám.
tổn hại|Gây thiệt hại, làm hư hỏng hoặc giảm sút về vật chất, tinh thần.
tốn kém|Phải chi nhiều tiền bạc, công sức hoặc thời gian.
tồn kho|Hàng hóa còn lại trong kho, chưa bán hoặc chưa dùng đến.
tồn tại|Có thật, vẫn còn hiện hữu; cũng chỉ thiếu sót chưa khắc phục được.
tôn trọng|Coi trọng, quý trọng người khác và ý kiến của họ.
tôn vinh|Đề cao, ca ngợi công lao hoặc giá trị của ai, cái gì.
tổng|Kết quả có được khi cộng các số với nhau.
tổng cộng|Số có được khi cộng tất cả các phần lại với nhau.
tổng đài|Nơi nhận và chuyển cuộc gọi, hoặc giải đáp thắc mắc qua điện thoại.
tổng hợp|Gom nhiều thứ, nhiều nguồn lại với nhau thành một.
tổng kết|Nhìn lại, đánh giá toàn bộ một công việc khi kết thúc.
tổng quan|Cái nhìn chung, bao quát toàn bộ một vấn đề.
tổng quát|Chung, bao quát, không đi vào từng chi tiết.
tổng số|Số lượng có được khi tính gộp tất cả lại.
tổng thể|Toàn bộ các phần gộp lại, nhìn như một khối thống nhất.
tốt bụng|Có lòng tốt, hay giúp đỡ và thương người.
tốt đẹp|Có nhiều điều hay, đáng quý, khiến mọi người hài lòng.
tốt lành|Tốt đẹp, mang lại điều may mắn và bình an.
tốt nghiệp|Hoàn thành chương trình học ở một trường hay một cấp học.
tờ báo|Ấn phẩm in trên giấy, đăng tin tức và bài viết theo định kỳ.
tơ lụa|Vải mềm mịn, óng ả được dệt từ sợi tơ tằm.
tờ rơi|Mẩu giấy in quảng cáo hay thông báo, được phát tận tay mọi người.
tơ tằm|Sợi mảnh, bóng do con tằm nhả ra để làm kén.
tới mức|Đạt đến một mức độ nào đó, thường dùng để nhấn mạnh.
tới nơi|Đã đến được chỗ cần đến sau một chuyến đi.
tới tấp|Liên tục và dồn dập, cái này nối ngay cái kia.
trả bài|Đọc thuộc bài đã học cho thầy cô kiểm tra; cũng chỉ việc phát lại bài đã chấm.
trả công|Đưa tiền hoặc vật để đền đáp người đã làm việc cho mình.
tra cứu|Tìm kiếm thông tin trong sách, từ điển hoặc trên mạng.
trả giá|Mặc cả để mua được rẻ hơn; cũng chỉ việc chịu hậu quả việc đã làm.
trả góp|Chia tiền mua hàng ra trả làm nhiều lần, mỗi lần một ít.
trả lại|Đưa lại cho chủ thứ mình đã nhận hoặc đã mượn.
trả lời|Nói hoặc viết để đáp lại câu hỏi, lời gọi.
trả ơn|Đền đáp lại người đã giúp đỡ mình.
trách|Nói ra sự không hài lòng về lỗi của người khác.
trách mắng|La rầy, nói nặng lời vì người khác có lỗi.
trách móc|Kể lể, phàn nàn về lỗi của người khác.
trách nhiệm|Phần việc mình phải làm và chịu kết quả về việc đó.
trái|Phía ngược với bên phải; cũng là sai, ngược lại; ở miền Nam còn là quả.
trái cây|Các loại quả ăn được như cam, xoài, chuối.
trái đào|Loại quả tròn, vỏ mịn có lông tơ, thịt ngọt và thơm.
trái đất|Hành tinh nơi con người và muôn loài đang sống.
trại hè|Đợt sinh hoạt, vui chơi tập thể dành cho học sinh vào mùa hè.
trái lại|Từ nối nêu ý ngược với điều vừa nói.
trái mùa|Xuất hiện không đúng mùa thường lệ, như mưa hay quả trái mùa.
trái nghĩa|Có nghĩa ngược nhau, như cao với thấp.
trải nghiệm|Tự mình trải qua để hiểu và cảm nhận; cũng chỉ điều đã trải qua.
trái ngược|Hoàn toàn ngược nhau, đối lập với nhau.
trái phiếu|Giấy vay nợ do nhà nước hoặc doanh nghiệp phát hành, có trả lãi.
trải qua|Đã sống qua, đã từng gặp hoặc chịu đựng điều gì đó.
trái tim|Bộ phận trong lồng ngực bơm máu đi khắp cơ thể; cũng là biểu tượng của tình yêu.
trai trẻ|Còn trẻ trung, đang tuổi thanh niên, thường nói về con trai.
trạm|Điểm dừng hoặc nơi làm việc đặt ở một khu vực, như trạm xe buýt.
trán|Phần trên của khuôn mặt, từ chân tóc đến lông mày.
tràn đầy|Đầy ắp, chan chứa, như sức sống hay niềm vui.
tràn lan|Xuất hiện ở khắp nơi một cách khó kiểm soát.
tràn ngập|Đầy khắp, phủ kín cả một vùng.
tràn trề|Rất đầy, như muốn tràn ra, thường nói về niềm vui, hy vọng.
trang bị|Cung cấp đồ dùng, dụng cụ cần thiết; cũng chỉ chính những đồ dùng đó.
trang chủ|Phần mở đầu chính của một trang web, nơi dẫn tới các mục khác.
trang điểm|Dùng phấn, son để làm đẹp khuôn mặt.
trang hoàng|Bày biện, trang trí cho đẹp, nhất là vào dịp lễ Tết.
trang lứa|Cùng độ tuổi, cùng một thế hệ với nhau.
tráng men|Phủ một lớp men bóng lên bề mặt đồ gốm, sứ hoặc kim loại.
tráng miệng|Ăn chút trái cây hoặc đồ ngọt sau bữa ăn chính.
trang nghiêm|Nghiêm túc, trịnh trọng, gây cảm giác kính cẩn.
trạng nguyên|Danh hiệu dành cho người đỗ đầu kỳ thi cao nhất thời xưa.
trang phục|Quần áo và đồ mặc nói chung.
trang sức|Đồ đeo để làm đẹp như nhẫn, vòng, dây chuyền.
trạng thái|Tình trạng của người hoặc vật vào một thời điểm nhất định.
trang trại|Khu đất rộng để trồng trọt, chăn nuôi quy mô lớn.
trang trí|Bày biện, sắp đặt để làm cho đẹp hơn.
trang trọng|Lịch sự, nghiêm túc, phù hợp với dịp quan trọng.
trạng từ|Từ bổ nghĩa cho động từ, tính từ, chỉ cách thức, thời gian, nơi chốn.
tranh|Tác phẩm hội họa vẽ trên giấy, vải; cũng có nghĩa là giành lấy với người khác.
tranh ảnh|Các bức vẽ và hình chụp nói chung, thường dùng để trang trí hay minh họa.
tranh cãi|Bàn cãi gay gắt, mỗi bên giữ ý kiến riêng của mình.
tranh giải|Thi đấu để giành giải thưởng.
tranh luận|Đưa ra ý kiến khác nhau để bàn cãi, tìm ra lẽ đúng.
tránh mặt|Cố ý không để gặp mặt người nào đó.
tránh né|Lảng đi, không muốn đối diện với người hay việc nào đó.
tranh thủ|Tận dụng thời gian hoặc cơ hội để làm việc gì đó.
tranh tường|Bức vẽ trực tiếp lên tường nhà hoặc tường công cộng.
trao|Đưa tận tay cho người khác.
trao đổi|Đổi cho nhau; cũng là cùng nhau bàn bạc, chia sẻ ý kiến.
trào lưu|Xu hướng được nhiều người theo trong một thời gian.
trao tặng|Đưa tặng một cách trân trọng, thường là quà hoặc giải thưởng.
trắc nghiệm|Hình thức kiểm tra bằng cách chọn đáp án đúng trong các phương án cho sẵn.
trăm năm|Khoảng thời gian một trăm năm; cũng chỉ trọn đời gắn bó, thường nói về vợ chồng.
trăm nghìn|Con số một trăm nghìn; cũng chỉ số lượng rất nhiều.
trằn trọc|Nằm trở mình mãi không ngủ được vì lo nghĩ.
trăn trở|Băn khoăn, suy nghĩ mãi không yên về một điều gì.
trăng|Mặt trăng, thiên thể sáng trên bầu trời ban đêm.
trắng bệch|Trắng nhợt, không có chút sắc hồng, thường nói về da mặt.
trắng đen|Hai màu trắng và đen, như ảnh không màu; cũng chỉ đúng sai rõ ràng.
trắng đục|Có màu trắng hơi mờ, không trong, giống màu sữa.
trăng khuyết|Mặt trăng chưa tròn, chỉ còn sáng một phần.
trăng mật|Chuyến đi chơi, nghỉ ngơi của đôi vợ chồng mới cưới.
trắng muốt|Trắng tinh, mịn màng và rất đẹp.
trăng non|Trăng đầu tháng âm lịch, hình lưỡi liềm mảnh và mờ.
trắng tinh|Có màu trắng hoàn toàn, sạch sẽ, không một vết bẩn.
trắng toát|Có màu trắng đều khắp, nổi bật hẳn lên.
trắng trẻo|Có làn da trắng và hồng hào, trông khỏe đẹp.
trầm hương|Loại gỗ quý có mùi thơm, lấy từ cây dó, thường dùng làm nhang.
trầm ngâm|Lặng lẽ suy nghĩ sâu xa về một điều gì đó.
trầm tính|Tính tình ít nói, điềm đạm, không sôi nổi.
trầm trọng|Rất nặng nề, nghiêm trọng, khó cứu vãn.
trầm trồ|Khen ngợi, tỏ ra thán phục khi thấy điều hay, đẹp.
trấn an|Làm cho người khác yên lòng, bớt lo lắng, sợ hãi.
trật tự|Sự sắp xếp có thứ tự, nề nếp; cũng chỉ sự yên lặng, không ồn ào.
trâu|Con vật nuôi to khỏe, sừng cong, da đen, thường dùng để cày ruộng.
trâu bò|Những gia súc lớn như trâu và bò, nuôi để kéo cày, lấy thịt.
trẻ con|Đứa bé nói chung; cũng chỉ cách cư xử non nớt như trẻ nhỏ.
trẻ em|Những người còn nhỏ tuổi, chưa trưởng thành nói chung.
trẻ nhỏ|Đứa bé còn ít tuổi, cần người lớn chăm sóc.
tre nứa|Tre và nứa, các loài cây thân có đốt, ruột rỗng.
trẻ thơ|Đứa bé còn nhỏ, hồn nhiên và ngây thơ.
trẻ trung|Có vẻ ngoài và tinh thần tươi tắn, đầy sức sống như người trẻ.
trẻ tuổi|Còn ít tuổi, đang ở độ tuổi thanh niên.
treo|Móc hoặc buộc vật lên cao cho lơ lửng, như treo áo, treo tranh.
trên|Ở vị trí cao hơn hoặc ở bề mặt của một vật.
trên dưới|Xấp xỉ, khoảng chừng một con số; cũng chỉ cấp trên và cấp dưới.
trêu|Chọc ghẹo cho người khác bực mình hoặc ngượng để đùa vui.
tri ân|Bày tỏ lòng biết ơn đối với người đã giúp đỡ mình.
trị giá|Giá trị của một vật khi tính thành tiền.
trì hoãn|Lùi lại, kéo dài thời gian, chưa chịu làm ngay.
trí khôn|Khả năng hiểu biết, suy nghĩ để biết cách xử lý việc.
trí não|Bộ óc và khả năng suy nghĩ của con người.
trí nhớ|Khả năng ghi lại và nhớ lại những điều đã biết, đã trải qua.
trí óc|Đầu óc, nơi diễn ra suy nghĩ, tư duy của con người.
tri thức|Kiến thức, hiểu biết mà con người tích lũy được.
trí tuệ|Khả năng nhận thức, hiểu biết và suy xét sâu sắc.
trích|Lấy ra một phần từ cái chung, như trích lời, trích tiền quỹ.
trích dẫn|Dẫn lại nguyên văn lời nói hoặc câu văn của người khác.
triển khai|Bắt đầu đưa một kế hoạch vào thực hiện trên diện rộng.
triển lãm|Trưng bày sản phẩm, tranh ảnh để mọi người đến xem.
triển vọng|Khả năng phát triển tốt đẹp trong tương lai.
triệt để|Làm đến cùng, tới nơi tới chốn, không bỏ sót.
triệu|Số bằng một nghìn lần một nghìn.
triều đại|Thời gian một dòng họ vua nối nhau trị vì đất nước.
triệu phú|Người rất giàu, có tài sản tính bằng hàng triệu.
trình|Đưa lên để cấp trên xem xét; khẩu ngữ còn chỉ trình độ, tay nghề.
trình bày|Nói hoặc viết ra rõ ràng, có thứ tự để người khác hiểu.
trình chiếu|Chiếu phim, hình ảnh hoặc bài thuyết trình lên màn hình cho người xem.
trình diễn|Biểu diễn hoặc thể hiện tài năng, sản phẩm trước người xem.
trình độ|Mức hiểu biết, kỹ năng mà một người đạt được.
trình làng|Ra mắt, giới thiệu lần đầu với công chúng.
trinh thám|Thể loại truyện, phim kể về việc điều tra, khám phá những bí ẩn.
trịnh trọng|Nghiêm trang, long trọng, tỏ ra rất coi trọng.
trình tự|Thứ tự trước sau cần theo khi làm một việc.
trò chơi|Hoạt động vui chơi, giải trí, thường có luật chơi riêng.
trò chuyện|Nói chuyện qua lại với nhau một cách thân mật.
trò cười|Việc làm hay câu chuyện khiến người khác bật cười, thường là chê cười.
trò đùa|Lời nói hay việc làm để đùa vui, không nghiêm túc.
trò hề|Việc làm lố bịch, đáng cười, giống như diễn hề.
trò vui|Hoạt động hoặc trò chơi mang lại niềm vui, tiếng cười.
trọc|Không có tóc trên đầu; cũng chỉ đồi núi không có cây.
trói buộc|Ràng buộc, làm cho mất tự do, không làm được theo ý mình.
tròn|Có hình như cái đĩa hay quả bóng; cũng chỉ con số chẵn, vừa đủ.
trọn đời|Suốt cả cuộc đời, mãi mãi về sau.
trọn gói|Bao gồm hết mọi khoản, không phải trả thêm gì.
tròn trịa|Có dáng tròn đều, đầy đặn, trông dễ thương.
tròn trĩnh|Đầy đặn, mũm mĩm, có dáng tròn trông dễ thương.
trọn vẹn|Đầy đủ, hoàn chỉnh, không thiếu sót gì.
tròn vo|Rất tròn, tròn đều như viên bi.
tròn xoe|Tròn đều và đẹp, như đôi mắt mở to.
trọng đại|Rất lớn lao và hệ trọng, có ý nghĩa đặc biệt.
tròng đen|Phần màu đen hoặc nâu sẫm ở giữa con mắt.
trọng điểm|Nơi hoặc điều quan trọng nhất, cần được tập trung.
trong khi|Từ nối chỉ cùng lúc với một việc khác đang diễn ra.
trong lành|Sạch sẽ, mát mẻ, không bị ô nhiễm, thường nói về không khí.
trong lúc|Vào khoảng thời gian một việc đang diễn ra.
trọng lượng|Độ nặng của một vật hay một người.
trong sạch|Sạch sẽ, không vẩn đục; cũng chỉ người sống ngay thẳng, liêm khiết.
trong sáng|Sạch và sáng, không vẩn đục; cũng chỉ tâm hồn ngây thơ, không vụ lợi.
trong suốt|Để ánh sáng đi qua, nhìn xuyên thấu được; cũng nghĩa là suốt cả một khoảng thời gian.
trọng tài|Người điều khiển trận đấu và phân xử theo luật chơi.
trọng tâm|Phần chính, quan trọng nhất cần chú ý của một vấn đề.
trong trắng|Ngây thơ, thuần khiết, chưa vướng điều xấu xa.
trong trẻo|Sáng và dễ chịu, không lẫn tạp, như giọng hát hay nước suối.
trong vắt|Rất trong, sạch đến mức nhìn thấu tận đáy.
trong veo|Rất trong, có thể nhìn thấy tận đáy.
trong vòng|Không quá một khoảng thời gian hoặc phạm vi nhất định.
trổ tài|Thể hiện tài năng, sự khéo léo của mình cho người khác thấy.
trôi chảy|Diễn ra suôn sẻ, lưu loát, không bị vấp váp.
trôi nổi|Lềnh bềnh theo dòng nước; cũng chỉ cuộc sống lang bạt, không ổn định.
trôi qua|Thời gian cứ thế đi qua, lùi dần vào quá khứ.
trốn học|Bỏ buổi học mà không xin phép.
trộn lẫn|Hòa nhiều thứ vào với nhau, không còn tách riêng.
trốn thoát|Thoát ra được khỏi nơi bị giữ lại hoặc chỗ nguy hiểm.
trốn tránh|Lẩn tránh, không dám đối mặt với người hoặc việc gì.
trốn việc|Lẩn tránh, không chịu làm công việc được giao.
trống|Nhạc cụ có mặt da căng, gõ cho kêu; cũng chỉ chỗ không có gì.
trông cậy|Tin tưởng và dựa vào sự giúp đỡ của người khác.
trông chờ|Ngóng chờ, hy vọng vào sự giúp đỡ hay điều sẽ đến.
trồng chuối|Chống tay xuống đất, dựng ngược người lên, chân hướng lên trời.
trông chừng|Để mắt canh giữ, đề phòng điều không hay xảy ra.
trông coi|Để mắt chăm lo, giữ gìn người hoặc tài sản.
trống đồng|Trống cổ đúc bằng đồng, có hoa văn tinh xảo, gắn với văn hóa Đông Sơn.
trông đợi|Chờ đợi với hy vọng một điều sẽ đến hoặc sẽ xảy ra.
trống không|Hoàn toàn rỗng, không có gì; cũng chỉ cách nói không thưa gửi.
trông mong|Mong mỏi, hy vọng điều gì đó tốt đẹp sẽ xảy ra.
trông nom|Chăm sóc, coi sóc người hoặc nhà cửa, đồ đạc chu đáo.
trống rỗng|Không có gì bên trong; cũng chỉ cảm giác hụt hẫng trong lòng.
trông thấy|Nhìn thấy được bằng chính mắt mình.
trống trải|Rộng và trống, không có gì che chắn; cũng chỉ cảm giác cô quạnh.
trồng trọt|Công việc trồng và chăm sóc cây cối, hoa màu.
trống trơn|Hoàn toàn trống, không còn sót lại thứ gì.
trống vắng|Vắng vẻ, thiếu người hay điều thân quen nên thấy buồn.
trợ cấp|Khoản tiền hay hiện vật hỗ trợ cho người gặp khó khăn hoặc theo chế độ.
trợ giúp|Giúp đỡ thêm cho người đang cần.
trở lại|Quay về chỗ cũ hoặc tình trạng như trước.
trở mặt|Bất ngờ đổi thái độ, quay lưng với người từng thân thiết.
trở mình|Xoay người sang tư thế khác khi đang nằm; cũng chỉ sự chuyển biến.
trở nên|Chuyển dần sang một tính chất, trạng thái khác.
trở ngại|Điều gây khó khăn, cản trở việc làm.
trở thành|Biến đổi để thành một người hay vật khác so với trước.
trợ thủ|Người giúp đỡ, hỗ trợ đắc lực cho người khác.
trớ trêu|Oái oăm, éo le, trái ngược với điều mong đợi.
trở trời|Thời tiết thay đổi đột ngột, dễ làm người mệt mỏi.
trở về|Quay về nơi mình đã ra đi.
trời|Khoảng không bao la trên cao; cũng chỉ thời tiết.
trời đất|Bầu trời và mặt đất, cả thiên nhiên; cũng là tiếng kêu khi ngạc nhiên.
trời ơi|Tiếng kêu khi ngạc nhiên, than thở hoặc bực mình.
trời xanh|Bầu trời màu xanh; cũng chỉ ông trời theo cách nói dân gian.
trơn tru|Suôn sẻ, trôi chảy, không gặp vướng mắc gì.
trơn tuột|Rất trơn, dễ trượt, khó cầm nắm hay đứng vững.
trú ẩn|Tạm ở nơi kín đáo, an toàn để tránh mưa gió hay nguy hiểm.
trụ cột|Cột chính chống đỡ; cũng chỉ người gánh vác chính trong nhà.
trụ sở|Nơi làm việc chính của một cơ quan, tổ chức.
trúc|Cây cùng họ với tre, thân nhỏ, thẳng, hay trồng làm cảnh.
trục trặc|Có chỗ hỏng hoặc vướng mắc nên hoạt động không trơn tru.
trụi|Không còn lông, lá hay thứ gì che phủ bên ngoài.
trùm chăn|Kéo chăn phủ kín người, thường khi trời lạnh hoặc ngủ nướng.
trung bình|Ở mức giữa, không cao không thấp; cũng là kết quả chia đều các giá trị.
trúng giải|Giành được giải thưởng trong một cuộc thi hoặc bốc thăm.
trung gian|Ở giữa hai bên, làm cầu nối để hai bên liên hệ với nhau.
trung học|Bậc học sau tiểu học, gồm trung học cơ sở và trung học phổ thông.
trùng hợp|Tình cờ giống nhau hoặc xảy ra cùng một lúc.
trung niên|Độ tuổi giữa đời người, khoảng từ bốn mươi đến sáu mươi.
trung tâm|Điểm ở giữa; cũng là nơi tập trung các hoạt động quan trọng.
trung thành|Một lòng một dạ, luôn gắn bó và giữ trọn niềm tin với ai.
trung thực|Ngay thẳng, thật thà, không gian dối.
trung tính|Không nghiêng về bên nào; trong hóa học chỉ chất không có tính axit hay bazơ.
trúng tuyển|Đỗ, được nhận sau một kỳ thi hoặc đợt xét tuyển.
trút|Đổ hết ra một lượt; cũng chỉ dồn hết cảm xúc ra ngoài.
trút bỏ|Bỏ hết đi những thứ đang mang trên người hoặc trong lòng.
truy cập|Vào xem, sử dụng một trang web hoặc dữ liệu trên máy tính.
truy tìm|Lần theo dấu vết để tìm cho ra.
truyền cảm|Gây được xúc động, làm người nghe cảm nhận sâu sắc.
truyền đạt|Nói lại, chuyển kiến thức hay ý kiến cho người khác hiểu.
truyền hình|Phát hình ảnh và âm thanh đi xa để xem trên ti vi.
truyền miệng|Kể lại cho nhau bằng lời nói, không ghi chép.
truyền tải|Chuyển, đưa thông điệp hoặc năng lượng đến nơi khác.
truyền thống|Thói quen, phong tục tốt đẹp được giữ gìn từ đời này sang đời khác.
truyền thuyết|Truyện dân gian kể về nhân vật, sự kiện lịch sử có pha yếu tố kỳ ảo.
truyện tranh|Câu chuyện được kể bằng các khung hình vẽ kèm lời thoại ngắn.
trừ khi|Ngoại trừ trường hợp, dùng để nêu điều kiện duy nhất có thể làm khác đi.
trừ phi|Chỉ trừ trường hợp, dùng để nêu điều kiện ngoại lệ duy nhất.
trữ tình|Giàu cảm xúc, nhẹ nhàng và sâu lắng, thường nói về thơ, nhạc.
trưa|Khoảng thời gian giữa ngày, lúc mặt trời lên cao nhất.
trực giác|Khả năng nhận biết ngay mà không cần suy luận.
trực quan|Dễ hiểu nhờ được nhìn thấy trực tiếp, như qua hình ảnh, mô hình.
trực thăng|Máy bay có cánh quạt lớn trên nóc, cất và hạ cánh thẳng đứng.
trực tiếp|Thẳng tới, không qua người hay khâu trung gian.
trực tuyến|Diễn ra hoặc kết nối thông qua mạng internet.
trứng|Vật hình bầu dục có vỏ do gà, vịt, chim đẻ ra, dùng làm thức ăn.
trứng gà|Quả trứng do gà mái đẻ ra, món ăn quen thuộc hằng ngày.
trứng muối|Trứng vịt ngâm nước muối lâu ngày, lòng đỏ đậm và bùi.
trước|Ở phía mặt hướng tới; cũng chỉ thời điểm sớm hơn.
trước đây|Thời gian đã qua, trước thời điểm hiện tại.
trước hết|Đầu tiên, trước tất cả những việc khác.
trước khi|Vào lúc chưa diễn ra một việc nào đó.
trước kia|Khoảng thời gian đã qua từ lâu, ngày xưa.
trước mặt|Ở ngay phía trước mắt; cũng chỉ thời gian sắp tới.
trước sau|Lúc trước và lúc sau, từ đầu đến cuối; cũng có nghĩa là sớm muộn gì.
trước tiên|Bước đầu tiên, việc phải làm trước nhất.
trườn|Di chuyển bằng cách áp sát thân xuống đất mà nhích tới, như rắn.
trường|Nơi thầy cô dạy học và học sinh đến học.
trưởng đoàn|Người đứng đầu, chịu trách nhiệm dẫn dắt một đoàn.
trường học|Nơi tổ chức việc dạy và học.
trường hợp|Một tình huống, hoàn cảnh cụ thể có thể xảy ra.
trưởng phòng|Người đứng đầu, quản lý một phòng ban trong cơ quan, công ty.
trường quay|Nơi dựng cảnh, có máy móc để quay phim, ghi hình chương trình.
trưởng thành|Đã lớn và phát triển đầy đủ; cũng chỉ suy nghĩ chín chắn.
trường thọ|Sống lâu, đạt tuổi thọ cao.
trượt|Lướt đi trên bề mặt trơn; cũng có nghĩa là thi không đỗ.
trượt băng|Môn thể thao lướt trên mặt băng bằng giày có gắn lưỡi.
trượt tuyết|Môn thể thao lướt trên tuyết bằng ván hoặc hai thanh trượt dài.
tủ áo|Loại tủ dùng để treo và cất giữ quần áo.
tủ đá|Thiết bị làm lạnh sâu để làm đá và trữ đông thực phẩm.
tu hú|Loài chim hay kêu vào đầu hè, đẻ trứng nhờ vào tổ chim khác.
tủ kính|Loại tủ có cửa bằng kính, dùng để trưng bày đồ vật.
tủ lạnh|Tủ giữ nhiệt độ thấp để bảo quản thức ăn, đồ uống.
tủ sách|Loại tủ để đựng sách; cũng chỉ những sách mà một nhà, một nơi sưu tầm.
tụ tập|Nhiều người cùng kéo đến và tập trung ở một chỗ.
tua rua|Những sợi nhỏ buông rủ ở mép khăn, áo, rèm để trang trí.
tuần|Khoảng thời gian bảy ngày, từ thứ hai đến chủ nhật.
tuần hoàn|Lặp đi lặp lại theo một vòng khép kín, như máu chảy khắp cơ thể.
tuần lễ|Khoảng thời gian gồm bảy ngày liên tiếp.
tuần lộc|Loài hươu sống ở xứ lạnh, có gạc lớn, hay kéo xe trượt tuyết.
tuân thủ|Làm đúng theo luật lệ, quy định đã đặt ra.
tuần tự|Lần lượt theo đúng thứ tự, bước này rồi đến bước khác.
tục lệ|Thói quen, nếp sống có từ lâu đời được cộng đồng gìn giữ.
tục ngữ|Câu nói dân gian ngắn gọn, đúc kết kinh nghiệm sống của ông cha.
túi bụi|Dồn dập, liên tục không ngớt, nhất là khi rất bận rộn.
tủi thân|Buồn và thấy thương cho bản thân khi bị đối xử lạnh nhạt.
túi tiền|Cái túi để đựng tiền; cũng chỉ khả năng chi tiêu của mỗi người.
túi xách|Đồ đựng có quai để xách hoặc đeo, dùng mang đồ theo người.
tulip|Loài hoa hình chén, nhiều màu sắc rực rỡ, nổi tiếng ở Hà Lan.
tung|Ném mạnh lên cao; cũng chỉ việc đưa ra, phát hành rộng rãi.
tung hô|Hô to để ca ngợi, chào đón ai đó.
tung hứng|Ném nhiều vật lên rồi bắt lại liên tục; cũng chỉ sự phối hợp ăn ý.
tung tăng|Đi lại, nhảy nhót vui vẻ, nhẹ nhàng, hồn nhiên.
tuổi đời|Số năm một người đã sống, tính từ lúc sinh ra.
tuổi già|Quãng đời khi con người đã cao tuổi.
tuổi ta|Cách tính tuổi theo âm lịch, sinh ra đã là một tuổi, qua mỗi Tết thêm một tuổi.
tuổi tác|Số tuổi của một người, nhất là khi đã lớn tuổi.
tuổi thật|Số tuổi tính đúng từ ngày sinh, không cộng thêm như tuổi ta.
tuổi thơ|Thời kỳ còn bé, khi ta còn là trẻ con.
tuổi trẻ|Quãng đời trẻ trung, sung sức nhất của con người.
tuổi xanh|Lứa tuổi trẻ, còn non nớt và tràn đầy sức sống.
tuổi xuân|Quãng đời tuổi trẻ, tươi đẹp nhất của mỗi người.
tuôn|Chảy ra hoặc tràn ra nhiều và liên tục.
tuột|Trượt ra hoặc tụt xuống khỏi chỗ cũ một cách bất ngờ.
túp lều|Căn nhà nhỏ, đơn sơ, thường dựng tạm bằng tre, lá.
tuy nhiên|Từ nối dùng để nêu ý trái ngược với điều vừa nói.
tuy rằng|Mặc dù, dùng để mở đầu một ý trái với điều nói sau.
tuy vậy|Dù là như thế, dùng để nối sang một ý trái ngược.
tuyến|Đường đi cố định theo lộ trình nhất định của xe cộ, tàu bè.
tuyên bố|Nói ra một cách chính thức, công khai cho mọi người biết.
tuyển chọn|Chọn lọc kỹ để lấy những người hoặc thứ tốt nhất.
tuyển dụng|Tìm và nhận người vào làm việc cho cơ quan, công ty.
tuyến đường|Con đường hoặc lộ trình đi lại từ nơi này đến nơi khác.
tuyển sinh|Xét chọn và nhận học sinh, sinh viên vào trường.
tuyển tập|Cuốn sách tập hợp những tác phẩm hay được chọn lọc.
tuyển thủ|Vận động viên được chọn vào đội tuyển để thi đấu.
tuyết|Những tinh thể băng nhỏ màu trắng, rơi xuống như bông khi trời rất lạnh.
tuyệt chiêu|Cách làm hay hoặc chiêu thức cực giỏi, ít ai biết.
tuyệt chủng|Mất hẳn nòi giống, cả loài không còn cá thể nào tồn tại.
tuyệt diệu|Hay và đẹp đến mức kỳ diệu, khó gì sánh bằng.
tuyệt đỉnh|Đạt đến mức cao nhất, không còn gì hơn.
tuyệt đối|Hoàn toàn, trọn vẹn, không có ngoại lệ nào.
tuyệt hảo|Tốt đến mức hoàn hảo, không chê vào đâu được.
tuyệt phẩm|Tác phẩm hoặc sản phẩm cực kỳ xuất sắc.
tuyệt tác|Tác phẩm nghệ thuật đặc sắc, có giá trị rất cao.
tuyệt vời|Hay, đẹp hoặc tốt đến mức hết sức, đáng khen ngợi.
tự ái|Dễ phật ý, thấy bị tổn thương khi bị chê hay trêu chọc.
từ biệt|Chào tạm biệt để chia tay, thường trước khi đi xa lâu ngày.
từ bỏ|Thôi không làm, không giữ hay theo đuổi điều gì nữa.
tư cách|Phẩm chất, đạo đức của một người; cũng chỉ vai trò, danh nghĩa.
tự cao|Tự đánh giá mình quá cao, hay xem thường người khác.
tự chế|Tự tay làm ra bằng những gì có sẵn, không phải đồ mua ở cửa hàng.
từ chối|Không nhận hoặc không đồng ý với lời mời, lời đề nghị.
tự do|Được làm theo ý mình, không bị ai ép buộc hay ngăn cản.
tư duy|Quá trình suy nghĩ, phân tích để hiểu và giải quyết vấn đề.
tự dưng|Bỗng nhiên xảy ra, không rõ vì sao.
từ đầu|Ngay từ lúc mới bắt đầu, từ điểm xuất phát.
từ đây|Kể từ nơi này hoặc từ lúc này trở về sau.
tự động|Tự vận hành, không cần người điều khiển trực tiếp; cũng chỉ tự ý làm.
tự giác|Tự mình làm việc cần làm mà không cần ai nhắc nhở.
tự hào|Hãnh diện, vui mừng về điều tốt đẹp của mình hoặc của người thân.
tự học|Tự mình tìm tòi, học hỏi, không cần người dạy trực tiếp.
tự hỏi|Thắc mắc trong lòng, tự đặt câu hỏi cho chính mình.
tứ kết|Vòng đấu có tám đội, chọn ra bốn đội vào bán kết.
tự lập|Tự lo liệu cuộc sống, không dựa dẫm vào người khác.
tự nguyện|Tự mình muốn làm, không bị ai bắt buộc.
từ ngữ|Các từ và cụm từ trong một ngôn ngữ nói chung.
tư nhân|Thuộc về cá nhân, không phải của nhà nước.
tự nhiên|Trời đất, cây cỏ quanh ta; cũng chỉ sự thoải mái, không gượng gạo.
tự nhủ|Tự nói thầm với chính mình, thường để nhắc nhở hay động viên.
tử số|Số viết ở phía trên dấu gạch ngang của một phân số.
tử tế|Tốt bụng, đàng hoàng, đối xử tốt với người khác.
tư thế|Dáng người khi đứng, ngồi hoặc nằm.
từ thiện|Giúp đỡ người khó khăn bằng tiền, đồ dùng hay công sức, không vụ lợi.
tư thục|Trường học do tư nhân lập ra và quản lý.
tự tiện|Tự ý làm điều gì mà không xin phép người khác.
tự tin|Tin vào khả năng của bản thân, không rụt rè.
từ tốn|Thong thả, nhẹ nhàng và điềm đạm trong lời nói, cử chỉ.
tự trọng|Biết giữ gìn phẩm giá và danh dự của bản thân.
từ trường|Vùng không gian quanh nam châm hay dòng điện, nơi có lực từ tác dụng.
tự túc|Tự lo liệu lấy những thứ mình cần, không trông chờ người khác.
tứ tung|Bừa bãi ra khắp nơi, không theo thứ tự nào.
từ từ|Chậm rãi, thong thả, từng chút một, không vội vàng.
tư vấn|Đưa ra lời khuyên, góp ý cho người cần giúp.
từ vựng|Tập hợp các từ của một ngôn ngữ, hoặc số từ mà một người biết.
tựa đề|Tên của một bài viết, cuốn sách, bộ phim hay bài hát.
tức cười|Gây buồn cười, khiến người ta không nhịn được cười.
tức giận|Bực bội, nổi giận khi gặp điều trái ý mình.
tức là|Từ nối dùng để giải thích, nói rõ hơn điều vừa nêu.
tức thì|Ngay lập tức, xảy ra liền mà không phải chờ đợi.
tức thời|Ngay lập tức, xảy ra liền ngay lúc đó.
tức tối|Bực bội, ấm ức trong lòng vì điều không như ý.
tưng bừng|Rộn ràng, náo nhiệt và vui vẻ, như ngày hội.
từng trải|Đã trải qua nhiều việc nên có nhiều kinh nghiệm sống.
tươi|Còn mới, chưa héo, chưa khô; cũng chỉ vẻ mặt vui vẻ, rạng rỡ.
tươi cười|Có vẻ mặt vui vẻ, luôn nở nụ cười.
tươi đẹp|Đẹp đẽ, tươi sáng và đầy sức sống.
tươi mát|Mát mẻ và tràn đầy sức sống, đem lại cảm giác dễ chịu.
tươi rói|Rất tươi, như vừa mới hái hay vừa đánh bắt; cũng chỉ nụ cười rạng rỡ.
tươi sáng|Sáng sủa, rực rỡ; cũng chỉ tương lai tốt đẹp, đầy hy vọng.
tươi sống|Còn tươi nguyên, chưa qua nấu nướng hay chế biến.
tươi tắn|Vui vẻ, rạng rỡ, trông rất dễ chịu.
tươi thắm|Tươi tắn và có màu sắc rực rỡ, đậm đà.
tươi tỉnh|Vẻ mặt vui vẻ, tỉnh táo, không còn mệt mỏi.
tươi tốt|Cây cối xanh mướt, phát triển mạnh.
tươi vui|Vui vẻ, phấn khởi và tràn đầy niềm vui sống.
tường|Khối xây bằng gạch, đá dựng đứng để ngăn chia hoặc bao quanh nhà.
tưởng bở|Cứ nghĩ là dễ dàng, có lợi cho mình nhưng thực ra không phải.
tưởng chừng|Ngỡ như là vậy, nhưng thực tế có thể khác.
tượng đài|Công trình có tượng lớn dựng nơi công cộng để ghi nhớ người hay sự kiện.
tương đối|Ở mức khá, chưa hoàn toàn; không phải tuyệt đối.
tương đương|Ngang bằng nhau về giá trị, mức độ hoặc số lượng.
tương lai|Khoảng thời gian sẽ đến sau hiện tại.
tương ớt|Nước chấm sệt làm từ ớt xay, có vị cay.
tương phản|Trái ngược hẳn nhau, làm nổi bật sự khác biệt.
tương tác|Tác động qua lại lẫn nhau giữa người với người hoặc vật với vật.
tương thích|Phù hợp với nhau, có thể hoạt động cùng nhau mà không trục trặc.
tường thuật|Kể lại diễn biến của một sự việc cho người khác biết.
tượng trưng|Dùng một hình ảnh, sự vật để đại diện cho một ý nghĩa.
tương tự|Gần giống nhau, na ná như nhau.
tưởng tượng|Hình dung ra trong đầu những điều chưa thấy hoặc không có thật.
tương ứng|Hợp với nhau, khớp nhau theo từng phần, từng cặp.
tựu trường|Ngày học sinh tập trung trở lại trường để chuẩn bị năm học mới.
uể oải|Mệt mỏi, chậm chạp, không có hứng làm việc gì.
um tùm|Cây cối mọc dày đặc, rậm rạp, chen chúc nhau.
ủn ỉn|Tiếng kêu khe khẽ, liên tục của con lợn.
ùn tắc|Tình trạng xe cộ dồn ứ, không lưu thông được.
ủng hộ|Đồng tình, giúp đỡ hoặc góp sức cho người hay việc gì.
uốn cong|Làm cho một vật đang thẳng trở nên cong.
uốn dẻo|Uốn cong người một cách mềm mại, như trong thể dục hay xiếc.
uốn lượn|Cong qua cong lại một cách mềm mại, như dòng sông, con đường.
uốn tóc|Làm cho tóc xoăn hoặc gợn sóng bằng dụng cụ hay thuốc.
uống|Đưa nước hay chất lỏng vào miệng rồi nuốt xuống.
uổng công|Mất công sức mà không đạt được kết quả gì.
úp mở|Nói không rõ ràng, nửa kín nửa hở, để người nghe tự đoán.
uy lực|Sức mạnh to lớn, gây ấn tượng và khiến người khác phải nể.
uy tín|Sự tin tưởng, tín nhiệm mà mọi người dành cho một người hay một nơi.
uyển chuyển|Mềm mại, nhịp nhàng trong cử động; cũng chỉ cách làm linh hoạt.
ưa chuộng|Yêu thích và hay chọn dùng hơn những thứ khác.
ưa nhìn|Có vẻ ngoài dễ coi, nhìn thấy dễ chịu.
ưa thích|Cảm thấy thích và muốn có, muốn làm điều gì.
ức chế|Cảm giác bực bội dồn nén trong lòng; cũng chỉ việc kìm hãm hoạt động.
ứng biến|Nhanh trí xử lý khi gặp tình huống bất ngờ.
ứng dụng|Đem kiến thức vào thực tế; cũng chỉ phần mềm trên điện thoại, máy tính.
ửng đỏ|Chuyển sang màu đỏ hồng nhẹ, như má hay quả chín.
ửng hồng|Hơi đỏ hồng lên, thường nói về má hay bầu trời.
ứng tuyển|Nộp hồ sơ để xin vào làm một công việc hay vị trí.
ứng viên|Người đăng ký dự tuyển cho một vị trí hay cuộc bầu chọn.
ưng ý|Thấy vừa lòng, hài lòng với điều mình chọn hay nhận được.
ước ao|Mong muốn tha thiết có được điều gì.
ước gì|Lời bày tỏ mong muốn, giá như điều gì đó trở thành sự thật.
ước lượng|Đoán, tính sơ bộ số lượng hay kích thước mà không đo chính xác.
ước mong|Mong muốn, hy vọng điều tốt đẹp sẽ đến.
ước mơ|Điều tốt đẹp mình mong muốn đạt được trong tương lai.
ước muốn|Điều mình mong muốn có được hoặc đạt được.
ước tính|Tính toán sơ bộ để ra con số gần đúng.
ương bướng|Bướng bỉnh, không chịu nghe lời người khác.
ướp lạnh|Để trong đá hay tủ lạnh cho mát lạnh hoặc giữ tươi lâu.
ướt đẫm|Thấm nước nhiều đến mức sũng ướt, như áo ướt đẫm mồ hôi.
ướt nhẹp|Thấm nước khắp nơi, ướt đẫm và bết dính lại.
ướt sũng|Ngấm đầy nước đến mức như có thể vắt ra được.
ưu ái|Dành sự quan tâm, đối xử đặc biệt tốt cho ai.
ưu đãi|Dành điều kiện tốt hơn bình thường, như giảm giá hay quà tặng.
ưu điểm|Điểm tốt, mặt mạnh của người hay sự vật.
ưu thế|Lợi thế, điểm mạnh giúp chiếm phần hơn so với bên khác.
ưu tiên|Được dành phần trước, được chú ý hay làm trước những việc khác.
va đập|Chạm mạnh vào nhau hoặc vào vật khác khi chuyển động.
vả lại|Dùng để nói thêm một lý do bổ sung cho điều vừa nêu.
vạch|Đường kẻ dài và thẳng, như trên mặt đường; cũng là kẻ thành nét.
vách đá|Sườn núi đá dựng đứng, cao và rất dốc.
vách ngăn|Tấm chắn dùng để chia một căn phòng thành các khu riêng.
vạch ra|Nêu ra rõ ràng, phác thảo trước một kế hoạch hay hướng đi.
vài ba|Một số lượng ít, khoảng hai hoặc ba.
vải bông|Loại vải dệt từ sợi bông, mềm, mát và thấm hút tốt.
vải thiều|Giống vải quả tròn vỏ đỏ, cùi dày, hạt nhỏ, ăn rất ngọt và thơm.
vai trò|Chức năng, phần việc của ai hay cái gì trong một việc chung.
vải vóc|Các loại vải dùng để may mặc nói chung.
vali|Hòm đựng đồ có quai xách, thường có bánh xe, dùng khi đi xa.
vạm vỡ|Thân hình to lớn, khỏe mạnh và rắn chắc.
vạn thọ|Loài hoa màu vàng cam, cánh xếp dày, thường được bày vào dịp Tết.
vạn vật|Tất cả mọi vật, mọi loài trong trời đất.
vàng|Kim loại quý óng ánh, làm trang sức; cũng là màu của nắng, hoa cúc.
vàng anh|Loài chim nhỏ có bộ lông vàng tươi, hót rất hay.
vàng bạc|Kim loại quý như vàng, bạc; nói chung là của cải quý giá.
vang dội|Có tiếng vang to và lan xa; cũng chỉ thành công lớn, nổi tiếng.
vàng hoe|Có màu vàng tươi, sáng nhạt, như nắng hay lúa chín.
vàng óng|Có màu vàng bóng mượt và lấp lánh.
vàng rực|Có màu vàng tươi, sáng rực rỡ.
vàng thỏi|Kim loại vàng đúc thành khối dài, dùng để cất giữ hoặc mua bán.
vàng vàng|Hơi ngả sang màu vàng, không đậm lắm.
vành|Phần viền tròn bao quanh mép một vật, như vành nón, vành xe.
vành đai|Dải đất hoặc tuyến đường chạy vòng quanh một khu vực, thành phố.
vành tai|Phần mỏng, cong bao quanh bên ngoài của tai.
vani|Hương liệu thơm dịu lấy từ quả một loài lan, dùng làm bánh, kem.
vào cuộc|Bắt đầu tham gia vào một việc hay giải quyết một vấn đề.
vào khoảng|Gần đúng, xấp xỉ một con số hay thời điểm nào đó.
vào vai|Diễn hoặc đóng một nhân vật trong phim, kịch hay trò chơi.
váy áo|Quần áo, trang phục nói chung, thường nói về phụ nữ.
váy đầm|Trang phục nữ dạng váy, thường may liền từ trên xuống.
vay mượn|Mượn tiền bạc hay đồ vật của người khác, sau này sẽ trả lại.
văn bản|Tài liệu được viết hoặc in ra, như thư, quyết định, hợp đồng.
văn chương|Các tác phẩm thơ, truyện giàu cảm xúc và hình ảnh; cũng chỉ lời văn hay.
văn học|Nghệ thuật dùng ngôn từ để sáng tác, gồm thơ, truyện, kịch.
văn minh|Trình độ phát triển cao của xã hội; cũng chỉ lối sống lịch sự, có ý thức.
văn nghệ|Các hoạt động nghệ thuật như ca hát, múa, diễn kịch.
văn phòng|Nơi làm việc giấy tờ, giao dịch của một cơ quan hay công ty.
văn xuôi|Lối văn viết bình thường, không theo vần điệu như thơ.
vắng bóng|Không còn thấy xuất hiện ở nơi quen thuộc nữa.
vắng lặng|Không có người, im ắng và yên tĩnh.
vắng mặt|Không có mặt ở nơi lẽ ra phải có mặt.
vắng tanh|Không có lấy một bóng người, hoàn toàn trống trải.
vắng vẻ|Ít người qua lại, yên tĩnh, quạnh hiu.
vận chuyển|Chuyển, chở hàng hóa hoặc người từ nơi này sang nơi khác.
vận dụng|Đem điều đã học, đã biết áp dụng vào việc cụ thể.
vấn đề|Điều cần xem xét, giải quyết hoặc bàn bạc.
vận động|Cử động, tập luyện cơ thể; cũng chỉ việc kêu gọi mọi người cùng tham gia.
vận hành|Điều khiển, cho máy móc hay một hệ thống hoạt động.
vận mệnh|Số phận, con đường tương lai của một người hay một dân tộc.
vận tải|Việc chuyên chở hàng hóa, hành khách bằng xe, tàu, máy bay.
vận tốc|Quãng đường đi được trong một đơn vị thời gian, cho biết độ nhanh chậm.
vân vân|Dùng ở cuối khi liệt kê, ý nói còn nhiều thứ tương tự.
vẩn vơ|Lan man, không có mục đích hay chủ đích rõ ràng.
vâng lời|Nghe theo và làm đúng lời người lớn dặn bảo.
vấp váp|Gặp trục trặc, sai sót hay khó khăn khi làm việc, nói năng.
vật chất|Những gì có thật, sờ thấy được; cũng chỉ tiền bạc, của cải.
vật dụng|Đồ dùng cần thiết trong sinh hoạt hay công việc hằng ngày.
vật liệu|Thứ dùng để làm nên đồ vật hay công trình, như gỗ, gạch, sắt.
vật nuôi|Những con vật được con người nuôi, như chó, mèo, gà, lợn.
vật phẩm|Đồ vật, sản phẩm có giá trị sử dụng hoặc làm quà tặng.
vật thể|Thứ có hình dạng nhất định, chiếm một chỗ trong không gian.
vật tư|Nguyên liệu, máy móc, dụng cụ cần cho sản xuất và xây dựng.
vất vả|Mệt nhọc, phải bỏ ra nhiều công sức, chịu nhiều khó khăn.
vây cá|Bộ phận mỏng trên thân cá, giúp cá bơi và giữ thăng bằng.
vẫy gọi|Đưa tay ra hiệu để gọi ai đến; nghĩa bóng là thu hút, mời gọi.
vậy mà|Dùng để nối hai ý, khi điều xảy ra trái với mong đợi.
vậy nên|Dùng để nêu kết quả, hệ quả của điều vừa nói.
vây quanh|Tụ lại hoặc bao kín xung quanh ai hay vật gì.
vẫy tay|Đưa bàn tay qua lại để chào hoặc ra hiệu.
vậy thì|Dùng để rút ra kết luận hay đưa ra ý kiến tiếp theo.
vẻ mặt|Nét biểu hiện trên khuôn mặt, cho thấy cảm xúc của một người.
vẻ ngoài|Hình dáng, dáng vẻ bên ngoài mà người khác nhìn thấy.
ve sầu|Côn trùng có cánh trong, kêu ra rả trên cây vào mùa hè.
ven biển|Phần đất nằm sát và chạy dọc theo bờ biển.
về già|Khoảng thời gian khi con người đã nhiều tuổi.
về hưu|Nghỉ làm việc khi đến tuổi theo quy định và nhận lương hưu.
về quê|Trở về quê nhà, nơi mình sinh ra hoặc có gia đình.
vệ sinh|Giữ sạch sẽ để bảo vệ sức khỏe; cũng chỉ việc lau dọn, làm sạch.
vệ tinh|Thiên thể hay thiết bị bay vòng quanh một hành tinh, như Mặt Trăng.
về vườn|Thôi công việc để về sống an nhàn; cũng nói vui là bị cho nghỉ việc.
vênh váo|Tỏ vẻ kiêu ngạo, tự đắc, coi thường người khác.
vết nhăn|Nếp gấp nhỏ trên da, thường xuất hiện khi lớn tuổi; cũng có ở vải.
vỉa hè|Phần đường dành cho người đi bộ, nằm hai bên lòng đường.
video|Đoạn phim ghi lại hình ảnh và âm thanh để xem trên màn hình.
việc|Điều phải làm hoặc công việc hằng ngày; cũng chỉ chuyện xảy ra.
việc gì|Chuyện gì, điều gì; cũng dùng để nói không cần phải làm vậy.
việc làm|Công việc được trả lương để kiếm sống; cũng chỉ hành động cụ thể.
việc nhà|Những công việc trong gia đình như nấu ăn, dọn dẹp, giặt giũ.
viền|Đường chạy dọc theo mép một vật, như mép áo, mép khăn.
viễn cảnh|Cảnh tượng hoặc tình hình có thể xảy ra trong tương lai.
viên chức|Người làm việc lâu dài, hưởng lương ở các đơn vị nhà nước.
viễn thông|Việc truyền tin đi xa bằng điện thoại, mạng, sóng vô tuyến.
viễn tưởng|Điều tưởng tượng về tương lai hay thế giới khác, như trong phim khoa học.
viển vông|Không thực tế, khó có thể trở thành hiện thực.
viếng thăm|Đến thăm một nơi hay một người, thường mang tính trang trọng.
viết|Dùng bút hoặc bàn phím ghi ra chữ; cũng chỉ việc sáng tác bài, sách.
viết hoa|Dùng chữ cái cỡ lớn, như ở đầu câu hay đầu tên riêng.
viết lách|Việc viết văn, viết bài nói chung, như một sở thích hay nghề.
viết máy|Bút có ống chứa mực bên trong, ngòi kim loại, viết được lâu.
viết tay|Được viết trực tiếp bằng bút, không phải đánh máy hay in.
vịnh|Vùng biển lõm sâu vào đất liền, ba phía có bờ bao quanh.
vĩnh cửu|Tồn tại mãi mãi, không bao giờ mất đi.
vinh dự|Niềm tự hào khi được tin tưởng, khen ngợi hay giao trọng trách.
vinh hạnh|Cảm thấy vui và hân hạnh, thường nói lịch sự khi được gặp ai đó.
vinh quang|Niềm vẻ vang, danh tiếng rực rỡ có được nhờ thành công lớn.
vĩnh viễn|Mãi mãi, không bao giờ thay đổi hay kết thúc.
visa|Giấy phép cho người nước ngoài vào một quốc gia, còn gọi là thị thực.
vịt trời|Loài vịt hoang dã, biết bay xa, sống ở đầm hồ.
vitamin|Chất cơ thể cần một lượng nhỏ để khỏe mạnh, có nhiều trong rau quả.
vỏ chai|Chiếc chai đã dùng hết, chỉ còn lại cái vỏ rỗng.
vỏ chăn|Lớp vải bọc ngoài ruột chăn, có thể tháo ra giặt.
vỏ chuối|Lớp vỏ bên ngoài của quả chuối.
vỏ sò|Lớp vỏ cứng của con sò, hay được nhặt ở bãi biển để trang trí.
vóc dáng|Hình dáng, tầm vóc của cơ thể một người.
vòi nước|Đầu ống có van để mở, đóng cho nước chảy ra.
vòi sen|Đầu vòi có nhiều lỗ nhỏ, phun nước như mưa để tắm.
vòi voi|Phần mũi dài và mềm của con voi, dùng để cầm nắm, hút nước.
vỏn vẹn|Chỉ có đúng chừng ấy, rất ít ỏi.
vòng|Đường cong khép kín hình tròn; cũng chỉ đồ trang sức đeo ở cổ, tay.
vòng cổ|Đồ trang sức đeo quanh cổ; cũng chỉ vòng đeo cổ cho thú cưng.
vòng cung|Đường cong như một phần của hình tròn, giống cầu vồng.
vòng đua|Một vòng chạy trọn quanh đường đua; cũng chỉ một cuộc đua.
vòng quanh|Đi theo một vòng bao quanh nơi nào đó; cũng chỉ đi khắp mọi nơi.
vòng quay|Một lần quay hết một vòng; cũng chỉ sự lặp đi lặp lại không ngừng.
vòng tay|Hai cánh tay vòng lại để ôm ai; cũng chỉ đồ trang sức đeo cổ tay.
vòng tròn|Đường cong khép kín, mọi điểm cách đều một điểm ở giữa.
vòng vèo|Quanh co, uốn lượn nhiều khúc, không đi thẳng.
vòng vo|Nói quanh co, không đi thẳng vào vấn đề chính.
vô bổ|Không mang lại lợi ích gì, chỉ tốn thời gian.
vô cớ|Không có lý do gì, không chính đáng.
vô cùng|Hết sức, cực kỳ; cũng chỉ điều không có giới hạn.
vô danh|Không có tên hoặc không được ai biết đến tên tuổi.
vô duyên|Thiếu duyên, nói năng hay cư xử không đúng lúc, khiến người khác khó chịu.
vô địch|Giành vị trí thứ nhất, thắng tất cả đối thủ trong một giải đấu.
vô giá|Quý đến mức không thể tính bằng tiền.
vô hại|Không gây ra tác hại hay nguy hiểm gì.
vô hạn|Không có giới hạn, không bao giờ hết.
vô hiệu|Không còn tác dụng hoặc không có giá trị.
vô hình|Không có hình dạng, không nhìn thấy được.
vô ích|Không có ích lợi gì, không mang lại kết quả.
vô kể|Nhiều đến mức không đếm xuể.
vô lễ|Thiếu lễ phép, không tôn trọng người lớn.
vô nghĩa|Không có ý nghĩa hoặc không có giá trị gì.
vỗ tay|Đập hai lòng bàn tay vào nhau thành tiếng để khen hay cổ vũ.
vô tâm|Không để ý, không quan tâm đến cảm xúc của người khác.
vô tận|Không bao giờ hết, không có điểm kết thúc.
vô thức|Xảy ra hoặc làm mà bản thân không nhận biết, không chủ ý.
vô tình|Không cố ý, tình cờ xảy ra; cũng chỉ sự thờ ơ, thiếu tình cảm.
vô tuyến|Truyền tín hiệu bằng sóng, không cần dây dẫn; cũng là cách gọi tivi.
vô tư|Hồn nhiên, không lo nghĩ gì; cũng chỉ sự công bằng, không thiên vị.
vô vàn|Nhiều đến mức không đếm xuể.
vỗ về|An ủi, dỗ dành nhẹ nhàng cho người khác yên lòng.
vội vã|Gấp gáp, làm thật nhanh vì sợ không kịp.
vội vàng|Làm gì đó thật nhanh, gấp gáp vì sợ không kịp.
vốn liếng|Tiền bạc, của cải hay hiểu biết tích góp được để làm ăn.
vốn sống|Hiểu biết, kinh nghiệm tích lũy được qua cuộc sống.
vợ chồng|Hai người đã kết hôn, cùng chung sống thành gia đình.
vợ con|Gia đình riêng của một người đàn ông, gồm vợ và các con.
vở diễn|Một tác phẩm được dàn dựng và biểu diễn trên sân khấu.
vở kịch|Tác phẩm sân khấu có nhân vật, lời thoại, do diễn viên trình diễn.
vỡ mộng|Điều mình mơ ước, hy vọng bỗng không thành, khiến thất vọng.
với lại|Từ nối dùng khi nói chuyện để bổ sung thêm ý hoặc lý do.
với nhau|Cùng nhau, chỉ sự qua lại giữa hai hay nhiều người.
vũ công|Người chuyên múa, biểu diễn các điệu nhảy trên sân khấu.
vũ đạo|Các động tác múa, nhảy được dàn dựng theo nhạc.
vũ điệu|Một điệu múa, điệu nhảy với những động tác theo nhạc.
vũ hội|Buổi tiệc lớn nơi mọi người ăn mặc đẹp và cùng khiêu vũ.
vú sữa|Loại cây ăn quả, quả tròn có nhựa trắng như sữa, vị ngọt mát.
vũ trụ|Toàn bộ không gian bao la chứa mọi vì sao, hành tinh và thiên hà.
vụ việc|Một sự việc cụ thể đã xảy ra, cần xem xét giải quyết.
vu vơ|Không có mục đích hay đối tượng rõ ràng, như nói hay hát bâng quơ.
vù vù|Tiếng gió thổi hay vật bay nhanh; cũng chỉ sự rất nhanh.
vua chúa|Những người đứng đầu, nắm quyền cai trị đất nước thời phong kiến.
vui chơi|Chơi đùa, giải trí để thấy vui vẻ, thư giãn.
vui cười|Cười nói rộn ràng, tỏ ra vui vẻ, hớn hở.
vùi đầu|Dồn hết tâm trí vào một việc, không để ý chuyện khác.
vui đùa|Chơi đùa, trêu chọc nhau một cách vui vẻ.
vui lòng|Hài lòng, bằng lòng; cũng dùng lịch sự khi đề nghị ai làm gì.
vui mắt|Trông đẹp, sinh động, khiến người nhìn thấy thích thú.
vui mừng|Rất vui, phấn khởi trước một tin tốt hay điều may mắn.
vui nhộn|Sôi nổi, hài hước, mang lại nhiều tiếng cười.
vui sướng|Vui đến mức thấy hạnh phúc, lòng tràn đầy phấn khởi.
vui thích|Cảm thấy vui và hứng thú khi làm hay có được điều gì.
vui tính|Tính tình cởi mở, hay pha trò, dễ làm người khác vui.
vui tươi|Tươi tắn, hớn hở và tràn đầy sức sống.
vui vẻ|Tâm trạng thoải mái, hay cười nói, khiến người khác dễ chịu.
vun đắp|Chăm chút, bồi đắp dần cho thêm bền chặt, như tình cảm, gia đình.
vụn vặt|Nhỏ nhặt, rời rạc và không mấy quan trọng.
vun vén|Chăm lo, gom góp từng chút để xây dựng gia đình, cuộc sống.
vũng|Chỗ trũng có nước đọng lại trên mặt đất.
vùng biển|Khu vực mặt biển rộng lớn, thường thuộc về một nước hay một miền.
vũng bùn|Chỗ trũng lầy lội, có nước đọng lẫn bùn đất.
vùng cao|Miền đất cao nhiều đồi núi, thường xa thành phố.
vùng đất|Một khu vực đất đai rộng lớn, có những nét riêng.
vũng lầy|Chỗ đất trũng đầy bùn nhão, dễ bị lún chân.
vùng trời|Khoảng trời bao trùm phía trên một khu vực.
vung vãi|Rơi rớt, tung tóe ra nhiều chỗ một cách bừa bãi.
vùng vẫy|Cựa quậy, quẫy đạp mạnh; cũng chỉ việc tự do hoạt động thỏa sức.
vùng ven|Khu vực nằm ở rìa, giáp ranh thành phố hoặc thị trấn.
vụng về|Không khéo tay, lóng ngóng, dễ làm hỏng việc.
vuông|Có hình bốn cạnh bằng nhau, bốn góc đều bằng chín mươi độ.
vuông góc|Hai đường cắt nhau tạo thành góc chín mươi độ.
vuông vắn|Ngay ngắn, cân đối, các góc cạnh rõ ràng như hình vuông.
vuốt ve|Lấy tay xoa nhẹ nhiều lần để âu yếm, vỗ về.
vừa lòng|Thấy hài lòng vì đúng như mong muốn.
vựa lúa|Kho chứa lúa; cũng chỉ vùng sản xuất nhiều lúa gạo.
vừa miệng|Món ăn nêm nếm đậm nhạt vừa phải, ăn thấy ngon.
vừa mới|Chỉ mới xảy ra cách đây một lúc ngắn.
vừa nãy|Lúc trước đây không lâu, cách bây giờ một chút.
vừa phải|Ở mức trung bình, không quá nhiều cũng không quá ít.
vừa qua|Mới trôi qua gần đây nhất, như tuần trước, năm trước.
vừa rồi|Cách đây không lâu, ngay trước lúc đang nói.
vừa sức|Phù hợp với khả năng, sức lực của mình.
vừa vặn|Đúng kích cỡ, không rộng cũng không chật.
vừa vừa|Ở mức tương đối, không nhiều quá cũng không ít quá.
vừa ý|Đúng như mình muốn, khiến mình hài lòng.
vững chắc|Chắc chắn, bền vững, khó bị lay động hay đổ vỡ.
vững vàng|Đứng chắc, ổn định; cũng chỉ tinh thần không dễ dao động.
vườn|Khoảng đất để trồng cây, hoa hoặc rau, thường ở quanh nhà.
vườn hoa|Khu đất trồng nhiều loại hoa để ngắm, thường có lối đi dạo.
vườn hồng|Khu vườn trồng hoa hồng hoặc trồng cây hồng lấy quả.
vươn mình|Duỗi người lên cao; thường chỉ sự lớn mạnh, phát triển vượt bậc.
vườn rau|Mảnh đất dùng để trồng các loại rau ăn hằng ngày.
vườn thú|Nơi nuôi nhiều loài động vật cho mọi người đến xem.
vươn tới|Nỗ lực hết mình để đạt được mục tiêu hay ước mơ cao hơn.
vườn trẻ|Nơi trông nom, chăm sóc trẻ nhỏ khi bố mẹ đi làm.
vươn vai|Duỗi thẳng hai tay và căng người ra cho đỡ mỏi.
vướng mắc|Điều khó khăn, trục trặc còn chưa giải quyết được.
vương miện|Mũ đội đầu sang trọng của vua, hoàng hậu hay hoa hậu.
vương quốc|Đất nước có vua hoặc nữ hoàng làm người đứng đầu.
vương vãi|Rơi rớt, nằm rải rác lộn xộn ở nhiều chỗ.
vượt|Đi qua được chỗ khó hay chướng ngại; cũng chỉ hơn hẳn một mức nào đó.
vượt qua|Đi qua được hoặc chiến thắng khó khăn, thử thách.
vứt bỏ|Ném đi, bỏ đi vì không còn cần đến.
xà bông|Chất tẩy rửa dùng khi tắm, giặt, cách gọi phổ biến ở miền Nam.
xa cách|Ở xa nhau, không được gần gũi, gặp gỡ.
xã giao|Cách cư xử lịch sự khi giao tiếp, thường ở mức quen biết bình thường.
xa hoa|Sang trọng, đắt tiền đến mức phô trương, phung phí.
xã hội|Cộng đồng con người cùng chung sống, gắn bó theo những quy tắc chung.
xa lạ|Chưa từng quen biết, không thân thuộc.
xà lách|Loại rau lá xanh mềm, thường ăn sống hoặc trộn dầu giấm.
xa lánh|Tránh không gặp gỡ, không muốn gần gũi với ai hay điều gì.
xà ngang|Thanh gỗ hay sắt đặt nằm ngang; cũng chỉ thanh ngang trên khung thành.
xà phòng|Chất tạo bọt dùng để rửa tay, tắm và giặt giũ.
xa tít|Rất xa, xa đến mức nhìn không rõ.
xa vời|Ở rất xa, khó mà với tới hay đạt được.
xa xa|Ở một khoảng cách hơi xa, vẫn còn trông thấy được.
xa xỉ|Đắt tiền, sang trọng, vượt quá nhu cầu cần thiết.
xá xíu|Thịt heo tẩm ướp gia vị màu đỏ rồi nướng hoặc quay, kiểu người Hoa.
xa xôi|Ở rất xa, cách trở, khó đi lại.
xa xưa|Thuộc về thời rất lâu trước đây.
xác định|Tìm ra hoặc nêu rõ một cách chắc chắn điều gì đó.
xác minh|Kiểm tra để biết chắc điều gì đúng hay sai.
xác nhận|Khẳng định điều gì là đúng sự thật hoặc đã đồng ý.
xác thực|Đúng với sự thật; cũng là kiểm tra để chứng nhận danh tính, tài khoản.
xách|Cầm quai hay phần trên của vật để mang đi, vật buông thõng xuống.
xách tay|Gọn nhẹ, cầm tay mang theo được; cũng chỉ hàng mang từ nước ngoài về.
xám xịt|Màu xám tối, u ám, như bầu trời sắp mưa.
xanh|Màu của lá cây tươi hoặc của bầu trời trong; cũng chỉ quả chưa chín.
xanh biếc|Màu xanh đậm và tươi trong, như nước hồ hay bầu trời.
xanh dương|Màu xanh giống bầu trời trong hoặc nước biển.
xanh lam|Màu xanh da trời đậm, hơi ngả sang màu chàm.
xanh lè|Xanh đậm đến chói mắt, thường nói về trái cây còn non.
xanh lục|Màu xanh giống màu lá cây tươi.
xanh mướt|Xanh tươi và mỡ màng, trông mượt mà, đầy sức sống.
xanh ngắt|Xanh đậm và tươi, trải rộng một màu, như bầu trời.
xanh tốt|Cây cối mọc tốt, lá xanh và tươi.
xanh tươi|Có màu xanh mơn mởn, tràn đầy sức sống.
xanh xanh|Có màu xanh nhạt, chỉ hơi xanh một chút.
xào nấu|Chế biến các món ăn bằng cách xào, nấu nói chung.
xào xạc|Âm thanh nhẹ của lá cây cọ vào nhau khi gió thổi.
xao xuyến|Lòng rung động, bồi hồi khó tả khi nhớ hay gặp điều gì.
xăng|Nhiên liệu lỏng dễ cháy, dùng cho xe máy, ô tô.
xăng dầu|Nhiên liệu nói chung như xăng, dầu, dùng cho xe cộ, máy móc.
xấp xỉ|Gần bằng nhau, chỉ chênh lệch một chút.
xấu hổ|Ngượng ngùng, thấy ngại vì lỗi của mình hoặc khi bị chú ý.
xấu mặt|Mất thể diện, bị chê cười trước mặt mọi người.
xấu tính|Có tính nết không tốt, hay ích kỷ, khó chịu.
xấu xa|Không tốt về tính cách, đạo đức, đáng chê trách.
xấu xí|Có hình dáng, vẻ ngoài không đẹp, khó ưa nhìn.
xây dựng|Làm nên nhà cửa, công trình; cũng chỉ tạo dựng, phát triển điều gì.
xây đắp|Xây dựng, vun đắp cho ngày càng vững bền.
xe ben|Xe tải có thùng nâng lên được để đổ hàng như cát, đá.
xe bò|Loại xe thô sơ do bò kéo, thường dùng chở đồ ở nông thôn.
xe buýt|Ô tô chở khách chạy theo tuyến cố định, dừng đón trả ở các trạm.
xe cộ|Các loại xe đi lại trên đường nói chung.
xe đạp|Xe hai bánh, người đi dùng chân đạp cho bánh quay.
xe điện|Phương tiện chạy bằng năng lượng điện, như xe máy điện, tàu điện.
xe đò|Ô tô chở khách đường dài, cách gọi quen thuộc ở miền Nam.
xe hơi|Phương tiện bốn bánh chạy bằng động cơ, còn gọi là ô tô.
xe kéo|Loại xe chở khách do người kéo thời xưa; cũng chỉ xe dùng để kéo xe khác.
xe khách|Ô tô lớn chở hành khách đi đường dài giữa các tỉnh, thành.
xe lu|Loại xe nặng có trục lăn lớn, dùng để nén phẳng mặt đường.
xe lửa|Đoàn toa chạy trên đường ray, còn gọi là tàu hỏa.
xe máy|Phương tiện hai bánh có động cơ, rất phổ biến ở Việt Nam.
xe ngựa|Cỗ xe do ngựa kéo, dùng chở người hay hàng hóa thời xưa.
xe nôi|Xe nhỏ có mui che, dùng để đẩy em bé đi dạo.
xe ôm|Dịch vụ chở khách bằng xe máy để lấy tiền.
xe rác|Loại xe chuyên đi thu gom và chở rác thải.
xe tải|Ô tô có thùng lớn, chuyên dùng để chở hàng hóa.
xé toạc|Làm rách mạnh, tạo thành một đường toác rộng.
xem lại|Kiểm tra lại hoặc xem thêm lần nữa cho chắc chắn.
xem nhẹ|Coi là không quan trọng, không chú ý đúng mức.
xem ra|Nhìn qua thì thấy có vẻ như vậy, dùng khi nhận xét.
xem thường|Coi nhẹ, không tôn trọng hoặc cho là thấp kém hơn mình.
xem xét|Nhìn kỹ, cân nhắc cẩn thận trước khi quyết định.
xen kẽ|Xếp lẫn vào nhau, cứ cái này rồi đến cái kia.
xen lẫn|Cái này chen vào giữa cái kia, trộn lẫn với nhau.
xẻng|Dụng cụ có lưỡi sắt rộng và cán dài, dùng để xúc đất, cát.
xế chiều|Lúc mặt trời đã ngả về chiều; cũng chỉ tuổi già.
xê dịch|Dời đi một chút cho khác chỗ; giới trẻ còn dùng để chỉ đi du lịch.
xếp bằng|Ngồi bắt chéo hai chân trước mặt, lưng giữ thẳng.
xếp hàng|Đứng nối đuôi nhau theo thứ tự để chờ đến lượt.
xếp loại|Đánh giá và chia thành các hạng theo mức độ, như học lực.
xì dầu|Nước chấm màu nâu làm từ đậu nành lên men, vị mặn.
xi măng|Bột màu xám trộn với cát và nước, đông cứng lại, dùng để xây dựng.
xí muội|Món ô mai làm từ quả mơ hay mận, vị chua ngọt mặn.
xi nhan|Đèn báo rẽ trên xe; cũng chỉ việc bật đèn báo trước khi rẽ.
xì xào|Nhiều người nói nhỏ, bàn tán với nhau.
xì xầm|Nói nhỏ với nhau, bàn tán không cho người khác nghe rõ.
xích|Dây gồm nhiều mắt kim loại nối nhau, như ở xe đạp; cũng là dịch lại gần.
xích đạo|Đường tưởng tượng chạy vòng quanh giữa Trái Đất, chia ra bán cầu Bắc và Nam.
xích đu|Ghế hoặc tấm ván treo bằng dây, đưa qua đưa lại để chơi.
xích lô|Xe ba bánh đạp bằng chân, chở khách ngồi phía trước.
xích mích|Va chạm nhỏ, bất hòa giữa hai người hay hai bên.
xiếc|Loại hình biểu diễn khéo léo như nhào lộn, tung hứng, thú diễn trò.
xiên|Que nhọn dùng xâu thức ăn để nướng; cũng chỉ hướng chéo, nghiêng.
xin lỗi|Nói lời nhận lỗi với người khác; cũng là câu lịch sự khi làm phiền ai.
xin phép|Hỏi và chờ được đồng ý trước khi làm việc gì.
xin việc|Nộp đơn, hồ sơ để mong được nhận vào làm ở một nơi.
xin xỏ|Năn nỉ hỏi xin người khác nhiều lần, thường mang ý chê bai.
xinh|Có vẻ ngoài đẹp, dễ thương và ưa nhìn.
xinh đẹp|Có vẻ đẹp ưa nhìn, thu hút, thường nói về phụ nữ.
xinh gái|Có gương mặt và dáng vẻ ưa nhìn, thường nói về con gái.
xinh trai|Có gương mặt sáng sủa, ưa nhìn, thường nói về con trai.
xinh tươi|Đẹp đẽ và tươi tắn, trông rạng rỡ, tràn sức sống.
xinh xắn|Đẹp và dễ thương, thường nói về người hay đồ vật nhỏ.
xinh xinh|Nhỏ nhắn, đẹp một cách dễ thương.
xíu mại|Món thịt băm viên tròn, hấp hoặc sốt cà chua, hay ăn với bánh mì.
xoa bóp|Dùng tay xoa và nắn để cơ thể bớt mỏi, dễ chịu.
xoa dịu|Làm cho cảm giác khó chịu, căng thẳng dịu bớt đi.
xoa tay|Chà hai lòng bàn tay vào nhau, khi trời lạnh hoặc khi hài lòng.
xoài|Quả nhiệt đới hình bầu dục, khi chín vàng, ngọt và thơm.
xoay|Quay theo vòng tròn hoặc đổi sang hướng khác.
xoay chuyển|Làm cho tình thế thay đổi theo hướng khác hẳn.
xoay quanh|Quay vòng quanh một điểm; cũng chỉ việc tập trung vào một chủ đề.
xoắn|Vặn cho các sợi quấn chặt vào nhau thành vòng.
xoắn ốc|Hình cuộn vòng như vỏ ốc, càng vào giữa càng nhỏ dần.
xói mòn|Đất đá bị nước, gió bào mòn dần; cũng chỉ sự hao mòn, giảm dần.
xóm giềng|Những người sống gần nhà nhau trong cùng xóm.
xóm làng|Nơi nhiều gia đình cùng sinh sống gần nhau ở nông thôn.
xong|Đã làm hết, hoàn tất, không còn gì phải làm nữa.
xong chuyện|Mọi việc đã được giải quyết, không còn phải bận tâm.
xong xuôi|Hoàn thành hết mọi việc một cách trọn vẹn.
xoong nồi|Các loại xoong, nồi dùng để nấu nướng nói chung.
xô bồ|Lộn xộn, ồn ào, nhiều thứ chen lẫn, không có trật tự.
xối xả|Đổ xuống mạnh và liên tục như mưa lớn; cũng chỉ sự dồn dập.
xôn xao|Ồn ào, rộn lên vì nhiều người cùng bàn tán; cũng chỉ lòng rộn ràng.
xông pha|Dũng cảm lao vào nơi gian khó, không ngại vất vả.
xông xáo|Hăng hái, mạnh dạn lao vào công việc, không ngại khó.
xu hướng|Hướng thay đổi chung, hoặc điều đang được nhiều người ưa chuộng.
xù xì|Bề mặt sần sùi, gồ ghề, không nhẵn.
xua đuổi|Làm cho phải đi chỗ khác, không cho lại gần.
xuân|Mùa đầu năm, trời ấm áp, cây cối đâm chồi nảy lộc; cũng chỉ tuổi trẻ.
xuất bản|In và phát hành sách, báo đến người đọc.
xuất chúng|Tài giỏi vượt trội hơn hẳn mọi người.
xuất hiện|Hiện ra, bắt đầu có mặt cho mọi người nhìn thấy.
xuất khẩu|Đưa hàng hóa trong nước ra bán ở nước ngoài.
xuất phát|Bắt đầu lên đường từ một nơi; cũng chỉ điều bắt nguồn từ đâu.
xuất thân|Nguồn gốc gia đình, hoàn cảnh mà một người sinh ra, lớn lên.
xúc động|Cảm động mạnh, lòng rung động trước điều gì.
xúc tác|Chất làm phản ứng hóa học xảy ra nhanh hơn mà bản thân không đổi.
xúc tiến|Thúc đẩy cho công việc được tiến hành nhanh hơn.
xúc xích|Món làm từ thịt xay nhồi vào vỏ mỏng, thành thanh dài.
xuôi|Theo cùng chiều dòng nước, chiều gió; cũng chỉ sự suôn sẻ, trôi chảy.
xuống cân|Bị giảm cân, người gầy đi so với trước.
xuống cấp|Bị hư hỏng dần, chất lượng kém đi theo thời gian.
xuống dòng|Ngắt chữ để bắt đầu viết ở một dòng mới.
xuống dốc|Đi từ chỗ cao xuống thấp; cũng chỉ sự sa sút, kém dần đi.
xuồng máy|Thuyền nhỏ chạy bằng động cơ.
xuống nước|Đi xuống chỗ có nước; nghĩa bóng là chịu nhún nhường, dịu giọng hơn.
xuyên|Đi thủng qua hoặc đi suốt từ bên này sang bên kia.
xưa nay|Từ trước đến bây giờ, suốt thời gian qua.
xứng|Ngang tầm, phù hợp hoặc đáng được nhận điều gì.
xứng đáng|Có đủ giá trị, công sức để được nhận điều gì đó.
xứng đôi|Hai người hợp nhau về mọi mặt, trông thật đẹp đôi.
xưng hô|Cách gọi mình và gọi người khác khi nói chuyện.
xương|Phần cứng bên trong cơ thể người và động vật, giúp nâng đỡ, tạo dáng.
xương cá|Phần xương mảnh của con cá; cũng chỉ kiểu hoa văn chữ V nối tiếp.
xương ống|Xương dài hình ống ở chân con vật, hay dùng ninh nước dùng.
xương rồng|Cây có gai, thân mọng nước, chịu được khô hạn.
xương sống|Cột xương chạy dọc lưng; cũng chỉ phần chủ chốt, quan trọng nhất.
ý định|Điều đã nghĩ sẵn trong đầu và định sẽ làm.
y hệt|Giống nhau hoàn toàn, không khác một chút nào.
ý kiến|Suy nghĩ, nhận xét riêng của mỗi người về một vấn đề.
ỷ lại|Dựa dẫm vào người khác, không tự cố gắng.
ý muốn|Điều mà một người mong được làm hoặc có được.
ý nghĩ|Điều nảy ra trong đầu khi suy nghĩ.
ý nghĩa|Nội dung, giá trị mà một điều gì đó muốn nói hoặc mang lại.
y nguyên|Vẫn còn nguyên như lúc đầu, không bị thay đổi gì.
y như|Giống hệt như người hay vật được đem ra so sánh.
ý thích|Những điều riêng mà một người hay thích làm, thích có.
ý thức|Sự hiểu biết và tự giác về việc mình làm; cũng là trạng thái tỉnh táo.
ý tưởng|Suy nghĩ mới nảy ra trong đầu về cách làm một việc gì.
yên ắng|Im lặng hẳn, không nghe thấy tiếng động nào.
yên bình|Êm đềm, thanh bình, không có điều gì xáo trộn.
yên giấc|Ngủ ngon lành, say sưa, không bị ai quấy rầy.
yên lành|Bình yên, không gặp chuyện gì xấu xảy ra.
yên lặng|Không có tiếng ồn, không ai nói năng gì.
yên lòng|Cảm thấy an tâm, không còn điều gì phải lo.
yến mạch|Loại ngũ cốc hạt nhỏ, thường nấu cháo hoặc ăn sáng cùng sữa.
yên ổn|Mọi thứ ổn định, êm xuôi, không gặp rắc rối gì.
yên sau|Chỗ ngồi phía sau trên xe máy hoặc xe đạp.
yên tâm|Tin tưởng, không còn lo lắng hay bận lòng.
yên tĩnh|Vắng tiếng ồn, êm ả, tạo cảm giác thư thái.
yên vui|Bình yên, vui vẻ, không có điều gì phải lo âu.
yêu cầu|Đề nghị ai đó phải làm việc gì; cũng chỉ điều cần phải đạt được.
yêu dấu|Rất được yêu thương, quý mến và trân trọng.
yêu đời|Vui vẻ, lạc quan và luôn thấy cuộc sống tươi đẹp.
yếu đuối|Thiếu sức mạnh về thể chất hoặc tinh thần, dễ nản lòng.
yêu đương|Có tình cảm lứa đôi, đang yêu nhau.
yếu kém|Còn kém cỏi, chưa đủ năng lực để đạt yêu cầu.
yêu mến|Có tình cảm quý trọng và thân thiết dành cho ai đó.
yếu ớt|Sức lực rất kém, mỏng manh, trông thiếu sức sống.
yêu thích|Rất thích, có cảm tình đặc biệt với điều gì.
yêu thương|Có tình cảm gắn bó, luôn quan tâm và chăm lo cho ai đó.
yếu tố|Một thành phần góp phần tạo nên hoặc ảnh hưởng đến kết quả.
yếu xìu|Yếu ớt, không có chút sức lực hay khí thế nào.
yoga|Môn tập kết hợp các tư thế kéo giãn và hít thở, giúp thân thể dẻo dai.
```
