from select_words import *
import difflib,hashlib,random,statistics
R=read('rank.json');S=read('seg.json');H=read('seg-talk.json')
def infile(f):
 return Path(f).read_text(encoding='utf8').splitlines() if Path(f).exists() else []
def manual():
 out={}
 for f in ('single.tsv','manual.tsv','fix.tsv','audit-fixes.tsv'):
  for l in infile(f):
   if '|' in l:
    w,g=l.split('|',1);out[w.strip()]=g.strip()
 return out
MAN=manual();MAN.pop('ong nghệ',None)
RAW={}
for runfile in ('draft.jsonl','reserve.jsonl'):
 for l in infile(runfile):
  if l:RAW.update(json.loads(l))
CUT=set(s.strip() for l in infile('veto.txt') for s in l.split('|') if s.strip())
TOK=split('khủng bố|xâm lăng|xâm lược|xâm hại|xâm phạm|vũ lực|bạo lực|đao|gươm|súng|đạn|vũ khí|pháo|quân|lính|tướng quân|lãnh tụ|đảng|nội các|nguyên thủ|chính trị|chính phủ|quốc hội|quốc trưởng|cộng sản|tư sản|vô sản|thực dân|đế quốc|phát xít|dân biểu|nghị viện|nghị sĩ|nghị sỹ|đối lập|phiến loạn|phản loạn|bang giao|ngoại giao|dân tộc chủ nghĩa|đức tin|thần linh|thần thánh|thần học|giáo phái|giáo hội|giáo dân|giáo xứ|tín đồ|nhà sư|nhà thờ|nhà chùa|Phật|phật|chúa|satan|thánh|linh mục|kinh phật|luân hồi|âm phủ|cõi âm|địa ngục|âm hồn|tâm linh|trừ tà|ma quỷ|mê tín|dị đoan|phong thủy|quê ma|quỷ|bùa|ngải|ấn đường|chữa bệnh|bệnh|bịnh|viêm|ung bướu|u nang|khối u|u ác|đau tim|suy tim|đột quỵ|động kinh|đái tháo đường|tiểu đường|đau ốm|ốm đau|đau đầu|đau bụng|đau yếu|bại liệt|bại não|thiểu năng|tâm thần|mất trí|ngộ độc|nhiễm trùng|nhiễm khuẩn|suy dinh dưỡng|ngất xỉu|tàn tật|khuyết tật|mù lòa|câm điếc|đui mù|mụn|mủ|lở loét|mồ mả|tang ma|đám tang|đám ma|mộ phần|mộ chí|mồ chôn|quan tài|tử thi|hài cốt|tro cốt|cải táng|mai táng|hỏa táng|an táng|khâm liệm|khâm liệm|hung thủ|truy nã|trại giam|nhà giam|nhà tù|tù nhân|tử tù|tử hình|án tù|án mạng|giết|chém|đấm|đá đấm|đá hậu|đá gà|trộm|cướp|trấn lột|móc túi|đạo chích|du côn|xã hội đen|côn đồ|hung hăng|hung dữ|hung bạo|ác ôn|dã man|man rợ|nhẫn tâm|tàn nhẫn|tàn độc|tàn ác|độc ác|ác độc|tàn sát|tiêu diệt|sát hại|tàn phá|đàn áp|cưỡng ép|bắt nạt|uy hiếp|đe dọa|đe doạ|dọa nạt|hăm dọa|vu khống|vu oan|sỉ nhục|làm nhục|mạt sát|nặc danh tố cáo|thù|hận|căm ghét|oán giận|căm giận|thù oán|nguyền rủa|chửi|quấy rối|cờ bạc|ăn chơi trác táng|cá cược|cá độ|sòng bạc|đỏ đen|bài bạc|con bạc|đánh bạc|đánh cược|rượu|bia|thuốc lá|ma túy|ma tuý|tiêm chích|hút xách|cần sa|thuốc phiện|độc dược|chất độc|đầu độc|dâm|dục tình|tình dục|giao hợp|tinh dịch|dương vật|âm đạo|sinh dục|ngoại tình|loạn luân|giang mai|phá thai|sảy thai|bạo hành|hiếp|đĩ|điếm|bêu riếu|hỏi cung|tra khảo|thẩm vấn|mưu phản|mưu sát|khủng hoảng tinh thần|đấu tố|đấu súng|đánh nhau|đánh nhau|lạm dụng|sa đọa|tự sướng|tống tiền|gian lận|lừa đảo|ăn cắp|tham nhũng|hối lộ|tham ô|tham nhũng|biển thủ|gian lận|đút lót|phạm pháp|bất hợp pháp|khởi tố|tố tụng|bắt giữ|lừa gạt|nội chiến|ngoại xâm|đô hộ|thống trị|thất thủ|đánh chiếm|tiêu vong|suy vong|đau đớn|đau thương|bi thảm|thảm khốc|thảm họa|tuyệt vọng|tuyệt thực|tang tóc|đòi mạng|đe nẹt|tống đạt|phi pháp|mại dâm|ăn hại|chết|tử nạn|tử vong|tử trận|mất mạng|sát sinh|đứt lìa|chấn thương|thương binh|bị thương|thương tích|chảy máu|tự hại|hủy hoại|huỷ hoại|dị giáo|phản bội|tiền án|tiền sự|vô nhân|vô đạo|vô liêm|bất lương|thất đức|đê tiện|đồi bại|tồi tệ|khốn nạn|khốn kiếp|tội đồ|ly dị|li dị|ly hôn|li hôn|cực đoan|coi thường|khinh bỉ|hành hạ|thượng đế|thờ cúng|cúng tế|đày đọa|chà đạp|bóc lột|lăng mạ|tẩy chay|thù hận|suy nhược|trầm cảm|trầm uất|sợ hãi|khiếp sợ|kinh hoàng|kinh hãi|tuyệt tự|vô sinh|nam khoa|phụ khoa|sản khoa|ngoại khoa|dược khoa|trị liệu|trấn yểm|tiểu tiện|đại tiện|tiêu chảy|bài tiết|phân biệt chủng tộc|cứt|đái|tình nhân|bồ bịch|đa thê')
PHRASES=split('mắc bệnh|chứng bệnh|căn bệnh|bệnh nhân|vi khuẩn gây bệnh|cơ thể mắc bệnh|dấu hiệu bệnh|chữa trị bệnh|bệnh lí|bệnh lý|người bệnh|bệnh tật|bệnh truyền|khối u|tử vong|chết người|người chết|xác chết|thi thể|giết|tàn sát|đánh nhau|đánh đập|vũ khí|binh khí|vũ trang|quân đội|quân sự|chiến trường|quân địch|quân lính|bắn súng|đạn pháo|giết hại|cảnh sát|bắt giữ|phạm tội|tội ác|bất hợp pháp|tội phạm|kẻ trộm|lừa đảo|người nghiện|ma túy|ma tuý|gây nghiện|hối lộ|cờ bạc|cá cược|hành hình|tử hình|dao găm|thanh kiếm|thần thánh|tôn giáo|thần linh|tín đồ|đức phật|giáo hội|chính đảng|đảng phái|quyền cai trị|chiến tranh|xâm lược|thù hận|gây thương tích|vết thương|dị tật|chất nổ|tình dục|sinh dục|giao cấu|mại dâm|phân biệt chủng tộc|miệt thị|chửi mắng|sỉ nhục|tử thi|loài ma|thiên chúa|hồn ma|người bị hại|chết chóc|cỗ quan tài|tàn nhẫn|đánh bạc|chất độc|bị kết án|lực lượng vũ trang|khủng bố|tấn công|quan hệ xác thịt|chất thải|đầy hơi|tiểu tiện|đại tiện|nước tiểu|ung thư|phân của|cứt|đồ đệ|đánh giết|nhà tu|thầy tu|đối phương bằng vũ lực')
rx=lambda xs:re.compile(r'(?<!\w)(?:'+'|'.join(map(re.escape,sorted(xs,key=lambda w:-len(w))))+r')(?!\w)',re.I)
wordbad=rx(TOK); glossbad=rx(PHRASES);vhuge=rx(split('binh khí|đạn dược|đâm chết|bắn chết|hành hình|xử tử|hiếp dâm|xuất tinh|tinh dịch|mại dâm|giao cấu|cá độ|đánh bạc|bệnh truyền nhiễm|độc dược|người nghiện|ma tuý|ma túy|giết hại|tử thi|tử hình|nhà tù|hài cốt|thi thể|bệnh tật|người chết|tội ác|cái chết|chất nổ|gây thương tích|ung thư|chính đảng'))
def texttokens(s):return re.findall(r'[^\W\d_]+|\d+',nfc(s.lower()))
def source_overlap(w,g):
 aa=texttokens(g);gset=set(aa);best=0;ratio=0
 for z in D[w]['v']:
  bb=texttokens(z[1]);
  if not bb:continue
  sm=difflib.SequenceMatcher(None,aa,bb,autojunk=False);mm=sm.find_longest_match().size;best=max(best,mm);rr=sm.ratio();ratio=max(ratio,rr)
  if aa==bb or len(aa)>=4 and mm==len(aa) or len(bb)>=5 and mm==len(bb) or mm>=6 or len(aa)>=5 and rr>=.78:return True,best,round(ratio,2)
 return False,best,round(ratio,2)
meta=re.compile(r'^(?:xem (?:thêm|mục|từ)\b|như mục|như từ|từ này|có nghĩa là|từ dùng để|cách nói khác của|từ đồng nghĩa|viết tắt|dạng khác|cách viết|một loại (?:cây|chim|cá|hoa)\.?$|giống như từ|đồng nghĩa với|không rõ|không có (?:nghĩa|thông tin|dữ kiện)\b|chưa có nghĩa|không biết nghĩa)|\[(?:xem|ghi chú)|thông tin cung cấp|\bnhư (?:đã nói|trên)\b')
critical=rx(split('chữa bệnh|chữa trị|chữa sốt|chữa cảm|chữa đau|trị bệnh|cầm máu|thuốc|điều trị|y học|y khoa|y dược|làm sảy thai|sảy thai|sẩy thai|bào thai|sinh sản|tình dục|mất chồng|mất vợ|góa|goá|mạng sống|tính mạng|tước mạng|hi sinh|hy sinh|cúng tế|thờ cúng|cầu cúng|cúng bái|tôn giáo|đình chùa|tín ngưỡng|vong linh|chính trị|vua|hoàng đế|chúa|ngai vàng|hoàng gia|triều đình|bộ máy nhà nước|cầm quyền|súng|đạn|gươm|vũ khí|phạm pháp|cưỡng ép|bắt giam|trai gái|bậy bạ|chửi bới|độc ác|sinh mệnh|gây hại cho người|hung dữ|hung hăng|phẫn nộ|gây phẫn nộ|làm hại người|đánh người|thần linh|lễ cúng|trừng phạt|cá cược|đánh bạc|chất ma túy|gây nghiện|người ốm|đau nhức|sinh dục|sức khỏe sinh sản|chất độc|độc tố|phòng bệnh|hành hạ|tàn phá|thiên tai|đánh giặc|giặc|kẻ thù|đấu tranh vũ trang|trận đánh|trận chiến|đánh trận|đánh đòn|giáo phái|tội ác|đau đớn|khóc thương|tội lỗi|tôn thờ|giải độc|tẩy độc|tòa án|bị kết án|toà án|bộ lạc nguyên thủy|mê tín|xác người|cưỡng đoạt|phạm nhân|bị tù|gây hấn|trộm cắp|dâm dục|thây|không sạch sẽ về đạo đức|thô tục|bị đày|nạn nhân|chết|người đã mất|kẻ thù|bàn thờ|trị vì|tín đồ|tu hành'))
def check(w,g,man=False):
 if w in CUT:return 'bỏ tay'
 if not man:
  if wordbad.search(w) or wordbad.search(g) or glossbad.search(g) or critical.search(w) or critical.search(g) or any(vhuge.search(z[1]) for z in D[w]['v'] if valid_source(z)):return 'an toàn'
  if any(k in w.split() for k in ('quỷ','quỉ','tuý','túy')):return 'an toàn'
  if not T.get(w) and (F.get(w,0)<2 or S.get(w,0)==0):return 'chứng liệu yếu'
 t=texttokens(g)
 if not 3<=len(t)<=32 or re.search(r'[|\n\r`<>\[\]{}]|[\u3400-\u9fff]',g) or not re.search(r'[ăâđêôơưàảãáạấầậạÈếềểệìíỉĩịòóỏọốồỗộớờợùúủũụứừựỳýỷỹỵ]',g.lower()):return 'định dạng nghĩa'
 if meta.search(g.lower()):return 'dẫn chiếu'
 if ' ' in w and re.search(r'(?<!\w)'+re.escape(w)+r'(?!\w)',g,re.I):return 'lặp đầu mục'
 if source_overlap(w,g)[0]:return 'quá gần từ điển'
 return ''
def rawscore(w,grade):
 r=R[w];n=len(w.split());ss=S.get(w,0);hh=H.get(w,0)
 return r['score']+.42*math.log2(1+ss)+.53*math.log2(1+min(hh,24))+2*r['concrete']+0.9*(grade=='A')+.55*(n>=2 and r['talk']>0)+.7*(r['df']>0 and r['talk']>0)
def pool():
 items={};why=collections.Counter();flagged={};
 for w,(grade,g) in RAW.items():
  if w in MAN or w not in R or ' ' not in w:continue
  if grade not in ('A','B'):
   why['xếp loại '+grade]+=1;continue
  issue=check(w,g);
  if issue:why[issue]+=1;flagged[w]=issue;continue
  items[w]=[g,'mô hình '+grade,rawscore(w,grade)]
 for w,g in MAN.items():
  if w not in R:flagged[w]='không đủ điều kiện';continue
  issue=check(w,g,True)
  if issue:flagged[w]=issue;why['tay: '+issue]+=1;continue
  items[w]=[g,'biên tập',100+rawscore(w,'A')]
 return items,why,flagged

def choose(items,n):
 l=sorted(items,key=lambda w:(-items[w][2],order(w)));used=set();sel={};rej=collections.Counter();drops={}
 for w in l:
  if len(sel)==n:break
  if flat(w) in used:rej['khóa']+=1;drops[w]='khóa';continue
  near=sorted(a for a in alternatives(w) if a in sel)
  if near:rej['cặp vùng']+=1;drops[w]='cặp vùng: '+near[0];continue
  sel[w]=items[w];used.add(flat(w))
 return sel,rej,drops
if __name__=='__main__':
 items,why,flags=pool();sel,rej,drops=choose(items,7776);print('draft',len(RAW),'manual',len(MAN),'pool',len(items),'selected',len(sel),why,rej,flush=True);print('manual flags:',{w:z for w,z in flags.items() if w in MAN});print('manual near:',{w:v for w,v in drops.items() if w in MAN});write('flags.json',flags);write('selected.json',sel);write('drops.json',drops)
