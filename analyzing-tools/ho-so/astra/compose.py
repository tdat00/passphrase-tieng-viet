import concurrent.futures as cf, json, os, re, sys, time, threading
from pathlib import Path
import requests
from prepare import *
URL='http://127.0.0.1:19263/v1/chat/completions'; K=Path('local.key').read_text(encoding='ascii').strip(); local=threading.local()
def ask(messages,maximum=800,seed=61913,grammar=None):
 if not hasattr(local,'http'):local.http=requests.Session(); local.http.trust_env=False
 b={'model':'local','messages':messages,'temperature':0.16,'seed':seed,'max_tokens':maximum,'chat_template_kwargs':{'enable_thinking':False},'top_p':0.85,'stream':False}
 if grammar:b['grammar']=grammar
 for i in range(3):
  try:
   r=local.http.post(URL,headers={'Authorization':'Bearer '+K},json=b,timeout=300);r.raise_for_status();msg=r.json()['choices'][0]['message']['content'];return msg
  except Exception as e:
   if i==2:raise
   time.sleep(2**i)
from select_words import D,pos,valid_source
SKIP=set('là làm bằng để cho của có hay và đã cái con những các sự một ở khi mà từ rất theo như được trong không nào này người với nhiều nó đó dùng tới trên vào thuộc tức chẳng cùng bằng một mỗi cũng thường giữa để thì vậy hoặc thứ phần bộ loại chỉ đến ra vật của đặt thế lấy hoặc tại đồng thường người như một từ mà là'.split())
CHOICE={'diều':1,'khăn':0,'tranh':0,'chân':0,'đường':0,'nghiên':0,'chuông':0,'vành khuyên':0,'công tắc':0,'công':0}
def hint(w):
 r=D.get(w,{'v':[],'e':[]});v=[z for z in r['v'] if valid_source(z)] or r['v'];e=[z for z in r['e'] if valid_source(z)];v=[z for z in v if z[1]]
 if w in CHOICE and len(v)>CHOICE[w]:v=[v[CHOICE[w]]]+[z for i,z in enumerate(v) if i!=CHOICE[w]]
 def bag(s):
  ts=[q for q in re.findall(r'[^\W\d_]+',s.lower()) if q not in SKIP and q not in w.split()];return ','.join(sorted(set(ts[:15])))
 vih=' / '.join(filter(None,[bag(z[1]) for z in v[:2]]));eng=' / '.join(z[1].split('(')[0].strip()[:62] for z in e[:3] if z[1] and not re.search(r'(?i)spelling|alternative|syllable|variant|form of',z[1]));return (vih+'; '+eng).strip(' ;/')
def refs(w):
 r=D.get(w,{'v':[],'e':[]});v=[z for z in r['v'] if valid_source(z)] or r['v'];e=[z for z in r['e'] if valid_source(z)];v=list(dict.fromkeys(z[1] for z in v if z[1]));e=list(dict.fromkeys(z[1] for z in e if z[1] and not re.search('tone placement|alternative (?:spelling|form)|syllable',z[1],re.I))); idx=CHOICE.get(w,0)
 if 0<idx<len(v):v=[v[idx]]+[z for j,z in enumerate(v) if j!=idx]
 return v,e
SYS="""Bạn biên soạn bảng chú giải cho người Việt. Hãy giải nghĩa chính xác từng từ bằng LỜI MỚI bình dị. Không chép lời tham khảo; không đặt câu ví dụ, không kể chuyện. Chọn một nghĩa quen dùng phù hợp với thông tin cho chính từ ấy. Mỗi lời giải thích khoảng 5–12 tiếng. Không giải thích bằng chính từ đó. Ví dụ 'mái chèo' → 'Thanh có bản dẹt, quạt nước để đẩy thuyền.'; 'kiên nhẫn' → 'Bền lòng theo đuổi việc cần nhiều thời gian.'
Mức A: rất quen trong đời sống; B: thường gặp trong sách phổ thông, việc làm; C: ít gặp, cổ, hẹp nghề hoặc địa phương; X: tên riêng, thô tục, xúc phạm, bạo lực, vũ khí, chiến tranh, tội phạm, bệnh/tật, cái chết, tình dục, chính trị hoặc tôn giáo đặc thù, hoặc không rõ nghĩa. X không cần giải thích. Trả lời không lời dẫn: mỗi dòng có số thứ tự, mức, nghĩa: 1|A|Thanh có bản dẹt, quạt nước để đẩy thuyền. Không viết lại đầu mục."""
def draft(words):
 arr=[]
 for w in words:
  v,e=refs(w);v=' / '.join([v[0][:185]]+([v[1][:95]] if len(v)>1 and len(v[0])<28 else [])) if v else '';e=(e[0].split('(')[0][:56] if e else '')
  arr.append(f'{len(arr)+1}. {w}: {v} [{e}]')
 rules=['root ::= '+' "\\n" '.join('"'+str(i)+'|" row' for i in range(1,len(words)+1)),'row ::= "X|-" | [ABC] "|" [^\\n\\r|]+'];gr='\n'.join(rules)
 text='Soạn nghĩa, không đặt câu ví dụ.\n'+'\n'.join(arr);msg=ask([{'role':'system','content':SYS},{'role':'user','content':text}],max(160,len(words)*55),grammar=gr);found={}
 for l in msg.splitlines():
  m=re.fullmatch(r'\s*(\d+)\s*\|\s*([ABCX])\s*\|\s*(.*?)\s*',l)
  if m and 0<int(m[1])<=len(words):found[words[int(m[1])-1]]=[m[2],nfc(m[3].strip())]
 out={}
 for w in words:
  rating,g=found.get(w,['?',msg[:450]]);g=re.sub(r'^'+re.escape(w)+r'\s+(?:là|chỉ)\s+','',g,flags=re.I);g=re.sub(r'^Là\s+','',g,flags=re.I);g=g[:1].upper()+g[1:];out[w]=[rating,g]
 return out
def combine(n='draft.jsonl'):
 out={};p=Path(n)
 if p.exists():
  for l in p.read_text(encoding='utf8').splitlines():
   if l:out.update(json.loads(l))
 return out

def run(words,fn=draft,output='draft.jsonl',k=12,threads=16):
 done=combine(output); todo=[w for w in words if w not in done or done[w][0]=='?']; groups=[todo[i:i+k] for i in range(0,len(todo),k)]; print('pending',len(todo),'groups',len(groups),flush=True);start=time.time();count=0
 with cf.ThreadPoolExecutor(threads) as pool,open(output,'a',encoding='utf8',newline='\n') as f:
  fs={pool.submit(fn,g):g for g in groups}
  for future in cf.as_completed(fs):
   g=fs[future]
   try:d=future.result()
   except Exception as e:print('ERROR',repr(e),flush=True);continue
   f.write(json.dumps(d,ensure_ascii=False)+'\n');f.flush();count+=len(g)
   if count%(k*20)<k or count>=len(todo):print(count,round(time.time()-start,1),flush=True)
if __name__=='__main__':
 if sys.argv[1]=='test':
  w=['máy bay','nghiên','diều','vành khuyên','công tắc','sên','bản lề','u nang','xâm lăng','kiên nhẫn','thời gian','khanh'];print(json.dumps(draft(w),ensure_ascii=False,indent=1))
 else:
  w=[x for x in Path('rank.txt').read_text(encoding='utf8').splitlines() if ' ' in x];run(w[:int(sys.argv[1])],k=8,threads=24)
