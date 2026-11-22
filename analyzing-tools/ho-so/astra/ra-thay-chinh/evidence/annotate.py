"""Ghép phiếu ngôn ngữ độc lập với số đo; không ghi bản phát hành hay câu giải nghĩa."""
import json
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP

from screen_core import AT, BASE, EV, OUT, U, inventory, key, load, o1, ppm, save_json, save_tsv, tsv
from screen_votes import (EXTRA_RARE, H5_EXPLICIT_DIFFERENT, H5_MEASURE, H5_REJECT,
                          H5_REVIEW, H7_HARD, H7_HOLD, H7_SIGN_NO_BLOCK)


def sources():
    out = defaultdict(list)
    for p in sorted(EV.glob("dictionary-*.tsv")):
        for r in tsv(p):
            if r["status"] == "FOUND" and r["has_vietnamese_section"] == "True":
                out[r["tu"]].append(f"{r['_ref']} ({r['url']})")
    return out


def s4(r):
    score = int((Decimal(r["diem"]) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    return (0 if r.get("nhan", "OK") == "OK" else 1, -score, len(key(r["tu"])), o1(r["tu"]))


def h5_rows(d, refs):
    membership = {r["id"]: r for r in tsv(EV / "h5-hnd-membership.tsv")}
    registered = {}
    for r in d["spelling_families"]:
        registered[frozenset((r["chuan"], r["bien_the"]))] = r
    result = []
    for i, raw in enumerate(d["h5"], 1):
        id_ = f"H5-{i:04d}"
        old = registered.get(frozenset((raw["tu"], raw["bien_the"])))
        m = membership[id_]
        family, typ, verdict, action = "-", "-", "KHAC_TU", "KHONG_LOAI_VI_CAP_NAY"
        note = H5_EXPLICIT_DIFFERENT.get(i, "Hai đầu mục khác nghĩa hoặc khác đơn vị từ vựng; phép biến âm tự động không chứng minh là cùng từ.")
        if m["HND74_only_capitalized"] == "True":
            verdict = "TEN_RIENG_BI_HA_CHU"
            note = "Trong HND ghim, dạng kia chỉ có mặt chữ viết hoa; bộ sinh hạ chữ đã làm tên riêng trông như biến thể."
        elif old:
            family = raw["tu"] + "/" + raw["bien_the"]
            typ, verdict, action = old["loai_H5"], "DA_PHAN_XU", "GIU_PHAN_XU_CU"
            note = f"Họ đã đăng ký, kết luận {old['ket_luan']}; không biến cặp thô thành một lỗi mới."
        elif i in H5_REJECT:
            family, typ, note = H5_REJECT[i]
            verdict, action = "DE_NGHI_LOAI_H5C", "DE_NGHI_THAY"
        elif i in H5_MEASURE:
            family, typ, note = H5_MEASURE[i]
            verdict, action = "CUNG_TU_CHO_DO", "CHO_H5_TRUOC_FINAL"
        elif i in H5_REVIEW:
            verdict, action, note = "CHO_XAC_NHAN_QUAN_HE", "HOA_NHAN_DIEN_TRUOC_FINAL", H5_REVIEW[i]
        own, other = d["counts"].get(raw["tu"], {}), d["counts"].get(raw["bien_the"], {})
        result.append({
            "id": id_, "tu": raw["tu"], "khoa": key(raw["tu"]), "bien_the": raw["bien_the"],
            "khoa_bien_the": key(raw["bien_the"]), "ho": family, "loai_H5_de_xuat": typ,
            "ket_qua": verdict, "hanh_dong": action, "ly_do": note,
            "sub_sach_tu": own.get("sub_sach", "CHUA_DO"), "web_sach_tu": own.get("web_sach", "CHUA_DO"),
            "sub_sach_bien_the": other.get("sub_sach", "CHUA_DO"), "web_sach_bien_the": other.get("web_sach", "CHUA_DO"),
            "HND74_only_capitalized": m["HND74_only_capitalized"],
            "bang_chung": ";".join([raw["_ref"], m["_ref"]] + ([old["_ref"]] if old else [])
                                   + refs.get(raw["bien_the"], []) + refs.get(raw["tu"], [])
                                   + (refs.get("chun", []) + refs.get("thun", []) if i in {126,154,155,507} else [])),
            "xac_minh": "verified: số đo/nguồn/tập cặp; assumed: nhận định ngôn ngữ của SA-Astra, chờ soát chéo",
        })
    return result


def assess_h7(d, w, alt, data, refs, id_, source, extra_id=None, registered=False, unmeasured=False):
    k = key(w)
    assert key(alt) == k and w != alt
    gate, level, action = "-", "KHONG_DO", "KHONG_LOAI_VI_CAP_NAY"
    note = "Lượt sàng lọc đầu mục của Astra chưa nhận diện nghĩa đỏ; không suy từ một âm tiết/cụm dài hơn. Đây không phải phép đo nghĩa trên kho."
    own = d["counts"].get(w)
    counter_ppm = None if unmeasured else ppm(data)
    own_ppm = None if own is None else ppm(own)
    force = False
    if registered:
        level, action = "DA_CO_PHAN_XU", "GIU_PHAN_XU_CU"
        note = "Đã có dòng ở bảng cảnh báo lịch sử; không phải một trong 1.177 cặp bỏ sót. Giữ chữ ký cũ, không mở lại cùng lý do."
    elif alt in H7_HARD:
        level, gate, note = H7_HARD[alt]
        action = "DE_NGHI_THAY"
        force = level == "K0" or gate in ("H6.1", "H6.6")
    elif alt == "hùng hổ":
        level, gate, action = "K1", "H6.1/H6.9", "DE_NGHI_THAY"
        note = "Cách đọc đối chứng thể hiện hung hăng; PPM thấp hơn 0,3 nhưng cao hơn mục hững hờ, còi tương đối bật."
        force = True
    elif alt in H7_HOLD:
        level, action, note = "CHO_NGHIA", "CHO_DO_HOA_TRUOC_FINAL", H7_HOLD[alt]
    elif alt in H7_SIGN_NO_BLOCK:
        level, action, note = "K2_DE_NGHI_KHONG_CHAN", "CAN_OPUS_DONG_KY", H7_SIGN_NO_BLOCK[alt]
    elif extra_id in EXTRA_RARE:
        level, gate, action = "K2_DE_NGHI_KHONG_CHAN", EXTRA_RARE[extra_id], "CAN_OPUS_DONG_KY"
        note = "Cách đọc có quan ngại nhưng chứng liệu cả chuỗi thấp; Astra đề nghị không tự động chặn vì hiếm/cổ hoặc phải dựa thêm ngữ cảnh. Chưa phải chữ ký hai bên."
        force = gate in ("H6.1", "H6.6") or alt == "tự ải"
    elif unmeasured and alt in {"áo ngự", "điểm nhãn", "đổ bác", "khuỵ", "khụy", "nghẻo", "nịch"}:
        level, action = "CHO_DO", "CHO_DO_HOA_TRUOC_FINAL"
        note = "Có quan ngại về nghĩa/nhóm đỏ của nguyên mục nhưng không có số đo; CHUA_DO không phải 0, không thể bỏ qua bằng ngưỡng."
        force = alt in {"nịch"}
    elif " ".join(alt.split()) == w:
        level, action = "CUNG_MAT_CHU_KHAC_KHOANG", "KHONG_LA_CACH_DOC_MOI"
        note = "Chỉ khác số dấu cách; không phải nghĩa đỏ hay một cách đọc mới."
    alarm = "CHUA_DO"
    if counter_ppm is not None:
        numeric = counter_ppm >= Decimal("0.3") or own_ppm is not None and counter_ppm >= own_ppm
        alarm = "CO_NEU_NGHIA_DO" if numeric else "KHONG_DAT_NGUONG_SO"
        if force:
            alarm = "BAT_BUOC_K0_HOAC_NHOM_XET_DUOI_NGUONG"
    return {
        "id": id_, "tu_chinh": w, "khoa": k, "doc_khac": alt,
        "sub_sach": data.get("sub_sach", "CHUA_DO"), "web_sach": data.get("web_sach", "CHUA_DO"),
        "ppm_tu_chinh": "CHUA_DO" if own_ppm is None else f"{float(own_ppm):.9f}",
        "ppm_doc_khac": "CHUA_DO" if counter_ppm is None else f"{float(counter_ppm):.9f}",
        "coi": alarm, "nhom_H6": gate, "muc_K_de_xuat": level, "hanh_dong": action,
        "ly_do": note, "nguoi_de_xuat": "SA-Astra", "chu_ky_opus": "CHUA_CO_MOI",
        "bang_chung": ";".join([source, data.get("_ref", "-")] + refs.get(alt, [])),
        "xac_minh": "verified: khóa/số đo/nguồn; assumed: nghĩa, độ tự nhiên và mức K do Astra đề xuất; chưa đo tỷ lệ nghĩa đỏ",
    }


def main():
    d = load()
    inventory(d)
    refs = sources()
    h5 = h5_rows(d, refs)
    save_tsv(OUT / "h5-sang-loc-632.tsv", h5)
    extra_h5 = []
    for i, (w, alt) in enumerate((("xà bông", "xà phòng"), ("xà phòng", "xà bông")), 1):
        own, other = d["counts"][w], d["counts"][alt]
        extra_h5.append({
            "id": f"H5-B{i:03d}", "tu": w, "khoa": key(w), "bien_the": alt,
            "khoa_bien_the": key(alt), "ho": "xà bông/xà phòng", "loai_H5_de_xuat": "f",
            "ket_qua": "CUNG_TU_CHO_DO", "hanh_dong": "CHO_H5_TRUOC_FINAL",
            "ly_do": "Mở đủ họ từ xà bông trong tập gốc: nguồn dẫn tới xà phòng, cả hai đang là chính. Không giữ cả hai nếu xác nhận H5f; số dạng cách không đủ thay phép cộng dạng gạch/viết liền.",
            "sub_sach_tu": own["sub_sach"], "web_sach_tu": own["web_sach"],
            "sub_sach_bien_the": other["sub_sach"], "web_sach_bien_the": other["web_sach"],
            "HND74_only_capitalized": "False",
            "bang_chung": ";".join([own["_ref"], other["_ref"]] + refs.get(w, []) + refs.get(alt, [])),
            "xac_minh": "verified: số dạng cách/nguồn/cả hai đang chính; assumed: quan hệ H5f, chờ soát chéo và đo đủ dạng",
        })
    save_tsv(OUT / "h5-sang-loc-bo-sung.tsv", extra_h5, list(h5[0]))
    oc = {(r["khoa"], r["tu"]): r for r in d["opus-counts"]}
    h7 = []
    for n, r in enumerate(d["h7"], 1):
        c = oc[(r["khoa"], r["doc_khac"])]
        h7.append(assess_h7(d, r["tu_chinh"], r["doc_khac"], c, refs, f"H7-{n:04d}", r["_ref"]))
    save_tsv(OUT / "h7-sang-loc-1177.tsv", h7)
    extra = []
    for n, r in enumerate(tsv(EV / "h7-mo-rong-dau-vao.tsv"), 1):
        c = oc[(r["khoa"], r["doc_khac"])]
        extra.append(assess_h7(d, r["tu_chinh"], r["doc_khac"], c, refs, r["id"], r["_ref"],
                               extra_id=n, registered=r["da_co_coi"] == "True"))
    for r in tsv(EV / "h7-hnd-chua-dem.tsv"):
        extra.append(assess_h7(d, r["tu_chinh"], r["doc_khac"], {}, refs, r["id"], r["_ref"], unmeasured=True))
    save_tsv(OUT / "h7-sang-loc-bo-sung.tsv", extra)
    issue_by_word = defaultdict(list)
    pending = defaultdict(list)
    for r in h5 + extra_h5:
        if r["hanh_dong"] == "DE_NGHI_THAY":
            issue_by_word[r["tu"]].append((r["id"], r["ket_qua"], r["bien_the"]))
        elif r["hanh_dong"] in ("CHO_H5_TRUOC_FINAL", "HOA_NHAN_DIEN_TRUOC_FINAL"):
            pending[r["tu"]].append(r["id"])
    for r in h7 + extra:
        if r["hanh_dong"] == "DE_NGHI_THAY":
            issue_by_word[r["tu_chinh"]].append((r["id"], r["muc_K_de_xuat"], r["doc_khac"]))
        elif r["hanh_dong"] == "CHO_DO_HOA_TRUOC_FINAL":
            pending[r["tu_chinh"]].append(r["id"])
    assert all(w in d["main"] for w in issue_by_word)
    pending_only = {w: v for w, v in pending.items() if w not in issue_by_word}
    out_words = sorted(issue_by_word, key=o1)
    reserve = d["du-phong-phan-loai"]
    a = sorted((r for r in reserve if r["tang"] == "A"), key=s4)
    nonf = [r for r in a if r["lop"] != "F"]
    f = [r for r in a if r["lop"] == "F"]
    replacements = []
    used = set()
    slots = sorted(out_words, key=lambda w: (d["label_by_word"][w]["lop"] == "F", o1(w)))
    for i, w in enumerate(slots, 1):
        label = d["label_by_word"][w]
        candidates = nonf if label["lop"] != "F" else f
        candidate = next((r for r in candidates if r["tu"] not in used), None)
        if candidate:
            used.add(candidate["tu"])
        replacements.append({
            "slot": f"S{i:03d}", "tu_ra": w, "khoa_ra": key(w), "lop_ra": label["lop"],
            "ngan_ra": "OK_F" if label["lop"] == "F" else "OK_KHONG_F",
            "can_cu_loai": ";".join(f"{id_}:{gate}:{alt}" for id_, gate, alt in issue_by_word[w]),
            "quyen_thay": "CHO_OWNER_GIAN" if w == "gián" else "CHO_FINAL_VA_OWNER_DUYET",
            "ung_vien_A_tham_chieu": candidate["tu"] if candidate else "THIEU_NGAN",
            "khoa_vao": candidate["khoa"] if candidate else "-",
            "lop_vao": candidate["lop"] if candidate else "-",
            "F_lich_su": candidate["F"] if candidate else "-",
            "diem_lich_su": candidate["diem"] if candidate else "-",
            "trang_thai_de_cu": "CHUA_TAI_KIEM_H1_H9_CHUA_VIET_SACH_MOI" if candidate else "CAN_NGUON_OK_BO_SUNG",
            "rang_buoc": "Chỉ là ghép ghế minh họa S4 cũ trong A; không ưu tiên tầng thay S4, không phải danh sách xuất bản.",
            "bang_chung": ";".join([label["_ref"]] + ([candidate["_ref"]] if candidate else [])),
            "xac_minh": "verified: khóa/ngăn/điểm lịch sử; assumed: đề nghị thay; chưa có câu mới và D8",
        })
    save_tsv(OUT / "de-xuat-thay-the.tsv", replacements)
    p_rows = [{
        "tu": w, "khoa": key(w), "lop": d["label_by_word"][w]["lop"],
        "ca_cho": ";".join(ids), "trang_thai": "PHAI_HOA_HOAC_DO_TRUOC_FINAL",
        "xac_minh": "assumed: nguy cơ, không tính là lỗi đã chốt",
    } for w, ids in sorted(pending_only.items(), key=lambda x: o1(x[0]))]
    save_tsv(OUT / "cac-tu-cho-phan-xu.tsv", p_rows)
    summary = {
        "base": BASE, "source_text_persisted": False, "production_modified": False,
        "h5_rows": len(h5), "h5_states": Counter(r["ket_qua"] for r in h5),
        "h5_extra_rows": len(extra_h5),
        "h7_rows": len(h7), "h7_states": Counter(r["muc_K_de_xuat"] for r in h7),
        "extra_rows": len(extra), "extra_states": Counter(r["muc_K_de_xuat"] for r in extra),
        "proposed_out_count": len(out_words),
        "proposed_out_by_class": Counter(d["label_by_word"][w]["lop"] for w in out_words),
        "proposed_out_words": out_words,
        "pending_additional_words": len(p_rows),
        "pending_words": [r["tu"] for r in p_rows],
        "A_reference_slots_filled": len(used),
        "A_reference_slots_missing": sum(r["ung_vien_A_tham_chieu"] == "THIEU_NGAN" for r in replacements),
        "reserve_A_non_F": len(nonf), "reserve_A_F": len(f),
        "reserve_non_F_before_new_gates_excluding_D": sum(r["lop"] != "F" and r["tang"] != "D" for r in reserve),
        "owner_forced_word": ["gián"] if "gián" in out_words else [],
        "all_labels_OK": all(d["label_by_word"][w]["nhan"] == "OK" for w in out_words),
        "R1_may_fill_OK_slot": False,
        "new_glosses_written": 0,
    }
    save_json(EV / "screen-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
