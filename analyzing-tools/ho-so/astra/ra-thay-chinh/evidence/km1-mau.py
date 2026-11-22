"""Đếm, lấy mẫu ở RAM; chỉ lưu số, ID và băm. Chạy từ gốc: python -B ...\\km1-mau.py sub|web."""
import argparse
import csv
import gzip
import hashlib
import heapq
import io
import json
import re
import unicodedata as ud
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

EV = Path(__file__).resolve().parent
AT = EV.parents[3]
SEED = "rtc-astra-km1-20261121"
FORMS = """áo ngự|điểm nhãn|đổ bác|khụy|khuỵ|nghẻo|nịch|xoành xoạch|xành xạch|xoàn xoạt|rướn|dướn|rướm|xầm xì|sầm sì|thụp|chụp|thụt|loáng thoáng|loáng choáng|màng màng|làm cỏ|thay lòng|chun|thun|căn cứ|chầu|đình|tiên lượng|bán thân|ghèn|tinh tử|truồng|nòng|thiêu|tịch|còng|cuồng|nang|báng|trận|triều|mất nước|chàm|chăn dắt|động dục|động đực|chủng|ngập|tự ải|mó máy|hì hụi|rỡn|dun|sanh|tép diu|thư dãn|giun|xanh""".split("|")
SAMPLE = set("chun|thun|căn cứ|chầu|đình|tiên lượng|bán thân|làm cỏ|còng|cuồng|nòng|thiêu|tịch|truồng|báng|mất nước|chàm|chăn dắt|mó máy|sanh|dun".split("|"))
TONE = "\u0300\u0309\u0303\u0301\u0323"
LETTERS = "abcdefghijklmnopqrstuvwxyzăâđêôơưàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ"
SPLIT = re.compile(f"[{LETTERS}]+|[^\\s{LETTERS}]+")
VOWELS = set("aăâeêioôơuưy")


def canon(s):
    n = ud.normalize("NFD", s)
    return ud.normalize("NFC", "".join(c for c in n if c not in TONE)) + next((c for c in n if c in TONE), "")


def spellings(t):
    n = canon(t)
    if n[-1] not in TONE:
        return {t}
    base, tone = n[:-1], n[-1]
    return {ud.normalize("NFC", base[:i + 1] + tone + base[i + 1:]) for i, c in enumerate(base) if c in VOWELS}


def save(name, header, rows):
    buf = io.StringIO()
    writer = csv.writer(buf, delimiter="\t", lineterminator="\r\n")
    writer.writerow(header)
    writer.writerows(rows)
    (EV / name).write_bytes(buf.getvalue().encode("utf-8"))


class Tee:
    def __init__(self, resp):
        self.resp, self.sha = resp, hashlib.sha256()

    def read(self, n=-1):
        data = self.resp.read(n)
        self.sha.update(data)
        return data


def download(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "VietnameseWordlistReview/1.0"}), timeout=90)


def dict2():
    ret = set()
    pins = json.loads((EV / "cr1-source-metrics.json").read_text(encoding="utf-8"))["HND_sources"]
    for spec in pins:
        with download(spec["url"]) as response:
            data = response.read()
        assert hashlib.sha256(data).hexdigest() == spec["sha256"]
        for line in data.decode("utf-8-sig").splitlines():
            parts = ud.normalize("NFC", line.strip().lower()).replace("-", " ").split()
            if len(parts) == 2:
                ret.add(tuple(map(canon, parts)))
    return ret


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("corpus", choices=["sub", "web"])
    ap.add_argument("--inspect", action="store_true", help="Chỉ hiện cửa sổ ngắn của mẫu, không lưu")
    ap.add_argument("--h7", action="store_true", help="Bỏ vắt từ cả với mục một khối (H7)")
    ap.add_argument("--day", action="store_true", help="Hiện cửa sổ kiểm cận dây, không lưu")
    a = ap.parse_args()
    cfg = json.loads((AT / "manifest.json").read_text(encoding="utf-8"))
    spec = next(r for r in cfg["nguon_du_lieu"] if r["source"].startswith({"sub": "OpenSubtitles VI", "web": "CCAligned VI"}[a.corpus]))
    d2 = dict2()
    ft = {f: tuple(map(canon, f.split())) for f in FORMS}
    first = defaultdict(list)
    for f, t in ft.items():
        first[t[0]].append((f, t))
    pre = re.compile("|".join(re.escape(s) for s in sorted({s for f in FORMS for s in spellings(f.split()[0])}, key=lambda x: (-len(x), x))))
    seen, cnt, samples, proofs, peek = set(), Counter(), defaultdict(list), [], []
    with download(spec["url"]) as response:
        stream = Tee(response)
        with gzip.GzipFile(fileobj=stream) as gz:
            for ln, raw in enumerate(gz, 1):
                text = ud.normalize("NFC", raw.decode("utf-8", "ignore").lower())
                if not pre.search(text):
                    continue
                digest = hashlib.blake2b(raw.rstrip(b"\r\n"), digest_size=16).digest()
                fresh = digest not in seen
                if a.corpus == "web" and not fresh:
                    continue
                words = SPLIT.findall(text)
                tokens = [canon(w) if w[0] in LETTERS else "#" for w in words]
                found = False
                for i, k in enumerate(tokens):
                    for f, t in first.get(k, ()):
                        j = i + len(t)
                        if tuple(tokens[i:j]) != t:
                            continue
                        found = True
                        cross = (i > 0 and (tokens[i-1], t[0]) in d2) or (j < len(tokens) and (t[-1], tokens[j]) in d2)
                        clean = (len(t) == 1 and not a.h7) or not cross
                        if a.day and fresh and len(peek) < 48 and f == {"web": "thun", "sub": "chun"}[a.corpus] and i and words[i-1] == "dây":
                            peek.append(f"{ln}/{i}: " + " ".join(words[max(0, i-4):min(len(words), j+4)]))
                        cnt[f, "all"] += 1
                        cnt[f, "clean"] += clean
                        cnt[f, "distinct_clean"] += fresh and clean
                        if not clean:
                            continue
                        if f in {"chun", "thun"} and i and words[i-1] == "dây":
                            cnt[f, "day"] += 1
                            cnt[f, "distinct_day"] += fresh
                            proofs.append((f, ln, i, digest.hex(), "CAN_DOC_DAY", int(fresh)))
                        if fresh and f in SAMPLE:
                            h = hashlib.sha256(f"{SEED}|{a.corpus}|{f}|{ln}|{i}".encode()).digest()
                            rank = -int.from_bytes(h, "big")
                            sample = samples[f]
                            if len(sample) < 6 or rank > sample[0][0]:
                                clip = " ".join(words[max(0, i-4):min(len(words), j+4)])
                                item = (rank, ln, i, digest.hex(), clip)
                                if len(sample) < 6:
                                    heapq.heappush(sample, item)
                                else:
                                    heapq.heapreplace(sample, item)
                if found and fresh:
                    seen.add(digest)
        assert stream.sha.hexdigest() == spec["sha256"] and ln == spec["input_lines"]
    cols = ("all", "clean", "distinct_clean", "day", "distinct_day")
    prefix = "km1-h7" if a.h7 else "km1"
    save(f"{prefix}-dem-{a.corpus}.tsv", ("tu", *cols), ((f, *(cnt[f, col] for col in cols)) for f in FORMS))
    save(f"{prefix}-mau-{a.corpus}.tsv", ("tu", "id_dong", "i_token", "blake2b128_dong"), ((f, ln, i, digest) for f in sorted(samples) for _, ln, i, digest, _ in sorted(samples[f], reverse=True)))
    if not a.h7:
        save(f"km1-day-{a.corpus}.tsv", ("tu", "id_dong", "i_token", "blake2b128_dong", "co", "dong_khac"), proofs)
    print(f"{a.corpus}: SHA256={spec['sha256']}, {spec['input_lines']} dòng; mẫu={sum(map(len,samples.values()))}, cờ dây={len(proofs)}", flush=True)
    if a.day:
        print(" | ".join(peek))
    if a.inspect:
        for f in sorted(samples):
            print(f + " | " + " ; ".join(f"{line}/{i}: {clip}" for _, line, i, _, clip in sorted(samples[f], reverse=True)))


if __name__ == "__main__":
    main()
