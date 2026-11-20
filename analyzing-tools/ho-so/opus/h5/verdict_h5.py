#!/usr/bin/env python3
"""Tính kết luận H5 từ h5/counts.json; in bảng so sánh và ghi h5/verdicts.json."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(HERE, "counts.json"), encoding="utf-8"))


def grp(forms, src, kind):
    return sum(C["counts"][f][src][kind] for f in forms)


def verdict(t, a_sub, b_sub, a_web, b_web):
    ts, tw = a_sub + b_sub, a_web + b_web
    if t == "e":
        return "CHO_NGHIA"
    if t == "g":
        return "QUA_H5G"
    if t in ("b", "c", "f"):
        if ts < 20 or tw < 20:
            return "LOAI_THIEU_DU_LIEU"
        if 100 * a_sub >= 95 * ts and 100 * a_web >= 95 * tw:
            return "QUA_RIENG_H5"
        if 100 * b_sub >= 95 * ts and 100 * b_web >= 95 * tw:
            return "QUA_RIENG_H5_DANG_KIA"
        return "LOAI_CANH_TRANH"
    if t == "d":
        dom = [(a, b) for a, b in ((a_sub, b_sub), (a_web, b_web)) if a + b >= 20]
        if any(10 * b >= a + b for a, b in dom):
            return "LOAI_LOI"
        if any(20 * b >= a + b for a, b in dom):
            return "TRU_DIEM"
        if not dom:
            return "QUA_RIENG_H5_THIEU_DU_LIEU"
        return "QUA_RIENG_H5"
    raise ValueError(t)


def pct(b, a):
    return f"{100 * b / (a + b):.1f}" if a + b else "-"


def main():
    out = []
    for A, B, t in C["pairs"]:
        r = {"A": A, "B": B, "loai": t}
        for kind in ("all", "all_clean", "dist", "dist_clean"):
            r[kind] = [grp(A, "sub", kind), grp(B, "sub", kind), grp(A, "web", kind), grp(B, "web", kind)]
        s = r["all_clean"][:2] + r["dist_clean"][2:]          # chính: phụ đề mọi dòng, web dòng khác nhau, đã lọc vắt từ
        raw = r["all"][:2] + r["dist"][2:]                     # chỉ tách dấu câu, chưa lọc vắt từ
        sens = r["dist_clean"]                                 # độ nhạy: phụ đề chỉ dòng khác nhau
        r["main"], r["raw"], r["sens"] = s, raw, sens
        r["v_main"], r["v_raw"], r["v_sens"] = verdict(t, *s), verdict(t, *raw), verdict(t, *sens)
        out.append(r)
    json.dump(out, open(os.path.join(HERE, "verdicts.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if "--quiet" in sys.argv:
        return
    for r in out:
        a, b, c, d = r["main"]
        ra, rb, rc, rd = r["raw"]
        flag = ""
        if r["v_main"] != r["v_raw"]:
            flag += " [đổi do lọc vắt từ: " + r["v_raw"] + "]"
        if r["v_main"] != r["v_sens"]:
            flag += " [độ nhạy dòng khác nhau: " + r["v_sens"] + "]"
        print(f"{'/'.join(r['A'])[:22]:22s} {'/'.join(r['B'])[:26]:26s} {r['loai']} "
              f"sub {a}/{b} ({pct(b, a)}%; thô {ra}/{rb}) web {c}/{d} ({pct(d, c)}%; thô {rc}/{rd}) -> {r['v_main']}{flag}")


if __name__ == "__main__":
    main()
