"""Đối chứng vòng 1; chỉ ghi diff, số đo, hash và đầu mục trong thư mục Astra."""
import argparse
import ast
import csv
import hashlib
import json
import statistics
import subprocess
import sys
import unicodedata
import urllib.request
from collections import Counter
from fractions import Fraction

from inventory import EV, OUT, ROOT, TOOLS, UNIFIED, key, o1, read, save_json, save_tsv, tsv

OPUS = TOOLS / "ho-so" / "opus" / "du-phong-v2"
SIGNED_SUB = 34_314_528
SIGNED_WEB = 149_860_716
DECIDED_D = {"hì hụi", "tròng trành", "nhão nhẹt", "nhão nhoẹt", "chọc lét", "chán phèo"}
RETRACT_C = {"ăn trầu", "bèo bọt", "chấp nhặt", "giở giọng", "giở quẻ", "mụ mị", "non choẹt", "tía lia"}
KEEP_C = {"thụp", "tuổi xanh"}
VARIANT_WORDS = [
    "hì hụi", "hì hục", "hè hụi", "tròng trành", "chòng chành",
    "nhão nhẹt", "nhão nhoẹt", "nhão nhét", "nhão nhoét",
    "chọc lét", "chọc léc", "thọc lét", "thọc léc",
    "chán phèo", "chán phè", "loằng ngoằng", "loằn ngoằn",
    "chạng vạng", "choạng vạng", "bao tử", "báo tử",
    "tần số", "tận số", "vậy nên", "vảy nến",
]


def clean_h8(sub, web, leipzig, tatoeba):
    numbers = (sub, web, leipzig, tatoeba)
    if any(n is None for n in numbers):
        return "CHUA_DU_BON_KHO"
    if sub * 10_000_000 >= SIGNED_SUB or web * 10_000_000 >= SIGNED_WEB or leipzig >= 2 or tatoeba >= 1:
        return "MANH"
    return "YEU" if any(numbers) else "ZERO"


def human_reserve_ruling(word, a, o):
    if word == "hì hụi":
        return "D", "verified:Wiktionary en ghi hè hụi là dạng khác, HND xác nhận cả hai; assumed:Astra ký họ hì hụi/hè hụi; không suy hì hục cùng họ"
    if word in DECIDED_D:
        return "D", "assumed:Astra đồng ý quan hệ cùng từ H5c; verified:số sạch không thể đạt điều kiện 95%/20 ở cả hai kho; chờ ghi biên bản chung"
    if word == "loằng ngoằng":
        return "C", "assumed:đồng ý cần làm rõ quan hệ loằn ngoằn; không tự chặn chỉ vì bộ sinh biến thể"
    if word in RETRACT_C:
        return "A", "assumed:rút ưu tiên thấp chỉ do sắc thái khi chưa có phản đối H6 đủ căn cứ; không khẳng định mọi cách dùng đều vô hại"
    if word in KEEP_C:
        return "C", "assumed:giữ cảnh báo độ quen/phạm vi dùng; không đổi nhãn OK và không đổi S4"
    if o["bac"] == "C":
        return "C", "assumed:chấp nhận C như cảnh báo dữ liệu/nhầm lẫn/gần nghĩa, không như trượt H8 hay quyền đổi thứ tự S4"
    return a["tang"], "verified:hai phân loại không có bất đồng tầng; giữ các điều kiện D8/P6/giải nghĩa"


def reserve_diff():
    a_rows = tsv(OUT / "du-phong-phan-loai.tsv")
    o_rows = tsv(OPUS / "du-phong-205-phan-loai-opus.tsv")
    aa = {r["tu"]: r for r in a_rows}
    oo = {r["tu"]: r for r in o_rows}
    assert len(aa) == len(oo) == 205 and aa.keys() == oo.keys()
    counts = {r["tu"]: r for r in tsv(UNIFIED / "opus-counts.tsv") if r["vai_tro"] == "UNG_VIEN"}
    rows = []
    for word, a in aa.items():
        o = oo[word]
        sub, web, lei, tat = (int(a[x]) for x in ("sub_sach", "web_sach", "leipzig", "tatoeba"))
        strong = clean_h8(sub, web, lei, tat)
        tier, ruling = human_reserve_ruling(word, a, o)
        rows.append({
            "tu": word, "khoa": key(word), "lop": a["lop"], "ngan": a["ngan"],
            "astra_v1": a["tang"], "opus_v1": o["bac"],
            "doi_chieu": "KHOP" if a["tang"] == o["bac"] else "LECH",
            "astra_sau_review": tier, "nhan_dinh_sau_review": ruling,
            "canh_bao_rieng": "H7:đối chứng vảy nến dưới ngưỡng còi không tự chứng minh PASS; cần khép nhận định K2" if word == "vậy nên" else "-",
            "astra_ly_do": a["danh_gia_moi"], "opus_ly_do": o["van_de"] or "-",
            "co_nghia_lich_su": o["giai_nghia"], "H8_astra_v1": a["h8_so_hoc"],
            "H8_opus_v1": o["H8"], "H8_so_sach_kiem_lai": strong,
            "sub_sach": sub, "web_sach": web, "leipzig": lei, "tatoeba": tat,
            "dem_goc_ref": counts.get(word, {}).get("_ref", a["dem_sach_dong"]),
            "astra_ref": a["_ref"], "opus_ref": o["_ref"],
        })
    save_tsv(EV / "cross-review-reserve-diff.tsv", list(rows[0]), rows)
    return rows


def honorable_diff():
    aa = {r["tu"]: r for r in tsv(OUT / "honorable-mentions.tsv")}
    oo = {r["tu"]: r for r in tsv(OPUS / "de-cu-them-opus.tsv")}
    intermediate = {r["tu"]: r for r in tsv(OPUS / "evidence" / "de-cu-ung-vien.tsv")}
    p1 = {r["tu"]: r for r in tsv(UNIFIED / "xep-hang.tsv")}
    l3 = {r["tu"]: r for r in tsv(UNIFIED / "l3b-de-cu-opus.tsv")}
    l2 = {r["tu"]: r for r in tsv(UNIFIED / "l2d-ung-vien.tsv")}
    blocked = {r["khoa"] for r in tsv(TOOLS / "blocked_keys.tsv")}
    main = {key(line.split("|")[0]) for line in read(TOOLS / "wordlist.txt").splitlines()}
    reserve = {key(word) for word in read(TOOLS / "du-phong.txt").splitlines()}
    rows = []
    for word in sorted(aa.keys() | oo.keys(), key=o1):
        a, o = aa.get(word, {}), oo.get(word, {})
        assert key(word) not in main | reserve | blocked
        where = "CA_HAI" if a and o else "CHI_ASTRA" if a else "CHI_OPUS"
        note = "assumed:khác chiến lược chọn, không phải phản đối H9"
        state = "CO_THE_GOP_THEO_HO_SO"
        if word == "bao tử":
            state = "CHO_H7_DE_NGHI_K1"
            note = "verified:còi báo tử đạt mốc 0,3; assumed:Astra xác nhận cách đọc tự nhiên thuộc H6.4, đề nghị K1; chưa tính là HM đã qua cổng"
        elif word == "chạng vạng":
            state = "CHO_H5"
            note = "verified:có đối chứng choạng vạng trong bảng HND; assumed:cần xác nhận cùng từ và đo, chưa đủ để gọi PASS H5 mới hoặc D"
        elif word == "tần số":
            state = "CHO_KHEP_H7"
            note = "verified:tận số dưới mốc còi; assumed:đề nghị ghi xử lý đọc không dấu, không dùng dưới-mốc làm chứng minh PASS"
        elif o.get("nhom") in ("DC3", "DC4", "DC5"):
            state = "BACKLOG_CHUA_DU_HO_SO_H"
            note = "verified:chưa có nhãn/lớp và phiếu P4/H9; assumed:tách khỏi tập HM đã qua cổng, không tự coi dữ liệu thiếu là 0"
            if o["nhom"] == "DC4":
                note += "; verified:lô L2D ghi H8 yếu/cần đọc và có mục cần H3 hai xác nhận"
            if o["nhom"] == "DC5":
                note += "; verified:chưa đo bốn kho, chưa nối xác nhận H3 hai bên"
            if word == "giờ cao điểm":
                state = "CHO_H2"
                note = "assumed:Astra phản đối H2: ba khối gọi khoảng thời gian, không thuộc tập tên thực thể cho phép; verified:lô chỉ ghi noun, checker chỉ đếm khối"
        elif word == "piano":
            note = "verified:spelling_families.tsv:269 đã QUA_RIENG_H5; mã loại DC2_H5 của Opus sai dữ kiện, không chứng minh họ mới chưa đo"
        elif word == "vây cá":
            note = "verified:H8 sạch 3/7/0/0 là YEU, không phải MANH như Astra v1; P4 Astra:4811 có đọc kiểm, chu-ky.tsv:2399 có xác nhận H8 Opus"
        elif where == "CHI_OPUS" and o["nhom"] == "DC1":
            state = "UU_TIEN_THAP_RA_H6"
            note = "assumed:Astra giữ đề nghị rà nghĩa trước khi ưu tiên; chưa có bằng chứng mới để tuyên bố loại H6, không xóa nhãn OK lịch sử"
        original = p1.get(word, l3.get(word, l2.get(word, {})))
        measured = a or o
        h8_numbers = [int(measured[k]) if measured.get(k) not in (None, "", "-", "None") else None
                      for k in ("sub_sach", "web_sach", "leipzig", "tatoeba")]
        rows.append({
            "tu": word, "khoa": key(word), "doi_chieu": where,
            "astra_nhom": a.get("tang", "-"), "opus_nhom": o.get("nhom", "-"),
            "lop_astra": a.get("lop", "-"), "lop_opus": o.get("lop") or "-",
            "nhan_astra": a.get("nhan", "-"), "nhan_opus": o.get("nhan") or "-",
            "F_astra": a.get("F", "-"), "F_opus": o.get("F") or "-",
            "H8_astra_v1": a.get("h8_so_hoc", "-"), "H8_opus_v1": o.get("H8") or "-",
            "H8_sach_hoac_thieu_kho": clean_h8(*h8_numbers),
            "opus_vi_sao_bo": intermediate.get(word, {}).get("loai_vi") or "-",
            "astra_de_xuat_sau_review": state, "nhan_dinh": note,
            "nguon_goc_ref": original.get("_ref", "-"),
            "astra_ref": a.get("_ref", "-"), "opus_ref": o.get("_ref", "-"),
        })
    assert len(rows) == 309 and len({r["khoa"] for r in rows}) == 309
    save_tsv(EV / "cross-review-honorable-diff.tsv", list(rows[0]), rows)
    return rows, aa, oo


def count_evidence():
    source = tsv(UNIFIED / "opus-counts.tsv")
    rows = []
    for word in VARIANT_WORDS + ["cả nghĩ", "tối mù", "piano"]:
        matches = [r for r in source if r["tu"] == word]
        for r in matches or [{}]:
            sub = int(r["sub_sach"]) if r else None
            web = int(r["web_sach"]) if r else None
            mean = (Fraction(sub, SIGNED_SUB) + Fraction(web, SIGNED_WEB)) * 500_000 if r else None
            rows.append({
                "tu": word, "khoa": key(word), "sub_be_mat": r.get("sub_be_mat", "CHUA_DO"),
                "sub_sach": sub, "web_be_mat": r.get("web_be_mat", "CHUA_DO"), "web_sach": web,
                "sub_dong_khac": r.get("sub_sach_dong_khac", "CHUA_DO"),
                "ppm_gop_mau_so_da_ky": f"{float(mean):.9f}" if mean is not None else "CHUA_DO",
                "ppm_gop_cot_cu": f"{(float(r['sub_ppm_sach']) + float(r['web_ppm_sach'])) / 2:.9f}" if r else "CHUA_DO",
                "nguon_ref": r.get("_ref", "-"),
            })
    save_tsv(EV / "cross-review-counts.tsv", list(rows[0]), rows)
    return rows


def independently_verify_hnd():
    manifest = json.loads(read(TOOLS / "manifest.json"))
    tags = {}
    metadata = []
    for item in manifest["nguon_du_lieu"]:
        name = item["source"]
        if name not in ("Viet11K", "Viet22K", "Viet39K", "Viet74K"):
            continue
        url = item["url"].replace("https://github.com/", "https://raw.githubusercontent.com/").replace("/blob/", "/")
        with urllib.request.urlopen(url, timeout=40) as response:
            payload = response.read()
        digest = hashlib.sha256(payload).hexdigest()
        assert digest == item["sha256"], name
        faces = payload.decode("utf-8").splitlines()
        for word in VARIANT_WORDS:
            exact = [i for i, face in enumerate(faces, 1) if face == word]
            normalized = [i for i, face in enumerate(faces, 1)
                          if unicodedata.normalize("NFC", face.strip().lower()).replace("-", " ") == word]
            tags.setdefault(word, []).append({
                "source": name, "exact_lines": exact, "normalized_lines": normalized,
                "sha256": digest,
            })
        metadata.append({"source": name, "url": url, "sha256": digest,
                         "expected_sha256": item["sha256"], "bytes": len(payload), "rows": len(faces)})
        del payload, faces
    rows = []
    for word in VARIANT_WORDS:
        checks = tags[word]
        rows.append({
            "tu": word, "khoa": key(word),
            "hnd_exact": ";".join(r["source"] for r in checks if r["exact_lines"]),
            "hnd_normalized": ";".join(r["source"] for r in checks if r["normalized_lines"]),
            "source_lines": ";".join(r["source"] + ":" + ",".join(map(str, r["exact_lines"]))
                                    for r in checks if r["exact_lines"]),
            "ket_luan": "verified:thành viên và hash; không phải bằng chứng tự động về cùng từ hoặc loại c/d",
        })
    save_tsv(EV / "cross-review-hnd-membership.tsv", list(rows[0]), rows)
    save_json(EV / "cross-review-hnd-sources.json", metadata)
    return metadata


def metrics(reserve, honorable, aa, oo):
    labels = tsv(TOOLS / "labels.tsv")
    main_f = sorted(float(r["F"]) for r in labels if r["trang_thai"] == "CHINH" and r["lop"] != "F")
    reserve_f = sorted(float(r["F"]) for r in labels if r["trang_thai"] == "DU_PHONG" and r["lop"] != "F")
    qex = statistics.quantiles(main_f, n=100, method="exclusive")
    qin = statistics.quantiles(main_f, n=100, method="inclusive")
    variants = count_evidence()
    bao = next(r for r in variants if r["tu"] == "báo tử")
    warnings = tsv(UNIFIED / "canh-bao-khong-dau.tsv")
    p4o = {r["tu"]: r for r in tsv(UNIFIED / "phieu-opus.tsv")}
    p4a = {r["tu"]: r for r in tsv(UNIFIED / "phieu-astra.tsv")}
    rank = {r["tu"]: r for r in tsv(UNIFIED / "xep-hang.tsv")}
    assert all(
        rank[w]["nhan"] == "R1" and rank[w]["lop"] != "F"
        and {p4o[w]["nhan"], p4a[w]["nhan"]} == {"OK", "R1"}
        and float(rank[w]["F"]) >= 50
        for w, row in oo.items() if row["nhom"] == "DC2"
    )
    l2d = tsv(UNIFIED / "l2d-ung-vien.tsv")
    selected_l2d = [r for r in l2d if r["tu"] in oo and oo[r["tu"]]["nhom"] == "DC4"]
    from classify import evidence_row, final_h9_refs
    from inventory import load
    data = load()
    h9refs = final_h9_refs(data)
    core = [r["tu"] for r in honorable if r["astra_de_xuat_sau_review"] == "CO_THE_GOP_THEO_HO_SO"]
    core_h8 = Counter()
    for word in core:
        checked = evidence_row(word, data, h9refs)
        core_h8[clean_h8(*(int(checked[k]) for k in ("sub_sach", "web_sach", "leipzig", "tatoeba")))] += 1
    assert len(core) == 231
    assert "hè hụi" not in set(data["main"] + data["reserve"])
    result = {
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "reserve_equal": sum(r["doi_chieu"] == "KHOP" for r in reserve),
        "reserve_different": sum(r["doi_chieu"] == "LECH" for r in reserve),
        "tier_matrix": dict(Counter(r["astra_v1"] + "→" + r["opus_v1"] for r in reserve)),
        "astra_tiers_after_review_proposal": dict(Counter(r["astra_sau_review"] for r in reserve)),
        "reserve_h8_clean": dict(Counter(r["H8_so_sach_kiem_lai"] for r in reserve)),
        "H8_Astra_corrections": [r["tu"] for r in reserve if r["H8_astra_v1"] != r["H8_so_sach_kiem_lai"]],
        "HM_intersection": len(aa.keys() & oo.keys()), "HM_Astra_only": len(aa.keys() - oo.keys()),
        "HM_Opus_only": len(oo.keys() - aa.keys()), "HM_union": len(honorable),
        "HM_Opus_only_groups": dict(Counter(r["nhom"] for w, r in oo.items() if w not in aa)),
        "HM_after_review_states": dict(Counter(r["astra_de_xuat_sau_review"] for r in honorable)),
        "HM_core_rechecked_source_gates": len(core),
        "HM_core_H8_clean": dict(core_h8),
        "H8_Astra_HM_corrections": [r["tu"] for r in honorable if r["H8_astra_v1"] != "-"
                                  and r["H8_astra_v1"] != r["H8_sach_hoac_thieu_kho"]],
        "Opus_DC2_60_original_votes_and_scores_verified": True,
        "Opus_missing_class": sum(not r["lop"] for r in oo.values()),
        "Opus_missing_four_corpus_measurements": [w for w, r in oo.items() if any(r[k] in ("", "None", "-") for k in ("sub_sach", "web_sach", "leipzig", "tatoeba"))],
        "Opus_selected_L2D_h3_needs_two": [r["tu"] for r in selected_l2d if "H3_CAN_HAI_XAC_NHAN" in r["co_ke_hoach"]],
        "F_main_nonF_median": statistics.median(main_f),
        "F_reserve_nonF_median": statistics.median(reserve_f),
        "F_main_exclusive_P1_P5": [qex[0], qex[4]],
        "F_main_inclusive_P1_P5": [qin[0], qin[4]],
        "reserve_below_exclusive_P1_P5": [sum(x < qex[0] for x in reserve_f), sum(x < qex[4] for x in reserve_f)],
        "max_reserve_F": max(reserve_f),
        "max_reserve_rank_percent_of_main_nonF": 100 * sum(x <= max(reserve_f) for x in main_f) / len(main_f),
        "bao_tu_reading": bao,
        "bao_tu_in_existing_alarm": any(r.get("ung_vien") == "bao tử" or r.get("doc_khac") == "báo tử" for r in warnings),
        "gia_tri": "verified:số đo, đối chiếu; assumed:phán đoán ngôn ngữ và tầng sau review, chưa là kết luận chung",
    }
    save_json(EV / "cross-review-metrics.json", result)
    return result


def verify_outputs(result, inputs):
    protected_before = json.loads((EV / "inventory.json").read_text(encoding="utf-8"))["protected_bytes"]
    protected_now = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                     for name in ("index.html", "thong-tin.html", r"analyzing-tools\wordlist.txt")}
    document = (ROOT / "WordListAnalyze.md").read_bytes()
    protected_now["WordListAnalyze.md section10 bytes"] = hashlib.sha256(
        document[document.index("## 10. Danh sách 7.776 từ phát hành".encode()):
                 document.index("## 11. Danh sách dự phòng".encode())]).hexdigest()
    assert protected_before == protected_now
    for name, metadata in inputs.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == metadata["sha256_bytes"], name

    def pure_function(path, name, extra=None):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        function = next(x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == name)
        namespace = dict(extra or {})
        exec(compile(ast.Module(body=[function], type_ignores=[]), str(path), "exec"), namespace)
        return namespace[name]

    verdict = pure_function(TOOLS / "ho-so" / "opus" / "h5" / "verdict_h5.py", "verdict")
    h5_checks = {
        "trong_tranh_chong_chanh": verdict("c", 2, 3, 1, 6),
        "nhao_nhet_nhao_nhoet_gop_khoa": verdict("c", 9, 11, 0, 2),
        "piano_frozen_family": verdict("f", 449, 3, 1818, 2),
    }
    assert list(h5_checks.values()) == ["LOAI_THIEU_DU_LIEU", "LOAI_THIEU_DU_LIEU", "QUA_RIENG_H5"]
    substitute = pure_function(UNIFIED / "p6-tinh-doc-lap-astra.py", "subst", {"Counter": Counter})
    assert substitute(Counter({"R1_N": 1}), Counter({"OK_N": 1}), 0) is None
    mapping = substitute(Counter({"OK_F": 40}), Counter({"OK_F": 77}), 0)
    assert sum(mapping.values()) == 40

    reference_count = 0
    source_lengths = {}
    for filename in ("cross-review-reserve-diff.tsv", "cross-review-honorable-diff.tsv", "cross-review-counts.tsv"):
        with (EV / filename).open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream, delimiter="\t"):
                for field, cell in row.items():
                    if not field.endswith("_ref") or cell == "-":
                        continue
                    for reference in cell.split(";"):
                        source, line = reference.rsplit(":", 1)
                        if source not in source_lengths:
                            source_lengths[source] = len((ROOT / source).read_text(encoding="utf-8").splitlines())
                        assert 1 <= int(line) <= source_lengths[source], reference
                        reference_count += 1
    artifact_paths = [OUT / "round-1-cross-review.md"] + sorted(EV.glob("cross-review*"))
    for path in artifact_paths:
        if not path.is_file():
            continue
        raw = path.read_bytes()
        text = raw.decode("utf-8")
        assert not raw.startswith(b"\xef\xbb\xbf") and raw.endswith(b"\r\n"), path
        assert raw.count(b"\r\n") == raw.count(b"\n"), path
        assert all(line == line.rstrip(" \t") for line in text.splitlines()), path
    verification = {
        "python": sys.version.split()[0],
        "command": ["python", "-X", "utf8", "-B", *sys.argv],
        "protected_bytes_unchanged": True, "protected_bytes": protected_now,
        "read_only_inputs_hashes_still_match": len(inputs),
        "H5_extracted_original_function_checks": h5_checks,
        "R1_to_OK_original_subst_returns_none": True,
        "forty_F_candidates_distinct_mapped_slots": sum(mapping.values()),
        "reference_pointers_checked": reference_count,
        "own_cross_review_artifacts_format_checked": [str(p.relative_to(OUT)) for p in artifact_paths if p.is_file()],
        "reserve_rows": 205, "honorable_union_rows": 309,
        "fresh_D6_run": False,
        "note": "Không chạy main của module được trích hàm; không ghi đầu ra vào thư mục Opus.",
    }
    save_json(EV / "cross-review-verification.json", verification)
    (EV / "cross-review-run.log").write_text(
        "COMMAND " + " ".join(verification["command"]) + "\n"
        + json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        + "VERIFY " + json.dumps(verification, ensure_ascii=False) + "\n",
        encoding="utf-8", newline="\r\n",
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-hnd", action="store_true",
                        help="Đọc bốn wordlist ghim trong bộ nhớ, chỉ lưu thành viên/hash, không lưu payload")
    args = parser.parse_args()
    for path in [
        OUT / "round-1-analysis.md", OPUS / "round-1-analysis.md",
        OPUS / "evidence" / "chung.py", OPUS / "evidence" / "do-bien-the.py",
        OPUS / "evidence" / "phan-loai-du-phong.py", OPUS / "evidence" / "lap-de-cu.py",
        OPUS / "evidence" / "xuat-de-cu.py", OPUS / "evidence" / "kiem-hnd.py",
        OPUS / "evidence" / "kiem-dau-ra.py", TOOLS / "tieu-chi-thong-nhat.md",
        TOOLS / "manifest.json", ROOT / "WordListAnalyze.md",
        UNIFIED / "p6-tinh-doc-lap-astra.py",
        TOOLS / "ho-so" / "opus" / "h5" / "verdict_h5.py",
        EV / "cross-review-web-sources.tsv",
        EV / "cross-review.py", EV / "inventory.py", EV / "classify.py",
    ]:
        read(path)
    reserve = reserve_diff()
    honorable, aa, oo = honorable_diff()
    result = metrics(reserve, honorable, aa, oo)
    if args.verify_hnd:
        result["hnd_checked_sources"] = len(independently_verify_hnd())
    from inventory import INPUTS
    save_json(EV / "cross-review-inputs.json", INPUTS)
    if (OUT / "round-1-cross-review.md").exists():
        verify_outputs(result, INPUTS)
    print(json.dumps({k: v for k, v in result.items() if k != "Opus_missing_four_corpus_measurements"},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
