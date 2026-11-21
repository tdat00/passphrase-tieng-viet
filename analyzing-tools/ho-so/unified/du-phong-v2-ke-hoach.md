# Dự phòng v2 — kế hoạch cập nhật tài liệu, bản sửa 1

Status: Draft (round 1)

**Authors:** SA-Astra (người soạn), SA-Opus (người review).
**Date:** 2026-11-20.
**Base commit:** `cefb99386d4845e40bc2d3eabc7d6898d078305d`.
**Sign-off:** SA-Opus accept ở Lượt duyệt 2 (`O\round-1-review-drafts.md`); SA-Astra nhận cập nhật §D và ghi T-dpv2-9. Hai SA đã thống nhất tầng/trạng thái và N. Giữ Status Draft theo yêu cầu, chưa phải lệnh triển khai, Final hoặc phê duyệt thay chính.

`AT = analyzing-tools`; `U = AT\ho-so\unified`; `A = AT\ho-so\astra\du-phong-v2`; `O = AT\ho-so\opus\du-phong-v2`; `E = A\evidence`. `verified` chỉ sự kiện đã đối chiếu; `assumed/proposed` chỉ đề nghị chưa được chốt. Dấu `/` trong liên kết Markdown là URL; các đường dẫn/lệnh Windows dùng `\`.

## 1. Mục tiêu

Lời chủ ngày 20/11/2026:

> giao agent SA-OPUS và SA-ASTRA phân tích tiếp 205 từ dự phòng trong WordListAnalyze.md, ngoài ra có thể thêm vào 1 số từ "honorable mentioned" là những từ "có thể" xem xét thêm vào list

Theo câu trả lời thiết lập phạm vi: chỉ phân tích/phân loại; danh sách chính 7.776 từ không đổi; khoảng 100–300 honorable mentions; không tạo docs mới, kết quả cuối cập nhật trực tiếp tài liệu hiện có.

**Kết quả cần có:** người bảo trì phân biệt được đầu mục, ngăn thay, cổng còn việc, trạng thái câu/D8 và điều kiện của đề cử; không nhầm một từ có mặt trong TSV với một từ đã được phép phát hành.

## 2. Phạm vi

### Trong phạm vi khi kế hoạch đã Final

- Sửa gạch đầu dòng dự phòng/thêm HM và mục lục của `WordListAnalyze.md`.
- Thay phần trình bày hiện hành §11; thêm §12; giữ nguyên nội dung lịch sử §3, §5–9.
- Giữ nguyên `AT\du-phong.txt`; thêm `AT\du-phong-phan-loai.tsv` và `AT\honorable-mentions.tsv`.
- Cập nhật các hàng/mục liên quan trong `AT\README.md` và metadata/hash của `AT\manifest.json`.
- Lưu chứng cứ và chữ ký trong hồ sơ hiện có; không thêm thư mục docs.

### Ngoài phạm vi

- **Mọi byte** của `index.html`, `thong-tin.html`, `AT\wordlist.txt` và toàn §10.
- `labels.tsv`, `nguon-goc-giai-nghia.tsv`, `blocked_keys.tsv`, `spelling_families.tsv`, tập luật, công cụ phát hành, code/test ứng dụng.
- Viết nghĩa mới, viết lại nghĩa, mở ngoại lệ D7, tự nâng R1, thay từ chính, đổi S4/TT2 hay quota, cam kết đủ 300 dự phòng.
- Tải/lưu corpus hoặc định nghĩa; chuẩn hóa checkout nguồn chính; commit/push/merge bởi SA.
- Các câu trạng thái có ngày 20/11/2026 về 205 dự phòng trong `WordListAnalyze-Opus.md:265`, `WordListAnalyze-Astra.md:95` và quyết định 10 tại `WordListAnalyze.md:153`: giữ nguyên như lịch sử; trạng thái hiện hành về sau đọc ở §11 mới.

**Giới hạn của bước đang thực hiện:** chỉ ghi năm tệp `U\du-phong-v2-*` được giao và thư mục Astra. Chưa thực hiện các thay đổi tài liệu hiện hành nêu trên.

## 3. Hiện trạng chuẩn để dựng

**verified:**

| Dữ liệu | Giá trị |
|---|---|
| Chính | 7.776, 7.699 OK không-F + 77 OK-F, R1 = 0 |
| Dự phòng gốc | 205: H85/K43/F77; 128 không-F + 77 F |
| Nghĩa dự phòng | 168 câu đạt lịch sử, 37 chưa viết; D8 = 0 |
| H8 dự phòng | 198 MANH, 4 YEU, 2 CHI_BE_MAT, 1 KHONG_LUOT |
| Mẫu số H8 P2 | phụ đề mọi dòng 34.329.387; phụ đề dòng khác nhau 27.978.808; web dòng khác nhau 150.070.912 |
| Mốc sau đóng 11 lệch cũ | A149/B36/C14/D6; chưa tính ca H7 mới |
| Tầng hiện tại | A148/B36/C15/D6; 0 CHO_HOA; ngoại trừ C/CHO_H7 chưa được dùng |
| HM hồ sơ | 285 = 122 D6 + 10 D7 + 107 R1 + 46 L3b |
| HM được tính | **N=237**: 120 D6 + 10 D7 + 107 R1; 48 dòng ngoài N, không còn tranh chấp HM |

`CHI_BE_MAT` không được gộp vào MANH hoặc xóa thành một nhãn YEU chung khi xuất mã P2. Mã cổng lịch sử có cảnh báo phải được đọc cùng hồ sơ P4/chữ ký, không tự coi là phản đối H9 mới.

Nguồn: `U\tap-luat-P2-v4.json`, hai `cong-*-v4.tsv`, các nhãn/counts và `E\joint-summary.json`. Mọi dòng lịch sử trong hai bảng đã được tính lại mã H8 khớp nguồn; *thụp* và các mục L2/L3 dùng hồ sơ lô đúng nguồn.

### Các byte/SHA cần bảo vệ

“Toàn §10” là khoảng byte từ đầu dòng `## 10. Danh sách 7.776 từ phát hành` đến ngay trước đầu dòng `## 11.`; gồm tiêu đề, hàng rào và các dòng trống trong khoảng đó.

| Vùng | SHA-256 byte của checkout hiện tại |
|---|---|
| `index.html` | `01b76617f8df57d80e59d0989001ced8f7714ae95e85828b351bce2a5517a423` |
| `thong-tin.html` | `8ec3bbf763f2465994bde4239079a3795eb2eb3bf21f61fe29aa683cb8bf3ea7` |
| `AT\wordlist.txt` | `8945fd4a732b210b4e027f6660b4f42d53b2344088028f967e01a30af7bbc6b4` |
| Toàn §10 | `4b91fac689e70ccb0715b92b49efe4305fbb19c3bc90dd449e72fba72889f6fa` |

Thân `wordlist.txt` LF trong Git có SHA `1d4fc3e803c4cb40ee39f3abe25fccd7815f1e750198b4b1fc1166753233f581`; cột từ có SHA `3609c88ff436708857ac323189f81b5bb9b31d31ea6f0a8924cc02bc61c0e713`. Không đánh tráo SHA byte checkout và SHA LF.

Hai tài liệu lưu trữ nêu trong phạm vi cũng phải nguyên byte; hash trước/sau ghi ở `E\revision-1-audit.json` và `E\joint-proof.json`.

## 4. Thiết kế dữ liệu

### 4.1. Hai bảng nháp trong hồ sơ

1. `U\du-phong-v2-phan-loai.tsv`: **205 dòng**, thứ tự/cột từ đúng `AT\du-phong.txt`.
2. `U\du-phong-v2-honorable-mentions.tsv`: **285 dòng hồ sơ**, O1. Chỉ dòng `CUNG_DE_CU_CHUA_PHAT_HANH` tính vào N=237; 46 dòng `NGOAI_HM_CHUA_THAM_DINH`, một `NGOAI_HM_CHO_H5` và một `LOAI_K1` không tính. Không xóa dấu vết quyết định loại/giữ ngoài.

Schema được đóng trong `E\joint-build.py`:

- Dự phòng, 23 cột:

```text
tu	khoa	lop	ngan	tang_opus	tang_astra	tang_chung	tranh_chap	ma_van_de	cau_hoi	trang_thai_h	giai_nghia	luot_viet	sha256_giai_nghia	h8	F	diem	thay_duoc	con_thieu	y_kien_opus	y_kien_astra	bang_chung	xac_minh
```

- HM, 27 cột:

```text
tu	khoa	nhom	nhan_ho_so	lop	xac_minh_lop	de_cu_opus	de_cu_astra	ket_luan_nhap	tranh_chap	cau_hoi	trang_thai_h	ngan_du_kien	h8	sub_sach	web_sach	leipzig	tatoeba	F	diem	nguon	ly_do_chua_chon	dieu_kien	y_kien_opus	y_kien_astra	bang_chung	xac_minh
```

`tranh_chap=KHONG` không có nghĩa đã phát hành hoặc đã khép mọi cổng. Ngoại trừ đã được hai SA chốt C/CHO_H7, `cau_hoi=-`; giữ nguyên việc đo nghĩa/ký mức K trước khi dùng. Không còn dòng CHO_HOA.

### 4.2. Hai bảng công bố ở AT sau khi chốt

Tách bảng công bố gọn khỏi các cột trao đổi nội bộ, nhưng giữ số liệu và pointer, đặc biệt trạng thái CHO_H7 và điều kiện chưa được dùng của ngoại trừ.

**`AT\du-phong-phan-loai.tsv`: 205 dòng, 17 cột**

```text
tu	khoa	lop	ngan	tang	trang_thai_h	ma_van_de	giai_nghia	luot_viet	sha256_giai_nghia	h8	F	diem	thay_duoc	con_thieu	ghi_chu	bang_chung
```

- `tang` lấy kết luận chung đã ký, không còn CHO_HOA.
- `ghi_chu` là lý do được chốt khi đóng từng câu hỏi; không tự lấy một phía chỉ để lấp ô.
- Mục D vẫn có dòng; `thay_duoc` phải giải thích **khả năng ngăn chỉ có ý nghĩa khi đủ cổng**, không làm D thành dùng được.
- `giai_nghia` tách khỏi tầng: CO_PASS_LICH_SU/CHUA_VIET. *Trở lên* ở C vẫn chưa viết.
- `sha256_giai_nghia` băm câu nguyên văn UTF-8, không nhầm với hash JSON-token của D6; bản token-hash/đúng lượt nằm ở hồ sơ chi tiết.

**`AT\honorable-mentions.tsv`: 237 dòng, 20 cột**

```text
tu	khoa	nhom	nhan_ho_so	lop	xac_minh_lop	trang_thai_h	ngan_du_kien	h8	sub_sach	web_sach	leipzig	tatoeba	F	diem	nguon	ly_do_chua_chon	dieu_kien	ghi_chu	bang_chung
```

N đã chốt phạm vi đề cử sau khi Astra nhận phương án 1 của Q-dpv2-6 và đồng ký K2. Lọc đúng trạng thái, không đếm mọi dòng hồ sơ:

```text
N = count(ket_luan_nhap == "CUNG_DE_CU_CHUA_PHAT_HANH")
  = 230 + 1 (tần số, K2 đủ hai chữ ký) + 6 (đề cử có cờ rà H6)
  = 120 D6_CUOI + 10 D7_CUOI + 107 R1
  = 237.
```

- Q-dpv2-4 đã chốt phương án 2: 46 L3b và chạng vạng ở hồ sơ/§12.3, không tính. Bao tử là K1, không tính cả khóa baotu.
- Bảng công bố chỉ chứa 237 dòng được tính. Điều kiện về nghĩa, R1, H6 trước khi dùng vẫn phải giữ; N không phải số ghế thay được.
- Không tự tìm thêm/bớt đầu mục để đạt con số khác. Nếu có phát hiện cổng mới trước Final, phải ghi nhận và chốt lại thay đổi, không sửa âm thầm.
- Giờ cao điểm: hai SA nhận phản đối H2; mục ở lại hồ sơ L3b. Không dùng nhãn có điều kiện để né luật.

**Định dạng chung:** UTF-8 không BOM, có tiêu đề, NFC đầu mục, không khoảng trắng cuối dòng, có dòng cuối. Dùng CRLF trong checkout Windows như các TSV hiện có, LF trong Git. Ô chưa có/không áp dụng ghi `-`, không đổi thành số 0. Không có cột giải nghĩa hoặc trích đoạn nguồn.

### 4.3. du-phong.txt và các bảng nền

- Giữ nguyên byte và 205 dòng một-từ-mỗi-dòng của `AT\du-phong.txt`; không tiêu đề, nhãn, chú thích hay khoảng trống mới.
- SHA LF vẫn `f015e718d03bc8cae4bcb0ab0014c813a02e918c1386075aff796e94189e098b`.
- Không thêm HM vào `du-phong.txt`; không xóa D khỏi ảnh chụp lịch sử.
- Không sửa nhãn/cờ/phả hệ nghĩa dùng cho bản phát hành. Họ H5/còi H7 mới được ghi trong phân tích và trạng thái, không lén đưa vào bảng checker rồi sửa chính để chữa lỗi.

## 5. Chỉnh sửa WordListAnalyze.md — văn bản/thuật toán chính xác

Các mẫu đã cập nhật quyết định về C/H7 và HM. Token viết hoa là vùng sinh tất định, không phải chỗ người triển khai tự quyết. Mẫu máy đọc: `E\joint-publication-text.json`.

### 5.1. Gạch đầu dòng hiện hành và mục lục

Thay duy nhất dòng bắt đầu `> - **Dự phòng:**` bằng:

```markdown
> - **Dự phòng:** giữ nguyên 205 từ để đối chiếu lịch sử, đã phân loại tại [mục 11](#11-danh-sách-dự-phòng-đã-phân-tích-chưa-phát-hành) và [bảng phân loại](analyzing-tools/du-phong-phan-loai.tsv). 168 mục có câu đạt D6/D7 trong hồ sơ, 37 mục chưa viết; trạng thái nghĩa không thay thế các cổng chọn từ. Tầng A/B/C/D không cấp quyền thay vào danh sách chính.
> - **Từ có thể cân nhắc:** 237 từ, xem [mục 12](#12-từ-có-thể-cân-nhắc-honorable-mentions) và [honorable-mentions.tsv](analyzing-tools/honorable-mentions.tsv); đây không phải dự phòng hay danh sách phát hành.
```

Thay dòng 11 của mục lục bằng đúng hai dòng:

```markdown
11. [Danh sách dự phòng (đã phân tích, chưa phát hành)](#11-danh-sách-dự-phòng-đã-phân-tích-chưa-phát-hành)
12. [Từ có thể cân nhắc (honorable mentions)](#12-từ-có-thể-cân-nhắc-honorable-mentions)
```

Không đổi các gạch về 7.776 từ/giải nghĩa, số liệu lịch sử hoặc quyết định 10. Không chèn bản sao tiêu đề §10 trước khối thật, vì checker tìm chuỗi tiêu đề đó.

### 5.2. Thay từ đầu §11 cũ đến EOF bằng mẫu §11–12

Giữ nguyên mọi byte trước đầu tiêu đề §11; riêng hai chỉnh sửa header/TOC ở trước §10 thực hiện theo §5.1. Không chèn anchor/ghi chú giữa cuối §10 và đầu §11. Anchor tương thích cũ nằm **sau** tiêu đề mới, như dưới đây.

````markdown
## 11. Danh sách dự phòng (đã phân tích, chưa phát hành)

<a id="11-danh-sách-dự-phòng-chưa-phân-tích"></a>

### 11.1. Trạng thái và phạm vi

**Trạng thái: đã phân tích, chưa phát hành.** Tập đối chiếu vẫn gồm 205 từ; đây không phải 205 gói thay thế đã được duyệt. Quyết định 10 ghi trạng thái ban đầu; yêu cầu phân tích ngày 20/11/2026 của chủ (D-dpv2-1) là căn cứ cập nhật trạng thái hiện hành. Danh sách chính 7.776 từ không đổi. Danh sách và SHA cột từ dự phòng vẫn giữ nguyên: `f015e718d03bc8cae4bcb0ab0014c813a02e918c1386075aff796e94189e098b`.

### 11.2. Các tầng và cảnh báo

A: hồ sơ ưu tiên chuẩn bị thay. B: còn thiếu câu giải nghĩa. C: cần thận trọng hoặc còn việc kiểm riêng. D: không dùng theo kết luận cổng/H9 đã ghi. Đọc cả cột trạng thái cổng và việc còn thiếu; tầng không thay nhãn OK/R1, không sửa S4 và không tự cấp quyền thay từ.

{{BANG_TANG}}

Chi tiết từng từ và căn cứ nằm trong [bảng phân loại](analyzing-tools/du-phong-phan-loai.tsv).

{{BANG_CANH_BAO}}

### 11.3. Ngăn hạn mức và quy tắc thay thế

Danh sách chính có 7.699 OK không-F và 77 OK-F, không có R1. Khi Q3 đang đầy, OK-F chỉ thay ghế F. OK không-F có thể thay ghế C/H/K hoặc F mà không tăng Q3. Dự phòng R1 chỉ thay R1; trần Q2 không cho mượn ghế OK. Không tự suy số từ có câu hoặc số dòng dự phòng thành số ghế đã đủ mọi điều kiện.

### 11.4. Giải nghĩa, chữ ký và việc còn thiếu

Trong tập 205 ban đầu, 168 mục có câu đạt D6/D7 lịch sử (123 v1, 35 v2, 10 v3), 37 mục chưa có câu đều thuộc F. Chưa có dòng D8 cho các mục dự phòng. Không gọi kết quả đối chiếu hash lịch sử là lần chạy D6 mới.

Mã H8 theo tập luật P2 v4.1: 198 MANH, 4 YEU, 2 CHI_BE_MAT, 1 KHONG_LUOT. Cả nghĩ và tối mù là CHI_BE_MAT; ăn nhịp có ngoại lệ không-lượt đã ký. Các mã cảnh báo của P2 phải đi cùng hồ sơ đọc kiểm/chữ ký P4, không tự chuyển thành PASS. Mẫu số P2 là 34.329.387 âm tiết phụ đề và 150.070.912 âm tiết web.

Khảo sát PPM gộp H7 trong hồ sơ này dùng mẫu số mục 0 của tiêu chí/manifest (34.314.528/149.860.716); nhãn H8 vẫn dùng P2. Các phép đo phải ghi rõ mẫu số, không trộn hai bộ.

Trước mỗi lần thay thật: kiểm lại H1–H9, ngăn và S4, câu sạch đúng lượt, D2/D5 trên toàn bộ tập thay, D6 với đủ tham chiếu, D7, D8 và các cổng phát hành. Không dùng mục D hoặc mục còn cổng chưa khép. Việc viết nghĩa mới và thay danh sách chính không thuộc lần phân tích này.

### 11.5. Danh sách 205 từ

```text
{{DU_PHONG_205}}
```

## 12. Từ có thể cân nhắc (honorable mentions)

### 12.1. Ý nghĩa và giới hạn

Đây là danh mục để xem xét, không phải dự phòng và không phải danh sách phát hành. Không tái sử dụng câu giải nghĩa đã bị loại, không tự nâng R1 thành OK, không coi đầu mục chưa thẩm định là đã qua luật cứng. Trạng thái của từng nhóm được ghi riêng.

Danh mục này chỉ tính các đầu mục có hồ sơ thẩm định từ đã được chốt. Các nguồn chưa hoàn tất nằm ở hồ sơ nghiên cứu, không tính vào số HM.

### 12.2. Danh mục và nguyên nhân chưa được chọn

{{BANG_NHOM_HM}}

Số đo, lớp, nguồn và điều kiện theo từng từ nằm ở [honorable-mentions.tsv](analyzing-tools/honorable-mentions.tsv). F là điểm thông dụng lịch sử, khác với lớp F; dấu `-` là chưa có hoặc không áp dụng, không phải số 0.

{{BANG_TU_HM}}

### 12.3. Các việc để sau

L2D và các ý tưởng ngoài pool chưa đủ chứng cứ chỉ lưu ở hồ sơ, không tính là từ đã qua cổng. Không tính vào N: lô L3b (48 ứng viên đã chuẩn bị ở [l3b-de-cu-opus.tsv](analyzing-tools/ho-so/unified/l3b-de-cu-opus.tsv), chưa qua P2/P4/H9); *chạng vạng* (chờ xác nhận và đo họ H5 với *choạng vạng*); *bao tử* (K1: khóa `baotu` đọc thành *báo tử*).

Nếu muốn khôi phục một mục từng bị loại ở P7, phải kiểm lịch sử lượt của đúng mục và quyền giao lượt sạch mới trước. Nếu muốn dùng một mục R1, phải tuân thủ P6/Q và quyết định cho danh sách tương ứng. Các bước đó không được mở tự động bởi việc đưa tên vào tài liệu.
````

**Lưu ý so khớp mẫu:** `joint-build.py --prove` yêu cầu sáu mẫu văn bản trong kế hoạch khớp mẫu máy ở `joint-publication-text.json`. Trước Final, hai SA khóa lại đồng bộ khi đáp án làm đổi văn bản.

**Thay token tất định:**

| Token | Nguồn và quy tắc |
|---|---|
| BANG_TANG | GROUP BY `tang, ngan` trên 205 dòng cuối; cột tầng/OK không-F/OK-F/tổng; tổng 205. Không có CHO_HOA khi công bố |
| BANG_CANH_BAO | Các mục C/D hoặc `trang_thai_h` còn việc riêng, O1; cột từ/tầng/mã vấn đề/việc thiếu/nguồn. Không viết giải nghĩa |
| DU_PHONG_205 | Cột từ nguyên trạng của `AT\du-phong.txt`, đúng 205 dòng, không thêm/sửa |
| BANG_NHOM_HM | GROUP BY `nhom,trang_thai_h` của N mục cuối; ghi rõ N, không dùng 285 nháp thay N |
| BANG_TU_HM | N dòng O1: từ/nhóm/lớp/trạng thái/điều kiện còn lại, link tới TSV; không có cờ tranh chấp chưa chốt |

Chính sách HM và đoạn §12.3 đã cố định theo T-dpv2-6/7; không còn nhánh HM chưa thẩm định. Bảng tầng/cảnh báo lấy kết luận chung, gồm ngoại trừ C/CHO_H7 theo T-dpv2-9.

## 6. README: đúng hàng và đúng mục thêm

Thay hàng du-phong.txt hiện tại bằng hàng đầu, chèn hai hàng tiếp theo ngay sau:

```markdown
| [`du-phong.txt`](du-phong.txt) | Giữ nguyên 205 từ để đối chiếu lịch sử; đã có bảng phân loại riêng, chưa phát hành và không phải 205 gói thay thế đã được duyệt |
| [`du-phong-phan-loai.tsv`](du-phong-phan-loai.tsv) | Một dòng cho mỗi từ dự phòng: tầng, ngăn, cảnh báo H, trạng thái nghĩa, mã H8, việc còn thiếu và nguồn chứng cứ |
| [`honorable-mentions.tsv`](honorable-mentions.tsv) | 237 từ có thể cân nhắc đã chốt phạm vi đề cử; không phải dự phòng, không tự cấp quyền thay từ hoặc viết thêm nghĩa |
```

Chèn trước `## Cập nhật danh sách`:

```markdown
## Dự phòng và từ có thể cân nhắc

Đọc `du-phong-phan-loai.tsv` cùng `du-phong.txt`; không thay từ chỉ dựa vào thứ tự dòng hoặc tầng A. Tầng không thay nhãn OK/R1 và không sửa S4. Mục D hoặc cổng chưa khép không được dùng. R1 không tự thay ghế OK; lớp F không được vượt 77.

Mã H8 lấy từ tập luật P2 v4.1 và kết quả hai bộ cổng đã đối chiếu, gồm cả CHI_BE_MAT. Điểm F, số đếm và mức H8 là ba dữ liệu khác nhau. Mẫu số P2 là 34.329.387/150.070.912 âm tiết phụ đề/web; không sửa ngược metadata nguồn lịch sử để làm chúng giống nhau.

Khảo sát PPM gộp H7 trong hồ sơ này dùng mẫu số mục 0 của tiêu chí/manifest (34.314.528/149.860.716); nhãn H8 vẫn dùng P2. Các phép đo phải ghi rõ mẫu số, không trộn hai bộ.

Từ có thể cân nhắc chỉ là đề cử; cột trạng thái nêu rõ hồ sơ nào chưa hoàn tất. Phân tích này không thay danh sách chính, không viết câu mới và không tự hoàn tất D8.

### Kiểm trên checkout Windows

Nguồn chuẩn trong Git dùng LF. Checkout CRLF có thể làm check_wordlist.py báo C1 và verify.mjs báo C1/C8; đó không phải native PASS. Kiểm đối chứng đúng nội dung LF hoặc trong môi trường giữ LF, đồng thời lưu kết quả kiểm byte của vùng được bảo vệ. Không sửa nguồn chính hoặc nới checker chỉ để làm mất lỗi nền trong tác vụ phân tích.
```

Không sửa quy trình thay danh sách thành A→C hoặc tự mở lô nghĩa. Không sửa hướng dẫn/tiêu chí đã ký.

## 7. Manifest: trường thay, trường giữ, cách băm

**Giữ nguyên** `danh_sach`, `du_phong.so_tu=205`, `du_phong.du_phong_txt_sha256`, mọi metadata nguồn/lịch sử D6, hash các tệp không đổi. Không ghi lại một lần D6 mới chỉ vì đối chiếu hash lịch sử.

**Thay/thêm khi có dữ liệu cuối:**

```text
du_phong.trang_thai = "đã phân tích, chưa phát hành"
du_phong.phan_loai_tsv = "du-phong-phan-loai.tsv"
du_phong.phan_loai_tsv_sha256 = SHA256(LF(public reserve TSV))
du_phong.tang = {A:a, B:b, C:c, D:d}   # tổng 205, số đã chốt
du_phong.giai_nghia_lich_su = {co_cau_dat:168, chua_viet:37, d8_du_phong:0}
du_phong.h8 = {MANH:198, YEU:4, CHI_BE_MAT:2, KHONG_LUOT:1}

honorable_mentions = {
  so_tu:237,
  trang_thai:"đề cử, chưa phát hành",
  tep:"honorable-mentions.tsv",
  sha256:SHA256(LF(public HM TSV)),
  nhom:{D6_CUOI:120,D7_CUOI:10,R1:107},
  ghi_chu:"không phải dự phòng; trạng thái cổng và điều kiện nằm trong TSV"
}

phan_tich_du_phong = {
  base_commit:"cefb99386d4845e40bc2d3eabc7d6898d078305d",
  h8_tap_luat:"ho-so/unified/tap-luat-P2-v4.json",
  h8_tap_luat_sha256:SHA256(LF(tập luật giữ nguyên)),
  h8_tong_am_tiet:{sub_moi_dong:34329387,sub_dong_khac:27978808,web_dong_khac:150070912}
}
```

Trong `tep`: thêm hai TSV mới, cập nhật `README.md`. Không băm manifest vào chính nó. `ho_so.so_tep` đếm từ các tệp dự kiến đưa vào Git trong `AT\ho-so`, không tính corpus/file tạm/ignored. Điều phối kiểm lại bằng danh mục Git sau khi stage các hồ sơ được phép; SA không stage/commit trong bước soạn này.

**LF chuẩn:** thay CRLF bằng LF trên byte UTF-8 để đối chiếu với blob Git; không đổi chữ/NFC/nội dung vì mục đích băm. Bảo vệ chính dùng SHA byte thực, không chỉ SHA quy đồng LF. Ghi rõ cả hai loại hash trong evidence.

## 8. Chứng minh tương thích checker

### 8.1. Suy ra từ phụ thuộc thật

- `check_wordlist.py` đọc wordlist, nhãn CHINH, khóa chặn, họ chính tả và ba khối; C6 chỉ tính CHINH (`AT\check_wordlist.py:139–151`).
- `verify.mjs` đọc nguồn chuẩn, khóa chặn và ba khối; không đọc hai TSV phân tích. Không gán cho nó việc kiểm H3/H6/H8/H9 hoặc D6.
- C8 của hai chương trình tìm đúng tiêu đề §10 rồi khối text đầu tiên. Thay header/TOC và phần từ §11 trở đi, giữ nguyên cả §10, thì cặp từ/nghĩa vẫn giống nguồn. Không sinh lại HTML.
- Các bảng nền của C1–C7 không đổi; định dạng LF của nguồn Git không đổi. C7 trong Python chỉ là một phần, không thay kiểm D2/D5/D6/D7 đầy đủ khi thay từ thật.

### 8.2. Kiểm thực nghiệm nháp, không ghi bản sao glossary

Lệnh từ gốc repo:

```powershell
python -X utf8 -B 'analyzing-tools\ho-so\astra\du-phong-v2\evidence\joint-build.py' --prove
```

Script:

1. Dựng hai TSV, kiểm số dòng/khóa/O1, mã H8 và mọi dòng tranh chấp có câu hỏi.
2. Tạo **trong bộ nhớ** nội dung WordListAnalyze dự kiến: header/TOC và §11–12 theo mẫu, giữ nguyên §10 từng byte. Mô phỏng không có CHO_HOA nhưng vẫn có các cổng chờ đã được thống nhất; không lưu hay tự công bố bản mô phỏng.
3. Chạy checker nguyên mã, chỉ cấp cho thao tác đọc nguồn chuẩn đúng blob LF tại base và cho thao tác đọc tài liệu bản mô phỏng. Không sửa checker hoặc working tree.
4. Chạy native baseline, rồi `build_wordlist.py --check` trên **tài liệu đã sửa** trong bộ nhớ ở CRLF; so với nền. Kiểm thêm giới hạn build khi toàn bộ HTML/tài liệu là LF ở cả nền lẫn bản sửa, không sửa script để che lỗi.
5. So byte vùng bảo vệ, hai tài liệu lưu trữ, hash đầu vào và định dạng năm bản nháp. Không có bản sao ngoài repo hoặc trong thư mục tạm.

**Kết quả bắt buộc và đã có phép kiểm tái lập:**

| Kiểm | Kỳ vọng |
|---|---|
| Native Python | Lỗi C1 nền do checkout CRLF; không tuyên bố PASS |
| Native JS | Lỗi C1 và hai C8 nền do CRLF; không tuyên bố PASS |
| Python, blob LF + mô phỏng tài liệu | 0 lỗi C1–C8 theo các kiểm mà chương trình thực thi |
| JS, blob LF + mô phỏng tài liệu | 0 lỗi C1–C5/C8 theo phạm vi chương trình |
| `build_wordlist.py --check` trên tệp thật chưa đổi | Ba khối khớp |
| `build_wordlist.py --check` trên tài liệu đã sửa, CRLF | **Ba khối khớp wordlist.txt.** |
| Build khi cả HTML/tài liệu là LF, trước và sau sửa | Cùng lỗi nền `ValueError: substring not found` do ghép khối bằng CRLF; không dùng chế độ này làm cổng build đạt |
| Byte bảo vệ và §10 mô phỏng | Khớp hoàn toàn |

Log và exit code nằm ở `E\joint-proof.json`, `E\joint-proof.log`. Nếu chưa có log đạt thì chưa được ghi hoàn tất acceptance; script dừng khi kết quả khác kỳ vọng. Chứng minh này chỉ chứng minh tương thích, không phê duyệt các dòng đang tranh luận. Lúc xuất thật phải chạy lại trên tệp thật và dữ liệu LF đúng revision; không dùng bản mô phỏng thay nghiệm thu cuối.

## 9. Decisions

Không gán `cefb993` cho những câu trả lời thiết lập chỉ mới có trong hội thoại. Các hàng CHUA_COMMIT sẽ được điều phối bổ sung commit lưu lời yêu cầu/quyết định thật; không tự bịa hash.

| ID | Decision | Decided by | Date | Source commit |
|---|---|---|---|---|
| D-dpv2-1 | Chỉ phân tích/phân loại dự phòng và HM; chưa viết nghĩa hoặc phát hành | owner | 2026-11-20 | CHUA_COMMIT — yêu cầu/setup chủ, được ghi trong lời giao việc và §1 |
| D-dpv2-2 | Main 7.776, hai HTML, nguồn chuẩn và toàn §10 giữ nguyên byte | owner | 2026-11-20 | CHUA_COMMIT — trả lời phạm vi của chủ; base bảo vệ cefb993 |
| D-dpv2-3 | HM khoảng 100–300 từ | owner | 2026-11-20 | CHUA_COMMIT — trả lời thiết lập số lượng |
| D-dpv2-4 | Không tạo docs mới; kết quả cuối cập nhật tài liệu hiện có | owner | 2026-11-20 | CHUA_COMMIT — lời chủ “không cần tạo thư mục riêng…” và chỉ dẫn bước 3 |
| T-dpv2-1 | Giữ du-phong.txt 205 dòng/SHA; tầng ở TSV riêng | SA-Opus + SA-Astra, đồng thuận kỹ thuật trong review | 2026-11-20 | CHUA_COMMIT — hai cross-review §1 và §2.4; không phải chữ ký Final |
| T-dpv2-2 | Tên HM là honorable-mentions.tsv, giữ khối 205 ở §11.5 | SA-Opus + SA-Astra | 2026-11-20 | CHUA_COMMIT — O\round-1-cross-review.md §2.4 |
| T-dpv2-3 | Dùng mã/mẫu số H8 P2 v4.1; giữ riêng CHI_BE_MAT | Hai SA đã cùng xác định lỗi; Astra đối mã lại khi soạn | 2026-11-20 | cefb993 — U\tap-luat-P2-v4.json và hai bảng cổng; sửa mô tả trong các bản du-phong-v2 chưa commit |
| T-dpv2-4 | Đóng 11 lệch cũ: A cho tám mục sắc thái; D theo H5c cho hì hụi, nhão nhẹt, nhão nhoẹt. Hì hụi theo họ hè hụi, không kết luận về hì hục | SA-Opus + SA-Astra | 2026-11-20 | pending |
| T-dpv2-5 | C chỉ là nhãn cảnh báo; S4 giữ nguyên; không ban hành TT2 | SA-Opus + SA-Astra | 2026-11-20 | pending |
| T-dpv2-6 | HM chỉ tính mục đủ thẩm định; 46 L3b và chạng vạng ở hồ sơ/§12.3, không tính N; giờ cao điểm không đạt H2 hiện hành | SA-Opus + SA-Astra | 2026-11-20 | pending |
| T-dpv2-7 | Baotu là K1; tanso và vaynen là K2 “không tự động chặn”, đủ hai chữ ký; không mở lại cổng nghĩa hay cấp quyền thay | SA-Opus + SA-Astra | 2026-11-20 | pending |
| T-dpv2-8 | Giữ cả sáu cơ quan/lực lượng/truy tìm/dự bị/lên chức/đại lục với cờ rà H6; chưa có chứng cứ mới đủ phản đối H9. N=237 | SA-Opus + SA-Astra | 2026-11-20 | pending |
| T-dpv2-9 | Ngoại trừ ở C/CHO_H7: nghĩa điều trị của ngoại trú thuộc phạm vi H6.5 theo tiền lệ nội trú, còi H7 bật; không dùng đến khi đo tỷ lệ nghĩa và hai SA ký mức K. Chưa ký K2 cho khóa này | SA-Opus + SA-Astra | 2026-11-20 | pending |

Luật không từ ba chữ và quyết định phát hành 7.776 không cần đủ 300 dự phòng tiếp tục áp dụng từ `WordListAnalyze.md:151–153` ở base. Không mở lại chúng.

Nguồn đóng T-dpv2-4..8: `O\round-1-review-drafts.md` §3.1–3.5 và `A\round-1-revision-1.md`; chữ ký K2 mới tại `E\revision-1-chu-ky-astra.tsv:2–3`, đối chiếu chữ ký Opus tại review dòng 95. Điều phối điền commit thật sau; không dùng hash base thay cho các quyết định mới.

Nguồn T-dpv2-9: `O\round-1-review-drafts.md`, Lượt duyệt 2 §B/§D, và ghi nhận lượt 2 ở `A\round-1-revision-1.md`. Nội dung câu hỏi trước khi rút được lưu trong `E\revision-1-question-history.json` vì các nháp trước chưa commit. Q-dpv2-2..7 không tái dùng; chỉ còn Q-dpv2-1 mở.

## 10. Acceptance criteria

### Business

| ID | Điều kiện | Cách nghiệm thu |
|---|---|---|
| B1 | Chính và hành vi app không đổi | Bốn SHA byte, toàn §10, không diff code/HTML/wordlist |
| B2 | Phân loại đủ 205 từ, không mất lịch sử D | TSV 205 dòng; cột từ bằng du-phong.txt; §11.5 khớp |
| B3 | 237 HM, không nhầm số dòng hồ sơ với tập công bố | Lọc đúng 237 CUNG_DE_CU_CHUA_PHAT_HANH từ 285; 48 dòng ngoài N vẫn có lý do |
| B4 | Người đọc biết ngăn và việc thiếu | Không đồng nhất số khóa/số câu/số ghế; vẫn nêu 37 thiếu nghĩa và 0 D8 |
| B5 | Không chốt thay bên đang bất đồng | Hết CHO_HOA/tranh chấp ở tập cuối hoặc hai bên cùng chốt trạng thái chờ với điều kiện cụ thể; có source quyết định |
| B6 | Không phát sinh viết nghĩa/tuyển corpus/thay chính | Phạm vi diff và log công việc; không có nhiệm vụ đó chạy tự động |

### Technical

| ID | Điều kiện | Cách nghiệm thu |
|---|---|---|
| T1 | Các đầu mục 4–12 chữ, NFC, không từ ba chữ, khóa không giao chính/dự phòng/HM | Bộ kiểm bảng theo đúng hàm app, cả viết hoa đầu |
| T2 | H8 không trộn raw/sạch hoặc mẫu số cũ | Đối hai bảng cổng và replay P2 v4.1; phân biệt CHI_BE_MAT |
| T3 | Không gọi cổng thiếu thành PASS | H3/K2/chữ ký/cổng đang chờ có pointer và điều kiện; nhãn/class dự kiến được đánh dấu |
| T4 | Nghĩa đúng lượt và loại hash | 168 hash lịch sử đúng câu/lượt; không dùng raw SHA làm token SHA; không tạo PASS D6 mới |
| T5 | Ba checker không hồi quy ở chế độ phù hợp | Python/JS trên LF đúng revision 0 lỗi; build --check trên tài liệu đã sửa ở CRLF khớp ba khối; lỗi build toàn-LF giống nền; lưu native riêng |
| T6 | Văn bản theo đúng mẫu và tập cuối | Link/anchor, token thay hết, bảng counts/word set/README/manifest đồng bộ |
| T7 | UTF-8 không BOM, CRLF working tree, final newline, không trailing whitespace | Kiểm byte; thử stage do điều phối, không để safecrlf thất bại |
| T8 | Không có bản sao corpus/định nghĩa/gloss cũ | Soát tệp mới; chỉ số/hash/đầu mục/nhận định, không tải/lưu nguồn thô |
| T9 | Manifest đúng | Parse JSON, đối SHA LF các tệp mới/đổi, giữ các hash bất biến, đếm hồ sơ dự kiến đưa Git |

## 11. Rủi ro và giảm thiểu

- **Cách đọc y khoa bị bỏ qua:** T-dpv2-9 giữ ngoại trừ C/CHO_H7; đo nghĩa trước khi ký mức K. Không suy “không phải tên bệnh” thành không thuộc H6.5 hoặc lấy PPM toàn chuỗi làm tỷ lệ nghĩa đỏ.
- **H5 mới tác động chính:** ghi phát hiện, không sửa bảng checker hoặc chính để che/bù; Q-dpv2-1 quyết định công việc tương lai.
- **Hồ sơ ngoài N bị xuất nhầm:** chỉ lọc CUNG_DE_CU_CHUA_PHAT_HANH; 46 L3b/chạng vạng/bao tử không nằm trong 237.
- **C thành luật xếp hạng mới:** TT2 đã rút; S4 giữ nguyên.
- **Bảng phát hành chưa phản ánh cổng mới:** ghi rõ D/LOAI_K1 trong TSV và thủ tục bảo trì; chỉ đăng ký bảng chính thức khi có tác vụ được giao, theo OI-BANG-PHAT-HANH.
- **D7 bị diễn giải theo số đợt chung:** 131 mục có v1/v2/v3, mặt khác chỉ v2/v3 trong log. Kiểm lịch sử đúng mục trước khi xin ngoại lệ, không mở viết hiện tại.
- **Đổi mẫu số khiến đổi nhãn sát mốc:** lấy P2 đã ký; bánh củ cải thuộc hồ sơ để sau và vẫn là YEU theo P2.
- **Hash CRLF/LF lẫn nhau:** bảo vệ bằng byte, manifest bằng LF; không sửa byte nguồn chính để đạt cổng.
- **Bản quyền:** không ghi văn bản nguồn vào evidence; preview chỉ trong bộ nhớ.

## 12. Phases và task outline

1. **Review — đã xong:** Opus accept ở Lượt duyệt 2; hai SA đóng Q-dpv2-2..7, ghi T-dpv2-4..9. Không còn câu hỏi supervisor.
2. **Câu hỏi còn mở:** chủ quyết định phạm vi công việc tương lai qua Q-dpv2-1. Không tự chọn đề nghị hoặc mở việc đo/quét mới.
3. **Khóa dữ liệu:** 205 tầng/trạng thái và 237 HM đã thống nhất; sinh TSV gọn bằng bộ lọc đã định, không suy CHO_H7 thành đã được phép dùng. Status vẫn Draft cho tới bước hoàn tất do điều phối/chủ yêu cầu.
4. **Cập nhật tài liệu hiện có:** áp đúng mẫu header/TOC/§11–12, README; chỉ ở giai đoạn được giao sau Final.
5. **Manifest và nghiệm thu:** băm LF/đếm tệp, chạy ba cổng ở chế độ phù hợp trên tệp thật, so byte/link/counts; điều phối ghi log và commit. Không push nếu chủ chưa yêu cầu.
6. **Tác vụ bảo trì sau, không tự mở:** đăng ký các họ/khóa mới vào bảng phát hành khi được giao. Họ chạm chòng chành cần quyết định riêng trước khi thay bảng gây C5 trượt; không nới checker để né.

Không có ước lượng tiền/thời gian giả định cho corpus/viết sạch; chúng nằm ngoài nhiệm vụ này.

## 13. Named open items và ranh giới Final

| Mã | Việc | Tình trạng/đường xử |
|---|---|---|
| Q-dpv2-1 | Chủ có giao hậu kiểm chính sau này không | Không chặn lưu phát hiện hiện tại; chưa có quyền mở tác vụ thêm |
| Q-dpv2-2, Q-dpv2-3 | H5 và tám A/C | Đã đóng: T-dpv2-4/5 |
| Q-dpv2-4 | HM chưa thẩm định | Đã đóng: T-dpv2-6 |
| Q-dpv2-5 | Baotu/tanso/vaynen | Đã đóng: T-dpv2-7; đủ hai chữ ký K2 |
| Q-dpv2-6 | Sáu đề cử H6 | Đã đóng: T-dpv2-8, phương án 1 |
| Q-dpv2-7 | Ngoại trừ/ngoại trú | Đã đóng: T-dpv2-9; thống nhất C/CHO_H7, không gửi SA-Fable |
| OI-H7-NGOAITRU | Đo tỷ lệ nghĩa điều trị của ngoại trú ở web như tiền lệ nội trú, rồi hai SA ký K1/K2/không tự động | Để sau; chỉ cần khi muốn dùng ngoại trừ. Chưa ký mức K và không mở đo tự động |
| OI-D7 | Kiểm lịch sử đúng từ trước tái mở P7 | Để sau; không có lượt viết nào được giao |
| OI-D8 | Hoàn tất nguồn gốc nghĩa khi chuẩn bị thay thật | Để sau, không giả hoàn thành từ 168 hash |
| OI-CHECKOUT | Cách giữ LF lâu dài trên Windows | Ngoài phạm vi; không sửa .gitattributes/nguồn chính hiện tại |
| OI-SCAN | Rà 632 cặp H5/474 từ chính và 1.177 cặp H7/634 khóa | Chỉ nếu chủ giao; đây là số đầu vào chưa phân loại, không phải số lỗi. Bước giới hạn ban đầu chỉ họ chòng chành/tròng trành |
| OI-BANG-PHAT-HANH | Đăng ký họ hì hụi/hè hụi, nhão nhẹt/nhão nhoẹt, chọc lét/chọc léc, chán phèo/chán phè vào spelling_families.tsv; baotu vào blocked_keys.tsv | Để sau, khi có tác vụ thay/bảo trì được giao. Họ tròng trành/chòng chành chờ quyết định chủ vì ghi LOAI sẽ làm C5 trượt ở chính; phải phối hợp P6/P7/phát hành nếu thay chính |

Chỉ đổi Status thành Final khi không còn câu hỏi quan trọng **trong phạm vi thực hiện** chưa được xử lý, hai SA accept văn bản/dữ liệu và mọi chữ ký/nguồn quyết định cần thiết đã ghi. Các việc tương lai chưa được giao không được coi là đã được chủ phê duyệt.

## 14. Tham chiếu

- [`du-phong-v2-bao-cao-chung.md`](du-phong-v2-bao-cao-chung.md): đồng thuận và hai lập trường.
- [`du-phong-v2-cau-hoi.md`](du-phong-v2-cau-hoi.md): chỉ câu hỏi còn mở.
- [`du-phong-v2-phan-loai.tsv`](du-phong-v2-phan-loai.tsv), [`du-phong-v2-honorable-mentions.tsv`](du-phong-v2-honorable-mentions.tsv): dữ liệu nháp có cờ tranh chấp.
- `A\round-1-analysis.md`, `A\round-1-cross-review.md`; hai báo cáo tương ứng trong O; các đề nghị sau review trong evidence.
- `U\tap-luat-P2-v4.json`, hai cổng v4, `AT\tieu-chi-thong-nhat.md`, các nguồn/dòng được nối trong TSV.
- `E\joint-build.py`, `joint-inputs.json`, `joint-summary.json`, `joint-publication-text.json`, `joint-proof.json`, `joint-proof.log`.
- `O\round-1-review-drafts.md`; `A\round-1-revision-1.md`; `E\revision-1-*` gồm audit, chữ ký, số H7, phiếu P4 sáu từ, ca ngoại trú và bản lưu câu hỏi cũ.

### Hồ sơ dự kiến đưa vào Git

Danh mục đường dẫn cụ thể: `E\revision-1-artifacts.tsv`. Danh mục chỉ gồm năm tệp chung, các báo cáo vòng 1/bản sửa và các evidence đã được các báo cáo đó giới thiệu ở thư mục du-phong-v2 của hai SA; không gồm cache, thư mục bắt đầu `_`, tệp nhị phân, corpus, danh sách HND tải về hoặc glossary sao chép.

Điều phối kiểm danh mục trước khi stage, đối số tệp để cập nhật `ho_so.so_tep`; không `git add` mù toàn cây. Không cần sửa `AT\ho-so\README.md` trong phạm vi này vì chỉ mục hồ sơ đã nằm ở đây và các báo cáo được dẫn. Nếu một nhiệm vụ sau sửa README hồ sơ, phải cập nhật `ho_so.readme_sha256` tương ứng.
