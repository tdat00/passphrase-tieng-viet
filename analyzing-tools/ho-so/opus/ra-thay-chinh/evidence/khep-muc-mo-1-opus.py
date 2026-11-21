"""Phiếu của Opus cho các mục mở (khép mục mở 1), đối chiếu từng dòng phiếu của Astra.

    python khep-muc-mo-1-opus.py  ->  ../khep-muc-mo-1-opus.tsv

Đầu vào chỉ đọc: ho-so/astra/ra-thay-chinh/khep-muc-mo-1.tsv (286 dòng). Mỗi dòng của Astra có một dòng tương ứng.
- y_opus: DONG_Y hoặc KHONG_DONG_Y (kèm hướng của Opus).
- ky_opus: Y trên dòng giữ K2 là chữ ký "không tự động chặn" của SA-Opus cho đúng khóa và mọi đối chứng ghi ở dòng
  Astra; Y trên dòng không đỏ, khác từ, qua là đồng ý giữ; N là không ký để giữ (đồng ý thay hoặc không nhận vào).
Lý do riêng cho các dòng Astra đề nghị thay hoặc từ chối ký nằm trong RIENG; các dòng còn lại dùng lý do chung theo loại.
"""
import collections

from chung import *

A = AT / "ho-so" / "astra" / "ra-thay-chinh"
TC = "tieu-chi-thong-nhat.md"
QD = "ho-so/unified/ra-thay-chinh-ke-hoach.md (D-rtc-6)"
RIENG = {  # tu: (y_opus, ky_opus, ly_do, bang_chung thêm)
    "chậm": ("DONG_Y", "N", "Nhận K1: chàm là tên bệnh da (nhóm 5, như ngứa ngáy), r 0,058; nhất quán với nhồi/nhói, "
             "choàng/choáng", f"{TC}:147"),
    "cổng": ("DONG_Y", "N", "Nhận K1: còng là còng tay, bắt giữ (nhóm 2), r 0,096; nhất quán với việc chủ dự án cho thay "
             "thuần/thụ án, xuân/xử án", f"{TC}:144; {QD}"),
    "mặt nước": ("DONG_Y", "N", "Nhận K1: mất nước có nghĩa mất nước nhà (nhóm 3) và mất nước cơ thể (nhóm 5); r 0,99",
                 f"{TC}:145, :147"),
    "thiếu": ("DONG_Y", "N", "Nhận K1: thiêu là đốt thi thể, thiêu sống (nhóm 4, 1), r 0,234; nhất quán với việc chủ dự "
              "án cho thay vòng/vong", f"{TC}:143, :146; {QD}"),
    "trán": ("DONG_Y", "N", "Nhận K1: trận là cách đọc rất tự nhiên (r 16,4) và có nghĩa trận đánh (nhóm 1) còn dùng "
             "phổ biến", f"{TC}:143"),
    "niêu": ("DONG_Y", "N", "Nhận K0: niệu có mục từ điển riêng nghĩa nước tiểu (chất thải); K0 áp bất kể tần suất và "
             "cho cả khóa một khối, dựa trên nguồn chứng thực toàn mục", f"{TC}:161, :163"),
    "cần cù": ("KHONG_DONG_Y: giữ K2", "Y", "Nghĩa chính của căn cứ là cơ sở, chỗ dựa (căn cứ vào); căn cứ quân sự là "
               "nơi đóng quân, cùng loại với các cách đọc quân sự chủ dự án đã cho giữ (tướng, phòng ngự, khiên). Opus "
               "ký K2", f"{QD}; ho-so/unified/ra-thay-chinh-cau-hoi.md tại 0253bb0"),
    "tiền lương": ("KHONG_DONG_Y: giữ K2", "Y", "Tiên lượng là dự đoán, kể cả trong y khoa; không phải tên bệnh, triệu "
                   "chứng hay thủ thuật như các ví dụ nhóm 5; r 0,167. Opus ký K2", f"{TC}:147"),
    "triệu": ("KHONG_DONG_Y: giữ K2", "Y", "Triều (triều đình, triều đại; cũng là thủy triều) là từ hoàng gia như ngai, "
              "trẫm mà chủ dự án đã cho giữ; r 0,092. Opus ký K2", f"{TC}:145; {QD}"),
    "bạn thân": ("KHONG_DONG_Y: giữ K2", "Y", "Nghĩa chính của bán thân là nửa người (tượng bán thân); nghĩa mại dâm là "
                 "nghĩa phụ, Astra thấy ít nhất 3 trong 38 dòng phụ đề đọc. Cả chuỗi bán thân chỉ bằng 0,050 lần bạn "
                 "thân; chưa có nguồn từ điển cho nghĩa tình dục nên không thuộc K0 (TC:162–163). Bạn thân là từ cốt "
                 "lõi. Opus ký K2", f"{TC}:148, :162–163; ho-so/astra/ra-thay-chinh/evidence/km1-ban-than-id.tsv"),
    "chun": ("DONG_Y", "N", "Nhận phép cận của Astra cho nghĩa dây đàn hồi: thun ≤ 101/108 ở phụ đề, chun ≤ 515/543 ở "
             "web, đều dưới 95%, nên không dạng nào đạt loại c ở cả hai kho; thay cả chun và thun", f"{TC}:124, :126"),
    "thun": ("DONG_Y", "N", "Như dòng chun/thun", f"{TC}:124, :126"),
    "tép riu": ("DONG_Y", "N", "Nhận: nguồn ghi tép diu tương ứng tép riu ở cả hai nghĩa nên là loại c; web 0 + 0 < 20 "
                "lượt, thiếu dữ liệu, loại", f"{TC}:124"),
    "lằng nhằng": ("DONG_Y", "N", "Từ đã ra vì H7 K1; khép dòng H5 bằng mã đó, không ghi QUA H5", "ho-so/unified/ra-thay-chinh-h7.tsv"),
    "xà bông": ("DONG_Y", "N", "Từ đã ra theo H5f (T-rtc-9); khép dòng này bằng mã đó", "ho-so/unified/ra-thay-chinh-ke-hoach.md (T-rtc-9)"),
    "qua quýt": ("DONG_Y", "N", "Mục dự phòng, không vào: họ c chưa qua", "ho-so/unified/ra-thay-chinh-thay-the.tsv"),
    "làm cỗ": ("DONG_Y", "N", "Nhận không cho vào: làm cỏ có nghĩa tàn sát trong hai nguồn; 4/6 mẫu phụ đề sạch rõ nghĩa "
               "bạo lực", f"{TC}:143"),
    "rướn": ("DONG_Y", "N", "Nhận không cho vào: dướn dẫn về rướn nên là loại c; phụ đề 14 + 0, web 5 + 0, đều dưới 20 "
             "lượt", f"{TC}:124"),
    "khác": ("DONG_Y", "Y", "Đồng ý cách đọc khác không thuộc nhóm đỏ (Opus từng xếp K2, nay nhận không đỏ)", "-"),
}
CHUNG = {
    ("K2", "Y"): "Đồng ý giữ. Opus ký K2 không tự động chặn cho khóa này, cùng phạm vi đối chứng ghi ở phiếu Astra",
    ("H7_CHO", "GIU_K2"): "Đồng ý giữ. Opus ký K2 không tự động chặn, cùng phạm vi đối chứng ghi ở phiếu Astra",
    ("H7_CHO", "GIU_KHONG_DO"): "Đồng ý cách đọc khác không thuộc nhóm đỏ (không tự động chặn)",
    ("H5_CHO", "Y"): "Đồng ý giữ: khác từ hay qua theo số; không có phản đối hợp lệ",
    ("CO_TU_VAO", "GIU_K2"): "Đồng ý giữ. Opus ký K2 không tự động chặn cho cờ này",
    ("CO_TU_VAO", "GIU_KHAC_TU"): "Đồng ý đóng cờ: dạng đối chứng là từ khác",
    ("CO_TU_VAO", "GIU_KHONG_DO"): "Đồng ý đóng cờ: cách đọc khác không thuộc nhóm đỏ",
}


def ten(o):
    return o.split(" (")[0].split(" / ")[0].strip()


def main():
    out_utf8()
    rows = []
    dem = collections.Counter()
    for i, r in enumerate(rd(A / "khep-muc-mo-1.tsv"), 2):
        w, loai, de = ten(r["tu_hoac_khoa"]), r["loai"], r["de_xuat_astra"]
        nguon = f"ho-so/astra/ra-thay-chinh/khep-muc-mo-1.tsv:{i}"
        if w in RIENG and (r["ky_astra"] == "N" or w == "khác"):
            y, ky, ly, bc = RIENG[w]
            bc = f"{nguon}; {bc}" if bc != "-" else nguon
        else:
            k = (loai, "Y") if loai in ("K2", "H5_CHO") else (loai, de)
            if k not in CHUNG or r["ky_astra"] != "Y":
                raise SystemExit(f"Thiếu lý do cho dòng {i}: {loai} {w} {de} {r['ky_astra']}")
            y, ky, ly, bc = "DONG_Y", "Y", CHUNG[k], nguon
        dem[(loai, y.split(":")[0], ky)] += 1
        rows.append({"loai": loai, "tu_hoac_khoa": r["tu_hoac_khoa"], "de_xuat_astra": de, "y_opus": y,
                     "ky_opus": ky, "ly_do": ly, "bang_chung": bc})
    write_tsv(OUT / "khep-muc-mo-1-opus.tsv", list(rows[0].keys()), rows)
    for k, v in sorted(dem.items()):
        print(k, v)
    print("tổng", len(rows), "chữ ký Y:", sum(r["ky_opus"] == "Y" for r in rows))


if __name__ == "__main__":
    main()
