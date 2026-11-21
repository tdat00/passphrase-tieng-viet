# Hồ sơ làm việc

Bản lưu trong repo của hồ sơ làm việc mà hai tác tử Opus và Astra dùng khi xây danh sách thống nhất (401 tệp, khoảng 37 MB). Các tài liệu [`WordListAnalyze.md`](../../WordListAnalyze.md), [`WordListAnalyze-Opus.md`](../../WordListAnalyze-Opus.md), [`WordListAnalyze-Astra.md`](../../WordListAnalyze-Astra.md) và [`tieu-chi-thong-nhat.md`](../tieu-chi-thong-nhat.md) link tới các tệp ở đây.

| Thư mục | Nội dung |
|---|---|
| [`discussion/`](discussion/) | Phản hồi, soát xét giữa hai bên; bảng khóa chung P1; bảng 84 cặp chính tả ban đầu |
| [`unified/`](unified/) | Đầu ra P1–P7: kết quả cổng, phiếu chấm, chữ ký, phản biện, xếp hạng, danh sách, khấu trừ, log D6, phiếu soát nghĩa, bài nộp lượt riêng v4, kịch bản C13; tin nhắn giữa hai bên ở [`trao-doi/`](unified/trao-doi/). Các tệp `du-phong-v2-*`: báo cáo chung, kế hoạch, câu hỏi và hai bảng nháp của đợt phân tích dự phòng v2 (WordListAnalyze.md mục 11–12) |
| [`opus/`](opus/), [`astra/`](astra/) | Script và phiếu riêng của từng bên được nhắc tới trong tài liệu; thư mục con `du-phong-v2/` chứa phân tích, review chéo và chứng cứ của từng bên trong đợt dự phòng v2 |

Trong tin nhắn và tài liệu lưu trữ, kí hiệu `U\` nghĩa là [`unified/`](unified/), `D\` nghĩa là [`discussion/`](discussion/), `files\opus\…`, `files\astra\…` nghĩa là [`opus/`](opus/), [`astra/`](astra/).

## Không lưu vào repo

- Văn bản các kho ngữ liệu (OpenSubtitles, CCAligned, Leipzig, Tatoeba), danh sách từ Hồ Ngọc Đức (GPL), dump Wiktionary; mọi tệp chứa câu trích từ các kho này (mẫu ngữ cảnh, căn cứ đọc kiểm).
- Bài nộp các lượt viết giải nghĩa v1–v3: có các câu không đạt D6 (quá gần nguồn tham chiếu). Hash từng câu được phát hành nằm ở [`../nguon-goc-giai-nghia.tsv`](../nguon-goc-giai-nghia.tsv).
- Các tệp trung gian không được tài liệu nhắc tới.

## Tệp đã lược hoặc sửa

SHA-256 ghi trong tài liệu là của tệp gốc. Các tệp dưới đây khác tệp gốc:

| Tệp | Thay đổi | SHA-256 gốc | SHA-256 bản lưu |
|---|---|---|---|
| [`astra/publish.py`](astra/publish.py) | đổi đường dẫn tuyệt đối thành tương đối | `b12976c14ffb08eb34fc98080cadc37c4ab17e3587b6c5be7b78f8d7511696cd` | `a556ab92207a9e68cbdacbed93f63c8b530cc072bddc84efbbd126b84aba5adf` |
| [`opus/h5/recount_h5.py`](opus/h5/recount_h5.py) | đường dẫn kho đọc từ biến môi trường CORPUS_DIR | `0c62776ef978e8b556e910470a2681765024f0bd7e650c5e242842a3ae28d0a3` | `d2cbb6fca45f86c3ba5de74a4b31f96858986f5bf8e09d30c40cd0a1f4b2db29` |
| [`opus/p4/p6_opus.py`](opus/p4/p6_opus.py) | đổi đường dẫn tuyệt đối thành tương đối | `7a332e942e0fc918a304beb5e1ac607cc93e35193303c3637e8ba7540b20dd3b` | `24a5f314c3141703d77e746e1975148b543da73c113060d9ea4d3ed39dbf5d81` |
| [`opus/p4/sau_h9.py`](opus/p4/sau_h9.py) | đổi đường dẫn tuyệt đối thành tương đối | `688bb36548377e2c5ed104251287dc1c43c350408b9b99e6609f1e841c6135ad` | `680b31e510f71906fafc02348dffd21629841264163ee4491227926e19ba9b63` |
| [`unified/chu-ky.tsv`](unified/chu-ky.tsv) | lược 42 đoạn trích kho văn bản trong «…» | `2437fbd98b722ce073bc8a2354afb239c2c0bce165ca02c652c7a1ee8f948ae6` | `23715db2b49c5c696f9d6fc128f8895ec80323a08a88b85aac45d8e5f51330d2` |
| [`unified/d6-tham-chieu.json`](unified/d6-tham-chieu.json) | đổi đường dẫn tuyệt đối thành tương đối | `9cfa4ba6dbe49820651f6ad048c7c18ba1fd5593bde12788467be1c6277bd7c7` | `6d6ed522921a00ec90dd4da98984651f8cc3199660848e7a80a6a57469192303` |
| [`unified/hieu-chinh-opus.tsv`](unified/hieu-chinh-opus.tsv) | lược 4 đoạn trích kho văn bản | `bc7491ff6b0ab4b65b3e4aec35d1c33ef725faeee0933cdd2c3aa99b5c6a6143` | `2eeb7604426e5283682ba572487fa74139c103128ae6395607c26277c3185f5e` |
| [`unified/p7-v3-hien-hanh-astra.tsv`](unified/p7-v3-hien-hanh-astra.tsv) | lược 123 câu không đạt D6 | `a8f55b2fb0a2a23401d00fccecfb69545366096f52468c1baa89f3fc971a2a8c` | `201bf8129584ef0221364781ae9efdadd8cb821a10595f2bf732155990c4155e` |
| [`unified/p7-v4-rieng-hien-hanh-astra.tsv`](unified/p7-v4-rieng-hien-hanh-astra.tsv) | lược 122 câu không đạt D6 | `f028b8dbd203a02047c14e3ac8f6e4cab8f933a3c26a852b19c248ee7f865a09` | `79deb45bd1d23aba8eadbaf8a6cba93e589b2124e9b77e272de78b7e4d917809` |
| [`unified/trao-doi/032-opus-den-astra.md`](unified/trao-doi/032-opus-den-astra.md) | lược 1 câu phụ đề | `e6a0c255dc20402e10a1d164176f62f5cd6885c1e111f20ee97c4461024473b2` | `84f4bb5eb41862bdb82be204041c7cc2cfefa680edc7e7870d06a01b027ba025` |
| [`unified/trao-doi/034-opus-den-astra.md`](unified/trao-doi/034-opus-den-astra.md) | đổi đường dẫn tuyệt đối thành đường dẫn trong repo | `110ab25e43bc9a65b32dc7b5af14629420bec993ae8e2aa5a106581f8bc4668e` | `ac5284aba7f3c6a717afda2e9d34ae81b62a9fc521568d18673444aefc6af1d4` |
