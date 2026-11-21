"""Ghim URL, nhãn quan sát và băm; không xuất HTML, lời từ điển hoặc câu báo."""
import csv
import hashlib
import io
import re
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

EV = Path(__file__).resolve().parent
VD = "https://vdict.com/"
SH = "http://tratu.soha.vn/dict/vn_vn/"
SOURCES = {
    **{"VDict:" + w: (VD + urllib.parse.quote(w) + ",3,0,0.html", note) for w, note in {
        "ăn bĩnh": "CO_MUC_CO_BAC_KHONG_PHAI_CHAT_THAI", "niệu": "DANH_TU_CHAT_THAI_VA_YEU_TO_GHEP",
        "tinh tử": "THUAT_NGU_SINH_HOC", "tép diu": "DAN_TEP_RIU", "bản hiệu": "KHONG_TIM_THAY",
        "bội phát": "THUAT_NGU_RIENG", "lòng dòng": "KHONG_TIM_THAY", "ọt ẹt": "TU_TUONG_THANH",
        "giu giú": "GAN_NGHIA_KHONG_GHI_BIEN_THE", "xành xạch": "TU_TUONG_THANH",
    }.items()},
    **{"SOHA:" + w: (SH + urllib.parse.quote(w.capitalize().replace(" ", "_")), c) for w, c in {
        "rỡn": "XEM_GION", "dướn": "XEM_RUON", "thư giãn": "XEM_THU_DAN",
    }.items()},
    "ZIM": ("https://dictionary.zim.vn/viet-anh/xoan-xoat-tieng-anh-la-gi", "CHI_MUC_TIM_KIEM_GHI_TU_TUONG_THANH; TRANG_TRUC_TIEP_CHAN_JS"),
    "BVNTL": ("https://benhviennamthanglong.vn/ghen-mat-la-gi/", "DICH_TIET_MAT_BINH_THUONG_CUNG_CO_THE_DI_KEM_BENH"),
    "Han:尿": ("https://hvdic.thivien.net/whv/%E5%B0%BF", "DOI_CHIEU_HAN_VIET_KHONG_THAY_NGUON_NGUYEN_MUC_VIET"),
    "NUOT": ("https://nghiencuulichsu.com/2026/08/16/hien-tuong-luong-kha-trong-tieng-viet/", "NGUON_PHU_QUAN_HE_CH_TR; KEM_HAI_MUC_TU_VV_30K"),
    "DIEM_NHAN": ("https://baolamdong.vn/net-dep-nghi-thuc-khai-quang-diem-nhan-lan-su-rong-dau-nam-424239.html", "CO_DUNG_CUM_TRONG_NGHI_THUC"),
    "ONG_THO": ("https://www.decathlon.vn/p/" + urllib.parse.quote("ống-thở-lặn-biển-người-lớn-có-van-100-xanh-ngọc-decathlon-9002855.html"), "DUNG_CU_LAN_KHONG_CHI_Y_TE"),
    "KHUY": ("https://nghengu.vn/tieng-nghe-cua-toi/khuy-goi-hay-khuyu-goi-2079.html", "DANG_KHUY_CHI_DONG_TAC"),
    "VDict:làm khổ": (VD + urllib.parse.quote("làm khổ") + ",3,0,0.html", "PHAM_VI_RONG_HON_BAO_LUC"),
    "VDict:thay lòng": (VD + urllib.parse.quote("thay lòng") + ",3,0,0.html", "THAY_DOI_TINH_CAM_Y_DINH"),
}


def fetch(item):
    name, (url, note) = item
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "VietnameseWordlistReview/1.0"}), timeout=12) as r:
            data = r.read()
        if re.search(rb"Checking if the site connection is secure|cf-chl-", data[:10000]):
            return name, url, note, "-", "KHONG_BAM_TRANG_CHAN"
        return name, url, note, hashlib.sha256(data).hexdigest(), "HTTP_200; BAM_PHAN_HOI"
    except Exception as exc:
        return name, url, note, "-", f"KHONG_BAM; {type(exc).__name__}"


def main():
    buf = io.StringIO()
    wr = csv.writer(buf, delimiter="\t", lineterminator="\r\n")
    wr.writerow(("ma", "url", "nhan_kiem", "sha256_http", "trang_thai"))
    path = EV / "km1-web.tsv"
    old = {}
    if path.exists():
        with path.open(encoding="utf-8") as f:
            for name, url, note, digest, status in list(csv.reader(f, delimiter="\t"))[1:]:
                if SOURCES.get(name) == (url, note) and digest != "-":
                    old[name] = (name, url, note, digest, status)
    with ThreadPoolExecutor(4) as pool:
        old.update((row[0], row) for row in pool.map(fetch, (s for s in SOURCES.items() if s[0] not in old)))
    wr.writerows(old[name] for name in SOURCES)
    path.write_bytes(buf.getvalue().encode("utf-8"))


if __name__ == "__main__":
    main()
