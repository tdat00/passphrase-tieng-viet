# Rà và thay danh sách chính — phân tích độc lập vòng 1

**SA-Astra — 21/11/2026.** Base: `1c3f50406f5115f5c33ca87c8534831b011e2b10`, nhánh `analyze/ra-thay-chinh`. **Chưa phải kế hoạch Final, chưa phải phê duyệt thay từ.** Không đọc thư mục `opus\ra-thay-chinh`.

Quy ước: **verified** = đã kiểm số, mã, nguồn hoặc trạng thái hồ sơ; **assumed** = nhận định ngôn ngữ/độ thông dụng, giả định hoặc đề xuất của Astra, chưa có chữ ký chung. Một nguồn chứng thực nghĩa **không** chứng minh tỷ lệ nghĩa đó trong kho.

Đường dẫn viết tắt: `AT = analyzing-tools`; `U = AT\ho-so\unified`; `A = AT\ho-so\astra\ra-thay-chinh`; `E = A\evidence`. Mọi số dưới đây là số của base trên, không phải dự báo chắc chắn cho bản phát hành.

## 1. Tóm tắt

1. **[verified]** Tái lập đúng 632 cặp H5/474 từ chính và 1.177 cặp H7/634 khóa; không coi số đầu vào là số lỗi.
2. **[verified]** 19 đối chứng H5 chỉ có dạng viết hoa trong HND; phép hạ chữ đã kéo tên riêng vào tập thô.
3. **[verified nguồn/số; assumed phán quyết]** Đề nghị thay tám từ qua bảy họ H5c; còn 44 cặp gốc và hai hướng bổ sung xà bông/xà phòng cần hòa/đo.
4. **[verified số; assumed phân loại]** Có 132 khóa chính được Astra đề nghị chặn qua H7; hợp H5/H7 là 140 từ, không phải 140 lỗi đã được hai SA ký.
5. **[verified]** `baotu` không thuộc chính và chưa có trong bảng chặn. Không được mô tả bao tử/báo tử như một từ chính cần thay.
6. **[verified]** Rà thêm 1.942 đối chứng có sẵn/thiếu đếm cho thấy phải xét K0 và còi dưới ngưỡng, không chỉ 1.177 cặp.
7. **[assumed]** Chưa nên Final: còn 87 từ chính có ca cần đo/hòa; gián cần chủ quyết vì quyết định giữ tại §3.5.
8. **[verified điều kiện]** Chỉ dùng A thiếu 29 ghế không-F; xét thêm dự phòng không bị giữ lại vẫn thiếu 21. Không lấy R1 lấp ghế OK.
9. **[verified điều kiện]** Nếu chủ mở lại HM OK, tính lại P6 cho 141 thay: 140 H5/H7 và do đó theo S4; vào 117 HM + 24 dự phòng, F=77, R1=0.
10. **[verified]** Chưa viết nghĩa, chưa chạy D6 mới; dump ghim vắng ở đường dẫn cấu hình, hai hash tham chiếu lệch do CRLF. Toàn bộ 24 tệp bảo vệ không đổi.

## 2. Hiểu yêu cầu

### 2.1. Mục tiêu và người dùng

- **[verified]** Thực hiện D-dpv2-5, không mở thêm T-dpv2-1 hay toàn bộ OI của dự phòng v2. Chủ cho phép thay chính **sau** Final và phê duyệt, kèm nghĩa viết mới đạt D6/D7. Nguồn: `U\ra-thay-chinh-yeu-cau.md:13–15`, commit `1c3f504`.
- **[assumed]** Người dùng cần khóa không dấu dễ gõ lại và tránh cách đọc nhạy cảm; không chỉ một bản danh sách có đủ số dòng.
- **[verified]** Luật H1–H9, Q, S4 và D1–D8 còn hiệu lực. Không đổi ngưỡng, không dùng ba chữ, không tự chuyển R1 thành OK, không ưu tiên tầng A thay cho S4.
- **[verified]** Quyết định 10 bỏ yêu cầu đủ 300 dự phòng, **không** bỏ yêu cầu đủ 7.776 từ hay các cổng khác (`WordListAnalyze.md:155`).

### 2.2. Trong/ngoài phạm vi

**Trong [verified yêu cầu; assumed thiết kế]:**

- Sàng lọc toàn bộ hai tập đã bàn giao; xét thêm cách đọc cần thiết để thực thi K0/H7, kể cả dưới 0,3 PPM, và kiểm lại ứng viên thay.
- Đăng ký họ/khóa mới có quan hệ với chính hoặc ứng viên của đợt; phối hợp thay dữ liệu, không chỉ sửa bảng để C5 đột ngột trượt.
- P6 mới, lượt nghĩa sạch, D8, sinh khối, C1–C13; cập nhật trực tiếp tài liệu/tệp hiện có và hồ sơ chung `U\ra-thay-chinh-*`.

**Ngoài [assumed ranh giới phù hợp yêu cầu]:**

- Rà toàn bộ H6 của mọi mục ngoài phạm vi H5/H7; mở rộng HM cho đủ một chỉ tiêu số lượng; viết nghĩa cho mọi dự phòng chưa cần dùng.
- Xử lý riêng ngoại trừ/ngoại trú, toàn bộ R1, L2D/L3b hay bốn họ D chỉ nằm ở dự phòng, trừ khi thật sự cần cho ghế thay của D-dpv2-5.
- Đổi thuật toán bốc từ, giao diện ứng dụng, trọng số S3, mục tiêu giấy phép hoặc các quyết định đã ghi của chủ.
- Sửa các phân tích gốc `WordListAnalyze-Opus.md`, `WordListAnalyze-Astra.md` hay sửa lịch sử dự phòng v2.

**Giả định có điều kiện [assumed]:** mô phỏng P6 ở §5.4 dùng nhánh chủ cho mở lại HM OK và cho thay gián. Cả hai **chưa được quyết định**. Các mục còn chờ được giữ trong mô phỏng cận dưới, không được suy ra là đã qua H9.

## 3. Hiện trạng và bằng chứng

### 3.1. Thành phẩm, dự phòng, rổ

| Dữ kiện [verified] | Giá trị | Chứng cứ |
|---|---:|---|
| Chính | 7.776, tất cả OK; C=2.915, H=3.169, K=1.615, F=77 | `E\inventory.json:1`; `AT\labels.tsv:1` |
| Dự phòng | 205; A148/B36/C15/D6; A không-F109, A-F39 | `E\inventory.json:1`; `AT\du-phong-phan-loai.tsv:1` |
| HM | 237; 130 OK và 107 R1; OK gồm C65/H38/K22/F5 | `AT\honorable-mentions.tsv:1`; `E\candidate-summary.json:1` |
| Hạng P6 lưu | 10.133 dòng; tái tính đúng F, điểm nguyên phần trăm và toàn bộ thứ tự | `E\p6-preview-summary.json:1`; `E\p6_preview.py` |
| H7 đã có số trên khóa chính | 3.074 cặp/1.635 khóa; tập 1.177 chỉ là một phần | `E\inventory.json:1` |
| HND bổ sung | 45 dạng cùng khóa chưa có dòng số đếm; sáu chỉ khác số dấu cách | `E\h7-hnd-chua-dem.tsv:1`; `E\hnd-metrics.json:1` |

**[verified]** Trong `xep-hang.tsv`, cột `vao=CHINH` khác danh sách hiện tại ở 127 từ: đó là hạng trước những thay đổi P7 cuối. Không lấy cột này thay cho `wordlist.txt`.

**[verified]** HND74K được tải vào RAM từ commit `688b0953c8cdb21ee090ce80b83cefdb052fe2cd`; SHA-256 khớp manifest: `b83d49308336f12ca46d06287d8db6e2cdc7a725d9a9dac56930051775fafb90`. Không lưu danh sách hoặc định nghĩa. Tái chạy bộ sinh trên đúng tập mặt chữ cho tập cặp khớp hoàn toàn 632 dòng.

### 3.2. Công cụ không tự quyết được nghĩa

- **[verified]** Python C5 đọc bảng chặn và họ đã đăng ký; C6 chỉ tính nhãn CHINH; C7 chỉ kiểm một phần D2/D5 (`AT\check_wordlist.py:120–160`).
- **[verified]** JS C5 chỉ đọc khóa chặn, chưa đọc bảng họ hay hạn mức; không được gọi JS là bộ kiểm đầy đủ H1–H9 (`AT\verify.mjs:63–67`).
- **[verified]** `build_wordlist.py` chỉ đồng bộ ba khối; không xác nhận nghĩa, H9 hoặc D8 (`AT\build_wordlist.py:22–76`).
- **[assumed thiết kế]** Cổng chấp nhận phải gồm hai phép tính P6 độc lập, hồ sơ H5/H7 được hai SA ký và kiểm gói thay theo bảng phân xử; không chỉ chạy hai checker công bố.

### 3.3. Nền kiểm và D6

| Lệnh/đối chứng [verified] | Kết quả hiện tại |
|---|---|
| Python native | exit 1, một lỗi C1 vì CRLF nguồn chuẩn |
| JS native | exit 1, C1 và hai lỗi C8 vì CRLF |
| `build_wordlist.py --check` native | exit 0, ba khối khớp |
| Python/JS với đúng blob LF tại `1c3f504` trong RAM | Cả hai exit 0; không sửa tệp |
| `d6-kiem.py --self-test` | 20 ca tổng hợp đạt; **không phải** D6 của bản mới |

Nguồn: `E\validation.json:1`, `E\validation.log:1`.

**[verified]** `vi.jsonl.gz` không có ở đường dẫn cấu hình. ASTRA và FAMILIES có hash raw không khớp nhưng khớp khi chuyển đúng CRLF→LF; OPUS và GUIDE khớp raw, **không** khớp nếu chuyển LF mù. `d6-kiem.py:371–377` fail-closed khi sai/thiếu nguồn; `:528–532` còn ghim body của hai bản cũ, snapshot và GUIDE.

**[assumed thiết kế]** Phải khôi phục đúng snapshot và giải quyết định dạng/hash từng nguồn, không bỏ phép kiểm, không coi `CHUA_KIEM` là PASS, không dùng dump mới rồi giữ hash cũ. Nếu phải đổi snapshot/nguồn và phát sinh phạm vi nghĩa cần viết lại lớn, trình chủ trước.

## 4. Phương án

| Phương án [assumed] | Lợi ích | Chi phí/rủi ro | Kết luận |
|---|---|---|---|
| Chỉ thay chòng chành | Rất ít thay đổi | Không thực hiện đầy đủ D-dpv2-5, bỏ K0/H7 mới | Không chọn |
| Rà đủ, chỉ dùng dự phòng hiện có | Không mở lại ngân sách nghĩa của HM | Kịch bản Astra thiếu ít nhất 21 ghế không-F sau sàng lọc; 87 từ chờ có thể làm thiếu thêm | Chưa đủ sức chứa |
| Rà đủ; chủ cho một chu kỳ sạch mới cho HM OK cần dùng; xếp lại P6 | Tận dụng chứng liệu/nhãn có sẵn, giữ các luật H/Q/S; có thể điền đủ và tránh chỉ dùng dự phòng yếu | Cần quyết định D7 rõ, tái kiểm H1–H9 và nghĩa mới; không bảo đảm mọi HM sẽ qua | **Đề nghị** |
| Không mở lại HM; bổ sung OK mới ngoài các từ đã hết lượt | Không thay giới hạn viết lại lịch sử | Phải H3, đo bốn kho, hai phiếu P4/H9; chi phí và thời gian cao hơn | Phương án thay thế để chủ chọn |

Không lấy “còn hạn mức R1 388” làm quyền dùng R1 dự phòng thay OK. Không tự thêm ngoại lệ K0/K1 để giữ một từ quen.

## 5. Kế hoạch đề xuất

### 5.1. H5: phương pháp và kết quả

**[verified phương pháp]** Gắn ID H5-0001..0632; giữ nguyên hai đầu mục và nguồn cặp. Đối chiếu bảng họ đã ký, nguồn HND đúng chữ hoa/thường, Wiktionary đúng phần tiếng Việt và revision. Tách “khác từ”, “cùng từ”, “chưa xác nhận”; chỉ áp tỷ lệ sau khi xác nhận cùng từ. Không lấy ô trống làm 0; thun có số ở `U\l2-ung-vien.tsv:281` dù bảng thô trống.

**[verified số; assumed nhãn ngôn ngữ]** Toàn bộ 632 dòng ở `A\h5-sang-loc-632.tsv:1`:

| Nhóm | Số cặp |
|---|---:|
| Khác từ/không phải biến thể theo nhận định Astra | 557 |
| Tên riêng bị hạ chữ | 19 |
| Đã phân xử trong bảng H5 | 4 |
| Đề nghị loại theo H5c | 8 |
| Có căn cứ cùng từ, chờ đo/đọc nghĩa | 5 |
| Chờ xác nhận quan hệ, không tự tạo họ | 39 |

**Tám từ đề nghị thay [verified nguồn và cận số; assumed phán quyết chờ ký chung]:**

| Từ chính | Đối chứng | Căn cứ loại |
|---|---|---|
| bồ kết | bồ kếp | Nguồn ghi alternate spelling; mặt chữ phụ đề của bồ kết chỉ 1 |
| chòng chành | tròng trành | Họ đã được hai SA xác nhận ở dự phòng v2; tổng phụ đề 5, web 7 |
| dây chun | dây thun | Chun/thun là cùng danh từ theo nguồn; phụ đề cả cặp 16 |
| dây thun | dây chun | Cặp đối xứng; không đếm thành hai họ |
| ngoảnh | ngảnh | Nguồn ghi như ngoảnh; toàn bộ web cả cặp tối đa 9+2=11 |
| phấp phới | phất phới | Nguồn ghi như phấp phới; mặt chữ chính 7 phụ đề/10 web |
| phí phạm | phí phạn | Nguồn ghi biến âm; toàn bộ web của phí phạm tối đa 17 |
| rau dền | rau giền | Nguồn ghi alternative form; mặt chữ phụ đề rau dền bằng 0 |

**[verified]** Bổ đề dùng số nguyên: tổng cặp ≥20 và tỷ trọng ≥95% đòi hỏi dạng thắng có ít nhất 19 lượt. Nếu ngay cả số mặt chữ của dạng chính dưới 19 ở một kho, loại c không thể qua, kể cả cho toàn bộ lượt bị lọc trở lại. Không cần đoán số chưa đo của dạng kia để kết luận cận này. Kiểm tám ca trong `E\validate.py`; nguồn riêng trong từng dòng TSV, các `dictionary-*.tsv` lưu URL/revision/hash, không lưu lời giải.

**[assumed]** Không tự kéo hì hục vào họ hì hụi/hè hụi; không coi bóng láng/bóng loáng hay từ gần nghĩa là cùng từ chỉ vì bộ sinh đề xuất. Các đối chứng như thon thả/thong thả, lục lạc/nục nạc, sáng loáng/sáng láng là ví dụ cần loại khỏi quan hệ chính tả, không loại từ chính.

**[verified nguồn/số; assumed quan hệ]** Khi mở nguồn của xà bông trong tập gốc, tìm thêm nhánh **xà bông/xà phòng**; cả hai đang là chính. Bộ sinh không có phép đổi b/ph nên không trả cặp này. Hai hướng được giữ riêng trong `A\h5-sang-loc-bo-sung.tsv`, không sửa 632 ID gốc. Số sạch dạng có khoảng cách là 51/318 và 181/3.894 (phụ đề/web), nhưng H5f còn phải cộng đúng dạng gạch/viết liền và xác nhận quan hệ. Chưa gọi số dạng cách là kết luận cuối; không giữ cả hai nếu hai SA chốt đây là một họ H5f.

**Việc phải khép trước Final [assumed thiết kế]:**

1. Hai SA hòa 39 quan hệ và nhánh xà bông/xà phòng. Nếu khác từ thì đóng cặp, không sinh phép đếm lỗi.
2. Với cặp cùng từ, xác định c/d/f/e bằng nguồn; đo cả hai kho, phụ đề bỏ dòng trùng để thử độ nhạy.
3. Giữ ranh giới dấu câu và bộ lọc nghi vắt từ. Nếu kết luận phụ thuộc bộ lọc, đọc **mọi** lượt bị gắn cờ của dạng thiểu số; chỉ lưu ID/hash/nhãn đọc.
4. Năm cặp chờ đo gồm bít tết/bíp tết, hai hướng chun/thun, rong ruổi/giong ruổi, trưng bày/chưng bày. Riêng chun có nguy cơ lẫn tên riêng/nghĩa động từ: không dùng tỉ lệ thô để chọn thắng.
5. Cặp còn tranh chấp thực sự đi H9, không phát hành chỉ vì checker chưa biết họ. Không đăng ký tự động toàn bộ 632 cặp hay lan cấm theo chuỗi con.

### 5.2. H7: phương pháp, kết quả và baotu

**[verified phương pháp]** So **toàn khóa**, không tách ép hoặc kiểm chuỗi con. Tái tính PPM bằng phân số từ `opus-counts.tsv`; tập 1.177 khớp cả hai bộ mẫu số. Khảo sát dùng mẫu số mục 0: 34.314.528/149.860.716; H8 vẫn dùng P2 v4.1: 34.329.387/150.070.912. Không sửa ngược metadata lịch sử.

**[verified số; assumed phán quyết]**

| Tập | Không nhận diện đỏ | Đề nghị K0 | Đề nghị K1 | K2 đề nghị không chặn | Chờ nghĩa/đo | Phân xử cũ / chỉ khoảng cách |
|---|---:|---:|---:|---:|---:|---:|
| 1.177 đã bàn giao | 941 | 2 | 136 | 56 | 42 | 0 |
| 1.942 bổ sung | 1.723 | 3 | 4 | 149 | 8 | 49 / 6 |

Tập bổ sung = 1.897 dòng số đã lưu ngoài tập 1.177, cộng 45 dạng HND chưa có dòng đếm. **[verified]** Các dòng không có số là `CHUA_DO`, không phải 0. **[assumed]** Các nhãn không đỏ là kết quả đọc đầu mục của Astra, không phải chứng minh không tồn tại nghĩa khác. K2 trong bảng mới là đề nghị của Astra, **chưa** đủ hai chữ ký.

**Các ca minh họa quan trọng [verified nguồn/số; assumed áp mức K]:**

- phản bác ↔ phân bắc: 0/0 nhưng nguồn chứng thực toàn mục về chất thải; đề nghị K0 (`A\h7-sang-loc-bo-sung.tsv:1127`).
- tính khí ↔ tinh khí: PPM cả chuỗi 0,058284351; từ điển dẫn tới tinh dịch; đề nghị K0 (`:1438`).
- di động ↔ đi đồng: PPM 0,035815038; nguồn tiếng Việt của enwiktionary chứng thực nghĩa chất thải, không phải suy từ một thành tố; đề nghị K0 (`:1729`).
- hững hờ ↔ hùng hổ: PPM 0,247708492, **dưới 0,3 nhưng cao hơn mục chính**; còi tương đối bật (`:634`).
- gián ↔ gian: PPM **toàn chuỗi** gian 10,806597177; nguồn có nghĩa dối trá; đề nghị K1 cần quyết định riêng của chủ (`A\h7-sang-loc-1177.tsv:414`).
- Không tự chặn hang vì háng, giỏi vì giòi, cổ vũ vì có vú, hoặc một mục chỉ vì đối chứng chứa từ sinh học. Các cách đọc về cơ thể, danh tính, tên loài, từ dùng trong cụm và nghĩa bóng cần xét đúng phạm vi H6.
- Nguồn đã tra của bán thân ghi nửa người/tượng; chưa đủ chứng cứ để tự ghi K0 cho nghĩa tình dục. Tương tự, không lấy nội dung một ngôn ngữ khác trên cùng trang “chun/thun” làm nghĩa tiếng Việt.

**[verified]** `baotu` không có trong 7.776 khóa chính, cũng chưa có ở `blocked_keys.tsv`. K1 đã thống nhất ở T-dpv2-7 vẫn chặn cả bao tử/bào tử khi xét ứng viên. Đề nghị ghi đúng khóa ASCII này trong bảng chặn của gói D-dpv2-5 để kiểm P6 không đưa lại; **không có ghế chính riêng mang tên báo tử để thay**. Nguồn: `E\inventory.json:1`; `U\du-phong-v2-ke-hoach.md:420–432`; revision viwiktionary báo tử `2351672` trong `E\dictionary-family-roots.tsv`.

**[assumed thiết kế]** Với cách đọc đa nghĩa chưa chốt: đọc mẫu sạch, cố định seed, lưu số từng nghĩa + số không phân định và khoảng bất định; tăng mẫu hoặc đọc hết khi kết luận đổi theo phần chưa rõ. H7 không có tỷ lệ nghĩa đỏ mới do Astra đặt ra. Hai SA quyết định “tự nhiên, thông dụng”/K2 trên nguồn và ngữ cảnh; bất đồng còn lại đi H9/supervisor. Không báo PPM cả chuỗi như PPM nghĩa đỏ.

### 5.3. Danh sách chính xác đề nghị thay

**[verified tập dữ liệu; assumed đề xuất]** `A\de-xuat-thay-the-S4.tsv` có **141 dòng**, mỗi ghế ghi từ ra, khóa, lớp, lý do/case ID, ứng viên vào, ngăn, điểm P6 mới và điều kiện còn thiếu. Đây là bảng đề nghị chính; `de-xuat-thay-the.tsv` chỉ là đối chứng dùng hạng lịch sử/A, không phải phương án phát hành.

Danh sách dưới đây là **kịch bản có điều kiện**, gồm 140 H5/H7 và **do đó** do S4:

```text
áo quần; ăn diện; bà chủ; bàn ăn; bản đồ; bảo hành; báo động; bền bỉ
bình; bồ kết; bố mẹ; bộ ba; bộ đồ; ca nhạc; cao giá; cắm đầu
chiên; choàng; chỏm; chòng chành; chồn; chồng; chốt; chú ý
chuông; chữ nghĩa; cò trắng; có mặt; cổ thụ; cộng sự; cuốc; dàn ý
dặn dò; dây chun; dây thun; di dời; di động; diều; do đó; dò hỏi
đa năng; đánh bại; đậm đà; đầu mùa; đề cử; đích; đỏ thắm; đông đúc
đồng ý; đột phá; đuốc; gầy gò; giảm; gián; giảng; giao
giấc; giận dỗi; gọng; hâm mộ; hoa mai; hỏi thăm; hóm hỉnh; hố ga
húng; hững hờ; kể cả; khảm; khăn; khiến; kiến; kiểu
kính; làm mẫu; làng; lằng nhằng; lề đường; liên quan; lo lắng; lưới
măng; mê mẩn; mời mọc; nằm mơ; nắm vững; ngại; ngao; ngắt
ngoảnh; ngọc; ngụm; nguyên; ngựa; nhai; nhàu; nhâm nhi
nhồi; nhốt; phản bác; phân công; phấp phới; phí phạm; phong bì; phong thư
phòng; phòng ngủ; phù dâu; quà tặng; quên; rau dền; sàng; sân ga
sông; tài hoa; thảm; than; thắm thiết; thầy; theo; thể lực
thị trường; thiên tài; thong dong; thổi; thôn; thớt; thuần; thư thái
tiệm; tiền công; tiếp viên; tính khí; trạm; trăng tròn; treo; trình diễn
trời; tung; tường; vòng; xuân
```

**[verified]** 87 từ chính khác còn ca chờ, liệt kê đầy đủ ở `A\cac-tu-cho-phan-xu.tsv`. Chúng **không** được tính vào 140 lỗi đề nghị. Mô phỏng vẫn chứa chúng để đo cận dưới về thay thế; vì vậy **không thể dùng mô phỏng này làm bằng chứng H9 hay phát hành**. Sau hòa/đo, chạy lại toàn bộ lựa chọn và trình danh sách chính xác cuối cùng trước Final/phê duyệt.

### 5.4. Ghép ngăn, chọn ứng viên, S2–S4

**[verified số; assumed thiết kế]**

- 140 từ đề nghị qua H5/H7 gồm C63/H56/K19/F2: **138 ghế OK không-F và hai ghế OK-F**.
- A chỉ có 109 không-F, không thể cung cấp 138 ghế đó; 39 A-F không được tràn vào ghế không-F khi F đã dùng hết.
- Sau rà 329 ứng viên (199 dự phòng không-D + 130 HM OK), có 15 mục giữ ngoài hàng đề cử vì H5/H6/H7 cần khép. Dự phòng còn xét theo cận này: **117 không-F + 76 F**; thiếu ít nhất **21 không-F**.
- 107 HM R1 không tự được lấp ghế OK. Tầng A/C không thay luật S4: C không vướng cổng vẫn được xét theo hạng, không dùng quy tắc “A trước C”.

Nguồn: `E\candidate-summary.json:1`; `A\ung-vien-theo-ngan.tsv:1`. Tái rà đầu mục ứng viên tìm 27 cặp H5/127 cặp H7 trong HND (`E\ung-vien-doi-chung-H5.tsv`, `E\ung-vien-doi-chung-H7.tsv`). **[assumed]** Đây chưa phải kiểm hoàn chỉnh Wiktionary/bốn kho hoặc chữ ký H1–H9 mới.

**[verified phép tính có điều kiện]** `p6_preview.py` tái lập đúng toàn bộ 10.133 điểm/hạng nền, rồi:

1. Bỏ 140 mục đề nghị, sáu D dự phòng, 15 ứng viên giữ lại và những loại P7 không được mở lại.
2. Trong nhánh xin chủ duyệt, chỉ mở lại 130 HM **OK**, không R1; bỏ gián khỏi tập bắt buộc **chỉ trong mô phỏng có điều kiện**.
3. Tính lại bách phân vị S2 theo số khối, G/T và khoản đảo S3, làm tròn số nguyên phần trăm như mã đã ký, rồi S4; giữ những mục bắt buộc còn lại.
4. Rổ còn 9.970; lựa chọn đủ 7.776, F=77, R1=0. Phát sinh thêm **do đó** rời chính theo S4 dù điểm của nó tăng từ 66,53 lên 66,57: các mục khác xếp trên trong ngăn F.

Không đóng băng điểm cũ để tránh tác động này. Đây là thay đổi phụ thuộc P6 của D-dpv2-5, không một phán quyết H5/H7 mới về do đó.

**Kết quả điều kiện [verified]:** 141 mục vào = **117 HM + 24 dự phòng A**; C/H/K/F = **2.915/3.159/1.625/77**; 429/7.083/264 mục một/hai/ba khối; trung bình 6,818673 chữ. Khóa duy nhất, không mục ba chữ. Chưa có nghĩa mới/D8 mới và chưa khép 87 từ chờ.

| Ghế minh họa | Ứng viên theo P6 mới có điều kiện | Ngăn | Điểm |
|---|---|---|---:|
| áo quần (C) | ngân hàng (C, HM) | OK không-F | 109,94 |
| ăn diện (H) | khách hàng (C, HM) | OK không-F | 106,16 |
| bà chủ (C) | biển (C, HM) | OK không-F | 100,60 |
| bàn ăn (C) | côn trùng (C, HM) | OK không-F | 98,50 |
| do đó (F) | mình (F, HM) | OK-F | 78,33 |
| kể cả (F) | làm sao (F, HM) | OK-F | 71,39 |
| theo (F) | thường xuyên (F, HM) | OK-F | 67,76 |

Ghép ghế trong cùng ngăn là tất định theo O1 của từ ra và hạng ứng viên; không phải yêu cầu thay bằng từ đồng nghĩa hoặc bắt buộc C→C. F≤77 là trần, không là mục tiêu phải lấp. Các điểm trên đã tính lại; bảng đầy đủ lưu cả phân số F chính xác.

**[assumed thiết kế]** Điểm F chỉ dùng chọn từ, không trở thành trọng số sinh passphrase; ứng dụng vẫn bốc đều 7.776 vé.

24 dự phòng được lấy trong kịch bản: **bâng quơ, bụng dạ, buồn thiu, chính cống, cờ vây, cụt hứng, đưa đò, gợi chuyện, khó nghĩ, lạ tai, leo dây, mấp mé, mỏi nhừ, mon men, mụ mị, nhá nhem, nín thinh, oái oăm, phất phơ, rơm rớm, sáng trưng, số âm, tấn tới, xuống cân**.

**[assumed thiết kế]** Sau mỗi loại ở H9 hoặc D6/D7, chọn ứng viên kế tiếp **đúng ngăn** theo hạng đã khóa; nếu phải thay rổ H/S thì tính lại phiên bản P6 và hai SA đối chứng. Không lặp viết vô hạn, không lấy cùng khóa để né K0/K1. Nếu cửa 7.776 không còn đạt, dừng trình chủ, không “sửa cho đủ”.

### 5.5. Thiết kế lượt nghĩa sạch

1. **[verified yêu cầu; assumed tổ chức]** Chỉ mở sau Final/phê duyệt. Mỗi từ vào có câu viết sạch mới, kể cả 24 A đã có câu lịch sử; không dùng hash lịch sử thay chứng minh lượt mới.
2. Mỗi lượt là agent mới, không kế thừa hội thoại của SA/người soát. Lô ≤400 từ, theo O1; với 141 từ dự kiến một lô ban đầu. Chỉ đọc lô, hướng dẫn bỏ §12 và `kiem-tra-giai-nghia.py`; chỉ ghi bài nộp. Không repo, mạng, từ điển, nghĩa cũ, bảng P4, ghi chú SA hoặc bài lượt trước.
3. Điều phối phải chứng minh cách ly bằng cấu hình quyền/nhật ký, không chỉ lời hứa trong prompt. Nếu runtime không bảo đảm, chưa được ghi D1 đạt.
4. Người viết chạy tự kiểm D2/D5. Điều phối gộp và chạy `--phat-hanh` trên **toàn 7.776**, không chỉ trên lô mới.
5. D6 do người soát quyền chạy, đủ năm nguồn ghim, đúng family map mới; không gửi đoạn trùng cho người viết. Kiểm tập mới sau từng lượt và kiểm lại toàn bộ thành phẩm trước xuất.
6. Hai SA soát D7 độc lập: chia nửa và **ít nhất 15 từ chồng chéo** nếu lô có 141; tất cả cờ phải hai bên xem. Cố định mẫu bằng hash đầu mục trước khi chấm. Chỉ trả mã/chẩn đoán bằng lời riêng, không câu thay thế.
7. D7 đã ký quy định tối đa **hai lượt viết lại**: v1+v2+v3 (`AT\tieu-chi-thong-nhat.md:307`, `WordListAnalyze.md:257`). §12 hướng dẫn ghi rút gọn “hai lượt viết”; điều phối áp hợp đồng đã ký, không tự nới. HM đã hết lượt cần Q-rtc-A2, không tự xóa lịch sử để đếm lại.
8. D8 mới dùng ID rõ, thí dụ `rtc-v1/rtc-v2/rtc-v3`, lô, người soát, người/ngày đóng cờ, hash câu raw và kết quả D6. Hash câu trong D8 và hash token trong log D6 là **hai loại hash**, không nối bằng so sánh tên cột.
9. Mục không đạt nhường đúng ghế cho hàng dự phòng đã tái kiểm; không sửa câu bằng tay. Mục buộc giữ hoặc thay đổi phạm vi vượt phương án được duyệt quay lại SA/chủ.

**[verified]** Hướng dẫn cách ly ở `AT\huong-dan-giai-nghia.md:7–11,167–185`. Lượt này không viết câu nghĩa, không tạo lô có nghĩa, không lưu corpus/định nghĩa/dictionary list; tra cứu đều ở RAM.

### 5.6. Tệp và mục phải đổi khi triển khai

**[assumed thiết kế; chưa thực hiện]**

| Tệp | Thay đổi cụ thể |
|---|---|
| `U\ra-thay-chinh-phan-xu-H5.tsv`, `...-H7.tsv`, `...-chu-ky.tsv` | Một ID mỗi cặp; nhận định hai SA, nhóm nghĩa, số đếm/mẫu số, nguồn/revision/hash, quyết định, lý do, ngày; không lưu câu kho/lời từ điển |
| `U\ra-thay-chinh-xep-hang.tsv`, `...-thay-the.tsv`, `...-kiem-goi.json` | Rổ đã khép H9, F/G/T/điểm nguyên, S4; ghế ra/vào và ngăn; hash, Q, H4, D8 và kết quả kiểm |
| `AT\wordlist.txt` | Giữ 7.776, O1, UTF-8/NFC/LF; chỉ ghép nghĩa mới đã đạt; không chép câu của người soát |
| `index.html`, `thong-tin.html`, WLA §10 | Sinh bằng `build_wordlist.py`; không sửa ba bản bằng tay |
| `AT\labels.tsv` | Bỏ dòng của từ ra khỏi tập nhãn hiện hành; D8/ledger giữ lịch sử. Đổi dự phòng được dùng sang CHINH, thêm HM vào; nhãn/lớp/điểm theo P6 mới. Thêm `phien_ban_diem` để không trộn điểm mới với điểm lịch sử của các dòng không tham gia rổ |
| `AT\nguon-goc-giai-nghia.tsv` | Từ ra thành LOAI với cổng/đợt ra-thay-chinh, giữ nguồn gốc nghĩa cũ. Từ vào PHAT_HANH với lượt mới. Khi HM tái nhập, giữ một dòng hiện hành/đầu mục; lịch sử trước/sau và hash nằm trong ledger/Git, không tạo dòng trùng |
| `AT\spelling_families.tsv` | Đăng ký các họ được hai SA xác nhận, số sạch và kết luận đúng; không gán 0 cho số chưa đo; không đăng ký 632 đề xuất thô |
| `AT\blocked_keys.tsv` | Thêm khóa ASCII K0/K1 chốt và `baotu`; không đưa từ tục có dấu vào bảng công bố. K2 chưa đủ chữ ký không được có mặt trong chính |
| `AT\d6-ho-chinh-ta.tsv`, `d6-tham-chieu.json` | Bổ sung quan hệ **cùng từ đã xác nhận** nếu D6 chưa có; cập nhật đúng hash/count/đường dẫn nguồn của lượt mới, không bỏ pin/giảm ngưỡng |
| `AT\du-phong.txt`, `du-phong-phan-loai.tsv` | Xóa đúng mục thực sự được dùng khỏi dự phòng hiện hành; giữ cảnh báo/tầng của phần còn lại, cập nhật nhận định liên quan. Không đưa từ chính bị chặn vào dự phòng |
| `AT\honorable-mentions.tsv` | Bỏ mục được thăng lên chính; cập nhật cổng/lý do/việc thiếu có bằng chứng mới trong đợt. Không lấp thêm để giữ số 237 |
| `AT\manifest.json` | Hash nguồn, cột từ, các tệp đổi; số thực của chính/dự phòng/HM, lớp/tầng/trạng thái nghĩa; metadata lượt D6 mới. Thêm hồ sơ đợt với base và commit quyết định; giữ nguyên metadata lịch sử v2 |
| `WordListAnalyze.md` header, §3, §10–12 | Header nêu đợt/commit, thống kê và SHA thực. §3 thêm quyết định mới sau khi chủ trả lời, không sửa lại quyết định cũ. §10 sinh; §11/12 phản ánh tập hiện hành, số gốc và nguồn lịch sử, có bảng lý do các loại/giữ |
| `AT\README.md`, README gốc | Cách tái lập đợt, phiên bản điểm, nghĩa mới/D8, số dư thực và lệnh kiểm. Hai TSV đề cử ghi rõ F/điểm lịch sử; điểm chọn hiện hành lấy từ P6 mới/labels có phiên bản |
| `thong-tin.html` “Quy tắc chọn từ” | Chỉ sửa nội dung luật nếu chủ thật sự đổi luật/ngoại lệ; không ngầm nới H6/H7 để phù hợp kết quả |

**[verified điều kiện]** Nếu kịch bản 141 thành công nguyên trạng, dự phòng còn `205−24=181`, HM còn `237−117=120` trước các loại thêm do cổng mới. Không đóng cứng hai số này vào task; sinh từ tập cuối. Hồ sơ v2 gốc vẫn giữ 205/237 để đối chiếu lịch sử.

**[assumed thiết kế]** Đề nghị cấu hình EOL riêng cho nguồn chuẩn LF và hai HTML CRLF bằng `.gitattributes` có phạm vi hẹp; không chuẩn hóa hàng loạt corpus/hồ sơ hay nới checker. Kiểm build cần đúng CRLF ở HTML; tài liệu chấp nhận LF/CRLF. Nếu chọn môi trường xuất thay vì attributes, vẫn phải có kết quả native thật trên đúng byte sẽ phát hành.

### 5.7. Đóng gói và kiểm tương thích

**[assumed thiết kế]** Chỉ đổi bundle sau khi rổ/ghế/nghĩa đã khép; kiểm giao chính–dự phòng–HM bằng khóa sau từng lần chọn. Không commit một bước thêm LOAI vào bảng họ nhưng còn từ đó trong chính.

Các gate trên dữ liệu cuối, không trên bản giả lập:

```text
python -B analyzing-tools\check_wordlist.py
node analyzing-tools\verify.mjs
python -B analyzing-tools\build_wordlist.py --check
python -B analyzing-tools\build_wordlist.py --lo analyzing-tools\ho-so\unified\ra-thay-chinh-kiem-nghia
python -B analyzing-tools\kiem-tra-giai-nghia.py --phat-hanh analyzing-tools\ho-so\unified\ra-thay-chinh-kiem-nghia\lo-01.txt analyzing-tools\ho-so\unified\ra-thay-chinh-kiem-nghia\lo-01.tsv
python -B analyzing-tools\d6-kiem.py --input <gop-7776.tsv> --log <d6-rtc-final.tsv> --meta <d6-rtc-final.json>
```

Giữ bộ kiểm hiện có, không gọi phạm vi JS rộng hơn thực tế. Bổ sung kiểm gói độc lập theo ledger: chữ ký, H3/H6/H8/H9, người thắng mỗi họ, R1→OK, D8 một-một và không còn khóa/đầu mục bị chặn. C9 báo lại nhập nhằng hai từ; C10 thử trình duyệt số dòng, viết hoa/chèn số với cụm nhiều khối; C12 hash, C13 đủ 7.776 theo ngăn (không yêu cầu 300).

## 6. Tiêu chí chấp nhận

Mọi dòng dưới đây là **[assumed hợp đồng đề xuất]**, không là kết quả đã đạt của bản phát hành mới.

| ID | Tiêu chí | Cách kiểm |
|---|---|---|
| B1 | Đúng D-dpv2-5, không tự mở OI khác | Ma trận phạm vi + danh sách thay chủ duyệt |
| B2 | Không thay trước Final/phê duyệt; quyết định gián và quyền HM rõ | Commit câu trả lời, Decisions, hai sign-off |
| B3 | Đúng 7.776; không ba chữ, trùng khóa hoặc né khóa đỏ | C1–C4 + đối chiếu ledger |
| B4 | Không còn ca H5/H7/H9 chưa phân xử có thể ảnh hưởng bản cuối | Hai phiếu từng cặp; các giữ lại K2 đủ hai chữ ký |
| B5 | Mỗi từ mới có nghĩa sạch, không phải câu do SA sửa tay | Hồ sơ D1, bài nộp, D6/D7/D8 |
| T1 | 632/632 và 1.177/1.177 có kết quả cuối; số đầu vào không bị xóa để giảm ca | ID/hash/tập cặp khớp; giải thích mọi thay số |
| T2 | K0 và các còi dưới ngưỡng được xét; CHUA_DO không thành 0 | Các bảng bổ sung, bao gồm 45 dạng HND và nguồn Wiktionary cần khôi phục |
| T3 | 95/20, 10/5, bộ lọc/ngữ cảnh và mẫu số đúng | Số nguyên, thử biên và độ nhạy phụ đề; log đọc nghĩa không chứa corpus |
| T4 | P6 hai chương trình khớp từng từ/hạng/ngăn; F≤77, R1≤388 và đúng quy tắc thay | Tính độc lập từ rổ đã khép, không đọc điểm bên kia |
| T5 | D2/D5 toàn danh sách đạt; D6 không CHUA_KIEM, đúng hash; D7 không CHAN | Log final + mẫu chéo/cờ đóng; không lấy self-test làm kiểm nghĩa |
| T6 | D8 tương ứng một-một với nguồn chuẩn; lịch sử loại/tái nhập còn truy được | SHA raw câu, ID lượt, hash token D6, ledger và Git |
| T7 | Hai checker, build --check, kiểm gói và trình duyệt đạt trên byte thật | Lưu lệnh/exit/log; không che lỗi CRLF bằng tuyên bố PASS |
| T8 | §10 khớp từng dòng; §11/12, TSV, nhãn, manifest khớp tập thực | Set diff, hash LF, số trạng thái/tầng, lý do không mất |
| T9 | Dữ liệu nguồn không bị đưa vào repo; không chép lời nguồn | Kiểm danh mục artefact và diff trước commit |
| T10 | Mọi số mô phỏng được cập nhật sau hòa/đo/viết lại | Chạy lại, công bố chênh với 141; không dùng cận dưới làm Final |

## 7. Rủi ro và giảm thiểu

- **[verified/assumed] Cận dưới chưa khép:** 87 từ chính còn ca chờ. Không được triển khai bảng 141 rồi tuyên bố rà xong. Hòa/đo trước khi khóa danh sách cuối.
- **[verified/assumed] Thiếu sức chứa nếu không mở HM:** thiếu 21 không-F ngay ở cận dưới, chưa tính thất bại nghĩa mới. Trình Q-rtc-A2; không lấp bằng F/R1 sai ngăn.
- **[verified/assumed] Chữ số không thay ngữ nghĩa:** PPM toàn từ, tên riêng bị hạ chữ, đa ngôn ngữ của Wiktionary và biến thể sinh tự động đều có thể gây kết luận sai. Giữ loại xác minh, URL/revision/hash và phản biện từng ca.
- **[verified/assumed] Bảng chặn chưa có không chứng minh từ an toàn:** kiểm nền canonical vẫn PASS dù sàng lọc tìm các ca mới. Cần bảng phân xử/chữ ký, không “chạy test xanh” thay quyết định.
- **[verified/assumed] S2/S4 có tác động phụ:** do đó đổi chỗ ở mô phỏng; mọi lần đổi rổ phải tính lại và trình thay đổi. Không đóng băng điểm cũ tùy tiện.
- **[verified/assumed] D6 không sẵn để chạy thật:** phải khôi phục snapshot, xử lý hash từng nguồn; không tìm/ghi tài liệu thô ra vị trí ngoài quyền. Ưu tiên nguồn được điều phối cung cấp hoặc luồng RAM; giữ log chỉ metadata.
- **[assumed] Lây ngữ cảnh vào người viết:** người viết là lượt mới, quyền tối thiểu, không đọc report này. Chẩn đoán viết lại không chứa câu nguồn/câu cũ.
- **[verified/assumed] Đổi bảng không nguyên tử:** đăng ký họ chòng chành làm C5 trượt nếu chưa thay chính. Ghép gói có gate cuối, không phát hành trạng thái nửa chừng.
- **[assumed] Phạm vi:** không suy rà H5/H7 là đã tái thẩm định mọi nghĩa H6 của cả 7.776. Các phát hiện ngoài phạm vi cần ghi riêng và xin phạm vi nếu cần, không tự sửa.

## 8. Công sức và phân kỳ

**Ước lượng [assumed], không phải trần được chủ duyệt; “lượt” có thể là tin tiếp theo cho SA hiện hữu, không nhất thiết agent mới.**

| Pha | Đầu ra/điểm dừng | Lượt agent ước tính |
|---|---|---:|
| A. Phân tích độc lập, rà chéo | Hợp nhất phiếu, phát hiện khác nhau; giữ nguyên hai lập trường | 2 phân tích + 2 rà chéo |
| B. Bổ sung nguồn/đo và hòa ca | Đóng 44 cặp H5 gốc còn chờ và hai hướng họ bổ sung; các H7 chờ và K2 liên quan; có nguồn D6 đúng; chốt sức chứa | 2–6 lượt SA, script đếm theo lô |
| C. Quyết định và kế hoạch | Q-rtc-A1/A2, joint report, plan Final, chủ duyệt danh sách/quy tắc fallback | 2–4 lượt soạn/duyệt |
| D. Triển khai và P7 | Một lô đầu ≤400; các lượt sạch mới chỉ cho mục lỗi | 1–3 lượt viết + 2–6 lượt soát D7; thêm 1–3 lượt viết nếu cần lô thay |
| E. Đóng gói/kiểm | P6 độc lập, D6 toàn tập, D8, build, tài liệu, C1–C13 | 1 lượt dev + 2 lượt SA kiểm |

Ước tính riêng từ sau Final: khoảng **6–12 lượt** cho nhánh không cần thêm lô thay; số thực tăng nếu nguồn/ca nghĩa hoặc D6/D7 buộc thay tiếp. Chưa có cơ sở quy đổi chính xác ra giờ hay AI credits.

Không chạy chồng đo kho nặng với repo khác; dùng lock helper nếu môi trường có và điều phối tuần tự. Không viết nghĩa trong pha A–C. Không lập task pack thực thi khi các quyết định/phân xử quan trọng còn mở.

## 9. Câu hỏi

### Q-rtc-A1 — owner: gián và quyết định giữ trước đây

**Cần quyết định:** có cho phép thay **gián** do cách đọc không dấu **gian** dù quyết định 5 đã giữ gián không?

- **[verified] Bối cảnh:** quyết định giữ là `WordListAnalyze.md:150`; đề xuất mới là H7, không phải phản đối lại con vật/việc vệ sinh vì ghê tởm.
- **[verified số; assumed phán quyết] Bằng chứng:** `A\h7-sang-loc-1177.tsv:414`, PPM cả chuỗi gian 10,806597177; nguồn vi revision `2415939`, en revision `93493903`, ghi trong `E\dictionary-h7critical.tsv`, `dictionary-edge-final.tsv`.
- **Phương án:** (1) cho thay gián và chặn khóa theo kết luận H7 chung; (2) giữ gián bằng ngoại lệ cụ thể do chủ quyết, phải ghi phạm vi ngoại lệ và kiểm máy tương ứng; (3) yêu cầu đo/hòa thêm trước quyết định.
- **Đề nghị Astra [assumed]:** (1), nếu Opus đồng ý mức K1; không tự áp dụng câu trả lời “cho thay chính” chung để xóa quyết định giữ riêng.
- **Bị chặn:** tập bắt buộc P6 và danh sách cuối. Mô phỏng hiện tại dùng (1) có điều kiện.

**Answer (owner, ngày):**

### Q-rtc-A2 — owner: quyền mở chu kỳ nghĩa mới cho HM OK

**Cần quyết định:** có cho phép một chu kỳ viết sạch mới, tối đa hai lượt viết lại, cho các HM OK cần được chọn để thay chính dù hồ sơ nghĩa cũ đã bị loại không?

- **[verified] Bối cảnh:** riêng A thiếu 29 không-F; sau xét dự phòng không bị giữ lại còn thiếu 21. Kịch bản đủ dùng 117 HM và 24 dự phòng, không R1.
- **[verified] Bằng chứng:** `E\candidate-summary.json:1`, `E\p6-preview-summary.json:1`, `AT\honorable-mentions.tsv:1`; giới hạn D7 tại `AT\tieu-chi-thong-nhat.md:307`. Phải kiểm lịch sử từng mục, không gán tự động “đã hết hai lần viết lại” cho mặt khác chỉ vì nó thuộc cùng lô loại.
- **Phương án:** (1) cho một chu kỳ mới có điều kiện cho HM OK thực sự được S4 chọn, ghi rõ quyết định/đợt trong D8; (2) không mở lại, cho tìm OK mới theo H1–H9 và đo bốn kho để bù thiếu; (3) chỉ hoàn tất phân tích, chưa thay/phát hành.
- **Đề nghị Astra [assumed]:** (1); dùng hồ sơ từ đã đo/chấm nhưng **không dùng lại câu bị loại**, không reset số lượt vô hạn. Nếu vẫn thiếu sau cổng/viết lại thì dừng trình chủ.
- **Bị chặn:** nguồn thay và ngân sách P7; không được coi chữ HM là quyền mở lượt sạch. Không có chu kỳ mới nào đã chạy.

**Answer (owner, ngày):**

**[verified trạng thái]** Chưa đặt câu hỏi SA-Fable trong lượt độc lập: trước hết gửi phiếu cho Opus, hòa đúng một lượt và đo những chỗ thiếu. Bất đồng còn lại về áp luật sẽ được nêu với hai lập trường, không lấy trung bình.

## 10. Chỉ mục bằng chứng và tái lập

### 10.1. Tệp kết quả

| Tệp trong `A` | Vai trò |
|---|---|
| `h5-sang-loc-632.tsv` | 632 cặp, số/nguồn, nhóm, lý do, hành động |
| `h5-sang-loc-bo-sung.tsv` | Hai hướng xà bông/xà phòng, chờ xác nhận/đo H5f; không sửa tập gốc |
| `h7-sang-loc-1177.tsv` | 1.177 cặp gốc, PPM, còi, mức K đề nghị |
| `h7-sang-loc-bo-sung.tsv` | 1.942 dòng bổ sung; phân biệt cũ/không đếm/khác khoảng cách |
| `cac-tu-cho-phan-xu.tsv` | 87 từ chính chưa thể khóa kết luận |
| `ung-vien-theo-ngan.tsv` | 329 ứng viên dự phòng/HM OK, điểm lịch sử, ngăn, cờ giữ |
| `de-xuat-thay-the.tsv` | Đối chứng dùng A/hạng lịch sử, chỉ ra thiếu ngăn; **không phải** đề xuất cuối theo P6 mới |
| `de-xuat-thay-the-S4.tsv` | **Bảng đề xuất chính có điều kiện:** 141 ghế, điểm S2/S3 mới, ngăn và quyền còn thiếu |
| `mo-phong-P6-tinh-lai.tsv` | 282 dòng ra/vào của kịch bản P6 có điều kiện |

### 10.2. Script và log

- `E\screen_core.py`, `inventory.json`, `inputs.json`, `protected-baseline.json`: base, hash 24 tệp bảo vệ, số gốc và H7 tính lại.
- `E\hnd_probe.py`, `hnd-metrics.json`, `h5-hnd-membership.tsv`: nguồn ghim trong RAM, 19 dạng chỉ viết hoa, tái lập đúng tập H5; hai bảng đối chứng ứng viên.
- `E\dictionary_probe.py`, `dictionary-*.tsv`: tra có giới hạn, chỉ lưu đầu mục/URL/revision/hash/trạng thái; phân biệt phần tiếng Việt, không lưu lời giải. URL `oldid` cho phép kiểm lại đúng bản; “MISSING” chỉ ghi trạng thái lần tra, không chứng minh từ không tồn tại.
- `E\screen_votes.py`, `annotate.py`, `screen-summary.json`: phiếu độc lập và phép ghép số. Các nhận định được ghi **assumed**, không giấu dưới nhãn “đã kiểm số”.
- `E\candidates.py`, `candidate-summary.json`: sức chứa/ngăn, các giữ lại và nhánh xin quyền HM.
- `E\p6_preview.py`, `p6-preview-summary.json`: tái lập nền 10.133 hạng, mô phỏng có điều kiện sau tính lại; không chạy hàm ghi tệp của công cụ P6 lịch sử.
- `E\validate.py`, `validation.json`, `validation.log`: cận H5, toàn khóa, phép chiếu 7.776, kiểm nền/canonical, 20 self-test D6, định dạng và byte bảo vệ.

**Lệnh đã chạy [verified], từ root repo:**

```text
python -X utf8 -B analyzing-tools\ho-so\astra\ra-thay-chinh\evidence\screen_core.py
python -X utf8 -B analyzing-tools\ho-so\astra\ra-thay-chinh\evidence\hnd_probe.py
python -X utf8 -B analyzing-tools\ho-so\astra\ra-thay-chinh\evidence\annotate.py
python -X utf8 -B analyzing-tools\ho-so\astra\ra-thay-chinh\evidence\candidates.py
python -X utf8 -B analyzing-tools\ho-so\astra\ra-thay-chinh\evidence\p6_preview.py
python -X utf8 -B analyzing-tools\ho-so\astra\ra-thay-chinh\evidence\validate.py
```

Tra từ điển dùng `dictionary_probe.py --lang vi|en --tag <tên> --words <các đầu mục nối bằng dấu |>`; danh sách đầu mục, ngôn ngữ, revision và SHA của từng lần nằm trong TSV tương ứng, không phụ thuộc trí nhớ hay một bản dịch của mô hình.

**[verified]** Không commit/push/chuyển nhánh; không sửa tệp của Opus hoặc tệp sản phẩm; không có corpus, wordlist HND hay lời từ điển/giải nghĩa cũ mới được lưu vào repo. Chỉ ghi hồ sơ trong `A`.
