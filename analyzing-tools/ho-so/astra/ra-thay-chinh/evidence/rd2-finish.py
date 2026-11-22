"""Kiểm chỉ append lượt duyệt 2 và bảo toàn các đầu vào nháp/sản phẩm."""
import hashlib
import json
import re
from datetime import datetime

from screen_core import EV, OUT, ROOT, U, save_json, save_tsv, tsv


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    protected = json.loads((EV / "protected-baseline.json").read_text(encoding="utf-8"))
    assert all(digest(ROOT / p) == h["sha256_bytes"] for p, h in protected.items())
    inputs = json.loads((EV / "rd2-input-hashes.json").read_text(encoding="utf-8"))
    assert all(digest(ROOT / p) == h for p, h in inputs.items())
    review = OUT / "round-1-review-drafts.md"
    raw = review.read_bytes()
    prefix = json.loads((EV / "rd2-review-prefix.json").read_text(encoding="utf-8"))
    assert hashlib.sha256(raw[:prefix["bytes"]]).hexdigest() == prefix["sha256"]
    added = raw[prefix["bytes"]:].decode("utf-8")
    assert added.lstrip().startswith("## Lượt duyệt 2")
    assert added.count("## Lượt duyệt 2") == 1 and "changes requested" in added
    old_index = tsv(EV / "rd1-artifact-index.tsv")
    old_unchanged = [r for r in old_index if (ROOT / r["tep"]).resolve() != review.resolve()]
    assert all(digest(ROOT / r["tep"]) == r["sha256_bytes"] for r in old_unchanged)
    audit = json.loads((EV / "rd2-audit-summary.json").read_text(encoding="utf-8"))
    assert len(tsv(EV / "rd2-H5-xac-nhan.tsv")) == 3
    assert len(tsv(EV / "rd2-H7-bao-luu.tsv")) == 17
    assert len(tsv(EV / "rd2-H5-bao-luu.tsv")) == 7
    assert len(tsv(EV / "rd2-K2-da-ky.tsv")) == 2
    assert len(tsv(EV / "rd2-de-xuat-dong-co.tsv")) == 3
    assert audit["net_new_K2_candidates"] == 194
    hnd = json.loads((EV / "rd2-HND-summary.json").read_text(encoding="utf-8"))
    assert hnd["counts"]["expanded_aliases_any"] == {"c": 34, "d": 3}
    assert not hnd["raw_source_saved"]
    answers = [s for s in (U / "ra-thay-chinh-cau-hoi.md").read_text(encoding="utf-8").splitlines() if s.startswith("**Answer")]
    assert len(answers) == 5 and all(re.fullmatch(r"\*\*Answer \([^)]*\):\*\*", s) for s in answers)
    paths = [review, *[p for p in EV.glob("rd2-*") if p.is_file()]]
    for path in paths:
        body = path.read_bytes()
        text = body.decode("utf-8")
        assert not body.startswith(b"\xef\xbb\xbf"), str(path)
        assert body.endswith(b"\r\n"), str(path)
        assert b"\n" not in body.replace(b"\r\n", b""), str(path)
        assert b"\r" not in body.replace(b"\r\n", b""), str(path)
        assert all(line == line.rstrip(" \t") for line in text.splitlines()), str(path)
    summary = {
        "checked_at": datetime.now().astimezone().isoformat(),
        "review_only_appended": True,
        "protected_files_unchanged": len(protected),
        "draft_and_Opus_inputs_unchanged": len(inputs),
        "rd1_artifacts_unchanged_except_appended_review": len(old_unchanged),
        "confirmed_H5f_exclusions": 3, "H7_disputed": 17, "H5_disputed": 7,
        "preexisting_K2_to_reuse": 2, "new_K2_signature_queue": 194,
        "flag_closure_proposals": 3,
        "source_text_saved": False, "new_glosses_written": 0, "new_release_signatures_written": 0,
        "format": "UTF-8 without BOM; CRLF; no trailing whitespace; final newline",
        "report_sha256_bytes": digest(review),
        "verdict": "changes requested",
        "status": "PASS_REVIEW_ARTIFACTS_NOT_RELEASE",
    }
    save_json(EV / "rd2-finish-summary.json", summary)
    paths = [review, *[p for p in EV.glob("rd2-*") if p.is_file() and p.name != "rd2-artifact-index.tsv"]]
    index = []
    for path in sorted(set(paths), key=str):
        body = path.read_bytes()
        index.append({"tep": str(path.relative_to(ROOT)), "bytes": len(body), "sha256_bytes": digest(path),
                      "sha256_LF": hashlib.sha256(body.replace(b"\r\n", b"\n")).hexdigest()})
    save_tsv(EV / "rd2-artifact-index.tsv", index)
    print(json.dumps({k: v for k, v in summary.items() if k != "report_sha256_bytes"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
