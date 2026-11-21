# Phân tích vòng 1 (SA-Opus): 205 từ dự phòng và danh sách đề cử thêm

Người viết: SA-Opus, ngày 20/11/2026. Nhánh `analyze/du-phong-v2`, gốc `cefb993`. Phân tích độc lập, chưa đọc thư mục của SA-Astra. Chỉ đọc dữ liệu trong repo; chỉ ghi trong `analyzing-tools/ho-so/opus/du-phong-v2/`. Không chép câu giải nghĩa, câu kho ngữ liệu hay lời từ điển; chỉ có số đếm, nhãn, hash và lời của Opus.

Kí hiệu: **(V)** đã kiểm bằng dữ liệu hoặc lệnh, có bằng chứng ở mục 10; **(A)** giả định hoặc nhận định, cần SA kia xác nhận.

## 1. Tóm tắt

1. **Khuyến nghị:** giữ nguyên danh sách chính và `du-phong.txt` (205 dòng, SHA không đổi); công bố phân bậc ở một TSV mới và mục 11 viết lại; thêm mục 12 cho đề cử thêm kèm TSV riêng. Không đổi `labels.tsv`, `nguon-goc-giai-nghia.tsv`, `spelling_families.tsv`.
2. **205 dự phòng:** A 151 (111 không-F, 40 F), B 36 (F chưa có nghĩa), C 12 (11 không-F, 1 F), D 6 (không-F). Sau khi bỏ D còn 122 suất thay cho ghế OK không-F và 77 cho ghế F (V; A cho các nhận định "cùng từ").
3. **D (6 từ)** là biến thể khác khóa của cùng một từ theo H5: *hì hụi* (↔ *hì hục* ở danh sách chính), *tròng trành* (↔ *chòng chành* ở danh sách chính), *nhão nhẹt/nhão nhoẹt*, *chọc lét*, *chán phèo*. Quét 6.1 bỏ sót vì chỉ đổi một chỗ, không đổi vần.
4. **Rủi ro chính:** 128 dự phòng không-F rất kém quen: 66/128 dưới bách phân vị 1 điểm F của danh sách chính, mục cao nhất chỉ ở bách phân vị 9 (V). Hai mục chính *hì hục*, *chòng chành* cũng vướng H5c nếu đăng ký họ; danh sách chính không đổi nên chỉ ghi nhận (câu hỏi CH1).
5. **Đề cử thêm: 262 từ, 5 nhóm.** DC1: 132 mục khấu trừ P0 (từ đạt, chỉ vướng D6/D7 của câu, như *ngân hàng, biển, mùa đông*); DC2: 60 R1 phiếu lệch, F ≥ 50; DC3: 46 mục L3b; DC4: 19 mục L2D; DC5: 5 mục HND chưa từng vào rổ.
6. DC1 có độ quen cao hơn hẳn dự phòng (trung vị F 45,6 so với 4,4) nhưng cần chủ dự án cho ngoại lệ D7 (thêm một lượt viết sạch). DC2 cần phân xử lại R1→OK, hoặc được dùng R1 theo hạn mức Q2 (câu hỏi CH3).
7. Hai bộ kiểm vẫn đạt vì không tệp đầu vào nào của chúng đổi; trên working tree Windows (CRLF) chúng báo lỗi C1/C8 giả, phải chạy trên bản LF (V).
8. Câu hỏi (đặt mã CH để khỏi lẫn với hạn mức Q): CH1, CH2, CH4 cho chủ dự án; CH3 cho SA-Fable (mục 9).

## 2. Hiểu yêu cầu

- **Mục tiêu** (V, brief của người điều phối): phân tích và phân loại 205 từ dự phòng ở `WordListAnalyze.md` mục 11; đề xuất khoảng 100–300 từ "đề cử thêm" có thể xem xét đưa vào danh sách sau này.
- **Người dùng:**
  - chủ dự án, cần biết từ nào thay được ngay khi phát hiện lỗi ở danh sách chính;
  - người bảo trì sau này, cần một thủ tục thay từ rõ ràng;
  - người dùng app: không bị ảnh hưởng vì danh sách phát hành không đổi.
- **Ràng buộc** (V):
  - danh sách 7.776 từ không đổi: `index.html`, `thong-tin.html`, `analyzing-tools/wordlist.txt`, mục 10 giữ nguyên từng byte;
  - không lập thư mục tài liệu mới; kết quả cuối ghi vào tài liệu hiện có ở bước báo cáo chung, không phải bây giờ;
  - quyết định 8: không dùng từ 3 chữ, kể cả làm dự phòng (`WordListAnalyze.md:151`);
  - bộ tiêu chí đã ký (H1–H9, Q1–Q4, S1–S5, D1–D8) giữ nguyên; muốn đổi phải mở bản luật mới có hai chữ ký;
  - không lưu văn bản kho, HND, Wiktionary hay giải nghĩa cũ (`analyzing-tools/ho-so/README.md`, mục "Không lưu vào repo").
- **Giả định:**
  - (A) "Đề cử thêm" không phải dự phòng: không có quyền thay từ, chỉ là danh sách xem xét cho đợt sau (thay thế lớn hay bản 2).
  - (A) Dự phòng chỉ dùng khi có lỗi ở danh sách chính; nhu cầu thực tế nhỏ, vì danh sách đã qua D6, D7 và hai bộ kiểm.
  - (V) Danh sách chính không còn mục R1; luật đã ký "dự phòng R1 chỉ thay mục R1" (`WordListAnalyze.md:436`).

## 3. Hiện trạng

### 3.1. Rổ sau kịch bản P0

Rổ P0 = `xep-hang.tsv` (10.133 khóa, sau khấu trừ P7 v1–v2) trừ 132 mục của `p7-v3-khau-tru-132-theo-P0-astra.tsv` = **10.001 khóa** (V).

| Ngăn | Danh sách chính | Dự phòng | Ngoài | Tổng |
|---|---:|---:|---:|---:|
| OK không-F | 7.699 | 128 | 0 | 7.827 |
| OK-F | 77 | 77 | 159 | 313 |
| R1 không-F | 0 | 0 | 1.839 | 1.839 |
| R1-F | 0 | 0 | 22 | 22 |

- OK không-F đã dùng hết (V). Sau 128 dự phòng không-F, theo S4 mục kế tiếp là R1; nhưng luật dự phòng đã ký và tin 119 của Astra ("Không gán R1 cho ghế OK", `trao-doi/119-astra-den-opus.md:7`) không cho R1 thay ghế OK (câu hỏi CH3).
- Hash (V, tính trên nội dung LF của HEAD): `du-phong.txt` `f015e718…` khớp `manifest.json`; cột từ `3609c88f…`; `wordlist.txt` `1d4fc3e8…`; `labels.tsv` `a5b882a8…`.
- Khối mục 11 của tài liệu khớp `du-phong.txt` từng dòng (V).

### 3.2. 205 dự phòng

- **Thành phần** (V):
  - lớp H 85, K 43, F 77; không có mục lớp C (vì C được +15 điểm nên đều đã vào danh sách chính);
  - 197 mục hai khối, 8 mục một khối; 4–12 chữ; không trùng khóa với danh sách chính hay với nhau; không trùng khóa bị chặn;
  - nguồn: 204 L1, 1 L2C (*thụp*).
- **Phiếu P4** (V): 201 mục hai bên cùng OK. Ba mục qua H9, Opus rút phản đối: *hì hụi*, *mụ mị* (V/H5b, so với dạng *hỳ*, *mỵ*) và *làm cỗ* (R2/H3). *thụp* thuộc L2C, phiếu L2 không có trong repo.
- **Chữ ký** (V, `chu-ky.tsv`):
  - 31 mục H3 đủ hai bên (đúng bằng số mục có cảnh báo H3 ở P2);
  - *ăn nhịp*: ngoại lệ H8 (0/0/0/0) đủ hai bên;
  - *hì hụi*, *mụ mị*: H5 đủ hai bên;
  - *làm cỗ*: K2 (*làm cỏ*) đủ hai bên;
  - 6 mục chứng liệu yếu có lượt đọc H8 của Opus;
  - không mục nào còn thiếu chữ ký bắt buộc (H3, ngoại lệ H8, H5, K2).
- **Giải nghĩa:**
  - 168 mục có câu (v1 123, v2 35, v3 10). Cả 168 câu khớp log D6 theo băm token, kết quả PASS và mã lần chạy (V, `kiem-d6-168.log`).
  - Phiếu D7 ở lượt cuối: không có CHAN; 2 NHE (*hì hụi*, *mỏng tanh*); 4 câu `HAI_NGHIA` (*vô tình, chắc, ỉu xìu, sẩy chân*) (V).
  - Chạy lại `kiem-tra-giai-nghia.py --phat-hanh` trên 7.776 câu chính + 168 câu dự phòng: 7.944 dòng, 0 lỗi, 0 cảnh báo (V, `kiem-d5-chinh-va-168.log`).
  - 37 mục chưa có câu, đều lớp F (V).
- **Độ quen** (V, điểm F trong `labels.tsv`):
  - dự phòng không-F: trung vị 4,4, khoảng 0–12,17;
  - danh sách chính không-F: trung vị 42,19; bách phân vị 1 là 4,54, bách phân vị 5 là 9,04;
  - 66/128 dự phòng không-F dưới bách phân vị 1 của danh sách chính, 112/128 dưới bách phân vị 5;
  - điểm S3 khớp đường cắt: mục chính không-F thấp nhất 8,967, dự phòng không-F cao nhất 8,947.
- **H8** (V): 198 mạnh; 6 yếu (*cả nghĩ, cửu chương, lời lỗ, tạnh ráo, thẳng đơ, tối mù*); 1 không có lượt (*ăn nhịp*, có hai chữ ký). Dùng *ăn nhịp* thì M4 = 1 (mục tiêu ≤ 1%).
- **Cặp đảo:** 10 dự phòng là cặp đảo của một mục chính (*cười mỉm/mỉm cười, mong nhớ/nhớ mong*…), đã trừ 5 điểm theo S3. Danh sách chính đã có 117 cặp đảo, nên đây là tiền lệ, không phải lỗi (V).
- **H5, phát hiện mới.**
  - Quét 6.1 chỉ sinh biến thể đổi một chỗ (`WordListAnalyze.md:601`), không đổi vần, không đổi cùng lúc hai âm tiết.
  - Opus quét lại bằng `do-bien-the.py`: đổi âm đầu và âm cuối ở một hay mọi âm tiết, thêm hoặc bỏ âm đệm, đối chiếu với HND và các bảng trong hồ sơ.
  - Các họ tìm được:
    - *hì hụi* ↔ *hì hục* (chính); cả hai có trong HND; đếm sạch 0/0 và 0/3;
    - *tròng trành* ↔ *chòng chành* (chính); cả hai có trong HND; 2/1 và 3/6;
    - *nhão nhẹt* ↔ *nhão nhoẹt* (cả hai là dự phòng; HND còn có *nhão nhét*, *nhão nhoét* cùng khóa); 9/0 và 6/1;
    - *chọc lét* ↔ *thọc lét, chọc léc, thọc léc* (cả ba có trong HND, chưa đếm); *chọc lét* 5/0;
    - *chán phèo* ↔ *chán phè* (HND 22K, chưa đếm); *chán phèo* 20/0;
    - *loằng ngoằng* ↔ *loằn ngoằn* (chỉ có ở HND 74K, chưa đếm).
  - Thành viên HND và số đếm là (V); việc hai dạng là "cùng một từ" là (A).
  - Theo H5c (`tieu-chi-thong-nhat.md:124`), cặp cạnh tranh chỉ nhận dạng chiếm ≥ 95% ở cả hai kho, mỗi kho ≥ 20 lượt, và không bao giờ nhận cả hai. Các họ trên đều thiếu dữ liệu, nên mục dự phòng không thể đạt.
- **Dễ lẫn khác khóa** (V có mặt, A mức độ): *lỗi hẹn* ↔ *lỡ hẹn* (chính, 23/3); *trở lên* ↔ *trở nên* (chính, chỉ khác l/n).
- **H7** (V):
  - không khóa nào bị chặn;
  - còi P2 duy nhất là *phất phơ* (*phật phờ*, 0 PPM);
  - đã đọc 44 mục có mục HND khác cùng khóa; không mục nào là nhóm đỏ trên mốc còi. Ví dụ *vậy nên* ↔ *vảy nến*: PPM gộp 0,25, dưới mốc 0,3.
- **H6** (A, đọc của Opus): không mục nào thuộc nhóm đỏ, không mục nào là tên riêng; nghĩa thứ hai của 4 câu `HAI_NGHIA` đều lành và cờ đã đóng ở D7 (V).
  - Đã xét kỹ *ăn trầu* (nhóm 7: tục truyền thống, không phải thuốc lá hay chất gây nghiện), *đầy tháng, đầy năm, làm cỗ* (nhóm 4: dịp mừng hay nấu cỗ).
  - Các từ chê nhẹ như *giở quẻ, giở giọng, chấp nhặt* có tiền lệ ở danh sách chính (*khó tính, cằn nhằn, cau có, đổi giọng*).

### 3.3. Nguồn cho đề cử thêm

| Nguồn | Số khóa | Tình trạng | Dùng cho |
|---|---:|---|---|
| Khấu trừ P0 | 132 (127 chính, 5 dự phòng) | Từ đạt H1–H9 và nhãn OK; câu trượt D6 (122: D6B 85, D6B+D6C 28, D6C 9) hoặc D7 (10: KIEN_THUC 6, HEP 4). Đã hết hai lượt viết lại (`tieu-chi-thong-nhat.md:307`) | DC1 |
| R1 không-F trong rổ | 1.839 | 786 phiếu lệch OK/R1, 723 R1+R1, 301 của L2/L3 (repo không có phiếu từng bên), 29 khác. Lệch và F ≥ 50: 195 | DC2 |
| L3b, L2D | 48, 99 | Chuẩn bị, chưa chấm, không vào pool (`WordListAnalyze.md:471`) | DC3, DC4 |
| OK-F ngoài rổ dự phòng | 159 | Chỉ thay được ghế F; Q3 đã đủ 77 | Không đề cử |
| LOAI khác trong D8 | 50 | Trượt H5, H6, K0 hay H9 ở cấp từ | Không đề cử |
| Chưa từng vào rổ | 129 từ Opus tự nghĩ, không thấy ở đâu | 25 có trong HND; phần lớn trượt H2 (3 chữ), H4 hay H5a; giữ 5 | DC5 |

Mọi số trong bảng là (V), xem mục 10.

### 3.4. Bộ kiểm và quy ước tệp

- `check_wordlist.py` đọc `wordlist.txt`, `labels.tsv` (dòng CHINH, cột `chu_ky_hai_ben`), `blocked_keys.tsv`, `spelling_families.tsv` và ba khối. `verify.mjs` đọc `blocked_keys.tsv` và ba khối. Cả hai tìm khối mục 10 bằng tiêu đề `## 10. Danh sách 7.776 từ phát hành` và khối ```` ```text ```` đầu tiên sau đó; `build_wordlist.py` cũng vậy (V, đọc mã).
- Working tree dùng CRLF (`core.autocrlf=true`), còn index dùng LF.
  - Chạy trực tiếp trên working tree: `check_wordlist.py` báo C1 (có CR); `verify.mjs` báo C1 và C8 (V).
  - Trên bản LF xuất bằng `git show HEAD:`, cả hai báo 0 lỗi; `build_wordlist.py --check` khớp (V, `chay-bo-kiem-lf.log`).
- TSV trong repo: UTF-8 không BOM, có tiêu đề, LF trong index và CRLF ở working tree. Hash trong `manifest.json` tính trên nội dung LF (V: hash `du-phong.txt`).

## 4. Phương án

**Tài liệu và tệp dữ liệu:**

| | Phương án | Chi phí | Rủi ro | Ảnh hưởng người dùng |
|---|---|---|---|---|
| **PA1 (khuyến nghị)** | Giữ `du-phong.txt` (205 dòng). Thêm `analyzing-tools/du-phong-phan-loai.tsv` và `analyzing-tools/de-cu-them.tsv`. Viết lại mục 11, thêm mục 12. Cập nhật README, manifest. Không đổi `labels.tsv`, `nguon-goc-giai-nghia.tsv`, `spelling_families.tsv` | Thấp | Thấp: không tệp nào bộ kiểm đọc bị đổi | Không có; tài liệu rõ hơn |
| PA2 | PA1, thêm bỏ 6 mục D khỏi `du-phong.txt` (còn 199 dòng) | Thấp | Đổi con số 205 ghi trong quyết định 10, đổi SHA, phải sửa mọi chỗ nhắc 205 | Không có |
| PA3 | Ghi bậc vào `labels.tsv` (thêm cột hoặc trạng thái mới) | Trung bình | Đụng tệp bộ kiểm đọc; trộn nhãn đã ký với nhận định mới | Không có |
| PA4 | Ghi 168 câu dự phòng vào D8 (`nguon-goc-giai-nghia.tsv`, trạng thái mới) | Trung bình | Đổi nghĩa của D8 (hiện chỉ PHAT_HANH và LOAI). Chưa cần, vì mục được dùng thì mới thêm dòng D8 | Không có |

**Độ rộng đề cử thêm:**

- ĐC-a: chỉ DC1 (132).
- **ĐC-b (khuyến nghị): DC1–DC5 (262)**, nằm trong khoảng 100–300 chủ dự án nêu.
- ĐC-c: ĐC-b thêm khoảng 120 cụm đời thường chưa đủ chứng cứ (*nước mía, rèm cửa, trạm xăng*…). Vượt 300; chưa có H3 và chưa có số đếm, nên chỉ lưu ở hồ sơ, không đề cử.

**Thứ tự dùng dự phòng:**

- TT1: giữ thứ tự S4 trong từng ngăn, chỉ bỏ D (cần biên bản khấu trừ H5 hai chữ ký).
- **TT2 (khuyến nghị): TT1, thêm luật v1.1 "bậc C dùng sau bậc A, B cùng ngăn"**, có hai SA ký. Bậc C không bị loại, chỉ đứng sau.

## 5. Kế hoạch đề xuất

### 5.1. Định nghĩa bậc

Xét theo thứ tự D, rồi C, rồi B, rồi A.

| Bậc | Tên | Điều kiện | Còn thiếu khi dùng |
|---|---|---|---|
| D | Không dùng | Biến thể khác khóa của cùng một từ (H5c): một dạng đã ở danh sách chính, hoặc cả họ thiếu dữ liệu nên mục không thể đạt | Biên bản khấu trừ H5 có hai chữ ký |
| C | Yếu | H8 yếu hoặc không có lượt, hoặc tổng chứng liệu (phụ đề + web sạch + Leipzig + Tatoeba) ≤ 3; hoặc dễ lẫn khác khóa với một mục chính; hoặc gần nghĩa với một dự phòng mạnh hơn; hoặc có họ chính tả chưa đo | Như A hoặc B; với họ chưa đo phải đăng ký và đo trước |
| B | Cần nghĩa | Không vướng điều kiện D, C nhưng chưa có câu giải nghĩa | Lượt viết sạch (D1), D6 theo P0, D7; sau đó như A |
| A | Sẵn sàng thay | Có câu đạt D6 (P0) và D7, H8 mạnh, không vướng điều kiện nào ở trên | Chạy lại P6 (ngăn, hạng); thêm dòng D8; đổi trạng thái trong `labels.tsv`; `--phat-hanh` toàn bộ; hai bộ kiểm |

### 5.2. Kết quả phân bậc

Tệp: [`du-phong-205-phan-loai-opus.tsv`](du-phong-205-phan-loai-opus.tsv) (205 dòng, cùng thứ tự O1 với `du-phong.txt`).

| Ngăn | A | B | C | D | Tổng |
|---|---:|---:|---:|---:|---:|
| OK không-F (H, K) | 111 | 0 | 11 | 6 | 128 |
| OK-F | 40 | 36 | 1 | 0 | 77 |
| **Tổng** | **151** | **36** | **12** | **6** | **205** |

**D (6):**

| Từ | Lý do | Xác minh |
|---|---|---|
| *hì hụi* | Biến thể của *hì hục* (chính), khác khóa; không bao giờ nhận cả hai | V số đếm, HND; A cùng từ |
| *tròng trành* | Biến thể của *chòng chành* (chính), đổi tr/ch ở hai âm tiết | V; A cùng từ |
| *nhão nhẹt*, *nhão nhoẹt* | Cùng từ, khác khóa. Không dạng nào chiếm ≥ 95%: phụ đề 9 so với 6 (thêm 5 của *nhão nhoét* cùng khóa), web 0 so với 1 (thêm 1); web cả họ dưới 20 lượt | V; A cùng từ |
| *chọc lét* | Họ *thọc lét, chọc léc, thọc léc* (đều có trong HND); *chọc lét* 0 lượt web, không thể đạt 95% với ≥ 20 lượt | V; A cùng từ |
| *chán phèo* | Họ *chán phè* (HND 22K); 0 lượt web | V; A cùng từ |

**C (12):**

- chứng liệu yếu: *ăn nhịp* (0/0/0/0, ngoại lệ H8 hai chữ ký), *cả nghĩ, cửu chương, tạnh ráo, thẳng đơ, tối mù, chễm chệ*;
- gần nghĩa với một dự phòng mạnh hơn: *lời lỗ* (chọn *lỗ lãi*), *mỏng tanh* (chọn *mỏng dính*);
- dễ lẫn với mục chính: *lỗi hẹn* (*lỡ hẹn*), *trở lên* (*trở nên*, F, chưa có nghĩa);
- họ chưa đo: *loằng ngoằng* (*loằn ngoằn*).

**B (36, đều F):** *bất chấp, biết bao, biết đâu, chút, coi như, cùng lúc, dần dần, dĩ nhiên, đáng lẽ, đến cùng, đôi lúc, giá mà, hàng loạt, ít khi, khắp, không ngờ, không những, làm ơn, lần lượt, lẽ ra, miễn là, mọi khi, nhân dịp, nhìn chung, phải chăng, quá mức, quanh, suốt, thật ra, thế mà, thế thì, ước gì, vậy mà, vậy nên, vừa rồi, y như*.

**A (151):** 111 mục không-F và 40 mục F, xem cột `bac` của TSV. Theo thứ tự dùng:

- 10 mục không-F đầu: *mụ mị, cờ vây, đưa đò, buồn thiu, xuống cân, phất phơ, tấn tới, leo dây, cụt hứng, nín thinh*;
- 10 mục F đầu: *một khi, ngược lại, nghe nói, chẳng hạn, có điều, nếu như, cho nên, xin chào, đồng thời, vừa mới*.

### 5.3. Suất thay

- **Không-F (A, C; 122 mục):**
  - thay một trong 7.699 ghế OK không-F, trừ 14 mục chủ dự án giữ;
  - lớp của ghế bị thay (C, H hay K) không là điều kiện, vì không có hạn mức theo lớp; chỉ báo M1 có thể giảm nhẹ khi thay mục lớp C;
  - chọn theo hạng trong ngăn (S4, cột `hang_trong_ngan_P0`); nếu ký TT2 thì dùng hết A trước C.
- **F (A, B, C; 77 mục):** chỉ thay một trong 77 ghế lớp F (Q3 ≤ 77). 40 mục A đủ cho mọi trường hợp dự kiến, nên chưa cần viết nghĩa cho 36 mục B (CH4).
- **Khi hết 122 suất không-F:** không còn OK không-F nào trong rổ. Phải chọn giữa: dùng R1 theo hạn mức Q2 (CH3 hỏi SA-Fable); phân xử lại một mục DC2 thành OK; hoặc chủ dự án mở lại DC1.

### 5.4. Đề cử thêm

Tệp: [`de-cu-them-opus.tsv`](de-cu-them-opus.tsv) (262 dòng). Định nghĩa đề xuất: *từ có thể xét đưa vào danh sách ở đợt sau; không phải dự phòng, không có suất thay*.

| Nhóm | Số | Ưu tiên | Cách chọn | Điều kiện để xét |
|---|---:|---|---|---|
| DC1 | 132 | 1 (124 mục không-F từng ở danh sách chính); 2 (5 mục F và 3 mục từng là dự phòng) | Toàn bộ khấu trừ P0. Trung vị F của mục không-F 45,6 | Chủ dự án cho ngoại lệ D7 (thêm một lượt viết sạch), D6 theo P0, D7, chạy lại P6 |
| DC2 | 60 | 2 | R1 không-F của L1, phiếu lệch OK/R1, F ≥ 50; bỏ mục kề nhóm đỏ hay quá chuyên môn (mã CT, PL, QS, YT, TG, TC, KT, NC, H5 trong `lap-de-cu.py`); lấy 60 mục điểm S3 cao nhất. Trung vị F 62,5 | Hai bên phân xử lại R1→OK và ký (luật gộp P4, `tieu-chi-thong-nhat.md:384`), hoặc theo kết quả CH3; viết nghĩa sạch, D6, D7 |
| DC3 | 46 | 2 | L3b trừ *chạy nước rút* (H2: cụm động từ ba khối) và *cồn cát* (nghi K1, khóa `concat`). *ớt đỏ*, *nắng ấm* cần xét X | P2, P4, H9, P5; viết nghĩa sạch |
| DC4 | 19 | 3 | L2D đời thường có tổng chứng liệu ≥ 5, hoặc tên vật ba khối rõ | Đọc ngữ cảnh (H8 yếu); một số cần H3 hai xác nhận; P2, P4, H9 |
| DC5 | 5 | 3 | Chưa từng vào rổ, có trong HND: *cặp lồng, chè đỗ đen, sao mai, sao hôm, vịt bầu* | Đếm bốn kho, P2, P4, H9 |

- **Kiểm tự động trên cả 262 mục** (V, `kiem-dau-ra.py`): 4–12 chữ, 1–3 khối; không trùng khóa với danh sách chính, dự phòng hay với nhau; không trùng khóa bị chặn; không thuộc họ chính tả LOAI hay CHO.
- **Ghi chú H5, H7 đáng lưu ý** (V số đo):
  - *bao tử*: khóa `baotu` trùng *báo tử*, PPM gộp 0,385, trên mốc còi, nhưng không có trong `canh-bao-khong-dau.tsv`. Còi P1 có thể đã sót; phải đọc K1/K2 trước khi xét.
  - *tần số* ↔ *tận số*: 0,21, dưới mốc còi.
  - *chạng vạng* có dạng *choạng vạng* trong HND, chưa đếm.
- **H6 của DC3–DC5 chưa chấm** (A).

### 5.5. Tệp dữ liệu cuối (đề xuất cho bước báo cáo chung)

Cả hai tệp sinh bằng script từ bảng của hai SA đã đối chiếu. UTF-8 không BOM, có tiêu đề, LF trong index, theo O1 hoặc theo nhóm. Không chứa câu giải nghĩa.

**`analyzing-tools/du-phong-phan-loai.tsv`** (205 dòng, cùng thứ tự `du-phong.txt`):

`tu, khoa, lop, ngan, hang_trong_ngan, bac, ma_van_de, ghi_chu, con_thieu, giai_nghia, luot_viet, sha256_giai_nghia, F, H8`

- `ngan`: OK_KHONG_F hoặc OK_F.
- `bac`: A, B, C hoặc D.
- `ma_van_de`: H5_BIEN_THE_CHINH, H5_HO_MOI_THIEU_DU_LIEU, H5_HO_CHUA_DO, DE_LAN_CHINH, GAN_NGHIA_DU_PHONG, CHUNG_LIEU_YEU (nhiều mã nối bằng `;`).
- `giai_nghia`: CO hoặc CHUA_VIET.
- `sha256_giai_nghia`: băm câu (UTF-8), cùng cách băm với D8. Câu nằm ở `ho-so/unified/p7-v4-du-phong-168-co-nghia-cho-duyet.tsv`.

**`analyzing-tools/de-cu-them.tsv`** (262 dòng):

`tu, khoa, nhom, uu_tien, lop, nhan, ngan_du_kien, F, H8, ly_do_chua_chon, dieu_kien_de_xet, ghi_chu`

- Không có câu giải nghĩa, không có lời từ điển.

### 5.6. Tài liệu (tiêu đề chính xác)

**`WordListAnalyze.md`:**

- **Đầu tài liệu:**
  - thay gạch đầu dòng "Dự phòng" bằng: *205 từ, đã phân bậc ngày …: A 151, B 36, C 12, D 6*, link tới mục 11 và hai tệp TSV;
  - thêm gạch "Đề cử thêm: 262 từ, không phải dự phòng" (link mục 12).
- **Mục lục:**
  - `11. [Danh sách dự phòng (đã phân bậc)](#11-danh-sách-dự-phòng-đã-phân-bậc)`;
  - `12. [Danh sách đề cử thêm](#12-danh-sách-đề-cử-thêm)`.
- **Mục 1:** thêm dòng "Sau P8 | Phân tích dự phòng và đề cử thêm | Xong | …".
- **Mục 3:** thêm quyết định 11 (20/11/2026): phân tích, phân loại 205 dự phòng; lập khoảng 100–300 đề cử thêm; danh sách chính không đổi; ghi vào tài liệu hiện có.
- **`## 11. Danh sách dự phòng (đã phân bậc)`:**
  - `### 11.1. Trạng thái và cách dùng`;
  - `### 11.2. Định nghĩa bậc` (bảng 5.1);
  - `### 11.3. Kết quả theo ngăn` (bảng 5.2);
  - `### 11.4. Danh sách theo bậc`: D, C có lý do; B, A dạng liệt kê; mỗi từ đúng một lần, hợp lại đúng 205 từ của `du-phong.txt`. Không lặp khối 205 từ nữa;
  - `### 11.5. Phát hiện khi rà lại`: H5 (gồm hai mục chính, không sửa), độ quen, còi H7 của *bao tử*.
- **`## 12. Danh sách đề cử thêm`:**
  - `### 12.1. Định nghĩa và điều kiện`;
  - `### 12.2. Năm nhóm` (bảng 5.4);
  - `### 12.3. Danh sách theo nhóm`.
- **Giữ nguyên:** mục 9 (hồ sơ lịch sử); mục 10 không đổi một byte.
- **Link cũ:** sửa link `#11-danh-sách-dự-phòng-chưa-phân-tích` ở dòng 9.

**`analyzing-tools/README.md`:**

- sửa dòng `du-phong.txt` của bảng Tệp;
- thêm hai dòng cho hai TSV;
- thêm mục `## Dự phòng và đề cử thêm` (bậc, thứ tự dùng, thủ tục thay một từ);
- câu cuối của mục "Cập nhật danh sách" nhắc thứ tự A → C.

**`analyzing-tools/manifest.json`:**

- `du_phong`: `trang_thai` thành "dự phòng, đã phân bậc"; thêm `bac` {A, B, C, D} và `phan_loai_tsv_sha256`;
- thêm khối `de_cu_them`: `so_tu`, `nhom`, `tsv_sha256`, `ghi_chu` ("không phải dự phòng");
- `tep`: thêm hai TSV, cập nhật hash `README.md`;
- `ho_so.so_tep`: đếm lại khi thêm hai thư mục `du-phong-v2`.

Mọi hash tính trên nội dung LF.

**Không đổi:**

- `du-phong.txt` (PA1), `labels.tsv`, `nguon-goc-giai-nghia.tsv`, `blocked_keys.tsv`;
- `spelling_families.tsv`: chưa thêm họ mới. Hai họ chạm mục chính (*hì hục*, *chòng chành*): ghi LOAI hay CHO thì `check_wordlist.py` C5 báo lỗi (khối C5 của script). Ba họ còn lại chỉ chạm dự phòng nên thêm được, nhưng đề nghị ghi cả năm họ ở TSV phân bậc trước, chờ CH1.

### 5.7. Script và tương thích bộ kiểm

- Script của Opus (mục 10) chạy lại được bằng `python chay-tat-ca.py`; phần HND cần tải bốn tệp Viet11K–74K theo `manifest.json` vào `evidence/_tam-hnd/` (bản tạm, đã xóa sau khi chạy).
- Bước báo cáo chung nên dùng một script sinh hai TSV cuối từ bảng đã đối chiếu, rồi chạy bản sửa của `kiem-dau-ra.py` trên tệp cuối.
- **Tương thích:**
  - không đổi tệp nào hai bộ kiểm đọc;
  - mục 11, 12 nằm sau mục 10;
  - không lặp chuỗi `## 10. Danh sách 7.776 từ phát hành`;
  - chạy `check_wordlist.py`, `verify.mjs` trên bản LF và `build_wordlist.py --check` trên working tree.

## 6. Tiêu chí nghiệm thu

| # | Tiêu chí | Cách kiểm |
|---|---|---|
| N1 | `index.html`, `thong-tin.html`, `wordlist.txt`, mục 10 không đổi một byte | `git diff --exit-code cefb993 -- index.html thong-tin.html analyzing-tools/wordlist.txt`; `check_wordlist.py` C8 |
| N2 | Hai bộ kiểm 0 lỗi; ba khối khớp | `chay-bo-kiem-lf.py` (bản LF của commit cuối); `python build_wordlist.py --check` |
| N3 | `du-phong.txt` giữ SHA `f015e718…` (PA1) | băm nội dung LF |
| N4 | TSV phân bậc: 205 dòng, cột `tu` trùng `du-phong.txt` theo thứ tự; `bac` ∈ {A, B, C, D}; số đếm theo ngăn khớp bảng mục 11.3; mọi mục A có câu, và băm token khớp log D6 PASS | `kiem-dau-ra.py`, `kiem-d6-168.py` |
| N5 | TSV đề cử: 100–300 dòng; khóa duy nhất, không giao với khóa chính và dự phòng; không trùng khóa bị chặn; 4–12 chữ, 1–3 khối; không thuộc họ LOAI hay CHO; dòng nào cũng có nhóm, lý do, điều kiện | `kiem-dau-ra.py` |
| N6 | Không tệp mới nào chứa câu giải nghĩa (7.944 câu), câu kho hay danh sách HND | `kiem-dau-ra.py` (quét câu); kiểm tay tên tệp |
| N7 | Mục 11 liệt kê mỗi từ trong 205 từ đúng một lần; mục 12 khớp TSV đề cử; anchor mục lục chạy | script đối chiếu danh sách trong tài liệu với hai TSV |
| N8 | `manifest.json` hợp lệ; hash của tệp mới và tệp đã đổi bằng SHA-256 nội dung LF | `python -c "import json…"` và băm lại |
| N9 | Tệp: UTF-8 không BOM, CRLF ở working tree, dòng cuối, không khoảng trắng cuối dòng; `git add` không lỗi safecrlf | `kiem-dau-ra.py`; `git add` |
| N10 | D và mọi khác biệt bậc với Astra có hai chữ ký hoặc đã gửi SA-Fable | biên bản ở báo cáo chung |

## 7. Rủi ro và cách giảm

| Rủi ro | Mức | Cách giảm |
|---|---|---|
| Dự phòng không-F kém quen: thay nhiều sẽ hạ chất lượng | Trung bình | Thay theo hạng, A trước C (TT2). Nếu cần thay nhiều, trình chủ dự án mở DC1 (quyết định riêng ở đợt sau) |
| H5 ở danh sách chính (*hì hục, chòng chành*) | Thấp đến trung bình | Không sửa danh sách chính (yêu cầu chủ dự án). Ghi nhận ở 11.5; hỏi CH1 |
| Quét 6.1 không xét đổi vần hay đổi hai chỗ: có thể còn cặp khác trong danh sách chính | Thấp đến trung bình | Ngoài phạm vi; nêu ở 11.5. Quét thô của Opus trên 7.776 mục chính cho 632 cặp (474 mục) có dạng khác khóa đã biết (V, `bien-the-chinh-tho.tsv`), phần lớn là từ khác nghĩa; vài cặp có vẻ cùng từ, ví dụ *xập xình/sập sình* (A). Nếu chủ dự án chọn CH1(b), đọc hết 632 cặp ở đợt sau |
| Còi H7 có thể sót (*bao tử* ↔ *báo tử*) | Thấp | Ghi ở DC1; đợt sau có thể quét lại còi trên danh sách chính |
| Nhận định "cùng một từ" và H6 của DC3–DC5 là (A) | Trung bình | Astra soát chéo; bất đồng gửi SA-Fable |
| DC1 cần ngoại lệ D7; DC2 cần quyết định R1 | Thấp | Ghi rõ điều kiện trong TSV; CH3 |
| Bản quyền: lỡ chép câu giải nghĩa hay HND | Thấp | Chỉ lưu băm, số đếm, đầu mục; `kiem-dau-ra.py` quét câu; HND chỉ tải tạm rồi xóa |
| CRLF và LF: bộ kiểm báo lỗi giả trên Windows | Thấp | Kiểm trên bản LF (`chay-bo-kiem-lf.py`) hoặc trên Linux |
| `manifest.json` lệch hash hay số tệp | Thấp | Sinh lại bằng script ở bước cuối; N8 |

## 8. Công sức và phân đợt

1. **T1, soát chéo** (hai SA): đối chiếu bậc từng mục, danh sách D, nhóm đề cử; ghi bất đồng. Khoảng 1 vòng.
2. **T2, tệp dữ liệu**: script sinh hai TSV cuối và kiểm N4–N6. Nhỏ.
3. **T3, `WordListAnalyze.md`**: đầu tài liệu, mục lục, mục 1, mục 3, mục 11 viết lại, mục 12 mới. Trung bình.
4. **T4, README và manifest**: nhỏ.
5. **T5, nghiệm thu** N1–N10: nhỏ.
6. **Tùy chủ dự án, ngoài đợt này:**
   - lượt viết sạch cho 36 mục B, chỉ khi cần;
   - ngoại lệ D7 cho DC1;
   - quét lại H5 và H7 trên danh sách chính.

## 9. Câu hỏi

| # | Gửi | Câu hỏi | Lựa chọn | Đề nghị của Opus | Căn cứ |
|---|---|---|---|---|---|
| CH1 | Chủ dự án | *hì hục* và *chòng chành* (danh sách chính) có biến thể khác khóa trong HND (*hì hụi*, *tròng trành*). Theo H5c, cả hai dạng đều thiếu dữ liệu. Làm gì với hai mục chính? | (a) chỉ ghi nhận ở 11.5, không đổi gì; (b) ghi nhận, mở việc rà riêng ở đợt sau; (c) thay ngay bằng dự phòng (trái yêu cầu "không đổi danh sách chính") | (b) | 3.2; `bien-the-du-phong-205.tsv`; `bien-the-hnd.tsv` |
| CH2 | Chủ dự án | Giữ `du-phong.txt` 205 dòng (bậc ở TSV riêng) hay bỏ 6 mục D (còn 199)? | (a) giữ 205; (b) bỏ D | (a): không đổi con số và SHA ghi trong quyết định 10; D đã bị chặn bằng bậc | 4, PA1/PA2 |
| CH3 | SA-Fable | Khi hết 122 suất OK không-F, R1 có được vào ghế OK không-F theo hạn mức Q2 (R1 ≤ 388, "chỉ lấy khi đã hết ứng viên OK") không, hay luật "dự phòng R1 chỉ thay mục R1" và tin 119 của Astra cấm? | (a) cấm, R1 phải được phân xử lại thành OK; (b) cho theo Q2 | (a), tức đọc chặt; chỉ ảnh hưởng điều kiện của DC2 | `WordListAnalyze.md:212`, `:436`; `trao-doi/119-astra-den-opus.md:7` |
| CH4 | Chủ dự án | Có viết nghĩa ngay cho 36 mục B (chi phí một lượt viết sạch cùng D6, D7) không? | (a) chưa, chỉ viết khi cần; (b) viết ngay | (a): 40 mục F bậc A đã đủ cho 77 ghế F | 5.3 |

## 10. Chỉ mục bằng chứng

**Thư mục:** `analyzing-tools/ho-so/opus/du-phong-v2/`.

- **Đầu ra chính:** `round-1-analysis.md` (tài liệu này), `du-phong-205-phan-loai-opus.tsv` (205 dòng), `de-cu-them-opus.tsv` (262 dòng).
- **Script** (trong `evidence/`):
  - `chung.py`: hàm chung (khóa, O1, đọc và ghi TSV, H8);
  - `thu-thap-du-phong.py` → `du-phong-205-su-kien.tsv`;
  - `do-bien-the.py` → `bien-the-du-phong-205.tsv`, `bien-the-de-cu.tsv`, `bien-the-chinh-tho.tsv` (quét thô 7.776 mục chính, chưa đọc);
  - `kiem-hnd.py` → `du-phong-205-hnd.tsv`, `de-cu-hnd.tsv`, `chua-vao-ro-hnd.tsv`, `bien-the-hnd.tsv`;
  - `phan-loai-du-phong.py` → `../du-phong-205-phan-loai-opus.tsv`;
  - `tra-tu.py` → `tra-tu-doi-thuong-1.tsv`, `tra-tu-doi-thuong-2.tsv` (đầu vào là hai danh sách Opus tự nghĩ: `tu-doi-thuong-tu-nghi*.txt`);
  - `lap-de-cu.py` → `de-cu-ung-vien.tsv` (cả mục bị loại, cột `loai_vi`), `de-cu-giu.txt`;
  - `xuat-de-cu.py` → `../de-cu-them-opus.tsv`;
  - kiểm: `kiem-d6-168.py`, `kiem-d5-chinh-va-168.py`, `chay-bo-kiem-lf.py`, `kiem-dau-ra.py`;
  - chạy tất cả: `chay-tat-ca.py`.
- **Log:**
  - `kiem-d6-168.log`: 168/168 câu khớp băm token, PASS và mã lần chạy;
  - `kiem-d5-chinh-va-168.log`: 7.944 dòng, 0 lỗi, 0 cảnh báo;
  - `chay-bo-kiem-lf.log`: `check_wordlist.py` 0 lỗi, `verify.mjs` 0 lỗi trên HEAD dạng LF.
- **Lệnh** (PowerShell, từ thư mục `evidence/`):
  - tải HND tạm: `curl.exe -sSL -o _tam-hnd/Viet74K.txt https://raw.githubusercontent.com/duyet/vietnamese-wordlist/688b0953c8cdb21ee090ce80b83cefdb052fe2cd/Viet74K.txt`, tương tự cho 11K, 22K, 39K. `kiem-hnd.py` kiểm SHA-256 theo `manifest.json` (đã khớp cả bốn);
  - chạy: `python chay-tat-ca.py`; xóa `_tam-hnd/` sau khi chạy.
- **Đầu vào** (đều trong repo, commit `cefb993`):
  - `analyzing-tools/`: `du-phong.txt`, `wordlist.txt`, `labels.tsv`, `blocked_keys.tsv`, `spelling_families.tsv`, `d6-ho-chinh-ta.tsv`, `nguon-goc-giai-nghia.tsv`;
  - `ho-so/unified/`: `xep-hang.tsv`, `p6-dau-vao.tsv`, `l2*-nhan-sau-H9-opus.tsv`, `l2*-ung-vien.tsv`, `l3-*.tsv`, `l2d-ung-vien.tsv`, `l3b-de-cu-opus.tsv`, `opus-counts.tsv`, `phieu-opus.tsv`, `phieu-astra.tsv`, `phan-bien.tsv`, `chu-ky.tsv`, `canh-bao-khong-dau.tsv`, `cong-opus-v4.tsv`, `p7-v3-khau-tru-132-theo-P0-astra.tsv`, `p7-v4-kiem-ke-D8-chua-chot-astra.tsv`, `p7-v4-du-phong-168-co-nghia-cho-duyet.tsv`, `p7-v3-c13-hoa-astra-tu-chua-viet.tsv`, `d6-log-v1..v3.tsv`, `soat-nghia-*.tsv`, `dong-co-*.tsv`;
  - `ho-so/discussion/bang-khoa-chung.tsv`.
- **Mẫu số H8:** 34.314.528 âm tiết phụ đề và 149.860.716 âm tiết web (`tieu-chi-thong-nhat.md`, mục 0). L2D dùng mẫu số web khác, nên *bánh củ cải* (15 lượt web) là ca sát mốc.
- **Trích dẫn luật:**
  - `WordListAnalyze.md`: `:151` (quyết định 8), `:153` (quyết định 10), `:212`, `:213` (Q2, Q3), `:255` (D7), `:436` (luật dự phòng), `:471` (L3b, L2D), `:601` (quét 6.1), `:8647–8863` (mục 11);
  - `tieu-chi-thong-nhat.md`: `:124` (H5c), `:135` (họ do người duyệt đăng ký), `:160` (còi H7), `:174` (H8), `:307` (D7), `:384` (gộp nhãn P4).
