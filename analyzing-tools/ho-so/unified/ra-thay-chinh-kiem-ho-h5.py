#!/usr/bin/env python3
"""Kiểm họ H5 độc lập cho đợt ra-thay-chinh (kế hoạch, mục 10; nghiệm thu T3).

Khác `check_wordlist.py` (C5): tách mọi dạng " / " của cột `chuan` và `bien_the` trước khi so với
`wordlist.txt`, và đối chiếu từng họ với `ho-so/unified/ra-thay-chinh-h5.tsv`.

    python ra-thay-chinh-kiem-ho-h5.py     # thoát 1 nếu có lỗi
"""
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
AT = HERE.parent.parent
errors = []


def err(msg):
    errors.append(msg)


def lines(path):
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip("\n").split("\n")


def tsv(path):
    ls = lines(path)
    head = ls[0].split("\t")
    out = []
    for i, l in enumerate(ls[1:], 2):
        p = l.split("\t")
        if len(p) != len(head):
            err(f"{path.name}:{i}: {len(p)} cột, cần {len(head)}")
            continue
        out.append(dict(zip(head, p)))
    return out


words = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
wset = set(words)
labels = {r["tu"]: r for r in tsv(AT / "labels.tsv")}
families = tsv(AT / "spelling_families.tsv")
h5rows = tsv(HERE / "ra-thay-chinh-h5.tsv")


def forms(cell):
    return [f.strip() for f in cell.split(" / ") if f.strip()]


fam_by_pair = {}
for r in families:
    for a in forms(r["chuan"]):
        for b in forms(r["bien_the"]):
            fam_by_pair.setdefault((a, b), []).append(r)
            fam_by_pair.setdefault((b, a), []).append(r)

# 1. Không có từ chính nào thuộc họ loại, chờ hay thiếu dữ liệu chưa ký H5
BLOCKING = ("CHO_LOAI", "CHO_NGHIA", "CHO_SAT_NGUONG")
for r in families:
    hit = [f for f in forms(r["chuan"]) + forms(r["bien_the"]) if f in wset]
    if not hit:
        continue
    v = r["ket_luan"]
    if v.startswith("LOAI") or v in BLOCKING:
        err(f"H5: '{hit[0]}' thuộc họ {r['chuan']} ~ {r['bien_the']} ({v})")
    elif "THIEU_DU_LIEU" in v:
        if "H5" not in labels.get(hit[0], {}).get("chu_ky_hai_ben", "").split(";"):
            err(f"H5: '{hit[0]}' thuộc họ thiếu dữ liệu {r['chuan']} ({v}) mà chưa có chữ ký H5")
    elif v.startswith("CHO"):
        err(f"H5: '{hit[0]}' thuộc họ đang chờ {r['chuan']} ({v})")

# 2. Từng dòng của bảng H5 hợp nhất
stat = Counter()
for x in h5rows:
    tu, bt, tt = x["tu"], x["bien_the"], x["trang_thai"]
    fams = fam_by_pair.get((tu, bt), [])
    stat[tt] += 1
    if tt in ("DONG_THUAN_THAY", "DONG_THUAN_THAY_CHO_LOAI"):
        want_cho = tt == "DONG_THUAN_THAY_CHO_LOAI"
        if tu in wset or bt in wset:
            err(f"H5 {tu}/{bt}: từ ra vẫn ở wordlist.txt")
        ok = [f for f in fams if (f["ket_luan"] == "CHO_LOAI" if want_cho else f["ket_luan"].startswith("LOAI"))]
        if not ok:
            err(f"H5 {tu}/{bt}: thiếu họ {'CHO_LOAI' if want_cho else 'LOAI_*'} trong spelling_families.tsv")
    elif tt == "DONG_THUAN_QUA":
        ok = [f for f in fams if f["ket_luan"].startswith("QUA")]
        if not ok:
            err(f"H5 {tu}/{bt}: thiếu họ QUA trong spelling_families.tsv")
        for f in ok:
            same = tu in forms(f["chuan"])
            got = (f["sub_chuan"], f["sub_bien_the"], f["web_chuan"], f["web_bien_the"])
            want = (x["sub_tu"], x["sub_bien_the"], x["web_tu"], x["web_bien_the"])
            if not same:
                want = (x["sub_bien_the"], x["sub_tu"], x["web_bien_the"], x["web_tu"])
            if got != want:
                err(f"H5 {tu}/{bt}: số đếm họ {got} khác bảng H5 {want}")
        if tu not in wset and bt not in wset:
            err(f"H5 {tu}/{bt}: họ QUA mà không có dạng nào trong wordlist.txt")
    elif tt == "DONG_THUAN_DA_RA":
        if tu in wset:
            err(f"H5 {tu}/{bt}: từ đã ra mà vẫn ở wordlist.txt")
    elif tt == "DONG_THUAN_KHONG_CHO_VAO":
        if tu in wset:
            err(f"H5 {tu}/{bt}: không được nhận mà ở wordlist.txt")
    elif tt == "DONG_THUAN_KHAC_TU":
        bad = [f for f in fams if f["ket_luan"].startswith(("LOAI", "CHO"))]
        if bad:
            err(f"H5 {tu}/{bt}: khác từ mà đã đăng ký họ {bad[0]['ket_luan']}")
    else:
        err(f"H5 {tu}/{bt}: trạng thái lạ {tt}")

# 3. Số họ mới của đợt
new = [r for r in families if r["nguon"] == "RA_THAY_CHINH"]
cnt = Counter(r["ket_luan"] for r in new)
want = {"CHO_LOAI": 7, "QUA_H5B": 8, "QUA_RIENG_H5": 6}
for k, v in want.items():
    if cnt.get(k, 0) != v:
        err(f"họ mới {k}: {cnt.get(k, 0)}, cần {v}")
if sum(v for k, v in cnt.items() if k.startswith("LOAI")) != 16:
    err(f"họ LOAI mới: {sum(v for k, v in cnt.items() if k.startswith('LOAI'))}, cần 16 (14 + 2 của T9)")
if len(new) != 37:
    err(f"họ mới: {len(new)}, cần 37")
# T9 (T-rtc-24): buồn thiu và ỉu xìu rút khỏi danh sách chính vì H5c thiếu dữ liệu
for a, b in (("buồn thiu", "buồn thỉu"), ("ỉu xìu", "ỉu xịu")):
    fs = [f for f in fam_by_pair.get((a, b), []) if f["ket_luan"].startswith("LOAI")]
    if not fs:
        err(f"T9: thiếu họ LOAI {a}/{b}")
    if a in wset or b in wset:
        err(f"T9: {a} còn ở wordlist.txt")
if len({(r["chuan"], r["bien_the"]) for r in families}) != len(families):
    err("spelling_families.tsv có họ trùng")

print(f"Từ chính: {len(words)}; họ: {len(families)} (mới {len(new)}: {dict(sorted(cnt.items()))})")
print("Dòng H5 hợp nhất: " + ", ".join(f"{k} {v}" for k, v in sorted(stat.items())))
for m in errors:
    print("LỖI | " + m)
print(f"Tổng: {len(errors)} lỗi.")
sys.exit(1 if errors else 0)
