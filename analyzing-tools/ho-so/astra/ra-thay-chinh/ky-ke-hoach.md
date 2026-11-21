# Ký duyệt kế hoạch rà và thay danh sách chính — SA-Astra

**changes requested — 22/11/2026, `91d8ee9`.** Hai SA thống nhất tập từ và các lựa chọn của chủ dự án. Chưa thể ký Final: rổ dùng để chấm S4 vẫn chứa hai mục đã trượt hoặc chờ cổng H. Đây là lỗi kỹ thuật; không cần hỏi lại chủ dự án.

## 1. Kết quả tái tính độc lập

Từ gốc repo, chạy `python -B analyzing-tools\ho-so\astra\ra-thay-chinh\evidence\ky1-xep-lai-astra.py`. Chương trình dựng rổ từ nhãn P6/L2–L3 và cổng loại lịch sử; tính phân vị bằng phân số trên bốn kho, tính lại cả khoản trừ cặp đảo, làm tròn S4 rồi xét ngăn khi chọn. Không đọc hoặc chạy code Opus. Chỉ đọc TSV kết quả của Opus **sau** hai phép tính. Mã thoát `1` ghi nhận T7 không khớp trên rổ qua H; phép đối chứng bảng `ky1-kiem-bang.py` trả `0`.

| Phép đối chứng | Kết quả |
|---|---|
| Hạng gốc 10.133 | Khớp toàn bộ thứ tự, F tới độ chính xác công bố, G, T và điểm phần trăm nguyên. |
| Rổ 10.005 ghi ở kế hoạch §6 | Khớp Opus tới từng mục, vị trí, hạng toàn rổ và điểm của 116 vào + 2 dự bị + 25 HM. Đây là đối chứng cùng đầu vào, không chứng minh đầu vào đúng. |
| Rổ theo T-rtc-14, **10.003** | Khớp tập 116 ra (3 K0, 89 K1, 24 H5), tập 116 vào, dự bị *cả nghĩ → cửu chương*, 25 HM đúng thứ tự và 94 khóa chặn mới (3 K0, 91 K1). F = 77, R1 = 0, đủ 7.776 khóa. **Không khớp thứ tự 6/116 từ vào** và điểm làm tròn của 24/116. |

**Hai mục phải bỏ trước S2.** *Bao tử* (hạng cũ 3.822) đã là `LOAI_K1` cho toàn khóa `baotu`; *chạng vạng* (6.958) là `NGOAI_HM_CHO_H5` với họ *choạng vạng*. Xem `U\du-phong-v2-honorable-mentions.tsv:17,42`, `U\du-phong-v2-ke-hoach.md:280,421–422` và T-rtc-1. Cả hai còn mang nhãn lịch sử `D6_CUOI`, nhưng T-rtc-14 chỉ giữ trong rổ một mục trượt câu nghĩa **nếu đầu mục đã qua H**. Chỉ bỏ lúc chọn là quá muộn: chúng đã làm đổi phân vị của các mục khác.

| Vị trí vào | Opus, rổ 10.005 | Astra, rổ đúng H 10.003 |
|---|---|---|
| 38–39 | leo lét → đỏ chót | đỏ chót → leo lét |
| 47–48 | học tủ → xoành xoạch | xoành xoạch → học tủ |
| 66–67 | méo xệch → mau mắn | mau mắn → méo xệch |

**Điều kiện ký T7:** loại hai mục trước chấm, chạy lại chương trình Opus và so cả thứ tự VAO/DU_BI/HM; khi khớp, khóa kết quả S4 mới làm nguồn dùng chung. Sửa §6:141–151, OI-RTC-P6 và T7 (§13:484). Không nhầm 28/118 vị trí đổi so với hạng lịch sử với 6/116 đổi so với phép chấm của Opus. Không cần đổi tập từ ra/vào hoặc chính sách HM.

## 2. Rà bản hợp nhất và gói phát hành

- Diff `2cc6aec..91d8ee9`: H5 không đổi; H7 sửa đúng bốn khóa Q-rtc-O2, tham chiếu đúng chữ ký mới; bảng thay bỏ bốn dòng giả định và thêm 25 HM. Đủ 238 khóa chính/từ vào có ý kiến hai bên và 5 khóa HM có hai chữ ký K2. Với `chia`, mở rộng hai dòng hiện có hoặc thay thế hiệu lực, không tạo bốn dòng còn hiệu lực.
- **Sửa đồng bộ §9:324–325 trước Final.** Chỉ dẫn bảng chặn chưa nêu `nieu` trong K0 (H7:235); phải ghi đủ `phanbac`, `tinhkhi`, `nieu`. Danh mục họ QUA còn thiếu *giỡn/rỡn, nuốt chửng/nuốt trửng, theo dõi/theo rõi, thư giãn/thư dãn* (H5:23,34,56,59, đã chốt T-rtc-16, chưa có trong `spelling_families.tsv`). Cho T2/T3 so đúng **khóa và mã**, **họ và kết luận**, không chỉ đếm dòng.
- D-rtc-1…8 và T-rtc-1…20 phù hợp các quyết định đã ghi. Khi thay trạng thái, điền nguồn `91d8ee9` cho T-rtc-19/20. Không còn câu hỏi chính sách; dừng và hỏi lại nếu hết hàng đợi hoặc thật sự mất nguồn D6 ghim.
- Lô ≤143, O1, cách ly `rtc-v1`, tối đa hai lượt viết lại, phần D7 chồng chéo ít nhất 15, D6 đủ năm nguồn và D8 mới đều có phép nghiệm thu. Hai dự bị trước HM; không mở vượt 25. D8 có đúng dòng LOAI để chuyển cho cả 25 HM; 118 dự phòng không có dòng D8 trước đó. Cổng cuối vẫn cần duyệt riêng của chủ dự án; không coi lần rà kế hoạch này là PASS D6/D7 hay phê duyệt phát hành.
- Các bộ kiểm đã đối chiếu: C5 Python so nguyên ô, nên vẫn cần kiểm alias H5 tách `" / "` và chữ ký; JS không thay kiểm H5/H9. Chạy C1/C8 trên bản xuất LF, `build_wordlist.py --check` trên checkout CRLF; giữ tiêu đề mục 10. Schema hiện tại của `labels.tsv` không có cột `hang`: ghi điểm trong nhãn, hạng trong hồ sơ S4, không đổi schema chỉ vì cách diễn đạt §9.

`U` = `analyzing-tools\ho-so\unified`, `E` = thư mục `evidence` cạnh phiếu. Chứng cứ tái lập: `E\ky1-xep-lai-astra.json` (hai rổ, băm đầu vào, sai khác), `E\ky1-xep-lai-astra.tsv` (vị trí và điểm), `E\ky1-tu-ra.tsv`, `E\ky1-khoa-chan.tsv`, `E\ky1-kiem-bang.py` và `.json`. Không sửa hồ sơ chung hay dữ liệu phát hành.
