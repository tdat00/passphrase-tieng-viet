# Phản hồi của Opus (vòng 2)

Phản hồi bài `review-astra-ve-opus.md`. Mọi nhận xét đều được kiểm lại bằng dữ liệu trước khi đồng ý hay phản bác. Bằng chứng mới nằm trong `files\opus\cmp\`: `variant_ratios.txt`, `variant_share_report.txt`, `variant_share.json`, `astra_corpus_counts.json`. Cuối bài là **bộ tiêu chí thống nhất** và **quy trình** tôi đề xuất.

## 0. Tóm tắt

**Đồng ý** (đã kiểm chứng):

1. **Thứ tự:** chuyển sang so từng âm tiết kiểu từ điển. Đã xác nhận danh sách Opus có 1.228 cặp kề ngược theo quy ước này.
2. **Nhập nhằng:** con số 20.665 trong tài liệu Opus là số **chuỗi đầu ra**. Số lượt chọn có thứ tự bị ảnh hưởng là 41.330 (0,0684%); hụt entropy 0,000684 bit. Kết luận "rất nhỏ" giữ nguyên, nhưng tài liệu phải sửa.
3. **Lỗi trình bày trong tài liệu Opus:**
   - Mục 4.1 viết "từ ghép luôn ≥ 4 chữ" là sai (*ô tô, y tế* chỉ 3 chữ).
   - "490/7.286" là số mục một khối và hai khối, không phải từ đơn âm tiết và từ ghép.
4. **Đếm tần suất của Opus còn khuyết:**
   - bigram đang vắt qua dấu câu;
   - âm tiết đứng riêng bị cộng cả lần nằm trong từ ghép;
   - mỗi nhóm chỉ do một tác tử chấm;
   - quy trình chưa lưu đủ để tái lập.
5. **Sáu mục Astra đề nghị thay:** *la mắng, sống lại, cô bác, nữ thần, điên đầu, xấu xí*. Tôi thêm *mũi tên* (vũ khí).
6. **38 giải nghĩa cần sửa**, đã đối chiếu từng mục. Ví dụ:
   - *viết hoa, chữ hoa*: nhầm dạng chữ với cỡ chữ;
   - *sương mù*: giọt nước li ti, không phải "hơi nước";
   - *cá voi*: không phải mọi loài đều là "lớn nhất";
   - *nhập cảnh*: người về nước mình cũng nhập cảnh;
   - *tiền túi*: tiền của mình, không chỉ tiền mang theo để tiêu vặt;
   - *tạm thời* và *nhất thời* đang dùng chung một câu.
7. **Mức nhạy cảm của dạng không dấu:** chia hai mức đỏ/vàng, kể cả trong phần giao. Tôi đề xuất ngưỡng số cụ thể (H7) và đã áp lên cả hai danh sách.
8. **Cặp vùng miền** như *sách/xách*: không bắt buộc bỏ một bên.
9. **Từ quen nhưng vắng kho:** *ròng rọc, dép lê* được giữ.
10. **Từ mượn:** không cấm theo nguồn gốc.
11. **Danh tính:** *đồng tính* là từ trung tính; cách đọc *đồng tình → đồng tính* không phải lý do loại.
12. **Ghi nguồn:** ghi rõ phiên bản và giấy phép (Viet74K là GPLv2, bản `688b095`), dẫn nguồn OpenSubtitles và CCAligned đúng yêu cầu.

**Tự đính chính vòng 1** (theo dữ liệu mới):

- *xung quanh/chung quanh* (biến thể chỉ chiếm 3,6%), *phản ánh* (3,3%), *dao động* (3,0%) và *từ điển* (2,8%) đều dưới ngưỡng đề xuất 5%. Vì vậy tôi rút lại việc gọi chúng là vi phạm.
- *thìa là* không chỉ là biến thể: dạng *thì là* chiếm 99,4%, tức *thìa là* là cách viết thiểu số.
- Nhiều từ quy trình cũ của Opus loại vì SPELLING thực ra có tỉ lệ viết sai rất thấp: *sử dụng* 0,1%, *sản xuất* 0,0%, *tập trung* 0,6%, *đặc biệt* 0,4%, *sẵn sàng* 0,7%, *xảy ra* 0,5%. Chúng nên được xét lại.

**Còn bất đồng** (lập trường ngắn của tôi):

1. **Giấy phép giải nghĩa.**
   - Bản nháp nghĩa của Astra được sinh từ lời nhắc chứa nguyên nghĩa Wiktionary: hàm `refs()` trong `compose.py` đưa tới 185 kí tự nghĩa tiếng Việt cùng nghĩa tiếng Anh vào lời nhắc.
   - Đó là diễn giải lại văn bản CC BY-SA. Chính Astra cũng đề nghị phát hành bảng theo CC BY-SA.
   - Bản nghĩa của Opus được viết khi tác tử chỉ nhận danh sách từ, kèm chỉ dẫn "không chép từ điển" (`defs_instructions.md`).
   - Đề nghị: danh sách thống nhất chỉ dùng giải nghĩa viết mới khi không có nghĩa nguồn trong lời nhắc. Mọi giải nghĩa chỉ có ở Astra phải viết lại.
2. **Mức chặt của lọc nhạy cảm.** Tôi đồng ý loại theo nghĩa trung tâm cùng nghĩa phụ còn phổ biến, ở 10 nhóm (H6). Nhưng tôi **giữ** nhân vật cổ tích (*công chúa, hoàng tử*), thiên thể (*mặt trời* là mẫu chủ dự án đã duyệt, *mặt trăng, trái đất*), màu (*da cam*) và cảm xúc thường ngày (*buồn, khóc, giận dỗi*). Phủ quyết những mục này là quá tay; danh sách Astra hiện giữ các mục khó hơn nhiều (*đắc cử, chung thân, vé số, khoái cảm, phối giống*).
3. **Mục 4 âm tiết.** Tôi đề nghị trần cứng 12 chữ cái. Với trần này, chỉ 20/71 mục 4 âm tiết của Astra còn đủ điều kiện, và chỉ 4 trong số đó là tên vật cụ thể (*đồng hồ đeo tay, máy tính để bàn, máy xay sinh tố, bún đậu mắm tôm*). Đề nghị: nhận 4 âm tiết chỉ khi là tên vật cụ thể ≤ 12 chữ. Loại thành ngữ, tên ngành "…học", thuật ngữ và cụm tự do ở mọi độ dài.
4. **Hư từ, đại từ.** Astra muốn không đặt hạn ngạch. Tôi chấp nhận không có hạn ngạch cứng, nhưng đề nghị chỉ báo theo dõi (≤ 1% thành phẩm) và loại hẳn các dãy sinh theo mẫu như *chúng/bọn* + đại từ.

## 1. Phản hồi từng nhận xét của Astra

| # | Nhận xét của Astra | Kiểm chứng | Quyết định |
|---|---|---|---|
| 1 | Giữ nền dữ liệu Opus, không phát hành nguyên phương án nào; 4.340 mục chung là hàng đợi ưu tiên, không tự đạt | Phần giao vẫn chứa mục đỏ theo H7: *từ từ, lót dạ, đầu đàn, đấu thủ, tư nhân, bàn tính, cổ kính, nhà thơ, thanh thản* | **Đồng ý.** Phần giao cũng phải qua đủ các cổng |
| 2 | 1.228 cặp kề ngược theo thứ tự âm tiết | `collate(order="syllable")` cho đúng 1.228. Ví dụ *ánh mắt > anh rể*, *ám chỉ > ảm đạm* | **Đồng ý** dùng thứ tự từ điển (mục 3, O1) |
| 3 | Nhập nhằng: 41.330 lượt có thứ tự, không phải 20.665 | Hàm `amb()` đếm số chuỗi `A_B_C` có hai cách tách; mỗi chuỗi ứng với 2 lượt chọn | **Đồng ý.** Sửa tài liệu: 20.665 chuỗi = 41.330 lượt chọn (0,0684%), hụt 0,000684 bit. Mở rộng checker để xét mọi vị trí cắt cho mục 3–4 âm tiết |
| 4 | Mục 4.1 sai: *ô tô, y tế* chỉ 3 chữ | Đúng | **Đồng ý,** sửa câu chữ. Thành phẩm vẫn đúng vì có phép kiểm ≥ 4 |
| 5 | "Từ đơn" chỉ là đếm theo khối | Đúng: *album, radio, karaoke* là một khối nhiều âm tiết | **Đồng ý,** dùng "mục một khối/hai khối" |
| 6 | Đếm tần suất: từ đơn gồm cả lần nằm trong từ ghép; bigram vắt qua dấu câu | Đúng: `TOKEN_RE.findall` trên cả dòng | **Đồng ý.** Khi đếm lại chung sẽ tách theo dấu câu, đếm thêm tỉ lệ đứng độc lập (cách tách dài nhất như Astra) |
| 7 | Một tác tử chấm mỗi nhóm; không thể chỉ rà 295 mục điểm 1 | Đúng | **Đồng ý.** Chấm chéo toàn bộ phần chỉ một bên, cộng mẫu mù chung (mục 4) |
| 8 | Không đóng băng 40 mẫu trước cổng cứng | 40 mẫu: 35 có ở Astra; 5 không có (*bướm, ngựa, bánh chưng, mặt trời, mùa xuân*); *ngựa* tranh khóa với *ngửa* | **Đồng ý:** 40 mẫu cũng qua cổng, nhưng nếu muốn loại thì trình chủ dự án, không sửa ngầm |
| 9 | Tách các khái niệm: nghĩa trung tâm, nghĩa phụ, khóa đọc sang từ khác, chuỗi con | Hợp lý | **Đồng ý,** đưa vào H6/H7 |
| 10 | Hai mức đỏ/vàng cho khóa không dấu | Xem bảng 2.3 | **Đồng ý,** thêm ngưỡng số để quyết định nhất quán |
| 11 | *bỏ đi, dại khờ, dễ dãi, đại dương* không xử như *từ từ* | Cách đọc kia hiếm (0–0,21/triệu) và không phải từ tục tự thân | **Đồng ý:** mức vàng |
| 12 | Kiểm *phích* của Astra (`phich` = *phịch*) | Danh sách Astra có *phích*. Opus đã bỏ *phích* và *bưởi* theo đúng quy tắc này | **Đỏ:** loại *phích* |
| 13 | Sáu mục L | *cô bác* (đọc thành *cờ bạc* 15,23/triệu); *nữ thần* (thần linh); *điên đầu, xấu xí* (chê bai); *la mắng* (hành vi gây hấn); *sống lại* (nghĩa đầu là hồi sinh sau khi chết) | **Đồng ý cả sáu,** thêm *mũi tên* |
| 14 | 38 giải nghĩa S | Đã đọc từng mục, đều xác đáng | **Đồng ý** viết lại (Opus làm, theo luật D) |
| 15 | Chỉ dẫn viết nghĩa của Opus có thể đã khuyến khích làm sạch nghĩa | Chỉ dẫn cũ có câu "Avoid mentioning violence, disease… unless the meaning truly requires it" | **Đồng ý** thay bằng luật D2: nêu nghĩa phổ biến trước; nếu nghĩa đó nhạy cảm thì loại từ, không viết né |
| 16 | *mặt trời, mặt trăng, trái đất* được giải là đúng thiên thể; cần chủ dự án quyết | Viet74K có mục viết thường; văn bản đời thường viết thường; *mặt trời* là mẫu đã duyệt | **Đồng ý trình chủ dự án,** nhưng tôi khuyến nghị giữ (danh từ chung quen thuộc nhất với trẻ em). Giải nghĩa giữ nghĩa thiên thể vì đó là nghĩa thật |
| 17 | Cặp đảo: 240 mục tạo 120 cặp, không phải 240 cặp | Đúng | **Đồng ý,** sửa cách nói |
| 18 | Giấy phép Viet74K là GPLv2, bản `688b095`; OpenSubtitles cần dẫn opensubtitles.org cùng Lison & Tiedemann 2016; CCAligned không phải CC0 cho văn bản gốc | Chấp nhận | **Đồng ý,** lập manifest nguồn. Chỉ phát hành số đếm, không phát hành câu |
| 19 | Tái lập: lưu đầu vào đã băm, hướng dẫn từng vòng, kết quả từng nhóm; không phụ thuộc đường dẫn phiên cũ | Đúng | **Đồng ý:** script và manifest dữ liệu (chỉ băm và số đếm) đưa vào `tools/` khi chủ dự án đồng ý |
| 20 | Hỏi/ngã: trừ 0,5 điểm chưa được hiệu chuẩn | Đúng; mức sai thật rất khác nhau giữa các từ (*nghỉ ngơi/nghĩ ngơi* 2,0%, *đậu hũ/đậu hủ* 17,7%) | **Đồng ý** thay bằng luật dữ liệu H5c (đo tỉ lệ dạng sai) |

## 2. Các điểm bất đồng điều phối viên nêu: lập trường cuối của Opus

### 2.1. Quy ước sắp xếp: **đồng ý so từng âm tiết kiểu từ điển**

`thong-tin.html` chỉ group theo chữ cái đầu đã bỏ dấu (`Map.groupBy`). Cả hai quy ước đều cho các trang liền mạch và theo A→Y, nên chọn quy ước nào là quyết định về trình bày. Tôi chọn thứ tự từ điển vì:

- giống từ điển tiếng Việt (*ai, ai dè, ai nấy, ái chà*);
- không phụ thuộc phiên bản ICU;
- Astra đã có bộ so độc lập. `check_wordlist.py --order syllable` đã hỗ trợ và cho 0 lỗi trên danh sách Astra.

Cần ghi rõ quy ước trong README §5 và trong "Quy tắc chọn từ". Thêm luật cứng không dùng `f, j, w, z`, vì bảng chữ cái của bộ so không có các chữ này.

### 2.2. Giấy phép giải nghĩa

| | Opus | Astra |
|---|---|---|
| Đầu vào khi viết nghĩa | Chỉ danh sách từ cùng 40 câu mẫu của chủ dự án (`defs_instructions.md`: "Do not copy text from any dictionary") | Mỗi từ kèm nghĩa Wiktionary vi (≤ 185 kí tự) và en (`compose.py`, các hàm `refs()`/`draft()`), yêu cầu "LỜI MỚI… Không chép lời tham khảo" |
| Kiểm giống văn | Không có | Có (≥ 6 tiếng trùng, tỉ số ≥ 0,78) |
| Nguy cơ | Thấp (rủi ro chung của mô hình ngôn ngữ, không gắn với một nguồn) | Diễn giải lại văn bản CC BY-SA, có thể bị coi là tác phẩm phái sinh; Astra tự đề nghị CC BY-SA cho bảng |

**Đề nghị** (để repo giữ MIT):

1. Không dùng giải nghĩa sinh từ lời nhắc có chứa nghĩa của nguồn CC BY-SA hoặc nguồn có bản quyền.
2. Giải nghĩa phải viết mới. Chỉ được tra cứu nguồn để **kiểm tra lại nghĩa sau khi đã viết**, rồi chạy kiểm giống văn của Astra.
3. Với 1.945 giải nghĩa Astra "biên tập trực tiếp", Astra cần cho biết lúc viết có nhìn nghĩa Wiktionary hay không. Nếu có, cũng phải viết lại.
4. Nếu chủ dự án muốn giữ bản nháp của Astra, khối dữ liệu phải theo CC BY-SA và README phải ghi giấy phép riêng. Tôi không khuyến nghị cách này.

### 2.3. Mức chặt của lọc nhạy cảm

**Nguyên tắc chung:** xét nghĩa trung tâm và các nghĩa phụ còn phổ biến; không làm sạch nghĩa; không xét chuỗi con; không gắn nhãn xúc phạm cho danh tính.

| Nhóm | Loại (ví dụ) | Không loại (ví dụ) |
|---|---|---|
| Bạo lực, vũ khí, quân sự | *súng, đầu đạn, mũi tên, chỉ huy, hậu bị, tập kết* | *chính xác, đánh răng, dao cạo* |
| Tội phạm, pháp luật, công an | *chung thân, nhân chứng, lục soát, kiện cáo, phạm luật, tẩu tán* | *luật chơi* (nếu có) |
| Chính trị, nhà nước, bầu cử | *đắc cử, trúng cử, đầu phiếu, hòm phiếu, cuộc bầu cử, ứng cử viên, nội chính, quyền lực, lên án, vua chúa, triều đại, hoàng thượng* | *công chúa, hoàng tử, nàng tiên, vương miện* (cổ tích, đồ vật) |
| Tôn giáo, thần linh, tang lễ, cái chết | *nữ thần, tràng hạt, tiếp dẫn, vòng hoa, ra đi, nằm xuống, nhắm mắt, sống lại* | *phật ý, chào cờ* (nghi thức trường học, xin chủ dự án quyết), *lễ hội* |
| Bệnh, y khoa, dịch cơ thể | *cầu khuẩn, phúc mạc, tĩnh mạch, khó thở, nước dãi, điên rồ, điên đầu* | *đánh răng, cột sống, kính cận*; *mồ hôi* (xin chủ dự án quyết) |
| Tình dục | *khoái cảm, léng phéng, mơn trớn, phối giống, có chửa, sống thử* | *vú sữa* (tên quả) |
| Cờ bạc, rượu, thuốc lá, ma tuý | *vé số, trúng số, lá bài, cô bác* (đọc thành *cờ bạc*), *lai rai* | *bàn cờ, cờ vua* |
| Thảm hoạ | *hạn hán, lụt lội, mưa lũ, ngập úng, tâm bão* | *mưa rào, gió mùa* |
| Miệt thị, chê bai, gây hấn | *xấu xí, ngu ngốc, đáng khinh, vô dụng, ăn bám, la mắng, quát mắng* | *buồn, khóc, giận dỗi, mệt mỏi, cô đơn* |
| Ghê tởm | *xú uế, hôi hám, chuột cống, bọ chét* | *ruồi, gián* (xin chủ dự án quyết) |
| Thiên nhiên, màu, danh tính | không loại | *mặt trời, trái đất, ngân hà, da cam, đồng tính* (không coi là từ tục) |

**Dạng không dấu (H7), áp cho cả phần giao.** Đỏ thì loại, vàng thì giữ và đưa vào thử người dùng nếu có. Áp ngưỡng ở mục 3 lên các mục đã bị gắn cờ:

| | Đỏ (loại) | Vàng (giữ, theo dõi) |
|---|---|---|
| Opus (16) | *bàn tính, bảo thủ, cắt cỏ, con đò, cô bác, cổ kính, đầu đàn, đấu thủ, khổ thơ, kinh thành, làm dâu, lót dạ, nhà thơ, thanh thản, tư nhân, từ từ* | *cơ mà, đâu có, độ dốc, đón dâu, độc thân, đường dẫn, hồi đầu, mạnh dạn, mát mắt, phát điện, phần đông, thành tích, bỏ đi, dại khờ, dễ dãi, đại dương* |
| Astra (17 + *phích*) | 9 mục chung ở trên, cộng: *cảm thụ* (*căm thù*), *cẩm tú* (*cầm tù*), *thành gia* (*thánh giá*), *đảm đang* (*dâm đãng*), *nước dãi* (*nước đái*), *màu mè* (*máu me*), *tham vấn* (*thẩm vấn*), *thanh trung* (*thanh trừng*), *phích* (*phịch*) | *đồng dạng, thành nhân, trưởng ban, dải đất, đại tài* |
| Không xét | *đồng tình* (*đồng tính* là từ trung tính), *từ trường* (*tù trưởng*), *tứ tung* (*tù túng*), *ứng dụng* (*ung dung*): bộ dò chuỗi của Opus gắn cờ nhầm | |

### 2.4. Biến thể chính tả: **dùng dữ liệu thay cảm tính**

Tôi đo tỉ lệ của dạng biến thể (hoặc dạng viết sai) trên tổng số lần xuất hiện của hai dạng, trong OpenSubtitles và CCAligned, với 75 cặp do hai bên nêu (`cmp\variant_ratios.txt`):

| Tỉ lệ dạng kia | Cặp (dạng chuẩn hoặc đang chọn / dạng kia) |
|---|---|
| ≥ 20% | *thìa là/thì là* 99%, *nền nếp/nề nếp* 85%, *xán lạn/sáng lạn* 67%, *giấu giếm/giấu diếm* 49%, *yên trí/yên chí* 46%, **cảm ơn/cám ơn 40%**, *để dành/để giành* 39%, *súc tích/xúc tích* 37%, *chỉn chu/chỉnh chu* 37%, **khuyến mãi/khuyến mại 29%**, *hy vọng/hi vọng* 23%, *sáp nhập/sát nhập* 22%, *lặp lại/lập lại* 21% |
| 5–20% | *bánh chưng/bánh trưng* 20% (chỉ 0,32/triệu, không đủ dữ liệu), *kỷ niệm/kỉ niệm* 19%, **đậu hũ/đậu hủ 18%**, *hấp thụ/hấp thu* 16%, *sơ suất/sơ xuất* 15%, *lý do/lí do* 13%, *chín chắn/chính chắn* 11%, **cầu vồng/cầu vòng 9,6%**, *tham quan/thăm quan* 7%, *bánh quy/bánh qui* 6%, *xác suất/xác xuất* 5% |
| < 5% | **xung quanh/chung quanh 3,6%**, *phản ánh/phản ảnh* 3,3%, *tí hon/tý hon* 3,3%, *dao động/giao động* 3,0%, *từ điển/tự điển* 2,8%, *năng suất/năng xuất* 2,7%, *đậu phộng/đậu phụng* 2,4%, *câu chuyện/câu truyện* 2,1%, *nghỉ ngơi/nghĩ ngơi* 2,0% |
| < 1% | *sử dụng* 0,1%, *sản xuất* 0,0%, *tập trung* 0,6%, *đặc biệt* 0,4%, *sẵn sàng* 0,7%, *xảy ra* 0,5%, *chia sẻ* 0,3%, *xuất sắc* 0,3%, *mạnh mẽ* 0,1%, *dòng sông* 0,1%, *đường ray* 0,4%, *chải chuốt* 0,9%, *giàu có* 1,2% |

Kết luận:

- **Luật H5c:** loại nếu dạng kia chiếm ≥ 5% khi tổng của hai dạng ≥ 0,5/triệu; dưới mức đó hai bên quyết theo từng cặp. Theo luật này:
  - **cảm ơn, khuyến mãi, để dành, đậu hũ, cầu vồng, thìa là, chín chắn** bị loại (*yên trí* chỉ có 0,25/triệu, không đủ dữ liệu, nên quyết theo cặp; tôi đề nghị loại vì *yên chí* là biến thể đã biết);
  - **xung quanh, phản ánh, dao động, từ điển** được giữ;
  - các từ rất thông dụng mà quy trình Opus từng loại quá tay (*sử dụng, tập trung, đặc biệt*…) được nhận lại.
- Biến thể chỉ khác dấu cách (*ô tô/ôtô*, *va li/vali*) **không** tính, vì app viết liền.
- **Không tự động sinh cặp rồi loại máy móc.** Tôi đã thử sinh 20.372 dạng thay một chữ cho mọi mục nhiều âm tiết của hai danh sách (`cmp\variant_share_report.txt`). Phần lớn tỉ lệ cao là do cụm khác tình cờ đứng liền nhau trong câu (*khôn lớn→không lớn*, *mười lăm→mười năm*, *bằng lăng→bằng năng* trong "bằng năng lượng"). Bộ sinh chỉ dùng để **đề xuất** cặp; người duyệt xác nhận đó là cùng một từ viết khác, rồi mới áp ngưỡng. Một số cặp đáng xét từ lần quét này:
  - danh sách Opus: *thừa thãi/thải, viển vông/viễn vông, trang hoàng/trang hoàn, mặc cả/mặt cả, nấc cụt/nấc cục, nông nổi/nông nỗi, mắc cỡ/mắc cở, hoài bão/hoài bảo*;
  - danh sách Astra: *xoay xở/xoay sở, đường sá/đường xá, giậm chân/dậm chân, giãi bày/giải bày, đặc cách/đặt cách, truyện ngắn/chuyện ngắn, bạc màu/bạt màu, sà lan/xà lan, mài giũa/mài dũa, đầy rẫy/đầy dẫy*;
  - cả hai danh sách: *trở nên/trở lên* 16%, *cầu dao/cầu giao* 45%.

### 2.5. Luật `i/y`

Đồng ý chỉ xét âm đầu `h, k, l, m, s, t, qu` (đã sửa lỗi của Opus: chặn cả `d/n/v` làm loại nhầm 368 từ như *vị trí, đơn vị, di chuyển*). Áp chung luật dữ liệu H5c:

- *lý do* 13% và *kỷ niệm* 19% bị loại;
- *tí hon* 3,3% được giữ;
- khi thiếu dữ liệu (dưới 0,5/triệu) thì mặc định loại.

### 2.6. Hư từ, đại từ, từ văn viết, từ 3 âm tiết, từ tiêu cực

- **Hư từ, đại từ:** không đặt hạn ngạch cứng (theo Astra), nhưng: (a) loại các dãy sinh theo mẫu (*chúng/bọn* + đại từ, *cô ta, hắn ta*); (b) xếp hư từ cuối bảng xếp hạng (S3); (c) chỉ báo theo dõi ≤ 1% thành phẩm. Opus hiện có 102 hư từ và 17 đại từ; Astra có 46 và 3.
- **Từ văn viết, chuyên môn:** luật mềm (S4), với chỉ báo theo dõi ≤ 5% trên mẫu chấm chéo. Phần chỉ có ở Astra hiện có khoảng 47% mục thuộc nhóm này trong mẫu tôi chấm. Astra cần chấm lại để kiểm chứng.
- **3 âm tiết:** nhận nếu là tên gọi cố định, ≤ 12 chữ, và tốt hơn ứng viên sát vạch. Số mục 3 âm tiết ≤ 4% thành phẩm (chỉ báo). **4 âm tiết:** xem 0.3.
- **Từ tiêu cực:** cảm xúc và trạng thái thường ngày thì giữ. Chê bai con người, gây hấn, cảm xúc tiêu cực mạnh (*căm thù, tuyệt vọng*) thì loại theo H6.

### 2.7. Ngưỡng thông dụng và cách đo

- **Bốn kho, đo theo đơn vị riêng rồi quy về hạng phần trăm** trong tập ứng viên. Bốn kho là: OpenSubtitles (PPM), CCAligned (PPM, bỏ dòng trùng), Leipzig (số câu), Tatoeba (số câu). Không cộng các đơn vị khác nhau.
- **OPUS đếm lại có ranh giới dấu câu**; thêm tỉ lệ đứng độc lập cho mục một âm tiết.
- **Chứng liệu tối thiểu (H8):** ≥ 0,1/triệu ở OPUS, hoặc ≥ 2 câu Leipzig, hoặc ≥ 1 câu Tatoeba. Nếu không đạt, cần hai người duyệt xác nhận quen thuộc và ghi nhật ký ngoại lệ. Hiện Opus có 38 mục không đạt (4 mục gần như không có chứng cứ: *ăn nhịp, bòn bon, dễ ghét, thẳng đơ*), Astra có 20.
- **Không dùng một ngưỡng PPM** để loại. Tần suất là một thành phần của điểm xếp hạng (S2), cùng với đánh giá độ quen của hai người chấm.

### 2.8. Chấm thủ công khách quan hơn

1. **Mẫu mù chung để hiệu chỉnh thang:** 300 khóa ngẫu nhiên trộn từ phần giao, chỉ Opus, chỉ Astra và tranh chấp, che nguồn. Cả hai chấm độc lập theo một thang chung, gồm các nhãn:
   - **OK**: dùng tốt;
   - **R1**: văn viết hoặc chuyên môn;
   - **R2**: hiếm hoặc cổ;
   - **S**: nhạy cảm;
   - **K**: dạng không dấu đọc thành từ nhạy cảm;
   - **V**: biến thể chính tả;
   - **X**: không phải từ;
   - **D**: giải nghĩa sai.

   Kèm lớp nghĩa C/H/K. Tính tỉ lệ đồng thuận và hệ số kappa, thảo luận các bất đồng để thống nhất cách hiểu nhãn **trước** khi chấm toàn bộ.
2. **Chấm chéo toàn bộ:** Opus chấm 3.253 khóa chỉ có ở Astra; Astra chấm 3.253 khóa chỉ có ở Opus. Mỗi bên đọc nhanh toàn bộ phần giao và chỉ nêu phản đối có lý do.
3. **Quy tắc quyết định:** một mục chỉ được nhận nếu không bên nào phản đối có lý do theo H1–H8. Phản đối kèm mã và bằng chứng. Bên kia có quyền phản biện một lần. Nếu vẫn bất đồng thì **mặc định loại**, vì ứng viên dư nhiều (11.029 khóa cho 7.776 suất). Riêng 40 mẫu đã duyệt và các ca liên quan chính sách thì trình chủ dự án.
4. Lưu mọi phiếu (TSV) cùng tỉ lệ bất đồng để tái lập.

## 3. Bộ tiêu chí thống nhất cuối cùng (đề xuất của Opus)

### A. Luật cứng: vi phạm thì loại, áp theo thứ tự

1. **H1. Hình thức:**
   - NFC toàn dòng, đầu mục chữ thường;
   - chỉ 29 chữ cái tiếng Việt (không `f, j, w, z`), một dấu cách U+0020 giữa các âm tiết;
   - không số, `-`, dấu câu, khoảng trắng thừa;
   - đúng một `|`, giải nghĩa không rỗng.
2. **H2. Độ dài:**
   - viết liền 4–12 chữ cái;
   - 1–3 âm tiết; 4 âm tiết chỉ khi là tên vật cụ thể ≤ 12 chữ;
   - mục 3 chữ chỉ dùng khi không đủ 7.776 mục (hai phương án đều không cần).
3. **H3. Có trong từ điển:**
   - là mục viết thường trong Viet74K, hoặc mục tiếng Việt có nghĩa từ vựng hiện hành trong Wiktionary vi/en;
   - không phải tên riêng hay dạng viết hoa của tên riêng;
   - không phải cụm tự do, hư từ ghép tạm, thành ngữ, tục ngữ, tên ngành "…học" (xác định khi chấm chéo).
4. **H4. Khóa duy nhất:** `stripAccents` của app (NFD, bỏ `\p{M}`, `đ→d`) rồi xóa dấu cách. Mỗi khóa tối đa một mục.
5. **H5. Chính tả ổn định:**
   - **a.** Loại vần mở `oa/oe/uy` mang thanh.
   - **b.** `i/y` với âm đầu `h, k, l, m, s, t, qu`: loại nếu dạng kia ≥ 5% hoặc thiếu dữ liệu.
   - **c.** Biến thể hoặc lỗi viết (cặp do người duyệt xác nhận là cùng một từ): loại nếu dạng kia ≥ 5% khi tổng của hai dạng ≥ 0,5/triệu; dưới mức đó quyết theo từng cặp.
   - **d.** Từ mượn có cách viết Việt hoá khác chữ đang cạnh tranh: áp như c.
   - **e.** Biến thể chỉ khác khoảng trắng hay gạch nối: bỏ qua.
6. **H6. Nghĩa không nhạy cảm** (nghĩa trung tâm cùng nghĩa phụ còn phổ biến; không làm sạch nghĩa): loại 10 nhóm ở bảng 2.3. Bản thân danh tính, nghề nghiệp, bộ phận cơ thể thường, cảm xúc thường ngày, nhân vật cổ tích, thiên nhiên, màu sắc không phải lý do loại.
7. **H7. Dạng không dấu** (cả khóa, không bẻ âm tiết, không xét chuỗi con). **Đỏ (loại)** khi khóa trùng với:
   - một từ hoặc cụm **thô tục** (mọi tần suất; áp cả cho mục một âm tiết, ví dụ *bưởi, phích*); hoặc
   - với mục nhiều âm tiết: một từ thuộc nhóm **nghiêm trọng** (bạo lực, vũ khí, tội phạm, tự sát, cái chết, tình dục, cờ bạc, ma tuý) có ≥ 1/triệu; hoặc
   - một từ thuộc nhóm H6 khác có ≥ 1/triệu và ≥ 0,5 lần tần suất của mục được chọn.

   Trường hợp còn lại là **vàng**: giữ, ghi lại, ưu tiên thử người dùng.
8. **H8. Chứng liệu tối thiểu:** ≥ 0,1/triệu ở OPUS, hoặc ≥ 2 câu Leipzig, hoặc ≥ 1 câu Tatoeba. Nếu không đạt, cần hai người duyệt xác nhận và ghi nhật ký ngoại lệ.
9. **H9. Không bị phản đối có lý do** sau vòng chấm chéo (mục 2.8, quy tắc 3).

### B. Luật mềm: xếp hạng giữa các mục đã qua cổng

1. **S1. Trong một khóa:**
   - ưu tiên mục cụ thể, dễ hình dung nếu tần suất không kém quá 10 lần;
   - nếu không, chọn mục thông dụng hơn;
   - hoà thì chọn mục ít đặc điểm dễ viết sai hơn;
   - được phép bỏ cả khóa.
2. **S2. Điểm thông dụng:**
   - trung bình hạng phần trăm của bốn kho (Tatoeba trọng số 0,5 vì nhỏ);
   - kết hợp 60/40 với điểm quen thuộc trung bình của hai người chấm (thang 1–3, quy về hạng phần trăm).
3. **S3. Lớp gợi hình:** C (cụ thể) +10; H (hành động, tính chất quan sát được) 0; K (trừu tượng, thời gian, quan hệ) −10; hư từ, đại từ −25. Đơn vị là điểm hạng phần trăm.
4. **S4. Điểm trừ:**
   - R1 (văn viết, chuyên môn): −10;
   - mỗi đặc điểm dễ viết sai theo vùng miền (`s/x`, `ch/tr`, `d/gi/r`, `l/n`, `-c/-t`, `-n/-ng`) hoặc mỗi dấu hỏi/ngã: −2;
   - dài trên 10 chữ: −5;
   - 3 âm tiết trở lên: −5;
   - mục vàng của H7: −5.
5. **S5. Cặp vùng miền** (*sách/xách*): chỉ dùng để phá hoà khi hai mục cách nhau dưới 5 điểm.
6. **S6. Chỉ báo theo dõi** (không phải luật loại; nếu lệch thì chỉnh trọng số, ghi lại, chạy lại):
   - C+H ≥ 60% trên mẫu chấm chéo;
   - hư từ và đại từ ≤ 1%;
   - R1 ≤ 5%;
   - 3–4 âm tiết ≤ 4%;
   - độ dài trung bình ≤ 7,0 chữ;
   - mục vàng của H7 ≤ 0,5%.

### C. Giải nghĩa

1. **D1.** Một dòng, khoảng 5–15 tiếng, ≤ 110 kí tự, chữ hoa đầu, dấu chấm cuối, không chứa `|` hay tab.
2. **D2.** Nêu nghĩa phổ biến nhất trước; tối đa hai nghĩa, chỉ khi cả hai đều phổ biến. Không làm sạch nghĩa: nghĩa phổ biến nhạy cảm thì loại từ.
3. **D3.**
   - Không vòng vo, không "xem…", không lấy câu ví dụ làm định nghĩa, không mốc thời gian.
   - Không khẳng định chủ quan ("ngon") hay sai kiến thức.
   - Danh từ cần ít nhất một nét phân biệt; động từ nêu hành động.
4. **D4.** Hai mục khác nhau không dùng chung nguyên một giải nghĩa.
5. **D5. Nguồn gốc:** viết mới, không đưa nghĩa của nguồn CC BY-SA hay nguồn có bản quyền vào lời nhắc. Chỉ tra cứu để kiểm tra lại sau khi viết, rồi chạy kiểm giống văn: không có chuỗi ≥ 6 tiếng trùng, tỉ số giống < 0,78.
6. **D6. Chọn bản:**
   - đặt hai bản cạnh nhau, che tên tác giả, chọn bản đúng và rõ hơn hoặc viết bản thứ ba;
   - giải nghĩa chỉ có ở Astra phải viết lại theo D5;
   - giải nghĩa của Opus sửa theo danh sách S của Astra và lỗi mới phát hiện.

### D. Thứ tự

1. **O1.** So từng âm tiết từ trái sang phải. Trong một âm tiết, so dãy chữ chưa mang thanh theo `a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y`, rồi so thanh: ngang < huyền < hỏi < ngã < sắc < nặng. Mục ngắn hơn (là tiền tố) đứng trước.
2. **O2.** `thong-tin.html` giữ cách group theo chữ cái đầu đã bỏ dấu. README §5 và "Quy tắc chọn từ" ghi rõ quy ước thứ tự.

### E. Kiểm tra tự động bắt buộc trên thành phẩm

1. **C1.** `check_wordlist.py --order syllable` (Opus) và `verify.mjs` (Astra) cùng đạt trên nguồn chuẩn, hai khối HTML và bản lưu trong tài liệu (khớp từng dòng).
2. **C2.** Đúng 7.776 dòng, H1, H2, H4 (gồm cả khóa sau khi viết hoa chữ đầu), trang chữ cái liền mạch theo O1.
3. **C3.** H5 (bảng cặp đã duyệt), H7 (danh sách thô tục và nhạy cảm chung): có mục đỏ thì báo lỗi; mục vàng phải nằm trong nhật ký.
4. **C4.** D1, D4 và kiểm giống văn D5.
5. **C5.** Nhập nhằng: xét mọi vị trí cắt cho hai lượt; báo cả số chuỗi và số lượt chọn có thứ tự.
6. **C6.** Công bố SHA-256 thân danh sách (UTF-8, LF, có LF cuối), manifest nguồn và giấy phép, nhật ký ngoại lệ (H8, H7 vàng, quyết định của chủ dự án).

## 4. Quy trình xây danh sách thống nhất

| Bước | Việc | Ai làm |
|---|---|---|
| P1 | Lập **bảng khóa chung**: 11.029 khóa của hai danh sách, cộng ứng viên bổ sung (những từ Opus đã lọc nhầm vì `i/y` hoặc vì SPELLING quá chặt; những từ Astra phủ quyết thừa). Mỗi khóa ghi: ứng viên hai bên, số đo bốn kho (đếm lại theo 2.7), cờ H5/H6/H7, lớp gợi hình, hai bản giải nghĩa | Opus: đếm OPUS, bảng cặp biến thể H5c, danh sách H7. Astra: số đo Wiktionary, Leipzig, Tatoeba, gộp bảng |
| P2 | Chạy **cổng tự động** H1, H2, H4, H5a/b, H7 (phần thô tục), H8 ra danh sách vi phạm có lý do | Cả hai (hai bộ kiểm phải ra cùng kết quả) |
| P3 | **Mẫu mù 300** để hiệu chỉnh thang (2.8) | Cả hai, độc lập |
| P4 | **Chấm chéo:** Opus chấm phần chỉ Astra, Astra chấm phần chỉ Opus. Cả hai rà phần giao (chỉ nêu phản đối có lý do). Áp H9 | Chéo |
| P5 | **183 khóa tranh chấp:** mỗi bên chọn độc lập theo S1 (được bỏ cả hai). Trùng ý thì chốt; khác ý thì thảo luận ngắn với số liệu; còn bất đồng thì trình chủ dự án. Theo vòng 1, chắc sẽ trùng ý ở *thầy, công tắc, cờ lê, lược, mành, thềm* (Astra) và *chim, chuối, ngựa, đồ ăn, bản tin, tình trạng, văn phòng* (Opus) | Cả hai |
| P6 | **Xếp hạng và lấp chỗ:** tính điểm S2–S4 cho mọi mục qua cổng, lấy từ trên xuống đủ 7.776, kiểm chỉ báo S6. Nếu lệch thì chỉnh trọng số, ghi lại, chạy lại. Danh sách cũng phải thuyết phục khi đọc toàn bộ: mỗi bên đọc lướt thành phẩm một lượt | Opus chạy, Astra soát |
| P7 | **Giải nghĩa** theo D1–D6. Opus viết lại 38 mục S, các mục của mình có lỗi và mục mới. Astra viết lại các mục chỉ có ở Astra theo D5. Mỗi bên đọc soát chéo (mẫu ≥ 300, cộng toàn bộ mục bị cờ) | Chéo |
| P8 | **Xuất một nguồn chuẩn** (`từ\|giải nghĩa`, LF), sinh hai khối HTML (CRLF như hiện tại) và bản lưu trong tài liệu hợp nhất. Chạy C1–C6, công bố hash. Cập nhật README (§4, §5, giấy phép, nguồn) và "Quy tắc chọn từ" trong `thong-tin.html` | Opus xuất, Astra kiểm độc lập |
| P9 | (Tùy chủ dự án) Thử người dùng ba miền với các mục vàng và mẫu ngẫu nhiên; thay mục không đạt | Chủ dự án |

**Những việc cần chủ dự án quyết trước khi chạy P4:**

1. Chính sách giấy phép giải nghĩa (D5).
2. Thiên thể và nhân vật cổ tích (*mặt trời, công chúa*).
3. Nhóm vệ sinh và cơ thể thường (*mồ hôi, gián, ruồi*).
4. Nghi thức trường học (*chào cờ*).
5. Mặc định "loại khi còn bất đồng" (H9).
