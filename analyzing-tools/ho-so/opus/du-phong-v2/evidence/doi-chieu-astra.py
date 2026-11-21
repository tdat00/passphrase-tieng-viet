"""Soát chéo vòng 1: đối chiếu phân bậc 205 dự phòng và tập đề cử thêm giữa Opus và Astra.

    python doi-chieu-astra.py
Ghi evidence/doi-chieu-du-phong.tsv (mọi từ khác bậc), evidence/doi-chieu-de-cu.tsv (hợp hai tập, đánh dấu bên có)
và in tóm tắt. Chỉ đọc tệp của Astra.
"""
import collections
from chung import *

out_utf8()
AS = AT / "ho-so" / "astra" / "du-phong-v2"
op = {r["tu"]: r for r in rd(OUT / "du-phong-205-phan-loai-opus.tsv", True)}
asr = {r["tu"]: r for r in rd(AS / "du-phong-phan-loai.tsv")}
assert list(op) == list(asr) == lines(AT / "du-phong.txt"), "thứ tự hoặc tập 205 khác nhau"
pairs = collections.Counter((op[w]["bac"], asr[w]["tang"]) for w in op)
print("bậc Opus × tầng Astra:", dict(sorted(pairs.items())))
diff = []
for w in op:
    o, a = op[w], asr[w]
    if o["bac"] != a["tang"]:
        diff.append({"tu": w, "ngan": o["ngan"], "bac_opus": o["bac"], "tang_astra": a["tang"],
                     "ly_do_opus": o["van_de"] or "-", "danh_gia_astra": a["danh_gia_moi"], "rui_ro_astra": a["rui_ro_can_luu_y"]})
write_tsv(HERE / "doi-chieu-du-phong.tsv", ["tu", "ngan", "bac_opus", "tang_astra", "ly_do_opus", "danh_gia_astra", "rui_ro_astra"], diff)
print("khác bậc:", len(diff))

ohm = {r["tu"]: r for r in rd(OUT / "de-cu-them-opus.tsv", True)}
ahm = {r["tu"]: r for r in rd(AS / "honorable-mentions.tsv")}
excl = {r["tu"]: r for r in rd(AS / "evidence" / "candidate-exclusions.tsv")}
rows = []
for w in sorted(set(ohm) | set(ahm), key=o1):
    o, a = ohm.get(w), ahm.get(w)
    ben = "CA_HAI" if o and a else ("CHI_OPUS" if o else "CHI_ASTRA")
    rows.append({"tu": w, "khoa": key(w), "ben": ben, "nhom_opus": o["nhom"] if o else "-", "nhom_astra": a["tang"] if a else "-",
                 "nhan": (o or a)["nhan"] or "-", "lop": (o or a)["lop"] or "-",
                 "astra_loai_tam": (excl[w]["ly_do"] if w in excl else "-"),
                 "ghi_chu_opus": (o["ghi_chu"] or "-") if o else "-"})
write_tsv(HERE / "doi-chieu-de-cu.tsv", ["tu", "khoa", "ben", "nhom_opus", "nhom_astra", "nhan", "lop", "astra_loai_tam", "ghi_chu_opus"], rows)
c = collections.Counter((r["ben"], r["nhom_opus"], r["nhom_astra"]) for r in rows)
for k, v in sorted(c.items()):
    print(k, v)
for b in ("CHI_ASTRA",):
    print(b, [r["tu"] for r in rows if r["ben"] == b])
print("CHI_OPUS DC1:", [r["tu"] for r in rows if r["ben"] == "CHI_OPUS" and r["nhom_opus"] == "DC1"])
print("CHI_OPUS DC2:", [r["tu"] for r in rows if r["ben"] == "CHI_OPUS" and r["nhom_opus"] == "DC2"])
