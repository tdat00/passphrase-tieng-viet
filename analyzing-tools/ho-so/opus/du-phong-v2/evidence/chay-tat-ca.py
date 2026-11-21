"""Chạy lại toàn bộ phân tích vòng 1 của Opus theo thứ tự. Cần evidence/_tam-hnd/Viet11K..74K.txt (tải theo
manifest.json, kiểm SHA-256) cho các bước có HND; thư mục đó là bản tạm, không đưa vào repo.

    python chay-tat-ca.py
"""
import subprocess
import sys
from chung import *

out_utf8()
DP = str(AT / "du-phong.txt")
steps = [
    ["thu-thap-du-phong.py"],
    ["kiem-hnd.py", DP, "du-phong-205-hnd.tsv"],
    ["do-bien-the.py", DP, "bien-the-du-phong-205.tsv"],
    ["phan-loai-du-phong.py"],
    ["tra-tu.py", "tu-doi-thuong-tu-nghi.txt", "tra-tu-doi-thuong-1.tsv"],
    ["tra-tu.py", "tu-doi-thuong-tu-nghi-2.txt", "tra-tu-doi-thuong-2.tsv"],
    ["-c", "from chung import *; rows = rd(HERE/'tra-tu-doi-thuong-1.tsv', True) + rd(HERE/'tra-tu-doi-thuong-2.tsv', True); "
           "write_lines(HERE/'chua-vao-ro.txt', list(dict.fromkeys(r['tu'] for r in rows if r['noi_co_mat'] == 'CHUA_TUNG_VAO_RO')))"],
    ["kiem-hnd.py", "chua-vao-ro.txt", "chua-vao-ro-hnd.tsv"],
    ["lap-de-cu.py"],
    ["do-bien-the.py", "de-cu-giu.txt", "bien-the-de-cu.tsv"],
    ["kiem-hnd.py", "de-cu-giu.txt", "de-cu-hnd.tsv"],
    ["xuat-de-cu.py"],
    ["kiem-hnd.py", "bien-the-tra.txt", "bien-the-hnd.tsv"],
    ["do-bien-the.py", "CHINH", "bien-the-chinh-tho.tsv"],
    ["kiem-d6-168.py"],
    ["kiem-d5-chinh-va-168.py"],
    ["chay-bo-kiem-lf.py"],
    ["kiem-dau-ra.py"],
]
for s in steps:
    print(">>", " ".join(s), flush=True)
    p = subprocess.run([sys.executable] + s, cwd=HERE)
    if p.returncode:
        sys.exit(f"Bước lỗi: {' '.join(s)}")
