"""Đối số trên các blob fc97441; giữ kết quả và phán quyết lần 1 đúng theo mốc của chúng."""
import csv
import io
import json
import subprocess
from collections import Counter
from pathlib import Path

E = Path(__file__).resolve().parent
ROOT = E.parents[4]
AT = ROOT / "analyzing-tools"
U = AT / "ho-so" / "unified"
O = AT / "ho-so" / "opus" / "ra-thay-chinh" / "evidence"


def load(p):
    b = subprocess.check_output(["git", "show", "fc97441:" + p.relative_to(ROOT).as_posix()], cwd=ROOT)
    return list(csv.DictReader(io.StringIO(b.decode("utf-8-sig")), delimiter="\t"))


def index(rs, col="tu"):
    out = {r[col]: r for r in rs}
    assert len(out) == len(rs)
    return out


def main():
    astra = [r for r in load(E / "ky1-xep-lai-astra.tsv") if r["ro"] == "T_RTC_14"]
    opus = index(load(O / "xep-lai-rtc.tsv"))
    merged = load(U / "ra-thay-chinh-thay-the.tsv")
    counts = Counter(r["vai_tro"] for r in astra)
    assert counts == {"VAO":116, "DU_BI":2, "HM":25}
    queue = [r for r in merged if r["vai_tro"] != "RA"]
    assert [r["tu"] for r in queue] == [r["tu"] for r in astra]
    assert opus.keys() == index(queue).keys() == index(astra).keys()
    rank = index(load(U / "xep-hang.tsv"))
    labels = load(AT / "labels.tsv")
    for a, m in zip(astra, queue, strict=True):
        o = opus[a["tu"]]
        assert a["vai_tro"] == m["vai_tro"] == o["vai_tro"]
        assert a["thu_tu"] == o["thu_tu"] and int(m["thu_tu"]) == int(a["thu_tu"]) + (116 if a["vai_tro"]=="DU_BI" else 0)
        assert a["hang_S4"] == m["hang_S4"] == o["hang_moi"] and a["diem_100"] == o["diem_100_moi"]
        assert a["khoa"] == o["khoa"] == rank[a["tu"]]["khoa"]
        assert m["hang_S4_cu"] == o["hang_cu"] == rank[a["tu"]]["hang"]
    ra = {r["tu"]: r["ma"] for r in merged if r["vai_tro"]=="RA"}
    assert ra == {r["tu"]:r["ma"] for r in load(E / "ky1-tu-ra.tsv")} and len(ra)==116
    blocks = {r["khoa"]:r["ma"] for r in load(E / "ky1-khoa-chan.tsv")}
    assert blocks == {rank[w]["khoa"]:v for w,v in ra.items() if v in {"K0","K1"}} | {"baotu":"K1","lamco":"K1"}
    assert len(blocks)==94 and {k for k,v in blocks.items() if v=="K0"}=={"phanbac","tinhkhi","nieu"}
    assert "hang" not in labels[0] and len(index(labels,"khoa"))==7981
    assert Counter(r["trang_thai"] for r in labels) == {"CHINH":7776,"DU_PHONG":205}
    for row in labels:
        assert all(row[c] == rank[row["tu"]][c] for c in ("khoa","nhan","lop","F","G","T","diem"))
    hm = index(load(AT / "honorable-mentions.tsv"))
    for a in astra:
        if a["vai_tro"]=="HM":
            w = a["tu"]
            assert w not in index(labels) and all(hm[w][c] == rank[w][c] for c in ("lop","F","diem"))
    signatures = load(U / "chu-ky.tsv")
    chia = [r for r in signatures if r["khoa"]=="chia" and r["tu"]=="chia" and r["loai_ky"]=="K2" and r["hieu_luc"]=="CO"]
    assert len(chia)==2 and {r["nguoi_ky"] for r in chia}=={"Astra","Opus"}
    fam = load(AT / "spelling_families.tsv")
    pairs = {(a.strip(),b.strip()) for r in fam for a in r["chuan"].split("/") for b in r["bien_the"].split("/")}
    passed = {(r["tu"],r["bien_the"]) for r in load(U / "ra-thay-chinh-h5.tsv") if r["trang_thai"]=="DONG_THUAN_QUA"}
    assert len(passed)==15 and passed & pairs=={("bít tết","bíp tết")}
    assert {("giỡn","rỡn"),("nuốt chửng","nuốt trửng"),("theo dõi","theo rõi"),("thư giãn","thư dãn")} <= passed-pairs
    print(json.dumps({"commit":"fc97441","co_so":len(rank),"T7_khop":len(astra),"ra":len(ra),
                      "thu_tu":dict(counts),"du_bi":[r["tu"] for r in astra if r["vai_tro"]=="DU_BI"],
                      "khoa_chan":len(blocks),"ho_qua_can_them":len(passed-pairs),"chu_ky_chia_cu":len(chia),
                      "nhan_khop_P6_lich_su":len(labels)},ensure_ascii=False))


if __name__=="__main__":
    main()
