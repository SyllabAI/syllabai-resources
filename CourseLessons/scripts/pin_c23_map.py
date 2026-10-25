#!/usr/bin/env python3
"""pin_c23_map.py — u4:c23 Crude oil S0 spine-pinning (T-BOOK-056 r0, trace 1a1744f21add5f0d)
1. Writes the REFINED 9-section lesson.yaml (raw 8 -> authored 9 with receipt-disclosed
   re-homings; chunk superset 26/26 single-home; bookPage monotonic 268..275).
2. Pins the course.yaml u4:c23 row: join_set (spine-derived 4.7-4.18 ALL CORE 12+0) +
   learning_objective (spine-verbatim '; '.join of T4:SUBb titles — all 12 spine titles
   COMPLETE; note the 4.17 glyph-variant spine "600-700 \u00baC" [U+00BA ordinal] vs chunk
   1050 "600-700 \u00b0C" [U+00B0 degree], spine-canonical pin disclosed at f-0016 class) +
   section_count 9 + pages [268, 275] (authored range; delta from the pre-derived raw
   [268, 273] disclosed — the questions-close section starts at printed p275).
Asserts all invariants BEFORE writing (c22 pin_c22_map precedent).
"""
import json, sys, pathlib, yaml

ROOT = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons')
COURSE = ROOT / 'lessons/pearson-edexcel/international-gcse/chemistry-4ch1'
SPINE = pathlib.Path('/home/z/my-project/repos/v2-main/apps/hub/spines/igcse-chemistry-19.json')
RAW = COURSE / 'section-maps/u4-c23.json'
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')

spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subb = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBb'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT'
              and 'igcse-chemistry-T4:SUBb' in (n.get('parents') or [])], key=lambda x: x['order'])
codes = [p['code'] for p in pts]
assert codes == ['4.7', '4.8', '4.9', '4.10', '4.11', '4.12', '4.13', '4.14',
                 '4.15', '4.16', '4.17', '4.18'], codes
assert subb['title'] == 'Crude oil', subb['title']
app = [p['applicability'] for p in pts]
assert all(a['papers'] == ['1C', '2C'] and a['double_award_shared'] for a in app), 'ALL-CORE expected'

# learning_objective: spine-verbatim, with the ONE disclosed 4.17 completion
titles = {p['code']: p['title'] for p in pts}
# 4.17 spine title is COMPLETE (191 chars) but carries the ordinal-indicator glyph
# U+00BA where the specification/chunk use U+00B0 degree — glyph-variant class,
# spine-canonical pin (f-0016); disclosed here, never repaired silently.
assert '\u00baC' in titles['4.17'] and 'in the range of 600\u2013700 \u00baC)' in titles['4.17'], titles['4.17']
learning_objective = '; '.join(titles[c] for c in codes)

P = 'chem_v3_u4_c23_pdf'
JOIN = codes
SECTIONS = [
 ('s01', 'Crude oil', 268,
  [P+'277_1049', P+'277_1050'], JOIN,
  ['crude-oil', 'hydrocarbon', 'fossil-fuel']),
 ('s02', 'What crude oil is', 269,
  [P+'278_1051', P+'278_1054'], ['4.7'],
  ['crude-oil', 'hydrocarbon', 'non-renewable', 'intermolecular-forces']),
 ('s03', 'How molecule size changes properties', 269,
  [P+'278_1053', P+'278_1055', P+'279_1056'], ['4.10'],
  ['volatile', 'viscosity', 'boiling-point', 'intermolecular-forces']),
 ('s04', 'Separating crude oil: fractional distillation', 270,
  [P+'279_1057', P+'279_1058', P+'279_1059'], ['4.8', '4.10'],
  ['fraction', 'fractional-distillation', 'fractionating-column', 'residue']),
 ('s05', 'Fuels and combustion', 270,
  [P+'279_1060', P+'280_1061', P+'280_1062', P+'280_1063'],
  ['4.11', '4.12', '4.13'],
  ['fuel', 'complete-combustion', 'incomplete-combustion', 'carbon-monoxide']),
 ('s06', 'The fractions and their uses', 271,
  [P+'280_1064', P+'281_1065'], ['4.9', '4.10'],
  ['refinery-gases', 'gasoline', 'kerosene', 'diesel', 'fuel-oil', 'bitumen']),
 ('s07', 'Burning fuels and the environment', 272,
  [P+'281_1066', P+'282_1068', P+'282_1069'], ['4.14', '4.15', '4.16'],
  ['greenhouse-gas', 'sulfur-dioxide', 'oxides-of-nitrogen', 'acid-rain']),
 ('s08', 'Cracking', 273,
  [P+'282_1070', P+'283_1072', P+'283_1073'], ['4.17', '4.18'],
  ['cracking', 'thermal-decomposition', 'catalyst', 'alkane', 'alkene']),
 ('s09', 'Chapter 23 questions', 275,
  [P+'284_1075', P+'284_1076', P+'284_1077', P+'284_1078'], JOIN,
  ['crude-oil', 'hydrocarbon', 'fraction', 'fuel', 'carbon-monoxide', 'acid-rain', 'cracking']),
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
    if c.get('unit_no') == 4 and c.get('chapter_no') == 23:
        census.add(c['id'])
assert len(census) == 26, len(census)
assert set(authored_refs) == census, 'authored != census'
assert len(authored_refs) == len(set(authored_refs)) == 26, 'single-home violated'

# raw re-homing spot-asserts (receipt-disclosed)
def home(cid):
    return next(s[0] for s in SECTIONS if cid in s[3])
assert home(P+'278_1053') == 's03', 'volatile HINT -> s03 (raw s02)'
assert home(P+'278_1054') == 's02', 'what-is-crude-oil body -> s02 (raw s03)'
assert home(P+'279_1057') == 's04', 'fractions-disagreement HINT -> s04 (raw s03)'
assert home(P+'280_1062') == 's05' and home(P+'280_1063') == 's05', 'combustion+CO -> s05 (raw s06)'
assert home(P+'280_1064') == 's06' and home(P+'281_1065') == 's06', 'fraction uses -> s06 (raw s06)'
assert home(P+'284_1075') == 's09', 'questions bank chunkRef home s09 (prose taught s08; c22 1044 precedent)'

pages = [s[2] for s in SECTIONS]
assert pages == sorted(pages), pages
assert pages[0] == 268 and pages[-1] == 275, pages

# ---- write lesson.yaml (refined) ----
lesson = {
    'lesson_id': 'u4-c23-crude-oil',
    'chapter_key': 'u4:c23',
    'course_id': 'chemistry-4ch1',
    'title': 'Crude oil',
    'chem_only': False,
    'stage': 'S0',
    'book_page_range': [268, 275],
    'sections': [
        {'id': f'u4:c23:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'glossary': list(glo), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
    'features': {k: False for k in [
        'prior_knowledge', 'cross_curricular', 'misconceptions',
        'ms_vocab', 'glossary_chips', 'quick_checks', 'summary', 'can_you']},
    'receipts': [],
    'notes': ('S0 refined spine pinned by pin_c23_map.py (T-BOOK-056 r0): raw 8 -> authored 9 '
              'sections, 26/26 census chunks single-home, raw superset; join_set DERIVED at S0-L0 '
              'from the SINGLE objectives chunk 1050 x spine igcse-chemistry-T4:SUBb = 4.7-4.18 '
              'ALL CORE 12+0 (second consecutive ALL-CORE pack after c22); chunk 1050 carries 11 '
              'bullets for 12 spine points - 4.13 bullet ABSENT from the printed list (editorial '
              'omission class) while the chapter teaches CO poisoning at 1063/1064 (spine-canonical '
              'pin); 4.17 spine glyph-variant U+00BA vs chunk U+00B0 (spine-canonical, disclosed); '
              '4.14/4.18 chunk drops spine commas; capitalisation class on all bullets; '
              'pages [268,275] authored range (raw pre-derived [268,273]; questions close starts p275)'),
}
lp = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/'
                  'international-gcse/chemistry-4ch1/lessons/u4-c23-crude-oil/lesson.yaml')
lp.write_text(yaml.safe_dump(lesson, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- pin course.yaml row ----
cp = COURSE / 'course.yaml'
cfg = yaml.safe_load(cp.read_text(encoding='utf-8'))
hit = False
for rows in cfg['spine'].values():
    for r in rows:
        if r['key'] == 'u4:c23':
            r['join_set'] = JOIN
            r['learning_objective'] = learning_objective
            r['section_count'] = 9
            r['pages'] = [268, 275]
            hit = True
assert hit, 'u4:c23 row not found'
cp.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

print('pin_c23_map: OK — lesson.yaml refined (9 sections / 26 chunks single-home), '
      'course row pinned (join_set 4.7-4.18 ALL CORE 12+0, section_count 9, pages [268,275])')
