import sys,os,time,sqlite3,hashlib
from pathlib import Path
sys.path.insert(0,str(Path('pydeps').resolve()));os.environ['TOKENIZERS_PARALLELISM']='false'
import numpy as np,onnxruntime as ort
from tokenizers import Tokenizer
from quality import *
def refs2(w):
 r=D[w];v=list(dict.fromkeys(z[1].strip()[:255] for z in r['v'] if valid_source(z)))[:6];e=list(dict.fromkeys(z[1].strip()[:170] for z in r['e'] if valid_source(z) and not re.search(r'(?i)traditional tone placement|alternative (?:spelling|form)|variant of',z[1])))[:5];return v,e
conn=sqlite3.connect('embed.sqlite');conn.execute('CREATE TABLE IF NOT EXISTS v (t TEXT PRIMARY KEY, vec BLOB)');cache={s:np.frombuffer(b,dtype=np.float16).astype('f') for s,b in conn.execute('select t, vec from v')}
o=ort.SessionOptions();o.intra_op_num_threads=4;o.inter_op_num_threads=1;sess=ort.InferenceSession('e5.onnx',o,providers=['CPUExecutionProvider']);tok=Tokenizer.from_file('e5-tok.json');tok.enable_truncation(max_length=90);tok.enable_padding(pad_id=1,pad_token='<pad>');
def embed(ts):
 missing=sorted(set(ts)-cache.keys(),key=lambda x:(len(x),x));print('to embed',len(missing),'cached',len(cache),flush=True);start=time.time();done=0
 for i in range(0,len(missing),32):
  b=missing[i:i+32];seq=tok.encode_batch(['query: '+t for t in b]);ids=np.array([v.ids for v in seq],dtype=np.int64);mask=np.array([v.attention_mask for v in seq],dtype=np.int64)
  em=sess.run(None,{'input_ids':ids,'attention_mask':mask,'token_type_ids':np.zeros_like(ids)})[0];em=(em*mask[:,:,None]).sum(1)/mask.sum(1)[:,None];em/=np.linalg.norm(em,axis=1)[:,None];em=em.astype(np.float16)
  conn.executemany('insert or replace into v(t,vec) values (?,?)',[(t,v.tobytes()) for t,v in zip(b,em)]);cache.update({t:v.astype('f') for t,v in zip(b,em)});done+=len(b)
  if done%1024<32 or done==len(missing):conn.commit()
  if done%4096<32 or done==len(missing):print(done,round(time.time()-start,1),flush=True)
if sys.argv[1]=='refs':
 groups=[w for w in Path('rank.txt').read_text(encoding='utf8').splitlines() if ' ' in w][:12600]+list(MAN);embed(t for w in groups if w in D for arr in refs2(w) for t in arr)
else:
 items,_,_=pool();texts=[];pairs={}
 for w,(g,m,sc) in items.items():
  v,e=refs2(w);texts.extend([g]+v+e);pairs[w]=(g,v,e)
 embed(texts);scores={}
 for w,(g,v,e) in pairs.items():
  av=[float(cache[g]@cache[a]) for a in v];ae=[float(cache[g]@cache[a]) for a in e];scores[w]=[round(max(av,default=0),4),round(max(ae,default=0),4)]
 write('sem.json',scores);xs=[max(z) for z in scores.values()];print('quantiles',np.quantile(xs,[0,.005,.01,.025,.05,.1,.25,.5,.75,1]));
