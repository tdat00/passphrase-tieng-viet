"""Đối số tiền lệ HND trong RAM; chỉ lưu membership của các họ đã có ở repo."""
import hashlib
import json
import unicodedata
import urllib.request
from collections import Counter

from screen_core import AT, EV, save_json, save_tsv, tsv


def main():
    specs = json.loads((EV / "cr1-source-metrics.json").read_text(encoding="utf-8"))["HND_sources"]
    sets, sources = {}, []
    for spec in specs:
        request = urllib.request.Request(spec["url"], headers={"User-Agent": "VietnameseWordlistReview/1.0"})
        with urllib.request.urlopen(request, timeout=40) as response:
            data = response.read()
        digest = hashlib.sha256(data).hexdigest()
        assert digest == spec["sha256"]
        words = {unicodedata.normalize("NFC", line.strip()) for line in data.decode("utf-8").splitlines()}
        sets[spec["source"]] = {w for w in words if w and w == w.lower()}
        sources.append({"source": spec["source"], "url": spec["url"], "sha256": digest, "raw_saved": False})
    rows = []
    counts = {"exact_cell": Counter(), "expanded_aliases_any": Counter()}
    for family in tsv(AT / "spelling_families.tsv"):
        kind = family["loai_H5"]
        if kind not in {"c", "d"}:
            continue
        exact = [family["bien_the"]]
        aliases = family["bien_the"].split(" / ")

        def qualifies(word):
            return (word in sets["Viet39K"] or word in sets["Viet74K"]) and word not in sets["Viet11K"] and word not in sets["Viet22K"]

        exact_ok = any(qualifies(w) for w in exact)
        alias_ok = any(qualifies(w) for w in aliases)
        if exact_ok:
            counts["exact_cell"][kind] += 1
        if alias_ok:
            counts["expanded_aliases_any"][kind] += 1
        if not (exact_ok or alias_ok):
            continue
        rows.append({
            "chuan": family["chuan"], "bien_the": family["bien_the"], "loai": kind,
            "ket_luan": family["ket_luan"], "nguon": family["_ref"],
            "exact_cell_only_large_HND": exact_ok,
            "any_alias_only_large_HND": alias_ok,
            "Viet11K_any_alias": any(w in sets["Viet11K"] for w in aliases),
            "Viet22K_any_alias": any(w in sets["Viet22K"] for w in aliases),
            "Viet39K_any_alias": any(w in sets["Viet39K"] for w in aliases),
            "Viet74K_any_alias": any(w in sets["Viet74K"] for w in aliases),
        })
    save_tsv(EV / "rd2-HND-tien-le.tsv", rows)
    summary = {
        "predicate": "loai c/d; dạng kia có ở Viet39K hoặc Viet74K chữ thường và không ở Viet11K/Viet22K; không suy không có ở Wiktionary",
        "counts": {mode: dict(count) for mode, count in counts.items()},
        "sources": sources, "raw_source_saved": False,
        "limit": "Phép đếm tiền lệ không tự chứng minh quan hệ cùng từ hay tính chuẩn của một cặp mới.",
    }
    save_json(EV / "rd2-HND-summary.json", summary)
    print(json.dumps(summary["counts"], ensure_ascii=False))


if __name__ == "__main__":
    main()
