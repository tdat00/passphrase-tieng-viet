"""Đối số phiếu HM viết tay, xuất tiền tố theo hạng lịch sử; không viết nghĩa, không tự ký K2."""
import csv
import hashlib
import io
import re
import subprocess
import unicodedata as ud
from collections import Counter, defaultdict
from pathlib import Path

from screen_core import AT, EV, OUT, ROOT, U, key, save_json, save_tsv

PIN = "2cc6aec"
S, W = 34314528, 149860716
ALPHA = set("aăâbcdđeêghiklmnoôơpqrstuưvxy")
TONES = "\u0300\u0309\u0303\u0301\u0323"
PAIRS = {
    "biển": (["biễn"], "h; kiểm cận trên số viết khác"),
    "chỗ ngồi": (["chổ ngồi"], "h/d; lỗi được xác nhận"),
    "tàu điện": (["tầu điện"], "c; phương ngữ của cách viết phương tiện"),
    "bày tỏ": (["bầy tỏ", "bày tõ"], "c/d cùng qua; không suy chuẩn/lỗi từ số"),
    "chuyển đổi": (["chuyễn đổi", "chuyển đỗi", "chuyễn đỗi"], "h; tổ hợp đổi hỏi/ngã"),
    "cụ thể": (["cụ thễ"], "h; cận trên số viết khác"),
    "côn trùng": (["côn trùn"], "sàng lọc, không đăng ký họ chỉ vì sinh được"),
}
H6 = {
    "ngân hàng": "Tài chính thông thường; không đồng nhất với cờ bạc hay quyền lực nhà nước.",
    "khách hàng": "Thành phần giao dịch thông thường, không tự là tội phạm.",
    "cơ quan": "KHONG_DAT H6.3; nghĩa đơn vị nhà nước tồn tại độc lập bên cạnh nghĩa sinh học.",
    "biển": "Các nghĩa địa lý và bảng hiệu không tự là thảm họa hay khẩu hiệu chính trị.",
    "côn trùng": "Tên nhóm động vật, không mặc nhiên H6.10.",
    "cô giáo": "Chức nghiệp; không chọn hay chặn chỉ vì giới của người giữ nghề.",
    "thay thế": "Động tác chung, không tự là cưỡng chế.",
    "chỗ ngồi": "Địa điểm sinh hoạt; không phải chức vị nhà nước.",
    "một mình": "Trạng thái thông thường; không tự là cảm xúc cực đoan.",
    "bí mật": "Việc giữ kín có cả trong đời sống; không đồng nhất với tội phạm/gián điệp.",
    "mùa đông": "Tên mùa, không gán nghĩa thảm họa chỉ do rét.",
    "tàu điện": "Giao thông dân dụng; không suy quân sự từ phương tiện.",
    "cụ thể": "Tính chất phi chuyên biệt; không có nghĩa độc lập thuộc nhóm đỏ.",
    "áp dụng": "Không đồng nhất với việc áp chế hay thi hành hình phạt.",
    "vận hành": "Hoạt động chung của hệ thống; không riêng điều khiển vũ khí.",
    "việc làm": "Sinh hoạt/lao động; đề tài chính sách lao động không phải nghĩa nguyên mục.",
    "chế tạo": "Không tự thêm một tân ngữ thuộc quân sự để gán H6.1.",
    "lực lượng": "T-dpv2-8: quân đội/công an là các tập thể có thể được nói tới, không phải nghĩa chuyên biệt của nguyên mục.",
    "chia": "Cả cách dùng tính toán, phân phần và tên hạt đều không tự thuộc nhóm đỏ.",
    "bánh ngọt": "Thực phẩm; không suy từ rủi ro sức khỏe của khẩu phần ăn.",
    "đánh răng": "Vệ sinh thường ngày, đúng ngoại lệ H6.5.",
    "xe điện": "Phương tiện giao thông, không hàm ý tai nạn/thảm họa.",
    "bày tỏ": "Thể hiện suy nghĩ không tự là la mắng hoặc thao túng.",
    "chuyển đổi": "Chuyển trạng thái nói chung, không mặc nhiên là thay đổi chế độ chính trị.",
    "ngắn gọn": "Đánh giá cách trình bày, không phải phán xét tiêu cực người.",
    "mình": "Đại từ/cơ thể không phải từ tục; loại vì hạn mức, không phải H6.",
    "tương đương": "Quan hệ so sánh thông thường, không nhập nghĩa của tên riêng.",
}
SHORT = {AT: "AT", U: "U", EV: "E", OUT: "A"}


def load(p, pin=False):
    if pin:
        body = subprocess.check_output(["git", "show", f"{PIN}:{p.relative_to(ROOT).as_posix()}"], cwd=ROOT)
        pfx = f"{PIN}@"
    else:
        body, pfx = p.read_bytes(), ""
    label = SHORT.get(p.parent, str(p.parent.relative_to(ROOT)))
    return [dict(r, n=n, ref=f"{pfx}{label}\\{p.name}:{n}") for n, r in enumerate(
        csv.DictReader(io.StringIO(body.decode("utf-8-sig")), delimiter="\t"), 2)]


def idx(p, col="tu"):
    return {r[col]: r for r in load(p)}


def spans(rs):
    if not rs:
        return "-"
    group = defaultdict(set)
    for r in rs:
        file, n = r["ref"].rsplit(":", 1)
        group[file].add(int(n))
    out = []
    for file, indexes in group.items():
        parts = []
        for n in sorted(indexes):
            if parts and n == parts[-1][1] + 1:
                parts[-1][1] = n
            else:
                parts.append([n, n])
        out.append(file + ":" + ",".join(str(a) if a == b else f"{a}–{b}" for a, b in parts))
    return "; ".join(out)


def h1h2(w):
    assert w == w.lower() == ud.normalize("NFC", w)
    sylls = w.split(" ")
    assert 4 <= len(key(w)) <= 12 and 1 <= len(sylls) <= 3 and all(sylls)
    for x in sylls:
        de = ud.normalize("NFD", x)
        tones = [c for c in de if c in TONES]
        bare = ud.normalize("NFC", "".join(c for c in de if c not in TONES))
        assert len(tones) <= 1 and set(bare) <= ALPHA
        prefix = next((p for p in ("ngh","ng","nh","ch","tr","th","kh","ph","gh","qu","gi","b","c","d","đ","g","h","k","l","m","n","r","s","t","v","x") if bare.startswith(p)), "")
        assert not tones or bare[len(prefix):] not in {"oa","oe","uy"}, (w, "H5a")
    return f"NFC; {len(key(w))} chữ/{len(sylls)} khối"


def main():
    hm = idx(AT / "honorable-mentions.tsv")
    rank = idx(U / "xep-hang.tsv")
    wc = lambda s: set(x.strip() for x in s.split("/") if x.strip())
    main = {r["tu"]: r for r in load(AT / "labels.tsv") if r["trang_thai"] == "CHINH"}
    assert len(main) == len({key(w) for w in main}) == 7776
    with (AT / "wordlist.txt").open(encoding="utf-8") as f:
        assert {line.partition("|")[0] for line in f} == set(main)
    reserve = idx(AT / "du-phong-phan-loai.tsv")
    assert len(reserve) == 205 and set(reserve) == set((AT / "du-phong.txt").read_text(encoding="utf-8").splitlines())
    slots = load(U / "ra-thay-chinh-thay-the.tsv", True)
    outgoing = {r["tu"]: r for r in slots if r["vai_tro"] == "RA"}
    candidates = {r["tu"] for r in slots if r["vai_tro"] in {"VAO", "DU_BI"}}
    incoming = {r["tu"] for r in slots if r["vai_tro"] == "VAO"}
    assert len(outgoing) == len(incoming) == 116 and len(candidates) == 118
    assert {r["tu"] for r in slots if r["vai_tro"] == "RA_NEU_CHU_DU_AN_THEO_ASTRA"} == {"cần cù", "tiền lương", "triệu", "bạn thân"}
    occ = {key(w) for w in (main.keys() | reserve.keys())}
    proj = (main.keys() - outgoing.keys()) | incoming
    assert len(proj) == len({key(w) for w in proj}) == 7776
    assert all(main[w]["lop"] != "F" and main[w]["nhan"] == "OK" for w in outgoing)
    assert sum(r["lop"] == "F" for r in main.values()) == 77 and all(r["nhan"] == "OK" for r in main.values())
    assert all(reserve[w]["lop"] != "F" and reserve[w]["ngan"] == "OK_KHONG_F" for w in candidates)
    oldblock = {r["khoa"] for r in load(AT / "blocked_keys.tsv")}
    newblock = {key(w) for w, r in outgoing.items() if r["ma"] in {"K0", "K1"}} | {"baotu", "lamco"}
    assert len(newblock) == 94 and newblock.isdisjoint({key(w) for w in proj})
    familles = load(AT / "spelling_families.tsv")
    rtf = load(U / "ra-thay-chinh-h5.tsv", True)
    rtc_loai = set().union(*(wc(r["tu"]) | wc(r["bien_the"]) for r in rtf if r["trang_thai"] in {
        "DONG_THUAN_THAY", "DONG_THUAN_THAY_CHO_LOAI", "DONG_THUAN_KHONG_CHO_VAO"})) | {"rướn", "dướn"}
    p2a = defaultdict(dict)
    p2o = defaultdict(dict)
    for side, out in (("astra", p2a), ("opus", p2o)):
        for r in load(U / f"cong-{side}-v4.tsv"):
            out[r["ung_vien"]][r["cong"]] = r
    pa, po = (idx(U / f"phieu-{x}.tsv") for x in ("astra", "opus"))
    oldsig = load(U / "chu-ky.tsv")
    pb = load(U / "phan-bien.tsv")
    history = idx(U / "p7-v3-khau-tru-132-theo-P0-astra.tsv")
    d8 = {r["tu"]: r for r in load(AT / "nguon-goc-giai-nghia.tsv") if r["trang_thai"] == "LOAI"}
    logs = [(v, idx(U / f"d6-log-{v}.tsv")) for v in ("v1","v2","v3")]
    manual = idx(EV / "hm1-nhan-astra.tsv")
    head = load(EV / "hm1-doi-chung.tsv")
    sample8 = idx(EV / "hm1-h8-da-doc.tsv")
    sampler = load(EV / "hm1-mau-da-doc.tsv")
    extra = idx(EV / "hm1-nguon-phu.tsv")
    meters = {s: idx(EV / f"hm1-h7-dem-{s}.tsv") for s in ("sub","web")}
    all_ok = sorted((w for w, r in hm.items() if r["nhan_ho_so"] == "OK"), key=lambda w: int(rank[w]["hang"]))
    assert len(hm) == 237 and len(all_ok) == 130 and sum(hm[w]["lop"] == "F" for w in all_ok) == 5
    assert all(hm[w]["ngan_du_kien"] == ("OK_F" if hm[w]["lop"] == "F" else "OK_KHONG_F") and
               abs(float(hm[w]["diem"]) - float(rank[w]["diem"])) < 2e-6 for w in all_ok)
    gatecounts, proposals, audits, h5numbers = Counter(), [], [], []
    k2words, acceptedkeys = set(), set()
    for w in all_ok:
        if len(proposals) >= 25:
            break
        m, k, row, r = hm[w], key(w), manual[w], rank[w]
        assert r["khoa"] == k == m["khoa"] and r["nhan"] == m["nhan_ho_so"] == "OK" and r["lop"] == m["lop"]
        g = row["ket_qua_H"]
        assert g in {"DAT_H_ASTRA","K2_ASTRA_CHO_OPUS","K2_ASTRA_BO_SUNG_CHO_OPUS","BO_H6_3","BO_Q3_F"}
        shape = h1h2(w)
        if len(w.split()) == 3:
            assert m["lop"] == "C" and w == "vòi hoa sen"
        hr = [x for x in head if x["tu"] == w]
        hh = next(x for x in hr if x["cong"] == "H3" and x["doi_chung"] == w)
        assert "Viet" in hh["nguon"] and "W" in hh["nguon"] and hh["nguon_Kaikki"] != "-"
        assert (("WVI:LEX" in m["nguon"]) or ("WEN:LEX" in m["nguon"])) and hh["co_nghia_Kaikki"] == "1"
        assert k not in occ | oldblock | newblock | acceptedkeys and w not in rtc_loai
        for f in familles:
            for name in wc(f["chuan"]) | wc(f["bien_the"]):
                matched = (f["nguon"] == "BAN_DAU" and f" {name} " in f" {w} ") or name == w
                assert not matched, (w, f["chuan"], f["ket_luan"])
        assert not any(x["cong"] == "H5b" for x in hr)
        if w in PAIRS:
            other, why = PAIRS[w]
            bins, refs = {}, []
            for label, src, col in [("sub_sach","sub","clean"),("sub_bo_trung","sub","distinct_clean"),
                                     ("web_sach","web","clean"),("sub_be_mat","sub","all"),("web_be_mat","web","all")]:
                base = meters[src][w]
                b, delta = int(base[col]), sum(int(meters[src][x][col]) for x in other)
                assert b+delta >= 20 and 100*b >= 95*(b+delta) and 100*delta < 5*(b+delta), (w,label,b,delta)
                bins[label] = f"{b}/{delta}"
                refs.extend([base, *(meters[src][x] for x in other)])
            h5numbers.append(dict(tu=w, doi_chung="; ".join(other), danh_gia=why, **bins, nguon=spans(refs)))
        alts, counts = [], []
        sub, web, lz, tt = (int(m[x]) for x in ("sub_sach","web_sach","leipzig","tatoeba"))
        pp0 = 500000 * (sub/S + web/W)
        for x in hr:
            if x["cong"] != "H7":
                continue
            alt, a, b = x["doi_chung"], x["sub"], x["web"]
            if a == "-" or b == "-":
                ca, cb = meters["sub"][alt.lower()], meters["web"][alt.lower()]
                a, b = ca["clean"], cb["clean"]
                counts.extend([ca, cb])
            assert a != "-" and b != "-"
            pp = 500000 * (int(a)/S + int(b)/W)
            alarm = "+".join(k for test,k in ((pp >= 0.3,"≥0,3"),(pp >= pp0,"≥mục")) if test) or "dưới hai mốc"
            alts.append(f"{alt}={a}/{b} ({pp:.4f}; {alarm})")
        # Chữ viết hoa/tên riêng cùng mặt chữ không thay thế H3 chữ thường; đang xét toàn khóa.
        used = [x for x in sampler if x["tu"] in {w, *(v["doi_chung"].lower() for v in hr)}]
        assert sub*10_000_000>=S or web*10_000_000>=W or lz>=2 or tt>=1
        assert sample8[w]["nhan_Astra"]=="DUNG_NGHIA_VIET"
        assert pa[w]["trang_thai"] == po[w]["trang_thai"] == "DONG" and pa[w]["nhan"] == po[w]["nhan"] == "OK"
        assert not any(x["tu"] == w for x in pb)
        assert all(p2a[w][g1]["ket_qua"] == p2o[w][g1]["ket_qua"] == "PASS" for g1 in ("H1","H2","H3","H4","H5","H8"))
        history_tag = history[w]["cong"]
        assert d8[w]["cong_loai"] == history_tag and history_tag.startswith(m["nhom"]) and m["dieu_kien"]
        lgs = [src[w] for v, src in logs if w in src]
        assert lgs and (m["nhom"] != "D6_CUOI" or len(lgs) == 3 and lgs[-1]["ket_qua"] != "PASS")
        old = [x for x in oldsig if x["tu"] == w and x["loai_ky"] == "K2" and x["hieu_luc"] == "CO"]
        if w == "chia":
            assert {x["nguoi_ky"] for x in old} == {"Astra","Opus"}
        else:
            assert p2a[w]["H7"]["ket_qua"] == p2o[w]["H7"]["ket_qua"] == "PASS"
        gatecounts[g] += 1
        if "K2_" in g:
            k2words.add(w)
        aq = int(r["hang"])
        refs = [m, r, *hr, *counts, sample8[w], *used, p2a[w]["TONG"],p2o[w]["TONG"],pa[w],po[w],history[w],d8[w],*lgs,*old]
        if w in extra:
            refs.append(extra[w])
        h5detail = (f"E\\hm1-h5-so.tsv:{len(h5numbers)+1}" if w in PAIRS else "-")
        h5x = "; ".join(x["doi_chung"] for x in hr if x["cong"].startswith("H5")) or "-"
        audits.append(dict(hang_S4=aq, tu=w, khoa=k, H1_H2=shape, H3=hh["nguon"], H4="KHONG_TRUNG",
                           H5="a–h: không trúng họ chờ/loại; cặp cần phân biệt: "+h5x, H5_tinh_lai=h5detail,
                           H6=H6[w], H7_ppm_muc=f"{pp0:.6f}", H7="; ".join(alts) or "KHONG_CO_DOI_CHUNG",
                           ly_do_rieng=row["ly_do"], H8=f"{sub}/{web}/{lz}/{tt}; H8-ID={sample8[w]['id_dong']}",
                           H9="H6.3: phản đối của Astra" if g=="BO_H6_3" else "K2: Astra ký, chờ Opus cho phạm vi hiện tại" if w in k2words else "Không còn phản đối H1–H8 trong hồ sơ Astra",
                           P7_cu=history_tag, Dieu_kien=m["dieu_kien"], ket_qua=g,
                           nguon=spans(refs)))
        if g.startswith("BO_"):
            assert (g == "BO_Q3_F") == (m["lop"] == "F")
            continue
        assert m["lop"] != "F"
        acceptedkeys.add(k)
        proposals.append(dict(thu_tu=len(proposals)+1, tu=w, khoa=k, lop=m["lop"], nhom_hm=m["nhom"], ket_qua_H=g,
                              ly_do=row["ly_do"], bang_chung=f"S4={aq}; điểm={m['diem']}; H8={sub}/{web}/{lz}/{tt}; "
                              f"{m['ref']}; {history[w]['ref']}; E\\hm1-phieu-H.tsv:{len(audits)+1}"
                              +(f"; {h5detail}" if w in PAIRS else "")))
    assert len(proposals)==len(acceptedkeys)==25 and all(x["khoa"] not in occ | oldblock | newblock for x in proposals)
    assert not acceptedkeys & {key(w) for w in proj}
    save_tsv(EV / "hm1-h5-so.tsv", h5numbers)
    save_tsv(EV / "hm1-phieu-H.tsv", audits)
    save_tsv(OUT / "hm-chu-ky-1.tsv", proposals)
    fingerprints = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [
        AT / "honorable-mentions.tsv", AT / "labels.tsv", AT / "du-phong-phan-loai.tsv", AT / "blocked_keys.tsv",
        AT / "spelling_families.tsv", U / "xep-hang.tsv", EV / "hm1-phieu-H.tsv", OUT / "hm-chu-ky-1.tsv"]}
    save_json(EV / "hm1-kiem.json", dict(nguon_quyet_dinh=PIN, hm=len(hm), ok=len(all_ok), r1=len(hm)-len(all_ok),
              ok_khong_F=125, soat_den_hang=audits[-1]["hang_S4"], so_da_soat=len(audits), nhan=dict(gatecounts),
              de_xuat=len(proposals), K2=sorted(k2words), H1_H9_can_Opus=True, moi_D6_D7_D8="CHUA_CHAY",
              loi_cu=dict(Counter(r["nhom_hm"] for r in proposals)), lop=dict(Counter(r["lop"] for r in proposals)),
              F_sau=77, R1_sau=0, khoa_chan_cu=len(oldblock), khoa_chan_moi_kiem=len(newblock),
              giao_2_bang_chan=sorted(oldblock & newblock), chinh=7776, du_phong=205, ra=116, nguon_du_phong=118,
              du_bi_truoc_HM=2, thu_tu_chinh_thuc="CHO_T7_T_RTC_14", sha256=fingerprints))
    print(f"{len(proposals)} HM; {len(audits)} dòng rà; K2={len(k2words)}, hạng cuối={audits[-1]['hang_S4']}.")


if __name__ == "__main__":
    main()
