"""Soát chéo: mã H8 chính thức (cổng P2, tập luật v4: MANH/CHI_BE_MAT/YEU/KHONG_LUOT) cho mọi từ trong
205 dự phòng và hai tập đề cử (Opus, Astra); so với nhãn H8 mà mỗi bên ghi.

    python kiem-h8-chinh-thuc.py
Ghi evidence/h8-chinh-thuc.tsv.
"""
import collections
from chung import *

out_utf8()
AS = AT / "ho-so" / "astra" / "du-phong-v2"
gate = {}
for f in ("cong-opus-v4.tsv", "cong-astra-v4.tsv"):
    for i, r in enumerate(rd(U / f), start=2):
        if r["cong"] == "H8":
            ma = r["ly_do"].split(":")[-1] if r["ly_do"] not in ("", "-") else "MANH"
            gate.setdefault(r["ung_vien"], {})[f] = (ma, i)
lots = {}
for f in ("l2-ung-vien.tsv", "l2b-ung-vien.tsv", "l2c-ung-vien.tsv", "l3-ung-vien.tsv", "l2d-ung-vien.tsv"):
    for i, r in enumerate(rd(U / f), start=2):
        lots[r["tu"]] = (r["H8_so_hoc"], f"{f}:{i}")
words = collections.OrderedDict()
for r in rd(OUT / "du-phong-205-phan-loai-opus.tsv", True):
    words.setdefault(r["tu"], {})["opus_du_phong"] = r["H8"]
for r in rd(AS / "du-phong-phan-loai.tsv"):
    words.setdefault(r["tu"], {})["astra_du_phong"] = r["h8_so_hoc"]
for r in rd(OUT / "de-cu-them-opus.tsv", True):
    words.setdefault(r["tu"], {})["opus_de_cu"] = r["H8"]
for r in rd(AS / "honorable-mentions.tsv"):
    words.setdefault(r["tu"], {})["astra_de_cu"] = r["h8_so_hoc"]
rows = []
for w, d in words.items():
    g = gate.get(w, {})
    o = g.get("cong-opus-v4.tsv")
    a = g.get("cong-astra-v4.tsv")
    if o:
        chinh_thuc, nguon = o[0], f"cong-opus-v4.tsv:{o[1]}"
        if a and a[0] != o[0]:
            chinh_thuc += f"|astra:{a[0]}"
    elif w in lots:
        chinh_thuc, nguon = "LO:" + lots[w][0], lots[w][1]
    else:
        chinh_thuc, nguon = "CHUA_CO", "-"
    rows.append({"tu": w, "h8_chinh_thuc": chinh_thuc, "nguon": nguon,
                 "opus_du_phong": d.get("opus_du_phong", "-"), "astra_du_phong": d.get("astra_du_phong", "-"),
                 "opus_de_cu": d.get("opus_de_cu", "-"), "astra_de_cu": d.get("astra_de_cu", "-")})
write_tsv(HERE / "h8-chinh-thuc.tsv", ["tu", "h8_chinh_thuc", "nguon", "opus_du_phong", "astra_du_phong", "opus_de_cu", "astra_de_cu"], rows)


def lech(col):
    out = []
    for r in rows:
        v = r[col]
        if v == "-":
            continue
        g = r["h8_chinh_thuc"].replace("LO:", "")
        strong_gate = g in ("MANH",)
        strong_side = v in ("MANH",)
        if strong_gate != strong_side:
            out.append((r["tu"], v, r["h8_chinh_thuc"], r["nguon"]))
    return out


for col in ("opus_du_phong", "astra_du_phong", "opus_de_cu", "astra_de_cu"):
    print(col, "lệch so với cổng chính thức:", lech(col))
print("mã cổng của 205 dự phòng:", collections.Counter(r["h8_chinh_thuc"] for r in rows if r["opus_du_phong"] != "-"))
print("mã cổng của đề cử Astra:", collections.Counter(r["h8_chinh_thuc"] for r in rows if r["astra_de_cu"] != "-"))
print("mã cổng của đề cử Opus:", collections.Counter(r["h8_chinh_thuc"] for r in rows if r["opus_de_cu"] != "-"))
