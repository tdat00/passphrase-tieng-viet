# Rà và thay danh sách chính — yêu cầu

**Ngày:** 21/11/2026. **Nhánh:** `analyze/ra-thay-chinh`, tạo từ `main` tại `f404a95` (merge PR #1, dự phòng v2).

## Lời chủ dự án (nguyên văn)

> tôi đã merge plan v2 vào main, giờ hãy thực hiện tiếp các việc D-dpv2-5, T-dpv2-1. Báo cáo progress cho tôi qua discord

## Làm rõ (form `ask_user`, 21/11/2026)

| Câu hỏi | Trả lời của chủ dự án |
|---|---|
| Ý về "T-dpv2-1" (đã thực hiện ở PR #1) | Không có việc nào khác, chỉ D-dpv2-5 |
| Phạm vi D-dpv2-5 | Rà đầy đủ: họ chòng chành/tròng trành, báo tử, sàng lọc 632 cặp H5 + 1.177 cặp H7, thay từ chính nếu cần |
| Cho phép thay danh sách chính trong đợt này | Có, sau khi kế hoạch Final và chủ dự án duyệt; kèm giải nghĩa viết mới đạt D6/D7 |

## D-dpv2-5 (kế hoạch dự phòng v2, `analyzing-tools/ho-so/unified/du-phong-v2-ke-hoach.md` §9, §13)

Phát hiện ở danh sách chính (họ chòng chành/tròng trành, 632 cặp H5 thô, 1.177 cặp H7, báo tử) được chuyển sang một yêu cầu riêng để rà/thay danh sách chính, với P6/P7/phát hành riêng. Nếu đổi từ, phải cập nhật WordListAnalyze.md §11–§12, hai TSV công bố và manifest.

## Quy ước

Theo yêu cầu của chủ dự án ở đợt trước, không tạo thư mục tài liệu mới: hồ sơ riêng của từng SA ở `analyzing-tools/ho-so/{opus,astra}/ra-thay-chinh/`, hồ sơ chung ở `analyzing-tools/ho-so/unified/ra-thay-chinh-*`; kết quả cuối cập nhật thẳng vào tài liệu có sẵn.
