import sys,re,random,collections
from compose import ask,run,combine
from quality import *
PS='''Hãy kiểm lỗi bảng từ dùng cho mật khẩu gia đình. Mỗi mục ghi từ, nghĩa đề xuất và chứng cứ từ điển. Chọn chính xác MỘT mã cho mỗi mục theo thứ tự: X = nghĩa nổi bật liên quan bệnh, triệu chứng, tội phạm, lăng mạ, tình dục, giết chóc, vũ khí, quân sự, tang ma, chính trị hay giáo phái; T = tên riêng, biến thể viết dễ lẫn, rất cổ, chủ yếu địa phương hoặc quá chuyên biệt với người bình thường; M = lời giải sai sự thật, sai đối tượng, lặp vô ích, chỉ là câu ví dụ, hoặc gán nghĩa của từ khác; O = mục phổ thông/trung tính và lời giải là cách diễn đạt chấp nhận được cho ÍT NHẤT một nghĩa quen. Không loại động từ/tính từ phổ biến chỉ vì không phải danh từ. Không loại khi gợi ý tham khảo khác mà nghĩa đề xuất là một nghĩa thông dụng bạn biết chắc. Đọc thực sự từng mục. Kiểm tra ngược: 'u nang → khối u bọc dịch' phải là X, 'xâm lăng → xâm chiếm' là X, 'vành khuyên → trang sức đeo tai' là M nếu đang nói về loài chim, 'bút chì → dụng cụ vẽ có lõi than' là O. Hãy chỉ cho biết kết luận, không giải thích.'''
def prepare(w,g):
 vr=[z[1][:118] for z in D.get(w,{}).get('v',[]) if valid_source(z)];en=[z[1].split('(')[0][:45] for z in D.get(w,{}).get('e',[]) if valid_source(z)];vr=list(dict.fromkeys(vr))[:2]; en=list(dict.fromkeys(en))[:2];return f'{w} → {g} / Đối chiếu: '+(' / '.join(vr[:1]+en))
G={w:v[0] for w,v in pool()[0].items()}
def checkbatch(ws):
 txt='\n'.join(f'{i+1}. '+prepare(w,G[w]) for i,w in enumerate(ws));gr='root ::= '+' "\\n" '.join('"'+str(i)+'|" [XTM O]' for i in range(1,len(ws)+1)).replace('[XTM O]','[XTMO]');res=ask([{'role':'system','content':PS},{'role':'user','content':txt}],max(90,8*len(ws)),seed=2818,grammar=gr);rat={int(m[1]):m[2] for m in re.finditer(r'(?m)^\s*(\d+)\|([XTMO])\s*$',res)};return {w:[rat.get(i+1,'?'),hashlib.sha256(G[w].encode()).hexdigest()[:10]] for i,w in enumerate(ws)}
if __name__=='__main__':
 if sys.argv[1]=='test':
  G.update({'u nang':'Khối bất thường có vỏ bao và chứa dịch.','xâm lăng':'Đưa quân vào chiếm nước khác.','vành khuyên':'Đồ trang sức bằng vàng để đeo tai.','bút chì':'Dụng cụ viết có lõi than chì.','tủ lạnh':'Một mùa có tuyết rơi.','nhãn khoa':'Chuyên ngành nghiên cứu và điều trị mắt.'});print(checkbatch(list(G)[0:0]+['u nang','xâm lăng','vành khuyên','bút chì','tủ lạnh','nhãn khoa']))
 else:
  ws=[w for w in G if w not in MAN]; ws.sort(key=lambda w:hashlib.sha256(w.encode()).digest());run(ws,fn=checkbatch,output='review.jsonl',k=9,threads=24)
