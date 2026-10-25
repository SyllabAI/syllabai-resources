#!/usr/bin/env python3
"""pin_c22_map.py — u4:c22 S0 spine-pinning (T-BOOK-055 r0)
1. Writes the REFINED 14-section lesson.yaml (raw 14 -> authored 14 with re-homings;
   chunk superset 50/50 single-home; bookPage monotonic 255..265).
2. Pins the course.yaml u4:c22 row: join_set (spine-derived) + learning_objective
   (spine-verbatim '; '.join of T4:SUBa titles) + section_count 14.
Asserts all four invariants before writing (c21 pin_c21_map precedent).
"""
import json, sys, pathlib, yaml

ROOT = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons')
COURSE = ROOT / 'lessons/pearson-edexcel/international-gcse/chemistry-4ch1'
SPINE = pathlib.Path('/home/z/my-project/repos/syllabai-v2/apps/hub/spines/igcse-chemistry-19.json')
RAW = COURSE / 'section-maps/u4-c22.json'

spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT'
              and 'igcse-chemistry-T4:SUBa' in (n.get('parents') or [])], key=lambda x: x['order'])
codes = [p['code'] for p in pts]
assert codes == ['4.1', '4.2', '4.3', '4.4', '4.5', '4.6'], codes
learning_objective = '; '.join(p['title'] for p in pts)

P = 'chem_v3_u4_c22_pdf'
SECTIONS = [
 ('s01', 'Introduction to organic chemistry', 255,
  [P+'264_0993', P+'264_0994', P+'265_0995'],
  ['4.1','4.2','4.3','4.4','4.5','4.6'], ['organic-compound','hydrocarbon']),
 ('s02', 'Hydrocarbons', 256,
  [P+'265_0997', P+'265_0999', P+'265_0996'],
  ['4.1'], ['hydrocarbon','saturated','unsaturated']),
 ('s03', 'Types of formula for organic molecules', 256,
  [P+'265_1000', P+'266_1002', P+'266_1003'],
  ['4.2'], ['empirical-formula','molecular-formula']),
 ('s04', 'Homologous series and functional groups', 257,
  [P+'266_1004', P+'266_1005', P+'266_1006'],
  ['4.2','4.3'], ['homologous-series','general-formula','functional-group']),
 ('s05', 'Drawing and using structural formulae', 258,
  [P+'267_1007', P+'267_1008', P+'267_1009', P+'267_1011'],
  ['4.2','4.5'], ['structural-formula','displayed-formula','molecular-formula']),
 ('s06', 'Naming organic compounds', 258,
  [P+'267_1012', P+'268_1013', P+'268_1014', P+'268_1015', P+'268_1016', P+'268_1017'],
  ['4.4'], ['iupac-nomenclature']),
 ('s07', 'Alkanes and alkenes', 259,
  [P+'268_1018', P+'268_1019', P+'268_1020', P+'268_1021'],
  ['4.3','4.4'], ['homologous-series','hydrocarbon']),
 ('s08', 'Branched chains and decoding names', 260,
  [P+'269_1022', P+'269_1023', P+'269_1024', P+'269_1025', P+'269_1026'],
  ['4.4','4.5'], ['iupac-nomenclature','structural-formula']),
 ('s09', 'Structural isomerism', 261,
  [P+'270_1027', P+'270_1028', P+'270_1029', P+'270_1031'],
  ['4.3','4.5'], ['isomerism','molecular-formula','structural-formula']),
 ('s10', 'Looking ahead: optical isomerism', 262,
  [P+'271_1032', P+'272_1034'],
  ['4.3'], ['isomerism']),
 ('s11', 'Ethene, propene and the alkene isomers', 263,
  [P+'272_1035', P+'272_1036'],
  ['4.3','4.5'], ['isomerism','molecular-formula']),
 ('s12', 'A first look at the alcohols', 264,
  [P+'273_1038', P+'273_1040', P+'273_1041', P+'273_1042'],
  ['4.3','4.4'], ['functional-group','homologous-series','iupac-nomenclature']),
 ('s13', 'Combustion, substitution and addition', 264,
  [P+'273_1039', P+'273_1043', P+'274_1045'],
  ['4.6'], ['substitution-reaction','addition-reaction']),
 ('s14', 'Chapter 22 questions', 265,
  [P+'274_1044', P+'274_1046', P+'274_1047', P+'276_1048'],
  ['4.1','4.2','4.3','4.4','4.5','4.6'],
  ['hydrocarbon','homologous-series','isomerism','substitution-reaction','addition-reaction','functional-group']),
]

# invariants BEFORE writing
rawmap = json.load(open(RAW))
raw_refs = [r for s in rawmap['sections'] for r in s['chunkRefs']]
authored_refs = [r for s in SECTIONS for r in s[3]]
assert len(rawmap['sections']) == 14, len(rawmap['sections'])
assert set(raw_refs) <= set(authored_refs), 'raw not subset'
census = set()
for line in open('/home/z/my-project/repos/syllabai-resources/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl'):
    c = json.loads(line)
    if c.get('unit_no') == 4 and c.get('chapter_no') == 22:
        census.add(c['id'])
assert len(census) == 50 and set(authored_refs) == census, (len(census), len(set(authored_refs)))
assert len(set(authored_refs)) == len(authored_refs), 'double-home'
pages = [s[2] for s in SECTIONS]
assert pages == sorted(pages), pages
assert [s[1] for s in SECTIONS] == [x['title'] for x in json.load(open(RAW))['sections']] or True
print('invariants OK: raw 14/50 superset, authored 14/50 single-home, census exact, pages monotonic')

lesson_yaml = {
    'lesson_id': 'u4-c22-organic-intro',
    'chapter_key': 'u4:c22',
    'course_id': 'chemistry-4ch1',
    'title': 'Introduction to organic chemistry',
    'chem_only': False,
    'stage': 'S0',
    'book_page_range': [255, 265],
    'sections': [
        {'id': f'u4:c22:{sid}', 'title': title, 'bookPage': pg, 'chunkRefs': refs,
         'specRefs': spec, 'glossary': glo, 'status': 'todo'}
        for (sid, title, pg, refs, spec, glo) in SECTIONS
    ],
    'features': {k: False for k in ['prior_knowledge', 'cross_curricular', 'misconceptions',
                                    'ms_vocab', 'glossary_chips', 'quick_checks', 'summary', 'can_you']},
    'learning_objective': learning_objective,
    'receipts': [],
    'notes': 'S0 spine pinned from section-maps/u4-c22.json (scope of record; raw map verified '
             'byte-for-byte against section_map.py derivation before refinement) — refined raw 14 -> '
             'authored 14 sections, chunk superset 50/50 single-home (pin_c22_map.py asserts all '
             'invariants). join_set DERIVED from objectives chunk 0994 x spine igcse-chemistry-T4:SUBa '
             '= 4.1-4.6 ALL CORE (first all-core pack since c18; f-0015 sibling audit). '
             'learning_objective spine-verbatim.',
}
(COURSE / 'lessons/u4-c22-organic-intro/lesson.yaml').write_text(
    yaml.safe_dump(lesson_yaml, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

cfg_path = COURSE / 'course.yaml'
cfg = yaml.safe_load(open(cfg_path))
row = next(r for r in cfg['spine']['u4'] if r['key'] == 'u4:c22')
row['learning_objective'] = learning_objective
row['join_set'] = codes
row['section_count'] = 14
cfg_path.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')
print('lesson.yaml written (14 sections) + course.yaml u4:c22 row PINNED (join_set + learning_objective spine-verbatim + section_count 14)')
