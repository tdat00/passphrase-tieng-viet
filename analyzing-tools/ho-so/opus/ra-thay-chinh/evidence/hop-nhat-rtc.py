"""Hợp nhất phiếu hai SA sau duyệt nháp vòng 1 (ra-thay-chinh): bảng H7 theo khóa, H5 theo cặp, bảng thay.

    set HND_DIR=<ngoài repo>; python de-xuat-thay-v2.py      (chạy trước; cần HND)
    python hop-nhat-rtc.py  ->  ho-so/unified/ra-thay-chinh-h7.tsv, -h5.tsv, -thay-the.tsv; hop-nhat-rtc.log

A = ho-so/astra/ra-thay-chinh, E = A/evidence, O = ho-so/opus/ra-thay-chinh.
- Phiếu hiện hành của Astra: phiếu sau duyệt nháp (E/rd1-*). Khóa/cặp không có trong rd1 thì dùng phiếu sau rà chéo
  (E/cr1-*), rồi phiếu v1 (A/h7-sang-loc-*, A/h5-sang-loc-*, E/cr1-H5b-hop-dong.tsv).
- Phiếu hiện hành của Opus: doi-chieu-v2.py (H7, H5), rồi O/evidence/doi-chieu-h7.tsv, doi-chieu-h5.tsv (ảnh lúc rà
  chéo), rồi O/sang-loc-h5.tsv.
- Mọi mã được ánh xạ bằng bảng đầy đủ; mã lạ làm script dừng (không dò chuỗi con trong mã). Cột nguon_* ghi tệp:dòng.
- Số H5 của cặp f lấy tổng các dạng phân cách trong evidence/dem-h5f.tsv (tieu-chi-thong-nhat.md:127).
Trạng thái là ghép máy móc hai phiếu, không phải chữ ký.
"""
import collections
import importlib.util
import re
import statistics

from chung import *

A = AT / "ho-so" / "astra" / "ra-thay-chinh"
E = A / "evidence"
SEV = {"K0": 6, "K1": 5, "CHO": 4, "K2": 3, "K2_DA_KY": 2, "GIU": 1, "GIU_QD_CHU": 1, "KHONG_DO": 1, "-": 0}
H7_V1 = {"K0": "K0", "K1": "K1", "K2_DE_NGHI_KHONG_CHAN": "K2", "CHO_NGHIA": "CHO", "CHO_DO": "CHO",
         "KHONG_DO": "KHONG_DO", "DA_CO_PHAN_XU": "K2_DA_KY", "CUNG_MAT_CHU_KHAC_KHOANG": "KHONG_DO"}
H7_CR1_SUA = {"BAO_LUU_K2_CU_CHO_PHAM_VI_BI_NH": "K2_DA_KY", "DE_NGHI_K1_KHONG_CHOT_K0": "K1",
              "CHO_PHAN_XU_H6_H7": "CHO", "DE_NGHI_K2_KHONG_TU_DONG": "K2", "CHO_PHAN_XU_H7": "CHO",
              "GIU_THEO_QUYET_DINH_CHU": "GIU_QD_CHU", "GIU_CHU_KY_K2_CU": "K2_DA_KY", "DE_NGHI_K1": "K1"}
H7_CR1_TL = {"DONG_Y_HUONG_KHONG_TU_DONG_THEO_NGHIA": "K2", "DONG_Y_CACH_DOC_NAY_CHUA_DONG_TOAN_KHOA": "CHO",
             "CAN_PHAN_XU_THEO_BAN_SUA_A": "CHO", "CAN_THEM_CAN_CU_TRUOC_KY": "CHO", "CHUA_DONG_Y_KY_K2": None}
H7_RD1 = {"NHAN_HUONG_GIU_H7": "GIU", "GIU_PHAN_DOI_K1": "K1", "NHAN_K2_CU": "K2_DA_KY", "NHAN_K1": "K1",
          "BAO_LUU_K1": "K1", "GIU_CHU_KY_CU": "K2_DA_KY", "TT1_K1": "K1", "TT1_K2": "K2",
          "NHAN_K2": "K2", "GIU_CHU_KY_CU_RUT_OI": "K2_DA_KY"}
H5_A = {
    "QUA_H5b_theo_so": "QUA", "NHAN_QUA_H5c_THEO_SO": "QUA", "NHAN_QUA_SO_NHUNG_SUA_LOAI_c": "QUA", "NHAN_QUA_CU": "QUA",
    "KHAC_TU": "KHAC_TU", "NHAN_KHAC_TU": "KHAC_TU", "TEN_RIENG_BI_HA_CHU": "KHAC_TU",
    "DE_NGHI_LOAI_H5C": "THAY", "GIU_DE_NGHI_LOAI_H5c": "THAY", "NHAN_LOAI_H5c": "THAY",
    "NHAN_KHONG_PHAT_HANH_CHO_MA_LOAI": "THAY", "DE_NGHI_THAY_H5c_MOI": "THAY",
    "CHO_XAC_NHAN_QUAN_HE": "CHO", "CUNG_TU_CHO_DO": "CHO", "CHUA_DONG_KY": "CHO", "CHO_H5f_DU_DANG_PHAN_CACH": "CHO",
    "RUT_LOAI_THEO_H5b_CHO_HO_RIENG": "CHO", "TU_CHOI_LY_DO_KY_HIEN_TAI": "CHO", "GIU_CHO_NHAN_DIEN": "CHO",
    "CHO_LOAI_c_d": "CHO", "NHAN_QUAN_HE_f_CHO_DO": "CHO", "CUNG_DANH_TU_CHO_DO_NGHIA": "CHO", "KHONG_THUOC_b": "CHO",
    "DA_PHAN_XU": "DA_PHAN_XU", "NHAN_THAY_H5f": "THAY", "BAO_LUU_CHO_LOAI": "CHO", "TT1_CHO_LOAI_THAY": "THAY",
}
H5_O = {"THAY": "THAY", "THAY_CHO_LOAI": "THAY", "CUNG_TU_QUA": "QUA", "KHONG": "KHAC_TU", "CHO_H5e": "CHO", "CHO_HO_C": "CHO", "KHONG_CHO_VAO": "KHONG_CHO_VAO"}


def rdn(path, mine=False):
    """Đọc TSV kèm số dòng (dòng tiêu đề là 1)."""
    return [(i, r) for i, r in enumerate(rd(path, mine), 2)]


def ref(path, n):
    return f"{path.relative_to(AT).as_posix()}:{n}"


def sach(s):
    return " ".join(str(s or "-").replace("\t", " ").split()) or "-"


def ma(table, code, where):
    if code not in table:
        raise SystemExit(f"Mã lạ {code!r} ở {where}")
    return table[code]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def nhom7(v):
    return {"K0": "THAY", "K1": "THAY", "CHO": "CHO"}.get(v, "GIU")


def trang7(ov, ah):
    go, ga = nhom7(ov), nhom7(ah)
    if go == ga == "THAY":
        return "DONG_THUAN_THAY"
    if "THAY" in (go, ga):
        return "TRANH_CHAP_ASTRA_CHO" if ga == "CHO" else "TRANH_CHAP"
    if ga == "CHO":
        return "CHO_CAN_CU"
    if "K2_DA_KY" in (ov, ah):
        return "GIU_CHU_KY_CU"
    if ah == "GIU_QD_CHU":
        return "GIU_QUYET_DINH_CHU"
    if "K2" in (ov, ah):
        return "DONG_THUAN_GIU_CAN_KY_K2"
    return "DONG_THUAN_GIU"


def trang5(og, ag, acode):
    if ag == "-":
        return "CHI_OPUS"
    if acode == "TT1_CHO_LOAI_THAY" and og == "THAY":
        return "DONG_THUAN_THAY_CHO_LOAI"
    if acode == "NHAN_QUAN_HE_f_CHO_DO":
        return "DO_XONG_CHO_ASTRA_XAC_NHAN" if og == "THAY" else "CHO_DO"
    if og == ag == "CHO":
        return "CHO_CAN_CU"
    if og == ag:
        return "DONG_THUAN_" + og
    if ag == "DA_PHAN_XU":
        return "DA_PHAN_XU_OPUS_" + og
    if acode in ("CHO_LOAI_c_d", "BAO_LUU_CHO_LOAI"):
        return "TRANH_CHAP"
    if "CHO" in (og, ag):
        return "CHO_CAN_CU"
    return "TRANH_CHAP"


def main():
    out_utf8()
    v2 = load("v2", HERE / "doi-chieu-v2.py")
    h7m = load("h7", HERE / "sang-loc-h7.py")
    lab = {r["tu"]: r for r in rd(AT / "labels.tsv")}
    main_words = {l.split("|")[0] for l in lines(AT / "wordlist.txt")}
    v2src = (HERE / "doi-chieu-v2.py").read_text(encoding="utf-8").splitlines()
    dong7, dong5 = {}, {}  # dòng cuối cùng gán phiếu (lệnh gán sau đè lệnh trước)
    for n, line in enumerate(v2src, 1):
        for mm in re.finditer(r'(?:^|[{,\s])"([^"]+)":', line):
            dong7[mm.group(1)] = n
        for mm in re.finditer(r'H7\["([^"]+)"\]', line):
            dong7[mm.group(1)] = n
        for mm in re.finditer(r'\("([^"]+)", "([^"]+)"\)', line):
            dong5[(mm.group(1), mm.group(2))] = n
    v2ref = "ho-so/opus/ra-thay-chinh/evidence/doi-chieu-v2.py"
    # ---- H7
    o7 = {r["tu_chinh"]: (i, r) for i, r in rdn(HERE / "doi-chieu-h7.tsv", mine=True)}
    av1 = collections.defaultdict(list)
    for f in (A / "h7-sang-loc-1177.tsv", A / "h7-sang-loc-bo-sung.tsv"):
        for i, r in rdn(f):
            av1[r["tu_chinh"]].append((ma(H7_V1, r["muc_K_de_xuat"], ref(f, i)), ref(f, i), r))
    sua = {r["tu"]: (i, r) for i, r in rdn(E / "cr1-Astra-sua-H7.tsv")}
    tl = {r["tu"]: (i, r) for i, r in rdn(E / "cr1-Astra-tra-loi-96-K2.tsv")}
    px = {r["tu"]: (i, r) for i, r in rdn(E / "rd1-H7-phan-xu.tsv")}
    bs = {r["tu"]: (i, r) for i, r in rdn(E / "rd1-H7-bo-sung.tsv")}
    bl = {r["tu"]: (i, r) for i, r in rdn(E / "rd2-H7-bao-luu.tsv")}
    kd = {r["tu"]: (i, r) for i, r in rdn(E / "rd2-K2-da-ky.tsv")}
    tt1 = [(i, r) for i, r in rdn(A / "thoa-thuan-1.tsv")]  # thỏa thuận 1 của Astra (D-rtc-5)
    tt7 = {r["tu_hoac_khoa"].split(" (")[0].split(" / ")[0].strip(): (i, r) for i, r in tt1 if r["loai"] == "S1"}
    tt5 = {r["tu_hoac_khoa"].split(" (")[0].split(" / ")[0].strip(): (i, r) for i, r in tt1 if r["loai"] == "S2"}
    rows7 = []
    for w in sorted(set(o7) | set(sua) | set(tl) | set(px) | set(bs), key=o1):
        if w not in main_words:
            continue
        oi, o = o7.get(w, (None, None))
        if w in v2.H7:
            ov, ly_o, n_o = v2.H7[w][0], v2.H7[w][1], f"{v2ref}:{dong7[w]}"
        else:
            ov = o["opus_v2"] if o and o["opus_v2"] != "-" else "KHONG_DO"
            ly_o = o["ly_do_opus_v2"] if o else "-"
            n_o = ref(HERE / "doi-chieu-h7.tsv", oi) if o else "-"
        rs = av1.get(w, [])
        top = max(rs, key=lambda t: SEV[t[0]], default=("-", "-", None))
        a1, n_a, ly_a = top[0], top[1], (top[2]["ly_do"] if top[2] else "-")
        acr = "-"
        if w in sua:
            i, r = sua[w]
            acr = ma(H7_CR1_SUA, r["A_sau_ra_cheo"], ref(E / "cr1-Astra-sua-H7.tsv", i))
            n_a, ly_a = ref(E / "cr1-Astra-sua-H7.tsv", i), r["ly_do"]
        elif w in tl:
            i, r = tl[w]
            m = ma(H7_CR1_TL, r["A_phan_hoi"], ref(E / "cr1-Astra-tra-loi-96-K2.tsv", i))
            if m is not None:
                acr = m
                n_a = ref(E / "cr1-Astra-tra-loi-96-K2.tsv", i)
                ly_a = r["A_phan_hoi"] + ": " + r["ly_do_cu_the_cho_cach_doc_co_the_khong_chan"]
        ah = acr if acr != "-" else a1
        if w in px:
            i, r = px[w]
            ah = ma(H7_RD1, r["Astra_duyet_nhap"], ref(E / "rd1-H7-phan-xu.tsv", i))
            n_a = ref(E / "rd1-H7-phan-xu.tsv", i)
            ly_a = f"{r['Astra_duyet_nhap']}: {r['ly_do_Astra']} | số: {r['doi_chung_so']}"
        elif w in bs:
            i, r = bs[w]
            ah = ma(H7_RD1, r["Astra_duyet_nhap"], ref(E / "rd1-H7-bo-sung.tsv", i))
            n_a, ly_a = ref(E / "rd1-H7-bo-sung.tsv", i), f"{r['Astra_duyet_nhap']}: {r['ly_do']}"
        if w in bl:
            i, r = bl[w]
            ah = ma(H7_RD1, r["Astra_duyet_2"], ref(E / "rd2-H7-bao-luu.tsv", i))
            n_a = f"{ref(E / 'rd2-H7-bao-luu.tsv', i)}; lý do: {n_a}"
        if w in kd:
            i, r = kd[w]
            code = r["action_Astra"].split(";")[0].strip()
            ah = ma(H7_RD1, code, ref(E / "rd2-K2-da-ky.tsv", i))
            chu_ky = r["signature_rows"].replace("\\", "/").replace("analyzing-tools/", "")
            n_a, ly_a = ref(E / "rd2-K2-da-ky.tsv", i), f"{r['action_Astra']} | chữ ký: {chu_ky}"
        if w in tt7:
            i, r = tt7[w]
            code = "TT1_" + r["de_xuat_chung"].split(";")[0].strip()
            ah = ma(H7_RD1, code, ref(A / "thoa-thuan-1.tsv", i))
            n_a, ly_a = f"{ref(A / 'thoa-thuan-1.tsv', i)}; trước đó: {n_a}", f"{r['de_xuat_chung']}: {r['ly_do']}"
        rows7.append({"khoa": key(w), "tu_chinh": w, "lop": lab[w]["lop"], "opus": ov, "astra": ah,
                      "trang_thai": trang7(ov, ah), "opus_v1": (o["opus_v1"] if o else "-") or "-", "astra_v1": a1,
                      "astra_cr1": acr, "nguon_opus": n_o, "nguon_astra": n_a, "ly_do_opus": sach(ly_o),
                      "ly_do_astra": sach(ly_a)})
    write_tsv(U / "ra-thay-chinh-h7.tsv", list(rows7[0].keys()), rows7)
    c7 = collections.Counter(r["trang_thai"] for r in rows7)
    # ---- H5
    o5 = {(r["tu"], r["bien_the"]): (i, r) for i, r in rdn(HERE / "doi-chieu-h5.tsv", mine=True)}
    m5 = {(r["tu"], r["bien_the"]): (i, r) for i, r in rdn(OUT / "sang-loc-h5.tsv", mine=True)}
    a5 = {}
    for f in (A / "h5-sang-loc-632.tsv", A / "h5-sang-loc-bo-sung.tsv"):
        for i, r in rdn(f):
            a5[(r["tu"], r["bien_the"])] = (r["ket_qua"], ref(f, i), r["ly_do"])
    for i, r in rdn(E / "cr1-H5b-hop-dong.tsv"):
        code = r["ket_luan"].split(";")[0]
        a5.setdefault((r["tu"], r["bien_the"]), (code, ref(E / "cr1-H5b-hop-dong.tsv", i), r["ket_luan"]))
    for i, r in rdn(E / "cr1-Astra-sua-H5.tsv"):
        a5[(r["tu"], r["bien_the"])] = (r["A_sau_ra_cheo"], ref(E / "cr1-Astra-sua-H5.tsv", i), r["ly_do"])
    rd1p = set()
    for f, col in ((E / "rd1-H5-phan-xu.tsv", "ly_do"), (E / "rd1-H5-quan-he-bo-sung.tsv", "ly_do")):
        for i, r in rdn(f):
            p = (r["tu"], r["doi_chung"])
            a5[p] = (r["Astra_duyet_nhap"], ref(f, i), r[col])
            rd1p.add(p)
    for f in (E / "rd2-H5-xac-nhan.tsv", E / "rd2-H5-bao-luu.tsv"):
        for i, r in rdn(f):
            p = (r["tu"], r["doi_chung"])
            truoc = a5.get(p, ("-", "-", "-"))
            a5[p] = (r["Astra_duyet_2"], ref(f, i) + (f"; lý do: {truoc[1]}" if truoc[1] != "-" else ""),
                     r.get("ly_do") or truoc[2])
            rd1p.add(p)
    for p in list(a5):
        if p[0] in tt5 and a5[p][0] in ("BAO_LUU_CHO_LOAI", "CHO_LOAI_c_d"):
            i, r = tt5[p[0]]
            a5[p] = ("TT1_CHO_LOAI_THAY", f"{ref(A / 'thoa-thuan-1.tsv', i)}; trước đó: {a5[p][1]}", f"{r['de_xuat_chung']}: {r['ly_do']}")
    h5f = {r["dang"]: r for r in rd(HERE / "dem-h5f.tsv", mine=True)}
    sf = {}  # tách các dạng ' / ' của họ đã đăng ký (C5 so nguyên ô nên không tự tách)
    for i, r in rdn(AT / "spelling_families.tsv"):
        for c in r["chuan"].split(" / "):
            for b in r["bien_the"].split(" / "):
                sf.setdefault((c, b), (i, r))

    def so_f(w):
        s = w.split()
        fs = {w, "-".join(s), "".join(s)}
        if len(s) < 2 or not fs <= h5f.keys():
            return None
        return (sum(int(h5f[x]["sub_moi_dong_sach"]) for x in fs), sum(int(h5f[x]["web_dong_khac_sach"]) for x in fs))

    keys5 = set(o5) | set(v2.H5) | rd1p | {p for p, (i, r) in m5.items() if r["hanh_dong"] != "GIU"} | \
        {p for p in a5 if a5[p][1].startswith("ho-so/astra/ra-thay-chinh/evidence/cr1-Astra-sua")}
    rows5 = []
    for p in sorted(keys5, key=lambda t: (o1(t[0]), o1(t[1]))):
        mi, m = m5.get(p, (None, {}))
        if p in v2.H5:
            ov, ly_o, n_o = v2.H5[p][0], v2.H5[p][1], f"{v2ref}:{dong5[p]}"
        elif p in o5:
            oi, o = o5[p]
            ov, ly_o, n_o = o["opus_v2"], o["ly_do_opus_v2"], ref(HERE / "doi-chieu-h5.tsv", oi)
        else:
            ov = {"THAY": "THAY", "DANG_KY_QUA": "CUNG_TU_QUA", "DA_THAY_VI_H7": "CUNG_TU_QUA"}.get(m.get("hanh_dong"), "KHONG")
            ly_o, n_o = m.get("ly_do", "-"), ref(OUT / "sang-loc-h5.tsv", mi) if mi else "-"
        og = ma(H5_O, ov, f"Opus {p}")
        acode, n_a, ly_a = a5.get(p, ("-", "-", "-"))
        ag = ma(H5_A, acode, f"Astra {p}") if acode != "-" else "-"
        so = {"sub_tu": m.get("sub_tu", "-"), "sub_bien_the": m.get("sub_bien_the", "-"),
              "web_tu": m.get("web_tu", "-"), "web_bien_the": m.get("web_bien_the", "-"),
              "nguon_so": ref(OUT / "sang-loc-h5.tsv", mi) if mi else "-"}
        f1, f2 = so_f(p[0]), so_f(p[1])
        if f1 and f2:
            so = {"sub_tu": f1[0], "sub_bien_the": f2[0], "web_tu": f1[1], "web_bien_the": f2[1],
                  "nguon_so": "ho-so/opus/ra-thay-chinh/evidence/dem-h5f.tsv (cộng dạng cách, gạch nối, viết liền)"}
        if p in sf:
            i, r = sf[p]
            so = {"sub_tu": r["sub_chuan"], "sub_bien_the": r["sub_bien_the"], "web_tu": r["web_chuan"],
                  "web_bien_the": r["web_bien_the"], "nguon_so": f"spelling_families.tsv:{i} (họ đã đăng ký, {r['ket_luan']})"}
        rows5.append({"tu": p[0], "bien_the": p[1], "trong_chinh": "CO" if p[0] in main_words else "KHONG", **so,
                      "opus": og, "astra": ag, "astra_ma": acode, "trang_thai": trang5(og, ag, acode),
                      "nguon_opus": n_o, "nguon_astra": n_a, "ly_do_opus": sach(ly_o), "ly_do_astra": sach(ly_a)})
    write_tsv(U / "ra-thay-chinh-h5.tsv", list(rows5[0].keys()), rows5)
    c5 = collections.Counter(r["trang_thai"] for r in rows5)
    # ---- Bảng thay
    st7 = {r["tu_chinh"]: r["trang_thai"] for r in rows7}
    st5 = collections.defaultdict(set)
    for r in rows5:
        if r["opus"] == "THAY" and r["trong_chinh"] == "CO":
            st5[r["tu"]].add(r["trang_thai"])

    def trang_ra(w):
        s = {st7[w]} if w in st7 and st7[w] in ("DONG_THUAN_THAY", "TRANH_CHAP") else set()
        s |= st5.get(w, set())
        if not s or s <= {"DONG_THUAN_THAY"}:
            return "DONG_THUAN"
        if s <= {"DONG_THUAN_THAY", "DONG_THUAN_THAY_CHO_LOAI"}:
            return "DONG_THUAN_CHO_LOAI"
        if "TRANH_CHAP" in s:
            return "TRANH_CHAP_S2" if w in st5 and "TRANH_CHAP" in st5[w] else "TRANH_CHAP"
        if "DO_XONG_CHO_ASTRA_XAC_NHAN" in s:
            return "DO_XONG_CHO_XAC_NHAN"
        return "/".join(sorted(s))

    d2 = rd(HERE / "de-xuat-thay-v2.tsv", mine=True)
    ra = [r for r in d2 if r["vai_tro"] == "RA"]
    vao = [r for r in d2 if r["vai_tro"] != "RA"]
    thu = {"DONG_THUAN": 0, "DONG_THUAN_CHO_LOAI": 1, "DO_XONG_CHO_XAC_NHAN": 2, "TRANH_CHAP_S2": 3}
    ra.sort(key=lambda r: (thu.get(trang_ra(r["tu"]), 3), o1(r["tu"])))
    ra_set = {r["tu"] for r in ra}
    s1 = [(tt7[r["tu_chinh"]][0], {"tu": r["tu_chinh"]}) for r in rows7 if r["trang_thai"] == "TRANH_CHAP" and r["tu_chinh"] not in ra_set]
    rows_t = []
    for r in ra:
        rows_t.append({"vai_tro": "RA", "thu_tu": "-", "tu": r["tu"], "lop": r["lop"], "ngan": r["ngan"], "ma": r["ma"],
                       "trang_thai": trang_ra(r["tu"]), "hang_S4": r["hang_S4"], "tang": "-", "can_soat": "-"})
    for i, r in s1:
        rows_t.append({"vai_tro": "RA_NEU_CHU_DU_AN_THEO_ASTRA", "thu_tu": "-", "tu": r["tu"], "lop": lab[r["tu"]]["lop"],
                       "ngan": "OK_KHONG_F" if lab[r["tu"]]["lop"] != "F" else "OK_F", "ma": "K1 (Astra)",
                       "trang_thai": "CHU_DU_AN_QUYET_Q-rtc-O1", "hang_S4": "-", "tang": "-",
                       "can_soat": ref(A / "thoa-thuan-1.tsv", i)})
    for r in vao:
        rows_t.append({"vai_tro": r["vai_tro"], "thu_tu": r["thu_tu"], "tu": r["tu"], "lop": r["lop"], "ngan": r["ngan"],
                       "ma": r["ma"], "trang_thai": "CAN_DOC" if r["can_doc"] not in ("-", "") else "SO_BO_DAT",
                       "hang_S4": r["hang_S4"], "tang": r["tang"], "can_soat": r["can_doc"] or "-"})
    write_tsv(U / "ra-thay-chinh-thay-the.tsv", list(rows_t[0].keys()), rows_t)
    ct = collections.Counter(r["trang_thai"] for r in rows_t if r["vai_tro"] == "RA")
    moi = [r["tu"] for r in vao]
    oc = rd(U / "opus-counts.tsv")
    pu = {}  # như screen_core.load() của Astra: UNG_VIEN trước, rồi dòng bất kỳ của opus-counts, rồi l2/l2b/l2c/l3
    for r in oc:
        if r["vai_tro"] == "UNG_VIEN" or r["tu"] not in pu:
            pu[r["tu"]] = h7m.ppm(r)
    for s in ("l2", "l2b", "l2c", "l3"):
        for r in rd(U / f"{s}-ung-vien.tsv"):
            pu.setdefault(r["tu"], h7m.ppm(r))

    def trung_vi(ws):
        v = [pu[w] for w in ws if w in pu]
        return f"{statistics.median(v):.9f} (n = {len(v)}/{len(ws)})" if v else "-"

    ra87 = [r["tu"] for r in ra if r["tu"] != "rầm rầm" and r["tu"] not in v2._K1_RD1 and r["tu"] not in v2._K1_TT1]  # tập ra 87 của bản nháp đầu
    duoi = __import__("json").loads((E / "rd1-audit-summary.json").read_text(encoding="utf-8"))["unprepared_tail"]
    log = [f"H7: {len(rows7)} khóa; {dict(sorted(c7.items()))}",
           f"H5: {len(rows5)} cặp; {dict(sorted(c5.items()))}",
           f"Thay: {len(ra)} từ ra ({dict(ct)}); {sum(r['vai_tro'] == 'VAO' for r in vao)} vào, "
           f"{sum(r['vai_tro'] == 'DU_BI' for r in vao)} dự bị, {sum(r['vai_tro'] == 'CON_LAI' for r in vao)} còn lại; "
           f"nhánh Q-rtc-O1: {len(s1)} khóa",
           f"đuôi sau O87 + 25 dự bị của Astra (rd1-audit-summary.json, unprepared_tail) = vị trí 113–120 ở đây: {moi[112:120] == duoi}; "
           f"từ vào thứ 88 = {moi[87] if len(moi) > 87 else '-'}; vị trí 113 = {moi[112] if len(moi) > 112 else '-'}",
           f"trung vị PPM sạch (opus-counts.tsv rồi l2/l2b/l2c/l3-ung-vien.tsv, như screen_core.load của Astra): "
           f"O87 ra {trung_vi(ra87)}, vào {trung_vi(moi[:87])}; "
           f"O{len(ra)} ra {trung_vi([r['tu'] for r in ra])}, vào {trung_vi(moi[:len(ra)])}",
           "Đồng thuận thay: " + ", ".join(r["tu"] for r in rows_t if r["trang_thai"] == "DONG_THUAN"),
           "Đo xong, chờ Astra xác nhận số: " + ", ".join(r["tu"] for r in rows_t if r["trang_thai"] == "DO_XONG_CHO_XAC_NHAN"),
           "Đồng thuận thay, nhãn CHO_LOAI: " + ", ".join(r["tu"] for r in rows_t if r["trang_thai"] == "DONG_THUAN_CHO_LOAI"),
           "Tranh chấp S2 (Opus thay): " + ", ".join(r["tu"] for r in rows_t if r["trang_thai"] == "TRANH_CHAP_S2"),
           "Chủ dự án quyết, Q-rtc-O1 (Astra K1, Opus K2): " + ", ".join(r["tu"] for _, r in s1),
           "H7 chờ căn cứ (Astra CHO): " + ", ".join(r["tu_chinh"] for r in rows7 if r["trang_thai"] == "CHO_CAN_CU"),
           "H7 giữ theo chữ ký cũ: " + ", ".join(r["tu_chinh"] for r in rows7 if r["trang_thai"] == "GIU_CHU_KY_CU"),
           "H5 chờ căn cứ: " + ", ".join(f"{r['tu']}/{r['bien_the']}" for r in rows5 if r["trang_thai"] == "CHO_CAN_CU"),
           "H5 tranh chấp khác: " + ", ".join(f"{r['tu']}/{r['bien_the']}" for r in rows5
                                               if r["trang_thai"] == "TRANH_CHAP" and r["astra_ma"] not in ("CHO_LOAI_c_d", "BAO_LUU_CHO_LOAI")),
           "H5 cặp khớp họ đã đăng ký khi tách ' / ': " + ", ".join(
               f"{r['tu']}/{r['bien_the']} ({r['nguon_so'].split(' ')[0]})" for r in rows5
               if r["nguon_so"].startswith("spelling_families"))]
    (HERE / "hop-nhat-rtc.log").write_text("\r\n".join(x.rstrip() for x in log) + "\r\n", encoding="utf-8", newline="")
    print("\n".join(log))


if __name__ == "__main__":
    main()
