"""H7 (và K0) cho danh sách chính: sàng lọc các cách đọc không dấu cùng khóa, ghi đề xuất của Opus.

    python sang-loc-h7.py  ->  ../sang-loc-h7.tsv, sang-loc-h7.log

Nguồn cặp (chỉ đọc):
- PHAM_VI: 1.177 cặp ≥ 0,3 PPM gộp chưa có trong canh-bao-khong-dau.tsv (du-phong-v2/evidence/pham-vi-hau-kiem-h7.tsv);
- DUOI_NGUONG: cặp DOC_KHAC < 0,3 PPM của khóa chính (opus-counts.tsv) chứa từ/cụm về tự hại, bạo lực, tình dục rõ,
  chất thải (luật H7: xét cả dưới mốc);
- HND_THIEU: cặp cùng khóa trong HND mà DOC_KHAC không có (h7-hnd-cung-khoa.tsv).
Luật đề xuất (giả định của Opus, xem round-1-analysis.md mục 5.2):
- K0: cách đọc là từ tục, tình dục người lớn hoặc chỉ chất thải, có nguồn chứng thực (H7 K0), bất kể tần suất.
- K1: khóa nhiều âm tiết; cách đọc là từ có thật mà nghĩa chính thuộc nhóm đỏ H6; r = PPM(đọc khác)/PPM(từ chính) ≥ 0,2
  (mốc neo theo tiền lệ bào tử/báo tử r = 0,23 → K1). GIAP_RANH: nhóm đỏ dựa trên cách đọc chặt bảng ví dụ H6.
- K2: khóa một âm tiết, cụm phải tách ép, nghĩa đỏ không chắc, hoặc r < 0,2. Cần hai chữ ký "không tự động chặn".
- KHONG_DO: cách đọc không thuộc nhóm đỏ H6.
"""
import collections
import re

from chung import *

SUB0, WEB0 = SUB_TOKENS, WEB_TOKENS
K1_RO = {  # (từ chính, cách đọc khác): nhóm H6
    ("sắn dây", "sán dây"): "G5,G10", ("chữ nghĩa", "chủ nghĩa"): "G3", ("tài hoa", "tai họa"): "G8",
    ("tài hoa", "tai hoạ"): "G8", ("giận dỗi", "gian dối"): "G9", ("đầu mùa", "đậu mùa"): "G5",
    ("lằng nhằng", "lăng nhăng"): "G6", ("hố ga", "ho gà"): "G5", ("thư thái", "thụ thai"): "G6",
    ("bàn ăn", "bản án"): "G2", ("thiên tài", "thiên tai"): "G8", ("nằm mơ", "nấm mồ"): "G4",
    ("áo quần", "áo quan"): "G4", ("thong dong", "thông đồng"): "G2", ("đỏ thắm", "do thám"): "G1,G2",
    ("dặn dò", "dẫn độ"): "G2", ("đậm đà", "đấm đá"): "G1",
}
K1_GR = {
    ("chung cư", "chứng cứ"): "G2", ("phong thư", "phòng thủ"): "G1", ("phân công", "phản công"): "G1",
    ("tiền công", "tiến công"): "G1", ("tiếp viên", "tiếp viện"): "G1", ("cổ thụ", "cố thủ"): "G1",
    ("nắm vững", "nằm vùng"): "G1,G3", ("thể lực", "thế lực"): "G3", ("gầy gò", "gây gổ"): "G1,G9",
    ("dò hỏi", "dở hơi"): "G9", ("hóm hỉnh", "hợm hĩnh"): "G9", ("cao giá", "cáo già"): "G9",
    ("mê mẩn", "mê man"): "G5", ("di dời", "đi đời"): "G4",
}
K2_MULTI = {  # (từ chính, cách đọc khác): (nhóm, lý do nếu không phải chỉ vì r < 0,2)
    ("bố mẹ", "bỏ mẹ"): ("G9", ""), ("bảo hành", "bạo hành"): ("G1,G2", ""), ("báo động", "bạo động"): ("G1", ""),
    ("đánh bại", "đánh bài"): ("G7", ""), ("bạn thân", "bán thân"): ("G6", "nghĩa đỏ không chắc: thường là tượng bán thân"),
    ("bản đồ", "ban đỏ"): ("G5", ""), ("đa năng", "đa nang"): ("G5", ""), ("đột phá", "đốt phá"): ("G1", ""),
    ("bền bỉ", "bên bị"): ("G2", "cụm ghép tình cờ, ít dùng"), ("họ hàng", "hở hang"): ("G6", ""),
    ("chứng nhận", "chứng nhân"): ("G2", "dạng hiếm của nhân chứng"), ("quà tặng", "quả tang"): ("G2", "chỉ dùng trong bắt quả tang"),
    ("sân ga", "sa ngã"): ("G6,G9", "nghĩa đỏ không chắc: sa ngã là sa vào thói xấu nói chung"), ("cổ vũ", "có vú"): ("G6", "cụm tách ép; chủ yếu là động vật có vú"),
    ("mặt nước", "mất nước"): ("G3,G5", "nghĩa đỏ không chắc: mất nước thường là thiếu nước"),
    ("ngụ ý", "ngụy"): ("G3", "đọc khóa hai âm tiết thành một âm tiết; ngụy đứng riêng chủ yếu đi trong từ ghép"), ("ngụ ý", "nguỵ"): ("G3", "như ngụy, cách đặt dấu cũ"), ("chú ý", "chuỳ"): ("G1", ""),
    ("ăn may", "ăn mày"): ("G9", "nghĩa đỏ không chắc: chỉ người hành khất, chỉ là lời chê khi dùng mắng"),
    ("cắm đầu", "cầm đầu"): ("G2", "nghĩa đỏ không chắc: cầm đầu nghĩa chung là đứng đầu"),
    ("bộ ba", "bỏ bà"): ("G9", "tiếng cảm thán, phải ghép với chết"), ("hâm mộ", "hầm mộ"): ("G4", ""),
    ("hỏi thăm", "hội thẩm"): ("G2", ""), ("liên quan", "liên quân"): ("G1", ""), ("phòng ngủ", "phòng ngự"): ("G1", ""),
    ("thị trường", "thị trưởng"): ("G3", "nghĩa đỏ không chắc: chức danh hành chính"), ("cộng sự", "công sự"): ("G1", ""),
    ("nằm mơ", "nam mô"): ("G4", "đi kèm K1 nấm mồ của cùng khóa"), ("bộ đồ", "bợ đỡ"): ("G9", ""),
    ("ca nhạc", "cà nhắc"): ("G5", "nghĩa đỏ không chắc: tả dáng đi, không phải tên bệnh"), ("hoa mai", "hoả mai"): ("G1", "vũ khí cổ, hiếm"),
    ("hoang đảo", "hoàng đạo"): ("G4", "nghĩa đỏ không chắc: chiêm tinh"),
    ("đồ bạc", "đổ bác"): ("G7", "từ Hán Việt cũ chỉ cờ bạc, rất hiếm; chưa đo"),
}
K2_SINGLE = {  # cách đọc khác (khóa một âm tiết): nhóm H6
    "binh": "G1", "bịnh": "G5", "chiến": "G1", "địch": "G1", "dịch": "G5", "giặc": "G1", "trận": "G1", "tướng": "G1",
    "khiên": "G1", "chùy": "G1", "nòng": "G1", "giam": "G2", "gông": "G2", "còng": "G2", "kiện": "G2", "trảm": "G2",
    "trói": "G2", "trừng": "G2", "chôn": "G4", "lăng": "G4", "vong": "G4", "thần": "G4", "tịch": "G4", "tụng": "G2,G4",
    "trối": "G4", "thiêu": "G4", "điếu": "G4,G7", "khấn": "G4", "nguyện": "G4", "ngải": "G4", "khuẩn": "G5",
    "nhọt": "G5", "niệu": "G5", "chàm": "G5", "ngất": "G5", "ngạt": "G5", "tiêm": "G5", "nạng": "G5", "sảng": "G5",
    "thọt": "G5", "chột": "G5", "thai": "G6", "thải": "G5", "háng": "G6", "liếm": "G6", "ngốc": "G9", "nhãi": "G9",
    "thằng": "G9", "mắng": "G9", "thối": "G10", "khắm": "G10", "giòi": "G10", "khạc": "G10", "sòng": "G7",
    "quyền": "G3", "triều": "G3", "ngập": "G8", "quái": "G4", "ngáo": "G7,G9", "nhậu": "G7", "cược": "G7",
    "ngủm": "G4", "ngứa": "G5", "nguyền": "G4", "thây": "G4", "trôn": "G6", "truồng": "G6", "cuồng": "G5",
    "cưỡng": "G2,G6", "hung": "G1", "rạch": "G1", "thẹo": "G5", "trẫm": "G3", "chôm": "G2", "nhũng": "G2,G3",
    "thụ án": "G2", "xử án": "G2", "nghẻo": "G4",
}
K0 = {}  # bình/bĩnh: Opus đề xuất K0 rồi rút lại, vì hai bên đã ký K2 ngày 19/11/2026 (unified/chu-ky.tsv:134–135)
LEX = ("tự tử tự sát tự vẫn giết chém đâm bắn hiếp dâm đụ địt lồn buồi cặc chịch phịch đéo đĩ điếm làm tình giao cấu "
       "tra tấn hành hạ treo cổ thắt cổ cắt cổ chặt đầu máu xác thây mổ thủ dâm ma túy ma tuý hãm cưỡng sát bạo đánh đập "
       "đấm tát thiến hoạn giao hợp tục mông ngực vú háng dương vật âm hộ tinh liếm bú mút nứng loạn ấu chết tử mồ mả "
       "quan tài hòm tang ma quỷ hành quyết xử tử tù súng đạn nổ bom dao kiếm chặt cắt đứt rạch đập giẫm thịt gái trai "
       "phò gạ dục khiêu trần truồng lõa khỏa cởi ỉa đái cứt bĩnh tè ị rắm đít").split()
LEX2 = ["tự tử", "tự sát", "tự vẫn", "làm tình", "giao cấu", "tra tấn", "hành hạ", "treo cổ", "thắt cổ", "cắt cổ", "chặt đầu",
        "thủ dâm", "ma túy", "ma tuý", "đánh đập", "giao hợp", "dương vật", "âm hộ", "quan tài", "hành quyết", "xử tử",
        "con heo", "trần truồng"]
PAT = re.compile(r"(^|\s)(" + "|".join(sorted(map(re.escape, set(LEX) | set(LEX2)), key=len, reverse=True)) + r")(\s|$)")
DUOI_NGUONG_DANH_GIA = {  # cặp dưới ngưỡng bị bộ lọc bắt: đánh giá của Opus
    ("đông đúc", "động dục"): ("K2_DE_XUAT", "G6",
                               "tình dục (thú vật động dục), xét dưới mốc theo H7; nghĩa kỹ thuật chăn nuôi, r nhỏ"),
    ("dại khờ", "đái khó"): ("KHONG_CONI", "G5",
                             "cụm chỉ triệu chứng tiểu tiện, PPM 0; theo tiền lệ bình/bĩnh (chu-ky.tsv:134–135) hoạt động "
                             "bài tiết không xếp K0; G5 dưới mốc: không còi"),
    ("đại dương", "đái đường"): ("KHONG_CONI", "G5", "tên bệnh (tiểu đường), không phải chất thải; dưới mốc 0,3: không còi"),
    ("bổ dưỡng", "bổ dương"): ("KHONG_CONI", "G6", "thuốc bổ, không phải tình dục rõ; dưới mốc 0,3: không còi"),
    ("tăng tốc", "tang tóc"): ("KHONG_CONI", "G4", "dưới mốc 0,3; không phải tự hại, bạo lực, tình dục rõ: không còi"),
    ("tính khí", "tinh khí"): ("KHONG_CONI", "G6", "nghĩa đông y; dưới mốc 0,3: không còi"),
    ("hát hò", "hạ thổ"): ("KHONG_CONI", "G4", "dưới mốc 0,3; không phải tự hại, bạo lực, tình dục rõ: không còi"),
}


def ppm(r):
    return (int(r["sub_sach"]) / SUB0 * 1e6 + int(r["web_sach"]) / WEB0 * 1e6) / 2


def main():
    out_utf8()
    main_words = [l.split("|")[0] for l in lines(AT / "wordlist.txt")]
    km = {key(w): w for w in main_words}
    oc = rd(U / "opus-counts.tsv")
    p_ung = {r["tu"]: ppm(r) for r in oc if r["vai_tro"] == "UNG_VIEN"}
    rows, log = [], []
    used = set()

    def verdict(w, x, r):
        if (w, x) in K0:
            return "K0_DE_XUAT", "K0", K0[(w, x)]
        if (w, x) in K1_RO:
            return ("K1_DE_XUAT" if r >= 0.2 else "K2_DE_XUAT"), K1_RO[(w, x)], f"nghĩa chính thuộc nhóm đỏ; r = {r:.3f}"
        if (w, x) in K1_GR:
            return ("K1_GIAP_RANH" if r >= 0.2 else "K2_DE_XUAT"), K1_GR[(w, x)], \
                f"nhóm đỏ theo cách đọc chặt bảng ví dụ H6; r = {r:.3f}"
        if (w, x) in K2_MULTI:
            g, why = K2_MULTI[(w, x)]
            return "K2_DE_XUAT", g, why or f"r = {r:.3f} < 0,2"
        if len(w.split()) == 1 and x in K2_SINGLE:
            return "K2_DE_XUAT", K2_SINGLE[x], "khóa một âm tiết: cách đọc mặc định khác, chỉ khớp một âm tiết"
        if len(x.split()) == 1 and x in K2_SINGLE and len(w.split()) > 1:
            return "K2_DE_XUAT", K2_SINGLE[x], "đọc khóa hai âm tiết thành một âm tiết: phải tách ép"
        return "KHONG_DO", "-", "cách đọc khác không thuộc nhóm đỏ H6"

    for r in rd(AT / "ho-so/opus/du-phong-v2/evidence/pham-vi-hau-kiem-h7.tsv"):
        a, b = float(r["ppm_gop_tu_chinh"]), float(r["ppm_gop_doc_khac"])
        v, g, why = verdict(r["tu_chinh"], r["doc_khac"], b / a)
        used.add((r["tu_chinh"], r["doc_khac"]))
        rows.append({"khoa": r["khoa"], "tu_chinh": r["tu_chinh"], "doc_khac": r["doc_khac"], "nguon_cap": "PHAM_VI",
                     "ppm_gop_tu_chinh": f"{a:.3f}", "ppm_gop_doc_khac": f"{b:.3f}", "ti_le_r": f"{b / a:.3f}",
                     "nhom_H6": g, "de_xuat": v, "ly_do": why})
    duoi = [r for r in oc if r["vai_tro"] == "DOC_KHAC" and r["khoa"] in km and ppm(r) < 0.3]
    for r in duoi:
        w, x = km[r["khoa"]], r["tu"]
        if not PAT.search(x) and (w, x) not in K0:
            continue
        a, b = p_ung.get(w), ppm(r)
        v, g, why = verdict(w, x, b / a if a else 0.0)
        if (w, x) in DUOI_NGUONG_DANH_GIA:
            v, g, why = DUOI_NGUONG_DANH_GIA[(w, x)]
        elif v in ("KHONG_DO", "K2_DE_XUAT") and (w, x) not in K0:
            v, why = "KHONG_CONI", ("dưới mốc 0,3; không phải tự hại, bạo lực, tình dục rõ hay chất thải: không còi")
        used.add((w, x))
        rows.append({"khoa": r["khoa"], "tu_chinh": w, "doc_khac": x, "nguon_cap": "DUOI_NGUONG",
                     "ppm_gop_tu_chinh": f"{a:.3f}" if a else "-", "ppm_gop_doc_khac": f"{b:.3f}",
                     "ti_le_r": f"{b / a:.3f}" if a else "-", "nhom_H6": g, "de_xuat": v, "ly_do": why})
    hnd = rd(HERE / "h7-hnd-cung-khoa.tsv", mine=True)
    thieu = [r for r in hnd if r["co_trong_doc_khac"] == "KHONG"]
    for r in thieu:
        w, x = r["tu_chinh"], r["doc_khac_hnd"]
        v, g, why = verdict(w, x, 0.0)
        used.add((w, x))
        rows.append({"khoa": r["khoa"], "tu_chinh": w, "doc_khac": x, "nguon_cap": "HND_THIEU", "ppm_gop_tu_chinh": "-",
                     "ppm_gop_doc_khac": "CHUA_DO", "ti_le_r": "-", "nhom_H6": g, "de_xuat": v,
                     "ly_do": why if v != "KHONG_DO" else "cách đọc khác không thuộc nhóm đỏ H6 (chưa đo; không cần đo)"})
    miss = [p for p in list(K1_RO) + list(K1_GR) + list(K2_MULTI) + list(K0) if p not in used]
    assert not miss, miss
    signed = collections.defaultdict(list)
    for i, r in enumerate(rd(U / "chu-ky.tsv"), 2):
        if r["loai_ky"] == "K2" and r["hieu_luc"] == "CO":
            signed[r["tu"]].append((r["nguoi_ky"], i))
    for r in rows:
        s = signed.get(r["tu_chinh"], [])
        if r["de_xuat"] == "K2_DE_XUAT" and {"Astra", "Opus"} <= {n for n, _ in s}:
            r["de_xuat"] = "K2_DA_KY"
            r["ly_do"] += "; đã có hai chữ ký K2 cho khóa: chu-ky.tsv:" + ",".join(str(i) for _, i in s)
        elif r["tu_chinh"] == "bình" and r["doc_khac"] == "bĩnh":
            r["de_xuat"], r["nhom_H6"] = "K2_DA_KY", "G5"
            r["ly_do"] = ("Opus định đề xuất K0 (Wiktionary: bĩnh là đại tiện) nhưng rút lại: P1 xếp COI_H7, hai bên đã ký K2 "
                          "với đúng lý do này (chu-ky.tsv:" + ",".join(str(i) for _, i in s) + "); không có chứng cứ mới")
    hdr = ["khoa", "tu_chinh", "doc_khac", "nguon_cap", "ppm_gop_tu_chinh", "ppm_gop_doc_khac", "ti_le_r", "nhom_H6",
           "de_xuat", "ly_do"]
    write_tsv(OUT / "sang-loc-h7.tsv", hdr, rows)
    c = collections.Counter((r["nguon_cap"], r["de_xuat"]) for r in rows)
    log.append(f"dòng: {len(rows)}; DOC_KHAC dưới mốc của khóa chính: {len(duoi)}; HND thiếu: {len(thieu)}")
    for k in sorted(c):
        log.append(f"{k[0]}\t{k[1]}\t{c[k]}")
    tu = collections.defaultdict(set)
    for r in rows:
        tu[r["de_xuat"]].add(r["tu_chinh"])
    k1 = tu["K0_DE_XUAT"] | tu["K1_DE_XUAT"] | tu["K1_GIAP_RANH"]
    log.append(f"từ chính phải thay nếu K0/K1 được ký: {len(k1)} (K0 {len(tu['K0_DE_XUAT'])}, K1 rõ {len(tu['K1_DE_XUAT'])}, "
               f"K1 giáp ranh {len(tu['K1_GIAP_RANH'])})")
    log.append(f"từ chính cần hai chữ ký K2 mới (không kể từ đã phải thay): {len(tu['K2_DE_XUAT'] - k1)}; "
               f"đã ký từ trước: {len(tu['K2_DA_KY'] - k1)} ({', '.join(sorted(tu['K2_DA_KY'] - k1, key=o1))})")
    (HERE / "sang-loc-h7.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
    print("\n".join(log))
    for v in ("K0_DE_XUAT", "K1_DE_XUAT", "K1_GIAP_RANH"):
        print(v, sorted(tu[v], key=o1))


if __name__ == "__main__":
    main()
