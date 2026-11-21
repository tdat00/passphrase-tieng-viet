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
