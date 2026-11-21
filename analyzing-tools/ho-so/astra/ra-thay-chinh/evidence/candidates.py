"""Đề cử theo từng ngăn, có nhánh xin mở lại HM; không giả định đã qua D6/D7 mới."""
import json
from collections import Counter

from annotate import s4
from screen_core import EV, OUT, key, load, o1, save_json, save_tsv, tsv

HOLD_H5 = {
    "loằng ngoằng": "T-dpv2-4 còn chờ họ loằn ngoằn.",
    "rướn": "Dạng dướn có trong HND; cần xác nhận cùng từ và đo.",
    "xoành xoạch": "Cần phân biệt xành xạch/xoàn xoạt với cùng từ, không dùng phép sinh làm phán quyết.",
    "loáng thoáng": "Cần phân biệt loáng choáng với cùng từ.",
}
HOLD_H7 = {
    "ngoại trừ": "Giữ CHO_H7 theo T-dpv2-9, không mở OI riêng nếu không chọn.",
    "làm cỗ": "làm cỏ có nghĩa bóng bạo lực trong enwiktionary; PPM cả chuỗi không phải tỷ lệ nghĩa đó.",
    "kịch": "kích có nghĩa vũ khí và dụng cụ nâng; cần hòa H7 trước đề cử.",
    "vuông": "vương có nghĩa tước vị lịch sử/tên riêng; cần hòa H7.",
    "vận hành": "vạn hạnh có khả năng nghĩa tín ngưỡng và tên riêng; cần hòa H7.",
    "ngắn gọn": "ngả ngớn/ngả ngốn cần nguồn xác nhận loại nghĩa, không tự lập K0.",
}
HOLD_H6 = {"cơ quan", "lực lượng", "truy tìm", "dự bị", "lên chức"}
K2_REVIEW = {
    "chữ hoa": "chủ hoà", "cơ quan": "cô quân", "hóng chuyện": "hồng chuyên",
    "mình": "mịnh", "tâm sự": "tam sự", "vậy nên": "vảy nến",
}


def main():
    d = load()
    slots = tsv(OUT / "de-xuat-thay-the.tsv")
    candidates = []
    sources = []
    for r in d["du-phong-phan-loai"]:
        if r["tang"] != "D":
            sources.append((r, "DU_PHONG_" + r["tang"], False))
    for r in d["honorable-mentions"]:
        if r["nhan_ho_so"] == "OK":
            sources.append((r, "HM_" + r["nhom"], True))
    blocked = {r["khoa"] for r in d["blocked_keys"]} | {"baotu"}
    main_keys = set(d["main_by_key"])
    h5_by = Counter(r["tu"] for r in tsv(EV / "ung-vien-doi-chung-H5.tsv"))
    h7_by = Counter(r["tu"] for r in tsv(EV / "ung-vien-doi-chung-H7.tsv"))
    for r, group, needs in sources:
        w = r["tu"]
        assert 4 <= len(key(w)) <= 12 and 1 <= len(w.split()) <= 3
        assert key(w) == r["khoa"] and key(w) not in main_keys and key(w) not in blocked
        hold = ";".join(x[w] for x in (HOLD_H5, HOLD_H7) if w in x)
        if w in HOLD_H6:
            hold += (";" if hold else "") + "T-dpv2-8: rà H6 trước khi dùng; không tự hủy quyết định giữ HM."
        row = {
            "tu": w, "khoa": key(w), "nhom": group, "nhan": "OK", "lop": r["lop"],
            "ngan": "OK_F" if r["lop"] == "F" else "OK_KHONG_F",
            "F": r["F"], "diem": r["diem"],
            "diem_100": d["rank_by_word"].get(w, {}).get("diem_100", "-"),
            "H5_cap_can_doc": h5_by[w], "H7_cap_can_doc": h7_by[w],
            "giu_ngoai_hang_de_cu": "CO" if hold else "KHONG",
            "ly_do_cho": hold or "-",
            "K2_can_soat_chu_ky": K2_REVIEW.get(w, "-"),
            "can_owner_mo_luot_sach_HM": "CO" if needs else "KHONG",
            "trang_thai_nghia_moi": "CHUA_VIET",
            "D8_moi": "CHUA_CO",
            "bang_chung": r["_ref"],
            "xac_minh": "verified: số/khóa/nhãn lịch sử; assumed: đề cử, chưa ký H1-H9/P6/P7 mới",
        }
        candidates.append(row)
    candidates.sort(key=s4)
    save_tsv(OUT / "ung-vien-theo-ngan.tsv", candidates)
    eligible = [r for r in candidates if r["giu_ngoai_hang_de_cu"] == "KHONG"]
    reserve = [r for r in eligible if r["can_owner_mo_luot_sach_HM"] == "KHONG"]
    used = set()
    by_slot = []
    for slot in slots:
        source = [r for r in eligible if (r["lop"] == "F") == (slot["lop_ra"] == "F") and r["tu"] not in used]
        assert source, slot["slot"]
        pick = source[0]
        used.add(pick["tu"])
        row = {k: v for k, v in slot.items() if not k.startswith("_")}
        row.update({
            "ghi_chu_ung_vien_A": next((r["ly_do_cho"] for r in candidates if r["tu"] == slot["ung_vien_A_tham_chieu"]), "THIEU_NGAN"),
            "ung_vien_neu_owner_duyet_HM": pick["tu"],
            "nguon_ung_vien_HM": pick["nhom"],
            "khoa_vao_HM": pick["khoa"],
            "lop_vao_HM": pick["lop"],
            "diem_HM_lich_su": pick["diem"],
            "quyen_mo_luot_HM": "CHUA_DUOC_OWNER_DUYET" if pick["can_owner_mo_luot_sach_HM"] == "CO" else "KHONG_CAN_MO_LAI_HM",
            "rang_buoc_HM": "Phải chốt H1-H9, tính lại S2/S3/S4 và viết sạch mới; đây là thứ tự tham chiếu, không phải PASS/phát hành.",
        })
        by_slot.append(row)
    save_tsv(OUT / "de-xuat-thay-the.tsv", by_slot)
    for category, pool in (("current_reserve", reserve), ("with_HM_permission", eligible)):
        assert len({r["khoa"] for r in pool}) == len(pool)
    projected = [w for w in d["main"] if w not in {r["tu_ra"] for r in slots}] + [r["ung_vien_neu_owner_duyet_HM"] for r in by_slot]
    assert len(projected) == len(set(projected)) == len({key(w) for w in projected}) == 7776
    labels = d["label_by_word"] | {r["tu"]: r for r in candidates}
    classes = Counter(labels[w]["lop"] for w in projected)
    assert classes["F"] == 77
    assert all(labels[w]["nhan"] == "OK" for w in projected)
    nonf_slots = sum(r["lop_ra"] != "F" for r in slots)
    result = {
        "candidate_rows": len(candidates),
        "held_candidates": [r["tu"] for r in candidates if r["giu_ngoai_hang_de_cu"] == "CO"],
        "reserve_eligible_before_final_signatures": Counter(r["ngan"] for r in reserve),
        "HM_eligible_before_owner_and_signatures": Counter(r["ngan"] for r in eligible if r not in reserve),
        "nonF_slots": nonf_slots,
        "current_reserve_nonF_shortfall": max(0, nonf_slots - sum(r["lop"] != "F" for r in reserve)),
        "slots_if_HM_permission": len(by_slot),
        "nominal_new_words_by_source": Counter(r["nguon_ung_vien_HM"] for r in by_slot),
        "nominal_main_classes": classes, "nominal_F": classes["F"], "nominal_R1": 0,
        "nominal_H1_H2_numeric_H4": True,
        "new_P6_S2_S3_computed": False,
        "new_glosses_written": 0,
        "D6_D7_D8_new": "CHUA_KIEM",
    }
    save_json(EV / "candidate-summary.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
