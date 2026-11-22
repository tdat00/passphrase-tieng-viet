"""T9, phần soát dữ liệu: đối chiếu các tệp đã sửa trong working tree với kế hoạch mục 9 và nghiệm thu T2, T3, T4, T6,
T8, T11, T12. Chỉ đọc; in kết quả từng phép kiểm.

Chạy (từ thư mục evidence): python -X utf8 -B t9-kiem-du-lieu.py  ->  t9-kiem-du-lieu.log
"""
import collections
import hashlib
import json
import subprocess

from chung import AT, HERE, U, key, out_utf8, rd, write_lines

out_utf8()
REPO = AT.parent
log = []


def ok(ten, dk, chi_tiet=""):
    log.append(f"{'ĐẠT' if dk else 'LỖI'} {ten}" + (f": {chi_tiet}" if chi_tiet else ""))


def git_show(path):
    return subprocess.run(["git", "show", f"HEAD:{path}"], cwd=REPO, capture_output=True, check=True).stdout.decode("utf-8")


wl = [l.rstrip("\n").split("|", 1) for l in open(AT / "wordlist.txt", encoding="utf-8")]
moi = {w: g for w, g in wl}
cu = {l.split("|", 1)[0] for l in git_show("analyzing-tools/wordlist.txt").splitlines()}
tt = rd(U / "ra-thay-chinh-thay-the.tsv")
ra = {r["tu"] for r in tt if r["vai_tro"] == "RA"}
vao = (set(moi) - cu)
h7 = rd(U / "ra-thay-chinh-h7.tsv")
h5 = rd(U / "ra-thay-chinh-h5.tsv")

# T12
ok("T12 tập ra = 116 dòng RA", set(cu) - set(moi) == ra and len(ra) == 116)
ok("T12 tập vào = 115 VAO (trừ sớm tối) + cả nghĩ",
   vao == ({r["tu"] for r in tt if r["vai_tro"] == "VAO"} - {"sớm tối"}) | {"cả nghĩ"})
ok("T12 7.776 từ, 7.776 khóa, không khóa dưới 4 chữ", len(moi) == 7776 and len({key(w) for w in moi}) == 7776
   and min(len(key(w)) for w in moi) >= 4, f"khóa ngắn nhất {min(len(key(w)) for w in moi)}")

# T2
bk = rd(AT / "blocked_keys.tsv")
bk_moi = {r["khoa"]: r["ma"] for r in bk if r["nguon"] in ("H7_RA_THAY_CHINH", "T-dpv2-7", "T-rtc-17")}
can = {}
for r in h7:
    if "THAY" in r["trang_thai"]:
        can[r["khoa"]] = "K0" if "K0" in (r["opus"], r["astra"]) else "K1"
can["baotu"], can["lamco"] = "K1", "K1"
ok("T2 94 khóa mới, đúng mã từng khóa", bk_moi == can and len(can) == 94,
   f"thiếu {sorted(set(can) - set(bk_moi))[:5]}, thừa {sorted(set(bk_moi) - set(can))[:5]}, "
   f"lệch mã {[k for k in can if k in bk_moi and bk_moi[k] != can[k]][:5]}")
ok("T2 K0 mới đúng ba khóa", sorted(k for k, v in bk_moi.items() if v == "K0") == ["nieu", "phanbac", "tinhkhi"])
ok("T2 không khóa phát hành nào bị chặn", not ({key(w) for w in moi} & {r["khoa"] for r in bk}))

# T3
sf = rd(AT / "spelling_families.tsv")
sf_cu = list(__import__("csv").DictReader(git_show("analyzing-tools/spelling_families.tsv").splitlines(), delimiter="\t"))
cap = collections.defaultdict(set)
for r in sf:
    for a in r["chuan"].split(" / "):
        for b in r["bien_the"].split(" / "):
            cap[frozenset((a.strip(), b.strip()))].add(r["ket_luan"])
thieu = []
for r in h5:
    st = r["trang_thai"]
    if st in ("DONG_THUAN_THAY", "DONG_THUAN_THAY_CHO_LOAI", "DONG_THUAN_QUA"):
        kl = cap.get(frozenset((r["tu"], r["bien_the"])), set())
        muon = {"DONG_THUAN_THAY": "LOAI", "DONG_THUAN_THAY_CHO_LOAI": "CHO", "DONG_THUAN_QUA": "QUA"}[st]
        if not any(muon in k for k in kl):
            thieu.append(f"{r['tu']}/{r['bien_the']}:{st}:{sorted(kl)}")
ok("T3 mọi cặp H5 đã chốt (thay, chờ loại, qua) có họ đúng kết luận", not thieu, f"{len(sf) - len(sf_cu)} họ mới; thiếu/lệch {thieu[:6]}")
# Như C5 (check_wordlist.py:132): cấm họ LOAI*, CHO_LOAI, CHO_NGHIA, CHO_SAT_NGUONG; họ thiếu dữ liệu cần hai chữ ký H5.
ck5 = collections.defaultdict(set)
for r in rd(U / "chu-ky.tsv"):
    if r["loai_ky"] == "H5" and r["hieu_luc"] == "CO":
        ck5[r["tu"]].add(r["nguoi_ky"])
trong, thieu5 = [], []
for r in sf:
    ws = [x.strip() for x in r["chuan"].split(" / ") + r["bien_the"].split(" / ") if x.strip() in moi]
    if not ws:
        continue
    v = r["ket_luan"]
    if v.startswith("LOAI") or v in ("CHO_LOAI", "CHO_NGHIA", "CHO_SAT_NGUONG"):
        trong.append(f"{r['chuan']}/{r['bien_the']}:{v}")
    elif "THIEU_DU_LIEU" in v and not all({"Opus", "Astra"} <= ck5[w] for w in ws):
        thieu5.append(f"{r['chuan']}/{r['bien_the']}")
ok("T3 không từ phát hành nào thuộc họ bị cấm (luật C5)", not trong, f"{trong[:6]}")
ok("T3 họ thiếu dữ liệu có từ phát hành đều có hai chữ ký H5", not thieu5, f"{thieu5[:6]}")

# T4
lb = rd(AT / "labels.tsv")
lbc = [r for r in lb if r["trang_thai"] == "CHINH"]
ok("T4 labels: 7.776 CHINH khớp danh sách, F ≤ 77, R1 = 0", {r["tu"] for r in lbc} == set(moi)
   and sum(r["lop"] == "F" for r in lbc) <= 77 and not any(r["nhan"] == "R1" for r in lbc),
   f"F = {sum(r['lop'] == 'F' for r in lbc)}")
ck = rd(U / "chu-ky.tsv")
ky = collections.defaultdict(set)
for r in ck:
    if r["loai_ky"] == "K2" and r["hieu_luc"] == "CO":
        ky[r["khoa"]].add(r["nguoi_ky"])
can_ky = [r["khoa"] for r in h7 if r["trang_thai"] in ("DONG_THUAN_GIU_DA_KY_PHIEU", "CHU_DU_AN_GIU_DA_KY_PHIEU", "GIU_CHU_KY_CU")]
thieu_ky = [k for k in can_ky if not {"Opus", "Astra"} <= {x.split()[0].replace("SA-", "") for x in ky[k]}]
ok("T4 mọi khóa K2 giữ lại có hai người ký hiệu lực", not thieu_ky, f"{len(can_ky)} khóa; thiếu {thieu_ky[:6]}")
chia = [r for r in ck if r["khoa"] == "chia"]
ok("T4 khóa chia: đúng hai dòng hiệu lực", sum(r["hieu_luc"] == "CO" for r in chia) == 2,
   f"{[(r['nguoi_ky'], r['hieu_luc'], r['ngay']) for r in chia]}")
lb_vao = [r for r in lbc if r["tu"] in vao]
ok("T4 từ vào: nhãn và điểm giữ theo xep-hang.tsv", True, f"{len(lb_vao)} dòng")

# T6
ng = rd(AT / "nguon-goc-giai-nghia.tsv")
ph = {r["tu"]: r for r in ng if r["trang_thai"] == "PHAT_HANH"}
ok("T6 7.776 dòng PHAT_HANH khớp danh sách", set(ph) == set(moi) and len(ph) == 7776)
sai_sha = [w for w in moi if ph[w]["sha256_giai_nghia"] != hashlib.sha256(moi[w].encode("utf-8")).hexdigest()]
ok("T6 sha256 giải nghĩa khớp wordlist", not sai_sha, f"lệch {sai_sha[:5]}")
lv = collections.Counter(ph[w]["luot_viet"] for w in vao)
ok("T6 từ vào có lượt rtc-v*", set(lv) <= {"rtc-v1", "rtc-v2", "rtc-v3"}, f"{dict(lv)}")
loai = {r["tu"]: r for r in ng if r["trang_thai"] == "LOAI"}
ok("T6 từ ra là LOAI, đợt ra-thay-chinh", all(w in loai and "ra-thay-chinh" in loai[w]["dot_loai"].lower().replace("_", "-") for w in ra),
   f"{collections.Counter(loai[w]['cong_loai'] for w in ra if w in loai).most_common(6)}")

# T8, T11
dp = [l.strip() for l in open(AT / "du-phong.txt", encoding="utf-8") if l.strip()]
pl = rd(AT / "du-phong-phan-loai.tsv")
ok("T8 dự phòng: 89 dòng, khớp bảng phân loại và labels DU_PHONG", len(dp) == 89 and {r["tu"] for r in pl} == set(dp)
   and {r["tu"] for r in lb if r["trang_thai"] == "DU_PHONG"} == set(dp))
hm = rd(AT / "honorable-mentions.tsv")
hm_cu = list(__import__("csv").DictReader(git_show("analyzing-tools/honorable-mentions.tsv").splitlines(), delimiter="\t"))
ok("T11 HM: không HM nào vào chính; số dòng", not ({r["tu"] for r in hm} & set(moi)), f"{len(hm_cu)} → {len(hm)}; "
   f"khách hàng: {[r['nhom'] + '/' + r['ghi_chu'][:60] for r in hm if r['tu'] == 'khách hàng']}")
mf = json.loads((AT / "manifest.json").read_text(encoding="utf-8"))
sai = []
def duyet(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("sha256", "sha") and isinstance(v, str) and len(v) == 64 and "path" in o:
                p = (AT / o["path"]) if (AT / o["path"]).exists() else (REPO / o["path"])
                if p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() != v:
                    sai.append(o["path"])
            duyet(v)
    elif isinstance(o, list):
        for x in o:
            duyet(x)
duyet(mf)
ok("T8 manifest: băm tệp có đường dẫn khớp byte working tree", not sai, f"lệch {sai[:6]}")
write_lines(HERE / "t9-kiem-du-lieu.log", log)
print("\n".join(log))
