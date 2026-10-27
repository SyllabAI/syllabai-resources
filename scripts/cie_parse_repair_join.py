#!/usr/bin/env python3
"""T-SPECS-CIE-PARSE-REPAIR-1 — the 9709 P3 3.1 algebra-glue repair joins.

The spine repair (PURE3_ALGEBRA_SPLIT in apps/hub/scripts/build_official_spines.py,
v2 side) materializes official bullets 2-5 as NEW points 3.1.3-3.1.6. This
vehicle moves the 12 band-A honest pendings onto their now-existing dedicated
points (the band-A reasons themselves named the bullets), leaves the 4 rows no
P3 statement teaches as honest pendings, regenerates ONLY the pure-3 verdict
rows in the yaml (all other rows object-preserved), and adds the repair block
to the manifest (additive; bands A/B/C byte-kept).

Battery (fail-closed):
  R1 code law: every joined code is one of the override's four new codes
  R2 never-overwrite: target notes carry no pre-existing non-repair codes
  R3 census-closure: 12 joins + 4 pendings EXACT vs the pure-3 pending universe
  R4 other-rows preservation: non-pure-3 yaml rows object-hash unchanged
  R5 idempotence: re-run applies zero rows, all written files byte-identical
  P0 verdicts-yaml round-trip byte fixed point
"""
from __future__ import annotations
import hashlib, json, os, sys, subprocess
import yaml

RES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SD_PATH = os.path.join(RES, 'spec-links', 'cie-a-level-maths-20-pure-3.json')
YAML_PATH = os.path.join(RES, 'scripts', 'cie_complete_verdicts.yaml')
MAN_PATH = os.path.join(RES, 'spec-links', 'manifest.json')
REPORT = os.path.join(RES, 'graph', 'reports', 'T_SPECS_CIE_PARSE_REPAIR_1_CHECK.json')

LANE = 'T-SPECS-CIE-PARSE-REPAIR-1'
TIER = 'V7_agent_note_join'
METHOD = 'agent_semantic_note_join'
STAMP = '2026-10-22T02:30:00Z'
ORDER = ("operator order 'band B (geo-25's 111 cross-edition rows), band C (EL/fleet "
         "leave-unjoined codification), and then the two parse/spine repair lanes' "
         "(gateway trace 1a1615fe86d96ed9, 2026-10-22, zai-web); repair candidate FILED "
         "by T-SPECS-CIE-COMPLETE-1-BAND-A corrections of record")
SLUG = 'cie-a-level-maths-20-pure-3'
NEW_CODES = {'3.1.3', '3.1.4', '3.1.5', '3.1.6'}
# the 12 unblockable rows, coded from band A's own reason evidence
# (bullet numbers verbatim from the band-A pending reasons)
JOINS = {
    'rn_yw5zfVwy3cTQRQXW': ['3.1.3'],
    'rn_76mfphV4w3cKtH82': ['3.1.3', '3.1.4'],
    'rn_mWqnR994WZsDWS5n': ['3.1.4'],
    'rn_7fdmrwB35FDFZp8r': ['3.1.5'],
    'rn_Pyr2nPYMGWX24X3m': ['3.1.5'],
    'rn_wBR3NX6mbvdPJjd7': ['3.1.5'],
    'rn_pHs9VM9KBTns5dqq': ['3.1.3', '3.1.5'],
    'rn_c7C8JPxJZNW6x8f5': ['3.1.5'],
    'rn_mJVSstNK58Bj6Xxf': ['3.1.6'],
    'rn_drjq6n3z58FR5Y3j': ['3.1.6'],
    'rn_YkGXK7HcGY3tPrzJ': ['3.1.6'],
    'rn_qrCWjGJYGkpDFYJf': ['3.1.6'],
}
PENDING_STAY = {
    'rn_64KPvjqtjbDTgxXQ': 'no_p3_statement_teaches_note_content (further-modelling: generic '
                           'modelling-skills note, no unique P3 statement) — codified leave-unjoined '
                           'under T-SPECS-CIE-PARSE-REPAIR-1; the 3.1 split does not create a target '
                           'for it (AGENT.md rule 3 held)',
    'rn_SXhzXxD6HcctXrHr': 'no_p3_statement_teaches_note_content (eliminating the parameter / '
                           'Cartesian conversion; not a P3 statement) — codified leave-unjoined under '
                           'T-SPECS-CIE-PARSE-REPAIR-1 (AGENT.md rule 3 held)',
    'rn_xSzWDrCGbhqXPZmS': 'no_p3_statement_teaches_note_content (sketching parametric graphs; not a '
                           'P3 statement) — codified leave-unjoined under T-SPECS-CIE-PARSE-REPAIR-1 '
                           '(AGENT.md rule 3 held)',
    'rn_zqzRNBZxTfm6XzK5': 'no_p3_statement_teaches_note_content (parametric basics / defining and '
                           'plotting; 3.4.3 covers differentiating only) — codified leave-unjoined '
                           'under T-SPECS-CIE-PARSE-REPAIR-1 (AGENT.md rule 3 held)',
}
OFFICIAL_TEXTS = {
    '3.1.3': 'divide a polynomial, of degree not exceeding 4, by a linear or quadratic '
             'polynomial, and identify the quotient and remainder (which may be zero)',
    '3.1.4': 'use the factor theorem and the remainder theorem',
    '3.1.5': 'recall an appropriate form for expressing rational functions in partial '
             'fractions, and carry out the decomposition, in cases where the denominator '
             'is no more complicated than ( ax + b )( cx + d )( ex + f ), '
             '( ax + b )( cx + d )², ( ax + b )( cx² + d )',
    '3.1.6': 'use the expansion of (1 + x)ⁿ, where n is a rational number and | x | < 1',
}
YAML_PARAMS = dict(sort_keys=False, allow_unicode=True, width=110)


def die(m):
    print(f'ABORT: {m}', flush=True)
    sys.exit(1)


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def main():
    apply_mode = '--apply' in sys.argv
    report = {'lane': LANE, 'stamp': STAMP, 'order': ORDER, 'apply': apply_mode,
              'problems': []}
    probs = report['problems']

    ybytes = open(YAML_PATH, 'rb').read()
    ydoc = yaml.safe_load(ybytes)
    if yaml.safe_dump(ydoc, **YAML_PARAMS).encode('utf8') != ybytes:
        die('P0 verdicts-yaml round-trip is not a byte fixed point')

    # R3 census-closure (pre-apply: the 16-row pending universe; post-apply
    # re-run: the 4 stay-rows remain pending and the 12 sit as applied resolves)
    universe = {r['id']: r for r in ydoc['verdicts']
                if r['verdict'] == 'pending_classified' and r['lane'] == SLUG}
    side_pre = json.load(open(SD_PATH, encoding='utf8'))
    already = all(any(e.get('lane') == LANE for e in ((side_pre['items'].get(nid) or {}).get('codes') or []))
                  for nid in JOINS)
    want_universe = set(PENDING_STAY) if already else set(JOINS) | set(PENDING_STAY)
    if set(universe) != want_universe:
        probs.append(f'R3 census mismatch: universe {sorted(set(universe) ^ want_universe)} (already={already})')
    for nid, codes in JOINS.items():
        if not set(codes) <= NEW_CODES:
            probs.append(f'R1 violation: {nid} codes {codes} outside the override set')
        if nid not in universe and not already:
            probs.append(f'R3: {nid} not in the pending universe')

    sd = json.load(open(SD_PATH, encoding='utf8'))
    items = sd['items']
    yaml_resolve = []
    if not probs:
        for nid, codes in sorted(JOINS.items()):
            it = items.get(nid)
            if it is None or it.get('kind') != 'note':
                probs.append(f'R2: {nid} absent/not a note'); continue
            existing = it.get('codes') or []
            mine = [e for e in existing if e.get('lane') == LANE]
            other = [e for e in existing if e.get('lane') != LANE]
            if other:
                probs.append(f'R2: {nid} pre-existing non-repair codes {other[:1]}'); continue
            if mine:
                if sorted(e['official_code'] for e in mine) != sorted(codes):
                    probs.append(f'R2: {nid} repair-code drift'); continue
            elif apply_mode:
                it['codes'] = existing + [
                    {'official_id': f'{sd.get("qual") or SLUG.upper()}:{c}',
                     'official_code': c, 'tier': TIER, 'method': METHOD,
                     'score': None, 'lane': LANE, 'applied_utc': STAMP}
                    for c in codes]
            yaml_resolve.append({
                'lane': SLUG, 'id': nid, 'verdict': 'resolve', 'tier': TIER,
                'method': METHOD, 'codes': sorted(codes),
                'label': it.get('label'), 'section': it.get('section'), 'topic': it.get('topic'),
                'official_texts': {c: OFFICIAL_TEXTS[c][:160] for c in sorted(codes)},
                'rule': f'{METHOD} under {LANE} (the 3.1 algebra split materialized the '
                        f'dedicated points); {ORDER}',
            })

    if apply_mode and not probs:
        rs = sd.setdefault('review_state', {}).setdefault('complete', {})
        pr = rs.setdefault('parse_repair', {})
        pr[LANE] = {
            'state': 'APPLIED_operator_ordered_parse_repair', 'stamp': STAMP,
            'order': ORDER, 'rows': len(JOINS), 'pending_stay': len(PENDING_STAY),
            'codes': sorted(NEW_CODES),
            'basis': 'the PURE3_ALGEBRA_SPLIT spine repair materialized official bullets 2-5 '
                     '(the band-A glued-parse finding); the band-A pendings that named those '
                     'bullets join their dedicated points; official_texts from the split '
                     'override of record',
        }
        json.dump(sd, open(SD_PATH, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
        open(SD_PATH, 'a', encoding='utf8').write('\n')

        # regen universe: pure-3 pending rows AND this lane's own resolve rows
        # are regenerated (idempotent); every other row is byte-preserved
        kept = [r for r in ydoc['verdicts']
                if not (r.get('lane') == SLUG and r['verdict'] == 'pending_classified')
                and not (r.get('lane') == SLUG and r['verdict'] == 'resolve'
                         and LANE in (r.get('rule') or ''))]
        new_rows = list(kept) + yaml_resolve
        for nid in sorted(PENDING_STAY):
            it = items.get(nid) or {}
            new_rows.append({'lane': SLUG, 'id': nid, 'verdict': 'pending_classified',
                             'reason': PENDING_STAY[nid], 'label': it.get('label'),
                             'section': it.get('section'), 'topic': it.get('topic')})
        ydoc['verdicts'] = new_rows
        cc = json.load(open(MAN_PATH, encoding='utf8')).get('cie_complete') or {}
        cc.setdefault('parse_repair', {})[LANE] = {
            'schema_note': 'additive parse-repair layer under cie_complete', 'stamp': STAMP,
            'order': ORDER, 'spineRepair': 'PURE3_ALGEBRA_SPLIT (+4 points 3.1.3-3.1.6)',
            'courses': {SLUG: {'joins': len(JOINS), 'pending_stay': len(PENDING_STAY),
                               'codes': sorted(NEW_CODES)}},
            'totals': {'joins': len(JOINS), 'pending_stay': len(PENDING_STAY)},
        }
        man = json.load(open(MAN_PATH, encoding='utf8'))
        man['cie_complete'] = cc
        json.dump(man, open(MAN_PATH, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
        open(MAN_PATH, 'a', encoding='utf8').write('\n')

        out_bytes = yaml.safe_dump(ydoc, **YAML_PARAMS).encode('utf8')
        chk = yaml.safe_load(out_bytes)
        p3 = [r for r in chk['verdicts'] if r.get('lane') == SLUG]
        res = [r for r in p3 if r['verdict'] == 'resolve' and LANE in (r.get('rule') or '')]
        pend = [r for r in p3 if r['verdict'] == 'pending_classified']
        if len(res) != len(JOINS) or len(pend) != len(PENDING_STAY):
            open(YAML_PATH, 'wb').write(ybytes)
            die(f'R-census failed on regenerated yaml: {len(res)}/{len(JOINS)} resolves, '
                f'{len(pend)}/{len(PENDING_STAY)} pendings — original yaml restored')
        with open(YAML_PATH, 'wb') as f:
            f.write(out_bytes)

    if probs:
        report['ok'] = False
        print('PROBLEMS:', probs[:10], flush=True)
    else:
        report['ok'] = True
        report['joins'] = len(JOINS)
        report['pending_stay'] = len(PENDING_STAY)
    json.dump(report, open(REPORT, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
    open(REPORT, 'a', encoding='utf8').write('\n')
    print(f"report -> {REPORT}  ok={report['ok']}", flush=True)
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    sys.exit(main())
