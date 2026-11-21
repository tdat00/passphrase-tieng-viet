"""Bước 3: lập bảng đề cử thêm (honorable mentions) và nhật ký loại.

Nguồn (theo thứ tự ưu tiên):
  DC1  132 mục khấu trừ theo kịch bản P0 (D6/D7 của giải nghĩa; từ đã qua H1–H9, nhãn OK);
  DC2  R1 không-F của L1, phiếu P4 lệch OK/R1, F ≥ 50, sau khi bỏ các mục kề nhóm đỏ hoặc quá chuyên môn;
       lấy 60 mục điểm S3 cao nhất;
  DC3  lô L3b (48, Opus đề cử, chưa chấm), bỏ mục trượt luật;
  DC4  lô L2D (99, H8 yếu, chưa chấm), chỉ lấy mục đời thường có tổng chứng liệu ≥ 5 hoặc tên vật ba khối rõ;
  DC5  mục chưa từng vào rổ, có trong HND (kiểm bằng kiem-hnd.py), qua kiểm hình thức.

    python lap-de-cu.py
Ghi evidence/de-cu-ung-vien.tsv (mọi ứng viên, kèm cột loai_vi) và in tóm tắt.
"""
import collections
from chung import *

out_utf8()
main = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
res = lines(AT / "du-phong.txt")
taken = {key(w): ("CHINH", w) for w in main}
taken.update({key(w): ("DU_PHONG", w) for w in res})
blocked = {r["khoa"]: r["ma"] for r in rd(AT / "blocked_keys.tsv")}
fam = collections.defaultdict(list)
for r in rd(AT / "spelling_families.tsv"):
    for x in (r["chuan"], r["bien_the"]):
        fam[x].append(f'{r["chuan"]}/{r["bien_the"]}:{r["ket_luan"]}')
xh = {r["tu"]: r for r in rd(U / "xep-hang.tsv")}
p1 = p1_table()
oc = counts_opus()
po = {r["tu"]: r for r in rd(U / "phieu-opus.tsv")}
pa = {r["tu"]: r for r in rd(U / "phieu-astra.tsv")}
cb = collections.defaultdict(list)
for r in rd(U / "canh-bao-khong-dau.tsv"):
    cb[r["ung_vien"]].append(f'{r["doc_khac"]}:{r["trang_thai_9_1"]}')
lot_counts = {}
for f in ["l2-ung-vien.tsv", "l2b-ung-vien.tsv", "l2c-ung-vien.tsv", "l3-ung-vien.tsv"]:
    for r in rd(U / f):
        lot_counts[r["tu"]] = {**r, "_lo": f.split("-ung")[0].upper()}
ck = collections.defaultdict(set)
for r in rd(U / "chu-ky.tsv"):
    if r["hieu_luc"] == "CO":
        ck[r["tu"]].add(f'{r["loai_ky"]}:{r["nguoi_ky"]}')
LETTERS = set("aăâbcdđeêghiklmnoôơpqrstuưvxy ")


def h1_ok(w):
    base = "".join(c for c in unicodedata.normalize("NFD", w) if c not in TONES)
    return set(unicodedata.normalize("NFC", base)) <= LETTERS and "  " not in w and w == w.strip()


# Mã loại tay cho DC2 (R1). Lý do bằng lời của Opus, chỉ để lọc đề cử; không phải phản đối H9.
LOAI_R1 = {
    "CT": "chính trị, nhà nước, hành chính hay di trú",
    "PL": "pháp lý, tố tụng",
    "QS": "quân sự, mệnh lệnh, cấp bậc",
    "YT": "y khoa, bệnh",
    "TG": "tôn giáo, tâm linh, tang lễ",
    "TC": "tài chính chuyên ngành",
    "KT": "từ hành chính khô, ít gợi hình",
    "NC": "dễ gợi nghĩa nhạy cảm hay vũ khí",
    "H5": "có cách ghi khác chưa đo (H5f)",
}
R1_LOAI = {
    "hội đồng": "CT", "hạt nhân": "NC", "tín dụng": "TC", "chứng khoán": "TC", "cổ phiếu": "TC", "hiệu lực": "PL",
    "cổ phần": "TC", "thực thi": "PL", "vi khuẩn": "YT", "chức vụ": "CT", "di cư": "CT", "biên giới": "CT", "cư trú": "PL",
    "nghiệp vụ": "KT", "chỉ định": "YT", "đối lập": "CT", "phán xét": "TG", "dân chúng": "CT", "phê duyệt": "KT",
    "kinh phí": "KT", "điều khoản": "PL", "tiền tệ": "TC", "trái phiếu": "TC", "đại hội": "CT", "hô hấp": "YT",
    "môi giới": "NC", "nhập cư": "CT", "thâm nhập": "NC", "vô hiệu": "PL", "nồng độ": "NC", "quyền hạn": "CT",
    "viếng thăm": "TG", "hội nhập": "CT", "kinh dị": "NC", "kiểm toán": "TC", "mệnh lệnh": "QS", "thanh lọc": "CT",
    "nhập cảnh": "PL", "bộ lạc": "NC", "cấp bậc": "QS", "quyền năng": "TG", "tôn kính": "TG", "piano": "H5",
    "thị thực": "PL", "chiến lược": "QS", "quốc tế": "CT", "nội bộ": "KT", "địa vị": "KT", "tầng lớp": "KT",
    "niêm phong": "PL", "độc quyền": "TC", "đàm phán": "CT", "thôi miên": "TG", "tiên đoán": "TG", "phản lực": "QS",
    "đột biến": "YT", "nhân sự": "KT", "quản trị": "KT", "chuyển nhượng": "TC", "hàm lượng": "KT", "hạng mục": "KT",
    "cơ cấu": "KT", "cơ chế": "KT", "sơ bộ": "KT", "trọng điểm": "KT", "khuôn khổ": "KT", "tác nhân": "KT",
    "thực thể": "KT", "cục bộ": "KT", "phương diện": "KT", "chuyên dụng": "KT", "cung ứng": "KT", "doanh số": "TC",
    "tham chiếu": "KT", "kiểm định": "KT", "thẩm định": "KT", "tiến trình": "KT", "tổng thể": "KT", "thực tiễn": "KT",
    "tối ưu": "KT", "nguồn lực": "KT", "kết cấu": "KT", "thông số": "KT", "tổ hợp": "KT", "tương đồng": "KT",
    "cá thể": "KT", "khuyến cáo": "KT", "nhận định": "KT", "đồng thuận": "CT", "xúc tiến": "KT", "tư liệu": "KT",
    "cấu hình": "KT", "thường niên": "KT", "chuyên sâu": "KT", "sản lượng": "KT", "điều phối": "KT", "chuyên đề": "KT",
    "tự phát": "KT", "giảm thiểu": "KT", "triển khai": "KT", "hiện diện": "KT", "đề cập": "KT", "khả thi": "KT",
    "tiếp cận": "KT", "chỉ số": "KT", "tuân theo": "KT", "trích dẫn": "KT", "khuynh hướng": "KT", "hiệu suất": "KT",
    "tích hợp": "KT", "kiểm chứng": "KT", "trọng đại": "KT", "lập luận": "KT", "kế thừa": "KT", "chiết xuất": "KT",
    "phúc lợi": "CT", "xuyên suốt": "KT", "cơ giới": "QS", "mật độ": "KT", "lưu lượng": "KT", "cường độ": "KT",
}

rows = []


def add(group, w, **kw):
    rows.append({"nhom": group, "tu": w, **kw})


# DC1
for r in rd(U / "p7-v3-khau-tru-132-theo-P0-astra.tsv"):
    ma = r["cong"] if r["cong"] != "D6_CUOI" else "D6_CUOI:" + r["ly_do"].split("mã ")[-1]
    add("DC1", r["tu"], ly_do_chua_chon=f"Khấu trừ P0 ({ma}); vị trí trước khi trừ: {xh[r['tu']]['vao']}",
        dieu_kien="Chủ dự án cho ngoại lệ D7 (thêm một lượt viết sạch); D6 theo P0, D7; chạy lại P6")
# DC2
for w, r in xh.items():
    if r["nhan"] != "R1" or r["lop"] == "F" or w not in po or w not in pa:
        continue
    o, a = po[w]["nhan"], pa[w]["nhan"]
    if {o, a} != {"OK", "R1"} or float(r["F"]) < 50:
        continue
    add("DC2", w, phieu=f"O={o};A={a}", ly_do_chua_chon="Nhãn gộp R1 (một bên OK, một bên R1); OK không-F được ưu tiên trước R1 (S3/S4)",
        dieu_kien="Hai bên phân xử lại nhãn R1→OK và ký (luật gộp P4), hoặc chủ dự án cho dùng R1 theo Q2 khi hết OK không-F; viết nghĩa sạch, D6, D7",
        loai_vi=("DC2_" + R1_LOAI[w] + ": " + LOAI_R1[R1_LOAI[w]]) if w in R1_LOAI else "")
# DC3
L3B_LOAI = {"chạy nước rút": "H2: mục ba khối là cụm động từ, không phải tên vật cố định",
            "cồn cát": "H7: khóa concat có cách đọc tục phổ biến ở phương ngữ Nam (nghi K1), cần hai bên xét; không đề cử"}
L3B_NOTE = {"ớt đỏ": "Cần xét X (tổ hợp tự do) ở P4", "nắng ấm": "Cần xét X (tổ hợp tự do) ở P4",
            "ánh nhìn": "", "bánh sinh nhật": "Dài 12 chữ, đúng mức trần"}
for r in rd(U / "l3b-de-cu-opus.tsv"):
    w = r["tu"]
    add("DC3", w, ly_do_chua_chon="Lô đệm L3b (Opus đề cử ở tin 083, rút ở tin 085 vì C13 đủ); chưa chạy P2, chưa chấm P4",
        dieu_kien="P2 hai bộ kiểm, P4 chấm đôi, H9, P5; viết nghĩa sạch, D6, D7" + ("; " + L3B_NOTE[w] if L3B_NOTE.get(w) else ""),
        loai_vi=L3B_LOAI.get(w, ""), sub_sach=r["sub_sach"], web_sach=r["web_sach"], hnd_lo=r["hnd"], wikt=r["wiktionary"])
# DC4
L2D_CHON = {"chim khách", "cá kìm", "cải bẹ", "củ từ", "gà giò", "mái hắt", "nhà ngang", "nước ròng", "rau lang", "đèn bão",
            "đậu ván", "ốc nhồi", "kem cây", "mèo mướp", "cá chuối", "máy quay đĩa", "cá thờn bơn", "bánh củ cải", "hoa mõm sói"}
for r in rd(U / "l2d-ung-vien.tsv"):
    w = r["tu"]
    if w not in L2D_CHON:
        continue
    add("DC4", w, ly_do_chua_chon="Lô dự bị L2D (Astra lập sổ; H8 yếu); chưa chấm, không đưa vào pool",
        dieu_kien="Đọc ngữ cảnh xác nhận đúng nghĩa (H8 yếu); " + ("H3 cần hai xác nhận; " if "H3_CAN_HAI_XAC_NHAN" in r["co_ke_hoach"] else "")
        + ("H2 ba khối phải là tên vật cố định; " if "H2_BA_KHOI" in r["co_ke_hoach"] else "") + "P2, P4, H9; viết nghĩa sạch, D6, D7",
        sub_sach=r["sub_sach"], web_sach=r["web_sach"], leipzig=r["leipzig_so_cau"], tatoeba=r["tatoeba_so_cau"], hnd_lo=r["nguon_tu_dien"])
# DC5 (đã kiểm HND bằng kiem-hnd.py trên danh sách tự nghĩ; xem chua-vao-ro-hnd.tsv)
for w, h in [("cặp lồng", "22K;39K;74K"), ("chè đỗ đen", "74K"), ("sao mai", "11K;22K;39K;74K"), ("sao hôm", "11K;22K;39K;74K"),
             ("vịt bầu", "39K;74K")]:
    add("DC5", w, ly_do_chua_chon="Chưa từng vào rổ P1 (không bên nào chọn); có trong HND", hnd_lo=h,
        dieu_kien="Đếm bốn kho (count_corpus.py), P2, P4, H9; viết nghĩa sạch, D6, D7")

# Kiểm chung
seen = collections.Counter(key(r["tu"]) for r in rows)
for r in rows:
    w = r["tu"]
    k = key(w)
    r["khoa"] = k
    r["so_chu"] = len(k)
    r["so_khoi"] = len(w.split(" "))
    x = xh.get(w, {})
    r["nhan"] = x.get("nhan", "")
    r["lop"] = x.get("lop", "")
    r["F"] = f'{float(x["F"]):.2f}' if x else ""
    r["diem"] = f'{float(x["diem"]):.2f}' if x else ""
    r["hang_xep_hang_v2"] = x.get("hang", "")
    c = oc.get(w)
    p = p1.get(w, {})
    lv = lot_counts.get(w)
    if c:
        r["sub_sach"], r["web_sach"] = c["sub_sach"], c["web_sach"]
    elif lv and not r.get("sub_sach"):
        r["sub_sach"], r["web_sach"] = lv["sub_sach"], lv["web_sach"]
    if p:
        r["leipzig"], r["tatoeba"] = p.get("leipzig_so_cau"), p.get("tatoeba_so_cau")
        r["nguon_P1"] = p.get("nguon")
    elif lv and not r.get("leipzig"):
        r["leipzig"], r["tatoeba"] = lv.get("leipzig_so_cau", ""), lv.get("tatoeba_so_cau", "")
        r["nguon_P1"] = "LO:" + lv["_lo"]
    sub = int(r["sub_sach"]) if str(r.get("sub_sach", "")).strip() not in ("", "None") else None
    web = int(r["web_sach"]) if str(r.get("web_sach", "")).strip() not in ("", "None") else None
    lei = int(r["leipzig"]) if str(r.get("leipzig", "")).strip() not in ("", "None") else None
    tat = int(r["tatoeba"]) if str(r.get("tatoeba", "")).strip() not in ("", "None") else None
    r["H8"] = h8(sub, web, lei, tat)
    if "phieu" not in r and w in po and w in pa:
        r["phieu"] = f'O={po[w]["nhan"]};A={pa[w]["nhan"]}'
    r["chu_ky"] = ";".join(sorted(ck.get(w, [])))
    r["canh_bao_H7"] = ";".join(cb.get(w, []))
    loi = []
    if not h1_ok(w):
        loi.append("H1")
    if not (4 <= len(k) <= 12 and 1 <= r["so_khoi"] <= 3):
        loi.append("H2_DO_DAI")
    if k in taken:
        loi.append(f"H4_TRUNG_KHOA:{taken[k][0]}:{taken[k][1]}")
    if seen[k] > 1:
        loi.append("H4_TRUNG_KHOA_TRONG_DE_CU")
    if k in blocked:
        loi.append(f"KHOA_BI_CHAN:{blocked[k]}")
    bad_fam = [f for f in fam.get(w, []) if ":LOAI" in f or ":CHO" in f]
    if bad_fam:
        loi.append("H5:" + ",".join(bad_fam))
    r["ho_chinh_ta"] = ";".join(fam.get(w, []))
    r["kiem_tu_dong"] = ";".join(loi) if loi else "DAT"
    if loi and not r.get("loai_vi"):
        r["loai_vi"] = "TU_DONG: " + ";".join(loi)

# DC2: chỉ giữ 60 mục điểm cao nhất trong số không bị loại
dc2 = sorted([r for r in rows if r["nhom"] == "DC2" and not r.get("loai_vi")], key=lambda r: (-float(r["diem"]), len(r["khoa"])))
for i, r in enumerate(dc2):
    if i >= 60:
        r["loai_vi"] = "DC2_NGOAI_60: ngoài 60 mục điểm cao nhất"

header = ["nhom", "tu", "khoa", "so_chu", "so_khoi", "nhan", "lop", "F", "diem", "hang_xep_hang_v2", "phieu", "nguon_P1", "hnd_lo",
          "wikt", "sub_sach", "web_sach", "leipzig", "tatoeba", "H8", "chu_ky", "canh_bao_H7", "ho_chinh_ta", "kiem_tu_dong",
          "ly_do_chua_chon", "dieu_kien", "loai_vi"]
write_tsv(HERE / "de-cu-ung-vien.tsv", header, rows)
kept = [r for r in rows if not r.get("loai_vi")]
write_lines(HERE / "de-cu-giu.txt", [r["tu"] for r in kept])
print("ứng viên:", collections.Counter(r["nhom"] for r in rows))
print("giữ:", collections.Counter(r["nhom"] for r in kept), len(kept))
print("lý do loại:", collections.Counter(r["loai_vi"].split(":")[0] for r in rows if r.get("loai_vi")))
print("tự động trượt:", [(r["tu"], r["kiem_tu_dong"]) for r in rows if r["kiem_tu_dong"] != "DAT"])
print("H8:", collections.Counter((r["nhom"], r["H8"]) for r in kept))
