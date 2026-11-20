from pathlib import Path
import collections, gzip, json, re, tarfile, unicodedata as U
P=Path('.'); nfc=lambda s:U.normalize('NFC',s); alphabet='aăâbcdđeêghiklmnoôơpqrstuưvxy'; tone='\u0300\u0309\u0303\u0301\u0323'
no_tone=lambda s:nfc(''.join(c for c in U.normalize('NFD',s) if c not in tone)); flat=lambda s:''.join(c for c in U.normalize('NFD',s.lower().replace('đ','d')) if not U.category(c).startswith('M') and c!=' ')
def order(s):
 return tuple((tuple(alphabet.index(c) for c in no_tone(t)),next((tone.index(c)+1 for c in U.normalize('NFD',t) if c in tone),0)) for t in s.split())
def ok(s):return bool(s) and 1<=len(s.split(' '))<=4 and all(t and all(c in alphabet for c in no_tone(t)) for t in s.split(' ')) and s==s.lower()
def write(n,v):Path(n).write_text(json.dumps(v,ensure_ascii=False,separators=(',',':')),encoding='utf8')
def read(n):return json.loads(Path(n).read_text(encoding='utf8'))
if __name__=='__main__':
 entries={}; allpos=collections.Counter(); counts=collections.Counter(); altsem={'v':{},'e':{}}
 for edition,stream in [('v',gzip.open('vi.jsonl.gz','rt',encoding='utf8')),('e',open('en.jsonl',encoding='utf8'))]:
  rawterms=set()
  with stream:
   for line in stream:
    x=json.loads(line)
    if x.get('lang_code')!='vi':continue
    w=nfc(x['word']);rawterms.add(w); counts[edition+' entries']+=1
    if not ok(w):continue
    if edition=='e' and w not in entries: continue
    rec=entries.setdefault(w,{'v':[],'e':[]})
    p=x['pos']; allpos[(edition,p)]+=1
    for s in x.get('senses',[]):
     g='; '.join(s.get('glosses',[])); tags=sorted(set(s.get('tags',[])+s.get('raw_tags',[]))); topics=s.get('topics',[]); alts=[r.get('word','') for r in s.get('alt_of',[])];
     if alts:altsem[edition].setdefault(w,[]).extend(alts)
     rec[edition].append([p,g[:1100],tags,topics])
  counts[edition+' headwords']=len(rawterms)
 write('dict.json',entries);write('altsem.json',altsem)
 trie={}
 for w in entries:
  t=trie
  for part in w.split():t=t.setdefault(part,{})
  t['']=w
 pat=re.compile(r'[^\W\d_]+|[^\s\w]+|[\d_]+'); df=collections.Counter(); nsent=0
 with tarfile.open('mixed.tar.gz','r|gz') as f:
  for m in f:
   if m.name.endswith('-sentences.txt'):
    for b in f.extractfile(m):
     s=nfc(b.decode('utf8').rstrip('\r\n').partition('\t')[2].lower()); blocks=pat.findall(s); seen=set()
     for i,w in enumerate(blocks):
      node=trie.get(w); j=i
      while node is not None:
       if '' in node:seen.add(node[''])
       j+=1
       if j==len(blocks):break
       node=node.get(blocks[j])
     df.update(seen);nsent+=1
 counts['sentences']=nsent;counts['lowercase-vi-1-4']=len(entries);write('df.json',df);write('prep-stats.json',counts);print(counts)
