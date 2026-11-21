"""H7, phần bổ sung: tìm cách đọc khác cùng khóa trong bốn danh sách HND (Viet11K/22K/39K/74K, bản ghim 688b095)
cho mọi từ chính; so với các dòng DOC_KHAC của U/opus-counts.tsv.

    set HND_DIR=<thư mục tạm NGOÀI repo chứa Viet11K.txt … Viet74K.txt>
    python h7-hnd-cung-khoa.py  ->  h7-hnd-cung-khoa.tsv, h7-hnd-cung-khoa.log

Chỉ ghi các cặp mà DOC_KHAC chưa có (cần đọc); các cặp còn lại chỉ ghi số đếm trong log. Không chép danh sách HND.
Danh sách HND là GPL: tải tạm ngoài repo, kiểm SHA-256 với manifest, xóa sau khi chạy.
"""
import collections
import hashlib
import json
import unicodedata
from chung import *

out_utf8()
m = json.loads((AT / "manifest.json").read_text(encoding="utf-8"))
sha_mf = {v["sha256"] for v in m["nguon_du_lieu"][:4]}
hnd = collections.defaultdict(set)
log = []
for ten in ("Viet11K", "Viet22K", "Viet39K", "Viet74K"):
    p = HND_DIR / f"{ten}.txt"
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    log.append(f"{ten}: sha256 {h} {'KHOP_MANIFEST' if h in sha_mf else 'KHONG_KHOP'}")
    for l in p.read_text(encoding="utf-8").splitlines():
        w = unicodedata.normalize("NFC", l.strip()).lower()
        if w:
            hnd[key(w)].add(w)
main = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
oc = rd(U / "opus-counts.tsv")
ung = {r["tu"] for r in oc if r["vai_tro"] == "UNG_VIEN"}
dk = collections.defaultdict(set)
for r in oc:
    if r["vai_tro"] == "DOC_KHAC":
        dk[r["khoa"]].add(r["tu"])
rows = []
thieu_phu = 0
for w in main:
    k = key(w)
    khac = sorted(hnd.get(k, set()) - {w}, key=o1)
    for x in khac:
        co_dk = x in dk.get(k, set())
        if not co_dk and w in ung:
            thieu_phu += 1
        rows.append({"khoa": k, "tu_chinh": w, "doc_khac_hnd": x,
                     "nhom_tu_chinh": "CO_DEM_OPUS" if w in ung else "LO_L2_L3_KHONG_DOC_KHAC",
                     "co_trong_doc_khac": "CO" if co_dk else "KHONG"})
write_tsv(HERE / "h7-hnd-cung-khoa.tsv", ["khoa", "tu_chinh", "doc_khac_hnd", "nhom_tu_chinh", "co_trong_doc_khac"],
          [r for r in rows if r["co_trong_doc_khac"] == "KHONG"])
khong_dem = [r for r in rows if r["nhom_tu_chinh"] == "LO_L2_L3_KHONG_DOC_KHAC"]
log.append(f"từ chính: {len(main)}; không có trong opus-counts (lô L2/L3): {sum(w not in ung for w in main)}")
log.append(f"cặp cùng khóa trong HND: {len(rows)}; của từ có đếm OPUS mà thiếu trong DOC_KHAC: {thieu_phu}")
log.append(f"cặp của từ lô L2/L3: {len(khong_dem)} trên {len({r['tu_chinh'] for r in khong_dem})} từ")
(HERE / "h7-hnd-cung-khoa.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
print("\n".join(log))
print(" ; ".join(f"{r['tu_chinh']}>{r['doc_khac_hnd']}" for r in khong_dem))
