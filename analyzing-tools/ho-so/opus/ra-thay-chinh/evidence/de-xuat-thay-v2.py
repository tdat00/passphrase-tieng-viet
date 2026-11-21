"""Mô phỏng thay theo lập trường của Opus sau duyệt nháp vòng 1, lấp ghế từ dự phòng theo hạng S4 đã khóa.

    set HND_DIR=<ngoài repo: Viet11K.txt … Viet74K.txt>
    python de-xuat-thay-v2.py  ->  de-xuat-thay-v2.tsv, de-xuat-thay-v2.log

RA = K0/K1 trong doi-chieu-v2.H7 (gồm 13 khóa Opus nhận K1 sau duyệt nháp) + K1 vòng 1 của Opus chưa bị hạ +
H5_V2_THAY dưới đây (O104 sau thỏa thuận 1).
Chọn từ vào theo vòng lấp của choose() trong ho-so/unified/p6-tinh-doc-lap-astra.py:83–88 (luật P7 "thay bằng
dự phòng", tieu-chi-thong-nhat.md:12, :191, :307): duyệt dự phòng theo hạng S4 đã khóa (xep-hang.tsv, cột hang);
bỏ tầng D, cổng còn mở, họ đang chờ; nhận mục nếu sau khi nhận vẫn F ≤ 77 và R1 ≤ 388 (LIM_F, LIM_R ở dòng 12
của script đó; đếm lại sau mỗi lần nhận) cho tới khi đủ số ghế; 25 mục kế tiếp theo cùng luật là dự bị.
Hai nhánh kiểm: (1) tập ra + các khóa Astra giữ K1 ở thoa-thuan-1.tsv mà Opus giữ K2 (Q-rtc-O1) để đo sức chứa;
(2) tập ra + theo (lớp F) để chứng minh hạn mức F được cập nhật mỗi lần nhận.
Cờ cần đọc của từ vào dùng đúng điều kiện còi đã ký (PPM ≥ 0,3 hoặc ≥ PPM của mục; không thêm ngưỡng r),
cách đọc HND cùng khóa trong từ vựng đỏ, biến thể H5b đúng hợp đồng (vần đúng bằng i hoặc y,
tap-luat-P2-v4.json:575) và đối chứng H5 trong ung-vien-doi-chung-H5.tsv của Astra.
"""
import collections
import importlib.util
import itertools
import unicodedata

from chung import *


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


H5_V2_THAY = {  # từ: lý do (chi tiết ở ho-so/unified/ra-thay-chinh-h5.tsv)
    "chòng chành": "c thiếu dữ liệu", "bồ kết": "c thiếu dữ liệu", "rau dền": "c thiếu dữ liệu",
    "ngoảnh": "c thiếu dữ liệu", "phấp phới": "c thiếu dữ liệu", "già dặn": "c thiếu dữ liệu",
    "dây chun": "c thiếu dữ liệu", "dây thun": "c thiếu dữ liệu", "phí phạm": "c thiếu dữ liệu",
    "lấn át": "lấn áp 13,3% phụ đề", "rầm rầm": "c thiếu dữ liệu (rần rần, enwiktionary rev 89902128)",
    "cải xoong": "f, phụ đề 4 < 20 (dem-h5f.tsv)", "xà bông": "f, 62,6%/92,4% < 95% (dem-h5f.tsv)",
    "xà phòng": "f, 62,6%/92,4% < 95% (dem-h5f.tsv)",
    "co rúm": "Opus: c thiếu dữ liệu; Astra: chờ căn cứ c/d", "xù xì": "như co rúm", "rầm rộ": "như co rúm",
    "chơ vơ": "như co rúm", "xập xình": "như co rúm", "su hào": "như co rúm", "loay hoay": "Opus: c 85% < 95%",
}
GATES_OPEN = {"loằng ngoằng": "CHO_H5", "ngoại trừ": "CHO_H7", "qua quýt": "họ H5 chờ xét"}
TONE = {"\u0300", "\u0301", "\u0303", "\u0309", "\u0323"}


def h5b(w):
    """Hợp đồng H5b (ho-so/unified/tap-luat-P2-v4.json:575): mỗi âm tiết có âm đầu h, k, l, m, qu, s, t và vần đúng
    bằng i hoặc y được đổi i <-> y; sinh mọi tổ hợp khác rỗng của các âm tiết đổi được (ví dụ tỉ mỉ -> tỷ mỉ, tỉ mỷ,
    tỷ mỷ), bỏ nguyên dạng."""
    opts = []
    for s in w.split():
        d = unicodedata.normalize("NFD", s)
        tone = "".join(c for c in d if c in TONE)
        base = unicodedata.normalize("NFC", "".join(c for c in d if c not in TONE))
        alt = None
        for on in ("qu", "h", "k", "l", "m", "s", "t"):
            if base in (on + "i", on + "y"):
                alt = on + unicodedata.normalize("NFC", ("y" if base.endswith("i") else "i") + tone)
                break
        opts.append([s] + ([alt] if alt else []))
    return [" ".join(c) for c in itertools.product(*opts) if " ".join(c) != w]


def chon(cand, n_slot, f_now, r_now, lab_res, n_du_bi=None, r_cap=388):
    """Chọn n_slot mục rồi các mục đủ điều kiện kế tiếp (tối đa n_du_bi) theo thứ tự, kiểm F ≤ 77 và R1 ≤ r_cap sau mỗi
    lần nhận. r_cap = min(388, R1 còn lại + số R1 ra): R1 chỉ thay ghế R1, không thay ghế OK (tieu-chi-thong-nhat.md:407)."""
    vao, bo = [], collections.Counter()
    f, r1 = f_now, r_now
    for r in cand:
        w = r["tu"]
        if r["tang"] == "D":
            bo["tang_D"] += 1
            continue
        if w in GATES_OPEN:
            bo["cong_mo_hoac_ho_cho"] += 1
            continue
        ff = int(r["lop"] == "F")
        rr = int(lab_res.get(w, {}).get("nhan") == "R1")
        if f + ff > 77 or r1 + rr > r_cap:
            bo["vuot_han_muc"] += 1
            continue
        vao.append(r)
        if len(vao) <= n_slot:
            f, r1 = f + ff, r1 + rr
        if n_du_bi is not None and len(vao) >= n_slot + n_du_bi:
            break
    return vao[:n_slot], vao[n_slot:], f, r1, bo


def _tu_kiem():
    """Hai ca do Astra nêu ở lượt duyệt 2 (rd2-audit-summary.json: H5b_combination_missing, R1_to_OK_counterexample)."""
    assert set(h5b("tỉ mỉ")) == {"tỉ mỷ", "tỷ mỉ", "tỷ mỷ"}, h5b("tỉ mỉ")
    assert h5b("qua quýt") == [], h5b("qua quýt")
    r1 = {"tu": "x", "tang": "A", "lop": "C", "ngan": "R1_KHONG_F"}
    vao, _, _, _, _ = chon([r1], 1, 77, 0, {"x": {"nhan": "R1"}}, n_du_bi=0, r_cap=min(388, 0 + 0))
    assert vao == [], "R1 không được thay ghế OK"


def main():
    out_utf8()
    _tu_kiem()
    v2 = load("v2", HERE / "doi-chieu-v2.py")
    h7 = load("h7", HERE / "sang-loc-h7.py")
    dx = load("dx", HERE / "de-xuat-thay.py")
    main_words = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
    lab = {r["tu"]: r for r in rd(AT / "labels.tsv")}
    xh = {r["tu"]: r for r in rd(U / "xep-hang.tsv")}
    res = rd(AT / "du-phong-phan-loai.tsv")
    ra = collections.OrderedDict()
    for r in rd(OUT / "sang-loc-h7.tsv", mine=True):
        if r["de_xuat"] in ("K1_DE_XUAT", "K1_GIAP_RANH"):
            if r["tu_chinh"] in v2.H7 and v2.H7[r["tu_chinh"]][0] not in ("K0", "K1"):
                continue
            ra.setdefault(r["tu_chinh"], set()).add("K1")
    for w, (v, _) in v2.H7.items():
        if v in ("K0", "K1"):
            ra.setdefault(w, set()).add(v)
    for w in H5_V2_THAY:
        ra.setdefault(w, set()).add("H5")
    miss = [w for w in ra if w not in lab or lab[w]["trang_thai"] != "CHINH"]
    assert not miss, miss
    cand = sorted(res, key=lambda r: (int(xh[r["tu"]]["hang"]) if r["tu"] in xh else 10 ** 6, o1(r["tu"])))
    f_main = sum(lab[w]["lop"] == "F" for w in main_words)
    r_main = sum(lab[w]["nhan"] == "R1" for w in main_words)

    def mo_phong(ra_set):
        f0 = f_main - sum(lab[w]["lop"] == "F" for w in ra_set)
        r0 = r_main - sum(lab[w]["nhan"] == "R1" for w in ra_set)
        n_r1_ra = sum(lab[w]["nhan"] == "R1" for w in ra_set)
        vao, du_bi, f1, r1, bo = chon(cand, len(ra_set), f0, r0, lab, r_cap=min(388, r0 + n_r1_ra))
        new = (set(main_words) - set(ra_set)) | {r["tu"] for r in vao}
        keys = {key(w) for w in new}
        return vao, du_bi, f1, r1, bo, len(new), len(keys)

    vao, du_bi, f1, r1, bo, n_new, n_keys = mo_phong(list(ra))
    gia_dinh = list(ra) + ["theo"]
    gv, _, gf, gr, _, gn, gk = mo_phong(gia_dinh)
    s1 = [r["tu_hoac_khoa"].split(" (")[0].strip() for r in rd(AT / "ho-so/astra/ra-thay-chinh/thoa-thuan-1.tsv")
          if r["loai"] == "S1" and r["de_xuat_chung"].startswith("K1")]  # Q-rtc-O1: chủ dự án theo Astra
    nhanh_s1 = list(ra) + [w for w in s1 if w not in ra]
    sv, sd, sf, sr, _, sn, sk = mo_phong(nhanh_s1)
    hnd = collections.defaultdict(set)
    allw = set()
    for ten in ("Viet11K", "Viet22K", "Viet39K", "Viet74K"):
        for l in open(HND_DIR / f"{ten}.txt", encoding="utf-8"):
            w = unicodedata.normalize("NFC", l.strip())
            if w and w == w.lower():
                hnd[key(w)].add(w)
                allw.add(w)
    oc = rd(U / "opus-counts.tsv")
    pu = {r["tu"]: h7.ppm(r) for r in oc if r["vai_tro"] == "UNG_VIEN"}
    dkr = collections.defaultdict(list)
    for r in oc:
        if r["vai_tro"] == "DOC_KHAC":
            dkr[r["khoa"]].append((r["tu"], h7.ppm(r)))
    av5 = collections.defaultdict(list)
    for r in rd(AT / "ho-so/astra/ra-thay-chinh/evidence/ung-vien-doi-chung-H5.tsv"):
        av5[r["tu"]].append(r["bien_the"])

    def co(r):
        w, k, pw = r["tu"], r["khoa"], pu.get(r["tu"], 0.0)
        c7 = [f"{x} {p:.2f}" for x, p in dkr.get(k, []) if p >= 0.3 or p >= pw]
        do = sorted(x for x in hnd.get(k, set()) - {w} if x in dx.RED)
        b5 = [v for v in h5b(w) if v in allw] + av5.get(w, [])
        return "; ".join(filter(None, ["còi H7: " + ", ".join(c7) if c7 else "", "HND đỏ: " + ", ".join(do) if do else "",
                                       "H5: " + ", ".join(b5) if b5 else ""])) or "-"

    rows = []
    for w, codes in ra.items():
        rows.append({"vai_tro": "RA", "thu_tu": "-", "tu": w, "lop": lab[w]["lop"], "ngan": "OK_KHONG_F" if lab[w]["lop"] != "F" else "OK_F",
                     "ma": ";".join(sorted(codes)), "tang": "-", "hang_S4": xh.get(w, {}).get("hang", "-"), "can_doc": "-"})
    for i, r in enumerate(vao + du_bi, 1):
        rows.append({"vai_tro": "VAO" if i <= len(vao) else ("DU_BI" if i <= len(vao) + 25 else "CON_LAI"), "thu_tu": i, "tu": r["tu"], "lop": r["lop"],
                     "ngan": r["ngan"], "ma": r["ma_van_de"], "tang": r["tang"],
                     "hang_S4": xh.get(r["tu"], {}).get("hang", "-"), "can_doc": co(r)})
    write_tsv(HERE / "de-xuat-thay-v2.tsv", list(rows[0].keys()), rows)
    vv = [x for x in rows if x["vai_tro"] == "VAO"]
    con_lai = [r for r in cand if r["lop"] != "F" and r["tang"] != "D" and r["tu"] not in GATES_OPEN]
    log = [f"RA: {len(ra)}; mã: {dict(collections.Counter(c for s in ra.values() for c in s))}; lớp F trong RA: "
           f"{sum(lab[w]['lop'] == 'F' for w in ra)}",
           f"VAO: {len(vao)} (tầng {dict(collections.Counter(r['tang'] for r in vao))}), hạng S4 "
           f"{vv[0]['hang_S4']}–{vv[-1]['hang_S4']}; sau đó còn {len(du_bi)} mục đủ điều kiện (25 đầu là dự bị); bỏ qua: {dict(bo)}",
           f"sau thay: {n_new} từ, {n_keys} khóa, F = {f1}, R1 = {r1}",
           f"nguồn không-F đủ điều kiện sơ bộ (tầng A/C, trừ cổng mở và họ chờ): {len(con_lai)}; còn sau {len(vao)} vào: "
           f"{len(con_lai) - len(vao)}",
           f"nhánh giả định thêm 'theo' (lớp F) vào RA: {len(gia_dinh)} ra, {len(gv)} vào, sau thay {gn} từ, {gk} khóa, "
           f"F = {gf}, R1 = {gr}",
           f"nhánh Q-rtc-O1 theo Astra (thêm {len(nhanh_s1) - len(ra)} khóa): {len(nhanh_s1)} ra, {len(sv)} vào, "
           f"còn {len(sd)}, sau thay {sn} từ, {sk} khóa, F = {sf}, R1 = {sr}; hạng S4 vào cuối "
           f"{xh.get(sv[-1]['tu'], {}).get('hang', '-') if sv else '-'}",
           f"cờ cần đọc trong VAO: {sum(x['can_doc'] != '-' for x in vv)}",
           "VAO: " + ", ".join(x["tu"] for x in vv), "DU_BI: " + ", ".join(r["tu"] for r in du_bi[:25]), "CON_LAI: " + ", ".join(r["tu"] for r in du_bi[25:])]
    (HERE / "de-xuat-thay-v2.log").write_text("\r\n".join(x.rstrip() for x in log) + "\r\n", encoding="utf-8", newline="")
    print("\n".join(log[:7]))


if __name__ == "__main__":
    main()
