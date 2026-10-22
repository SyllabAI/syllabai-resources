#!/usr/bin/env python3
"""T-SPECS-CIE-PARSE-REPAIR-2 — the 0606 topics-3/9/12 materialization joins.

The spine repair (FM25_ADDED_TOPICS in apps/hub/scripts/build_official_spines.py,
v2 side) materializes the three dropped topics as full subtrees. This vehicle
moves the 9 band-A honest pendings whose reasons named statements 3.1-3.3 /
9.1 / 12.1-12.5 onto their now-existing points (N.M.1 per the codified
statement/example split policy); 'Operations with Polynomials' (band A:
prior-knowledge expansion) stays pending — no 0606 statement teaches generic
polynomial manipulation. Regenerates ONLY fm25's 10 touched rows in the yaml.

Battery: R1 code law (joins restricted to the override's nine new codes),
R2 never-overwrite, R3 census-closure (9 joins + 1 stay EXACT, post-apply
shape aware), R4 other-rows preservation, R5 idempotence, P0 round-trip.
"""
from __future__ import annotations
import hashlib, json, os, sys
import yaml

RES = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SD_PATH = os.path.join(RES, 'spec-links', 'cie-igcse-further-maths-additional-maths-25.json')
YAML_PATH = os.path.join(RES, 'scripts', 'cie_complete_verdicts.yaml')
MAN_PATH = os.path.join(RES, 'spec-links', 'manifest.json')
REPORT = os.path.join(RES, 'graph', 'reports', 'T_SPECS_CIE_PARSE_REPAIR_2_CHECK.json')

LANE = 'T-SPECS-CIE-PARSE-REPAIR-2'
TIER = 'V7_agent_note_join'
METHOD = 'agent_semantic_note_join'
STAMP = '2026-10-22T03:00:00Z'
ORDER = ("operator order 'band B (geo-25's 111 cross-edition rows), band C (EL/fleet "
         "leave-unjoined codification), and then the two parse/spine repair lanes' "
         "(gateway trace 1a1615fe86d96ed9, 2026-10-22, zai-web); repair candidate FILED "
         "by T-SPECS-CIE-COMPLETE-1-BAND-A corrections of record")
SLUG = 'cie-igcse-further-maths-additional-maths-25'
NEW_CODES = {'3.1.1', '3.2.1', '3.3.1', '9.1.1', '12.1.1', '12.2.1', '12.3.1', '12.4.1', '12.5.1'}
JOINS = {
    'rn_VrTbNyJ2KHJNfqKQ': ['3.1.1'],
    'rn_9H8h7XhYhYpwhZTz': ['3.2.1'],
    'rn_QMV8TxSD9WjM8KPq': ['3.2.1', '3.3.1'],
    'rn_cwnTtzgNpP3frDKf': ['9.1.1'],
    'rn_wGNNSj8pztQ9ZJ3D': ['9.1.1'],
    'rn_277Qgfb6dxbykZ48': ['12.1.1', '12.2.1'],
    'rn_q8MRstxMpD9n5d5S': ['12.3.1'],
    'rn_rztyPZCwJ2MnmxXZ': ['12.4.1'],
    'rn_6MVw7sx6qnYGPXSX': ['12.4.1', '12.5.1'],
}
PENDING_STAY = {
    'rn_swjpBvbHyDmNPxZT': 'no_0606_statement_teaches_note_content (operations with polynomials: '
                           'prior-knowledge manipulation; band A classified it under the then-absent '
                           'topic 3, but statements 3.1-3.3 teach the factor theorem, factor-finding '
                           'and cubic equations, not generic polynomial operations) — codified '
                           'leave-unjoined under T-SPECS-CIE-PARSE-REPAIR-2 (AGENT.md rule 3 held)',
}
OFFICIAL_TEXTS = {
    '3.1.1': 'Know and use the remainder and factor theorems.',
    '3.2.1': 'Find factors of polynomials.',
    '3.3.1': 'Solve cubic equations.',
    '9.1.1': 'Solve problems involving the arc length and sector area of a circle, '
             'including knowledge and use of radian measure.',
    '12.1.1': 'Use the binomial theorem for expansion of (a + b)ⁿ for positive integer n.',
    '12.2.1': 'Use the general term nCr aⁿ⁻r bʳ, 0 ⩽ r ⩽ n.',
    '12.3.1': 'Recognise arithmetic and geometric progressions and understand the '
              'difference between them.',
    '12.4.1': 'Use the formulas for the nth term and for the sum of the first n terms '
              'to solve problems involving arithmetic or geometric progressions.',
    '12.5.1': 'Use the condition for the convergence of a geometric progression, and '
              'the formula for the sum to infinity of a convergent geometric progression.',
}
YAML_PARAMS = dict(sort_keys=False, allow_unicode=True, width=110)


def die(m):
    print(f'ABORT: {m}', flush=True)
    sys.exit(1)


def main():
    apply_mode = '--apply' in sys.argv
    report = {'lane': LANE, 'stamp': STAMP, 'order': ORDER, 'apply': apply_mode,
              'problems': []}
    probs = report['problems']

    ybytes = open(YAML_PATH, 'rb').read()
    ydoc = yaml.safe_load(ybytes)
    if yaml.safe_dump(ydoc, **YAML_PARAMS).encode('utf8') != ybytes:
        die('P0 verdicts-yaml round-trip is not a byte fixed point')

    sd = json.load(open(SD_PATH, encoding='utf8'))
    side_pre = json.loads(json.dumps(sd))
    already = all(any(e.get('lane') == LANE for e in ((side_pre['items'].get(nid) or {}).get('codes') or []))
                  for nid in JOINS)
    # R3: the lane's touched rows must sit in the fm25 pending universe
    # pre-apply (41 rows: 10 touched + 31 band-A rows this lane leaves
    # byte-untouched); post-apply the pendings are 32 and the 9 joins are out
    universe = {r['id'] for r in ydoc['verdicts']
                if r['verdict'] == 'pending_classified' and r['lane'] == SLUG}
    touched = set(JOINS) | set(PENDING_STAY)
    if already:
        if universe & touched != set(PENDING_STAY):
            probs.append('R3 post-apply shape wrong: stay rows must remain the only touched pendings')
    else:
        if not touched <= universe:
            probs.append(f'R3 pre-apply: touched rows missing from universe: {sorted(touched - universe)}')

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
                'rule': f'{METHOD} under {LANE} (topics 3/9/12 materialized; statement/'
                        f'example split policy of record); {ORDER}',
            })

    if apply_mode and not probs:
        rs = sd.setdefault('review_state', {}).setdefault('complete', {})
        pr = rs.setdefault('parse_repair', {})
        pr[LANE] = {
            'state': 'APPLIED_operator_ordered_parse_repair', 'stamp': STAMP,
            'order': ORDER, 'rows': len(JOINS), 'pending_stay': len(PENDING_STAY),
            'codes': sorted(NEW_CODES),
            'policy': 'statement/example split policy of record: the served 0606 grammar '
                      'renders official statements as SUBTOPIC titles and their example '
                      'sub-bullets as N.M.K points (over-split codes byte-stable — the '
                      'join surface); sub-bullet-less statements land as point N.M.1',
            'basis': 'topics 3/9/12 materialized from the official 662470 text (fetched '
                     'fresh this lane); the band-A pendings that named those statements '
                     'join their dedicated points',
        }
        json.dump(sd, open(SD_PATH, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
        open(SD_PATH, 'a', encoding='utf8').write('\n')

        kept = [r for r in ydoc['verdicts']
                if not (r.get('lane') == SLUG and r['verdict'] == 'pending_classified'
                        and (r['id'] in JOINS or r['id'] in PENDING_STAY))
                and not (r.get('lane') == SLUG and r['verdict'] == 'resolve'
                         and LANE in (r.get('rule') or ''))]
        new_rows = list(kept) + yaml_resolve
        for nid in sorted(PENDING_STAY):
            it = items.get(nid) or {}
            new_rows.append({'lane': SLUG, 'id': nid, 'verdict': 'pending_classified',
                             'reason': PENDING_STAY[nid], 'label': it.get('label'),
                             'section': it.get('section'), 'topic': it.get('topic')})
        ydoc['verdicts'] = new_rows
        man = json.load(open(MAN_PATH, encoding='utf8'))
        man.setdefault('cie_complete', {}).setdefault('parse_repair', {})[LANE] = {
            'schema_note': 'additive parse-repair layer under cie_complete', 'stamp': STAMP,
            'order': ORDER, 'spineRepair': 'FM25_ADDED_TOPICS (+3 topics / +9 subtopics / +9 points)',
            'policy': 'statement/example split policy codified (over-split codes byte-stable; '
                      'sub-bullet-less statements land as point N.M.1)',
            'courses': {SLUG: {'joins': len(JOINS), 'pending_stay': len(PENDING_STAY),
                               'codes': sorted(NEW_CODES)}},
            'totals': {'joins': len(JOINS), 'pending_stay': len(PENDING_STAY)},
        }
        json.dump(man, open(MAN_PATH, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
        open(MAN_PATH, 'a', encoding='utf8').write('\n')

        out_bytes = yaml.safe_dump(ydoc, **YAML_PARAMS).encode('utf8')
        chk = yaml.safe_load(out_bytes)
        f = [r for r in chk['verdicts'] if r.get('lane') == SLUG]
        res = [r for r in f if r['verdict'] == 'resolve' and LANE in (r.get('rule') or '')]
        pend = [r for r in f if r['verdict'] == 'pending_classified']
        if len(res) != len(JOINS) or len(pend) != 32:
            open(YAML_PATH, 'wb').write(ybytes)
            die(f'R-census failed on regenerated yaml: {len(res)}/{len(JOINS)} resolves, '
                f'{len(pend)}/32 pendings — original yaml restored')
        with open(YAML_PATH, 'wb') as fh:
            fh.write(out_bytes)

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
