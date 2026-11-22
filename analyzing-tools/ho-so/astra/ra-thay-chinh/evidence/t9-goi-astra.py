"""Đối trước/sau checkout với HEAD d78e97a; không ghi nghĩa, chỉ in sai khác và số/băm."""
import csv
import hashlib
import io
import json
import re
import subprocess
import unicodedata as ud
from collections import Counter
from pathlib import Path

E=Path(__file__).resolve().parent
ROOT=E.parents[4]; AT=ROOT/"analyzing-tools"; U=AT/"ho-so"/"unified"
BASE="d78e97a"


def data(path,before=False):
    if before:
        return subprocess.check_output(["git","show",BASE+":"+path.relative_to(ROOT).as_posix()],cwd=ROOT)
    return path.read_bytes().replace(b"\r\n",b"\n")


def read(p,old=False):
    return list(csv.DictReader(io.StringIO(data(p,old).decode("utf-8-sig")),delimiter="\t"))


def idx(p,field="tu",old=False):
    records=read(p,old)
    v={r[field]:r for r in records}
    assert len(v)==len(records),p
    return v


def sha(b):
    return hashlib.sha256(b).hexdigest()


def words(old=False):
    return dict(line.split("|",1) for line in data(AT/"wordlist.txt",old).decode().splitlines())


def run():
    actual,prior=words(),words(True)
    add=actual.keys()-prior.keys(); rem=prior.keys()-actual.keys()
    locked=read(U/"ra-thay-chinh-thay-the.tsv")
    accepted=idx(U/"ra-thay-chinh-giai-nghia-dat.tsv")
    wi={r["tu"] for r in locked if r["vai_tro"]=="VAO"}-{"sớm tối"}|{"cả nghĩ"}
    wo={r["tu"]:r["ma"] for r in locked if r["vai_tro"]=="RA"}
    sig=read(U/"chu-ky.tsv")
    report={}
    report["T12"]=len(actual)==len(prior)==7776 and wi==add and wo.keys()==rem and len(wi)==116 and all(actual[w]==prior[w] for w in actual.keys()&prior.keys())
    report["cot_tu_sha256"]=sha(("\n".join(actual)+"\n").encode())
    report["T11"]=set(x for x,r in accepted.items() if r["ket_luan"]=="VAO_CHINH")==wi and {w for w,r in accepted.items() if r["ket_luan"]=="DU_BI_CON_LAI"}=={"cửu chương"} and len([1 for r in accepted.values() if r["ket_luan"]=="HM_CHUA_DUNG"])==24 and "khách hàng" not in accepted
    lb=idx(AT/"labels.tsv"); rank=idx(U/"xep-hang.tsv"); block=idx(AT/"blocked_keys.tsv","khoa")
    baseblock=idx(AT/"blocked_keys.tsv","khoa",True)
    intended={r["khoa"]:r["ma"] for r in read(E/"ky1-khoa-chan.tsv")}
    adds={k:r["ma"] for k,r in block.items() if k not in baseblock}
    report["T2"]=adds==intended and len(adds)==94 and all(block.get(k)==r for k,r in baseblock.items())
    oldlabels=idx(AT/"labels.tsv",old=True)
    report["T4"]=set(actual)=={w for w,r in lb.items() if r["trang_thai"]=="CHINH"} and len({lb[w]["khoa"] for w in actual})==7776 and all(lb[w]["nhan"]=="OK" for w in actual) and sum(lb[w]["lop"]=="F" for w in actual)==77
    assert lb.keys()==oldlabels.keys()-rem
    for w in lb:
        assert all(lb[w][k]==rank[w][k] for k in ("khoa","nhan","lop","F","G","T","diem"))
    effective=Counter((r["tu"],r["nguoi_ky"]) for r in sig if r["loai_ky"]=="K2" and r["hieu_luc"]=="CO")
    package={r["tu_chinh"] for r in read(U/"ra-thay-chinh-h7.tsv") if r["trang_thai"].endswith("GIU_DA_KY_PHIEU")}|{"thay lông"}
    yellow={w for w in actual if "K2" in lb[w]["chu_ky_hai_ben"].split(";")}
    for w in yellow|package|{"biển","bí mật","vận hành","chia","ngắn gọn"}:
        if any(effective[w,sa]!=1 for sa in ("Astra","Opus")): report["T4"]=False
    assert len(package)==238 and package<=yellow
    report["nhan_K2_them_thuc"]=len({w for w in actual if "K2" in lb[w]["chu_ky_hai_ben"].split(";") and "K2" not in oldlabels[w]["chu_ky_hai_ben"].split(";")})
    report["K2_chinh_hieu_luc"]=sum(effective[w,"Astra"]==effective[w,"Opus"]==1 for w in actual)
    split=lambda cell:{s.strip() for s in cell.split("/")}
    oldfam=read(AT/"spelling_families.tsv",True);fam=read(AT/"spelling_families.tsv")
    newfam=[r for r in fam if r["nguon"]=="RA_THAY_CHINH"]
    assert len(newfam)==35 and len(fam)==312 and [r for r in fam if r["nguon"]!="RA_THAY_CHINH"]==oldfam
    for h in read(U/"ra-thay-chinh-h5.tsv"):
        if h["trang_thai"] not in {"DONG_THUAN_THAY","DONG_THUAN_THAY_CHO_LOAI","DONG_THUAN_QUA"}:continue
        w,v=h["tu"],h["bien_the"]
        hits=[r for r in fam if (w in split(r["chuan"]) and v in split(r["bien_the"])) or (v in split(r["chuan"]) and w in split(r["bien_the"]))]
        expected={"DONG_THUAN_THAY":"LOAI_","DONG_THUAN_THAY_CHO_LOAI":"CHO_LOAI","DONG_THUAN_QUA":"QUA"}[h["trang_thai"]]
        assert hits and all(r["ket_luan"].startswith(expected) for r in hits)
    report["T3_ho_da_chot"]=True
    provenance=idx(AT/"nguon-goc-giai-nghia.tsv")
    d6=idx(U/"ra-thay-chinh-d6-log-ban-2.tsv")
    assert {w for w,r in provenance.items() if r["trang_thai"]=="PHAT_HANH"}==set(actual)==d6.keys()
    seq={w:r["luot_viet"] for w,r in accepted.items() if w in add}
    def norm_hash(g):
        tok="".join(c if c.isalpha() else " " for c in ud.normalize("NFC",g.lower())).split()
        return sha(json.dumps(tok,ensure_ascii=False,separators=(",",":")).encode())
    assert all(provenance[w]["sha256_giai_nghia"]==sha(g.encode()) and norm_hash(g)==d6[w]["sha256_giai_nghia"] and d6[w]["ket_qua"]=="PASS" for w,g in actual.items())
    assert all(actual[w]==accepted[w]["giai_nghia"] and provenance[w]["lo"]=="rtc-lo-01" and provenance[w]["luot_viet"]==seq[w] and provenance[w]["d6_ket_qua"]=="PASS" and
               accepted[w]["d7_ket_qua"]=="DAT" for w in add)
    assert all(provenance[w]["trang_thai"]=="LOAI" and provenance[w]["dot_loai"]=="ra-thay-chinh" and (provenance[w]["cong_loai"]=="H7_"+code if code in {"K0","K1"} else provenance[w]["cong_loai"].startswith("H5_")) for w,code in wo.items())
    report["T6"]=True;report["D8_luot"]=dict(Counter(seq.values()))
    dp=idx(AT/"du-phong-phan-loai.tsv");dpold=idx(AT/"du-phong-phan-loai.tsv",old=True)
    assert dp.keys()==dpold.keys()-add==set(data(AT/"du-phong.txt").decode().splitlines())
    assert dp["làm cỗ"]["tang"]==dp["rướn"]["tang"]=="D"
    hm=idx(AT/"honorable-mentions.tsv");oh=idx(AT/"honorable-mentions.tsv",old=True)
    changes={w for w in hm if hm[w]!=oh[w]}
    assert hm.keys()==oh.keys() and changes=={r["tu"] for r in locked if r["vai_tro"]=="HM"}
    m=json.loads(data(AT/"manifest.json"))
    facts=m["ra_thay_chinh"]
    gate=all(v==sha(data(AT/k)) for k,v in m["tep"].items())
    met=json.loads(data(U/"ra-thay-chinh-d6-run-ban-2.json"))
    hlog=sha(data(U/"ra-thay-chinh-d6-log-ban-2.tsv")); pub=m["d6"]["kiem_lai_phat_hanh"]
    report["T8"]=(gate and facts["tu_ra"]==len(rem) and facts["tu_vao"]==len(add) and m["danh_sach"]["so_tu"]==len(actual) and
                  m["danh_sach"]["wordlist_txt_sha256"]==sha(data(AT/"wordlist.txt"))==pub["wordlist_txt_sha256"] and
                  report["cot_tu_sha256"]==m["danh_sach"]["cot_tu_sha256"] and m["du_phong"]["tang"]==dict(Counter(r["tang"] for r in dp.values())) and
                  m["du_phong"]["so_tu"]==len(dp)==89 and m["honorable_mentions"]["so_tu"]==len(hm)==237 and
                  m["honorable_mentions"]["sha256"]==sha(data(AT/"honorable-mentions.tsv")) and pub["run_id"]==met["run_id"] and
                  all(r["run_id"]==pub["run_id"] for r in d6.values()) and pub["log_sha256"]==met["log_sha256"]==hlog and
                  all(x["expected_sha256"]==x["actual_sha256"] for x in met["sources"].values()) and len(met["sources"])==5)
    doc=data(ROOT/"WordListAnalyze.md").decode().split("\n## 13. ",1)[1]
    listed=set(re.findall(r"\*([^*]+)\*",next(l for l in doc.splitlines() if l.startswith("**Vào (116")).split(":**",1)[1]))
    report["du_lieu_muc_13"]=listed==add and all(t in doc for t in ("141/143","7.776/7.776","105 từ tầng A và 11 từ tầng C","3 K0, 89 K1, 24 H5","94 khóa chặn mới","35 họ chính tả mới","84, `rtc-v2` 27, `rtc-v3` 5"))
    report["muc_13_H7_chi_noi_K0_tuc"]=bool(re.search("K0 cần nguồn chứng thực toàn mục là tục, không có ngưỡng tần suất",doc))
    report["wordlist_sha256_LF"]=m["danh_sach"]["wordlist_txt_sha256"]
    (E/"t9-goi-astra.json").write_bytes((json.dumps(report,ensure_ascii=False,indent=2)+"\n").replace("\n","\r\n").encode())
    print(report)
    return 0 if all(report[x] for x in ("T2","T3_ho_da_chot","T4","T6","T8","T11","T12")) else 1


if __name__=="__main__":
    raise SystemExit(run())
