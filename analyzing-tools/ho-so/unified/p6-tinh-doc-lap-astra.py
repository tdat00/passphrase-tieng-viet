"""Đối chứng độc lập S2–S4, Q và C13 từ các nhãn/khóa đã phân xử; không đọc điểm của Opus."""
import argparse, csv, hashlib, itertools, json, os, unicodedata as U
from pathlib import Path
from collections import Counter, defaultdict
from fractions import Fraction

os.chdir(Path(__file__).resolve().parent)
ALPHA="aăâbcdđeêghiklmnoôơpqrstuưvxy";TONES="\u0300\u0309\u0303\u0301\u0323"
alphabet={c:i for i,c in enumerate(ALPHA)}
allowed=set(ALPHA)|{U.normalize('NFC',v+t) for v in 'aăâeêioôơuưy' for t in TONES}
KEEP=set("mặt trời|mặt trăng|trái đất|ngân hà|công chúa|hoàng tử|hoàng hậu|mồ hôi|ruồi|gián|chào cờ|ròng rọc|dép lê|bánh chưng".split("|"))
LIM_F=77;LIM_R=388;TARGET=7776;BACKUP=300
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def fold(w):
    return "".join(c for c in U.normalize('NFD',w.lower()) if not U.category(c).startswith('M')).replace('đ','d').replace(' ','')
def o1(w):
    v=[]
    for syl in w.split(" "):
        de=U.normalize("NFD",syl)
        tone=[1+TONES.index(z) for z in de if z in TONES]
        assert len(tone)<=1
        bare=U.normalize("NFC","".join(z for z in de if z not in TONES))
        v.append((tuple(alphabet[c]for c in bare),tone[0]if tone else 0))
    return tuple(v)
def risk(w):
    vals=set()
    for t in w.split(" "):
        syl=U.normalize('NFC',''.join(c for c in U.normalize('NFD',t) if c not in TONES))
        for i,ons in enumerate((("s","x"),("ch","tr"),("d","gi","r"),("l","n"))):
            if any(syl.startswith(a)and (len(syl)>len(a)or a==syl=='gi') for a in ons):
                if i==3 and syl.startswith(('ng','nh')):continue
                vals.add(i)
        if syl.endswith(('c','t')):vals.add(4)
        if syl.endswith(('n','ng')):vals.add(5)
    return min(len(vals),4)
def pct(nums):
    counts=Counter(x for x in nums if x>0)
    n=sum(counts.values()); p={0:Fraction(0)};before=0
    for x,num in sorted(counts.items()):
        p[x]=Fraction(100*(2*before+num+1),2*n);before+=num
    return [p[n]for n in nums]
def cents(n):
    v=abs(n)*100;q,r=divmod(v.numerator,v.denominator)
    return (q+(2*r>=v.denominator))*(1 if n>=0 else -1)
def score(pool):
    bylen=defaultdict(list)
    for w in pool:bylen[w.count(' ')+1].append(w)
    for ws in bylen.values():
        pc=[pct([pool[w][n]for w in ws])for n in ('sub_sach','web_sach','leipzig','tatoeba')]
        for i,w in enumerate(ws):
            o=pool[w];o['F']=sum(v[i]for v in pc)/4;o['G']={'C':15,'H':5,'K':0,'F':-20}[o['lop']];o['co_so']=o['F']+o['G']
    for w,o in pool.items():
        p=w.split();rev=" ".join(reversed(p));both=len(p)==2 and rev!=w and rev in pool
        second=both and (o['co_so']<pool[rev]['co_so'] or o['co_so']==pool[rev]['co_so'] and o1(w)>o1(rev))
        o['T']=risk(w)+5*bool(o['phat_h5d'])+5*(len(fold(w))>10)+3*(len(p)==3)+5*second
        o['diem_goc']=o['co_so']-o['T'];o['diem_x100']=cents(o['diem_goc'])
    return sorted(pool,key=lambda w:(pool[w]['nhan']!='OK',-pool[w]['diem_x100'],len(fold(w)),o1(w)))
def binof(o):
    return ('R1'if o['nhan']=='R1'else'OK')+('_F'if o['lop']=='F'else'_N')
def subst(sup,base,free_f):
    """Lập phép gán thay thế riêng biệt; R1 chỉ thay R1, không giả định sẽ loại một F trước."""
    m=Counter(base);trace=Counter();slack=free_f
    for r,targets in [('R1_F',('R1_F','R1_N')),('R1_N',('R1_N','R1_F')),
                      ('OK_F',('OK_F','R1_F','OK_N','R1_N')),('OK_N',('OK_N','OK_F','R1_N','R1_F'))]:
        remains=sup[r]
        for b in targets:
            cost=r.endswith('_F') and not b.endswith('_F')
            q=min(remains,m[b],slack if cost else remains)
            if q>0:
                trace[r,b]+=q;m[b]-=q;remains-=q
                if cost:slack-=q
        if remains:return None
    return trace
def choose(pool,order,keep=KEEP,size=TARGET,rf=LIM_F,rr=LIM_R,bn=BACKUP):
    if not keep<=pool.keys():raise ValueError("Thiếu từ chủ quyết "+repr(keep-pool.keys()))
    main=list(sorted(keep,key=o1));reserved=set(main)
    f=sum(pool[w]['lop']=='F'for w in main);r=sum(pool[w]['nhan']=='R1'for w in main)
    if f>rf or r>rr:raise ValueError("Chỉ thị/hạn mức xung đột")
    buckets=Counter(binof(pool[w])for w in set(pool)-keep)
    b=min(rf-f,buckets['OK_F']);c=min(rr-r,buckets['R1_N']);d=min(buckets['R1_F'],rf-f-b,rr-r-c)
    upper=len(keep)+buckets['OK_N']+b+c+d
    for w in order:
        if len(main)==size:break
        if w in reserved:continue
        ff=int(pool[w]['lop']=='F');rr1=int(pool[w]['nhan']=='R1')
        if f+ff>rf or r+rr1>rr:continue
        main.append(w);reserved.add(w);f+=ff;r+=rr1
    assert len(main)==min(size,upper)
    # Ưu tiên khóa OK không-F, vì thay được cả mục OK không-F. Ứng viên chuyên biệt chỉ thay đúng ngăn.
    remaining=[w for w in order if w not in reserved];remaining.sort(key=lambda w:{'OK_N':0,'OK_F':1,'R1_N':2,'R1_F':3}[binof(pool[w])])
    by=Counter(binof(pool[w])for w in main if w not in keep)
    supply=Counter();repl=[]
    for w in remaining:
        if len(repl)>=bn:break
        g=binof(pool[w])
        supply[g]+=1
        if subst(supply,by,rf-f) is not None:repl.append(w)
        else:supply[g]-=1
    map_bins=subst(supply,by,rf-f)
    return main,repl,{'N_cong_ra':len(pool),'suat_kha_dung':upper,'chinh':len(main),'du_phong':len(repl),'chinh_F':f,'chinh_R1':r,
                      'ngan_tong':dict(Counter(binof(o)for o in pool.values())),'ngan_chinh':dict(Counter(binof(pool[w])for w in main)),
                      'ngan_du_phong':dict(supply),'suat_thay_the_gan_rieng':{'→'.join(k):v for k,v in map_bins.items()},
                      'dat':len(main)==size and len(repl)==bn}
def counterfactual(pool,main):
    """Chỉ diễn giải cho chủ: không nới luật khi dựng chính/dự phòng và không hạch toán tín dụng rút một F/R1."""
    m=set(main);avail=Counter(binof(pool[w])for w in pool.keys()-m);slots=Counter(binof(pool[w])for w in m-KEEP)
    slack_f=LIM_F-sum(pool[w]['lop']=='F'for w in m);slack_r=LIM_R-sum(pool[w]['nhan']=='R1'for w in m)
    initial_f=slack_f;initial_r=slack_r;sub=Counter()
    for source,targets in (('OK_N',('OK_N','OK_F','R1_N','R1_F')),('OK_F',('OK_F','R1_F','OK_N','R1_N')),
                           ('R1_N',('R1_N','R1_F','OK_N','OK_F')),('R1_F',('R1_F','R1_N','OK_F','OK_N'))):
        for t in targets:
            cost_f=source.endswith('_F')and not t.endswith('_F');cost_r=source.startswith('R1')and not t.startswith('R1')
            z=min(avail[source],slots[t],BACKUP-sum(sub.values()),slack_f if cost_f else BACKUP,slack_r if cost_r else BACKUP)
            if z<=0:continue
            avail[source]-=z;slots[t]-=z;sub[source,t]+=z
            if cost_f:slack_f-=z
            if cost_r:slack_r-=z
    return {'khong_phai_quy_tac_da_ky':True,'khong_dat_muc_3_chu':True,'so_khoa_gan_duoc_neu_chu_duyet_R1_thay_OK':sum(sub.values()),
            'Q2_trong_truoc_thay':initial_r,'Q2_trong_sau_thay_bao_thu':slack_r,'Q3_trong_truoc_thay':initial_f,
            'Q3_trong_sau_thay_bao_thu':slack_f,'tuyen_thay_kha_thi':{'→'.join(k):z for k,z in sub.items()}}
def indicators(P,sel):
    samp=sorted(sel,key=lambda w:hashlib.sha256(('Astra-Opus-M1-v1-20261119|'+fold(w)).encode()).digest())[:300]
    c=Counter(P[w]['lop']for w in samp);len3=sum(len(w.split())==3 for w in sel);total=sum(len(fold(w))for w in sel)
    exempt=sum(bool(P[w]['h8_ngoai_le'])for w in sel);starts=Counter(w.split()[0]for w in sel)
    m=Counter((P[w]['lop_A'],P[w]['lop_O'])for w in samp)
    if any(a not in ('C','H','K','F')or o not in ('C','H','K','F')for a,o in m):raise ValueError('Thiếu một lớp gốc trong mẫu M1.')
    matched=sum(n for (a,o),n in m.items()if a==o and a in('C','H'))
    dif=sum(n for (a,o),n in m.items()if a!=o)
    lower=sum(n for (a,o),n in m.items()if a in('C','H')and o in('C','H'))
    upper=sum(n for (a,o),n in m.items()if a in('C','H')or o in('C','H'))
    return {'M1_mau_n':len(samp),'M1_lop_mau':dict(c),'M1_C_cong_H':(c['C']+c['H'])/len(samp),
            'M1_lech_ma_goc':dif,'M1_lech_qua_bien_CH_KF':upper-lower,'M1_can_hai_phieu_so_tu':[lower,upper],
            'M1_gia_dinh_moi_lech_loai_deu_khong_tinh_hoac_deu_tinh':[matched,matched+dif],
            'M2_ba_khoi':len3,'M2_ti_le':len3/len(sel),'M3_tong_chu':total,'M3_trung_binh':total/len(sel),
            'M4_ngoai_le_H8':exempt,'M4_ti_le':exempt/len(sel),'M5_so_nhieu_nhat':max(starts.values()),
            'M5_am_tiet_dau_dat_muc_do':sorted([w for w,n in starts.items()if n==max(starts.values())],key=o1),
            'M1_seed':'Astra-Opus-M1-v1-20261119| + khóa','M1_mau_sha':hashlib.sha256(('\n'.join(samp)+'\n').encode()).hexdigest()}
def validate_bytes(b,n):
    s=b.decode('utf8',errors='strict')
    if s.startswith('\ufeff')or not s.endswith('\n')or '\r'in s or s!=U.normalize('NFC',s):raise ValueError('Không đúng UTF-8/NFC/LF (cần LF cuối, không BOM).')
    words=s[:-1].split('\n')
    if len(words)!=n:raise ValueError(('Sai số dòng',len(words),n))
    keys=set();caps=set();prev=None;initials=[]
    for i,w in enumerate(words,1):
        pieces=w.split(' ');k=fold(w);wc=w[:1].upper()+w[1:]
        if not (1<=len(pieces)<=3 and all(p and set(p)<=allowed for p in pieces) and 4<=len(k)<=12):raise ValueError(('H1/H2',i,w))
        if k in keys or fold(wc)in caps or fold(wc)!=k or wc!=U.normalize('NFC',wc):raise ValueError(('H4',i,w))
        cur=o1(w)
        if prev is not None and not prev<cur:raise ValueError(('O1',i,w))
        if not initials or k[0]!=initials[-1]:initials.append(k[0])
        keys.add(k);caps.add(fold(wc));prev=cur
    if initials!=sorted(set(initials)):raise ValueError(('Nhóm đầu không liền mạch',initials))
    return words,keys
def published(fn_main,fn_reserve):
    if not all(Path('_done',f'P{s}-{a}.flag').is_file()for s in(4,5)for a in('opus','astra')):raise SystemExit('Chưa đóng P4/P5 ở cả hai bên.')
    frozen=json.loads(Path('p6-suc-chua-astra.json').read_text(encoding='utf8'))
    if not frozen.get('dat'):raise SystemExit('Cửa sức chứa Astra chưa đạt.')
    if frozen.get('sha_script')!=sha(__file__) or any(sha(p)!=v for p,v in frozen['sha_dau_vao'].items()):raise ValueError('Phiên bản tính/đầu vào đã đổi; phải tính độc lập lại.')
    sets=[];snap={}
    for their,ours,n in ((fn_main,'p6-chinh-astra.txt',TARGET),(fn_reserve,'p6-du-phong-astra.txt',BACKUP)):
        b=Path(their).read_bytes();ws,ks=validate_bytes(b,n)
        expected=frozen['sha_'+ours]
        if sha(ours)!=expected or hashlib.sha256(b).hexdigest()!=expected:
            left=Path(ours).read_text(encoding='utf8').splitlines();i=next((i for i,(l,r)in enumerate(zip(left,ws),1)if l!=r),None)
            raise ValueError(('Khác kết quả tính độc lập',their,'dòng',i))
        sets.append(ks);snap[str(their)]=expected
    d=json.loads(Path('tap-luat-P2-v4.json').read_text(encoding='utf8'))['danh_sach'];forbidden=set().union(*(d[k]for k in('khoa_bo','k0_khoa','k1_khoa','k2_chua_ky_91_khoa')))
    if sets[0]&sets[1]or (sets[0]|sets[1])&forbidden or not {fold(w)for w in KEEP}<=sets[0]:raise ValueError('Giao chính/dự phòng, chỉ thị hoặc cổng khóa đỏ.')
    print(json.dumps({'so_chinh':len(sets[0]),'so_du_phong':len(sets[1]),'sha':snap,'doi_chieu_Astra':True},ensure_ascii=False))
def input_raw(name):
    with Path(name).open(encoding='utf-8-sig',newline='')as f:
        for r in csv.DictReader(f,delimiter='\t'):yield r
def run(filename,counts_files):
    if not all(Path('_done',f'P{s}-{a}.flag').is_file()for s in(4,5)for a in('opus','astra')):raise SystemExit('Chưa đóng P4/P5 ở cả hai bên; không mở phiếu/chạy P6.')
    originals={}
    for who in ('astra','opus'):
        fname=f'phieu-{who}.tsv';fr=Path('_done',f'P4-{who}.flag')
        if sha(fname) not in fr.read_text(encoding='utf-8-sig').lower():raise ValueError('Phiếu gốc thay đổi: '+who)
        originals[who]={r['tu']:r['lop']for r in input_raw(fname)}
    counts={}
    for file in counts_files:
        for r in input_raw(file):
            fields=('sub_sach','web_sach','leipzig_so_cau','tatoeba_so_cau','opensub_n','ccaligned_n')
            if r.get("ung_vien","").startswith("["):
                vs={k:json.loads(r[k])for k in ('ung_vien',*fields)}
                for j,w in enumerate(vs['ung_vien']):counts[w]=[vs[k][j]for k in fields]
            else:counts[r['tu']]=[int(r[k])for k in fields]
    P={};seen=set()
    for r in input_raw(filename):
        w=r['tu'];k=fold(w);assert k==r['khoa'] and k not in seen and w not in P and 4<=len(k)<=12 and 1<=len(w.split(' '))<=3
        seen.add(k);assert r['nhan']in('OK','R1') and r['lop']in('C','H','K','F')
        p=dict(zip(('sub_sach','web_sach','leipzig','tatoeba','sub_be_mat','web_be_mat'),counts[w]));assert all(type(x)==int and x>=0 for x in p.values())
        p['h8_ngoai_le']=not any(p[k]for k in ('leipzig','tatoeba','sub_be_mat','web_be_mat'))
        p.update(nhan=r['nhan'],lop=r['lop'],lop_A=r.get('lop_A')or originals['astra'].get(w),lop_O=r.get('lop_O')or originals['opus'].get(w),phat_h5d=bool(int(r['phat_h5d'])));P[w]=p
    order=score(P);sel,reserve,stats=choose(P,order)
    log=Path('p6-suc-chua-astra.json')
    stats['sha_dau_vao']={str(f):sha(f)for f in (filename,*counts_files,'tap-luat-P2-v4.json','phieu-astra.tsv','phieu-opus.tsv')};stats['sha_script']=sha(__file__)
    if not stats['dat']:
        if len(sel)==TARGET:
            stats['chi_bao_chinh_tam_khong_phat_hanh']=indicators(P,sel)
            stats['kich_ban_chi_de_trinh_chu']=counterfactual(P,sel)
        for key,ws in [('chinh',sel),('du_phong',reserve)]:
            data=('\n'.join(sorted(ws,key=o1))+'\n').encode('utf8');validate_bytes(data,len(ws));stats['sha_'+key+'_tam_chua_dat_C13']=hashlib.sha256(data).hexdigest()
        log.write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n');print(stats);return
    stats['chi_bao']=indicators(P,sel)
    for title,items in [('p6-chinh-astra.txt',sorted(sel,key=o1)),('p6-du-phong-astra.txt',sorted(reserve,key=o1))]:
        b=('\n'.join(items)+'\n').encode('utf8');validate_bytes(b,TARGET if title=='p6-chinh-astra.txt'else BACKUP);Path(title).write_bytes(b);stats['sha_'+title]=hashlib.sha256(b).hexdigest()
    with Path('p6-diem-astra.tsv').open('w',encoding='utf8',newline='')as f:
        wr=csv.writer(f,delimiter='\t',lineterminator='\n');wr.writerow('khoa tu nhan lop F_chinh_xac G T diem_chinh_xac diem_100'.split())
        for w in order:
            p=P[w];wr.writerow((fold(w),w,p['nhan'],p['lop'],str(p['F']),p['G'],p['T'],str(p['diem_goc']),p['diem_x100']))
    log.write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n');print(stats)
def test():
    assert pct([0,5,5,15])==[0,50,50,100] and pct([1])==[100] and pct([0,0])==[0,0]
    assert cents(Fraction(1005,1000))==101 and cents(Fraction(-1005,1000))==-101
    assert o1('anh rể')<o1('ánh mắt') and o1('ăn')<o1('ấn') and o1('da')<o1('đa')
    assert risk('nghe nhạc')==1 and risk('sách')==1 and risk('sương')==2 and risk('gì')==1
    assert subst(Counter({'R1_N':2,'OK_F':1}),Counter({'R1_N':1,'R1_F':2}),0)
    assert subst(Counter({'R1_F':1}),Counter({'OK_F':2}),4) is None
    p={w:{'nhan':r,'lop':c}for w,r,c in [('chung','OK','K'),('đông','OK','H'),('xanh','OK','F'),('trắng','R1','C'),('đẹp','R1','F')]};main,sp,st=choose(p,list(p),set(),size=3,rf=1,rr=1,bn=1);assert len(main)==3 and len(sp)==0 and st['suat_kha_dung']==4
    lines='anh rể\nánh mắt\nsương\n';assert validate_bytes(lines.encode(),3)[1]=={'anhre','anhmat','suong'}
    for bad in [lines.replace('\n','\r\n'),lines+'sương\n',lines[:-1],'\ufeff'+lines,'anh rể\nán hả\n','nội thất\nnói thật\n','cáćh\n']:
        try:validate_bytes(bad.encode(),len(bad.splitlines()))
        except (ValueError,AssertionError):continue
        raise AssertionError(('Bộ thử đã cho qua một chuỗi không hợp lệ',bad))
    sample={w:{'lop_A':a,'lop_O':o,'lop':z,'h8_ngoai_le':False}for w,a,o,z in [('chung','H','H','H'),('đông','C','H','C'),('đóng','C','K','H'),('xanh','F','K','F')]}
    m=indicators(sample,list(sample));assert m['M1_can_hai_phieu_so_tu']==[2,3]and m['M1_gia_dinh_moi_lech_loai_deu_khong_tinh_hoac_deu_tinh']==[1,4]
if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument('--test',action='store_true');a.add_argument('--input');a.add_argument('--counts',nargs='+',default=['bang-khoa-chung.tsv']);a.add_argument('--doi-chieu',nargs=2,metavar=('CHINH','DU_PHONG'));p=a.parse_args()
    test()
    if p.input:run(p.input,p.counts)
    if p.doi_chieu:published(*p.doi_chieu)
    elif p.test:print('Kiểm số 0, đồng hạng, nhóm đơn, làm tròn chính xác, O1, rủi ro âm đầu và ngăn thay thế: đạt.')
