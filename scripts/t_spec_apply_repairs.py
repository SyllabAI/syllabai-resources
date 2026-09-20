#!/usr/bin/env python3
"""T-SPEC-NORM-1 master applier — repairs to both JSON layers (v1 + canonical).

Repairs:
  R1 ial-maths: delete at-a-glance duplicate IAL_MATHS:6.5; apply 45 verified
    prose rebuild texts; set band-verified sub_items on the 191 changed rows;
    flag 146 formula-dense interleaved rows ('two-column-line-interleave');
    renumber canonical orderings.
  R2 econ + business: apply the 57 accepted cell rebuilds (verbatim-verified).
  R3 ict 6.7.3: strip assessment-table tail from text.
  R4 SDA linear Physics-8.10: clear 120 foreign assessment-bullet items.
  R5 SDA modular Chemistry-6.17/6.18: restore satellite spacing per linear
     sibling convention.
All edits preserve file formatting (indent=1, ensure_ascii=False, no trailing
newline — as committed).
"""
import json, glob, re
from pathlib import Path

RES = Path('/home/z/my-project/download/syllabai-resources/Official-Specifications/parsed')
FLAG = 'two-column-line-interleave'

def load(p):
    return json.loads(Path(p).read_text())

def save(p, obj):
    raw = Path(p).read_text()
    trailing = raw.endswith('\n')
    Path(p).write_text(json.dumps(obj, indent=1, ensure_ascii=False) + ('\n' if trailing else ''))

def both(q):
    v1_path = glob.glob(str(RES / q / '*.parsed.json'))[0]
    return v1_path, RES / q / 'spec_points.json'

report = {}

def norm_ok(a, b):
    return re.sub(r'\s+', ' ', a or '').strip() == re.sub(r'\s+', ' ', b or '').strip()

# ---------- R1 ial-maths ----------
q = 'ial-maths'
v1_path, can_path = both(q)
v1 = load(v1_path)
can = load(can_path)
rebuilds = load('/home/z/my-project/scripts/t_spec_ialmaths_repairs.json')
classified = load('/home/z/my-project/scripts/t_spec_ialmaths_repairs_classified.json')

n_del = n_text = n_items = n_flag = 0
for layer_name, doc in (('v1', v1), ('canonical', can)):
    pts = doc['spec_points']
    pts2 = [p for p in pts if p['id'] != 'IAL_MATHS:6.5']
    n_del += len(pts) - len(pts2)
    doc['spec_points'] = pts2
    for p in doc['spec_points']:
        pid = p['id']
        cl = classified.get(pid)
        if not cl:
            continue
        if cl['action'] == 'rebuild':
            p['text'] = cl['text']
            n_text += 1
        # sub_items: band-verified truth for every changed row
        if pid in rebuilds and p.get('sub_items') != rebuilds[pid]['sub_items']:
            p['sub_items'] = rebuilds[pid]['sub_items']
            n_items += 1
        if cl['action'] == 'flag' and FLAG not in p.get('flags', []):
            p.setdefault('flags', []).append(FLAG)
            n_flag += 1
    # counts
    doc['counts']['spec_points'] = len(doc['spec_points'])
    doc['counts']['flagged'] = sum(1 for p in doc['spec_points'] if p.get('flags'))
    if 'ordering' in doc['spec_points'][0]:
        for i, p in enumerate(doc['spec_points'], 1):
            p['ordering'] = i
# canonical parse_report canonical_bundle counts
rp_path = RES / q / 'parse_report.json'
rp = load(rp_path)
if 'canonical_bundle' in rp:
    rp['canonical_bundle']['counts']['spec_points'] = can['counts']['spec_points']
    save(rp_path, rp)
save(v1_path, v1)
save(can_path, can)
report['ial-maths'] = dict(deleted=n_del // 2, texts=n_text // 2 if n_text else n_text,
                           items=n_items, flags=n_flag)

report['ial-maths'] = {'deleted_6_5': True, 'rows_retexted': sum(
    1 for p in can['spec_points'] if classified.get(p['id'], {}).get('action') == 'rebuild'),
    'rows_flagged': sum(1 for p in can['spec_points'] if FLAG in p.get('flags', [])),
    'canonical_points': can['counts']['spec_points'],
    'canonical_flagged': can['counts']['flagged']}

# ---------- R2 econ + business ----------
for q in ('igcse-economics', 'igcse-business'):
    acc = load('/home/z/my-project/scripts/t_spec_cellrepairs_accepted.json')['accepted']
    rows = {pid: v for pid, v in acc.items() if v['qual'] == q}
    v1_path, can_path = both(q)
    v1 = load(v1_path)
    can = load(can_path)
    n = 0
    for doc in (v1, can):
        for p in doc['spec_points']:
            if p['id'] in rows:
                v = rows[p['id']]
                p['text'] = v['text']
                p['sub_items'] = v['sub_items']
                n += 1
    save(v1_path, v1)
    save(can_path, can)
    report[q] = {'rows_repaired': n // 2}

# ---------- R3 ict 6.7.3 ----------
q = 'igcse-ict'
v1_path, can_path = both(q)
v1 = load(v1_path)
can = load(can_path)
n = 0
for doc in (v1, can):
    for p in doc['spec_points']:
        if p['id'] == 'IGCSE_ICT:6.7.3':
            p['text'] = 'Create and manage files and folder structures.'
            n += 1
save(v1_path, v1)
save(can_path, can)
report['igcse-ict'] = {'rows_repaired': n // 2}

# ---------- R4 SDA linear Physics-8.10 ----------
q = 'igcse-science-double-award'
v1_path, can_path = both(q)
v1 = load(v1_path)
can = load(can_path)
n = 0
for doc in (v1, can):
    for p in doc['spec_points']:
        if p['id'] == 'IGCSE_SCIENCE_DOUBLE_AWARD:Physics-8.10':
            n += len(p['sub_items'])
            p['sub_items'] = []
save(v1_path, v1)
save(can_path, can)
report[q] = {'foreign_items_cleared': n // 2}

# ---------- R5 SDA modular satellite spacing ----------
q = 'igcse-science-double-award-modular'
v1_path, can_path = both(q)
v1 = load(v1_path)
can = load(can_path)
FIX = {
    'Li+is red': 'Li + is red',
    'Na+is yellow': 'Na + is yellow',
    'K+is lilac': 'K + is lilac',
    'Ca2+is orange-red': 'Ca 2+ is orange-red',
    'Cu2+is blue-green': 'Cu 2+ is blue-green',
    'NH4+using sodium hydroxide solution and identifying the gas evolved':
        'NH 4 + using sodium hydroxide solution and identifying the gas evolved',
    'Cu2+, Fe2+and Fe3+using sodium hydroxide solution':
        'Cu 2+ , Fe 2+ and Fe 3+ using sodium hydroxide solution',
}
n = 0
for doc in (v1, can):
    for p in doc['spec_points']:
        new_items = [FIX.get(it, it) for it in p.get('sub_items') or []]
        if new_items != p.get('sub_items'):
            p['sub_items'] = new_items
            n += 1
save(v1_path, v1)
save(can_path, can)
report[q] = {'items_renormalized': n // 2}

print(json.dumps(report, indent=1))
