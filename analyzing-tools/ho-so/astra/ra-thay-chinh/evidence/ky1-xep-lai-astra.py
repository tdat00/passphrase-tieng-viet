"""Đối chứng P6 của SA-Astra. Chỉ đọc dữ liệu Git; không nhập/chạy chương trình của Opus."""
import csv
import hashlib
import io
import itertools
import json
import subprocess
import unicodedata as ud
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

EV = Path(__file__).resolve().parent
ROOT = EV.parents[4]
AT = ROOT / "analyzing-tools"
U = AT / "ho-so" / "unified"
A = EV.parent
O = AT / "ho-so" / "opus" / "ra-thay-chinh"
REV = "91d8ee9"
VOWEL_TONES = "\u0300\u0309\u0303\u0301\u0323"
LETTERS = "aăâbcdđeêghiklmnoôơpqrstuưvxy"
GAIN = {"C": 15, "H": 5, "K": 0, "F": -20}
FIXED = set("mặt trời|mặt trăng|trái đất|ngân hà|công chúa|hoàng tử|hoàng hậu|mồ hôi|ruồi|gián|chào cờ|ròng rọc|dép lê|bánh chưng".split("|"))
SHA = {}


def src(path, rev=REV):
    p = path.relative_to(ROOT).as_posix()
    b = subprocess.check_output(["git", "show", f"{rev}:{p}"], cwd=ROOT)
    SHA[f"{rev}:{p}"] = hashlib.sha256(b).hexdigest()
    return b.decode("utf-8-sig")


def rows(path, rev=REV):
    return [dict(r, line=i) for i, r in enumerate(csv.DictReader(io.StringIO(src(path, rev)), delimiter="\t"), 2)]


def ix(data, col="tu"):
    index = {x[col]: x for x in data}
    assert len(index) == len(data), col
    return index


def write(name, table):
    b = io.StringIO()
    writer = csv.DictWriter(b, fieldnames=table[0], delimiter="\t", lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(table)
    (EV / name).write_bytes(b.getvalue().encode("utf-8"))


@lru_cache(None)
def fold(w):
    return "".join(c for c in ud.normalize("NFD", w.lower()) if not ud.combining(c) and c != " ").replace("đ", "d")


@lru_cache(None)
def syll(s):
    de = ud.normalize("NFD", s)
    return (ud.normalize("NFC", "".join(c for c in de if c not in VOWEL_TONES)),
            next((1 + VOWEL_TONES.index(c) for c in de if c in VOWEL_TONES), 0))


@lru_cache(None)
def o1(w):
    return tuple((tuple(LETTERS.index(c) for c in base), tone) for base, tone in map(syll, w.split()))


@lru_cache(None)
def region(w):
    families = set()
    for base, _ in map(syll, w.split()):
        if base.startswith(("s", "x")):
            families.add(1)
        if base.startswith(("ch", "tr")):
            families.add(2)
        if base.startswith(("d", "gi", "r")):
            families.add(3)
        if base.startswith(("n", "l")) and not base.startswith(("nh", "ng")):
            families.add(4)
        if base.endswith(("c", "t")):
            families.add(5)
        if base.endswith(("n", "ng")):
            families.add(6)
    return min(4, len(families))


def percen(values):
    pos = sorted(v for v in values if v > 0)
    out = {0: Fraction(0)}
    for _, group in itertools.groupby(enumerate(pos, 1), key=lambda x: x[1]):
        taken = list(group)
        out[taken[0][1]] = Fraction(50 * (taken[0][0] + taken[-1][0]), len(pos))
    return out


def cents(n):
    scaled = abs(n) * 100
    return (2*scaled.numerator + scaled.denominator) // (2*scaled.denominator) * (-1 if n < 0 else 1)


def score(info, removed):
    active = {w: r for w, r in info.items() if w not in removed}
    bylen = defaultdict(list)
    for w in active:
        bylen[len(w.split())].append(w)
    base, vals = {}, {}
    for ws in bylen.values():
        dist = [percen(active[w]["measure"][j] for w in ws) for j in range(4)]
        for w in ws:
            observed = active[w]["measure"]
            f = sum(d[observed[j]] for j, d in enumerate(dist)) / 4
            base[w] = f + GAIN[active[w]["lop"]]
            vals[w] = {"F": f}
    for w, r in active.items():
        chunks = w.split()
        flip = " ".join(reversed(chunks))
        second = len(chunks) == 2 and flip != w and flip in base and (
            base[w] < base[flip] or (base[w] == base[flip] and o1(w) > o1(flip)))
        penalty = region(w) + 5*int(r["phat_h5d"]) + 5*(len(fold(w)) > 10) + 3*(len(chunks) == 3) + 5*second
        vals[w].update(G=GAIN[r["lop"]], T=penalty, pts=cents(base[w] - penalty))
    order = sorted(active, key=lambda w: (info[w]["nhan"] != "OK", -vals[w]["pts"], len(fold(w)), o1(w)))
    for n, w in enumerate(order, 1):
        vals[w]["rank"] = n
    return order, vals


def load_inputs():
    stages = ("p6-dau-vao", "l2-nhan-sau-H9-opus", "l2b-nhan-sau-H9-opus", "l2c-nhan-sau-H9-opus", "l3-nhan-sau-H9-opus")
    info = ix([r for stem in stages for r in rows(U / f"{stem}.tsv")])
    assert all(r["nhan"] in {"OK", "R1"} and r["lop"] in GAIN and fold(w) == r["khoa"] for w, r in info.items())
    provenance = rows(AT / "nguon-goc-giai-nghia.tsv")
    old_loses = {r["tu"]: r["cong_loai"] for r in provenance if r["trang_thai"] == "LOAI"}
    # Lỗi D6/D7 cũ không loại mục khỏi rổ chấm.
    for w in old_loses:
        if not old_loses[w].startswith(("D6", "D7")):
            info.pop(w, None)
    obs = {}
    for r in rows(U / "opus-counts.tsv"):
        if r["tu"] not in obs or r["vai_tro"] == "UNG_VIEN":
            obs[r["tu"]] = tuple(int(r[c]) for c in ("sub_sach", "web_sach"))
    small = {}
    for r in rows(AT / "ho-so" / "discussion" / "bang-khoa-chung.tsv"):
        for w, lz, tt in zip(*(json.loads(r[c]) for c in ("ung_vien","leipzig_so_cau","tatoeba_so_cau")), strict=True):
            small[w] = (lz, tt)
    for stem in ("l2", "l2b", "l2c", "l3"):
        for r in rows(U / f"{stem}-ung-vien.tsv"):
            obs.setdefault(r["tu"], (int(r["sub_sach"]), int(r["web_sach"])))
            small[r["tu"]] = (int(r["leipzig_so_cau"]), int(r["tatoeba_so_cau"]))
    for w, r in info.items():
        r["measure"] = (*obs[w], *small[w])
        assert all(type(v) is int and v >= 0 for v in r["measure"])
    return info, old_loses


def filter_and_pick(order, info, remain, retiring, dp, hm, old_loses, authorized):
    f0 = sum(r["lop"] == "F" for r in remain.values())
    r0 = sum(r["nhan"] == "R1" for r in remain.values())
    r_cap = min(388, r0 + sum(r["nhan"] == "R1" for r in retiring.values()))

    def queue(allowed, reopened=False):
        f, rr = f0, r0
        result = []
        for w in order:
            item = info[w]
            if w not in allowed or (w in old_loses and not (reopened and w in authorized)):
                continue
            if f + (item["lop"] == "F") > 77 or rr + (item["nhan"] == "R1") > r_cap:
                continue
            result.append(w)
            if len(result) <= len(retiring):
                f += item["lop"] == "F"
                rr += item["nhan"] == "R1"
        return result

    dlist = queue(dp)
    # Mọi HM được duyệt đều là OK không-F trong đợt này. Mục thứ 26 chỉ dùng đối chứng.
    hm_eligible = [w for w in order if w in hm and hm[w]["nhan_ho_so"] == "OK"
                   and not (info[w]["lop"] == "F" and f0 == 77)]
    hm_approved = queue(set(hm_eligible) & authorized, True)
    assert hm_approved == hm_eligible[:25]
    chosen = set(remain) | set(dlist[:len(retiring)])
    assert len(chosen) == len({fold(w) for w in chosen}) == 7776 and FIXED <= chosen
    f = sum(info[w]["lop"] == "F" for w in chosen)
    rr = sum(info[w]["nhan"] == "R1" for w in chosen)
    assert f <= 77 and rr <= r_cap
    return {"VAO": dlist[:len(retiring)], "DU_BI": dlist[len(retiring):], "HM": hm_approved}, (f, rr), hm_eligible[25]


def main():
    assert percen([0,5,5,15]) == {0:0,5:50,15:100} and percen([9]) == {0:0,9:100}
    assert cents(Fraction(1005,1000)) == 101 and cents(Fraction(-1005,1000)) == -101
    info, old_loses = load_inputs()
    before, base = score(info, set())
    locked = rows(U / "xep-hang.tsv")
    assert len(locked) == 10133 and before == [r["tu"] for r in locked]
    for r in locked:
        w = r["tu"]
        v = base[w]
        assert (v["rank"], v["pts"], v["T"], v["G"]) == tuple(int(r[c]) for c in ("hang","diem_100","T","G")), w
        assert abs(v["F"]-Fraction(r["F"])) <= Fraction(1,2_000_000), w
    mainlist = {r["tu"]:r for r in rows(AT / "labels.tsv") if r["trang_thai"] == "CHINH"}
    dp = ix(rows(AT / "du-phong-phan-loai.tsv"))
    hm = ix(rows(AT / "honorable-mentions.tsv"))
    approved = {r["tu"] for r in rows(A / "hm-chu-ky-1.tsv")}
    h7 = rows(U / "ra-thay-chinh-h7.tsv")
    h5 = rows(U / "ra-thay-chinh-h5.tsv")
    out7 = {r["tu_chinh"]: ("K1" if r["trang_thai"] == "CHU_DU_AN_THAY" else r["astra"])
            for r in h7 if r["trang_thai"] in {"CHU_DU_AN_THAY", "DONG_THUAN_THAY"}}
    out5 = {r["tu"] for r in h5 if r["trong_chinh"] == "CO" and r["trang_thai"] in {"DONG_THUAN_THAY", "DONG_THUAN_THAY_CHO_LOAI"}}
    assert not (out5 & out7.keys())
    out = out5 | out7.keys()
    oldblock = {r["khoa"] for r in rows(AT / "blocked_keys.tsv")}
    blocks = {fold(w):(w, k, "H7 chính") for w, k in out7.items()}
    blocks.update(baotu=("bao tử", "K1", "T-rtc-1/T-dpv2-7"), lamco=("làm cỗ", "K1", "T-rtc-17"))
    assert not (oldblock & blocks.keys())
    write("ky1-khoa-chan.tsv", [dict(khoa=k, ma=v[1], tu_doi_chieu=v[0], can_cu=v[2]) for k,v in sorted(blocks.items())])
    write("ky1-tu-ra.tsv", [dict(tu=w, khoa=fold(w), ma=out7.get(w,"H5")) for w in sorted(out, key=o1)])
    remain = {w:r for w,r in mainlist.items() if w not in out}
    retiring = {w:mainlist[w] for w in out}
    assert len(retiring) == 116 and all(r["nhan"]=="OK" and r["lop"]!="F" for r in retiring.values())
    rtc_cards = rows(A / "khep-muc-mo-1.tsv")
    rtc_flags = {r["tu_hoac_khoa"] for r in rtc_cards if r["loai"]=="CO_TU_VAO" and r["ky_astra"]=="N"}
    hm_rejected = {r["tu"] for r in rows(EV / "hm1-phieu-H.tsv") if r["ket_qua"].startswith("BO_H")}
    reserve_gate = {w for w,r in dp.items() if r["tang"]=="D" or r["trang_thai_h"].startswith("CHO_")}
    reserve_gate |= {r["tu"] for r in h5 if r["trang_thai"]=="DONG_THUAN_KHONG_CHO_VAO"}
    excluded_declared = out | reserve_gate | rtc_flags | hm_rejected
    dpv2 = rows(U / "du-phong-v2-honorable-mentions.tsv")
    prior_failed = {r["tu"] for r in dpv2 if r["ket_luan_nhap"] in ("LOAI_K1","NGOAI_HM_CHO_H5")}
    failed_keys = {w for w,r in info.items() if r["khoa"] in (oldblock | blocks.keys())}
    # Kiểm cả dạng kia của các họ không qua, không chỉ dạng đại diện.
    h5_forms = {v.strip() for r in h5 if r["trang_thai"] in {"DONG_THUAN_THAY","DONG_THUAN_THAY_CHO_LOAI","DONG_THUAN_KHONG_CHO_VAO"}
                for col in ("tu","bien_the") for v in r[col].split("/")}
    h5_forms |= {v.strip() for r in h5 if r["trang_thai"] == "DONG_THUAN_QUA"
                 for v in r["bien_the"].split("/")}
    strict_extra = (failed_keys | prior_failed | h5_forms) & (info.keys() - excluded_declared)
    assert len(excluded_declared & info.keys()) == 128
    declarations = {"RO_MUC_6": excluded_declared, "T_RTC_14": excluded_declared | strict_extra}
    picked, measures, report = {}, {}, {}
    for mode, denied in declarations.items():
        ranking, vals = score(info, denied)
        selection, (f, rr), next_hm = filter_and_pick(ranking, info, remain, retiring, dp, hm, old_loses, approved)
        if mode=="T_RTC_14":
            assert not ({fold(w) for w in ranking} & (oldblock | blocks.keys())) and not (prior_failed & set(ranking))
        picked[mode], measures[mode] = selection, vals
        report[mode] = {"so_muc_cham":len(ranking), "bam_hang_LF":hashlib.sha256(("\n".join(ranking)+"\n").encode()).hexdigest(),
                        "d6_d7_cu_con_trong_ro":len(set(old_loses) & set(ranking)), "F":f,"R1":rr,"HM_ke":next_hm}
    # Chỉ đọc kết quả Opus sau khi đã tính và chọn xong cả hai rổ.
    op = rows(O / "evidence" / "xep-lai-rtc.tsv")
    unified = rows(U / "ra-thay-chinh-thay-the.tsv")
    compare_ra = {r["tu"]:r["ma"] for r in unified if r["vai_tro"]=="RA"}
    assert compare_ra == {**dict.fromkeys(out5,"H5"), **out7}
    expectedblocks = {fold(w):k for w,k in compare_ra.items() if k != "H5"} | {"baotu":"K1","lamco":"K1"}
    assert {k:v[1] for k,v in blocks.items()} == expectedblocks
    oldpos = {r["tu"]:int(r["thu_tu"]) for r in unified if r["vai_tro"] in {"VAO","DU_BI"}}
    table, diffs = [], []
    for mode in declarations:
        metrics = {}
        for role, ws in picked[mode].items():
            peer = sorted((r for r in op if r["vai_tro"]==role), key=lambda r:int(r["thu_tu"]))
            byword = ix(peer)
            other = [r["tu"] for r in peer]
            s4_old = [r["tu"] for r in sorted((r for r in unified if r["vai_tro"]==role),key=lambda r:int(r["thu_tu"]))]
            metrics[role] = {"N":len(ws),"cung_tap_Opus":set(ws)==set(other),"vi_tri_khac_Opus":sum(x!=y for x,y in itertools.zip_longest(ws,other)),
                             "vi_tri_khac_TSV_hang_cu":sum(x!=y for x,y in itertools.zip_longest(ws,s4_old)),
                             "hang_toan_ro_khac":sum(measures[mode][w]["rank"]!=int(byword[w]["hang_moi"]) for w in ws if w in byword),
                             "diem_100_khac":sum(measures[mode][w]["pts"]!=int(byword[w]["diem_100_moi"]) for w in ws if w in byword)}
            for i,w in enumerate(ws,1):
                v=measures[mode][w]
                peerrow=byword.get(w,{})
                tbl=dict(ro=mode, vai_tro=role, thu_tu=i, tu=w, khoa=fold(w), hang_S4=v["rank"], diem_100=v["pts"],
                         F_chinh_xac=str(v["F"]), G=v["G"], T=v["T"], thu_tu_Opus=peerrow.get("thu_tu","-"),
                         hang_Opus=peerrow.get("hang_moi","-"), diem_100_Opus=peerrow.get("diem_100_moi","-"))
                table.append(tbl)
                if mode=="T_RTC_14" and (i>len(other) or w!=other[i-1]):
                    diffs.append(dict(vai_tro=role, vi_tri=i, Astra=w, Opus=other[i-1] if i<=len(other) else "-"))
        report[mode]["doi_chieu"] = metrics
        report[mode]["du_bi"] = picked[mode]["DU_BI"]
        report[mode]["so_cho_doi_trong_118_so_voi_cu"] = sum(oldpos[w]!=i for i,w in enumerate(picked[mode]["VAO"]+picked[mode]["DU_BI"],1))
    write("ky1-xep-lai-astra.tsv",table)
    t7 = all(r["cung_tap_Opus"] and not any(r[k] for k in ("vi_tri_khac_Opus","hang_toan_ro_khac","diem_100_khac"))
             for r in report["T_RTC_14"]["doi_chieu"].values())
    wrap = {"commit":REV, "T7_khop_Tren_ro_qua_H":t7, "co_so_nguon":len(info), "co_so_S4_F_G_T_diem_100_khop":True,
            "tu_ra":len(out), "tu_ra_theo_cong":dict(Counter(compare_ra.values())), "khoa_chan_moi":len(blocks),
            "loai_them_de_dung_H":{w:{"hang_cu":base[w]["rank"],"dong_dpv2":next((r["line"] for r in dpv2 if r["tu"]==w),None)}
                                    for w in sorted(strict_extra,key=o1)},
            "ket_qua":report, "vi_tri_khac_Opus_tren_ro_dung_H":diffs, "sha256_blob_dau_vao":SHA}
    (EV / "ky1-xep-lai-astra.json").write_bytes((json.dumps(wrap,ensure_ascii=False,indent=2)+"\n").replace("\n","\r\n").encode())
    print("Gốc:",len(info),"; RA:",len(out),"; chặn:",len(blocks),"; thêm ngoài rổ mục 6:", sorted(strict_extra))
    for mode,m in report.items():
        print(mode,m["so_muc_cham"],[(role,x["vi_tri_khac_Opus"],x["hang_toan_ro_khac"],x["diem_100_khac"]) for role,x in m["doi_chieu"].items()],m["du_bi"])
    if diffs:
        print("Chỗ đổi:",[(x["vi_tri"],x["Astra"],x["Opus"]) for x in diffs][:14])
    return 0 if t7 else 1


if __name__=="__main__":
    raise SystemExit(main())
