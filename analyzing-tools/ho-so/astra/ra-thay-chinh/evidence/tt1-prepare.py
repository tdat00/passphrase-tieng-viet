"""Ghim hàng đợi cho phiếu độc lập Astra; không đọc thoa-thuan của Opus."""
import hashlib
import json
from collections import defaultdict

from screen_core import AT, EV, OUT, ROOT, U, load, o1, ppm, save_json, save_tsv, tsv


def main():
    d = load()
    files = [U / f"ra-thay-chinh-{n}.tsv" for n in ("h7", "h5", "thay-the")]
    data = {}
    hashes = {}
    for path in files:
        rows = tsv(path)
        name = path.stem.removeprefix("ra-thay-chinh-")
        data[name] = rows
        hashes[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
        save_tsv(EV / f"tt1-{name}-snapshot.tsv", [
            {**{k: v for k, v in r.items() if k != "_ref"}, "nguon_chung": r["_ref"]} for r in rows
        ])
    queue7 = [r for r in data["h7"] if r["trang_thai"] == "CHO_CAN_CU"]
    k2 = [r for r in data["h7"] if r["trang_thai"] == "DONG_THUAN_GIU_CAN_KY_K2"]
    queue5 = [r for r in data["h5"] if r["trang_thai"] == "CHO_CAN_CU"]
    flags = [r for r in data["thay-the"] if r["vai_tro"] in {"VAO", "DU_BI"} and r["can_soat"] != "-"]
    assert (len(queue7), len(k2), len(queue5), len(flags)) == (46, 194, 27, 11)
    original = tsv(OUT / "h7-sang-loc-1177.tsv") + tsv(OUT / "h7-sang-loc-bo-sung.tsv")
    opus = tsv(AT / "ho-so" / "opus" / "ra-thay-chinh" / "sang-loc-h7.tsv")
    byword = defaultdict(list)
    for r in original:
        byword[r["tu_chinh"]].append(r)
    opairs = defaultdict(list)
    for r in opus:
        if r["de_xuat"] == "K2_DE_XUAT":
            opairs[r["tu_chinh"]].append(r)
    interesting = {"K0", "K1", "K2_DE_NGHI_KHONG_CHAN", "CHO_NGHIA", "CHO_DO"}
    for group, records in (("H7-cho", queue7), ("K2", k2)):
        cards = []
        for r in records:
            w = r["tu_chinh"]
            aa = [x for x in byword[w] if x["muc_K_de_xuat"] in interesting]
            alt_names = {x["doc_khac"] for x in aa} | {x["doc_khac"] for x in opairs[w]}
            if not alt_names:
                alt_names = {x["doc_khac"] for x in byword[w]}
            alt_names = sorted(alt_names, key=o1)
            numbers, reasons, sources = [], [], []
            for alt in alt_names:
                c = d["counts"].get(alt)
                if c:
                    numbers.append(f"{alt}={c['sub_sach']}/{c['web_sach']};ppm={float(ppm(c)):.6f}")
                    sources.append(c["_ref"])
                else:
                    numbers.append(alt + "=CHUA_DO")
                ar = next((x for x in byword[w] if x["doc_khac"] == alt), None)
                if ar:
                    reasons.append(alt + ":" + ar["ly_do"])
                    sources.append(ar["_ref"])
                    if ar.get("bang_chung"):
                        sources.append(ar["bang_chung"])
            cards.append({
                "tu": w, "khoa": r["khoa"], "doi_chung": ";".join(alt_names),
                "so_do": " | ".join(numbers), "y_astra_hien_hanh": r["ly_do_astra"],
                "y_opus_hien_hanh": r["ly_do_opus"],
                "ly_do_theo_doi_chung_v1": " | ".join(reasons),
                "nguon": ";".join([r["_ref"], *sources]),
                "canh_bao": "Mã v1 là lịch sử; không dùng để lật phiếu rd1/rd2 hoặc chữ ký cũ.",
            })
        save_tsv(EV / f"tt1-{group}-review-input.tsv", cards)
    protected = json.loads((EV / "protected-baseline.json").read_text(encoding="utf-8"))
    assert all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h["sha256_bytes"] for p, h in protected.items())
    save_json(EV / "tt1-input-hashes.json", hashes)
    save_json(EV / "tt1-queue-summary.json", {
        "S1": sum(r["trang_thai"] == "TRANH_CHAP" for r in data["h7"]),
        "S2": sum(r["trang_thai"] == "TRANH_CHAP" for r in data["h5"]),
        "S3": 1, "H7_pending": len(queue7), "H5_pending": len(queue5),
        "entrant_flags": len(flags), "K2_pending": len(k2),
        "D_rtc_5": "owner, Discord 2026-11-21 16:58 +07:00; không SA-Fable; hai SA thỏa thuận rồi trình owner",
        "Opus_negotiation_files_read": False, "production_unchanged": len(protected),
    })
    print("Frozen: S1=17 S2=7 S3=1; H7=46 H5=27 flags=11 K2=194. No Opus negotiation file read.")


if __name__ == "__main__":
    main()
