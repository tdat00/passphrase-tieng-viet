"""Opus duyệt đề xuất HM của Astra cho chu kỳ D-rtc-8 (hm-chu-ky-1.tsv).

Kiểm bằng dữ liệu trong repo: hạng, nhãn, lớp, khóa so với danh sách chính sau thay, dự phòng còn lại, khóa chặn
cũ và mới, họ H5, chữ ký cũ. Liệt kê cách đọc cùng khóa từ opus-counts.tsv, bốn danh sách HND (bản tạm ngoài repo,
HND_DIR) và bản Kaikki ghim (KAIKKI, ngoài repo). Chỉ ghi đầu mục và số đếm, không ghi lời giải nghĩa.

Chạy (từ thư mục evidence):
    set HND_DIR=<ngoài repo: Viet11K.txt … Viet74K.txt>
    set KAIKKI=<ngoài repo: vi.jsonl.gz, sha256 1f0abd…>
    python -X utf8 -B hm-chu-ky-1-opus.py
"""
import gzip
import json
import os
from collections import defaultdict
from pathlib import Path

from chung import AT, OUT, U, HND_DIR, key, lines, out_utf8, rd, sha_file, write_tsv

out_utf8()
ASTRA = AT / "ho-so" / "astra" / "ra-thay-chinh"
KAIKKI = Path(os.environ["KAIKKI"])

hm = rd(AT / "honorable-mentions.tsv")
xh = {r["tu"]: r for r in rd(U / "xep-hang.tsv")}
de_xuat = rd(ASTRA / "hm-chu-ky-1.tsv")
ten_dx = [r["tu"] for r in de_xuat]

# 1. Hạng: mọi HM nhãn OK theo hạng S4 đã khóa.
ok = sorted((r for r in hm if r["nhan_ho_so"] == "OK"), key=lambda r: int(xh[r["tu"]]["hang"]))
assert len(ok) == 130 and all(r["tu"] in xh for r in ok)
dau = []
for r in ok:
    dau.append(r)
    if r["tu"] == ten_dx[-1]:
        break
bo_qua = [(r["tu"], r["lop"], xh[r["tu"]]["hang"]) for r in dau if r["tu"] not in ten_dx]
thieu = [w for w in ten_dx if w not in {r["tu"] for r in dau}]
thu_tu_khop = [r["tu"] for r in dau if r["tu"] in ten_dx] == ten_dx
print(f"OK theo hạng tới {ten_dx[-1]}: {len(dau)} mục; bỏ qua {bo_qua}; thiếu {thieu}; thứ tự khớp {thu_tu_khop}")
f_ok = [r["tu"] for r in ok if r["lop"] == "F"]
print("OK lớp F:", f_ok)

# 2. Khóa: chính sau thay, dự phòng còn lại, khóa chặn cũ và mới.
chinh = {l.split("|")[0] for l in lines(AT / "wordlist.txt")}
tt = rd(U / "ra-thay-chinh-thay-the.tsv")
ra = {r["tu"] for r in tt if r["vai_tro"] == "RA"}
vao = {r["tu"] for r in tt if r["vai_tro"] == "VAO"}
assert len(chinh) == 7776 and ra <= chinh and len(ra) == len(vao) == 116
chinh_sau = (chinh - ra) | vao
du_phong = set(lines(AT / "du-phong.txt"))
assert len(du_phong) == 205 and vao <= du_phong
du_phong_con = du_phong - vao
khoa_chinh = {key(w): w for w in chinh_sau}
khoa_dp = {key(w): w for w in du_phong_con}
chan_cu = {r["khoa"]: r["ma"] for r in rd(AT / "blocked_keys.tsv")}
h7 = rd(U / "ra-thay-chinh-h7.tsv")
chan_moi = {r["khoa"]: r["trang_thai"] for r in h7 if "THAY" in r["trang_thai"]}
chan_moi["baotu"] = "T-dpv2-7"
chan_moi["lamco"] = "T-rtc-17"
print(f"chính sau thay {len(chinh_sau)}; dự phòng còn {len(du_phong_con)}; khóa chặn cũ {len(chan_cu)}, mới {len(chan_moi)}")

# 3. Nguồn cách đọc cùng khóa.
k25 = {key(w) for w in ten_dx}
assert len(k25) == 25
hnd = defaultdict(set)
for ten in ("Viet11K", "Viet22K", "Viet39K", "Viet74K"):
    for l in (HND_DIR / f"{ten}.txt").read_text(encoding="utf-8").splitlines():
        w = l.strip().lower()
        if w and key(w) in k25:
            hnd[key(w)].add(w)
kk = defaultdict(set)
with gzip.open(KAIKKI, "rt", encoding="utf-8") as f:
    for l in f:
        w = json.loads(l).get("word", "").strip().lower()
        if w and key(w) in k25:
            kk[key(w)].add(w)
oc = defaultdict(list)
for r in rd(U / "opus-counts.tsv"):
    if r["khoa"] in k25:
        oc[r["khoa"]].append(r)

ho = rd(AT / "spelling_families.tsv")
h5 = rd(U / "ra-thay-chinh-h5.tsv")
lb = {r["tu"]: r for r in rd(AT / "labels.tsv")}
ck = defaultdict(list)
for r in rd(U / "chu-ky.tsv"):
    ck[r["khoa"]].append(r)

rows = []
for i, r in enumerate(de_xuat, 1):
    w, k = r["tu"], r["khoa"]
    h = next(x for x in hm if x["tu"] == w)
    loi = []
    if key(w) != k:
        loi.append("khóa sai")
    if k in khoa_chinh:
        loi.append(f"trùng chính {khoa_chinh[k]}")
    if k in khoa_dp:
        loi.append(f"trùng dự phòng {khoa_dp[k]}")
    if k in chan_cu:
        loi.append(f"khóa chặn cũ {chan_cu[k]}")
    if k in chan_moi:
        loi.append(f"khóa chặn mới {chan_moi[k]}")
    if len(k) < 4:
        loi.append("dưới 4 chữ")
    if h["nhan_ho_so"] != "OK" or h["lop"] == "F" or h["lop"] != r["lop"]:
        loi.append(f"nhãn/lớp {h['nhan_ho_so']}/{h['lop']}")
    l = lb.get(w)
    ho_w = [f"{x['chuan']}/{x['bien_the']}:{x['ket_luan']}" for x in ho if w in (x["chuan"], x["bien_the"])]
    h5_w = [f"{x.get('tu_chinh', '')}" for x in h5 if w in "\t".join(x.values()).split("\t")]
    doc = {}
    for x in oc[k]:
        if x["tu"] != w:
            doc[x["tu"]] = f"{x['vai_tro']}:{x['sub_sach']}/{x['web_sach']}"
    for x in sorted((hnd[k] | kk[k]) - {w}):
        nguon = ("HND" if x in hnd[k] else "") + ("+KK" if x in kk[k] else "")
        doc[x] = (doc[x] + ";" if x in doc else "") + nguon
    ch = next((x for x in oc[k] if x["tu"] == w), None)
    rows.append({
        "thu_tu": i, "tu": w, "khoa": k, "lop": r["lop"], "hang_S4": xh[w]["hang"], "nhom_hm": h["nhom"],
        "de_xuat_astra": r["ket_qua_H"], "kiem_du_lieu": "; ".join(loi) or "DAT",
        "nhan_labels": f"{l['trang_thai']}/{l['nhan']}/{l['lop']}" if l else "-",
        "ho_h5": "; ".join(ho_w + h5_w) or "-",
        "chu_ky_cu": "; ".join(f"{x['tu']}:{x['loai_ky']}:{x['nguoi_ky']}" for x in ck[k]) or "-",
        "so_chinh": f"{ch['sub_sach']}/{ch['web_sach']}" if ch else "-",
        "doc_khac": "; ".join(f"{a}({b})" for a, b in doc.items()) or "-",
    })
hdr = list(rows[0].keys())
write_tsv(OUT / "evidence" / "hm-chu-ky-1-opus-kiem.tsv", hdr, rows)
for x in rows:
    print(x["thu_tu"], x["tu"], x["hang_S4"], x["kiem_du_lieu"], "|", x["nhan_labels"], "|", x["ho_h5"][:60], "|",
          x["chu_ky_cu"][:60], "|", x["so_chinh"], "|", x["doc_khac"][:230])
print("sha256 Kaikki:", sha_file(KAIKKI)[:12])
