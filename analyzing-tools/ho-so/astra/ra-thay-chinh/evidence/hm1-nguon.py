"""Đối HND/Kaikki ghim trong RAM. Tệp ra chỉ có đầu mục trong ca, cờ, nhãn, băm và số."""
import argparse
import csv
import gzip
import hashlib
import importlib.util
import io
import itertools
import json
import re
import sys
import unicodedata as ud
import urllib.request
from collections import defaultdict
from pathlib import Path

from screen_core import AT, EV, ROOT, U, key, save_json, save_tsv

OD = AT / "ho-so" / "opus" / "du-phong-v2" / "evidence"
TONE = "\u0300\u0309\u0303\u0301\u0323"


def read(p):
    with p.open(encoding="utf-8-sig", newline="") as f:
        return [dict(r, ref=f"{p.relative_to(ROOT)}:{n}", n=n) for n, r in enumerate(csv.DictReader(f, delimiter="\t"), 2)]


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "VietnameseWordlistReview/1.0"}), timeout=80) as r:
        return r.read()


def shape(w):
    return key(w).replace("-", "").replace("‐", "").replace("‑", "")


def interchange(w):
    pools = []
    for syll in w.split(" "):
        tx = ud.normalize("NFD", syll)
        tone = "".join(c for c in tx if c in TONE)
        base = ud.normalize("NFC", "".join(c for c in tx if c not in TONE))
        pair = [syll]
        if re.fullmatch("(?:qu|[hklmst])[iy]", base):
            pair.append(ud.normalize("NFC", base[:-1] + ("i" if base[-1] == "y" else "y") + tone))
        pools.append(pair)
    return {" ".join(z) for z in itertools.product(*pools)} - {w}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rank-max", type=int, required=True)
    ap.add_argument("--inspect", action="store_true")
    ap.add_argument("--inspect-h6", action="store_true")
    args = ap.parse_args()
    rank = {r["tu"]: int(r["hang"]) for r in read(U / "xep-hang.tsv")}
    hh = sorted((r for r in read(AT / "honorable-mentions.tsv") if r["nhan_ho_so"] == "OK"
                 and rank[r["tu"]] <= args.rank_max), key=lambda r: rank[r["tu"]])
    target = {r["tu"]: r for r in hh}
    bykey = {key(w): w for w in target}
    sys.path.insert(0, str(OD))
    spec = importlib.util.spec_from_file_location("rtc_variants", OD / "do-bien-the.py")
    gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)
    variants = defaultdict(set)
    for w in target:
        for val in gen.word_variants(w) | {gen.canon(x) for x in interchange(w)}:
            variants[val].add(w)
    feat = defaultdict(set)
    def tag(face, source):
        face = ud.normalize("NFC", face.strip())
        n = face.lower()
        j = shape(n)
        if j in bykey:
            w = bykey[j]
            cat = "H3" if n == w else "H5g" if n.replace("-", " ") == w or n.replace(" ", "") == w.replace(" ", "") else "H7"
            feat[(w, cat, face)].add(source)
        canon = gen.canon(n.replace("-", " "))
        for w in variants.get(canon, ()):
            if shape(n) != key(w):
                feat[(w, "H5", face)].add(source)
    manifest = json.loads((AT / "manifest.json").read_text(encoding="utf-8"))
    pins = {r["source"]: r for r in manifest["nguon_du_lieu"]}
    inputs = []
    for ht in ("Viet11K", "Viet22K", "Viet39K", "Viet74K"):
        pin = pins[ht]
        url = pin["url"].replace("github.com/", "raw.githubusercontent.com/").replace("/blob/", "/")
        raw = get(url)
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == pin["sha256"]
        inputs.append({"source": ht, "url": url, "sha256": digest})
        for line in raw.decode("utf-8-sig").splitlines():
            tag(line, ht)
    lex = defaultdict(list)
    cache = {}
    for language, suffix in (("vi", "/viwiktionary/raw-wiktextract-data.jsonl.gz"),
                             ("en", "/dictionary/Vietnamese/kaikki.org-dictionary-Vietnamese.jsonl.gz")):
        src = next(k for k in pins if k.startswith("Kaikki " + language))
        url = "https://kaikki.org" + suffix
        raw = get(url)
        payload = gzip.decompress(raw)
        digest = hashlib.sha256(raw if language == "vi" else payload).hexdigest()
        assert digest == pins[src]["sha256"], (src, digest)
        inputs.append({"source": src, "url": url, "sha256": digest, "hash_of": "gzip" if language == "vi" else "jsonl"})
        for ln, line in enumerate(io.BytesIO(payload), 1):
            x = json.loads(line)
            if x.get("lang_code") != "vi" or not x.get("word"):
                continue
            face = ud.normalize("NFC", x["word"])
            tag(face, "W" + language.upper())
            n = face.lower()
            linked = {ud.normalize("NFC", a["word"].strip()).lower() for s in x.get("senses", [])
                      for a in s.get("alt_of", []) if a.get("word")}
            for other in linked & target.keys():
                if other != n:
                    feat[(other, "H5_REF", face)].add("W" + language.upper())
            if n in target:
                for other in linked - {n}:
                    feat[(n, "H5_REF", other)].add("W" + language.upper())
            interested = shape(n) in bykey or gen.canon(n.replace("-", " ")) in variants or bool(linked & target.keys())
            if not interested:
                continue
            groups, desc, alt_of = set(), [], set()
            for sense in x.get("senses", []):
                desc.extend(sense.get("glosses", []))
                groups.update(sense.get("tags", []))
                groups.update(sense.get("raw_tags", []))
                alt_of.update(a["word"] for a in sense.get("alt_of", []) if a.get("word"))
            lex[face].append(f"W{language.upper()}:{ln}:{x.get('pos','-')}:{hashlib.sha256(line).hexdigest()}")
            cache[face, language, ln] = (desc, groups, alt_of)
    freq = {}
    for r in read(U / "opus-counts.tsv"):
        if r["tu"] not in freq or r["vai_tro"] == "UNG_VIEN":
            freq[r["tu"]] = r
        if r["khoa"] in bykey and r["vai_tro"] == "DOC_KHAC":
            tag(r["tu"], "DOC_KHAC")
        if gen.canon(r["tu"]) in variants:
            tag(r["tu"], "OPUS_MOI_VAI")
    for st in ("l2", "l2b", "l2c", "l2d", "l3"):
        for r in read(U / f"{st}-ung-vien.tsv"):
            freq.setdefault(r["tu"], r)
            if shape(r["tu"]) in bykey or gen.canon(r["tu"]) in variants:
                tag(r["tu"], "LO_" + st)
    for r in read(U / "canh-bao-khong-dau.tsv"):
        if r["ung_vien"] in target:
            tag(r["doc_khac"], "CANH_BAO")
    for w in target:
        for alt in interchange(w):
            feat[(w, "H5b", alt)].add("LUAT_B")
    out = []
    for (w, gate, alt), sources in sorted(feat.items(), key=lambda p: (rank[p[0][0]], p[0][1], p[0][2])):
        c = freq.get(alt.lower())
        po = (500000 * (int(c["sub_sach"]) / 34314528 + int(c["web_sach"]) / 149860716)) if c else None
        senses = [(f"{lang}:{ln}:" + ",".join(sorted(tags))) for (x, lang, ln), (_, tags, _) in cache.items() if x == alt and tags]
        alts = sorted({q for (x, _, _), (_, _, relatives) in cache.items() if x == alt for q in relatives if q in target})
        has_lex = any(desc and "no-gloss" not in tags for (face, _, _), (desc, tags, _) in cache.items() if face == alt)
        out.append(dict(hang=rank[w], tu=w, cong=gate, doi_chung=alt, nguon=";".join(sorted(sources)), co_nghia_Kaikki=int(has_lex),
                        nguon_Kaikki=";".join(lex[alt]) or "-", nhan_tho=";".join(senses) or "-",
                        alt_trong_tap=";".join(alts) or "-", sub=c["sub_sach"] if c else "-",
                        web=c["web_sach"] if c else "-", ppm=f"{po:.6f}" if c else "CHUA_DO",
                        nguon_so=c["ref"] if c else "-"))
    save_tsv(EV / "hm1-doi-chung.tsv", out)
    save_json(EV / "hm1-nguon-ghim.json", {"ghim": inputs, "hnd_cau_tho_da_luu": False, "nguong_hang_quet": args.rank_max})
    for w in target:
        pieces = [f"{r['cong']}:{r['doi_chung']}({r['ppm']})" for r in out if r["tu"] == w and r["cong"] != "H3"]
        print(f"{rank[w]} {w}: " + (", ".join(pieces) or "-"))
    if args.inspect:
        for w in sorted(target, key=rank.get):
            labels = {w} | {r["doi_chung"] for r in out if r["tu"] == w and r["doi_chung"].islower()}
            for (face, lg, idx), (dest, tags, _) in cache.items():
                if face in labels and dest and (face != w or w in {"ngắn gọn", "cơ quan", "lực lượng"}):
                    print(f"{w} <> {face} {lg}@{idx}: {' | '.join(dest)[:175]}")
    if args.inspect_h6:
        for w in sorted(target, key=rank.get):
            desc = [t for (word, lang, _), (senses, _, _) in cache.items() if word == w and lang == "en" for t in senses]
            print(f"H6 {w}: " + " / ".join(t[:90] for t in desc)[:300])


if __name__ == "__main__":
    main()
