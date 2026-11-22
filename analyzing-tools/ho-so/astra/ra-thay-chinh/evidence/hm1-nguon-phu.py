"""Đo băm các trang bổ trợ; không lưu nội dung hoặc lời từ điển."""
import hashlib
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from screen_core import EV, save_tsv

URLS = {
    "vận hành": ("https://phatgiao.org.vn/tu-dien-phat-hoc-online/van-hanh-k68088.html", "THUAT_NGU_VA_TEN_RIENG"),
    "lực lượng": ("https://tudientiengviet.org/luc-luong/", "SUC_MANH_HOAC_TAP_HOP_NGUOI_KHONG_DONG_NHAT_QUAN_LUC"),
    "chỗ ngồi": ("https://nghengu.vn/tieng-nghe-cua-toi/cho-ngoi-hay-cho-ngoi-2038.html", "LOI_CHINH_TA_CHO_NGOI"),
    "tàu điện": ("https://nghengu.vn/tieng-nghe-cua-toi/tau-bay-hay-tau-bay-2193.html", "TAU_TAU_BIEN_THE_PHUONG_NGU_CUA_TIENG_NGUYEN"),
    "bày tỏ": ("https://tudientiengviet.org/bay-to/", "MUC_DUNG_BAY_TO"),
    "chia": ("https://vdict.com/thia,3,0,0.html", "THIA_TEN_CA_KHAC_TU"),
    "bí mật": ("https://vdict.com/" + urllib.parse.quote("bỉ mặt") + ",3,0,0.html", "H6_9_DO_NGHIA_NGUYEN_MUC"),
    "ngắn gọn": ("https://vdict.com/" + urllib.parse.quote("ngả ngớn") + ",3,0,0.html", "THAI_DO_THIEU_DUNG_DAN_KHONG_MAC_DINH_K0"),
}


def fetch(w):
    url, tag = URLS[w]
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "VietnameseWordlistReview/1.0"}), timeout=20) as r:
            digest = hashlib.sha256(r.read()).hexdigest()
        state = "HTTP_200_DA_BAM"
    except OSError as exc:
        digest, state = "-", f"DA_DOC_QUA_WEB; KHONG_BAM_HTTP:{type(exc).__name__}"
    return dict(tu=w, url=url, sha256_http=digest, trang_thai=state, nhan_Astra=tag)


if __name__ == "__main__":
    with ThreadPoolExecutor(4) as ex:
        save_tsv(EV / "hm1-nguon-phu.tsv", list(ex.map(fetch, URLS)))
