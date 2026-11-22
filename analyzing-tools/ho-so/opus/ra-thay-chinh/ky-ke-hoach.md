# Ký kế hoạch rà và thay danh sách chính — SA-Opus

**accept** — 22/11/2026 (lần 2), SA-Opus. Không còn điều kiện.

**Phạm vi chữ ký:**

- `ho-so/unified/ra-thay-chinh-ke-hoach.md` (`Status: Draft (round 1)`);
- báo cáo chung, tệp câu hỏi và ba TSV `ra-thay-chinh-{h7,h5,thay-the}.tsv`.

Các tệp này ở trạng thái của lượt này: gốc `91d8ee9` cộng phần sửa chưa commit.

## Lần 2: sau duyệt ký của Astra

Astra yêu cầu sửa (`ho-so/astra/ra-thay-chinh/ky-ke-hoach.md`). Opus nhận cả ba điểm và đã sửa.

- **Rổ chấm S4: Astra đúng.**
  - *bao tử* (K1 của khóa `baotu`, T-dpv2-7) và *chạng vạng* (chờ H5, T-dpv2-6) mang mã lịch sử D6_CUOI, nhưng đầu mục không qua H. T-rtc-14 chỉ giữ trong rổ những mục mà đầu mục đã qua H.
  - Đây là hai mục LOAI duy nhất trong rổ mà không phải HM (`ho-so/unified/du-phong-v2-honorable-mentions.tsv:17,42`).
  - Đã bỏ cả hai khỏi rổ. Rổ còn 10.003 mục.
- **T7 khớp:** chương trình của Opus (`evidence/xep-lai-rtc.*`) và của Astra (`evidence/ky1-xep-lai-astra.*`) khớp 143/143 dòng: vai trò, vị trí, từ, hạng, điểm (`evidence/so-t7.log`).
  - Ba cặp từ vào đổi chỗ đúng như Astra nêu: 38–39, 47–48, 66–67.
  - Tập vào, dự bị (*cả nghĩ*, rồi *cửu chương*) và thứ tự 25 HM không đổi.
  - Thứ tự này đã khóa làm nguồn chung (T-rtc-21) và ghi vào `ra-thay-chinh-thay-the.tsv` (cột `hang_S4` mới, `hang_S4_cu`).
- **Mục 9:**
  - thêm `nieu` vào K0;
  - thêm 4 họ QUA: *giỡn/rỡn, nuốt chửng/nuốt trửng, theo dõi/theo rõi, thư giãn/thư dãn*. Tổng cộng 14 họ QUA chưa có trong bảng;
  - khóa `chia`: thay hai dòng chữ ký cũ, không để bốn dòng cùng hiệu lực;
  - T2 và T3 so từng khóa và mã, từng họ và kết luận.
- **Nguồn:** T-rtc-19 và T-rtc-20 đã điền `91d8ee9`. T-rtc-21 đang ghi "chờ commit".

**Đổi để Astra xem khi ký:** mục 9, dòng `labels.tsv`.

- Bảng giữ F, G, T, `diem` như hiện có, tức rổ P6, khớp `xep-hang.tsv`. Đã kiểm: cả 7.981 dòng đều khớp.
- HM vào lấy điểm từ `xep-hang.tsv`. Không đổi schema.
- Thứ tự mới chỉ ghi ở hồ sơ S4, vì tập vào và dự bị giống nhau theo cả hai hạng. Như vậy cả bảng dùng một rổ, không lẫn điểm của hai rổ.

**Không chặn Final:**

- OI-RTC-K2-KY: ghép chữ ký vào `chu-ky.tsv` ở gói phát hành;
- Q-rtc-A3: chỉ hỏi khi bản Kaikki đã ghim bị mất.

## Phát hành

**phát hành: accept** — 22/11/2026, SA-Opus.

Gói đã kiểm là working tree trên `d78e97a`, trước commit phát hành. Script `evidence/phat-hanh-kiem.py`; mọi phép kiểm ở `evidence/phat-hanh-kiem.log` đều đạt.

- **Danh sách:** 7.776 từ, 7.776 khóa.
  - Ra 119: 116 từ cũ, cộng *phết*, *cau có*, *tụ tập*.
  - Vào 119: 115 từ VAO, bỏ *buồn thiu* và *ỉu xìu*; thêm *cả nghĩ*, *cửu chương* và bốn HM *ngân hàng, biển, côn trùng, cô giáo*.
  - Kết quả này khớp T-rtc-24, D-rtc-10, D-rtc-11.
- **Khóa chặn:** thêm 97 khóa, đúng khóa và mã (gồm `phet` K0, `cauco` K1, `tutap` K1). Không từ phát hành nào bị chặn.
- **Họ chính tả:** thêm 37 họ, gồm hai họ loại c vì thiếu dữ liệu: *buồn thiu*/*buồn thỉu* và *ỉu xìu*/*ỉu xịu*. Không từ phát hành nào thuộc họ bị cấm.
- **Chữ ký:** 310 từ phát hành có K2, mỗi từ đúng một dòng hiệu lực của Astra và một của Opus (*thầy* đã sửa). Phạm vi chữ ký của *bảng* gồm *băng*. `labels.tsv` khớp.
- **Nhãn:** `labels.tsv` có 7.776 dòng CHINH, F = 77, R1 = 0. Bốn HM vào có nhãn và điểm lấy từ `xep-hang.tsv`.
- **D8:** 7.776 dòng PHAT_HANH khớp câu (sha256), 297 dòng LOAI. Từ vào có lượt rtc-v1/v2/v3 và D6 PASS.
- **Dự phòng và HM:**
  - dự phòng 90 từ (41 A, 36 B, 3 C, 10 D);
  - HM 233 mục; không HM nào nằm trong danh sách chính.
- **Không còn phản đối:** không từ phát hành nào còn bị phiếu T9 của Opus hay Astra đề xuất thay, K0, K1 hay loại.
- **Manifest:** băm khớp working tree.
- **WordListAnalyze.md:** có D-rtc-10, D-rtc-11, T-rtc-24; mô tả K0 đủ ba loại nghĩa.
- **Bản quyền:** không thấy lời Kaikki đã đọc trong các tệp thay đổi. Kho, HND và Kaikki-en chỉ để ngoài repo và đã xóa sau khi dùng.
