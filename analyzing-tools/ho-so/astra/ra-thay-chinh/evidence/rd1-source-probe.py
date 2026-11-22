"""Đọc nguồn ở RAM; chỉ lưu revision/hash/membership, không lưu lời từ điển."""
import hashlib
import json
import re
import urllib.parse
import urllib.request
from datetime import date

from dictionary_probe import vietnamese as vietnamese_part
from screen_core import EV, save_tsv


H5 = [
    "co dúm", "sù sì", "rần rộ", "trơ vơ", "sập sình", "xu hào", "lay hoay",
    "xà bông", "xà phòng", "cải xoong", "cải soong",
    "chun", "thun", "hì hục", "hì hụi", "bội phát", "bột phát", "buồm lòng",
    "rí rỏm", "rỡn", "dun", "lăm tăm", "long tong", "ọt ẹt", "rần rần",
    "giậm giạp", "ròn rã", "giu giú", "rung rung", "sềnh sệch", "tâm chí",
    "tép diu", "sanh",
]
H7 = [
    "bợ đỡ", "bên bị", "cà nhắc", "cầm đầu", "chiến", "choáng", "chưởng",
    "cờ trắng", "cơ mật", "dê cụ", "giàng", "giáo", "hung", "hùng hổ",
    "kẻ cả", "khiên", "kiêu", "làm màu", "lê dương", "ngai", "ngáo",
    "ngạo", "nguyền", "nhảm nhí", "nhói", "phòng bị", "phủ đầu", "quả tang",
    "quèn", "sảng", "sa ngã", "sòng", "thai", "thảm thiết", "thộn",
    "thụ án", "tiêm", "trẫm", "trắng trợn", "trình diện", "tướng", "xử án",
]


def main():
    metadata = []
    for lang, words in (("vi", H5 + H7), ("en", H5)):
        for offset in range(0, len(words), 40):
            batch = words[offset:offset + 40]
            params = urllib.parse.urlencode({
                "action": "query", "format": "json", "formatversion": 2,
                "prop": "revisions", "rvprop": "ids|content", "rvslots": "main",
                "titles": "|".join(batch), "redirects": 1,
            })
            url = f"https://{lang}.wiktionary.org/w/api.php?{params}"
            request = urllib.request.Request(url, headers={"User-Agent": "VietnameseWordlistReview/1.0"})
            with urllib.request.urlopen(request, timeout=40) as response:
                data = json.load(response)
            for page in data["query"]["pages"]:
                title = page["title"]
                revision = (page.get("revisions") or [{}])[0]
                text = revision.get("slots", {}).get("main", {}).get("content", "")
                part = vietnamese_part(text, lang)
                rev = revision.get("revid", "-")
                metadata.append({
                    "tu": title, "lang": lang, "revision": rev,
                    "co_trang": bool(text), "co_phan_tieng_Viet": bool(part),
                    "sha256_wikitext": hashlib.sha256(text.encode("utf-8")).hexdigest() if text else "-",
                    "url": f"https://{lang}.wiktionary.org/w/index.php?title={urllib.parse.quote(title)}&oldid={rev}",
                    "ngay": date.today().isoformat(),
                })
                definitions = [
                    line for line in part.splitlines()
                    if re.match(r"^#{1,2}[^#*:]", line)
                ]
                if part and lang == "vi" and title in {
                    "hùng hổ", "làm màu", "nhảm nhí", "sa ngã", "thụ án", "dun",
                    "tâm chí", "tiêm", "giàng", "ngáo", "sanh", "thun", "rần rần",
                }:
                    summary = " / ".join(definitions[:6])[:900]
                    print(f"{lang} | {title} | rev {rev} | {summary or 'Vietnamese section, no simple definition line'}")
    save_tsv(EV / "rd1-dictionary-metadata.tsv", metadata)
    print(f"Metadata only saved: {len(metadata)} records; raw source never written.")


if __name__ == "__main__":
    main()
