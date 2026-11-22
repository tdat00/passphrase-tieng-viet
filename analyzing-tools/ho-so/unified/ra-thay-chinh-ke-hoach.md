# Rà và thay danh sách chính — kế hoạch

**Status: Final (2026-11-22, base fc97441)** — SA-Opus "accept" (`ho-so/opus/ra-thay-chinh/ky-ke-hoach.md`), SA-Astra "accept" (`ho-so/astra/ra-thay-chinh/ky-ke-hoach.md`, chạy trên gpt-6.2-astra theo Q-rtc-M1 b). Không còn câu hỏi mở. Thay danh sách chính chỉ bắt đầu khi chủ dự án duyệt kế hoạch này (D-rtc-3).

- **Tác giả:** SA-Opus (soạn), SA-Astra (duyệt). Lượt duyệt 1 và 2 của Astra: "changes requested" (`ho-so/astra/ra-thay-chinh/round-1-review-drafts.md`). Bản này đã sửa theo cả hai lượt, các thỏa thuận T-rtc-12 đến T-rtc-18 và quyết định D-rtc-5 đến D-rtc-8 của chủ dự án (nhật ký: `ho-so/opus/ra-thay-chinh/round-1-revision-1.md`).
- **Ngày:** 21/11/2026.
- **Gốc:** `1c3f504` (= `main` `f404a95` cộng hồ sơ yêu cầu), nhánh `analyze/ra-thay-chinh`.

**Tài liệu đi kèm** (trong `analyzing-tools/ho-so/unified/`):

- báo cáo chung: `ra-thay-chinh-bao-cao-chung.md`;
- câu hỏi: `ra-thay-chinh-cau-hoi.md`;
- bảng: `ra-thay-chinh-h7.tsv`, `ra-thay-chinh-h5.tsv`, `ra-thay-chinh-thay-the.tsv`.

**Viết tắt:** `AT` = `analyzing-tools`; `TC` = `AT/tieu-chi-thong-nhat.md`; `RD` = `ho-so/astra/ra-thay-chinh/evidence/`; `OE` = `ho-so/opus/ra-thay-chinh/evidence/`.

## 1. Mục tiêu

Thực hiện D-dpv2-5. Rà danh sách 7.776 từ theo H5 (họ chính tả) và H7 (cách đọc không dấu), gồm:

- họ *chòng chành*/*tròng trành*;
- ca báo tử;
- 632 cặp H5 và 1.177 cặp H7.

Từ chính trượt luật đã ký được thay bằng từ dự phòng có giải nghĩa viết sạch mới đạt D6/D7. Sau đó cập nhật dữ liệu và tài liệu có sẵn. Chỉ thay sau khi kế hoạch Final và chủ dự án duyệt (`ra-thay-chinh-yeu-cau.md:13–15`).

## 2. Phạm vi

**Trong phạm vi:**

- sàng lọc H5/H7, kể cả K0, còi dưới 0,3 PPM, còi tương đối, cách đọc HND cùng khóa;
- phân xử và ký;
- xếp hạng và chọn từ vào theo P6/P7 (`ra-thay-chinh-yeu-cau.md:19`), theo S4 và ngăn hạn mức. Thứ tự từ vào theo T-rtc-14: tính lại S2/S3 một lần theo P6;
- lượt viết sạch; D2/D5/D6/D7/D8;
- sinh khối bằng `build_wordlist.py`;
- cập nhật `WordListAnalyze.md` (đầu tài liệu, mục 3, 10, 11, 12 và mục 13 mới), các TSV công bố, bảng chặn, họ chính tả, `README.md`, `manifest.json`;
- đăng ký `baotu` và các họ H5 có từ chính.

**Ngoài phạm vi:**

- việc mở khác của dự phòng v2: bốn họ chỉ ở tầng D, *ngoại trừ*/*ngoại trú*, L2D/L3b;
- rà lại H6 cho toàn bộ 7.776 từ;
- đổi trọng số S3 hoặc ưu tiên tầng;
- bù dự phòng về 205 hay 300; viết nghĩa cho mọi dự phòng;
- đổi giao diện app;
- sửa `WordListAnalyze-Opus.md`, `WordListAnalyze-Astra.md`.

## 3. Hiện trạng

- 7.776 từ chính: 480 từ một âm tiết, 7.033 từ hai âm tiết, 263 từ ba âm tiết; F = 77, R1 = 0.
- Dự phòng 205 từ: A148, B36, C15, D6. Từ có thể cân nhắc (HM): 237.
- `blocked_keys.tsv`: K0 43, K0;K1 1, K1 58, K2_CHUA_KY 8. `spelling_families.tsv`: 277 họ.
- Chữ ký nằm ở `ho-so/unified/chu-ky.tsv`. Bảng còi cũ chỉ bật theo từ vựng âm tiết, nên sót các cách đọc có nghĩa đỏ ở mức cả cụm.
- Kết quả rà: báo cáo chung, mục 1–4.

## 4. Luật quyết định

### 4.1. H7 và K0

**Hai bên đã đồng ý:**

- So toàn khóa. Còi khi PPM của cách đọc ≥ 0,3 hoặc ≥ PPM của mục. Cách đọc về tự hại, bạo lực, tình dục rõ thì xét cả dưới mốc (TC:160).
- Xét mọi nghĩa còn dùng phổ biến của cách đọc; không làm sạch bằng nghĩa phụ lành (TC:139).
- K0 cần nguồn chứng thực toàn mục là tục, tình dục người lớn hay chất thải, không có ngưỡng tần suất. Nhãn *offensive* không đủ cho K0.
- K2 không vào bản 1 khi chưa đủ hai chữ ký (TC:167, :202, :525). Phản đối hợp lệ còn giữ sau một lần phản biện thì từ không phát hành (TC:190–191).
- Chữ ký K2 cũ giữ nguyên nếu không có chứng cứ mới.
- Không chặn chỉ vì tên loài, bộ phận cơ thể thường ngày, danh tính.

**S1 (17 khóa), đã khép:**

- Hai SA thỏa thuận 7 khóa (T-rtc-12): K1 cho *cò trắng, sân ga, trăng tròn*; K2 cho *húng, hững hờ, phù dâu, thắm thiết*.
- Chủ dự án quyết 10 khóa (D-rtc-6): K1, thay, cho *vòng, thuần, xuân*; K2, giữ, hai SA ký kèm lý do, cho *lưới, phòng ngủ, tường, thị trường, khiến, ngại, trạm*.
- Không ban hành ngưỡng số: Opus chỉ dùng tỷ lệ r làm chứng cứ đối chiếu tiền lệ. Muốn dùng một ngưỡng số làm luật thì phải có chủ dự án xác nhận.

### 4.2. H5

**Hai bên đã đồng ý:**

- Ngưỡng ≥ 20 lượt và ≥ 95% cho loại c, b, f; ≥ 10% cho loại d; đo bằng số nguyên, có thử độ nhạy dòng trùng (TC:103–135).
- H5f cộng các dạng chỉ khác dấu phân cách (cách, gạch nối, viết liền), không đếm một lượt hai lần (TC:127). Đây là hợp đồng, không phải điểm tranh chấp.
- H5b chỉ áp cho vần đúng bằng i hoặc y (`ho-so/unified/tap-luat-P2-v4.json:575`).
- H5e: cặp mà phép đếm lẫn nghĩa khác thì đọc mẫu ngữ cảnh; chưa phân định thì chờ (TC:126).
- Dạng kia chỉ là tên riêng viết hoa thì không tạo họ. Không đăng ký 632 cặp thô.
- Chữ CHO của bộ sinh không tự là phản đối hợp lệ (TC:180–194). "Chờ" là chưa được nhận ở bản 1 (TC:12).

**S2, đã thỏa thuận (T-rtc-13):** bảy từ có dạng kia chỉ là đầu mục HND, chưa đủ căn cứ loại c hay d. Ghi CHO_LOAI và không phát hành ở bản này. Không dùng có mặt trong HND làm căn cứ loại c.

## 5. Danh sách từ chính phải thay

Danh sách đầy đủ: `ra-thay-chinh-thay-the.tsv` (vai trò RA, cột `trang_thai`).

**Thay (116 từ):** 104 từ hai SA đồng thuận ở thỏa thuận S1–S3, 3 từ theo D-rtc-6, và 9 từ hai SA đồng ý thay khi khép mục mở (T-rtc-15, T-rtc-16).

- H7 K0 (2): *phản bác, tính khí*.
- H7 K0 thêm: *niêu* (T-rtc-15).
- H7 K1 (89), gồm *cò trắng, sân ga, trăng tròn* (T-rtc-12), *vòng, thuần, xuân* (D-rtc-6) và *chậm, cổng, mặt nước, thiếu, trán* (T-rtc-15):
  - *áo quần, ăn diện, bà chủ, bàn ăn, bảo hành, báo động, bền bỉ, bố mẹ, bộ ba, ca nhạc, cao giá, cắm đầu, choàng, chỏm, chồn, chữ nghĩa, cổ thụ, cộng sự, cuốc, dàn ý*;
  - *dặn dò, di dời, diều, dò hỏi, đánh bại, đậm đà, đầu mùa, đích, đỏ thắm, đột phá, gầy gò, giảm, giao, giấc, giận dỗi, gọng, hâm mộ, hoa mai, hỏi thăm, hóm hỉnh*;
  - *hố ga, kiến, làng, lằng nhằng, lề đường, măng, mê mẩn, mời mọc, nằm mơ, nắm vững, ngao, ngắt, ngọc, ngụm, nguyên, ngựa, nhai, nhàu, nhồi, nhốt*;
  - *phân công, phong thư, sàng, sông, tài hoa, thái, thảm, than, thể lực, thiên tài, thong dong, thôn, thớt, thư thái, tiệm, tiền công, tiếp viên, trời*;
  - *cò trắng, sân ga, trăng tròn*;
  - *vòng, thuần, xuân*;
  - *chậm, cổng, mặt nước, thiếu, trán*.
- H5 (24):
  - loại c, thiếu dữ liệu hay dưới ngưỡng: *chòng chành, bồ kết, rau dền, ngoảnh, phấp phới, già dặn, dây chun, dây thun, phí phạm, lấn át, rầm rầm*;
  - loại f, đã cộng dạng phân cách (`OE/dem-h5f.tsv`; Astra xác nhận ở `RD/rd2-H5-xac-nhan.tsv:2–4`): *cải xoong, xà bông, xà phòng*;
  - CHO_LOAI, không phát hành ở bản này (T-rtc-13): *co rúm, xù xì, rầm rộ, chơ vơ, xập xình, su hào, loay hoay*;
  - khép mục mở (T-rtc-16): *chun, thun* (H5e rồi c, không dạng nào đạt 95% ở cả hai kho), *tép riu* (c, thiếu dữ liệu).

**Chủ dự án đã quyết (D-rtc-6, `0253bb0`):** thay *vòng, thuần, xuân*; giữ *lưới, phòng ngủ, tường, thị trường, khiến, ngại, trạm*. Bảy từ giữ là K2: hai SA ký "không tự động chặn" kèm lý do; chưa đủ chữ ký thì không phát hành.

**Khép mục mở (T-rtc-15 đến T-rtc-18):** 282 trong 286 dòng đã khép bằng một lượt đối đáp (`ho-so/astra/ra-thay-chinh/khep-muc-mo-1.*`, `ho-so/opus/ra-thay-chinh/khep-muc-mo-1-opus.*`).

**Chủ dự án đã quyết (D-rtc-7, `2cc6aec`):** giữ *cần cù, tiền lương, triệu* (H7) và *bạn thân* (gói K2), K2; hai SA đã ký (Astra: `ho-so/astra/ra-thay-chinh/khep-muc-mo-2.tsv`; T-rtc-20).

**Giữ:**

- 233 khóa K2 hai SA đã ký trong phiếu khép mục mở (T-rtc-18): 204 khóa của gói (193 khóa cũ, 4 của T-rtc-12, 7 của D-rtc-6) và 29 khóa H7 chờ;
- 4 khóa của D-rtc-7, hai SA đã ký (T-rtc-20). Mọi chữ ký được ghép vào `chu-ky.tsv` ở gói phát hành;
- 8 khóa H7 chờ có cách đọc không đỏ (T-rtc-15);
- *đồng ý, đuốc* (cách đọc không đỏ);
- K2 đã ký (9): *bình, di động, khảm, kính, nướng, phết, thầy, thổi, trứng*;
- *gián* (quyết định 5);
- các cặp QUA và khác từ (báo cáo chung, C12, C13), gồm 21 dòng H5 chờ đã khép giữ (T-rtc-16).

**Số từ ra cuối: 116.** Từ vào lấy từ 118 dự phòng dùng được; đệm thêm tối đa 25 HM theo D-rtc-8 (mục 6.1).

## 6. Từ vào

**Ngăn và hạn mức.**

- Mọi từ ra hiện ở ngăn OK không-F. F = 77 đã đủ trần, nên mục F chỉ vào được khi có từ F rời danh sách.
- Mỗi lần nhận một mục thì cập nhật F và R1, như vòng lấp của `choose()` (`ho-so/unified/p6-tinh-doc-lap-astra.py:83–88`, trần ở dòng 12: F ≤ 77, R1 ≤ 388).
- Mục OK không-F được thay ghế F nếu phép gán và hạn mức cho phép.
- Nghiệm thu dùng F ≤ 77, không bắt F = 77. Không dùng từ ba chữ.
- R1 chỉ thay ghế R1, không lấp ghế OK (TC:407). Trần nhận R1 khi chọn là min(388, R1 còn lại + số từ R1 ra).
- `OE/de-xuat-thay-v2.py` có phép tự kiểm cho hai ca Astra nêu: R1 không thay ghế OK; H5b sinh mọi tổ hợp (*tỉ mỉ* → *tỷ mỷ*). Kết quả mô phỏng không đổi vì dự phòng hiện không có R1.

**Thứ tự (T-rtc-14).**

- Tính lại S2/S3 một lần theo P6 trên tập ra cuối (TC:227, :402; `ra-thay-chinh-yeu-cau.md:19`). Rổ chấm: mọi mục qua H1–H9 và có nhãn; mục loại ở D6 chỉ bị bỏ lúc chọn.
- Dùng S4 mới, khóa một lần trước khi viết nghĩa; không chấm lại sau từng lượt viết lại. Giữ trọng số, ưu tiên tầng và luật hòa.
- Dự bị là phần chưa dùng của cùng hàng đợi đã khóa, tối đa 25 nếu đủ.
- **Đã tính lại và khóa (T-rtc-21):**
  - hai chương trình độc lập (Opus: `OE/xep-lai-rtc.*`; Astra: `RD/ky1-xep-lai-astra.*`) đều tái lập đúng `xep-hang.tsv` (10.133 mục) rồi chấm lại;
  - rổ chấm 10.003 mục. Bỏ 116 từ ra và 14 mục không qua H1–H9: 6 mục tầng D; *loằng ngoằng, ngoại trừ, qua quýt, làm cỗ, rướn, cơ quan*; *bao tử* (K1, T-dpv2-7) và *chạng vạng* (chờ H5, T-dpv2-6). Mục chỉ trượt D6/D7 ở P7 vẫn ở rổ;
  - hai chương trình khớp cả 143 dòng (vai trò, vị trí, từ, hạng, điểm): `OE/so-t7.log`;
  - tập 116 từ vào không đổi; hạng mới 7.975–8.115; 28 trong 118 vị trí đổi so với hạng cũ. Dự bị: *cả nghĩ* (8.116), rồi *cửu chương* (8.118);
  - 25 HM giữ nguyên thứ tự (hạng mới 30–1.522) và vẫn là 25 HM OK không-F đầu bảng (mục 26: *giảng viên*);
  - chế độ phụ (bỏ mọi mục LOAI cũ khỏi rổ) cho cùng tập vào và cùng dự bị.
- `ra-thay-chinh-thay-the.tsv` dùng thứ tự đã khóa: cột `hang_S4` là hạng trong rổ mới, `hang_S4_cu` là hạng ở `xep-hang.tsv`.

Khi chọn thì bỏ qua:

- tầng D;
- hai cổng còn mở: *loằng ngoằng* (chờ H5), *ngoại trừ* (chờ H7, lớp F);
- *qua quýt* (họ c đang chờ);
- mục F khi vượt trần.

**Sức chứa.**

- 120 dự phòng OK không-F qua lọc sơ bộ: 108 tầng A, 12 tầng C. Đây chỉ là nguồn sau lọc sơ bộ, chưa khép H1–H9 và nghĩa mới, không bảo đảm đủ 120 từ dùng được.
- Số này được tính lại sau khi khép các mục mở (mục 12), sau khi khép cờ từ vào và sau D6/D7. Không dùng 120 làm ngưỡng cố định của chủ dự án.

**Kết quả mô phỏng** (`OE/de-xuat-thay-v2.py`, `.tsv`, `.log`):

- **116 từ ra:** 118 dự phòng dùng được (120 nguồn, bỏ *làm cỗ*, *rướn* theo T-rtc-17). 116 từ vào (106 A, 10 C; hạng cũ 8.096–8.245, hạng mới 7.975–8.115); còn 2 dự bị. Sau thay: 7.776 từ, 7.776 khóa, F = 77, R1 = 0.
- **Chủ dự án giữ cả 4 từ của Q-rtc-O2 (D-rtc-7)**, nên không thiếu ghế; nhưng chỉ còn 2 dự bị. Đệm cho D6/D7 là chu kỳ HM ≤ 25 (D-rtc-8, mục 6.1).
- **Tính lại S2/S3 (T-rtc-14)** chỉ đổi thứ tự trong cùng hàng đợi, không đổi sức chứa.
- **Nhánh thêm *theo* (lớp F):** 117 ra, 117 vào, F = 77, 7.776 khóa. Chứng minh hạn mức F được cập nhật mỗi lần nhận.
- **Trung vị PPM sạch:** tập 116, từ ra 1,914, từ vào 0,0729 (`OE/hop-nhat-rtc.log`).

**Cờ từ vào (đã khép, T-rtc-10 và T-rtc-17).** Cờ có thể làm đổi tập vào hay sức chứa, nên phải khép trước khi kế hoạch Final, không chỉ trước lượt viết. Có 11 cờ (cột `can_soat` của `ra-thay-chinh-thay-the.tsv`). Ba cờ đã đóng chung (T-rtc-10); đóng riêng cờ không thay cho tái kiểm H1–H9 toàn từ.

| Từ | Vai trò | Cờ | Trạng thái |
|---|---|---|---|
| *đưa đò* | vào 3 | cách đọc *dưa đỏ* | Đã đóng chung: không đỏ (`RD/rd2-de-xuat-dong-co.tsv:2`) |
| *làm cỗ* | vào 15 | *làm cỏ* | Không nhận (T-rtc-17): *làm cỏ* có nghĩa tàn sát; 4/6 mẫu phụ đề sạch rõ nghĩa bạo lực |
| *thay lông* | vào 31 | *thay lòng* (0,31 PPM) | Giữ (T-rtc-17): K2, hai SA đã ký |
| *xoành xoạch* | vào 48 | H5: *xành xạch, xoàn xoạt* | Giữ (T-rtc-17): khác từ |
| *thụp* | vào 51 | H5: *chụp, thụt* | Giữ (T-rtc-17): khác từ |
| *loáng thoáng* | vào 59 | H5: *loáng choáng* | Giữ (T-rtc-17): khác từ |
| *nặng cân* | vào 65 | H5: *lặng câm* | Đã đóng chung: khác từ (`RD/rd2-de-xuat-dong-co.tsv:3`) |
| *rướn* | vào 73 | H5: *dướn, rướm* | Không nhận (T-rtc-17): *dướn* dẫn về *rướn*, loại c; phụ đề 14 + 0, web 5 + 0, thiếu dữ liệu |
| *mang máng* | vào 77 | *màng màng* | Giữ (T-rtc-17): không đỏ |
| *xầm xì* | vào 106 | H5: *sầm sì* | Giữ (T-rtc-17): khác từ |
| *thẳng đơ* | dự bị 108 | *thang độ* | Đã đóng chung: không đỏ (`RD/rd2-de-xuat-dong-co.tsv:4`) |

**Tái soát mỗi từ vào trước khi viết:**

- H7: cách đọc DOC_KHAC, HND và đầu mục Kaikki cùng khóa. Gồm K0 bất kể tần suất và các cách đọc về tự hại, bạo lực, tình dục rõ dưới mốc còi;
- H5: các dạng a–h, gồm dạng phân cách;
- H6, H8.

Từ vào trượt cổng thì nhường ghế cho mục kế tiếp theo phương pháp chọn đã thống nhất; tính lại sức chứa.

### 6.1. Chu kỳ HM có giới hạn (D-rtc-8)

**Nguồn.**

- `AT/honorable-mentions.tsv`, chỉ nhãn OK (130 mục: 120 D6_CUOI, 10 D7_CUOI).
- Bỏ 5 mục lớp F: F đang ở trần 77 và mọi ghế cần lấp đều không-F. Còn 125 mục OK không-F.
- Không dùng 107 mục R1: R1 không thay ghế OK (TC:407).

**Chọn ứng viên.**

- Astra lập `ho-so/astra/ra-thay-chinh/hm-chu-ky-1.tsv` theo hạng; Opus duyệt một lượt (`ho-so/opus/ra-thay-chinh/hm-chu-ky-1-opus.*`). Không có mục nào phải trình chủ dự án.
- Mỗi ứng viên kiểm lại đủ H1–H9:
  - khóa không trùng danh sách chính sau thay, dự phòng, và `blocked_keys.tsv` (gồm các khóa K0/K1 mới của đợt này và `baotu`);
  - H5/H7 theo luật đã thống nhất ở đợt này (T-rtc-5, T-rtc-6, T-rtc-12 đến T-rtc-17), K0 bất kể tần suất;
  - H6, H8; không từ ba chữ; điều kiện ghi ở cột `dieu_kien` (kiểm lịch sử từng mục, rà H6 khi có ghi chú).
- Không dùng lại câu nghĩa đã bị loại. Lịch sử D6_CUOI hay D7_CUOI không chặn mục khi câu mới đạt.
- Astra chọn theo `diem` của `honorable-mentions.tsv`. Tính lại S4 (T-rtc-14) cho cùng 25 mục, cùng thứ tự (mục 6), nên không có mục mới phải kiểm.

**Kết quả (T-rtc-19).** 25 HM theo hạng (`ra-thay-chinh-thay-the.tsv`, vai trò HM):

- *ngân hàng, khách hàng, biển, côn trùng, cô giáo, thay thế, chỗ ngồi, một mình, bí mật, mùa đông, tàu điện, cụ thể, áp dụng, vận hành, việc làm, chế tạo, lực lượng, chia, bánh ngọt, đánh răng, xe điện, bày tỏ, chuyển đổi, ngắn gọn, tương đương*;
- lớp: 9 C, 9 H, 7 K; hạng S4 cũ 32–1.541, mới 30–1.522; lịch sử P7: 20 D6_CUOI, 5 D7_CUOI (*côn trùng, mùa đông, việc làm, bánh ngọt, xe điện*);
- 5 K2 hai SA ký "không tự động chặn": *biển* (*biến*), *bí mật* (*bỉ mặt*), *vận hành* (*vạn hạnh*), *chia* (*chĩa, chỉa, chía, chị ả*; mở rộng chữ ký cũ của khóa `chia`), *ngắn gọn* (*ngả ngớn, ngả ngốn*);
- không chọn: *cơ quan* (Astra phản đối theo H6 nhóm 3, Opus nhận; TC:190–191), *mình* (lớp F);
- không có HM dự phòng ngoài 25 (trần của D-rtc-8).

**Hàng đợi lấp ghế.**

1. Từ vào lấy từ hàng đợi dự phòng, theo thứ tự T-rtc-14.
2. HM xếp sau toàn bộ dự phòng; trong nhóm HM theo S4 tính lại (T-rtc-14). HM không vượt lên trước dự phòng, vì D-rtc-8 chỉ cho HM làm nguồn bù.
3. Hạn mức kiểm sau mỗi lần nhận: F ≤ 77, R1 không thay OK.

**Viết nghĩa.**

- Một lô `rtc-lo-01` gồm 116 từ vào, 2 dự bị và các HM được duyệt (tối đa 143 từ), viết cùng lượt `rtc-v1`.
- Cổng D2/D5/D6/D7 và tối đa hai lượt viết lại (`rtc-v2`, `rtc-v3`) như mục 7, áp như nhau cho dự phòng và HM.

**Lấp ghế khi trượt.**

- Sau lượt viết lại cuối, từ vào nào còn trượt D6 hay D7 thì nhường ghế. Ghế đó lấy mục kế tiếp của hàng đợi đã đạt D6/D7: 2 dự bị trước, rồi HM theo hạng.
- Mỗi lần lấp kiểm lại khóa và hạn mức.
- Hết hàng đợi mà còn ghế trống thì dừng và hỏi chủ dự án; không tự nới luật.

**Ghi chép.**

- D8 (`AT/nguon-goc-giai-nghia.tsv`, mỗi từ một dòng):
  - HM vào: đổi dòng LOAI sẵn có thành PHAT_HANH, điền các cột của lượt `rtc`, để trống `cong_loai` và `dot_loai` như mọi dòng PHAT_HANH. Lịch sử P7 ghi ở `WordListAnalyze.md` mục 13 và còn trong git;
  - dự phòng vào: thêm dòng PHAT_HANH;
  - mục đã viết mà không dùng (dự bị, HM): không có dòng PHAT_HANH; kết quả D6/D7 nằm trong hồ sơ lượt `rtc` ở `ho-so/unified/`. Dòng LOAI cũ của HM chưa dùng giữ nguyên.
- HM vào danh sách chính được bỏ khỏi `honorable-mentions.tsv`. HM đã viết mà chưa dùng vẫn là HM, kèm ghi chú.
- Không bù dự phòng về 205 hay 300 (T-rtc-7).

## 7. Lượt viết sạch giải nghĩa

Theo D1 và `huong-dan-giai-nghia.md:167–185`.

**Lô và lượt.**

- Một lô `rtc-lo-01` gồm 116 từ vào, 2 dự bị và các HM được duyệt (tối đa 25), xếp liên tiếp theo O1: tối đa 143 từ, dưới 400.
- Lượt `rtc-v1`: một agent mới, cách ly, chỉ có ba tệp: hướng dẫn (bỏ mục 12), `kiem-tra-giai-nghia.py` và lô từ.
- Không mạng, không repo, không giải nghĩa cũ (Opus, Astra, câu lịch sử của dự phòng), không `bang-khoa-chung.tsv`, không phiếu soát.
- Orchestrator lưu cấu hình quyền và nhật ký để chứng minh cách ly.

**Lời nhắc cho người viết.** Chỉ gồm đầu mục và yêu cầu trong hướng dẫn. Không có từ đồng nghĩa gợi ý, không có số đo, không có lý do thay.

**Cổng.**

1. Người viết tự chạy `kiem-tra-giai-nghia.py lo.txt lo.tsv` (D2/D5) và sửa mọi LỖI.
2. Sau khi ghép, orchestrator chạy `kiem-tra-giai-nghia.py --phat-hanh` trên toàn 7.776 từ.
3. Người soát chạy D6 bằng `d6-kiem.py` trong vùng chạy ở mục 8; không chấp nhận `CHUA_KIEM`.
4. D7: hai SA soát độc lập.
   - Chia đôi lô; phần chồng chéo ít nhất max(15, ⌈0,10 × N⌉) từ, chọn trước bằng băm đầu mục (TC:423).
   - Mọi cờ phải được cả hai xem.
   - Phiếu soát chỉ ghi mã lỗi và mô tả bằng lời của người soát.
5. D8: một dòng `PHAT_HANH` cho mỗi từ vào, gồm `luot_viet` = rtc-v1/v2/v3, `lo`, `sha256_giai_nghia`, `d6_ket_qua`, `soat_noi_dung` và cờ.

**Viết lại.**

- Tối đa hai lượt (`rtc-v2`, `rtc-v3`). Mỗi lượt là agent mới, chỉ nhận đầu mục và chẩn đoán ngắn, không nhận câu cũ (TC:307).
- Mục còn trượt thì nhường ghế theo thứ tự lấp ở mục 6.1: dự bị trước, rồi HM.
- Không sửa câu bằng tay.

## 8. D6: vùng chạy và nguồn đã ghim

**Băm từng nguồn so `AT/d6-tham-chieu.json`** (Opus và Astra cùng kiểm ngày 21/11/2026):

| Nguồn | Đường dẫn trong manifest | Byte khớp băm ghim |
|---|---|---|
| OPUS | `../WordListAnalyze-Opus.md` | byte checkout (CRLF); blob Git (LF) không khớp |
| ASTRA | `../WordListAnalyze-Astra.md` | blob Git (LF); byte checkout không khớp |
| GUIDE | `huong-dan-giai-nghia.md` | byte checkout (CRLF); blob Git không khớp |
| FAMILIES | `d6-ho-chinh-ta.tsv` | blob Git (LF); byte checkout không khớp |
| WIKT_VI | `vi.jsonl.gz` | bản lưu ngoài repo; không nằm trong Git |

**Bản Kaikki đã ghim:**

- `vi.jsonl.gz`: SHA-256 `1f0abd21…ffb8187`, 34.422.366 byte;
- tải lại được ngày 21/11/2026 từ URL trong `manifest.json` (`https://kaikki.org/viwiktionary/raw-wiktextract-data.jsonl.gz`, bản trích từ dump 2026-10-02);
- orchestrator giữ một bản đã kiểm băm ở thư mục phiên, ngoài repo.

**Cách chạy D6:**

- Dựng vùng chạy ngoài worktree, giữ bố cục của repo: thư mục gốc chứa hai tệp `WordListAnalyze-*.md`; thư mục `analyzing-tools/` chứa `d6-kiem.py`, `d6-tham-chieu.json`, `huong-dan-giai-nghia.md`, `d6-ho-chinh-ta.tsv`, `vi.jsonl.gz`.
- CLI tìm manifest cạnh script (`AT/d6-kiem.py:545–560`); `--meta` chỉ là tệp ghi siêu dữ liệu, không thay manifest.
- Mỗi nguồn đặt đúng dạng byte khớp băm ở bảng trên. Code và manifest lấy từ revision đã khóa.
- Kiểm SHA-256 từng tệp trước khi chạy. Lưu log, băm và mã định danh bản lưu vào hồ sơ; không lưu nguồn thô vào repo.
- Không đổi pin, không sửa tài liệu nguồn cũ, không chuẩn hóa mù để bộ kiểm xanh.
- Chỉ hỏi Q-rtc-A3 nếu bản ghim thật sự mất. Không dùng A3 để xử lý lỗi EOL.

`d6-ho-chinh-ta.tsv` không đổi, trừ khi hai SA thấy cần thêm họ mới cho D6. Nếu đổi thì phải cập nhật băm trong `d6-tham-chieu.json`.

## 9. Sửa dữ liệu và tài liệu

**Commit.**

- Tác vụ chuẩn bị (phiếu ký, đăng ký họ, lô viết, log D6) có thể commit riêng trong hồ sơ.
- Gói phát hành phải vào cùng một commit cuối:
  - dữ liệu: `wordlist.txt`, `labels.tsv`, `nguon-goc-giai-nghia.tsv`, `blocked_keys.tsv`, `spelling_families.tsv`, `du-phong.txt`, `du-phong-phan-loai.tsv`, `chu-ky.tsv`;
  - khối sinh: `index.html`, `thong-tin.html`, mục 10 của `WordListAnalyze.md`;
  - tài liệu, số và băm liên quan: `WordListAnalyze.md` (mục 11–13), `README.md`, `manifest.json`.
- Cổng (mục 10) chạy trên đúng byte của commit đó.

| Tệp | Sửa |
|---|---|
| `AT/wordlist.txt` | Bỏ các từ ra; thêm từ vào dạng `từ\|giải nghĩa`; giữ O1, NFC, đủ 7.776 dòng |
| `AT/labels.tsv` | Xóa dòng của từ ra. Đổi `trang_thai` của từ vào từ DU_PHONG sang CHINH, giữ nhãn và lớp. F, G, T, `diem` giữ như hiện có (rổ P6, khớp `xep-hang.tsv`); thứ tự S4 mới (T-rtc-21) chỉ ở hồ sơ S4, vì tập vào và dự bị giống nhau theo cả hai hạng. Không đổi schema; bảng không có cột hạng. Thêm `K2` (và `H5` nếu có) vào `chu_ky_hai_ben` cho các từ được ký. HM vào: thêm dòng CHINH (nhãn OK, lớp; F, G, T, `diem` lấy từ `xep-hang.tsv`) |
| `AT/nguon-goc-giai-nghia.tsv` | Từ ra: chuyển sang LOAI, ghi `cong_loai` (H7_K0, H7_K1, H5_c, H5_f…) và `dot_loai` = `ra-thay-chinh`. Từ dự phòng vào: thêm dòng PHAT_HANH. HM vào: đổi dòng LOAI sẵn có thành PHAT_HANH, không thêm dòng (mục 6.1). Giữ 7.776 dòng PHAT_HANH |
| `AT/blocked_keys.tsv` | Khóa ASCII của mọi từ ra vì H7: K0 cho `phanbac`, `tinhkhi`, `nieu`; K1 cho các khóa K1; K2_CHUA_KY cho khóa K2 không đủ chữ ký; cột `nguon` = `H7_RA_THAY_CHINH`. Thêm `baotu` (K1, `nguon` = `T-dpv2-7`) và `lamco` (K1 của dự phòng *làm cỗ*, `nguon` = `T-rtc-17`): tổng 94 khóa mới |
| `AT/spelling_families.tsv` | Thêm họ đã chốt: họ LOAI của từ ra (c, f; CHO_LOAI cho bảy họ của T-rtc-13); 14 họ QUA chưa có trong bảng (8 H5b, *rong ruổi*, *trưng bày*, *giỡn/rỡn*, *nuốt chửng/nuốt trửng*, *theo dõi/theo rõi*, *thư giãn/thư dãn*; `ra-thay-chinh-h5.tsv`, DONG_THUAN_QUA); ghi đủ các dạng phân cách theo cách của dòng 258. Không đăng ký họ còn chờ khi từ chính của họ vẫn ở danh sách |
| `AT/du-phong.txt`, `AT/du-phong-phan-loai.tsv` | Bỏ các từ đã vào chính; cập nhật tầng và mã vấn đề (*làm cỗ*: H7 K1; *rướn*: H5c, T-rtc-17); tính lại số đếm |
| `AT/honorable-mentions.tsv` | Bỏ các HM vào danh sách chính (D-rtc-8); HM đã viết mà chưa dùng giữ lại, ghi chú lượt `rtc` |
| `ho-so/unified/chu-ky.tsv` | Thêm dòng K2 và H5 của từng SA (`hieu_luc = CO`): 238 khóa của danh sách chính và từ vào (T-rtc-18, T-rtc-20) và 5 khóa HM (T-rtc-19); `tep_goc` trỏ tới phiếu ký của SA. Khóa `chia`: hai dòng cũ đổi `hieu_luc` và được thay bằng hai dòng mới có phạm vi *chĩa, chỉa, chía, chị ả*; không để bốn dòng cùng hiệu lực |
| `WordListAnalyze.md` | Đầu tài liệu (dòng 3–11): bản phát hành 2, số liệu tính lại, lượt `rtc`, số dư dự phòng, trỏ tới mục 13. Mục lục (dòng 26–37): thêm mục 13. Mục 3: thêm quyết định của chủ dự án khi duyệt. Mục 10: sinh lại. Mục 11 (dòng 8649–8920): sửa 11.1, 11.2, 11.4, 11.5. Mục 12: cập nhật số HM và các HM đã dùng (D-rtc-8). Mục 13 mới "Rà và thay danh sách chính (bản phát hành 2)": 13.1 Phạm vi và nguồn; 13.2 H5; 13.3 H7; 13.4 Từ đã thay; 13.5 Chữ ký; 13.6 Giải nghĩa từ vào; 13.7 Việc để sau |
| `index.html`, `thong-tin.html` | Chỉ khối `#wordlist`, sinh bằng `python build_wordlist.py`. Mục "Quy tắc chọn từ" của `thong-tin.html` và `TC` chỉ sửa nếu chủ dự án xác nhận một luật mới |
| `AT/README.md` | Dòng 77 (số dòng LOAI), dòng 81 (`luot_viet` có `rtc-v*`), dòng 92 (lần chạy D6 mới), số khóa chặn, số họ |
| `AT/manifest.json` | Băm mọi tệp đã sửa, siêu dữ liệu D6, bản phát hành 2, số chính, dự phòng, HM |

## 10. Tương thích bộ kiểm

**Mốc mà bộ kiểm đọc:** giữ 7.776 dòng (`check_wordlist.py:20`, `verify.mjs:41`) và tiêu đề "## 10. Danh sách 7.776 từ phát hành" (`build_wordlist.py:20`). Thêm mục 13 sau mục 12 không chạm khối mục 10.

**C5** (`check_wordlist.py:120–137`):

- từ ra rời `wordlist.txt` trong cùng commit với khóa chặn và họ LOAI mới;
- không có từ chính nào trong họ LOAI hay CHO;
- họ thiếu dữ liệu phải có chữ ký `H5`.

**C6:** F ≤ 77, R1 = 0, R2 = 0.

**Hai bộ kiểm không phủ hết H1–H9:**

- C5 so nguyên ô `chuan`/`bien_the`, không tự tách các dạng nối bằng " / " (như họ *bít tết*). `verify.mjs` chỉ đọc bảng khóa chặn.
- Vì vậy thêm hai kiểm độc lập, viết trong tác vụ:
  - kiểm họ H5: tách mọi dạng " / ", so với danh sách chính và các trạng thái chờ;
  - kiểm gói chữ ký: mỗi khóa K2 giữ lại ↔ đủ hai người ký ↔ `hieu_luc` ↔ lý do và đối chứng ↔ `labels.tsv`.

**Lệnh chạy:**

- `check_wordlist.py` và `verify.mjs` trên bản xuất LF. Trên checkout CRLF hai lệnh có lỗi nền C1/C8 do EOL (`RD/rd1-gates-summary.json`);
- `build_wordlist.py --check` trên checkout CRLF;
- `kiem-tra-giai-nghia.py --phat-hanh` trên toàn danh sách;
- `d6-kiem.py` trong vùng chạy ở mục 8;
- hai kiểm độc lập ở trên.

Lưu lệnh, mã thoát và log.

## 11. Quyết định

| ID | Quyết định | Người quyết | Ngày | Commit nguồn |
|---|---|---|---|---|
| D-rtc-1 | Chỉ làm D-dpv2-5; không mở việc nào khác | owner | 2026-11-21 | `1c3f504` |
| D-rtc-2 | Rà đầy đủ: họ chòng chành/tròng trành, báo tử, 632 cặp H5 và 1.177 cặp H7; thay từ chính nếu cần | owner | 2026-11-21 | `1c3f504` |
| D-rtc-3 | Cho thay danh sách chính sau khi kế hoạch Final và chủ dự án duyệt, kèm giải nghĩa viết mới đạt D6/D7 | owner | 2026-11-21 | `1c3f504` |
| D-rtc-4 | Không tạo thư mục tài liệu mới; hồ sơ chung ở `ho-so/unified/ra-thay-chinh-*`, kết quả cuối vào tài liệu có sẵn | owner | 2026-11-21 | `1c3f504` |
| D-rtc-5 | Không dùng SA-Fable; hai SA thỏa thuận rồi trình chủ dự án quyết định | owner | 2026-11-21 | tin nhắn Discord 2026-11-21 16:58 +07:00; ghi ở `7fb17fb` |
| D-rtc-6 | Q-rtc-O1: thay *vòng, thuần, xuân* (K1, chặn khóa `vong`, `thuan`, `xuan`); giữ *lưới, phòng ngủ, tường, thị trường, khiến, ngại, trạm* (K2, hai SA ký "không tự động chặn" kèm lý do) | owner | 2026-11-21 | `0253bb0` |
| D-rtc-7 | Q-rtc-O2: giữ *cần cù, tiền lương, triệu, bạn thân* (K2, hai SA ký "không tự động chặn") | owner | 2026-11-21 | `2cc6aec` |
| D-rtc-8 | Q-rtc-A2, phương án 1: mở một chu kỳ có giới hạn, tối đa 25 HM nhãn OK theo hạng; kiểm lại H1–H9; viết nghĩa sạch mới; D6/D7/D8 mới; không dùng lại câu cũ | owner | 2026-11-21 | `2cc6aec` |
| D-rtc-9 | Q-rtc-D1: duyệt kế hoạch Final và cho bắt đầu thay danh sách chính; triển khai trực tiếp (không tách task pack), orchestrator điều phối lượt viết sạch và SA soát. Q-rtc-M1 (22:10): SA-Astra chạy trên gpt-6.2-astra | owner | 2026-11-22 | form `ask_user` và tin nhắn Discord; ghi ở commit này |
| D-rtc-10 | Q-rtc-O3: thay *tụ tập* (K1, khóa `tutap` đọc thành *tu tập*) bằng *cô giáo* (HM kế tiếp theo hàng đợi) | owner | 2026-11-22 | form `ask_user` "thay"; Discord 2026-11-22 18:16 +07:00 "Q-rtc-03 thay, q-rtc-b1 duyệt"; ghi ở commit này |
| D-rtc-11 | Q-rtc-B1: duyệt danh sách ra/vào cuối trước commit phát hành (B1) | owner | 2026-11-22 | như D-rtc-10 |
| T-rtc-1 | Ghi `baotu` K1 vào bảng chặn | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-2 | Giữ chín K2 đã ký (*bình, di động, khảm, kính, nướng, phết, thầy, thổi, trứng*); rút OI-RTC-KY-CU; giữ *gián* theo quyết định 5 | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-3 | Thay 80 khóa H7: K0 *phản bác*, *tính khí*; 78 K1, gồm *thái* và 13 khóa Opus nhận sau duyệt (`ra-thay-chinh-h7.tsv`, `DONG_THUAN_THAY`) | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-4 | Giữ hướng không chặn cho 29 khóa (Astra nhận); *chung cư*, *sắn dây* là K2; mọi khóa K2 giữ lại cần đủ hai chữ ký | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-5 | Thay 11 từ H5 (gồm *rầm rầm*). Qua: 8 họ H5b, *rong ruổi*, *trưng bày*, *bít tết*. Khác từ: *bóng láng*/*bóng loáng*, *thiện chí*/*thiện trí*, *buồn lòng*, *tâm trí*, *run run*; bỏ đối chứng tên riêng. *qua quýt* không thuộc H5b. *chun*/*thun* xử theo H5e | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-6 | Mặc định: K2 chưa đủ hai chữ ký không vào bản 1; phản đối hợp lệ còn giữ thì không phát hành; chữ CHO của bộ sinh không phải phản đối hợp lệ | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-7 | Từ vào có câu viết sạch mới; không bù dự phòng về 205 hay 300; mỗi lần chọn cập nhật F và R1, R1 không thay ghế OK; nghiệm thu F ≤ 77; 120 chỉ là nguồn sau lọc sơ bộ; không đổi trọng số S3 hay ưu tiên tầng, thứ tự chọn theo T-rtc-14 | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-8 | D6 chạy trong vùng riêng ngoài worktree, mỗi nguồn đúng byte ghim; không đổi pin; không đưa nguồn thô vào repo | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-9 | Thay *cải xoong*, *xà bông*, *xà phòng* theo H5f (f xử như c), đã cộng dạng cách, gạch nối, viết liền: *cải xoong* phụ đề 4 < 20 lượt; *xà phòng* 62,6% phụ đề, 92,4% web, dưới 95% ở cả hai kho. Đóng OI-RTC-H5F (`OE/dem-h5f.tsv`; `RD/rd2-H5-xac-nhan.tsv:2–4`) | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-10 | Đóng riêng ba cờ từ vào: *đưa đò*/*dưa đỏ* không đỏ; *nặng cân*/*lặng câm* khác từ; *thẳng đơ*/*thang độ* không đỏ. Không thay cho tái kiểm H1–H9 toàn từ (`RD/rd2-de-xuat-dong-co.tsv:2–4`) | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-11 | Hai SA khép mục mở theo quy trình ở mục 12.1; ca còn bất đồng cụ thể trình chủ dự án (D-rtc-5); K0 còn tranh cãi gửi chủ dự án (TC:164) | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-12 | S1, 7 trong 17 khóa: K1 (thay) cho *cò trắng, sân ga, trăng tròn*; K2 (giữ, hai SA ký) cho *húng, hững hờ, phù dâu, thắm thiết*. 10 khóa còn lại trình chủ dự án (Q-rtc-O1), đã quyết ở D-rtc-6 | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-13 | S2: *co rúm, xù xì, rầm rộ, chơ vơ, xập xình, su hào, loay hoay* ghi CHO_LOAI, không phát hành ở bản này (thay). Không bắt buộc tra thêm; có căn cứ loại d về sau vẫn phải đạt hợp đồng đếm, chữ ký khi thiếu dữ liệu và luật CHO_SAT_NGUONG | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-14 | S3: tính lại S2/S3 một lần theo P6 trên tập ra cuối, rổ gồm mọi mục qua H1–H9 có nhãn, mục loại ở D6 bỏ lúc chọn; S4 mới khóa một lần trước khi viết nghĩa; dự bị là phần chưa dùng của cùng hàng đợi (tối đa 25 nếu đủ); giữ trọng số, ưu tiên tầng, luật hòa | SA-Opus + SA-Astra | 2026-11-21 | `7fb17fb` |
| T-rtc-15 | 46 khóa H7 chờ: giữ 37 (29 K2 hai SA ký, 8 không đỏ); thay 6 (*chậm, cổng, mặt nước, thiếu, trán* K1; *niêu* K0); 3 khóa trình chủ dự án (Q-rtc-O2: *cần cù, tiền lương, triệu*) | SA-Opus + SA-Astra | 2026-11-21 | `67466fb` |
| T-rtc-16 | 27 dòng H5 chờ: giữ 21 (khác từ, không lập họ hay qua theo số); thay *chun, thun* (H5e rồi c) và *tép riu* (c, thiếu dữ liệu); khép 3 dòng đã ra hay không vào (*lằng nhằng, xà bông, qua quýt*) | SA-Opus + SA-Astra | 2026-11-21 | `67466fb` |
| T-rtc-17 | 8 cờ từ vào: giữ 6 (*thay lông* K2 hai SA ký; *xoành xoạch, thụp, loáng thoáng, xầm xì* khác từ; *mang máng* không đỏ); không nhận *làm cỗ* (K1) và *rướn* (c, thiếu dữ liệu) | SA-Opus + SA-Astra | 2026-11-21 | `67466fb` |
| T-rtc-18 | Gói K2: hai SA ký 204 trong 205 khóa (193 cũ, 4 của T-rtc-12, 7 của D-rtc-6); *bạn thân* trình chủ dự án (Q-rtc-O2). Cùng 29 khóa của T-rtc-15 và *thay lông*, hai SA có 234 chữ ký chung | SA-Opus + SA-Astra | 2026-11-21 | `67466fb` |
| T-rtc-19 | Chu kỳ HM (D-rtc-8): 25 HM theo hạng, đều qua H1–H9 (mục 6.1); 5 K2 hai SA ký (*biển, bí mật, vận hành, chia, ngắn gọn*); không chọn *cơ quan* (H6 nhóm 3) và *mình* (lớp F) | SA-Opus + SA-Astra | 2026-11-22 | `91d8ee9` |
| T-rtc-20 | Gói K2 đủ hai chữ ký: Astra ký 4 khóa của D-rtc-7 (`khep-muc-mo-2.tsv`). Tổng 238 khóa (233 khóa chính của T-rtc-18, *thay lông*, 4 khóa của D-rtc-7) và 5 khóa HM của T-rtc-19 | SA-Opus + SA-Astra | 2026-11-22 | `91d8ee9` |
| T-rtc-21 | Tính lại S4 theo T-rtc-14: rổ 10.003 (bỏ thêm *bao tử*, *chạng vạng* theo T-dpv2-6, T-dpv2-7); hai chương trình độc lập khớp 143/143 dòng (T7); thứ tự này khóa làm nguồn chung | SA-Opus + SA-Astra | 2026-11-22 | fc97441 |

| T-rtc-22 | D7 của lượt `rtc`: câu thuộc phần chồng chéo (hoặc có cờ) bị một SA đánh VIET_LAI thì viết lại | SA-Opus + SA-Astra (Opus nhận đề nghị của orchestrator, 2026-11-22) | 2026-11-22 | commit này |
| T-rtc-23 | Kết quả viết nghĩa `rtc-v1..v3`: 141/143 câu đạt D2/D5/D6/D7 (`ho-so/unified/ra-thay-chinh-giai-nghia-dat.tsv`). *sớm tối* (từ vào 101) còn phản đối D7 của Astra sau `rtc-v3` nên nhường ghế theo T-rtc-6 và mục 6.1; dự bị *cả nghĩ* vào thế chỗ. *khách hàng* (HM) trượt cả ba lượt (D6 ở `rtc-v1` và `rtc-v3`, D7 ở `rtc-v2`), rời chu kỳ HM. Còn 1 dự bị (*cửu chương*) và 24 HM đã có câu đạt, chưa dùng | orchestrator theo T-rtc-6, mục 6.1; hai SA đã soát | 2026-11-22 | commit này |
| T-rtc-24 | T9 (soát toàn tập, một lượt đối đáp): hai SA ký K2 cho 61 khóa (65 dòng đối chứng, gồm *đuôi*/đượi, *tử tế*/tư tế); thay *phết* (K0, *phẹt*) và *cau có* (K1, *cầu cơ*); rút từ vào *buồn thiu*, *ỉu xìu* (H5c, thiếu dữ liệu); *công cộng*/công công không đỏ; giữ *dài ngoằng*, *lu bù* (khác từ); sửa chữ ký trùng của *thầy*, mở rộng chữ ký *bảng* cho *băng*, sửa WordListAnalyze.md §13. Ghế lấp theo hàng đợi: *cửu chương*, *ngân hàng*, *biển*, *côn trùng* (và *cô giáo* theo D-rtc-10). Hồ sơ: `ho-so/{opus,astra}/ra-thay-chinh/t9-*` | SA-Opus + SA-Astra | 2026-11-22 | commit này |
Các mục T-rtc-* là chỗ hai bên đã đồng ý qua rà chéo, hai lượt duyệt và hai vòng thỏa thuận (`ho-so/{opus,astra}/ra-thay-chinh/thoa-thuan-*`). SA-Astra xác nhận khi duyệt bản sửa này.

## 12. Mục mở

| ID | Nội dung | Đường xử lý | Chặn Final |
|---|---|---|---|
| OI-RTC-K2-KY | Ghép 238 chữ ký K2 chung và 5 khóa HM vào `chu-ky.tsv` | Gói phát hành; kiểm gói chữ ký (mục 10) | Không: chữ ký đã đủ (T-rtc-20) |

**Đã khép:** OI-RTC-P6 (T-rtc-21); OI-RTC-HM (T-rtc-19); OI-RTC-O2 (D-rtc-7); OI-RTC-A2 (D-rtc-8); OI-RTC-H7-S1 (T-rtc-12, D-rtc-6); OI-RTC-H5-LOAI (T-rtc-13); OI-RTC-H7-CHO và OI-RTC-HND (T-rtc-15; Astra tái ghép đủ 238/238 dòng); OI-RTC-H5-QH và OI-RTC-H5E (T-rtc-16); OI-RTC-VAO (T-rtc-10, T-rtc-17); OI-RTC-H5F (T-rtc-9).

### 12.1. Quy trình hai SA khép mục mở (đã dùng ở khép mục mở 1)

Theo đề nghị của Astra (`ho-so/astra/ra-thay-chinh/round-1-review-drafts.md`, Lượt duyệt 2, mục 2.6); Opus nhận (T-rtc-11).

**Nguyên tắc:**

- Hai SA làm chung. Một bên lập phiếu đề nghị trong thư mục của mình; bên kia đọc, rồi ký hay đối đáp độc lập trong thư mục của mình.
- Không ký gộp chỉ vì đang có nhãn K2; không sinh chữ ký tự động từ chữ "giữ". Không cam kết trước rằng mọi khóa sẽ được giữ.
- Bắt đầu ngay; S1, S2, S3 đã khép. Không sửa dữ liệu chính, không viết nghĩa, không để dev tự quyết ca chưa chốt.
- Không Final khi còn mục nào ảnh hưởng danh sách, thứ tự, dự bị, sức chứa hay chữ ký.

**Phiếu chung** (TSV, một dòng mỗi ca): `case_id, tu, khoa, doi_chung, nguon_va_revision_hash, dem_va_mau_so, ma_cong, ket_luan_de_nghi, ly_do, nguoi_duyet, ngay, phien_ban_ro`.

- Khóa có nhiều cách đọc thì ghi đủ các cách đọc có quan ngại, không chỉ cách đọc có mức cao nhất.
- Phiếu ký cuối thêm phạm vi, hiệu lực và liên kết tới hai ý kiến.
- Không ghi câu của kho, lời từ điển hay giải nghĩa cũ.

| Hàng đợi | Việc | Điều kiện khép |
|---|---|---|
| 46 khóa H7 chờ | Tái ghép số mọi vai trò, gồm 238 dòng từng ghi CHUA_DO nhầm. Tra nguồn toàn mục. Tách nghĩa khi cần; đọc mẫu có seed, lưu ID, hash và nhãn (ví dụ *cần cù*/*căn cứ*, *chậu*/*chầu*, *đinh*/*đình*, *tiền lương*/*tiên lượng*). Các dòng báo thiếu số (*áo ngủ, điểm nhấn, khuy*) kiểm lại trước khi đo bù | Mỗi khóa thành không đỏ, K2 đủ lý do và hai chữ ký, hoặc phản đối đủ căn cứ rồi khép theo H9. CHUA_DO không phải 0 |
| 27 dòng H5 chờ | 14 quan hệ khác từ; 9 cặp QUA về số nhưng chưa rõ quan hệ hay loại; *hì hục*/*hì hụi*; *qua quýt*/*qua quít*; *chun*/*thun* hai chiều. Áp nguyên tắc nguồn của phán quyết S2 khi phù hợp; quan hệ cùng từ kiểm riêng | Mỗi dòng có kết luận nhận, khác từ, loại hay chờ hợp lệ, kèm quyết định phát hành. Dòng có từ đã rời danh sách vì cổng khác thì khép bằng mã đó, không ghi QUA H5 giả |
| 8 cờ từ vào, dự bị | Đọc nguồn và quan hệ. *làm cỗ*/*làm cỏ* xét cả nghĩa bóng. *rướn*/*dướn*, *xoành xoạch*, *xầm xì* cần căn cứ, và số nếu là họ | Từ trượt nhường chỗ cho ứng viên kế tiếp theo phương pháp chọn đã thống nhất; tính lại sức chứa |
| Chữ ký K2 | Kiểm rồi dùng lại chữ ký cũ của *nướng*, *phết*. 205 khóa (194 khóa cũ, 4 của T-rtc-12, 7 của D-rtc-6): mỗi SA ghi lý do và ký từng khóa, dẫn mọi đối chứng đã xét. Cộng riêng khóa chờ được nhận K2 | Hai người ký khác nhau, hiệu lực rõ, không trùng dòng, phạm vi và nguồn khớp bảng H7 và `labels.tsv`. Chưa đủ ký thì không vào |

**Phân tuyến:**

- **Không dùng SA-Fable (D-rtc-5).** S1, S2, S3 đã khép bằng thỏa thuận (T-rtc-12 đến T-rtc-14) và quyết định của chủ dự án (D-rtc-6). Với mọi hàng đợi khác, hai SA thỏa thuận; ca còn lệch sau một lượt đối đáp trình chủ dự án thành lựa chọn ngắn: hai lập trường, hệ quả, đề nghị chung nếu có.
- **Ca phụ thuộc kết quả S1** (ví dụ *đông đúc, nóng, thiếu, tích*; cờ *làm cỗ*, *thay lông*): hai SA áp nguyên tắc của T-rtc-12 và D-rtc-6. Sau một lượt đối đáp mà vẫn còn phản đối hợp lệ thì trình chủ dự án đúng ca đó với hai lập trường, hoặc thống nhất không phát hành theo H9. Không trình cả 46 khóa.
- **K0 tiềm tàng** (*ghen*/*ghèn*, *tình tứ*, *trường*/*truồng*): xét nguồn trước. Nếu hai SA còn tranh cãi một khóa K0 thì gửi chủ dự án (TC:164).
- **Chủ dự án:** Q-rtc-A3 khi kích hoạt (mục 12.2); hàng đợi lấp ghế cạn sau D6/D7 (mục 6.1); mọi đổi luật hay đổi quyết định của chủ dự án. *gián* không mở lại.

### 12.2. Câu hỏi dự phòng cho chủ dự án

Q-rtc-A2 đã được chủ dự án trả lời (D-rtc-8, `2cc6aec`); nội dung dưới đây giữ làm lịch sử. Q-rtc-A3 chưa kích hoạt.

Khi điều kiện xảy ra, orchestrator chép câu hỏi vào `ra-thay-chinh-cau-hoi.md`, đủ mẫu (người nhận, quyết định cần, bối cảnh, chứng cứ, phương án, đề nghị, phần bị chặn, dòng Answer).

**Q-rtc-A2 — mở lại từ có thể cân nhắc (HM) để lấp ghế.**

- **Điều kiện:** gửi ngay khi một trong hai việc xảy ra:
  - kiểm sức chứa sau khi khép 46 khóa chờ, 27 dòng H5 và cờ từ vào, trước Final, cho thấy thiếu ghế. Hiện còn 13 dự bị sơ bộ, nên thiếu khi phải thay thêm quá 13 từ;
  - trượt D6/D7 sau khi chủ dự án duyệt làm thiếu ghế.
- **Cần quyết định:** có cho một chu kỳ viết sạch mới, có giới hạn, cho các HM nhãn OK cần dùng hay không. Nhiều HM đã bị loại ở P7 vì câu trượt D6 hai lần (TC:307), nên mở lại là đổi kết quả P7.
- **Phương án:**
  1. cho một chu kỳ có giới hạn: kiểm lịch sử từng mục, D6/D7/D8 mới, không dùng lại câu cũ; khoảng 1–3 lượt viết, 2–4 lượt SA; không bảo đảm đủ ghế;
  2. không mở HM: tìm từ OK mới qua H1–H9 và đo bốn kho, tốn nhiều thời gian hơn;
  3. dừng ở phân tích.
- **Đề nghị hai SA:** phương án 1.

**Q-rtc-A3 — nguồn D6 đã ghim không còn dùng được.**

- **Điều kiện:** chỉ khi bản Kaikki khớp băm `1f0abd…` thật sự mất. Lỗi EOL của nguồn khác không phải lý do để hỏi.
- **Cần quyết định:** có cho đổi nguồn WIKT_VI của D6 (sửa pin ở `d6-kiem.py:528–531` và `d6-tham-chieu.json`, chạy lại D6 toàn danh sách) hay không.
- **Phương án:**
  1. đổi sang bản mới và chạy lại D6 toàn danh sách;
  2. tìm bản cũ ở kho lưu trữ khác;
  3. tạm dừng việc thay.
- **Đề nghị hai SA:** giữ bản đã kiểm ở thư mục phiên để không phải hỏi; nếu vẫn xảy ra thì phương án 1.

## 13. Nghiệm thu

**Nghiệp vụ:**

- B1: chủ dự án duyệt kế hoạch Final (116 từ ra, hàng đợi từ vào, chu kỳ HM), rồi duyệt danh sách ra và vào cuối cùng trước commit phát hành.
- B2: không còn cách đọc không dấu nào ở nhóm đỏ chưa phân xử trên các khóa của bản phát hành.
- B3: không còn từ chính nào thuộc họ H5 trượt hoặc đang chờ.
- B4: mỗi từ mới có giải nghĩa viết sạch, đạt D6/D7.
- B5: tài liệu nêu đúng từ đã thay và lý do.

**Kỹ thuật:**

- T1: hai bộ kiểm (bản LF) và `build --check` báo 0 lỗi.
- T2: `blocked_keys.tsv` có đúng 94 khóa mới với đúng mã: K0 `phanbac`, `tinhkhi`, `nieu`; K1 cho 89 khóa của từ ra vì H7, `baotu` và `lamco`. So từng khóa và mã với `ra-thay-chinh-h7.tsv`, không chỉ đếm dòng.
- T3: mọi họ đã chốt có trong `spelling_families.tsv` với đúng kết luận (LOAI, CHO_LOAI, QUA), so từng họ với `ra-thay-chinh-h5.tsv`; C5 đạt; kiểm họ H5 độc lập (tách " / ") đạt.
- T4: `labels.tsv` có 7.776 dòng CHINH, F ≤ 77, R1 = 0. Kiểm gói chữ ký đạt: mọi K2 giữ lại, kể cả HM vào, có hai dòng ký hiệu lực trong `chu-ky.tsv`.
- T5: `--phat-hanh` báo 0 LỖI; D6 PASS 7.776/7.776 với đủ năm nguồn ghim. D7 có ý kiến của cả hai SA, phần chồng chéo ít nhất max(15, ⌈0,10 × N⌉) từ.
- T6: D8 khớp một-một với danh sách: 7.776 dòng PHAT_HANH, từ ra là LOAI.
- T7: hai chương trình độc lập, theo phương pháp T-rtc-14, cho cùng tập vào, cùng thứ tự dự bị và HM Đạt ở bước kế hoạch: `OE/so-t7.log`, 143/143 dòng. Chạy lại nếu tập ra đổi.
- T8: dự phòng, HM, `manifest.json` và các mục tài liệu khớp tập thực.
- T9: soát toàn tập sau khi thay (A9). Mọi cách đọc cùng khóa trong DOC_KHAC, HND và đầu mục Kaikki đã có phán quyết, gồm:
  - K0 bất kể tần suất;
  - cách đọc về tự hại, bạo lực, tình dục rõ dưới mốc còi;
  - mọi cách đọc có còi.
- T10: repo không chứa câu của kho, danh sách HND hay lời Wiktionary.
- T11: chu kỳ HM (D-rtc-8): chỉ dùng 25 HM của T-rtc-19, theo thứ tự đã khóa, sau toàn bộ dự phòng; mỗi HM vào có câu sạch mới đạt D6/D7, dòng D8 và dòng `labels.tsv`.
- T12: đúng 116 từ ra của `ra-thay-chinh-thay-the.tsv`; mỗi từ vào thuộc hàng đợi đã khóa; sau thay có 7.776 từ, 7.776 khóa, không từ ba chữ.
- T13: lượt viết có cấu hình quyền và nhật ký chứng minh cách ly; băm câu mới khác băm mọi câu cũ đã lưu của cùng từ (P7, D8).

## 14. Rủi ro

| Rủi ro | Cách giảm |
|---|---|
| Từ vào ít gặp hơn nhiều: trung vị 0,0729 PPM so với 1,804 PPM của từ ra (tập 107) | S4 là luật đã ký; chủ dự án thấy đủ danh sách trước khi duyệt |
| Chỉ còn 2 dự bị; HM từng trượt D6/D7 ở P7 nên có thể trượt nhiều lần nữa | Chu kỳ HM ≤ 25 (D-rtc-8); hết hàng đợi thì dừng và hỏi chủ dự án |
| Kaikki đổi bản trước khi chạy D6 | Giữ bản đã kiểm băm ngoài repo; chỉ hỏi Q-rtc-A3 nếu bản ghim mất |
| Lỗi nền CRLF làm sai kết quả bộ kiểm hoặc D6 | Bộ kiểm chạy trên bản LF; D6 chạy trong vùng riêng đúng byte ghim; lưu log |
| Bộ ghép phiếu đọc sai mã | Bảng ánh xạ đủ mã, mã lạ làm script dừng; cột tệp:dòng để soát |
| Bản quyền | Chỉ lưu số đếm, khóa, nhãn, revision. Kho, HND và Kaikki chỉ để ngoài repo, xóa sau khi dùng (trừ bản Kaikki ghim) |

## 15. Giai đoạn và ước lượng

| Giai đoạn | Việc | Lượt agent |
|---|---|---|
| 1 | Đã xong: Astra duyệt nháp hai lượt; Opus sửa (`round-1-revision-1.md`). Lượt duyệt cuối gộp vào bước ký ở 3b | Xong |
| 2 | Đã xong: hai SA thỏa thuận S1, S2, S3 (`thoa-thuan-1`, `thoa-thuan-2`; T-rtc-12 đến T-rtc-14); chủ dự án trả lời Q-rtc-O1 (D-rtc-6, `0253bb0`) | Xong |
| 3a | Đã xong: hai SA khép mục mở (`khep-muc-mo-1` của hai bên; T-rtc-15 đến T-rtc-18); chủ dự án trả lời Q-rtc-O2 (D-rtc-7) và Q-rtc-A2 (D-rtc-8), `2cc6aec` | Xong |
| 3b | Đã xong: chọn 25 HM (T-rtc-19), gói K2 đủ hai chữ ký (T-rtc-20), tính lại S4, hai chương trình khớp (T-rtc-21). Còn: Astra ký; orchestrator đặt Final; chủ dự án duyệt | 1 lượt SA; 1 lần chủ dự án duyệt |
| 4 | Viết `rtc-v1` cho lô tối đa 143 từ (từ vào, dự bị, HM); D2/D5/D6, D7; viết lại tối đa hai lượt; lấp ghế theo mục 6.1. Hết hàng đợi thì hỏi chủ dự án | 1–3 lượt viết; 2–6 lượt SA |
| 5 | Dev-Sonnet: (a) tác vụ chuẩn bị: gói chữ ký, đăng ký họ, khóa chặn, hai kiểm độc lập; (b) commit phát hành: dữ liệu, khối sinh, tài liệu, manifest; (c) soát toàn tập (T9) | 3–4 lượt dev; orchestrator kiểm và commit |
| Tổng | | Khoảng 7–14 lượt agent còn lại và 1 lần chủ dự án duyệt |

## 16. Tham chiếu

- `ho-so/unified/ra-thay-chinh-yeu-cau.md`;
- `TC` (mục 0 dòng 12; H5 103–135; H6 137–154; H7 156–169; H9 180–194; Q 195–203; D7 307; P6/P7 402–427; bảng phân xử 520–527);
- `huong-dan-giai-nghia.md:167–185`;
- `check_wordlist.py:120–137`;
- `d6-kiem.py:371–378, 528–531, 545–560`; `d6-tham-chieu.json`;
- `ho-so/unified/chu-ky.tsv`, `canh-bao-khong-dau.tsv`, `xep-hang.tsv`, `p6-tinh-doc-lap-astra.py`, `du-phong-v2-ke-hoach.md:415–432`;
- `AT/honorable-mentions.tsv`; `ho-so/astra/ra-thay-chinh/hm-chu-ky-1.{tsv,md}`, `khep-muc-mo-2.tsv`; `ho-so/opus/ra-thay-chinh/hm-chu-ky-1-opus.{tsv,md}`, `OE/hm-chu-ky-1-opus.py`, `OE/xep-lai-rtc.py`, `OE/so-t7.py`; `RD/ky1-xep-lai-astra.*`;
- phân tích, rà chéo, duyệt nháp, thỏa thuận và phiếu ký trong `ho-so/{opus,astra}/ra-thay-chinh/` (Opus ký kế hoạch: `ho-so/opus/ra-thay-chinh/ky-ke-hoach.md`).
