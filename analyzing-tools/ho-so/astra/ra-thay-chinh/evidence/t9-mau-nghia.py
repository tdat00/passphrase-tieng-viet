"""Mẫu đúng ngữ cảnh: ≤30 vị trí sạch/dòng khác nhau/nghĩa; trường ghi chỉ là ID, băm, cờ tìm ngữ cảnh."""
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
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

E=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('km1_meter',E/'km1-mau.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
CANON=lru_cache(120000)(m.canon)
GROUPS={
    "lồng":r"vãi\s+(cả\s+)?lồng|cái\s+con\s+lồng|cái\s+lồng\s+gì|có\s+cái\s+lồng|địt|âm hộ|âm đạo|sinh dục|lồn|dương vật",
    "cương":r"dương vật|cậu nhỏ|rối loạn cương|cương dương|cương cứng|cương lên|sinh lý|sinh dục|cường dương",
    "rùng mình":r"xuất tinh|cực khoái|lên đỉnh|khoái cảm|tình dục|quan hệ sinh lý",
    "tâm hồn":r"vòng một|vòng 1|vòng ngực|ngực khủng|ngực to|khoe ngực|bộ ngực",
    "vắt sữa":r"xuất tinh|thủ dâm|lên đỉnh|dương vật|kích dục",
    "tiếp khách":r"làng chơi|mại dâm|bán dâm|bán thân|nhà thổ|lầu xanh|kỹ viện|điếm|bán hoa",
    "đòn đá":r"võ|đấu|đòn|đánh",
    "cầu cơ":r"gọi hồn|linh hồn|ma quỷ|người chết|bàn cầu cơ",
}


def main(side):
    terms={tuple(map(CANON,w.split())):w for w in GROUPS}
    starts={seq[0] for seq in terms}
    pre=re.compile(r"(?<!\w)(?:"+"|".join(re.escape(s) for w in GROUPS for s in m.spellings(w.split()[0]))+r")(?!\w)")
    lex=m.dict2()
    cfg=json.loads((m.AT/"manifest.json").read_text(encoding="utf-8"))
    src=next(r for r in cfg['nguon_du_lieu'] if r['source'].startswith({"sub":"OpenSubtitles VI","web":"CCAligned VI"}[side]))
    samples=defaultdict(list); seen=set()
    with m.download(src['url']) as response:
        tee=m.Tee(response)
        with gzip.GzipFile(fileobj=tee) as z:
            for n,raw in enumerate(z,1):
                text=ud.normalize('NFC',raw.decode('utf-8','ignore').lower())
                if not pre.search(text):continue
                digest=hashlib.blake2b(raw.rstrip(b"\r\n"),digest_size=16).hexdigest()
                if digest in seen:continue
                tokens=m.SPLIT.findall(text); c=[CANON(x) if x[0] in m.LETTERS else '#' for x in tokens]
                found=False
                for i,tok in enumerate(c):
                    if tok not in starts:continue
                    for size in (1,2):
                        seq=tuple(c[i:i+size])
                        if len(seq)!=size or seq not in terms:continue
                        w=terms[seq]; j=i+size
                        if (i and (c[i-1],seq[0]) in lex) or (j<len(c) and (seq[-1],c[j]) in lex):continue
                        found=True;win=' '.join(tokens[max(0,i-8):j+8])
                        route=bool(re.search(r"(?<!\w)(?:"+GROUPS[w]+r")(?!\w)",win))
                        for label in ('NGAU_NHIEN','GOI_Y_NGU_CANH') if route else ('NGAU_NHIEN',):
                            h=-int.from_bytes(hashlib.sha256(f"rtc-T9-20261122|{side}|{w}|{n}|{i}".encode()).digest(),'big')
                            entry=(h,n,i,digest,win); heap=samples[w,label]
                            if len(heap)<30:heapq.heappush(heap,entry)
                            elif h>heap[0][0]:heapq.heapreplace(heap,entry)
                if found:seen.add(digest)
        assert tee.sha.hexdigest()==src['sha256'] and n==src['input_lines']
    b=io.StringIO(); wr=csv.writer(b,delimiter='\t',lineterminator='\r\n');wr.writerow(('doi_chung','loai_mau','id_dong','i_token','blake2b128_dong'))
    for (w,lbl),vs in sorted(samples.items()):
        val=sorted(vs,reverse=True)
        wr.writerows((w,lbl,n,i,d) for _,n,i,d,_ in val)
        if lbl=='GOI_Y_NGU_CANH' and '--inspect' in sys.argv and w not in ('cầu cơ','đòn đá'):
            print(w+': '+' | '.join(f'{n}/{i} {clip[:110]}' for _,n,i,d,clip in val[:8]))
        elif w in ('đòn đá','cầu cơ') and lbl=='NGAU_NHIEN' and '--inspect' in sys.argv:
            print(w+': '+' | '.join(f'{n}/{i} {clip[:90]}' for _,n,i,d,clip in val[:4]))
    (E/f't9-mau-nghia-{side}.tsv').write_bytes(b.getvalue().encode())
    print(side,[(k,len(v)) for k,v in samples.items()])


if __name__=="__main__":main(sys.argv[1])
