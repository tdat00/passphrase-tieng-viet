# T9 — SA-Astra, 22/11/2026, rà working tree bản 2

Phạm vi: 7.776 khóa thực, gồm 116 từ vào sau T-rtc-23. So mọi vai trò đếm, DOC_KHAC, bốn nguồn HND và hai bản Kaikki ghim; không lưu nguồn thô.

**Chưa chấp nhận phát hành.** Mốc trước sửa `d78e97a`; băm LF của danh sách đang rà `8c21d035e1275560cb1253489e9bcf75a18a17f2b0e6d237873e6e98aa367ef4`. D6 đạt không chứng minh T9 đạt.

- `wordlist.txt:5333` (*phết*): cách đọc *phẹt* được Kaikki VI:37654 ghi nghĩa bài tiết với nhãn thô tục của chính đầu mục (VDict cũng ghi nhận). Phụ đề/web sạch 0/0 không miễn K0. Phiếu cũ chỉ ký cách đọc *phét/phệt* (`chu-ky.tsv:1872–1873`), không xử nghĩa này. Astra phản đối K0 cho khóa `phet`, không tự hủy T-rtc-2. Nếu còn tranh cãi phải đưa owner theo TC:164.
- `wordlist.txt:915,7144,7203`: *cau có/cầu cơ*, *tụ tập/tu tập*, *tử tế/tư tế* có cách đọc nghi lễ, thực hành hoặc chức sắc tôn giáo. Số sạch lần lượt 47/1, 0/171, 110/34; PPM 0,6882 / 0,5705 / 1,7163; không phải suy từ một âm tiết. Chưa có phán quyết chung đúng đối chứng.
- `wordlist.txt:2248` (*đon đả*): *đòn đá* (Kaikki VI:281788) là đối chứng H6.1 của **từ vào**. Số 1/1 khác 0, PPM 0,0179 ≥ 0,0146 của mục và phải xét bạo lực ngay cả dưới còi. Không phải cặp có thể bỏ qua hoặc đã ký. *Cả nghĩ* (dòng 760) được kiểm như mọi từ vào: không có đối chứng khác trong ba nguồn.
- `chu-ky.tsv:2152–2154`: *thầy* hiện có **3** dòng K2 `CO` (Astra 1, Opus 2), không đúng T4 “hai dòng ký hiệu lực”. Hợp nhất/đánh dấu thay thế dòng Opus lặp, giữ một dòng/người; kiểm cả khóa lịch sử chứ không chỉ 243 khóa mới. Việc này không lật quyết định giữ *thầy*.

## Độ phủ và những ca cần đối đáp

| Phép đối | Kết quả |
|---|---:|
| Khóa phát hành / không có cách đọc khác / có ít nhất một | 7.776 / 5.780 / 1.996 |
| Cặp khóa–mặt chữ khác phân biệt sau khi hợp nguồn | 3.856, gồm 143 dòng chỉ khác viết hoa |
| DOC_KHAC / Việt 11K / 22K / 39K / 74K / Kaikki VI / EN | 2.794 / 773 / 1.548 / 2.220 / 3.263 / 2.122 / 1.757 cặp; không cộng các cột có giao nhau |
| Từ vào / có đối chứng khác / số cặp | 116 / 26 / 35 |
| Khóa trong bảng H7 hợp nhất còn ở chính có đối chứng / số cặp | 257 / 842 |
| Cặp ban đầu thiếu số / còn thiếu sau khi đo hai kho | 556 / **0** |
| Cặp đạt ít nhất một mốc **số** / cặp ở bảng còi cũ đang áp dụng đã ghép | 1.530 / 53 trên 53; đạt mốc số không có nghĩa là đỏ |

Đã đối cả bốn bộ HND ở commit `688b095` và hai bộ Kaikki ghim, duyệt mọi mục tiếng Việt trùng **toàn** khóa, kể cả khác dấu cách/gạch nối, viết hoa, thiếu vai trò DOC_KHAC. Không dùng PPM cả mặt chữ làm PPM nghĩa đỏ; không đồng nhất mọi tên riêng (thần linh, tước hiệu khác với địa danh). Năm mục không có chính dạng cách trong hợp nguồn có dạng gạch nối tương ứng và đã được kiểm; không phải năm từ bị bỏ sót.

`t9-soat-toan-tap.tsv` ghi tên và lý do từng ca cần chú ý. Phiếu hash cho **mọi** cặp ở `evidence\t9-phan-xu-tung-cap.tsv`. Kết quả Astra: **3.793 cặp không còn phản đối riêng của Astra; 63 cặp thuộc 59 khóa phải đối đáp**. Trong 63 có 1 phản đối K0, 3 phản đối K1, 2 ca chưa đủ phân định K0 và 57 phiếu K2 của **riêng Astra**. Không được hiểu là yêu cầu thay 59 từ hoặc rằng các K2 này tự có hai chữ ký; đối chiếu phiếu Opus đúng đối chứng, nếu giữ thì ghi lý do và trạng thái hiệu lực.

- Hai ca K0 chưa khép: `wordlist.txt:1607` *cuống/cương* (EN:15144; phụ đề ID `3570902` và hai câu kề xác nhận nghĩa sinh lý dùng độc lập, không phải chỉ trong cụm dài; chữ ký cũ chỉ nêu *cuồng/cưỡng*); `:3895` *lông/lồng* (EN:25441, mục riêng cho cách viết lóng của một từ tục). Cần phân định độ phổ biến của nghĩa phụ. Không dùng 300/2.310 hay 659/6.634 lượt cả mặt chữ làm tỷ lệ nghĩa. Đây chưa phải quyết định K0.
- Bốn ca H7 của từ vào cần Opus đối đáp đúng phạm vi: *chấp nhặt/chấp nhất* (`:1137`, còi tương đối), *đon đả/đòn đá* (`:2248`), *hóng chuyện/hồng chuyên* (`:3120`, thuật ngữ chính trị hiếm), *nặng cân/nặng căn* (`:4426`, phán quyết cũ về H5 *lặng câm* không xét cách đọc này). Các ca khác được liệt kê riêng trong phiếu; ví dụ *bộ đồ/bò đỏ* không nằm trong chữ ký cũ cho *bợ đỡ*. Đối với *bảng/băng*, khi hợp nhất phải giữ phạm vi của hai dòng cũ đã chuyển `THAY_THE`.
- Đọc thêm tín hiệu K0 trên **chính mặt chữ**, không mở cuộc rà H6 đại trà. `evidence\t9-mat-chinh.tsv` phân biệt ba nghĩa phụ cần phản biện (*rùng mình, tâm hồn, vắt sữa*) với cách hiểu chỉ xuất hiện trong lời dịch, với ba chữ ký cũ (*bịch, ngoài, trứng*) và quyết định giữ *chào cờ*. Nghĩa lóng của *chào cờ* đã được nêu đích danh trước đây: **không** chất vấn lại chủ vì cùng chứng cứ. Chỉ dẫn tới bộ phận cơ thể, chữ `dung` trong *nội dung* hoặc từ chuyên ngành trong ví dụ không phải nghĩa K0.

## H5 của từ vào và gói dữ liệu

- **Hai phản đối H5c độc lập với H7:** `wordlist.txt:702` *buồn thiu/buồn thỉu* (Kaikki VI:272859); `:3244` *ỉu xìu/ỉu xịu* (VI:111007; Việt–Việt 30K:8288). Đây là dẫn chiếu **nguyên mục** sang dạng còn lại, không chỉ có tên trong wordlist HND. Phụ đề hai cặp lần lượt **9/0, 6/0** (bỏ trùng **7/0, 5/0**), web **0/0, 1/0**. Không đủ 20 lượt cho c; không phải chỉ đổi cách đặt dấu trên cùng âm tiết hoặc một cặp hỏi↔ngã. Chưa đăng ký trong `spelling_families.tsv`. Hai SA phải xử và nếu giữ kết luận c thì rút từ vào, lấp lại đúng thứ tự.
- Không kết luận hai từ là cùng họ chỉ vì gần nghĩa: *dài ngoằng/dài ngoẵng* (`:1670`, 7/0 phụ đề, 0/0 web) và *lu bù/lu bu/lù bù* (`:3938`, từng dạng lần lượt 10/5/0 phụ đề và 0/1/1 web) có giao nghĩa nhưng nguồn còn phân biệt nét biểu cảm, từ loại hoặc phạm vi dùng. Cần xác nhận quan hệ trước khi áp tỷ lệ; không coi cả bốn trường hợp là K0 hay tự chặn khóa ASCII. Với *chấp nhặt/chấp nhất*, có nét nghĩa riêng; hồ sơ H7 không tự thành họ H5.
- T2: 94 khóa và mã khớp từng dòng với phiếu đã khóa; không có từ chính trong các khóa đang chặn. T3: 35 họ đã chốt/312 tổng khớp loại và kết luận; kiểm được bảng đã đăng ký không chứng minh đã bắt đủ hai họ mới ở trên. T4: 7.776 `CHINH`, toàn bộ OK, F=77, R1=0; toàn bộ gói 238 chính/từ vào + 5 HM có đủ hai người. **Ngoại lệ toàn danh sách:** *thầy*. `ra-thay-chinh-kiem-chu-ky.py:64–82` dùng tập tên người cho khóa cũ, chỉ ép đúng hai dòng đối với gói `rtc`; cần ép đúng một dòng/người cho mọi K2 chính.
- T6/T8/T11/T12: khớp từng mục D8, băm câu gốc D8 và băm dãy token JSON của D6; bản 2 có 7.776 dòng D6 PASS, run `555017cb…`. So với `d78e97a`: đúng 116 ra, 115 vào theo hàng đợi + *cả nghĩ*, 7.660 câu giữ nguyên; 84/27/5 câu từ v1/v2/v3. Còn 89 dự phòng, 237 HM; 24 HM có câu đạt chưa dùng, *khách hàng* không có trong tập đạt; dự bị *cửu chương* chưa vào. `manifest.json` khớp các băm LF đã khai, cột từ và nguồn D6.
- Sửa `WordListAnalyze.md:9101`: K0 bao gồm nghĩa **tục, tình dục người lớn hoặc chỉ chất thải**, không đòi có nhãn tục cho cả ba loại. Dòng `:9124`: 238 mục thuộc gói ký, nhưng chỉ **237 nhãn K2 mới** so với HEAD (*bảng* đã có K2). Các số, tập 116 từ, danh sách có *cả nghĩ* và không có *sớm tối* ở §13.4 khớp.

## Tái kiểm và xử lý

Trong `analyzing-tools\ho-so\astra\ra-thay-chinh\evidence\`, chạy từng script bằng `python -B`: `t9-nguon-astra.py --fresh`, `t9-dem-astra.py sub` và `web`, `t9-phan-xu-astra.py`, `t9-goi-astra.py`. Hai lệnh cuối trả `1` trên bản đang rà: còn cặp chờ, và T4 sai số dòng hiệu lực. `t9-nguon.json` ghi sáu pin và hash danh sách; `t9-phu-khoa.tsv` đủ 7.776 khóa. Dữ liệu thô chỉ đọc trong RAM; bảng chỉ chứa chỉ mục/băm, số đếm và ý kiến. `t9-kiem-nghia.py` đối lại nghĩa ở các dòng nguồn cụ thể; `t9-mau-nghia.py sub|web --inspect` lấy tối đa 30 vị trí/dạng/kho với seed `rtc-T9-20261122`, chỉ lưu mã dòng và băm. Mẫu định hướng không đại diện cho tần suất nghĩa. Ví dụ đúng nghĩa *đòn đá*: phụ đề ID `4015748`, web ID `2493937`.

Không commit gói này. Hai SA đối đáp theo H9, xác định lại tập cần thay/bù theo §6.1; nếu đổi danh sách/số lượng chủ đã duyệt thì trình lại, không tự mở vượt 25 HM. Sau sửa phải tái sinh khối, cập nhật D8, băm và tài liệu (kể cả `manifest.ho_so.so_tep` khi thêm hồ sơ T9), chạy lại T2–T13 trên đúng byte sẽ phát hành. **Astra không duyệt thay cho owner.**
