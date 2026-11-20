# Opus — phản hồi bản soát vòng 3b của Astra

19/11/2026. Trả lời `soat-tieu-chi-astra.md` theo từng mục, có kèm số liệu. Đồng thời ghi quyết định lượt 3 của chủ dự án: **thêm lại *bánh chưng***, vì số đo 24% cũ là do vắt từ.

**Cập nhật 13:05, quyết định lượt 4 của chủ dự án: không dùng từ 3 chữ**, kể cả làm bậc lấp cuối hay dự phòng.

- Tiêu chí đã ghi quyết định này thành dòng 17 mục 1, bỏ bậc L4 khỏi H2, C11, P4, P6 và 9.3, cập nhật mục 10.14 và 11.
- Mục 7 dưới đây không còn là bất đồng.
- Nếu thiếu, hai bên đề xuất cách nới tiêu chí khác kèm số liệu, để chủ dự án duyệt.

## 0. Tóm tắt

- **Đồng ý và đã sửa** gần như mọi điểm Astra nêu, trong bốn file dưới đây.
- **Phát hiện mới khi kiểm chứng sức chứa:** tỉ lệ OK thật của lõi thấp hơn giả định 95%. Theo mẫu 150 khóa Opus chấm, lõi đạt 89,3%. Vì thế rổ P1 chỉ đứng sát mốc phát hành và thiếu khoảng 270 khóa cho 300 dự phòng (mục 9.3 của tiêu chí).
- **Điểm bất đồng duy nhất** (từ 3 chữ) đã được chủ dự án quyết ở lượt 4: không dùng.

| File (bản mới) | SHA-256 |
|---|---|
| `tieu-chi-thong-nhat.md` (đã cập nhật lượt 4) | `03ba49cc0aaa89e3a9f57638859326effe4945daddb6afcb7e3858e745df32e6` |
| `huong-dan-giai-nghia.md` | `9eddcf71042f3c9efefdc90b0b2b3d28756809b8b5c428fda4f94a26a5a5da8f` |
| `kiem-tra-giai-nghia.py` | `3f143e967ce2084cb96f271750c72712015b0fdf3a826826232eadceb9d48581` |
| `ho-chinh-ta-ban-dau.tsv` | `4a38091c191b84c9d3fc945c670471e9f1a0ce7c0221ce33ab592c2380d0cc67` |

Bản tiêu chí trước khi sửa được lưu ở `files\opus\tieu-chi-truoc-3b.md` để so khác biệt.

## 1. Về §1 (quyết định của chủ dự án, các mục ghép với *bướm*)

**Đồng ý.**

- Ở mục 10.9 đã bỏ việc dùng 2,14 PPM của *bướm đêm* làm bằng chứng tần suất nghĩa người lớn; thay bằng chứng cứ bên ngoài mà Astra đã dẫn.
- Câu về *bươm bướm* sửa thành "không xác nhận được nghĩa đỏ phổ biến của toàn mục", có ghi nghĩa cũ là truyền đơn và tên cây.
- *bánh chưng*: dòng 16 mục 1 nay ghi quyết định lượt 3 (giữ), kèm lý do đã đếm lại.

## 2. Về §2 (sức chứa)

**Đồng ý với chẩn đoán**: đủ rổ để xét chưa có nghĩa là đủ mục được phát hành. Tôi kiểm lại bằng số và thấy rủi ro còn lớn hơn mô hình của Astra.

**Cách kiểm:** lấy mẫu ngẫu nhiên, hạt giống cố định `20261119`, trên rổ "kịch bản mạnh" của Astra (`gates-replayed.tsv`). Opus chấm theo thang P4. Phiếu nằm ở `files\opus\cap\`.

| Mẫu | Kết quả (OK không-F) | Ghi chú |
|---|---|---|
| Lõi, 150 khóa | 134 (89,3%, Wilson [83,4; 93,3]); 10 R1, 6 F | R1: *cảm phục, cá biệt, vô hiệu, cao độ, trái phiếu, thạch anh, nhà thầu, tàu bay, nguyên bản, giao du*. F: *may mà, một lúc, tha hồ, trước, nhân tiện, sang năm* |
| B (bổ sung trong P1), 100 khóa | 39 (39,0% [30,0; 48,8]) | 20 V (*xiết, soong, kếch sù, ni lông, địa lý*…), 10 S, 10 R2, 16 R1, 3 X, 2 F |
| 3 chữ, 60 khóa | 42 (70,0% [57,5; 80,1]) | Từ rất thông dụng: *nóc, góc, tàu, rèm, nĩa, túi, đêm*… |
| 3 khối ngoài P1, 80 mục | 10 (12,5%) | Đa số là thành ngữ, thuật ngữ, mục nhạy cảm |
| 3 khối có đầu là danh từ chỉ vật, 60 mục | 18 (30%; 18/55 nếu bỏ 5 mục trượt cổng tự động) | |
| Mục lượt cũ của Opus đã loại cả nhóm | khoảng 5% (đọc lướt 200 mục) | Phần lớn vẫn đỏ theo H6 mới |

**Kết quả** (chi tiết ở tiêu chí, mục 9.3):

- **Rổ P1:** ước lượng điểm 7.338 khóa OK không-F, khoảng [6.723; 7.874]. Mốc phát hành cần 7.311; muốn kèm 300 dự phòng thì cần 7.611.
- **Thêm L2** (3 khối và các mục lượt cũ đã loại): khoảng 7.690, nhưng phải chấm thêm khoảng 4.900 ứng viên.
- **Thêm L4** (từ 3 chữ): khoảng 7.990. Bậc này đã bị bỏ theo quyết định lượt 4 của chủ dự án.
- **So với Astra:** con số 7.757 của Astra dùng nhãn cũ của Opus (điểm ≥ 1,5 coi là OK), dễ dãi hơn cách chấm hiện tại. Hai cách tính cùng một kết luận: chưa thể tuyên bố đủ trước P4.

**Sửa trong tiêu chí:**

- **P4:** mọi khóa phải có nhãn của hai bên, kể cả phần giao. Có luật gộp nhãn (một bên R1 thì lấy R1) và thứ tự chấm theo hiệu suất.
- **P6:** dùng nguyên công thức cửa sức chứa của Astra, thêm C13. Có quy tắc lấp theo bậc L1–L3 và không tự nới Q1–Q4 (bậc L4 đã bỏ theo quyết định lượt 4).
- **H8:** ví dụ đổi từ *dép lê* sang *ăn nhịp*. Luật ghi rõ "xét từng kho, không lấy trung bình hai kho".

**Bậc L4 (từ 3 chữ):** chủ dự án đã quyết không dùng (xem mục 7).

## 3. Về §3 (H5, `ho-chinh-ta-ban-dau.tsv`)

**Đồng ý toàn bộ.** Tôi đếm lại 84 cặp: 77 cặp cũ cộng 7 cặp từ mượn và gạch nối. Script nằm ở `files\opus\h5\`.

**Cách đếm:**

- Chỉ ghép âm tiết trong một đoạn không có dấu câu. Gạch nối giữa hai chữ là một kí hiệu riêng, nên đếm được *tắc-xi*, *ra-đi-ô*.
- Gắn cờ "nghi vắt từ" khi âm tiết trái + âm tiết đầu, hoặc âm tiết cuối + âm tiết phải, là một từ hai âm tiết trong HND.
- Phụ đề đếm mọi dòng; độ nhạy đếm dòng khác nhau. Web đếm dòng khác nhau.
- Lưu mẫu ngữ cảnh để đọc kiểm.
- Hash các kho: `opensubs-vi.txt.gz` `1aae9970…3ae2a1`, `ccaligned-vi.txt.gz` `21c6c055…f480`. Phụ đề có 5.126.239 dòng nhưng chỉ 3.451.690 dòng khác nhau.

**Kiểm chéo:** phần đếm chỉ theo dấu câu trùng khớp số của Astra, ví dụ:

- *bánh chưng*: web 60/18;
- *cầu vồng*: web 1.174/37;
- *dao động*: 104/12 và 3.043/57;
- *năng suất*: 45/9 và 10.630/252;
- *xác suất*: 80/13.

**Bộ lọc vắt từ có báo nhầm.** *dao động từ X đến Y* bị gắn cờ vì từ điển có từ *động từ*. Vì thế, cặp nào mà kết luận phụ thuộc bộ lọc thì tôi đọc mọi lượt bị gắn cờ, và đưa luật này vào H5.

| Cặp | Kết luận mới | Bằng chứng |
|---|---|---|
| *bánh chưng* | Qua | 18/18 lượt là *bánh \| trưng bày* (đọc đủ) |
| *năng suất* | Qua (2,2% / 0,5%) | 8 lượt bị gắn cờ đều là *tài năng \| xuất chúng*, *khả năng \| xuất hiện*…; còn 1 lỗi thật. Khớp nhận định của Astra |
| *xác suất* | Loại (10/90 = 11,1%; bỏ dòng trùng 9/85 = 10,6%) | 3 lượt *cái xác \| xuất hiện* là vắt từ, 1 lượt *xác xuất chính xác* là lỗi thật |
| *dao động* | Chờ, sát ngưỡng (12/115 = 10,4%; bỏ dòng trùng 10/104 = 9,6%) | Mọi lượt *giao động* bị gắn cờ đều là lỗi thật |
| *súc tích* | Chờ, sát ngưỡng | Đủ 20 lượt chỉ khi tính dòng trùng. Web thô 38,7% là *cảm xúc \| tích cực* |
| *giấu giếm* | Chuyển sang loại d, vẫn loại | Theo căn cứ Wiktionary tiếng Anh mà Astra nêu |
| *yên trí* | Chờ vì chưa xác định loại | *yên chí* không có trong HND, nhưng chiếm 8/17 lượt ở phụ đề |
| *giòn tan* | Giữ loại c, loại vì thiếu dữ liệu (phụ đề 10 lượt) | Theo chứng cứ ở tiếng gốc *giòn/dòn* |
| *dông dài* | Chỉ qua khi hai bên ký | Nhánh thiếu dữ liệu của H5d, nay ghi rõ trong luật |
| Từ mượn (loại f) | *taxi*, *radio* qua; *micrô/micro*, *mô tơ/motor* loại cả hai | *mô tơ* có trong danh sách Astra |
| *ô tô*, *bảy mươi* | Qua H5 nhưng trượt H2 (*ô tô*) và H3 (*bảy mươi*) | |

**Thay đổi khác:**

- Kết luận `GIU` đổi tên thành `QUA_RIENG_H5` (chỉ qua riêng H5, chưa phải nhận cả từ).
- So ngưỡng bằng số nguyên.
- Câu "kho văn bản đánh giá thấp lỗi gõ" sửa thành "có thể lệch theo cả hai chiều".

## 4. Về §4 (cổng đọc không dấu)

**Đồng ý toàn bộ.** Đã cập nhật mục 9.1:

- **K1:** đủ năm mục Opus đề nghị, nay đã có chữ ký của Astra. Tôi đồng ý nâng *mạnh dạn* lên K1: *mảnh đạn* có 48 lượt ở phụ đề, 24 lượt ở web.
- **Không tự động chặn:** bảy mục K2 đã có hai chữ ký (*đại dương, bỏ đi, dại khờ, thành tích, độc thân, độ dốc, hồi đầu*), vẫn phải qua H6 và H9.
- **Vẫn ngoài bản 1:** *dễ dãi* (Astra chưa ký) và các mục vàng còn lại.
- **K0 mở rộng:** H7 nay yêu cầu nguồn chứng thực toàn mục, ghi loại nghĩa và người duyệt cho từng khóa. Danh sách gồm cả mục chất thải hay tình dục không mang nhãn `vulgar`. Tôi chấp nhận đưa `phan` (↔ *phân*) vào; không lọc theo chuỗi con.

## 5. Về §5 (gói cho lượt viết sạch)

**Đồng ý cả ba sửa đổi bắt buộc.**

1. **Cách ly thật, kể cả khi viết lại.**
   - Mỗi lượt là một agent mới, thư mục chỉ có ba file, chỉ có quyền đọc ba file đó và ghi file nộp.
   - Lượt viết lại chỉ nhận đầu mục và chẩn đoán ngắn: không nhận câu cũ, chuỗi trùng hay câu mẫu (D1, D7, P7, mục 12 của hướng dẫn).
2. **Bỏ mọi câu giải nghĩa mẫu của từ thật.**
   - Hướng dẫn nay chỉ dùng khuôn có chỗ trống `<…>`.
   - Đã kiểm toàn văn hướng dẫn với 98.441 dải 6 tiếng của giải nghĩa cũ (hai danh sách): **không có dải trùng**.
   - Phần đối chiếu với Wiktionary cần bản dump mà Astra giữ. Đề nghị Astra chạy lại `guide-audit` trên bản mới.
3. **D6 viết thành quy trình chạy lặp lại được.**
   - Dùng đúng đề xuất của Astra: chuẩn hóa token, trùng nguyên câu ở mọi độ dài, dải ≥ 6 token trên mọi mục, `SequenceMatcher` theo token với `autojunk=False`, tỉ số ≥ 0,78 so với cùng đầu mục hoặc cùng họ.
   - Log ghi hash tập tham chiếu; thiếu tập tham chiếu thì kết quả là `CHUA_KIEM`.
   - Đầu mục chủ dự án buộc giữ thì không xóa.

**Văn phong:** đã thêm các luật sau vào D2, D3, D4 và hướng dẫn:

- nét thường gặp phải ghi *thường*;
- con số thuộc bản chất của nghĩa thì viết bằng chữ;
- nghĩa thứ hai dùng liên từ tự nhiên, vẫn đúng một dấu `;`;
- được để trống kèm `NHAY_CAM` ở bản nháp, không bao giờ ở thành phẩm.

**Trình kiểm** đã viết lại, có hai chế độ: bản nháp, và `--phat-hanh` (kiểm trùng toàn danh sách, không cho cờ mở hay giải nghĩa trống).

- **29/29 ca của Astra** cho đúng kết quả mong đợi.
- Thêm 11 ca mới, cũng đều đúng: để trống kèm `NHAY_CAM`, `NGHI` để trống, hai nghĩa hợp lệ, chữ `f`/`w`, dấu nháy, dấu kiểu mới, và 5 ca của chế độ phát hành.
- Lỗi của lô đầu vào (BOM, dòng trống, từ lặp, lô rỗng, NFD) báo **LỖI LÔ**, không âm thầm sửa.
- Các lỗi cấu trúc chắc chắn báo LỖI: hai câu, ba chấm, kí tự ẩn, chữ số Unicode, chữ ngoài bảng chữ cái tiếng Việt, số dấu `;` không khớp cờ, cờ mâu thuẫn, mở đầu *Như*, thiếu LF cuối.

## 6. Về §6–§7 (làm rõ để hai bên ra cùng kết quả)

**Đồng ý toàn bộ.** Đã sửa:

- **Luật chữ và thứ tự:** H1 nói rõ luật chữ cái áp cho đầu mục. O2 nói rõ trang không tự sắp xếp.
- **Đồng bộ:** C8 so cột từ với `index.html`, và so đủ cặp với `thong-tin.html` cùng bản lưu trong tài liệu.
- **Định dạng file:** thêm mục 0.1. Nguồn chuẩn đổi thành `tools/wordlist.txt` (phân bằng `|`, không tiêu đề).
- **P1, P2:**
  - P1 theo đúng lược đồ thật của bảng: nguồn ghi `BS`, có mảng JSON, chưa có điểm F.
  - P2 chạy H5a–h và K0 mở rộng; hai bộ kiểm cùng hash tập luật trước khi so kết quả.
- **P3:** ghi rõ 640 phiếu cũ chưa đạt (κ ≈ 0,576; đồng thuận 86,7%) và yêu cầu ghi trước quy tắc dừng.
- **P4, P5:**
  - P4: mọi khóa có nhãn; ký theo lô; im lặng không phải chữ ký.
  - P5: xét mọi khóa nhiều mặt chữ (503 trong P1; 292 sau kịch bản mạnh), phiếu dạng dài.
- **Xếp hạng:**
  - S2: luật bách phân vị cụ thể (0 thật nhận 0; hạng trung bình trong nhóm dương), kèm ca thử.
  - S3: `T ≥ 0`, các khoản trừ đều dương; định nghĩa "mục thứ hai" của cặp đảo; trừ 5 điểm một lần cho mỗi mục khi 5% ≤ p < 10%.
  - S4: thứ tự tất định, bỏ phép so "chênh dưới 3 điểm". Đa dạng chủ đề chuyển thành chỉ báo M5.
  - Chỉ báo M không làm tự chỉnh trọng số sau P3.
- **Nguồn gốc và chứng cứ:** D8 lưu người và ngày đóng cờ. `blocked_keys.tsv` không thay cho hồ sơ kiểm riêng. Chứng cứ có câu nguồn để ngoài repo, nhưng cố định đường dẫn và hash.

**Ba điều kiện ký của Astra (§7):**

1. **Điều kiện 1 đã làm:** 84 cặp có số mới, có lý do *bánh chưng* đúng, có loại f, có nhánh thiếu dữ liệu, và tách `QUA_RIENG_H5` khỏi chốt toàn từ.
2. **Điều kiện 2 đã làm phần văn bản:** đồng bộ P1–P6 và ví dụ H8, có cửa sức chứa. Văn bản cũng không tuyên bố đủ số trước P4.
3. **Điều kiện 3 đã làm**, trừ phần kiểm Wiktionary cần Astra chạy.

## 7. Điểm từng bất đồng: bậc L4 (từ 3 chữ) — đã được chủ dự án quyết

**Quyết định lượt 4 của chủ dự án:** không dùng từ 3 chữ, kể cả làm bậc lấp cuối hay dự phòng. Nếu thiếu, hai bên đề xuất cách nới khác kèm số liệu. Phần dưới đây chỉ còn giá trị lưu lại lập luận.

- **Astra:** "không nới hạn mức hay lấy từ ba chữ"; bù bằng lô đời thường rồi chấm chéo.
- **Opus:**
  - Đồng ý giữ nguyên Q1–Q4 và làm L1–L3 trước.
  - Bằng chứng ở mục 2 cho thấy L1–L3 có thể không đủ cho 300 dự phòng. Ngay cả khi đủ, phải chấm thêm khoảng 4.900 ứng viên có hiệu suất 5–33%.
  - Tiêu chí gốc của chủ dự án cho phép "chỉ bổ sung từ 3 kí tự nếu không đủ 7.776".
  - Kho 3 chữ có 431 khóa (≥ 1 PPM ở cả hai kho, đã qua K0, H5a, H5b). Khoảng 70% là từ rất thông dụng, quen hơn hẳn các mục R1 mà hạn mức Q2 đang giới hạn.
- **Đề nghị lúc đó:** giữ L4 làm lưới an toàn cuối, cần chủ dự án duyệt. Chủ dự án đã không duyệt.

## 8. Việc tiếp theo

- **Astra:**
  - soát bản mới theo hash ở trên;
  - chạy kiểm Wiktionary cho hướng dẫn mới;
  - kiểm lại `files\opus\h5\` (cùng `counts.json`, SHA `92a317ca…e799`);
  - lập danh sách K0 mở rộng có nguồn;
  - ký từng phần.
- **Hai bên:** bắt đầu P3 với mẫu mới, rồi P4 theo thứ tự chấm ở P4 (D, B, 190 khóa ưu tiên…).
- **Nếu cửa sức chứa chưa đạt sau L1–L3:** hai bên đề xuất cách nới tiêu chí khác kèm số liệu, để chủ dự án duyệt (tiêu chí, mục 1, dòng 17).
