# Bộ tiêu chí và quy trình thống nhất: danh sách 7.776 từ (bản 1)

Soạn: Opus (vòng 3). Hợp nhất từ [`phan-hoi-opus.md`](ho-so/discussion/phan-hoi-opus.md), [`phan-hoi-astra.md`](ho-so/discussion/phan-hoi-astra.md) và ba lượt quyết định của chủ dự án ngày 19/11/2026. **Sửa vòng 3b** theo [`soat-tieu-chi-astra.md`](ho-so/discussion/soat-tieu-chi-astra.md); phản hồi từng điểm ở [`phan-hoi-soat-opus.md`](ho-so/discussion/phan-hoi-soat-opus.md). Astra soát và ký sau.

**Mức bắt buộc của từng phần:**

- **Luật cứng (H):** vi phạm thì loại, không bù bằng điểm.
- **Hạn mức (Q):** giới hạn số lượng trong thành phẩm.
- **Luật xếp hạng (S):** dùng để chọn giữa các mục đã qua cổng.
- **Chỉ báo theo dõi (M):** báo cáo, không loại.

"Chờ" nghĩa là **chưa được nhận** ở bản 1. Mục còn phản đối hợp lệ chưa giải quyết thì **không phát hành**, mà dùng từ dự phòng. Kết luận của từng cổng (ví dụ "qua riêng H5") không có nghĩa là nhận cả từ.

## 0. Thuật ngữ, đầu vào đóng băng, định dạng file

**Thuật ngữ:**

- **Khóa:** `s.normalize("NFD").replace(/\p{M}/gu,"").replace(/đ/g,"d").replace(/Đ/g,"D")`, sau đó hạ chữ thường và xóa dấu cách. Đây là hàm của app; so trên toàn chuỗi đã viết liền.
- **Khối:** phần chữ giữa các dấu cách. **Số chữ:** số chữ cái khi viết liền (ví dụ `ươ` tính là 2).
- **PPM:** số lần trên một triệu âm tiết, đo riêng trên OpenSubtitles VI v2018 (phụ đề, 34.314.528 âm tiết) và CCAligned VI v1 (web, bỏ dòng trùng, 149.860.716 âm tiết). **PPM gộp** là trung bình cộng PPM của hai kho. **DF:** số câu chứa mục, đo trên Leipzig Mixed VI 2014 300K và Tatoeba VI (33.328 câu).

**Danh sách đóng băng** (SHA-256 của thân dữ liệu UTF-8, LF, có LF cuối):

| Danh sách | Các dòng `từ\|giải nghĩa` | Chỉ cột từ |
|---|---|---|
| Opus | `97d0b2fba487118029a83cd4aebd1c45248c3a1a3a5282cf5bb3ef506e56da0d` | `da727e6514e6f1b55362f91bbf1e35373c63ccb12d39f8928785c76ce1aa3ba8` |
| Astra | `dfd74f433bb77faf2d9033800c58dccdb54adcb5be8a1580ed90cb63c8744f8e` | `c4123bc2bdb5295ccc8cd2ba6e4fdf915ca3bc190757e28b9e2fcdd5f07a5214` |

**Tập ứng viên ban đầu** gồm 11.029 khóa: 4.340 mặt chữ chung, 183 khóa hai bên chọn khác nhau, 3.253 + 3.253 khóa riêng mỗi bên.

- Bảng P1 ([`bang-khoa-chung.tsv`](ho-so/discussion/bang-khoa-chung.tsv), SHA-256 `07195c28834f5bd3ae2c520da1eb60c9c12991c091dd3a259264b5dd9baa03f8`) cộng thêm ứng viên bổ sung: tổng 12.757 khóa, 13.356 mặt chữ.
- Khóa có nhiều mặt chữ: 503 khóa, nhiều nhất 7 mặt chữ.

### 0.1. Định dạng file

| File | Định dạng |
|---|---|
| [`tools/wordlist.txt`](wordlist.txt) (nguồn chuẩn) | UTF-8, LF, có LF cuối, không dòng tiêu đề; mỗi dòng `từ\|giải nghĩa` (đúng một `\|`), xếp theo O1 |
| Khối `#wordlist` trong `index.html` | mỗi dòng `từ,` (giữ CRLF như hiện tại) |
| Khối `#wordlist` trong `thong-tin.html` và bản lưu trong tài liệu | mỗi dòng `từ\|giải nghĩa` |
| `lo-XX.txt` (lô cho người viết), [`danh-sach-chon.txt`](ho-so/unified/danh-sach-chon.txt), [`du-phong.txt`](ho-so/unified/du-phong.txt) | UTF-8, LF, mỗi dòng một từ, không dòng tiêu đề |
| `lo-XX.tsv` (bài nộp của người viết) | phân tab, có tiêu đề `tu<TAB>giai_nghia<TAB>co`, LF, có LF cuối |
| Phiếu và bảng làm việc trong [`ho-so/discussion/`](ho-so/discussion/), [`ho-so/unified/`](ho-so/unified/) | phân tab, UTF-8, LF, có dòng tiêu đề |
| [`bang-khoa-chung.tsv`](ho-so/discussion/bang-khoa-chung.tsv) | theo lược đồ [`astra/round3/schema-bang-khoa.json`](ho-so/astra/round3/schema-bang-khoa.json): 8 cột vô hướng, sau đó các mảng JSON thẳng hàng theo vị trí ứng viên. Mỗi dòng là một khóa, không phải một ứng viên |

## 1. Đã chốt (không bàn lại)

Dòng 1–6 là quyết định lượt 1 của chủ dự án. Dòng 15–16 và phần sửa ở dòng 2–3 là quyết định lượt 2; dòng 16 được sửa lại ở lượt 3; dòng 17 là quyết định lượt 4. Cả bốn lượt cùng ngày 19/11/2026. Dòng 7–14 là đồng thuận của hai bên.

| # | Nội dung | Nguồn |
|---|---|---|
| 1 | Viết mới toàn bộ 7.776 giải nghĩa (kể cả 40 mẫu cũ). Người và lượt viết không được thấy giải nghĩa cũ (Opus, Astra) hay lời từ điển/Wiktionary. Opus và Astra chỉ soạn hướng dẫn và soát lại, trả **chẩn đoán**, không trả câu để diễn đạt lại | Chủ dự án |
| 2 | Bỏ *bướm* (có nghĩa phụ tục). Khóa `buom` **để trống**: không dùng *bướm* lẫn *buồm* | Chủ dự án (lượt 2 chốt để trống) |
| 3 | Giữ các thiên thể *mặt trời, mặt trăng, trái đất, ngân hà* và nhân vật cổ tích *công chúa, hoàng tử, hoàng hậu*, viết thường như danh từ chung | Chủ dự án (lượt 2 thêm *ngân hà*) |
| 4 | Giữ từ cơ thể, vệ sinh thường ngày: *mồ hôi, ruồi, gián*… | Chủ dự án |
| 5 | Giữ *chào cờ* | Chủ dự án |
| 6 | Đưa script tạo/kiểm tra và manifest (chỉ hash, số đếm, nguồn, giấy phép) vào `tools/` | Chủ dự án |
| 7 | Sắp xếp so từng âm tiết, không dùng ICU | Hai bên |
| 8 | Cổng đọc không dấu áp cho mọi mục, kể cả phần giao | Hai bên |
| 9 | Biến thể chính tả quyết theo ngưỡng đo được (H5) | Hai bên |
| 10 | Không bắt buộc bỏ một trong cặp vùng miền (*sách/xách*) | Hai bên |
| 11 | Giữ *ròng rọc, dép lê*: vắng ở kho nhỏ không có nghĩa là không quen | Hai bên |
| 12 | Mục còn phản đối hợp lệ thì không phát hành, dùng dự phòng | Hai bên + chủ dự án |
| 13 | Chấm chéo: phần chỉ có ở một bên do bên kia xét chính | Hai bên |
| 14 | Đích giấy phép là MIT. Không đưa vào repo văn bản kho ngữ liệu hay lời từ điển; chỉ ghi nguồn, phiên bản, hash, số đếm | Hai bên + chủ dự án |
| 15 | Khóa `chim` **để trống**: không dùng *chim* lẫn *chìm*. Đây là một trong 183 khóa tranh chấp, chốt BO. Từ dòng 2 và dòng này suy ra luật chung ở K0 (H7): khóa trùng khóa của một từ có nghĩa phụ tục phổ biến thì chặn cả khóa | Chủ dự án (lượt 2) |
| 16 | **Giữ *bánh chưng*.** Số đo 24% "bánh trưng" trước đây là do vắt từ: đếm lại đúng ranh giới thì cả 18/18 lượt là *bánh \| trưng bày*, 0 lượt viết sai tên bánh | Chủ dự án (lượt 3, thay quyết định loại ở lượt 2) |
| 17 | **Không dùng từ 3 chữ** (viết liền chỉ có 3 chữ cái), kể cả làm bậc lấp cuối hay dự phòng. Nếu thiếu, hai bên đề xuất cách nới tiêu chí khác, kèm số liệu, để chủ dự án duyệt | Chủ dự án (lượt 4) |

## 2. Luật cứng H1–H9 (áp theo thứ tự)

### H1. Hình thức của đầu mục

- Toàn dòng ở dạng NFC; đầu mục viết thường.
- Đầu mục chỉ dùng 29 chữ cái tiếng Việt (`a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y` cùng dấu thanh); không `f, j, w, z`. Dấu câu trong giải nghĩa theo D2.
- Giữa các khối đúng một dấu cách U+0020; không số, `-`, dấu câu, tab, khoảng trắng đầu/cuối hay kí tự ẩn/BOM.
- Mỗi dòng nguồn chuẩn có đúng một `|`.

### H2. Độ dài và số khối

- Viết liền 4–12 chữ; 1–3 khối. Mục 4 khối không dùng ở bản 1.
- Mục 3 khối chỉ nhận nếu là **danh từ hoặc cụm danh từ cố định**, gọi tên người, vật, loài, món ăn, nơi chốn hay thiết bị dễ xác định (ví dụ *chim cánh cụt, máy hút bụi*).
- Không nhận thành ngữ, tục ngữ, tên ngành "…học", thuật ngữ ghép hàng loạt, cụm tự do.
- Không dùng mục 3 chữ, kể cả để lấp khi thiếu hay làm dự phòng (mục 1, dòng 17).

### H3. Đầu mục có trong từ điển

- **Điều kiện:** khớp nguyên mặt chữ trong hợp các bộ Viet11K/22K/39K/74K (bản ghim `688b095`, GPLv2), **hoặc** là mục tiếng Việt có nghĩa từ vựng hiện hành trong Wiktionary vi/en (dump đã ghi trong báo cáo Astra).
- Ghi lại loại chứng cứ: khớp nguyên; chỉ khác kiểu đặt dấu hay gạch nối; chỉ là mục chuyển hướng.
- **Không nhận:**
  - tên người, địa danh, nhãn hiệu, dạng viết hoa của tên riêng;
  - chuỗi số sản sinh (*bảy mươi*);
  - khung câu, hư từ ghép tạm (*có một, ba bốn, ơi là, kể trên, sẽ hay*);
  - tổ hợp tự do (*đôi nam nữ, giăng kín*).

  Việc xác định tổ hợp tự do làm trong lúc chấm chéo (mã `X`).
- Nếu mục chỉ có trong một wordlist (không có nghĩa từ điển), hai bên phải ký xác nhận nghĩa thông dụng.

### H4. Mỗi khóa một vé

Không trùng mặt chữ, không trùng khóa (kể cả sau khi viết hoa chữ đầu). Hai nghĩa của cùng một cách viết vẫn chỉ là một vé. Kiểm lại sau **mỗi** lần thay từ, kể cả các mục mẫu.

### H5. Chính tả ổn định

**Cách đo** (đếm lại ở vòng 3b; script trong [`ho-so/opus/h5/`](ho-so/opus/h5/), bảng 84 cặp ở [`ho-chinh-ta-ban-dau.tsv`](ho-so/discussion/ho-chinh-ta-ban-dau.tsv)):

- Đo **riêng** từng kho, bằng **số nguyên**. Ngưỡng ≥ 20 lượt, ≥ 95%, ≥ 10%, ≥ 5% so trực tiếp bằng số nguyên, không dùng phần trăm đã làm tròn. "Đủ dữ liệu" nghĩa là cặp có ≥ 20 lượt ở kho đang xét.
- **Ranh giới:**
  - chỉ ghép các âm tiết liền nhau trong một đoạn không có dấu câu;
  - lượt có âm tiết trái + âm tiết đầu, hoặc âm tiết cuối + âm tiết phải, tạo thành một từ hai âm tiết trong HND thì gắn cờ "nghi vắt từ" (ví dụ *bánh \| trưng bày*, *khả năng \| xuất hiện*);
  - số chính không tính lượt bị gắn cờ, trừ khi đọc ngữ cảnh thấy lượt đó cùng nghĩa;
  - bộ lọc có báo nhầm (*dao động từ X đến Y* bị gắn cờ vì *động từ* có trong từ điển), nên **cặp nào mà kết luận phụ thuộc bộ lọc thì bắt buộc đọc mọi lượt bị gắn cờ** của dạng thiểu số.
- **Dòng trùng:** phụ đề đếm mọi dòng (giữ chính sách cũ); web đếm dòng khác nhau.
  - Độ nhạy: đếm lại phụ đề chỉ theo dòng khác nhau. Nếu kết luận đổi thì ghi `CHO_SAT_NGUONG` (chờ, không nhận ở bản 1 nếu hai bên chưa ký sau khi đọc thêm).
- **Loại c hay d phải có căn cứ:**
  - HND, Wiktionary hoặc nguồn tương đương ghi nhận dạng kia là cách viết chuẩn thì là loại c;
  - nguồn ghi là lỗi viết thì là loại d;
  - chưa xác định được thì `CHO_LOAI`.

| Loại | Luật | Kết quả theo số đếm mới (tỉ lệ % của dạng kia: phụ đề / web) |
|---|---|---|
| a. Vần mở `oa/oe/uy` có thanh (hai vị trí đặt dấu) | Loại. Xét âm đầu (không quét mù mọi `uy`); tiếng thanh ngang không bị cấm | *hòa/hoà, khỏe/khoẻ, thủy/thuỷ* |
| b. `i/y` sau `h, k, l, m, s, t, qu` | Xử như loại c. Thiếu dữ liệu thì loại. **Không** áp cho `d, n, v` | *lý do* 17,8/2,1 → loại; *mì/mỳ* 14,4/5,4 → loại cả họ khi là tiếng nguyên (*bánh mì*…); *tí hon* 3,5/2,3 → qua |
| c. **Cạnh tranh**: hai dạng đều được ghi nhận là cách viết chuẩn của cùng nghĩa | Chỉ nhận dạng chiếm ≥ 95% **ở cả hai kho** khi đủ dữ liệu; còn lại loại ở bản 1. Không bao giờ nhận cả hai | *cảm ơn/cám ơn* 42,7/8,9, *xung quanh/chung quanh* 6,2/1,7, *khuyến mãi/mại* 22,9/29,4, *phản ánh/ảnh* 12,9/1,7, *từ điển/tự điển* 6,1/2,0, *đậu phộng/phụng* 6,1/0,5, *hấp thụ/thu* 16,7/15,5 → loại; *giòn tan/dòn tan*: phụ đề chỉ 10 lượt → loại; *đường ray/rầy* 0,8/0,1, *thầy/thày* 1,1/1,0 → qua; *yên trí/yên chí*: chưa xác định loại → chờ |
| d. **Chuẩn và lỗi viết phổ biến** | Loại nếu lỗi ≥ 10% ở **một** kho đủ dữ liệu; 5% ≤ tỉ lệ < 10% → qua nhưng trừ điểm (S3); < 5% → qua. Không kho nào đủ dữ liệu → qua, chỉ khi hai bên cùng ký "không có chứng cứ lỗi" | Loại: *chín chắn* 11,5, *cầu vồng* 16,4, *xác suất* 11,1 (sau khi đọc), *sơ suất* 19,8, *tham quan* 12,4 (phụ đề). Chờ, sát ngưỡng: *dao động* 10,4 (9,6 nếu bỏ dòng trùng), *súc tích*. Qua: *năng suất* 2,2/0,5, *bánh chưng* 0/0, *sử dụng* 1,1/0,0, *sản xuất* 0,6/0,0, *tập trung* 1,2/0,1, *đặc biệt* 0,7/0,2, *câu chuyện* 2,7/0,5, *cư xử* 0,9/0,0. Thiếu dữ liệu, cần hai chữ ký: *dông dài* |
| e. Cặp mà phép đếm bị lẫn sang nghĩa khác | Không dùng tỉ lệ thô. Đọc mẫu ngữ cảnh; chưa phân định được thì **chờ** | *để dành, lặp lại, thìa là* → chờ |
| f. Từ mượn có cách ghi Việt hóa khác chữ cái | Xử như loại c, mỗi cặp tối đa một vé. Cộng các dạng chỉ khác dấu phân cách (cách, gạch nối, viết liền) mà không đếm một lượt hai lần | *taxi* (so với *tắc xi* + *tắc-xi* + *tắcxi*) 3,2/0,5 → qua; *radio* 1,7/0,1 → qua; *micrô/micro*, *mô tơ/motor* → loại cả hai |
| g. Biến thể chỉ khác gạch nối hay khoảng trắng | Không tạo vé riêng (danh sách không có `-`); dạng được chọn phải có chứng cứ không gạch | *sơ mi, đô la, bít tết* → qua H5g; *ô tô* qua H5g nhưng trượt H2 (viết liền 3 chữ) |
| h. Hỏi/ngã đứng riêng | Không cấm (hai dạng đã trùng khóa). Chỉ xét như loại c/d khi có lỗi viết đo được | *nghỉ ngơi/nghĩ ngơi* 2,6/0,8 → qua; *đậu hũ/hủ* 14,3/23,5 → loại |

**Lý do chọn ngưỡng:**

- **Loại c theo đề xuất của Astra** (≥ 95% ở mỗi kho), vì hai dạng cùng chuẩn thì người dùng thật sự có thể gõ dạng kia.
- **Loại d dùng ngưỡng 10% tính riêng từng kho.** Tỉ lệ đo trên kho văn bản có thể lệch theo cả hai chiều so với lỗi gõ thật của người dùng. Vì vậy 10% là mức thận trọng, nhưng không loại các từ chỉ có lỗi lẻ tẻ.
- **Danh sách cặp do người duyệt đăng ký** và xác nhận là cùng một từ. Bộ sinh biến thể tự động chỉ đề xuất, vì đa số tỉ lệ cao của nó là cụm khác tình cờ đứng liền (*khôn lớn/không lớn*). Các tỉ lệ này không chứng minh tỉ lệ gõ sai của người dùng thật.

### H6. Nghĩa không thuộc nhóm đỏ

Xét **nghĩa chính và mọi nghĩa còn dùng phổ biến của đúng nguyên mục**. Không làm sạch nghĩa bằng cách chọn nghĩa phụ lành. Không suy từ một âm tiết hay chuỗi con (*chính xác, đánh răng, kiện toàn, ung dung* không vi phạm). Nghĩa đa dạng thì đọc ngữ cảnh hoặc dựa vào chứng cứ từ điển; không dùng PPM của cả chuỗi thay cho tần suất của nghĩa đỏ.

| Nhóm đỏ | Loại (ví dụ đã nêu trong thảo luận) | Không vì nhóm này mà loại |
|---|---|---|
| 1. Bạo lực, vũ khí, quân sự | *súng, đầu đạn, mũi tên, hậu bị, chỉ huy* | *dao cạo, rùng mình, móng vuốt, giải cứu* |
| 2. Tội phạm, tố tụng, công an, hình phạt | *chung thân, nhân chứng, lục soát, kiện cáo, phạm luật, tẩu tán, vô can* | |
| 3. Chính trị, bầu cử, quyền lực nhà nước, ý thức hệ | *đắc cử, trúng cử, tái cử, đầu phiếu, hòm phiếu, cuộc bầu cử, ứng cử viên, nội chính, nhà tư bản, chư hầu, quyền lực, lên án, khẩu hiệu, vua chúa, triều đại* | *công chúa, hoàng tử, hoàng hậu* (đã chốt), *chào cờ* (đã chốt) |
| 4. Tôn giáo nghi lễ, thần linh, mê tín, tang lễ, cái chết và uyển ngữ | *nữ thần, tràng hạt, tiếp dẫn, tinh tấn, vòng hoa, ngày giỗ, ra đi, nằm xuống, nhắm mắt, sống lại* | *lễ hội, phép thuật* (chất liệu truyện), *phật ý* |
| 5. Bệnh, triệu chứng, thương tích, y khoa chuyên biệt, chất thải | *cầu khuẩn, phúc mạc, siêu âm tim, trồng răng, ngứa ngáy, nằm bẹp, cuồng loạn, điên rồ, điên đầu* | *mồ hôi, ruồi, gián* (đã chốt), *hắt hơi, ngực, nách, đánh răng, kính cận* |
| 6. Tình dục, bộ phận riêng tư theo nghĩa người lớn | *khoái cảm, léng phéng, mơn trớn, phối giống, có chửa, sống thử, ngón tay giữa*; từ một khối có nghĩa phụ tục phổ biến (*bướm, chim*: mục 1, dòng 2 và 15); mục ghép có nghĩa bóng phổ biến về mại dâm, trăng hoa (*bướm đêm, ong bướm*: mục 10.9) | *vú sữa* (tên quả), *hôn nhân*, *bươm bướm, chim sẻ* (xét như toàn mục) |
| 7. Cờ bạc, rượu bia, thuốc lá, ma túy | *vé số, trúng số, lá bài, bài tây, lai rai, ăn chơi, chơi bời, say sưa* | *bàn cờ, cờ vua* |
| 8. Thảm họa | *hạn hán, lụt lội, mưa lũ, ngập úng, tan hoang* | *mưa rào, gió mùa* |
| 9. Chửi rủa, miệt thị, chê bai người, thao túng, cảm xúc tiêu cực cực mạnh | *xấu xí, la mắng, tham lam, thô lỗ, giả dối, nói xấu, đáng khinh, vô dụng, ăn bám, giật dây, căm thù* | *buồn, khóc, giận dỗi, cô đơn, mệt mỏi* |
| 10. Ghê tởm rõ | *xú uế, hôi hám, nhà ổ chuột* | *chuột cống, bọ chét* (tên con vật; chỉ hạ hạng) |

Danh tính (giới, xu hướng tính dục, dân tộc) không bị coi là từ tục. Vì là đề tài nhạy cảm nên không chọn làm mục; nhưng cũng không phải lý do loại một từ khác chỉ vì cách đọc không dấu của nó trùng với một từ chỉ danh tính. Bảng ví dụ trên không thay cho phiếu chấm P4.

### H7. Cổng đọc không dấu (áp cho mọi mục, kể cả phần giao)

So **cả khóa** với khóa của mọi mục từ điển khác (Viet74K, Wiktionary), không bẻ âm tiết, không xét chuỗi con.

- **Còi báo** (bắt buộc người đọc xét): cách đọc khác thuộc nhóm đỏ H6, hoặc thuộc danh sách tục, **và** có PPM gộp ≥ 0,3 hoặc ≥ PPM gộp của mục đang xét. Riêng các cách đọc về tự hại, bạo lực hay tình dục rõ thì xét cả khi dưới mốc này.
- **K0, đỏ:** khóa trùng khóa của một từ hoặc cụm có thật mà nghĩa là **tục, tình dục người lớn hoặc chỉ chất thải** (trùng cả khóa, không chỉ chứa một âm tiết như vậy), bất kể tần suất. Áp cả cho mục một khối (*bưởi* ↔ *buồi*, *phích* ↔ *phịch*).
  - K0 cũng áp khi khóa trùng khóa của một từ có **nghĩa phụ** tục hoặc tình dục còn dùng phổ biến. Khi đó chặn cả khóa, không dùng từ lành nào cùng khóa (mục 1, dòng 2 và 15: `buom`, `chim`).
  - Danh sách khóa K0 phải dựa trên **nguồn chứng thực toàn mục** (HND, Wiktionary hoặc từ điển khác). Danh sách gồm cả các mục chất thải hay tình dục không mang nhãn `vulgar` (ví dụ `phan` ↔ *phân*).
  - Mỗi khóa K0 ghi nguồn, loại nghĩa và người duyệt; Astra lập ở P1, hai bên duyệt, mục còn tranh cãi gửi chủ dự án.
  - Không dùng chuỗi con (*cu, máu, đái*) làm bộ lọc; không gán nhãn tục cho danh tính.
- **K1, đỏ:** người đọc xác nhận cách đọc khác là cách đọc tự nhiên, thông dụng, thuộc nhóm đỏ (ví dụ *từ từ* ↔ *tự tử*, *lót dạ* ↔ *lột da*). Loại toàn khóa, không đổi sang từ lành khác cùng khóa để né.
- **K2, vàng:** cách đọc khác hiếm, phải tách ép, chỉ khớp một âm tiết, hoặc nghĩa đỏ của nó không chắc. **Không vào bản 1** trừ khi **cả hai bên ký "không tự động chặn"** kèm lý do. Mục đã được ký vẫn phải qua H6, H9 như mọi mục.
- **Không tự động:** hai bên đã đồng ý rằng cách đọc khác không thuộc nhóm đỏ. Mục được đi tiếp.
- Bảng phân xử ở mục 9.1. Mọi mục mới phải qua cổng này sau khi ghép.

### H8. Chứng liệu tối thiểu

- Mục phải có H3 **và** ít nhất một lần dùng **đúng nghĩa** trong một trong bốn kho.
- **Chứng cứ mạnh:** ≥ 0,1 PPM ở phụ đề **hoặc** ở web (xét từng kho, không lấy trung bình hai kho), hoặc ≥ 2 câu Leipzig, hoặc ≥ 1 câu Tatoeba. **Yếu hơn mức này:** phải đọc ngữ cảnh để xác nhận đúng nghĩa.
- **Không có lần dùng nào ở cả bốn kho:** cần hai người duyệt độc lập (khác vùng nếu có thể) giải thích được nghĩa và nêu căn cứ đời sống, rồi ghi vào **nhật ký ngoại lệ**.
  - Ví dụ cần hai chữ ký: *ăn nhịp* (0/0/0/0).
  - *dép lê* không phải ca này: có 0,175 PPM ở phụ đề và 0,187 PPM ở web, chỉ vắng ở hai kho câu.
- Kho chưa đo **không** tính là số 0: phải đo bù.

### H9. Không còn phản đối hợp lệ

**Phản đối hợp lệ** phải có đủ:

- mã cổng (H1–H8, K0/K1/K2, nhãn R2/X);
- nghĩa hoặc khóa đối chứng cụ thể, hay số đo, hay ngữ cảnh;
- người phản đối.

**Cách xử lý:**

- Bên kia được phản biện **một lần**.
- Nếu vẫn còn phản đối: **không phát hành**; mục vào danh sách gửi chủ dự án (chỉ khi đó là ca chính sách) hoặc nhường chỗ cho dự phòng.
- Cảm giác chung chung không phải phản đối hợp lệ. Bất đồng nhãn OK/R1 không phải phản đối; xử theo luật gộp nhãn ở P4.
- Mục đã chốt ở mục 1 không bị phản đối lại vì chính lý do đã chốt.

## 3. Hạn mức bản 1 (Q)

| # | Hạn mức | Ngưỡng |
|---|---|---|
| Q1 | R2 (hiếm, cổ, hẹp) | 0 |
| Q2 | R1 (dùng được nhưng thiên văn viết, chuyên môn): chỉ lấy khi ứng viên OK đã hết | ≤ 388 (5%) |
| Q3 | Hư từ, khung câu, đại từ ghép (lớp F, tính gộp không trùng); không lấy các dãy sinh theo mẫu (*chúng/bọn* + đại từ) | ≤ 77 (1%) |
| Q4 | Mục vàng K2 chưa được hai bên ký | 0 |

**Chỉ báo theo dõi (M):**

| # | Chỉ báo | Mục tiêu |
|---|---|---|
| M1 | Tỉ lệ C+H trên mẫu thẩm định chung 300 mục | ≥ 60% |
| M2 | Mục 3 khối | ≤ 4% |
| M3 | Độ dài trung bình | ≤ 7,0 chữ |
| M4 | Nhật ký ngoại lệ H8 | ≤ 1% |
| M5 | Số mục nhiều nhất có cùng âm tiết đầu | báo cáo |

Chỉ báo chỉ để báo cáo. Trọng số S3 đóng băng sau P3; ở P6 **không** tự chỉnh lại vì chỉ báo lệch. Muốn đổi trọng số phải mở phiên bản mới có chữ ký hai bên. **Không** lấy từ hiếm để đạt mục tiêu.

## 4. Xếp hạng (S): chọn giữa các mục đã qua cổng

### S1. Chọn trong một khóa (mọi khóa còn ≥ 2 mặt chữ)

- Ưu tiên mục cụ thể, dễ hình dung (C > H > K > F), rồi đến mục thông dụng hơn, rồi mục dễ gõ lại đúng hơn.
- Nếu mục được ưu tiên có PPM gộp thấp hơn **quá 10 lần** mục kia, cần **cả hai bên** ký giải trình mới được chọn; nếu không, chọn mục thông dụng hơn.
- Được phép bỏ cả khóa.
- Ví dụ đã đồng thuận ở vòng 2: *thầy, công tắc, cờ lê, riềng, thềm, trọng lực, chuối, ngựa, đồ ăn, nhà ở, bản tin, bán hàng, văn phòng, ve sầu*. Không lấy khóa `ngaygio`, vì *ngày giỗ* cùng khóa với *ngày giờ* và đọc ra tang lễ.

### S2. Điểm thông dụng F (0–100)

- **Tập tính:** mọi mục đã qua cổng, tính riêng trong từng nhóm số khối (1, 2, 3).
- **Hạng theo từng kho** (phụ đề, web theo số lượt; Leipzig, Tatoeba theo số câu):
  - mục có số đếm 0 thật nhận `p = 0`;
  - các mục có số đếm dương xếp tăng dần, nhận `p = 100 × hạng / n`, trong đó `n` là số mục dương, còn `hạng` là hạng trung bình của nhóm giá trị bằng nhau (các hạng đánh từ 1 đến `n`);
  - một mục dương duy nhất nhận 100.
- **Công thức:** `F = (p_phụđề + p_web + p_Leipzig + p_Tatoeba) / 4`.
- Kho chưa đo thì phải đo bù; không tính F khi còn thiếu kho.
- F chỉ dùng để xếp hạng, **không** dùng làm xác suất khi sinh passphrase: mọi vé đều được bốc đều.
- Bộ kiểm phải có ca thử cho: giá trị bằng nhau, nhóm chỉ có một mục dương, mục 0 thật.

### S3. Điểm tổng

Bậc độ quen xét trước: mọi mục **OK** đứng trước mọi mục **R1**. Trong cùng bậc:

`Điểm = F + G − T`, với `T ≥ 0`.

| Thành phần | Cách tính |
|---|---|
| G (lớp gợi hình) | C (người, vật, loài, món ăn, nơi chốn, cảnh vật) +15; H (hành động, tính chất quan sát được) +5; K (trừu tượng, thời gian, quan hệ) 0; F (hư từ, đại từ, khung câu) −20 |
| T (khoản trừ, đều dương) | +1 cho mỗi loại đặc điểm dễ viết sai theo vùng có trong mục (`s/x, ch/tr, d/gi/r, l/n, -c/-t, -n/-ng`), tối đa +4; +5 nếu lỗi viết 5% ≤ p < 10% (H5d), tính một lần cho cả mục; +5 nếu dài trên 10 chữ; +3 nếu 3 khối; +5 cho mục thứ hai của cặp đảo thứ tự (*an bình/bình an*) khi cả hai cùng có mặt |

**Mục thứ hai của cặp đảo** là mục có điểm cơ sở `F + G` thấp hơn; nếu bằng nhau thì là mục đứng sau theo O1.

Trọng số trên được **hiệu chỉnh một lần** sau P3, rồi đóng băng trước P6.

### S4. Thứ tự tất định

Sắp mọi ứng viên theo bộ khóa sau:

1. bậc độ quen (OK trước R1);
2. Điểm giảm dần, làm tròn 2 chữ số thập phân;
3. số chữ tăng dần;
4. thứ tự O1.

Không dùng phép so "chênh dưới N điểm" (không bắc cầu). Cặp vùng miền (*sách/xách*) không có luật riêng ngoài khoản T. Đa dạng chủ đề chỉ là chỉ báo M5.

### S5. Không chia suất 50:50 theo nguồn

Không chia suất theo nguồn A hay O; không cộng điểm cho tác giả của mục.

## 5. Giải nghĩa (D)

1. **D1. Quy trình sạch** (đã chốt):
   - Mỗi lượt viết hay viết lại là một agent mới, không kế thừa hội thoại, làm trong thư mục riêng.
   - Thư mục chỉ chứa lô từ, [`huong-dan-giai-nghia.md`](huong-dan-giai-nghia.md) (bỏ mục 12) và [`kiem-tra-giai-nghia.py`](kiem-tra-giai-nghia.py). Chỉ được đọc ba file đó và ghi file nộp; không duyệt repo, mạng hay thư mục khác.
   - Người viết không thấy giải nghĩa cũ, từ điển, Wiktionary, kho câu, file trong repo hay trong hồ sơ làm việc, kể cả câu của lượt trước.
2. **D2. Hình thức:**
   - đúng một câu, khoảng 5–15 tiếng, ≤ 110 kí tự Unicode sau NFC;
   - chữ hoa đầu, một dấu chấm cuối;
   - chỉ chữ cái tiếng Việt cùng `, ; : ( ) - /`;
   - không chữ số (con số thuộc bản chất của nghĩa thì viết bằng chữ);
   - đặt dấu kiểu cũ.
3. **D3. Nội dung:**
   - Nêu **một nghĩa phổ biến nhất**. Chỉ thêm nghĩa thứ hai khi nghĩa đó cũng rất phổ biến, khác hẳn nghĩa đầu và không thuộc nhóm đỏ. Hai vế nối bằng đúng một `;` với liên từ tự nhiên, kèm cờ `HAI_NGHIA`.
   - Đúng từ loại; danh từ có ít nhất một nét phân biệt.
   - Nét thường gặp ghi *thường*, không biến thành điều kiện bắt buộc.
   - Không vòng vo, không câu ví dụ, không mốc thời gian hay số liệu dễ đổi.
   - Không khẳng định chủ quan, tuyệt đối hay sai kiến thức.
   - Không nhắc nghĩa tục.
4. **D4. Không làm sạch nghĩa.**
   - Nếu nghĩa phổ biến thuộc nhóm đỏ, viết đúng nghĩa và gắn cờ `NHAY_CAM`. Nếu không thể viết trung tính, được để trống ở **bản nháp**; không bao giờ nhập vào thành phẩm.
   - Nếu biết có nghĩa phụ tục phổ biến, gắn cờ `TUC_PHU`.
   - Mục có cờ quay lại cổng H6/H7.
5. **D5. Không trùng.** Hai mục khác nhau không có giải nghĩa giống hệt nhau, xét trên **toàn danh sách** (cổng gộp `--phat-hanh`). Với từ đồng nghĩa, viết riêng từng câu theo đối tượng hoặc ngữ cảnh, không bịa khác biệt.
6. **D6. Kiểm nguồn gốc** (do người soát chạy sau khi viết; không gửi cho người viết):
   - **Tập tham chiếu**, mỗi tập ghi hash vào log:
     - giải nghĩa cũ của Opus và của Astra;
     - các nghĩa tiếng Việt trong dump Wiktionary vi (snapshot ghi trong manifest);
     - các câu trong [`huong-dan-giai-nghia.md`](huong-dan-giai-nghia.md).
   - **Chuẩn hóa:** NFC, hạ chữ thường, tách token theo chữ cái (giữ dấu tiếng Việt), bỏ dấu câu.
   - **Ba phép kiểm, vi phạm phép nào cũng trả lại:**
     1. trùng nguyên câu với bất kỳ mục tham chiếu nào, ở mọi độ dài;
     2. có dải ≥ 6 token liên tiếp trùng với bất kỳ mục tham chiếu nào;
     3. với câu ≥ 5 token: `difflib.SequenceMatcher` trên token, `autojunk=False`, tỉ số ≥ 0,78 so với tham chiếu của cùng đầu mục hoặc cùng họ chính tả.
   - **Xử lý:** vi phạm thì cho viết lại, không sửa tay. Log ghi phiên bản script, hash từng tập tham chiếu và kết quả từng mục. Thiếu tập tham chiếu thì kết quả là `CHUA_KIEM`, không phải `PASS`.
   - **Phạm vi:** D6 là kiểm kỹ thuật, không phải thẩm định pháp lý. Lời dịch từ nghĩa tiếng Anh không đo được bằng token, nên người soát quyền kiểm tay thêm một mẫu.
7. **D7. Soát nội dung:**
   - Người soát được tra từ điển để kiểm **sự kiện, từ loại, phạm vi nghĩa**.
   - Phiếu soát chỉ ghi mã lỗi và mô tả vấn đề bằng lời của người soát. **Không** viết câu thay thế, không trích câu nguồn hay chuỗi bị trùng.
   - Lượt viết lại chỉ nhận đầu mục và chẩn đoán ngắn (mục 12 của hướng dẫn).
   - Tối đa hai lượt viết lại; còn lỗi thì thay từ bằng dự phòng. Đầu mục chủ dự án buộc giữ thì không xóa: giao một lượt sạch mới hoặc trình chủ dự án.
8. **D8. Lưu nguồn gốc** trong [`nguon-goc-giai-nghia.tsv`](nguon-goc-giai-nghia.tsv), kể cả khi mục bị thay bằng dự phòng:
   - mã lượt viết và mã các lượt viết lại;
   - người soát nội dung, người soát quyền;
   - kết quả D6 (kèm hash tham chiếu);
   - người và ngày đóng từng cờ.

## 6. Thứ tự (O)

1. **O1.** So từng âm tiết từ trái sang phải. Trong một âm tiết:
   - trước hết so dãy chữ chưa mang thanh theo `a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y`;
   - sau đó so thanh: ngang < huyền < hỏi < ngã < sắc < nặng;
   - rồi mới sang âm tiết kế tiếp; mục ngắn hơn (là tiền tố) đứng trước.

   Không gộp `ă/â, ô/ơ, u/ư, d/đ` khi xếp. Ví dụ *anh rể* đứng trước *ánh mắt*.
2. **O2.** `thong-tin.html` không tự sắp xếp: thứ tự lấy nguyên từ dữ liệu đã xếp theo O1. Trang chỉ nhóm (`Map.groupBy`) theo chữ cái đầu đã bỏ dấu, A→Y, nên các nhóm phải liền mạch. ICU chỉ dùng để báo cáo tương thích. README §5 và mục "Quy tắc chọn từ" phải ghi quy ước này.

## 7. Kiểm tra tự động bắt buộc (C), chạy trên đầu ra thật

| # | Kiểm tra |
|---|---|
| C1 | UTF-8 không BOM, NFC toàn dòng; đúng 7.776 dòng; định dạng từng file đúng mục 0.1 |
| C2 | H1, H2 trên đầu mục: chữ cái, số chữ, số khối, khoảng trắng, không kí tự ẩn hay `-` |
| C3 | H4: duy nhất về mặt chữ và khóa theo regex của app, cả sau khi viết hoa chữ đầu |
| C4 | O1 (bộ so tham chiếu riêng); các nhóm chữ cái liền mạch A→Y |
| C5 | Không còn khóa K0/K1 (gồm K0 mở rộng), không còn mục vàng chưa ký, không còn họ chính tả bị cấm hay đang chờ |
| C6 | Hạn mức Q1–Q4 theo bảng nhãn; báo M1–M5 |
| C7 | D2, D5 trên toàn danh sách bằng `kiem-tra-giai-nghia.py --phat-hanh` (không còn cờ mở, không giải nghĩa trống); D6 có log và hash tham chiếu |
| C8 | Đồng bộ: **cột từ** của nguồn chuẩn khớp khối `index.html`; **đủ cặp** `từ\|giải nghĩa` của nguồn chuẩn khớp khối `thong-tin.html` và bản lưu trong tài liệu (từng dòng, cùng thứ tự) |
| C9 | Nhập nhằng khi dùng hai lượt, xét mọi vị trí cắt; báo cả số chuỗi lẫn số lượt chọn có thứ tự |
| C10 | Thử trên trình duyệt: app báo 7.776 từ, 6 từ ≈ 77,5 bit; trang thông tin đủ 7.776 dòng; viết hoa và chèn số đúng cho mục nhiều khối |
| C11 | Hai bộ kiểm độc lập cùng đạt: `check_wordlist.py --order syllable` (Opus) và bộ kiểm JS (Astra), tham số hóa cho 1–3 khối, 4–12 chữ |
| C12 | Công bố SHA-256 thân dữ liệu (UTF-8, LF, có LF cuối); manifest nguồn, phiên bản, giấy phép; nhật ký ngoại lệ; phiên bản script và hash tập luật |
| C13 | Cửa sức chứa P6 đạt trên chính danh sách xuất ra (một dòng mỗi khóa), kèm danh sách dự phòng theo từng ngăn hạn mức |

## 8. Quy trình P1–P8

### 8.1. Bảng công việc

Mọi file nằm trong [`ho-so/discussion/`](ho-so/discussion/) (gọi tắt D) hoặc [`ho-so/unified/`](ho-so/unified/) (gọi tắt U), định dạng theo mục 0.1. Tệp nào chỉ là đầu ra dự kiến mà không được lập thì ghi tên dạng mã, không có link. "Xong khi" là điều kiện để sang bước sau.

**P1. Bảng khóa chung.**

- *Việc:* hợp hai danh sách cùng ứng viên bổ sung; đo bốn kho; gắn cờ tự động.
- *Ai làm:* Astra lập bảng và lược đồ. Opus nộp số đếm OPUS đếm lại (theo ranh giới của H5), bảng họ chính tả, danh sách còi báo không dấu. Astra nộp DF Leipzig/Tatoeba, chứng cứ Wiktionary, danh sách khóa K0 mở rộng có nguồn. **Opus soát.**
- *Đầu vào:* hai danh sách đóng băng; [`ho-chinh-ta-ban-dau.tsv`](ho-so/discussion/ho-chinh-ta-ban-dau.tsv) (84 cặp); [`opus-counts.tsv`](ho-so/unified/opus-counts.tsv); [`canh-bao-khong-dau.tsv`](ho-so/unified/canh-bao-khong-dau.tsv).
- *Đầu ra:* [`bang-khoa-chung.tsv`](ho-so/discussion/bang-khoa-chung.tsv) theo [`schema-bang-khoa.json`](ho-so/astra/round3/schema-bang-khoa.json).
  - Cột hiện có: nguồn `A`, `O`, `A+O`, `BS`; số lượt và PPM của `opensub` và `ccaligned`; `leipzig_so_cau`, `tatoeba_so_cau`.
  - Bảng **chưa có** điểm F cuối cùng, vì F tính ở P6.
  - Mọi bộ đọc phải dùng bộ chuyển đổi đã kiểm theo phiên bản lược đồ; không giả định mỗi dòng là một ứng viên.
- *Xong khi:* đủ mọi khóa; không có kho nào bỏ trống mà chưa đo bù.

**P2. Cổng tự động.**

- *Việc:* chạy H1, H2, H4, H5a–h theo bảng họ đã đăng ký (c, d, f theo ngưỡng; e chờ; g), K0 (gồm K0 mở rộng), H8 (phần đo được), và mọi quyết định của chủ dự án.
- *Ai làm:* cả hai, mỗi bên một bộ kiểm. Hai bộ kiểm dùng cùng một tập luật đã băm (ghi hash) trước khi so kết quả.
- *Đầu vào:* [`bang-khoa-chung.tsv`](ho-so/discussion/bang-khoa-chung.tsv).
- *Đầu ra:* [`cong-opus.tsv`](ho-so/unified/cong-opus-v4.tsv), [`cong-astra.tsv`](ho-so/unified/cong-astra-v4.tsv) với các cột `khoa`, `ung_vien`, `cong`, `ket_qua` (PASS/FAIL/CANH_BAO/CHO), `ly_do`, `bang_chung`.
- *Xong khi:* hai kết quả khớp, hoặc mọi chỗ lệch đã được giải thích và sửa.

**P3. Hiệu chỉnh thang chấm.**

- *Việc:* 300 khóa phân tầng (nguồn, tần suất, số khối, vùng, có hoặc không có cờ), che nguồn. Hai bên chấm độc lập theo phiếu ở 8.2. Ghi trước quy tắc dừng.
- *Ai làm:* cả hai.
- *Đầu vào:* [`mau-hieu-chinh-300.tsv`](ho-so/unified/mau-hieu-chinh-300.tsv) (mẫu mới; 640 phiếu vòng 2 không dùng thay).
- *Đầu ra:* [`hieu-chinh-opus.tsv`](ho-so/unified/hieu-chinh-opus.tsv), [`hieu-chinh-astra.tsv`](ho-so/unified/hieu-chinh-astra.tsv), [`hieu-chinh-ket-qua.md`](ho-so/unified/hieu-chinh-ket-qua.md) (ma trận lẫn, κ, cách hiểu nhãn đã thống nhất, trọng số S3 đã chỉnh).
- *Xong khi:* κ của nhãn chính ≥ 0,6 và tỉ lệ đồng thuận về "có phản đối hay không" ≥ 90%. Nếu chưa đạt: sửa định nghĩa nhãn rồi chấm thêm 100 khóa.
- Tham khảo: 640 phiếu vòng 2 có κ ≈ 0,576 và đồng thuận OK/R1 so với phản đối là 555/640 = 86,7%, tức **chưa đạt**.

**P4. Chấm chéo, đủ nhãn cho mọi khóa.**

- *Việc:* **mọi** khóa còn trong rổ sau P2 đều phải có nhãn (OK/R1/R2/S/K/V/X) và lớp (C/H/K/F) từ hai bên, kể cả phần giao.
  - Opus chấm chính phần chỉ Astra; Astra chấm chính phần chỉ Opus.
  - Cả hai chấm phần giao, phần bổ sung (B), khóa tranh chấp (D) và ứng viên mới của quy tắc lấp.
  - Được ký theo lô qua bảng ID có nhãn rõ cho từng dòng.
- *Thứ tự chấm theo hiệu suất dự kiến* (mục 9.3): D, B, danh sách ưu tiên 190 khóa của Astra ([`astra/round3b/priority-for-next-review.tsv`](ho-so/astra/round3b/priority-for-next-review.tsv)), phần còn lại của rổ, rồi các bậc L2–L3 nếu cửa sức chứa chưa đạt.
- *Gộp nhãn:*
  - OK + OK → OK; có một bên R1 → R1, trừ khi phân xử và ghi lại;
  - có phản đối hợp lệ → H9;
  - cờ K2 đã đóng có thể đi cùng nhãn OK hay R1.
- *Im lặng không phải chữ ký:* ký K2, xác nhận H3 và ngoại lệ H8 đều cần hai chữ ký ghi rõ.
- *Ai làm:* chấm chéo; bên sở hữu mục chỉ được nộp phản chứng.
- *Đầu ra:* [`phieu-opus.tsv`](ho-so/unified/phieu-opus.tsv), [`phieu-astra.tsv`](ho-so/unified/phieu-astra.tsv), [`chu-ky.tsv`](ho-so/unified/chu-ky.tsv), [`phan-bien.tsv`](ho-so/unified/phan-bien.tsv), [`tranh-chap-con-lai.tsv`](ho-so/unified/tranh-chap-con-lai.tsv).
- *Xong khi:* mọi khóa có đủ nhãn hai bên; mọi phản đối đã được phản biện hoặc đã chốt loại; danh sách gửi chủ dự án (nếu có) chỉ gồm ca chính sách.

**P5. Chọn trong khóa có nhiều mặt chữ.**

- *Việc:* với **mọi** khóa còn ≥ 2 mặt chữ sau P2, mỗi bên chọn độc lập một mặt chữ hoặc BO, theo S1.
  - P1 có 503 khóa nhiều mặt chữ. Trong phép thử kịch bản mạnh của Astra còn 292 khóa, trong đó 117 khóa không thuộc 183 khóa gốc.
- *Ai làm:* cả hai, phiếu dạng dài (8.2). Kết quả lịch sử của 183 khóa gốc vẫn lưu. Khóa đã chốt (`buom`, `chim`, `ngaygio`) không bỏ phiếu lại.
- *Đầu ra:* [`phieu-chon-opus.tsv`](ho-so/unified/phieu-chon-opus.tsv), [`phieu-chon-astra.tsv`](ho-so/unified/phieu-chon-astra.tsv), [`ket-qua-chon.tsv`](ho-so/unified/ket-qua-chon.tsv).
- *Xong khi:* khóa nào hai bên trùng ý (và qua cổng) thì chốt; khóa khác ý có một lượt lý lẽ kèm số đo; còn lệch thì BO hoặc gửi chủ dự án.

**P6. Xếp hạng, cửa sức chứa và lấp đủ 7.776.**

- *Việc:* tính S2–S3 cho mọi mục đã qua cổng và có nhãn; xếp theo S4; lấy OK còn hợp hạn mức trước R1; áp Q1–Q4; lập 300 dự phòng.
- **Cửa sức chứa**, tính sau khi đóng H9 và đã chọn một mặt chữ mỗi khóa:
  - Trừ trước các suất bắt buộc (mục chủ dự án giữ).
  - Gọi `a, b, c, d` là số khóa còn lại lần lượt là OK không-F, OK-F, R1 không-F, R1-F; `qF, qR` là phần hạn mức Q3, Q2 còn lại.
  - Lấy `B = min(b, qF)`, `C = min(c, qR)`, `D = min(d, qF − B, qR − C)`.
  - Yêu cầu: `bắt buộc + a + B + C + D ≥ 7.776`, và còn đủ 300 **khóa khác** làm dự phòng, đếm theo từng ngăn hạn mức. Dự phòng R1 chỉ thay được mục R1.
  - Vì hạn mức Q2, Q3 gần như chắc chắn bị dùng hết, điều kiện thực tế là khoảng `a ≥ 7.311` để phát hành và `a ≥ 7.611` nếu 300 dự phòng đều là OK không-F.
- **Quy tắc lấp theo bậc**, khi cửa chưa đạt; không tự nới Q1–Q4 hay luật cứng:
  - **L1:** rổ P1 sau P2, chấm hết ở P4.
  - **L2:** lô đời thường mới, cả hai cùng chấm. Gồm danh từ cụ thể 3 khối (lọc theo danh từ đầu chỉ vật) và các mục mà lượt chọn cũ của Opus đã loại cả nhóm nhưng có thể qua H6 mới. Lọc bằng cổng tự động trước khi chấm.
  - **L3:** nguồn khác do hai bên đề xuất (ví dụ mục Wiktionary chưa có trong HND). Đo hiệu suất trên mẫu trước khi chấm toàn bộ.
  - **Nếu L1–L3 vẫn không đủ:** không dùng từ 3 chữ (mục 1, dòng 17). Hai bên đề xuất cách nới tiêu chí khác, kèm số liệu (số khóa thu thêm, ảnh hưởng tới chất lượng), để chủ dự án duyệt.
- *Ai làm:* Opus chạy; Astra tính lại độc lập và đọc lướt toàn bộ thành phẩm.
- *Đầu vào:* kết quả P4, P5.
- *Đầu ra:* [`xep-hang.tsv`](ho-so/unified/xep-hang.tsv) (đủ thành phần điểm), [`danh-sach-chon.txt`](ho-so/unified/danh-sach-chon.txt) (7.776 từ theo O1), [`du-phong.txt`](ho-so/unified/du-phong.txt), [`bao-cao-suc-chua.md`](ho-so/unified/bao-cao-suc-chua.md), [`bao-cao-chi-bao.md`](ho-so/unified/bao-cao-chi-bao.md).
- *Xong khi:* cửa sức chứa đạt trên danh sách xuất ra (C13), đạt Q1–Q4, báo cáo M1–M5, hai lần tính độc lập cho cùng kết quả.

**P7. Giải nghĩa sạch.**

- *Việc:*
  - Người điều phối tạo các lượt viết sạch theo D1, với lô ≤ 400 từ liên tiếp theo O1, kể cả dự phòng. Người viết tự kiểm bằng script rồi nộp.
  - Hai bên soát D6/D7 theo lô xen kẽ: mỗi người soát nửa danh sách, cộng 10% chồng chéo để đo đồng thuận; mục bị cờ thì cả hai cùng xem.
  - Mục cần viết lại giao cho lượt sạch mới, chỉ kèm đầu mục và chẩn đoán ngắn (D7).
- *Ai làm:* lượt viết sạch (do người điều phối tạo); Opus và Astra soát.
- *Đầu ra:* `giai-nghia-vN/lo-XX.tsv`, [`soat-nghia-opus.tsv`](ho-so/unified/soat-nghia-opus.tsv), [`soat-nghia-astra.tsv`](ho-so/unified/soat-nghia-astra.tsv), [`d6-log.tsv`](ho-so/unified/d6-log-v1.tsv), [`nguon-goc-giai-nghia.tsv`](nguon-goc-giai-nghia.tsv).
- *Xong khi:* không còn mã lỗi mức CHAN; D6 đạt (không còn `CHUA_KIEM`); mọi cờ đã đóng (mục cờ `NHAY_CAM`/`TUC_PHU` đã qua lại cổng H6/H7, thay bằng dự phòng nếu cần); `--phat-hanh` đạt trên toàn danh sách.

**P8. Xuất bản và kiểm.**

- *Việc:*
  - Lập nguồn chuẩn [`tools/wordlist.txt`](wordlist.txt); sinh hai khối HTML (giữ CRLF như hiện tại) và bản lưu trong tài liệu; chạy C1–C13.
  - Cập nhật README (§4 thứ tự và chính tả, §5 cập nhật danh sách, nguồn và giấy phép), mục "Quy tắc chọn từ" trong `thong-tin.html`, và tài liệu phân tích hợp nhất.
  - Đưa `tools/` vào repo.
- *Ai làm:* Opus xuất và soạn tài liệu; Astra kiểm độc lập và soát tài liệu; người điều phối ghi vào repo sau khi chủ dự án duyệt.
- *Đầu ra:* [`analyzing-tools/`](./) (xem 8.3; kế hoạch gốc đặt tên `tools/`), thay đổi repo, `bao-cao-phat-hanh.md`.
- *Xong khi:* C1–C13 đạt ở cả hai bộ kiểm; chủ dự án duyệt.

### 8.2. Định dạng phiếu (TSV)

**Phiếu chấm từ (P3, P4).** Các cột:

```
khoa  tu  nguoi_cham  nhan  lop  cong  bang_chung  trang_thai  ghi_chu
```

- `nhan`: đúng một trong các giá trị sau.
  - **OK**: dùng tốt.
  - **R1**: dùng được nhưng thiên văn viết, chuyên môn.
  - **R2**: hiếm, cổ, hẹp.
  - **S**: thuộc nhóm đỏ H6.
  - **K**: vướng cổng H7.
  - **V**: vướng H5.
  - **X**: không phải đơn vị dùng được theo H3 hoặc H2 (cụm tự do, khung câu, thành ngữ).
- `lop`: C, H, K hoặc F.
- `cong`: bắt buộc khi `nhan` thuộc R2/S/K/V/X. Ghi mã cổng: H2, H3, H5a–h, H6.1–H6.10, K0, K1, K2.
- `bang_chung`: nghĩa hoặc khóa đối chứng, số đo, ngữ cảnh. Bắt buộc khi có `cong`.
- `trang_thai`: MO (còn mở), DONG (đã đóng), PHAN_XU (đã phân xử, ghi kết quả ở `ghi_chu`).

**Phiếu ký** (K2 "không tự động chặn", xác nhận H3, ngoại lệ H8). Các cột:

```
khoa  tu  loai_ky  nguoi_ky  ly_do  ngay
```

Mỗi mục cần đủ hai dòng ký của hai bên.

**Phiếu phản biện.** Các cột:

```
khoa  tu  ben_phan_doi  cong  ben_kia  dong_y(Y/N)  phan_bien
```

**Phiếu chọn trong khóa (P5), dạng dài.** Mỗi ứng viên một dòng:

```
khoa  candidate_id  tu  nguon  nguoi_cham  chon(Y/N/BO)  ly_do
```

**Phiếu soát nghĩa (P7).** Các cột:

```
tu  ma  muc_do  mo_ta
```

- `ma`: SAI_NGHIA, NGHIA_HIEM (chọn nghĩa không phổ biến), HEP, RONG, VONG, TU_LOAI, KIEN_THUC, CHU_QUAN, LAM_SACH, NHAY_CAM, TRUNG, DO_DAI, CHINH_TA, VAN_PHONG, NGUON (vượt ngưỡng D6).
- `muc_do`: **CHAN** (phải viết lại) hoặc **NHE** (nên sửa).
- `mo_ta`: lời của người soát mô tả vấn đề. Không viết câu thay thế, không trích câu nguồn hay chuỗi bị trùng.

### 8.3. Nội dung `tools/` trong repo (MIT; không chứa văn bản kho ngữ liệu hay nghĩa từ điển)

| File | Nội dung |
|---|---|
| [`tools/README.md`](README.md) | Cách tải lại nguồn theo manifest, cách dựng và kiểm |
| [`tools/wordlist.txt`](wordlist.txt) | Nguồn chuẩn `từ\|giải nghĩa` (giải nghĩa MIT mới), định dạng ở mục 0.1 |
| [`tools/labels.tsv`](labels.tsv) | Mỗi từ: lớp C/H/K/F, nhãn OK/R1, số đo (chỉ số), trạng thái H5/H7, ngoại lệ H8 |
| [`tools/blocked_keys.tsv`](blocked_keys.tsv) | Khóa ASCII bị chặn (K0/K1) cùng mã nhóm; chỉ ghi khóa, không ghi từ tục có dấu. Không thay cho hồ sơ kiểm riêng của hai bên |
| [`tools/spelling_families.tsv`](spelling_families.tsv) | Cặp hoặc họ chính tả, số lượt mỗi kho, căn cứ loại, quyết định |
| [`tools/manifest.json`](manifest.json) | Nguồn (tên, URL, phiên bản/commit, SHA-256 file tải, giấy phép, yêu cầu ghi công), tổng số đếm, SHA-256 danh sách, phiên bản script, hash tập luật |
| [`tools/check_wordlist.py`](check_wordlist.py) | Bộ kiểm C1–C9 (Python) |
| [`tools/kiem-tra-giai-nghia.py`](kiem-tra-giai-nghia.py) | Bộ kiểm hình thức giải nghĩa (bản nháp và `--phat-hanh`) |
| [`tools/build_wordlist.py`](build_wordlist.py) | Sinh hai khối HTML và bản lưu từ [`wordlist.txt`](wordlist.txt) |
| [`tools/count_corpus.py`](count_corpus.py) | Đếm PPM/DF và họ chính tả (theo ranh giới H5) khi đã tải kho về máy (không đi kèm kho) |
| `tools/verify.mjs` | Bộ kiểm JS độc lập (Astra) |

Không đưa vào repo:

- các wordlist Hồ Ngọc Đức (GPLv2), dump Wiktionary, kho câu, giải nghĩa cũ;
- mọi chứng cứ có chứa câu nguồn (ngữ cảnh đọc kiểm, mẫu kho).

Manifest chỉ tham chiếu tới chúng. Chứng cứ để ngoài repo, nhưng đường dẫn và hash được cố định để tái lập được.

## 9. Phụ lục: phân xử và số liệu

### 9.1. Cổng đọc không dấu (H7)

Số trong ngoặc là PPM gộp (cache OPUS đóng băng).

| Kết luận | Mục | Trạng thái |
|---|---|---|
| **K0 đỏ** | *đảm đang* (↔ *dâm đãng*), *nước dãi* (↔ *nước đái*), *phích* (↔ *phịch*), *bưởi* (↔ *buồi*; không có trong danh sách nào) | Hai bên đồng ý |
| **K0 đỏ, chặn cả khóa** | `buom` (*bướm, buồm*), `chim` (*chim, chìm*) | Chủ dự án quyết (mục 1, dòng 2 và 15) |
| **K0 mở rộng** | ví dụ `phan` (↔ *phân*, nghĩa chất thải) | Astra lập danh sách có nguồn ở P1; hai bên duyệt |
| **K1 đỏ** | *màu mè, thanh trung, cảm thụ, cẩm tú, tham vấn, trưởng ban, thành gia, từ từ, bàn tính, cổ kính, lót dạ, đầu đàn, đấu thủ, tư nhân, nhà thơ, phát điện, thanh thản, đường dẫn, cắt cỏ, con đò, cô bác*; *bảo thủ* (↔ *báo thù* 11,08), *khổ thơ* (↔ *khó thở* 3,77), *kinh thành* (↔ *kinh thánh* 18,78), *làm dâu* (↔ *làm đau* 5,47), *phần đông* (↔ *phản động* 0,85); *mạnh dạn* (↔ *mảnh đạn* 0,78) | Hai bên đồng ý: Astra đã ký năm mục Opus đề nghị; Opus đồng ý nâng *mạnh dạn* lên K1 theo đề nghị của Astra |
| **K2 vàng, không vào bản 1** | *dễ dãi* (↔ *đẻ đái*); *dải đất, đồng dạng, thành nhân*; *cơ mà, đâu có, mát mắt, đón dâu* | Chưa đủ hai chữ ký |
| **Không tự động chặn** | *đại tài, đồng tình, từ trường, đôn đốc, ứng dụng, tứ tung*; *đại dương, bỏ đi, dại khờ, thành tích, độc thân, độ dốc, hồi đầu* | Hai bên ký; vẫn phải qua H6, H9 |

### 9.2. Họ chính tả (đếm lại vòng 3b)

Số đếm, căn cứ HND, độ nhạy và ghi chú đọc kiểm cho 84 cặp nằm ở [`ho-chinh-ta-ban-dau.tsv`](ho-so/discussion/ho-chinh-ta-ban-dau.tsv).

- **Cột kết luận:**
  - `QUA_RIENG_H5`: chỉ qua riêng H5, chưa phải nhận cả từ;
  - `QUA_RIENG_H5_THIEU_DU_LIEU`: cần hai chữ ký;
  - `QUA_H5G`;
  - `TRU_DIEM`;
  - `LOAI_CANH_TRANH`, `LOAI_LOI`, `LOAI_THIEU_DU_LIEU`;
  - `CHO_NGHIA`, `CHO_SAT_NGUONG`, `CHO_LOAI`.
- **Kiểm chéo:** Astra bổ sung DF trong [`astra/round2/variant-metrics.json`](ho-so/astra/round2/variant-metrics.json) và phiếu từng dòng trong [`astra/round3b/phieu-ho-77-astra.tsv`](ho-so/astra/round3b/phieu-ho-77-astra.tsv).

| Kết luận | Mục |
|---|---|
| **Loại ở bản 1, đang có trong danh sách** | Astra: *cảm ơn, xung quanh, khuyến mãi, hấp thụ, phản ánh, từ điển, đậu phộng, náo nức, ngùn ngụt, gãy gọn, hoa màu, giòn tan, chín chắn, cầu vồng, xác suất, mô tơ*. Opus: *đậu hũ* |
| **Chờ (chưa nhận ở bản 1), đang có trong danh sách** | Astra: *dao động* (sát ngưỡng), *yên trí* (chưa xác định loại), *để dành, lặp lại, thìa là* (loại e) |
| **Loại hoặc chờ, không có trong danh sách nào** | *sơ suất, tham quan, lý do, kỷ niệm, hy vọng, bánh quy, chẩn đoán, sáp nhập, chỉn chu, giấu giếm, nền nếp, xán lạn, trau dồi*; họ *mì/mỳ*; *micrô/micro*; *súc tích* (chờ) |
| **Qua riêng H5** | *thầy, đường ray, tí hon, năng suất, bánh chưng, sử dụng, sản xuất, tập trung, đặc biệt, sẵn sàng, xảy ra, chia sẻ, câu chuyện, cư xử, chải chuốt, nghỉ ngơi, giàu có, xuất sắc, mạnh mẽ, nhảy vọt, màu sắc, dòng sông, xếp hàng, vui vẻ, rực rỡ, sạch sẽ, xinh xắn, suy nghĩ, đậu xanh, sửa soạn, dỗ dành, taxi, radio*… Qua H5 nhưng trượt cổng khác: *ô tô* (H2), *bảy mươi* (H3). Cần hai chữ ký: *dông dài* |
| **Chờ dữ liệu** | Mọi cặp mới do P1/P4 đăng ký |

**Thay đổi so với bản đếm đầu** (vắt từ và dấu câu):

- *bánh chưng*: 24,1% → 0%, cả 18/18 lượt là *trưng bày*.
- *năng suất*: 16,7% → 2,2% ở phụ đề, 8/9 lượt là *tài năng \| xuất chúng*…
- *súc tích*: web 38,7% → 2,5% (*cảm xúc \| tích cực*).
- *lập lại*: web 1.327 → 98 lượt (*thiết lập \| lại*).
- *dao động*: thành chờ.

### 9.3. Sức chứa: số liệu hiện có (Opus, vòng 3b)

Rổ theo phép thử "kịch bản mạnh" của Astra ([`astra/round3b/gates-replayed.tsv`](ho-so/astra/round3b/gates-replayed.tsv)), cộng *bánh chưng*. Tỉ lệ là "OK, không thuộc lớp F", kèm khoảng Wilson 95%. Phiếu nằm trong [`ho-so/opus/cap/`](ho-so/opus/cap/).

| Nhóm | Số khóa | Tỉ lệ OK không-F | Nguồn tỉ lệ | Ước tính (khoảng) |
|---|---:|---|---|---|
| C lõi | 4.320 | 89,3% [83,4; 93,3] | Opus chấm 150 mẫu ngẫu nhiên: 134 OK, 10 R1, 6 F ([`cham_loi_150.tsv`](ho-so/opus/cap/cham_loi_150.tsv)) | 3.859 [3.602; 4.032] |
| O chỉ Opus | 3.177 | 76,0% [70,9; 80,4] | Hai bên cùng OK, 237/312 phiếu vòng 2 | 2.413 [2.253; 2.553] |
| A chỉ Astra | 3.024 | 23,6% [19,0; 29,0] | Hai bên cùng OK, 64/271 phiếu vòng 2 | 714 [573; 878] |
| D tranh chấp | 181 | ít nhất một mặt chữ OK | Suy từ tỉ lệ O và A | 145 [136; 153] |
| B bổ sung trong P1 | 529 | 39,0% [30,0; 48,8] | Opus chấm 100 mẫu ([`cham_bs_100.tsv`](ho-so/opus/cap/cham_bs_100.tsv)) | 206 [159; 258] |
| **Tổng rổ P1** | **11.231** | | | **7.338 [6.723; 7.874]** |

**Mốc cần đạt:** `a ≥ 7.311` để phát hành; `a ≥ 7.611` nếu có thêm 300 dự phòng OK không-F.

| Kho bổ sung | Số khóa | Tỉ lệ OK không-F (mẫu Opus) | Ước tính |
|---|---:|---|---|
| L2: 3 khối, đầu là danh từ chỉ vật | ≈ 138 (sau cổng) | 18/55 = 32,7% | 45 [30; 63] |
| L2: 3 khối khác | ≈ 950 | 10/80 = 12,5% | 119 [66; 204] |
| L2: mục lượt cũ của Opus đã loại cả nhóm (đỏ, hiếm) | ≈ 3.800 | khoảng 5% (đọc lướt 200 mục, chưa chấm chuẩn) | khoảng 190 |

**Kết luận:**

- **Rổ P1 đứng sát mốc phát hành và thiếu khoảng 270 khóa cho dự phòng.** Ước lượng điểm 7.338 chỉ hơn mốc phát hành 27 khóa.
  - Tỉ lệ lõi mới là của một người chấm. Mỗi 1% bất đồng ở lõi làm mất khoảng 43 khóa.
- **Cộng thêm L2**, ước lượng điểm đạt khoảng 7.690, qua mốc có dự phòng khoảng 80 khóa. Nhưng phải chấm thêm khoảng 4.900 ứng viên hiệu suất thấp.
- **Ở cận dưới của mọi nhóm cùng lúc** thì vẫn chưa chắc đủ. Cận này rất bi quan, nhưng cho thấy rủi ro có thật.
- **Không dùng từ 3 chữ** (mục 1, dòng 17). Nếu sau P4 và L2–L3 mà cửa vẫn chưa đạt, hai bên đề xuất cách nới khác kèm số liệu để chủ dự án duyệt.
- **Không thể tuyên bố "đủ" trước P4.** Cửa sức chứa ở P6 là điều kiện bắt buộc.

## 10. Mâu thuẫn giữa hai bản đề xuất: phương án Opus chọn và lý do

Mục 7, 8, 11 và 14 đã được chủ dự án chốt; những mục còn lại chờ Astra ký.

1. **Ngưỡng của cổng H7.** Chọn PPM gộp ≥ 0,3 làm **còi báo bắt buộc đọc** (theo Astra), không làm án loại tự động. Quyết định đỏ dựa trên định nghĩa K0/K1. Mục vàng không vào bản 1 nếu chưa có hai chữ ký. *Lý do:* PPM của một chuỗi không phải tần suất của nghĩa đỏ (*có kinh* phần lớn là *có kinh nghiệm*); quy tắc "phản đối hợp lệ thì không phát hành" của chủ dự án đã bảo đảm phía an toàn.
2. **Chính tả.** Lấy luật 95%/95% của Astra cho cặp cạnh tranh, cùng ngưỡng 10% (đo riêng từng kho) của Opus cho cặp chuẩn và lỗi. Mọi cặp đếm theo ranh giới âm tiết, dấu câu, từ (H5). *Lý do:* hai dạng cùng chuẩn thì người dùng có thể gõ dạng kia; với cặp chuẩn và lỗi, 10% là mức thận trọng mà không loại từ chỉ vì lỗi lẻ tẻ.
3. **Hạn mức hay chỉ báo.** Lấy **hạn mức cứng** của Astra cho R1 (≤ 388) và hư từ/đại từ (≤ 77). Mục 3 khối và C+H chỉ là chỉ báo. *Lý do:* hai hạn mức này kiểm được, nhất quán với mục tiêu chất lượng của cả hai; còn tỉ lệ C+H phụ thuộc mẫu chấm nên không nên thành cổng.
4. **4 khối.** Loại ở bản 1 (theo Astra; Opus rút đề xuất cho phép 4 tên vật ≤ 12 chữ). *Lý do:* chỉ mất 4 ứng viên, luật đơn giản hơn.
5. **Cách xếp hạng.** Bậc độ quen (OK trước R1) như Astra muốn; trong bậc thì dùng **điểm cộng có trọng số** (S3) và thứ tự tất định (S4). *Lý do:* thứ tự từ điển thuần theo lớp gợi hình sẽ loại hàng loạt từ trừu tượng rất thông dụng để nhận từ cụ thể hiếm. Điểm có trọng số thì tái lập được và hiệu chỉnh được ở P3.
6. **Chứng liệu H8.** Gộp "một lần dùng đúng nghĩa hoặc hai người duyệt" (Astra) với ngưỡng "chứng cứ mạnh" xét từng kho (Opus) để biết khi nào phải đọc ngữ cảnh.
7. **Khóa `buom`: đã chốt để trống** (mục 1, dòng 2). Opus từng đề nghị nhận *buồm*; Astra phản đối theo K0; chủ dự án chọn để trống. Từ quyết định này, K0 nay gồm cả khóa trùng một từ có nghĩa phụ tục (H7).
8. **Khóa `chim`: đã chốt để trống** (mục 1, dòng 15), không dùng *chim* lẫn *chìm*.
   - Các mục ghép (*chim sẻ, chim én, chim cánh cụt*…) có khóa khác, nên vẫn xét như toàn mục.
   - Danh sách khóa K0 mở rộng (Astra lập ở P1) áp cùng luật, có nguồn chứng thực.
9. **Các mục ghép với *bướm*:** loại *bướm đêm* (danh sách Astra) và *ong bướm* (danh sách Opus); giữ *bươm bướm* (cả hai danh sách).
   - *bướm đêm*: ngoài nghĩa loài côn trùng, còn có nghĩa bóng chỉ người bán dâm, được báo chí dùng (có chứng cứ bên ngoài, Astra đã dẫn). Số lượt của cả chuỗi **không** đo được tần suất của nghĩa này. Opus **rút ý kiến vòng 1** (từng đề nghị giữ).
   - *ong bướm*: từ điển và ngữ cảnh phụ đề đều xác nhận nghĩa bóng chỉ chuyện trăng hoa.
   - *bươm bướm*: không xác nhận được nghĩa đỏ phổ biến của toàn mục. Bản tiếng Việt còn ghi nghĩa cũ là truyền đơn và một tên cây.
10. ***da cam*: chờ, tức loại ở bản 1.** Phản đối của Astra có số liệu: ít nhất 52/76 câu Leipzig thuộc *chất độc da cam*.
11. ***ngân hà*: đã chốt giữ** (mục 1, dòng 3), viết thường như danh từ chung. *thiên hà* (có trong danh sách Opus, khóa `thienha`) xét bình thường.
12. ***sư phụ, thám tử*: chờ, tức loại ở bản 1** (phản đối của Astra; dễ thay).
13. **Hoàng gia và quyền lực.**
    - **Giữ:** nhân vật cổ tích *công chúa, hoàng tử, hoàng hậu*, theo quyết định của chủ dự án.
    - **Loại:** từ có nghĩa trung tâm là quyền lực triều chính, gồm *vua chúa, triều đại, hoàng thượng*. Đây là các mục Opus tự bỏ; Astra đã đồng ý *vua chúa, triều đại*.
    - **Opus đề nghị giữ, xét ở P4 theo cùng nguyên tắc với mục 1, dòng 3:** *nhà vua, nàng tiên, vương miện, cung điện, lâu đài* (nhân vật, đồ vật, nơi chốn trong truyện).
    - **Xét ở P4:** *ngai vàng, lên ngôi*. Nghĩa bóng phổ biến của hai mục này là "giành ngôi vô địch" trong thể thao, nhưng chúng cũng gợi việc giành quyền lực.
14. **Lấp khi thiếu: đã chốt không dùng từ 3 chữ** (mục 1, dòng 17).
    - Opus từng đề nghị giữ từ 3 chữ làm bậc lấp cuối; Astra phản đối. Chủ dự án chọn không dùng, kể cả làm dự phòng.
    - Nếu thiếu, hai bên đề xuất cách nới tiêu chí khác kèm số liệu, để chủ dự án duyệt.

## 11. Việc cần chủ dự án quyết

Các câu hỏi gửi ngày 19/11/2026 đã được quyết:

| # | Câu hỏi | Quyết định |
|---|---|---|
| 1 | Khóa ASCII trùng một từ lành có nghĩa phụ tục (`buom`, `chim`): có chặn cả khóa không? | Chặn: để trống cả hai khóa, không dùng *bướm, buồm, chim, chìm* |
| 2 | *bánh chưng* | Lượt 2: loại. Lượt 3: **giữ**, vì số đo 24% là do vắt từ |
| 3 | Có thêm *ngân hà* vào nhóm thiên thể không? | Giữ *ngân hà*, viết thường như danh từ chung |
| 4 | Có dùng từ 3 chữ để lấp khi thiếu không? | Không dùng, kể cả làm bậc lấp cuối hay dự phòng. Nếu thiếu, hai bên đề xuất cách nới khác kèm số liệu |

Hiện không còn câu hỏi mở. Nếu cửa sức chứa ở P6 chưa đạt sau L1–L3, hai bên gửi đề xuất nới tiêu chí kèm số liệu để chủ dự án duyệt.

## 12. Ký duyệt

- **Opus:** đồng ý toàn văn bản sửa vòng 3b (đã cập nhật quyết định lượt 4 của chủ dự án), 19/11/2026.
- **Astra:** đồng ý và ký bộ tiêu chí, quy trình P1–P8 đã cập nhật quyết định lượt 4, ngày 19/11/2026. Không dùng mục ba chữ ở cả danh sách chính lẫn dự phòng. Số liệu §9.3 là dự báo, không thay cửa C13; xem lần soát cuối trong [`soat-tieu-chi-astra.md`](ho-so/discussion/soat-tieu-chi-astra.md).
