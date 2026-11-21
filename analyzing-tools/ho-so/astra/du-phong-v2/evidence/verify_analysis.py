"""Kiểm chỉ đọc và lưu log; đối chứng lỗi CRLF bằng đúng blob Git LF, không sửa nguồn."""
import contextlib
import csv
import importlib.util
import io
import json
import os
import subprocess
import sys
from collections import Counter

from inventory import EV, OUT, ROOT, TOOLS, UNIFIED, load, read, save_json, sha


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, TOOLS / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def command(label, args, expected):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True,
                            encoding="utf-8", errors="strict", env=env)
    return {
        "label": label, "command": subprocess.list2cmdline([str(x) for x in args]),
        "exit_code": result.returncode, "expected_baseline_exit": expected,
        "as_expected": result.returncode == expected,
        "stdout": result.stdout, "stderr": result.stderr,
    }


def main():
    before = json.loads((EV / "inventory.json").read_text(encoding="utf-8"))
    py = [sys.executable, "-X", "utf8", "-B"]
    runs = [
        command("NATIVE_PYTHON_BASELINE", py + [str(TOOLS / "check_wordlist.py")], 1),
        command("NATIVE_NODE_BASELINE", ["node", str(TOOLS / "verify.mjs")], 1),
        command("BUILD_CHECK_READONLY", py + [str(TOOLS / "build_wordlist.py"), "--check"], 0),
        command("ANALYSIS_NODE_INDEPENDENT", ["node", str(EV / "verify-analysis.mjs")], 0),
    ]
    base = before["base_commit"]
    code = f"""
import pathlib, subprocess, runpy
root = pathlib.Path({str(ROOT)!r})
target = root / 'analyzing-tools' / 'wordlist.txt'
canonical = subprocess.check_output(['git', 'show', {base + ':analyzing-tools/wordlist.txt'!r}], cwd=root)
native = pathlib.Path.read_bytes
pathlib.Path.read_bytes = lambda p: canonical if p.resolve() == target.resolve() else native(p)
runpy.run_path(str(root / 'analyzing-tools' / 'check_wordlist.py'), run_name='__main__')
"""
    runs.append(command("CANONICAL_GIT_LF_PYTHON", py + ["-c", code], 0))
    code = f"""
import fs from 'node:fs';
import path from 'node:path';
import {{execFileSync}} from 'node:child_process';
import {{pathToFileURL}} from 'node:url';
const root = {json.dumps(str(ROOT))};
const target = path.join(root, 'analyzing-tools', 'wordlist.txt');
const canonical = execFileSync('git', ['show', {json.dumps(base + ':analyzing-tools/wordlist.txt')}], {{cwd:root}});
const native = fs.readFileSync;
fs.readFileSync = function(p, options) {{
  if (typeof p === 'string' && path.resolve(p).toLowerCase() === target.toLowerCase()) {{
    const encoding = typeof options === 'string' ? options : options?.encoding;
    return encoding ? canonical.toString(encoding) : Buffer.from(canonical);
  }}
  return native.apply(this, arguments);
}};
await import(pathToFileURL(path.join(root, 'analyzing-tools', 'verify.mjs')).href);
"""
    runs.append(command("CANONICAL_GIT_LF_NODE", ["node", "--input-type=module", "-e", code], 0))

    canonical = subprocess.check_output(["git", "show", base + ":analyzing-tools/wordlist.txt"], cwd=ROOT)
    current = (TOOLS / "wordlist.txt").read_bytes()
    assert canonical == current.replace(b"\r\n", b"\n")
    data = load()
    mod = module("astra_gloss_checker_readonly", "kiem-tra-giai-nghia.py")
    published = [line.split("|") for line in read(TOOLS / "wordlist.txt").splitlines()]
    with (UNIFIED / "p7-v4-du-phong-168-co-nghia-cho-duyet.tsv").open(encoding="utf-8", newline="") as stream:
        reserve = list(csv.DictReader(stream, delimiter="\t"))
    virtual = {}
    for label, rows in (
        ("main", [(w, g, "HAI_NGHIA" if ";" in g else "") for w, g in published]),
        ("reserve", [(r["tu"], r["giai_nghia"], r["co"]) for r in reserve]),
    ):
        virtual[f"{label}.txt"] = "".join(w + "\n" for w, _, _ in rows)
        virtual[f"{label}.tsv"] = "tu\tgiai_nghia\tco\n" + "".join(
            "\t".join((w, g, flags)) + "\n" for w, g, flags in rows)
    mod.read_raw = lambda name: (virtual[name].encode("utf-8"), virtual[name])
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        release_exit = mod.main(["kiem-tra-giai-nghia.py", "--phat-hanh",
                                 "main.txt", "main.tsv", "reserve.txt", "reserve.tsv"])
    runs.append({
        "label": "D2_D5_EXISTING_7944_IN_MEMORY",
        "command": "kiem-tra-giai-nghia.main --phat-hanh; read_raw cung cấp lô LF trong bộ nhớ từ 7.776+168 câu có sẵn",
        "exit_code": release_exit, "expected_baseline_exit": 0, "as_expected": release_exit == 0,
        "stdout": stream.getvalue(), "stderr": "",
    })
    d6 = module("astra_d6_hash_readonly", "d6-kiem.py")
    historical = Counter()
    for r in reserve:
        digest = d6.digest(d6.json_bytes(d6.tokens(r["giai_nghia"])))
        matches = [x for x in data["d6"][r["tu"]] if x["sha256_giai_nghia"] == digest]
        assert len(matches) == 1 and matches[0]["ket_qua"] == "PASS"
        historical[matches[0]["_version"]] += 1
    assert sum(historical.values()) == 168

    protected = {name: sha((ROOT / name).read_bytes()) for name in
                 ("index.html", "thong-tin.html", r"analyzing-tools\wordlist.txt")}
    document = (ROOT / "WordListAnalyze.md").read_bytes()
    protected["WordListAnalyze.md section10 bytes"] = sha(
        document[document.index("## 10. Danh sách 7.776 từ phát hành".encode()):
                 document.index("## 11. Danh sách dự phòng".encode())])
    assert protected == before["protected_bytes"]
    status = subprocess.check_output(["git", "--no-pager", "diff", "--name-only"], cwd=ROOT, text=True)
    artifact_checks = []
    for path in sorted(OUT.rglob("*")):
        if not path.is_file():
            continue
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        assert not raw.startswith(b"\xef\xbb\xbf") and raw.endswith(b"\r\n"), path
        assert raw.count(b"\r\n") == raw.count(b"\n"), path
        assert all(line == line.rstrip(" \t") for line in text.splitlines()), path
        artifact_checks.append(str(path.relative_to(OUT)))
    reference_lines = {}
    checked_refs = 0
    for filename in ("du-phong-phan-loai.tsv", "honorable-mentions.tsv"):
        with (OUT / filename).open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream, delimiter="\t"):
                for field, cell in row.items():
                    if not field.endswith("_ref") or cell == "-":
                        continue
                    for reference in cell.split(";"):
                        source, line = reference.rsplit(":", 1)
                        if source not in reference_lines:
                            reference_lines[source] = len((ROOT / source).read_text(encoding="utf-8").splitlines())
                        assert 1 <= int(line) <= reference_lines[source], reference
                        checked_refs += 1
    result = {
        "runs": runs, "all_outcomes_as_expected": all(r["as_expected"] for r in runs),
        "native_release_checkers_pass": False,
        "native_failure_reason": "verified:checkout CRLF trước thay đổi; Python 1 lỗi C1, Node C1 và 2 lỗi C8; không sửa vùng bảo vệ",
        "canonical_is_exact_git_blob_and_equal_worktree_after_EOL_only": True,
        "canonical_wordlist_sha256": sha(canonical),
        "D6_historical_hash_matches": dict(historical),
        "D6_fresh_run": "CHUA_KIEM:không có vi.jsonl.gz; không gọi đối chiếu hash lịch sử là chạy D6 mới",
        "protected_bytes_unchanged": True, "protected_bytes": protected,
        "existing_files_diff": status.splitlines(),
        "own_artifacts_utf8_no_BOM_CRLF_no_trailing_whitespace": artifact_checks,
        "table_reference_pointers_checked": checked_refs,
        "table_reference_source_files": len(reference_lines),
    }
    save_json(EV / "verification.json", result)
    log = []
    for run in runs:
        log.extend(["=== " + run["label"], run["command"],
                    "exit=" + str(run["exit_code"]), run["stdout"].rstrip(),
                    run["stderr"].rstrip(), ""])
    log.extend([
        "D6 lịch sử: " + json.dumps(dict(historical), ensure_ascii=False),
        "D6 mới: CHUA_KIEM; thiếu tham chiếu, không tải corpus.",
        "Bốn vùng bảo vệ: byte-identical.",
    ])
    (EV / "verification.log").write_text("\n".join(log) + "\n", encoding="utf-8", newline="\r\n")
    assert result["all_outcomes_as_expected"], "Một kết quả kiểm không đúng kỳ vọng đã ghi"
    print(json.dumps({k: v for k, v in result.items() if k != "runs"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
