"""Bước 1: gom sự kiện cho 205 từ dự phòng (không chép giải nghĩa; chỉ hash).

    python thu-thap-du-phong.py

Ghi evidence/du-phong-205-su-kien.tsv và in tóm tắt.
"""
import collections
from chung import *

out_utf8()
res = lines(AT / "du-phong.txt")
main = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
main_keys = {key(w): w for w in main}
res_keys = {key(w): w for w in res}
labels = {r["tu"]: r for r in rd(AT / "labels.tsv")}
xh = rd(U / "xep-hang.tsv")
xh_by = {r["tu"]: r for r in xh}
p6in = {r["tu"]: r for r in rd(U / "p6-dau-vao.tsv")}
lo = {}
for name, f in [("L2A", "l2-nhan-sau-H9-opus.tsv"), ("L2B", "l2b-nhan-sau-H9-opus.tsv"),
                ("L2C", "l2c-nhan-sau-H9-opus.tsv"), ("L3", "l3-nhan-sau-H9-opus.tsv")]:
    for r in rd(U / f):
        lo[r["tu"]] = (name, r)
ungvien = {}
for f in ["l2-ung-vien.tsv", "l2b-ung-vien.tsv", "l2c-ung-vien.tsv", "l3-ung-vien.tsv"]:
    for r in rd(U / f):
        ungvien[r["tu"]] = r
p1 = p1_table()
oc = counts_opus()
po = collections.defaultdict(list)
pa = collections.defaultdict(list)
for r in rd(U / "phieu-opus.tsv"):
    po[r["tu"]].append(r)
for r in rd(U / "phieu-astra.tsv"):
    pa[r["tu"]].append(r)
pb = collections.defaultdict(list)
for r in rd(U / "phan-bien.tsv"):
    pb[r["tu"]].append(r)
ck = collections.defaultdict(set)
for r in rd(U / "chu-ky.tsv"):
    if r["hieu_luc"] == "CO":
        ck[r["tu"]].add(f'{r["loai_ky"]}:{r["nguoi_ky"]}')
cb = collections.defaultdict(list)
for r in rd(U / "canh-bao-khong-dau.tsv"):
    cb[r["ung_vien"]].append(r)
gate = collections.defaultdict(list)
for r in rd(U / "cong-opus-v4.tsv"):
    if r["ket_qua"] != "PASS":
        gate[r["ung_vien"]].append(f'{r["cong"]}:{r["ket_qua"]}')
blocked = {r["khoa"]: r["ma"] for r in rd(AT / "blocked_keys.tsv")}
fam = collections.defaultdict(list)
for r in rd(AT / "spelling_families.tsv"):
    for x in (r["chuan"], r["bien_the"]):
        fam[x].append(f'{r["chuan"]}/{r["bien_the"]}:{r["ket_luan"]}')
d6fam = collections.defaultdict(list)
for r in rd(AT / "d6-ho-chinh-ta.tsv"):
    d6fam[r["dang_A"]].append(r["dang_B"])
    d6fam[r["dang_B"]].append(r["dang_A"])
kk = {r["tu"]: r for r in rd(U / "p7-v4-kiem-ke-D8-chua-chot-astra.tsv")}
gn = {r["tu"]: r for r in rd(U / "p7-v4-du-phong-168-co-nghia-cho-duyet.tsv")}
chua_viet = {r["tu"] for r in rd(U / "p7-v3-c13-hoa-astra-tu-chua-viet.tsv")}
review_files = {"v1": ["soat-nghia-astra.tsv", "soat-nghia-opus.tsv"], "v2": ["soat-nghia-v2-astra.tsv", "soat-nghia-v2-opus.tsv"],
                "v3": ["soat-nghia-v3-astra.tsv", "soat-nghia-v3-opus.tsv", "soat-nghia-v3-opus-bo-sung.tsv"]}
reviews = {}
for luot, fs in review_files.items():
    for f in fs:
        who = "astra" if "astra" in f else "opus"
        for r in rd(U / f):
            reviews.setdefault((luot, r["tu"]), []).append(f'{who}:{r["ma"]}/{r["muc_do"]}:{r["vai"]}')

# Thứ hạng trong ngăn sau kịch bản P0 (bỏ 132 mục khấu trừ khỏi xep-hang sau v2)
k132 = {r["tu"] for r in rd(U / "p7-v3-khau-tru-132-theo-P0-astra.tsv")}
pool_p0 = [r for r in xh if r["tu"] not in k132]
ngan_rank = {}
for ngan in ("OK_KHONG_F", "OK_F"):
    items = [r for r in pool_p0 if r["nhan"] == "OK" and ((r["lop"] == "F") == (ngan == "OK_F"))]
    items.sort(key=lambda r: int(r["hang"]))
    for i, r in enumerate(items, 1):
        ngan_rank[r["tu"]] = (ngan, i, len(items))

rows = []
for i, w in enumerate(res, 1):
    k = key(w)
    lab = labels[w]
    x = xh_by.get(w, {})
    src = "L1" if w in p6in else lo.get(w, ("?",))[0]
    p = p1.get(w, {})
    c = oc.get(w, {})
    uv = ungvien.get(w, {})
    sub_n = int(c["sub_be_mat"]) if c else (int(uv["opensub_n"]) if uv else None)
    sub_s = int(c["sub_sach"]) if c else (int(uv["sub_sach"]) if uv else None)
    web_n = int(c["web_be_mat"]) if c else (int(uv["ccaligned_n"]) if uv else None)
    web_s = int(c["web_sach"]) if c else (int(uv["web_sach"]) if uv else None)
    leip = p.get("leipzig_so_cau") if p else (int(uv["leipzig_so_cau"]) if uv else None)
    tato = p.get("tatoeba_so_cau") if p else (int(uv["tatoeba_so_cau"]) if uv else None)
    ngan, nr, nn = ngan_rank.get(w, ("?", "", ""))
    syl = w.split(" ")
    rev = " ".join(reversed(syl)) if len(syl) == 2 else ""
    rev_hit = ("CHINH:" + rev) if rev in main else (("DU_PHONG:" + rev) if rev in res else "")
    kkr = kk.get(w, {})
    luot = (kkr.get("luot_nguon_gan_nhat") or "").split("-")[-1] if kkr.get("luot_nguon_gan_nhat") else ""
    g = gn.get(w)
    rows.append({
        "stt": i, "tu": w, "khoa": k, "so_chu": len(k), "so_khoi": len(syl),
        "lo_nguon": src, "nguon_P1": p.get("nguon") or "",
        "nhan": lab["nhan"], "lop": lab["lop"],
        "lop_O": p6in.get(w, lo.get(w, (None, {}))[1] if w in lo else {}).get("lop_O", ""),
        "lop_A": p6in.get(w, lo.get(w, (None, {}))[1] if w in lo else {}).get("lop_A", ""),
        "phieu_O": ";".join(f'{r["nhan"]}/{r["lop"]}' for r in po.get(w, [])),
        "phieu_A": ";".join(f'{r["nhan"]}/{r["lop"]}' for r in pa.get(w, [])),
        "phan_bien": ";".join(f'{r["ben_phan_doi"]}:{r["cong"]}:{r["ket_qua"]}' for r in pb.get(w, [])),
        "F": f'{float(lab["F"]):.2f}', "G": lab["G"], "T": lab["T"], "diem": f'{float(lab["diem"]):.2f}',
        "T_vung": x.get("T_vung", ""), "phat_h5d": x.get("phat_h5d", ""), "dao_thu_hai": x.get("dao_thu_hai", ""),
        "hang_xep_hang_v2": x.get("hang", ""), "vao_xep_hang_v2": x.get("vao", ""),
        "ngan": ngan, "hang_trong_ngan_P0": nr, "co_ngan_P0": nn,
        "sub_be_mat": sub_n, "sub_sach": sub_s, "web_be_mat": web_n, "web_sach": web_s,
        "sub_ppm_sach": f"{(sub_s or 0) / SUB_TOKENS * 1e6:.3f}", "web_ppm_sach": f"{(web_s or 0) / WEB_TOKENS * 1e6:.3f}",
        "leipzig": leip, "tatoeba": tato, "H8": h8(sub_s, web_s, leip, tato),
        "chu_ky": ";".join(sorted(ck.get(w, []))), "chu_ky_labels": lab["chu_ky_hai_ben"],
        "canh_bao_H7": ";".join(f'{r["doc_khac"]}({r["ppm_gop_doc_khac"]}):{r["trang_thai_9_1"]}' for r in cb.get(w, [])),
        "doc_khac_P1": ";".join(p.get("canh_bao_can_doc") or []) if p else "",
        "cong_P2_khac_PASS": ";".join(gate.get(w, [])),
        "khoa_bi_chan": blocked.get(k, ""),
        "trung_khoa_chinh": main_keys.get(k, ""),
        "ho_chinh_ta": ";".join(fam.get(w, [])), "ho_d6": ";".join(d6fam.get(w, [])),
        "dao_thu_tu_co_mat": rev_hit,
        "giai_nghia": "CO" if g else ("CHUA_VIET" if w in chua_viet else "?"),
        "sha256_giai_nghia": sha(g["giai_nghia"]) if g else "",
        "co_giai_nghia": g["co"] if g else "",
        "luot_viet": luot, "lo_viet": kkr.get("luot_nguon_gan_nhat", ""), "D6": kkr.get("D6", ""),
        "D6_run_id": (kkr.get("run_id") or "")[:12],
        "D7_luot_cuoi": ";".join(reviews.get((luot, w), [])) if luot else "",
    })

header = list(rows[0].keys())
write_tsv(HERE / "du-phong-205-su-kien.tsv", header, rows)
print("ghi", len(rows), "dòng")
print("ngăn:", collections.Counter(r["ngan"] for r in rows))
print("lớp:", collections.Counter(r["lop"] for r in rows))
print("H8:", collections.Counter(r["H8"] for r in rows))
print("giải nghĩa:", collections.Counter(r["giai_nghia"] for r in rows))
print("lượt:", collections.Counter(r["luot_viet"] for r in rows))
print("khóa bị chặn:", [r["tu"] for r in rows if r["khoa_bi_chan"]])
print("trùng khóa chính:", [r["tu"] for r in rows if r["trung_khoa_chinh"]])
print("trùng khóa trong dự phòng:", [k for k, v in collections.Counter(r["khoa"] for r in rows).items() if v > 1])
print("số chữ < 4 hoặc > 12:", [r["tu"] for r in rows if not 4 <= r["so_chu"] <= 12])
print("số khối:", collections.Counter(r["so_khoi"] for r in rows))
print("họ chính tả:", [(r["tu"], r["ho_chinh_ta"]) for r in rows if r["ho_chinh_ta"]])
print("họ D6:", [(r["tu"], r["ho_d6"]) for r in rows if r["ho_d6"]])
print("đảo thứ tự:", [(r["tu"], r["dao_thu_tu_co_mat"]) for r in rows if r["dao_thu_tu_co_mat"]])
print("cảnh báo H7:", [(r["tu"], r["canh_bao_H7"]) for r in rows if r["canh_bao_H7"]])
print("cổng P2 khác PASS:", collections.Counter(r["cong_P2_khac_PASS"] for r in rows))
print("O1 đúng thứ tự:", all(o1(a) < o1(b) for a, b in zip(res, res[1:])))
