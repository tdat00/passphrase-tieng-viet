"""Rà D-dpv2-5: chỉ ghi nhãn, số đếm, hash và tham chiếu trong hồ sơ Astra."""
import argparse
import csv
import hashlib
import io
import json
import subprocess
import unicodedata as ud
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent.parent
EV = OUT / "evidence"
AT = ROOT / "analyzing-tools"
U = AT / "ho-so" / "unified"
OLD_O = AT / "ho-so" / "opus" / "du-phong-v2" / "evidence"
BASE = "1c3f504"
INPUTS = {}
ALPHA = "aăâbcdđeêghiklmnoôơpqrstuưvxy"
TONES = "\u0300\u0309\u0303\u0301\u0323"
SUB, WEB = 34314528, 149860716


def sha(b):
    return hashlib.sha256(b).hexdigest()


def key(w):
    return "".join(c for c in ud.normalize("NFD", w.lower())
                   if not ud.category(c).startswith("M")).replace("đ", "d").replace(" ", "")


def o1(w):
    out = []
    for syllable in w.split(" "):
        de = ud.normalize("NFD", syllable)
        tone = [1 + TONES.index(c) for c in de if c in TONES]
        base = ud.normalize("NFC", "".join(c for c in de if c not in TONES))
        out.append((tuple(ALPHA.index(c) for c in base), tone[0] if tone else 0))
    return tuple(out)


def read(p):
    b = p.read_bytes()
    INPUTS[str(p.relative_to(ROOT))] = {
        "sha256_bytes": sha(b), "sha256_LF": sha(b.replace(b"\r\n", b"\n")),
        "lines": b.count(b"\n"),
    }
    return b.decode("utf-8").replace("\r\n", "\n")


def tsv(p):
    rows = []
    for line, row in enumerate(csv.DictReader(io.StringIO(read(p)), delimiter="\t"), 2):
        row["_ref"] = f"{p.relative_to(ROOT)}:{line}"
        rows.append(row)
    return rows


def write(p, text):
    assert OUT in p.resolve().parents
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(("\r\n".join(x.rstrip(" \t") for x in text.splitlines()) + "\r\n").encode("utf-8"))


def save_json(p, data):
    write(p, json.dumps(data, ensure_ascii=False, indent=2))


def save_tsv(p, rows, fields=None):
    fields = fields or list(rows[0])
    s = io.StringIO()
    w = csv.DictWriter(s, fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows({k: "-" if r.get(k) in ("", None) else str(r[k]) for k in fields} for r in rows)
    write(p, s.getvalue())


def ppm(r, sub=SUB, web=WEB):
    return (Fraction(int(r["sub_sach"]), sub) + Fraction(int(r["web_sach"]), web)) * 500000


def load():
    d = {"main": [x.split("|", 1)[0] for x in read(AT / "wordlist.txt").splitlines()]}
    d["main_by_key"] = {key(w): w for w in d["main"]}
    for stem in ("labels", "du-phong-phan-loai", "honorable-mentions", "blocked_keys",
                 "spelling_families", "nguon-goc-giai-nghia", "d6-ho-chinh-ta"):
        d[stem] = tsv(AT / f"{stem}.tsv")
    for stem in ("opus-counts", "canh-bao-khong-dau", "xep-hang", "phieu-astra",
                 "phieu-opus", "chu-ky", "phan-bien"):
        d[stem] = tsv(U / f"{stem}.tsv")
    d["h5"] = tsv(OLD_O / "bien-the-chinh-tho.tsv")
    d["h7"] = tsv(OLD_O / "pham-vi-hau-kiem-h7.tsv")
    d["counts"] = {}
    for r in d["opus-counts"]:
        d["counts"].setdefault(r["tu"], r)
        if r["vai_tro"] == "UNG_VIEN":
            d["counts"][r["tu"]] = r
    for short in ("l2", "l2b", "l2c", "l3"):
        for r in tsv(U / f"{short}-ung-vien.tsv"):
            d["counts"].setdefault(r["tu"], r)
    d["label_by_word"] = {r["tu"]: r for r in d["labels"]}
    d["rank_by_word"] = {r["tu"]: r for r in d["xep-hang"]}
    d["alarm_pairs"] = {(r["khoa"], r["doc_khac"]) for r in d["canh-bao-khong-dau"]}
    d["all_h7"] = [r for r in d["opus-counts"] if r["vai_tro"] == "DOC_KHAC"
                   and r["khoa"] in d["main_by_key"] and r["tu"] != d["main_by_key"][r["khoa"]]]
    for stem in ("tieu-chi-thong-nhat.md", "huong-dan-giai-nghia.md", "README.md",
                 "manifest.json", "check_wordlist.py", "verify.mjs", "build_wordlist.py",
                 "kiem-tra-giai-nghia.py", "d6-kiem.py", "d6-tham-chieu.json"):
        read(AT / stem)
    read(U / "ra-thay-chinh-yeu-cau.md")
    return d


def inventory(d):
    assert len(d["main"]) == len(d["main_by_key"]) == 7776
    assert len(d["h5"]) == len({(r["tu"], r["bien_the"]) for r in d["h5"]}) == 632
    assert len({r["tu"] for r in d["h5"]}) == 474
    expected = {(r["khoa"], r["tu_chinh"], r["doc_khac"]) for r in d["h7"]}
    reconstructed = set()
    for r in d["all_h7"]:
        if ppm(r) >= Fraction(3, 10) and (r["khoa"], r["tu"]) not in d["alarm_pairs"]:
            reconstructed.add((r["khoa"], d["main_by_key"][r["khoa"]], r["tu"]))
    assert reconstructed == expected and len(expected) == 1177
    assert len({x[0] for x in expected}) == 634
    sensitivity = {(r["khoa"], d["main_by_key"][r["khoa"]], r["tu"])
                   for r in d["all_h7"] if ppm(r, 34329387, 150070912) >= Fraction(3, 10)
                   and (r["khoa"], r["tu"]) not in d["alarm_pairs"]}
    assert sensitivity == expected
    extra = []
    for r in d["all_h7"]:
        w = d["main_by_key"][r["khoa"]]
        if (r["khoa"], w, r["tu"]) in expected:
            continue
        own = d["counts"].get(w)
        extra.append({
            "id": f"H7-X{len(extra)+1:04d}", "khoa": r["khoa"], "tu_chinh": w,
            "doc_khac": r["tu"], "sub_sach": r["sub_sach"], "web_sach": r["web_sach"],
            "ppm": f"{float(ppm(r)):.9f}",
            "ge_tu_chinh": "CHUA_DO" if own is None else str(ppm(r) >= ppm(own)),
            "da_co_coi": str((r["khoa"], r["tu"]) in d["alarm_pairs"]),
            "bang_chung": r["_ref"],
        })
    save_tsv(EV / "h7-mo-rong-dau-vao.tsv", extra)
    protected = {}
    for p in (ROOT / "index.html", ROOT / "thong-tin.html", ROOT / "WordListAnalyze.md",
              ROOT / "README.md", AT / "wordlist.txt", AT / "du-phong.txt", AT / "labels.tsv",
              AT / "nguon-goc-giai-nghia.tsv", AT / "spelling_families.tsv",
              AT / "blocked_keys.tsv", AT / "manifest.json", AT / "du-phong-phan-loai.tsv",
              AT / "honorable-mentions.tsv", AT / "README.md", AT / "check_wordlist.py",
              AT / "verify.mjs", AT / "build_wordlist.py", AT / "d6-kiem.py",
              AT / "d6-ho-chinh-ta.tsv", AT / "d6-tham-chieu.json",
              AT / "huong-dan-giai-nghia.md", AT / "tieu-chi-thong-nhat.md",
              ROOT / "WordListAnalyze-Opus.md", ROOT / "WordListAnalyze-Astra.md"):
        b = p.read_bytes()
        rel = str(p.relative_to(ROOT))
        blob = subprocess.check_output(["git", "show", f"{BASE}:{rel.replace(chr(92), '/')}"], cwd=ROOT)
        assert b.replace(b"\r\n", b"\n") == blob.replace(b"\r\n", b"\n"), rel
        protected[rel] = {"sha256_bytes": sha(b), "sha256_LF": sha(b.replace(b"\r\n", b"\n"))}
    old = EV / "protected-baseline.json"
    if old.exists():
        previous = json.loads(old.read_text(encoding="utf-8"))
        assert all(protected[k] == v for k, v in previous.items())
    save_json(old, protected)
    result = {
        "base_commit": subprocess.check_output(["git", "rev-parse", BASE], cwd=ROOT).decode().strip(),
        "H5": {"pairs": 632, "main_words": 474},
        "H7": {"pairs": 1177, "keys": 634, "recomputed_exact": True,
               "both_denominators_same_scope": True, "all_saved_main_pairs": len(d["all_h7"]),
               "all_saved_main_keys": len({r["khoa"] for r in d["all_h7"]}),
               "extended_pairs": len(extra)},
        "baotu_main": d["main_by_key"].get("baotu"),
        "baotu_registered": any(r["khoa"] == "baotu" for r in d["blocked_keys"]),
        "A_by_class": Counter(r["lop"] for r in d["du-phong-phan-loai"] if r["tang"] == "A"),
        "main_classes": Counter(d["label_by_word"][w]["lop"] for w in d["main"]),
        "main_labels": Counter(d["label_by_word"][w]["nhan"] for w in d["main"]),
        "D6_dump_available": (AT / "vi.jsonl.gz").exists(),
    }
    save_json(EV / "inventory.json", result)
    save_json(EV / "inputs.json", INPUTS)
    return result


if __name__ == "__main__":
    print(json.dumps(inventory(load()), ensure_ascii=False, indent=2))
