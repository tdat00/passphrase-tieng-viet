"""Đối chiếu độc lập các bảng hợp nhất, phiếu ký và thay đổi 2cc6aec..91d8ee9."""
import csv
import hashlib
import io
import json
import subprocess
from pathlib import Path

E = Path(__file__).resolve().parent
A, AT = E.parent, E.parents[3]
U, O = AT / "ho-so" / "unified", AT / "ho-so" / "opus" / "ra-thay-chinh"


def read(path, rev="91d8ee9"):
    spec = rev + ":" + path.relative_to(AT.parent).as_posix()
    buf = subprocess.check_output(["git", "show", spec], cwd=AT.parent)
    return list(csv.DictReader(io.StringIO(buf.decode("utf-8-sig")), delimiter="\t"))


def index(data, fields):
    ix = {tuple(r[k] for k in fields):r for r in data}
    assert len(ix) == len(data)
    return ix


def signatures():
    aa = read(A / "khep-muc-mo-1.tsv")
    oa = read(O / "khep-muc-mo-1-opus.tsv")
    added = read(A / "khep-muc-mo-2.tsv")
    hm1, hm2 = read(A / "hm-chu-ky-1.tsv"), read(O / "hm-chu-ky-1-opus.tsv")
    h7 = read(U / "ra-thay-chinh-h7.tsv")
    keep_main = {r["tu_chinh"] for r in h7 if r["trang_thai"].endswith("GIU_DA_KY_PHIEU")}
    assert len(keep_main) == 237 and all(r["chu_ky_phieu"]=="Astra+Opus" for r in h7 if r["tu_chinh"] in keep_main)
    k_a = {r["tu_hoac_khoa"] for r in aa if r["ky_astra"]=="Y" and r["de_xuat_astra"]=="GIU_K2"}
    k_a |= {r["tu_hoac_khoa"] for r in added if r["ky_astra"]=="Y" and r["de_xuat_astra"]=="GIU_K2"}
    k_o = {r["tu_hoac_khoa"] for r in oa if r["ky_opus"]=="Y"}
    expect = keep_main | {"thay lông"}
    assert k_a == expect and expect <= k_o
    kh = {r["tu"] for r in hm1 if r["ket_qua_H"].startswith("K2")}
    assert len(kh)==5 and kh=={r["tu"] for r in hm2 if r["ky_opus"]=="Y"}
    assert set(r["tu"] for r in hm1).issubset({r["tu"] for r in hm2})
    assert all(r["ly_do"].strip() for r in added+aa+oa+hm1+hm2)
    old = read(U / "chu-ky.tsv")
    assert {r["nguoi_ky"] for r in old if r["tu"]=="chia" and r["loai_ky"]=="K2" and r["hieu_luc"]=="CO"}=={"Astra","Opus"}
    return sorted(kh),len(expect)


def main():
    diff = {}
    for stem, fields in (("h5",["tu","bien_the"]),("h7",["khoa"]),("thay-the",["vai_tro","tu"])):
        file = U / f"ra-thay-chinh-{stem}.tsv"
        old, new = (index(read(file, rev),fields) for rev in ("2cc6aec","91d8ee9"))
        changed = sorted(k for k in old.keys() & new.keys() if old[k]!=new[k])
        diff[stem] = {"doi_dong":len(changed),"them_dong":len(new.keys()-old.keys()),"bo_dong":len(old.keys()-new.keys())}
        if stem=="h7":
            assert {k[0] for k in changed}=={"cancu","tienluong","trieu","banthan"}
            assert all(old[k]["trang_thai"]=="TRANH_CHAP" and new[k]["quyet_dinh_chu"]=="D-rtc-7: K2" and
                       new[k]["astra"]==new[k]["opus"]=="K2" for k in changed)
        if stem=="thay-the":
            assert old.keys()-new.keys()=={("RA_NEU_CHU_DU_AN_THEO_ASTRA",w) for w in ("cần cù","tiền lương","triệu","bạn thân")}
            assert new.keys()-old.keys()=={("HM",r["tu"]) for r in read(A / "hm-chu-ky-1.tsv")}
            assert not changed
        if stem=="h5":
            assert old==new
    hm,total=signatures()
    d8 = read(AT / "nguon-goc-giai-nghia.tsv")
    slots=read(U/"ra-thay-chinh-thay-the.tsv")
    reserve={r["tu"] for r in slots if r["vai_tro"] in {"VAO","DU_BI"}}
    hmw={r["tu"] for r in slots if r["vai_tro"]=="HM"}
    assert reserve.isdisjoint({r["tu"] for r in d8})
    assert hmw <= {r["tu"] for r in d8 if r["trang_thai"]=="LOAI" and r["cong_loai"].startswith(("D6","D7"))}
    families=read(AT / "spelling_families.tsv")
    existing={tuple(sorted((r["chuan"],part.strip()))) for r in families for part in r["bien_the"].split("/")}
    late={r["tu"]:(r["bien_the"],i) for i,r in enumerate(read(U / "ra-thay-chinh-h5.tsv"),2)
          if r["trang_thai"]=="DONG_THUAN_QUA" and r["tu"] in {"giỡn","nuốt chửng","theo dõi","thư giãn"}}
    assert len(late)==4 and all(tuple(sorted((w,alt))) not in existing for w,(alt,_) in late.items())
    js={"revision":"91d8ee9","diff_depuis":"2cc6aec","tsv":diff,"K2_chinh_va_vao":total,"K2_HM":hm,
        "D8_118_ung_vien_du_phong_chua_co_dong":len(reserve),"D8_HM_da_co_dong_LOAI":len(hmw),
        "ho_H5_QUA_bo_sung_T_rtc_16_chua_co_trong_bang_goc":late,
        "sha256_script":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (E / "ky1-kiem-bang.json").write_bytes((json.dumps(js,ensure_ascii=False,indent=2)+"\n").replace("\n","\r\n").encode())
    print(diff, "; chữ ký:",total,"+",len(hm),"; D8:",len(reserve),"/",len(hmw))


if __name__=="__main__":
    main()
