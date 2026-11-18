# Cụm mật khẩu tiếng Việt

Mini web app tạo **cụm mật khẩu** (passphrase) ngẫu nhiên từ từ vựng tiếng Việt, dùng **cùng thuật toán với trình tạo passphrase của Bitwarden**.

- Chỉ một file [`index.html`](index.html), viết bằng HTML/CSS/JavaScript thuần: không thư viện, không tài nguyên ngoài, không SVG.
- Mở trực tiếp bằng trình duyệt (chạy được offline qua `file://`) hoặc triển khai lên GitHub Pages: workflow [`pages.yml`](.github/workflows/pages.yml) tự động publish `index.html` mỗi khi push lên `main`. Lần đầu cần bật **Settings → Pages → Source: GitHub Actions**.
- Danh sách từ hiện chỉ có **100 từ để thử nghiệm**, **chưa đủ an toàn** để dùng thật (xem [Entropy](#3-entropy)).

## 1. Bitwarden tạo passphrase như thế nào

### Luồng gọi trong extension trình duyệt (`apps/browser`)

| Lớp | File (permalink) | Vai trò |
|---|---|---|
| UI popup | [`apps/browser/.../credential-generator.component.html`](https://github.com/bitwarden/clients/blob/4fcead0bd2cb7b57505986422b58d4e7e4585fdc/apps/browser/src/tools/popup/generator/credential-generator.component.html) | Nhúng `<tools-credential-generator>` từ thư viện dùng chung |
| Form tùy chọn | [`passphrase-settings.component.html`](https://github.com/bitwarden/clients/blob/4fcead0bd2cb7b57505986422b58d4e7e4585fdc/libs/tools/generator/components/src/passphrase-settings.component.html) | Số từ, dấu phân cách, viết hoa, bao gồm cả số |
| Metadata | [`eff-word-list.ts`](https://github.com/bitwarden/clients/blob/4fcead0bd2cb7b57505986422b58d4e7e4585fdc/libs/tools/generator/core/src/metadata/password/eff-word-list.ts#L50-L72) | Giá trị mặc định và giới hạn; engine là `SdkPasswordRandomizer` |
| Engine | [`sdk-password-randomizer.ts`](https://github.com/bitwarden/clients/blob/4fcead0bd2cb7b57505986422b58d4e7e4585fdc/libs/tools/generator/core/src/engine/sdk-password-randomizer.ts) | Gọi SDK (WASM): `client.generator().passphrase(...)` |
| Thuật toán | [`sdk-internal/.../passphrase.rs`](https://github.com/bitwarden/sdk-internal/blob/56c7617b23501af70221094cdee59e10b2a9d8d2/crates/bitwarden-generators/src/passphrase.rs#L91-L130) | `passphrase_with_rng()`, phần được port sang JS |

Bản TypeScript cũ [`PasswordRandomizer.randomEffLongWords`](https://github.com/bitwarden/clients/blob/4fcead0bd2cb7b57505986422b58d4e7e4585fdc/libs/tools/generator/core/src/engine/password-randomizer.ts) nay đã bị đánh dấu `@deprecated` nhưng vẫn dùng cùng thuật toán.

### Thuật toán (`passphrase_with_rng`)

1. Kiểm tra số từ nằm trong khoảng 3–20.
2. **`gen_words`**: chọn từng từ một cách độc lập, phân phối đều và **có thể lặp lại**, từ danh sách EFF Long Wordlist. Danh sách có 7.776 từ; Bitwarden bỏ 4 từ chứa `-` (`drop-down`, `felt-tip`, `t-shirt`, `yo-yo`) để tránh nhầm với dấu phân cách. Nguồn ngẫu nhiên là CSPRNG của hệ điều hành; trên trình duyệt, đó chính là `crypto.getRandomValues`.
3. **`include_number_in_words`** (nếu bật): chọn ngẫu nhiên 1 từ rồi nối thêm **1 chữ số 0–9** vào cuối từ đó.
4. **`capitalize_words`** (nếu bật): viết hoa chữ cái đầu của mỗi từ.
5. Nối các từ bằng dấu phân cách.

### Mặc định và giới hạn

Nguồn: [`eff-word-list.ts`](https://github.com/bitwarden/clients/blob/4fcead0bd2cb7b57505986422b58d4e7e4585fdc/libs/tools/generator/core/src/metadata/password/eff-word-list.ts#L50-L72) và [`passphrase-policy-constraints.ts`](https://github.com/bitwarden/clients/blob/4fcead0bd2cb7b57505986422b58d4e7e4585fdc/libs/tools/generator/core/src/policies/passphrase-policy-constraints.ts).

| Tùy chọn | Mặc định | Giới hạn |
|---|---|---|
| Số từ | 6 | 3–20, khuyến nghị ≥ 6 |
| Dấu phân cách từ | `-` | 0–1 ký tự (có thể để trống) |
| Viết hoa | tắt | chữ cái đầu mỗi từ |
| Bao gồm cả số | tắt | 1 chữ số 0–9 ở cuối 1 từ |

## 2. Ánh xạ sang `index.html`

| Bitwarden | `index.html` |
|---|---|
| `EFF_LONG_WORD_LIST` + `filter(!w.contains('-'))` | `WORDS`: đọc từ khối `#wordlist`, chuẩn hoá NFC, bỏ trùng, bỏ từ chứa `-` |
| CSPRNG của hệ điều hành | `crypto.getRandomValues` |
| Lấy số nguyên phân phối đều | `randomNumber(min, max)`, port từ hàm [`randomNumber()` TypeScript](https://github.com/bitwarden/clients/blob/browser-v2024.10.0/libs/common/src/platform/services/crypto.service.ts#L616-L649) của Bitwarden (gốc từ EFF diceware). Hàm lấy mẫu loại bỏ (rejection sampling) nên không bị lệch như khi dùng `%` |
| `gen_words` | `Array.from({ length: numWords }, () => WORDS[randomNumber(0, WORDS.length - 1)])` |
| `include_number_in_words` | `words[randomNumber(0, numWords - 1)] += randomNumber(0, 9)` |
| `capitalize_first_letter` | `w.charAt(0).toUpperCase() + w.slice(1)` |
| `join(word_separator)` | `words.join(wordSeparator)` |
| UI: ô số 3–20, `maxlength=1`, 2 checkbox | Thanh trượt 3–20 kèm nút −/+, `maxlength=1`, 2 công tắc. Đổi tùy chọn nào thì tạo passphrase mới (giống Bitwarden). Khác Bitwarden: dấu phân cách mặc định là `_` thay vì `-` |

Thuật toán không có bước nào mới. Phần thêm vào chỉ là làm sạch dữ liệu đầu vào (chuẩn hoá Unicode NFC, bỏ từ trùng) và hiển thị (tô màu chữ số/dấu phân cách, ước lượng entropy).

## 3. Entropy

Mỗi từ được chọn đều từ danh sách `N` từ nên đóng góp `log2(N)` bit. Viết hoa và dấu phân cách **không** làm tăng entropy, vì kẻ tấn công được giả định là biết thuật toán và các tùy chọn. Bật "Bao gồm cả số" cộng thêm `log2(10 × số từ)` bit (≈ 5,9 bit với 6 từ).

| Danh sách | bit/từ | 4 từ | 5 từ | 6 từ | 8 từ | 12 từ |
|---|---|---|---|---|---|---|
| 100 từ (thử nghiệm) | 6,64 | 26,6 | 33,2 | 39,9 | 53,2 | 79,7 |
| 7.776 từ (dự kiến) | 12,92 | 51,7 | 64,6 | **77,5** | 103,4 | 155,1 |

Với 100 từ, phải dùng 12 từ mới đạt khoảng 80 bit. Vì vậy app hiện cảnh báo khi danh sách có ít hơn 7.776 từ. Thanh độ mạnh chuyển xanh từ 77,5 bit, tức mức 6 từ EFF mà Bitwarden khuyến nghị.

Từ trong passphrase có thể lặp lại (chọn có hoàn lại, giống Bitwarden); công thức trên đã tính điều này. Nếu để trống dấu phân cách, ranh giới giữa các từ có thể bị nhập nhằng, ví dụ *cá + táo* và *cát + áo* đều thành `cátáo`, nên entropy thực tế thấp hơn một chút. Vì vậy nên luôn dùng dấu phân cách.

## 4. Lưu ý riêng cho tiếng Việt (khi chốt danh sách 7.776 từ)

1. **Unicode dựng sẵn và tổ hợp**: chữ có dấu có thể mã hoá dạng dựng sẵn (NFC) hoặc tổ hợp (NFD, hay "Unicode tổ hợp" trong bộ gõ). Hai dạng trông giống hệt nhau nhưng khác byte, nên mật khẩu sẽ bị báo sai. App chuẩn hoá danh sách về NFC; khi gõ tay, hãy đặt bộ gõ ở chế độ *Unicode dựng sẵn*.
2. **Kiểu đặt dấu cũ/mới**: các vần `oa`, `oe`, `uy` không có phụ âm cuối có thể đặt dấu theo hai kiểu: *hòa/hoà*, *khỏe/khoẻ*, *thủy/thuỷ*. Nên loại các từ này khỏi danh sách.
3. **Biến thể chính tả**: *lý/lí*, *kỹ/kĩ*, *mỹ/mĩ*, *sĩ/sỹ*, *giày/giầy*… Nên loại.
4. **Từ dễ viết sai theo vùng miền**: các cặp hỏi/ngã, s/x, ch/tr, d/gi/r, l/n, -c/-t, -n/-ng, và những cặp từ có thật dễ lẫn như *sương/xương*. Nên ưu tiên từ ít bị viết sai.
5. **Gõ dấu trong ô mật khẩu**: một số nền tảng tắt bộ gõ (IME) khi nhập vào ô mật khẩu, ví dụ chế độ Secure Input của macOS hay bàn phím điện thoại ở chế độ mật khẩu, nên có thể không gõ được dấu trực tiếp. Passphrase có dấu dùng tốt khi lưu trong trình quản lý mật khẩu (dán hoặc tự điền). Nếu cần gõ tay, ví dụ cho mật khẩu chính hay khi đăng nhập máy, phải thử trước trên thiết bị thật.
6. **Nếu sau này thêm chế độ "không dấu"**: danh sách phải không có từ nào trùng nhau sau khi bỏ dấu, vì *ca/cá/cà/cả/cã/cạ* đều thành `ca` và làm giảm entropy. Danh sách 100 từ thử nghiệm đã thoả điều kiện này.
7. **Từ đơn hay từ ghép**: số âm tiết tiếng Việt thông dụng chỉ khoảng vài nghìn, nên khó có đủ 7.776 từ đơn dễ nhớ và danh sách cuối nhiều khả năng cần có từ ghép. Nếu giữ dấu cách trong từ ghép (*bánh mì*), không nên dùng dấu cách làm dấu phân cách vì sẽ gây nhập nhằng; đây cũng là lý do Bitwarden bỏ các từ chứa `-`. Không đưa `-` vào từ, vì app sẽ tự loại các từ đó giống Bitwarden.
8. **Viết hoa**: `toUpperCase()` xử lý đúng chữ có dấu khi danh sách ở dạng NFC (*đá → Đá*, *ước → Ước*).

## 5. Thay danh sách từ chính thức

Thay nội dung khối `<script type="text/plain" id="wordlist">` ở cuối `index.html` bằng danh sách mới, mỗi dòng một từ và kết thúc bằng dấu `,` (UTF-8). App tách từ theo `,` và xuống dòng nên không bị lệch giữa CRLF và LF. Không cần sửa code: entropy, số từ và cảnh báo tự cập nhật theo kích thước danh sách sau khi đã bỏ trùng.

Thuật toán không đòi hỏi đúng 7.776 từ. Con số 6⁵ chỉ để có thể tung 5 viên xúc xắc như EFF; entropy luôn bằng `log2(số từ thực tế)`.

Tiêu chí gợi ý: từ phổ biến, cụ thể, dễ hình dung và dễ viết đúng; không có từ tục tĩu hay nhạy cảm; không trùng; không chứa `-`; tránh các trường hợp ở mục 2–4; nếu cần chế độ không dấu thì không trùng sau khi bỏ dấu.

## 6. Bảo mật của web app

- Số ngẫu nhiên lấy từ `crypto.getRandomValues` (CSPRNG) và dùng rejection sampling để phân phối đều.
- Content-Security-Policy `default-src 'none'`: trang không thể tải hay gửi dữ liệu ra ngoài, chỉ chạy CSS/JS nội tuyến.
- Không lưu gì (không cookie, không localStorage). Passphrase chỉ nằm trong bộ nhớ của trang.
- Sau khi sao chép, passphrase nằm trong clipboard (và lịch sử clipboard của hệ điều hành hoặc bàn phím) cho đến khi bị ghi đè.
