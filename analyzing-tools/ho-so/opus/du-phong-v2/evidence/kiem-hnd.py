"""Tra thành viên HND (H3) và các mục HND khác cùng khóa (đầu vào cho H7) của một danh sách từ.

Cần bốn tệp Viet11K/22K/39K/74K (bản 688b095, kiểm SHA-256 theo manifest.json) trong thư mục HND_DIR (biến môi trường; mặc định evidence/_tam-hnd);
thư mục này chỉ là bản tạm, xóa sau khi chạy (không lưu danh sách HND, GPL, vào repo).

    python kiem-hnd.py <tệp mỗi dòng một từ> <tệp TSV ra>
"""
import collections
import sys
import unicodedata
from chung import *

out_utf8()
SHA = {"Viet11K": "401752a95c8c97638ecf4df8445ded60d9db87a8f1bbca2e7fc3b6d00eb1132e",
       "Viet22K": "fdb37a1f21cb44898894390fb87d137830ed1507316c2729bad2d804db81033d",
       "Viet39K": "5c139a85964bf8980c6659418007e2ba5e3e5cc0098fe16c08f1bf5a6dd91ec5",
       "Viet74K": "b83d49308336f12ca46d06287d8db6e2cdc7a725d9a9dac56930051775fafb90"}
tam = HND_DIR
sets = {}
for name, h in SHA.items():
    p = tam / f"{name}.txt"
    assert sha_file(p) == h, f"{name}: SHA-256 không khớp manifest"
    sets[name] = {unicodedata.normalize("NFC", l.strip().lower()).replace("-", " ") for l in open(p, encoding="utf-8") if l.strip()}
bykey = collections.defaultdict(set)
for w in sets["Viet74K"]:
    bykey[key(w)].add(w)
words = lines(sys.argv[1])
rows = []
for w in words:
    tags = [n.replace("Viet", "") for n in SHA if w in sets[n]]
    others = sorted(x for x in bykey.get(key(w), ()) if x != w)
    rows.append({"tu": w, "khoa": key(w), "hnd": ";".join(tags), "muc_hnd_cung_khoa": ";".join(others)})
write_tsv(sys.argv[2], ["tu", "khoa", "hnd", "muc_hnd_cung_khoa"], rows)
print(len(rows), "từ;", sum(1 for r in rows if r["hnd"]), "có trong HND;", sum(1 for r in rows if r["muc_hnd_cung_khoa"]), "có mục HND khác cùng khóa")
