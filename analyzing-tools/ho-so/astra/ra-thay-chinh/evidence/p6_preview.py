"""Đo tác động tái tính S2/S3 trước khi khóa plan; không phát hành và không ghi nghĩa."""
import ast
import copy
import json
import unicodedata as UCD
from collections import Counter, defaultdict
from fractions import Fraction

from screen_core import AT, EV, OUT, U, key, load, o1, read, save_json, save_tsv, tsv


def scorer():
    source = read(U / "p6-tinh-doc-lap-astra.py")
    tree = ast.parse(source)
    functions = [x for x in tree.body if isinstance(x, ast.FunctionDef)
                 and x.name in {"risk", "pct", "cents", "score"}]
    ns = {"Counter": Counter, "defaultdict": defaultdict, "Fraction": Fraction,
          "U": UCD, "TONES": "\u0300\u0309\u0303\u0301\u0323", "fold": key, "o1": o1}
    exec(compile(ast.Module(body=functions, type_ignores=[]), "<pure-P6-functions>", "exec"), ns)
    return ns["score"]


def main():
    d = load()
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
        counts = d["counts"][w]
        pool[w] = {"sub_sach": int(counts["sub_sach"]), "web_sach": int(counts["web_sach"]),
                   **small[w], "nhan": r["nhan"], "lop": r["lop"], "phat_h5d": bool(int(r["phat_h5d"]))}
    score = scorer()
    original = copy.deepcopy(pool)
    original_order = score(original)
    mismatch = [r["tu"] for r in d["xep-hang"] if abs(float(original[r["tu"]]["F"]) - float(r["F"])) > 0.000001
                or original[r["tu"]]["diem_x100"] != int(r["diem_100"])]
    assert not mismatch, mismatch[:20]
    assert original_order == [r["tu"] for r in d["xep-hang"]]
    proposed = {r["tu_ra"] for r in tsv(OUT / "de-xuat-thay-the.tsv")}
    candidate_hold = {r["tu"] for r in tsv(OUT / "ung-vien-theo-ngan.tsv") if r["giu_ngoai_hang_de_cu"] == "CO"}
    rejected = {r["tu"] for r in d["du-phong-phan-loai"] if r["tang"] == "D"} | proposed | candidate_hold
    reopened = {r["tu"] for r in d["honorable-mentions"] if r["nhan_ho_so"] == "OK"}
    old_removed = {r["tu"] for r in d["nguon-goc-giai-nghia"] if r["trang_thai"] == "LOAI"}
    # Đây là nhánh có điều kiện: chủ cho phép mở lại HM và đổi quyết định riêng về gián.
    active = {w: r for w, r in pool.items() if w not in rejected and (w not in old_removed or w in reopened)}
    order = score(active)
    keep = set("mặt trời|mặt trăng|trái đất|ngân hà|công chúa|hoàng tử|hoàng hậu|mồ hôi|ruồi|chào cờ|ròng rọc|dép lê|bánh chưng".split("|"))
    assert keep <= active.keys()
    selected = set(keep)
    f = sum(active[w]["lop"] == "F" for w in selected)
    r1 = 0
    for w in order:
        if len(selected) == 7776:
            break
        if w in selected or f + (active[w]["lop"] == "F") > 77 or r1 + (active[w]["nhan"] == "R1") > 388:
            continue
        selected.add(w)
        f += active[w]["lop"] == "F"
        r1 += active[w]["nhan"] == "R1"
    assert len(selected) == 7776 and f <= 77 and r1 == 0
    previous = set(d["main"])
    extra_out = sorted((previous - selected) - proposed, key=o1)
    into = sorted(selected - previous, key=lambda w: order.index(w))
    rows = []
    for w in sorted(previous - selected, key=o1):
        rows.append({"tu": w, "huong": "RA", "ly_do": "H5_H7" if w in proposed else "S4_SAU_TINH_LAI_S2_S3",
                     "F_moi": str(active[w]["F"]) if w in active else "-",
                     "diem_100_moi": active[w]["diem_x100"] if w in active else "-",
                     "xac_minh": "verified: mô phỏng; assumed: quyền HM/gián và các cổng còn chờ, KHONG_PHAT_HANH"})
    for w in into:
        rows.append({"tu": w, "huong": "VAO", "ly_do": "S4_SAU_TINH_LAI_S2_S3",
                     "F_moi": str(active[w]["F"]), "diem_100_moi": active[w]["diem_x100"],
                     "xac_minh": "verified: mô phỏng; assumed: chưa viết sạch mới/chưa đủ chữ ký mới"})
    save_tsv(OUT / "mo-phong-P6-tinh-lai.tsv", rows)
    outgoing = sorted(previous - selected, key=lambda w: (d["label_by_word"][w]["lop"] == "F", o1(w)))
    queue = list(into)
    slot_rows = []
    base_slots = {r["tu_ra"]: r for r in tsv(OUT / "de-xuat-thay-the.tsv")}
    reserve_words = {r["tu"] for r in d["du-phong-phan-loai"]}
    hm_group = {r["tu"]: r["nhom"] for r in d["honorable-mentions"]}
    for i, old in enumerate(outgoing, 1):
        old_class = d["label_by_word"][old]["lop"]
        pick = next(w for w in queue if (active[w]["lop"] == "F") == (old_class == "F"))
        queue.remove(pick)
        p = active[pick]
        slot_rows.append({
            "slot": f"P6-S{i:03d}", "tu_ra": old, "khoa_ra": key(old), "lop_ra": old_class,
            "ly_do_ra": base_slots[old]["can_cu_loai"] if old in base_slots else "S4 sau tính lại S2/S3; không phải phát hiện H5/H7 mới",
            "tu_vao_de_xuat": pick, "khoa_vao": key(pick), "lop_vao": p["lop"],
            "ngan": "OK_F" if p["lop"] == "F" else "OK_KHONG_F",
            "nguon": "HM_" + hm_group[pick] if pick in hm_group else "DU_PHONG",
            "F_moi_phan_so": str(p["F"]), "diem_100_moi": p["diem_x100"],
            "quyen": "CHO_OWNER_GIAN_VA_HM;CHO_FINAL;CHUA_D6_D7_D8_MOI",
            "con_thieu": "Hòa các ca chờ; kiểm H1-H9/P6 hai SA; lượt viết sạch mới, D2/D5/D6/D7/D8; chủ duyệt",
            "xac_minh": "verified: số/ranking có điều kiện; assumed: các giả định chính sách và nghĩa; không phải PASS phát hành",
        })
    assert not queue
    save_tsv(OUT / "de-xuat-thay-the-S4.tsv", slot_rows)
    summary = {
        "baseline_replay_pool": len(pool), "baseline_scores_and_order_exact": True,
        "conditional_active_pool": len(active), "main_size": len(selected), "F": f, "R1": r1,
        "proposed_H5_H7_out": len(proposed),
        "additional_out_by_S4": extra_out,
        "new_selected_count": len(into),
        "new_selected_by_source": Counter("HM" if w in reopened else "DU_PHONG" if w in {r["tu"] for r in d["du-phong-phan-loai"]} else "POOL_KHAC" for w in into),
        "new_words_not_in_candidate_audit": sorted(set(into) - {r["tu"] for r in tsv(OUT / "ung-vien-theo-ngan.tsv")}, key=o1),
        "main_classes": Counter(active[w]["lop"] for w in selected),
        "main_blocks": Counter(len(w.split()) for w in selected),
        "main_mean_letters": sum(len(key(w)) for w in selected)/7776,
        "consumed_reserve": sorted(set(into) & reserve_words, key=o1),
        "promoted_HM": sorted(set(into) & reopened, key=o1),
        "out_words": sorted(previous - selected, key=o1),
        "extra_out_score_details": {w: {
            "old_F": d["rank_by_word"][w]["F"], "new_F": str(active[w]["F"]),
            "old_cents": d["rank_by_word"][w]["diem_100"], "new_cents": active[w]["diem_x100"]
        } for w in extra_out},
        "not_a_release": True,
        "open_main_screening_rows_not_yet_removed": len([r for r in tsv(OUT / "cac-tu-cho-phan-xu.tsv") if r["tu"] in selected]),
        "policy_assumptions": ["owner mở lại HM OK", "owner duyệt thay gián", "các mục đang chờ chưa bị loại trong kịch bản cận dưới"],
    }
    save_json(EV / "p6-preview-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
