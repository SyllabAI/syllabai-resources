#!/usr/bin/env python3
"""pin_c26_map.py — u4:c26 Alcohols S0 spine-pinning (T-BOOK-059, trace 1a175004e0eb6081)
1. Writes the REFINED 9-section lesson.yaml (raw 7 -> authored 9 with receipt-disclosed
   re-homings; chunk census 21/21 single-home; slots 1117..1141 = 25 with 1120, 1125,
   1134, 1135 absent — 1125 + one of 1134/1135 are the image-rendered equation objects
   ([O] oxidation; sucrose hydrolysis) restored from the PDF of record; bookPage monotonic
   287..292).
2. Pins the course.yaml u4:c26 row: join_set (spine-derived 4.29C-4.33C ALL CHEMISTRY-ONLY
   0+5 — the FIRST all-C pack since c15, fifth overall) + learning_objective (spine-verbatim
   '; '.join of T4:SUBe titles — all 5 spine titles incl. their bullet tails; the 4.30C spine
   title glues two sentences "...name each compound the names propanol and butanol are
   acceptable" — spine-canonical pin carried as-is and disclosed; the 4.31C/4.32C chunk
   renders dichromate as (Vl) vs spine (VI) — l/I glyph class, spine-canonical) +
   section_count 9 + pages [287, 292] (authored range; delta from the pre-derived raw
   [287, 291] disclosed — the questions close runs to printed p292 where END OF CHEMISTRY
   ONLY also prints). chem_only stays true (spine applicability governs; the printed
   CHEMISTRY ONLY banner sits ABOVE the chapter heading on p287 and END OF CHEMISTRY ONLY
   closes p292 — whole-chapter block).
Asserts all invariants BEFORE writing (c23/c24/c25 pin precedent).
"""
import json, pathlib, yaml

ROOT = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons')
COURSE = ROOT / 'lessons/pearson-edexcel/international-gcse/chemistry-4ch1'
SPINE = pathlib.Path('/tmp/spine-19.json')
RAW = COURSE / 'section-maps/u4-c26.json'
PARSE = pathlib.Path('/tmp/chunks_v3.jsonl')

spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
sube = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBe'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT'
              and 'igcse-chemistry-T4:SUBe' in (n.get('parents') or [])], key=lambda x: x['order'])
codes = [p['code'] for p in pts]
assert codes == ['4.29C', '4.30C', '4.31C', '4.32C', '4.33C'], codes
assert sube['title'] == 'Alcohols', sube['title']
app = [p['applicability'] for p in pts]
assert all(a['papers'] == ['2C'] and not a['double_award_shared'] for a in app), 'ALL-C expected'

# learning_objective: spine-verbatim
titles = {p['code']: p['title'] for p in pts}
assert 'functional group' in titles['4.29C'] and 'OH' in titles['4.29C'], titles['4.29C']
assert 'propan-1-ol only' in titles['4.30C'], titles['4.30C']
assert 'potassium dichromate(VI) in dilute sulfuric acid' in titles['4.31C'], titles['4.31C']
assert 'fermentation of glucose' in titles['4.32C'], titles['4.32C']
assert 'reasons for fermentation' in titles['4.33C'], titles['4.33C']
learning_objective = '; '.join(titles[c] for c in codes)

P = 'chem_v3_u4_c26_pdf'
JOIN = codes
ALL5 = list(codes)
SECTIONS = [
 ('s01', 'Alcohols', 287,
  [P+'296_1117', P+'296_1118'], ALL5,
  ['alcohol', 'functional-group', 'homologous-series', 'ethanol']),
 ('s02', 'Drawing and naming the alcohols', 288,
  [P+'297_1119', P+'297_1121', P+'297_1122', P+'297_1123'], ['4.30C'],
  ['molecular-formula', 'structural-formula', 'displayed-formula', 'isomer', 'methanol']),
 ('s03', 'Ethanol burns in air', 288,
  [P+'297_1124'], ['4.31C'],
  ['complete-combustion', 'biofuel', 'ethanol']),
 ('s04', 'Microbial oxidation', 289,
  [P+'298_1126'], ['4.31C'],
  ['microbial-oxidation', 'ethanoic-acid']),
 ('s05', 'Lab oxidation with acidified potassium dichromate(VI)', 289,
  [P+'298_1127', P+'298_1128', P+'298_1129', P+'299_1130', P+'299_1131'], ['4.31C'],
  ['oxidising-agent', 'reflux', 'ethanoic-acid']),
 ('s06', 'Making ethanol by fermentation', 290,
  [P+'299_1132', P+'299_1133'], ['4.32C', '4.33C'],
  ['fermentation', 'glucose', 'enzyme', 'yeast', 'anaerobic']),
 ('s07', 'Making ethanol by the hydration of ethene', 291,
  [P+'300_1136'], ['4.32C'],
  ['hydration', 'ethanol', 'catalyst']),
 ('s08', 'Comparing the two methods of producing ethanol', 291,
  [P+'300_1137', P+'300_1138', P+'300_1139'], ['4.32C'],
  ['batch-process', 'continuous-process', 'fractional-distillation']),
 ('s09', 'Chapter 26 questions', 292,
  [P+'301_1140', P+'301_1141'], ALL5,
  ['alcohol', 'ethanol', 'fermentation', 'hydration', 'ethanoic-acid', 'isomer']),
]

# ---- invariants BEFORE writing ----
rawmap = json.load(open(RAW))
raw_refs = [r for s in rawmap['sections'] for r in s['chunkRefs']]
authored_refs = [r for s in SECTIONS for r in s[3]]
assert len(rawmap['sections']) == 7, len(rawmap['sections'])
assert set(raw_refs) <= set(authored_refs), 'raw not subset of authored'
census = set()
for line in open(PARSE, encoding='utf-8'):
    c = json.loads(line)
    if c.get('unit_no') == 4 and c.get('chapter_no') == 26:
        census.add(c['id'])
assert len(census) == 21, len(census)
assert set(authored_refs) == census, 'authored != census'
assert len(authored_refs) == len(set(authored_refs)) == 21, 'single-home violated'
# absent slots: chapter's global sequence 1117..1141 = 25 numbers, 1120/1125/1134/1135 dropped
# by the parse (1125 = the [O] oxidation displayed-equation object; 1134/1135 class = the
# sucrose-hydrolysis equation object + a hydration-block fragment; 1120 = a p288 element with
# no print-content loss detected between the HINT box and the DRAWING AND NAMING heading).
suffixes = {int(c.rsplit('_', 1)[1]) for c in census}
assert suffixes == set(range(1117, 1142)) - {1120, 1125, 1134, 1135}, sorted(suffixes ^ set(range(1117, 1142)))
assert all(c.startswith(P) for c in census), 'unexpected id prefix in census'

# raw re-homing spot-asserts (receipt-disclosed)
def home(cid):
    return next(s[0] for s in SECTIONS if cid in s[3])
assert home(P+'297_1119') == 's02', 'double HINT (O-H bond + acceptable names) -> s02 (prints p288 beside the drawing section)'
assert home(P+'297_1124') == 's03', 'oxidation parent chunk bulk home s03 (ETHANOL BURNS IN AIR sub-heading promoted; MICROBIAL OXIDATION heading tail taught s04)'
assert home(P+'298_1126') == 's04', 'acetic-acid DID YOU KNOW -> s04 (microbial oxidation block)'
assert home(P+'298_1128') == 's05', '1128 TRIPLE-GLUED bulk home s05 (wine/vinegar head taught s04; dichromate-naming EXTENSION + lab body taught s05)'
assert home(P+'299_1130') == 's05', '1130 home s05 (Fig 26.5 conditions box belongs to the lab oxidation; fermentation heading tail taught s06)'
assert home(P+'299_1133') == 's06', '1133 bulk home s06 (biochemistry + equations + conditions; REMINDER + hydration heading tail taught s06/s07 boundary)'
assert home(P+'300_1136') == 's07', '1136 MULTI-GLUED home s07 (yeast-15% head taught s06 tail; KEY POINT + hydration body + conditions + recycle taught s07)'
assert home(P+'301_1140') == 's09' and home(P+'301_1141') == 's09', 'questions bank -> s09 (questions close, c11-c25 precedent)'

pages = [s[2] for s in SECTIONS]
assert pages == sorted(pages), pages
assert pages[0] == 287 and pages[-1] == 292, pages

# join_set coverage: every spine point anchored by >=1 authored section
anchored = {c for s in SECTIONS for c in s[4]}
assert set(codes) <= anchored, f'spine points uncovered: {set(codes) - anchored}'

# ---- write lesson.yaml (refined) ----
lesson = {
    'lesson_id': 'u4-c26-alcohols',
    'chapter_key': 'u4:c26',
    'course_id': 'chemistry-4ch1',
    'title': 'Alcohols',
    'chem_only': True,
    'stage': 'S0',
    'book_page_range': [287, 292],
    'sections': [
        {'id': f'u4:c26:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'glossary': list(glo), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
    'features': {k: False for k in [
        'prior_knowledge', 'cross_curricular', 'misconceptions',
        'ms_vocab', 'glossary_chips', 'quick_checks', 'summary', 'can_you']},
    'receipts': [],
    'notes': ('S0 refined spine pinned by pin_c26_map.py (T-BOOK-059 r0): raw 7 -> authored '
              '9 sections, 21/21 census chunks single-home, raw superset, slots 1117..1141 '
              '= 25 with 1120/1125/1134/1135 absent (image-rendered equation objects dropped '
              'by the parse; restored from the PDF of record via 300-dpi crop OCR + '
              'atom-balance verification, f-0026/f-0028-gated recipe); join_set DERIVED at '
              'S0-L0 from the printed objectives box (chunk 1118, all FIVE bullets present '
              'but interleaved with the chapter intro prose by the parse) x spine '
              'igcse-chemistry-T4:SUBe = 4.29C-4.33C ALL CHEMISTRY-ONLY 0+5 (papers [2C]; '
              'double_award_shared false) — the FIRST ALL-C pack since c15 and the fifth '
              'overall (f-0015 sibling audit run substantively: c22/c23/c24/c25 ALL-CORE '
              'before, c26 ALL-C after — the mixed-shape ledger has no drift); chem_only: '
              'true (spine applicability governs; the printed CHEMISTRY ONLY banner sits '
              'ABOVE the chapter heading on p287 and END OF CHEMISTRY ONLY closes p292 '
              '— whole-chapter block, per the f-0027 locator law); DISCLOSED f-0016 covers '
              '(spine-canonical pins): the 4.30C spine title glues two sentences '
              '("...name each compound the names propanol and butanol are acceptable" — '
              'missing separator; the acceptable-names rule taught in s02 prose + exam-hint); '
              'the chunk renders dichromate as (Vl) vs spine (VI) — l/I glyph class; LO box '
              'glue class (bullets interleaved with intro prose in 1118, no point missing); '
              're-homings mirror the PRINTED book order: 1119 raw-s01 -> s02, 1124 raw-s03 '
              'bulk home s03 (ETHANOL BURNS IN AIR sub-heading promoted to authored s03 — '
              'the parse dropped the sub-heading; MICROBIAL OXIDATION heading tail taught '
              's04), 1126 raw-s03 -> s04, 1128 TRIPLE-GLUED bulk home s05 (wine/vinegar head '
              'taught s04; dichromate-naming EXTENSION + lab body taught s05), 1130 raw-s05 '
              'home s05 (its Fig 26.5 conditions box belongs to the lab oxidation; '
              'fermentation heading tail taught s06), 1133 bulk home s06 (REMINDER tail + '
              'hydration heading taught s06/s07 boundary), 1136 MULTI-GLUED home s07 '
              '(yeast-15% head taught s06 tail; KEY POINT + hydration + conditions + recycle '
              'taught s07), 1140/1141 -> s09 (questions close, c11-c25 precedent); TWO '
              'absent display equations RESTORED byte-precise from the PDF of record: '
              'CH3CH2OH + 2[O] -> CH3COOH + H2O (chunk 1125 absent — the Fig 26.5 displayed '
              'oxidation) and C12H22O11(aq) + H2O(l) -> C6H12O6(aq) + C6H12O6(aq) (sucrose '
              'hydrolysis, 1134/1135 class) — plus in-chunk repairs: combustion (I)->(l) '
              'l/I class, fermentation spacing/comma garble, hydration flat-digit subscripts '
              '+ (H3PO)->(H3PO4); the print-true SAFETY note (eye protection / spit hazard '
              'at Fig 26.4) is UNTYPED in the parse (0 safety census chunks) — taught as the '
              's05 safety box with the census-mismatch disclosed; pages [287,292] authored '
              'range (raw pre-derived [287,291]; questions close runs to printed p292)'),
}
lp = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/'
                  'international-gcse/chemistry-4ch1/lessons/u4-c26-alcohols/lesson.yaml')
lp.parent.mkdir(parents=True, exist_ok=True)
lp.write_text(yaml.safe_dump(lesson, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- pin course.yaml row ----
cp = COURSE / 'course.yaml'
cfg = yaml.safe_load(cp.read_text(encoding='utf-8'))
hit = False
for rows in cfg['spine'].values():
    for r in rows:
        if r['key'] == 'u4:c26':
            r['join_set'] = JOIN
            r['learning_objective'] = learning_objective
            r['section_count'] = 9
            r['pages'] = [287, 292]
            hit = True
assert hit, 'u4:c26 row not found'
cp.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- regenerate committed section map to the REFINED authored set ----
refined_map = {
    'chapter_key': 'u4:c26',
    'key_mapping': rawmap['key_mapping'],
    'book_page_range': [287, 292],
    'sections': [
        {'id': f'u4:c26:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
}
sm_path = COURSE / 'section-maps/u4-c26.json'
sm_path.write_text(json.dumps(refined_map, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('pin_c26_map: OK — lesson.yaml refined (9 sections / 21 chunks single-home / 25 slots '
      'with 1120+1125+1134+1135 absent), course row pinned (join_set 4.29C-4.33C ALL-C 0+5, '
      'section_count 9, pages [287,292]), section-maps/u4-c26.json regenerated to the '
      'refined authored set')
