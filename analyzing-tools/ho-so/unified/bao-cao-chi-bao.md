# Báo cáo chỉ báo M1–M5 (P6)

*Lập bởi Opus ngày 19/11/2026, tính trên `danh-sach-chon.txt` (SHA-256 `dfcf4ba6…73d4ee`). Chương trình độc lập của Astra phải cho cùng giá trị (xác nhận ở `_done\P6-astra.flag`).*

Chỉ báo chỉ để báo cáo. Trọng số S3 đã đóng băng sau P3, không chỉnh theo chỉ báo, và không lấy từ hiếm để đạt mục tiêu (mục 3 của bộ tiêu chí).

| # | Chỉ báo | Mục tiêu | Giá trị | Đạt |
|---|---|---|---|---|
| M1 | Tỉ lệ C+H trên mẫu thẩm định 300 mục | ≥ 60% | **78,7%** (236/300); khoảng 221–274 (73,7%–91,3%) | Có |
| M2 | Số mục 3 khối | ≤ 4% | **264** (3,40%) | Có |
| M3 | Độ dài trung bình khi viết liền | ≤ 7,0 chữ | **6,80** (52.845/7.776) | Có |
| M4 | Ngoại lệ H8 (cả bốn kho đều 0 lượt) | ≤ 1% | **0** | Có |
| M5 | Số mục nhiều nhất có cùng âm tiết đầu | báo cáo | **59** (*bánh*) | — |

## M1: mẫu thẩm định

- **Cách lấy mẫu:** 300 khóa của danh sách chính có SHA-256 nhỏ nhất của chuỗi `Astra-Opus-M1-v1-20261119|` + khóa. SHA-256 của mẫu: `f93d615266af08e0743e133869186c82bbbaf2293d53e04ce9e9736c133a45a8`.
- **Lớp tác nghiệp trong mẫu:** C 105, H 131, K 63, F 1.
- **Khoảng 221–274:**
  - cận dưới chỉ tính mục mà cả hai mã gốc (Opus, Astra) đều là C hoặc H;
  - cận trên tính mục có ít nhất một mã là C hoặc H;
  - có 56 mục mà hai mã gốc lệch nhau.

## Phân bố của danh sách chính (tham khảo)

- **Lớp:** C 2.988 · H 3.101 · K 1.610 · F 77.
- **Nhãn:** OK 7.776 (không có R1).
- **Số khối:** 1 khối 486 · 2 khối 7.026 · 3 khối 264.
- **Độ dài khi viết liền:**

  | Số chữ | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
  |---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
  | Số mục | 539 | 974 | 1.887 | 2.056 | 1.318 | 622 | 256 | 85 | 39 |

- **Âm tiết đầu thường gặp nhất:** *bánh* 59, *nhà* 57, *cá* 50, *máy* 44, *nước* 41, *đường* 36, *xe* 36, *làm* 35, *ăn* 34, *đồng* 30, *giấy* 29, *công* 28.
  - Không âm tiết nào vượt 0,8% danh sách.
  - Đa dạng chủ đề chỉ là chỉ báo, không có luật riêng (S4).
