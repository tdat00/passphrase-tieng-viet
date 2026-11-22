"""Xác nhận số H5f và đề xuất xử lý các mục mở; không ghi chữ ký phát hành."""
import json

from screen_core import EV, U, save_json, save_tsv, tsv


def main():
    measured = {(r["tu"], r["bien_the"]): r for r in tsv(U / "ra-thay-chinh-h5.tsv")}
    pairs = [("cải xoong", "cải soong"), ("xà bông", "xà phòng"), ("xà phòng", "xà bông")]
    results = []
    for word, alt in pairs:
        r = measured[(word, alt)]
        results.append({
            "tu": word, "doi_chung": alt, "Astra_duyet_2": "NHAN_THAY_H5f",
            "loai_H5": "f", "sub_tu": r["sub_tu"], "sub_doi_chung": r["sub_bien_the"],
            "web_tu": r["web_tu"], "web_doi_chung": r["web_bien_the"],
            "ly_do": "Tổng phụ đề 4 < 20." if word == "cải xoong" else "Không bên nào đạt 95%; kết luận giữ nguyên khi dùng bề mặt hoặc bỏ dòng trùng.",
            "nguon": r["_ref"] + ";analyzing-tools\\ho-so\\astra\\ra-thay-chinh\\evidence\\rd2-audit-summary.json",
            "xac_minh": "Đã tính lại bảng số nguyên, đối chiếu mã/log/hash; không tái tải/đếm corpus. Không phải D6/D7 hay phê duyệt thay.",
        })
    save_tsv(EV / "rd2-H5-xac-nhan.tsv", results)
    remaining7 = [r for r in tsv(U / "ra-thay-chinh-h7.tsv") if r["trang_thai"] == "TRANH_CHAP"]
    assert len(remaining7) == 17 and all(r["astra"] == "K1" and r["opus"] == "K2" for r in remaining7)
    save_tsv(EV / "rd2-H7-bao-luu.tsv", [
        {"tu": r["tu_chinh"], "khoa": r["khoa"], "Astra_duyet_2": "BAO_LUU_K1",
         "nguon_hien_hanh": r["_ref"], "nguon_ly_do_Astra": r["nguon_astra"],
         "phai_gui": "Q-rtc-S1; xin phán từng khóa trong luật hiện hành, không xin ngưỡng mới"}
        for r in remaining7
    ])
    remaining5 = [r for r in measured.values() if r["trang_thai"] == "TRANH_CHAP"]
    assert len(remaining5) == 7
    save_tsv(EV / "rd2-H5-bao-luu.tsv", [
        {"tu": r["tu"], "doi_chung": r["bien_the"], "Astra_duyet_2": "BAO_LUU_CHO_LOAI",
         "nguon_hien_hanh": r["_ref"], "nguon_ly_do_Astra": r["nguon_astra"],
         "phai_gui": "Q-rtc-S2; giữ phân biệt cùng nghĩa, cùng từ và cách viết chuẩn/lỗi"}
        for r in remaining5
    ])
    flagged = {r["tu"]: r for r in tsv(U / "ra-thay-chinh-thay-the.tsv") if r["vai_tro"] in {"VAO", "DU_BI"} and r["can_soat"] != "-"}
    proposals = [
        ("đưa đò", "dưa đỏ", "KHONG_DO", "Tên quả, không suy nghĩa đỏ từ âm tiết đỏ."),
        ("nặng cân", "lặng câm", "KHAC_TU", "Khác hình vị và nghĩa toàn cụm; không lập họ chỉ từ phép sinh biến thể."),
        ("thẳng đơ", "thang độ", "KHONG_DO", "Khái niệm thang/mức độ không tự là y khoa chuyên biệt hay nhóm đỏ khác."),
    ]
    save_tsv(EV / "rd2-de-xuat-dong-co.tsv", [
        {"tu": w, "doi_chung": alt, "Astra_de_xuat": state, "ly_do": why,
         "nguon_co": flagged[w]["_ref"], "trang_thai": "DE_NGHI_DONG_RIENG_CO; CHO_OPUS_XAC_NHAN; khong chung nhan toan tu"}
        for w, alt, state, why in proposals
    ])
    save_json(EV / "rd2-decision-summary.json", {
        "H5f_confirmed_replace": [p[0] for p in pairs],
        "H7_disputed": 17, "H5_disputed": 7,
        "agreed_out_after_H5f_confirmation": 94,
        "O_proposed_out_unchanged": 101,
        "existing_K2_to_reuse": ["nướng", "phết"],
        "new_K2_signature_queue": 194,
        "entrant_flag_closure_proposals": [p[0] for p in proposals],
        "open_items_can_be_worked_jointly": True,
        "no_promise_all_pending_items_will_pass": True,
        "new_release_signatures_written": 0,
    })
    print("Confirmed 3 H5f exclusions; retained 17 H7 and 7 H5 disputes; proposed 3 individual flag closures.")


if __name__ == "__main__":
    main()
