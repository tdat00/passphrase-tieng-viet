# Review chéo vòng 1 — SA-Astra đọc SA-Opus

**Ngày:** 20/11/2026. **Base dữ liệu/mã:** `cefb99386d4845e40bc2d3eabc7d6898d078305d`.
**Kết luận:** đồng ý kiến trúc tài liệu, chưa chấp nhận nguyên trạng mọi kết luận/tệp của Opus. Các chỉnh sửa dưới đây cũng thay thế những nhận định tương ứng trong phân tích vòng 1 của Astra; giữ nguyên hai bộ đầu ra độc lập để đối chiếu.

Quy ước: **verified** = đã đo/đọc kiểm nguồn; **assumed** = nhận định ngôn ngữ hoặc đề nghị của Astra, chưa là quyết định chung. Xác nhận có đầu mục trong wordlist không tự chứng minh quan hệ “cùng từ”. Không viết giải nghĩa mới.

Đường dẫn ngắn: `AT = analyzing-tools`; `U = AT\ho-so\unified`; `O = AT\ho-so\opus\du-phong-v2`; `A = AT\ho-so\astra\du-phong-v2`; `E = A\evidence`. Mọi dẫn dòng của dữ liệu/mã cũ thuộc base trên; tệp mới có hash đầu vào tại `E\cross-review-inputs.json`.

## 1. Điểm đồng ý

1. **verified/assumed:** giữ nguyên danh sách chính và §10; giữ `du-phong.txt` 205 dòng để bảo toàn đầu vào lịch sử; đặt phân loại và đề cử ở TSV riêng, sửa §11/thêm §12, README/manifest. Chưa cần sửa `labels.tsv`, D8, khóa chặn hoặc họ chính tả dùng cho phát hành.
2. **verified:** pool 10.156 của P6 khác bảng xếp hạng 10.133 sau P7 v1/v2 và rổ P0 10.001. Dự phòng có 128 OK không-F + 77 OK-F; 168 câu đã đạt lịch sử và 37 mục chưa viết đều F. Không có D8 cho các mục dự phòng.
3. **verified:** Opus tính H8 bằng **số sạch** là đúng hướng. Kết quả phải là 198 mạnh, 6 yếu, 1 không-lượt; Astra sửa hai nhãn số học trước đây ở §4.
4. **verified:** các số so sánh F của Opus được tái lập: 66/128 dưới P1 và 112/128 dưới P5 của F danh sách chính không-F. Với quantile `exclusive`, P1 = 4,540514, P5 = 9,043560; `inclusive` đổi nhẹ ngưỡng nhưng không đổi hai số đếm. Trung vị chính = 42,186087, dự phòng = 4,4583265; dự phòng cao nhất ở khoảng 9,027% của phân bố chính. **assumed:** diễn giải “rất kém quen” vẫn là suy luận, không phải kết quả khảo sát người dùng. F tính trong nhóm số khối, không phải xác suất biết từ hay xác suất bốc.
5. **verified:** 60 DC2 đúng điều kiện phiếu gốc một OK/một R1, không-F, F ≥ 50; không được tự biến chúng thành OK. Nguồn kiểm là hai phiếu P4 và `U\xep-hang.tsv`, không chỉ bảng đề cử của Opus.
6. **verified/assumed:** còi `bao tử`/`báo tử` có thật và cần xử lý; không thể xem không nằm trong `blocked_keys.tsv` là đã hoàn tất H7.
7. **verified:** lỗi CRLF có sẵn ở checkout; phải giữ cả log native không đạt lẫn log đối chứng đúng blob LF. Không gọi đó là native PASS hoặc sửa tệp bảo vệ để có log xanh.

## 2. Bất đồng và phán đoán sau review

### 2.1. Đối chiếu đầy đủ từng từ

**verified:** `E\cross-review-reserve-diff.tsv` có đủ 205 dòng: **177 khớp, 28 lệch**. Ma trận Astra→Opus: A→A 141; A→C 11; C→A 10; B→B 36; A→D 6; B→C 1. Mỗi dòng có lý do của cả hai, H8 số sạch, nguồn và phán đoán sau review.

**assumed — phán đoán mới của Astra cho toàn bộ 28 chỗ lệch:**

| Từ | Astra cũ | Opus | Astra sau review | Lý do |
|---|---|---|---|---|
| ăn nhịp | A | C | C | Cảnh báo dữ liệu 0; ngoại lệ H8 hai chữ ký vẫn hợp lệ |
| ăn trầu | C | A | A | Bỏ ưu tiên thấp thiếu căn cứ H6 mới; không khẳng định không gây nghiện |
| bèo bọt | C | A | A | Chưa có phản đối H6 mới đủ chứng cứ |
| cả nghĩ | A | C | C | H8 phải dùng 2/0/0/0 sạch, không dùng 8/4 bề mặt |
| chán phèo | A | D | D | Đồng ý họ chán phè/chán phèo; xem §2.2 |
| chấp nhặt | C | A | A | Sắc thái chê nhẹ chưa đủ tự lật kết luận cũ |
| chễm chệ | A | C | C | Cảnh báo ít chứng liệu; Leipzig 2 vẫn đạt H8 mạnh |
| chọc lét | A | D | D | Đồng ý họ với chọc léc; không cần gộp mọi từ đồng nghĩa |
| cửu chương | A | C | C | Chấp nhận cảnh báo dữ liệu, không gọi là thiếu đọc kiểm H8 |
| giở giọng | C | A | A | Rút ưu tiên thấp chỉ do sắc thái khi chưa có chứng cứ đỏ mới |
| giở quẻ | C | A | A | Xét toàn mục, không suy nghi lễ từ tiếng quẻ |
| hì hụi | A | D | D | Căn cứ mới là **hè hụi**, chưa xác nhận cùng từ với hì hục |
| loằng ngoằng | A | C | C | Chờ làm rõ họ loằn ngoằn; không tự coi bộ sinh biến thể là phán quyết |
| lỗi hẹn | A | C | C | Cảnh báo gần âm/nghĩa, không tự gộp với lỡ hẹn thành H5 |
| lời lỗ | A | C | C | Ưu tiên biên tập; H3/H8 lịch sử vẫn đạt |
| mỏng tanh | A | C | C | Ưu tiên biên tập; Leipzig 2 vẫn đạt H8 mạnh |
| mụ mị | C | A | A | Rút cờ thận trọng thiếu chứng cứ mới; không phục hồi phản đối H5 cũ |
| nhão nhẹt | A | D | D | Đồng ý quan hệ biến thể với nhão nhoẹt |
| nhão nhoẹt | A | D | D | Như trên; cần phân biệt mặt chữ và khóa |
| non choẹt | C | A | A | Không tự đồng nhất chê nhẹ với phản đối H6 hợp lệ |
| tạnh ráo | A | C | C | H8 yếu nhưng có đọc kiểm, không phải ngoại lệ không-lượt |
| thẳng đơ | A | C | C | H3 hai chữ ký và đọc kiểm H8 không mất hiệu lực |
| thụp | C | A | C | Vẫn ưu tiên thấp về độ quen khi đứng độc lập; không đổi OK thành R1 |
| tía lia | C | A | A | Rút cảnh báo sắc thái chưa đủ căn cứ thành cổng |
| tối mù | A | C | C | H8 sạch 1/0/1/0, không phải mạnh |
| tròng trành | A | D | D | Đồng ý họ chòng chành/tròng trành |
| trở lên | B | C | C | Chỉ cảnh báo lẫn với trở nên; **vẫn là mục chưa có nghĩa** |
| tuổi xanh | C | A | C | Giữ cảnh báo văn chương, không tự đổi nhãn OK |

**assumed:** đề nghị sau review của Astra là **A149/B36/C14/D6**, khác Opus ở *thụp, tuổi xanh* và căn cứ loại *hì hụi*. Hai chỗ C/A còn lại là nhận định ưu tiên, không phải phản đối H9. C là nhãn cảnh báo; không áp luật “C luôn sau A” để âm thầm đổi S4. Tổng 37 mục chưa viết không giảm thành 36: gồm B36 và *trở lên* ở C.

### 2.2. Sáu D và điều kiện H5c

**verified:** đã tự tải bốn wordlist **đúng commit ghim**, kiểm khớp cả bốn SHA của manifest, tra trong bộ nhớ và chỉ lưu đầu mục được hỏi, vị trí dòng, nhãn thành viên, hash. Không lưu payload GPL. Kết quả: `E\cross-review-hnd-membership.tsv`; nguồn/hash: `E\cross-review-hnd-sources.json`.

**verified:** đã kiểm số đếm trực tiếp trong `U\opus-counts.tsv`, không dùng bảng tổng hợp của Opus làm nguồn cuối. Hàm `verdict()` trong `AT\ho-so\opus\h5\verdict_h5.py:15–28` yêu cầu ≥20 mỗi kho và ≥95%; ví dụ nguyên tắc “chưa đo ≠ 0” vẫn phải giữ.

| Mục dự phòng | Quan hệ được Astra xác nhận | Số sạch phụ đề/web | Kết luận |
|---|---|---|---|
| hì hụi | **hì hụi ↔ hè hụi**, không phải mặc nhiên ↔ hì hục | hì hụi 0/0; hè hụi chưa đo | **assumed:** ký cùng từ cho cặp có liên kết dạng khác rõ. **verified:** hì hụi không thể đạt H5c với web 0 |
| tròng trành | chòng chành ↔ tròng trành | 3/6 ↔ 2/1 | **assumed:** đồng ý họ H5c. **verified:** hai kho đều dưới 20; nguồn từ vựng có tham chiếu trực tiếp |
| nhão nhẹt | nhão nhẹt ↔ nhão nhoẹt | 9/0 ↔ 6/1 | **assumed:** đồng ý biến thể âm đệm của cùng mục, không phải hai hành động khác nhau |
| nhão nhoẹt | Như hàng trên | nhão nhoét thêm 5/1; nhão nhét 0/0 | **verified:** kể cả cộng theo khóa, phụ đề 9 so với 11, web 0 so với 2; không đạt |
| chọc lét | Ít nhất chọc lét ↔ chọc léc; thọc lét/léc có thể ghi rộng hơn sau | chọc lét 5/0; các đối chứng chưa đo | **assumed:** đồng ý biến thể cuối t/c; không cần coi cù/chọc là cùng cách viết. **verified:** dạng chọc lét không thể đạt H5c với web 0 |
| chán phèo | chán phèo ↔ chán phè | chán phèo 20/0; chán phè chưa đo | **assumed:** đồng ý cùng từ; có tham chiếu từ vựng trực tiếp. **verified:** dạng chán phèo không thể đạt H5c với web 0 |

**verified:** với một dạng có web = 0, không cần giả số đo đối chứng: nếu tổng họ <20 thì thiếu dữ liệu; nếu tổng ≥20 thì dạng này chiếm 0%, không thể ≥95%. Điều đó loại **dạng này**, không chứng minh mọi dạng khác của họ đều phải bị loại. “Các đối chứng chưa đo” phải giữ là chưa đo, không ghi 0.

**verified:** số thô và số sạch ở các dạng đã đo của sáu ca trên không khác; đổi phụ đề sang dòng khác nhau không cứu điều kiện web. `E\cross-review-counts.tsv` lưu cả các cột đó và dòng gốc.

**assumed — phân biệt quan trọng về hì hụi:** tôi chưa ký quan hệ hì hụi/hì hục chỉ từ gần âm và gần nghĩa. Trang enwiktionary của *hì hụi*, revision `93445969`, ghi *hè hụi* ở nhóm dạng khác; cả hì hụi và hè hụi có trong wordlist ghim, và hè hụi không ở danh sách chính/dự phòng. Đây là căn cứ đủ tốt hơn để giải quyết D của dự phòng mà **không** suy tiếp *hì hục* chính cũng sai H5. Sự vắng liên kết với hì hục không chứng minh hai từ khác nhau; chỉ là chưa có căn cứ để gộp.

**verified:** liên kết *chòng chành → tròng trành* và *chán phèo → chán phè* đọc được ở Wiktionary; xem W1–W5 trong `E\cross-review-web-sources.tsv`. Quan hệ *nhão nhẹt/nhão nhoẹt* và *chọc lét/chọc léc* vẫn được ghi là phán đoán ngôn ngữ của Astra, không giả làm kết quả máy hoặc trích lời từ điển. Họ cù lét/cù léc đã được đăng ký cùng kiểu c tại `AT\spelling_families.tsv:116` là tiền lệ phương pháp, không tự động thay chữ ký cho họ mới.

**assumed:** ghi các họ mới trong kết quả phân tích có hai SA xác nhận; chưa sửa bảng họ dùng cho bản phát hành. *Chòng chành* chính có phát hiện H5 có căn cứ; *hì hục* chỉ là liên hệ cần nghiên cứu, chưa được kết luận tương tự. Cả hai vẫn nguyên byte theo phạm vi chủ giao.

**verified/assumed:** hồ sơ §6.1 chỉ mô tả đổi một vị trí (`WordListAnalyze.md:601–617`); mã mới `O\evidence\do-bien-the.py` mở rộng tổ hợp. Điều này hỗ trợ tìm cặp, không chứng minh mọi cặp là cùng từ. Không tìm thấy mã quét §6.1 đầy đủ trong các script đã lưu để tái chạy, nên không gọi mô tả phạm vi cũ là kiểm thử lại mã cũ.

### 2.3. Bao tử / báo tử và các còi khác

- **verified:** cùng toàn khóa `baotu`; cả hai là đầu mục HND. *Báo tử* có số sạch 26 phụ đề/2 web tại `U\opus-counts.tsv:13474`, không phải một cụm được bẻ ép từ âm tiết.
- **verified:** theo mẫu số đã ký, PPM gộp = **0,385521145 > 0,3**. Trung bình hai cột PPM lưu cũ là 0,385348; chênh mẫu số/làm tròn không đổi việc còi phải bật. Không tìm được còi tương ứng trong `U\canh-bao-khong-dau.tsv`.
- **verified:** mục từ *báo tử* liên quan thông báo cái chết, thuộc H6.4; nguồn W7. **assumed — phán đoán của Astra:** đây là cách đọc tự nhiên, thông dụng của nguyên khóa, tôi đề nghị **K1**, không phải K0. Không lấy ngưỡng 0,3 làm lệnh tự động loại; kết luận K1 gồm cả phán đoán vừa nêu.
- **assumed:** trước khi có chữ ký chung, để `CHO_H7_DE_NGHI_K1` và **không tính bao tử vào HM đã qua cổng**. Nếu Opus đánh giá là K2 thì cũng cần hai chữ ký cho đi tiếp, không được giữ nhãn “đạt H7 mới” chỉ vì bảng chặn chưa có khóa.
- **verified/assumed:** *tần số/tận số* khoảng 0,20733 và *vậy nên/vảy nến* khoảng 0,25302 đều dưới mốc còi; điều đó **không tự chứng minh PASS H7**. Tôi chưa áp K1 cho hai ca này trong review; đề nghị ghi việc khép nhận định K2/không tự chặn trước khi gọi là thẩm định mới hoàn tất. Đây là việc kỹ thuật giữa hai SA, không phải đề nghị nới H7.

### 2.4. Hai tập honorable mentions

**verified:** `E\cross-review-honorable-diff.tsv` có **309 dòng hợp**: chung 153, chỉ Astra 47, chỉ Opus 109. Phần chỉ Opus gồm DC1 5, DC2 34, DC3 46, DC4 19, DC5 5. Bảng có nguồn từng dòng, nhóm của mỗi bên, lý do Opus không chọn (nếu có), H8 số sạch/thiếu kho và hướng xử sau review.

**assumed — cách gộp đề nghị:**

| Phần | Nhận xét và hướng xử |
|---|---|
| 153 chung | Đồng ý nguồn cơ bản; giữ riêng cảnh báo bao tử, chạng vạng, tần số; sửa H8 của vây cá |
| 47 chỉ Astra | Đều là R1 trong pool; khác với việc Opus chỉ lấy phiếu lệch và F≥50. Không chọn không có nghĩa trượt H; riêng piano có lỗi dữ kiện H5 ở bộ lọc Opus |
| 5 DC1 chỉ Opus | cơ quan, lực lượng, truy tìm, dự bị, lên chức: Astra ưu tiên rà nghĩa thêm, chưa tuyên bố loại H6. Đây là lựa chọn đề cử thận trọng, không hủy nhãn OK cũ |
| 34 DC2 chỉ Opus | Cùng loại hồ sơ P4 đã xét, có thể gộp lựa chọn; không tự nâng R1 hoặc tạo ghế thay OK |
| 46 DC3 | Nguồn nghiên cứu đáng giữ; mới có số OPUS, thiếu DF và chưa có chấm đôi/H9. Cần nhãn/lớp đề nghị hoặc tách rõ danh mục chưa thẩm định |
| 19 DC4 | H8 yếu cần đọc đúng nghĩa; bánh củ cải và hoa mõm sói còn cờ cần H3 hai xác nhận. Không đổi “cần đọc” thành “đã đọc” |
| 5 DC5 | Đầu mục có trong HND nhưng chưa đo bốn kho, chưa nối xác nhận H3/hồ sơ P4. Chưa đủ để tính vào tập HM thỏa luật cứng |

**verified:** bảng Opus có **70 dòng chưa có lớp**, không chỉ chưa có F. Có thể là nguồn để xét, nhưng chưa đáp ứng phần yêu cầu “mỗi từ có lớp/chứng cứ và thỏa luật cứng”. Trong đó:

- *giờ cao điểm*: `U\l3b-de-cu-opus.tsv:3` chỉ ghi noun. **assumed — phản đối H2 của Astra:** ba khối gọi khoảng thời gian, không thuộc nhóm tên người/vật/loài/món ăn/nơi chốn/thiết bị của `AT\tieu-chi-thong-nhat.md:79–84`. Một nhãn noun và phép đếm 3 khối không đủ; các mục ba khối chính hiện có đều lớp C. Để `CHO_H2`, không tuyên bố đã đạt.
- *ớt đỏ, nắng ấm*: Opus đã ghi cần xét X; vì thế không thể đồng thời coi đã hoàn tất H3 cho mọi dòng.
- *bánh củ cải*: 15 lượt web là ca sát mốc theo mẫu số; bảng L2D gốc ghi yếu. Giữ cảnh báo nguồn/mẫu số và đọc nghĩa, không tự hợp thức hóa cả lô bằng đổi mẫu số.

**assumed:** không cần đưa cả 309 vào tài liệu rồi vượt trần 300. Tách 70 chưa thẩm định, 5 cần rà nghĩa theo đề nghị Astra và 3 ca H5/H7 nêu trên, còn **231 mục lõi theo hồ sơ** để hai SA lựa chọn, trong khoảng chủ yêu cầu. Đây chưa là danh sách được duyệt chung hoặc được phép phát hành.

**verified:** tái kiểm 231 mục lõi không thấy trùng khóa/họ đã cấm, thiếu chứng cứ H3 bắt buộc trong hồ sơ cũ hoặc thiếu nguồn H9; H8 sạch gồm 230 mạnh và 1 yếu (*vây cá*, đã có đọc kiểm). Mỗi mục được nối lại dữ liệu gốc bằng script, không mặc nhiên tin bảng của bên nào.

## 3. Lỗi hoặc kết luận cần sửa trong phân tích Opus

1. **Hì hục bị suy quá mức.** **verified:** bộ phân loại hard-code cùng từ với hì hụi ở `O\evidence\phan-loai-du-phong.py:23`; HND chỉ chứng minh hai mặt chữ tồn tại. **assumed:** chưa đủ để đưa hì hục vào nhóm chính sai H5. D của hì hụi nay có căn cứ độc lập với **hè hụi**, không phải chữ ký đồng ý cặp Opus nêu.
2. **Piano bị loại bằng dữ kiện sai.** **verified:** `O\evidence\lap-de-cu.py:70` gắn `H5`; `de-cu-ung-vien.tsv:208` ghi chưa đo. Nhưng `AT\spelling_families.tsv:269` đã ghi 449/3 phụ đề và 1.818/2 web, `QUA_RIENG_H5`. Có thể không thích đưa từ này vào danh mục, nhưng không dùng lý do “H5 chưa đo”. Không có bằng chứng họ mới khác được nêu.
3. **40 từ không thành 77 ghế riêng biệt.** **verified:** A-F có 40 từ. Chúng có thể thay bất kỳ ghế F phù hợp khi xét một lần, nhưng tối đa 40 ghế cùng lúc, không phủ 77 phép thay riêng biệt. Lý do không viết nghĩa ngay là **phạm vi chỉ phân tích**, không phải phép đếm ở CH4 (`O\round-1-analysis.md:196`, `:342`).
4. **36 B không phải tổng thiếu nghĩa.** **verified:** còn *trở lên* ở C chưa viết; tổng vẫn 37. Cần giữ trục trạng thái nghĩa độc lập với bậc ưu tiên.
5. **Phép kiểm độ dài không phải toàn bộ H2/H3/H6/H9.** **verified:** `O\evidence\kiem-dau-ra.py` chỉ kiểm số chữ/khối, khóa và họ trong bảng, không xét loại thực thể ba khối hay hoàn tất H6 cho 70 mục mới. Trường `xac_minh` không nên khiến người đọc hiểu cả 262 đã thỏa mọi luật. Ví dụ cụ thể là *giờ cao điểm* và hai tổ hợp đang chờ X.
6. **Tổng 122 sau bỏ D là trần cấu trúc, không phải 122 gói dùng được.** **verified:** C còn *loằng ngoằng* chờ H5; toàn bộ dự phòng chưa có D8; 37 F chưa có nghĩa. Phải báo riêng số khóa, số câu, số ghế và số mục đã khép cổng.
7. **Không nên ban hành TT2 trong bước phân tích.** **verified:** S4 đã đóng băng theo bậc OK/R1, điểm và O1; Opus cũng thừa nhận cần luật v1.1. **assumed:** chỉ công bố cảnh báo C, chưa thay chỉ dẫn chọn từ trong README thành một thứ tự vận hành mới A→C. Không biến việc phân loại thành thay đổi quy trình thay thế mà chủ chưa yêu cầu.
8. **Phủ định về chất gây nghiện không có cơ sở.** **verified ở mức kết quả tìm kiếm nguồn:** chương IARC về ngừng sử dụng thuốc lá không khói/cau nêu cau có chất gây nghiện; W8 lưu URL và giới hạn web-fetch bị challenge. **assumed:** có thể nhận ăn trầu theo phạm vi H6 hiện hành, nhưng không lập luận rằng mọi trầu cau không gây nghiện hoặc vô hại.
9. **“Lỗi giả” CRLF dễ gây hiểu nhầm.** **verified:** nguồn chuẩn đã quy định LF và checker thật sự thấy CR, nên đó là lỗi định dạng checkout có thật, không phải false-positive của phép đọc byte. Đối chứng blob LF chứng minh nội dung chuẩn đạt; hai kết quả phải được trình bày riêng.

**assumed — không xem là lỗi:** chọn 60 R1 thay vì mọi R1; giữ C cho từ ít chứng liệu; hoặc không chọn từ gần nghĩa. Đây là chiến lược biên tập được phép, miễn không gán sai cổng, không coi điểm F là xác suất biết từ và không đổi S4 ngầm.

## 4. Sửa nhận định của chính Astra

1. **verified — sửa lỗi H8:** `E\inventory.py` vòng 1 dùng số bề mặt để đặt mức mạnh. *Cả nghĩ* bề mặt 8/4 nhưng sạch 2/0, L/T 0/0; *tối mù* bề mặt 6/1 nhưng sạch 1/0, L/T 1/0. Do đó **200 mạnh/4 yếu/1 không-lượt → 198/6/1**. Hai mục vẫn có hồ sơ đọc H8: `U\chu-ky.tsv:225`, `:2273–2275`.
2. **verified — lỗi tương tự ở HM:** *vây cá* bề mặt 10/26 nhưng sạch 3/7, L/T 0/0. Khẳng định “200 HM đều H8 mạnh” phải sửa thành **199 mạnh + 1 yếu đã đọc kiểm**. Nguồn: `U\opus-counts.tsv:12697`, `U\phieu-astra.tsv:4811`, `U\chu-ky.tsv:2397–2399`. Không loại lại mục đã có chứng cứ đúng nghĩa chỉ vì đổi nhãn số học.
3. **verified/assumed — H5:** bảng đóng băng không có họ cấm không có nghĩa mọi họ mới đã qua. Rút A cho sáu D và bổ sung cảnh báo *loằng ngoằng*. Với *hì hụi*, chữ ký cũ về dạng hỳ hụi không giải quyết dạng **hè hụi** mới được nối; không hủy hay viết lại lịch sử tranh luận cũ.
4. **verified/assumed — H7:** rút *bao tử* khỏi tập gọi là đã qua cổng; thêm cảnh báo chưa khép cho *tần số*, và cảnh báo riêng *vậy nên* ở bảng dự phòng. Không tự sửa danh sách khóa chặn của bản phát hành.
5. **assumed — bỏ thận trọng thiếu căn cứ thành tầng:** chuyển tám C cũ về A như bảng §2.1; vẫn giữ *thụp, tuổi xanh* là C biên tập. Không tự chuyển nhãn OK sang R1 hoặc dùng cảm giác làm phản đối H9.
6. **assumed — cách diễn đạt:** “A sẵn sàng” phải hiểu là hồ sơ ưu tiên chuẩn bị thay, không phải quyền thay ngay. Không đếm gộp C đang chờ H5/H7 vào nguồn đã khép cổng. Bảng gốc vòng 1 là ảnh chụp độc lập; khi sinh bảng chung phải áp sửa lỗi trong diff/metrics lần này, không chạy lại builder cũ rồi giữ kết luận H8 sai.

## 5. Danh sách câu hỏi hợp nhất

**assumed — đề nghị của Astra để Opus xác nhận; không tự đổi quyết định chủ:**

| ID | Người nhận cũ | Đề nghị trạng thái | Lý do và cách ghi |
|---|---|---|---|
| CH1 | Chủ | **Rút câu hỏi thay phạm vi hiện tại; giữ việc hậu kiểm** | Chủ đã yêu cầu chính bất biến. Ghi phát hiện chòng chành; chưa gọi hì hục là vi phạm đã xác nhận. Rà/đổi danh sách chính ở đợt sau chỉ khi chủ giao |
| CH2 | Chủ | **Rút** | Cả hai đề nghị giữ 205 dòng và SHA, tầng D ở bảng phân loại. Không có lựa chọn phạm vi chưa được giải quyết cần chặn báo cáo |
| CH3 | SA-Fable | **Rút trong phạm vi hiện tại** | Dự phòng hiện hành chỉ thay cùng ngăn; quota Q2 không cho mượn ghế OK. Một đợt xây danh sách mới khi thật sự hết OK là bài toán P6 khác, không phải phép thay trực tiếp này |
| CH4 | Chủ | **Rút** | Chủ đã chốt chỉ phân tích; chưa giao viết nghĩa. Nêu đủ 37 thiếu nghĩa và giới hạn 40 phép thay, không hỏi lại vì phép đếm sai |

**verified — căn cứ CH3:** `AT\tieu-chi-thong-nhat.md:407` ghi rõ R1 chỉ thay R1. `U\p6-tinh-doc-lap-astra.py:61–73` áp đúng điều đó; nhánh cho R1 thay OK ở `:105–122` tự ghi `khong_phai_quy_tac_da_ky=True`. Hàm chọn danh sách mới ở `:75–104` là bước khác. Vì vậy không nói “R1 vĩnh viễn phải nâng thành OK mới có thể phát hành”, nhưng cũng không dùng Q2 để tự sửa quy tắc dự phòng hiện hành.

**assumed — giữ/mới:** không có câu hỏi owner/supervisor còn cần mở cho đợt chỉ phân tích; chưa tạo CH5+. Các việc cần Opus trả lời ở review kỹ thuật là: xác nhận sáu D với căn cứ mới; khép nhận định H7; sửa piano/40–77/37 thiếu nghĩa; phân biệt 70 ứng viên chưa thẩm định với HM đã qua cổng; thống nhất hai C còn khác và cách trình bày ưu tiên không đổi S4.

**assumed:** nếu sau trao đổi thực sự còn bất đồng ảnh hưởng cổng/policy, lúc đó mới lập CH5+ với hai lập trường và chứng cứ cụ thể, không gửi supervisor các giả định chưa phát sinh. Những điểm có thể giữ ở trạng thái chưa duyệt hoặc ngoài tập HM lõi không buộc nới luật để hoàn tất yêu cầu.

## 6. Bằng chứng, lệnh và giới hạn

**verified — chạy từ gốc repo, không ngẫu nhiên:**

```powershell
python -X utf8 -B 'analyzing-tools\ho-so\astra\du-phong-v2\evidence\cross-review.py' --verify-hnd
python -X utf8 -B 'analyzing-tools\ho-so\astra\du-phong-v2\evidence\cross-review.py'
```

Lệnh đầu kiểm lại bốn SHA nguồn HND trong bộ nhớ; lệnh sau tái sinh diff/số liệu từ tệp hiện có, không tải lại. Cả hai chỉ ghi trong `E`. Không chạy các script sinh đầu ra của Opus.

| Tệp mới | Nội dung |
|---|---|
| `A\round-1-cross-review.md` | Review này, bao gồm chữ ký nhận định riêng của Astra |
| `E\cross-review.py` | Chương trình tái lập, hàm H8 số sạch và các phán đoán mới có ghi nhãn |
| `E\cross-review-reserve-diff.tsv` | Đủ 205 dòng, 28 khác tầng, nguồn và việc sửa |
| `E\cross-review-honorable-diff.tsv` | Hợp 309 từ, có/không ở mỗi bên, nguyên nhân và trạng thái sau review |
| `E\cross-review-counts.tsv` | Số bề mặt/sạch/dòng khác nhau, PPM theo mẫu số ký và cột PPM cũ |
| `E\cross-review-hnd-membership.tsv` | Chỉ thành viên của 25 đầu mục được hỏi và vị trí dòng nguồn, không lưu wordlist |
| `E\cross-review-hnd-sources.json` | URL ghim, SHA kỳ vọng/thực tế, số byte/dòng của bốn nguồn |
| `E\cross-review-web-sources.tsv` | URL, quan hệ từ vựng/nhãn đã đọc và thất bại truy xuất; không lưu định nghĩa, IPA, ví dụ hoặc hình |
| `E\cross-review-inputs.json` | Hash các dữ liệu/mã thực sự dùng để đối chiếu |
| `E\cross-review-metrics.json` | Ma trận, giao/hợp, mức H8 sửa lại, quantile và phép tính còi |
| `E\cross-review-verification.json`, `E\cross-review-run.log` | Lệnh, kiểm hash đầu vào/vùng bảo vệ, định dạng, pointer và chạy hàm H5/P6 gốc bằng AST không có tác dụng phụ |

**verified/assumed — giới hạn:** không đo lại toàn bộ kho; các số sạch là số đã lưu ở commit gốc. Quan hệ ngôn ngữ được phân biệt khỏi số liệu và được ghi ký bởi Astra tại §2.2. Không sao chép lời từ điển hoặc corpus vào đầu ra. Không sửa tệp của Opus, tệp sản xuất, các bảng độc lập vòng 1 hay bất kỳ vùng bảo vệ nào.
