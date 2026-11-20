#!/usr/bin/env python3
"""Đếm số lần xuất hiện của từng mục trong danh sách trên một kho văn bản thuần (một câu/dòng).

    python count_corpus.py vi.txt.gz --list wordlist.txt --out dem.tsv [--dedup]

Kho có thể là .txt hoặc .gz. Dòng được hạ chữ thường, chuẩn hóa NFC, cắt thành đoạn tại dấu câu,
rồi tách âm tiết theo khoảng trắng. Một mục nhiều âm tiết chỉ được đếm khi các âm tiết đứng liền nhau
trong cùng một đoạn (không đếm vắt qua dấu câu), theo ranh giới của luật H5.
`--dedup` bỏ dòng trùng nguyên văn (cách đếm kho web CCAligned).
Đầu ra: `tu<TAB>so_luot<TAB>ppm`, ppm = số lượt trên một triệu âm tiết của kho.
Script không ghi lại bất kỳ câu nào của kho.
"""
import argparse
import gzip
import re
import unicodedata
from collections import Counter

SEGMENT = re.compile(r"[^\w\s]+|_+")


def open_text(path):
    return gzip.open(path, "rt", encoding="utf-8", errors="replace") if path.endswith(".gz") else open(path, encoding="utf-8", errors="replace")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus")
    ap.add_argument("--list", default="wordlist.txt", help="danh sách `từ` hoặc `từ|giải nghĩa`, mỗi dòng một mục")
    ap.add_argument("--out", default="dem.tsv")
    ap.add_argument("--dedup", action="store_true")
    args = ap.parse_args()

    entries = [l.split("|")[0].strip() for l in open(args.list, encoding="utf-8") if l.strip()]
    targets = {tuple(e.split(" ")) for e in entries}
    sizes = sorted({len(t) for t in targets})
    counts, total, seen = Counter(), 0, set()
    with open_text(args.corpus) as f:
        for line in f:
            line = unicodedata.normalize("NFC", line.strip().lower())
            if args.dedup:
                if line in seen:
                    continue
                seen.add(line)
            for seg in SEGMENT.split(line):
                toks = seg.split()
                total += len(toks)
                for n in sizes:
                    for i in range(len(toks) - n + 1):
                        gram = tuple(toks[i:i + n])
                        if gram in targets:
                            counts[gram] += 1
    with open(args.out, "w", encoding="utf-8", newline="\n") as out:
        out.write(f"tu\tso_luot\tppm\n")
        for e in entries:
            c = counts[tuple(e.split(" "))]
            out.write(f"{e}\t{c}\t{c * 1e6 / total if total else 0:.4f}\n")
    print(f"{total} âm tiết; {sum(1 for e in entries if counts[tuple(e.split(' '))])}/{len(entries)} mục có xuất hiện")


if __name__ == "__main__":
    main()
