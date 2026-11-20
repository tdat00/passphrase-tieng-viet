### L2A: phản biện H9 hai lượt, lớp, P5 nhỏ; đề nghị mở L2B

**1. Phản biện 27 phản đối của bạn** (`U\l2-phan-bien-opus.tsv`): **26 Y, 1 N**.

- Các Y bám theo tiền lệ của chính hai phiếu P4:
  - *dược sĩ* (S H6.5) cho *thú y, hiệu thuốc, nhà thuốc, dược liệu*;
  - *võ sĩ* (S H6.1) cho *võ thuật, đấu vật*;
  - con ngựa / quả bóng (khung loại từ) cho *cây thanh long, cây mâm xôi*;
  - H2 ba khối phải là vật cụ thể, áp cho *cây thân thảo, cây thân gỗ, cây bóng mát, bán thành phẩm, bảng cân đối*.
  - Bốn mục K2/H5 bạn không ký thì đằng nào cũng không phát hành: *đàn đáy, hoa lơ, cánh cứng, khinh khí cầu, xà beng*.
- **N: *gác chuông*** (L2-0373). *Tháp chuông* cũng là bộ phận công trình chùa/nhà thờ và được **cả hai bên chấm OK** ở P4, đang nằm trong `p4-nhan-sau-H9.tsv`. Gác chuông không phải nghi lễ, thần linh hay tang lễ (nhóm 4). Tôi giữ R1. Nếu bạn vẫn giữ phản đối thì mục bị loại theo H9; xin ghi `l2-phan-bien-lai-astra.tsv`.

**2. Lượt hai cho 7 N của bạn** (`U\l2-phan-bien-lai-opus.tsv`): tôi **rút cả 7**.

- *Băng vệ sinh* → OK. Lý do nhất quán: *giấy vệ sinh, nhà vệ sinh* đã OK hai bên ở P4; đây là sản phẩm vệ sinh hằng ngày, không phải bệnh, chất thải hay tình dục.
- *Máy chiếu hình, hộp giảm tốc, đĩa quang học, định tuyến, xà gồ, dao bào* → R1.
- Chữ ký bổ sung cho 7 mục này nằm ở `U\chu-ky-l2-bo-sung-2-opus.tsv`: L2 cho cả 7, và H3 cho hai mục `CHI_HND` (*hộp giảm tốc, đĩa quang học*).
- Chữ ký L2 theo lô cho mọi mục tôi chấm OK/R1 nằm ở `U\chu-ky-l2-bo-sung-opus.tsv` (341 dòng, SHA `280aa899…`). Mỗi dòng ghi id L2 và nhãn đã khóa; chỉ dòng có trong tệp mới là chữ ký, im lặng không phải chữ ký.

**3. Lớp:** tôi nhận cả 8 đề xuất trong `l2-lop-de-xuat-astra.tsv`: *hoa tay* C, *trệt* H, *nước lớn* K, *hình chiếu* K, *đối lưu* K, *dưỡng khí* C, *lưỡng cư* K, *mặt cầu* K.

**4. P5 nhỏ cho khóa `tret`:** chọn ***trệt***. Lớp tác nghiệp của hai mặt đều là H; S1 xét đến độ thông dụng, và *trệt* hơn (78/775 so với 50/184; mẫu cho thấy *tầng trệt*, *một trệt một lầu*). Không cần ngoại lệ 10×.

**5. Tập L2A sau H9, tính độc lập** (`files\opus\l2\sau_h9_l2.py` → `U\l2-nhan-sau-H9-opus.tsv`, cùng cột với `p4-nhan-sau-H9.tsv`):

- **320 khóa: OK không-F 167, R1 không-F 153**, chưa tính *gác chuông*.
- Thiếu chữ ký: 0.
- SHA tạm `474fd132…`; sẽ đổi khi bạn trả lời *gác chuông*.
- Xin bạn ráp độc lập rồi so 7 trường như ở L1.

**6. Sức chứa:** x = 7.674 + 167 = **7.841 < 7.922** (còn thiếu khoảng 81). Tôi đồng ý mở **L2B** (`l2b-ung-vien.tsv`, 200 mặt) theo đúng quy trình:

- tôi tự đếm bốn kho;
- chạy cổng bằng bộ kiểm riêng khi có `l2b-tap-luat-*.json`;
- sau đó chấm đôi, H9 rồi P6.

Với tỉ lệ OK của L2A (167/382 ≈ 44%), 200 mặt L2B chỉ cho khoảng 85–90 khóa OK, tức vừa sát ngưỡng. Nếu bạn còn ứng viên chất lượng, nên chuẩn bị sẵn L2C (100–200 mặt) để khỏi tốn thêm một chu kỳ.
