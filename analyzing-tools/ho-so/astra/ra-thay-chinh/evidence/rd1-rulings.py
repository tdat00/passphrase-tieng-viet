"""Phiếu Astra sau đọc thước mới: từng khóa, không tạo chữ ký phát hành."""
import json
from collections import Counter

from screen_core import EV, OUT, U, key, load, o1, ppm, save_json, save_tsv, tsv


KEEP = {
    "bản đồ": "Nhận K2: ban đỏ là cách đọc y khoa hẹp; chưa đủ chứng cứ nó là cách đọc thông dụng của khóa bản đồ. Không biến r=0,017866 thành mốc miễn trừ cho mọi khóa.",
    "bộ đồ": "Nhận K2 cho bợ đỡ: có nghĩa chê người, nhưng cách đọc độc lập ít dùng và khóa có đọc lành rất trội; 23/1 lượt là bằng chứng hỗ trợ, không tự là luật.",
    "chiên": "Nhận K2: nguồn vi ghi chiến kết hợp hạn chế; phải phân biệt cách dùng nói tắt/lóng với nghĩa ở từ ghép. Không đồng nhất 2.200/2.193 lượt với nghĩa chiến tranh.",
    "chồng": "Nhận K2: chông là cách đọc vũ khí ít dùng của khóa này, 29/42 lượt; không phủ nhận nó thuộc H6.1 và không miễn mọi khóa một khối.",
    "chốt": "Nhận K2: chột không chỉ nghĩa khiếm thị, còn cách dùng tâm lý trong tổ hợp; chưa đủ căn cứ coi cách đọc bệnh là thông dụng của khóa.",
    "chú ý": "Nhận K2: chùy/chuỳ là cách đọc vũ khí hiếm/chuyên biệt so với chú ý; hai cách đặt dấu dùng cùng số 33/8, không cộng đôi.",
    "chuông": "Nhận K2: nguồn en của chưởng ghi võ thuật, chủ yếu hư cấu; nghĩa đỏ toàn mục cần phân biệt chất liệu truyện. Không nhận lý do một âm tiết hay mọi truyện đều miễn H6.",
    "có mặt": "Nhận K2: cơ mật có nghĩa bí mật/riêng tư, không tự quy mọi lần dùng cho quyền lực nhà nước; cách đọc hẹp hơn có mặt.",
    "đa năng": "Nhận K2: đa nang chủ yếu trong thuật ngữ y khoa dài hơn, không suy 147 lượt web thành một cách đọc độc lập phổ biến của khóa.",
    "đề cử": "Nhận K2: dê cụ là lời chê hiếm, 2/0 lượt; đã xét nghĩa và nhóm H6, không bỏ qua chỉ vì dưới còi. Không tự suy nhãn tục/K0 từ lời chê này.",
    "đồng ý": "Nhận hướng không tự động chặn: đông y là tên ngành/y học nói chung, không tự đồng nhất với một bệnh hay thủ thuật chuyên biệt. Rút K1 của v1.",
    "đuốc": "Nhận hướng không tự động chặn: dược đứng riêng còn là thành tố/tên ngành, không tự là bệnh hoặc triệu chứng. Rút K1 đại trà của v1.",
    "giảng": "Nhận K2: giàng có nghĩa địa phương/cổ, nguồn en ghi cung/nỏ cổ và động từ chờ phương ngữ. Rút việc coi toàn số đếm là cách đọc thần linh phổ biến.",
    "kể cả": "Nhận K2: kẻ cả có cả nghĩa người trên và cách tả thái độ; chưa chứng minh toàn mục là lời chửi/tiêu cực mạnh. R thấp chỉ hỗ trợ, không quyết thay.",
    "khăn": "Nhận K2 sau xét đủ khàn/khản/khấn: đặc điểm giọng không tự là bệnh; đọc khấn có nghĩa nghi lễ nhưng ít tự nhiên ở khóa khăn. Không chỉ ký một đối chứng rồi bỏ các đối chứng còn lại.",
    "kiểu": "Nhận K2: kiêu có nghĩa chê nhưng chủ yếu cần ngữ cảnh/tổ hợp; cách đọc độc lập của khóa hiếm hơn kiểu, không tự phát hành mọi từ chê có r thấp.",
    "kính": "Giữ K2 đã ký tại chu-ky.tsv:1338–1339; không có chứng cứ mới. Tôi rút K1 v1 và thừa nhận đã bỏ sót chữ ký này khi viết cross-review.",
    "làm mẫu": "Nhận K2: làm màu có nghĩa canh tác và nghĩa lóng phô trương/làm rắc rối; chưa đủ cơ sở gán mọi lượt cho chê bai mạnh hay thao túng.",
    "liên quan": "Nhận K2 cho cách đọc liên quân ở khóa này: cách đọc chuyên ngành/ít tự nhiên hơn mục đang xét; không gọi mọi mục quân sự có r<0,035 là được giữ.",
    "lo lắng": "Nhận K2: lố lăng là nhận xét sắc thái, mức đỏ/nghĩa chê người chưa chắc trong nguyên mục; cách đọc ít gặp hơn lo lắng.",
    "nhâm nhi": "Nhận K2: nhảm nhí có thể đánh giá nội dung/lời nói chứ không chê người; không suy nhãn tục của từ dịch tiếng Anh thành K0 của tiếng Việt.",
    "phong bì": "Nhận K2/không tự động: phòng bị là chuẩn bị đề phòng nói chung; không tự đưa mọi sự đề phòng vào quân sự.",
    "phòng": "Nhận K2: phỏng đa nghĩa, không lấy toàn bộ số đếm làm nghĩa bỏng/thương tích; cách đọc bệnh của khóa chưa được chứng minh phổ biến.",
    "quà tặng": "Nhận K2: quả tang mô tả gặp đúng lúc làm điều không nên, không luôn là tội phạm/tố tụng. Không nhận lập luận rằng chỉ đi cùng bắt thì không phải từ.",
    "quên": "Nhận K2: quèn có cả cách tự hạ mình/tả vị thế, mức miệt thị người chưa chắc; không dùng riêng r=0,006731 làm lý do.",
    "theo": "Nhận K2 cho thẹo theo phạm vi phương ngữ/đặc điểm cơ thể; rút phản đối thẻo vì chưa có nghĩa gây hại toàn mục, không thêm đối tượng cắt để tạo bạo lực. Giữ theo trong nhánh hiện tại.",
    "treo": "Nhận K2: trẹo là cách đọc ít gặp, thường phụ thuộc tổ hợp; không suy mọi lượt là triệu chứng của khóa. Không mở miễn trừ mọi từ thương tích.",
    "trình diễn": "Nhận K2: trình diện còn là đến báo có mặt/ra mắt, không chỉ công an/tố tụng; nguồn vi xác nhận các nghĩa này.",
    "tung": "Nhận K2: tụng cần phân biệt nghĩa nghi lễ và thành tố trong tổ hợp; cách đọc độc lập ít tự nhiên hơn tung. Không chặn cả khóa chỉ từ thành tố.",
}

DISAGREE = {
    "bền bỉ": "Giữ đề nghị K1: nguồn vi bên bị chỉ người bị cáo trong tố tụng. Pháp lý hẹp không tự là nhẹ; H6.2 có nhân chứng/hình phạt, cần lý do về tính thông dụng chứ không chỉ nhãn M.",
    "ca nhạc": "Giữ K1: cà nhắc gắn với chân không cử động bình thường; không chỉ một dáng đi trung tính. Cần nhất quán với thớt/thọt đã đồng thuận.",
    "cắm đầu": "Giữ K1: nguồn cầm đầu nêu nhóm làm việc thường không chính đáng; không rút còn nghĩa đứng đầu chung rồi bỏ nghĩa đang phổ biến.",
    "choàng": "Giữ K1: nguồn choáng có nghĩa sốc/chóng mặt; có nghĩa bóng choáng ngợp không xóa nghĩa triệu chứng phổ biến. Cần đo nghĩa nếu phản đối phạm vi.",
    "cò trắng": "Giữ K1: cờ trắng là biểu tượng đầu hàng/đình chiến, thuộc quân sự theo toàn cụm; tiền lệ một chức danh không miễn mọi biểu tượng.",
    "giao": "Giữ K1: giáo là danh từ vũ khí độc lập trong nguồn; đa nghĩa giàn giáo không đủ để bỏ nghĩa vũ khí còn phổ biến.",
    "húng": "Giữ K1: nguồn hung có nghĩa dữ tợn/quá mạnh, không chỉ màu. Cần xét nghĩa đỏ đang dùng, không ưu tiên một nghĩa lành để giữ.",
    "hững hờ": "Giữ K1: hùng hổ được nguồn mô tả hung hăng/dữ dội; không chỉ dáng điệu vô hại. Còi tương đối bật 0,247708 >= 0,055834.",
    "khiến": "Giữ K1: khiên là khí cụ phòng thủ chống vũ khí; H6.1 gồm quân sự, không chỉ vũ khí gây sát thương.",
    "lề đường": "Giữ K1: lê dương chỉ quân đoàn/lính, không phải chỉ tên riêng; yếu tố lịch sử không tự ra ngoài H6.1.",
    "lưới": "Giữ K1: lười có nghĩa đánh giá người/lối hành xử còn thông dụng; 3,764462 PPM không được gọi hiếm chỉ vì mẫu số lưới lớn. Cần phân xử ranh giới G9.",
    "ngại": "Giữ K1: ngai có cả nghĩa ghế vua và vật thờ linh vị; không chỉ biểu tượng trang trí. Ngoại lệ công chúa/hoàng tử không tự mở rộng.",
    "ngao": "Giữ K1 vì ngạo: nguồn nêu khinh thường người; không chỉ hình vị. Không suy mọi nghĩa ngáo là ma túy hay bỏ nghĩa công cụ của ngáo.",
    "nguyên": "Giữ K1: nguyền là động từ rủa/mong người gặp nạn độc lập; không chỉ hình vị hay nguyện vọng trung tính.",
    "nhồi": "Giữ K1: nhói chỉ cảm giác đau buốt; H6.5 có triệu chứng. Không suy cứ là cảm giác thì ngoài H6.",
    "phòng ngủ": "Giữ K1: phòng ngự là cách đọc tự nhiên, có nghĩa quân sự; r=0,031147 không làm mất nghĩa đó. Đối chiếu phòng thủ đã đồng thuận; nghĩa thể thao cần xét chứ không tự miễn.",
    "phù dâu": "Giữ K1: phủ đầu mang nghĩa áp đảo tinh thần/dằn mặt để giành thế; cần đối chiếu H6.9 thao túng, không chỉ gọi M.",
    "sàng": "Giữ K1: nguồn sảng chỉ trạng thái mê man; đối chiếu mê man đã được hai bên dùng cho K1. Không chỉ là mảnh của mê sảng.",
    "sân ga": "Giữ K1: sa ngã nói sự hư hỏng/trụy lạc; không chỉ tả một thói quen trung tính. Cần phân xử H6.9 trên toàn cụm.",
    "sông": "Giữ K1: nguồn sòng có danh từ nơi đánh bạc, dùng độc lập; không chỉ là hình vị sòng bạc hoặc sòng phẳng.",
    "thắm thiết": "Giữ K1: thảm thiết chỉ mức thương tâm/đau xót rất mạnh; đối chiếu G9 với ngoại lệ buồn/khóc. Đớn đau chưa được hai bên ký giữ nên không là tiền lệ cho phép phát hành.",
    "thị trường": "Giữ K1: thị trưởng là chức vụ quyền lực nhà nước, cách đọc tự nhiên; không suy ngoại lệ đô đốc thành miễn mọi chức danh.",
    "thôn": "Giữ K1: nguồn thộn chỉ đần độn, cần nhất quán với ngốc đã đồng thuận; không đủ lý do chỉ nói chê nhẹ.",
    "thuần": "Giữ K1: thụ án là nguyên cụm pháp luật có nguồn; cùng toàn khóa thuan. Khác số khối không chứng minh tách ép.",
    "tiệm": "Giữ K1: tiêm thuốc là thủ thuật y khoa, không phải vệ sinh thường ngày như đánh răng. Đối chiếu trồng răng của H6.5; nghĩa còn phổ biến không thể bỏ.",
    "trạm": "Giữ đề nghị K1: trẫm liên quan ngôi vua/quyền lực, trảm là nghĩa hành hình cần xét riêng. Ngoại lệ ba nhân vật hoàng gia không tự phủ xưng hô này.",
    "trăng tròn": "Giữ K1: nguồn trắng trợn nêu tính ngang ngược/bất chấp luật và lẽ phải; là trạng từ hay tính từ không tự ra ngoài H6.9.",
    "tường": "Giữ K1: nghĩa tướng quân/quân hàm còn phổ biến; nghĩa dáng vẻ không xóa nghĩa quân sự. Tiền lệ đô đốc cần đọc đúng phạm vi.",
    "vòng": "Giữ K1: vong có cách đọc về người chết/thần linh còn dùng; PPM 2,860521 không tự hiếm vì r=0,017385.",
    "xuân": "Giữ K1: xử án là cụm tố tụng tự nhiên và trùng cả khóa xuan; không có căn cứ gọi tách ép chỉ vì chuyển một khối thành hai.",
}


def main():
    d = load()
    merged = tsv(U / "ra-thay-chinh-h7.tsv")
    target = [r for r in merged if r["trang_thai"].startswith("TRANH_CHAP")]
    assert len(KEEP) == 29 and len(DISAGREE) == 30
    assert {r["tu_chinh"] for r in target} == set(KEEP) | set(DISAGREE) | {"thái"}
    original = tsv(OUT / "h7-sang-loc-1177.tsv") + tsv(OUT / "h7-sang-loc-bo-sung.tsv")
    source_files = [EV / "rd1-dictionary-metadata.tsv", EV / "dictionary-rd1-h7-extra.tsv"]
    source_rows = [r for path in source_files for r in tsv(path)]
    source_refs = {}
    for r in source_rows:
        source_refs.setdefault(r["tu"], []).append(r["_ref"])
    rows = []
    for r in target:
        w = r["tu_chinh"]
        if w == "thái":
            state = "NHAN_K1"
            note = "Nhận K1 với thai: nghĩa thai nghén đối chiếu trực tiếp ví dụ có chửa/thụ thai của H6.6; nguồn toàn mục và số 807/22414. Không lấy r=1,555 làm luật mới."
        elif w in KEEP:
            state = "NHAN_K2_CU" if w == "kính" else "NHAN_HUONG_GIU_H7"
            note = KEEP[w]
        else:
            state, note = "GIU_PHAN_DOI_K1", DISAGREE[w]
        old = [x for x in original if x["tu_chinh"] == w and x["muc_K_de_xuat"] in {"K0", "K1", "CHO_NGHIA", "CHO_DO"}]
        alternatives = {x["doc_khac"] for x in old}
        if w == "thái":
            alternatives.add("thai")
        numeric, refs = [], []
        for alt in sorted(alternatives, key=o1):
            c = d["counts"].get(alt)
            if c:
                ratio = ppm(c) / ppm(d["counts"][w])
                numeric.append(f"{alt}:{c['sub_sach']}/{c['web_sach']};ppm={float(ppm(c)):.9f};r={float(ratio):.9f}")
                refs.append(c["_ref"])
            refs.extend(source_refs.get(alt, []))
        rows.append({
            "tu": w, "khoa": r["khoa"], "Opus_v2": r["opus"], "Astra_truoc": r["astra"],
            "ly_do_Opus_trong_nhap": r["ly_do_opus"],
            "Astra_duyet_nhap": state, "ly_do_Astra": note,
            "doi_chung_so": " | ".join(numeric), "nguon": ";".join([r["_ref"], *refs]),
            "trang_thai": "NHAN_DINH_ASTRA; khong phai chu ky phat hanh; khong nhan nguong 0,035",
        })
    save_tsv(EV / "rd1-H7-phan-xu.tsv", rows)
    extra = [
        {"tu": "chung cư", "Astra_duyet_nhap": "NHAN_K2", "ly_do": "Chứng cứ là bằng chứng nói chung; không chỉ tố tụng. Nhận lập trường sửa của Opus."},
        {"tu": "sắn dây", "Astra_duyet_nhap": "NHAN_K2", "ly_do": "Sán dây là tên loài; không tự biến nguyên mục thành bệnh. Nhận đối chiếu ngoại lệ tên con vật."},
        {"tu": "bình", "Astra_duyet_nhap": "GIU_CHU_KY_CU_RUT_OI", "ly_do": "Thiếu chữ bịnh trong lý do cũ không tự là chứng cứ mới để vô hiệu chữ ký theo khóa; không phản đối mới ở lượt này."},
        {"tu": "trứng", "Astra_duyet_nhap": "GIU_CHU_KY_CU_RUT_OI", "ly_do": "Thiếu chữ trừng trong lý do cũ không tự chứng minh chưa từng xét; giữ chữ ký theo khóa khi không có phản đối mới đủ căn cứ."},
    ]
    save_tsv(EV / "rd1-H7-bo-sung.tsv", extra)
    h5_rows = []
    merged5 = {(r["tu"], r["bien_the"]): r for r in tsv(U / "ra-thay-chinh-h5.tsv")}
    seven = [
        ("co rúm", "co dúm"), ("xù xì", "sù sì"), ("rầm rộ", "rần rộ"),
        ("chơ vơ", "trơ vơ"), ("xập xình", "sập sình"), ("su hào", "xu hào"),
        ("loay hoay", "lay hoay"),
    ]
    numeric_notes = {
        "co rúm": "c thiếu web 16 lượt; d có thể qua theo phụ đề.",
        "xù xì": "c thiếu phụ đề 8 lượt; d có thể qua theo web.",
        "rầm rộ": "c thiếu phụ đề 6 lượt; d có thể qua theo web.",
        "chơ vơ": "c thiếu cả hai kho; d thiếu dữ liệu phải có hai chữ ký riêng.",
        "xập xình": "c thiếu cả hai kho; d thiếu dữ liệu phải có hai chữ ký riêng.",
        "su hào": "c thiếu cả hai kho; một lượt xu hào đã được nêu nên không thể ký vô căn cứ không có lỗi.",
        "loay hoay": "c không đạt 95%; d có độ nhạy 17/3 so với 15/3, vẫn phải khép CHO_SAT_NGUONG.",
    }
    for w, alt in seven:
        original5 = merged5[(w, alt)]
        h5_rows.append({
            "tu": w, "doi_chung": alt, "Astra_duyet_nhap": "CHO_LOAI_c_d",
            "ly_do": "Không phủ nhận dạng có trong HND. Tỷ lệ 34 c/3 d không tự quyết ca này; chưa có nguồn riêng phân biệt cách viết chuẩn/lỗi. " + numeric_notes[w],
            "so_do_chinh": original5["sub_tu"] + "/" + original5["sub_bien_the"] + "; " + original5["web_tu"] + "/" + original5["web_bien_the"],
            "nguon": original5["_ref"],
        })
    for w, alt in (("cải xoong", "cải soong"), ("xà bông", "xà phòng"), ("xà phòng", "xà bông")):
        h5_rows.append({
            "tu": w, "doi_chung": alt, "Astra_duyet_nhap": "NHAN_QUAN_HE_f_CHO_DO",
            "ly_do": "Nhận cùng họ từ mượn, không hỏi supervisor xác nhận quan hệ nữa. Chưa chốt loại từ số dạng cách; phải cộng dạng gạch/viết liền, không đếm trùng.",
            "nguon": merged5[(w, alt)]["_ref"],
        })
    h5_rows += [
        {"tu": "bít tết", "doi_chung": "bíp tết", "Astra_duyet_nhap": "NHAN_QUA_CU",
         "ly_do": "Sửa lỗi của tôi: dòng 258 ghi cả ba dạng phân cách mỗi bên, loại c, 183/3 và 362/4, QUA_RIENG_H5. Không mở lại khi thiếu chứng cứ mới.",
         "nguon": "analyzing-tools\\spelling_families.tsv:258"},
        {"tu": "rầm rầm", "doi_chung": "rần rần", "Astra_duyet_nhap": "DE_NGHI_THAY_H5c_MOI",
         "ly_do": "enwiktionary rần rần rev 89902128 ghi alt form của rầm rầm, phương ngữ. Phụ đề 6+5=11, web sạch 2+5=7 (bề mặt 3+5=8). Rút CHO, đề nghị c/thiếu dữ liệu; không nhận KHAC_TU.",
         "nguon": merged5[("rầm rầm", "rần rần")]["_ref"] + ";rd1-dictionary-metadata.tsv (rần rần, en)"},
    ]
    save_tsv(EV / "rd1-H5-phan-xu.tsv", h5_rows)
    h5_extra = [
        {"tu": "buồn lòng", "doi_chung": "buồm lòng", "Astra_duyet_nhap": "NHAN_KHAC_TU",
         "ly_do": "Buồm lòng là thuật ngữ buồm, không phải cảm giác buồn; nguồn en rev 82587886. Rút CHO quan hệ này."},
        {"tu": "tâm trí", "doi_chung": "tâm chí", "Astra_duyet_nhap": "NHAN_KHAC_TU",
         "ly_do": "Tâm trí nói trí óc/nhận thức, tâm chí nói ý chí/quyết tâm; nguồn en tâm chí rev 90333139. Rút CHO quan hệ này."},
        {"tu": "run run", "doi_chung": "rung rung", "Astra_duyet_nhap": "NHAN_KHAC_TU",
         "ly_do": "Phân biệt động từ run và rung, không coi mọi cặp coda n/ng là một từ; nguồn vi rung rung rev 1327458. Rút CHO quan hệ này."},
        {"tu": "chun", "doi_chung": "thun", "Astra_duyet_nhap": "CUNG_DANH_TU_CHO_DO_NGHIA",
         "ly_do": "Quan hệ danh từ đàn hồi có nguồn; không đồng nhất mọi nghĩa động từ/vải của các mặt chữ. Cần phân định số theo H5e."},
        {"tu": "thun", "doi_chung": "chun", "Astra_duyet_nhap": "CUNG_DANH_TU_CHO_DO_NGHIA",
         "ly_do": "Cùng quan hệ với chiều chun/thun; không dùng PPM cả chuỗi làm số của một nghĩa."},
    ]
    save_tsv(EV / "rd1-H5-quan-he-bo-sung.tsv", h5_extra)
    result = {
        "H7_original_contested_cohort": 60,
        "H7_concessions_keep": 29,
        "H7_concession_replace": ["thái"],
        "H7_remaining_contested": len(DISAGREE),
        "H7_remaining_words": sorted(DISAGREE, key=o1),
        "H7_extra_pending_closed": ["chung cư", "sắn dây"],
        "H7_pending_other_keys": 46,
        "old_signature_scope_questions_withdrawn": ["kính/kinh", "bình/bịnh", "trứng/trừng"],
        "H5_old_ten_still_without_final_gate": 10,
        "H5_new_case": "rầm rầm/rần rần",
        "H5_words_requiring_adjudication": 8,
        "H5_relation_agreed_measurement_pending": ["cải xoong", "xà bông", "xà phòng"],
        "H5_affected_words_not_closed": 11,
        "H5_prior_signed_case_closed": "bít tết/bíp tết",
        "H5_additional_18_closed_different": ["buồn lòng/buồm lòng", "tâm trí/tâm chí", "run run/rung rung"],
        "H5_remaining_relations_from_18": 14,
        "new_release_signatures_written": 0,
    }
    save_json(EV / "rd1-ruling-summary.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
