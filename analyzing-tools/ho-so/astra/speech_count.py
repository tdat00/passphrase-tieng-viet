import bz2,collections,re
from prepare import *
trie={}
for w in read('dict.json'):
 n=trie
 for b in w.split():n=n.setdefault(b,{})
 n['']=w
pat=re.compile(r'[^\W\d_]+|[^\s\w]+|[\d_]+'); df=collections.Counter();ns=0
for line in bz2.open('tatoeba.bz2','rt',encoding='utf8'):
 f=line.rstrip('\r\n').split('\t');assert f[1]=='vie'
 a=pat.findall(nfc(f[2].lower()));seen=set()
 for i,t in enumerate(a):
  n=trie.get(t);j=i
  while n is not None:
   if '' in n:seen.add(n[''])
   j+=1
   if j>=len(a):break
   n=n.get(a[j])
 df.update(seen);ns+=1
write('df-talk.json',df);print(ns,len(df))
