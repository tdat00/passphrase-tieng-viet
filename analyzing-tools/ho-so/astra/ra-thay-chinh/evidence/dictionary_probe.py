"""Đọc Wiktionary vào bộ nhớ; trên đĩa chỉ ghi URL, revision, hash và trạng thái."""
import argparse
import json
import re
import urllib.parse
import urllib.request

from screen_core import EV, save_tsv, sha


def vietnamese(body, lang):
    if lang == "en":
        hit = re.search(r"(?m)^==\s*Vietnamese\s*==\s*$", body)
        if not hit:
            return ""
        rest = body[hit.end():]
        end = re.search(r"(?m)^==[^=].*?==\s*$", rest)
        return rest[:end.start()] if end else rest
    hit = re.search(r"(?m)^\{\{-(?:vie|vi)-\}\}|^==\s*(?:Tiếng Việt|\{\{langname\|vi\}\})\s*==\s*$", body)
    if not hit:
        return ""
    rest = body[hit.end():]
    sections = {"adj", "adv", "num", "int", "con", "det", "pro", "art", "sym",
                "abb", "exp", "inf", "pre", "ref", "see", "syn", "ant", "rel", "sim", "acr"}
    boundaries = [m.start() for m in re.finditer(r"(?m)^\{\{-([a-z]{2,3})-\}\}", rest)
                  if m.group(1) not in sections]
    boundaries += [m.start() for m in re.finditer(r"(?m)^==[^=].*?==\s*$", rest)]
    return rest[:min(boundaries)] if boundaries else rest


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--lang", default="vi", choices=("vi", "en"))
    p.add_argument("--words", required=True, help="Các đầu mục ngăn bằng |")
    p.add_argument("--tag", required=True)
    args = p.parse_args()
    words = args.words.split("|")
    rows = []
    for start in range(0, len(words), 30):
        query = urllib.parse.urlencode({
            "action": "query", "format": "json", "formatversion": 2, "prop": "revisions",
            "rvprop": "ids|content", "rvslots": "main", "titles": "|".join(words[start:start+30]),
        })
        url = f"https://{args.lang}.wiktionary.org/w/api.php?{query}"
        request = urllib.request.Request(url, headers={"User-Agent": "VietnamesePassphraseReview/1.0 (metadata-only research)"})
        with urllib.request.urlopen(request, timeout=60) as response:
            data = json.load(response)
        assert "error" not in data, data.get("error")
        for page in data["query"]["pages"]:
            title = page["title"]
            revision = page.get("revisions", [{}])[0]
            body = revision.get("slots", {}).get("main", {}).get("content", "")
            vi = vietnamese(body, args.lang)
            redirect = re.match(r"(?i)^#(?:redirect|đổi)\s*\[\[([^\]]+)\]\]", body.strip())
            oldid = revision.get("revid", "-")
            rows.append({
                "tu": title, "lang": args.lang, "revision": oldid,
                "url": f"https://{args.lang}.wiktionary.org/w/index.php?title={urllib.parse.quote(title)}&oldid={oldid}",
                "status": "MISSING" if page.get("missing") else "FOUND",
                "has_vietnamese_section": str(bool(vi)),
                "redirect_target": redirect.group(1) if redirect else "-",
                "sha256_wikitext": sha(body.encode("utf-8")) if body else "-",
                "ngay_doc": "2026-11-21",
            })
            print(f"\n[{title}] oldid={oldid}")
            if not body:
                print("MISSING")
                continue
            if redirect:
                print("REDIRECT", redirect.group(1))
            if not vi:
                print("NO VIETNAMESE SECTION")
                continue
            lines = vi.splitlines()
            keep = [line for line in lines if line.startswith(("# ", "#{{", "#[", "# Như", "# Xem"))
                    or line.startswith("[[")
                    or re.search(r"\{\{(?:alt|alter|syn|vi-noun|vi-verb|vi-adj)|Alternative forms", line)]
            print("\n".join(keep[:10])[:1600])
    save_tsv(EV / f"dictionary-{args.tag}.tsv", sorted(rows, key=lambda x: x["tu"]))


if __name__ == "__main__":
    main()
