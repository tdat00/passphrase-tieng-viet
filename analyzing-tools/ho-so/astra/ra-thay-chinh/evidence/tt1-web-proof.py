"""Metadata nguồn web đã đọc; không lưu HTML, lời từ điển hoặc văn bản bách khoa."""
import hashlib
import json
import urllib.parse
import urllib.request

from screen_core import EV, save_tsv


def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": "VietnameseWordlistReview/1.0"})
    with urllib.request.urlopen(request, timeout=40) as response:
        return response.read()


def main():
    rows = []
    for word, fact in (
        ("theo rõi", "web_fetch xác nhận nhãn không chuẩn; quy về theo dõi"),
        ("dun", "web_fetch xác nhận nghĩa động tác đẩy/thúc, không phải đầu mục giun đã xét"),
        ("rí rỏm", "web_fetch xác nhận nét hài hước tế nhị; không có nhãn biến thể của dí dỏm trong trang đã đọc"),
        ("đá gà", "web_fetch xác nhận hoạt động chọi gà, thường gắn cá cược"),
    ):
        url = f"https://vdict.com/{urllib.parse.quote(word)},3,0,0.html"
        body = get(url)
        rows.append({"tu": word, "nguon": "VDict", "url": url, "revision": "-",
                     "sha256_response": hashlib.sha256(body).hexdigest(),
                     "ket_qua_kiem": fact, "source_text_saved": False})
    params = urllib.parse.urlencode({
        "action": "query", "format": "json", "formatversion": 2, "titles": "Chọi gà",
        "redirects": 1, "prop": "extracts|revisions", "exintro": 1, "explaintext": 1,
        "rvprop": "ids",
    })
    body = get("https://vi.wikipedia.org/w/api.php?" + params)
    page = json.loads(body)["query"]["pages"][0]
    revision = page["revisions"][0]["revid"]
    intro = page.get("extract", "")
    print(page["title"], "revision", revision, intro.split("\n\n", 1)[0][:700])
    rows.append({"tu": "đá gà", "nguon": "Wikipedia vi", "revision": revision,
                 "url": "https://vi.wikipedia.org/w/index.php?oldid=" + str(revision),
                 "sha256_response": hashlib.sha256(body).hexdigest(),
                 "ket_qua_kiem": "Đã đọc phần mở đầu; đối chứng toàn hoạt động, không suy từ tiếng gà",
                 "source_text_saved": False})
    save_tsv(EV / "tt1-web-sources.tsv", rows)
    print("Saved metadata only; no source text retained.")


if __name__ == "__main__":
    main()
