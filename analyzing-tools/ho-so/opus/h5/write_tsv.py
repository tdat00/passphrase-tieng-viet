#!/usr/bin/env python3
"""Ghi files/discussion/ho-chinh-ta-ban-dau.tsv từ h5/verdicts.json + các điều chỉnh đã đọc ngữ cảnh."""
import json
import os
import unicodedata as ud

HERE = os.path.dirname(os.path.abspath(__file__))
OPUS = os.path.dirname(HERE)
DISC = os.path.join(os.path.dirname(OPUS), "discussion")
nfc = lambda s: ud.normalize("NFC", s)
V = json.load(open(os.path.join(HERE, "verdicts.json"), encoding="utf-8"))


def words(name):
    return {l.split("|")[0] for l in open(os.path.join(OPUS, name), encoding="utf-8").read().splitlines() if l.strip()}


O, A = words("current.txt"), words("astra.txt")
HND = {}
for name in ("Viet11K", "Viet22K", "Viet39K", "Viet74K"):
    for w in open(os.path.join(OPUS, "data", f"{name}.txt"), encoding="utf-8").read().splitlines():
        HND.setdefault(" ".join(nfc(w.strip().lower()).replace("-", " ").split()), set()).add(name[4:])

# Điều chỉnh sau khi đọc lượt bị gắn cờ "vắt từ" (chỉ ở cặp mà kết luận phụ thuộc bộ lọc):
# (sub_chuan, sub_kia, web_chuan, web_kia), (sub dòng khác nhau: chuan, kia)
ADJ = {
    "dao động": ((103, 12, 3043, 57), (94, 10),
                 "Đọc lượt bị gắn cờ: 5/5 lượt giao động là lỗi thật (mẫu 'dao động từ X đến Y' bị gắn cờ nhầm vì có từ 'động từ'); "
                 "4/5 lượt dao động bị gắn cờ là đúng từ. Số chính 12/115 = 10,4%; bỏ dòng trùng 10/104 = 9,6%: sát ngưỡng."),
    "xác suất": ((80, 10, 944, 8), (76, 9),
                 "Đọc lượt bị gắn cờ: 3 lượt 'cái xác xuất hiện' là vắt từ, 1 lượt 'xác xuất chính xác' là lỗi thật. 10/90 = 11,1%; bỏ dòng trùng 9/85 = 10,6%."),
}
NOTES = {
    "bánh chưng": "Đọc đủ 18/18 lượt web của 'bánh trưng': đều là 'bánh | trưng bày' (vắt từ), 0 lượt viết sai tên bánh. Số 24% cũ sai. Chủ dự án quyết giữ.",
    "năng suất": "Đọc đủ 8 lượt phụ đề bị gắn cờ: đều vắt từ (tài năng | xuất chúng, khả năng | xuất hiện…); còn 1 lỗi thật.",
    "súc tích": "Phụ đề mọi dòng 17/3 (đủ 20) → loại; bỏ dòng trùng 15/3 (dưới 20) → qua. Web thô 172 lượt 'xúc tích' gần hết là cảm xúc | tích cực.",
    "yên trí": "Chưa xác nhận được loại: 'yên chí' không có trong HND (và theo Astra không có ở hai bản Wiktionary) nhưng chiếm 8/17 lượt phụ đề.",
    "giấu giếm": "Astra: Wiktionary tiếng Anh ghi 'giấu diếm' là lỗi viết → nên là loại d; kết luận loại không đổi.",
    "giòn tan": "Giữ loại c (Astra: có chứng cứ biến thể giòn/dòn ở tiếng gốc); phụ đề chỉ 10 lượt nên thiếu dữ liệu.",
    "ô tô": "Qua H5g nhưng viết liền 'oto' chỉ 3 chữ: trượt H2.",
    "bảy mươi": "Qua H5 nhưng là chuỗi số sản sinh: trượt H3.",
    "dông dài": "Không kho nào đủ 20 lượt, không có chứng cứ lỗi: chỉ đi tiếp khi hai bên ký (H5d, nhánh thiếu dữ liệu).",
    "vẻ đẹp": "'vẽ đẹp' còn là cụm đúng (vẽ + đẹp); tỉ lệ chỉ là cận trên của lỗi.",
    "chia sẻ": "'chia xẻ' còn có nghĩa xẻ, tách vật; tỉ lệ chỉ là cận trên.",
    "lặp lại": "Web thô 1.327 lượt 'lập lại' phần lớn là 'thiết lập | lại'; vẫn chờ đọc nghĩa (loại e).",
    "thìa là": "'thì là' phần lớn là từ nối thì + là (loại e).",
    "để dành": "'để giành' phần lớn là để + giành (thắng lợi…) (loại e).",
    "taxi": "Cộng các dạng chỉ khác dấu phân cách; còn phải qua H3, H6, H7 như mọi mục.",
    "radio": "Cộng các dạng chỉ khác dấu phân cách; còn phải qua H3, H6, H7 như mọi mục.",
    "micrô": "Không dạng nào đạt 95% ở cả hai kho.",
    "mô tơ": "'motor' không có trong HND; không dạng nào đạt 95% ở cả hai kho.",
    "đô la": "Ở phụ đề dạng có gạch hoặc viết liền chiếm đa số; dạng 'đô la' vẫn có chứng cứ không gạch.",
    "mì": "Áp cho cả họ khi mì/mỳ là một tiếng nguyên của từ (bánh mì…), không dò chuỗi con.",
}
OVERRIDE = {"dao động": "CHO_SAT_NGUONG", "súc tích": "CHO_SAT_NGUONG", "yên trí": "CHO_LOAI"}


def verdict(t, a, b, c, d):
    ts, tw = a + b, c + d
    if t == "e":
        return "CHO_NGHIA"
    if t == "g":
        return "QUA_H5G"
    if t in ("b", "c", "f"):
        if ts < 20 or tw < 20:
            return "LOAI_THIEU_DU_LIEU"
        if 100 * a >= 95 * ts and 100 * c >= 95 * tw:
            return "QUA_RIENG_H5"
        return "LOAI_CANH_TRANH"
    dom = [(x, y) for x, y in ((a, b), (c, d)) if x + y >= 20]
    if any(10 * y >= x + y for x, y in dom):
        return "LOAI_LOI"
    if any(20 * y >= x + y for x, y in dom):
        return "TRU_DIEM"
    return "QUA_RIENG_H5" if dom else "QUA_RIENG_H5_THIEU_DU_LIEU"


def pct(b, a):
    return f"{100 * b / (a + b):.1f}" if a + b else "-"


def main():
    head = ["chuan", "bien_the", "loai_H5", "HND_chuan", "HND_bien_the",
            "sub_chuan", "sub_bien_the", "ti_le_sub_%", "web_chuan", "web_bien_the", "ti_le_web_%",
            "sub_dong_khac_chuan", "sub_dong_khac_bien_the", "ti_le_sub_dong_khac_%",
            "sub_chuan_tho", "sub_bien_the_tho", "web_chuan_tho", "web_bien_the_tho",
            "ket_luan", "trong_ds_chuan", "trong_ds_bien_the", "ghi_chu"]
    lines = ["\t".join(head)]
    for r in V:
        a0, b0 = r["A"][0], r["B"][0]
        t = r["loai"]
        if a0 == "giấu giếm":
            t = "d"
        main_c = list(r["main"])
        sens = [r["dist_clean"][0], r["dist_clean"][1]]
        note = NOTES.get(a0, "")
        if a0 in ADJ:
            main_c, sens2, note = list(ADJ[a0][0]), ADJ[a0][1], ADJ[a0][2]
            sens = list(sens2)
        v = OVERRIDE.get(a0) or verdict(t, *main_c)
        raw = r["raw"]
        mem = lambda forms: "".join(x for x, s in (("O", O), ("A", A)) if any(f in s for f in forms)) or "-"
        hnd = lambda f: ",".join(sorted(HND.get(" ".join(f.replace("-", " ").split()), set()), key=lambda x: (len(x), x))) or "-"
        lines.append("\t".join(map(str, [
            " / ".join(r["A"]), " / ".join(r["B"]), t, hnd(a0), hnd(b0),
            main_c[0], main_c[1], pct(main_c[1], main_c[0]), main_c[2], main_c[3], pct(main_c[3], main_c[2]),
            sens[0], sens[1], pct(sens[1], sens[0]),
            raw[0], raw[1], raw[2], raw[3], v, mem(r["A"]), mem(r["B"]), note])))
    p = os.path.join(DISC, "ho-chinh-ta-ban-dau.tsv")
    open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    print("ghi", p, len(lines) - 1, "dòng")


if __name__ == "__main__":
    main()
