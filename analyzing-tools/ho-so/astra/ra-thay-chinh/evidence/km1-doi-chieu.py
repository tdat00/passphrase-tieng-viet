"""Gắn nguồn vào các QUYẾT ĐỊNH VIẾT TAY; không tạo hoặc sửa đề xuất hay chữ ký."""
import csv
import hashlib
import io
import json
import re
import unicodedata as ud
from collections import Counter, defaultdict
from pathlib import Path

E = Path(__file__).resolve().parent
A, AT = E.parent, E.parents[3]
U, O = AT / "ho-so" / "unified", AT / "ho-so" / "opus" / "ra-thay-chinh"
S, W = 34314528, 149860716
OUT = A / "khep-muc-mo-1.tsv"
SECTIONS = ("H7_CHO", "H5_CHO", "CO_TU_VAO", "K2")
OLD = "bình|di động|khảm|kính|nướng|phết|thầy|thổi|trứng".split("|")
EXTERNAL = {
    "an bình": ("VDict:ăn bĩnh",), "ghen": ("BVNTL",), "niêu": ("VDict:niệu", "Han:尿"),
    "tình tứ": ("VDict:tinh tử",), "tép riu": ("VDict:tép diu",),
    "bảng hiệu": ("VDict:bản hiệu",), "bộc phát / bội phát": ("VDict:bội phát",),
    "lòng vòng": ("VDict:lòng dòng",), "ọp ẹp": ("VDict:ọt ẹt",), "ru rú": ("VDict:giu giú",),
    "xoành xoạch": ("VDict:xành xạch", "ZIM"), "giỡn": ("SOHA:rỡn",), "rướn": ("SOHA:dướn",),
    "thư giãn": ("SOHA:thư giãn",), "nuốt chửng": ("NUOT",),
    "điểm nhấn": ("DIEM_NHAN",), "ong thợ": ("ONG_THO",), "khuy": ("KHUY",),
    "làm khó": ("VDict:làm khổ",), "thay lông": ("VDict:thay lòng",),
}
FLAGS = {
    "làm cỗ": ("H7", ["làm cỏ"]), "thay lông": ("H7", ["thay lòng"]),
    "mang máng": ("H7", ["màng màng"]), "xoành xoạch": ("H5", ["xành xạch", "xoàn xoạt"]),
    "thụp": ("H5", ["chụp", "thụt"]), "loáng thoáng": ("H5", ["loáng choáng"]),
    "rướn": ("H5", ["dướn", "rướm"]), "xầm xì": ("H5", ["sầm sì"]),
}
# Chỉ dẫn các dòng thực sự đã đọc như đầu mục, không lấy một ví dụ tình cờ bắt đầu cùng chữ.
PRINT_LINES = {
    12139, 12641, 26851, 137922, 37510, 58434, 119687, 58485, 79088, 83132, 83138, 83228, 108127,
    114159, 119084, 119016, 122537, 129546, 133358, 133382, 138834, 121235,
    77476, 131528, 87717, 165130, 138257, 138260, 27282, 138270, 82740, 82739, 120360, 39822,
    120358, 163730, 5352, 5356, 5359, 8575, 17561, 19560, 19569, 20352, 21517, 21526, 31452, 30457,
    29437, 34307, 34309, 37988, 50171, 50191, 54584, 67086, 65138, 65242, 70485,
    83659, 94569, 120008, 135059, 140770, 150552, 151474, 151479, 158546,
    5123, 29621, 49660, 58138, 91470, 98800, 113882, 120989, 154034, 141248, 149072,
}


def key(w):
    return "".join(c for c in ud.normalize("NFD", w.lower()) if not ud.combining(c)).replace("đ", "d").replace(" ", "")


def rows(path):
    prefix = ("E\\" + path.name if path.parent == E else "A\\" + path.name if path.parent == A
              else "U\\" + path.name if path.parent == U else "AT\\" + path.name if path.parent == AT
              else "O\\" + str(path.relative_to(O)))
    with path.open(encoding="utf-8-sig", newline="") as f:
        return [dict(r, ref=f"{prefix}:{n}", line=n) for n, r in enumerate(csv.DictReader(f, delimiter="\t"), 2)]


def save(path, data, fields):
    b = io.StringIO()
    writer = csv.DictWriter(b, fields, delimiter="\t", lineterminator="\r\n", extrasaction="ignore")
    writer.writeheader()
    writer.writerows(data)
    path.write_bytes(b.getvalue().encode("utf-8"))


def index(data, field):
    return {r[field]: r for r in data}


def compact(refs):
    found = defaultdict(set)
    for r in refs:
        if not r:
            continue
        p, n = r.rsplit(":", 1)
        found[p].add(int(n))
    result = []
    for p, ns in found.items():
        spans = []
        for n in sorted(ns):
            if spans and n == spans[-1][1] + 1:
                spans[-1][1] = n
            else:
                spans.append([n, n])
        result.append(p + ":" + ",".join(str(a) if a == b else f"{a}–{b}" for a, b in spans))
    return "; ".join(result)


def main():
    cards = rows(OUT)
    h7 = index(rows(U / "ra-thay-chinh-h7.tsv"), "tu_chinh")
    h5 = {(r["tu"], r["bien_the"]): r for r in rows(U / "ra-thay-chinh-h5.tsv")}
    changes = rows(U / "ra-thay-chinh-thay-the.tsv")
    pool = {r["tu"]: r for r in changes if r["vai_tro"] in {"VAO", "DU_BI"}}
    out0 = {r["tu"] for r in changes if r["vai_tro"] == "RA"}
    labels = index(rows(AT / "labels.tsv"), "tu")
    freq = {}
    for r in rows(U / "opus-counts.tsv"):
        if r["tu"] not in freq or r["vai_tro"] == "UNG_VIEN":
            freq[r["tu"]] = r
    for tag in ("l2", "l2b", "l2c", "l3"):
        for r in rows(U / f"{tag}-ung-vien.tsv"):
            freq.setdefault(r["tu"], r)
    cross = rows(E / "cr1-HND-da-co-so-do.tsv")
    for r in cross:
        old = freq[r["doc_khac"]]
        assert (r["sub_sach"], r["web_sach"]) == (old["sub_sach"], old["web_sach"])
    assert len({(r["khoa"], r["doc_khac"]) for r in cross}) == len(cross) == 238
    measured = {(g, s): index(rows(E / f"{'km1-h7' if g == 'H7' else 'km1'}-dem-{s}.tsv"), "tu")
                for g in ("H5", "H7") for s in ("sub", "web")}
    rec5 = index(rows(O / "evidence" / "dem-h5.tsv"), "dang")
    for r in rows(O / "evidence" / "dem-h5b.tsv"):
        rec5.setdefault(r["dang"], r)
    aspairs = defaultdict(dict)
    for fname in ("h7-sang-loc-1177.tsv", "h7-sang-loc-bo-sung.tsv"):
        for r in rows(A / fname):
            if r["muc_K_de_xuat"] in {"K0", "K1", "K2_DE_NGHI_KHONG_CHAN", "CHO_NGHIA", "CHO_DO"}:
                aspairs[r["tu_chinh"]][r["doc_khac"]] = r["ref"]
    opairs = defaultdict(dict)
    for r in rows(O / "sang-loc-h7.tsv"):
        if r["de_xuat"].startswith(("K0", "K1", "K2")):
            opairs[r["tu_chinh"]][r["doc_khac"]] = r["ref"]
    kg = index(rows(E / "tt1-K2-review-input.tsv"), "tu")
    sg = index(rows(E / "tt1-H7-cho-review-input.tsv"), "tu")
    tt1 = index([r for r in rows(A / "thoa-thuan-1.tsv") if r["loai"] == "S1"], "tu_hoac_khoa")
    ext = index(rows(E / "km1-web.tsv"), "ma")
    samples = rows(E / "km1-nhan-mau.tsv")
    bounds = rows(E / "km1-can-da-doc.tsv")
    oldweb = index(rows(E / "tt1-web-sources.tsv"), "tu")
    wikt = defaultdict(list)
    for path in sorted(E.glob("km1-dictionary-*.tsv")):
        for r in rows(path):
            if r["co_phan_tieng_Viet"] == "True" and r["revision"] != "-":
                wikt[r["tu"]].append((r["lang"], r["revision"], r["ref"]))
    for path in ("rd1-dictionary-metadata.tsv", "cr1-dictionary-metadata.tsv", "dictionary-h7critical.tsv"):
        for r in rows(E / path):
            if r.get("co_phan_tieng_Viet", r.get("has_vietnamese_section")) == "True" and r["revision"] != "-":
                wikt[r["tu"]].append((r["lang"], r["revision"], r["ref"]))
    vv, printed = defaultdict(list), defaultdict(list)
    for g in ("H5", "H7", "VAO", "K2"):
        for r in rows(E / f"km1-vv-{g}.tsv"):
            if r["co_muc_30K"] == "1":
                vv[r["tu"]].append(r["ref"])
        for r in rows(E / f"km1-ban-in-{g}.tsv"):
            if int(r["dong_ocr_khop_chuoi"]) in PRINT_LINES:
                printed[r["tu"]].append(r["ref"])
    yes_h7 = {w for w, r in h7.items() if r["trang_thai"] in {"DONG_THUAN_GIU_CAN_KY_K2", "CHU_DU_AN_GIU_CAN_KY_K2"}}
    queue7 = {w for w, r in h7.items() if r["trang_thai"] == "CHO_CAN_CU"}
    queue5 = {" / ".join(p) for p, r in h5.items() if r["trang_thai"] == "CHO_CAN_CU"}
    flags = {w for w, r in pool.items() if r["can_soat"] != "-"} - {"đưa đò", "nặng cân", "thẳng đơ"}
    expected = dict(zip(SECTIONS, (queue7, queue5, flags, yes_h7)))
    assert [len(expected[x]) for x in SECTIONS] == [46, 27, 8, 205]
    for group in SECTIONS:
        actual = [r["tu_hoac_khoa"] for r in cards if r["loai"] == group]
        assert len(actual) == len(set(actual)) and set(actual) == expected[group], (group, set(actual) ^ expected[group])
    assert set(FLAGS) == flags
    protected = {w: r["line"] for w, r in h7.items()}
    cards.sort(key=lambda c: (SECTIONS.index(c["loai"]), protected[c["tu_hoac_khoa"]] if c["loai"] == "K2" else c["line"]))
    detail = []
    for c in cards:
        g, item = c["loai"], c["tu_hoac_khoa"]
        w = item.split(" / ")[0]
        h7mode = g in {"H7_CHO", "K2"} or g == "CO_TU_VAO" and FLAGS[w][0] == "H7"
        enclosing = (h7[w] if g in {"H7_CHO", "K2"} else pool[w] if g == "CO_TU_VAO"
                     else h5[tuple(item.split(" / "))])
        if g in {"H7_CHO", "K2"}:
            prior = kg.get(w) or sg.get(w)
            alts = list(dict.fromkeys([*(prior["doi_chung"].split(";") if prior else []), *aspairs[w], *opairs[w]]))
            assert alts and w not in alts and all(key(w) == key(x) for x in alts), w
        else:
            alts = FLAGS[w][1] if g == "CO_TU_VAO" else [item.split(" / ")[1]]
            prior = None
        field_refs, brief = [enclosing["ref"]], []
        if prior:
            field_refs.append(prior["ref"])
        if w in tt1 and g == "K2":
            field_refs.append(tt1[w]["ref"])
        start = len(detail) + 2
        for alt in alts:
            lex = []
            seen = set()
            for name in (alt, w) if not h7mode else (alt,):
                for lang, rev, ref in wikt.get(name, []):
                    if (name, lang, rev) not in seen:
                        lex.append(f"{name} {lang}@{rev} {ref}")
                        seen.add((name, lang, rev))
                if vv.get(name):
                    lex.append(f"{name} {vv[name][0]}")
            pair_refs, wnums = [], []
            if h7mode:
                for name in (w, alt):
                    r = freq.get(name)
                    if r:
                        ns = int(r["sub_sach"]), int(r["web_sach"])
                        pair_refs.append(r["ref"])
                    else:
                        r1, r2 = (measured["H7", s][name] for s in ("sub", "web"))
                        ns = int(r1["clean"]), int(r2["clean"])
                        pair_refs.extend((r1["ref"], r2["ref"]))
                    p = 500000 * (ns[0]/S + ns[1]/W)
                    wnums.append((str(ns[0]), "-", str(ns[1]), f"{p:.6f}"))
            else:
                for name in (w, alt):
                    if g == "H5_CHO" and name in rec5:
                        r = rec5[name]
                        ns = r["sub_moi_dong_sach"], r["sub_dong_khac_sach"], r["web_dong_khac_sach"], "-"
                        pair_refs.append(r["ref"])
                    else:
                        r1, r2 = (measured["H5", s].get(name) for s in ("sub", "web"))
                        if r1 and r2:
                            ns = r1["clean"], r1["distinct_clean"], r2["clean"], "-"
                            pair_refs.extend((r1["ref"], r2["ref"]))
                        else:
                            assert g == "H5_CHO" and enclosing["tu"] == w
                            ns = (enclosing["sub_tu"], "-", enclosing["web_tu"], "-") if name == w else (enclosing["sub_bien_the"], "-", enclosing["web_bien_the"], "-")
                            pair_refs.append(enclosing["ref"])
                    wnums.append(ns)
            d, e = wnums
            brief.append(f"{alt}={e[0]}/{e[2]}")
            if g in {"H7_CHO", "K2"}:
                attr = [aspairs[w].get(alt), opairs[w].get(alt)]
                if prior:
                    attr.append(prior["ref"])
            else:
                attr = [enclosing["ref"]]
            detail.append(dict(loai=g, tu=w, khoa=key(w), doi_chung=alt, sub_tu=d[0], sub_tu_khac=d[1],
                               web_tu=d[2], ppm_tu=d[3], sub_doc=e[0], sub_doc_khac=e[1], web_doc=e[2], ppm_doc=e[3],
                               nguon_dem=compact(pair_refs), dau_muc_va_revision="; ".join(lex) or "-",
                               nguon_phieu=compact(attr), ngay="2026-11-21"))
        end = len(detail) + 1
        field_refs.extend(f"E\\km1-doi-chung.tsv:{n}" for n in range(start, end+1))
        ns = [alt for alt in alts if any(r["tu"] == alt and r["phep"] == "H7" for r in samples)]
        if ns:
            field_refs.extend(r["ref"] for r in samples if r["tu"] in ns and r["phep"] == "H7")
        if w in {"chun", "thun"} and g == "H5_CHO":
            field_refs.extend(r["ref"] for r in samples if r["phep"] == "H5e")
            field_refs.extend(r["ref"] for r in bounds if r["kho"] == ("web" if w == "chun" else "sub"))
        for name in (w, *alts):
            # Dòng OCR còn có thể là đồng âm hoặc ví dụ, không phải chứng minh chỉ bằng hiện diện.
            if name in printed and (g != "K2" or w in {"tự ái", "bạn thân", "tròn", "phượng", "giỏi giang", "đồng cỏ", "cô dâu", "ngỗng", "sắn dây", "tiên nữ"}):
                field_refs.extend(printed[name])
        for tag in EXTERNAL.get(item, EXTERNAL.get(w, ())):
            field_refs.append(ext[tag]["ref"])
        if w in {"da gà", "dí dỏm", "giun", "theo dõi"}:
            name = {"da gà": "đá gà", "dí dỏm": "rí rỏm", "giun": "dun", "theo dõi": "theo rõi"}[w]
            field_refs.append(oldweb[name]["ref"])
        if w == "xanh":
            field_refs.append(labels[w]["ref"])
        if w == "bạn thân" and g == "K2":
            field_refs.extend(r["ref"] for r in rows(E / "km1-ban-than-id.tsv") if r["nhan_Astra"] == "MAI_DAM_RO")
        owner = " | D-rtc-6" if enclosing.get("trang_thai") == "CHU_DU_AN_GIU_CAN_KY_K2" else " | T-rtc-12" if g == "K2" and w in tt1 else ""
        main_counts = f"{w}={d[0]}/{d[2]}; " if not h7mode else ""
        c["bang_chung"] = f"{key(w)} | {main_counts}{'; '.join(brief)} | {compact(field_refs)}{owner}"
    save(E / "km1-doi-chung.tsv", detail, list(detail[0]))
    fields = ["loai", "tu_hoac_khoa", "de_xuat_astra", "ky_astra", "ly_do", "bang_chung"]
    save(OUT, cards, fields)
    new = {r["tu_hoac_khoa"].split(" / ")[0] for r in cards if r["de_xuat_astra"].startswith("THAY_")}
    blocked = {r["tu_hoac_khoa"] for r in cards if r["loai"] == "CO_TU_VAO" and r["ky_astra"] == "N"}
    assert not (new & out0) and all(labels[w]["lop"] != "F" and labels[w]["nhan"] == "OK" for w in out0 | new)
    assert set(pool).isdisjoint(out0 | new) and all(r["ngan"] == "OK_KHONG_F" for r in pool.values())
    oldsign = rows(U / "chu-ky.tsv")
    for w in OLD:
        assert {r["nguoi_ky"] for r in oldsign if r["tu"] == w and r["loai_ky"] == "K2" and r["hieu_luc"] == "CO"} == {"Astra", "Opus"}
        assert w not in yes_h7
    out_n, available = len(new | out0), len(set(pool) - blocked)
    assert len(cards) == 286 and len(out0) == 107 and len(pool) == 120
    bins = {g: dict(Counter(r["de_xuat_astra"] for r in cards if r["loai"] == g)) for g in SECTIONS}
    inputs = [U / f"ra-thay-chinh-{s}.tsv" for s in ("h7", "h5", "thay-the")]
    res = {"base": "0253bb0", "inputs_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
           "seed": "rtc-astra-km1-20261121", "sub_web_token_bases": [S, W], "phan_quyet": bins,
           "doi_chung": len(detail), "hnd_ghep_thanh_cong": len(cross), "K2_cu_hai_nguoi": OLD,
           "them_ra": sorted(new), "bo_ung_vien": sorted(blocked), "ra": out_n, "vao_toi_da": available,
           "thieu": max(0, out_n-available), "du_bi": max(0, available-out_n), "T7_chay": False}
    (E / "km1-kiem.json").write_bytes((json.dumps(res, ensure_ascii=False, indent=2) + "\n").replace("\n", "\r\n").encode("utf-8"))
    print(f"{len(cards)} ca; {len(detail)} đối chứng; {out_n} ghế / {available} nguồn / thiếu {res['thieu']}.")


if __name__ == "__main__":
    main()
