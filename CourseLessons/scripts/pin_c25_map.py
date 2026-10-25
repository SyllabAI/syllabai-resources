#!/usr/bin/env python3
"""pin_c25_map.py — u4:c25 Alkenes S0 spine-pinning (T-BOOK-058, trace 1a174d7a0e21fb09)
1. Writes the REFINED 11-section lesson.yaml (raw 8 -> authored 11 with receipt-disclosed
   re-homings; chunk census 20/20 single-home; slots 1095..1116 = 22 with 1105 + 1110
   absent (image-rendered equations dropped by the parse, restored from the PDF of record);
   bookPage monotonic 282..286).
2. Pins the course.yaml u4:c25 row: join_set (spine-derived 4.23-4.28 ALL CORE 6+0) +
   learning_objective (spine-verbatim '; '.join of T4:SUBd titles — all 6 spine titles;
   4.26 is ABSENT from the printed objectives list (5 printed bullets vs 6 spine points,
   f-0016 editorial-omission class, c23 4.13 precedent; content taught via the Table 25.1
   formulae, the isomers section and the addition equations); the 4.26 spine title glues
   two sentences "...unbranched-chain isomers knowledge of cis/trans..." — spine-canonical
   pin carried as-is and disclosed) + section_count 11 + pages [282, 286] (authored range;
   delta from the pre-derived raw [282, 285] disclosed — the questions-close section runs
   to printed p286, chunk-truth book_pages of 1115/1116 = [286, 286]).
Asserts all invariants BEFORE writing (c23/c24 pin precedent).
"""
import json, pathlib, yaml

ROOT = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons')
COURSE = ROOT / 'lessons/pearson-edexcel/international-gcse/chemistry-4ch1'
SPINE = pathlib.Path('/tmp/spine-19.json')
RAW = COURSE / 'section-maps/u4-c25.json'
PARSE = pathlib.Path('/tmp/chunks_v3.jsonl')

spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subd = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBd'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT'
              and 'igcse-chemistry-T4:SUBd' in (n.get('parents') or [])], key=lambda x: x['order'])
codes = [p['code'] for p in pts]
assert codes == ['4.23', '4.24', '4.25', '4.26', '4.27', '4.28'], codes
assert subd['title'] == 'Alkenes', subd['title']
app = [p['applicability'] for p in pts]
assert all(a['papers'] == ['1C', '2C'] and a['double_award_shared'] for a in app), 'ALL-CORE expected'

# learning_objective: spine-verbatim
titles = {p['code']: p['title'] for p in pts}
assert 'functional group >C=C<' in titles['4.23'], titles['4.23']
assert 'general formula for alkenes' in titles['4.24'], titles['4.24']
assert 'unsaturated hydrocarbons' in titles['4.25'], titles['4.25']
assert 'unbranched-chain isomers' in titles['4.26'], titles['4.26']
assert 'cis/trans or E/Z notation is not required' in titles['4.26'], titles['4.26']
assert 'dibromoalkanes' in titles['4.27'], titles['4.27']
assert 'bromine water' in titles['4.28'], titles['4.28']
learning_objective = '; '.join(titles[c] for c in codes)

P = 'chem_v3_u4_c25_pdf'
JOIN = codes
SECTIONS = [
 ('s01', 'Alkenes', 282,
  [P+'291_1095', P+'291_1096', P+'291_1097', P+'291_1098'],
  ['4.23', '4.24', '4.25'],
  ['alkene', 'functional-group', 'homologous-series', 'hydrocarbon', 'displayed-formula']),
 ('s02', 'Isomers', 283,
  [P+'292_1100'], ['4.26'],
  ['isomer', 'displayed-formula', 'molecular-formula']),
 ('s03', 'Unsaturated hydrocarbons', 283,
  [P+'292_1099'], ['4.25'],
  ['unsaturated-hydrocarbon', 'saturated-hydrocarbon', 'alkene']),
 ('s04', 'The general formula', 283,
  [P+'292_1101'], ['4.24'],
  ['general-formula', 'empirical-formula', 'molecular-formula']),
 ('s05', 'Combustion', 283,
  [P+'292_1102'], ['4.24'],
  ['complete-combustion', 'hydrocarbon']),
 ('s06', 'Addition', 283,
  [P+'292_1103'], ['4.27'],
  ['addition-reaction', 'functional-group', 'alkene']),
 ('s07', 'The addition of bromine', 284,
  [P+'293_1108', P+'293_1104', P+'293_1109'], ['4.27'],
  ['addition-reaction', 'dibromoalkane', 'alkene']),
 ('s08', 'The test for unsaturated compounds', 284,
  [P+'293_1106', P+'293_1107'], ['4.28'],
  ['bromine-water', 'unsaturated-hydrocarbon']),
 ('s09', 'Hydrogenation', 285,
  [P+'294_1113'], ['4.27'],
  ['hydrogenation', 'addition-reaction', 'alkane']),
 ('s10', 'Hydration', 285,
  [P+'294_1114', P+'294_1111'], ['4.27'],
  ['hydration', 'ethanol', 'catalyst']),
 ('s11', 'Chapter 25 questions', 286,
  [P+'294_1112', P+'295_1115', P+'295_1116'], JOIN,
  ['alkene', 'bromine-water', 'isomer', 'addition-reaction', 'general-formula',
   'unsaturated-hydrocarbon']),
]

# ---- invariants BEFORE writing ----
rawmap = json.load(open(RAW))
raw_refs = [r for s in rawmap['sections'] for r in s['chunkRefs']]
authored_refs = [r for s in SECTIONS for r in s[3]]
assert len(rawmap['sections']) == 8, len(rawmap['sections'])
assert set(raw_refs) <= set(authored_refs), 'raw not subset of authored'
census = set()
for line in open(PARSE, encoding='utf-8'):
    c = json.loads(line)
    if c.get('unit_no') == 4 and c.get('chapter_no') == 25:
        census.add(c['id'])
assert len(census) == 20, len(census)
assert set(authored_refs) == census, 'authored != census'
assert len(authored_refs) == len(set(authored_refs)) == 20, 'single-home violated'
# absent slots: the chapter's global sequence 1095..1116 = 22 numbers, 1105 + 1110 dropped
# by the parse (image-rendered equations; restored from the PDF of record — f-0026 recipe).
# NOTE: the id suffix is a book-wide running counter, NOT a per-pdf-page slot — pdf page
# numbers embedded in the ids vary (verified against the census).
suffixes = {int(c.rsplit('_', 1)[1]) for c in census}
assert suffixes == set(range(1095, 1117)) - {1105, 1110}, sorted(suffixes ^ set(range(1095, 1117)))
assert all(c.startswith(P) for c in census), 'unexpected id prefix in census'

# raw re-homing spot-asserts (receipt-disclosed)
def home(cid):
    return next(s[0] for s in SECTIONS if cid in s[3])
assert home(P+'292_1099') == 's03', 'unsaturated HINT -> s03 (raw s01; prints p283 beside the unsaturated text)'
assert home(P+'292_1101') == 's04', '1101 bulk home s04 (general-formula centre; UNSATURATED head P1 taught s03 prose, PHYSICAL PROPERTIES tail P4 taught s04 closing prose)'
assert home(P+'293_1104') == 's07', 'double HINT (decode name / formulae relate) -> s07 (prints p284 with the bromine-addition equation)'
assert home(P+'293_1106') == 's08', 'colourless-vs-clear HINT -> s08 (THE TEST FOR UNSATURATED COMPOUNDS block)'
assert home(P+'293_1107') == 's08', 'organic-layer EXTENSION -> s08'
assert home(P+'294_1111') == 's10', 'propene-hydration EXTENSION -> s10 (prints in the hydration block p285; raw s06)'
assert home(P+'294_1112') == 's11', 'CHAPTER QUESTIONS header -> s11 (questions close, c11-c24 precedent)'
assert home(P+'295_1115') == 's11' and home(P+'295_1116') == 's11', 'questions tables -> s11'
assert home(P+'294_1114') == 's10', 'hydration body bulk home s10 (questions tail glued after END OF CHEMISTRY ONLY taught s11 prose)'

pages = [s[2] for s in SECTIONS]
assert pages == sorted(pages), pages
assert pages[0] == 282 and pages[-1] == 286, pages

# join_set coverage: every spine point anchored by >=1 authored section
anchored = {c for s in SECTIONS for c in s[4]}
assert set(codes) <= anchored, f'spine points uncovered: {set(codes) - anchored}'

# ---- write lesson.yaml (refined) ----
lesson = {
    'lesson_id': 'u4-c25-alkenes',
    'chapter_key': 'u4:c25',
    'course_id': 'chemistry-4ch1',
    'title': 'Alkenes',
    'chem_only': False,
    'stage': 'S0',
    'book_page_range': [282, 286],
    'sections': [
        {'id': f'u4:c25:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'glossary': list(glo), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
    'features': {k: False for k in [
        'prior_knowledge', 'cross_curricular', 'misconceptions',
        'ms_vocab', 'glossary_chips', 'quick_checks', 'summary', 'can_you']},
    'receipts': [],
    'notes': ('S0 refined spine pinned by pin_c25_map.py (T-BOOK-058 r0): raw 8 -> authored '
              '11 sections, 20/20 census chunks single-home, raw superset, slots 1095..1116 '
              '= 22 with 1105 + 1110 absent (image-rendered equations dropped by the parse; '
              'restored from the PDF of record via 300-dpi crop OCR + atom-balance '
              'verification, f-0026 recipe); join_set DERIVED at S0-L0 from the printed '
              'objectives list (chunk 1096, 5 bullets) x spine igcse-chemistry-T4:SUBd = '
              '4.23-4.28 ALL CORE 6+0 (papers [1C,2C]; fourth consecutive ALL-CORE pack '
              'after c22 6+0, c23 12+0, c24 4+0); 4.26 ABSENT from the printed list '
              '(f-0016 editorial-omission class, c23 4.13 precedent; taught via the first-'
              'three-alkenes formulae table, the isomers section and the addition product '
              'formulae) and the 4.26 spine title glues two sentences (spine-canonical pin); '
              're-homings mirror the PRINTED book order: 1099 raw-s01 -> s03, 1101 raw-s03 '
              '-> s04 bulk home (UNSATURATED head P1 taught s03 prose, PHYSICAL PROPERTIES '
              'tail P4 taught s04 closing prose), 1104 raw-s05 -> s07, 1106/1107 raw-s05 -> '
              's08 (THE TEST FOR UNSATURATED COMPOUNDS promoted to its own authored section '
              'per the printed heading the parse glued into 1108), 1108 split home s07 by '
              'bulk with the test tail taught s08, 1109 split home s07 (propene paragraphs) '
              'with the OTHER IMPORTANT ADDITION REACTIONS tail taught s09 intro, 1111 '
              'raw-s06 -> s10, 1112 raw-s06 -> s11, 1114 split home s10 (hydration body) '
              'with the questions tail taught s11, 1115/1116 raw-s08 -> s11 (questions close '
              'split, c11-c24 precedent); the printed CHEMISTRY ONLY banner sits between '
              'Hydrogenation and Hydration (p285, verified by page OCR; the parse dropped '
              'the banner chunk) — hydration is the chemistry-only block bridging to Chapter '
              '26, taught in s10 with the boundary disclosed while the pack paperRoute stays '
              'core per the join_set; pages [282,286] authored range (raw pre-derived '
              '[282,285]; questions close runs to printed p286)'),
}
lp = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/'
                  'international-gcse/chemistry-4ch1/lessons/u4-c25-alkenes/lesson.yaml')
lp.parent.mkdir(parents=True, exist_ok=True)
lp.write_text(yaml.safe_dump(lesson, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- pin course.yaml row ----
cp = COURSE / 'course.yaml'
cfg = yaml.safe_load(cp.read_text(encoding='utf-8'))
hit = False
for rows in cfg['spine'].values():
    for r in rows:
        if r['key'] == 'u4:c25':
            r['join_set'] = JOIN
            r['learning_objective'] = learning_objective
            r['section_count'] = 11
            r['pages'] = [282, 286]
            hit = True
assert hit, 'u4:c25 row not found'
cp.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- regenerate committed section map to the REFINED authored set (c23/c24 precedent:
#      S0.3b asserts the committed map carries the refined section set) ----
refined_map = {
    'chapter_key': 'u4:c25',
    'key_mapping': rawmap['key_mapping'],
    'book_page_range': [282, 286],
    'sections': [
        {'id': f'u4:c25:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
}
sm_path = COURSE / 'section-maps/u4-c25.json'
sm_path.write_text(json.dumps(refined_map, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('pin_c25_map: OK — lesson.yaml refined (11 sections / 20 chunks single-home / 22 slots '
      'with 1105+1110 absent), course row pinned (join_set 4.23-4.28 ALL CORE 6+0, '
      'section_count 11, pages [282,286]), section-maps/u4-c25.json regenerated to the '
      'refined authored set')
