"""Lượt duyệt 3 (ký kế hoạch): kiểm trạng thái cuối của năm tệp U/du-phong-v2-* sau trả lời của chủ (1734b43).

    python kiem-ky-ke-hoach.py  ->  kiem-ky-ke-hoach.log

Chỉ đọc. Mỗi dòng log: DAT/CHUA_DAT, mã, mô tả, giá trị đo; cuối log là các bảng số mà người triển khai phải ra.
"""
import collections
import csv
import hashlib
import re
import subprocess
from chung import *

out_utf8()
log = []
loi = 0


def kiem(ma, mo_ta, dieu_kien, gia_tri=""):
    global loi
    if not dieu_kien:
        loi += 1
    log.append(f"{'DAT' if dieu_kien else 'CHUA_DAT'} | {ma} | {mo_ta}" + (f" | {gia_tri}" if gia_tri != "" else ""))


def ghi(*a):
    log.append(" ".join(str(x) for x in a).rstrip())


def tsv(path):
    return list(csv.DictReader(open(path, encoding="utf-8", newline=""), delimiter="\t"))


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True, encoding="utf-8")


R = tsv(U / "du-phong-v2-phan-loai.tsv")
H = tsv(U / "du-phong-v2-honorable-mentions.tsv")
Rw = {r["tu"]: r for r in R}
ke_hoach = (U / "du-phong-v2-ke-hoach.md").read_text(encoding="utf-8")
bao_cao = (U / "du-phong-v2-bao-cao-chung.md").read_text(encoding="utf-8")
cau_hoi = (U / "du-phong-v2-cau-hoi.md").read_text(encoding="utf-8")

ghi("== Dữ liệu cuối")
d = git("diff", "--stat", "1734b43", "--", "analyzing-tools/ho-so/unified/du-phong-v2-phan-loai.tsv",
        "analyzing-tools/ho-so/unified/du-phong-v2-honorable-mentions.tsv").stdout.strip()
kiem("TSV", "hai TSV không đổi so với 1734b43", d == "", d)
tang = collections.Counter(r["tang_chung"] for r in R)
kiem("TSV", "tầng A148/B36/C15/D6, không CHO_HOA", dict(tang) == {"A": 148, "B": 36, "C": 15, "D": 6}, dict(sorted(tang.items())))
kiem("TSV", "không còn tranh chấp hay câu hỏi trong dự phòng", all(r["tranh_chap"] == "KHONG" and r["cau_hoi"] == "-" for r in R))
n = [r for r in H if r["ket_luan_nhap"] == "CUNG_DE_CU_CHUA_PHAT_HANH"]
kiem("TSV", "HM 285 dòng hồ sơ, N = 237", len(H) == 285 and len(n) == 237)
nt = Rw["ngoại trừ"]
kiem("D-L2", "ngoại trừ theo Lượt duyệt 2 §D", nt["tang_opus"] == nt["tang_chung"] == "C" and nt["tranh_chap"] == "KHONG"
     and nt["cau_hoi"] == "-" and nt["ma_van_de"] == "H7;D8_CHUA_CO" and nt["trang_thai_h"] == "CHO_H7"
     and "đo tỷ lệ nghĩa điều trị" in nt["con_thieu"] and nt["y_kien_opus"].startswith("C/CHO_H7"))
kiem("E1-L2", "ba D có lại nguồn/câu kết", "93445969" in Rw["hì hụi"]["y_kien_opus"]
     and all("95%/20" in Rw[w]["y_kien_opus"] for w in ("nhão nhẹt", "nhão nhoẹt")))
kiem("E2-L2", "bỏ chữ 'Astra:' lặp", all("Astra: Astra:" not in r["y_kien_opus"] for r in R))

ghi("== Câu hỏi và Decisions")
kiem("Q", "tệp câu hỏi chỉ còn 'Không còn câu hỏi mở.'", cau_hoi.strip() == "Không còn câu hỏi mở.")
cu = git("show", "1734b43:analyzing-tools/ho-so/unified/du-phong-v2-cau-hoi.md").stdout
kiem("Q", "1734b43 có Answer 3 của chủ cho Q-dpv2-1", "**Answer (owner, 2026-11-20):** 3" in cu
     and "**Yêu cầu rà/thay chính riêng:**" in cu)
bat_dau = ke_hoach.index("\n## 9. Decisions")
sec9 = ke_hoach[bat_dau:ke_hoach.index("\n## 10.", bat_dau)]
hang = [l for l in sec9.splitlines() if re.match(r"^\| [DT]-dpv2-\d+ \|", l)]
ids = [l.split("|")[1].strip() for l in hang]
ghi("Decisions:", ", ".join(ids))
kiem("DEC", "mã duy nhất, đủ D-dpv2-1..5 và T-dpv2-1..9", len(ids) == len(set(ids))
     and set(ids) == {f"D-dpv2-{i}" for i in range(1, 6)} | {f"T-dpv2-{i}" for i in range(1, 10)})
kiem("DEC", "mỗi hàng đủ 5 ô, có người quyết, ngày, commit nguồn", all(len([c for c in l.split("|")[1:-1]]) == 5
     and l.split("|")[3].strip() and re.search(r"2026-11-20", l.split("|")[4]) and re.search(r"1734b43|cefb993", l.split("|")[5])
     for l in hang))
kiem("DEC", "D-dpv2-* do chủ quyết, T-dpv2-* do hai SA", all(("owner" in l.split("|")[3]) == l.split("|")[1].strip().startswith("D-")
                                                         for l in hang))
for c in ("1734b43", "cefb993"):
    kiem("DEC", f"commit {c} tồn tại", git("cat-file", "-e", f"{c}^{{commit}}").returncode == 0)
kiem("DEC", "không còn 'pending' hay 'CHUA_COMMIT' trong kế hoạch", "pending" not in ke_hoach and "CHUA_COMMIT" not in ke_hoach)
kiem("OPEN", "kế hoạch và báo cáo ghi không còn câu hỏi mở", "Hiện không còn câu hỏi mở." in ke_hoach
     and "**Không còn câu hỏi mở.**" in bao_cao)

ghi("== Điểm neo cho người triển khai")
wla = (REPO / "WordListAnalyze.md").read_text(encoding="utf-8")
readme = (AT / "README.md").read_text(encoding="utf-8")
kiem("NEO", "WordListAnalyze.md: đúng một dòng '> - **Dự phòng:**'", sum(l.startswith("> - **Dự phòng:**") for l in wla.splitlines()) == 1)
kiem("NEO", "WordListAnalyze.md: đúng một dòng mục lục 11", sum(l.startswith("11. [Danh sách dự phòng (chưa phân tích)]")
                                                         for l in wla.splitlines()) == 1)
kiem("NEO", "WordListAnalyze.md: §11 là mục cuối", wla.count("\n## ") and wla.rfind("\n## ") == wla.index("\n## 11. Danh sách dự phòng"))
kiem("NEO", "README: đúng một hàng du-phong.txt trong bảng tệp", sum(l.startswith("| [`du-phong.txt`](du-phong.txt) |")
                                                                    for l in readme.splitlines()) == 1)
kiem("NEO", "README: có tiêu đề '## Cập nhật danh sách'", readme.count("\n## Cập nhật danh sách\n") == 1)

ghi("== Số liệu người triển khai phải ra (từ hai TSV hồ sơ)")
bt = collections.Counter((r["tang_chung"], r["ngan"]) for r in R)
for t in "ABCD":
    a, b = bt[(t, "OK_KHONG_F")], bt[(t, "OK_F")]
    ghi(f"BANG_TANG {t}: OK không-F {a}, OK-F {b}, tổng {a + b}")
cb = [r["tu"] for r in R if r["tang_chung"] in ("C", "D")]
ngoai = [r["tu"] for r in R if r["tang_chung"] not in ("C", "D") and r["trang_thai_h"] != "HO_SO_LICH_SU_CHUA_PHE_DUYET_THAY"]
ghi(f"BANG_CANH_BAO: {len(cb)} mục C/D; mục A/B có trạng thái riêng: {ngoai or 'không có'}")
ghi("trang_thai_h dự phòng:", dict(collections.Counter(r["trang_thai_h"] for r in R)))
ghi("BANG_NHOM_HM:", dict(collections.Counter((r["nhom"], r["trang_thai_h"]) for r in n)))
dk = [len(r["dieu_kien"]) for r in n]
ghi(f"BANG_TU_HM: {len(n)} dòng; độ dài dieu_kien tối đa {max(dk)} ký tự, trung vị {sorted(dk)[len(dk) // 2]}")
bc = [len(r["bang_chung"]) for r in R]
ghi(f"bang_chung dự phòng: độ dài tối đa {max(bc)} ký tự; có dấu '\\\\': {sum('\\' in r['bang_chung'] for r in R)} dòng")

ghi("== Vùng bảo vệ")
for f, h in (("index.html", "01b76617f8df57d80e59d0989001ced8f7714ae95e85828b351bce2a5517a423"),
             ("thong-tin.html", "8ec3bbf763f2465994bde4239079a3795eb2eb3bf21f61fe29aa683cb8bf3ea7"),
             ("analyzing-tools/wordlist.txt", "8945fd4a732b210b4e027f6660b4f42d53b2344088028f967e01a30af7bbc6b4")):
    kiem("B1", f"SHA byte {f}", hashlib.sha256((REPO / f).read_bytes()).hexdigest() == h)
sua = [l[3:] for l in git("status", "--porcelain", "--untracked-files=no").stdout.splitlines()]
ngoai_ho_so = [p for p in sua if not p.startswith("analyzing-tools/ho-so/")]
kiem("B1", "chỉ tệp hồ sơ bị sửa so với 1734b43", not ngoai_ho_so, ngoai_ho_so or len(sua))

ghi(f"Tổng: {loi} mục chưa đạt.")
(HERE / "kiem-ky-ke-hoach.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
print("\n".join(log))
