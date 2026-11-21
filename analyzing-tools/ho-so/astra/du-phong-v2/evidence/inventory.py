"""Đo hồ sơ có sẵn; chỉ ghi số đếm, nhãn, hash và tham chiếu trong thư mục SA-Astra."""
import csv
import hashlib
import json
import re
import subprocess
import sys
import unicodedata as U
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent.parent
EV = OUT / "evidence"
TOOLS = ROOT / "analyzing-tools"
UNIFIED = TOOLS / "ho-so" / "unified"
INPUTS = {}
ALPHA = "aăâbcdđeêghiklmnoôơpqrstuưvxy"
TONES = "\u0300\u0309\u0303\u0301\u0323"
LETTERS = set(ALPHA) | {
    U.normalize("NFC", v + t) for v in "aăâeêioôơuưy" for t in TONES
}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def key(w):
    return "".join(c for c in U.normalize("NFD", w.lower())
                   if not U.category(c).startswith("M")).replace("đ", "d").replace(" ", "")


def o1(w):
    result = []
    for syllable in w.split(" "):
        de = U.normalize("NFD", syllable)
        tone = [1 + TONES.index(c) for c in de if c in TONES]
        base = U.normalize("NFC", "".join(c for c in de if c not in TONES))
        result.append((tuple(ALPHA.index(c) for c in base), tone[0] if tone else 0))
    return tuple(result)


def read(path):
    raw = path.read_bytes()
    INPUTS[str(path.relative_to(ROOT))] = {
        "sha256_bytes": sha(raw),
        "sha256_LF": sha(raw.replace(b"\r\n", b"\n")),
        "bytes": len(raw), "lines": raw.count(b"\n"),
        "CRLF": raw.count(b"\r\n"), "BOM": raw.startswith(b"\xef\xbb\xbf"),
    }
    return raw.decode("utf-8").replace("\r\n", "\n")


def tsv(path):
    result = []
    for line, row in enumerate(csv.DictReader(read(path).splitlines(),
                                            delimiter="\t", quoting=csv.QUOTE_NONE), 2):
        row["_ref"] = f"{path.relative_to(ROOT)}:{line}"
        result.append(row)
    return result


def save_tsv(path, fields, rows):
    assert OUT in path.resolve().parents
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t",
                                lineterminator="\r\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows({f: ("-" if r.get(f) in (None, "") else r[f]) for f in fields}
                         for r in rows)


def save_json(path, data):
    assert OUT in path.resolve().parents
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8", newline="\r\n")


def load():
    d = {}
    d["main"] = [s.split("|", 1)[0] for s in read(TOOLS / "wordlist.txt").splitlines()]
    d["reserve"] = read(TOOLS / "du-phong.txt").splitlines()
    d["current_by_key"] = defaultdict(list)
    for word in d["main"] + d["reserve"]:
        d["current_by_key"][key(word)].append(word)
    for name in ("labels", "blocked_keys", "spelling_families", "nguon-goc-giai-nghia"):
        d[name] = tsv(TOOLS / f"{name}.tsv")
    d["blocked_by_key"] = {r["khoa"]: r for r in d["blocked_keys"]}
    d["spelling_by_word"] = defaultdict(list)
    for row in d["spelling_families"]:
        for word in {v.strip() for side in ("chuan", "bien_the") for v in row[side].split("/")}:
            d["spelling_by_word"][word].append(row)
    for name in ("xep-hang", "p6-dau-vao", "opus-counts", "chu-ky", "phan-bien",
                 "phieu-astra", "phieu-opus", "p6-khau-tru-cuoi", "p7-khau-tru",
                 "p7-khau-tru-v2", "p7-v3-khau-tru-132-theo-P0-astra",
                 "p7-v3-c13-hoa-astra-tu-chua-viet",
                 "p7-v4-kiem-ke-D8-chua-chot-astra", "l2d-ung-vien", "l3b-de-cu-opus"):
        d[name] = tsv(UNIFIED / f"{name}.tsv")
    d["rules"] = json.loads(read(UNIFIED / "tap-luat-P2-v4.json"))
    d["p1"] = tsv(TOOLS / "ho-so" / "discussion" / "bang-khoa-chung.tsv")
    d["by_word"] = {}
    cleaned = {r["tu"]: r for r in d["opus-counts"]}
    for row in d["p1"]:
        arrays = {f: json.loads(row[f]) for f in (
            "ung_vien", "nguon", "opensub_n", "ccaligned_n", "leipzig_so_cau",
            "tatoeba_so_cau", "nguon_tu_dien_so_bo")}
        for i, word in enumerate(arrays["ung_vien"]):
            c = cleaned.get(word, {})
            d["by_word"][word] = {
                "nguon_pool": "L1", "nguon_de_cu": arrays["nguon"][i],
                "h3_nguon": ";".join(arrays["nguon_tu_dien_so_bo"][i]),
                "sub_be_mat": arrays["opensub_n"][i],
                "web_be_mat": arrays["ccaligned_n"][i],
                "sub_sach": c.get("sub_sach", ""),
                "web_sach": c.get("web_sach", ""),
                "leipzig": arrays["leipzig_so_cau"][i],
                "tatoeba": arrays["tatoeba_so_cau"][i],
                "nguon_dong": row["_ref"],
                "dem_sach_dong": c.get("_ref", ""),
            }
    for short, pool in (("l2", "L2A"), ("l2b", "L2B"), ("l2c", "L2C"), ("l3", "L3")):
        d[f"{short}-ung-vien"] = tsv(UNIFIED / f"{short}-ung-vien.tsv")
        d[f"{short}-nhan"] = tsv(UNIFIED / f"{short}-nhan-sau-H9-opus.tsv")
        for row in d[f"{short}-ung-vien"]:
            d["by_word"][row["tu"]] = {
                "nguon_pool": pool, "nguon_de_cu": row["nguon_ung_vien"],
                "h3_nguon": row["nguon_tu_dien"],
                "sub_be_mat": row["opensub_n"], "web_be_mat": row["ccaligned_n"],
                "sub_sach": row["sub_sach"], "web_sach": row["web_sach"],
                "leipzig": row["leipzig_so_cau"], "tatoeba": row["tatoeba_so_cau"],
                "nguon_dong": row["_ref"], "dem_sach_dong": row["_ref"],
            }
    d["labels_by_word"] = {r["tu"]: r for r in d["labels"]}
    d["rank_by_word"] = {r["tu"]: r for r in d["xep-hang"]}
    d["p4_by_word"] = defaultdict(list)
    for name in ("phieu-astra", "phieu-opus"):
        for row in d[name]:
            d["p4_by_word"][row["tu"]].append(row)
    d["excluded"] = {r["tu"]: r for r in d["nguon-goc-giai-nghia"]
                     if r["trang_thai"] == "LOAI"}
    d["signatures"] = defaultdict(list)
    for r in d["chu-ky"]:
        d["signatures"][r["tu"]].append(r)
    d["d6"] = defaultdict(list)
    for version in ("v1", "v2", "v3", "v4-rieng"):
        for r in tsv(UNIFIED / f"d6-log-{version}.tsv"):
            r["_version"] = version
            d["d6"][r["tu"]].append(r)
    d["gloss"] = {}
    for r in tsv(UNIFIED / "p7-v4-du-phong-168-co-nghia-cho-duyet.tsv"):
        digest = sha(r["giai_nghia"].encode("utf-8"))
        norm = U.normalize("NFC", U.normalize("NFC", r["giai_nghia"]).lower())
        tokens = "".join(c if c.isalpha() else " " for c in norm).split()
        token_digest = sha(json.dumps(tokens, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8"))
        matched = [x for x in d["d6"][r["tu"]] if x["sha256_giai_nghia"] == token_digest]
        d["gloss"][r["tu"]] = {
            "gloss_sha256": digest, "gloss_ref": r["_ref"],
            "d6_token_sha256": token_digest,
            "d6_match_n": len(matched),
            "d6_version": ";".join(x["_version"] for x in matched),
            "d6_result": ";".join(x["ket_qua"] for x in matched),
            "d6_ref": ";".join(x["_ref"] for x in matched),
            "co": r["co"],
        }
    d["reviews"] = defaultdict(list)
    for filename in ("soat-nghia-astra.tsv", "soat-nghia-opus.tsv",
                     "soat-nghia-v2-astra.tsv", "soat-nghia-v2-opus.tsv",
                     "soat-nghia-v3-astra.tsv", "soat-nghia-v3-opus.tsv",
                     "soat-nghia-v3-opus-bo-sung.tsv"):
        for r in tsv(UNIFIED / filename):
            d["reviews"][r["tu"]].append(r)
    return d


def basic(word, data):
    k = key(word)
    parts = word.split(" ")
    collisions = [w for w in data["current_by_key"][k] if w != word]
    blocked = [data["blocked_by_key"][k]] if k in data["blocked_by_key"] else []
    spelling = data["spelling_by_word"][word]
    h5a = []
    for syl in parts:
        de = U.normalize("NFD", syl)
        base = U.normalize("NFC", "".join(c for c in de if c not in TONES))
        if any(c in TONES for c in de):
            for onset in ("ngh", "ch", "gh", "gi", "kh", "ng", "nh", "ph", "th", "tr",
                          "qu", "b", "c", "d", "đ", "g", "h", "k", "l", "m", "n",
                          "p", "r", "s", "t", "v", "x", ""):
                if base.startswith(onset) and base[len(onset):] in ("oa", "oe", "uy"):
                    h5a.append(syl)
    row = {
        "tu": word, "khoa": k, "so_chu": len(k), "so_khoi": len(parts),
        "h1": U.normalize("NFC", word) == word and all(p and set(p) <= LETTERS for p in parts),
        "h2_so_hoc": 4 <= len(k) <= 12 and 1 <= len(parts) <= 3,
        "trung_khoa": ";".join(collisions),
        "blocked": ";".join(x["ma"] for x in blocked),
        "h5a": ";".join(h5a),
        "h5_ho": ";".join(f"{r['chuan']}~{r['bien_the']}:{r['ket_luan']}" for r in spelling),
        "h5_ref": ";".join(r["_ref"] for r in spelling),
    }
    source = data["by_word"].get(word, {})
    row.update(source)
    label = data["labels_by_word"].get(word, data["rank_by_word"].get(word, {}))
    for field in ("nhan", "lop", "F", "G", "T", "diem"):
        row[field] = label.get(field, "")
    row["nhan_ref"] = label.get("_ref", "")
    rank = data["rank_by_word"].get(word, {})
    row["hang_lich_su"] = rank.get("hang", "")
    row["vao_lich_su"] = rank.get("vao", "")
    row["rank_ref"] = rank.get("_ref", "")
    row["chu_ky_tom_tat"] = label.get("chu_ky_hai_ben", "")
    signatures = data["signatures"][word]
    row["chu_ky_chi_tiet"] = ";".join(
        f"{r['loai_ky']}:{r['nguoi_ky']}:{r['hieu_luc']}" for r in signatures)
    row["chu_ky_ref"] = ";".join(r["_ref"] for r in signatures)
    for field in ("sub_be_mat", "web_be_mat", "sub_sach", "web_sach", "leipzig", "tatoeba"):
        if row.get(field, "") != "":
            row[field] = int(row[field])
    if source:
        strong = (row["sub_be_mat"] * 10_000_000 >= 34_314_528
                  or row["web_be_mat"] * 10_000_000 >= 149_860_716
                  or row["leipzig"] >= 2 or row["tatoeba"] >= 1)
        row["h8_so_hoc"] = "MANH" if strong else (
            "YEU" if any(row[k] for k in ("sub_be_mat", "web_be_mat", "leipzig", "tatoeba"))
            else "ZERO")
    row.update(data["gloss"].get(word, {}))
    removed = data["excluded"].get(word)
    row["loai_truoc"] = removed["cong_loai"] if removed else ""
    row["loai_ref"] = removed["_ref"] if removed else ""
    row["p4_ref"] = ";".join(r["_ref"] for r in data["p4_by_word"][word])
    return row


def main():
    EV.mkdir(parents=True, exist_ok=True)
    data = load()
    reserve_rows = [basic(w, data) for w in data["reserve"]]
    current = set(data["main"] + data["reserve"])
    candidates = [basic(r["tu"], data) for r in data["xep-hang"] if r["tu"] not in current]
    fields = list(dict.fromkeys(k for r in reserve_rows + candidates for k in r))
    save_tsv(EV / "reserve-probe.tsv", fields, reserve_rows)
    save_tsv(EV / "candidate-probe.tsv", fields, candidates)
    sections = (ROOT / "WordListAnalyze.md").read_bytes()
    s10 = sections[sections.index("## 10. Danh sách 7.776 từ phát hành".encode()):
                   sections.index("## 11. Danh sách dự phòng".encode())]
    protected = {name: sha((ROOT / name).read_bytes()) for name in
                 ("index.html", "thong-tin.html", r"analyzing-tools\wordlist.txt")}
    protected["WordListAnalyze.md section10 bytes"] = sha(s10)
    if (EV / "inventory.json").exists():
        initial = json.loads((EV / "inventory.json").read_text(encoding="utf-8"))
        assert protected == initial["protected_bytes"], "Vùng được bảo vệ đã đổi so với lần đo đầu"
    reserve_set = set(data["reserve"])
    summary = {
        "base_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "branch": subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip(),
        "main_n": len(data["main"]), "reserve_n": len(data["reserve"]),
        "main_classes": dict(Counter(data["labels_by_word"][w]["lop"] for w in data["main"])),
        "reserve_classes": dict(Counter(r["lop"] for r in reserve_rows)),
        "reserve_labels": dict(Counter(r["nhan"] for r in reserve_rows)),
        "reserve_gloss_n": len(data["gloss"]),
        "reserve_gloss_matches": dict(Counter(r.get("d6_result", "CHUA_VIET") for r in reserve_rows)),
        "reserve_h8": dict(Counter(r["h8_so_hoc"] for r in reserve_rows)),
        "reserve_flags": {field: [r["tu"] for r in reserve_rows if r.get(field)]
                          for field in ("trung_khoa", "blocked", "h5a", "h5_ho")},
        "reserve_gloss_by_class": dict(Counter(r["lop"] for r in reserve_rows if r.get("gloss_sha256"))),
        "reserve_no_gloss_by_class": dict(Counter(r["lop"] for r in reserve_rows if not r.get("gloss_sha256"))),
        "reserve_signed_types": dict(Counter(s for r in reserve_rows
                                          for s in r["chu_ky_tom_tat"].split(";") if s)),
        "reserve_d8_rows": sum(r["tu"] in reserve_set for r in data["nguon-goc-giai-nghia"]),
        "rank_current_rows": len(data["xep-hang"]),
        "p6_components": {name: len(data[name]) for name in
                          ("p6-dau-vao", "l2-nhan", "l2b-nhan", "l2c-nhan", "l3-nhan",
                           "p6-khau-tru-cuoi", "p7-khau-tru", "p7-khau-tru-v2",
                           "p7-v3-khau-tru-132-theo-P0-astra")},
        "pool_after_p7_final": len(data["xep-hang"]) - len(data["p7-v3-khau-tru-132-theo-P0-astra"]),
        "rank_current_labels_classes": dict(Counter(r["nhan"] + "_" + r["lop"] for r in data["xep-hang"])),
        "outside_main_reserve": len(candidates),
        "outside_removal": dict(Counter(r["loai_truoc"] or "KHONG_LOAI" for r in candidates)),
        "d8_removed": len(data["excluded"]),
        "d8_removed_gates": dict(Counter(r["cong_loai"] for r in data["excluded"].values())),
        "protected_bytes": protected,
        "normalized_reserve_sha256": sha(("\n".join(data["reserve"]) + "\n").encode()),
        "normalized_main_word_sha256": sha(("\n".join(data["main"]) + "\n").encode()),
        "d6_reference_available": (TOOLS / "vi.jsonl.gz").is_file(),
    }
    for name in ("check_wordlist.py", "verify.mjs", "build_wordlist.py",
                 "kiem-tra-giai-nghia.py", "d6-kiem.py", "d6-tham-chieu.json",
                 "README.md", "tieu-chi-thong-nhat.md", "huong-dan-giai-nghia.md",
                 "manifest.json"):
        read(TOOLS / name)
    save_json(EV / "inventory.json", summary)
    save_json(EV / "inputs.json", INPUTS)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
