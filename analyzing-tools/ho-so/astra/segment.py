import bz2,collections,re,tarfile
from prepare import *
D=read('dict.json');trie={}
for w,r in D.items():
 if not any(z[0] in ('noun','verb','adj','adv','num','phrase','pron','intj','prep','conj','det','particle') for z in r['v']):continue
 n=trie
 for k in w.split():n=n.setdefault(k,{})
 n['']=w
pat=re.compile(r'[^\W\d_]+|[^\s\w]+|[\d_]+');
def count(lines):
 c=collections.Counter();ns=0
 for s in lines:
  a=pat.findall(nfc(s.lower()));seen=set();i=0
  while i<len(a):
   n=trie.get(a[i]);best=None;j=i+1
   while n is not None:
    if '' in n:best=(n[''],j)
    if j>=len(a):break
    n=n.get(a[j]);j+=1
   if best is not None:w,i=best;seen.add(w)
   else:i+=1
  c.update(seen);ns+=1
 return ns,c
with tarfile.open('mixed.tar.gz','r|gz') as f:
 for m in f:
  if m.name.endswith('-sentences.txt'):
   ns,c=count(b.decode('utf8').rstrip('\r\n').partition('\t')[2] for b in f.extractfile(m)); print(ns,len(c),flush=True);write('seg.json',c)
with bz2.open('tatoeba.bz2','rt',encoding='utf8') as f:
 ns,c=count(l.rstrip('\r\n').split('\t')[2] for l in f);print(ns,len(c),flush=True);write('seg-talk.json',c)
