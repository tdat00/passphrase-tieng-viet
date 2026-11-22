"""Mô phỏng thay từ chính theo P6 (S4, ngăn hạn mức) cho tập loại do Opus đề xuất.

    set HND_DIR=<ngoài repo: Viet11K.txt … Viet74K.txt>
    python de-xuat-thay.py  ->  ../de-xuat-thay.tsv, de-xuat-thay.log

Tập loại (RA): K0 và K1 (rõ, giáp ranh) trong sang-loc-h7.tsv, cộng hành động THAY trong sang-loc-h5.tsv.
Tập điều kiện (DIEU_KIEN): H5 cần hai chữ ký hoặc đọc thêm, K0_NGHI; nếu không được ký thì cũng phải thay.
Từ vào (VAO): theo p6-tinh-doc-lap-astra.py, ghế trống được lấp bằng mục kế tiếp theo S4 (hạng trong xep-hang.tsv)
còn vừa hạn mức: F đã đủ 77 nên ghế không-F chỉ nhận mục không-F; R1 = 0 nên không lấy R1. Lấy từ dự phòng
(du-phong-phan-loai.tsv), bỏ tầng D và hai cổng còn mở (loằng ngoằng CHO_H5, ngoại trừ CHO_H7).
Mỗi từ vào được soát lại: cách đọc DOC_KHAC ≥ 0,3 PPM hoặc ≥ PPM của mục, cách đọc cùng khóa trong HND (K0 và
nhóm đỏ), biến thể H5b (i/y sau h, k, l, m, s, t, qu).
"""
import collections
import importlib.util
import unicodedata

from chung import *

spec = importlib.util.spec_from_file_location("h7", HERE / "sang-loc-h7.py")
h7 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h7)
GATES_OPEN = {"loằng ngoằng": "CHO_H5", "ngoại trừ": "CHO_H7"}
LOAI_VAO = {"qua quýt": "H5b qua quít: phụ đề 2 + 0 < 20 lượt (dem-h5b.tsv, sang-loc-h5.tsv) → LOAI_THIEU_DU_LIEU"}
VAO_KHONG_DO = {("đưa đò", "dưa đỏ"): "dưa đỏ là quả, không đỏ", ("làm cỗ", "làm cỏ"): "làm cỏ là việc đồng áng",
                ("thay lông", "thay lòng"): "thay lòng (đổi dạ) chỉ sự đổi ý, không thuộc nhóm đỏ",
                ("đáp số", "đập số"): "-", ("dài ngoằng", "dài ngoẵng"): "-"}
RED = set(h7.K2_SINGLE) | {x for _, x in h7.K1_RO} | {x for _, x in h7.K1_GR} | {x for _, x in h7.K2_MULTI} | \
    {x for _, x in h7.K0} | set(h7.LEX)
TONE = {"\u0300", "\u0301", "\u0303", "\u0309", "\u0323"}


def h5b(w):
    out = []
    syl = w.split()
    for i, s in enumerate(syl):
        d = unicodedata.normalize("NFD", s)
        tone = "".join(c for c in d if c in TONE)
        base = unicodedata.normalize("NFC", "".join(c for c in d if c not in TONE))
        for on in ("h", "k", "l", "m", "s", "t", "qu"):
            for coda in ("", "t") if on == "qu" else ("",):
                if base in (on + "i" + coda, on + "y" + coda):
                    vow = "y" if base[len(on)] == "i" else "i"
                    v = on + unicodedata.normalize("NFC", vow + tone) + coda
                    out.append(" ".join(syl[:i] + [v] + syl[i + 1:]))
    return out


def main():
    out_utf8()
    main_words = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
    lab = {r["tu"]: r for r in rd(AT / "labels.tsv")}
    xh = {r["tu"]: r for r in rd(U / "xep-hang.tsv")}
    res = rd(AT / "du-phong-phan-loai.tsv")
    s7 = rd(OUT / "sang-loc-h7.tsv", mine=True)
    s5 = rd(OUT / "sang-loc-h5.tsv", mine=True)
    ra, dk = collections.OrderedDict(), collections.OrderedDict()
    for i, r in enumerate(s7, 2):
        if r["de_xuat"] in ("K0_DE_XUAT", "K1_DE_XUAT", "K1_GIAP_RANH"):
            ra.setdefault(r["tu_chinh"], []).append((r["de_xuat"].replace("_DE_XUAT", ""), f"{r['doc_khac']}",
                                                     f"sang-loc-h7.tsv:{i}"))
        elif r["de_xuat"] == "K0_NGHI":
            dk.setdefault(r["tu_chinh"], []).append(("K0_NGHI", r["doc_khac"], f"sang-loc-h7.tsv:{i}"))
    for i, r in enumerate(s5, 2):
        if r["hanh_dong"] == "THAY":
            ra.setdefault(r["tu"], []).append((r["ket_luan_H5"], r["bien_the"], f"sang-loc-h5.tsv:{i}"))
        elif r["hanh_dong"] in ("KY_HAI_BEN_HOAC_THAY", "DOC_THEM_KY_HOAC_THAY"):
            dk.setdefault(r["tu"], []).append((r["ket_luan_H5"], r["bien_the"], f"sang-loc-h5.tsv:{i}"))
    assert all(w in main_words for w in list(ra) + list(dk))

    def binof(w):
        return ("R1" if lab[w]["nhan"] == "R1" else "OK") + ("_F" if lab[w]["lop"] == "F" else "_N")

    f_main = sum(lab[w]["lop"] == "F" for w in main_words)
    need = collections.Counter(binof(w) for w in ra)
    need_dk = collections.Counter(binof(w) for w in dk)
    slack_f = 77 - (f_main - need["OK_F"] - need["R1_F"])
    hnd = collections.defaultdict(set)
    allw = set()
    for ten in ("Viet11K", "Viet22K", "Viet39K", "Viet74K"):
        for l in open(HND_DIR / f"{ten}.txt", encoding="utf-8"):
            w = unicodedata.normalize("NFC", l.strip()).lower()
            if w:
                hnd[key(w)].add(w)
                allw.add(w)
    oc = rd(U / "opus-counts.tsv")
    pu = {r["tu"]: h7.ppm(r) for r in oc if r["vai_tro"] == "UNG_VIEN"}
    dkr = collections.defaultdict(list)
    for r in oc:
        if r["vai_tro"] == "DOC_KHAC":
            dkr[r["khoa"]].append((r["tu"], h7.ppm(r)))
    cand = sorted(res, key=lambda r: (int(xh[r["tu"]]["hang"]) if r["tu"] in xh else 10 ** 6, o1(r["tu"])))
    rows, vao, bo = [], [], collections.Counter()
    n_n = need["OK_N"] + need_dk["OK_N"] + 12
    for r in cand:
        w = r["tu"]
        if r["tang"] == "D":
            bo["tang_D"] += 1
            continue
        if w in GATES_OPEN:
            bo["cong_mo"] += 1
            continue
        if w in LOAI_VAO:
            bo["loai_H5b"] += 1
            continue
        if r["lop"] == "F" and slack_f <= 0:
            bo["F_day"] += 1
            continue
        k = r["khoa"]
        doc = [(x, p) for x, p in dkr.get(k, []) if p >= 0.3 or p >= pu.get(w, 0.0)]
        ghi = []
        for x, p in doc:
            ghi.append(f"{x} {p:.2f}: " + VAO_KHONG_DO.get((w, x), "CAN_DOC"))
        do = sorted(x for x in hnd.get(k, set()) - {w} if x in RED)
        if do:
            ghi.append("HND cùng khóa thuộc danh sách đỏ: " + ", ".join(do))
        b5 = [v for v in h5b(w) if v in allw]
        if b5:
            ghi.append("H5b có trong HND: " + ", ".join(b5))
        vao.append((w, r, "; ".join(ghi) or "không có cách đọc khác ≥ mốc; không có biến thể H5b trong HND"))
        if len(vao) >= n_n:
            break
    for w, items in ra.items():
        rows.append({"vai_tro": "RA", "thu_tu": "-", "tu": w, "khoa": key(w), "ngan": binof(w),
                     "diem": f"{float(lab[w]['diem']):.2f}", "hang_S4": xh.get(w, {}).get("hang", "-"), "tang": "-",
                     "ma": ";".join(sorted({c for c, _, _ in items})), "doi_chung": "; ".join(x for _, x, _ in items),
                     "soat_vao": "-", "viec_con_lai": "đăng ký khóa/họ sau khi thay",
                     "bang_chung": ";".join(e for _, _, e in items)})
    for w, items in dk.items():
        rows.append({"vai_tro": "DIEU_KIEN", "thu_tu": "-", "tu": w, "khoa": key(w), "ngan": binof(w),
                     "diem": f"{float(lab[w]['diem']):.2f}", "hang_S4": xh.get(w, {}).get("hang", "-"), "tang": "-",
                     "ma": ";".join(sorted({c for c, _, _ in items})), "doi_chung": "; ".join(x for _, x, _ in items),
                     "soat_vao": "-", "viec_con_lai": "hai SA ký (H5 chu_ky_hai_ben hoặc K0 đọc chung); không ký thì RA",
                     "bang_chung": ";".join(e for _, _, e in items)})
    n_ra = len(ra)
    for i, (w, r, ghi) in enumerate(vao, 1):
        vai = "VAO" if i <= n_ra else ("VAO_NEU_DIEU_KIEN" if i <= n_ra + len(dk) else "DU_BI")
        todo = "viết sạch mới; D2; D5; D6; D7; D8"
        if r["tang"] == "C":
            todo += "; xử cảnh báo tầng C: " + r["ma_van_de"]
        rows.append({"vai_tro": vai, "thu_tu": i, "tu": w, "khoa": r["khoa"], "ngan": r["ngan"],
                     "diem": f"{float(r['diem']):.2f}", "hang_S4": xh.get(w, {}).get("hang", "-"), "tang": r["tang"],
                     "ma": r["ma_van_de"], "doi_chung": "-", "soat_vao": ghi, "viec_con_lai": todo,
                     "bang_chung": "analyzing-tools/du-phong-phan-loai.tsv;analyzing-tools/ho-so/unified/xep-hang.tsv"})
    hdr = list(rows[0].keys())
    write_tsv(OUT / "de-xuat-thay.tsv", hdr, rows)
    log = [f"RA: {n_ra} ({dict(need)}); DIEU_KIEN: {len(dk)} ({dict(need_dk)}); F chính {f_main}, chỗ trống F sau khi ra {slack_f}",
           f"mã RA: {dict(collections.Counter(c for items in ra.values() for c in sorted({x for x, _, _ in items})))}",
           f"bỏ qua khi lấp: {dict(bo)}",
           f"VAO: {sum(1 for x in rows if x['vai_tro'] == 'VAO')}; tầng: "
           f"{dict(collections.Counter(x['tang'] for x in rows if x['vai_tro'] == 'VAO'))}",
           f"dự phòng còn lại nếu không bù: {len(res) - sum(1 for x in rows if x['vai_tro'] == 'VAO')}"
           f" (thêm {len(dk)} nếu các ca điều kiện đều phải thay)",
           "RA: " + ", ".join(ra), "DIEU_KIEN: " + ", ".join(dk),
           "VAO: " + ", ".join(x["tu"] for x in rows if x["vai_tro"] == "VAO"),
           "VAO_NEU_DIEU_KIEN: " + ", ".join(x["tu"] for x in rows if x["vai_tro"] == "VAO_NEU_DIEU_KIEN"),
           "DU_BI: " + ", ".join(x["tu"] for x in rows if x["vai_tro"] == "DU_BI")]
    (HERE / "de-xuat-thay.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
    print("\n".join(log))
    for x in rows:
        if x["vai_tro"] != "RA" and x["vai_tro"] != "DIEU_KIEN" and "không có cách đọc" not in x["soat_vao"]:
            print("SOAT:", x["tu"], "|", x["soat_vao"])


if __name__ == "__main__":
    main()
