# Dự phòng v2 — báo cáo chung, bản sửa 1

**Status: Draft (round 1).** Phân tích ngày 20/11/2026, cập nhật 21/11/2026. **Soạn:** SA-Astra; **đồng tác giả phân tích:** SA-Opus. Lượt duyệt 3 yêu cầu giữ lý do trong bảng công bố; Astra đã áp nguyên văn 30/8 ghi chú và bổ sung kiểm T10, chờ kiểm lại riêng điểm này. Chưa chuyển Final hoặc phát hành. **Base:** `cefb99386d4845e40bc2d3eabc7d6898d078305d`.

## Tóm tắt

- Giữ nguyên 7.776 từ chính, toàn §10 và `du-phong.txt` 205 dòng; chưa sửa tài liệu phát hành.
- **11 lệch tầng cũ đã đóng:** tám mục về A, ba mục về D; thống nhất mốc A149/B36/C14/D6. TT2 rút, S4 giữ nguyên.
- Ca **ngoại trừ/ngoại trú** đã được hai SA chốt C/CHO_H7, không dùng trước khi đo và ký mức K. Tầng cuối: **A148/B36/C15/D6**, không còn CHO_HOA.
- **HM N=237**: 120 D6, 10 D7, 107 R1. Bảng hồ sơ vẫn 285 dòng; 48 dòng không tính gồm 46 L3b, chạng vạng và bao tử.
- Astra đồng ký K2 cho `tanso`, `vaynen`; hai SA nhận K1 cho `baotu`; nhận phương án giữ sáu HM có cờ rà H6. Q-dpv2-2 đến Q-dpv2-6 đã đóng.
- **Không còn câu hỏi mở.** Chủ trả lời “3” cho Q-dpv2-1 ngày 20/11/2026, lưu tại `1734b43`: chuyển phát hiện sang yêu cầu rà/thay chính riêng, không làm trong dự phòng v2. Q-dpv2-7 đã đóng bằng T-dpv2-9; việc đo để khép H7 vẫn để sau.
- Kiểm LF nguyên mã và kiểm `build_wordlist.py --check` trên tài liệu đã sửa được mô phỏng trong bộ nhớ; byte bảo vệ không đổi. Lỗi CRLF nền và giới hạn build trên bản LF được ghi riêng.

**Quy ước:** `verified` là đối chiếu dữ liệu/mã/hồ sơ; `assumed` là nhận định ngôn ngữ, không phải phép đo nghĩa đỏ. “Cùng đề cử” không phải phê duyệt phát hành. `AT = analyzing-tools`; `U = AT\ho-so\unified`; `O = AT\ho-so\opus\du-phong-v2`; `OE = O\evidence`; `A = AT\ho-so\astra\du-phong-v2`; `E = A\evidence`.

## 1. Đồng thuận và dữ kiện đã kiểm lại

### 1.1. Phạm vi

- **verified — chủ đã chốt:** chỉ phân tích/phân loại; chính bất biến; HM khoảng 100–300; không tạo docs mới.
- Hai SA giữ `du-phong.txt` 205 dòng/SHA và khối 205 từ ở §11.5; D chỉ nằm trong bảng phân loại, không xóa dấu vết lịch sử.
- Tên công bố là `AT\du-phong-phan-loai.tsv`, `AT\honorable-mentions.tsv`; cập nhật tài liệu hiện có sau khi kế hoạch được chốt.
- Không sửa nhãn, D8, bảng khóa/họ dùng cho phát hành hoặc công cụ trong đợt này. Không viết nghĩa, không tự mở ngoại lệ D7.
- Hai tài liệu lưu trữ `WordListAnalyze-Opus.md:265`, `WordListAnalyze-Astra.md:95` và quyết định 10 `WordListAnalyze.md:153` giữ nguyên. Trạng thái hiện hành về sau đọc ở §11 mới.

### 1.2. Số liệu

**verified**, kiểm từ tệp gốc, không chỉ chép báo cáo:

| Tập | Giá trị |
|---|---|
| Pool P6 / bảng xếp hạng sau v2 / rổ P0 cuối | 10.156 / 10.133 / 10.001 |
| Chính | 7.776 = 7.699 OK không-F + 77 OK-F; R1 = 0 |
| Dự phòng | 205 = H85 + K43 + F77; không có lớp C |
| Câu dự phòng có hồ sơ đạt | 168: v1 123, v2 35, v3 10; D7 không CHAN; 4 HAI_NGHIA |
| Chưa có câu / D8 dự phòng | 37 đều F / 0 dòng |
| Mức A chung hiện tại | 109 không-F + 39 F; ngoại trừ ở C/CHO_H7 |
| Ngoài chính/dự phòng sau trừ lỗi nghĩa | 159 OK-F + 1.839 R1 không-F + 22 R1-F |

40 mục F có câu lịch sử chỉ có thể phủ tối đa 40 ghế F riêng biệt, không thành 77 phép thay; hiện một trong số đó còn cần khép H7. OK không-F có thể thay C/H/K hoặc F; OK-F chỉ thay F khi Q3 đang đầy; R1 chỉ thay R1 trong quy trình dự phòng hiện hành.

Nguồn: `U\p7-v3-c13-hoa-astra.json`, `U\p6-tinh-doc-lap-astra.py:61–104`, `E\inventory.json`, `E\joint-summary.json`, `E\cross-review-verification.json`. Không dùng số câu/SHA lịch sử để tuyên bố D8 hoặc D6 mới đã hoàn tất.

### 1.3. H8 và quy ước mẫu số

**verified:** mã P2 v4.1 vẫn là **198 MANH, 4 YEU, 2 CHI_BE_MAT, 1 KHONG_LUOT** cho dự phòng. Cả nghĩ/tối mù là CHI_BE_MAT; ăn nhịp có ngoại lệ không-lượt đã ký. Với 237 HM được tính, có 236 MANH và 1 CHI_BE_MAT (*vây cá*), kèm hồ sơ đọc kiểm đã đóng.

- Nhãn H8 theo `U\tap-luat-P2-v4.json`, `hop_dong[12]`: mẫu số 34.329.387 phụ đề mọi dòng, 150.070.912 web dòng khác nhau; phụ đề dòng khác nhau 27.978.808.
- Khảo sát PPM gộp H7 trong hồ sơ này ghi rõ mẫu số mục 0 của tiêu chí/manifest: 34.314.528/149.860.716. Không trộn hai bộ hoặc gọi tên cột cũ là thẩm quyền cho mọi phép tính.
- Astra tính lại cả hai bộ cho các khóa đang xét và tập hậu kiểm: không đổi quyết định mốc còi hay tập 1.177 cặp. Không sửa ngược log/metadata cũ.

Nguồn: hai `U\cong-*-v4.tsv`, `E\revision-1-h7-counts.tsv`, `E\revision-1-audit.json`. Kiểm D2/D5/cờ 7.944 câu hiện có vẫn là 0 lỗi/0 cảnh báo trong hồ sơ; không phải một lần D6 mới.

## 2. Bảng tầng theo từng từ

Bảng đầy đủ: [`du-phong-v2-phan-loai.tsv`](du-phong-v2-phan-loai.tsv), **205 dòng**, giữ đúng từ/thứ tự của du-phong.txt. Hai cột ý kiến phản ánh vị trí mới nhất; các phân tích độc lập và diff vòng 1 vẫn giữ làm lịch sử.

**Đã bổ sung lý do công bố:** cột `ghi_chu` có đúng 30 văn bản được chốt ở Lượt duyệt 3 §D, gồm mọi C/D và các đầu mục có quyết định riêng. Khi bỏ hai cột ý kiến để xuất bảng gọn, vẫn sao chép nguyên `ghi_chu`; bảng cảnh báo §11 có 21 dòng C/D và cột Lý do, không chỉ còn mã D8/H5 chung.

| Mốc | A | B | C | D | Chờ hòa |
|---|---:|---:|---:|---:|---:|
| Opus đề xuất trước review bản chung | 141 | 36 | 25 | 3 | — |
| Astra trước review bản chung | 149 | 36 | 14 | 6 | — |
| Hai SA sau đóng 11 lệch cũ | 149 | 36 | 14 | 6 | 0 |
| Bản sửa 1 sau phát hiện ngoại trừ | **148** | **36** | **14** | **6** | **1** |
| Sau đóng Q-dpv2-7 | **148** | **36** | **15** | **6** | **0** |

- **D cùng nhận:** chán phèo, chọc lét, hì hụi, nhão nhẹt, nhão nhoẹt, tròng trành.
- **C cùng nhận:** ăn nhịp, cả nghĩ, chễm chệ, cửu chương, loằng ngoằng, lỗi hẹn, lời lỗ, mỏng tanh, ngoại trừ, tạnh ráo, thẳng đơ, thụp, tối mù, trở lên, tuổi xanh.
- B36 cộng trở lên ở C vẫn là **37 chưa viết**.
- **Đã chốt:** ngoại trừ có Opus C/Astra C, `trang_thai_h=CHO_H7`, `tranh_chap=KHONG`. Hết bất đồng không đồng nghĩa H7 đã đạt; không tự kết luận K1/K2.

### 2.1. Lịch sử 11 điểm đã hòa

| Từ | Opus trước | Astra | Kết luận chung | Căn cứ đóng |
|---|---|---|---|---|
| ăn trầu | C | A | A | Chưa có phản đối H6 mới đủ căn cứ; rút khẳng định y khoa về chất gây nghiện |
| bèo bọt | C | A | A | Nhận lần rút C của Astra |
| chấp nhặt | C | A | A | Như trên |
| giở giọng | C | A | A | Như trên |
| giở quẻ | C | A | A | Không suy nghĩa nghi lễ từ một tiếng |
| hì hụi | C | D | D | Hai SA ký họ **hì hụi/hè hụi**; không suy hì hục cùng họ |
| mụ mị | C | A | A | Nhận lần rút C; không phục hồi phản đối H5 cũ |
| nhão nhẹt | C | D | D | Hai SA xác nhận biến thể cùng từ; số sạch không đạt H5c |
| nhão nhoẹt | C | D | D | Như trên, kể cả số nhão nhoét cùng khóa |
| non choẹt | C | A | A | Nhận lần rút C |
| tía lia | C | A | A | Nhận lần rút C |

Nguồn: `O\round-1-review-drafts.md:64–81`, `A\round-1-revision-1.md`; các quyết định T-dpv2-4/5 trong kế hoạch. C chỉ là cảnh báo, không tự sửa S4 hoặc ban hành TT2. D cũng không bị xóa khỏi tập đối chiếu 205.

## 3. Honorable mentions: N và số dòng hồ sơ khác nhau

Bảng hồ sơ [`du-phong-v2-honorable-mentions.tsv`](du-phong-v2-honorable-mentions.tsv) giữ **285 dòng** để lưu cả quyết định không nhận. Chỉ dòng `ket_luan_nhap=CUNG_DE_CU_CHUA_PHAT_HANH` được xuất vào bảng công bố ở AT.

| Nhóm hồ sơ | Tổng dòng | Tính vào N | Không tính |
|---|---:|---:|---|
| D6_CUOI | 122 | **120** | bao tử: LOAI_K1; chạng vạng: NGOAI_HM_CHO_H5 |
| D7_CUOI | 10 | **10** | — |
| R1 | 107 | **107** | — |
| L3B_CHUA_CHAM | 46 | **0** | NGOAI_HM_CHUA_THAM_DINH |
| **Tổng** | **285** | **237** | **48** |

**Đã chốt:**

- Q-dpv2-4 phương án 2: L3b và chạng vạng không được tính là HM đủ thẩm định; lớp L3b chỉ là đề xuất, DF/F còn thiếu. Giờ cao điểm bị hai SA phản đối H2; ớt đỏ/nắng ấm vẫn cần xét X.
- Baotu là K1: không tính bao tử, không đổi sang bào tử để né khóa.
- Tần số được hai SA ký K2 “không tự động chặn”; vẫn R1, không tự có ghế thay OK.
- Cả sáu cơ quan/lực lượng/truy tìm/dự bị/lên chức/đại lục được giữ với cờ rà H6 trước khi dùng. Hai phiếu P4 lần lượt OK/OK cho năm mục đầu, R1/R1 cho đại lục; không có phản biện trong bảng P4 lưu. Các lo ngại mới chưa đủ làm phản đối H9. Không vì thế tuyên bố mọi ngữ cảnh của sáu từ đều lành.

**verified:** N=230 cùng đề cử ban đầu + tần số + sáu mục H6 = **237**. N không còn phụ thuộc một câu hỏi Q-dpv2-6 chưa trả lời.

Tám ghi chú HM (sáu cờ H6, tần số K2, vây cá CHI_BE_MAT) được giữ nguyên trong bảng công bố; 229 mục còn lại ghi `-`. T10 kiểm cả phép chiếu 237 dòng, không nhầm 285 dòng hồ sơ với bảng công bố.

**Lịch sử viết:** cả hai xác nhận 131/132 mục lỗi nghĩa có log v1/v2/v3, riêng mặt khác chỉ có v2/v3 và không có ở danh sách viết lại v1. Khi khôi phục phải kiểm lịch sử đúng từ/quyền mở lượt; không khẳng định cả 132 đã hết hai lượt viết lại. Đợt này không mở viết.

## 4. Lịch sử đóng câu hỏi và việc còn mở

### 4.1. Q-dpv2-1 — đã đóng, D-dpv2-5

**Trước:** Opus muốn ghi nhận rồi hậu kiểm giới hạn; Astra không mở thêm công việc trong đợt này nếu chủ chưa giao.

**Quyết định chủ:** chọn phương án **3**, “Yêu cầu rà/thay chính riêng”, ngày 20/11/2026 khoảng 22:40 +07:00. Toàn bộ câu hỏi và Answer nằm ở `1734b43:analyzing-tools/ho-so/unified/du-phong-v2-cau-hoi.md`. Astra kiểm lại và **accept**: họ chòng chành/tròng trành, 632 cặp H5 thô, 1.177 cặp H7 và ca báo tử được bàn giao cho yêu cầu riêng, với P6/P7/phát hành; không mở rộng dự phòng v2 hoặc thay chính tại đây.

**verified:** bộ sinh H5 thô có 632 cặp/474 từ chính. Khảo sát H7 có 1.177 cặp/634 khóa chính đạt mốc PPM nhưng chưa có dòng trong bảng còi; bảng còi có 227 dòng/117 khóa. `E\revision-1-audit.py` tính lại độc lập, khớp tập chứ không chỉ tổng số.

**Không suy thành lỗi:** chưa phân loại nghĩa đỏ của 1.177 đối chứng, không gọi đó là 1.177 còi bắt buộc bị bỏ sót. Số 632 cũng không phải số họ H5 đã xác nhận. Câu hỏi đã ghi phạm vi, chi phí sàng lọc, bước giới hạn ban đầu và quyền giao tiếp của chủ.

### 4.2. Q-dpv2-2 — đã đóng, T-dpv2-4

**Trước:** Opus C/Astra D cho hì hụi, nhão nhẹt, nhão nhoẹt; vướng chuẩn xác nhận cùng từ.

**Sau:** Opus ký họ hì hụi/hè hụi theo liên kết từ vựng và HND; ký nhão nhẹt/nhão nhoẹt là biến thể cùng từ theo nhận định ngôn ngữ. Cả ba về D theo H5c. Không còn câu hỏi H9 ở các ca này. Không ai kết luận hì hục chính sai H5.

### 4.3. Q-dpv2-3 — đã đóng, T-dpv2-4/5

**Trước:** Opus hợp các C, Astra đã rút tám cảnh báo thiếu căn cứ H6 mới.

**Sau:** tám mục về A; Opus nhận đây là lệch thời điểm. C là nhãn cảnh báo; TT2 rút, S4 không đổi. Các nhận định sắc thái cũ vẫn truy được ở hồ sơ.

### 4.4. Q-dpv2-4 — đã đóng, T-dpv2-6

**Trước:** Opus muốn HM có điều kiện cho 46 L3b và chạng vạng; Astra chỉ tính mục đủ thẩm định.

**Sau:** cả hai chọn phương án 2. Những dòng này ở hồ sơ, §12.3 ghi số lượng/nguồn và lý do không tính; không ghi PASS hoặc giả DF bằng 0. Giờ cao điểm không đáp ứng H2 ba khối theo luật hiện hành.

### 4.5. Q-dpv2-5 — đã đóng, T-dpv2-7

**Trước:** Opus để bao tử chờ K1/K2, chưa khép tanso/vaynen; Astra đề nghị K1 baotu và chữ ký cụ thể cho hai ca kia.

**Sau:** K1 baotu được hai bên nhận. Opus ký K2 ở `O\round-1-review-drafts.md:95`; Astra đồng ký tại `E\revision-1-chu-ky-astra.tsv:2–3`.

Lý do ký: tận số/vảy nến là nghĩa đỏ được thừa nhận nhưng ít gặp, khoảng 0,207/0,253 PPM và thấp hơn nhiều cách đọc tần số/vậy nên; không thuộc ngoại lệ tự hại/bạo lực/tình dục. Đây là đánh giá K2 có lý do và hai chữ ký, **không** suy PASS chỉ từ “dưới 0,3”. Vậy nên vẫn B/chưa viết nghĩa.

### 4.6. Q-dpv2-6 — đã đóng, T-dpv2-8

**Trước:** Opus giữ năm mục OK nhưng bỏ đại lục; Astra giữ đại lục và tạm không ưu tiên năm mục.

**Sau:** Opus rút ngoại lệ không nhất quán về đại lục; Astra nhận phương án 1 cho cả sáu. Dữ liệu P4/H9 đã kiểm lại; chưa có chứng cứ mới đủ phản đối H6. Giữ cả sáu, giữ cờ rà H6, không xóa nhãn lịch sử và không diễn giải việc đề cử thành quyền phát hành.

Nguồn: `O\round-1-review-drafts.md:101–108`; `E\revision-1-h6-six-votes.tsv`; `A\round-1-revision-1.md`.

### 4.7. Q-dpv2-7 — đã đóng, T-dpv2-9

**verified:** `OE\h7-quet-bo-sung.tsv:36` đánh giá ngoại trú không đỏ vì “không phải bệnh”. Đối chứng có 9/325 lượt sạch, khoảng 1,21548 PPM (mục 0) hoặc 1,21390 (P2), trên mốc còi. Nguồn từ vựng có nghĩa học đường và nghĩa điều trị; chỉ lưu URL/phạm vi nghĩa, không sao chép định nghĩa.

- **Trước review:** Opus giữ A/không đỏ; Astra đề nghị C/CHO_H7 vì H6.5 gồm y khoa chuyên biệt và phải đối chiếu tiền lệ nội trú.
- **Sau Lượt duyệt 2:** Opus rút nhận định “không phải bệnh; không đỏ”, nhận nghĩa điều trị thuộc phạm vi H6.5 theo tiền lệ đã đồng ký. Hai SA chốt ngoại trừ **C/CHO_H7**.
- **Điều kiện trước khi dùng:** đo tỷ lệ nghĩa điều trị của ngoại trú ở web như tiền lệ nội trú; sau đó hai SA ký K1, K2 “không tự động chặn” hoặc “không tự động”. Opus nghiêng K2 nhưng **chưa ký**; không ghi K2 đã đạt.
- **Giới hạn:** không lấy số của toàn chuỗi làm tỷ lệ nghĩa y khoa; không suy tỷ lệ của nội trú sang ngoại trú; không tự kết luận K1 từ 0,3.

Không còn CHO_HOA; Q-dpv2-7 đóng tại review, không gửi SA-Fable. Việc đo/ký H7 được giữ thành OI-H7-NGOAITRU, không mở tự động và không ảnh hưởng N HM.

Astra cũng đã đọc cặp móng/mông ở G5: đồng ý đánh giá bộ phận cơ thể thông thường không tự là nghĩa người lớn; không ký trắng kết luận ngữ nghĩa cho toàn bộ các cặp thô còn lại.

## 5. Đăng ký bảng phát hành và kiểm tương thích

**Để sau:** khi có tác vụ thay từ, đăng ký các họ H5 chỉ chạm dự phòng và khóa `baotu` vào bảng phát hành. Họ chòng chành/tròng trành cần quyết định riêng: thêm LOAI vào bảng hiện hành sẽ khiến C5 báo lỗi ở chính. Không né bằng cách nới checker hoặc đổi chính trong nhiệm vụ này.

**Đã bổ sung phép kiểm:** `build_wordlist.py --check` chạy trên tài liệu mô phỏng **đã sửa**, ở chế độ CRLF, phải báo “Ba khối khớp wordlist.txt.”. Ở bản tất cả LF, script có giới hạn CRLF ngay từ nền; ghi cùng lỗi trước/sau, không dùng kết quả ấy làm lỗi hồi quy.

Tất cả mô phỏng của Astra nằm trong bộ nhớ. Checker Python/JS với đúng blob nguồn LF đạt; native checkout giữ lỗi C1/C8 nền; byte của ba tệp chính, §10 và hai tài liệu lưu trữ không đổi.

## 6. Bước tiếp và bằng chứng

1. Ghi T-dpv2-9 và đóng Q-dpv2-7 theo Lượt duyệt 2 đã accept; không gửi lại các câu đã đóng.
2. Bàn giao các phát hiện cho yêu cầu rà/thay chính riêng theo D-dpv2-5; không chạy quét/đo hoặc thay chính trong dự phòng v2.
3. Giữ các tầng/trạng thái đã thống nhất và chỉ xuất **237 dòng được tính** ra bảng HM công bố ở bước được giao. Hai SA xác nhận bản cập nhật quyết định chủ; điều phối chuyển Final sau sign-off và thực hiện các bước nghiệm thu/commit tương ứng. Status hiện vẫn Draft.

Kế hoạch: [`du-phong-v2-ke-hoach.md`](du-phong-v2-ke-hoach.md). Tệp câu hỏi (không còn câu mở): [`du-phong-v2-cau-hoi.md`](du-phong-v2-cau-hoi.md).

Evidence bản sửa: `E\revision-1-audit.py`, `revision-1-audit.json`, `revision-1-h7-counts.tsv`, `revision-1-h6-six-votes.tsv`, `revision-1-chu-ky-astra.tsv`, `revision-1-h7-ngoaitru.tsv`; code dựng/kiểm `E\joint-build.py`, các `joint-*.json` và `joint-proof.log`. Các bản lưu câu hỏi cũ ở `E\revision-1-question-history.json` được giữ làm lịch sử; Q&A cuối của chủ nằm trong `1734b43`. Status vẫn Draft, chưa thực hiện yêu cầu riêng.
