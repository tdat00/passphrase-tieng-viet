"""Ghép bằng chứng và ý kiến của Astra; không suy chữ ký hai bên từ một mã giữ theo khóa."""
import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path

E=Path(__file__).resolve().parent
A=E.parent; AT=E.parents[3]; U=AT/"ho-so"/"unified"
S,W=34314528,149860716
def read(p):
    with p.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def dump(p,rs):
    b=io.StringIO();w=csv.DictWriter(b,fieldnames=rs[0].keys(),delimiter="\t",lineterminator="\r\n");w.writeheader();w.writerows(rs);p.write_bytes(b.getvalue().encode())
def sha(b):return hashlib.sha256(b).hexdigest()

# Số thứ tự chỉ có hiệu lực với đúng SHA-256 của tập ID bên dưới.
# K2_A: chữ ký riêng "không tự động chặn" cho đúng đọc đối chứng; chưa có chữ ký Opus đúng phạm vi mới.
CARDS={}
def group(code,text):
    for line in text.strip().splitlines():
        number, word, reason=line.strip().split("|",2)
        i=int(number);assert i not in CARDS;CARDS[i]=(word,code,reason)
group("K0_PHAN_DOI","""
2652|phẹt|Cả động từ được VI:37654 và VDict ghi nhận có cách nói tục về bài tiết; không phải suy từ một thành tố. Phiếu cũ cho phét/phệt không chứa phẹt. K0 không có ngưỡng.
""")
group("K0_CAN_PHAN_XU","""
896|cương|EN:15144 ghi riêng tính từ có nghĩa về cơ quan sinh dục nam; phân biệt với dây cương và các nghĩa khác. Phiếu cuống mới xét cuồng/cưỡng. Phải phân định nghĩa độc lập còn phổ biến, không dùng toàn bộ 300/2310 lượt hoặc các cụm cương cứng/cương dương làm tỷ lệ nghĩa.
2010|lồng|EN:25441 ghi riêng mặt chữ lóng mô phỏng phát âm của từ tục; chữ gốc mang khóa khác nhưng mặt chữ được ghi đúng là lồng. Mục cũng có nhiều nghĩa lành, cần phân xử quy chế dạng nói tránh và độ phổ biến của nghĩa phụ; không cộng tất cả lượt chỉ lồng chim/lồng ghép.
""")
group("K1_PHAN_DOI","""
483|cầu cơ|Nguyên cụm là thực hành gọi hồn; có mẫu thật ở hai kho (kể cả lượt đứng riêng) và có còi. Không phải lời cầu mong nói chung.
3628|tu tập|Cách đọc thực hành tu học tôn giáo thông dụng, có còi tuyệt đối. Không nhầm với nhóm người tụ tập hay dựa vào riêng tiếng tu.
3629|tư tế|VI:423530 xác nhận người thực hiện nghi lễ; cách đọc ở hai kho rõ và thông dụng, thuộc H6.4. Cần xét cả tứ tế cùng khóa riêng.
""")
group("K2_A","""
82|bàn độc|Cách gọi đồ thờ cũ, 0/0; không dùng riêng tiếng độc làm còi. THONG_TIN của P2 không phải cặp chữ ký.
86|băng|Hai phiếu cũ cho bảng nêu băng/đạn hoặc băng đảng nhưng đã mang THAY_THE; hai phiếu đang hiệu lực chỉ nêu báng. Bảo toàn đối chứng cũ khi mở rộng chữ ký, không tự chuyển thành K1.
93|bang đỏ|Thuật ngữ bầu cử của Hoa Kỳ, 0/0 ở hai kho đã ghim, cách đọc phụ thuộc ngữ cảnh nước ngoài.
133|bán thần|Đối chứng về thần linh/chất liệu thần thoại; không phải bán thân mà D-rtc-7 đã cân nhắc. Không xin lật quyết định giữ bạn thân; ký mở rộng phạm vi.
233|binh di|Cách gọi dẹp giặc đã xét dù không có lượt; nghĩa quân sự cổ khác với tên riêng và với mặt chính.
263|bò đỏ|VI/EN ghi riêng nghĩa chính trị miệt thị, ngoài tên giống bò. Cách đọc phụ ít xuất hiện; chữ ký bộ đồ cho bợ đỡ không bao quát.
374|cai cò|Đối chứng chỉ chức cảnh sát cũ, 0/0; khác cai cơ đã ký cho cãi cọ.
551|chảnh|Có lời chê làm cao nhưng cũng có cách trêu nhẹ, không tách nghĩa từ tần suất cả mặt chữ. Đối chứng đã bật còi.
571|chấp nhất|Có thể trách thái độ so đo/cố chấp, nhưng không nhất thiết là xúc phạm; 6/0 vượt mốc tương đối của từ vào chấp nhặt.
649|chính đảng|Nguyên cụm liên quan chính trị rõ, nhưng cách đọc phụ có 6/48 và dưới hai mốc. Không gọi THONG_TIN cũ là hai chữ ký K2.
650|chỉnh đảng|Thuật ngữ chính trị chuyên biệt, 0/0; ký theo đúng cả cụm, không cấm tiếng đảng riêng.
726|chung chi|Nguồn có nghĩa hối lộ, trong hai kho cả cụm vẫn thưa; không quy mọi lượt đứng liền thành đưa hối lộ.
733|chủng tử|Có nghĩa Phật học cùng nghĩa về hạt giống; nghĩa đạo không rõ khi đọc riêng, không dùng số cả cụm làm tỷ lệ nghĩa.
831|cộng đoàn|Có nghĩa cộng đoàn Công giáo; còi bật. Không đồng nhất một cộng đồng tín hữu với bản thân nghi lễ; đây không phải công đoàn đã xét ở T-rtc-15.
910|đa đảng|Toàn cụm thuộc chính trị, 0/30 ở kho ghim; cách đọc phụ dưới hai mốc, không suy nhãn THONG_TIN thành chữ ký phát hành.
931|Đại hãn|Tước vị trong lịch sử; không cộng tần suất các nghĩa đại hạn để suy số lượt chức danh. Chữ ký dài hạn cũ không nêu đối chứng mới này.
966|đảng trị|Thuật ngữ thể chế thuần chính trị nhưng nguyên cụm văn viết hiếm, 0/0.
1030|đau đẻ|Cách đọc tình trạng sinh nở có thật và có còi tương đối; không đồng nhất với hành vi tình dục hoặc mọi bệnh lý. Mã thông tin cũ không đại diện chữ ký.
1215|đòn đá|H6.1: tên đòn võ, hai lượt sạch đều đúng ngữ cảnh; có còi tương đối dù PPM thấp. Astra ký K2 vì tổng chỉ hai lượt; cần Opus đối đáp, không tự cho đon đả qua.
1257|Đông Du|Phong trào lịch sử, cũng là tên trong địa danh; không gán toàn bộ tần suất hạ chữ cho chính trị, nhưng không bỏ qua chỉ vì viết hoa.
1258|đông du|Đi về phương đông cũng là văn sử; cùng số với Đông Du, không cộng đôi. Cần phân biệt nghĩa của nguyên cụm.
1471|Gia-vê|Tên riêng chỉ thần linh, không bỏ qua theo quy tắc tên người/địa danh; hình thức cụ thể này hiếm.
1595|Hình thư|Nhan đề bộ luật trong lịch sử; không gọi mọi lượt một tên sách cổ là tố tụng hiện hành.
1663|hồng chuyên|Thuật ngữ chính trị có nguồn cho nguyên cụm, 0/2. Đã từng cắm cờ ở hồ sơ ứng viên; hóng chuyện chưa có hai chữ ký cho đối chứng.
1691|hưởng dương|Uyển ngữ tang lễ chỉ tuổi người mất, không phải tên cây hướng dương; chỉ một lượt web, không lấy vong làm ngưỡng.
1751|khảo|Có nghĩa thẩm vấn có thể dùng vũ lực ngoài nghĩa khảo sát/nghiên cứu; toàn mặt chữ bật còi. Chữ ký khao cho khả ố không ký luôn khảo.
1756|khấu|Có nghĩa giặc/cướp kiểu Hán Việt, thường cần tổ hợp; còn các cách dùng trung tính. Không gán cả mặt chữ cho tội phạm.
1859|kình ngạc|Có cách dùng văn sử về giặc ngoài nghĩa hai con vật, 0/0; đã xét bạo lực dưới còi.
1964|linh đường|Nguồn hiện hành xác nhận nơi tang lễ của nguyên cụm, nhưng chỉ 1/1 lượt sạch.
2122|ma sơ|Danh xưng người tu nữ, không phải hành vi nghi lễ; cách đọc mượn ít gặp của khóa mã số, không mặc nhiên chặn.
2189|mụ nội|Từ điển ghi lối chửi thề, không đủ nhãn tục của toàn mục để áp K0; chỉ một lượt phụ đề.
2225|nặng căn|Nguồn ghi cách nói về thói xấu khó sửa, 0/2; có thể gợi tín ngưỡng theo ngữ cảnh, không gán toàn bộ lượt cho nghĩa đó. Không nhầm với cờ H5 lặng câm đã đóng.
2306|nghề|Mục tính từ có nhãn thô tục ở Kaikki VI, trong khi Việt–Việt 30K viết tắt và nghĩa nghề nghiệp thông thường rất rộng. Chưa đủ căn cứ cho nghĩa phụ tục phổ biến, không tự K0.
2403|nha bào|Thuật ngữ vi sinh chuyên biệt nhưng chưa có lượt sạch; không phải mọi sinh vật là bệnh.
2453|nhân tai|Nguyên cụm có nghĩa tai họa do người gây ra; một lượt web, không mặc định là cách đọc phổ biến của nhân tài.
2644|phật sống|Đối chứng về tôn giáo rõ nhưng cách gọi này rất thưa (1/1); không gán mọi cụm có phật là đỏ.
2731|quại|Động từ chỉ đánh mạnh đã xét dưới còi, 3/0; chữ ký quai với quái không bao trùm đối chứng này.
2735|quân bộ|Nguồn dẫn về binh chủng; H6.1 đã xét dưới mốc, 0/0.
2888|sân hận|Có nghĩa thù ghét và thuật ngữ Phật học; đủ căn cứ đọc toàn cụm, thưa hơn đáng kể so với mục chính.
2936|sở trưởng|Chức vụ trong cơ quan ở bối cảnh nước ngoài, còi bật nhưng phạm vi hẹp; đối chiếu quyết định giữ thị trưởng, không suy ra miễn mọi chức danh.
2975|tâm chấn|Tâm động đất là khái niệm địa chấn; không mặc định mọi hiện tượng địa chất là thảm họa dù còi bật.
3006|tán tỉnh|Dùng cả cho việc làm quen và cho việc dụ bằng lời; việc tìm hiểu tình cảm không tự là tình dục hay thao túng. Còi tuyệt đối và tương đối đều bật.
3033|thâm thù|Nghĩa thù hận mạnh nhưng lối nói văn viết thưa, 17/0, chưa chạm hai mốc; không gán phán quyết ý nghĩa chỉ từ chữ thù.
3061|thánh quả|Thuật ngữ Phật học chuyên biệt; hai kho không có lượt sạch.
3063|thánh thất|Nơi thờ tự có thật, 0/7; chưa phải cách đọc thông dụng của thành thật ở hai kho ghim.
3064|thánh thi|Cụm chỉ tác phẩm tôn giáo; chỉ 1/14, ký theo đúng đối chứng này.
3163|thoái|Ngoài nghĩa lùi có danh từ chuyên môn võ thuật; đã xét khả năng bạo lực chứ không lấy số của cả mặt chữ cho đòn võ.
3180|thoi|Có động từ đánh mạnh ngoài công cụ dệt; đã đọc cả dưới mốc vì bạo lực, thực tế còn có còi. Phiếu thổi hiện nói về thối chứ chưa nói về thoi.
3231|thứ dữ|Có cách dùng về người bạo lực, cũng có sắc thái khẩu ngữ chỉ người sành sỏi; đã xét cả H6.1, không gán toàn tần suất cho nghĩa gây hại.
3255|thuốc đỏ|Sản phẩm dùng sát trùng, cách đọc phụ thưa, 5/6; không tự chặn theo riêng chữ thuốc.
3266|thượng|Nghĩa động từ có ghi sắc thái thô tục ở một nguồn nhưng nguồn khác ghi khẩu ngữ, còn nhiều nghĩa lành. Chưa chứng minh nghĩa phụ tục phổ biến.
3311|Tiền Lê|Tên triều đại xác định trong sử Việt; không xem là tên riêng vô can, cũng không gán mọi lượt hạ chữ cho chế độ chính trị.
3312|tiền Lê|Cùng cách đọc lịch sử với Tiền Lê, không cộng đôi số hạ chữ.
3366|tì vị|Khái niệm cơ quan trong đông y, không chỉ bệnh; đúng nguyên cụm dùng hiếm (0/2).
3578|tù đồ|Lối gọi tù nhân cũ, 1/0; đã xét nghĩa tố tụng, không lấy tần suất tù đứng riêng.
3626|tướt|Cách dùng chỉ chứng bệnh trẻ nhỏ, không phải tên chất thải hay từ tục; hiếm, 3/0.
3630|tứ tế|Nghi thức được ban trong văn sử cổ, rất thưa. Đây là cách đọc riêng ngoài tư tế ở cùng khóa.
""")
group("DA_KY_HOAC_CHU_GIU","""
224|bĩnh|Chữ ký có hiệu lực cho bình nói rõ động tác bài tiết phương ngữ; không hủy quyết định T-rtc-2 vì chính lý do đã xét.
268|bố đường|Hai chữ ký K2 lịch sử còn hiệu lực của bổ dưỡng; Astra nêu chính bố đường và đã phân biệt với nghĩa tình dục bắt buộc.
1109|đi đồng|T-rtc-2 giữ đúng K2 đã ký của di động sau khi xét lại bằng chứng.
1285|Đông y|T-rtc-4: tên một ngành không tự là bệnh hay thủ thuật; đồng ý không đỏ, kể cả viết hoa đầu mục.
1286|đông y|T-rtc-4: rút K1 sơ bộ; nguồn hiện hành dùng như tên ngành, không tự là thủ thuật.
1337|dược|T-rtc-4 giữ đuốc, dược là thành tố hoặc tên ngành; không chỉ một bệnh.
1429|gian|Quyết định 5 của chủ dự án giữ gián; không mở lại cùng lý do.
2597|nường|T-rtc-2; chữ ký cũ của nướng đã xét biểu tượng nghi lễ địa phương, không phải chứng cứ mới.
2651|phét|T-rtc-2 và hai chữ ký phết đã xét riêng nghĩa cũ của phét; không nhầm với phẹt.
2670|phối|Hai phiếu K2 cũ của phổi xét tường minh phối; nguồn ghi sinh sản động vật, không phải mặc nhiên tình dục người lớn.
2958|sụp lở|Có hai chữ ký cũ của súp lơ xét đúng đối chứng, không có chứng cứ mới để lật.
""")

def main():
    raw=read(E/"t9-doi-so-cap.tsv")
    assert sha(("\n".join(r["id"] for r in raw)+"\n").encode())=="a2e59d4008784232c875974cea34a0934f7b0c1a8b46236e83d55c34ed00cec6"
    prefixes=[x.split("|",1)[0] for x in (AT/"wordlist.txt").read_text(encoding="utf-8").splitlines()]
    measures={s:{r["mat_chu_thuong_sha256"]:r for r in read(E/f"t9-dem-{s}.tsv")} for s in ("sub","web")}
    count={}
    for r in read(U/"opus-counts.tsv"):
        if r["tu"] not in count or r["vai_tro"]=="UNG_VIEN":count[r["tu"]]=(int(r["sub_sach"]),int(r["web_sach"]))
    for s in ("l2","l2b","l2c","l2d","l3"):
        for r in read(U/f"{s}-ung-vien.tsv"):count.setdefault(r["tu"],(int(r["sub_sach"]),int(r["web_sach"])))
    p=lambda a,b:500000*(a/S+b/W)
    allout,action,closed=[],[],Counter()
    for r in raw:
        i=int(r["stt"]);w=prefixes[int(r["dong_wordlist"])-1];k=r["khoa"]
        a,b=[int(r[side]) if r[side]!="-" else int(measures[side][r["mat_thuong_sha256"]]["sach"]) for side in ("sub","web")]
        pp=p(a,b);p0=p(*count[w]); flags="+".join(z for z,condition in (("≥0,3",pp>=.3),("≥mục",pp>=p0)) if condition) or "THAP"
        severity="HURT" in r["nhan_doc"] or "K0" in r["nhan_doc"]
        if i in CARDS:
            alt,code,why=CARDS[i]
            assert sha(alt.encode())==r["mat_chu_sha256"],(i,alt)
        elif r["cung_mat_khac_hoa"]=="1":
            code,why="KHONG_DOC_KHAC","Chỉ đổi chữ hoa, không thêm một cách đọc."
        elif r["muc_A_sau"]=="GIU_K2":
            code,why="GIU_K2_DA_KY","Đúng đối chứng trong phạm vi phiếu khép mục mở."
            assert r["hai_K2_cua_khoa"]=="1",(i,w)
        elif r["muc_A_sau"] in ("GIU_KHONG_DO","KHONG_DO"):
            code,why="KHONG_DO_DA_PHAN_XU","Đúng quan hệ trong phiếu khép mục mở."
        elif r["phan_xu_P2"]=="KHONG_TU_DONG":
            code,why="GIU_KQ_P2","Đúng đối chứng đã phân xử; không có bằng chứng đảo quyết định."
        elif r["muc_A_cu"] in ("K0","K1","K2_DE_NGHI_KHONG_CHAN") and r["hai_K2_cua_khoa"]=="1":
            code,why="GIU_KQ_CU_T_RTC_2","Lịch sử có phiếu K2; đã kiểm tiếp phạm vi riêng của cách đọc, không hủy bằng mã vòng 1."
        elif r["chi_ten_trong_nguon"]=="1" or r["khac_hoa"]=="1":
            code,why="KHONG_DO_TEN_RIENG_HOAC_CUNG_AM","Tên riêng, tên địa lý, tên người hoặc đổi hoa không tự là cách đọc đỏ; ngoại lệ chức vụ/thần linh đã tách."
        elif r["muc_A_cu"]=="KHONG_DO":
            code,why="KHONG_DO_XAC_NHAN","Đã có phiếu đọc từng mặt chữ; rà tín hiệu mới của ngữ nghĩa toàn mục không cho thêm phản đối."
        elif r["muc_A_cu"]=="CUNG_MAT_CHU_KHAC_KHOANG":
            code,why="KHONG_DO_BIEN_DANG","Đối chứng khác cách trình bày/phân cách mà không tạo nghĩa đỏ."
        elif r["muc_A_cu"]=="DA_CO_PHAN_XU":
            code,why=("GIU_KQ_CU_DA_KIEM","Đã đọc đối chứng của cờ P2; không có quan ngại mới đủ H9 ngoài các ca tách riêng.")
        elif r["muc_A_cu"]=="-" and r["muc_A_sau"]=="-":
            code,why="KHONG_DO_ASTRA_T9","Astra đã đọc hàng đợi các mặt chữ chưa có phiếu; không có nghĩa đỏ nguyên mục được xác nhận."
        else:
            raise AssertionError((i,w,r["muc_A_cu"],r["muc_A_sau"]))
        waiting=code in {"K0_PHAN_DOI","K0_CAN_PHAN_XU","K1_PHAN_DOI","K2_A"}
        packed=dict(id=r["id"],khoa=k,doi_chung_sha256=r["mat_chu_sha256"],dong_wordlist=r["dong_wordlist"],tu_vao=r["tu_vao"],
                    sub_sach=a,web_sach=b,ppm_doc=f"{pp:.6f}",ppm_muc=f"{p0:.6f}",coi_so=flags,
                    nguon_va_dong=r["nguon"],can_cu_cu=r["phieu_sau"] if r["phieu_sau"]!="-" else r["phieu_cu"],
                    ket_luan_Astra=code,trang_thai="CHO_DOI_DAP" if waiting else "DA_SOAT_ASTRA")
        allout.append(packed);closed[packed["trang_thai"]]+=1
        if i in CARDS:
            action.append(dict(stt=i,tu=w,doi_chung=alt,**packed,nguoi_duyet="SA-Astra",ngay="2026-11-22",
                               ky_K2_cho_dung_doi_chung="Y" if code=="K2_A" else "-",ly_do=why))
    dump(E/"t9-phan-xu-tung-cap.tsv",allout)
    dump(A/"t9-soat-toan-tap.tsv",action)
    assert len({r["id"] for r in allout})==len(allout)==3856
    print(len(allout),"cặp;",dict(closed),"; ca chi tiết",dict(Counter(r["ket_luan_Astra"] for r in action)))
    print("Số cặp đạt mốc số (không nhất thiết đỏ):",sum(r["coi_so"]!="THAP" for r in allout))
    print("Chưa khép ở từ vào:",[(r["tu"],r["doi_chung"],r["ket_luan_Astra"]) for r in action if r["tu_vao"]=="1" and r["trang_thai"]=="CHO_DOI_DAP"])
    print("Số khóa còn đối đáp:",len({r["khoa"] for r in action if r["trang_thai"]=="CHO_DOI_DAP"}))
    return 1 if closed["CHO_DOI_DAP"] else 0


if __name__=="__main__":raise SystemExit(main())
