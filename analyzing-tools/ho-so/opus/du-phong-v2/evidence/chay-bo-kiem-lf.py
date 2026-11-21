"""Chạy hai bộ kiểm của repo trên bản xuất LF của HEAD (working tree Windows dùng CRLF vì core.autocrlf=true).

Xuất các tệp cần thiết bằng `git show HEAD:<đường dẫn>` vào evidence/_xuat-lf, chạy
`check_wordlist.py` và `verify.mjs`, ghi log, rồi xóa thư mục tạm.

    python chay-bo-kiem-lf.py [rev]
"""
import os
import shutil
import subprocess
import sys
from chung import *

out_utf8()
rev = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
tam = HERE / "_xuat-lf"
files = ["index.html", "thong-tin.html", "WordListAnalyze.md", "analyzing-tools/wordlist.txt", "analyzing-tools/labels.tsv",
         "analyzing-tools/blocked_keys.tsv", "analyzing-tools/spelling_families.tsv", "analyzing-tools/check_wordlist.py",
         "analyzing-tools/verify.mjs"]
try:
    for f in files:
        data = subprocess.run(["git", "-C", str(REPO), "show", f"{rev}:{f}"], capture_output=True, check=True).stdout
        p = tam / f
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    a = subprocess.run(["python", "check_wordlist.py"], cwd=tam / "analyzing-tools", capture_output=True, text=True, encoding="utf-8", env=env)
    b = subprocess.run(["node", "verify.mjs"], cwd=tam / "analyzing-tools", capture_output=True, text=True, encoding="utf-8", env=env)
    log = [f"rev: {rev}", "check_wordlist.py ma_thoat: %d" % a.returncode] + ["  " + l for l in a.stdout.strip().splitlines()[-6:]]
    log += ["verify.mjs ma_thoat: %d" % b.returncode] + ["  " + l for l in b.stdout.strip().splitlines()[-3:]]
    (HERE / "chay-bo-kiem-lf.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
    print("\n".join(log))
finally:
    shutil.rmtree(tam, ignore_errors=True)
