"""Đo hai kho ghim bằng bộ km1; đổi tên đầu ra và seed. Không lưu văn bản kho."""
import importlib.util
import sys
from pathlib import Path

EV = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("rtc_meter", EV / "km1-mau.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.SEED = "rtc-hm-astra-20261122"
m.FORMS = ("cơ quan|lực lượng|cô quân|cố quận|biển|biễn|biến|bí mật|bỉ mặt|mưa dông|tàu điện|tầu điện|"
           "chỗ ngồi|chổ ngồi|bày tỏ|bầy tỏ|bày tõ|chuyển đổi|chuyễn đổi|chuyển đỗi|chuyễn đỗi|cụ thể|cụ thễ|"
           "côn trùng|côn trùn|vạn hạnh|hạnh|chia|chía|chĩa|chỉa|thia|ngắn gọn|ngá ngởn|ngả ngốn|ngả ngớn|"
           "tương dương|mịnh|chế tạo|tương đương|giảng viên").split("|")
m.SAMPLE = set("cơ quan|lực lượng|biến|vạn hạnh|bỉ mặt|chỉa|chĩa|ngả ngốn|ngả ngớn|ngá ngởn|tầu điện".split("|"))
old = m.save


def save(name, header, rows):
    if "day-" not in name:
        old(name.replace("km1-", "hm1-", 1), header, rows)


m.save = save
if __name__ == "__main__":
    m.main()
