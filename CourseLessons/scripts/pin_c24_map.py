#!/usr/bin/env python3
"""pin_c24_map.py — u4:c24 Alkanes S0 spine-pinning (T-BOOK-057, trace 1a174aa15579a90d)
1. Writes the REFINED 8-section lesson.yaml (raw 5 -> authored 8 with receipt-disclosed
   re-homings; chunk superset 16/16 single-home; bookPage monotonic 277..281).
2. Pins the course.yaml u4:c24 row: join_set (spine-derived 4.19-4.22 ALL CORE 4+0) +
   learning_objective (spine-verbatim '; '.join of T4:SUBc titles — all 4 spine titles;
   4.21 chunk drops the spine comma "molecule, and to name"; 4.22 chunk truncates the
   spine tail "knowledge of reaction mechanisms is not required" — spine-canonical pins
   disclosed at the f-0016 class) + section_count 8 + pages [277, 281] (authored range;
   delta from the pre-derived raw [277, 279] disclosed — the questions-close section
   starts at printed p281, substitution content runs to p280).
Asserts all invariants BEFORE writing (c23 pin_c23_map precedent).
"""
import json, sys, pathlib, yaml

ROOT = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons')
COURSE = ROOT / 'lessons/pearson-edexcel/international-gcse/chemistry-4ch1'
SPINE = pathlib.Path('/home/z/my-project/repos/v2-main/apps/hub/spines/igcse-chemistry-19.json')
RAW = COURSE / 'section-maps/u4-c24.json'
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')

spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subc = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBc'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT'
              and 'igcse-chemistry-T4:SUBc' in (n.get('parents') or [])], key=lambda x: x['order'])
codes = [p['code'] for p in pts]
assert codes == ['4.19', '4.20', '4.21', '4.22'], codes
assert subc['title'] == 'Alkanes', subc['title']
app = [p['applicability'] for p in pts]
assert all(a['papers'] == ['1C', '2C'] and a['double_award_shared'] for a in app), 'ALL-CORE expected'

# learning_objective: spine-verbatim
titles = {p['code']: p['title'] for p in pts}
assert 'general formula for alkanes' in titles['4.19'], titles['4.19']
assert 'saturated hydrocarbons' in titles['4.20'], titles['4.20']
assert 'unbranched-chain isomers' in titles['4.21'], titles['4.21']
assert 'ultraviolet radiation' in titles['4.22'], titles['4.22']
learning_objective = '; '.join(titles[c] for c in codes)

P = 'chem_v3_u4_c24_pdf'
JOIN = codes
SECTIONS = [
 ('s01', 'Alkanes', 277,
  [P+'286_1079', P+'286_1080', P+'286_1081', P+'286_1082'], JOIN,
  ['alkane', 'hydrocarbon', 'saturated-hydrocarbon', 'general-formula']),
 ('s02', 'Isomers of alkanes', 278,
  [P+'287_1085'], ['4.21'],
  ['isomer', 'molecular-formula', 'structural-formula', 'displayed-formula']),
 ('s03', 'Homologous series', 278,
  [P+'287_1083', P+'287_1086'], ['4.19'],
  ['homologous-series', 'functional-group', 'general-formula']),
 ('s04', 'Members of a homologous series have the same general formula', 278,
  [P+'287_1084'], ['4.19', '4.21'],
  ['general-formula', 'homologous-series', 'molecular-formula']),
 ('s05', 'Members of a homologous series show a trend in physical properties', 279,
  [P+'288_1088'], ['4.19'],
  ['boiling-point', 'intermolecular-forces', 'homologous-series']),
 ('s06', 'Members of a homologous series have similar chemical properties', 279,
  [P+'288_1089'], ['4.20'],
  ['saturated-hydrocarbon', 'alkane', 'functional-group']),
 ('s07', 'Two reactions of the alkanes', 279,
  [P+'288_1087', P+'288_1090', P+'289_1091', P+'289_1092', P+'289_1093'], ['4.22'],
  ['complete-combustion', 'incomplete-combustion', 'carbon-monoxide', 'substitution-reaction',
   'halogenoalkane', 'ultraviolet-radiation']),
 ('s08', 'Chapter 24 questions', 281,
  [P+'290_1094'], JOIN,
  ['alkane', 'general-formula', 'isomer', 'substitution-reaction', 'saturated-hydrocarbon']),
]

# ---- invariants BEFORE writing ----
rawmap = json.load(open(RAW))
raw_refs = [r for s in rawmap['sections'] for r in s['chunkRefs']]
authored_refs = [r for s in SECTIONS for r in s[3]]
assert len(rawmap['sections']) == 5, len(rawmap['sections'])
assert set(raw_refs) <= set(authored_refs), 'raw not subset of authored'
census = set()
for line in open(PARSE, encoding='utf-8'):
    c = json.loads(line)
    if c.get('unit_no') == 4 and c.get('chapter_no') == 24:
        census.add(c['id'])
assert len(census) == 16, len(census)
assert set(authored_refs) == census, 'authored != census'
assert len(authored_refs) == len(set(authored_refs)) == 16, 'single-home violated'

# raw re-homing spot-asserts (receipt-disclosed)
def home(cid):
    return next(s[0] for s in SECTIONS if cid in s[3])
assert home(P+'287_1083') == 's03', 'homologous-series exam HINT -> s03 (raw s01)'
assert home(P+'288_1087') == 's07', 'equations HINT -> s07 (raw s04)'
assert home(P+'288_1088') == 's05', 'trend-body bulk chunk home s05 (raw s04; hint head taught s07, chem-properties tail taught s06 — c23 1064/1075 split precedent)'
assert home(P+'288_1089') == 's06', 'not-inert KEY POINT -> s06 (raw s04)'
assert home(P+'288_1090') == 's07', 'combustion body -> s07 (raw s05)'
assert home(P+'290_1094') == 's08', 'questions bank chunkRef home s08 (c11-c23 precedent)'

pages = [s[2] for s in SECTIONS]
assert pages == sorted(pages), pages
assert pages[0] == 277 and pages[-1] == 281, pages

# join_set coverage: every spine point anchored by >=1 authored section
anchored = {c for s in SECTIONS for c in s[4]}
assert set(codes) <= anchored, f'spine points uncovered: {set(codes) - anchored}'

# ---- write lesson.yaml (refined) ----
lesson = {
    'lesson_id': 'u4-c24-alkanes',
    'chapter_key': 'u4:c24',
    'course_id': 'chemistry-4ch1',
    'title': 'Alkanes',
    'chem_only': False,
    'stage': 'S0',
    'book_page_range': [277, 281],
    'sections': [
        {'id': f'u4:c24:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'glossary': list(glo), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
    'features': {k: False for k in [
        'prior_knowledge', 'cross_curricular', 'misconceptions',
        'ms_vocab', 'glossary_chips', 'quick_checks', 'summary', 'can_you']},
    'receipts': [],
    'notes': ('S0 refined spine pinned by pin_c24_map.py (T-BOOK-057 r0): raw 5 -> authored '
              '8 sections, 16/16 census chunks single-home, raw superset; join_set DERIVED at '
              'S0-L0 from the printed objectives list SPLIT across chunks 1080 (typed '
              'learning_objectives, 2 doubled bullets) + 1081 (2 further bullets glued to the '
              'saturated key_point) x spine igcse-chemistry-T4:SUBc = 4.19-4.22 ALL CORE 4+0 '
              '(third consecutive ALL-CORE pack after c22 6+0 and c23 12+0); 4.21 chunk drops '
              'the spine comma, 4.22 chunk truncates the spine tail (spine-canonical pins, '
              'f-0016 class); printed section order on p278 differs from chunk reading order '
              '(1084 heading prints after the 1086 definition) — authored order mirrors the '
              'PRINTED book (isomers s02, homologous series s03, general formula s04); 1088 is '
              'a triple-glued chunk (combustion HINT head + Fig 24.4 trend body + '
              'chemical-properties tail): chunkRef home s05 by bulk, hint head taught s07, '
              'chem-properties tail taught s06 (c23 1064/1075 split precedent); questions close '
              'split out of raw s05 as authored s08 (c11-c23 precedent); FOUR absent display '
              'equations (two complete + two incomplete combustion, lost by the parse as '
              'image-rendered text) restored byte-precise from the PDF of record via 300-dpi '
              'crop OCR + atom-balance verification (f-0026 recipe); pages [277,281] authored '
              'range (raw pre-derived [277,279]; questions close starts p281)'),
}
lp = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/'
                  'international-gcse/chemistry-4ch1/lessons/u4-c24-alkanes/lesson.yaml')
lp.write_text(yaml.safe_dump(lesson, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- pin course.yaml row ----
cp = COURSE / 'course.yaml'
cfg = yaml.safe_load(cp.read_text(encoding='utf-8'))
hit = False
for rows in cfg['spine'].values():
    for r in rows:
        if r['key'] == 'u4:c24':
            r['join_set'] = JOIN
            r['learning_objective'] = learning_objective
            r['section_count'] = 8
            r['pages'] = [277, 281]
            hit = True
assert hit, 'u4:c24 row not found'
cp.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- regenerate committed section map to the REFINED authored set (c23 precedent:
#      S0.3b asserts the committed map carries the refined section set) ----
refined_map = {
    'chapter_key': 'u4:c24',
    'key_mapping': rawmap['key_mapping'],
    'book_page_range': [277, 281],
    'sections': [
        {'id': f'u4:c24:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
}
sm_path = COURSE / 'section-maps/u4-c24.json'
sm_path.write_text(json.dumps(refined_map, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('pin_c24_map: OK — lesson.yaml refined (8 sections / 16 chunks single-home), '
      'course row pinned (join_set 4.19-4.22 ALL CORE 4+0, section_count 8, pages [277,281]), '
      'section-maps/u4-c24.json regenerated to the refined authored set')
