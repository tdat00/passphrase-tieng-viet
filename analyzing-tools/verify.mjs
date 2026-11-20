// Bộ kiểm độc lập bằng JavaScript cho danh sách phát hành (C1–C5, C8), viết riêng với check_wordlist.py.
//   node verify.mjs
// Thoát 1 nếu có lỗi.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const repo = path.dirname(here);
const errors = [];
const fail = (m) => errors.push(m);

// Hàm bỏ dấu giống app (index.html, thong-tin.html)
const stripAccents = (s) => s.normalize("NFD").replace(/\p{M}/gu, "").replace(/đ/g, "d").replace(/Đ/g, "D");
const key = (w) => stripAccents(w).toLowerCase().replaceAll(" ", "");

// O1: mỗi âm tiết thành một khóa (chữ cái theo bảng chữ Việt, rồi thanh), so lần lượt từng âm tiết
const ALPHA = "aăâbcdđeêghiklmnoôơpqrstuưvxy";
const TONE = { "\u0300": 1, "\u0309": 2, "\u0303": 3, "\u0301": 4, "\u0323": 5 };
const syllable = (s) => {
  let tone = 0;
  const base = [...s.normalize("NFD")].filter((c) => (TONE[c] ? ((tone = TONE[c]), false) : true)).join("").normalize("NFC");
  return { letters: [...base].map((c) => ALPHA.indexOf(c)), tone };
};
const compare = (a, b) => {
  const sa = a.split(" ").map(syllable), sb = b.split(" ").map(syllable);
  for (let i = 0; i < Math.min(sa.length, sb.length); i++) {
    const x = sa[i], y = sb[i];
    for (let j = 0; j < Math.min(x.letters.length, y.letters.length); j++) if (x.letters[j] !== y.letters[j]) return x.letters[j] - y.letters[j];
    if (x.letters.length !== y.letters.length) return x.letters.length - y.letters.length;
    if (x.tone !== y.tone) return x.tone - y.tone;
  }
  return sa.length - sb.length;
};

const raw = fs.readFileSync(path.join(here, "wordlist.txt"));
const text = new TextDecoder("utf-8", { fatal: true, ignoreBOM: true }).decode(raw);
if (text.startsWith("\ufeff") || text.includes("\r") || !text.endsWith("\n")) fail("C1: wordlist.txt phải là UTF-8 không BOM, LF, có LF cuối");
if (text.normalize("NFC") !== text) fail("C1: wordlist.txt chưa ở dạng NFC");
const lines = text.slice(0, -1).split("\n");
if (lines.length !== 7776) fail(`C1: có ${lines.length} dòng, cần 7776`);
const pairs = lines.map((l) => l.split("|"));
pairs.forEach((p, i) => { if (p.length !== 2 || !p[1].trim()) fail(`C1: dòng ${i + 1} sai dạng`); });
const words = pairs.map((p) => p[0]);

for (const w of words) {
  const blocks = w.split(" ");
  const ok = blocks.every((b) => b && [...syllable(b).letters].every((i) => i >= 0));
  if (!ok) fail(`C2: '${w}' có kí tự ngoài chữ cái tiếng Việt`);
  const n = key(w).length;
  if (n < 4 || n > 12 || blocks.length > 3) fail(`C2: '${w}' dài ${n} chữ, ${blocks.length} khối`);
}
for (const [name, f] of [["mặt chữ", (w) => w], ["khóa", key], ["viết hoa", (w) => w.charAt(0).toUpperCase() + w.slice(1)]]) {
  const seen = new Set();
  for (const w of words) { const k = f(w); if (seen.has(k)) fail(`C3: trùng ${name}: ${w}`); seen.add(k); }
}
for (let i = 1; i < words.length; i++) if (compare(words[i - 1], words[i]) >= 0) { fail(`C4: sai thứ tự: '${words[i - 1]}' trước '${words[i]}'`); break; }
const groups = Map.groupBy(words, (w) => stripAccents(w)[0].toUpperCase());
let runs = 0;
words.forEach((w, i) => { if (i === 0 || stripAccents(w)[0].toUpperCase() !== stripAccents(words[i - 1])[0].toUpperCase()) runs++; });
if (runs !== groups.size) fail("C4: nhóm chữ cái đầu không liền mạch");

const keys = new Set(words.map(key));
for (const line of fs.readFileSync(path.join(here, "blocked_keys.tsv"), "utf8").trim().split("\n").slice(1)) {
  const k = line.split("\t")[0];
  if (keys.has(k)) fail(`C5: danh sách có khóa bị chặn ${k}`);
}

// C8: tách khối giống cách hai trang đọc dữ liệu
const block = (file) => {
  const t = fs.readFileSync(path.join(repo, file), "utf8");
  return t.match(/<script type="text\/plain" id="wordlist">([\s\S]*?)<\/script>/)[1];
};
const appWords = block("index.html").split(",").map((w) => w.trim()).filter(Boolean);
if (JSON.stringify(appWords) !== JSON.stringify(words)) fail("C8: index.html không khớp wordlist.txt");
const pageRows = block("thong-tin.html").trim().split("\n").map((l) => l.trim());
if (JSON.stringify(pageRows) !== JSON.stringify(lines)) fail("C8: thong-tin.html không khớp wordlist.txt");
const doc = fs.readFileSync(path.join(repo, "WordListAnalyze.md"), "utf8").split("## 10. Danh sách 7.776 từ phát hành")[1] ?? "";
const archived = (doc.split("```text")[1] ?? "").split("```")[0].split(/\r?\n/).filter(Boolean);
if (JSON.stringify(archived) !== JSON.stringify(lines)) fail("C8: mục 10 của WordListAnalyze.md không khớp wordlist.txt");

console.log(`Số từ: ${words.length}; ${Math.log2(words.length).toFixed(2)} bit/từ; ${groups.size} nhóm chữ cái`);
for (const m of errors) console.log("LỖI | " + m);
console.log(`Tổng: ${errors.length} lỗi.`);
process.exit(errors.length ? 1 : 0);
