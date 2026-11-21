"""Review bản nháp chung (bước 3): kiểm dữ kiện của năm tệp U/du-phong-v2-* với dữ liệu repo.

    python kiem-ban-nhap-chung.py  ->  kiem-ban-nhap-chung.log

Chỉ đọc; không ghi gì ngoài log trong evidence/.
"""
import collections
import csv
import unicodedata
from chung import *

out_utf8()
log = []


def p(*a):
    log.append(" ".join(str(x) for x in a).rstrip())


def tsv(path):
    return list(csv.DictReader(open(path, encoding="utf-8", newline=""), delimiter="\t"))


def so_chu(w):
    return sum(1 for c in unicodedata.normalize("NFC", w) if c.isalpha())


R = tsv(U / "du-phong-v2-phan-loai.tsv")
H = tsv(U / "du-phong-v2-honorable-mentions.tsv")
main = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
du = lines(AT / "du-phong.txt")
kmain = {key(w) for w in main}
kdu = {key(w) for w in du}

p("== Dự phòng")
p("so_dong", len(R), "so_cot", len(R[0]), "dung_thu_tu_du_phong_txt", [r["tu"] for r in R] == du)
p("tang_chung", dict(collections.Counter(r["tang_chung"] for r in R)))
p("giai_nghia", dict(collections.Counter(r["giai_nghia"] for r in R)))
p("h8", dict(collections.Counter(r["h8"] for r in R)))
cho = [r["tu"] for r in R if r["tang_chung"] == "CHO_HOA"]
p("CHO_HOA", len(cho), ", ".join(cho))
# Tầng sau khi đóng Q-dpv2-2 (D cho 3) và Q-dpv2-3 (A cho 8)
sau = collections.Counter()
for r in R:
    t = r["tang_chung"]
    if t == "CHO_HOA":
        t = "D" if r["cau_hoi"] == "Q-dpv2-2" else "A" if r["cau_hoi"] == "Q-dpv2-3" else "?"
    sau[t] += 1
p("tang_sau_khi_dong_Q2_Q3", dict(sorted(sau.items())))
sau_ngan = collections.Counter()
for r in R:
    t = r["tang_chung"]
    if t == "CHO_HOA":
        t = "D" if r["cau_hoi"] == "Q-dpv2-2" else "A"
    sau_ngan[(t, r["ngan"])] += 1
p("tang_x_ngan_sau", dict(sorted(sau_ngan.items())))
p("A_F_co_nghia", sum(1 for r in R if r["ngan"] == "OK_F" and r["giai_nghia"] == "CO_PASS_LICH_SU"))

p("== HM")
p("so_dong", len(H), "so_cot", len(H[0]))
kh = [r["khoa"] for r in H]
p("khoa_tinh_lai_dung", all(key(r["tu"]) == r["khoa"] for r in H))
p("khoa_trung_trong_HM", len(kh) - len(set(kh)))
p("giao_khoa_chinh", sorted(set(kh) & kmain), "giao_khoa_du_phong", sorted(set(kh) & kdu))
p("do_dai_ngoai_4_12", [r["tu"] for r in H if not 4 <= so_chu(r["tu"]) <= 12])
p("khong_NFC", [r["tu"] for r in H if unicodedata.normalize("NFC", r["tu"]) != r["tu"]])
p("nhom", dict(collections.Counter(r["nhom"] for r in H)))
p("ket_luan_nhap", dict(collections.Counter(r["ket_luan_nhap"] for r in H)))
p("h8", dict(collections.Counter(r["h8"] for r in H)))
for r in H:
    if r["ket_luan_nhap"] == "CHO_HOA" and r["nhom"] != "L3B_CHUA_CHAM":
        p("  CHO_HOA:", r["tu"], r["khoa"], r["nhom"], r["nhan_ho_so"], r["lop"], r["cau_hoi"], r["tranh_chap"],
          r["de_cu_opus"], r["de_cu_astra"], r["trang_thai_h"])
l3b = [r for r in H if r["nhom"] == "L3B_CHUA_CHAM"]
p("L3B", len(l3b), "tranh_chap_dac_biet", [(r["tu"], r["tranh_chap"]) for r in l3b if r["tranh_chap"] != "CO_DUOC_TINH_HM_L3B"])
dong = [r for r in H if r["ket_luan_nhap"] != "CHO_HOA"]
p("cung_de_cu", len(dong))


def n_sau(q6_giu):
    n = len(dong)
    n += 0  # Q-dpv2-5: bao tử K1 -> 0; tần số K2 ký "không tự động chặn" -> 1
    n += 1  # tần số
    n += q6_giu
    return n


p("N_neu_Q4_pa2_Q5_baotu_K1_tanso_K2", {"Q6_giu_6": n_sau(6), "Q6_bo_6": n_sau(0), "Q6_astra_giu_1": n_sau(1),
                                        "Q6_opus_cu_giu_5": n_sau(5)})
p("nhom_N_Q6_giu_6", dict(collections.Counter(r["nhom"] for r in H if r["ket_luan_nhap"] != "CHO_HOA"
                                              or r["cau_hoi"] == "Q-dpv2-6" or r["tu"] == "tần số")))

p("== Cột không chứa câu giải nghĩa")
cot_r = [c for c in R[0] if c.startswith("giai_nghia")]
cot_h = [c for c in H[0] if "nghia" in c]
p("cot_nghia_du_phong", cot_r, "gia_tri", sorted({r["giai_nghia"] for r in R}), "cot_nghia_HM", cot_h)
gloss = {}
for path in (AT / "wordlist.txt",):
    for l in lines(path):
        w, g = l.split("|", 1)
        gloss[w] = g
p("cau_nghia_chinh_xuat_hien_trong_hai_TSV", sum(1 for g in gloss.values()
                                                  if g in (U / "du-phong-v2-phan-loai.tsv").read_text(encoding="utf-8")
                                                  or g in (U / "du-phong-v2-honorable-mentions.tsv").read_text(encoding="utf-8")))

p("== Dòng được trích trong câu hỏi")
oc = (U / "opus-counts.tsv").read_text(encoding="utf-8").splitlines()
for n in (463, 1961, 4870, 8221, 8222, 10478, 12029, 12702, 13474, 15957, 15958, 17448, 17654):
    p(f"opus-counts.tsv:{n}", "\t".join(oc[n - 1].split("\t")[:6]))
dc = (OUT / "de-cu-them-opus.tsv").read_text(encoding="utf-8").splitlines()
for n in (81, 171):
    p(f"O/de-cu-them-opus.tsv:{n}", dc[n - 1].split("\t")[3])
cr = (OUT / "round-1-cross-review.md").read_text(encoding="utf-8").splitlines()
for n in (58, 78, 80, 97, 102, 106, 110, 113, 114, 141, 173):
    p(f"O/round-1-cross-review.md:{n}", cr[n - 1][:90])
wla = (REPO / "WordListAnalyze.md").read_text(encoding="utf-8").splitlines()
for n in (471, 744, 745, 151, 153):
    p(f"WordListAnalyze.md:{n}", wla[n - 1][:110])
tc = (AT / "tieu-chi-thong-nhat.md").read_text(encoding="utf-8").splitlines()
for n in (79, 97, 103, 135, 137, 154, 156, 169, 171, 178, 180, 193):
    p(f"tieu-chi-thong-nhat.md:{n}", tc[n - 1][:90])
vh = (AT / "ho-so" / "opus" / "h5" / "verdict_h5.py")
p("verdict_h5.py ton_tai", vh.exists(), "so_dong", len(vh.read_text(encoding="utf-8").splitlines()) if vh.exists() else "-")
hx = (OUT / "evidence" / "de-xuat-hop-nhat.py").read_text(encoding="utf-8").splitlines()
p("de-xuat-hop-nhat.py:53", hx[52][:90])
p("de-xuat-hop-nhat.py:61", hx[60][:90])
l3 = (U / "l3b-de-cu-opus.tsv")
p("U/l3b-de-cu-opus.tsv ton_tai", l3.exists(), "so_dong_du_lieu", len(lines(l3)) - 1 if l3.exists() else "-",
  "dong3", lines(l3)[2].split("\t")[0] if l3.exists() else "-")

p("== Lịch sử lượt viết của 132 mục khấu trừ (nhận định của Astra về mặt khác)")
k132 = [r["tu"] for r in rd(U / "p7-v3-khau-tru-132-theo-P0-astra.tsv")]
seen = collections.defaultdict(set)
for v in ("v1", "v2", "v3"):
    for r in rd(U / f"d6-log-{v}.tsv"):
        seen[r["tu"]].add(v)
p("so_muc", len(k132), "theo_luot", dict(collections.Counter("+".join(sorted(seen[w])) for w in k132)))
p("muc_thieu_v1", [w for w in k132 if "v1" not in seen[w]])
for v in ("v1", "v2"):
    p(f"mat_khac_trong_viet-lai-{v}", any(r.get("tu") == "mặt khác" for r in rd(U / f"viet-lai-{v}.tsv")))

p("== SHA vùng bảo vệ (kế hoạch §3, §4.3)")
import hashlib
import subprocess
for f in ("index.html", "thong-tin.html", "analyzing-tools/wordlist.txt"):
    p(f"sha_byte {f}", hashlib.sha256((REPO / f).read_bytes()).hexdigest())
docb = (REPO / "WordListAnalyze.md").read_bytes()
a10 = docb.index("## 10. Danh sách 7.776 từ phát hành".encode())
b11 = docb.index("## 11. ".encode(), a10)
p("sha_byte muc10 (từ đầu dòng ## 10. đến ngay trước dòng ## 11.)", hashlib.sha256(docb[a10:b11]).hexdigest())
blob = subprocess.run(["git", "-C", str(REPO), "show", "HEAD:analyzing-tools/wordlist.txt"], capture_output=True).stdout
p("sha_lf wordlist.txt", hashlib.sha256(blob).hexdigest())
p("sha cot tu", hashlib.sha256("".join(l.split("|")[0] + "\n" for l in blob.decode().splitlines()).encode()).hexdigest())
dub = subprocess.run(["git", "-C", str(REPO), "show", "HEAD:analyzing-tools/du-phong.txt"], capture_output=True).stdout
p("sha_lf du-phong.txt", hashlib.sha256(dub).hexdigest())

(HERE / "kiem-ban-nhap-chung.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
print("\n".join(log))
