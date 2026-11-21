"""Lượt duyệt 2: kiểm bản sửa 1 của năm tệp U/du-phong-v2-* theo 13 thay đổi bắt buộc trong round-1-review-drafts.md.

    python kiem-ban-sua-1.py  ->  kiem-ban-sua-1.log

Chỉ đọc. Mỗi dòng log: DAT/CHUA_DAT, mã yêu cầu, mô tả, giá trị đo.
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


R = tsv(U / "du-phong-v2-phan-loai.tsv")
H = tsv(U / "du-phong-v2-honorable-mentions.tsv")
Rw = {r["tu"]: r for r in R}
Hw = {r["tu"]: r for r in H}
du = lines(AT / "du-phong.txt")
main = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
kmain, kdu = {key(w) for w in main}, {key(w) for w in du}
cau_hoi = (U / "du-phong-v2-cau-hoi.md").read_text(encoding="utf-8")
bao_cao = (U / "du-phong-v2-bao-cao-chung.md").read_text(encoding="utf-8")
ke_hoach = (U / "du-phong-v2-ke-hoach.md").read_text(encoding="utf-8")

ghi("== Bất biến của hai TSV")
kiem("TSV-R", "205 dòng, 23 cột, đúng thứ tự du-phong.txt", len(R) == 205 and len(R[0]) == 23 and [r["tu"] for r in R] == du)
ghi("tang_chung", dict(sorted(collections.Counter(r["tang_chung"] for r in R).items())))
ghi("giai_nghia", dict(collections.Counter(r["giai_nghia"] for r in R)), "h8", dict(collections.Counter(r["h8"] for r in R)))
kiem("TSV-H", "285 dòng, 27 cột, khóa duy nhất, không giao chính/dự phòng",
     len(H) == 285 and len(H[0]) == 27 and len({r["khoa"] for r in H}) == 285
     and not ({r["khoa"] for r in H} & (kmain | kdu)) and all(key(r["tu"]) == r["khoa"] for r in H))
tinh = [r for r in H if r["ket_luan_nhap"] == "CUNG_DE_CU_CHUA_PHAT_HANH"]
ghi("ket_luan_nhap", dict(collections.Counter(r["ket_luan_nhap"] for r in H)))
ghi("N theo nhom", dict(collections.Counter(r["nhom"] for r in tinh)), "h8 cua N", dict(collections.Counter(r["h8"] for r in tinh)))
kiem("TSV-H", "N = 237 và không còn tranh chấp/câu hỏi trong HM", len(tinh) == 237
     and all(r["tranh_chap"] == "KHONG" and r["cau_hoi"] == "-" for r in H))
nghia = [l.split("|", 1)[1] for l in lines(AT / "wordlist.txt")]
txt = (U / "du-phong-v2-phan-loai.tsv").read_text(encoding="utf-8") + (U / "du-phong-v2-honorable-mentions.tsv").read_text(encoding="utf-8")
kiem("T8", "không có câu giải nghĩa của danh sách chính trong hai TSV", sum(g in txt for g in nghia) == 0)

ghi("== Thay đổi bắt buộc 1–3 (TSV dự phòng)")
T8 = ["ăn trầu", "bèo bọt", "chấp nhặt", "giở giọng", "giở quẻ", "mụ mị", "non choẹt", "tía lia"]
kiem("1", "tám mục A/A, KHONG, '-', ý kiến Opus mới", all(
    Rw[w]["tang_opus"] == Rw[w]["tang_chung"] == "A" and Rw[w]["tranh_chap"] == "KHONG" and Rw[w]["cau_hoi"] == "-"
    and Rw[w]["y_kien_opus"].startswith("A: nhận lần rút C của Astra") for w in T8))
kiem("1", "ăn trầu có câu không đưa nhận định y khoa", "Không đưa nhận định y khoa" in Rw["ăn trầu"]["y_kien_opus"])
T3 = ["hì hụi", "nhão nhẹt", "nhão nhoẹt"]
kiem("2", "ba mục D/D, KHONG, '-', KHONG_DUNG_H5_H9, con_thieu như D cũ, ý kiến Opus ký", all(
    Rw[w]["tang_opus"] == Rw[w]["tang_chung"] == "D" and Rw[w]["tranh_chap"] == "KHONG" and Rw[w]["cau_hoi"] == "-"
    and Rw[w]["trang_thai_h"] == "KHONG_DUNG_H5_H9" and Rw[w]["con_thieu"] == Rw["tròng trành"]["con_thieu"]
    and Rw[w]["y_kien_opus"].startswith("D (H5c): Opus ký") for w in T3))
for w in T3:
    ghi(f"  y_kien_opus {w}:", Rw[w]["y_kien_opus"])
v = Rw["vậy nên"]
kiem("3", "vậy nên: H7_K2, trạng thái lịch sử, '-', bỏ 'Khép H7', ý kiến K2", v["ma_van_de"] == "H7_K2;CHUA_VIET;D8_CHUA_CO"
     and v["trang_thai_h"] == "HO_SO_LICH_SU_CHUA_PHE_DUYET_THAY" and v["cau_hoi"] == "-" and "Khép H7" not in v["con_thieu"]
     and "K2" in v["y_kien_opus"] and "không tự động chặn" in v["y_kien_astra"])

ghi("== Thay đổi bắt buộc 4–6 (TSV HM)")
S5 = ["cơ quan", "dự bị", "lên chức", "lực lượng", "truy tìm"]
kiem("4", "năm mục: ý kiến Opus là giữ có cờ; bang_chung trỏ lý do cụ thể của Astra", all(
    Hw[w]["y_kien_opus"].startswith("Opus giữ đề cử có cờ") and "de-cu-hop-nhat-de-xuat-opus.tsv:" in Hw[w]["bang_chung"] for w in S5))
kiem("4", "đại lục: CO_DIEU_KIEN, ý kiến Opus đổi lập trường", Hw["đại lục"]["de_cu_opus"] == "CO_DIEU_KIEN"
     and Hw["đại lục"]["y_kien_opus"].startswith("Opus đổi lập trường"))
kiem("4", "sáu mục được tính, KHONG, '-', điều kiện rà H6", all(
    Hw[w]["ket_luan_nhap"] == "CUNG_DE_CU_CHUA_PHAT_HANH" and Hw[w]["tranh_chap"] == "KHONG" and Hw[w]["cau_hoi"] == "-"
    and "rà H6 trước khi dùng" in Hw[w]["dieu_kien"] for w in S5 + ["đại lục"]))
b, t = Hw["bao tử"], Hw["tần số"]
kiem("5", "bao tử LOAI_K1, KHONG_DE_CU, H7_K1", b["ket_luan_nhap"] == "LOAI_K1" and b["de_cu_opus"] == "KHONG_DE_CU"
     and b["trang_thai_h"].endswith("H7_K1") and b["y_kien_opus"].startswith("Nhận K1 của Astra"))
kiem("5", "tần số được tính, H7_K2, hai chữ ký", t["ket_luan_nhap"] == "CUNG_DE_CU_CHUA_PHAT_HANH"
     and t["trang_thai_h"].endswith("H7_K2") and "K2" in t["y_kien_opus"])
l3 = [r for r in H if r["nhom"] == "L3B_CHUA_CHAM"]
kiem("6", "46 L3b NGOAI_HM_CHUA_THAM_DINH, KHONG_TINH_HM, ý kiến Opus theo phương án 2", len(l3) == 46 and all(
    r["ket_luan_nhap"] == "NGOAI_HM_CHUA_THAM_DINH" and r["de_cu_opus"] == "KHONG_TINH_HM"
    and r["y_kien_opus"].startswith("Q-dpv2-4 phương án 2") for r in l3))
kiem("6", "giờ cao điểm: Opus nhận phản đối H2; cờ H2 ở dieu_kien", "phản đối H2" in Hw["giờ cao điểm"]["y_kien_opus"]
     and Hw["giờ cao điểm"]["dieu_kien"].startswith("H2"))
kiem("6", "ớt đỏ, nắng ấm: cờ X ở dieu_kien", all("X" in Hw[w]["dieu_kien"] for w in ("ớt đỏ", "nắng ấm")))
kiem("6", "chạng vạng NGOAI_HM_CHO_H5", Hw["chạng vạng"]["ket_luan_nhap"] == "NGOAI_HM_CHO_H5"
     and Hw["chạng vạng"]["de_cu_opus"] == "KHONG_TINH_HM")

ghi("== Thay đổi bắt buộc 7–8 (tệp câu hỏi)")
de_muc = re.findall(r"^## (Q-dpv2-\d+)", cau_hoi, re.M)
ghi("cac_cau_con_trong_tep", de_muc)
kiem("7", "chỉ còn câu mở; Q-dpv2-2..6 không còn trong tệp", not any(q in de_muc for q in
     ("Q-dpv2-2", "Q-dpv2-3", "Q-dpv2-4", "Q-dpv2-5", "Q-dpv2-6")))
q1 = cau_hoi[cau_hoi.index("## Q-dpv2-1"):cau_hoi.index("## Q-dpv2-7")] if "## Q-dpv2-7" in cau_hoi else cau_hoi[cau_hoi.index("## Q-dpv2-1"):]
for truong in ("**Addressee:** owner", "**Decision needed:**", "**Context:**", "**Evidence:**", "**Options:**",
               "**The SAs' recommendation:**", "**Blocked:**"):
    kiem("8", f"Q-dpv2-1 có trường {truong}", truong in q1)
for so in ("632", "474", "1.177", "634", "227", "117", "1.809", "4156"):
    kiem("8", f"Q-dpv2-1 có số {so}", so in q1)
kiem("8", "Q-dpv2-1 câu hì hục đã sửa", "không ai kết luận hì hục sai H5" in q1)
kiem("8", "dòng Answer của mọi câu để trống", all(l.strip().endswith("<date>):**") for l in cau_hoi.splitlines()
                                                  if l.startswith("**Answer")))
for p_ in re.findall(r"`((?:OE|O|E|U|AT|A)\\[^`]+?)`", q1):
    goc = {"OE": OUT / "evidence", "O": OUT, "E": AT / "ho-so" / "astra" / "du-phong-v2" / "evidence", "U": U, "AT": AT,
           "A": AT / "ho-so" / "astra" / "du-phong-v2"}
    tien_to, _, duoi = p_.partition("\\")
    tep = re.sub(r":[\d–,\s]+$", "", duoi)
    kiem("8", f"đường dẫn bằng chứng tồn tại: {p_}", (goc[tien_to] / tep.replace("\\", "/")).exists())

ghi("== Thay đổi bắt buộc 9–10 (báo cáo chung)")
kiem("9", "dòng trạng thái ghi Opus changes requested", "changes requested" in bao_cao.splitlines()[2])
kiem("9", "tóm tắt: mốc A149/B36/C14/D6, N=237, câu còn mở", "A149/B36/C14/D6" in bao_cao and "N=237" in bao_cao
     and "Q-dpv2-1" in bao_cao)
kiem("10", "bảng tầng có hàng sau hòa và bản sửa", "Hai SA sau đóng 11 lệch cũ | 149 | 36 | 14 | 6 | 0" in bao_cao)
kiem("10", "bảng 11 điểm đã hòa", "### 2.1. Lịch sử 11 điểm đã hòa" in bao_cao)
kiem("10", "bảng HM có cột Tính vào N", "| Nhóm hồ sơ | Tổng dòng | Tính vào N | Không tính |" in bao_cao)
kiem("10", "§4.2–4.6 ghi đã đóng", all(f"### 4.{i}. Q-dpv2-{i} — đã đóng" in bao_cao for i in range(2, 7)))

ghi("== Thay đổi bắt buộc 11–13 (kế hoạch)")
kiem("11", "§3 tầng và N", "A149/B36/C14/D6" in ke_hoach and "**N=237**" in ke_hoach)
kiem("11", "§4.1 phân biệt dòng tính/không tính", "NGOAI_HM_CHUA_THAM_DINH" in ke_hoach and "LOAI_K1" in ke_hoach)
kiem("11", "§4.2 công thức N cố định", "N = count(ket_luan_nhap == \"CUNG_DE_CU_CHUA_PHAT_HANH\")" in ke_hoach)
kiem("11", "§5.2 không còn nhánh HM có điều kiện", "Nếu nhận nhóm có điều kiện" not in ke_hoach and "CHINH_SACH_UNG_VIEN" not in ke_hoach)
kiem("11", "§5.2 đoạn §12.3 đúng văn bản yêu cầu", "Không tính vào N: lô L3b (48 ứng viên" in ke_hoach
     and "*bao tử* (K1: khóa `baotu` đọc thành *báo tử*)" in ke_hoach)
kiem("11", "§9 có T-dpv2-4..8", all(f"| T-dpv2-{i} |" in ke_hoach for i in range(4, 9)))
kiem("11", "§11 bỏ rủi ro lệch thời điểm", "Lệch thời điểm review" not in ke_hoach)
kiem("11", "§13 ghi Q-dpv2-2..6 đã đóng, OI-SCAN có số", "Đã đóng: T-dpv2-8" in ke_hoach and "1.177 cặp H7/634 khóa" in ke_hoach)
kiem("12", "§8.2 và T5 có build --check trên tài liệu đã sửa ở CRLF",
     "`build_wordlist.py --check` trên tài liệu đã sửa, CRLF" in ke_hoach and "build --check trên tài liệu đã sửa ở CRLF" in ke_hoach)
kiem("13", "§2 ngoài phạm vi có hai tài liệu lưu trữ và quyết định 10", "`WordListAnalyze-Opus.md:265`" in ke_hoach
     and "`WordListAnalyze-Astra.md:95`" in ke_hoach and "`WordListAnalyze.md:153`" in ke_hoach)
kiem("13", "§13 có OI-BANG-PHAT-HANH", "| OI-BANG-PHAT-HANH |" in ke_hoach)

ghi("== Vùng bảo vệ và tệp đã theo dõi")
for f, h in (("index.html", "01b76617f8df57d80e59d0989001ced8f7714ae95e85828b351bce2a5517a423"),
             ("thong-tin.html", "8ec3bbf763f2465994bde4239079a3795eb2eb3bf21f61fe29aa683cb8bf3ea7"),
             ("analyzing-tools/wordlist.txt", "8945fd4a732b210b4e027f6660b4f42d53b2344088028f967e01a30af7bbc6b4")):
    kiem("B1", f"SHA byte {f}", hashlib.sha256((REPO / f).read_bytes()).hexdigest() == h)
diff = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain", "--untracked-files=no"], capture_output=True, text=True).stdout
kiem("B1", "không tệp đã theo dõi nào bị sửa (kể cả hai tài liệu lưu trữ)", diff.strip() == "", diff.strip())

ghi(f"Tổng: {loi} yêu cầu chưa đạt.")
(HERE / "kiem-ban-sua-1.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
print("\n".join(log))
