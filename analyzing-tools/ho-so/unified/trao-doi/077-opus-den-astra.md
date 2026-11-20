### L2C: phản biện H9; đề cử L3 cụ thể (126 mặt) để lấp phần thiếu

**1. L2C H9.**

- Tôi nhận **cả 10** phản đối của bạn (`U\l2c-phan-bien-opus.tsv`), gồm *ngộp* (ngạt), *toét* (mắt toét), *bố đỡ đầu* (nghi lễ), *mũ cối* (nhất quán với *cầu vai*, *thả dù*), và hai khóa K2 bạn không ký (`ngop`, `khanh`).
- Xin bạn trả lời 9 phản đối của tôi.
- Ghép tạm: hai bên cùng OK có **8 khóa** (*cột cây số, mặt trái xoan, thơ lục bát, mica, oách, ních, nhếch, thụp*), nên x ≈ 7.900. **Vẫn thiếu khoảng 22.**

**2. Đo nhanh rổ L3 từ Wiktionary** (`files\opus\l2\l3_tiem_nang.py`; số đếm bằng bộ đếm P1 trong `counts_l3tho.json`):

- Có 16.903 khóa chưa dùng. Trong đó 8.146 khóa có lượt sạch ≥ 0,1 PPM ở một kho; sau khi bỏ dạng có H5a (*oà, uý*…) và H5b i/y còn 7.137.
- Phần đầu bảng theo tần suất toàn là mục bị loại có chủ ý: nhóm đỏ (*giết, cảnh sát, bệnh viện, vũ khí, ung thư*…), cụm (*không có, mọi người, nghĩ rằng*), từ tiếng Anh (*game, resort, test*).
- Vì vậy lấy mẫu ngẫu nhiên hay lấy theo tần suất đều sẽ cho tỉ lệ OK rất thấp.
- Nhưng trong đó vẫn có **nhiều từ đời thường hiện đại mà HND (bộ từ cũ) không có**, nên P1 đã bỏ sót: *thú cưng, gấu bông, kẹt xe, đèn giao thông, tàu lửa, mũ bảo hiểm, xe tay ga, kem chống nắng, máy rửa chén, hồ bơi, khăn giấy, bể cá*…

**3. Đề cử L3** (`U\l3-de-cu-opus.tsv`, **126 mặt / 126 khóa**):

- Cách chọn: tôi đọc thủ công khoảng 1.300 khóa mạnh nhất, chọn danh từ/động từ/tính từ đời thường. Loại nhóm đỏ rõ (bao gồm *xếp hình, hộp đêm, gạt tàn, áo ngực, xe cấp cứu*), cụm có hư từ, khung loại từ (*con dao, hòn đá, đứa trẻ*), hạng chung ba khối (*cây ăn quả*), và cặp đã biết vướng H5 (*rỉ sét*).
- Mỗi khóa chỉ một mặt; không khóa nào trùng P1, L2A, L2B, L2C hay danh mục K/CHU.
- Cột: khóa, nguồn Wiktionary (en/vi), từ loại, HND, và 6 số đếm OPUS của tôi.
- Đây là **đề cử có chủ đích, không phải mẫu ngẫu nhiên**, giống L2. Tỉ lệ OK của nó không dùng để suy ra cho cả rổ L3.

Đề nghị quy trình, giống hệt L2:

1. Bạn dựng `l3-ung-vien.tsv` theo lược đồ L2 (thêm Leipzig/Tatoeba, `nguon_tu_dien`), cùng `l3-tap-luat-P2-v1.json` và sổ H5/H7.
2. Tôi chạy cổng độc lập; số đếm của tôi đã có sẵn.
3. Hai bên chấm đôi, qua H9 rồi P5/P6.

Bạn cứ thêm, bớt hay phản đối từng mục trước khi dựng bảng, ví dụ *dạ dày, bồn cầu, vết xước, bạn trai* có thể vướng H6. Với chừng này mục đời thường, tôi dự kiến cổng sau khi chấm cho dư 22.

Nếu bạn thấy L3 kiểu này vượt định nghĩa đã ký ("nguồn khác do hai bên đề xuất"), xin nói rõ. Khi đó ta dừng ở L2 và cùng trình chủ dự án hai phương án kèm số liệu: (a) mở L3 như trên; (b) cho dự phòng R1 thay suất OK.
