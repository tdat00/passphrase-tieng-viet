"""Đối số lượt duyệt 2; không chạy main của script Opus hoặc ghi ngoài hồ sơ Astra."""
import ast
import collections
import copy
import hashlib
import itertools
import json
import statistics
import unicodedata
from fractions import Fraction

from p6_preview import scorer
from screen_core import AT, EV, OUT, ROOT, U, key, load, o1, ppm, save_json, save_tsv, tsv

O = AT / "ho-so" / "opus" / "ra-thay-chinh"
OE = O / "evidence"


def extract(path, names, environment):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    nodes = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in names:
            nodes.append(node)
        elif isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and node.targets[0].id in names:
            nodes.append(node)
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), "exec"), environment)
    return environment


def full_h5b(word, tone):
    choices = []
    for syl in word.split():
        de = unicodedata.normalize("NFD", syl)
        accents = "".join(c for c in de if c in tone)
        base = unicodedata.normalize("NFC", "".join(c for c in de if c not in tone))
        variants = [syl]
        for onset in ("qu", "h", "k", "l", "m", "s", "t"):
            if base in (onset + "i", onset + "y"):
                variants.append(onset + unicodedata.normalize("NFC", ("y" if base[-1] == "i" else "i") + accents))
        choices.append(variants)
    return set(" ".join(v) for v in itertools.product(*choices)) - {word}


def main():
    d = load()
    files = [U / f"ra-thay-chinh-{n}.{ext}" for n, ext in (
        ("bao-cao-chung", "md"), ("ke-hoach", "md"), ("cau-hoi", "md"),
        ("h7", "tsv"), ("h5", "tsv"), ("thay-the", "tsv"),
    )]
    files += [OE / n for n in ("de-xuat-thay-v2.py", "hop-nhat-rtc.py", "doi-chieu-v2.py",
                               "cap-h5f.tsv", "dem-h5f.tsv", "dem-h5f.log", "dem-h5.py")]
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    snap = EV / "rd2-input-hashes.json"
    if snap.exists():
        assert json.loads(snap.read_text(encoding="utf-8")) == hashes, "Draft input changed during review"
    else:
        save_json(snap, hashes)
    prefix = EV / "rd2-review-prefix.json"
    if not prefix.exists():
        body = (OUT / "round-1-review-drafts.md").read_bytes()
        save_json(prefix, {"bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()})
    h7, h5, slots = (tsv(U / f"ra-thay-chinh-{stem}.tsv") for stem in ("h7", "h5", "thay-the"))
    assert len(h7) == 349 and len(h5) == 65 and len(slots) == 238
    outgoing = {r["tu"] for r in slots if r["vai_tro"] == "RA"}
    extra = {r["tu"] for r in slots if r["vai_tro"] == "RA_NEU_S1_THEO_ASTRA"}
    incoming = [r["tu"] for r in slots if r["vai_tro"] == "VAO"]
    spares = [r["tu"] for r in slots if r["vai_tro"] == "DU_BI"]
    assert (len(outgoing), len(extra), len(incoming), len(spares)) == (101, 17, 101, 19)
    lab = d["label_by_word"]
    main_set = set(d["main"])
    projected = main_set - outgoing | set(incoming)
    assert len(projected) == len({key(w) for w in projected}) == 7776
    assert all(lab[w]["nhan"] == "OK" for w in projected)
    assert sum(lab[w]["lop"] == "F" for w in projected) == 77
    candidates = sorted(d["du-phong-phan-loai"], key=lambda r: int(d["rank_by_word"][r["tu"]]["hang"]))
    ns = extract(OE / "de-xuat-thay-v2.py", {"GATES_OPEN", "TONE", "chon", "h5b"},
                 {"collections": collections, "unicodedata": unicodedata})
    selected, reserve, f, r1, _ = ns["chon"](candidates, 101, 77, 0, lab)
    assert [r["tu"] for r in selected] == incoming and [r["tu"] for r in reserve] == spares
    assert f == 77 and r1 == 0
    tests = []
    for label, rejected in (("O101", outgoing), ("O101_THEO", outgoing | {"theo"}), ("A118", outgoing | extra)):
        f0 = sum(lab[w]["lop"] == "F" for w in main_set - rejected)
        picked, remain, ff, rr, _ = ns["chon"](candidates, len(rejected), f0, 0, lab)
        target = main_set - rejected | {r["tu"] for r in picked}
        assert len(target) == len({key(w) for w in target}) == 7776 and ff <= 77 and rr == 0
        tests.append({"case": label, "out": len(rejected), "in": len(picked), "spares": len(remain),
                      "keys": len(target), "F": ff, "R1": rr})
    one = dict(next(r for r in candidates if r["tu"] == "mụ mị"))
    one["ngan"] = "R1_KHONG_F"
    hypothetical_labels = {one["tu"]: {"nhan": "R1"}}
    r1_bad, _, _, r1_total, _ = ns["chon"]([one], 1, 77, 0, hypothetical_labels)
    actual_h5b = set(ns["h5b"]("tỉ mỉ"))
    expected_h5b = full_h5b("tỉ mỉ", ns["TONE"])
    missing_h5b = sorted(expected_h5b - actual_h5b)
    assert missing_h5b and not ns["h5b"]("qua quýt")
    affected = []
    for r in selected + reserve:
        missing = full_h5b(r["tu"], ns["TONE"]) - set(ns["h5b"](r["tu"]))
        if missing:
            affected.append({"tu": r["tu"], "missing_generated_forms": sorted(missing)})

    merger = extract(OE / "hop-nhat-rtc.py", {"H5_A", "ma"}, {})
    assert merger["ma"](merger["H5_A"], "CHO_XAC_NHAN_QUAN_HE", "test") == "CHO"
    assert merger["ma"](merger["H5_A"], "NHAN_QUA_CU", "test") == "QUA"
    try:
        merger["ma"](merger["H5_A"], "UNKNOWN_RD2_TEST", "test")
    except SystemExit:
        unknown_fails = True
    else:
        unknown_fails = False
    assert unknown_fails
    old_false = {(r["tu"], r["bien_the"]) for r in tsv(EV / "rd1-H5-qua-gia.tsv")}
    assert all(r["trang_thai"] == "CHO_CAN_CU" for r in h5 if (r["tu"], r["bien_the"]) in old_false)

    measure = {r["dang"]: r for r in tsv(OE / "dem-h5f.tsv")}
    cols = ("sub_moi_dong_sach", "web_dong_khac_sach", "sub_dong_khac_sach", "sub_moi_dong", "web_dong_khac")
    totals = {}
    for w in ("cải xoong", "cải soong", "xà phòng", "xà bông"):
        forms = {w, w.replace(" ", "-"), w.replace(" ", "")}
        assert forms <= measure.keys() and len(forms) == 3
        totals[w] = {c: sum(int(measure[f][c]) for f in forms) for c in cols}
    assert totals["cải xoong"]["sub_moi_dong_sach"] == 4
    assert totals["cải soong"]["sub_moi_dong_sach"] == 0
    assert totals["xà phòng"]["sub_moi_dong_sach"] == 181
    assert totals["xà bông"]["sub_moi_dong_sach"] == 108
    assert totals["xà phòng"]["web_dong_khac_sach"] == 3895
    assert totals["xà bông"]["web_dong_khac_sach"] == 320
    robustness = []
    for col in cols:
        a, b = totals["xà phòng"][col], totals["xà bông"][col]
        assert a + b >= 20 and 100 * max(a, b) < 95 * (a + b)
        robustness.append({"column": col, "xa_phong": a, "xa_bong": b, "total": a + b,
                           "xa_phong_percent": f"{float(Fraction(100*a, a+b)):.9f}", "pass95": False})
    manifest_hashes = {r["sha256"] for r in json.loads((AT / "manifest.json").read_text(encoding="utf-8"))["nguon_du_lieu"]}
    corpus_log = []
    for line in (OE / "dem-h5f.log").read_text(encoding="utf-8").splitlines():
        if line.startswith(("sub:", "web:")):
            record = json.loads(line.split(": ", 1)[1])
            assert record["sha256"] in manifest_hashes and record["khop_manifest"]
            corpus_log.append(record)
    assert len(corpus_log) == 2
    existing = []
    for row in h7:
        if row["trang_thai"] == "DONG_THUAN_GIU_CAN_KY_K2":
            signed = [s for s in d["chu-ky"] if s["tu"] == row["tu_chinh"] and s["loai_ky"] == "K2" and s["hieu_luc"] == "CO"]
            if {"Astra", "Opus"} <= {s["nguoi_ky"] for s in signed}:
                existing.append({"tu": row["tu_chinh"], "current_row": row["_ref"],
                                 "signature_rows": ";".join(s["_ref"] for s in signed),
                                 "action_Astra": "GIU_CHU_KY_CU; không có chứng cứ mới ở lượt này"})
    assert {r["tu"] for r in existing} == {"nướng", "phết"}
    save_tsv(EV / "rd2-K2-da-ky.tsv", existing)

    small = {}
    for r in tsv(AT / "ho-so" / "discussion" / "bang-khoa-chung.tsv"):
        words = json.loads(r["ung_vien"])
        ls, ts = json.loads(r["leipzig_so_cau"]), json.loads(r["tatoeba_so_cau"])
        for i, word in enumerate(words):
            small[word] = {"leipzig": ls[i], "tatoeba": ts[i]}
    for stem in ("l2", "l2b", "l2c", "l3"):
        for r in tsv(U / f"{stem}-ung-vien.tsv"):
            small[r["tu"]] = {"leipzig": int(r["leipzig_so_cau"]), "tatoeba": int(r["tatoeba_so_cau"])}
    pool = {}
    for r in d["xep-hang"]:
        w, c = r["tu"], d["counts"][r["tu"]]
        pool[w] = {"sub_sach": int(c["sub_sach"]), "web_sach": int(c["web_sach"]), **small[w],
                   "nhan": r["nhan"], "lop": r["lop"], "phat_h5d": bool(int(r["phat_h5d"]))}
    score = scorer()
    assert score(copy.deepcopy(pool)) == [r["tu"] for r in d["xep-hang"]]
    removed_old = {r["tu"] for r in d["nguon-goc-giai-nghia"] if r["trang_thai"] == "LOAI"}
    excluded = {r["tu"] for r in candidates if r["tang"] == "D"} | set(ns["GATES_OPEN"])
    keep = set("mặt trời|mặt trăng|trái đất|ngân hà|công chúa|hoàng tử|hoàng hậu|mồ hôi|ruồi|gián|chào cờ|ròng rọc|dép lê|bánh chưng".split("|"))
    locked_queue = incoming + spares
    rescore = []
    for mode in ("CHON_DUOC_MOI_TINH", "H_QUA_CONG_TINH_D6_LOAI_KHI_CHON"):
        removed = removed_old if mode == "CHON_DUOC_MOI_TINH" else {"bao tử", "bào tử", "chạng vạng"}
        active = {w: copy.deepcopy(r) for w, r in pool.items() if w not in removed | excluded | outgoing}
        order = score(active)
        chosen = set(keep)
        ff = sum(active[w]["lop"] == "F" for w in chosen)
        for w in order:
            if len(chosen) == 7776:
                break
            if w in chosen or w in removed_old or active[w]["nhan"] != "OK":
                continue
            is_f = active[w]["lop"] == "F"
            if ff + is_f > 77:
                continue
            chosen.add(w)
            ff += is_f
        assert len(chosen) == 7776
        new_queue = [w for w in order if w in set(locked_queue)]
        differences = [{"position": i, "locked": a, "rescored": b}
                       for i, (a, b) in enumerate(zip(locked_queue, new_queue), 1) if a != b]
        rescore.append({"mode": mode, "pool": len(active), "F": ff,
                        "new_entry_only": sorted(chosen - projected, key=o1),
                        "locked_only": sorted(projected - chosen, key=o1),
                        "queue_difference_count": len(differences), "queue_differences": differences})
    result = {
        "H7_states": dict(collections.Counter(r["trang_thai"] for r in h7)),
        "H5_states": dict(collections.Counter(r["trang_thai"] for r in h5)),
        "roles": dict(collections.Counter(r["vai_tro"] for r in slots)),
        "selection_cases": tests, "F_R1_current_rows_valid": True,
        "R1_to_OK_counterexample": {"candidate_taken": bool(r1_bad), "R1_after": r1_total,
                                  "actual_current_reserve_R1": sum(lab[r["tu"]]["nhan"] == "R1" for r in candidates)},
        "H5b_combination_missing": missing_h5b, "H5b_affected_current_queue": affected,
        "H5_exact_mapping_pass": True, "H5_unknown_code_fails_closed": unknown_fails,
        "H5f_totals": totals, "H5f_sensitivity": robustness, "corpus_hash_logs_match_manifest": True,
        "corpus_recounted_by_Astra": False,
        "existing_K2_in_pending": existing, "net_new_K2_candidates": 196 - len(existing),
        "O101_median": {
            "out": statistics.median(float(ppm(d["counts"][w])) for w in outgoing),
            "in": statistics.median(float(ppm(d["counts"][w])) for w in incoming),
        },
        "S4_O101": rescore,
        "new_glosses_written": 0, "source_text_saved": False,
    }
    save_json(EV / "rd2-audit-summary.json", result)
    print(json.dumps({k: v for k, v in result.items() if k not in {"S4_O101", "H5f_totals", "existing_K2_in_pending"}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
