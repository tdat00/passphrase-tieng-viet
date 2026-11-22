#!/usr/bin/env python3
"""Kiểm gói chữ ký và khóa chặn độc lập cho đợt ra-thay-chinh (kế hoạch, mục 10; nghiệm thu T2, T4).

Mỗi khóa K2 giữ lại <-> đủ hai người ký <-> `hieu_luc` <-> lý do và tệp gốc <-> `labels.tsv`;
đồng thời so từng khóa và mã trong `blocked_keys.tsv` với `ho-so/unified/ra-thay-chinh-h7.tsv`.

    python ra-thay-chinh-kiem-chu-ky.py     # thoát 1 nếu có lỗi
"""
import sys
import unicodedata
from collections import Counter, defaultdict
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


def key(w):
    s = "".join(c for c in unicodedata.normalize("NFD", w) if not unicodedata.combining(c))
    return s.replace("đ", "d").replace("Đ", "D").lower().replace(" ", "")


words = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
wkeys = {key(w): w for w in words}
labels = {r["tu"]: r for r in tsv(AT / "labels.tsv")}
blocked = {r["khoa"]: r for r in tsv(AT / "blocked_keys.tsv")}
sig = tsv(HERE / "chu-ky.tsv")
h7 = {r["khoa"]: r for r in tsv(HERE / "ra-thay-chinh-h7.tsv")}
thay = tsv(HERE / "ra-thay-chinh-thay-the.tsv")
hm = {r["tu"] for r in tsv(AT / "honorable-mentions.tsv")}

# 1. Chữ ký K2 theo khóa
by_key = defaultdict(list)
for r in sig:
    if r["loai_ky"] == "K2":
        by_key[r["khoa"]].append(r)
    if r["hieu_luc"] not in ("CO", "RUT", "THAY_THE"):
        err(f"chu-ky.tsv: hieu_luc lạ '{r['hieu_luc']}' ở {r['khoa']}/{r['loai_ky']}/{r['nguoi_ky']}")
valid = {}
legacy_single = []
for k, rows in by_key.items():
    co = [r for r in rows if r["hieu_luc"] == "CO"]
    who = {r["nguoi_ky"] for r in co}
    if who == {"Astra", "Opus"}:
        valid[k] = co
    elif co:
        legacy_single.append(k)
    for r in rows:
        if r["hieu_luc"] == "THAY_THE" and not co and k not in blocked:
            err(f"K2 {k}: dòng THAY_THE mà không có cặp hiệu lực thay thế hay khóa chặn")
    for r in co:
        if not r["ly_do"].strip() or not r["tep_goc"].strip() or not r["ngay"].strip():
            err(f"K2 {k}/{r['nguoi_ky']}: thiếu lý do, ngày hoặc tệp gốc")
        if key(r["tu"]) != k:
            err(f"K2 {k}: cột tu '{r['tu']}' không ra khóa")
    rtc = [r for r in co if "ra-thay-chinh/" in r["tep_goc"]]
    if rtc and sorted(r["nguoi_ky"] for r in rtc) != ["Astra", "Opus"]:
        err(f"K2 {k}: gói rtc phải có đúng một dòng hiệu lực mỗi người, có {sorted(r['nguoi_ky'] for r in rtc)}")
    if rtc and len(co) != 2:
        err(f"K2 {k}: còn {len(co)} dòng hiệu lực cạnh gói rtc (dòng cũ phải THAY_THE)")

# 2. Mọi K2 trong labels.tsv và mọi K2 giữ lại của bảng H7 phải có hai chữ ký hiệu lực
k2_labels = {key(w): w for w, r in labels.items() if r["trang_thai"] == "CHINH" and "K2" in r["chu_ky_hai_ben"].split(";")}
K2_STATUS = ("DONG_THUAN_GIU_DA_KY_PHIEU", "CHU_DU_AN_GIU_DA_KY_PHIEU", "GIU_CHU_KY_CU")
k2_h7 = {k for k, r in h7.items() if r["trang_thai"] in K2_STATUS and k in wkeys}
rtc_keys = {k for k, rows in by_key.items() if any("ra-thay-chinh/" in r["tep_goc"] and r["hieu_luc"] == "CO" for r in rows)}
for k, w in k2_labels.items():
    if k not in valid:
        err(f"labels: '{w}' có K2 nhưng khóa {k} thiếu hai chữ ký hiệu lực")
    if k not in wkeys:
        err(f"labels: '{w}' có K2 nhưng không ở wordlist.txt")
for k in k2_h7:
    if k not in valid:
        err(f"H7: khóa K2 giữ lại {k} ({wkeys[k]}) thiếu hai chữ ký hiệu lực")
    if k not in k2_labels:
        err(f"H7: khóa K2 giữ lại {k} ({wkeys[k]}) chưa có K2 trong labels.tsv")
hm_keys = {key(h) for h in hm}
for k in rtc_keys:
    if k in wkeys and k not in k2_labels:
        err(f"chu-ky: khóa K2 {k} của '{wkeys[k]}' chưa vào labels.tsv")
    if k not in wkeys and k not in hm_keys:
        err(f"chu-ky: khóa K2 {k} của gói rtc không thuộc từ chính hay HM")
    if k in blocked and blocked[k]["ma"] in ("K0", "K1", "K0;K1"):
        err(f"chu-ky: khóa K2 {k} đang bị chặn {blocked[k]['ma']}")
for k in valid:
    if k in blocked and blocked[k]["ma"] in ("K0", "K1", "K0;K1") and k in set(rtc_keys) | set(k2_labels) | k2_h7:
        err(f"chu-ky: khóa K2 {k} đang bị chặn {blocked[k]['ma']}")
for k, rows in by_key.items():
    if k in ("lamco", "bang", "chia") and any(r["hieu_luc"] == "CO" for r in rows) and k in blocked:
        err(f"chu-ky: khóa {k} bị chặn mà vẫn có chữ ký K2 hiệu lực")
for w, r in labels.items():
    if r["trang_thai"] == "CHINH" and key(w) in blocked:
        err(f"blocked_keys: khóa {key(w)} của từ chính '{w}' bị chặn")

# 3. Khóa chặn so với bảng H7 (T2) và kết quả T9
ra = [r for r in thay if r["vai_tro"] == "RA" and r["ma"] in ("K0", "K1")]
expect = {key(r["tu"]): r["ma"] for r in ra}
expect["baotu"] = "K1"
expect["lamco"] = "K1"
# T9 (T-rtc-24, D-rtc-10): phết K0, cau có K1 (hai SA thống nhất), tụ tập K1 (chủ dự án thay)
t9_extra = {"phet": "K0", "cauco": "K1", "tutap": "K1"}
t9_astra = {r["khoa"]: r["de_xuat_chung"] for r in tsv(HERE.parent / "astra" / "ra-thay-chinh" / "t9-doi-dap.tsv")}
for k, code in t9_extra.items():
    if k != "tutap" and not t9_astra.get(k, "").startswith("THAY_" + code):
        err(f"T9: bảng đối đáp của Astra không ghi THAY_{code} cho {k}")
expect.update(t9_extra)
new_bk = {k: r for k, r in blocked.items() if r["nguon"] in ("H7_RA_THAY_CHINH", "T-dpv2-7", "T-rtc-17")}
if len(new_bk) != 97 or len(expect) != 97:
    err(f"khóa chặn mới: {len(new_bk)}, kỳ vọng {len(expect)}, cần 97")
for k, code in expect.items():
    r = blocked.get(k)
    if not r or r["ma"] != code:
        err(f"khóa chặn {k}: có {r and r['ma']}, cần {code}")
    elif k not in ("baotu", "lamco") and k not in t9_extra:
        if h7[k]["opus"] == "K0" and code != "K0" or h7[k]["opus"] != "K0" and code != "K1":
            err(f"khóa chặn {k}: mã {code} lệch bảng H7 ({h7[k]['opus']}/{h7[k]['astra']})")
        if r["nguon"] != "H7_RA_THAY_CHINH":
            err(f"khóa chặn {k}: nguồn {r['nguon']}")
    elif k in t9_extra and r["nguon"] != "H7_RA_THAY_CHINH":
        err(f"khóa chặn {k}: nguồn {r['nguon']}")
for k in new_bk:
    if k not in expect:
        err(f"khóa chặn thừa {k}")
for k, r in h7.items():
    if r["trang_thai"] in ("DONG_THUAN_THAY", "CHU_DU_AN_THAY") and (k not in blocked or k in wkeys):
        err(f"H7 thay {k}: thiếu khóa chặn hoặc từ còn ở wordlist.txt")
for k in t9_extra:
    if k in wkeys:
        err(f"T9: từ {wkeys[k]} của khóa chặn {k} còn ở wordlist.txt")

# 3b. Gói chữ ký T9: khóa hai SA cùng ký "Y" trong hai bảng đối đáp phải có K2 hiệu lực
t9_o = tsv(HERE.parent / "opus" / "ra-thay-chinh" / "t9-doi-dap.tsv")
t9_a = tsv(HERE.parent / "astra" / "ra-thay-chinh" / "t9-doi-dap.tsv")
t9_keys = {o["khoa"] for o, a in zip(t9_o, t9_a)
           if o["ky"] == "Y" and a["ky(Y/N)"] == "Y" and o["khoa"] not in ("-", "thay")}
if len(t9_keys) != 61:
    err(f"T9: {len(t9_keys)} khóa cùng ký, cần 61")
for k in t9_keys:
    if k not in valid:
        err(f"T9: khóa {k} thiếu hai chữ ký hiệu lực")
    t9rows = [r for r in by_key.get(k, []) if r["hieu_luc"] == "CO" and "t9-doi-dap" in r["tep_goc"]]
    if sorted(r["nguoi_ky"] for r in t9rows) != ["Astra", "Opus"]:
        err(f"T9: khóa {k} cần đúng một dòng T9 hiệu lực mỗi người, có {sorted(r['nguoi_ky'] for r in t9rows)}")
    if k not in wkeys:
        err(f"T9: khóa {k} không thuộc từ chính")
    elif k not in k2_labels:
        err(f"T9: khóa {k} chưa có K2 trong labels.tsv")

# 3c. Mỗi từ chính có K2: đúng một dòng hiệu lực mỗi người cho chính mặt chữ
for k, w in k2_labels.items():
    mine = [r for r in by_key.get(k, []) if r["hieu_luc"] == "CO" and r["tu"] == w]
    cnt = Counter(r["nguoi_ky"] for r in mine)
    if cnt.get("Astra", 0) != 1 or cnt.get("Opus", 0) != 1:
        err(f"K2 '{w}': dòng hiệu lực {dict(cnt)}, cần đúng một dòng mỗi người")

# 4. Nhãn (T4)
chinh = [r for r in labels.values() if r["trang_thai"] == "CHINH"]
cnt = Counter(r["nhan"] for r in chinh)
lop = Counter(r["lop"] for r in chinh)
if len(chinh) != 7776 or {r["tu"] for r in chinh} != set(words):
    err(f"labels: {len(chinh)} dòng CHINH không khớp wordlist.txt")
if cnt.get("R1", 0) or cnt.get("R2", 0):
    err(f"labels: R1/R2 = {cnt.get('R1', 0)}/{cnt.get('R2', 0)}, cần 0")
if lop.get("F", 0) > 77:
    err(f"labels: lớp F {lop['F']} > 77")

print(f"K2: {len(valid)} khóa có chữ ký hiệu lực của cả hai người (gói rtc {len(rtc_keys)}); labels K2 {len(k2_labels)}; H7 K2 giữ lại {len(k2_h7)}")
print(f"Chữ ký K2 cũ chỉ một người ký, ngoài tập giữ lại: {len(legacy_single)} khóa (không xét)")
print(f"Khóa chặn mới: {len(new_bk)} ({dict(Counter(r['ma'] for r in new_bk.values()))}); tổng {len(blocked)}")
print(f"Nhãn: CHINH {len(chinh)}, {dict(cnt)}, lớp {dict(sorted(lop.items()))}")
for m in errors:
    print("LỖI | " + m)
print(f"Tổng: {len(errors)} lỗi.")
sys.exit(1 if errors else 0)
