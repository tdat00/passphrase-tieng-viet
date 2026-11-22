"""Đối chiếu chéo vòng 1 (Opus ↔ Astra) cho rà/thay danh sách chính: H7 theo khóa, H5 theo cặp, danh sách thay.

    python doi-chieu-astra.py  ->  doi-chieu-h7.tsv, doi-chieu-h5.tsv, doi-chieu-thay.tsv, doi-chieu-astra.log

Chỉ đọc: bảng của Opus (../sang-loc-h7.tsv, ../sang-loc-h5.tsv, ../de-xuat-thay.tsv) và bảng của Astra
(ho-so/astra/ra-thay-chinh/*.tsv). Cột opus_v2 là lập trường sau rà chéo (xem round-1-cross-review.md mục 2.1, 4);
phán quyết từng cặp nằm trong doi-chieu-v2.py.
"""
import collections
import importlib.util

from chung import *

A = AT / "ho-so" / "astra" / "ra-thay-chinh"
SEV = {"K0": 6, "K1": 5, "K1_GIAP_RANH": 5, "CHO": 4, "K2": 3, "K2_DA_KY": 2, "KHONG_DO": 1, "-": 0}


def norm_opus(v):
    return {"K0_DE_XUAT": "K0", "K1_DE_XUAT": "K1", "K1_GIAP_RANH": "K1_GIAP_RANH", "K2_DE_XUAT": "K2",
            "K2_DA_KY": "K2_DA_KY", "KHONG_DO": "KHONG_DO", "KHONG_CONI": "KHONG_DO"}.get(v, v or "-")


def norm_astra(v):
    return {"K0": "K0", "K1": "K1", "K2_DE_NGHI_KHONG_CHAN": "K2", "CHO_NGHIA": "CHO", "CHO_DO": "CHO",
            "KHONG_DO": "KHONG_DO", "DA_CO_PHAN_XU": "K2_DA_KY", "CUNG_MAT_CHU_KHAC_KHOANG": "KHONG_DO"}.get(v, v or "-")


def main():
    out_utf8()
    spec = importlib.util.spec_from_file_location("v2", HERE / "doi-chieu-v2.py")
    v2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v2)
    mine = rd(OUT / "sang-loc-h7.tsv", mine=True)
    ast = rd(A / "h7-sang-loc-1177.tsv") + rd(A / "h7-sang-loc-bo-sung.tsv")
    main_words = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
    km = {key(w): w for w in main_words}
    pairs = collections.defaultdict(dict)
    for r in mine:
        pairs[(r["tu_chinh"], r["doc_khac"])]["o"] = (norm_opus(r["de_xuat"]), r["ti_le_r"], r["ppm_gop_doc_khac"])
    for i, r in enumerate(ast):
        a = float(r["ppm_tu_chinh"]) if r["ppm_tu_chinh"] not in ("", "-", "CHUA_DO") else 0.0
        b = float(r["ppm_doc_khac"]) if r["ppm_doc_khac"] not in ("", "-", "CHUA_DO") else None
        rr = f"{b / a:.3f}" if a and b is not None else "-"
        pairs[(r["tu_chinh"], r["doc_khac"])]["a"] = (norm_astra(r["muc_K_de_xuat"]), rr,
                                                      f"{b:.3f}" if b is not None else "CHUA_DO", r["id"])
    by_key = collections.defaultdict(list)
    for (w, x), d in pairs.items():
        by_key[w].append((x, d))
    rows7 = []
    for w in sorted(by_key, key=o1):
        items = by_key[w]
        ov = max((d.get("o", ("-",))[0] for _, d in items), key=lambda v: SEV.get(v, 0))
        av = max((d.get("a", ("-",))[0] for _, d in items), key=lambda v: SEV.get(v, 0))
        lech = [f"{x}[O:{d.get('o', ('-',))[0]};A:{d.get('a', ('-',))[0]};r={d.get('a', d.get('o', ('', '-')))[1]}]"
                for x, d in sorted(items, key=lambda t: o1(t[0]))
                if d.get("o", ("-",))[0] != d.get("a", ("-",))[0] and
                max(SEV.get(d.get("o", ("-",))[0], 0), SEV.get(d.get("a", ("-",))[0], 0)) >= 3]
        cls = (lambda v: "THAY" if SEV.get(v, 0) >= 5 else ("CHO" if v == "CHO" else
                                                            ("KY_K2" if v == "K2" else "GIU")))
        v2v, v2why = v2.H7.get(w, (None, None))
        if v2v is None:
            v2v = ov if SEV.get(ov, 0) < 5 or ov in ("K1", "K1_GIAP_RANH") else ov
            v2v = "K1" if v2v == "K1_GIAP_RANH" else v2v
            v2why = "giữ lập trường vòng 1"
        if cls(ov) == cls(av) == cls(v2v) == "GIU" and not lech:
            continue
        rows7.append({"khoa": key(w), "tu_chinh": w, "trong_chinh": "CO" if km.get(key(w)) == w else "KHONG",
                      "opus_v1": ov, "astra_v1": av, "ket_qua_v1": f"{cls(ov)}|{cls(av)}",
                      "opus_v2": v2v, "ket_qua_v2": f"{cls(v2v)}|{cls(av)}",
                      "hoa_v2": "HOA" if cls(v2v) == cls(av) else "LECH",
                      "cap_lech": "; ".join(lech) or "-", "ly_do_opus_v2": v2why})
    write_tsv(HERE / "doi-chieu-h7.tsv", list(rows7[0].keys()), rows7)
    log = [f"H7: khóa có ít nhất một cặp lệch hoặc kết quả khác: {len(rows7)}",
           "H7 v1 (opus|astra): " + str(dict(collections.Counter(r["ket_qua_v1"] for r in rows7))),
           "H7 v2 (opus|astra): " + str(dict(collections.Counter(r["ket_qua_v2"] for r in rows7))),
           "H7 v2 hòa/lệch: " + str(dict(collections.Counter(r["hoa_v2"] for r in rows7)))]
    # H5
    m5 = {(r["tu"], r["bien_the"]): r for r in rd(OUT / "sang-loc-h5.tsv", mine=True)}
    a5 = {(r["tu"], r["bien_the"]): r for r in rd(A / "h5-sang-loc-632.tsv") + rd(A / "h5-sang-loc-bo-sung.tsv")}
    rows5 = []
    for p in sorted(set(m5) | set(a5), key=lambda t: (o1(t[0]), o1(t[1]))):
        o, a = m5.get(p), a5.get(p)
        oh = o["hanh_dong"] if o else "-"
        ah = a["hanh_dong"] if a else "-"
        ok = o["ket_luan_cap"] if o else "-"
        ak = a["ket_qua"] if a else "-"
        oc = "THAY" if oh == "THAY" else ("DIEU_KIEN" if oh in ("KY_HAI_BEN_HOAC_THAY", "DOC_THEM_KY_HOAC_THAY") else
                                          ("CUNG_TU_QUA" if oh in ("DANG_KY_QUA", "DA_THAY_VI_H7") else
                                           ("KHONG_CHO_VAO" if oh == "KHONG_CHO_VAO_DU_PHONG" else "KHONG")))
        ac = "THAY" if ah == "DE_NGHI_THAY" else ("CHO" if ah in ("CHO_H5_TRUOC_FINAL", "HOA_NHAN_DIEN_TRUOC_FINAL") else
                                                 "KHONG")
        v2v, v2why = v2.H5.get(p, (None, None))
        if v2v is None:
            v2v, v2why = oc, "giữ lập trường vòng 1"
        if oc == ac and v2v == oc and (ok in ("KHAC_TU", "DA_DANG_KY") or ak not in ("TEN_RIENG_BI_HA_CHU",)):
            continue
        rows5.append({"tu": p[0], "bien_the": p[1], "opus_ket_luan_cap": ok, "opus_loai": o["loai_H5"] if o else "-",
                      "opus_ket_luan_H5": o["ket_luan_H5"] if o else "-", "opus_v1": oc,
                      "astra_ket_qua": ak, "astra_loai": a["loai_H5_de_xuat"] if a else "-", "astra_v1": ac,
                      "astra_HND_chi_viet_hoa": a["HND74_only_capitalized"] if a else "-",
                      "opus_v2": v2v, "hoa_v2": "HOA" if (v2v == ac or (v2v in ("KHONG", "CUNG_TU_QUA") and ac == "KHONG"))
                      else "LECH", "ly_do_opus_v2": v2why})
    write_tsv(HERE / "doi-chieu-h5.tsv", list(rows5[0].keys()), rows5)
    log += [f"H5: cặp khác kết luận/hành động: {len(rows5)}",
            "H5 v1 (opus|astra): " + str(dict(collections.Counter(f"{r['opus_v1']}|{r['astra_v1']}" for r in rows5))),
            "H5 v2 hòa/lệch: " + str(dict(collections.Counter(r["hoa_v2"] for r in rows5)))]
    # Danh sách thay
    mt = rd(OUT / "de-xuat-thay.tsv", mine=True)
    s4 = rd(A / "de-xuat-thay-the-S4.tsv")
    o_ra = {r["tu"]: r["ma"] for r in mt if r["vai_tro"] == "RA"}
    mt2 = rd(HERE / "de-xuat-thay-v2.tsv", mine=True)
    o2 = {r["tu"]: r["vai_tro"] for r in mt2}
    o_dk = {r["tu"]: r["ma"] for r in mt if r["vai_tro"] == "DIEU_KIEN"}
    o_vao = {r["tu"]: r["vai_tro"] for r in mt if r["vai_tro"] in ("VAO", "VAO_NEU_DIEU_KIEN", "DU_BI")}
    a_ra = {r["tu_ra"]: r["ly_do_ra"] for r in s4}
    a_vao = {r["tu_vao_de_xuat"]: r["nguon"] for r in s4}
    cx = {r["tu"]: r["ca_cho"] for r in rd(A / "cac-tu-cho-phan-xu.tsv")}
    rows_t = []
    for w in sorted(set(o_ra) | set(o_dk) | set(a_ra) | set(cx) | {x for x, v in o2.items() if v == "RA"}, key=o1):
        rows_t.append({"chieu": "RA", "tu": w, "opus": "RA" if w in o_ra else ("DIEU_KIEN" if w in o_dk else "GIU"),
                       "opus_ma": o_ra.get(w) or o_dk.get(w) or "-",
                       "astra": "RA" if w in a_ra else ("CHO" if w in cx else "GIU"),
                       "astra_ma": a_ra.get(w) or cx.get(w) or "-", "opus_v2": o2.get(w, "GIU")})
    for w in sorted(set(o_vao) | set(a_vao) | {x for x, v in o2.items() if v != "RA"}, key=o1):
        rows_t.append({"chieu": "VAO", "tu": w, "opus": o_vao.get(w, "-"), "opus_ma": "-",
                       "astra": "VAO" if w in a_vao else "-", "astra_ma": a_vao.get(w, "-"), "opus_v2": o2.get(w, "-")})
    write_tsv(HERE / "doi-chieu-thay.tsv", list(rows_t[0].keys()), rows_t)
    c_ra = collections.Counter((r["opus"], r["astra"]) for r in rows_t if r["chieu"] == "RA")
    log += [f"RA: Opus {len(o_ra)} (+{len(o_dk)} điều kiện), Astra {len(a_ra)} (+{len(cx)} chờ); chung "
            f"{len(set(o_ra) & set(a_ra))}", "RA (opus, astra): " + str(dict(c_ra)),
            f"VAO: Opus {sum(v == 'VAO' for v in o_vao.values())}, Astra {len(a_vao)}; chung "
            f"{len({w for w, v in o_vao.items() if v == 'VAO'} & set(a_vao))}"]
    r2 = {w for w, v in o2.items() if v == "RA"}
    v2v = {w for w, v in o2.items() if v == "VAO"}
    log += [f"RA v2: Opus {len(r2)}, chung với Astra {len(r2 & set(a_ra))}, chỉ Opus {sorted(r2 - set(a_ra), key=o1)}, "
            f"chỉ Astra {len(set(a_ra) - r2)}", f"VAO v2: Opus {len(v2v)}, chung với Astra {len(v2v & set(a_vao))}"]
    (HERE / "doi-chieu-astra.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
    print("\n".join(log))


if __name__ == "__main__":
    main()
