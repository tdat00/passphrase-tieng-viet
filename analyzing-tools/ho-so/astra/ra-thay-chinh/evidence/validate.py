"""Đối chứng nền và kiểm hồ sơ; không ghi bản sao giải nghĩa/nguồn thô."""
import base64
import csv
import json
import re
import subprocess
import sys
from collections import Counter

from dictionary_probe import vietnamese
from screen_core import AT, BASE, EV, OUT, ROOT, inventory, key, load, o1, save_json, sha, tsv, write


PY_CANON = r'''
import base64,json,runpy,sys
from pathlib import Path
from unittest.mock import patch
x=json.load(sys.stdin);root=Path(x["root"]);target=root/"analyzing-tools"/"wordlist.txt"
blob=base64.b64decode(x["blob"]);old=Path.read_bytes
def read(p):
    return blob if p.resolve()==target.resolve() else old(p)
sys.argv=[str(root/"analyzing-tools"/"check_wordlist.py")]
with patch.object(Path,"read_bytes",read):
    runpy.run_path(sys.argv[0],run_name="__main__")
'''
JS_CANON = r'''
const fs=require("node:fs"),path=require("node:path"),{pathToFileURL}=require("node:url");
const input=JSON.parse(fs.readFileSync(0,"utf8"));
const file=path.resolve(input.root,"analyzing-tools","wordlist.txt");
const blob=Buffer.from(input.blob,"base64"),old=fs.readFileSync;
fs.readFileSync=function(p,...args){
  if(typeof p==="string"&&path.resolve(p)===file){
    const opt=args[0],enc=typeof opt==="string"?opt:opt&&opt.encoding;
    return enc?blob.toString(enc):blob;
  }
  return old.call(fs,p,...args);
};
import(pathToFileURL(path.resolve(input.root,"analyzing-tools","verify.mjs")).href);
'''


def main():
    d = load()
    inventory(d)
    h5, h7, extra = (tsv(OUT / p) for p in ("h5-sang-loc-632.tsv", "h7-sang-loc-1177.tsv", "h7-sang-loc-bo-sung.tsv"))
    h5_extra = tsv(OUT / "h5-sang-loc-bo-sung.tsv")
    assert [len(h5), len(h7), len(extra)] == [632, 1177, 1942]
    assert len(h5_extra) == 2
    assert len({r["id"] for r in h5+h5_extra+h7+extra}) == 632+2+1177+1942
    for r in h5+h5_extra+h7+extra:
        assert r["ly_do"] and r["bang_chung"] and r["xac_minh"].startswith("verified:")
    for r in h7+extra:
        assert key(r["doc_khac"]) == key(r["tu_chinh"])
    hard_h5 = [r for r in h5 if r["hanh_dong"] == "DE_NGHI_THAY"]
    assert len(hard_h5) == 8
    for r in hard_h5:
        c = d["counts"][r["tu"]]
        assert min(int(c["sub_be_mat"]), int(c["web_be_mat"])) < 19
    primary = tsv(OUT / "de-xuat-thay-the-S4.tsv")
    assert len({r["tu_ra"] for r in primary}) == len(primary)
    assert len({key(r["tu_vao_de_xuat"]) for r in primary}) == len(primary)
    projected = (set(d["main"]) - {r["tu_ra"] for r in primary}) | {r["tu_vao_de_xuat"] for r in primary}
    assert len(projected) == len({key(w) for w in projected}) == 7776
    assert all(4 <= len(key(w)) <= 12 and 1 <= len(w.split()) <= 3 for w in projected)
    assert {r["khoa"] for r in d["blocked_keys"]}.isdisjoint(key(w) for w in projected)
    assert "baotu" not in {key(w) for w in projected}
    report = OUT/"round-1-analysis.md"
    if report.exists():
        section = report.read_text(encoding="utf-8").split("### 5.3.", 1)[1]
        listing = section.split("```text", 1)[1].split("```", 1)[0].strip()
        names = [x.strip() for x in listing.replace("\n", ";").split(";") if x.strip()]
        assert names == sorted({r["tu_ra"] for r in primary}, key=o1)
    assert vietnamese("{{-eng-}}\n# unrelated\n", "vi") == ""
    assert "# unrelated" not in vietnamese("{{-vie-}}\n{{-adj-}}\n# selected\n{{-tha-}}\n# unrelated\n", "vi")
    assert "# selected" in vietnamese("=={{langname|vi}}==\n# selected\n==English==\n# unrelated\n", "vi")
    blob = subprocess.check_output(["git", "show", f"{BASE}:analyzing-tools/wordlist.txt"], cwd=ROOT)
    payload = json.dumps({"root": str(ROOT), "blob": base64.b64encode(blob).decode()})
    commands = [
        ("native-python", [sys.executable, "-X", "utf8", "-B", str(AT/"check_wordlist.py")], None, 1, 1),
        ("native-js", ["node", str(AT/"verify.mjs")], None, 1, 3),
        ("native-build-check", [sys.executable, "-X", "utf8", "-B", str(AT/"build_wordlist.py"), "--check"], None, 0, None),
        ("canonical-python", [sys.executable, "-X", "utf8", "-B", "-c", PY_CANON], payload, 0, 0),
        ("canonical-js", ["node", "-e", JS_CANON], payload, 0, 0),
        ("D6-self-test", [sys.executable, "-X", "utf8", "-B", str(AT/"d6-kiem.py"), "--self-test"], None, 0, None),
    ]
    results = []
    for name, cmd, stdin, expected_rc, errors in commands:
        done = subprocess.run(cmd, input=stdin, cwd=ROOT, capture_output=True, encoding="utf-8")
        count = re.search(r"Tổng:\s*(\d+)\s*lỗi", done.stdout)
        assert done.returncode == expected_rc, (name, done.returncode, done.stdout, done.stderr)
        if errors is not None:
            assert count and int(count.group(1)) == errors
        results.append({"name": name, "exit": done.returncode, "stdout": done.stdout, "stderr": done.stderr})
    config = json.loads((AT/"d6-tham-chieu.json").read_text(encoding="utf-8"))
    references = {}
    for name, spec in config["sources"].items():
        p = AT/spec["path"]
        b = p.read_bytes() if p.exists() else None
        references[name] = {
            "available": b is not None,
            "raw_match": b is not None and sha(b) == spec["sha256"],
            "LF_match": b is not None and sha(b.replace(b"\r\n", b"\n")) == spec["sha256"],
            "expected_sha256": spec["sha256"],
            "actual_sha256": sha(b) if b is not None else None,
        }
    inventory(d)
    bad_format = []
    for p in OUT.rglob("*"):
        if p.is_file() and p.suffix in {".md", ".tsv", ".json", ".py", ".log"}:
            b = p.read_bytes()
            if b.startswith(b"\xef\xbb\xbf") or not b.endswith(b"\r\n") or b"\n" in b.replace(b"\r\n", b"") or any(
                line != line.rstrip(" \t") for line in b.decode("utf-8").splitlines()
            ):
                bad_format.append(str(p.relative_to(ROOT)))
    assert not bad_format, bad_format
    result = {
        "base": BASE, "rows": [632,1177,1942], "h5_mathematical_exclusions": len(hard_h5),
        "new_selected_word_projection": len(primary), "projected_size": 7776,
        "projected_keys_unique": True, "H1_H2_numeric": True,
        "new_glosses_written": 0, "fresh_D6_run": False,
        "D6_preflight": references,
        "baseline_commands": results, "native_checkers_pass": False,
        "canonical_is_exact_git_blob": True, "new_release_pass_claimed": False,
        "production_protected_bytes_unchanged": True, "format_errors": [],
    }
    save_json(EV/"validation.json", result)
    write(EV/"validation.log", "\n".join(f"[{r['name']}] exit={r['exit']}\n{r['stdout']}{r['stderr']}" for r in results))
    print(json.dumps({k:v for k,v in result.items() if k != "baseline_commands"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
