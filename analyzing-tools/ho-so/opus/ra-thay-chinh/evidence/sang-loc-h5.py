"""H5 cho danh sách chính: kết luận của Opus trên 632 cặp thô (du-phong-v2/evidence/bien-the-chinh-tho.tsv).

    python sang-loc-h5.py  ->  ../sang-loc-h5.tsv, sang-loc-h5.log

- Số đếm: dem-h5.tsv (cùng một lượt đếm cho hai dạng; dạng nhiều âm tiết bỏ lượt "nghi vắt từ"). Cặp một âm tiết dùng
  số sạch của opus-counts.tsv khi cả hai dạng có ở đó (số sạch một âm tiết của dem-h5 không bỏ lượt nằm trong từ ghép).
- Người duyệt (Opus) xác nhận cặp nào là CÙNG TỪ; mặc định là KHAC_TU (khác từ, khác nghĩa, hay khác hình vị).
- Loại c/f khi Wiktionary tiếng Việt ghi dạng kia là cách viết khác hoặc "như" dạng chính, hoặc là cách Việt hóa khác
  của từ mượn; loại d khi dạng kia chỉ có trong HND 39K/74K (danh sách lớn có cả lỗi viết, ví dụ theo rõi, chưng bày).
  Tra Wiktionary qua API ngày 21/11/2026; không lưu lời định nghĩa.
- Luật đếm theo tieu-chi-thong-nhat.md H5 và ho-so/opus/h5/verdict_h5.py.
"""
import collections

from chung import *

WIKT = {  # dạng kia: điều Wiktionary vi ghi (đã tra, chỉ ghi nhãn)
    "tròng trành": "WIKT_LIKE(chòng chành)", "bồ kếp": "WIKT_ALT(bồ kết)", "rau giền": "WIKT_ALT_NGUOC(rau dền)",
    "ngảnh": "WIKT_LIKE(ngoảnh)", "phất phới": "WIKT_LIKE_IT_DUNG(phấp phới)", "già giặn": "WIKT_MUC_RIENG",
    "bóng loáng": "WIKT_MUC_RIENG", "bóng láng": "WIKT_MUC_RIENG", "long tong": "WIKT_NGHIA_KHAC",
    "lỏa tỏa": "WIKT_NGHIA_KHAC", "loả toả": "WIKT_NGHIA_KHAC", "y trang": "WIKT_NGHIA_KHAC",
}
for _x in ("cải soong", "xu hào", "sập sình", "sù sì", "co dúm", "rần rộ", "lấn áp", "lay hoay", "loằng nhoằng", "trơ vơ"):
    WIKT[_x] = "WIKT_KHONG_MUC"
CUNG_TU = {  # (từ chính, dạng kia): (loại H5, ghi chú)
    ("chòng chành", "tròng trành"): ("c", "D-dpv2-5; cả hai có mục Wiktionary"),
    ("bồ kết", "bồ kếp"): ("c", "Wiktionary ghi bồ kếp là cách viết khác"),
    ("rau dền", "rau giền"): ("c", "Wiktionary ghi rau dền là dạng khác của rau giền"),
    ("ngoảnh", "ngảnh"): ("c", "Wiktionary: ngảnh như ngoảnh"),
    ("phấp phới", "phất phới"): ("c", "Wiktionary: phất phới (ít dùng) như phấp phới"),
    ("già dặn", "già giặn"): ("c", "Wiktionary có mục già giặn; ngữ cảnh web dùng già giặn với nghĩa trưởng thành, như già dặn"),
    ("cải xoong", "cải soong"): ("f", "từ mượn (cresson); theo tiền lệ soong/xoong loại f"),
    ("lấn át", "lấn áp"): ("d", "ngữ cảnh: 9/9 lượt phụ đề đọc được dùng nghĩa lấn át"),
    ("loay hoay", "lay hoay"): ("d", "ngữ cảnh: lay hoay dùng nghĩa loay hoay"),
    ("xập xình", "sập sình"): ("d", "s/x; chỉ có trong HND74K"),
    ("su hào", "xu hào"): ("d", "s/x; ngữ cảnh web cùng nghĩa; chỉ có trong HND74K"),
    ("chơ vơ", "trơ vơ"): ("d", "ch/tr; chỉ có trong HND74K"),
    ("xù xì", "sù sì"): ("d", "s/x; chỉ có trong HND74K"),
    ("co rúm", "co dúm"): ("d", "r/d; chỉ có trong HND39K"),
    ("rầm rộ", "rần rộ"): ("d", "m/n cuối; chỉ có trong HND74K"),
    ("lằng nhằng", "loằng nhoằng"): ("d", "chỉ có trong HND74K; từ chính đã bị K1 ở H7"),
    ("bảng hiệu", "bản hiệu"): ("d", "ng/n cuối"), ("hạt dẻ", "hạt giẻ"): ("d", "d/gi"),
    ("xà bông", "sà bông"): ("d", "x/s"), ("thư giãn", "thư dãn"): ("d", "gi/d"),
    ("rong ruổi", "giong ruổi"): ("c", "có trong HND11K"), ("cột mốc", "cột mốt"): ("d", "c/t cuối"),
    ("lòng vòng", "lòng dòng"): ("d", "v/d"), ("nuốt chửng", "nuốt trửng"): ("d", "ch/tr"),
    ("theo dõi", "theo rõi"): ("d", "d/r"), ("thiện chí", "thiện trí"): ("d", "ch/tr"),
    ("trưng bày", "chưng bày"): ("d", "tr/ch"), ("bít tết", "bíp tết"): ("f", "đã đăng ký QUA_RIENG_H5"),
}
KHAC_TU_LY_DO = {
    ("bóng láng", "bóng loáng"): "hai hình vị khác (láng/loáng); Wiktionary có hai mục riêng, không ghi là cách viết khác",
    ("bóng loáng", "bóng láng"): "hai hình vị khác (láng/loáng); Wiktionary có hai mục riêng, không ghi là cách viết khác",
    ("lon ton", "long tong"): "Wiktionary: long tong là từ tượng thanh, khác nghĩa lon ton", ("lả tả", "loả toả"): "Wiktionary: nghĩa khác",
    ("lả tả", "lỏa tỏa"): "Wiktionary: nghĩa khác", ("y chang", "y trang"): "Wiktionary: y trang là danh từ (quần áo)",
    ("dây chun", "dây thun"): "từ đồng nghĩa hai miền, khác hình vị", ("ngâm nga", "ngân nga"): "khác hình vị (ngâm/ngân)",
    ("chăm nom", "thăm nom"): "hai từ khác", ("thon thả", "thong thả"): "khác nghĩa", ("hì hục", "hì hụi"): "T-dpv2-4",
    ("trở nên", "trở lên"): "l/n do phạt T của S4; trở lên là cụm khác (từ X trở lên)",
}


def verdict(t, a_s, b_s, a_w, b_w):
    ts, tw = a_s + b_s, a_w + b_w
    if t in ("b", "c", "f"):
        if ts < 20 or tw < 20:
            return "LOAI_THIEU_DU_LIEU"
        if 100 * a_s >= 95 * ts and 100 * a_w >= 95 * tw:
            return "QUA_RIENG_H5"
        return "LOAI_CANH_TRANH"
    ok = [(b, a + b) for a, b, n in ((a_s, b_s, ts), (a_w, b_w, tw)) if n >= 20]
    if not ok:
        return "CAN_HAI_CHU_KY"
    if any(100 * b >= 10 * n for b, n in ok):
        return "LOAI_LOI"
    if any(100 * b >= 5 * n for b, n in ok):
        return "TRU_DIEM"
    return "QUA_RIENG_H5"


def main():
    out_utf8()
    P = rd(AT / "ho-so/opus/du-phong-v2/evidence/bien-the-chinh-tho.tsv")
    D5 = {r["dang"]: r for r in rd(HERE / "dem-h5.tsv", mine=True)}
    oc = {r["tu"]: r for r in rd(U / "opus-counts.tsv") if r["vai_tro"] in ("UNG_VIEN", "DOC_KHAC")}
    rows, log = [], []
    for r in P:
        a, b = r["tu"], r["bien_the"]
        one = len(a.split()) == 1
        if one and a in oc and b in oc:
            c = [int(oc[a]["sub_sach"]), int(oc[b]["sub_sach"]), int(oc[a]["web_sach"]), int(oc[b]["web_sach"])]
            dk = ["-", "-"]
            nguon_dem = "opus-counts"
        else:
            A, B = D5[a], D5[b]
            c = [int(A["sub_moi_dong_sach"]), int(B["sub_moi_dong_sach"]), int(A["web_dong_khac_sach"]),
                 int(B["web_dong_khac_sach"])]
            dk = [A["sub_dong_khac_sach"], B["sub_dong_khac_sach"]]
            nguon_dem = "dem-h5" + ("_mot_am_tiet_chua_tru_tu_ghep" if one else "")
        reg = "DA_DANG_KY" if r["da_dang_ky_H5"] or r["trong_ho_d6"] else ""
        if (a, b) in CUNG_TU:
            t, note = CUNG_TU[(a, b)]
            v = verdict(t, *c)
            if v not in ("LOAI_THIEU_DU_LIEU", "CAN_HAI_CHU_KY") and dk[0] != "-":
                v2 = verdict(t, int(dk[0]), int(dk[1]), c[2], c[3])
                if (v.startswith("LOAI")) != (v2.startswith("LOAI")):
                    v = "CHO_SAT_NGUONG"
            act = {"QUA_RIENG_H5": "DANG_KY_QUA", "TRU_DIEM": "DANG_KY_TRU_DIEM", "CAN_HAI_CHU_KY": "KY_HAI_BEN_HOAC_THAY",
                   "CHO_SAT_NGUONG": "DOC_THEM_KY_HOAC_THAY"}.get(v, "THAY")
            if a == "lằng nhằng":
                act = "DA_THAY_VI_H7"
            kl, why = (reg or "CUNG_TU"), note
        else:
            t, v, act = "-", "-", "GIU"
            kl = reg or "KHAC_TU"
            why = KHAC_TU_LY_DO.get((a, b), "đã đăng ký" if reg else "khác từ: khác nghĩa hoặc khác hình vị (Opus đọc)")
        rows.append({"tu": a, "bien_the": b, "so_am_tiet": len(a.split()), "noi_co_mat": r["noi_co_mat"],
                     "ket_luan_cap": kl, "loai_H5": t, "wiktionary": WIKT.get(b, "-"), "nguon_dem": nguon_dem,
                     "sub_tu": c[0], "sub_bien_the": c[1], "web_tu": c[2], "web_bien_the": c[3],
                     "sub_dong_khac_tu": dk[0], "sub_dong_khac_bien_the": dk[1], "ket_luan_H5": v, "hanh_dong": act,
                     "ly_do": why})
    miss = [p for p in CUNG_TU if p not in {(x["tu"], x["bien_the"]) for x in rows}]
    assert not miss, miss
    d5b = {r["dang"]: r for r in rd(HERE / "dem-h5b.tsv", mine=True)}
    main_words = {l.split("|")[0] for l in lines(AT / "wordlist.txt")}
    for r in rd(HERE / "cap-h5b.tsv"):
        a, b = r["tu"], r["bien_the"]
        A, B = d5b[a], d5b[b]
        c = [int(A["sub_moi_dong_sach"]), int(B["sub_moi_dong_sach"]), int(A["web_dong_khac_sach"]),
             int(B["web_dong_khac_sach"])]
        v = verdict("b", *c)
        if v == "QUA_RIENG_H5" and verdict("b", int(A["sub_dong_khac_sach"]), int(B["sub_dong_khac_sach"]),
                                           c[2], c[3]) != v:
            v = "CHO_SAT_NGUONG"
        chinh = a in main_words
        rows.append({"tu": a, "bien_the": b, "so_am_tiet": len(a.split()), "noi_co_mat": "H5B_MOI_HND",
                     "ket_luan_cap": "CUNG_TU", "loai_H5": "b", "wiktionary": "-", "nguon_dem": "dem-h5b",
                     "sub_tu": c[0], "sub_bien_the": c[1], "web_tu": c[2], "web_bien_the": c[3],
                     "sub_dong_khac_tu": A["sub_dong_khac_sach"], "sub_dong_khac_bien_the": B["sub_dong_khac_sach"],
                     "ket_luan_H5": v,
                     "hanh_dong": ("DANG_KY_QUA" if v == "QUA_RIENG_H5" else "THAY") if chinh else
                     ("DANG_KY_QUA" if v == "QUA_RIENG_H5" else "KHONG_CHO_VAO_DU_PHONG"),
                     "ly_do": ("i/y sau qu; " + ("từ chính" if chinh else "từ dự phòng tầng A, du-phong-v2 chưa bắt H5b"))})
    hdr = list(rows[0].keys())
    write_tsv(OUT / "sang-loc-h5.tsv", hdr, rows)
    log.append(f"cặp: {len(rows)} (632 cặp thô + {len(rows) - len(P)} cặp H5b mới); từ: {len({x['tu'] for x in rows})}")
    for k, n in sorted(collections.Counter((x["ket_luan_cap"], x["ket_luan_H5"], x["hanh_dong"]) for x in rows).items()):
        log.append("\t".join(k) + f"\t{n}")
    for act in ("THAY", "DOC_THEM_KY_HOAC_THAY", "KY_HAI_BEN_HOAC_THAY", "KHONG_CHO_VAO_DU_PHONG"):
        log.append(f"{act}: " + ", ".join(sorted({x['tu'] for x in rows if x['hanh_dong'] == act}, key=o1)))
    (HERE / "sang-loc-h5.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
    print("\n".join(log))


if __name__ == "__main__":
    main()
