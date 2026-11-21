"""Kiểm lại D2/D5 (`kiem-tra-giai-nghia.py --phat-hanh`) trên 7.776 cặp chính + 168 cặp dự phòng có nghĩa.

Tạo tệp lô tạm trong evidence/_tam (LF), chạy bộ kiểm của repo, ghi tóm tắt vào log, rồi xóa tệp tạm
(không lưu lại câu giải nghĩa trong hồ sơ của Opus).

    python kiem-d5-chinh-va-168.py
"""
import shutil
import subprocess
from chung import *

out_utf8()
tam = HERE / "_tam"
tam.mkdir(exist_ok=True)
try:
    main = [l.split("|") for l in lines(AT / "wordlist.txt")]
    co_main = {r["tu"]: r["co_phat_hanh"] for r in rd(AT / "nguon-goc-giai-nghia.tsv") if r["trang_thai"] == "PHAT_HANH"}
    res168 = rd(U / "p7-v4-du-phong-168-co-nghia-cho-duyet.tsv")
    lots = [("lo-01", [(w, g, co_main.get(w, "")) for w, g in main]),
            ("lo-02", [(r["tu"], r["giai_nghia"], r["co"]) for r in res168])]
    args = ["python", str(AT / "kiem-tra-giai-nghia.py"), "--phat-hanh"]
    for name, items in lots:
        (tam / f"{name}.txt").write_bytes(("\n".join(w for w, _, _ in items) + "\n").encode("utf-8"))
        body = "tu\tgiai_nghia\tco\n" + "".join(f"{w}\t{g}\t{c}\n" for w, g, c in items)
        (tam / f"{name}.tsv").write_bytes(body.encode("utf-8"))
        args += [str(tam / f"{name}.txt"), str(tam / f"{name}.tsv")]
    p = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
    out = p.stdout.strip().splitlines()
    summary = [l for l in out if l.startswith(("Tổng", "TỔNG", "Tong")) or "lỗi" in l.lower()][-3:]
    log = [f"lenh: kiem-tra-giai-nghia.py --phat-hanh lo-01 (7776 chinh) lo-02 (168 du phong)",
           f"so_cap: {sum(len(i) for _, i in lots)}", f"ma_thoat: {p.returncode}", f"so_dong_xuat: {len(out)}"]
    log += ["dong_cuoi: " + l for l in out[-3:]]
    (HERE / "kiem-d5-chinh-va-168.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
    print("\n".join(log))
finally:
    shutil.rmtree(tam, ignore_errors=True)
