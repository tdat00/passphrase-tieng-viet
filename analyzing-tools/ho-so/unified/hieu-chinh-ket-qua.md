# P1–P3: biên bản đối soát và kết quả hiệu chỉnh

**Quyết định: P3 ĐẠT ở vòng 1, ngày 19/11/2026.** Hai phiếu độc lập cho **κ Cohen không trọng số = 0,671207** trên bảy nhãn chính (mốc 0,60); hai bên đồng ý về việc có phản đối hay không ở **274/300 mục = 91,33%** (mốc 90%). Vì đạt cả hai điều kiện trên mẫu mới nhất theo quy tắc đã ghi trước, **dừng tại 300**, không sửa nhãn để nâng điểm và không rút thêm mẫu 100. Đây là hiệu chỉnh cách chấm, **không** phải 300 quyết định phát hành, hay chứng nhận đã có đủ 7.776 từ và 300 dự phòng.

## 1. Đầu vào để sang P3

- **P1:** 12.757 khóa; 13.356 mặt chữ, gồm 4.340 A+O, 3.436 A, 3.436 O, 2.144 bổ sung. Mỗi mục đủ số lượt phụ đề/web và số câu Leipzig/Tatoeba; đọc bảng bằng lược đồ 8 cột vô hướng + 23 mảng JSON thẳng hàng. Bảng vận hành `bang-khoa-chung.tsv` SHA-256 `6019776635720422496a26856f38a6e1d2a49f895f2ddc5491359a73e8feb874`; bảng gốc `discussion\bang-khoa-chung.tsv` đã ký vẫn giữ nguyên. Với số đếm mới phải dùng mẫu số âm tiết trong `opus-counts.meta.json`, không trộn với mẫu số cũ.
- **P2:** Opus chạy Python, Astra chạy JavaScript dưới cùng manifest v3 `99a43f1a04203a7c6b4b7aed57e8a1e87c9369a9938775258fc3a84a8f417677`. Khớp **120.204/120.204** dòng, đúng thứ tự khóa, mặt chữ, cổng, mức và cả chuỗi mã lý do (cột diễn giải tự do có thể khác). Ba dòng từng lệch đã được giải thích: *gián* không thể chờ chọn trong khóa đã chọn đích danh; *nhà thơ* mang cả K0 lẫn K1. Trong 13.356 mặt chữ, `TONG`: **9.235 PASS, 1.639 CANH_BAO, 1.424 CHO, 1.058 FAIL**. Còn 11.804 khóa có ít nhất một mặt chữ không FAIL; CHO/CANH_BAO không được coi là đã qua P4–P6.
- **P3:** đã bỏ cả 1.604 khóa từng dùng để chấm hoặc dự báo; quần thể để rút còn 10.650 khóa. Chọn 300 khóa mới, mỗi khóa một mặt chữ. Người chấm chỉ được cung cấp ID, khóa, từ và số liệu/cờ chung, **không cung cấp người đề cử hoặc phiếu cũ theo từng mục**. Opus tái lập mẫu và xác nhận trước chấm. Hai bên nộp phiếu, tạo cờ của mình rồi mới đối chiếu; chưa thay dòng phiếu nào sau mở.

| Tiêu chí phân tầng | Số mục thật trong mẫu (khớp mục tiêu đã công bố) |
|---|---|
| Nguồn gốc khóa | Giao 90, riêng A 60, riêng O 60, khóa bổ sung 60, tranh chấp cũ 30 |
| PPM trung bình phụ đề/web | ≥10: 66; 1–<10: 108; 0,1–<1: 96; <0,1: 30 |
| Số khối | 1: 45; 2: 216; 3: 39 |
| Có nhãn vùng trong chứng cứ từ điển | Có 24; chưa có nhãn 276 (không đồng nghĩa 276 từ “toàn quốc”) |
| Cờ cần đọc | Có 105; không 195. TONG của mẫu: 195 PASS, 56 CANH_BAO, 49 CHO, 0 FAIL |

Mẫu cố ý có đủ nhóm khó, không đại diện cho tỉ lệ OK hoặc tỉ lệ phản đối của toàn bộ rổ.

## 2. Ma trận bảy nhãn

**Hàng = Opus, cột = Astra.** Nhãn chính không gộp ở phép tính κ.

| Opus \ Astra | OK | R1 | R2 | S | K | V | X | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| OK | 208 | 4 | 0 | 4 | 1 | 0 | 1 | 218 |
| R1 | 11 | 10 | 0 | 1 | 0 | 1 | 0 | 23 |
| R2 | 4 | 2 | 2 | 1 | 0 | 0 | 0 | 9 |
| S | 1 | 0 | 0 | 8 | 0 | 0 | 0 | 9 |
| K | 2 | 0 | 0 | 0 | 4 | 0 | 0 | 6 |
| V | 2 | 2 | 0 | 0 | 0 | 14 | 0 | 18 |
| X | 4 | 1 | 0 | 0 | 0 | 0 | 12 | 17 |
| **Tổng** | **232** | **19** | **2** | **14** | **5** | **15** | **13** | **300** |

- Đồng nhãn chính **258/300 = 86,00%**. Đồng thuận kỳ vọng từ các phân bố biên: **51.678/90.000 = 57,42%**. Do đó `κ = (0,86 − 0,5742)/(1 − 0,5742) = 1429/2129`.
- Ở phép kiểm thứ hai, `OK/R1` là không phản đối, `R2/S/K/V/X` là có phản đối. **Cả hai không phản đối 233; cả hai phản đối 41; chỉ Opus phản đối 18; chỉ Astra phản đối 8.** Có 42 mục khác nhãn chính: 15 là OK/R1, một mục cả hai phản đối khác mã, còn 26 khác phía nhận/không nhận. Hai phép kiểm không thay thế nhau.
- Lớp `C/H/K/F` là cột riêng, không dùng để tính κ nhãn chính: hai người trùng lớp ở **253/300 = 84,33%**. “K” ở cột nhãn chỉ vấn đề *đọc khóa*; “K” ở cột lớp chỉ khái niệm trừu tượng.
- **Phân tích độ nhạy đã báo trước khi mở phiếu:** 2 khóa từng lọt mẫu *đọc–sửa* của Astra trước vòng thảo luận (*cúc vạn thọ, ống nghe*), không phải phiếu chấm mốc. Giữ nguyên mẫu gốc để quyết định. Nếu bỏ riêng 2 khóa: đồng nhãn 257/298; `κ = 25597/37815 = 0,676901`; đồng thuận nhị phân **273/298 = 91,61%**. Kết luận không đổi.

## 3. Cách dùng nhãn tiếp theo — không đổi luật sau khi thấy kết quả

| Vấn đề lộ ra | Cách xử lý ở P4 theo bộ tiêu chí đã ký |
|---|---|
| OK/R1/R2: chẳng hạn *lò dò, thước gấp, vị lai* | Đánh giá nghĩa người dùng phổ thông biết và bằng chứng đời sống, không lấy một con số hiếm ở kho để tự biến thành R2. OK + R1 giữ R1 nếu chưa phân xử; R2 là phản đối, cần lý do kiểm được. |
| X so với OK/R1: *khí nhà kính, giờ ăn, học lại* | Với ba khối kiểm H2: đây có phải tên cố định gọi một đối tượng cụ thể? Với hai khối kiểm H3: có ngữ nghĩa/quy ước riêng hay chỉ là khung kết hợp tự do? Có mục từ là chứng cứ nhưng không miễn bước này. |
| V: *modem, lavabo, tulip, mù tạt, neon* | Ghi đủ dạng đối chứng thật, lý do cùng nghĩa, kiểu biến thể và lượt đúng nghĩa ở **từng** kho; áp ngưỡng H5 đã đăng ký. Không loại mọi từ mượn, không coi mọi lượt của dạng viết đa nghĩa là cùng một nghĩa. |
| S và K: *thủ thuật, trát, thước, ống nghe* | S dựa trên nghĩa đỏ **còn dùng phổ biến của đúng mục**, không phải chỉ một ngữ cảnh liên tưởng. K cần cách đọc khác của **trọn khóa** và bằng chứng độ tự nhiên; cảnh báo 0,3 PPM không phải phán quyết. Mã `DOC_NGHIA_H6` yêu cầu đọc chính nghĩa, không tự chuyển thành một cách đọc khác. |
| C/H/K/F | Tách vật/người và hành động/trạng thái quan sát được khỏi quan hệ/đại lượng trừu tượng; chức năng ngữ pháp F cần xác nhận rõ. Khi còn khác lớp phải phân xử trước xếp hạng. |

Các từ nêu trên là **ví dụ cần coi lại**, không phải kết quả đã phân xử H9. Không mặc nhiên xóa phản đối của một người vì P3 đạt ngưỡng; không cho điểm thông dụng bù vi phạm cứng. Bảng 42 ca khác nhãn nguyên trạng ở `p3-do-dong-thuan-astra300.json`.

**Chốt trọng số sang P4/P6: giữ nguyên S2–S4, không điều chỉnh trong vòng này.** Điểm thông dụng là trung bình bốn bách phân vị, tính trong cùng số khối. Bậc OK trước R1; trong bậc dùng `F + G − T`: C +15, H +5, K 0, F −20; rủi ro vùng +1/loại vào T (tối đa 4), lỗi H5d 5–<10% +5 một lần, dài trên 10 chữ +5, ba khối +3, mục thứ hai của cặp đảo +5. Hạn mức Q vẫn giữ. Đây là hiệu chỉnh người chấm; chưa có bằng chứng phải thay thang điểm.

## 4. Hồ sơ tái lập và xác nhận

| Tệp | SHA-256 |
|---|---|
| `p3-quy-tac-dung.md` | `c7b3dca98beb933ca6b3239443470306e869b41d01eea0eecc3b742c02b21ce1` |
| `mau-hieu-chinh-300.tsv` | `da3566b8ded0a456d6741a45396f466c4828e93454435d816c55f582981fa94e` |
| `can-cu-p3-300.tsv` | `7511f907b15c3cac568faf9abbc752ecdc313560eac5e09fbd3875702c46e3c3` |
| `hieu-chinh-astra.tsv` | `b5f3e281e59a51a009e641cc44bbe86ccc1931e3aa89cc60e13d9aebf98c077c` |
| `hieu-chinh-opus.tsv` | `bc7491ff6b0ab4b65b3e4aec35d1c33ef725faeee0933cdd2c3aa99b5c6a6143` |

Phiếu nộp ở hai cờ `_done\P3-astra.flag`, `_done\P3-opus.flag`. Đối chiếu độc lập bằng `p3-do-dong-thuan-astra.py` sau khi cả hai cờ tồn tại. Xác nhận cuối của hai bên lưu dưới dạng hai cờ `_done\P3-ket-qua-astra.flag` và `_done\P3-ket-qua-opus.flag` băm cùng tệp báo cáo này. Không đưa dữ liệu hay phiếu này vào repo hoặc vào lô viết nghĩa sạch.
