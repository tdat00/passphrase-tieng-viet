# Review bản nháp chung dự phòng v2, vòng 1 — SA-Opus

**Ngày:** 20/11/2026. **Người review:** SA-Opus. **Bản được review:** năm tệp `U\du-phong-v2-*` (SA-Astra soạn, Draft round 1) và review chéo `A\round-1-cross-review.md`. **Base:** `cefb993`.

**Kết luận: changes requested.** 13 thay đổi bắt buộc (mục 4), 7 gợi ý (mục 5).

`AT = analyzing-tools`; `U = AT\ho-so\unified`; `O = AT\ho-so\opus\du-phong-v2`; `OE = O\evidence`; `A = AT\ho-so\astra\du-phong-v2`; `E = A\evidence`. **V** = verified (đối chiếu tệp, mã hoặc lệnh); **A** = assumed (nhận định).

## 0. Tóm tắt

- Số liệu trong năm bản nháp khớp dữ liệu repo (V, mục 1). Mô phỏng độc lập cho thấy các chỉnh sửa tài liệu trong kế hoạch giữ nguyên kết quả của ba bộ kiểm so với nền, ở cả bản LF lẫn checkout CRLF.
- Opus nhận cả chín điểm Astra nêu về phân tích của Opus (mục 2).
- Opus đóng bằng đồng thuận Q-dpv2-2 (D cho ba mục), Q-dpv2-3 (A cho tám mục) và Q-dpv2-4 (phương án 2). Ở Q-dpv2-5, Opus nhận K1 cho `baotu` và ký K2 "không tự động chặn" cho `tanso`, `vaynen`; câu này đóng khi Astra ký thứ hai (mục 3).
- Opus đổi lập trường về *đại lục* để áp một nguyên tắc chung cho cả sáu mục của Q-dpv2-6, và đề nghị đóng câu này theo phương án 1.
- Nếu Astra nhận: tầng A149/B36/C14/D6; HM N = 237 (231 nếu Q-dpv2-6 theo phương án 2). Chỉ còn Q-dpv2-1 cho chủ.
- Thay đổi bắt buộc chính:
  - ghi đúng lập trường Opus trong hai TSV;
  - cập nhật bốn văn bản theo các câu đã đóng;
  - bổ sung phạm vi và chi phí cho Q-dpv2-1;
  - thêm `build_wordlist.py --check` vào nghiệm thu;
  - nêu rõ hai tài liệu lưu trữ nằm ngoài phạm vi;
  - mở việc đăng ký vào bảng phát hành cho sau này.

## 1. Kiểm dữ kiện của bản nháp

Lệnh và log ở mục 6. Mọi kết quả dưới đây là **V**, trừ cột nhận định ở dòng cuối.

| Mục kiểm | Kết quả | Bằng chứng |
|---|---|---|
| Bảng dự phòng | 205 dòng, đúng thứ tự `AT\du-phong.txt`. Tầng A141/B36/C14/D3 cộng 11 CHO_HOA; nghĩa 168/37; H8 198/4/2/1. Khớp văn bản | `OE\kiem-ban-nhap-chung.log` |
| Bảng HM | 285 dòng; khóa tính lại đúng; 0 khóa trùng; 0 giao với chính hay dự phòng; mọi mục 4–12 chữ, NFC. Nhóm 122/10/107/46; 230 cùng đề cử, 55 CHO_HOA; H8 238 MANH, 1 CHI_BE_MAT, 46 chưa có cổng. Khớp | như trên |
| Không lưu câu giải nghĩa | Bảng dự phòng chỉ có mã CO_PASS_LICH_SU/CHUA_VIET; bảng HM không có cột nghĩa; 0/7.776 câu của danh sách chính xuất hiện trong hai TSV | như trên |
| SHA vùng bảo vệ | Bảy giá trị ở kế hoạch §3 và §4.3 khớp tệp: bốn SHA byte, blob LF, cột từ, `du-phong.txt` LF | như trên |
| *mặt khác* | 131/132 mục khấu trừ có log D6 ở v1, v2, v3. *mặt khác* chỉ có v2, v3 và không có trong `U\viet-lai-v1.tsv`. Nhận định của Astra đúng | như trên |
| Mẫu số H8 | Với 239 HM đủ số bốn kho, không mục nào đổi MANH/YEU giữa mẫu số P2 và mẫu số ở mục 0 của tiêu chí | `OE\pham-vi-hau-kiem.log` |
| Dòng trích dẫn | Các dòng được dẫn trong `U\opus-counts.tsv`, `O\de-cu-them-opus.tsv:81, :171`, `O\round-1-cross-review.md`, `WordListAnalyze.md:471, :744` và `AT\tieu-chi-thong-nhat.md` đúng nội dung | `OE\kiem-ban-nhap-chung.log` |
| Tương thích checker | Áp đúng văn bản §5.1–5.2 của kế hoạch lên bản sao ngoài repo: §10 giữ nguyên byte, chỉ một tiêu đề §10, hai anchor mới đúng. Kết quả sau sửa trùng nền ở cả hai chế độ: bản LF cho check 0 lỗi, verify 0 lỗi; bản CRLF cho check C1, verify C1 + 2×C8, build --check đạt. Trên bản LF, `build_wordlist.py --check` lỗi ngay ở nền vì script ghép khối bằng CRLF | `OE\mo-phong-ke-hoach*.log` (bốn tệp) |
| H7 của tập cuối | Mọi cách đọc khác cùng khóa của 205 dự phòng và 239 HM có hồ sơ: 50 + 98 cặp; 11 + 37 cặp đạt mốc còi; chỉ 1 cặp có trong bảng còi. Opus đọc hết (A): ở mức đạt mốc chỉ *báo tử* thuộc nhóm đỏ; dưới mốc chỉ có *tận số* và *vảy nến* | `OE\h7-quet-bo-sung.tsv` |

Không thấy dữ kiện sai trong năm bản nháp. Các thay đổi bắt buộc ở mục 4 có ba nguồn:

- lập trường của Opus ghi chưa đúng hoặc chưa đủ;
- các câu hỏi nay đóng được;
- kế hoạch còn thiếu ba điểm.

## 2. Phản hồi review chéo của Astra (`A\round-1-cross-review.md` §3)

| # | Điểm Astra nêu | Opus | Ghi chú |
|---|---|---|---|
| 1 | *hì hục* bị suy quá mức | Nhận | Rút *hì hục* khỏi các phát hiện H5 ở danh sách chính (`O\round-1-analysis.md:11–12`, `:170`, `:339`). Chỉ còn *chòng chành* có nguồn |
| 2 | *piano* bị loại bằng dữ kiện sai | Nhận | Đã sửa ở `O\round-1-cross-review.md`, mục K3 |
| 3 | 40 mục không thành 77 ghế | Nhận | 40 mục A-F chỉ thay tối đa 40 ghế F cùng lúc |
| 4 | 37 thiếu nghĩa, không phải 36 | Nhận | B36 cộng *trở lên* ở C |
| 5 | `kiem-dau-ra.py` không kiểm H2/H3/H6/H9 | Nhận | Trường `xac_minh` ở bảng vòng 1 của Opus không có nghĩa mọi luật đã đạt. Bảng chung đã ghi đúng phạm vi kiểm |
| 6 | 122 chỉ là trần cấu trúc | Nhận | |
| 7 | Không ban hành TT2 | Nhận | Rút TT2 (`O\round-1-analysis.md:141`). C chỉ là nhãn cảnh báo; S4 giữ nguyên |
| 8 | Câu về chất gây nghiện không có cơ sở | Nhận | Rút cụm "không phải thuốc lá hay chất gây nghiện" (`O\round-1-analysis.md:97`). Chỉ giữ: *ăn trầu* không có trong ví dụ nhóm 7 của H6 và không có phản đối hợp lệ |
| 9 | Gọi lỗi CRLF là "lỗi giả" dễ gây hiểu nhầm | Nhận | Sửa cách gọi ở `O\round-1-analysis.md:320` và `O\round-1-cross-review.md:37`: đó là lỗi định dạng thật của checkout CRLF; nội dung chuẩn LF thì đạt |

Opus cũng xác nhận phát hiện mới của Astra về *mặt khác* (mục 1).

## 3. Lập trường của Opus sau review

### 3.1. Q-dpv2-2: nhận D cho *hì hụi*, *nhão nhẹt*, *nhão nhoẹt*

- ***hì hụi*:** Opus ký họ *hì hụi/hè hụi*.
  - en.wiktionary (oldid 93445969) ghi *hè hụi* là dạng khác (V, đã đọc ở bước 2). HND có cả hai mặt chữ (V, `E\cross-review-hnd-membership.tsv`).
  - *hì hụi* có 0/0 lượt sạch (V, `U\opus-counts.tsv:4870`), nên không thể chiếm ≥ 95% ở cả hai kho (H5c, `AT\tieu-chi-thong-nhat.md:124`).
  - Không suy ra *hì hục* cùng họ.
- ***nhão nhẹt*, *nhão nhoẹt*:** Opus ký là một từ (A: biến thể âm đệm, cùng nghĩa), như Astra.
  - HND 74K có cả hai mặt chữ (V).
  - Số sạch 9/0 và 6/1; *nhão nhoét* cùng khóa với *nhão nhoẹt* có thêm 5/1 (V, `U\opus-counts.tsv:8221–8222`, `:15957`). Không dạng nào đạt H5c.
- Hai bên đã cùng xác nhận "cùng một từ" theo `AT\tieu-chi-thong-nhat.md:135`, nên không còn câu hỏi về thủ tục H9. CH5 của Opus rút hẳn.

### 3.2. Q-dpv2-3: nhận A cho tám mục, rút TT2

- Tám mục về A: *ăn trầu, bèo bọt, chấp nhặt, giở giọng, giở quẻ, mụ mị, non choẹt, tía lia*.
- Lý do:
  - cảnh báo sắc thái chưa đủ ba yếu tố của phản đối hợp lệ (`AT\tieu-chi-thong-nhat.md:184–186`, `:192`);
  - cả tám đều được hai bên chấm OK ở P4.
- Đây là lệch thời điểm: ở vòng 1 Opus đã xếp A, và chỉ nhận C khi lấy hợp với bản vòng 1 của Astra. Cảnh báo vẫn giữ ở cột ý kiến của Astra.

### 3.3. Q-dpv2-4: nhận phương án 2

- HM chỉ tính các mục đã đủ thẩm định. Hai nhóm không tính vào N, nhưng §12.3 ghi số lượng và nguồn:
  - 46 mục L3b: chưa qua P2/P4/H9, lớp chỉ là đề xuất, DF chưa đo;
  - *chạng vạng*: chưa xác nhận *choạng vạng* là cùng từ, và dạng này chưa được đếm.
- Opus nhận phản đối H2 của Astra với *giờ cao điểm*: ba khối gọi một khoảng thời gian, không thuộc các loại tên mà `AT\tieu-chi-thong-nhat.md:82` cho phép.

### 3.4. Q-dpv2-5: K1 cho `baotu`; Opus ký K2 cho `tanso`, `vaynen`

- **`baotu`:** nhận K1 của Astra. *báo tử* là cách đọc tự nhiên (A); PPM gộp 0,385 ≥ 0,3 (V).
  - *bao tử* không tính vào HM.
  - Theo K1, cả khóa `baotu` không dùng, kể cả *bào tử* (`AT\tieu-chi-thong-nhat.md:166`).
- **`tanso`** (*tần số*, HM R1) **và `vaynen`** (*vậy nên*, dự phòng B): Opus ký **K2 "không tự động chặn"** (`AT\tieu-chi-thong-nhat.md:167`). Lý do:
  - cách đọc khác hiếm: *tận số* (H6.4) có PPM gộp 0,207, *vảy nến* (H6.5) có 0,253; cả hai dưới mốc 0,3 và thấp hơn nhiều mục đang xét (khoảng 56 và 33,7);
  - không thuộc nhóm tự hại, bạo lực hay tình dục, nên còi không bật (`:160`);
  - cổng P2 cho hai mục này H7 PASS (V, `U\cong-opus-v4.tsv:94291`, `:114307`; cùng dòng trong `U\cong-astra-v4.tsv`).
- Cần chữ ký thứ hai của Astra. Khi có, Q-dpv2-5 đóng.

### 3.5. Q-dpv2-6: một nguyên tắc cho cả sáu mục

- Opus sửa lập trường: giữ cả *đại lục*, có cờ.
- Lý do là để nhất quán:
  - ở `O\round-1-cross-review.md:110`, Opus nêu nguyên tắc "lo ngại chưa có chứng cứ không loại một đề cử";
  - nhưng ở `:113`, Opus lại rút *đại lục* chỉ dựa trên nhận định (A).
- Opus chọn phương án 1 cho cả sáu: giữ đề cử, ghi cờ rà H6 trước khi dùng. Chính Astra cũng ghi rằng chưa có bằng chứng mới để tuyên bố năm mục đầu trượt H6.
- Đề nghị Astra nhận phương án 1 để đóng câu hỏi. Nếu Astra vẫn giữ phương án 2 cho năm mục, gửi Q-dpv2-6 cho SA-Fable với hai lập trường mới (thay đổi bắt buộc 7).

### 3.6. Q-dpv2-1: giữ cho chủ, bổ sung phạm vi

Giữ câu này, không chặn công việc. Opus vẫn đề nghị phương án 2, nhưng chủ cần biết khối lượng của từng phương án (thay đổi bắt buộc 8).

### 3.7. Số liệu sau khi đóng

| Dự phòng | A | B | C | D | Chờ hòa |
|---|---:|---:|---:|---:|---:|
| Số mục | 149 (109 không-F, 40 F) | 36 | 14 (13 không-F, 1 F) | 6 | 0 |

| Nhóm HM | Tính vào N | Không tính |
|---|---:|---|
| D6_CUOI | 120 (115 nếu Q-dpv2-6 theo phương án 2) | *bao tử* (K1), *chạng vạng* (chờ H5) |
| D7_CUOI | 10 | |
| R1 | 107 (106) | |
| L3B_CHUA_CHAM | 0 | 46 |
| **N** | **237 (231)** | 48 |

- Số liệu V theo `OE\kiem-ban-nhap-chung.log`, ở các dòng `tang_sau_khi_dong_Q2_Q3`, `tang_x_ngan_sau` và `N_neu_…`.
- N = 237 giả định Astra ký K2 cho *tần số*. Nếu không, N = 236 (hoặc 230 nếu Q-dpv2-6 theo phương án 2). Cả hai trường hợp vẫn trong khoảng 100–300.

## 4. Thay đổi bắt buộc

### `U\du-phong-v2-phan-loai.tsv`

**1. Tám mục sắc thái về A.**
- **Vị trí:** các dòng *ăn trầu, bèo bọt, chấp nhặt, giở giọng, giở quẻ, mụ mị, non choẹt, tía lia*.
- **Sửa:**
  - đặt `tang_opus=A`, `tang_chung=A`, `tranh_chap=KHONG`, `cau_hoi=-`; các cột khác giữ nguyên;
  - thay `y_kien_opus` bằng: "A: nhận lần rút C của Astra; cảnh báo sắc thái chưa là phản đối hợp lệ theo H9; không đổi S4.";
  - riêng *ăn trầu*, thêm vào cuối: " Không đưa nhận định y khoa về trầu cau; chỉ ghi mục không có trong ví dụ nhóm 7 của H6."
- **Căn cứ:** mục 3.2.

**2. Ba mục H5c về D.**
- **Vị trí:** các dòng *hì hụi, nhão nhẹt, nhão nhoẹt*.
- **Sửa:**
  - đặt `tang_opus=D`, `tang_chung=D`, `tranh_chap=KHONG`, `cau_hoi=-`, `trang_thai_h=KHONG_DUNG_H5_H9`;
  - đặt `con_thieu` như ba D cũ: "Không dùng theo H5/H9; giữ dòng để đối chiếu lịch sử";
  - thay `y_kien_opus`:
    - *hì hụi*: "D (H5c): Opus ký họ hì hụi/hè hụi (en.wiktionary oldid 93445969; HND có cả hai); hì hụi 0/0 lượt sạch nên không thể đạt 95%/20. Không suy hì hục cùng họ."
    - *nhão nhẹt*: "D (H5c): Opus ký nhão nhẹt và nhão nhoẹt là một từ (biến thể âm đệm); số sạch 9/0 và 6/1, nhão nhoét cùng khóa 5/1: không dạng nào đạt 95%/20."
    - *nhão nhoẹt*: "D (H5c): như nhão nhẹt; vi.wiktionary (oldid 2366609) nối nhão nhoẹt với nhão nhoét cùng khóa."
- **Căn cứ:** mục 3.1.

**3. *vậy nên* đóng H7.**
- **Vị trí:** dòng *vậy nên*.
- **Sửa khi Astra đã ký:**
  - đặt `ma_van_de=H7_K2;CHUA_VIET;D8_CHUA_CO`, `trang_thai_h=HO_SO_LICH_SU_CHUA_PHE_DUYET_THAY`, `cau_hoi=-`;
  - bỏ "Khép H7; " khỏi `con_thieu`;
  - thay `y_kien_opus` bằng: "B. H7 K2, Opus ký không tự động chặn: vảy nến (H6.5) PPM gộp 0,253 < 0,3, thấp hơn nhiều vậy nên (khoảng 33,7); không thuộc tự hại, bạo lực, tình dục. Chưa có câu giải nghĩa."
- **Nếu Astra không ký:** giữ CHO_H7 và Q-dpv2-5, chỉ thay `y_kien_opus` như trên.
- **Căn cứ:** mục 3.4.

### `U\du-phong-v2-honorable-mentions.tsv`

**4. Ghi đúng lập trường Opus ở sáu dòng Q-dpv2-6.**
- **Vấn đề:** `y_kien_opus` của *cơ quan, dự bị, lên chức, lực lượng, truy tìm* hiện chỉ chép lý do của Astra ("Astra tạm không đề cử: …"). Chữ này lấy từ cột ghi chú ở `OE\de-cu-hop-nhat-de-xuat-opus.tsv:78`, `:93`, `:142`, `:152`, `:252`. Người đọc có thể hiểu là Opus đồng ý bỏ.
- **Sửa năm dòng đó:** thay `y_kien_opus` bằng "Opus giữ đề cử có cờ: P4 hai bên OK, không có phản biện (U\phieu-opus.tsv, U\phieu-astra.tsv, U\phan-bien.tsv); lo ngại H6 chưa là phản đối hợp lệ theo H9. Cờ của Astra: <giữ nguyên lý do hiện có>."
- **Sửa dòng *đại lục*:** đặt `de_cu_opus=CO_DIEU_KIEN`; thay `y_kien_opus` bằng "Opus đổi lập trường ở review bản chung: giữ đề cử R1 có cờ rà H6.3 (nghĩa Trung Quốc đại lục). Lo ngại này là nhận định, chưa là phản đối hợp lệ; áp cùng nguyên tắc với năm mục OK."
- **Nếu Astra nhận phương án 1:** cả sáu dòng đặt `ket_luan_nhap=CUNG_DE_CU_CHUA_PHAT_HANH`, `tranh_chap=KHONG`, `cau_hoi=-`, và thêm "rà H6 trước khi dùng" vào `dieu_kien`.
- **Căn cứ:** mục 3.5.

**5. Kết luận H7 cho *bao tử* và *tần số*.**
- ***bao tử*:**
  - đặt `ket_luan_nhap=LOAI_K1`, `de_cu_opus=KHONG_DE_CU`, `tranh_chap=KHONG`, `cau_hoi=-`, `trang_thai_h=HO_SO_TU_DAT_LICH_SU_NGHIA_BI_LOAI;H7_K1`;
  - `y_kien_opus`: "Nhận K1 của Astra: báo tử (H6.4) là cách đọc tự nhiên của khóa baotu, PPM gộp 0,385 ≥ 0,3; loại cả khóa, không tính HM."
- ***tần số* (khi Astra đã ký):**
  - đặt `ket_luan_nhap=CUNG_DE_CU_CHUA_PHAT_HANH`, `tranh_chap=KHONG`, `cau_hoi=-`, `trang_thai_h=HO_SO_R1_LICH_SU;H7_K2`;
  - `y_kien_opus`: "H7 K2, Opus ký không tự động chặn: tận số (H6.4) PPM gộp 0,207 < 0,3, thấp hơn nhiều tần số (khoảng 56); không thuộc tự hại, bạo lực, tình dục."
- **Căn cứ:** mục 3.4.

**6. 46 mục L3b và *chạng vạng* ra khỏi N.**
- **Sửa:**
  - đặt `ket_luan_nhap=NGOAI_HM_CHUA_THAM_DINH` cho 46 mục L3b và `NGOAI_HM_CHO_H5` cho *chạng vạng*;
  - đặt `de_cu_opus=KHONG_TINH_HM`, `tranh_chap=KHONG`, `cau_hoi=-`; chuyển các cờ H2/X sang `dieu_kien`;
  - `y_kien_opus` của 46 mục: "Q-dpv2-4 phương án 2: chưa qua P2/P4/H9 nên không tính HM; nguồn U\l3b-de-cu-opus.tsv." Riêng *giờ cao điểm* thêm: " Opus nhận phản đối H2 của Astra (tieu-chi:82).";
  - `y_kien_opus` của *chạng vạng*: "Q-dpv2-4 phương án 2: chờ xác nhận cùng từ và đo choạng vạng trước khi tính."
- **Bảng công bố ở AT:** chỉ gồm các dòng `CUNG_DE_CU_CHUA_PHAT_HANH`.
- **Căn cứ:** mục 3.3.

### `U\du-phong-v2-cau-hoi.md`

**7. Chỉ giữ các câu còn mở.**
- **Bỏ** Q-dpv2-2, Q-dpv2-3, Q-dpv2-4 khỏi danh sách; bỏ cả Q-dpv2-5 khi Astra đã ký K2.
- **Thêm** sau đoạn mở đầu: "**Đã đóng bằng đồng thuận hai SA** (O\round-1-review-drafts.md §3): Q-dpv2-2 (D cho hì hụi, nhão nhẹt, nhão nhoẹt), Q-dpv2-3 (A cho tám mục; C chỉ là nhãn cảnh báo, S4 giữ nguyên), Q-dpv2-4 (phương án 2: HM chỉ tính mục đủ thẩm định), Q-dpv2-5 (K1 cho baotu; K2 không tự động chặn cho tanso, vaynen, đủ hai chữ ký). Các mã này không dùng lại."
- **Nếu Astra không ký K2:** giữ Q-dpv2-5, chỉ còn phần `tanso`/`vaynen`, ghi lập trường Opus như mục 3.4.
- **Q-dpv2-6** (nếu còn phải gửi):
  - Context: ghi "Opus đã đổi lập trường về đại lục (giữ có cờ) để áp một nguyên tắc cho cả sáu";
  - Recommendation: thay bằng "Opus chọn 1 cho cả sáu. Astra chọn 2 cho năm mục đầu và 1 cho đại lục.";
  - Options: thêm hệ quả "1 → N = 237; 2 → N = 231; 3 → N từ 231 đến 237";
  - Evidence: sửa trích dẫn `O\round-1-cross-review.md:102–114` thành `:106–110` và `:113`.
- **Căn cứ:** mục 3.

**8. Q-dpv2-1: thêm phạm vi và chi phí.**
- **Vị trí:** cuối đoạn Context (dòng 14).
- **Thêm đoạn sau** (số liệu V, diễn giải A):

  > **Phạm vi và chi phí nếu hậu kiểm.**
  >
  > - H5: chỉ *chòng chành* có nguồn ghi là cùng từ với một mục khác khóa (*tròng trành*). Opus đã rút suy luận *hì hục ↔ hì hụi*. Bộ sinh biến thể thô cho 632 cặp trên 474 từ chính (`O\evidence\bien-the-chinh-tho.tsv`). Phần lớn các cặp này là từ khác nhau, nên phải đọc từng cặp.
  > - H7: bảng còi `U\canh-bao-khong-dau.tsv` (227 dòng, 117 khóa) thiếu *báo tử*, dù PPM gộp 0,385 ≥ 0,3, vì bộ lọc từ vựng đỏ không bắt được; cổng P2 cũng cho *bao tử* H7 PASS (`U\cong-opus-v4.tsv:4156`). Trên danh sách chính có 1.177 cặp đọc khác (634 khóa) đạt mốc PPM mà không có dòng nào trong bảng còi (`O\evidence\pham-vi-hau-kiem-h7.tsv`). Chưa biết cặp nào thuộc nhóm đỏ.
  > - Hệ quả cho người dùng: H5 tồn tại vì người dùng có thể gõ dạng kia (`AT\tieu-chi-thong-nhat.md:133`). Ai nhớ *tròng trành* sẽ gõ khác khóa với *chòng chành*. Muốn thay một mục chính thì cần câu viết sạch, qua D6/D7/D8 và đúng ngăn P6.

- **Options:** thêm hệ quả cho hai phương án đầu:
  - (1) "không tốn thêm; *chòng chành* giữ nguyên cùng rủi ro trên; không biết bảng còi còn sót ca nào";
  - (2) "bước đầu chỉ đánh giá *chòng chành*; quét 632 cặp H5 và 1.177 cặp H7 chỉ làm khi chủ giao tiếp; việc thay từ là quyết định riêng".
- **Sửa câu** "Liên hệ hì hục/hì hụi chưa được hai SA xác nhận; Astra loại hì hụi theo căn cứ khác là hè hụi, …" thành "Hai SA loại hì hụi theo họ hè hụi; không ai kết luận hì hục sai H5."
- **Căn cứ:** `OE\pham-vi-hau-kiem.log`, `OE\pham-vi-hau-kiem-h7.tsv`.

### `U\du-phong-v2-bao-cao-chung.md`

**9. Tóm tắt và dòng trạng thái.**
- **Dòng 3:** thay "Review bản chung: chờ SA-Opus" bằng "SA-Opus đã review: changes requested (O\round-1-review-drafts.md)".
- **Dòng 8:** thay bằng "Hai bên thống nhất đủ 205 tầng: **A149, B36, C14, D6**. 11 dòng chờ hòa ở nháp vòng 1 đã đóng sau review của Opus (8 A, 3 D)."
- **Dòng 11:** thay bằng "Bảng HM hồ sơ giữ 285 dòng. Tính vào HM: **N = 237** (231 nếu Q-dpv2-6 theo phương án 2), gồm 230 cùng đề cử, *tần số* (K2 đủ hai chữ ký) và sáu mục có cờ H6. Không tính 46 L3b, *chạng vạng* (chờ H5) và *bao tử* (K1)."
- **Dòng 12:** thay bằng "Câu hỏi còn mở: Q-dpv2-1 cho chủ, không chặn công việc. Q-dpv2-6 chỉ gửi SA-Fable nếu Astra không nhận phương án 1."
- **Căn cứ:** mục 3.7.

**10. Các mục §2–§4.**
- **Bảng tầng §2:** thêm hàng "Opus sau review bản chung | 149 | 36 | 14 | 6 | —" và hàng "Chung | 149 | 36 | 14 | 6 | 0".
- **Bảng "những dòng chưa hòa" (từ dòng 74):** thay bằng bảng đã hòa, gồm các cột Từ, Opus trước, Astra, Kết luận, Căn cứ (mục 3.1–3.2 của review này).
- **Bảng HM §3 (đến dòng 106):** thêm cột "Tính vào N" theo mục 3.7.
- **§4.2–§4.5:** thêm dòng đầu "**Đã đóng sau review bản chung:** …" theo mục 3.1–3.4. Giữ lập trường trước review làm lịch sử, để không xóa dấu vết bất đồng.
- **§4.6:** sửa lập trường Opus theo mục 3.5.

### `U\du-phong-v2-ke-hoach.md`

**11. Cập nhật theo các câu đã đóng.**
- **§3:**
  - hàng tầng: "Tầng đã cùng nhận | A149/B36/C14/D6; 0 CHO_HOA";
  - hàng HM: "HM | hồ sơ 285 dòng; N = 237 (231 nếu Q-dpv2-6 chọn 2)".
- **§4.1 mục 2:** thêm "Cột ket_luan_nhap phân biệt dòng tính vào N (CUNG_DE_CU_CHUA_PHAT_HANH) với dòng không tính (NGOAI_HM_CHUA_THAM_DINH, NGOAI_HM_CHO_H5, LOAI_K1)."
- **§4.2:**
  - thay công thức N (dòng 118–122) bằng "N = 230 + 1 (tần số, khi đủ hai chữ ký K2) + k, với k là số mục của Q-dpv2-6 được nhận (0..6)";
  - sửa dòng 125 thành "Sau review: N = 237 (231)";
  - bỏ dòng 128 (nhánh HM có điều kiện);
  - viết dòng 127 thành quy tắc đã chốt;
  - ở dòng 129, thay ví dụ giờ cao điểm bằng "giờ cao điểm: hai SA nhận phản đối H2; mục ở lại hồ sơ L3b".
- **§5.2:**
  - `CHINH_SACH_UNG_VIEN` cố định là đoạn ở dòng 242; bỏ đoạn ở dòng 243;
  - `NGUON_NGOAI_DANH_MUC` thay bằng đúng văn bản: "L2D và các ý tưởng ngoài pool chưa đủ chứng cứ chỉ lưu ở hồ sơ, không tính là từ đã qua cổng. Không tính vào N: lô L3b (48 ứng viên đã chuẩn bị ở [`l3b-de-cu-opus.tsv`](analyzing-tools/ho-so/unified/l3b-de-cu-opus.tsv), chưa qua P2/P4/H9); *chạng vạng* (chờ xác nhận và đo họ H5 với *choạng vạng*); *bao tử* (K1: khóa `baotu` đọc thành *báo tử*).";
  - cập nhật `E\joint-publication-text.json` cho khớp.
- **§9:** thêm bốn dòng. Decided by: SA-Opus + SA-Astra; Date: 2026-11-20; Source commit: "CHUA_COMMIT — O\round-1-review-drafts.md §3 và bản sửa của Astra".
  - T-dpv2-4: "Tầng của 11 dòng chờ hòa: A cho tám mục sắc thái; D (H5c) cho hì hụi, nhão nhẹt, nhão nhoẹt."
  - T-dpv2-5: "C chỉ là nhãn cảnh báo; S4 giữ nguyên; không ban hành TT2."
  - T-dpv2-6: "HM chỉ tính mục đủ thẩm định; L3b và chạng vạng ở hồ sơ, ghi ở §12.3."
  - T-dpv2-7: "H7: baotu K1; tanso, vaynen K2 'không tự động chặn', đủ hai chữ ký."
- **§11:** bỏ rủi ro "Lệch thời điểm review" (dòng 394) vì đã khép.
- **§12:** ghi bước 1 đã xong.
- **§13:**
  - Q-dpv2-2 đến Q-dpv2-5: "Đã đóng (T-dpv2-4 đến T-dpv2-7)";
  - Q-dpv2-6: "Chờ Astra nhận phương án 1; nếu không, gửi SA-Fable";
  - OI-SCAN: ghi thêm số 632 cặp H5 và 1.177 cặp H7.
- **Căn cứ:** mục 3.

**12. Thêm bộ kiểm thứ ba vào nghiệm thu.**
- **Vấn đề:** `build_wordlist.py --check` đọc khối §10 của `WordListAnalyze.md` (`AT\build_wordlist.py:11`, `:45`), nhưng §8.2 chỉ chạy nó trên tệp chưa sửa (dòng 342).
- **Sửa:**
  - thêm vào bảng kỳ vọng §8.2 và T5 (dòng 386): "`build_wordlist.py --check` trên `WordListAnalyze.md` đã sửa, checkout CRLF: 'Ba khối khớp wordlist.txt.'";
  - ghi thêm: trên bản LF, script này lỗi ngay ở nền vì ghép khối bằng CRLF, nên không dùng kết quả ở chế độ LF.
- **Căn cứ:**
  - `OE\mo-phong-ke-hoach-crlf.log`: đạt;
  - `OE\mo-phong-ke-hoach-nen.log` và `OE\mo-phong-ke-hoach.log`: ở bản LF, cùng một lỗi `ValueError` cả trước và sau sửa.

**13. Ghi rõ phạm vi và việc để sau.**
- **§2 "Ngoài phạm vi" (sau dòng 37), thêm:** "Câu trạng thái có ngày 20/11/2026 về 205 dự phòng trong hai tài liệu lưu trữ `WordListAnalyze-Opus.md:265`, `WordListAnalyze-Astra.md:95`, và quyết định 10 ở `WordListAnalyze.md:153`: giữ nguyên; trạng thái hiện hành đọc ở §11 mới."
  - Lý do: hai tài liệu lưu trữ vẫn ghi "dự phòng, chưa phân tích". Nếu không nêu rõ, người triển khai có thể sửa sót hoặc sửa quá.
- **§13, thêm dòng:** "OI-BANG-PHAT-HANH | Khi có tác vụ thay từ: đăng ký các họ H5 chỉ chạm dự phòng (hì hụi/hè hụi, nhão nhẹt/nhão nhoẹt, chọc lét/chọc léc, chán phèo/chán phè) vào `spelling_families.tsv` và khóa K1 `baotu` vào `blocked_keys.tsv`. Họ tròng trành/chòng chành chờ Q-dpv2-1, vì ghi LOAI sẽ làm C5 báo lỗi trên mục chính | Để sau."
  - Lý do: hiện `check_wordlist.py` không chặn được một mục D nếu ai đó lấy từ `du-phong.txt`. Chỉ có TSV phân loại và README cảnh báo.
- **Căn cứ:** `AT\check_wordlist.py:120–137`; `OE\mo-phong-ke-hoach.log`.

## 5. Gợi ý không bắt buộc

**G1. Khoảng byte của "toàn §10".** Kế hoạch §3 (dòng 67) nên ghi rõ khoảng byte: từ đầu dòng `## 10. Danh sách 7.776 từ phát hành` đến ngay trước dòng `## 11.`. Opus đã kiểm SHA `4b91fac6…` theo đúng khoảng này.

**G2. Hai bộ mẫu số.** Nên thêm vào README §6 và §11.4 một câu: "PPM gộp của H7 theo mục 0 của tiêu chí (34.314.528/149.860.716, cũng là `counter_tokens` trong manifest); mức H8 theo tập luật P2 (34.329.387/150.070.912)."
- Cột `ppm_gop_mau_so_da_ky` trong `E\cross-review-counts.tsv` dùng bộ số mục 0, trong khi bản chung gọi bộ số P2 là "mẫu số của bộ cổng đã ký". Nên đổi tên cột hoặc ghi chú.
- Không kết luận nào đổi vì khác biệt này (mục 1).

**G3. Nguồn đổi trạng thái ở §11.1.** Thêm một câu dẫn nguồn: quyết định 10 ghi trạng thái ban đầu; yêu cầu phân tích của chủ ngày 20/11/2026 (D-dpv2-1) đổi trạng thái.

**G4. Danh sách tệp hồ sơ đưa vào Git.** Kế hoạch §7 hoặc §12 nên liệt kê các tệp hồ sơ du-phong-v2 sẽ đưa vào Git. Luật ở `AT\ho-so\README.md:17` không lưu tệp trung gian mà tài liệu không nhắc tới. Nếu thêm một dòng về du-phong-v2 vào `AT\ho-so\README.md` thì phải cập nhật `ho_so.readme_sha256` trong manifest.

**G5. Phạm vi H7 của tập cuối.** Dẫn `OE\h7-quet-bo-sung.tsv` ở báo cáo chung §1.3 hoặc §4.5. Đề nghị Astra đối chiếu hai cặp Opus ghi là không đỏ: *móng ↔ mông* và *ngoại trừ ↔ ngoại trú*.

**G6. Lý do C mượn của Astra.** Ở các dòng C chung dùng lý do của Astra (*thụp, tuổi xanh*), thêm tiền tố "Opus nhận C theo lý do của Astra:" vào `y_kien_opus`, để khỏi đọc nhầm là ý kiến của Astra.

**G7. Số ghế C/H/K.** Báo cáo chung §1.2 nên ghi rằng có 109 mục A không-F, để người đọc biết ngay số ghế C/H/K có thể thay.

## 6. Bằng chứng và lệnh của bước này

Chạy trong `OE`, vì các script dùng `chung.py`:

1. `python kiem-ban-nhap-chung.py` → `kiem-ban-nhap-chung.log`. Nội dung: dữ kiện hai TSV, số liệu sau khi đóng, dòng trích dẫn, lịch sử lượt viết của 132 mục khấu trừ, SHA vùng bảo vệ.
2. `python mo-phong-ke-hoach.py <thư mục tạm ngoài repo> [--crlf] [--goc]`, chạy đủ bốn chế độ → `mo-phong-ke-hoach.log`, `mo-phong-ke-hoach-crlf.log`, `mo-phong-ke-hoach-nen.log`, `mo-phong-ke-hoach-nen-crlf.log`. Thư mục tạm nằm trong thư mục phiên, đã xóa sau khi chạy.
3. `python pham-vi-hau-kiem.py` → `pham-vi-hau-kiem.log`, `pham-vi-hau-kiem-h7.tsv`.
4. `python h7-quet-bo-sung.py` → `h7-quet-bo-sung.tsv`.
5. `python kiem-dau-ra.py`: kiểm định dạng mọi tệp trong `O`.

Bước này không tải và không lưu văn bản kho, định nghĩa hay câu giải nghĩa. Các tệp mới chỉ chứa đầu mục, khóa, số đếm, hash và nhận định của Opus.

## Lượt duyệt 2

**Ngày:** 20/11/2026. **Bản được duyệt:** bản sửa 1 của năm tệp `U\du-phong-v2-*` (SA-Astra, Status: Draft round 1) và nhật ký `A\round-1-revision-1.md`. Opus kiểm trực tiếp trên tệp, không dựa vào nhật ký.

**Kết luận: accept.**

- Cả 13 thay đổi bắt buộc đã áp đúng (mục A).
- Opus đồng ý với Astra ở Q-dpv2-7, nên câu này đóng thành quyết định chung của hai SA, không gửi SA-Fable (mục B).
- Q-dpv2-1 đủ các trường cần cho chủ (mục C).
- Mục D liệt kê các cập nhật hệ quả khi ghi việc đóng Q-dpv2-7; đây không phải lỗi của bản sửa.

### A. Kiểm 13 thay đổi bắt buộc

Lệnh `python kiem-ban-sua-1.py` (chạy trong `OE`) → `OE\kiem-ban-sua-1.log`: 0 yêu cầu chưa đạt (V).

| # | Kết quả | Ghi chú |
|---|---|---|
| 1 | Đạt | Tám mục A/A, ý kiến Opus đúng; *ăn trầu* có câu không đưa nhận định y khoa |
| 2 | Đạt | Ba mục D, `KHONG_DUNG_H5_H9`. Ý kiến Opus bị rút gọn: bỏ nguồn ở *hì hụi* và câu kết "không dạng nào đạt 95%/20" ở hai mục *nhão*. Phần còn lại đúng; nguồn vẫn có ở cột ý kiến Astra và `bang_chung`. Chấp nhận |
| 3 | Đạt | *vậy nên*: `H7_K2`, đủ hai chữ ký (`E\revision-1-chu-ky-astra.tsv:3`) |
| 4 | Đạt | Sáu mục được tính, có cờ rà H6. Lý do cụ thể của Astra không chép vào dòng, nhưng `bang_chung` trỏ tới `OE\de-cu-hop-nhat-de-xuat-opus.tsv:78`, `:93`, `:142`, `:152`, `:252`. Chấp nhận |
| 5 | Đạt | *bao tử* `LOAI_K1`; *tần số* `H7_K2`, đủ hai chữ ký (`E\revision-1-chu-ky-astra.tsv:2`) |
| 6 | Đạt | 46 L3b và *chạng vạng* nằm ngoài N; cờ H2/X nằm ở `dieu_kien` |
| 7 | Đạt | Tệp câu hỏi chỉ còn Q-dpv2-1 và Q-dpv2-7. Astra không thêm đoạn liệt kê các câu đã đóng; thay vào đó, đầu tệp trỏ sang Decisions, còn kế hoạch §13 ghi từng mã đã đóng. Tương đương, chấp nhận |
| 8 | Đạt | Xem mục C |
| 9, 10 | Đạt | Dòng trạng thái, tóm tắt, bảng tầng, bảng 11 điểm, cột "Tính vào N", §4.2–4.6 ghi đã đóng |
| 11 | Đạt | §3, §4.1, §4.2, §5.2, §9 (T-dpv2-4..8), §11, §12, §13 |
| 12 | Đạt | Opus mô phỏng lại độc lập trên bản sửa (V). Bản LF: check 0 lỗi, verify 0 lỗi, build lỗi `ValueError` như nền. Bản CRLF: check C1, verify C1 + 2×C8, build đạt. Trùng nền và khớp `E\joint-proof.log` |
| 13 | Đạt | §2 có hai tài liệu lưu trữ và quyết định 10; §13 có OI-BANG-PHAT-HANH |

Kiểm thêm (V):

- Bảng dự phòng có 205 dòng, đúng thứ tự `du-phong.txt`.
- Bảng HM có 285 dòng, khóa duy nhất, không giao với chính hay dự phòng. N = 237 (120 D6, 10 D7, 107 R1; 236 MANH, 1 CHI_BE_MAT). HM không còn tranh chấp. Không có câu giải nghĩa trong hai TSV.
- SHA byte của ba tệp chính đúng. Không tệp đã theo dõi nào bị sửa, kể cả hai tài liệu lưu trữ.
- Tập 1.177 cặp H7 giống hệt nhau với mẫu số mục 0 và mẫu số P2 (cùng 634 khóa).
- Các gợi ý G1–G4, G6, G7 đã áp. G5 dẫn tới ca mới ở mục B.

### B. Q-dpv2-7: Opus đồng ý với Astra

**Dữ kiện (V):**

- *ngoại trừ* là dự phòng lớp F (`AT\labels.tsv:7901`), có câu đạt lịch sử ở lượt v2 (`U\du-phong-v2-phan-loai.tsv:125`). Cổng P2 cho H7 PASS (`U\cong-opus-v4.tsv:70900`, `U\cong-astra-v4.tsv:70900`).
- *ngoại trú* cùng khóa `ngoaitru`, có 9/325 lượt sạch, PPM gộp 1,215 (`U\opus-counts.tsv:15743`). *ngoại trừ* có PPM gộp 35,284 (`:7879`), gấp khoảng 29 lần.
- vi.wiktionary, trang *ngoại trú* (oldid 1879974, đọc ngày 20/11/2026), ghi đây là tính từ có hai nghĩa: học sinh ở ngoài trường (ghi trước) và bệnh nhân chữa bệnh không nằm viện. Ở đây chỉ ghi quan hệ nghĩa, không chép định nghĩa.
- Tiền lệ `U\p7-khau-tru.tsv:19`: *nội trú* bị loại ở P7 theo H6.5, có chữ ký Astra và Opus, vì nghĩa điều trị chiếm từ 20% trở lên ở web.

**Lập trường Opus:**

1. Opus rút nhận định "không phải bệnh; không đỏ" ở `OE\h7-quet-bo-sung.tsv:36`. Nhận định đó trái với tiền lệ *nội trú* mà chính Opus đã ký. Tệp evidence giữ nguyên làm ảnh chụp lượt 1.
2. Theo tiền lệ này, nghĩa điều trị của *ngoại trú* thuộc phạm vi H6.5 (A). PPM gộp 1,215 ≥ 0,3, nên còi H7 bật (`AT\tieu-chi-thong-nhat.md:160`): phải đọc và ký mức K.
3. Opus đồng ý với đề nghị của Astra: *ngoại trừ* ở **C, CHO_H7** (phương án 1, tạm quản lý như phương án 2). Mục này không dùng cho đến khi đủ hai điều kiện:
   - đo tỷ lệ nghĩa điều trị của *ngoại trú* ở web, theo đúng cách của tiền lệ *nội trú*;
   - hai SA ký K1, K2 "không tự động chặn" hoặc "không tự động" (`AT\tieu-chi-thong-nhat.md:166–168`).
4. Đánh giá sơ bộ của Opus là K2, không phải K1 (A). Lý do:
   - nghĩa đỏ không chắc, vì từ điển ghi nghĩa học đường trước;
   - cách đọc tự nhiên của khóa là *ngoại trừ*;
   - các ví dụ K1 trong tiêu chí đều là cách đọc đỏ rõ (*tự tử*, *lột da*).

   Opus chưa ký "không tự động chặn" khi chưa có số đo.
5. Hai bên đã cùng chốt trạng thái và điều kiện khép, nên Q-dpv2-7 đóng ngay ở vòng review, không gửi SA-Fable. Đề nghị ghi quyết định T-dpv2-9 (mục D).

**Hệ quả** (suy từ `OE\kiem-ban-sua-1.log`):

- Tầng thành **A148/B36/C15/D6**, không còn CHO_HOA.
- A gồm 109 mục không-F và 39 mục F. C gồm 13 mục không-F và 2 mục F (*trở lên*, *ngoại trừ*).
- N HM vẫn là 237. Danh sách chính không bị ảnh hưởng.

### C. Q-dpv2-1: đủ các trường cho chủ

| Trường | Có | Ghi chú |
|---|---|---|
| Decision needed | Có | Ba lựa chọn rõ |
| Context | Có | Câu về *hì hục* đã sửa đúng |
| Phạm vi và chi phí | Có | 632 cặp/474 từ (H5); 1.177 cặp/634 khóa (H7); bảng còi 227 dòng/117 khóa; tổng 1.809 bản ghi; ca *báo tử* kèm `U\cong-opus-v4.tsv:4156`. Chi phí được ghi bằng khối lượng việc, không quy ra giờ hay credits vì chưa có cơ sở. Chấp nhận |
| Evidence | Có | Cả 11 đường dẫn đều tồn tại (V) |
| Options và hệ quả | Có | Cả ba phương án đều có hệ quả |
| Recommendation | Có | Opus chọn 2. Astra ưu tiên không mở thêm việc, nhưng nhận 2 nếu chủ giao |
| Blocked | Có | Chỉ chặn việc mở rộng hậu kiểm hoặc thay danh sách chính |
| Answer | Trống | `**Answer (owner, <date>):**` |

Opus không đề nghị sửa Q-dpv2-1. Gợi ý E5 chỉ là tùy chọn.

### D. Cập nhật hệ quả khi ghi việc đóng Q-dpv2-7

Đây là việc ghi quyết định chung, không phải lỗi của bản sửa 1.

1. `U\du-phong-v2-phan-loai.tsv`, dòng *ngoại trừ*:
   - đặt `tang_opus=C`, `tang_chung=C`, `tranh_chap=KHONG`, `cau_hoi=-`; giữ `ma_van_de=H7;D8_CHUA_CO` và `trang_thai_h=CHO_H7`;
   - trong `con_thieu`, thay "Khép H7" bằng "Khép H7: đo tỷ lệ nghĩa điều trị của ngoại trú như tiền lệ nội trú, rồi hai SA ký K1/K2/không tự động";
   - thay `y_kien_opus` bằng "C/CHO_H7: Opus rút nhận định không phải bệnh nên không đỏ (h7-quet-bo-sung.tsv:36) vì trái tiền lệ nội trú (p7-khau-tru.tsv:19). Còi bật (PPM gộp 1,215 ≥ 0,3). Opus nghiêng K2, chưa ký trước khi đo."
2. `U\du-phong-v2-cau-hoi.md`: bỏ Q-dpv2-7, chỉ còn Q-dpv2-1.
3. `U\du-phong-v2-bao-cao-chung.md`:
   - tóm tắt: tầng A148/B36/C15/D6, không còn CHO_HOA; chỉ còn Q-dpv2-1;
   - §1.2: hàng mức A ghi "109 không-F + 39 F; ngoại trừ ở C/CHO_H7";
   - §2: thêm hàng "Sau đóng Q-dpv2-7 | 148 | 36 | 15 | 6 | 0" và thêm *ngoại trừ* vào danh sách C;
   - §4.7: đổi thành "đã đóng, T-dpv2-9", ghi lập trường như mục B.
4. `U\du-phong-v2-ke-hoach.md`:
   - §3: "Tầng hiện tại | A148/B36/C15/D6; 0 CHO_HOA";
   - bỏ các câu nói bảng hay tầng dự phòng còn chờ Q-dpv2-7 (§4.1, §4.2, đầu §5, cuối §5.2);
   - §9: thêm hàng T-dpv2-9 "Ngoại trừ ở C/CHO_H7: nghĩa điều trị của ngoại trú thuộc phạm vi H6.5 theo tiền lệ nội trú, còi H7 bật; không dùng cho đến khi đo tỷ lệ nghĩa và hai SA ký mức K", người quyết định SA-Opus + SA-Astra, ngày 2026-11-20;
   - §13: Q-dpv2-7 thành "Đã đóng: T-dpv2-9"; thêm hàng "OI-H7-NGOAITRU | Đo tỷ lệ nghĩa điều trị của ngoại trú ở web như tiền lệ nội trú, rồi hai SA ký K1/K2/không tự động | Để sau; chỉ cần khi muốn dùng ngoại trừ".

### E. Gợi ý không bắt buộc

1. Ba dòng D: khôi phục phần bị lược trong `y_kien_opus`, gồm nguồn en.wiktionary oldid 93445969 ở *hì hụi* và câu "không dạng nào đạt 95%/20" ở hai mục *nhão*.
2. *thụp*, *tuổi xanh*: bỏ chữ "Astra:" bị lặp trong `y_kien_opus` ("…theo lý do của Astra: Astra: …").
3. Kế hoạch §9: thống nhất cách ghi `pending` với `CHUA_COMMIT` của các hàng cũ.
4. `E\revision-1-artifacts.tsv`: dựng lại trước khi stage, để có bốn tệp mới của lượt này (`kiem-ban-sua-1.py`, `kiem-ban-sua-1.log`, `mo-phong-ke-hoach-sua-1.log`, `mo-phong-ke-hoach-sua-1-crlf.log`).
5. Q-dpv2-1: có thể ghi *ngoại trú* là ca thứ hai mà bảng còi có thể đã bỏ sót. Ca này chưa được xác nhận cho đến khi đo.
6. Sáu HM có cờ: ghi nhóm H6 ngay trong `dieu_kien` (ví dụ "rà H6.1, nghĩa quân sự"), để bảng công bố tự nói rõ mà người đọc không phải lần theo `bang_chung`.

### F. Bằng chứng của lượt này

Chạy trong `OE`:

1. `python kiem-ban-sua-1.py` → `kiem-ban-sua-1.log`.
2. `python mo-phong-ke-hoach.py <thư mục tạm ngoài repo> --nhan sua-1 [--crlf]` → `mo-phong-ke-hoach-sua-1.log`, `mo-phong-ke-hoach-sua-1-crlf.log`. Nền không đổi nên dùng lại `mo-phong-ke-hoach-nen.log` và `mo-phong-ke-hoach-nen-crlf.log`. Thư mục tạm đã xóa.
3. `python kiem-dau-ra.py`: kiểm định dạng mọi tệp trong `O`.

Lượt này không tải và không lưu văn bản kho, định nghĩa hay câu giải nghĩa. Trang Wiktionary chỉ được đọc để ghi quan hệ nghĩa.

## Lượt duyệt 3 (ký kế hoạch)

**Ngày:** 21/11/2026. **Bản được duyệt:** năm tệp `U\du-phong-v2-*` ở working tree. So với `1734b43`, chỉ kế hoạch, báo cáo chung và tệp câu hỏi đổi; hai TSV không đổi. Opus cũng đọc nhật ký `A\round-1-revision-1.md`.

**Kết luận: changes requested.** Trả lời của chủ được ghi đúng (mục A). Dữ liệu, Decisions, điểm neo và tương thích checker đều đạt (mục B, C). Còn **một thay đổi bắt buộc**: hai bảng công bố và bảng cảnh báo ở §11 chưa mang lý do tầng của các mục C và D (mục D). Opus sẽ ký Final ngay khi thay đổi này được áp; chỉ cần kiểm lại riêng điểm đó.

### A. Trả lời của chủ cho Q-dpv2-1: accept

- Câu trả lời "3" tại `1734b43:analyzing-tools/ho-so/unified/du-phong-v2-cau-hoi.md` khớp nguyên văn phương án 3: mở yêu cầu riêng để rà/thay danh sách chính, không làm trong dự phòng v2 (V).
- D-dpv2-5 ghi đúng ý đó. Hệ quả đã có đủ trong kế hoạch: một gạch ở §2 "Ngoài phạm vi", rủi ro ở §11, bước 2 và 6 ở §12, các dòng OI-RA-THAY-CHINH và OI-SCAN ở §13. Báo cáo chung §4.1 ghi quyết định; tệp câu hỏi ghi "Không còn câu hỏi mở." (V).
- Không cần hỏi thêm chủ. Phạm vi và chi phí của yêu cầu riêng sẽ được chốt khi yêu cầu đó được mở, ngoài kế hoạch này.

### B. Kiểm trạng thái cuối

Lệnh `python kiem-ky-ke-hoach.py` (chạy trong `OE`) → `OE\kiem-ky-ke-hoach.log`: 0 mục chưa đạt (V).

- **Dữ liệu:**
  - hai TSV không đổi so với `1734b43`; tầng A148/B36/C15/D6, không còn CHO_HOA, tranh chấp hay câu hỏi;
  - HM có 285 dòng hồ sơ, N = 237;
  - dòng *ngoại trừ* đúng Lượt duyệt 2 §D; gợi ý E1 và E2 của lượt 2 đã áp.
- **Decisions:**
  - 14 hàng (D-dpv2-1..5, T-dpv2-1..9), mã duy nhất, đủ năm ô;
  - D-dpv2-* do chủ quyết, T-dpv2-* do hai SA quyết;
  - commit `1734b43` và `cefb993` tồn tại; không còn `pending` hay `CHUA_COMMIT`.
- **Điểm neo cho người triển khai:** mỗi neo xuất hiện đúng một lần.
  - Trong `WordListAnalyze.md`: dòng `> - **Dự phòng:**` và dòng 11 của mục lục; §11 là mục cuối.
  - Trong `AT\README.md`: hàng `du-phong.txt` và tiêu đề `## Cập nhật danh sách`.
- **Vùng bảo vệ:** SHA byte của ba tệp chính đúng; chỉ tệp hồ sơ bị sửa.
- **Mô phỏng lại** (`mo-phong-ke-hoach.py --nhan ky-3`), kết quả trùng nền ở cả hai chế độ:
  - bản LF: check 0 lỗi, verify 0 lỗi, build `ValueError`;
  - bản CRLF: check C1, verify C1 + 2×C8, build đạt.

### C. Kế hoạch đã đủ để triển khai chưa

| Phần | Kết luận | Ghi chú |
|---|---|---|
| Gạch đầu dòng và mục lục của `WordListAnalyze.md` | Đủ | Văn bản chính xác; neo duy nhất |
| §11–§12 | Đủ, trừ `BANG_CANH_BAO` | Mẫu cố định; token tất định. Số người triển khai phải ra được nêu sau bảng này |
| `AT\README.md` | Đủ | Hàng thay, hai hàng mới và mục mới đều có văn bản chính xác |
| Hai TSV mới ở `AT` | Thiếu lý do tầng | Thay đổi bắt buộc D.1 |
| `manifest.json` | Đủ | Trường thay, trường giữ và cách băm đã rõ; số cuối lấy từ TSV |
| Nghiệm thu | Đủ, cần thêm một kiểm | Thêm T10 (D.1) |
| Decisions | Nhất quán | Xem mục B |
| Câu hỏi mở | Không còn | |

Số người triển khai phải ra (V, `OE\kiem-ky-ke-hoach.log`):

- `BANG_TANG` (OK không-F / OK-F / tổng): A 109/39/148, B 0/36/36, C 13/2/15, D 6/0/6.
- `BANG_CANH_BAO`: 21 dòng C/D. Không có mục A/B nào mang trạng thái riêng.
- `BANG_NHOM_HM`: 120 D6_CUOI, 10 D7_CUOI, 106 R1, và 1 R1 có H7_K2.
- `BANG_TU_HM`: 237 dòng.

### D. Thay đổi bắt buộc

**1. Lý do tầng phải có trong bảng công bố và trong §11.**

- **Vấn đề:**
  - Bảng công bố `AT\du-phong-phan-loai.tsv` bỏ hai cột ý kiến, và kế hoạch §4.2 (dòng 113) chỉ định nghĩa `ghi_chu` cho các dòng có câu hỏi đã đóng.
  - Vì vậy sáu mục C không còn lý do tầng nào trong cột công bố: `ma_van_de` của chúng chỉ là `D8_CHUA_CO`, chung cho mọi dòng. Đó là *chễm chệ, lỗi hẹn, mỏng tanh, thụp, tuổi xanh* và *trở lên* (mục này còn thêm `CHUA_VIET`). *lời lỗ* mất ý gần nghĩa với *lỗ lãi*.
  - Sáu mục D chỉ có mã `H5`, không nêu từ cùng họ.
  - `BANG_CANH_BAO` (§5.2, dòng 242) không có cột lý do.
  - Chủ yêu cầu phân tầng kèm lý do, và hai SA đã thống nhất "thêm một bảng ngắn cho D, C có lý do" (`O\round-1-cross-review.md:129`). Theo kế hoạch hiện tại, lý do chỉ còn truy được qua con trỏ `bang_chung` vào hồ sơ.
- **Sửa kế hoạch:**
  - **§4.2:** thay gạch `ghi_chu` của bảng dự phòng bằng: "`ghi_chu`: lý do tầng/trạng thái đã thống nhất, một câu ngắn, không trích nguồn. Bắt buộc với mọi dòng C, D và mọi dòng có quyết định T-dpv2-*; nêu từ đối chứng khi lý do là H5, dễ lẫn hoặc gần nghĩa. Các dòng khác ghi `-`. Văn bản lấy đúng bảng ở `O\round-1-review-drafts.md`, Lượt duyệt 3 §D." Định nghĩa `ghi_chu` của bảng HM theo cùng nguyên tắc.
  - **§5.2:** thay quy tắc `BANG_CANH_BAO` bằng: "21 dòng C/D theo O1; cột `Từ | Tầng | Lý do | Việc còn thiếu`; Lý do = `ghi_chu`, Việc còn thiếu = `con_thieu`. Không viết giải nghĩa." Nếu `E\joint-build.py` dựng bảng này thì cập nhật cho khớp và giữ `--prove` đạt.
  - **§10:** thêm T10: "`du-phong-phan-loai.tsv` có 30 dòng mang `ghi_chu` đúng bảng đã chốt (8 A, 1 B, 15 C, 6 D) và 175 dòng `-`; `honorable-mentions.tsv` có 8 dòng mang `ghi_chu`, 229 dòng `-`; `BANG_CANH_BAO` có 21 dòng và cột Lý do."
- **Văn bản `ghi_chu` cho bảng dự phòng** (O1; dấu `—` là gạch ngang trong ô):

| Từ | `ghi_chu` |
|---|---|
| ăn nhịp | C: chứng liệu yếu — tổng chứng liệu 0 ở bốn kho; H8 theo ngoại lệ hai chữ ký |
| ăn trầu, bèo bọt, chấp nhặt, giở giọng, giở quẻ, mụ mị, non choẹt, tía lia | A: cảnh báo sắc thái đã rút, chưa có phản đối H6 hợp lệ (T-dpv2-4) |
| cả nghĩ | C: H8 CHI_BE_MAT — chỉ đủ mức nhờ lượt bề mặt; tổng chứng liệu 2 ở bốn kho |
| chán phèo | D: H5c — cùng từ với chán phè; chán phèo không có lượt web nên không thể đạt ≥ 95% ở cả hai kho |
| chễm chệ | C: chứng liệu yếu — tổng chứng liệu 3 ở bốn kho |
| chọc lét | D: H5c — cùng từ với chọc léc (như họ cù lét/cù léc); chọc lét không có lượt web nên không thể đạt ≥ 95% |
| cửu chương | C: H8 YEU — tổng chứng liệu 6 ở bốn kho |
| hì hụi | D: H5c — cùng từ với hè hụi; hì hụi không có lượt sạch nào nên không thể đạt ≥ 95% (T-dpv2-4) |
| loằng ngoằng | C: chờ H5 — dạng loằn ngoằn (khác khóa) chưa xác nhận cùng từ và chưa đếm |
| lỗi hẹn | C: dễ lẫn với lỡ hẹn (danh sách chính) cả nghĩa lẫn âm |
| lời lỗ | C: H8 YEU; gần nghĩa lỗ lãi (dự phòng) — dùng lỗ lãi trước |
| mỏng tanh | C: gần nghĩa mỏng dính (dự phòng) — dùng mỏng dính trước |
| ngoại trừ | C: chờ H7 — ngoại trú có nghĩa điều trị (H6.5, tiền lệ nội trú), PPM gộp 1,215 ≥ 0,3; đo tỷ lệ nghĩa rồi hai SA ký mức K (T-dpv2-9) |
| nhão nhẹt | D: H5c — cùng từ với nhão nhoẹt; không dạng nào đạt ≥ 95% với ≥ 20 lượt (T-dpv2-4) |
| nhão nhoẹt | D: H5c — cùng từ với nhão nhẹt; không dạng nào đạt ≥ 95% với ≥ 20 lượt (T-dpv2-4) |
| tạnh ráo | C: H8 YEU — tổng chứng liệu 2 ở bốn kho |
| thẳng đơ | C: H8 YEU — tổng chứng liệu 1 ở bốn kho |
| thụp | C: từ đơn, thường cần cụm đi kèm để nhận ra |
| tối mù | C: H8 CHI_BE_MAT — chỉ đủ mức nhờ lượt bề mặt; tổng chứng liệu 2 ở bốn kho |
| tròng trành | D: H5c — cùng từ với chòng chành (danh sách chính); cả họ dưới 20 lượt mỗi kho; mục chính chuyển sang yêu cầu riêng (D-dpv2-5) |
| trở lên | C: chỉ khác trở nên (danh sách chính) ở l/n, dễ gõ nhầm khóa; chưa có câu |
| tuổi xanh | C: sắc thái văn chương hơn giao tiếp thường |
| vậy nên | B: H7 K2 — vảy nến hiếm (PPM gộp 0,253); hai SA ký không tự động chặn (T-dpv2-7) |

- **Văn bản `ghi_chu` cho bảng HM** (229 dòng còn lại ghi `-`):

| Từ | `ghi_chu` |
|---|---|
| cơ quan | T-dpv2-8: rà H6.3 (nghĩa cơ quan nhà nước) trước khi dùng |
| dự bị | T-dpv2-8: rà H6.1 (nghĩa quân sự) trước khi dùng |
| đại lục | T-dpv2-8: rà H6.3 (cách dùng Trung Quốc đại lục) trước khi dùng |
| lên chức | T-dpv2-8: rà H6.3 (quyền lực nhà nước) trước khi dùng |
| lực lượng | T-dpv2-8: rà H6.1 (liên tưởng quân sự) trước khi dùng |
| tần số | T-dpv2-7: H7 K2 — tận số hiếm (PPM gộp 0,207); hai SA ký không tự động chặn |
| truy tìm | T-dpv2-8: rà H6.2 (ngữ cảnh tố tụng) trước khi dùng |
| vây cá | H8 CHI_BE_MAT; đã đọc kiểm đúng nghĩa ở P4 |

- **Căn cứ cho số liệu:** các lý do lấy đúng nội dung đã thống nhất trong cột ý kiến của hai TSV hồ sơ và các quyết định T-dpv2-*. Với ba mục *chán phèo, chọc lét, hì hụi*, đối chứng chưa được đo, nên chỉ ghi rằng dạng dự phòng không thể đạt ngưỡng; không suy rằng dạng kia đạt hay trượt (theo `A\round-1-cross-review.md` §2.2). Các tổng chứng liệu lấy từ `y_kien_opus` của bảng dự phòng hồ sơ.

### E. Gợi ý không bắt buộc

1. Cột `bang_chung` trong hai bảng công bố: dùng dấu `/` và đường dẫn tương đối từ `analyzing-tools`, như `manifest.json`. Hiện chưa có TSV công bố nào chứa đường dẫn.
2. Kế hoạch §7: ghi thẳng số cuối, `du_phong.tang = {A:148, B:36, C:15, D:6}`, và thêm commit quyết định `1734b43` vào `phan_tich_du_phong`.
3. Tệp câu hỏi: thêm một tiêu đề và một câu trỏ tới `1734b43` cùng kế hoạch §9, để người mở tệp biết Q&A nằm ở đâu.
4. Thứ tự với D-dpv2-5: nên triển khai phần công bố dự phòng v2 trước, như ảnh chụp dữ liệu tại `1734b43`. Nếu yêu cầu riêng đổi danh sách chính hoặc dự phòng, yêu cầu đó phải cập nhật §11–§12, hai TSV và manifest.
5. Báo cáo chung §6: đổi chữ "Câu hỏi chỉ còn mở" thành "Tệp câu hỏi (không còn câu mở)".

### F. Bằng chứng của lượt này

Chạy trong `OE`:

1. `python kiem-ky-ke-hoach.py` → `kiem-ky-ke-hoach.log`.
2. `python mo-phong-ke-hoach.py <thư mục tạm ngoài repo> --nhan ky-3 [--crlf]` → `mo-phong-ke-hoach-ky-3.log`, `mo-phong-ke-hoach-ky-3-crlf.log`. Thư mục tạm đã xóa.
3. `python kiem-dau-ra.py`: kiểm định dạng mọi tệp trong `O`.

Lượt này không tải và không lưu văn bản kho, định nghĩa hay câu giải nghĩa.

### Kiểm lại thay đổi 4

**Ngày:** 21/11/2026. So working tree với `1734b43`. **Kết luận: accept. Opus ký kế hoạch Final.**

- **Lệnh:** `python kiem-thay-doi-4.py` (chạy trong `OE`) → `OE\kiem-thay-doi-4.log`: 0 mục chưa đạt (V). Văn bản chuẩn được đọc thẳng từ hai bảng ở §D trên, không gõ lại.
- **Hai bảng hồ sơ:**
  - mỗi bảng chỉ thêm cột `ghi_chu`; cột cũ duy nhất đổi là `bang_chung`, và chỉ được nối thêm một con trỏ tới đúng dòng của bảng §D (38/38 con trỏ đúng);
  - thứ tự từ, tầng A148/B36/C15/D6 và N = 237 không đổi; tệp vẫn CRLF, UTF-8 không BOM.
- **Ô `ghi_chu`:**
  - 30 dòng dự phòng và 8 dòng HM trùng nguyên văn §D; mọi dòng khác ghi `-`;
  - cả 21 dòng C/D đều có lý do;
  - bảng §4.2.1 của kế hoạch và `E\public-ghi-chu.tsv` (38 dòng) cũng trùng nguyên văn.
- **Kế hoạch:**
  - §4.1 ghi đúng 24/28 cột hồ sơ; schema công bố 17/20 cột giữ nguyên; định nghĩa `ghi_chu` cũ đã được thay;
  - `BANG_CANH_BAO` có cột Lý do và 21 dòng;
  - T10 kiểm trên phép chiếu công bố; phép chiếu thử cho đúng 30/175 và 8/229.
- **Phần diễn giải mới ở §4.2.1 và §11:**
  - không đổi văn bản ghi chú;
  - điểm S4 được dẫn khớp cột `diem` (lỗ lãi 5,401989 > lời lỗ 2,900190; mỏng dính 7,006689 > mỏng tanh 4,969709);
  - câu "lượt sạch chỉ hai kho OPUS" làm rõ đúng ý ô *hì hụi*.
- **Không làm hỏng chỗ khác:**
  - mô phỏng lại sau khi mẫu §11 đổi (`mo-phong-ke-hoach.py --nhan td4`) cho kết quả trùng nền ở cả hai chế độ;
  - SHA byte của ba tệp chính đúng; chỉ tệp hồ sơ bị sửa;
  - tệp câu hỏi vẫn ghi không còn câu mở.
- **Gợi ý không bắt buộc của Lượt duyệt 3:** E2–E5 đã áp. E1 (dấu `/` trong `bang_chung` công bố) chưa áp; điểm này không chặn ký.
