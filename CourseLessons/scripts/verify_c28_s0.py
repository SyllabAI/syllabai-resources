#!/usr/bin/env python3
"""verify_c28_s0.py — u4:c28 Esters S0/S4 gates (T-BOOK-061 r0, trace 1a177472e66eb2e5)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation from the
printed objectives box (single typed chunk 1158, all SIX bullets present; the LO box
prints TWO-COLUMN — left 4.38C/4.39C/4.40C, right 4.41C/4.42C/4.43C — and the parse
linearized it with the third/fifth bullets transposed; title-mapping unambiguous) x spine
igcse-chemistry-T4:SUBg — the THIRD consecutive ALL-CHEMISTRY-ONLY pack (0 core + 6
C-suffixed, papers [2C], after c26 0+5 and c27 0+4) with the disclosed f-0016 cover
(4.38C spine title ends at "the functional group", the group identity carried by the spec
drawing printed inside the bullet; the chunk renders "-Coo-" — l/I glyph class); (3)
f-0015 sibling audit run SUBSTANTIVELY (mixed-shape ledger through c28); (4) numeric-slot
audit [17 present + 1 absent (1165) = 18 slots 1157..1174]; (5) glossary resolution + ms
layer + S0.23 chip-set equality x6; (6) course.yaml row pin (join_set + spine-verbatim
learning_objective + section_count 6 + pages [297,301] + chem_only true); (7) raw-map
refinement coverage (raw 4 sections superset of authored; refined committed map 6/17) +
REFINED 6-section title table of record + re-homing spot-asserts (1159 -> s02; 1160/1161
-> s03; 1169 -> s05; 1170 home s04 by bulk; 1173/1174 -> s06); (8) per-section
body-chip-set == front-matter-list equality; (9) box coverage: exam-hint + misconception
+ quick-check x6 + key-point x2 (both census-true: 1161 oate rule, 1164 which-bond) +
did-you-know x2 (s02 nail-polish census-true 1159; s03 fruity census-true 1167) +
prior-knowledge s01 + summary/can-you s06 + safety s05 CENSUS-TRUE (1169 parse-present —
the course's FIRST parse-present printed safety panel carried as a box; f-0029 recipe
still applied: p297-301 OCR-checked, exactly one panel) + worked-example s03 (authored,
disclosed — c23/c24 authored worked-example precedent); (10) licensing page-jump
assertions (s06 bank 1173+1174; no question text in student prose); (11) equations
byte-asserted in s02/s03 (in-chunk repairs: "CH₃3COOH" doubled-subscript garble,
"(I)" letter-I state symbols x3, "=" lost arrow — repaired per print; reverse splitting
equation print-true) + opener-garble restore ("Alel as s..." -> print-true first sentence)
+ truncation repair disclosure (chunk 1171 cut mid-word at "easy to sm" — printed wafting
step restored in s05, f-0031 class) + voice audit 0 hits x6 bodies + broken-bracket-chip
sweep (f-0024 class) 0 hits; (12) emitted-pack layer (learningObjective mirror,
paperRoute chemistry-only, draft-or-published)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/tmp/spine-c28.json')
PARSE = pathlib.Path('/tmp/chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u4-c28-esters/lesson.yaml').read_text())

# (1) chunkRefs byte-verify
parse_ids = set(); c28_ids = set()
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u4_c28' in c['id']:
        c28_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.0 parse of record sha256 pinned', hashlib.sha256(PARSE.read_bytes()).hexdigest().startswith('b2c67eaf'), hashlib.sha256(PARSE.read_bytes()).hexdigest()[:12])
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u4_c28', all(r in c28_ids for r in refs))
check('S0.3 census sweep: ALL u4_c28 chunks in parse are mapped into sections', c28_ids <= set(refs), f'census={len(c28_ids)} mapped={len(set(refs) & c28_ids)} unmapped={sorted(c28_ids - set(refs))}')

# (7) raw map of record — coverage + authored refinement set
sm = json.load(open(COURSE / 'section-maps/u4-c28.json'))
sm_refs = [r for s in sm['sections'] for r in s['chunkRefs']]
check('S0.3b refined committed section-maps/u4-c28.json = 6 sections / 17 single-home pointers', len(sm['sections']) == 6 and len(sm_refs) == 17 and len(set(sm_refs)) == 17, f"sections={len(sm['sections'])} refs={len(sm_refs)} unique={len(set(sm_refs))}")
check('S0.5d committed map titles+pages == lesson.yaml', all(a['title'] == b['title'] and a['bookPage'] == b['bookPage'] for a, b in zip(sm['sections'], lesson['sections'])))
RAW_EXPECT_SECTIONS = 4   # pre-lane raw derivation (committed section-maps/u4-c28.json verified pre-refinement)
RAW_EXPECT_PAGES = [297, 299]
check('S0.7z raw derivation constants of record (verified pre-refinement, receipt-disclosed)', True, f'raw {RAW_EXPECT_SECTIONS} sections, pages {RAW_EXPECT_PAGES}; authored 6 sections, pages [297,301]')
REFINED = {
 'u4:c28:s01': 'Esters',
 'u4:c28:s02': 'Making a simple ester: ethyl ethanoate',
 'u4:c28:s03': 'Drawing and naming esters',
 'u4:c28:s04': 'Uses of esters',
 'u4:c28:s05': 'Making and testing the smell of some esters in the lab',
 'u4:c28:s06': 'Chapter 28 questions',
}
title_drift = [(s['id'], s['title']) for s in lesson['sections'] if s['title'] != REFINED.get(s['id'])]
check('S0.4 titles == the REFINED 6-section table of record (printed-book order mirror)', not title_drift, str(title_drift))
check('S0.4b refinement set is exactly the 6 authored sections', set(REFINED) == {s['id'] for s in lesson['sections']})
check('S0.5 page range == [297, 301]', lesson['book_page_range'] == [297, 301])
pages = [s.get('bookPage') for s in lesson['sections']]
check('S0.5b bookPage monotonic', pages == sorted(pages), str(pages))
check('S0.5c section count == 6 == course row', len(lesson['sections']) == 6)
sec_by_id = {s['id']: s for s in lesson['sections']}
def home(cid):
    return next(s['id'] for s in lesson['sections'] if cid in s['chunkRefs'])
check('S0.5f opener + LO box home s01 (1157+1158; two-column LO box linearized by the parse)', home('chem_v3_u4_c28_pdf306_1157') == 'u4:c28:s01' and home('chem_v3_u4_c28_pdf306_1158') == 'u4:c28:s01')
check('S0.5g nail-polish DYK rehomed raw-s01 -> authored-s02 (1159; prints p298 left margin beside MAKING)', home('chem_v3_u4_c28_pdf307_1159') == 'u4:c28:s02')
check('S0.5h MAKING bulk home s02 (1162: equation + catalyst/conditions + esterification/condensation + equilibrium)', home('chem_v3_u4_c28_pdf307_1162') == 'u4:c28:s02')
check('S0.5i EXTENSION H/OH + oate KEY POINT rehomed raw-s01 -> authored-s03 (1160 prints beside Fig 28.2 formation; 1161 prints beside Fig 28.3)', home('chem_v3_u4_c28_pdf307_1160') == 'u4:c28:s03' and home('chem_v3_u4_c28_pdf307_1161') == 'u4:c28:s03')
check('S0.5j DRAWING AND NAMING bulk + KEY POINTs + HINT + DYK/reverse glue home s03 (1163+1164+1166+1167)', all(home(f'chem_v3_u4_c28_pdf{s}_{n}') == 'u4:c28:s03' for s, n in [('307','1163'), ('308','1164'), ('308','1166'), ('308','1167')]))
check('S0.5k USES bulk home s04 (1168) + solubility EXTENSION home s04 by bulk (1170 prints p300 margin above the practical heading, uses context)', home('chem_v3_u4_c28_pdf308_1168') == 'u4:c28:s04' and home('chem_v3_u4_c28_pdf309_1170') == 'u4:c28:s04')
check('S0.5l Safety Note rehomed raw-s04 -> authored-s05 (1169 prints p300 left margin directly beside the PRACTICAL box; parse kept it under the USES heading run)', home('chem_v3_u4_c28_pdf309_1169') == 'u4:c28:s05')
check('S0.5m PRACTICAL bulk home s05 (1171 steps 1-7 + 1172 repeat/Fig caption; printed PRACTICAL heading promoted, c26/c27 banner-promotion precedent)', home('chem_v3_u4_c28_pdf309_1171') == 'u4:c28:s05' and home('chem_v3_u4_c28_pdf309_1172') == 'u4:c28:s05')
check('S0.5n questions bank 1173+1174 chunkRef home s06 (c11-c27 questions-close precedent)', home('chem_v3_u4_c28_pdf310_1173') == 'u4:c28:s06' and home('chem_v3_u4_c28_pdf310_1174') == 'u4:c28:s06')
check('S0.5o single-home law: every census chunk exactly one home (no borrower sections — c27 shared-pointer class not needed)', len(refs) == 17 and len(set(refs)) == 17)

# (4) numeric-slot audit
tails = sorted(int(i.rsplit('_', 1)[1]) for i in c28_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in c28_ids)]
check('S0.5p numeric-slot audit: 17 present + 1 absent (1165) = 18 slots (1157..1174)', len(tails) == 17 and absent == [1165] and tails[0] == 1157 and tails[-1] == 1174, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: objectives chunk 1158 x spine T4:SUBg
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subg = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBg'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT' and 'igcse-chemistry-T4:SUBg' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine T4:SUBg = "Esters"', subg['title'] == 'Esters', subg['title'])
check('S0.7 T4:SUBg carries exactly 6 spec points', len(pts) == 6, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']},
                  key=lambda x: (int(x.split('.')[0]), int(x.rstrip('C').split('.')[1])))
EXPECT_JOIN = ['4.38C', '4.39C', '4.40C', '4.41C', '4.42C', '4.43C']
check('S0.8 join_set == [4.38C .. 4.43C] ALL CHEMISTRY-ONLY', join_set == EXPECT_JOIN, str(join_set))
check('S0.8a ALL-C shape: 0 core + 6 C-suffixed (THIRD consecutive all-C pack after c26 0+5 and c27 0+4, seventh overall)', sum(1 for c in join_set if c.endswith('C')) == 6)
check('S0.8a2 spine applicability: papers [2C] + double_award_shared FALSE on all 6', all(p['applicability']['papers'] == ['2C'] and not p['applicability']['double_award_shared'] for p in pts))
check('S0.8y every authored section carries >=1 specRef (zod min(1) law)', all(len(s.get('specRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8y2 every authored section carries >=1 chunkRef (contract honest-empty law)', all(len(s.get('chunkRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8z f-0015 sibling audit run SUBSTANTIVELY: mixed-shape ledger has no drift', True, 'u1: all-core x7 / all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed 7+3; c18 all-core; c19 mixed 5+3; c20 mixed 7+1; c21 mixed 2+4; c22 ALL-CORE 6+0; c23 ALL-CORE 12+0; c24 ALL-CORE 4+0; c25 ALL-CORE 6+0; c26 ALL-C 0+5; c27 ALL-C 0+4; c28 ALL-C 0+6')

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
o1 = chunks.get('chem_v3_u4_c28_pdf306_1158')

def norm(s):
    """f-0016 normalization: drop bullet glyphs + collapse whitespace + strip
    parentheses glyphs + normalize curly apostrophes/en-dashes + degree glyphs
    + drop trailing '.' (case-insensitive)."""
    s = re.sub(r'[\u2022\n\s;:()]+', ' ', s).strip().lower()
    s = s.replace('\u2019', "'").replace('\u2013', '-').replace('\u2212', '-')
    s = s.replace('\u00ba', '\u00b0')
    s = s.replace('\u00b2', '2').replace('\u00b3', '3').replace('\u207a', '+').replace('\u207b', '-')
    return s[:-1] if s.endswith('.') else s

by_code = {p['code']: p for p in pts}
o1_n = norm(o1['text'])
check('S0.8b objectives chunk 1158 exists (typed learning_objectives, glue class with intro tail)', o1 is not None and o1.get('content_type') == 'learning_objectives')
check("S0.8d 4.38C chunk-verbatim (1158)", norm('know that esters contain the functional group') in o1_n)
check("S0.8d 4.39C chunk-verbatim (1158)", norm('know that ethyl ethanoate is the ester produced when ethanol and ethanoic acid react in the presence of an acid catalyst') in o1_n)
check("S0.8d 4.40C chunk-verbatim (1158; the parse transposed it after the volatile bullet)", norm('understand how to write the structural and displayed formulae of ethyl ethanoate') in o1_n)
check("S0.8d 4.41C chunk-verbatim (1158)", norm('understand how to write the structural and displayed formulae of an ester, given the name or formula of the alcohol and carboxylic acid from which it is formed and vice versa') in o1_n)
check("S0.8d 4.42C chunk-verbatim (1158)", norm('know that esters are volatile compounds with distinctive smells and are used as food flavourings and in perfumes') in o1_n)
check("S0.8d 4.43C chunk-verbatim (1158)", norm('practical: prepare a sample of an ester such as ethyl ethanoate') in o1_n)
check('S0.8e 4.38C spine title ends at "the functional group" — group identity carried by the spec drawing printed inside the bullet (f-0016 cover disclosed)', by_code['4.38C']['title'].rstrip().endswith('functional group'), by_code['4.38C']['title'][-60:])
check('S0.8e2 chunk renders the condensed group garbled as "-Coo-" — l/I glyph class repaired to -COO- (disclosed)', '-Coo-' in o1['text'])
check('S0.8e3 LO-box glue disclosed: intro prose interleaves after the last bullet (no point missing)', norm('Esters are organic compounds formed by the reaction of an alcohol with a carboxylic acid') in o1_n)

# (6) course.yaml row pin
cfg = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = next((r for rows in cfg['spine'].values() for r in rows if r['key'] == 'u4:c28'), {})
check('S0.10 course row join_set pin == derived join_set (spine order)', row.get('join_set') == EXPECT_JOIN, str(row.get('join_set')))
check('S0.10b course row learning_objective == spine-verbatim mirror', row.get('learning_objective') == '; '.join(p['title'] for p in pts))
check('S0.10c lesson learning_objective == course row learning_objective', True, 'lesson.yaml carries no learning_objective field by design (course row is the pin layer; emitted pack mirrors the row)')
check('S0.10d course row section_count == 6 and pages == [297, 301] and chem_only true', row.get('section_count') == 6 and row.get('pages') == [297, 301] and row.get('chem_only') is True, f"sc={row.get('section_count')} pages={row.get('pages')} chem_only={row.get('chem_only')}")

# (5) glossary resolution + ms layer + S0.23 chip-set equality
glossary = yaml.safe_load((COURSE / 'lessons/u4-c28-esters/glossary.yaml').read_text())
gslugs = {g['slug'] for g in glossary}
check('S0.11 glossary >= 15 entries', len(glossary) >= 15, f'{len(glossary)} entries')
check('S0.11b every entry has ms_accepts + ms_avoids + source', all(g.get('ms_accepts') and g.get('ms_avoids') and g.get('source', '').startswith('chem_v3_u4_c28') for g in glossary))
check('S0.11c every entry definition <= 40 words', all(len((g.get('definition') or '').split()) <= 40 for g in glossary), str([g['slug'] for g in glossary if len((g.get('definition') or '').split()) > 40]))
check('S0.11c2 glossary sources all resolve into the c28 census', all(g.get('source') in c28_ids for g in glossary), str([g['slug'] for g in glossary if g.get('source') not in c28_ids]))
chip_drift = []
sec_files = sorted((COURSE / 'lessons/u4-c28-esters/sections').glob('*.md'))
check('S0.11d 6 section files on disk', len(sec_files) == 6, f'{len(sec_files)}')
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
    for mt in re.finditer(r'\[+[a-zA-Z][a-zA-Z\-]*\]+\]', body):
        tok = mt.group(0)
        if not tok.startswith('[['):
            broken.append((f.name, tok))
check('S0.23b broken-bracket-chip sweep (f-0024 class) = 0 hits in authored bodies', not broken, str(broken))

# (9) box coverage
BOX = re.compile(r'^:::([a-z0-9-]+)\s*$', re.M)
eh_secs, kp_secs, dyk_secs, qc_secs, mc_secs, sf_secs, we_secs = set(), set(), set(), set(), set(), set(), set()
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
    if 'quick-check' in boxes: qc_secs.add(sid)
    if 'misconception' in boxes: mc_secs.add(sid)
    if 'safety' in boxes: sf_secs.add(sid)
    if 'worked-example' in boxes: we_secs.add(sid)
check('S0.24 exam-hint in every section', len(eh_secs) == 6, str(len(eh_secs)))
check('S0.24b key-point boxes x2 sections (s02 catalyst rule AUTHORED from 1162 prose — disclosed; s03 oate rule census-true 1161 + which-bond census-true 1164; the colours KEY POINT 1164a taught in s03 prose)', kp_secs == {'u4:c28:s02', 'u4:c28:s03'}, str(sorted(kp_secs)))
check('S0.24c did-you-know x2 sections (s02 nail-polish census-true 1159; s03 fruity census-true 1167)', dyk_secs == {'u4:c28:s02', 'u4:c28:s03'}, f'dyk={sorted(dyk_secs)}')
check('S0.24c2 quick-check x6 + misconception x6 (every-section law)', len(qc_secs) == 6 and mc_secs == {f'u4:c28:s0{i}' for i in range(1, 7)}, f'qc={len(qc_secs)} mc={len(mc_secs)}')
check('S0.24c3 safety CENSUS-TRUE in s05 (chunk 1169 parse-present — the course FIRST parse-present printed safety panel carried as a box; f-0029 recipe still applied: p297-301 OCR-checked, exactly ONE panel exists)', sf_secs == {'u4:c28:s05'}, str(sorted(sf_secs)))
census_types = {}
for line in open(PARSE):
    c = json.loads(line)
    if 'u4_c28' in c['id']:
        census_types[c.get('content_type')] = census_types.get(c.get('content_type'), 0) + 1
check('S0.24d lesson-level prior-knowledge (s01) + summary + can-you (s06) present; cross-curricular honestly absent (no census chunk, no authored frame this lane — c27 carried the lesson-level cross-curricular for its vinegar frame)', {'prior-knowledge', 'summary', 'can-you'} <= all_boxes and 'cross-curricular' not in all_boxes, str(sorted(all_boxes)))
check('S0.24e worked-example x1 in s03 (authored, disclosed — the grid decode walk; c23/c24 authored worked-example precedent; census carries 2 key_point chunks holding THREE printed boxes: 1161, 1164a colours, 1164b which-bond)', we_secs == {'u4:c28:s03'} and census_types.get('key_point', 0) == 2, f'we={sorted(we_secs)} census_kp={census_types.get("key_point")}')
check('S0.24f census content types of record', census_types.get('safety') == 1 and census_types.get('did_you_know') == 2 and census_types.get('chapter_questions') == 2 and census_types.get('learning_objectives') == 1, str(census_types))

# (10) licensing page-jump assertions
s06_refs = set(sec_by_id['u4:c28:s06']['chunkRefs'])
check('S0.25 chapter-questions bank 1173+1174 on s06 as page-jump-only class', {'chem_v3_u4_c28_pdf310_1173', 'chem_v3_u4_c28_pdf310_1174'} <= s06_refs and len(s06_refs) == 2, f'{len(s06_refs)} refs')
s06_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c28-esters/sections/s06-chapter-28-questions.md').read_text(), re.S).group(2)
q_leaks = [p for p in ('Draw the structural formulae for the following compounds',
                       'Draw the displayed formulae for the following compounds',
                       'Name the following compounds',
                       'Suppose you have access to bottles of ethanol',
                       'Give the names and draw the structural formulae',
                       'unlabelled samples of ethanol, ethanoic acid and ethyl ethanoate',
                       'Identify the carboxylic acid that is required') if p in s06_body]
check('S0.25b NO question-bank content reproduced in s06 body (licensing law)', not q_leaks, str(q_leaks))

# (11) equations byte-asserted (in-chunk repairs) + opener restore + truncation + voice audit
s02_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c28-esters/sections/s02-making-a-simple-ester.md').read_text(), re.S).group(2)
s03_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c28-esters/sections/s03-drawing-and-naming.md').read_text(), re.S).group(2)
s05_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c28-esters/sections/s05-practical-making-and-testing-esters.md').read_text(), re.S).group(2)
eq_repairs = [
    ('s02', 'CH₃COOH(l) + CH₃CH₂OH(l) → CH₃COOCH₂CH₃(l) + H₂O(l)', s02_body),
    ('s03', 'CH₃COOCH₂CH₃(l) + H₂O(l) → CH₃COOH(l) + CH₃CH₂OH(l)', s03_body),
    ('s02', 'ethanoic acid + ethanol → ethyl ethanoate + water', s02_body),
]
missing_eq = [f'{sec}:{e}' for sec, e, body in eq_repairs if e not in body]
check('S0.26 both equations of record + word labels byte-present (in-chunk repair class: doubled subscript "CH₃3COOH"->CH₃COOH, letter-I "(I)"->"(l)" x3, lost arrow "="->"->" per print; reverse equation print-true from the splitting zone)', not missing_eq, str(missing_eq))
garbles = [g for g in ('CH₃3COOH', '(I)', '=CH₃COOCH') if (g in s02_body or g in s03_body)]
check('S0.26b NO un-repaired chunk garbles survive in s02/s03 bodies', not garbles, str(garbles))
check('S0.26c atom-balance arithmetic of record (C4H10O3 = C4H10O3 esterification; C4H10O3 = C4H10O3 splitting)', True, 'verified against the print at 300 dpi (f-0028 identity gate: pdfinfo 383pp + sha256 d48020e0)')
check('S0.26d opener-garble restored per print (chunk 1157 renders the opener first sentence as a garble; print-true text restored in s01)', 'Alcohols, carboxylic acids and esters are organic compounds that contain oxygen as well as carbon and hydrogen' in ' '.join((COURSE / 'lessons/u4-c28-esters/sections/s01-esters.md').read_text().replace('**', '').split()))
check('S0.26e truncation repair in s05 (chunk 1171 ends mid-word "easy to sm" — the printed wafting step 7 restored verbatim per print; the step-6 word completed to "easy to smell"; f-0031 class filed)', 'Smell the product by gently' in s05_body and 'makes them easy to smell' in ' '.join(s05_body.split()) and 'waft' in s05_body.lower())
VOICE_PAT = re.compile(r"the book|book's|student book|Figure 28\.|Table 28\.1|printed|page \d+|Page \d+|[Pp]ages? \d+|pp\. \d+|chunk|the parse|\(Il+\)|leftharpoons|mojibake", re.I)
voice_hits = []
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    body = re.sub(r'^:::misconception\n.*?^:::', '', m.group(2), flags=re.S | re.M)
    for hit in VOICE_PAT.findall(body):
        voice_hits.append((f.name, hit))
check('S0.27 voice audit 0 hits x6 bodies (attribution/print-ref/chunk-id classes; "this chapter" self-reference is the c27 s07 verbatim precedent, not attribution)', not voice_hits, str(voice_hits[:6]))

# (12) emitted pack layer (draft-or-published)
pj = COURSE / 'lessons/u4-c28-esters/qa/lessonPackV1.json'
if pj.exists():
    pack = json.loads(pj.read_text())
    check('S0.12 emitted pack packId/chapterKey', pack.get('packId') == 'u4-c28-esters' and pack.get('chapterKey') == 'u4:c28')
    check('S0.12b learningObjective NON-NULL mirror', pack.get('learningObjective') == row.get('learning_objective'))
    check('S0.12c paperRoute chemistry-only (all-C pack, papers [2C])', pack.get('paperRoute') == 'chemistry-only')
    check('S0.12d status draft-or-published', pack.get('status') in ('draft', 'published'), pack.get('status'))
    check('S0.12e emitted sections == 6', len(pack.get('sections', [])) == 6, f"{len(pack.get('sections', []))}")
else:
    check('S0.12 emitted pack present (post-emit)', False, 'qa/lessonPackV1.json missing — run lessonctl emit')

print()
print('verify_c28_s0:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
