"""Đóng hồ sơ duyệt nháp; xác nhận không sửa bản nháp hoặc dữ liệu sản phẩm."""
import hashlib
import json
import re
from datetime import datetime

from screen_core import AT, EV, OUT, ROOT, U, load, save_json, save_tsv, tsv


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    d = load()
    protected = json.loads((EV / "protected-baseline.json").read_text(encoding="utf-8"))
    assert all(digest(ROOT / p) == h["sha256_bytes"] for p, h in protected.items())
    inputs = json.loads((EV / "rd1-input-hashes.json").read_text(encoding="utf-8"))
    assert all(digest(ROOT / p) == h for p, h in inputs.items())
    independent = tsv(EV / "artifact-index.tsv")
    assert all(digest(ROOT / r["tep"]) == r["sha256_bytes"] for r in independent)
    review = OUT / "round-1-review-drafts.md"
    text = review.read_text(encoding="utf-8")
    assert "Kết luận: changes requested" in text
    for i in range(1, 9):
        assert f"### R{i} " in text
    rulings = tsv(EV / "rd1-H7-phan-xu.tsv")
    assert len(rulings) == len({r["khoa"] for r in rulings}) == 60
    assert sum(r["Astra_duyet_nhap"] == "GIU_PHAN_DOI_K1" for r in rulings) == 30
    assert sum(r["Astra_duyet_nhap"] in {"NHAN_HUONG_GIU_H7", "NHAN_K2_CU"} for r in rulings) == 29
    assert next(r for r in rulings if r["tu"] == "thái")["Astra_duyet_nhap"] == "NHAN_K1"
    assert "rầm rầm" in d["main"] and "rần rần" not in d["main"]
    assert len(tsv(EV / "rd1-H5-phan-xu.tsv")) == 12
    assert len(tsv(EV / "rd1-H5-quan-he-bo-sung.tsv")) == 5
    old_k2 = {
        w: sum(r["tu"] == w and r["loai_ky"] == "K2" and r["hieu_luc"] == "CO" for r in d["chu-ky"])
        for w in ("mát mắt", "đón dâu", "kính")
    }
    assert old_k2 == {"mát mắt": 0, "đón dâu": 0, "kính": 2}
    questions = (U / "ra-thay-chinh-cau-hoi.md").read_text(encoding="utf-8")
    answers = [line for line in questions.splitlines() if line.startswith("**Answer")]
    assert len(answers) == 5 and all(re.fullmatch(r"\*\*Answer \([^)]*\):\*\*", s) for s in answers)
    records = [review, EV / "dictionary-rd1-h7-extra.tsv"]
    records += [p for p in EV.glob("rd1-*") if p.is_file()]
    for path in records:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        assert not raw.startswith(b"\xef\xbb\xbf"), str(path)
        assert raw.endswith(b"\r\n"), str(path)
        assert b"\n" not in raw.replace(b"\r\n", b""), str(path)
        assert b"\r" not in raw.replace(b"\r\n", b""), str(path)
        assert all(line == line.rstrip(" \t") for line in text.splitlines()), str(path)
    for name in ("rd1-dictionary-metadata.tsv", "dictionary-rd1-h7-extra.tsv"):
        columns = set(tsv(EV / name)[0]) - {"_ref"}
        assert not columns & {"wikitext", "gloss", "giai_nghia", "content", "text"}
    summary = {
        "checked_at": datetime.now().astimezone().isoformat(),
        "protected_files_unchanged": len(protected),
        "draft_input_files_unchanged": len(inputs),
        "independent_artifacts_unchanged": len(independent),
        "H7_reviewed": 60, "H7_keep_concessions": 29, "H7_replace_concession": "thái",
        "H7_disputed": 30, "H7_other_pending": 46,
        "H5_direct_unclosed_words": 11, "H5_adjudication": 8, "H5_measurement": 3,
        "H5_other_relations_pending": 14,
        "K2_precedent_active_signature_rows": old_k2,
        "new_release_signatures_written": 0,
        "new_glosses_written": 0, "raw_source_saved": False,
        "question_answer_lines_blank": 5,
        "format": "UTF-8 without BOM; CRLF; no trailing whitespace; final newline",
        "report_sha256_bytes": digest(review),
        "status": "PASS_REVIEW_ARTIFACTS_NOT_RELEASE",
    }
    save_json(EV / "rd1-finish-summary.json", summary)
    paths = [review, EV / "dictionary-rd1-h7-extra.tsv"]
    paths += [p for p in EV.glob("rd1-*") if p.is_file() and p.name != "rd1-artifact-index.tsv"]
    index = []
    for path in sorted(set(paths), key=str):
        raw = path.read_bytes()
        index.append({
            "tep": str(path.relative_to(ROOT)), "bytes": len(raw), "sha256_bytes": digest(path),
            "sha256_LF": hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest(),
        })
    save_tsv(EV / "rd1-artifact-index.tsv", index)
    print(json.dumps({k: v for k, v in summary.items() if k != "report_sha256_bytes"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
