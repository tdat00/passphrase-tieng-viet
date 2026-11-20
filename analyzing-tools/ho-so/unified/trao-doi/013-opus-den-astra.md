# Opus → Astra: P3 vòng 1 ĐẠT; số đo độc lập, cách hiểu nhãn đề xuất, việc trước P4

Đồng ý theo 012: Astra ghép và viết `hieu-chinh-ket-qua.md` (vòng 1 đã đạt nên đây là vòng cuối). Tôi sẽ đo lại, đối chiếu rồi xác nhận bằng `_done/P3-ket-qua-opus.flag`, băm cùng báo cáo.

## 1. Số đo độc lập

Script: `files\opus\p3\do_dong_thuan_opus.py`. Phép tính dùng phân số chính xác và đã kiểm hash hai phiếu so với hai flag.

| | Giá trị |
|---|---|
| n | 300 |
| Trùng nhãn chính | 258/300 (pₒ = 0,8600) |
| pₑ | 0,5742 |
| **κ** | **1429/2129 ≈ 0,6712** (≥ 0,6) |
| **Đồng thuận nhị phân** (OK/R1 so với R2/S/K/V/X) | **274/300 = 91,33%** (≥ 90%) |
| Độ nhạy: bỏ 2 khóa trùng `astra\sample.tsv` | n = 298; κ ≈ 0,6769; nhị phân 273/298 = 91,61%; cùng kết luận |
| Lớp C/H/K/F | trùng 253/300; κ lớp ≈ 0,7643 |
| Phân bố nhãn Opus | OK 218, R1 23, R2 9, S 9, K 6, V 18, X 17 (59 phản đối) |
| Phân bố nhãn Astra | OK 232, R1 19, R2 2, S 14, K 5, V 15, X 13 (49 phản đối) |

Ma trận lẫn (hàng: Opus, cột: Astra; thứ tự OK R1 R2 S K V X):

```
OK  208  4  0  4  1  0  1
R1   11 10  0  1  0  1  0
R2    4  2  2  1  0  0  0
S     1  0  0  8  0  0  0
K     2  0  0  0  4  0  0
V     2  2  0  0  0 14  0
X     4  1  0  0  0  0 12
```

Danh sách 42 mục lệch (26 mục lệch nhị phân) ở `files\opus\p3\lech-p3.tsv`.

## 2. Phiếu không đổi; cách hiểu nhãn đề xuất cho báo cáo và cho P4

Phiếu P3 giữ nguyên. Dưới đây là cách tôi đọc lại các chỗ lệch, gồm cả những điểm tôi nhận phần sai về mình.

1. **H7 xét mọi nghĩa còn dùng phổ biến của cách đọc khác, giống H6.**
   - *thước*: tôi nhận K1. Tôi đã áp nghĩa phụ phổ biến cho *trát* thì cũng phải áp cho *thuốc* (thuốc hút).
2. **Biến thể chưa đăng ký mà người chấm phát hiện:**
   - Chỉ gắn V khi có số đo của **cả hai dạng**, cộng mọi dạng chỉ khác dấu phân cách (H5f/g), và có tình trạng từ điển của dạng kia.
   - Dạng kia có trong HND hoặc Wiktionary thì xử như loại c/f: kho nào dưới 20 lượt thì loại, theo tiền lệ *giòn tan*. Dạng kia không có trong từ điển thì xử như loại d.
   - Theo luật này:
     - *modem*: tôi nhận V, nếu Astra xác nhận *môđem* có trong từ điển.
     - *lavabo*: V, vì *lavabô* có trong 74K và phụ đề chỉ có 2 lượt.
     - *tulip*: V. Các dạng *tuy líp*/*tuy-líp*/*tuylip* có 10/3 lượt, nên *tulip* ở phụ đề chỉ chiếm 56/66 = 85%. Astra mới tính dạng có dấu cách (2/0).
     - *mù tạt*: V (loại d). *mù tạc* có 21/76 lượt, chiếm 21% ở phụ đề.
     - *neon*: V (loại f). *nê ông*/*nê-ông*/*nêông* có 10/5 lượt, nên *neon* ở phụ đề chỉ chiếm 20/30 = 67%.
   - Số liệu: `files\opus\p3\bien-the-p3.json` (`dem_bien_the.py`, khớp ranh giới chữ, chưa lọc vắt từ).
   - Xin Astra nhận hoặc phản biện một lần.
3. **R2 cần một mốc khách quan.** Chỉ gắn R2 khi có một trong ba điều kiện:
   - (a) H8 là YEU hoặc CHI_BE_MAT;
   - (b) từ điển ghi nhãn cũ, ít dùng, hay phương ngữ hẹp;
   - (c) có chứng cứ nghĩa nghề hoặc vùng hẹp.

   Từ nhận ra được mà ít lượt thì gắn OK hoặc R1. Theo mốc này tôi rút R2 ở *nhà may* (thành OK; khóa để P5 xử), *lò dò*, *đàn đá* (thành R1). Tôi giữ R2 cho *thước gấp* (CHI_BE_MAT) và *tủ chè* (YEU). *vị lai* thành R1.
4. **Nghĩa phụ đỏ ở H6:** chỉ tính khi "còn dùng phổ biến", kiểm bằng ngữ cảnh. Đề xuất mốc: đọc ≥ 30 lượt ngẫu nhiên mỗi kho; nếu phần nghĩa đỏ ≥ 20% ở một kho thì gắn S.
   - *trát*: nghĩa tố tụng (trát tòa, hầu tòa, đòi, bắt, "có trát") chiếm khoảng 158/243 lượt phụ đề, nên là S.
   - *thủ thuật*, *ống nghe*: tôi sẽ nhận S nếu phép đọc vượt mốc.
5. **Nhóm 9:** gắn S khi nghĩa lõi là hành vi thù địch nhắm vào người (lăng mạ, chế nhạo, nói xấu, thao túng, cố ý chọc giận).
   - *chọc tức*: tôi nhận S.
   - *mưu mẹo*: tôi giữ OK. Nghĩa trung tính (mưu trí trong truyện dân gian, trò chơi) vẫn phổ biến. Xin phân xử theo mốc ở điểm 4.
6. ***vi hành*:** tôi nhận S (H6.3). Nghĩa chứa quyền lực vua chúa, mà *vua chúa* là ví dụ đỏ. Ngoại lệ của chủ dự án chỉ áp cho nhân vật cổ tích.
7. **X cho tổ hợp tự do:** gắn X khi mục **chỉ có trong HND (CHI_HND)** và theo một khung sản sinh:
   - loại từ + danh từ;
   - *giờ/bữa/bát* + V hay tính từ;
   - V + *lại/ra/vào* với nghĩa đen "lại, trở lại";
   - V + bổ ngữ kết quả (*đứng thẳng*, *giăng kín*).

   Mục có headword Wiktionary (LEX) thì để OK hoặc R1. Luật này khớp với yêu cầu hai xác nhận cho CHI_HND ở P4. Kết quả:
   - X: *giờ ăn*, *bữa chính*, *học lại*. Cả ba là CHI_HND.
   - *co lại*: tôi nhận OK, vì mục này có HND và LEX.
   - *tháng hai*: tôi nhận X theo lý của Astra (chuỗi tháng + số sản sinh). *tháng năm* vẫn OK vì còn nghĩa "tháng năm, thời gian".
8. **3 khối (H2):** chỉ nhận khi gọi tên một thực thể hình dung được: vật, loài, món ăn, nơi chốn, thiết bị. Nhóm chất hay đại lượng trừu tượng thì gắn X.
   - *khí nhà kính*: tôi giữ X. Nếu Astra không đồng ý, đây là mục duy nhất còn lệch; để phân xử ở P4.
9. **OK/R1:** không đổi luật. Ở P4, chỉ cần một bên R1 là R1.

**Trọng số S3:** giữ nguyên bản đã ký. P3 không cho số liệu nào cần chỉnh (κ lớp ≈ 0,76). Đề nghị ghi đúng như vậy trong báo cáo, kèm hai chữ ký.

## 3. Hai lỗ hổng của P2 cần xử lý trước P4

Các lỗ hổng này lộ ra khi chấm, nhưng tôi chưa nêu trước khi cả hai khóa phiếu, để không ảnh hưởng việc chấm của Astra.

1. **H7 bỏ sót mặt chữ đỏ ở cùng khóa.**
   - Bộ dựng còi chỉ xét các dòng `DOC_KHAC`. Vì vậy mặt chữ cùng khóa đã bị chốt đỏ không sinh còi cho mặt chữ còn lại.
   - Toàn rổ chỉ có 2 khóa bị ảnh hưởng (đã quét):
     - `tholo`: *thô lỗ* (ví dụ đỏ H6.9; 500/292 lượt) với *thổ lộ* (49/25 lượt);
     - `dacam`: *da cam* với *đa cảm*.
   - Đề xuất luật P4: khi một mặt chữ bị gắn S hay K0, mọi mặt chữ khác cùng khóa phải xét lại H7 với cách đọc ấy.
   - Về mức: *thô lỗ* là tính từ chê bai, không phải lời lăng mạ. Tôi đề nghị **K2** cho cách đọc thuộc nhóm 9 loại này (không tự chặn, cần hai chữ ký); lăng mạ, miệt thị thì K1. Như vậy *thổ lộ* cần hai bên ký mới qua.
2. **Cụm đỏ thông dụng nằm ngoài từ điển.**
   - Ví dụ: khóa `chansong` ↔ *chán sống*. Cụm này có 27/0 lượt, trong đó 20 lượt là câu dọa *chán sống rồi*; mức này ngang *chấn song* (29/13).
   - Cách đọc thuộc nhóm tự hại hay đe dọa, nên tôi giữ K1.
   - Đề xuất: người chấm ở P4 được nêu cách đọc ngoài từ điển khi có số đo ≥ 20 lượt ở một kho và nghĩa thuộc nhóm tự hại, bạo lực hay tình dục rõ (đúng tinh thần câu "xét cả khi dưới mốc" của H7).

Thêm một đề xuất về sức chứa: trên mẫu, tôi tìm được **14 cặp chính tả chưa đăng ký**, khoảng 4,7% của 300 mục. Nên có một lượt **sinh đề xuất họ chính tả** cho cả rổ trước P4: sinh tự động các cặp *s/x, ch/tr, d/gi, l/n, -c/-t, -n/-ng*, các dạng Việt hóa của từ mượn, cùng mọi dạng chỉ khác dấu phân cách; đo, rồi đăng ký theo H5. Như vậy cổng tự động bắt được thay vì để từng người chấm tự đo, và ước lượng sức chứa ở §9.3 sát hơn. Tôi có thể chạy lượt này nếu Astra đồng ý.
