#!/usr/bin/env python3
"""P7: generate docs/P7-CHANNEL-POOLS.md (census from the drafts + emitted hub
files; net spec deltas computed vs the pre-emit committed hub state)."""
import json, subprocess, os

RES = '/home/z/my-project/repos/syllabai-resources/Videos'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh'
W = '/home/z/my-project/work/p7'

summ = json.load(open(f'{W}/summary.json'))
ORDER = ['cie-a-level-biology-25', 'cie-a-level-chemistry-25', 'cie-a-level-physics-25',
         'cie-igcse-biology-23', 'cie-igcse-chemistry-23', 'cie-igcse-physics-23',
         'ial-biology-18', 'ial-chemistry-17', 'ial-physics-19',
         'igcse-biology-19', 'igcse-chemistry-19', 'igcse-physics-19']

# pre-emit committed coverage (hub @ 3e10718d — the tree the emit ran against)
pre = {}
for c in ORDER:
    blob = subprocess.run(['git', '-C', HUB, 'show', f'3e10718d:apps/hub/content/video-map/{c}.json'],
                          capture_output=True, text=True).stdout
    pre[c] = json.loads(blob)['coverage']['specPointsMapped'] if blob else 0

tot_rows = sum(summ[c]['rows'] for c in ORDER)
tot_m = sum(summ[c]['m'] for c in ORDER)
tot_l = sum(summ[c]['l'] for c in ORDER)

CASCADE = [
    ('cie-as-biology-25', 28), ('cie-as-chemistry-25', 13), ('cie-as-physics-25', 1),
    ('cie-igcse-science-co-ordinated-sciences-double-award-23-biology', 19),
    ('cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry', 9),
    ('cie-igcse-science-co-ordinated-sciences-double-award-23-physics', 12),
    ('cie-igcse-science-combined-science-23-biology', 5),
    ('cie-igcse-science-combined-science-23-chemistry', 3),
    ('cie-igcse-science-combined-science-23-physics', 10),
    ('igcse-biology-modular-24-unit-1', 10), ('igcse-biology-modular-24-unit-2', 27),
    ('igcse-chemistry-modular-24-unit-1', 9), ('igcse-chemistry-modular-24-unit-2', 2),
    ('igcse-physics-modular-24-unit-1', 14), ('igcse-physics-modular-24-unit-2', 5),
    ('igcse-science-double-award-17-biology', 36), ('igcse-science-double-award-17-chemistry', 8),
    ('igcse-science-double-award-17-physics', 11),
    ('igcse-science-double-award-modular-24-biology-unit-1', 15),
    ('igcse-science-double-award-modular-24-biology-unit-2', 21),
    ('igcse-science-double-award-modular-24-chemistry-unit-1', 6),
    ('igcse-science-double-award-modular-24-chemistry-unit-2', 2),
    ('igcse-science-double-award-modular-24-physics-unit-1', 10),
    ('igcse-science-double-award-modular-24-physics-unit-2', 1),
]
casc = sum(n for _, n in CASCADE)

md = ['# P7 — remaining external channel pools (T-VIDEOMAP-P7)', '',
      'Owner ask (chat 2026-11-13): *"Proceed with remaining channel pools"* — map the unmapped remainder of '
      'the four previously-mined pools (P2B/P2C/P2D took the easy wins) onto the 12 science parent courses '
      'whose children inherit. Same title-only posture + tightened binding rule as P2E/P5/P6.', '',
      '## Pool', '',
      '- Four pools, re-enumerated fresh before the lane (`scripts/p7/p7_enumerate.py`): **amoeba-sisters 179, '
      'freesciencelessons 776, malmesbury-education 72, doodlescience 58 = 1,085 public uploads — 0 deltas on '
      'all four** (unlike PhysicsOnline\u2019s +1 before P6).',
      '- Already mapped before P7: **417** pool videos across the union. Unmapped remainder: **668**.',
      '- Routed into the lane: **516** (`scripts/p7/p7_target_pool.py` — subject-marker routing per channel '
      'shape + idf best-of across the subject\u2019s four parent spines). Skipped honest-no-target: **152** '
      '(73 sewage incl. ALL non-science malmesbury content — English-Lit poem analyses, Spanish/German/French '
      'lessons, KS3, DT, PE (no such video-map lane exists); 40 amoeba no-biology-vocabulary; 28 '
      'no-spine-overlap; 11 misc).', '',
      '## Method', '',
      '1. Re-enumerate (0 deltas) → union-exclude → route (516).',
      '2. Top-8 SPEC_POINT candidates per video via idf token overlap (`scripts/p7/p7_candidates.py`).',
      '3. Deterministic binding pre-pass, tightened rule: a spec binds only on a token with in-course df <= 3 '
      '(`scripts/p7/p7_candidates.py`). **388 binds proposed**, 128 no-binding rejects.',
      '4. **Agent judgment pass over every proposed row** (`scripts/p7/p7_judgment_*.py`, title-asserted '
      'tables): **277 kept** (M88/L189), **111 full-row drops** with reasons — '
      'misbind classes: the IAL CORE-PRACTICAL-13 magnet (spec 6.4 attached to 18 unrelated rows), FSL '
      'practise-question calculation drills (P6 generic-drill class), Doodle physics videos idf-routed onto '
      'biology specs (cross-subject), AQA-specific content verified absent from the spines (homeobox genes, '
      'insect tracheal systems, dialysis, cofactors, potometers, oestrogen-cancer), US-curriculum divergence '
      '(amoeba), spine-code verification before every rebind (lac operon 16.3.2, 4.2.1 endocytosis, 7.2.2 '
      'apoplast, 8.3.4 sinoatrial, 6.1.4 semi-conservative, 6.2.7 deletion/insertion verified in-spine).',
      '5. Identity: **277/277 verified** (159 oEmbed + 118 thumb-fallback for the freesciencelessons '
      'embedding-disabled A-level videos, per the P2D law, `identityMethod` per video). Channel-author '
      'discovery: DoodleScience\u2019s oEmbed name has no space — expected-author map corrected pre-ship.',
      '6. Delegated self-review per owner chat 2026-11-09 standing ruling; verdicts '
      '`owner-review-verdicts.p7.json` x12 (360+ reject-ledger entries total incl. pre-pass no-binds); '
      'review file `drafts/review-file-external-p7.md`.', '',
      '## Emit + cascade', '',
      'Builder gains a P7 section (9 non-inherit-child parents, appended BEFORE the P4 inherit loop) **and a '
      'P7B section (the three ial courses — themselves inherit children — appended AFTER it, the P2F shape)**: '
      'the first emit attempt lost the 85 direct ial rows to the inherit rebuild; the split is the committed '
      'fix. Children cascade through the committed containment map.', '',
      '| course (parent) | rows | medium/low | specs drafted (net new) | course coverage |',
      '| --- | --- | --- | --- | --- |']
for c in ORDER:
    s = summ[c]
    post = json.load(open(f'{HUB}/apps/hub/content/video-map/{c}.json'))['coverage']['specPointsMapped']
    net = post - pre[c]
    md.append(f"| {c} | {s['rows']} | {s['m']}/{s['l']} | {s['specs']} (+{net}) | {pre[c]} → **{post}** |")
md += ['', f'**Total: {tot_rows} owner-reviewed rows (M{tot_m}/L{tot_l}) onto 12 parent courses; '
       f'{casc} cascaded rows onto 24 child courses** (per-course: ' + '; '.join(f'{c.rsplit("-",1)[0] if len(c)<40 else c[:38]}… +{n}' for c, n in CASCADE[:6]) + ' …). '
       'The three ial parents additionally carry 10 spec-level inherited rows derived from the P7-enriched '
       'a-level parents (cascade artifacts inside parent files).', '',
      '## Gates', '',
      '- Full emit exit 0 (after the P7B split fix); all review-law/integrity gates pass; 0 `reviewed:false` '
      'in content.',
      '- Hub video-map tests **16/16** — the ial-chemistry-17 at-rest pin updated 42 → 70 (36 lesson rows = '
      '9 inherited + 27 P7 + 34 zero-weight anchors; anchor law unchanged).',
      '- Independent spec-join census: **100%** — 53 courses, **4,193** rows, 0 violations.',
      '- `next build` compiled + prerendered with DOM check on the videos pages (see hub PR).', '']
open(f'{RES}/docs/P7-CHANNEL-POOLS.md', 'w').write('\n'.join(md))
print('docs/P7-CHANNEL-POOLS.md written')
for c in ORDER:
    post = json.load(open(f'{HUB}/apps/hub/content/video-map/{c}.json'))['coverage']['specPointsMapped']
    print(f"  {c}: {pre[c]} -> {post} (net +{post - pre[c]}, draft distinct {summ[c]['specs']})")
