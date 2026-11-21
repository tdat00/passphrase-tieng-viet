"""Đọc Việt–Việt 30K (DICT) trong RAM; chỉ xuất cờ hiển diện và băm của mục tra."""
import csv
import gzip
import hashlib
import importlib.util
import io
import re
import sys
import unicodedata as ud
import urllib.request
import zipfile
from pathlib import Path

EV = Path(__file__).resolve().parent
loader = importlib.util.spec_from_file_location("km1_ban_in", EV / "km1-ban-in.py")
bi = importlib.util.module_from_spec(loader)
loader.loader.exec_module(bi)
URL = "https://web.archive.org/web/20241112031805id_/https://www.informatik.uni-leipzig.de/~duc/Dict/VietViet.zip"
PIN = "1882c078187dfb8db646cd5c21d0b80fb06b03fc44f27c8cade4377fea80567c"
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def decode_num(s):
    n = 0
    for c in s:
        n = n * 64 + ABC.index(c)
    return n


def main():
    words = bi.GROUPS[sys.argv[1]].split("|")
    with urllib.request.urlopen(urllib.request.Request(URL, headers={"User-Agent": "VietnameseWordlistReview/1.0"}), timeout=70) as r:
        raw = r.read()
    assert hashlib.sha256(raw).hexdigest() == PIN
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        data = gzip.decompress(z.read("data/VV/vv30K.dict.dz"))
        index = {}
        for line in z.read("data/VV/vv30K.index").decode("utf-8-sig").splitlines():
            fields = line.split("\t")
            if len(fields) >= 3 and ud.normalize("NFC", fields[0]).lower() in words:
                w, a, n = fields[:3]
                start, size = map(decode_num, (a, n))
                index.setdefault(ud.normalize("NFC", w).lower(), []).append(data[start:start+size])
    buf = io.StringIO()
    wr = csv.writer(buf, delimiter="\t", lineterminator="\r\n")
    wr.writerow(("tu", "co_muc_30K", "sha256_muc", "sha256_nguon"))
    for w in words:
        entries = index.get(w, [])
        wr.writerow((w, int(bool(entries)), ";".join(hashlib.sha256(e).hexdigest() for e in entries) or "-", PIN))
        brief = " / ".join(re.sub(r"\s+", " ", e.decode("utf-8", "replace"))[:130] for e in entries)
        if "--inspect" in sys.argv[2:]:
            print(f"{w}: {brief or '-'}")
    (EV / f"km1-vv-{sys.argv[1]}.tsv").write_bytes(buf.getvalue().encode("utf-8"))


if __name__ == "__main__":
    main()
