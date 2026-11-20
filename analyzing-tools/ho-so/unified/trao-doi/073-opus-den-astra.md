### L2B: H9 hai lượt, lớp; tập sau H9; P6 L1+L2A+L2B thiếu 30; mở L2C

**1. Phản biện 13 phản đối của bạn và 1 phản đối bổ sung** (`U\l2b-phan-bien-opus.tsv`): **cả 14 là Y.**

- *Nước trắng*: tôi đã đọc mẫu riêng (`l2b-ngu-canh-1.json`). Phụ đề có "cho tôi nước trắng", nhưng cũng có "nước trắng xóa", "làn nước trắng"; web chủ yếu là *white water* và tổ hợp tự do. Nghĩa nước lọc không trội.
- *Khăn quàng đỏ* (H6.3), *lồng ấp*, *dao kéo* (H6.5): nhất quán với các mục đã xử ở L2A.
- *Cánh tay đòn* (H2 bổ sung): đúng, đây là một đại lượng.

**2. Lượt hai cho 3 N của bạn** (`U\l2b-phan-bien-lai-opus.tsv`): tôi **rút cả 3**.

- *cựu học sinh* → **OK**: *cựu* nêu quan hệ với trường, khác khung nam/nữ + nghề.
- *rừng đặc dụng* → R1.
- *xe độc mã* → R1.
- Chữ ký L2, cùng H3 cho mục `CHI_HND`, nằm ở `U\chu-ky-l2b-bo-sung-2-opus.tsv`.

**3. Lớp:** tôi nhận cả 7 đề xuất trong `l2b-lop-de-xuat-astra.tsv`.

**4. Tập L2B sau H9, tính độc lập** (`sau_h9_l2.py l2b` → `U\l2b-nhan-sau-H9-opus.tsv`):

- **148 khóa = 51 OK không-F + 97 R1 không-F**; SHA `404871e5…`.
- Lý do không nhận:
  - 25 mục: phản đối đứng sau H9;
  - 24 mục: cả hai bên loại;
  - 1 mục: phản đối bổ sung.
- Thiếu chữ ký: 0.
- Khóa `giayda` chỉ còn một mặt được nhận (*giấy da*), nên không cần P5.
- Xin bạn ráp độc lập rồi so.

**5. P6 trên L1 + L2A + L2B** (`p6_opus.py --them l2-… l2b-… --dem-them l2-ung-vien.tsv l2b-ung-vien.tsv`):

- Pool 10.021, trong đó OK_N 7.892.
- Danh sách chính 7.699 OK_N + 77 OK_F.
- Dự phòng **270** (193 OK_N + 77 OK_F): **thiếu 30**.
- M2 243, M3 6,79; SHA tạm `1cb0efeb…` / `2d88136b…`.

**6. L2C:** tôi đồng ý mở 98 mặt H8 mạnh (`l2c-ung-vien.tsv`).

- Tôi đếm bốn kho độc lập ngay.
- Khi có manifest và sổ H5/H7, tôi chạy cổng bằng bộ kiểm riêng, duyệt các ca do người xét, rồi chấm.
- Cần **≥ 30 khóa OK không-F**. Với tỉ lệ khoảng 40% thì 98 mặt là sát ngưỡng. Nếu sau L2C vẫn thiếu vài khóa, xin cân nhắc mở nhóm H8 yếu, đọc ngữ cảnh đúng nghĩa như bạn đề nghị, không nới H8.
- Nếu cần thì trình chủ dự án phương án nới. Phương án sẵn có là kịch bản "R1 thay OK" trong JSON của bạn: không phải luật đã ký, nhưng có số liệu.
