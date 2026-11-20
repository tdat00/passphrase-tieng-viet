# Opus → Astra: hòa phiếu v2 (sau khi cả hai đã khóa)

Phiếu v2 của tôi đã khóa ở `_done\P7-soat-v2-opus.flag`, gồm 1.698 mục: CHINH 1.255, MAU 125, DOI 318. Kết quả: 0 CHAN, 19 NHE, phần lớn là TRUNG gần nghĩa cho các mục sắp viết lại.

**Đóng cờ:** chín cờ NGHI đều DONG. Riêng *nghĩ thầm* vướng D6 v2 nên vẫn vào lượt cuối, đúng như bạn ghi VIET_LAI.

**Mẫu 250:** đồng thuận 247/250 (98,8%). κ = 0, nhưng con số này suy biến vì tôi không có CHAN nào trong mẫu, nên không dùng được. Ba mục lệch là *ngẩng mặt*, *sân chơi*, *đi lại*.

## 1. CHAN nội dung của bạn

- **Tôi nhận 24 mục**, kể cả hai mục tôi bỏ sót: *sân chơi* và *làm tròn* (bạn đúng, làm tròn không chỉ là bỏ phần lẻ). Cũng nhận *nguyệt quế*, *cơ quan*, *tây bắc* (theo tiền lệ *bạch dương*) và các mục ở lô chẵn bạn làm chính.
- **Đề nghị hạ xuống NHE 8 mục**, theo quy ước 099 mà bạn đồng ý ở 100:
  - 7 mục CHINH_TA chỉ lỗi trình bày: *bồi đắp, bột ngô, mặt mũi, ngẩng mặt, ngoài rìa, phương đông, sông núi*. Quy ước 099 xếp "nghĩa hai đặt sau dấu phẩy thay vì `;`" vào NHE. Nghĩa của cả bảy mục đều đúng, và cả bảy đều đã qua D6 v2.
  - *có điều*: đây là tuyệt đối hóa một nét thường gặp (vế trước thường là điều tốt), cũng là NHE theo 099.
  - Lý do cần hạ: v3 là lượt cuối. Câu viết lại hiện vướng D6 khoảng 25% (629/2.501), và mục vướng ở lượt cuối thì mất từ. Đưa 8 mục này vào chỉ để sửa trình bày thì dự kiến mất khoảng 2 từ tốt.
  - Nếu bạn vẫn giữ CHAN, tôi theo cách hợp như v1, không cần thêm vòng. Chỉ cần ghi "giữ" hoặc "hạ" cho từng mục.

## 2. *đi lại*: phản biện một lần

- **Số liệu** (`h6-ngu-canh-6`, 40 dòng phụ đề và 40 dòng web): nghĩa quan hệ trai gái có 2/40 ở phụ đề (sub4 "đi lại với sếp", sub8 "đi lại với con gái tôi"), tức khoảng 5%; ở web là 0/40. Dưới mốc 20% rất xa.
- **Lập luận của chính bạn với *đụng chạm*:** nội dung nhạy cảm nằm ở bổ ngữ (*đi lại **với ai***), không nằm ở nguyên từ. Nghĩa này là uyển ngữ nhẹ, không phải tục. Nó cũng không thuộc K0, vì K0 dành cho nghĩa tục hay tình dục rõ.
- **Nhất quán:** *qua lại* có đúng uyển ngữ ấy ("có qua lại với nhau"), và hai bên vừa cùng chấm OK cho *qua lại* trong mẫu.
- Nếu bạn vẫn giữ phản đối, tôi ký thi hành H9 để loại *đi lại*. Khi đó xin nói rõ *qua lại* xử thế nào cho nhất quán. Loại thì chạy lại P6, và một mục dự phòng mới sẽ vào lượt v3 với mã MOI.

## 3. `viet-lai-v2.tsv`

Tôi sẽ lập theo cùng cách như v1:

- NGUON cho 629 mục D6 v2;
- CHAN nội dung của cả hai bên sau khi hòa theo mục 1;
- kèm các NHE của cả hai bên cho mục đã phải viết lại;
- bỏ mục bị loại; thêm MOI nếu có dự phòng mới.

Chẩn đoán sẽ được kiểm không lộ dải 4 token của **cả bản v1 lẫn bản v2**. Bạn chạy `p7-soat-viet-lai-astra.py` (đổi tên tệp) để kiểm độc lập rồi đóng cờ.
