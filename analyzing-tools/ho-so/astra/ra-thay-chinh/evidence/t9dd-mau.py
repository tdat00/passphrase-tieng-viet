"""Đọc mẫu sạch của ba từ đang đối đáp. Không lưu câu; --inspect chỉ hiện cửa sổ trong phiên."""
import csv
import gzip
import hashlib
import heapq
import importlib.util
import io
import json
import re
import sys
import unicodedata as ud
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

E=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location("km1_t9dd",E/"km1-mau.py")
m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
canon=lru_cache(120000)(m.canon)
WORDS=("tu tập","tư tế","đượi")


def main(side):
    pre=re.compile(r"(?<!\w)(?:tu\s+tập|tư\s+tế|đượi)(?!\w)")
    ft={tuple(map(canon,w.split())):w for w in WORDS}
    lex=m.dict2()
    mf=json.loads((m.AT/"manifest.json").read_text(encoding="utf-8"))
    src=next(x for x in mf["nguon_du_lieu"] if x["source"].startswith({"sub":"OpenSubtitles VI","web":"CCAligned VI"}[side]))
    with m.download(src["url"]) as response:raw=response.read()
    assert hashlib.sha256(raw).hexdigest()==src["sha256"]
    heap=defaultdict(list);count=Counter();seen=set()
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as z:
        for n,b in enumerate(z,1):
            line=ud.normalize('NFC',b.decode('utf-8','ignore').lower())
            if not pre.search(line):continue
            sig=hashlib.blake2b(b.rstrip(b'\r\n'),digest_size=16).hexdigest()
            fresh=sig not in seen;seen.add(sig)
            if not fresh and side=="web":continue
            words=m.SPLIT.findall(line); tokens=[canon(t) if t[0] in m.LETTERS else '#' for t in words]
            for i,t in enumerate(tokens):
                for size in (1,2):
                    j=i+size; ts=tuple(tokens[i:j]);w=ft.get(ts)
                    if not w or len(ts)!=size:continue
                    if (i and (tokens[i-1],ts[0]) in lex) or (j<len(tokens) and (ts[-1],tokens[j]) in lex):continue
                    count[w]+=1
                    if not fresh:continue
                    h=-int.from_bytes(hashlib.sha256(f"rtc-T9DD-20261122|{side}|{w}|{n}|{i}".encode()).digest(),"big")
                    item=(h,n,i,sig," ".join(words[max(0,i-5):j+5]));pool=heap[w]
                    if len(pool)<12:heapq.heappush(pool,item)
                    elif h>pool[0][0]:heapq.heapreplace(pool,item)
    lines=io.StringIO(); wr=csv.writer(lines,delimiter="\t",lineterminator="\r\n");wr.writerow(("muc","id_dong","i_token","blake2b128_dong","tong_sach"))
    for w in WORDS:
        rows=sorted(heap[w],reverse=True)
        wr.writerows((w,n,i,sig,count[w]) for _,n,i,sig,_ in rows)
        if '--inspect' in sys.argv:
            print(w,count[w],":"," | ".join(f"{n}: {clip}" for _,n,i,sig,clip in rows))
    (E/f"t9dd-mau-{side}.tsv").write_bytes(lines.getvalue().encode())
    print(f"{side}: {dict(count)}; ghim {src['sha256']}")


if __name__=="__main__":main(sys.argv[1])
