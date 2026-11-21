# Phân tích độc lập: 205 từ dự phòng và honorable mentions

**SA-Astra — vòng 1, ngày 20/11/2026.**
**Trạng thái:** phân tích độc lập, chưa có chữ ký review chéo, không phải lệnh thay từ.
**Base đã kiểm:** `cefb99386d4845e40bc2d3eabc7d6898d078305d`; nhánh `analyze/du-phong-v2`.

Quy ước: **verified** = đã đối chiếu dữ liệu/mã/hồ sơ hoặc yêu cầu chủ; **assumed** = nhận định ngôn ngữ, đề xuất thiết kế hay ước lượng của Astra, chưa được coi là quyết định chung. “Verified hồ sơ” không có nghĩa đã tải và đọc lại từ điển/ngữ liệu. Dẫn nguồn có dòng thuộc base trên, trừ đầu ra mới trong thư mục này.

Tên ngắn: `AT = analyzing-tools`; `U = AT\ho-so\unified`; `E = AT\ho-so\astra\du-phong-v2\evidence`. Mọi đường dẫn trong báo cáo tính từ gốc repo.

## 1. Tóm tắt

- **verified:** Đã đối chiếu đủ 205 từ; 128 không-F, 77 F, đều mang nhãn OK lịch sử; không có lớp C.
- **assumed:** Đề nghị 158 A ưu tiên, 37 B cần nghĩa sạch, 10 C ưu tiên thấp/cần thống nhất sắc thái; chưa có căn cứ loại cứng mới.
- **verified:** 168 câu hiện có khớp PASS D6 lịch sử và có phiếu D7 đúng lượt; 37 câu thiếu đều thuộc F.
- **verified:** Không có dòng D8 cho 205 dự phòng; A không đồng nghĩa được thay ngay.
- **verified:** Đề cử 200 honorable mentions: 117 bị loại vì D6, 10 vì D7, 73 R1; mọi khóa khác chính và dự phòng.
- **assumed:** Chỉ bổ sung bảng phân loại và tài liệu, không sửa luật, danh sách chính hay viết giải nghĩa.
- **verified:** Hai bộ kiểm phát hành lỗi sẵn do CRLF ở checkout; cùng mã kiểm trên đúng blob Git LF đạt.
- **verified:** Ba tệp chính và toàn §10 giữ nguyên byte; chưa mở thêm nguồn ngữ liệu.

## 2. Hiểu yêu cầu

### Mục tiêu, người dùng và giới hạn

- **verified — yêu cầu chủ trong lời giao việc:** phân tích tiếp 205 dự phòng, thêm khoảng 100–300 từ “có thể” cân nhắc; chưa phát hành và không phải khôi phục cửa 300 dự phòng.
- **verified — phạm vi bất biến:** `index.html`, `thong-tin.html`, `AT\wordlist.txt` và toàn §10 của `WordListAnalyze.md`; đối chiếu hash byte trước/sau ở `E\inventory.json` và `E\verification.json`.
- **verified — quyết định 8/10:** không từ ba chữ, kể cả dự phòng; phát hành 7.776 không cần đủ 300 dự phòng. Nguồn: `WordListAnalyze.md:151–153`.
- **verified — quyền ghi đợt này:** chỉ thư mục Astra hiện tại; chưa sửa §11, README, manifest, nhãn hoặc D8. Không commit, chuyển nhánh hay push.
- **assumed — người dùng trực tiếp:** người bảo trì cần biết từ nào còn việc gì và thay được ngăn nào. Người dùng ứng dụng không thấy thay đổi hành vi, xác suất hay nội dung.
- **assumed — cách hiểu “honorable mention”:** danh mục xem xét, không phải danh sách đạt phát hành, không tự cho thêm lượt viết sau D7, không tự nâng R1 thành OK.

### Giới hạn chứng cứ

- **verified:** chỉ dùng đầu mục, số đếm, nhãn, hash và phiếu đã lưu. Không tải kho, lưu câu nguồn, trích định nghĩa hoặc viết lời giải mới; phù hợp `AT\ho-so\README.md:15–19`.
- **verified:** mọi nhận định mới về độ quen, sắc thái hoặc nghĩa phụ được đánh dấu `assumed`; các cổng ngữ nghĩa cần review chéo trước khi thành kết luận chung.
- **verified — minh bạch độc lập:** không mở phân tích, phiếu hoặc đề cử mới của Opus. Sau khi hai bảng 205/200 đã được ghi, một lệnh `rg` mã Python ở phạm vi AT vô tình trả thêm một dòng hàm SHA chung trong thư mục Opus mới. Không mở tiếp, không dùng dòng đó làm chứng cứ hoặc sửa phân loại. Không nên mô tả điều này là tuyệt đối không có kết quả tìm kiếm từ thư mục kia.

## 3. Hiện trạng và bằng chứng

### 3.1. Không nhầm các mốc pool

**verified:** kết quả đo từ `E\inventory.py`, đầu vào/hash ở `E\inputs.json`:

| Mốc | Số mục | Cách đối chiếu |
|---|---:|---|
| P6 cuối | 10.156 | 9.552 L1 + 321 L2A + 148 L2B + 51 L2C + 111 L3 − 27 |
| `U\xep-hang.tsv` đang lưu | 10.133 | P6 trừ 22 + 1 mục H6 của P7 v1/v2 |
| Sau trừ 132 mục nghĩa cuối | 10.001 | Khớp `U\p7-v3-c13-hoa-astra.json:2–24` |
| Danh sách phát hành | 7.776 | C 2.915; H 3.169; K 1.615; F 77; R1 = 0 |
| Dự phòng nguyên trạng | 205 | H 85; K 43; F 77; C = 0 |
| Ngoài chính và dự phòng, chưa trừ lỗi nghĩa trong bảng xếp hạng cũ | 2.152 | 132 mục D6/D7 + 2.020 mục khác |
| Ngoài chính và dự phòng sau trừ lỗi nghĩa | 2.020 | 159 OK-F + 1.839 R1 không-F + 22 R1-F |

**verified:** không thể gọi 2.152 mục là “đều dưới điểm cắt”. Trong đó 132 mục từng được chọn rồi bị trừ vì nghĩa. Cũng không thể lấy 159 OK-F hay 1.861 R1 làm thêm ghế thay OK không-F. Nguồn luật: `WordListAnalyze.md:436`, `WordListAnalyze.md:724–736`; hồ sơ lịch sử: `U\bao-cao-suc-chua.md:9–35`.

### 3.2. Tái kiểm 205 từ

**verified:** `du-phong-phan-loai.tsv` có đúng một dòng mỗi từ, đúng thứ tự `AT\du-phong.txt`. Script kiểm H1/H2 số học, H4, cả khóa viết hoa, H5a, bảng họ đã đăng ký, biến thể thua, bảng K0/K1/K2, chứng cứ H3, chữ ký và hồ sơ H9. Kết quả:

- 205/205 dài 4–12 chữ, không có từ ba chữ hoặc mục ba khối; không trùng chính, không trùng nhau.
- Không trúng khóa chặn; không trúng họ chính tả bị loại/chờ. *Dễ ợt* trúng họ `TRU_DIEM`, không phải loại.
- 31 mục cần H3 có đủ hai chữ ký; *ăn nhịp* đủ hai chữ ký H8; *hì hụi, mụ mị* đủ H5; *làm cỗ* đủ K2.
- H8 số học: 200 mạnh, 4 yếu, 1 không-lượt. Bốn mục yếu là *cửu chương, lời lỗ, tạnh ráo, thẳng đơ*; đều có đọc kiểm đúng nghĩa trong phiếu cũ, không phải bốn ngoại lệ thiếu chữ ký.

**verified — đối chiếu quan trọng:** `U\chu-ky.tsv:11–12` (*ăn nhịp*), `:1154–1155` (*hì hụi*), `:1358–1359` (*làm cỗ*), `:1592–1593` (*mụ mị*); đọc kiểm H8 tại `U\phieu-astra.tsv:2490`, `:3436`, `:4359`, `:4411`. Không khôi phục phản đối H5 đã rút chỉ vì chuỗi máy sinh `i/y` thiếu dữ liệu. Điều kiện H8 ở `AT\tieu-chi-thong-nhat.md:171–178` chỉ đòi hai chữ ký ngoại lệ khi thật sự không có lượt.

**assumed — nhận định từng từ:** đã ghi riêng lý do/sắc thái trong phiếu 205 dòng `E\reserve-judgements.tsv`. Không loại cơ thể thông thường, cảm xúc nhẹ, trò chơi trí tuệ hoặc toàn mục lành chỉ vì một âm tiết gợi đỏ. Chẳng hạn *cờ vây* không tự thành cờ bạc; *làm cỗ* không tự thành nghi lễ; *mệt lả* không tự là tên bệnh. Từ gần nghĩa không mặc nhiên là cùng họ chính tả.

**assumed — 10 C:** *ăn trầu, bèo bọt, chấp nhặt, giở giọng, giở quẻ, mụ mị, non choẹt, thụp, tía lia, tuổi xanh*. Tám mục liên quan sắc thái/nghĩa cần thận trọng; riêng *thụp* là độ quen đầu mục độc lập, *tuổi xanh* thiên văn chương. Đây là mức ưu tiên, **không** phải 10 phản đối H9 hợp lệ mới hoặc 10 mục bị đổi nhãn/loại cứng. Không có chứng liệu ngữ cảnh mới để tuyên bố đã lật kết luận cũ.

### 3.3. Nghĩa và ngăn thay thế

**verified:** 168 câu lưu tại `U\p7-v4-du-phong-168-co-nghia-cho-duyet.tsv` khớp đúng log D6: 123 v1, 35 v2, 10 v3. Phiếu D7 cùng lượt không còn CHAN; hai phiếu NHE không phải cổng loại. Bốn câu có `HAI_NGHIA`. Kiểm D2/D5/cờ chung 7.944 câu hiện có: 0 lỗi, 0 cảnh báo (`E\verification.log:76–85`).

**verified — lưu ý hash:** cột `sha256_giai_nghia` trong log D6 băm JSON của token chuẩn hóa, không phải byte câu nguyên văn (`AT\d6-kiem.py:441`). Bảng mới lưu riêng `gloss_sha256` và `d6_token_sha256`, nối PASS đúng lượt. Không mượn log v1 cho câu v2/v3.

**verified:** toàn bộ 37 mục chưa viết đều thuộc F; danh sách chính đã dùng đủ 77 F và không có R1. Có ánh xạ lý thuyết 205 ghế riêng biệt, không đụng 14 mục chủ buộc giữ: 85 ghế H, 43 ghế K, 77 ghế F (`E\substitution-slots.tsv`). Ghế là mã tượng trưng, không đề nghị xóa bất kỳ từ chính nào.

**verified:** theo Q và quy tắc P6 hiện hành:

- OK-F chỉ thay một ghế F khi Q3 đang đầy; không giả định sẽ rút trước một F khác để lấy “tín dụng”.
- OK không-F thay ghế OK không-F thuộc C/H/K; thay F thì giảm F cũng hợp hạn mức nhưng không cần dùng hướng đó để chứng minh 205 ghế.
- Không có hạn mức cứng riêng C/H/K; ưu tiên cùng lớp chỉ là đề nghị chất lượng.
- R1 chỉ thay R1; 388 là trần chứ không phải quyền tự đưa 388 R1 vào khi OK còn đủ.

**verified:** `AT\nguon-goc-giai-nghia.tsv` có 7.776 PHAT_HANH và 182 LOAI, **0** dòng của 205 dự phòng. Vì vậy không gọi 168 câu có hồ sơ đạt là 168 gói thay thế D8 hoàn chỉnh. Máy này thiếu `AT\vi.jsonl.gz`; chưa chạy lại D6 với đủ tham chiếu. Đây là đối chiếu PASS lịch sử, không phải PASS D6 mới.

### 3.4. Hai trăm honorable mentions

**verified:** `honorable-mentions.tsv` có 200 khóa mới đối với cả chính và 205 dự phòng, xếp O1; Python và JS kiểm độc lập cho tổng hợp 8.181 khóa duy nhất.

| Nhóm | Số | Vì sao chưa ở bản chính |
|---|---:|---|
| HM_D6 | 117 | Đầu mục từng OK, câu cuối trượt D6 |
| HM_D7 | 10 | Đầu mục từng OK, câu cuối trượt D7 |
| HM_R1 | 73 | Bậc R1 đứng sau OK; bản hiện hành không có ghế R1 |

**verified:** lớp C/H/K/F lần lượt 117/44/34/5; ngăn gồm 122 OK không-F, 5 OK-F, 73 R1 không-F. Nguồn là 195 L1, 2 L2A, 3 L3. Cả 200 có chứng liệu mạnh theo số học; mỗi dòng có số bề mặt, số sạch, DF Leipzig/Tatoeba, F/G/T/điểm, hạng lịch sử, nguồn đề cử/từ điển và tham chiếu dòng. Có 18 mục đủ hai chữ ký H3; *chia* đủ hai chữ ký K2. “F điểm thông dụng” không phải “lớp F”.

**assumed:** đây là chọn có chủ đích, không phải mẫu đại diện hoặc phép chứng minh mọi người đều biết 200 từ. Nhóm đầu cho cơ hội phục hồi chất lượng từ cụ thể; nhóm R1 bổ sung ý tưởng học tập/nghề nghiệp mà không giả nhãn OK. Ví dụ *ngân hàng, cô giáo, dãy núi, vỏ sò, thợ may* là ứng viên khác về trạng thái với *lập trình, piano, tinh thể*.

**verified:** 132/182 LOAI là D6/D7, 50 còn lại liên quan H5/H6/H9. Chỉ lấy 127 trong 132 mục nghĩa: tạm không đề cử *cơ quan, lực lượng, truy tìm, dự bị, lên chức*. **assumed:** năm mục này cần rà nghĩa/ngữ cảnh thêm; không khẳng định bị loại cứng mới. Không tái đưa 50 mục loại cổng cứng, từ ba chữ, P5 loser trùng khóa hay biến thể thua vào để đủ số.

**assumed:** không đề cử *hạ lưu*: cần tránh “làm sạch” nghĩa miệt thị bằng nghĩa địa lý. **verified:** bốn đề cử thử *bộ giải mã, bộ chuyển đổi, thảm thực vật, khung gầm* chưa nối được đủ chữ ký H3 từ bảng thống nhất, nên để ngoài thay vì suy chữ ký từ việc có mặt trong pool; điều này không chứng minh chữ ký không tồn tại ở hồ sơ L2 khác. Nhật ký giữ/bỏ: `E\candidate-exclusions.tsv`.

**verified:** 127 mục lỗi nghĩa không được tự có lượt viết thứ tư chỉ nhờ được đưa vào honorable mentions (`AT\tieu-chi-thong-nhat.md:303–308`, `WordListAnalyze.md:746`). 73 R1 cũng không bổ sung 73 ghế thay bản hiện tại. **assumed:** không cần mở 147 ứng viên L2D/L3b hoặc tìm từ mới ngoài pool để hoàn thành yêu cầu phân tích lần này.

### 3.5. Bộ kiểm hiện tại và lỗi nền CRLF

**verified:** bộ kiểm Python chỉ dùng dòng `CHINH` khi xét Q (`AT\check_wordlist.py:139–151`), tách đúng tiêu đề §10 (`:168–173`); JS tách cùng tiêu đề và chỉ kiểm khóa chặn ở C5. Hai bộ kiểm không tự thẩm định bảng dự phòng/HM, H3, H6, H8, H9; JS không đọc bảng họ chính tả hoặc hạn mức. Không thể dùng “7776 PASS” để chứng nhận 405 dòng phân tích.

**verified:** trước khi có đầu ra phân loại, `git ls-files --eol` cho `AT\wordlist.txt` là `i/lf w/crlf`; `core.autocrlf=true`. Chạy trực tiếp:

| Kiểm | Checkout nguyên trạng | Đối chứng blob LF đúng commit |
|---|---|---|
| `check_wordlist.py` | 1 lỗi C1 | 0 lỗi, 0 cảnh báo |
| `verify.mjs` | 1 C1 và 2 C8 | 0 lỗi |
| `build_wordlist.py --check` | Khớp cả ba khối | Không cần đối chứng |

**verified:** script đối chứng chỉ cung cấp byte `git show cefb993:analyzing-tools/wordlist.txt` trong bộ nhớ cho đúng thao tác đọc nguồn chuẩn; không sửa mã checker, working tree hoặc đổi nội dung. Byte đó bằng chính checkout sau quy đồng duy nhất CRLF→LF, SHA `1d4fc3e803c4cb40ee39f3abe25fccd7815f1e750198b4b1fc1166753233f581`. Log có đầy đủ command, stdout và exit code, không che lỗi native.

**assumed:** trong phạm vi chủ đã chốt bất biến byte, chấp nhận đối chứng chuẩn LF cùng việc không tăng lỗi nền; không sửa `.gitattributes` hay checkout nguồn chính trong đợt này. Nếu cần hai lệnh native xanh trên Windows, đó là việc định dạng riêng ngoài phạm vi hiện tại.

## 4. Các phương án

**assumed — so sánh thiết kế/công/rủi ro:**

| Phương án | Thiết kế | Công | Rủi ro và tác động |
|---|---|---|---|
| Chỉ viết lời tổng kết | Ghi con số 205/168/37 và một danh sách HM | Thấp | Không trả lời được từng từ, chữ ký và ngăn; thiếu yêu cầu |
| **Bảng phân loại có chứng cứ, chính bất biến** | 205 dòng + 200 HM, trạng thái nghĩa riêng, cập nhật §11–12/README/manifest sau hòa | Vừa, hữu hạn | Người bảo trì có đường đi rõ; người dùng app không đổi |
| Tuyển/đếm mới và làm sạch nghĩa ngay | Mở L2D/L3b, thêm nguồn hoặc viết lại 127+37 câu | Cao hơn, chưa ước lượng chắc | Trộn phân tích với khôi phục/phát hành, cần quyền D7 và chi phí khác |

**assumed — khuyến nghị:** phương án thứ hai. Không đặt mục tiêu tìm thêm “95 ghế đủ nghĩa” hoặc ép đủ 300 dự phòng; quyết định 10 đã bỏ điều kiện đó.

## 5. Kế hoạch đề xuất

### 5.1. Định nghĩa tầng, không lẫn với nhãn cũ

**assumed — tầng dùng cho báo cáo chung:**

| Tầng | Định nghĩa | Kết quả vòng độc lập |
|---|---|---:|
| A | Ưu tiên xem xét thay: đầu mục có hồ sơ qua cổng, câu đã đạt lịch sử; còn D8, ký chung và kiểm bộ thay thế | 158 = 118 không-F + 40 F |
| B | Dùng được về đầu mục theo hồ sơ, thiếu câu sạch; không được thay bằng khóa trống | 37 F |
| C | Ưu tiên thấp hoặc cần thống nhất sắc thái/độ quen; giữ nhãn gốc, không tự mở phản đối H9 | 10 không-F |
| D | Có vi phạm cứng mới đủ bằng chứng và xử theo H9; giữ dòng lịch sử, không đếm đủ điều kiện | 0 ở vòng này |

**assumed:** đổi số tầng sau review chéo được ghi rõ là kết luận chung; không dùng các số 158/37/10 như một quyết định của chủ. Nếu C chưa được ưu tiên, A+B tối đa 195 ứng viên theo ngăn, trong đó B vẫn thiếu nghĩa. Không gọi đó là “195 sẵn sàng”.

### 5.2. Tệp dữ liệu cuối

**assumed — đích sau bước báo cáo chung, chưa ghi trong vòng này:**

1. `AT\du-phong.txt`: giữ đúng 205 từ, một từ mỗi dòng, O1, không tiêu đề/chú thích/nhãn; giữ nguyên tập và byte nếu không có lý do đổi. Các mục C vẫn ở đây như danh mục dự phòng lịch sử.
2. `AT\du-phong-phan-loai.tsv`: một dòng mỗi mục, khóa ngoài chính; dùng schema hai bảng mẫu trong thư mục này.
3. `AT\honorable-mentions.tsv`: bảng riêng, tuyệt đối không ghép vào `du-phong.txt` hoặc `wordlist.txt`.
4. `AT\labels.tsv`: **không cần sửa**. Giữ 7.776 CHINH + 205 DU_PHONG và nhãn/lớp gốc; tầng mới nằm ở bảng phân loại.
5. `AT\nguon-goc-giai-nghia.tsv`: **không cần sửa trong phân tích**. Giữ 182 LOAI và toàn bộ nguồn gốc cũ; bảng mới tham chiếu lịch sử nghĩa, không giả đã bổ sung D8. Khi được phép chuẩn bị thay thật mới hoàn tất D8.

**verified:** schema mẫu đã có các nhóm cột:

- định danh: `tu`, `khoa`, `nhan`, `lop`, `ngan`, `so_chu`, `so_khoi`;
- quyết định phân tích: `tang`, `thay_ngan`, `uu_tien_lop`, `danh_gia_moi`, `rui_ro_can_luu_y`, `vi_sao_chua_chon`;
- cổng độc lập: `H1` đến `H9`, `D6_D7`, `thieu_truoc_thay`, `chu_ky_hai_ben_da_doi`;
- đo: `sub_be_mat`, `web_be_mat`, `sub_sach`, `web_sach`, `leipzig`, `tatoeba`, `F`, `G`, `T`, `diem`, `hang_lich_su`, `vao_lich_su`;
- provenance: nguồn pool/đề cử/H3, `gloss_sha256`, `d6_token_sha256`, `d6_version`, các cột `*_ref` và dòng nguồn.

**assumed:** giữ ký hiệu `-` cho không áp dụng/chưa có, không đổi thành số 0; ghi rõ trạng thái verified/assumed trong cột nhận định. Điểm/hạng là ảnh chụp lịch sử, không tự xếp lại danh sách chính. Trong Git lưu UTF-8 không BOM, LF; working tree Windows CRLF như TSV hiện có, không cột thiếu, không khoảng trắng thừa.

### 5.3. Đề mục chính xác trong tài liệu

**assumed — thay phần trình bày hiện hành, không sửa nội dung lịch sử quyết định hoặc §10:**

```text
## 11. Danh sách dự phòng (đã phân tích, chưa phát hành)
### 11.1. Trạng thái và phạm vi
### 11.2. Các tầng ưu tiên
### 11.3. Ngăn hạn mức và quy tắc thay thế
### 11.4. Giải nghĩa, chữ ký và việc còn thiếu
### 11.5. Danh sách 205 từ
## 12. Từ có thể cân nhắc (honorable mentions)
### 12.1. Điều kiện đề cử và giới hạn sử dụng
### 12.2. Danh mục và nguyên nhân chưa được chọn
### 12.3. Điều kiện trước khi xét đưa vào danh sách
```

**assumed:** đầu tài liệu và mục lục bỏ trạng thái hiện hành “chưa phân tích”, thay bằng “đã phân loại, chưa phát hành”; cập nhật link đến §11 và thêm §12. Giữ khối 205 từ đầy đủ; §12 có bảng gọn từ/lớp/nhóm/nguyên nhân, số đếm và chi tiết dẫn sang TSV. Không thêm khối `từ|giải nghĩa` mới, không chạy `build_wordlist.py` ở chế độ ghi.

### 5.4. README, manifest và kiểm tương thích

- **assumed — README:** đổi hàng `du-phong.txt`, thêm hai TSV, giải thích tầng ≠ nhãn, F điểm ≠ lớp F, trạng thái nghĩa ≠ quyền thay thế, và ghi lỗi nền Windows/đối chứng LF.
- **assumed — manifest:** giữ `danh_sach`, SHA 205 từ, mọi nguồn và lịch sử D6; đổi `du_phong.trang_thai`; thêm metadata bảng/tầng/168 đã có câu/37 chưa viết; thêm `honorable_mentions` với 200 mục, 117/10/73 và trạng thái `CHUA_PHE_DUYET`. Hash các tệp mới/đổi theo byte LF của Git, không theo CRLF ngẫu nhiên của checkout. Kiểm lại số tệp hồ sơ khi điều phối đưa các đầu ra vào Git.
- **verified — tương thích mã:** giữ nguyên tiêu đề §10 và mọi byte từ tiêu đề đó đến trước §11 thì logic C8 không đổi. Hai TSV ngoài không được checker phát hành đọc; không cần đổi production code/test.
- **assumed — kiểm riêng:** tái lập các assert của `E\classify.py` và kiểm JS `E\verify-analysis.mjs`, rồi kiểm byte bảo vệ, blob LF, D2/D5 trong bộ nhớ. Trước thay thật phải kiểm toàn bộ tập thay, quota, H6/H9, D8 và D6 với đủ tham chiếu; kết quả vòng này không thay công đoạn đó.

## 6. Tiêu chí chấp nhận

| Tiêu chí | Cách kiểm | Trạng thái vòng 1 |
|---|---|---|
| Không đổi ba tệp chính và toàn §10 | So bốn SHA byte trước/sau | **verified đạt** |
| Phủ đủ 205 từ, không bỏ hoặc lặp dòng | So cột từ với `du-phong.txt` | **verified đạt** |
| 100–300 HM, không giao khóa với chính/dự phòng hoặc nhau | Python + JS, kể cả viết hoa đầu | **verified 200; đạt** |
| Không từ ba chữ; H1/H2 số học/H5 bảng/K chặn đúng | Assert từng dòng | **verified đạt** |
| Không suy H3/ngoại lệ/K2 từ im lặng | Nối nguồn lexical hoặc hai chữ ký còn hiệu lực | **verified đạt theo hồ sơ lưu** |
| Mỗi dòng có tầng, ngăn, việc thiếu, số đo và nguồn | Schema/kiểm đủ cột; các cột số thiếu không mang 0 giả | **verified đạt** |
| Mọi kết luận nghĩa/độ quen được hai SA hòa | Review độc lập và xử phản đối có bằng chứng | **assumed chưa đạt chữ ký chung; bước kế tiếp** |
| Không gọi 168 nghĩa là 205 nghĩa hoặc D8 hoàn tất | Nối 168 hash đúng lượt, 37 chưa viết, 0 D8 dự phòng | **verified đạt phân biệt trạng thái** |
| Cổng phát hành không hồi quy | Native lỗi nền được giữ nguyên; blob Git LF cùng checker = 0 lỗi | **verified; không tuyên bố native PASS** |
| Không xuất câu nguồn/định nghĩa hoặc sửa gloss | Đầu ra chỉ chứa nhãn, số, nhận định, hash và pointer | **verified theo thiết kế script và nội dung đã viết** |

## 7. Rủi ro và giảm thiểu

- **verified/assumed:** có ngăn F bão hòa và không có C trong dự phòng; ưu tiên chất lượng cùng lớp khi thay thật, không tự đặt quota mới để sửa kết quả.
- **verified:** R1, H5/H6 bị loại và D6/D7 bị loại là ba nguyên nhân khác nhau. Không khôi phục câu cũ hoặc nâng nhãn để làm danh mục trông “sẵn sàng”.
- **assumed:** số đếm thấp có thể phản ánh thiên lệch kho đối với khẩu ngữ; giữ cả số sạch và bề mặt, giữ đọc kiểm H8, không loại từ quen chỉ vì F thấp.
- **assumed:** sắc thái nhẹ dễ bị quét thành H6.9 quá rộng. C là ưu tiên thấp, không là cờ đỏ mới; mọi phản đối thật phải có nguyên mục, nghĩa cụ thể, nguồn và người phản đối.
- **verified:** thiếu dump tham chiếu D6; chỉ công bố PASS lịch sử được nối đúng token-hash. Không lách D6, không tải/lưu corpus trong đợt phân tích này.
- **verified:** CRLF làm checker lỗi trước thay đổi. Lưu cả log native lẫn đối chứng Git, giữ hash byte riêng; không sửa tệp bảo vệ để có log xanh.
- **assumed:** sửa tiêu đề §11 có thể gãy liên kết cũ; cập nhật mục lục/link hiện hành hoặc thêm anchor tương thích, không đổi §10.
- **verified:** hiệu năng ứng dụng không đổi vì không thay HTML/JS/nguồn phát hành; đo benchmark hoặc thêm kiểm UI mới không phục vụ thay đổi tài liệu này.

## 8. Công sức và phân kỳ

**assumed — ước lượng tương đối, không cam kết thời gian hay chi phí:**

1. **Đã có đầu vào độc lập:** 205 phiếu, 200 đề cử và script/log; không cần đo lại 7.776 từ hoặc tải từ điển.
2. **Hòa phân loại:** hai SA đối chiếu 10 C, cách xử 127 lỗi nghĩa, R1 và những đề cử bên kia khác; bổ sung chứng cứ chỉ cho điểm bất đồng. Không viết nghĩa.
3. **Xuất tài liệu chung:** chốt schema/tầng; cập nhật §11–12, hai TSV, README/manifest ở vị trí đã được chủ cho phép; tránh thêm thư mục docs.
4. **Nghiệm thu tài liệu:** chạy lại kiểm nhỏ, so hash bảo vệ, kiểm link và metadata; điều phối ghi chữ ký, commit. Không push hoặc phát hành trong nhiệm vụ này.

**assumed — để riêng cho lần sau:** 37 lượt viết đầu, bổ sung D8 dự phòng, quyền mở lại các mục đã hết lượt D7, tuyển nguồn mới, xử định dạng checkout Windows lâu dài. Không tự chuyển các việc này thành yêu cầu triển khai.

## 9. Câu hỏi

**verified:** chủ đã chốt phạm vi chỉ phân tích, số HM và không tạo docs; không cần hỏi lại các quyết định đó.

**assumed:** **không có câu hỏi cần chủ hoặc SA supervisor trả lời để hoàn tất vòng phân tích này.** Mười C là nội dung review chéo kỹ thuật, không phải lý do tự bỏ từ hoặc nới chính sách. Nếu hai SA bất đồng về áp dụng H6/H9 sau khi có chứng cứ, mới trình supervisor với hai lập trường; chưa suy diễn một bất đồng chưa xảy ra.

**assumed — điều kiện tương lai, không phải yêu cầu mở ngay:** chỉ khi chủ muốn khôi phục 127 mục nghĩa thì xin phép cụ thể cho giới hạn lượt D7; chỉ khi muốn native checker xanh mà vẫn đang giữ checkout CRLF thì tách quyết định định dạng. Không áp dụng ngoại lệ nào trong báo cáo này.

## 10. Chỉ mục bằng chứng và tái lập

**verified — chạy từ `Q:\tmp\passphrase-tieng-viet`, Python UTF-8, không ngẫu nhiên/không seed:**

```powershell
python -X utf8 -B 'analyzing-tools\ho-so\astra\du-phong-v2\evidence\inventory.py'
python -X utf8 -B 'analyzing-tools\ho-so\astra\du-phong-v2\evidence\classify.py'
python -X utf8 -B 'analyzing-tools\ho-so\astra\du-phong-v2\evidence\verify_analysis.py'
node 'analyzing-tools\ho-so\astra\du-phong-v2\evidence\verify-analysis.mjs'
git --no-pager diff --name-only
git --no-pager ls-files --eol -- 'analyzing-tools\wordlist.txt'
```

**verified — các tệp mới do Astra ghi, đều dưới thư mục được giao:**

| Tệp | Công dụng |
|---|---|
| `round-1-analysis.md` | Báo cáo này; chưa phải kết luận chung |
| `du-phong-phan-loai.tsv` | 205 dòng phân loại và evidence pointer từng cổng |
| `honorable-mentions.tsv` | 200 đề cử, nhóm nguyên nhân, số liệu và điều kiện |
| `E\reserve-judgements.tsv` | 205 nhận định thủ công độc lập; không có câu giải nghĩa mới |
| `E\honorable-r1-picks.tsv` | 73 lựa chọn R1 có lý do, không nâng nhãn |
| `E\inventory.py` | Đọc schema, nối số liệu, D6 và chụp hash bảo vệ |
| `E\classify.py` | Kiểm cổng/chữ ký, ghép phiếu, xuất hai bảng và ngăn |
| `E\verify_analysis.py` | Lưu log native, đối chứng LF, D2/D5 trong bộ nhớ, đối D6 hash lịch sử |
| `E\verify-analysis.mjs` | Kiểm khóa/hình thức độc lập bằng JS cho 405 từ |
| `E\inputs.json`, `E\classification-inputs.json` | Hash byte và hash LF của các bảng/tệp được script nối dữ liệu |
| `E\inventory.json` | Các mốc pool, 205/168/37, ngoại lệ, bốn hash bảo vệ |
| `E\classification-summary.json` | Số tầng/ngăn/nguồn và danh sách C |
| `E\reserve-probe.tsv`, `E\candidate-probe.tsv` | Phép nối dữ liệu trước phán đoán; không chứa gloss |
| `E\candidate-exclusions.tsv` | 50 loại cứng cũ, 5 tạm không đề cử, hạ lưu và 4 hồ sơ H3 chưa nối đủ |
| `E\substitution-slots.tsv` | Chứng minh 205 ghế tượng trưng riêng biệt, không phải kế hoạch xóa từ |
| `E\verification.json`, `E\verification.log` | Lệnh đầy đủ, exit code, stdout, giới hạn D6 và đối chiếu byte |

**verified:** nguồn chính để người review bắt đầu là `WordListAnalyze.md:138–153`, `:432–533`, `:719–756`, `:8647–8655`; tiêu chí `AT\tieu-chi-thong-nhat.md:72–214`, `:267–312`, `:399–417`; hồ sơ từ/nghĩa và dòng cụ thể nằm ngay trong hai TSV. Không cần đọc lại văn bản kho hoặc định nghĩa cũ để kiểm các phép đếm, chữ ký, hash và nguyên nhân loại đã ghi.
