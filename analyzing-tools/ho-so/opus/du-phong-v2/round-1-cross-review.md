# Soát chéo vòng 1 (SA-Opus đọc phân tích của SA-Astra)

Người viết: SA-Opus, ngày 20/11/2026. Đã đọc `analyzing-tools/ho-so/astra/du-phong-v2/` (báo cáo, hai TSV, `evidence/`). Mọi kiểm chứng dưới đây chạy lại trên tệp và script trong repo (commit `cefb993`), không dựa vào lời báo cáo. Không sửa tệp của Astra.

Kí hiệu: **(V)** đã kiểm bằng dữ liệu hay lệnh; **(A)** nhận định cần bên kia xác nhận. Đường dẫn: `AT` = `analyzing-tools`, `U` = `AT/ho-so/unified`, `E` = `AT/ho-so/opus/du-phong-v2/evidence`.

Chứng cứ từ điển trực tuyến (mục 2.1) chỉ ghi quan hệ giữa các đầu mục và mã phiên bản trang, không chép lời định nghĩa. Bốn danh sách HND chỉ tải tạm ra ngoài repo để tra, đã xóa sau khi chạy.

## 1. Điểm đồng ý

**Phạm vi và tệp:**

- Danh sách chính giữ nguyên từng byte; hai bên cùng kiểm được.
- `du-phong.txt` giữ 205 dòng và SHA `f015e718…`.
- Không sửa `labels.tsv`, `nguon-goc-giai-nghia.tsv`.
- Thêm hai TSV mới; viết lại mục 11, thêm mục 12; cập nhật README và manifest với hash tính trên nội dung LF; không lập thư mục tài liệu mới.

**Số liệu** (V, hai bên ra cùng kết quả):

- 205 dự phòng = 128 không-F (H 85, K 43) + 77 F; không có lớp C; 4–12 chữ; không mục ba khối.
- Không trùng khóa với danh sách chính hay với nhau; không trùng khóa bị chặn; *dễ ợt* chỉ vướng họ TRU_DIEM.
- 168 câu khớp log D6 theo băm token (v1 123, v2 35, v3 10). Phiếu D7 lượt cuối không có CHAN, có 2 NHE; 4 câu `HAI_NGHIA`.
- `--phat-hanh` trên 7.944 cặp: 0 lỗi, 0 cảnh báo.
- 37 mục chưa có câu, đều F. Dự phòng không có dòng D8 nào.
- Chữ ký: 31 mục H3 đủ hai bên; *ăn nhịp* H8; *hì hụi, mụ mị* H5; *làm cỗ* K2.
- Rổ P0: 10.001 khóa. Ngoài danh sách chính và dự phòng còn 159 OK-F, 1.839 R1 không-F, 22 R1-F.

**Luật:**

- R1 chỉ thay R1; không đưa R1 vào ghế OK. Lớp F chỉ thay ghế F (Q3 đầy).
- 127 mục khấu trừ D6/D7 đã hết hai lượt viết lại; muốn khôi phục phải có phép của chủ dự án.
- Đề cử thêm không phải dự phòng, không có suất thay.
- 50 mục LOAI do cổng cứng không đề cử.

**Bộ kiểm:**

- Trên working tree CRLF, hai bộ kiểm báo lỗi giả.
- Trên bản LF: `check_wordlist.py` 0 lỗi, `verify.mjs` 0 lỗi; `build_wordlist.py --check` khớp.
- Hai TSV mới không được bộ kiểm nào đọc.

**Đề cử:** 153 mục chung (127 khấu trừ D6/D7 và 26 R1).

**Việc để sau:** không viết nghĩa cho 36–37 mục chưa có câu trong đợt này.

## 2. Điểm bất đồng

Bảng đối chiếu đầy đủ: `E/doi-chieu-du-phong.tsv` (28 từ khác bậc) và `E/doi-chieu-de-cu.tsv` (309 từ thuộc hợp hai tập đề cử). Đề xuất hợp nhất của Opus: `E/du-phong-205-bac-sau-soat-cheo-opus.tsv` và `E/de-cu-hop-nhat-de-xuat-opus.tsv`.

| Bậc Opus vòng 1 → tầng Astra | Số từ |
|---|---:|
| A → A | 141 |
| B → B | 36 |
| A → C | 10 |
| C → A | 11 |
| C → B | 1 |
| D → A | 6 |

### 2.1. Sáu từ D của Opus (Astra: A)

Astra giữ A vì "không tự dựng họ chưa có trong hồ sơ" và "từ gần nghĩa không mặc nhiên là cùng họ". Opus đồng ý rằng cần chứng cứ, nên chia làm hai nhóm.

**Giữ D: có nguồn kiểm được** rằng hai dạng là một từ, hoặc tiền lệ đã ký. Opus nêu đây là phản đối H9, mã H5c.

| Từ | Chứng cứ | Số đếm (phụ đề/web sạch) |
|---|---|---|
| *tròng trành* | en.wiktionary, trang *tròng trành* (oldid 89219050): mục "Alternative forms" ghi *chòng chành*, mục đang ở danh sách chính. Cả hai có trong HND (V) | 2/1 và 3/6: cả họ dưới 20 lượt ở mỗi kho, H5c không nhận dạng nào |
| *chán phèo* | vi.wiktionary (oldid 2366348): chú *chán phèo* là "như *chán phè*", nhãn thông tục, hiếm. *chán phè* có trong HND 22K (V) | *chán phèo* 20/0; web không có lượt nào, nên không thể đạt ≥ 95% ở cả hai kho |
| *chọc lét* | Cùng phép đổi *lét/léc* với họ *cù lét/cù léc* mà hai bên đã đăng ký loại c, kết luận LOAI_CANH_TRANH (`AT/spelling_families.tsv:116`). HND 74K có *chọc léc*. en.wiktionary (oldid 51000637) ghi giọng Sài Gòn đọc *lét* thành [lɛk̚] (V). Không dựa vào *thọc lét*: Wiktionary ghi đó là từ đồng nghĩa | *chọc lét* 5/0; web 0 lượt nên không thể đạt H5c |

**Hạ D → C: "cùng một từ" chỉ là nhận định** (A).

- *hì hụi*: gần nghĩa với *hì hục* (chính). en.wiktionary (oldid 93445969) chỉ ghi dạng khác là *hè hụi*, không nối với *hì hục*.
- *nhão nhẹt*, *nhão nhoẹt*: cùng nghĩa, khác khóa. vi.wiktionary (oldid 2366609) chỉ nối *nhão nhoẹt* với *nhão nhoét* (cùng khóa); *nhão nhẹt* không có trang. Đề nghị dùng tối đa một trong hai.

**Cách xử:**

- Theo H9 (`AT/tieu-chi-thong-nhat.md:180–193`), Astra phản biện một lần ở báo cáo chung; nếu Opus vẫn giữ thì mục không được dùng.
- H5 lại đòi hai bên xác nhận "cùng một từ" mới áp (`AT/tieu-chi-thong-nhat.md:135`). Nếu hai luật được hiểu khác nhau, gửi SA-Fable (CH5).

### 2.2. Bậc C

- **Opus C, Astra A (11):**
  - chứng liệu yếu: *ăn nhịp* (0 lượt), *cả nghĩ, tối mù* (cổng P2 ghi CHI_BE_MAT), *cửu chương, tạnh ráo, thẳng đơ* (YEU), *chễm chệ* (tổng 3), *mỏng tanh* (tổng 2);
  - gần nghĩa với dự phòng mạnh hơn: *lời lỗ* (chọn *lỗ lãi*), *mỏng tanh* (chọn *mỏng dính*);
  - dễ lẫn với mục chính: *lỗi hẹn* (*lỡ hẹn*);
  - họ chưa đo: *loằng ngoằng* (*loằn ngoằn*).
- **Astra C, Opus A (10):** *ăn trầu, bèo bọt, chấp nhặt, giở giọng, giở quẻ, mụ mị, non choẹt, thụp, tía lia, tuổi xanh*. Lý do là sắc thái, độ quen của từ đơn (*thụp*), văn chương (*tuổi xanh*).
- **Đề nghị: lấy hợp hai danh sách.** C chỉ là "dùng sau A cùng ngăn", không loại, nên chi phí gần như bằng không:
  - với hơn 100 mục A không-F, bậc C hầu như không bao giờ đến lượt;
  - Opus nhận cả 10 mục C của Astra.
- **Astra không nhất quán:** Astra hạ *thụp* vì độ quen, dù *thụp* có 10 lượt phụ đề sạch và 4 câu Leipzig. Trong khi đó Astra để A cho *ăn nhịp* (0/0/0/0), *thẳng đơ* (1/0/0/0), *tối mù* (1/0/1/0) và *cả nghĩ* (2/0/0/0) (V, `E/du-phong-205-su-kien.tsv`).
- ***trở lên*** (Opus C, Astra B): chưa có nghĩa, và chỉ khác *trở nên* (chính) ở l/n. Đề nghị C, ghi rõ còn thiếu câu.
- **Kết quả đề xuất** (`E/du-phong-205-bac-sau-soat-cheo-opus.tsv`):
  - A 141 (101 không-F, 40 F); B 36; C 25 (24 không-F, 1 F); D 3;
  - còn 125 suất thay cho ghế OK không-F.

### 2.3. Đề cử thêm

| | Astra (200) | Opus (262) |
|---|---|---|
| Khấu trừ D6/D7 | 127; tạm bỏ 5 mục | 132 |
| R1 | 73: chọn theo chủ đề; gồm 19 mục hai bên cùng chấm R1 và 4 mục L2/L3 | 60: phiếu lệch, F ≥ 50, lấy điểm cao nhất sau khi lọc |
| L3b, L2D, chưa vào rổ | không mở | 46, 19, 5 |
| Chung | 127 + 26 = 153 | |

- **5 mục Astra tạm bỏ** (*cơ quan, lực lượng, truy tìm, dự bị, lên chức*):
  - cả năm được hai bên chấm OK ở P4 và không có phản biện nào (V, `U/phieu-opus.tsv`, `U/phieu-astra.tsv`, `U/phan-bien.tsv`);
  - lượt đọc toàn bộ ở P6 (19 khấu trừ) cũng không nêu chúng;
  - Astra chỉ ghi "assumed, cần rà".
  - Đề nghị giữ trong đề cử, ghi cờ "Astra đề nghị rà H6". Đề cử không phát hành, nên một mối lo chưa có chứng cứ không cần đến H9.
- **R1:**
  - hai cách chọn đều là nhận định; đề nghị lấy hợp: 26 chung, 46 chỉ Astra, 34 chỉ Opus, tổng 106;
  - trừ *đại lục* (A): hai bên đều chấm R1; trong báo chí từ này thường chỉ "Trung Quốc đại lục", dễ chạm H6.3;
  - nhận *piano* của Astra: mã loại H5 của Opus là sai (mục 4).
- **L3b (46):**
  - giữ. Bản §9.1 đã ký mô tả việc mở L2D/L3b là "giữ nguyên luật, mở thêm ứng viên… không đổi luật" (`WordListAnalyze.md:744`); brief cũng cho đề cử từ chưa vào rổ nếu có chứng cứ;
  - số đếm mạnh, hầu hết là tên vật đời thường;
  - điều kiện ghi rõ: P2, P4, H9.
- **L2D (19) và 5 mục chưa vào rổ:** Opus rút khỏi danh sách đề cử, chuyển sang phụ lục "ý tưởng cần đo". Lý do: H8 yếu hoặc chưa có số đếm, và để tổng không vượt 300.
- **Kết quả đề xuất:** 284 = 132 khấu trừ + 106 R1 + 46 L3b. Khóa duy nhất, không giao với khóa chính hay dự phòng (V, assert trong `E/de-xuat-hop-nhat.py`).
- **Kiểm thêm các mục chỉ Astra có** (V, `E/bien-the-de-cu-chi-astra.tsv`, `E/de-cu-chi-astra-hnd.tsv`):
  - không trùng khóa chặn, không thuộc họ LOAI hay CHO, không có còi H7;
  - *ấn bản* trùng khóa *ăn bẩn* (HND), không phải nhóm đỏ rõ;
  - *tụ điện* trùng khóa *từ điển*; *từ điển* không có trong danh sách, nên không có vấn đề.

### 2.4. Thiết kế tài liệu và tệp

- **Tên tệp và tiêu đề:** Opus nhận đề xuất của Astra: `AT/honorable-mentions.tsv` và `## 12. Từ có thể cân nhắc (honorable mentions)`, theo đúng chữ chủ dự án dùng.
- **Mục 11:** Opus nhận giữ khối 205 từ (11.5 của Astra) và thêm một bảng ngắn cho D, C có lý do. Số A, B ghi kèm link sang TSV.
- **Cột của TSV công bố:** đề nghị bản ở `AT/` gọn (khoảng 14 cột như mục 5.5 vòng 1 của Opus); bản 58 cột của Astra để trong hồ sơ. Lý do: bản công bố cho người bảo trì đọc, còn bằng chứng từng cổng đã có trong hồ sơ.

## 3. Lỗi trong phân tích của Astra

| # | Lỗi | Bằng chứng (V) | Hệ quả |
|---|---|---|---|
| E1 | H8 bỏ qua mã CHI_BE_MAT của tập luật P2: `inventory.py` xếp mạnh khi đủ ngưỡng theo lượt bề mặt, không xét lượt sạch | Tập luật `U/tap-luat-P2-v4.json`, `hop_dong[12]`: "mạnh nhưng chỉ nhờ lượt bề mặt… → H8:CHI_BE_MAT (CANH_BAO)". Cổng thật của cả hai bộ kiểm cho *cả nghĩ* (`U/cong-opus-v4.tsv:10484`), *tối mù* (`:105425`), *vây cá* (`:114263`) là CANH_BAO H8:CHI_BE_MAT; cùng dòng trong `U/cong-astra-v4.tsv` | Dự phòng là 198 MANH (gồm *thụp* của L2C), 4 YEU, 2 CHI_BE_MAT, 1 KHONG_LUOT, không phải "200 mạnh, 4 yếu, 1 không-lượt". Đề cử của Astra có *vây cá* CHI_BE_MAT, không phải "cả 200 mạnh" (`E/h8-chinh-thuc.tsv`) |
| E2 | Mẫu số H8 lấy 34.314.528 và 149.860.716 (mục 0 của bộ tiêu chí), không lấy số cổng P2 đã dùng | `U/tap-luat-P2-v4.json` → `tong_am_tiet`: 34.329.387 và 150.070.912 | Không mục nào của Astra đổi kết quả. Opus mắc cùng lỗi (mục 4) |
| E3 | Dẫn `WordListAnalyze.md:746` cho ngoại lệ hai lượt viết lại của D7 | Dòng 745 là phương án B (ngoại lệ D7); dòng 746 là phương án C (đổi D6) | Chỉ sai trích dẫn |
| E4 | Không quét biến thể ngoài bảng họ đã đăng ký ("chưa phát hiện họ mới") | Mục 2.1: *tròng trành ↔ chòng chành* có nguồn từ điển ghi là dạng khác; *chán phèo ↔ chán phè*; *chọc lét ↔ chọc léc* theo tiền lệ *cù lét/cù léc* | Ba mục xếp A dù không thể qua H5c nếu họ được đăng ký; một mục chính (*chòng chành*) vướng theo (CH1) |
| E5 | Tiêu chí C không nhất quán về độ quen | Mục 2.2 | Không đổi luật; chỉ cần sửa bậc |
| E6 | Lý do giữ *đại lục* ("khái niệm địa lý") bỏ qua nghĩa chính trị thường gặp | (A) | Đề nghị bỏ khỏi đề cử |

Các số khác của Astra đã đối chiếu và **đúng** (V):

- mốc rổ 10.156, 10.133, 10.001 và 2.020;
- lớp, ngăn, nguồn của 200 đề cử (C/H/K/F 117/44/34/5; 122/5/73; 195 L1, 2 L2A, 3 L3);
- 18 mục đủ hai chữ ký H3, *chia* đủ K2;
- 8.181 khóa duy nhất;
- trích dẫn `U/chu-ky.tsv` và `U/phieu-astra.tsv` cho H8, H5, K2;
- lỗi CRLF của hai bộ kiểm (1 C1; 1 C1 và 2 C8).

## 4. Sửa phân tích vòng 1 của Opus

| # | Sửa | Căn cứ |
|---|---|---|
| K1 | D từ 6 xuống 3: *hì hụi, nhão nhẹt, nhão nhoẹt* sang C. Với *chọc lét*, bỏ *thọc lét, thọc léc* khỏi lý do (Wiktionary ghi là từ đồng nghĩa); chỉ dựa vào *chọc léc* và tiền lệ *cù lét/cù léc* | Mục 2.1 |
| K2 | Mục 5.3 thiếu một trường hợp: dự phòng không-F cũng thay được ghế F, vì Q3 là trần ≤ 77 (Astra 3.3). Số suất thay cho ghế F không chỉ là 77 mục F | `AT/tieu-chi-thong-nhat.md:201` |
| K3 | *piano* đã có họ đăng ký và qua H5 (`AT/spelling_families.tsv:269`: *pi a nô, pi-a-nô, pianô*, 449/3 và 1.818/2, QUA_RIENG_H5). Các dạng kia cùng khóa `piano`. Mã loại H5 của Opus cho *piano* là sai | V |
| K4 | Mẫu số H8 phải dùng 34.329.387 và 150.070.912 của P2 v4.1. *bánh củ cải* (15 lượt web) là YEU, không phải MANH. Nhãn H8 nên ghi đúng mã cổng: dự phòng 198 MANH, 4 YEU, 2 CHI_BE_MAT, 1 KHONG_LUOT ("6 yếu" ở vòng 1 gộp hai mã) | `E/chung.py` ghi thêm hằng số; `E/h8-chinh-thuc.tsv` |
| K5 | Thủ tục D: không cần "biên bản khấu trừ hai chữ ký"; theo H9, phản đối hợp lệ còn giữ sau một lượt phản biện thì mục không được dùng (như định nghĩa D của Astra) | `AT/tieu-chi-thong-nhat.md:180–193` |
| K6 | Nhận 10 mục C của Astra. Bậc đề xuất: A 141, B 36, C 25, D 3 | Mục 2.2 |
| K7 | Đề cử: bỏ L2D và 5 mục chưa vào rổ khỏi danh sách (chuyển phụ lục); nhận R1 của Astra trừ *đại lục*. Tổng 284 | Mục 2.3 |
| K8 | Mục 11: giữ khối 205 từ; tên tệp và tiêu đề mục 12 theo Astra | Mục 2.4 |

Bảng `du-phong-205-phan-loai-opus.tsv` và `de-cu-them-opus.tsv` của vòng 1 giữ nguyên làm hồ sơ. Các sửa đổi ghi ở hai tệp đề xuất trong `E/` và sẽ đưa vào bảng chung ở bước báo cáo chung.

## 5. Danh sách câu hỏi hợp nhất

Astra không có câu hỏi, nên không có câu nào cần đổi mã.

| # | Trạng thái | Gửi | Câu hỏi | Lựa chọn | Đề nghị |
|---|---|---|---|---|---|
| CH1 | Giữ, cập nhật chứng cứ | Chủ dự án | *chòng chành* (danh sách chính) và *tròng trành* (dự phòng) là hai dạng của cùng một từ (V, en.wiktionary). Cả họ thiếu dữ liệu nên theo H5c cả mục chính cũng không đạt. *hì hục ↔ hì hụi* là trường hợp tương tự nhưng chưa có nguồn (A). Làm gì với mục chính? | (a) chỉ ghi nhận ở 11.5; (b) ghi nhận, rà riêng ở đợt sau; (c) thay ngay (trái yêu cầu "không đổi danh sách chính") | (b) |
| CH2 | Rút | — | Giữ `du-phong.txt` 205 dòng hay bỏ D | Hai SA cùng giữ 205 dòng và SHA (Astra 5.2 mục 1) | — |
| CH3 | Rút | — | R1 có vào ghế OK không-F khi hết OK không | Hai SA cùng đọc chặt: R1 chỉ thay R1 (Astra 3.3) | — |
| CH4 | Rút | — | Viết nghĩa ngay cho 36 mục B | Hai SA cùng để sau (Astra mục 8); chủ dự án đã giới hạn đợt này ở phân tích | — |
| CH5 | Thêm, có điều kiện | SA-Fable | Chỉ gửi nếu sau báo cáo chung hai SA vẫn khác ý ở một trong hai điểm. (a) Một cặp biến thể mới tìm thấy, có nguồn từ điển hoặc tiền lệ, có được xử theo H5c và H9 (một bên phản đối thì mục không dùng) khi cặp đó chưa có trong bảng họ, trong khi H5 đòi hai bên xác nhận "cùng một từ"? Áp cho *tròng trành, chán phèo, chọc lét*. (b) Ứng viên L3b chưa chấm có được ghi là đề cử thêm, kèm điều kiện P2/P4/H9? | (a1) được, theo H9; (a2) chỉ khi hai bên cùng xác nhận. (b1) được, có điều kiện; (b2) không | (a1) và (b1) |

## 6. Tệp mới trong bước này

Tất cả trong `AT/ho-so/opus/du-phong-v2/`; chỉ có đầu mục, số đếm, mã và băm.

- `round-1-cross-review.md` (tài liệu này).
- `evidence/doi-chieu-astra.py` → `doi-chieu-du-phong.tsv`, `doi-chieu-de-cu.tsv`.
- `evidence/kiem-h8-chinh-thuc.py` → `h8-chinh-thuc.tsv`.
- `evidence/de-xuat-hop-nhat.py` → `du-phong-205-bac-sau-soat-cheo-opus.tsv`, `de-cu-hop-nhat-de-xuat-opus.tsv`.
- `evidence/de-cu-chi-astra.txt`, `bien-the-de-cu-chi-astra.tsv`, `de-cu-chi-astra-hnd.tsv`.
- Sửa nhỏ, không đổi kết quả vòng 1:
  - `chung.py`, `kiem-hnd.py`, `do-bien-the.py` đọc thư mục HND tạm từ biến môi trường `HND_DIR`, để bản tạm nằm ngoài repo;
  - `chung.py` ghi thêm mẫu số P2.
