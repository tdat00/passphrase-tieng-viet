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
