"""Lượt duyệt 3, kiểm lại thay đổi 4: ghi_chu (lý do tầng) trong hai bảng hồ sơ, kế hoạch §4.2.1, E/public-ghi-chu.tsv.

    python kiem-thay-doi-4.py  ->  kiem-thay-doi-4.log

Văn bản chuẩn được đọc thẳng từ hai bảng ở round-1-review-drafts.md, Lượt duyệt 3 §D (không gõ lại).
Chỉ đọc. Mỗi dòng log: DAT/CHUA_DAT, mã, mô tả, giá trị đo.
"""
import csv
import hashlib
import io
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


def doc_tsv(text):
    return list(csv.DictReader(io.StringIO(text.replace("\r\n", "\n")), delimiter="\t"))


def bang_md(text, tieu_de):
    """Đọc bảng Markdown hai cột ngay sau dòng chứa tieu_de; trả {từ: văn bản}, tách ô gộp 'a, b, c'."""
    dong = text.split("\n")
    i = next(k for k, l in enumerate(dong) if tieu_de in l)
    while not dong[i].startswith("| "):
        i += 1
    i += 2  # bỏ dòng tiêu đề và dòng ---
    kq = {}
    while i < len(dong) and dong[i].startswith("| "):
        o = [c.strip() for c in dong[i].strip().strip("|").split("|")]
        for w in o[0].split(", "):
            kq[w] = o[1]
        i += 1
    return kq


review = (OUT / "round-1-review-drafts.md").read_text(encoding="utf-8").replace("\r\n", "\n")
l3 = review[review.index("## Lượt duyệt 3 (ký kế hoạch)"):]
CHUAN_R = bang_md(l3, "**Văn bản `ghi_chu` cho bảng dự phòng**")
CHUAN_H = bang_md(l3, "**Văn bản `ghi_chu` cho bảng HM**")
ghi("chuan:", len(CHUAN_R), "dòng dự phòng,", len(CHUAN_H), "dòng HM")

ghi("== Hai bảng hồ sơ")
cu = {}
for ten, chuan, n_mang in (("du-phong-v2-phan-loai.tsv", CHUAN_R, 30), ("du-phong-v2-honorable-mentions.tsv", CHUAN_H, 8)):
    old = doc_tsv(subprocess.run(["git", "-C", str(REPO), "show", f"1734b43:analyzing-tools/ho-so/unified/{ten}"],
                                 capture_output=True).stdout.decode("utf-8"))
    raw = (U / ten).read_bytes().decode("utf-8")
    new = doc_tsv(raw)
    cu[ten] = (old, new)
    kiem("4", f"{ten}: cùng số dòng/thứ tự từ, thêm đúng một cột ghi_chu",
         [r["tu"] for r in old] == [r["tu"] for r in new] and set(new[0]) - set(old[0]) == {"ghi_chu"} and set(old[0]) <= set(new[0]))
    doi = sorted({c for a, b in zip(old, new) for c in old[0] if a[c] != b[c]})
    kiem("4", f"{ten}: cột cũ duy nhất bị đổi là bang_chung", doi in ([], ["bang_chung"]), doi)
    mang = {r["tu"]: r["ghi_chu"] for r in new if r["ghi_chu"] != "-"}
    kiem("4", f"{ten}: {n_mang} dòng có ghi_chu, còn lại '-'", len(mang) == n_mang and all(r["ghi_chu"] for r in new),
         f"{len(mang)} có / {sum(r['ghi_chu'] == '-' for r in new)} '-'")
    sai = {w: (mang.get(w), v) for w, v in chuan.items() if mang.get(w) != v}
    thua = sorted(set(mang) - set(chuan))
    kiem("4", f"{ten}: từng ô ghi_chu trùng nguyên văn Lượt duyệt 3 §D", not sai and not thua, f"sai {len(sai)}, thừa {thua}")
    for w, (a, b) in list(sai.items())[:5]:
        ghi("   khác:", w, "| có:", a, "| chuẩn:", b)
    them = {a["tu"]: b["bang_chung"][len(a["bang_chung"]):] for a, b in zip(old, new) if a["bang_chung"] != b["bang_chung"]}
    kiem("4", f"{ten}: bang_chung chỉ được nối thêm (không xóa con trỏ cũ)",
         all(b["bang_chung"].startswith(a["bang_chung"]) for a, b in zip(old, new)))
    ghi("   phần nối thêm (mẫu):", sorted(set(them.values()))[:3])
    kiem("T7", f"{ten}: CRLF đồng nhất, UTF-8 không BOM, có dòng cuối, không khoảng trắng cuối ô dòng",
         raw.count("\r\n") == raw.count("\n") and not raw.startswith("\ufeff") and raw.endswith("\r\n")
         and all(l == l.rstrip(" ") for l in raw.split("\r\n")))

R = cu["du-phong-v2-phan-loai.tsv"][1]
H = cu["du-phong-v2-honorable-mentions.tsv"][1]
cd = [r for r in R if r["tang_chung"] in ("C", "D")]
kiem("4", "21 dòng C/D đều có ghi_chu bắt đầu bằng tầng của dòng", len(cd) == 21 and all(r["ghi_chu"].startswith(r["tang_chung"] + ":")
                                                                                       for r in cd))
tinh = [r for r in H if r["ket_luan_nhap"] == "CUNG_DE_CU_CHUA_PHAT_HANH"]
kiem("4", "8 ghi_chu HM đều thuộc 237 dòng được tính", len(tinh) == 237 and all(r["ket_luan_nhap"] == "CUNG_DE_CU_CHUA_PHAT_HANH"
                                                                                for r in H if r["ghi_chu"] != "-"))
from collections import Counter
kiem("4", "tầng và N không đổi", Counter(r["tang_chung"] for r in R) == Counter({"A": 148, "B": 36, "C": 15, "D": 6}))

ghi("== Phép chiếu công bố (T10)")
COT_R = "tu khoa lop ngan tang trang_thai_h ma_van_de giai_nghia luot_viet sha256_giai_nghia h8 F diem thay_duoc con_thieu ghi_chu bang_chung".split()
COT_H = "tu khoa nhom nhan_ho_so lop xac_minh_lop trang_thai_h ngan_du_kien h8 sub_sach web_sach leipzig tatoeba F diem nguon ly_do_chua_chon dieu_kien ghi_chu bang_chung".split()
ke_hoach = (U / "du-phong-v2-ke-hoach.md").read_text(encoding="utf-8").replace("\r\n", "\n")
kiem("T10", "schema công bố 17/20 cột trong kế hoạch còn nguyên và có ghi_chu", "\t".join(COT_R) in ke_hoach and "\t".join(COT_H) in ke_hoach)
kiem("T10", "mọi cột công bố (trừ tang) có trong bảng hồ sơ", all(c in R[0] for c in COT_R if c != "tang") and all(c in H[0] for c in COT_H))
chieu_r = [{c: (r["tang_chung"] if c == "tang" else r[c]) for c in COT_R} for r in R]
chieu_h = [{c: r[c] for c in COT_H} for r in tinh]
kiem("T10", "phép chiếu: 30/175 và 8/229", sum(r["ghi_chu"] != "-" for r in chieu_r) == 30 and sum(r["ghi_chu"] == "-" for r in chieu_r) == 175
     and sum(r["ghi_chu"] != "-" for r in chieu_h) == 8 and sum(r["ghi_chu"] == "-" for r in chieu_h) == 229)

ghi("== Kế hoạch §4.2.1 và evidence của Astra")
kh_r = bang_md(ke_hoach, "#### 4.2.1.")
sau = ke_hoach[ke_hoach.index("#### 4.2.1."):]
kh_h = bang_md(sau[sau.index("| Từ | ghi_chu |") + 10:], "| Từ | ghi_chu |")
kiem("4", "bảng dự phòng ở §4.2.1 trùng nguyên văn", kh_r == CHUAN_R, f"{len(kh_r)} dòng")
kiem("4", "bảng HM ở §4.2.1 trùng nguyên văn", kh_h == CHUAN_H, f"{len(kh_h)} dòng")
pg = doc_tsv((AT / "ho-so/astra/du-phong-v2/evidence/public-ghi-chu.tsv").read_text(encoding="utf-8"))
ghi("public-ghi-chu.tsv cột:", list(pg[0].keys()), "dòng:", len(pg))
cot_tu = "tu" if "tu" in pg[0] else list(pg[0])[0]
cot_gc = "ghi_chu" if "ghi_chu" in pg[0] else [c for c in pg[0] if "ghi" in c][0]
pgd = {r[cot_tu]: r[cot_gc] for r in pg}
kiem("4", "E/public-ghi-chu.tsv trùng nguyên văn (38 dòng)", pgd == {**CHUAN_R, **CHUAN_H} and len(pg) == 38)
kiem("4", "§5.2 BANG_CANH_BAO có cột Lý do = ghi_chu, 21 dòng",
     "| BANG_CANH_BAO | 21 dòng C/D theo O1; cột Từ / Tầng / Lý do / Việc còn thiếu. Lý do = `ghi_chu`" in ke_hoach)
kiem("4", "§10 có T10", "| T10 | Lý do không bị mất khi xuất công bố |" in ke_hoach)
kiem("4", "kế hoạch không còn định nghĩa ghi_chu cũ", "`ghi_chu` là lý do được chốt khi đóng từng câu hỏi" not in ke_hoach)

ghi("== Số liệu thứ tự S4 được dẫn trong kế hoạch")
dm = {r["tu"]: r["diem"] for r in R}
for w in ("lỗ lãi", "lời lỗ", "mỏng dính", "mỏng tanh"):
    ghi(f"   diem {w}: {dm.get(w)}")
kiem("4", "điểm S4 dẫn ở §4.2.1 khớp cột diem", dm.get("lỗ lãi") == "5.401989" and dm.get("lời lỗ") == "2.900190"
     and dm.get("mỏng dính") == "7.006689" and dm.get("mỏng tanh") == "4.969709",
     {w: dm.get(w) for w in ("lỗ lãi", "lời lỗ", "mỏng dính", "mỏng tanh")})

ghi("== Câu hỏi, vùng bảo vệ")
cau_hoi = (U / "du-phong-v2-cau-hoi.md").read_text(encoding="utf-8")
kiem("Q", "tệp câu hỏi vẫn ghi không còn câu hỏi mở", "Không còn câu hỏi mở" in cau_hoi and "## Q-dpv2" not in cau_hoi)
for f, h in (("index.html", "01b76617f8df57d80e59d0989001ced8f7714ae95e85828b351bce2a5517a423"),
             ("thong-tin.html", "8ec3bbf763f2465994bde4239079a3795eb2eb3bf21f61fe29aa683cb8bf3ea7"),
             ("analyzing-tools/wordlist.txt", "8945fd4a732b210b4e027f6660b4f42d53b2344088028f967e01a30af7bbc6b4")):
    kiem("B1", f"SHA byte {f}", hashlib.sha256((REPO / f).read_bytes()).hexdigest() == h)
sua = [l[3:] for l in subprocess.run(["git", "-C", str(REPO), "status", "--porcelain", "--untracked-files=no"],
                                     capture_output=True, text=True).stdout.splitlines()]
kiem("B1", "chỉ tệp hồ sơ bị sửa", all(p.startswith("analyzing-tools/ho-so/") for p in sua), len(sua))

ghi(f"Tổng: {loi} mục chưa đạt.")
(HERE / "kiem-thay-doi-4.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
print("\n".join(log))
