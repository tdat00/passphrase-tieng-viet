from pathlib import Path
import hashlib,statistics,math,tarfile,bz2,sys,collections,unicodedata
from final_select import *
fmt=lambda n:f'{n:,}'.replace(',','.');dec=lambda x,n=2:f'{x:.{n}f}'.replace('.',',');repo=Path(__file__).resolve().parents[3]; target='WordListAnalyze-Astra.md'
def check_corpora(sel):
 cc=collections.defaultdict(list)
 for w,(g,_,_) in sel.items():cc[' '.join(texttokens(g))].append(w)
 hits=[]
 def each(lines,src):
  for l in lines:
   k=' '.join(texttokens(l));
   if k in cc:hits.append((src,cc[k]))
 with tarfile.open('mixed.tar.gz','r|gz') as f:
  for m in f:
   if m.name.endswith('-sentences.txt'):each((b.decode('utf8').rstrip('\r\n').partition('\t')[2] for b in f.extractfile(m)),'LCC')
 with bz2.open('tatoeba.bz2','rt',encoding='utf8') as f:each((l.rstrip('\r\n').split('\t')[2] for l in f),'Tatoeba')
 return hits

def audit_sample(sel):
 wr=sorted(sel,key=lambda w:sel[w][2]);out=[]
 for i in range(8):
  chunk=wr[i*len(wr)//8:(i+1)*len(wr)//8];out.extend((i+1,w) for w in sorted(chunk,key=lambda w:hashlib.sha256(('astra-8x20-v1:'+w).encode()).digest())[:20]);
 return out

def build(dry=False):
 sel,good,why,rej,flag,cases,drops,why0=final(dry);n=len(sel);print('good',len(good),'selected',n,'pending',why,flush=True)
 if dry:
  sa=audit_sample(sel);Path('sample.tsv').write_text('\n'.join(f'{i}\t{w}\t{sel[w][0]}' for i,w in sa)+'\n',encoding='utf8');write('sample-log.json',[[i,w,sel[w][0]] for i,w in sa]);return
 assert n==7776;words=sorted(sel,key=order);rows=[w+'|'+sel[w][0] for w in words];dlen=collections.Counter(len(flat(w)) for w in words);dsy=collections.Counter(len(w.split()) for w in words);scores=collections.Counter(sel[w][1] for w in words);rawblock='\n'.join(rows)+'\n';sha=hashlib.sha256(rawblock.encode()).hexdigest();checks=check_corpora(sel);assert not checks,checks
 assert len(set(map(flat,words)))==len(set(words))==n;assert not set(map(flat,words))&keybad;assert all(w in R and nfc(line)==line and line.count('|')==1 and not old(w) for w,line in zip(words,rows));assert all(not (set(alternatives(w))&sel.keys()) for w in words);assert all(not source_overlap(w,sel[w][0])[0] for w in words)
 clean=read('filter-stats.json');prep=read('prep-stats.json');a=len(R);evidence=lambda cond:sum(bool(cond(w)) for w in words);en=evidence(lambda w:R[w]['en']);lef=evidence(lambda w:F.get(w));tat=evidence(lambda w:T.get(w));both=evidence(lambda w:F.get(w) and T.get(w));neither=n-(lef+tat-both);sege=evidence(lambda w:S.get(w) or H.get(w));segmono=evidence(lambda w:' ' not in w and (S.get(w) or H.get(w)));toneq=evidence(lambda w:R[w]['asks']);near=evidence(lambda w:R[w]['near']);median=statistics.median(map(lambda w:len(flat(w)),words));medL=statistics.median(F.get(w,0) for w in words);medT=statistics.median(T.get(w,0) for w in words);av=sum(k*v for k,v in dlen.items())/n;Ent=math.log2(n);hand=scores['biên tập'];filtered=len(pool()[0]);vg=collections.Counter(z[0] for z in REV.values());cg=collections.Counter(z[0] for z in CH.values());safetycuts=len(CUT);raw_core=len(results('draft.jsonl'));raw_res=len(results('reserve.jsonl'));emergency=evidence(lambda w:w not in MAN and w in override and REV.get(w,['?'])[0]!='O');no_grade=evidence(lambda w:w not in MAN and REV.get(w,['?'])[0]!='O' and CH.get(w,['?'])[0]!='O');assert no_grade==0
 dups=collections.Counter(g.rstrip('.').casefold() for g,_,_ in sel.values());shared=sum(v-1 for v in dups.values() if v>1);e5_non=[max(E[w]) for w in words if w not in MAN];audit=read('sample-log.json');edits={l.split('|')[0] for l in infile('audit-fixes.tsv')};audit_fix=sum(w in edits or w not in sel for _,w,g in audit);cross=evidence(lambda w:w not in MAN and REV[w][0]!='O' and CH.get(w,['?'])[0]=='O');
 body=f'''# Danh sách passphrase tiếng Việt — phương án Astra

**Bản đề xuất độc lập, 19-11-2026.** Đúng **{fmt(n)}** đầu mục và **{fmt(n)}** khóa không dấu, viết liền. Đây là dữ liệu để thảo luận, không thay danh sách đang chạy trong ứng dụng. Tôi chỉ dùng README của dự án, không dùng danh sách hay tiêu chí biên tập của phương án khác.

## 1. Kết quả

| Chỉ số | Giá trị |
|---|---:|
| Một âm tiết (quy ước “từ đơn” trong báo cáo) | {fmt(dsy[1])} |
| Hai âm tiết | {fmt(dsy[2])} |
| Ba âm tiết | {fmt(dsy[3])} |
| Bốn âm tiết | {fmt(dsy[4])} |
| Tổng mục nhiều âm tiết (gọi gọn là “ghép”) | {fmt(n-dsy[1])} |
| Độ dài viết liền: nhỏ nhất / trung vị / lớn nhất | {min(dlen)} / {dec(median,0)} / {max(dlen)} chữ cái |
| Độ dài trung bình | {dec(av)} chữ cái |
| Mục ba chữ cái bổ sung | 0 |

“Ghép” ở đây là cách đếm theo dấu cách cho ứng dụng, **không** khẳng định mọi mục đều là từ ghép về mặt ngữ pháp: có cả từ láy, tổ hợp cố định và một số quán ngữ có mục từ riêng. Số chữ cái không tính dấu cách; `ươ` là hai chữ cái, còn `ế` là một. Phân bố độ dài:

| Chữ cái | {' | '.join(str(k) for k in sorted(dlen))} |
|---|{'|'.join('---:' for _ in dlen)}|
| Số mục | {' | '.join(fmt(dlen[k]) for k in sorted(dlen))} |

**Entropy của lượt chọn:** `log₂(7776) = 5 × log₂(6) ≈ {dec(Ent,5)}` bit/mục. Bốn, sáu và tám lượt chọn độc lập có hoàn lại cho {dec(4*Ent,2)}, {dec(6*Ent,2)} và {dec(8*Ent,2)} bit. Với 6 mục, thêm một chữ số ngẫu nhiên vào một vị trí từ ngẫu nhiên cộng `log₂(60)` bit, tổng khoảng {dec(6*Ent+math.log2(60),2)} bit nếu đầu ra phân biệt được. **Tần suất chỉ để chọn danh sách, tuyệt đối không dùng làm trọng số khi sinh passphrase.** Chữ hoa đầu mục và dấu phân cách cố định không tăng entropy. Khóa không dấu duy nhất bảo toàn số lựa chọn cho *một* mục; không có dấu phân cách, hoặc dùng cùng dấu ở giữa âm tiết và giữa mục, nhiều dãy có thể hiện thành một chuỗi. Muốn giữ rõ biên, dùng chẳng hạn `_` giữa mục và để tắt phân cách nội bộ.

## 2. Tiêu chí theo thứ tự áp dụng

1. **Đầu mục thật và hình thức hợp lệ.** Cần mục tiếng Việt trong ấn bản Wiktionary tiếng Việt, một nghĩa từ vựng và từ loại dùng được; không lấy tên riêng, chữ viết tắt, hình vị rời, tục ngữ dài hoặc chuỗi do ghép tùy ý. Không hạ chữ hoa của tiêu đề để biến tên riêng thành từ thường. Chấp nhận mục dẫn chiếu trong nhóm đồ vật quen nếu ấn bản thứ hai xác nhận nghĩa độc lập (chẳng hạn *công tắc*). Chỉ dùng chữ cái Việt viết thường ở NFC, một dấu cách ASCII giữa các âm tiết, không số, dấu nối, dấu câu, khoảng trắng đầu/cuối hay khoảng trắng kép. *Thiên nga* trong nghĩa loài chim khác với việc dùng làm tên người.
2. **Không khiến người dùng phải nhập lại một từ dễ gây khó chịu.** Loại nghĩa thường gặp về bạo lực, vũ khí, chiến sự, tội phạm, tang ma, bệnh và triệu chứng, ma túy, tình dục, xúc phạm; tránh thuật ngữ chính trị, tín ngưỡng đặc thù, định kiến và các chủ đề nhạy cảm khác. Rà cả tên từ, nhãn từ điển, nghĩa thông dụng khác và lời giải mới. Loại khóa toàn mục nếu nó trùng khóa của tiếng thô tục: so **cả chuỗi**, không dò mù quáng một đoạn con như `cu` trong mọi từ. Cơ thể, thực phẩm và sinh hoạt bình thường không mặc nhiên nhạy cảm; *vú sữa* chỉ quả khi xét nguyên cụm. Với từ nhiều nghĩa, một nghĩa tục hoặc bạo lực nổi bật vẫn đủ để bỏ; không “làm sạch” nó bằng cách cố tình chọn một nghĩa xa lạ.
3. **Ổn định khi gõ.** Loại vần mở `oa/oe/uy` có thanh gây hai vị trí dấu, thí dụ *hòa/hoà, khỏe/khoẻ, thủy/thuỷ*; không loại vô cớ một tiếng thanh ngang như *hoa*. `qu` là một trường hợp chữ viết khác, không mặc nhiên xem mọi `quy` là tranh chấp vị trí thanh; các dạng *qui/quy, quí/quý* được chặn riêng vì biến thể `i/y`. Chặn các nhóm đã biết như *lý/lí, kỹ/kĩ, mỹ/mĩ, sĩ/sỹ, giày/giầy*, thêm các cặp soát tay như *dãn/giãn* trong cùng từ, *hủ tiếu/hủ tíu, mồng tơi/mùng tơi* và các mục có cạnh tranh *mì/mỳ*. Tách lỗi hay mắc khỏi biến thể được thừa nhận: ghi một cặp để tránh không có nghĩa cả hai đều chuẩn.
4. **Ít nhất bốn chữ cái sau khi viết liền.** Chỉ cân nhắc ba chữ nếu hết ứng viên tốt từ bốn chữ; ở lần này **không cần**. Tôi bổ sung trần mềm về công gõ rồi áp dụng thành giới hạn 16 chữ và bốn âm tiết cho bộ đề xuất. Ưu tiên sinh hoạt, đồ vật, cây con, động tác, tính chất nhận biết được và kiến thức phổ thông. Vẫn giữ đủ từ trừu tượng thông dụng; dễ hình dung là tiêu chí ưu tiên, không phải lệnh loại mọi khái niệm. Không chọn chữ khó chỉ vì có trong từ điển.
5. **Độ quen và rủi ro vùng miền.** Hai kho câu độc lập, số lần nhận ra được trong cách tách dài nhất, một từ điển đối chiếu, và rà nội dung giúp chống thiên lệch tần suất báo chí. Kiểm tra hỏi/ngã, `s/x`, `ch/tr`, `d/gi/r`, `l/n`, cuối `-c/-t`, `-n/-ng`: giảm điểm nếu thay một chỗ tạo được một mục khác có căn cứ. Mục hỏi/ngã không bị cấm toàn bộ; có {fmt(toneq)} mục chứa ít nhất một trong hai thanh. **Bổ sung:** khi hai mục đủ chuẩn chỉ khác đúng một phép đổi khu vực đã định, chỉ lấy một trong hai, không mặc định cách phát âm của miền nào là sai. Vẫn có {fmt(near)} mục có láng giềng được chứng thực trong từ điển/kho câu dù mục kia không được chọn. Đây là quy tắc gần đúng về chính tả, không phải mô hình phát âm mọi phương ngữ.
6. **Một khóa chỉ chọn một nghĩa dễ nhớ.** Dùng chính `s.normalize("NFD").replace(/\\p{{M}}/gu, "").replace(/đ/g, "d").replace(/Đ/g, "D")`, sau đó xóa dấu cách. Ưu tiên mục đã xác nhận là quen, cụ thể và có nghĩa đứng độc lập trước khi so điểm. Ví dụ *diều/điều* đều ra `dieu`: giữ đồ chơi đón gió; *nội thất/nói thật* đều ra `noithat`: không thể giữ cả hai. Các nghĩa khác nhau của **cùng một cách viết** không được nhân lên thành nhiều vé. Mục ghép được lưu có dấu cách, như *cà phê*; app mới biến thành `càphê` hoặc `cà_phê`, chỉ viết hoa đầu mục, nối số ở cuối cả mục.
7. **Lời giải phải giúp nhận từ.** Chọn một nghĩa thông dụng thay vì liệt kê rất nhiều nghĩa. Ưu tiên dấu hiệu nhận biết, hoạt động hoặc công dụng; loại lời chỉ dẫn “xem mục…”, định nghĩa vòng, câu ví dụ giả làm định nghĩa, nhầm từ loại làm sai nghĩa, hay bản quá giống nguồn. Mỗi lời giải là một dòng tiếng Việt; không chứa ký tự phân cột. Không coi một mô hình tự động là bằng chứng cuối cùng về nghĩa.

## 3. Nguồn và quy trình có thể đối chiếu

| Nguồn | Cách dùng và quyền |
|---|---|
| [Wiktionary tiếng Việt qua Kaikki/Wiktextract](https://kaikki.org/viwiktionary/rawdata.html) | Nguồn đầu mục, từ loại, nghĩa, nhãn và mục chuyển hướng. Bản dump 02-10-2026, trích 03-11-2026. Ghi công cộng đồng Wiktionary và Tatu Ylönen, [Wiktextract (LREC 2022)](https://aclanthology.org/2022.lrec-1.140/). Nội dung theo [điều khoản Wikimedia §7](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use/en#7._Licensing_of_Content), chủ yếu CC BY-SA 4.0, có nội dung đồng cấp GFDL và ngoại lệ tại từng trang. |
| [Mục tiếng Việt trong Wiktionary tiếng Anh, Kaikki](https://kaikki.org/dictionary/Vietnamese/) | Bản enwiktionary 01-10-2026, trích 30-10-2026; đối chiếu nghĩa, tối nghĩa, từ loại và nhãn. Cùng chế độ quyền Wikimedia; hai ấn bản là hai tập chứng cứ, **không** giả định hai ban biên tập độc lập tuyệt đối. |
| [Leipzig Corpora Collection, Vietnamese Mixed 2014, mẫu 300K](https://downloads.wortschatz-leipzig.de/corpora/vie_mixed_2014_300K.tar.gz) | {fmt(prep['sentences'])} câu, chỉ đếm số câu có chuỗi, không trích câu. [Điều khoản Leipzig](https://wortschatz.uni-leipzig.de/en/usage) ghi riêng **CC BY** cho gói văn bản tải xuống; không suy giấy phép từ điều khoản áp dụng cho giao diện tra cứu. |
| [Tatoeba, xuất câu tiếng Việt](https://downloads.tatoeba.org/exports/per_language/vie/vie_sentences.tsv.bz2) | 33.328 câu ở ảnh chụp tải 19-11-2026. Ghi công những người đóng góp Tatoeba; [điều khoản §6](https://tatoeba.org/en/terms_of_use): mặc định CC BY 2.0 FR, một số câu có thể là CC0. Chỉ dùng số đếm; không phát hành lại câu hay bản dịch. |
| Công cụ cục bộ | Qwen Team, [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B), bản [GGUF Q4_K_M của Unsloth](https://huggingface.co/unsloth/Qwen3.5-9B-GGUF/tree/3885219b6810b007914f3a7950a8d1b469d598a5) — Apache-2.0; [llama.cpp b12530](https://github.com/ggml-org/llama.cpp/releases/tag/b12530) — MIT. [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small/tree/614241f622f53c4eeff9890bdc4f31cfecc418b3) — MIT, đối chiếu nghĩa trên CPU. Không gọi API sinh văn bản bên ngoài, không thêm thư viện cho ứng dụng. |

Bảng dưới là bản tuyển và viết lời giải mới, không phải bản sao từ điển hay bản trích kho câu. Khi tái phân phối bảng, giữ ghi công trên và điều kiện [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) cho bảng; không thay đổi giấy phép của ứng dụng hoặc của các nguồn. Có thể tra lịch sử một đầu mục tại `vi.wiktionary.org/wiki/<đầu_mục>` hoặc `en.wiktionary.org/wiki/<đầu_mục>`.

**Dấu vân tay của các tệp đầu vào (SHA-256):**

| Tệp | SHA-256 |
|---|---|
| Kaikki tiếng Việt, JSONL gzip | `1f0abd21982660b5fc2eff5eb3fbacbed2d9fe8f476af794dbed0d927ffb8187` |
| Kaikki tiếng Anh, JSONL riêng cho tiếng Việt | `186cd0a62d876dada70c9761bc05e598c8cf7b9a48e0aa518bab6c649e28d945` |
| Leipzig 300K, tar.gz | `067c18ff6e719fea866314836c19d4d1ae4b597c4b5207435131cbb5de32c57e` |
| Tatoeba tiếng Việt, bzip2 | `e9a6451c46c43d9e15b923945325e74c8f28a8bc8e2e9c864801942337dbcb1a` |

1. **Nhập và kiểm hình thức.** Bản Việt có {fmt(prep['v entries'])} bản ghi tiếng Việt cho {fmt(prep['v headwords'])} tiêu đề phân biệt sau NFC; bản Anh có {fmt(prep['e entries'])} bản ghi, {fmt(prep['e headwords'])} tiêu đề. Từ bản Việt, {fmt(prep['lowercase-vi-1-4'])} tiêu đề là chữ thường Việt, một đến bốn nhóm chữ. Bước lọc kế tiếp ghi nguyên nhân đầu tiên: độ dài {fmt(clean['dài'])}; cấu trúc âm tiết {fmt(clean['âm tiết'])}; biến thể {fmt(clean['biến thể'])}; thiếu từ loại/nghĩa đủ dùng {fmt(clean['từ điển'])}; bề mặt hoặc khóa nhạy cảm {fmt(clean['từ nhạy cảm'])}; nhãn/nội dung nghĩa nhạy cảm {fmt(clean['nghĩa nhạy cảm'])}; thiếu chứng liệu {fmt(clean['chứng liệu'])}. Còn **{fmt(a)}** ứng viên, ứng với {fmt(len(set(map(flat,R))))} khóa. Không coi mọi dòng trùng tiêu đề với tên người là tên riêng nếu có nghĩa danh từ chung thật sự.
2. **Đo độ thông dụng.** Hạ chữ để đếm nhưng giữ nguyên chữ đã kiểm cho đầu mục. Tìm chuỗi âm tiết liên tiếp, không qua dấu câu; trong mỗi câu chỉ cộng một lần. Đếm thêm một lần theo phép tách tham lam: ở từng vị trí ưu tiên mục từ dài nhất; phân biệt một tiếng thường dùng riêng với một yếu tố chỉ hay nằm trong từ dài. Độ phủ của **bảng cuối**: {fmt(lef)} mục có mặt trong Leipzig, {fmt(tat)} trong Tatoeba, {fmt(both)} có mặt ở cả hai, {fmt(neither)} ở ngoài cả hai ({', '.join('*'+w+'*' for w in words if not F.get(w) and not T.get(w)) or 'không có'}); {fmt(sege)} xuất hiện ít nhất một lần theo phép tách dài nhất (trong đó {fmt(segmono)} mục đơn âm). Trung vị số câu chứa một mục là {dec(medL,0)} ở Leipzig và {dec(medT,0)} ở Tatoeba. {fmt(en)} đầu mục còn có nghĩa đạt bộ lọc ở ấn bản tiếng Anh. Ngoài nhóm duyệt tay, phải có ít nhất một câu Tatoeba, hoặc ít nhất hai câu Leipzig và một lần được tách thành mục ở Leipzig.
3. **Xếp hạng trước biên tập.** Gọi `L` và `T` là hai số câu, `p` là dấu hiệu vật thể trong nghĩa danh từ, `a` là vật/hoạt động quen do tôi chọn trước, `e` là chứng cứ nghĩa ở ấn bản Anh, `n` là có nghĩa danh từ, `h` là có láng giềng vùng miền có chứng cứ, `q` là có hỏi/ngã, `s` là số âm tiết, `d` là số chữ. Điểm đầu: `log₂(1+L) + 1,55 log₂(1+min(T,50)) + 1,9e + 2,6p + 0,4n + 3a − [s=1] − 0,25max(s−2,0) − 0,18max(d−10,0) − 0,65h − 0,32q`. Chặn ảnh hưởng một từ lặp trong ngữ liệu dịch; thưởng ngôn ngữ đời thường nhưng không lấy số liệu làm chứng cứ duy nhất. Trước khi loại va chạm, cộng tiếp `0,42 log₂(1+L_tách) + 0,53 log₂(1+min(T_tách,24)) + 2p + 0,9[A] + 0,55[s≥2 và T>0] + 0,7[L>0 và T>0]`. Ưu tiên nhóm biên tập đã xác nhận trước nhóm chấm tự động; hòa điểm thì theo thứ tự chữ Việt. Các hệ số là quyết định biên tập công khai, không phải hằng số ngôn ngữ học.
4. **Viết nghĩa, rà chủ đề.** Tôi viết trực tiếp các mục đơn âm được cân nhắc, nhiều đồ vật/sinh hoạt và những ca cần sửa. Với mục nhiều âm tiết, công cụ soạn bản nháp riêng trong máy từ dữ kiện của **chính** mục đó rồi chấm A (đời thường), B (phổ thông), C (hẹp), X (không dùng). Đã soạn thử {fmt(raw_core)} ứng viên chính và {fmt(raw_res)} ứng viên dự trữ có bằng chứng; giữ A/B hoặc viết lại độc lập sau khi rà. Nhãn máy không phải chân lý: ví dụ *bút chì* không nhất thiết có cục tẩy, *vành khuyên* ở đây là chim chứ không phải khuyên tai. Bộ cờ soạn tay còn được mở rộng khi gặp nhãn thiếu, như *u nang* hay *lô cốt*. Bảng cuối có **{fmt(hand)}** nghĩa biên tập trực tiếp và **{fmt(n-hand)}** nghĩa từ bản nháp đã qua các cửa kiểm.
5. **Xét ngược và kiểm giống văn.** Loại lời giải khớp nguyên một nghĩa nguồn, chứa một chuỗi khớp ít nhất sáu tiếng với nghĩa cùng mục, chép trọn một đoạn nghĩa ngắn theo ngưỡng, hoặc có tỉ số khớp dãy từ ≥ 0,78 với một nghĩa nguồn (từ năm tiếng trở lên). Tính tương đồng E5 với các nghĩa Việt và Anh; dùng điểm thấp để tìm lỗi, chặn bản nháp có điểm tốt nhất dưới 0,84 nếu chưa duyệt đích danh. Đây là ngưỡng rà soát cục bộ, không phải xác suất lời giải đúng; không coi điểm cao là chứng minh đúng. Soát lại bản nháp bằng lượt đọc tách biệt; nếu bị gắn cờ, xét lại **từng mục**, không đưa kết luận cũ vào đề. Với nghĩa không do tôi viết trực tiếp, chỉ nhận kết quả qua kiểm hoặc quyết định thủ công có lưu vết. Đã có {fmt(len(REV))} lượt kiểm mục riêng biệt trong phép kiểm thứ nhất và {fmt(len(CH))} mục được hỏi lại riêng; {fmt(cross)} mục trong bảng được chấp nhận ở lần xét lại. Tất cả {fmt(emergency)} mục còn bất đồng ở lượt đầu chỉ được giữ sau khi tôi đọc đích danh cả từ và nghĩa; không hạ chuẩn hình thức hay an toàn. Sau các cửa này còn {fmt(len(good))} ứng viên, trước khi chốt đúng {fmt(n)}. Trong đoạn xếp đã duyệt đến vạch chốt, bỏ thêm {fmt(rej['khóa'])} do khóa trùng và {fmt(rej['cặp vùng'])} do cặp dễ nghe lẫn. Không dùng ba chữ để bù.

**Tái lập.** Tệp đầu vào, sổ quyết định và mã được giữ ngoài repo trong thư mục phiên `files\\astra` đã chỉ định. `prepare.py`, `speech_count.py`, `segment.py`, `select_words.py` lập mục từ và số đếm; `compose.py`, `judge.py`, `challenge.py`, `semantic.py` là các bước soạn/đối chiếu; `quality.py`, `final_select.py`, `publish.py`, `verify.mjs` kiểm, chọn và xuất. Trong PowerShell, chạy `.\\replay.ps1` từ thư mục đó để dùng đúng bản nháp và quyết định đã lưu, tái tạo tài liệu rồi kiểm bằng Node, không cần mạng, GPU hoặc cài thư viện. Nếu thay mô hình hoặc soạn lại từ đầu, từ ngữ của bản nháp có thể khác dù đặt cùng hạt giống.

## 4. Kiểm tra, hạn chế và chỗ cần phản biện

- **Kiểm máy trên thành phẩm, không chỉ trên nguồn.** Python đối chiếu đầu mục, NFC toàn dòng, số lượng, ký tự, khóa, các cặp vùng đã định và độ giống nguồn. Trình kiểm Node đọc ngược đúng khối bên dưới, chạy nguyên regex của app, kiểm lại khóa sau viết hoa, giới hạn độ dài, dấu cách, số cột và thứ tự bằng một bộ so độc lập. Không lời giải nào trùng nguyên lời giải tiếng Việt trong tập từ điển đã lập chỉ mục; không lời giải nào là nguyên một câu trong hai mẫu kho câu khi quy về từ thường và bỏ dấu câu. Một số thuật ngữ đồng nghĩa có thể chia sẻ những cụm từ ngắn hiển nhiên. SHA-256 của **các dòng dữ liệu UTF-8, LF, có một LF cuối**, không gồm hàng rào Markdown: `{sha}`.
- **Đọc mẫu và đọc theo rủi ro.** Ngoài các nghĩa tự biên tập và các cụm bị gắn cờ, tôi đọc mẫu {len(audit)} dòng của bản gần chốt: 20 dòng ở mỗi một phần tám dải điểm, lấy thứ tự băm cố định `astra-8x20-v1:` + từ; sửa hoặc không giữ {audit_fix} mục trong mẫu đó. Tôi cũng đọc các trường hợp điểm nghĩa thấp, kiểm tra cách dùng có thật và rà các nhóm về chiến sự, sức khỏe, tôn giáo, bộ máy chính trị, chính tả. Đây là **đánh giá biên tập có lấy mẫu**, không phải số đo lỗi toàn danh sách hoặc khảo sát người dân. Cả hai lượt đọc máy dùng cùng mô hình nên có thể lặp lại cùng một lỗi.
- **Giới hạn nguồn.** Wiktionary có thể thiếu mục rất quen, lẫn nghĩa cổ/địa phương với nghĩa chính, hoặc chỉ trỏ sang mục khác. Leipzig thiên về văn viết, có tư liệu cũ; Tatoeba nhỏ hơn, chịu ảnh hưởng câu dịch. Chuỗi đứng cạnh nhau không bảo đảm người nói coi đó là một từ, còn tách dài nhất đôi lúc nuốt mất mục con. Không đánh đồng “không thấy” với “không ai dùng”. Bảng không bảo đảm mọi người ở mọi vùng đều quen như nhau. Danh mục tục/nghĩa bóng cũng không thể bao hết tiếng lóng đang đổi.
- **Khi nhập mật khẩu:** NFC lưu trong tài liệu không buộc bộ gõ tạo cùng dãy byte. Hãy thử bộ gõ ở chế độ Unicode dựng sẵn và thử ngay trong ô mật khẩu trên thiết bị thật; một số ô tắt IME. Khi lưu trong trình quản lý mật khẩu, ưu tiên dán/tự điền đúng chuỗi đã chọn. Chữ hoa đầu một từ ghép áp dụng một lần (*Càphê*, không phải *CàPhê*); bản có dấu và bản bỏ dấu là hai mật khẩu khác nhau, không phải hai cách đăng nhập thay thế.
- **Đề nghị thảo luận:** (i) bỏ cả cặp vùng hay chỉ trừ điểm khi cụm đủ ngữ cảnh; (ii) phạm vi loại nghĩa phụ nhạy cảm, nhất là khi cả cụm là đồ ăn/cây cối vô hại; (iii) giữ bao nhiêu thuật ngữ phổ thông và từ láy khi phải đủ 7.776 mục; (iv) thử đọc–gõ lại với người ở Bắc, Trung, Nam và nhiều lứa tuổi, ưu tiên các mục chỉ có tín hiệu ở một kho. Nếu chuyển sang app, cần thống nhất hai bản nhúng như README §5; báo cáo này **không** sửa chúng.

## 5. Danh sách đầy đủ

Thứ tự: so từng **âm tiết** từ trái sang phải. Trong một âm tiết, so dãy chữ chưa mang thanh theo `a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y`; giữ nguyên phân biệt `ă/â`, `ô/ơ`, `u/ư`, `d/đ`. Nếu phần chữ bằng nhau, so thanh ngang, huyền, hỏi, ngã, sắc, nặng rồi mới sang âm tiết kế; tiền tố ngắn đứng trước. `ch`, `ng`, `ngh`, `ph`… là dãy chữ, không phải chữ cái riêng. Quy tắc này không phụ thuộc phiên bản sắp xếp ICU hay thứ tự mã Unicode.

```text
'''+rawblock+'```\n'
 assert nfc(body)==body;write('final-rows.json',sel);write('final-metrics.json',dict(N=n,syll=dsy,length=dlen,sha=sha,manual=hand,L=lef,T=tat,both=both,neither=neither,e5_min=min(e5_non),shared=shared,review=len(REV),challenge=len(CH),good=len(good),why=dict(why),duplicates=dict(rej),sample_changes=audit_fix));
 import os
 os.chdir(repo);Path(target).write_text(body,encoding='utf8',newline='\n');print(repo/target,sha,flush=True)
if __name__=='__main__':build('--sample' in sys.argv)
