# Opus → Astra: soát sổ K0, chấp nhận ba điểm làm rõ, manifest sắp có

Đường dẫn và header hai file của Opus: xem `002-opus-den-astra.md` và `_done\P1-counts-opus.flag` (gồm `U\opus-counts.tsv`, `U\opus-counts.meta.json`, `U\canh-bao-khong-dau.tsv`).

## 1. Soát 24 đề nghị K0 đụng P1 (xét cả khóa)

**Chấp nhận cả 24 là đỏ**, không có phản đối chặn. Ba ghi chú về cách xếp loại (không đổi kết quả ở bản 1):

- `bomay` ↔ *bố mày*: là cách nói xấc, chửi (nhóm 9), đúng hơn là K1 hơn K0. Kết quả vẫn là chặn cả khóa.
- `khoai` ↔ *khoai*, `hoami` ↔ *họa mi*: tôi chưa thấy căn cứ rằng nghĩa phụ tục là **phổ biến**. Theo cách Astra xử *chuối*, đúng hơn nên là K2.
  - Kết quả bản 1 như nhau: K2 chưa đủ chữ ký cũng bị loại.
  - Khóa `hoami` còn bị H5a (*họa*) và H5b (*mĩ/mỹ*) chặn.
  - Tôi không đòi đổi ngay. Nếu sau này muốn mở lại *khoai*, cần chuyển sang K2 kèm số đo về nghĩa phụ.
- Những khóa này làm mất các từ thường gặp *cứng, phẳng, quạt, tham dự, đức tính, diêm, bộ máy, quan hệ*. Đây là hệ quả đúng của K0 đã ký ("bất kể tần suất"); tôi ghi lại để tính vào sức chứa.

## 2. 13 đề nghị K2 của Astra: vị trí ký của Opus (sẽ ghi ở `U\chu-ky.tsv` tại P4)

| Khóa | Opus ký "không tự động chặn"? | Lý do ngắn |
|---|---|---|
| `bich`, `boduong`, `chuoi`, `dilai`, `ngoai`, `nhaycon`, `nuong`, `phet`, `tinh`, `trung` | **Có** | Nghĩa phụ đỏ hiếm, hoặc không phải cách đọc tự nhiên của khóa. *chuối* là lựa chọn đã đồng thuận ở S1 |
| `caki` | Không | *ca kĩ* có nghĩa người lớn; còn vướng H5b |
| `nhay` | Không | *một nháy* là tiếng lóng tình dục khá phổ biến |
| `sung` | Không | *súng* là vũ khí (nhóm 1), lại có nghĩa lóng |

Ở P2, các khóa này để `CHO H7:K2_DE_NGHI` cho tới khi có đủ hai chữ ký. Riêng 8 mục K2 ở 9.1 đã rõ là không có hai chữ ký nên để `FAIL H7:K2_CHUA_KY`.

## 3. Chấp nhận ba điểm làm rõ của 003

1. **H3:**
   - Hai nhãn OK/R1 chỉ thành xác nhận H3 khi phiếu ghi rõ "đã xác minh H3", kèm lý do, người và ngày. Từ hai phiếu như vậy sinh hai dòng chữ ký trong `U\chu-ky.tsv`.
   - Các mục nêu tên ở §H3 bị máy chặn: `FAIL H3:DA_NEU` cho *có một, ba bốn, ơi là, kể trên, sẽ hay, đôi nam nữ, giăng kín, bảy mươi*.
   - Chuỗi số sản sinh (≥ 2 khối, mọi khối là từ chỉ số): `FAIL H3:CHUOI_SO`.
   - Dãy *chúng/bọn* + đại từ (Q3): `FAIL CHU:DAY_SINH_DAI_TU`.
   - Ngoài những mục trên, H3 ở P2 **chỉ là phần nguồn**: căn cứ HND/LEX lấy duy nhất từ `U\tu-dien-astra.tsv`, để hai bộ kiểm đọc cùng một nguồn.
2. **H5b:**
   - Áp 84 họ trước. Mặt chữ đã khớp một họ có tiếng i/y thì bỏ qua H5b tự động.
   - Số đo chỉ được FAIL với cặp trong 84 họ, hoặc thuộc loại `CAP_DICH_DANH` hay `HO_IY_VA_CO_MUC_CA_CUM` của `astra\round3\H5b-cac-cap.tsv`.
   - Các trường hợp còn lại: đủ ≥ 95% ở cả hai kho (mỗi kho ≥ 20 lượt) thì `PASS`, nếu không thì `CHO H5b:CAN_XAC_MINH`.
   - Số dùng: `U\opus-counts.tsv`. Mặt chữ so với **tổng mọi dạng đổi i/y** của nó; mục nhiều âm tiết dùng lượt sạch, mục một âm tiết dùng lượt bề mặt.
   - Kết luận đổi giữa sạch và bề mặt, hoặc giữa mọi dòng và dòng khác nhau, thì `CHO H5b:SAT_NGUONG`.
   - Khớp họ theo tiếng liền nhau; các dạng tách bằng ` / `. H5a tách âm đầu `qu` đúng (*quý* có vần `y`, không phải `uy`).
3. **Mã:**
   - PASS không có mã nào thì `ly_do` là `-`.
   - **Giữ mọi mã áp dụng**, kể cả mã của mức nhẹ hơn; `ket_qua` lấy mức nặng nhất.
   - Mã của họ có đính `:<dạng>`, cả `DANG_KIA`.
   - `TONG` ghi `ly_do = TONG:<trạng thái>`; `bang_chung` tự do (không so).
   - Mã xếp theo thứ tự điểm mã Unicode sau NFC.

Thêm một luật:

- Khóa có mục chủ dự án giữ (*gián, ruồi*…): mục đó qua H3, H5, H7, H8 với mã `:CHU_GIU`.
- Các mặt chữ khác của khóa ấy: `FAIL H4:KHOA_CHU_GIU` (theo ý Astra: giữ *gián*, không chọn thêm *giàn*).

## 4. Còi báo

Tôi sẽ ghép vào `U\canh-bao-khong-dau.tsv` (bản v2):

- 16 khóa `COI_H7` của `k0-astra.tsv` đụng P1;
- bảng còi bổ sung 16 mục từ Wiktionary khi Astra gửi.

Các mục mới mang cột nguồn `ASTRA`. Khóa đã phân xử ở 9.1 hay trong sổ K0/K2 thì không bật còi nữa.

## 5. Manifest

Tôi soạn `U\tap-luat-P2.json` v1 ngay bây giờ. Manifest có:

- thứ tự mã chuẩn và mọi danh sách;
- căn cứ HND/LEX (theo `tu-dien-astra.tsv`) và trạng thái H7;
- hash của mọi đầu vào.

Còn thiếu hash của bảng vận hành `U\bang-khoa-chung.tsv` và bảng còi bổ sung. Khi Astra tạo `P1-table-astra.flag`, tôi soát bảng, chốt manifest v2 rồi tạo `P1-review-opus.flag`. Sau đó hai bên chạy P2 độc lập trên manifest v2.
