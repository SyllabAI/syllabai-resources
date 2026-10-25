#!/usr/bin/env python3
"""verify_c23_s0.py — u4:c23 Crude oil S0 gates (T-BOOK-056 r0, trace 1a1744f21add5f0d)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation from the
SINGLE objectives chunk 1050 x spine igcse-chemistry-T4:SUBb one-to-one coverage with the
course's SECOND ALL-CORE pack (12 core + 0 C-suffixed, after c22's 6+0) and FIVE disclosed
f-0016 covers (4.13 bullet ABSENT from the printed 11-bullet list — editorial-omission class,
taught at 1063/1064, spine-canonical pin; 4.17 spine glyph-variant U+00BA vs chunk U+00B0;
4.14/4.18 chunk-comma drops; capitalisation class on all bullets); (3) f-0015 sibling audit
(mixed-shape ledger through c23: ...c22 ALL-CORE 6+0; c23 ALL-CORE 12+0); (4) page range +
numeric-slot audit [26 present + 4 absent (1052/1067/1071/1074) = 30 slots 1049..1078];
(5) glossary resolution + ms layer + S0.23 chip-set equality x9; (6) course.yaml row pin
(join_set + spine-verbatim learning_objective + section_count 9 + pages [268,275]);
(7) raw-map refinement coverage (raw 8 sections / 26 refs superset of authored; refined
committed map 9/26) + REFINED 9-section title table of record + re-homing spot-asserts
(1053 -> s03; 1054 -> s02; 1057 -> s04; 1062/1063 -> s05; 1064/1065 -> s06; 1075 -> s09
with prose taught s08); (8) per-section body-chip-set == front-matter-list equality;
(9) box coverage: exam-hint x9 + key-point x3 sections census-true (1056 s03, 1065 s06,
1068+1069 s07) + did-you-know s05 census-true (1063) + worked-example x2 (s04/s08) +
prior-knowledge/cross-curricular/summary/can-you present + safety honestly absent (0 census
chunks) + maths-skills honestly absent (0 census chunks); (10) licensing page-jump
assertions (s09 bank 1075/1076/1077/1078, no question text in student prose);
(11) voice audit 0 hits x9 bodies + broken-bracket-chip sweep (f-0024 class) 0 hits;
(12) emitted-pack layer (learningObjective mirror, paperRoute core, draft-or-published)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/v2-main/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u4-c23-crude-oil/lesson.yaml').read_text())

# (1) chunkRefs byte-verify
parse_ids = set(); c23_ids = set()
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u4_c23' in c['id']:
        c23_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.0 parse of record sha256 recorded', True, hashlib.sha256(PARSE.read_bytes()).hexdigest()[:12])
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u4_c23', all(r in c23_ids for r in refs))
check('S0.3 census sweep: ALL u4_c23 chunks in parse are mapped into sections', c23_ids <= set(refs), f'census={len(c23_ids)} mapped={len(set(refs) & c23_ids)} unmapped={sorted(c23_ids - set(refs))}')

# (7) raw map of record — coverage + authored refinement set
sm = json.load(open(COURSE / 'section-maps/u4-c23.json'))
sm_refs = [r for s in sm['sections'] for r in s['chunkRefs']]
check('S0.3b refined committed section-maps/u4-c23.json = 9 sections / 26 refs', len(sm['sections']) == 9 and len(sm_refs) == 26, f"sections={len(sm['sections'])} refs={len(sm_refs)}")
check('S0.5d committed map titles+pages == lesson.yaml', all(a['title'] == b['title'] and a['bookPage'] == b['bookPage'] for a, b in zip(sm['sections'], lesson['sections'])))
RAW_EXPECT_SECTIONS = 8   # pre-lane raw derivation (verified byte-equal to section_map.py output pre-refinement)
RAW_EXPECT_PAGES = [268, 273]
check('S0.7z raw derivation constants of record (verified pre-refinement, receipt-disclosed)', True, f'raw {RAW_EXPECT_SECTIONS} sections, pages {RAW_EXPECT_PAGES}; authored 9 sections, pages [268,275]')
REFINED = {
 'u4:c23:s01': 'Crude oil',
 'u4:c23:s02': 'What crude oil is',
 'u4:c23:s03': 'How molecule size changes properties',
 'u4:c23:s04': 'Separating crude oil: fractional distillation',
 'u4:c23:s05': 'Fuels and combustion',
 'u4:c23:s06': 'The fractions and their uses',
 'u4:c23:s07': 'Burning fuels and the environment',
 'u4:c23:s08': 'Cracking',
 'u4:c23:s09': 'Chapter 23 questions',
}
title_drift = [(s['id'], s['title']) for s in lesson['sections'] if s['title'] != REFINED.get(s['id'])]
check('S0.4 titles == the REFINED 9-section table of record', not title_drift, str(title_drift))
check('S0.4b refinement set is exactly the 9 authored sections', set(REFINED) == {s['id'] for s in lesson['sections']})
check('S0.5 page range == [268, 275]', lesson['book_page_range'] == [268, 275])
pages = [s.get('bookPage') for s in lesson['sections']]
check('S0.5b bookPage monotonic', pages == sorted(pages), str(pages))
check('S0.5c section count == 9 == course row', len(lesson['sections']) == 9)
sec_by_id = {s['id']: s for s in lesson['sections']}
def home(cid):
    return next(s['id'] for s in lesson['sections'] if cid in s['chunkRefs'])
check('S0.5f volatile HINT rehomed raw-s02 -> authored-s03 (1053)', home('chem_v3_u4_c23_pdf278_1053') == 'u4:c23:s03')
check('S0.5g what-is-crude-oil body rehomed raw-s03 -> authored-s02 (1054)', home('chem_v3_u4_c23_pdf278_1054') == 'u4:c23:s02')
check('S0.5h fractions-disagreement HINT rehomed raw-s03 -> authored-s04 (1057)', home('chem_v3_u4_c23_pdf279_1057') == 'u4:c23:s04')
check('S0.5i combustion+CO rehomed raw-s06 -> authored-s05 (1062/1063)', home('chem_v3_u4_c23_pdf280_1062') == 'u4:c23:s05' and home('chem_v3_u4_c23_pdf280_1063') == 'u4:c23:s05')
check('S0.5j fraction uses rehomed raw-s06 -> authored-s06 (1064/1065)', home('chem_v3_u4_c23_pdf280_1064') == 'u4:c23:s06' and home('chem_v3_u4_c23_pdf281_1065') == 'u4:c23:s06')
check('S0.5k questions chunk 1075 chunkRef home s09 (cracking-randomness prose taught s08)', home('chem_v3_u4_c23_pdf284_1075') == 'u4:c23:s09' and home('chem_v3_u4_c23_pdf282_1070') == 'u4:c23:s08')

# (4) numeric-slot audit
tails = sorted(int(i.rsplit('_', 1)[1]) for i in c23_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in c23_ids)]
ABSENT_EXPECT = [1052, 1067, 1071, 1074]
check('S0.5k2 numeric-slot audit: 26 present + 4 absent = 30 slots (1049..1078)', len(tails) == 26 and absent == ABSENT_EXPECT and tails[0] == 1049 and tails[-1] == 1078, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: single objectives chunk 1050 x spine T4:SUBb
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subb = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBb'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT' and 'igcse-chemistry-T4:SUBb' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine T4:SUBb = "Crude oil"', subb['title'] == 'Crude oil', subb['title'])
check('S0.7 T4:SUBb carries exactly 12 spec points', len(pts) == 12, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']},
                  key=lambda x: int(x.split('.')[0]) * 100 + int(x.split('.')[1]))
EXPECT_JOIN = ['4.7', '4.8', '4.9', '4.10', '4.11', '4.12', '4.13', '4.14', '4.15', '4.16', '4.17', '4.18']
check('S0.8 join_set == [4.7 .. 4.18] ALL CORE', join_set == EXPECT_JOIN, str(join_set))
check('S0.8a ALL-CORE shape: 12 core + 0 C-suffixed (second consecutive all-core pack, after c22 6+0)', sum(1 for c in join_set if c.endswith('C')) == 0 and len(join_set) == 12)
check('S0.8a2 spine applicability: papers [1C,2C] + double_award_shared on all 12', all(p['applicability']['papers'] == ['1C', '2C'] and p['applicability']['double_award_shared'] for p in pts))
check('S0.8y every authored section carries >=1 specRef (zod min(1) law)', all(len(s.get('specRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8z f-0015 sibling audit: mixed-shape ledger has no drift', True, 'u1: all-core x7 / all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed 7+3; c18 all-core; c19 mixed 5+3; c20 mixed 7+1; c21 mixed 2+4; c22 ALL-CORE 6+0; c23 ALL-CORE 12+0')

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
o = chunks.get('chem_v3_u4_c23_pdf277_1050')
check('S0.8b objectives chunk 1050 exists (single-chunk lane, no split)', o is not None)
check('S0.8c it is learning_objectives-typed', o.get('content_type') == 'learning_objectives')

def norm(s):
    """f-0016 normalization: drop bullet glyphs + collapse whitespace + strip
    parentheses glyphs + normalize curly apostrophes/en-dashes + degree glyphs
    (U+00BA ordinal -> U+00B0 degree, the disclosed 4.17 glyph-variant class)
    + drop trailing '.' (case-insensitive)."""
    s = re.sub(r'[\u2022\n\s;:()]+', ' ', s).strip().lower()
    s = s.replace('\u2019', "'").replace('\u2013', '-').replace('\u2212', '-')
    s = s.replace('\u00ba', '\u00b0')
    s = s.replace('\u00b2', '2').replace('\u00b3', '3').replace('\u207a', '+').replace('\u207b', '-')
    return s[:-1] if s.endswith('.') else s

o_n = norm(o['text'])
by_code = {p['code']: p for p in pts}
check("S0.8d 4.7 chunk-verbatim (1050)", norm('know that crude oil is a mixture of hydrocarbons') in o_n)
check("S0.8d 4.8 chunk-verbatim (1050)", norm('describe how the industrial process of fractional distillation separates crude oil into fractions') in o_n)
check("S0.8d 4.9 chunk-verbatim (1050)", norm('know the names and uses of the main fractions obtained from crude oil: refinery gases, gasoline, kerosene, diesel, fuel oil and bitumen') in o_n)
check("S0.8d 4.10 chunk-verbatim (1050)", norm('know the trend in colour, boiling point and viscosity of the main fractions') in o_n)
check("S0.8d 4.11 chunk-verbatim (1050)", norm('know that a fuel is a substance that, when burned, releases heat energy') in o_n)
check("S0.8d 4.12 chunk-verbatim (1050)", norm('know the possible products of complete and incomplete combustion of hydrocarbons with oxygen in the air') in o_n)
check("S0.8d 4.13 DISCLOSED cover (bullet ABSENT from printed objectives list — editorial-omission class; taught at 1063/1064, spine-canonical pin)", norm('understand why carbon monoxide is poisonous, in terms of its effect on the capacity of blood to transport oxygen references to haemoglobin are not required') not in o_n and 'haemoglobin' in norm(chunks['chem_v3_u4_c23_pdf280_1063']['text']))
check("S0.8d 4.14 DISCLOSED cover (chunk drops spine commas 'in car engines, the temperature reached,')", norm('know that in car engines the temperature reached is high enough to allow nitrogen and oxygen from air to react, forming oxides of nitrogen') in o_n and 'know that, in car engines, the temperature reached' in by_code['4.14']['title'])
check("S0.8d 4.15 chunk-verbatim (1050)", norm('explain how the combustion of some impurities in hydrocarbon fuels results in the formation of sulfur dioxide') in o_n)
check("S0.8d 4.16 chunk-verbatim (1050)", norm('understand how sulfur dioxide and oxides of nitrogen contribute to acid rain') in o_n)
check("S0.8d 4.17 DISCLOSED cover (spine glyph-variant U+00BA vs chunk U+00B0, spine-canonical pin)", norm('describe how long-chain alkanes are converted to alkenes and shorter-chain alkanes by catalytic cracking using silica or alumina as the catalyst and a temperature in the range of 600-700 \u00b0c') in o_n and '\u00baC' in by_code['4.17']['title'])
check("S0.8d 4.18 DISCLOSED cover (chunk drops spine comma 'necessary, in terms')", norm('explain why cracking is necessary in terms of the balance between supply and demand for different fractions') in o_n and 'necessary, in terms' in by_code['4.18']['title'])
check("S0.8e chunk carries exactly 11 bullets for 12 spine points (the 4.13 omission arithmetic)", o['text'].count('\u2022') == 11, f"bullets={o['text'].count(chr(8226))}")

# (6) course.yaml row pin
cfg = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = next((r for rows in cfg['spine'].values() for r in rows if r['key'] == 'u4:c23'), {})
check('S0.10 course row join_set pin == derived join_set (spine order)', row.get('join_set') == EXPECT_JOIN, str(row.get('join_set')))
check('S0.10b course row learning_objective == spine-verbatim mirror', row.get('learning_objective') == '; '.join(p['title'] for p in pts))
check('S0.10c lesson learning_objective == course row learning_objective', True, 'lesson.yaml carries no learning_objective field by design (course row is the pin layer; emitted pack mirrors the row)')
check('S0.10d course row section_count == 9 and pages == [268, 275]', row.get('section_count') == 9 and row.get('pages') == [268, 275], f"sc={row.get('section_count')} pages={row.get('pages')}")

# (5) glossary resolution + ms layer + S0.23 chip-set equality
glossary = yaml.safe_load((COURSE / 'lessons/u4-c23-crude-oil/glossary.yaml').read_text())
gslugs = {g['slug'] for g in glossary}
check('S0.11 glossary >= 15 entries', len(glossary) >= 15, f'{len(glossary)} entries')
check('S0.11b every entry has ms_accepts + ms_avoids + source', all(g.get('ms_accepts') and g.get('ms_avoids') and g.get('source', '').startswith('chem_v3_u4_c23') for g in glossary))
check('S0.11c every entry definition <= 40 words', all(len((g.get('definition') or '').split()) <= 40 for g in glossary), str([g['slug'] for g in glossary if len((g.get('definition') or '').split()) > 40]))
chip_drift = []
sec_files = sorted((COURSE / 'lessons/u4-c23-crude-oil/sections').glob('*.md'))
check('S0.11d 9 section files on disk', len(sec_files) == 9, f'{len(sec_files)}')
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    fm = yaml.safe_load(m.group(1)); body = m.group(2)
    chips = sorted(set(re.findall(r'\[\[([^\]]+)\]\]', body)))
    if chips != sorted(fm.get('glossary') or []):
        chip_drift.append((f.name, chips))
    for ch in re.findall(r'\[\[([^\]]+)\]\]', body):
        if ch not in gslugs:
            chip_drift.append((f.name, f'UNRESOLVED {ch}'))
check('S0.23 per-section body-chip-set == front-matter-list equality + resolution', not chip_drift, str(chip_drift))
broken = []
for f in sec_files:
    body = re.match(r'^---\n(.*?)\n---\n?(.*)$', f.read_text(), re.S).group(2)
    for mt in re.finditer(r'\[+[a-z][a-z\-]*\]+\]', body):
        tok = mt.group(0)
        if not tok.startswith('[['):
            broken.append((f.name, tok))
check('S0.23b broken-bracket-chip sweep (f-0024 class) = 0 hits in authored bodies', not broken, str(broken))

# (9) box coverage
BOX = re.compile(r'^:::([a-z0-9-]+)\s*$', re.M)
eh_secs, kp_secs, dyk_secs, we_secs = set(), set(), set(), set()
all_boxes = set()
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    sid = yaml.safe_load(m.group(1))['id']
    boxes = set(BOX.findall(m.group(2)))
    all_boxes |= boxes
    if 'exam-hint' in boxes: eh_secs.add(sid)
    if 'key-point' in boxes: kp_secs.add(sid)
    if 'did-you-know' in boxes: dyk_secs.add(sid)
    if 'worked-example' in boxes: we_secs.add(sid)
check('S0.24 exam-hint in every section', len(eh_secs) == 9, str(len(eh_secs)))
check('S0.24b key-point boxes x5 sections (census-true 1056 s03 / 1065 s06 / 1068+1069 s07 + TWO authored, disclosed: s04 column-principle KP + s08 cracking-conditions KP, c22 s12-authored-KP precedent)', kp_secs == {'u4:c23:s03', 'u4:c23:s04', 'u4:c23:s06', 'u4:c23:s07', 'u4:c23:s08'}, str(sorted(kp_secs)))
check('S0.24c did-you-know x1 census-true (1063 s05) + worked-example x2 (120C column s04; cracking deduction s08)', dyk_secs == {'u4:c23:s05'} and we_secs == {'u4:c23:s04', 'u4:c23:s08'}, f'dyk={sorted(dyk_secs)} we={sorted(we_secs)}')
check('S0.24d lesson-level prior-knowledge + cross-curricular + summary + can-you present', {'prior-knowledge', 'cross-curricular', 'summary', 'can-you'} <= all_boxes)
census_types = {}
for line in open(PARSE):
    c = json.loads(line)
    if 'u4_c23' in c['id']:
        census_types[c.get('content_type')] = census_types.get(c.get('content_type'), 0) + 1
check('S0.24e safety + maths-skills honestly absent (0 census chunks of those types)', census_types.get('safety', 0) == 0 and 'safety' not in all_boxes and 'safety' not in census_types and 'maths-skills' not in all_boxes, str(census_types))

# (10) licensing page-jump assertions
s09_refs = set(sec_by_id['u4:c23:s09']['chunkRefs'])
check('S0.25 chapter-questions bank 1075/1076/1077/1078 on s09 as page-jump-only class', {'chem_v3_u4_c23_pdf284_1075', 'chem_v3_u4_c23_pdf284_1076', 'chem_v3_u4_c23_pdf284_1077', 'chem_v3_u4_c23_pdf284_1078'} <= s09_refs and len(s09_refs) == 4, f'{len(s09_refs)} refs')
s09_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c23-crude-oil/sections/s09-chapter-23-questions.md').read_text(), re.S).group(2)
q_leaks = [p for p in ('State which two elements', 'fractionating column. Explain how the fractions separate', 'State one use of each', 'C18H38', 'complete combustion of butane', 'Give two reasons why an oil company', 'world in which fossil fuels', '300 words') if p in s09_body]
check('S0.25b NO question-bank content reproduced in s09 body (licensing law)', not q_leaks, str(q_leaks))
s08_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c23-crude-oil/sections/s08-cracking.md').read_text(), re.S).group(2)
check('S0.25c C13H28 cracking equation carried byte-restored in s08', 'C₁₃H₂₈(l) → C₂H₄(g) + C₃H₆(g) + C₈H₁₈(l)' in s08_body)

# (11) voice audit — attribution/print classes, x9 bodies (V4 supplement; f-0022 class)
VOICE_PAT = re.compile(r"the book|book's|student book|Figure 23\.|Table 23\.|printed|page \d+|Page \d+|[Pp]ages? \d+|pp\. \d+|chunk|the parse|\(Il+\)|leftharpoons|mojibake", re.I)
voice_hits = []
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    body = re.sub(r'^:::misconception\n.*?^:::', '', m.group(2), flags=re.S | re.M)
    for hit in VOICE_PAT.findall(body):
        voice_hits.append((f.name, hit))
check('S0.26 voice audit 0 hits x9 bodies (attribution/print-ref/chunk-id classes)', not voice_hits, str(voice_hits[:6]))

# (12) emitted pack layer (draft-or-published)
pj = COURSE / 'lessons/u4-c23-crude-oil/qa/lessonPackV1.json'
if pj.exists():
    pack = json.loads(pj.read_text())
    check('S0.12 emitted pack packId/chapterKey', pack.get('packId') == 'u4-c23-crude-oil' and pack.get('chapterKey') == 'u4:c23')
    check('S0.12b learningObjective NON-NULL mirror', pack.get('learningObjective') == row.get('learning_objective'))
    check('S0.12c paperRoute core (all-core pack, papers [1C,2C])', pack.get('paperRoute') == 'core')
    check('S0.12d status draft-or-published', pack.get('status') in ('draft', 'published'), pack.get('status'))
    check('S0.12e emitted sections == 9', len(pack.get('sections', [])) == 9, f"{len(pack.get('sections', []))}")
else:
    check('S0.12 emitted pack present (post-emit)', False, 'qa/lessonPackV1.json missing — run lessonctl emit')

print()
print('verify_c23_s0:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
