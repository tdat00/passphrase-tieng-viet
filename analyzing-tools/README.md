# analyzing-tools

Công cụ và hồ sơ của danh sách 7.776 từ trong [`index.html`](../index.html) và [`thong-tin.html`](../thong-tin.html). Quá trình chọn từ và bộ tiêu chí được tóm tắt trong [`WordListAnalyze.md`](../WordListAnalyze.md); bản đầy đủ các luật đã ký nằm ở [`tieu-chi-thong-nhat.md`](tieu-chi-thong-nhat.md).

Thư mục này **không** chứa văn bản kho ngữ liệu, danh sách từ Hồ Ngọc Đức (GPL), dump Wiktionary hay giải nghĩa cũ của hai phân tích ban đầu. Chỉ có danh sách phát hành, nhãn, số đếm, hash và script. Nguồn, giấy phép và hash của từng nguồn ghi ở [`manifest.json`](manifest.json).

## Tệp

| Tệp | Nội dung |
|---|---|
| [`wordlist.txt`](wordlist.txt) | **Nguồn chuẩn** của danh sách: 7.776 dòng `từ\|giải nghĩa`, UTF-8, LF, NFC, xếp theo thứ tự O1. Giải nghĩa được viết mới (MIT) |
| [`du-phong.txt`](du-phong.txt) | 90 từ dự phòng còn lại sau bản phát hành 2 (205 từ ban đầu trừ 115 từ đã vào danh sách chính, xem `WordListAnalyze.md` mục 13); giữ để đối chiếu lịch sử, đã có bảng phân loại riêng, chưa phát hành và không phải gói thay thế đã được duyệt |
| [`du-phong-phan-loai.tsv`](du-phong-phan-loai.tsv) | Một dòng cho mỗi từ dự phòng còn lại: tầng, ngăn, cảnh báo H, trạng thái nghĩa, mã H8, việc còn thiếu và nguồn chứng cứ |
| [`honorable-mentions.tsv`](honorable-mentions.tsv) | 233 từ có thể cân nhắc đã chốt phạm vi đề cử (237 trừ 4 HM đã vào danh sách chính ở bản phát hành 2); không phải dự phòng, không tự cấp quyền thay từ hoặc viết thêm nghĩa |
| [`labels.tsv`](labels.tsv) | Nhãn của từng từ chính và dự phòng: khóa không dấu, nhãn (OK/R1), lớp (C người/vật, H hành động/tính chất, K trừu tượng, F hư từ), điểm thông dụng F, điểm cộng G, khoản trừ T, điểm xếp hạng, các ngoại lệ có đủ chữ ký hai bên (H3, H5, K2) |
| [`nguon-goc-giai-nghia.tsv`](nguon-goc-giai-nghia.tsv) | Hồ sơ nguồn gốc giải nghĩa (D8), xem mục dưới |
| [`blocked_keys.tsv`](blocked_keys.tsv) | 207 khóa không dấu bị chặn (K0: trùng khóa từ tục hoặc có nghĩa phụ tục; K1: đọc tự nhiên thành từ nhạy cảm; K2_CHUA_KY: mức vàng chưa đủ chữ ký). Chỉ ghi khóa ASCII, không ghi từ tục |
| [`spelling_families.tsv`](spelling_families.tsv) | 314 cặp chính tả đã đo: số lượt mỗi dạng trong phụ đề (`sub_*`) và web (`web_*`), loại theo luật H5, kết luận |
| [`ho-so/`](ho-so/) | Bản lưu hồ sơ làm việc của hai tác tử: phản hồi, phiếu chấm, bảng khóa, kết quả cổng, log D6, khấu trừ, tin nhắn. Xem [`ho-so/README.md`](ho-so/README.md) |
| [`manifest.json`](manifest.json) | Nguồn dữ liệu (URL, giấy phép, SHA-256, số dòng, số âm tiết), hash tập luật, hash bốn lượt kiểm D6 và lần kiểm lại trên danh sách phát hành, hash mọi tệp trong thư mục |
| [`tieu-chi-thong-nhat.md`](tieu-chi-thong-nhat.md) | Bộ tiêu chí và quy trình P1–P8 hai tác tử đã ký (các tệp hồ sơ được nhắc tới nằm trong [`ho-so/`](ho-so/)) |
| [`huong-dan-giai-nghia.md`](huong-dan-giai-nghia.md) | Hướng dẫn cho lượt viết giải nghĩa "sạch" (mục 12 dành cho người điều phối) |
| [`check_wordlist.py`](check_wordlist.py) | Bộ kiểm Python: C1–C8 trên [`wordlist.txt`](wordlist.txt) và ba khối trong repo |
| [`verify.mjs`](verify.mjs) | Bộ kiểm JavaScript viết riêng: C1–C5, C8, dùng đúng hàm bỏ dấu của app |
| [`build_wordlist.py`](build_wordlist.py) | Sinh lại ba khối danh sách từ [`wordlist.txt`](wordlist.txt); xuất lô cho trình kiểm giải nghĩa |
| [`kiem-tra-giai-nghia.py`](kiem-tra-giai-nghia.py) | Kiểm hình thức giải nghĩa (D2, D5); `--phat-hanh` kiểm cả trùng nhau và cờ còn mở |
| [`d6-kiem.py`](d6-kiem.py), [`d6-tham-chieu.json`](d6-tham-chieu.json), [`d6-ho-chinh-ta.tsv`](d6-ho-chinh-ta.tsv) | Kiểm nguồn gốc giải nghĩa (D6): trùng nguyên câu, dải ≥ 6 token, độ giống ≥ 0,78 so với giải nghĩa cũ, nghĩa Wiktionary và hướng dẫn |
| [`count_corpus.py`](count_corpus.py) | Đếm số lượt và PPM của từng mục trên một kho văn bản đã tải về, không đếm vắt qua dấu câu |

## Kiểm tra

```
python check_wordlist.py
node verify.mjs
python build_wordlist.py --check
python build_wordlist.py --lo lo-kiem
python kiem-tra-giai-nghia.py --phat-hanh lo-kiem/lo-01.txt lo-kiem/lo-01.tsv
```

Cả năm lệnh phải báo 0 lỗi. Hai kiểm độc lập của đợt ra-thay-chinh, chạy từ `ho-so/unified/` (`python ra-thay-chinh-kiem-ho-h5.py`, `python ra-thay-chinh-kiem-chu-ky.py`), cũng phải báo 0 lỗi: họ H5 tách mọi dạng " / ", gói chữ ký K2 và khóa chặn so với bảng H7. [`check_wordlist.py`](check_wordlist.py) kiểm:

- C1: UTF-8 không BOM, LF, NFC, đúng 7.776 dòng `từ|giải nghĩa`;
- C2: chỉ chữ cái tiếng Việt viết thường, 4–12 chữ khi viết liền, 1–3 khối;
- C3: không trùng mặt chữ, khóa không dấu hay dạng viết hoa chữ đầu;
- C4: thứ tự O1 (so từng âm tiết; trong âm tiết so chữ cái theo `a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y`, rồi thanh ngang < huyền < hỏi < ngã < sắc < nặng), nhóm chữ cái đầu liền mạch;
- C5: không trùng khóa bị chặn, không thuộc họ chính tả bị loại hoặc đang chờ, họ thiếu dữ liệu phải có hai chữ ký H5;
- C6: mọi từ có nhãn OK/R1, R1 ≤ 388, lớp F ≤ 77;
- C7 (một phần): giải nghĩa không trùng, ≤ 110 kí tự, chữ hoa đầu, dấu chấm cuối;
- C8: khối `#wordlist` của `index.html`, `thong-tin.html` và mục 10 của `WordListAnalyze.md` khớp [`wordlist.txt`](wordlist.txt) từng dòng.

## Dự phòng và từ có thể cân nhắc

Đọc `du-phong-phan-loai.tsv` cùng `du-phong.txt`; không thay từ chỉ dựa vào thứ tự dòng hoặc tầng A. Tầng không thay nhãn OK/R1 và không sửa S4. Mục D hoặc cổng chưa khép không được dùng. R1 không tự thay ghế OK; lớp F không được vượt 77.

Mã H8 lấy từ tập luật P2 v4.1 và kết quả hai bộ cổng đã đối chiếu, gồm cả CHI_BE_MAT. Điểm F, số đếm và mức H8 là ba dữ liệu khác nhau. Mẫu số P2 là 34.329.387/150.070.912 âm tiết phụ đề/web; không sửa ngược metadata nguồn lịch sử để làm chúng giống nhau.

Khảo sát PPM gộp H7 trong hồ sơ này dùng mẫu số mục 0 của tiêu chí/manifest (34.314.528/149.860.716); nhãn H8 vẫn dùng P2. Các phép đo phải ghi rõ mẫu số, không trộn hai bộ.

Từ có thể cân nhắc chỉ là đề cử; cột trạng thái nêu rõ hồ sơ nào chưa hoàn tất. Phân tích này không thay danh sách chính, không viết câu mới và không tự hoàn tất D8.

### Kiểm trên checkout Windows

Nguồn chuẩn trong Git dùng LF. Checkout CRLF có thể làm check_wordlist.py báo C1 và verify.mjs báo C1/C8; đó không phải native PASS. Kiểm đối chứng đúng nội dung LF hoặc trong môi trường giữ LF, đồng thời lưu kết quả kiểm byte của vùng được bảo vệ. Không sửa nguồn chính hoặc nới checker chỉ để làm mất lỗi nền trong tác vụ phân tích.

## Cập nhật danh sách

1. Sửa [`wordlist.txt`](wordlist.txt) (giữ thứ tự O1; từ ghép có một dấu cách giữa các âm tiết).
2. Thêm hoặc sửa dòng tương ứng trong [`labels.tsv`](labels.tsv) và [`nguon-goc-giai-nghia.tsv`](nguon-goc-giai-nghia.tsv).
3. `python build_wordlist.py` để ghi lại ba khối trong repo.
4. Chạy các lệnh ở mục Kiểm tra.
5. Cập nhật [`manifest.json`](manifest.json) (hash [`wordlist.txt`](wordlist.txt), cột từ và các tệp đã đổi), README §5 và mục "Quy tắc chọn từ" trong `thong-tin.html` nếu tiêu chí đổi.

Từ mới (kể cả từ lấy từ [`du-phong.txt`](du-phong.txt)) phải qua lại các luật H1–H9 và hạn mức Q trong [`tieu-chi-thong-nhat.md`](tieu-chi-thong-nhat.md), có giải nghĩa viết bởi một lượt sạch theo [`huong-dan-giai-nghia.md`](huong-dan-giai-nghia.md), rồi đạt D6 và soát nội dung D7.

## Hồ sơ nguồn gốc giải nghĩa ([`nguon-goc-giai-nghia.tsv`](nguon-goc-giai-nghia.tsv))

Mỗi dòng là một từ. `trang_thai = PHAT_HANH` cho 7.776 từ đang dùng; `LOAI` cho 297 từ đã bị loại: 178 từ ở P6 và P7, 119 từ ở đợt ra-thay-chinh (cột `cong_loai`, `dot_loai` ghi luật và đợt loại; `dot_loai = ra-thay-chinh` với `cong_loai` là `H7_K0`, `H7_K1`, `H5_c`, `H5_f` hoặc `H5_CHO_LOAI`).

| Cột | Ý nghĩa |
|---|---|
| `luot_viet`, `lo` | Lượt viết sạch có câu được phát hành (`v1`: lượt đầu cho 8.076 từ; `v2`, `v3`: hai lượt viết lại; `v4-rieng`: lượt riêng cho *ròng rọc*; `rtc-v1`, `rtc-v2`, `rtc-v3`: ba lượt của đợt ra-thay-chinh cho 119 từ vào, lô `rtc-lo-01`; HM vào danh sách chính được đổi dòng `LOAI` thành `PHAT_HANH`) và lô trong lượt đó |
| `sha256_giai_nghia` | SHA-256 của câu giải nghĩa (UTF-8, đúng như trong [`wordlist.txt`](wordlist.txt)) |
| `d6_ket_qua` | Kết quả D6 của câu ở lượt đó. Hash script, tập tham chiếu và mã lần chạy của từng lượt ở [`manifest.json`](manifest.json) → `d6.cac_luot` |
| `soat_noi_dung` | Người soát nội dung (D7) ở lượt đó: `CHINH` soát chính, `DOI` soát chéo, `MAU` thuộc mẫu đo đồng thuận. Với từ `rtc` thuộc mẫu hoặc soát chéo, phiếu D7 không ghi người soát chính nên cả hai người cùng mã (`astra:MAU;opus:MAU`) |
| `co_khi_viet` | Cờ người viết gắn (`NGHI`, `TUC_PHU`, `NHAY_CAM`, `HAI_NGHIA`) |
| `dong_co` | Kết luận của từng người soát khi đóng cờ (`DONG` giữ, `LOAI` loại; `LOAI>RUT` là phản đối đã rút sau phản biện) |
| `co_phat_hanh` | Cờ còn lại trong bản phát hành (chỉ `HAI_NGHIA`) |

## Tái lập

- **Số đếm:** tải các kho trong [`manifest.json`](manifest.json) → `nguon_du_lieu`, kiểm SHA-256, rồi chạy [`count_corpus.py`](count_corpus.py) (thêm `--dedup` cho kho web CCAligned). Điểm F trong [`labels.tsv`](labels.tsv) là bách phân vị trung bình của số đếm trên bốn kho, tính trong hồ sơ làm việc với cùng ranh giới đếm.
- **D6:** tải bản trích Kaikki viwiktionary (xem [`manifest.json`](manifest.json)), lưu thành `vi.jsonl.gz` trong thư mục này, kiểm SHA-256, rồi chạy `python d6-kiem.py --input <tệp tu/giai_nghia> --log d6-log.tsv --meta d6-run.json`. Lần chạy lại ngày 20/11/2026 trên [`wordlist.txt`](wordlist.txt) (bản phát hành 1) cho 7.776/7.776 PASS. Đợt ra-thay-chinh chạy ba lượt `rtc-v1`..`rtc-v3` trên lô 143, 48 và 10 câu (`ho-so/unified/ra-thay-chinh-d6-run-*.json`, `ra-thay-chinh-d6-log-*.tsv`); lần chạy trên [`wordlist.txt`](wordlist.txt) cuối của bản phát hành 2, sau soát toàn tập T9 (22/11/2026, đủ năm nguồn ghim): 7.776/7.776 PASS, run_id `06024271e10fd70e69e46228a935b89e1a28e72f2180bcb00215ec11e2e5c39b` (`ho-so/unified/ra-thay-chinh-d6-run-ban-2.json`, `ra-thay-chinh-d6-log-ban-2.tsv`; `manifest.json` → `d6.kiem_lai_phat_hanh`). Lần chạy trước T9 (run_id `555017cb…`, 7.776 PASS) đã bị lần chạy này thay thế.

## Giấy phép

Script, [`wordlist.txt`](wordlist.txt) (kể cả giải nghĩa) và các bảng trong thư mục này theo giấy phép MIT của repo. Số đếm được rút ra từ các kho nêu trong [`manifest.json`](manifest.json); repo không phân phối lại văn bản của các kho đó.
