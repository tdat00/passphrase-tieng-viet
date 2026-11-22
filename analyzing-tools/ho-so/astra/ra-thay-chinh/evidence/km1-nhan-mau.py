"""Mã Astra đã gán khi đọc cửa sổ trong RAM, theo thứ tự băm nhỏ nhất. Không chép nguồn."""
import csv
import io
from pathlib import Path

EV = Path(__file__).resolve().parent
LABELS = {
    "bán thân": ("MO_HO BAN_MINH BAN_MINH BAN_MINH BAN_MINH MO_HO", "MO_HO NUA_NGUOI NUA_NGUOI MO_HO NUA_NGUOI NUA_NGUOI"),
    "báng": ("PHAN_SUNG PHAN_SUNG PHAN_SUNG PHAN_SUNG PHAN_SUNG NHAM_CHU", "TAY_CAM MO_HO PHAN_SUNG TAY_CAM TAY_CAM TAY_CAM"),
    "chun": ("TEN TEN TEN TEN TEN TEN", "TEN TEN TEN TEN TEN TEN"),
    "chàm": ("THANH_NGU THANH_NGU THANH_NGU THANH_NGU THANH_NGU THANH_NGU", "BENH DIA_DANH MAU BENH MAU MAU"),
    "chăn dắt": ("CHAN_NUOI MO_HO TON_GIAO DAN_DAT MO_HO BOC_LOT_NGUOI", "DAN_DAT TON_GIAO TON_GIAO TON_GIAO TON_GIAO TON_GIAO"),
    "chầu": ("UYEN_NGU_CUM BUOI BUOI BUOI UYEN_NGU_CUM BUOI", "NGHI_LE MO_HO MO_HO TON_GIAO TRIEU_DINH NGHI_LE"),
    "cuồng": ("CUM_DAI CUM_DAI DAM_ME DAM_ME DAM_ME DAM_ME", "DAM_ME DAM_ME DAM_ME DAM_ME DAM_ME DAM_ME"),
    "còng": ("BAT_GIU BAT_GIU BAT_GIU BAT_GIU BAT_GIU BAT_GIU", "KHOA_KIM_KHI MO_HO KIM_KHI KIM_KHI MO_HO KIM_KHI"),
    "căn cứ": ("CO_SO_DIA_DIEM LIEN_LAC_DON_VI CO_SO_DIA_DIEM NGHIEN_CUU QUAN_SU CO_SO_DIA_DIEM", "CO_SO_LY_LE CO_SO_LY_LE MO_HO MO_HO MO_HO CO_SO_DIA_DIEM"),
    "dun": ("TEN TUONG_THANH TEN TUONG_THANH TEN TUONG_THANH", "NHAM_CHU TEN NHAM_CHU TU_VAY TEN MO_HO"),
    "làm cỏ": ("BAO_LUC LAM_VUON BAO_LUC BAO_LUC BAO_LUC LAM_VUON", "MO_HO LAM_VUON LAM_VUON LAM_VUON MO_HO LAM_VUON"),
    "mất nước": ("CO_THE CO_THE CO_THE CO_THE CO_THE CO_THE", "THUC_PHAM THUC_PHAM MO_HO THUC_PHAM CO_THE THUC_PHAM"),
    "nòng": ("CO_NONG MO_HO PHAN_SUNG PHAN_SUNG PHAN_SUNG PHAN_SUNG", "CO_NONG CO_NONG PHAN_SUNG THE_THAO KY_THUAT THE_THAO"),
    "sanh": ("NHAM_CHU SINH_NO TON_GIAO TEN TEN SINH_NO", "DIA_DANH TON_GIAO SINH_NO TON_GIAO DIA_DANH TON_GIAO"),
    "thiêu": ("BAO_LUC DOT BAO_LUC DOT BAO_LUC TAN_PHA", "KY_THUAT KY_THUAT KY_THUAT KY_THUAT KY_THUAT KY_THUAT"),
    "thun": ("VAI MO_HO VAI MO_HO NGHIA_KHAC DAN_HOI", "VAI DAN_HOI VAI MO_HO TEN VAI"),
    "tiên lượng": ("THIEU_CANH THIEU_CANH LAM_SANG DU_DOAN LAM_SANG THIEU_CANH", "LAM_SANG LAM_SANG DU_DOAN_SONG LAM_SANG LAM_SANG THIEU_CANH"),
    "truồng": ("KHOA_THAN KHOA_THAN KHOA_THAN KHOA_THAN KHOA_THAN KHOA_THAN", "KHOA_THAN KHOA_THAN NGU_CANH_NGUOI_LON KHOA_THAN KHOA_THAN NHAM_CHU"),
    "tịch": ("TEN THANH_NGU TEN TEN TEN TEN", "QUOC_TICH NHAM_CHU QUOC_TICH NHAM_CHU QUOC_TICH TEN"),
    "đình": ("TEN THANH_NGU NHA_LANG NHA_LANG NHAM_CHU MO_HO", "TEN DIA_DANH MO_HO DIA_DANH DINH_GIA_DINH DINH_GIA_DINH"),
}
WEB_PROVED = set(map(int, """410202 419504 441476 598679 983026 1276021 1380287 1423640 2199881 2720039 2853662 2995512 3536156 3723175 3898948 3948705 4798683 5417734 5833305 5861031 5907102 6222986 6240913 6311440 7030066 7306168 8928466 9424576""".split()))
SUB_PROVED = {1324148, 1904147, 1904149, 1904152, 3580644, 4116931, 4116932}


def rows(path):
    with (EV / path).open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def save(name, table):
    b = io.StringIO()
    writer = csv.writer(b, delimiter="\t", lineterminator="\r\n")
    writer.writerow(("phep", "kho", "tu", "id_dong", "i_token", "blake2b128_dong", "nhan_Astra"))
    writer.writerows(table)
    (EV / name).write_bytes(b.getvalue().encode("utf-8"))


def main():
    out, proof = [], []
    for k, s in enumerate(("sub", "web")):
        cards = rows(f"km1-h7-mau-{s}.tsv")
        assert {r["tu"] for r in cards} == set(LABELS)
        for w, labels in LABELS.items():
            rs = [r for r in cards if r["tu"] == w]
            for r, label in zip(rs, labels[k].split(), strict=True):
                out.append(("H7", s, w, r["id_dong"], r["i_token"], r["blake2b128_dong"], label))
        for r in rows(f"km1-mau-{s}.tsv"):
            if r["tu"] in {"chun", "thun"}:
                label = "TEN" if r["tu"] == "chun" else "VAI"
                out.append(("H5e", s, r["tu"], r["id_dong"], r["i_token"], r["blake2b128_dong"], label))
        cards = rows("km1-can-day-web.tsv" if k else "km1-day-sub.tsv")
        kept = set()
        for r in cards:
            n = int(r["id_dong"])
            if n in (WEB_PROVED if k else SUB_PROVED) and n not in kept:
                kept.add(n)
                proof.append(("CAN_DUOI_H5e", s, "thun" if k else "chun", n, r["i_token"], r["blake2b128_dong"], "DAY_DAN_HOI"))
        assert len(kept) == (28 if k else 7)
    save("km1-nhan-mau.tsv", out)
    save("km1-can-da-doc.tsv", proof)
    assert 20*515 < 19*(515+28) and 20*101 < 19*(101+7) and 20*87 < 19*(87+7)


if __name__ == "__main__":
    main()
