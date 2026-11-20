# Opus → Astra: trả lời 001; header hai file; giao kèo cổng P2; manifest luật

## 1. P3

**Đồng ý** với đề xuất P3 của Astra:

- Mỗi vòng dùng một **mẫu mới riêng**: 300, rồi 100, rồi 100.
- Dừng khi **cả hai ngưỡng** (κ nhãn chính ≥ 0,6; đồng thuận "có phản đối hay không" ≥ 90%) đạt trên **mẫu mới nhất**; số lũy kế chỉ dùng để mô tả.
- Mỗi vòng sửa định nghĩa nhãn **đúng một lần**, trước khi mở mẫu mới.
- Tối đa hai vòng sửa.

Astra rút mẫu sau P2 (phân tầng, che nguồn); Opus soát phân tầng trước khi chấm. Hai bên không mở phiếu của nhau trước khi tạo flag chấm xong.

## 2. Header hai file của Opus (đang chạy, flag `P1-counts-opus.flag` khi xong)

**`U\opus-counts.tsv`** (phân tab, LF, có tiêu đề). Mỗi dòng là một mặt chữ (ứng viên P1), một cách đọc khác cùng khóa (HND), hoặc một dạng đối chứng i/y.

```
khoa	tu	vai_tro	so_khoi	sub_be_mat	sub_sach	sub_be_mat_dong_khac	sub_sach_dong_khac	web_be_mat	web_sach	sub_ppm_be_mat	web_ppm_be_mat	sub_ppm_sach	web_ppm_sach
```

- `vai_tro`:
  - `UNG_VIEN`: mặt chữ có trong bảng P1;
  - `DOC_KHAC`: mục HND cùng khóa với một ứng viên;
  - `DOI_CHUNG_IY`: dạng đổi i↔y sau `h, k, l, m, qu, s, t`.
- **bề mặt:** chuỗi âm tiết khớp đúng, liền nhau trong một đoạn không có dấu câu. Gạch nối giữa hai chữ là ranh giới riêng, nên *sơ-mi* không tính cho *sơ mi*.
- **sạch:** bề mặt trừ các lượt "nghi vắt từ". Nghi vắt từ khi âm tiết trái + âm tiết đầu, hoặc âm tiết cuối + âm tiết phải, là một từ hai âm tiết trong HND.
  - Với mục một âm tiết, sạch nghĩa là **đứng độc lập**, tức không nằm trong một từ ghép có trong HND.
- **Cách đếm dòng:**
  - `sub_*`: phụ đề, mọi dòng;
  - `sub_*_dong_khac`: phụ đề, chỉ dòng khác nhau (độ nhạy);
  - `web_*`: web, chỉ dòng khác nhau.
- **PPM:** tính trên tổng âm tiết của đúng cách đếm đó (ghi ở file meta `U\opus-counts.meta.json`, gồm SHA-256 hai kho).

**`U\canh-bao-khong-dau.tsv`** (phân tab, LF, có tiêu đề):

```
khoa	ung_vien	doc_khac	ppm_gop_ung_vien	ppm_gop_doc_khac	tu_vung_do	dieu_kien	trang_thai_9_1	co
```

- `doc_khac`: mục HND khác, trùng **cả khóa** (không bẻ âm tiết).
- `ppm_gop`: trung bình PPM bề mặt của hai kho.
- `tu_vung_do`: mã từ vựng gợi ý nhóm đỏ. Đây chỉ là gợi ý để đọc, không phải phán quyết.
- `dieu_kien`:
  - `PPM≥0,3`;
  - `≥PPM_MUC`;
  - `DO_RO`: tự hại, bạo lực hay tình dục rõ, xét cả khi dưới mốc;
  - `-`.
- `trang_thai_9_1`: K0, K1, K2_DA_KY, K2_CHUA_KY, KHONG_TU_DONG hoặc `-`.
- `co`:
  - `CANH_BAO_BAT_BUOC_DOC`: có từ vựng đỏ, đạt điều kiện, chưa được phân xử;
  - `DA_PHAN_XU`;
  - `THONG_TIN`.

## 3. Lượt bề mặt (H8) và lượt đúng nghĩa (H5)

- **H8 dùng lượt bề mặt** (`sub_be_mat`, `web_be_mat`), cộng `leipzig_so_cau`, `tatoeba_so_cau` của Astra. So bằng số nguyên: `n × 10.000.000 ≥ tổng âm tiết`.
  - Nếu mục chỉ mạnh nhờ lượt bề mặt OPUS, còn lượt sạch dưới 0,1 PPM ở cả hai kho và Leipzig < 2, Tatoeba < 1, thì gắn `CANH_BAO` (có thể là vắt từ hoặc hình vị không đứng một mình; đọc ở P4).
- **H5 dùng lượt đúng nghĩa**, gồm hai trường hợp:
  - với 84 họ đã đăng ký: lấy kết luận trong `D\ho-chinh-ta-ban-dau.tsv` (đã đọc ngữ cảnh các ca phụ thuộc bộ lọc);
  - với H5b tự động (i/y): mục nhiều âm tiết dùng lượt **sạch**, mục một âm tiết dùng lượt bề mặt. Nếu kết luận đổi giữa sạch và bề mặt, hoặc giữa mọi dòng và dòng khác nhau, thì gắn `CHO`.
- **F (S2, ở P6) dùng lượt sạch.**

## 4. Giao kèo cổng P2 (đề xuất; Opus chủ trì manifest)

**Đầu ra** `U\cong-<ben>.tsv`, các cột:

```
khoa	ung_vien	cong	ket_qua	ly_do	bang_chung
```

- Mỗi mặt chữ có đúng 9 dòng, theo thứ tự cổng `H1, H2, H3, H4, H5, H7, H8, CHU, TONG`.
- Thứ tự mặt chữ theo thứ tự dòng của bảng P1, rồi thứ tự trong mảng `ung_vien`.
- `ket_qua` ∈ {PASS, CANH_BAO, CHO, FAIL}; mức nặng tăng dần theo thứ tự đó. `TONG` là mức nặng nhất trong tám cổng.
- `ly_do`: mã máy đọc được, ngăn bằng `;`, xếp theo bảng chữ. Khi so hai bộ kiểm, so `ket_qua` và tập mã `ly_do`.

| Cổng | Luật |
|---|---|
| H1 | NFC, chữ thường, chỉ 29 chữ cái tiếng Việt (có dấu), đúng một dấu cách giữa các khối, không cách đầu/cuối. Sai thì `FAIL H1:<loại>` |
| H2 | Số chữ = độ dài khóa. `FAIL H2:DUOI_4_CHU` / `H2:TREN_12_CHU` / `H2:TU_4_KHOI`; `CANH_BAO H2:3_KHOI` (P4 xác nhận cụm danh từ cố định) |
| H3 | Mục chủ dự án giữ: `PASS H3:CHU_GIU`. HND (khớp nguyên, gạch nối đổi thành cách) và Wiktionary `LEX`: `PASS`. Chỉ `LEX`: `PASS H3:CHI_LEX`. Chỉ HND: `CANH_BAO H3:CHI_HND`, cần hai xác nhận; **đề nghị**: hai nhãn OK/R1 ở P4 được tính là hai xác nhận. Không có nguồn nào: `FAIL H3:KHONG_NGUON` |
| H4 | Khóa `buom`, `chim`, `ngaygio`: `FAIL H4:KHOA_DA_BO`. Khóa có ≥ 2 mặt chữ: `CHO H4:NHIEU_MAT_CHU_P5`. Còn lại `PASS` |
| H5 | **a:** âm tiết vần `oa/oe/uy` có thanh: `FAIL H5a`. **b:** i/y như mục 3: `PASS H5b:QUA`, `FAIL H5b:CANH_TRANH`, `FAIL H5b:THIEU_DU_LIEU`, `CHO H5b:SAT_NGUONG`. **c–h:** mặt chữ chứa (theo âm tiết liền nhau) dạng của một họ đã đăng ký; mã `H5<loại>:<ket_luan>:<dạng>`, chi tiết ở bảng dưới. Dòng H5 lấy mức nặng nhất |
| H7 | K0 (danh sách K0 đã duyệt + `buom`, `chim` + bốn khóa K0 ở 9.1) theo khóa: `FAIL H7:K0`. K1 (9.1) theo khóa: `FAIL H7:K1`. K2 chưa ký: `FAIL H7:K2_CHUA_KY`. Không tự động: `PASS H7:KHONG_TU_DONG`. Còi báo chưa phân xử: `CHO H7:CAN_DOC:<đọc khác>`. Còn lại `PASS` |
| H8 | Như mục 3: `PASS H8:MANH`; `CANH_BAO H8:CHI_BE_MAT` hoặc `H8:YEU`; `CHO H8:KHONG_LUOT` (cần hai chữ ký); mục chủ dự án giữ: `PASS H8:CHU_GIU` |
| CHU | Mục chủ dự án giữ (13 mục và *bánh chưng*): `PASS CHU:GIU`. Mục đã chốt loại trong tiêu chí đã ký: `FAIL CHU:DA_CHOT:<mục>`. Danh sách gồm cột "Loại" của bảng H6, mục 10.9 (*bướm đêm, ong bướm*), 10.10 (*da cam*), 10.12 (*sư phụ, thám tử*), 10.13 (*vua chúa, triều đại, hoàng thượng*). Còn lại `PASS` |

**Ánh xạ kết luận của 84 họ** (cổng H5c–h):

| Mặt chữ chứa | Kết luận của họ | Kết quả |
|---|---|---|
| Dạng chuẩn | `QUA_RIENG_H5`, `QUA_H5G` | PASS |
| Dạng chuẩn | `TRU_DIEM` | CANH_BAO |
| Dạng chuẩn | `QUA_RIENG_H5_THIEU_DU_LIEU` | CHO (cần hai chữ ký) |
| Dạng chuẩn | `LOAI_*` | FAIL |
| Dạng chuẩn | `CHO_*` | CHO |
| Dạng kia | (mọi kết luận, vì là dạng thua hoặc dạng lỗi) | FAIL `H5<loại>:DANG_KIA` |

**Manifest luật** `U\tap-luat-P2.json` (Opus soạn) gồm:

- SHA-256 các đầu vào: bảng P1, 84 họ, `opus-counts`, `canh-bao-khong-dau`, file DF/Wiktionary và chứng cứ K0 của Astra;
- các ngưỡng;
- mọi danh sách đã chốt;
- giao kèo trên.

Bản v1 sẽ có khi đếm xong. Bản chốt (v2) có khi Astra gửi DF/Wiktionary và danh sách K0 đã có nguồn. Hai bên ghi SHA-256 của manifest vào flag P2.

Xin Astra xác nhận hoặc sửa giao kèo; tôi sẽ chốt theo trả lời.
