"""Kiểm tương thích marker/tài liệu bằng RAM, không dựng hay lưu câu nghĩa mới."""
import json
import re
import subprocess
import sys

from screen_core import AT, EV, ROOT, save_json, write


PY_RAM = r'''
import json,runpy,sys
from pathlib import Path
from unittest.mock import patch
x=json.load(sys.stdin);root=Path(x["root"]);word=root/"analyzing-tools"/"wordlist.txt"
doc=root/"WordListAnalyze.md";old_bytes=Path.read_bytes;old_text=Path.read_text
def rb(p):
    b=old_bytes(p)
    return b.replace(b"\r\n",b"\n") if p.resolve()==word.resolve() else b
def rt(p,*args,**kwargs):
    t=old_text(p,*args,**kwargs)
    if p.resolve()==doc.resolve():
        nl="\r\n" if "\r\n" in t else "\n"
        t+=nl+"## 13. Rà và thay danh sách chính (bản phát hành 2)"+nl+nl+"Hồ sơ kiểm marker; không thay khối mục 10."+nl
    return t
sys.argv=[str(root/"analyzing-tools"/x["script"]),*x["args"]]
with patch.object(Path,"read_bytes",rb),patch.object(Path,"read_text",rt):
    runpy.run_path(sys.argv[0],run_name="__main__")
'''

JS_RAM = r'''
const fs=require("node:fs"),path=require("node:path"),{pathToFileURL}=require("node:url");
const input=JSON.parse(fs.readFileSync(0,"utf8")),old=fs.readFileSync;
const target=path.resolve(input.root,"analyzing-tools","wordlist.txt"),doc=path.resolve(input.root,"WordListAnalyze.md");
fs.readFileSync=function(p,...args){
  if(typeof p==="string"&&[target,doc].includes(path.resolve(p))){
    const raw=old.call(fs,p),opt=args[0],enc=typeof opt==="string"?opt:opt&&opt.encoding;
    let text=raw.toString("utf8");
    text=path.resolve(p)===target?text.replaceAll("\r\n","\n"):text+"\n## 13. Rà và thay danh sách chính (bản phát hành 2)\n";
    return enc?text:Buffer.from(text,"utf8");
  }
  return old.call(fs,p,...args);
};
import(pathToFileURL(path.resolve(input.root,"analyzing-tools","verify.mjs")).href);
'''


def main():
    cases = [
        ("native-python", [sys.executable, "-X", "utf8", "-B", str(AT / "check_wordlist.py")], None, 1, 1),
        ("native-js", ["node", str(AT / "verify.mjs")], None, 1, 3),
        ("native-build-check", [sys.executable, "-X", "utf8", "-B", str(AT / "build_wordlist.py"), "--check"], None, 0, None),
        ("canonical-python-added-section13", [sys.executable, "-X", "utf8", "-B", "-c", PY_RAM],
         {"root": str(ROOT), "script": "check_wordlist.py", "args": []}, 0, 0),
        ("canonical-js-added-section13", ["node", "-e", JS_RAM], {"root": str(ROOT)}, 0, 0),
        ("CRLF-build-added-section13", [sys.executable, "-X", "utf8", "-B", "-c", PY_RAM],
         {"root": str(ROOT), "script": "build_wordlist.py", "args": ["--check"]}, 0, None),
    ]
    results = []
    for name, command, payload, expected, expected_errors in cases:
        done = subprocess.run(
            command, input=json.dumps(payload, ensure_ascii=False) if payload else None,
            cwd=ROOT, capture_output=True, encoding="utf-8",
        )
        count = re.search(r"Tổng:\s*(\d+)\s*lỗi", done.stdout)
        assert done.returncode == expected, (name, done.returncode, done.stdout, done.stderr)
        if expected_errors is not None:
            assert count and int(count.group(1)) == expected_errors, (name, done.stdout)
        results.append({
            "case": name, "exit": done.returncode, "expected_exit": expected,
            "errors": int(count.group(1)) if count else None,
            "stdout": done.stdout, "stderr": done.stderr,
        })
    save_json(EV / "rd1-gates-summary.json", {
        "results": results, "new_glosses_written": 0, "fresh_D6_run": False,
        "limits": "Kiểm baseline và marker mục 13 ở RAM; không chứng nhận gói thay 87 hoặc nghĩa mới.",
    })
    write(EV / "rd1-gates.log", "\n".join(f"[{r['case']}] exit={r['exit']}\n{r['stdout']}{r['stderr']}" for r in results))
    print(json.dumps({r["case"]: r["exit"] for r in results}, ensure_ascii=False))


if __name__ == "__main__":
    main()
