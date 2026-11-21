"""Kết hợp số liệu đã đo với phiếu độc lập Astra; không viết hay sao chép giải nghĩa."""
import json
from collections import Counter, defaultdict

from inventory import (EV, INPUTS, OUT, ROOT, UNIFIED, basic, key, load, o1,
                       save_json, save_tsv, tsv)

OMIT_GLOSS_WORDS = {
    "cơ quan": "assumed:để ngoài đợt đề cử vì cần rà riêng nghĩa cơ quan nhà nước; không kết luận loại cứng.",
    "lực lượng": "assumed:để ngoài vì có liên tưởng phổ biến quân sự; không chọn nghĩa lành để tự cho qua H6.",
    "truy tìm": "assumed:để ngoài vì cần phân định ngữ cảnh tố tụng và tìm kiếm thường ngày.",
    "dự bị": "assumed:để ngoài vì cần phân định nghĩa quân sự với thể thao.",
    "lên chức": "assumed:để ngoài vì cần phân định công việc thông thường với quyền lực nhà nước.",
}


def two_signatures(data, word):
    signatures = defaultdict(set)
    for r in data["signatures"][word]:
        if r["hieu_luc"] == "CO":
            signatures[r["loai_ky"]].add(r["nguoi_ky"])
    return sorted(kind for kind, people in signatures.items() if {"Astra", "Opus"} <= people)


def final_h9_refs(data):
    by_word = {}
    for name in ("p6-dau-vao", "l2-nhan", "l2b-nhan", "l2c-nhan", "l3-nhan"):
        for r in data[name]:
            by_word[r["tu"]] = r["_ref"]
    return by_word


def evidence_row(word, data, h9refs):
    r = basic(word, data)
    signatures = two_signatures(data, word)
    assert r["h1"] and r["h2_so_hoc"] and not r["trung_khoa"]
    assert not r["blocked"] and not r["h5a"], word
    for family in data["spelling_by_word"][word]:
        conclusion = family["ket_luan"]
        assert not conclusion.startswith("LOAI"), (word, conclusion)
        assert not conclusion.startswith("CHO") or (
            "THIEU_DU_LIEU" in conclusion and "H5" in signatures), (word, conclusion)
        standard = [s.strip() for s in family["chuan"].split("/")]
        variants = [s.strip() for s in family["bien_the"].split("/")]
        assert word not in variants or word in standard, (word, "BIEN_THE_THUA")
    lexical = any(m in r["h3_nguon"] for m in ("WVI:LEX", "WEN:LEX", ",en", ",vi")) or r["h3_nguon"] in ("en", "vi")
    assert lexical or "H3" in signatures, (word, "THIEU_H3", r["h3_nguon"])
    if r["h8_so_hoc"] == "ZERO":
        assert "H8" in signatures, (word, "THIEU_H8")
    if key(word) in data["rules"]["danh_sach"]["k2_de_nghi_khoa"]:
        assert "K2" in signatures, (word, "K2_CHUA_KY")
    assert word in h9refs, (word, "THIEU_H9_LICH_SU")
    r.update({
        "ngan": r["nhan"] + ("_F" if r["lop"] == "F" else "_KHONG_F"),
        "H1": "verified:đạt NFC, chữ Việt viết thường, một dấu cách",
        "H2": "verified:đạt số chữ và khối; "
              + ("assumed:danh từ cố định ba khối theo hồ sơ" if r["so_khoi"] == 3 else "không có ba khối"),
        "H3": "verified:hồ sơ có chứng cứ từ vựng" if lexical else "verified:chỉ wordlist; đủ hai chữ ký H3",
        "H4": "verified:khóa khác chính và dự phòng, kể cả viết hoa đầu",
        "H5": "verified:không trúng H5a/họ cấm/biến thể thua; "
              + ("ngoại lệ H5 có hai chữ ký" if "H5" in signatures else
                 "họ đã đo=" + (r["h5_ho"] or "không trúng"))
              + "; assumed:chưa phát hiện họ mới",
        "H6": "verified:nhãn nhận trong hồ sơ cũ; assumed:nhận định nghĩa toàn mục của Astra ở cột đánh giá",
        "H7": "verified:không trúng bảng khóa chặn; "
              + ("K2 đủ hai chữ ký" if "K2" in signatures else "không có K2 mở trong hồ sơ kiểm"),
        "H8": "verified:" + r["h8_so_hoc"]
              + ("; ngoại lệ không-lượt đủ hai chữ ký" if r["h8_so_hoc"] == "ZERO" else
                 "; đã có đọc kiểm trong phiếu P4" if r["h8_so_hoc"] == "YEU" else
                 "; đây là mức số học, không đo nghĩa đỏ"),
        "H9": "verified:đã qua H9 lịch sử; assumed:chờ chữ ký review chéo đợt này",
        "chu_ky_hai_ben_da_doi": ";".join(signatures),
        "H9_ref": h9refs[word],
        "tinh_chat_so_do": "verified:số lưu trong repo, chưa đếm lại kho; F là điểm, không phải tần suất",
    })
    return r


def d7_for_version(data, word, version):
    result = []
    for r in data["reviews"][word]:
        filename = r["_ref"].rsplit("\\", 1)[-1]
        v = "v3" if "-v3-" in filename else "v2" if "-v2-" in filename else "v1"
        if v == version:
            result.append(r)
    return result


def main():
    data = load()
    h9refs = final_h9_refs(data)
    judgements = tsv(EV / "reserve-judgements.tsv")
    assert len(judgements) == 205 and [r["tu"] for r in judgements] == data["reserve"]
    assert data["reserve"] == sorted(data["reserve"], key=o1)
    reserve_rows = []
    for j in judgements:
        word = j["tu"]
        r = evidence_row(word, data, h9refs)
        r["tang"] = j["tang"]
        r["danh_gia_moi"] = "assumed:" + j["danh_gia_moi"]
        r["rui_ro_can_luu_y"] = "assumed:" + j["rui_ro_can_luu_y"]
        r["thay_ngan"] = "OK_F→OK_F" if r["lop"] == "F" else "OK_KHONG_F→OK_KHONG_F (C/H/K)"
        r["uu_tien_lop"] = "assumed:ưu tiên cùng lớp " + r["lop"] + "; không phải hạn mức mới"
        if j["tang"] == "B":
            assert word not in data["gloss"]
            r["D6_D7"] = "verified:chưa từng có lượt viết; không có PASS để kế thừa"
            r["thieu_truoc_thay"] = "Lượt viết sạch mới; D2/D5/D6/D7; D8; review chéo; kiểm bộ thay thế"
            r["D7_ref"] = ""
        else:
            assert r["d6_result"] == "PASS" and int(r["d6_match_n"]) == 1
            reviews = d7_for_version(data, word, r["d6_version"])
            assert reviews and not any(x["muc_do"] == "CHAN" for x in reviews), word
            r["D6_D7"] = "verified:D6 token-hash khớp PASS và có D7 đúng lượt, không CHAN; chưa chạy D6 mới"
            r["D7_ref"] = ";".join(x["_ref"] for x in reviews)
            r["thieu_truoc_thay"] = "D8 cho đúng câu/lượt; review chéo; kiểm D2/D5 toàn tập thay thế; P6 và C1–C8"
            if j["tang"] == "C":
                r["thieu_truoc_thay"] = "Thống nhất điểm yếu/sắc thái trước khi ưu tiên; " + r["thieu_truoc_thay"]
        reserve_rows.append(r)

    r1picks = tsv(EV / "honorable-r1-picks.tsv")
    assert len(r1picks) == 73
    gloss_words = [w for w, row in data["excluded"].items()
                   if row["cong_loai"].startswith(("D6_", "D7_")) and w not in OMIT_GLOSS_WORDS]
    assert len(gloss_words) == 127
    picks = {r["tu"]: r for r in r1picks}
    assert len(picks) == 73 and not set(picks) & set(gloss_words)
    hm_rows = []
    for word in sorted(gloss_words + list(picks), key=o1):
        r = evidence_row(word, data, h9refs)
        assert word not in set(data["main"] + data["reserve"])
        if word in picks:
            assert r["nhan"] == "R1"
            r.update({
                "tang": "HM_R1",
                "danh_gia_moi": "assumed:" + picks[word]["ly_do_de_cu"],
                "chu_de": "assumed:" + picks[word]["chu_de"],
                "vi_sao_chua_chon": "verified:R1 đứng sau OK; danh sách chính không có R1, không phải thiếu điểm đơn thuần",
                "thay_ngan": "verified:chưa có ghế hợp lệ; R1 chỉ thay R1, hiện có 0",
                "thieu_truoc_thay": "Không tự nâng R1 thành OK; chỉ xét lại khi có bằng chứng/phiên bản được duyệt; viết sạch và D6/D7/D8 nếu về sau được chọn",
            })
        else:
            assert r["nhan"] == "OK"
            old = data["excluded"][word]
            r.update({
                "tang": "HM_D6" if old["cong_loai"].startswith("D6") else "HM_D7",
                "danh_gia_moi": "assumed:đầu mục lành, đáng cân nhắc vì nhãn OK và chứng liệu; không phục hồi câu đã bị loại",
                "chu_de": "assumed:đa dạng theo lớp " + r["lop"],
                "vi_sao_chua_chon": "verified:bị khấu trừ " + old["cong_loai"]
                                     + "; không phải từ hiếm hoặc thua P5",
                "thay_ngan": "OK_F→OK_F" if r["lop"] == "F" else "OK_KHONG_F→OK_KHONG_F (C/H/K)",
                "thieu_truoc_thay": "Chưa được tự mở lượt viết lại vượt giới hạn D7; cần phép riêng nếu khôi phục, rồi viết sạch D6/D7/D8 và kiểm bộ thay thế",
            })
        r["D6_D7"] = "verified:không có câu được duyệt cho lần đề cử này; không chép câu cũ"
        hm_rows.append(r)
    assert len(hm_rows) == 200 and len({key(r["tu"]) for r in hm_rows}) == 200
    assert not {r["khoa"] for r in hm_rows} & {key(w) for w in data["main"] + data["reserve"]}

    preferred = [
        "tu", "khoa", "tang", "nhan", "lop", "ngan", "so_chu", "so_khoi",
        "thay_ngan", "uu_tien_lop", "danh_gia_moi", "rui_ro_can_luu_y", "chu_de",
        "vi_sao_chua_chon", "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9",
        "D6_D7", "thieu_truoc_thay", "chu_ky_hai_ben_da_doi",
        "nguon_pool", "nguon_de_cu", "h3_nguon", "h8_so_hoc",
        "sub_be_mat", "web_be_mat", "sub_sach", "web_sach", "leipzig", "tatoeba",
        "F", "G", "T", "diem", "hang_lich_su", "vao_lich_su", "tinh_chat_so_do",
        "gloss_sha256", "d6_token_sha256", "d6_version",
        "nhan_ref", "rank_ref", "nguon_dong", "dem_sach_dong", "chu_ky_ref",
        "h5_ref", "p4_ref", "H9_ref", "gloss_ref", "d6_ref", "D7_ref", "loai_ref",
    ]
    save_tsv(OUT / "du-phong-phan-loai.tsv", preferred, reserve_rows)
    save_tsv(OUT / "honorable-mentions.tsv", preferred, hm_rows)

    excluded_rows = []
    for word, row in data["excluded"].items():
        if word in set(gloss_words):
            continue
        excluded_rows.append({
            "tu": word, "khoa": row["khoa"],
            "ly_do": OMIT_GLOSS_WORDS.get(word, "verified:khấu trừ cổng cứng " + row["cong_loai"]),
            "nguon": row["_ref"],
        })
    excluded_rows.append({
        "tu": "hạ lưu", "khoa": "haluu",
        "ly_do": "assumed:Astra không đề cử do nghĩa miệt thị người của đúng nguyên mục; không dùng nghĩa địa lý để làm sạch",
        "nguon": data["rank_by_word"]["hạ lưu"]["_ref"],
    })
    for word in ("bộ giải mã", "bộ chuyển đổi", "thảm thực vật", "khung gầm"):
        excluded_rows.append({
            "tu": word, "khoa": key(word),
            "ly_do": "verified:chưa tìm đủ hai chữ ký H3 trong chu-ky.tsv thống nhất; assumed:để ngoài đợt đề cử, chưa kết luận thiếu trong mọi hồ sơ L2",
            "nguon": data["by_word"][word]["nguon_dong"],
        })
    save_tsv(EV / "candidate-exclusions.tsv", ["tu", "khoa", "ly_do", "nguon"],
             sorted(excluded_rows, key=lambda x: o1(x["tu"])))

    slots = []
    serial = Counter()
    keep = set(data["rules"]["danh_sach"]["chu_giu"])
    available = Counter(data["labels_by_word"][w]["lop"] for w in data["main"] if w not in keep)
    for row in reserve_rows:
        c = row["lop"]
        serial[c] += 1
        assert serial[c] <= available[c]
        slots.append({
            "tu_du_phong": row["tu"], "tang": row["tang"], "nhan": row["nhan"],
            "lop": c, "ghe_gia_dinh": f"OK_{c}_{serial[c]:03}",
            "y_nghia": "verified:ghế tượng trưng riêng biệt; không chỉ định xóa từ chính nào",
        })
    save_tsv(EV / "substitution-slots.tsv",
             ["tu_du_phong", "tang", "nhan", "lop", "ghe_gia_dinh", "y_nghia"], slots)

    summary = {
        "reserve_tiers": dict(Counter(r["tang"] for r in reserve_rows)),
        "reserve_tier_compartments": dict(Counter(r["tang"] + "_" + r["ngan"] for r in reserve_rows)),
        "reserve_tier_words_C": [r["tu"] for r in reserve_rows if r["tang"] == "C"],
        "hm_n": len(hm_rows),
        "hm_tiers": dict(Counter(r["tang"] for r in hm_rows)),
        "hm_classes": dict(Counter(r["lop"] for r in hm_rows)),
        "hm_compartments": dict(Counter(r["ngan"] for r in hm_rows)),
        "hm_sources": dict(Counter(r["nguon_pool"] for r in hm_rows)),
        "hm_h8": dict(Counter(r["h8_so_hoc"] for r in hm_rows)),
        "hm_h3_two_signatures": [r["tu"] for r in hm_rows if "H3" in r["chu_ky_hai_ben_da_doi"].split(";")],
        "hm_k2_two_signatures": [r["tu"] for r in hm_rows if "K2" in r["chu_ky_hai_ben_da_doi"].split(";")],
        "hm_F_score_range": [min(float(r["F"]) for r in hm_rows), max(float(r["F"]) for r in hm_rows)],
        "reserve_d6_versions": dict(Counter(r.get("d6_version") or "CHUA_VIET" for r in reserve_rows)),
        "substitution_slots": dict(serial),
        "available_main_slots_excluding_owner_keep": dict(available),
        "rule_new_hard_rejections": 0,
        "meaning": "verified:số đếm và đối chiếu; assumed:tầng mới, độ quen và nhận định nghĩa của riêng Astra; không là phê duyệt thay từ",
    }
    save_json(EV / "classification-summary.json", summary)
    save_json(EV / "classification-inputs.json", INPUTS)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
