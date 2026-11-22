"""T9: đếm các cách đọc chỉ có ở Kaikki (vi, en) cùng từ chính của chúng trên hai kho đã ghim, để quyết còi H7.

Cách đếm như count_corpus.py: hạ chữ thường, NFC, cắt đoạn tại dấu câu, đếm n-gram âm tiết liền nhau trong đoạn;
kho web bỏ dòng trùng (ở đây so băm 8 byte của dòng để đỡ bộ nhớ). Mẫu số là số âm tiết đã ghi ở manifest.json.
Chỉ ghi số đếm, không ghi câu nào của kho.

Chạy (từ thư mục evidence):
    set KHO_SUB=...\\os-vi.txt.gz  &  set KHO_WEB=...\\cc-vi.txt.gz   (bản ghim, ngoài repo)
    python -X utf8 -B t9-dem.py  ->  t9-dem.tsv
"""
import gzip
import hashlib
import os
import re
import unicodedata
from collections import Counter

from chung import HERE, SUB_TOKENS, WEB_TOKENS, out_utf8, sha_file, write_tsv

out_utf8()
CAP = [  # (từ chính, cách đọc) cần số để quyết còi; nhóm H6 của cách đọc theo phán đoán của Opus
    ("linh dương", "linh đường", "G4"), ("chứng chỉ", "chung chi", "G2"), ("sành ăn", "sân hận", "G9"),
    ("mũ nồi", "mụ nội", "G9"), ("tụ tập", "tu tập", "G4"), ("song ngữ", "song ngư", "G4"), ("tử tế", "tư tế", "G4"),
    ("tử tế", "tứ tế", "G4"), ("chanh", "chảnh", "G9"), ("liệng", "liêng", "G7"), ("bổ dưỡng", "bố đường", "G6"),
    ("đuôi", "đượi", "K0?"), ("thú dữ", "thứ dữ", "G1"), ("tung", "tửng", "G5"), ("mằn mặn", "man man", "G5"),
    ("đon đả", "đòn đá", "G1"), ("bạn thân", "bán thần", "G4"), ("thiện chí", "thiền chỉ", "G4"),
    ("thành quả", "thánh quả", "G4"), ("cau có", "cầu cơ", "G4"), ("công cộng", "công công", "G3"),
    ("hướng dương", "hưởng dương", "G4"), ("nhân tài", "nhân tai", "G8"), ("đá tảng", "đa tạng", "G5"),
    ("mã số", "ma sơ", "G4"), ("dài hạn", "đại hãn", "G3"), ("chốt", "chớt", "G4"), ("băng đô", "bang đỏ", "G3"),
    ("liễu", "liêu", "G3"), ("nhà ăn", "nhà ân", "G3"), ("riêu", "riệu", "G7"), ("bình dị", "binh di", "G1"),
    ("quần bò", "quân bộ", "G1"), ("tiến bộ", "tiền bộ", "G1"), ("cãi cọ", "cai cò", "G2"), ("bồi bàn", "bôi bàn", "G7"),
    ("hóng chuyện", "hồng chuyên", "G3"), ("nhìn", "nhĩn", "G6?"),
]
SEG = re.compile(r"[^\w\s]+|_+")
targets = {tuple(w.split(" ")) for a, b, _ in CAP for w in (a, b)}
sizes = sorted({len(t) for t in targets})


def dem(path, dedup):
    c, total, seen = Counter(), 0, set()
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = unicodedata.normalize("NFC", line.strip().lower())
            if dedup:
                h = hashlib.blake2b(line.encode("utf-8"), digest_size=8).digest()
                if h in seen:
                    continue
                seen.add(h)
            for seg in SEG.split(line):
                toks = seg.split()
                total += len(toks)
                for n in sizes:
                    for i in range(len(toks) - n + 1):
                        g = tuple(toks[i:i + n])
                        if g in targets:
                            c[g] += 1
    return c, total


sub, ts = dem(os.environ["KHO_SUB"], False)
web, tw = dem(os.environ["KHO_WEB"], True)
ppm = lambda w: (sub[tuple(w.split(" "))] / SUB_TOKENS + web[tuple(w.split(" "))] / WEB_TOKENS) * 1e6 / 2
rows = []
for a, b, g in CAP:
    rows.append({"tu_chinh": a, "doc_khac": b, "nhom": g, "sub_tu": sub[tuple(a.split(" "))], "web_tu": web[tuple(a.split(" "))],
                 "sub_doc": sub[tuple(b.split(" "))], "web_doc": web[tuple(b.split(" "))],
                 "ppm_tu": f"{ppm(a):.4f}", "ppm_doc": f"{ppm(b):.4f}",
                 "ti_le": f"{ppm(b) / ppm(a):.4f}" if ppm(a) else "-",
                 "coi": "Y" if ppm(b) >= 0.3 or (ppm(b) > 0 and ppm(b) >= ppm(a)) else "-"})
write_tsv(HERE / "t9-dem.tsv", list(rows[0].keys()), rows)
print(f"âm tiết đếm được: phụ đề {ts} (manifest {SUB_TOKENS}), web bỏ trùng {tw} (manifest {WEB_TOKENS})")
print("còi:", [(r["tu_chinh"], r["doc_khac"], r["ppm_doc"], r["ti_le"]) for r in rows if r["coi"] == "Y"])
