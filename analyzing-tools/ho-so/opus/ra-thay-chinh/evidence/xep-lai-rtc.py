"""Tính lại S2/S3/S4 một lần theo P6 trên tập ra cuối (T-rtc-14), chương trình của Opus (T7).

Dùng lại các hàm chấm của chương trình P6 của Opus (ho-so/opus/p4/p6_opus.py). Bước 1 tái lập đúng
xep-hang.tsv (F sáu chữ số thập phân và thứ tự); bước 2 bỏ khỏi rổ chấm các mục không còn qua H1–H9, chấm lại,
rồi xếp hàng đợi từ vào: 118 dự phòng dùng được (116 vào, 2 dự bị), sau đó 25 HM đã thống nhất (T-rtc-19).
Mục trượt D6/D7 ở P7 vẫn ở rổ chấm, chỉ bị bỏ lúc chọn (T-rtc-14). Chế độ phụ (bỏ mọi mục LOAI cũ) chỉ để đo độ nhạy.

Chạy: python -X utf8 -B xep-lai-rtc.py  ->  xep-lai-rtc.tsv, xep-lai-rtc.log
"""
import importlib.util
from collections import defaultdict

from chung import AT, HERE, U, counts_opus, out_utf8, p1_table, rd, write_lines, write_tsv

out_utf8()
A = AT / "ho-so" / "astra" / "ra-thay-chinh"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


p6 = load("p6_opus", AT / "ho-so" / "opus" / "p4" / "p6_opus.py")
dx = load("dx2", HERE / "de-xuat-thay-v2.py")

xh = rd(U / "xep-hang.tsv")
COT = ("sub_sach", "web_sach", "leipzig_so_cau", "tatoeba_so_cau")
counts = {}  # sub/web: opus-counts.tsv (UNG_VIEN); Leipzig/Tatoeba: bảng khóa chung (ho-so/discussion); lô L2/L3: tệp ứng viên
l2 = {}
for f in ("l2-ung-vien.tsv", "l2b-ung-vien.tsv", "l2c-ung-vien.tsv", "l2d-ung-vien.tsv", "l3-ung-vien.tsv"):
    for r in rd(U / f):
        l2[r["tu"]] = {k: int(r[k]) for k in COT}
co, p1 = counts_opus(), p1_table()
for r in xh:
    w = r["tu"]
    c = dict(l2.get(w, {}))
    if w in co:
        c["sub_sach"], c["web_sach"] = int(co[w]["sub_sach"]), int(co[w]["web_sach"])
    if w in p1 and p1[w].get("leipzig_so_cau") is not None:
        c["leipzig_so_cau"], c["tatoeba_so_cau"] = int(p1[w]["leipzig_so_cau"]), int(p1[w]["tatoeba_so_cau"])
    assert set(COT) <= set(c), w
    counts[(r["khoa"], w)] = c
base = {}
for r in xh:
    c = counts[(r["khoa"], r["tu"])]
    base[r["tu"]] = dict(khoa=r["khoa"], nhan=r["nhan"], lop=r["lop"], phat=int(r["phat_h5d"]),
                         sub=c["sub_sach"], web=c["web_sach"], L=c["leipzig_so_cau"], T=c["tatoeba_so_cau"])


def cham(ws):
    """Chấm S2/S3/S4 như p6_opus.main() trên tập ws; trả về (thứ tự, dict điểm)."""
    pool = {w: dict(base[w]) for w in ws}
    groups = defaultdict(list)
    for w in pool:
        groups[len(w.split(" "))].append(w)
    for g in groups.values():
        cols = [p6.percentiles([pool[w][f] for w in g]) for f in ("sub", "web", "L", "T")]
        for i, w in enumerate(g):
            pool[w]["F"] = sum(col[i] for col in cols) / 4
    for w, it in pool.items():
        it["co_so"] = it["F"] + p6.GVAL[it["lop"]]
    for w, it in pool.items():
        parts = w.split(" ")
        rev = " ".join(reversed(parts))
        second = False
        if len(parts) == 2 and rev != w and rev in pool:
            o = pool[rev]
            second = it["co_so"] < o["co_so"] or (it["co_so"] == o["co_so"] and p6.o1_key(w) > p6.o1_key(rev))
        it["T_all"] = p6.regional_risk(w) + 5 * it["phat"] + 5 * (len(p6.fold(w)) > 10) + 3 * (len(parts) == 3) + 5 * second
        it["diem100"] = p6.round2(it["co_so"] - it["T_all"])
    order = sorted(pool, key=lambda w: (pool[w]["nhan"] != "OK", -pool[w]["diem100"], len(p6.fold(w)), p6.o1_key(w)))
    return order, pool


# Bước 1: tái lập xep-hang.tsv.
order0, pool0 = cham(list(base))
assert order0 == [r["tu"] for r in xh], "không tái lập được thứ tự xep-hang.tsv"
assert all(f"{float(pool0[r['tu']]['F']):.6f}" == r["F"] for r in xh), "không tái lập được F"
assert all(pool0[r["tu"]]["diem100"] == int(r["diem_100"]) for r in xh)

# Bước 2: rổ chấm sau đợt này.
tt = rd(U / "ra-thay-chinh-thay-the.tsv")
ra = {r["tu"] for r in tt if r["vai_tro"] == "RA"}
dung_duoc = [r["tu"] for r in tt if r["vai_tro"] in ("VAO", "DU_BI")]  # 118 dự phòng dùng được, theo hạng đã khóa
hm = [r["tu"] for r in tt if r["vai_tro"] == "HM"]
pl = rd(AT / "du-phong-phan-loai.tsv")
tang_d = {r["tu"] for r in pl if r.get("tang") == "D"}
loai_cu = {r["tu"]: r["cong_loai"] for r in rd(AT / "nguon-goc-giai-nghia.tsv") if r["trang_thai"] == "LOAI"}
loai_h = {w for w, c in loai_cu.items() if not c.startswith(("D6", "D7"))}
khong_qua_h = set(dx.GATES_OPEN) | set(dx.KHONG_VAO_1) | {"cơ quan"} | tang_d
assert len(ra) == 116 and len(dung_duoc) == 118 and len(hm) == 25 and len(tang_d) == 6
assert ra <= set(base) and set(dung_duoc) <= set(base) and set(hm) <= set(base)
log = [f"tái lập xep-hang.tsv: {len(xh)} mục, thứ tự và F khớp",
       f"bỏ khỏi rổ chấm: {len(ra)} từ ra; {len(loai_h & set(base))} mục LOAI vì cổng H ({sorted(loai_h & set(base))}); "
       f"{len(khong_qua_h & set(base))} mục không qua H1–H9 ở đợt này ({sorted(khong_qua_h & set(base))})"]
ket_qua = {}
for che_do, bo in (("T-rtc-14", ra | loai_h | khong_qua_h), ("PHU_BO_MOI_LOAI_CU", ra | set(loai_cu) | khong_qua_h)):
    ro = [w for w in base if w not in bo]
    order, pool = cham(ro)
    hang = {w: i for i, w in enumerate(order, 1)}
    hang_doi = sorted(dung_duoc, key=hang.get)
    vao, du_bi = hang_doi[:116], hang_doi[116:]
    hm_moi = sorted(hm, key=hang.get) if all(w in hang for w in hm) else []  # chế độ phụ bỏ cả HM (LOAI D6/D7 cũ)
    ket_qua[che_do] = (vao, du_bi, hm_moi, hang, pool)
    doi_cho = sum(a != b for a, b in zip(dung_duoc, hang_doi))
    log.append(f"{che_do}: rổ {len(ro)} mục; tập vào {'giống' if set(vao) == set(dung_duoc[:116]) else 'khác'} bản sơ bộ "
               f"(vào thêm {sorted(set(vao) - set(dung_duoc[:116]))}, ra khỏi tập vào {sorted(set(dung_duoc[:116]) - set(vao))}); "
               f"{doi_cho}/118 vị trí đổi; dự bị {du_bi}; thứ tự HM đổi "
               + (f"{sum(a != b for a, b in zip(hm, hm_moi))}/25" if hm_moi else "(HM không ở rổ chấm)"))
vao, du_bi, hm_moi, hang, pool = ket_qua["T-rtc-14"]
hm_ok = [r["tu"] for r in rd(AT / "honorable-mentions.tsv") if r["nhan_ho_so"] == "OK" and r["lop"] != "F"
         and r["tu"] not in khong_qua_h]
top25 = sorted(hm_ok, key=hang.get)[:25]
log.append(f"25 HM OK không-F đứng đầu theo S4 mới (bỏ mục không qua H1–H9): "
           f"{'trùng' if top25 == hm_moi else 'khác'} danh sách đã thống nhất; mục 26: {sorted(hm_ok, key=hang.get)[25]}")
cu = {r["tu"]: r for r in xh}
rows = []
for vai, ws in (("VAO", vao), ("DU_BI", du_bi), ("HM", hm_moi)):
    for i, w in enumerate(ws, 1):
        rows.append({"vai_tro": vai, "thu_tu": i, "tu": w, "khoa": base[w]["khoa"], "lop": base[w]["lop"],
                     "hang_cu": cu[w]["hang"], "diem_100_cu": cu[w]["diem_100"], "hang_moi": hang[w],
                     "diem_100_moi": pool[w]["diem100"],
                     "thu_tu_so_bo": (dung_duoc.index(w) + 1) if w in dung_duoc else hm.index(w) + 1})
write_tsv(HERE / "xep-lai-rtc.tsv", list(rows[0].keys()), rows)
same = all(set(ket_qua[k][0]) == set(vao) for k in ket_qua)
log.append(f"hai chế độ cho cùng tập vào: {same}")
write_lines(HERE / "xep-lai-rtc.log", log)
print("\n".join(log))
