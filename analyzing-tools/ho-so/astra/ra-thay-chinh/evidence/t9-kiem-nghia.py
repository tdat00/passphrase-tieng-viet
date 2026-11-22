"""Đọc riêng bằng chứng của nghĩa mới; chỉ công bố tình trạng, URL, dòng nguồn, băm mục từ."""
import csv
import gzip
import hashlib
import io
import json
import urllib.request
import zipfile
from pathlib import Path

E=Path(__file__).resolve().parent
ROOT=E.parents[4]; AT=ROOT/"analyzing-tools"
WORDS="phẹt|phét|phệt|lồng|cương|buồn thiu|buồn thỉu|ỉu xìu|ỉu xịu|lu bù|lu bu|lù bù|dài ngoằng|dài ngoẵng|bịch|chào cờ|rùng mình|tâm hồn|vắt sữa|tiếp khách|biết|ngoài|vệ sinh|thượng|nghề|mụ nội|ngả nghiêng|cầu cơ|tu tập|tư tế|chung chi|đòn đá|cộng đoàn|tán tỉnh|chảnh|đá|bố đường".split("|")
PIN=json.loads((E/"hm1-nguon-ghim.json").read_text(encoding="utf-8"))["ghim"][-2:]
URL="https://web.archive.org/web/20241112031805id_/https://www.informatik.uni-leipzig.de/~duc/Dict/VietViet.zip"
ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"VietnameseWordlistReview/1.0"}),timeout=60) as r:return r.read()
def decode(s):
    n=0
    for c in s:n=n*64+ABC.index(c)
    return n
def main():
    import sys
    show=set(sys.argv[1:]); chosen=set(WORDS); out=[]
    for spec in PIN:
        raw=get(spec["url"]);payload=gzip.decompress(raw);h=hashlib.sha256(raw if spec["hash_of"]=="gzip" else payload).hexdigest();assert h==spec["sha256"]
        lang="vi" if spec["hash_of"]=="gzip" else "en"
        for i,line in enumerate(io.BytesIO(payload),1):
            x=json.loads(line);w=x.get("word","")
            if x.get("lang_code")!="vi" or w not in chosen:continue
            tags=set();alt=set(); note=[]
            for s in x.get("senses",[]):
                sub=s.get("tags",[])+s.get("raw_tags",[])
                tags.update(sub); alt.update(z.get("word","") for z in s.get("alt_of",[]))
                note.extend(f"[{','.join(sub)}] {g}" for g in s.get("glosses",[]))
            out.append((w,lang,i,x.get("pos"),";".join(sorted(tags)) or "-",";".join(sorted(alt & chosen)) or "-",hashlib.sha256(line).hexdigest()))
            if w in show: print(f"{w} {lang}:{i} {x.get('pos','?')} "+" / ".join(note)[:330])
    raw=get(URL);assert hashlib.sha256(raw).hexdigest()=="1882c078187dfb8db646cd5c21d0b80fb06b03fc44f27c8cade4377fea80567c"
    z=zipfile.ZipFile(io.BytesIO(raw));data=gzip.decompress(z.read("data/VV/vv30K.dict.dz"))
    for i,line in enumerate(z.read("data/VV/vv30K.index").decode("utf-8-sig").splitlines(),1):
        fields=line.split("\t")
        if len(fields)<3 or fields[0] not in chosen:continue
        w=fields[0]; a,n=map(decode,fields[1:3]);sub=data[a:a+n];out.append((w,"VV30K",i,"-","-","-",hashlib.sha256(sub).hexdigest()))
        if w in show:print(f"{w} VV30K:{i} "+" ".join(sub.decode("utf8").split())[:265])
    b=io.StringIO();ww=csv.writer(b,delimiter="\t",lineterminator="\r\n");ww.writerow(("muc_kiem","nguon","dong","tu_loai","nhan_nguon","dan_den_muc_trong_ca","sha256_muc"));ww.writerows(out);(E/"t9-nguon-cac-ca.tsv").write_bytes(b.getvalue().encode())
if __name__=="__main__":main()
