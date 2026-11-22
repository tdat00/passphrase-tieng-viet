# T9 — soát toàn tập sau khi thay (SA-Opus)

Ngày soát: 22/11/2026. Đối tượng: working tree trên `d78e97a` (danh sách mới chưa commit). Không sửa tệp phát hành.

**Kết luận: T9 chưa đạt.**

- Còn 14 cặp cùng khóa cần phán quyết chung: 13 K2 (Opus đã ký "không tự động chặn") và 1 không đỏ. Một cặp, *đuôi*/*đượi*, có thể phải trình chủ dự án nếu Astra xếp K0.
- Không có K1 mới, nên nếu Astra đồng ý thì không phải thay thêm từ.
- Soát dữ liệu (T2, T3, T4, T6, T8, T11, T12) và mục 13 của `WordListAnalyze.md` đều đạt.

`OE` = `ho-so/opus/ra-thay-chinh/evidence/`; `TC` = `tieu-chi-thong-nhat.md`.

## 1. Cách làm

**Danh sách (verified):**

- 7.776 từ, 7.776 khóa, khóa ngắn nhất 4 chữ;
- tập ra đúng 116 dòng RA;
- tập vào gồm 115 từ VAO (không có *sớm tối*) và *cả nghĩ*.

**Nguồn cách đọc cùng khóa** (đều khớp băm trong `manifest.json`, để ngoài repo, đã xóa sau khi dùng; trừ bản Kaikki-vi ghim):

- DOC_KHAC của `opus-counts.tsv`;
- bốn danh sách HND;
- Kaikki viwiktionary (`1f0abd…`), chỉ mục `lang_code` = vi. Bản trích này còn chứa mục tiếng Anh, Pháp; lượt chạy đầu bị lẫn các mục đó và đã sửa;
- Kaikki enwiktionary tiếng Việt (`186cd0…`).

**Quét** (`OE/t9-soat.py`, `.tsv`, `.log`):

- 3.463 cặp cùng khóa. 1.288 cặp cần xét vì có cờ đỏ (từ khóa nhóm đỏ, nhãn Kaikki), có còi số, thuộc từ vào, hoặc nằm trong bảng phán quyết T9.
- 1.210 cặp đã có phán quyết từ trước: hai phiếu sàng lọc vòng 1, `ra-thay-chinh-h7.tsv`, `canh-bao-khong-dau.tsv`, `chu-ky.tsv`, cờ từ vào.
- 78 cặp nay có phán quyết T9 của Opus (`OE/t9-phan-quyet.tsv`, 84 dòng).

**Đọc tay** toàn bộ đầu mục chỉ có ở Kaikki, không có ở DOC_KHAC hay HND: 172 mục ở Kaikki-vi, 126 mục ở Kaikki-en. Vòng 1 không quét nguồn này, dù H7 so với mọi mục của Wiktionary (TC:158) và T9 ghi rõ đầu mục Kaikki.

**Đếm** 38 cặp trên hai kho ghim (băm khớp manifest), theo cách của `count_corpus.py`, mẫu số lấy theo manifest (`OE/t9-dem.py`, `.tsv`). Đã đếm riêng *liêng* sau khi bỏ *thiêng liêng*.

**Luật:**

- Còi: TC:160. Cách đọc thuộc nhóm đỏ và có PPM ≥ 0,3 hoặc ≥ PPM của từ chính. Tự hại, bạo lực, tình dục rõ xét cả dưới mốc.
- K0: TC:161–164.
- K1, K2: luật chung đã thống nhất. K1 khi nghĩa chính đỏ nặng và tỉ lệ ≥ 0,035; nhẹ hay hiếm thì K2.

## 2. Cách đọc cần phán quyết chung

PPM là PPM gộp của cách đọc / của từ chính.

| Từ | Cách đọc | Nhóm | PPM | Opus | Ghi chú |
|---|---|---|---|---|---|
| *đuôi* | *đượi* | K0? | 0,131 / 35,7 | K2 | Nói lái của *đĩ*, chỉ có ở viwiktionary; 9 lượt phụ đề, nghi gõ sai *được*. Theo tiền lệ *bình*/*bĩnh* (`chu-ky.tsv:134–135`). Astra giữ K0 thì trình chủ dự án (TC:164) |
| *đon đả* (từ vào) | *đòn đá* | G1 | 0,018 / 0,015 | K2 | Tên đòn võ, cụm ghép; 1+1 lượt, nên tỉ lệ không có ý nghĩa. Khác *đấm đá* (K1) |
| *tụ tập* | *tu tập* | G4 | 0,58 / 4,89 | K2 | Tu hành, nghĩa nhẹ |
| *song ngữ* | *song ngư* | G4 | 0,54 / 1,84 | K2 | Cung hoàng đạo; tiền lệ *hoàng đạo* |
| *tử tế* | *tư tế* | G4 | 1,85 / 24,9 | K2 | Chức sắc tôn giáo; tỉ lệ 0,074 |
| *chanh* | *chảnh* | G9 | 1,60 / 16,9 | K2 | Lời chê nhẹ; tiền lệ *ngốc, nhãi* |
| *thú dữ* | *thứ dữ* | G1 | 0,44 / 0,56 | K2 | Người khó chơi; số bị thổi phồng bởi *thứ dữ liệu, thứ dữ dội* |
| *tung* | *tửng* | G5 | 0,67 / 61,2 | K2 | Phần lớn là *tưng tửng*; mở rộng K2 sẵn có của `tung` |
| *mằn mặn* | *man man* | G5 | 0,10 / 0,05 | K2 | Số web phần lớn là chữ tiếng Anh |
| *bạn thân* | *bán thần* | G4 | 0,38 / 24,3 | K2 | Mở rộng K2 của `banthan` (D-rtc-7) |
| *cau có* | *cầu cơ* | G4 | 2,23 / 0,64 | K2 | Số bị thổi phồng bởi *nhu cầu cơ bản*; tiền lệ *ngải, nguyền* |
| *dài hạn* | *đại hãn* | G3 | 0,73 / 13,9 | K2 | Tước hiệu; tiền lệ *triệu*/*triều*; mở rộng K2 của `daihan` |
| *liễu* | *liêu* | G3 | 4,21 / 15,2 | K2 | Số gồm *quan liêu, liêu xiêu*, họ Liêu |
| *công cộng* | *công công* | — | 2,47 / 50,0 | Không đỏ | Thái giám, bố chồng trong phim; như *hoàng hậu* (TC:145) |

**Đã xét, không cần phán quyết chung (dưới mốc còi, không thuộc tự hại, bạo lực, tình dục rõ, K0; TC:160):** 23 cặp.

- *liệng*/*liêng*: bài liêng chỉ khoảng 5 lượt web; 356/361 lượt phụ đề của *liêng* là *thiêng liêng*.
- *linh dương*/*linh đường*: 1+1 lượt.
- *chứng chỉ*/*chung chi*: 0,22 PPM.
- *hướng dương*/*hưởng dương*: 0+1 lượt.
- *nhân tài*/*nhân tai*: 0,11 PPM.
- *mũ nồi*/*mụ nội*: 2+0 lượt.
- *hóng chuyện*/*hồng chuyên*, và các cặp khác: xem `OE/t9-phan-quyet.tsv`.

**Không đỏ:** 48 cặp gồm tên riêng, biến thể và từ thường, có cả các cặp của từ vào.

## 3. Soát dữ liệu

Kết quả ở `OE/t9-kiem-du-lieu.py`, `.log`; mọi phép kiểm đạt.

- **T2:** đúng 94 khóa mới với đúng mã: K0 `phanbac`, `tinhkhi`, `nieu`; K1 cho 89 khóa, `baotu`, `lamco`. Không khóa phát hành nào bị chặn.
- **T3:**
  - 35 họ mới, khớp từng cặp đã chốt (thay, chờ loại, qua) với đúng kết luận;
  - không từ phát hành nào thuộc họ bị cấm (luật C5);
  - họ thiếu dữ liệu có từ phát hành đều có hai chữ ký H5 (ví dụ *rỉ tai*).
- **T4:**
  - 7.776 dòng CHINH, F = 77, R1 = 0;
  - 246 khóa K2 giữ lại đều có hai người ký hiệu lực;
  - khóa `chia` có đúng hai dòng hiệu lực (hai dòng cũ là THAY_THE).
- **T6:**
  - 7.776 dòng PHAT_HANH, sha256 khớp câu trong `wordlist.txt`;
  - từ vào có lượt rtc-v1 84, rtc-v2 27, rtc-v3 5;
  - 116 từ ra là LOAI (H7_K1 89, H5_c 14, H5_CHO_LOAI 7, H5_f 3, H7_K0 3).
- **T8, T11:**
  - dự phòng 89 dòng, khớp bảng phân loại (41 A, 36 B, 4 C, 8 D) và `labels.tsv`;
  - HM 237 dòng, không HM nào vào chính;
  - băm trong manifest khớp byte working tree.
- **T12:** đạt.

## 4. Mục 13 của `WordListAnalyze.md`

Số liệu khớp dữ liệu:

- 116 ra (3 K0, 89 K1, 24 H5); 116 vào (105 A, 11 C);
- 94 khóa; 35 họ; 238 khóa K2 chung và 5 khóa HM;
- dự phòng 89 (41/36/4/8); 24 HM chưa dùng.

**Sau T9 cần sửa:**

- mục 13.3 và 13.5: thêm số khóa K2 mới, các phạm vi mở rộng, và cách đọc Kaikki đã soát;
- mục 13.7: ghi rằng T9 đã quét cả đầu mục Kaikki.

Gợi ý nhỏ, không chặn: `du-phong-phan-loai.tsv` có thể ghi *sớm tối* đã trượt D7 ở lượt `rtc`.

## 5. Việc cần làm trước commit phát hành

1. **Astra cho ý kiến 14 cặp ở mục 2.** Với cặp cả hai cùng ký K2:
   - thêm hai dòng mỗi khóa vào `chu-ky.tsv`. Với `tung`, `banthan`, `daihan`: đổi dòng cũ sang THAY_THE, như đã làm với `chia`;
   - thêm `K2` vào `chu_ky_hai_ben` trong `labels.tsv`;
   - cập nhật mục 13 và `manifest.json`.
2. ***đuôi*/*đượi*:** nếu Astra giữ K0, trình chủ dự án (TC:164). Nếu chọn K0: chặn `duoi`, thay *đuôi* bằng dự bị *cửu chương* (mục 6.1).
3. **Cặp nào thành K1:** chặn khóa, thay từ theo hàng đợi (*cửu chương*, rồi HM có câu đạt), rồi chạy lại các cổng.
4. **Ghi kết quả T9 vào quyết định** (đề nghị T-rtc-24) khi hai SA khép.

## 6. Chứng cứ

- `OE/t9-soat.py`, `t9-soat.tsv`, `t9-soat.log`;
- `OE/t9-phan-quyet.py`, `t9-phan-quyet.tsv`;
- `OE/t9-dem.py`, `t9-dem.tsv`;
- `OE/t9-kiem-du-lieu.py`, `t9-kiem-du-lieu.log`.

Tệp chỉ có đầu mục, khóa, số đếm và nhận định của Opus. Không chép lời Wiktionary, câu của kho hay danh sách HND.

## 7. Đối đáp với Astra (lượt 1, 22/11/2026)

Bảng hợp nhất phía Opus: `t9-doi-dap.tsv` (76 dòng; script `OE/t9-doi-dap.py`). Đã đối chiếu với dữ liệu: nguồn Kaikki tại đúng dòng Astra dẫn, `chu-ky.tsv`, `labels.tsv`, `WordListAnalyze.md`.

**Nhận của Astra:**

- *phết*/*phẹt* là K0: VI:37654 ghi động từ thô tục chỉ việc thải phân. Khác *bĩnh*, mục không mang nhãn tục.
- *cau có*/*cầu cơ* là K1: số sạch 47/1 vượt cả từ chính.
- *buồn thiu*/*buồn thỉu* và *ỉu xìu*/*ỉu xịu* loại theo H5c, thiếu dữ liệu: từ điển ghi "như …"; dưới 20 lượt.
- *thầy* thừa một dòng ký Opus.
- Hai chỗ sửa ở `WordListAnalyze.md` (dòng 9101: K0; dòng 9124: 237 nhãn K2 mới).
- Phạm vi chữ ký của *bảng* phải gồm *băng*.

**Cùng ký K2:** 57 cặp K2 của Astra.

**Giữ, không cần thay:**

- 5 cặp chỉ Opus nêu: *đượi, song ngư, tửng, man man, liêu*. Astra không phản đối; ký K2 hoặc xếp không đỏ đều giữ từ.
- *công công*: không đỏ.
- *dài ngoẵng*, *lu bu*: khác từ.

**Còn lệch, trình chủ dự án nếu Astra giữ ý:**

- *tụ tập*/*tu tập* và *tử tế*/*tư tế*: Astra xếp K1, Opus xếp K2.
- *cuống*/*cương* và *lông*/*lồng*: chỉ khi Astra chốt K0; Opus xếp K2.

**Thay đã thống nhất: 4 từ** (*phết, cau có, buồn thiu, ỉu xìu*).

- Lấp theo hàng đợi: *cửu chương*, rồi các HM có câu đạt theo thứ tự (*ngân hàng, biển, côn trùng*, …).
- Đổi danh sách mà chủ dự án đã duyệt, nên cần chủ dự án duyệt lại danh sách ra và vào (B1).
