"""T9 (kế hoạch mục 13): soát toàn tập sau khi thay — cách đọc cùng khóa của 7.776 từ phát hành (working tree).

Nguồn cách đọc (chỉ đọc): DOC_KHAC của U/opus-counts.tsv; bốn danh sách HND (bản tạm ngoài repo, HND_DIR); đầu mục
tiếng Việt (lang_code vi) của Kaikki bản ghim (KAIKKI, ngoài repo). Không lưu danh sách HND hay lời Wiktionary: tệp ra chỉ có các cặp cần xét.

Nguồn phán quyết đã có: sàng lọc vòng 1 của Opus (../sang-loc-h7.tsv) và Astra (h7-sang-loc-1177.tsv, -bo-sung.tsv),
U/ra-thay-chinh-h7.tsv (phán quyết theo khóa), U/canh-bao-khong-dau.tsv, U/chu-ky.tsv, cờ từ vào (de-xuat-thay-v2.tsv)
và phán quyết T9 của Opus ở bảng T9 dưới đây.

Cờ đỏ của một cách đọc: LEX (từ/cụm tự hại, bạo lực, tình dục, chất thải; như sang-loc-h7.py), K2_SINGLE (một âm tiết
thuộc nhóm đỏ), nhãn Kaikki vulgar/offensive/derogatory, hoặc lời Kaikki có từ khóa đỏ (chỉ đọc trong bộ nhớ).
Còi tần suất: DOC_KHAC có PPM gộp ≥ 0,3 hoặc ≥ PPM của từ chính.

Chạy (từ thư mục evidence):
    set HND_DIR=...  &  set KAIKKI=...\\vi.jsonl.gz
    python -X utf8 -B t9-soat.py  ->  t9-soat.tsv, t9-soat.log
"""
import collections
import gzip
import importlib.util
import json
import os
import re
import subprocess
import unicodedata
from pathlib import Path

from chung import AT, HERE, OUT, U, HND_DIR, key, out_utf8, rd, sha_file, write_lines, write_tsv

out_utf8()
A = AT / "ho-so" / "astra" / "ra-thay-chinh"
KAIKKI = Path(os.environ["KAIKKI"])


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


sl = load("sl", HERE / "sang-loc-h7.py")
nfc = lambda s: unicodedata.normalize("NFC", s.strip()).lower()

# Danh sách phát hành (working tree) và từ vào (so với HEAD).
moi = [l.rstrip("\n").split("|", 1)[0] for l in open(AT / "wordlist.txt", encoding="utf-8")]
cu = {l.split("|", 1)[0] for l in subprocess.run(["git", "show", "HEAD:analyzing-tools/wordlist.txt"], cwd=AT.parent,
                                                  capture_output=True, check=True).stdout.decode("utf-8").splitlines()}
vao = set(moi) - cu
assert len(moi) == 7776 and len({key(w) for w in moi}) == 7776 and len(vao) == 116
kmoi = {key(w): w for w in moi}

# Cách đọc cùng khóa.
oc = rd(U / "opus-counts.tsv")
ppm_tu = {r["tu"]: sl.ppm(r) for r in oc if r["vai_tro"] == "UNG_VIEN"}
doc = collections.defaultdict(dict)  # khoa -> {cách đọc: {nguồn, ppm}}
for r in oc:
    if r["vai_tro"] == "DOC_KHAC" and r["khoa"] in kmoi:
        doc[r["khoa"]].setdefault(nfc(r["tu"]), {"nguon": set(), "ppm": None})
        doc[r["khoa"]][nfc(r["tu"])]["nguon"].add("DOC_KHAC")
        doc[r["khoa"]][nfc(r["tu"])]["ppm"] = sl.ppm(r)
for ten in ("Viet11K", "Viet22K", "Viet39K", "Viet74K"):
    for l in (HND_DIR / f"{ten}.txt").read_text(encoding="utf-8").splitlines():
        w = nfc(l)
        if w and key(w) in kmoi:
            doc[key(w)].setdefault(w, {"nguon": set(), "ppm": None})["nguon"].add("HND")
KW = ("tục", "chửi", "giao cấu", "giao hợp", "làm tình", "dương vật", "âm hộ", "âm đạo", "tinh dịch", "mại dâm", "đĩ",
      "cứt", "nước tiểu", "chất thải", "đại tiện", "tiểu tiện", "giết", "tự tử", "tự sát", "thắt cổ", "treo cổ", "vũ khí",
      "súng", "chém", "đâm chết", "xác chết", "thi thể", "ma túy", "cờ bạc", "khiêu dâm", "dâm", "miệt thị", "lăng mạ")
KWP = re.compile(r"(^|[^\w])(" + "|".join(map(re.escape, KW)) + r")([^\w]|$)")
kk_do = collections.defaultdict(set)  # cách đọc -> lý do đỏ theo Kaikki (chỉ nhãn hay từ khóa, không lưu lời)
with gzip.open(KAIKKI, "rt", encoding="utf-8") as f:
    for l in f:
        j = json.loads(l)
        if j.get("lang_code") != "vi":  # bản trích viwiktionary có cả mục tiếng Anh, Pháp...; chỉ lấy mục tiếng Việt
            continue
        w = nfc(j.get("word", ""))
        if not w or key(w) not in kmoi:
            continue
        doc[key(w)].setdefault(w, {"nguon": set(), "ppm": None})["nguon"].add("KAIKKI")
        for s in j.get("senses", []):
            tg = {t for t in s.get("tags", []) if t in ("vulgar", "offensive", "derogatory")}
            if tg:
                kk_do[w].add("nhãn " + "/".join(sorted(tg)))
            for g in s.get("glosses", []):
                m = KWP.search(g.lower())
                if m:
                    kk_do[w].add("từ khóa " + m.group(2))

# Bộ Kaikki thứ hai: mục tiếng Việt của enwiktionary (bản ghim 186cd0…, KAIKKI_EN, ngoài repo); lời tiếng Anh.
KWE = re.compile(r"\b(vulgar|penis|vagina|vulva|testic\w*|sex\w*|intercourse|fuck\w*|prostitut\w*|whore|slut|brothel|"
                 r"fec\w*|faec\w*|excrement|shit\w*|urin\w*|defecat\w*|fart\w*|kill\w*|murder\w*|suicid\w*|corpse|"
                 r"funeral|coffin|bribe\w*|gambl\w*|opium|heroin|curse\w*|swear\w*|insult\w*|rape\w*|tortur\w*|"
                 r"execut\w*|weapon\w*|gun|bomb\w*|prison\w*|jail\w*|crim\w*)\b")
KAIKKI_EN = Path(os.environ["KAIKKI_EN"]) if os.environ.get("KAIKKI_EN") else None
if KAIKKI_EN:
    with open(KAIKKI_EN, encoding="utf-8") as f:
        for l in f:
            j = json.loads(l)
            if j.get("lang_code") != "vi":
                continue
            w = nfc(j.get("word", ""))
            if not w or key(w) not in kmoi:
                continue
            doc[key(w)].setdefault(w, {"nguon": set(), "ppm": None})["nguon"].add("KAIKKI_EN")
            for s in j.get("senses", []):
                tg = {t for t in s.get("tags", []) if t in ("vulgar", "offensive", "derogatory", "pejorative", "slur")}
                if tg:
                    kk_do[w].add("nhãn en " + "/".join(sorted(tg)))
                for g in s.get("glosses", []):
                    m = KWE.search(g.lower())
                    if m:
                        kk_do[w].add("từ khóa en " + m.group(1))

# Phán quyết đã có.
xet = collections.defaultdict(set)  # (từ chính, cách đọc) -> nguồn
for r in rd(OUT / "sang-loc-h7.tsv"):
    xet[(r["tu_chinh"], nfc(r["doc_khac"]))].add("SL_OPUS:" + r["de_xuat"])
for f in ("h7-sang-loc-1177.tsv", "h7-sang-loc-bo-sung.tsv"):
    for r in rd(A / f):
        xet[(r["tu_chinh"], nfc(r["doc_khac"]))].add("SL_ASTRA:" + r["muc_K_de_xuat"])
for r in rd(U / "canh-bao-khong-dau.tsv"):
    xet[(r["ung_vien"], nfc(r["doc_khac"]))].add("CANH_BAO:" + r["trang_thai_9_1"])
h7 = {r["khoa"]: r["trang_thai"] for r in rd(U / "ra-thay-chinh-h7.tsv")}
ck = collections.Counter(r["khoa"] for r in rd(U / "chu-ky.tsv") if r["loai_ky"] == "K2" and r["hieu_luc"] == "CO")
co_vao = {r["tu"]: r["can_doc"] for r in rd(HERE / "de-xuat-thay-v2.tsv", mine=True) if r["vai_tro"] != "RA"}

# Phán quyết T9 của Opus cho cặp chưa có phán quyết mà có cờ đỏ hay còi (điền sau khi đọc; xem t9-soat-toan-tap.md).
T9 = {}
T9_FILE = HERE / "t9-phan-quyet.tsv"
if T9_FILE.exists():
    T9 = {(r["tu"], r["doc_khac"]): (r["phan_quyet"], r["ly_do"]) for r in rd(T9_FILE, mine=True)}

rows, dem = [], collections.Counter()
for k, w in kmoi.items():
    for x, v in sorted(doc[k].items()):
        if x == w:
            continue
        dem["cặp"] += 1
        do = []
        if sl.PAT.search(x) or x in sl.K2_SINGLE:
            do.append("LEX")
        if x in kk_do:
            do.append("KAIKKI(" + "; ".join(sorted(kk_do[x])) + ")")
        p = v["ppm"]
        coi = p is not None and (p >= 0.3 or p >= ppm_tu.get(w, 0))
        nguon_xet = sorted(xet.get((w, x), set()))
        if k in h7:
            nguon_xet.append("H7_RTC:" + h7[k])
        if ck[k]:
            nguon_xet.append(f"CHU_KY_K2:{ck[k]}")
        if w in vao and co_vao.get(w):
            nguon_xet.append("CO_VAO")
        can = bool(do) or coi or w in vao or (w, x) in T9
        if not can:
            continue
        pq = T9.get((w, x))
        dem["cần xét"] += 1
        dem["từ vào" if w in vao else "từ giữ"] += 1
        if nguon_xet:
            dem["đã có phán quyết"] += 1
        elif pq:
            dem["T9 Opus"] += 1
        else:
            dem["CHƯA XÉT"] += 1
        rows.append({"tu": w, "khoa": k, "tu_vao": "Y" if w in vao else "-", "doc_khac": x,
                     "nguon_doc": "+".join(sorted(v["nguon"])), "ppm_doc": f"{p:.3f}" if p is not None else "-",
                     "ppm_tu": f"{ppm_tu[w]:.3f}" if w in ppm_tu else "-", "coi": "Y" if coi else "-",
                     "co_do": " ".join(do) or "-", "da_xet": " ".join(nguon_xet) or "-",
                     "phan_quyet_t9": pq[0] if pq else "-", "ly_do_t9": pq[1] if pq else "-"})
write_tsv(HERE / "t9-soat.tsv", list(rows[0].keys()), rows)
log = [f"danh sách phát hành: 7.776 từ, 7.776 khóa; từ vào {len(vao)}; Kaikki sha256 {sha_file(KAIKKI)[:12]}",
       "đếm: " + ", ".join(f"{a} {b}" for a, b in dem.items())]
write_lines(HERE / "t9-soat.log", log)
print("\n".join(log))
