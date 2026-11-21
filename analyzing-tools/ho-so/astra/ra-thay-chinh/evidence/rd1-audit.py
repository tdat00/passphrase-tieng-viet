"""Đối số độc lập của bản nháp chung; chỉ ghi metadata/số trong hồ sơ Astra."""
import copy
import csv
import hashlib
import io
import json
from collections import Counter

from p6_preview import scorer
from screen_core import AT, EV, OUT, ROOT, U, key, load, o1, save_json, save_tsv, tsv


def main():
    d = load()
    h7 = tsv(U / "ra-thay-chinh-h7.tsv")
    h5 = tsv(U / "ra-thay-chinh-h5.tsv")
    slots = tsv(U / "ra-thay-chinh-thay-the.tsv")
    out = {r["tu_ra"] for r in slots if r["tu_ra"] != "-"}
    incoming = [r["tu_vao"] for r in slots if r["vai_tro_vao"] == "VAO"]
    spares = [r["tu_vao"] for r in slots if r["vai_tro_vao"] == "DU_BI"]
    assert len(h7) == 349 and len(h5) == 65 and len(slots) == 112
    assert len(out) == len(incoming) == 87 and len(spares) == 25
    assert len({r["khoa"] for r in h7}) == 349
    assert len({(r["tu"], r["bien_the"]) for r in h5}) == 65
    reserve = d["du-phong-phan-loai"]
    blocked_reserve = {"loằng ngoằng", "ngoại trừ", "qua quýt"}
    ordered = sorted(reserve, key=lambda r: int(d["rank_by_word"][r["tu"]]["hang"]))
    eligible = [
        r for r in ordered if r["tang"] != "D" and r["tu"] not in blocked_reserve
        and r["ngan"] == "OK_KHONG_F"
    ]
    assert [r["tu"] for r in eligible[:112]] == incoming + spares
    selected = (set(d["main"]) - out) | set(incoming)
    labels = d["label_by_word"]
    assert len(selected) == len({key(w) for w in selected}) == 7776
    assert all(4 <= len(key(w)) <= 12 and 1 <= len(w.split()) <= 3 for w in selected)
    assert all(labels[w]["nhan"] == "OK" for w in selected)
    assert sum(labels[w]["lop"] == "F" for w in selected) == 77
    new_h7_out = {r["tu_chinh"] for r in h7 if r["opus"] in {"K0", "K1"}}
    new_blocks = {r["khoa"] for r in d["blocked_keys"]} | {key(w) for w in new_h7_out} | {"baotu"}
    assert not new_blocks & {key(w) for w in selected}
    false_pass = [
        {"tu": r["tu"], "bien_the": r["bien_the"], "astra_ma": r["astra_ma"],
         "trang_thai_sai": r["trang_thai"], "nguon": r["_ref"],
         "nguyen_nhan": "'QUA' in 'CHO_XAC_NHAN_QUAN_HE' == True"}
        for r in h5 if r["trang_thai"] == "DONG_THUAN_QUA" and r["astra_ma"].startswith("CHO")
    ]
    assert len(false_pass) == 9
    save_tsv(EV / "rd1-H5-qua-gia.tsv", false_pass)
    old_reserve = {r["tu"] for r in reserve}
    a24 = {r["tu_vao_de_xuat"] for r in tsv(OUT / "de-xuat-thay-the-S4.tsv")} & old_reserve
    first24 = set(incoming[:24])
    assert len(a24) == 24 and len(first24 & a24) == 23

    counts = d["counts"]
    frequencies = []
    import statistics
    for role, words in (("RA", out), ("VAO", incoming)):
        from screen_core import ppm
        frequencies.append({
            "role": role, "n": len(words),
            "median_clean_ppm": statistics.median(float(ppm(counts[w])) for w in words),
        })
    hypothetical_out = out | {"theo"}
    need_non_f = sum(labels[w]["lop"] != "F" for w in hypothetical_out)
    slack_f = 77 - sum(labels[w]["lop"] == "F" for w in set(d["main"]) - hypothetical_out)
    queue = [
        r for r in ordered if r["tang"] != "D" and r["tu"] not in blocked_reserve
        and (r["lop"] != "F" or slack_f > 0)
    ]
    bad_chosen = queue[:need_non_f]
    bad_result = (set(d["main"]) - hypothetical_out) | {r["tu"] for r in bad_chosen}
    counterexample = {
        "scenario": "O87 + theo; chạy lại logic vòng chọn v2 hiện có, không nạp HND",
        "out": len(hypothetical_out), "needed_OK_N": need_non_f, "initial_F_slack": slack_f,
        "selected": len(bad_chosen),
        "selected_F": sum(r["lop"] == "F" for r in bad_chosen),
        "result_size": len(bad_result),
        "result_F": sum(labels[w]["lop"] == "F" for w in bad_result),
    }
    assert counterexample["result_size"] != 7776 and counterexample["result_F"] > 77

    small = {}
    for r in tsv(AT / "ho-so" / "discussion" / "bang-khoa-chung.tsv"):
        ws = json.loads(r["ung_vien"])
        ls, ts = json.loads(r["leipzig_so_cau"]), json.loads(r["tatoeba_so_cau"])
        for i, w in enumerate(ws):
            small[w] = {"leipzig": ls[i], "tatoeba": ts[i]}
    for stem in ("l2", "l2b", "l2c", "l3"):
        for r in tsv(U / f"{stem}-ung-vien.tsv"):
            small[r["tu"]] = {"leipzig": int(r["leipzig_so_cau"]), "tatoeba": int(r["tatoeba_so_cau"])}
    pool = {}
    for r in d["xep-hang"]:
        w = r["tu"]
        pool[w] = {
            "sub_sach": int(counts[w]["sub_sach"]), "web_sach": int(counts[w]["web_sach"]),
            **small[w], "nhan": r["nhan"], "lop": r["lop"], "phat_h5d": bool(int(r["phat_h5d"])),
        }
    score = scorer()
    assert score(copy.deepcopy(pool)) == [r["tu"] for r in d["xep-hang"]]
    removed_old = {r["tu"] for r in d["nguon-goc-giai-nghia"] if r["trang_thai"] == "LOAI"}
    no_reserve = {r["tu"] for r in reserve if r["tang"] == "D"} | blocked_reserve
    keep = set("mặt trời|mặt trăng|trái đất|ngân hà|công chúa|hoàng tử|hoàng hậu|mồ hôi|ruồi|gián|chào cờ|ròng rọc|dép lê|bánh chưng".split("|"))
    s4 = []
    for mode in ("CHON_DUOC_MOI_TINH", "H_QUA_CONG_TINH_D6_LOAI_KHI_CHON"):
        score_removed = removed_old if mode == "CHON_DUOC_MOI_TINH" else {"bao tử", "bào tử", "chạng vạng"}
        active = {w: copy.deepcopy(r) for w, r in pool.items() if w not in score_removed | no_reserve | out}
        order = score(active)
        chosen = set(keep)
        f = sum(active[w]["lop"] == "F" for w in chosen)
        r1 = sum(active[w]["nhan"] == "R1" for w in chosen)
        for w in order:
            if len(chosen) == 7776:
                break
            if w in chosen or w in removed_old:
                continue
            ff, rr = active[w]["lop"] == "F", active[w]["nhan"] == "R1"
            if f + ff > 77 or r1 + rr > 388:
                continue
            chosen.add(w)
            f += ff
            r1 += rr
        assert len(chosen) == 7776 and f <= 77 and r1 == 0
        eligible_words = {r["tu"] for r in eligible}
        reserve_order = [w for w in order if w in eligible_words]
        order_differences = [
            {"position": i, "locked": a["tu"], "rescored": b}
            for i, (a, b) in enumerate(zip(eligible, reserve_order), 1) if a["tu"] != b
        ]
        s4.append({
            "mode": mode, "pool": len(active), "F": f, "R1": r1,
            "new_entry_only": sorted(chosen - selected, key=o1),
            "locked_selection_only": sorted(selected - chosen, key=o1),
            "additional_main_out": sorted((set(d["main"]) - chosen) - out, key=o1),
            "reserve_order_difference_count": len(order_differences),
            "reserve_order_first_differences": order_differences[:12],
            "reserve_order_all_differences": order_differences,
            "assumption": "Chỉ kiểm rổ O87 hiện có; mọi phán quyết H5/H7 của nhánh vẫn có điều kiện.",
        })

    families = [
        r for r in d["spelling_families"]
        if "bít tết" in r["chuan"].split(" / ") and "bíp tết" in r["bien_the"].split(" / ")
    ]
    assert len(families) == 1 and families[0]["ket_luan"] == "QUA_RIENG_H5"
    protected = json.loads((EV / "protected-baseline.json").read_text(encoding="utf-8"))
    changed = [
        p for p, h in protected.items()
        if hashlib.sha256((ROOT / p).read_bytes()).hexdigest() != h["sha256_bytes"]
    ]
    assert not changed, changed
    inputs = [
        U / f"ra-thay-chinh-{n}.{ext}" for n, ext in (
            ("bao-cao-chung", "md"), ("ke-hoach", "md"), ("cau-hoi", "md"),
            ("h7", "tsv"), ("h5", "tsv"), ("thay-the", "tsv"),
        )
    ]
    oe = AT / "ho-so" / "opus" / "ra-thay-chinh" / "evidence"
    inputs += [oe / n for n in ("hop-nhat-rtc.py", "de-xuat-thay-v2.py", "doi-chieu-v2.py")]
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    snapshot = EV / "rd1-input-hashes.json"
    if snapshot.exists():
        assert json.loads(snapshot.read_text(encoding="utf-8")) == hashes, "Draft input changed during review"
    else:
        save_json(snapshot, hashes)
    result = {
        "H7_rows": len(h7), "H7_states": dict(Counter(r["trang_thai"] for r in h7)),
        "H5_rows": len(h5), "H5_states": dict(Counter(r["trang_thai"] for r in h5)),
        "H5_false_pass_count": len(false_pass),
        "current_out": len(out), "current_in": len(incoming), "prepared_spares": len(spares),
        "raw_eligible_reserve": len(eligible),
        "eligible_tiers": dict(Counter(r["tang"] for r in eligible)),
        "remaining_after_87": len(eligible) - len(incoming),
        "unprepared_tail": [r["tu"] for r in eligible[112:]],
        "entrants_order_matches": True, "projected_main_size": len(selected),
        "projected_main_F": 77, "projected_main_R1": 0,
        "A24_vs_first24": {
            "intersection": len(a24 & first24), "A_only": sorted(a24 - first24, key=o1),
            "first24_only": sorted(first24 - a24, key=o1),
        },
        "current_frequency": frequencies,
        "F_fallback_counterexample": counterexample,
        "S4_baseline_exact": True, "S4_O87": s4,
        "bit_tet_registered_family_source": families[0]["_ref"],
        "new_glosses_written": 0, "protected_files_unchanged": len(protected),
        "limits": "Cổng ngữ nghĩa và nghĩa mới chưa khép; phép chiếu 87 không phải nghiệm thu phát hành.",
    }
    save_json(EV / "rd1-audit-summary.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
