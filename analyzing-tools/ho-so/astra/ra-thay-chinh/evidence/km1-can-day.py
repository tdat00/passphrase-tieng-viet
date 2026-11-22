"""Đọc lại chỉ các ID có dây thun; tìm cửa sổ chắc nghĩa để SA duyệt cận dưới, không lưu cửa sổ."""
import csv
import gzip
import hashlib
import io
import json
import re
import sys
import unicodedata as ud
import urllib.request
from pathlib import Path

EV = Path(__file__).resolve().parent
AT = EV.parents[3]
L = "abcdefghijklmnopqrstuvwxyzăâđêôơưàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ"
RX = re.compile(f"[{L}]+|[^\\s{L}]+")
CLUE = re.compile("đàn hồi|cao su|co giãn|co dãn|bungee|buộc|chằng|ràng đồ|cột tóc|thắt nút")


def main():
    cards = {}
    with (EV / "km1-day-web.tsv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["tu"] == "thun":
                cards.setdefault(int(r["id_dong"]), []).append((int(r["i_token"]), r["blake2b128_dong"]))
    cfg = json.loads((AT / "manifest.json").read_text(encoding="utf-8"))
    url = next(r["url"] for r in cfg["nguon_du_lieu"] if r["source"].startswith("CCAligned VI"))
    chosen = []
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "VietnameseWordlistReview/1.0"}), timeout=80) as r:
        with gzip.GzipFile(fileobj=r) as payload:
            for n, raw in enumerate(payload, 1):
                if n not in cards:
                    continue
                digest = hashlib.blake2b(raw.rstrip(b"\r\n"), digest_size=16).hexdigest()
                words = RX.findall(ud.normalize("NFC", raw.decode("utf-8", "ignore").lower()))
                for i, orig in cards[n]:
                    assert orig == digest and words[i-1:i+1] == ["dây", "thun"]
                    clip = " ".join(words[max(0, i-6):i+8])
                    if CLUE.search(clip) and not re.search("không co|không đàn|không có độ", clip):
                        chosen.append((n, i, digest))
                        if "--inspect" in sys.argv[1:]:
                            print(f"{n}/{i}: {clip}")
                        break
                if len(chosen) == 44:
                    break
    buf = io.StringIO()
    out = csv.writer(buf, delimiter="\t", lineterminator="\r\n")
    out.writerow(("id_dong", "i_token", "blake2b128_dong", "trang_thai"))
    out.writerows((*row, "MAU_CHO_SA_DOC") for row in chosen)
    (EV / "km1-can-day-web.tsv").write_bytes(buf.getvalue().encode("utf-8"))
    print("Số dòng khác nhau có tín hiệu để SA duyệt:", len(chosen))


if __name__ == "__main__":
    main()
