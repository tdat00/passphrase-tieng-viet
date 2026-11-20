from quality import *
from compose import ask,run,combine
G={w:v[0] for w,v in pool()[0].items() if w not in MAN};VER=combine('review.jsonl')
CHECK='''Duyệt MỘT đầu mục cho bảng từ phổ thông Việt Nam. Trả O nếu từ an toàn và lời giải mô tả đúng một nghĩa quen. Trả X nếu cả mục có nghĩa nổi bật chỉ tội phạm, bạo lực, vũ khí, chiến tranh, bệnh tật, ma túy, tình dục, xúc phạm, cái chết hay nội dung chính trị/tôn giáo đặc thù; đừng gán X do một tiếng riêng lẻ hoặc một liên tưởng xa. Trả M nếu giải nghĩa sai, quá vô nghĩa hoặc chỉ là ví dụ. Trả T nếu tên riêng, quá cổ, hẹp nghề hoặc địa phương khó hiểu. Chỉ khi trả X/M/T thì viết thêm lý do ngắn sau dấu |. Thí dụ: cha mẹ = hai người sinh thành hoặc nuôi dạy con: O. Động cơ = máy biến năng lượng thành chuyển động: O. U nang = khối u chứa dịch: X. Bút chì = thiết bị đo nhiệt: M.'''
def single(ws):
 w=ws[0];g=G[w];v=[z[1][:118] for z in D[w]['v'] if valid_source(z)];e=[z[1][:70] for z in D[w]['e'] if valid_source(z)];txt=f'Mục: {w}\nChú giải cần kiểm: {g}\nTham khảo (có thể không đủ hết các nghĩa): '+(' / '.join(v[:2]+e[:2]));res=ask([{'role':'system','content':CHECK},{'role':'user','content':txt}],40,31767,grammar='root ::= "O" | [XMT] "|" [^\\r\\n|]+');k=res.strip()[:1];return {w:[k if k in 'OXMT' else '?',res[2:].strip()]}
if __name__=='__main__':
 ws=[w for w in G if w in VER and VER[w][0] not in ('O','?')];run(ws,fn=single,output='challenge.jsonl',k=1,threads=20)
