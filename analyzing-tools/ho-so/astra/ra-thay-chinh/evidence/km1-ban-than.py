"""Đọc thêm ca đa nghĩa bán thân trong phụ đề: câu trước/sau chỉ ở RAM; lưu ID và băm."""
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
RX = re.compile(r"(?<!\w)bán\s+thân(?!\w)")
NHAN = {
    "MAI_DAM_RO": {1236053, 1236056, 4651749},
    "GOI_MAI_DAM_KHONG_DUNG_LAM_CAN_DUOI": {795082, 953307, 1675582, 2293086, 2831064, 3393188, 4789794, 4797488, 4797641, 4961010},
    "TUONG_NUA_NGUOI": {474153, 617426, 2672322, 2881787, 2884205, 3028041, 3428241, 3428242, 4368957, 5062283},
    "BAN_MINH_HOAC_LAO_DONG": {1097021, 1097023, 1448201, 3239515, 3239524, 3953982, 4354736},
}


def main():
    cfg = json.loads((AT / "manifest.json").read_text(encoding="utf-8"))
    spec = next(r for r in cfg["nguon_du_lieu"] if r["source"].startswith("OpenSubtitles VI"))
    with urllib.request.urlopen(urllib.request.Request(spec["url"], headers={"User-Agent": "VietnameseWordlistReview/1.0"}), timeout=80) as r:
        zip_data = r.read()
    assert hashlib.sha256(zip_data).hexdigest() == spec["sha256"]
    seen, audit = set(), []
    prev, pending = "", None
    with gzip.GzipFile(fileobj=io.BytesIO(zip_data)) as z:
        for n, raw in enumerate(z, 1):
            text = ud.normalize("NFC", raw.decode("utf-8", "ignore").strip().lower())
            if pending:
                num, digest, left, hit = pending
                if "--inspect" in sys.argv[1:]:
                    print(f"{num}: …{left[-60:]} | {hit[:150]} | {text[:60]}…")
                label = next((name for name, ids in NHAN.items() if num in ids), "MO_HO_NHIEU_HOAC_NGHIA_KHAC")
                ctx_hash = hashlib.sha256("\n".join((left, hit, text)).encode()).hexdigest()
                audit.append((num, digest, ctx_hash, label))
                pending = None
            if RX.search(text):
                digest = hashlib.blake2b(raw.rstrip(b"\r\n"), digest_size=16).hexdigest()
                if digest not in seen:
                    pending = (n, digest, prev, text)
                    seen.add(digest)
            prev = text
    b = io.StringIO()
    w = csv.writer(b, delimiter="\t", lineterminator="\r\n")
    assert len(audit) == 38 and len(NHAN["MAI_DAM_RO"]) == 3
    w.writerow(("id_dong", "blake2b128_dong", "sha256_3_dong_NFC_ha_chu", "nhan_Astra"))
    w.writerows(audit)
    (EV / "km1-ban-than-id.tsv").write_bytes(b.getvalue().encode("utf-8"))


if __name__ == "__main__":
    main()
