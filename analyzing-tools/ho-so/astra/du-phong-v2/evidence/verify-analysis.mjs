// Kiểm độc lập khóa/cổng hình thức của hai bảng phân tích; không thay bộ kiểm phát hành.
import fs from "node:fs";
import path from "node:path";
import assert from "node:assert/strict";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const out = path.dirname(here);
const root = path.resolve(here, "..", "..", "..", "..", "..");
const tools = path.join(root, "analyzing-tools");
const key = (w) => w.normalize("NFD").replace(/\p{M}/gu, "").replace(/đ/gu, "d").replace(/Đ/gu, "D").toLowerCase().replaceAll(" ", "");
const lines = (file) => fs.readFileSync(file, "utf8").trimEnd().split(/\r?\n/u);
const table = (file) => {
  const [header, ...body] = lines(file);
  const names = header.split("\t");
  return body.map((line) => {
    const values = line.split("\t");
    assert.equal(values.length, names.length);
    return Object.fromEntries(names.map((name, i) => [name, values[i]]));
  });
};
const main = lines(path.join(tools, "wordlist.txt")).map((s) => s.split("|")[0]);
const originalReserve = lines(path.join(tools, "du-phong.txt"));
const reserve = table(path.join(out, "du-phong-phan-loai.tsv"));
const honorable = table(path.join(out, "honorable-mentions.tsv"));
assert.deepEqual(reserve.map((r) => r.tu), originalReserve);
assert.equal(reserve.length, 205);
assert.equal(honorable.length, 200);
const blocked = new Set(table(path.join(tools, "blocked_keys.tsv")).map((r) => r.khoa));
const allKeys = new Set(main.map(key));
assert.equal(allKeys.size, 7776);
const allowed = new Set("aăâbcdđeêghiklmnoôơpqrstuưvxy");
for (const row of [...reserve, ...honorable]) {
  const word = row.tu;
  assert.equal(word.normalize("NFC"), word);
  assert.equal(word.toLowerCase(), word);
  const parts = word.split(" ");
  assert(parts.length >= 1 && parts.length <= 3);
  for (const part of parts) {
    const bare = part.normalize("NFD").replace(/[\u0300\u0309\u0303\u0301\u0323]/gu, "").normalize("NFC");
    assert(bare.length > 0 && [...bare].every((c) => allowed.has(c)));
  }
  const k = key(word);
  assert.equal(k, row.khoa);
  assert(k.length >= 4 && k.length <= 12);
  assert.equal(key(word[0].toUpperCase() + word.slice(1)), k);
  assert(!blocked.has(k));
  assert(!allKeys.has(k));
  allKeys.add(k);
}
assert.equal(allKeys.size, 8181);
console.log("PASS: 205 dự phòng + 200 honorable mentions; H1/H2 số học/H4/khóa chặn độc lập, 8.181 khóa duy nhất kể cả chính.");
