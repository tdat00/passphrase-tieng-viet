"""Đối số review Opus; chỉ lưu hash, số đo, nhãn và tham chiếu."""
import hashlib
import json
from collections import Counter
from fractions import Fraction

from inventory import EV, INPUTS, ROOT, TOOLS, UNIFIED, key, read, save_json, save_tsv, tsv

OE = TOOLS / "ho-so" / "opus" / "du-phong-v2" / "evidence"


def ppm(row, sub, web):
    return (Fraction(int(row["sub_sach"]), sub) + Fraction(int(row["web_sach"]), web)) * 500_000


def main():
    history = EV / "revision-1-question-history.json"
    if not history.exists():
        source = UNIFIED / "du-phong-v2-cau-hoi.md"
        payload = source.read_bytes()
        save_json(history, {"source": str(source.relative_to(ROOT)),
                            "sha256_bytes_before_revision": hashlib.sha256(payload).hexdigest(),
                            "text_before_revision": payload.decode("utf-8"),
                            "note": "Giữ câu hỏi gốc trước khi rút các mục đã đóng; chưa có commit nháp gốc."})
    else:
        archive = json.loads(history.read_text(encoding="utf-8"))
        source = UNIFIED / "du-phong-v2-cau-hoi.md"
        payload = source.read_bytes()
        if "## Q-dpv2-7" in payload.decode("utf-8") and "before_accept_luot2" not in archive:
            archive["before_accept_luot2"] = {
                "sha256_bytes": hashlib.sha256(payload).hexdigest(),
                "text": payload.decode("utf-8"),
            }
            save_json(history, archive)
    main_words = [line.split("|")[0] for line in read(TOOLS / "wordlist.txt").splitlines()]
    main_by_key = {key(word): word for word in main_words}
    alarms = tsv(UNIFIED / "canh-bao-khong-dau.tsv")
    alarm_pairs = {(r["khoa"], r["doc_khac"]) for r in alarms}
    counts = tsv(UNIFIED / "opus-counts.tsv")
    h5_rows = tsv(OE / "bien-the-chinh-tho.tsv")
    assert len(h5_rows) == len({(r["tu"], r["bien_the"]) for r in h5_rows}) == 632
    assert len({r["tu"] for r in h5_rows}) == 474
    assert all(r["tu"] in main_words for r in h5_rows)
    audit_saved = tsv(OE / "pham-vi-hau-kiem-h7.tsv")
    expected = {(r["khoa"], r["tu_chinh"], r["doc_khac"]) for r in audit_saved}
    missing = {}
    for mode, sub, web in (("muc0", 34_314_528, 149_860_716), ("P2", 34_329_387, 150_070_912)):
        pairs = {
            (r["khoa"], main_by_key[r["khoa"]], r["tu"])
            for r in counts
            if r["vai_tro"] == "DOC_KHAC" and r["khoa"] in main_by_key
            and ppm(r, sub, web) >= Fraction(3, 10)
            and (r["khoa"], r["tu"]) not in alarm_pairs
        }
        assert pairs == expected and not any(a == b for _, a, b in pairs)
        missing[mode] = {"pairs": len(pairs), "keys": len({r[0] for r in pairs})}
    selected = {"tần số", "tận số", "vậy nên", "vảy nến", "ngoại trừ", "ngoại trú", "móng", "mông"}
    pair_rows = []
    for r in counts:
        if r["tu"] not in selected:
            continue
        pair_rows.append({
            "tu": r["tu"], "khoa": r["khoa"], "sub_sach": r["sub_sach"], "web_sach": r["web_sach"],
            "ppm_mau_so_muc0": f"{float(ppm(r, 34_314_528, 149_860_716)):.9f}",
            "ppm_mau_so_P2": f"{float(ppm(r, 34_329_387, 150_070_912)):.9f}",
            "nguon": r["_ref"],
        })
    save_tsv(EV / "revision-1-h7-counts.tsv", list(pair_rows[0]), pair_rows)
    six = {"cơ quan", "lực lượng", "truy tìm", "dự bị", "lên chức", "đại lục"}
    votes = []
    for who in ("opus", "astra"):
        for r in tsv(UNIFIED / f"phieu-{who}.tsv"):
            if r["tu"] in six:
                assert r["nhan"] == ("R1" if r["tu"] == "đại lục" else "OK")
                votes.append({"tu": r["tu"], "nguoi": who, "nhan": r["nhan"], "lop": r["lop"], "nguon": r["_ref"]})
    assert len(votes) == 12
    objections = [r for r in tsv(UNIFIED / "phan-bien.tsv") if r["tu"] in six]
    assert not objections
    save_tsv(EV / "revision-1-h6-six-votes.tsv", ["tu", "nguoi", "nhan", "lop", "nguon"], votes)
    legacy = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
              for name in ("WordListAnalyze-Opus.md", "WordListAnalyze-Astra.md")}
    read(OE.parent / "round-1-review-drafts.md")
    read(OE / "pham-vi-hau-kiem.py")
    read(OE / "h7-quet-bo-sung.py")
    read(EV / "revision-1-chu-ky-astra.tsv")
    read(EV / "revision-1-h7-ngoaitru.tsv")
    result = {
        "h5_raw_pairs": 632, "h5_distinct_main_words": 474,
        "h7_independent_match": missing,
        "alarm_rows": len(alarms), "alarm_keys": len({r["khoa"] for r in alarms}),
        "h7_warning": "Chưa phân loại nghĩa đỏ của 1.177 cặp; không gọi đây là 1.177 lỗi hay còi bị bỏ sót.",
        "six_word_historical_votes": Counter(r["nhan"] for r in votes),
        "six_word_objections_in_saved_P4_table": len(objections),
        "K2_Astra_signatures": ["tần số", "vậy nên"],
        "agreed_H7_hold": "ngoại trừ / ngoại trú: C/CHO_H7; Q-dpv2-7 đã đóng, chưa ký mức K trước khi đo",
        "legacy_files_sha256_bytes": legacy,
    }
    if (EV / "revision-1-audit.json").exists():
        old = json.loads((EV / "revision-1-audit.json").read_text(encoding="utf-8"))
        assert old["legacy_files_sha256_bytes"] == legacy
    save_json(EV / "revision-1-audit.json", result)
    save_json(EV / "revision-1-audit-inputs.json", INPUTS)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
