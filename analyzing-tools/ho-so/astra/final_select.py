from quality import *
def results(name):
 d={}
 for l in infile(name):
  if l:d.update(json.loads(l))
 return d
REV=results('review.jsonl');CH=results('challenge.jsonl');E=read('sem.json') if Path('sem.json').exists() else {};override=set(w for l in infile('approve.txt') for w in l.split('|') if w)
allgloss={' '.join(texttokens(z[1])) for r in D.values() for z in r['v'] if z[1]};proper_mark=re.compile('(?i)dạng viết phân biệt chữ hoa|alternative letter-case form|alternative capitalization of');
def final(permit_wait=False):
 base,why0,flags=pool();good={};why=collections.Counter();cases={}
 for w,(g,m,sc) in base.items():
  if ' '.join(texttokens(g)) in allgloss:reason='trùng nguyên nghĩa bất kỳ';why[reason]+=1;cases[w]=reason;continue
  if w in MAN:good[w]=[g,m,sc];continue
  if any(proper_mark.search(z[1]) for a in ('v','e') for z in D[w][a]) and not any(valid_source(z) and not proper_mark.search(z[1]) for z in D[w]['v']):why['kiểu viết tên riêng']+=1;cases[w]='kiểu viết tên riêng';continue
  if w not in E and not permit_wait:why['đợi đối chiếu E5']+=1;cases[w]='đợi đối chiếu E5';continue
  if w in E and max(E[w])<.84 and w not in override:why['E5 cực thấp']+=1;cases[w]='E5 cực thấp';continue
  r=REV.get(w,['?'])[0];c=CH.get(w,['?'])[0];code='O' if r=='O' else c
  if (code!='O' or r!='O' and w not in override) and not (permit_wait and code=='?'):
   why['xét lại '+code]+=1;cases[w]='xét lại '+code;continue
  good[w]=[g,m,sc]
 sel,rej,drops=choose(good,7776)
 return sel,good,why,rej,flags,cases,drops,why0
if __name__=='__main__':
 import sys
 sel,good,why,rej,fl,ca,ds,wh=final('--waiting' in sys.argv);print('raw',len(RAW),'pool',len(pool()[0]),'good',len(good),'selected',len(sel),'review',len(REV),'challenge',len(CH),'model filters',why,'selectors',rej,'base',wh,flush=True);print('manual still rejected',[(w,f) for w,f in list(fl.items())+list(ca.items()) if w in MAN]);write('final-preview.json',sel);write('final-cases.json',ca);write('final-drops.json',ds)
