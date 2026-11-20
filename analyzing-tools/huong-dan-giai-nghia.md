# Hướng dẫn viết giải nghĩa (cho lượt viết sạch)

Tài liệu này dành cho người hoặc agent viết giải nghĩa cho danh sách từ của dự án passphrase tiếng Việt. Mỗi giải nghĩa hiện cạnh từ trên trang thông tin, giúp người dùng hiểu và dễ nhớ từ có trong passphrase của mình. Mọi giải nghĩa sẽ phát hành theo giấy phép MIT, nên **phải là lời của chính bạn**.

Hướng dẫn cố ý **không có câu giải nghĩa mẫu nào của từ thật**. Các khung ở mục 7–8 chỉ có chỗ trống, đặt trong ngoặc nhọn `<…>`.

## 1. Nguồn: chỉ dùng hiểu biết của bạn

1. Chỉ được mở ba file: lô từ (`lo-XX.txt`), hướng dẫn này, và `kiem-tra-giai-nghia.py`. Không mở file hay thư mục nào khác.
2. Không tra từ điển, Wiktionary, Wikipedia, trang web, công cụ dịch hay danh sách từ nào khác. Không hỏi agent khác về nghĩa của từ.
3. Không cố nhớ lại rồi chép câu chữ của một từ điển. Hãy hiểu nghĩa rồi diễn đạt bằng lời thường của mình.
4. Nếu không chắc một nét nghĩa, chỉ viết phần bạn chắc chắn và gắn cờ `NGHI`. Nếu không biết từ, để trống giải nghĩa và gắn cờ `KHONG_BIET`. Đừng đoán.

## 2. Đầu vào và đầu ra

**Đầu vào:** `lo-XX.txt`, UTF-8, mỗi dòng một từ (NFC), không có dòng tiêu đề, đã xếp sẵn theo thứ tự.

- Nếu script báo **LỖI LÔ** (lô có BOM, dòng trống, từ lặp…), hãy báo lại người điều phối. Không tự sửa lô.

**Đầu ra:** `lo-XX.tsv`, UTF-8, xuống dòng LF, có xuống dòng ở cuối file.

- Dòng đầu là tiêu đề `tu<TAB>giai_nghia<TAB>co`.
- Sau đó mỗi từ một dòng: `từ<TAB>giải nghĩa<TAB>cờ`.
- Đúng thứ tự và đúng số từ của lô. Chép nguyên từng kí tự của từ.
- Cột `co` để trống nếu không có cờ; nhiều cờ thì nối bằng `;`, không có dấu cách.

Khuôn dòng (không phải nội dung thật):

```text
tu	giai_nghia	co
<từ thứ nhất>	<Câu giải nghĩa một nghĩa.>	
<từ thứ hai>	<Nghĩa thứ nhất>; <nghĩa thứ hai.>	HAI_NGHIA
<từ thứ ba>		KHONG_BIET
```

## 3. Hình thức

- **Đúng một câu**, khoảng **5–15 tiếng**, tối đa **110 kí tự**.
- Viết hoa chữ đầu và kết thúc bằng một dấu chấm. Không có dấu chấm, chấm than hay chấm hỏi nào khác trong câu.
- Chỉ viết hoa thêm tên riêng thật sự cần (tên ngày lễ, tên địa danh khi là một phần của nghĩa).
- Chỉ dùng chữ cái tiếng Việt cùng các dấu `, ; : ( ) - /`.
- **Không dùng:**
  - kí tự `|`, tab, ngoặc kép, nháy đơn, dấu ba chấm, biểu tượng cảm xúc;
  - chữ số: nếu con số thuộc bản chất của nghĩa (số cạnh, số chân, đơn vị đo) thì viết bằng chữ;
  - viết tắt (*v.v., vd.*);
  - từ tiếng nước ngoài và các chữ `f, j, w, z` (kể cả khi đầu mục là từ mượn: mô tả bằng tiếng Việt).
- **Chính tả:**
  - theo chuẩn phổ thông, dạng Unicode dựng sẵn (NFC);
  - đặt dấu kiểu cũ, thống nhất trong mọi câu (ví dụ *òa, óa, ỏe, úy*, không viết *oà, oá, oẻ, uý*).
- **Không mở đầu bằng:**
  - chính đầu mục;
  - chữ *Là*, *Xem*, *Như*.

## 4. Chọn nghĩa

1. Viết **nghĩa phổ biến nhất hiện nay**: nghĩa mà phần lớn người đọc phổ thông, kể cả học sinh, nghĩ tới đầu tiên khi gặp từ.
2. Chỉ thêm **một** nghĩa thứ hai khi nghĩa đó cũng rất phổ biến và khác hẳn nghĩa đầu.
   - Hai vế nối bằng **đúng một** dấu `;`. Vế sau mở đầu bằng một liên từ tự nhiên, hợp với từ loại, như *cũng chỉ…*, *còn có nghĩa…*.
   - Gắn cờ `HAI_NGHIA`. Không bao giờ quá hai nghĩa.
3. Nếu nghĩa bóng phổ biến hơn nghĩa đen thì viết nghĩa bóng.
4. **Không "làm sạch" nghĩa.** Có từ mà nghĩa phổ biến nhất thuộc một trong các nhóm dưới đây. Khi đó, vẫn viết đúng nghĩa ấy bằng giọng trung tính rồi gắn cờ `NHAY_CAM`; đừng thay bằng một nghĩa phụ ít người dùng cho "sạch". Các nhóm:
   - bạo lực, vũ khí, quân sự;
   - tội phạm, pháp luật, hình phạt;
   - chính trị, bầu cử, quyền lực nhà nước;
   - tôn giáo, nghi lễ, tang lễ, cái chết;
   - bệnh tật, thương tích, y khoa;
   - tình dục;
   - cờ bạc, rượu bia, thuốc lá, ma túy;
   - thảm họa;
   - chửi rủa, miệt thị;
   - điều ghê tởm.

   Nếu không thể nêu nghĩa ấy bằng lời trung tính, được để trống giải nghĩa kèm cờ `NHAY_CAM`. Người soát sẽ quyết định có giữ từ đó hay không.
5. Nếu bạn biết từ có một **nghĩa phụ tục hoặc tình dục** đang được dùng phổ biến: không viết nghĩa đó, không ám chỉ, nhưng phải gắn cờ `TUC_PHU`.

## 5. Viết theo loại từ

| Loại | Cách viết |
|---|---|
| Đồ vật, dụng cụ | Thuộc loại gì, cộng ít nhất một nét phân biệt (hình dạng, chất liệu, cơ chế) và công dụng chính |
| Con vật, cây, quả | Loài gì, cộng nét nhận biết dễ thấy: hình dáng, màu, nơi sống, công dụng |
| Món ăn | Nguyên liệu chính, cộng cách làm hoặc đặc điểm |
| Người, nghề | Người như thế nào, hoặc làm việc gì |
| Hành động (động từ) | Bắt đầu bằng một động từ khái quát; nêu đối tượng, cách thức hay mục đích nếu cần |
| Tính chất (tính từ) | Tả tính chất hoặc mức độ; nêu phạm vi thường dùng nếu giúp hiểu |
| Từ láy tả âm thanh | Bắt đầu bằng *Tiếng…*: âm thanh như thế nào, thường phát ra từ đâu |
| Từ láy tả dáng vẻ | Tả dáng, trạng thái |
| Từ trừu tượng | Nói rõ đó là tình cảm, trạng thái, việc hay quan hệ gì |
| Từ địa phương | Tả sự vật, kèm *cách gọi ở miền Nam/Bắc/Trung* (chỉ khi chắc) |
| Từ chức năng (nếu có trong lô) | Nêu chức năng: *Từ dùng để…* |

- **Nét thường gặp không phải điều kiện bắt buộc.** Nếu một đặc điểm chỉ đúng với phần lớn trường hợp (chất liệu, kích cỡ, cơ chế, lý do), hãy thêm *thường* hoặc bỏ đặc điểm đó. Đừng viết như thể mọi trường hợp đều vậy.
- Không giải nghĩa chỉ bằng một từ đồng nghĩa. Nếu dùng từ đồng nghĩa thì phải kèm ít nhất một nét mô tả.

## 6. Văn phong

- Trung tính, giản dị, câu ngắn. Ưu tiên từ thuần Việt dễ hiểu hơn từ Hán Việt hay thuật ngữ.
- **Không:**
  - lời khen chê, so sánh tuyệt đối (*nhất, ai cũng, tuyệt vời*);
  - lời khuyên, bài học đạo đức, đùa cợt;
  - định kiến giới, vùng miền, dân tộc.
- **Không đưa thông tin dễ sai hoặc mau cũ:** mốc thời gian, chữ *hiện nay*, giá cả, số liệu thống kê, tên hãng, địa danh hay người cụ thể không thuộc nghĩa của từ.
- Không lặp một khuôn mở đầu cho mọi câu. Viết tự nhiên nhưng nhất quán.

## 7. Khuôn câu (chỉ có chỗ trống)

| Loại | Khuôn |
|---|---|
| Đồ vật | `<Loại đồ vật> <nét phân biệt>, dùng để <công dụng chính>.` |
| Con vật, cây | `<Loài gì> <nét nhận biết>, thường <nơi sống hoặc công dụng>.` |
| Món ăn | `Món <làm từ nguyên liệu chính>, <cách làm hoặc đặc điểm>.` |
| Động từ | `<Động từ khái quát> <đối tượng hoặc cách thức> (để <mục đích>).` |
| Tính từ | `<Có tính chất hoặc mức độ…>, thường nói về <phạm vi>.` |
| Âm thanh | `Tiếng <đặc điểm âm thanh>, như tiếng <nguồn phát quen thuộc>.` |
| Dáng vẻ | `<Tả dáng hoặc trạng thái>, thường khi <hoàn cảnh>.` |
| Trừu tượng | `<Tình cảm/trạng thái/việc/quan hệ> <nội dung cụ thể>.` |
| Địa phương | `Cách gọi ở miền <vùng> của <sự vật>, <nét mô tả>.` |
| Hai nghĩa | `<Nghĩa thứ nhất>; <liên từ tự nhiên> <nghĩa thứ hai>.` kèm cờ `HAI_NGHIA` |

## 8. Lỗi thường gặp (không làm theo)

| Kiểu sai (dạng khuôn) | Lỗi |
|---|---|
| `Tiếng <đầu mục>.` | Lặp lại đầu mục, không giải thích gì |
| `<Người> luôn <đầu mục> khi <việc>.` | Câu ví dụ, không phải giải nghĩa |
| `Người đang <hành động>.` cho một từ tả dáng | Sai từ loại |
| `Đồ dùng tiện lợi nhất mà nhà nào cũng có.` | Chủ quan, tuyệt đối, thiếu nét phân biệt |
| `Sản phẩm của hãng <tên hãng>, hiện nay giá khoảng <số tiền>.` | Tên hãng, thông tin mau cũ |
| `Một loại <phạm trù rất rộng>.` | Quá rộng, không phân biệt được với vật khác |
| `<Một đặc điểm chỉ đúng với một phần> là điều bắt buộc.` | Biến nét thường gặp thành điều kiện bắt buộc |
| `Đức tính mà ai cũng phải có.` | Lời khuyên, không nêu nghĩa |
| `Xem <từ khác>.` hoặc chỉ `<Từ đồng nghĩa>.` | Tham chiếu hoặc chỉ đưa từ đồng nghĩa |
| `<Nghĩa 1>; <nghĩa 2>; <nghĩa 3>.` | Quá hai nghĩa |
| `Là <nội dung>.` | Mở đầu bằng *Là*, thừa chữ |

## 9. Từ gần nghĩa và câu trùng

- Hai từ khác nhau không được có giải nghĩa giống hệt nhau (kể cả khác lô).
- Với từ gần nghĩa, nêu đúng nét khác có thật, ví dụ mức độ, đối tượng, vùng miền, sắc thái trang trọng hay thân mật. **Không bịa** ra khác biệt.
- Nếu không thấy khác biệt rõ, hãy viết mỗi câu từ một góc khác nhưng vẫn đúng, và gắn cờ `NGHI`.

## 10. Cờ

| Cờ | Khi nào dùng | Giải nghĩa |
|---|---|---|
| `NHAY_CAM` | Nghĩa phổ biến nhất thuộc các nhóm ở mục 4.4 | Viết trung tính; được để trống nếu không thể viết trung tính |
| `TUC_PHU` | Có nghĩa phụ tục hoặc tình dục phổ biến | Không ghi nghĩa đó |
| `HAI_NGHIA` | Câu có hai nghĩa nối bằng đúng một `;` | Bắt buộc có `;` |
| `NGHI` | Không chắc nghĩa, nét phân biệt hay sự kiện trong câu | Phải có câu |
| `KHONG_BIET` | Không biết từ | Để trống; không đi cùng cờ khác |

Các cờ `NHAY_CAM`, `TUC_PHU`, `NGHI`, `KHONG_BIET` chỉ được phép ở bản nháp. Người soát phải đóng hết trước khi nhập vào thành phẩm.

## 11. Tự kiểm trước khi nộp

1. Đủ dòng, đúng thứ tự, từ chép nguyên, có dòng tiêu đề, có xuống dòng cuối file.
2. Mỗi giải nghĩa là đúng một câu, khoảng 5–15 tiếng, không quá 110 kí tự, viết hoa chữ đầu, có dấu chấm cuối.
3. Không có kí tự cấm, chữ số, chữ ngoài bảng chữ cái tiếng Việt, ngoặc kép.
4. Không lặp nguyên đầu mục; không mở đầu bằng *Là*, *Xem*, *Như*.
5. Đúng từ loại; danh từ có nét phân biệt; nét thường gặp có chữ *thường*.
6. Nghĩa phổ biến nhất đứng trước; tối đa hai nghĩa, đúng một dấu `;` khi có hai nghĩa.
7. Không chủ quan, không thông tin mau cũ, không tên hãng, không lời khuyên.
8. Không có hai câu giống nhau.
9. Gắn cờ đúng, không dùng cờ mâu thuẫn.
10. Chạy `python kiem-tra-giai-nghia.py lo-XX.txt lo-XX.tsv`. Sửa hết mọi dòng **LỖI**; đọc lại mọi dòng **CẢNH BÁO** và chỉ giữ nguyên khi bạn chắc là đúng. Có **LỖI LÔ** thì báo người điều phối.

## 12. Dành cho người điều phối (không gửi mục này cho người viết)

- **Cách ly:**
  - Mỗi lượt viết hay viết lại là một agent mới, không kế thừa hội thoại.
  - Agent làm việc trong một thư mục riêng chỉ chứa ba file: hướng dẫn này (bỏ mục 12), `kiem-tra-giai-nghia.py` và một lô từ.
  - Chỉ cấp quyền đọc ba file đó và quyền ghi file nộp; không cấp quyền duyệt repo, mạng hay thư mục khác.
  - Không đưa vào lời nhắc: giải nghĩa cũ (Opus, Astra), lời từ điển, `bang-khoa-chung.tsv`, các file soát và phản hồi.
- **Chia lô:**
  - mỗi lô tối đa khoảng 400 từ, lấy liên tiếp theo thứ tự O1, để các từ cùng họ nằm chung một lô;
  - viết cả cho các từ dự phòng.
- **Lượt viết lại** chỉ nhận:
  - đầu mục;
  - một chẩn đoán ngắn: mã lỗi và mô tả vấn đề bằng lời của người soát.

  Lượt viết lại **không** nhận câu của lượt trước, câu bị nghi trùng nguồn, chuỗi trùng, câu mẫu hay giải nghĩa cũ. Người soát giữ liên kết giữa các lượt ở phía điều phối.
- **Sau khi gộp các lô:**
  - chạy `python kiem-tra-giai-nghia.py --phat-hanh <các cặp lô>` (kiểm trùng toàn danh sách và cờ còn mở);
  - người soát chạy kiểm nguồn gốc D6 theo `tieu-chi-thong-nhat.md`.
- **Mục không đạt sau hai lượt viết:** thay bằng từ dự phòng. Riêng đầu mục chủ dự án buộc giữ thì không xóa: giao một lượt sạch mới hoặc trình chủ dự án.
