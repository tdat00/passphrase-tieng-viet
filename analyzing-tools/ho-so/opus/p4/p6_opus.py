"""P6 phía Opus: S2–S4, Q1–Q4, cửa sức chứa C13, danh sách chính 7.776 và dự phòng 300.

Viết lại từ bộ tiêu chí đã ký (mục 3, 4, 6, 8.1 P6) và các quy ước đã thống nhất trong trao-doi (002/018/040/043/045/049/050/052).
Đầu vào:
  U\\p4-nhan-sau-H9-opus.tsv   tập được nhận sau H9 (nhãn gộp, lớp tác nghiệp, phat_h5d)
  U\\ket-qua-chon.tsv          kết quả P5 chung (khoa, chon); nếu chưa có thì dùng U\\p5-ket-luan-opus.tsv
  U\\bang-khoa-chung.tsv       số đếm bốn kho (sub_sach, web_sach, Leipzig, Tatoeba) và số đếm bề mặt
Đầu ra (U): xep-hang.tsv, danh-sach-chon.txt, du-phong.txt, bao-cao-suc-chua.md, bao-cao-chi-bao.md, p6-so-opus.json
Chế độ dự phòng: --du-phong chat (dự phòng R1 chỉ thay R1) | han-muc (thay được mọi suất miễn giữ Q2, Q3).
"""
import argparse, csv, hashlib, io, json, sys, unicodedata as ud
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
U = Path(__file__).resolve().parents[2] / 'unified'
TARGET, BACKUP, QF, QR = 7776, 300, 77, 388
GVAL = {'C': 15, 'H': 5, 'K': 0, 'F': -20}
KEEP = ['mặt trời', 'mặt trăng', 'trái đất', 'ngân hà', 'công chúa', 'hoàng tử', 'hoàng hậu',
        'mồ hôi', 'ruồi', 'gián', 'chào cờ', 'ròng rọc', 'dép lê', 'bánh chưng']
LETTERS = 'a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y'.split()
LIDX = {c: i for i, c in enumerate(LETTERS)}
TONE = {'\u0300': 1, '\u0309': 2, '\u0303': 3, '\u0301': 4, '\u0323': 5}  # huyền hỏi ngã sắc nặng


def tsv(p):
    with open(p, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def fold(w):
    s = ''.join(c for c in ud.normalize('NFD', w.lower()) if not ud.category(c).startswith('M'))
    return s.replace('đ', 'd').replace(' ', '')


def syl_parts(syl):
    d = ud.normalize('NFD', syl)
    tones = [TONE[c] for c in d if c in TONE]
    assert len(tones) <= 1, syl
    bare = ud.normalize('NFC', ''.join(c for c in d if c not in TONE))
    return bare, (tones[0] if tones else 0)


def o1_key(w):
    out = []
    for syl in w.split(' '):
        bare, t = syl_parts(syl)
        out.append((tuple(LIDX[c] for c in bare), t))
    return tuple(out)


def regional_risk(w):
    groups = set()
    for syl in w.split(' '):
        bare, _ = syl_parts(syl)
        if bare.startswith(('s', 'x')) and len(bare) > 1:
            groups.add('s/x')
        if bare.startswith(('ch', 'tr')) and len(bare) > 2:
            groups.add('ch/tr')
        if (bare.startswith('gi') and (len(bare) > 2 or bare == 'gi')) or \
           (bare.startswith(('d', 'r')) and len(bare) > 1):
            groups.add('d/gi/r')
        if (bare.startswith('l') and len(bare) > 1) or (bare.startswith('n') and not bare.startswith(('ng', 'nh')) and len(bare) > 1):
            groups.add('l/n')
        if bare.endswith(('c', 't')):
            groups.add('-c/-t')
        if bare.endswith(('n', 'ng')):
            groups.add('-n/-ng')
    return min(len(groups), 4)


def percentiles(vals):
    pos = sorted(v for v in vals if v > 0)
    n = len(pos)
    rank = {}
    i = 0
    while i < n:
        j = i
        while j < n and pos[j] == pos[i]:
            j += 1
        rank[pos[i]] = Fraction(i + 1 + j, 2)  # hạng trung bình của nhóm bằng nhau (đánh từ 1)
        i = j
    return [Fraction(0) if v == 0 else 100 * rank[v] / n for v in vals]


def round2(x):
    v = abs(x) * 100
    q, r = divmod(v.numerator, v.denominator)
    q += 1 if 2 * r >= v.denominator else 0
    return q if x >= 0 else -q


def load_counts(extra=()):
    counts = {}
    for r in tsv(U / 'bang-khoa-chung.tsv'):
        uv = json.loads(r['ung_vien'])
        cols = {k: json.loads(r[k]) for k in ('sub_sach', 'web_sach', 'leipzig_so_cau', 'tatoeba_so_cau', 'opensub_n', 'ccaligned_n')}
        for i, w in enumerate(uv):
            counts[(r['khoa'], w)] = {k: int(cols[k][i]) for k in cols}
    for f in extra:  # bảng ứng viên L2/L2B…: một dòng một mặt chữ
        for r in tsv(U / f):
            counts[(r['khoa'], r['tu'])] = {k: int(r[k]) for k in ('sub_sach', 'web_sach', 'leipzig_so_cau', 'tatoeba_so_cau', 'opensub_n', 'ccaligned_n')}
    return counts


def bin_of(it):
    return ('OK' if it['nhan'] == 'OK' else 'R1') + ('_F' if it['lop'] == 'F' else '_N')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--du-phong', choices=('chat', 'han-muc'), default='han-muc')
    ap.add_argument('--chon', default=None)
    ap.add_argument('--ghi', action='store_true', help='ghi các tệp đầu ra chính thức')
    ap.add_argument('--them', nargs='*', default=[], help='tập nhận sau H9 của các lô bổ sung (L2A, L2B…)')
    ap.add_argument('--dem-them', nargs='*', default=[], help='bảng ứng viên của các lô bổ sung (số đếm bốn kho)')
    ap.add_argument('--loai', nargs='*', default=[], help='các tệp TSV (khoa, tu) các mục bị khấu trừ có biên bản (H5 liên tầng, P7…)')
    ap.add_argument('--so-tep', default='p6-so-opus.json', help='tệp số liệu ghi kèm khi --ghi')
    ap.add_argument('--cho-ghi-khi-truot', action='store_true', help='cho phép --ghi dù C13 chưa đạt (chỉ dùng khi hai bên đã thống nhất)')
    a = ap.parse_args()
    nh = {(r['khoa'], r['tu']): r for r in tsv(U / 'p4-nhan-sau-H9-opus.tsv') if not r['thieu_ky_O'] and not r['thieu_ky_A']}
    chon_file = Path(a.chon) if a.chon else (U / 'ket-qua-chon.tsv' if (U / 'ket-qua-chon.tsv').is_file() else U / 'p5-ket-luan-opus.tsv')
    chon = {r['khoa']: r['chon'] for r in tsv(chon_file)}
    counts = load_counts(a.dem_them)
    l1_keys = {k[0] for k in nh}
    for f in a.them:
        for r in tsv(U / f):
            assert r['khoa'] not in l1_keys and (r['khoa'], r['tu']) not in nh, ('khóa bổ sung trùng', r['khoa'])
            nh[(r['khoa'], r['tu'])] = r
    bo = set()
    if a.loai:
        bo = {(r['khoa'], r['tu']) for f in a.loai for r in tsv(U / f if not Path(f).is_absolute() else Path(f))}
        assert bo <= set(nh), ('mục khấu trừ không có trong tập nhận', bo - set(nh))
        for k in bo:
            del nh[k]
    bykey = defaultdict(list)
    for k in nh:
        bykey[k[0]].append(k)
    pool = {}
    for key, ks in bykey.items():
        if key in chon:
            if chon[key] == 'BO':
                continue
            if (key, chon[key]) in bo:
                # Mặt đã chọn ở P5 bị khấu trừ vì nghĩa đỏ: cách đọc đó vẫn là cách đọc tự nhiên của khóa,
                # nên theo H7/K1 bỏ cả khóa, không đổi sang mặt lành cùng khóa.
                continue
            sel = [k for k in ks if k[1] == chon[key]]
            assert len(sel) == 1, (key, chon[key])
            k = sel[0]
        else:
            assert len(ks) == 1, (key, ks)
            k = ks[0]
        r = nh[k]
        c = counts[k]
        pool[k[1]] = dict(khoa=key, tu=k[1], nhan=r['nhan'], lop=r['lop'], lop_O=r['lop_O'], lop_A=r['lop_A'],
                          phat=int(r['phat_h5d']), sub=c['sub_sach'], web=c['web_sach'], L=c['leipzig_so_cau'], T=c['tatoeba_so_cau'],
                          h8=not any((c['leipzig_so_cau'], c['tatoeba_so_cau'], c['opensub_n'], c['ccaligned_n'])))
    assert all(fold(w) == it['khoa'] for w, it in pool.items())
    # S2 theo nhóm số khối
    groups = defaultdict(list)
    for w in pool:
        groups[len(w.split(' '))].append(w)
    for ws in groups.values():
        cols = [percentiles([pool[w][f] for w in ws]) for f in ('sub', 'web', 'L', 'T')]
        for i, w in enumerate(ws):
            pool[w]['F'] = sum(col[i] for col in cols) / 4
    # S3
    for w, it in pool.items():
        it['G'] = GVAL[it['lop']]
        it['co_so'] = it['F'] + it['G']
    for w, it in pool.items():
        parts = w.split(' ')
        rev = ' '.join(reversed(parts))
        second = False
        if len(parts) == 2 and rev != w and rev in pool:
            o = pool[rev]
            second = it['co_so'] < o['co_so'] or (it['co_so'] == o['co_so'] and o1_key(w) > o1_key(rev))
        it['T_vung'] = regional_risk(w)
        it['T'] = it['T_vung'] + 5 * it['phat'] + 5 * (len(fold(w)) > 10) + 3 * (len(parts) == 3) + 5 * second
        it['dao_thu_hai'] = int(second)
        it['diem'] = it['co_so'] - it['T']
        it['diem100'] = round2(it['diem'])
    order = sorted(pool, key=lambda w: (pool[w]['nhan'] != 'OK', -pool[w]['diem100'], len(fold(w)), o1_key(w)))
    # chọn chính
    missing = [w for w in KEEP if w not in pool]
    assert not missing, missing
    main_ = list(KEEP)
    used = set(main_)
    f = sum(pool[w]['lop'] == 'F' for w in main_)
    r1 = sum(pool[w]['nhan'] == 'R1' for w in main_)
    for w in order:
        if len(main_) == TARGET:
            break
        if w in used:
            continue
        isf, isr = pool[w]['lop'] == 'F', pool[w]['nhan'] == 'R1'
        if f + isf > QF or r1 + isr > QR:
            continue
        main_.append(w)
        used.add(w)
        f += isf
        r1 += isr
    # dự phòng: thứ tự ngăn OK_N, OK_F, R1_N, R1_F; trong ngăn theo S4
    pref = {'OK_N': 0, 'OK_F': 1, 'R1_N': 2, 'R1_F': 3}
    rest = sorted((w for w in order if w not in used), key=lambda w: (pref[bin_of(pool[w])], order.index(w)))
    slots = Counter(bin_of(pool[w]) for w in main_ if w not in KEEP)
    sl_f, sl_r = QF - f, QR - r1  # chỗ trống còn lại của Q3, Q2
    backups, assign = [], Counter()
    for w in rest:
        if len(backups) == BACKUP:
            break
        b = bin_of(pool[w])
        bf, br = b.endswith('_F'), b.startswith('R1')
        if a.du_phong == 'chat':
            targets = {'OK_N': ['OK_N', 'OK_F', 'R1_N', 'R1_F'], 'OK_F': ['OK_F', 'R1_F', 'OK_N', 'R1_N'],
                       'R1_N': ['R1_N', 'R1_F'], 'R1_F': ['R1_F', 'R1_N']}[b]
        else:
            targets = ['OK_N', 'OK_F', 'R1_N', 'R1_F'] if not br else ['R1_N', 'R1_F', 'OK_N', 'OK_F']
            if b == 'OK_F':
                targets = ['OK_F', 'R1_F', 'OK_N', 'R1_N']
        done = False
        for t in targets:
            if slots[t] <= 0:
                continue
            df = int(bf) - int(t.endswith('_F'))
            dr = int(br) - int(t.startswith('R1'))
            if df > sl_f or dr > sl_r:
                continue
            slots[t] -= 1
            sl_f -= max(df, 0)
            sl_r -= max(dr, 0)
            assign[(b, t)] += 1
            backups.append(w)
            done = True
            break
    stats = {
        'che_do_du_phong': a.du_phong, 'tep_chon_P5': chon_file.name,
        'pool': len(pool), 'ngan_pool': dict(Counter(bin_of(it) for it in pool.values())),
        'chinh': len(main_), 'chinh_F': f, 'chinh_R1': r1, 'ngan_chinh': dict(Counter(bin_of(pool[w]) for w in main_)),
        'du_phong': len(backups), 'ngan_du_phong': dict(Counter(bin_of(pool[w]) for w in backups)),
        'gan_suat': {f'{x}->{y}': n for (x, y), n in assign.items()},
        'dat_C13': len(main_) == TARGET and len(backups) == BACKUP,
    }
    # chỉ báo
    samp = sorted(main_, key=lambda w: hashlib.sha256(('Astra-Opus-M1-v1-20261119|' + fold(w)).encode('utf-8')).digest())[:300]
    cls = Counter(pool[w]['lop'] for w in samp)
    pair = Counter((pool[w]['lop_A'], pool[w]['lop_O']) for w in samp)
    lower = sum(n for (x, y), n in pair.items() if x in 'CH' and y in 'CH')
    upper = sum(n for (x, y), n in pair.items() if x in 'CH' or y in 'CH')
    starts = Counter(w.split(' ')[0] for w in main_)
    mx = max(starts.values())
    ind = {
        'M1_C_cong_H': (cls['C'] + cls['H']) / len(samp), 'M1_lop_mau': dict(cls), 'M1_can_duoi_tren': [lower, upper],
        'M1_lech_ma_goc': sum(n for (x, y), n in pair.items() if x != y),
        'M2_ba_khoi': sum(len(w.split(' ')) == 3 for w in main_), 'M3_trung_binh_chu': sum(len(fold(w)) for w in main_) / len(main_),
        'M4_ngoai_le_H8': sum(pool[w]['h8'] for w in main_), 'M5_nhieu_nhat': mx,
        'M5_am_tiet': sorted([s for s, n in starts.items() if n == mx], key=o1_key),
        'M1_mau_sha': hashlib.sha256(('\n'.join(samp) + '\n').encode('utf-8')).hexdigest(),
    }
    stats['chi_bao'] = ind
    main_sorted = sorted(main_, key=o1_key)
    back_sorted = sorted(backups, key=o1_key)
    b_main = ('\n'.join(main_sorted) + '\n').encode('utf-8')
    b_back = ('\n'.join(back_sorted) + '\n').encode('utf-8')
    stats['sha_danh_sach_chon'] = hashlib.sha256(b_main).hexdigest()
    stats['sha_du_phong'] = hashlib.sha256(b_back).hexdigest()
    if a.ghi and not stats['dat_C13'] and not a.cho_ghi_khi_truot:
        print(json.dumps(stats, ensure_ascii=False, indent=1))
        print('C13 chưa đạt: không ghi tệp chính thức (thêm --cho-ghi-khi-truot nếu hai bên đã thống nhất).')
        sys.exit(1)
    if a.ghi:
        (U / 'danh-sach-chon.txt').write_bytes(b_main)
        (U / 'du-phong.txt').write_bytes(b_back)
        with open(U / 'xep-hang.tsv', 'w', encoding='utf-8', newline='') as fh:
            wr = csv.writer(fh, delimiter='\t', lineterminator='\n')
            wr.writerow('hang khoa tu nhan lop F G T_vung phat_h5d dai_tren_10 ba_khoi dao_thu_hai T diem diem_100 vao'.split())
            for i, w in enumerate(order, 1):
                it = pool[w]
                vao = 'CHINH' if w in used else ('DU_PHONG' if w in set(backups) else '-')
                wr.writerow((i, it['khoa'], w, it['nhan'], it['lop'], f"{float(it['F']):.6f}", it['G'], it['T_vung'], it['phat'],
                             int(len(fold(w)) > 10), int(len(w.split(' ')) == 3), it['dao_thu_hai'], it['T'], f"{float(it['diem']):.6f}", it['diem100'], vao))
    if a.ghi:
        (U / a.so_tep).write_text(json.dumps(stats, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(stats, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
