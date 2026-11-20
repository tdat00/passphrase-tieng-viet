# Danh sách passphrase tiếng Việt — phương án Astra

> **Trạng thái ngày 20/11/2026:** Đây là phân tích độc lập ban đầu của Astra, đã được thay bằng [danh sách thống nhất](WordListAnalyze.md). Khối ở mục 6 chỉ để lưu trữ: lời nhắc soạn nháp có chứa nghĩa Wiktionary, nên bảng giữ điều kiện [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Không dùng các lời giải cũ này cho bản phát hành MIT.

Ngày 19/11/2026, tôi lập phương án gồm **7.776 đầu mục, 7.776 khóa**. Trong các tài liệu của dự án, tôi chỉ dùng [README](README.md) ở thời điểm đó, không dùng danh sách hay tiêu chí của phương án khác. Mục 1–4 ghi lại số liệu và phương pháp của riêng Astra; sau mục 5 là [đối chiếu với bản phát hành](#kết-quả-cuối-cùng).

## 1. Kết quả

| Chỉ số | Giá trị |
|---|---:|
| Một khối chữ (quy ước “từ đơn” trong báo cáo) | 453 |
| Hai khối | 6.986 |
| Ba khối | 266 |
| Bốn khối | 71 |
| Tổng mục nhiều khối (gọi gọn là “ghép”) | 7.323 |
| Độ dài viết liền: nhỏ nhất / trung vị / lớn nhất | 4 / 7 / 16 chữ cái |
| Độ dài trung bình | 6,97 chữ cái |
| Mục ba chữ cái bổ sung | 0 |

“Ghép” ở đây là cách đếm theo dấu cách cho ứng dụng, **không** khẳng định mọi mục đều là từ ghép về mặt ngữ pháp: có cả từ láy, tổ hợp cố định và một số quán ngữ có mục từ riêng. Số chữ cái không tính dấu cách; `ươ` là hai chữ cái, còn `ế` là một. Phân bố độ dài:

| Chữ cái | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Số mục | 538 | 902 | 1.752 | 1.931 | 1.413 | 713 | 289 | 98 | 61 | 35 | 19 | 15 | 10 |

**Entropy của lượt chọn:** `log₂(7776) = 5 × log₂(6) ≈ 12,92481` bit/mục. Bốn, sáu và tám lượt chọn độc lập có hoàn lại cho 51,70, 77,55 và 103,40 bit. Với 6 mục, thêm một chữ số ngẫu nhiên vào một vị trí từ ngẫu nhiên cộng `log₂(60)` bit, tổng khoảng 83,46 bit nếu đầu ra phân biệt được. **Tần suất chỉ để chọn danh sách, tuyệt đối không dùng làm trọng số khi sinh passphrase.** Chữ hoa đầu mục và dấu phân cách cố định không tăng entropy. Khóa không dấu duy nhất bảo toàn số lựa chọn cho *một* mục; không có dấu phân cách, hoặc dùng cùng dấu ở giữa âm tiết và giữa mục, nhiều dãy có thể hiện thành một chuỗi. Muốn giữ rõ biên, dùng chẳng hạn `_` giữa mục và để tắt phân cách nội bộ.

## 2. Tiêu chí theo thứ tự áp dụng

Đây là tiêu chí của vòng độc lập. [Bộ tiêu chí thống nhất đã ký](analyzing-tools/tieu-chi-thong-nhat.md) là căn cứ chọn từ cho bản phát hành.

1. **Đầu mục thật và hình thức hợp lệ.** Cần mục tiếng Việt trong ấn bản Wiktionary tiếng Việt, một nghĩa từ vựng và từ loại dùng được; không lấy tên riêng, chữ viết tắt, hình vị rời, tục ngữ dài hoặc chuỗi do ghép tùy ý. Không hạ chữ hoa của tiêu đề để biến tên riêng thành từ thường. Chấp nhận mục dẫn chiếu trong nhóm đồ vật quen nếu ấn bản thứ hai xác nhận nghĩa độc lập (chẳng hạn *công tắc*). Chỉ dùng chữ cái Việt viết thường ở NFC, một dấu cách ASCII giữa các âm tiết, không số, dấu nối, dấu câu, khoảng trắng đầu/cuối hay khoảng trắng kép. *Thiên nga* trong nghĩa loài chim khác với việc dùng làm tên người.
2. **Không khiến người dùng phải nhập lại một từ dễ gây khó chịu.** Loại nghĩa thường gặp về bạo lực, vũ khí, chiến sự, tội phạm, tang ma, bệnh và triệu chứng, ma túy, tình dục, xúc phạm; tránh thuật ngữ chính trị, tín ngưỡng đặc thù, định kiến và các chủ đề nhạy cảm khác. Rà cả tên từ, nhãn từ điển, nghĩa thông dụng khác và lời giải mới. Loại khóa toàn mục nếu nó trùng khóa của tiếng thô tục: so **cả chuỗi**, không dò mù quáng một đoạn con như `cu` trong mọi từ. Cơ thể, thực phẩm và sinh hoạt bình thường không mặc nhiên nhạy cảm; *vú sữa* chỉ quả khi xét nguyên cụm. Với từ nhiều nghĩa, một nghĩa tục hoặc bạo lực nổi bật vẫn đủ để bỏ; không “làm sạch” nó bằng cách cố tình chọn một nghĩa xa lạ.
3. **Ổn định khi gõ.** Loại vần mở `oa/oe/uy` có thanh gây hai vị trí dấu, thí dụ *hòa/hoà, khỏe/khoẻ, thủy/thuỷ*; không loại vô cớ một tiếng thanh ngang như *hoa*. `qu` là một trường hợp chữ viết khác, không mặc nhiên xem mọi `quy` là tranh chấp vị trí thanh; các dạng *qui/quy, quí/quý* được chặn riêng vì biến thể `i/y`. Chặn các nhóm đã biết như *lý/lí, kỹ/kĩ, mỹ/mĩ, sĩ/sỹ, giày/giầy*, thêm các cặp soát tay như *dãn/giãn* trong cùng từ, *hủ tiếu/hủ tíu, mồng tơi/mùng tơi* và các mục có cạnh tranh *mì/mỳ*. Tách lỗi hay mắc khỏi biến thể được thừa nhận: ghi một cặp để tránh không có nghĩa cả hai đều chuẩn.
4. **Ít nhất bốn chữ cái sau khi viết liền.** Phương án Astra từng để ngỏ trường hợp ba chữ nếu hết ứng viên tốt, nhưng không dùng đến. Giới hạn trên của phương án này là 16 chữ và bốn khối. Ưu tiên sinh hoạt, đồ vật, cây con, động tác, tính chất nhận biết được và kiến thức phổ thông. Vẫn giữ đủ từ trừu tượng thông dụng; dễ hình dung là tiêu chí ưu tiên, không phải lệnh loại mọi khái niệm. Không chọn chữ khó chỉ vì có trong từ điển.
5. **Độ quen và rủi ro vùng miền.** Hai kho câu độc lập, số lần nhận ra được trong cách tách dài nhất, một từ điển đối chiếu, và rà nội dung giúp chống thiên lệch tần suất báo chí. Kiểm tra hỏi/ngã, `s/x`, `ch/tr`, `d/gi/r`, `l/n`, cuối `-c/-t`, `-n/-ng`: giảm điểm nếu thay một chỗ tạo được một mục khác có căn cứ. Mục hỏi/ngã không bị cấm toàn bộ; có 1.908 mục chứa ít nhất một trong hai thanh. Riêng vòng đầu, khi hai mục đủ chuẩn chỉ khác đúng một phép đổi khu vực đã định, tôi chỉ lấy một trong hai, không mặc định cách phát âm của miền nào là sai. Vẫn có 131 mục có láng giềng được chứng thực trong từ điển/kho câu dù mục kia không được chọn. Đây là quy tắc gần đúng về chính tả, không phải mô hình phát âm mọi phương ngữ.
6. **Một khóa chỉ chọn một đầu mục dễ nhớ.** Dùng chính `s.normalize("NFD").replace(/\p{M}/gu, "").replace(/đ/g, "d").replace(/Đ/g, "D")`, sau đó xóa dấu cách. Ưu tiên mục đã xác nhận là quen, cụ thể và có nghĩa đứng độc lập trước khi so điểm. Ví dụ *diều/điều* đều ra `dieu`: giữ đồ chơi đón gió; *nội thất/nói thật* đều ra `noithat`: không thể giữ cả hai. Các nghĩa khác nhau của **cùng một cách viết** không được nhân lên thành nhiều vé. Mục ghép được lưu có dấu cách, như *dép lê*; khi sinh mật khẩu, ứng dụng mới biến thành `déplê` hoặc `dép_lê` tùy cách đặt dấu phân cách.
7. **Lời giải phải giúp nhận từ.** Chọn một nghĩa thông dụng thay vì liệt kê rất nhiều nghĩa. Ưu tiên dấu hiệu nhận biết, hoạt động hoặc công dụng; loại lời chỉ dẫn “xem mục…”, định nghĩa vòng, câu ví dụ giả làm định nghĩa, nhầm từ loại làm sai nghĩa, hay bản quá giống nguồn. Mỗi lời giải là một dòng tiếng Việt; không chứa ký tự phân cột. Không coi một mô hình tự động là bằng chứng cuối cùng về nghĩa.

## 3. Nguồn và quy trình có thể đối chiếu

| Nguồn | Cách dùng và quyền |
|---|---|
| [Wiktionary tiếng Việt qua Kaikki/Wiktextract](https://kaikki.org/viwiktionary/rawdata.html) | Nguồn đầu mục, từ loại, nghĩa, nhãn và mục chuyển hướng. Bản dump 02-10-2026, trích 03-11-2026. Ghi công cộng đồng Wiktionary và Tatu Ylönen, [Wiktextract (LREC 2022)](https://aclanthology.org/2022.lrec-1.140/). Nội dung theo [điều khoản Wikimedia §7](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use/en#7._Licensing_of_Content), chủ yếu CC BY-SA 4.0, có nội dung đồng cấp GFDL và ngoại lệ tại từng trang. |
| [Mục tiếng Việt trong Wiktionary tiếng Anh, Kaikki](https://kaikki.org/dictionary/Vietnamese/) | Bản enwiktionary 01-10-2026, trích 30-10-2026; đối chiếu nghĩa, tối nghĩa, từ loại và nhãn. Cùng chế độ quyền Wikimedia; hai ấn bản là hai tập chứng cứ, **không** giả định hai ban biên tập độc lập tuyệt đối. |
| [Leipzig Corpora Collection, Vietnamese Mixed 2014, mẫu 300K](https://downloads.wortschatz-leipzig.de/corpora/vie_mixed_2014_300K.tar.gz) | 300.000 câu, chỉ đếm số câu có chuỗi, không trích câu. [Điều khoản Leipzig](https://wortschatz.uni-leipzig.de/en/usage) ghi riêng **CC BY** cho gói văn bản tải xuống; không suy giấy phép từ điều khoản áp dụng cho giao diện tra cứu. |
| [Tatoeba, xuất câu tiếng Việt](https://downloads.tatoeba.org/exports/per_language/vie/vie_sentences.tsv.bz2) | 33.328 câu ở ảnh chụp tải 19-11-2026. Ghi công những người đóng góp Tatoeba; [điều khoản §6](https://tatoeba.org/en/terms_of_use): mặc định CC BY 2.0 FR, một số câu có thể là CC0. Chỉ dùng số đếm; không phát hành lại câu hay bản dịch. |
| Công cụ cục bộ | Qwen Team, [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B), bản [GGUF Q4_K_M của Unsloth](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF/tree/3885219b6810b007914f3a7950a8d1b469d598a5) — Apache-2.0; [llama.cpp b12530](https://github.com/ggml-org/llama.cpp/releases/tag/b12530) — MIT. [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small/tree/614241f622f53c4eeff9890bdc4f31cfecc418b3) — MIT, đối chiếu nghĩa trên CPU. Không gọi API sinh văn bản bên ngoài, không thêm thư viện cho ứng dụng. |

Bảng lưu trữ ở mục 6 không trích câu của Leipzig hay Tatoeba, nhưng có dùng nghĩa Wiktionary trong lời nhắc soạn nháp. Khi tái phân phối bảng này, giữ ghi công trên và điều kiện [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); điều kiện đó không thay đổi [giấy phép MIT của ứng dụng](LICENSE) hoặc giấy phép của các nguồn. Có thể tra lịch sử một đầu mục tại `vi.wiktionary.org/wiki/<đầu_mục>` hoặc `en.wiktionary.org/wiki/<đầu_mục>`.

**Dấu vân tay của các tệp đầu vào (SHA-256):**

| Tệp | SHA-256 |
|---|---|
| Kaikki tiếng Việt, JSONL gzip | `1f0abd21982660b5fc2eff5eb3fbacbed2d9fe8f476af794dbed0d927ffb8187` |
| Kaikki tiếng Anh, JSONL riêng cho tiếng Việt | `186cd0a62d876dada70c9761bc05e598c8cf7b9a48e0aa518bab6c649e28d945` |
| Leipzig 300K, tar.gz | `067c18ff6e719fea866314836c19d4d1ae4b597c4b5207435131cbb5de32c57e` |
| Tatoeba tiếng Việt, bzip2 | `e9a6451c46c43d9e15b923945325e74c8f28a8bc8e2e9c864801942337dbcb1a` |

1. **Nhập và kiểm hình thức.** Bản Việt có 44.871 bản ghi tiếng Việt cho 41.797 tiêu đề phân biệt sau NFC; bản Anh có 52.167 bản ghi, 45.519 tiêu đề. Từ bản Việt, 35.471 tiêu đề là chữ thường Việt, một đến bốn nhóm chữ. Bước lọc kế tiếp ghi nguyên nhân đầu tiên: độ dài 3.046; cấu trúc âm tiết 160; biến thể 1.671; thiếu từ loại/nghĩa đủ dùng 6.654; bề mặt hoặc khóa nhạy cảm 826; nhãn/nội dung nghĩa nhạy cảm 757; thiếu chứng liệu 4.692. Còn **17.665** ứng viên, ứng với 15.631 khóa. Không coi mọi dòng trùng tiêu đề với tên người là tên riêng nếu có nghĩa danh từ chung thật sự.
2. **Đo độ thông dụng.** Hạ chữ để đếm nhưng giữ nguyên chữ đã kiểm cho đầu mục. Tìm chuỗi âm tiết liên tiếp, không qua dấu câu; trong mỗi câu chỉ cộng một lần. Đếm thêm một lần theo phép tách tham lam: ở từng vị trí ưu tiên mục từ dài nhất; phân biệt một tiếng thường dùng riêng với một yếu tố chỉ hay nằm trong từ dài. Độ phủ của **bảng Astra**: 7.762 mục có mặt trong Leipzig, 3.691 trong Tatoeba, 3.681 có mặt ở cả hai, 4 ở ngoài cả hai (*bánh quế*, *dép lê*, *ròng rọc*, *thước dây*); 7.764 xuất hiện ít nhất một lần theo phép tách dài nhất (trong đó 453 mục một khối). Trung vị số câu chứa một mục là 29 ở Leipzig và 0 ở Tatoeba. 6.033 đầu mục còn có nghĩa đạt bộ lọc ở ấn bản tiếng Anh. Ngoài nhóm duyệt tay, phải có ít nhất một câu Tatoeba, hoặc ít nhất hai câu Leipzig và một lần được tách thành mục ở Leipzig.
3. **Xếp hạng trước biên tập.** Gọi `L` và `T` là hai số câu, `p` là dấu hiệu vật thể trong nghĩa danh từ, `a` là vật/hoạt động quen do tôi chọn trước, `e` là chứng cứ nghĩa ở ấn bản Anh, `n` là có nghĩa danh từ, `h` là có láng giềng vùng miền có chứng cứ, `q` là có hỏi/ngã, `s` là số âm tiết, `d` là số chữ. Điểm đầu: `log₂(1+L) + 1,55 log₂(1+min(T,50)) + 1,9e + 2,6p + 0,4n + 3a − [s=1] − 0,25max(s−2,0) − 0,18max(d−10,0) − 0,65h − 0,32q`. Chặn ảnh hưởng một từ lặp trong ngữ liệu dịch; thưởng ngôn ngữ đời thường nhưng không lấy số liệu làm chứng cứ duy nhất. Trước khi loại va chạm, cộng tiếp `0,42 log₂(1+L_tách) + 0,53 log₂(1+min(T_tách,24)) + 2p + 0,9[A] + 0,55[s≥2 và T>0] + 0,7[L>0 và T>0]`. Ưu tiên nhóm biên tập đã xác nhận trước nhóm chấm tự động; hòa điểm thì theo thứ tự chữ Việt. Các hệ số là quyết định biên tập công khai, không phải hằng số ngôn ngữ học.
4. **Viết nghĩa, rà chủ đề.** Tôi viết hoặc sửa lời giải cho các mục một khối được cân nhắc và nhiều mục về đồ vật, sinh hoạt. Với mục nhiều khối, công cụ soạn nháp trên máy từ nghĩa từ điển của chính mục đó rồi chấm A (đời thường), B (phổ thông), C (hẹp), X (không dùng). Đã soạn thử 11.900 ứng viên chính và 2.176 ứng viên dự trữ có bằng chứng; giữ A/B hoặc biên tập lại sau khi rà. Nhãn máy không phải chân lý: ví dụ *bút chì* không nhất thiết có cục tẩy, *vành khuyên* ở đây là chim chứ không phải khuyên tai. Bộ cờ soạn tay còn được mở rộng khi gặp nhãn thiếu, như *u nang* hay *lô cốt*. Bảng Astra có **5.831** nghĩa từ nhánh soạn nháp và **1.945** nghĩa gắn nhãn biên tập, kể cả những câu sửa sau khi đã thấy nháp.
5. **Xét ngược và kiểm giống văn.** Loại lời giải khớp nguyên một nghĩa nguồn, chứa một chuỗi khớp ít nhất sáu tiếng với nghĩa cùng mục, chép trọn một đoạn nghĩa ngắn theo ngưỡng, hoặc có tỉ số khớp dãy từ ≥ 0,78 với một nghĩa nguồn (từ năm tiếng trở lên). Tính tương đồng E5 với các nghĩa Việt và Anh; dùng điểm thấp để tìm lỗi, chặn bản nháp có điểm tốt nhất dưới 0,84 nếu chưa duyệt đích danh. Đây là ngưỡng rà soát cục bộ, không phải xác suất lời giải đúng; không coi điểm cao là chứng minh đúng. Soát lại bản nháp bằng lượt đọc tách biệt; nếu bị gắn cờ, xét lại **từng mục**, không đưa kết luận cũ vào đề. Với nghĩa không do tôi viết trực tiếp, chỉ nhận kết quả qua kiểm hoặc quyết định thủ công có lưu vết. Đã có 8.444 lượt kiểm mục riêng biệt trong phép kiểm thứ nhất và 2.001 mục được hỏi lại riêng; 419 mục trong bảng được chấp nhận ở lần xét lại. Tất cả 419 mục còn bất đồng ở lượt đầu chỉ được giữ sau khi tôi đọc đích danh cả từ và nghĩa; không hạ chuẩn hình thức hay an toàn. Sau các cửa này còn 8.104 ứng viên, trước khi chốt đúng 7.776. Trong đoạn xếp đã duyệt đến vạch chốt, bỏ thêm 209 do khóa trùng và 13 do cặp dễ nghe lẫn. Không dùng ba chữ để bù.

**Đối chiếu vòng đầu.** Các bước lập mục từ và số đếm nằm ở [prepare.py](analyzing-tools/ho-so/astra/prepare.py), [speech_count.py](analyzing-tools/ho-so/astra/speech_count.py), [segment.py](analyzing-tools/ho-so/astra/segment.py) và [select_words.py](analyzing-tools/ho-so/astra/select_words.py). Các bước soạn và xét nháp nằm ở [compose.py](analyzing-tools/ho-so/astra/compose.py), [judge.py](analyzing-tools/ho-so/astra/judge.py), [challenge.py](analyzing-tools/ho-so/astra/challenge.py) và [semantic.py](analyzing-tools/ho-so/astra/semantic.py). [quality.py](analyzing-tools/ho-so/astra/quality.py), [final_select.py](analyzing-tools/ho-so/astra/final_select.py) và [publish.py](analyzing-tools/ho-so/astra/publish.py) lần lượt kiểm, chọn và xuất **phương án cũ**. Các script này không kèm đủ kho câu, bản nháp và sổ quyết định để chạy lại toàn bộ vòng đầu chỉ từ repo. Để tái lập các phép kiểm của **bản phát hành**, xem [hướng dẫn công cụ](analyzing-tools/README.md).

## 4. Kiểm tra, hạn chế và chỗ cần phản biện

- **Kiểm máy trên thành phẩm, không chỉ trên nguồn.** Python đối chiếu đầu mục, NFC toàn dòng, số lượng, ký tự, khóa, các cặp vùng đã định và độ giống nguồn. Trình kiểm Node đọc ngược đúng khối bên dưới, chạy nguyên regex của app, kiểm lại khóa sau viết hoa, giới hạn độ dài, dấu cách, số cột và thứ tự bằng một bộ so độc lập. Không lời giải nào trùng nguyên lời giải tiếng Việt trong tập từ điển đã lập chỉ mục; không lời giải nào là nguyên một câu trong hai mẫu kho câu khi quy về từ thường và bỏ dấu câu. Một số thuật ngữ đồng nghĩa có thể chia sẻ những cụm từ ngắn hiển nhiên. SHA-256 của **các dòng dữ liệu UTF-8, LF, có một LF cuối**, không gồm hàng rào Markdown: `dfd74f433bb77faf2d9033800c58dccdb54adcb5be8a1580ed90cb63c8744f8e`.
- **Đọc mẫu và đọc theo rủi ro.** Ngoài các nghĩa tự biên tập và các cụm bị gắn cờ, tôi đọc mẫu 160 dòng của bản gần chốt: 20 dòng ở mỗi một phần tám dải điểm, lấy thứ tự băm cố định `astra-8x20-v1:` + từ; sửa hoặc không giữ 64 mục trong mẫu đó. Tôi cũng đọc các trường hợp điểm nghĩa thấp, kiểm tra cách dùng có thật và rà các nhóm về chiến sự, sức khỏe, tôn giáo, bộ máy chính trị, chính tả. Đây là **đánh giá biên tập có lấy mẫu**, không phải số đo lỗi toàn danh sách hoặc khảo sát người dân. Cả hai lượt đọc máy dùng cùng mô hình nên có thể lặp lại cùng một lỗi.
- **Giới hạn nguồn.** Wiktionary có thể thiếu mục rất quen, lẫn nghĩa cổ/địa phương với nghĩa chính, hoặc chỉ trỏ sang mục khác. Leipzig thiên về văn viết, có tư liệu cũ; Tatoeba nhỏ hơn, chịu ảnh hưởng câu dịch. Chuỗi đứng cạnh nhau không bảo đảm người nói coi đó là một từ, còn tách dài nhất đôi lúc nuốt mất mục con. Không đánh đồng “không thấy” với “không ai dùng”. Bảng không bảo đảm mọi người ở mọi vùng đều quen như nhau. Danh mục tục/nghĩa bóng cũng không thể bao hết tiếng lóng đang đổi.
- **Khi nhập mật khẩu:** NFC lưu trong tài liệu không buộc bộ gõ tạo cùng dãy byte. Hãy thử bộ gõ ở chế độ Unicode dựng sẵn và thử ngay trong ô mật khẩu trên thiết bị thật; một số ô tắt IME. Khi lưu trong trình quản lý mật khẩu, ưu tiên dán/tự điền đúng chuỗi đã chọn. Chữ hoa đầu một từ ghép áp dụng một lần (*Déplê*, không phải *DépLê*); bản có dấu và bản bỏ dấu là hai mật khẩu khác nhau, không phải hai cách đăng nhập thay thế.
- **Các câu hỏi sau vòng đầu.** Hai bên đã thống nhất không bắt buộc loại một từ trong cặp vùng miền, xét nghĩa nhạy cảm của **nguyên mục** và xếp hạng theo độ quen sau khi qua các luật cứng. Thử đọc–gõ lại với người ở Bắc, Trung, Nam và nhiều lứa tuổi là một đề xuất; các số đếm của Astra không thay cho phép thử đó.

## 5. Kết quả review chéo

Khi so hai phương án độc lập, Opus kiểm cả 7.776 dòng và chấm tay **320 khóa lấy ngẫu nhiên trong 3.253 khóa riêng của Astra**. Bảng đạt yêu cầu NFC, độ dài tối thiểu, thứ tự từng âm tiết và không trùng khóa **trong bảng**. Nhưng một khóa độc nhất vẫn có thể đọc thành từ nhạy cảm **ngoài bảng**; một mục có trong từ điển cũng chưa chắc thích hợp làm passphrase. Xem [phản hồi vòng hai của Astra](analyzing-tools/ho-so/discussion/phan-hoi-astra.md).

| Điểm Opus nêu | Điều Astra đã kiểm và sửa trong tiêu chí chung |
|---|---|
| Đầu mục lành nhưng khóa không dấu không lành | *Đảm đang* trùng `damdang` với *dâm đãng*; *nước dãi* trùng `nuocdai` với *nước đái*. Danh mục tục cũ thiếu cả hai đối chứng. Phải kiểm toàn khóa, kể cả phần giao của hai danh sách, chứ không chỉ dò một tiếng trong từ ghép. |
| Lọt chủ đề nhạy cảm hoặc chọn nghĩa phụ để tránh nghĩa chính | Bộ lọc cũ bỏ *bầu cử* nhưng giữ *cuộc bầu cử, ứng cử viên*; còn lọt *vé số, tràng hạt, siêu âm tim*. Với *chung thân*, 18/20 dòng Leipzig và cả 2 câu Tatoeba xác nhận ngữ cảnh hình phạt. Đổi sang một lời giải nghe lành không làm đầu mục này phù hợp. |
| Biến thể chính tả | *Cảm ơn/cám ơn* có cùng khóa nhưng là hai mật khẩu khác nhau khi giữ dấu; *xung quanh/chung quanh* thì khác cả khóa. Cả hai cặp đều có cạnh tranh thực. Ngược lại, nhiều lượt *để giành* nằm trước tên phần thưởng hoặc kết quả tranh đấu, không phải lỗi của *để dành* theo nghĩa tiết kiệm. Phải đo từng kho và đọc đúng nghĩa. |
| Cụm tự do và độ quen | Có tiêu đề từ điển không đủ để nhận *có một, ba bốn, ơi là* hay thành ngữ bốn tiếng. Trong 320 mục, Opus xếp 80 OK, 151 thiên văn viết/chuyên môn, 27 hiếm; 62 mục còn lại thuộc nhóm nhạy cảm, khóa, chính tả hoặc cấu tạo. Trung vị Leipzig trên đúng 3.253 khóa riêng là **11 câu ở Astra, 18 ở Opus**. Đây là nhận xét về hai tập, không phải phán quyết cho từng từ. |
| Giải nghĩa sai hoặc quá hẹp | Tôi xác nhận cả **14/14 cờ về lời giải** Opus nêu trong mẫu Astra; đây là cờ bổ sung, không cộng vào 320 nhãn chính. Chẳng hạn *cùi chỏ* nhầm vị trí khớp, *đầu phiếu* nhầm thao tác, *nhất nhất* bị gán thêm nét “cẩn thận”, còn *ngứa ngáy* chỉ viết nghĩa bóng. Điểm tương đồng cao không xác nhận sự kiện hay từ loại. |

**Quyền sử dụng lời giải.** Với **5.831/7.776** lời giải, lời nhắc cho mô hình có chứa nghĩa của Wiktionary (CC BY-SA). **1.945** dòng gắn nhãn biên tập gồm cả những câu sửa sau khi đã thấy nháp. Kiểm không trùng nguyên câu không chứng minh các dòng này được soạn độc lập. **Không dùng bất kỳ lời giải Astra cũ nào cho dữ liệu phát hành theo MIT.** Theo quyết định của chủ dự án, các lượt viết mới chỉ nhận đầu mục và [hướng dẫn](analyzing-tools/huong-dan-giai-nghia.md), không thấy bản Astra, bản Opus, nghĩa từ điển hay câu trong kho. Khi cần viết lại, người soát chỉ trả chẩn đoán, không đưa câu mẫu.

**Những điểm tôi giữ sau đối chiếu.** Không bỏ một từ chỉ vì vắng ở một kho nhỏ: *ròng rọc, dép lê* đều có trong bản phát hành. Cơ thể và sinh hoạt thường ngày không mặc nhiên nhạy cảm; một âm tiết xuất hiện trong từ tục không làm mọi từ chứa nó thành tục. Tôi giữ cách so từng âm tiết và ưu tiên danh từ cụ thể ba khối như *máy hút bụi*, nhưng **rút** quy tắc bắt buộc loại một trong *sách/xách*. Hai bên đã thu phạm vi còn 4–12 chữ, 1–3 khối, không dùng từ ba chữ kể cả dự phòng; cùng hiệu chỉnh thang chấm rồi chấm chéo, không chia suất theo nguồn.

## Kết quả cuối cùng

Ngày **20/11/2026**, [quyết định 10 của chủ dự án](WordListAnalyze.md#3-quyết-định-của-chủ-dự-án) cho phát hành 7.776 từ: [trang tạo mật khẩu](index.html) dùng cột từ; [trang thông tin](thong-tin.html) có cả giải nghĩa viết mới theo MIT, đã đạt kiểm nguồn gốc D6 và soát nội dung D7. [205 từ dự phòng](analyzing-tools/du-phong.txt) ở trạng thái **“dự phòng, chưa phân tích”**, không được phát hành; đủ 300 dự phòng không còn là điều kiện phát hành.

Tôi so cột trước dấu `|` của mục 6 với [nguồn chuẩn phát hành](analyzing-tools/wordlist.txt), trước hết theo nguyên mặt chữ, sau đó theo khóa của ứng dụng (NFD, bỏ dấu kết hợp, `đ` → `d`, viết thường, bỏ dấu cách). **4.766/7.776 từ Astra (61,29%)** trùng nguyên mặt chữ; **104** chỉ trùng khóa nhưng khác từ (như *bản thân* → *bạn thân*); **2.906** không còn cả khóa. Như vậy hai danh sách có **4.870 khóa chung**, nhưng **3.010 mặt chữ Astra không vào bản chính**.

| Điểm dừng của 3.010 mặt chữ (mỗi từ tính một lần) | Số từ | Lý do theo hồ sơ |
|---|---:|---|
| Trượt [cổng tự động P2](analyzing-tools/ho-so/unified/cong-astra-v4.tsv) | 281 | Tính cổng trượt đầu tiên: 99 độ dài/số khối, 60 quyết định chủ dự án, 58 chính tả, 47 cách đọc không dấu, 14 tư cách đầu mục, 3 khóa đã chốt. |
| Có [phiếu Astra](analyzing-tools/ho-so/unified/phieu-astra.tsv) và [phiếu Opus](analyzing-tools/ho-so/unified/phieu-opus.tsv) nhưng vắng ở [đầu vào P6](analyzing-tools/ho-so/unified/p6-dau-vao.tsv) | 1.074 | 454 từ có ít nhất một phiếu R2 (hiếm/hẹp), 275 có phiếu S (nghĩa nhạy cảm); các nhãn có thể chồng nhau. Còn có cụm tự do, vướng chính tả/cách đọc, hoặc [P5 chọn mặt chữ khác cùng khóa](analyzing-tools/ho-so/unified/ket-qua-chon.tsv). |
| Bị ghi `LOAI` ở P6–P7 trong [hồ sơ D8](analyzing-tools/nguon-goc-giai-nghia.tsv) | 107 | 5 do chính tả H5, 16 do nghĩa nhạy cảm H6. 77 trường hợp còn vướng D6 và 9 chưa đạt D7 là do **lời giải mới**, không phải kết luận rằng bản thân từ không phù hợp. |
| Có tên trong [bảng xếp hạng](analyzing-tools/ho-so/unified/xep-hang.tsv), không bị ghi `LOAI` | 1.548 | 1.381 từ thiên văn viết/chuyên môn (R1) xếp sau từ thông dụng (OK); 92 từ OK nằm trong 205 dự phòng; 75 từ OK lớp F ngoài cả hai danh sách vì hạn mức 77 hư từ/đại từ. |

**Bài học cho Astra.** Đếm theo ranh giới và kiểm khóa giúp phát hiện lỗi hình thức, nhưng tiêu đề từ điển hay điểm tần suất không đủ chứng minh một nghĩa quen dùng. Phần riêng của Astra thiên về văn viết; cách khắc phục là đối chiếu bốn kho, đọc đúng ngữ cảnh và chấm độc lập theo cùng thang, thay vì thưởng thêm cho mục tự biên tập. Tương tự, điểm giống nghĩa không chứng minh câu đúng hoặc độc lập với nguồn: phải tách lượt viết khỏi văn bản tham chiếu rồi soát nội dung.

## 6. Danh sách đầy đủ — bản lưu trữ Astra

Khối dưới đây giữ nguyên để đối chiếu kết quả độc lập và làm tham chiếu cho [bộ kiểm D6](analyzing-tools/d6-kiem.py); SHA-256 thân khối ghi ở mục 4. **Đây không phải dữ liệu đang chạy.** Hai trang HTML đã dùng [danh sách thống nhất](WordListAnalyze.md#10-danh-sách-7776-từ-phát-hành) từ bước P8. Bản đối chứng còn lại là [phương án độc lập của Opus](WordListAnalyze-Opus.md).

Thứ tự: so từng **âm tiết** từ trái sang phải. Trong một âm tiết, so dãy chữ chưa mang thanh theo `a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y`; giữ nguyên phân biệt `ă/â`, `ô/ơ`, `u/ư`, `d/đ`. Nếu phần chữ bằng nhau, so thanh ngang, huyền, hỏi, ngã, sắc, nặng rồi mới sang âm tiết kế; tiền tố ngắn đứng trước. `ch`, `ng`, `ngh`, `ph`… là dãy chữ, không phải chữ cái riêng. Quy tắc này không phụ thuộc phiên bản sắp xếp ICU hay thứ tự mã Unicode.

```text
á nhiệt đới|Vùng khí hậu nằm giữa vùng ôn đới và vùng nhiệt đới nóng.
ách tắc|Bị dồn ứ nên người, xe hoặc công việc không tiếp tục thông suốt.
ai ai|Mọi người, tất cả mọi người trong số đó.
ai dè|Không ngờ đến việc xảy ra.
ai nấy|Mọi người đều như vậy, không ai ngoại lệ.
ai ngờ|Chẳng ai lường trước được điều bất ngờ xảy ra.
ái chà|Tiếng thốt ra khi thấy vui hoặc bất ngờ.
ái lực|Khả năng tự nhiên thu hút và gắn kết với vật chất khác.
ái ngại|Thương xót và lo lắng trước hoàn cảnh khó khăn của người khác.
am hiểu|Biết rõ tường tận về một vấn đề hoặc lĩnh vực nào đó.
am tường|Hiểu rõ mọi chi tiết của một việc.
ám chỉ|Chỉ người hoặc việc một cách gián tiếp.
an cư|Sống yên ổn tại một nơi định cư.
an cư lạc nghiệp|Sống yên ổn tại một chỗ và làm việc phát triển với tâm thế thoải mái, vững chắc.
an dưỡng|Nghỉ ngơi và bồi dưỡng để phục hồi sức khỏe.
an hưởng|Sống trong sự bình yên, tận hưởng cuộc đời.
an khang|Sống yên ổn, không có tai ương và cơ thể khỏe mạnh.
an nhàn|Thảnh thơi, yên ổn, không phải làm việc vất vả.
an nhiên|Sống yên bình, tự tại như lẽ tự nhiên vốn có.
an ninh|Trạng thái yên ổn, không có sự hỗn loạn hay nguy hiểm.
an ổn|Bình yên và không có sự thay đổi bất lợi.
an sinh|Đảm bảo đời sống ổn định, đủ ăn mặc.
an toàn|Yên ổn, không còn lo sợ tai họa hay nguy hiểm.
an toàn giao thông|Sự an toàn và thông suốt cho người và phương tiện trên mọi đường đi.
an toàn lao động|Các quy tắc và biện pháp bảo vệ người làm việc khỏi nguy hiểm.
an ủi|Dùng lời nói hoặc việc làm để làm vơi đi nỗi buồn.
an vị|Ngồi yên tại một chỗ không di chuyển.
an vui|Tâm hồn thư thái, không lo âu và cảm thấy hạnh phúc.
áng chừng|Đoán số lượng hoặc giá trị xấp xỉ.
anh chị em|Những người con trong cùng gia đình xét trong quan hệ với nhau.
anh đào|Cây ăn quả vùng lạnh, vỏ bóng, thịt đỏ hoặc vàng, vị ngọt chua.
anh em|Những người con trong một gia đình xét theo vai anh và em.
anh hào|Người có tài năng, dũng cảm và được nhiều người kính trọng.
anh minh|Người lãnh đạo có tài năng và trí tuệ sáng suốt.
anh tài|Người có năng lực và trí tuệ vượt trội so với người khác.
anh trai|Người nam lớn tuổi hơn, cùng cha mẹ sinh ra với người được gọi.
ảnh hưởng|Tác động làm thay đổi suy nghĩ hoặc hành động của người khác.
ảnh thật|Bức hình thực sự tạo nên khi ánh sáng hội tụ trên màn chắn.
ánh dương|Ánh sáng tỏa ra từ Mặt Trời, thường dùng cho buổi sáng.
ánh kim|Vẻ sáng bóng đặc trưng do kim loại phản chiếu ánh sáng.
ánh sáng|Hiện tượng vật lý giúp mắt người nhìn thấy các vật thể.
ánh trăng|Ánh sáng từ Mặt Trăng chiếu xuống, thường thấy rõ ban đêm.
ánh xạ|Cách biểu diễn mối quan hệ giữa các phần tử của hai nhóm khác nhau.
ao ước|Mong muốn có được điều mình thích.
ào ào|Nhanh và mạnh. / Ồn ào, sôi sục.
ào ạt|Tuôn đến nhanh và nhiều, như mưa lớn hoặc một dòng người.
ảo ảnh|Hình ảnh nhìn thấy nhưng không tồn tại trong thực tế.
ảo thuật|Nghệ thuật dùng tay nhanh để làm biến mất đồ vật.
ảo thuật gia|Người chuyên thực hiện các trò chơi giả tạo để gây ngạc nhiên.
áo ấm|Áo dày hoặc có lớp lót để giữ nhiệt khi trời lạnh.
áo bông|Áo khoác có lót bông giữ ấm, thường có cổ và tay dài.
áo choàng|Áo khoác ngoài tương đối dài, phủ vai và thân người.
áo dài|Trang phục Việt có hai tà dài, thường mặc với quần.
áo gối|Vỏ bọc bên ngoài chiếc gối để bảo vệ và trang trí.
áo khoác|Áo mặc ngoài trang phục chính để giữ ấm hay che nắng.
áo mưa|Áo không thấm nước dùng khi đi ngoài trời mưa.
áo phao|Áo có phần nổi giúp người mặc không chìm trong nước.
áo sơ mi|Áo có cổ, thường mở phía trước bằng một hàng cúc.
áo tơi|Áo ghép từ lá, choàng ngoài để che mưa.
áp dụng|Dùng vào thực tế những điều đã hiểu hoặc học được.
áp lực|Sức ép mạnh từ bên ngoài tác động vào.
áp phích|Bức tranh lớn dùng để thông tin hoặc trang trí.
áp suất|Lực ép tính trên mỗi đơn vị bề mặt.
áp thấp|Vùng có áp suất không khí thấp hơn khu vực xung quanh.
ăn bám|Sống dựa vào tiền bạc hoặc công sức của người khác.
ăn chắc|Nắm chắc phần thắng hoặc lợi ích trong một việc làm.
ăn chơi|Sử dụng tiền bạc để vui chơi, giải trí hoặc đi lại xa.
ăn cỗ|Tham dự bữa ăn trang trọng nhân dịp đặc biệt.
ăn cơm|Ăn bữa cơm chính thức của gia đình hoặc dùng bữa để thỏa mãn nhu cầu.
ăn cưới|Đến dự tiệc cưới để ăn uống.
ăn dặm|Cho trẻ ăn thêm thức ăn ngoài sữa để làm quen với món mới.
ăn đứt|Hơn hẳn, trội hơn hẳn trong việc so sánh.
ăn học|Học tập và trau dồi kiến thức thông qua việc đến trường.
ăn hỏi|Đến nhà gái để xin phép kết hôn.
ăn khách|Được nhiều người mua hàng hoặc xem biểu diễn, rất được lòng công chúng.
ăn khớp|Phù hợp hoàn toàn, hòa hợp và không có sự mâu thuẫn với nhau.
ăn lương|Nhận tiền lương hàng tháng từ nơi làm việc.
ăn may|Thành công hoặc đạt được điều mong muốn nhờ vận may thay vì nỗ lực.
ăn mặc|Đeo quần áo lên người.
ăn mòn|Làm vật liệu mất dần ở bề mặt do tác động hóa học hay môi trường.
ăn mừng|Tổ chức ăn uống, vui chơi để kỷ niệm một sự kiện vui vẻ.
ăn năn|Cảm thấy hối lỗi vì đã làm sai điều gì đó.
ăn nói|Dùng lời nói để bày tỏ suy nghĩ hoặc quan điểm của mình.
ăn tạp|Ăn cả thịt lẫn rau củ, không kén chọn loại thức ăn.
ăn tết|Đón dịp đầu năm với những sinh hoạt và món ăn theo phong tục.
ăn tiệc|Dự bữa ăn tổ chức để gặp gỡ hoặc mừng một dịp nào đó.
ăn uống|Hành động ăn cơm, uống nước hoặc chuẩn bị bữa ăn.
âm điệu|Sự lên xuống, ngắt nối tạo sắc thái cho giọng nói hoặc giai điệu.
âm giai|Tập hợp các nốt nhạc được sắp xếp theo quy luật nhất định.
âm hưởng|Tiếng vang, dư âm hoặc cảm xúc lan tỏa.
âm lịch|Hệ thống lịch tính toán dựa trên chu kỳ tròn đầy của mặt trăng.
âm lượng|Mức to hoặc nhỏ của âm thanh mà người nghe cảm nhận.
âm nhạc|Nghệ thuật dùng âm thanh, nhịp điệu và lời.
âm thanh|Âm phát ra từ vật thể hoặc con người khi rung động.
âm thầm|Làm việc hoặc hành động kín đáo, không để người khác biết.
âm tiết|Đơn vị nhỏ nhất cấu thành nên lời nói trong ngôn ngữ.
ầm ầm|Tiếng động lớn, rền vang liên tục.
ẩm mốc|Độ ẩm cao dẫn đến sinh ra nấm mốc.
ẩm thấp|Ẩm và bí, thường do nơi đó ít ánh sáng hoặc khó thoát hơi nước.
ẩm thực|Hệ thống cách nấu ăn, chế biến thức ăn mang đặc trưng văn hóa.
ẩm ướt|Có nhiều hơi nước hoặc còn đọng nước, chưa khô ráo.
ấm áp|Có nhiệt độ cao và tạo cảm giác dễ chịu cho người.
ấm chén|Bộ gồm ấm rót nước và chén uống nước.
ấm cúng|Tạo cảm giác gần gũi, dễ chịu như ở bên người thân.
ấm êm|Hạnh phúc, vui vẻ và không có lo toan.
ấm no|Đủ lương thực để ăn và đủ quần áo để mặc.
ấm tích|Ấm pha nước uống có thân lớn, thường đặt trong giỏ ủ.
ân cần|Thân thiện, nhiệt tình và chu đáo trong cách đối xử với người khác.
ân đức|Công ơn và lòng tốt của người đã giúp đỡ.
ân huệ|Ơn lớn từ cấp trên ban tặng cho người dưới.
ân nghĩa|Tình cảm sâu sắc phát sinh từ việc nhận ơn và đáp nghĩa.
ân tình|Tình cảm sâu nặng vì đã được giúp đỡ.
ẩn chứa|Tồn tại bên trong mà không biểu hiện rõ ra bên ngoài.
ẩn dật|Sống một mình ở nơi xa xôi, tránh xa việc làm và người đời.
ẩn dụ|Cách dùng từ khác để gợi ý nghĩa tương tự, không nói thẳng ra.
ẩn hiện|Lúc xuất hiện, lúc biến mất, không rõ ràng.
ẩn số|Số chưa biết cần phải tính toán tìm ra.
ấn bản|Phiên bản sách đã được in thành phẩm để phát hành.
ấn định|Quyết định chính thức để mọi người tuân theo.
ấn hành|In sách và phát hành ra thị trường.
ấn phẩm|Sản phẩm được in hoặc xuất bản, như sách hay tập san.
ấn tượng|Cảm nhận mạnh về sự vật do tác động của bên ngoài gây ra trong tâm trí.
ấp úng|Nói lắp bắp, không rõ ràng vì lúng túng hoặc không biết nói gì tiếp.
âu phục|Trang phục được may theo kiểu phương Tây.
âu yếm|Thể hiện tình cảm yêu thương bằng cử chỉ nhẹ nhàng, trìu mến.
ấu trùng|Giai đoạn non sau khi nở, trước khi thành dạng trưởng thành ở nhiều loài.
ba ba|Rùa nước ngọt có mai mềm và mõm nhô như một ống nhỏ.
ba bốn|Số lượng ít, chừng ba hoặc bốn.
ba chỉ|Loại thịt lợn nằm ở phần bụng, gồm nhiều lớp mỡ xen kẽ với thịt nạc.
ba gác|Xe ba bánh có thùng hoặc sàn nhỏ để chở đồ.
ba lê|Nghệ thuật múa sân khấu có hệ thống động tác và tư thế riêng.
ba lô|Túi có quai để đeo trên lưng.
ba mươi|Số lượng bằng ba lần mười.
bà bầu|Phụ nữ đang mang thai trong bụng.
bà chủ|Người phụ nữ nắm quyền điều hành một cơ sở kinh doanh hoặc gia đình.
bà con|Những người cùng dòng họ hoặc thân quen.
bà đỡ|Người phụ nữ chuyên đỡ đẻ cho bà mẹ.
bà ngoại|Người phụ nữ sinh ra mẹ mình.
bà nội|Mẹ của cha mình.
bà xã|Người vợ, dùng để gọi thân mật, vui vẻ.
bả vai|Phần xương nằm giữa lưng, sát dưới vai.
bác ái|Lòng thương yêu rộng lớn, không phân biệt đối xử với bất kỳ ai hay loài vật nào.
bác bỏ|Nêu lý do không công nhận một ý kiến là đúng hay phù hợp.
bác học|Có vốn hiểu biết sâu rộng về nhiều mặt của tri thức.
bạc bẽo|Cư xử thiếu tình nghĩa, không biết ơn và làm người khác thất vọng.
bạc màu|Đất mặt bị rửa trôi, nghèo dinh dưỡng và nhạt màu.
bách bộ|Đi chậm rãi, không vội vàng từng bước chân.
bách khoa|Tập hợp nhiều lĩnh vực khoa học và kỹ thuật khác nhau.
bách khoa toàn thư|Tập hợp sách ghi lại mọi kiến thức chung của nhân loại.
bạch dương|Loại cây thân gỗ lớn, vỏ màu trắng bong mảng.
bạch đàn|Cây gỗ cao lớn, thường trồng để phủ xanh đất trống hoặc làm hàng rào ven đường.
bạch kim|Kim loại quý màu trắng bạc còn có tên là platin.
bạch tuộc|Loài động vật biển thân mềm, có nhiều chân dài vươn ra ngoài.
bài bản|Cách làm việc đúng trình tự và quy tắc đã định.
bài hát|Bài nhạc được hát lên.
bài học|Kiến thức, kinh nghiệm bổ ích rút ra từ việc học tập hoặc sai lầm.
bài làm|Việc thực hiện theo yêu cầu đã được giao trước.
bài tập|Nhiệm vụ để người học thực hành điều vừa học.
bài tây|Bộ bài dùng để chơi trò chơi bài phổ biến.
bài thơ|Tác phẩm bằng lời thường tổ chức theo dòng, nhịp và hình ảnh.
bài toán|Vấn đề cần tính toán để tìm ra kết quả đúng.
bài trí|Sắp xếp và trang hoàng đồ vật để tạo vẻ đẹp hoặc sự ngăn nắp.
bài viết|Văn bản ghi chép thông tin hoặc tài liệu bằng tay hoặc máy.
bài vở|Nội dung bài giảng hoặc tài liệu dùng để học tập nói chung.
bãi biển|Dải cát hoặc sỏi ven biển có thể đi bộ hoặc tắm nắng.
bãi bồi|Đất thấp được hình thành do phù sa sông bồi đắp.
bãi chức|Cắt bỏ chức vụ của một người đang giữ.
bãi cỏ|Khoảng đất trống có lớp cỏ phủ trên mặt.
bãi tắm|Đất cát rộng, phẳng ven biển hoặc sông để tắm.
bái phục|Kính trọng và cảm phục sâu sắc.
bám riết|Cố bám lấy hoặc theo sát người khác không rời.
bám sát|Theo dõi sát sao mọi diễn biến của sự việc.
ban bố|Công bố rộng rãi để mọi người đều biết và làm theo.
ban công|Phần sàn nhô ra ngoài tầng trên, có lan can bảo vệ.
ban đầu|Thời điểm mới khởi đầu, buổi đầu tiên.
ban đêm|Thời gian từ khi mặt trời lặn đến khi nó mọc.
ban mai|Buổi sáng, lúc trời vừa mới sáng.
ban nãy|Khoảng thời gian vừa mới qua.
ban ngày|Thời gian trong ngày khi mặt trời còn chiếu sáng.
ban phát|Cấp phát của cải, chức vụ hoặc phần thưởng cho người ở dưới.
ban sơ|Thời điểm khởi đầu của mọi sự việc.
ban tặng|Trao phần thưởng hoặc chức vụ cho người có công lao.
bàn bạc|Cùng trao đổi để hiểu tình hình hoặc tìm ra cách làm.
bàn chải|Dụng cụ có nhiều sợi ngắn để cọ rửa hoặc chải sạch.
bàn chải đánh răng|Dụng cụ gồm lông và tay cầm, dùng chà sạch răng.
bàn chân|Phần cuối của chân chạm đất khi ta đứng.
bàn cờ|Mặt có ô, đường hoặc điểm để đặt và di chuyển quân cờ.
bàn đạp|Bộ phận để chân tác động vào, như ở xe đạp hoặc máy khâu.
bàn ghế|Đồ nội thất để ngồi và đặt vật khi học hoặc ăn.
bàn giao|Giao lại công việc, tài sản hoặc trách nhiệm cho người khác.
bàn giấy|Bàn dùng cho việc đọc, viết hoặc xử lý hồ sơ.
bàn là|Dụng cụ có đế nóng và phẳng để vuốt quần áo cho hết nhăn.
bàn là hơi|Thiết bị điện dùng hơi nước nóng để ủi quần áo.
bàn luận|Trao đổi ý kiến về vấn đề nào đó dựa trên lý lẽ phân tích.
bàn phím|Bộ nút để nhập chữ và lệnh vào máy.
bàn tán|Nói chuyện lung tung, không có mục đích rõ ràng.
bàn tay|Phần cuối cánh tay, gồm cả lòng, mu và các ngón.
bàn tính|Dụng cụ có các hạt trượt trên thanh để biểu diễn số và làm phép tính.
bản chất|Thuộc tính cốt lõi, vốn có bên trong sự vật.
bản đồ|Hình biểu diễn thu nhỏ một khu vực để xác định vị trí.
bản đồ tư duy|Sơ đồ ghi chép các ý tưởng liên kết tỏa ra từ một từ khóa chính.
bản ghi|Danh sách ghi chép thông tin về sự việc.
bản gốc|Phiên bản đầu tiên được ghi chép hoặc viết ra.
bản lề|Khớp giúp cánh cửa mở và khép quanh một trục.
bản lĩnh|Tính cách mạnh mẽ, tự tin, dám làm và chịu trách nhiệm.
bản năng|Tính năng vốn có, sinh ra đã có, không cần học tập.
bản ngữ|Ngôn ngữ mà người đó sinh ra và lớn lên sử dụng.
bản nhạc|Bài nhạc được ghi chép lại để biểu diễn hoặc lưu trữ.
bản quyền|Quyền của tác giả hoặc chủ sở hữu đối với tác phẩm.
bản sao|Phiên bản được sao chép từ một mẫu gốc duy nhất.
bản sắc|Đặc điểm riêng biệt, tạo nên phong cách và bản chất của một người hay một dân tộc.
bản thảo|Bản tác phẩm đang viết hoặc chưa được duyệt để xuất bản.
bản thân|Chính mình, bản người hoặc sự việc đang được nhắc đến.
bản vẽ|Giấy vẽ mô tả hình dáng, kích thước và cấu tạo chi tiết.
bán buôn|Bán số lượng lớn hàng hóa cho người khác để họ bán tiếp.
bán cầu|Nửa hình cầu, thường dùng để chỉ phần Bắc hoặc phần Nam của Trái Đất.
bán chạy|Sản phẩm được nhiều người mua và bán đi nhanh chóng trong thời gian ngắn.
bán dẫn|Chất dẫn điện có khả năng thay đổi điện trở khi nhiệt độ thay đổi.
bán đảo|Khoảng đất bị nước bao quanh phần lớn nhưng vẫn nối liền với đất liền.
bán đấu giá|Bán hàng bằng cách để người mua lần lượt đưa ra mức giá cao nhất.
bán kết|Vòng thi quyết định ai vào chung kết hoặc tranh giải ba.
bán kính|Đoạn nối tâm với điểm trên đường tròn.
bán nguyệt|Nửa hình tròn giống mặt trăng.
bán ròng|Trạng thái người bán cổ phiếu nhiều hơn người mua.
bán trú|Học sinh học và ăn nghỉ ở trường ban ngày, tối về nhà.
bạn bè|Những người có mối quan hệ thân thiết, tin tưởng và giúp đỡ lẫn nhau.
bạn đọc|Người thường xuyên đọc sách, báo hoặc tạp chí.
bạn đời|Người vợ hoặc người chồng chung sống với nhau.
bạn đường|Người đồng hành cùng đi trên một con đường dài.
bạn gái|Người bạn nữ hoặc người yêu nữ giới.
bạn hàng|Người cùng nghề nghiệp hoặc khách hàng quen thuộc với người bán.
bạn học|Người cùng lớp hoặc cùng trường học với mình.
bảng|Mặt phẳng để viết cho cả lớp cùng xem.
bảng biểu|Dụng cụ ghi chép và biểu đồ số liệu.
bảng chọn|Danh sách các lựa chọn lệnh để điều khiển phần mềm.
bảng chữ cái|Tập hợp tất cả các ký tự dùng để viết một ngôn ngữ.
bảng đen|Mặt bảng sẫm màu để viết lên bằng phấn.
bảng điện|Tấm đặt các công tắc, ổ cắm hoặc bộ phận điều khiển điện.
bảng hiệu|Bảng ghi tên cửa hàng hoặc thông tin cần thiết dùng để quảng cáo.
bảng kê|Bảng ghi chép liệt kê các mục cần biết.
bảng màu|Tập hợp các màu được chọn để phối hoặc hiển thị cùng nhau.
bảng tin|Bảng dùng để gắn hoặc dán các thông báo cần biết.
bảng tổng sắp|Bảng liệt kê và xếp hạng toàn bộ các đối tượng cùng loại.
bảng tuần hoàn|Bảng xếp các nguyên tố theo số hiệu nguyên tử và các tính chất lặp lại.
bánh|Món ăn thường làm từ bột rồi nặn, hấp hoặc nướng.
bánh bao|Bánh bột mì hấp phồng, có thể bọc nhân ở giữa.
bánh bèo|Bánh bột gạo hấp mỏng, thường ăn với tôm và nước chấm.
bánh bò|Bánh bột lên men, khi chín xốp và bên trong có nhiều lỗ nhỏ.
bánh bột lọc|Bánh làm từ tinh bột sắn dẻo trong, thường bọc nhân tôm hoặc thịt.
bánh canh|Món nước dùng với sợi bột to và khá dày.
bánh căn|Bánh bột gạo nhỏ nướng trong khuôn đất, ăn cùng nước chấm.
bánh chay|Bánh nếp thường có nhân đậu xanh, ăn cùng nước đường hoặc nước sánh.
bánh chè|Chỗ xương tròn, dẹt ở đầu gối người.
bánh cốm|Bánh dẻo làm từ cốm, thường gói nhân đậu xanh.
bánh cuốn|Lá bánh bột gạo hấp mỏng, cuốn lại, có thể thêm nhân.
bánh da lợn|Bánh hấp dẻo có nhiều lớp xen kẽ, thường có đậu xanh.
bánh dẻo|Bánh trung thu có vỏ trắng mềm làm từ bột nếp chín.
bánh đa|Bánh bột tráng mỏng thành tấm, có loại nướng lên ăn giòn.
bánh đa nem|Bánh tráng mỏng dùng để cuốn thịt hoặc rau ăn sống.
bánh đậu xanh|Bánh ngọt bở mịn làm từ đậu xanh nghiền.
bánh đúc|Bánh bột nấu thành khối mềm mịn rồi để nguội hoặc ăn nóng.
bánh gai|Bánh nếp có lá gai tạo vỏ sẫm, thường bọc nhân đậu xanh.
bánh giò|Bánh bột gạo nhân thịt, thường gói lá thành hình chóp rồi hấp.
bánh hỏi|Những sợi bột gạo thật nhỏ kết thành lớp mỏng để ăn.
bánh in|Bánh bột ngọt được nén vào khuôn có hình hoặc chữ nổi.
bánh ít|Bánh nếp nhỏ thường có nhân, gói lá thành từng chiếc.
bánh kem|Món ngọt nướng từ bột, đường, trứng phủ kem.
bánh kếp|Bánh làm từ bột mịn, chiên vàng mỏng, mềm và thơm mùi bơ.
bánh khoai|Bánh có khoai làm nguyên liệu chính, thường chiên cho vàng.
bánh khọt|Bánh nhỏ tròn đổ trong khuôn riêng, thường có tôm trên mặt.
bánh khúc|Bánh nếp có lá khúc, thường bọc nhân đậu xanh và thịt.
bánh lái|Bộ phận dưới nước xoay được để đổi hướng tàu thuyền.
bánh mật|Bánh làm từ bột nếp trộn mật, nhân đậu hoặc lạc, gói lá chuối, hấp chín.
bánh nậm|Bánh bột gạo mềm phết mỏng trên lá, thường rắc nhân tôm thịt.
bánh nếp|Bánh làm từ gạo nếp hoặc bột nếp, thường có độ dẻo.
bánh ngọt|Bánh có vị ngọt rõ, thường ăn nhẹ hoặc tráng miệng.
bánh nướng|Loại bánh được làm chín bằng nhiệt trong lò, như bánh trung thu vỏ nâu.
bánh phồng|Bánh làm từ bột nếp hoặc khoai, nướng lên nở to và giòn.
bánh phồng tôm|Bánh mỏng có tôm và tinh bột, nở xốp khi làm nóng.
bánh phở|Loại bánh làm từ bột gạo, dùng để nấu món phở.
bánh pía|Bánh có vỏ mỏng tách lớp, nhân ngọt thường làm với đậu xanh.
bánh quế|Bánh mỏng giòn, thường cuộn thành ống hoặc ốc quế.
bánh rán|Bánh làm chín trong dầu nóng, thường có vỏ vàng.
bánh răng|Bộ phận cơ khí hình tròn có răng để truyền lực quay.
bánh tẻ|Bánh bột gạo tẻ gói lá, thường có nhân thịt và mộc nhĩ.
bánh tét|Bánh nếp hình trụ gói lá, lúc ăn cắt thành khoanh tròn.
bánh tiêu|Bánh bột mì chiên phồng, thường phủ hạt vừng ngoài vỏ.
bánh tôm|Bánh có tôm gắn vào phần bột rồi chiên cho giòn.
bánh trái|Tổng hợp nhiều loại bánh ngọt và bánh kẹo khác nhau.
bánh trôi|Viên bột nếp nhỏ bọc nhân ngọt, khi chín nổi lên trong nồi nước.
bánh trung thu|Bánh làm vào dịp rằm tháng tám, thường có vỏ và nhân.
bánh ú|Bánh nếp gói lá thành khối nhọn, có loại có nhân.
bánh ướt|Lá bánh bột gạo tráng hấp mỏng, ăn khi còn mềm ẩm.
bánh xe|Phần tròn quay quanh trục giúp phương tiện lăn đi.
bánh xèo|Bánh rán mỏng trên chảo, gập lại phủ lên nhân tôm, thịt hoặc giá.
bao bì|Vật liệu dùng để đóng gói và bảo vệ hàng hóa.
bao bọc|Che chắn hoặc bảo vệ xung quanh mọi phía.
bao bố|Bao lớn dùng để đựng và vận chuyển hàng hóa nặng.
bao dung|Thái độ rộng lượng, không trách móc người khác.
bao giờ|Thời điểm nào đó chưa xác định rõ.
bao gói|Đóng gói đồ vật vào bao bì để bảo vệ và vận chuyển.
bao gồm|Chứa đựng tất cả các thành phần hoặc đối tượng bên trong.
bao hàm|Chứa đựng bên trong những ý nghĩa hoặc nội dung.
bao la|Rộng lớn vô cùng, không thể nhìn thấy hết bằng mắt thường.
bao lăm|Số lượng hoặc mức độ của một sự vật, hiện tượng.
bao lâu|Khoảng thời gian kéo dài bao nhiêu.
bao nhiêu|Số lượng cụ thể nào đó, thường dùng để hỏi về con số.
bao phủ|Che kín và bao trùm lên bề mặt của vật khác.
bao quát|Nhìn thấy hoặc nắm được toàn bộ diện mạo.
bao tải|Bao dệt bằng sợi đay hoặc gai dùng đựng đồ.
bao tay|Đồ xỏ vào bàn tay để che, bảo vệ hoặc giữ ấm.
bao tiêu|Nhận mua hết sản phẩm để tiêu thụ thay cho người sản xuất.
bao trùm|Che phủ lên trên và bao kín một vùng không gian rộng lớn.
bao tử|Tên gọi dạ dày, nơi giữ và tiêu hóa bước đầu thức ăn.
bao xa|Hỏi độ dài khoảng cách giữa hai nơi.
bào mòn|Làm bề mặt mỏng hoặc mòn dần qua cọ xát và thời gian.
bào ngư|Động vật biển có vỏ dẹt một mảnh, mặt trong óng ánh.
bảo dưỡng|Trông nom, giữ gìn và sửa chữa thiết bị để dùng được.
bảo đảm|Cam kết chắc chắn rằng việc gì đó sẽ được thực hiện đúng.
bảo hành|Cam kết sửa hoặc thay sản phẩm lỗi trong thời hạn quy định.
bảo hiểm|Hình thức tạo quỹ tiền tệ để bù đắp tổn thất do rủi ro gây ra.
bảo hộ|Hành động giúp đỡ, che chở để an toàn.
bảo lãnh|Cam kết chịu trách nhiệm thay cho người khác nếu họ không làm đúng.
bảo lưu|Giữ lại quyền lợi, thành tích hoặc thời gian học tập.
bảo mật|Giữ kín thông tin quan trọng không cho người khác biết.
bảo quản|Giữ gìn để đồ vật không bị hỏng.
bảo toàn|Giữ cho sự vật, sự việc còn nguyên vẹn, không bị hư hỏng hay mất mát.
bảo tồn|Gìn giữ những gì có giá trị lịch sử hoặc thuộc về cộng đồng để không bị mất đi.
bảo trì|Thực hiện các công việc sửa chữa và bảo dưỡng để duy trì hoạt động.
bảo trợ|Trợ giúp, đỡ đầu về vật chất hoặc tinh thần.
bảo vật|Vật quý được coi trọng và gìn giữ đặc biệt.
bảo vệ|Giữ cho người hoặc vật không bị tổn hại.
bão cát|Luồng gió mạnh cuốn theo cát bụi làm trời đất tối om.
bão tuyết|Cơn gió mạnh cuốn theo tuyết rơi dày đặc.
báo cáo viên|Người trình bày nội dung trước hội nghị.
báo chí|Tổng hợp các tờ báo và tạp chí đưa tin cho công chúng.
báo công|Nói về những việc đã làm tốt để được khen ngợi.
báo danh|Ghi tên vào danh sách để được tham gia thi.
báo điện tử|Loại báo chí hiển thị tin tức, hình ảnh trên màn hình máy tính qua mạng Internet.
báo giá|Viết cho khách hàng biết mức tiền phải trả.
báo giới|Các cơ quan và người làm công tác thông tin, truyền thông.
báo hiệu|Cho biết trước sự việc sắp xảy ra bằng dấu hiệu riêng.
báo nói|Loại báo chí phát tin tức qua sóng vô tuyến để nghe.
báo thức|Làm thức người đang ngủ dậy đúng vào giờ đã hẹn trước.
báo trước|Truyền tin về sự việc hay tình trạng nào đó trước khi nó xảy ra.
báo viết|Loại ấn phẩm in trên giấy, trình bày tin tức và hình ảnh.
bát giác|Hình đa giác có tổng cộng tám góc và tám cạnh nối liền nhau.
bát ngát|Rộng lớn vô tận, bao la đến mức không thấy hết.
bát nháo|Trạng thái hỗn độn, rối rắm, không có trật tự hay sắp xếp rõ ràng.
bạt ngàn|Nhiều vô kể trải rộng trên diện tích lớn.
báu vật|Đồ vật có giá trị rất cao, quý hiếm và đáng trân trọng.
bay bổng|Tư duy bay cao, thoát khỏi thực tế tầm thường.
bay hơi|Chuyển từ chất lỏng hoặc rắn thành hơi.
bay lượn|Di chuyển trên không trung bằng cách bay và lượn.
bày biện|Sắp đồ vật ra cho thuận tiện hoặc đẹp mắt.
bày đặt|Tự ý tạo ra chuyện phức tạp không cần thiết.
bày tỏ|Nói ra suy nghĩ, cảm xúc một cách chân thành.
bày vẽ|Nghĩ thêm cách làm hoặc bày thêm việc không thật cần thiết.
băn khoăn|Không yên lòng vì có điều cần phải suy nghĩ.
bắn tin|Gửi lời nhắn nhờ người khác chuyển đến.
băng chuyền|Dải băng chạy liên tục để vận chuyển hàng hóa.
băng dính|Vải hoặc nhựa có chất dính ở một mặt dùng để dán.
băng đô|Dải vải quấn quanh trán để giữ tóc gọn và thấm mồ hôi.
băng giá|Lớp băng do nước đóng lại khi nhiệt độ xuống thấp.
băng nhạc|Đĩa từ lưu trữ âm thanh các bài hát, bản nhạc.
băng rôn|Dải vải hoặc vật liệu dài có chữ, hình để treo truyền thông điệp.
băng thông|Khả năng truyền dữ liệu của đường kết nối trong một đơn vị thời gian.
băng từ|Dải vật liệu có lớp từ tính để ghi âm, hình hoặc dữ liệu.
bằng cấp|Văn bằng chứng nhận kết quả học tập sau khi thi đỗ.
bằng chứng|Cái dùng để chứng minh sự thật của một vấn đề.
bằng lăng|Cây thường trồng ven đường, nhiều loài nở những chùm hoa tím.
bằng lòng|Cho là thỏa đáng, đồng ý với điều đó.
bằng nhau|Có cùng số lượng, kích thước hay giá trị khi so sánh.
bằng phẳng|Bề mặt phẳng lì, không có chỗ lồi lõm hay gồ ghề.
bằng vai|Ngang hàng với nhau về thứ bậc, địa vị hoặc quan hệ trong gia đình.
bắp cải|Rau có nhiều lá cuộn chặt vào nhau thành bắp.
bắp chân|Phần thịt cơ nổi ở phía sau cẳng chân.
bắp đùi|Phần thịt lớn ở phía trước đùi.
bắp thịt|Cơ bắp có hình khối phình to ở giữa và thuôn nhỏ ở hai đầu.
bắt buộc|Buộc phải làm theo ý muốn của người khác.
bắt chước|Làm theo cách làm, hành động hoặc hình dáng của người khác.
bắt đầu|Khởi động hoặc làm đầu tiên một công việc nào đó.
bắt gặp|Gặp phải một cách ngẫu nhiên.
bắt mắt|Gây ấn tượng đẹp nhờ vẻ ngoài nổi bật, thu hút.
bắt nguồn|Có điểm xuất phát hoặc nguyên nhân từ một nơi nào đó.
bắt rễ|Cây non đã cắm rễ chắc vào đất để sống.
bắt tay|Nắm tay nhau trong chốc lát để chào hoặc thể hiện thiện chí.
bậc thầy|Người có trình độ chuyên môn cao, đáng được tôn trọng và noi theo.
bẩm sinh|Vốn có sẵn từ khi mới chào đời.
bấm bụng|Nén đau trong bụng, không cho người khác thấy.
bẩn thỉu|Không sạch sẽ, hôi thối và đồ đạc bừa bãi.
bận bịu|Đang làm nhiều việc không rảnh tay.
bận tâm|Dành tâm trí, suy nghĩ và lo lắng về một vấn đề nào đó.
bâng khuâng|Buồn nhớ mông lung, xen lẫn cảm giác ngẩn ngơ.
bâng quơ|Không tập trung vào một mục tiêu hay đối tượng cụ thể nào cả.
bập bẹ|Lời nói còn nhỏ, chưa rõ ràng, chưa thành câu trọn vẹn.
bập bênh|Trò chơi có tấm ván tựa giữa để hai đầu lần lượt lên xuống.
bập bùng|Tỏa sáng nhấp nháy, lúc cao lúc thấp.
bất an|Cảm thấy lo lắng, không yên tâm hay chắc chắn về điều gì.
bất biến|Không thay đổi, không biến động dù hoàn cảnh có khác đi.
bất cẩn|Không chú ý kỹ, làm việc thiếu cẩn trọng.
bất cập|Tình trạng chưa đạt được mức độ cần thiết hoặc không phù hợp với yêu cầu.
bất chợt|Xảy đến nhanh, vào lúc không được chờ đợi.
bất cứ|Chỉ bất kỳ thứ gì cũng được chấp nhận hoặc thực hiện.
bất đắc dĩ|Không thể làm cách khác, buộc phải chịu thế.
bất đẳng thức|Mối quan hệ giữa hai số hoặc biểu thức có dấu lớn hơn hoặc nhỏ hơn.
bất động|Không di chuyển hay thay đổi vị trí.
bất động sản|Đất cùng nhà cửa hoặc công trình gắn liền với đất.
bất hợp tác|Không tham gia hợp tác hoặc làm việc chung với người khác.
bất kể|Không phân biệt hay loại trừ bất kỳ trường hợp nào.
bất khả kháng|Không thể ngăn cản hay chống lại bằng bất kỳ cách nào.
bất khả thi|Không thể thực hiện được trong những điều kiện đang có.
bất khuất|Không chịu khuất phục trước áp lực hay đối thủ.
bất lợi|Không thuận lợi, gây khó khăn cho việc làm.
bất ngờ|Việc xảy ra mà người ta không lường trước được hay không tính toán sẵn.
bất tận|Nhiều đến mức dường như không bao giờ có thể kết thúc hoặc cạn kiệt.
bất thành|Không đạt được mục tiêu hoặc kết quả như mong đợi.
bất thần|Xảy ra bất ngờ, không thể lường trước được.
bất thình lình|Xảy ra một cách bất ngờ mà không ai đoán trước được.
bất thường|Không giống với trạng thái hay quy luật thông thường.
bất tiện|Không thuận lợi, gây khó khăn cho việc làm hoặc sinh hoạt.
bất tín nhiệm|Không tin tưởng hoặc nghi ngờ về sự trung thực của người khác.
bật mí|Nói ra những điều kín đáo, chưa ai biết đến trước đó.
bầu bạn|Làm bạn với nhau, cùng nhau vui chơi.
bầu bĩnh|Tròn trịa, đáng yêu (thường chỉ mặt).
bầu dục|Có dáng cong khép kín, dài hơn bề ngang như quả trứng.
bầu trời|Không gian rộng lớn nằm ngay phía trên đầu con người.
bây giờ|Khoảng thời gian hiện tại, lúc đang nói chuyện.
bấy lâu|Suốt khoảng thời gian khá dài cho đến mốc đang nói.
bấy nhiêu|Số lượng vừa nhắc đến, ngần ấy.
be bé|Hơi nhỏ về kích thước hoặc âm thanh.
bé bỏng|Nhỏ bé, yếu ớt và chưa trưởng thành.
bé con|Đứa trẻ, người còn nhỏ tuổi.
bé gái|Cô gái còn nhỏ tuổi, thường dưới mười sáu tuổi.
bé hạt tiêu|Người có thân hình nhỏ nhưng trí tuệ sắc sảo, kinh nghiệm dày dặn.
bé nhỏ|Kích thước hoặc quy mô rất nhỏ bé.
bé tí|Cực kỳ nhỏ bé.
bẽn lẽn|Thẹn thùng, rụt rè và cảm thấy ngượng nghịu.
bén rễ|Rễ cây đâm sâu và phát triển tốt trong lòng đất.
bèo bọt|Ít giá trị, không đáng kể.
béo bở|Dễ dàng sinh ra nhiều lợi nhuận hoặc tiền bạc.
bê bết|Bị chất bẩn dính chặt và lan khắp nơi.
bê tông|Đá nhân tạo làm từ cát, sỏi trộn xi măng để xây dựng.
bê tông cốt thép|Loại bê tông được nhúng thêm thanh sắt bên trong nhằm tăng độ bền và khả năng chịu lực.
bề bộn|Nhiều việc rối rắm, không ngăn nắp.
bề mặt|Phần giới hạn bên ngoài của một hình hoặc vật.
bề ngoài|Hình dáng, vẻ bề mặt nhìn thấy được của sự vật.
bề thế|Quy mô lớn, uy quyền mạnh mẽ hoặc tầm ảnh hưởng sâu rộng.
bể bơi|Nơi chứa nước lớn dành riêng cho việc bơi lội.
bế mạc|Kết thúc trang trọng một sự kiện, khóa học hay hội nghị.
bế tắc|Không lối thoát, việc làm bị dừng hẳn, không thể tiến thêm.
bệ đỡ|Vị trí thấp hơn dùng để nâng đỡ, giữ cho vật trên không ngã.
bên cạnh|Nằm kế bên, sát cạnh hoặc ở gần.
bên ngoài|Mặt hướng ra phía bên kia của vật.
bên trong|Phần nằm ở giữa, phía trong của sự vật hoặc hiện tượng.
bền bỉ|Duy trì sức hoặc sự cố gắng lâu mà không dễ bỏ cuộc.
bền chí|Bền lòng theo đuổi việc khó mà không nản lòng.
bền gan|Kiên cường đối mặt thử thách, không chùn bước.
bền vững|Mạnh mẽ, chắc chắn và tồn tại lâu dài.
bến đò|Nơi dừng thuyền, bè để đón khách qua sông.
bến tàu|Chỗ tàu ghé cho khách lên xuống hoặc bốc dỡ hàng.
bến xe|Điểm tập trung các chuyến xe khách để đón và trả người đi.
bênh|Đứng về phía người khác để bảo vệ họ.
bếp núc|Nơi nấu ăn hoặc công việc nấu ăn.
bi bô|Nói lắp bắp, chưa rõ ràng.
bi hài|Cảm xúc vừa buồn thương, đau lòng vừa buồn cười, nghịch lý.
bi quan|Có cách nhìn tiêu cực, không tin vào tương lai.
bi tráng|Buồn thương nhưng đầy khí phách.
bi ve|Viên bi nhỏ bằng thủy tinh, trẻ em hay dùng để chơi.
bì bõm|Tiếng nước chảy và vỗ nhẹ liên tục khi lội qua vùng nước nông.
bí ẩn|Chứa đựng điều khó hiểu, khó đoán.
bí bách|Cảm thấy ngột ngạt, khó chịu vì không gian chật hẹp hoặc thiếu lối thoát.
bí đao|Dây leo cho quả dài, ruột trắng, thường dùng nấu canh.
bí mật|Thông tin chỉ được một số ít người biết, không công khai.
bí ngô|Loại bí có ruột vàng cam và hạt dẹt, thường dùng nấu súp.
bí quyết|Cách làm có tác dụng rõ mà không phải ai cũng biết.
bí truyền|Được giữ kín và truyền lại cho một số ít người.
bị động|Chịu ảnh hưởng từ bên ngoài thay vì chủ động quyết định.
biên bản|Văn bản ghi nhận diễn biến và kết quả của một việc.
biên dịch|Dịch nội dung văn bản từ ngôn ngữ này sang ngôn ngữ khác.
biên đạo|Người sáng tác và chỉ đạo các động tác trong điệu múa.
biên độ|Độ lệch lớn nhất so với vị trí cân bằng của một dao động.
biên giới|Chỗ ranh giới giữa hai vùng lãnh thổ hoặc hai quốc gia.
biên khảo|Tìm hiểu kỹ lưỡng và tổng hợp lại thành văn bản.
biên kịch|Viết hoặc chỉnh sửa kịch bản cho sân khấu và phim ảnh.
biên lai|Giấy xác nhận số tiền hoặc vật đã được giao nhận.
biên nhận|Giấy xác nhận đã nhận tiền, hàng hoặc tài liệu nào đó.
biên niên|Ghi chép sự kiện theo trình tự thời gian từng năm.
biên soạn|Tập hợp, lựa chọn tài liệu rồi viết thành sách.
biên tập|Việc thu thập và chỉnh sửa tài liệu để hoàn thành sách báo.
biên tập viên|Người chọn lọc, chỉnh sửa và hoàn thiện nội dung trước khi công bố.
biển|Vùng nước mặn rộng lớn nối với đại dương.
biển báo|Bảng có dấu hiệu hoặc chữ để hướng dẫn hay cảnh báo.
biển báo giao thông|Biển đặt trên đường để cảnh báo hoặc hướng dẫn người tham gia giao thông.
biển cả|Biển rộng lớn, thường nói khi hình dung khoảng nước mênh mông.
biển hiệu|Biển đề tên cửa hàng, địa chỉ và thông tin liên lạc để phục vụ kinh doanh.
biến ảo|Thay đổi hình dáng hoặc màu sắc một cách khó lường.
biến cải|Thay đổi hình dáng hoặc tính chất thành cái khác.
biến dạng|Thay đổi hình dáng khiến nó không còn giống ban đầu.
biến đổi|Làm thay đổi hình dạng hoặc tính chất của sự vật.
biến động|Thay đổi đáng kể khiến tình hình không còn như trước.
biến hình|Thay đổi hình dáng, hình thái.
biến mất|Trở nên không còn thấy được hoặc không thể tìm lại được.
biến tấu|Thay đổi giai điệu hoặc hình thức để làm phong phú thêm bài nhạc.
biến trở|Thiết bị điều chỉnh điện trở để kiểm soát dòng điện.
biện bạch|Nói rõ mọi sự thật để giải thích hoặc xin lỗi.
biện minh|Lời nói nhằm bảo vệ hành vi sai trái hoặc làm cho việc làm trở nên hợp lý.
biện pháp|Cách cụ thể được dùng để xử lý một vấn đề.
biêng biếc|Màu xanh đậm, trong trẻo và đẹp mắt.
biếng|Ngại làm việc dù có khả năng làm.
biết bao|Nhiều đến mức khiến người nói ngạc nhiên hoặc xúc động.
biết chừng nào|Biết đến mức độ vô cùng lớn, không thể đo đếm hay giới hạn được.
biết đâu|Phỏng đoán một khả năng có thể xảy ra mà chưa chắc chắn.
biết điều|Hiểu rõ lẽ phải, cư xử đúng mực và biết tự trọng.
biết ơn|Ghi nhận điều tốt người khác đã làm cho mình.
biết thân|Hiểu rõ hậu quả, biết dừng lại việc sai.
biết ý|Hiểu được mong muốn hay ý định của người khác.
biệt danh|Tên gọi khác thân mật hoặc vui vẻ thay cho tên thật.
biệt lập|Tách rời ra một mình, không có người khác ở chung quanh.
biệt tài|Khả năng đặc biệt, xuất sắc mà ít người trong xã hội có được.
biệt thự|Ngôi nhà riêng biệt, thường xây ở vùng núi, ven biển hoặc nông thôn để nghỉ dưỡng.
biệt tích|Hoàn toàn không còn thấy dấu vết hay tin tức gì cả.
biểu cảm|Biểu lộ cảm xúc qua lời nói hoặc nét mặt.
biểu diễn|Trình bày các tiết mục văn nghệ trước đám đông.
biểu dương|Khen ngợi công khai để mọi người cùng biết.
biểu đạt|Thể hiện, làm rõ tư tưởng hoặc cảm xúc bằng lời nói hay hành động.
biểu đồ|Hình vẽ dùng để so sánh các con số hoặc các đại lượng khác nhau.
biểu hiện|Dấu hiệu thể hiện ra bên ngoài hoặc làm rõ nội dung bên trong.
biểu lộ|Thể hiện rõ ràng ra bên ngoài bằng hành động hoặc lời nói.
biểu mẫu|Khung soạn sẵn những mục cần điền để thu thập thông tin.
biểu ngữ|Tấm vải hoặc giấy lớn có viết lời kêu gọi treo ở nơi đông người.
biểu quyết|Hành động thể hiện ý kiến cá nhân để đưa ra quyết định chung.
biểu thị|Tỏ ra, cho thấy điều gì đó.
biểu thuế|Bảng kê mức thuế cho từng loại hàng.
biểu thức|Dãy các ký hiệu toán học được viết đúng quy tắc để tính toán.
biểu trưng|Hình tượng đại diện cho ý nghĩa hoặc vật cụ thể.
biểu tượng|Hình, dấu hoặc vật đại diện cho một ý nghĩa rộng hơn.
biếu|Tặng vật gì để tỏ lòng kính trọng.
bịn rịn|Dùng dằng, không muốn rời xa người thân vì nặng tình.
bình|Đồ có lòng rỗng để đựng nước hoặc cắm hoa.
bình an|Trạng thái yên tĩnh, không có chuyện xấu hay nguy hiểm xảy ra.
bình chọn|Chọn ra người hoặc sự vật tốt nhất dựa trên ý kiến và sự lựa chọn của nhiều người.
bình dân|Người dân thường không thuộc tầng lớp quý tộc hay quan lại.
bình dị|Giản dị, khiêm tốn trong tác phong và thái độ.
bình đẳng|Có vị thế, cơ hội hoặc quyền như nhau, không bị phân biệt.
bình điện|Thiết bị chứa và cung cấp điện tích trữ cho xe hay máy.
bình giảng|Phân tích và bình luận về nghệ thuật, ý nghĩa trong tác phẩm văn học.
bình lặng|Yên và ít biến động, như mặt nước lúc không có gió.
bình luận|Nêu nhận xét và cách hiểu riêng về một việc hay tác phẩm.
bình luận viên|Người chuyên phân tích, đánh giá sự kiện trên báo chí hay truyền hình.
bình minh|Khoảng đầu ngày khi chân trời bắt đầu sáng.
bình nguyên|Vùng đất bằng phẳng, rộng lớn, thấp hơn mặt nước biển.
bình nóng lạnh|Thiết bị làm nóng nước và thường giữ nước nóng để dùng dần.
bình ổn|Giữ cho tình hình ổn định, không để xảy ra biến động hay thay đổi thất thường.
bình phẩm|Phân tích và nêu ý khen chê, đánh giá về người hay việc.
bình phong|Vật chắn gió, bụi hoặc che tầm nhìn, thường làm bằng gỗ, tre hoặc vải.
bình phục|Trở lại trạng thái khỏe mạnh sau khi bị ốm hoặc thương.
bình phương|Lấy số đó nhân với chính nó một lần.
bình tâm|Giữ được sự bình tĩnh và làm chủ được suy nghĩ, cảm xúc.
bình thản|Bình tĩnh, không lo sợ hay bối rối trước chuyện gì.
bình thường|Trạng thái phổ biến, không có gì lạ hoặc đặc biệt.
bình tĩnh|Trạng thái tâm lý ổn định, không hoảng loạn và làm chủ được hành động trong mọi tình huống.
bình xét|Đánh giá, xem xét kỹ lưỡng để xếp loại.
bình xịt|Bình chứa khí nén hoặc chất lỏng dùng để phun mạnh ra ngoài.
bình yên|Trạng thái không có sự xáo trộn, lo âu hay bất an nào.
bít tất|Đồ dệt ôm bàn chân, thường mang bên trong giày.
bít tết|Món thịt thái miếng dày, thường áp chảo hoặc nướng.
bịt kín|Che phủ hoặc ngăn chặn hoàn toàn sự tiếp xúc.
bịt miệng|Ngăn chặn miệng người khác để họ không thể nói ra lời.
bò bía|Món cuốn bánh tráng trộn dừa, mạch nha và vừng đen.
bò cạp|Động vật có tám chân, hai càng trước và đuôi cong mang ngòi.
bò sát|Nhóm động vật có xương sống gồm rùa, thằn lằn, rắn và cá sấu.
bò tót|Bò rừng lớn có thân lực lưỡng và đôi sừng cong.
bỏ cuộc|Ngừng tham gia cuộc thi hoặc bỏ giữa chừng.
bỏ đi|Đi đến nơi khác và rời bỏ chỗ cũ.
bỏ hoang|Bỏ không canh tác hay sử dụng trong thời gian dài.
bỏ lỡ|Không tận dụng được cơ hội có sẵn.
bỏ túi|Có kích thước nhỏ gọn, dễ dàng bỏ vào túi mang theo.
bó bột|Dùng bột thạch cao ép chặt quanh xương gãy để cố định.
bó buộc|Buộc phải làm theo quy định, không được tự do.
bó gối|Ngồi co chân lại, tay ôm đầu gối để suy nghĩ.
bó tay|Không thể làm gì thêm, đành chịu thua số phận.
bọ chét|Bọ dẹp sống ký sinh trên thú.
bọ hung|Loài bọ cánh cứng màu đen, kích thước to bằng ngón chân cái.
bọ ngựa|Côn trùng có đôi chân trước gập lại để chộp mồi.
bọ rùa|Côn trùng nhỏ có lưng tròn, nhiều loài mang những chấm màu.
bói cá|Chim có mỏ dài thẳng, thường lao xuống nước bắt cá.
bong bóng|Khối khí được bao trong lớp màng mỏng, như khi thổi nước xà phòng.
bỏng ngô|Hạt ngô nổ phồng khi đun nóng.
bóng bàn|Môn đánh quả bóng nhỏ qua lưới trên một mặt bàn.
bóng bay|Túi khí mỏng căng phồng, dùng làm đồ chơi bay trên không.
bóng bầu dục|Môn đồng đội dùng quả bóng thuôn, có thể ôm chạy hoặc chuyền bóng.
bóng chày|Môn thể thao dùng gậy đánh bóng rồi chạy qua các gôn.
bóng chuyền|Môn hai đội dùng tay đưa bóng qua lưới cao.
bóng dáng|Hình dáng mờ ảo, thấp thoáng khó nhìn rõ của người hoặc vật.
bóng đá|Môn hai đội chủ yếu dùng chân đưa bóng vào khung thành.
bóng đèn|Bộ phận nhận điện và phát ra ánh sáng.
bóng điện|Thiết bị dùng để tạo ra ánh sáng nhờ dòng điện.
bóng gió|Nói chuyện vòng vo, không đi thẳng vào vấn đề.
bóng láng|Bề mặt bóng và trơn láng đến mức phản chiếu rõ.
bóng loáng|Bóng sáng đến mức có thể phản chiếu hình ảnh bên ngoài.
bóng mát|Nơi có cây cối che nắng, không bị ánh mặt trời chiếu trực tiếp.
bóng mềm|Môn đánh bóng bằng gậy có luật gần bóng chày, dùng quả bóng lớn hơn.
bóng ném|Môn đồng đội chuyền và ném bóng bằng tay vào cầu môn.
bóng nước|Môn thể thao dưới nước, người chơi chuyền bóng để ghi bàn.
bóng râm|Chỗ mát mẻ, tránh ánh nắng trực tiếp.
bóng rổ|Môn hai đội ghi điểm bằng cách đưa bóng qua vòng rổ.
bóng tối|Khoảng không thiếu ánh sáng đến mức khó nhìn thấy vật.
boong|Sàn ngoài trời trên thân tàu.
bóp còi|Nén tay vào còi xe để phát âm báo hiệu.
bọt biển|Động vật thủy sinh đơn giản, có nhiều lỗ nhỏ để lọc nước.
bồ câu|Chim có ngực đầy, thường gù và được nuôi ở nhiều nơi.
bổ dưỡng|Có chất dinh dưỡng giúp cơ thể khỏe mạnh và phát triển.
bổ ích|Có lợi ích thiết thực và cần thiết cho cuộc sống.
bổ khuyết|Thêm vào chỗ còn thiếu để đầy đủ.
bổ nhiệm|Cử người vào giữ chức vụ lãnh đạo.
bổ sung|Thêm vào để làm cho đầy đủ hoặc phong phú hơn.
bổ túc|Thêm vào để làm cho đầy đủ hoặc hoàn thiện hơn.
bố cục|Cách sắp các phần trong bài viết, bức ảnh hoặc tác phẩm.
bố thí|Việc ban phát tài sản hoặc của cải cho người khác.
bố trí|Sắp xếp các việc, người hoặc đồ vật theo trật tự nhất định với mục đích cụ thể.
bộ dạng|Ngoại hình và cách đứng ngồi của người ta nhìn chung.
bộ đồ|Những món quần áo hoặc vật dụng được dùng chung thành bộ.
bộ gõ|Nhóm nhạc cụ được đánh bằng tay hoặc dụng cụ gõ để tạo ra âm thanh.
bộ luật|Tập hợp các quy định pháp luật thành một hệ thống thống nhất.
bộ mặt|Hình dáng bề ngoài hoặc nét mặt thể hiện suy nghĩ, tình cảm bên trong.
bộ môn|Một lĩnh vực nhỏ thuộc một ngành học lớn.
bộ nhớ|Bộ phận lưu trữ dữ liệu để máy tính sử dụng khi cần.
bộ phận|Một phần nhỏ thuộc vào tổng thể lớn.
bốc hơi|Chuyển từ dạng lỏng hoặc rắn sang dạng khí.
bộc bạch|Nói thẳng sự thật, không giấu giếm điều gì.
bộc lộ|Làm cho sự thật hoặc cảm xúc hiện rõ ra ngoài.
bộc phát|Xảy ra đột ngột, mạnh mẽ và lan rộng ra xung quanh một cách bất ngờ.
bộc trực|Nói đúng những gì mình nghĩ, không giấu giếm.
bôi trơn|Bôi chất nhờn lên bề mặt chuyển động để giảm ma sát và mài mòn.
bồi bàn|Người phục vụ món ăn và chăm lo bàn của khách ở quán.
bồi dưỡng|Làm tăng thêm sức khỏe bằng chất bổ.
bồi đắp|Thêm đất, cát vào để làm dày, làm chắc cho nền móng.
bồi hồi|Cảm thấy xao xuyến, bồn chồn trong lòng.
bồi thường|Đền lại những thiệt hại đã làm cho người khác.
bối cảnh|Hoàn cảnh chung bao quanh sự việc hoặc con người.
bối rối|Cảm thấy hoang mang, không biết xử lý tình huống như thế nào.
bội chi|Trạng thái chi tiêu vượt quá số tiền thu về trong năm.
bội thu|Thu được nhiều sản phẩm hơn bình thường, nhất là sau vụ mùa.
bôn ba|Di chuyển liên tục nhiều nơi để làm việc hoặc sinh sống.
bôn tẩu|Chạy vạy khắp nơi để kiếm sống, mưu sinh.
bổn phận|Việc mình phải làm theo lẽ phải.
bốn mươi|Số lượng bằng bốn lần mười.
bốn phương|Tất cả mọi hướng và mọi nơi trên thế gian.
bông đùa|Đùa cợt bằng lời nói.
bông gòn|Bông lấy từ cây gòn dùng làm đệm.
bông tai|Trang sức dạng hoa, phụ nữ đeo ở lỗ tai.
bồng bế|Bế ẵm trẻ nhỏ khi di chuyển.
bỗng dưng|Xảy ra bất ngờ mà không thấy dấu hiệu báo trước.
bỗng nhiên|Xảy ra một cách bất ngờ, không ai lường trước được.
bột bắp|Bột mịn làm từ lõi hạt bắp, dùng để tạo độ dính và làm đặc món ăn.
bột chiên|Món làm từ bột chín cắt miếng đem chiên, thường dùng với trứng.
bột gạo|Hạt ngũ cốc đã được xay nhuyễn thành bột mịn để nấu ăn.
bột giặt|Chất tẩy dạng hạt hay bột dùng để làm sạch quần áo.
bột năng|Bột làm từ củ sắn, nấu chín thì trong, đặc và dính.
bột nếp|Bột xay từ gạo nếp, cho khối dẻo dính khi nấu.
bột ngọt|Chất phụ gia thực phẩm dùng để tăng vị ngon, là muối của axit glutamic.
bột nở|Bột dùng để làm bánh nở phồng và xốp mềm.
bột sắn|Loại bột trắng làm từ củ khoai mì dùng để nấu ăn.
bơ phờ|Gương mặt xanh xao, mệt mỏi tột độ.
bơ thực vật|Sản phẩm béo làm chủ yếu từ dầu thực vật, dùng phết bánh hoặc nấu ăn.
bờ bến|Bờ sông, biển, hồ; nơi ranh giới giữa mặt nước lớn với đất liền.
bờ biển|Dải đất tiếp xúc với nước biển.
bờ đê|Dải đất đắp cao chạy ven sông hoặc ven biển để ngăn nước.
bờ vai|Phần thân ở hai bên gốc cổ, phía trên cánh tay.
bỡ ngỡ|Ngạc nhiên, bối rối vì mới lạ hoặc chưa quen.
bơi ếch|Bơi bằng cách tay chân cùng lúc co duỗi đều đặn giống con ếch.
bơi lội|Hoạt động dùng tay, chân hoặc cả thân để di chuyển trong nước.
bởi vì|Từ nối giới thiệu nguyên nhân của điều vừa nói.
bỡn cợt|Trêu đùa, nói chuyện vui vẻ với người khác.
bu lông|Chi tiết cơ khí dạng trụ tròn, dùng để nối và cố định các bộ phận lại với nhau.
bù đắp|Bù lại những tổn thất, thiếu hụt bằng hành động hoặc vật chất tương ứng.
bù lỗ|Bù lại số tiền thua lỗ bằng cách cấp thêm.
bù trừ|Sử dụng phần thừa của cái này để bù đắp cho phần thiếu của cái kia.
búa tạ|Công cụ đập có cán dài và đầu rất nặng, dùng để phá vỡ vật cứng.
bụi bặm|Có nhiều hạt bụi bám hoặc lẫn vào quanh vật.
bụi rậm|Nơi cây cối mọc dày đặc, che kín mặt đất.
bún bò|Món bún nước ăn với thịt bò và các gia vị.
bún chả|Món bún ăn với thịt nướng, rau và nước chấm.
bún đậu mắm tôm|Món ăn gồm bún, đậu rán và mắm tôm cùng nhiều nguyên liệu khác.
bún thang|Món bún nước thường có trứng thái sợi, giò và thịt gà.
bún thịt nướng|Món bún ăn với thịt nướng, rau, nước chấm và thường có lạc rang.
bụng|Phần thân nằm dưới ngực, chứa dạ dày và ruột.
buộc lòng|Phải làm việc dù không muốn vì hoàn cảnh bắt buộc.
buổi biểu diễn|Thời điểm tổ chức trình bày tác phẩm nghệ thuật trước nhiều người xem.
buổi chiều|Khoảng thời gian trong ngày từ lúc mặt trời bắt đầu lặn đến tối hẳn.
buổi sáng|Khoảng thời gian từ khi mặt trời mọc đến lúc mặt trời lên cao.
buổi tối|Phần ngày sau khi trời tối và trước lúc đêm khuya.
buổi trưa|Phần giữa ban ngày, thường quanh thời điểm ăn bữa chính giữa ngày.
buôn bán|Mua hàng rồi bán lại để tạo thu nhập.
buồn|Cảm thấy không vui vì điều không như ý.
buồn cười|Gây ra cảm giác vui vẻ, muốn bật cười vì sự khôi hài.
buồn ngủ|Cảm thấy muốn ngủ, cần nghỉ ngay.
buồn tênh|Cảm thấy buồn vì thiếu vắng điều gì đó mơ hồ.
buồn thảm|Cảm thấy đau lòng và bi thương.
buông lỏng|Không siết chặt, để cho tự do, lỏng lẻo.
buông lơi|Thả lỏng, không giữ chặt hoặc quản lý nghiêm ngặt.
buông tha|Không giữ lại nữa mà để cho người hoặc vật tự do.
buông thõng|Để vật gì đó rơi xuống tự do không giữ chặt.
buồng lái|Không gian riêng trong xe hoặc máy để người điều khiển ngồi.
buốt|Có cảm giác lạnh hoặc nhói thấm sâu.
buột miệng|Nói ra lời không kịp nghĩ, thường là lời không nên nói.
búp bê|Đồ chơi có hình người, thường để mặc quần áo và chơi đóng vai.
búp măng|Phần chồi non, mầm xanh của cây tre hoặc cây trúc.
bút bi|Bút dùng viên bi nhỏ ở đầu để đưa mực lên giấy.
bút chì|Bút có lõi rắn để lại nét có thể xóa bằng tẩy.
bút danh|Tên một tác giả chọn dùng khi công bố tác phẩm.
bút lông|Bút có chùm sợi mềm ở đầu để đưa mực hoặc màu.
bút máy|Cây bút có bình mực chứa bên trong để tự động cung cấp mực khi viết.
bút mực|Bút viết bằng mực lỏng dẫn ra đầu ngòi.
bút nghiên|Bút và nghiên của người xưa, chỉ việc học hành văn chương.
bút pháp|Cách một tác giả dùng chữ, nét hay hình ảnh để thể hiện phong cách.
bút thử điện|Thiết bị cầm tay dùng kim tiếp xúc để báo hiệu sự có mặt của dòng điện.
bút toán|Bản ghi chép về thu chi của xí nghiệp hay cơ quan.
bút vẽ|Dụng cụ cầm tay đưa màu lên giấy, vải hoặc bề mặt khác.
bừa bãi|Không sắp xếp gọn gàng, thiếu trật tự và nền nếp.
bừa bộn|Ngổn ngang, lộn xộn, không có trật tự.
bữa ăn|Lần một người hay nhiều người ngồi lại để ăn.
bữa tiệc|Bữa ăn lớn với nhiều người cùng tham gia.
bức bách|Buộc người khác phải làm việc ngay lập tức, không cho phép trì hoãn.
bức thiết|Cực kỳ quan trọng, cần phải xử lý ngay lập tức.
bức tranh|Tác phẩm nghệ thuật được vẽ bằng bút màu trên giấy hoặc vải.
bực bội|Cảm thấy khó chịu, tức giận vì không vừa lòng mà không làm gì được.
bực dọc|Cảm thấy khó chịu, bực bội trong lòng vì điều gì đó.
bực mình|Cảm thấy khó chịu, bức bối trong người; nổi giận, nổi cơn.
bực tức|Cảm thấy khó chịu, giận dữ vì một chuyện gì đó.
bước|Đưa một chân lên trước để di chuyển.
bước đầu|Thời điểm khởi đầu của một công việc hay sự việc.
bước đi|Cách di chuyển của chân hoặc quá trình phát triển sự việc từng bước.
bước đường|Khoảng thời gian hoặc hoàn cảnh mà một người trải qua.
bước ngoặt|Thời điểm thay đổi hoàn toàn hướng đi của sự việc.
bước sóng|Khoảng cách giữa hai đỉnh sóng liên tiếp trên cùng một sóng đều.
bưởi chùm|Loài cây nhiệt đới có quả lớn, vị chua ngọt, vỏ dày, thịt nhiều nước.
bươm bướm|Côn trùng có hai đôi cánh rộng mang lớp vảy nhỏ nhiều màu.
bướm đêm|Loài côn trùng cánh vẩy, thân dày, hoạt động vào ban đêm.
bướng bỉnh|Khăng khăng giữ ý mình dù người khác đã khuyên bảo.
bứt phá|Vượt qua giới hạn cũ để đạt thành tích tốt hơn.
bưu chính|Lĩnh vực nhận, chuyển và phát thư hay bưu phẩm.
bưu cục|Nơi làm việc, giao dịch và phân phối thư tín của cơ quan bưu điện.
bưu điện|Nơi nhận gửi thư, bưu phẩm và thực hiện các dịch vụ bưu chính.
bưu kiện|Gói hàng gửi qua mạng lưới bưu chính.
bưu tá|Người chuyên đi giao nhận thư từ và báo chí cho dân.
ca cao|Cây nhiệt đới có hạt dùng để làm sô cô la và đồ uống.
ca dao|Câu hát dân gian truyền miệng, không theo quy tắc cố định.
ca hát|Dùng giọng hát để thể hiện giai điệu.
ca khúc|Bản nhạc có lời được viết để hát.
ca kịch|Thể loại sân khấu kết hợp giữa diễn xuất và hát, khác với kịch chỉ dùng lời nói.
ca múa|Biểu diễn nghệ thuật kết hợp giữa hát và nhảy múa.
ca ngợi|Nói lên điều tốt đẹp của người, việc hay thành tựu.
ca nhạc|Nghệ thuật kết hợp giữa âm thanh nhạc cụ và giọng hát.
ca nô|Thuyền nhỏ chạy bằng động cơ, có vách cao và buồng lái.
ca trù|Loại hình hát truyền thống có phách và đàn đáy đệm.
ca tụng|Nói lên những điều tốt đẹp để khen ngợi, tôn vinh.
ca từ|Lời viết trong bài hát.
cà chua|Quả mọng thường đỏ khi chín, dùng ăn sống hoặc nấu sốt.
cà cuống|Côn trùng nước cỡ lớn, con đực có chất thơm đặc trưng.
cà kheo|Đồ dùng bằng hai cây dài có chỗ đứng chân để đi trên đất lầy.
cà phê|Đồ uống pha từ hạt rang xay, có mùi thơm và vị đắng.
cà phê trứng|Đồ uống kết hợp cà phê với lớp trứng đánh bông.
cà ri|Món nấu với hỗn hợp gia vị thơm, thường dùng kèm cơm hay bánh.
cà rốt|Rau ăn củ thường có màu cam và hình thon dần.
cà tím|Loại cà quả thường dài, vỏ tím, thịt mềm sau khi nấu.
cả thảy|Tổng số lượng mọi thứ tính chung lại.
cả tin|Tin người một cách dễ dàng mà không suy nghĩ kỹ.
cá biển|Tên chung các loài cá sống tự nhiên trong nước mặn ở biển.
cá biệt|Độc nhất, không giống ai, không thuộc nhóm chung.
cá bống|Tên chung của nhiều loài cá nhỏ thường sống gần đáy nước.
cá chép|Cá nước ngọt thân dày, vảy lớn, có râu ngắn gần miệng.
cá cơm|Loài cá nhỏ sống thành đàn trong biển, thường dùng làm thực phẩm.
cá đối|Cá thân dài phủ vảy bạc, thường gặp ở vùng nước ven biển.
cá đuối|Cá có thân dẹp bè ngang, vây ngực mở rộng và đuôi dài.
cá heo|Thú sống dưới nước, có phổi, bơi nhanh và thường sống theo đàn.
cá hồi|Loài cá lớn sống ở biển, thịt màu hồng rất ngon.
cá hộp|Cá đã được đóng gói vào hộp kim loại hoặc nhựa để bảo quản.
cá kho|Món cá nấu lâu với gia vị và một ít nước cho vị đậm.
cá kiếm|Cá biển lớn có phần hàm trên vươn dài như thanh kiếm.
cá mập|Cá có bộ xương bằng sụn, mang mở thành các khe hai bên đầu.
cá mè|Cá nước ngọt thân dẹp, thường lọc thức ăn nhỏ trong nước.
cá mòi|Cá biển nhỏ thân bạc thường đi thành đàn.
cá ngừ|Cá biển bơi nhanh, thân thuôn và thịt chắc.
cá ngựa|Cá nhỏ có đầu giống đầu ngựa và chiếc đuôi có thể cuộn.
cá nhà táng|Cá voi có răng, đầu lớn gần hình hộp và có khả năng lặn sâu.
cá nhân|Một con người được xét riêng, phân biệt với tập thể.
cá sấu|Bò sát lớn sống ven nước, có mõm dài và đuôi khỏe.
cá tai tượng|Cá nước ngọt cỡ lớn, thân dẹp cao, thường được nuôi làm thực phẩm.
cá tầm|Cá thân dài có các hàng tấm xương cứng chạy dọc thân.
cá thể|Một cơ thể sống riêng lẻ.
cá thu|Cá biển thân thuôn, thường có những vệt sẫm trên lưng.
cá tính|Tính cách riêng biệt, độc đáo vốn có của mỗi người, khác với người khác.
cá trê|Cá nước ngọt da trơn có râu quanh miệng.
cá vàng|Cá cảnh nước ngọt có nhiều giống mang màu vàng cam.
cá voi|Thú biển thở bằng phổi và nuôi con bằng sữa.
cách|Lối thực hiện để đạt điều mong muốn.
cách biệt|Có khoảng xa đáng kể về vị trí, mức độ hay tình trạng.
cách điện|Ngăn chặn dòng điện đi qua vật liệu.
cách ngôn|Lời nói ngắn gọn, sâu sắc được truyền lại qua nhiều đời để làm chuẩn mực hành xử.
cách tân|Đổi mới cách làm việc, phá bỏ lối cũ để tạo ra cái mới.
cách thức|Phương pháp, hình thức để thực hiện một hành động cụ thể.
cách trở|Xa cách và bị vật gì ngăn trở không thể gần nhau.
cài đặt|Ghép phần mềm hoặc thiết bị vào máy tính để hoạt động.
cải biên|Sửa đổi lại nội dung hoặc hình thức để phù hợp với nhu cầu mới.
cải cách|Sửa đổi những điều chưa tốt để phù hợp với hoàn cảnh mới.
cải củ|Rau họ cải trồng chủ yếu để thu phần rễ phình to thành củ.
cải cúc|Loài rau thân nhỏ, lá thơm dùng để nấu ăn.
cải lương|Việc sửa đổi để tốt hơn hoặc một loại hát cải cách ở miền Nam.
cải thảo|Cải lá bao phủ nhau, ngoài xanh đậm, trong xanh nhạt, cuống trắng, ăn được.
cải thìa|Cải màu vàng, cuống trắng to, dùng nấu canh hoặc xào.
cải thiện|Làm cho tình trạng hoặc chất lượng trở nên tốt hơn.
cải tiến|Thay đổi cách làm hoặc thiết kế để tiến bộ hơn, tốt hơn so với trước.
cải tổ|Sắp xếp lại tổ chức để hoạt động hiệu quả hơn.
cái tôi|Ý thức về bản thân, giá trị và phẩm chất riêng của mỗi người.
cam đoan|Khẳng định chắc chắn và hứa chịu trách nhiệm.
cam kết|Việc hứa chắc chắn sẽ thực hiện đúng những gì đã nói dù trong bất kỳ hoàn cảnh nào.
cảm biến|Thiết bị dùng để chuyển đổi các đại lượng vật lý thành tín hiệu đo lường.
cảm động|Cảm thấy lòng rung động trước sự việc hay cử chỉ tốt đẹp.
cảm giác|Điều nhận thấy qua giác quan hoặc cảm xúc trong lòng.
cảm hứng|Trạng thái tâm hồn tràn đầy cảm xúc mạnh, thúc đẩy óc tưởng tượng và sáng tạo.
cảm kích|Cảm thấy vui và xúc động vì hành động tốt của người khác.
cảm mến|Thương yêu và quý trọng vì thấy người đó đáng khen hoặc đáng nể.
cảm nghĩ|Những suy nghĩ và cảm xúc nảy ra trước một sự việc.
cảm nhận|Tiếp nhận và hiểu điều gì qua cảm giác hoặc trải nghiệm.
cảm ơn|Bày tỏ lòng biết ơn khi được giúp hay nhận điều tốt.
cảm phục|Kính trọng và ngưỡng mộ vì thấy phẩm chất tốt đẹp của người khác.
cảm quan|Nhận biết, cảm nhận trực tiếp bằng mắt, tai, mũi, lưỡi, da.
cảm tạ|Tỏ lòng biết ơn một cách trang trọng và chân thành.
cảm thán|Nói lên những gì trong lòng với giọng đầy cảm xúc.
cảm thấy|Thu nhận thông tin qua mắt, tai, mũi, lưỡi hay da.
cảm thụ|Tiếp nhận và cảm nhận những tác động từ bên ngoài bằng giác quan.
cảm tình|Sự yêu mến và thiện cảm với ai đó.
cảm tưởng|Ý nghĩ xuất hiện khi cảm nhận hoặc xúc động trước sự việc.
cảm xúc|Tình cảm và suy nghĩ nảy sinh từ sự việc.
can dự|Tham gia vào việc làm chung của tập thể.
can trường|Dũng cảm, chịu đựng gian khổ.
cản trở|Tạo ra trở ngại khiến việc làm gì đó trở nên khó khăn hoặc không xong.
cán sự|Người phụ trách một công việc cụ thể trong tổ chức.
cảng|Nơi tàu ghé để nhận khách hoặc chuyển hàng.
cảng hàng không|Sân bay lớn chuyên dùng để bốc dỡ hàng hóa và đón trả hành khách.
cảng vụ|Đơn vị nhà nước phụ trách quản lý và giữ gìn an toàn tại cảng biển.
cáng đáng|Nhận việc khó và chịu trách nhiệm làm.
canh cải|Ăn rau cải hoặc sửa đổi, thay đổi.
canh giữ|Giám sát và bảo vệ an toàn.
canh tác|Trồng trọt, chăm sóc cây cối và đất đai.
cành cây|Phần mọc từ thân hoặc nhánh lớn, thường mang lá.
cảnh báo|Trước báo về việc nguy hiểm sắp xảy ra.
cảnh huống|Tình trạng xảy ra cần phải ứng xử.
cảnh quan|Diện mạo tổng thể của một vùng nhìn qua địa hình, cây và công trình.
cảnh sắc|Đẹp đẽ của thiên nhiên khiến người ta thích thú ngắm nhìn.
cảnh tỉnh|Làm cho người nhận ra sai lầm để sửa đổi.
cảnh trí|Cảnh quan thiên nhiên được sắp xếp hài hòa.
cảnh tượng|Cảnh vật hiện ra trước mắt người nhìn.
cảnh vật|Những gì hiện ra trong phong cảnh ở một nơi.
cánh|Bộ phận chim dang ra để bay.
cánh cửa|Tấm gỗ hoặc kim loại lắp vào bản lề để đóng mở lối đi.
cánh đồng|Khoảng đất canh tác rộng trải ra ngoài làng hay khu dân cư.
cánh hoa|Phần bao ngoài của hoa, thường có màu sắc và mùi thơm.
cánh quạt|Bộ phận hình lá mỏng, khi quay tạo lực đẩy hoặc kéo.
cánh tay|Phần chi trên từ vai đến gần bàn tay.
cạnh tranh|Cố gắng giành phần thắng trong hoạt động cùng lợi ích.
cao áp|Áp lực chất lỏng hoặc khí lớn hơn mức bình thường.
cao cả|Lớn lao về phẩm chất đạo đức, đáng kính trọng và tôn vinh.
cao cấp|Thuộc hạng cao nhất, đứng trên các cấp thấp hơn.
cao đẳng|Trường dạy nghề cao cấp, nằm giữa trung học và đại học.
cao đẹp|Có phẩm chất cao quý và vẻ đẹp lộng lẫy.
cao điểm|Thời điểm hoặc vị trí đạt mức độ cao nhất trong một chu kỳ.
cao độ|Độ lớn của âm thanh hoặc mức độ rất cao.
cao học|Bậc học sau đại học để đào sâu chuyên môn, thường dẫn tới bằng thạc sĩ.
cao hứng|Đang vui vẻ, phấn chấn đột ngột.
cao ngất|Vươn rất cao so với những vật ở xung quanh.
cao nguyên|Vùng đất cao, bằng phẳng và rộng lớn.
cao ốc|Tòa nhà có nhiều tầng vươn cao so với xung quanh.
cao ráo|Có độ cao và bề mặt khô không có nước.
cao sản|Cho ra nhiều sản phẩm, đạt năng suất cao.
cao sang|Vị trí cao quý, trang trọng và xa hoa.
cao tay|Làm việc giỏi, xử lý tình huống khó khăn xuất sắc hơn người.
cao tầng|Có nhiều tầng xếp lên nhau, thường nói về nhà hoặc công trình.
cao thủ|Người có kỹ năng xuất sắc đứng đầu trong một nghề.
cao trào|Thời điểm phát triển mạnh nhất của sự việc hay phong trào.
cao vút|Rất cao, cao đến mức khó tưởng tượng.
cào bằng|Không phân biệt sự khác biệt giữa cao thấp hay tốt xấu.
cào cào|Loài côn trùng bay nhảy trên đồng ruộng.
cáo lỗi|Xin lỗi, xin tha thứ cho lỗi lầm đã làm.
cáo từ|Nói lời xin phép để rời khỏi nơi đang ở.
cau mày|Nhăn lông mày để tỏ vẻ khó chịu hoặc giận dữ.
càu nhàu|Nói nhỏ, than phiền vì không vừa ý.
cáu kỉnh|Tỏ vẻ bực bội bằng giọng điệu gắt gỏng.
cày bừa|Làm đất bằng cày và bừa để chuẩn bị gieo trồng.
cày cấy|Làm đất và gieo trồng, thường nói về công việc trên ruộng.
cày cuốc|Làm đất bằng cày và cuốc để gieo trồng cây lúa.
cắm đầu|Làm việc say sưa, chỉ chú tâm vào việc đó.
cắm trại|Dựng chỗ ở tạm ngoài trời để nghỉ hoặc sinh hoạt.
cặm cụi|Chăm chú làm việc liên tục, ít để ý tới xung quanh.
căn bản|Phần nền tảng quan trọng nhất quyết định bản chất.
căn bậc hai|Số nhân với chính nó ra được số đã cho.
căn cơ|Nền móng vững chắc hoặc biết tích lũy để xây dựng sự nghiệp.
căn cước|Những điểm để nhận rõ người như họ tên, ngày sinh, cha mẹ, đặc điểm nhân dạng.
căn dặn|Dặn dò kỹ lưỡng từng chi tiết nhỏ.
căn hộ|Chỗ ở riêng có các phòng trong một tòa nhà nhiều hộ.
căn nhà|Tòa nhà hoặc nơi ở riêng lẻ của một gia đình.
căn thức|Kết quả của phép tính tìm căn bậc hai hoặc căn bậc cao của một biểu thức.
căn tính|Tính chất vốn có của con người.
cằn cỗi|Đất khô cằn không màu mỡ hoặc cây cối già yếu không phát triển.
cằn nhằn|Nói nhỏ để than phiền hoặc trách móc người khác.
căng tin|Phòng bán đồ ăn uống phục vụ nhân viên trong cơ quan.
cẳng tay|Phần chi trên nằm giữa cổ tay và khuỷu tay.
cặp đôi|Gắn hai vật lại với nhau hoặc ghép hai người khác giới.
cắt đặt|Sắp xếp công việc và phân công người thực hiện.
cắt ngang|Cản trở ở giữa hoặc làm đứt đoạn.
cắt nghĩa|Giải thích rõ ràng để người khác hiểu được ý nghĩa.
cắt tóc|Hành động tỉa bớt tóc trên đầu người.
cầm ca|Đàn hát, thường dùng trong ngữ cảnh nghệ thuật dân gian.
cầm lòng|Nén giữ lại cảm xúc, không cho phép bộc lộ ra ngoài.
cầm trịch|Đứng ra điều khiển, chỉ đạo mọi người làm việc.
cẩm chướng|Loài hoa nhỏ có cánh nhiều màu sắc và mùi thơm dễ chịu.
cẩm nang|Cuốn sách nhỏ ghi tóm tắt kiến thức cần thiết để tham khảo.
cẩm tú|Cảnh sắc thiên nhiên rực rỡ hoặc văn chương đẹp như gấm thêu.
cân bằng|Trạng thái hai bên hỗ trợ nhau để giữ vững, không nghiêng lệch.
cân đối|Sự hợp lý, hài hòa giữa các phần khác nhau.
cân nhắc|Đặt các mặt lợi, hại lên bàn suy xét trước khi chọn.
cân xứng|Các bộ phận trong tổng thể có kích thước và hình dáng tương thích nhau.
cần câu|Thanh dài gắn dây và lưỡi để câu cá.
cần cù|Chịu bỏ công đều đặn, không dễ ngại việc.
cần lao|Cần mẫn, siêng năng và chịu khó làm việc vất vả.
cần mẫn|Làm việc rất chăm chỉ và nhanh nhẹn.
cần thiết|Cần phải có, thiếu đi sẽ không thể hoàn thành việc đó.
cẩn tắc|Chăm sóc kỹ lưỡng mọi việc để tránh sai sót.
cẩn thận|Chăm sóc kỹ lưỡng mọi việc để tránh sai sót hay rủi ro.
cẩn trọng|Cân nhắc kỹ để tránh sai sót khi làm việc.
cận cảnh|Cảnh quay hoặc chụp ảnh ở khoảng cách rất gần, thường thấy rõ chi tiết.
cận đại|Thời kỳ lịch sử nằm giữa trung đại và hiện đại.
cận kề|Ở ngay sát bên cạnh, không còn khoảng cách xa.
cấp bách|Cần làm ngay lập tức vì tình thế rất khẩn trương.
cấp báo|Thông báo ngay lập tức cho người khác biết.
cấp độ|Mỗi bậc trong một thang phân chia mức độ.
cấp phối|Hỗn hợp các hạt đất, cát, sỏi trộn theo tỷ lệ nhất định để rải đường.
cấp số|Dãy số mà mỗi số được tạo ra từ số trước theo quy tắc cộng hoặc nhân.
cấp tập|Xảy ra dồn dập, liên tục không có khoảng cách.
cấp thiết|Cần phải làm ngay lập tức, không thể chờ đợi.
cấp tiến|Có tư tưởng tiến bộ, không bảo thủ.
cấp tốc|Làm việc rất nhanh để kịp thời hạn.
cấp vốn|Cung cấp tiền bạc để hỗ trợ kinh doanh hoặc sản xuất.
cất cánh|Rời mặt đất để bắt đầu bay.
cất công|Dành nhiều công sức và tâm huyết để thực hiện một việc gì đó.
cất giấu|Đặt vào nơi kín đáo để người khác không nhìn thấy hay biết đến.
cất giữ|Đặt vào nơi an toàn để bảo quản cho nguyên vẹn.
cất nhắc|Nâng đỡ để đưa người khác lên địa vị cao hơn trong công việc hoặc xã hội.
cất tiếng|Bắt đầu phát âm, nói hoặc hát thành lời.
cất trữ|Giữ lại đồ vật để dùng sau này.
câu chuyện|Nội dung sự việc được kể lại bằng lời nói.
câu đố|Câu văn ngắn, gợi ý bí ẩn để người khác đoán.
câu đối|Hai câu văn ngắn có cấu trúc và ý nghĩa đối xứng nhau về âm thanh và nghĩa.
câu hỏi|Lời nói dùng để hỏi và mong người nghe đáp lại.
câu lạc bộ|Nơi tập hợp những người có cùng sở thích để vui chơi chung.
câu lệnh|Mệnh lệnh được viết bằng ngôn ngữ lập trình để máy tính thực hiện.
cầu chì|Dây kim loại dễ nóng chảy đặt trong mạch điện để tự ngắt khi dòng điện quá lớn.
cầu cống|Tổng hợp các công trình xây dựng để người đi lại và thoát nước.
cầu cứu|Yêu cầu người khác đến cứu trong lúc nguy hiểm.
cầu dao|Công tắc điện tự động đóng ngắt mạch khi quá tải.
cầu khỉ|Cầu nhỏ ở vùng sông rạch, thường dùng thân cây làm lối đi hẹp.
cầu khuẩn|Loại vi khuẩn có hình dạng tròn hoặc gần tròn.
cầu lông|Môn thể thao đưa quả cầu gắn lông qua lưới bằng vợt nhẹ.
cầu mong|Mong ước điều tốt đẹp sẽ xảy ra.
cầu nối|Cái kết nối, làm trung gian để các bên liên quan có thể giao tiếp, hợp tác.
cầu tài|Cầu mong được sở hữu nhiều tiền bạc, của cải.
cầu thang|Dãy bậc để đi lên xuống giữa các tầng hoặc các mức cao thấp.
cầu thị|Chủ động tìm hiểu để mở rộng kiến thức.
cầu thủ|Người tham gia tập luyện hoặc thi đấu chuyên nghiệp trong các môn thể thao dùng bóng.
cầu toàn|Yêu cầu mọi việc phải đạt mức tốt nhất, không chấp nhận thiếu sót.
cầu truyền hình|Hình thức phát sóng trực tiếp cuộc trò chuyện giữa nhiều nơi.
cầu vồng|Dải màu hình cung do ánh sáng gặp các giọt nước trong không khí.
cầu vượt|Cầu cho một tuyến đường đi qua phía trên một tuyến khác.
cẩu thả|Làm việc thiếu cẩn thận, chỉ muốn cho xong việc.
cấu hình|Tổng hợp các bộ phận máy tính nối nhau để làm việc theo mục đích.
cấu kiện|Bộ phận cấu thành nên một tổng thể lớn.
cấu tạo|Ghép nhiều phần riêng lẻ thành một tổng thể.
cấu thành|Tổng hợp các bộ phận và tỷ lệ giữa chúng.
cấu trúc|Mối liên hệ giữa các bộ phận tạo nên chỉnh thể.
cây cảnh|Cây trồng trong chậu hoặc vườn để làm đẹp cảnh quan.
cây cối|Tên gọi chung những cây mọc trong một khu vực.
cây leo|Cây có thân mềm dài, vươn lên bằng cách bám hoặc quấn vật khác.
cây nến|Vật bằng sáp có dây bấc ở giữa, đốt lên để lấy sáng.
cây nhà lá vườn|Sản phẩm tự làm tại nhà để biếu hoặc mời khách.
cây số|Cách gọi thông dụng của đơn vị đo độ dài bằng một nghìn mét.
cây trồng|Cây được con người chăm sóc để thu hoạch sản phẩm.
cây viết|Công cụ dùng để ghi chép bằng mực hoặc chất lỏng khác.
cây xanh|Thực vật được trồng nhằm mục đích bảo vệ môi trường sống.
cây xăng|Chỗ bán nhiên liệu cho xe cộ di chuyển.
cha đẻ|Người sáng lập ra một sự vật hay tổ chức đầu tiên.
chà bông|Thịt nạc xé nhỏ, tơi như bông dùng để ăn kèm.
chà là|Cây họ cau cho quả thuôn có vị ngọt khi chín.
chả cá|Món ăn làm từ cá cơm giã nhuyễn, rán vàng, ăn với cơm.
chả lụa|Thịt lợn giã nhuyễn, gói chặt trong lá rồi làm chín thành cây giò.
chả quế|Giò thịt có hương quế, thường có lớp ngoài vàng thơm.
chai|Đồ đựng chất lỏng có cổ hẹp và có thể đậy nắp.
chạm trán|Gặp nhau bất ngờ và buộc phải đối đầu.
chạm trổ|Làm việc chạm khắc để trang trí.
chan chứa|Đầy tràn, không còn chỗ chứa nữa.
chán nản|Thất vọng, mất hết ý chí và không còn muốn cố gắng làm việc gì nữa.
chán ngắt|Cảm thấy buồn chán vì sự việc quá nhàm chán, không có gì thú vị.
chang chang|Nói trời nắng rất gắt, ánh sáng chiếu mạnh xuống mặt đất.
chạng vạng|Lúc ánh sáng lờ mờ giữa ban ngày và ban đêm.
chanh|Quả có múi, vị chua, thường vắt lấy nước.
chánh văn phòng|Người đứng đầu bộ phận hành chính của một cơ quan nhà nước hoặc tổ chức lớn.
chào bán|Thông báo muốn bán hàng, kèm đủ thông tin cần thiết.
chào đón|Đón tiếp người đến với niềm vui và sự nhiệt tình.
chào đời|Khởi đầu cuộc đời, ra đời vào thế gian.
chào giá|Nói rõ mức tiền muốn mua hoặc bán kèm điều kiện.
chào hàng|Giới thiệu hàng hóa để mời khách mua.
chào hỏi|Chúc mừng và hỏi thăm khi gặp nhau.
chào mào|Chim nhỏ có mào nhọn, thường thấy mảng đỏ dưới đuôi và sau má.
chào mời|Ân cần mời mọc người khác đến hoặc mua hàng.
chảo|Đồ nấu có lòng rộng để rán hoặc xào.
cháo đậu|Cháo nấu riêng từ đậu và củ sắn.
cháo hoa|Cháo nấu chưa chín kỹ, hạt gạo vẫn nguyên vẹn và nở to như bông.
chạo tôm|Món ăn làm từ tôm tươi giã nhuyễn, bọc quanh mía và nướng chín vàng.
cháu chắt|Những người thuộc thế hệ sau đời con, bao gồm cháu và chắt.
chạy|Di chuyển nhanh bằng những bước chân liên tiếp.
chạy đua|Cố gắng hết sức để tranh giành vị trí cao hơn hoặc thắng lợi.
chắc|Vững và khó bung ra hay đổ ngã.
chắc ăn|Có thể tin chắc là sẽ xảy ra đúng như dự định.
chắc chắn|Có cơ sở vững để tin rằng điều gì đó sẽ xảy ra.
chắc nịch|Vững chắc, kiên cố, không dễ gì lung lay hay đổ vỡ.
chăm chỉ|Sẵn lòng làm việc đều đặn và chuyên tâm.
chăm chú|Dồn sự chú ý vào một việc, ít bị điều khác làm xao nhãng.
chăm chút|Chăm sóc, lo lắng tỉ mỉ, chu đáo cho người hoặc việc.
chăm nom|Để mắt tới và làm những việc cần để người hay vật được ổn thỏa.
chăm sóc|Trông nom và đáp ứng nhu cầu để người, vật hoặc cây phát triển tốt.
chằm chằm|Nhìn chăm chú không rời mắt.
chăn chiếu|Đồ dùng để nằm ngủ và giữ ấm cơ thể vào ban đêm.
chăn nuôi|Nuôi và chăm sóc vật nuôi để lấy sản phẩm hoặc sức kéo.
chăn thả|Cho vật nuôi tự đi ăn cỏ trong khu vực quy định.
chắn bùn|Bộ phận trên bánh xe giúp bùn nước không văng lên người hay xe.
chằng chịt|Nhiều đường hoặc sợi đan xen, chồng chéo khó tách biệt.
chẳng hạn|Mở đầu một ví dụ cụ thể cho nhận xét vừa nêu.
chẳng may|Rủi thay. / Không dè.
chẳng trách|Không có gì lạ, vì đã có nguyên nhân dẫn đến điều đó.
chặng|Một đoạn trong cả hành trình.
chắp|Ghép những phần rời thành một vật liền.
chắt chiu|Dành dụm tiền của, công sức để không bị hao phí.
chặt chẽ|Gắn kết khăng khít, không có khoảng cách hay kẽ hở.
châm biếm|Chế giễu bằng lời nói hài hước nhằm phê phán.
châm ngôn|Câu nói ngắn gọn, lưu truyền để hướng dẫn về đạo đức và lối sống.
chấm dứt|Làm cho việc đang tiếp diễn dừng hẳn lại.
chấm hết|Kết thúc hoàn toàn, chấm dứt mọi sự tiếp diễn.
chấm phá|Vẽ vài nét đơn giản để làm nổi bật vẻ đẹp của cảnh vật.
chấm thi|Đọc bài thi để cho điểm cho thí sinh.
chậm|Làm việc hoặc di chuyển với tốc độ thấp.
chậm chạp|Di chuyển hoặc thực hiện việc gì với tốc độ rất chậm, dưới mức bình thường.
chậm trễ|Làm việc muộn hơn thời hạn quy định.
chân|Bộ phận cơ thể chống đỡ người khi đứng hoặc đi.
chân chống|Bộ phận bật xuống để xe hai bánh đứng vững khi dựng.
chân dung|Bức tranh vẽ hoặc ảnh chụp thể hiện rõ khuôn mặt người.
chân đất|Đi chân trần không mang giày dép.
chân gà|Phần ở cuối chân con gà, có các ngón và móng.
chân không|Khoảng không gian không chứa bất kỳ vật chất nào.
chân núi|Phần thấp nhất của ngọn núi, nơi đất liền bắt đầu dốc lên cao.
chân phương|Viết chữ thẳng hàng, rõ ràng, đúng quy tắc và không cầu kỳ.
chân thành|Xuất phát từ ý nghĩ thật, không giả vờ lấy lòng.
chân thật|Trung thực, nói và làm đúng với suy nghĩ, tình cảm thật.
chân tình|Tấm lòng thành thật, không giả dối hay che giấu.
chân trời|Đường giới hạn nơi bầu trời gặp mặt đất hoặc biển.
chân tu|Sống đúng đạo lý, giữ gìn phẩm chất trong sạch.
chần chừ|Do dự, cân nhắc kỹ lưỡng chưa quyết định làm ngay.
chấn chỉnh|Sửa lại cho đúng, gọn gàng, ngăn nắp.
chấn hưng|Làm cho sự việc trở nên hưng thịnh, phát triển mạnh mẽ hơn trước.
chấn lưu|Thiết bị điện dùng để hạn chế dòng điện chạy qua.
chấp bút|Viết thay cho người khác dựa trên ý tưởng hay sườn bài của họ.
chấp hành|Thực hiện đúng các quy định hoặc chỉ đạo của tổ chức.
chấp nhận|Đồng ý nhận lời hoặc làm theo điều người khác đề nghị.
chấp thuận|Bằng lòng nhận một yêu cầu hay đề nghị.
chập choạng|Thời điểm trời tối mờ, ranh giới giữa sáng và tối không rõ ràng.
chập chờn|Lúc hiện lúc mất hoặc không giữ trạng thái ổn định.
chập chững|Nói trẻ nhỏ mới tập đi, bước đi chưa vững vàng.
chập tối|Khoảng thời gian trời vừa bắt đầu tối, ánh sáng còn mờ ảo.
chất béo|Chất dinh dưỡng giúp cơ thể dự trữ năng lượng.
chất dẻo|Chất mềm dẻo, dễ uốn nắn thành hình khi đun nóng rồi cứng lại khi nguội.
chất đống|Nén nhiều vật chất lại thành một khối lớn.
chất đốt|Chất liệu khi cháy sinh ra nhiều nhiệt dùng để đun nấu hoặc chạy máy.
chất khí|Dạng vật chất có thể lan ra chiếm toàn bộ chỗ trống của bình chứa.
chất liệu|Vật liệu, tư liệu dùng để tạo nên sản phẩm.
chất lỏng|Chất chảy tự do, không giữ được hình dạng cố định.
chất lượng|Độ tốt xấu, giá trị thực của sự vật hay việc làm.
chất rắn|Trạng thái vật chất có dạng và thể tích tương đối ổn định.
chật|Không đủ rộng cho người hay đồ vật bên trong.
chật chội|Không còn chỗ trống, không gian hẹp khiến người và vật khó di chuyển.
chật hẹp|Không gian quá nhỏ khiến việc di chuyển hoặc hoạt động trở nên khó khăn.
chật ních|Chật chội đến mức không thể chen thêm người hay vật nào nữa.
châu báu|Vàng bạc, đá quý dùng làm của quý.
châu chấu|Côn trùng ăn lá, có hai chân sau dài để bật nhảy.
châu lục|Vùng đất lớn trên Trái Đất.
châu thổ|Đồng bằng phù sa hình thành nơi sông đổ ra biển hay hồ.
chầu chực|Đứng bên cạnh để phục vụ hoặc chờ đợi lâu để mong gặp gỡ.
chậu|Đồ đựng miệng rộng để rửa đồ hoặc trồng cây.
che chắn|Dựng vật hoặc dùng tay để ngăn chặn tác động từ bên ngoài.
che chở|Bảo vệ người khác khỏi nguy hiểm hoặc khó khăn.
che kín|Dùng vật che phủ để không thấy rõ hình dáng bên trong.
che phủ|Làm cho vật gì che khuất không nhìn thấy được.
chè xanh|Lá cây chè non hoặc già, dùng để chế biến nước uống giải khát.
chen chân|Chèn vào giữa người khác để đứng hoặc lấy chỗ.
chen chúc|Đứng sát nhau vì quá đông người.
chén|Đồ nhỏ có lòng sâu, thường để uống trà.
chèo|Gạt nước bằng mái dẹt để đưa thuyền đi.
chèo kéo|Cố níu kéo, mời mọc người khác bằng mọi cách.
chép|Ghi lại theo chữ hoặc nội dung có sẵn.
chê trách|Nói xấu, chỉ trích lỗi lầm của người khác.
chế bản|Bản thiết kế sách hoặc báo được sắp xếp sẵn để in ấn.
chế biến|Làm thay đổi chất liệu hoặc hình dáng để tạo ra sản phẩm cần dùng.
chế tạo|Làm ra máy móc hay đồ vật từ vật liệu và các bộ phận.
chế tạo máy|Sản xuất ra các loại máy móc thiết bị công nghiệp.
chế xuất|Làm hàng hóa để bán ra nước ngoài, phục vụ cho việc xuất khẩu.
chệch|Lệch khỏi hướng hoặc vị trí dự định.
chêm|Nhét thêm vật nhỏ vào khe để giữ cho chắc.
chênh lệch|Không bằng nhau, có sự khác biệt về số lượng hoặc chất lượng.
chênh vênh|Ở chỗ cao, bấp bênh và ít có điểm tựa vững.
chểnh mảng|Làm việc không hết sức, bỏ qua trách nhiệm.
chi chít|Nhiều vật hay dấu nhỏ nằm sát nhau trên một khoảng hẹp.
chi dùng|Dùng tiền bạc để mua sắm hoặc chi trả cho việc gì.
chi hội|Nhánh hoặc bộ phận cơ sở của một tổ chức hội.
chi nhánh|Phần phụ tách ra từ hệ thống chính để phục vụ khu vực nhỏ hơn.
chi phí|Số tiền phải bỏ ra để làm một việc hoặc mua đồ.
chi phiếu|Giấy ngân hàng dùng để thay thế tiền mặt khi thanh toán.
chi phối|Có sức mạnh làm cho cái kia phải nghe theo.
chi trả|Bỏ tiền ra để thanh toán cho một khoản chi phí.
chỉ bảo|Hướng dẫn cụ thể cách làm hoặc cách xử lý việc.
chỉ dẫn|Hành động giúp người khác hiểu rõ điều cần biết.
chỉ định|Quyết định giao việc hoặc chỉ rõ ai làm gì.
chỉ huy|Người đứng đầu hoặc điều khiển một tập thể.
chỉ rõ|Nói rõ ràng để người khác hiểu đúng ý nghĩa.
chỉ số|Con số dùng đo lường sự thay đổi của hiện tượng qua các thời kỳ.
chỉ tay|Chỉ trỏ hoặc ra lệnh để sai khiến người khác thực hiện việc gì.
chỉ tiêu|Mục tiêu định trước để đo lường kết quả công việc.
chỉ trỏ|Chỉ bằng tay để nói chuyện chung chung.
chí công|Không thiên vị, xử sự công bằng tuyệt đối.
chí công vô tư|Làm việc công bằng, không thiên vị hay vì lợi ích riêng.
chí cốt|Gắn bó máu thịt, xem như người thân.
chí hướng|Ý chí kiên định hướng tới mục tiêu cao đẹp trong đời.
chí khí|Đức tính mạnh mẽ, dám làm việc lớn.
chí tình|Chân thành hết lòng và cảm động sâu sắc.
chí tuyến|Vĩ tuyến cách xích đạo hai mươi ba độ hai mươi bảy phút.
chị em|Người chị và người em trong cùng gia đình.
chị gái|Người con gái cùng cha mẹ nhưng lớn tuổi hơn mình.
chia|Tách một thứ thành nhiều phần nhỏ hơn.
chia cắt|Phân chia thành nhiều phần rời rạc, làm mất đi sự nguyên vẹn.
chia chác|Phân chia phần của nhiều người cùng hưởng.
chia đều|Phân chia số lượng hoặc chất lượng cho mọi người bằng nhau.
chia hết|Việc chia số này cho số kia mà không còn số dư.
chia sẻ|Cho người khác dùng chung những gì mình đang có.
chia tay|Dứt bỏ tình cảm, coi như không còn mối quan hệ với nhau.
chiếc|Từ đếm riêng từng đồ vật như ô tô hay áo.
chiêm ngưỡng|Ngắm nhìn với lòng kính trọng và yêu quý.
chiền chiện|Chim nhỏ thường vừa bay cao vừa cất tiếng hót.
chiêng|Nhạc cụ kim loại hình đĩa, gõ lên phát tiếng ngân.
chiết khấu|Khoản giảm tính theo tỷ lệ trên mức giá hoặc số tiền ban đầu.
chiết xuất|Lấy ra phần cần thiết từ hỗn hợp bằng phương pháp đặc biệt.
chiêu hiền|Tìm kiếm và mời gọi những người có tài năng để làm việc.
chiêu sinh|Mời gọi người đến để ghi danh vào các lớp học.
chiêu thức|Cách thức hoặc thủ đoạn để thực hiện công việc.
chiều cao|Kết quả đo từ dưới lên trên hoặc từ chân đến đầu người.
chiều chuộng|Nuông chiều, chiều theo ý muốn vì yêu thương hoặc coi trọng.
chiều dài|Kích thước đo dọc theo hướng dài của một vật.
chiều hướng|Hướng đi hoặc xu hướng phát triển của sự việc, hiện tượng.
chiều kích|Những phần khác nhau cấu thành nên ý nghĩa của một sự việc hay vấn đề.
chiều lòng|Làm đúng ý người khác chỉ để được khen, dù trong lòng không muốn.
chiều rộng|Khoảng từ mép bên này đến mép bên kia theo hướng ngang.
chiếu|Tấm dệt trải trên sàn hay giường để ngồi, nằm.
chiếu bóng|Nghệ thuật quay và chiếu hình ảnh trên màn bạc.
chiếu cố|Quan tâm đặc biệt hoặc chú ý riêng đến người nào đó.
chiếu lệ|Làm việc qua loa, chỉ cốt cho có mà không cần kỹ lưỡng.
chiếu sáng|Phát ra ánh sáng để làm cho chỗ tối trở nên sáng rõ.
chiếu xạ|Việc dùng tia bức xạ chiếu vào vật thể hoặc sinh vật.
chim cánh cụt|Loài chim biển đen trắng, không biết bay, bơi bằng cánh và đi bằng chân.
chim cắt|Chim săn mồi có cánh nhọn, bay nhanh và có mỏ cong.
chim muông|Chim và thú rừng sống ngoài tự nhiên.
chim sâu|Tên gọi những chim nhỏ thường tìm sâu bọ trên cành lá.
chim sẻ|Chim nhỏ, thường có bộ lông nâu xám và hay sống gần nhà.
chim xanh|Người truyền tin hoặc người làm mối cho hai bên.
chìm|Hạ xuống dưới mặt nước hoặc bề mặt chất lỏng.
chìm đắm|Bị bao trùm hoàn toàn bởi một thứ gì đó mạnh mẽ.
chìm nghỉm|Lặn sâu xuống nước đến mức không còn nhìn thấy dù chỉ một phần nhỏ.
chín|Đã qua giai đoạn xanh và có thể thu hái, ăn được.
chín chắn|Biết suy nghĩ kỹ, không hành động bộp chộp.
chín muồi|Đã phát triển đến lúc thích hợp để cho kết quả.
chín vàng|Trái cây hoặc vật thể đã chín và chuyển sang màu vàng.
chỉnh|Đổi một chút để vật ở đúng vị trí hoặc đúng mức.
chỉnh sửa|Điều chỉnh hoặc thay đổi để đạt được sự chính xác và phù hợp.
chỉnh tề|Quần áo, đồ dùng hoặc hàng ngũ đều ngay ngắn và gọn.
chỉnh thể|Tập hợp các bộ phận liên kết chặt chẽ thành một khối thống nhất.
chỉnh trang|Sửa sang, sắp xếp lại cho gọn gàng, đẹp mắt.
chính chủ|Người sở hữu, chủ nhân của vật.
chính cống|Đúng thật, không giả mạo, xuất phát từ nguồn gốc chính.
chính diện|Mặt trước, mặt hướng ra ngoài.
chính đáng|Việc làm hoặc hành động đúng theo lẽ phải, hợp tình và hợp lý.
chính hiệu|Đúng thật với tên gọi, xuất xứ và chất lượng ban đầu.
chính lưu|Những quan điểm, cách nghĩ hoặc xu hướng được đa số xã hội công nhận là chuẩn mực.
chính ngạch|Hình thức giao thương hợp pháp theo hiệp định quốc gia hoặc tổ chức.
chính tả|Quy tắc viết chữ và đặt dấu đúng trong một ngôn ngữ.
chính thống|Thuộc về hệ thống, quy tắc hoặc quan điểm được công nhận là chính thức và chuẩn mực.
chính thức|Việc được chính quyền hoặc cơ quan có thẩm quyền công nhận.
chính văn|Nội dung chính của tác phẩm không bao gồm phần chú thích hay phụ lục.
chính xác|Đúng hoàn toàn, không sai sót hay lệch lạc.
chính yếu|Quan trọng nhất, cốt lõi, khác với những thứ kém trọng yếu.
chịu|Chấp nhận gánh một việc hay một tác động.
chịu đi|Đồng ý, thuận theo việc đi.
chịu đựng|Bền lòng chịu các tác động khó khăn mà không bỏ cuộc.
chịu khó|Làm việc cần cù, chịu đựng mọi khó khăn vất vả mà không nản lòng.
chịu thua|Đành nhận thua và không còn chống cự.
cho biết|Nói ra một số lượng hoặc nội dung đã xác định.
cho hay|Thông báo kết quả hoặc tin tức cho người khác.
cho là|Đưa ra ý kiến hoặc quan điểm về một vấn đề nào đó.
cho mượn|Giao vật để người khác dùng tạm rồi trả lại.
cho phép|Cho người khác được làm việc gì hoặc không cấm cản.
cho thuê|Cho người khác mượn đồ trong thời gian nhất định rồi trả tiền.
chó sói|Thú hoang họ chó, thường có mõm dài và sống theo đàn.
choán|Chiếm nhiều chỗ khiến phần còn lại bị thu hẹp.
choàng|Phủ khăn hoặc áo quanh vai hay cổ.
choáng ngợp|Cảm thấy bị bao vây, choáng váng vì quá nhiều sự vật hoặc cảm xúc.
chói mắt|Ánh sáng quá mạnh chiếu vào mắt khiến không nhìn rõ.
chói tai|Âm thanh quá cao, sắc nhọn khiến tai bị đau và khó chịu.
chòm sao|Nhóm các ngôi sao tạo thành hình ảnh trên bầu trời.
chòm xóm|Khu vực dân cư nhỏ gồm nhiều nhà ở gần nhau, thường thấy ở vùng nông thôn.
chỏm|Phần nhỏ nhô lên ở trên cùng.
chọn lọc|Lựa giữ những phần tốt nhất và loại bỏ phần xấu.
chong chóng|Đồ chơi có cánh quay quanh trục khi gặp gió.
chóng vánh|Nhanh chóng, tốn ít thời gian hơn dự kiến.
chót vót|Vật thể cao vút lên tận trời, vượt quá tầm nhìn thường.
chỗ nghỉ|Chỗ để ngồi nhằm mục đích nghỉ ngơi.
chỗ ngồi|Nơi dùng để ngồi nghỉ hoặc làm việc.
chỗ ở|Nơi con người sinh sống và cư trú hàng ngày.
chỗ trống|Nơi không có vật gì chiếm chỗ.
chốc lát|Khoảng thời gian rất ngắn, chỉ trong tích tắc.
chốc nữa|Khoảng thời gian ngắn sắp đến.
chổi|Dụng cụ có cán và túm sợi để quét bụi.
chối từ|Từ chối một lời mời, yêu cầu hoặc đề nghị bằng cách nói không.
chôm chôm|Quả nhiệt đới có vỏ nhiều gai mềm, phần ăn được thường trắng.
chôn chân|Giữ nguyên vị trí, không thể di chuyển đi đâu.
chông gai|Những trở ngại, nguy hiểm trên đường đi.
chồng|Xếp nhiều vật lên nhau thành tầng.
chồng chất|Chồng lên nhau thành nhiều lớp.
chồng chéo|Nằm đè lên nhau, xen kẽ lộn xộn.
chốt|Thanh nhỏ để cài cửa hoặc giữ các phần khỏi rời nhau.
chột dạ|Lo sợ giật mình vì nghĩ việc mình giấu sẽ bị phát hiện.
chơ vơ|Lẻ loi, cô đơn giữa khoảng không gian rộng mênh mông.
chờ đợi|Mong ngóng sự việc, người hoặc hành động sẽ xảy ra hoặc cùng làm.
chợ búa|Nơi người dân tụ họp để mua bán thực phẩm và đồ dùng sinh hoạt.
chợ cóc|Chợ họp tự phát, nhỏ bé, tạm thời và không có địa điểm cố định.
chợ nổi|Chợ họp trên sông, người mua bán ngồi trên thuyền.
chợ trời|Chợ họp ngoài trời, hàng hóa tự do.
chơi bời|Chơi đùa, vui chơi với nhau một cách thoải mái, không mục đích cụ thể.
chơi chữ|Sử dụng đặc điểm đồng âm hay đa nghĩa của từ ngữ để tạo hiệu ứng hài hước hoặc sâu sắc.
chơi hụi|Cách góp tiền xoay vòng giữa nhóm người để cùng nhau tiêu dùng.
chơi trội|Làm những việc vượt trội để thể hiện mình hơn người khác.
chớm nở|Hoa mới bắt đầu nở; việc mới có triển vọng.
chớp|Luồng sáng lóe trên trời khi có dông.
chớp mắt|Động tác nhanh chóng khép mở mí mắt một lần trong tích tắc.
chớp nhoáng|Xúc động nhanh như tia chớp, chỉ trong khoảnh khắc rất ngắn.
chu cấp|Cung cấp tiền bạc hoặc vật chất cần thiết để duy trì cuộc sống.
chu du|Du lịch nhiều nơi xa.
chu đáo|Cẩn thận kỹ lưỡng, không bỏ sót chi tiết gì.
chu tất|Đầy đủ, trọn vẹn, xong xuôi.
chu trình|Quá trình lặp lại khiến kết thúc quay về trạng thái đầu.
chu vi|Kết quả đo trọn một vòng dọc theo biên của hình.
chủ biên|Người đứng đầu chịu trách nhiệm chính về nội dung.
chủ chốt|Người hoặc việc quan trọng nhất, đóng vai trò then chốt.
chủ đề|Nội dung chính hoặc chủ yếu được bàn luận trong tác phẩm.
chủ đích|Điều người làm nhắm tới ngay từ đầu.
chủ động|Tự mình làm việc để tạo ra kết quả mong muốn.
chủ lực|Lực lượng quan trọng nhất, đóng vai trò then chốt trong tổng thể.
chủ ngữ|Thành phần đứng đầu câu dùng để chỉ người hoặc việc chính mà câu nói đến.
chủ nhà|Người sở hữu và quản lý ngôi nhà.
chủ nhân|Người có quyền sở hữu vật đang được nhắc đến.
chủ quan|Dựa vào cách nhìn của bản thân hơn là sự kiểm tra khách quan.
chủ sự|Người đứng đầu một phòng ban trong cơ quan hành chính thời thuộc địa.
chủ thầu|Người đứng ra nhận thầu toàn bộ hoặc phần lớn một công trình xây dựng hay dịch vụ.
chủ thể|Phần quan trọng nhất, đóng vai trò chính trong sự việc.
chủ trì|Đứng ra điều hành và chịu trách nhiệm chính trong một hoạt động.
chủ trương|Những quyết định định hướng cho hoạt động của tổ chức hoặc cá nhân.
chủ xị|Người mời hoặc chi trả tiền cho mọi người trong tiệc.
chủ yếu|Quan trọng nhất, chiếm phần lớn hoặc là cốt lõi.
chú giải|Lời bổ sung giúp người đọc hiểu một chữ, ký hiệu hay đoạn khó.
chú rể|Người nam tham gia lễ cưới để lấy vợ.
chú thích|Phần ghi chú thêm để giải thích hoặc làm rõ ý nghĩa của nội dung.
chú trọng|Đặt hết sự quan tâm vào việc nào đó.
chú ý|Dùng toàn tâm trí vào việc gì hoặc nên cẩn thận.
chua|Có vị giống nước cốt chanh hay giấm.
chua cay|Cảm giác đau buồn, cay đắng và xót xa.
chuẩn|Mức được chọn làm căn cứ để đối chiếu.
chuẩn bị|Làm sẵn những việc cần thiết trước khi thực hiện công việc nào đó.
chuẩn xác|Đúng y hệt những gì đã tính toán hoặc quy định.
chúc thọ|Chúc người lớn tuổi sống lâu thêm.
chục|Nhóm gồm mười đơn vị.
chui|Luồn cả người qua một chỗ hẹp.
chung|Thuộc về hoặc được dùng bởi nhiều người.
chung cuộc|Kết quả cuối cùng của mọi sự việc.
chung cư|Tòa nhà có nhiều căn hộ riêng và các phần dùng chung.
chung kết|Vòng cuối quyết định người hay đội đứng đầu cuộc thi.
chung thân|Trọn cả cuộc đời, không có ngày kết thúc.
chung tình|Trung thành với người yêu đến cùng.
chủng loại|Nhóm các vật có đặc điểm giống nhau, cùng một giống.
chúng ta|Nhóm người bao gồm cả người đang nói chuyện và người được nói đến.
chúng tôi|Nhóm người đang nói chuyện với người nghe.
chuỗi|Dãy gồm nhiều phần tử nối tiếp nhau.
chuỗi cung ứng|Hệ thống các khâu liên kết vận chuyển hàng từ nơi sản xuất đến tay người dùng.
chuỗi thức ăn|Dãy sinh vật nối nhau theo quan hệ loài này làm thức ăn cho loài sau.
chuồn chuồn|Côn trùng thân dài, mắt lớn và có hai đôi cánh mỏng.
chuông|Vật rỗng thường bằng kim loại, gõ vào sẽ ngân vang.
chuông gió|Vật trang trí phát tiếng leng keng khi gió làm các ống rung va chạm.
chuồng trại|Chỗ nhốt các loài vật nuôi.
chuột|Thú gặm nhấm nhỏ có răng cửa dài liên tục.
chuột cống|Chuột lớn thường sống trong các cống rãnh thoát nước.
chuột đồng|Chuột thường sinh sống và kiếm thức ăn ở đồng ruộng.
chuột lang|Loài gặm nhấm có nguồn gốc Nam Mỹ, thường được nuôi làm thú cưng hoặc lấy thịt.
chuột túi|Thú nhảy bằng chân sau khỏe, con cái có túi bụng nuôi con.
chụp|Bấm máy để lưu hình một người, vật hoặc phong cảnh.
chụp ảnh|Dùng máy ghi hình một cảnh thành ảnh tĩnh.
chút|Một phần hay một lượng rất nhỏ.
chút đỉnh|Một lượng nhỏ, không đáng kể.
chút nữa|Chỉ hành động sẽ xảy ra trong thời gian rất ngắn sắp tới.
chuyên biệt|Được thiết kế hoặc dành riêng cho một mục đích xác định.
chuyên canh|Trồng duy nhất một loại cây trên cùng một diện tích đất.
chuyên cần|Thường xuyên chịu khó học hoặc làm việc.
chuyên chở|Đưa hành khách hoặc hàng hóa tới nơi khác bằng phương tiện.
chuyên cơ|Máy bay chuyên chở nhân vật quan trọng hoặc đi công vụ đặc biệt.
chuyên đề|Nội dung tập trung nghiên cứu hoặc trình bày riêng một chủ điểm.
chuyên gia|Người am hiểu sâu sắc và giỏi nghề trong một lĩnh vực chuyên môn.
chuyên luận|Bài viết nghiên cứu chuyên sâu về một vấn đề cụ thể.
chuyên mục|Phần nội dung thường xuyên xuất hiện trên báo chí hoặc truyền thông về một chủ đề riêng.
chuyên ngành|Thuật ngữ dùng để chỉ một mảng kiến thức hoặc công việc cụ thể trong một lĩnh vực rộng lớn.
chuyên nghiệp|Làm một nghề cụ thể với kỹ năng cao và kinh nghiệm sâu.
chuyên sâu|Nghiên cứu kỹ lưỡng một vấn đề chuyên môn.
chuyên tâm|Dồn sự chú ý và công sức vào một việc.
chuyên trách|Được giao phụ trách tập trung một loại việc cụ thể.
chuyên trang|Trang báo chỉ tập trung viết về một chủ đề cụ thể.
chuyên viên|Người có kiến thức sâu rộng và thành thạo về một nghề.
chuyền|Đưa vật sang tay kế bên cho nó lần lượt đi tiếp.
chuyển biến|Thay đổi từ trạng thái cũ sang trạng thái mới khác.
chuyển dịch|Di chuyển từng đoạn ngắn hoặc thay đổi dần cơ cấu.
chuyển đổi|Đổi từ dạng này sang dạng khác.
chuyển động|Qua một khoảng thời gian, vật không còn ở cùng vị trí so với mốc.
chuyển động thẳng|Chuyển động có đường đi là một đường thẳng không cong queo.
chuyển giao|Việc trao quyền sở hữu hoặc nhiệm vụ cho người khác.
chuyển hướng|Đổi sang phương hướng khác.
chuyển khoản|Thanh toán bằng cách ghi giảm tiền bên gửi và ghi tăng tiền bên nhận.
chuyển mình|Di chuyển toàn bộ cơ thể để bắt đầu thay đổi hoặc phát triển.
chuyển phát|Gửi và vận chuyển thư từ, bưu phẩm đến nơi người nhận.
chuyển tải|Vận chuyển một vật gì đó đến nơi khác.
chuyển thể|Chuyển nội dung một tác phẩm sang hình thức mới, như từ truyện sang phim.
chuyển tiếp|Kết nối phần trước với phần sau để tạo sự liên tục trong nội dung.
chuyển tự|Việc viết lại âm thanh của từ ngữ nước ngoài bằng chữ cái của tiếng Việt.
chuyển vận|Di chuyển hoặc vận chuyển người, hàng hóa từ nơi này đến nơi khác.
chuyến bay|Quá trình máy bay rời sân bay này để đến sân bay khác.
chuyện trò|Nói chuyện thân thiết, vui vẻ với người khác.
chư hầu|Các nước nhỏ phải tuân lệnh và cống nạp cho một nước lớn.
chữ cái|Ký hiệu dùng để ghi lại âm thanh và biến thể trong chữ viết.
chữ nổi|Chữ viết có các điểm nổi để người khiếm thị dùng tay sờ đọc.
chữ số|Ký hiệu đơn giản dùng để biểu thị con số trong toán học.
chữ viết|Dấu hiệu dùng để ghi lại lời nói thành văn bản.
chưa kể|Chỉ những điều chưa được nhắc đến hay bàn luận.
chứa đựng|Giữ các vật bên trong lòng mình.
chức danh|Tên gọi chính thức của một vị trí hay công việc trong tổ chức.
chức năng|Khả năng hoặc vai trò cụ thể mà một vật, sự việc hay người có thể thực hiện được.
chức vụ|Nhiệm vụ và địa vị công việc mà người ta đảm nhận trong tổ chức.
chưng cất|Phương pháp tách các chất lỏng khác nhau dựa vào khả năng bay hơi.
chừng mực|Độ vừa đủ, không quá nhiều cũng không quá ít trong mọi việc.
chững chạc|Đứng vững vàng, có dáng vẻ nghiêm trang và uy nghi.
chứng chỉ|Giấy tờ xác nhận năng lực hoặc thành tích do cơ quan cấp.
chứng khoán|Giấy chứng nhận quyền sở hữu tài sản có thể mua bán trên thị trường.
chứng kiến|Có mặt và trực tiếp nhìn thấy việc xảy ra.
chứng minh|Đưa ra căn cứ và lập luận để làm rõ một điều là đúng.
chứng nhận|Giấy tờ hoặc lời nói xác minh sự thật của một việc.
chứng tích|Những dấu vết còn sót lại dùng làm bằng chứng cho sự việc đã xảy ra.
chứng tỏ|Làm rõ sự thật bằng bằng chứng.
chứng từ|Giấy tờ xác nhận các khoản thu chi hoặc xuất nhập.
chương trình|Danh sách các công việc cần làm theo thứ tự và thời gian.
chướng ngại|Vật hoặc tình thế làm cho việc đi tiếp gặp khó.
co ngót|Hiện tượng bê tông co lại do mất đi độ ẩm.
co quắp|Co lại với sức mạnh lớn hơn mức bình thường.
co rút|Thu nhỏ kích thước hoặc phạm vi lại.
có ăn|Đủ cơm ăn, không thiếu thốn vật chất.
có chửa|Trạng thái phụ nữ mang thai trong bụng.
có hiếu|Làm tròn bổn phận chăm sóc cha mẹ.
có ích|Có tác dụng tốt, mang lại lợi ích.
có lợi|Mang lại lợi ích, giúp ích cho người khác.
có mặt|Xuất hiện và hiện diện tại một địa điểm cụ thể.
có một|Tồn tại một mình, không có người hay vật nào khác cùng bên cạnh.
có một không hai|Chỉ duy nhất một cái, không có gì giống hoặc sánh được.
có tài|Có năng lực xuất chúng trong việc gì.
có vẻ|Trông như vậy, hiện ra ở bề ngoài.
có vị|Có mùi vị đặc trưng của món ăn hoặc đồ uống.
cọc cạch|Không ăn khớp, không hợp nhau về hình dáng hay tính chất.
cọc chèo|Thanh gỗ hay kim loại gắn ở mạn thuyền để giữ chèo.
coi chừng|Chú ý đề phòng kẻo gặp chuyện xấu.
coi như|Tưởng là đã xảy ra hoặc quyết định xem là như vậy.
coi trọng|Xem là có giá trị và chú ý đúng mức đến.
com lê|Bộ quần áo nam gồm áo, vest và quần.
con cháu|Những người thuộc thế hệ sau trong gia đình hoặc dòng họ.
con dấu|Vật cứng có khắc chữ hoặc hình, dùng đóng lên giấy tờ để xác nhận danh nghĩa.
con đường|Lối trên mặt đất để người hoặc phương tiện đi lại.
con em|Những người con cháu trong nhà còn nhỏ tuổi.
con gái|Người con thuộc giới nữ trong quan hệ với cha mẹ.
con giáp|Chu kỳ mười hai con vật dùng để tính năm theo lịch âm.
con một|Người không có anh chị em cùng cha mẹ trong gia đình.
con ngươi|Phần tròn nhỏ nhất ở giữa tròng đen mắt.
con nuôi|Người được nhận vào nhà để nuôi dưỡng thay vì sinh ra từ chính cha mẹ.
con nước|Một đợt nước dâng lên hoặc rút xuống theo nhịp thủy triều.
con rối|Hình người hoặc vật được điều khiển cho cử động khi biểu diễn.
con số|Ký hiệu dùng để chỉ lượng hoặc giá trị cụ thể.
con tiện|Thanh trụ đứng dùng làm lan can, cửa sổ hoặc cầu thang.
con trai|Người con thuộc giới nam trong quan hệ với cha mẹ.
con trỏ|Kí hiệu di chuyển trên màn hình máy tính theo chuột.
còn lại|Phần còn sót lại sau khi đã lấy đi hoặc sử dụng.
còn nữa|Chưa kết thúc, vẫn còn tiếp tục.
còn nước còn tát|Còn chút hy vọng dù nhỏ thì vẫn cố gắng hết sức để cứu vãn.
cỏn con|Bé nhỏ, tầm thường, không đáng kể.
cót két|Âm thanh khô khan, giòn tan phát ra liên tục.
cô dâu|Người phụ nữ được kết hôn và trở thành vợ trong ngày lễ trọng đại.
cô đặc|Làm bớt dung môi để phần còn lại đậm đặc hơn.
cô gái|Người phụ nữ trẻ, chưa lập gia đình.
cô giáo|Người phụ nữ làm công việc dạy học.
cô nhi viện|Nơi chăm sóc và nuôi dưỡng trẻ em không cha mẹ.
cô quạnh|Một mình, không có người thân bên cạnh.
cổ chân|Khớp nối giữa phần chân và phần cẳng chân, giúp gập duỗi bàn chân.
cổ đại|Thuộc thời xa xưa của những nền văn minh đầu tiên.
cổ điển|Thuộc phong cách lâu đời, được xem là mẫu mực của một thời.
cổ đông|Người nắm giữ phần vốn góp trong công ty.
cổ họng|Phần ống dẫn không khí và thức ăn nằm bên trong cổ người.
cổ hủ|Cũ kỹ, bảo thủ, không thích ứng với thời đại mới.
cổ kính|Cổ xưa, lâu đời và mang vẻ đẹp trang nghiêm, uy nghi.
cổ nhân|Người sống ở thời đại xa xưa.
cổ phần|Số tiền bỏ ra để mua quyền sở hữu trong công ty.
cổ phiếu|Phiếu chứng nhận quyền sở hữu một phần vốn và nhận lợi nhuận của công ty.
cổ tay|Khớp ở ngay dưới lòng bàn tay, giúp bàn tay gập và xoay.
cổ tích|Truyện dân gian thường có nhân vật hoặc sự việc kỳ diệu.
cổ truyền|Được để lại và tiếp tục thực hành qua các thế hệ.
cổ tức|Tiền thưởng chia cho chủ sở hữu cổ phần từ lợi nhuận.
cổ vật|Đồ vật từ thời trước còn lưu lại và có giá trị lịch sử.
cổ vũ|Khích lệ tinh thần để người khác làm việc hăng say.
cổ xưa|Thuộc về thời đại rất lâu trước đây, cách nay đã nhiều thế hệ.
cố công|Gắng sức làm việc một cách kiên trì và bền bỉ.
cố định|Giữ nguyên vị trí hoặc trạng thái không di chuyển, không thay đổi.
cố đô|Nơi từng làm kinh đô của một nước trong quá khứ.
cố gắng|Dùng hết sức lực và tâm trí để hoàn thành việc khó.
cố hữu|Đã có và bám sâu từ lâu, không dễ thay đổi.
cố kết|Gắn bó chặt chẽ với nhau tạo thành khối vững chắc.
cố nhiên|Chắc chắn, tất nhiên là như vậy.
cối xay|Dụng cụ dùng chuyển động quay để nghiền hạt hoặc tách vỏ.
côn trùng|Động vật nhỏ, không có xương sống, có sáu chân và bộ xương cứng bên ngoài.
công ăn việc làm|Việc làm để kiếm tiền nuôi sống bản thân.
công bằng|Áp dụng cùng nguyên tắc, không thiên vị bên nào.
công bố|Nói ra hoặc đăng tải thông tin để mọi người đều biết.
công chiếu|Đưa một bộ phim ra chiếu cho công chúng xem.
công chúng|Tập thể đông đảo những người xem xét.
công chức|Người làm việc thường xuyên cho nhà nước có lương.
công chứng viên|Người chuyên nghiệp làm nhiệm vụ xác nhận tính hợp pháp của giấy tờ.
công cốc|Làm việc vất vả mà không thu được kết quả.
công cộng|Thuộc về chung của mọi người trong xã hội.
công cụ|Đồ dùng để làm việc hoặc sản xuất.
công danh|Vị trí xã hội và danh tiếng được công chúng biết đến.
công dân|Người có quyền lợi và nghĩa vụ sống trong một quốc gia.
công diễn|Diễn ra trước mặt nhiều người xem một cách chính thức.
công du|Người quan trọng đi làm việc công vụ ở nơi xa.
công dụng|Lợi ích thực tế nhận được khi sử dụng vật dụng.
công đoạn|Một bước hoặc giai đoạn cụ thể trong quy trình sản xuất hoặc làm việc.
công hiệu|Khả năng tạo ra kết quả hoặc tác dụng rõ rệt sau khi thực hiện một việc gì đó.
công hữu|Thuộc về mọi người cùng chung hưởng.
công ích|Lợi ích chung dành cho cả tập thể hoặc toàn xã hội.
công khai|Làm việc hoặc chia sẻ thông tin trước mặt tất cả mọi người, không giấu giếm hay kín đáo.
công khố|Kho chứa tiền bạc và tài sản của nhà nước.
công lao|Sức lực đã bỏ ra và đóng góp đáng ghi nhận của ai đó.
công lập|Do cơ quan nhà nước thành lập và quản lý, như một số trường học.
công luận|Ý kiến chung của mọi người trong xã hội.
công lực|Sức mạnh nội tại do luyện tập tạo ra, tác động mạnh vào đối tượng.
công minh|Xét việc công bằng và phân biệt rõ đúng sai.
công nghệ|Phương pháp dùng máy móc, dụng cụ để tạo ra sản phẩm.
công nghệ cao|Công nghệ ứng dụng những thành tựu khoa học mới nhất và chính xác.
công nghệ phần mềm|Cách dùng máy tính và lập trình để tạo ra các chương trình phần mềm.
công nghệ thông tin|Ngành nghiên cứu và ứng dụng kỹ thuật xử lý thông tin.
công nghiệp|Ngành kinh tế hiện đại khai thác tài nguyên, chế tạo công cụ và sản xuất hàng hóa.
công nhân viên|Tập hợp người làm việc và người giữ chức vụ trong cơ quan nhà nước.
công nhật|Tiền trả cho người làm việc theo ngày.
công nhiên|Làm việc công khai, rõ ràng trước mọi người.
công nông nghiệp|Tổng hợp hai ngành sản xuất công nghiệp và trồng trọt.
công nợ|Tổng số tiền nợ và số tiền phải trả trong các giao dịch.
công sản|Tài sản, của cải thuộc về chung nhà nước hoặc cộng đồng.
công sở|Nơi làm việc chung của các cơ quan nhà nước hoặc doanh nghiệp.
công sức|Nỗ lực và sức lực bỏ ra để làm việc.
công tắc|Bộ phận cho phép nối hoặc ngắt đường điện khi thao tác.
công thái học|Môn khoa học nghiên cứu về khả năng và giới hạn của con người trong lao động.
công thự|Tòa nhà lớn dùng làm nơi làm việc của cơ quan nhà nước.
công thức|Dãy ký hiệu viết tắt thể hiện quy tắc, nguyên lý hoặc sự kiện chung.
công thương|Tổng hợp hai lĩnh vực sản xuất hàng hóa và mua bán trao đổi.
công trình|Kết quả của việc xây dựng để phục vụ nhu cầu sinh hoạt hay đi lại của cộng đồng.
công trình phụ|Những công trình xây dựng nhỏ đi kèm với ngôi nhà chính, dùng để phục vụ nhu cầu sinh hoạt hàng ngày.
công trình xây dựng|Kết quả của lao động con người gắn chặt với đất.
công trường|Nơi đang tiến hành xây dựng công trình.
công ước|Văn bản do nhiều nước cùng ký để quy định luật chơi.
công văn|Giấy tờ dùng để trao đổi công việc nhà nước.
công việc|Nhiệm vụ cần bỏ công sức và thời gian để thực hiện.
công viên|Khu đất dành cho mọi người đi dạo, nghỉ ngơi và vui chơi.
công viên nước|Nơi công cộng có hồ bơi và trò chơi dưới nước.
công xưởng|Nơi chứa nhiều máy móc lớn để sản xuất hàng hóa với quy mô rộng.
cồng chiêng|Các nhạc cụ gõ bằng kim loại, thường dùng thành bộ.
cồng kềnh|Lớn cồng, nặng nề và chiếm nhiều chỗ.
cổng|Lối ra vào qua hàng rào hoặc tường bao.
cổng chào|Cổng xây dựng ở đầu đường để báo hiệu điểm đến hoặc ranh giới.
cống hiến|Cho đi những gì quý giá nhất để giúp việc chung thành công.
cộng đồng|Một tập hợp những người chung sống hoặc có điểm tương đồng.
cộng sự|Người cùng làm việc chung với nhau.
cốt cách|Đức tính, khí chất riêng biệt và cao quý của một con người.
cốt cán|Người hoặc nhóm người giữ vai trò then chốt, quyết định sự thành bại của tổ chức.
cốt liệu|Vật liệu xây dựng gồm cát, sỏi, đá nhỏ dùng trộn với xi măng.
cốt lõi|Phần quan trọng nhất, yếu tố chủ yếu của sự vật.
cốt truyện|Dòng sự kiện chính dẫn dắt diễn biến và phát triển nhân vật.
cốt tử|Vấn đề quan trọng nhất cần giải quyết.
cột buồm|Cột cao dựng trên thuyền để nâng cánh buồm.
cột cờ|Cây cột cao dùng để treo lá cờ của đất nước.
cột trụ|Cột lớn, vững chãi dùng để nâng đỡ, chống lại trọng lượng lớn.
cơ bản|Coi như là nền tảng gốc rễ của mọi thứ.
cơ bắp|Bắp thịt; cũng chỉ công việc cần dùng nhiều sức mạnh.
cơ cấu|Cách sắp xếp và phối hợp các bộ phận để máy vận hành theo quy luật.
cơ chế|Cách thức hoạt động và quy luật vận hành bên trong.
cơ giới|Các trang thiết bị sử dụng máy móc trong sản xuất.
cơ học|Ngành vật lý nghiên cứu lực và chuyển động của các vật.
cơ hội|Thời điểm thuận lợi để đạt được thành công.
cơ khí|Lĩnh vực thiết kế, chế tạo và sửa chữa máy cùng chi tiết máy.
cơ man|Số lượng đồ vật hoặc người nhiều đến mức không thể đếm được.
cơ năng|Năng lượng của một vật do chuyển động hoặc vị trí của nó.
cơ nghiệp|Tài sản tích lũy được để làm nền tảng cho cuộc sống.
cơ ngơi|Tổng hợp nhà cửa, ruộng đất và tài sản đã tích lũy.
cơ quan|Đơn vị hành chính hoặc tổ chức thực hiện chức năng.
cơ sở|Nền tảng để xây dựng hoặc dựa vào.
cơ sở dữ liệu|Tập hợp các thông tin được sắp xếp có trật tự để lưu trữ.
cơ sở hạ tầng|Mạng công trình thiết yếu như điện, đường và cấp nước.
cơ thể|Toàn bộ cấu trúc sống của một cá thể.
cờ cá ngựa|Trò đua quân hình ngựa trên bàn chơi, số bước dựa vào xúc xắc.
cờ lê|Dụng cụ kẹp vào đai ốc để vặn chặt hay nới lỏng.
cờ tướng|Trò cờ có hai bên tướng, sĩ, tượng và các quân khác.
cờ vây|Trò chơi đặt quân đen, trắng ở giao điểm để bao vùng trên bàn cờ.
cờ vua|Trò cờ có vua, hậu và các quân khác trên 64 ô đen trắng.
cơi nới|Xây thêm phần mới để làm rộng diện tích nhà cửa.
cởi mở|Bày tỏ tâm tư, cảm xúc một cách tự nhiên và không che giấu.
cơm áo|Cơm ăn, áo mặc; nhu yếu phẩm cơ bản của đời sống.
cơm bình dân|Loại cơm giá rẻ, phục vụ nhu cầu ăn uống của đại đa số người dân.
cơm bữa|Lượng cơm ăn vào mỗi bữa trong cuộc sống hàng ngày, mang tính thường nhật.
cơm cháo|Các món ăn chính hàng ngày như cơm trắng hay cháo loãng.
cơm gạo|Thực phẩm và nhu yếu phẩm để nuôi sống người.
cơm hộp|Cơm ăn được đựng trong hộp nhựa hoặc giấy.
cơm nắm|Cơm chín ép chặt thành phần có thể cầm tay.
cơm nước|Việc lo nấu và dọn các bữa ăn hằng ngày.
cơm rang|Cơm xào nóng trên chảo, thường trộn với trứng hoặc rau.
cơm tấm|Món cơm nấu từ hạt gạo vỡ, thường ăn cùng đồ nướng.
củ cải|Rau có rễ phình to thành củ, thường màu trắng và ăn được.
củ cải đường|Cây trồng lấy rễ phình to chứa nhiều đường để chế biến đường.
cú mèo|Chim cú thường kiếm ăn về đêm, có mặt tròn và mắt hướng ra trước.
cú pháp|Quy tắc sắp xếp các từ để tạo thành câu hoàn chỉnh.
của cải|Tổng hợp các tài sản, tiền bạc và vật dụng quý giá mà người ta sở hữu.
của riêng|Thứ thuộc về một người hay một nhóm, không phải dùng chung.
cúc vạn thọ|Loài hoa cúc có cánh vàng đậm xếp dày thành khối tròn, lá xẻ thùy, mùi hắc.
cục bộ|Chỉ thuộc về một phần nhỏ trong tổng thể.
cục cưng|Con người hoặc vật nuôi được yêu thương và chiều chuộng hết mực.
cục diện|Tình hình chung của cuộc tranh chấp trong một khoảng thời gian.
cục mịch|Thô kệch, vụng về, thiếu tinh tế trong cách ứng xử.
cục tẩy|Cục vật cứng dùng để xóa chữ viết sai trên giấy.
cùi chỏ|Phần xương nối giữa cánh tay và bàn tay ở mặt trước.
cung cách|Cách ứng xử, hành động thể hiện qua vẻ bề ngoài.
cung cấp|Đưa đến nơi cần dùng những thứ cần thiết.
cung kính|Thái độ rất tôn trọng, lễ phép.
cung ứng|Cung cấp hàng hóa hoặc dịch vụ để đáp ứng nhu cầu cần thiết.
cùng chung|Hai hay nhiều người dùng chung một vật hay chịu chung một việc.
cùng tận|Đến mức cuối cùng, không còn gì thêm nữa.
củng cố|Làm cho vững hoặc chắc hơn so với hiện trạng.
cũng như|Nối thêm đối tượng tương tự hoặc đặt hai bên cạnh nhau để so.
cuốc|Dụng cụ có lưỡi tra ngang cán dài để xới đất.
cuộc bầu cử|Quá trình người dân đi bỏ phiếu để chọn người đại diện.
cuộc đời|Thời gian con người sống trên đời.
cuộc sống|Tổng hợp mọi việc làm và trải nghiệm trong đời.
cuối cùng|Ở sau mọi phần hoặc mọi bước còn lại.
cuối tuần|Hai ngày cuối cùng của tuần, thường là thứ Bảy và Chủ nhật.
cuồn cuộn|Chảy mạnh, liên tục thành từng lớp nối nhau.
cuộn|Quấn vật dài hay mỏng thành nhiều vòng.
cuồng loạn|Mất kiểm soát, hành động hỗn loạn không theo trật tự.
cuồng nhiệt|Bộc lộ sự hào hứng rất mạnh đối với điều mình yêu thích.
cuống|Phần nối hoa, lá hay quả với cành.
cuống họng|Phần cổ họng sâu bên trong, nơi bắt đầu của đường thở.
cuống phổi|Phần nối giữa đường dẫn không khí và túi chứa khí.
cuống quýt|Làm việc vội vàng, mất bình tĩnh khiến hành động rối rắm.
cúp điện|Ngắt dòng điện khiến đèn và thiết bị ngừng hoạt động.
cư dân|Người sinh sống và ở lại lâu dài tại một địa phương.
cư trú|Sống và sinh hoạt thường xuyên tại một địa điểm cụ thể.
cư xá|Khu nhà ở tập thể gồm nhiều căn phòng giống nhau.
cư xử|Cách ứng xử, hành động với người khác trong đời sống.
cử chỉ|Hành động hoặc điệu bộ thể hiện ý nghĩ bên trong.
cử động|Làm một phần của cơ thể chuyển sang vị trí khác.
cử hành|Thực hiện một sự kiện quan trọng với thái độ trang trọng.
cử nhân|Người được cấp bằng sau khi hoàn thành một chương trình đại học.
cứ liệu|Tài liệu, số liệu hoặc thông tin dùng làm căn cứ để thực hiện công việc.
cửa hàng|Nơi bày bán hàng hóa cho khách lựa chọn.
cửa hiệu|Nơi bán hàng, thường nhỏ và do cá nhân tự kinh doanh.
cửa khẩu|Nơi người, hàng và phương tiện được phép qua biên giới.
cửa kính|Khung cửa lắp tấm kính trong suốt để nhìn xuyên qua.
cửa sổ|Ô trên tường để lấy sáng, thông gió hoặc nhìn ra ngoài.
cửa sông|Nơi dòng nước lớn đổ ra biển hoặc hợp vào sông khác.
cực chẳng đã|Bắt buộc phải làm điều không muốn vì hoàn cảnh quá khó khăn.
cực nhọc|Làm việc vất vả, nặng nhọc khiến người ta mệt mỏi.
cưng chiều|Yêu thương quá mức, chiều theo ý thích.
cứng cỏi|Mạnh mẽ, không chịu khuất phục trước khó khăn.
cứng đầu|Không nghe lời khuyên, không chịu làm theo ý người khác dù phải vâng.
cứng ngắc|Chất rắn không mềm, khó uốn cong hay biến dạng.
cứng rắn|Bền bỉ, không mềm yếu trước áp lực hay khó khăn.
cước phí|Tiền phải trả cho dịch vụ vận chuyển hàng hóa hoặc hành lý.
cười|Biểu lộ niềm vui qua nét mặt hoặc thành tiếng.
cười duyên|Cười một cách duyên dáng để gây thiện cảm.
cười gượng|Cười cố gắng để che giấu sự không vui hoặc ngượng.
cười rộ|Cười to, nhiều người cùng lúc do vui mừng đột ngột.
cười trừ|Cười để lảng tránh câu hỏi hoặc vấn đề không muốn đối mặt.
cưới xin|Tổ chức lễ thành hôn theo phong tục và nghi thức truyền thống.
cườm|Hạt nhỏ nhiều màu dùng để xâu hay đính trang trí.
cương quyết|Quyết tâm mạnh mẽ, không thay đổi dù có khó khăn.
cương trực|Có tính cách cứng rắn, không chịu khuất phục và luôn giữ lẽ phải.
cương vị|Vai trò hoặc vị trí mà một người đảm nhiệm.
cường điệu|Nói quá mức sự thật để gây chú ý cho người nghe.
cường độ|Độ lớn hay mức độ mạnh yếu của một sự vật, hiện tượng.
cường lực|Sức mạnh rất lớn, tác động mạnh mẽ vào đối tượng.
cường thịnh|Có sức mạnh lớn và phát triển thịnh vượng.
cường tráng|Cơ thể khỏe mạnh, đầy đặn và tràn đầy sức lực.
cưu mang|Giúp đỡ người gặp khó khăn, nguy hiểm.
cứu giúp|Giúp đỡ người gặp nạn.
cứu trợ|Cứu giúp người gặp nạn hoặc khó khăn.
cứu vãn|Hỗ trợ, can thiệp để đưa tình hình nguy hiểm trở lại trạng thái bình thường hoặc an toàn.
cứu viện|Đưa thêm lực lượng hoặc vật chất để hỗ trợ khi đang gặp khó khăn.
cựu sinh viên|Học sinh đã hoàn thành chương trình đào tạo và rời trường.
da dẻ|Lớp da bao bọc cơ thể người, nhìn thấy được bên ngoài.
da diết|Thấm sâu, day dứt và không nguôi ngoai.
da láng|Da động vật đã qua xử lý, được đánh bóng và phủ chất làm cho bề mặt ngoài sáng bóng.
da thuộc|Lớp da động vật đã qua xử lý hóa chất để làm đồ dùng.
dã ngoại|Chuyến đi chơi và sinh hoạt ngoài trời, xa chỗ ở thường ngày.
dạ hội|Cuộc liên hoan trang trọng được tổ chức vào buổi tối.
dạ quang|Sáng lên màu xanh trong bóng tối nhờ chất phát quang.
dai dẳng|Kéo dài thời gian lâu, không ngừng nghỉ.
dài dòng|Nói nhiều, viết nhiều khiến người nghe phải mất thời gian vô ích.
dài hạn|Có thời gian kéo dài trong một khoảng khá lâu, trái ngược với ngắn hạn.
dải đất|Phần đất hẹp, dài uốn cong như một vòng đai bao quanh.
dàn trải|Phân tán rộng ra, không tập trung.
dàn xếp|Bàn bạc để sắp xếp mọi việc cho ổn thỏa.
dáng dấp|Hình dáng, vẻ bề ngoài thể hiện qua các nét chính.
dáng đi|Cách người di chuyển bằng chân từ nơi này sang nơi khác.
dáng điệu|Cách đi đứng, cử chỉ và vẻ ngoài thể hiện tính cách.
dáng vẻ|Hình dáng và vẻ bề ngoài nhìn thấy được.
danh bạ|Danh sách ghi tên người hoặc tổ chức theo chủ đề.
danh ca|Ca sĩ nổi tiếng được nhiều người biết đến.
danh dự|Đức tính cao quý khiến người ta được xã hội tôn trọng.
danh hiệu|Tên gọi thể hiện thành tích hoặc phẩm chất.
danh lam|Nơi có phong cảnh đẹp được nhiều người biết đến.
danh lam thắng cảnh|Nơi đẹp nổi tiếng thu hút khách.
danh lợi|Danh tiếng và lợi ích vật chất mà con người thường theo đuổi.
danh mục|Danh sách ghi tên các mục đã được sắp xếp theo loại.
danh ngôn|Lời nói hay, sâu sắc được nhiều người biết đến và truyền tụng.
danh nhân|Người nổi tiếng và được cộng đồng tôn vinh.
danh sách|Bản liệt kê tên người hoặc sự vật theo từng mục.
danh thiếp|Thiếp nhỏ ghi tên, nghề, chức và địa chỉ.
danh thủ|Người chơi giỏi nhất, nổi tiếng trong lĩnh vực đó.
danh tính|Thông tin xác định về tên gọi, lai lịch và bản sắc riêng của một người hoặc vật.
danh vọng|Tên gọi tốt đẹp về địa vị mà mọi người đều kính trọng.
danh xưng|Tên gọi dùng để chỉ người hoặc vật.
dành|Để riêng ra cho một người hay một mục đích.
dành dành|Cây bụi có hoa trắng thơm và quả cho màu vàng.
dao động|Chuyển động lên xuống hoặc qua lại quanh một điểm cố định.
dạt dào|Nước dâng lên nhiều, tràn đầy và chảy mạnh liên tục.
dãy núi|Nhóm các ngọn núi nối tiếp nhau tạo thành một dãy dài.
dãy số|Tập hợp các con số được sắp xếp theo quy luật nhất định.
dạy bảo|Hướng dẫn người khác hiểu biết điều đúng đắn và lẽ phải.
dạy dỗ|Giáo dục trẻ bằng cả lời khuyên nghiêm khắc và sự quan tâm.
dạy học|Hướng dẫn người học tiếp thu kiến thức và rèn kỹ năng.
dặn dò|Nói kỹ những điều người khác cần nhớ trước khi làm việc.
dằng dặc|Kéo dài rất xa, dường như không có điểm kết thúc.
dân ca|Bài hát truyền qua nhiều thế hệ trong một cộng đồng.
dân chơi|Người sành điệu, am hiểu và thích thú với các trò giải trí.
dân chúng|Tập hợp đông đảo những người dân bình thường trong xã hội.
dân công|Người dân tham gia lao động chân tay theo quy định nhà nước.
dân cư|Tập thể những người sinh sống và định cư tại một vùng.
dân dụng|Dùng phục vụ nhu cầu sinh hoạt hàng ngày của dân chúng.
dân gian|Những sáng tác do nhân dân sáng tạo và lưu truyền.
dân lập|Do người dân tự xây dựng và quản lý.
dân phòng|Người trực tiếp tham gia công tác phòng cháy và bảo vệ an ninh địa phương.
dân quê|Những người làm việc ở nông thôn.
dân số|Tổng số người sinh sống trong một vùng lãnh thổ tại một thời điểm cụ thể.
dân sự|Việc liên quan đến đời sống thường nhật của người dân.
dân tình|Tình trạng, hoàn cảnh chung của nhân dân.
dân tộc|Cộng đồng người có chung nguồn gốc, lãnh thổ và văn hóa.
dần dần|Làm việc hoặc thay đổi từng chút một, không vội vàng mà đi từ từ qua từng giai đoạn.
dẫn chương trình|Người đứng ra giới thiệu và điều khiển chương trình.
dẫn dắt|Dẫn lối để người đi đúng hướng hoặc đạt mục đích.
dẫn điện|Cho phép dòng điện chạy qua vật liệu đó.
dấn thân|Chủ động tham gia sâu vào một việc hoặc một cuộc đời mới.
dập dềnh|Chuyển động lên xuống nhẹ nhàng như sóng nước.
dập dìu|Đi lại liên tục, nối đuôi nhau tạo nên cảnh náo nhiệt.
dâu tây|Quả nhỏ thường đỏ khi chín, có những hạt nhỏ lấm tấm bên ngoài.
dầu ăn|Chất lỏng được lọc từ thực vật dùng để nấu nướng và ăn uống.
dầu hào|Nước xốt nêm món ăn có vị đậm, theo truyền thống làm từ hàu.
dầu khí|Tài nguyên nhiên liệu từ dầu mỏ và khí đốt.
dầu lửa|Dầu thô dùng để chế biến thành nhiên liệu đốt.
dầu mè|Dầu ép từ hạt vừng, có mùi thơm dùng nêm thức ăn.
dầu mỏ|Chất lỏng đen, nặng mùi khai được khai thác từ lòng đất dùng làm nhiên liệu và nguyên liệu công nghiệp.
dầu nhờn|Chất lỏng đặc, bôi vào máy để giảm ma sát và ngăn hư hỏng.
dấu chấm hỏi|Dấu ? đặt cuối câu để biểu thị ý nghi vấn, cần trả lời.
dấu gạch ngang|Dấu nối dùng để tách phần chú thích hoặc ghép các tên riêng lại.
dấu hiệu|Dấu cho biết điều gì đó sắp xảy ra hoặc đang có.
dấu phẩy|Dấu câu ngăn quãng ngắn giữa các thành phần trong câu.
dấu vết|Dấu hiệu còn lại để nhận biết sự việc đã qua.
dây an toàn|Dây đai cố định người ngồi trên xe để tránh bị văng ra khi xảy ra va chạm mạnh.
dây buộc|Đồ dùng dùng để thắt chặt hoặc buộc lại các vật.
dây cáp|Dây lớn gồm nhiều sợi hoặc lõi, dùng truyền tín hiệu hay chịu lực.
dây chuyền|Dây gồm nhiều mắt nối nhau, dùng để chuyền hàng hoặc làm trang sức.
dây cương|Dây buộc vào miệng ngựa để người cưỡi điều khiển hướng đi.
dây dẫn|Cái dây cho dòng điện chạy qua.
dây dưa|Kéo dài sự việc ra, không dứt điểm.
dè dặt|Cẩn trọng, hạn chế hành động để tránh sai lầm.
dẻo dai|Bền bỉ, có sức chịu đựng tốt trong thời gian dài.
dép lê|Dép hở gót, có thể xỏ chân vào mà không cần cài quai sau.
dễ dãi|Không đặt điều kiện khó khăn, dễ dàng chấp nhận mọi yêu cầu.
dễ dàng|Không khó khăn, không cần nhiều công sức hay điều kiện.
dễ nghe|Âm thanh dễ chịu, làm người nghe thấy thoải mái.
dễ thương|Gây được tình cảm yêu quý, thương mến ở người khác.
dễ tính|Dễ thỏa mãn, không đòi hỏi nhiều để vui lòng.
dệt kim|Dùng kim móc để kết nối các sợi len thành tấm vải.
di chúc|Lời dặn dò những việc cần làm sau khi người đó qua đời.
di chuyển|Đưa vật hoặc người từ nơi này sang nơi khác.
di cư|Di chuyển đến sinh sống ở nơi khác.
di dân|Người rời bỏ nơi ở cũ để đến sinh sống ở nơi khác.
di động|Di chuyển chỗ này sang chỗ khác, không cố định tại một nơi.
di sản|Tài sản, giá trị do người xưa để lại cho đời sau.
di tích|Dấu vết hoặc công trình còn lại từ một thời trước.
dĩ nhiên|Chắc chắn là đúng như vậy, không cần nghi ngờ.
dịch chuyển|Sự thay đổi vị trí của các bộ phận trong một vật.
dịch giả|Người chuyển nghĩa từ ngôn ngữ này sang ngôn ngữ khác.
dịch vụ|Công việc giúp đỡ người khác có trả tiền.
diệc|Chim chân dài, cổ dài, rình bắt cá ở vùng nước nông.
diêm|Que nhỏ cho lửa khi quẹt đầu que lên vỏ hộp.
diêm dúa|Trang điểm hoặc ăn mặc cầu kỳ, phô trương hình thức quá mức.
diễm phúc|Hạnh phúc lớn lao và may mắn hiếm có.
diên vĩ|Loài hoa màu tím có gốc từ nhiều vùng trên thế giới.
diễn biến|Cách sự việc thay đổi và phát triển theo thời gian.
diễn dịch|Cách suy luận từ nguyên lý chung đến trường hợp riêng.
diễn đàn|Nơi công cộng để mọi người cùng thảo luận, chia sẻ ý kiến.
diễn đạt|Biến suy nghĩ thành lời nói hoặc hành động cụ thể.
diễn giả|Người đứng trước đám đông để nói về một chủ đề cụ thể.
diễn giải|Diễn đạt ý nghĩa và giải thích rõ ràng cho người khác hiểu.
diễn kịch|Tham gia đóng vai và biểu diễn các tình tiết trong vở kịch.
diễn ra|Xảy ra, diễn biến trong thực tế.
diễn tả|Biểu lộ suy nghĩ tình cảm qua lời nói cử chỉ.
diễn tiến|Thay đổi dần theo thời gian và hướng đi.
diễn văn|Bài nói chuyện trang trọng được đọc trước đám đông.
diễn viên|Người chuyên hát, múa hoặc đóng vai trong phim, kịch.
diễn xuất|Thể hiện nhân vật trong vở kịch hoặc bộ phim.
diện mạo|Ngoại hình, dáng vẻ tổng thể của người hoặc sự vật.
diện tích|Số đo độ rộng của một bề mặt, tính bằng đơn vị vuông.
diều|Đồ chơi đón gió để bay cao, có dây giữ từ dưới đất.
diều hâu|Chim săn mồi lớn, mỏ quặp, móng nhọn, thường lượn trên cao để tìm con mồi dưới đất.
dinh cơ|Khu nhà ở rộng lớn, đồ đạc đầy đủ và vững chãi.
dinh dưỡng|Chất cần thiết để nuôi sống cơ thể.
dinh thự|Ngôi nhà lớn, nguy nga dành riêng cho quan lại hoặc người giàu có.
dìu dắt|Hướng dẫn và giúp ai từng bước tiến bộ.
dìu dịu|Cảm giác nhẹ nhàng, không quá mạnh.
dịu dàng|Thái độ nhẹ nhàng, êm ái khiến người khác dễ chịu.
dịu hiền|Thái độ mềm mỏng, nhân hậu và dễ gần.
dò hỏi|Hỏi thăm kín đáo để biết tin.
doanh nghiệp|Nơi tổ chức sản xuất hàng hóa để bán lấy tiền.
doanh thu|Tổng số tiền thu về từ hoạt động buôn bán.
dọc đường|Trong lúc đang di chuyển trên con đường.
dọn dẹp|Làm sạch và sắp xếp lại đồ đạc cho ngăn nắp.
dọn đường|Chuẩn bị điều kiện thuận lợi để việc làm dễ dàng hơn.
dọn sạch|Làm cho sạch sẽ hoặc đánh đuổi kẻ xấu.
dong dỏng|Mô tả dáng người gầy guộc và cao ráo.
dong riềng|Cây có thân rễ chứa bột, thường dùng lấy bột để làm miến.
dòng chảy|Nước hoặc khí di chuyển liên tục theo một hướng.
dòng điện một chiều|Dòng điện chạy theo một hướng cố định, không đổi chiều.
dồi dào|Số lượng lớn, nhiều đến mức không thiếu hụt trong bất kỳ nhu cầu nào.
dồn dập|Xảy ra nhiều lần sát nhau, gần như không có lúc ngơi.
dông dài|Nói lan man, dài dòng không đi vào trọng tâm.
dở dang|Việc gì đó đang làm dở mà chưa thể hoàn thành.
du canh|Làm ruộng hoặc nương rẫy mà không cố định ở một địa điểm.
du dương|Có âm điệu êm và nối nhau dễ nghe.
du học|Đi học tập tại một quốc gia khác nơi mình đang sinh sống.
du học sinh|Người rời nước mình sang nước khác để học tập.
du khách|Người đi xa đến nơi khác để tham quan, vui chơi.
du lịch|Đi xa đến nơi khác để tham quan.
du mục|Chuyển chỗ sống để chăn nuôi gia súc theo mùa.
du ngoạn|Đi tới nơi khác để tham quan và thưởng thức phong cảnh.
du thuyền|Tàu du lịch nhỏ chuyên chở khách tham quan cảnh đẹp.
dù rằng|Dù có điều kiện không thuận lợi thì vẫn xảy ra.
dung dịch|Chất lỏng hòa tan một chất khác vào trong đó.
dung lượng|Khả năng chứa đựng của một vật.
dung mạo|Dáng vẻ bên ngoài và nét mặt biểu lộ tâm trạng.
dung môi|Chất hóa học dùng để hòa tan hoặc tách rửa các chất khác.
dung nạp|Chấp nhận đưa vào thành viên trong nhóm.
dung thân|Tìm chỗ dựa, nương tựa bản thân trong lúc khó khăn.
dung tích|Số lượng tối đa mà một vật chứa có thể đựng được bên trong.
dùng dằng|Do dự, không dứt khoát vì còn quyến luyến không muốn rời.
dũng cảm|Dám đối mặt việc khó dù biết mình có thể gặp nguy hiểm.
dụng công|Cố gắng nhiều công sức để làm tốt công việc.
dụng cụ|Đồ vật dùng để hỗ trợ cho công việc hoặc sinh hoạt.
dụng ý|Mục đích, ý định mà người ta muốn đạt được.
duy nhất|Chỉ có một, không có thêm bất kỳ cái nào khác.
duy trì|Giữ cho sự việc tiếp tục tồn tại không thay đổi.
duyên|Nét thu hút khiến người khác cảm thấy mến.
duyên hải|Vùng đất nằm ngay bên bờ biển, giáp với đại dương.
dư âm|Tiếng vang còn nghe thấy sau khi âm thanh đã tắt.
dư dả|Có nhiều của cải, vật chất hơn mức cần thiết cho cuộc sống.
dư luận|Ý kiến chung của quần chúng về một vấn đề nào đó.
dư thừa|Nhiều hơn mức cần thiết cho việc sử dụng.
dữ kiện|Thông tin đã biết dùng làm căn cứ để suy luận hay giải bài toán.
dữ liệu|Các con số, thông tin thu thập được để làm căn cứ.
dự án|Kế hoạch hoặc dự thảo văn bản cần thực hiện sau này.
dự báo|Dự đoán trước tình hình sẽ diễn biến thế nào dựa trên các số liệu và thông tin có sẵn.
dự định|Lập trước việc sẽ làm.
dự đoán|Việc suy nghĩ trước để biết kết quả sẽ ra sao.
dự phòng|Vật dụng giữ sẵn để thay thế khi vật chính bị hỏng.
dự thảo|Bản viết còn chờ thảo luận và sửa trước khi chính thức dùng.
dự thầu|Tham gia đấu giá để nhận hợp đồng.
dự thi|Tham gia thi đấu hoặc làm bài kiểm tra để được xét tuyển hoặc xếp hạng.
dự tính|Nghĩ và ước lượng trước việc mình sẽ làm hoặc điều có thể xảy ra.
dự toán|Bản kế hoạch tính trước số tiền thu và chi trong tương lai.
dự trữ|Gom nhiều đồ lại một nơi để dùng khi cần.
dưa chuột|Quả thon mọng nước, thường có vỏ xanh và ăn giòn.
dưa hấu|Quả lớn vỏ cứng, ruột mọng nước, thường có màu đỏ.
dừa nước|Loài họ cau có lá mọc sát mặt nước, thường gặp ở vùng nước lợ.
dựa trên|Lấy một sự việc làm nền tảng để suy nghĩ hay làm việc.
dừng lại|Ngừng hẳn hoặc tạm ngưng một hoạt động, chuyển động đang diễn ra.
dửng dưng|Thờ ơ, không quan tâm hay cảm xúc trước sự việc xảy ra.
dương cầm|Nhạc cụ có bàn phím, phát tiếng khi búa nhỏ gõ vào dây.
dương lịch|Hệ thống tính năm tháng dựa trên chu kỳ quay quanh mặt trời.
dương liễu|Cây liễu mọc bên bờ sông, cành rủ xuống nước.
dường nào|Đến mức độ nào, biết bao nhiêu là.
dường như|Cách nói khi chưa chắc chắn về sự việc hoặc tính chất của một điều gì đó.
dưỡng dục|Nuôi dưỡng và dạy dỗ con cái từ nhỏ đến lớn.
dưỡng lão|Dùng tiền của để nuôi dưỡng khi tuổi già.
dưỡng sinh|Tập luyện để nuôi dưỡng sức khỏe và kéo dài tuổi thọ.
dứt khoát|Quyết định rõ ràng, không do dự hay chần chừ.
đa cảm|Dễ rung động và buồn vui trước những điều xảy ra.
đa dạng|Có nhiều hình thức, nhiều kiểu dáng khác nhau.
đa nghi|Hay nghi ngờ người khác không đáng nghi ngờ.
đa phương tiện|Sử dụng nhiều loại phương tiện khác nhau để truyền tải thông tin.
đa số|Phần gồm nhiều hơn một nửa tổng số đang xét.
đa tài|Có nhiều khả năng giỏi trong nhiều việc khác nhau.
đa thức|Tổng hữu hạn các đơn thức, chẳng hạn biểu thức có lũy thừa nguyên không âm của biến.
đà điểu|Chim lớn không bay, có chân dài và chạy rất nhanh.
đá banh|Cuộc chơi dùng chân để đẩy quả bóng vào lưới đối phương.
đá hoa|Loại đá cứng, có vân đẹp dùng để lát nền hoặc trang trí.
đá hoa cương|Đá granit cứng, thường lộ các hạt khoáng khác màu trên mặt.
đá lửa|Đá cứng dùng để đánh lửa.
đá mài|Đá có bề mặt nhám để mài dụng cụ cho sắc hoặc nhẵn hơn.
đá vôi|Loại đá tự nhiên có thành phần chính là canxi cacbonat, thường dùng để xây dựng hoặc làm vôi.
đài phát|Thiết bị hoặc tổ chức chuyên phát sóng âm thanh qua không khí.
đài phát thanh|Cơ sở sản xuất và phát chương trình âm thanh cho người nghe.
đại bàng|Chim săn mồi cỡ lớn, có cánh rộng và mỏ cong khỏe.
đại chúng|Số đông người dân hoặc những việc phù hợp với lợi ích của đại đa số.
đại cục|Việc chung lớn lao vì lợi ích của cả tập thể.
đại cương|Các nét chính để có cái nhìn ban đầu về một lĩnh vực.
đại diện|Người hoặc tổ chức thay mặt cho người khác.
đại dương|Biển rộng lớn nằm giữa các lục địa.
đại để|Nói chung, không chi tiết cụ thể từng phần.
đại gia|Người có nhiều tiền bạc, sở hữu tài sản lớn trong xã hội.
đại gia đình|Gia đình nhiều thế hệ cùng sống chung.
đại hải|Đại dương rộng lớn bao phủ phần lớn bề mặt Trái Đất.
đại học|Nơi đào tạo bậc cao hơn trung học để nghiên cứu chuyên sâu.
đại học công lập|Trường cao đẳng do nhà nước tài trợ bằng tiền thuế công dân.
đại hội|Hội họp lớn của nhiều người để bàn việc chung.
đại khái|Nêu nét chính mà không đi vào từng chi tiết cụ thể.
đại lộ|Đường phố lớn và rộng, thường có nhiều làn xe.
đại lục|Phần đất liền lớn, bị các biển và đại dương bao quanh ở mọi phía.
đại lượng|Số lượng hoặc tính chất có thể đo đếm được.
đại mạch|Cây ngũ cốc lấy hạt, còn được gọi là lúa mạch.
đại số|Phần toán học dùng chữ và ký hiệu để biểu diễn các quan hệ số.
đại tài|Người có tài năng xuất chúng, hiếm có.
đại thể|Những điểm chính yếu và cốt lõi của vấn đề.
đại trà|Thực hiện trên diện rộng hoặc quy mô lớn.
đại tu|Sửa chữa toàn bộ hoặc phần lớn để khôi phục lại trạng thái tốt.
đại ý|Nội dung cốt lõi, ý chính được tóm tắt ngắn gọn từ toàn bộ sự việc.
đam mê|Yêu thích một việc gì đó đến mức quên hết mọi chuyện khác.
đàm đạo|Nói chuyện thân mật, trao đổi ý kiến với nhau.
đàm phán|Bàn luận để cùng nhau thống nhất cách giải quyết việc gì.
đàm thoại|Trao đổi lời nói để chia sẻ ý kiến với nhau.
đảm bảo|Cam kết chắc chắn về sự đúng đắn hoặc an toàn của một việc.
đảm đang|Có tài năng, làm được nhiều việc và chịu khó gánh vác.
đảm đương|Chịu trách nhiệm làm những việc khó khăn quan trọng.
đảm nhận|Chấp nhận và gánh vác trách nhiệm cho một công việc hay nhiệm vụ.
đảm nhiệm|Chấp nhận và thực hiện một công việc hoặc nhiệm vụ được giao.
đám cưới|Lễ kết hôn giữa hai người.
đám đông|Tập hợp nhiều người tụ họp lại với nhau.
đan lát|Cài các nan hoặc sợi vào nhau để làm đồ dùng.
đan xen|Lẫn vào nhau, cái này nối tiếp cái kia.
đàn bà|Người phụ nữ đã lớn, trưởng thành hoặc già.
đàn bầu|Nhạc cụ Việt Nam có một dây và cần uốn để đổi cao độ.
đàn đá|Nhạc cụ gồm các thanh đá phát ra cao độ khác nhau khi gõ.
đàn hồi|Có khả năng quay lại hình dạng ban đầu sau khi lực tác động dừng lại.
đàn nguyệt|Đàn gảy có thân tròn, cần dài và hai dây.
đàn nhị|Nhạc cụ hai dây, phát âm bằng cách kéo vĩ.
đàn ông|Người thuộc giới nam, thường đã trưởng thành và có nhiều tuổi.
đàng hoàng|Người có học thức, cư xử đúng mực và lương thiện.
đáng kể|Có mức độ lớn đến mức đáng được chú ý.
đáng khen|Dành lời khen cho việc làm tốt đẹp.
đáng khinh|Không đáng được tôn trọng hoặc xem nhẹ.
đáng lẽ|Theo lẽ thường thì phải như vậy nhưng thực tế lại khác.
đáng yêu|Có nét khiến người khác cảm thấy mến và muốn gần gũi.
đánh bạn|Thân thiết với nhau hoặc kết hôn với nhau.
đánh bóng|Chà bề mặt cho nhẵn và phản chiếu ánh sáng tốt hơn.
đánh chữ|Viết chữ trên máy tính bằng bàn phím thay vì viết tay.
đánh dấu|Đặt một dấu tại chỗ cần ghi nhớ hoặc nhận biết.
đánh đàn|Dùng tay hay dụng cụ làm đàn phát thành giai điệu.
đánh đồng|Coi các đối tượng vốn khác nhau là như nhau.
đánh giá|Nhận xét về giá trị hoặc ước tính số tiền của một vật.
đánh hơi|Ngửi mùi để phát hiện hoặc tìm ra vật gì đó.
đánh máy|Viết chữ bằng bàn phím máy tính hoặc điện thoại.
đánh răng|Dùng bàn chải làm sạch răng và các kẽ quanh răng.
đánh thức|Làm cho người đang ngủ hoặc đang nghỉ trở nên tỉnh táo.
đánh vần|Đọc các thành phần rồi ghép lại để phát âm một tiếng viết sẵn.
đào bới|Đào đất và lật xới để tìm kiếm vật gì đó.
đào hoa|Có duyên, được nhiều người yêu mến và quý trọng.
đào luyện|Huấn luyện kỹ năng cho người bằng cách thử thách và rèn giũa.
đào tạo|Giúp người khác có đủ kỹ năng và kiến thức cần thiết.
đào xới|Đào lên, xới lên (dùng cho việc tìm kiếm hoặc lật lại).
đảo lộn|Làm cho trật tự cũ bị phá vỡ, đảo ngược hoàn toàn.
đảo ngược|Thay đổi hoàn toàn chiều hướng ban đầu.
đảo quốc|Quốc gia có lãnh thổ nằm trên một hòn đảo hoặc nhóm đảo.
đáo hạn|Thời điểm hợp đồng hoặc khoản vay đến hạn phải thanh toán hoặc hoàn trả.
đạo diễn|Người đứng đầu chỉ huy toàn bộ quá trình làm phim.
đạo đức|Những chuẩn mực giúp phân biệt cách cư xử tốt và xấu.
đạo đức học|Môn học nghiên cứu về các nguyên tắc và chuẩn mực đạo đức.
đạo hạnh|Những đức tính và nhân cách tốt đẹp của con người.
đạo nghĩa|Tình cảm và lẽ phải theo đúng chuẩn mực đạo đức.
đáp án|Lời giải hoặc kết quả được công nhận cho một câu hỏi.
đáp lại|Trả lời lại câu hỏi hoặc yêu cầu của người khác.
đáp số|Kết quả tính ra sau khi giải xong bài toán.
đáp ứng|Làm đúng theo những gì được yêu cầu hoặc mong đợi.
đắc chí|Hạnh phúc vì đạt được điều mình mong muốn.
đắc cử|Trúng được chức vụ hoặc danh hiệu trong cuộc bầu cử.
đặc ân|Ơn huân huệ được ban riêng cho một người.
đặc biệt|Có nét nổi riêng, không giống phần đông.
đặc cách|Được ưu tiên vì có điều kiện đặc biệt.
đặc điểm|Nét riêng biệt, dấu hiệu phân biệt của sự vật.
đặc hiệu|Có tác dụng riêng biệt và hiệu quả cao cho một đối tượng hoặc mục đích cụ thể.
đặc phái|Gửi đi thực hiện một nhiệm vụ riêng biệt, quan trọng hoặc khẩn cấp.
đặc phái viên|Người được cử đi làm nhiệm vụ đặc biệt thay cho cấp trên.
đặc quyền|Quyền lợi đặc biệt chỉ dành riêng cho một người hay nhóm người.
đặc sản|Đồ vật, món ăn hoặc hàng hóa nổi tiếng và chỉ có ở một vùng nhất định.
đặc sắc|Có nét riêng nổi bật và đáng chú ý.
đặc tả|Mô tả kỹ lưỡng chi tiết một bộ phận tiêu biểu để làm rõ bản chất toàn thể.
đặc tính|Tính chất riêng biệt của sự vật.
đặc trưng|Nét tiêu biểu giúp nhận ra một loại sự vật.
đăm chiêu|Có vẻ đang suy nghĩ sâu sắc, bận tâm lo lắng.
đằm thắm|Nồng nàn, sâu sắc và khó phai mờ.
đăng cai|Chịu trách nhiệm tổ chức và điều hành sự kiện lớn.
đăng nhập|Việc nhập tên đăng ký và mật khẩu để truy cập vào hệ thống mạng máy tính.
đăng tải|Viết và công bố thông tin lên mạng internet hoặc các phương tiện truyền thông đại chúng.
đăng xuất|Thao tác rời khỏi tài khoản và ngắt kết nối hệ thống mạng.
đẳng thức|Hệ thống hai số hoặc biểu thức được nối với nhau bằng dấu bằng.
đắng|Có vị như cà phê nguyên chất không pha đường.
đắt đỏ|Có giá cao khiến người mua phải chi nhiều tiền.
đặt cọc|Đưa tiền ứng trước để đảm bảo cho giao dịch.
đặt hàng|Yêu cầu bên bán cung cấp hoặc làm sản phẩm theo thỏa thuận.
đặt tên|Chọn từ ngữ để gọi cho người hoặc vật.
đầm ấm|Gợi cảm giác gần gũi, yên vui giữa những người bên nhau.
đầm đìa|Ướt nhiều đến mức nước thấm sâu qua vải hoặc da.
đầm lầy|Vùng đất thấp ngập nước thường xuyên, có nhiều bùn và cây ưa ẩm.
đậm đà|Có hương vị đậm, ngon hoặc tình cảm sâu sắc, bền lâu.
đậm nét|Có những đường nét nổi bật, rõ ràng và dễ nhận thấy nhất.
đất bùn|Đất trộn lẫn với rơm hoặc chất hữu cơ khác.
đất đai|Bề mặt đất dùng để canh tác hoặc sinh sống.
đất khách|Nơi ở xa quê hương, không phải đất của mình.
đất nước|Vùng lãnh thổ mà dân tộc sinh sống và cai quản.
đất sét|Đất hạt rất mịn, khi ẩm có thể nặn thành hình.
đầu bài|Nội dung đề bài mà học sinh cần làm trong giờ học.
đầu bảng|Đứng vị trí số một trong danh sách xếp hạng.
đầu bếp|Người làm nghề chế biến món ăn.
đầu đàn|Dẫn dắt cả đàn; cũng chỉ người tiêu biểu của một lĩnh vực.
đầu đề|Tên gọi ngắn gọn đặt cho một bài viết hoặc bài thơ.
đầu gối|Chỗ khớp giữa chân và đùi, dùng để ngồi hoặc quỳ.
đầu máy|Thiết bị tự hành trên đường ray để kéo toa tàu.
đầu mối|Điểm khởi đầu của một chuỗi sự việc hoặc nơi tập trung nhiều đường lối.
đầu óc|Bộ não, nơi diễn ra hoạt động suy nghĩ và nhận thức.
đầu phiếu|Gõ vào hộp hoặc bỏ phiếu để chọn người lãnh đạo.
đầu ra|Phần sản phẩm hoặc lợi nhuận thu được sau khi hoàn thành công việc.
đầu rau|Khối đất nung kê nồi trên bếp kiểu cũ, thường dùng thành bộ ba.
đầu sách|Một nhan đề riêng, không tính số bản in của nhan đề đó.
đầu tàu|Người đi đầu, làm gương và thúc đẩy hoạt động chung.
đầu tắt mặt tối|Làm việc vất vả suốt ngày, không kịp nghỉ ngơi.
đầu tiên|Thứ tự đứng đầu, không có gì trước nó.
đầu tư|Bỏ tiền bạc, công sức hoặc thời gian vào việc gì để sinh lợi.
đầu vào|Tài liệu, tiền bạc hoặc nguyên liệu đưa vào để sản xuất.
đấu giá|Bán theo cách những người mua đưa giá cạnh tranh với nhau.
đấu thầu|Quá trình nhiều bên cạnh tranh giá để chọn người làm việc hoặc cung cấp hàng hóa.
đấu thủ|Người tham gia vào cuộc thi hoặc trận đấu.
đậu cô ve|Loại đậu quả dài, dẹp thường dùng để nấu ăn.
đậu đũa|Đậu leo có quả dài và thon, thường hái lúc non để làm rau.
đậu nành|Loại đậu lấy hạt để ép dầu, làm sữa hoặc làm đậu phụ.
đậu ngự|Loại đậu có hạt lớn và dẹt, thường được nấu chè.
đậu phộng|Cây họ đậu có quả phát triển trong đất, hạt nhiều dầu.
đậu phụ|Thức ăn thành miếng mềm nhờ làm đông phần sữa từ hạt đậu nành.
đậu rồng|Cây đậu leo có quả dài mang bốn gờ như những cánh dọc.
đậu trắng|Loại đậu có hạt màu trắng, dùng nấu món mặn hoặc chè.
đậu tương|Loại đậu lớn, hạt tròn, dùng để nấu nước tương hoặc làm thức ăn.
đậu xanh|Loại đậu hạt nhỏ, vỏ thường xanh, hay dùng nấu chè.
đầy ắp|Đầy đến mức không thể chứa thêm vật gì nữa.
đầy đủ|Có đủ tất cả các phần cần thiết, không thiếu sót so với yêu cầu.
đầy rẫy|Có rất nhiều, xuất hiện ở khắp nơi.
đầy tớ|Người phục vụ làm việc cho chủ trong xã hội cũ.
đẩy lùi|Làm cho đối phương phải lui lại, không thể tiến lên.
đẩy mạnh|Thúc đẩy để việc đó tiến triển nhanh hơn.
đem ra|Hành động lấy một vật gì đó từ nơi chứa ra để sử dụng.
đen nhánh|Màu đen bóng loáng, sáng lên khi có ánh đèn chiếu.
đen như mực|Tối đen hoàn toàn, không thấy rõ bất kỳ vật gì bên trong.
đèn dầu|Đèn đốt dầu qua một sợi bấc để chiếu sáng.
đèn điện|Dụng cụ dùng để chiếu sáng bằng nguồn điện.
đèn đỏ|Tín hiệu đèn giao thông yêu cầu dừng lại.
đèn lồng|Đèn có khung bao quanh nguồn sáng, thường treo để trang trí.
đèn ông sao|Đèn lồng hình ngôi sao, trẻ em thường rước dịp trung thu.
đèn pha|Thiết bị chiếu sáng tạo chùm tia xa, hẹp nhờ gương và thấu kính.
đèn pin|Đèn mang theo được, dùng điện từ pin để soi đường.
đèn sợi đốt|Bóng đèn dùng dây tóc nóng lên để phát ra ánh sáng.
đèn vàng|Đèn giao thông báo hiệu chuẩn bị chuyển sang tín hiệu đỏ.
đèn xanh|Đèn tín hiệu màu xanh đặt ở ngã tư, báo hiệu phương tiện được phép đi tiếp.
đeo đẳng|Theo đuổi liên tục, không thể dứt bỏ.
đeo đuổi|Bền tâm theo đuổi việc gì đó dù gặp khó khăn.
đẹp duyên|Xứng đôi, hợp nhau về tính cách và ngoại hình.
đẹp đẽ|Có hình dáng, màu sắc hoặc vẻ ngoài gây cảm giác thích mắt.
đẹp đôi|Hai người bạn hoặc vợ chồng rất hợp nhau, vừa ý nhau.
đẹp mắt|Gương mặt, dáng vẻ hoặc đồ vật khiến người nhìn thấy cảm thấy thích và vui vẻ.
đẹp mê hồn|Vẻ đẹp khiến người ta mê mẩn, say đắm không thể rời mắt.
đẹp trai|Người nam giới trẻ có khuôn mặt và dáng vẻ ưa nhìn.
đề án|Bản dự tính chi tiết các việc cần làm để bàn bạc và phê duyệt.
đề bạt|Đưa người ta lên giữ chức vụ cao hơn trong công việc.
đề cao|Đưa lên vị trí cao để được chú ý nhiều hơn.
đề cập|Nhắc đến, nói về một điều gì đó.
đề cử|Giới thiệu tên một người ra để mọi người bỏ phiếu bầu chọn.
đề cương|Bản ghi các ý chính làm nền tảng để viết bài hay làm nghiên cứu.
đề dẫn|Phần mở đầu dùng để giới thiệu hoặc dẫn dắt nội dung chính.
đề mục|Dòng chữ đứng đầu bài viết hoặc chương sách để nêu chủ đề.
đề nghị|Nêu lên ý kiến để mọi người cùng bàn bạc hoặc xem xét.
đề phòng|Chuẩn bị trước để tránh hoặc giảm tác động không mong muốn.
đề tài|Chủ đề, vấn đề được chọn để nghiên cứu hoặc viết.
đề xuất|Đưa ra ý kiến hoặc ý tưởng mới để mọi người cùng xem xét.
để bụng|Giữ kín suy nghĩ, cảm xúc hoặc bí mật trong lòng không nói ra.
để dành|Giữ lại một phần cho lúc sau hoặc cho mục đích riêng.
để đời|Có tiếng tăm được truyền lại qua nhiều thế hệ.
để mắt|Chú ý theo dõi để kịp nhận ra điều cần làm.
để phần|Để lại phần thức ăn cho người vắng mặt ăn sau khi mọi người đã xong bữa.
để tâm|Chú ý quan tâm đến điều gì đó.
đệ nhất|Thứ tự đứng đầu hoặc vị trí quan trọng nhất trong một nhóm.
đêm ngày|Thời gian trôi qua liên tục từ sáng đến tối.
đêm tối|Thời gian từ khi mặt trời lặn đến khi sáng, trời tối đen không thấy ánh sáng.
đền bù|Bồi hoàn lại những thiệt hại hoặc công sức đã bỏ ra bằng tiền hoặc vật chất.
đền đài|Các công trình kiến trúc lớn, trang trọng.
đền đáp|Làm việc tốt để trả ơn cho những điều người khác đã giúp đỡ mình.
đền ơn|Trả lại cho người khác những gì họ đã giúp đỡ mình.
đến điều|Đủ tất cả mọi thứ, không còn thiếu sót điều gì cả.
đến mức|Dẫn vào giới hạn hoặc hệ quả cho thấy mức độ của điều vừa nói.
đến nơi|Sắp xảy ra hoặc sắp đến gần rồi.
đến tuổi|Đủ độ tuổi để được phép làm những việc nhất định.
đều nhau|Giống hệt nhau về số lượng và kích thước.
đi bộ|Di chuyển bằng đôi chân, không dùng phương tiện giao thông.
đi chơi|Ra ngoài gặp gỡ hoặc tìm niềm vui, không vì công việc chính.
đi dạo|Đi chậm rãi để thư giãn, ngắm nhìn hoặc tìm kiếm thứ gì đó.
đi đến|Nơi mà người đến sau khi di chuyển từ chỗ khác.
đi đứng|Cách thức di chuyển chân và giữ thân người.
đi học|Đến nơi để học hỏi kiến thức từ người dạy.
đi làm|Đến nơi thực hiện công việc hằng ngày kiếm sống.
đi lên|Chuyển động từ thấp đến vị trí cao hơn.
đi ra|Bước chân từ nơi đang đứng sang chỗ khác.
đi sát|Tiếp cận trực tiếp để nắm bắt thông tin chính xác.
đi vào|Chuyển động từ bên ngoài vào bên trong một nơi nào đó.
đi vắng|Không có mặt ở nhà, ra khỏi nơi ở.
đi xuống|Chuyển động từ vị trí cao về vị trí thấp hơn.
đĩa cứng|Thiết bị lưu trữ dữ liệu điện tử có tốc độ xử lý nhanh.
đĩa mềm|Vật lưu dữ liệu từ tính dạng đĩa mỏng nằm trong vỏ bảo vệ.
địa bàn|Khu vực địa lý hoặc phạm vi hoạt động cụ thể.
địa chất|Thành phần, cấu tạo và lịch sử của các lớp đất đá.
địa chỉ|Nơi cư trú được ghi chép trên giấy tờ để liên lạc.
địa danh|Tên gọi của một địa điểm cụ thể trên bản đồ.
địa điểm|Nơi chốn cụ thể mà sự việc xảy ra.
địa hạt|Vùng đất thuộc quyền quản lý của một đơn vị hành chính cụ thể.
địa hình|Hình dáng và độ cao thấp của bề mặt đất đai.
địa lợi|Lợi thế tự nhiên do vị trí địa lý thuận lợi mang lại.
địa phận|Phần đất đai thuộc về một địa phương, vùng miền hoặc quốc gia cụ thể.
địa phương|Khu vực riêng biệt, khác với các vùng khác trong cả nước.
địa thế|Hình dáng và vị trí của đất đai.
địa vị|Chỗ đứng xã hội phù hợp với vai trò, trách nhiệm và quyền lợi.
đích danh|Chỉ đúng tên hoặc người cụ thể, không nói chung chung.
đích đáng|Phù hợp hoàn toàn với mức độ, đúng với giá trị bản thân.
đích thân|Chính bản thân người đó trực tiếp làm việc.
đích thị|Chắc chắn đúng là người đó, không phải người khác.
đích thực|Đúng thật, không giả mạo hay hư cấu.
đích xác|Chính xác tuyệt đối, không sai lệch dù chỉ một chút.
điềm đạm|Giữ thái độ bình tĩnh, nhẹ nhàng, không nóng nảy hay gắt gỏng.
điềm tĩnh|Bình thản, không hoảng sợ hay lo lắng.
điểm ảnh|Đơn vị nhỏ nhất cấu thành nên hình ảnh trên màn hình máy tính.
điểm danh|Gọi tên từng người để kiểm tra xem ai đã có mặt.
điểm sách|Lời tóm tắt, đánh giá chung về nội dung cuốn sách.
điểm số|Con số dùng để chấm điểm học tập của học trò.
điểm tâm|Ăn bữa sáng, thường là một bữa nhẹ.
điểm xuyết|Thêm vài nét trang trí vào vật đã có sẵn để làm đẹp thêm.
điểm yếu|Nơi hoặc khía cạnh dễ bị tổn thương nhất.
điền đơn|Viết và nộp giấy tờ để xin cấp giấy phép hoặc đăng ký thủ tục.
điền kinh|Nhóm môn thể thao gồm chạy, nhảy, ném và một số nội dung phối hợp.
điển cố|Sự tích xưa làm khuôn mẫu cho lời văn.
điển hình|Có những nét đặc trưng tiêu biểu nhất của nhóm, dùng làm mẫu để suy luận.
điện|Dạng năng lượng có thể cấp cho đèn và máy móc.
điện ảnh|Nghệ thuật tạo ra hình ảnh chuyển động liên tục để chiếu lên màn hình.
điện áp|Độ chênh điện thế giữa hai điểm của một mạch.
điện gió|Năng lượng sạch dùng sức gió quay máy phát điện.
điện hoa|Dịch vụ chuyển giao các bó hoa tươi kèm quà đến người nhận.
điện lực|Ngành sản xuất, truyền tải và cung cấp điện.
điện máy|Các thiết bị và dụng cụ hoạt động bằng điện năng.
điện mặt trời|Năng lượng điện sinh ra từ ánh sáng và nhiệt của mặt trời.
điện môi|Chất cách điện dùng trong các thiết bị điện.
điện năng|Năng lượng mà dòng điện có thể truyền hoặc chuyển thành dạng khác.
điện phân|Quá trình phân hủy chất bằng cách cho dòng điện chạy qua.
điện thoại|Thiết bị để nói chuyện từ xa nhờ truyền tín hiệu.
điện thoại di động|Thiết bị liên lạc cầm tay nhỏ gọn, có thể bỏ vào túi để gọi điện.
điện tín|Bản tin ngắn gửi qua hệ thống điện báo.
điện trở|Đại lượng vật lý biểu thị khả năng cản trở dòng điện chạy qua một vật dẫn.
điện tử|Sử dụng kỹ thuật điện hoặc hoạt động dựa trên nguyên lý điện.
điệp khúc|Đoạn nhạc và lời được lặp lại nhiều lần trong bài hát.
điệp ngữ|Cách lặp lại từ ngữ để tăng giá trị biểu cảm.
điêu khắc|Nghề làm bằng cách đục đẽo đá hoặc gỗ để tạo thành hình tượng.
điều chế|Làm ra chất mới từ các nguyên liệu sẵn có.
điều chỉnh|Làm thay đổi nhỏ để phù hợp hơn với ý muốn.
điều chuyển|Di chuyển người hoặc vật đến địa điểm khác để phục vụ nhiệm vụ.
điều đình|Bàn luận để tìm cách giải quyết mâu thuẫn giữa các bên.
điều độ|Phân chia công việc hoặc thời gian sao cho đều đặn, không quá nhiều hay quá ít.
điều động|Sắp xếp đưa người hoặc phương tiện đến nơi cần thiết.
điều hành|Chỉ huy và điều phối công việc chung.
điều khiển|Thao tác vào vật hay việc để chúng diễn ra đúng ý muốn.
điều khiển từ xa|Cho thiết bị thực hiện lệnh mà không cần đứng ngay bên máy.
điều khoản|Nội dung trong văn bản pháp luật hoặc hợp đồng phải tuân theo.
điều kiện|Những yếu tố cần phải có để sự việc xảy ra.
điều kiện cần|Điều kiện bắt buộc phải có để một mệnh đề trở nên đúng.
điều lệ|Văn bản ghi rõ các quy tắc và nguyên tắc hoạt động của tổ chức.
điều nghiên|Tìm hiểu kỹ lưỡng và khảo sát thực tế để làm rõ sự việc.
điều phối|Sắp xếp và điều khiển các khâu làm việc.
điều phối viên|Người phụ trách việc sắp xếp và điều hành công việc.
điều tiết|Sắp xếp lại công việc cho cân đối và hợp lý.
điều ước|Mong muốn người ta thầm nghĩ hoặc nói ra.
điệu bộ|Những cử chỉ tay chân dùng để diễn đạt ý nghĩ.
đinh|Thanh kim loại nhỏ có mũ, đóng vào để ghép vật liệu.
đinh ninh|Tin chắc chắn, không còn nghi ngờ gì nữa về một sự việc.
đinh ốc|Đinh kim loại có ren để vặn chặt vật liệu.
đinh vít|Chốt có ren xoắn, gắn vào vật bằng cách vặn.
đình đốn|Trì trệ, không phát triển và sắp tan vỡ.
đỉnh cao|Vị trí cao nhất của một địa hình, sự nghiệp hoặc quá trình phát triển của một sự vật.
đỉnh điểm|Điểm cao nhất của một sự vật hoặc quá trình đang diễn ra.
đĩnh đạc|Thái độ trang nghiêm, vững chãi và đầy tự tin.
đính chính|Sửa lại chỗ sai cho đúng sự thật.
đính hôn|Cam kết sẽ kết hôn với nhau trong tương lai gần.
định cư|Ở lâu dài tại một nơi và coi đó là chỗ sinh sống.
định dạng|Hành động sắp xếp nội dung theo một trình tự hoặc quy định nhất định.
định danh|Việc xác định tên gọi và chứng minh bản chất của người hay vật.
định giá|Việc quy định mức tiền cho sản phẩm hoặc dịch vụ.
định hình|Bắt đầu có hình dạng hoặc những nét rõ ràng, ổn định.
định hướng|Xác định phương hướng đi hoặc đứng.
định liệu|Suy nghĩ và lên kế hoạch trước để giải quyết việc gì.
định luật|Mệnh đề mô tả một quan hệ ổn định trong tự nhiên.
định lượng|Việc đo đạc để xác định con số cụ thể của một đối tượng.
định mức|Số lượng hoặc thời gian được quy định sẵn để hoàn thành công việc.
định nghĩa|Lời giải thích rõ ràng về ý nghĩa của từ.
định rõ|Làm cho một vấn đề, quy định hay ý kiến trở nên cụ thể, tường minh, không còn mơ hồ.
định sở|Nơi cư trú cố định, không thay đổi.
định tâm|Tập trung ý chí, quyết tâm làm việc.
định thần|Làm cho tâm trí trở lại trạng thái bình tĩnh.
định vị|Tìm ra chỗ đứng thực tế của vật dựa trên dấu hiệu phát ra hay nhận được.
đo lường|Việc xác định độ lớn bằng cách so sánh với đại lượng chuẩn.
đỏ au|Màu đỏ rực rỡ, tươi sáng và nổi bật.
đoái hoài|Quan tâm, chú ý và chăm sóc đến người hoặc việc cụ thể.
đoàn kết|Biết hợp sức và gắn bó để đạt mục đích chung.
đoàn thể|Tổ chức xã hội do quần chúng thành lập để bảo vệ quyền lợi chung.
đoàn tụ|Gặp và sống lại bên nhau sau thời gian xa cách.
đoàn viên|Người được chọn làm thành viên trong một tổ chức hoặc hội đoàn.
đoán|Thử đưa ra đáp án từ những dấu hiệu chưa đầy đủ.
đoạn thẳng|Đoạn đường thẳng nối giữa hai điểm xác định.
đọc hiểu|Đọc và nắm rõ ý nghĩa của nội dung.
đòi hỏi|Yêu cầu người khác phải làm hoặc có những gì cần thiết.
đom đóm|Côn trùng nhỏ có thể phát ánh sáng ở phần cuối bụng.
đỏm dáng|Trang điểm kỹ lưỡng để trông đẹp mắt bên ngoài.
đon đả|Nhanh nhẹn, nhiệt tình và vui vẻ khi tiếp xúc với người khác.
đòn tay|Gỗ hoặc tre dùng để đỡ rui mái nhà.
đón tiếp|Gặp gỡ và đãi khách bằng lời nói hoặc đồ ăn.
đóng băng|Chuyển từ dạng lỏng sang dạng rắn do hạ nhiệt độ.
đóng gói|Đặt hàng vào bao bì có kích thước, trọng lượng xác định.
đóng góp|Việc bỏ ra công sức, tiền bạc hoặc tài nguyên để hỗ trợ cho mục đích chung.
đóng khung|Lắp khung quanh tranh, ảnh hoặc một vật phẳng để bảo vệ và trưng bày.
đóng phim|Đảm nhận vai diễn trước máy quay để làm tác phẩm điện ảnh.
đóng thùng|Xếp hàng vào đồ chứa cứng để bảo quản hay vận chuyển.
đô la|Tên đơn vị tiền tệ của một số nước, chẳng hạn Mỹ và Úc.
đồ ăn nhanh|Món được chuẩn bị và phục vụ nhanh, thường có thể mang đi.
đồ chơi|Đồ vật dùng để vui chơi, giải trí cho trẻ em hoặc người lớn.
đồ đạc|Những vật dụng dùng để sinh hoạt hàng ngày trong gia đình.
đồ đệ|Người được thầy truyền dạy nghề nghiệp hoặc kiến thức.
đồ hàng|Những món đồ chơi nhỏ mô phỏng vật dụng để trẻ chơi mua bán, nấu nướng.
đồ nghề|Tập hợp các dụng cụ cần thiết để thực hiện một nghề nghiệp.
đồ sộ|Có kích thước hoặc quy mô lớn gây ấn tượng rõ.
đồ thị|Hình biểu diễn quan hệ giữa các đại lượng bằng điểm hoặc đường.
đồ vật|Thứ vật chất cụ thể, có thể sờ thấy hoặc cảm nhận bằng giác quan.
độ ẩm|Lượng hơi nước chứa trong một đơn vị không khí.
độ bền|Khả năng chịu đựng lâu dài mà không hỏng.
độ chính xác|Mức độ đúng đắn so với lý thuyết hoặc chuẩn mực.
độ nhạy|Khả năng phát hiện hay phản ứng với một kích thích nhỏ.
độ phân giải|Chỉ số đo độ rõ nét của hình ảnh qua số điểm trên mỗi inch.
độ thân|Tự kiếm ăn để qua ngày.
độc đáo|Có tính chất riêng biệt, không giống bất kỳ cái nào khác.
độc giả|Người thường xuyên đọc sách, báo, tài liệu.
độc lập|Trạng thái tự do không phụ thuộc vào ai hay quốc gia nào.
độc nhất|Chỉ duy nhất một cái, không có thứ hai.
độc nhất vô nhị|Thứ duy nhất trên đời, không có gì giống hoặc bằng nó.
độc tấu|Biểu diễn âm nhạc hoặc nghệ thuật chỉ có một người thực hiện.
độc tôn|Được tôn vinh là duy nhất, không ai sánh bằng.
đôi bên|Hai phía đối diện nhau trong một sự việc.
đôi khi|Có lần xảy ra nhưng không đều và không thường xuyên.
đôi nam nữ|Hai người, một nam và một nữ, thường đi cùng nhau hoặc có quan hệ gắn bó.
đổi gió|Thay đổi không khí hoặc hoàn cảnh sống mới mẻ.
đổi mới|Thay đổi để trở nên hiện đại và tốt hơn so với trước.
đổi thay|Dần trở nên khác với hình dạng hay tình trạng ban đầu.
đối chiếu|So sánh hai sự vật để tìm điểm giống và khác nhau.
đối diện|Nằm ở phía trước mặt và hướng về phía bên kia.
đối đáp|Trả lời lại lời người khác nói.
đối tác|Người hoặc đơn vị cùng làm việc chung.
đối thoại|Trao đổi ý kiến qua lời nói giữa nhiều người.
đối thủ|Người cùng tham gia cạnh tranh hoặc đối kháng để quyết định thắng thua.
đối tượng|Người hoặc vật được chọn để nghiên cứu, khảo sát hoặc thử nghiệm.
đối với|Chỉ người, vật hoặc việc được nhắc đến làm đối tượng liên quan.
đối xử|Thể hiện thái độ với người khác qua lời nói và việc làm.
đội ngũ|Tập hợp những người cùng làm một loại công việc.
đội tuyển|Nhóm người giỏi nhất được chọn để thi đấu.
đội viên|Người tham gia đội thiếu niên tiền phong Hồ Chí Minh.
đôn đốc|Thúc giục người khác làm việc cho đạt hiệu quả cao nhất.
đồn đoán|Việc nói lan truyền những tin tức chưa chắc chắn dựa trên phỏng đoán.
đông bắc|Hướng nằm giữa phía Đông và phía Bắc.
đông chí|Tiết trong năm khi Bắc bán cầu có ngày ngắn nhất.
đông đảo|Có mặt hoặc tham gia với số lượng lớn.
đông đặc|Chuyển từ trạng thái lỏng sang rắn khi điều kiện thích hợp.
đông đúc|Nơi có rất nhiều người chen chúc.
đông phương|Thuộc về các nước nằm ở phía mặt trời mọc.
đồng|Khoảng đất rộng ngoài trời để trồng trọt.
đồng áng|Công việc làm trên đồng ruộng, trồng trọt.
đồng âm|Những từ đọc giống nhau nhưng ý nghĩa hoàn toàn khác biệt.
đồng bộ|Các chuyển động cùng nhịp, cùng tốc độ, phối hợp ăn khớp với nhau.
đồng ca|Nhiều người cùng hát một bài với nhau.
đồng cam cộng khổ|Hưởng niềm vui và chịu nỗi khổ cùng nhau trong mọi hoàn cảnh.
đồng cảm|Biết và cảm nhận được nỗi buồn, vui hay đau khổ của người khác như chính mình.
đồng cỏ|Vùng đất rộng chủ yếu phủ cỏ, thường dùng cho gia súc ăn.
đồng dạng|Có hình dáng và kích thước tương tự nhau.
đồng điệu|Cùng nhịp điệu, cùng suy nghĩ hoặc cùng lối sống với nhau.
đồng đội|Người ở cùng một đội và cùng phối hợp thực hiện nhiệm vụ.
đồng hành|Cùng đi chung một con đường hoặc tham gia cùng một quá trình.
đồng hồ|Dụng cụ cho biết giờ hoặc đo thời gian trôi qua.
đồng hồ đeo tay|Thiết bị đo thời gian được thiết kế để đeo quanh cổ tay người dùng.
đồng hương|Người cùng quê hương nhưng đang sống ở nơi khác.
đồng liêu|Cùng làm việc trong một cơ quan hoặc cùng chức vụ.
đồng loại|Những sinh vật cùng thuộc một giống loài với nhau.
đồng loạt|Làm việc hoặc xảy ra cùng một lúc, không ai trước ai sau.
đồng nát|Đồ kim loại cũ hỏng và phế liệu được thu gom để tái chế.
đồng nghĩa|Có cách viết hay phát âm khác nhưng diễn đạt nghĩa giống nhau.
đồng nhất|Có cùng tính chất hoặc được coi là cùng một đối tượng.
đồng phục|Bộ quần áo giống nhau về màu, chất liệu và kiểu dáng cho cùng một nhóm người.
đồng quê|Khu vực nông thôn với đồng ruộng và cảnh quan thiên nhiên.
đồng ruộng|Tổng hợp các thửa đất rộng lớn dùng để cày bừa và gieo trồng cây cối.
đồng tâm|Có cùng một tâm, như các vòng tròn trên mặt bia.
đồng thanh|Nói cùng một lúc với nhau thành một tiếng.
đồng thoại|Thể truyện cho trẻ em thường để loài vật hay đồ vật nói và hành động như người.
đồng thời|Xảy ra vào cùng một lúc.
đồng thuận|Có cùng ý kiến hoặc đồng ý với người khác.
đồng tiền|Đơn vị dùng để trao đổi, mua bán hàng hóa trong xã hội.
đồng tình|Có chung ý kiến và ủng hộ điều người khác nêu.
đồng văn|Có cùng ngôn ngữ, chữ viết hoặc nền văn hóa giống nhau.
đồng ý|Chấp nhận ý kiến hoặc hành động của người khác.
động cơ đốt trong|Thiết bị dùng nhiên liệu cháy trong buồng kín để sinh công.
động đậy|Chuyển động một chút.
động lực|Lực lượng bên trong thúc đẩy con người hoặc sự vật phát triển, tiến bộ.
động não|Suy nghĩ nhiều và sâu sắc để tìm ra cách giải quyết vấn đề.
động năng|Lực lượng sinh ra từ chuyển động của vật thể trong vật lý học.
động sản|Tài sản hữu hình có thể di chuyển được.
động tác|Sự vận động có chủ đích của cơ thể.
động vật|Sinh vật lấy dinh dưỡng từ sinh vật khác, thường có khả năng vận động.
động vật học|Môn khoa học nghiên cứu về đặc điểm và đời sống của động vật.
đột ngột|Xảy ra bất ngờ, không có dấu hiệu báo trước.
đột nhiên|Xảy ra ngay lập tức mà không có dấu hiệu báo trước.
đời đầu|Sản phẩm đầu tiên được làm ra trong một loạt sản xuất.
đời đời|Mãi mãi, kéo dài qua nhiều thế hệ.
đời nào|Không bao giờ xảy ra trong bất kỳ hoàn cảnh nào.
đời sống|Những hoạt động và điều kiện sinh hoạt của con người.
đời thường|Cuộc sống hàng ngày, bình thường, không đặc biệt.
đơn điệu|Ít thay đổi nên dễ gây cảm giác đều đều, thiếu thú vị.
đơn lẻ|Rất ít, đứng một mình không có người cùng.
đơn nguyên|Bộ phận của công trình được giới hạn và là đơn vị hoàn chỉnh.
đơn phương|Chỉ do một bên thực hiện hoặc quyết định.
đơn sơ|Đơn giản, không cầu kỳ.
đơn thuần|Chỉ có một mặt, không pha tạp hay phức tạp với các yếu tố khác.
đơn từ|Giấy viết để trình bày nguyện vọng hoặc yêu cầu với cơ quan.
đơn vị|Đại lượng dùng để đo lường, so sánh với các đại lượng cùng loại.
đơn vị tiền tệ|Loại tiền do nhà nước phát hành làm chuẩn đo lường giá cả.
đu đủ|Quả nhiệt đới có khoang hạt đen, thịt mềm khi chín.
đu đưa|Chuyển động qua lại liên tục theo nhịp đều đặn trong không gian.
đua đòi|Làm theo người khác những việc vô bổ, không cần thiết.
đùa giỡn|Chơi đùa để tạo niềm vui, nói chung.
đùa nghịch|Chơi vui vẻ, nghịch ngợm không nghiêm túc.
đúc kết|Rút ra điều cốt yếu sau khi xem xét nhiều trường hợp hoặc trải nghiệm.
đúc rút|Lấy những phần quan trọng từ nhiều việc để tổng hợp.
đục ngầu|Nước đục đến mức không nhìn xuyên qua được.
đùm bọc|Che chở và giúp đỡ lẫn nhau như người thân trong gia đình.
đun sôi|Đun lửa cho nước nóng lên đến mức bốc hơi mạnh.
đung đưa|Chuyển động nhẹ nhàng qua lại hoặc nghiêng ngả trong không gian.
đủng đỉnh|Làm việc chậm rãi, không vội vàng, từng bước một.
đúng đắn|Phù hợp với thực tế, quy luật và lẽ phải.
đúng mức|Phù hợp với yêu cầu thực tế, không quá nhiều hay quá ít.
đụng chạm|Chạm vào vật thể hoặc xảy ra mâu thuẫn nhỏ.
đuốc|Vật cầm tay được đốt ở một đầu để soi đường.
đuôi|Phần cơ thể nhô dài về phía sau của nhiều loài vật.
đuổi kịp|Đi nhanh hơn để đạt tới người hay vật đang ở phía trước.
đưa đón|Đi đưa người đi và đón người về.
đưa đường|Chỉ đường, hướng dẫn người khác đi đến nơi cần đến.
đưa ra|Nêu một ý hoặc đề nghị để người khác xem xét.
đưa tin|Truyền đạt thông tin về sự việc.
đưa vào|Hành động di chuyển một vật hoặc con người từ bên ngoài vào bên trong một nơi nào đó.
đứa bé|Một người còn nhỏ tuổi, chưa trưởng thành.
đức hạnh|Những tính cách tốt đẹp của con người.
đức tính|Tính tốt đẹp, phù hợp với đạo lý làm người.
đứng|Giữ thân người thẳng, tựa sức nặng trên hai chân.
đứng đầu|Nằm ở vị trí cao nhất hoặc giữ vai trò lãnh đạo trong nhóm.
đứng lớp|Thực hiện nhiệm vụ giảng dạy cho học sinh trong lớp.
đứng tuổi|Đã lớn lên nhưng chưa đến tuổi già cỗi.
đứng vững|Giữ vững tâm trí và thân thể không bị lung lay hay sụp đổ.
được mùa|Thu hoạch nông sản nhiều hơn mức thông thường.
được việc|Làm xong việc được giao một cách nhanh chóng và tốt đẹp.
đười ươi|Vượn lớn lông nâu đỏ, có tay dài và thường sống trên cây.
đượm|Thấm đều và hiện rõ mà không quá gắt.
đương chức|Đang giữ chức vụ, có nhiệm vụ và quyền hạn tại nơi làm việc.
đương đại|Thuộc về thời đại hiện tại, đang diễn ra ngay lúc này.
đương nhiên|Sự việc hiển nhiên, ai cũng phải thừa nhận.
đương thời|Thời gian hiện tại của một sự việc hoặc giai đoạn lịch sử cụ thể.
đường|Tinh thể có vị ngọt dùng pha nước hay làm bánh.
đường bộ|Tuyến giao thông trên đất dành cho người và xe đi lại.
đường bột|Bột mịn làm từ đường dùng để trang trí mặt bánh ngọt.
đường cái|Con đường lớn dùng để xe cộ đi lại giữa các vùng miền.
đường cao tốc|Con đường lớn chỉ dành cho xe cơ giới chạy nhanh, cấm người đi bộ và xe thô sơ.
đường cát|Đường kết tinh thành hạt nhỏ rời nhau, thường dùng nêm hay pha đồ uống.
đường dẫn|Dãy ký hiệu chỉ hướng đi từ nơi bắt đầu đến đích trong máy tính.
đường dây|Tuyến dây dẫn để truyền điện hoặc tín hiệu qua một khoảng cách.
đường đi|Con đường dẫn đến một địa điểm hoặc mục tiêu.
đường hàng hải|Tuyến đường mà tàu thuyền di chuyển trên mặt biển.
đường hướng|Hướng đi và cách thức tiến hành.
đường kính|Đường thẳng dài nhất xuyên qua tâm hình tròn.
đường mòn|Lối nhỏ hình thành do người hoặc vật đi qua nhiều lần.
đường nâu|Loại đường có màu nâu vàng làm từ mía.
đường phố|Đường đi giữa các dãy nhà trong đô thị.
đường ray|Các thanh kim loại làm lối dẫn bánh xe lửa.
đường sá|Tổng hợp các con đường trên bộ dùng cho việc đi lại.
đường sắt|Hệ thống tuyến có ray để tàu hỏa chạy.
đường sắt cao tốc|Hệ thống đường ray chuyên dụng cho các chuyến tàu chạy với tốc độ rất cao.
đường thẳng|Đường kẻ chỉ có một chiều dài, không cong và không có điểm cuối.
đường tròn|Đường cong khép kín trên mặt phẳng, các điểm cách tâm một khoảng bằng nhau.
đường trục|Con đường chính nối các khu vực và tỏa ra nhiều đường nhỏ.
đường trường|Con đường dài và xa, thường gặp nhiều khó khăn vất vả.
đứt đoạn|Bị chia làm nhiều phần rời rạc, không nối tiếp nhau liên tục.
e rằng|Sợ một việc gì sẽ xảy ra.
em bé|Người mới sinh ra, còn nhỏ và chưa biết đi.
em chồng|Người em trai hoặc em gái của chồng mình.
em dâu|Vợ của anh chị em trai mình.
em gái|Người phụ nữ có tuổi nhỏ hơn mình hoặc người khác.
em trai|Người em thuộc giới nam trong một gia đình.
em út|Người em nhỏ tuổi nhất hoặc cuối cùng trong gia đình.
eo biển|Đoạn biển dài và hẹp nối liền hai vùng biển với nhau.
eo hẹp|Không rộng rãi, thiếu thốn hoặc khó khăn.
eo lưng|Phần giữa hẹp lại, hai đầu to ra như hình quả lê.
ê kíp|Nhóm người được tổ chức để cùng làm việc chung.
ếch nhái|Tên gọi chung những động vật lưỡng cư thường nhảy bằng chân sau.
êm ái|Nhẹ nhàng, dễ chịu và tạo cảm giác thoải mái cho người nghe hoặc người cảm nhận.
êm dịu|Nhẹ và dễ chịu, không gây chói gắt hay kích thích mạnh.
êm đẹp|Hoàn cảnh thuận lợi, không có chuyện buồn xảy ra.
êm đềm|Không ồn ào, không gợn sóng, nhẹ nhàng và thanh thản.
êm thấm|Hoàn cảnh ổn định, suôn sẻ, không xảy ra chuyện rắc rối.
gà gáy|Tiếng kêu của gà trống báo hiệu trời sắp sáng.
gà lôi|Chim rừng thuộc họ trĩ, nhiều loài có đuôi dài và bộ lông sặc sỡ.
gà mái|Gà cái trưởng thành, có thể đẻ trứng.
gà rừng|Loài gà hoang dã sống trong rừng, có khả năng bay giỏi và xương cứng.
gà sao|Loài gà lớn, lông màu xám tro.
gà tây|Loài gà lớn, lông màu sặc sỡ, thường nuôi làm thịt hoặc lấy trứng.
gà trống|Gà đực trưởng thành, thường cất tiếng gáy và có mào rõ.
gác bếp|Chỗ kê cao trên bếp, thường để hong hay cất đồ.
gác xép|Tầng nhỏ chen trong khoảng cao giữa nền nhà và mái hoặc trần.
gạch|Khối vật liệu nhỏ dùng để xây tường hay lát nền.
gạch bông|Gạch lát có hoa văn và màu trang trí ở mặt trên.
gạch chân|Vẽ một đường thẳng ngang dưới chữ hoặc cụm từ.
gạch dưới|Vạch một đường thẳng dưới từ hoặc dòng chữ để nhấn mạnh.
gạch men|Gạch lát nền mỏng, bề mặt phủ lớp men bóng chịu nước.
gạch nối|Dấu nối ngắn dùng ghép các phần của từ nước ngoài.
gạch ốp lát|Gạch mỏng dùng để lát sàn hoặc ốp lên tường.
gan bàn chân|Phần thịt dày nằm ở giữa lòng bàn chân, dùng để đứng và đi.
gạn hỏi|Hỏi dồn dập, cố tình bắt người phải trả lời.
ganh đua|Cạnh tranh để giành lấy phần thắng hoặc vị trí cao hơn.
gánh|Vận chuyển đồ bằng cách đặt đòn mang tải lên vai.
gánh vác|Đứng ra nhận và lo liệu phần việc có trách nhiệm.
gạo cội|Dày dạn kinh nghiệm và có vị thế trong một lĩnh vực.
gạo nếp|Gạo cho hạt chín dẻo dính, thường dùng đồ xôi.
gạo tẻ|Gạo thường nấu thành cơm ăn hằng ngày, ít dính hơn nếp.
gạt bỏ|Không quan tâm, bỏ qua hoặc loại trừ một điều gì đó ra khỏi sự chú ý.
gay cấn|Có diễn biến căng và khó đoán khiến người xem hồi hộp.
gãy gọn|Nói hoặc viết ngắn gọn, rõ ràng và dứt khoát.
gặm nhấm|Cắn từng chút bằng răng, như chuột ăn một hạt ngô.
gắn bó|Có quan hệ gần gũi, bền lâu và khó tách rời.
gắn kết|Liên kết chặt chẽ, tạo thành một khối không thể chia cắt.
gắn liền|Luôn xuất hiện cùng nhau không thể tách rời.
găng|Đồ mang ở bàn tay để giữ ấm hoặc bảo vệ da.
gắng gượng|Cố gắng làm một việc khó khăn, vượt quá sức.
gắng sức|Dùng hết sức lực để làm việc.
gặp gỡ|Gặp nhau giữa những người quen biết.
gặp mặt|Tới cùng một nơi để trực tiếp chào hỏi hoặc trao đổi.
gặp nhau|Có mặt tại một chỗ và tiếp xúc với người kia.
gặp phải|Bất ngờ đối mặt với tình huống, thường là việc khó.
gặp thời|Được gặp lúc hoàn cảnh thuận lợi để làm việc tốt.
gắt gỏng|Dễ bực tức hoặc thường xuyên nổi giận.
gặt hái|Thu về hoa màu đã trồng hoặc kết quả nhờ công đã bỏ ra.
gầm cầu|Khoang không gian nằm dưới thân cầu để xe đi qua.
gấm vóc|Vải dệt từ tơ tằm hoặc các loại sợi quý, dùng làm quần áo hoặc trang trí.
gần đây|Xảy ra trong thời gian vừa qua hoặc ở nơi không xa.
gần gũi|Gần nhau về mặt tình cảm và tâm hồn.
gần như|Chỉ còn cách rất ít so với mức hoặc trạng thái nêu ra.
gần sát|Đến mức chạm vào nhau.
gần xa|Khu vực rộng lớn từ nơi ở đến nơi đi xa, khắp mọi nơi.
gấp bội|Tăng lên nhiều lần hơn mức bình thường.
gấp đôi|Nhân hai lần số lượng hoặc mức độ ban đầu để có kết quả mới.
gấp gáp|Cần làm ngay, không thể chậm trễ.
gấp khúc|Đường gồm nhiều đoạn thẳng nối tiếp nhau nhưng không nằm trên cùng một đường thẳng.
gấp rút|Phải đẩy nhanh công việc vì thời gian còn lại rất ít.
gấp rưỡi|Nhân số lượng hay mức độ lên một rưỡi lần.
gập ghềnh|Mặt đường lên xuống, lồi lõm khiến đi lại không êm.
gật đầu|Cúi đầu nhẹ để tỏ ý đồng ý hoặc chấp nhận.
gật gù|Gật đầu nhẹ lặp lại, như khi đồng tình hoặc nghe nhạc.
gấu chó|Loài gấu có mõm ngắn giống mõm chó.
gấu trúc|Thú lông trắng đen, thường ăn tre trúc.
gây dựng|Xây dựng nền tảng ban đầu cho một công việc hoặc sự nghiệp.
gầy còm|Mỏng da, xương lộ và thấp bé.
gầy gò|Mỏng, ít thịt, xương lộ ra ngoài.
ghé mắt|Nhìn lướt qua một cái gì đó bằng ánh mắt.
ghen|Khó chịu khi người mình yêu dành tình cảm cho người khác.
ghen ghét|Cảm thấy khó chịu, bực bội khi thấy người khác có được những điều mình muốn.
ghép|Nối các phần riêng để tạo thành một chỉnh thể.
ghế bành|Ghế ngồi rộng cho một người, có chỗ tựa lưng và gác tay.
ghế bố|Ghế dài có khung và mặt vải, thường gấp lại được.
ghế dài|Ghế có chỗ ngồi kéo dài cho nhiều người hoặc để nằm.
ghế đẩu|Đồ ngồi thấp, thường chỉ gồm mặt ghế và chân đỡ.
ghế ngồi|Đồ dùng để người ngồi nghỉ ngơi, làm việc hoặc tiếp khách.
ghế tựa|Ghế có phần dựng phía sau để đỡ lưng người ngồi.
ghềnh|Đoạn lòng sông nhiều đá làm dòng nước chảy gấp.
ghi âm|Ghi lại tiếng nói, nhạc hay âm thanh để có thể phát lại.
ghi bàn|Đưa bóng vào vị trí ghi điểm hợp lệ trong thi đấu.
ghi chép|Viết lại những gì nghe được hoặc đọc được.
ghi chú|Viết lại điều đã biết thành lời văn để lưu giữ.
ghi công|Viết tên người có công lao để ghi nhận.
ghi danh|Ký tên vào sổ hoặc điền đơn để tham gia tổ chức.
ghi hình|Thu lại hình ảnh động bằng máy quay hoặc thiết bị tương tự.
ghi nhận|Công nhận sự thật và lưu giữ lại trong trí nhớ.
ghi nhớ|Giữ thông tin trong trí để có thể nhắc lại hoặc thực hiện sau.
ghi tên|Viết tên vào danh sách để đăng ký.
ghim|Giữ giấy hoặc vải bằng vật nhỏ có đầu nhọn.
gia bảo|Đồ vật quý giá do ông bà cha mẹ để lại truyền cho con cháu.
gia cảnh|Tình trạng tài chính và hoàn cảnh sống của gia đình.
gia cầm|Những loài chim được nuôi trong nhà để lấy trứng hoặc thịt.
gia chính|Việc quản lý, lo liệu các công việc trong gia đình.
gia cố|Làm chắc thêm để công trình hay vật liệu chịu lực tốt hơn.
gia dụng|Dùng cho các nhu cầu sinh hoạt thường ngày trong gia đình.
gia đình|Nhóm người có quan hệ ruột thịt hoặc hôn nhân chung sống.
gia giảm|Thêm bớt phần nào để đạt mức vừa phải.
gia giáo|Việc dạy dỗ, rèn luyện nề nếp và phép tắc cho thành viên trong nhà.
gia hạn|Kéo dài thêm thời gian sử dụng của một hợp đồng hay giấy tờ.
gia nhập|Chính thức trở thành thành viên của một tổ chức hay nhóm.
gia phả|Sách ghi chép dòng họ, thế hệ và sự nghiệp của một gia đình.
gia phong|Những quy tắc, nề nếp và cách dạy dỗ riêng của một gia đình.
gia quyến|Tập hợp những người thân thuộc cùng chung một dòng họ.
gia sản|Tất cả tài sản chung của một gia đình.
gia súc|Những loài thú được nuôi để lấy sản phẩm hoặc sức kéo.
gia tài|Tất cả của cải vật chất và tinh thần mà ông cha để lại.
gia tăng|Làm cho số lượng hoặc mức độ trở nên nhiều hơn, lớn hơn.
gia thất|Cặp vợ chồng sống chung với nhau.
gia tiên|Những người đã khuất là tổ phụ và tổ mẫu của một gia đình.
gia tộc|Tập hợp họ hàng thân thuộc trong một dòng họ lớn.
gia truyền|Được truyền trong một gia đình qua nhiều thế hệ.
gia tư|Tài sản, đồ đạc riêng của một gia đình.
gia vị|Chất liệu được thêm vào món ăn để tăng hương vị thơm ngon.
già dặn|Đã trưởng thành đầy đủ về thể chất và kinh nghiệm.
già nua|Đã lớn tuổi và sức khỏe suy yếu.
giả bộ|Làm ra vẻ như có điều gì đó mà thực tế không phải vậy.
giả lập|Tạo ra mô hình hoặc hệ thống giả để hoạt động giống với đối tượng thật nhằm mục đích nghiên cứu hoặc thử nghiệm.
giả sử|Tạm coi một điều là đúng để xét điều gì sẽ xảy ra.
giả tạo|Không phải sự thật, được làm ra để giả vờ.
giả thuyết|Cách giải thích tạm được nêu ra để kiểm tra bằng chứng cứ.
giả tưởng|Không có thật, chỉ tồn tại trong trí tưởng tượng.
giả vờ|Làm giả hành động hoặc trạng thái để người khác tin là thật.
giá cả|Số tiền phải trả để mua hoặc sở hữu một món hàng hóa, dịch vụ.
giá lạnh|Rất lạnh, thường gợi cảm giác rét buốt ngoài trời.
giá thành|Chi phí sản xuất sản phẩm, bao gồm lương công nhân, nguyên liệu, nhiên liệu và khấu hao tài sản.
giá thể|Hỗn hợp vật liệu dùng làm nền để cây trồng phát triển.
giá thị trường|Giá cả trung bình trong ngày do thị trường quyết định.
giá trị|Độ tốt đẹp hoặc mức độ hữu ích của một vật đối với con người.
giá trị sử dụng|Công dụng của đồ vật giúp đáp ứng nhu cầu sản xuất hay sinh hoạt.
giá trị trao đổi|Số tiền hoặc lượng hàng nhận được khi đổi món này lấy món khác.
giá vốn|Tổng số tiền doanh nghiệp bỏ ra để mua nguyên liệu làm ra sản phẩm.
giác mạc|Lớp màng trong suốt ở trước mắt, giúp ánh sáng đi vào.
giác quan|Bộ phận cơ thể giúp nhận biết ánh sáng, âm thanh, mùi vị.
giai điệu|Tiếng nhạc vang lên nối tiếp nhau tạo thành bài hát.
giai đoạn|Khoảng thời gian riêng biệt trong một chuỗi sự kiện.
giai nhân|Người phụ nữ có vẻ đẹp.
giai thoại|Câu chuyện thú vị được truyền miệng, liên quan đến nhân vật có thật.
giải|Tìm ra cách làm hoặc đáp số của một bài toán.
giải đáp|Trả lời và làm rõ các thắc mắc hay câu hỏi.
giải khát|Uống nước để làm hết cảm giác khát.
giải lao|Dừng việc làm một lát để nghỉ ngơi, thư giãn cho khỏe người.
giải mã|Tìm ra ý nghĩa của những ký hiệu bí ẩn hoặc mã hóa.
giải ngân|Đưa tiền ra để chi trả hoặc thực hiện.
giải nghệ|Ngừng làm nghề, rời bỏ công việc đã theo đuổi.
giải nghĩa|Nói rõ ý nghĩa của một điều gì đó.
giải pháp|Phương cách xử lý để giải quyết vấn đề khó khăn.
giải quyết|Xử lý hết khó khăn để thành công.
giải thích|Nói để người khác hiểu rõ ý.
giải thưởng|Phần quà tặng dành cho người thắng cuộc thi.
giải trí|Hoạt động giúp thư giãn tinh thần.
giải trình|Nói rõ lý do hoặc trình bày sự việc để người khác hiểu.
giải trừ|Loại bỏ hoàn toàn, chấm dứt hẳn đi.
giải vây|Giải thoát khỏi tình trạng bị bao vây hoặc nguy hiểm.
giãi bày|Nói rõ nguyên nhân, lý do hoặc tâm tư của mình.
giảm giá|Hạ mức tiền bán hàng xuống thấp hơn so với lúc trước.
giảm nhẹ|Làm cho bớt nặng, giảm bớt mức độ khó khăn.
giảm thiểu|Giảm số lượng hoặc mức độ xuống thấp nhất có thể đạt được.
giảm thuế|Việc hạ bớt mức thuế phải nộp cho nhà nước.
giảm tốc|Làm chậm lại vận động của cơ thể hoặc vật thể.
giám đốc|Người đứng đầu quản lý một cơ quan, xí nghiệp hoặc công ty.
giám hiệu|Người đứng đầu quản lý trường.
giám hộ|Người trông nom, chăm sóc và bảo vệ một gia đình.
giám khảo|Người đứng ra chấm điểm, quyết định kết quả cuộc thi.
giám sát|Theo dõi tiến trình để biết công việc có đúng yêu cầu không.
giám thị|Người trông coi để kỳ thi diễn ra đúng quy định.
gian hàng|Khoảng bày sản phẩm riêng của một người bán hoặc đơn vị.
gian khó|Những lúc gặp trở ngại lớn, thiếu thốn và vất vả.
gian lao|Khó khăn, vất vả, cực nhọc.
gian nan|Tình trạng khó khăn, vất vả, thiếu thốn và gian khổ.
giàn|Khung có cọc chống để cây leo bám vào.
giàn giáo|Hệ thống cột, ván dựng tạm để thợ xây leo lên cao.
giản dị|Mộc mạc, không cầu kỳ trong cách sống hoặc thể hiện.
giản đơn|Đơn giản, không phức tạp hay rườm rà.
giản lược|Viết hoặc nói ngắn gọn, bỏ bớt chi tiết không cần thiết.
giản thể|Làm cho việc gì đó trở nên đơn giản hơn, bớt phức tạp đi.
gián đoạn|Đứt quãng, không nối tiếp nhau.
gián tiếp|Xảy ra qua trung gian, không trực tiếp.
giảng dạy|Truyền đạt kiến thức cho người khác.
giảng đường|Phòng lớn nơi giảng viên đứng dạy học sinh.
giảng giải|Nói rõ ý nghĩa để người khác hiểu hết vấn đề.
giảng viên|Người giảng dạy ở đại học hoặc cơ sở đào tạo tương tự.
giao|Đưa cho người khác nhận và chịu trách nhiệm.
giao ban|Họp họp để tóm tắt việc vừa làm và định hướng việc sau.
giao bóng|Động tác bắt đầu trận đấu bằng cách đá bóng.
giao ca|Bàn giao nhiệm vụ cho người hoặc ca làm tiếp theo.
giao dịch|Gặp gỡ để trao đổi công việc hoặc mua bán hàng hóa.
giao diện|Mặt tiếp xúc giữa một thiết bị, phần mềm với người dùng hoặc môi trường bên ngoài.
giao du|Gần gũi, qua lại thường xuyên với người khác.
giao điểm|Điểm chung nơi hai hay nhiều đường thẳng gặp nhau.
giao hảo|Có mối quan hệ thân thiện, hòa thuận với nhau.
giao hưởng|Hình thức biểu diễn âm nhạc kết hợp nhiều loại nhạc khí tạo nên tiếng vang lớn.
giao hữu|Tỏ lòng thân thiện, muốn kết bạn với nhau.
giao kèo|Thỏa thuận bằng lời hoặc văn bản giữa hai bên về quyền lợi và nghĩa vụ.
giao kết|Thiết lập quan hệ thân thiết hoặc liên minh với người khác.
giao khoán|Truyền lại trách nhiệm làm việc cho người khác để họ tự lo.
giao lộ|Nơi hai hoặc nhiều con đường gặp nhau trên mặt đất.
giao lưu|Sự trao đổi qua lại giữa hai bên về hàng hóa hay tư tưởng.
giao nhận|Nhận và trao đổi tài sản, hàng hóa giữa hai bên.
giao phó|Giao một việc gì đó cho người khác để họ trông nom và thực hiện thay mình.
giao tế|Giao tiếp, liên hệ hoặc tiếp đón khách.
giao thiệp|Giao tiếp, làm việc chung hoặc kết thân với người khác.
giao thoa|Hiện tượng hai sóng gặp nhau làm tăng hoặc giảm độ mạnh.
giao thông|Việc người và phương tiện đi lại trên các tuyến đường.
giao thừa|Giờ phút cuối cùng của năm cũ, đánh dấu sự chuyển sang năm mới.
giao thương|Hành động mua bán hàng hóa với nhau.
giao tiếp|Hành động trao đổi thông tin, chia sẻ ý nghĩ giữa các người.
giao ước|Điều kiện hai bên cùng hứa với nhau.
giáo án|Bản ghi chi tiết nội dung bài giảng của thầy cô.
giáo cụ|Vật mẫu hay dụng cụ người dạy dùng để minh họa bài học.
giáo dục|Dạy dỗ để người ta có kiến thức và đạo đức.
giáo dục học|Lĩnh vực nghiên cứu quy luật, phương pháp và tổ chức dạy học.
giáo dục phổ thông|Hệ thống dạy kiến thức cơ bản cho học sinh từ cấp nhỏ đến cấp lớn.
giáo huấn|Lời chỉ bảo, dạy dỗ từ người lớn tuổi.
giáo khoa|Sách dùng để dạy học hoặc quan điểm coi là chân lý.
giáo sư|Học hàm cao cấp nhất dành cho giảng viên dạy tại trường đại học.
giáo viên|Người đảm nhận công việc truyền đạt kiến thức cho học trò.
giáo vụ|Bộ phận phụ trách công tác giảng dạy và học tập tại trường.
giáp mặt|Gặp nhau trực tiếp hoặc đứng trước mặt nhau.
giàu|Có của cải vượt xa mức cần cho sinh hoạt.
giàu có|Có nhiều tiền bạc và của cải hơn người thường.
giàu sang|Có nhiều tiền của và sống xa xỉ.
giàu sụ|Có nhiều tiền bạc và của cải.
giãy giụa|Cố gắng vùng vẫy, chống chọi liên tục và mạnh mẽ.
giăng giăng|Trải rộng ra khắp nơi hoặc nối tiếp nhau thành từng hàng dài.
giăng kín|Dùng vật liệu bao bọc kín xung quanh một vật khác.
giặt|Làm sạch quần áo bằng nước và vò hoặc quay máy.
giặt giũ|Làm sạch quần áo và đồ dùng bằng nước.
giặt ủi|Làm sạch quần áo và dùng bàn là để làm phẳng vải.
giấc|Một lượt ngủ từ lúc thiếp đi đến khi tỉnh dậy.
giấc mộng|Trạng thái ngủ có hình ảnh mơ thấy.
giấc ngủ|Khoảng thời gian nghỉ ngơi để cơ thể được thư giãn.
giấc nồng|Trạng thái ngủ sâu, khó đánh thức.
giấm|Chất lỏng vị chua do lên men, dùng nêm thức ăn.
giậm chân|Nện mạnh bàn chân xuống đất, thường để bày tỏ sự tiếc nuối.
giật dây|Sai khiến người khác làm việc mà không nói rõ ra.
giấu kín|Ẩn giấu đi một cách kín đáo, không ai hay biết.
giây lát|Khoảng thời gian rất ngắn, thoáng qua trong tích tắc.
giây phút|Khoảng thời gian ngắn gắn với một sự việc cụ thể.
giấy|Vật liệu dạng tờ mỏng để viết, in hay gói đồ.
giấy ăn|Giấy mỏng, mềm, thấm nước nhanh, dùng lau miệng hoặc tay sau khi ăn.
giấy bạc|Tiền giấy dùng để mua bán hàng hóa trong đời sống hàng ngày.
giấy bản|Giấy thủ công mỏng và xốp, thường làm từ vỏ cây.
giấy bồi|Giấy ghép từ nhiều lớp cho dày và cứng.
giấy can|Giấy mỏng trong suốt dùng để vẽ hoặc sao chép.
giấy chứng minh|Tài liệu do cơ quan nhà nước cấp để xác nhận thông tin cá nhân như tên, tuổi, nơi sinh và nguồn gốc.
giấy chứng nhận|Văn bản xác nhận một sự việc, tư cách hoặc kết quả.
giấy dán tường|Vật liệu dạng giấy có hoa văn trang trí dùng để dán lên bề mặt tường nhà.
giấy dó|Giấy truyền thống làm từ vỏ cây dó, thường dùng in tranh.
giấy in|Giấy dùng để in chữ, hình cho sách báo.
giấy khen|Giấy ghi lời khen thưởng cho thành tích tốt.
giấy lọc|Lớp vật liệu xốp, giữ lại tạp chất khi lọc nước hoặc chất lỏng.
giấy nháp|Giấy dùng để ghi thử, tính thử hoặc phác ý.
giấy nhún|Giấy mềm, dai, không thấm nước, dùng để tạo hình hoa giả.
giấy phép|Giấy tờ chính thức cho phép được làm một việc cụ thể.
giấy thấm|Giấy xốp, dày, dùng để hút mực thừa sau khi viết.
giấy thông hành|Giấy chứng nhận cho phép người được cấp đi qua biên giới hoặc vùng kiểm soát.
giấy tờ|Các loại giấy viết, hợp đồng và hồ sơ dùng cho việc công.
giấy trắng mực đen|Văn bản viết rõ ràng, không thể chối cãi hay thay đổi.
giấy vệ sinh|Giấy mỏng, mềm, dùng để lau dọn sau khi đi vệ sinh.
gieo|Rải hạt vào đất để cây mới mọc lên.
gieo cấy|Trồng lúa bằng cách gieo hạt và cấy mạ để tạo ra lương thực.
gieo trồng|Hạt giống xuống đất và chăm sóc cây để phát triển.
gieo vần|Chọn âm cuối của từ để tạo nhịp điệu cho bài thơ.
giếng|Hố đào hoặc khoan xuống đất để lấy nước.
giếng dầu|Nơi khoan sâu để lấy dầu mỏ ra khỏi lòng đất.
giếng khoan|Giếng đào sâu xuống mạch nước ngầm bằng máy khoan.
giếng khơi|Hố sâu đào xuống đất để chứa nước uống cho người và súc vật.
giếng trời|Khoang hở giữa các tầng nhà để ánh sáng tự nhiên chiếu xuống.
gìn giữ|Chăm sóc cẩn thận để bảo vệ vật gì đó khỏi bị mất mát hoặc hư hỏng.
giò chả|Tên gọi chung cho các món ăn làm từ thịt lợn xay hoặc băm nhỏ.
giò lụa|Giò làm từ thịt lợn nạc giã nhỏ, cuốn trong lụa.
giò thủ|Món giò làm từ phần đầu lợn thái miếng, xào rồi ép chặt.
gió đông|Luồng khí thổi từ hướng mặt trời mọc về.
gió heo may|Loại gió mát mẻ, khô ráo thường xuất hiện vào cuối mùa thu.
gió lốc|Luồng gió thổi rất mạnh và xoay tròn.
gió mùa|Loại gió thổi theo mùa với hướng và tính chất thay đổi theo mùa.
gió nồm|Gió ẩm thổi từ hướng đông nam, thường xuất hiện vào mùa hè.
giỏi|Có khả năng làm việc gì ở mức cao.
giòn|Dễ vỡ, gãy hoặc phát tiếng rốp khi cắn.
giòn tan|Dễ vỡ, giòn rất nhiều.
giọng|Âm sắc riêng có thể nhận ra khi ai đó nói hoặc hát.
giọng điệu|Cách phát âm hoặc lối nói thể hiện thái độ, cảm xúc cụ thể.
giọt|Khối chất lỏng nhỏ tách ra, thường rơi từng hạt.
giọt sương|Nước mưa đọng lại trên lá cây rồi rơi xuống từng giọt nhỏ.
giông giống|Có sự tương đồng ở một vài điểm nhưng không giống hoàn toàn.
giống hệt|Giống y hệt nhau, không có điểm nào khác biệt dù chỉ một chút.
giống nòi|Toàn bộ người cùng dòng máu hoặc cùng dân tộc.
giờ đây|Ngay ở thời điểm hiện tại, thường so với thời trước.
giờ địa phương|Thời gian tính theo múi giờ tại một địa điểm cụ thể.
giờ giấc|Thời điểm và khung giờ cụ thể được quy định hoặc sắp xếp.
giờ phút|Khoảng thời gian ngắn tính bằng giờ và phút chứa đựng sự việc quan trọng.
giới chức|Người nắm giữ chức vụ quan trọng trong ngành.
giới hạn|Độ rộng hay số lượng tối đa không được phép vượt qua.
giới thiệu|Làm cho người lạ biết tên và việc làm của nhau.
giới tính|Đặc điểm sinh học dùng để phân biệt giữa nam và nữ, đực và cái.
giới trẻ|Những người đang ở lứa tuổi thanh niên nói chung.
giục|Thúc người khác làm ngay hoặc làm nhanh hơn.
giục giã|Khuyên răn, thúc giục người khác làm việc gì đó.
giun|Động vật thân dài mềm, không chân, thường gặp trong đất.
giun đất|Loài động vật thân dài, mềm, sống chui rúc trong đất và phân hủy chất hữu cơ.
giúp|Góp công hoặc đưa phương tiện cho người khác làm việc.
giúp đỡ|Làm việc chung tay để hỗ trợ người khác hoàn thành việc.
giúp sức|Cung cấp thêm sức lực, tiền bạc hoặc sự hỗ trợ cho việc làm.
giúp việc|Làm những công việc hỗ trợ, thường là việc nhà cho người thuê.
giữ chân|Giữ lại người hoặc vật, không để họ hoặc nó rời đi.
giữ gìn|Bảo vệ để không bị hư hỏng hoặc mất mát.
giữ lại|Không cho vật gì rời khỏi tay hoặc nơi đang có.
giữ lời|Thực hiện đúng những gì đã hứa trước.
giữ miệng|Kiểm soát lời nói để không gây tổn hại.
giữ mình|Chú ý bảo vệ bản thân khỏi bị tổn thương hoặc gặp nguy hiểm.
giữ nguyên|Giữ cho vật gì đó không thay đổi hình dáng hay tính chất.
giữ vững|Giữ nguyên trạng thái, không để bị thay đổi hay lung lay.
giữa|Vị trí cách hai phía hoặc hai đầu một khoảng tương đương.
giữa chừng|Thời điểm đang thực hiện hoặc xảy ra việc chưa xong.
giường|Đồ có mặt rộng kê cao để nằm ngủ.
giường nằm|Nệm hoặc chỗ nằm dành riêng cho hành khách trên phương tiện giao thông.
gò bó|Buộc vào khuôn khổ hẹp, khó tự do.
gò đống|Núi đất nhỏ hoặc đống đất cao lên.
gò má|Phần xương và thịt nhô lên ở hai bên mặt dưới mắt.
gõ cửa|Gõ lên cánh cửa để báo rằng có người muốn vào.
góc cạnh|Các cạnh và góc rõ tạo nên dáng sắc nét của vật.
góc độ|Vị trí đứng để quan sát sự vật theo một hướng nhất định.
góc học tập|Chỗ đặt bàn ghế riêng để ngồi học bài trong nhà.
góc nhọn|Góc tạo thành nhỏ hơn góc vuông chín mươi độ.
góc vuông|Giao điểm tạo thành hai đường thẳng đứng nhau.
gói ghém|Gói lại đồ vật để gọn gàng, ngăn nắp.
gói thầu|Phần công việc được chia để đấu thầu.
gọi là|Dùng một tên hoặc cách diễn đạt để chỉ sự vật đang nói.
gom góp|Tập hợp lại những thứ đã có để dùng sau.
gọn gàng|Được sắp đặt ngay ngắn, không rườm rà hay bừa bộn.
gọn ghẽ|Sắp xếp ngăn nắp, gọn gàng, dễ nhìn.
gọn nhẹ|Nhỏ gọn, nhẹ nhàng, chỉ bao gồm những gì cần thiết nhất.
gọng|Khung cứng giữ mắt kính hay đỡ một vật khác.
góp mặt|Tham gia vào hoạt động chung của tập thể.
góp nhặt|Thu thập từng chút một từ nhiều nơi để làm thành một khối.
góp phần|Đóng góp một phần nhỏ vào công việc chung.
góp sức|Đóng góp công sức của bản thân vào công việc chung.
góp vốn|Đóng tiền vào dự án chung cùng nhiều người khác để làm ăn.
góp ý|Đưa ra ý kiến để người khác tham khảo nhằm hoàn thiện hơn.
gót chân|Phần sau của bàn chân chạm đất khi đứng.
gồ ghề|Bề mặt không bằng phẳng, có nhiều chỗ lồi lên hoặc lõm xuống.
gỗ ván|Gỗ đã được cưa thành những tấm phẳng để làm đồ.
gỗ xẻ|Tấm hoặc khúc gỗ đã được tách ra từ thân cây theo chiều dọc.
gốc cây|Phần thấp nhất của thân, ở chỗ tiếp giáp với rễ.
gốc rễ|Phần đầu tiên, nguyên nhân khởi đầu tạo nên sự vật hoặc hiện tượng.
gốc tích|Nơi bắt đầu của một người, một sự vật hay một dòng họ.
gối đầu|Đặt đầu lên một vật đỡ để nghỉ hoặc nằm ngủ.
gột rửa|Làm cho sạch hết mọi vết bẩn.
gỡ gạc|Làm lại để lấy lại những gì đã mất.
gỡ lỗi|Tìm và sửa những chỗ sai trong chương trình máy tính.
gợi hình|Sử dụng lời nói để tạo ra hình ảnh cụ thể trong tâm trí người nghe.
gợi mở|Làm nảy sinh suy nghĩ hay ý tưởng mới.
gợi ý|Đưa ra ý kiến để người khác cân nhắc và tự quyết.
guốc|Đồ mang ở chân có đế cứng và quai để xỏ chân.
gửi gắm|Giao phó một cách tin tưởng và thiết tha cho người thân hoặc đối tượng đáng tin cậy.
gừng|Cây cho củ thơm cay dùng làm gia vị.
gương|Mặt nhẵn phản chiếu cho ta thấy hình của mình.
gương mặt|Dáng vẻ, nét mặt biểu lộ tâm trạng.
gương mẫu|Làm mẫu mực để người khác noi theo.
gượng ép|Làm việc không thoải mái vì cố gắng vượt qua khó khăn thiếu điều kiện.
ha ha|Tiếng cười lớn, vang rõ và lặp lại liên tục thể hiện sự vui vẻ.
hà mã|Thú lớn da dày, miệng rộng, phần lớn ban ngày ở dưới nước.
hà tất|Chẳng cần phải làm, không có lý do gì để làm.
hả hê|Hài lòng vì việc đã xong.
há hốc|Mở miệng ra rất rộng.
hạ cánh|Rời trạng thái đang bay và tiếp đất an toàn, như máy bay xuống sân.
hạ cấp|Bậc thấp hơn, hạng dưới trong phân cấp chức vụ.
hạ du|Vùng ở phía cuối lưu vực sông, gần nơi nước đổ ra.
hạ giá|Giảm tiền bán hàng hoặc làm giảm giá trị của một thứ.
hạ gục|Làm cho đối thủ thua cuộc và không thể đứng dậy tiếp tục.
hạ lệnh|Truyền ý muốn xuống cho cấp dưới phải làm.
hạ lưu|Phần sông phía dưới, gần nơi nước đổ ra biển hoặc hồ lớn.
hạ mình|Tự đặt mình ở vị thế khiêm nhường hơn khi ứng xử.
hạ nguồn|Đoạn cuối của con sông, nơi nước chảy ra biển.
hạ tầng|Các công trình nền tảng như đường, điện, nước phục vụ hoạt động chung.
hạ thế|Điện áp có mức độ thấp, an toàn cho sinh hoạt hàng ngày.
hai mươi|Số lượng gồm hai nhóm, mỗi nhóm có mười đơn vị.
hài hước|Nói chuyện vui nhộn nhằm mục đích làm người nghe cười.
hài kịch|Kịch dùng tiếng cười để phê phán thói xấu trong đời.
hài lòng|Vui vẻ và chấp nhận hoàn cảnh hiện tại.
hải âu|Chim lớn sống ở biển, có cánh dài, mỏ quặm và chân ngắn.
hải cẩu|Thú biển có chi dạng vây, vừa bơi vừa có thể lên bờ nghỉ.
hải dương|Nước mặn bao phủ diện tích rộng lớn trên bề mặt Trái Đất.
hải đảo|Những phần đất nổi nằm ngoài khơi biển.
hải đăng|Đèn lớn đặt trên bờ biển hoặc đảo để soi sáng đường cho tàu thuyền.
hải đồ|Bản đồ vùng biển dùng cho người đi tàu xác định đường đi.
hải ngoại|Nơi ở bên ngoài lãnh thổ nước mình.
hải quan|Việc kiểm tra và thu thuế cho hàng hóa qua biên giới.
hải sản|Thực phẩm lấy từ biển như tôm, cá, mực dùng để ăn.
hải sâm|Động vật sống dưới biển, thân dài mềm, dùng làm món ăn ngon.
ham mê|Yêu thích đến mức say mê, không thể rời bỏ.
ham muốn|Cảm giác muốn điều gì đó một cách mạnh mẽ.
hàm lượng|Số lượng chất cụ thể có mặt bên trong một hỗn hợp hoặc vật chất.
hàm số|Quy tắc gán mỗi giá trị đầu vào với đúng một giá trị đầu ra.
hàm súc|Viết ngắn gọn nhưng chứa đựng nhiều ý nghĩa sâu sắc.
hàm ý|Ý nghĩa ngầm ẩn, không nói ra nhưng hiểu được.
hàn huyên|Trò chuyện thân mật, tâm tình với nhau sau khi xa nhau.
hàn lâm|Viện nghiên cứu khoa học hoặc lối văn trừu tượng, khó hiểu.
hãn hữu|Ít khi xảy ra, rất hiếm gặp.
hạn chế|Giữ lại, ngăn không cho vượt qua một giới hạn nhất định.
hạn hán|Thời tiết khô hạn kéo dài, thiếu nước mưa cho cây trồng và sinh hoạt.
hạn hẹp|Có số lượng ít, phạm vi nhỏ, không rộng rãi.
hạn mức|Giới hạn tối đa được phép đạt đến hoặc sử dụng.
hạn ngạch|Số lượng hoặc trị giá hàng hóa được nhà nước cho phép nhập hoặc xuất trong một thời gian.
hạn sử dụng|Mốc thời gian cuối cùng được phép dùng một vật.
hang|Khoang rỗng tự nhiên ăn sâu vào lòng núi hay đất.
hang động|Khoang rỗng ăn sâu vào núi đá hoặc lòng đất.
hàng đầu|Đứng ở vị trí số một, xuất sắc hơn tất cả những người khác.
hàng giậu|Bờ rào ngăn cách hai bên đường hoặc khu đất.
hàng hải|Kĩ thuật liên quan đến tàu thuyền và biển cả.
hàng không|Lĩnh vực vận chuyển bằng máy bay và các hoạt động liên quan.
hàng không vũ trụ|Khoa học và kỹ thuật nghiên cứu về việc bay trong không gian vũ trụ.
hàng loạt|Nhiều sự vật hay việc xảy ra nối nhau hoặc cùng đợt.
hàng ngũ|Tập hợp người được xếp thành hàng lối chỉnh tề.
hàng quán|Các cửa hàng bán đồ ăn và vật dụng nhỏ ven đường.
hàng rào|Dãy vật chắn bao quanh nhà hoặc khu vườn để ngăn cách.
hàng rong|Hàng hóa được bán bằng cách đi lang thang trên đường phố.
hàng tiêu dùng|Sản phẩm dùng cho sinh hoạt hàng ngày của mọi người.
hàng xóm|Người sống gần nhà mình trong cùng khu dân cư.
hanh thông|Việc làm suôn sẻ, không gặp trở ngại.
hành động|Việc làm cụ thể thay vì chỉ suy nghĩ hay nói.
hành hoa|Hành lấy phần lá và thân non để nêm món ăn.
hành khách|Người mua vé và di chuyển trên phương tiện giao thông công cộng.
hành khúc|Bài nhạc có nhịp điệu đều đặn để đi thành hàng.
hành lang|Lối đi dài trong công trình, nối cửa các phòng hoặc các khu.
hành nghề|Làm việc chuyên môn để kiếm sống theo nghề đã chọn.
hành phi|Hành thái nhỏ, rang cho đến khi vàng giòn, thơm và hơi cháy.
hành sự|Làm những việc đã được lên kế hoạch hoặc suy tính kỹ.
hành tây|Loại hành có củ to tròn, gồm nhiều lớp thịt giòn mọng.
hành tinh|Thiên thể lớn quay quanh một ngôi sao, như Trái Đất.
hành trang|Đồ vật và giấy tờ cần thiết mang theo khi đi xa.
hành tung|Dấu tích để lại từ những việc làm và di chuyển của một người.
hành văn|Cách thức sắp xếp câu và lựa chọn từ ngữ khi viết.
hành vi|Cách một người xử sự được thể hiện qua việc làm cụ thể.
hãnh diện|Hài lòng về thành tích của mình và thể hiện sự tự hào đó.
hạnh kiểm|Đạo đức và cách cư xử của một người được thể hiện qua hành động hàng ngày.
hạnh nhân|Loại cây có quả cứng, bên trong là nhân ăn được, thường dùng làm món ăn vặt.
hạnh phúc|Trạng thái sung sướng, vui vẻ và đầy đủ.
hao hụt|Giảm bớt về số lượng so với mức lúc đầu.
hao mòn|Suy yếu dần đi vì dùng nhiều hoặc thời gian dài.
hào hứng|Cảm thấy vui vẻ và nhiệt tình cao độ đối với điều gì đó.
hào nhoáng|Đẹp bề ngoài nhưng phô trương, lộng lẫy.
hào phóng|Sẵn sàng chi tiền nhiều để đối xử tốt với người.
hào quang|Ánh sáng rực rỡ tỏa ra xung quanh người hoặc vật.
hảo cảm|Cảm thấy thích và thiện chí với ai đó.
hảo tâm|Lòng tốt, sự thiện tâm muốn giúp đỡ người khác.
hát hò|Hát ca, biểu diễn âm nhạc bằng giọng nói.
hát ru|Bài hát nhẹ nhàng dùng để ru trẻ nhỏ vào giấc ngủ.
hạt dẻ|Hạt có vỏ nâu cứng, phần trong bùi, thường ăn sau khi rang.
hạt giống|Hạt được giữ hoặc chọn để gieo thành cây mới.
hạt mưa|Một giọt nước mưa riêng lẻ đang rơi.
hạt nhân|Phần giữa của nguyên tử chứa proton và neutron.
hạt tiêu|Hạt gia vị thơm cay thu từ cây hồ tiêu.
hay chữ|Có tài năng về văn học và ngôn ngữ.
hay ho|Hay, thú vị hoặc đáng chú ý.
hay làm|Thực hiện hành động đó thường xuyên, nhiều lần.
hãy còn|Vẫn còn tiếp tục tồn tại hoặc chưa kết thúc hoàn toàn.
hăm hở|Tinh thần hăng hái, nhiệt tình và sẵn sàng hành động ngay lập tức.
hẳn hoi|Xác nhận sự việc là đúng thật, rõ ràng không nghi ngờ.
hăng say|Làm việc với tinh thần nhiệt huyết và sự say mê cao độ.
hằng số|Con số giữ nguyên giá trị không thay đổi trong một quy trình.
hắng giọng|Phát âm thanh ngắn từ cổ họng để làm rõ giọng hoặc báo hiệu.
hắt hơi|Bật mạnh hơi ra ngoài mũi kèm tiếng kêu.
hâm mộ|Yêu thích và kính trọng người hay việc nào đó.
hâm nóng|Làm cho cái nguội trở lại nóng hoặc kích hoạt lại.
hầm chui|Đường hầm nằm dưới lòng đất để xe hoặc người đi qua.
hầm tàu|Khoang kín nằm bên dưới boong, thường dùng chứa hàng.
hân hạnh|Vui mừng, thấy may mắn khi được gặp gỡ hay làm việc với người khác.
hân hoan|Cảm thấy vui mừng rất nhiều.
hấp dẫn|Có sức thu hút khiến người khác muốn xem hoặc tham gia.
hấp tấp|Làm việc vội vàng, không suy nghĩ kỹ.
hấp thụ|Thu vào bên trong các chất từ môi trường xung quanh.
hầu chuyện|Nói chuyện với người lớn tuổi hoặc cấp trên một cách tôn trọng.
hầu gái|Cô gái làm công việc phục vụ trong gia đình hoặc khách sạn.
hầu hết|Phần lớn số lượng hoặc phần lớn trường hợp.
hậu bị|Duy trì nguồn lực sẵn sàng dùng khi cần sau này.
hậu duệ|Những người con cháu sinh ra sau nhiều đời trong cùng một dòng họ.
hậu quả|Kết quả xấu xảy ra sau một sự việc.
hậu thế|Những người hoặc đời sống của các thế hệ sau này.
hậu thuẫn|Lực lượng đứng sau để hỗ trợ, giúp đỡ hoặc làm chỗ dựa.
hậu trường|Nơi diễn ra hoạt động sau khi khán giả không thấy.
hậu vận|Số phận xảy ra ở phần sau của cuộc đời.
hậu vệ|Cầu thủ chủ yếu bảo vệ phần sân nhà trong bóng đá.
hé mở|Mở ra một chút để thấy bên trong.
hẻo lánh|Nằm ở vùng xa xôi, ít người đến và khó khăn trong việc đi lại.
héo úa|Trở nên vàng úa, khô cứng do thiếu nước hoặc già cỗi.
hẹp hòi|Chỉ người chỉ biết nghĩ đến lợi ích riêng của mình.
hệ điều hành|Phần mềm quản lý thiết bị điện tử và điều khiển hoạt động.
hệ quả|Kết quả xảy ra do một sự việc trước đó gây nên.
hệ sinh thái|Sinh vật trong một vùng cùng môi trường và các quan hệ giữa chúng.
hệ số|Con số làm nhân tử hoặc cho biết mức tác động trong một phép tính.
hệ thống|Những bộ phận liên kết và cùng hoạt động theo một cách nhất định.
hệ trọng|Có vai trò và tác động rất lớn, rất quan trọng.
hệ tuần hoàn|Hệ thống cơ quan vận chuyển máu đi khắp cơ thể sinh vật.
hếch|Hướng đầu hoặc mép vật hơi ngửa lên.
hết cả|Chỉ toàn bộ, không còn sót lại gì khác.
hết lòng|Sử dụng toàn bộ tâm huyết và sức lực cho một việc.
hết lời|Nói hết mọi điều để thuyết phục.
hết mực|Ở mức rất cao, như khi nói về sự kính trọng hoặc tận tình.
hết sức|Làm việc với toàn bộ sức lực và tinh thần tối đa.
hết thảy|Tất cả mọi người và mọi vật.
hết ý|Đạt đến mức độ hoàn hảo nhất, không còn gì để chê trách.
hì hục|Làm việc chăm chỉ, vất vả không ngơi.
hí hoáy|Làm việc chăm chỉ, nhanh tay nhanh mắt.
hiếm|Ít xuất hiện hoặc khó tìm được.
hiếm có|Ít xuất hiện hoặc số lượng rất nhỏ.
hiếm hoi|Có rất ít, không thường gặp hoặc không dễ có được.
hiên|Khoảng có mái che ngay trước cửa nhà.
hiên ngang|Tự tin, đường hoàng, không chịu khuất phục.
hiền hậu|Thân thiện, tốt bụng và dễ gần người khác.
hiền lành|Tính tình tốt bụng, dịu dàng, không làm tổn thương ai.
hiền lương|Tính tình tốt bụng và làm việc lương thiện.
hiển nhiên|Rõ ràng, ai cũng thấy và không thể phủ nhận được.
hiển vi|Dụng cụ dùng kính để nhìn thấy vật thể rất nhỏ.
hiến kế|Đề xuất phương án hay để giúp người trên giải quyết việc lớn.
hiện diện|Xuất hiện ở nơi nào đó.
hiện đại|Thuộc về thời nay, dùng công nghệ và cách làm mới nhất.
hiện hành|Đang được áp dụng và thi hành trong thực tế.
hiện hữu|Đang tồn tại và có mặt trong thực tế.
hiện kim|Tiền tệ vật thể đang lưu hành, gồm giấy và kim loại.
hiện nay|Thời điểm đang xảy ra chuyện lúc này.
hiện tại|Khoảng thời gian đang diễn ra ngay lúc này, chưa đến tương lai.
hiện thế|Thời điểm đang sống, cuộc đời hiện tại.
hiện thực|Những gì có thật, tồn tại trong cuộc sống thực tế.
hiện trạng|Tình hình, trạng thái của sự vật tại thời điểm hiện tại.
hiện tượng|Điều có thể quan sát thấy trong tự nhiên hoặc đời sống.
hiện vật|Vật có thật được lưu giữ hoặc trưng bày làm bằng chứng, tư liệu.
hiệp đồng|Hợp sức cùng nhau làm việc chung theo một mục đích.
hiệp hội|Tổ chức của những cá nhân hay đơn vị có chung mối quan tâm.
hiệp phụ|Thời gian thêm vào sau trận đấu chính thức để quyết định thắng thua.
hiệp vần|Sắp xếp âm cuối của các câu thơ giống nhau.
hiểu|Nắm được ý nghĩa hay cách vận hành của điều gì.
hiểu biết|Biết rõ và đầy đủ về sự vật, sự việc.
hiểu lầm|Nắm sai ý hoặc đánh giá sai vì thiếu thông tin.
hiếu động|Thích chạy nhảy, hoạt động nhiều và không chịu yên lặng.
hiếu học|Thích học hỏi và chịu khó học tập.
hiếu khách|Thái độ thân thiện, vui vẻ đón tiếp người đến nhà.
hiếu thảo|Biết ơn và tôn trọng sâu sắc cha mẹ.
hiếu thuận|Kính trọng và chăm sóc chu đáo đối với cha mẹ.
hiệu bộ|Văn phòng hoặc phòng làm việc của ban giám hiệu nhà trường.
hiệu chỉnh|Điều chỉnh lại thiết bị để sửa lỗi và đạt độ chính xác cao nhất.
hiệu lệnh|Tín hiệu quy định trước để mọi người cùng thực hiện một động tác.
hiệu lực|Lực lượng sinh ra kết quả mong muốn.
hiệu năng|Khả năng hoàn thành công việc của thiết bị hay hệ thống trong điều kiện nhất định.
hiệu phó|Người phụ trách việc quản lý nhà trường thay cho hiệu trưởng.
hiệu quả|Mức độ một việc đem lại kết quả mong muốn.
hiệu số|Kết quả khi lấy số này trừ đi số kia.
hiệu suất|Kết quả làm việc đạt được trong một khoảng thời gian.
hiệu trưởng|Người đứng đầu và phụ trách điều hành một trường học.
hiệu ứng|Kết quả hoặc sự thay đổi xảy ra khi có tác động từ bên ngoài.
hiệu ứng nhà kính|Hiện tượng khí quyển giữ nhiệt khiến Trái Đất nóng dần lên.
hình|Đường nét hoặc ảnh cho thấy dáng vẻ của một vật.
hình ảnh|Hình dạng, bóng dáng của người, vật hoặc cảnh tượng được ghi lại bằng máy móc hoặc lưu giữ trong trí nhớ.
hình bầu dục|Hình dáng giống quả trứng gà, tròn ở hai đầu và phình ra ở giữa.
hình bình hành|Hình bốn cạnh mà từng đôi cạnh đối diện chạy song song.
hình cầu|Hình khối không gian tròn đều, mọi điểm trên bề mặt cách tâm một khoảng bằng nhau.
hình chữ nhật|Hình gồm bốn cạnh và bốn góc đều vuông góc với nhau.
hình dạng|Bề ngoài của vật để phân biệt với vật khác.
hình dung|Tưởng tượng ra hình ảnh, sự việc trong đầu.
hình học|Nghiên cứu hình dạng, kích thước và vị trí của các vật thể trong không gian.
hình lập phương|Hình khối có sáu mặt phẳng bằng nhau, mỗi mặt là hình vuông.
hình nền|Hình ảnh được đặt làm nền cho màn hình máy tính.
hình như|Dường như vậy, nhưng chưa chắc chắn hoàn toàn.
hình thái|Hình dáng bên ngoài có thể thấy được của sự vật.
hình thang|Hình có bốn cạnh với hai cạnh đối diện song song với nhau.
hình thành|Dần xuất hiện và có những đặc điểm nhận biết được.
hình thể|Hình dáng và cấu trúc bên ngoài của một vật hoặc người.
hình thoi|Hình bốn cạnh bằng nhau, hai cặp cạnh đối diện song song với nhau.
hình thức|Cách một sự vật hiện ra bên ngoài hoặc được trình bày.
hình tròn|Hình dạng phẳng có các điểm cách tâm một khoảng bằng nhau.
hình trụ|Khối hình có hai đáy tròn bằng nhau và mặt bên nối hai đáy.
hình tượng|Hình ảnh mang ý nghĩa khái quát trong văn học hoặc nghệ thuật.
hình vuông|Hình có bốn cạnh bằng nhau và bốn góc vuông.
hiu hắt|Không khí lạnh lẽo, vắng vẻ và buồn tẻ.
hò reo|Cùng nhau hét lớn tiếng để thể hiện sự vui mừng hoặc cổ vũ.
họ hàng|Những người cùng dòng máu, có quan hệ với nhau.
họ mạc|Những người cùng dòng họ hoặc họ hàng.
hoa đại|Loài cây có hoa lớn, màu trắng hoặc hồng, thường trồng làm cảnh.
hoa giấy|Cây cảnh có lá bắc mỏng nhiều màu bao quanh những hoa nhỏ.
hoa hậu|Người chiến thắng cuộc thi nhan sắc.
hoa hồng|Hoa có nhiều cánh của cây bụi hoặc cây leo, thường có gai.
hoa lệ|Đẹp rực rỡ, lộng lẫy.
hoa lợi|Sản vật tự nhiên thu được từ ruộng, vườn hoặc tài sản.
hoa màu|Các loại cây trồng trên cạn dùng làm lương thực hoặc thức ăn chăn nuôi.
hoa mười giờ|Hoa nhỏ nhiều màu của cây mọng nước, thường nở khi có nắng.
hoa sứ|Hoa của cây sứ, cánh dày, nhiều giống trắng và thơm.
hoa tiêu|Người am hiểu luồng nước, hướng dẫn tàu qua khu vực khó đi.
hoa văn|Hình ảnh trang trí được tạo ra bằng cách vẽ, chạm hoặc khắc lên bề mặt.
hoa viên|Vườn trồng nhiều loại hoa để ngắm nhìn.
hoạch định|Vạch trước mục tiêu, phương án và các bước cần thực hiện.
hoài bão|Ước muốn lớn được giữ lâu dài và hướng người ta hành động.
hoài niệm|Tưởng nhớ về những điều đã qua từ lâu.
hoan hô|La to để khen ngợi, cổ vũ hoặc thể hiện sự vui mừng.
hoan nghênh|Lời khen ngợi khi ai đó bắt đầu làm một việc tốt.
hoàn cảnh|Tổng hợp các yếu tố bên ngoài ảnh hưởng đến sự việc.
hoàn cầu|Toàn bộ thế giới.
hoàn chỉnh|Có đủ tất cả bộ phận cần thiết để hoàn tất.
hoàn hảo|Tốt tuyệt đối, không còn điều gì cần sửa đổi.
hoàn tất|Làm xong toàn bộ, không còn bước nào chưa thực hiện.
hoàn thành|Làm xong mọi việc cần làm, không còn thiếu sót hay bỏ dở.
hoàn thiện|Đầy đủ và hoàn hảo.
hoàn toàn|Không còn sót lại gì, trọn vẹn và đầy đủ về mọi khía cạnh.
hoãn|Dời việc đã định sang một lúc muộn hơn.
hoán cải|Thay đổi hình thức hoặc bản chất theo hướng tốt hơn.
hoán vị|Cách sắp lại thứ tự mọi phần tử của một tập hữu hạn.
hoang|Không có người chăm nom, canh tác hay ở thường xuyên.
hoang dã|Sống hoặc phát triển trong tự nhiên, chưa được thuần hóa.
hoang dại|Mang tính chất tự nhiên, chưa có bàn tay con người tác động.
hoang mạc|Vùng đất rất khô, mưa ít và chỉ có thảm thực vật thưa thớt.
hoang phí|Sử dụng tiền bạc hoặc của cải một cách bừa bãi, không cần thiết.
hoang sơ|Còn dáng vẻ tự nhiên, ít chịu tác động của con người.
hoang vắng|Ít người đến, không có người sinh sống.
hoang vu|Hoang vắng, không có người ở, chỉ có cây cỏ mọc tự nhiên.
hoàng hôn|Lúc trời về chiều khi mặt trời lặn xuống chân trời.
hoàng oanh|Loài chim lông vàng, có tiếng hót hay và đẹp.
hoành tráng|Có quy mô lớn, bề thế và gây ấn tượng mạnh.
hoạt bát|Nhanh nhẹn, linh hoạt trong lời nói và hành động.
hoạt cảnh|Cảnh diễn trên sân khấu với người đứng yên để mô tả hoặc tượng trưng cho một sự việc.
hoạt động|Thực hiện các việc khác nhau để đạt mục đích.
hoạt náo|Làm cho không khí vui vẻ, náo nhiệt.
hoạt thạch|Chất khoáng dạng bột trắng dùng để thấm hút mồ hôi trên da.
học bạ|Sổ ghi chép điểm số, thành tích và các thông tin liên quan đến học tập của học sinh.
học bổng|Số tiền hỗ trợ miễn phí để người học tiếp tục theo đuổi việc học tập.
học cụ|Đồ dùng phục vụ trực tiếp cho việc học và thực hành.
học đường|Nơi dạy học cho học sinh.
học giả|Người chuyên khảo cứu và có hiểu biết sâu trong một lĩnh vực.
học hành|Học tập nói chung hoặc vừa học vừa thực hành.
học hỏi|Tìm tòi, học tập để tích lũy thêm kiến thức và hiểu biết mới.
học liệu|Tài liệu, dụng cụ vật chất dùng để hỗ trợ việc học và nghiên cứu.
học nghiệp|Kiến thức và kỹ năng thu được qua việc học tập.
học phái|Nhóm học giả cùng theo đuổi một phương pháp hoặc tư tưởng riêng.
học phần|Phần chương trình học tập có đủ kiến thức và kỹ năng cần thiết.
học phí|Tiền phải đóng định kỳ để được đến trường học.
học sinh|Người đang theo học ở trường phổ thông.
học tập|Học hỏi kiến thức và rèn luyện kỹ năng để biết, để quen.
học thêm|Học bài thêm ngoài giờ học ở trường.
học thuật|Hệ thống tri thức chuyên sâu về khoa học và xã hội.
học thuyết|Hệ thống quan điểm có trật tự để làm nền tảng suy nghĩ.
học thức|Kiến thức, hiểu biết thu được qua việc học tập.
học trò|Người đang theo học hoặc người được người khác dạy dỗ.
học vấn|Kiến thức và trình độ hiểu biết thu được qua việc học tập.
học vị|Tên gọi cấp bậc cho người đã hoàn thành chương trình đào tạo đại học.
học việc|Người mới vào nghề tập làm việc dưới sự hướng dẫn.
học viên|Người tham dự một khóa đào tạo hay bồi dưỡng.
học vụ|Công việc tổ chức và quản lý việc học trong nhà trường.
hoen|Xuất hiện những vết màu khác trên bề mặt.
hỏi han|Hỏi để biết tình hình của người khác.
hỏi thăm|Hỏi tin về tình hình của ai để bày tỏ quan tâm.
hòm phiếu|Thùng nhựa hoặc kim loại dùng để đựng phiếu bầu cử.
hóm hỉnh|Nói đùa vui vẻ, dí dỏm, hài hước.
hòn đảo|Phần đất nổi có nước bao quanh tứ phía.
hỏng hóc|Mất khả năng làm việc do bộ phận hỏng.
hóng mát|Ra chỗ thoáng để tận hưởng gió và không khí mát.
họp báo|Cuộc gặp gỡ các nhà báo để tuyên bố về vấn đề quan trọng.
họp hành|Tập trung để nghe báo cáo, trao đổi và giải quyết công việc chung.
họp mặt|Gặp gỡ, tụ tập với nhau trong không khí thân thiết.
hô hào|Kêu gọi mọi người cùng tham gia vào việc chung.
hô hấp|Quá trình trao đổi khí vào ra cơ thể.
hô hoán|Kêu to, la lớn để báo hiệu hoặc gọi người đến gần.
hồ điệp|Con bướm có cánh hình cánh bướm.
hồ đồ|Không có lý lẽ, nói chuyện mơ hồ.
hồ hởi|Cảm thấy vui vẻ, phấn khởi và nhiệt tình.
hồ nghi|Cảm thấy chưa chắc chắn về sự thật nên không tin ngay.
hồ sơ|Tập hợp các giấy tờ, thông tin liên quan đến một người hoặc vụ việc.
hồ tiêu|Dây leo cho quả nhỏ thường phơi khô làm gia vị cay thơm.
hổ phách|Khoáng vật trong suốt màu vàng nâu từ nhựa cây hóa thạch.
hỗ trợ|Giúp đỡ nhau hoặc thêm sức vào công việc.
hố ga|Hố đào dọc đường để nước thải lắng cặn và thoát đi.
hộ chiếu|Giấy nhà nước cấp cho công dân để đi nước ngoài.
hộ sản|Người phụ nữ giúp đỡ người khác khi sinh con.
hộ sinh|Nơi chuyên chăm sóc mẹ và trẻ sau khi sinh con.
hộ vệ|Đi theo để che chắn, bảo vệ người khác.
hôi hám|Mang mùi hôi thối khó chịu lan tỏa trong không gian.
hồi âm|Thư trả lời.
hồi đáp|Trả lời lại lời nói hoặc câu hỏi của người khác.
hồi xuân|Khoảng thời gian cây cối đâm chồi nảy lộc sau mùa đông.
hối hả|Vội làm hoặc vội đi như đang thiếu thời gian.
hối thúc|Thúc giục người khác làm nhanh hơn.
hội chợ|Nơi tập hợp nhiều gian hàng bán sản phẩm trong thời gian ngắn.
hội diễn|Dịp các đoàn nghệ thuật cùng trình bày tiết mục của mình.
hội đồng quản trị|Ban lãnh đạo được bầu ra để điều hành công việc của tổ chức.
hội hè|Những ngày vui lớn được tổ chức công khai để mừng lễ hoặc kỷ niệm.
hội họp|Nhiều người tập trung gặp nhau để trao đổi việc chung.
hội nghị|Cuộc họp có tổ chức để nhiều người bàn về một chủ đề.
hội ngộ|Gặp lại người thân thiết sau thời gian xa cách.
hội nhập|Tham gia vào hoạt động chung để cùng phát triển với cộng đồng.
hội thảo|Buổi trao đổi chuyên đề giữa những người có quan tâm hoặc chuyên môn.
hội thoại|Hai bên cùng nhau trao đổi lời nói với nhau.
hội trường|Nơi tổ chức họp lớn chứa được nhiều người.
hội viên|Người tham gia và tuân thủ các quy định của một tổ chức hội.
hội ý|Bàn nhanh với nhau để thống nhất cách xử lý hoặc quyết định.
hôm kia|Lùi hai ngày so với hôm nay.
hôm nay|Ngày mà người nói đang trải qua trong lúc này.
hôm qua|Ngày hôm trước so với ngày hiện tại.
hôn lễ|Lễ cưới hỏi giữa hai người.
hồn hậu|Thật thà, rộng lượng và tốt bụng.
hồn nhiên|Thái độ trong sáng, tự nhiên và không giả dối.
hồn thơ|Nguồn cảm hứng sáng tác khi làm thơ.
hỗn hợp|Các chất hoặc phần tử khác nhau được trộn chung.
hỗn loạn|Không có trật tự, rối rắm.
hồng|Màu nhạt như sắc đỏ pha thêm trắng.
hồng hạc|Chim nước chân dài, lông thường hồng, có mỏ gập để lọc thức ăn.
hồng hào|Da mặt đỏ thắm vì sức khỏe tốt.
hồng phúc|May mắn lớn lao, được hưởng nhiều điều tốt đẹp.
hồng xiêm|Quả vỏ nâu, khi chín có thịt mềm ngọt và hạt đen bóng.
hộp số|Bộ phận dùng để đổi tốc độ quay của động cơ.
hộp thư|Hộp chứa thư hoặc mục nhắn tin trên mạng.
hờ hững|Thiếu sự quan tâm và không chú ý đến người khác.
hơi nước|Khí nước bốc lên khi nước sôi hoặc nóng.
hơi thở|Không khí đi vào và ra khỏi phổi khi con người sống.
hời hợt|Chỉ nhìn mặt ngoài không đi sâu vào chi tiết.
hỡi ôi|Than thở vì sự việc đáng tiếc xảy ra.
hớn hở|Biểu lộ niềm vui rõ ra trên nét mặt và cử chỉ.
hợp âm|Nhóm các nốt nhạc vang lên cùng lúc tạo thành giai điệu.
hợp chất|Chất tạo thành từ nhiều nguyên tử khác nhau liên kết với nhau theo tỷ lệ cố định.
hợp đồng|Văn bản ghi rõ các điều kiện hai bên đồng ý và phải tuân theo theo luật.
hợp kim|Kim loại được tạo ra bằng cách trộn lẫn nhiều nguyên tố khác nhau.
hợp lệ|Đúng theo quy định và được công nhận là có giá trị.
hợp lực|Tổng sức mạnh tạo ra khi nhiều lực cùng tác động vào một vật.
hợp lưu|Nơi hai dòng sông gặp nhau và chảy thành một dòng duy nhất.
hợp nhất|Gộp nhiều phần lại thành một khối.
hợp pháp|Đúng quy định của nhà nước, được pháp luật công nhận và bảo vệ.
hợp phần|Một phần riêng đóng góp vào cấu tạo của toàn thể.
hợp tác|Làm việc chung với nhau để đạt được mục đích cùng nhau.
hợp tác xã|Nhóm người cùng sở hữu và quản lý cơ sở sản xuất chung.
hợp thành|Ghép nhiều phần lại thành một khối.
hợp thời|Phù hợp với hoàn cảnh, đúng thời điểm và thích ứng với xu hướng của thời đại.
hợp thức|Phù hợp với các quy định, luật lệ và thủ tục đã được thiết lập.
hợp xướng|Hát cùng lúc nhiều bè để tạo thành một bài.
huân chương|Huy hiệu, huy chương hoặc vật phẩm trang trọng do nhà nước trao tặng để khen thưởng công lao.
huấn luyện viên|Người hướng dẫn tập luyện và chuẩn bị cho vận động viên thi đấu.
huê viên|Khu vực trồng nhiều loại hoa để làm đẹp cảnh quan.
hun đúc|Tạo nên phẩm chất tốt qua rèn luyện, thử thách.
hùng cường|Mạnh mẽ, có sức ảnh hưởng lớn.
hùng hậu|Mạnh mẽ và có quy mô rất lớn.
hùng tráng|Mạnh mẽ, oai hùng và có quy mô lớn lao.
hùng vĩ|Mạnh mẽ, lớn lao và gây ấn tượng mạnh.
húng|Rau thơm có lá nhỏ, thường ăn kèm các món cuốn.
huống gì|Khi nói việc sau chắc chắn xảy ra hơn việc trước.
huống hồ|Từ nối nêu trường hợp thứ hai càng rõ hơn trường hợp vừa nói.
huy chương|Vật kỷ niệm thường bằng kim loại để trao khi đạt thành tích.
huy động|Tập hợp và sử dụng nguồn lực con người, tiền của cho việc lớn.
huy hiệu|Dấu nhỏ thường gắn lên áo để nhận biết tổ chức hoặc thành tích.
huy hoàng|Đạt được đỉnh cao rực rỡ về giá trị và gây lòng kính phục.
huyền thoại|Câu chuyện hư cấu mang vẻ thần bí và lạ lùng.
huyện|Đơn vị hành chính từng gồm nhiều xã hoặc thị trấn ở Việt Nam.
huyện hàm|Chức quan quản lý một huyện nhưng không có quyền lực thực tế.
huyện thị|Đơn vị hành chính gồm cả huyện và thị xã khi nói chung.
huyện vụ|Công việc hành chính do người quản lý huyện phụ trách.
huýt|Chúm môi thổi ra luồng hơi phát tiếng cao.
hư cấu|Tạo ra từ trí tưởng tượng, không dựa trên sự thật.
hư danh|Tên gọi hoặc tiếng tăm không có thật, chỉ là hư vô.
hư hỏng|Chịu tác động làm mất đi chức năng hoặc tính chất tốt đẹp ban đầu.
hứa hẹn|Báo hiệu khả năng đem lại điều đáng mong đợi.
hưng thịnh|Phát triển mạnh và sung túc.
hừng hực|Nóng rực, bốc lên mạnh mẽ hoặc đầy sức sống.
hững hờ|Thờ ơ, không quan tâm gì hết.
hứng thú|Sự thích thú, vui vẻ khi làm việc gì.
hương|Mùi thơm tỏa từ hoa, thức ăn hoặc vật khác.
hương chính|Nhiệm vụ hành chính do chính quyền địa phương trong làng đảm nhiệm.
hương liệu|Chất được thêm với lượng nhỏ để tạo mùi cho sản phẩm.
hương thơm|Mùi ngát dễ chịu tỏa ra từ hoa hoặc trầm.
hương vị|Mùi thơm và vị ngon đặc trưng của món ăn hay sự vật.
hưởng thụ|Tận dụng và cảm thấy vui vẻ với những điều tốt đẹp.
hưởng ứng|Tham gia hoặc bày tỏ sự ủng hộ sau một lời kêu gọi.
hướng dẫn|Chỉ bảo cách làm và dẫn đường để người khác biết tiến hành việc gì.
hướng dương|Cây cho cụm hoa lớn với vòng cánh vàng quanh đĩa hạt.
hướng thiện|Hướng về điều tốt đẹp, lương thiện.
hươu|Thú móng guốc chân thon, con đực nhiều loài có gạc.
hươu cao cổ|Thú châu Phi có cổ và chân rất dài, lông nhiều mảng đốm.
hưu trí|Trạng thái nghỉ việc của công chức khi đã đến tuổi già.
hữu cơ|Trong hóa học, thuộc nhóm hợp chất có nền tảng cacbon.
hữu dụng|Có ích, mang lại lợi ích hoặc phục vụ được công việc.
hữu hạn|Có giới hạn rõ ràng, không thể vô tận.
hữu hiệu|Có tác dụng, sinh hiệu quả như mong đợi.
hữu hình|Có thể nhìn thấy và sờ thấy bằng mắt.
hữu ích|Mang lại lợi ích, có tác dụng tốt cho việc làm hoặc cuộc sống.
hữu nghị|Tình bạn thân thiết, hòa thuận.
hữu quan|Có mối liên hệ hoặc dính líu đến vấn đề đang xét.
hữu thể|Những gì tồn tại và có thể cảm nhận được trong thực tế.
hữu ý|Có chủ đích thực hiện việc gì đó.
ì ạch|Tiến lên chậm chạp như phải gắng sức từng chút.
ích lợi|Cái có tác dụng tốt, mang lại lợi ích cho người khác.
im bặt|Im lặng hoàn toàn, không còn tiếng động.
im ỉm|Nói nhỏ, không để người khác nghe thấy.
im lặng|Không phát ra âm thanh hay tiếng nói dù có hoạt động.
im lìm|Yên tĩnh, không có tiếng động hay hoạt động gì cả.
im phăng phắc|Không có tiếng động nào cả, yên tĩnh tuyệt đối.
in ấn|Tạo nhiều bản chữ hay hình trên giấy hoặc vật liệu khác.
ít khi|Trạng thái xảy ra sự việc không thường xuyên hoặc rất hiếm hoi.
ít lời|Người ít nói chuyện, không hay mở miệng nhiều.
ít nhất|Số lượng hoặc mức độ thấp nhất có thể chấp nhận được.
ít nhiều|Không nhiều cũng không ít, ở mức độ vừa phải.
ít ỏi|Số lượng hoặc số tiền rất nhỏ, không đáng kể.
ít tuổi|Còn trẻ, chưa lớn tuổi.
kẽ hở|Nơi trống rỗng nhỏ giữa hai vật hoặc hai phần.
kem que|Kem đông trên một que nhỏ để cầm khi ăn.
kèm cặp|Theo sát để chỉ bảo, dìu dắt.
kèm theo|Có thêm bên cạnh thứ chính hoặc đến cùng một việc khác.
kèn trống|Tên chung các nhạc cụ thổi và gõ thường dùng khi diễu hành hay mở hội.
kén chọn|Tìm và lựa chọn rất kỹ lưỡng đối tượng cần thiết.
kẻng|Miếng kim loại được gõ cho vang để báo hiệu.
keo kiệt|Ít cho, chỉ biết giữ của, không muốn chia sẻ.
keo sơn|Gắn bó keo dán, gắn kết bền chặt không rời.
kéo co|Trò chơi tập thể kéo dây để xem bên nào thắng.
kéo dài|Làm tăng chiều dài hoặc khiến việc diễn ra lâu hơn.
kéo lê|Kéo vật nặng lê trên mặt đất mà không thể nâng lên.
kẹo cao su|Loại kẹo dẻo dai, nhai lâu để làm sạch răng hoặc giải trí.
kẹp tóc|Vật nhỏ dùng để giữ các lọn tóc gọn ở vị trí mong muốn.
kê khai|Liệt kê từng mục ra giấy.
kể lại|Nói lại những điều đã xảy ra, thường dùng để thuật lại một câu chuyện.
kể ra|Thực tế, sự thật vốn có của việc đó.
kể trên|Những điều đã được nhắc đến hoặc ghi lại ở trên.
kế cận|Nằm sát bên cạnh hoặc đứng ngay sau để thay thế.
kế đến|Tiếp nối ngay sau sự việc hoặc người trước.
kế hoạch|Danh sách các việc định làm trước, được sắp xếp rõ ràng và có thời gian cụ thể.
kế nghiệp|Tiếp tục công việc, sự nghiệp của người đi trước.
kế sách|Phương pháp, mưu kế lớn để giải quyết việc khó.
kế thừa|Tiếp tục phát huy giá trị tốt đẹp từ những gì đã có của người trước.
kế tiếp|Đến lượt sau, nối tiếp ngay sau sự việc hoặc người trước.
kế toán|Công việc ghi chép, kiểm tra và tổng hợp các khoản tài chính.
kế tục|Tiếp nối công việc hoặc vai trò của người đã đi trước.
kế tự|Làm người nối tiếp dòng dõi tổ tiên.
kếch xù|Lớn vượt ngoài mức thông thường.
kênh|Dòng nước do người đào, dùng dẫn nước hay đi thuyền.
kết bạn|Làm quen và trở thành người bạn với nhau.
kết cấu|Cách những phần bên trong nối nhau để tạo thành một chỉnh thể.
kết cấu hạ tầng|Tổng hợp các công trình phục vụ sản xuất và đời sống.
kết cục|Kết quả cuối cùng xảy ra sau khi sự việc kết thúc.
kết dư|Số tiền còn lại sau khi trừ chi phí khỏi tổng thu nhập.
kết giao|Gắn bó, thân thiết với nhau bằng lời hứa.
kết hôn|Làm lễ cưới để trở thành vợ chồng chính thức theo quy định.
kết hợp|Gắn liền với nhau để hỗ trợ và hoàn thiện cho nhau.
kết luận|Kết quả cuối cùng rút ra sau khi bàn bạc về vấn đề.
kết nghĩa|Hai bên xem nhau như anh em ruột thịt.
kết nối|Gắn các phần rời rạc lại thành một khối liền mạch.
kết quả|Tổng hợp mọi điều xảy ra sau khi một việc kết thúc.
kết thúc|Đi đến điểm cuối, không còn phần tiếp theo của việc ấy.
kết tinh|Hình thành chất rắn có trật tự tinh thể từ dung dịch hay chất nóng chảy.
kết trái|Chuyển sang giai đoạn có quả sau khi cây ra hoa.
kết tủa|Chất rắn ít tan xuất hiện trong dung dịch sau một biến đổi.
kêu ca|Nói ra điều mình không hài lòng một cách phiền muộn.
kêu cứu|Hét lớn để xin người đến giúp đỡ.
kêu gọi|Lời kêu mời mọi người cùng tham gia làm một việc.
khả ái|Có vẻ đẹp dễ làm người khác yêu mến.
khả dụng|Dùng được và có tác dụng tốt.
khả năng|Tính chất có thể xảy ra khi gặp điều kiện thích hợp.
khả quan|Tình hình nhìn chung tốt và đáng tin cậy.
khả thi|Có thể thực hiện được.
khá giả|Có tiền bạc đủ dùng cho sinh hoạt hàng ngày mà không thiếu thốn.
khác biệt|Có những điểm không giống nhau giữa các đối tượng.
khác nhau|Không giống nhau khi so về ít nhất một đặc điểm.
khác thường|Đặc biệt, không giống với điều bình thường.
khác xa|Hoàn toàn không giống nhau.
khách|Người đến thăm, mua hàng hoặc sử dụng dịch vụ.
khách hàng|Người đến cửa hàng để mua sắm hoặc thuê dịch vụ.
khách khứa|Những người đến chơi nhà.
khách sạn|Cơ sở cho khách đi xa thuê phòng nghỉ theo đêm.
khách sáo|Tỏ ra lịch sự khi từ chối để giữ thể diện cho cả hai bên.
khách thể|Đối tượng mà con người quan sát, nhận biết và tác động vào.
khai|Nêu ra chính thức những thông tin được hỏi.
khai bút|Viết những dòng đầu tiên, thường nhân dịp đầu năm.
khai giảng|Khởi động hoạt động giảng dạy cho một năm học hoặc khóa học mới.
khai hoa|Mở cánh hoa hoặc sinh con.
khai hoang|Đưa đất còn bỏ trống vào sử dụng để trồng trọt.
khai khoáng|Đào lấy các chất khoáng từ lòng đất ra ngoài.
khai mạc|Trang trọng mở đầu buổi biểu diễn hay sự kiện.
khai sáng|Mở mang trí tuệ, giúp người ta hiểu rõ sự thật và tiến bộ.
khai thác|Đưa nguồn lực đang có vào sử dụng để thu lợi ích.
khai trương|Bắt đầu mở cửa hoạt động chính thức, thường nói về cửa hàng.
khải hoàn|Thắng trận và trở về với vinh quang.
khái lược|Nói ngắn gọn những ý chính và bao quát nhất.
khái niệm|Cách suy nghĩ giúp con người nhận ra và hiểu rõ những đặc điểm, tính chất cơ bản của sự vật và hiện tượng.
khái quát|Tóm lược những điểm chung của nhiều sự vật hay hiện tượng.
khái toán|Số tiền ước tính tổng cộng cho toàn bộ dự án xây dựng.
khảm|Gắn vật liệu khác màu vào những chỗ khoét để trang trí.
khám phá|Tìm thấy hoặc hiểu ra điều trước đó còn chưa biết.
khan hiếm|Số lượng ít, khó tìm thấy trên thị trường.
khán đài|Khu ghế hoặc bậc cao dành cho người theo dõi cuộc thi đấu.
khán giả|Người xem các buổi biểu diễn, phim hoặc chương trình.
khán phòng|Phòng lớn dành cho khán giả xem biểu diễn nghệ thuật.
khang trang|Ngôi nhà rộng rãi, sạch sẽ và đẹp.
khánh kiệt|Hết sạch mọi thứ, không còn gì lại.
khánh thành|Trang trọng mở cửa cho công trình hoàn tất.
khao khát|Cảm giác muốn có điều gì đó một cách rất mạnh mẽ.
khảo cổ|Nghiên cứu đời sống xưa qua di vật và dấu tích được tìm thấy.
khảo cổ học|Ngành nghiên cứu xã hội xưa thông qua đồ vật và di tích còn lại.
khảo luận|Việc tìm hiểu kỹ và tranh luận chi tiết về một chủ đề cụ thể.
khảo thí|Việc thi cử để kiểm tra kiến thức và chọn người.
khát|Cảm thấy cơ thể cần uống nước.
khát vọng|Ước muốn lớn, mong đợi một điều gì đó rất mạnh mẽ.
khay|Đồ có mặt phẳng và thành thấp để bày hoặc bưng đồ.
khắc|Tạo chữ hoặc hình bằng cách khoét vào bề mặt cứng.
khắc phục|Vượt qua khó khăn để đạt được mục tiêu.
khắc sâu|Ghi nhớ kỹ lưỡng, khó quên.
khăn|Miếng vải dùng lau người, quàng cổ hay phủ đồ.
khăn gói|Sửa soạn đồ dùng cần mang để lên đường.
khăn quàng|Dải vải mang quanh cổ để giữ ấm hoặc trang trí.
khăn tay|Miếng vải nhỏ có thể mang theo để lau tay hay mặt.
khăng khăng|Cố chấp, nhất định không chịu đổi ý.
khăng khít|Gắn bó chặt chẽ, không thể tách rời nhau.
khẳng định|Nói chắc chắn rằng một điều gì đó là đúng sự thật.
khẳng khiu|Cơ thể gầy guộc, xương lộ rõ, thiếu mỡ và thịt.
khắp|Ở tất cả các nơi trong phạm vi đang nói đến.
khâm phục|Tỏ lòng kính trọng và ngưỡng mộ đối với người có đạo đức, trí tuệ vượt trội.
khẩn cấp|Việc cần phải giải quyết ngay lập tức, không thể chậm trễ.
khẩn cầu|Cầu xin một cách rất khẩn thiết, hết lòng.
khẩn trương|Làm nhanh và tập trung vì thời gian không còn nhiều.
khập khiễng|Đi không vững vì chân trái và chân phải không bằng nhau.
khâu|Dùng kim và chỉ nối các lớp vải lại.
khẩu ngữ|Khả năng diễn đạt ý nghĩ và cảm xúc bằng tiếng nói.
khẩu phần|Lượng thức ăn được chia cho mỗi bữa hoặc mỗi ngày.
khẩu trang|Đồ bảo vệ bằng vải, đeo che mũi và miệng.
khẩu vị|Thích ăn món gì, không thích món gì.
khấu hao|Tính toán phần giá trị bị mòn hao của tài sản để trừ dần vào chi phí sản xuất.
khấu trừ|Trừ bớt một khoản tiền ra khỏi tổng số phải trả.
khen|Nói ra điều tốt mình nhận thấy ở người hay việc.
khen ngợi|Ca ngợi những việc làm tốt đẹp.
khen thưởng|Tỏ lời khen ngợi và trao tặng quà hoặc giấy khen.
khéo|Làm việc thành thạo và tinh tế.
khéo léo|Biết dùng tay hoặc lựa cách ứng xử một cách tinh tế.
khéo tay|Có đôi tay linh hoạt, làm các việc thủ công rất giỏi.
khép|Đưa hai mép hoặc hai cánh lại gần nhau.
khép kín|Đóng chặt cửa hoặc ngăn cách để không có gì lọt qua.
khét|Có mùi đặc trưng của thứ bị cháy quá lửa.
khế ước|Giấy viết ghi rõ các điều kiện hai bên đồng ý thực hiện.
khệ nệ|Nặng nề, chậm chạp do mang vác đồ vật cồng kềnh.
khi nào|Bao giờ, lúc nào. / Không bao giờ.
khí cầu|Quả cầu lớn chứa khí nhẹ, dùng để bay lơ lửng trên không trung.
khí chất|Đặc điểm tâm lý tạo nên tính cách riêng của mỗi người.
khí cụ|Đồ dùng để thực hiện công việc hoặc hoạt động cụ thể.
khí động học|Môn học nghiên cứu cách vật chuyển động trong không khí.
khí đốt|Khí nhiên có trong lòng đất, dùng làm nhiên liệu sinh nhiệt.
khí hậu|Đặc điểm nắng, mưa và nhiệt độ của một vùng trong nhiều năm.
khí lực|Sức khỏe và năng lượng thể chất của con người.
khí nhà kính|Loại khí giữ nhiệt, làm Trái Đất nóng lên.
khí nhạc|Âm nhạc được biểu diễn bằng cách sử dụng các nhạc cụ.
khí phách|Đức tính mạnh mẽ, dám làm những việc lớn lao, không sợ khó khăn.
khí quản|Ống dẫn khí từ cổ xuống hai lá phổi.
khí quyển|Lớp không khí bao bọc lấy toàn bộ Trái Đất.
khí thế|Sự hăng hái và sức thúc đẩy thể hiện ở một tập thể hay hoạt động.
khí thiên nhiên|Khí đốt tự nhiên dùng làm nhiên liệu hoặc nguyên liệu.
khí thực|Chất khí có thật tồn tại trong tự nhiên và môi trường.
khí tiết|Đạo đức, khí phách và nguyên tắc sống của con người.
khí tượng|Những biến đổi trong không khí như mưa, gió, sấm sét.
khí tượng học|Môn khoa học nghiên cứu các hiện tượng trong khí quyển để dự báo thời tiết.
khía|Rạch một đường nông dài trên bề mặt.
khía cạnh|Một mặt riêng có thể xem xét của vấn đề.
khích lệ|Khuyến khích, động viên để người khác thêm phần phấn khởi, nỗ lực.
khiêm nhường|Thái độ khiêm tốn, không tự cao, sẵn sàng nhường nhịn người khác.
khiêm tốn|Thái độ bình tĩnh, không tự cao, không khoe khoang về khả năng hay thành tích của mình.
khiêng|Cùng người khác nâng và chuyển một vật nặng.
khiêu vũ|Chuyển động cơ thể theo nhịp điệu.
khiếu kiện|Nộp đơn kiện cơ quan nhà nước ra tòa để đòi quyền lợi.
khiếu nại|Nói lên sự không đồng ý để yêu cầu xem xét lại quyết định.
khinh thị|Xem thường, không để ý đến giá trị của ai.
khít|Sát nhau đến mức hầu như không có khe hở.
kho báu|Tập hợp nhiều của quý được cất giữ cùng một nơi.
kho quẹt|Món kho mặn sánh, thường dùng chấm rau luộc khi ăn cơm.
kho tàng|Nơi chứa đựng tiền bạc và của cải quý giá.
khò khò|Tiếng thở dài đều đều khi ngủ say.
khó chịu|Cảm thấy không thoải mái, bức bối trong người.
khó coi|Không đẹp mắt, thiếu hấp dẫn hoặc có vẻ đáng sợ.
khó hiểu|Khó mà hiểu rõ ý nghĩa của điều đó.
khó khăn|Điều gây trở ngại, làm việc tiến hành không suôn sẻ.
khó lòng|Khó mà thực hiện được, thường dùng để phủ định điều gì đó.
khó nhọc|Vất vả, nặng nhọc, tốn nhiều sức lực.
khó tính|Khắt khe, đòi hỏi nhiều khiến người khác khó đáp ứng.
khó ưa|Không ai thích, không ai chịu nổi.
khó xử|Gặp tình huống khó khăn, không biết nên làm thế nào.
khoa|Đơn vị ở trường đại học phụ trách một nhóm ngành.
khoa học|Tập hợp tri thức và kinh nghiệm do con người khám phá ra.
khoa học cơ bản|Những ngành nghiên cứu quy luật nền tảng, chưa nhất thiết nhằm ứng dụng ngay.
khoa học máy tính|Lĩnh vực nghiên cứu về máy tính, phần mềm và cách xử lý dữ liệu.
khoa học tự nhiên|Khoa học nghiên cứu các quy luật tự nhiên của thế giới vật chất bằng thực nghiệm.
khoa học ứng dụng|Lĩnh vực nghiên cứu nhằm áp dụng thành tựu khoa học vào kỹ thuật.
khoa học xã hội|Lĩnh vực nghiên cứu các quy luật vận động và phát triển của đời sống xã hội con người.
khoác|Cho áo hoặc khăn phủ lên vai.
khoai lang|Cây dây bò cho củ ăn được, nhiều giống có vị ngọt.
khoai môn|Cây lá rộng hình tim, cho củ nhiều bột dùng nấu ăn.
khoai sọ|Loại khoai có nhiều củ con nhỏ, thịt bở và nhiều tinh bột.
khoai tây|Cây cho củ dưới đất, thường đem luộc, nghiền hoặc chiên.
khoái cảm|Cảm giác vui vẻ, sung sướng từ bên trong.
khoái khẩu|Đồ ăn khiến người ta cảm thấy ngon miệng và thích thú.
khoan|Tạo lỗ bằng một mũi cứng quay nhanh.
khoan dung|Sẵn lòng rộng lượng trước lỗi lầm hoặc khác biệt của người khác.
khoan đã|Yêu cầu người khác chậm lại, đừng vội.
khoan khoái|Cảm thấy nhẹ nhàng, thư thái trong người.
khoan nhượng|Chấp nhận một phần ý kiến đối phương để cùng thỏa thuận.
khoản đãi|Chăm sóc khách quý với lòng tôn trọng và sự chu đáo.
khoảng chừng|Số lượng hoặc mức độ ước lượng không chính xác.
khoảng không|Phần không gian trống giữa các vật hoặc bên trên mặt đất.
khoảng trống|Chỗ không có vật gì lấp đầy, tạo ra khoảng cách giữa hai điểm.
khoáng chất|Thành phần vô cơ có trong tự nhiên hoặc cần cho cơ thể.
khoáng đạt|Rộng rãi, thoáng đãng và tự do, không bị gò bó.
khoáng sản|Chất có trong lòng đất có thể khai thác để làm giàu.
khoáng vật|Chất rắn tự nhiên không có cấu tạo sống, gồm đá, đất, cát hay kim loại.
khoanh|Vẽ một vòng kín quanh điều muốn đánh dấu.
khoanh tay|Gập hai cánh tay lại và đặt chéo phía trước người.
khoanh vùng|Giới hạn một khu vực cụ thể để tiến hành công việc hoặc nghiên cứu.
khoảnh khắc|Một đoạn thời gian rất ngắn đang được nhắc tới.
khóc|Chảy nước mắt khi có cảm xúc mạnh hoặc bị đau.
khóc lóc|Khóc nhiều và than vãn với giọng rên rỉ kéo dài.
khóc nhè|Hay khóc lóc, nũng nịu hoặc than vãn.
khóc thầm|Cảm thấy buồn nhưng không phát ra tiếng khóc.
khoe|Cho người khác thấy thứ khiến mình tự hào.
khoét|Lấy bớt vật liệu để tạo lỗ hoặc phần lõm.
khói|Luồng khí lẫn hạt nhỏ bốc lên từ chỗ cháy.
khóm|Một nhóm cây hoặc hoa mọc tụ gần nhau.
khô cằn|Thiếu nước và dinh dưỡng khiến cây cối hoặc đất đai không phát triển.
khô khốc|Thiếu nước đến mức cứng và nứt nẻ.
khô ráo|Không bị ướt, không có nước dính vào.
khổ công|Làm việc vất vả, tốn nhiều sức lực và tâm trí.
khôi hài|Có tính chất vui vẻ, khiến người ta cười.
khôi ngô|Sáng sủa, đẹp trai và thông minh.
khôi phục|Đưa về gần trạng thái tốt hoặc trạng thái vốn có trước đó.
khối cầu|Hình dạng không gian tròn đều bao quanh một điểm cố định.
khối lượng|Số đo thể hiện độ nặng của vật tại một nơi cụ thể.
khôn|Biết suy xét để chọn cách làm có lợi.
khôn khéo|Thông minh và linh hoạt trong cách ứng xử hàng ngày.
khôn lanh|Thông minh và nhanh nhẹn trong suy nghĩ.
khôn lường|Khó có thể dự đoán trước được kết quả.
khôn ngoan|Biết xử lý mọi việc và ứng xử khéo léo.
khôn tả|Khó có thể diễn đạt hết bằng lời nói hay chữ viết.
khôn xiết|Không thể tính hết, không có giới hạn.
không bao giờ|Chưa từng xảy ra vào bất kỳ lúc nào.
không biết|Chưa nhận thức được điều gì hoặc chưa từng nghe biết về sự việc đó.
không đổi|Giữ nguyên giá trị, không thay đổi dù thời gian trôi qua.
không gian|Môi trường vô hình chứa đựng mọi vật chất và sự vận động.
không hề|Chưa từng xảy ra hay xuất hiện trong bất kỳ lúc nào.
không hư|Trống rỗng, không chứa đựng vật gì bên trong.
không kém|Bằng hoặc hơn một vật khác.
không khí|Chất khí vô hình, không mùi vị mà sinh vật cần để thở.
không lưu|Hoạt động bay của máy bay trong không gian và ra vào sân bay.
không ngừng|Làm liên tục, không bao giờ dừng lại hay nghỉ ngơi.
không thể|Không có năng lực hay điều kiện để thực hiện được việc gì đó.
không thích|Cảm giác khó chịu, không hài lòng hoặc ghét bỏ khi gặp phải điều gì đó.
không trung|Khoảng trời phía trên mặt đất.
không tưởng|Viển vông, xa rời thực tế, không thể hiện thành hiện thực.
khổng lồ|Cực kỳ to lớn, vượt xa mức bình thường.
khởi công|Bắt đầu tiến hành xây dựng một công trình.
khởi đầu|Bắt đầu thực hiện một công việc hoặc sự kiện mới.
khởi điểm|Nơi bắt đầu của một sự việc hay hành trình.
khởi động|Bật máy hoặc mở chương trình để bắt đầu hoạt động.
khởi hành|Bắt đầu rời nơi xuất phát để đi một chuyến.
khởi nghiệp|Thành lập và phát triển một công ty mới.
khởi nguồn|Bắt đầu được sinh ra từ nơi xuất phát.
khởi phát|Bắt đầu xuất hiện hoặc khởi đầu một sự việc.
khởi sự|Bắt đầu tiến hành việc đã tính đến.
khớp|Chỗ nối giữa các xương cho phép cơ thể cử động.
khớp gối|Chỗ nối giữa đùi và cẳng chân giúp chân co duỗi.
khu biệt|Phân định ranh giới rõ ràng giữa các khu vực hoặc đối tượng khác nhau.
khu công nghiệp|Khu vực được quy hoạch riêng để sản xuất hàng hóa công nghiệp.
khu dân cư|Nơi tập trung sinh sống của nhiều hộ gia đình.
khu trú|Chỉ sinh sống hoặc hoạt động tại một địa điểm duy nhất.
khu vực|Phần đất đai có ranh giới rõ ràng và chức năng riêng biệt.
khuân|Mang vật nặng từ nơi này sang nơi khác.
khuất|Bị che nên không còn nhìn thấy từ một phía.
khuất phục|Chịu thua, bỏ ý chí chống đối.
khuấy|Đưa thìa hay que xoay trong chất lỏng cho đều.
khuấy động|Làm cho nơi chốn hoặc tâm trí chuyển từ yên lặng sang ồn ào, náo nhiệt.
khúc|Đoạn được tách ra từ một vật dài.
khúc côn cầu|Môn thể thao dùng gậy đánh bóng vào lỗ trên sân rộng.
khúc khích|Cười nhỏ, tiếng cười ríu rít vui vẻ.
khúc khuỷu|Quanh co, không thẳng, nhiều khúc ngoặt.
khúc mắc|Có vấn đề vướng víu, khó nói ra hoặc khó giải quyết.
khuếch đại|Làm cho âm thanh, hình ảnh hoặc ý tưởng trở nên to hơn, rõ hơn.
khuếch tán|Các hạt lan ra vùng xung quanh do chuyển động ngẫu nhiên.
khum|Uốn cong như lòng bàn tay đang hứng nước.
khúm núm|Thái độ cúi đầu, co người lại để tỏ vẻ kính sợ và lễ phép.
khung|Bộ phận cứng tạo dáng hoặc nâng đỡ cho đồ vật.
khung cảnh|Cảnh vật bao quanh trong một không gian cụ thể.
khung cửi|Khung máy giữ sợi dọc để luồn sợi ngang thành tấm vải.
khung thành|Cấu trúc gồm hai cột và một xà ngang dùng để ghi bàn trong bóng đá.
khuôn|Vật có lòng định hình để đúc hoặc ép sản phẩm.
khuôn khổ|Phạm vi hoặc giới hạn đặt ra cho hoạt động nào đó.
khuôn mặt|Toàn phần phía trước của đầu, gồm mắt, mũi và miệng.
khuôn mẫu|Hình mẫu chuẩn mực để làm theo hoặc người đáng được noi gương.
khuôn viên|Toàn bộ khoảng đất trong ranh giới của một công trình hay cơ sở.
khuya|Khoảng đêm muộn khi phần đông đã đi ngủ.
khuyên|Nói cho ai biết điều mình nghĩ họ nên làm.
khuyên bảo|Nói lời hay để người khác biết điều phải trái.
khuyên can|Bảo ban, ngăn cản không nên phạm lỗi.
khuyên giải|Nói lời thân thiết để làm cho người khác bớt buồn, vơi đi nỗi khổ.
khuyên nhủ|Chia sẻ lời khuyên với thái độ dịu dàng.
khuyến cáo|Đưa ra lời khuyên cho số đông.
khuyến học|Việc động viên và hỗ trợ người đi học.
khuyến khích|Tạo động lực để người khác mạnh dạn làm điều có ích.
khuyến mãi|Dành lợi ích cho khách hàng để thúc đẩy mua sắm.
khuyến nghị|Đề xuất ý kiến nhằm khuyến khích người khác thực hiện mà không ép buộc.
khuyến nông|Hoạt động cổ động, hỗ trợ để phát triển nghề trồng trọt và chăn nuôi.
khuyết|Thiếu mất một phần nên không còn đầy đặn.
khuyết danh|Viết tác phẩm nhưng không ghi tên người làm.
khuyết điểm|Sai lầm, thiếu sót hoặc điểm yếu.
khuynh hướng|Xu hướng mà tâm trí người ta thường hướng về.
khuỷu tay|Chỗ gập nối cánh tay với cẳng tay.
khứ hồi|Đi và về trên cùng một lộ trình, dùng cùng một phương tiện.
khước từ|Từ chối không nhận hoặc không đồng ý với điều gì đó.
khứu giác|Khả năng nhận biết và phân biệt các mùi.
ki bo|Ít tiền, keo kiệt và không chịu chi.
kích cỡ|Số đo hoặc kích thước phân loại theo mức độ lớn nhỏ.
kích hoạt|Làm cho thiết bị hoặc sự việc bắt đầu hoạt động.
kích thước|Độ dài, rộng, cao xác định kích cỡ của vật.
kịch|Tác phẩm được diễn trên sân khấu bằng lời và động tác.
kịch bản|Nội dung chi tiết của vở kịch được viết thành văn bản trước khi diễn.
kịch bản phim|Lời thoại và hành động được viết sẵn cho nhân vật.
kịch câm|Loại kịch chỉ diễn bằng nét mặt và cử chỉ.
kịch hát|Nghệ thuật sân khấu kết hợp giữa diễn xuất và hát theo điệu thức cố định.
kịch liệt|Mạnh mẽ, quyết liệt đến mức cao độ.
kịch mục|Danh sách các chương mục trong buổi biểu diễn.
kịch nói|Loại kịch dùng lời đối thoại để diễn biến câu chuyện.
kiềm chế|Dùng sức mạnh hoặc ý chí để kìm giữ, không cho phát triển.
kiểm chứng|Làm lại để xác nhận điều đó có đúng không.
kiểm đếm|Đếm số lượng và rà soát lại thông tin.
kiểm định|Đối chiếu với tiêu chuẩn để xác nhận chất lượng hoặc độ tin cậy.
kiểm kê|Đếm số lượng từng loại để biết tổng cộng còn bao nhiêu.
kiểm lâm|Lực lượng chuyên theo dõi và bảo vệ rừng.
kiểm ngân|Quản lý, đếm và giao nhận tiền bạc, tài sản quý.
kiểm nghiệm|Đem thử hoặc phân tích để xác nhận một tính chất hay kết luận.
kiểm ngư|Bộ phận nhà nước giám sát và bảo vệ nguồn lợi thủy sản.
kiểm soát|Giữ cho mọi việc diễn ra đúng quy định và không sai lệch.
kiểm thử|Hoạt động kiểm tra kết quả hoạt động của phần mềm.
kiểm tra|Xem xét kỹ lưỡng để biết có đúng hay không.
kiếm ăn|Tìm phương cách để nuôi sống bản thân.
kiên cố|Vững chắc, bền bỉ, khó bị hư hỏng hay đổ vỡ.
kiên cường|Bền lòng không bỏ cuộc dù gặp khó khăn lớn.
kiên định|Giữ vững tâm trí và lập trường không thay đổi trước khó khăn.
kiên nhẫn|Bền lòng theo đuổi việc cần nhiều thời gian.
kiên quyết|Giữ vững quyết định và hành động dứt khoát trước trở ngại.
kiên tâm|Giữ vững ý chí, không lay chuyển trước khó khăn.
kiên trì|Tiếp tục làm việc đã chọn dù tiến độ chậm hoặc gặp trở ngại.
kiến|Côn trùng nhỏ sống thành đàn, thường đi kiếm ăn theo hàng.
kiến giải|Cách hiểu và đưa ra ý kiến riêng về một vấn đề cụ thể.
kiến lập|Xây dựng nên một sự vật hay một tổ chức.
kiến nghị|Đề xuất để mọi người cùng bàn và quyết định.
kiến tạo|Tạo dựng nên một cấu trúc hoặc giá trị mới.
kiến thiết|Thực hiện công tác xây dựng với quy mô lớn và mục đích phát triển.
kiến thức|Những điều đã biết được nhờ vào việc học hỏi và tìm tòi.
kiến trúc|Nghề nghiệp thiết kế và xây dựng các công trình có tính thẩm mỹ.
kiến trúc sư|Người thiết kế không gian, hình dáng và cách sử dụng công trình.
kiện cáo|Đưa vụ việc ra tòa để kiện.
kiện toàn|Hoàn thiện và củng cố để đạt đến mức độ đầy đủ, mạnh mẽ nhất.
kiện tướng|Người có tài năng xuất sắc hoặc danh hiệu khen thưởng cao quý.
kiêng cữ|Tránh không ăn uống hoặc làm những việc mình cho là có hại cho sức khỏe.
kiềng|Giá đỡ để đặt nồi lên trên ngọn lửa.
kiếp trước|Cuộc đời hoặc kiếp sống mà một người đã trải qua trước khi sinh ra đời này.
kiệt tác|Tác phẩm nghệ thuật có giá trị và vẻ đẹp vượt trội so với các tác phẩm khác.
kiệt xuất|Vượt trội hẳn so với những người khác.
kiều diễm|Đẹp đê, mềm mại và lộng lẫy như người con gái.
kiểu|Mẫu hình hoặc cách làm có nét riêng.
kiểu cách|Cách thức hành xử hoặc phong cách riêng.
kiểu dáng|Hình dáng bên ngoài được thiết kế theo một mẫu nhất định.
kiểu hình|Tổng hợp tất cả những đặc điểm bên ngoài và tính chất của cơ thể.
kiểu mẫu|Mẫu hình chuẩn dùng để làm ra nhiều sản phẩm giống nhau.
kim băng|Ghim bằng kim loại dùng để đóng miệng túi hoặc băng bó.
kim chỉ nam|Cái chỉ đường, mục tiêu quan trọng nhất cần hướng tới.
kim cúc|Loài hoa cúc nhỏ màu vàng.
kim cương|Khoáng vật cacbon rất cứng, khi mài thường dùng làm đá quý.
kim hoàn|Đồ trang sức làm bằng vàng, bạc hoặc các kim loại quý khác.
kim khí|Đồ dùng, công cụ được chế tạo từ kim loại.
kim loại màu|Tên gọi chung các kim loại không phải là sắt và hợp kim của chúng.
kim ngạch|Số tiền thu được từ việc bán hoặc mua hàng.
kim tiền|Tiền bạc nói chung hoặc đồng vàng dùng để thưởng công.
kìm hãm|Ngăn cản mạnh mẽ, không cho phát triển.
kín đáo|Không để người khác thấy rõ hoặc biết đến.
kín miệng|Nói chuyện kín đáo, giữ bí mật.
kín mít|Đóng kín hoàn toàn không có chỗ hở nào.
kinh doanh|Hoạch định mua bán nhằm kiếm tiền.
kinh điển|Được nhiều thế hệ xem là mẫu mực của một lĩnh vực.
kinh độ|Khoảng góc đo từ đường kinh tuyến gốc đến đường kinh tuyến đi qua địa điểm.
kinh ngạc|Cảm thấy bất ngờ đến mức không thể tin nổi.
kinh nghiệm|Hiểu biết rút ra nhờ từng làm hoặc từng trải qua một việc.
kinh phí|Tiền bạc dùng để chi trả cho công việc.
kinh tế|Tổng hợp các hoạt động tạo ra của cải và phân phối chúng.
kinh tế học|Khoa học nghiên cứu về sản xuất, phân phối và trao đổi của cải.
kính|Tấm vật liệu trong, thường lắp ở cửa cho ánh sáng đi qua.
kính áp tròng|Kính đeo sát mắt, không cần gọng, dùng để sửa tật khúc xạ.
kính chúc|Chúc mừng người khác với thái độ tôn trọng và thành kính.
kính hiển vi|Dụng cụ quang học dùng thấu kính phóng đại để nhìn vật nhỏ.
kính mắt|Vật đeo trước mắt để sửa tật, làm đẹp hoặc tránh nắng.
kính nể|Kính trọng và nể phục người khác.
kính ngữ|Từ ngữ dùng để gọi người lớn tuổi hoặc cấp trên.
kính phục|Kính trọng và phục tùng vì thấy người hoặc việc đó rất tốt.
kính râm|Kính có tròng sẫm giúp giảm lượng ánh sáng đi vào mắt.
kính thiên văn|Dụng cụ để quan sát các vật thể ở rất xa trên bầu trời.
kính trọng|Coi người khác đáng quý và thể hiện điều đó bằng thái độ lễ phép.
kính viễn vọng|Dụng cụ thu ánh sáng để quan sát vật ở rất xa.
kính yêu|Vừa quý mến vừa có lòng tôn trọng sâu sắc.
la bàn|Dụng cụ chỉ phương hướng, loại thông thường có kim nam châm.
la cà|Đi lang thang không mục đích rõ ràng.
la liệt|Nhiều thứ nằm rải rác khắp nơi, không sắp xếp thành hàng lối hay trật tự nào.
là lạ|Khác thường, không giống với những gì đã biết.
là lượt|Đẹp đẽ, sang trọng và quý phái.
lả tả|Nhiều người hoặc nhiều vật đi lại tấp nập.
lá bài|Mỗi tấm rời có ký hiệu trong bộ bài để chơi.
lá bánh|Lá dùng để gói bánh trước khi luộc chín.
lá cờ đầu|Người hoặc đơn vị tiên tiến nhất, làm mẫu mực cho mọi người.
lá dứa|Lá dài thơm của cây nếp, thường dùng ướp hương hoặc tạo màu xanh cho món ăn.
lạ đời|Khác thường, ít khi gặp trong đời sống.
lạ hoắc|Không quen thuộc, chưa từng gặp hoặc biết.
lạ lùng|Khác thường, khó hiểu hoặc gây ngạc nhiên.
lạ mặt|Người hoặc vật mà ta chưa từng gặp hoặc biết đến.
lạ tai|Nghe thấy âm thanh hoặc từ ngữ chưa từng biết.
lạ thật|Tiếng thốt lên khi thấy điều bất ngờ, kinh ngạc.
lạ thường|Khác thường đến mức khiến người ta ngạc nhiên.
lác đác|Có vài vật hoặc người xuất hiện thưa, cách xa nhau.
lạc đà|Thú cổ dài có bướu chứa mỡ, thích nghi với vùng khô hạn.
lạc điệu|Hát sai nhịp điệu hoặc hành động không phù hợp hoàn cảnh.
lạc hướng|Lạc đường, không biết đi đâu tiếp theo.
lạc loài|Bị tách khỏi đồng loại, bơ vơ không nơi nương tựa.
lạc quan|Tin rằng vẫn có triển vọng tốt dù đang gặp khó.
lạc thú|Sự vui thích, niềm vui đặc biệt mà người ta mong muốn được trải nghiệm.
lạch|Dòng nhỏ có nước chảy qua, thường thông ra sông hoặc biển.
lai rai|Phân nhỏ ra từng chút, trải dài qua nhiều thời điểm.
lãi gộp|Phần lợi còn lại sau khi trừ chi phí mua hàng.
lãi ròng|Số tiền thực tế thu về sau khi trừ hết các khoản chi.
lãi suất|Tỷ lệ phần trăm được tính toán dựa trên số tiền vay hoặc gửi tiết kiệm.
lái buôn|Người chuyên mua bán hàng hóa xa.
lái đò|Người chuyên chở khách và hàng trên sông bằng thuyền.
lái xe|Điều khiển phương tiện có bánh để đi trên đường.
lại giống|Hiện tượng con cháu có đặc điểm giống tổ tiên.
làm ăn|Làm việc để kiếm tiền nuôi sống bản thân.
làm bạn|Kết thân với nhau hoặc kết hôn làm vợ chồng.
làm cho|Gây ra, khiến cho sự vật hay sự việc xảy ra.
làm chủ|Nắm quyền quyết định hoặc điều khiển được việc đang làm.
làm chứng|Xuất hiện trước tòa để xác nhận sự việc.
làm cỗ|Chuẩn bị bữa ăn lớn để cúng hoặc ăn mừng.
làm công|Làm việc thuê mướn để nhận tiền lương từ người khác.
làm công ăn lương|Nhận tiền công bằng cách làm việc thuê.
làm dịu|Hành động làm giảm bớt sự căng thẳng hoặc gay gắt của tình thế.
làm gì|Hành động thực hiện việc gì đó.
làm giàu|Tích lũy tiền bạc, của cải để có nhiều hơn.
làm hỏng|Gây hư hại, làm mất giá trị.
làm lành|Làm cho mối quan hệ trở nên hòa thuận.
làm lợi|Hành động thực hiện để đạt được lợi ích cho bản thân hoặc tập thể.
làm nên|Thành công, tạo nên danh tiếng hoặc sự nghiệp lớn lao.
làm người|Sống và cư xử đúng mực, có đạo đức, xứng đáng với danh nghĩa là một con người.
làm ơn|Cách nhờ người khác giúp một việc một cách lịch sự.
làm phiền|Làm cho người khác cảm thấy khó chịu hoặc bận rộn không cần thiết.
làm quà|Làm để tặng người khác nhằm gây vui lòng hoặc ghi nhớ.
làm quen|Bắt đầu biết đến và tạo mối quan hệ thân thiện.
làm ra vẻ|Giả vờ hành xử như một người khác không phải bản thân.
làm rối|Gây ồn ào, làm mất trật tự chung.
làm ruộng|Cày cấy ruộng đất để sản xuất ra lương thực.
làm sáng tỏ|Hành động tìm hiểu, phân tích để làm rõ nguyên nhân, bản chất sự việc.
làm sao|Cách hỏi cần dùng phương pháp nào hoặc vì lý do gì.
làm thân|Tìm cách trở thành người quen biết thân thiết.
làm thinh|Không nói năng gì, giả vờ không biết sự việc.
làm tròn|Hoàn thành đầy đủ mọi nghĩa vụ hoặc nhiệm vụ đã giao.
làm việc|Dùng sức lực và trí tuệ để tạo ra kết quả có lợi cho bản thân hoặc xã hội.
làm vườn|Trồng và chăm rau, cây ăn quả hay hoa trong vườn.
lan man|Nói dài dòng, không đi vào trọng tâm vấn đề.
lan tràn|Phát triển nhanh, lan rộng ra nhiều nơi.
lan truyền|Truyền đi và lan rộng khắp nơi.
làn điệu|Giai điệu có nét riêng của một bài hay lối hát.
làn sóng|Nước biển dồn dập tạo thành từng lớp nhấp nhô.
lang thang|Đi đây đó mà không có điểm đến hay kế hoạch rõ ràng.
làng|Điểm cư trú truyền thống của cộng đồng nông thôn.
làng mạc|Khu dân cư nhỏ gồm nhiều nhà ở tập trung gần nhau.
làng xã|Khu dân cư gồm nhiều nhà ở tập trung gần nhau.
làng xóm|Khu dân cư gồm nhiều nhà ở gần nhau và người thân quen.
lảng tránh|Tránh né không muốn gặp hoặc không muốn nhắc đến.
lãng đãng|Bay lượn nhẹ nhàng, mờ ảo xa gần.
lãng mạn|Có tình cảm đẹp, mơ mộng và không thực tế lắm.
lãng phí|Sử dụng tiền bạc, thời gian hoặc công sức một cách vô ích.
lãng quên|Quên mất những việc cần phải làm hoặc chú ý.
láng giềng|Người sống ở nhà sát bên hoặc ở gần nhà.
lanh lẹ|Nhanh nhẹn, hoạt bát.
lanh lợi|Nhanh trí, thông minh và làm việc rất nhanh.
lành lặn|Chưa bị hư hỏng, rách nát hay tổn thương.
lành mạnh|Tốt cho sức khỏe và tinh thần.
lành nghề|Thường làm và hiểu rõ nghề nghiệp của mình.
lãnh đạm|Thờ ơ, không quan tâm hay biểu lộ cảm xúc trước chuyện gì.
lạnh|Có nhiệt độ thấp hoặc tạo cảm giác thiếu ấm.
lạnh buốt|Lạnh thấu xương, lạnh đến mức run rẩy.
lạnh giá|Lạnh đến mức rất khó chịu.
lạnh lẽo|Không có hơi ấm, thiếu sự gần gũi và thân thiết.
lạnh nhạt|Không thân mật, thiếu sự quan tâm ân cần.
lao động|Hoạt động có mục đích để tạo ra sản phẩm vật chất hoặc tinh thần.
lao lực|Làm việc vất vả bằng sức lực của cơ thể.
lao tâm|Sử dụng trí não làm việc vất vả, căng thẳng nhiều.
lao xao|Nhiều tiếng động nhỏ nổi lên cùng lúc, lúc rõ lúc mờ.
lão làng|Người lớn tuổi, làm việc lâu năm và có nhiều kinh nghiệm.
lão luyện|Thấm nhuần kỹ năng nhờ trải nghiệm lâu dài.
lạp xưởng|Món thịt xay tẩm ướp nhồi vào vỏ dài rồi làm khô.
lay động|Chuyển động rung nhẹ qua lại tại chỗ.
lắc đầu|Quay đầu sang hai bên để tỏ ý không đồng ý.
lắc lư|Động tác rung nhẹ hoặc nghiêng ngả qua lại liên tục.
lắm khi|Nhiều lúc, nhiều thời điểm.
lăn lóc|Làm việc say mê, tận tâm và chịu khó.
lăn lộn|Lăn đi lăn lại nhiều lần trên mặt đất hoặc vật khác.
lăn tăn|Gợn những nếp sóng nhỏ trên bề mặt nước.
lặn lội|Đi đường xa, gặp nhiều khó khăn và vất vả để làm việc.
lăng kính|Dụng cụ hình lăng trụ trong suốt, dùng để bẻ cong và tách ánh sáng thành nhiều màu.
lăng trụ|Hình khối có hai đáy song song và các mặt bên là hình bình hành.
lăng xăng|Làm việc tất bật, rối rít nhưng không đạt kết quả đáng kể.
lắng đọng|Chuyển từ trạng thái lỏng xuống đáy và dừng lại.
lắng nghe|Chú tâm nghe để hiểu rõ lời người nói.
lặng im|Không phát ra tiếng nói hay âm thanh.
lặng lẽ|Im lặng, không phát ra tiếng động và không cử động.
lắp bắp|Nói ngập ngừng, có tiếng bị lặp hoặc ngắt quãng.
lắp đặt|Gắn thiết bị vào vị trí đã chuẩn bị để có thể sử dụng.
lắp ráp|Ghép các bộ phận lại để máy hoạt động được.
lặp lại|Làm lại việc đã làm hoặc nói lại điều đã nói.
lặt vặt|Nhỏ bé, tầm thường, không quan trọng.
lâm nghiệp|Lĩnh vực trồng, chăm sóc, bảo vệ và sử dụng rừng.
lâm thời|Dùng tạm trong thời gian ngắn, chưa làm chính thức.
lầm lẫn|Trộn lẫn, hiểu sai sự việc này với sự việc kia.
lẩm bẩm|Nói nhỏ thành tiếng không rõ, thường như đang nói với chính mình.
lấm lem|Bị dính bẩn ở nhiều chỗ trên bề mặt.
lấm tấm|Có những chấm nhỏ nằm rải trên bề mặt.
lân cận|Nằm ở vị trí gần bên cạnh hoặc sát với nơi khác.
lân la|Dần dần đến gần một cách rụt rè.
lần lần|Từng bước, từ từ thay đổi hoặc trôi qua theo thời gian.
lần lượt|Làm theo thứ tự từ người này đến người kia.
lần mò|Tìm kiếm vật gì đó một cách vất vả, từng bước từng bước.
lẩn tránh|Cố gắng né tránh để không gặp hoặc không dính líu.
lẫn nhau|Hai bên đều có tác động lên nhau.
lận đận|Gặp nhiều trở ngại, làm việc vất vả không suôn sẻ.
lâng lâng|Cảm thấy nhẹ nhàng và khoan khoái.
lấp lánh|Ánh sáng lóe ra thành từng điểm nhỏ rồi tắt.
lập công|Làm việc có ích lớn cho xã hội.
lập giá|Quy định mức tiền và cách tính cho một món hàng.
lập lờ|Bập bồng trên mặt nước, lúc nổi lúc chìm.
lập luận|Trình bày lý lẽ để chứng minh hoặc bảo vệ quan điểm.
lập nghiệp|Tự xây dựng cơ nghiệp hoặc sự nghiệp riêng.
lập phương|Hình khối có sáu mặt bằng nhau, mỗi mặt đều là hình vuông.
lập trình|Viết các chỉ dẫn để máy tính thực hiện một nhiệm vụ.
lập trình viên|Người chuyên viết mã để máy tính hoạt động.
lật đật|Đồ chơi có phần đáy nặng, nghiêng đi rồi tự đứng lại.
lật ngửa|Đảo vật đang úp xuống để mặt trên hướng lên.
lâu bền|Kéo dài thời gian và giữ được sự vững chắc.
lâu đài|Tòa nhà lớn, đẹp và sang trọng thường có nhiều phòng.
lâu đời|Đã hình thành và tồn tại qua nhiều thế hệ.
lâu lâu|Thỉnh thoảng, không phải lúc nào cũng xảy ra.
lâu ngày|Đã qua một khoảng thời gian tương đối dài.
lầy lội|Nơi có nhiều bùn đất làm cho chân khó đi.
lấy chồng|Kết hôn với một người đàn ông để trở thành vợ của họ.
lấy lại|Thu hồi lại những gì đã mất hoặc thuộc về mình.
lấy lòng|Làm việc để gây thiện cảm, mong được vui lòng.
lấy nhau|Kết hôn, trở thành vợ chồng với nhau.
lẻ tẻ|Thưa thớt, rời rạc, không tập trung thành nhóm.
lẽ phải|Điều đúng theo đạo lý và lẽ thường.
lẽ ra|Đáng lẽ phải làm như vậy theo đúng lẽ phải hoặc quy định ban đầu.
lẽ thường|Chuyện thường xảy ra trong đời sống.
lem nhem|Bẩn dơ, không sạch sẽ hoặc không rõ ràng.
lén lút|Làm việc âm thầm, giấu kín và không công khai.
léng phéng|Quan hệ thân mật, không nghiêm túc hoặc thiếu đứng đắn giữa hai người.
leo lét|Ánh sáng yếu ớt, nhấp nháy như sắp tắt hẳn.
leo núi|Hoạt động leo trèo lên đỉnh núi.
leo trèo|Đi lên xuống các bậc thang hoặc cây cối.
lép vế|Ở vị trí thấp hơn nên bị người khác lấn át hoặc đè bẹp.
lề đường|Dải nằm sát mép phần đường chính cho xe đi.
lề lối|Phương pháp làm việc đã trở thành thói quen.
lề mề|Làm việc chậm chạp, không khẩn trương, kéo dài thời gian.
lễ độ|Thái độ lịch sự, tôn trọng và đúng mực trong giao tiếp.
lễ hội|Dịp cộng đồng tổ chức nghi thức và các hoạt động vui chung.
lễ lạt|Các ngày lễ hội và dịp vui chung.
lễ phép|Thái độ cư xử đúng mực, tôn trọng người lớn tuổi hoặc cấp trên.
lễ phục|Bộ quần áo chỉnh tề mặc trong các buổi lễ quan trọng.
lễ tân|Bộ phận tiếp nhận và hướng dẫn khách đến làm việc.
lễ tết|Thời điểm đi thăm hỏi nhau trong dịp Tết Nguyên Đán.
lệ phí|Khoản tiền nộp khi được cơ quan có thẩm quyền thực hiện một dịch vụ.
lệ thuộc|Phải tuân theo ý muốn của người khác.
lệch|Không nằm đúng phía, vị trí hoặc hướng dự kiến.
lên cao|Di chuyển theo hướng đi lên, cao hơn vị trí ban đầu.
lên cân|Thân thể tăng trọng lượng do sức khỏe tốt.
lên dây|Điều chỉnh chốt đàn để âm thanh vang đúng chuẩn.
lên đường|Bắt đầu hành trình rời khỏi nơi ở để đi xa.
lên lớp|Được chuyển sang lớp cao hơn sau khi hoàn thành năm học.
lên men|Quá trình biến đổi chất hữu cơ nhờ tác dụng của men.
lên tiếng|Cất tiếng nói lên để người khác biết hoặc thể hiện ý kiến.
lênh đênh|Trôi dạt trên mặt nước, không đứng yên ở một chỗ.
lềnh bềnh|Nổi trên mặt nước và bị sóng đẩy lên xuống liên tục.
lêu lổng|Lang thang không làm việc, không có mục đích rõ ràng.
lia lịa|Làm động tác liên tục rất nhanh không dừng.
lịch|Bảng sắp ngày, tuần và tháng để theo dõi thời gian.
lịch lãm|Có vẻ từng trải và biết cư xử nhã nhặn trong giao tiếp.
lịch sử|Những sự kiện đã xảy ra và để lại dấu vết trong quá khứ.
lịch trình|Kế hoạch cho biết khi nào và theo thứ tự nào các việc diễn ra.
liếc|Đưa mắt nhìn nhanh sang một phía.
liềm|Dụng cụ lưỡi cong cầm tay để cắt lúa hoặc cỏ.
liên bộ|Hai hay nhiều bộ ngành phối hợp cùng nhau thực hiện nhiệm vụ.
liên chi|Đơn vị hành chính hoặc đoàn thể được thành lập từ nhiều nhóm nhỏ hơn.
liên doanh|Hợp tác kinh doanh giữa hai hay nhiều bên cùng nhau.
liên đoàn|Tập hợp nhiều nhóm nhỏ cùng nhau thành một tổ chức lớn.
liên đội|Tổ hợp các đội nhỏ cùng hoạt động dưới một chỉ huy chung.
liên hệ|Giao tiếp hoặc tác động qua lại lẫn nhau giữa các sự vật.
liên hiệp|Gộp nhiều nhóm khác nhau thành một khối chung để cùng làm việc.
liên hoan phim|Sự kiện văn hóa chiếu phim mới và trao giải thưởng.
liên hợp|Tạo mối quan hệ gắn kết giữa các bộ phận vốn độc lập thành một thể thống nhất.
liên kết|Nối các phần riêng để chúng tạo thành một khối hoặc cùng hoạt động.
liên khu|Tập hợp nhiều vùng hành chính cùng quản lý chung.
liên lạc|Giao tiếp, trao đổi tin tức hoặc mệnh lệnh giữa các nơi.
liên miên|Kéo dài liên tục không có lúc dừng.
liên minh|Sự hợp sức của nhiều bên để cùng đạt mục tiêu.
liên quan|Có mối nối về ý nghĩa, nguyên nhân hay công việc với nhau.
liên tiếp|Nối liền nhau không có khoảng cách giữa các sự vật.
liên tỉnh|Kết nối giao thông giữa nhiều tỉnh với nhau.
liên tưởng|Nghĩ đến việc khác khi nhắc đến sự việc có liên quan.
liền|Sát ngay bên cạnh, không có khoảng ngăn cách.
liền kề|Nằm sát bên nhau, không có vật hay khoảng lớn xen giữa.
liệng|Bay lượn qua không trung theo một đường cong.
liệt kê|Việc ghi ra từng mục, từng hạng mục một cách lần lượt.
liêu xiêu|Ngả nghiêng, xiêu vẹo như sắp đổ hoặc ngã xuống.
liễu|Cây có lá dài hẹp và cành mềm rủ xuống.
linh cảm|Cảm giác tự nhiên trong người như biết trước điều sắp xảy ra.
linh dương|Thú ăn cỏ chân thon thuộc nhóm có móng guốc, thường chạy nhanh.
linh đình|Tổ chức lớn, sang trọng và có nhiều người tham gia.
linh động|Thay đổi linh hoạt, thích ứng nhanh với hoàn cảnh mới.
linh hoạt|Dễ uốn cong, thích ứng nhanh với hoàn cảnh.
linh kiện|Chi tiết máy có thể tháo rời, thay thế khi hỏng hóc.
linh tính|Cảm giác tự nhiên biết trước điều sắp xảy ra với mình.
lĩnh hội|Hiểu rõ và tiếp thu trọn vẹn kiến thức.
líu ríu|Âm thanh nhỏ, liên tiếp dính quyện khó phân biệt rạch ròi.
lo âu|Cảm thấy buồn rầu, hồi hộp và lo lắng một cách thường xuyên.
lo lắng|Không yên tâm vì nghĩ đến chuyện bất lợi có thể xảy ra.
lo liệu|Chuẩn bị, sắp xếp để làm việc tốt.
lo ngại|Lo lắng, e sợ điều gì đó xảy ra.
lo nghĩ|Cảm thấy lo lắng, suy nghĩ nhiều về một vấn đề nào đó.
lò ấp|Thiết bị tạo nhiệt và độ ẩm giúp trứng ấp nở.
lò dò|Đi từng bước chậm rãi, cẩn thận như lần từng bước chân.
lò rèn|Nơi dùng sức người để nung chảy và tạo ra đồ kim loại.
lò sưởi|Thiết bị tỏa nhiệt để giữ ấm cho không gian.
lò vi sóng|Thiết bị làm nóng thức ăn bằng sóng điện từ tần số cao.
lò xo|Bản thép mỏng uốn cong hoặc dây thép xoắn ốc, dễ trở lại hình cũ sau khi bị kéo hay nén, dùng để trữ lực.
loài|Nhóm sinh vật cùng loại theo cách phân chia sinh học.
loài người|Tập hợp toàn bộ con người sinh sống trên hành tinh này.
loại bỏ|Không giữ lại phần không cần hoặc không đạt yêu cầu.
loại hình|Nhóm các sự vật có những đặc điểm tương đồng.
loại từ|Từ như “con” hoặc “cái” đi cùng danh từ khi đếm hay xác định vật.
loãng|Có ít chất hòa tan hoặc ít phần đặc so với phần nước.
loáng thoáng|Chỉ thấy mờ mờ, lúc có lúc không, không rõ ràng.
loanh quanh|Chạy đi chạy lại, hoạt động trong một khu vực nhỏ hẹp.
loạt|Một dãy việc hay vật cùng loại nối tiếp nhau.
loay hoay|Làm việc vất vả, khó khăn và không suôn sẻ.
lon ton|Đi bộ nhanh nhẹn với những bước chân ngắn.
long lanh|Sáng trong và ánh lên khi có ánh sáng chiếu tới.
long nhãn|Thịt nhãn đã được phơi khô để làm quà.
long trọng|Trang nghiêm, cử hành với đầy đủ nghi thức trọng thể.
long vân|Cơ hội may mắn lớn đến với người.
lòng bàn chân|Phần dưới của bàn chân, không tính ngón chân.
lòng bàn tay|Mặt trong bàn tay lộ ra khi ta ngửa tay.
lòng chảo|Khoảng đất trũng rộng có địa hình cao hơn bao quanh.
lòng đất|Phần nằm sâu bên dưới bề mặt đất.
lòng đỏ|Phần màu vàng nằm ở giữa bên trong quả trứng.
lòng đỏ trứng|Phần trong trứng màu vàng, nằm giữa lòng trắng, chứa nhiều dinh dưỡng nuôi phôi.
lòng đường|Mặt đất giữa hai lề đường, dành riêng cho xe cộ lưu thông.
lòng sông|Phần đất thấp nằm giữa hai bên bờ của dòng nước chảy.
lòng thành|Ý nghĩ chân thành, thật thà và hết lòng với người khác.
lòng thòng|Đồ vật rủ xuống dài, rối rắm và không ngăn nắp.
lòng tin|Sự yên tâm rằng người hoặc điều mình dựa vào là đáng tin.
lòng tự trọng|Cách suy nghĩ về bản thân một cách đúng đắn, giữ gìn phẩm giá.
lòng vòng|Nói hoặc làm việc quanh co, không đi thẳng vào vấn đề chính.
lóng ngóng|Cử động vụng về vì chưa quen tay hoặc thiếu tự tin.
lót dạ|Ăn tạm một chút để giảm bớt cảm giác đói bụng.
lọt lòng|Nói trẻ em vừa mới sinh ra đời.
lô hội|Cây lá mọng chứa gel trong, thường còn gọi là nha đam.
lỗ chân lông|Khe nhỏ trên da giúp tiết mồ hôi và điều hòa nhiệt.
lỗ chỗ|Bề mặt có nhiều lỗ nhỏ hoặc vết thủng rải rác.
lỗ vốn|Thua tiền vốn, bị thiệt hại nặng về tài chính.
lộ diện|Hiện ra trước mắt người khác sau khi ẩn nấp.
lộ trình|Tuyến đường cụ thể cần đi qua để đến được nơi cần đến.
lôi cuốn|Thu hút khiến người ta muốn tham gia.
lôi kéo|Kéo người khác về phía mình để phục vụ.
lỗi hẹn|Không giữ đúng lời hứa hẹn đã đưa ra.
lỗi lạc|Vượt trội hẳn so với mọi người khác.
lỗi thời|Cũ kỹ, không còn phù hợp với thời đại hiện nay.
lối thoát|Phương cách hành động để thoát khỏi tình trạng khó khăn, nguy hiểm.
lối vào|Nơi bắt đầu để bước vào một không gian hoặc công trình nào đó.
lồm cồm|Di chuyển bằng cách dùng tay và chân, dáng vẻ vụng về.
lốm đốm|Có những chấm màu to nhỏ rải rác không đều.
lộn xộn|Không được sắp theo trật tự nên khó thấy rõ các phần.
lông bông|Lang thang không ở cố định, không chịu làm việc kiếm tiền.
lông lá|Lông nói chung, thường chỉ lông rậm rạp.
lông mao|Lông mềm mịn mọc trên da của động vật có vú.
lông mày|Đám lông mọc dày, dài trên phần mắt của con người.
lông măng|Lông tơ mềm mịn bao phủ cơ thể thai nhi hoặc trẻ sơ sinh.
lông mi|Hàng lông ngắn mọc dọc theo mí mắt.
lông nách|Mái tóc mọc ở nách người lớn.
lông vũ|Lông bao phủ cơ thể chim, giúp giữ ấm và bay lượn.
lồng đèn|Đèn giấy nhiều mặt kính, dùng để trang trí hoặc chiếu sáng.
lồng lộng|Không khí thổi mạnh và rộng rãi, không bị cản trở.
lồng ngực|Phần thân giữa hai vai, nằm trong lồng xương sườn bảo vệ tim phổi.
lơ là|Không để tâm đúng mức đến việc mình cần làm.
lờ mờ|Chỉ hiện ra không rõ nét, như khi ánh sáng còn yếu.
lỡ cơ|Bỏ lỡ dịp tốt hoặc cơ hội thuận lợi.
lời chúc|Những mong muốn tốt đẹp dành cho người khác.
lời hứa|Điều đã nói ra để cam kết mình sẽ thực hiện.
lời khuyên|Ý kiến, đề nghị để người khác cân nhắc làm theo.
lời lẽ|Cách dùng từ và nội dung của những gì được nói ra.
lời nói|Những âm thanh phát ra từ miệng để truyền đạt ý nghĩ.
lời văn|Cách dùng từ, câu để diễn đạt ý nghĩa trong văn bản.
lợi hại|Mặt tốt và mặt xấu, những điều có lợi và có hại.
lợi ích|Những điều mang lại lợi thế, giúp ích hoặc thỏa mãn nhu cầu.
lợi lộc|Lợi ích vật chất và tiền bạc thu về.
lợi suất|Lợi nhuận thu được tính theo tỷ lệ phần trăm.
lợi thế|Điều kiện tốt hơn người khác trong cùng hoàn cảnh.
lợi tức|Số tiền lãi nhận được từ việc cho vay hoặc gửi tiết kiệm.
lớn lao|Quan trọng, cao cả, có tầm vóc rộng lớn.
lớn tiếng|Nói với âm lượng lớn, giọng cao.
lớn tuổi|Đã qua tuổi trưởng thành hoặc trẻ em sắp lớn.
lu mờ|Giảm dần độ sáng hoặc suy giảm giá trị, vị thế.
lũ lượt|Di chuyển nối tiếp nhau thành từng nhóm đông đúc.
lúa chiêm|Lúa được gieo trồng và thu hoạch vào mùa xuân.
lúa mạch|Cây ngũ cốc có bông mang hạt dùng làm thực phẩm và mạch nha.
lúa mùa|Lúa trồng và thu hoạch vào mùa mưa.
luân canh|Trồng nối tiếp những loại cây khác nhau trên cùng một mảnh đất.
luân chuyển|Di chuyển tuần tự từ nơi này sang nơi khác.
luẩn quẩn|Chạy vòng vo mãi không thoát ra khỏi chỗ cũ.
luận án|Công trình nghiên cứu được trình bày để xét cấp học vị, thường là tiến sĩ.
luận chứng|Dấu hiệu thực tế dùng để bảo vệ cho một ý kiến.
luận đề|Chủ đề được nêu ra để mọi người cùng trao đổi, bàn bạc.
luận điểm|Ý kiến chính, lập trường cốt lõi trong cuộc tranh luận.
luận giải|Bàn bạc, phân tích để tìm ra lẽ phải, làm sáng tỏ vấn đề.
luận thuyết|Bài văn hoặc lời nói phân tích, bàn bạc về một chủ đề.
luận văn|Bài nghiên cứu chuyên sâu trình bày kết quả khảo cứu khoa học.
luật|Hệ thống quy tắc có hiệu lực bắt buộc trong xã hội.
luật chơi|Tập hợp các quy tắc cụ thể hoặc ngầm hiểu mà mọi người trong cuộc chơi phải cùng tuân theo.
luật định|Quy tắc cụ thể do nhà nước ban hành để điều chỉnh hành vi.
luật gia|Người chuyên nghiên cứu và làm việc trong lĩnh vực pháp luật.
luật học|Ngành học chuyên nghiên cứu về các quy tắc và chế độ nhà nước.
luật lệ|Tập hợp các quy định và lề lối đã được mọi người quen thuộc và tuân theo.
luật pháp|Tổng hợp các quy tắc bắt buộc do nhà nước ban hành và bảo đảm thực hiện.
lúc lắc|Đưa vật này sang vật kia một cách nhanh chóng.
lúc lỉu|Nhung nhão, rủ xuống không thẳng tắp.
lúc nhúc|Nhiều người hoặc vật di chuyển liên tục, chen chúc.
lục địa|Mảng đất liền lớn trên Trái Đất, bị bao quanh bởi các đại dương.
lục giác|Hình học có sáu góc và sáu cạnh bằng nhau.
lục soát|Tìm kiếm kỹ lưỡng từng ngóc ngách để kiểm tra, khám xét xem có gì giấu kín.
lui tới|Đi lại thường xuyên, quen thuộc một nơi.
lủi thủi|Đi lại hoặc ở một mình với vẻ cô đơn, buồn rầu.
lúi húi|Cúi đầu chăm chú làm việc, không để ý đến xung quanh.
lụi cụi|Làm việc vất vả, chịu khó với tâm thế kiên trì.
lung lay|Bắt đầu lỏng lẻo hoặc rung chuyển ngả nghiêng.
lúng túng|Không biết làm thế nào cho phải, bối rối vì không chủ động được tình hình.
luôn luôn|Luôn xảy ra hoặc thường xuyên xuất hiện.
luống|Dải đất vun dài để gieo cây theo hàng.
luống cuống|Mất bình tĩnh, vụng về, làm việc không khéo léo.
luống tuổi|Đến giai đoạn tuổi đời đã khá cao.
lụp xụp|Thấp bé, cũ nát và lộn xộn.
lụt lội|Bị ngập nước do mưa lớn hoặc nước dâng.
luyến tiếc|Cảm thấy buồn bã, thương tiếc khi nhớ lại điều đã qua.
luyện|Làm đi làm lại để ngày càng thành thạo.
luyện kim|Cách chế biến quặng để tách ra các kim loại cần thiết.
luyện tập|Làm đi làm lại nhiều lần để rèn kỹ năng cho thuần thục.
luyện tinh|Quá trình đun nóng chất lỏng để tách lấy phần tinh khiết nhất.
lữ hành|Đi xa qua nhiều nơi, thường nói về hoạt động du lịch.
lữ khách|Người đi đường xa, thường là người lữ hành.
lửa trại|Đống lửa nhóm ngoài trời để mọi người quây quần khi cắm trại.
lứa tuổi|Độ tuổi của những người sinh ra trong cùng một năm hoặc thời gian gần nhau.
lựa chọn|Xem xét nhiều khả năng rồi giữ lại phương án mình muốn.
lực kế|Dụng cụ dùng để đo độ lớn của lực tác động.
lực lượng|Tổng hợp sức mạnh có thể gây ra tác động đáng kể đến sự vật hay con người.
lưng|Phía sau thân người, từ vai tới vùng thắt eo.
lừng danh|Được nhiều người biết đến và ca ngợi vì danh tiếng.
lững thững|Bước đi chậm rãi như không có gì phải vội.
lược|Vật có dãy răng để gỡ rối và sửa tóc.
lược dịch|Viết lại nội dung từ ngôn ngữ khác nhưng không giữ nguyên từng câu.
lười biếng|Không thích làm việc, lười nhác, ít năng động.
lưới|Tấm đan nhiều mắt trống, có thể giăng ra để bắt cá.
lượm|Nhặt một vật đang ở dưới đất lên.
lượm lặt|Nhặt từng chút nhỏ, thu thập những thứ vụn vặt.
lươn|Cá nước ngọt thân dài trơn, thường sống dưới bùn.
lương duyên|Cuộc hôn nhân may mắn, thuận hòa và hạnh phúc.
lương tâm|Cảm giác bên trong giúp tự xét mình đúng hay sai.
lương thiện|Có đạo đức, làm việc tốt và tuân theo pháp luật.
lương thực|Thức ăn chính làm từ ngũ cốc như gạo, ngô.
lương tri|Khả năng tự nhiên phân biệt đúng sai và biết điều thiện ác.
lưỡng lự|Do dự, cân nhắc kỹ lưỡng giữa các lựa chọn.
lượng tử|Đơn vị nhỏ nhất của năng lượng khi trao đổi.
lướt|Di chuyển nhẹ và nhanh sát trên một bề mặt.
lướt sóng|Môn thể thao trượt ván trên mặt sóng biển.
lướt ván|Đứng hoặc nằm trên ván để di chuyển trên mặt nước.
lưu danh|Để lại tên tuổi và tiếng thơm cho đời sau nhớ mãi.
lưu diễn|Di chuyển đến nhiều nơi khác nhau để biểu diễn cho công chúng.
lưu động|Di chuyển từ nơi này sang nơi khác liên tục.
lưu hành|Phổ biến và lan rộng trong cộng đồng.
lưu huỳnh|Nguyên tố phi kim thường gặp dưới dạng chất rắn màu vàng.
lưu luyến|Yêu thương sâu sắc, không muốn rời.
lưu lượng|Lượng nước, khí hay hàng đi qua một chỗ tính theo thời gian.
lưu tâm|Dành sự chú ý cho điều cần nhớ hoặc cần giải quyết.
lưu thông|Đi lại hoặc vận chuyển thông suốt qua một hệ thống.
lưu truyền|Trao lại qua nhiều người hoặc nhiều thế hệ.
lưu trữ|Giữ tài liệu hoặc dữ liệu để có thể tìm lại lâu dài.
lưu vực|Vùng đất mà nước từ đó chảy về một con sông chính.
lưu ý|Gợi người ta chú tâm đến điều quan trọng.
ma sát|Lực cản xuất hiện khi hai bề mặt trượt lên nhau.
mà cả|Thương lượng để mua hàng với giá thấp hơn.
mà thôi|Chỉ có vậy, không thêm gì nữa.
mã hiệu|Ký hiệu riêng biệt dùng để nhận dạng từng loại sản phẩm công nghiệp.
mã lực|Đơn vị đo công suất, tương đương sức kéo của một con ngựa.
mã não|Đá cứng có vân nhiều màu, dùng làm đồ trang sức hoặc cối giã.
mã nguồn|Mã chứa lệnh để máy tính thực thi.
mã số|Dãy số hoặc ký hiệu dùng để nhận dạng và phân loại.
mã vạch|Dấu sọc đen trắng ghi mã để máy quét đọc thông tin.
mách nước|Chỉ cách làm hoặc mẹo nhỏ giúp việc gì đó thành công.
mạch|Đường dẫn cho dòng điện chạy qua các linh kiện.
mạch lạc|Các bộ phận liên kết chặt chẽ, không rời rạc.
mạch nha|Chất ngọt sánh thu từ tinh bột nhờ men của hạt nảy mầm.
mai một|Dần mất đi vì ít còn được dùng hay lưu truyền.
mai sau|Thời điểm ở tương lai, những ngày tháng còn lại phía trước.
mài giũa|Làm cho sắc bén hơn qua rèn luyện.
mải mê|Tập trung cao độ vào việc gì đến mức quên hết mọi thứ khác.
mải miết|Tâm trí tập trung vào việc làm đến mức quên hết mọi thứ xung quanh.
mái chèo|Thanh có bản dẹt, quạt nước để đẩy thuyền.
mái hiên|Phần mái nhô khỏi tường để che khoảng trước cửa.
mái nhà|Lớp vật liệu che phủ trên đỉnh để bảo vệ nhà.
mái tóc|Toàn bộ tóc trên đầu khi nhìn như một thể.
màn ảnh|Mặt phẳng sáng dùng để hiển thị hình ảnh trong rạp chiếu phim.
màn bạc|Màn chiếu phim, nơi trình chiếu các bộ phim điện ảnh.
màn cửa|Tấm vải treo ở ô cửa để che sáng hoặc tạo chỗ kín.
màn hình|Bề mặt hiển thị chữ và hình của thiết bị điện tử.
mãn nguyện|Hạnh phúc vì mọi điều mong muốn đều được thực hiện trọn vẹn.
mạn phép|Cách nói lịch sự khi xin được làm một việc.
mang lại|Gây ra kết quả tốt hoặc xấu cho một sự việc nào đó.
màng nhĩ|Màng mỏng nằm sâu trong tai, ngăn cách hai khoang tai.
mãng cầu|Cây ăn quả có trái to, thịt nhiều nước và vị ngọt đậm.
máng xối|Máng dẫn nước mưa từ nơi hai mái nhà gặp nhau.
mạng lưới|Hệ thống các đường dây hoặc lối đi nối kết với nhau.
mạng máy tính|Các máy và thiết bị kết nối để trao đổi dữ liệu.
mạng nhện|Lưới tơ mỏng do nhện giăng ra để bắt mồi ăn.
mạng xã hội|Dịch vụ trực tuyến để mọi người kết nối và chia sẻ nội dung.
manh mối|Dấu hiệu giúp tìm ra nguyên nhân hoặc kết quả của việc gì.
manh nha|Mới có dấu hiệu đầu tiên, vừa bắt đầu hình thành.
mành|Tấm che bằng các nan hoặc sợi, thường treo trước cửa.
mảnh khảnh|Gầy gò nhưng có dáng người cao ráo.
mảnh mai|Mỏng manh, yếu đuối nhưng dễ thương.
mảnh vụn|Những phần nhỏ rời rạc của đồ vật hoặc thức ăn bị vỡ.
mãnh liệt|Mạnh mẽ đến mức dữ dội, gây ấn tượng mạnh.
mạnh mẽ|Có sức mạnh lớn hoặc ý chí kiên định.
mào đầu|Phần mở đầu dùng để dẫn dắt vào nội dung chính.
mạo muội|Dám làm việc khó khăn mà không chắc chắn thành công.
mạo từ|Từ đứng trước danh từ số ít để xác định tính đếm được.
mát lòng|Tâm hồn thấy dễ chịu, vừa ý.
mát tay|Làm việc thành thạo, gặp việc gì cũng làm được.
mạt cưa|Vụn gỗ nhỏ rời ra khi dùng cưa xẻ gỗ.
mau chóng|Hoàn thành hoặc diễn ra trong quãng thời gian ngắn.
mau lẹ|Làm việc nhanh chóng và không chậm trễ.
mau mắn|Làm việc nhanh chóng, không chậm trễ.
màu mè|Tô vẽ nhiều màu sắc cho đẹp.
màu mỡ|Đất có nhiều chất dinh dưỡng giúp cây trồng phát triển tốt.
màu sắc|Đặc tính riêng biệt của ánh sáng tạo nên vẻ ngoài của vật.
may mà|Mở đầu lời nói về điều thuận lợi đã giúp tránh một kết quả xấu.
may mặc|Việc tạo ra quần áo, trang phục để mặc.
may ra|Có chút hy vọng mong manh, khả năng xảy ra không chắc chắn.
may sao|May mắn một cách bất ngờ.
may sẵn|May quần áo theo số đo chung cho nhiều người thay vì đo riêng từng người.
mày mò|Cố gắng tìm hiểu kỹ lưỡng từng chi tiết nhỏ.
máy ảnh|Thiết bị thu ánh sáng để ghi lại ảnh tĩnh.
máy bán hàng|Thiết bị tự động bán hàng hóa sau khi khách hàng trả tiền.
máy bay|Phương tiện có thể bay để chở người hoặc hàng trên không.
máy bay trực thăng|Phương tiện bay có thể đứng yên hoặc di chuyển thẳng đứng.
máy bộ đàm|Thiết bị cầm tay dùng để liên lạc bằng sóng vô tuyến.
máy bơm|Thiết bị dùng điện để hút và đẩy nước hoặc chất lỏng khác di chuyển.
máy cày|Thiết bị cơ giới dùng để cày xới đất.
máy chiếu|Thiết bị rọi hình ảnh lên màn hoặc tường cho nhiều người xem.
máy chủ|Thiết bị điện tử trung tâm xử lý yêu cầu của máy khác.
máy công cụ|Thiết bị dùng năng lượng để thay thế sức lao động của con người trong việc thực hiện công việc.
máy điện|Thiết bị tạo ra hoặc sử dụng năng lượng điện.
máy giặt|Thiết bị làm sạch quần áo bằng nước và chuyển động cơ học.
máy hút bụi|Thiết bị điện dùng để hút bụi bẩn và rác nhỏ.
máy in|Thiết bị chuyển chữ hoặc hình từ dữ liệu ra giấy.
máy kéo|Xe dùng sức kéo để vận hành máy móc hoặc kéo xe khác.
máy khách|Máy tính gửi yêu cầu tới máy chủ để dùng dữ liệu hay dịch vụ.
máy khâu|Thiết bị cơ khí dùng để khâu nối các mảnh vải hoặc da thành quần áo.
máy khoan|Thiết bị quay mũi cắt để tạo lỗ trên vật liệu.
máy lạnh|Thiết bị làm mát không khí và giữ độ ẩm thích hợp trong phòng kín.
máy may|Thiết bị dùng kim và chỉ để ráp vải bằng đường khâu.
máy móc|Tên gọi chung các thiết bị có cơ cấu làm việc giúp con người.
máy nổ|Động cơ tạo chuyển động nhờ nhiên liệu cháy bên trong xilanh.
máy phát điện|Thiết bị tạo ra dòng điện để cung cấp năng lượng.
máy sưởi|Thiết bị dùng để tạo nhiệt làm ấm không gian.
máy thu thanh|Thiết bị dùng để bắt sóng và nghe các chương trình phát thanh.
máy tính|Thiết bị xử lý dữ liệu và chạy chương trình theo lệnh.
máy tính cá nhân|Máy tính điện tử dùng cho nhu cầu riêng của từng người.
máy tính để bàn|Máy tính thiết kế để đặt cố định trên bàn khi dùng.
máy tính xách tay|Loại máy tính nhỏ gọn, dễ mang theo người.
máy trạm|Thiết bị điện tử dùng để xử lý dữ liệu với cấu hình mạnh hơn máy tính thường.
máy ủi|Thiết bị chạy động cơ, có thiết bị ở trước để san phẳng mặt đất.
máy vi tính|Thiết bị điện tử dùng để xử lý số liệu và điều khiển hoạt động.
máy xay sinh tố|Dụng cụ điện dùng để xay nhuyễn trái cây, rau củ làm sinh tố.
máy xúc|Thiết bị cơ giới dùng để đào và di chuyển đất đá.
mắc áo|Vật có móc để treo quần áo cho khỏi nhăn.
mắc nợ|Phải trả tiền cho người khác vì đã mượn.
mặc dù|Dù có điều kiện không thuận lợi nhưng vẫn làm tiếp.
mặc định|Được đặt sẵn, tự động áp dụng khi không có ai thay đổi.
mặc kệ|Bỏ qua, không quan tâm hay để ý đến người hay việc gì.
mặc nhiên|Thỏa thuận ngầm mà không cần nói ra bằng lời.
mặc sức|Làm việc theo ý muốn, không ai cấm cản.
mắm ruốc|Mắm làm từ những con ruốc nhỏ ủ với muối.
mắm tôm|Chế phẩm làm từ tôm tép, để lâu cho thịt tôm tan ra.
mặn mà|Có nét đằm và duyên khiến người khác thấy dễ mến.
mặn mòi|Vị muối đậm đà, thường dùng để tả nước biển hoặc thực phẩm.
măng|Chồi non của cây tre, thường được hái về nấu.
măng cụt|Quả có vỏ tím dày, bên trong chia múi trắng mềm.
măng tây|Rau ăn phần chồi non hình mũi giáo nhô khỏi mặt đất.
mắt bão|Vùng trung tâm của cơn bão nơi gió nhẹ và trời quang.
mắt cá|Hai chỗ xương gồ lên ở hai bên cổ chân.
mặt bằng|Diện tích mặt đất trống hoặc không gian bên trong dùng để xây dựng nhà cửa, nhà xưởng.
mặt cắt|Hình vẽ thể hiện các đường viền của vật thể trên mặt phẳng cắt ngang.
mặt chữ|Hình dáng nét vẽ của ký tự viết tay hoặc in ấn.
mặt đất|Bề mặt phần đất nơi người và vật có thể đứng.
mặt đường|Bề mặt phẳng của con đường để xe và người đi lại.
mặt hàng|Một chủng loại sản phẩm được đưa ra bán.
mặt mũi|Cái mặt người, biểu tượng cho thể diện.
mặt nạ|Vật đeo che toàn bộ hoặc một phần khuôn mặt.
mặt nước|Bề mặt nơi nước chảy hoặc đọng lại.
mặt sắt|Vẻ mặt nghiêm nghị, lạnh lùng không chút biểu cảm.
mâm xôi|Cây bụi cho quả gồm nhiều múi nhỏ mọng nước kết sát nhau.
mầm non|Chồi mới nhú, còn mềm và đang bắt đầu phát triển.
mẫn cán|Cần cù, hăng hái và làm việc hiệu quả.
mấp máy|Cử động nhẹ nhàng và liên tiếp.
mấp mé|Đến sát ngay bên cạnh một ranh giới hoặc mức độ nhất định.
mấp mô|Bề mặt gồ ghề, không phẳng mịn.
mất hồn|Ngẩn ngơ, mất tập trung khiến trí óc không hoạt động.
mật độ|Mức độ dày đặc của người hoặc vật trong một khu vực.
mật hoa|Chất lỏng ngọt do hoa tiết ra, thu hút ong và nhiều côn trùng khác.
mật khẩu|Mã bí mật gồm các ký tự, dùng để xác minh danh tính khi truy cập hệ thống.
mật mã|Mã bí mật dùng để mã hóa hoặc giải mã thông tin.
mật ong|Chất ngọt sánh do ong tạo ra từ mật hoa.
mật thiết|Gần gũi, gắn bó khăng khít không thể tách rời nhau.
mâu thuẫn|Tình trạng hai ý kiến hoặc sự việc trái ngược nhau.
mẫu đơn|Biểu mẫu soạn sẵn để người làm đơn điền thông tin.
mẫu giáo|Trường học dành cho trẻ em từ 3 đến 6 tuổi để chuẩn bị vào lớp một.
mẫu hệ|Dòng họ tính theo mẹ.
mẫu mã|Kiểu dáng, mẫu hình hoặc quy cách bên ngoài của sản phẩm hàng hóa.
mẫu số|Số ở dưới gạch ngang trong phép chia phân số.
mẫu vật|Vật mẫu dùng để nghiên cứu, phân tích hoặc làm chuẩn so sánh.
mấu chốt|Điểm quan trọng nhất, quyết định kết quả của vấn đề cần giải quyết.
mậu dịch|Hoạt động mua bán và trao đổi hàng hóa giữa các bên.
mè xửng|Loại bánh kẹo mềm, rắc hạt vừng trắng lên bề mặt.
mẹ kế|Vợ của người chồng mà người phụ nữ đó không phải là vợ chính thức.
mẹ nuôi|Người đàn bà nhận nuôi và chăm sóc trẻ không phải con ruột.
mèo rừng|Thú hoang thuộc họ mèo, vóc gần mèo nhà và thường có lông đốm.
méo xệch|Hình dạng bị lệch, không cân đối.
mét vuông|Diện tích của hình vuông có cạnh dài một mét.
mê cung|Nơi có nhiều lối đi quanh co khiến người ta khó tìm đường ra.
mê đắm|Say mê đến mức không thể rời bỏ.
mê mẩn|Say mê đến mức mất đi sự tỉnh táo bình thường.
mề gà|Dạ dày con gà; hoặc túi da buộc thắt lưng đựng tiền.
mềm mại|Mềm dịu, uyển chuyển và dễ chịu về hình dáng hay âm thanh.
mềm mỏng|Nói chuyện, cư xử nhẹ nhàng, không cứng nhắc hay gây khó chịu.
mềm nhũn|Mềm yếu đến mức không giữ được hình dáng hay sức lực.
mềm yếu|Thiếu ý chí kiên định, dễ dàng đầu hàng trước khó khăn.
mến phục|Yêu quý và nể phục đối phương.
mến yêu|Yêu thương với tình cảm gắn bó sâu sắc.
mênh mông|Rộng lớn vô tận, lan ra khắp nơi không thấy hết được.
mệnh danh|Gọi tên một người hoặc sự vật theo cách gọi đó.
mệnh đề|Đoạn câu có cấu trúc ngữ pháp hoàn chỉnh để diễn đạt một ý riêng.
mệnh giá|Số tiền ghi trên tiền giấy, tiền xu hoặc tem thư.
mệnh lệnh|Lời bảo buộc phải làm việc gì đó.
mệt lử|Mệt mỏi đến mức không thể vận động thêm được.
mệt mỏi|Cảm thấy kiệt sức, không còn muốn vận động cơ thể hay tinh thần.
mệt nhoài|Mệt mỏi đến mức không còn sức lực để làm gì thêm.
mệt nhọc|Cảm thấy cơ thể thiếu năng lượng và uể oải.
mỉa mai|Nói với giọng mỉa, nói ngược lại ý thật để chế giễu.
miên man|Kéo dài không dứt, lan rộng ra mãi.
miễn cưỡng|Làm việc với tâm trạng không vui, không muốn.
miễn là|Từ nối nêu điều kiện đủ để điều đang nói có thể thực hiện.
miễn phí|Không bắt buộc phải trả tiền để được sử dụng dịch vụ.
miễn thuế|Không bắt buộc phải nộp tiền thuế cho nhà nước.
miến|Sợi thực phẩm khô làm từ tinh bột, mềm trong nước nóng.
miệng|Nơi thức ăn đi vào cơ thể khi ta ăn.
miết|Ấn tay hoặc dụng cụ rồi kéo sát dọc bề mặt.
miệt mài|Trạng thái tập trung cao độ vào việc làm đến mức quên hết mọi thứ khác.
miêu tả|Dùng lời nói hoặc hình ảnh để người khác thấy rõ hình dáng, tâm trạng.
mỉm cười|Hơi cong khóe môi để biểu lộ niềm vui, không bật thành tiếng.
minh bạch|Rõ ràng, dễ thấy và không có gì che giấu.
minh mẫn|Sáng suốt, tinh nhanh và không nhầm lẫn.
mình|Từ người nói dùng để tự xưng một cách thân mật.
mịt mùng|Không phân biệt rõ, tối sầm cả tầm nhìn.
mò mẫm|Tìm kiếm bằng cách sờ tay vào vật.
mỏ hàn|Dụng cụ sắt nóng đỏ dùng để làm chảy kim loại hàn gắn các vật khác.
mỏ lết|Dụng cụ dùng để vặn ốc, có thể thay đổi kích thước để phù hợp nhiều loại.
mỏ neo|Dụng cụ sắt nặng có móc cong, thả xuống đáy nước để giữ tàu thuyền cố định.
móc câu|Lưỡi kim loại nhỏ uốn cong, gắn vào dây để câu cá.
mỏi mắt|Mong chờ điều gì đó đã lâu mà vẫn chưa đến.
mỏi nhừ|Mệt mỏi đến mức không thể chịu đựng thêm được nữa.
mọi nơi|Tất cả mọi địa điểm, mọi chỗ.
mon men|Di chuyển từng bước nhỏ một cách thận trọng để lại gần.
món ăn|Thức ăn đã được chế biến chín theo một cách thức riêng biệt.
mong đợi|Hy vọng điều mong muốn sẽ xảy ra.
mong manh|Dễ rách, dễ vỡ hoặc khó giữ được lâu.
mong mỏi|Mong muốn điều gì đó rất tha thiết.
mong muốn|Muốn có và hy vọng đạt được điều mong đợi.
mong ước|Muốn có được điều gì đó một cách rất tha thiết.
mỏng dính|Mỏng rất nhiều, không dày.
mỏng tang|Mỏng manh, ít ỏi, không dày dặn.
móng|Lớp cứng ở đầu mỗi ngón tay hoặc ngón chân.
mọt sách|Người chỉ biết đọc sách, ít quan tâm đến thực tế.
mô hình|Vật nhỏ giống hình thật, dùng để nghiên cứu hoặc trưng bày.
mô liên kết|Chất nền giữa các tế bào giúp nâng đỡ và giữ cơ quan.
mô phỏng|Làm theo hình dáng, cách thức của mẫu để giả lập lại.
mô thức|Mẫu hình hoặc cách thức được dùng làm chuẩn mực để bắt chước.
mô tơ|Thiết bị dùng để sinh ra lực kéo hoặc lực đẩy cho máy móc hoạt động.
mồ hôi|Chất lỏng trong suốt tiết ra từ lỗ chân lông trên da.
mộc bản|Bản khắc chữ bằng gỗ dùng để in ấn sách báo.
mộc lan|Loài cây lớn có hoa màu trắng và tỏa hương thơm ngào ngạt.
mộc nhĩ|Nấm mỏng hình tai, mọc trên gỗ và thường dùng trong món ăn.
môi giới|Người làm trung gian để hai bên gặp nhau.
môi trường|Không gian bao quanh nơi sinh sống và hoạt động.
mỗi một|Chỉ riêng một cái, một người hoặc một việc.
mối hàng|Người mua bán thường xuyên, có quan hệ quen thuộc với nhau.
mông lung|Mờ mờ, không rõ ràng, khó xác định cụ thể.
mộng tưởng|Ước mơ xa vời, không thể thực hiện được trong thực tế.
một chút|Một lượng nhỏ, một phần ít ỏi, không đáng kể trong tổng thể.
một lần|Chỉ một hành động hoặc sự việc duy nhất, không lặp lại.
một lòng|Chung chí hướng, không đổi lòng trước sau.
một lúc|Chỉ khoảng thời gian ngắn hoặc một thời điểm cụ thể.
một mạch|Làm việc liên tục không dừng nghỉ giữa chừng.
một mình|Chỉ duy nhất bản thân, không có người nào khác cùng tham gia.
một mực|Dứt khoát giữ nguyên ý định, không đổi trước sau.
một số|Chỉ con số không xác định, thường là vài cái trong tổng số.
một thể|Cùng một lúc, không tách rời.
một vài|Số lượng ít, chỉ một hoặc vài cái, không nhiều.
mơ mộng|Để trí tưởng tượng hướng tới những điều đẹp hoặc xa thực tế.
mơ tưởng|Hình dung và mong tới điều mình chưa có trong thực tế.
mơ ước|Mong điều tốt đẹp chưa có sẽ thành hiện thực.
mở đầu|Khởi đầu cho một công việc hay chuỗi sự kiện.
mở đường|Làm việc đầu tiên để tạo điều kiện cho người khác.
mở hàng|Thực hiện giao dịch mua hoặc bán lần đầu tiên trong ngày.
mở màn|Khởi động buổi biểu diễn trên sân khấu.
mở mang|Làm cho kiến thức hoặc phạm vi hoạt động trở nên rộng hơn.
mở máy|Bật công tắc để thiết bị bắt đầu hoạt động.
mở mắt|Đã tỉnh giấc và bắt đầu làm việc ngay buổi sáng sớm.
mở rộng|Làm cho phạm vi hoặc quy mô trở nên lớn hơn.
mở toang|Mở cửa hoặc vật ra hết cỡ.
mời mọc|Kêu gọi người khác đến hoặc làm việc một cách chân thành.
mới đây|Xảy ra trong thời gian vừa qua.
mới hay|Biết được sự thật sau khi trải qua hoặc chứng kiến.
mới lạ|Được tạo ra gần đây hoặc chưa từng xuất hiện trước đây.
mới mẻ|Vừa xuất hiện vừa chưa ai biết rõ.
mới rồi|Gần đây, trong khoảng thời gian vừa qua.
mới tinh|Vật còn mới, chưa từng được sử dụng hoặc dùng ít.
mơn mởn|Cỏ cây xanh non và mềm mại.
mơn trớn|Vuốt nhẹ để thể hiện sự trìu mến.
mu bàn tay|Phần thịt ở giữa lòng bàn tay, không tính các ngón.
mù mịt|Không nhìn thấy rõ vì tối hoặc bị che khuất.
mù mờ|Không thấy rõ, thiếu sáng hoặc không hiểu rõ sự vật.
mù tịt|Không nhìn thấy gì, không hiểu biết gì cả.
mũ lưỡi trai|Mũ có phần vành cứng nhô ra trước để che mắt.
mũ nồi|Mũ mềm, dẹt, dáng tròn, thường đội hơi nghiêng.
mũ phớt|Mũ vành mềm làm bằng dạ hoặc vật liệu có dáng tương tự.
mua hàng|Trao tiền để nhận lại các món đồ cần thiết.
mua lẻ|Mua từng cái một thay vì mua theo số lượng lớn.
mua sắm|Đi mua các vật dụng cần thiết để sử dụng trong đời sống.
mùa đông|Mùa lạnh nhất trong chu kỳ bốn mùa ở vùng ôn đới.
mùa hanh|Thời kỳ khô hạn trong năm.
mùa hè|Mùa nóng nhất trong năm ở những nơi có bốn mùa.
mùa lạnh|Thời gian trong năm có nhiệt độ thấp, gió lạnh và thường có tuyết rơi.
mùa màng|Các vụ gieo trồng cùng kết quả thu hoạch của nhà nông.
mùa thi|Thời điểm trong năm diễn ra các kỳ thi học tập.
mùa thu|Mùa nằm sau hè và trước đông, trời thường mát dần.
múa rối|Biểu diễn bằng cách làm các hình nhân cử động theo câu chuyện.
mục đích|Mục tiêu cần đạt được trong tương lai.
mục đồng|Người chăn dắt đàn gia súc trên đồng cỏ.
mục lục|Bảng liệt kê các phần của tài liệu để tìm đến đúng chỗ.
mục sở thị|Nhìn thấy tận mắt bằng đôi mắt của mình.
mục tiêu|Đích cần đạt được sau khi hoàn thành công việc.
mục từ|Phần ghi định nghĩa của một từ trong từ điển hoặc sách tra cứu.
mùi hôi|Mùi khó chịu, không thơm.
mùi vị|Cảm giác vị giác hoặc khứu giác nhận được từ đồ ăn, thức uống hoặc mùi hương.
múi giờ|Khu vực địa lý có cùng một giờ quy định để phân chia thời gian.
mũm mĩm|Mỡ nhiều, thân hình tròn trịa và đầy đặn trông rất đáng yêu.
muối|Gia vị có vị mặn, thường thu từ nước biển.
muối ăn|Chất bột trắng dùng để nêm nếm thức ăn, có vị mặn đặc trưng.
muối khoáng|Hợp chất vô cơ chứa nhiều nguyên tố hóa học.
muối vừng|Hỗn hợp vừng rang và muối ăn để ăn.
muôn loài|Mọi loài sinh vật sống trên đời.
muôn thuở|Diễn ra mãi mãi từ thời xa xưa cho đến tận ngày sau.
muôn trùng|Rất nhiều sự vật nối tiếp nhau tạo thành cảnh tượng rộng lớn.
muộn màng|Đến sau thời điểm mong đợi hoặc quy định.
muông thú|Tên gọi chung nhiều loài thú, nhất là những loài sống ngoài tự nhiên.
mưa đá|Mưa có những cục nước đóng băng rơi xuống đất.
mưa lũ|Mưa lớn kèm theo nước lũ từ thượng nguồn tràn xuống.
mưa phùn|Mưa nhỏ li ti, ẩm ướt thường xảy ra vào mùa đông.
mưa rào|Hiện tượng nước mưa rơi xuống mạnh trong một thời gian ngắn rồi nhanh chóng tạnh hẳn.
mưa tuyết|Hiện tượng những tinh thể băng rơi xuống mặt đất thành bông tuyết.
mực tàu|Mực đen đặc dùng để viết chữ Hán hoặc vẽ tranh.
mực thước|Những quy tắc, chuẩn mực cần phải tuân theo.
mừng|Vui vì điều mong đợi đã xảy ra.
mừng rỡ|Vui mừng thể hiện rõ qua nét mặt.
mừng tuổi|Tặng tiền mừng cho người lớn tuổi hoặc trẻ em nhân dịp đầu năm.
mười lăm|Số lượng bằng tổng của mười và năm.
mười mươi|Chắc chắn không thể nghi ngờ.
mượn|Nhận dùng tạm vật của người khác rồi trả lại.
mương|Đường nước nhỏ để tưới tiêu cho ruộng vườn.
mường tượng|Hình dung chưa thật rõ bằng trí nhớ hoặc trí tưởng tượng.
mướp|Dây leo cho quả dài, thường dùng nấu canh.
mướp hương|Loài mướp có mùi thơm đặc trưng.
mượt|Êm và trơn đều khi vuốt trên bề mặt.
mượt mà|Cảm giác êm trơn, không gồ ghề.
mưu cầu|Chủ động tìm cách đạt được điều mong muốn.
mưu kế|Kế hoạch chi tiết để thực hiện một công việc cụ thể.
mưu sinh|Tìm phương cách để duy trì cuộc sống.
mưu trí|Có kế hoạch thông minh và tài năng vượt trội.
na ná|Trông bề ngoài giống hệt nhau.
nách|Chỗ lõm ngay dưới khớp vai và cánh tay.
nai nịt|Buộc chặt quần áo để sát vào thân người.
nài nỉ|Yêu cầu tha thiết, khẩn khoản xin ai đó làm gì.
nam bán cầu|Phần bán cầu phía nam của Trái Đất, nằm từ đường xích đạo đến cực Nam.
nam châm|Vật có khả năng hút sắt thép nhờ từ trường.
nam giới|Những người thuộc giới tính đực trong loài người, bao gồm cả trẻ em và người lớn.
nam nhi|Nam giới, đàn ông.
nam nữ|Nam giới và nữ giới nói chung.
nam sinh|Học trò nam đang theo học tại trường.
nam tính|Tính chất đặc trưng thường thấy ở người đàn ông.
nam trang|Quần áo mặc của người đàn ông.
nan giải|Việc khó tìm ra cách giải quyết.
nan hoa|Mỗi que mảnh căng từ may-ơ ra mép vành để đỡ bánh xe.
nanh|Răng nhọn mọc cạnh nhóm răng cửa.
nao lòng|Cảm xúc trong lòng bị lay động mạnh.
nào đâu|Không có, chẳng có gì cả.
nào ngờ|Không lường trước được điều gì xảy ra ngoài dự định.
não nề|Buồn bã sâu sắc, ảnh hưởng tâm trạng đến người khác.
náo động|Nơi có tiếng ồn lớn, mọi người chạy nhảy hỗn loạn.
náo nhiệt|Nơi đông người, ồn ào và nhộn nhịp.
náo nức|Nôn nao vui và mong chờ điều sắp đến.
nạo vét|Dùng dụng cụ cào, vét sạch những vật chất nằm sâu dưới đáy.
nạp điện|Đưa điện vào thiết bị để sử dụng.
nay kính|Thể hiện sự tôn trọng, chân thành khi viết thư cho nhau.
nảy lộc|Trái cây hoặc cây cối bắt đầu đâm chồi, ra lá mới.
nảy mầm|Hạt cây bắt đầu phát triển thành cây con.
nảy nở|Sinh ra, phát triển và lớn lên từ bên trong.
nảy sinh|Xuất hiện hoặc hình thành từ từ trong một hoàn cảnh.
nãy giờ|Thời gian từ lúc vừa rồi đến lúc này.
năm ánh sáng|Đơn vị đo khoảng cách bằng quãng đường ánh sáng đi được trong một năm.
năm dương lịch|Đơn vị thời gian gồm ba trăm sáu mươi lăm ngày hoặc ba trăm sáu mươi sáu ngày, chia thành mười hai tháng.
năm học|Thời gian học tập tại trường trong một năm.
năm nhuận|Năm có số ngày nhiều hơn bình thường để điều chỉnh lịch âm với dương.
năm sau|Năm kế tiếp năm nay.
năm xưa|Thời gian đã qua từ lâu trong quá khứ.
nằm bẹp|Nằm yên một chỗ, không cử động hay làm gì.
nằm dài|Nằm duỗi thẳng người hoặc không làm gì cả.
nằm ngang|Đặt song song với mặt phẳng của nước yên.
nằm ngủ|Nằm nghỉ ngơi trong giấc ngủ.
nắm bắt|Hiểu rõ để áp dụng vào việc làm.
nắm vững|Hiểu chắc và biết vận dụng điều đã học.
năn nỉ|Yêu cầu khẩn thiết với giọng điệu van xin.
nắn nót|Viết hoặc vẽ từng nét rất cẩn thận.
năng động|Hoạt động nhanh nhẹn, sáng tạo và luôn sẵn sàng thay đổi.
năng khiếu|Khả năng bẩm sinh làm giỏi một việc nào đó mà không cần học nhiều.
năng lực|Khả năng thực tế để hoàn thành một loại công việc.
năng lượng|Khả năng sinh công của một hệ thống vật lý.
năng lượng tái tạo|Năng lượng lấy từ nguồn tự nhiên có thể phục hồi.
năng nổ|Tích cực, nhiệt tình và sẵn sàng tham gia làm việc chung.
năng suất|Kết quả làm việc được tính theo đơn vị thời gian.
nắng|Ánh sáng và sức nóng từ mặt trời chiếu xuống.
nắng mới|Ánh nắng dịu nhẹ xuất hiện vào đầu mùa hè.
nặng lòng|Yêu thương sâu sắc, hết lòng quan tâm.
nặng nề|Trọng lượng lớn hoặc cảm giác khó chịu, chậm chạp.
nặng nhọc|Công việc nặng nề, vất vả vượt quá sức chịu đựng.
nặng tình|Có tình cảm sâu sắc, khó lòng chia cắt.
nặng trịch|Nặng đến mức khó khăn, vất vả mới có thể nâng lên được.
nặng trĩu|Cảm thấy nặng nề đến mức tưởng như sắp rơi.
nấc cụt|Khó thở khiến cơ hoành co giật tạo tiếng ngắn liên tiếp.
nấm hương|Loài nấm có mũ thơm, mọc trên gỗ mục và ăn được.
nấm mèo|Nấm ăn mỏng hình tai thường phơi khô, còn gọi là mộc nhĩ.
nấm rơm|Nấm ăn thường được trồng trên rơm đã ủ.
nấm sò|Loài nấm ăn có mũ tròn, dày.
nâng cao|Làm cho mức độ cao hơn lên.
nâng cấp|Cải tiến để thiết bị, chương trình hay dịch vụ đạt mức cao hơn.
nâng giá|Tăng mức tiền bán hàng lên cao hơn.
nâng lên|Động tác di chuyển vật từ thấp lên vị trí cao hơn.
nâng niu|Chăm sóc cẩn thận với tình cảm yêu quý sâu sắc.
nấu ăn|Chuẩn bị thức ăn chín để ăn bằng cách đun nóng nguyên liệu.
nấu bếp|Nấu ăn để bán hoặc làm nghề.
nấu nướng|Làm chín và chế biến nguyên liệu thành món ăn.
né tránh|Tránh né không muốn đối mặt hoặc không làm việc gì.
nem chua|Món ăn từ thịt lợn giã nhuyễn, gói lá và lên men chua.
nem rán|Món ăn gồm nhân thịt hoặc hải sản được gói trong bánh rồi chiên giòn.
ném tạ|Môn điền kinh dùng một tay đẩy quả tạ đi xa nhất có thể.
neo đơn|Không có người thân, sống cô độc và không ai giúp đỡ.
nẻo đường|Con đường hoặc lối đi để di chuyển.
nét mặt|Vẻ thể hiện qua mắt, miệng và các đường trên gương mặt.
nề hà|Quản ngại, không muốn làm hoặc không muốn chịu đựng.
nể phục|Cảm thấy kính trọng và ngưỡng mộ đối với người khác.
nể trọng|Cảm thấy kính nể và quý trọng người khác.
nếm trải|Trải qua sự việc để hiểu rõ và biết cảm giác của nó.
nên chi|Vì lý do đó, do vậy mà dẫn đến kết quả này.
nên thơ|Có vẻ đẹp hài hòa và gợi lên nhiều cảm xúc tốt đẹp.
nền móng|Phần dưới cùng truyền tải trọng của công trình xuống đất.
nền tảng|Bộ phận vững chắc làm cơ sở cho các phần khác tồn tại.
nếp cái|Loại gạo nếp hạt to, cơm dẻo, thường dùng để gói bánh chưng.
nếp sống|Thói quen sinh hoạt hàng ngày của con người.
nêu gương|Làm việc tốt để người khác học theo.
ngả mũ|Bỏ mũ khỏi đầu để chào hoặc tỏ lòng kính phục.
ngã ba|Chỗ giao nhau của ba con đường hoặc ba nhánh đường.
ngã giá|Đàm phán để chốt mức tiền mua bán cuối cùng.
ngã rẽ|Điểm đường đi chia làm hai hướng khác nhau.
ngã tư|Chỗ giao nhau của đường, từ đó có bốn hướng đi.
ngạc nhiên|Trạng thái bất ngờ, sửng sốt vì thấy sự việc không như dự kiến.
ngách|Lối nhỏ tách ra từ một lối đi khác.
ngại ngùng|Cảm thấy e thẹn, rụt rè nên không dám mạnh dạn làm hoặc nói.
ngàn xưa|Thời gian rất xa xưa, thuộc về quá khứ lâu đời.
ngang|Theo hướng từ trái sang phải hoặc ngược lại.
ngang dọc|Hướng đi từ trái qua phải và từ trên xuống dưới, bao quát mọi phía.
ngang hàng|Cùng cấp bậc trong gia đình hay xã hội.
ngang ngửa|Có sức hoặc trình độ gần như bằng nhau.
ngành|Lĩnh vực nghề nghiệp, học tập hoặc sản xuất riêng.
ngành nghề|Công việc chuyên môn mà người ta làm.
ngao|Động vật có hai mảnh vỏ, sống vùi ở bãi cát.
ngao du|Đi chơi xa để thư giãn, ngắm cảnh.
ngào ngạt|Mùi thơm nồng nặc, lan tỏa mạnh và gây cảm giác sảng khoái.
ngáp|Há miệng hít sâu theo phản xạ, thường khi buồn ngủ.
ngay cả|Bao gồm tất cả mọi người, không loại trừ bất kỳ ai.
ngay lập tức|Ngay lúc đó, không chờ đợi thêm.
ngay mặt|Cứng đầu, không chịu nghe lời khuyên.
ngay tức khắc|Ngay lập tức, không chờ đợi chút nào.
ngày|Khoảng thời gian một vòng quay của Trái Đất, thường tính 24 giờ.
ngày công|Đơn vị tính ngày làm việc để trả lương.
ngày giỗ|Ngày kỷ niệm ngày mất của người thân trong gia đình.
ngày lễ|Ngày nghỉ do nhà nước quy định để kỷ niệm sự kiện.
ngày mai|Ngày tiếp theo sau hôm nay hoặc tương lai sắp tới.
ngày mùa|Thời điểm thu hoạch lúa hoặc cây trồng.
ngày nay|Thời điểm hiện tại đang diễn ra.
ngày sản xuất|Thời điểm kết thúc quá trình làm ra sản phẩm.
ngày sinh|Ngày mà một người được chào đời trên thế gian.
ngày tháng|Thời gian cụ thể được tính theo năm, tháng và ngày.
ngày xanh|Độ tuổi trẻ trung, sung sức.
ngày xưa|Thời đã qua từ lâu, thường nhắc khi kể chuyện.
ngắm|Nhìn chăm chú để thưởng thức vẻ đẹp.
ngắm nghía|Nhìn đi nhìn lại, quan sát kỹ lưỡng một đối tượng nào đó.
ngắm nhìn|Nhìn chăm chú vào đối tượng trước mắt.
ngăn|Khoang nhỏ chia riêng bên trong tủ hay hộp.
ngăn cách|Tạo thành ranh giới khiến hai bên không còn tiếp xúc trực tiếp.
ngăn cản|Gây trở ngại khiến việc làm không thể tiến hành được.
ngăn chặn|Dùng sức hoặc biện pháp để làm cho việc gì đó dừng lại ngay.
ngăn kéo|Khoang đựng đồ có thể trượt ra vào trong bàn hoặc tủ.
ngăn nắp|Sắp đặt đồ có thứ tự, dễ tìm và dễ dùng.
ngăn trở|Gây khó khăn, cản trở việc làm của người khác.
ngắn gọn|Nói ít lời nhưng vẫn đủ ý nghĩa cần truyền đạt.
ngắn hạn|Có thời gian diễn ra hoặc kết thúc trong khoảng ngắn.
ngắt|Bấm rồi tách một phần nhỏ của cây bằng ngón tay.
ngắt điện|Làm đường dẫn điện không còn cấp dòng tới thiết bị.
ngắt lời|Cắt lời người khác giữa chừng khiến họ không nói tiếp được.
ngắt quãng|Đứt đoạn, không liên tục và chia thành từng phần rời rạc.
ngâm nga|Đọc hoặc hát chậm rãi để thưởng thức.
ngân hàng|Nơi nhận tiền gửi, cho vay và phát hành tiền giấy.
ngân nga|Kéo dài các âm theo giai điệu với giọng nhẹ nhàng.
ngân phiếu|Giấy ghi số tiền, dùng để rút hoặc chi thay cho tiền thật.
ngân sách|Tổng số tiền thu vào và chi ra trong một khoảng thời gian nhất định.
ngần ngại|Chưa muốn làm ngay vì còn băn khoăn hoặc e dè.
ngần ngừ|Do dự, chưa dám quyết định ngay.
ngẩn ngơ|Ngơ ngác vì tâm trí đang nghĩ ngợi chuyện khác.
ngập ngừng|Trì hoãn, không dám nói ra ngay hoặc tỏ ra do dự khi giao tiếp.
ngập úng|Nước tràn vào và gây ra tình trạng bị úng.
ngẫu hứng|Ý tưởng tự nhiên nảy ra trong lúc không có chuẩn bị.
ngẫu nhiên|Xảy ra một cách tình cờ, không có sự sắp xếp hay dự tính.
ngây ngất|Cảm thấy lâng lâng, say sưa hoặc choáng váng.
ngây thơ|Hồn nhiên, dễ tin vì còn ít kinh nghiệm.
nghe lời|Làm theo lời dạy bảo của người lớn tuổi.
nghe ngóng|Lắng tai để biết tin tức hoặc ý định của người khác.
nghẽn|Bị chặn đến mức không thể lưu thông bình thường.
nghèo nàn|Thiếu thốn nhiều mặt, không đủ về số lượng hoặc chất lượng cần thiết.
nghề nghiệp|Công việc chuyên môn làm để kiếm sống hằng ngày.
nghệ|Cây cùng họ với gừng cho củ màu vàng dùng nấu ăn.
nghệ danh|Tên gọi khác mà nghệ sĩ sử dụng khi biểu diễn trước công chúng.
nghệ nhân|Người có tài năng trong nghề thủ công hoặc nghệ thuật.
nghệ thuật|Hoạt động sáng tạo dùng âm thanh, hình ảnh hay hình thức khác để biểu đạt.
nghi hoặc|Cảm thấy không chắc chắn vì chưa rõ sự việc ra sao.
nghi ngút|Bốc lên liên tiếp thành nhiều làn dày, thường là khói hoặc hơi.
nghi thức|Hình thức hành động hoặc tổ chức lễ hội theo quy ước.
nghi vấn|Còn đáng ngờ, chưa thể tin tưởng hoàn toàn.
nghỉ|Tạm ngừng làm việc để lấy lại sức.
nghỉ dưỡng|Dừng việc để nghỉ ngơi, phục hồi sức khỏe.
nghỉ ngơi|Dừng lại việc làm hoặc hoạt động để thư giãn.
nghỉ việc|Dừng làm công việc hoặc không còn làm ở chỗ cũ.
nghĩ bụng|Suy nghĩ thầm trong lòng mà không nói thành lời.
nghị luận|Bàn luận, phân tích và đưa ra nhận xét về vấn đề.
nghị lực|Sức tinh thần giúp người ta kiên trì trước trở ngại.
nghĩa|Nội dung mà một từ hoặc một câu muốn diễn đạt.
nghĩa bóng|Nghĩa ẩn, trừu tượng suy ra từ nghĩa đen của từ.
nghĩa cử|Hành động, việc làm thể hiện lòng tốt hoặc trách nhiệm xã hội.
nghĩa đen|Ý nghĩa gốc, cách hiểu đầu tiên và tự nhiên nhất của từ.
nghĩa hẹp|Ý nghĩa của từ chỉ giới hạn trong phạm vi hẹp, ít bao quát.
nghĩa rộng|Nghĩa bao quát, mở rộng từ nghĩa cụ thể của một vật.
nghĩa vụ|Việc bắt buộc phải làm theo luật hoặc đạo đức.
nghịch|Bày trò vui, đôi khi gây phiền hoặc làm rối đồ đạc.
nghịch đảo|Hai số nhân với nhau ra một.
nghiêm khắc|Riết ráo, không cho phép sai sót hay tha thứ.
nghiêm minh|Quyết liệt, rõ ràng và không khoan nhượng.
nghiêm ngặt|Chặt chẽ, khắt khe, không cho phép sai sót.
nghiêm trang|Thái độ, hành động và lời nói trang trọng, nghiêm túc phù hợp với tình huống cần tôn kính.
nghiêm túc|Nghiêm chỉnh, không đùa cợt và hết sức cẩn thận.
nghiễm nhiên|Hiển nhiên được coi là có quyền hoặc có vị thế ấy.
nghiên cứu sinh|Người đang theo chương trình đào tạo để đạt học vị tiến sĩ.
nghiên cứu viên|Người chuyên làm việc nghiên cứu khoa học.
nghiền|Làm nhỏ vật rắn bằng cách chà hoặc ép mạnh.
nghiêng|Lệch sang một phía thay vì thẳng đứng hay nằm ngang.
nghiêng nghiêng|Có độ nghiêng nhẹ, không đứng thẳng hoàn toàn.
nghiệp dư|Làm việc vì sở thích, không chuyên nghiệp hay lấy làm nghề chính.
nghiệp vụ|Kiến thức và kỹ năng chuyên môn cần thiết cho nghề nghiệp.
nghìn|Số đếm bằng mười lần một trăm.
ngỏ lời|Nói ra suy nghĩ, tình cảm với người khác.
ngõ cụt|Đường nhỏ hẹp, kín ở một đầu không thể đi tiếp.
ngõ hẻm|Con đường nhỏ dẫn vào sâu trong khu dân cư hoặc nơi nào đó.
ngõ ngách|Đường nhỏ, hẹp và nhiều khúc ngoặt khó đi.
ngoài|Ở phía không thuộc phần bên trong một vật hay khu vực.
ngoài vòng|Không thuộc về bất kỳ tổ chức hay nhóm nào.
ngoại cảnh|Điều kiện bên ngoài ảnh hưởng đến sự sống.
ngoại hình|Hình dáng, vẻ bề ngoài của người.
ngoại lực|Lực tác động từ bên ngoài vào vật thể, làm thay đổi trạng thái.
ngoại ngữ|Thứ tiếng khác với tiếng mẹ đẻ mà một người học hoặc sử dụng.
ngoại ô|Khu vực nằm ở rìa thành phố, cách trung tâm một đoạn.
ngoại quốc|Nơi ở của những người không cùng quốc tịch với ta.
ngoại sinh|Các quá trình hình thành do tác nhân từ bên ngoài tác động.
ngoại tệ|Loại tiền tệ của nước ngoài dùng để mua bán trao đổi.
ngoại thành|Khu vực nằm ngoài thành phố chính, thường là nơi dân cư thưa thớt hơn.
ngoại thất|Phần bên ngoài và cách bài trí bên ngoài công trình.
ngoại văn|Các loại sách, báo được viết bằng ngôn ngữ của nước khác.
ngoại vi|Phần rìa, vùng bên ngoài của một khu vực hoặc hệ thống.
ngoan|Biết nghe lời và cư xử đúng mực.
ngoan cường|Bền bỉ, kiên quyết không chịu khuất phục.
ngoan ngoãn|Thái độ vâng lời, không nghịch ngợm và dễ dạy bảo.
ngoạn cảnh|Ngắm nhìn phong cảnh đẹp.
ngoảnh|Quay mặt về một phía khác để nhìn.
ngoáy|Xoay ngón tay hoặc que nhỏ trong một chỗ hẹp.
ngoặc|Dấu viết thành cặp để bao một phần nội dung.
ngoặc kép|Dấu hai chấm đặt ở đầu và cuối lời trích dẫn hoặc từ đặc biệt.
ngoằn ngoèo|Uốn lượn qua nhiều khúc quanh, không đi thẳng.
ngóc ngách|Đường nhỏ, hẹp và nằm sâu trong nơi ít người đến.
ngọc bội|Đồ trang sức bằng ngọc; người có đức tính cao quý.
ngọc lam|Loại đá quý màu xanh biển ngả xanh lá dùng làm đồ trang sức.
ngọc lan|Cây có hoa trắng hoặc vàng ngà và mùi thơm rõ rệt.
ngọc trai|Hạt ngọc tròn, sáng bóng được tạo thành bên trong vỏ của loài trai biển.
ngói|Miếng vật liệu cứng xếp chồng mép nhau để lợp mái.
ngói ống|Loài ngói hình ống dùng lợp nhà.
ngòn ngọt|Có vị ngọt nhẹ, không đậm đà.
ngón|Một trong các nhánh cử động được ở đầu bàn tay, bàn chân.
ngón áp út|Ngón tay thứ tư nằm giữa ngón út và ngón giữa trên bàn tay.
ngón chân|Một trong các nhánh nhỏ ở phần trước của bàn chân.
ngón chân út|Ngón chân nhỏ nhất ở bàn chân, dùng để cảm nhận vật thể trong bóng tối.
ngón tay|Một trong các phần cử động riêng ở cuối bàn tay.
ngón tay giữa|Ngón tay nằm giữa ngón trỏ và ngón đeo nhẫn.
ngón út|Ngón tay ngắn nhất và nhỏ nhất ở bàn tay.
ngọn nguồn|Nơi bắt đầu hoặc nguyên nhân tạo ra một sự vật, hiện tượng.
ngọt|Có vị giống đường hoặc mật ong.
ngọt lịm|Ngọt đến mức làm người ta thấy sung sướng.
ngộ nghĩnh|Lạ lùng, đáng yêu và khác thường.
ngộ nhận|Hiểu lầm, nhận thức sai sự thật.
ngôi sao|Vật thể tự nhiên trong vũ trụ phát ra ánh sáng và nhiệt.
ngôi thứ|Thứ tự sắp xếp vị trí dựa trên quan hệ thân thuộc hoặc địa vị trong xã hội cũ.
ngồi không|Không thực hiện bất kỳ công việc nào cả.
ngồi lê|Ngồi nói chuyện phiếm, không ngồi yên một chỗ.
ngồi xổm|Ngồi gập đầu gối lại, mông không chạm đất.
ngôn luận|Việc dùng lời nói để trao đổi, thảo luận hoặc trình bày quan điểm.
ngôn ngữ|Hệ thống lời nói, ký hiệu hoặc chữ dùng để giao tiếp.
ngôn ngữ học|Ngành nghiên cứu cấu trúc, cách dùng và sự biến đổi của tiếng nói.
ngôn ngữ lập trình|Ngôn ngữ đặc biệt dùng để ra lệnh cho máy tính thực hiện việc.
ngôn ngữ tự nhiên|Ngôn ngữ con người dùng để giao tiếp hàng ngày, khác với ngôn ngữ máy tính.
ngôn từ|Những chữ viết hoặc lời nói dùng để giao tiếp.
ngỗng|Chim nuôi cổ dài, chân có màng, lớn hơn vịt.
ngơ ngác|Có vẻ chưa hiểu chuyện gì đang xảy ra quanh mình.
ngờ đâu|Không lường trước được điều vừa xảy ra.
ngờ vực|Chưa tin hẳn vì còn những điều đáng nghi hoặc chưa sáng tỏ.
ngỡ ngàng|Cảm thấy lạ và bất ngờ trước điều chưa từng thấy hoặc chưa biết.
ngủ dậy|Tỉnh dậy sau giấc ngủ.
ngủ đông|Trạng thái ngủ sâu kéo dài để bảo toàn sức lực trong mùa lạnh.
ngủ gục|Ngủ say trong lúc không nên ngủ hoặc ở nơi không thích hợp.
ngủ mê|Ngủ say hoặc nằm mơ.
ngủ thiếp|Ngủ rất sâu, khó đánh thức dậy.
ngũ cốc|Tổng hợp năm loại hạt cây dùng làm lương thực.
ngũ giác|Hình học có năm góc và năm cạnh nối tiếp nhau.
ngũ liên|Tiếng trống đánh nhanh liên tiếp năm tiếng để báo nguy hoặc thúc việc.
ngũ quan|Năm giác quan dùng để cảm nhận thế giới bên ngoài.
ngũ sắc|Năm màu cơ bản gồm xanh, vàng, đỏ, trắng, đen.
ngũ vị|Năm loại vị giác cơ bản của con người.
ngụ ngôn|Truyện kể dùng loài vật để nói về con người và dạy bài học đạo lý.
nguệch ngoạc|Viết hoặc vẽ không ngay ngắn, không đúng quy cách.
ngụm|Lượng nước vừa lấy vào miệng trong một lần uống.
ngùn ngụt|Bốc lên dữ dội, tràn đầy sức mạnh.
nguồn|Nơi dòng nước hoặc một sự vật bắt đầu phát sinh.
nguồn điện|Thiết bị tạo ra dòng điện để chạy các đồ dùng.
nguồn gốc|Nơi bắt đầu, xuất phát của sự vật hay sự việc.
nguồn lực|Tổng hợp các yếu tố như người, của, tiền, trí để làm việc.
ngụp|Hạ cả đầu và thân xuống dưới mặt nước.
nguy cơ|Khả năng xảy ra điều không may hoặc tai họa trong tương lai.
nguy nga|Xây dựng đồ vật to lớn, đẹp mắt, lộng lẫy.
nguyên|Còn trọn vẹn, chưa bị thay đổi hoặc chia cắt.
nguyên âm|Âm phát ra khi luồng hơi qua miệng tương đối thông thoáng.
nguyên bản|Phiên bản đầu tiên chưa qua chỉnh sửa hay sao chép lại.
nguyên chất|Chỉ gồm chất đang nói đến, không pha thêm chất khác.
nguyên cớ|Lý do, cớ sự.
nguyên do|Lý do sâu xa dẫn đến một sự việc xảy ra.
nguyên liệu|Vật liệu tự nhiên chưa qua chế biến dùng để tạo ra sản phẩm.
nguyên mẫu|Vật mẫu gốc dùng để làm căn cứ cho các bản sao.
nguyên nhân|Điều dẫn đến sự xuất hiện của một kết quả hoặc hiện tượng.
nguyên tắc|Điều căn bản cần tuân theo khi quyết định hoặc hành động.
nguyên tố|Loại nguyên tử có tính chất hóa học riêng biệt và ổn định.
nguyên trạng|Trạng thái ban đầu, chưa bị thay đổi hay sửa chữa gì.
nguyên tử|Đơn vị nhỏ nhất cấu tạo nên chất hóa học, gồm hạt nhân ở giữa và các electron quay xung quanh.
nguyên văn|Bản ghi chép giữ nguyên đúng từng chữ, không sửa đổi hay thêm bớt.
nguyên vật liệu|Chất liệu dùng để chế biến thành sản phẩm.
nguyên vẹn|Đầy đủ các bộ phận, không bị hư hại hay thiếu sót.
nguyên xi|Còn y như trước, chưa thay đổi chút nào.
nguyện vọng|Những điều hy vọng muốn đạt được trong tương lai.
nguyệt san|Cuốn tạp chí được ấn hành mỗi tháng một lần.
nguyệt thực|Hiện tượng Mặt Trăng đi vào bóng của Trái Đất.
ngư nghiệp|Nghề nghiệp chuyên bắt cá và khai thác sản vật dưới nước.
ngư trường|Vùng biển rộng lớn nơi cá tôm sinh sống đông đúc và dễ bắt.
ngữ âm|Hệ thống các âm thanh cấu thành nên một ngôn ngữ.
ngữ cảnh|Môi trường xung quanh giúp hiểu rõ ý nghĩa.
ngữ điệu|Cách lên xuống giọng và ngắt nghỉ để thể hiện ý nghĩa, tình cảm.
ngữ học|Nghiên cứu cấu tạo, nguồn gốc và cách dùng của ngôn ngữ.
ngữ pháp|Quy tắc kết hợp từ và thành phần để tạo câu trong một ngôn ngữ.
ngữ văn|Môn học về tiếng Việt và cách đọc, viết, cảm thụ văn chương.
ngửa|Hướng mặt hay lòng của vật lên phía trên.
ngứa ngáy|Cảm thấy khó chịu, muốn làm việc gì đó.
ngựa gỗ|Đồ chơi hình con ngựa làm từ gỗ, có loại để ngồi đung đưa.
ngựa vằn|Thú thuộc họ ngựa có những dải lông đen trắng trên thân.
ngực|Phần thân trên phía trước, nằm giữa cổ và bụng.
ngửi|Dùng mũi để nhận biết mùi.
ngừng|Chấm dứt một động tác đang diễn ra.
ngừng trệ|Bị dừng lại hoàn toàn, gây ra sự ứ đọng và chậm trễ.
ngước|Hướng mắt hoặc ngẩng đầu để nhìn lên cao.
ngược chiều|Hai hướng di chuyển hoặc phát triển trái ngược nhau.
ngược đời|Trái ngược với quy luật thông thường hoặc khác lạ so với đời sống.
người|Sinh vật thuộc loài biết dùng ngôn ngữ và chế tạo công cụ.
người chủ|Người có quyền ra quyết định hoặc quản lý trong một tổ chức.
người dùng|Người thực hiện việc sử dụng một sản phẩm, dịch vụ hoặc công cụ.
người đời|Những người sống chung quanh, khác với bản thân mình.
người hiền|Người có tính tốt và khả năng làm việc giỏi.
người lạ|Người chưa từng quen biết.
người làm|Người được thuê làm việc cho người khác.
người lớn|Người đã trưởng thành, phân biệt với trẻ em.
người mẫu|Người chuyên trình diễn trang phục hoặc làm mẫu cho nghệ thuật.
người ngoài|Người không thuộc gia đình hay không tham gia việc đó.
người nhà|Thành viên thuộc gia đình ruột thịt hoặc người thân thiết.
người phát ngôn|Người đại diện chính thức phát biểu thay cho cơ quan, tổ chức hoặc hội nghị.
người quen|Người mà mình đã biết mặt.
người ta|Cách gọi người khác nói chung mà không nêu đích danh.
người thân|Người có quan hệ huyết thống hoặc gắn bó sâu sắc với bản thân.
người thợ|Người làm việc chân tay, nhận lương từ chủ.
người thương|Người mà mình yêu thương, gắn bó trong tình cảm.
người tuyết|Con người được tạo hình từ tuyết, thường có hình tròn.
người xem|Những người đến xem chương trình hoặc thưởng thức tác phẩm nghệ thuật.
người yêu|Người có mối quan hệ tình cảm lãng mạn với một người khác.
ngưỡng|Mốc phải đạt hay vượt qua để có thay đổi.
ngưỡng mộ|Quý trọng và kính phục trước phẩm chất hoặc tài năng.
ngưỡng vọng|Trông chờ, kính trọng và hy vọng vào người có địa vị cao hơn.
ngượng nghịu|Tỏ ra không tự nhiên trong cử chỉ, đi đứng hoặc nói năng.
nha đam|Cây mọng nước, lá dài có phần gel trong ở giữa.
nhà ăn|Nơi phục vụ bữa ăn chung ở trường, cơ quan hoặc xí nghiệp.
nhà bác học|Người học giả tinh thông sâu sắc về khoa học.
nhà báo|Người chuyên nghiệp làm công việc viết bài và đưa tin trên báo chí.
nhà bạt|Nhà lợp bằng vải bạt, dựng tạm và dễ tháo rời.
nhà bè|Ngôi nhà làm bằng tre nứa đặt trên bè nổi.
nhà bếp|Chỗ dành để chuẩn bị thức ăn và nấu nướng.
nhà buôn|Người chuyên mua bán hàng hóa để kiếm tiền.
nhà chọc trời|Tòa nhà xây dựng rất cao, thường có từ vài chục tầng trở lên.
nhà chồng|Gia đình bên chồng của người làm dâu.
nhà chuyên môn|Người am hiểu sâu sắc về một lĩnh vực khoa học hay kỹ thuật.
nhà chức trách|Người có chức vụ và quyền hạn giải quyết việc công.
nhà cửa|Nơi ở chung của gia đình hoặc người thân.
nhà dưới|Tầng nhà thấp nhất sát mặt đất.
nhà đất|Tên gọi chung nhà ở và đất đai trong giao dịch bất động sản.
nhà điêu khắc|Người chuyên tạo tác hình tượng bằng chất liệu cứng.
nhà ga|Công trình nơi hành khách chờ, lên hay rời tàu.
nhà giáo|Người chuyên dạy học ở trường lớp.
nhà giàu|Gia đình có nhiều tiền bạc, tài sản và điều kiện sống sung túc.
nhà hàng|Điểm bán đồ ăn và thức uống, nơi có nhân viên phục vụ khách.
nhà hát|Nơi có sân khấu và chỗ ngồi để xem biểu diễn nghệ thuật.
nhà khách|Ngôi nhà riêng biệt dùng để đón tiếp khách đến chơi.
nhà kho|Ngôi nhà chuyên dùng để chứa đựng hàng hóa hoặc vật dụng.
nhà khoa học|Người làm nghiên cứu có hệ thống để tìm hiểu thế giới.
nhà kinh doanh|Người chuyên lo việc mua bán, kinh doanh để kiếm lời.
nhà kính|Công trình có vách hoặc mái trong để trồng cây trong điều kiện kiểm soát.
nhà lá|Ngôi nhà được lợp mái bằng các loại lá cây khô.
nhà lầu|Ngôi nhà có nhiều tầng lầu xây chồng lên nhau.
nhà may|Nơi nhận đo, cắt và may quần áo cho khách.
nhà nghề|Người chuyên tâm làm hoặc rất giỏi một nghề cụ thể.
nhà nghỉ|Nhà cho thuê để nghỉ ngơi, thường ở nơi có cảnh đẹp hoặc du lịch.
nhà ngoài|Nhà ở bên ngoài dùng để tiếp khách hoặc làm việc.
nhà ngói|Nhà có mái lợp bằng ngói làm từ đất nung.
nhà nhà|Mọi gia đình, tất cả các nhà đều như nhau.
nhà ổ chuột|Nhà ở thấp, bẩn, chật và tồi tàn, thường xây chen chúc.
nhà ống|Kiểu nhà dài hẹp, hai bên có tường, chỉ có cửa trước và sau.
nhà phát minh|Người tạo ra hoặc tìm ra những phát minh có ích cho đời.
nhà riêng|Chỗ ở cá nhân, không thuộc cơ quan.
nhà sách|Cửa hàng chuyên bán sách, thường có cả văn phòng phẩm.
nhà sàn|Nhà có mặt sàn được nâng cao khỏi đất bằng hệ cột.
nhà sử học|Người chuyên nghiên cứu và viết về các sự kiện trong quá khứ.
nhà tắm|Nơi dùng để tắm rửa sạch sẽ cơ thể.
nhà tầng|Ngôi nhà được xây dựng có nhiều tầng để ở.
nhà tập thể|Nhà chung có nhiều căn phòng dành cho cán bộ, nhân viên.
nhà thầu|Đơn vị nhận làm công trình hoặc cung cấp dịch vụ theo hợp đồng.
nhà thi đấu|Nơi xây dựng để tập luyện và thi đấu các môn thể thao trong nhà.
nhà thiên văn học|Người chuyên nghiên cứu về các thiên thể trong vũ trụ.
nhà thơ|Người viết thơ hay và nổi tiếng.
nhà trai|Đoàn người đứng về phía chú rể trong buổi lễ cưới.
nhà tranh|Ngôi nhà được lợp mái bằng cỏ hoặc rơm rạ khô.
nhà trẻ|Nơi nhận trông và chăm sóc trẻ còn nhỏ vào ban ngày.
nhà trí thức|Người làm việc bằng tư duy, trí tuệ thay vì sức lực thể xác.
nhà trọ|Nơi cho người thuê phòng ở tạm thời.
nhà trường|Nơi dạy học và bộ phận quản lý trường.
nhà tư bản|Người sở hữu vốn lớn để kinh doanh và kiếm lời.
nhà tư tưởng|Người đưa ra các quan điểm triết học hoặc xã hội nổi tiếng.
nhà văn|Người sáng tác tác phẩm văn chương, nhất là văn xuôi.
nhà vệ sinh|Phòng dùng để đi vệ sinh.
nhà vợ|Gia đình vợ của người làm rể.
nhà vườn|Người hoặc hộ làm vườn để bán cây, trái hay hoa.
nhà xe|Đơn vị chuyên chở khách hay hàng bằng xe đường bộ.
nhà xuất bản|Đơn vị tổ chức chuyên in ấn, phát hành sách, báo, tạp chí.
nhà xưởng|Kho nhà lớn chứa máy móc dùng để chế biến hàng hóa.
nhã nhặn|Lịch sự, khiêm tốn, không phô trương.
nhá nhem|Sắp đến lúc trời tối, ánh sáng mờ dần.
nhạc|Âm thanh sắp theo nhịp và giai điệu để nghe hoặc biểu diễn.
nhạc chuông|Âm thanh đặc biệt vang lên khi có cuộc gọi đến trên điện thoại di động.
nhạc công|Người chơi nhạc cụ trong một buổi diễn hay bản thu.
nhạc cụ|Dụng cụ dùng để tạo ra âm thanh.
nhạc đồng quê|Dòng nhạc đại chúng khởi nguồn từ đời sống nông thôn Hoa Kỳ.
nhạc phẩm|Tác phẩm âm nhạc được sáng tác hoặc trình diễn.
nhạc phụ|Cha của người vợ.
nhạc sống|Âm nhạc được trình diễn trực tiếp bởi người hát và người chơi nhạc cụ tại chỗ.
nhạc trưởng|Người đứng đầu, điều khiển dàn nhạc khi biểu diễn.
nhạc viện|Trường đại học chuyên đào tạo và nghiên cứu về các loại nhạc cụ.
nhai|Dùng răng nghiền nhỏ thức ăn trong miệng.
nhàm chán|Cảm thấy buồn tẻ, không còn hứng thú gì.
nhan đề|Tên gọi ngắn gọn nêu bật nội dung chính của tác phẩm.
nhan nhản|Nhiều lắm, xuất hiện ở khắp nơi.
nhàn nhã|Thư thái, không bận rộn, thoải mái cả thân lẫn tâm.
nhàn nhạt|Có màu sắc hoặc cảm xúc không đậm, thiếu rõ rệt.
nhàn rỗi|Không có việc gì phải làm, rảnh rỗi.
nhãn hiệu|Dấu riêng do nhà sản xuất gắn lên sản phẩm để nhận biết.
nhãn lồng|Loại nhãn có cùi dày, mọng, hạt thường nhỏ.
nhanh|Có tốc độ cao, không mất nhiều thời gian.
nhanh chóng|Làm việc nhanh, không chậm trễ.
nhanh nhạy|Cảm nhận nhanh, hiểu ý ngay lập tức.
nhanh nhẹn|Thân thể linh hoạt, di chuyển nhanh và khéo léo.
nhanh tay|Thực hiện hành động một cách nhanh chóng và dứt khoát.
nhanh trí|Suy nghĩ nhanh và xử lý tình huống kịp thời.
nhào|Trộn và ép bột liên tiếp cho thành khối dẻo.
nhào lộn|Quay vòng người trên không trung.
nhạt nhẽo|Thiếu vị đậm hay nét thú vị khiến người ta ít hứng thú.
nhàu|Có nhiều nếp gấp lộn xộn, không còn phẳng.
nháy mắt|Khoảng thời gian ngắn đến mức chỉ bằng một cái chớp mắt.
nhạy|Nhận biết hoặc phản ứng nhanh trước thay đổi nhỏ.
nhạy bén|Nhanh chóng nhận ra dấu hiệu nhỏ và biết ứng xử phù hợp.
nhạy cảm|Dễ dàng cảm nhận được những thay đổi nhỏ hoặc tác động từ bên ngoài.
nhắc lại|Nói lại hoặc làm lại điều đã từng xảy ra để người ta nhớ.
nhắc nhở|Nói lại để người khác nhớ đến việc cần làm.
nhắc tới|Nói đến một điều gì đó đã biết hoặc đã xảy ra.
nhắm nghiền|Đóng chặt hai mí mắt lại không hé mở.
nhăn nheo|Có nhiều nếp gấp, nhăn nhúm do khô hoặc già.
nhắn nhủ|Dặn dò, khuyên bảo người khác với thái độ chân thành và nhẹ nhàng.
nhặt|Cúi hoặc đưa tay lấy vật rời khỏi mặt đất.
nhặt nhạnh|Lượm từng chút một để gom lại thành nhiều.
nhâm nhi|Ăn uống chậm rãi, thưởng thức từng chút một.
nhẩm|Tính hoặc đọc thầm mà không nói to.
nhân ái|Yêu thương, quan tâm và giúp đỡ người khác.
nhân bản|Nhân văn hoặc tạo ra nhiều bản sao giống bản gốc.
nhân cách|Đức tính tốt đẹp và danh dự của người.
nhân chứng|Người biết rõ sự việc và có thể làm chứng trước tòa.
nhân công|Sức lực lao động của con người dùng làm việc.
nhân danh|Lấy tên của người khác để làm việc hoặc phát biểu.
nhân dân|Toàn bộ người sống trong một nước hoặc một vùng.
nhân dân tệ|Đơn vị tiền chính thức dùng trong nước Trung Quốc.
nhân dịp|Lý do hay thời điểm thuận tiện để làm việc gì đó.
nhân đạo|Thái độ tôn trọng và yêu thương con người, đề cao giá trị sống.
nhân giống|Tạo ra nhiều cá thể mới từ giống cây hoặc vật nuôi để nuôi trồng.
nhân hậu|Có lòng thương yêu người khác và sống ngay thẳng.
nhân khẩu|Mỗi người được tính trong số thành viên của một hộ hay khu dân cư.
nhân kiệt|Người tài năng vượt trội so với những người khác.
nhân loại học|Môn khoa học nghiên cứu về con người, bao gồm cả đặc điểm hình thể và các giống loài.
nhân nghĩa|Tình thương yêu con người và việc làm đúng lẽ phải.
nhân rộng|Lan truyền rộng rãi để nhiều nơi cùng thực hiện.
nhân sinh|Cuộc đời và những trải nghiệm của con người trong xã hội.
nhân sự|Tập hợp những người làm việc trong một tổ chức hoặc đơn vị.
nhân tài|Người có năng lực đặc biệt hoặc tài năng xuất chúng.
nhân tạo|Do con người tạo ra, không phải tự nhiên sinh ra.
nhân thân|Tổng hợp thông tin về thân thế, tính cách và quá khứ của một người.
nhân thế|Tình hình và hoàn cảnh xã hội.
nhân tiện|Làm thêm việc khác vào lúc có thời gian rảnh hoặc thuận tiện.
nhân tính|Đặc điểm, phẩm chất và bản chất chung của con người.
nhân tố|Yếu tố có ảnh hưởng tới sự hình thành hay kết quả của việc.
nhân từ|Có lòng thương người, không muốn họ chịu khổ đau.
nhân văn|Thuộc về con người, đề cao giá trị và phẩm chất của nhân loại.
nhân vật|Người nổi tiếng, có vai trò quan trọng hoặc địa vị trong xã hội.
nhân viên|Người làm việc dưới quyền lãnh đạo.
nhẫn|Vòng nhỏ đeo trên ngón tay làm trang sức.
nhẫn cưới|Vòng kim loại trao cho đôi vợ chồng trong buổi lễ cưới.
nhẫn nại|Chịu đựng khó khăn mà không bỏ cuộc hay than vãn.
nhấn mạnh|Nói rõ ra để người khác chú ý nhiều hơn.
nhận biết|Hiểu rõ và phân biệt được đặc điểm của sự vật hay con người.
nhận dạng|Xác định rõ đối tượng dựa trên hình dáng, dấu hiệu.
nhận định|Đưa ra ý kiến đánh giá hoặc kết luận về sự việc.
nhận lời|Đồng ý làm theo yêu cầu của người khác.
nhận ra|Biết rõ sự thật sau khi suy nghĩ kỹ.
nhận thầu|Nhận làm công việc thay chủ, lấy tiền công theo thỏa thuận.
nhận thấy|Biết được điều gì đó khi quan sát hoặc suy nghĩ.
nhận thức|Khả năng hiểu biết, nhận ra và nắm bắt được sự vật, hiện tượng trong thực tế.
nhận xét|Việc đưa ra ý kiến đánh giá về người hay việc.
nhấp|Uống từng chút nhỏ bằng môi.
nhấp nháy|Động tác chớp tắt liên tục của ánh sáng hoặc mắt.
nhấp nhô|Lúc nhô cao, lúc hạ thấp, như những đợt sóng nối nhau.
nhập cuộc|Tham gia trực tiếp vào công việc hoặc sự kiện.
nhập cư|Đi đến nơi khác để sinh sống lâu dài.
nhập hội|Tham gia vào một tổ chức hoặc nhóm người.
nhập khẩu|Đưa hàng từ nước ngoài vào để dùng hoặc bán trong nước.
nhập ngoại|Nhập từ nước ngoài vào trong nước.
nhập nhoạng|Thời điểm trời tối mờ chưa hẳn đêm.
nhập siêu|Tình trạng mua vào nhiều hơn bán ra trong thương mại.
nhất cử nhất động|Mọi hành động nhỏ nhất cũng đều có tác động.
nhất định|Khẳng định chắc chắn rằng việc đó sẽ xảy ra hoặc không thể thay đổi.
nhất nhất|Làm tất cả mọi việc đều cẩn thận, không bỏ sót chi tiết nào.
nhất quán|Giữ cùng một nguyên tắc, không tự mâu thuẫn giữa các phần.
nhất quyết|Quyết tâm làm một việc gì đó dù có khó khăn cản trở.
nhất sinh|Suốt cả cuộc đời.
nhất tề|Tất cả mọi người đều làm cùng lúc.
nhất trí|Tất cả mọi người đều đồng ý với một ý kiến chung.
nhật báo|Báo in phát hành mỗi ngày.
nhật thực|Hiện tượng Mặt Trăng che một phần hoặc toàn bộ Mặt Trời khi nhìn từ Trái Đất.
nhầy nhụa|Dính đầy chất lỏng làm bề mặt trơn và bẩn.
nhè nhẹ|Hành động nhẹ nhàng, không mạnh tay hay gây tiếng động lớn.
nhẹ nhàng|Có lực, cử chỉ hoặc cách nói êm và không gắt.
nhẹ nhõm|Cảm thấy bớt gánh nặng hay lo âu sau một việc.
nheo|Khép hai mí lại để mắt chỉ còn một khe nhỏ.
nhét|Đưa vật vào chỗ hẹp, thường phải dùng chút sức.
nhện|Động vật có tám chân, nhiều loài giăng tơ bắt mồi.
nhi đồng|Những người còn nhỏ tuổi, chưa đến độ trưởng thành.
nhí nhảnh|Hoạt bát, vui tươi, nhanh nhẹn trong cử chỉ và lời nói.
nhích|Chuyển vị trí từng chút một.
nhiệm vụ|Việc cần phải làm hoặc phải hoàn thành trong một thời gian.
nhiếp ảnh|Nghệ thuật ghi lại hình ảnh bằng máy ảnh.
nhiệt|Năng lượng truyền từ vật nóng hơn sang vật lạnh hơn.
nhiệt điện|Điện sinh ra từ hơi nước do đốt nhiên liệu.
nhiệt độ|Đại lượng đo lường mức độ nóng hoặc lạnh của vật.
nhiệt đới|Vùng đất quanh xích đạo có khí hậu nóng.
nhiệt huyết|Sự hăng say, nhiệt tình cao độ trong công việc.
nhiệt kế|Dụng cụ đo nhiệt độ của vật thể.
nhiệt liệt|Thể hiện sự nhiệt tình cao độ, vui mừng lớn lao.
nhiệt năng|Năng lượng sinh ra từ sự nóng lên của vật chất hoặc môi trường.
nhiệt tâm|Tình cảm hăng hái, nhiệt tình và sẵn sàng giúp đỡ người khác.
nhiệt tình|Thái độ làm việc hăng hái, nhiệt tâm và tích cực.
nhiều|Có số lượng hoặc mức độ lớn hơn bình thường.
nhiều lời|Nói nhiều, hay nói chuyện.
nhiều người|Số lượng con người lớn hơn một người.
nhím|Thú có lưng phủ những gai cứng để tự bảo vệ.
nhìn|Dùng mắt để nhận thấy hình dạng và màu sắc.
nhìn chung|Xét các nét chính của toàn bộ sự việc thay vì từng chi tiết.
nhìn nhận|Hiểu rõ sự vật, sự việc.
nhìn thấy|Dùng mắt để quan sát và nhận biết được sự vật.
nhìn xa trông rộng|Có tầm nhìn bao quát, suy nghĩ thấu đáo và dự đoán được những điều sẽ xảy ra trước.
nhịn đói|Không ăn uống và chịu đựng cảm giác đói.
nhỉnh|Cao hơn hoặc hơn về lượng một chút.
nhịp|Sự lặp lại đều đặn của âm thanh hay chuyển động.
nhịp điệu|Sự lên xuống đều đặn trong âm thanh hoặc nhịp bước.
nhịp nhàng|Đúng giờ và khớp nhau trong chuyển động.
nhíu|Kéo hai đầu lông mày gần lại, làm trán có nếp.
nhỏ bé|Có kích thước ngắn hoặc không quan trọng.
nhỏ nhắn|Có dáng nhỏ gọn và trông cân đối.
nhỏ nhặt|Bé nhỏ, vụn vặt hoặc hẹp hòi trong cách nhìn.
nhỏ nhẹ|Nói chuyện nhẹ nhàng, không gay gắt hay ồn ào.
nhoài|Vươn thân ra hết mức để với tới một chỗ.
nhọc nhằn|Làm việc vất vả khiến người ta rất mệt mỏi.
nhóm người|Tập hợp nhiều người cùng nhau.
nhọn|Thu hẹp dần tới một đầu rất nhỏ.
nhọn hoắt|Có đầu sắc nhọn và sắc bén đến mức đáng sợ.
nhồi|Ấn thêm chất liệu vào bên trong một vật cho đầy.
nhôm|Kim loại nhẹ có màu trắng bạc, thường dùng làm xoong nồi.
nhộn nhịp|Nơi có nhiều người qua lại tấp nập và hoạt động sôi nổi.
nhộng|Giai đoạn côn trùng biến đổi giữa ấu trùng và dạng trưởng thành.
nhờ vả|Dùng lời nói xin người khác giúp đỡ việc gì.
nhớ lại|Gợi về trong trí điều mình đã trải qua hoặc từng biết.
nhớ nhà|Cảm xúc nhớ nhung người thân khi ở xa nhà.
nhớ nhung|Nghĩ về người hoặc nơi đã xa cách một cách tha thiết.
nhớ thương|Yêu nhớ và thương tiếc người thân đang xa hoặc đã mất.
nhu cầu|Những việc cần phải có để duy trì sự sống và hoạt động.
nhu động|Sự co giãn tự nhiên của ruột để trộn thức ăn.
nhu yếu|Những thứ cần phải có để duy trì cuộc sống.
nhu yếu phẩm|Những vật cần thiết để duy trì cuộc sống hàng ngày.
nhuần nhuyễn|Làm việc rất thành thạo, tự nhiên và trôi chảy.
nhuận bút|Tiền trả cho tác giả khi tác phẩm được sử dụng hoặc công bố.
nhúc nhắc|Di chuyển từng bước một cách chậm rãi, khó khăn.
nhúc nhích|Chuyển động một chút, không mạnh.
nhuệ khí|Lòng hăng hái, quyết tâm mạnh mẽ.
nhúm|Lượng nhỏ có thể lấy bằng mấy đầu ngón tay.
nhún|Hạ nhẹ người bằng cách co đầu gối.
nhún nhường|Tự ý thức hạ mình xuống, tỏ ra lễ phép và khiêm tốn trước người khác.
nhún vai|Cúi vai lên để tỏ vẻ không quan tâm hoặc nghi ngờ.
nhung|Vải có lớp lông ngắn dày cho cảm giác mềm mịn.
nhuộm|Làm cho vải, tóc hay vật liệu mang màu mới.
nhút nhát|Dễ e ngại, ít dám làm quen hoặc thử việc mới.
nhuyễn|Mịn đều, không còn những hạt hay miếng to.
như thế|Giống hệt hoặc đúng như việc đã nói hoặc làm.
như ý|Hợp với điều mình mong muốn.
nhựa|Vật liệu có thể tạo khuôn, dùng làm nhiều đồ gia dụng.
nhựa đường|Chất đen rải đường.
nhựa thông|Chất nhựa lỏng lấy từ thân cây thông để làm keo dán hoặc sơn.
nhược điểm|Khía cạnh yếu kém, thiếu sót hoặc điểm không tốt của một sự vật, con người.
nhường|Để người khác nhận phần hoặc đi trước mình.
nhường lại|Cho người khác được dùng thứ mình đang giữ.
nhường nhịn|Sẵn lòng để người khác có phần hoặc tránh tranh hơn thua.
nhượng bộ|Chấp nhận để đối phương làm theo ý muốn vì yếu thế.
niêm|Dán hoặc đóng kín để nhận biết nếu bị mở ra.
niêm phong|Đóng kín và dán dấu của cơ quan để không ai mở được.
niêm yết|Đặt thông tin ở nơi công khai để mọi người đọc hoặc tra cứu.
niềm nở|Tỏ ra vui vẻ, thân thiện và đón tiếp khách rất nhiệt tình.
niềm tin|Sự tin tưởng chắc chắn vào điều gì đó hoặc ai đó.
niềm vui|Cảm giác sung sướng, mừng rỡ.
niên biểu|Bảng liệt kê theo trình tự thời gian các sự kiện quan trọng.
niên đại|Thời gian, năm tháng trong quá khứ.
niêu|Nồi đất nhỏ, thường dùng để nấu cơm.
nín thinh|Im lặng không nói gì cả.
ninh|Nấu lâu trên lửa nhỏ để thức ăn mềm và ra chất ngọt.
níu kéo|Giữ chặt không cho ai hoặc vật gì rời đi.
no ấm|Đủ đầy những thứ cần thiết cho cuộc sống.
noi gương|Làm theo tấm gương tốt của người có đức tính và tài năng.
nói chung|Tỏ ý bỏ qua các chi tiết nhỏ và trường hợp riêng biệt.
nói chuyện|Trao đổi lời nói với nhau về nhiều vấn đề.
nói dối|Cố tình nói điều mình biết là không đúng sự thật.
nói khéo|Nói lời dịu dàng, ngọt ngào để làm người nghe hài lòng.
nói lên|Cho thấy một ý nghĩa hay đặc điểm qua lời hoặc dấu hiệu.
nói năng|Dùng miệng để trao đổi, giao tiếp với người khác.
nói quanh|Dùng từ ngữ vòng vo, tránh nói thẳng vào vấn đề cần thiết.
nói riêng|Nói về một bộ phận cụ thể trong khi có điều chung cho tất cả.
nói sai|Nói những điều không đúng sự thật, bịa đặt ra.
nói thẳng|Nói lời ra ngoài ý nghĩ mà không giấu giếm.
nói thầm|Nói nhỏ tiếng chỉ đủ cho một người bên cạnh nghe rõ.
non choẹt|Người còn rất nhỏ tuổi và chưa có nhiều kinh nghiệm.
non nớt|Chưa đủ lớn hoặc còn yếu kém so với mức bình thường.
non nước|Sông, suối, núi, đồi; thường dùng để gọi chung đất nước.
non sông|Núi sông, thường dùng để nói về đất nước quê hương.
nón bài thơ|Nón lá có hình hoặc chữ nằm giữa các lớp lá, soi sáng mới hiện.
nón quai thao|Nón rộng vành, có quai dệt buông hai bên, gắn với trang phục dân gian.
nóng|Có nhiệt độ cao hoặc tạo cảm giác cần được làm mát.
nóng bức|Thời tiết nóng làm người ta cảm thấy khó chịu.
nóng chảy|Đổi từ trạng thái rắn sang trạng thái lỏng khi nóng.
nóng hổi|Vẫn còn nóng, vừa mới được làm hoặc mới có.
nóng lòng|Cảm thấy bực bội vì phải chờ đợi.
nỗ lực|Ráng dùng hết toàn bộ sức lực và trí tuệ để hoàn thành một việc khó khăn.
nồi áp suất|Nồi đậy kín giữ hơi nóng dưới áp lực để thức ăn mau mềm.
nồi cơm|Nồi dành để nấu gạo thành cơm.
nồi hấp|Nồi làm chín thực phẩm bằng hơi nước từ phần đáy.
nồi niêu|Bộ nồi dùng để nấu ăn trong gia đình.
nổi bật|Dễ được chú ý hơn những thứ ở xung quanh.
nổi cáu|Phát giọng rít lên do tức giận.
nổi tiếng|Được nhiều người biết đến và nhắc đến rộng rãi.
nổi trội|Có một đặc điểm vượt lên rõ rệt so với những thứ cùng loại.
nỗi niềm|Những tâm tư, cảm xúc sâu kín và riêng tư trong lòng mỗi người.
nối liền|Kết nối hai phần lại với nhau để không còn chỗ trống.
nối mạng|Kết nối máy tính vào mạng lưới để trao đổi và sử dụng dữ liệu chung.
nội bộ|Tình trạng bên trong một tổ chức hoặc cơ quan.
nội chính|Việc sửa lỗi, chỉnh đốn nội bộ đất nước.
nội dung|Phần bên trong của sự vật, chất chứa hoặc thể hiện ý nghĩa.
nội địa|Phần đất liền nằm sâu trong nước, cách xa biển cả và biên giới.
nội lực|Lực bên trong vật thể giúp chống lại sự phá vỡ khi chịu tác động từ bên ngoài.
nội tại|Thuộc về bên trong sự vật.
nội tâm|Nội dung của những suy nghĩ và cảm xúc bên trong.
nội thành|Khu vực trung tâm, nằm trong thành phố lớn.
nội thất|Đồ dùng và phần bố trí bên trong nhà hay xe.
nội trợ|Làm các việc chăm sóc, dọn dẹp và quản lý gia đình hàng ngày.
nôn nao|Cảm thấy bứt rứt, khó chịu trong bụng như sắp nôn.
nôn nóng|Thiếu kiên nhẫn, muốn đạt kết quả ngay lập tức.
nông cụ|Đồ dùng hỗ trợ cho công việc cày cấy và làm ruộng.
nông dân|Người sống bằng việc làm ruộng, trồng trọt hoặc chăn nuôi.
nông gia|Người chuyên làm ruộng để kiếm sống.
nông lâm|Làm việc trên đồng ruộng và chăm sóc rừng cây.
nông nghiệp|Ngành sản xuất chủ yếu dựa vào trồng trọt và chăn nuôi để tạo ra lương thực, thực phẩm cho con người.
nông nhàn|Thời gian rảnh rỗi của người làm nông khi không cần cày cấy.
nông sản|Sản phẩm thu hoạch từ cây trồng và vật nuôi trong nông nghiệp.
nông thôn|Vùng dân cư ngoài đô thị, thường gắn với sản xuất nông nghiệp.
nông trại|Nơi trồng trọt và chăn nuôi quy mô lớn.
nông trang|Đất đai hoặc cơ sở sản xuất nông nghiệp quy mô lớn.
nông trường|Nơi sản xuất nông nghiệp do nhà nước quản lý và điều hành.
nồng độ|Số lượng chất tan có trong một đơn vị thể tích của dung dịch.
nồng hậu|Thân thiết, ấm áp và chân thành với người khác.
nồng nàn|Mạnh và đằm sâu, thường nói về tình cảm hoặc mùi hương.
nồng nặc|Mùi hương rất mạnh, lan tỏa khắp nơi và dễ ngửi thấy.
nốt ruồi|Chấm đen nhỏ xuất hiện tự nhiên trên bề mặt da.
nở hoa|Trở nên tươi đẹp, rực rỡ.
nở nang|Đầy đặn, phổng phao, phát triển tốt.
nở rộ|Hoa hoặc sự vật phát triển mạnh mẽ, lan rộng khắp nơi.
nợ nước|Nghĩa vụ tài chính hoặc trách nhiệm lớn mà một quốc gia phải gánh vác.
nơi nơi|Tại khắp mọi nơi, ở đâu cũng có.
nụ cười|Cái biểu hiện vui vẻ, miệng hơi hé nhẹ.
núi lửa|Ngọn núi phun ra đá nóng và khí từ lòng đất.
núi non|Các dãy núi và đồi núi nói chung trong tự nhiên.
núi rừng|Núi non và cây cối bao phủ trên đó.
nung chảy|Dùng nhiệt độ cao để làm cho vật rắn chuyển sang trạng thái lỏng.
nuôi dạy|Chăm sóc về ăn uống và dạy dỗ về đạo đức, kỹ năng.
nuôi dưỡng|Nuôi nấng và chăm sóc để phát triển khỏe mạnh.
nuôi lợn|Chăm sóc đàn lợn để lấy thịt hoặc mỡ.
nuôi nấng|Chăm lo ăn ở và giúp trẻ hoặc vật non lớn lên.
nuông chiều|Làm theo ý người khác một cách thái quá.
nuốt|Đưa thức ăn hay nước từ miệng xuống cổ họng.
núp bóng|Dựa vào sức mạnh hay sự bảo vệ của người khác.
nút bấm|Vật dụng nhỏ dùng để bấm vào nhằm vận hành máy móc.
nữ sinh|Người nữ đang theo học ở trường.
nữ trang|Đồ trang sức như vòng, nhẫn hoặc hoa tai để đeo trên người.
nữ tử|Con gái trong gia đình hoặc dòng họ.
nửa đêm|Khoảng thời gian giữa hai giờ khuya và sáng sớm.
nửa mùa|Làm việc chưa hoàn thiện, thiếu kỹ năng cần thiết.
nức lòng|Cảm thấy vui sướng và phấn khích trong lòng.
nức tiếng|Nổi tiếng vang xa, được nhiều nơi biết đến.
nước|Chất lỏng thông thường để uống, tắm giặt và tưới cây.
nước biển|Nước mặn chứa các muối hòa tan ở biển và đại dương.
nước bọt|Chất lỏng trong suốt do cơ thể tiết ra ở miệng.
nước cam|Nước ép lấy từ quả cam tươi.
nước cất|Nước tinh khiết được làm từ nước thường qua phương pháp chưng cất.
nước chanh|Nước đường pha với nước cốt chanh để uống.
nước chấm|Chất lỏng có vị mặn dùng để chấm thức ăn trước khi ăn.
nước dãi|Chất lỏng trong miệng giúp làm ẩm và hỗ trợ tiêu hóa thức ăn.
nước dùng|Nước nấu lấy vị từ rau củ, thịt hay xương để làm món nước.
nước dừa|Chất lỏng trong khoang quả dừa, có thể uống trực tiếp.
nước đá|Nước đã đông lại thành khối cứng.
nước giải khát|Các loại đồ uống giải khát cung cấp khoáng chất cho cơ thể.
nước hoa|Dung dịch thơm dùng với lượng nhỏ trên da hoặc quần áo.
nước khoáng|Nước tự nhiên chứa nhiều chất khoáng được khai thác từ mạch ngầm.
nước lã|Nước tự nhiên chưa qua đun sôi hoặc lọc kỹ.
nước lạnh|Nước có nhiệt độ thấp hoặc không được hâm nóng.
nước lọc|Nước uống đã lọc, không pha thêm đường, sữa hoặc hương liệu.
nước lợ|Nước có vị mặn nhẹ, không đậm như nước biển.
nước màu|Nước đường đặc sánh dùng để nấu kẹo.
nước máy|Nước sạch được xử lý và dẫn qua đường ống để sinh hoạt hàng ngày.
nước mắm|Nước chấm mặn thu được khi ủ cá với muối.
nước mặn|Nước có nhiều muối hòa tan, như nước ngoài biển.
nước mắt|Chất lỏng tiết ở mắt, có thể chảy ra khi xúc động.
nước ngoài|Những quốc gia hoặc vùng đất nằm ngoài lãnh thổ của chính mình.
nước ngọt|Nước có rất ít muối hòa tan, như nước sông hay nước hồ.
nước nhà|Đất nước nơi mình sinh sống.
nước non|Sông núi đại diện cho đất nước.
nước sạch|Nước đáp ứng các yêu cầu dùng cho sinh hoạt, không lẫn chất bẩn đáng kể.
nước suối|Nước chảy từ mạch ngầm sâu dưới đất lên mặt.
nước uống|Loại nước dùng để uống vào cơ thể.
nườm nượp|Hết nhóm này đến nhóm khác đi qua, đông và liên tục.
nương náu|Ẩn mình vào nơi an toàn và dựa vào sự bảo vệ của người khác.
nương nhờ|Tìm sự che chở và giúp đỡ từ người khác.
nương rẫy|Ruộng đất canh tác trên vùng đồi núi cao.
nương tựa|Cậy vào người hoặc vật khác để sống và tồn tại.
nướng|Làm chín thức ăn bằng hơi nóng, than hoặc lửa trực tiếp.
oai phong|Có vẻ uy quyền, nghiêm trang khiến người khác kính nể.
oai vệ|Có dáng vẻ uy nghi, trang trọng và bề thế.
oái oăm|Gây khó khăn, rắc rối, phức tạp và dễ làm người ta bực bội.
oang oang|Nói với âm thanh lớn và vang dội.
oanh liệt|Lẫy lừng, vang dội. Anh dũng, vẻ vang.
oi bức|Nóng ẩm khiến người ta cảm thấy khó chịu.
om sòm|Náo nhiệt, ồn ào với nhiều tiếng nói lẫn lộn.
ong bắp cày|Nhóm ong có eo thắt rõ, thường làm tổ từ vật liệu giống giấy.
ong mật|Loài ong sống theo đàn, tích trữ mật trong các ô sáp.
ong thợ|Loài ong chuyên bay đi thu thập phấn hoa để làm mật.
óng ả|Bóng ánh lấp lánh và mềm mại, uyển chuyển.
óng ánh|Mượt, bóng loáng và lấp lánh ánh sáng.
ọp ẹp|Hỏng hóc nhiều, các bộ phận rời rạc dễ đổ.
ô liu|Loài cây có quả nhỏ, thường dùng để ăn hoặc ép dầu.
ô mai|Quả mơ đã tẩm gia vị, phơi khô để ăn.
ô nhiễm|Trạng thái bị lẫn chất bẩn gây hại cho môi trường.
ổ bánh|Một chiếc bánh nguyên khối, hay nói về bánh mì chưa cắt.
ổ cắm|Bộ phận nhận phích để nối thiết bị vào nguồn điện.
ổ cứng|Bộ phận lưu dữ liệu lâu dài bằng các đĩa từ quay.
ổ đĩa|Thiết bị dùng để ghi và đọc dữ liệu từ các đĩa lưu trữ.
ổ đĩa cứng|Thiết bị lưu trữ dữ liệu lớn gắn ngoài hoặc trong máy tính.
ổ voi|Chỗ lõm sâu và to trên mặt đường, thường dùng để chỉ đường xấu.
ốc bươu|Loại ốc nước ngọt thân tròn, thường được chế biến thành món ăn.
ốc bươu vàng|Ốc nước ngọt vỏ lớn, thường đẻ trứng màu hồng trên cây ven nước.
ốc đảo|Vùng có nước và cây xanh giữa miền sa mạc.
ốc hương|Loài ốc biển nhỏ có vỏ trắng chấm nâu.
ốc quế|Vỏ bánh giòn cuộn hình nón, thường đựng kem để cầm tay.
ôi thôi|Thốt lên tiếng than thở, tiếc nuối hoặc thất vọng.
ôm ấp|Chạm vào người với tình cảm yêu thương sâu sắc.
ôm đồm|Chịu trách nhiệm làm quá nhiều việc cùng lúc.
ôn đới|Vùng đất có khí hậu mát mẻ, nằm giữa hai vùng nóng và lạnh.
ôn luyện|Lặp lại nhiều lần để ghi nhớ và làm thành thạo.
ôn tập|Học lại và luyện tập những điều đã biết để nhớ kỹ.
ồn ào|Nhiều tiếng nói to, chen lấn nhau.
ổn áp|Thiết bị giúp duy trì điện áp đầu ra gần mức định trước.
ổn định|Trạng thái không còn biến động hay thay đổi lớn.
ông bà|Cha mẹ của cha hoặc mẹ mình.
ông cụ|Người đàn ông đã lớn tuổi, thường được gọi với sự tôn kính.
ông lão|Người đàn ông đã lớn tuổi, có nhiều năm tháng.
ông ngoại|Người cha của người mẹ mình.
ông tổ|Người đầu tiên khai sinh ra một dòng họ hoặc nghề nghiệp.
ống dẫn|Ống dùng để dẫn nước hoặc khí từ nơi này sang nơi khác.
ống hút|Vật hình ống dùng để hút nước hoặc đồ ăn, thường làm bằng giấy hoặc nhựa.
ống khói|Ống dẫn khói từ bếp ra ngoài trời.
ống kính|Hệ thống thấu kính ghép thành ống để thu hoặc chiếu hình ảnh.
ống máng|Ống dẫn nước mưa từ mái nhà xuống đất hoặc bể chứa.
ống nghe|Phần máy đặt vào tai để nghe âm thanh từ đầu dây.
ống nghiệm|Ống nhỏ dài, đáy kín, dùng đựng mẫu trong phòng thí nghiệm.
ống nhòm|Dụng cụ quang học đưa hình của vật ở xa lại gần mắt.
ống quần|Phần vải quần che chân từ đầu gối xuống.
ống tay|Đoạn vải ở tay áo che phủ cánh tay người mặc.
ống thổi|Ống tre dùng để thổi hơi làm lửa cháy mạnh trong bếp.
ốp lát|Dán hoặc lát vật liệu lên bề mặt để trang trí hoặc bảo vệ.
ở đậu|Sống tạm thời ở một nơi.
ở đời|Sống trong cuộc đời.
ở lại|Còn tiếp tục sống và ở tại một chỗ khi người khác đã rời đi.
ở riêng|Sống độc lập, tách biệt khỏi gia đình cha mẹ.
ở trần|Không mặc áo, để hở phần thân trên khi ở trong nhà.
ở trọ|Ở tạm tại nhà người khác để kiếm sống.
ơi là|Lời nói thể hiện cảm xúc mạnh mẽ trước một điều gì đó đặc biệt.
ớt chuông|Loại ớt có quả to, vỏ dày, giòn và độ cay nhẹ hơn các loại ớt khác.
pa nô|Bức tranh hoặc phù điêu được đóng khung treo trên tường.
pha lê|Loại thủy tinh trong suốt, nặng hơn thủy tinh thường.
pha loãng|Trộn nước khác vào để làm nước uống bớt đặc.
pha trò|Kể chuyện vui hoặc làm động tác để gây tiếng cười.
phá cách|Không theo khuôn quen để tạo ra cách thể hiện mới.
phá cỗ|Chia bánh trái bày sẵn cho trẻ em ăn.
phá giá|Bán hàng với giá rất thấp, không đúng với giá trị thực tế.
phá lấu|Món ăn chế biến từ các bộ phận như lưỡi, tai, ruột của động vật.
phác thảo|Bản vẽ hoặc bản ghi tóm tắt các ý chính ban đầu.
phai|Mất dần sắc màu hoặc cường độ so với ban đầu.
phải chăng|Ở mức vừa và dễ chấp nhận, thường nói về giá bán.
phải đạo|Hợp với lẽ phải, đúng chuẩn mực đạo đức và công lý.
phải đường|Hành xử đúng mực, phù hợp với tình huống và đạo lý.
phải rồi|Đúng như những gì đã nói hoặc nghĩ.
phái đẹp|Tập hợp những người phụ nữ.
phái đoàn|Đoàn người được cử đi thực hiện nhiệm vụ cụ thể.
phái sinh|Cách tạo từ mới bằng cách thêm, bớt hoặc đổi phần nhỏ trong từ gốc.
phái viên|Người được cử đi thực hiện nhiệm vụ đặc biệt.
phàm nhân|Người bình thường không có tài năng đặc biệt.
phạm luật|Vi phạm, làm trái với quy định của luật.
phạm trù|Khái niệm chung để phân loại sự vật.
phạm vi|Giới hạn mà một hoạt động, quy định hay nhận định áp dụng.
phàn nàn|Nói lời than phiền về điều khiến mình không vui.
phản ánh|Thể hiện lại những nét chính của sự vật hay hiện tượng.
phản bác|Chứng minh người khác sai bằng lý lẽ và bằng chứng thật.
phản biện|Xem xét kỹ lưỡng để đưa ra ý kiến trái ngược.
phản chiếu|Hiện tượng ánh sáng bật lại từ bề mặt vật thể.
phản đối|Chống lại ý kiến hoặc hành động của người khác.
phản ứng|Hoạt động đáp lại một tác động hoặc kích thích từ bên ngoài.
phản xạ|Phản ứng tự động của cơ thể trước tác động bên ngoài.
phán đoán|Kéo ra kết luận về sự việc hoặc con người sau khi cân nhắc.
phảng phất|Lờ mờ, không rõ ràng, khó nắm bắt.
phanh|Bộ phận hãm cho xe chậm lại hoặc dừng hẳn.
phao|Vật nhẹ nổi trên nước để đánh dấu hoặc đỡ người.
phát âm|Tạo âm của một tiếng bằng các cơ quan nói.
phát biểu|Nói ra suy nghĩ, quan điểm hay cảm xúc của bản thân về một vấn đề.
phát đạt|Làm ăn sung túc, sự nghiệp tiến triển tốt.
phát điện|Tạo ra dòng điện để cung cấp năng lượng.
phát hành|Đưa ra thị trường để người khác mua hoặc phân phối các ấn phẩm.
phát hiện|Tìm ra điều chưa ai biết đến trước.
phát huy|Khai thác và phát triển tác dụng tốt của điều gì đó.
phát minh|Nghĩ ra và tạo được thiết bị hay phương pháp mới có ích.
phát ngôn|Nói ra ý kiến hoặc phát biểu một nội dung trọn vẹn.
phát sáng|Tự phát ra ánh sáng có thể thu nhận hoặc nhìn thấy.
phát sóng|Truyền tải chương trình qua sóng vô tuyến để nhiều người cùng nghe, xem.
phát thanh|Việc truyền tải thông tin đến nhiều người qua loa phóng thanh hoặc máy móc chuyên dụng.
phát thanh viên|Người đọc tin hoặc dẫn chương trình bằng giọng nói trên đài.
phát tích|Xuất hiện, nổi lên hoặc bắt đầu từ một nguồn gốc nào đó.
phát triển|Trở nên to lớn, mạnh mẽ hơn từ lúc nhỏ hoặc yếu.
phẳng lặng|Yên tĩnh, không có sóng gió hay biến động bất thường.
phẳng phiu|Trơn tru, bằng phẳng và đẹp mắt.
phẩm cách|Đức tính tốt đẹp và giá trị đạo đức của người.
phẩm chất|Nét tương đối bền vững thể hiện trong tính cách và cách cư xử.
phẩm màu|Chất phụ gia dùng để tạo hoặc làm đẹp màu cho sản phẩm.
phẩm vật|Vật phẩm quý giá, dùng để trao đổi hoặc làm của cải.
phân biệt|Nhận ra điểm khác nhau giữa hai hoặc nhiều sự vật, sự việc.
phân bón|Chất dùng để cung cấp dinh dưỡng cho cây trồng.
phân bố|Phân tán các vật hoặc người ra nhiều địa điểm khác nhau theo quy luật.
phân cách|Chia cắt hoặc ngăn chặn sự tiếp xúc giữa hai phần.
phân cảnh|Đoạn phim được quay trong cùng một lúc, nơi và hoàn cảnh nhất định.
phân cấp|Việc chia nhỏ thành nhiều bậc hoặc hạng khác nhau.
phân chia|Tách một khối hay nhóm lớn thành những phần riêng.
phân công|Giao nhiệm vụ cụ thể cho người khác để họ thực hiện.
phân định|Chia ranh giới và xác định rõ từng phần.
phân giải|Phân tích thành các phần nhỏ để hiểu rõ bản chất vấn đề.
phân lân|Chất bón giúp cây phát triển mạnh nhờ chứa nhiều phốt-pho.
phân loại|Chia nhóm các sự vật thành từng loại riêng biệt.
phân minh|Rõ ràng, tách biệt hẳn và xử lý dứt khoát từng vấn đề.
phân phát|Đem một số lượng đồ vật hoặc tiền bạc chia đều và trao cho nhiều người nhận.
phân phối|Phân chia hoặc sắp xếp các phần của một tổng thể.
phân số|Số biểu thị một phần hoặc nhiều phần bằng nhau của một đơn vị nguyên vẹn.
phân tích|Chia nhỏ ra từng phần để tìm hiểu kỹ.
phân tử|Hạt nhỏ nhất cấu tạo nên chất mà vẫn giữ tính chất đó.
phân vân|Do dự, phân tích nhiều lần mà chưa thể đưa ra quyết định.
phân xanh|Lá cây tươi được vùi xuống đất để làm phân bón.
phần cứng|Các linh kiện vật lý có thể tháo lắp của máy tính.
phần mềm|Tập hợp các lệnh và dữ liệu giúp máy tính thực hiện công việc.
phần thưởng|Vật phẩm trao tặng để ghi nhận công lao hoặc thành tích đạt được.
phần việc|Công việc thuộc trách nhiệm, phận sự của mình phải làm.
phấn đấu|Cố gắng hết sức để đạt được mục tiêu mong muốn.
phấn khích|Cảm thấy vui mừng, hăng hái và đầy nhiệt huyết.
phấn khởi|Cảm thấy vui vẻ và hăng hái trong lòng.
phận sự|Việc riêng mà mỗi người phải làm.
phấp phới|Bay lượn, rung động trước gió.
phất|Đưa nhanh một vật nhẹ lên cao, như khi vẫy cờ.
phất phơ|Lang thang đi khắp nơi mà không có mục đích rõ ràng.
phẩy|Đưa nhẹ cổ tay theo một nét ngắn và nhanh.
phép|Sự đồng ý cho một người được làm việc nào đó.
phép chia|Phép toán tìm thương khi biết số bị chia và số chia.
phép cộng|Cách gộp các số đơn vị thành tổng chung.
phép giải|Cách tính toán để tìm ra kết quả cuối cùng.
phép nhân|Phép tính lấy một số nhân với số khác để tìm tích.
phép tính|Cách thức tính toán để tìm kết quả số mới từ các số đã biết.
phê duyệt|Xem xét rồi chính thức chấp nhận kế hoạch hoặc đề xuất.
phê phán|Phân tích để chỉ rõ điểm tốt, điểm xấu của một việc hay tác phẩm.
phế liệu|Vật liệu hỏng nhưng còn dùng lại được.
phế phẩm|Sản phẩm làm ra không đạt tiêu chuẩn hoặc bị loại bỏ.
phế thải|Vật chất, vật liệu hoặc sản phẩm bị bỏ đi vì hết giá trị, hết hạn hay không dùng được.
phế tích|Vật thể đổ nát, chỉ còn dấu vết của công trình cũ.
phên|Tấm nan tre hoặc nứa đan thành mặt phẳng để che.
phết|Trải một lớp mỏng lên bề mặt, như bơ lên bánh.
phễu|Đồ miệng rộng, có ống nhỏ để rót vào chai.
phi công|Người điều khiển máy bay hoặc tàu vũ trụ.
phi cơ|Phương tiện bay dùng để chở người hoặc hàng hóa trên không trung.
phi hành đoàn|Tập hợp phi công và nhân viên phục vụ trên máy bay.
phi lao|Cây thân gỗ có cành nhỏ như sợi, thường trồng chắn gió ven biển.
phi thường|Khác hẳn mọi người, xuất sắc và đáng được khen ngợi.
phì nhiêu|Đất màu mỡ, thích hợp cho cây cối sinh trưởng tốt.
phí phạm|Làm hỏng, lãng phí hoặc sử dụng không đúng mục đích cần thiết.
phí tổn|Số tiền chi ra cho công việc hoặc hoạt động nào đó.
phía|Một bên hoặc một hướng so với điểm đang xét.
phía sau|Vị trí nằm ở phía ngược lại với hướng nhìn thẳng hoặc phía trước của cơ thể.
phía trước|Hướng đối diện với phía sau, nơi mắt nhìn thấy trước tiên.
phích|Bình có vỏ cách nhiệt để giữ nước nóng lâu.
phích nước|Bình giữ nhiệt dùng để trữ nước nóng sau khi đun.
phiên|Một lượt diễn ra theo lịch, như buổi họp hoặc buổi chợ.
phiên âm|Viết lại âm thanh của từ nước ngoài bằng âm tiếng Việt.
phiên bản|Bản sao chép hoặc chỉnh sửa từ nguyên bản.
phiên dịch|Chuyển lời nói từ ngôn ngữ này sang ngôn ngữ khác.
phiền hà|Gây ra nhiều rắc rối, phiền toái và phức tạp cho người khác.
phiền lòng|Cảm thấy buồn rầu, khó chịu hoặc bực bội trong lòng.
phiến diện|Chỉ nhìn nhận vấn đề từ một phía, thiếu toàn diện.
phiến lá|Phần chính của lá cây, hình dạng dẹt, rộng và màu xanh.
phiêu diêu|Bay lượn nhẹ nhàng, di chuyển tự do ở trên không.
phiêu lưu|Dấn bước vào hành trình có điều mới lạ và chưa chắc chắn.
phiếu|Mảnh giấy hoặc biểu mẫu ghi thông tin cho một việc.
phim ảnh|Tên gọi chung tác phẩm điện ảnh hoặc những hình được ghi trên phim.
phim hoạt hình|Phim tạo hình ảnh chuyển động từ các bức tranh vẽ liên tiếp.
phím|Nút bấm trên bàn chữ hoặc trên một số nhạc cụ.
phin|Dụng cụ giữ bột cà phê và cho nước nhỏ xuống cốc.
phình|Nở ra, làm một phần trở nên to và căng.
phó bản|Bản sao chép y nguyên từ bản gốc để làm tài liệu phụ.
phó hiệu trưởng|Người giúp hiệu trưởng phụ trách một số phần việc của trường.
phong ba|Thời tiết có gió lớn, sóng dữ và nhiều biến cố.
phong bao|Gói tiền dùng để tặng người khác trong dịp lễ tết.
phong bì|Bao giấy mỏng để đựng thư hoặc giấy tờ.
phong cách|Cách thể hiện riêng dễ nhận ra qua việc làm, ăn mặc hoặc sáng tác.
phong cảnh|Tổng thể các cảnh đẹp của thiên nhiên và con người trước mắt.
phong cầm|Nhạc cụ hơi có phần bễ xếp, phát tiếng khi kéo và ép bễ.
phong độ|Mức thể hiện khả năng của một người tại một thời điểm.
phong lan|Lan thường bám trên thân cây, có rễ lộ ra ngoài không khí.
phong lưu|Có phong thái lịch sự, sang trọng hoặc giàu có.
phong nhã|Có vẻ ngoài thanh lịch, tao nhã và mực thước.
phong phú|Nhiều và đủ các thứ cần thiết cho cuộc sống.
phong quang|Có cảnh đẹp, không khí trong lành và thoáng đãng.
phong thái|Dáng vẻ và cách ứng xử tạo ấn tượng riêng về một người.
phong thư|Lá thư đặt trong phong bì để gửi cho người nhận.
phong trào|Hoạt động tập thể có đông đảo người tham gia cùng nhau.
phong tục|Thói quen, cách ứng xử và hoạt động chung được hình thành và duy trì trong một cộng đồng.
phòng|Khoảng bên trong nhà được ngăn riêng bằng vách.
phòng ăn|Gian nhà dành cho việc dùng bữa.
phòng ban|Các bộ phận làm việc riêng biệt trong cơ quan.
phòng giữ|Chuẩn bị trước để ngăn chặn và giữ lại điều không mong muốn.
phòng khi|Sẵn sàng đối phó với những tình huống xấu có thể xảy ra bất ngờ.
phòng ngủ|Gian nhà dành cho việc nằm ngủ và nghỉ ngơi.
phòng ngừa|Tránh không để điều xấu xảy ra trước khi nó đến.
phòng tắm|Căn phòng dùng để tắm rửa và vệ sinh cơ thể.
phòng thí nghiệm|Không gian riêng có dụng cụ để làm thí nghiệm khoa học.
phòng tối|Hộp kín có thấu kính để chiếu sáng và tạo ảnh rõ nét.
phòng tránh|Làm việc trước để chủ động tránh những điều bất lợi có thể xảy ra.
phòng trọ|Phòng cho thuê để người khác ở tạm hoặc ở theo tháng.
phỏng chừng|Ước lượng hoặc đoán một cách đại khái, không đảm bảo chính xác tuyệt đối.
phỏng đoán|Ước lượng kết quả dựa trên những dấu hiệu chưa chắc chắn.
phỏng vấn|Hỏi ý kiến người khác để đưa tin cho công chúng biết.
phóng đại|Nói hoặc làm cho sự vật to hơn mức thực tế.
phóng khoáng|Không chịu những ràng buộc nhỏ nhặt, cứng nhắc.
phóng sự|Bài viết thuật lại sự việc thật đã xảy ra.
phóng tác|Viết lại kịch bản hoặc câu chuyện dựa trên nội dung tác phẩm khác.
phóng thanh|Sử dụng thiết bị để làm cho tiếng nói to hơn, vang xa.
phóng viên|Người chuyên đi thu thập tin tức để viết bài đăng trên báo chí hoặc phát trên đài.
phô diễn|Thể hiện ra trước người khác để họ thấy rõ tài nghệ hay đặc điểm.
phô trương|Bày ra ngoài để khoe mẽ hoặc làm cho đẹp bề ngoài.
phổ biến|Có tính chất chung, dùng được cho nhiều sự vật, hiện tượng.
phổ cập|Phổ biến đến khắp mọi nơi.
phổ dụng|Dùng rộng rãi cho nhiều người, nhiều nơi.
phổ thông|Phổ biến, dành cho đại đa số người học hoặc sử dụng hàng ngày.
phố phường|Tổng hợp các con đường và khu dân cư trong thành phố.
phố xá|Đường lớn và đường nhỏ trong khu dân cư.
phối giống|Giao phối để sinh ra con cái hoặc tạo ra giống mới.
phối hợp|Kết nối các phần việc để nhiều bên cùng đạt một kết quả.
phối trộn|Trộn lẫn các chất lại với nhau theo một tỷ lệ đã định trước.
phồn vinh|Phát triển thịnh vượng, giàu có và sung túc.
phông nền|Mặt hoặc cảnh ở phía sau đối tượng chính khi chụp hay biểu diễn.
phở xào|Loại phở khô được xào chín với hành và mỡ.
phơi|Để ngoài nắng, gió cho thoáng hoặc khô.
phơi phới|Tươi vui, tràn đầy sức sống và hy vọng về tương lai.
phớt lờ|Không thèm để ý, bỏ qua việc người khác nói hay làm.
phu thê|Người vợ và người chồng.
phù du|Côn trùng có giai đoạn non sống dưới nước, trưởng thành thường sống rất ngắn.
phù dung|Loài cây có hoa to, sáng nở màu trắng, chiều tàn chuyển sang hồng, dùng làm cảnh.
phù điêu|Tác phẩm điêu khắc nổi trên mặt phẳng để kể chuyện hoặc trang trí.
phù hiệu|Dấu đeo trên áo hay mũ để nhận biết đơn vị hoặc vai trò.
phù hợp|Ăn khớp với điều kiện, nhu cầu hoặc tiêu chuẩn đang xét.
phù rể|Người đàn ông đi cùng chú rể trong đám cưới để hỗ trợ.
phù sa|Đất màu mỡ bị nước cuốn trôi và lắng xuống.
phủ định|Bác bỏ, không công nhận sự thật hay giá trị.
phủ nhận|Không công nhận là đúng hoặc không thừa nhận.
phú thịnh|Giàu có, sung túc và phát triển mạnh mẽ về mọi mặt.
phụ âm|Âm được tạo ra khi đường thoát của hơi bị chặn hoặc thu hẹp.
phụ cấp|Số tiền thêm vào lương hoặc thu nhập chính.
phụ đề|Dòng chữ trên phim hoặc video thể hiện lời thoại hay bản dịch.
phụ gia|Chất liệu được thêm vào để hỗ trợ hoặc làm đẹp.
phụ huynh|Cha mẹ hoặc người chăm sóc học sinh trong quan hệ với nhà trường.
phụ kiện|Bộ phận lắp thêm để hỗ trợ, hoàn thiện chức năng cho thiết bị chính.
phụ lục|Phần bổ sung đặt sau nội dung chính của sách hoặc tài liệu.
phụ nữ|Những người nữ đã trưởng thành.
phụ phẩm|Phần vật chất còn lại sau khi tách lấy phần chính cần dùng.
phụ phí|Tiền phải trả thêm ngoài số tiền đã thỏa thuận ban đầu.
phụ tải|Thiết bị dùng để tiêu thụ và chuyển hóa năng lượng điện.
phụ thu|Thu thêm một khoản tiền ngoài số tiền đã quy định.
phụ thuộc|Cần đến người, vật hoặc điều kiện khác mới thực hiện được.
phụ trách|Đảm nhận nhiệm vụ và chịu trách nhiệm làm.
phụ trợ|Giúp thêm vào việc làm chính để hoàn thành.
phụ tùng|Bộ phận rời dùng để thay thế hay lắp vào máy.
phúc đáp|Viết lại câu trả lời cho người hỏi.
phúc hậu|Có tính tình tốt bụng, nhân hậu và phúc đức.
phúc lợi|Những quyền lợi hỗ trợ đời sống ngoài khoản thu nhập chính.
phúc mạc|Lớp màng mỏng bao phủ và che chở các cơ quan bên trong bụng.
phúc trình|Văn bản ghi lại kết quả làm việc để báo cáo cho cấp trên.
phục hồi|Trở lại trạng thái ban đầu hoặc làm cho cái đã mất lại có được.
phục vụ|Làm những việc cần thiết để giúp đỡ người khác.
phủi|Dùng tay gạt nhẹ cho bụi hay vụn rơi đi.
phun|Đẩy chất lỏng hoặc khí ra thành tia hay thành hạt nhỏ.
phung phí|Sử dụng tài sản hoặc nguồn lực một cách quá mức, không cần thiết.
phụng dưỡng|Chăm sóc ăn uống cho người lớn tuổi.
phụng sự|Làm việc giúp đỡ người khác bằng toàn bộ tấm lòng.
phút|Đơn vị thời gian dài bằng sáu mươi giây.
phức tạp|Gồm nhiều chi tiết liên kết khiến việc hiểu hay làm rất khó khăn.
phương án|Lời dự tính việc cần thực hiện.
phương châm|Điều định hướng để giữ cách làm nhất quán trong công việc.
phương diện|Một khía cạnh riêng biệt được tách ra để xem xét.
phương hướng|Con đường chỉ về phía cần đi hoặc lối làm việc.
phương pháp|Cách làm và quy tắc cần tuân theo để hoàn thành nhiệm vụ hiệu quả.
phương sách|Cách thức để giải quyết vấn đề.
phương thức|Cách thức thực hiện hoặc phương pháp làm việc.
phương tiện|Cái dùng để giúp thực hiện công việc.
phương tiện vận tải|Xe, tàu hoặc thiết bị dùng để chuyên chở người và hàng.
phương trình|Đẳng thức có ẩn số cần tìm để hai vế bằng nhau.
pin sạc|Loại pin có thể nạp lại điện năng sau khi hết.
qua lại|Hoạt động qua đi và trở lại giữa hai bên.
qua loa|Làm nhanh cho xong mà chưa chú ý đủ đến chi tiết.
qua mặt|Không để ý đến, bỏ qua hoặc vượt lên trên người khác.
qua quýt|Làm việc một cách sơ sài, qua loa chỉ để cho xong chuyện.
quà cáp|Vật phẩm dùng để biếu tặng người khác.
quà tặng|Vật phẩm được tặng cho người khác mà không đòi hỏi tiền.
quà vặt|Món ăn nhỏ dùng giữa các bữa, như bánh, kẹo hay trái cây.
quả cầu|Vật tròn đều trong không gian như một trái bóng.
quả là|Chính xác là như vậy.
quả mọng|Trái cây nhỏ, mềm, có nhiều nước và vị ngọt.
quả nhiên|Đúng y như lời đoán trước hoặc như sự thật hiển nhiên.
quả quyết|Nói chắc chắn, không do dự hay e ngại.
quả thật|Đúng sự thật, không có gì phải nghi ngờ.
quá bán|Đi qua con số một nửa của tổng thể.
quá cảnh|Đi qua lãnh thổ nước này để đến nước khác.
quá chừng|Đạt mức độ cao hơn hẳn so với mức bình thường.
quá đà|Quá mức cho phép, vượt khỏi giới hạn.
quá đáng|Vượt quá mức cần thiết hoặc mức cho phép, gây khó chịu.
quá đỗi|Đến mức vượt quá giới hạn bình thường.
quá khứ|Thời gian đã trôi qua, không còn tồn tại ở hiện tại.
quá lời|Nói những điều vượt quá mức cần thiết, khiến người nghe khó chịu hoặc bị tổn thương.
quá mức|Vượt qua giới hạn cho phép hoặc mức độ cho phép.
quá sức|Làm việc vượt quá khả năng chịu đựng của bản thân.
quá tải|Vượt quá khả năng chịu đựng hoặc sức chứa cho phép.
quá trình|Đường đi của sự biến đổi, phát triển hoặc tiến triển theo thời gian.
quá trời|Quá mức, vượt xa thường lệ đến mức lạ.
quá trớn|Làm việc vượt quá mức cho phép hoặc giới hạn quy định.
quai hàm|Hai khối xương cứng bao bọc và nâng đỡ răng hàm dưới.
quái gở|Kỳ lạ, khác thường đến mức khó tin.
quan điểm|Cách nhìn nhận, đánh giá vấn đề dựa trên lập trường và tư duy riêng của mỗi người.
quan hệ|Sự liên kết chặt chẽ giữa các sự vật hoặc con người với nhau.
quan họ|Lối hát đối đáp truyền thống gắn với vùng Kinh Bắc.
quan khách|Người được mời đến tham dự sự kiện hoặc buổi lễ.
quan niệm|Cách hiểu riêng về sự vật hay vấn đề.
quan sát|Nhìn kỹ và ghi nhận chi tiết của sự vật hay hiện tượng.
quan sát viên|Người đứng xem, ghi chép và phân tích sự việc diễn ra.
quan trắc|Nhìn và ghi chép các hiện tượng tự nhiên để biết thông tin.
quan trọng|Có giá trị to lớn, tác động mạnh mẽ và đáng được ưu tiên.
quản đốc|Người giám sát và ra lệnh cho công nhân trong nhà máy.
quản ngại|Không dám làm vì e ngại hoặc thấy khó khăn.
quản trị|Tổ chức và điều hành con người, nguồn lực hay hệ thống.
quán chiếu|Quá trình suy nghĩ sâu sắc để tìm hiểu sự vật.
quán tính|Khả năng vật giữ nguyên trạng thái chuyển động khi không bị lực cản.
quán xuyến|Quản lý và điều hành trọn vẹn mọi công việc.
quang cảnh|Toàn cảnh nhìn thấy từ một vị trí vào một thời điểm.
quang đãng|Sáng rõ, thoáng đãng và rộng rãi.
quang gánh|Bộ đòn vai cùng hai quang để mang vật nặng hai bên.
quang học|Môn nghiên cứu về ánh sáng và bức xạ.
quang minh|Sáng rõ, dễ thấy và không che giấu.
quang năng|Năng lượng có trong ánh sáng, được dùng để tạo ra điện hoặc hỗ trợ sự sống của thực vật.
quang phổ|Dải màu cầu vồng xuất hiện khi ánh sáng bị tán sắc.
quang vinh|Được khen ngợi vì có nhiều thành tích tốt đẹp.
quảng bá|Phổ biến rộng rãi thông tin đến nhiều người.
quảng cáo|Truyền tin về món hàng hay sự kiện để thu hút nhiều người biết và mua.
quảng đại|Rộng rãi, bao dung, dễ tha thứ.
quảng trường|Khu đất rộng trong thành phố dành cho công cộng.
quanh co|Đổi hướng nhiều lần thay vì đi theo đường thẳng.
quanh năm|Suốt cả thời gian trong một năm.
quanh quẩn|Di chuyển lặp đi lặp lại trong một khu vực nhỏ, không đi xa khỏi nơi ban đầu.
quanh quất|Ở gần nơi mình đang đứng hoặc sinh sống, không đi xa.
quạnh hiu|Không có người qua lại, không khí trống trải.
quạnh quẽ|Vắng người, không có ai đến sinh hoạt.
quạt giấy|Cái dùng nan tre và giấy để phất tan gió nóng.
quạt máy|Thiết bị quay cánh bằng động cơ để tạo luồng gió.
quạt nan|Quạt làm bằng những thanh tre mỏng đan chéo nhau.
quạt thông gió|Thiết bị điện dùng để làm không khí lưu thông trong phòng kín.
quạt trần|Thiết bị có cánh quay, lắp trên trần nhà để làm mát không khí.
quay lại|Đi trở về nơi đã từng ở hoặc quay mặt về phía sau.
quay phim|Chạy máy quay để ghi lại hình ảnh chuyển động.
quay tay|Quay bánh lái tàu hoặc cuộn phim bằng tay.
quắc thước|Tinh thần sảng khoái, thể lực sung mãn dù tuổi đã cao.
quần áo|Những thứ may để mặc và che thân.
quần âu|Loại quần dài có cạp cao, ống đứng và dáng gọn gàng theo kiểu phương Tây.
quần bò|Quần may bằng loại vải denim chắc, thường có màu xanh chàm.
quần đảo|Nhóm nhiều hòn đảo nằm gần nhau trong biển.
quần đùi|Quần có ống ngắn, phần lớn đùi hoặc cẳng chân để hở.
quần soóc|Quần ống ngắn, cạp cao trên đầu gối.
quần tất|Quần bó sát da, co giãn được, che từ mắt cá chân lên đến đầu gối.
quần thể|Tập hợp nhiều cá thể cùng loài sống chung trong một khu vực.
quần vợt|Môn thể thao dùng vợt để đánh bóng qua lưới trên sân phẳng.
quẫn bách|Khốn khó, túng thiếu đến mức không còn lối thoát.
quấn quýt|Luôn ở bên nhau vì yêu thương, không muốn rời.
quật cường|Mạnh mẽ, kiên cường, không chịu khuất phục trước áp lực.
quây quần|Tập hợp lại gần nhau trong không khí thân thiết, vui vẻ.
quầy lễ tân|Khu vực trong văn phòng dùng để đón tiếp khách và làm thủ tục đầu tiên.
quấy rầy|Làm phiền, gây khó chịu cho người khác.
quen biết|Đã từng tiếp xúc nên nhận ra và có quan hệ với nhau.
quen dần|Thích nghi từ từ với khí hậu, thời tiết hoặc môi trường mới.
quen mặt|Trông thấy khuôn mặt đã từng gặp, dễ dàng nhận ra người đó.
quen thuộc|Đã gặp nhiều lần nên dễ nhận ra và không thấy lạ.
quét dọn|Dùng chổi, khăn để lau sạch bụi bẩn và rác.
quê hương|Nơi sinh ra và lớn lên của một người.
quê người|Nơi ở xa, không phải quê hương.
quê nhà|Nơi sinh ra và lớn lên của bản thân.
quê quán|Nơi sinh ra và lớn lên của một người, gốc gác gia đình.
quên bẵng|Hoàn toàn không nhớ đến một điều gì đó.
quốc hoa|Loài hoa đại diện cho vẻ đẹp và bản sắc của một đất nước.
quốc lộ|Đường giao thông lớn do nhà nước quản lý.
quốc tế|Liên quan đến nhiều nước hoặc quan hệ giữa các nước.
quốc tịch|Tư cách công dân của một quốc gia cụ thể.
quốc văn|Ngôn ngữ chính thức của đất nước.
quở trách|Nói lời nghiêm khắc để phê bình lỗi lầm của người dưới.
quyên góp|Tập hợp tiền của từ nhiều người để làm việc thiện.
quyền biến|Biết cách ứng xử linh hoạt trước những tình huống bất ngờ.
quyền hạn|Quyền lực được giao do chức vụ hoặc cương vị.
quyền lợi|Những lợi ích một người được hưởng theo thông lệ hay quy định.
quyền tác giả|Quyền sở hữu và kiểm soát tác phẩm do mình tạo ra.
quyến luyến|Tình cảm gắn bó sâu sắc, không muốn chia ly.
quyến rũ|Gây mê hoặc thu hút người khác bằng vẻ đẹp và sức hấp dẫn.
quyến thuộc|Những người có quan hệ huyết thống gần gũi và thân thiết.
quyết chí|Có ý định mạnh mẽ và kiên định để hoàn thành việc mình muốn.
quyết đoán|Dùng ý chí mạnh mẽ để ra quyết định dứt khoát.
quyết sách|Các quyết định quan trọng để định hướng công việc chung.
quyết tâm|Thái độ kiên định, nỗ lực hết sức để hoàn thành mục tiêu đã đặt ra dù gặp khó khăn.
ra công|Dùng hết sức lực và công sức để làm một việc gì đó.
ra dáng|Có vẻ ngoài giống với hình ảnh người ta thường thấy.
ra đời|Khởi đầu, được thành lập hoặc xuất hiện vào đời.
ra hiệu|Làm động tác để báo hiệu hoặc truyền tin.
ra hồn|Đủ điều kiện cần thiết để được gọi là như vậy.
ra mắt|Xuất hiện chính thức lần đầu trước công chúng hoặc một nhóm người.
ra sao|Ở trong tình trạng, hoàn cảnh hoặc mức độ như thế nào.
ra sức|Nỗ lực hết sức mình để làm việc.
ra vào|Di chuyển từ bên trong ra ngoài hoặc từ bên ngoài vào trong.
ra vẻ|Trông có vẻ như vậy hoặc giả tạo hình thức bên ngoài.
rách|Bị đứt thành đường hoặc lỗ trên vải, giấy.
rách rưới|Rách nhiều quá, thường do quá nghèo túng.
rải rác|Nằm hoặc xuất hiện tách nhau ở nhiều chỗ khác nhau.
rái cá|Thú bán thủy sinh bơi giỏi, thân thuôn và thường ăn cá.
rám nắng|Da trở nên sẫm màu do tiếp xúc nhiều với nắng.
rạn nứt|Xuất hiện những đường nứt nhỏ trên bề mặt vốn liền.
ràng buộc|Buộc phải tuân theo quy định, không được tự do thay đổi.
rạng danh|Làm cho tên tuổi trở nên vang dội, được nhiều người biết đến.
rạng đông|Thời điểm ánh ngày đầu tiên xuất hiện ở chân trời.
rạng rỡ|Sáng sủa, tỏa ra vẻ đẹp lộng lẫy và rực rỡ.
ranh giới|Đường vạch ra để phân chia hai bên.
ranh mãnh|Tinh ranh, thông minh nhưng hay làm trò nghịch ngợm.
rành mạch|Nói hoặc viết rõ ràng, mạch lạc, dễ hiểu.
rành rành|Hết sức rõ ràng, dễ thấy và dễ hiểu.
rành rõ|Biết rõ, thông thạo và hiểu sâu sắc về một việc.
rành rọt|Rõ ràng từng chi tiết, không lẫn lộn.
rảnh rang|Rảnh rỗi, không có việc gì phải làm.
rảnh rỗi|Có thời gian trống vì chưa bận việc phải làm.
rảnh tay|Không bận rộn, có thời gian rỗi.
rãnh|Đường lõm hẹp chạy dài trên một bề mặt.
rao vặt|Bài quảng cáo đăng bán hàng hóa giá rẻ.
ráo riết|Làm việc rất khẩn trương, nghiêm túc và không bỏ sót chi tiết.
rau cần|Rau thân giòn mọc ở nơi ẩm, thường dùng xào hoặc nấu canh.
rau câu|Loài tảo đỏ mọc ven biển, dùng để nấu thạch hoặc làm rau ăn.
rau chân vịt|Rau ăn lá còn gọi là cải bó xôi.
rau diếp|Loài rau có lá mềm, thường dùng để ăn kèm với các món khác.
rau má|Rau bò sát đất, lá tròn hơi khía, dùng ăn hoặc xay lấy nước.
rau màu|Các loại rau và hoa dùng để ăn làm thực phẩm.
rau mùi|Rau gia vị lá nhỏ xẻ thùy, có mùi thơm đặc trưng.
rau muống|Rau thân rỗng hay mọc ở nơi ẩm, ăn được ngọn và lá.
rau ngót|Cây bụi có lá nhỏ, thường tuốt lá để nấu canh.
rau răm|Rau mọc bò, lá nhọn, mùi thơm cay, dùng làm gia vị.
rau sam|Loài cây bò, lá dày nhỏ màu tím, vị đắng nhớt dùng ăn.
rau sống|Rau dùng để ăn trực tiếp không qua nấu chín.
rắc rối|Phức tạp, nhiều chi tiết khiến việc giải quyết trở nên khó khăn.
răm rắp|Làm việc đều đặn, nhanh chóng và không bỏ sót gì.
rắn chắc|Cứng và bền, không bị mềm hay gãy.
răng|Các phần cứng mọc trong miệng để cắn và nhai.
răng cửa|Những răng nằm phía trước hàm, có cạnh để cắn thức ăn.
răng giả|Nha răng nhân tạo thay thế răng thật đã rụng hoặc bị hỏng.
răng hàm|Những răng ở phía trong khoang miệng, chủ yếu để nghiền thức ăn.
răng khôn|Răng hàm cuối cùng mọc ra khi người đã trưởng thành.
răng nanh|Chiếc răng nhọn nằm giữa răng cửa và nhóm răng phía trong.
răng sữa|Răng trắng, mềm yếu mọc ở trẻ nhỏ trước răng vĩnh viễn.
râm ran|Nhiều tiếng nói cười vang lên rộn rã liên tục.
rầm rộ|Náo nhiệt, ồn ào và có nhiều người tham gia cùng lúc.
rậm rịch|Gợi âm thanh trầm, nặng, liên tục do nhiều người làm việc khẩn trương.
rất là|Độ lớn vượt quá mức thông thường.
rất mực|Ở mức độ rất cao, vượt quá mức bình thường.
râu quai nón|Râu mọc nối từ hai bên má vòng xuống cằm.
rẻ quạt|Đồ trang trí hình nan quạt xếp chồng lên nhau, thường dùng làm quạt hoặc che chắn.
rèn luyện|Tập luyện nhiều lần để thành thạo.
reo hò|La hét lớn tiếng để thể hiện niềm vui hoặc cổ vũ.
réo rắt|Tiếng hát trong trẻo, hay, nghe rất dễ chịu tai.
rễ cây|Phần thân cây đâm xuống đất để hút nước và chất dinh dưỡng.
rêu rao|Nói toạc ra ngoài, thường với ý đồ xấu.
rì rào|Tiếng đều và nhẹ như lá cây hoặc sóng nhỏ chuyển động.
riêng biệt|Thuộc về một vật riêng, không giống với các vật khác.
riêng lẻ|Tách ra thành từng cái một, không dính dáng với nhau.
riêng rẽ|Tách biệt, không cùng chung một chỗ.
riêng tư|Thuộc về cá nhân, không chia sẻ với người khác.
riềng|Cây họ gừng, có thân rễ thơm dùng làm gia vị.
riêu|Món nước chua nhẹ, thường nấu với cua đồng.
riu riu|Chảy nhỏ giọt đều đặn, nhẹ nhàng.
ríu rít|Nhiều tiếng trong, ngắn tiếp nhau như tiếng chim gọi đàn.
rõ ràng|Dễ thấy, không che khuất, hiển nhiên.
róc rách|Tiếng nước nhỏ chảy liên tục qua sỏi đá hoặc khe hẹp.
rón rén|Đi đứng nhẹ nhàng, cẩn thận để tránh gây tiếng động.
rong chơi|Đi dạo tự do, không có mục đích cụ thể hay kế hoạch rõ ràng.
rong ruổi|Đi lại nhiều nơi một cách vui vẻ.
ròng rã|Kéo dài liên tục không có lúc nghỉ hay gián đoạn.
ròng rọc|Bánh xe có rãnh dẫn dây để kéo vật hay đổi hướng lực.
rối bù|Tóc rối, lộn xộn, quấn chặt vào nhau.
rối nước|Nghệ thuật điều khiển con rối trên mặt ao hoặc bể nước.
rối rắm|Ngôn ngữ lộn xộn, khó hiểu, không mạch lạc.
rối rít|Vội vã làm hoặc nói nhiều việc, việc nọ tiếp ngay việc kia.
rôm rả|Hoạt động tấp nập, vui vẻ, nhiều người.
rộn rã|Nhiều tiếng nói ồn ào, náo nhiệt và vui tươi.
rộn ràng|Nơi đông người, hoạt động tấp nập.
rồng|Con vật tưởng tượng thân dài có vảy, xuất hiện trong truyền thuyết.
rỗng tuếch|Không chứa đựng gì bên trong, trống rỗng hoàn toàn.
rộng lớn|Diện tích hoặc phạm vi bao trùm rất rộng.
rộng lượng|Có lòng bao dung, sẵn sàng tha thứ và yêu thương người khác.
rộng mở|Không đóng cửa, sẵn sàng tiếp nhận và chia sẻ.
rộng rãi|Phạm vi trải khắp nhiều nơi.
rơi rớt|Còn sót lại một phần nhỏ sau khi đã chia hoặc lấy đi.
rơi tự do|Trạng thái vật rơi chỉ chịu lực hút của Trái Đất.
rời rạc|Không liên kết chặt chẽ với nhau, bị chia cắt thành từng phần.
rơm rớm|Chảy ra từng giọt nhỏ li ti trên bề mặt da hoặc vật.
ru ngủ|Làm cho người khác buồn ngủ, mất tập trung.
ru rú|Sống quanh quẩn trong không gian nhỏ, không dám đi xa.
rủ rê|Mời người khác cùng tham gia một việc, thường bằng lời thân mật.
rũ rượi|Mô tả mái tóc xõa ra, rối rắm và bết dính.
rùa biển|Rùa sống ở biển, có chi dạng mái chèo để bơi.
rục rịch|Làm việc gì đó từ từ, âm thầm để chuẩn bị cho tương lai.
run run|Cơ thể hơi run rẩy.
rung chuyển|Làm rung động mạnh hoặc lay động sâu sắc tâm trí.
rung động|Lay chuyển nhẹ hoặc cảm thấy hồi hộp vì xúc động.
rung rinh|Lung lay nhẹ nhàng như có gió thổi qua.
ruốc tôm|Món ăn khô màu hồng, thơm ngọt, làm từ tôm he rim nhỏ, ăn với cơm hoặc bánh mì.
ruồi|Côn trùng nhỏ chỉ có một đôi cánh dùng để bay.
ruộng|Khoảnh đất người ta làm để gieo trồng, nhất là trồng lúa.
ruộng bậc thang|Đất trồng lúa trên sườn núi, được làm thành từng tầng bậc.
ruộng đất|Đất đai dùng để gieo trồng cây cối.
ruộng lúa|Đất trồng lúa.
ruộng nương|Đất trồng lúa và cây ăn trái nói chung.
ruột|Ống tiêu hóa nối từ dạ dày xuống phần cuối đường tiêu hóa.
ruột gan|Tâm tư, cảm xúc bên trong con người.
ruột già|Phần ruột nối giữa ruột non và hậu môn, nằm ngang bụng.
ruột non|Phần ruột nằm giữa dạ dày và ruột già để tiêu hóa thức ăn.
rút gọn|Làm cho ngắn gọn, đơn giản hơn về hình thức.
rút lui|Hành động rời bỏ vị trí hiện tại để di chuyển về phía sau hoặc về nơi an toàn.
rút ngắn|Làm cho ngắn lại, bớt đi một phần.
rút thăm|Lấy những tờ giấy kín để chọn người được hưởng lợi.
rụt rè|Tỏ vẻ e dè, không dám mạnh dạn làm những điều mình muốn.
ruy băng|Dải vải dài dùng để trang trí hoặc buộc vào vật khác.
rực rỡ|Sáng rực, đẹp lộng lẫy và nổi bật.
rừng|Vùng đất có nhiều cây mọc thành quần thể rộng.
rừng cấm|Rừng được bảo vệ, cấm người vào chặt phá hoặc khai thác gỗ.
rừng già|Rừng có nhiều cây cổ thụ lớn tuổi và to lớn.
rước|Đón và đưa người hay vật đi một cách trang trọng.
rườm rà|Có nhiều chi tiết thừa khiến khó theo dõi hoặc sử dụng.
rướn|Vươn thân hoặc nhón cao để tới xa hơn.
sa bàn|Mô hình thu nhỏ bằng đất hoặc vật liệu mô phỏng địa hình.
sa lầy|Chìm vào nơi đất mềm, khó di chuyển, thường ví cảnh gặp khó khăn, khó thoát.
sa mạc|Vùng rất khô hạn, ít mưa và có thảm thực vật thưa.
sa sút|Trở nên nghèo khó, kém tiến bộ hoặc suy giảm dần về chất lượng.
sa tế|Hỗn gia ớt, dầu và sả để ướp thức ăn, thường dùng cho lẩu.
sà lan|Thuyền chở hàng có đáy bằng, thành thấp, chạy trên sông hoặc trong cảng.
sách|Tập trang có chữ hoặc hình để đọc và tra cứu.
sách báo|Tổng hợp các loại sách và báo chí để đọc.
sách dẫn|Danh mục liệt kê các mục lục để tra cứu nhanh.
sách giáo khoa|Cuốn sách được biên soạn theo chương trình học để dùng trong nhà trường.
sách vở|Tài liệu dùng để học tập và nghiên cứu.
sạch sẽ|Không có bụi bẩn, rác rưởi hoặc đồ đạc lộn xộn.
sai bảo|Ra lệnh cho người khác làm theo ý mình.
sai biệt|Khác nhau rõ rệt, không giống nhau.
sai khiến|Ra lệnh cho người khác phải làm theo ý muốn của mình.
sai lầm|Trái với yêu cầu thực tế hoặc lẽ phải, gây hậu quả xấu.
sai sót|Lỗi nhỏ xảy ra trong quá trình làm việc hoặc xử lý công việc.
sai số|Độ chênh giữa kết quả đo hay tính và giá trị được dùng làm chuẩn.
san bằng|Làm cho mặt phẳng hoặc làm cho các phần bằng nhau.
san hô|Động vật nhỏ thường sống thành tập đoàn, nhiều loài tạo rạn đá vôi.
san phẳng|Làm cho mặt đất hoặc vật trở nên bằng phẳng, không còn gồ ghề.
san sát|Có nhiều vật nằm ngay cạnh nhau, chừa rất ít khoảng trống.
san sẻ|Chia một phần tài sản, công việc hoặc gánh nặng cho người khác.
sản lượng|Số lượng sản phẩm làm ra trong một khoảng thời gian.
sản phẩm|Vật tạo ra nhờ sức lao động của người hoặc máy.
sản sinh|Tạo ra, sinh ra từ bên trong.
sản vật|Vật được tạo ra hoặc thu hoạch từ thiên nhiên.
sản xuất|Làm ra của cải vật chất từ nguyên liệu bằng sức người.
sang năm|Năm tiếp theo sau năm hiện tại.
sang nhượng|Bán lại tài sản và chuyển tên sở hữu.
sang sảng|Âm thanh vang to, rõ ràng và giòn tan.
sang tên|Đổi tên chủ sở hữu trên giấy tờ để chuyển quyền cho người khác.
sang trọng|Đẹp đẽ, sang sảng và thể hiện sự giàu có, lịch sự.
sàng|Dụng cụ có nhiều lỗ để tách hạt to khỏi hạt nhỏ.
sàng lọc|Lựa chọn kỹ lưỡng để loại bỏ những phần không đạt chuẩn.
sảng khoái|Cảm thấy nhẹ người, dễ chịu và tinh thần phấn chấn.
sáng bóng|Được đánh bóng đến mức bề mặt trơn láng và phản chiếu ánh sáng.
sáng chế|Nghĩ ra và làm ra cái chưa từng có.
sáng chói|Sáng rực rỡ đến mức làm mắt khó chịu.
sáng kiến|Ý tưởng mới giúp việc làm tiến triển tốt hơn.
sáng lập|Người đầu tiên tạo ra hoặc xây dựng nên.
sáng loáng|Tỏa ánh sáng lấp lánh, rực rỡ.
sáng mai|Buổi sáng của ngày hôm sau.
sáng mắt|Có thể nhìn thấy rõ ràng hoặc trở nên thông minh hơn.
sáng ngời|Sáng rực rỡ và tỏa ra vẻ đẹp lộng lẫy.
sáng rực|Ánh sáng chiếu mạnh lan tỏa khắp nơi.
sáng sớm|Thời điểm đầu tiên của buổi sáng.
sáng sủa|Có đủ ánh sáng nên dễ nhìn và tạo cảm giác thoáng.
sáng suốt|Biết rõ sự việc và xử lý đúng đắn.
sáng tác|Tự mình tạo ra tác phẩm văn học hay nghệ thuật.
sáng tạo|Tìm ra và làm nên những điều chưa từng có.
sáng tỏ|Tình trạng sự việc đã rõ ràng, không còn nghi ngờ gì nữa.
sành|Chất gốm nung cứng, thường dùng làm chum vại.
sánh bước|Đi cùng nhau ngang hàng với nhau trong một khoảng cách nhất định.
sánh vai|Đứng ngang hàng nhau về địa vị, tài năng hoặc thành tích.
sao băng|Vệt sáng do vật thể nhỏ từ không gian đi vào khí quyển.
sao chép|Viết lại nội dung giống hệt bản gốc.
sao chổi|Thiên thể bay quanh Mặt trời với đuôi khí sáng dài.
sao la|Thú móng guốc hiếm ở Trường Sơn, có hai sừng dài gần song song.
sao y|Chép hoặc tạo bản có nội dung đúng như bản gốc.
sáp ong|Chất liệu màu vàng nhạt được lấy ra từ tổ ong sau khi đã thu hoạch mật.
sát cánh|Làm việc cùng nhau, chia sẻ khó khăn và hỗ trợ lẫn nhau.
sát hạch|Cho người học làm bài kiểm tra để đánh giá trình độ.
sát nút|Chênh lệch rất ít, ở ngay sát ranh giới nguy hiểm nhất.
sau đây|Những điều sẽ được nói đến ở phần tiếp theo.
sau hết|Cuối cùng, sau cùng.
sau này|Thời điểm sẽ đến sau khi hiện tại kết thúc.
sáu mươi|Số lượng bằng sáu lần mười.
say đắm|Say mê đến mức quên hết mọi thứ.
say mê|Yêu thích sâu sắc đến mức quên hết mọi thứ xung quanh.
say sưa|Thích thú đến mức say mê, quên cả mọi chuyện xung quanh.
sắc bén|Có khả năng phân tích, nhận biết và tác động mạnh mẽ, nhanh chóng.
sắc đẹp|Nét đẹp có thể nhìn thấy ở diện mạo của một người.
sắc sảo|Thông minh, nhanh trí và biết phân tích vấn đề.
sắc thái|Điểm tinh tế giúp phân biệt sự khác nhau giữa các vật.
sặc sỡ|Có nhiều màu sắc rực rỡ, nổi bật và bắt mắt.
săm lốp|Bộ phận cao su giữ hơi và tiếp xúc mặt đường của loại bánh xe có săm.
sắm sửa|Chuẩn bị mua sắm các vật dụng cần thiết cho việc gì.
săn sóc|Chăm sóc, quan tâm và bảo vệ người khác một cách tận tình.
sẵn có|Đã tồn tại sẵn để sử dụng ngay.
sẵn lòng|Tự nguyện và vui vẻ làm điều người khác đề nghị.
sẵn sàng|Đã chuẩn bị đầy đủ để có thể hành động hoặc sử dụng ngay lập tức.
sắn dây|Dây leo có rễ phình thành củ, từ đó có thể lấy bột.
sắp đặt|Sắp xếp đồ đạc hoặc công việc cho có quy củ.
sắp sửa|Ngay lúc này, chuẩn bị bắt đầu làm việc hoặc hành động.
sắp tới|Những việc sẽ xảy ra trong thời gian gần đây.
sắp xếp|Đặt các vật hoặc người theo thứ tự mong muốn.
sầm uất|Đông người qua lại và có nhiều hoạt động buôn bán.
sấm sét|Tiếng nổ và tia phóng điện xuất hiện khi trời có dông.
sân bay|Khu có đường băng và cơ sở phục vụ máy bay đến, đi.
sân bóng|Khoảng sân dành cho tập luyện hoặc thi đấu các môn bóng.
sân bóng đá|Không gian thi đấu dành riêng cho môn thể thao bóng đá.
sân chơi|Khoảng trống hay khu trang bị đồ dùng để vui chơi.
sân ga|Nơi đứng chờ tàu hỏa đến hoặc để hành khách lên xuống.
sân khách|Sân vận động nơi đội đối thủ thi đấu.
sân khấu|Khoảng dành cho người biểu diễn trước khán giả.
sân sau|Khu vực phía sau nhà hoặc nơi phụ thuộc phục vụ cho một thế lực lớn.
sân thượng|Khoảng sân lộ thiên trên tầng trên cùng của nhà.
sân vận động|Khu thể thao lớn có chỗ cho khán giả xem thi đấu.
sần sùi|Bề mặt gồ ghề, có nhiều nốt nhỏ nổi lên.
sâu bọ|Động vật nhỏ, không xương sống, thường có sáu chân và bộ xương ngoài cứng.
sâu đậm|Cảm xúc hoặc ấn tượng rất sâu và rõ.
sâu lắng|Sâu sắc và đọng lại trong tâm hồn.
sâu nặng|Tình cảm sâu sắc, gắn bó chặt chẽ và khó có thể quên.
sâu sắc|Đi sâu vào bản chất, chạm đến những điều cốt lõi của vấn đề.
sâu thẳm|Rất sâu, không thể nhìn thấy đáy hay bên trong.
sâu xa|Sâu sắc, đi vào bản chất và cần suy nghĩ kỹ mới hiểu rõ.
sầu riêng|Quả nhiệt đới vỏ gai to, múi béo và có mùi rất rõ.
sấy tóc|Làm khô tóc bằng luồng gió nóng từ máy điện.
se se|Hơi lạnh, hơi se lạnh khiến da cảm thấy tê tê.
sẽ hay|Chưa thể biết rõ kết quả hay giá trị của việc làm.
sen đá|Cây mọng nước thường có lá dày xếp thành hình hoa thị.
sền sệt|Đặc, sánh và khó chảy.
siêng|Đều đặn bỏ công làm việc, ít khi lười nhác.
siêng năng|Thường xuyên chịu khó làm việc mà không cần ai thúc giục.
siết|Làm dây hay vật ôm quanh trở nên chặt hơn.
siết chặt|Nén chặt lại bằng cách dùng tay nắm hoặc kéo lại.
siêu âm tim|Phương pháp dùng sóng âm tần cao để chụp ảnh và kiểm tra hoạt động của tim.
siêu máy tính|Máy tính điện tử có sức mạnh và tốc độ xử lý dữ liệu vượt trội so với máy thường.
siêu nhiên|Thuộc về thế giới ngoài tự nhiên, không tuân theo quy luật thông thường.
siêu phàm|Vượt hẳn ra ngoài mức bình thường của con người hay sự vật.
siêu thị|Cửa hàng lớn, khách thường tự chọn hàng rồi đến quầy thanh toán.
sinh dưỡng|Sinh con và nuôi dưỡng chúng lớn khôn.
sinh đẻ|Đẻ ra con cái.
sinh đôi|Hai người sinh ra cùng lúc thành một cặp.
sinh động|Có nhiều nét sống động khiến người xem dễ hình dung.
sinh hoạt|Những việc làm thường ngày trong cuộc sống hàng ngày.
sinh học|Khoa học nghiên cứu về sự sống, cấu tạo và hoạt động của sinh vật.
sinh kế|Phương thức kiếm sống để duy trì cuộc đời.
sinh lực|Sức mạnh bên trong giúp cơ thể hoạt động và phát triển.
sinh nhật|Ngày kỷ niệm thời điểm người ta chào đời.
sinh quyển|Lớp vỏ Trái Đất nơi sinh vật sống và tương tác.
sinh ra|Bắt đầu có mặt trên đời hoặc làm phát sinh điều mới.
sinh sự|Tạo ra chuyện phiền phức, rắc rối làm người khác khó chịu.
sinh thái|Cách các loài tương tác với nhau và với điều kiện sống.
sinh thành|Đẻ ra và nuôi dưỡng con cái.
sinh thể|Cơ thể của một sinh vật đang sống, thường chỉ người.
sinh tố|Đồ uống xay nhuyễn trái cây, có thể thêm đá hoặc sữa.
sinh tồn|Sống sót qua khó khăn để duy trì sự sống.
sinh trưởng|Phát triển và lớn lên.
sinh vật|Tên gọi chung cho mọi loài có khả năng sống và lớn lên.
sinh viên|Người đang theo học ở bậc đại học hay cao đẳng.
sình lầy|Bùn nhão, ẩm ướt và khó đi.
so le|Bề mặt không bằng phẳng, có chỗ cao chỗ thấp xen kẽ lẫn nhau.
so sánh|Đặt hai hay nhiều đối tượng cạnh nhau để tìm điểm giống, khác.
so với|Đưa hai sự vật ra để so sánh.
sò huyết|Loài hàu có nước bên trong màu đỏ như máu.
sọ dừa|Vỏ cứng bên trong xơ của quả dừa, có thể làm vật đựng.
soạn|Chuẩn bị và sắp xếp nội dung hoặc đồ dùng trước khi cần.
soạn thảo|Viết ra nội dung chi tiết của một văn kiện.
soát|Xem lại kỹ từng phần để tìm chỗ sai hoặc sót.
soát xét|Kiểm tra kỹ từng phần, xem xét cẩn thận để tìm lỗi.
soi xét|Chú ý tìm hiểu kỹ để phát hiện những điều không rõ ràng.
son phấn|Đồ trang điểm truyền thống gồm son môi và phấn mặt của người phụ nữ.
son sắt|Có lòng trung thành, thủy chung bền vững với người yêu.
son trẻ|Trẻ tuổi, sức khỏe dồi dào và tràn đầy sinh lực.
song ca|Bài hát do hai người cùng hát.
song hành|Hai vật hoặc hai sự việc cùng tiến triển, diễn ra song song.
song phương|Có sự tham gia và thỏa thuận giữa hai bên.
song song|Hai đường thẳng hoặc mặt phẳng nằm cạnh nhau mà không bao giờ gặp nhau.
song thân|Người cha và người mẹ của một người.
song toàn|Cả hai bên trong gia đình hoặc vợ chồng đều còn sống.
sòng phẳng|Làm việc rõ ràng, không thiên vị, công bằng.
sóng âm|Dao động truyền qua một môi trường và có thể tạo ra âm thanh.
sóng gió|Khó khăn, biến cố lớn lao cần phải vượt qua.
sóng sánh|Nước trong vật chứa chao động nhẹ.
sổ cái|Sổ ghi chép tổng hợp các khoản tiền thu chi theo từng loại.
sổ tay|Cuốn sổ nhỏ có thể mang theo để ghi điều cần nhớ.
sổ vàng|Sổ ghi danh những người có công lớn với đất nước.
số chẵn|Số tự nhiên chia cho hai mà không còn số dư.
số chia|Số đứng sau dấu chia và cho biết từng nhóm được chia theo lượng nào.
số chính phương|Số nguyên bằng tích của một số nguyên với chính nó.
số dư|Phần còn lại sau phép chia số nguyên, nhỏ hơn số chia dương.
số đếm|Con số dùng để tính số lượng nhiều ít của các sự vật.
số đo|Chỉ con số ghi lại kết quả khi dùng dụng cụ để xác định kích thước, khối lượng hay các đặc tính khác của vật.
số đông|Phần lớn số lượng người hoặc vật trong một tập thể.
số ghế|Số lượng chỗ ngồi hoặc đại diện.
số hạng|Một thành phần số lượng góp phần tạo nên tổng số.
số học|Ngành toán nghiên cứu về số và các phép tính cơ bản.
số ít|Dạng số lượng chỉ một hoặc dùng cho một người, vật duy nhất.
số không|Con số biểu thị trạng thái không có gì cả hoặc không có giá trị.
số liệu|Tài liệu ghi chép bằng các con số cụ thể.
số lượng|Tổng số đếm được của các sự vật hoặc hiện tượng.
số một|Đứng vị trí cao nhất, quan trọng nhất.
số mục|Danh sách ghi rõ từng mục chi tiết.
số nguyên|Số đếm nguyên vẹn, không có phần thập phân hay phân số.
số nguyên tố|Số tự nhiên lớn hơn một chỉ chia hết cho một và chính nó.
số nhiều|Dùng để chỉ nhiều người hoặc nhiều vật cùng loại.
số thực|Số có thể biểu diễn bằng một điểm trên trục số.
số tự nhiên|Số dùng để đếm; theo quy ước phổ biến gồm cả số không.
sôi động|Trạng thái vui tươi, nhộn nhịp và tràn đầy năng lượng.
sôi nổi|Hoạt động mạnh mẽ, náo nhiệt và đầy nhiệt huyết.
sông|Dòng nước tự nhiên lớn, chảy qua đất liền.
sông đào|Con sông nhân tạo được đào bằng máy móc để dùng cho tàu thuyền hoặc tưới tiêu.
sông nước|Dòng nước lớn chảy giữa đất liền.
sống động|Sôi nổi, rõ ràng và có sức sống mạnh mẽ.
sống thử|Sống chung như vợ chồng chưa kết hôn.
sốt ruột|Cảm thấy nôn nóng, không yên tâm chờ đợi.
sốt sắng|Năng nổ, nhiệt tình làm việc ngay.
sột soạt|Tiếng vật mỏng nhẹ va chạm nhau tạo ra âm thanh xào xạc.
sơ bộ|Làm trước để chuẩn bị, chưa hoàn thiện chi tiết.
sơ cấp|Thuộc về trình độ thấp nhất hoặc nền tảng.
sơ khai|Mới khởi đầu, chưa phát triển rộng rãi.
sơ khảo|Việc chấm điểm hoặc xét duyệt bài thi lần đầu tiên.
sơ lược|Chỉ những nét lớn, bỏ qua chi tiết nhỏ.
sơ mi|Kiểu áo có cổ bẻ, thường cài cúc ở phía trước.
sơ qua|Xem xét hoặc làm việc một cách sơ bộ, chưa kỹ lưỡng.
sơ sài|Chỉ làm qua những nét chính, thiếu phần cần có.
sơ sinh|Trẻ em vừa mới chào đời, chưa được bao nhiêu ngày tuổi.
sơ yếu|Bản ghi tóm tắt những nội dung chính cần thiết.
sờ sờ|Rõ ràng đến mức ai cũng nhìn thấy và không thể chối cãi.
sở hữu|Có quyền nắm giữ và định đoạt một tài sản.
sở hữu trí tuệ|Quyền được pháp luật bảo vệ đối với các thành quả của trí óc.
sở thích|Việc mình yêu thích, thường làm cho vui.
sở thú|Nơi nuôi và chăm nhiều loài động vật để tham quan hoặc bảo tồn.
sở trường|Nơi mà người ta làm việc rất giỏi.
sớm hôm|Buổi sáng và buổi tối, dùng để chỉ mọi lúc trong ngày.
sớm mai|Thời điểm sáng sớm của ngày hôm sau.
sớm muộn|Dù đến trước hay sau thì cuối cùng cũng xảy ra.
sơn ca|Loài chim nhỏ có tiếng hót hay thường được khen ngợi.
sơn dầu|Chất liệu vẽ bằng sơn pha trộn dầu để tạo màu.
sơn dương|Dê núi có sừng ngắn, lông đen hoặc nâu, chạy nhanh.
sơn hà|Núi sông; đất nước.
sơn hải|Lời hứa kiên định, bất biến như núi cao biển sâu.
sơn mài|Chất liệu vẽ tranh trong bóng, làm từ nhựa cây sơn.
sơn môn|Đền thờ hoặc ngôi chùa tọa lạc trên vùng núi cao.
sơn tràng|Nghề làm việc trong rừng bằng tay để khai thác gỗ hoặc vật liệu.
su hào|Rau họ cải có phần thân phình to thành củ trên mặt đất.
su su|Cây leo có quả hình lê sần sùi dùng để nấu ăn.
suất|Phần được chia theo định mức cho một người hoặc một lượt.
súc miệng|Rửa sạch miệng bằng cách ngậm nước rồi súc đi súc lại.
sục sạo|Đi tìm kiếm khắp nơi bằng cách lật giở hoặc dò xét kỹ lưỡng.
sủi bọt|Tạo ra nhiều bong bóng khí nhỏ liên tục.
sủi cảo|Món bánh hấp có vỏ mỏng, nhân gồm thịt tôm nấm và mỡ heo xay nhuyễn.
sum họp|Tụ lại cùng nhau vui vẻ sau khi đã sống xa nhau.
sum vầy|Tập hợp lại cùng nhau trong niềm vui và tình thân.
sung mãn|Đầy đủ sức khỏe, năng lượng và tinh thần.
sung sức|Dồi dào sức khỏe, tràn đầy năng lượng.
sung sướng|Cảm thấy lòng nhẹ nhàng, vui vẻ vì đạt được điều mong muốn.
sung túc|Có điều kiện vật chất đầy đủ và tương đối dư dả.
suối|Dòng nước tự nhiên nhỏ, thường chảy từ vùng cao xuống.
suốt|Liên tục từ đầu đến cuối, không có lúc ngắt quãng.
suốt đời|Trong suốt cả cuộc đời của một người.
sụt giảm|Giảm số lượng hoặc giá trị xuống rất nhanh và mạnh.
suy diễn|Lấy nguyên lý chung để đưa ra kết luận cho từng trường hợp cụ thể.
suy giảm|Trở nên ít đi, yếu đi hoặc kém dần theo thời gian.
suy luận|Kéo ra kết luận dựa trên những dấu hiệu hoặc bằng chứng.
suy nghĩ|Dùng trí óc để phân tích và tìm ra tri thức mới.
suy tính|Nghĩ kỹ để cân nhắc lợi ích và thiệt hại.
suy yếu|Trở nên yếu dần đi theo thời gian hoặc qua tác động bên ngoài.
suýt|Đã gần xảy ra nhưng cuối cùng không xảy ra.
sư phạm|Lĩnh vực đào tạo giáo viên và nghiên cứu cách dạy học.
sư tử|Thú họ mèo lớn thường sống theo đàn; con đực thường có bờm.
sư tử biển|Loài động vật lớn sống dưới nước, có chân màng để bơi.
sử dụng|Dùng vào mục đích hoặc công việc cụ thể nào đó.
sử gia|Người chuyên nghiên cứu và viết về các sự kiện lịch sử.
sử học|Khoa học nghiên cứu về quá khứ.
sử liệu|Tài liệu dùng để nghiên cứu về quá khứ lịch sử.
sử sách|Sách ghi chép về lịch sử và các sự kiện đã qua.
sử thi|Tác phẩm tự sự dài kể chuyện có tầm quan trọng với cộng đồng.
sự cố|Sự việc bất ngờ xảy ra làm hỏng công việc hoặc gây tai nạn.
sự kiện|Việc xảy ra có thể xác định và đáng nhắc tới.
sự nghiệp|Công việc lớn, lâu dài và có lợi cho xã hội.
sự thực|Sự việc đã diễn ra trong thực tế chứ không phải hư cấu.
sự tích|Câu chuyện dân gian kể về thời xa xưa.
sự tình|Tình trạng, diễn biến của một sự việc cụ thể.
sự vật|Những đồ vật hữu hình tồn tại trong thế giới xung quanh con người.
sự việc|Điều đã xảy ra hoặc đang diễn ra có thể kể lại.
sự vụ|Việc công nhỏ nhặt, không phải trọng tâm chính.
sửa đổi|Thay đổi, chỉnh sửa lại để phù hợp hơn với yêu cầu hoặc hoàn cảnh mới.
sửa sai|Làm lại đúng những việc đã làm sai trước đó.
sửa sang|Dọn dẹp, làm cho đẹp và tiện hơn.
sữa chua|Sữa lên men có vị chua dịu và thường sánh đặc.
sữa đặc|Sữa đã bớt nước cho sánh lại, thường có thêm đường.
sữa đậu nành|Thức uống lỏng làm từ đậu nành, vị thanh mát, hơi béo ngậy.
sức bật|Khả năng nhanh chóng phục hồi và vươn lên sau khi gặp khó khăn.
sức bền|Khả năng chịu lực kéo hay bẻ gãy của vật liệu trên một đơn vị diện tích.
sức ép|Lực đè lên vật, hoặc tác động khiến người ta phải ứng phó.
sức kéo|Lực dùng để kéo một vật di chuyển.
sức lực|Khả năng làm việc mạnh mẽ của cơ thể con người.
sức mạnh|Khả năng tạo lực hoặc gây tác động lớn.
sức mua|Khả năng mua sắm hàng hóa của người dân dựa trên thu nhập.
sức nặng|Khả năng tác động mạnh mẽ đến người khác.
sức sống|Khả năng tiếp tục phát triển và giữ vẻ khỏe mạnh, tươi mới.
sức vóc|Sức mạnh cơ thể hiện ra qua dáng người.
sừng|Cấu trúc cứng vươn khỏi đầu trâu, bò và một số loài thú khác.
sừng sững|Đứng cao và nổi hẳn lên, tạo cảm giác vững chãi.
sửng sốt|Cảm thấy bất ngờ mạnh mẽ đến mức không thể giữ bình tĩnh.
sững sờ|Ngạc nhiên đến mức đứng yên không động đậy.
sườn|Phần dốc nằm bên một ngọn đồi hay ngọn núi.
sương sa|Món thạch mát làm từ rong, thường cắt miếng ăn với nước đường.
sương sáo|Món thạch sẫm màu làm từ cây thạch đen, thường dùng ăn ngọt.
sướt mướt|Khóc nhiều, nước mắt tuôn rơi liên tục không ngừng.
sứt mẻ|Bị nứt, vỡ hoặc hư hại khiến không còn nguyên vẹn như ban đầu.
sưu tầm|Tìm kiếm và thu thập nhiều đồ vật thuộc cùng một loại.
sưu tập|Việc gom lại những đồ vật hoặc thông tin đã có sẵn.
sưu thuế|Các khoản tiền nộp cho nhà nước thời xưa.
tả cảnh|Viết lời mô tả quang cảnh bằng văn bản.
tả tình|Viết hoặc nói để thể hiện cảm xúc của người.
tã lót|Quần áo vải mỏng dùng để quấn hoặc mặc cho trẻ nhỏ.
tác dụng|Kết quả sinh ra từ sự tác động, hoặc khả năng gây ra biến đổi ở đối tượng khác.
tác động|Lực lượng hoặc ảnh hưởng làm thay đổi sự vật.
tác giả|Người sáng tạo ra tác phẩm văn học hay nghệ thuật.
tác hại|Điều gây hại đáng kể.
tác hợp|Làm cho hai người kết duyên thành vợ chồng.
tác nghiệp|Thực hiện nhiệm vụ chuyên môn hoặc kỹ thuật.
tác nhân|Yếu tố tạo nên hoặc gây ra một kết quả.
tác phẩm|Kết quả lao động sáng tạo của nghệ sĩ, nhà văn hoặc nhà khoa học.
tác phong|Thói quen làm việc và ứng xử với người.
tác thành|Giúp người thành công, hoàn thành việc.
tác vụ|Công việc cụ thể được thiết lập trong phần mềm để máy thực hiện.
tách|Cốc nhỏ thường có quai, dùng uống trà hay cà phê.
tách bạch|Phân biệt rõ ràng từng phần, không lẫn lộn.
tách rời|Phân chia thành các phần riêng biệt, không còn dính liền.
tai nghe|Thiết bị đặt ở tai để nghe âm thanh riêng.
tài cán|Khả năng giải quyết và thực hiện việc tốt.
tài chính|Việc quản lý tiền bạc của quốc gia hay tập thể.
tài đức|Tài năng và đạo đức tốt đẹp của một người.
tài giỏi|Có năng lực xuất chúng trong nhiều việc.
tài hoa|Giỏi giang, khéo léo trong nghệ thuật hay văn chương.
tài khoản|Số liệu ghi chép để theo dõi tiền bạc và tài sản.
tài liệu|Văn bản, sách báo dùng để tra cứu thông tin.
tài lực|Khả năng thực hiện công việc hoặc nhiệm vụ.
tài mạo|Khả năng và vẻ bề ngoài của người.
tài năng|Khả năng làm việc xuất sắc kèm theo sự sáng tạo và trí tuệ.
tài nguyên|Vật liệu hoặc nguồn lực sẵn có trong tự nhiên dùng để sản xuất.
tài sản|Tiền, vật và những quyền có giá trị thuộc về một chủ thể.
tài tình|Có kỹ năng cao độ và sự khéo léo đáng được khen ngợi.
tài trí|Sự thông minh kết hợp với khả năng giải quyết vấn đề.
tài trợ|Cung cấp tiền bạc để người khác làm được việc.
tài vụ|Công việc thu chi tiền bạc và quản lý vốn của cơ quan.
tải xuống|Lấy dữ liệu hoặc tệp tin từ mạng về máy tính.
tái bản|In lại sách báo dựa trên nội dung của bản cũ.
tái chế|Lấy đồ cũ, hỏng hoặc rác về làm lại thành sản phẩm mới.
tái cử|Được bầu chọn lại giữ chức vụ lần thứ hai.
tái diễn|Xảy ra lại lần nữa vào một thời điểm khác.
tái hiện|Làm cho cảnh hoặc việc đã qua xuất hiện lại bằng hình, lời hay diễn xuất.
tái hợp|Gặp lại nhau và sống chung trở lại sau khi xa cách.
tái lập|Xây dựng lại sau khi đã bị phá hủy hoặc dừng hẳn.
tái ngộ|Gặp lại nhau sau một khoảng thời gian dài không thấy nhau.
tái tạo|Tạo lại phần đã mất, đã dùng hoặc không còn nguyên vẹn.
tái thiết|Xây dựng lại sau khi bị phá hủy.
tại chỗ|Ngay nơi sự việc đang xảy ra hoặc đang được nhắc đến.
tại chức|Đang giữ một chức vụ công việc hoặc vừa làm việc vừa học tập.
tại sao|Hỏi về nguyên nhân, lý do dẫn đến một sự việc xảy ra.
tam cấp|Được phân thành ba bậc hoặc cấp độ.
tam giác|Hình có ba cạnh và ba góc nối nhau.
tam giác cân|Hình có ba cạnh, trong đó hai cạnh thì bằng nhau.
tam giác đều|Tam giác có ba cạnh cùng độ dài.
tam giác vuông|Hình tam giác có một góc bằng chín mươi độ.
tàm tạm|Chỉ ở mức vừa đủ, chưa thực sự tốt.
tám đời|Đã trải qua rất nhiều năm tháng, kéo dài từ thời xa xưa.
tạm biệt|Lời chào khi rời nhau, ngụ ý sẽ có dịp gặp lại.
tạm bợ|Không chắc chắn, dễ hư hỏng hoặc không bền vững.
tạm dịch|Dịch tạm thời vì chưa có từ chính thức trong tiếng Việt.
tạm ngừng|Dừng hoạt động trong một thời gian ngắn.
tạm ổn|Trạng thái ổn định, không có biến động lớn.
tạm quyền|Giữ chức vụ thay thế khi chưa có người được bổ nhiệm chính thức.
tạm thời|Chỉ việc xảy ra trong thời gian ngắn.
tạm trú|Ở tạm trong một khoảng thời gian ngắn.
tạm ứng|Cho trước một phần tiền, sẽ trả lại sau.
tạm vắng|Không có mặt tại nơi quy định trong một khoảng thời gian.
tan hoang|Phá hủy hoàn toàn khiến nơi đó trở nên trống trải, không còn gì.
tan vỡ|Trạng thái bị chia nhỏ, tan rã hoàn toàn.
tàn dư|Những gì còn sót lại sau khi cái chính đã mất.
tản bộ|Đi bộ chậm rãi để ngắm cảnh hoặc thư giãn.
tán dương|Nói lời tốt đẹp để ca ngợi, khen thưởng về phẩm chất hoặc thành tích.
tán gẫu|Nói chuyện phiếm, bàn tán những chuyện không quan trọng.
tán lá|Phần vòm gồm các cành mang lá của cây.
tán thành|Đồng ý cho phép hoặc ủng hộ việc làm của người khác.
tán thưởng|Tỏ ý khen ngợi, đồng tình với điều tốt.
tán tỉnh|Dùng lời nói ngọt ngào để làm người khác dễ dàng nghe theo ý mình.
tán tụng|Khen ngợi và ca tụng một cách thái quá.
tạnh|Mưa ngừng rơi và bầu trời dần ráo.
tao nhã|Thanh cao, lịch sự và có vẻ đẹp trong cách ứng xử.
tào phớ|Thức ăn làm từ đậu nành đông đặc, ăn kèm với nước đường ngọt.
táo tàu|Quả táo nhỏ thường được phơi khô, hay dùng trong món hầm hoặc chè.
táo tây|Quả táo tròn, ruột giòn, của cây táo vùng ôn đới.
tạo dựng|Làm ra, xây dựng nên sự vật hay tình thế.
tạo hình|Nghệ thuật tạo ra các hình khối qua vẽ tranh hay điêu khắc.
tạo lập|Xây dựng nên những điều mới hoặc thiết lập các tổ chức.
tạo mẫu|Thiết kế và làm ra những kiểu dáng mẫu mới.
tạo thành|Gây ra hoặc hình thành nên một sự vật, hiện tượng.
tạp chất|Chất lạ lẫn vào chất chính.
tạp chí|Sách báo chuyên ngành xuất bản định kỳ thành tập.
tạp dề|Tấm vải đeo trước ngực để bảo vệ quần áo khi làm việc.
tạp phẩm|Các mặt hàng nhỏ nhiều loại, phục vụ nhu cầu sinh hoạt hằng ngày.
tạp vụ|Công việc hỗ trợ, dọn dẹp và phục vụ hàng ngày.
tàu bay|Cách gọi máy bay, phương tiện hàng không có thể chở người hay hàng.
tàu bè|Tên gọi chung của tàu, thuyền và phương tiện đi trên nước.
tàu điện|Xe chạy bằng điện trên đường ray chở người trong thành phố.
tàu điện ngầm|Phương tiện giao thông công cộng chạy ngầm dưới lòng đất.
tàu nhanh|Phương tiện vận tải di chuyển với tốc độ rất nhanh.
tàu tốc hành|Xe lửa chạy rất nhanh, chỉ dừng ở những ga lớn.
tàu vũ trụ|Phương tiện chở người và đồ vào không gian.
tay áo|Phần áo bao quanh cánh tay người mặc.
tay đua|Người chuyên tham gia các cuộc thi chạy xe nhanh.
tay lái|Bộ phận dùng để điều khiển hướng đi của xe cộ hoặc phương tiện.
tay nghề|Năng lực và kỹ năng thực hiện công việc chuyên môn của một người.
tay quay|Bộ phận máy dùng để nhận lực và làm quay toàn bộ thiết bị.
tay trái|Cánh tay nằm ở phía bên trái của cơ thể người.
tay trắng|Không có tiền bạc hay của cải gì cả.
tay vịn|Thanh hay bộ phận để bám tay khi đi lại hoặc ngồi xuống.
tắc kè|Thằn lằn có ngón bám chắc, nổi tiếng với tiếng kêu thành nhịp.
tắc nghẽn|Trạng thái bị chặn lại, không thể di chuyển hoặc lưu thông.
tắc trách|Làm việc qua loa, chỉ chú trọng hoàn thành hình thức.
tắc xi|Xe ô tô nhỏ chuyên chở khách trả tiền.
tăm tích|Tin tức hoặc dấu vết còn lại của một sự vật, sự việc.
tắm giặt|Rửa người và giặt quần áo cho sạch.
tắm nắng|Phơi da dưới ánh nắng để khỏe mạnh.
tắm rửa|Rửa người, lau chùi cơ thể cho sạch sẽ.
tăng cường|Thực hiện hành động làm cho sức mạnh hoặc số lượng tăng lên.
tăng gia|Nỗ lực làm thêm việc để tăng sản lượng.
tăng tiến|Tăng lên và phát triển dần theo thời gian.
tăng tốc|Tăng nhanh độ nhanh của phương tiện hoặc chuyển động.
tăng trưởng|Trở nên to hơn, nhiều hơn hoặc phát triển mạnh mẽ hơn.
tặng phẩm|Vật phẩm được trao tặng để thể hiện lòng biết ơn hoặc tình cảm.
tặng thưởng|Cho tiền hoặc phần thưởng để khen ngợi công lao, thành tích.
tâm bão|Vùng giữa cơn bão có gió lặng, trời quang và áp suất thấp nhất.
tâm can|Nơi chứa đựng những suy nghĩ, cảm xúc sâu kín nhất của con người.
tâm đắc|Hiểu rõ ý nghĩa nên đã tiếp thu vào lòng.
tâm điểm|Vị trí quan trọng nhất, nơi mọi sự chú ý tập trung.
tâm hồn|Thế giới nội tâm chứa đựng suy nghĩ và cảm xúc của con người.
tâm khảm|Chỗ sâu kín nhất trong lòng người.
tâm lực|Sức mạnh nội tâm và ý chí của con người.
tâm nguyện|Ước muốn sâu kín trong lòng, là điều mong muốn chân thành nhất.
tâm phục|Tin tưởng và phục tùng một cách chân thành.
tâm phục khẩu phục|Tin phục lòng, không chỉ nói ra ngoài miệng.
tâm sự|Những suy nghĩ và cảm xúc riêng tư mà ít người biết đến.
tâm thành|Lòng chân thành, không giả dối, hết lòng với việc làm.
tâm tình|Cảm xúc riêng tư, kín đáo trong lòng mỗi người.
tâm trạng|Trạng thái cảm xúc và tâm lý của con người.
tâm trí|Lòng dạ và đầu óc, nơi chứa đựng tình cảm cùng suy nghĩ.
tâm tư|Những suy nghĩ, cảm xúc nằm sâu trong lòng người.
tầm gửi|Loài cây ký sinh bám vào thân cây khác để lấy chất dinh dưỡng.
tầm nhìn|Khoảng không gian mà mắt người có thể nhìn thấy được.
tầm thường|Thường thấy, không có gì đặc biệt hay nổi bật.
tầm vóc|Hình dáng cơ thể của người hoặc quy mô, tầm cỡ của sự vật.
tấm bé|Thời kỳ tuổi nhỏ, giai đoạn còn nhỏ bé.
tấm lòng|Những tình cảm chân thành, sâu sắc nhất trong lòng người.
tân cử|Đã được bầu chọn nhưng chưa nhận chức vụ.
tân gia|Lễ mừng khi chuyển vào nhà ở mới.
tân học|Học kiến thức hiện đại, khác với học Nho giáo xưa.
tân hôn|Đôi vợ chồng vừa mới kết hôn.
tân lang|Người vừa kết hôn (cũ).
tân ngữ|Đối tượng nhận tác động của động từ trong câu.
tân sinh viên|Học sinh đã được trường đại học chấp nhận và cho phép nhập học.
tân tạo|Làm ra mới, chưa từng tồn tại trước đó.
tân thời|Đi theo phong cách, xu hướng mới nhất của thời đại.
tân tiến|Phát triển theo hướng mới, tiến bộ hơn so với trước đây.
tân trang|Sửa chữa, trang trí lại cho đồ vật trông mới.
tân xuân|Thời điểm đầu năm mới, đầu mùa xuân.
tần số|Số lần lặp lại của một chuyển động trong một giây.
tần suất|Số lần một việc lặp lại trong khoảng quan sát.
tận dụng|Sử dụng hết mọi tiềm năng có sẵn để đạt kết quả tốt nhất.
tận hưởng|Sống trọn vẹn để cảm nhận niềm vui.
tận lực|Dùng hết sức lực, cố gắng hết khả năng của mình.
tận tay|Nhận trực tiếp bằng tay, không qua người khác.
tận tâm|Làm việc bằng hết cả tấm lòng và sự tận tụy.
tận thu|Thu hết toàn bộ số tiền hoặc tài sản có thể thu được.
tầng|Một lớp hay một mức riêng trong vật xếp theo chiều cao.
tầng hầm|Phần nhà xây dưới đất để chứa đồ.
tấp nập|Nơi có đông người qua lại, hoạt động liên tục không ngừng nghỉ.
tập dượt|Luyện tập nhiều lần để làm thành thạo.
tập đoàn|Nhóm công ty có liên kết chặt chẽ về vốn hoặc quản lý.
tập hợp|Gom những phần rời vào cùng một nhóm hoặc một chỗ.
tập huấn|Tập hợp để hướng dẫn và luyện tập kỹ năng.
tập kết|Tập trung người từ nhiều nơi đến một chỗ để cùng làm việc.
tập lệnh|Dãy các chỉ thị để máy tính thực hiện theo trình tự.
tập luyện|Làm việc nhiều lần để nâng cao kỹ năng hoặc sức khỏe.
tập quán|Thói quen được hình thành lâu dài và được nhiều người cùng làm theo.
tập sự|Làm việc với vai trò học nghề để quen thuộc trước khi chính thức.
tập tành|Luyện tập nhiều lần để làm việc gì đó thành thạo.
tập thể|Tập hợp gồm nhiều người cùng chung mục đích hoặc hoạt động với nhau.
tập tin|Tập hợp các dữ liệu điện tử có tên riêng, được lưu trữ trong máy tính.
tập tính|Cách ứng xử lặp lại đặc trưng cho một loài sinh vật.
tập trung|Dồn hết sức lực vào một việc cụ thể.
tập tục|Phong tục, tập quán chung của cộng đồng.
tất bật|Vội vã, bận rộn, làm việc nhiều và không có thời gian nghỉ ngơi.
tất cả|Chỉ toàn bộ mọi sự vật, con người mà không bỏ sót ai, không trừ gì.
tất nhiên|Đúng theo lẽ thường, không có gì phải ngạc nhiên.
tất niên|Lúc kết thúc năm, thường tổ chức ăn mừng.
tất tả|Vội vã, chạy nhanh vì bận rộn.
tất tần tật|Mọi thứ, tất cả các phần không bỏ sót.
tất yếu|Việc chắc chắn phải xảy ra, không thể tránh khỏi hay thay đổi.
tẩu tán|Chạy đi giấu đồ để tránh bị phát hiện.
tây học|Kiến thức, học thuật đến từ phương Tây.
tây nam|Hướng nằm giữa phía tây và phía nam trên la bàn.
tẩy rửa|Làm sạch vật thể bằng hóa chất và nước để loại bỏ bẩn.
tẻ nhạt|Không thú vị, gây cảm giác chán nản và nhàm chán.
té ra|Hóa ra là sự thật như thế.
tê giác|Thú lớn da dày có một hoặc hai sừng ở phía trên mõm.
tê tê|Thú có vảy cứng, ăn kiến và thường cuộn người khi tự vệ.
tề tựu|Tập hợp đông người từ nhiều nơi khác nhau đến cùng một chỗ.
tế bào|Đơn vị nhỏ nhất cấu tạo nên cơ thể sống.
tế nhị|Khéo léo, tinh tế và nhã nhặn trong cách ứng xử.
tên gọi|Cách gọi tên người hoặc vật như tên thật.
tên miền|Tên bằng chữ dùng để tìm đến một địa chỉ trên Internet.
tên tuổi|Danh tiếng và uy tín được xã hội công nhận.
tên tự|Tên gọi khác của người để thể hiện ý nghĩa hoặc mong muốn.
tết nhất|Ngày Tết nói chung trong dịp đầu năm.
tha hồ|Làm việc gì cũng được thoải mái không bị ngăn cản.
thả bộ|Đi bộ chậm rãi, không có mục đích cụ thể.
thả lỏng|Để cơ thể thư giãn, không dùng chút sức nào.
thả rông|Cho vật nuôi tự do đi lại mà không có người dắt.
thác|Đoạn nước sông hoặc suối đổ mạnh từ cao xuống thấp.
thách thức|Đưa ra lời mời làm việc khó để xem ai dám thực hiện.
thạch|Món ăn mềm, đông thành khối và thường để nguội.
thạch anh|Khoáng vật thường tạo tinh thể, có thể trong hoặc mang nhiều màu.
thạch cao|Khoáng vật chứa canxi sunfat, thường dùng làm vật liệu đúc và xây dựng.
thải loại|Loại bỏ những người hoặc vật không còn cần thiết.
thái độ|Phản ứng thể hiện suy nghĩ và cảm xúc qua hành vi, lời nói hoặc nét mặt.
thái quá|Vượt quá mức cần thiết, quá đáng hoặc đi quá giới hạn bình thường.
tham chiếu|Căn cứ dùng để đối chiếu và tham khảo.
tham dự|Tham gia vào hoạt động chung để chia sẻ trách nhiệm và công việc.
tham gia|Góp sức mình vào hoạt động chung của tập thể.
tham khảo|Tìm thêm thông tin từ nguồn khác trước khi đưa ra quyết định.
tham luận|Phần trình bày ý kiến tại hội nghị.
tham vấn|Tham gia tư vấn để cùng bàn bạc, góp ý hoặc hỗ trợ.
thảm|Tấm dệt dày thường trải trên sàn nhà.
thám hiểm|Đi vào vùng đất xa lạ để tìm hiểu và khảo sát.
than|Nhiên liệu rắn màu đen dùng cho bếp hay lò.
than đá|Loại than đen cứng như đá, thường được khai thác từ lòng đất.
than phiền|Nói lời than thở về chuyện không vừa lòng.
than thở|Nói lên những điều buồn bã, khổ đau để chia sẻ hoặc than vãn.
than tổ ong|Than được nung thành khối tròn có nhiều lỗ nhỏ dùng đốt lửa.
thán phục|Khen ngợi và cảm thấy nể phục trước một điều gì đó.
thang cuốn|Thang máy dạng cầu thang có băng chuyền chạy liên tục.
thang máy|Thiết bị vận chuyển người và hàng hóa lên xuống giữa các tầng.
thanh|Một đoạn vật liệu dài và nhỏ, như miếng gỗ để làm nan.
thanh cảnh|Không to lớn, không cầu kỳ hay thô bạo.
thanh cao|Lòng trong sạch, phẩm chất cao quý.
thanh đạm|Ăn uống đơn giản, không dùng nhiều món cầu kỳ hay đắt tiền.
thanh điệu|Sự lên xuống của giọng giúp phân biệt nghĩa giữa các tiếng.
thanh lịch|Trang trọng, nhã nhặn và có văn hóa trong cách ăn mặc, hành xử.
thanh lọc|Lấy đi những phần không tốt để làm cho sạch sẽ.
thanh long|Quả của cây họ xương rồng, thịt có nhiều hạt đen li ti.
thanh mảnh|Mảnh mai, gầy guộc nhưng có vẻ yếu ớt và dễ thương.
thanh nhã|Vẻ đẹp thanh lịch, trang trọng và mực thước.
thanh quản|Phần cổ họng dùng để tạo ra âm thanh khi nói.
thanh tao|Có vẻ ngoài và hành động thanh lịch, sang trọng, tao nhã.
thanh tân|Nhanh nhẹn, thanh lịch trong cử chỉ và hành động.
thanh thải|Việc dọn dẹp sạch sẽ, loại bỏ những thứ không cần thiết.
thanh thản|Trạng thái tâm hồn nhẹ nhàng, không lo âu hay phiền muộn.
thanh thoát|Linh hoạt, nhẹ nhàng, không bị gò bó hay cứng nhắc.
thanh tịnh|Yên tĩnh, không có tiếng động hay xao động.
thanh toán|Trả khoản tiền cần trả khi mua hàng hoặc dùng dịch vụ.
thanh tra|Người được cử đến để xem xét, kiểm tra việc làm tại các cơ quan hoặc đơn vị.
thanh trung|Có phẩm chất trong sạch và thẳng thắn.
thanh vắng|Không có tiếng động, không thấy bóng người qua lại.
thành bại|Kết quả tốt và kết quả xấu của một việc.
thành công|Đạt được kết quả tốt như mong muốn hoặc dự định.
thành danh|Làm nên tiếng tăm, được nhiều người biết đến.
thành đạt|Đạt được kết quả mong muốn trong sự nghiệp và danh tiếng.
thành gia|Nói về con trai con gái đã kết hôn và thành lập nhà cửa.
thành hôn|Làm lễ cưới để chính thức kết hôn.
thành khẩn|Thật lòng một cách chân thành và hết sức.
thành kiến|Ý kiến định sẵn về người hay việc, thường xuất phát từ cảm tính hoặc hiểu lầm.
thành lập|Chính thức tạo dựng và cho một tổ chức bắt đầu hoạt động.
thành ngữ|Cụm từ cố định mang nghĩa bóng, thường dùng để diễn tả ý trọn vẹn.
thành nhân|Người đã đến tuổi trưởng thành, tự lập.
thành niên|Đã đạt đến độ tuổi được pháp luật coi là người trưởng thành.
thành phẩm|Sản phẩm đã hoàn thành tất cả các công đoạn chế biến.
thành phần|Mỗi yếu tố góp vào cấu tạo của một vật hoặc tập thể.
thành phố|Đô thị có dân cư tập trung cùng nhiều hoạt động và dịch vụ.
thành quả|Kết quả tốt đẹp thu được sau khi cố gắng.
thành sự|Đã hoàn thành xong việc.
thành tài|Trở thành người có tài năng và thành công.
thành tâm|Chân thành, xuất phát từ tận đáy lòng.
thành thạo|Làm việc trôi chảy và ít sai nhờ đã có nhiều kinh nghiệm.
thành thật|Trung thực, không nói dối và luôn bộc lộ sự thật trong mọi việc.
thành thị|Khu dân cư đô thị, phân biệt với vùng nông thôn.
thành thực|Trung thực, nói đúng suy nghĩ thật lòng.
thành tích|Kết quả tốt đẹp đạt được sau khi cố gắng.
thành tố|Phần nhỏ trực tiếp cấu tạo nên một tổng thể lớn.
thành tựu|Kết quả tốt đẹp sau khi hoàn thành việc khó.
thành viên|Người hoặc đơn vị đóng vai trò là một phần trong tổ chức hay tập thể.
thành ý|Tâm tư chân thật, xuất phát từ lòng tốt và mong muốn điều thiện.
thảnh thơi|Thư thái, không còn bận tâm hay lo lắng gì.
thao luyện|Tập luyện thường xuyên để nâng cao kỹ năng và sức khỏe.
thao tác|Sự vận động của tay chân để thực hiện công việc.
thảo luận|Cùng trao đổi góc nhìn để hiểu vấn đề hoặc tìm cách giải quyết.
thảo mộc|Cây cối và thực vật nói chung.
thảo nguyên|Cánh đồng cỏ rộng lớn trải dài.
thảo quả|Gia vị thơm lấy từ quả một loài cây cùng họ với gừng.
tháo|Gỡ một vật khỏi chỗ gắn hoặc tách rời các bộ phận.
tháo dỡ|Tháo rời từng bộ phận để lấy ra hoặc bỏ đi hoàn toàn.
tháo vát|Biết cách giải quyết nhanh chóng và tốt những việc khó khăn.
tháp chuông|Tòa cao có chuông treo bên trong để phát âm thanh.
thau|Đồ đựng miệng rộng, thường dùng hứng nước để rửa.
thay đổi|Làm cho khác trước, hoặc tự trở nên khác trước.
thay mặt|Đại diện cho người khác hoặc một tổ chức.
thay vì|Thay thế một vật, việc này bằng một vật, việc khác.
thắc mắc|Có điều chưa rõ, cần người khác giải thích.
thăm dò|Tìm những thông tin ban đầu trước khi quyết định bước tiếp.
thăm hỏi|Liên lạc hoặc tới gặp để biết tình hình và bày tỏ quan tâm.
thăm viếng|Đến nhà người khác để hỏi han, thăm hỏi tình hình.
thắm thiết|Tình cảm giữa hai người rất sâu đậm, gắn bó khăng khít.
thằn lằn|Bò sát có vảy, thường có bốn chân và đuôi dài.
thăng bằng|Trạng thái giữ vững không bị nghiêng ngả hay đổ xuống.
thăng hoa|Chuyển trực tiếp từ thể rắn thành hơi mà không thành lỏng.
thăng tiến|Được nâng lên chức vụ cao hơn trong công việc hoặc học tập.
thăng trầm|Thường xuyên thay đổi giữa lúc tốt và lúc xấu.
thẳng đứng|Thẳng theo chiều từ dưới lên trên, vuông góc với mặt đất.
thẳng góc|Hai đường thẳng cắt nhau tạo thành góc vuông.
thẳng tắp|Vật dài nằm thẳng, không cong vẹo chút nào.
thẳng thắn|Nói thẳng, không cong vẹo hay lệch hướng.
thắng bại|Kết quả của việc giành chiến thắng hoặc chịu thất bại.
thắng cảnh|Nơi nổi tiếng nhờ phong cảnh đẹp.
thắng lợi|Chiếm được vị trí cao hơn hoặc đạt được kết quả mong muốn.
thắng thế|Đạt được vị trí vượt trội hơn đối thủ.
thặng dư|Phần còn thừa ra sau khi đã đáp ứng đủ nhu cầu cần thiết.
thắp|Làm cho đèn, nến hay que hương bắt đầu cháy sáng.
thắt|Buộc hay làm dây ôm chặt vào một chỗ.
thắt lưng|Dải đeo quanh eo để giữ quần hoặc trang trí.
thâm hụt|Trạng thái thiếu hụt tiền bạc do chi tiêu vượt quá thu nhập.
thâm nhập|Đi sâu vào bên trong hoặc hòa nhập để hiểu rõ.
thâm niên|Thời gian làm việc lâu năm trong một ngành nghề hoặc tổ chức.
thâm tâm|Nơi chứa đựng những suy nghĩ sâu kín nhất mà người ta không nói ra.
thâm tình|Tình cảm gắn bó, sâu nặng giữa những người thân thiết.
thâm trầm|Nét tính sâu sắc, ít nói và giữ kín những suy nghĩ bên trong.
thầm kín|Giấu kín, không cho người khác biết.
thầm lặng|Không nói ra, giữ im lặng và không để người khác hay biết.
thẩm tra|Kiểm tra kỹ lưỡng để xác nhận tính chính xác của thông tin.
thấm nhuần|Hiểu sâu sắc và thấm đẫm vào tâm trí.
thấm thía|Hiểu sâu sắc và cảm nhận rõ ràng một điều gì đó.
thậm chí|Đến mức mà điều đó xảy ra hoặc được nhấn mạnh thêm.
thân ái|Cư xử ấm áp, coi người khác như bạn bè.
thân cận|Gần gũi và có tình cảm thân thiết với nhau.
thân cây|Trục chính nối rễ với các cành, giúp nâng đỡ cây.
thân hành|Trực tiếp đứng ra làm việc, không ủy quyền cho người khác.
thân hình|Dáng vẻ tổng thể của cơ thể khi nhìn từ bên ngoài.
thân hữu|Bạn bè thân thiết hoặc người thân trong gia đình.
thân mật|Có cách cư xử gần gũi, ít giữ khoảng cách xã giao.
thân mẫu|Người mẹ sinh ra mình, dùng để gọi một cách tôn kính.
thân mềm|Nhóm động vật không có xương sống, thân thể mềm mại và thường có vỏ cứng bảo vệ.
thân mến|Người mà ta quý trọng và cảm thấy gần gũi.
thân mình|Cơ thể người.
thân phụ|Người cha (dùng để gọi hoặc nói về cha).
thân quen|Quen biết rõ và có tình cảm thân thiết với nhau.
thân thể|Phần vật chất cấu tạo nên người hoặc động vật, bao gồm da thịt và xương.
thân thiện|Dễ gần và sẵn lòng đối xử tốt với người khác.
thân thiết|Gần gũi, thân mật và có tình cảm sâu sắc.
thân thuộc|Rất quen và gần gũi vì đã gắn bó từ lâu.
thân thương|Gây ra tình cảm yêu quý, trìu mến sâu sắc trong lòng người.
thân tín|Người thân quen, gần gũi và đáng tin cậy tuyệt đối.
thân tình|Chân thật và gần gũi như giữa những người quen lâu.
thần diệu|Kỳ lạ, phi thường, làm việc khó thành công dễ dàng.
thần đồng|Trẻ em có trí tuệ vượt trội so với mọi người cùng tuổi.
thần sắc|Vẻ mặt biểu lộ trạng thái tâm lý hoặc tinh thần bên trong.
thần thái|Nét biểu cảm và phong cách riêng toát lên qua dáng vẻ, cử chỉ.
thận trọng|Luôn cẩn thận, suy tính kỹ lưỡng trước khi làm để tránh sai lầm.
thấp thoáng|Hiện ra rồi ẩn đi, khó thấy rõ ràng.
thập cẩm|Gồm nhiều thứ khác nhau trộn lẫn vào nhau.
thập toàn|Hoàn hảo, đầy đủ mọi điều tốt đẹp.
thất bại|Không đạt được điều dự định dù đã cố gắng.
thất cơ|Làm hỏng hoặc phá vỡ kế hoạch đã định.
thất lạc|Bị lẫn hoặc mất dấu nên hiện chưa tìm thấy.
thất ngôn|Thể thơ mỗi câu gồm bảy tiếng.
thất thường|Không đều, lúc này lúc khác, không có quy luật.
thất vọng|Không còn tin vào điều mình mong đợi sẽ xảy ra.
thật ra|Thực chất sự việc, trái ngược với điều vừa nói hoặc nghĩ.
thật sự|Có thực, không phải là hư cấu hay giả dối.
thật thà|Tự nhiên bộc lộ bản thân, không giả dối.
thấu đáo|Làm việc kỹ lưỡng, hiểu rõ mọi chi tiết.
thấu hiểu|Hiểu rõ sâu sắc mọi chi tiết và bản chất của vấn đề.
thấu suốt|Hiểu rõ toàn bộ vấn đề từ đầu đến cuối một cách sâu sắc và mạch lạc.
thầy|Người dạy học, truyền đạt kiến thức hay tay nghề.
thầy giáo|Nam giới đảm nhiệm việc dạy học.
thẻ nhớ|Thiết bị nhỏ dùng để lưu trữ và chuyển dữ liệu cho máy tính.
thèm khát|Muốn có điều gì đó đến mức nóng lòng, thúc giục mạnh mẽ vì cảm thấy thiếu hụt.
thèm thuồng|Thèm đến mức biểu lộ rõ ràng qua hành động, ánh mắt.
then|Thanh ngang gài ở cửa để giữ cho cửa đóng.
then chốt|Yếu tố quan trọng nhất quyết định kết quả.
thẹn thùng|Cảm thấy xấu hổ, ngại ngùng khiến mặt đỏ hoặc cúi đầu.
theo|Đi cùng hướng phía sau hoặc làm như người khác đã chỉ.
theo đuổi|Kiên trì nỗ lực để đạt được mục tiêu hoặc hoàn thành công việc.
theo gương|Học tập và làm theo cách làm của người khác.
thép|Hợp kim chủ yếu từ sắt và cacbon, cứng và chịu lực.
thề nguyền|Nói lời hứa chắc chắn với nhau.
thể chất|Cấu tạo và sức khỏe của cơ thể con người.
thể diện|Hình ảnh, danh tiếng giúp con người được xã hội trọng vọng.
thể dục|Tập các động tác có bài bản để rèn luyện và giữ gìn sức khỏe.
thể dục dụng cụ|Môn thể thao tập luyện các động tác trên các dụng cụ chuyên dụng.
thể hình|Dáng và tỷ lệ của cơ thể khi nhìn tổng thể.
thể lệ|Những quy tắc chung quy định cách thức thực hiện việc làm.
thể lực|Sức khỏe và khả năng vận động của cơ thể.
thể nghiệm|Dùng trải nghiệm thực tế để kiểm tra xem điều gì đúng hay sai.
thể thao|Hoạt động rèn luyện sức khỏe, sức bền theo quy tắc.
thể theo|Làm như nguyện vọng, yêu cầu hay đề nghị người khác đã nêu.
thể thống|Quy tắc, nề nếp phải tuân theo để giữ trật tự.
thể tích|Số lượng không gian ba chiều mà một vật chiếm giữ.
thể trạng|Tình trạng sức khỏe tổng quát của cơ thể.
thể xác|Phần thịt xương, da lông của người.
thế chấp|Đưa tài sản ra làm bảo đảm cho khoản tiền vay.
thế gian|Cõi đời trần tục nơi con người sinh sống và hoạt động hàng ngày.
thế giới|Toàn thể Trái Đất cùng con người và sự sống trên đó.
thế hệ|Nhóm người cùng sinh ra trong một khoảng thời gian.
thế mà|Từ nối dùng để chuyển ý, chỉ sự trái ngược hoặc bất ngờ so với điều vừa nói.
thế năng|Năng lượng tiềm ẩn do vị trí hoặc trạng thái của vật.
thế nhân|Con người đang sống trong đời thường, ngoài xã hội.
thế thái|Thói quen, cách sống và lối ứng xử của con người trong xã hội.
thế thường|Những thói quen, cách sống phổ biến mà mọi người thường gặp.
thế tục|Những phong tục, thói quen thông thường của đời sống.
thềm|Phần nền cao ngay trước lối vào nhà.
thềm lục địa|Phần đáy biển nông nối tiếp đất liền trước khi dốc xuống sâu.
thênh thang|Rộng lớn, thoáng đãng đến mức dư thừa.
thêu|Dùng chỉ màu và kim tạo họa tiết trên vải.
thêu thùa|Làm hoa văn trên vải bằng những đường kim và chỉ màu.
thi công|Thực hiện xây dựng công trình theo bản vẽ đã thiết kế.
thi cử|Những kỳ kiểm tra có tổ chức để đánh giá hoặc tuyển chọn người học.
thi đấu|Tham gia tranh tài để xem ai giỏi hơn về sức hoặc trí.
thi đỗ|Vượt qua kỳ thi, đạt kết quả như mong đợi.
thi phẩm|Bài thơ hoặc tác phẩm văn học có giá trị nghệ thuật và nội dung sâu sắc.
thi thoảng|Có xảy ra một vài lần, nhưng cách nhau và không đều.
thi thố|Dùng hết tài năng và sức lực để thể hiện khả năng của mình.
thi tuyển|Thi để chọn người đủ điều kiện làm việc.
thi vị|Cái mang vẻ đẹp, sự gợi cảm đặc trưng của thơ ca.
thì giờ|Thời gian được xem là có ích và đáng quý.
thì thào|Nói rất khẽ, âm thanh nhỏ không rõ ràng, lẫn vào hơi thở.
thì thầm|Nói nhỏ tiếng để người khác không nghe thấy.
thí dụ|Dùng sự việc cụ thể để làm sáng tỏ ý nghĩa của một khái niệm.
thí điểm|Thử ở phạm vi nhỏ để rút kinh nghiệm trước khi mở rộng.
thí nghiệm|Thử trong điều kiện xác định để quan sát hoặc kiểm tra giả thuyết.
thí sinh|Người tham dự kỳ thi để kiểm tra kiến thức đã học.
thị giác|Khả năng nhìn thấy và phân biệt hình ảnh bằng mắt.
thị hiếu|Thói quen thích những thứ vật chất hoặc văn hóa của nhiều người trong một thời gian ngắn.
thị lực|Khả năng nhìn thấy rõ vật ở xa.
thị tộc|Nhóm người lớn cùng tổ tiên sống chung và làm ăn cùng nhau.
thị trấn|Khu vực đông dân cư, nơi buôn bán và thủ công nghiệp phát triển.
thị trường|Nơi diễn ra hoạt động mua bán và trao đổi hàng hóa.
thị tứ|Khu dân cư nhỏ hình thành tự phát quanh nhà máy.
thị xã|Đô thị từng là đơn vị hành chính dưới tỉnh ở Việt Nam.
thìa|Đồ có cán và lòng lõm để múc thức ăn.
thìa là|Loài rau thơm có lá nhỏ, dùng để ăn hoặc nấu canh.
thích|Cảm thấy vui hoặc hứng thú trước người, vật hay việc gì.
thích đáng|Phù hợp và thỏa đáng với yêu cầu cần thiết.
thích hợp|Phù hợp với yêu cầu hoặc hoàn cảnh cần thiết.
thích nghi|Thay đổi bản thân để phù hợp với hoàn cảnh mới.
thích nghĩa|Việc phân tích và làm rõ ý nghĩa của một từ, câu hay văn bản.
thích thời|Hợp với hoàn cảnh và xu hướng của thời đại.
thích thú|Thấy vui và có hứng với điều mình đang làm hoặc quan sát.
thích ứng|Thay đổi để phù hợp với hoàn cảnh hoặc yêu cầu mới.
thích ý|Tâm trạng hài lòng, vừa ý.
thiếc|Kim loại trắng bạc, mềm, thường dùng trong hợp kim hàn.
thiên di|Di chuyển đến nơi ở khác.
thiên đỉnh|Điểm cao nhất trên bầu trời theo hướng nhìn thẳng lên.
thiên hạ|Tất cả mọi người và mọi nơi trên thế gian.
thiên hướng|Khuynh hướng thiên về một phía hoặc một cách nhìn nhất định.
thiên lệch|Có quan điểm hoặc cách xử sự không công bằng mà thiên về một phía.
thiên nga|Chim nước lớn cổ dài, có màng bơi giữa các ngón chân.
thiên nhiên|Tất cả các hiện tượng, cây cối, con vật tồn tại ngoài con người.
thiên phú|Khả năng vốn có từ khi sinh ra.
thiên tài|Người có tài năng vượt trội bẩm sinh.
thiên thể|Tên gọi chung cho các vật thể tồn tại trong không gian vũ trụ.
thiên thời|Thời tiết thuận lợi hoặc hoàn cảnh phù hợp để làm việc.
thiên tính|Tính chất vốn có, được trời phú cho con người từ khi sinh ra.
thiên văn|Nghiên cứu các hiện tượng tự nhiên trên bầu trời.
thiên văn học|Ngành nghiên cứu các thiên thể và những hiện tượng trong vũ trụ.
thiên vị|Yêu thích hoặc đối xử khác biệt với một bên một cách không công bằng.
thiển ý|Ý kiến ít sâu sắc, dùng để tự khiêm tốn khi nói về mình.
thiện cảm|Cảm giác tốt đẹp, dễ chịu khi tiếp xúc hoặc nhìn nhận về một người nào đó.
thiện chí|Ý định tốt đẹp khi thực hiện một việc gì đó.
thiện nghệ|Giỏi nghề, thành thạo kỹ năng.
thiện nguyện|Làm việc giúp đỡ người khác vì lòng tốt mà không lấy tiền.
thiện tâm|Lòng tốt, lòng nhân ái muốn giúp đỡ người khác.
thiệp|Tấm giấy đẹp để gửi lời chúc, lời mời hay lời cảm ơn.
thiết bị|Dụng cụ, máy móc dùng trong sản xuất hay xây dựng.
thiết kế|Lập kế hoạch chi tiết để xây dựng.
thiết lập|Dựng nên một tổ chức, quy trình hoặc hệ thống mới.
thiết thân|Rất quan trọng hoặc liên quan trực tiếp đến mình.
thiết thực|Phù hợp với nhu cầu và hoàn cảnh thực tế.
thiết yếu|Quan trọng nhất, không thể thiếu được trong mọi hoàn cảnh.
thiểu số|Số lượng ít hơn so với phần lớn còn lại.
thiếu|Không có đủ số lượng hoặc phần cần thiết.
thiếu hụt|Số lượng hoặc chất lượng không đạt đủ yêu cầu cần thiết.
thiếu nhi|Nhóm trẻ em từ thiếu niên đến nhi đồng.
thiếu niên|Người còn nhỏ, chưa đến tuổi trưởng thành, khoảng từ mười đến mười sáu tuổi.
thiếu phụ|Người vợ trẻ của một người đàn ông.
thiếu sót|Phần còn thiếu hoặc làm chưa đúng.
thiếu suy nghĩ|Làm việc hoặc quyết định nhanh, không suy xét kỹ.
thiếu thốn|Không đủ số lượng cần thiết cho việc sinh hoạt.
thiếu thời|Thời kỳ khi con người còn ở độ tuổi trẻ.
thím|Cách gọi vợ của em trai người cha.
thinh không|Không gian trống rỗng, hoàn toàn vắng vẻ không có tiếng động.
thình lình|Xảy ra đột ngột mà không có dấu hiệu báo trước nào.
thỉnh giảng|Mời chuyên gia từ nơi khác đến giảng dạy tạm thời.
thính|Có khả năng nghe hoặc nhận biết mùi rất tốt.
thính giả|Người nghe một chương trình phát thanh hay buổi diễn bằng âm thanh.
thính giác|Khả năng cảm nhận âm thanh bằng tai.
thịnh hành|Phổ biến rộng rãi và được ưa chuộng.
thịnh soạn|Nhiều món ăn ngon, được chuẩn bị kỹ lưỡng và trang trọng.
thịt|Phần mềm của cơ thể động vật, thường dùng làm thức ăn.
thịt lợn|Phần thịt lấy từ con lợn, thường dùng chế biến thức ăn.
thiu|Bắt đầu có mùi chua hoặc khó chịu vì để lâu.
thoa|Dùng tay trải một lớp kem hay dầu lên da.
thoải mái|Cảm thấy dễ chịu, không căng thẳng.
thoái thác|Tìm lý do để từ chối làm việc hoặc không đáp ứng yêu cầu của người khác.
thoái trào|Giai đoạn phong trào suy yếu, giảm sút.
thoảng|Lướt qua rất nhẹ và ngắn, như mùi hương trong gió.
thoáng đãng|Rộng rãi, sáng sủa và dễ chịu.
thoáng khí|Không khí trong lành, mát mẻ và dễ chịu.
thoát|Ra khỏi chỗ bị giữ, bị vướng hoặc bị cản.
thoát khỏi|Hành động rời khỏi một nơi nào đó.
thoạt tiên|Lúc khởi đầu, trước hết khi bắt đầu sự việc.
thoăn thoắt|Cử động rất nhanh và liền mạch như người đã thuần thục.
thóc|Hạt lúa còn nguyên vỏ trấu sau khi thu hoạch.
thóc gạo|Lương thực chính dùng để ăn no.
thóc lúa|Tên gọi chung lúa và hạt lúa thu được ở ruộng.
thói quen|Lối sống hay hành động lặp lại nhiều lần thành nếp khó bỏ.
thong dong|Thong thả, không vội vã.
thong thả|Làm việc chậm rãi, không vội vàng, thư thả.
thô sơ|Đơn giản, chưa hoàn thiện, thiếu kỹ thuật tinh vi.
thổ cẩm|Vải dệt thủ công của các dân tộc miền núi với nhiều màu sắc và hoa văn đẹp.
thổ lộ|Nói ra những điều bí mật hoặc kín đáo đang chứa trong lòng.
thổ nhưỡng|Chất đất xét về khả năng thích hợp cho việc trồng trọt.
thổ sản|Sản vật đặc trưng do người dân địa phương trồng trọt hoặc nuôi dưỡng.
thôi thôi|Đừng làm tiếp, dừng việc lại ngay.
thôi thúc|Giục giã, khiến muốn làm ngay, không thể chậm trễ.
thổi|Đẩy một luồng hơi ra từ miệng.
thổi cơm|Nấu ăn bằng cách quạt lửa để than hồng lên.
thổi phồng|Thêm thắt, phóng đại sự thật khiến nó trông lớn hơn hoặc quan trọng hơn.
thôn dã|Khu vực làng quê nơi dân cư sống bằng nghề nông.
thông|Cây thân gỗ thường có lá kim và quả dạng nón.
thông báo|Nói ra sự việc để mọi người cùng biết.
thông cảm|Hiểu rõ khó khăn của người khác và chia sẻ tâm tư.
thông cáo|Văn bản chính thức do cơ quan nhà nước ban hành để thông báo sự việc quan trọng.
thông dịch|Người chuyên dịch lời nói từ ngôn ngữ này sang ngôn ngữ khác.
thông dụng|Được nhiều người dùng thường xuyên trong đời sống.
thông hành|Giấy cho phép được đi qua các nơi kiểm soát.
thông hiểu|Hiểu rõ sâu sắc, nắm bắt đầy đủ ý nghĩa và chi tiết của vấn đề.
thông lệ|Tục lệ chung được cộng đồng chấp nhận và thực hành thường xuyên.
thông minh|Hiểu nhanh và biết tìm cách xử lý tình huống hiệu quả.
thông qua|Chấp thuận cho việc được thực hiện sau khi xem xét.
thông số|Đại lượng cho biết một đặc điểm của thiết bị hay quá trình.
thông suốt|Hiểu rõ toàn bộ nội dung từ đầu đến cuối.
thông thạo|Hiểu rõ và làm thành thạo mọi việc liên quan đến chủ đề đó.
thông thường|Thường xuất hiện, phổ biến và bình thường trong đời sống.
thông tin|Nội dung được truyền đi để người khác biết.
thống kê|Việc thu thập và sắp xếp số liệu để phân tích tình hình.
thốt nốt|Cây họ cau lá xòe, có dịch hoa ngọt để làm đường.
thơ ca|Tổng hợp các tác phẩm văn học viết theo vần điệu hoặc hát.
thơ phú|Thơ và văn nói chung theo cách gọi cũ.
thờ ơ|Không quan tâm, không có tình cảm.
thở dài|Thở ra một hơi kéo dài, thường vì suy nghĩ hoặc mệt.
thở dốc|Thở mạnh và nhanh do cơ thể quá mệt mỏi.
thợ bạc|Người chuyên nghề chế tác các vật phẩm bằng kim loại quý.
thợ điện|Người chuyên lắp đặt và sửa chữa đồ điện.
thợ lặn|Người làm việc dưới nước bằng dụng cụ thở.
thợ may|Người cắt vải và ráp thành quần áo theo số đo hoặc mẫu.
thợ mộc|Người làm nghề gia công gỗ để đóng, sửa đồ dùng.
thợ rèn|Người chuyên nghề rèn sắt thành các loại dụng cụ.
thợ sơn|Người chuyên nghề quét sơn, vẽ tranh lên tường hoặc đồ vật.
thợ thủ công|Người làm nghề thủ công bằng tay.
thời cơ|Khoảnh khắc thuận lợi để làm việc gì đó thành công.
thời đại|Giai đoạn lịch sử dài có những đặc điểm nổi bật riêng.
thời điểm|Khoảng thời gian cụ thể trong quá khứ.
thời giá|Mức giá bán của hàng hóa tại một thời điểm cụ thể.
thời gian biểu|Bản ghi thời gian sắp xếp các hoạt động trong ngày.
thời gian rảnh rỗi|Khoảng thời gian không phải làm việc, được dùng để nghỉ ngơi.
thời hạn|Khoảng thời gian được ấn định để làm hoặc duy trì một việc.
thời lượng|Thời gian kéo dài của một hoạt động cụ thể.
thời sự|Những sự việc mới nhất, quan trọng đang diễn ra và được nhiều người quan tâm.
thời thế|Xu hướng và hoàn cảnh xã hội trong một giai đoạn lịch sử nhất định.
thời tiết|Trạng thái của không khí như nắng, mưa, gió, lạnh hay nóng.
thời trang|Phong cách ăn mặc thịnh hành trong từng thời đại.
thời vụ|Khoảng thời gian thích hợp cho một việc, như gieo trồng một loại cây.
thơm|Có mùi dễ chịu như mùi hoa hay thức ăn mới nấu.
thơm tho|Có mùi hương dễ chịu lan tỏa trong không khí.
thớt|Miếng gỗ hoặc nhựa dày kê dưới thực phẩm khi thái.
thu chi|Việc nhận tiền vào và chi tiền ra trong quản lý tài chính.
thu dọn|Sắp xếp đồ đạc cho gọn gàng, sạch sẽ.
thu gom|Lấy vật từ nhiều nơi khác nhau để tập trung lại một chỗ.
thu gọn|Giảm kích thước hoặc số phần để đỡ chiếm chỗ.
thu hẹp|Giảm kích thước hoặc phạm vi lại cho nhỏ hơn.
thu hoạch|Lấy toàn bộ sản phẩm nông nghiệp đã trồng ra khỏi ruộng.
thu hồi|Lấy lại những gì đã trao hoặc cho người khác trước đó.
thu hút|Gây sự chú ý, làm người ta muốn nhìn vào.
thu lượm|Thu nhặt và gom góp lại những gì tìm thấy.
thu mua|Mua lại hàng hóa từ người dân để bán tiếp.
thu nhặt|Ghép lại từng chút nhỏ để tạo thành tổng số đáng kể.
thu nhận|Chấp nhận đưa vào hoặc tiếp nhận.
thu nhập|Khoản tiền hoặc lợi ích nhận được từ việc làm hay tài sản.
thu xếp|Sắp đặt công việc hoặc đồ đạc cho ổn thỏa.
thủ công|Thực hiện chủ yếu bằng bàn tay và dụng cụ đơn giản.
thủ công nghiệp|Ngành sản xuất dựa chủ yếu vào sự khéo léo của bàn tay và công cụ đơn giản.
thủ đô|Nơi đặt trụ sở chính quyền và các cơ quan lãnh đạo tối cao của một quốc gia.
thủ kho|Người trông coi và quản lý kho hàng.
thủ môn|Người chơi đứng trước khung thành để ngăn bóng vào.
thủ thành|Người đứng trước khung thành để ngăn chặn bóng vào lưới.
thủ thuật|Cách làm khéo léo đạt hiệu quả cao.
thủ thư|Người trông coi, quản lý sách báo trong thư viện.
thủ tục|Cách thức làm việc theo quy định đã thành lệ.
thú hoang|Những loài động vật sống tự do ngoài rừng, không thuần hóa.
thú thật|Nói thẳng sự thật mình thường giấu.
thú vị|Gây cảm giác thích thú và vui vẻ cho người nghe hoặc người xem.
thú vui|Điều gì gây ra niềm vui, hứng thú hoặc sở thích cho con người.
thụ động|Không chủ động hành động, chờ đợi người khác làm trước.
thụ hưởng|Nhận được lợi ích hoặc niềm vui từ những thành quả do người khác tạo ra.
thụ phấn|Hạt phấn được chuyển tới phần tiếp nhận của cơ quan sinh sản cái ở cây.
thua kém|Không bằng, kém hơn về chất lượng hoặc giá trị.
thua kiện|Bị thua trong một vụ kiện tụng, bị coi là sai lý lẽ.
thua thiệt|Bị mất mát nhiều hơn người khác trong hoàn cảnh.
thuần|Không pha lẫn thứ khác, hoặc chỉ gồm một loại.
thuần khiết|Hoàn toàn trong sạch, không lẫn tạp chất hay điều xấu xa.
thuần nhất|Chỉ gồm một chất, một loại duy nhất, không lẫn tạp chất.
thuần thục|Làm việc thành thạo nhờ luyện tập nhiều lần.
thuận buồm xuôi gió|Công việc tiến hành suôn sẻ, không gặp trở ngại.
thuận lợi|Điều kiện thuận tiện giúp việc làm dễ dàng hơn.
thuận tiện|Dễ dàng, không gặp khó khăn hay trở ngại.
thuật ngữ|Từ dùng trong ngành học để chỉ một khái niệm rõ ràng.
thuật toán|Các bước rõ ràng và hữu hạn để giải một bài toán.
thúc giục|Khuyên răn liên tục để người khác làm nhanh.
thuê|Trả tiền để được dùng vật hoặc nhờ người làm việc.
thuê bao|Người hoặc số đăng ký sử dụng dịch vụ theo thỏa thuận với nhà cung cấp.
thung lũng|Dải đất thấp nằm giữa các sườn núi hoặc đồi.
thùng|Đồ chứa khá lớn, thường để đựng hay chở hàng.
thùng thư|Hòm đựng thư đặt ở nơi công cộng để người gửi bỏ thư vào.
thùng xe|Phần chứa hàng gắn trên khung một chiếc xe tải.
thuộc lòng|Nhớ kỹ toàn bộ nội dung để có thể lặp lại bất cứ lúc nào.
thuộc tính|Đặc tính vốn có của sự vật giúp phân biệt nó với vật khác.
thuôn|Có hình dài, nhỏ dần mềm mại về một phía.
thụt lùi|Di chuyển dần về phía sau, kém tiến bộ.
thuyên chuyển|Đổi chỗ làm việc hoặc chuyển đến địa điểm khác.
thuyền|Phương tiện nhỏ đi trên mặt nước, có thể chèo bằng tay.
thuyền bè|Phương tiện giao thông nhỏ di chuyển trên mặt nước.
thuyền buồm|Thuyền dùng sức gió tác động lên buồm để di chuyển.
thuyền chài|Con tàu nhỏ dùng lưới để bắt cá trên sông biển.
thuyền nan|Thuyền được đan bằng nan tre có gắn sơn.
thuyền rồng|Thuyền dài trang trí hình rồng, thường dùng trong lễ hội hay đua thuyền.
thuyền thúng|Loại thuyền nhỏ bằng tre nứa, hình dáng như cái thúng.
thuyền trưởng|Người đứng đầu, chỉ huy toàn bộ hành trình trên biển.
thuyền viên|Người thuộc đội làm việc trên tàu, thuyền.
thuyết minh|Giải thích bằng lời để người nghe hiểu một vật, cảnh hay sự việc.
thuyết phục|Làm người khác tin là đúng và muốn nghe theo.
thuyết trình|Trình bày một vấn đề một cách rõ ràng, có hệ thống trước đám đông để mọi người hiểu.
thư điện tử|Thông điệp gửi qua mạng đến địa chỉ hộp thư của người nhận.
thư mục|Danh sách ghi tên các cuốn sách có trong thư viện để tra cứu.
thư pháp|Nghệ thuật viết chữ đẹp, chú trọng nét bút và bố cục trang trọng.
thư phòng|Căn phòng dành riêng để đọc sách, nghiên cứu trong nhà.
thư thái|Trạng thái thư giãn, thoải mái và không bị căng thẳng.
thư tín|Thư từ được gửi đi và nhận lại qua đường bưu điện.
thư viện|Nơi lưu trữ sách và tài liệu để mọi người đọc hoặc mượn.
thử nghiệm|Làm thử để xem kết quả thế nào.
thử thách|Những việc khó khăn, gian khổ cần nghị lực để vượt qua.
thứ ba|Số thứ tự đứng ngay sau cái thứ hai hoặc trước cái thứ tư trong dãy đếm.
thứ bậc|Trật tự sắp xếp phân chia cao thấp giữa các cấp bậc.
thứ cấp|Trị số được dùng sau trị số chính hoặc ban đầu.
thứ hai|Thứ đứng ngay sau cái đầu tiên trong một dãy đếm.
thứ lỗi|Tha lỗi, bỏ qua cho lỗi lầm của người khác khi xin lỗi.
thứ mười|Số thứ tự đứng ngay sau con số chín.
thứ tự|Sự sắp trước sau theo một quy tắc.
thứ yếu|Có tầm quan trọng thấp hơn việc chính.
thưa|Có nhiều khoảng trống giữa các vật cùng loại.
thưa thớt|Ít số lượng và phân bố không đều, tạo cảm giác rời rạc.
thừa hành|Thực hiện các nhiệm vụ được cấp trên giao phó.
thừa hưởng|Nhận được tài sản hoặc quyền lợi do người trước để lại.
thừa mứa|Có nhiều hơn mức cần thiết, dư dả không dùng hết.
thừa nhận|Công nhận là đúng sự thật hoặc hợp pháp.
thừa số|Số nhân dùng để tính ra kết quả khi nhân với các số khác.
thức|Không ở trong giấc ngủ, còn nhận biết xung quanh.
thức ăn|Những thứ người hay vật ăn vào để sống và lớn lên.
thức dậy|Tỉnh khỏi giấc ngủ và bắt đầu hoạt động.
thức giả|Người có trình độ học vấn cao và hiểu biết sâu rộng.
thức giấc|Tỉnh dậy sau khi đang ngủ.
thức thời|Hiểu biết và biết cách thích nghi với hoàn cảnh thời đại.
thực bì|Tầng thảm cỏ và cây bụi phủ kín trên bề mặt đất.
thực chất|Cái cốt lõi, bản chất thật sự.
thực dụng|Coi trọng lợi ích thiết thực và hiệu quả trước mắt hơn lý tưởng.
thực địa|Không gian thực tế, khác với hình ảnh trên giấy tờ hay bản vẽ.
thực đơn|Danh sách món có thể gọi hoặc dự định dùng cho một bữa.
thực hành|Làm để áp dụng lý thuyết vào thực tế.
thực hiện|Biến ý tưởng thành hiện thực bằng hành động cụ thể.
thực lực|Sức mạnh thực tế có sẵn bên trong.
thực phẩm|Nguyên liệu hoặc món đã chế biến dùng cho con người ăn uống.
thực quyền|Quyền lực thực sự, không chỉ là danh hiệu.
thực tại|Hiện thực, những gì đang tồn tại và diễn ra ngay tại thời điểm này.
thực tập|Làm việc thực tế để vận dụng kiến thức đã học, nâng cao tay nghề.
thực tế|Sự việc, hiện tượng có thật, không phải là tưởng tượng.
thực thi|Thực hiện đúng những nhiệm vụ đã được phân công hoặc các quyết định chính thức.
thực thụ|Chắc chắn là có thật, không phải giả.
thực tiễn|Những việc làm thực tế trong đời sống.
thực trạng|Tình hình, thực tế đang tồn tại một cách chân thực.
thực từ|Những từ dùng để chỉ sự việc, con người, tính chất hoặc hành động.
thực vật|Sinh vật tự chế tạo dinh dưỡng từ chất vô cơ.
thước|Dụng cụ có vạch chia để đo độ dài hoặc kẻ đường thẳng.
thước dây|Dải mềm có vạch chia, cuộn gọn được sau khi đo.
thước đo|Căn cứ được chọn để đánh giá một giá trị hay mức độ.
thước gấp|Thước đo gồm nhiều đoạn nối bằng khớp để gấp ngắn khi cất.
thước kẻ|Thanh thẳng có mép đều để kẻ đường hoặc đo đoạn ngắn.
thược dược|Cây cảnh có củ và cụm hoa lớn với nhiều lớp cánh.
thương gia|Người chuyên buôn bán hàng hóa với số lượng lớn.
thương hiệu|Tên hoặc dấu hiệu giúp nhận ra sản phẩm hay cơ sở kinh doanh.
thương lái|Người mua nguyên liệu từ nông dân rồi bán lại với giá cao hơn để kiếm lời.
thương lượng|Hai bên cùng bàn bạc để thống nhất.
thương mại|Hoạt động mua bán, trao đổi hàng hóa và dịch vụ giữa các bên.
thương mại điện tử|Hoạt động mua bán hàng và dịch vụ qua mạng.
thương nhân|Người làm nghề buôn bán, mua bán hàng hóa để kiếm tiền.
thương nhớ|Nhớ nhung người đã xa với tình cảm sâu sắc và buồn bã.
thương phẩm|Những mặt hàng được mua bán trao đổi giữa người với người.
thương thuyết|Bàn chuyện với nhau để cùng đồng ý về một điều.
thương vụ|Một vụ giao dịch mua bán có quy mô hoặc giá trị đáng kể.
thường hay|Hành động lặp đi lặp lại nhiều lần trong đời sống hàng ngày.
thường khi|Vào những lúc thường xuyên, xảy ra vào nhiều dịp khác nhau.
thường ngày|Những việc xảy ra vào mọi ngày trong cuộc sống.
thường nhật|Những ngày thường xuyên, hàng ngày.
thường niên|Một lần trong mỗi năm, lặp lại đều đặn hàng năm.
thường thức|Kiến thức phổ biến mà đa số người đều biết đến.
thường tình|Tình huống hoặc cảm xúc phổ biến ở mọi người.
thường trực|Luôn có mặt và làm việc không nghỉ ngơi.
thường xuyên|Xảy ra đều đặn, lặp lại liên tục trong thời gian dài.
thưởng|Tặng một lợi ích để ghi nhận việc làm tốt.
thượng cấp|Người đứng ở cấp bậc cao hơn trong tổ chức hoặc cơ quan.
thượng đẳng|Thuộc bậc cao, hạng nhất hoặc xuất sắc nhất.
thượng hạng|Thuộc loại hàng hóa hoặc chất lượng tốt nhất.
thượng lộ bình an|Chúc người sắp đi đường được an toàn, không gặp chuyện xui xẻo.
thượng sách|Phương pháp hay nhất để giải quyết vấn đề.
thượng tầng|Tầng trên hoặc lớp trên trong kiến trúc.
tí chút|Một lượng rất nhỏ, chỉ bằng một chút ít.
tí hon|Rất nhỏ bé về hình dáng và kích thước.
tí nữa|Trong một khoảng thời gian rất ngắn sắp tới.
tí tách|Tiếng nhỏ, ngắn lặp lại như giọt nước rơi.
tí xíu|Kích thước nhỏ bé.
tía lia|Nói hoặc làm việc liên tục không ngừng nghỉ.
tía tô|Rau thơm có lá mép răng cưa, thường tím ở một hoặc hai mặt.
tích cóp|Tích lũy tiền bạc hoặc của cải từ từ.
tích cực|Chủ động góp sức theo hướng có lợi thay vì chỉ chờ đợi.
tích góp|Gom nhặt từng chút một để tạo thành số lượng lớn.
tích hợp|Kết hợp các bộ phận nhỏ vào một tổng thể lớn.
tích số|Kết quả thu được khi nhân các số với nhau.
tích tắc|Tiếng kêu ngắn, nhanh của đồng hồ báo giờ.
tích tiểu thành đại|Góp nhặt nhiều thứ nhỏ bé lại để tạo thành một khối lớn.
tích truyện|Câu chuyện, tích cũ kể lại.
tích trữ|Góp nhặt dần để có nhiều của dùng sau.
tiệc|Bữa ăn tổ chức để nhiều người cùng dự và chung vui.
tiệc trà|Buổi tiệc nhỏ chỉ dùng nước chè và các món ăn nhẹ.
tiệc tùng|Những dịp tụ họp ăn uống và chung vui với nhau.
tiềm ẩn|Ẩn giấu bên trong, chưa thể hiện ra bên ngoài.
tiềm lực|Khả năng và nguồn lực sẵn có nhưng chưa được dùng hết.
tiềm năng|Khả năng hoặc sức mạnh có thể phát triển trong tương lai.
tiệm|Cửa hàng nhỏ bán hàng hoặc làm dịch vụ.
tiên đoán|Dự báo trước những việc sẽ xảy ra trong tương lai.
tiên phong|Người đi trước nhất trong phong trào hoặc công việc khó khăn.
tiên quyết|Việc phải làm trước khi làm các việc khác.
tiên tiến|Đạt mức phát triển mới, có nhiều ưu điểm so với trước.
tiền|Phương tiện trao đổi được chấp nhận để mua bán và thanh toán.
tiền bạc|Tiền dùng để mua sắm, chi trả cho các nhu cầu trong đời sống.
tiền bối|Người lớn tuổi hơn mình về tuổi tác hoặc kinh nghiệm.
tiền công|Khoản trả cho việc một người đã bỏ sức thực hiện.
tiền của|Tiền bạc và những tài sản khác có giá trị.
tiền góp|Tiền bạc mọi người quyên góp chung.
tiền lẻ|Những đồng tiền nhỏ, là số dư hoặc phần lẻ của đơn vị tiền tệ chính.
tiền lương|Khoản trả cho người lao động theo công việc đã làm.
tiền mặt|Tiền kim loại hoặc giấy dùng trực tiếp để mua bán, chi trả hàng hóa.
tiền nhiệm|Người đã giữ chức vụ trước đây, nói so với người đang làm việc.
tiền nong|Tiền bạc nói chung dùng cho các nhu cầu sinh hoạt.
tiền tệ|Tiền được dùng như phương tiện trao đổi và thanh toán.
tiến độ|Tốc độ và mức độ tiến hành của công việc.
tiến hành|Thực hiện công việc theo kế hoạch đã định.
tiến thoái|Di chuyển về phía trước và phía sau (nói chung).
tiến triển|Thay đổi từng bước theo một chiều hướng, thường là tốt lên.
tiến trình|Đường đi hoặc cách thức tiến hành công việc.
tiện dụng|Có ích và dễ dàng sử dụng cho công việc.
tiện lợi|Dễ dàng sử dụng và mang lại lợi ích.
tiện nghi|Những đồ dùng, thiết bị hỗ trợ sinh hoạt hàng ngày.
tiếng|Âm phát ra khiến tai có thể nghe được.
tiếng động|Âm phát ra khi vật chuyển động, cọ xát hoặc va chạm.
tiếng hót|Âm thanh chim kêu.
tiếng kêu|Âm thanh phát ra từ miệng người hoặc con vật.
tiếng lóng|Cách gọi riêng trong một nhóm, khác cách nói phổ thông.
tiếng mẹ đẻ|Ngôn ngữ đầu tiên của người đó.
tiếng nói|Tiếng người nói để bày tỏ suy nghĩ, tình cảm.
tiếng ồn|Âm thanh lớn, khó chịu làm ảnh hưởng đến sự yên tĩnh hoặc gây khó chịu cho người nghe.
tiếng rằng|Nói rằng, gọi là.
tiếng tăm|Đánh giá tốt về một người hoặc sự việc đã được nhiều người biết đến và truyền đi.
tiếng vang|Âm thanh nghe thấy lại do sóng âm dội ngược từ vật cản.
tiếp|Nối thêm vào việc đang làm, không dừng lại ở đó.
tiếp cận|Đến gần để có thể chạm hoặc nói chuyện với ai.
tiếp chuyện|Nói chuyện để tiếp đãi hoặc tiếp đón người.
tiếp dẫn|Đón tiếp và dẫn đường đi theo.
tiếp điểm|Nơi hai đường thẳng hoặc hai mặt phẳng chạm vào nhau.
tiếp đón|Đón người đến và chăm lo việc gặp gỡ, thăm hỏi.
tiếp giáp|Nằm sát nhau, không có khoảng cách ngăn cách giữa hai bên.
tiếp khách|Đón tiếp và trò chuyện với người đến thăm.
tiếp kiến|Quan chức đón tiếp khách đến thăm chính thức.
tiếp liệu|Cung cấp nguyên liệu cần thiết cho hoạt động.
tiếp lời|Nói thêm vào sau để làm rõ hoặc phát triển ý.
tiếp nhận|Đón lấy hoặc chấp nhận những gì người khác chuyển giao cho mình.
tiếp sức|Thêm sức lực vào người khác để họ làm việc tốt hơn.
tiếp tân|Đón tiếp khách đến.
tiếp theo|Đến ngay sau sự việc hoặc người khác.
tiếp thu|Nhận điều được truyền đạt và biến thành hiểu biết của mình.
tiếp tục|Tiếp diễn hành động hoặc quá trình mà không bị gián đoạn.
tiếp tuyến|Đường thẳng tiếp xúc với đường cong tại một điểm cố định.
tiếp xúc|Đụng vào nhau hoặc gặp gỡ để biết đến nhau.
tiết|Phần thời gian dành cho một giờ học theo thời khóa biểu.
tiết giảm|Giảm số lượng hoặc mức độ của việc làm nào đó một cách cố ý.
tiết kiệm|Giảm bớt chi phí không cần thiết.
tiết lộ|Cho người khác biết chuyện đã giữ kín.
tiết mục|Một phần trình diễn cụ thể trong chương trình nghệ thuật.
tiêu|Gia vị cay thơm lấy từ hạt của một loài dây leo.
tiêu biểu|Đại diện cho nhóm, làm mẫu mực để người khác noi theo.
tiêu chí|Dấu hiệu dùng để phân biệt hay đánh giá.
tiêu chuẩn|Quy định chung dùng làm thước đo để so sánh, đánh giá.
tiêu cực|Thái độ tiêu điều, không tích cực hay phấn đấu.
tiêu dùng|Sử dụng tài sản để đáp ứng nhu cầu.
tiêu đề|Dòng tên đặt cho bài viết, mục hoặc tác phẩm.
tiêu điểm|Điểm mà các tia sáng gặp nhau sau khi khúc xạ.
tiêu điều|Hoang vắng, xơ xác và buồn tẻ.
tiêu hao|Làm cho vật chất hoặc sức lực giảm đi dần dần.
tiêu khiển|Hoạt động để thư giãn hoặc làm vui lòng mình.
tiêu pha|Sử dụng tiền bạc cho các nhu cầu sinh hoạt hàng ngày.
tiêu tan|Biến mất hoàn toàn, không còn dấu vết.
tiêu thụ|Dùng hết một lượng sản phẩm, nhiên liệu hoặc năng lượng.
tiêu trừ|Loại bỏ hẳn đi.
tiêu xài|Tiêu tiền mua sắm hoặc chi dùng.
tiểu ban|Nhóm nhỏ được thành lập để bàn bạc, nghiên cứu chuyên sâu.
tiểu dẫn|Lời giới thiệu ngắn gọn ở đầu cuốn sách.
tiểu hành tinh|Những khối đá, kim loại hoặc băng bay quanh Mặt Trời, không có khí quyển và không có hình dạng cố định.
tiểu học|Học trình đầu tiên của trường phổ thông, gồm năm lớp đầu.
tiểu khu|Đơn vị hành chính nhỏ nằm trong thành phố, thuộc khu phố.
tiểu luận|Bài viết ngắn phân tích vấn đề văn hóa hoặc xã hội.
tiểu sử|Bản tóm tắt các mốc và hoạt động chính trong cuộc đời một người.
tiểu thuyết|Tác phẩm văn xuôi khá dài kể chuyện qua nhân vật và tình tiết.
tiểu thuyết gia|Người viết tiểu thuyết.
tiểu tiết|Những chi tiết nhỏ nhặt, không quan trọng trong một công việc hay sự việc.
tim đen|Nơi chứa những suy nghĩ kín đáo nhất mà người khác không hay biết.
tìm hiểu|Khảo sát, xem xét kỹ lưỡng để biết rõ nguyên nhân.
tìm thấy|Phát hiện ra cái gì đó đã tồn tại hoặc bị mất.
tìm tòi|Tìm kiếm kỹ lưỡng và kiên trì những điều mới lạ.
tin cậy|Có thể yên tâm giao việc hoặc dựa vào lời hứa.
tin đồn|Tin tức được truyền miệng, chưa được kiểm chứng chính xác.
tin học|Lĩnh vực nghiên cứu việc xử lý thông tin bằng máy tính.
tin nhắn|Lời nhắn ngắn gửi đi để thông báo hoặc trao đổi.
tin nóng|Tin tức cấp bách, quan trọng được cập nhật ngay lập tức.
tin tức|Những sự việc vừa xảy ra và mới được biết đến.
tin tưởng|Tin chắc vào khả năng hoặc lòng tốt của người khác.
tín chấp|Cho vay tiền dựa vào uy tín cá nhân thay vì tài sản.
tín chỉ|Đơn vị quy đổi khối lượng học tập trong chương trình đào tạo.
tín dụng|Việc ngân hàng cho vay và người dùng tiền vay đó.
tín hiệu|Dấu hiệu được phát ra để mang tin cho bên nhận.
tín nghĩa|Sự trung thành và giữ trọn lời hứa.
tín nhiệm|Tin tưởng vào khả năng hoàn thành nhiệm vụ.
tín phiếu|Voucher ghi nợ có hạn sử dụng do ngân hàng phát hành.
tinh anh|Phần tinh túy, xuất sắc nhất của một người hoặc một sự vật.
tinh bột|Chất dự trữ của thực vật, có nhiều trong gạo, ngô và các loại củ.
tinh cần|Siêng năng, chăm chỉ làm việc không nghỉ.
tinh chế|Lọc bỏ tạp chất để giữ lại phần tinh khiết cần thiết.
tinh chỉnh|Điều chỉnh lại chi tiết để hoàn thiện hơn.
tinh giảm|Giảm bớt số lượng hoặc quy mô một cách hợp lý.
tinh giản|Làm cho đơn giản, bớt đi những phần không cần.
tinh gọn|Giảm bớt nhân sự xuống mức tối thiểu cần thiết để công việc vẫn vận hành hiệu quả.
tinh hoa|Những phần tốt đẹp nhất, xuất sắc nhất của một sự vật.
tinh khiết|Không lẫn tạp chất, rất sạch sẽ.
tinh khôn|Thông minh, lanh lợi và biết suy nghĩ chín chắn.
tinh mơ|Thời điểm sáng rất sớm, khi mặt trời chưa mọc hoặc vừa ló dạng.
tinh nghịch|Có tính chất nghịch ngợm, tinh quái và hay làm những việc vui đùa.
tinh tấn|Làm việc rất chăm chỉ và nỗ lực hết mình không ngừng nghỉ.
tinh tế|Rất tinh vi, nhạy bén trong việc nhận biết chi tiết.
tinh thần|Tổng hợp suy nghĩ, tình cảm và hoạt động bên trong con người.
tinh thể|Chất rắn có các thành phần vi mô sắp xếp theo trật tự lặp lại.
tinh thông|Hiểu rõ và làm thành thạo việc gì.
tinh tường|Hiểu rõ mọi việc, biết rõ nguyên nhân và kết quả.
tinh ý|Có khả năng quan sát kỹ lưỡng và nhận ra những điều tinh tế.
tình bạn|Tình cảm thân thiết giữa những người cùng nhau tin tưởng.
tình cảm|Những rung động sâu sắc trong lòng trước sự việc hay con người.
tình cờ|Xảy ra không do chủ ý, ngẫu nhiên mà gặp hoặc biết.
tình hình|Tổng thể sự việc liên quan thể hiện quá trình diễn biến hoặc trạng thái hiện tại.
tình huống|Hoàn cảnh cụ thể trong đó người ta phải ứng xử hoặc quyết định.
tình khúc|Bài hát viết về chuyện tình yêu.
tình nghĩa|Tình cảm và sự biết ơn giữa người với người.
tình nguyện|Tự nguyện nhận việc không do bắt buộc.
tình thương|Tình cảm yêu thương và sẵn sàng chia sẻ, che chở cho người khác.
tình tiết|Chi tiết tạo nên hoặc làm thay đổi diễn biến câu chuyện.
tình tứ|Thấy yêu thương, đáng mến và có tình cảm sâu sắc.
tình yêu|Tình cảm sâu đậm khiến ta quý mến và muốn gắn bó.
tỉnh|Đã thức và nhận biết rõ những gì đang diễn ra.
tỉnh bơ|Giả vờ không buồn, không lo trước chuyện đáng phải chú ý.
tỉnh dậy|Thoát khỏi giấc ngủ và bắt đầu nhận biết xung quanh.
tỉnh giấc|Kết thúc giấc ngủ và trở lại trạng thái thức.
tỉnh táo|Trạng thái minh mẫn, tỉnh thức, không lơ là hoặc mất tập trung.
tĩnh điện|Điện tích đứng yên tại chỗ không di chuyển.
tĩnh lặng|Lặng và êm, hầu như không có gì xao động.
tĩnh mạch|Mạch máu vận chuyển máu nghèo oxy từ các bộ phận cơ thể trở về tim.
tĩnh mịch|Không có tiếng động, không có người qua lại.
tĩnh tại|Giữ nguyên vị trí, không di chuyển hay thay đổi chỗ.
tĩnh vật|Thể loại tranh lấy những đồ vật không chuyển động làm đề tài.
tính cách|Tổng thể những nét tâm lý ổn định, thể hiện thái độ thường thấy của người đó.
tính chất|Nét vốn có giúp mô tả một vật, chất hay hiện tượng.
tính danh|Họ và tên của người.
tính năng|Công dụng hay khả năng riêng mà một thiết bị cung cấp.
tính nết|Đặc tính, thói quen và cách ứng xử riêng của mỗi người.
tính toán|Làm các phép tính để tìm ra kết quả cụ thể.
tính trạng|Đặc điểm có thể nhận biết hay đo được ở một sinh vật.
to lớn|Có kích thước dài rộng và chiều cao vượt mức thông thường.
to tát|Lớn lao về mức độ hoặc tầm quan trọng.
to tướng|Rất to lớn, vượt quá mức bình thường.
to xác|Có thân hình to lớn, đồ sộ.
tò he|Đồ chơi dân gian nặn từ bột nhiều màu thành người, con vật hoặc hoa.
tò mò|Muốn tìm biết điều còn lạ hoặc chưa được giải thích.
tỏ ra|Thể hiện rõ ràng ra bên ngoài.
tỏ tình|Nói hoặc viết để người khác biết mình yêu quý họ.
tỏ vẻ|Thể hiện ra bên ngoài một cảm xúc hay thái độ.
toàn bộ|Mọi phần, mọi bộ phận hợp lại thành một khối hoàn chỉnh.
toàn cầu|Trải rộng hoặc có liên hệ tới khắp thế giới.
toàn diện|Đầy đủ mọi mặt, không thiếu sót phần nào.
toàn lực|Sử dụng hết sức mạnh và khả năng.
toàn phần|Chứa đủ tất cả các bộ phận.
toàn quốc|Toàn bộ lãnh thổ của một quốc gia.
toàn tài|Người có đủ mọi tài năng, khả năng xuất sắc trong mọi lĩnh vực.
toàn thể|Mọi bộ phận hợp thành một khối.
toàn vẹn|Hoàn chỉnh, không bị mất mát hay hư hại gì.
toán|Môn học về số, hình và những quan hệ giữa chúng.
toán tử|Ký hiệu dùng để chỉ hành động tính toán hoặc xử lý dữ liệu.
toang|Mở rộng hết cỡ, không còn gì che hay chắn.
toát|Rịn ra rồi hiện trên bề mặt, như mồ hôi trên da.
tóc bạc|Tóc màu trắng xuất hiện ở người lớn tuổi do tuổi tác.
tóc mai|Tóc mọc ở hai bên thái dương, thường búi lên.
tóc tơ|Một phần cực nhỏ, chẳng khác gì sợi tóc hay sợi tơ.
tỏi tây|Rau họ hành có bẹ lá ôm thành phần thân giả dài.
tóm lại|Nói ngắn gọn những ý chính nhất của vấn đề.
tóm lược|Nêu lại những ý chính quan trọng, lược bỏ chi tiết để có cái nhìn tổng quát.
tóm tắt|Viết lại ngắn gọn, chỉ nêu những ý chính quan trọng nhất.
tô điểm|Thêm màu sắc hoặc chi tiết để vật trở nên đẹp hơn.
tổ chức|Nhóm người làm việc chung vì mục đích nhất định.
tổ hợp|Nhiều thành phần được ghép theo một cách nhất định.
tổ phó|Người phụ trách một nhóm nhỏ trong đơn vị làm việc.
tổ trưởng|Người đứng đầu nhóm nhỏ trong công việc.
tố chất|Đặc tính vốn có bên trong con người, quyết định cách suy nghĩ và hành động.
tốc độ|Độ nhanh chậm của sự di chuyển hay phát triển theo thời gian.
tốc hành|Chạy xe hoặc di chuyển với vận tốc lớn nhất có thể.
tôi tớ|Người ở dưới quyền phải tuân lệnh và phục vụ người khác.
tối đa|Số lượng lớn nhất có thể.
tối giản|Chỉ phân số không thể rút gọn thêm được nữa.
tối mịt|Tối đen kịt, không thể nhìn thấy bất cứ vật gì xung quanh.
tối ngày|Suốt cả ngày, thường nhấn mạnh việc cứ lặp đi lặp lại.
tối tăm|Tối đen, không có ánh sáng hoặc không ai biết đến.
tối tân|Thuộc loại mới và hiện đại bậc nhất vào lúc đang xét.
tối thiểu|Số lượng ít nhất, không thể giảm thêm được nữa.
tối ưu|Tốt nhất, hiệu quả cao nhất trong mọi khả năng.
tôm đất|Loài tôm nhỏ thường sống chui rúc trong bùn đáy sông ao.
tôm he|Loài tôm thân dẹp, sống ở vùng nước lợ ven biển, thường dùng làm thực phẩm.
tôm hùm|Loài tôm biển lớn, đầu có nhiều gai nhọn.
tôm khô|Tôm đã được sấy khô, dùng làm gia vị cho món ăn.
tôm sú|Loài tôm biển lớn, thân đỏ, dùng làm thực phẩm.
tôn chỉ|Nguyên tắc cốt lõi định hướng hoạt động của một tổ chức.
tôn kính|Thờ phượng, quý trọng người hoặc việc rất cao.
tôn sùng|Tôn trọng và xem trọng một cách cực kỳ sâu sắc.
tôn tạo|Sửa chữa, tu bổ những phần hư hỏng nhằm giữ gìn vẻ đẹp và giá trị của công trình cũ.
tôn vinh|Khen ngợi công khai để nâng cao vị thế và danh tiếng cho người có tài đức.
tồn đọng|Còn lại chưa được xử lý hoặc giải quyết xong.
tồn kho|Số lượng hàng hóa còn lại trong kho chưa được bán hoặc sử dụng.
tồn tại|Có mặt, hiện hữu trong thực tế.
tồn trữ|Cất giữ, tích trữ đồ dùng lâu ngày.
tốn kém|Tiêu hao nhiều tiền bạc hoặc công sức.
tổng|Kết quả thu được khi cộng các số hạng.
tổng cộng|Cộng tất cả các số lại với nhau.
tổng cục|Cơ quan chỉ huy cao nhất của một ngành chuyên môn.
tổng đài|Hệ thống tiếp nhận và nối cuộc gọi đến các số hay bộ phận khác nhau.
tổng hợp|Kết hợp nhiều phần riêng lẻ thành một khối thống nhất.
tổng kết|Tổng hợp lại những việc đã làm để rút ra kết luận chung.
tổng quát|Xem xét toàn bộ vấn đề một cách chung chung.
tổng sản lượng|Tổng số lượng hàng hóa sản xuất ra trong cả nước trong một năm.
tổng số|Tổng cộng tất cả các con số lại với nhau.
tổng thầu|Đơn vị nhận toàn bộ hoặc một phần công việc từ chủ đầu tư.
tổng thể|Tổng hợp toàn bộ các bộ phận tạo nên một chỉnh thể.
tống khứ|Đuổi người khác đi khỏi nơi ở hoặc làm việc.
tốt bạn|Có nhiều người bạn chân thành, tử tế.
tốt bụng|Có lòng nhân ái, sẵn sàng giúp đỡ người khác.
tốt đẹp|Đẹp, hay, khiến lòng người hài lòng.
tốt lành|May mắn và thuận lợi trong mọi việc.
tốt nghiệp|Hoàn thành hết chương trình học ở bậc cao nhất.
tốt tiếng|Có danh tiếng tốt, được mọi người yêu quý.
tốt tươi|Cây cối xanh tốt, đẹp.
tột cùng|Đến mức độ cao nhất, không thể vượt qua hơn nữa.
tột đỉnh|Mức độ cao nhất, đạt đến giới hạn lớn nhất.
tơ duyên|Duyên phận làm vợ chồng.
tơ hồng|Cây ký sinh thân mảnh, màu vàng hoặc trắng, không có lá, quấn quanh cây chủ.
tờ lịch|Giấy in ngày tháng dùng để ghi lại thời gian.
tơi bời|Tan tành, không còn giữ được hình dáng ban đầu.
tới lui|Đi lại nhiều lần giữa hai nơi hoặc di chuyển qua lại liên tục.
tra cứu|Tìm kiếm và xác nhận thông tin cần thiết từ sách báo hay tài liệu.
trà chanh|Đồ uống làm từ nước trà, đường và chanh.
trà đen|Loại trà được chế biến bằng cách oxy hóa lá trà trước khi sấy khô.
trà sữa|Đồ uống pha trộn giữa nước trà và sữa.
trả giá|Đổi tiền hoặc bỏ công sức để mua sắm, làm việc.
trả góp|Phương thức thanh toán tiền hàng bằng cách trả từng phần vào các kỳ hạn khác nhau.
trả lại|Cho lại tiền hoặc đồ vật đã nhận cho người khác.
trả lời|Nói lại điều người khác đã hỏi.
trả ơn|Đền đáp lại những việc tốt mà người khác đã giúp mình.
trách nhiệm|Phần việc phải lo và nghĩa vụ trả lời về kết quả.
trai trẻ|Người nam giới còn nhỏ tuổi.
trải nghiệm|Cảm nhận trực tiếp những gì xảy ra trong thực tế.
trải qua|Đã từng sống hoặc gặp phải chuyện đó.
trái|Quả mọc từ hoa của cây, thường có hạt bên trong.
trái đào|Quả đào có hạt cứng, vỏ nhiều giống phủ lông tơ.
trái mùa|Xuất hiện hoặc xảy ra khi không phải là thời điểm thích hợp.
trái ngược|Chống lại nhau hoặc hướng đi khác hẳn.
trái phiếu|Giấy chứng nhận nợ của nhà nước hoặc doanh nghiệp.
trái xoan|Hình bầu dục thuôn, hay dùng để tả đường nét gương mặt.
trại hè|Nơi tập trung của thanh thiếu niên để vui chơi hoặc nghệ sĩ để sáng tác.
trại sinh|Những người tham gia sinh hoạt trong trại hè hoặc trại huấn luyện.
tràn lan|Phân tán rộng khắp hoặc nói dài dòng, không tập trung.
tràn ngập|Đầy khắp một nơi, hầu như không còn khoảng trống.
tràn trề|Nhiều đến mức không chứa hết, chảy ra ngoài.
trán|Phần mặt nằm phía trên lông mày và dưới chân tóc.
trang bị|Những đồ dùng, phương tiện hoặc kiến thức được chuẩn bị sẵn để phục vụ cho một mục đích cụ thể.
trang điểm|Dùng mỹ phẩm và quần áo để làm cho vẻ ngoài đẹp hơn.
trang hoàng|Bày biện đồ vật để làm cho đẹp hơn.
trang lứa|Nhóm người cùng tuổi và hoàn cảnh.
trang nghiêm|Có vẻ đứng đắn và gợi sự kính trọng.
trang nhã|Đẹp một cách thanh lịch, không màu mè hay phô trương.
trang sức|Những vật quý giá đeo trên người để làm đẹp và thể hiện sang trọng.
trang trại|Nơi nuôi trồng cây hoặc chăn nuôi vật nuôi quy mô lớn.
trang trí|Sắp xếp đồ vật, hoa văn để làm cho đẹp mắt.
trang trọng|Thể hiện sự nghiêm túc và tôn kính trong cách ứng xử.
tràng hạt|Chuỗi hạt dùng để tụng kinh.
tráng kiện|Cơ thể cường tráng, sức lực dồi dào và khỏe mạnh.
tráng miệng|Ăn thêm trái cây hoặc đồ ngọt sau bữa ăn chính để dịu bụng.
trạng ngữ|Thành phần trong câu chỉ thời gian, nơi chốn, nguyên nhân hoặc mục đích của việc làm.
trạng thái|Tình trạng của một vật hoặc hệ thống tại thời điểm đang xét.
tranh ảnh|Các bức vẽ và hình ảnh chụp lại sự vật, sự việc.
tranh luận|Hoạt động bàn bạc, phân tích lý lẽ để tìm ra sự thật hoặc quyết định chung.
tranh sơn dầu|Tranh vẽ bằng chất màu pha với dầu làm chất kết dính.
tranh thủ|Tận dụng quãng thời gian hay cơ hội đang có để làm việc.
tranh truyện|Truyện kể bằng hình ảnh minh họa.
trao|Đưa một vật tận tay để người khác nhận.
trao đổi|Hoán đổi lẫn nhau những thứ có giá trị tương đương về vật chất hoặc ý kiến.
trao tay|Đưa vật trực tiếp vào tay người nhận.
trao trả|Đưa lại đồ vật đã giữ cho người khác.
trào lưu|Luồng tư tưởng hoặc phong trào thu hút nhiều người tham gia.
trào phúng|Viết hoặc nói để chế giễu, phê phán thói hư tật xấu.
tráp|Hộp nhỏ có nắp, thường đựng đồ lễ hoặc vật quý.
trát|Phủ vật liệu ướt thành lớp lên một bề mặt như tường.
trau chuốt|Làm cho đẹp, chỉnh sửa kỹ lưỡng từng chi tiết hình thức.
trắc nghiệm|Phương pháp kiểm tra bằng cách chọn đáp án đúng trong nhiều lựa chọn.
trắc trở|Gặp nhiều trở ngại khiến việc làm không suôn sẻ.
trăng|Thiên thể quay quanh Trái Đất, thường thấy sáng về đêm.
trăng mật|Thời gian vui vẻ đầu tiên của cặp vợ chồng sau khi kết hôn.
trăng tròn|Trăng ở trạng thái đầy đặn, tròn hoàn toàn vào giữa tháng.
trắng đục|Màu trắng mờ mờ không trong suốt như sữa.
trắng ngần|Màu trắng sáng, trong trẻo và bóng đẹp.
trắng toát|Màu trắng quá mức, gây cảm giác khó chịu.
trắng trẻo|Da màu trắng và trông rất đẹp, sáng sủa.
trâm|Vật nhỏ dài cài vào tóc để giữ hoặc trang trí.
trâm anh|Cái trâm cài tóc và dải khăn đội đầu.
trầm lặng|Ít nói năng, giữ im lặng và không biểu lộ cảm xúc bên ngoài.
trầm mặc|Im lặng, ít nói và thường xuyên suy nghĩ.
trầm ngâm|Ngồi yên lặng suy nghĩ một cách sâu sắc.
trầm tích|Vật liệu như cát, bùn hoặc sỏi lắng đọng lại thành lớp.
trầm tư|Tĩnh lặng suy nghĩ, tập trung vào nội tâm.
trân châu|Ngọc trai quý giá, tròn trịa, sáng bóng.
trân trọng|Tỏ ý quý mến và coi trọng đối phương.
trần thuật|Kể lại sự việc một cách chi tiết và rõ ràng.
trần trụi|Không che giấu, để lộ hết mọi thứ ra ngoài.
trần tục|Những chuyện thường ngày, không thanh tao.
trấn an|Dùng lời nói hoặc hành động để làm người khác yên tâm.
trấn tĩnh|Giữ tâm trí bình thản, tránh bị hoảng loạn.
trận đấu|Cuộc thi để xem bên nào giỏi hơn.
trật tự|Cách sắp đặt có nền nếp, không lộn xộn.
trâu|Thú nuôi có sừng cong, quen sống ở đồng ruộng vùng nóng.
trâu bò|Tên gọi chung hai loại gia súc lớn thường nuôi ở nông thôn.
trầu không|Loài cây leo lá hình tim, dùng để nhai trầu hoặc đánh gió.
trầy|Bị xước nhẹ ở lớp ngoài của da hay bề mặt vật.
trẩy hội|Đi tham gia ngày hội lớn thường niên.
trẻ con|Đặc tính của người nhỏ tuổi, chưa trưởng thành.
trẻ em|Người còn nhỏ, chưa trưởng thành và chưa làm việc.
trẻ măng|Còn rất trẻ, mới chỉ vừa tròn tuổi lớn.
trẻ nhỏ|Trẻ ở lứa tuổi còn bé và cần người lớn chăm nom.
trẻ thơ|Người còn nhỏ tuổi hoặc người trẻ chưa có nhiều kinh nghiệm.
trẻ trung|Tinh thần và vẻ ngoài của người trẻ, tràn đầy sức sống.
treo|Móc vật vào điểm tựa cao để vật thả xuống.
treo giải|Đặt giải thưởng cho người làm việc khó.
trên|Ở vị trí cao hơn so với một vật hoặc một mốc.
trên dưới|Khoảng chừng một con số, có thể hơn hoặc kém đôi chút.
trêu|Nói hay làm điều đùa vui cho người khác phản ứng.
trêu ngươi|Cố ý chọc tức, làm phiền hoặc gây bực mình người khác.
tri ân|Biết ơn và ghi nhận công ơn của người khác.
tri hô|Kêu to lên để thông báo hoặc gọi người đến.
tri thức|Những điều đã học và hiểu rõ về thế giới.
trì hoãn|Chưa thực hiện ngay mà dời lại sau.
trí khôn|Khả năng tư duy, phán đoán và hiểu biết của con người.
trí lực|Năng lực tư duy và hiểu biết của con người.
trí nhớ|Khả năng lưu giữ và nhớ lại những điều đã biết trong não bộ.
trí óc|Bộ phận trong đầu dùng để suy nghĩ, nhớ và hiểu biết.
trí tuệ|Khả năng suy nghĩ, tư duy để tưởng tượng, ghi nhớ, lý luận và sáng tạo.
trí tuệ nhân tạo|Lĩnh vực xây hệ thống có thể học, suy luận hoặc giải quyết nhiệm vụ.
trị giá|Giá trị được quy ra một số tiền cụ thể.
trị số|Giá trị được biểu thị bằng con số cụ thể.
trích dẫn|Lấy nguyên văn một câu hoặc đoạn văn từ nguồn gốc để đưa vào bài viết.
trích dịch|Lấy một đoạn hoặc phần trong tác phẩm để dịch sang ngôn ngữ khác.
trích đoạn|Một phần nhỏ được cắt ra từ toàn bộ tác phẩm nghệ thuật.
trích lập|Lấy ra một phần tiền hoặc tài sản riêng để tạo thành một quỹ mới.
trích yếu|Lấy ra những nội dung cốt lõi và quan trọng nhất.
triền|Dải đất dốc thoai thoải bên đồi hoặc dọc bờ đê.
triền miên|Kéo dài liên tục không có dấu hiệu kết thúc.
triển khai|Đưa kế hoạch vào thực tế bằng các phần việc cụ thể.
triển lãm|Bày ra nhiều đồ vật, tranh ảnh để người ta đến ngắm nhìn.
triển vọng|Khả năng phát triển tốt đẹp trong tương lai của một sự vật hay con người.
triết gia|Người chuyên nghiên cứu và giảng dạy triết học.
triều cường|Kỳ nước triều lên cao và xuống thấp với biên độ lớn.
triệu|Số đếm bằng một nghìn lần một nghìn.
triệu hồi|Gọi về để trở lại nơi cũ.
triệu phú|Người có số tiền tích lũy lên đến hàng triệu đơn vị tiền tệ.
triệu tập|Gọi mọi người đến một nơi để họp bàn việc chung.
trình báo|Thông báo sự việc cho người hoặc cơ quan có quyền xử lý.
trình bày|Nêu ra các ý, sự việc hoặc số liệu một cách rõ ràng.
trình cắm|Thiết bị hoặc phần mềm gắn vào để bổ sung chức năng cho máy tính.
trình chiếu|Đưa bài nói hoặc phim lên màn hình để công chúng xem.
trình diễn|Thực hiện trước mặt đám đông để người xem thưởng thức.
trình duyệt|Chương trình máy tính dùng để xem và điều hướng trang web.
trình dược viên|Người chuyên chào hàng và bán sản phẩm dược phẩm.
trình đơn|Danh sách các lựa chọn để người dùng chọn khi điều khiển máy tính.
trình tự|Các bước hay việc sắp trước sau theo một trật tự.
trịnh trọng|Thể hiện sự nghiêm túc và tôn trọng cao độ.
trĩu|Nặng đến mức oằn hoặc chúi xuống.
trò chơi|Hoạt động vui chơi để giải trí và thư giãn tinh thần.
trò cười|Việc khiến người ta thấy buồn cười và chê trách.
trò đùa|Việc làm hay câu nói nhằm khiến người khác bật cười.
trò hề|Việc giả dối, trò đùa nhạo báng hoặc hành động lừa bịp.
trò vui|Hoạt động tổ chức để mang lại niềm vui, thư giãn cho người tham gia.
tróc|Bong lớp ngoài thành vảy, mảnh hay từng mảng.
trói buộc|Kìm hãm, ép buộc, khiến không tự do.
tròn|Có đường bao đều quanh tâm như một chiếc đĩa.
tròn trịa|Có hình hoặc đường nét tròn đầy và đều đặn.
tròn trĩnh|Tròn đầy, gọn gàng; nói người béo tốt và cân đối.
trọn gói|Bao gồm mọi phần cần thiết trong một lần đặt hoặc một mức giá.
trọn vẹn|Đầy đủ mọi phần, không thiếu hay dở dang.
trong khi|Thời điểm đang xảy ra việc khác.
trong sạch|Sạch sẽ, không lẫn tạp chất hay điều xấu xa vào.
trong sáng|Sạch sẽ, không lẫn tạp chất và không bị bẩn.
trong suốt|Chất cho ánh sáng đi qua hoàn toàn và thấy rõ hình vật bên kia.
trong trẻo|Rất sạch, không lẫn tạp chất, nhìn thấy rõ đáy.
trong vắt|Nước nhìn thấy đáy, không có cặn bẩn.
trong xanh|Màu xanh trong suốt, thường dùng để tả bầu trời không mây.
tròng đen|Phần tròn màu đen nằm giữa con ngươi trên mắt người.
trọng dụng|Dùng người tài giỏi vào vị trí quan trọng.
trọng đại|Mang tầm quan trọng rất lớn, đặc biệt và nghiêm túc.
trọng điểm|Chỗ quan trọng nhất, nơi tập trung nhiều yếu tố chính cần ưu tiên.
trọng lực|Lực hút của Trái Đất kéo mọi vật xuống phía dưới.
trọng lượng|Lực hút của Trái Đất tác dụng vào vật.
trọng tài|Người đứng ra giám sát và công nhận kết quả trong các cuộc thi đấu.
trọng tâm|Điểm mà lực hút của Trái Đất tác dụng vào vật.
trọng thể|Trang nghiêm, đầy đủ nghi thức để thể hiện sự tôn kính và quan trọng.
trọng thị|Coi trọng, dành sự tôn kính và quan tâm đặc biệt.
trọng trách|Nhiệm vụ rất quan trọng và nặng nề.
trọng vọng|Tôn trọng rất nhiều, xem trọng người khác.
trọng yếu|Có vai trò cực kỳ quan trọng, không thể thiếu được.
trôi chảy|Làm việc suôn sẻ, không gặp trở ngại hay khó khăn.
trôi nổi|Nổi trên mặt nước và di chuyển không định hướng.
trôi sông|Đi theo dòng nước mà không có chủ đích.
trồi lên|Nổi lên từ bên dưới ra phía trên.
trộn lẫn|Hòa lẫn nhiều thứ khác nhau vào cùng một chỗ.
trông cậy|Tin tưởng và dựa vào sự giúp đỡ của người khác.
trông chờ|Đợi với hy vọng điều mình mong sẽ đến.
trông mong|Mong đợi điều gì sẽ xảy ra hoặc dựa vào sự giúp đỡ của ai đó.
trông ngóng|Mong chờ một cách tha thiết để được gặp hoặc thấy người.
trông nom|Chăm sóc, lo lắng cho người khác.
trông thấy|Nhận biết rõ ràng bằng mắt hoặc giác quan.
trồng răng|Gắn các răng giả vào hàm răng để thay thế răng thật.
trồng trọt|Gieo trồng và chăm cây để thu nông sản.
trống|Nhạc cụ có mặt căng, đánh lên để tạo nhịp.
trống chầu|Trống tròn hai mặt dùng để đánh nhịp theo bài hát.
trống cơm|Trống hai mặt thường đeo ngang người và vỗ bằng tay.
trống không|Không có gì bên trong, trống rỗng hoàn toàn.
trống rỗng|Không chứa đựng vật chất, không có kiến thức hoặc nội dung.
trơ trọi|Độc thân, không có người thân hay bạn bè bên cạnh.
trơ trụi|Không còn gì che phủ, trống rỗng và không có dấu vết của sự sống hay vật chất.
trở lại|Quay về nơi xuất phát ban đầu.
trở nên|Biến đổi thành trạng thái hoặc tính chất mới.
trở ngại|Cái vật cản khiến việc làm bị khó khăn hoặc dừng lại.
trở về|Quay lại nơi ở hoặc chỗ cũ.
trở xuống|Số lượng ít hơn hoặc thấp hơn con số đó.
trớ trêu|Xảy ra trái ngược với mong đợi, gây buồn phiền.
trợ cấp|Cấp tiền hỗ trợ từ ngân sách nhà nước hoặc tổ chức cho đối tượng khó khăn.
trợ giảng|Người phụ giúp giảng viên dạy thêm ở trường đại học.
trợ giáo|Người dạy học ở trường cấp thấp.
trợ giúp|Việc hỗ trợ để giảm bớt khó khăn hoặc thiếu thốn cho người khác.
trợ lực|Tăng thêm sức mạnh hoặc khả năng.
trợ thủ|Người hỗ trợ công việc cho người khác.
trời|Khoảng không rộng nhìn thấy phía trên mặt đất.
trời đất|Khoảng trời và mặt đất, chỉ không gian tự nhiên rộng lớn quanh người.
trơn tru|Nhẵn, không gồ ghề hay thô ráp.
trù phú|Nơi dân cư đông đúc và kinh tế phát triển, giàu có.
trú ngụ|Dừng chân sinh sống tạm thời ở nơi không phải quê hương.
trụ cầu|Những cột lớn dùng để đỡ và giữ vững kết cấu cây cầu.
trúc|Cây họ tre, có thân chia đốt và thường khá thon.
trục trặc|Hoạt động không suôn sẻ, gặp sự cố khiến việc làm bị gián đoạn.
trụi|Không còn lớp lông, lá hoặc vật che phủ bên ngoài.
trùm|Phủ kín từ phía trên bằng chăn, áo hay tấm vải.
trung bình|Nằm ở mức độ giữa, không quá cao cũng không quá thấp trong thang đo.
trung bình cộng|Kết quả thu được khi chia tổng các số cho số lượng số.
trung cấp|Cấp độ học vấn ở giữa, cao hơn sơ cấp nhưng thấp hơn cao cấp.
trung chuyển|Dùng làm nơi tạm giữ đồ đạc để chuyển đi chỗ khác.
trung du|Vùng địa hình đồi chuyển tiếp từ miền núi xuống đồng bằng.
trung dũng|Trung thành với nghĩa và gan dạ, không sợ nguy hiểm.
trung điểm|Điểm chia một đoạn thẳng thành hai đoạn bằng nhau.
trung gian|Vị trí hoặc trạng thái nằm ở giữa hai phần, đóng vai trò kết nối.
trung hạn|Thời gian kéo dài ở mức trung bình, khác với ngắn hay dài hạn.
trung học|Cấp học phổ thông nằm ở giai đoạn giữa tiểu học và đại học.
trung lập|Không ủng hộ hay chống lại bên nào trong cuộc tranh chấp giữa hai phe.
trung niên|Giai đoạn tuổi đời ở giữa tuổi trẻ và tuổi già.
trung tâm|Vùng ở giữa của một khu vực hoặc không gian.
trung thành|Giữ trọn lòng tin và cam kết với người hay việc đã hứa.
trung thực|Trung thành và thành thật trong mọi việc làm.
trung tín|Giữ trọn vẹn lời hứa và luôn chân thật trong mọi việc.
trung trực|Đường thẳng cắt đoạn kia tại giữa và vuông góc với nó.
trung tuần|Khoảng mười ngày giữa của một tháng.
trung vị|Số ở vị trí giữa trong một dãy số đã được sắp xếp.
trùng hợp|Tình cờ giống nhau hoặc xảy ra cùng lúc mà không sắp trước.
trùng sinh|Sống lại một lần nữa sau khi đã qua đời hoặc biến mất.
trùng tu|Sửa chữa lại nhà cửa, công trình để chúng bền đẹp như mới.
trúng cử|Được bầu làm đại biểu hoặc giữ chức vụ.
trúng số|May mắn trúng được giải thưởng tiền bạc hoặc quà tặng trong cuộc bốc thăm.
trúng thầu|Được chọn sau khi những đề nghị cung cấp hàng hay dịch vụ được so sánh.
trúng tuyển|Thi đỗ, được chọn vào học hoặc làm việc.
truy cập|Kết nối để xem hay sử dụng dữ liệu trên một hệ thống.
truyền bá|Phổ biến rộng rãi thông tin, tư tưởng hoặc văn hóa đến nhiều người.
truyền cảm|Tạo cảm xúc mạnh khiến người nghe rung động.
truyền dẫn|Gửi thông tin từ nơi này đến nơi khác qua nhiều phương tiện.
truyền đạt|Gửi lời nói, ý nghĩ hoặc thông tin từ người này sang người khác để họ biết.
truyền động|Quá trình chuyển đổi năng lượng từ dạng này sang động năng.
truyền đơn|Tờ giấy in phát ra để cổ động, hô hào người dân làm một việc gì đó.
truyền hình|Thiết bị phát và thu hình ảnh, âm thanh qua sóng điện.
truyền khẩu|Chuyển giao thông tin qua lời nói thay vì viết.
truyền nhân|Người kế thừa di sản hoặc tiếp nối sự nghiệp của người đi trước.
truyền thanh|Thiết bị hoặc hoạt động phát sóng âm thanh ra xa.
truyền thần|Vẽ chân dung dựa trên hình ảnh hoặc quan sát trực tiếp người mẫu.
truyền thông|Đưa thông tin đến công chúng qua các kênh như báo, đài hoặc mạng.
truyền thuyết|Truyện lưu truyền trong dân gian về nhân vật hay sự kiện xưa.
truyền tin|Chuyển thông điệp đến người hoặc nơi cần nhận.
truyện|Tác phẩm kể lại một chuỗi sự việc xoay quanh nhân vật.
truyện ngắn|Truyện hư cấu có độ dài ngắn gọn.
truyện tranh|Sách kể chuyện bằng hình vẽ và chữ.
trừ bị|Dành sẵn một phần tiền của hay vật dụng để dùng sau này.
trừ phi|Ngoại trừ trường hợp này thì điều kia sẽ không xảy ra.
trữ lượng|Tổng khối lượng tài nguyên chưa được khai thác trong khu vực.
trữ tình|Nghệ thuật tập trung vào việc diễn tả cảm xúc và tâm trạng của con người.
trứ danh|Nổi tiếng khắp nơi, ai cũng đều biết đến.
trưa|Khoảng giữa ban ngày, thường quanh mười hai giờ.
trực diện|Gặp nhau trực tiếp ở phía trước mà không né tránh.
trực giác|Nhận biết rất nhanh mà chưa cần lập luận từng bước.
trực quan|Dùng hình ảnh cụ thể hay cử chỉ để giúp người học dễ hiểu.
trực thăng|Loại máy bay có cánh quạt lớn quay nhanh để nâng thân máy bay lên thẳng đứng.
trực tiếp|Gặp nhau ngay lập tức mà không cần qua người hay vật làm cầu nối.
trực tuyến|Đang được kết nối trực tiếp vào mạng lưới để trao đổi dữ liệu.
trưng bày|Đặt đồ vật ở nơi đẹp để mọi người đến xem.
trưng cầu|Hỏi ý kiến của phần lớn mọi người để ra quyết định.
trứng|Vật có vỏ do chim và nhiều động vật khác đẻ ra.
trứng cá|Trứng sinh ra từ cá.
trứng muối|Trứng đã được muối làm cứng lòng đỏ và tạo vị mặn đặc trưng.
trứng ngỗng|Kết quả không có giá trị, công sức bỏ ra mà không thu lại được gì.
trước|Ở phía mặt hướng tới hoặc ở thời điểm sớm hơn một mốc.
trước đây|Thời gian đã qua, không phải lúc hiện tại.
trước hết|Trước khi làm những việc khác.
trước khi|Thời điểm sắp xảy ra hoặc chưa thực hiện việc gì.
trước mắt|Hiện tại, ngay lúc này.
trước nhất|Dùng để bắt đầu khi liệt kê hoặc nhấn mạnh điều đầu tiên.
trước sau|Luôn giữ thái độ hoặc hành động như vậy từ đầu đến cuối.
trước tác|Tác phẩm văn học do người viết sáng tạo ra.
trước tiên|Được thực hiện đầu tiên, đứng trước mọi việc khác.
trường|Nơi người học đến lớp và được thầy cô hướng dẫn.
trường ca|Bài thơ hoặc câu chuyện kể rất dài, nhiều chương.
trường đại học|Nơi tổ chức dạy học cho người đã tốt nghiệp trung học.
trường đời|Cuộc sống con người, nơi mọi người học hỏi kiến thức và tích lũy kinh nghiệm thực tế.
trường đua|Nơi tổ chức các cuộc đua ngựa, xe đạp hoặc xe máy.
trường học|Nơi tổ chức lớp và chương trình để người học đến học tập.
trường hợp|Sự việc cụ thể đã xảy ra hoặc có khả năng xảy ra.
trường phái|Nhóm người cùng chia sẻ một tư tưởng, phương pháp hoặc phong cách riêng biệt trong khoa học hay nghệ thuật.
trường quay|Nơi chuyên dụng để diễn xuất và quay phim.
trường thiên|Tác phẩm văn học có số lượng chữ rất nhiều.
trường thọ|Sống được một thời gian dài, tuổi thọ cao.
trưởng ban|Người đứng đầu nhóm hoặc tổ chức.
trưởng phòng|Người quản lý đầu tiên của một phòng ban.
trưởng thành|Trở thành người lớn, có đủ khả năng và trách nhiệm.
trượt|Di chuyển trơn trên bề mặt mà không nhấc khỏi đó.
trượt băng|Di chuyển trên mặt băng với giày có lưỡi trượt.
trượt tuyết|Chuyển động nhanh trên mặt tuyết bằng ván trượt và gậy chống.
tu dưỡng|Rèn luyện bản thân để tốt hơn.
tu thân|Sửa đổi hành vi và tâm tính để trở nên tốt hơn.
tủ chè|Tủ gỗ có phần trưng bày, thường dùng bày ấm chén và đồ quý.
tủ kính|Tủ có mặt kính để trưng bày đồ đạc bên trong.
tủ lạnh|Thiết bị giữ thực phẩm ở nhiệt độ thấp để bảo quản lâu hơn.
tủ sách|Tủ có các ngăn hoặc đợt để xếp sách.
tụ họp|Tập trung lại thành một nhóm người tại cùng một địa điểm.
tụ tập|Tập hợp nhiều người hoặc vật cùng một nơi.
tua bin|Thiết bị quay để lấy năng lượng từ nước hoặc gió.
tua rua|Những sợi nhỏ buông rủ ở mép vải hoặc đồ trang trí.
tuân theo|Làm đúng theo yêu cầu, luật lệ hoặc chỉ dẫn.
tuân thủ|Làm đúng và nghiêm chỉnh theo quy định hoặc mệnh lệnh đã đặt ra.
tuần|Khoảng thời gian gồm bảy ngày liên tiếp.
tuần báo|Báo in hoặc phát hành mỗi tuần một lần.
tuần hoàn|Sự di chuyển liên tục theo vòng tròn.
tuần lễ|Khoảng bảy ngày, đôi khi được dành cho một hoạt động chung.
tuần lộc|Hươu sống ở phương bắc, cả con đực và con cái thường mọc gạc.
túc trực|Luôn có mặt bên cạnh để chăm sóc hoặc sẵn sàng giúp việc.
tục lệ|Những thói quen, cách sống được truyền lại từ đời này sang đời khác.
tục ngữ|Câu dân gian ngắn gói một kinh nghiệm hoặc nhận xét quen thuộc.
túi bụi|Đến dồn dập, liên tục khiến không thể ứng phó kịp.
túi khí|Thiết bị an toàn tự động bung ra khi va chạm để giảm chấn động cho người ngồi xe.
túi tiền|Số tiền có sẵn trong tay dùng để chi trả cho các nhu cầu sinh hoạt.
túi xách|Túi có quai để cầm theo khi mang đồ ra ngoài.
tùm lum|Nhiều thứ nằm lan ra khắp nơi một cách hỗn độn.
tủm tỉm|Nụ cười nhỏ nhẹ, môi khép lại, không lộ răng.
tung|Hất vật lên khỏi tay cho bay vào không trung.
tung tăng|Chạy đi chạy lại một cách vui vẻ, nhanh nhẹn.
túng bấn|Thiếu tiền bạc và đồ dùng cần thiết.
tuổi nghề|Số năm hoặc quãng thời gian một người đã làm trong nghề.
tuổi tác|Số năm đã sống của con người nói chung.
tuổi thơ|Thời kỳ còn nhỏ, tuổi non dại.
tuổi trẻ|Giai đoạn đầu đời khi một người còn trẻ và nhiều sức lực.
tuôn|Chảy hoặc trào ra liên tục thành dòng.
tuột|Trượt ra khỏi chỗ đang giữ hoặc đang mắc.
túp lều|Nhà ở đơn sơ, nhỏ bé làm bằng vật liệu tự nhiên.
tuy nhiên|Từ dùng khi ý sắp nói khác ý vừa nói nhưng vẫn cần nêu để bổ sung.
tuy vậy|Từ nối báo hiệu ý sau khác với điều có thể suy từ ý trước.
tuyên dương|Khen ngợi một cách trang trọng và công khai.
tuyên huấn|Truyền thông tin và dạy kỹ năng cho người khác.
tuyên thệ|Cam kết làm đúng lời hứa trước công chúng.
tuyển|Chọn người phù hợp trong số những người có thể tham gia.
tuyển dụng|Cơ quan chọn người vào làm việc chính thức.
tuyển sinh|Chọn và tiếp nhận người vào học một trường hay chương trình.
tuyển tập|Tập hợp các tác phẩm hoặc bài được chọn để in chung.
tuyết|Những tinh thể băng rơi xuống thành bông khi trời đủ lạnh.
tuyệt đỉnh|Đỉnh cao nhất về chất lượng, vị trí hoặc mức độ phát triển.
tuyệt đối|Không kèm giới hạn hoặc ngoại lệ trong phạm vi đang nói.
tuyệt giao|Dừng hẳn việc nói chuyện và qua lại với nhau.
tuyệt tác|Tác phẩm được đánh giá đặc biệt xuất sắc.
tuyệt vời|Rất xuất sắc, đẹp đẽ đến mức không gì sánh kịp.
tư cách|Hành vi, thái độ và phẩm chất đạo đức của con người.
tư chất|Tính chất trí tuệ vốn có của người.
tư duy|Hoạt động của trí não để suy xét, phân tích.
tư duy phản biện|Nghĩ kỹ, phân tích kỹ để kiểm tra xem thông tin có đúng không.
tư liệu|Vật dụng, tài liệu hoặc nguồn thông tin dùng để phục vụ công việc.
tư lự|Suy xét kỹ lưỡng và lo nghĩ về một vấn đề nào đó.
tư nhân|Thuộc về một người hoặc tổ chức riêng, không phải của nhà nước.
tư thái|Dáng vẻ bên ngoài và cách ứng xử của một người.
tư thế|Cách đứng, ngồi hay nằm của người ta.
tư thục|Trường học do cá nhân hoặc tổ chức tư nhân thành lập.
tư tưởng|Những ý kiến, quan điểm chung về thế giới và xã hội.
tư vấn|Đưa ra ý kiến chuyên môn để người khác cân nhắc khi quyết định.
từ biệt|Chia tay nhau khi phải rời đi xa.
từ bỏ|Từ chối, không còn quan tâm hay chấp nhận nữa.
từ chối|Không đồng ý nhận hoặc không làm theo điều được yêu cầu.
từ chức|Yêu cầu được thôi việc và rời bỏ chức vụ đang đảm nhiệm.
từ điển|Sách ghi tên từ theo thứ tự chữ cái để tra cứu ý nghĩa, nguồn gốc và cách dùng.
từ đồng nghĩa|Những từ có ý nghĩa tương đương hoặc gần giống nhau với từ đang xét.
từ ghép|Từ tạo thành từ hai hay nhiều từ nối tiếp nhau.
từ giã|Chia tay để rời đi hoặc kết thúc mối quan hệ.
từ khi|Thời điểm bắt đầu tính từ lúc đó.
từ láy|Từ gồm nhiều tiếng, trong đó có tiếng lặp lại âm của tiếng khác.
từ loại|Nhóm các từ có chức năng và hình thức giống nhau.
từ ngữ|Những tiếng nói kết hợp lại để diễn đạt một ý tưởng cụ thể.
từ nhiệm|Tự nguyện từ bỏ chức vụ đang đảm nhiệm.
từ thiện|Việc tự nguyện giúp những người đang thiếu thốn hoặc gặp khó khăn.
từ tốn|Nói năng, ứng xử chậm rãi, bình tĩnh và giữ thái độ lễ độ.
từ trường|Không gian xung quanh vật nam châm, nơi lực hút từ tính tác động đến các vật khác.
từ từ|Làm việc chậm rãi, không vội vàng.
từ vị|Đơn vị ngôn ngữ nhỏ nhất mang nghĩa.
từ vựng|Tập hợp tất cả các từ dùng trong một ngôn ngữ.
tử số|Số ở trên vạch ngang của phân số.
tử tế|Biết cư xử có tình có lý và đáng tin cậy.
tứ kết|Vòng còn tám đối thủ để chọn bốn bên vào bán kết.
tứ tung|Phân tán ra khắp nơi, nằm rải rác ở nhiều chỗ khác nhau.
tự biên tự diễn|Tự làm bài hát và hát lại ngay không nhờ người khác.
tự cấp|Tự mình tạo ra hoặc cung cấp nhu cầu cho bản thân.
tự chủ|Quản lí mọi việc riêng, không chịu sự chi phối của người khác.
tự do|Khả năng tự quyết định và hành động theo ý muốn.
tự dưng|Xảy ra đột ngột mà không có nguyên nhân hay lý do rõ ràng.
tự động|Làm việc không cần người khác nhắc nhở hay chỉ đạo.
tự giác|Biết rõ trách nhiệm và tự động làm việc.
tự hành|Có thể tự di chuyển mà không cần người khác kéo đẩy.
tự hào|Cảm thấy vui vẻ, hãnh diện về điều tốt đẹp của mình.
tự học|Tự mình tìm hiểu kiến thức mà không cần người khác hướng dẫn.
tự lập|Tự mình làm lấy việc sống, không dựa dẫm vào người khác.
tự luận|Cách làm bài bằng việc tự viết lời giải thích hay lập luận.
tự lực|Dùng sức mình làm việc, không nhờ vả người khác.
tự mãn|Tự cho bản thân là hoàn hảo, không còn thiếu sót gì về tài sản hay năng lực.
tự nguyện|Tự mình muốn làm, không ai bắt buộc.
tự nhiên|Không do con người làm nên hoặc sắp đặt.
tự phát|Tự sinh ra mà không có ai tổ chức hay lãnh đạo trước.
tự phục vụ|Tự mình làm các việc cần thiết cho cuộc sống hàng ngày.
tự quản|Tự mình trông nom và điều hành công việc của bản thân.
tự quyết|Tự mình quyết định lấy việc của mình.
tự sự|Kể lại chuyện xảy ra với mình để bày tỏ cảm xúc.
tự tiện|Làm việc theo ý riêng mà không xin phép hay hỏi ý kiến ai.
tự tin|Tin chắc vào năng lực và phẩm chất của chính mình.
tự tình|Viết thư hoặc nói chuyện để bày tỏ tình yêu với người mình thương.
tự trọng|Biết giữ gìn phẩm giá và không làm điều khiến mình hổ thẹn.
tự truyện|Sách trong đó tác giả kể lại cuộc đời chính mình.
tự túc|Tự lo liệu đủ nhu cầu vật chất, không nhờ ai.
tự xưng|Tự nhận một danh xưng hay tự giới thiệu mình theo một cách nhất định.
tựa hồ|Có vẻ như vậy, chưa chắc chắn là đúng.
tức cười|Gây ra tiếng cười vì sự vô lý hoặc sai lầm.
tức khắc|Xảy ra ngay lập tức không có sự chậm trễ.
tức là|Cũng chính là, có nghĩa là.
tức thì|Xảy ra ngay lập tức, không có sự chậm trễ.
tức tốc|Mau lẹ, khẩn trương làm ngay lập tức.
tức tối|Bực bội, giận dữ vì cảm thấy bị xúc phạm.
tưng bừng|Náo nhiệt, vui vẻ làm động cả không gian xung quanh.
từng trải|Đã gặp nhiều việc trong đời nên có kinh nghiệm thực tế.
tước|Tách dần thành từng dải hay sợi dài.
tươi cười|Mặt biểu lộ niềm vui và sự hồ hởi.
tươi mát|Tươi đẹp và dịu mát, tạo cảm giác dễ chịu.
tươi sống|Được giữ nguyên trạng thái tự nhiên, chưa qua chế biến hay nấu nướng.
tươi tắn|Sáng sủa, vui vẻ và trông rất dễ nhìn.
tươi tỉnh|Tinh thần sảng khoái, vui vẻ và tỉnh táo.
tưới|Rải nước lên cây hoặc đất để cung cấp độ ẩm.
tưới tiêu|Đưa nước vào và thoát nước ra cho cây trồng.
tươm tất|Chuẩn bị đầy đủ, ngăn nắp, khang trang.
tương đen|Nước xốt đậu sẫm màu, thường dùng làm gia vị hoặc nước chấm.
tương đối|Không hoàn toàn tuyệt đối mà chỉ đúng trong một chừng mực nhất định.
tương đồng|Có những điểm giống nhau dù vẫn còn khác biệt ở một số mặt.
tương đương|Có giá trị hoặc mức độ ngang nhau về một mặt nào đó.
tương hỗ|Hai bên cùng giúp đỡ nhau.
tương lai|Thời gian sắp đến, thời gian sau này.
tương ớt|Nước sốt làm từ ớt xay nhỏ, có vị chua cay.
tương phản|Hai sự vật, hiện tượng có tính chất trái ngược nhau.
tương quan|Trạng thái có mối liên kết chặt chẽ, ảnh hưởng lẫn nhau.
tương tác|Tác động qua lại giữa hai hay nhiều bên.
tương thân tương ái|Tinh thần cùng nhau thương yêu và giúp đỡ lẫn nhau.
tương thích|Hai thứ có thể hòa hợp, phù hợp và dùng chung được.
tương trợ|Giúp đỡ lẫn nhau trong công việc.
tương tự|Có những điểm giống nhau ở nhiều khía cạnh hoặc một số mặt nhất định.
tương ứng|Đáp lại hoặc khớp nhau chính xác về mặt ý nghĩa và chức năng.
tương xứng|Phù hợp, cân đối về giá trị hoặc mức độ với nhau.
tường|Kết cấu dựng thẳng để bao quanh hoặc chia các phòng.
tường lửa|Phần mềm kiểm soát dữ liệu vào ra mạng để chặn nguy hiểm.
tường minh|Viết ra hoặc nói ra một cách rõ ràng, chi tiết để ai cũng hiểu ngay.
tường tận|Hiểu rõ, biết hết mọi chi tiết nhỏ.
tường thuật|Thuật lại diễn biến một sự kiện cho người không trực tiếp chứng kiến.
tường trình|Kể lại có trình tự những gì đã xảy ra cho người cần biết.
tưởng chừng|Nghĩ rằng sự việc sẽ xảy ra như vậy nhưng thực tế lại khác.
tưởng tượng|Khả năng hình thành những hình ảnh mới trong tâm trí.
tượng đài|Công trình điêu khắc ngoài trời để ghi nhớ người hoặc sự kiện.
tượng hình|Dùng hình vẽ đơn giản để biểu thị ý nghĩa.
tượng thanh|Từ ngữ mô phỏng âm thanh của sự vật.
tượng trưng|Dùng vật cụ thể để đại diện cho ý niệm trừu tượng, không phải sự thật trực tiếp.
tựu trường|Học sinh trở lại trường học vào ngày đầu tiên sau kỳ nghỉ dài.
u buồn|Buồn lặng lẽ, không biểu lộ ra ngoài.
u tối|Ánh sáng yếu ớt, tối sầm và gợi cảm giác buồn bã, cô đơn.
ú tim|Trò trẻ em đi trốn rồi tìm nhau.
uẩn khúc|Việc khó hiểu, phức tạp và khó nói ra.
uất ức|Cảm thấy bực bội, khó chịu sâu sắc vì không thể làm gì để thay đổi.
ùn tắc|Trạng thái bị kẹt, không thể di chuyển hoặc lưu thông được.
ủng hộ|Tỏ ý đồng tình và giúp đỡ người khác thực hiện việc gì.
uốn cong|Làm cho vật thẳng bị cong lại theo hình vòng cung.
uốn éo|Làm dáng vẻ mềm mỏng, dịu dàng nhưng thiếu tự nhiên.
uốn khúc|Làm cong thành từng đoạn không thẳng.
uốn lượn|Uốn thành đường cong mềm mại và liên tục.
uốn nắn|Dạy dỗ, sửa lỗi để hành vi đúng đạo lý.
uốn tóc|Làm tóc quăn, giữ nếp theo kiểu.
uống|Lấy nước qua miệng và đưa xuống cổ họng.
uống nước nhớ nguồn|Luôn ghi nhớ ơn sinh thành và dưỡng dục của cha mẹ.
úp mở|Nói chuyện mập mờ, không nói rõ ràng hết ý.
uy nghi|Vẻ ngoài oai vệ, nghiêm trang khiến người ta kính nể.
uy nghiêm|Có vẻ ngoài trang trọng, nghiêm túc khiến người khác phải kính trọng.
uy thế|Quyền lực lớn khiến người khác phải kính sợ và tuân theo.
uy tín|Sự tín nhiệm người khác dành cho người hay tổ chức có hành động đáng tin.
uyển chuyển|Linh hoạt, mềm dẻo trong cử chỉ và cách nói năng.
ứ đọng|Chất lỏng hoặc người bị tắc lại không thể chảy đi.
ưa chuộng|Thích dùng cái này hơn cái khác cùng loại.
ưa nhìn|Có vẻ ngoài đẹp mắt, dễ gây thiện cảm khi nhìn.
ưa thích|Thích một điều gì đó hơn hẳn những điều khác.
ức chế|Cơ chế thần kinh làm giảm hoặc ngăn chặn phản ứng của cơ thể.
ưng ý|Cảm thấy vừa ý với điều nhận được hoặc lựa chọn.
ửng hồng|Trở nên đỏ hồng một cách tươi đẹp và rạng rỡ.
ứng biến|Thay đổi cách làm ngay lập tức để đối phó tình huống mới.
ứng cử viên|Người được chọn để tranh giành chức vụ hay tham gia cuộc bầu cử.
ứng dụng|Dùng kiến thức đã học vào việc làm thực tế.
ứng đối|Trả lời lại lời nói một cách nhanh chóng.
ứng lực|Lực xuất hiện bên trong vật khi bị tác động từ bên ngoài.
ứng nghiệm|Điều gì xảy ra đúng như lời tiên đoán hay lời cầu nguyện trước đó.
ứng phó|Làm việc nhanh chóng để đối mặt với tình huống mới.
ứng tác|Tự nghĩ ra và làm ngay khi đang diễn ra.
ứng trực|Sẵn sàng ở lại nơi làm việc để xử lý khi có việc xảy ra.
ứng tuyển|Đăng ký để được xem xét cho một vị trí đang cần người.
ứng viên|Người đăng ký tham gia cuộc thi hoặc xét tuyển.
ứng xử|Thể hiện thái độ và hành vi phù hợp trong giao tiếp với người khác.
ước chừng|Tính toán ra một con số gần đúng.
ước định|Thỏa thuận trước về nội dung và thời gian.
ước lệ|Quy ước dùng hình ảnh để biểu trưng trong nghệ thuật.
ước lượng|Đoán số lượng, khối lượng một cách đại khái.
ước muốn|Điều mong được thực hiện nhưng chưa trở thành sự thật.
ước tính|Tính toán số lượng hoặc giá trị bằng cách đoán gần đúng.
ước vọng|Điều mong muốn đạt được trong tương lai.
ươm mầm|Việc gieo hạt xuống đất để cây con mọc lên.
ướp lạnh|Cho vào nơi có đá lạnh hoặc nước đá để làm mát.
ướt đẫm|Bị nước thấm vào nhiều, ướt đều khắp bề mặt.
ướt sũng|Ướt rất nhiều, thấm đẫm nước do ngâm lâu hoặc tiếp xúc trực tiếp.
ưu ái|Yêu thương và ưu tiên đối với ai đó.
ưu đãi|Dành quyền lợi hoặc điều kiện tốt hơn cho một số người.
ưu điểm|Chỗ tốt, điểm mạnh hoặc lợi thế.
ưu phiền|Cảm thấy buồn rầu và lo lắng vì chuyện không vui.
ưu thế|Khía cạnh vượt trội hơn hẳn so với những cái còn lại.
ưu tiên|Được xem xét trước những người khác.
ưu tú|Người có tài năng xuất sắc và đạo đức tốt, được mọi người tôn trọng.
ưu việt|Có những mặt tốt nổi trội hơn khi đem so sánh.
va chạm|Hai vật đang di chuyển hoặc ở gần nhau đụng vào nhau.
vả lại|Thêm vào đó, nêu thêm lý do hoặc sự việc khác.
vạ miệng|Hậu quả xấu xảy ra vì lời nói thiếu suy nghĩ hoặc không đúng lúc.
vách|Mặt dựng đứng chia không gian, như tấm ngăn phòng.
vách đá|Bề mặt đá dựng đứng ở sườn núi, bờ sông hay ven biển.
vạch mặt|Làm cho lộ rõ bản chất xấu xa của ai.
vai trò|Nhiệm vụ hoặc vị trí quan trọng mà một người hay vật đảm nhận.
vải bạt|Loa vải dày, bền, dùng làm túi xách hoặc lều trại.
vạm vỡ|Có thân hình to lớn, cơ bắp phát triển trông rất khỏe mạnh.
van nài|Cầu xin một cách rất khẩn thiết và lâu dài.
van xin|Cầu xin người khác bằng giọng điệu khẩn thiết.
vạn năng|Có thể thực hiện được nhiều chức năng khác nhau để ứng phó với nhiều công việc.
vạn sự|Mọi chuyện, mọi việc xảy ra trong cuộc sống.
vạn sự như ý|Ước mong mọi chuyện đều suôn sẻ, tốt đẹp như ý muốn.
vạn thọ|Loài hoa cúc vàng rực rỡ, cánh nhiều, trồng làm cảnh.
vạn vật|Mọi sự vật tồn tại trong tự nhiên.
vang dội|Âm thanh vang to, dội lại mạnh mẽ và truyền đi rất xa.
vang lừng|Tiếng tăm nổi danh lan rộng khắp mọi nơi.
vang vọng|Âm thanh hoặc ý nghĩa lan truyền xa, nghe thấy rõ ở nhiều nơi.
vàng|Kim loại quý mang sắc óng ấm, hay được chế tác thành nhẫn.
vàng anh|Chim có sắc lông vàng nổi bật, thường điểm đen ở cánh hoặc đầu.
vàng bạc|Tên gọi chung hai kim loại quý thường dùng làm trang sức.
vãng lai|Đi lại, đến và đi qua lại nhiều nơi.
vanh vách|Biết rõ từng chi tiết, thuộc lòng và phân biệt rất chính xác.
vành|Vòng ngoài bao quanh một vật, như phần rìa của chiếc nón.
vành đai|Dải bao quanh một vùng, như tuyến đường vòng ngoài thành phố.
vành khuyên|Chim nhỏ có vòng lông sáng màu quanh mắt.
vành tai|Phần bên ngoài của tai có hình cong.
vào cầu|Gặp may mắn, kiếm được việc làm ăn tốt hoặc tiền bạc dễ dàng.
vào khoảng|Ước lượng thời gian hoặc số lượng không chính xác.
vay mượn|Lấy của người khác dùng thay cho việc tự mình làm ra.
vay tiền|Việc mượn tiền và hứa trả lại cùng lãi.
văn bản|Tài liệu viết ra để lưu giữ thông tin, sự kiện hoặc quy định.
văn bằng|Giấy xác nhận kết quả thi đạt yêu cầu.
văn chương|Những câu chữ, bài viết hoặc tác phẩm dùng để thể hiện tư tưởng, cảm xúc.
văn đàn|Không gian hoạt động sáng tác của các nhà văn.
văn hào|Người viết văn nổi tiếng tài năng.
văn hiến|Truyền thống văn hóa và học thuật tốt đẹp đã được tích lũy lâu đời.
văn học|Nghệ thuật viết hoặc nói bằng ngôn ngữ để phản ánh đời sống.
văn kiện|Giấy tờ quan trọng dùng để ghi chép hoặc chứng minh việc lớn.
văn minh|Trình độ phát triển cao của xã hội loài người.
văn nghệ|Các hoạt động sáng tác và biểu diễn thuộc về văn học và nghệ thuật.
văn nghị luận|Thể loại văn dùng lý lẽ để phân tích, bàn luận và giải quyết vấn đề.
văn phong|Cách chọn từ và đặt câu đặc trưng của một người viết.
văn phòng phẩm|Đồ dùng cần thiết để làm việc tại văn phòng như giấy, bút.
văn thư|Nội dung ghi chép hoặc in trên giấy.
văn vẻ|Chải chuốt, bóng bẩy, có vẻ đẹp văn chương.
văn xuôi|Văn viết thành câu và đoạn, không buộc theo nhịp hay số chữ của thơ.
vắn tắt|Ngắn gọn, cô đọng, không dài dòng khi nói hoặc viết.
vặn vẹo|Uốn cong, vặn xoắn theo nhiều hướng khác nhau.
vằng vặc|Trời sáng rực rỡ, không có mây che phủ, nhìn thấy mọi vật rất rõ.
vắng hoe|Không có người nào ở lại, hoàn toàn trống trải và im lặng.
vắng mặt|Không hiện diện ở nơi cần đến.
vắng vẻ|Không có người qua lại, ít người đến.
vặt vãnh|Nhỏ nhặt, tầm thường, không quan trọng và không đáng kể.
vân vân|Dùng để chỉ những điều còn lại tương tự như những điều đã nêu.
vẩn đục|Trạng thái nước hoặc chất lỏng bị bẩn, không trong suốt.
vấn đáp|Hỏi câu và trả lời câu để tìm hiểu hoặc kiểm tra kiến thức.
vấn đề|Việc cần phải tìm cách nghiên cứu và giải quyết.
vận chuyển|Đưa người hay hàng từ điểm này đến điểm khác.
vận dụng|Dùng kiến thức vào việc thực tế.
vận động|Hoạt động cơ thể để thay đổi vị trí so với các vật khác.
vận động viên|Người chuyên chơi thể thao và thi đấu trong các giải đấu.
vận hành|Làm cho các bộ phận hoạt động đúng chức năng và phối hợp nhịp nhàng.
vận tải|Chuyên chở hành khách hoặc hàng hóa bằng các phương tiện.
vận tốc|Tốc độ di chuyển, chỉ quãng đường đi được trong một đơn vị thời gian.
vâng lời|Thi hành đúng ý muốn của người có quyền.
vất vả|Phải dùng nhiều sức lực hoặc trí tuệ để làm việc.
vật chất|Những gì tồn tại khách quan trong thế giới vật lý.
vật dụng|Đồ cụ thể dùng trong sinh hoạt hoặc công việc.
vật liệu|Chất liệu dùng để chế tạo nên các đồ vật.
vật lực|Tài sản, công cụ và nguồn lực vật chất phục vụ cho công việc.
vật nuôi|Động vật được con người thuần hóa để nuôi dưỡng.
vật phẩm|Đồ vật, sản phẩm được chế tạo hoặc mua bán.
vật thể|Vật có hình dạng và tính chất cụ thể.
vật tư|Nguyên liệu, dụng cụ và thiết bị dùng để sản xuất.
ve chai|Chai lọ và những thứ phế liệu thu gom để bán hay tái chế.
vẻ vang|Sự nổi tiếng, uy tín và danh dự cao quý của một người hoặc gia đình.
vé số|Tờ giấy ghi số để mua may mắn, hy vọng trúng giải thưởng tiền bạc.
ven đô|Khu vực nằm ngay bên ngoài thành phố lớn.
vẹn toàn|Hoàn hảo, không thiếu sót hay sai lầm ở bất kỳ điểm nào.
về hưu|Đến lúc nghỉ việc, không còn làm công ăn lương nữa.
về sau|Thời gian diễn ra sau khi sự việc đã xảy ra.
vệ tinh|Vật thể chuyển động trên quỹ đạo quanh một thiên thể lớn hơn.
vênh|Cong lệch khỏi mặt phẳng ban đầu, như tấm gỗ bị ẩm.
vết tích|Dấu vết còn sót lại của những gì đã từng tồn tại.
vi ba|Sóng vô tuyến có bước sóng ngắn hơn sóng radio nhưng dài hơn tia hồng ngoại.
vi lượng|Số lượng rất ít nhưng lại có vai trò quan trọng.
vi mạch|Bảng mạch điện tử nhỏ chứa nhiều linh kiện.
vi phạm|Làm trái quy định hoặc luật lệ đã đặt ra.
vi tính|Kỹ thuật xử lý thông tin bằng máy tính cỡ nhỏ.
vi vu|Tiếng gió mảnh và kéo dài khi luồn qua khe hoặc cành lá.
vì kèo|Cấu kiện gỗ hoặc thép dùng để đỡ mái nhà.
vì sao|Lý do khiến một việc gì xảy ra hoặc nguyên nhân của sự việc.
vì thế|Do đó mà dẫn đến kết quả này.
vĩ đại|Lớn lao, phi thường, có tầm vóc vượt trội.
vĩ mô|Xét ở tầm nhìn rộng lớn, bao quát toàn bộ hệ thống.
vĩ nhân|Những người có tài năng kiệt xuất, đóng góp lớn lao thúc đẩy tiến bộ của nhân loại.
ví dụ|Một trường hợp cụ thể dùng để minh họa cho nội dung chung.
ví như|Giống như, dùng để so sánh hoặc đưa ra trường hợp tương tự.
vị giác|Khả năng cảm nhận vị ngọt, mặn, chua, đắng, umami.
vị ngữ|Phần cuối câu dùng để nói rõ hành động, tính chất hoặc trạng thái của chủ thể.
vị tha|Lấy lòng thương người mà chỉ chăm làm lợi cho kẻ khác.
vị thành niên|Người chưa đủ tuổi để pháp luật công nhận đầy đủ quyền lợi.
vị trí|Chỗ ở, địa điểm cụ thể.
vỉa hè|Dải dành cho người đi bộ nằm sát bên lòng phố.
việc|Điều cần làm để đạt một kết quả nhất định.
việc làm|Hoạt động lao động cụ thể được giao làm và nhận tiền lương.
viên mãn|Hoàn hảo, đầy đủ mọi mặt.
viền|Dải hẹp chạy quanh mép vải hoặc ven một vật.
viển vông|Không thực tế, chỉ là suy nghĩ xa vời.
viễn thám|Quan sát vật thể từ xa bằng thiết bị kỹ thuật.
viễn thông|Việc liên lạc qua đường không khí hoặc sóng điện từ.
viễn tưởng|Hình dung về những điều chưa có thật, thường trong tương lai.
viện bảo tàng|Nơi lưu giữ và bảo quản các hiện vật lịch sử quý giá.
viện dẫn|Dẫn ra bằng lời hay bằng chứng để làm căn cứ cho lập luận.
viết|Tạo chữ trên giấy hay bề mặt khác để ghi lại ý.
viết lách|Viết bài văn, viết sách hoặc làm việc với bút mực.
viết tay|Viết bằng tay trên giấy, không dùng máy.
viết tắt|Ghi một tên hoặc cụm từ bằng dạng rút gọn.
việt dã|Chạy bộ đường dài vượt qua nhiều địa hình khác nhau.
vinh danh|Khen ngợi công lao, danh tiếng của người khác.
vinh dự|Cảm giác tự hào vì được làm việc tốt hoặc có thành tích đáng khen.
vinh quang|Vẻ đẹp lộng lẫy, đáng tự hào và tôn vinh.
vĩnh cửu|Không bao giờ kết thúc, tồn tại mãi mãi.
vĩnh hằng|Tồn tại mãi mãi không bao giờ kết thúc hay thay đổi.
vĩnh viễn|Tồn tại mãi mãi không có điểm bắt đầu hay kết thúc.
vịnh|Phần biển lấn vào đất liền và được đất bao quanh một phần.
vịt trời|Loài vịt hoang bay giỏi, di cư về vùng ấm vào mùa đông.
vò võ|Lẻ loi, lang thang, không có người nào cùng đi hoặc ở lại.
vỏ chuối|Lớp da mỏng bao bọc bên ngoài quả chuối.
vóc dáng|Dáng dấp và vóc người của con người.
vòi nước|Thiết bị gắn vào ống nước để điều tiết dòng chảy.
vòi vĩnh|Cố đòi hỏi, năn nỉ để được nhận.
vòi voi|Phần mũi kéo dài, linh hoạt để voi cầm nắm và hút nước.
vòng hoa|Những bông hoa được buộc lại thành hình tròn để trang trí hoặc làm lễ.
vòng quanh|Di chuyển theo hình tròn bao quanh một vật.
vòng tròn|Đường cong khép kín, mọi điểm trên đó cách tâm một khoảng bằng nhau.
vòng xuyến|Đường giao thông hình tròn để xe chạy vòng quanh tránh kẹt.
võng|Tấm vải hoặc lưới treo hai đầu để nằm đung đưa.
võng mạc|Màng mỏng ở đáy mắt, nơi tiếp nhận hình ảnh vật thể.
vô biên|Không gian rộng lớn không có điểm kết thúc.
vô bổ|Không có lợi ích, không giúp ích được gì.
vô cảm|Không còn cảm xúc hay rung động trước mọi sự việc.
vô can|Hoàn toàn không liên quan, không dính dáng gì đến sự việc hay vấn đề đó.
vô căn cứ|Không có lý do hay bằng chứng nào làm nền tảng.
vô chủ|Không thuộc về ai, không có chủ sở hữu.
vô cớ|Không có nguyên nhân hay lý do chính đáng nào cả.
vô cùng|Đạt mức rất cao hoặc không có giới hạn thấy được.
vô cực|Lớn hơn mọi con số có thể nghĩ ra.
vô danh|Không có tên gọi; người ta không biết tên ai đó.
vô dụng|Không có tác dụng hay giá trị gì cả.
vô duyên|Thiếu sự khéo léo, không biết cách ứng xử tế nhị.
vô định|Không xác định được rõ ràng ai hay cái gì.
vô đối|Không ai sánh kịp.
vô giá|Không thể định giá, quý giá đến mức không có tiền nào mua nổi.
vô hại|Không gây tổn hại, vô ích gì cho ai.
vô hiệu|Không còn tác dụng hay giá trị.
vô hình|Không có hình dáng cụ thể hoặc mắt thường không nhìn thấy được.
vô ích|Không mang lại giá trị hay lợi ích gì.
vô lăng|Vành tròn dùng để điều khiển phương tiện di chuyển.
vô song|Không có ai sánh được.
vô số|Số lượng nhiều đến không thể đếm được.
vô sự|Không gặp tai nạn hay rủi ro bất ngờ.
vô tận|Không bao giờ kết thúc, không có điểm dừng.
vô thời hạn|Không bị giới hạn bởi một khoảng thời gian cụ thể hay ngày kết thúc.
vô thượng|Đứng ở vị trí cao nhất, không có gì hơn.
vô tình|Xảy ra ngoài ý định, không phải do chủ tâm.
vô tuyến|Truyền tín hiệu qua không gian mà không cần dây nối.
vô tư|Thản nhiên, không bận tâm hay tính toán.
vô vàn|Nhiều đến mức khó đếm hoặc kể ra cho hết.
vô vị|Không có hương vị ngon, hoặc sự việc nhàm chán, không hấp dẫn.
vồ vập|Chào đón người khác quá nhiệt tình.
vỗ béo|Cho ăn nhiều để vật nuôi nhanh chóng tăng cân.
vỗ tay|Tạo tiếng bằng cách cho hai bàn tay chạm nhau nhiều lần.
vỗ về|An ủi, làm dịu nỗi đau hay sự khó chịu.
vôi bột|Vôi đã được nghiền nhỏ thành dạng bột mịn.
vội vã|Làm việc nhanh chóng, không chậm trễ vì muốn kịp giờ.
vội vàng|Hành động gấp, ít dành thời gian để thong thả cân nhắc.
vôn kế|Dụng cụ dùng để đo mức độ chênh lệch điện áp trong mạch.
vốn liếng|Số tiền tích lũy dùng để làm ăn hoặc chi tiêu.
vở kịch|Loại kịch bản nghệ thuật có nhiều nhân vật được diễn giả hóa trang biểu diễn.
vỡ lẽ|Hiểu rõ được bản chất sự việc sau khi tìm tòi.
vỡ lòng|Bắt đầu học đọc và viết những điều cơ bản đầu tiên.
vợ chồng|Hai người nam nữ kết hôn, sống chung và có trách nhiệm với nhau.
vợ chưa cưới|Người phụ nữ đã hứa kết hôn với người khác.
vợ con|Vợ và con cái, thành viên trong gia đình của người đàn ông.
với nhau|Cùng tồn tại hoặc thực hiện hành động với người khác.
vu vơ|Làm việc không có mục đích, không rõ nguyên nhân.
vũ công|Người chuyên thực hiện các động tác múa trên sân khấu hoặc trong cuộc vui.
vũ trụ|Không gian vô tận chứa đựng mọi thiên hà.
vú sữa|Quả có vỏ nhẵn, phần thịt ngọt và tiết ra nước trắng đục.
vụ việc|Sự việc không tốt, thường thu hút sự chú ý của mọi người.
vui chơi|Làm những việc để giải tỏa tâm tư, tìm thấy niềm vui.
vui lòng|Cảm thấy hài lòng và sẵn sàng đồng ý.
vui mừng|Cảm thấy sung sướng, hân hoan trong lòng.
vui nhộn|Vui vẻ, ồn ào và khiến mọi người cùng cười.
vui sướng|Cảm thấy sung sướng, vui vẻ trong lòng.
vui thích|Cảm thấy sung sướng và thích thú.
vui thú|Cảm thấy vui vẻ và thích thú với điều gì đó.
vui vẻ|Có tâm trạng thoải mái và thể hiện niềm vui ra ngoài.
vun trồng|Chăm sóc cây cối để chúng lớn lên và phát triển.
vun vén|Khéo chăm lo và thu xếp từng chút cho việc chung hoặc gia đình.
vùn vụt|Chạy hoặc tăng lên rất nhanh.
vụn vặt|Nhỏ bé, không quan trọng, không đáng kể.
vung|Đưa tay hay đồ vật theo một đường rộng và nhanh.
vung vãi|Rơi ra, lan ra khắp nơi một cách không ngăn nắp, không trật tự.
vùng cao|Khu vực có địa hình nằm cao so với vùng đồng bằng quanh đó.
vùng đất|Lãnh thổ, khu vực địa lý của một quốc gia.
vụng về|Làm việc không khéo léo, thiếu cẩn thận.
vuông|Có bốn cạnh dài bằng nhau và bốn góc 90 độ.
vuông góc|Hai đường thẳng cắt nhau tạo thành góc bằng chín mươi độ.
vuông vức|Có các cạnh và góc rõ ràng, đều và ngay ngắn.
vuốt ve|Vuốt nhẹ cơ thể để thể hiện tình cảm trìu mến.
vừa lòng|Cảm thấy hài lòng vì phù hợp với ý muốn.
vừa mới|Xảy ra trong khoảng thời gian gần đây vừa qua.
vừa phải|Ở mức độ vừa đủ, không quá nhiều cũng không quá ít.
vừa rồi|Trong quãng thời gian rất gần trước lúc đang nói.
vững bền|Bền chắc, không bị lung lay hay sụp đổ trước tác động.
vững chãi|Bền chắc, không dễ bị lung lay hay đổ ngã.
vững chắc|Được xây dựng hoặc tạo nên rất bền, khó bị hư hỏng hay đổ vỡ khi có lực tác động.
vững vàng|Có sức mạnh nội tại để đứng vững trước mọi khó khăn và tác động xấu.
vườn|Khoảng đất trồng cây, hoa hoặc rau, thường gần nhà.
vườn bách thảo|Vườn trồng và giới thiệu nhiều loài cây để học tập, nghiên cứu hay tham quan.
vườn bách thú|Nơi công cộng nuôi nhiều loài thú để người ta xem và học hỏi.
vườn hoa|Khu đất trồng hoa để ngắm hoặc lấy hoa.
vườn quốc gia|Khu bảo tồn thiên nhiên có quy chế bảo vệ ở cấp quốc gia.
vương vãi|Rơi rớt, lan tán khắp nơi không tập trung thành một chỗ.
vương vấn|Cảm thấy nhớ nhung, quyến luyến mà không thể dứt bỏ.
vướng mắc|Bị vật gì chặn đường khiến việc làm không trôi chảy.
vướng víu|Bị vướng phải nhiều thứ, gây cản trở hoạt động.
vượt|Qua được vật cản, giới hạn hoặc người đang ở phía trước.
vượt bậc|Tiến xa rõ rệt so với mức trước hoặc mặt bằng chung.
vượt qua|Qua được vật cản hoặc hoàn thành một thử thách.
vượt trội|Đi qua hoặc đạt được mức độ cao hơn hẳn những người khác.
vứt bỏ|Làm mất vật không cần dùng nữa bằng cách quăng đi.
xa cách|Ở cách xa nhau, không gặp gỡ hay gần gũi.
xa hoa|Sang trọng quá mức, tốn kém tiền bạc chỉ để khoe khoang.
xa lạ|Chưa quen biết hoặc khác những gì từng gặp.
xa lắc|Rất xa, cách trở đến mức khó tưởng tượng.
xa lộ|Đường lớn dành riêng cho xe hơi.
xa tít|Cự ly rất lớn, vượt quá tầm nhìn của mắt thường.
xa xăm|Chỉ khoảng cách rất lớn hoặc thời gian đã qua lâu lắm.
xa xỉ|Tốn tiền nhiều cho những thứ không cần thiết.
xa xưa|Thuộc thời rất lâu trước hiện tại.
xà bông|Chất tẩy rửa dùng để giặt quần áo.
xà cừ|Cây bóng mát thân gỗ lớn, thường được trồng thành hàng ven đường.
xà lách|Loại rau lá nhỏ, quăn, dùng ăn sống trong bữa cơm.
xà phòng|Chất dùng với nước để rửa sạch dầu và bụi bẩn.
xả láng|Làm việc hết sức, không giữ lại hay kìm hãm gì cả.
xã giao|Làm việc chung với người khác, giữ phép lịch sự xã hội.
xã hội|Tập hợp những người cùng sống, làm việc và tương tác với nhau.
xác đáng|Chính xác, đúng sự thật và hợp lý.
xác định|Việc khẳng định chắc chắn về một điều gì đó.
xác lập|Thiết lập một quy định hoặc tổ chức dựa trên nền tảng chắc chắn.
xác minh|Làm rõ sự thật bằng chứng cứ cụ thể và thực tế.
xác nhận|Khai báo lại là điều đó đúng sự thật.
xác suất|Số đo khả năng một kết quả xảy ra, từ không đến một.
xác thực|Có căn cứ để tin là đúng, không phải bịa hay giả.
xanh|Có màu như lá cây tươi hoặc như bầu trời quang.
xanh biếc|Sắc xanh tươi và đậm, thường gợi bầu trời hoặc mặt nước.
xanh da trời|Sắc xanh nhạt gợi màu bầu trời quang đãng.
xanh dương|Màu xanh giống màu của biển cả.
xanh lá cây|Màu xanh điển hình của lá còn tươi.
xanh lơ|Màu xanh nhạt giống màu nước lơ.
xanh tươi|Có màu xanh đậm, cây cối phát triển mạnh và tràn đầy sức sống.
xanh xanh|Màu sắc hơi ngả về xanh.
xao xuyến|Lòng cảm thấy bồi hồi, xao động không yên.
xáo động|Gây ra tiếng ồn lớn, làm mất yên tĩnh.
xáo trộn|Đảo lộn trật tự, làm cho mọi thứ không còn ổn định.
xảy ra|Trở thành sự việc, hiện tượng.
xăng|Nhiên liệu lỏng nhẹ, thường dùng cho động cơ ô tô, xe máy.
xấp xỉ|Chỉ số lượng hoặc giá trị chênh lệch nhau rất nhỏ, gần như bằng nhau.
xập xình|Tiếng ồn ào, hỗn độn vang lên liên tục như nhạc cụ.
xấu xa|Thiếu đạo đức, làm việc trái lương tâm khiến người khác phải chê trách.
xây dựng|Tạo nên công trình bằng cách ghép vật liệu theo thiết kế.
xây đắp|Làm công trình hoặc sự vật cho vững chắc thêm.
xe ben|Xe tải có thùng sau nâng lên để đổ hàng nhờ hệ thống thủy lực.
xe bò|Xe chở đồ hoặc người, dùng bò làm sức kéo.
xe buýt|Ô tô chở khách theo tuyến với những điểm dừng quy định.
xe ca|Xe buýt lớn chuyên chở hành khách đi đường dài hoặc di chuyển.
xe con|Ô tô có kích thước nhỏ gọn.
xe cộ|Tên gọi chung các phương tiện có bánh dùng để đi lại.
xe du lịch|Loại ô tô chuyên chở hành khách đi tham quan hoặc công tác.
xe đạp|Xe thường có hai bánh, người đi đạp bàn đạp để chạy.
xe điện|Phương tiện có bánh chuyển động nhờ động cơ dùng điện.
xe đò|Ô tô chở khách theo tuyến, thường đi từ địa phương này tới địa phương khác.
xe gắn máy|Xe nhỏ có động cơ, thường có hai bánh và người lái ngồi trên yên.
xe kéo|Xe nhỏ có càng để người đi bộ kéo khách hay hàng.
xe khách|Ô tô chở nhiều hành khách, thường chạy theo tuyến.
xe lam|Xe ba bánh gắn máy, nhỏ như ô tô, dùng chở người hoặc hàng hóa.
xe máy|Xe thường có hai bánh và động cơ, người lái ngồi điều khiển.
xe ôm|Nghề chở khách bằng xe máy để kiếm tiền sống.
xe tải|Ô tô thiết kế chủ yếu để chở hàng hóa.
xem xét|Quan sát kỹ lưỡng để đưa ra nhận định hoặc kết luận.
xen canh|Cách trồng hai loại cây khác nhau xen kẽ nhau trên cùng một diện tích.
xen kẽ|Đặt các vật khác loại xen vào nhau liên tục.
xẻng|Dụng cụ cán dài, lưỡi rộng để xúc đất hoặc cát.
xét tuyển|Đánh giá hồ sơ để chọn người phù hợp theo quy định.
xê dịch|Di chuyển vị trí trong khoảng cách ngắn.
xếp đặt|Sắp xếp đồ vật vào vị trí theo trình tự.
xếp hàng|Đứng lần lượt thành một dãy để chờ tới lượt mình.
xi măng|Chất kết dính dạng bột, trộn nước rồi đóng rắn trong xây dựng.
xì dầu|Nước chấm làm từ đậu tương lên men, ngũ cốc rang, nước và muối.
xì xào|Nói nhỏ tiếng, xì xầm để bàn tán về chuyện người khác.
xì xầm|Nói chuyện nhỏ nhẹ, chỉ khe khẽ.
xí ngầu|Đồ chơi hình khối nhiều mặt dùng để gieo tung.
xí nghiệp|Cơ sở tổ chức lao động để sản xuất hoặc cung cấp dịch vụ.
xích|Dây gồm các vòng cứng móc nối với nhau.
xích đạo|Đường vòng tưởng tượng chia Trái Đất thành hai nửa bằng nhau.
xích đu|Ghế hoặc tấm ngồi treo lên để đưa qua đưa lại.
xích lô|Xe ba bánh có chỗ ngồi phía trước, người đạp ngồi phía sau.
xiếc|Màn diễn đòi hỏi thăng bằng, nhào lộn hay phối hợp động tác tinh xảo.
xiên|Đưa que nhọn xuyên qua vật, như khi xâu thức ăn để nướng.
xiêu|Nghiêng sang bên, không còn đứng vững như trước.
xiêu lòng|Thay đổi ý kiến theo người khác.
xiêu vẹo|Không đứng thẳng vững vàng mà nghiêng lệch nhiều hướng.
xin chào|Lời nói thể hiện sự chào hỏi lễ phép khi lần đầu gặp nhau.
xin lỗi|Thừa nhận sai lầm và cầu xin sự tha thứ.
xin việc|Nộp đơn hoặc trình bày nguyện vọng để được nhận vào làm một công việc.
xinh|Có nét đẹp nhỏ nhắn, dễ gây thiện cảm.
xinh đẹp|Có vẻ ngoài ưa nhìn, trang nhã và hài hòa.
xinh tươi|Đẹp và rạng rỡ, tràn đầy sức sống.
xinh xắn|Có vẻ đẹp dễ thương và đáng yêu.
xíu mại|Món nhân thịt băm nặn viên hoặc bọc vỏ mỏng rồi làm chín.
xoài|Quả nhiệt đới có hạt dẹt lớn, thịt thường vàng và thơm khi chín.
xoành xoạch|Làm việc liên tục, lặp đi lặp lại trong thời gian ngắn.
xoay|Làm cho vật quay quanh một tâm hay một trục.
xoay quanh|Di chuyển theo vòng tròn quanh một điểm hoặc tập trung vào một chủ đề.
xoay xở|Tìm mọi cách để giải quyết khó khăn hoặc đạt được mục đích cần thiết.
xoăn|Uốn thành nhiều lọn hoặc vòng nhỏ như một số kiểu tóc.
xóm giềng|Những người sống chung quanh nhà mình.
xong|Đã đạt tới lúc hoàn tất, không còn phần cần làm.
xong xuôi|Hoàn thành xong mọi việc một cách suôn sẻ.
xô đẩy|Đẩy nhau bằng sức mạnh.
xôn xao|Nhiều tiếng nói, âm thanh vang lên liên tục và rộn ràng.
xốn xang|Bồn chồn, lo lắng khiến tâm trí không thể yên tĩnh.
xông xáo|Chạy nhanh vào mọi nơi, không ngại khó khăn.
xởi lởi|Thái độ vui vẻ, hòa đồng và dễ dàng tiếp xúc.
xu hướng|Chiều biến đổi hoặc cách lựa chọn ngày càng rõ.
xu thế|Hướng biến đổi chung đang dần hiện ra.
xú uế|Mùi hôi thối, bẩn thỉu.
xuân|Mùa trong năm đến sau mùa đông, trước mùa hè.
xuất bản|Viết xong bài rồi in ra và phát hành.
xuất cảng|Đưa hàng hóa từ trong nước ra bán ở nước ngoài.
xuất chúng|Có năng lực vượt rõ rệt so với phần đông.
xuất hiện|Trở nên hiện ra, có thể nhìn thấy được.
xuất khẩu|Đưa hàng hóa ra nước ngoài để bán.
xuất phát|Bắt đầu đi ra hoặc lấy làm gốc để làm.
xuất thân|Nơi sinh ra, nguồn gốc xuất phát của một người.
xuất xứ|Nguồn gốc, nơi sinh ra của một văn bản hoặc tác phẩm nghệ thuật.
xúc động|Có cảm xúc mạnh trước điều mình thấy, nghe hay nhớ lại.
xúc giác|Khả năng cảm nhận khi da tiếp xúc với vật thể xung quanh.
xúc tiến|Lần lượt làm những việc cần để một kế hoạch tiến nhanh hơn.
xúc tu|Cánh tay mềm ở đầu động vật dùng để bắt mồi.
xúc xích|Món thịt xay tẩm gia vị nhồi trong vỏ thành từng đoạn dài.
xung quanh|Vùng bao bọc bên ngoài một vật hay địa điểm.
xúng xính|Đeo quần áo rộng thùng thình, trông rất sang trọng.
xuôi|Đi cùng chiều dòng nước hoặc theo hướng thuận.
xuôi chiều|Đồng ý theo ý kiến chung, không có quan điểm trái chiều.
xuôi dòng|Theo chiều nước chảy từ trên xuống dưới.
xuồng|Thuyền nhỏ thân thon, thường dùng trên kênh rạch.
xuống cấp|Trở nên kém chất lượng, hư hỏng dần theo thời gian.
xuống dốc|Di chuyển từ vị trí cao xuống thấp hoặc tình trạng xấu đi nhanh chóng.
xuyên|Đi qua hoặc thông từ phía này sang phía kia của vật.
xuyên suốt|Tiếp diễn liên tục trong suốt một khoảng thời gian.
xử trí|Giải quyết vấn đề theo tình hình cụ thể.
xứ sở|Đất đai, lãnh thổ hoặc nơi sinh sống.
xưa kia|Vào thời trước, cách hiện tại một quãng khá lâu.
xưa nay|Khoảng thời gian kéo dài từ quá khứ xa xưa cho đến tận lúc hiện tại.
xưng hô|Cách tự gọi tên mình và gọi người khác khi trò chuyện.
xưng tụng|Ca ngợi, khen ngợi người khác một cách trân trọng.
xứng đáng|Đáng được hưởng những phần thưởng hoặc quyền lợi tương xứng.
xương rồng|Cây mọng nước thích nghi với nơi khô, nhiều loài có gai.
xương sống|Cột trụ bằng xương nằm giữa lưng, giữ cho cơ thể đứng vững.
xương sườn|Những xương nằm ở hai bên lồng ngực, nối từ cột sống ra phía trước.
y hệt|Giống hệt nhau, không khác gì.
y như|Giống hệt như; (khẩu ngữ) nhấn mạnh sự lặp lại y hệt nhiều lần.
y như rằng|Đúng như mong đợi hoặc như đã hy vọng trước đó.
y phục|Đồ dùng để che thân, bao gồm quần và áo.
ý chí|Khả năng muốn làm điều gì đó một cách kiên quyết.
ý định|Lòng muốn làm một việc gì đó trước khi bắt đầu hành động.
ý kiến|Điều một người nghĩ và nêu ra về vấn đề đang bàn.
ý muốn|Điều người ta mong muốn.
ý nghĩ|Điều vừa xuất hiện hoặc đang được suy xét trong đầu.
ý nghĩa|Nội dung thực sự mà lời nói hoặc ký hiệu muốn truyền tải.
ý nguyện|Điều một người thành tâm mong muốn được thực hiện.
ý nhị|Lời nói hay cử chỉ kín đáo, hàm chứa nhiều ý nghĩa sâu.
ý niệm|Sự hiểu biết sơ bộ, hình dung ban đầu về một vấn đề.
ý tưởng|Điều nảy ra trong trí, có thể phát triển thành một việc mới.
yếm dãi|Mảnh vải nhỏ đeo trước ngực trẻ em để thấm nước dãi.
yếm thế|Chán nản, không còn hy vọng vào tương lai.
yên ả|Yên tĩnh, không có tiếng động, tạo cảm giác bình yên.
yên ắng|Yên tĩnh, im lìm không có tiếng động.
yên giấc|Ngủ sâu, không bị đánh thức giữa đêm.
yên lành|Trạng thái bình an, không có sự cố hay tai ương xảy ra.
yên lặng|Không phát ra tiếng động và giữ sự bình tĩnh tuyệt đối.
yên lòng|Tâm trí bình thản, không còn điều gì phải lo.
yên phận|Bằng lòng với số phận, sống an tâm với hiện tại.
yên tâm|Trạng thái tâm lý bình yên, không còn lo lắng hay nghi ngờ gì nữa.
yên thân|Được sống yên ổn, không bị người khác làm phiền hay quấy nhiễu.
yên tĩnh|Ít hoặc không có tiếng động gây xáo trộn.
yên trí|Tin chắc, không còn nghi ngờ gì nữa.
yên vị|Đã ổn định, an toàn và không di chuyển khỏi vị trí hiện tại.
yên vui|Bình an và sung sướng trong tâm hồn.
yến mạch|Loại lúa nhỏ, hạt dùng làm thức ăn cho gia súc.
yến sào|Tổ của chim yến, được thu để chế biến thực phẩm.
yến tiệc|Cuộc ăn uống trang trọng với nhiều món ăn, đồ uống để chiêu đãi khách quý.
yết giá|Công bố mức giá của hàng hóa ra công chúng.
yết hầu|Ống dẫn khí nằm ở phía trước cổ họng, dùng để thở.
yết thị|Bản tin được dán công khai để mọi người cùng biết.
yêu cầu|Sự bắt buộc người khác phải làm việc gì đó.
yêu chuộng|Thích và thể hiện sự quý trọng hơn những thứ khác.
yêu đời|Luôn vui vẻ, tin tưởng và yêu thích cuộc sống.
yêu kiều|Dáng vẻ xinh đẹp, mềm mại của người phụ nữ.
yêu mến|Cảm thấy quý trọng và muốn ở bên cạnh người hoặc vật mình yêu thích.
yêu thích|Cảm thấy vui và muốn dành nhiều tình cảm cho người hay việc.
yêu thương|Yêu mến, quan tâm chăm sóc hết lòng.
yếu lược|Tóm gọn những điểm cốt lõi cần thiết nhất.
yếu ớt|Sức lực hoặc hiệu quả rất nhỏ, gần như không có.
yếu thế|Tình trạng gặp khó khăn, bất lợi hoặc thua thiệt.
yếu tố|Thành phần cấu tạo nên một sự vật, sự việc hoặc hiện tượng.
```
