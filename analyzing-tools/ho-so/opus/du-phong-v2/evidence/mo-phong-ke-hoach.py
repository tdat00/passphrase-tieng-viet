"""Review bản nháp chung: tự dựng (ngoài repo) bản sao các tệp cần cho ba bộ kiểm, áp đúng các thay đổi văn bản mà
U/du-phong-v2-ke-hoach.md mô tả cho WordListAnalyze.md (đầu tài liệu, mục lục, §11 đến hết tệp), điền token bằng
nội dung thử, rồi chạy check_wordlist.py, verify.mjs và build_wordlist.py --check trên bản đó.

    python mo-phong-ke-hoach.py <thư mục tạm NGOÀI repo> [--crlf] [--goc] [--nhan <nhãn>]

Mặc định lấy blob LF của HEAD; --crlf lấy tệp working tree (CRLF); --goc không áp chỉnh sửa (đo nền để so);
--nhan thêm nhãn vào tên log để giữ log của lượt trước.
Log: mo-phong-ke-hoach[-<nhãn>][-nen][-crlf].log. Không ghi gì vào repo ngoài log trong evidence/; thư mục tạm bị xóa.
Token chỉ được điền khi có trong mẫu (bản sửa 1 của kế hoạch đã viết thẳng hai đoạn cố định thay cho token).
"""
import os
import re
import shutil
import subprocess
import sys
from chung import *

out_utf8()
tam = Path(sys.argv[1]).resolve()
CRLF = "--crlf" in sys.argv[2:]  # dùng tệp working tree (CRLF) thay cho bản LF của HEAD
GOC = "--goc" in sys.argv[2:]  # không áp chỉnh sửa: đo nền để so
NHAN = sys.argv[sys.argv.index("--nhan") + 1] if "--nhan" in sys.argv else ""
assert REPO not in tam.parents and tam != REPO, "thư mục tạm phải nằm ngoài repo"
plan = (U / "du-phong-v2-ke-hoach.md").read_text(encoding="utf-8").replace("\r\n", "\n")
sec51 = plan[plan.index("### 5.1."):plan.index("### 5.2.")]
blocks = re.findall(r"```markdown\n(.*?)```", sec51, re.S)
assert len(blocks) == 2, len(blocks)
header_new, toc_new = blocks[0], blocks[1]
sec52 = plan[plan.index("### 5.2."):]
s1112 = re.search(r"````markdown\n(.*?)````", sec52, re.S).group(1)
log = []
try:
    files = ["index.html", "thong-tin.html", "WordListAnalyze.md", "analyzing-tools/wordlist.txt", "analyzing-tools/labels.tsv",
             "analyzing-tools/blocked_keys.tsv", "analyzing-tools/spelling_families.tsv", "analyzing-tools/check_wordlist.py",
             "analyzing-tools/verify.mjs", "analyzing-tools/build_wordlist.py", "analyzing-tools/du-phong.txt"]
    for f in files:
        if CRLF:
            data = (REPO / f).read_bytes()
        else:
            data = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{f}"], capture_output=True, check=True).stdout
        p = tam / f
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
    doc_path = tam / "WordListAnalyze.md"
    doc = doc_path.read_bytes().decode("utf-8").replace("\r\n", "\n")
    old10 = doc[doc.index("## 10. Danh sách 7.776 từ phát hành"):doc.index("## 11. Danh sách dự phòng (chưa phân tích)")]
    # 1) dòng "> - **Dự phòng:**" duy nhất
    lines_ = doc.split("\n")
    idx = [i for i, l in enumerate(lines_) if l.startswith("> - **Dự phòng:**")]
    log.append(f"so_dong_du_phong_header: {len(idx)}")
    lines_[idx[0]] = header_new.rstrip("\n")
    # 2) dòng 11 của mục lục
    idx = [i for i, l in enumerate(lines_) if l.startswith("11. [Danh sách dự phòng (chưa phân tích)]")]
    log.append(f"so_dong_toc_11: {len(idx)}")
    lines_[idx[0]] = toc_new.rstrip("\n")
    doc = "\n".join(lines_)
    # 3) §11 cũ đến hết tệp
    start = doc.index("## 11. Danh sách dự phòng (chưa phân tích)")
    du = (tam / "analyzing-tools/du-phong.txt").read_text(encoding="utf-8").rstrip("\n")
    fill = {"{{BANG_TANG}}": "| Tầng | OK không-F | OK-F | Tổng |\n|---|---:|---:|---:|\n| A | 1 | 1 | 2 |",
            "{{BANG_CANH_BAO}}": "| Từ | Tầng | Mã | Việc thiếu | Nguồn |\n|---|---|---|---|---|\n| x | D | H5 | - | - |",
            "{{DU_PHONG_205}}": du, "{{CHINH_SACH_UNG_VIEN}}": "Đoạn chính sách.",
            "{{BANG_NHOM_HM}}": "| Nhóm | Số |\n|---|---:|\n| D6_CUOI | 1 |",
            "{{BANG_TU_HM}}": "| Từ | Nhóm |\n|---|---|\n| y | R1 |", "{{NGUON_NGOAI_DANH_MUC}}": "Câu cố định."}
    body = s1112
    BAT_BUOC = ("{{BANG_TANG}}", "{{BANG_CANH_BAO}}", "{{DU_PHONG_205}}", "{{BANG_NHOM_HM}}", "{{BANG_TU_HM}}")
    for k in BAT_BUOC:
        assert k in body, k
    co_mat = [k for k in fill if k in body]
    for k in co_mat:
        body = body.replace(k, fill[k])
    assert "{{" not in body
    log.append("token_da_dien: " + ", ".join(k.strip("{}") for k in co_mat))
    doc = doc[:start] + body
    if not GOC:
        doc_path.write_bytes((doc.replace("\n", "\r\n") if CRLF else doc).encode("utf-8"))
    log.append("che_do: " + ("working tree CRLF" if CRLF else "HEAD LF") + (", KHÔNG áp chỉnh sửa (nền)" if GOC else ", đã áp chỉnh sửa"))
    new10 = doc[doc.index("## 10. Danh sách 7.776 từ phát hành"):doc.index("## 11. Danh sách dự phòng (đã phân tích, chưa phát hành)")]
    if not GOC:
        log.append(f"muc10_giu_nguyen_byte: {old10 == new10}")
        log.append(f"so_lan_tieu_de_muc10: {doc.count('## 10. Danh sách 7.776 từ phát hành')}")
        log.append("anchor_moi: " + ", ".join(a for a in ("#11-danh-sách-dự-phòng-đã-phân-tích-chưa-phát-hành",
                                                         "#12-từ-có-thể-cân-nhắc-honorable-mentions") if a in doc))
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    for name, cmd in (("check_wordlist.py", ["python", "check_wordlist.py"]), ("verify.mjs", ["node", "verify.mjs"]),
                      ("build_wordlist.py --check", ["python", "build_wordlist.py", "--check"])):
        r = subprocess.run(cmd, cwd=tam / "analyzing-tools", capture_output=True, text=True, encoding="utf-8", env=env)
        log.append(f"{name} ma_thoat: {r.returncode}")
        log += ["  " + l for l in (r.stdout.strip().splitlines()[-2:] or r.stderr.strip().splitlines()[-1:])]
finally:
    shutil.rmtree(tam, ignore_errors=True)
ten = "mo-phong-ke-hoach" + (f"-{NHAN}" if NHAN else "") + ("-nen" if GOC else "") + ("-crlf" if CRLF else "") + ".log"
(HERE / ten).write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
print("\n".join(log))
