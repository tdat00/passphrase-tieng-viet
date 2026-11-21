"""Dựng hai TSV nháp chung và kiểm tương thích trong bộ nhớ; không sửa tệp phát hành."""
import argparse
import csv
import hashlib
import io
import json
import os
import subprocess
import sys
import unicodedata
from collections import Counter

from inventory import EV, INPUTS, LETTERS, OUT, ROOT, TOOLS, UNIFIED, key, load, o1, read, save_json, save_tsv, tsv

OPUS = TOOLS / "ho-so" / "opus" / "du-phong-v2"
JOINT_FILES = {
    name: UNIFIED / f"du-phong-v2-{name}"
    for name in ("bao-cao-chung.md", "ke-hoach.md", "phan-loai.tsv",
                 "honorable-mentions.tsv", "cau-hoi.md")
}
H5_RESOLVED = {"hì hụi", "nhão nhẹt", "nhão nhoẹt"}
SOFT_RESOLVED = {"ăn trầu", "bèo bọt", "chấp nhặt", "giở giọng", "giở quẻ", "mụ mị", "non choẹt", "tía lia"}
H6_FLAGGED = {"cơ quan", "lực lượng", "truy tìm", "dự bị", "lên chức", "đại lục"}
L3_CLASS = {"ánh nhìn": "K", "giờ cao điểm": "K", "tên đệm": "K",
            "ngủ nướng": "H", "nhấp chuột": "H", "tắc đường": "H"}

HEADER = (
    "> - **Dự phòng:** giữ nguyên 205 từ để đối chiếu lịch sử, đã phân loại tại "
    "[mục 11](#11-danh-sách-dự-phòng-đã-phân-tích-chưa-phát-hành) và "
    "[bảng phân loại](analyzing-tools/du-phong-phan-loai.tsv). "
    "168 mục có câu đạt D6/D7 trong hồ sơ, 37 mục chưa viết; trạng thái nghĩa không thay thế "
    "các cổng chọn từ. Tầng A/B/C/D không cấp quyền thay vào danh sách chính."
    "\n> - **Từ có thể cân nhắc:** 237 từ, xem [mục 12](#12-từ-có-thể-cân-nhắc-honorable-mentions) "
    "và [honorable-mentions.tsv](analyzing-tools/honorable-mentions.tsv); "
    "đây không phải dự phòng hay danh sách phát hành."
)
TOC = (
    "11. [Danh sách dự phòng (đã phân tích, chưa phát hành)]"
    "(#11-danh-sách-dự-phòng-đã-phân-tích-chưa-phát-hành)\n"
    "12. [Từ có thể cân nhắc (honorable mentions)]"
    "(#12-từ-có-thể-cân-nhắc-honorable-mentions)"
)
SECTION11 = """## 11. Danh sách dự phòng (đã phân tích, chưa phát hành)

<a id="11-danh-sách-dự-phòng-chưa-phân-tích"></a>

### 11.1. Trạng thái và phạm vi

**Trạng thái: đã phân tích, chưa phát hành.** Tập đối chiếu vẫn gồm 205 từ; đây không phải 205 gói thay thế đã được duyệt. Quyết định 10 ghi trạng thái ban đầu; yêu cầu phân tích ngày 20/11/2026 của chủ (D-dpv2-1) là căn cứ cập nhật trạng thái hiện hành. Danh sách chính 7.776 từ không đổi. Danh sách và SHA cột từ dự phòng vẫn giữ nguyên: `f015e718d03bc8cae4bcb0ab0014c813a02e918c1386075aff796e94189e098b`.

### 11.2. Các tầng và cảnh báo

A: hồ sơ ưu tiên chuẩn bị thay. B: còn thiếu câu giải nghĩa. C: cần thận trọng hoặc còn việc kiểm riêng. D: không dùng theo kết luận cổng/H9 đã ghi. Đọc cả cột trạng thái cổng và việc còn thiếu; tầng không thay nhãn OK/R1, không sửa S4 và không tự cấp quyền thay từ.

{{BANG_TANG}}

Chi tiết từng từ và căn cứ nằm trong [bảng phân loại](analyzing-tools/du-phong-phan-loai.tsv).

Lý do ngữ nghĩa/độ quen là nhận định đã thống nhất của hai SA, không phải tỷ lệ gõ sai đã đo. Tổng chứng liệu là tổng lượt sạch phụ đề/web và số câu Leipzig/Tatoeba; đây là chỉ báo biên tập, không thay mã H8. Trong lý do H5, lượt sạch chỉ hai kho OPUS. Các cụm dùng từ nào trước phản ánh hạng S4 hiện tại, không tạo quy tắc ưu tiên mới.

{{BANG_CANH_BAO}}

### 11.3. Ngăn hạn mức và quy tắc thay thế

Danh sách chính có 7.699 OK không-F và 77 OK-F, không có R1. Khi Q3 đang đầy, OK-F chỉ thay ghế F. OK không-F có thể thay ghế C/H/K hoặc F mà không tăng Q3. Dự phòng R1 chỉ thay R1; trần Q2 không cho mượn ghế OK. Không tự suy số từ có câu hoặc số dòng dự phòng thành số ghế đã đủ mọi điều kiện.

### 11.4. Giải nghĩa, chữ ký và việc còn thiếu

Trong tập 205 ban đầu, 168 mục có câu đạt D6/D7 lịch sử (123 v1, 35 v2, 10 v3), 37 mục chưa có câu đều thuộc F. Chưa có dòng D8 cho các mục dự phòng. Không gọi kết quả đối chiếu hash lịch sử là lần chạy D6 mới.

Mã H8 theo tập luật P2 v4.1: 198 MANH, 4 YEU, 2 CHI_BE_MAT, 1 KHONG_LUOT. Cả nghĩ và tối mù là CHI_BE_MAT; ăn nhịp có ngoại lệ không-lượt đã ký. Các mã cảnh báo của P2 phải đi cùng hồ sơ đọc kiểm/chữ ký P4, không tự chuyển thành PASS. Mẫu số P2 là 34.329.387 âm tiết phụ đề và 150.070.912 âm tiết web.

Khảo sát PPM gộp H7 trong hồ sơ này dùng mẫu số mục 0 của tiêu chí/manifest (34.314.528/149.860.716); nhãn H8 vẫn dùng P2. Các phép đo phải ghi rõ mẫu số, không trộn hai bộ.

Trước mỗi lần thay thật: kiểm lại H1–H9, ngăn và S4, câu sạch đúng lượt, D2/D5 trên toàn bộ tập thay, D6 với đủ tham chiếu, D7, D8 và các cổng phát hành. Không dùng mục D hoặc mục còn cổng chưa khép. Việc viết nghĩa mới và thay danh sách chính không thuộc lần phân tích này.

### 11.5. Danh sách 205 từ

```text
{{DU_PHONG_205}}
```
"""
SECTION12 = """## 12. Từ có thể cân nhắc (honorable mentions)

### 12.1. Ý nghĩa và giới hạn

Đây là danh mục để xem xét, không phải dự phòng và không phải danh sách phát hành. Không tái sử dụng câu giải nghĩa đã bị loại, không tự nâng R1 thành OK, không coi đầu mục chưa thẩm định là đã qua luật cứng. Trạng thái của từng nhóm được ghi riêng.

Danh mục này chỉ tính các đầu mục có hồ sơ thẩm định từ đã được chốt. Các nguồn chưa hoàn tất nằm ở hồ sơ nghiên cứu, không tính vào số HM.

### 12.2. Danh mục và nguyên nhân chưa được chọn

{{BANG_NHOM_HM}}

Số đo, lớp, nguồn và điều kiện theo từng từ nằm ở [honorable-mentions.tsv](analyzing-tools/honorable-mentions.tsv). F là điểm thông dụng lịch sử, khác với lớp F; dấu `-` là chưa có hoặc không áp dụng, không phải số 0.

{{BANG_TU_HM}}

### 12.3. Các việc để sau

L2D và các ý tưởng ngoài pool chưa đủ chứng cứ chỉ lưu ở hồ sơ, không tính là từ đã qua cổng. Không tính vào N: lô L3b (48 ứng viên đã chuẩn bị ở [l3b-de-cu-opus.tsv](analyzing-tools/ho-so/unified/l3b-de-cu-opus.tsv), chưa qua P2/P4/H9); *chạng vạng* (chờ xác nhận và đo họ H5 với *choạng vạng*); *bao tử* (K1: khóa `baotu` đọc thành *báo tử*).

Nếu muốn khôi phục một mục từng bị loại ở P7, phải kiểm lịch sử lượt của đúng mục và quyền giao lượt sạch mới trước. Nếu muốn dùng một mục R1, phải tuân thủ P6/Q và quyết định cho danh sách tương ứng. Các bước đó không được mở tự động bởi việc đưa tên vào tài liệu.
"""
README_ROWS = """| [`du-phong.txt`](du-phong.txt) | Giữ nguyên 205 từ để đối chiếu lịch sử; đã có bảng phân loại riêng, chưa phát hành và không phải 205 gói thay thế đã được duyệt |
| [`du-phong-phan-loai.tsv`](du-phong-phan-loai.tsv) | Một dòng cho mỗi từ dự phòng: tầng, ngăn, cảnh báo H, trạng thái nghĩa, mã H8, việc còn thiếu và nguồn chứng cứ |
| [`honorable-mentions.tsv`](honorable-mentions.tsv) | 237 từ có thể cân nhắc đã chốt phạm vi đề cử; không phải dự phòng, không tự cấp quyền thay từ hoặc viết thêm nghĩa |
"""
README_SECTION = """## Dự phòng và từ có thể cân nhắc

Đọc `du-phong-phan-loai.tsv` cùng `du-phong.txt`; không thay từ chỉ dựa vào thứ tự dòng hoặc tầng A. Tầng không thay nhãn OK/R1 và không sửa S4. Mục D hoặc cổng chưa khép không được dùng. R1 không tự thay ghế OK; lớp F không được vượt 77.

Mã H8 lấy từ tập luật P2 v4.1 và kết quả hai bộ cổng đã đối chiếu, gồm cả CHI_BE_MAT. Điểm F, số đếm và mức H8 là ba dữ liệu khác nhau. Mẫu số P2 là 34.329.387/150.070.912 âm tiết phụ đề/web; không sửa ngược metadata nguồn lịch sử để làm chúng giống nhau.

Khảo sát PPM gộp H7 trong hồ sơ này dùng mẫu số mục 0 của tiêu chí/manifest (34.314.528/149.860.716); nhãn H8 vẫn dùng P2. Các phép đo phải ghi rõ mẫu số, không trộn hai bộ.

Từ có thể cân nhắc chỉ là đề cử; cột trạng thái nêu rõ hồ sơ nào chưa hoàn tất. Phân tích này không thay danh sách chính, không viết câu mới và không tự hoàn tất D8.

### Kiểm trên checkout Windows

Nguồn chuẩn trong Git dùng LF. Checkout CRLF có thể làm check_wordlist.py báo C1 và verify.mjs báo C1/C8; đó không phải native PASS. Kiểm đối chứng đúng nội dung LF hoặc trong môi trường giữ LF, đồng thời lưu kết quả kiểm byte của vùng được bảo vệ. Không sửa nguồn chính hoặc nới checker chỉ để làm mất lỗi nền trong tác vụ phân tích.
"""

RESERVE_COLUMNS = [
    "tu", "khoa", "lop", "ngan", "tang_opus", "tang_astra", "tang_chung",
    "tranh_chap", "ma_van_de", "cau_hoi", "trang_thai_h", "giai_nghia",
    "luot_viet", "sha256_giai_nghia", "h8", "F", "diem", "thay_duoc",
    "con_thieu", "ghi_chu", "y_kien_opus", "y_kien_astra", "bang_chung", "xac_minh",
]
HM_COLUMNS = [
    "tu", "khoa", "nhom", "nhan_ho_so", "lop", "xac_minh_lop",
    "de_cu_opus", "de_cu_astra", "ket_luan_nhap", "tranh_chap", "cau_hoi",
    "trang_thai_h", "ngan_du_kien", "h8", "sub_sach", "web_sach", "leipzig",
    "tatoeba", "F", "diem", "nguon", "ly_do_chua_chon", "dieu_kien",
    "ghi_chu", "y_kien_opus", "y_kien_astra", "bang_chung", "xac_minh",
]
PUBLIC_RESERVE_COLUMNS = [
    "tu", "khoa", "lop", "ngan", "tang", "trang_thai_h", "ma_van_de", "giai_nghia",
    "luot_viet", "sha256_giai_nghia", "h8", "F", "diem", "thay_duoc", "con_thieu",
    "ghi_chu", "bang_chung",
]
PUBLIC_HM_COLUMNS = [
    "tu", "khoa", "nhom", "nhan_ho_so", "lop", "xac_minh_lop", "trang_thai_h",
    "ngan_du_kien", "h8", "sub_sach", "web_sach", "leipzig", "tatoeba", "F", "diem",
    "nguon", "ly_do_chua_chon", "dieu_kien", "ghi_chu", "bang_chung",
]


def write_joint_tsv(path, columns, rows):
    assert path in JOINT_FILES.values(), path
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t", lineterminator="\r\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({c: "-" if row.get(c) in ("", None) else row[c] for c in columns})


def catalog_artifacts():
    catalog = EV / "revision-1-artifacts.tsv"
    files = set(JOINT_FILES.values()) | {catalog}
    extensions = {".md", ".py", ".mjs", ".tsv", ".json", ".log", ".txt"}
    for folder in (OUT, OPUS):
        for path in folder.rglob("*"):
            if not path.is_file() or path.suffix not in extensions:
                continue
            if any(part.startswith(("_", ".")) for part in path.relative_to(folder).parts):
                continue
            if path.name.lower() in {"memory.md", "notes.md", "wordlist.txt"}:
                continue
            if path.name.startswith("Viet") and path.suffix == ".txt":
                continue
            files.add(path)
    rows = []
    for path in sorted(files):
        group = "CHUNG" if path in JOINT_FILES.values() else "ASTRA" if OUT in path.parents else "OPUS"
        rows.append({
            "tep": str(path.relative_to(ROOT)), "nhom": group,
            "gioi_thieu": "du-phong-v2-ke-hoach.md §14; báo cáo/phân tích/review của nhóm tương ứng",
        })
    save_tsv(catalog, ["tep", "nhom", "gioi_thieu"], rows)
    return len(rows)


def public_notes():
    source = OPUS / "round-1-review-drafts.md"
    notes = {"reserve": {}, "hm": {}}
    active, kind = False, None
    for line_no, line in enumerate(read(source).splitlines(), 1):
        if line == "## Lượt duyệt 3 (ký kế hoạch)":
            active = True
        if not active:
            continue
        if line.startswith("- **Văn bản `ghi_chu` cho bảng dự phòng**"):
            kind = "reserve"
        elif line.startswith("- **Văn bản `ghi_chu` cho bảng HM**"):
            kind = "hm"
        elif line.startswith("### E."):
            break
        if kind and line.startswith("| "):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) != 2 or cells[0] == "Từ":
                continue
            for word in cells[0].split(", "):
                assert word not in notes[kind]
                notes[kind][word] = {"ghi_chu": cells[1],
                                     "nguon": str(source.relative_to(ROOT)) + ":" + str(line_no)}
    assert len(notes["reserve"]) == 30 and len(notes["hm"]) == 8
    rows = [{"pham_vi": kind, "tu": word, **entry} for kind in ("reserve", "hm")
            for word, entry in sorted(notes[kind].items(), key=lambda item: o1(item[0]))]
    save_tsv(EV / "public-ghi-chu.tsv", ["pham_vi", "tu", "ghi_chu", "nguon"], rows)
    return notes


def public_projection(reserve, hm):
    reserve_out = [
        {c: row["tang_chung"] if c == "tang" else row[c] for c in PUBLIC_RESERVE_COLUMNS}
        for row in reserve
    ]
    hm_out = [
        {c: row[c] for c in PUBLIC_HM_COLUMNS}
        for row in hm if row["ket_luan_nhap"] == "CUNG_DE_CU_CHUA_PHAT_HANH"
    ]
    return reserve_out, hm_out


def official_h8(data):
    gates = {}
    for author in ("opus", "astra"):
        for row in tsv(UNIFIED / f"cong-{author}-v4.tsv"):
            if row["cong"] != "H8":
                continue
            code = "MANH" if row["ly_do"] == "-" else row["ly_do"].split(":")[-1]
            gates.setdefault(row["ung_vien"], {})[author] = (code, row["ket_qua"], row["_ref"])
    result = {}
    for word, pair in gates.items():
        assert pair["opus"][:2] == pair["astra"][:2], word
        result[word] = (pair["opus"][0], ";".join(x[2] for x in pair.values()))
    for lot in ("l2", "l2b", "l2c", "l3"):
        for row in data[f"{lot}-ung-vien"]:
            result.setdefault(row["tu"], (row["H8_so_hoc"], row["_ref"]))
    return result


def h8_replay(source, rules):
    sub_total = rules["tong_am_tiet"]["sub_moi_dong"]
    web_total = rules["tong_am_tiet"]["web_dong_khac"]
    sub, web, clean_sub, clean_web, lei, tat = (
        int(source[k]) for k in ("sub_be_mat", "web_be_mat", "sub_sach", "web_sach", "leipzig", "tatoeba")
    )
    strong_raw = sub * 10_000_000 >= sub_total or web * 10_000_000 >= web_total or lei >= 2 or tat >= 1
    strong_clean = clean_sub * 10_000_000 >= sub_total or clean_web * 10_000_000 >= web_total or lei >= 2 or tat >= 1
    if strong_raw and not strong_clean:
        return "CHI_BE_MAT"
    if strong_raw:
        return "MANH"
    return "YEU" if any((sub, web, lei, tat)) else "KHONG_LUOT"


def build():
    data = load()
    notes = public_notes()
    h8 = official_h8(data)
    rules = data["rules"]
    opus_res = {r["tu"]: r for r in tsv(OPUS / "evidence" / "du-phong-205-bac-sau-soat-cheo-opus.tsv")}
    astra_res = {r["tu"]: r for r in tsv(EV / "cross-review-reserve-diff.tsv")}
    astra_v1 = {r["tu"]: r for r in tsv(OUT / "du-phong-phan-loai.tsv")}
    opus_hm = {r["tu"]: r for r in tsv(OPUS / "evidence" / "de-cu-hop-nhat-de-xuat-opus.tsv")}
    old_opus_hm = {r["tu"]: r for r in tsv(OPUS / "de-cu-them-opus.tsv")}
    astra_union = {r["tu"]: r for r in tsv(EV / "cross-review-honorable-diff.tsv")}
    astra_core = {w for w, r in astra_union.items() if r["astra_de_xuat_sau_review"] == "CO_THE_GOP_THEO_HO_SO"}
    l3b = {r["tu"]: r for r in data["l3b-de-cu-opus"]}
    removed = {r["tu"]: r for r in data["p7-v3-khau-tru-132-theo-P0-astra"]}
    new_signatures = {r["tu"]: r for r in tsv(EV / "revision-1-chu-ky-astra.tsv")}
    assert set(new_signatures) == {"tần số", "vậy nên"}
    assert all(r["nguoi_ky"] == "SA-Astra" and r["loai_ky"] == "K2"
               and r["ket_luan"] == "KHONG_TU_DONG_CHAN" and r["hieu_luc"] == "CO"
               for r in new_signatures.values())
    review_ref = str((OPUS / "round-1-review-drafts.md").relative_to(ROOT))
    review_lines = read(OPUS / "round-1-review-drafts.md").splitlines()
    accepted_h7_line = next(i for i, line in enumerate(review_lines, 1)
                            if line.startswith("### B. Q-dpv2-7:"))
    accepted_h7_ref = review_ref + ":" + str(accepted_h7_line)
    new_h7 = tsv(EV / "revision-1-h7-ngoaitru.tsv")[0]
    assert new_h7["tu"] == "ngoại trừ" and new_h7["de_nghi"] == "C_CHO_H7"
    keep_hm = set(opus_hm) | astra_core
    assert len(keep_hm) == 285 and keep_hm - opus_hm.keys() == {"đại lục"}
    assert len(opus_res) == len(astra_res) == 205
    reserve_rows = []
    for word in data["reserve"]:
        a, o = astra_res[word], opus_res[word]
        original = astra_v1[word]
        label = data["labels_by_word"][word]
        source = data["by_word"][word]
        h8_code, h8_ref = h8[word]
        assert h8_replay(source, rules) == h8_code, word
        a_tier = a["astra_sau_review"]
        if o["bac_de_xuat"] != a_tier:
            assert word in H5_RESOLVED | SOFT_RESOLVED
        o_tier = a_tier  # Opus accepted the eleven previous differences in its draft review.
        o_note = o["ly_do"]
        a_note = a["nhan_dinh_sau_review"]
        if word in SOFT_RESOLVED:
            o_note = "A: nhận lần rút C của Astra; cảnh báo sắc thái chưa là phản đối hợp lệ theo H9; không đổi S4."
            if word == "ăn trầu":
                o_note += " Không đưa nhận định y khoa về trầu cau; chỉ ghi mục không có trong ví dụ nhóm 7 của H6."
        elif word == "hì hụi":
            o_note = "D (H5c): Opus ký họ hì hụi/hè hụi (en.wiktionary oldid 93445969; HND có cả hai); hì hụi 0/0 lượt sạch không thể đạt 95%/20. Không suy hì hục cùng họ."
        elif word in {"nhão nhẹt", "nhão nhoẹt"}:
            o_note = "D (H5c): Opus ký nhão nhẹt/nhão nhoẹt là một từ, biến thể âm đệm; số sạch 9/0 và 6/1, nhão nhoét cùng khóa thêm 5/1; không dạng nào đạt 95%/20."
        elif word in {"thụp", "tuổi xanh"}:
            o_note = "Opus nhận C theo lý do của Astra: " + o_note.removeprefix("Astra: ")
        if word in {"cả nghĩ", "tối mù"}:
            o_note = o_note.replace("H8 YEU", "H8 CHI_BE_MAT")
        if word == "vậy nên":
            o_note = "B. H7 K2: Opus ký không tự động chặn; vảy nến khoảng 0,253 PPM, hiếm hơn nhiều vậy nên; không thuộc ngoại lệ tự hại/bạo lực/tình dục. Chưa có câu."
            a_note = new_signatures[word]["ly_do"]
        if word == "ngoại trừ":
            a_tier = o_tier = "C"
            o_note = "C/CHO_H7: Opus rút nhận định không phải bệnh nên không đỏ (h7-quet-bo-sung.tsv:36) vì trái tiền lệ nội trú (p7-khau-tru.tsv:19). Còi bật (PPM gộp 1,215 ≥ 0,3). Opus nghiêng K2, chưa ký trước khi đo."
            a_note = "Astra nhận đồng thuận T-dpv2-9: C/CHO_H7; không dùng trước khi đo tỷ lệ nghĩa điều trị của ngoại trú ở web và hai SA ký mức K. Không tự kết luận K1/K2."
        disputes, questions, issues = [], [], []
        assert a_tier == o_tier, word
        if word == "vậy nên":
            issues.append("H7_K2")
        if word in H5_RESOLVED or a_tier == o_tier == "D" or word == "loằng ngoằng":
            issues.append("H5")
        if word == "ngoại trừ":
            issues.append("H7")
        if h8_code != "MANH":
            issues.append("H8_" + h8_code)
        gloss = data["gloss"].get(word)
        if not gloss:
            issues.append("CHUA_VIET")
        issues.append("D8_CHUA_CO")
        joint = a_tier if a_tier == o_tier else "CHO_HOA"
        gate = "HO_SO_LICH_SU_CHUA_PHE_DUYET_THAY"
        if joint == "D":
            gate = "KHONG_DUNG_H5_H9"
        elif "H5" in issues:
            gate = "CHO_H5"
        elif "H7" in issues:
            gate = "CHO_H7"
        missing = "P6/H/Q và S4; D8; kiểm toàn tập thay; phê duyệt thay ở tác vụ khác"
        if not gloss:
            missing = "Lượt viết sạch, D6, D7; " + missing
        if gate.startswith("CHO"):
            if word == "ngoại trừ":
                missing = "Khép H7: đo tỷ lệ nghĩa điều trị của ngoại trú như tiền lệ nội trú, rồi hai SA ký K1/K2/không tự động; " + missing
            else:
                missing = "Khép " + gate[4:] + "; " + missing
        if joint == "D":
            missing = "Không dùng theo H5/H9; giữ dòng để đối chiếu lịch sử"
        reserve_rows.append({
            "tu": word, "khoa": key(word), "lop": label["lop"], "ngan": a["ngan"],
            "tang_opus": o_tier, "tang_astra": a_tier, "tang_chung": joint,
            "tranh_chap": ";".join(disputes) or "KHONG", "ma_van_de": ";".join(issues),
            "cau_hoi": ";".join(questions), "trang_thai_h": gate,
            "giai_nghia": "CO_PASS_LICH_SU" if gloss else "CHUA_VIET",
            "luot_viet": gloss["d6_version"] if gloss else "-",
            "sha256_giai_nghia": gloss["gloss_sha256"] if gloss else "-",
            "h8": h8_code, "F": label["F"], "diem": label["diem"],
            "thay_duoc": "OK_F→F khi Q3 đang đầy" if label["lop"] == "F" else "OK_khong_F→C/H/K/F nếu các cổng đủ",
            "con_thieu": missing, "y_kien_opus": o_note, "y_kien_astra": a_note,
            "ghi_chu": notes["reserve"].get(word, {}).get("ghi_chu", "-"),
            "bang_chung": ";".join(x for x in (
                o["_ref"], a["_ref"], label["_ref"], h8_ref, original["p4_ref"],
                review_ref + ":64" if word in H5_RESOLVED else None,
                review_ref + ":75" if word in SOFT_RESOLVED else None,
                new_signatures[word]["_ref"] if word == "vậy nên" else None,
                new_h7["_ref"] if word == "ngoại trừ" else None,
                accepted_h7_ref if word == "ngoại trừ" else None,
                notes["reserve"].get(word, {}).get("nguon"),
            ) if x),
            "xac_minh": "verified:nhãn/số/hash/hồ sơ; assumed:tầng mới và ngữ nghĩa; chưa có chữ ký bản chung",
        })

    hm_rows = []
    for word in sorted(keep_hm, key=o1):
        rank = data["rank_by_word"].get(word, {})
        old_o = old_opus_hm.get(word, {})
        o = opus_hm.get(word, {})
        a = astra_union[word]
        if word in removed:
            group = "D6_CUOI" if removed[word]["cong"].startswith("D6") else "D7_CUOI"
        elif word in l3b:
            group = "L3B_CHUA_CHAM"
        else:
            assert rank["nhan"] == "R1"
            group = "R1"
        provisional = group == "L3B_CHUA_CHAM"
        cls = L3_CLASS.get(word, "C") if provisional else rank["lop"]
        source = data["by_word"].get(word)
        if provisional:
            r = l3b[word]
            numbers = {k: r.get(k) for k in ("sub_sach", "web_sach")}
            numbers.update(leipzig="-", tatoeba="-")
            h8_code, h8_ref = "CHUA_CO_CONG_L3B", r["_ref"]
            origin = "L3b; Wiktionary " + r["wiktionary"]
            source_ref = r["_ref"]
        else:
            numbers = {k: source[k] for k in ("sub_sach", "web_sach", "leipzig", "tatoeba")}
            h8_code, h8_ref = h8[word]
            assert h8_replay(source, rules) == h8_code, word
            origin = source["nguon_pool"] + "; " + source["h3_nguon"]
            source_ref = source["nguon_dong"] + ";" + source["dem_sach_dong"]
        disputes, questions = [], []
        counted = not provisional and word not in {"chạng vạng", "bao tử"}
        a_yes = o_yes = counted
        if provisional:
            missing = "P2/P4/H9, H2/H3/H6 ngữ nghĩa, DF còn thiếu, xếp lớp/nhãn; chỉ sau đó xét nghĩa sạch"
            reason = "Lô L3b chuẩn bị rồi rút trước chấm; chưa vào pool"
            gate = "CHUA_CHAM_DOI"
        elif word in removed:
            attempts = [r["_version"] for r in data["d6"][word]]
            reason = removed[word]["cong"] + "; log có " + ",".join(attempts)
            missing = "Không dùng câu bị loại; kiểm lịch sử từng mục/quyền mở lượt sạch trước khôi phục; D6/D7/D8/P6"
            gate = "HO_SO_TU_DAT_LICH_SU_NGHIA_BI_LOAI"
        else:
            reason = "R1 đứng sau OK; danh sách chính hiện không có ghế R1"
            missing = "Không tự nâng R1; chỉ xét theo P6/Q của tác vụ được duyệt; viết sạch D6/D7/D8 nếu chọn"
            gate = "HO_SO_R1_LICH_SU"
        if word == "mặt khác":
            missing += "; log chỉ có v2/v3, chưa đủ để khẳng định đã hết hai lượt viết lại"
        o_position = o.get("ghi_chu", "-")
        a_position = a["nhan_dinh"]
        state = "CUNG_DE_CU_CHUA_PHAT_HANH"
        if word in H6_FLAGGED:
            missing += "; rà H6 trước khi dùng"
            if word == "đại lục":
                o_position = "Opus đổi lập trường: giữ R1 có cờ rà H6.3 về cách dùng Trung Quốc đại lục; lo ngại là nhận định, chưa là phản đối H9 hợp lệ."
            else:
                o_position = "Opus giữ đề cử có cờ: hai phiếu P4 OK, không có phản biện trong bảng đã lưu; lo ngại H6 chưa là phản đối H9 hợp lệ. Lưu cờ Astra để rà trước khi dùng."
            a_position = "Astra nhận phương án 1 cho cả sáu mục: giữ theo hồ sơ đã xét, lưu cờ rà H6; chưa có chứng cứ mới đủ phản đối H9, không tuyên bố mọi cách dùng đều lành."
        if provisional:
            state = "NGOAI_HM_CHUA_THAM_DINH"
            o_position = "Q-dpv2-4 phương án 2: chưa qua P2/P4/H9 nên không tính HM; nguồn l3b-de-cu-opus.tsv."
            a_position = "Astra và Opus thống nhất không tính HM trước khi đủ thẩm định; giữ dòng làm hồ sơ."
            if word == "giờ cao điểm":
                missing = "H2: ba khối chỉ khoảng thời gian không thuộc nhóm thực thể cho phép; không nhận theo luật hiện hành. " + missing
                o_position += " Opus nhận phản đối H2 của Astra."
            if word in {"ớt đỏ", "nắng ấm"}:
                missing += "; cần xét X/tổ hợp tự do"
        if word == "chạng vạng":
            state = "NGOAI_HM_CHO_H5"
            gate += ";CHO_H5"
            missing = "Xác nhận cùng từ và đo họ choạng vạng trước khi tính HM; " + missing
            o_position = "Q-dpv2-4 phương án 2: chờ xác nhận cùng từ và đo choạng vạng trước khi tính."
            a_position = "Astra đồng ý giữ ngoài HM cho đến khi khép H5."
        if word == "bao tử":
            state = "LOAI_K1"
            gate += ";H7_K1"
            missing = "Không dùng toàn khóa baotu, gồm bào tử; không tính HM. Giữ dòng lịch sử loại D6."
            o_position = "Nhận K1 của Astra: báo tử thuộc H6.4, cách đọc tự nhiên, PPM gộp khoảng 0,385 trên mốc còi; loại cả khóa."
            a_position = "Astra xác nhận K1 cho toàn khóa baotu; không dùng nghĩa lành để né cổng."
        if word == "tần số":
            gate += ";H7_K2"
            o_position = "Opus ký K2 không tự động chặn: tận số khoảng 0,207 PPM, hiếm hơn nhiều tần số; không thuộc ngoại lệ tự hại/bạo lực/tình dục."
            a_position = new_signatures[word]["ly_do"]
        if word == "vây cá":
            a_position = "H8 CHI_BE_MAT theo P2 v4.1; đã có đọc kiểm ở P4 và xác nhận H8, không ghi MANH."
        hm_rows.append({
            "tu": word, "khoa": key(word), "nhom": group,
            "nhan_ho_so": rank.get("nhan", "CHUA_CHAM"), "lop": cls,
            "xac_minh_lop": "assumed:đề xuất Astra, chưa P4" if provisional else "verified:nhãn lịch sử",
            "de_cu_opus": "CO_DIEU_KIEN" if o_yes else ("KHONG_DE_CU" if word == "bao tử" else "KHONG_TINH_HM"),
            "de_cu_astra": "DE_CU_LOI" if a_yes else ("KHONG_DE_CU_K1" if word == "bao tử" else "KHONG_TINH_HM"),
            "ket_luan_nhap": state,
            "tranh_chap": ";".join(disputes) or "KHONG", "cau_hoi": ";".join(questions),
            "trang_thai_h": gate,
            "ngan_du_kien": "CHUA_CHAM" if provisional else
                (rank["nhan"] + ("_F" if rank["lop"] == "F" else "_KHONG_F")),
            "h8": h8_code, **numbers, "F": rank.get("F", "-"), "diem": rank.get("diem", "-"),
            "nguon": origin, "ly_do_chua_chon": reason, "dieu_kien": missing,
            "ghi_chu": notes["hm"].get(word, {}).get("ghi_chu", "-"),
            "y_kien_opus": o_position, "y_kien_astra": a_position,
            "bang_chung": ";".join(x for x in (o.get("_ref"), a["_ref"], source_ref, h8_ref,
                                                 rank.get("_ref"), removed.get(word, {}).get("_ref"),
                                                 review_ref + ":101" if word in H6_FLAGGED else None,
                                                 review_ref + ":83" if provisional or word == "chạng vạng" else None,
                                                 review_ref + ":90" if word in {"bao tử", "tần số"} else None,
                                                 new_signatures[word]["_ref"] if word == "tần số" else None,
                                                 notes["hm"].get(word, {}).get("nguon")) if x),
            "xac_minh": "verified:số/khóa/nguồn; assumed:đề cử và ngữ nghĩa; không phải phê duyệt phát hành",
        })
    assert len(reserve_rows) == 205 and len(hm_rows) == 285
    counted_hm = [r for r in hm_rows if r["ket_luan_nhap"] == "CUNG_DE_CU_CHUA_PHAT_HANH"]
    assert len(counted_hm) == 237
    assert not any(r["tranh_chap"] != "KHONG" for r in hm_rows)
    assert not any(r["tranh_chap"] != "KHONG" for r in reserve_rows)
    assert Counter(r["tang_chung"] for r in reserve_rows) == {"A": 148, "B": 36, "C": 15, "D": 6}
    ngoai = next(r for r in reserve_rows if r["tu"] == "ngoại trừ")
    assert ngoai["trang_thai_h"] == "CHO_H7" and ngoai["ma_van_de"] == "H7;D8_CHUA_CO"
    expected_notes = {r["tu"] for r in reserve_rows if r["tang_chung"] in {"C", "D"}} | SOFT_RESOLVED | {"vậy nên"}
    assert set(notes["reserve"]) == expected_notes
    assert set(notes["hm"]) == H6_FLAGGED | {"tần số", "vây cá"}
    public_reserve, public_hm = public_projection(reserve_rows, hm_rows)
    assert sum(r["ghi_chu"] != "-" for r in public_reserve) == 30
    assert sum(r["ghi_chu"] == "-" for r in public_reserve) == 175
    assert sum(r["ghi_chu"] != "-" for r in public_hm) == 8
    assert sum(r["ghi_chu"] == "-" for r in public_hm) == 229
    for kind, rows in (("reserve", public_reserve), ("hm", public_hm)):
        for row in rows:
            assert row["ghi_chu"] == notes[kind].get(row["tu"], {}).get("ghi_chu", "-")
    for first, second in (("lỗ lãi", "lời lỗ"), ("mỏng dính", "mỏng tanh")):
        left, right = (data["labels_by_word"][w] for w in (first, second))
        assert left["nhan"] == right["nhan"] == "OK" and float(left["diem"]) > float(right["diem"])
    for word, expected_total in {"ăn nhịp": 0, "cả nghĩ": 2, "chễm chệ": 3, "cửu chương": 6,
                                 "tạnh ráo": 2, "thẳng đơ": 1, "tối mù": 2}.items():
        assert sum(int(data["by_word"][word][k]) for k in ("sub_sach", "web_sach", "leipzig", "tatoeba")) == expected_total
    assert int(data["by_word"]["hì hụi"]["sub_sach"]) == int(data["by_word"]["hì hụi"]["web_sach"]) == 0
    all_new_keys = [r["khoa"] for r in reserve_rows + hm_rows]
    assert len(set(all_new_keys)) == 490
    assert not set(all_new_keys) & {key(w) for w in data["main"]}
    assert not set(all_new_keys) & {r["khoa"] for r in data["blocked_keys"]}
    assert [r["tu"] for r in reserve_rows] == sorted(data["reserve"], key=o1)
    for row in reserve_rows + hm_rows:
        word = row["tu"]
        parts = word.split(" ")
        assert word == unicodedata.normalize("NFC", word) == word.lower()
        assert 1 <= len(parts) <= 3 and all(p and set(p) <= LETTERS for p in parts), word
        assert 4 <= len(key(word)) <= 12, word
        assert key(word[0].upper() + word[1:]) == row["khoa"]
    write_joint_tsv(JOINT_FILES["phan-loai.tsv"], RESERVE_COLUMNS, reserve_rows)
    write_joint_tsv(JOINT_FILES["honorable-mentions.tsv"], HM_COLUMNS, hm_rows)
    summary = {
        "base_commit": "cefb99386d4845e40bc2d3eabc7d6898d078305d",
        "reserve_rows": len(reserve_rows), "reserve_common_tiers": dict(Counter(r["tang_chung"] for r in reserve_rows)),
        "reserve_tier_disputes": [r["tu"] for r in reserve_rows if r["tang_chung"] == "CHO_HOA"],
        "reserve_any_disputes": sum(r["tranh_chap"] != "KHONG" for r in reserve_rows),
        "reserve_h8": dict(Counter(r["h8"] for r in reserve_rows)),
        "reserve_glosses": dict(Counter(r["giai_nghia"] for r in reserve_rows)),
        "hm_rows": len(hm_rows), "hm_groups": dict(Counter(r["nhom"] for r in hm_rows)),
        "hm_joint_states": dict(Counter(r["ket_luan_nhap"] for r in hm_rows)),
        "hm_counted_N": len(counted_hm), "hm_counted_groups": dict(Counter(r["nhom"] for r in counted_hm)),
        "hm_counted_h8": dict(Counter(r["h8"] for r in counted_hm)),
        "public_notes": {"reserve_nonempty": 30, "reserve_dash": 175, "hm_nonempty": 8, "hm_dash": 229,
                         "C_D_warning_rows": 21, "evidence_totals_and_S4_verified": True,
                         "source": "Opus Lượt duyệt 3 §D; giữ nguyên văn"},
        "reserve_agreement_before_new_Q7": {"A": 149, "B": 36, "C": 14, "D": 6},
        "closed_questions": [f"Q-dpv2-{i}" for i in range(1, 8)],
        "open_questions": [],
        "owner_Q1_answer": {"option": "3", "source_commit": "1734b43",
                            "decision": "D-dpv2-5", "separate_main_list_request": True,
                            "executed_within_du_phong_v2": False},
        "ngoaitru_decision": "T-dpv2-9: C/CHO_H7, không dùng trước khi đo tỷ lệ nghĩa và hai SA ký mức K",
        "hm_h8": dict(Counter(r["h8"] for r in hm_rows)),
        "hm_original_attempts": dict(Counter(",".join(r["_version"] for r in data["d6"][w]) for w in removed)),
        "mat_khac_recorded_versions_and_refs": [
            {"version": r["_version"], "ref": r["_ref"]} for r in data["d6"]["mặt khác"]
        ],
        "h8_rule_version": rules["phien_ban"], "h8_rule_denominators": rules["tong_am_tiet"],
        "h8_replay_all_historical_rows_matched": True,
        "h1_h2_numeric_h4_blocked_keys_490_rows": True,
        "protected": json.loads((EV / "inventory.json").read_text(encoding="utf-8"))["protected_bytes"],
        "draft_tables_sha256_LF": {
            path.name: hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
            for path in (JOINT_FILES["phan-loai.tsv"], JOINT_FILES["honorable-mentions.tsv"])
        },
    }
    save_json(EV / "joint-summary.json", summary)
    save_json(EV / "joint-inputs.json", INPUTS)
    save_json(EV / "joint-publication-text.json", {
        "wordlist_header": HEADER, "toc": TOC, "section11": SECTION11, "section12": SECTION12,
        "readme_rows": README_ROWS, "readme_section": README_SECTION,
    })
    return data, reserve_rows, hm_rows, summary


def proposed_document(data, reserve, hm):
    original = (ROOT / "WordListAnalyze.md").read_bytes().decode("utf-8")
    text = original.replace("\r\n", "\n")
    old_header = next(line for line in text.splitlines() if line.startswith("> - **Dự phòng:**"))
    text = text.replace(old_header, HEADER, 1)
    old_toc = next(line for line in text.splitlines() if line.startswith("11. [Danh sách dự phòng"))
    text = text.replace(old_toc, TOC, 1)
    tiers = Counter(r["tang_chung"] for r in reserve)
    tier_order = ["A", "B", "C", "D"] + (["CHO_HOA"] if tiers["CHO_HOA"] else [])
    tier_table = "| Tầng | Số từ trong nháp |\n|---|---:|\n" + "\n".join(f"| {k} | {tiers[k]} |" for k in tier_order)
    warning_rows = [r for r in reserve if r["tang_chung"] in ("C", "D")]
    assert len(warning_rows) == 21 and all(r["ghi_chu"] != "-" for r in warning_rows)
    warning_table = "| Từ | Tầng | Lý do | Việc còn thiếu |\n|---|---|---|---|\n" + "\n".join(
        f"| {r['tu']} | {r['tang_chung']} | {r['ghi_chu']} | {r['con_thieu']} |"
        for r in warning_rows
    )
    section11 = SECTION11.replace("{{BANG_TANG}}", tier_table).replace("{{BANG_CANH_BAO}}", warning_table)
    section11 = section11.replace("{{DU_PHONG_205}}", "\n".join(data["reserve"]))
    hm = [r for r in hm if r["ket_luan_nhap"] == "CUNG_DE_CU_CHUA_PHAT_HANH"]
    assert len(hm) == 237
    groups = Counter(r["nhom"] for r in hm)
    section12 = SECTION12
    section12 = section12.replace("{{BANG_NHOM_HM}}", "| Nhóm | Số dòng nháp |\n|---|---:|\n" +
                                  "\n".join(f"| {k} | {v} |" for k, v in groups.items()))
    section12 = section12.replace("{{BANG_TU_HM}}", "| Từ | Nhóm | Trạng thái nháp |\n|---|---|---|\n" +
                                  "\n".join(f"| {r['tu']} | {r['nhom']} | {r['ket_luan_nhap']} |" for r in hm))
    start = text.index("## 11. Danh sách dự phòng")
    preview = (text[:start] + section11 + "\n" + section12).replace("\n", "\r\n")
    before_sec = original[original.index("## 10. Danh sách 7.776 từ phát hành"):original.index("## 11. Danh sách dự phòng")]
    after_sec = preview[preview.index("## 10. Danh sách 7.776 từ phát hành"):preview.index("## 11. Danh sách dự phòng")]
    assert before_sec.encode("utf-8") == after_sec.encode("utf-8")
    return preview


def proof(data, reserve, hm, summary):
    for path in JOINT_FILES.values():
        assert path.is_file(), path
    plan_text = JOINT_FILES["ke-hoach.md"].read_text(encoding="utf-8")
    for template in (HEADER, TOC, SECTION11, SECTION12, README_ROWS, README_SECTION):
        assert template.strip() in plan_text, "Mẫu trong kế hoạch khác mẫu được mô phỏng"
    qtext = JOINT_FILES["cau-hoi.md"].read_text(encoding="utf-8")
    assert "Không còn câu hỏi mở." in qtext
    assert not any(line.startswith("## Q-dpv2-") for line in qtext.splitlines())
    notes = public_notes()
    for kind in notes.values():
        for entry in kind.values():
            assert entry["ghi_chu"] in plan_text, "Kế hoạch thiếu nguyên văn ghi_chu đã chốt"
    plan_notes = {"reserve": {}, "hm": {}}
    notes_block = plan_text.split("#### 4.2.1. Văn bản ghi_chu đã chốt", 1)[1].split("### 4.3.", 1)[0]
    kind = "reserve"
    for line in notes_block.splitlines():
        if line.startswith("**Tám dòng HM**"):
            kind = "hm"
        if line.startswith("| "):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) == 2 and cells[0] != "Từ":
                for word in cells[0].split(", "):
                    plan_notes[kind][word] = cells[1]
    assert plan_notes == {kind: {w: r["ghi_chu"] for w, r in words.items()} for kind, words in notes.items()}
    for path in (JOINT_FILES["phan-loai.tsv"], JOINT_FILES["honorable-mentions.tsv"]):
        git_path = str(path.relative_to(ROOT)).replace("\\", "/")
        previous = subprocess.check_output(["git", "show", "1734b43:" + git_path],
                                           cwd=ROOT, text=True, encoding="utf-8")
        before = list(csv.DictReader(io.StringIO(previous), delimiter="\t"))
        with path.open(encoding="utf-8", newline="") as stream:
            after = list(csv.DictReader(stream, delimiter="\t"))
        assert [r["tu"] for r in before] == [r["tu"] for r in after]
        for old, new in zip(before, after):
            for column, value in old.items():
                if column == "bang_chung":
                    assert new[column].startswith(value), (old["tu"], column)
                else:
                    assert new[column] == value, (old["tu"], column)
    owner_record = subprocess.check_output(
        ["git", "show", "1734b43:analyzing-tools/ho-so/unified/du-phong-v2-cau-hoi.md"],
        cwd=ROOT, text=True, encoding="utf-8",
    )
    assert "**Answer (owner, 2026-11-20):** 3" in owner_record
    assert "**Yêu cầu rà/thay chính riêng:**" in owner_record
    for row in reserve + hm:
        if row["cau_hoi"]:
            for question in row["cau_hoi"].split(";"):
                assert question in qtext, question
        if row["tranh_chap"] != "KHONG":
            assert row["cau_hoi"], row["tu"]
    preview = proposed_document(data, reserve, hm)
    assert "| Từ | Tầng | Lý do | Việc còn thiếu |" in preview
    for row in reserve:
        if row["tang_chung"] in {"C", "D"}:
            assert f"| {row['tu']} | {row['tang_chung']} | {row['ghi_chu']} | {row['con_thieu']} |" in preview
    canonical = subprocess.check_output(
        ["git", "show", summary["base_commit"] + ":analyzing-tools/wordlist.txt"], cwd=ROOT)
    assert canonical == (TOOLS / "wordlist.txt").read_bytes().replace(b"\r\n", b"\n")
    payload = json.dumps({"doc": preview, "wordlist": canonical.decode("utf-8")}, ensure_ascii=False)
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
    pycode = """
import json,pathlib,runpy,sys
p=json.load(sys.stdin); root=pathlib.Path.cwd(); rb=pathlib.Path.read_bytes; rt=pathlib.Path.read_text
def b(path):return p['wordlist'].encode('utf-8') if path.resolve()==root/'analyzing-tools'/'wordlist.txt' else rb(path)
def t(path,*args,**kw):return p['doc'].replace('\\r\\n','\\n') if path.resolve()==root/'WordListAnalyze.md' else rt(path,*args,**kw)
pathlib.Path.read_bytes=b;pathlib.Path.read_text=t
runpy.run_path(str(root/'analyzing-tools'/'check_wordlist.py'),run_name='__main__')
"""
    jscode = """
import fs from 'node:fs';import path from 'node:path';import {pathToFileURL} from 'node:url';
const native=fs.readFileSync,p=JSON.parse(native(0,'utf8')),root=process.cwd();
fs.readFileSync=function(file,opt){
 if(typeof file==='string'){
  const f=path.resolve(file).toLowerCase();let s;
  if(f===path.join(root,'analyzing-tools','wordlist.txt').toLowerCase())s=p.wordlist;
  if(f===path.join(root,'WordListAnalyze.md').toLowerCase())s=p.doc;
  if(s!==undefined){const enc=typeof opt==='string'?opt:opt?.encoding;return enc?s:Buffer.from(s,'utf8');}
 }
 return native.apply(this,arguments);
};
await import(pathToFileURL(path.join(root,'analyzing-tools','verify.mjs')).href);
"""
    build_preview_code = """
import json,pathlib,runpy,sys
p=json.load(sys.stdin);root=pathlib.Path.cwd();rt=pathlib.Path.read_text
def t(path,*args,**kw):
 if path.resolve()==root/'WordListAnalyze.md':
  return p['doc'] if kw.get('newline')=='' else p['doc'].replace('\\r\\n','\\n')
 return rt(path,*args,**kw)
pathlib.Path.read_text=t
script=root/'analyzing-tools'/'build_wordlist.py';sys.argv=[str(script),'--check']
runpy.run_path(str(script),run_name='__main__')
"""
    build_lf_code = """
import json,pathlib,runpy,sys
p=json.load(sys.stdin);root=pathlib.Path.cwd();rt=pathlib.Path.read_text
def t(path,*args,**kw):
 value=p['doc'] if path.resolve()==root/'WordListAnalyze.md' else rt(path,*args,**kw)
 if path.resolve() in {root/'index.html',root/'thong-tin.html',root/'WordListAnalyze.md'}:
  return value.replace('\\r\\n','\\n')
 return value
pathlib.Path.read_text=t
script=root/'analyzing-tools'/'build_wordlist.py';sys.argv=[str(script),'--check']
runpy.run_path(str(script),run_name='__main__')
"""
    original_payload = json.dumps({"doc": (ROOT / "WordListAnalyze.md").read_text(encoding="utf-8"),
                                   "wordlist": canonical.decode("utf-8")}, ensure_ascii=False)
    commands = [
        ("native_python", [sys.executable, "-X", "utf8", "-B", str(TOOLS / "check_wordlist.py")], None, 1),
        ("native_node", ["node", str(TOOLS / "verify.mjs")], None, 1),
        ("build_check", [sys.executable, "-X", "utf8", "-B", str(TOOLS / "build_wordlist.py"), "--check"], None, 0),
        ("preview_python_canonical_LF", [sys.executable, "-X", "utf8", "-B", "-c", pycode], payload, 0),
        ("preview_node_canonical_LF", ["node", "--input-type=module", "-e", jscode], payload, 0),
        ("build_edited_document_CRLF", [sys.executable, "-X", "utf8", "-B", "-c", build_preview_code], payload, 0),
        ("build_LF_baseline_known_limit", [sys.executable, "-X", "utf8", "-B", "-c", build_lf_code], original_payload, 1),
        ("build_LF_edited_known_limit", [sys.executable, "-X", "utf8", "-B", "-c", build_lf_code], payload, 1),
    ]
    runs = []
    for label, args, stdin, expected in commands:
        result = subprocess.run(args, cwd=ROOT, input=stdin, encoding="utf-8",
                                capture_output=True, env=env)
        runs.append({"label": label, "argv": args, "exit_code": result.returncode,
                     "expected": expected, "stdout": result.stdout, "stderr": result.stderr})
    assert runs[0]["stdout"].count("LỖI |") == 1 and "C1:" in runs[0]["stdout"]
    assert runs[1]["stdout"].count("LỖI |") == 3 and "C1:" in runs[1]["stdout"] and "C8:" in runs[1]["stdout"]
    assert "Ba khối khớp wordlist.txt." in runs[5]["stdout"]
    assert all("ValueError: substring not found" in r["stderr"] for r in runs[6:8])
    protected_now = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                     for name in ("index.html", "thong-tin.html", r"analyzing-tools\wordlist.txt")}
    doc = (ROOT / "WordListAnalyze.md").read_bytes()
    protected_now["WordListAnalyze.md section10 bytes"] = hashlib.sha256(
        doc[doc.index("## 10. Danh sách 7.776 từ phát hành".encode()):
            doc.index("## 11. Danh sách dự phòng".encode())]).hexdigest()
    assert protected_now == summary["protected"]
    legacy = json.loads((EV / "revision-1-audit.json").read_text(encoding="utf-8"))["legacy_files_sha256_bytes"]
    assert all(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest for name, digest in legacy.items())
    for name, metadata in INPUTS.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == metadata["sha256_bytes"], name
    for path in JOINT_FILES.values():
        raw = path.read_bytes()
        assert not raw.startswith(b"\xef\xbb\xbf") and raw.endswith(b"\r\n")
        assert raw.count(b"\r\n") == raw.count(b"\n"), path
        assert all(line == line.rstrip(" \t") for line in raw.decode("utf-8").splitlines()), path
    proof_data = {
        "runs": runs, "protected_bytes_unchanged": True, "all_expected": all(r["exit_code"] == r["expected"] for r in runs),
        "preview_section10_byte_identical": True,
        "preview_doc_sha256_bytes": hashlib.sha256(preview.encode("utf-8")).hexdigest(),
        "preview_saved_to_disk": False, "native_checkers_pass": False,
        "canonical_is_exact_git_blob": True, "fresh_D6_run": False,
        "draft_rows": [len(reserve), len(hm)], "unique_keys_including_main": len(data["main"]) + len(reserve) + len(hm),
        "hm_counted_N": sum(r["ket_luan_nhap"] == "CUNG_DE_CU_CHUA_PHAT_HANH" for r in hm),
        "reserve_agreed_H7_hold": "ngoại trừ / ngoại trú; T-dpv2-9; chưa ký mức K trước khi đo",
        "build_edited_document_CRLF_pass": runs[5]["exit_code"] == 0,
        "build_LF_baseline_and_edited_same_known_error": True,
        "legacy_files_unchanged": True, "legacy_files_sha256_bytes": legacy,
        "question_links_valid": True, "inputs_still_match": len(INPUTS),
        "owner_Q1_answer_commit_verified": "1734b43",
        "open_questions": [],
        "publication_templates_match_plan": True,
        "T10_public_reasons": summary["public_notes"],
        "draft_data_unchanged_except_added_reasons_and_appended_refs": True,
        "draft_output_sha256_bytes": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in JOINT_FILES.values()},
        "document_format": "UTF-8 không BOM, CRLF, không khoảng trắng cuối dòng, có dòng cuối",
    }
    save_json(EV / "joint-proof.json", proof_data)
    log = []
    for r in runs:
        log.extend(["=== " + r["label"], "argv=" + json.dumps(r["argv"], ensure_ascii=False),
                    "exit=" + str(r["exit_code"]), r["stdout"].rstrip(), r["stderr"].rstrip(), ""])
    log.append("Mô phỏng nằm trong bộ nhớ; không ghi bản sao glossary hoặc sửa vùng bảo vệ.")
    (EV / "joint-proof.log").write_text("\n".join(log) + "\n", encoding="utf-8", newline="\r\n")
    proof_data["artifact_catalog_rows"] = catalog_artifacts()
    save_json(EV / "joint-proof.json", proof_data)
    assert proof_data["all_expected"], "Kết quả cổng khác dự kiến; xem joint-proof.log"
    return {k: v for k, v in proof_data.items() if k != "runs"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prove", action="store_true")
    args = parser.parse_args()
    for path in [
        OPUS / "round-1-analysis.md", OPUS / "round-1-cross-review.md",
        OPUS / "round-1-review-drafts.md", OPUS / "evidence" / "h7-quet-bo-sung.tsv",
        OPUS / "evidence" / "de-xuat-hop-nhat.py", OPUS / "evidence" / "kiem-h8-chinh-thuc.py",
        OUT / "round-1-analysis.md", OUT / "round-1-cross-review.md",
        TOOLS / "manifest.json", TOOLS / "README.md", TOOLS / "tieu-chi-thong-nhat.md",
        TOOLS / "check_wordlist.py", TOOLS / "verify.mjs", TOOLS / "build_wordlist.py",
        ROOT / "WordListAnalyze.md", EV / "joint-build.py",
        EV / "revision-1-audit.json",
    ]:
        read(path)
    data, reserve, hm, summary = build()
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.prove:
        print(json.dumps(proof(data, reserve, hm, summary), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
