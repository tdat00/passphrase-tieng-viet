"""Kiểm hồ sơ rà chéo; không đọc cross-review Opus hoặc sửa tệp sản phẩm."""
import csv
import hashlib
import io
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

from screen_core import EV, OUT, ROOT, save_json, save_tsv


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows(path):
    return list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8")), delimiter="\t"))


def main():
    protected = json.loads((EV / "protected-baseline.json").read_text(encoding="utf-8"))
    changed = [p for p, h in protected.items() if digest(ROOT / p) != h["sha256_bytes"]]
    assert not changed, changed
    inputs = json.loads((EV / "cr1-input-hashes.json").read_text(encoding="utf-8"))
    input_changes = [p for p, h in inputs.items() if digest(ROOT / p) != h]
    assert not input_changes, input_changes
    independent = rows(EV / "artifact-index.tsv")
    independent_changes = [
        r["tep"] for r in independent if digest(ROOT / r["tep"]) != r["sha256_bytes"]
    ]
    assert not independent_changes, independent_changes

    tables = {
        "cr1-diff-H7-theo-khoa.tsv": (7776, "khoa"),
        "cr1-diff-H5.tsv": (643, None),
        "cr1-diff-thay-va-vao.tsv": (321, "tu"),
        "cr1-audit-96-K2.tsv": (96, "khoa"),
        "cr1-Astra-tra-loi-96-K2.tsv": (96, "khoa"),
        "cr1-Astra-sua-H7.tsv": (14, "khoa"),
        "cr1-Astra-sua-H5.tsv": (17, None),
        "cr1-HND-da-co-so-do.tsv": (238, None),
        "cr1-frequency-rows.tsv": (76, None),
        "cr1-H5b-hop-dong.tsv": (9, None),
    }
    data = {}
    for name, (count, unique_column) in tables.items():
        data[name] = rows(EV / name)
        assert len(data[name]) == count, (name, len(data[name]), count)
        if unique_column:
            assert len({r[unique_column] for r in data[name]}) == count, name
    audit_keys = {r["khoa"] for r in data["cr1-audit-96-K2.tsv"]}
    replies = data["cr1-Astra-tra-loi-96-K2.tsv"]
    assert audit_keys == {r["khoa"] for r in replies}
    response_counts = Counter(r["A_phan_hoi"] for r in replies)
    rulings = json.loads((EV / "cr1-ruling-summary.json").read_text(encoding="utf-8"))
    assert dict(response_counts) == rulings["K2_response_counts"]
    assert rulings["new_release_signatures_written"] == 0
    assert all(r["chu_ky"].startswith("CHUA_KY_PHAT_HANH") for r in replies)
    h5_updates = data["cr1-Astra-sua-H5.tsv"]
    rong = next(r for r in h5_updates if r["tu"] == "rong ruổi")
    assert "37/1" in rong["ly_do"] and "21/1" in rong["ly_do"]
    h5b = data["cr1-H5b-hop-dong.tsv"]
    assert sum(r["thuoc_H5b_da_ky"] == "True" for r in h5b) == 8
    assert next(r for r in h5b if r["tu"] == "qua quýt")["thuoc_H5b_da_ky"] == "False"
    s4 = json.loads((EV / "cr1-S4-summary.json").read_text(encoding="utf-8"))
    assert s4["baseline_exact"] and len(s4["simulations"]) == 4
    assert all(r["F"] == 77 and r["R1"] == 0 for r in s4["simulations"])

    report = OUT / "round-1-cross-review.md"
    candidates = sorted([report, *EV.glob("cr1-*")], key=str)
    checked = []
    for path in candidates:
        if not path.is_file():
            continue
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        assert not raw.startswith(b"\xef\xbb\xbf"), str(path)
        assert raw.endswith(b"\r\n"), str(path)
        assert b"\n" not in raw.replace(b"\r\n", b""), str(path)
        assert b"\r" not in raw.replace(b"\r\n", b""), str(path)
        assert all(line == line.rstrip(" \t") for line in text.splitlines()), str(path)
        checked.append(str(path.relative_to(ROOT)))
    summary = {
        "checked_at": datetime.now().astimezone().isoformat(),
        "base": "1c3f50406f5115f5c33ca87c8534831b011e2b10",
        "protected_files_checked": len(protected),
        "protected_files_changed": changed,
        "cross_review_inputs_checked": len(inputs),
        "cross_review_inputs_changed": input_changes,
        "independent_artifacts_checked": len(independent),
        "independent_artifacts_changed": independent_changes,
        "table_rows": {name: len(value) for name, value in data.items()},
        "K2_response_counts": dict(response_counts),
        "new_release_signatures_written": 0,
        "rong_ruoi_partial_artifact_typo_fixed": True,
        "S4_baseline_exact": True,
        "S4_simulations_checked": 4,
        "format": "UTF-8 without BOM; CRLF; no trailing whitespace; final newline",
        "format_checked_files": checked,
        "report_sha256_bytes": digest(report),
        "limits": [
            "Không tái tải/đếm corpus trong phiên tiếp nối.",
            "Không coi phép tính là chữ ký ngữ nghĩa hoặc phê duyệt phát hành.",
        ],
    }
    save_json(EV / "cr1-finish-summary.json", summary)
    artifacts = sorted(
        [report, *[p for p in EV.glob("cr1-*") if p.is_file() and p.name != "cr1-artifact-index.tsv"]],
        key=str,
    )
    index = []
    for path in artifacts:
        raw = path.read_bytes()
        index.append({
            "tep": str(path.relative_to(ROOT)),
            "bytes": len(raw),
            "sha256_bytes": hashlib.sha256(raw).hexdigest(),
            "sha256_LF": hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest(),
        })
    save_tsv(EV / "cr1-artifact-index.tsv", index)
    print(json.dumps({
        "protected_unchanged": len(protected),
        "inputs_unchanged": len(inputs),
        "independent_artifacts_unchanged": len(independent),
        "cross_review_artifacts": len(index),
        "H5_numeric_rows": len(rows(EV / "cr1-H5-so-doc-lap.tsv")),
        "K2_keys": len(replies),
        "status": "PASS",
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
