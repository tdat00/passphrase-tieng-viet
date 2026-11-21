# Rà và thay danh sách chính — phân tích độc lập vòng 1 (SA-Opus)

**Ngày:** 21/11/2026. **Nhánh:** `analyze/ra-thay-chinh`, gốc `1c3f504`. **Người viết:** SA-Opus. Chưa đọc hồ sơ `ra-thay-chinh` của SA-Astra.

Nhãn chứng cứ: **[đã kiểm]** là số hay sự kiện mà Opus đã đọc trực tiếp hoặc chạy lại trong repo và nguồn ghim; **[giả định]** là phán đoán của Opus, cần SA-Astra đối chiếu. Mọi script, log và bảng nằm trong thư mục này; file sản phẩm chỉ được đọc.

## 1. Tóm tắt

1. Đề xuất thay **38 từ chính** theo đúng luật đã ký: 30 vì H7 K1 (16 rõ, 14 giáp ranh) và 8 vì H5. Có thêm 4 ca H5 cần hai chữ ký; nếu không ký thì phải thay 42 từ.
2. Từ vào là 38 mục kế tiếp theo S4 trong dự phòng, đều tầng A, ngăn OK không-F. F đã đủ 77 và R1 = 0 nên mọi ghế đều là ghế OK không-F. Mỗi từ vào cần một lượt viết sạch mới, rồi D2/D5/D6/D7/D8.
3. 96 từ chính cần hai chữ ký K2 "không tự động chặn"; Opus đề xuất ký cả 96, mỗi dòng có lý do. 5 từ đã có hai chữ ký K2 từ trước.
4. Ca báo tử: không từ chính nào có khóa `baotu`; đề xuất ghi `baotu` K1 vào `blocked_keys.tsv` theo T-dpv2-7. Ca *bình*/*bĩnh* đã có hai chữ ký K2 nên không mở lại.
5. Đã đếm lại H5 trên hai kho (SHA-256 khớp manifest) và tra Wiktionary. Thấy thêm 8 cặp i/y của từ chính (đều qua) và một lỗi xếp tầng dự phòng: *qua quýt* trượt H5b.
6. Nguyên nhân sót H7: bộ sinh còi cũ chỉ khớp từ vựng âm tiết hay khóa tục, không xét nghĩa của cả cách đọc. Vì vậy *chủ nghĩa*, *thiên tai*, *sán dây* chưa từng được đọc.
7. Rủi ro chính: từ vào ít gặp hơn nhiều (trung vị 0,073 PPM, so với 0,748 PPM của từ ra). Ngoài ra, 14 ca K1 giáp ranh và cách xếp loại c/d có thể không khớp với Astra.
8. Không có câu hỏi chặn. Khi duyệt kế hoạch, chủ dự án duyệt luôn danh sách thay và giả định không bù dự phòng (205 → 167).
9. Ước lượng 11–21 lượt agent, thường khoảng 15: 4–6 lượt SA phân tích, 0–2 lượt ký, 1–3 lượt viết, 2–6 lượt soát D7, 3 lượt dev.

## 2. Hiểu yêu cầu

- **Mục tiêu** [đã kiểm: `analyzing-tools/ho-so/unified/ra-thay-chinh-yeu-cau.md:7`, `:13–15`]: thực hiện đầy đủ D-dpv2-5. Phạm vi gồm họ *chòng chành*/*tròng trành*, ca báo tử, sàng lọc 632 cặp H5 và 1.177 cặp H7, và thay từ chính nếu cần. Chỉ được thay sau khi kế hoạch Final và chủ dự án duyệt, kèm giải nghĩa viết mới đạt D6/D7. Không có việc nào khác ngoài D-dpv2-5.
- **Người dùng:**
  - người dùng app sinh passphrase, gõ có dấu hay không dấu (`index.html`);
  - người đọc tài liệu (`thong-tin.html`, `WordListAnalyze.md`);
  - chủ dự án, người duyệt danh sách thay.
- **Ràng buộc:**
  - các luật đã ký: H1–H9, Q1–Q4, S4, D1–D8, P6–P8 (`analyzing-tools/tieu-chi-thong-nhat.md`);
  - quyết định 1, 8 và 10 của chủ dự án (`WordListAnalyze.md:146`, `:153`, `:155`);
  - không tạo thư mục tài liệu mới; kết quả cuối ghi thẳng vào tài liệu có sẵn (`ra-thay-chinh-yeu-cau.md:23`).
- **Giả định:**
  - **G-1** [giả định]: "giải nghĩa viết mới" nghĩa là mỗi từ vào có câu của một lượt viết sạch mới. Không dùng lại câu lịch sử P7 của dự phòng; câu lịch sử chỉ còn là tham chiếu cho D6.
  - **G-2** [giả định]: không bù dự phòng. 38 từ vào rời dự phòng, còn 167 từ. Quyết định 10 đã phát hành mà không chờ đủ 300 dự phòng (`WordListAnalyze.md:155`). Chủ dự án duyệt điểm này khi duyệt kế hoạch.
  - **G-3** [giả định]: luật H5/H7 không đổi. Mốc r ≥ 0,2 cho K1 (mục 5.2) chỉ là cách người duyệt áp K1, neo theo tiền lệ *bao tử*/*báo tử* (T-dpv2-7, r = 0,23). Vì tiêu chí không đổi, `thong-tin.html` mục "Quy tắc chọn từ" giữ nguyên.
  - **G-4** [giả định]: bốn họ H5 mới chỉ chạm dự phòng tầng D (*hì hụi*, *nhão nhẹt*/*nhão nhoẹt*, *chọc lét*, *chán phèo*), không đụng danh sách chính. Theo lời chủ dự án, không đăng ký chúng ở đợt này. Riêng họ *chòng chành*/*tròng trành* đụng danh sách chính nên phải đăng ký.

## 3. Hiện trạng và chứng cứ

| # | Sự kiện | Chứng cứ |
|---|---|---|
| 3.1 | 7.776 từ chính: 480 từ một âm tiết, 7.033 từ hai âm tiết, 263 từ ba âm tiết; 77 từ lớp F (đúng trần Q3), R1 = 0 | [đã kiểm] `analyzing-tools/labels.tsv`, `evidence/de-xuat-thay.log` |
| 3.2 | C5 báo lỗi khi từ chính trùng một khóa bị chặn. C5 cũng báo lỗi khi từ chính thuộc họ `LOAI*`, `CHO_LOAI`, `CHO_NGHIA` hay `CHO_SAT_NGUONG`, hoặc thuộc họ `*THIEU_DU_LIEU*` mà `labels.tsv` chưa ghi chữ ký `H5` | [đã kiểm] `analyzing-tools/check_wordlist.py:120–137` |
| 3.3 | Bảng còi `canh-bao-khong-dau.tsv` có 227 dòng. Cột `tu_vung_do` cho thấy còi chỉ bật theo từ vựng âm tiết hay khóa: AM_TIET_NHAY_CAM 69, AM_TIET_TUC 7, KHOA_TUC_ASTRA 30, TU_DO 15, 38 dòng tổ hợp, 68 dòng không mã. Cách đọc có nghĩa đỏ ở mức cả cụm (*chủ nghĩa*, *tai họa*, *sán dây*) nên lọt qua | [đã kiểm] `analyzing-tools/ho-so/unified/canh-bao-khong-dau.tsv` |
| 3.4 | `chu-ky.tsv` có 2.547 dòng dữ liệu: H3 2.369, K2 96 (thêm 1 dòng đã rút), H8 50, H5 31. 24 từ chính đã có K2 trong `labels.tsv`, trong đó có *bình*. Hai bên đã ký *bĩnh* với đúng lý do K0 mà Opus định nêu | [đã kiểm] `analyzing-tools/ho-so/unified/chu-ky.tsv:134–135` |
| 3.5 | `blocked_keys.tsv` có K0 43, K0;K1 1, K1 58, K2_CHUA_KY 8. Chưa có `baotu`, dù T-dpv2-7 đã xếp K1 | [đã kiểm] `analyzing-tools/blocked_keys.tsv`; `analyzing-tools/ho-so/unified/du-phong-v2-ke-hoach.md:422` |
| 3.6 | `spelling_families.tsv` có 277 họ. Chưa có họ nào cho 8 từ H5 trong mục 5.3 | [đã kiểm] |
| 3.7 | 205 dự phòng chia tầng: A148 (109 OK không-F, 39 OK F), B36 (F), C15, D6. Mục không-F đầu tiên ngoài danh sách chính đứng ở hạng S4 8.096 (*mụ mị*) | [đã kiểm] `analyzing-tools/du-phong-phan-loai.tsv`, `analyzing-tools/ho-so/unified/xep-hang.tsv` |
| 3.8 | Đầu vào sàng lọc: 632 cặp H5 trên 474 từ, 1.177 cặp H7 ≥ 0,3 PPM ngoài bảng còi, 1.888 dòng DOC_KHAC < 0,3 PPM của khóa chính. 323 từ lô L2/L3 không có dòng nào trong `opus-counts.tsv` | [đã kiểm] `ho-so/opus/du-phong-v2/evidence/bien-the-chinh-tho.tsv`, `ho-so/opus/du-phong-v2/evidence/pham-vi-hau-kiem-h7.tsv`, `evidence/h7-hnd-cung-khoa.log` |
| 3.9 | Kho đếm lại: OpenSubtitles v2018 vi (5.126.239 dòng) và CCAligned v1 vi (10.943.350 dòng khác nhau). Bốn danh sách HND ở bản ghim `688b095`. Mọi SHA-256 khớp `manifest.json` | [đã kiểm] `evidence/dem-h5.log`, `evidence/h7-hnd-cung-khoa.log` |
| 3.10 | Quy trình viết sạch: mỗi lượt là một agent cách ly; lô tối đa khoảng 400 từ theo O1; lượt viết lại chỉ nhận đầu mục và chẩn đoán; mục trượt sau hai lượt viết lại thì thay bằng dự phòng | [đã kiểm] `analyzing-tools/huong-dan-giai-nghia.md:167–185` |

## 4. Phương án

| Phương án | Nội dung | Chi phí | Rủi ro | Ảnh hưởng tới người dùng |
|---|---|---|---|---|
| **A (đề xuất)** | Áp đủ luật: thay 38 từ (30 K1, 8 H5), ký 96 K2, ký hoặc thay 4 ca H5 điều kiện | Một lô viết sạch khoảng 54 từ, khoảng 200 chữ ký, 3 tác vụ dev | Bất đồng với Astra về 14 ca giáp ranh | 38–42 từ đổi; không còn cách đọc không dấu thuộc nhóm đỏ ở các khóa đã soát |
| B | Chỉ thay 8 ca H5 và 16 ca K1 rõ (24 từ); 14 ca giáp ranh chuyển sang K2 và ký | Như A, bớt 14 câu | Trái ví dụ H6 (*chỉ huy*, *hậu bị* thuộc G1; *xấu xí*, *giả dối* thuộc G9; `tieu-chi-thong-nhat.md:143–151`) | 24 từ đổi |
| C | Chỉ thay *chòng chành*, ghi các phát hiện khác thành việc mở | Thấp | Không đáp ứng yêu cầu "rà đầy đủ, thay nếu cần" | 1 từ đổi |

Hai lựa chọn phụ:

- **Giải nghĩa:**
  - **G1 (đề xuất):** lượt viết sạch mới, đúng lời chủ dự án "viết mới".
  - G2: dùng lại câu lịch sử P7 của dự phòng tầng A rồi soát lại; rẻ hơn, nhưng có thể không đạt "viết mới".
- **Dự phòng:**
  - **R-a (đề xuất):** không bù; dự phòng còn 167 từ.
  - R-b: bù theo P6 bằng các mục kế tiếp ngoài dự phòng; tốn thêm phân tầng và giải nghĩa cho khoảng 40 từ mới.

## 5. Kế hoạch đề xuất

### 5.1. Sàng lọc H5: cách làm và kết quả

- **Số đếm** [đã kiểm]: `evidence/dem-h5.py` đếm 986 dạng của 632 cặp trên hai kho, theo ranh giới của `ho-so/opus/h5/recount_h5.py`:
  - ghép âm tiết liền nhau trong đoạn không dấu câu;
  - chuẩn hóa vị trí dấu thanh;
  - bỏ lượt "nghi vắt từ" của dạng nhiều âm tiết;
  - phụ đề đếm mọi dòng và đếm dòng khác nhau để xét độ nhạy; web đếm dòng khác nhau.

  Với từ hai âm tiết, số đếm gần khớp `opus-counts.tsv` (ví dụ *an tâm* 141/1.125 so với 141/1.131). Với cặp một âm tiết, script dùng số sạch của `opus-counts.tsv`, vì `dem-h5.py` không trừ lượt nằm trong từ ghép.
- **Cùng từ hay khác từ** [giả định, có chứng cứ]: Opus đọc cả 632 cặp. 600 cặp là khác từ (khác nghĩa hoặc khác hình vị). 5 cặp đã đăng ký. 27 cặp được coi là cùng một từ.
  - Ngữ cảnh đọc ngoài repo xác nhận cùng nghĩa cho *lấn áp*, *lay hoay*, *già giặn* và *xu hào*.
  - Wiktionary xác nhận khác nghĩa cho *long tong*, *lỏa tỏa* và *y trang*.
  - *bóng láng*/*bóng loáng* (cả hai đều là từ chính) được xếp khác từ: hai hình vị khác nhau, Wiktionary có hai mục riêng và không mục nào ghi là cách viết khác.
- **Loại c/d** [giả định, theo `tieu-chi-thong-nhat.md:115–117`, `:124–127`]:
  - **c/f** khi Wiktionary tiếng Việt ghi dạng kia là cách viết khác hoặc "như" dạng chính, hoặc khi đó là một cách Việt hóa khác của từ mượn;
  - **d** khi dạng kia chỉ có trong HND 39K/74K, vì hai danh sách lớn này có cả lỗi viết (*theo rõi* trong 39K, *chưng bày* trong 11K);
  - Opus đã tra Wiktionary qua API ngày 21/11/2026 và chỉ ghi nhãn, không ghi lời định nghĩa.

| Kết luận | Số cặp | Từ chính |
|---|---|---|
| THAY: c/f thiếu dữ liệu (một kho < 20 lượt) | 7 | *chòng chành* (tròng trành, phụ đề 3+2), *bồ kết* (bồ kếp, 1+0), *rau dền* (rau giền, 0+0), *ngoảnh* (ngảnh, 3+1), *phấp phới* (phất phới, 7+1), *già dặn* (già giặn, web 4+1), *cải xoong* (cải soong, f, 4+0) |
| THAY: d, lỗi ≥ 10% ở kho đủ dữ liệu | 1 | *lấn át*: lấn áp chiếm 10/75 lượt phụ đề (13,3%), độ nhạy 9/64 |
| Điều kiện: d, không kho nào đủ dữ liệu, cần hai chữ ký "không có chứng cứ lỗi" | 3 | *chơ vơ* (trơ vơ 0/0), *xập xình* (sập sình 0/0), *su hào* (xu hào 0 phụ đề, 1/13 web) |
| Điều kiện: d, CHO_SAT_NGUONG | 1 | *loay hoay*: lay hoay chiếm 3/20 lượt phụ đề (15%) theo mọi dòng, nhưng chỉ 18 dòng khác nhau; web 1/62 |
| QUA, đăng ký để không phải soát lại | 22 | 14 cặp d/c (*bảng hiệu*, *hạt dẻ*, *xà bông*, *thư giãn*, *rong ruổi*, *cột mốc*, *lòng vòng*, *nuốt chửng*, *theo dõi*, *thiện chí*, *trưng bày*, *co rúm*, *xù xì*, *rầm rộ*) và 8 cặp H5b mới (*cao quý*, *công ty*, *đá quý*, *quy luật*, *quy mô*, *quy tắc*, *quỹ đạo*, *quý phái*, đều ≥ 95% ở cả hai kho) |
| Không cho vào từ dự phòng | 1 | *qua quýt*/*qua quít*: H5b, phụ đề 2+0 → LOAI_THIEU_DU_LIEU; du-phong-v2 xếp tầng A là sai |

Opus đề xuất ký cả 4 ca điều kiện:

- *chơ vơ* và *xập xình*: không thấy lượt nào của dạng kia;
- *su hào*: 1/13 lượt, dưới 10%;
- *loay hoay*: hai trong ba lượt *lay hoay* ở phụ đề là cùng một câu của hai bản phụ đề; web chỉ 1/62.

Nguồn: [đã kiểm] `sang-loc-h5.tsv` (dòng 28, 41, 101, 113, 182, 291, 299, 349, 390, 405, 434, 616, 634–642), `evidence/dem-h5.tsv`, `evidence/dem-h5b.tsv`.

### 5.2. Sàng lọc H7: cách làm và kết quả

Luật Opus áp, theo `tieu-chi-thong-nhat.md:160–168` [giả định ở mốc r]:

- **K0:** cách đọc là từ tục, tình dục người lớn hoặc chỉ chất thải, có nguồn chứng thực. Áp bất kể tần suất.
- **K1:**
  - khóa có từ hai âm tiết;
  - cách đọc là một từ có thật mà nghĩa chính thuộc nhóm đỏ H6;
  - r = PPM(cách đọc khác) / PPM(từ chính) ≥ 0,2.
  - Mốc 0,2 neo theo T-dpv2-7: *báo tử*, r = 0,23 → K1. Tiền lệ *ngoại trú*, r = 0,034, là CHO.
  - **K1 giáp ranh:** nhóm đỏ chỉ đúng khi đọc chặt bảng ví dụ H6: G1 có *chỉ huy*, *hậu bị*; G3 có *quyền lực*; G9 có *xấu xí*, *thô lỗ*.
- **K2:**
  - khóa một âm tiết, vì cách đọc mặc định thường là một âm tiết khác (*nhau* chứ không phải *nhậu*), tức "chỉ khớp một âm tiết";
  - hoặc cụm phải tách ép;
  - hoặc nghĩa đỏ không chắc;
  - hoặc r < 0,2.
- **KHONG_DO:** cách đọc khác không thuộc nhóm đỏ.

| Nguồn cặp | Số dòng | K1 | K1 giáp ranh | K2 mới | K2 đã ký | Không đỏ / không còi |
|---|---|---|---|---|---|---|
| 1.177 cặp ≥ 0,3 PPM ngoài bảng còi | 1.177 | 17 (16 từ) | 14 | 103 | 7 | 1.036 |
| DOC_KHAC < 0,3 PPM có từ tự hại, bạo lực, tình dục rõ hay chất thải | 138 trong 1.888 | 0 | 0 | 1 (*đông đúc*/*động dục*) | 0 | 137 |
| Cách đọc cùng khóa trong HND nhưng DOC_KHAC không có (335 cặp của từ có số đếm; 39 cặp của 25 từ lô L2/L3) | 374 | 0 | 0 | 2 (*nghèo*/*nghẻo*, *đồ bạc*/*đổ bác*) | 0 | 372 |

Ghi chú:

- **Rút lại K0 *bình*/*bĩnh*.** Wiktionary ghi *bĩnh* là đại tiện. Nhưng P1 đã xếp ca này COI_H7 và hai bên đã ký K2 ngày 19/11/2026 với đúng lý do đó (`chu-ky.tsv:134–135`). Không có chứng cứ mới nên không mở lại.
- ***dại khờ*/*đái khó*** (PPM 0) xử theo cùng tiền lệ: hoạt động bài tiết không xếp K0; G5 dưới mốc 0,3 nên không bật còi.
- **K2 đã ký từ trước:** *bình*, *khảm*, *thầy*, *thổi*, *trứng* (`chu-ky.tsv`), không cần ký lại.
- **Phân bố 106 dòng K2 mới trên 97 từ:**
  - 35 dòng là cụm nhiều âm tiết, như *bố mẹ*/*bỏ mẹ* r 0,07, *bảo hành*/*bạo hành* 0,05, *hỏi thăm*/*hội thẩm* 0,175, *cổ vũ*/*có vú* (cụm tách ép);
  - 71 dòng là khóa một âm tiết: G1 9, G2 12, G3 3, G4 15, G5 16, G6 5, G7 4, G8 1, G9 4, G10 2.
  - Bỏ *nằm mơ*, vốn đã là K1, thì còn **96 từ** cần ký.

Nguồn: [đã kiểm] `sang-loc-h7.tsv`, `evidence/sang-loc-h7.log`, `evidence/h7-hnd-cung-khoa.tsv`.

### 5.3. Danh sách từ chính phải thay

Tất cả đều ở ngăn OK không-F.

| Mã | Từ chính → cách đọc hay dạng đối chứng (nhóm H6, r) | Dòng chứng cứ |
|---|---|---|
| K1 | *áo quần* → áo quan (G4, 0,33); *bàn ăn* → bản án (G2, 0,74); *chữ nghĩa* → chủ nghĩa (G3, 36,3); *dặn dò* → dẫn độ (G2, 3,72); *đậm đà* → đấm đá (G1, 0,21); *đầu mùa* → đậu mùa (G5, 1,34); *đỏ thắm* → do thám (G1/G2, 22,9); *giận dỗi* → gian dối (G9, 2,59) | `sang-loc-h7.tsv:4, 11, 217, 275, 307, 309, 329, 430` |
| K1 | *hố ga* → ho gà (G5, 1,22); *lằng nhằng* → lăng nhăng (G6, 1,27); *nằm mơ* → nấm mồ (G4, 0,45); *sắn dây* → sán dây (G5/G10, 34,9); *tài hoa* → tai họa (G8, 5,91); *thiên tài* → thiên tai (G8, 0,254); *thong dong* → thông đồng (G2, 6,86); *thư thái* → thụ thai (G6, 1,45) | `:482, 579, 665, 886, 903–904, 958, 970, 993` |
| K1 giáp ranh | *cao giá* → cáo già (G9, 0,45); *chung cư* → chứng cứ (G2, 1,44); *cổ thụ* → cố thủ (G1, 2,55); *di dời* → đi đời (G4, 0,34); *dò hỏi* → dở hơi (G9, 8,57); *gầy gò* → gây gổ (G1/G9, 0,92); *hóm hỉnh* → hợm hĩnh (G9, 2,37) | `:89, 206, 232, 286, 294, 402, 481` |
| K1 giáp ranh | *mê mẩn* → mê man (G5, 0,54); *nắm vững* → nằm vùng (G1/G3, 0,92); *phân công* → phản công (G1, 1,25); *phong thư* → phòng thủ (G1, 47,8); *thể lực* → thế lực (G3, 2,45); *tiền công* → tiến công (G1, 0,93); *tiếp viên* → tiếp viện (G1, 0,83) | `:638, 666, 806, 814, 952, 1013, 1018` |
| H5 | *chòng chành*, *bồ kết*, *rau dền*, *ngoảnh*, *phấp phới*, *già dặn*, *cải xoong*, *lấn át* | `sang-loc-h5.tsv:101, 28, 405, 349, 390, 182, 41, 291` |
| Điều kiện H5 | *chơ vơ*, *xập xình*, *su hào*, *loay hoay*: thay nếu không đủ hai chữ ký | `sang-loc-h5.tsv:113, 616, 434, 299` |

### 5.4. Từ vào theo ghế

Bảng đầy đủ: `de-xuat-thay.tsv`, cột `vai_tro`, `thu_tu`, `hang_S4`, `tang`, `soat_vao`.

- **Quy tắc** [đã kiểm: `analyzing-tools/ho-so/unified/p6-tinh-doc-lap-astra.py:59–104`]:
  - ghế trống nhận mục kế tiếp theo S4 (OK trước R1, điểm giảm dần, ít chữ cái trước, rồi O1) mà vẫn vừa hạn mức;
  - vì F = 77, các mục F bị bỏ qua (76 mục);
  - các mục bị loại khi lấp: tầng D (3 mục), hai cổng còn mở (*loằng ngoằng*, *ngoại trừ*; 1 mục trong khoảng đã duyệt) và *qua quýt* (H5b).
- **38 từ vào**, theo hạng S4 từ 8.096 đến 8.138, đều tầng A: *mụ mị, cờ vây, đưa đò, buồn thiu, xuống cân, phất phơ, tấn tới, leo dây, cụt hứng, nín thinh, khó nghĩ, số âm, bâng quơ, lạ tai, làm cỗ, mỏi nhừ, oái oăm, mon men, chính cống, gợi chuyện, bụng dạ, mấp mé, rơm rớm, sáng trưng, nhá nhem, nhảy sào, chốc nữa, hay dở, đủng đỉnh, mong nhớ, thay lông, giở giọng, đon đả, ủn ỉn, xúng xính, ăn tiệm, bèo bọt, leo lét*.
- **Vào nếu 4 ca điều kiện phải thay:** *đáp số, đỏ chót, ve vẩy, dài ngoằng*.
- **Dự bị** cho mục trượt giải nghĩa sau hai lượt viết lại: *giở quẻ, lộp độp, tía lia, khuya khoắt, khúc khuỷu, xoành xoạch, học tủ, lạ đời, thụp* (tầng C), *gặp thời, chung tình, ỉu xìu*.
- **Soát từ vào** [đã kiểm số; nghĩa: giả định]:
  - Cách đọc DOC_KHAC ≥ mốc chỉ có ba cặp, đều không đỏ: *đưa đò* → dưa đỏ 0,17; *làm cỗ* → làm cỏ 0,63; *thay lông* → thay lòng 0,31.
  - Không có cách đọc HND cùng khóa nào thuộc danh sách đỏ.
  - Không có biến thể H5b trong HND.
  - Phép soát toàn tập ở nghiệm thu A9 vẫn phải chạy lại sau khi viết.

### 5.5. Chữ ký

- **K2:** 96 từ, hai chữ ký mỗi từ.
  - Opus đề xuất ký "không tự động chặn" cả 96; lý do theo từng dòng ở cột `ly_do` của `sang-loc-h7.tsv`.
  - Mỗi SA ghi một bảng ký trong thư mục `ra-thay-chinh` của mình.
  - Khi thực hiện, thêm vào `ho-so/unified/chu-ky.tsv` 192 dòng (`loai_ky = K2`, `hieu_luc = CO`) và ghi `K2` vào `labels.tsv`, cột `chu_ky_hai_ben`.
  - Từ nào không đủ hai chữ ký thì không được ở lại (Q4 = 0, `tieu-chi-thong-nhat.md:202`). Khi đó lấy tiếp mục dự bị ở mục 5.4.
- **H5:** 4 ca điều kiện. Ghi `H5` vào `chu_ky_hai_ben` cho *chơ vơ*, *xập xình*, *su hào*; điều kiện là C5 với họ `QUA_RIENG_H5_THIEU_DU_LIEU`. Với *loay hoay*, hai bên đọc thêm rồi ký, sau đó đổi họ thành `QUA_RIENG_H5`.

### 5.6. Thiết kế lượt viết giải nghĩa

Theo `huong-dan-giai-nghia.md:167–185`.

1. **Lô `rtc-lo-01`:** 54 từ (38 từ vào, 4 từ vào có điều kiện, 12 dự bị), xếp theo O1, dưới mức 400.
2. **Lượt `rtc-v1`:** một agent viết sạch mới.
   - Thư mục chỉ có hướng dẫn (bỏ mục 12), `kiem-tra-giai-nghia.py` và lô từ.
   - Không mạng, không repo, không có câu cũ.
3. **Kiểm tự động:** `python kiem-tra-giai-nghia.py rtc-lo-01.txt rtc-lo-01.tsv` để kiểm D2/D5. Sau khi ghép vào danh sách, chạy `python kiem-tra-giai-nghia.py --phat-hanh ...` để kiểm trùng toàn danh sách và cờ còn mở.
4. **D6:**
   - tải lại bản trích Kaikki viwiktionary và so SHA-256 với `manifest.json`; nếu khác thì ghi bản mới vào `d6-run.json`;
   - chạy `python d6-kiem.py --input <tệp tu/giai_nghia> --log d6-log.tsv --meta d6-run.json` (`README.md:92`).
5. **D7:** SA-Opus và SA-Astra soát độc lập; ghi `soat_noi_dung` theo dạng `astra:...;opus:...`.
6. **Viết lại:** tối đa hai lượt (`rtc-v2`, `rtc-v3`). Mỗi lượt là agent mới, chỉ nhận đầu mục và chẩn đoán. Mục trượt sau hai lượt thì nhường ghế cho dự bị kế tiếp; dự bị đã có câu trong cùng lô.
7. **D8:**
   - từ vào: dòng `PHAT_HANH` trong `nguon-goc-giai-nghia.tsv`, đủ các cột `luot_viet`, `lo`, `sha256_giai_nghia`, `d6_ket_qua`, `soat_noi_dung`, `co_khi_viet`, `dong_co`, `co_phat_hanh`;
   - từ ra: đổi thành `LOAI`, với `cong_loai` là `H7_K1` hay `H5` kèm loại, và `dot_loai = ra-thay-chinh`.

### 5.7. Tệp và mục phải sửa

Phải sửa trong cùng một commit để C5 không báo lỗi giữa chừng.

| Tệp | Sửa |
|---|---|
| `analyzing-tools/wordlist.txt` | Bỏ 38 dòng, thêm 38 dòng `từ\|giải nghĩa`; giữ thứ tự O1 và 7.776 dòng |
| `analyzing-tools/labels.tsv` | Xóa 38 dòng từ ra; đổi `trang_thai` của 38 từ vào từ DU_PHONG sang CHINH; thêm `K2` cho 96 từ; thêm `H5` cho các ca điều kiện đã ký |
| `analyzing-tools/nguon-goc-giai-nghia.tsv` | 38 dòng chuyển sang LOAI (LOAI từ 182 lên 220); 38 dòng PHAT_HANH mới (vẫn 7.776) |
| `analyzing-tools/blocked_keys.tsv` | Thêm 30 khóa K1 (`nguon = H7_RA_THAY_CHINH`) và `baotu` (K1, `nguon = T-dpv2-7`); K1 từ 58 lên 89 |
| `analyzing-tools/spelling_families.tsv` | Thêm 35 họ: 8 LOAI của từ ra (*chòng chành*/*tròng trành* là LOAI_THIEU_DU_LIEU), 4 họ điều kiện, 22 họ QUA, *qua quýt*/*qua quít* LOAI_THIEU_DU_LIEU |
| `analyzing-tools/du-phong.txt`, `analyzing-tools/du-phong-phan-loai.tsv` | Bỏ 38 từ vào; *qua quýt* chuyển từ A sang D (mã `H5`); còn 167 từ: A109, B36, C15, D7 |
| `analyzing-tools/honorable-mentions.tsv` | Không đổi. Không có H5b; từ ra trượt luật cứng nên không thành từ có thể cân nhắc |
| `WordListAnalyze.md` | Xem danh sách ngay dưới bảng |
| `analyzing-tools/README.md` | Dòng 77: "182 từ … ở P6 và P7" thành 220 từ, thêm đợt rà/thay. Dòng 81: thêm `rtc-v1`…`rtc-v3`. Dòng 92: ghi lần chạy D6 mới. Cập nhật mọi số đếm khóa và họ được nêu |
| `analyzing-tools/manifest.json` | SHA-256 mới của mọi tệp đã sửa, siêu dữ liệu D6, bản phát hành 2 |
| `analyzing-tools/ho-so/unified/chu-ky.tsv` | 192 dòng K2 và tối đa 8 dòng H5; `tep_goc` trỏ tới bảng ký của từng SA |
| `index.html`, `thong-tin.html` | Chỉ khối `#wordlist`, do `build_wordlist.py` sinh lại; mục "Quy tắc chọn từ" giữ nguyên (G-3) |

Các sửa trong `WordListAnalyze.md`:

- **Đầu tài liệu:**
  - dòng 3: "Bản phát hành 2. Cập nhật ngày …";
  - dòng 5: tính lại số liệu (dự kiến 479/7.034/263 âm tiết, độ dài trung bình);
  - dòng 8: thêm lượt `rtc`;
  - dòng 9: "Dự phòng: 167 từ (205 − 38 đã dùng)";
  - thêm một gạch đầu dòng trỏ tới mục 13.
- **Mục lục:** thêm dòng 13.
- **Mục 3:** thêm quyết định 11 khi chủ dự án duyệt.
- **Mục 10:** sinh lại bằng script.
- **Mục 11:** sửa 11.1, 11.2 (bảng tầng và bảng cảnh báo có thêm *qua quýt*), 11.4 và 11.5.
- **Mục 13 mới**, tên "Rà và thay danh sách chính (bản phát hành 2)", gồm:
  - 13.1 Phạm vi và nguồn;
  - 13.2 Kết quả H5;
  - 13.3 Kết quả H7;
  - 13.4 Từ đã thay;
  - 13.5 Chữ ký mới;
  - 13.6 Giải nghĩa của từ vào;
  - 13.7 Việc để sau.

### 5.8. Tương thích bộ kiểm

- **Giữ nguyên các mốc mà bộ kiểm đọc:**
  - `check_wordlist.py` (N = 7776 ở dòng 20) và `verify.mjs` (dòng 41) đếm 7.776 dòng;
  - hai bộ kiểm và `build_wordlist.py` (dòng 20) tìm tiêu đề "## 10. Danh sách 7.776 từ phát hành".

  Thêm mục 13 sau mục 12 không chạm khối mục 10: lần du-phong-v2 đã thêm mục 11 và 12 mà bộ kiểm vẫn đạt.
- **C5:** từ ra rời `wordlist.txt` cùng commit với khóa K1 và họ LOAI mới. Ba họ `*_THIEU_DU_LIEU` cần chữ ký `H5` trong `labels.tsv`.
- **C6:** F = 77, R1 = 0, R2 = 0 không đổi, vì cả 38 ghế đều là ghế OK không-F.
- **Cách chạy:**
  - chạy `check_wordlist.py` và `verify.mjs` trên bản xuất LF của commit, vì checkout CRLF có lỗi nền C1/C8 đã biết (`README.md:61`);
  - chạy `build_wordlist.py --check` trên checkout CRLF.

### 5.9. Thứ tự thực hiện

1. Đối chiếu chéo với SA-Astra, hòa các điểm lệch, lập báo cáo chung và `plan.md`. Điểm nào không hòa được thì hỏi SA-Fable.
2. Hai SA ký K2 và H5 (mục 5.5). Chốt danh sách ra và vào.
3. Chủ dự án duyệt kế hoạch Final, gồm danh sách thay và G-2.
4. Viết lô `rtc-lo-01`, kiểm D2/D5/D6, soát D7, viết lại nếu cần, chốt 38 câu.
5. Dev-Sonnet sửa dữ liệu (mục 5.7), chạy `build_wordlist.py` và cả bộ kiểm.
6. Dev-Sonnet sửa tài liệu (`WordListAnalyze.md`, README, manifest).
7. Soát toàn tập lần cuối (A9). Orchestrator commit từng tác vụ.

## 6. Nghiệm thu

| # | Tiêu chí đo được | Cách kiểm |
|---|---|---|
| A1 | `wordlist.txt` có 7.776 dòng, không còn từ ra nào; 38 từ vào đều có giải nghĩa | `check_wordlist.py`, `verify.mjs` (bản LF) báo 0 lỗi; `build_wordlist.py --check` (CRLF) báo 0 |
| A2 | 30 khóa K1 và `baotu` có trong `blocked_keys.tsv`; không từ chính nào trùng khóa bị chặn | C5 |
| A3 | Có đủ 35 họ mới; không từ chính nào thuộc họ LOAI/CHO; họ thiếu dữ liệu có chữ ký H5 | C5 và đếm dòng |
| A4 | `labels.tsv` có 7.776 dòng CHINH, F = 77, R1 = 0; 96 từ có `K2`, khớp 192 dòng `chu-ky.tsv` có hiệu lực | C6; script đếm theo cặp (từ, người ký) |
| A5 | Mỗi từ vào có câu viết sạch mới và một dòng D8 PHAT_HANH; D6 PASS 7.776/7.776; D7 có ý kiến của cả hai SA; `--phat-hanh` 0 LỖI | `d6-kiem.py`, `kiem-tra-giai-nghia.py --phat-hanh`, đếm dòng D8 |
| A6 | Mỗi từ ra có dòng D8 LOAI, đủ `cong_loai` và `dot_loai` | Đếm 220 dòng LOAI |
| A7 | `du-phong.txt` và `du-phong-phan-loai.tsv` có 167 từ, chia A109/B36/C15/D7; không từ vào nào còn trong dự phòng | So hai tệp với `wordlist.txt` |
| A8 | `WordListAnalyze.md` có mục 13, mục lục, đầu tài liệu và mục 11 đã sửa; SHA-256 trong manifest khớp tệp | Đọc lại; script SHA-256 |
| A9 | Soát toàn tập sau khi thay: mọi cách đọc cùng khóa trong DOC_KHAC, HND74K và đầu mục Kaikki viwiktionary, nếu thuộc nhóm đỏ và ≥ 0,3 PPM hoặc ≥ PPM của mục, đều đã có K1, K2 hay "không tự động"; mọi biến thể H5 a–h của từ vào đã xét | Chạy lại `sang-loc-h7.py`, `sang-loc-h5.py` và `dem-h5.py` trên danh sách mới, cộng thêm đầu mục Kaikki |
| A10 | Repo không chứa câu của kho, danh sách HND, lời Wiktionary hay giải nghĩa cũ ngoài phần đã có | Soát diff; tệp tạm nằm ngoài repo và đã xóa |

## 7. Rủi ro và cách giảm

| Rủi ro | Cách giảm |
|---|---|
| Từ vào ít gặp hơn nhiều (trung vị 0,073 PPM, từ ra 0,748 PPM) | S4 là luật đã ký; chủ dự án thấy đủ danh sách trước khi duyệt; phương án B bớt 14 từ đổi |
| Bất đồng với Astra về 14 ca K1 giáp ranh, cách xếp c/d (ảnh hưởng *già dặn*, *co rúm*, *xù xì*, *rầm rộ* và ba ca d điều kiện) hay 96 chữ ký K2 | Mỗi dòng có lý do và số đo; bất đồng chuyển SA-Fable kèm hai lập trường. H9 cho bên kia phản biện một lần; không hòa thì không phát hành từ đó |
| Ký K2 hàng loạt thành ký chiếu lệ | Mỗi dòng có mã nhóm, r và lý do riêng; hai SA ký độc lập |
| Câu viết mới trượt D6/D7 | Dự bị đã viết trong cùng lô; tối đa hai lượt viết lại |
| Còn cách đọc đỏ chưa soát: đầu mục Wiktionary của 323 từ lô L2/L3 và của toàn danh sách | A9 dùng bản Kaikki tải cho D6 |
| Luật c thiếu dữ liệu loại cả dạng đang trội (*rau dền* 0/45, *rau giền* 0/0) | Áp đúng luật đã ký (tiền lệ *giòn tan*); ghi ở mục 13.7 để xét lại luật trong một yêu cầu khác |
| Lỗi nền CRLF làm hỏng kết quả bộ kiểm | Chạy trên bản xuất LF như du-phong-v2 |
| Bản quyền | Chỉ ghi số đếm, khóa, nhãn và lời của SA; kho, HND và ngữ cảnh nằm ngoài repo, xóa sau khi dùng |

## 8. Công sức và giai đoạn

| Giai đoạn | Việc | Lượt agent (ước lượng) |
|---|---|---|
| 0 | Phân tích độc lập (xong), đối chiếu chéo, báo cáo chung, các vòng duyệt kế hoạch | 4–6 lượt SA |
| 1 | SA-Fable cho điểm không hòa (qua chủ dự án); chủ dự án duyệt kế hoạch | 0–1 lượt SA-Fable, 1 lần hỏi chủ dự án |
| 2 | Ký K2 và H5 | 2 lượt SA (có thể gộp vào giai đoạn 0) |
| 3 | Viết `rtc-v1`, soát D7, viết lại tối đa hai lượt | 1–3 lượt viết, 2–6 lượt SA |
| 4 | Dev: dữ liệu; tài liệu; soát toàn tập A9 | 3 lượt Dev-Sonnet; orchestrator chạy cổng và commit |
| Tổng | | 11–21 lượt, thường khoảng 15 |

Chi phí đo: tải lại hai kho (61 MB và 404 MB, khoảng 2 phút mỗi lượt đếm trên 14 tiến trình) và bản Kaikki cho D6.

## 9. Câu hỏi

Không có câu hỏi chặn cho chủ dự án hay SA-Fable ở vòng này.

- **Chủ dự án duyệt khi duyệt kế hoạch** (không phải câu hỏi riêng):
  - danh sách thay ở mục 5.3–5.4;
  - giả định G-2: không bù, dự phòng còn 167.
- **Hỏi SA-Fable nếu hai SA không hòa**, nêu đủ hai lập trường:
  - 14 ca K1 giáp ranh;
  - cách xếp c/d theo Wiktionary hay HND;
  - 4 ca H5 điều kiện;
  - bất kỳ chữ ký K2 nào bị một bên từ chối.

## 10. Chỉ mục chứng cứ

Đường dẫn tính từ `analyzing-tools/ho-so/opus/ra-thay-chinh/`.

| Tệp | Nội dung |
|---|---|
| `sang-loc-h5.tsv` | 641 cặp (632 thô và 9 H5b): kết luận cùng/khác từ, loại, nhãn Wiktionary, số đếm, kết luận H5, hành động, lý do |
| `sang-loc-h7.tsv` | 1.689 dòng (1.177 PHAM_VI, 138 DUOI_NGUONG, 374 HND_THIEU): PPM, r, nhóm H6, đề xuất, lý do |
| `de-xuat-thay.tsv` | 38 RA, 4 DIEU_KIEN, 38 VAO, 4 VAO_NEU_DIEU_KIEN, 12 DU_BI: ngăn, điểm, hạng S4, tầng, soát từ vào, việc còn lại |
| `evidence/chung.py` | Hàm dùng chung (khóa, O1, đọc/ghi TSV CRLF) |
| `evidence/dem-h5.py`, `dem-h5.tsv`, `dem-h5.log` | Đếm 986 dạng trên hai kho; log ghi SHA-256 khớp manifest |
| `evidence/cap-h5b.tsv`, `dem-h5b.tsv`, `dem-h5b.log` | 9 cặp i/y và số đếm (`CAP_H5`, `RA_H5`) |
| `evidence/h7-hnd-cung-khoa.py`, `.tsv`, `.log` | Cách đọc cùng khóa trong HND mà DOC_KHAC chưa có; chỉ ghi 374 cặp cần đọc |
| `evidence/sang-loc-h5.py`, `sang-loc-h7.py`, `de-xuat-thay.py` và log | Luật và phán đoán của Opus dưới dạng dữ liệu; mô phỏng P6 |

Cách chạy lại, từ thư mục `evidence/`:

```powershell
$env:HND_DIR = '<ngoài repo>\hnd-tam'      # Viet11K/22K/39K/74K @688b095
$env:KHO_DIR = '<ngoài repo>\kho-tam'      # sub-vi.txt.gz, web-vi.txt.gz theo URL trong manifest
$env:NGU_CANH = '<ngoài repo>\ngu-canh-h5.json'
python h7-hnd-cung-khoa.py
python dem-h5.py
$env:CAP_H5 = "$PWD\cap-h5b.tsv"; $env:RA_H5 = 'dem-h5b'; python dem-h5.py
python sang-loc-h7.py; python sang-loc-h5.py; python de-xuat-thay.py
```

Nguồn ngoài repo đã dùng và đã xóa: hai kho OPUS, bốn danh sách HND, mẫu ngữ cảnh. Wiktionary tiếng Việt được tra ngày 21/11/2026, chỉ đọc: 37 đầu mục qua API và trang *bĩnh*. Commit gốc: `1c3f504`. Tiền lệ: T-dpv2-4, T-dpv2-7, D-dpv2-5 (`du-phong-v2-ke-hoach.md:415–422`).
