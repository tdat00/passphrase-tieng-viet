"""Phiếu D7 của SA-Opus cho lượt viết lại rtc-v2 (nửa của Opus, 30 mục) và phép đo gần trùng làm căn cứ.

Phán quyết là của người soát (bảng VIET_LAI, CO dưới đây); script chỉ ghi phiếu và đo tỉ số gần trùng (đầu mục và tỉ số,
không ghi câu giải nghĩa).

Chạy (từ thư mục evidence):
    set RTC_DIR=<ngoài repo: thư mục chứa rtc-v1\\lo-01.tsv, rtc-v2\\lo-01.tsv, rtc-v2\\d7-opus.tsv>
    python -X utf8 -B d7-rtc-v2.py  ->  ../d7-rtc-v2.tsv, d7-rtc-v2-gan-trung.tsv
"""
import difflib
import os
import re
import unicodedata
from pathlib import Path

from chung import AT, HERE, OUT, U, out_utf8, rd, write_tsv

out_utf8()
SRC = Path(os.environ["RTC_DIR"])
VIET_LAI = {
    "sớm tối": ("HEP", "Vế nghĩa thứ hai thu về chuyện có mặt đều đặn, bỏ mất ý suốt ngày, liên tục mà cách dùng này "
                       "thường mang."),
}
CO = {}  # cờ được đóng mà vẫn DAT; lượt này cờ duy nhất (sớm tối) thuộc mục viết lại

phieu = rd(SRC / "rtc-v2" / "d7-opus.tsv")
assert len(phieu) == 30 and set(VIET_LAI) <= {r["tu"] for r in phieu}
rows = []
for r in phieu:
    w = r["tu"]
    if w in VIET_LAI:
        rows.append({"tu": w, "ket_qua": "VIET_LAI", "ma": VIET_LAI[w][0], "chan_doan": VIET_LAI[w][1]})
    else:
        assert not r["co"], w
        rows.append({"tu": w, "ket_qua": "DAT", "ma": CO.get(w, "-"), "chan_doan": ""})
write_tsv(OUT / "d7-rtc-v2.tsv", ["tu", "ket_qua", "ma", "chan_doan"], rows)

tok = lambda s: re.findall(r"\w+", unicodedata.normalize("NFC", s.lower()))
v2 = {r["tu"]: r["giai_nghia"] for r in rd(SRC / "rtc-v2" / "lo-01.tsv")}
ra = {r["tu"] for r in rd(U / "ra-thay-chinh-thay-the.tsv") if r["vai_tro"] == "RA"}
pool = {}
for l in open(AT / "wordlist.txt", encoding="utf-8"):
    w, g = l.rstrip("\n").split("|", 1)
    if w not in ra:
        pool[w] = g
pool.update({r["tu"]: r["giai_nghia"] for r in rd(SRC / "rtc-v1" / "lo-01.tsv") if r["tu"] not in v2})
pool.update(v2)
ev = []
for r in phieu:
    w = r["tu"]
    s, x = max((difflib.SequenceMatcher(None, tok(v2[w]), tok(g), autojunk=False).ratio(), x) for x, g in pool.items() if x != w)
    ev.append({"tu": w, "gan_nhat": x, "ti_so": f"{s:.2f}"})
write_tsv(HERE / "d7-rtc-v2-gan-trung.tsv", ["tu", "gan_nhat", "ti_so"], ev)
print(f"DAT {sum(r['ket_qua'] == 'DAT' for r in rows)}, VIET_LAI {len(VIET_LAI)}: {', '.join(VIET_LAI)}")
