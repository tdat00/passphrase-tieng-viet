# Rà và thay danh sách chính — kế hoạch

**Status: Draft (round 1)**

- **Tác giả:** SA-Opus (soạn), SA-Astra (duyệt). Lượt duyệt 1 và 2 của Astra: "changes requested" (`ho-so/astra/ra-thay-chinh/round-1-review-drafts.md`). Bản này đã sửa theo cả hai lượt (nhật ký: `ho-so/opus/ra-thay-chinh/round-1-revision-1.md`).
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

**Chủ dự án quyết (Q-rtc-O2, 4 từ):** *cần cù, tiền lương, triệu* (H7) và *bạn thân* (gói K2). Astra: K1, thay. Opus: K2, giữ; Opus đã ký. Chưa quyết thì không phát hành.

**Giữ:**

- 233 khóa K2 hai SA đã ký trong phiếu khép mục mở (T-rtc-18): 204 khóa của gói (193 khóa cũ, 4 của T-rtc-12, 7 của D-rtc-6) và 29 khóa H7 chờ. Chữ ký được ghép vào `chu-ky.tsv` ở gói phát hành;
- 8 khóa H7 chờ có cách đọc không đỏ (T-rtc-15);
- *đồng ý, đuốc* (cách đọc không đỏ);
- K2 đã ký (9): *bình, di động, khảm, kính, nướng, phết, thầy, thổi, trứng*;
- *gián* (quyết định 5);
- các cặp QUA và khác từ (báo cáo chung, C12, C13), gồm 21 dòng H5 chờ đã khép giữ (T-rtc-16).

**Phạm vi số từ ra:** 116 đã chốt; thêm tối đa 4 theo Q-rtc-O2.

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
- Mô phỏng ở dưới vẫn dùng hạng đã khóa (`xep-hang.tsv`), nên tập vào và thứ tự chỉ là sơ bộ. Ở tập ra 101, Astra đo được cùng tập vào nhưng đổi thứ tự 31 vị trí, gồm dự bị 104/105 (`RD/rd2-audit-summary.json`, `S4_O101`). Không suy ra tập vào của các tập ra khác khi chưa chạy.

Khi chọn thì bỏ qua:

- tầng D;
- hai cổng còn mở: *loằng ngoằng* (chờ H5), *ngoại trừ* (chờ H7, lớp F);
- *qua quýt* (họ c đang chờ);
- mục F khi vượt trần.

**Sức chứa.**

- 120 dự phòng OK không-F qua lọc sơ bộ: 108 tầng A, 12 tầng C. Đây chỉ là nguồn sau lọc sơ bộ, chưa khép H1–H9 và nghĩa mới, không bảo đảm đủ 120 từ dùng được.
- Số này được tính lại sau khi khép các mục mở (mục 12), sau khi khép cờ từ vào và sau D6/D7. Không dùng 120 làm ngưỡng cố định của chủ dự án.

**Kết quả mô phỏng** (`OE/de-xuat-thay-v2.py`, `.tsv`, `.log`):

- **116 từ ra:** 118 dự phòng dùng được (120 nguồn, bỏ *làm cỗ*, *rướn* theo T-rtc-17). 116 từ vào (106 A, 10 C; hạng đã khóa 8.096–8.245); còn 2 dự bị. Sau thay: 7.776 từ, 7.776 khóa, F = 77, R1 = 0.
- **Nếu Q-rtc-O2 theo Astra cả 4 từ:** 120 ra, 118 vào, thiếu 2 ghế (Q-rtc-A2).
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

## 7. Lượt viết sạch giải nghĩa

Theo D1 và `huong-dan-giai-nghia.md:167–185`.

**Lô và lượt.**

- Một lô `rtc-lo-01` gồm mọi từ vào cộng dự bị đã chuẩn bị, xếp liên tiếp theo O1, không quá 400 từ. Với tập ra 101: 120 từ.
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
- Mục còn trượt thì nhường ghế cho dự bị đã viết trong cùng lô.
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
| `AT/labels.tsv` | Xóa dòng của từ ra. Đổi `trang_thai` của từ vào từ DU_PHONG sang CHINH, giữ nhãn và lớp; điểm và hạng S4 mới theo T-rtc-14. Thêm `K2` (và `H5` nếu có) vào `chu_ky_hai_ben` cho các từ được ký |
| `AT/nguon-goc-giai-nghia.tsv` | Từ ra: chuyển sang LOAI, ghi `cong_loai` (H7_K0, H7_K1, H5_c, H5_f…) và `dot_loai` = `ra-thay-chinh`. Từ vào: thêm dòng PHAT_HANH. Giữ 7.776 dòng PHAT_HANH |
| `AT/blocked_keys.tsv` | Khóa ASCII của mọi từ ra vì H7: K0 cho `phanbac`, `tinhkhi`; K1 cho các khóa K1; K2_CHUA_KY cho khóa K2 không đủ chữ ký; cột `nguon` = `H7_RA_THAY_CHINH`. Thêm `baotu` (K1, `nguon` = `T-dpv2-7`) |
| `AT/spelling_families.tsv` | Thêm họ đã chốt: họ LOAI của từ ra (c, f; CHO_LOAI cho bảy họ của T-rtc-13); họ QUA (8 H5b, *rong ruổi*, *trưng bày*); ghi đủ các dạng phân cách theo cách của dòng 258. Không đăng ký họ còn chờ khi từ chính của họ vẫn ở danh sách |
| `AT/du-phong.txt`, `AT/du-phong-phan-loai.tsv` | Bỏ các từ đã vào chính; cập nhật tầng và mã vấn đề; tính lại số đếm |
| `AT/honorable-mentions.tsv` | Không đổi, trừ khi Q-rtc-A2 được kích hoạt |
| `ho-so/unified/chu-ky.tsv` | Thêm dòng K2 và H5 của từng SA (`hieu_luc = CO`); `tep_goc` trỏ tới bảng ký của SA |
| `WordListAnalyze.md` | Đầu tài liệu (dòng 3–11): bản phát hành 2, số liệu tính lại, lượt `rtc`, số dư dự phòng, trỏ tới mục 13. Mục lục (dòng 26–37): thêm mục 13. Mục 3: thêm quyết định của chủ dự án khi duyệt. Mục 10: sinh lại. Mục 11 (dòng 8649–8920): sửa 11.1, 11.2, 11.4, 11.5. Mục 12: chỉ sửa nếu A2 được kích hoạt. Mục 13 mới "Rà và thay danh sách chính (bản phát hành 2)": 13.1 Phạm vi và nguồn; 13.2 H5; 13.3 H7; 13.4 Từ đã thay; 13.5 Chữ ký; 13.6 Giải nghĩa từ vào; 13.7 Việc để sau |
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
| T-rtc-15 | 46 khóa H7 chờ: giữ 37 (29 K2 hai SA ký, 8 không đỏ); thay 6 (*chậm, cổng, mặt nước, thiếu, trán* K1; *niêu* K0); 3 khóa trình chủ dự án (Q-rtc-O2: *cần cù, tiền lương, triệu*) | SA-Opus + SA-Astra | 2026-11-21 | chờ commit |
| T-rtc-16 | 27 dòng H5 chờ: giữ 21 (khác từ, không lập họ hay qua theo số); thay *chun, thun* (H5e rồi c) và *tép riu* (c, thiếu dữ liệu); khép 3 dòng đã ra hay không vào (*lằng nhằng, xà bông, qua quýt*) | SA-Opus + SA-Astra | 2026-11-21 | chờ commit |
| T-rtc-17 | 8 cờ từ vào: giữ 6 (*thay lông* K2 hai SA ký; *xoành xoạch, thụp, loáng thoáng, xầm xì* khác từ; *mang máng* không đỏ); không nhận *làm cỗ* (K1) và *rướn* (c, thiếu dữ liệu) | SA-Opus + SA-Astra | 2026-11-21 | chờ commit |
| T-rtc-18 | Gói K2: hai SA ký 204 trong 205 khóa (193 cũ, 4 của T-rtc-12, 7 của D-rtc-6); *bạn thân* trình chủ dự án (Q-rtc-O2). Cùng 29 khóa của T-rtc-15 và *thay lông*, hai SA có 234 chữ ký chung | SA-Opus + SA-Astra | 2026-11-21 | chờ commit |

Các mục T-rtc-* là chỗ hai bên đã đồng ý qua rà chéo, hai lượt duyệt và hai vòng thỏa thuận (`ho-so/{opus,astra}/ra-thay-chinh/thoa-thuan-*`). SA-Astra xác nhận khi duyệt bản sửa này.

## 12. Mục mở

| ID | Nội dung | Đường xử lý | Chặn Final |
|---|---|---|---|
| OI-RTC-O2 | 4 từ còn lệch sau khép mục mở: *cần cù, tiền lương, triệu, bạn thân* | Q-rtc-O2, chủ dự án quyết | Có |
| OI-RTC-A2 | Sức chứa: 2 dự bị nếu theo Opus ở Q-rtc-O2, thiếu 2 ghế nếu theo Astra; không có đệm cho D6/D7 | Q-rtc-A2, chủ dự án quyết | Có |
| OI-RTC-P6 | Thứ tự chọn theo T-rtc-14 | Tính lại trên tập ra cuối bằng hai chương trình độc lập (T7) | Có |
| OI-RTC-K2-KY | Ghép 234 chữ ký K2 chung của phiếu khép mục mở vào `chu-ky.tsv`, cộng các khóa chủ dự án cho giữ ở Q-rtc-O2 | Gói phát hành; kiểm gói chữ ký (mục 10) | Có |

**Đã khép:** OI-RTC-H7-S1 (T-rtc-12, D-rtc-6); OI-RTC-H5-LOAI (T-rtc-13); OI-RTC-H7-CHO và OI-RTC-HND (T-rtc-15; Astra tái ghép đủ 238/238 dòng); OI-RTC-H5-QH và OI-RTC-H5E (T-rtc-16); OI-RTC-VAO (T-rtc-10, T-rtc-17); OI-RTC-H5F (T-rtc-9).

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
- **Chủ dự án:** Q-rtc-A2, Q-rtc-A3 khi kích hoạt (mục 12.2); mọi đổi luật hay đổi quyết định của chủ dự án. *gián* không mở lại.

### 12.2. Câu hỏi dự phòng cho chủ dự án

Q-rtc-A2 đã kích hoạt và nằm ở `ra-thay-chinh-cau-hoi.md` (khép mục mở 1 để lại 2 dự bị, hoặc thiếu 2 ghế). Q-rtc-A3 chưa kích hoạt.

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

- B1: chủ dự án duyệt danh sách ra và vào cuối cùng.
- B2: không còn cách đọc không dấu nào ở nhóm đỏ chưa phân xử trên các khóa của bản phát hành.
- B3: không còn từ chính nào thuộc họ H5 trượt hoặc đang chờ.
- B4: mỗi từ mới có giải nghĩa viết sạch, đạt D6/D7.
- B5: tài liệu nêu đúng từ đã thay và lý do.

**Kỹ thuật:**

- T1: hai bộ kiểm (bản LF) và `build --check` báo 0 lỗi.
- T2: mọi khóa của từ ra vì H7 và `baotu` có trong `blocked_keys.tsv`.
- T3: các họ mới có trong `spelling_families.tsv`; C5 đạt; kiểm họ H5 độc lập (tách " / ") đạt.
- T4: `labels.tsv` có 7.776 dòng CHINH, F ≤ 77, R1 = 0. Kiểm gói chữ ký đạt: mọi K2 giữ lại có hai dòng ký hiệu lực trong `chu-ky.tsv`.
- T5: `--phat-hanh` báo 0 LỖI; D6 PASS 7.776/7.776 với đủ năm nguồn ghim. D7 có ý kiến của cả hai SA, phần chồng chéo ít nhất max(15, ⌈0,10 × N⌉) từ.
- T6: D8 khớp một-một với danh sách: 7.776 dòng PHAT_HANH, từ ra là LOAI.
- T7: hai chương trình độc lập, theo phương pháp T-rtc-14, cho cùng tập vào, cùng thứ tự và cùng dự bị sẽ dùng.
- T8: dự phòng, HM, `manifest.json` và các mục tài liệu khớp tập thực.
- T9: soát toàn tập sau khi thay (A9). Mọi cách đọc cùng khóa trong DOC_KHAC, HND và đầu mục Kaikki đã có phán quyết, gồm:
  - K0 bất kể tần suất;
  - cách đọc về tự hại, bạo lực, tình dục rõ dưới mốc còi;
  - mọi cách đọc có còi.
- T10: repo không chứa câu của kho, danh sách HND hay lời Wiktionary.

## 14. Rủi ro

| Rủi ro | Cách giảm |
|---|---|
| Từ vào ít gặp hơn nhiều: trung vị 0,0729 PPM so với 1,804 PPM của từ ra (tập 107) | S4 là luật đã ký; chủ dự án thấy đủ danh sách trước khi duyệt |
| Sau khép mục mở chỉ còn 2 dự bị (hoặc thiếu 2 ghế nếu Q-rtc-O2 theo Astra); trượt D6/D7 sẽ làm thiếu ghế | Khép OI-RTC-H7-CHO và OI-RTC-VAO trước Final; tính lại sức chứa; thấy thiếu là hỏi Q-rtc-A2 ngay, kể cả trước Final |
| Kaikki đổi bản trước khi chạy D6 | Giữ bản đã kiểm băm ngoài repo; chỉ hỏi Q-rtc-A3 nếu bản ghim mất |
| Lỗi nền CRLF làm sai kết quả bộ kiểm hoặc D6 | Bộ kiểm chạy trên bản LF; D6 chạy trong vùng riêng đúng byte ghim; lưu log |
| Bộ ghép phiếu đọc sai mã | Bảng ánh xạ đủ mã, mã lạ làm script dừng; cột tệp:dòng để soát |
| Bản quyền | Chỉ lưu số đếm, khóa, nhãn, revision. Kho, HND và Kaikki chỉ để ngoài repo, xóa sau khi dùng (trừ bản Kaikki ghim) |

## 15. Giai đoạn và ước lượng

| Giai đoạn | Việc | Lượt agent |
|---|---|---|
| 1 | Astra duyệt bản sửa này (lượt 3); Opus sửa nếu cần | 1–2 lượt SA |
| 2 | Đã xong: hai SA thỏa thuận S1, S2, S3 (`thoa-thuan-1`, `thoa-thuan-2`; T-rtc-12 đến T-rtc-14); chủ dự án trả lời Q-rtc-O1 (D-rtc-6, `0253bb0`) | Xong |
| 3a | Đã xong: hai SA khép mục mở (`khep-muc-mo-1` của hai bên; T-rtc-15 đến T-rtc-18). Gửi Q-rtc-O2 và Q-rtc-A2 cho chủ dự án | 1 lần hỏi chủ dự án |
| 3b | Áp Q-rtc-O2 và Q-rtc-A2 (chu kỳ HM có giới hạn nếu được duyệt: chọn, kiểm H1–H9); tính lại S4 theo T-rtc-14; tính lại tập ra và sức chứa. Hai chương trình chọn (T7). Kế hoạch Final; chủ dự án duyệt | 2–4 lượt SA; 1 lần hỏi chủ dự án |
| 4 | Viết `rtc-v1`, D2/D5/D6, D7, viết lại tối đa hai lượt. Trượt D6/D7 làm thiếu ghế thì hỏi Q-rtc-A2 | 1–3 lượt viết; 2–6 lượt SA |
| 5 | Dev-Sonnet: (a) tác vụ chuẩn bị: gói chữ ký, đăng ký họ, khóa chặn, hai kiểm độc lập; (b) commit phát hành: dữ liệu, khối sinh, tài liệu, manifest; (c) soát toàn tập (T9) | 3–4 lượt dev; orchestrator kiểm và commit |
| Tổng | | Khoảng 9–19 lượt còn lại |

## 16. Tham chiếu

- `ho-so/unified/ra-thay-chinh-yeu-cau.md`;
- `TC` (mục 0 dòng 12; H5 103–135; H6 137–154; H7 156–169; H9 180–194; Q 195–203; D7 307; P6/P7 402–427; bảng phân xử 520–527);
- `huong-dan-giai-nghia.md:167–185`;
- `check_wordlist.py:120–137`;
- `d6-kiem.py:371–378, 528–531, 545–560`; `d6-tham-chieu.json`;
- `ho-so/unified/chu-ky.tsv`, `canh-bao-khong-dau.tsv`, `xep-hang.tsv`, `p6-tinh-doc-lap-astra.py`, `du-phong-v2-ke-hoach.md:415–432`;
- phân tích, rà chéo, duyệt nháp trong `ho-so/{opus,astra}/ra-thay-chinh/`.
