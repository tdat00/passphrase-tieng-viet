"""Đóng H9 (bản tính của Opus): lập tập mặt chữ được nhận sau P4 để dùng cho P5/P6.

Đầu ra:
  U\\p4-nhan-sau-H9-opus.tsv   khoa tu nhan lop lop_O lop_A phat_h5d nguon thieu_ky_O thieu_ky_A
  U\\p4-sau-H9-so-opus.json    số đếm
"""
import csv, json, sys, io, hashlib, collections
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
U = Path(__file__).resolve().parents[2] / 'unified'
POS = {'OK', 'R1'}
G = {'C': 15, 'H': 5, 'K': 0, 'F': -20}
OPUS_GIU_F = {'theo', 'thông qua', 'thưa', 'chắc'}


def tsv(p):
    with open(p, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def dump(p, head, rows):
    with open(p, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(head.split())
        w.writerows(rows)


def merge(a, b):
    return 'OK' if a == b == 'OK' else 'R1'


def main():
    O = {(r['khoa'], r['tu']): r for r in tsv(U / 'phieu-opus.tsv')}
    A = {(r['khoa'], r['tu']): r for r in tsv(U / 'phieu-astra.tsv')}
    gates = collections.defaultdict(dict)
    for r in tsv(U / 'cong-astra-v4.tsv'):
        gates[(r['khoa'], r['ung_vien'])][r['cong']] = (r['ket_qua'], r['ly_do'])

    # chữ ký có hiệu lực
    sig = {'O': collections.defaultdict(set), 'A': collections.defaultdict(set)}
    for side, files in (('O', ['chu-ky-opus.tsv', 'chu-ky-bo-sung-opus.tsv']),
                        ('A', ['chu-ky-astra.tsv', 'p4-chu-ky-bo-sung-astra.tsv', 'p4-chu-ky-bo-sung-astra-2.tsv'])):
        for fn in files:
            if (U / fn).is_file():
                for r in tsv(U / fn):
                    t = 'K2' if r['loai_ky'] in ('K2', 'K2_KHONG_TU_DONG') else r['loai_ky']
                    sig[side][(r['khoa'], r['tu'])].add(t)
    rut_ky_A = set()
    for r in tsv(U / 'p4-dieu-chinh-khoa-sau-doc-astra.tsv'):
        if r['moi'] == 'K2_KHONG_KY':
            sig['A'][(r['khoa'], r['tu'])].discard('K2')
            rut_ky_A.add((r['khoa'], r['tu']))

    # nhãn sau H9
    lab_O = {k: r['nhan'] for k, r in O.items()}
    lab_A = {k: r['nhan'] for k, r in A.items()}
    cls_prop = {}
    # Astra phản đối, Opus trả lời (Y = chấp nhận; N = phản biện) rồi Astra chốt ở p4-phan-xu-19
    for r in tsv(U / 'p4-phan-xu-19-astra.tsv'):
        k = (r['khoa'], r['tu'])
        if r['hanh_dong'] == 'RUT':
            lab_A[k] = r['nhan_moi']
            cls_prop[k] = r['lop_de_xuat']
    # Opus phản đối, Astra phản biện N, Opus chốt ở phan-bien-lai-opus
    for r in tsv(U / 'phan-bien-lai-opus.tsv'):
        k = (r['khoa'], r['tu'])
        if r['ket_qua'] == 'RUT':
            lab_O[k] = r['nhan_moi_cua_opus']
    bosung = {(r['khoa'], r['tu']) for r in tsv(U / 'p4-phan-doi-bo-sung-astra.tsv')}
    # điều chỉnh khóa của Astra: didong hạ K1 -> nhãn loại thường (R2) cho dị đồng
    for r in tsv(U / 'p4-dieu-chinh-khoa-sau-doc-astra.tsv'):
        if r['cu'] == 'K1' and r['moi'] == 'K2_KY':
            for k in A:
                if k[0] == r['khoa'] and A[k]['nhan'] == 'K' and A[k]['cong'] == 'K1':
                    lab_A[k] = 'R2'
    # khóa bị chặn K0/K1 sau điều chỉnh
    blocked = collections.defaultdict(list)
    for k in O:
        for side, L, B in (('O', lab_O, O), ('A', lab_A, A)):
            if L[k] == 'K' and B[k]['cong'] in ('K0', 'K1'):
                blocked[k[0]].append(f'{side}:{k[1]}')
    # Astra 051: giữ K1 cho khóa danhca (đánh cá đọc ra cá cược)
    blocked['danhca'].append('A:K1-051')
    # Astra 052/053: bốn họ giữ ngoài (H5c/H5e/H6.6;K1)
    ngoai = {(r['khoa'], r['tu']) for r in tsv(U / 'p4-bon-ho-sau-phan-bien-astra.tsv') if r['ket_qua'] == 'GIU_NGOAI'}
    # mặt dương chung khóa với mặt bị gắn S/K ở một bên: cần K2 hai chữ ký (cổng H7 theo nghĩa đỏ mới)
    red_keys = collections.defaultdict(set)
    for k in O:
        for B in (O, A):
            if B[k]['nhan'] in ('S', 'K'):
                red_keys[k[0]].add(k[1])

    lop049 = {(r['khoa'], r['tu']): r['ma'] for r in tsv(U / 'p4-lop-de-xuat-astra.tsv')}
    # Astra 052: lớp cho các mục phục hồi ở H9 chưa có trong 049
    LOP052 = {'ấm êm': 'K', 'bờ bến': 'K', 'cầu thị': 'K', 'gợi hình': 'K', 'hanh thông': 'K', 'hiếu thuận': 'K',
              'hồn hậu': 'K', 'chuyên canh': 'H', 'thiện nghệ': 'H', 'cơ man': 'F', 'mi mắt': 'C', 'đàn xếp': 'C',
              'kiệt sức': 'H', 'đói lả': 'H', 'ô nhiễm': 'K'}

    def op_class(k):
        lo, la = O[k]['lop'], A[k]['lop']
        if lo == la:
            return lo
        if k[1] in OPUS_GIU_F:
            return 'F'
        if k in lop049:
            return lop049[k]
        if k[1] in LOP052:
            return LOP052[k[1]]
        if k in cls_prop and cls_prop[k] in (lo, la):
            return cls_prop[k]
        return min((lo, la), key=lambda c: G[c])

    def need(k):
        g = gates[k]
        n = set()
        if 'CHI_HND' in g['H3'][1]:
            n.add('H3')
        if g['H8'][1] == 'H8:KHONG_LUOT':
            n.add('H8')
        if g['H7'][0] == 'CHO' and g['H7'][1] != 'H7:DOC_NGHIA_H6':
            n.add('K2')
        if g['H5'][0] == 'CHO':
            n.add('H5')
        if red_keys.get(k[0], set()) - {k[1]}:
            n.add('K2')
        return n

    rows, c = [], collections.Counter()
    for k in sorted(O):
        lo, la = lab_O[k], lab_A[k]
        if lo not in POS or la not in POS:
            c['loai_hoac_con_phan_doi'] += 1
            continue
        if k in bosung:
            c['phan_doi_bo_sung'] += 1
            continue
        if k[0] in blocked:
            c['khoa_chan_K0_K1'] += 1
            continue
        if k in rut_ky_A:
            c['K2_rut_chu_ky'] += 1
            continue
        if k in ngoai:
            c['bon_ho_giu_ngoai'] += 1
            continue
        n = need(k)
        mo = ','.join(sorted(n - sig['O'].get(k, set())))
        ma = ','.join(sorted(n - sig['A'].get(k, set())))
        src = 'HAI_BEN' if (O[k]['nhan'] in POS and A[k]['nhan'] in POS) else ('A_RUT' if O[k]['nhan'] in POS else 'O_RUT')
        g5 = gates[k]['H5'][1]
        phat = int('TRU_DIEM' in g5)
        rows.append((k[0], k[1], merge(lo, la), op_class(k), O[k]['lop'], A[k]['lop'], phat, src, mo, ma))
        c['thieu_ky' if (mo or ma) else 'nhan'] += 1
    dump(U / 'p4-nhan-sau-H9-opus.tsv', 'khoa tu nhan lop lop_O lop_A phat_h5d nguon thieu_ky_O thieu_ky_A', rows)
    ok_rows = [r for r in rows if not r[8] and not r[9]]
    keys = collections.defaultdict(list)
    for r in ok_rows:
        keys[r[0]].append(r)
    rep = {
        'dem': dict(c),
        'mat_chu_nhan_du_ky': len(ok_rows),
        'khoa_co_mat_nhan': len(keys),
        'nguon': dict(collections.Counter(r[7] for r in ok_rows)),
        'thieu_ky_O': [(r[0], r[1], r[8]) for r in rows if r[8]],
        'thieu_ky_A': [(r[0], r[1], r[9]) for r in rows if r[9]],
        'khoa_chan': {k: v for k, v in blocked.items()},
        'rut_ky_A': sorted(rut_ky_A),
        'sha': hashlib.sha256((U / 'p4-nhan-sau-H9-opus.tsv').read_bytes()).hexdigest(),
    }
    (U / 'p4-sau-H9-so-opus.json').write_text(json.dumps(rep, ensure_ascii=False, indent=1) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({k: v for k, v in rep.items() if k != 'khoa_chan'}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
