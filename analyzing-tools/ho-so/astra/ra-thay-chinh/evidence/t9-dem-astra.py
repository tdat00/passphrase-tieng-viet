"""Đếm bù các mặt chữ chưa có số: hai kho trong RAM, xuất ID/hash, không xuất danh sách nguồn."""
import csv
import gzip
import hashlib
import io
import importlib.util
import re
import sys
import unicodedata as ud
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path

EV=Path(__file__).resolve().parent
def module(name,file):
    s=importlib.util.spec_from_file_location(name,EV/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
t=module("t9_sources","t9-nguon-astra.py")
m=module("t9_meter","km1-mau.py")
canon=lru_cache(140000)(m.canon)
EXTRA="đon đả|đòn đá|buồn thiu|buồn thỉu|ỉu xìu|ỉu xịu|lu bù|lu bu|lù bù|dài ngoằng|dài ngoẵng|hóng chuyện|hồng chuyên|chấp nhất|nặng căn|giái|hoan hảo|hưởng dương|linh đường|tư tế|tu tập|bò đỏ|bố đường|phẹt|phét|nường|lồng|cương|khảo|sân hận|sở trưởng|cầu cơ|thành niên|cả nghĩ".split("|")


def trie_pattern(strings):
    trie={}
    for word in strings:
        n=trie
        for c in word:
            n=n.setdefault(c,{})
        n[""]=True
    def gen(node):
        branches=[re.escape(c)+gen(ch) for c,ch in node.items() if c]
        if not branches:return ""
        s="(?:"+"|".join(branches)+")" if len(branches)>1 else branches[0]
        return "(?:"+s+")?" if "" in node else s
    return gen(trie)


def main(side):
    table=t.rows(EV/"t9-doi-so-cap.tsv")
    keys={r["khoa"] for r in table if r["coi_so"]=="CHUA_DO"}
    wanted={r["mat_chu_sha256"] for r in table if r["coi_so"]=="CHUA_DO"}
    forms=set(EXTRA)
    with ThreadPoolExecutor(4) as ex:
        for _,raw in ex.map(lambda p:t.collect(p,keys),t.PINS):
            forms.update(face.lower() for _,face,_,_,_ in raw if t.digest(face.encode()) in wanted)
    ft={w:tuple(canon(part) if part[0] in m.LETTERS else part for part in m.SPLIT.findall(w)) for w in forms}
    assert all(v for v in ft.values())
    starts=defaultdict(list)
    for w,ts in ft.items():starts[ts[0]].append((w,ts))
    spell=set()
    for w in forms:
        first=m.SPLIT.findall(w)[0]
        spell.update(m.spellings(first))
    # Biên phải làm phép lọc chữ thường đủ nhạy; số chính vẫn do cùng phép tách âm tiết/HND quyết định.
    pat=re.compile("(?<!["+m.LETTERS+"])"+trie_pattern(spell)+"(?!["+m.LETTERS+"])")
    cfg=t.json.loads((t.AT/"manifest.json").read_text(encoding="utf-8"))
    spec=next(r for r in cfg["nguon_du_lieu"] if r["source"].startswith({"sub":"OpenSubtitles VI","web":"CCAligned VI"}[side]))
    d2=m.dict2()
    seen=set();counts=defaultdict(Counter)
    with m.download(spec["url"]) as response:
        stream=m.Tee(response)
        with gzip.GzipFile(fileobj=stream) as gz:
            for ln,raw in enumerate(gz,1):
                text=ud.normalize("NFC",raw.decode("utf-8","ignore").lower())
                if pat.search(text) is None:continue
                digest=hashlib.blake2b(raw.rstrip(b"\r\n"),digest_size=16).digest()
                fresh=digest not in seen
                if not fresh and side=="web":continue
                tokens=[canon(x) if x[0] in m.LETTERS else x for x in m.SPLIT.findall(text)]
                found=False
                for i,k in enumerate(tokens):
                    for w,ts in starts.get(k,()):
                        j=i+len(ts)
                        if tuple(tokens[i:j])!=ts:continue
                        cross=(i>0 and (tokens[i-1],ts[0]) in d2) or (j<len(tokens) and (ts[-1],tokens[j]) in d2)
                        found=True; r=counts[w];r["all"]+=1;r["clean"]+=not cross;r["subuniq"]+=fresh and not cross
                if fresh and found:seen.add(digest)
        assert stream.sha.hexdigest()==spec["sha256"] and ln==spec["input_lines"]
    t.save(f"t9-dem-{side}.tsv",[dict(mat_chu_thuong_sha256=t.digest(w.encode()),be_mat=counts[w]["all"],sach=counts[w]["clean"],sach_dong_khac=counts[w]["subuniq"]) for w in sorted(forms)])
    print(f"{side}: {len(forms)} mặt chữ, {ln} dòng; SHA-256 {spec['sha256']}, không lưu câu.")


if __name__=="__main__":
    main(sys.argv[1])
