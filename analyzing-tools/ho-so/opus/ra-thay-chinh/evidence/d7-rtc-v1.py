"""Phiếu D7 của SA-Opus cho lượt viết sạch rtc-v1 (nửa của Opus, 66 mục) và phép đo gần trùng làm căn cứ.

Phán quyết là của người soát (bảng KET_QUA dưới đây); script chỉ ghi phiếu và đo độ gần trùng. Không ghi câu giải nghĩa
vào repo: tệp chứng cứ chỉ có đầu mục và tỉ số.

Chạy (từ thư mục evidence):
    set RTC_V1_DIR=<ngoài repo: thư mục có d7-opus.tsv và lo-01.tsv của lượt rtc-v1>
    python -X utf8 -B d7-rtc-v1.py  ->  ../d7-rtc-v1.tsv, d7-rtc-v1-gan-trung.tsv, d7-rtc-v1-gan-trung.log
"""
import difflib
import os
import re
import unicodedata
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

from chung import AT, HERE, OUT, U, out_utf8, rd, write_lines, write_tsv

out_utf8()
SRC = Path(os.environ["RTC_V1_DIR"])

# Mục có cờ: đóng cờ. Mọi mục khác: DAT, không mã.
CO = {"biển": "GIU_HAI_NGHIA", "bụng dạ": "GIU_HAI_NGHIA", "ỉu xìu": "GIU_HAI_NGHIA",
      "lời lỗ": "DONG_NGHI", "mỏng tanh": "DONG_NGHI"}
VIET_LAI = {}  # tu -> (ma, chẩn đoán); lượt này không có mục nào

phieu = rd(SRC / "d7-opus.tsv")
assert len(phieu) == 66
for r in phieu:
    if r["co"]:
        assert r["tu"] in CO and CO[r["tu"]].endswith(r["co"]), r["tu"]
rows = []
for r in phieu:
    w = r["tu"]
    if w in VIET_LAI:
        ma, cd = VIET_LAI[w]
        rows.append({"tu": w, "ket_qua": "VIET_LAI", "ma": ma, "chan_doan": cd})
    else:
        rows.append({"tu": w, "ket_qua": "DAT", "ma": CO.get(w, "-"), "chan_doan": ""})
write_tsv(OUT / "d7-rtc-v1.tsv", ["tu", "ket_qua", "ma", "chan_doan"], rows)

# Căn cứ gần trùng: câu gần nhất trong danh sách chính (sau thay) và trong lô, cùng mức đã chấp nhận ở bản phát hành.
tok = lambda s: re.findall(r"\w+", unicodedata.normalize("NFC", s.lower()))
ra = {r["tu"] for r in rd(U / "ra-thay-chinh-thay-the.tsv") if r["vai_tro"] == "RA"}
chinh = []
for l in open(AT / "wordlist.txt", encoding="utf-8"):
    w, g = l.rstrip("\n").split("|", 1)
    chinh.append((w, tok(g)))
lo = {r["tu"]: tok(r["giai_nghia"]) for r in rd(SRC / "lo-01.tsv")}
ev = []
for r in phieu:
    w, a = r["tu"], lo[r["tu"]]
    bc = max((difflib.SequenceMatcher(None, a, b, autojunk=False).ratio(), x) for x, b in chinh if x not in ra and x != w)
    bl = max((difflib.SequenceMatcher(None, a, b, autojunk=False).ratio(), x) for x, b in lo.items() if x != w)
    ev.append({"tu": w, "gan_nhat_chinh": bc[1], "ti_so_chinh": f"{bc[0]:.2f}", "gan_nhat_lo": bl[1], "ti_so_lo": f"{bl[0]:.2f}"})
write_tsv(HERE / "d7-rtc-v1-gan-trung.tsv", list(ev[0].keys()), ev)

# Mức đã chấp nhận ở bản phát hành: tỉ số lớn nhất của mỗi câu với câu khác (ứng viên chung từ hiếm), cặp từ đảo.
df = Counter(t for _, ts in chinh for t in set(ts))
idx = defaultdict(list)
for i, (_, ts) in enumerate(chinh):
    for t in set(ts):
        if df[t] <= 300:
            idx[t].append(i)
best, seen = [0.0] * len(chinh), set()
for ids in idx.values():
    for a, b in combinations(ids, 2):
        if (a, b) not in seen:
            seen.add((a, b))
            s = difflib.SequenceMatcher(None, chinh[a][1], chinh[b][1], autojunk=False).ratio()
            best[a], best[b] = max(best[a], s), max(best[b], s)
gm = dict(chinh)
dao = sorted(((difflib.SequenceMatcher(None, gm[w], gm[" ".join(reversed(w.split(" ")))], autojunk=False).ratio(), w)
              for w in gm if len(w.split(" ")) == 2 and " ".join(reversed(w.split(" "))) in gm
              and w < " ".join(reversed(w.split(" ")))), reverse=True)
log = [f"phiếu: {len(rows)} mục; DAT {sum(r['ket_qua'] == 'DAT' for r in rows)}, VIET_LAI {len(VIET_LAI)}",
       "bản phát hành 7.776 câu, số câu có tỉ số lớn nhất ≥ ngưỡng (cận dưới): "
       + ", ".join(f"≥{t}: {sum(x >= t for x in best)}" for t in (0.5, 0.6, 0.65, 0.7)),
       f"cặp từ đảo trong bản phát hành: {len(dao)}; năm cặp gần nhất: "
       + ", ".join(f"{w} {s:.2f}" for s, w in dao[:5]),
       "mục của Opus có tỉ số với danh sách chính ≥ 0,55: "
       + ", ".join(f"{e['tu']}~{e['gan_nhat_chinh']} {e['ti_so_chinh']}" for e in ev if float(e["ti_so_chinh"]) >= 0.55)]
write_lines(HERE / "d7-rtc-v1-gan-trung.log", log)
print("\n".join(log))
