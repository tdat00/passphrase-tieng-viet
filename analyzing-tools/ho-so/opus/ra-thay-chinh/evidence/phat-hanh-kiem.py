"""Kiểm cuối gói phát hành bản 2 (working tree, trước commit): kết quả T9 và quyết định D-rtc-10, D-rtc-11 đã áp đúng.

Chỉ đọc. In ĐẠT/LỖI từng phép kiểm; ghi phat-hanh-kiem.log.
Chạy (từ thư mục evidence): python -X utf8 -B phat-hanh-kiem.py
"""
import collections
import csv
import hashlib
import io
import json
import re
import subprocess

from chung import AT, HERE, OUT, U, key, out_utf8, rd, write_lines

out_utf8()
REPO = AT.parent
log = []


def ok(ten, dk, ct=""):
    log.append(f"{'ĐẠT' if dk else 'LỖI'} {ten}" + (f": {ct}" if ct else ""))


def head(path):
    return subprocess.run(["git", "show", f"HEAD:{path}"], cwd=REPO, capture_output=True, check=True).stdout.decode("utf-8")


def rd_head(path):
    return list(csv.DictReader(io.StringIO(head(path)), delimiter="\t", quoting=csv.QUOTE_NONE))


moi = dict(l.rstrip("\n").split("|", 1) for l in open(AT / "wordlist.txt", encoding="utf-8"))
cu = {l.split("|", 1)[0] for l in head("analyzing-tools/wordlist.txt").splitlines()}
tt = rd(U / "ra-thay-chinh-thay-the.tsv")
RA0 = {r["tu"] for r in tt if r["vai_tro"] == "RA"}
VAO0 = {r["tu"] for r in tt if r["vai_tro"] == "VAO"}
ra, vao = cu - set(moi), set(moi) - cu
ra_mong = RA0 | {"phết", "cau có", "tụ tập"}
vao_mong = (VAO0 - {"sớm tối", "buồn thiu", "ỉu xìu"}) | {"cả nghĩ", "cửu chương", "ngân hàng", "biển", "côn trùng", "cô giáo"}
ok("Danh sách: 7.776 từ, 7.776 khóa, khóa ≥ 4 chữ", len(moi) == 7776 and len({key(w) for w in moi}) == 7776
   and min(len(key(w)) for w in moi) >= 4)
ok("Ra 119 = 116 + phết, cau có, tụ tập", ra == ra_mong and len(ra) == 119, f"thừa {sorted(ra - ra_mong)}, thiếu {sorted(ra_mong - ra)}")
ok("Vào 119 = 115 VAO − buồn thiu, ỉu xìu + cả nghĩ, cửu chương + 4 HM", vao == vao_mong and len(vao) == 119,
   f"thừa {sorted(vao - vao_mong)}, thiếu {sorted(vao_mong - vao)}")

# Khóa chặn
bk = rd(AT / "blocked_keys.tsv")
bk_cu = {r["khoa"] for r in rd_head("analyzing-tools/blocked_keys.tsv")}
moi_bk = {r["khoa"]: r["ma"] for r in bk if r["khoa"] not in bk_cu}
h7 = rd(U / "ra-thay-chinh-h7.tsv")
mong = {r["khoa"]: ("K0" if "K0" in (r["opus"], r["astra"]) else "K1") for r in h7 if "THAY" in r["trang_thai"]}
mong.update({"baotu": "K1", "lamco": "K1", "phet": "K0", "cauco": "K1", "tutap": "K1"})
ok("Khóa chặn: +97 đúng khóa và mã (gồm phet K0, cauco K1, tutap K1)", moi_bk == mong,
   f"{len(moi_bk)} mới; lệch {[(k, moi_bk.get(k), mong.get(k)) for k in set(moi_bk) | set(mong) if moi_bk.get(k) != mong.get(k)][:6]}")
ok("Không từ phát hành nào có khóa bị chặn", not ({key(w) for w in moi} & {r["khoa"] for r in bk}))

# Họ chính tả
sf = rd(AT / "spelling_families.tsv")
sf_cu = rd_head("analyzing-tools/spelling_families.tsv")
them = [r for r in sf if (r["chuan"], r["bien_the"]) not in {(x["chuan"], x["bien_the"]) for x in sf_cu}]
hai = {(r["chuan"], r["bien_the"]): r["ket_luan"] for r in them if r["chuan"] in ("buồn thiu", "ỉu xìu")}
ok("Họ: +37, gồm buồn thiu/buồn thỉu và ỉu xìu/ỉu xịu loại c thiếu dữ liệu", len(them) == 37
   and hai == {("buồn thiu", "buồn thỉu"): "LOAI_THIEU_DU_LIEU", ("ỉu xìu", "ỉu xịu"): "LOAI_THIEU_DU_LIEU"}, f"{len(them)}; {hai}")
cam = []
for r in sf:
    ws = [x.strip() for x in r["chuan"].split(" / ") + r["bien_the"].split(" / ") if x.strip() in moi]
    if ws and (r["ket_luan"].startswith("LOAI") or r["ket_luan"] in ("CHO_LOAI", "CHO_NGHIA", "CHO_SAT_NGUONG")):
        cam.append(f"{r['chuan']}/{r['bien_the']}")
ok("Không từ phát hành nào thuộc họ bị cấm (C5)", not cam, f"{cam[:5]}")

# Chữ ký: mọi khóa K2 của từ phát hành có đúng một dòng hiệu lực mỗi SA
ck = rd(U / "chu-ky.tsv")
hl = collections.defaultdict(collections.Counter)  # theo (khóa, mặt chữ): một khóa có thể có dòng của mặt chữ cũ không phát hành
for r in ck:
    if r["loai_ky"] == "K2" and r["hieu_luc"] == "CO":
        hl[(r["khoa"], r["tu"])][r["nguoi_ky"]] += 1
k2_phat = [(k, w) for k, w in hl if w in moi]
sai = [kw for kw in k2_phat if dict(hl[kw]) != {"Astra": 1, "Opus": 1}]
ok("Mọi từ phát hành có K2: đúng một dòng hiệu lực của Astra và một của Opus", not sai,
   f"{len(k2_phat)} từ; sai {[(kw, dict(hl[kw])) for kw in sai[:6]]}")
t9k = ["duoi", "tute", "cuong", "long", "chanh", "thudu", "tung", "manman", "banthan", "daihan", "lieu", "donda", "songngu",
       "bang", "thoi", "nghe", "thuong", "tantinh", "tuot"]
t9w = {key(w): w for w in moi}
thieu = [k for k in t9k if dict(hl[(k, t9w[k])]) != {"Astra": 1, "Opus": 1}]
ok("Khóa T9 tiêu biểu có hai chữ ký ", not thieu, f"{thieu}")
bang = [r for r in ck if r["khoa"] == "bang" and r["loai_ky"] == "K2" and r["hieu_luc"] == "CO"]
ok("Chữ ký bảng có phạm vi băng", all("băng" in r["ly_do"] for r in bang), f"{len(bang)} dòng")

# Nhãn
lb = rd(AT / "labels.tsv")
lbc = {r["tu"]: r for r in lb if r["trang_thai"] == "CHINH"}
ok("labels: 7.776 CHINH khớp danh sách, F = 77, R1 = 0", set(lbc) == set(moi) and sum(r["lop"] == "F" for r in lbc.values()) == 77
   and not any(r["nhan"] == "R1" for r in lbc.values()))
xh = {r["tu"]: r for r in rd(U / "xep-hang.tsv")}
hm4 = ["ngân hàng", "biển", "côn trùng", "cô giáo"]
ok("labels: 4 HM vào có dòng CHINH, nhãn OK, điểm theo xep-hang.tsv",
   all(w in lbc and lbc[w]["nhan"] == "OK" and abs(float(lbc[w]["diem"]) - float(xh[w]["diem"])) < 1e-6 for w in hm4))
thieu_k2 = [w for w in moi if dict(hl[key(w)]) == {"Astra": 1, "Opus": 1} and "K2" not in lbc[w]["chu_ky_hai_ben"]]
ok("labels: từ có K2 hai chữ ký đều mang K2 ở chu_ky_hai_ben", not thieu_k2, f"{thieu_k2[:6]}")
dpl = {r["tu"]: r for r in lb if r["trang_thai"] == "DU_PHONG"}

# D8
ng = rd(AT / "nguon-goc-giai-nghia.tsv")
ph = {r["tu"]: r for r in ng if r["trang_thai"] == "PHAT_HANH"}
lo = [r for r in ng if r["trang_thai"] == "LOAI"]
ok("D8: 7.776 PHAT_HANH khớp danh sách và sha256 câu; 297 LOAI", set(ph) == set(moi) and len(lo) == 297
   and all(ph[w]["sha256_giai_nghia"] == hashlib.sha256(moi[w].encode("utf-8")).hexdigest() for w in moi), f"LOAI {len(lo)}")
ok("D8: từ vào có lượt rtc-v*, D6 PASS", all(ph[w]["luot_viet"].startswith("rtc-v") and ph[w]["d6_ket_qua"] == "PASS" for w in vao),
   f"{collections.Counter(ph[w]['luot_viet'] for w in vao)}")
lom = {r["tu"]: r for r in lo}
ok("D8: 119 từ ra là LOAI", all(w in lom for w in ra), f"{collections.Counter(lom[w]['cong_loai'] for w in ra if w in lom).most_common(6)}")

# Dự phòng, HM
dp = [l.strip() for l in open(AT / "du-phong.txt", encoding="utf-8") if l.strip()]
pl = {r["tu"]: r for r in rd(AT / "du-phong-phan-loai.tsv")}
ok("Dự phòng: 90 từ (thêm buồn thiu, ỉu xìu tầng D; bớt cửu chương), khớp phân loại và labels", len(dp) == 90 and set(dp) == set(pl)
   == set(dpl) and pl["buồn thiu"]["tang"] == "D" and pl["ỉu xìu"]["tang"] == "D" and "cửu chương" not in dp,
   f"{len(dp)}; tầng {collections.Counter(r['tang'] for r in pl.values())}")
hm = rd(AT / "honorable-mentions.tsv")
ok("HM: bỏ 4 HM đã vào, không HM nào ở danh sách chính", not ({r["tu"] for r in hm} & set(moi)) and len(hm) == 233, f"{len(hm)} dòng")

# Không phát hành từ còn phản đối: mọi dòng T9 của hai SA
for ten, f, cot_tu in (("Opus", OUT / "t9-doi-dap.tsv", "tu_chinh"), ("Astra", AT / "ho-so" / "astra" / "ra-thay-chinh" / "t9-doi-dap.tsv", None)):
    if not f.exists():
        ok(f"Phiếu T9 đối đáp của {ten} có mặt", False)
        continue
    rr = rd(f)
    c_tu = cot_tu or next(c for c in rr[0] if c in ("tu_chinh", "tu"))
    cot_de = next(c for c in rr[0] if c.startswith("de_xuat"))
    con = [r[c_tu] for r in rr if r[c_tu] in moi and re.search(r"THAY(?!_THE)|K0|K1|LOAI|TRANH", r[cot_de])
           and not re.search(r"KHAC_TU|^K2|GIU", r[cot_de])
           and not (ten == "Opus" and r[cot_de].startswith("TRANH") and r[c_tu] == "tử tế")]  # tử tế: Astra chuyển K2, T-rtc-24
    ok(f"Không từ phát hành nào bị phiếu T9 của {ten} đề xuất thay, K0, K1, loại", not con, f"{con[:6]}")

# Manifest
mf = json.loads((AT / "manifest.json").read_text(encoding="utf-8"))
lech = []


def duyet(o):
    if isinstance(o, dict):
        p = o.get("path") or o.get("tep")
        for k in ("sha256", "sha256_lf"):
            v = o.get(k)
            if isinstance(v, str) and len(v) == 64 and isinstance(p, str):
                f = AT / p if (AT / p).exists() else REPO / p
                if f.exists():
                    b = f.read_bytes()
                    if v not in (hashlib.sha256(b).hexdigest(), hashlib.sha256(b.replace(b"\r\n", b"\n")).hexdigest()):
                        lech.append(p)
        for v in o.values():
            duyet(v)
    elif isinstance(o, list):
        for v in o:
            duyet(v)


duyet(mf)
ok("manifest: băm khớp byte (CRLF hoặc LF) của working tree", not lech, f"lệch {lech[:6]}")

# Tài liệu
w = (REPO / "WordListAnalyze.md").read_text(encoding="utf-8")
ok("WordListAnalyze.md: có D-rtc-10, D-rtc-11, T-rtc-24, 119 từ ra", all(s in w for s in ("D-rtc-10", "D-rtc-11", "T-rtc-24")) and "119" in w)
ok("WordListAnalyze.md: mô tả K0 đủ ba loại nghĩa", re.search(r"K0[^\n]{0,200}tình dục người lớn[^\n]{0,60}chất thải", w) is not None)

# Không có văn bản kho, HND, Kaikki: dò các chuỗi lời Kaikki/HND đã đọc trong lượt T9 trong toàn bộ tệp thay đổi
diff = subprocess.run(["git", "diff", "HEAD", "--name-only"], cwd=REPO, capture_output=True, check=True).stdout.decode().split()
moi_tep = subprocess.run(["git", "ls-files", "--others", "--exclude-standard"], cwd=REPO, capture_output=True, check=True).stdout.decode().split()
MAU = ["Đọc lái đĩ", "Thải ra chất bẩn", "eye dialect spelling", "Cách gọi khác của trò chơi bài cào", "Dùng làm tiếng chửi thề",
       "Như buồn thiu", "Như ỉu xìu", "Dài lòng thòng rất vướng", "Nhảy lên, ngồi lên", "Thông thạo (thô tục)"]
dinh = []
for p in diff + moi_tep:
    f = REPO / p
    if f.is_file() and f.name != "phat-hanh-kiem.py" and f.suffix in (".md", ".tsv", ".txt", ".json", ".py", ".html", ".log"):
        s = f.read_text(encoding="utf-8", errors="replace")
        dinh += [f"{p}:{m}" for m in MAU if m in s]
lon = [p for p in moi_tep if (REPO / p).is_file() and (REPO / p).stat().st_size > 2_000_000 and "d6-log" not in p]
ok("Không chép lời Kaikki đã đọc vào tệp thay đổi; không tệp mới lớn bất thường", not dinh and not lon, f"{dinh[:4]} {lon[:4]}")
write_lines(HERE / "phat-hanh-kiem.log", log)
print("\n".join(log))
