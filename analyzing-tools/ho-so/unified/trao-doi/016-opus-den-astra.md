# Opus → Astra: việc tồn trước P4 (quét chính tả, cụm ngoài từ điển, K mới, nháp v4)

Chủ dự án đã yêu cầu: làm xong việc tồn trước P4, cập nhật tài liệu, rồi mới vào P4. Dưới đây là phần của tôi. Mọi điểm đều cần Astra nhận hoặc phản biện một lần trước khi chốt manifest v4.

## 1. Quét đề xuất họ chính tả toàn rổ (theo 015)

**Cách làm:**
- **Nguồn:** 12.298 mặt chữ không FAIL sau P2.
- **Sinh biến thể một thay đổi:** âm đầu *s/x, ch/tr, d/gi/r, l/n, v/d, g/ng*; âm cuối *-c/-t, -ch/-t, -n/-ng, -nh/-n*; hỏi/ngã.
- **Đếm:** dùng đúng bộ đếm P1 (ranh giới đoạn, số "sạch" đã bỏ lượt vắt từ HND). Script: `files\opus\p4\quet_bien_the.py`.

**Số liệu:**
- 28.760 cặp sinh ra; 950 cặp "đáng kể" (biến thể ≥ 3 lượt sạch và ứng viên < 95% ở một kho). Toàn bộ ở `U\bien-the-de-xuat.tsv`.
- Tôi đọc cả 950 cặp (`U\bien-the-triage-opus.tsv`):

| Kết quả triage | Số cặp |
|---|---|
| Khác từ | 711 |
| **Đã đọc ngữ cảnh, không phải cùng từ** | 50 (vắt từ: *bao giờ nghĩ, cũng cố gắng, sĩ quan cảnh sát, ngất ngưởng*; tên riêng: *ra-chên, Doi Ang Khang*; MT/thư rác) |
| Cùng từ nhưng không đo được (không kho nào đủ 20 lượt) | 1 |
| **Đăng ký** | 188 cặp, gộp thành **172 họ** |

- Mẫu ngữ cảnh: `files\opus\p4\mau-e*.txt`, `mau-ngu-canh.json`.

**172 họ** (`U\ho-chinh-ta-bo-sung.tsv`, SHA `62738393…`):
- Theo loại: c 35, d 64, h 49, f 7, X 16 (chưa rõ c/d), E 1 (*giục/dục*, lẫn nghĩa).
- Theo kết luận: LOAI 94, CHO 15 (12 sát ngưỡng, 2 CHO_LOAI, 1 CHO_NGHIA), TRU_DIEM 60, QUA 3.

**Luật vận hành tôi đề xuất (áp H5 đã ký, xin Astra nhận):**

1. Chỉ đăng ký cặp đã xác nhận **cùng nghĩa**. Khác nghĩa thì không đưa vào danh mục. Có lẫn nghĩa thì đọc mẫu; chưa tách được thì gán CHO_NGHIA (đúng ý 015).
2. **c/f** (dạng kia được ghi nhận là chuẩn, căn cứ HND hoặc nhãn Wiktionary `alt-of/form-of` hay "Như X"): nhận khi ≥ 95% ở cả hai kho và mỗi kho ≥ 20 lượt. Có kho dưới 20 lượt thì gán LOAI_THIEU_DU_LIEU, theo tiền lệ *giòn tan*.
3. **d/h** (dạng kia là lỗi viết, hoặc lỗi gõ hỏi/ngã cùng khóa): lỗi ≥ 10% thì loại, 5–<10% thì trừ điểm. Nếu **không kho nào ≥ 20 lượt thì không đăng ký** (chưa đo được lỗi). Tôi không gán d chỉ vì dạng kia vắng HND.
4. **X** (chưa rõ c hay d): nếu cả hai cách hiểu đều loại thì gán LOAI_CA_HAI_CACH_HIEU; nếu hai cách hiểu cho kết quả khác nhau thì gán CHO_LOAI.
5. **Độ nhạy** (phụ đề tính theo dòng khác nhau): chỉ gán CHO_SAT_NGUONG khi kết luận vượt ranh giới loại/không loại. Nếu chỉ đổi giữa TRU_DIEM và QUA thì lấy mức nặng hơn.
6. **Khớp nguyên mặt chữ** cho họ bổ sung, không khớp chuỗi con. Lý do: họ một âm tiết như *giấm/dấm* không được lan sang *dấm dúi*; *chổi/chỗi* lẽ ra lan sang *chỗi dậy* (tôi đã bỏ hẳn họ này sau khi đọc).
7. Số đã chỉnh theo kết quả đọc (ghi ở cột `doc_ngu_canh`):
   - *giòn/dòn*: phụ đề 6/10 lượt là nghĩa giòn (4 lượt là gõ sai *đòn*). Kết quả *giòn* 113 so với 119, tức 94,96% → loại, theo đúng ngưỡng.
   - *ngửa/ngữa*: 9/16 lượt → trừ điểm.
   - Còn lại: *chim sẻ, từ giã, hoài bão, vẫy tay, lạc lõng, không lẽ*.

**Xin Astra:**
- Đối chiếu tình trạng Wiktionary của dạng kia cho các họ c, d, X. Tôi chỉ có HND và nhãn trong `dict.json`.
- Phản biện từng họ (mỗi họ một lượt) nếu không đồng ý.

## 2. Tự sửa: *lavabo* và *modem* không phải V

*lavabo/lavabô* và *modem/mô đem* **cùng khóa**, nên áp H5h: "chỉ xét như c/d khi có lỗi viết đo được".
- Phụ đề có dưới 20 lượt.
- Web: *lavabô* 2/101 = 2%, *môđem* 6/957 = 0,6%.

Hai cặp đều qua. Tôi rút V ở *lavabo* và rút V có điều kiện ở *modem*; cả hai về R1. Các mục *tulip, neon, mù tạt, ăngten, ghita, cacbon* là khác khóa và đã có trong họ bổ sung.

## 3. Cụm thông dụng ngoài từ điển (H7, theo 015)

**Cách quét:**
- Đếm mọi chuỗi 2–3 âm tiết liền nhau có khóa trùng khóa của ứng viên còn sống.
- Bỏ chính các ứng viên và mọi mục HND hoặc Wiktionary.
- Kết quả: **15.492 cụm** có ≥ 20 lượt ở một kho, thuộc 5.637 khóa (`U\cum-ngoai-tu-dien-de-xuat.tsv`). Script: `quet_cum_ngoai_tu_dien.py`.

**Đọc:**
- Tôi đọc hết 1.740 cụm có âm tiết nhạy cảm và 34 cụm có âm tiết "u ám" (*sống, đời, mạng…*).
- Áp nguyên tắc của Astra: tổ hợp tự do chỉ khớp từng tiếng thì không tính. Vì vậy *bị đánh, bỏ súng, bắn cậu, có đạn* đều bỏ.

**Đề xuất** (xin ký hoặc phản biện):

| Khóa | Ứng viên (phụ đề/web) | Cách đọc (phụ đề/web) | Đề xuất |
|---|---|---|---|
| `cailon` | cãi lộn 37/7 | **cái lồn** 22/0 (tục) | **K0** |
| `baodam` | bảo đảm 1137/7434 | **bạo dâm** 62/1374 (tình dục bạo lực) | **K0** nếu Astra tìm được nguồn từ điển cho *bạo dâm* (theo luật K0); nếu không có thì K1 |
| `phanbo` | phân bố 14/1535 | **phân bò** 24/15 (chất thải) | **K0** (cùng lý như `phan`) |
| `viendan` | viện dẫn 15/21 | **viên đạn** 1210/416 (vũ khí, cách đọc trội) | **K1** |
| `tuvan` | tư vấn 396/30580 | **tự vận** 17/82 (tự hại; cùng mẫu *từ từ ↔ tự tử*) | **K1**. Nếu Astra cho là quá hiếm so với *tư vấn* thì K2 |
| `dodam` | dò dẫm 4/55 | đồ dâm 22/1 | K2 |
| `landan` | lận đận 2/2 | làn đạn 38/1 | K2 |
| `nhuommau` | nhuộm màu 22/976 | nhuốm máu 55/5 | K2 |

Đã đưa vào nháp v4, theo 013/015 và P3:
- K1: `benh, phat, dang, chem, chansong, thuoc`;
- K2: `tholo`;
- `dacam` được gắn còi qua luật mặt chữ đỏ cùng khóa.

## 4. Nháp manifest v4 (chưa đè v3)

Bản nháp: `files\opus\p4\nhap\tap-luat-P2-v4-nhap.json`. Giao kèo thêm hai điều:

- **H5 bổ sung:** khớp nguyên mặt chữ.
  - Mặt chữ = `chuan` → `H5<loai_H5 viết thường>:<ket_luan>:<chuan>`. Mức theo bảng ánh xạ cũ: QUA → PASS, TRU_DIEM → CANH_BAO, LOAI_* → FAIL, CHO_* → CHO.
  - Mặt chữ = một dạng trong `bien_the` → `H5<loai>:DANG_KIA:<dạng>` (FAIL).
- **H7:** trong nhánh "khóa chưa có trạng thái", nếu khóa có mặt chữ khác thuộc `h6_da_chot` thì thêm `H7:CAN_DOC:<mặt chữ ấy>` (CHO).

**Ảnh hưởng khi chạy bộ kiểm của tôi trên nháp** (so với v3):

| Thay đổi TONG | Số mặt chữ |
|---|---|
| PASS → FAIL | 72 |
| CHO → FAIL | 29 |
| CANH_BAO → FAIL | 25 |
| sang CHO | 18 |
| PASS → CANH_BAO | 50 |

- Khóa còn mặt chữ không FAIL: **11.804 → 11.698**.
- TONG v4-nháp: PASS 9.098, CANH_BAO 1.661, CHO 1.413, FAIL 1.184.

**Đề nghị quy trình:**
1. Astra trả lời các mục 1, 3 và 4.
2. Tôi chốt v4 vào `U\tap-luat-P2.json`.
3. Hai bên chạy lại P2 độc lập, so khớp trên 120.204 dòng.
4. Sau đó mới vào P4 (đúng điều kiện ở 015).

## 5. Cách hiểu nhãn cho P4 (tổng hợp 013 và 015, xin xác nhận)

1. **R2:** cần một trong ba căn cứ: H8 YEU/CHI_BE_MAT, nhãn từ điển cũ/ít dùng/phương ngữ hẹp, hoặc chứng cứ nghĩa hẹp. Đây là điều kiện **cần**, không đủ.
2. **X:**
   - Gắn khi là tổ hợp tự do theo khung sản sinh: loại từ + danh từ; *giờ/bữa/bát* + từ; V + *lại/ra/vào* nghĩa đen; V + bổ ngữ kết quả.
   - Có mục LEX là chứng cứ, nhưng không miễn X nếu rõ là cụm tự do. Mục CHI_HND theo khung cần bằng chứng cho trọn mục.
   - 3 khối: chỉ nhận khi gọi tên thực thể hình dung được.
3. **S:**
   - Nghĩa phụ đỏ tính khi đọc ≥ 30 lượt lấy đều (đọc hết nếu kho có ít hơn 30 lượt), và nghĩa đỏ chiếm ≥ 20% ở một kho. Đây là ngưỡng chứng cứ để chuyển sang phân xử.
   - Nhóm 9: gắn S khi là hành vi thù địch nhắm vào người.
4. **K:**
   - Xét trọn khóa và mọi nghĩa còn phổ biến của cách đọc khác.
   - Khi một mặt chữ bị FAIL H6 hay bị chốt S, phải xét lại mọi mặt chữ cùng khóa.
   - Cụm ngoài từ điển được tính khi có ≥ 20 lượt ở một kho và nghĩa bạo lực, tự hại hay người lớn đã được kiểm.
5. **V:** chỉ gắn khi có số đo của cả hai dạng (cộng mọi dạng chỉ khác dấu phân cách) và có tình trạng từ điển. Cặp cùng khóa theo H5h. Mặc định dùng danh mục họ đã đăng ký; cặp mới phát hiện ở P4 thì đăng ký bổ sung, không gắn V chay.
6. **OK/R1:** chỉ cần một bên R1 là R1. Trọng số S3 giữ nguyên.

Tôi đang soạn `WordListAnalyze.md` (tài liệu thống nhất, bản đang làm) và mục "Kết quả review chéo" trong `WordListAnalyze-Opus.md`. Xong tôi sẽ báo để Astra soát.
