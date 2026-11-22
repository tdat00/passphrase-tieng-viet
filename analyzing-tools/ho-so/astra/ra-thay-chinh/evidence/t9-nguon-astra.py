"""Đọc nguồn đã ghim trong RAM; chỉ lưu hash mặt chữ, dòng nguồn, số và mã kiểm vào hồ sơ."""
import argparse
import csv
import gzip
import hashlib
import io
import json
import re
import sys
import unicodedata as ud
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path

EV = Path(__file__).resolve().parent
A, AT = EV.parent, EV.parents[3]
U = AT / "ho-so" / "unified"
S, W = 34314528, 149860716
PINS = json.loads((EV / "hm1-nguon-ghim.json").read_text(encoding="utf-8"))["ghim"]
RULES = {
    "K0": r"vulgar|obscen(?:e|ity)|profan(?:e|ity)|swearword|fuck(?:ing)?|intercourse|sexual|genital|porn(?:ography|ographic)?|prostitut(?:e|ion)|semen|sperm|ejaculat\w*|masturbat\w*|penis|vagina|vulva|clitoris|testicl\w*|scrotum|erection|orgasm|anus|excrement|feces|faeces|defecat\w*|urine|piss|shit|tình dục|giao hợp|giao cấu|sinh dục|dương vật|âm đạo|âm hộ|tinh dịch|thủ dâm|đi cầu|đi ỉa|ỉa|đái|nước tiểu|chất thải|cứt|phân người|phân súc vật|phân động vật|tục tĩu|thô tục|nói tục|mại dâm|bán dâm",
    "HURT": r"suicid\w*|self-harm|kill(?:ing|ed|s)?|murder\w*|assassin\w*|shoot(?:ing)?|gun(?:s|fire|shot)?|firearm\w*|rifle|pistol|ammunition|bomb(?:ing|s)?|weapon\w*|stab(?:bing)?|tortur\w*|beat up|massacre|slay|slaughter\w*|rape|rapist|violent|violence|tự sát|tự tử|tự vẫn|tự hại|tự thiêu|tự trầm|giết|sát hại|đánh đập|chém|đâm chết|bắn|súng|vũ khí|bạo lực|tra tấn|tàn sát|hãm hiếp|cưỡng hiếp|hành hung|hành hình|tử hình",
    "WARN": r"offensive|derogatory|insult\w*|pejorative|slur|prison\w*|punishment|arrest\w*|crim(?:e|inal)|lawsuit|judicial|government|politic\w*|military|soldier|battle|funeral|religio\w*|superstiti\w*|deity|worship|Buddhis\w*|coffin|death|dead|disease|symptom|illness|patholog\w*|surgery|wound|injury|gambl\w*|alcohol|liquor|tobacco|narcotic|disaster|earthquake|disgust\w*|contempt\w*|miệt thị|khinh bỉ|chửi|quân sự|quân đội|chiến tranh|tố tụng|tội phạm|phạt tù|chính trị|nhà nước|thần linh|tang lễ|mê tín|thờ cúng|người chết|bệnh|thương tích|cờ bạc|ma túy|rượu|ghê tởm",
}
RULES["K0"] += r"|cặc|buồi|lồn|địt|đụ|rắm|dái|hậu môn|phóng tinh|nhũ hoa|âm vật|làm tình|ăn nằm|chịch|giao hoan|dâm dục|thô bỉ|tinh hoàn|bộ phận kín|chỗ kín|nước đái|đại tiện|tiểu tiện|đồ cứt|đánh hơi|phân của|làm gái|đi khách|whore|slut|pussy|dick|prick|buttocks|arsehole|asshole|organs? of reproduction|private parts|to fart|flatulen\w*|turd|faecal|fecal|(?-i:\bdung\b)(?! (?:và|của|trong|tập|chính|ngắn|về|được))|animal droppings|copulat\w*|lewd|obscenity|pimp|brothel|fornicat\w*|nói tránh|chuyện chăn gối|điếm|ỉa chảy|dâm đãng|dâm ô|nhục dục|xác thịt|quan hệ sinh lý|xuất tinh|sinh thực khí|tinh trùng|giao phối|phối giống|tinh hoàn|nipple|fellatio|blowjob|indecent|euphemis\w*|erectile|titoris|ejacul\w*"
RULES["HURT"] += r"|đòn tấn công|võ thuật|đấu võ|đá vào|đứt cổ|dao găm|gươm|giặc|đòn đánh|đao|nỏ|cây lao|đạn|đấm|đánh chết|đánh vào|đánh nhau|đâm vào|treo cổ|tự kết liễu|thắt cổ|đâm chém|thiêu sống|chém đầu|pháo|cắt cổ|tự gây thương tích|self-injur\w*|combat|sword|ammunition|shooting|artillery|martial arts|handgun|bullet|explosive|punch|kick|hang oneself"
RXS = {k:re.compile(r"(?<!\w)(?:"+p+r")(?!\w)", re.I) for k,p in RULES.items()}


def digest(b):
    return hashlib.sha256(b).hexdigest()


def nfc(s):
    return ud.normalize("NFC", s)


@lru_cache(maxsize=250000)
def shape(s):
    return "".join(c for c in ud.normalize("NFD", s.lower()) if not ud.combining(c) and not c.isspace() and c not in "-‐‑").replace("đ","d")


def rows(p):
    with p.open(encoding="utf-8-sig",newline="") as f:
        return [dict(r,n=i) for i,r in enumerate(csv.DictReader(f,delimiter="\t"),2)]


def save(name, table):
    b=io.StringIO()
    w=csv.DictWriter(b,fieldnames=table[0],delimiter="\t",lineterminator="\r\n")
    w.writeheader();w.writerows(table)
    (EV/name).write_bytes(b.getvalue().encode("utf-8"))


def collect(spec, keys):
    with urllib.request.urlopen(urllib.request.Request(spec["url"],headers={"User-Agent":"VietnameseWordlistReview/1.0"}),timeout=100) as response:
        data=response.read()
    kind=spec["source"]
    if kind.startswith("Viet"):
        assert digest(data)==spec["sha256"]
        return kind,[(n,nfc(x.strip()),"",(),()) for n,x in enumerate(data.decode("utf-8-sig").splitlines(),1) if shape(nfc(x.strip())) in keys]
    lang="vi" if "viwiktionary" in kind else "en"
    payload=gzip.decompress(data)
    assert digest(data if spec["hash_of"]=="gzip" else payload)==spec["sha256"]
    result=[]
    for i,line in enumerate(io.BytesIO(payload),1):
        x=json.loads(line)
        if x.get("lang_code")!="vi" or not x.get("word"):
            continue
        face=nfc(x["word"].strip())
        if shape(face) not in keys:
            continue
        parttags,gloss=[],[]
        for sense in x.get("senses",[]):
            parttags.extend(sense.get("tags",[])+sense.get("raw_tags",[])+sense.get("topics",[]))
            gloss.extend(sense.get("glosses",[]))
        result.append((i,face,x.get("pos","?"),tuple(sorted(set(parttags))),tuple(gloss)))
    return lang,result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--inspect",default="",help="all_missing, entrants, severe, unjudged or comma-separated case IDs")
    ap.add_argument("--skip",type=int,default=0);ap.add_argument("--limit",type=int,default=150)
    ap.add_argument("--compact",action="store_true",help="Chỉ hiện STT và mặt chữ theo lô 12, không in nghĩa.")
    ap.add_argument("--self",action="store_true",help="Đọc riêng cả nghĩa K0 tiềm tàng của chính mặt chữ phát hành.")
    ap.add_argument("--deep",action="store_true",help="Đọc từng mục từ đã chọn theo dòng nguồn, không lưu nghĩa.")
    ap.add_argument("--fresh",action="store_true",help="Ghi ảnh chụp phiếu hash, không ghi danh sách từ điển")
    args=ap.parse_args()
    mainwords={}
    wl=AT/"wordlist.txt"
    for i,line in enumerate(wl.read_text(encoding="utf-8-sig").splitlines(),1):
        w=line.partition("|")[0]
        assert shape(w) not in mainwords
        mainwords[shape(w)]=(w,i)
    assert len(mainwords)==7776
    change={r["tu"] for r in rows(U/"ra-thay-chinh-giai-nghia-dat.tsv") if r["ket_luan"]=="VAO_CHINH"}
    assert len(change)==116 and "cả nghĩ" in change and "sớm tối" not in change
    freq,allfaces={},defaultdict(lambda:defaultdict(set))
    for r in rows(U/"opus-counts.tsv"):
        if r["tu"] not in freq or r["vai_tro"]=="UNG_VIEN":
            freq[r["tu"]]=(int(r["sub_sach"]),int(r["web_sach"]))
        if r["vai_tro"]=="DOC_KHAC" and r["khoa"] in mainwords:
            assert shape(r["tu"])==r["khoa"]
            allfaces[(r["khoa"],r["tu"])]["DOC"].add(r["n"])
    for st in ("l2","l2b","l2c","l2d","l3"):
        for r in rows(U/f"{st}-ung-vien.tsv"):
            freq.setdefault(r["tu"],(int(r["sub_sach"]),int(r["web_sach"])))
    for prefix in ("km1-h7","hm1-h7"):
        c=[{r["tu"]:int(r["clean"]) for r in rows(EV/f"{prefix}-dem-{side}.tsv")} for side in ("sub","web")]
        for w in c[0].keys() & c[1].keys():
            freq.setdefault(w,(c[0][w],c[1][w]))
    old, cards, decisions = {}, {}, {}
    for f in ("h7-sang-loc-1177.tsv","h7-sang-loc-bo-sung.tsv"):
        for r in rows(A/f):
            old[r["khoa"],r["doc_khac"].lower()] = (r["muc_K_de_xuat"],f"{f}:{r['n']}")
    for f in ("khep-muc-mo-1.tsv","khep-muc-mo-2.tsv"):
        for r in rows(A/f):
            if r["loai"]!="H5_CHO":
                cards[r["tu_hoac_khoa"]]=(r["de_xuat_astra"],f"{f}:{r['n']}")
    for r in rows(EV/"km1-doi-chung.tsv"):
        w,alt=r["tu"],r["doi_chung"].lower()
        if w in cards and shape(w)==shape(alt):
            decisions[(shape(w),alt)]=cards[w]
    for r in rows(EV/"rd2-de-xuat-dong-co.tsv"):
        w, alt = r.get("tu",""), r.get("doi_chung","")
        if w and alt and shape(w)==shape(alt):
            decisions[(shape(w),alt.lower())]=("KHONG_DO",f"rd2-de-xuat-dong-co.tsv:{r['n']}")
    alerts={(r["khoa"],r["doc_khac"].lower()):(r["co"],r["trang_thai_9_1"],r["n"]) for r in rows(U/"canh-bao-khong-dau.tsv") if r["khoa"] in mainwords and mainwords[r["khoa"]][0]==r["ung_vien"]}
    sig=defaultdict(set)
    for r in rows(U/"chu-ky.tsv"):
        if r["loai_ky"]=="K2" and r["hieu_luc"]=="CO" and r["khoa"] in mainwords and mainwords[r["khoa"]][0]==r["tu"]:
            sig[r["khoa"]].add(r["nguoi_ky"])
    lex=defaultdict(list)
    with ThreadPoolExecutor(4) as ex:
        for spec, result in zip(PINS,ex.map(lambda p:collect(p,mainwords),PINS),strict=True):
            name,obs=result
            for n,face,pos,tags,glosses in obs:
                k=shape(face)
                allfaces[k,face][name].add(n)
                if pos:
                    lex[k,face].append((name,n,pos,tags,glosses))
    table,seen,details=[],set(),[]
    exact={}
    changed_keys={r["khoa"] for r in rows(U/"ra-thay-chinh-h7.tsv") if r["khoa"] in mainwords}
    for (k,alt),sources in sorted(allfaces.items(),key=lambda z:(z[0][0],z[0][1])):
        w,lno=mainwords[k]
        if w==alt:
            found=[]
            for name,n,pos,tags,gs in lex[k,alt]:
                for g in gs:
                    if RXS["K0"].search("; ".join((*tags,g))):
                        found.append((name,n,pos,tags,g))
            exact[k]=(sources,found)
            continue
        case=digest((k+"\t"+alt).encode())[:16]; assert case not in seen;seen.add(case)
        found=freq.get(alt.lower());base=freq.get(w)
        assert base,w
        p=lambda pair:500000*(pair[0]/S+pair[1]/W)
        flag="CHUA_DO" if found is None else " / ".join(a for a,cond in (("≥0,3",p(found)>=0.3),("≥mục",p(found)>=p(base))) if cond) or "THAP"
        o,oref=old.get((k,alt.lower()),("-","-"))
        signed,sref=decisions.get((k,alt.lower()),("-","-"))
        hist,kind,aline=alerts.get((k,alt.lower()),("-","-",0))
        texts=lex[k,alt]
        triggers=set()
        for _,_,_,tags,glosses in texts:
            msg="; ".join((*tags,*glosses))
            for typ,rx in RXS.items():
                if rx.search(msg):
                    triggers.add(typ)
        proper = (alt!=alt.lower()) and not any(pos not in ("name","character","symbol") and any(g for g in gs) for _,_,pos,_,gs in texts)
        table.append(dict(stt=len(table)+1,id=case,khoa=k,dong_wordlist=lno,mat_chu_sha256=digest(alt.encode()),mat_thuong_sha256=digest(alt.lower().encode()),nguon=";".join(f"{n}:{','.join(map(str,sorted(idx)))}" for n,idx in sorted(sources.items())),tu_vao=int(w in change),khoa_da_xu=int(k in changed_keys),cung_mat_khac_hoa=int(w==alt.lower()),khac_hoa=int(alt!=alt.lower()),chi_ten_trong_nguon=int(proper),sub=found[0] if found else "-",web=found[1] if found else "-",coi_so=flag,nhan_doc="/".join(sorted(triggers)) or "-",muc_A_cu=o,phieu_cu=oref,muc_A_sau=signed,phieu_sau=sref,co_P2=hist,phan_xu_P2=kind,dong_P2=aline or "-",hai_K2_cua_khoa=int(sig[k]=={"Astra","Opus"})))
        details.append((w,alt,texts))
    if args.fresh:
        save("t9-doi-so-cap.tsv",table)
        amount=Counter(r["khoa"] for r in table)
        save("t9-phu-khoa.tsv",[dict(khoa=k,dong_wordlist=lno,vao=int(w in change),so_cach_doc_khac=amount[k],nguon_khop_chinh=";".join(sorted(exact.get(k,({},[]))[0])) or "-",so_co_goi_doc_K0_mat_chinh=len(exact.get(k,({},[]))[1])) for k,(w,lno) in mainwords.items()])
        (EV/"t9-nguon.json").write_bytes((json.dumps({"wordlist_sha256_LF":digest(wl.read_bytes().replace(b"\r\n",b"\n")),"khoa":len(mainwords),"khoa_co_cap":len({r["khoa"] for r in table}),"cap":len(table),"doc":sum("DOC:" in r["nguon"] for r in table),"nguon":PINS},ensure_ascii=False,indent=2)+"\n").replace("\n","\r\n").encode())
    def need(row):
        if args.inspect=="all_missing":
            return row["muc_A_sau"]=="-" and row["muc_A_cu"]=="-"
        if args.inspect=="entrants": return row["tu_vao"]
        if args.inspect=="severe": return bool({"K0","HURT"}&set(row["nhan_doc"].split("/")))
        if args.inspect=="warnings": return row["nhan_doc"]!="-" or row["co_P2"] not in ("-","THONG_TIN")
        if args.inspect=="prior_unsettled": return row["muc_A_cu"] not in ("-", "KHONG_DO","CUNG_MAT_CHU_KHAC_KHOANG") and row["muc_A_sau"]=="-"
        if args.inspect=="capital": return row["khac_hoa"] and not row["cung_mat_khac_hoa"]
        if args.inspect=="all": return True
        if args.inspect=="unjudged": return row["muc_A_sau"]=="-" and row["muc_A_cu"]=="-" and row["chi_ten_trong_nguon"]==0 and not row["cung_mat_khac_hoa"]
        return row["id"] in set(args.inspect.split(",")) or str(row["stt"]) in set(args.inspect.split(","))
    selected=[(r,d) for r,d in zip(table,details) if need(r)]
    if args.self:
        want=[(mainwords[k],gs) for k,(src,gs) in exact.items() if gs]
        print("Số chính mặt có tín hiệu để đọc:",len(want))
        for (w,ln),gs in want[args.skip:args.skip+args.limit]:
            print(f"{ln} {w}: "+" | ".join(f"{lang}:{n} {g}" for lang,n,p,ts,g in gs)[:180])
    elif args.compact:
        found=selected[args.skip:args.skip+args.limit]
        for i in range(0,len(found),10):
            print(" | ".join(f"{r['stt']} {d[0]}/{d[1]}" for r,d in found[i:i+10]))
    elif args.deep:
        for r,(w,alt,gloss) in selected[args.skip:args.skip+args.limit]:
            print(f"{r['stt']} {w} → {alt}")
            for lang,n,pos,tags,gs in gloss:
                print(f"  {lang}:{n} {pos} [{','.join(tags)}] "+" / ".join(gs)[:280])
    elif args.inspect:
        for r,(w,alt,texts) in selected[args.skip:args.skip+args.limit]:
            vals=[g for lang,n,pos,tags,gs in texts for g in gs if any(rx.search("; ".join((*tags,g))) for rx in RXS.values())]
            picks=vals if args.inspect=="severe" else [g for lang,n,pos,tags,gs in texts for g in gs][:2]
            print(f"{r['stt']} {w} → {alt} [{r['nhan_doc']};{r['muc_A_cu']}/{r['muc_A_sau']};{r['sub']}/{r['web']}] "+" | ".join(picks)[:180])
    print(f"7.776 khóa; {len(table)} cặp; lọc {len(selected)}; nguồn ghim khớp, không lưu văn bản thô.")


if __name__=="__main__":
    main()
