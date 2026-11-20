# Passphrase tiếng Việt
**Live app: https://tdat00.github.io/passphrase-tieng-viet/**

Mini web app tạo **cụm mật khẩu** (passphrase) ngẫu nhiên từ từ vựng tiếng Việt, dùng **cùng thuật toán với trình tạo passphrase của Bitwarden**.

- Chỉ một file [`index.html`](index.html), viết bằng HTML/CSS/JavaScript thuần: không thư viện, không tài nguyên ngoài, không SVG.
- Mở trực tiếp bằng trình duyệt (chạy được offline qua `file://`) hoặc triển khai lên GitHub Pages: workflow [`pages.yml`](.github/workflows/pages.yml) tự động publish `index.html` và `thong-tin.html` mỗi khi push lên `main`. Lần đầu cần bật **Settings → Pages → Source: GitHub Actions**.
- Danh sách gồm **7.776 từ** tiếng Việt thông dụng (480 từ đơn, 7.033 từ ghép 2 âm tiết, 263 từ ghép 3 âm tiết), mỗi từ có giải nghĩa ở trang [`thong-tin.html`](thong-tin.html). Phương pháp chọn từ, bộ tiêu chí và quá trình thống nhất giữa hai phân tích: xem [`WordListAnalyze.md`](WordListAnalyze.md).

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
| `EFF_LONG_WORD_LIST` + `filter(!w.contains('-'))` | `WORDS`: các từ trong khối `#wordlist`, tách theo dấu `,`. Danh sách đã được lọc sẵn (không có từ chứa `-`, không trùng, dạng NFC) nên code không lọc lại; từ ghép giữ một dấu cách giữa các âm tiết (`trà sữa`) |
| CSPRNG của hệ điều hành | `crypto.getRandomValues` |
| Lấy số nguyên phân phối đều | `randomNumber(min, max)`, port từ hàm [`randomNumber()` TypeScript](https://github.com/bitwarden/clients/blob/browser-v2024.10.0/libs/common/src/platform/services/crypto.service.ts#L616-L649) của Bitwarden (gốc từ EFF diceware). Hàm lấy mẫu loại bỏ (rejection sampling) nên không bị lệch như khi dùng `%` |
| `gen_words` | `Array.from({ length: numWords }, () => WORDS[randomNumber(0, WORDS.length - 1)])` |
| `include_number_in_words` | `words[randomNumber(0, numWords - 1)] += randomNumber(0, 9)` |
| `capitalize_first_letter` | `w.charAt(0).toUpperCase() + w.slice(1)` |
| `join(word_separator)` | `words.map(...).join(wordSeparator)`: trước khi nối, dấu cách trong từ ghép được bỏ đi (`tràsữa`), hoặc thay bằng dấu phân cách nếu bật "Phân cách từ ghép" (`trà_sữa`). Số và chữ hoa đã được thêm trên cả từ ghép ở các bước trước (`Trà_sữa7`) |
| UI: ô số 3–20, `maxlength=1`, 2 checkbox | Thanh trượt 3–20 kèm nút −/+, `maxlength=1`, 3 công tắc. Đổi tùy chọn nào thì tạo passphrase mới (giống Bitwarden). Khác Bitwarden: dấu phân cách mặc định là `_` thay vì `-`; thêm công tắc "Phân cách từ ghép" (mặc định tắt) |

Thuật toán không có bước nào mới. Phần thêm vào chỉ là cách nối các âm tiết của từ ghép và phần hiển thị (bản không dấu, tô màu chữ số/dấu phân cách, độ dài, entropy và thanh độ mạnh theo KeePassXC, xem mục 3).

## 3. Entropy

Mỗi từ được chọn đều từ danh sách `N` từ nên đóng góp `log2(N)` bit. Viết hoa và dấu phân cách **không** làm tăng entropy, vì kẻ tấn công được giả định là biết thuật toán và các tùy chọn. Bật "Bao gồm cả số" cộng thêm `log2(10 × số từ)` bit (≈ 5,9 bit với 6 từ).

| Danh sách | bit/từ | 4 từ | 5 từ | 6 từ | 8 từ | 12 từ |
|---|---|---|---|---|---|---|
| 7.776 từ | 12,92 | 51,7 | 64,6 | **77,5** | 103,4 | 155,1 |

Từ trong passphrase có thể lặp lại (chọn có hoàn lại, giống Bitwarden); công thức trên đã tính điều này. Nếu để trống dấu phân cách, ranh giới giữa các từ có thể bị nhập nhằng, ví dụ *cá + táo* và *cát + áo* đều thành `cátáo`, nên entropy thực tế thấp hơn một chút. Vì vậy nên luôn dùng dấu phân cách. Bật "Phân cách từ ghép" cũng có thể gây nhập nhằng tương tự nhưng hiếm hơn nhiều: từ ghép *A B* + từ *C* và từ *A* + từ ghép *B C* đều thành `A_B_C` nếu cả bốn từ đều có trong danh sách.

### Thanh độ mạnh

Bitwarden không có thanh đo cho passphrase do generator tạo ra; generator chỉ gợi ý *"Use 6 words or more to generate a strong passphrase"* ([`recommendation: 6`](https://github.com/bitwarden/clients/blob/4fcead0bd2cb7b57505986422b58d4e7e4585fdc/libs/tools/generator/core/src/metadata/password/eff-word-list.ts#L70), [chuỗi gợi ý](https://github.com/bitwarden/clients/blob/4fcead0bd2cb7b57505986422b58d4e7e4585fdc/apps/web/src/locales/en/messages.json#L11497-L11498)). Các thanh đo khác của Bitwarden, gồm thanh đo khi đặt mật khẩu chính ([`password-strength-v2.component.ts`](https://github.com/bitwarden/clients/blob/4fcead0bd2cb7b57505986422b58d4e7e4585fdc/libs/angular/src/tools/password-strength/password-strength-v2.component.ts#L137-L157)) và trang [bitwarden.com/password-generator](https://bitwarden.com/password-generator/), đều dùng thư viện ngoài [zxcvbn](https://github.com/dropbox/zxcvbn). zxcvbn ước lượng số lần đoán cho mật khẩu do người dùng tự đặt và cho điểm cao nhất từ 10¹⁰ lần đoán, khoảng 33 bit ([`score`](https://github.com/dropbox/zxcvbn/blob/67c4ece9efc40c9d0a1d7d995b2b22a91be500c2/README.md#L179-L189)). Khi thử với danh sách này, zxcvbn và cả cách chấm của bitwarden.com đều xếp mọi passphrase từ 3 từ trở lên vào mức cao nhất (Strong), nên không phân biệt được 3 từ với 6 từ.

Vì vậy app port thang chất lượng của [KeePassXC](https://keepassxc.org/), trình quản lý mật khẩu mã nguồn mở có generator passphrase tính entropy theo đúng công thức trên ([`PassphraseGenerator::estimateEntropy`](https://github.com/keepassxreboot/keepassxc/blob/cd42236540c1cfca332c0f051d981acfdacf7b4e/src/core/PassphraseGenerator.cpp#L41-L51)) và mặc định dùng danh sách EFF 7.776 từ ([`Config.cpp`](https://github.com/keepassxreboot/keepassxc/blob/cd42236540c1cfca332c0f051d981acfdacf7b4e/src/core/Config.cpp#L233-L235)):

- Ngưỡng lấy từ [`PasswordHealth::quality()`](https://github.com/keepassxreboot/keepassxc/blob/cd42236540c1cfca332c0f051d981acfdacf7b4e/src/core/PasswordHealth.cpp#L99-L111), cách hiển thị theo [`PasswordGeneratorWidget::updatePasswordStrength()`](https://github.com/keepassxreboot/keepassxc/blob/cd42236540c1cfca332c0f051d981acfdacf7b4e/src/gui/PasswordGeneratorWidget.cpp#L277-L322).
- Nhãn lấy từ [bản dịch tiếng Việt của KeePassXC](https://github.com/keepassxreboot/keepassxc/blob/cd42236540c1cfca332c0f051d981acfdacf7b4e/share/translations/keepassxc_vi.ts#L7385-L7404).
- Thanh tối đa 200 bit, giống [`PasswordGeneratorWidget.ui`](https://github.com/keepassxreboot/keepassxc/blob/cd42236540c1cfca332c0f051d981acfdacf7b4e/src/gui/PasswordGeneratorWidget.ui#L182-L184).

| Mức | Entropy | Với danh sách 7.776 từ | Màu |
|---|---|---|---|
| Kém | < 40 bit | 3 từ không có số | đỏ |
| Yếu | 40 đến < 75 bit | 3 từ có số, 4–5 từ | vàng |
| Tốt | 75 đến < 100 bit | 6–7 từ | xanh |
| Xuất sắc | ≥ 100 bit | từ 8 từ | xanh |

Thanh là một `div` (`role="meter"`) tự vẽ thay vì thẻ `<meter>`, vì màu của `<meter>` do trình duyệt quyết định, không dùng chung được với màu nhãn. Nhãn và thanh cùng một màu; Tốt và Xuất sắc cùng màu xanh, chỉ nhãn chữ phân biệt hai mức này (KeePassXC dùng một màu riêng cho mỗi mức).

Thang này khớp với các khuyến nghị cho passphrase: 6 từ (77,5 bit) là mức Tốt, cũng là mức tối thiểu mà Bitwarden, [EFF](https://www.eff.org/dice) (*"We recommend selecting a minimum of six words from our long wordlist, or when using any other list of this size"*) và [Diceware](https://theworld.com/~reinhold/dicewarefaq.html#howlong) (*"I now recommend six words for most users"*) đưa ra. Diceware còn ước tính 4 từ (51,6 bit) bị bẻ trong khoảng một giờ bằng một cụm 25 GPU năm 2012, còn 8 từ an toàn đến năm 2050.

Có chuẩn khắt khe hơn: [CNIL](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000046432885) (Pháp, Délibération 2022-100) yêu cầu mật khẩu tương đương ít nhất 80 bit nếu không có biện pháp bảo vệ nào khác, tức 7 từ hoặc 6 từ có số (83,5 bit) với danh sách này; nếu dịch vụ giới hạn số lần thử thì 50 bit là đủ.

## 4. Lưu ý riêng cho tiếng Việt

1. **Unicode dựng sẵn và tổ hợp**: chữ có dấu có thể mã hoá dạng dựng sẵn (NFC) hoặc tổ hợp (NFD, hay "Unicode tổ hợp" trong bộ gõ). Hai dạng trông giống hệt nhau nhưng khác byte, nên mật khẩu sẽ bị báo sai. Danh sách được lưu ở dạng NFC; khi gõ tay, hãy đặt bộ gõ ở chế độ *Unicode dựng sẵn*.
2. **Kiểu đặt dấu cũ/mới**: các vần `oa`, `oe`, `uy` không có phụ âm cuối có thể đặt dấu theo hai kiểu: *hòa/hoà*, *khỏe/khoẻ*, *thủy/thuỷ*. Nên loại các từ này khỏi danh sách.
3. **Biến thể chính tả**: *lý/lí*, *kỹ/kĩ*, *mỹ/mĩ*, *sĩ/sỹ*, *giày/giầy*… Nên loại.
4. **Từ dễ viết sai theo vùng miền**: các cặp hỏi/ngã, s/x, ch/tr, d/gi/r, l/n, -c/-t, -n/-ng, và những cặp từ có thật dễ lẫn như *sương/xương*. Nên ưu tiên từ ít bị viết sai.
5. **Gõ dấu trong ô mật khẩu**: một số nền tảng tắt bộ gõ (IME) khi nhập vào ô mật khẩu, ví dụ chế độ Secure Input của macOS hay bàn phím điện thoại ở chế độ mật khẩu, nên có thể không gõ được dấu trực tiếp. Passphrase có dấu dùng tốt khi lưu trong trình quản lý mật khẩu (dán hoặc tự điền). Nếu cần gõ tay, ví dụ cho mật khẩu chính hay khi đăng nhập máy, phải thử trước trên thiết bị thật.
6. **Bản không dấu**: app hiện cả passphrase đã bỏ dấu, nên danh sách không được có hai từ trùng nhau sau khi bỏ dấu và viết liền (*ca/cá/cà/cả/cã/cạ* đều thành `ca`), nếu không entropy thực tế sẽ thấp hơn con số app hiển thị. Khi trùng chỉ giữ một từ, ưu tiên từ cụ thể, dễ hình dung (*diều* thay vì *điều*). Danh sách hiện tại đã thoả điều kiện này.
7. **Từ ghép**: sau khi bỏ dấu và loại trùng, cả [bộ danh sách 74K từ của Hồ Ngọc Đức](https://github.com/duyet/vietnamese-wordlist) chỉ có 2.453 từ đơn (1 âm tiết), phần lớn là từ hiếm, nên danh sách cần thêm từ ghép 2–3 âm tiết (từ 3 âm tiết chỉ nhận danh từ cố định gọi tên vật, như *máy hút bụi*). Trong danh sách, từ ghép có dấu cách (*trà sữa*) để trang thông tin dễ đọc. Khi tạo passphrase, app mặc định viết liền (*tràsữa*), nên passphrase không chứa dấu cách và dùng dấu cách làm dấu phân cách cũng không bị nhập nhằng; bật "Phân cách từ ghép" thì các âm tiết được nối bằng dấu phân cách (*trà_sữa*). App coi mỗi từ ghép là một từ: chỉ viết hoa chữ cái đầu (*Tràsữa*, *Trà_sữa*) và chèn số vào cuối từ ghép (*tràsữa7*, *trà_sữa7*). Danh sách không có từ chứa `-`, giống việc Bitwarden loại các từ này khỏi danh sách EFF.
8. **Viết hoa**: `toUpperCase()` xử lý đúng chữ có dấu khi danh sách ở dạng NFC (*đá → Đá*, *ước → Ước*).

## 5. Cập nhật danh sách từ

Nguồn chuẩn của danh sách là [`analyzing-tools/wordlist.txt`](analyzing-tools/wordlist.txt) (mỗi dòng `từ|giải nghĩa`). Sửa tệp này rồi chạy `python analyzing-tools/build_wordlist.py` để sinh lại các khối danh sách bên dưới, và chạy các bộ kiểm trong [`analyzing-tools/README.md`](analyzing-tools/README.md). Thư mục đó cũng chứa nhãn, hồ sơ nguồn gốc từng giải nghĩa và manifest nguồn dữ liệu.

Thay nội dung khối `<script type="text/plain" id="wordlist">` ở cuối `index.html` bằng danh sách mới (UTF-8), mỗi dòng một từ và kết thúc bằng dấu `,`; từ ghép có một dấu cách giữa các âm tiết, ví dụ `trà sữa,`. App chỉ tách theo dấu `,` và bỏ khoảng trắng ở hai đầu mỗi từ (nên dùng CRLF hay LF đều được), không chuẩn hoá hay lọc gì thêm. Vì vậy danh sách mới phải ở sẵn dạng NFC, không trùng (kể cả sau khi bỏ dấu và viết liền) và không có từ chứa `-`. Entropy và số từ tự cập nhật theo kích thước danh sách.

Trang [`thong-tin.html`](thong-tin.html) hiện quy tắc chọn từ và bảng gồm từ, dạng bỏ dấu và giải nghĩa, chia trang theo chữ cái đầu (đã bỏ dấu). Vì CSP chặn mọi tài nguyên ngoài nên trang này có khối `<script type="text/plain" id="wordlist">` riêng, mỗi dòng `từ|giải nghĩa`; cần cập nhật cùng lúc với `index.html`. Trang không tự sắp xếp, nên các dòng phải được xếp sẵn theo thứ tự từ điển tiếng Việt: so từng âm tiết từ trái sang phải; trong một âm tiết, so chữ cái theo `a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y` rồi so thanh (ngang < huyền < hỏi < ngã < sắc < nặng). Ví dụ *anh rể* đứng trước *ánh mắt*.

Thuật toán không đòi hỏi đúng 7.776 từ. Con số 6⁵ chỉ để có thể tung 5 viên xúc xắc như EFF; entropy luôn bằng `log2(số từ thực tế)`.

Tiêu chí chọn từ: từ thông dụng, có trong từ điển tiếng Việt; không dùng tên riêng, từ thuộc các chủ đề nhạy cảm (bạo lực, tội phạm, chính trị, tôn giáo và tang lễ, bệnh tật, tình dục, cờ bạc và rượu bia, thảm họa, chửi rủa, ghê tởm), kể cả từ mà khi bỏ dấu đọc thành từ thô tục hay nhạy cảm; không trùng nhau sau khi bỏ dấu (mục 6); dài 4–12 chữ cái khi viết liền, không dùng từ 3 chữ cái; không chứa `-`; tránh các trường hợp ở mục 2–4 theo tỉ lệ viết khác đo được trên kho văn bản. Mỗi từ có một câu giải nghĩa viết mới (giấy phép MIT). Bộ tiêu chí đầy đủ và quy trình chọn 7.776 từ hiện tại được ghi trong [`WordListAnalyze.md`](WordListAnalyze.md); hai phân tích độc lập ban đầu là [`WordListAnalyze-Opus.md`](WordListAnalyze-Opus.md) và [`WordListAnalyze-Astra.md`](WordListAnalyze-Astra.md). Khi đổi tiêu chí, cập nhật cả mục "Quy tắc chọn từ" ở đầu `thong-tin.html`.

## 6. Bảo mật của web app

- Số ngẫu nhiên lấy từ `crypto.getRandomValues` (CSPRNG) và dùng rejection sampling để phân phối đều.
- Content-Security-Policy `default-src 'none'`: trang không thể tải hay gửi dữ liệu ra ngoài, chỉ chạy CSS/JS nội tuyến.
- Không lưu gì (không cookie, không localStorage). Passphrase chỉ nằm trong bộ nhớ của trang.
- Sau khi sao chép, passphrase nằm trong clipboard (và lịch sử clipboard của hệ điều hành hoặc bàn phím) cho đến khi bị ghi đè.
