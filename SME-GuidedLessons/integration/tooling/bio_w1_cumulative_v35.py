#!/usr/bin/env python3
"""Emit the BIOLOGY-4BI1 stage-B wave-1 CUMULATIVE corrective (manifest v35 + INT-3 v35 + receipt).

The v34 tranche-scoped INT-3 (14 rows) makes the runner-owned guided-import.json rebuild
DROP the stage-A pilot row from the biology index — the physics-wave1-v19 defect class
(caught there by the LIVE SPOT-CHECK calibration leg). The v35 corrective re-pins all 30
pack artifacts byte-identical (2 pilot @ stage-A shas + 28 wave-1 @ landed shas) and
re-issues the index with all 15 rows. ZERO authored bytes change.
"""
import hashlib, json, subprocess, time

W = '/home/z/my-project/w12_work'
REPO = f'{W}/repo'
INT = 'SME-GuidedLessons/integration'
TRACE = '1a1ce45bbe8dc30d'

def sha256(b):
    return hashlib.sha256(b).hexdigest()

def git(*a):
    return subprocess.run(['git', *a], cwd=REPO, capture_output=True, text=True, check=True).stdout.strip()

man34 = json.load(open(f'{REPO}/{INT}/hub-import-manifest-v34.json'))
int3a = json.load(open(f'{REPO}/{INT}/records/INT-3-transform-record-bio-stagea.json'))
int3b = json.load(open(f'{REPO}/{INT}/records/INT-3-transform-record-bio-stageb1.json'))
receipt = json.load(open(f'{REPO}/{INT}/records/BIOLOGY-4BI1-STAGEB1-PROMOTION-20261112.json'))

PILOT = 'rn_qRXSsjyzyZsJnc7k'
pilot_row = next(n for n in int3a['notes'] if n['noteId'] == PILOT)
pilot_art = [a for a in json.load(open(f'{REPO}/{INT}/hub-import-manifest-v33.json'))['artifacts'] if a['noteId'] == PILOT]
assert len(pilot_art) == 2

# byte-verify the pilot artifacts on the tree
for a in pilot_art:
    b = open(f'{REPO}/{a["path"]}', 'rb').read()
    assert len(b) == a['bytes'] and sha256(b) == a['sha256'], a['path']
print('pilot artifacts byte-verified on tree')

# ── INT-3 v35 (cumulative, 15 rows: pilot first, then the 14 wave-1 rows) ────
rows = [pilot_row] + [n for n in int3b['notes']]
assert len(rows) == 15 and len({r['noteId'] for r in rows}) == 15
waves = {}
grand = hashlib.sha256()
grand_chars = 0
for r in rows:
    s = r['stream']['sha256']
    waves.setdefault(r['wave'], hashlib.sha256())
    # wave subtotals hash the STREAM TEXT; we only have the stream sha — but a single-note
    # wave's subtotal == the stream sha; for multi-row waves the v34 subtotal of record
    # (64ddcb4c) is the of-record hash. Rebuild wave hashes from the v34 conservation.
grand_chars = sum(r['stream']['chars'] for r in rows)
# grand stream sha: concatenate the row streams — we do NOT have the raw stream text here,
# but the runner recomputes it from the LANDED artifacts via targetTokens; the manifest's
# authored_stream_sha256 must equal that value. Compute it the same way the pipeline did:
# grand = sha256 of the concatenated streams. For the 14 wave-1 rows the v34 pipeline hashed
# them IN ROW ORDER; prepending the pilot stream changes the grand. We recompute from the
# landed hub/pkg artifacts via the same targetTokens law — replicate it here in Python.
import re
STOP = set(('a an the of to in on for and or is are be by with as at from that this it its into than then so such '
            'what which when how why state name give explain describe each every their there these those can could may might will would '
            'not no nor but if while during about above below between under over again further once here all any both more most other '
            'some only own same than too very one two first second third new used using use uses').split())
def toks(s):
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", (s or '').lower())
def target_tokens(hub, pkg):
    s = []
    les = hub['lesson']
    for sp in les['specAnchors']:
        s.extend([sp['code'], sp['text']])
    s.append(les['primer']['text'])
    if les['primer'].get('prerequisiteSubtopic') is not None:
        s.append(les['primer']['prerequisiteSubtopic'])
    for m in les['modules']:
        s.append(m['title'])
        for h in m.get('sourceHeadings', []):
            s.append(h)
        for r in m.get('specRefs', []):
            s.append(r)
        s.append(m.get('opening', ''))
        for k in m.get('keyPoints', []):
            s.append(k)
        for dl in ('low', 'medium'):
            d = m['depthLayers'][dl]
            s.extend([d['restatement'], d['analogy'], d['examPointer']])
    for g in les['assets']['glossary']:
        s.extend([g['term'], g['definition']])
    we = les['assets'].get('workedExample')
    if we:
        s.append(we['prompt'])
        s.extend(we['steps'])
        s.append(we['finalAnswer'])
    for q in pkg['questions']:
        s.extend([q['stem'], q['misconceptionClass']])
        for o in q.get('options', []):
            s.extend([o['key'], o['text'], o['explanation']])
            if o.get('misconception') is not None:
                s.append(o['misconception'])
        if q.get('kind') and q['kind'] != 'mcq':
            if q.get('modelAnswer') is not None:
                s.append(q['modelAnswer'])
            if isinstance(q.get('keywords'), list):
                s.extend(q['keywords'])
    return s

wave_hashes = {}
order = []
for r in rows:
    nid = r['noteId']
    hub_b = open(f'{REPO}/{INT}/hub-import-1.6/{nid}.hub-lesson-import.json', 'rb').read()
    pkg_b = open(f'{REPO}/{INT}/question-packages-1.3/{nid}.sme-question-package.json', 'rb').read()
    # byte-identity vs anchors
    assert sha256(hub_b) == r['hubSha256'], nid
    assert sha256(pkg_b) == r['pkgSha256'], nid
    hub = json.loads(hub_b)
    pkg = json.loads(pkg_b)
    s = '\n'.join(target_tokens(hub, pkg))
    assert sha256(s.encode()) == r['stream']['sha256'], f'stream mismatch {nid}'
    wk = 'wave-' + r['wave']
    wave_hashes.setdefault(wk, hashlib.sha256())
    wave_hashes[wk].update(s.encode())
    grand.update(s.encode())
    order.append(nid)
grand_hex = grand.hexdigest()
wave_out = {k: h.hexdigest() for k, h in wave_hashes.items()}
print('rows order:', order)
print('waves:', {k: v[:16] for k, v in wave_out.items()})
print('grand:', grand_hex[:16], grand_chars, 'chars')
# cross-check wave-1 subtotal vs v34 conservation
v34_wave = man34['conservation']['wave_stream_sha256'].get('wave-bio-stageb1')
assert v34_wave == wave_out['wave-bio-stageb1'], 'wave-1 subtotal drift vs v34'

counts = {
    'notes': 15,
    'lessons': 30,
    'checks': 270,
    'keyPoints': man34['counts']['keyPoints'] + int3a['biology_stagea_of_record']['tranche_census']['keyPoints'] if False else None,
}

# derive cumulative counts from the two manifests (v34 wave-1 + v33 stage-A)
man33 = json.load(open(f'{REPO}/{INT}/hub-import-manifest-v33.json'))
def add_counts(a, b):
    out = {}
    for k in a['counts']:
        if isinstance(a['counts'][k], (int, float)) and k in b['counts']:
            out[k] = a['counts'][k] + b['counts'][k]
        else:
            out[k] = a['counts'][k]
    return out
cum = add_counts(man34, man33)
cum['authored_chars_conserved'] = man34['counts']['authored_chars_conserved'] + man33['counts']['authored_chars_conserved']
assert cum['notes'] == 15 and cum['lessons'] == 30 and cum['checks'] == 270, cum
assert cum['authored_chars_conserved'] == grand_chars, (cum['authored_chars_conserved'], grand_chars)

promo = git('rev-parse', 'HEAD')
promo_tree = git('log', '-1', '--format=%T')
promo_parent = git('log', '-1', '--format=%P')

manifest = {
    'format': 'hub-import-manifest/1.0',
    'manifest_version': 35,
    'course_id': 'igcse-biology-19',
    'b6_manifest_continuity': {
        'decision': 'continue-global',
        'selected': 'biology stage-B wave-1 CUMULATIVE corrective = manifest v35 (the programme-level v-series continues: chemistry v1..v17+v32, physics v18..v31, biology v33..v35)',
        'rejected': 'per-course series (biology v1 restart) — would fork the programme-level integration ledger',
        'recorded_by': 'runbook B6 (continue-global; re-recorded by this corrective)',
    },
    'generated_at_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    'operator_trace': TRACE,
    'supersedes': ('hub-import-manifest-v34.json (the wave-1 tranche: 28 artifacts) — this v35 corrective CUMULATIVE manifest '
                   're-pins all 30 pack artifacts byte-identical (2 stage-A pilot artifacts @ the v33 landed shas + 28 wave-1 '
                   'artifacts @ the v34 landed shas) and re-issues the runner-owned guided-import.json index with all 15 rows, '
                   'restoring the stage-A pilot flow (the physics-wave1-v19 defect class: a tranche-scoped INT-3 makes the index '
                   'rebuild drop prior rows; caught before landing via the v20 precedent, disclosed). ZERO authored bytes change; '
                   'the physics v31 (254) and chemistry v32 (224) packs untouched.'),
    'checks_layer': {
        'wave': 'BIOLOGY-4BI1 stage-B wave 1 CUMULATIVE (the 14-note register bucket + the stage-A pilot: 15 notes / 30 lessons / 270 checks)',
        'derivation': man34['checks_layer']['derivation'],
        'declared_revision': 'CUMULATIVE re-pin — all 30 artifacts byte-identical to the landed generation; only the runner-owned guided-import.json index carries new bytes on the hub (the corrective class of record, physics wave-1 v20 precedent)',
        'grading_law': man34['checks_layer']['grading_law'],
        'fail_closed': man34['checks_layer']['fail_closed'],
    },
    'source_generation': man34['source_generation'],
    'load_scope': man34['load_scope'],
    'counts': cum,
    'conservation': {
        'authored_stream_sha256': grand_hex,
        'authored_chars': str(grand_chars),
        'wave_stream_sha256': wave_out,
    },
    'artifacts': pilot_art + man34['artifacts'],
}
assert len(manifest['artifacts']) == 30
mb = json.dumps(manifest, indent=1, ensure_ascii=False).encode() + b'\n'
open(f'{REPO}/{INT}/hub-import-manifest-v35.json', 'wb').write(mb)

int35 = {
    'stage': 'BIOLOGY-4BI1 stage-B wave 1 CUMULATIVE (the 14-note register bucket + the stage-A pilot: 15 rows)',
    'title': ('INT-3 transform record — biology stage-B wave 1 CUMULATIVE (guided-lesson/0.7 -> hub/lesson-import/1.6 + '
              'sme-question-package/1.3), the 15-row pack anchor table of record (the stage-A pilot row carried byte-equivalent '
              'from INT-3-transform-record-bio-stagea.json; the 112 chemistry stage-B anchors stay in '
              'INT-3-transform-record-chem-stageb.json, re-proven on this tree by the G-E gates)'),
    'generated_at_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
    'operator_traces': {'ignition': TRACE, 'execution': TRACE},
    'adapter': 'guided-lesson-0.7--hub-lesson-import-1.6',
    'course_id': 'igcse-biology-19',
    'supersedes_int3': 'records/INT-3-transform-record-bio-stageb1.json (the 14-row tranche-scoped table; its 14 rows carried byte-equivalent here plus the pilot row)',
    'b6_manifest_continuity': {'decision': 'continue-global', 'selected': 'manifest v35 supersedes v34 (cumulative)'},
    'notes': rows,
}
ib = json.dumps(int35, indent=1, ensure_ascii=False).encode() + b'\n'
open(f'{REPO}/{INT}/records/INT-3-transform-record-bio-stageb1-v35.json', 'wb').write(ib)

# ── receipt re-issue: append the corrective block ─────────────────────────────
receipt['cumulative_corrective'] = {
    'class': 'physics-wave1-v19/v20 precedent — tranche-scoped index drop',
    'defect': ('the v34 tranche-scoped INT-3 (14 rows) would make the runner-owned guided-import.json rebuild DROP the '
               'stage-A pilot row from the biology index — invisible to the artifact gates (the index is runner-owned '
               'run metadata), caught before landing via the v20 precedent review'),
    'corrective': ('manifest v35 + INT-3 v35 re-pin all 30 pack artifacts byte-identical and re-issue the index with all '
                   '15 rows; ZERO authored bytes change; the wave-1 tranche artifacts, gates and census are unchanged'),
    'manifest': 'hub-import-manifest-v35.json',
    'int3': 'records/INT-3-transform-record-bio-stageb1-v35.json',
    'counts_cumulative': cum,
    'grand_stream': {'sha256': grand_hex, 'chars': grand_chars},
    'wave_stream_sha256': wave_out,
}
receipt['disclosures'] = list(receipt.get('disclosures', [])) + [
    'the wave-1 tranche-scoped INT-3 (14 rows) carried the physics-wave1-v19 index-drop defect class; the CUMULATIVE corrective (manifest v35 + INT-3 v35, 15 rows) rides on top, disclosed — force-back rule-blocked per standing discipline',
]
rb = json.dumps(receipt, indent=1, ensure_ascii=False).encode() + b'\n'
open(f'{REPO}/{INT}/records/BIOLOGY-4BI1-STAGEB1-PROMOTION-20261112.json', 'wb').write(rb)

print('manifest v35:', len(mb), 'B | INT-3 v35:', len(ib), 'B | receipt:', len(rb), 'B')
print('CUMULATIVE EMITTED')
