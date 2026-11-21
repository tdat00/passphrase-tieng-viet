"""Đối số hợp đồng H5b, phép tính H5 và các điều kiện quyết định của Opus, chỉ trong RAM."""
import ast
import itertools
import json
import unicodedata as ud
from fractions import Fraction

from screen_core import AT, EV, OUT, U, load, o1, ppm, read, save_json, save_tsv, tsv

O=AT/"ho-so"/"opus"/"ra-thay-chinh"
TONE=set("\u0300\u0301\u0303\u0309\u0323")


def signed_h5b(w):
    choices=[]
    for syllable in w.split():
        de=ud.normalize("NFD",syllable)
        tone="".join(c for c in de if c in TONE)
        bare=ud.normalize("NFC","".join(c for c in de if c not in TONE))
        variants=[syllable]
        for onset in ("h","k","l","m","qu","s","t"):
            if bare in (onset+"i",onset+"y"):
                new="y" if bare[-1]=="i" else "i"
                variants.append(onset+ud.normalize("NFC",new+tone))
        choices.append(variants)
    return sorted({" ".join(xs) for xs in itertools.product(*choices)}-{w})


def numeric(a,b,aw,bw):
    return a+b>=20 and aw+bw>=20 and 100*a>=95*(a+b) and 100*aw>=95*(aw+bw)


def main():
    d=load()
    rules=json.loads(read(U/"tap-luat-P2-v4.json"))
    contract=next(x for x in rules["hop_dong"] if x.startswith("H5b:"))
    assert "vần đúng bằng 'i' hoặc 'y'" in contract
    tree=ast.parse(read(O/"evidence"/"de-xuat-thay.py"))
    fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=="h5b")
    ns={"unicodedata":ud,"TONE":TONE}
    exec(compile(ast.Module(body=[fn],type_ignores=[]),"<Opus-h5b-pure>","exec"),ns)
    observed=ns["h5b"]("qua quýt")
    assert observed==["qua quít"] and signed_h5b("qua quýt")==[]
    assert len(signed_h5b("kỹ sĩ"))==3
    measurements={r["dang"]:r for r in tsv(O/"evidence"/"dem-h5b.tsv")}
    comparisons=[]
    for r in tsv(O/"evidence"/"cap-h5b.tsv"):
        a,b=measurements[r["tu"]],measurements[r["bien_the"]]
        vals=[int(a["sub_moi_dong_sach"]),int(b["sub_moi_dong_sach"]),
              int(a["web_dong_khac_sach"]),int(b["web_dong_khac_sach"])]
        raw=[int(a["sub_moi_dong"]),int(b["sub_moi_dong"]),
             int(a["web_dong_khac"]),int(b["web_dong_khac"])]
        unique=[int(a["sub_dong_khac_sach"]),int(b["sub_dong_khac_sach"]),vals[2],vals[3]]
        comparisons.append({
            "tu":r["tu"],"bien_the":r["bien_the"],
            "thuoc_H5b_da_ky":str(r["bien_the"] in signed_h5b(r["tu"])),
            "cong_so_sach_gia_dinh_b":str(numeric(*vals)),
            "cong_so_be_mat_gia_dinh_b":str(numeric(*raw)),
            "cong_so_dong_khac_gia_dinh_b":str(numeric(*unique)),
            "nguon":r["_ref"]+";"+a["_ref"]+";"+b["_ref"],
            "ket_luan":"QUA_H5b_theo_so" if r["bien_the"] in signed_h5b(r["tu"]) else "KHONG_THUOC_b; phải xét họ c/d riêng, không dùng b để loại",
        })
    assert all(r["cong_so_sach_gia_dinh_b"]==r["cong_so_be_mat_gia_dinh_b"]==r["cong_so_dong_khac_gia_dinh_b"]=="True"
               for r in comparisons if r["thuoc_H5b_da_ky"]=="True")
    save_tsv(EV/"cr1-H5b-hop-dong.tsv",comparisons)
    public_pairs=set()
    for r in d["spelling_families"]:
        public_pairs.add((r["chuan"],r["bien_the"]))
    d6pairs={(r["dang_A"],r["dang_B"]) for r in d["d6-ho-chinh-ta"]}
    assert ("bít tết","bíp tết") not in public_pairs
    assert ("bít tết","bíp tết") in d6pairs or ("bíp tết","bít tết") in d6pairs
    h7tree=ast.parse(read(O/"evidence"/"sang-loc-h7.py"))
    h7ns={}
    for stmt in h7tree.body:
        if isinstance(stmt,ast.Assign) and isinstance(stmt.targets[0],ast.Name) and stmt.targets[0].id in {
            "K0","K1_RO","K1_GR","K2_MULTI","K2_SINGLE"}:
            h7ns[stmt.targets[0].id]=ast.literal_eval(stmt.value)
    vf=next(node for node in ast.walk(h7tree) if isinstance(node,ast.FunctionDef) and node.name=="verdict")
    exec(compile(ast.Module(body=[vf],type_ignores=[]),"<Opus-verdict-pure>","exec"),h7ns)
    verdict_rows=[]
    for a,b in (("nhàu","nhậu"),("ngọc","ngốc"),("thuần","thụ án"),("xuân","xử án"),
                ("bảo hành","bạo hành"),("tính khí","tinh khí")):
        pa,pb=ppm(d["counts"][a]),ppm(d["counts"][b])
        verdict,group,why=h7ns["verdict"](a,b,float(pb/pa))
        verdict_rows.append({"tu":a,"doc_khac":b,"khoa_trung_toan_bo":str(d["counts"][a]["khoa"]==d["counts"][b]["khoa"]),
                             "khoi_chinh":len(a.split()),"khoi_doc_khac":len(b.split()),
                             "r":f"{float(pb/pa):.9f}","ket_qua_ham_O":verdict,"ly_do_ham_O":why,
                             "ghi_chu":"Tái chạy đúng hàm thuần của O; không gọi đây là đánh giá ngữ nghĩa được Astra chấp nhận."})
    save_tsv(EV/"cr1-H7-dieu-kien-ma.tsv",verdict_rows)
    proposed=tsv(O/"de-xuat-thay.tsv")
    prior_out={r["tu"] for r in proposed if r["vai_tro"]=="RA"}
    assert "theo" not in prior_out and d["label_by_word"]["theo"]["lop"]=="F"
    hypothetical_out=prior_out|{"theo"}
    slack=77-sum(d["label_by_word"][w]["lop"]=="F" for w in set(d["main"])-hypothetical_out)
    assert slack==1
    conditional={r["tu"] for r in proposed if r["vai_tro"]=="DIEU_KIEN"}
    n_n=sum(d["label_by_word"][w]["lop"]!="F" for w in hypothetical_out|conditional)+12
    queue=[]
    for r in sorted(d["du-phong-phan-loai"],key=lambda r:(int(d["rank_by_word"][r["tu"]]["hang"]),o1(r["tu"]))):
        if r["tang"]=="D" or r["tu"] in {"loằng ngoằng","ngoại trừ","qua quýt"}:
            continue
        if r["lop"]=="F" and slack<=0:
            continue
        queue.append(r)
        if len(queue)>=n_n:
            break
    chosen=queue[:len(hypothetical_out)]
    new_f=77-1+sum(r["lop"]=="F" for r in chosen)
    assert new_f>77
    stats={
        "H5b_actual_new_main_pairs":8,"H5b_surface_and_dedup_pass":True,
        "qua_quyt_signed_variants":signed_h5b("qua quýt"),"qua_quyt_Opus_variants":observed,
        "bip_tet_in_D6_but_not_public_H5":True,
        "multi_syllable_rule_is_extra":True,
        "Opus_K0_map_empty":not h7ns["K0"],
        "conditional_F_counterexample":{
            "case":"thêm theo (F) vào tập ra nếu K2 không được ký",
            "out":len(hypothetical_out),"slack_initial":slack,
            "taken_F_by_existing_loop":sum(r["lop"]=="F" for r in chosen),
            "resulting_main_F":new_f,
            "actual_O38_has_this_failure":False,
            "cause":"de-xuat-thay.py không giảm slack_f khi thêm F và n_n chỉ tính ngăn không-F",
        },
        "protected_data_changed":False,
    }
    save_json(EV/"cr1-contract-summary.json",stats)
    print(json.dumps(stats,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
