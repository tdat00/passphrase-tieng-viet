"""Phiếu D7 của SA-Opus cho lượt viết lại cuối rtc-v3 (9 mục qua D6; khách hàng trượt D6 lần ba, không soát).

Phán quyết là của người soát; script chỉ ghi phiếu và đo tỉ số gần trùng (đầu mục và tỉ số, không ghi câu).

Chạy (từ thư mục evidence):
    set RTC_DIR=<ngoài repo: thư mục chứa rtc-v1, rtc-v2, rtc-v3>
    python -X utf8 -B d7-rtc-v3.py  ->  ../d7-rtc-v3.tsv, d7-rtc-v3-gan-trung.tsv
"""
import difflib
import os
import re
import unicodedata
from pathlib import Path

from chung import AT, HERE, OUT, U, out_utf8, rd, write_tsv

out_utf8()
SRC = Path(os.environ["RTC_DIR"])
VIET_LAI = {}  # không có mục nào
CO = {"sớm tối": "GIU_HAI_NGHIA"}

phieu = [r for r in rd(SRC / "rtc-v3" / "d7-chung.tsv") if r["tu"] != "khách hàng"]
assert len(phieu) == 9
rows = []
for r in phieu:
    w = r["tu"]
    assert not r["co"] or w in CO, w
    if w in VIET_LAI:
        rows.append({"tu": w, "ket_qua": "VIET_LAI", "ma": VIET_LAI[w][0], "chan_doan": VIET_LAI[w][1]})
    else:
        rows.append({"tu": w, "ket_qua": "DAT", "ma": CO.get(w, "-"), "chan_doan": ""})
write_tsv(OUT / "d7-rtc-v3.tsv", ["tu", "ket_qua", "ma", "chan_doan"], rows)

tok = lambda s: re.findall(r"\w+", unicodedata.normalize("NFC", s.lower()))
ra = {r["tu"] for r in rd(U / "ra-thay-chinh-thay-the.tsv") if r["vai_tro"] == "RA"}
pool = {}
for l in open(AT / "wordlist.txt", encoding="utf-8"):
    w, g = l.rstrip("\n").split("|", 1)
    if w not in ra:
        pool[w] = g
for luot in ("rtc-v1", "rtc-v2", "rtc-v3"):
    pool.update({r["tu"]: r["giai_nghia"] for r in rd(SRC / luot / "lo-01.tsv")})
ev = []
for r in phieu:
    w = r["tu"]
    s, x = max((difflib.SequenceMatcher(None, tok(pool[w]), tok(g), autojunk=False).ratio(), x) for x, g in pool.items() if x != w)
    ev.append({"tu": w, "gan_nhat": x, "ti_so": f"{s:.2f}"})
write_tsv(HERE / "d7-rtc-v3-gan-trung.tsv", ["tu", "gan_nhat", "ti_so"], ev)
print(f"DAT {sum(r['ket_qua'] == 'DAT' for r in rows)}, VIET_LAI {len(VIET_LAI)}; "
      "tỉ số gần trùng lớn nhất: " + ", ".join(f"{e['tu']}~{e['gan_nhat']} {e['ti_so']}" for e in ev if float(e["ti_so"]) >= 0.5))
