# Rà chéo vòng 1 — Opus đọc phân tích độc lập của Astra (rà và thay danh sách chính)

**Ngày:** 21/11/2026. **Nhánh:** `analyze/ra-thay-chinh`, gốc `1c3f504`. **Người viết:** SA-Opus.

**Đã đọc:** `analyzing-tools/ho-so/astra/ra-thay-chinh/round-1-analysis.md`, chín TSV ở thư mục gốc và các tệp `evidence/` cần cho từng điểm (`artifact-index.tsv`, `ung-vien-doi-chung-H5.tsv`, `ung-vien-doi-chung-H7.tsv`).

**Cách kiểm:** mọi khẳng định của Astra được đối chiếu với dữ liệu và script trong repo, không với báo cáo của Astra:

- `chu-ky.tsv`, `canh-bao-khong-dau.tsv`, `blocked_keys.tsv`, `spelling_families.tsv`, `opus-counts.tsv`, `xep-hang.tsv`, `d6-kiem.py`, `tieu-chi-thong-nhat.md`;
- danh sách HND ghim `688b095`, tải tạm ngoài repo rồi xóa;
- Wiktionary qua API, chỉ đọc nhãn và đầu mục; mỗi lần tra ghi số revision, không lưu lời định nghĩa.

Nhãn: **[đã kiểm]** hoặc **[giả định]**.

**Ba bảng đối chiếu từng mục** (trong `evidence/`):

- `doi-chieu-h7.tsv`: 349 khóa chính;
- `doi-chieu-h5.tsv`: 60 cặp;
- `doi-chieu-thay.tsv`: danh sách ra và vào.

Lập trường mới của Opus (v2) nằm trong `evidence/doi-chieu-v2.py` và mô phỏng `evidence/de-xuat-thay-v2.tsv`.

## 0. Tóm tắt

1. Sau rà chéo, Opus nâng đề xuất từ **38 lên 86 từ thay**: 65 K1, 2 K0, 19 H5. Astra đề xuất 141. Hai bên chung 74 từ.
2. Phần lớn khoảng cách nằm ở luật K1 của H7. Mốc r ≥ 0,2 của Opus và quy tắc "một âm tiết luôn là K2" sai so với tiền lệ, nên Opus bỏ cả hai.
3. Luật K1 của Astra (chỉ cần cách đọc thuộc nhóm đỏ, bất kể tần suất) cũng sai so với chữ của H7, với tiền lệ, và với sáu chữ ký K2 mà chính Astra đã ký.
4. Opus đề xuất một thước hai trục rút ra từ các phân xử đã ký: **K1 khi nghĩa chính nặng và r ≥ 0,035**, các trường hợp đỏ còn lại là K2, chữ ký K2 cũ giữ nguyên. Còn lệch 67 khóa: 58 khóa Opus xếp K2, 8 khóa đã ký hoặc không đỏ, và *do đó*.
5. Opus nhận các phát hiện đúng của Astra:
   - hai ca K0: *phản bác*/*phân bắc*, *tính khí*/*tinh khí*;
   - các họ H5 *dây chun*/*dây thun*, *phí phạm*/*phí phạn*, *xà bông*/*xà phòng*;
   - 19 đối chứng chỉ là tên riêng;
   - còi tương đối dưới 0,3 PPM;
   - D6 phải dùng đúng snapshot đã ghim.
6. Opus sửa luật loại c/d của mình theo tiền lệ, nên thêm 7 từ H5 phải thay: *co rúm*, *xù xì*, *rầm rộ*, *chơ vơ*, *xập xình*, *su hào*, *loay hoay*.
7. Lỗi chính của Astra:
   - mở lại sáu chữ ký K2 khi không có chứng cứ mới;
   - xếp K1 cho 22 khóa có r < 0,035;
   - không soát 332 cách đọc HND cùng khóa;
   - chấm lại điểm P6 làm *do đó* bị đẩy ra.
8. Với 86 từ thay, dự phòng đủ ghế: 86 từ vào, còn 25 mục dự bị. Vì vậy Q-rtc-A2 (mở lại từ có thể cân nhắc) chưa cần. Q-rtc-A1 (*gián*) chỉ cần nếu SA-Fable xếp *gian* là K1.

## 1. Điểm đồng ý

| # | Điểm | Chứng cứ |
|---|---|---|
| Đ1 | Đầu vào tái lập đúng: 632 cặp H5 trên 474 từ, 1.177 cặp H7 trên 634 khóa | [đã kiểm] cả hai bên ra cùng tập |
| Đ2 | `baotu` không thuộc danh sách chính; ghi K1 vào `blocked_keys.tsv` theo T-dpv2-7 | [đã kiểm] `blocked_keys.tsv`; `du-phong-v2-ke-hoach.md:422` |
| Đ3 | Thay *bồ kết*, *chòng chành*, *ngoảnh*, *phấp phới*, *rau dền* (H5c thiếu dữ liệu) | [đã kiểm] số đếm của Opus khớp cận của Astra |
| Đ4 | 19 đối chứng H5 chỉ có dạng viết hoa trong HND (tên riêng) | [đã kiểm] 19/19 |
| Đ5 | 66 khóa H7 hai bên cùng đề nghị thay, ví dụ *chữ nghĩa*, *thiên tài*, *nhàu*, *cuốc*, *bảo hành*, *bố mẹ* | [đã kiểm] `doi-chieu-h7.tsv`, `ket_qua_v2 = THAY\|THAY` |
| Đ6 | Giữ F = 77, R1 = 0; không lấy R1 lấp ghế OK; không dùng từ ba chữ; quyết định 10 không bỏ cửa 7.776 | [đã kiểm] `tieu-chi-thong-nhat.md:407`, `WordListAnalyze.md:153–155` |
| Đ7 | Mọi từ vào có câu viết sạch mới, kể cả từ dự phòng A đã có câu lịch sử; cách ly theo `huong-dan-giai-nghia.md:167–185`; tối đa hai lượt viết lại (`tieu-chi-thong-nhat.md:307`) | [đã kiểm] |
| Đ8 | D6 phải chạy với đúng snapshot đã ghim. `d6-kiem.py:528–531` ghim WIKT_VI = `1f0abd…`; `:375–378` dừng an toàn khi băm khác. `vi.jsonl.gz` hiện không có trong `analyzing-tools/` | [đã kiểm] |
| Đ9 | Cột `vao` của `xep-hang.tsv` lệch danh sách hiện hành 127 từ, nên chỉ dùng thứ hạng, không dùng cột này | [đã kiểm] 127/127 |
| Đ10 | Checkout CRLF có lỗi nền C1/C8; bản LF đạt; chỉ đăng ký họ đã xác nhận, không đăng ký 632 cặp thô | [đã kiểm] |

## 2. Điểm bất đồng

### 2.1. Luật quyết định K1 của H7

**Chữ của tiêu chí** (`tieu-chi-thong-nhat.md:160–168`):

- **K1:** người đọc xác nhận cách đọc khác là cách đọc **tự nhiên, thông dụng**, thuộc nhóm đỏ.
- **K2:** cách đọc khác **hiếm**, phải tách ép, chỉ khớp một âm tiết, hoặc nghĩa đỏ **không chắc**.
- H6 (`:143–152`) liệt kê cả những từ *không* bị loại vì nhóm đỏ: *hắt hơi*; *bọ chét*, *chuột cống* (tên con vật); *công chúa*, *hoàng tử*, *hoàng hậu*; *lễ hội*, *phép thuật*; *bàn cờ*, *cờ vua*.

Tiêu chí không ghi tỷ lệ nào.

**Luật vòng 1 của Opus:** K1 khi r ≥ 0,2; khóa một âm tiết luôn là K2. Luật này mâu thuẫn tiền lệ:

- K1 đã ký ở mức r = 0,036 (*đường dẫn*/*đường đạn*) và r = 0,181 (*phát điện*/*phát điên*), theo `canh-bao-khong-dau.tsv`;
- khóa một âm tiết đã bị chặn K1 ở P2 (`blocked_keys.tsv`):
  - *tầng*/*tang*, r 0,072;
  - *phát*/*phạt*, r 0,138;
  - *dành*/*đánh*, r 0,68.

**Opus rút luật vòng 1.**

**Luật của Astra** [đã kiểm từ dữ liệu của Astra]: cách đọc thuộc nhóm đỏ thì xếp K1, không xét tần suất. Cột `ly_do` dùng một câu mẫu cho mọi cặp cùng nhóm, ví dụ "Cách đọc tự nhiên về bệnh, triệu chứng…", và không có số đo nào cho "tự nhiên". Luật này mâu thuẫn:

- Chữ "hiếm → K2". Astra xếp K1 cho *theo*/*thẹo* (r 0,001), *kiểu*/*kiêu* (0,002), *liên quan*/*liên quân* (0,003).
- Tiền lệ K2 đã ký:
  - *thầy*/*thây*, r 0,016 (`chu-ky.tsv:2152–2154`);
  - *bình*/*bĩnh*, r 0,012, và *bình*/*bịnh*, r 0,017 (`chu-ky.tsv:134–135`);
  - *di động*/*đi đồng*, khoảng 0,001 (`chu-ky.tsv:786–787`).
- Tiền lệ KHONG_TU_DONG cho cách đọc nặng mà nghĩa không chắc: *độ dốc*/*đô đốc* r 3,8; *đồng tình*/*động tình* 0,53; *từ trường*/*tù trưởng* 0,35.
- Tiền lệ K2 cho cách đọc nhẹ dù r lớn: *mát mắt*/*mất mặt* 47,7; *đón dâu*/*đớn đau* 2,5; *thổi*/*thối* 0,17; *khảm*/*khắm* 0,065.

**Thước hai trục mà Opus đề xuất** cho hai bên dùng chung (`evidence/doi-chieu-v2.py`, docstring):

- **Nặng:** nghĩa chính của cách đọc đúng loại mà bảng H6 ghi là đỏ:
  - chết, mai táng;
  - vũ khí, địch, tấn công;
  - tội phạm, xử phạt, tố tụng, giam giữ;
  - bệnh, triệu chứng (H6 ghi *ngứa ngáy*);
  - tình dục, thai nghén;
  - rượu, thuốc lá, cờ bạc (H6 ghi *lá bài*);
  - đảng phái, bầu cử, quyền lực;
  - thảm họa;
  - thần thánh, từ tôn giáo;
  - chửi rủa, chê người (H6 ghi *la mắng*, *tham lam*, *giả dối*).
- **Nhẹ:**
  - từ đa nghĩa có nghĩa chính trung tính;
  - hình vị chỉ dùng trong từ ghép;
  - cụm phải tách ép;
  - tiếng lóng, lời chê nhẹ;
  - biểu tượng, chức danh, dáng điệu, cảm xúc.
- **Tự nhiên:** r ≥ **0,035**. Mốc này nằm giữa K2 cao nhất của cách đọc nặng (*bịnh* 0,017) và K1 thấp nhất (*đường đạn* 0,036). Cách đọc nhẹ (*khắm*, *thối*, *mất mặt*) là K2 dù r cao hơn.
- **Kết luận:** K1 = nặng và r ≥ 0,035. K2 = các ca còn lại có nghĩa đỏ. Chữ ký K2 đã có giữ nguyên nếu không có chứng cứ mới (H9).

**Đối chiếu thước với các tiền lệ** [đã kiểm]:

- Thước giải thích được mọi K1 đã ký: *tự tử*, *đường đạn*, *phát điên*, *tang*, *phạt*.
- Thước giải thích được mọi K2 đã ký:
  - *thây*, *bĩnh*, *bịnh*: r thấp;
  - *thối*, *khắm*: nghĩa nhẹ;
  - *kinh*: đa nghĩa;
  - *binh*: hình vị.
- Thước giải thích được hai ca KHONG_TU_DONG trong ba ca đã nêu: *đô đốc* (chức danh), *tù trưởng*.
- Ca không khớp: *đồng tình*/*động tình* (r 0,53) được ký KHONG_TU_DONG dù là cách đọc về tình dục; Opus coi đây là phân xử đơn lẻ và theo nó cho *động dục*.

**Tác động** [đã kiểm, `evidence/doi-chieu-astra.log`]:

- Theo thước này, Opus thêm 37 K1 và 2 K0, đồng thời bỏ K1 cho *sắn dây*, *chung cư* (mục 4). Kết quả: 65 K1 và 2 K0.
- Astra có 132 khóa chặn. Hai bên chung 66 khóa.
- Còn lệch 67 khóa (`doi-chieu-h7.tsv`, `ket_qua_v2 = KY_K2|THAY` hoặc `GIU|THAY`, cộng *do đó*), xếp theo lý do Opus giữ:

| Lý do Opus không thay | Số khóa | Khóa |
|---|---:|---|
| Hai bên đã ký K2 và không có chứng cứ mới | 6 | *bình, di động, khảm, kính, thầy, thổi* |
| r < 0,035 (hiếm) | 22 | *bản đồ, bộ đồ, chồng, chốt, chú ý, có mặt, đa năng, đề cử, kể cả, khăn, kiểu, liên quan, lo lắng, lưới, phòng, phòng ngủ, quà tặng, quên, theo, treo, tung, vòng* |
| Nhẹ: đa nghĩa, hình vị, tách ép, biểu tượng, chức danh, cảm xúc | 36 | *bền bỉ, ca nhạc, cắm đầu, chiên, choàng, chuông, cò trắng, đông đúc, gián, giảng, giao, húng, hững hờ, khiến, làm mẫu, lề đường, ngại, ngao, nguyên, nhâm nhi, nhồi, phong bì, phù dâu, sàng, sân ga, sông, thắm thiết, thị trường, thôn, thuần, tiệm, trạm, trăng tròn, trình diễn, tường, xuân* |
| Không thuộc nhóm đỏ | 2 | *đồng ý* (đông y), *đuốc* (dược) |
| Chấm lại P6 (mục 2.4) | 1 | *do đó* |

Ngược lại, Opus thay *thái* (đọc thành *thai*, thai nghén theo ví dụ *có chửa* của H6, r 1,6); Astra để chờ. Mỗi dòng của bảng có lý do riêng.

### 2.2. K0

- **Opus nhận K0 cho hai ca:**
  - *phản bác*/*phân bắc*: chất thải người; vi.wiktionary có mục (rev 1892186);
  - *tính khí*/*tinh khí*: vi.wiktionary chỉ trỏ tới *tinh dịch* (rev 1930782), mà `tinhdich` là K0_TU_DIEN.
- **Không nhận K0 cho *bố mẹ*/*bỏ mẹ*.** enwiktionary ghi nhãn *offensive*, không ghi *vulgar* (rev 84835723). Các khóa K0_TU_DIEN đều là mục tục, tình dục hay chất thải, còn lời văng thuộc H6 nhóm 9, đi theo đường K1/K2. Opus xếp K1 (nặng, r 0,070), nên kết quả vẫn là thay; chỉ khác mã ghi trong `blocked_keys.tsv`.
- **Không nhận K0 cho *di động*/*đi đồng*.** enwiktionary ghi *dialectal*, *colloquial* (rev 84662196). Đó đúng là điều chữ ký của Astra đã nêu: "KHÔNG phải tên chất thải hay từ tục có nhãn" (`chu-ky.tsv:786`).

### 2.3. H5

| Điểm | Astra | Opus v2 | Căn cứ |
|---|---|---|---|
| *lấn át*/*lấn áp* | Chờ nguồn và đo | Thay | [đã kiểm] lấn áp 10/75 lượt phụ đề (13,3%), độ nhạy 9/64; c hay d đều loại; ngữ cảnh cùng nghĩa |
| *cải xoong*/*cải soong* | Chờ | Thay (f) | Tiền lệ *soong*/*xoong* là f, LOAI_CANH_TRANH (`spelling_families.tsv`); phụ đề 4 + 0 < 20 |
| *co rúm, xù xì, rầm rộ, chơ vơ, xập xình, su hào* | Chờ | Thay (c, thiếu dữ liệu) | [đã kiểm] dạng kia có trong HND chữ thường. Theo tiền lệ, dạng chỉ có trong HND 39K/74K được xếp c 34 lần và d 3 lần. Số đếm: phụ đề 2–8 hoặc web 16 |
| *loay hoay*/*lay hoay* | Chờ | Thay (c, 15% < 95%) | [đã kiểm] phụ đề 17/3; ngữ cảnh cùng nghĩa |
| *xà bông*/*xà phòng* | Chờ đo H5f | Thay cả hai | Cùng từ mượn *savon*. Phụ đề xà phòng 181/232 = 78% < 95%, nên dù cộng thêm dạng gạch nối hay viết liền cũng không qua |
| 14 cặp đủ dữ liệu (*bít tết, rong ruổi, trưng bày, theo dõi, hạt dẻ*…) | Chờ đo | QUA, đăng ký | [đã kiểm] `evidence/dem-h5.tsv`: đều ≥ 95% ở cả hai kho |
| 8 cặp i/y mới (*công ty/công ti*…) | Không có | QUA, đăng ký | [đã kiểm] `evidence/dem-h5b.tsv` |
| *bóng láng*/*bóng loáng* | Chờ quan hệ | Khác từ | Wiktionary có hai mục riêng, không mục nào ghi là cách viết khác |

Astra để chờ 44 cặp vì chưa có số đếm; số đếm của Opus khép phần lớn các cặp này. Bảng đủ ở `doi-chieu-h5.tsv`.

### 2.4. P6: chấm lại điểm hay giữ thứ hạng đã khóa

- **Astra** tính lại S2 trên rổ mới. Kết quả là *do đó* (F) bị đẩy ra dù không trượt cổng nào.
- **Opus** giữ điểm và hạng đã khóa, lấp ghế từ dự phòng theo S4, đúng luật cho mục rời chính sau P6:
  - "Tối đa hai lượt viết lại; còn lỗi thì thay từ bằng dự phòng" (`tieu-chi-thong-nhat.md:307`);
  - "thay bằng dự phòng nếu cần" (`tieu-chi-thong-nhat.md:427`).
- D-dpv2-5 có nhắc "P6/P7/phát hành riêng". Opus hiểu cụm này là chạy lại kiểm sức chứa và ngăn hạn mức (C13) và lập lại dự phòng, chứ không phải đổi điểm của các từ không trượt cổng.
- Chấm lại điểm sinh thay đổi ngoài yêu cầu "thay nếu cần". Nếu không hòa được thì hỏi SA-Fable (Q-rtc-O2).

### 2.5. Sức chứa và nguồn từ vào

- Với 86 từ ra (đều ngăn OK không-F), dự phòng đủ [đã kiểm, `evidence/de-xuat-thay-v2.log`]:
  - 86 từ vào gồm 84 tầng A và 2 tầng C, hạng S4 từ 8.096 đến 8.194;
  - còn 25 mục dự bị đủ điều kiện;
  - bỏ qua 76 mục F, 6 mục tầng D, 2 mục cổng mở hoặc trượt H5b (trong đó có *qua quýt*).
- Chín từ vào cần đọc lại:
  - ba có còi H7 nhưng cách đọc không đỏ: *đưa đò*, *làm cỗ*, *thay lông*;
  - sáu có cờ H5 theo bảng ứng viên của Astra, ví dụ *rướn*/*dướn*. Các cờ này phải khép ở A9.
- Kịch bản 141 từ của Astra (117 từ có thể cân nhắc + 24 dự phòng) chỉ cần đến khi luật K1 của Astra được chọn.
- 24 từ dự phòng trong kịch bản của Astra trùng đúng 24 từ vào đầu tiên của Opus.

## 3. Lỗi trong phân tích của Astra

| # | Lỗi | Chứng cứ [đã kiểm] |
|---|---|---|
| L1 | Mở lại sáu quyết định K2 đã có hai chữ ký (cả chữ ký của Astra) mà không có chứng cứ mới: *bình, thầy, thổi, khảm, kính, di động* | `chu-ky.tsv:134–135, 786–787, 1270–1271, 1338–1339, 2152–2154, 2198–2199`; nguồn mới chỉ nhắc lại nhãn cũ |
| L2 | K1 cho 22 khóa có r < 0,035, trái chữ "hiếm → K2" và trái tiền lệ *thây*, *bĩnh*, *bịnh* | `doi-chieu-h7.tsv` |
| L3 | `ly_do` là câu mẫu theo nhóm: 140 dòng K1 chỉ dùng 11 câu khác nhau. Các câu này khẳng định "tự nhiên" mà không dùng số đo nào. Ví dụ *thầy*/*thây* bị ghi "tự nhiên", trong khi bản ký ghi tỷ lệ 0,1% | `h7-sang-loc-1177.tsv`, `h7-sang-loc-bo-sung.tsv`; `chu-ky.tsv:2153` |
| L4 | Xếp đỏ những cách đọc trái H6 hoặc trái tiền lệ: *đông y*, *dược*, *cờ trắng* (tiền lệ *đô đốc*), *động dục* (tiền lệ *động tình*), *ngai*, *trẫm* (chủ dự án đã giữ *công chúa*, *hoàng tử*, *hoàng hậu*) | `canh-bao-khong-dau.tsv`; `tieu-chi-thong-nhat.md:143–152` |
| L5 | Ghi K0 cho *bỏ mẹ* dù nguồn chỉ ghi *offensive* | enwiktionary rev 84835723 |
| L6 | Chưa soát 332 cách đọc HND cùng khóa với từ chính: 237 có dòng UNG_VIEN trong `opus-counts.tsv`, 95 không có dòng nào. H7 đòi so với mọi mục từ điển. Opus đã đọc cả 332, không thấy K1 | `sang-loc-h7.tsv`, `nguon_cap = HND_THIEU` |
| L7 | Chấm lại P6 đẩy *do đó* ra mà không có lỗi cổng | mục 2.4 |
| L8 | Q-rtc-A1 và Q-rtc-A2 đặt cho chủ dự án trước khi hai SA hòa luật K1, mà cả hai câu đều phụ thuộc vào luật đó | mục 5 |

## 4. Sửa phân tích vòng 1 của Opus

| # | Sửa | Hệ quả |
|---|---|---|
| S1 | Bỏ mốc r ≥ 0,2 và quy tắc "một âm tiết luôn là K2"; dùng thước hai trục ở mục 2.1 | Thêm 37 K1, ví dụ *nhàu, cuốc, bố mẹ, bảo hành, báo động, đánh bại, hâm mộ, ăn diện, dàn ý, mời mọc* |
| S2 | Sót K0 *phản bác*/*phân bắc* và *tính khí*/*tinh khí* | Thêm 2 từ thay |
| S3 | Chỉ quét dưới 0,3 PPM theo từ vựng, bỏ sót còi tương đối (PPM của cách đọc ≥ PPM của mục) | Có 20 dòng; chỉ *hững hờ*/*hùng hổ* có nét đỏ, Opus xếp K2. Thêm K2 cho *đề cử*/*dê cụ* và *đông đúc*/*động đực* |
| S4 | Sót cách đọc đỏ trong 1.177 cặp: *ân điển, dân ý, moi móc, bá chủ*. Còn khoảng 25 cách đọc trước đây ghi không đỏ, nay là K2 (ví dụ *chông, gian, choáng, chưởng*) | Cập nhật `doi-chieu-v2.py` |
| S5 | Luật "dạng kia chỉ có trong HND 39K/74K thì là loại d" trái tiền lệ: 34 lần c so với 3 lần d (`spelling_families.tsv`) | Thêm thay *co rúm, xù xì, rầm rộ, chơ vơ, xập xình, su hào, loay hoay*; bỏ bốn ca "cần hai chữ ký" |
| S6 | Bỏ sót *phí phạm*/*phí phạn* và *dây chun*/*dây thun*; nhận thêm *xà bông*/*xà phòng* | Thêm 5 từ thay |
| S7 | *sắn dây*: H6 nhóm 10 không loại tên con vật (*bọ chét*). *chung cư*: *chứng cứ* là bằng chứng nói chung. *già dặn*: *già giặn* có mục Wiktionary riêng với nghĩa khác, đúng luật Opus đã dùng cho *bóng láng* | Bỏ 3 từ thay; *sắn dây* và *chung cư* chuyển sang K2 |
| S8 | *thiện chí*/*thiện trí*: *thiện trí* chỉ là tên riêng | Bỏ đăng ký QUA |
| S9 | Kế hoạch D6 ghi "tải bản Kaikki mới, khác băm thì ghi bản mới" là sai: `d6-kiem.py` dừng an toàn khi snapshot khác bản đã ghim | Phải khôi phục đúng `1f0abd…`. Nếu không khôi phục được, dừng và trình chủ dự án |
| S10 | Ước lượng việc: lô viết sạch khoảng 111 từ (86 từ vào + 25 dự bị), soát D7 nhiều hơn | Khoảng 12–22 lượt agent |

**Kết quả Opus v2:** 86 từ thay. Danh sách nằm ở `evidence/de-xuat-thay-v2.log`:

- 65 K1;
- 2 K0;
- 19 H5:
  - *chòng chành, bồ kết, rau dền, ngoảnh, phấp phới, cải xoong, lấn át, loay hoay, co rúm, xù xì*;
  - *rầm rộ, chơ vơ, xập xình, su hào, dây chun, dây thun, phí phạm, xà bông, xà phòng*.

Cần hai chữ ký K2 mới cho 93 từ (186 dòng). Astra đề nghị K2 cho khoảng 170 khóa. Phạm vi ký sẽ hòa ở bước báo cáo chung; việc này không làm đổi danh sách thay.

## 5. Danh sách câu hỏi hợp nhất

| Mã | Gửi | Trạng thái | Nội dung và đề nghị |
|---|---|---|---|
| Q-rtc-O1 | SA-Fable | **Thêm**, chỉ hỏi nếu bước báo cáo chung không hòa | Luật K1 của H7: thước hai trục của Opus (nghĩa chính nặng và r ≥ 0,035; chữ ký K2 cũ giữ nguyên) hay luật của Astra (thuộc nhóm đỏ là K1, mở lại chữ ký cũ). Hệ quả: 86 hay khoảng 141 từ thay; có cần mở lại từ có thể cân nhắc hay không. Opus đề nghị thước hai trục vì nó khớp chữ của H7 và mọi tiền lệ đã ký trừ một ca. Câu này chặn danh sách cuối và Q-rtc-A1, Q-rtc-A2 |
| Q-rtc-O2 | SA-Fable | **Thêm**, chỉ hỏi nếu không hòa | P6: giữ điểm đã khóa và lấp từ dự phòng (Opus, theo `tieu-chi-thong-nhat.md:307`, `:427`) hay chấm lại S2/S3 trên rổ mới (Astra). Hệ quả: *do đó* ở lại hay bị thay; có thay đổi phụ ngoài các lỗi cổng hay không. Opus đề nghị giữ điểm đã khóa và chạy C13 để kiểm sức chứa |
| Q-rtc-A1 | Chủ dự án | **Giữ, có điều kiện**: chỉ hỏi nếu kết luận Q-rtc-O1 xếp *gián*/*gian* là K1 | Theo Opus, *gian* là K2: nghĩa chính là gian nhà, gian hàng; nghĩa dối trá chủ yếu nằm trong từ ghép. Nếu thành K1 thì cần chủ dự án, vì quyết định 5 (`WordListAnalyze.md:150`) đã giữ *gián*. Khi đó Opus nghiêng về thay để H7 nhất quán, nhưng quyền quyết là của chủ dự án |
| Q-rtc-A2 | Chủ dự án | **Giữ, có điều kiện**: chỉ hỏi nếu số ghế cần thay vượt dự phòng đủ điều kiện | Với 86 từ thay, dự phòng đủ và còn 25 mục dự bị, nên chưa cần. Nếu luật của Astra được chọn thì thiếu khoảng 21 ghế không-F; khi đó mở lại từ có thể cân nhắc là việc của chủ dự án, vì làm thay đổi kết quả P7 (D6_CUOI) |
| Q-rtc-A3 (rủi ro) | Chủ dự án | **Thêm, có điều kiện** | Nếu không khôi phục được snapshot Kaikki `1f0abd…` cho D6 thì phải đổi nguồn D6 đã ký. Chỉ hỏi khi rơi vào trường hợp đó |

Câu đã rút: không. Vòng 1 Opus không có câu hỏi nào để rút.

## 6. Chứng cứ và cách chạy lại

Đường dẫn tính từ thư mục này. Chạy từ `evidence/` (cần `HND_DIR` cho script thứ hai):

```powershell
python doi-chieu-astra.py      # cần doi-chieu-v2.py, de-xuat-thay-v2.tsv
$env:HND_DIR = '<ngoài repo>\hnd-tam'; python de-xuat-thay-v2.py
```

| Tệp | Nội dung |
|---|---|
| `evidence/doi-chieu-h7.tsv` | 349 khóa chính: kết luận vòng 1 của hai bên, lập trường v2 của Opus, các cặp lệch kèm r, lý do |
| `evidence/doi-chieu-h5.tsv` | 60 cặp khác nhau về cùng/khác từ, loại, hành động; cột HND chỉ viết hoa |
| `evidence/doi-chieu-thay.tsv` | Danh sách ra và vào: Opus vòng 1, Astra, Opus v2 |
| `evidence/doi-chieu-v2.py` | Thước hai trục và phán quyết v2 từng khóa và cặp |
| `evidence/de-xuat-thay-v2.py`, `.tsv`, `.log` | 86 từ ra, 86 từ vào, 25 dự bị, cờ cần đọc |
| `evidence/doi-chieu-astra.py`, `.log` | Phép ghép và số tổng |

Nguồn ngoài repo đã dùng và đã xóa: bốn danh sách HND. Các revision Wiktionary đã tra (chỉ nhãn và đầu mục), ngày 21/11/2026:

- vi.wiktionary: *phân bắc* 1892186, *tinh khí* 1930782, *chun* 2034319, *thun* 2418418, *phí phạn* 1314795;
- en.wiktionary: *bỏ mẹ* 84835723, *đi đồng* 84662196, *thun* 93727986.
