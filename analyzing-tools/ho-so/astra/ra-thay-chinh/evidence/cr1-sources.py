"""Đọc nguồn ghim/API trong RAM, chỉ lưu metadata, không lưu văn bản nguồn."""
import json
import re
import unicodedata as ud
import urllib.parse
import urllib.request
from collections import defaultdict

from dictionary_probe import vietnamese
from screen_core import AT, EV, OUT, U, key, load, read, save_json, save_tsv, sha, tsv

O = AT/"ho-so"/"opus"/"ra-thay-chinh"


def main():
    d=load()
    mf=json.loads(read(AT/"manifest.json"))
    hnd=defaultdict(set)
    membership=defaultdict(set)
    source_meta=[]
    wanted={r["tu"] for r in tsv(O/"sang-loc-h5.tsv") if r["loai_H5"]!="-"}
    wanted|={r["bien_the"] for r in tsv(O/"sang-loc-h5.tsv") if r["loai_H5"]!="-"}
    wanted|={"phí phạn","phí phạm","dây chun","dây thun","chun","thun"}
    for spec in mf["nguon_du_lieu"][:4]:
        name=spec["source"]
        url=f"https://raw.githubusercontent.com/duyet/vietnamese-wordlist/688b0953c8cdb21ee090ce80b83cefdb052fe2cd/{name}.txt"
        with urllib.request.urlopen(url,timeout=60) as response:
            b=response.read()
        assert sha(b)==spec["sha256"]
        source_meta.append({"source":name,"url":url,"sha256":sha(b),"source_saved":False})
        for line in b.decode("utf-8").splitlines():
            face=ud.normalize("NFC",line.strip()).lower()
            if face:
                hnd[key(face)].add(face)
                if face in wanted:
                    membership[face].add(name)
    oc=d["opus-counts"]
    docs=defaultdict(set)
    for r in oc:
        if r["vai_tro"]=="DOC_KHAC":
            docs[r["khoa"]].add(r["tu"])
    hnd_all={(key(w),w,v) for w in d["main"] for v in hnd.get(key(w),()) if v!=w}
    missing={(k,w,v) for k,w,v in hnd_all if v not in docs[k]}
    saved=tsv(O/"evidence"/"h7-hnd-cung-khoa.tsv")
    assert missing=={(r["khoa"],r["tu_chinh"],r["doc_khac_hnd"]) for r in saved}
    save_tsv(EV/"cr1-HND-membership.tsv",[{"tu":w,"HND":",".join(sorted(membership[w])) or "KHONG",
                                          "xac_minh":"verified: có mặt; không tự chứng minh chuẩn/lỗi hay cùng từ"}
                                         for w in sorted(wanted)])
    targets={
        "vi":["già dặn","già giặn","qua quýt","qua quít","phí phạm","phí phạn","chưng bày","chun","thun",
              "bĩnh","tinh khí","tinh dịch","phân bắc","chứng cứ","sán dây","sán xơ mít","nội trú","ngoại trú"],
        "en":["thun","chun","già dặn","già giặn","qua quýt","qua quít","làm cỏ","bỏ mẹ","đi đồng",
              "lăng nhăng","thị trưởng","liếm","chứng cứ","sán dây"],
    }
    results=[]
    for lang, words in targets.items():
        query=urllib.parse.urlencode({"action":"query","format":"json","formatversion":2,
                                     "prop":"revisions","rvprop":"ids|content","rvslots":"main",
                                     "titles":"|".join(words)})
        req=urllib.request.Request(f"https://{lang}.wiktionary.org/w/api.php?{query}",
                                   headers={"User-Agent":"VietnamesePassphraseReview/1.0"})
        with urllib.request.urlopen(req,timeout=60) as response:
            data=json.load(response)
        assert "error" not in data
        for page in data["query"]["pages"]:
            revision=page.get("revisions",[{}])[0]
            body=revision.get("slots",{}).get("main",{}).get("content","")
            vi=vietnamese(body,lang)
            rev=revision.get("revid","-")
            results.append({
                "tu":page["title"],"lang":lang,"revision":rev,
                "co_phan_tieng_Viet":str(bool(vi)),"co_trang":str(bool(body)),
                "sha256_wikitext":sha(body.encode()) if body else "-",
                "url":f"https://{lang}.wiktionary.org/w/index.php?title={urllib.parse.quote(page['title'])}&oldid={rev}",
                "ngay":"2026-11-21",
            })
            print(f"\n[{lang}:{page['title']}] revision={rev}")
            if not vi:
                print("NO VIETNAMESE SECTION")
                continue
            keep=[]
            lines=vi.splitlines()
            alt_mode=False
            for line in lines:
                if "===Alternative forms===" in line:
                    alt_mode=True
                    keep.append(line)
                elif re.match("^===",line):
                    alt_mode=False
                elif alt_mode or line.startswith("# ") or line.startswith("#{{") or line.startswith("From "):
                    keep.append(line)
            print("\n".join(keep[:12])[:1800])
    save_tsv(EV/"cr1-dictionary-metadata.tsv",results)
    save_json(EV/"cr1-source-metrics.json",{
        "HND_sources":source_meta,"HND_main_pairs":len(hnd_all),"HND_missing_DOC_pairs":len(missing),
        "matches_Opus_HND_table":True,"Wiktionary_queries":len(results),"raw_source_saved":False,
    })


if __name__=="__main__":
    main()
