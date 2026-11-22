"""Mẫu đúng nghĩa: hai dòng khác nhau sau offset theo seed của từng mặt chữ. Không lưu câu."""
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

from screen_core import AT, EV, save_tsv


def main():
    with (EV / "hm1-doi-chung.tsv").open(encoding="utf-8") as f:
        words = {r["tu"] for r in csv.DictReader(f, delimiter="\t")}
    terms = words | {"chía", "tương dương", "cố giao"}
    offset = {w: 1 + int.from_bytes(hashlib.sha256(("rtc-hm-H8-20261122|" + w).encode()).digest()[:4], "big") % 40000 for w in terms}
    rx = re.compile(r"(?<!\w)(" + "|".join(re.escape(w) for w in sorted(terms, key=lambda x: (-len(x), x))) + r")(?!\w)")
    got = {w: {} for w in terms}
    cfg = json.loads((AT / "manifest.json").read_text(encoding="utf-8"))
    spec = next(r for r in cfg["nguon_du_lieu"] if r["source"].startswith("OpenSubtitles"))
    with urllib.request.urlopen(urllib.request.Request(spec["url"], headers={"User-Agent": "VietnameseWordlistReview/1.0"}), timeout=80) as r:
        blob = r.read()
    assert hashlib.sha256(blob).hexdigest() == spec["sha256"]
    with gzip.GzipFile(fileobj=io.BytesIO(blob)) as text:
        for n, raw in enumerate(text, 1):
            line = ud.normalize("NFC", raw.decode("utf-8", "ignore").strip().lower())
            for hit in rx.finditer(line):
                w = hit.group()
                if n < offset[w] or len(got[w]) >= 2:
                    continue
                right, left = line[hit.end():], line[:hit.start()]
                if w == "chia" and not re.match(r"\s+(đều|đôi|thành|phần|cho|nhau)\b", right):
                    continue
                if w == "biển" and not (re.search(r"\b(tắm|ngoài|bờ|nước)\s+$", left) or re.match(r"\s+(khơi|xanh)\b", right)):
                    continue
                if w in {"xe điện", "tàu điện"} and re.match(r"\s+ngầm\b", right):
                    continue
                if w == "vòi hoa sen" and not re.search(r"\b(nước|tắm|chảy|mở|bật|phòng)\b", left + " " + right):
                    continue
                if w == "cố giao" and re.match(r"\s+(tiếp|dịch|thương)\b", right):
                    continue
                digest = hashlib.blake2b(raw.rstrip(b"\r\n"), digest_size=16).hexdigest()
                clip = " ".join(line[:hit.start()].split()[-4:] + [w] + line[hit.end():].split()[:4])
                got[w].setdefault(digest, (n, hit.start(), clip))
            if all(len(x) == 2 for x in got.values()):
                break
    data = []
    for w in sorted(terms):
        samples = []
        for h, (n, i, clip) in got[w].items():
            samples.append(f"{n}:{clip}")
            data.append(dict(tu=w, offset_seed=offset[w], id_dong=n, vi_tri_chu=i, blake2b128_dong=h))
        if "--inspect" in sys.argv[1:]:
            print(f"{w}: " + " / ".join(samples))
    save_tsv(EV / "hm1-h8-id.tsv", data)


if __name__ == "__main__":
    main()
