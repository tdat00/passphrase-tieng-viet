"""Đối chiếu bản độc lập vòng 1; giữ nguyên cả hai bản, chỉ ghi hồ sơ rà chéo của Astra."""
import ast
import csv
import hashlib
import json
import re
import statistics
import unicodedata as ud
from collections import Counter, defaultdict
from fractions import Fraction

from screen_core import AT, EV, OUT, ROOT, U, key, load, o1, ppm, read, save_json, save_tsv, tsv

O = AT / "ho-so" / "opus" / "ra-thay-chinh"
OE = O / "evidence"


def h7_state(rows, who):
    states = {r["muc_K_de_xuat"] if who == "A" else r["de_xuat"] for r in rows}
    if not states:
        return "KHONG_CO_DONG"
    if states & {"K0", "K0_DE_XUAT"}:
        return "K0"
    if states & {"K1", "K1_DE_XUAT", "K1_GIAP_RANH"}:
        return "K1"
    if states & {"CHO_NGHIA", "CHO_DO"}:
        return "CHO"
    if states & {"K2_DE_NGHI_KHONG_CHAN", "K2_DE_XUAT"}:
        return "K2_DE_XUAT"
    if states & {"DA_CO_PHAN_XU", "K2_DA_KY"}:
        return "DA_PHAN_XU"
    return "KHONG_CHAN"


def h5_state(r, who):
    if not r:
        return "KHONG_CO_DONG"
    a = r["hanh_dong"]
    if a in {"DE_NGHI_THAY", "THAY", "KHONG_CHO_VAO_DU_PHONG"}:
        return "LOAI"
    if a == "DA_THAY_VI_H7":
        return "LOAI_H7"
    if a in {"CHO_H5_TRUOC_FINAL", "HOA_NHAN_DIEN_TRUOC_FINAL",
             "KY_HAI_BEN_HOAC_THAY", "DOC_THEM_KY_HOAC_THAY"}:
        return "CHO"
    return "KHONG_LOAI"


def detail(rows, who):
    return ";".join(
        f"{r['doc_khac']}:{r['muc_K_de_xuat'] if who == 'A' else r['de_xuat']}"
        for r in rows
    ) or "-"


def classify(t, a, b, aw, bw):
    if t in {"b", "c", "f"}:
        if a+b < 20 or aw+bw < 20:
            return "LOAI_THIEU_DU_LIEU"
        return "QUA_RIENG_H5" if 100*a >= 95*(a+b) and 100*aw >= 95*(aw+bw) else "LOAI_CANH_TRANH"
    totals = [(b, a+b), (bw, aw+bw)]
    totals = [(other, n) for other, n in totals if n >= 20]
    if not totals:
        return "CAN_HAI_CHU_KY"
    if any(100*other >= 10*n for other, n in totals):
        return "LOAI_LOI"
    return "TRU_DIEM" if any(100*other >= 5*n for other,n in totals) else "QUA_RIENG_H5"


def refs(rows):
    return ";".join(r["_ref"] for r in rows) or "-"


def main():
    d = load()
    a7 = tsv(OUT/"h7-sang-loc-1177.tsv") + tsv(OUT/"h7-sang-loc-bo-sung.tsv")
    o7 = tsv(O/"sang-loc-h7.tsv")
    a5 = tsv(OUT/"h5-sang-loc-632.tsv") + tsv(OUT/"h5-sang-loc-bo-sung.tsv")
    o5 = tsv(O/"sang-loc-h5.tsv")
    ar = tsv(OUT/"de-xuat-thay-the-S4.tsv")
    orepl = tsv(O/"de-xuat-thay.tsv")
    aa, oo = defaultdict(list), defaultdict(list)
    for r in a7:
        aa[r["khoa"]].append(r)
    for r in o7:
        oo[r["khoa"]].append(r)
    diff7 = []
    for w in d["main"]:
        k = key(w)
        av, ov = h7_state(aa[k], "A"), h7_state(oo[k], "O")
        diff7.append({
            "tu_chinh": w, "khoa": k, "A_v1": av, "O_v1": ov,
            "A_so_cap": len(aa[k]), "O_so_cap": len(oo[k]),
            "lech": str(av != ov), "A_chi_tiet": detail(aa[k], "A"), "O_chi_tiet": detail(oo[k], "O"),
            "A_nguon": refs(aa[k]), "O_nguon": refs(oo[k]),
            "ghi_chu": "So bản độc lập; KHONG_CO_DONG không phải kết luận an toàn; K1 giáp ranh của Opus gộp vào K1.",
        })
    save_tsv(EV/"cr1-diff-H7-theo-khoa.tsv", diff7)
    ad = {(r["tu"],r["bien_the"]):r for r in a5}
    od = {(r["tu"],r["bien_the"]):r for r in o5}
    diff5 = []
    for w,v in sorted(ad.keys() | od.keys(), key=lambda p:(o1(p[0]),o1(p[1]))):
        a, b = ad.get((w,v)), od.get((w,v))
        av, bv = h5_state(a,"A"), h5_state(b,"O")
        diff5.append({
            "tu": w, "bien_the": v, "la_tu_chinh": str(w in d["main"]),
            "A_v1": av, "O_v1": bv, "lech": str(av != bv),
            "A_loai": a["loai_H5_de_xuat"] if a else "-",
            "O_loai": b["loai_H5"] if b else "-",
            "A_ly_do": a["ly_do"] if a else "-", "O_ly_do": b["ly_do"] if b else "-",
            "O_ket_qua_so": b["ket_luan_H5"] if b else "-",
            "A_nguon": a["_ref"] if a else "-", "O_nguon": b["_ref"] if b else "-",
        })
    save_tsv(EV/"cr1-diff-H5.tsv", diff5)
    roles_a, roles_o = defaultdict(list), defaultdict(list)
    for r in ar:
        roles_a[r["tu_ra"]].append(("RA", r["slot"], r["ly_do_ra"], r["_ref"]))
        roles_a[r["tu_vao_de_xuat"]].append(("VAO_CO_DIEU_KIEN_HM", r["slot"], r["nguon"], r["_ref"]))
    for r in orepl:
        roles_o[r["tu"]].append((r["vai_tro"],r["thu_tu"],r["doi_chung"],r["_ref"]))
    replacement_diff = []
    for w in sorted(roles_a.keys() | roles_o.keys(), key=o1):
        ra, ro = roles_a[w], roles_o[w]
        replacement_diff.append({
            "tu": w, "khoa": key(w),
            "A_vai_tro": ";".join(x[0] for x in ra) or "-",
            "O_vai_tro": ";".join(x[0] for x in ro) or "-",
            "A_chi_tiet": ";".join(f"{x[1]}:{x[2]}" for x in ra) or "-",
            "O_chi_tiet": ";".join(f"{x[1]}:{x[2]}" for x in ro) or "-",
            "A_nguon": ";".join(x[3] for x in ra) or "-",
            "O_nguon": ";".join(x[3] for x in ro) or "-",
            "canh_bao": "A dùng nhánh xin mở HM và S2 mới; O dùng hạng lịch sử/dự phòng. Hai tập chưa phải cùng giả thiết.",
        })
    save_tsv(EV/"cr1-diff-thay-va-vao.tsv", replacement_diff)
    signed = defaultdict(list)
    for r in d["chu-ky"]:
        if r["loai_ky"] == "K2" and r["hieu_luc"] == "CO":
            signed[r["tu"]].append(r)
    hist = []
    for r in o7:
        if r["de_xuat"] == "K2_DA_KY":
            ss = signed[r["tu_chinh"]]
            hist.append({
                "tu": r["tu_chinh"], "doc_khac": r["doc_khac"], "O_nguon": r["_ref"],
                "co_du_hai_nguoi": str({"Astra","Opus"} <= {x["nguoi_ky"] for x in ss}),
                "doc_khac_duoc_nhac_nguyen_mat_chu": str(any(r["doc_khac"] in x["ly_do"] for x in ss)),
                "ly_do_lich_su": ";".join(x["nguoi_ky"]+":"+x["ly_do"] for x in ss),
                "chu_ky_nguon": refs(ss),
                "luu_y": "Phải đọc phạm vi chữ ký; không suy kiểm tra substring này thành phán quyết tự động.",
            })
    save_tsv(EV/"cr1-chu-ky-cu.tsv", hist)
    blocked_o = {r["tu_chinh"] for r in o7 if r["de_xuat"].startswith(("K0_DE","K1"))}
    groups = defaultdict(list)
    for r in o7:
        if r["de_xuat"]=="K2_DE_XUAT" and r["tu_chinh"] not in blocked_o:
            groups[r["tu_chinh"]].append(r)
    assert len(groups) == 96
    k2 = []
    for w, rr in sorted(groups.items(), key=lambda x:o1(x[0])):
        astate = h7_state(aa[key(w)],"A")
        k2.append({
            "tu": w, "khoa": key(w), "doc_khac": ";".join(r["doc_khac"] for r in rr),
            "O_ly_do": ";".join(r["ly_do"] for r in rr),
            "so_cap_O": len(rr),
            "ly_do_chi_mot_am_tiet": str(any("khóa một âm tiết" in r["ly_do"] for r in rr)),
            "ly_do_r_duoi_02": str(any(re.fullmatch(r"r = [0-9.]+ < 0,2",r["ly_do"]) for r in rr)),
            "A_v1_theo_khoa": astate,
            "A_v1_chi_tiet": detail(aa[key(w)],"A"),
            "O_nguon": refs(rr), "A_nguon": refs(aa[key(w)]),
            "trang_thai_ra_cheo": "CHUA_DONG_KY; cần phân xử theo nguyên mục, không ký theo hai lối tắt",
        })
    save_tsv(EV/"cr1-audit-96-K2.tsv", k2)
    h5audit = []
    dm = {r["dang"]:r for r in tsv(OE/"dem-h5.tsv")}
    db = {r["dang"]:r for r in tsv(OE/"dem-h5b.tsv")}
    for r in o5:
        if r["loai_H5"] not in {"b","c","d","f"}:
            continue
        vals=[int(r[x]) for x in ("sub_tu","sub_bien_the","web_tu","web_bien_the")]
        base = classify(r["loai_H5"],*vals)
        distinct = classify(r["loai_H5"],int(r["sub_dong_khac_tu"]),int(r["sub_dong_khac_bien_the"]),vals[2],vals[3]) if r["sub_dong_khac_tu"]!="-" else "CHUA_CO"
        h5audit.append({
            "tu":r["tu"],"bien_the":r["bien_the"],"loai_gia_dinh_O":r["loai_H5"],
            "dem_chinh": "/".join(map(str,vals)), "tinh_doc_lap_chinh":base,
            "tinh_doc_lap_dong_khac":distinct, "O_ket_luan":r["ket_luan_H5"],"nguon":r["_ref"],
            "gioi_han": "Chỉ kiểm số với loại O giả định; chưa chứng minh kiểu c/d hay đã đếm đủ dạng phân cách.",
        })
    save_tsv(EV/"cr1-H5-so-doc-lap.tsv",h5audit)
    missing_hnd = tsv(OE/"h7-hnd-cung-khoa.tsv")
    known_hnd = []
    for r in missing_hnd:
        c = d["counts"].get(r["doc_khac_hnd"])
        if c:
            known_hnd.append({
                "tu_chinh":r["tu_chinh"],"doc_khac":r["doc_khac_hnd"],"khoa":r["khoa"],
                "sub_sach":c["sub_sach"],"web_sach":c["web_sach"],"ppm":f"{float(ppm(c)):.9f}",
                "nguon_so_da_co":c["_ref"],"nguon_O_goi_thieu":r["_ref"],
                "ghi_chu":"Không có vai DOC_KHAC không đồng nghĩa không có số đo.",
            })
    save_tsv(EV/"cr1-HND-da-co-so-do.tsv",known_hnd)
    anchors = []
    for w,alt,source in (
        ("bao tử","báo tử","T-dpv2-7"),
        ("bào tử","báo tử","Đối chứng mẫu số, không phải đầu mục của quyết định T-dpv2-7"),
        ("ngoại trừ","ngoại trú","T-dpv2-9: CHO đo nghĩa, không phải K2 theo r"),
        ("con đò","côn đồ","tieu-chi-thong-nhat.md:524"),
        ("đường dẫn","đường đạn","tieu-chi-thong-nhat.md:524"),
        ("mạnh dạn","mảnh đạn","tieu-chi-thong-nhat.md:524"),
        ("thanh thản","thánh thần","tieu-chi-thong-nhat.md:524"),
        ("bảo hành","bạo hành","Đề xuất mới"),
        ("nhàu","nhậu","Đề xuất mới"),
        ("ngọc","ngốc","Đề xuất mới"),
        ("hững hờ","hùng hổ","Còi tương đối dưới 0,3"),
    ):
        a,b=d["counts"].get(w),d["counts"].get(alt)
        if a and b and ppm(a)>0:
            anchors.append({
                "tu":w,"doc_khac":alt,"ppm_tu":f"{float(ppm(a)):.9f}","ppm_doc":f"{float(ppm(b)):.9f}",
                "r":f"{float(ppm(b)/ppm(a)):.9f}","nguon_quyet_dinh":source,
                "nguon_dem":a["_ref"]+";"+b["_ref"],
                "xac_minh":"verified: số toàn chuỗi; không phải tỷ lệ nghĩa đỏ",
            })
    save_tsv(EV/"cr1-tien-le-va-ti-le.tsv",anchors)
    one_k1 = []
    forbidden={r["khoa"]:r for r in d["blocked_keys"] if "K1" in r["ma"]}
    for r in d["opus-counts"]:
        if r["vai_tro"]=="UNG_VIEN" and r["khoa"] in forbidden and len(r["tu"].split())==1:
            one_k1.append({"tu":r["tu"],"khoa":r["khoa"],"ma":forbidden[r["khoa"]]["ma"],
                           "nguon":forbidden[r["khoa"]]["_ref"]+";"+r["_ref"],
                           "ghi_chu":"K1 một khối có thật trong bộ luật/bảng phát hành trước; không suy mọi dạng là nghĩa đỏ."})
    save_tsv(EV/"cr1-K1-mot-khoi-lich-su.tsv",one_k1)
    aset={r["tu_chinh"] for r in a7 if r["muc_K_de_xuat"] in {"K0","K1"}}
    oset=blocked_o
    as5={r["tu"] for r in a5 if r["hanh_dong"]=="DE_NGHI_THAY"}
    os5={r["tu"] for r in o5 if r["hanh_dong"]=="THAY"}
    aina={r["tu_vao_de_xuat"] for r in ar};oina={r["tu"] for r in orepl if r["vai_tro"]=="VAO"}
    aout={r["tu_ra"] for r in ar};oout={r["tu"] for r in orepl if r["vai_tro"]=="RA"}
    result={
        "H7_diff_rows":len(diff7),"H7_original_blocked_A":len(aset),"H7_original_blocked_O":len(oset),
        "H7_blocked_intersection":len(aset&oset),"H7_A_only_blocked":sorted(aset-oset,key=o1),
        "H7_O_only_blocked":sorted(oset-aset,key=o1),
        "H7_keys_both_have_rows":sum(bool(aa[key(w)]) and bool(oo[key(w)]) for w in d["main"]),
        "H7_scope_A_pairs":len(a7),"H7_scope_O_pairs":len(o7),
        "H5_diff_rows":len(diff5),"H5_pair_states":Counter((r["A_v1"]+" → "+r["O_v1"]) for r in diff5),
        "H5_common_out":sorted(as5&os5,key=o1),"H5_A_only_out":sorted(as5-os5,key=o1),"H5_O_only_out":sorted(os5-as5,key=o1),
        "replacement_diff_rows":len(replacement_diff),
        "out_sets":{"A":len(aout),"O":len(oout),"intersection":len(aout&oout)},
        "in_sets":{"A":len(aina),"O":len(oina),"intersection":len(aina&oina)},
        "Opus_K2_new_keys":len(k2),"Opus_K2_new_key_rows":sum(r["so_cap_O"] for r in k2),
        "Opus_K2_one_syllable_rationale_keys":sum(r["ly_do_chi_mot_am_tiet"]=="True" for r in k2),
        "Opus_K2_only_ratio_rationale_keys":sum(r["ly_do_r_duoi_02"]=="True" for r in k2),
        "Opus_K2_old_rows":len(hist),"old_counter_not_named_in_signatures":[r["doc_khac"] for r in hist if r["doc_khac_duoc_nhac_nguyen_mat_chu"]=="False"],
        "Opus_H5_pass_actions":sum(r["hanh_dong"]=="DANG_KY_QUA" for r in o5),
        "HND_marked_missing_but_counted":len(known_hnd),
        "historical_single_block_K1_candidate_rows":len(one_k1),
    }
    save_json(EV/"cr1-summary.json",result)
    frequency_rows=[]
    frequency={}
    for role in ("RA","VAO"):
        vals=[];surface=[]
        for r in orepl:
            if r["vai_tro"]!=role:
                continue
            c=d["counts"][r["tu"]]
            clean=float(ppm(c))
            s=int(c.get("sub_be_mat",c.get("opensub_n")))
            w=int(c.get("web_be_mat",c.get("ccaligned_n")))
            bare=(s/34314528+w/149860716)*500000
            vals.append(clean);surface.append(bare)
            frequency_rows.append({"vai_tro":role,"tu":r["tu"],"ppm_sach":f"{clean:.9f}",
                                   "ppm_be_mat":f"{bare:.9f}","nguon":c["_ref"]+";"+r["_ref"]})
        frequency[role]={"n":len(vals),"median_ppm":statistics.median(vals),
                         "median_surface_ppm":statistics.median(surface),
                         "min_ppm":min(vals),"max_ppm":max(vals)}
    frequency["median_ratio_RA_VAO"]=frequency["RA"]["median_ppm"]/frequency["VAO"]["median_ppm"]
    frequency["note"]="verified: số sạch/bề mặt tách riêng, mẫu số mục 0; không phải hệ số độ quen của con người"
    save_tsv(EV/"cr1-frequency-rows.tsv",frequency_rows)
    save_json(EV/"cr1-frequency.json",frequency)
    inputs=[O/"round-1-analysis.md",O/"sang-loc-h5.tsv",O/"sang-loc-h7.tsv",O/"de-xuat-thay.tsv",
            OE/"sang-loc-h5.py",OE/"sang-loc-h7.py",OE/"de-xuat-thay.py",OE/"dem-h5.py",
            OE/"dem-h5.tsv",OE/"dem-h5b.tsv",OE/"cap-h5b.tsv",OE/"dem-h5.log",OE/"dem-h5b.log",
            OE/"h7-hnd-cung-khoa.py",OE/"h7-hnd-cung-khoa.tsv",OE/"h7-hnd-cung-khoa.log",
            AT/"tieu-chi-thong-nhat.md",AT/"spelling_families.tsv",U/"tap-luat-P2-v4.json",
            U/"chu-ky.tsv",U/"canh-bao-khong-dau.tsv",U/"p7-khau-tru.tsv"]
    snapshot={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    old_snapshot=EV/"cr1-input-hashes.json"
    if old_snapshot.exists():
        assert json.loads(old_snapshot.read_text(encoding="utf-8"))==snapshot,"Đầu vào vòng 1 đã đổi; không ghi đè snapshot."
    else:
        save_json(old_snapshot,snapshot)
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
