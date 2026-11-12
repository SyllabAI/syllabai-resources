#!/usr/bin/env python3
"""P7: write the lane review file (drafts/review-file-external-p7.md)."""
import json

RES = '/home/z/my-project/repos/syllabai-resources/Videos'
W = '/home/z/my-project/work/p7'

summ = json.load(open(f'{W}/summary.json'))
ORDER = ['cie-a-level-biology-25', 'cie-a-level-chemistry-25', 'cie-a-level-physics-25',
         'cie-igcse-biology-23', 'cie-igcse-chemistry-23', 'cie-igcse-physics-23',
         'ial-biology-18', 'ial-chemistry-17', 'ial-physics-19',
         'igcse-biology-19', 'igcse-chemistry-19', 'igcse-physics-19']

tot_rows = sum(summ[c]['rows'] for c in ORDER)
tot_rej = sum(summ[c]['rejects'] for c in ORDER)
tot_m = sum(summ[c]['m'] for c in ORDER)
tot_l = sum(summ[c]['l'] for c in ORDER)

md = ['# Review file — external lane P7 (T-VIDEOMAP-P7, remaining external channel pools)', '',
      'Lane: the unmapped remainder of four previously-mined channel pools — amoeba-sisters (179), '
      'freesciencelessons (776), malmesbury-education (72), doodlescience (58) — re-enumerated fresh before '
      'the lane (0 deltas on all four) and union-excluded against the current corpus (417 of the 1,085 pool '
      'videos already mapped across the union). Authorized owner chat 2026-11-13 ("Proceed with remaining '
      'channel pools"). Prior-lane precedents carried: the P2B/P2C/P2D mines took the easy wins (372 FSL, 20 '
      'doodle, 19 amoeba, 6 malmesbury videos already mapped); this lane re-adjudicates the REMAINDER under '
      'the same tightened binding rule (title-only evidence; the title must name the spec\'s distinctive '
      'content) against the CURRENT corpus state (post-P5/P6). Deterministic distinctive-token pre-pass then '
      'a full agent judgment pass over every row (keeps, re-binds, drops all tabled and title-asserted). '
      'Delegated self-review per owner chat 2026-11-09 "approve and review yourself".', '',
      '## Census', '',
      '| course | rows | medium/low | specs drafted | reject ledger |',
      '| --- | --- | --- | --- | --- |']
for c in ORDER:
    s = summ[c]
    md.append(f"| {c} | {s['rows']} | {s['m']}/{s['l']} | {s['specs']}/{s['total']} | {s['rejects']} |")
md += ['', f'**Total: {tot_rows} rows (M{tot_m}/L{tot_l}) across 12 parent courses; {tot_rej} reject-ledger '
       'entries; identity sweep 277/277 verified (159 oEmbed + 118 thumb-fallback for the freesciencelessons '
       'embedding-disabled A-level videos, per the P2D identity law).**', '',
       '## Routing', '',
      'Subject-marker routing per channel shape: freesciencelessons self-annotates (GCSE/A-level × '
      'biology/chemistry/physics) → idf best-of within the subject\'s four parent spines; amoeba-sisters → '
      'biology parents; malmesbury → subject by practical titles; doodlescience → physics markers. '
      '516 routed / 152 skipped (73 sewage — promos, exam-technique, non-science channel content (malmesbury '
      'English-Lit poem analyses, language lessons, KS3, DT); 40 amoeba no-biology-vocabulary; 28 '
      'no-spine-overlap; 11 misc). Non-science malmesbury content is honestly skipped — SyllabAI\'s 53-flagged '
      'video-map course set has no English-Lit/languages/KS3 lane.', '',
      '## Judgment pass (self-review)', '',
      f'The deterministic distinctive-token pre-pass proposed 388 binds; the agent judgment pass tabled every '
      f'row: {tot_rows} kept (re-binds and trims applied in-table), 138 full-row drops with reasons, plus the '
      f'pre-pass no-binding rejects — {tot_rej} reject-ledger entries in total. Misbind classes caught:', '',
      '- **IAL CORE-PRACTICAL magnet**: spec 6.4 (CP13 growth-rate practical) attached itself to 18 unrelated '
      'IAL-biology rows via generic tokens — dropped everywhere except the two genuine practicals;',
      '- **FSL practise-questions drills**: generic calculation-practice videos (standard enthalpy cycles, bond '
      'enthalpies, titration calcs) rejected wholesale per the P6 maths-drill class — no distinctive content '
      'named;',
      '- **cross-subject misroutes**: Doodle physics videos routed by idf onto biology specs (nuclear '
      'radiation → mitosis; eye-vs-camera → eye-structure) — dropped, not re-bound;',
      '- **AQA-specific content absent from the spines** (verified against the spine text before any '
      'rebind): homeobox genes, insect tracheal systems, dialysis, cofactors, potometers, oestrogen-cancer '
      '— rejected per the P2E/P6 board-absence class;',
      '- **US-curriculum divergence** (amoeba): protein-synthesis/genetics videos whose honest UK targets '
      'the pre-pass missed were dropped rather than force-bound; genuine matches kept (specialised cells, '
      'meiosis, Punnett squares, nephron, trophic levels);',
      '- **channel-author discovery**: DoodleScience\'s oEmbed author string has no space — the expected-author '
      'map was corrected before any row shipped (250/250 → 277/277 after the ial-chemistry table landed).', '',
      '## Borderline kept rows (disclosed low-confidence partial overlaps)', '',
      '- FSL AQA→CIE/Edexcel-IAL pairs (boardMismatch:true throughout, the P2D conservative-binding posture): '
      'Year-13 inheritance/spec videos bound on topic where the CIE/IAL spec names the same content '
      '(autosomal linkage, codominant alleles, lac operon, Krebs cycle, loop of Henle, sinoatrial control);',
      '- apparatus-step partials kept low: reaction-time/decay/chromatography/food-test practicals bound to '
      'the nearest honest spec with the procedure half disclosed;',
      '- amoeba OLD-video remakes kept when the remake is a distinct ID and the bind is genuine;', '',
      '## Honest no-target census', '',
      'Of the 668 union-unmapped pool videos: 516 routed into this lane, 152 skipped with no honest spine '
      'target (73 sewage incl. all non-science malmesbury content, 40 no-biology-vocabulary amoeba, 28 '
      'no-spine-overlap, 11 misc). Of the 516 routed, 277 bound and 239 stay unmapped with reasoned '
      'reject-ledger entries (the prior-lane reject classes above; pre-pass no-binding rejects recorded '
      'per course in the verdicts).', '']
open(f'{RES}/drafts/review-file-external-p7.md', 'w').write('\n'.join(md))
print('review file written:', f'{RES}/drafts/review-file-external-p7.md')
