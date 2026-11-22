# Ký duyệt kế hoạch rà và thay danh sách chính — SA-Astra

**accept — 22/11/2026, SA-Astra, `fc97441`.** Chấp nhận kế hoạch và các bảng hợp nhất, không còn điều kiện. Có thể đặt trạng thái Final; đây không phải phê duyệt phát hành.

| Điểm đã kiểm trên `fc97441` | Kết quả |
|---|---|
| Rổ và thứ tự T7 | Rổ 10.003 đã bỏ *bao tử* (K1) và *chạng vạng* (chờ H5) trước khi chấm. Kết quả độc lập của Astra, phần `T_RTC_14` trong `evidence\ky1-xep-lai-astra.tsv`, khớp **143/143** với kết quả Opus về vai trò, vị trí, từ, khóa, hạng và điểm nguyên; bảng `ra-thay-chinh-thay-the.tsv` khớp thứ tự, hạng mới và hạng lịch sử. |
| Tập ra và hàng đợi | Đúng 116 từ ra, 116 từ vào, dự bị *cả nghĩ* rồi *cửu chương*, kế đến 25 HM. Ba cặp vị trí 38–39, 47–48 và 66–67 đã được sửa đúng. |
| Bảng chặn và chính tả | §9 và T2 nêu đúng 94 khóa mới: 3 K0 (`phanbac`, `tinhkhi`, `nieu`), 91 K1. Trong 15 cặp H5 QUA, chỉ *bít tết/bíp tết* đã có trong bảng gốc; §9 và T3 đã bao gồm đủ 14 họ phải thêm, kể cả bốn họ của T-rtc-16. |
| Chữ ký | Đủ 238 khóa chính/từ vào và 5 khóa HM đã được hai SA ký. §9 yêu cầu thay hiệu lực hai dòng K2 hiện có của `chia`, không thêm hai dòng đang có hiệu lực song song. |
| Điểm trong `labels.tsv` | Cả **7.981/7.981** dòng (7.776 chính + 205 dự phòng) khớp `xep-hang.tsv` ở khóa, nhãn, lớp, F, G, T và `diem`. Đồng ý giữ cùng một rổ lịch sử cho các cột này, kể cả HM được nhận. Không đổi schema; khi chọn và bù ghế chỉ dùng thứ tự S4 mới đã khóa (T-rtc-21). |

Tái kiểm từ gốc repo: `python -B analyzing-tools\ho-so\astra\ra-thay-chinh\evidence\ky2-kiem-khoa.py` → mã thoát `0`. Phép kiểm đọc blob Git, không dùng thứ tự cũ của bảng hợp nhất làm kỳ vọng. Kết luận “changes requested” và mã thoát `1` của lần một chỉ áp dụng cho `91d8ee9`, không phải bản sửa này.

T-rtc-19/20 đã trỏ tới `91d8ee9`; nguồn của T-rtc-21 là `fc97441`, có thể điền khi đặt Final. Không còn câu hỏi cho chủ dự án. Việc duyệt danh sách cuối và các cổng D6/D7/D8 vẫn thuộc gói phát hành.

## Kiểm gói phát hành 2 — 22/11/2026

**phát hành: accept — 22/11/2026, SA-Astra.** Đã khép mọi điểm T8; không còn điều kiện hay phản đối đối với gói phát hành 2.

- Đối với `d78e97a`, hiệu hai tập đúng 119 ra/119 vào theo T-rtc-23/24 và D-rtc-10/11. Danh sách có 7.776 khóa, F = 77, R1 = 0. Khớp 97 khóa chặn và 37 họ mới; cả 61 khóa T9 đã ký. Với cả 310 **mặt chữ phát hành** mang nhãn K2, mỗi SA có đúng một dòng hiệu lực trên mặt chữ đó. Không còn phản đối chưa xử trong tập phát hành.
- D8 có đúng 7.776 dòng phát hành và 297 dòng loại. Câu của 119 từ vào khớp câu đã duyệt; đối lại từng hash và kết quả D6 của 7.776 từ trong lần chạy `06024271…`. Dự phòng còn đúng 90, HM còn đúng 233. Không thấy bản nguồn thô của kho, HND hay Kaikki trong danh mục tệp sẽ đưa vào Git.

| Điểm nêu ở lần kiểm trước | Cách đối chiếu |
|---|---|
| `WordListAnalyze.md:8698,8713`; `analyzing-tools\du-phong-phan-loai.tsv:75` | Ghi *chòng chành* là từ chính **bản 1**, đã ra ở bản 2 vì H5; tầng D của *tròng trành* không đổi. §11.4 ghi đã thay **119**, không phải 116. |
| `WordListAnalyze.md:8818` | Bốn HM ghi là “theo hàng đợi” nên phải là *ngân hàng, biển, côn trùng, cô giáo*, đúng như §13.4. |
| `WordListAnalyze.md:9108` | Tách số liệu lượt quét trước đối đáp (116 từ vào; Astra 3.856 cặp) khỏi tập cuối (119 từ vào). Bỏ 7 cặp ở năm mặt chữ rút, còn 3.849; kiểm trực tiếp sáu nguồn ghim và DOC_KHAC cho năm từ bù thấy 5 cặp: 4 ở *biển* và 1 ở *cô giáo*, đã có phán quyết. Tập cuối có 3.854 cặp theo cách đếm của Astra. |
| `WordListAnalyze.md:9125` | Bỏ khẳng định không còn **khóa** có bốn dòng K2 hiệu lực. Đó là tính chất của **mặt chữ phát hành**: `daydan` và `phoi` còn 4 dòng trên hai mặt chữ, `thay` còn 5; *thầy* đúng 2. Không cần rút chữ ký của mặt chữ khác. |
| `analyzing-tools\manifest.json:309` | `ho_so.so_tep` ghi 742, nhưng `git ls-files -co --exclude-standard` ở `analyzing-tools\ho-so` cho 744 đường dẫn khác nhau, gồm cả `phat-hanh-kiem.py` và `.log` của Opus. Đếm theo danh mục thực stage; băm lại các tệp công bố đã sửa. |

Tái kiểm: các dòng §11–§13 và ghi chú *tròng trành* đã đúng. Danh sách phát hành, D6 và số dòng D8 không đổi; các cổng §10 đã chạy lại đạt. Manifest ghi đúng 744 tệp hồ sơ. Băm LF của `du-phong-phan-loai.tsv` là `4a3b9253ef7e1b24bbd7ee57311746a51528fe2d15f8d4fdce3ff11580ee93c3`, khớp cả `du_phong.phan_loai_tsv_sha256` lẫn `tep`. `honorable_mentions.sha256` và 20/20 băm trong `tep` đều khớp nội dung; manifest không tự băm.
