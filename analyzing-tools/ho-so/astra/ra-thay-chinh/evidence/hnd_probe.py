"""Đối số HND74K trong RAM; không lưu danh sách từ điển hoặc lời giải."""
import json
import importlib.util
import sys
import unicodedata as ud
import urllib.request
from collections import defaultdict

from screen_core import AT, EV, OLD_O, U, key, load, read, save_json, save_tsv, sha, tsv


def main():
    d = load()
    url = "https://raw.githubusercontent.com/duyet/vietnamese-wordlist/688b0953c8cdb21ee090ce80b83cefdb052fe2cd/Viet74K.txt"
    with urllib.request.urlopen(url, timeout=60) as response:
        payload = response.read()
    manifest = json.loads(read(AT / "manifest.json"))
    expected = next(r["sha256"] for r in manifest["nguon_du_lieu"] if r["source"] == "Viet74K")
    assert sha(payload) == expected
    forms = defaultdict(list)
    by_key = defaultdict(set)
    for line in payload.decode("utf-8-sig").splitlines():
        original = ud.normalize("NFC", line.strip()).replace("-", " ")
        if original:
            forms[original.lower()].append(original)
            if original == original.lower():
                by_key[key(original)].add(original)
    rows = []
    for n, r in enumerate(d["h5"], 1):
        alt = r["bien_the"]
        rows.append({
            "id": f"H5-{n:04d}", "tu": r["tu"], "bien_the": alt,
            "HND74_normalized": str(alt in forms),
            "HND74_lowercase_exact": str(alt in forms.get(alt, [])),
            "HND74_only_capitalized": str(alt in forms and alt not in forms[alt]),
            "source": url, "sha256_source": expected,
        })
    save_tsv(EV / "h5-hnd-membership.tsv", rows)
    saved = {(r["khoa"], r["tu"]) for r in d["opus-counts"]}
    extra = []
    for k, w in d["main_by_key"].items():
        for alt in sorted(by_key.get(k, set())):
            if alt != w and (k, alt) not in saved:
                extra.append({
                    "id": f"H7-H{len(extra)+1:04d}", "khoa": k, "tu_chinh": w,
                    "doc_khac": alt, "so_dem": "CHUA_DO",
                    "source": url, "sha256_source": expected,
                })
    if extra:
        save_tsv(EV / "h7-hnd-chua-dem.tsv", extra)
    candidates = {r["tu"]: r for r in d["du-phong-phan-loai"] if r["tang"] != "D"}
    candidates.update({r["tu"]: r for r in d["honorable-mentions"] if r["nhan_ho_so"] == "OK"})
    extra_candidates = []
    for w in sorted(candidates):
        for alt in sorted(by_key.get(key(w), set())):
            if alt != w:
                c = d["counts"].get(alt, {})
                extra_candidates.append({
                    "tu": w, "doc_khac": alt, "khoa": key(w),
                    "sub_sach": c.get("sub_sach", "CHUA_DO"),
                    "web_sach": c.get("web_sach", "CHUA_DO"),
                    "source": url, "sha256_source": expected,
                })
    save_tsv(EV / "ung-vien-doi-chung-H7.tsv", extra_candidates)
    sys.path.insert(0, str(OLD_O))
    spec = importlib.util.spec_from_file_location("old_h5_generator", OLD_O / "do-bien-the.py")
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)
    original_faces = set(forms) | set(d["main"]) | {r["tu"] for r in d["du-phong-phan-loai"]}
    original_faces.update(r["tu"] for r in d["opus-counts"])
    for stem in ("l2", "l2b", "l2c", "l3", "l2d"):
        original_faces.update(r["tu"] for r in tsv(U / f"{stem}-ung-vien.tsv"))
    original_faces.update(r["tu"] for r in tsv(U / "l3b-de-cu-opus.tsv"))
    original_canon = defaultdict(set)
    for face in original_faces:
        original_canon[generator.canon(face)].add(face)
    replay = {
        (w, alt) for w in d["main"] for canon in generator.word_variants(w)
        for alt in original_canon.get(canon, ()) if key(w) != key(alt)
    }
    assert replay == {(r["tu"], r["bien_the"]) for r in d["h5"]}
    canon_forms = defaultdict(set)
    for face, originals in forms.items():
        if face in originals:
            canon_forms[generator.canon(face)].add(face)
    new_h5 = []
    for w in sorted(candidates):
        for variant in sorted(generator.word_variants(w)):
            for other in sorted(canon_forms.get(variant, ())):
                if key(w) != key(other):
                    c = d["counts"].get(other, {})
                    new_h5.append({
                        "tu": w, "bien_the": other, "khoa": key(w), "khoa_bien_the": key(other),
                        "sub_sach_bien_the": c.get("sub_sach", "CHUA_DO"),
                        "web_sach_bien_the": c.get("web_sach", "CHUA_DO"),
                        "source": url, "sha256_source": expected,
                    })
    save_tsv(EV / "ung-vien-doi-chung-H5.tsv", new_h5)
    metrics = {
        "source": url, "sha256": sha(payload), "stored_source_text": False,
        "main_H5_pairs": len(rows),
        "H5_generator_replay_exact": True,
        "h5_HND_lowercase": sum(r["HND74_lowercase_exact"] == "True" for r in rows),
        "h5_HND_only_capitalized": sum(r["HND74_only_capitalized"] == "True" for r in rows),
        "h5_not_in_HND74": sum(r["HND74_normalized"] == "False" for r in rows),
        "additional_main_HND_readings_without_saved_count_row": len(extra),
        "replacement_candidate_words": len(candidates),
        "replacement_candidate_H5_pairs": len(new_h5),
        "replacement_candidate_H7_pairs": len(extra_candidates),
    }
    save_json(EV / "hnd-metrics.json", metrics)
    print(json.dumps(metrics, ensure_ascii=False, indent=2))
    print("CAPITALIZED ONLY:", [(r["tu"], r["bien_the"]) for r in rows if r["HND74_only_capitalized"] == "True"])
    print("ADDITIONAL H7:")
    for r in extra:
        print(r["id"], r["tu_chinh"], ">", r["doc_khac"])


if __name__ == "__main__":
    main()
