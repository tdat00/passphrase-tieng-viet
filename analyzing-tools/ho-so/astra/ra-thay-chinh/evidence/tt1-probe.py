"""Đọc nguồn phục vụ thỏa thuận ở RAM; chỉ lưu metadata/quan hệ đầu mục."""
import argparse
import hashlib
import json
import re
import urllib.parse
import urllib.request

from dictionary_probe import vietnamese as old_vietnamese
from screen_core import EV, save_tsv

GROUPS = {
    "critical": "mèo mỡ|mó máy|chổng lái|ăn đút|ăn bĩnh|bạo quân|báo tang|cầu kinh|cầu hồn|dằn mặt|liệm|phiện|tự ải|hố tiểu|mất kinh|cô đầu|bát tiên",
    "pending": "áo ngự|báng|bẽ mặt|bê bối|căn cứ|chàm|chăn dắt|chầu|chủng|chứng|cô đồng|cơ động|công đoàn|còng|cuồng|cưỡng|điểm nhãn|diễu hành|đình|đổ bác|động dục|động đực|ghèn|hở hang|hoàng đạo|hoảng sợ|khạc|khuỵ|làm khổ|lôi thôi|mất nước|nang|ngập|nghẻo|niệu|nòng|ống thở|quyền|ranh|rúng động|thiêu|thỉnh|tịch|tiên lượng|tinh tử|tong|tông|tống|trận|triều|truồng|trượng|vật vã",
    "spelling": "bản hiệu|cột mốt|hạt giẻ|loằng nhoằng|lòng dòng|nuốt trửng|theo rõi|thư dãn|sà bông|bộc phát|bội phát|bột phát|dí dỏm|rí rỏm|giỡn|rỡn|giun|dun|lăn tăn|lăm tăm|lon ton|long tong|ọp ẹp|ọt ẹt|rậm rạp|giậm giạp|ròng rã|ròn rã|ru rú|giu giú|sền sệt|sềnh sệch|tép riu|tép diu|xanh|sanh|hì hục|hì hụi|qua quýt|qua quít",
    "entrants": "làm cỏ|thay lòng|màng màng|xoành xoạch|xành xạch|xoàn xoạt|thụp|chụp|thụt|loáng thoáng|loáng choáng|rướn|dướn|rướm|xầm xì|sầm sì|dưa đỏ|thang độ",
    "followup": "ngọng|thâm hiểm|cắn cấu",
}


def vietnamese(body, lang):
    if lang == "en":
        return old_vietnamese(body, lang)
    hit = re.search(r"(?m)^\{\{-(?:vie|vi)-\}\}|^==\s*(?:Tiếng Việt|\{\{langname\|vi\}\})\s*==\s*$", body)
    if not hit:
        return ""
    rest = body[hit.end():]
    sections = {"adj", "adv", "num", "int", "con", "det", "pro", "art", "sym",
                "abb", "exp", "inf", "pre", "ref", "see", "syn", "ant", "rel",
                "sim", "acr", "dfn", "alt", "pos"}
    boundaries = [m.start() for m in re.finditer(r"(?m)^\{\{-([a-z]{2,3})-\}\}", rest)
                  if m.group(1) not in sections]
    boundaries += [m.start() for m in re.finditer(r"(?m)^==[^=].*?==\s*$", rest)]
    return rest[:min(boundaries)] if boundaries else rest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("group", choices=GROUPS)
    args = parser.parse_args()
    words = GROUPS[args.group].split("|")
    rows, memory = [], {}
    for lang in ("vi", "en"):
        for start in range(0, len(words), 35):
            query = urllib.parse.urlencode({
                "action": "query", "format": "json", "formatversion": 2, "prop": "revisions",
                "rvprop": "ids|content", "rvslots": "main", "titles": "|".join(words[start:start + 35]),
            })
            req = urllib.request.Request(f"https://{lang}.wiktionary.org/w/api.php?{query}",
                                         headers={"User-Agent": "VietnameseWordlistReview/1.0"})
            with urllib.request.urlopen(req, timeout=40) as response:
                data = json.load(response)
            assert "error" not in data, data.get("error")
            for page in data["query"]["pages"]:
                title = page["title"]
                revision = (page.get("revisions") or [{}])[0]
                body = revision.get("slots", {}).get("main", {}).get("content", "")
                part = vietnamese(body, lang)
                rev = revision.get("revid", "-")
                definitions = [s for s in part.splitlines() if re.match(r"^#{1,2}[^#*:]", s)]
                aliases = re.findall(r"\{\{(?:alt form|alternative form of|alt spelling|alternative spelling of)\|vi\|([^|}]+)", part, re.I)
                aliases += re.findall(r"\{\{like-entry\|([^|}]+)", part, re.I)
                aliases += re.findall(
                    r"(?m)^#?\s*(?:\[\[(?:Như|như)(?:\|[^\]]+)?\]\]|Như|như|Nghĩa như)\s+\[\[([^\]|]+)",
                    part,
                )
                redir = re.match(r"(?i)^#(?:redirect|đổi)\s*\[\[([^\]]+)\]\]", body.strip())
                alias_text = ";".join(sorted(set(aliases))) or "-"
                rows.append({
                    "tu": title, "lang": lang, "revision": rev,
                    "status": "MISSING" if page.get("missing") else "FOUND",
                    "co_phan_tieng_Viet": bool(part), "dau_muc_bien_the_dan_den": alias_text,
                    "redirect_target": redir.group(1) if redir else "-",
                    "sha256_wikitext": hashlib.sha256(body.encode("utf-8")).hexdigest() if body else "-",
                    "url": f"https://{lang}.wiktionary.org/w/index.php?title={urllib.parse.quote(title)}&oldid={rev}",
                })
                memory[(title, lang)] = (definitions, alias_text, rev, bool(body), redir.group(1) if redir else "-")
    for word in words:
        vi, en = memory.get((word, "vi")), memory.get((word, "en"))
        preferred = vi if vi and vi[0] else en if en and en[0] else vi or en
        lang = "vi" if preferred is vi else "en"
        if preferred and preferred[0]:
            deep = word in {"chàm", "nang", "nòng", "cưỡng", "chứng", "quyền", "trận", "tông", "triều", "thỉnh"}
            brief = " / ".join(preferred[0][:6 if deep else 2])[:700 if deep else 330]
            print(f"{word} [{lang}:{preferred[2]}] {brief}")
        else:
            print(f"{word}: no simple Vietnamese definition in fetched pages")
        for language, info in (("vi", vi), ("en", en)):
            if info and (info[1] != "-" or info[4] != "-"):
                print(f"  {language}: aliases={info[1]}; redirect={info[4]}")
    save_tsv(EV / f"tt1-dictionary-{args.group}.tsv", rows)
    print(f"Metadata/relations only: {len(rows)} records; no dictionary text saved.")


if __name__ == "__main__":
    main()
