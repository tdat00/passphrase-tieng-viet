"""Bước 2: dò biến thể chính tả (H5) mà quét 6.1 có thể bỏ sót, cho 205 dự phòng và bảng đề cử.

Quét 6.1 chỉ đổi MỘT chỗ mỗi lần và không đổi vần. Ở đây áp cùng một phép đổi cho một hoặc mọi âm tiết,
thêm đổi âm cuối rộng hơn và chèn/bỏ âm đệm (e/oe, a/oa, ă/oă, ê/uê, i/uy). Chỉ báo các dạng có thật trong
danh sách chính, dự phòng, bảng P1, các lô L2–L3b hoặc bảng đếm OPUS. Người duyệt phải đọc từng cặp.

    python do-bien-the.py <tệp danh sách từ, mỗi dòng một từ | CHINH (cột từ của wordlist.txt)> <tệp TSV ra>
"""
import itertools
import sys
import unicodedata
from chung import *

out_utf8()
TONE_MARKS = set(TONES)
INITIAL = [("ch", "tr"), ("s", "x"), ("d", "gi"), ("d", "r"), ("gi", "r"), ("l", "n"), ("v", "d"), ("ch", "th"), ("c", "k")]
FINAL = [("c", "t"), ("ch", "t"), ("n", "ng"), ("nh", "n"), ("i", "c"), ("u", "o"), ("m", "n"), ("p", "t")]
GLIDE = [("e", "oe"), ("a", "oa"), ("ă", "oă"), ("ê", "uê"), ("i", "uy"), ("eo", "e")]
ONSETS = sorted(["ngh", "ng", "nh", "ch", "tr", "th", "kh", "ph", "gh", "gi", "qu", "b", "c", "d", "đ", "g", "h", "k", "l", "m",
                 "n", "p", "r", "s", "t", "v", "x"], key=len, reverse=True)
FINALS = sorted(["ch", "ng", "nh", "c", "m", "n", "p", "t", "i", "y", "o", "u"], key=len, reverse=True)


def split_tone(syl):
    tone = ""
    base = ""
    for ch in unicodedata.normalize("NFD", syl):
        if ch in TONE_MARKS:
            tone = ch
        else:
            base += ch
    return unicodedata.normalize("NFC", base), tone


def parts(base):
    on = next((o for o in ONSETS if base.startswith(o)), "")
    rest = base[len(on):]
    fi = next((f for f in FINALS if rest.endswith(f) and len(rest) > len(f)), "")
    nucleus = rest[:len(rest) - len(fi)] if fi else rest
    return on, nucleus, fi


def canon_syl(syl):
    base, tone = split_tone(syl)
    return base + "|" + tone


def canon(w):
    return " ".join(canon_syl(s) for s in w.split(" "))


def syl_variants_canon(syl):
    base, tone = split_tone(syl)
    on, nu, fi = parts(base)
    out = set()
    for a, b in INITIAL:
        for x, y in ((a, b), (b, a)):
            if on == x:
                out.add(y + nu + fi + "|" + tone)
    for a, b in FINAL:
        for x, y in ((a, b), (b, a)):
            if fi == x:
                out.add(on + nu + y + "|" + tone)
    for a, b in GLIDE:
        for x, y in ((a, b), (b, a)):
            if nu == x:
                out.add(on + y + fi + "|" + tone)
    if tone in ("\u0309", "\u0303"):
        out.add(base + "|" + ("\u0303" if tone == "\u0309" else "\u0309"))
    out.discard(canon_syl(syl))
    return out


def word_variants(w):
    """Tập dạng chuẩn tắc (mỗi âm tiết = chữ không thanh|thanh) của các biến thể; một phép đổi áp cho một hay mọi âm tiết."""
    syls = w.split(" ")
    opts = [[canon_syl(s)] + sorted(syl_variants_canon(s)) for s in syls]
    me = canon(w)
    res = set()
    for combo in itertools.product(*opts):
        v = " ".join(combo)
        if v != me:
            res.add(v)
    return res


def known_faces():
    faces = {}
    for w in (l.split("|")[0] for l in lines(AT / "wordlist.txt")):
        faces[w] = "CHINH"
    for w in lines(AT / "du-phong.txt"):
        faces.setdefault(w, "DU_PHONG")
    for r in rd(U / "opus-counts.tsv"):
        faces.setdefault(r["tu"], "DEM_OPUS:" + r["vai_tro"])
    for f in ["l2-ung-vien.tsv", "l2b-ung-vien.tsv", "l2c-ung-vien.tsv", "l3-ung-vien.tsv", "l2d-ung-vien.tsv", "l3b-de-cu-opus.tsv"]:
        for r in rd(U / f):
            faces.setdefault(r["tu"], "LO:" + f.split("-")[0])
    hnd = HND_DIR / "Viet74K.txt"
    if hnd.exists():  # bản tạm, chỉ để tra; không lưu vào repo
        for l in open(hnd, encoding="utf-8"):
            w = unicodedata.normalize("NFC", l.strip().lower()).replace("-", " ")
            if w:
                faces.setdefault(w, "HND74K")
    return faces


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    words = [l.split("|")[0] for l in lines(AT / "wordlist.txt")] if src == "CHINH" else lines(src)
    faces = known_faces()
    oc = {r["tu"]: r for r in rd(U / "opus-counts.tsv")}
    fam_known = {(r["chuan"], r["bien_the"]) for r in rd(AT / "spelling_families.tsv")}
    fam_known |= {(b, a) for a, b in fam_known}
    d6 = {(r["dang_A"], r["dang_B"]) for r in rd(AT / "d6-ho-chinh-ta.tsv")}
    d6 |= {(b, a) for a, b in d6}
    by_canon = {}
    for f in faces:
        by_canon.setdefault(canon(f), []).append(f)
    rows = []
    for w in words:
        for cv in sorted(word_variants(w)):
            for v in by_canon.get(cv, []):
                if key(v) == key(w):
                    continue
                c = oc.get(v, {})
                cw = oc.get(w, {})
                rows.append({"tu": w, "bien_the": v, "noi_co_mat": faces[v], "da_dang_ky_H5": "Y" if (w, v) in fam_known else "",
                             "trong_ho_d6": "Y" if (w, v) in d6 else "",
                             "sub_sach_tu": cw.get("sub_sach", ""), "web_sach_tu": cw.get("web_sach", ""),
                             "sub_sach_bien_the": c.get("sub_sach", ""), "web_sach_bien_the": c.get("web_sach", "")})
    write_tsv(dst, ["tu", "bien_the", "noi_co_mat", "da_dang_ky_H5", "trong_ho_d6", "sub_sach_tu", "web_sach_tu",
                    "sub_sach_bien_the", "web_sach_bien_the"], rows)
    print(len(words), "từ;", len(rows), "cặp có dạng kia đã biết")
    for r in rows:
        print(r["tu"], "->", r["bien_the"], r["noi_co_mat"], r["da_dang_ky_H5"], r["trong_ho_d6"], r["sub_sach_tu"], r["web_sach_tu"], r["sub_sach_bien_the"], r["web_sach_bien_the"], sep=" | ")
