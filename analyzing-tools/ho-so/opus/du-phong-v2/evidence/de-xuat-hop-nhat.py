"""Soát chéo vòng 1: đề xuất hợp nhất của Opus sau khi đọc Astra (bậc dự phòng và tập đề cử).

    python de-xuat-hop-nhat.py
Ghi evidence/du-phong-205-bac-sau-soat-cheo-opus.tsv và evidence/de-cu-hop-nhat-de-xuat-opus.tsv.
"""
import collections
from chung import *

out_utf8()
AS = AT / "ho-so" / "astra" / "du-phong-v2"
op = {r["tu"]: r for r in rd(OUT / "du-phong-205-phan-loai-opus.tsv", True)}
asr = {r["tu"]: r for r in rd(AS / "du-phong-phan-loai.tsv")}

# D giữ lại: có chứng cứ kiểm được rằng hai dạng là một từ, hoặc tiền lệ họ đã ký cùng phép đổi
D_GIU = {
    "tròng trành": "en.wiktionary (oldid 89219050) ghi chòng chành là dạng khác (Alternative forms); chòng chành ở danh sách chính",
    "chán phèo": "vi.wiktionary (oldid 2366348) ghi chán phèo 'như chán phè', nhãn thông tục, hiếm; chán phè có trong HND 22K",
    "chọc lét": "Cùng phép đổi lét/léc với họ cù lét/cù léc đã đăng ký loại c (spelling_families.tsv:116); HND có chọc léc; Wiktionary ghi giọng Sài Gòn đọc lét thành [lɛk]",
}
# D hạ xuống C: "cùng một từ" chỉ là nhận định, chưa có nguồn kiểm được
D_HA_C = {
    "hì hụi": "Gần nghĩa với hì hục (danh sách chính); chưa có nguồn ghi là một từ (en.wiktionary chỉ ghi dạng khác hè hụi)",
    "nhão nhẹt": "Cùng nghĩa với nhão nhoẹt (dự phòng), khác khóa; dùng tối đa một; chưa có nguồn ghi là một từ",
    "nhão nhoẹt": "Cùng nghĩa với nhão nhẹt (dự phòng), khác khóa; dùng tối đa một; vi.wiktionary chỉ nối với nhão nhoét (cùng khóa)",
}
rows = []
for w, o in op.items():
    a = asr[w]
    b1, t1 = o["bac"], a["tang"]
    if w in D_GIU:
        moi, ly = "D", "Giữ D (H5c, phản đối H9 của Opus): " + D_GIU[w]
    elif w in D_HA_C:
        moi, ly = "C", "Hạ D→C: " + D_HA_C[w]
    elif b1 == "C" or t1 == "C":
        moi = "C"
        ly = "; ".join(x for x in ((("Opus: " + o["van_de"].split(" | ")[0]) if b1 == "C" else ""),
                                   (("Astra: " + a["danh_gia_moi"].replace("assumed:", "")) if t1 == "C" else "")) if x)
    elif b1 == "B" or t1 == "B":
        moi, ly = "B", "Chưa có câu giải nghĩa"
    else:
        moi, ly = "A", "Hai bên cùng A" if b1 == t1 == "A" else f"Opus {b1}, Astra {t1}"
    rows.append({"tu": w, "ngan": o["ngan"], "bac_opus_v1": b1, "tang_astra_v1": t1, "bac_de_xuat": moi, "ly_do": ly})
write_tsv(HERE / "du-phong-205-bac-sau-soat-cheo-opus.tsv", ["tu", "ngan", "bac_opus_v1", "tang_astra_v1", "bac_de_xuat", "ly_do"], rows)
c = collections.Counter((r["ngan"], r["bac_de_xuat"]) for r in rows)
print("đề xuất:", dict(sorted(c.items())), collections.Counter(r["bac_de_xuat"] for r in rows))
for b in "DC":
    print(b, [r["tu"] for r in rows if r["bac_de_xuat"] == b])

# Đề cử: DC1 (132, cờ cho 5 mục Astra giữ lại) + R1 hợp hai bên trừ mục bị phủ quyết + DC3 (L3b)
ohm = {r["tu"]: r for r in rd(OUT / "de-cu-them-opus.tsv", True)}
ahm = {r["tu"]: r for r in rd(AS / "honorable-mentions.tsv")}
excl = {r["tu"]: r["ly_do"] for r in rd(AS / "evidence" / "candidate-exclusions.tsv")}
PHU_QUYET_OPUS = {"đại lục": "H6.3 (A): trong báo chí thường chỉ Trung Quốc đại lục; hai bên đều chấm R1"}
out = []
for w in sorted(set(ohm) | set(ahm), key=o1):
    o, a = ohm.get(w), ahm.get(w)
    nhom_o = o["nhom"] if o else ""
    if nhom_o in ("DC4", "DC5"):
        continue
    if w in PHU_QUYET_OPUS:
        continue
    if (o and nhom_o == "DC1") or (a and a["tang"] in ("HM_D6", "HM_D7")):
        nhom = "DC1"
    elif (o and nhom_o == "DC2") or (a and a["tang"] == "HM_R1"):
        nhom = "R1"
    else:
        nhom = "DC3"
    ghi = []
    if w in excl and not excl[w].startswith("verified:khấu trừ"):
        ghi.append("Astra tạm không đề cử: " + excl[w].replace("assumed:", ""))
    if o and o["ghi_chu"]:
        ghi.append(o["ghi_chu"])
    if w == "piano":
        ghi.append("Họ pi a nô/pi-a-nô/pianô đã qua H5 (spelling_families.tsv:269); Opus rút mã loại H5")
    if w == "bánh củ cải":
        ghi.append("H8 YEU theo mẫu số P2 v4.1")
    out.append({"tu": w, "khoa": key(w), "nhom_de_xuat": nhom, "ben": "CA_HAI" if o and a else ("CHI_OPUS" if o else "CHI_ASTRA"),
                "nhan": (o or a)["nhan"] or "-", "lop": (o or a)["lop"] or "-", "ghi_chu": " | ".join(ghi) or "-"})
write_tsv(HERE / "de-cu-hop-nhat-de-xuat-opus.tsv", ["tu", "khoa", "nhom_de_xuat", "ben", "nhan", "lop", "ghi_chu"], out)
print("đề cử đề xuất:", len(out), collections.Counter((r["nhom_de_xuat"], r["ben"]) for r in out))
main_keys = {key(l.split("|")[0]) for l in lines(AT / "wordlist.txt")} | {key(x) for x in lines(AT / "du-phong.txt")}
assert len({r["khoa"] for r in out}) == len(out) and not ({r["khoa"] for r in out} & main_keys)
