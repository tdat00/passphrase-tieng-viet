"""Đối phiếu Opus đã ký với phiếu Astra và các đổi ý có lý do; ky(Y/N) chỉ ký K2 của Astra."""
import csv
import hashlib
import io
import re
import unicodedata as ud
from collections import Counter
from pathlib import Path

E=Path(__file__).resolve().parent
A=E.parent
AT=E.parents[3]
O=AT/"ho-so"/"opus"/"ra-thay-chinh"
U=AT/"ho-so"/"unified"


def read(p):
    with p.open(encoding="utf-8-sig",newline="") as fh:
        return [dict(row,n=i) for i,row in enumerate(csv.DictReader(fh,delimiter="\t"),2)]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fold(w):
    return "".join(c for c in ud.normalize("NFD",w.lower()) if not ud.combining(c) and not c.isspace()).replace("đ","d")


def span(rs):
    ns=sorted({r["n"] for r in rs})
    if not ns:return "-"
    return str(ns[0]) if len(ns)==1 else f"{ns[0]}–{ns[-1]}" if ns==list(range(ns[0],ns[-1]+1)) else ",".join(map(str,ns))


CHANGES = {
    ("tutap","tu tập"): ("GIU_PHAN_DOI_K1", "TRINH_CHU: Giữ tụ tập dù có cách đọc tu tập (K2), hay thay tụ tập bằng HM đã viết còn dùng được kế tiếp trong hàng đợi?",
        "Mẫu web có hành trì giáo pháp thật (ID 1681414, 5906650, 885718); 0/171 sạch, 0,571 PPM. Không đòi phải là tang lễ hay đặt ngưỡng r=0,035. Opus giữ K2, Astra giữ K1. Bốn chỗ đã chốt dùng cửu chương trước rồi ba HM; theo thứ tự hiện có, HM cho chỗ thứ năm là cô giáo nếu vẫn khả dụng."),
    ("tute","tư tế"): ("K1 → K2", "GIU_K2",
        "Astra nhận K2: nghĩa tôn giáo là thật nhưng đây là danh xưng chuyên biệt. Nhiều mẫu phụ đề là tước vị trong phim dịch; mẫu web gắn với kinh sách, chức vụ và cổ sử. Cùng lý do về phạm vi như ma sơ; không suy tỷ lệ nghĩa từ 110/34 lượt. Gộp cả tư tế và tứ tế vào phạm vi ký cho tute."),
    ("cuong","cương"): ("CHỜ K0 → K2", "GIU_K2",
        "Astra không phủ nhận nghĩa sinh lý dùng độc lập (phụ đề 3570902); EN:15144 không đánh dấu tục. Một lượt đúng nghĩa và số của các tổ hợp dài hơn chưa chứng minh nghĩa phụ người lớn còn phổ biến như trường hợp chim/bướm. Ký mở rộng cho cương bên cạnh cuồng/cưỡng."),
    ("long","lồng"): ("CHỜ K0 → K2", "GIU_K2",
        "EN:25441 xác nhận có cách viết lóng theo phát âm; không coi đó là không có nguồn. Mẫu phụ đề sạch chủ yếu nói vật đựng/động tác, chưa chứng minh nghĩa phụ tục phổ biến của đúng lồng; không dùng số gộp của các nghĩa lành."),
    ("duoi","đượi"): ("KHÔNG ĐỎ → K2", "GIU_K2",
        "VI:273441 (viwiki rev 2010218) ghi dạng nói chệch dùng chê người, không gắn nhãn tục hay xác định người bán dâm; tiêu đề Tục ngữ không phải nhãn tục. 5/7 dòng phụ đề sạch khác nhau là lời xúc phạm, nên rút nhận định không đỏ nhưng không đồng ý gọi phần lớn lượt là lỗi gõ. Chấp nhận K2, không đề nghị K0."),
    ("songngu","song ngư"): ("KHÔNG ĐỎ → K2", "GIU_K2",
        "Song Ngư là tên chòm sao/cung hoàng đạo; thiên văn không tự là bói toán nhưng cách dùng chiêm tinh có thật. Ký đúng cả dạng viết hoa và thường."),
    ("tung","tửng"): ("KHÔNG ĐỎ → K2", "GIU_K2",
        "Có thể là lời trêu về hành vi khác thường, không tự là bệnh; nhiều lượt của tổ hợp tưng tửng. Nhận K2 cho cách đọc này và mở rộng phạm vi chữ ký sẵn có của tung."),
    ("manman","man man"): ("KHÔNG ĐỎ → K2", "GIU_K2",
        "Mục Việt có sắc thái khẩu ngữ về trạng thái hơi bất thường; lượt mặt chữ lẫn tiếng Anh. Còi tương đối buộc đọc, không xác lập tỷ lệ nghĩa đỏ."),
    ("lieu","liêu"): ("KHÔNG ĐỎ → K2", "GIU_K2",
        "Liêu còn là tên/dòng họ, có trong nhiều tổ hợp không nêu triều đại. Ký vì tách được trường hợp lịch sử nhưng không coi mọi lượt liêu là nghĩa H6.3."),
    ("congcong","công công"): ("KHONG_DO", "GIU_KHONG_DO",
        "Đây là xưng danh/chức trong văn cảnh cung đình hoặc họ hàng; thân phận một người không tự là hành vi tình dục, thủ thuật hay thực thi quyền lực. Không cần ký K2."),
}
SPECIAL_K2 = {
    ("bang","băng"):"Thay hai phiếu hiệu lực chứ không ghi bốn phiếu: phạm vi cho bảng phải chứa cả báng và băng, gồm ngữ cảnh đạn/băng đảng đã xét ở hai dòng cũ.",
    ("banthan","bán thần"):"Hai SA ký bổ sung cho bán thần, có cả nghĩa nhân vật truyện; không thay hoặc thu hẹp phạm vi bán thân theo D-rtc-7.",
    ("daihan","đại hãn"):"Tước hiệu lịch sử là nghĩa thật nhưng có phạm vi hẹp; không dùng tần suất hạ chữ làm số nghĩa chức tước. Giữ cả đối chứng đại hạn cũ trong phiếu mới.",
    ("chapnhat","chấp nhất"):"Có thể tả sự cố chấp; sắc thái phê bình phụ thuộc ngữ cảnh, không tự là lời rủa. Còi tương đối 6/0 so với mục 5/0 đủ để đọc, không phải K1; hai SA đã ký K2.",
    ("chungtu","chủng tử"):"Có nghĩa triết học nhà Phật bên cạnh nghĩa hạt giống; không đánh đồng mọi lượt thành tôn giáo. Ghi K2 có đủ hai chữ ký thay vì buộc loại hoặc bỏ sót đối chứng.",
    ("hongchuyen","hồng chuyên"):"Thuật ngữ chính trị lịch sử 0/2, dưới hai mốc, đã đọc và Opus ký cùng Astra. Không mặc định mọi thuật ngữ dưới còi đều phải trình chủ.",
    ("thoai","thoái"):"Có danh từ thuật ngữ cho đòn võ nhưng còn nhiều nghĩa lành và tổ hợp dài. Đã đọc cả xét bạo lực, ủng hộ giữ K2.",
    ("tute","tứ tế"):"Cách dùng văn sử cổ khác tư tế; toàn cụm rất hiếm. Ký cả hai đối chứng của tute, không tạo hai cặp chữ ký đang hiệu lực cho cùng khóa.",
}
NON_H7={
    "buonthiu":("THAY_H5c","THAY_H5c: rút buồn thiu khỏi tập vào và đăng ký họ.","VI:272859 trỏ trực tiếp sang buồn thiu; phụ đề 9/0 (bỏ trùng 7/0), web 0/0. Cùng khóa ASCII không miễn H5c; không chặn khóa H7. Với cả bốn vị trí cần bù: cửu chương rồi HM đủ điều kiện theo hạng, lần lượt ngân hàng, biển, côn trùng trên bảng hiện có. Tôn trọng bàn giao một dự bị + tối đa 23 HM, F ≤ 77; không dùng khách hàng hoặc cấp thêm ghế."),
    "iuxiu":("THAY_H5c","THAY_H5c: rút ỉu xìu khỏi tập vào và đăng ký họ.","VI:111007 và Việt–Việt 30K:8288 dẫn ỉu xịu về ỉu xìu; phụ đề 6/0 (bỏ trùng 5/0), web 1/0. Hai kho đều dưới 20; không chặn khóa H7."),
    "daingoang":("CHỜ QUAN HỆ → KHÁC TỪ","GIU_KHONG_LAP_HO","VI:270194 mô tả riêng nét vướng víu, không dẫn chiếu cách viết; cùng mức nhấn về độ dài không đủ lập họ c. Không áp tỷ lệ của hai mục khác nhau."),
    "lubu":("CHỜ QUAN HỆ → KHÔNG LẬP HỌ","GIU_KHONG_LAP_HO","Lu bu có cách dùng tính từ về bận việc; lu bù còn nhấn mức độ/cường độ kéo dài. Với lù bù cũng chưa có chứng cứ hai cách viết cạnh tranh của cùng từ; không tự lập họ chỉ do gần âm, gần nghĩa."),
    "thay":("SUA_KY","SUA_CHU_KY_THAY","Giữ hiệu lực dòng 2152 và 2153, chuyển dòng Opus lặp 2154 thành THAY_THE. Kiểm mọi khóa K2 trong chính có đúng một dòng CO mỗi SA; không thay từ thầy."),
    "WordListAnalyze.md:9101":("SUA_MO_TA_K0","SUA_TAI_LIEU","Bổ sung đủ ba trường hợp: tục, tình dục người lớn hoặc chỉ chất thải; quy tắc nghĩa phụ phổ biến vẫn riêng. Ngoài hợp cặp, Astra không duy trì phản đối K0 cho rùng mình, tâm hồn, vắt sữa: chưa xác lập nghĩa phụ phổ biến của chính từ tiếng Việt; không mở lại quyết định chào cờ."),
    "WordListAnalyze.md:9124":("SUA_SO_NHAN","SUA_TAI_LIEU","Trên mốc so sánh d78e97a: 238 khóa thuộc gói ký, 237 nhãn K2 thêm mới vì bảng đã có K2. Khi thi hành T9 phải tính lại trên đúng dữ liệu và đừng lẫn số khóa với số dòng ký."),
}


def main():
    peer=read(O/"t9-doi-dap.tsv")
    peer_set={(r["khoa"],r["tu_chinh"],r["cach_doc"]) for r in peer}
    old=[r for r in read(A/"t9-soat-toan-tap.tsv") if r["trang_thai"]=="CHO_DOI_DAP"]
    aa={(r["khoa"],r["tu"],r["doi_chung"]):r for r in old}
    assert aa.keys()<=peer_set and len(aa)==63
    own_raw=read(E/"t9-doi-so-cap.tsv");scored=read(E/"t9-phan-xu-tung-cap.tsv")
    byid={r["id"]:r for r in scored}
    h={(r["khoa"],r["mat_chu_sha256"]):r for r in own_raw}
    old_op=read(O/"evidence"/"t9-phan-quyet.tsv")
    oc={(fold(r["tu"]),r["doc_khac"].casefold()):r for r in old_op}
    o14={(fold(r["tu"]),r["doc_khac"].casefold()) for r in old_op if r["phan_quyet"]=="K2_DE_XUAT" or r["tu"]=="công cộng"}
    p2=read(E/"t9dd-mau-sub.tsv"); w2=read(E/"t9dd-mau-web.tsv")
    wit=read(E/"t9-nguon-cac-ca.tsv")
    h7_keys={r["khoa"] for r in old}|{k for k,_ in o14}
    expectedpairs={(r["khoa"],r["doi_chung"].casefold()) for r in old}|o14
    queue=sorted((r for r in read(U/"ra-thay-chinh-thay-the.tsv") if r["vai_tro"]=="HM"),key=lambda r:int(r["thu_tu"]))
    accepted={r["tu"]:r for r in read(U/"ra-thay-chinh-giai-nghia-dat.tsv")}
    available=[r["tu"] for r in queue if accepted.get(r["tu"],{}).get("ket_luan")=="HM_CHUA_DUNG"]
    assert available[:4]==["ngân hàng","biển","côn trùng","cô giáo"] and len(available)==24
    wordlines={s.split("|",1)[0]:i for i,s in enumerate((AT/"wordlist.txt").read_text(encoding="utf-8").splitlines(),1)}
    out=[]; h7=[]
    for r in peer:
        k,w,c=r["khoa"],r["tu_chinh"],r["cach_doc"]; name=c.casefold()
        ofield=r["y_opus"]; st=aa.get((k,w,c))
        is_h7=k in h7_keys
        refs=[f"O\\t9-doi-dap.tsv:{r['n']}"]
        if is_h7:
            assert w in wordlines and fold(w)==k
            ref=h.get((k,sha(c.encode())))
            if not ref and c=="song ngư":
                ref=h[k,sha("Song Ngư".encode())]
            assert ref,(w,c)
            cm=byid[ref["id"]]
            refs.extend([f"wordlist.txt:{wordlines[w]}",f"E\\t9-doi-so-cap.tsv:{ref['n']} ({ref['nguon']})",
                         f"E\\t9-phan-xu-tung-cap.tsv:{cm['n']} (sạch {cm['sub_sach']}/{cm['web_sach']})"])
            if st:
                refs.append(f"A\\t9-soat-toan-tap.tsv:{st['n']}")
            if (k,name) in oc:
                refs.append(f"OE\\t9-phan-quyet.tsv:{oc[k,name]['n']}")
            if (k,name) in CHANGES:
                ac,verdict,why=CHANGES[k,name]
            elif st and st["ket_luan_Astra"]=="K2_A":
                ac,verdict,why="K2","GIU_K2",SPECIAL_K2.get((k,name),st["ly_do"])
            elif st and st["ket_luan_Astra"]=="K0_PHAN_DOI":
                ac,verdict,why="K0","THAY_K0: thay phết, chặn phet.","Cả động từ phẹt được nguồn ghi thô tục, không phụ thuộc 0/0. Đây là chứng cứ khác mặt chữ phét/phệt của chữ ký cũ, không đảo tiền lệ bình/bĩnh."
            elif st and st["ket_luan_Astra"]=="K1_PHAN_DOI":
                assert w=="cau có"
                ac,verdict,why="K1","THAY_K1: thay cau có, chặn cauco.","H6.4: vẫn có 47/1 lượt sạch (0,688 so với 0,523 của mục), có lượt gọi hồn đứng độc lập. Đếm bề mặt có nhiễu nhưng không đảo kết quả; Opus đã nhận."
            else:
                raise ValueError((k,w,c))
            if name in {"tu tập","tư tế","đượi"}:
                for src,side in ((p2,"sub"),(w2,"web")):
                    sel=[q for q in src if q["muc"]==name]
                    if sel:refs.append(f"E\\t9dd-mau-{side}.tsv:{span(sel)}")
            if w=="đuôi":
                refs.append("vi.wiktionary.org/?oldid=2010218")
            if (k,name) in {("phet","phẹt"),("cuong","cương"),("long","lồng")}:
                sel=[q for q in wit if q["muc_kiem"]==name]
                refs.append(f"E\\t9-nguon-cac-ca.tsv:{span(sel)}")
            if w=="tụ tập" and c=="tu tập":
                refs.append("TC:146,160–167; KH §4.1 (không ban hành ngưỡng r)")
            h7.append((k,name,verdict))
        else:
            key=w if k=="-" else k
            ac,verdict,why=NON_H7[key]
            if k in {"buonthiu","iuxiu","daingoang","lubu"}:
                refs.extend([f"wordlist.txt:{wordlines[w]}","E\\t9-dem-sub.tsv; E\\t9-dem-web.tsv; TC:115–131"])
                wr=h.get((k,sha(c.encode())))
                if wr:refs.append(f"E\\t9-doi-so-cap.tsv:{wr['n']} ({wr['nguon']})")
                if k=="buonthiu":refs.extend(["U\\ra-thay-chinh-giai-nghia-dat.tsv:ket_luan","U\\ra-thay-chinh-thay-the.tsv:thu_tu"])
            elif k=="thay":
                refs.append("U\\chu-ky.tsv:2152–2154; U\\ra-thay-chinh-kiem-chu-ky.py:64–82")
            else:
                refs.append(w+"; E\\t9-goi-astra.json")
                if w.endswith(":9101"):refs.append("E\\t9-mat-chinh.tsv; TC:161–164")
        signature="Y" if verdict=="GIU_K2" else "N"
        if signature=="Y":
            assert r["ky"]=="Y" and ofield.startswith("K2"),(k,c)
        out.append(dict(zip(("khoa","tu_chinh","cach_doc","nguon","y_opus","y_astra","de_xuat_chung","ky(Y/N)","ly_do"),
                            (k,w,c,"; ".join(refs),ofield,ac,verdict,signature,why))))
    assert len(out)==len(peer)==len(peer_set)==76
    assert {(k,c) for k,c,v in h7}==expectedpairs and len(h7_keys)==65
    b=io.StringIO(); wr=csv.DictWriter(b,fieldnames=out[0],delimiter="\t",lineterminator="\r\n");wr.writeheader();wr.writerows(out)
    (A/"t9-doi-dap.tsv").write_bytes(b.getvalue().encode())
    print("H7:",len(h7),"dòng",len(expectedpairs),"cặp không phân biệt hoa",len(h7_keys),"khóa; K2:",sum(v=="GIU_K2" for _,_,v in h7),len({k for k,_,v in h7 if v=="GIU_K2"}),"khóa")
    print("Phân loại:",dict(Counter(r["de_xuat_chung"].split(":")[0] for r in out)))
    print("Nguồn sau cửu chương:",available[:4],"; giới hạn của lượt này: 23 HM, không tự mở rộng lên 24.")


if __name__=="__main__":main()
