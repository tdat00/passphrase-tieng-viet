"""Đọc bản in qua OCR ở RAM; SHA-1 phân phối, SHA-256 dòng, chỉ số dòng 1-based. Không lưu lời từ điển."""
import argparse
import csv
import hashlib
import io
import re
import unicodedata as ud
import urllib.parse
import urllib.request
from pathlib import Path

EV = Path(__file__).resolve().parent
URL = "https://ia601608.us.archive.org/2/items/tu-dien-tieng-viet-vien-ngon-ngu-hoc/" + urllib.parse.quote("Tu dien tieng Viet_Vien Ngon ngu hoc_djvu.txt")
SHA1 = "31e3c22434339a722e8636e05ebe195c13dfd510"
GROUPS = {
    "H5": "bảng hiệu|bản hiệu|bộc phát|bội phát|bột phát|chun|thun|cột mốc|cột mốt|dí dỏm|rí rỏm|giỡn|rỡn|giun|dun|hạt dẻ|hạt giẻ|hì hục|hì hụi|lăn tăn|lăm tăm|lằng nhằng|loằng nhoằng|lon ton|long tong|lòng vòng|lòng dòng|nuốt chửng|nuốt trửng|ọp ẹp|ọt ẹt|qua quýt|qua quít|rậm rạp|giậm giạp|ròng rã|ròn rã|ru rú|giu giú|sền sệt|sềnh sệch|tép riu|tép diu|theo dõi|theo rõi|thư giãn|thư dãn|xà bông|sà bông|xanh|sanh",
    "VAO": "làm cỏ|thay lòng|màng màng|xoành xoạch|xành xạch|xoàn xoạt|thụp|chụp|thụt|loáng thoáng|loáng choáng|rướn|dướn|rướm|xầm xì|sầm sì",
    "H7": "áo ngự|báng|bẽ mặt|bê bối|căn cứ|chàm|chăn dắt|chầu|chủng|chứng|cô đồng|cơ động|công đoàn|còng|cuồng|cưỡng|điểm nhãn|diễu hành|đình|đổ bác|động dục|động đực|ghèn|ho hắng|hở hang|hoàng đạo|hoảng sợ|khạc|khụy|khuỵ|làm khổ|lôi thôi|mất nước|nang|nạng|ngập|nghẻo|niệu|nòng|ống thở|quyền|ranh|rúng động|thiêu|thỉnh|tịch|tiên lượng|tinh tử|tong|tông|tống|trần|trận|triều|truồng|trượng|vật vã",
    "K2": "ăn bĩnh|ăn đút|ăn lường|bà vãi|bán thân|chổng lái|chẩn|cô đầu|có vú|dê cụ|đồng cô|giối giăng|hạ thọ|hố tiểu|mèo mỡ|mó máy|ngọng|phướng|sán dây|tam điểm|tự ải|tiện nữ|trôn|vọng cung|vô tự",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("group", choices=GROUPS)
    ap.add_argument("--inspect", action="store_true")
    a = ap.parse_args()
    with urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "VietnameseWordlistReview/1.0"}), timeout=65) as r:
        body = r.read()
    assert hashlib.sha1(body).hexdigest() == SHA1
    lines = ud.normalize("NFC", body.decode("utf-8")).splitlines()
    text = "\n".join(lines)
    hits = []
    for w in GROUPS[a.group].split("|"):
        pat = re.compile(r"(?im)^[^a-zÀ-ỹ\d\n]{0,2}" + re.escape(w) + r"(?=[^\w\n]|$)[^\n]*")
        rs = []
        for m in pat.finditer(text):
            n = text.count("\n", 0, m.start()) + 1
            line = lines[n-1]
            row = (w, n, hashlib.sha256(line.encode("utf-8")).hexdigest())
            if len(rs) < 3:
                rs.append(row)
                if a.inspect:
                    print(f"{w} @{n}: {line[:108]}")
        if a.inspect and not rs:
            print(f"{w}: không có dòng mở đầu khớp OCR; không suy vắng trong bản in")
        hits.extend(rs)
    out = io.StringIO()
    writer = csv.writer(out, delimiter="\t", lineterminator="\r\n")
    writer.writerow(("tu", "dong_ocr_khop_chuoi", "sha256_dong_NFC", "sha1_toan_ban", "url"))
    writer.writerows((*row, SHA1, URL) for row in hits)
    (EV / f"km1-ban-in-{a.group}.tsv").write_bytes(out.getvalue().encode("utf-8"))


if __name__ == "__main__":
    main()
