"""T7: so kết quả chấm lại của Opus (xep-lai-rtc.tsv) với chương trình độc lập của Astra (ky1-xep-lai-astra.tsv, rổ T_RTC_14).

So từng vai trò (VAO, DU_BI, HM) theo vị trí: từ, hạng toàn rổ, điểm phần trăm. Chạy: python -X utf8 -B so-t7.py -> so-t7.log
"""
from chung import AT, HERE, out_utf8, rd, sha_file, write_lines

out_utf8()
ASTRA = AT / "ho-so" / "astra" / "ra-thay-chinh" / "evidence" / "ky1-xep-lai-astra.tsv"
OPUS = HERE / "xep-lai-rtc.tsv"
o = [(r["vai_tro"], r["thu_tu"], r["tu"], r["hang_moi"], r["diem_100_moi"]) for r in rd(OPUS, mine=True)]
a = [(r["vai_tro"], r["thu_tu"], r["tu"], r["hang_S4"], r["diem_100"]) for r in rd(ASTRA) if r["ro"] == "T_RTC_14"]
lech = [(x, y) for x, y in zip(o, a) if x != y]
log = [f"Opus {OPUS.name} sha256 {sha_file(OPUS)[:16]}; Astra {ASTRA.name} sha256 {sha_file(ASTRA)[:16]}",
       f"số dòng: Opus {len(o)}, Astra {len(a)}; vai trò: " + ", ".join(
           f"{v} {sum(x[0] == v for x in o)}/{sum(x[0] == v for x in a)}" for v in ("VAO", "DU_BI", "HM")),
       f"khớp từng dòng (vai trò, vị trí, từ, hạng, điểm): {len(o) == len(a) and not lech}; lệch {len(lech)}"]
log += [f"  lệch: Opus {x} / Astra {y}" for x, y in lech[:10]]
write_lines(HERE / "so-t7.log", log)
print("\n".join(log))
