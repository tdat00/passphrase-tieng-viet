"""Nhãn từng mẫu do SA-Astra đọc; ghép ID/băm, không sao chép câu nguồn."""
import csv

from screen_core import EV, save_tsv

MARKS = {
    "sub": {
        "biến": "THAY_DOI BIEN_MAT BIEN_MAT LOI_DUOI_CUM TAN_BIEN THAY_DOI",
        "chĩa": "PHAI_THEM_DOI_TUONG " * 6,
        "chỉa": "HUONG_VAT PHAI_THEM_DOI_TUONG PHAI_THEM_DOI_TUONG PHAI_THEM_DOI_TUONG TOC HUONG_VAO",
        "cơ quan": "CONG_QUYEN TO_CHUC_CHUNG CHAP_PHAP CHAP_PHAP CHUA_RO TO_CHUC_DAU_NAO",
        "lực lượng": "TAP_HOP CUM_PHONG_THU TAP_HOP CUM_KHANG_CHIEN CUM_DAN_QUAN NGUOI_DUOC_HUY_DONG",
        "ngả ngốn": "TU_THE",
        "tầu điện": "PHUONG_TIEN " * 4,
    },
    "web": {
        "biến": "KY_THUAT BIEN_SO THAY_DOI TUY_BIEN BIEN_MAT BIEN_MAT",
        "bỉ mặt": "CHE_BAI",
        "chĩa": "PHAI_THEM_DOI_TUONG TOC DANH_TU DUNG_CU HUONG_CAMERA HUONG_MUI",
        "chỉa": "NHIEM_CHU HUONG_ANG_TEN HUONG_CHAN HUONG_LONG_MI HUONG_LONG_MI",
        "cơ quan": "CO_QUAN_PHAP_LY CO_THE TO_CHUC_CHUNG DANG_NHA_NUOC CO_THE TO_CHUC_CHUNG",
        "lực lượng": "TAP_HOP CUM_KHONG_QUAN BAN_DICH_KY_THUAT CUM_VU_TRANG BAN_DICH_KY_THUAT CHUA_RO",
        "tầu điện": "PHUONG_TIEN " * 6,
        "vạn hạnh": "TEN_TRUONG DIA_CHI DIA_CHI TEN_THUONG_MAI TEN_CO_SO TEN_TRUONG",
    },
}
H8_ID = {
    "ngân hàng": 22794, "khách hàng": 22064, "cơ quan": 47995, "biển": 50278, "côn trùng": 35864,
    "cô giáo": 47431, "thay thế": 20845, "chỗ ngồi": 43502, "một mình": 1748, "bí mật": 15359,
    "mùa đông": 41932, "tàu điện": 225616, "cụ thể": 46405, "áp dụng": 76875, "vận hành": 87942,
    "việc làm": 42103, "chế tạo": 13130, "lực lượng": 52403, "chia": 53543, "bánh ngọt": 34373,
    "đánh răng": 42679, "xe điện": 231390, "bày tỏ": 60863, "chuyển đổi": 142938, "ngắn gọn": 71694,
    "mình": 18473, "tương đương": 55244, "giảng viên": 240680, "cởi mở": 163544, "vòi hoa sen": 267197,
}


def read(name):
    with (EV / name).open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main():
    rows = []
    for source, marks in MARKS.items():
        ids = read(f"hm1-h7-mau-{source}.tsv")
        assert {r["tu"] for r in ids} == set(marks)
        for w, text in marks.items():
            rs = [r for r in ids if r["tu"] == w]
            for r, mark in zip(rs, text.split(), strict=True):
                rows.append(dict(kho=source, **r, nhan_Astra=mark))
    save_tsv(EV / "hm1-mau-da-doc.tsv", rows)
    h8 = [dict(tu=r["tu"], kho="sub", id_dong=r["id_dong"], blake2b128_dong=r["blake2b128_dong"],
               nhan_Astra="DUNG_NGHIA_VIET", phep="H8_KHONG_SUY_TY_LE_NGHIA")
          for r in read("hm1-h8-id.tsv") if int(r["id_dong"]) == H8_ID.get(r["tu"])]
    assert len(h8) == len(H8_ID)
    save_tsv(EV / "hm1-h8-da-doc.tsv", h8)


if __name__ == "__main__":
    main()
