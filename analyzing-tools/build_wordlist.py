#!/usr/bin/env python3
"""Sinh các khối danh sách từ `wordlist.txt` (nguồn chuẩn, mỗi dòng `từ|giải nghĩa`).

    python build_wordlist.py           # ghi lại ba khối
    python build_wordlist.py --check   # chỉ so, thoát 1 nếu có khối lệch
    python build_wordlist.py --lo DIR  # xuất DIR/lo-01.txt và DIR/lo-01.tsv cho kiem-tra-giai-nghia.py

Ba khối được sinh:
- `index.html`, khối `#wordlist`: mỗi dòng `từ,` (CRLF).
- `thong-tin.html`, khối `#wordlist`: mỗi dòng `từ|giải nghĩa` (CRLF).
- `WordListAnalyze.md`, khối ```text đầu tiên sau tiêu đề mục 10: mỗi dòng `từ|giải nghĩa`.
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SCRIPT_OPEN = '<script type="text/plain" id="wordlist">'
DOC_HEADING = "## 10. Danh sách 7.776 từ phát hành"


def read_list():
    lines = (HERE / "wordlist.txt").read_text(encoding="utf-8").splitlines()
    pairs = [line.split("|") for line in lines]
    bad = [i + 1 for i, p in enumerate(pairs) if len(p) != 2 or not p[0] or not p[1]]
    if bad:
        sys.exit(f"wordlist.txt: dòng sai định dạng: {bad[:10]}")
    return pairs


def splice(text, start_marker, end_marker, body, nl):
    start = text.index(start_marker) + len(start_marker)
    start = text.index(nl, start) + len(nl)
    end = text.index(end_marker, start)
    return text[:start] + body + text[end:]


def build(pairs):
    out = {}
    for name, lines in (("index.html", [f"{w}," for w, _ in pairs]),
                        ("thong-tin.html", [f"{w}|{d}" for w, d in pairs])):
        text = (REPO / name).read_text(encoding="utf-8", newline="")
        out[name] = (text, splice(text, SCRIPT_OPEN, "</script>", "".join(l + "\r\n" for l in lines), "\r\n"))
    name = "WordListAnalyze.md"
    text = (REPO / name).read_text(encoding="utf-8", newline="")
    nl = "\r\n" if "\r\n" in text else "\n"
    head = text.index(DOC_HEADING)
    fence = text.index("```text", head)
    new = text[:fence] + splice(text[fence:], "```text", "```", "".join(f"{w}|{d}{nl}" for w, d in pairs), nl)
    out[name] = (text, new)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="chỉ kiểm, không ghi")
    ap.add_argument("--lo", type=Path, help="xuất lô cho kiem-tra-giai-nghia.py vào thư mục này, không ghi repo")
    args = ap.parse_args()
    if args.lo:
        pairs = read_list()
        args.lo.mkdir(parents=True, exist_ok=True)
        (args.lo / "lo-01.txt").write_text("".join(w + "\n" for w, _ in pairs), encoding="utf-8", newline="\n")
        # Cờ HAI_NGHIA ứng với câu có hai nghĩa nối bằng ";" (hướng dẫn giải nghĩa, mục 10)
        rows = "".join(f"{w}\t{d}\t{'HAI_NGHIA' if ';' in d else ''}\n" for w, d in pairs)
        (args.lo / "lo-01.tsv").write_text("tu\tgiai_nghia\tco\n" + rows, encoding="utf-8", newline="\n")
        print(f"python kiem-tra-giai-nghia.py --phat-hanh {args.lo / 'lo-01.txt'} {args.lo / 'lo-01.tsv'}")
        return
    changed = []
    for name, (old, new) in build(read_list()).items():
        if old != new:
            changed.append(name)
            if not args.check:
                (REPO / name).write_text(new, encoding="utf-8", newline="")
    if args.check:
        print("Lệch: " + ", ".join(changed) if changed else "Ba khối khớp wordlist.txt.")
        sys.exit(1 if changed else 0)
    print("Đã ghi: " + ", ".join(changed) if changed else "Không có gì thay đổi.")


if __name__ == "__main__":
    main()
