#!/usr/bin/env python3
"""Kiểm hình thức giải nghĩa theo huong-dan-giai-nghia.md. Không chứa nghĩa của từ nào.

Bản nháp (người viết tự kiểm một lô):
    python kiem-tra-giai-nghia.py lo-XX.txt lo-XX.tsv
Cổng gộp (người điều phối, trước khi nhập thành phẩm; kiểm cả trùng giữa các lô):
    python kiem-tra-giai-nghia.py --phat-hanh lo-01.txt lo-01.tsv lo-02.txt lo-02.tsv ...

Thoát mã 1 nếu còn LỖI. CẢNH BÁO là chỗ cần đọc lại.
"LỖI LÔ" là lỗi của file lô đầu vào: người viết báo lại người điều phối, không tự sửa.
"""
import re
import sys
import unicodedata as ud

HEADER = "tu\tgiai_nghia\tco"
FLAGS = {"NHAY_CAM", "TUC_PHU", "HAI_NGHIA", "NGHI", "KHONG_BIET"}
OPEN_FLAGS = {"NHAY_CAM", "TUC_PHU", "NGHI", "KHONG_BIET"}  # phải được người soát đóng trước khi phát hành
MAX_CHARS = 110
SYL_MIN, SYL_MAX = 5, 15
VI_BASE = set("abcdeghiklmnopqrstuvxyđ")
PUNCT_OK = set(" ,.;:()-/")

WORD = re.compile(r"[^\W\d_]+")
ABBREV = re.compile(r"(?i)(?<![^\W\d_])(v\.v|vd|v\.d|tr\.)(?![^\W\d_])")
NEW_STYLE = re.compile(r"(?i)^(?!qu)[^\W\d_]*(o[àáảãạ]|o[èéẻẽẹ]|u[ỳýỷỹỵ])$")
SUBJECTIVE = re.compile(r"(?i)(?<![^\W\d_])((tốt|đẹp|ngon|hay|giỏi|tiện lợi|quan trọng|nổi tiếng|phổ biến) nhất|tuyệt vời|ai cũng|nhà nào cũng)(?![^\W\d_])")
DATED = re.compile(r"(?i)(?<![^\W\d_])(hiện nay|ngày nay|bây giờ|gần đây|mới nhất|năm nay)(?![^\W\d_])")


def nfc(s):
    return ud.normalize("NFC", s)


def base_letter(c):
    return ud.normalize("NFD", c.lower())[0]


def whole(phrase, text):
    return re.search(r"(?<![^\W\d_])" + re.escape(phrase) + r"(?![^\W\d_])", text, re.IGNORECASE) is not None


def read_raw(path):
    raw = open(path, "rb").read()
    try:
        return raw, raw.decode("utf-8")
    except UnicodeDecodeError as e:
        sys.exit(f"{path}: không phải UTF-8 ({e})")


def read_batch(path, issues):
    """Đọc lô từ; mọi sai sót đều là LỖI LÔ, không âm thầm sửa."""
    def bad(n, msg):
        issues.append((path, n, "", "LỖI LÔ", msg))
    raw, text = read_raw(path)
    if text.startswith("\ufeff"):
        bad(0, "có BOM ở đầu file")
        text = text[1:]
    if "\r" in text:
        bad(0, "có kí tự CR (cần xuống dòng LF)")
        text = text.replace("\r", "")
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    elif lines:
        bad(0, "thiếu xuống dòng cuối file")
    words = []
    for n, w in enumerate(lines, 1):
        if not w.strip():
            bad(n, "dòng trống")
            continue
        if w != w.strip() or "  " in w:
            bad(n, f"thừa dấu cách: “{w}”")
        if w != nfc(w):
            bad(n, f"từ chưa ở dạng NFC: “{nfc(w)}”")
        words.append(w)
    if not words:
        bad(0, "lô không có từ nào")
    seen = set()
    for w in words:
        if w in seen:
            bad(0, f"từ lặp trong lô: “{w}”")
        seen.add(w)
    return words


def check_definition(add, word, gloss, flags):
    if gloss != nfc(gloss):
        add("LỖI", "giải nghĩa chưa ở dạng NFC")
    gloss = nfc(gloss)
    if gloss != gloss.strip() or "  " in gloss:
        add("LỖI", "thừa dấu cách ở đầu, cuối hoặc giữa câu")
    if len(gloss) > MAX_CHARS:
        add("LỖI", f"dài {len(gloss)} kí tự (> {MAX_CHARS})")
    syl = WORD.findall(gloss)
    if not SYL_MIN <= len(syl) <= SYL_MAX:
        add("CẢNH BÁO", f"{len(syl)} tiếng (nên {SYL_MIN}–{SYL_MAX})")
    if not gloss[:1].isalpha() or not gloss[:1].isupper():
        add("LỖI", "chữ đầu phải là chữ cái viết hoa")
    if not gloss.endswith(".") or gloss.endswith(".."):
        add("LỖI", "phải kết thúc bằng đúng một dấu chấm")
    if gloss[:-1].count(".") or any(c in gloss for c in "!?…"):
        add("LỖI", "chỉ được một câu: không có dấu chấm, chấm than, chấm hỏi hay ba chấm ở giữa")
    bad = set()
    for c in gloss:
        cat = ud.category(c)
        if c == "|" or c in "\"“”„«»'’‘`":
            bad.add(c)
        elif cat == "Nd" or cat.startswith("N"):
            add("LỖI", f"có chữ số “{c}”: viết số bằng chữ")
        elif cat in ("Cf", "Cc", "Co", "Cs", "Cn"):
            add("LỖI", f"có kí tự ẩn hoặc điều khiển U+{ord(c):04X}")
        elif c.isalpha():
            if base_letter(c) not in VI_BASE:
                add("LỖI", f"có chữ ngoài bảng chữ cái tiếng Việt “{c}”")
        elif c not in PUNCT_OK and not c.isspace():
            bad.add(c)
        elif c.isspace() and c != " ":
            add("LỖI", f"khoảng trắng lạ U+{ord(c):04X}")
    if bad:
        add("LỖI", "có kí tự cấm: " + " ".join(sorted(bad)))
    if ABBREV.search(gloss):
        add("LỖI", "có chữ viết tắt")
    first = syl[0].lower() if syl else ""
    if first in ("là", "xem", "như"):
        add("LỖI", f"mở đầu bằng “{syl[0]}”")
    head = word.lower().split()
    if [s.lower() for s in syl[: len(head)]] == head:
        add("LỖI", "mở đầu bằng chính đầu mục")
    elif whole(word, gloss):
        add("CẢNH BÁO", "câu lặp lại nguyên đầu mục")
    newstyle = sorted({s for s in syl if NEW_STYLE.match(s)})
    if newstyle:
        add("LỖI", "đặt dấu kiểu mới (dùng kiểu cũ như hòa, thủy): " + ", ".join(newstyle))
    for rx, msg in ((SUBJECTIVE, "lời khen chê hoặc tuyệt đối"), (DATED, "thông tin mau cũ")):
        m = rx.search(gloss)
        if m:
            add("CẢNH BÁO", f"{msg}: “{m.group(0)}”")
    semis = gloss.count(";")
    if semis > 1:
        add("LỖI", "quá hai nghĩa: chỉ được một dấu chấm phẩy")
    if semis == 1 and "HAI_NGHIA" not in flags:
        add("LỖI", "có dấu chấm phẩy nhưng thiếu cờ HAI_NGHIA")
    if "HAI_NGHIA" in flags and semis == 0:
        add("LỖI", "có cờ HAI_NGHIA nhưng không có dấu chấm phẩy")


def check_pair(batch_path, tsv_path, release, issues, glosses):
    words = read_batch(batch_path, issues)
    raw, text = read_raw(tsv_path)
    out = []

    def file_err(msg):
        issues.append((tsv_path, 0, "", "LỖI", msg))
    if text.startswith("\ufeff"):
        file_err("có BOM ở đầu file")
        text = text[1:]
    if "\r" in text:
        file_err("có kí tự CR, hãy dùng xuống dòng LF")
        text = text.replace("\r", "")
    if text and not text.endswith("\n"):
        file_err("thiếu xuống dòng cuối file")
    rows = text.split("\n")
    if rows and rows[-1] == "":
        rows.pop()
    start = 1
    if rows and rows[0] == HEADER:
        rows, start = rows[1:], 2
    else:
        issues.append((tsv_path, 1, "", "LỖI", "dòng đầu phải là tiêu đề: tu<TAB>giai_nghia<TAB>co"))
        if rows and words and rows[0].split("\t")[0] != words[0]:
            rows, start = rows[1:], 2
    if len(rows) != len(words):
        file_err(f"có {len(rows)} dòng giải nghĩa, lô có {len(words)} từ")
    for i, row in enumerate(rows):
        n = i + start
        parts = row.split("\t")
        if len(parts) != 3:
            issues.append((tsv_path, n, row[:30], "LỖI", f"cần đúng 3 cột ngăn bằng tab, đang có {len(parts)}"))
            continue
        word, gloss, flag_text = parts
        out.append(word)

        def add(level, msg, n=n, word=word):
            issues.append((tsv_path, n, word, level, msg))
        if i < len(words) and word != words[i]:
            add("LỖI", f"từ không khớp lô (cần “{words[i]}”, đúng thứ tự, chép nguyên)")
        flags = flag_text.split(";") if flag_text else []
        unknown = [f for f in flags if f not in FLAGS]
        if unknown:
            add("LỖI", "cờ không hợp lệ: " + ", ".join(unknown))
        if len(set(flags)) != len(flags):
            add("LỖI", "cờ bị lặp")
        if "KHONG_BIET" in flags and len(set(flags)) > 1:
            add("LỖI", "KHONG_BIET không đi cùng cờ khác")
        if release and set(flags) & OPEN_FLAGS:
            add("LỖI", "cờ chưa đóng: " + ", ".join(sorted(set(flags) & OPEN_FLAGS)) + " (người soát phải xử lý trước khi phát hành)")
        if not gloss:
            if release:
                add("LỖI", "giải nghĩa trống")
            elif not set(flags) & {"KHONG_BIET", "NHAY_CAM"}:
                add("LỖI", "giải nghĩa trống (chỉ được để trống khi có cờ KHONG_BIET hoặc NHAY_CAM)")
            elif set(flags) & {"HAI_NGHIA", "NGHI"}:
                add("LỖI", "giải nghĩa trống thì không dùng cờ HAI_NGHIA hay NGHI")
            continue
        if "KHONG_BIET" in flags:
            add("LỖI", "cờ KHONG_BIET thì để trống giải nghĩa")
            continue
        check_definition(add, word, gloss, flags)
        key = nfc(gloss).casefold()
        if key in glosses:
            add("LỖI", f"trùng nguyên văn giải nghĩa của “{glosses[key]}”")
        else:
            glosses[key] = word
    return out


def main(argv):
    release = "--phat-hanh" in argv
    files = [a for a in argv[1:] if a != "--phat-hanh"]
    if not files or len(files) % 2 or (not release and len(files) != 2):
        sys.exit(__doc__)
    issues, glosses, seen = [], {}, {}
    for j in range(0, len(files), 2):
        for w in check_pair(files[j], files[j + 1], release, issues, glosses):
            if w in seen:
                issues.append((files[j + 1], 0, w, "LỖI", f"đầu mục đã có ở {seen[w]}"))
            seen.setdefault(w, files[j + 1])
    errors = sum(1 for x in issues if x[3] != "CẢNH BÁO")
    for path, n, word, level, msg in sorted(issues, key=lambda x: (x[0], x[1], x[3] == "CẢNH BÁO")):
        where = f"dòng {n}" if n else "file"
        prefix = f"{path} | " if release else ""
        print(f"{prefix}{where} | {word} | {level} | {msg}")
    print(f"Tổng: {len(seen)} dòng, {errors} lỗi, {len(issues) - errors} cảnh báo.")
    return 1 if errors else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main(sys.argv))
