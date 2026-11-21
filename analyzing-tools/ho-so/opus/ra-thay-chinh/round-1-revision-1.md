# Rà và thay danh sách chính — nhật ký sửa lần 1 (theo duyệt nháp của Astra)

**Ngày:** 21/11/2026. **Gốc:** `1c3f504`, nhánh `analyze/ra-thay-chinh`. **Người sửa:** SA-Opus.

**Đầu vào:** `ho-so/astra/ra-thay-chinh/round-1-review-drafts.md` ("changes requested", R1–R8) và các phiếu `RD/rd1-*`. Mọi điểm đều kiểm lại trên dữ liệu repo, không chỉ dựa vào báo cáo của Astra.

**Viết tắt:** `RD` = `ho-so/astra/ra-thay-chinh/evidence/`; `OE` = `ho-so/opus/ra-thay-chinh/evidence/`; `U` = `ho-so/unified/`; `TC` = `tieu-chi-thong-nhat.md`.

**Tệp đã sửa:**

- `U/ra-thay-chinh-bao-cao-chung.md`, `U/ra-thay-chinh-ke-hoach.md` (giữ `Status: Draft (round 1)`), `U/ra-thay-chinh-cau-hoi.md`;
- `U/ra-thay-chinh-h7.tsv`, `U/ra-thay-chinh-h5.tsv`, `U/ra-thay-chinh-thay-the.tsv` (sinh lại);
- `OE/doi-chieu-v2.py`, `OE/de-xuat-thay-v2.py`, `OE/hop-nhat-rtc.py` (viết lại);
- tệp mới: `OE/cap-h5f.tsv`, `OE/dem-h5f.tsv`, `OE/dem-h5f.log`.

## 1. Đã áp dụng

| # | Yêu cầu của Astra | Việc đã làm | Kiểm [verified] |
|---|---|---|---|
| 1 | R1: bộ ghép H5 tạo 9 đồng thuận QUA giả | `hop-nhat-rtc.py` dùng bảng ánh xạ đủ mã cho mọi mã của Astra (v1, cr1, rd1, H5b); mã lạ làm script dừng. Bảng H5b cũng không còn gán QUA cho dòng KHONG_THUOC_b | DONG_THUAN_QUA từ 19 xuống 11 (10 cũ cộng *bít tết*); 9 cặp về CHO_CAN_CU |
| 2 | R2: H7 phải dùng phiếu sau duyệt; bỏ `cap_lech` tự mâu thuẫn; không cắt lý do; thêm tệp:dòng | Cột hiện hành `opus`, `astra`; cột lịch sử `opus_v1`, `astra_v1`, `astra_cr1`; bỏ `cap_lech`; lý do đủ; cột `nguon_opus`, `nguon_astra` ghi tệp:dòng | Trước khi Opus đổi lập trường: đúng 67 đồng thuận thay, 30 tranh chấp, 46 chờ, 7 giữ theo chữ ký cũ như Astra nêu |
| 3 | R3: sức chứa, trung vị, quan hệ tập vào | Ghi 120 (108 A, 12 C), gọi là nguồn sau lọc sơ bộ; *ngoại trừ* là OK-F nên không trừ. Trung vị ghi theo mẫu. Ghi giao 23/24 với kịch bản cũ của Astra | Trung vị tập 87: từ ra 1,706275071, từ vào 0,076191870, khớp `RD/rd1-audit-summary.json`. Tám mục cuối khớp `unprepared_tail` của Astra |
| 4 | R4: vòng chọn không cập nhật hạn mức; ghép ghế sai ngăn | `de-xuat-thay-v2.py` chọn theo vòng lấp của `choose()` (`U/p6-tinh-doc-lap-astra.py:83–88`): nhận mục khi F ≤ 77 và R1 ≤ 388 sau mỗi lần nhận. Bảng thay không còn ghép đôi từ ra với từ vào theo dòng. Nghiệm thu F ≤ 77 | Nhánh thêm *theo*: 102 ra, 102 vào, 7.776 từ, 7.776 khóa, F = 77 (trước đây F152 và 7.775 từ) |
| 5 | R4: cờ còi của từ vào không thêm r; H5b đúng hợp đồng | Cờ còi chỉ dùng PPM ≥ 0,3 hoặc ≥ PPM của mục; hàm H5b chỉ đổi âm tiết có vần đúng bằng i hoặc y (`U/tap-luat-P2-v4.json:575`) | 9 cờ trong từ vào, 2 cờ trong dự bị |
| 6 | R5: cùng tập 87 không chứng minh cùng thứ tự | Q-rtc-S3: điều kiện gửi gồm lệch tập, lệch thứ tự hay lệch dự bị; không còn ghi "phương án 2 cùng kết quả"; T7 so cả ba | Các chỗ đổi trong `S4_O87` của Astra ở vị trí ≤ 73 và 104/105, không cắt qua ranh 101/102 |
| 7 | R6: D6 không chạy được bằng cách đổi cả repo sang LF | Kế hoạch mục 8: vùng chạy ngoài worktree, mỗi nguồn đúng byte ghim, manifest cạnh script; bỏ câu "đặt `vi.jsonl.gz` vào `analyzing-tools/`"; A3 chỉ khi bản ghim mất | Opus tự băm: OPUS, GUIDE khớp byte checkout; ASTRA, FAMILIES khớp blob Git; bản Kaikki ngoài repo khớp `1f0abd…`, 34.422.366 byte |
| 8 | R7: *bít tết*, H5f, *rầm rầm*, phạm vi S2 | *bít tết* đóng theo `spelling_families.tsv:258`. H5f cộng dạng phân cách ghi là hợp đồng (TC:127). Đã đo ba từ f (mục 4). Nhận *rầm rầm* thay. S2 thu về 7 từ c/d, đủ hai lập trường. 14 quan hệ còn lại thành mục mở, không gửi SA-Fable | `U/ra-thay-chinh-h5.tsv` |
| 9 | R8: nghiệm thu và tác vụ | D7 chồng chéo ít nhất max(15, ⌈0,10 × N⌉) từ. Thêm kiểm gói chữ ký. T9 gồm K0 bất kể tần suất và các cách đọc dưới mốc còi. Thêm kiểm họ H5 độc lập (tách " / "). Một commit phát hành gồm dữ liệu, khối sinh, tài liệu và băm. Cờ từ vào khép trước Final | Kế hoạch mục 6, 9, 10, 12, 13 |
| 10 | Ghi nhượng bộ của Astra thành quyết định chung | T-rtc-2 (bảy chữ ký cũ, rút OI-RTC-KY-CU), T-rtc-3 (*thái*), T-rtc-4 (29 khóa giữ; *chung cư*, *sắn dây* K2), T-rtc-5 (*bít tết*; ba cặp khác từ) | Kế hoạch mục 11 |
| 11 | Sửa tiền lệ "đã ký" | *mất mặt*, *đớn đau* chỉ là tiền lệ phân loại K2 chưa ký (`U/canh-bao-khong-dau.tsv:124, 87`); hai từ chính *mát mắt*, *đón dâu* không vào bản 1 (TC:525) | `OE/doi-chieu-v2.py` |
| 12 | Câu hỏi | S1 còn 17 khóa (mục 2); S2 còn 7 từ; S3 có điều kiện; A2, A3 là dự phòng, chưa gửi; A1 rút; không có câu hỏi K0 | `U/ra-thay-chinh-cau-hoi.md` |

## 2. Opus đổi lập trường sau khi kiểm lại

**13 khóa H7 nhận K1.** Lý do: nhất quán với các K1 đã đồng thuận, và H6 không cho làm sạch bằng nghĩa phụ lành (TC:139).

| Khóa | Cách đọc | r | Lý do |
|---|---|---:|---|
| *bền bỉ* | bên bị | 0,078 | Thuật ngữ tố tụng; nhóm 2 có *nhân chứng*, *vô can* |
| *ca nhạc* | cà nhắc | 0,26 | Tả tật ở chân, như *thớt*/*thọt* đã đồng thuận |
| *cắm đầu* | cầm đầu | 4,3 | Nghĩa thường gặp là đứng đầu nhóm làm việc không chính đáng |
| *choàng* | choáng | 4,8 | Triệu chứng; không làm sạch bằng *choáng ngợp* |
| *giao* | giáo | 0,117 | Danh từ vũ khí dùng độc lập |
| *lề đường* | lê dương | 0,13 | Lính quân đoàn, như *hậu bị* |
| *ngao* | ngạo, ngáo | 0,77; 1,05 | Khinh người; tiếng lóng chê người, như *ngọc*/*ngốc* |
| *nguyên* | nguyền | 0,31 | Nguyền rủa, dùng độc lập |
| *nhồi* | nhói | 0,074 | Cảm giác đau, như *ngựa*/*ngứa* |
| *sàng* | sảng | 0,038 | Triệu chứng, như *mê mẩn*/*mê man* |
| *sông* | sòng | 0,076 | Nơi đánh bạc; r nằm giữa *tầng*/*tang* (0,072) và *phát*/*phạt* (0,138) đã ký K1 |
| *thôn* | thộn | 0,29 | Chê người đần, như *ngọc*/*ngốc* |
| *tiệm* | tiêm | 2,58 | Thủ thuật y khoa như *trồng răng*, khác *đánh răng* |

**H5:**

- nhận thay *rầm rầm*: *rần rần* là biến thể phương ngữ (enwiktionary rev 89902128); cả hai kho dưới 20 lượt;
- *chun*/*thun* không phải khác từ hoàn toàn mà là H5e (mục mở OI-RTC-H5E);
- *qua quýt* không thuộc H5b; họ c riêng còn chờ, nên mục dự phòng này chưa được chọn.

**Tự sửa lỗi:** lý do K2 trong bản nháp trước ghi tiền lệ "*đôn đốc*/*đô đốc*". Đúng là *độ dốc*/*đô đốc* (`U/canh-bao-khong-dau.tsv:89`). Thêm tiền lệ chức danh *từ trường*/*tù trưởng* (dòng 214).

## 3. Không áp dụng, hoặc chỉ áp dụng một phần

| Điểm | Lý do |
|---|---|
| 17 khóa Astra giữ K1 | Opus vẫn giữ K2, mỗi khóa dựa vào một tiêu chí K2 đã ký (TC:167) và tiền lệ có dòng. Hai lập trường được ghi đủ trong Q-rtc-S1 |
| Căn cứ loại c cho 7 từ | Opus vẫn coi đầu mục chữ thường của HND là căn cứ loại c (TC:116). Ghi đủ hai lập trường trong Q-rtc-S2 |
| Thứ tự chọn từ vào | Opus vẫn đề nghị giữ hạng đã khóa. Q-rtc-S3 giữ ở dạng có điều kiện, với điều kiện gửi đã mở rộng như Astra yêu cầu |
| Gợi ý tùy chọn (mục 7 của Astra): một ID quyết định cho mỗi khóa; tách cột loại H5, kết quả số học, đủ nguồn, ý kiến từng SA, chữ ký hiệu lực | Chưa làm. Bảng hiện có cột `nguon_*` tệp:dòng và trạng thái riêng của mỗi bên. Có thể làm khi lập gói chữ ký |

## 4. Số đo mới: H5f

**Đầu vào:**

- cặp dạng: `OE/cap-h5f.tsv` (dạng cách, gạch nối, viết liền của *cải xoong*/*cải soong* và *xà phòng*/*xà bông*);
- kho: OpenSubtitles v2018 VI (SHA-256 `1aae9970…`) và CCAligned v1 VI (`21c6c055…`), khớp `manifest.json`;
- kho tải tạm ngoài repo và đã xóa sau khi đếm. Không lưu câu của kho (không đặt `NGU_CANH`).

**Lệnh** (từ `OE/`):

```powershell
$env:HND_DIR = '<ngoài repo>'; $env:KHO_DIR = '<ngoài repo>'
$env:CAP_H5 = "$PWD\cap-h5f.tsv"; $env:RA_H5 = 'dem-h5f'
python dem-h5.py
```

**Kết quả** (`OE/dem-h5f.tsv`): phụ đề tính mọi dòng, đã lọc nghi vắt từ; web tính dòng khác nhau, đã lọc.

| Họ | Dạng | Phụ đề | Web |
|---|---|---:|---:|
| *cải xoong* | cải xoong + cải-xoong + cảixoong | 4 + 0 + 0 = 4 | 42 + 0 + 0 = 42 |
| | cải soong + cải-soong + cảisoong | 0 | 0 |
| *xà phòng* | xà phòng + xà-phòng + xàphòng | 181 + 0 + 0 = 181 | 3.894 + 0 + 1 = 3.895 |
| | xà bông + xà-bông + xàbông | 51 + 57 + 0 = 108 | 318 + 2 + 0 = 320 |

**Kết luận đề nghị** (loại f xử như loại c, TC:127, 124):

- *cải xoong*: phụ đề 4 < 20 lượt → thiếu dữ liệu, loại.
- *xà phòng*/*xà bông*: không dạng nào đạt 95% ở cả hai kho → loại cả hai.
  - So bằng số nguyên: phụ đề 181 × 100 < 95 × 289; web 3.895 × 100 < 95 × 4.215.
  - Không phụ thuộc bộ lọc: chưa lọc thì phụ đề 185/293, web 3.981/4.302.
  - Không phụ thuộc độ nhạy: phụ đề dòng khác nhau 151/254.
  - Riêng *xà-bông* có 57 lượt gạch nối ở phụ đề, nên phép cộng dạng phân cách làm tỷ lệ của *xà phòng* giảm từ 78% xuống 62,6%.
- Ba từ ở trạng thái DO_XONG_CHO_ASTRA_XAC_NHAN, chờ Astra xác nhận số ở lượt duyệt tới.

## 5. Chạy lại

Từ `OE/`, theo thứ tự (HND tải tạm ngoài repo, xóa sau khi chạy):

```powershell
$env:HND_DIR = '<ngoài repo>'; python -X utf8 -B de-xuat-thay-v2.py
python -X utf8 -B hop-nhat-rtc.py
python -X utf8 -B kiem-dau-ra.py
```

**Kết quả** (`de-xuat-thay-v2.log`, `hop-nhat-rtc.log`):

- H7: 349 khóa. 80 đồng thuận thay, 17 tranh chấp, 46 chờ, 7 giữ theo chữ ký cũ, 1 *gián*, 196 cần ký K2, 2 không đỏ.
- H5: 65 cặp. 11 đồng thuận thay, 3 đã đo, 7 tranh chấp, 11 QUA, 6 khác từ, 27 chờ.
- Thay: 101 từ ra, 101 từ vào (96 A, 5 C), 19 dự bị; sau thay 7.776 từ, 7.776 khóa, F = 77, R1 = 0. Nhánh S1 theo Astra: 118 từ ra, còn 2.

## 6. Sửa lần 2 (theo Lượt duyệt 2 của Astra)

**Đầu vào:** `ho-so/astra/ra-thay-chinh/round-1-review-drafts.md`, mục "Lượt duyệt 2" ("changes requested"), và các phiếu `RD/rd2-*`. Mỗi điểm được kiểm lại trên repo trước khi áp dụng.

**Tệp đã sửa:** ba tài liệu chung (giữ `Status: Draft (round 1)`); ba TSV chung (sinh lại); `OE/doi-chieu-v2.py`, `OE/de-xuat-thay-v2.py`, `OE/hop-nhat-rtc.py`; nhật ký này.

| # | Điểm của Astra | Kiểm [verified] | Việc đã làm |
|---|---|---|---|
| 1 | Xác nhận thay ba từ H5f | `RD/rd2-H5-xac-nhan.tsv:2–4` dùng đúng số của `OE/dem-h5f.tsv` | Ghi T-rtc-9; đóng OI-RTC-H5F. Đồng thuận thay: 94 (80 H7, 14 H5) |
| 2 | *nướng*, *phết* đã có chữ ký K2 cũ | `chu-ky.tsv:1831–1832`, `:1872–1873`: mỗi khóa có dòng của Astra và Opus | Thêm hai khóa vào chữ ký cũ: giữ theo chữ ký cũ 9, cần ký mới 194. C3 bỏ *kinh* khỏi ví dụ mặt chữ thiếu |
| 3 | Bỏ "chạy lại P6" khỏi phần ngoài phạm vi; kích hoạt S3 | `ra-thay-chinh-yeu-cau.md:19` ghi "P6/P7/phát hành riêng"; TC:227, :402. Số đổi thứ tự 24/31 vị trí đọc từ `RD/rd2-audit-summary.json`, trường `S4_O101`; Opus không chạy lại script của Astra | Sửa kế hoạch mục 2, 6, 9 (điểm trong `labels.tsv` theo phán quyết S3), báo cáo mục 4.3; Q-rtc-S3 thành câu hỏi gửi ngay. Lập trường Opus vẫn là giữ hạng đã khóa, nhưng không dựa vào lý do phạm vi nữa |
| 4 | Điều kiện A2 | Kế hoạch: nghĩa mới chỉ viết sau khi duyệt, nên không thể bắt chờ D6/D7 | A2 gửi ngay khi kiểm sức chứa trước Final cho thấy thiếu, hoặc khi trượt D6/D7 sau khi duyệt làm thiếu |
| 5 | `nguon_opus` thiếu số dòng | `hop-nhat-rtc.py` lấy dòng gán cuối cùng của mỗi khóa và cặp trong `doi-chieu-v2.py` | Không còn dòng nào chỉ ghi "(H7)" hay "(H5)"; mọi số dòng trỏ đúng dòng có khóa hay cặp đó |
| 6 | Hàm chọn: R1 có thể thay ghế OK; H5b thiếu tổ hợp | Tự kiểm: *tỉ mỉ* cho đủ *tỉ mỷ, tỷ mỉ, tỷ mỷ*; ca R1 vào ghế OK bị chặn | `chon()` nhận R1 chỉ tới min(388, R1 còn lại + số R1 ra); `h5b()` sinh mọi tổ hợp; thêm `_tu_kiem()`. Chạy lại với HND tạm ngoài repo (đã xóa): kết quả không đổi |
| 7 | Phiếu rd2 của Astra | Mã mới: NHAN_THAY_H5f, BAO_LUU_CHO_LOAI, BAO_LUU_K1, GIU_CHU_KY_CU | Thêm vào bảng ánh xạ của `hop-nhat-rtc.py`; cột `nguon_astra` ghi dòng rd2 kèm dòng lý do rd1 |
| 8 | Ba cờ từ vào đề nghị đóng | Trùng nhận định sơ bộ của Opus | Ghi T-rtc-10; còn 8 cờ. Nhận lưu ý của Astra: *làm cỗ*/*làm cỏ* phải xét nghĩa bóng tàn sát |
| 9 | Quy trình khép mục mở | Không trái luật đã ký; phân tuyến đúng TC:164, H9 | Kế hoạch mục 12.1 (phiếu chung, bốn hàng đợi, phân tuyến), mục 15 (giai đoạn 3a, 3b), T-rtc-11; OI-RTC-HND làm cùng OI-RTC-H7-CHO |
| 10 | Dẫn tiền lệ 34/3 kèm điều kiện đếm | Astra đếm lại: 34 c, 3 d khi tách " / "; 33/3 nếu so nguyên ô | Q-rtc-S2 và báo cáo mục 4.2 ghi điều kiện đếm và `RD/rd2-HND-tien-le.tsv` |

**Không bác điểm nào của Lượt duyệt 2.** Opus vẫn giữ lập trường của mình ở Q-rtc-S1 (17 khóa), Q-rtc-S2 (7 từ) và Q-rtc-S3 (giữ hạng đã khóa). Đó là lập trường cần phán quyết, không phải từ chối một yêu cầu sửa.

**Số sau sửa lần 2** (`OE/hop-nhat-rtc.log`, `OE/de-xuat-thay-v2.log`):

- H7: 349 khóa. 80 đồng thuận thay, 17 tranh chấp, 46 chờ, 9 giữ theo chữ ký cũ, 1 *gián*, 194 cần ký K2 mới, 2 không đỏ.
- H5: 65 cặp. 14 đồng thuận thay, 7 tranh chấp, 11 QUA, 6 khác từ, 27 chờ.
- Thay: 101 từ ra (94 đồng thuận, 7 của S2), 101 từ vào (96 A, 5 C), 19 dự bị. Sau thay: 7.776 từ, 7.776 khóa, F = 77, R1 = 0.
- Nhánh: thêm *theo* thì 102/102, F = 77; S1 theo Astra thì 118 ra, còn 2 dự bị.

**Câu hỏi gửi SA-Fable ngay:** Q-rtc-S1, Q-rtc-S2, Q-rtc-S3. Q-rtc-A2, Q-rtc-A3 vẫn là dự phòng cho chủ dự án, chưa gửi.

## 7. Sửa lần 3 (quyết định D-rtc-5 của chủ dự án)

**Đầu vào:** tin nhắn Discord của chủ dự án, 21/11/2026 16:58 +07:00: không dùng SA-Fable; hai SA tự thỏa thuận rồi trình chủ dự án quyết định.

- Kế hoạch mục 11: thêm D-rtc-5 (owner, 2026-11-21, nguồn: tin nhắn Discord; commit chờ).
- Ba tài liệu chung:
  - Q-rtc-S1, S2, S3 chuyển sang thỏa thuận giữa hai SA, chưa gửi;
  - phần còn lệch sau một lượt đối đáp trình chủ dự án; dòng Answer đổi thành owner;
  - mục 12.1 (phân tuyến), T-rtc-11, mục 14 và mục 15 (giai đoạn 2, 3b; tổng khoảng 15–28 lượt) bỏ đường SA-Fable.
- Đề xuất từng mục của Opus: `thoa-thuan-1.tsv`, `thoa-thuan-1.md`.
  - S1: nhận K1 cho 7 khóa, giữ K2 cho 10 khóa;
  - S2: thay cả bảy với nhãn CHO_LOAI;
  - S3: nhận tính lại, đề xuất rổ 2.
- Giữ `Status: Draft (round 1)`. Không đổi TSV chung hay dữ liệu chính.

## 8. Sửa lần 4 (thỏa thuận vòng 2, theo D-rtc-5)

**Đầu vào:** `ho-so/astra/ra-thay-chinh/thoa-thuan-1.tsv`, `thoa-thuan-1.md` (gồm mục "Đối chiếu với Opus").

**Lập trường cuối của Opus** (`thoa-thuan-2.md`):

- nhận K2 của Astra cho 4 khóa chéo: *húng, hững hờ, phù dâu, thắm thiết*. Đây là lập trường gốc của Opus;
- giữ K2 cho 10 khóa, trình chủ dự án ở Q-rtc-O1.

**Tài liệu chung:**

- Kế hoạch:
  - thêm T-rtc-12 (S1: 7 khóa), T-rtc-13 (S2: 7 từ CHO_LOAI, không phát hành), T-rtc-14 (S3: tính lại S2/S3 theo P6, rổ mọi mục qua H1–H9 có nhãn, mục loại ở D6 bỏ lúc chọn, dự bị cùng hàng đợi);
  - sửa mục 4, 5, 6, 9, 12, 13, 14, 15; mục 12.2 mới chứa điều kiện của Q-rtc-A2, A3;
  - tổng khoảng 13–25 lượt agent; giữ `Status: Draft (round 1)`.
- Câu hỏi: chỉ còn một câu cho chủ dự án, Q-rtc-O1 (10 từ, chia bốn nhóm). Q-rtc-S1, S2, S3 đã khép. A2, A3 chưa kích hoạt.
- Báo cáo chung: viết lại mục 1 và mục 4; sửa các bảng ở mục 3.

**Script:**

- `doi-chieu-v2.py`: thêm `_K1_TT1` (*cò trắng, sân ga, trăng tròn*); bảy cặp S2 thành THAY_CHO_LOAI.
- `hop-nhat-rtc.py`:
  - đọc `thoa-thuan-1.tsv` của Astra làm phiếu mới nhất;
  - thêm trạng thái DONG_THUAN_THAY_CHO_LOAI;
  - vai trò RA_NEU_CHU_DU_AN_THEO_ASTRA cho 10 khóa của Q-rtc-O1.
- `de-xuat-thay-v2.py`: nhánh "chủ dự án theo Astra" lấy các khóa Astra giữ K1 ở thỏa thuận 1.
- Chạy lại với HND tạm ngoài repo, đã xóa sau khi chạy.

**Số sau sửa lần 4:**

- H7: 83 đồng thuận thay, 10 chủ dự án quyết, 46 chờ, 9 chữ ký cũ, 1 *gián*, 198 cần ký K2 mới, 2 không đỏ.
- H5: 14 thay theo số đếm, 7 CHO_LOAI, 11 QUA, 6 khác từ, 27 chờ.
- Thay: 104 từ ra, 104 từ vào (99 A, 5 C; hạng đã khóa 8.096–8.218), 16 dự bị.
- Nhánh:
  - theo Astra ở Q-rtc-O1: 114 ra, 6 dự bị;
  - thêm *theo*: 105/105, F = 77.
- Trung vị PPM sạch của tập 104: từ ra 1,741, từ vào 0,0729. Phép kiểm tập 87 vẫn khớp số của Astra.

## 9. Sửa lần 5 (quyết định D-rtc-6 của chủ dự án)

**Đầu vào:** câu trả lời Q-rtc-O1 của chủ dự án, commit `0253bb0`. Nguyên văn form: "thay A-1 và tất cả C, giữ các chữ còn lại". Nguyên văn Discord, 21/11/2026 21:01 +07:00: "Q-rtc-O1 C thay, 1 thay, giữ còn lại". Opus kiểm: rõ nghĩa, nhận.

**Kế hoạch:**

- mục 11: thêm D-rtc-6 (owner, `0253bb0`); D-rtc-5 và 14 dòng T-rtc-* trỏ tới `7fb17fb`;
- mục 4, 5, 6, 12, 12.1, 12.2, 14, 15: thay *vòng, thuần, xuân*; giữ bảy khóa còn lại với K2 (gói chữ ký 205 khóa); bỏ OI-RTC-H7-S1;
- giữ `Status: Draft (round 1)`.

**Câu hỏi:** tệp ghi "Không còn câu hỏi mở". Q-rtc-O1 đầy đủ ở `0253bb0`; Q-rtc-A2, A3 chưa kích hoạt.

**Báo cáo chung:** mục 1, 3.1, 3.3, 4.1 và 5 theo D-rtc-6.

**Script:**

- `de-xuat-thay-v2.py`: thêm `D_RTC_6`; bỏ nhánh "chủ dự án theo Astra".
- `hop-nhat-rtc.py`:
  - thêm cột `quyet_dinh_chu` và hai trạng thái CHU_DU_AN_THAY, CHU_DU_AN_GIU_CAN_KY_K2;
  - từ ra theo chủ dự án mang trạng thái QUYET_DINH_CHU_D-rtc-6.
- Chạy lại với HND tạm ngoài repo, đã xóa sau khi chạy.

**Số sau sửa lần 5:**

- H7: 83 đồng thuận thay, 3 chủ dự án thay, 7 chủ dự án giữ (K2), 46 chờ, 9 chữ ký cũ, 1 *gián*, 198 hai bên giữ (K2), 2 không đỏ.
- Thay: 107 từ ra (97 đồng thuận, 7 CHO_LOAI, 3 theo D-rtc-6). 107 từ vào (101 A, 6 C; hạng đã khóa 8.096–8.223), 13 dự bị.
- Nhánh thêm *theo*: 108/108, F = 77.
- Trung vị PPM sạch tập 107: từ ra 1,804, từ vào 0,0729.
- Cờ còn mở: 8, nay đều ở từ vào; *xầm xì* thành từ vào thứ 106.
- Gói chữ ký K2: 205 khóa (194; 4 của T-rtc-12; 7 của D-rtc-6).

## 10. Sửa lần 6 (khép mục mở 1)

**Đầu vào:** `ho-so/astra/ra-thay-chinh/khep-muc-mo-1.tsv`, `khep-muc-mo-1.md` (Astra, gpt-6.2-astra theo Q-rtc-M1 b).

**Phiếu của Opus:** `khep-muc-mo-1-opus.tsv`, `khep-muc-mo-1-opus.md`, sinh bằng `evidence/khep-muc-mo-1-opus.py`.

- Đồng ý 282 trong 286 dòng.
- Không đồng ý 4 dòng: *cần cù, tiền lương, triệu, bạn thân*; Opus giữ K2 và đã ký.
- 238 chữ ký K2 của Opus; hai SA cùng ký 234.

**Script:**

- `de-xuat-thay-v2.py`:
  - thêm KHEP_1 (9 từ ra) và KHONG_VAO_1 (*làm cỗ*, *rướn*);
  - thêm nhánh Q-rtc-O2 theo Astra; đếm ghế thiếu.
- `hop-nhat-rtc.py`:
  - đọc hai phiếu khép mục mở;
  - thêm cột `chu_ky_phieu` và trạng thái DONG_THUAN_GIU_DA_KY_PHIEU, CHU_DU_AN_GIU_DA_KY_PHIEU;
  - bỏ hai phép kiểm hồi quy của tập 87 (đuôi hàng và trung vị). Hai phép này không còn áp dụng sau khi loại *làm cỗ*, *rướn*; chúng đã đạt ở sửa lần 1 đến lần 5.
- Chạy lại với HND tạm ngoài repo, đã xóa sau khi chạy.

**Số:**

- H7: 89 đồng thuận thay, 3 chủ dự án thay, 4 tranh chấp, 226 giữ đã ký phiếu, 7 chủ dự án giữ đã ký phiếu, 10 không đỏ, 9 chữ ký cũ, 1 *gián*.
- H5: 17 thay, 7 CHO_LOAI, 15 QUA, 23 khác từ, 2 đã ra, 1 không vào; không còn dòng chờ.
- Thay: 116 từ ra (106 đồng thuận, 7 CHO_LOAI, 3 theo D-rtc-6). 118 dự phòng dùng được; 116 từ vào (106 A, 10 C; hạng đã khóa 8.096–8.245); 2 dự bị.
- Nhánh Q-rtc-O2 theo Astra: 120 ra, 118 vào, thiếu 2 ghế. Tính lại S2/S3 (T-rtc-14) không đổi sức chứa.
- Trung vị PPM sạch tập 116: từ ra 1,914, từ vào 0,0729.

**Tài liệu chung:**

- Kế hoạch: T-rtc-15 đến T-rtc-18 (commit chờ); mục 5, 6, 12 (bảng mục mở mới), 12.2, 14, 15 (còn khoảng 9–19 lượt).
- Câu hỏi: Q-rtc-O2 (4 từ) và Q-rtc-A2 (lấp ghế; đề nghị hai SA là chu kỳ HM có giới hạn), dòng Answer trống.
- Báo cáo chung: mục 1, 3, 4.5 mới, 5.
- Giữ `Status: Draft (round 1)`.
