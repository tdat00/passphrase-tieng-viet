"""Hàm dùng chung cho các script phân tích dự phòng v2 (Opus). Chỉ đọc dữ liệu trong repo."""
import csv
import hashlib
import json
import sys
import unicodedata
from pathlib import Path

csv.field_size_limit(10**9)
HERE = Path(__file__).resolve().parent
OUT = HERE.parent
REPO = HERE.parents[4]
AT = REPO / "analyzing-tools"
U = AT / "ho-so" / "unified"
D = AT / "ho-so" / "discussion"
# Bản tạm của bốn danh sách HND (GPL): đặt ngoài repo qua biến môi trường HND_DIR; không lưu vào repo.
HND_DIR = Path(__import__("os").environ.get("HND_DIR", str(HERE / "_tam-hnd")))

SUB_TOKENS = 34314528  # OpenSubtitles VI v2018 (tieu-chi-thong-nhat.md mục 0)
WEB_TOKENS = 149860716  # CCAligned VI v1, dòng khác nhau
# Mẫu số mà cổng P2 đã ký thật sự dùng (tap-luat-P2-v4.json, tong_am_tiet). Vòng 1 của Opus dùng hai số ở trên;
# chỉ "bánh củ cải" (15 lượt web) đổi kết quả H8. Xem round-1-cross-review.md, mục 4.
SUB_TOKENS_P2 = 34329387
WEB_TOKENS_P2 = 150070912

ALPHABET = "a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y".split()
RANK = {c: i for i, c in enumerate(ALPHABET)}
TONES = {"\u0300": 1, "\u0309": 2, "\u0303": 3, "\u0301": 4, "\u0323": 5}


def strip(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c)).replace("đ", "d").replace("Đ", "D")


def key(w):
    return strip(w).lower().replace(" ", "")


def o1(w):
    out = []
    for syl in w.split(" "):
        tone, base = 0, ""
        for ch in unicodedata.normalize("NFD", syl):
            if ch in TONES:
                tone = TONES[ch]
            else:
                base += ch
        out.append((tuple(RANK.get(c, 99) for c in unicodedata.normalize("NFC", base)), tone))
    return tuple(out)


def rd(path, mine=False):
    """Đọc TSV. mine=True: tệp do các script này ghi, đổi '-' ở cột cuối về chuỗi rỗng."""
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if mine and rows:
        last = list(rows[0].keys())[-1]
        for r in rows:
            if r[last] == "-":
                r[last] = ""
    return rows


def lines(path):
    return [l.strip() for l in open(path, encoding="utf-8") if l.strip()]


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def sha_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_tsv(path, header, rows):
    """UTF-8 không BOM, CRLF (quy ước working tree của repo, core.autocrlf=true), có dòng cuối.
    Ô trống ở cột cuối ghi '-' để dòng không kết thúc bằng khoảng trắng."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(header) + "\r\n")
        for r in rows:
            vals = ["" if r.get(h) is None else str(r.get(h)).strip() for h in header]
            for v in vals:
                assert "\t" not in v and "\n" not in v and "\r" not in v, v
            if vals and vals[-1] == "":
                vals[-1] = "-"
            f.write("\t".join(vals) + "\r\n")


def write_lines(path, items):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("".join(str(x).rstrip() + "\r\n" for x in items))


def p1_table():
    """Bảng khóa P1: trả về dict mặt chữ -> các số đo (theo vị trí ứng viên)."""
    out = {}
    vec = ["ung_vien", "nguon", "opensub_n", "ccaligned_n", "leipzig_so_cau", "tatoeba_so_cau", "so_khoi",
           "nguon_tu_dien_so_bo", "ket_qua_uv_P2", "ly_do_cong", "co_loai", "canh_bao_can_doc"]
    with open(D / "bang-khoa-chung.tsv", encoding="utf-8", newline="") as f:
        rdr = csv.DictReader(f, delimiter="\t")
        for r in rdr:
            v = {k: json.loads(r[k]) for k in vec if r.get(k)}
            for i, w in enumerate(v["ung_vien"]):
                out[w] = {"khoa": r["khoa"], "trang_thai_khoa": r["trang_thai_khoa"],
                          **{k: v[k][i] if isinstance(v.get(k), list) and i < len(v[k]) else None for k in vec}}
    return out


def counts_opus():
    """Số lượt OPUS (Opus đếm lại theo ranh giới H5): mặt chữ -> dict."""
    out = {}
    for r in rd(U / "opus-counts.tsv"):
        if r["vai_tro"] == "UNG_VIEN":
            out[r["tu"]] = r
    return out


def h8(sub_sach, web_sach, leip, tato):
    """H8: MANH nếu ≥0,1 PPM ở phụ đề hoặc web (số sạch), hoặc ≥2 câu Leipzig, hoặc ≥1 câu Tatoeba."""
    vals = [sub_sach, web_sach, leip, tato]
    if all(v is None for v in vals):
        return "CHUA_DO"
    s = (sub_sach or 0) / SUB_TOKENS * 1e6
    w = (web_sach or 0) / WEB_TOKENS * 1e6
    if s >= 0.1 or w >= 0.1 or (leip or 0) >= 2 or (tato or 0) >= 1:
        return "MANH"
    if any((v or 0) > 0 for v in vals):
        return "YEU"
    return "KHONG"


def out_utf8():
    sys.stdout.reconfigure(encoding="utf-8")
