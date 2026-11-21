"""Đo riêng khác biệt hạng cũ và S2/S3 tính lại, theo giả thiết của Opus; không viết nghĩa."""
import copy
import json
from collections import Counter

from p6_preview import scorer
from screen_core import AT, EV, OUT, U, key, load, o1, save_json, save_tsv, tsv

O=AT/"ho-so"/"opus"/"ra-thay-chinh"


def main():
    d=load()
    small={}
    for r in tsv(AT/"ho-so"/"discussion"/"bang-khoa-chung.tsv"):
        ws=json.loads(r["ung_vien"])
        ls,ts=json.loads(r["leipzig_so_cau"]),json.loads(r["tatoeba_so_cau"])
        for i,w in enumerate(ws):
            small[w]={"leipzig":ls[i],"tatoeba":ts[i]}
    for stem in ("l2","l2b","l2c","l3"):
        for r in tsv(U/f"{stem}-ung-vien.tsv"):
            small[r["tu"]]={"leipzig":int(r["leipzig_so_cau"]),"tatoeba":int(r["tatoeba_so_cau"])}
    pool={}
    for r in d["xep-hang"]:
        w=r["tu"];c=d["counts"][w]
        pool[w]={"sub_sach":int(c["sub_sach"]),"web_sach":int(c["web_sach"]),**small[w],
                 "nhan":r["nhan"],"lop":r["lop"],"phat_h5d":bool(int(r["phat_h5d"]))}
    score=scorer()
    old=copy.deepcopy(pool)
    assert score(old)==[r["tu"] for r in d["xep-hang"]]
    keep=set("mặt trời|mặt trăng|trái đất|ngân hà|công chúa|hoàng tử|hoàng hậu|mồ hôi|ruồi|gián|chào cờ|ròng rọc|dép lê|bánh chưng".split("|"))
    removed_old={r["tu"] for r in d["nguon-goc-giai-nghia"] if r["trang_thai"]=="LOAI"}
    excluded_reserve={r["tu"] for r in d["du-phong-phan-loai"] if r["tang"]=="D"}|{"loằng ngoằng","ngoại trừ","qua quýt"}
    proposed=tsv(O/"de-xuat-thay.tsv")
    base_out={r["tu"] for r in proposed if r["vai_tro"]=="RA"}
    conditional={r["tu"] for r in proposed if r["vai_tro"]=="DIEU_KIEN"}
    summaries=[]
    all_changes=[]
    for title,extra,mode in (("O38",set(),"CHON_DUOC_MOI_TINH"),
                             ("O42",conditional,"CHON_DUOC_MOI_TINH"),
                             ("O38",set(),"H_QUA_CONG_TINH_D6_LOAI_KHI_CHON"),
                             ("O42",conditional,"H_QUA_CONG_TINH_D6_LOAI_KHI_CHON")):
        rejected=base_out|extra
        score_removed=removed_old if mode=="CHON_DUOC_MOI_TINH" else {"bao tử","bào tử","chạng vạng"}
        active={w:copy.deepcopy(r) for w,r in pool.items() if w not in score_removed|excluded_reserve|rejected}
        order=score(active)
        assert keep<=active.keys()
        selected=set(keep);f=0;r1=0
        for w in order:
            if len(selected)==7776:break
            if w in selected or w in removed_old:continue
            ff=active[w]["lop"]=="F";rr=active[w]["nhan"]=="R1"
            if f+ff>77 or r1+rr>388:continue
            selected.add(w);f+=ff;r1+=rr
        assert len(selected)==7776 and f==77 and r1==0
        old_in={r["tu"] for r in proposed if r["vai_tro"]=="VAO" or extra and r["vai_tro"]=="VAO_NEU_DIEU_KIEN"}
        old_selection=set(d["main"])-rejected|old_in
        assert len(old_selection)==7776
        new_in=selected-set(d["main"])
        new_out=set(d["main"])-selected
        for w in sorted(old_selection ^ selected,key=o1):
            all_changes.append({
                "kich_ban":title,"ro_tinh":mode,"tu":w,"hien_dang_chinh":str(w in d["main"]),
                "trong_de_xuat_O":str(w in old_selection),"sau_tinh_lai":str(w in selected),
                "F_cu":d["rank_by_word"][w]["F"],"F_moi":str(active[w]["F"]) if w in active else "-",
                "diem_100_cu":d["rank_by_word"][w]["diem_100"],
                "diem_100_moi":active[w]["diem_x100"] if w in active else "-",
                "ghi_chu":"Mô phỏng, chưa khép H5/H7; giả thiết loại qua quýt của O chỉ dùng để so phương pháp, không được Astra nhận.",
            })
        summaries.append({
            "scenario":title,"score_universe":mode,"pool":len(active),
            "selection_eligible":len(set(active)-removed_old),"current_out":len(new_out),"new_in":len(new_in),
            "F":f,"R1":r1,
            "difference_from_frozen_rank_list":sorted(old_selection^selected,key=o1),
            "additional_main_out":sorted(new_out-rejected,key=o1),
            "new_entry_only":sorted(new_in-old_in,key=o1),
            "old_proposed_entry_not_selected":sorted(old_in-new_in,key=o1),
            "assumptions":"Chỉ dùng giả thiết O38/O42, không mở HM; bỏ D/hai cổng mở/qua quýt như O; giữ 14 mục bắt buộc. Hai cách hiểu rổ tính S2; không phải phán quyết cuối.",
        })
    if all_changes:
        save_tsv(EV/"cr1-S4-tinh-lai.tsv",all_changes)
    save_json(EV/"cr1-S4-summary.json",{"baseline_exact":True,"simulations":summaries})
    print(json.dumps(summaries,ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
