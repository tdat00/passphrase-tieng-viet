"""Phiếu sau rà chéo của Astra; không sửa các kết luận vòng độc lập hoặc bảng phát hành."""
import json
from collections import Counter, defaultdict

from screen_core import EV, OUT, o1, save_json, save_tsv, tsv

CHANGES = {
    "bình": ("BAO_LUU_K2_CU_CHO_PHAM_VI_BI_NH",
             "Không mở lại bĩnh; binh đã được lý do cũ đề cập. Bịnh chưa được nhắc trong chữ ký: không gộp tự động, nhưng rút việc coi cả khóa là một lỗi K1 mới đã đủ căn cứ."),
    "khảm": ("GIU_CHU_KY_K2_CU",
             "Khám/khắm đã được lý do chữ ký tại 1270–1271 xem xét; v1 không có chứng cứ mới đủ để lật kết luận cũ."),
    "thầy": ("GIU_CHU_KY_K2_CU",
             "Rút K1 với thây: chính số 96/47 và so sánh đọc tự nhiên đã được hai SA ký ở 2152–2154."),
    "thổi": ("GIU_CHU_KY_K2_CU",
             "Rút K1 với thối: lý do cũ đã xét tính chất mùi và tên chất thải, không có chứng cứ mới ở v1."),
    "di động": ("DE_NGHI_K2_KHONG_TU_DONG",
             "Rút K0: đi đồng là động tác khẩu ngữ/phương ngữ, không phải danh từ chất thải; nguồn không ghi vulgar. Đối chiếu bĩnh, số 2/2; không suy mọi động từ bài tiết đều được miễn K0."),
    "bố mẹ": ("DE_NGHI_K1_KHONG_CHOT_K0",
             "Nguồn ghi offensive, chưa tự chứng minh đúng nhãn vulgar/K0. Giữ phản đối H6.9/H7 đối với bỏ mẹ, không nhận r<0,2 làm quyền giữ."),
    "lằng nhằng": ("DE_NGHI_K1",
             "Đồng thuận loại qua H7 với Opus; dùng K1 đã thống nhất về nhóm đỏ, không cần đẩy thành K0 khi nhãn nghĩa phụ cần phân biệt thêm."),
    "gián": ("GIU_THEO_QUYET_DINH_CHU",
             "Rút gián khỏi tập thay đang đề nghị: quyết định 5 đã giữ. Nghĩa gian còn cần phân xử, không lấy PPM cả chuỗi làm phổ biến nghĩa đỏ. Nếu sau này hai SA có căn cứ mới và muốn đổi quyết định thì trình chủ rõ, không miễn H7 ngầm."),
    "đông đúc": ("CHO_PHAN_XU_H7",
             "Rút tính chắc chắn của K1 v1: phải phân biệt sinh lý động vật/nhóm đỏ với tình dục người lớn. Bảng cũ đồng tình là trạng thái theo khóa, không tự chứng minh mọi nghĩa động tình đã được xét."),
    "nóng": ("CHO_PHAN_XU_H7",
             "V1 bỏ sót quan ngại nòng của vũ khí; không giữ nhãn không đỏ mặc định, cũng không ký chỉ vì một âm tiết."),
    "thiếu": ("CHO_PHAN_XU_H7",
             "V1 chưa xét đủ thiêu: cần phân biệt động tác đốt, bạo lực và tang lễ; không tự chốt không đỏ."),
    "tích": ("CHO_PHAN_XU_H7",
             "V1 chưa xét đủ tịch ở nghĩa tôn giáo/cái chết; cần phân biệt từ độc lập, từ ghép và nghĩa khác."),
    "chung cư": ("CHO_PHAN_XU_H6_H7",
             "Nguồn chứng cứ là bằng chứng nói chung; Opus viện tố tụng/nhân chứng. Tôi chưa đồng ý K1, nhưng ghi rõ phản đối cần hòa thay vì coi đã khép."),
    "sắn dây": ("CHO_PHAN_XU_H6_H7",
             "Nguồn sán dây là tên loài, cần hòa với ngoại lệ tên con vật và ví dụ cầu khuẩn. Không đồng nhất một loài với bệnh hoặc tự suy ghê tởm."),
}

# Đây là phản hồi về đúng cách đọc O yêu cầu, không tự ký sạch toàn khóa.
NO_BLOCK = {
    "ăn mày": "Tình cảnh/nghề xã hội không tự là lời chửi; nghĩa đỏ chưa chắc.",
    "bán thân": "Các nguồn đã tra ghi nửa người/tượng; chưa chứng thực nghĩa tình dục của đúng đầu mục. Có thể K2 không tự động, không suy nghĩa đỏ từ cả chuỗi.",
    "chứng nhân": "Nguồn ghi cách nói văn chương về người chứng kiến, không tự đồng nhất mọi lần dùng với tố tụng.",
    "có vú": "Tên/đặc tính động vật có vú không tự là tình dục người lớn; không phải tách ép chỉ vì có khoảng cách.",
    "giòi": "Tên loài; không tự xếp ghê tởm, đối chiếu bọ chét/chuột cống.",
    "háng": "Bộ phận cơ thể thường ngày, không tự là tình dục người lớn.",
    "khuẩn": "Không tự ghép thêm cầu/vi hay bệnh để tạo đối chứng dài hơn khóa; nghĩa đỏ của nguyên mục chưa chắc.",
    "liếm": "Hành động dùng lưỡi nói chung; không tự thêm đối tượng tình dục.",
    "nạng": "Dụng cụ hỗ trợ sinh hoạt, đối chiếu kính cận; không tự là y khoa chuyên biệt.",
    "nguỵ": "Phải phân biệt nghĩa của nguyên mục, tên riêng và thành tố ghép; không vì đổi số âm tiết mà gọi tách ép.",
    "ngụy": "Như nguỵ: đề nghị không tự động, không dựa vào số âm tiết.",
    "nhũng": "Không ghép thêm tham; nghĩa của thành tố không tự là nghĩa nguyên mục đang đọc.",
    "quái": "Có chất liệu truyện/trò chơi, không tự là thần linh/nghi lễ.",
    "rạch": "Động tác cắt/địa hình không tự là tự hại; không thêm cổ/tay vào đối chứng.",
    "thằng": "Xưng gọi thông tục không mặc nhiên là lời chửi của nguyên mục.",
    "trôn": "Nguồn còn có đáy đồ vật và cách gọi cổ; chưa có chứng cứ nghĩa tình dục phổ biến, không tự K0.",
    "thải": "Động tác loại bỏ không tự là danh từ chất thải hay bệnh.",
    "nguyện": "Mong muốn/cam kết không tự là nghi lễ.",
}

H5_UPDATES = [
    ("già dặn","già giặn","NHAN_LOAI_H5c",
     "Sửa KHAC_TU của tôi: enwiktionary 80169171 ghi alternative form of già giặn; trang 80175599 ghi lại già dặn. Số web 4+1<20."),
    ("bóng láng","bóng loáng","NHAN_KHAC_TU",
     "Hai nguồn phân biệt nét nhẵn và phản chiếu, không có quan hệ cách viết khác; nhận phán đoán khác hình vị của Opus."),
    ("bóng loáng","bóng láng","NHAN_KHAC_TU","Như chiều đối xứng của bóng láng/bóng loáng."),
    ("rong ruổi","giong ruổi","NHAN_QUA_H5c_THEO_SO",
     "Nguồn đã xác nhận quan hệ, nay có số 37/1 phụ đề, 21/1 web; dữ liệu loại c đủ và qua, kể cả độ nhạy dòng khác."),
    ("trưng bày","chưng bày","NHAN_QUA_SO_NHUNG_SUA_LOAI_c",
     "Nguồn chưng bày 2242633 dẫn trưng bày; HND11K cũng có. Không có nguồn ghi lỗi để xếp d; tính lại số ở cr1-H5-so-doc-lap.tsv vẫn qua c."),
    ("dây chun","dây thun","GIU_DE_NGHI_LOAI_H5c",
     "enwiktionary thun 93727986 ghi chun ở Alternative forms; vi chun 2034319 dẫn thun. Phụ đề 7+9=16. Chưa nhận lý do chỉ là đồng nghĩa hai miền."),
    ("dây thun","dây chun","GIU_DE_NGHI_LOAI_H5c","Cùng họ và phép đếm với chiều dây chun/dây thun."),
    ("phí phạm","phí phạn","GIU_DE_NGHI_LOAI_H5c",
     "vi phí phạm 1892276 ghi biến âm phí phạn; web 13+1=14, cả bề mặt tối đa 17+1=18. Không nhận KHAC_TU."),
    ("bít tết","bíp tết","CHO_H5f_DU_DANG_PHAN_CACH",
     "Không phải họ H5 đã đăng ký: chỉ có quan hệ D6. Cần cộng đủ dạng cách/gạch/viết liền; số dạng cách riêng qua không thay điều đó."),
    ("qua quýt","qua quít","RUT_LOAI_THEO_H5b_CHO_HO_RIENG",
     "Hợp đồng P2 chỉ vần i/y, không it/yt. Có từ điển cho hai dạng nhưng chưa được dùng cổng b để loại; đề nghị xét/đăng ký c nếu hai SA xác nhận cùng từ."),
    ("cải xoong","cải soong","CHO_H5f_DU_DANG_PHAN_CACH",
     "Nhận cần xét họ từ mượn, số dạng cách có 4/0 phụ đề. Chưa đếm đủ dạng phân cách theo H5f, không chốt chỉ bằng dạng cách."),
    ("lấn át","lấn áp","NHAN_KHONG_PHAT_HANH_CHO_MA_LOAI",
     "Nhận phép tính 10/75 và 9/64 vượt 10%; nếu cùng từ thì cả c lẫn d đều không qua. Nhận hướng không phát hành khi còn phản đối, nhưng cùng nghĩa trong ngữ cảnh không tự chứng minh lỗi viết; cần nguồn c/d hoặc CHO_LOAI."),
    ("chơ vơ","trơ vơ","CHUA_DONG_KY","Nguồn chỉ HND lớn không tự cho loại d. Không có lượt dạng kia không giải quyết loại c/d."),
    ("xập xình","sập sình","CHUA_DONG_KY","Như chơ vơ: cần căn cứ loại trước ngoại lệ thiếu dữ liệu."),
    ("su hào","xu hào","TU_CHOI_LY_DO_KY_HIEN_TAI",
     "Cả hai kho thiếu 20; 1/13 không được dùng ngưỡng 10%. Nếu đúng d và một lượt là lỗi đã đọc thì không thể ký không có chứng cứ lỗi."),
    ("loay hoay","lay hoay","CHUA_DONG_KY",
     "Số dạng lỗi là 3 theo mọi dòng và 3 theo dòng khác; thay đổi do dạng chính 17→15. Cần chứng cứ/hash đọc thêm, không ký theo lời giải thích trùng dòng chưa khớp số."),
    ("hì hục","hì hụi","GIU_CHO_NHAN_DIEN",
     "T-dpv2-4 không kết luận quan hệ này, nên không thể dùng nó làm chứng minh KHAC_TU."),
]


def main():
    diff={r["tu_chinh"]:r for r in tsv(EV/"cr1-diff-H7-theo-khoa.tsv")}
    changes=[]
    for w,(new,note) in sorted(CHANGES.items(),key=lambda x:o1(x[0])):
        r=diff[w]
        changes.append({"tu":w,"khoa":r["khoa"],"A_v1":r["A_v1"],"O_v1":r["O_v1"],
                        "A_sau_ra_cheo":new,"ly_do":note,
                        "phat_hanh":"CHUA_PHE_DUYET; không sửa bảng gốc",
                        "bang_chung":r["A_nguon"]+";"+r["O_nguon"]})
    save_tsv(EV/"cr1-Astra-sua-H7.tsv",changes)
    arows=tsv(OUT/"h7-sang-loc-1177.tsv")+tsv(OUT/"h7-sang-loc-bo-sung.tsv")
    bypair={(r["tu_chinh"],r["doc_khac"]):r for r in arows}
    byword=defaultdict(list)
    for r in arows:
        byword[r["tu_chinh"]].append(r)
    responses=[]
    for r in tsv(EV/"cr1-audit-96-K2.tsv"):
        w=r["tu"];readings=r["doc_khac"].split(";")
        same=[];accepted=[]
        for alt in readings:
            ar=bypair.get((w,alt))
            st=ar["muc_K_de_xuat"] if ar else "CHUA_CO_PHIEU_A"
            same.append(f"{alt}:{st}")
            if alt in NO_BLOCK:
                accepted.append(alt)
        other=[x["doc_khac"] for x in byword[w] if x["doc_khac"] not in readings
               and x["muc_K_de_xuat"] in {"K0","K1","CHO_NGHIA","CHO_DO"}]
        if w in CHANGES:
            answer="CAN_PHAN_XU_THEO_BAN_SUA_A"
        elif len(accepted)==len(readings):
            answer="DONG_Y_HUONG_KHONG_TU_DONG_THEO_NGHIA"
            if other:
                answer="DONG_Y_CACH_DOC_NAY_CHUA_DONG_TOAN_KHOA"
        elif any(bypair.get((w,x),{}).get("muc_K_de_xuat") in {"K0","K1"} for x in readings) or other:
            answer="CHUA_DONG_Y_KY_K2"
        else:
            answer="CAN_THEM_CAN_CU_TRUOC_KY"
        responses.append({
            "tu":w,"khoa":r["khoa"],"O_cach_doc_xin_ky":r["doc_khac"],"A_ve_cung_cach_doc":";".join(same),
            "A_doi_chung_khac_con_phan_doi_cho":";".join(other) or "-",
            "A_phan_hoi":answer,
            "ly_do_cu_the_cho_cach_doc_co_the_khong_chan":";".join(x+":"+NO_BLOCK[x] for x in accepted) or "-",
            "O_ly_do":r["O_ly_do"],
            "chu_ky":"CHUA_KY_PHAT_HANH; đây là phiếu rà chéo, không phải 192 chữ ký mới",
            "nguon":r["_ref"],
        })
    save_tsv(EV/"cr1-Astra-tra-loi-96-K2.tsv",responses)
    save_tsv(EV/"cr1-Astra-sua-H5.tsv",[
        {"tu":a,"bien_the":b,"A_sau_ra_cheo":c,"ly_do":reason,"trang_thai":"NHAN_DINH_ASTRA; CHO_OPUS_PHAN_HOI"}
        for a,b,c,reason in H5_UPDATES
    ])
    metrics={"H7_corrections":len(changes),"H5_positions":len(H5_UPDATES),
             "K2_keys":len(responses),"K2_response_counts":Counter(r["A_phan_hoi"] for r in responses),
             "new_release_signatures_written":0,"original_files_rewritten":False}
    save_json(EV/"cr1-ruling-summary.json",metrics)
    print(json.dumps(metrics,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
