"""Kiểm 168 câu dự phòng có nghĩa: băm token theo đúng cách của d6-kiem.py rồi đối với log D6 của lượt ghi trong
p7-v4-kiem-ke-D8-chua-chot-astra.tsv; phải khớp băm và kết quả PASS. Không ghi câu giải nghĩa ra tệp.

    python kiem-d6-168.py
"""
import json
import unicodedata as ud
from chung import *

out_utf8()


def tokens(text):  # chép đúng hàm tokens() của analyzing-tools/d6-kiem.py
    text = ud.normalize("NFC", ud.normalize("NFC", text).lower())
    return tuple("".join(c if c.isalpha() else " " for c in text).split())


def token_hash(text):
    return sha_bytes(json.dumps(tokens(text), ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def sha_bytes(b):
    import hashlib
    return hashlib.sha256(b).hexdigest()


logs = {}
for v in ("v1", "v2", "v3"):
    for r in rd(U / f"d6-log-{v}.tsv"):
        logs[(v, r["tu"])] = r
kk = {r["tu"]: r for r in rd(U / "p7-v4-kiem-ke-D8-chua-chot-astra.tsv")}
ok, bad = 0, []
for r in rd(U / "p7-v4-du-phong-168-co-nghia-cho-duyet.tsv"):
    v = kk[r["tu"]]["luot_nguon_gan_nhat"].split("-")[-1]
    l = logs.get((v, r["tu"]))
    if l and l["ket_qua"] == "PASS" and l["sha256_giai_nghia"] == token_hash(r["giai_nghia"]) and l["run_id"] == kk[r["tu"]]["run_id"]:
        ok += 1
    else:
        bad.append(r["tu"])
log = [f"so_cau: {ok + len(bad)}", f"khop_bam_token_va_PASS_va_run_id: {ok}", f"lech: {len(bad)} {bad}"]
(HERE / "kiem-d6-168.log").write_text("\r\n".join(log) + "\r\n", encoding="utf-8", newline="")
print("\n".join(log))
