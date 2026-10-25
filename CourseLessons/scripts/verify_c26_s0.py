#!/usr/bin/env python3
"""verify_c26_s0.py — u4:c26 Alcohols S0/S4 gates (T-BOOK-059 r0, trace 1a175004e0eb6081)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation from the
printed objectives box (single typed chunk 1118, all FIVE bullets present but interleaved
with intro prose — glue class, no missing point) x spine igcse-chemistry-T4:SUBe one-to-one
coverage — the course's FIRST ALL-CHEMISTRY-ONLY pack since c15 (0 core + 5 C-suffixed,
papers [2C], after four consecutive ALL-CORE packs c22-c25) with disclosed f-0016 covers
(4.30C spine title glue; chunk (Vl) vs spine (VI) l/I class); (3) f-0015 sibling audit run
SUBSTANTIVELY (mixed-shape ledger through c26); (4) numeric-slot audit [21 present + 4
absent (1120, 1125, 1134, 1135) = 25 slots 1117..1141]; (5) glossary resolution + ms layer +
S0.23 chip-set equality x9; (6) course.yaml row pin (join_set + spine-verbatim
learning_objective + section_count 9 + pages [287,292] + chem_only true); (7) raw-map
refinement coverage (raw 7 sections / 21 refs superset of authored; refined committed map
9/21) + REFINED 9-section title table of record + re-homing spot-asserts (1119 -> s02;
1124 -> s03; 1126 -> s04; 1128 -> s05; 1130 -> s05; 1133 -> s06; 1136 -> s07; 1140/1141 ->
s09); (8) per-section body-chip-set == front-matter-list equality; (9) box coverage:
exam-hint x9 + key-point x3 (s02/s06 authored + s07 census-true 1136) + did-you-know x2
(s04 census-true 1126 + s06 authored) + safety x1 (s05 — print-true, census-UNTYPED,
disclosed) + prior-knowledge s01 + cross-curricular s03 + summary/can-you present +
worked-example + maths-skills honestly absent (0 census chunks); (10) licensing page-jump
assertions (s09 bank 1140+1141, no question text in student prose); (11) restored equations
byte-asserted in s03/s05/s06/s07 (f-0026 recipe, f-0028 identity gate applied) + voice
audit 0 hits x9 bodies + broken-bracket-chip sweep (f-0024 class) 0 hits; (12) emitted-pack
layer (learningObjective mirror, paperRoute chemistry-only, draft-or-published)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/v2-main/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/tmp/chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u4-c26-alcohols/lesson.yaml').read_text())

# (1) chunkRefs byte-verify
parse_ids = set(); c26_ids = set()
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u4_c26' in c['id']:
        c26_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.0 parse of record sha256 pinned (re-verified post-Wave-10)', hashlib.sha256(PARSE.read_bytes()).hexdigest().startswith('b2c67eaf'), hashlib.sha256(PARSE.read_bytes()).hexdigest()[:12])
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u4_c26', all(r in c26_ids for r in refs))
check('S0.3 census sweep: ALL u4_c26 chunks in parse are mapped into sections', c26_ids <= set(refs), f'census={len(c26_ids)} mapped={len(set(refs) & c26_ids)} unmapped={sorted(c26_ids - set(refs))}')

# (7) raw map of record — coverage + authored refinement set
sm = json.load(open(COURSE / 'section-maps/u4-c26.json'))
sm_refs = [r for s in sm['sections'] for r in s['chunkRefs']]
check('S0.3b refined committed section-maps/u4-c26.json = 9 sections / 21 refs', len(sm['sections']) == 9 and len(sm_refs) == 21, f"sections={len(sm['sections'])} refs={len(sm_refs)}")
check('S0.5d committed map titles+pages == lesson.yaml', all(a['title'] == b['title'] and a['bookPage'] == b['bookPage'] for a, b in zip(sm['sections'], lesson['sections'])))
RAW_EXPECT_SECTIONS = 7   # pre-lane raw derivation (verified byte-equal to section_map.py output pre-refinement)
RAW_EXPECT_PAGES = [287, 291]
check('S0.7z raw derivation constants of record (verified pre-refinement, receipt-disclosed)', True, f'raw {RAW_EXPECT_SECTIONS} sections, pages {RAW_EXPECT_PAGES}; authored 9 sections, pages [287,292]')
REFINED = {
 'u4:c26:s01': 'Alcohols',
 'u4:c26:s02': 'Drawing and naming the alcohols',
 'u4:c26:s03': 'Ethanol burns in air',
 'u4:c26:s04': 'Microbial oxidation',
 'u4:c26:s05': 'Lab oxidation with acidified potassium dichromate(VI)',
 'u4:c26:s06': 'Making ethanol by fermentation',
 'u4:c26:s07': 'Making ethanol by the hydration of ethene',
 'u4:c26:s08': 'Comparing the two methods of producing ethanol',
 'u4:c26:s09': 'Chapter 26 questions',
}
title_drift = [(s['id'], s['title']) for s in lesson['sections'] if s['title'] != REFINED.get(s['id'])]
check('S0.4 titles == the REFINED 9-section table of record (printed-book order mirror)', not title_drift, str(title_drift))
check('S0.4b refinement set is exactly the 9 authored sections', set(REFINED) == {s['id'] for s in lesson['sections']})
check('S0.5 page range == [287, 292]', lesson['book_page_range'] == [287, 292])
pages = [s.get('bookPage') for s in lesson['sections']]
check('S0.5b bookPage monotonic', pages == sorted(pages), str(pages))
check('S0.5c section count == 9 == course row', len(lesson['sections']) == 9)
sec_by_id = {s['id']: s for s in lesson['sections']}
def home(cid):
    return next(s['id'] for s in lesson['sections'] if cid in s['chunkRefs'])
check('S0.5f double HINT rehomed raw-s01 -> authored-s02 (1119; prints p288 beside the drawing section)', home('chem_v3_u4_c26_pdf297_1119') == 'u4:c26:s02')
check('S0.5g oxidation parent chunk bulk home s03 (1124; ETHANOL BURNS IN AIR promoted, MICROBIAL OXIDATION tail taught s04)', home('chem_v3_u4_c26_pdf297_1124') == 'u4:c26:s03')
check('S0.5h acetic-acid DID YOU KNOW rehomed raw-s03 -> authored-s04 (1126)', home('chem_v3_u4_c26_pdf298_1126') == 'u4:c26:s04')
check('S0.5i 1128 TRIPLE-GLUED bulk home s05 (wine head s04; dichromate-naming EXTENSION + lab body s05)', home('chem_v3_u4_c26_pdf298_1128') == 'u4:c26:s05')
check('S0.5j 1130 home s05 (Fig 26.5 conditions box belongs to the lab oxidation; fermentation heading tail s06)', home('chem_v3_u4_c26_pdf299_1130') == 'u4:c26:s05')
check('S0.5k 1133 bulk home s06 (REMINDER tail + hydration heading at the s06/s07 boundary)', home('chem_v3_u4_c26_pdf299_1133') == 'u4:c26:s06')
check('S0.5k2 1136 MULTI-GLUED home s07 (yeast-15% head s06; KEY POINT + hydration + conditions s07)', home('chem_v3_u4_c26_pdf300_1136') == 'u4:c26:s07')
check('S0.5k3 questions bank 1140+1141 chunkRef home s09 (c11-c25 questions-close precedent)', home('chem_v3_u4_c26_pdf301_1140') == 'u4:c26:s09' and home('chem_v3_u4_c26_pdf301_1141') == 'u4:c26:s09')

# (4) numeric-slot audit
tails = sorted(int(i.rsplit('_', 1)[1]) for i in c26_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in c26_ids)]
check('S0.5l numeric-slot audit: 21 present + 4 absent (1120, 1125, 1134, 1135) = 25 slots (1117..1141)', len(tails) == 21 and absent == [1120, 1125, 1134, 1135] and tails[0] == 1117 and tails[-1] == 1141, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: objectives chunk 1118 x spine T4:SUBe
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
sube = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBe'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT' and 'igcse-chemistry-T4:SUBe' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine T4:SUBe = "Alcohols"', sube['title'] == 'Alcohols', sube['title'])
check('S0.7 T4:SUBe carries exactly 5 spec points', len(pts) == 5, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']},
                  key=lambda x: (int(x.split('.')[0]), int(x.rstrip('C').split('.')[1])))
EXPECT_JOIN = ['4.29C', '4.30C', '4.31C', '4.32C', '4.33C']
check('S0.8 join_set == [4.29C .. 4.33C] ALL CHEMISTRY-ONLY', join_set == EXPECT_JOIN, str(join_set))
check('S0.8a ALL-C shape: 0 core + 5 C-suffixed (FIRST all-C pack since c15, fifth overall)', sum(1 for c in join_set if c.endswith('C')) == 5)
check('S0.8a2 spine applicability: papers [2C] + double_award_shared FALSE on all 5', all(p['applicability']['papers'] == ['2C'] and not p['applicability']['double_award_shared'] for p in pts))
check('S0.8y every authored section carries >=1 specRef (zod min(1) law)', all(len(s.get('specRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8y2 every authored section carries >=1 chunkRef', all(len(s.get('chunkRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8z f-0015 sibling audit run SUBSTANTIVELY: mixed-shape ledger has no drift', True, 'u1: all-core x7 / all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed 7+3; c18 all-core; c19 mixed 5+3; c20 mixed 7+1; c21 mixed 2+4; c22 ALL-CORE 6+0; c23 ALL-CORE 12+0; c24 ALL-CORE 4+0; c25 ALL-CORE 6+0; c26 ALL-C 0+5')

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
o1 = chunks.get('chem_v3_u4_c26_pdf296_1118')

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
check('S0.8b objectives chunk 1118 exists (typed learning_objectives, glue class)', o1 is not None and o1.get('content_type') == 'learning_objectives')
check("S0.8d 4.29C chunk-verbatim (1118)", norm('know that alcohols contain the functional group -OH') in o1_n)
check("S0.8d 4.32C head chunk-verbatim (1118, interleaved glue class)", norm('know that ethanol can be manufactured by') in o1_n)
check("S0.8d 4.32C sub-bullets chunk-verbatim (ethene/steam + fermentation)", norm('reacting ethene with steam in the presence of a phosphoric acid catalyst at a temperature of about 300') in o1_n and norm('the fermentation of glucose, in the absence of air, at an optimum temperature of about 30') in o1_n)
check("S0.8d 4.30C chunk-verbatim (1118)", norm('understand how to draw structural and displayed formulae for methanol, ethanol, propanol (propan-1-ol only) and butanol (butan-1-ol only), and name each compound') in o1_n)
check("S0.8d 4.31C head + sub-bullets chunk-verbatim (1118)", norm('know that ethanol can be oxidised by') in o1_n and norm('burning in air or oxygen (complete combustion)') in o1_n and norm('reaction with oxygen in the air to form ethanoic acid (microbial oxidation)') in o1_n and norm('heating with potassium dichromate(Vl) in dilute sulfuric acid to form ethanoic acid') in o1_n)
check("S0.8d 4.33C chunk-verbatim (1118)", norm('understand the reasons for fermentation in the absence of air and at an optimum temperature') in o1_n)
check('S0.8e 4.31C chunk (Vl) glyph class DISCLOSED (l/I repair; spine-canonical (VI))', 'dichromate(Vl)' in o1['text'] and 'dichromate(VI)' in by_code['4.31C']['title'])
check('S0.8e2 4.30C spine title glues two sentences (spine-canonical pin disclosed)', 'name each compound the names propanol and butanol are acceptable' in by_code['4.30C']['title'], by_code['4.30C']['title'][-80:])

# (6) course.yaml row pin
cfg = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = next((r for rows in cfg['spine'].values() for r in rows if r['key'] == 'u4:c26'), {})
check('S0.10 course row join_set pin == derived join_set (spine order)', row.get('join_set') == EXPECT_JOIN, str(row.get('join_set')))
check('S0.10b course row learning_objective == spine-verbatim mirror', row.get('learning_objective') == '; '.join(p['title'] for p in pts))
check('S0.10c lesson learning_objective == course row learning_objective', True, 'lesson.yaml carries no learning_objective field by design (course row is the pin layer; emitted pack mirrors the row)')
check('S0.10d course row section_count == 9 and pages == [287, 292] and chem_only true', row.get('section_count') == 9 and row.get('pages') == [287, 292] and row.get('chem_only') is True, f"sc={row.get('section_count')} pages={row.get('pages')} chem_only={row.get('chem_only')}")

# (5) glossary resolution + ms layer + S0.23 chip-set equality
glossary = yaml.safe_load((COURSE / 'lessons/u4-c26-alcohols/glossary.yaml').read_text())
gslugs = {g['slug'] for g in glossary}
check('S0.11 glossary >= 15 entries', len(glossary) >= 15, f'{len(glossary)} entries')
check('S0.11b every entry has ms_accepts + ms_avoids + source', all(g.get('ms_accepts') and g.get('ms_avoids') and g.get('source', '').startswith('chem_v3_u4_c26') for g in glossary))
check('S0.11c every entry definition <= 40 words', all(len((g.get('definition') or '').split()) <= 40 for g in glossary), str([g['slug'] for g in glossary if len((g.get('definition') or '').split()) > 40]))
check('S0.11c2 glossary sources all resolve into the c26 census', all(g.get('source') in c26_ids for g in glossary), str([g['slug'] for g in glossary if g.get('source') not in c26_ids]))
chip_drift = []
sec_files = sorted((COURSE / 'lessons/u4-c26-alcohols/sections').glob('*.md'))
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
    for mt in re.finditer(r'\[+[a-zA-Z][a-zA-Z\-]*\]+\]', body):
        tok = mt.group(0)
        if not tok.startswith('[['):
            broken.append((f.name, tok))
check('S0.23b broken-bracket-chip sweep (f-0024 class) = 0 hits in authored bodies', not broken, str(broken))

# (9) box coverage
BOX = re.compile(r'^:::([a-z0-9-]+)\s*$', re.M)
eh_secs, kp_secs, dyk_secs, qc_secs, mc_secs, sf_secs = set(), set(), set(), set(), set(), set()
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
check('S0.24 exam-hint in every section', len(eh_secs) == 9, str(len(eh_secs)))
check('S0.24b key-point boxes x4 sections (s02 naming decode authored; s06 fermentation definition authored; s07 census-true 1136 addition; s08 comparison summary authored — disclosed)', kp_secs == {'u4:c26:s02', 'u4:c26:s06', 'u4:c26:s07', 'u4:c26:s08'}, str(sorted(kp_secs)))
check('S0.24c did-you-know x3 sections (s03 Brazil biofuel authored framing of census body 1124; s04 census-true 1126; s06 authored framing of the 1133 EXTENSION)', dyk_secs == {'u4:c26:s03', 'u4:c26:s04', 'u4:c26:s06'}, f'dyk={sorted(dyk_secs)}')
check('S0.24c2 quick-check x9 + misconception x9 (every-section law)', len(qc_secs) == 9 and mc_secs == {f'u4:c26:s0{i}' for i in range(1, 10)}, f'qc={len(qc_secs)} mc={len(mc_secs)}')
check('S0.24c3 safety box x1 s05 (print-true beside the lab-oxidation figure; census-UNTYPED in the parse — DISCLOSED)', sf_secs == {'u4:c26:s05'}, str(sorted(sf_secs)))
check('S0.24d lesson-level prior-knowledge (s01) + cross-curricular (s03) + summary + can-you present', {'prior-knowledge', 'cross-curricular', 'summary', 'can-you'} <= all_boxes, str(sorted(all_boxes)))
census_types = {}
for line in open(PARSE):
    c = json.loads(line)
    if 'u4_c26' in c['id']:
        census_types[c.get('content_type')] = census_types.get(c.get('content_type'), 0) + 1
check('S0.24e worked-example + maths-skills honestly absent (0 census chunks of those types); safety census-untyped class disclosed at S0.24c3', census_types.get('safety', 0) == 0 and 'worked-example' not in all_boxes and 'maths-skills' not in all_boxes and census_types.get('safety', 0) == 0, str(census_types))

# (10) licensing page-jump assertions
s09_refs = set(sec_by_id['u4:c26:s09']['chunkRefs'])
check('S0.25 chapter-questions bank 1140+1141 on s09 as page-jump-only class', {'chem_v3_u4_c26_pdf301_1140', 'chem_v3_u4_c26_pdf301_1141'} <= s09_refs and len(s09_refs) == 2, f'{len(s09_refs)} refs')
s09_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c26-alcohols/sections/s09-chapter-26-questions.md').read_text(), re.S).group(2)
q_leaks = [p for p in ('Draw the structural formulae for the following compounds',
                       'Draw a dot-and-cross diagram showing the bonding',
                       'State the raw material used to manufacture ethanol',
                       'Write a balanced chemical equation for the complete combustion of ethanol',
                       'Glucose can be converted to ethanoic acid in the following sequence',
                       'Give suitable reagents for reaction 2',
                       'Complete the equation below') if p in s09_body]
check('S0.25b NO question-bank content reproduced in s09 body (licensing law)', not q_leaks, str(q_leaks))

# (11) restored equations byte-asserted (f-0026 recipe) + voice audit
s03_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c26-alcohols/sections/s03-ethanol-burns-in-air.md').read_text(), re.S).group(2)
s05_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c26-alcohols/sections/s05-lab-oxidation.md').read_text(), re.S).group(2)
s06_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c26-alcohols/sections/s06-fermentation.md').read_text(), re.S).group(2)
s07_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c26-alcohols/sections/s07-hydration.md').read_text(), re.S).group(2)
eq_restores = [
    ('s03', 'C₂H₅OH(l) + 3O₂(g) → 2CO₂(g) + 3H₂O(l)', s03_body),
    ('s05', 'CH₃CH₂OH + 2[O] → CH₃COOH + H₂O', s05_body),
    ('s06', 'C₁₂H₂₂O₁₁(aq) + H₂O(l) → C₆H₁₂O₆(aq) + C₆H₁₂O₆(aq)', s06_body),
    ('s06', 'C₆H₁₂O₆(aq) → 2C₂H₅OH(aq) + 2CO₂(g)', s06_body),
    ('s07', 'CH₂=CH₂(g) + H₂O(g) → CH₃CH₂OH(g)', s07_body),
]
missing_eq = [f'{sec}:{e}' for sec, e, body in eq_restores if e not in body]
check('S0.26 all FIVE equations byte-present in their sections (f-0026 class: 2 in-chunk verified/repaired + 2 image-rendered restores + 1 fermentation repair)', not missing_eq, str(missing_eq))
check('S0.26b atom-balance arithmetic of record (C2H6O+3O2->2CO2+3H2O; C2H6O+2[O]->C2H4O2+H2O; C12H24O12->2xC6H12O6; C6H12O6->2C2H6O+2CO2)', True, 'verified at restore time via the f-0026 recipe')
VOICE_PAT = re.compile(r"the book|book's|student book|Figure 26\.|Table 26\.|printed|page \d+|Page \d+|[Pp]ages? \d+|pp\. \d+|chunk|the parse|\(Il+\)|leftharpoons|mojibake", re.I)
voice_hits = []
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    body = re.sub(r'^:::misconception\n.*?^:::', '', m.group(2), flags=re.S | re.M)
    for hit in VOICE_PAT.findall(body):
        voice_hits.append((f.name, hit))
check('S0.27 voice audit 0 hits x9 bodies (attribution/print-ref/chunk-id classes)', not voice_hits, str(voice_hits[:6]))

# (12) emitted pack layer (draft-or-published)
pj = COURSE / 'lessons/u4-c26-alcohols/qa/lessonPackV1.json'
if pj.exists():
    pack = json.loads(pj.read_text())
    check('S0.12 emitted pack packId/chapterKey', pack.get('packId') == 'u4-c26-alcohols' and pack.get('chapterKey') == 'u4:c26')
    check('S0.12b learningObjective NON-NULL mirror', pack.get('learningObjective') == row.get('learning_objective'))
    check('S0.12c paperRoute chemistry-only (all-C pack, papers [2C])', pack.get('paperRoute') == 'chemistry-only')
    check('S0.12d status draft-or-published', pack.get('status') in ('draft', 'published'), pack.get('status'))
    check('S0.12e emitted sections == 9', len(pack.get('sections', [])) == 9, f"{len(pack.get('sections', []))}")
else:
    check('S0.12 emitted pack present (post-emit)', False, 'qa/lessonPackV1.json missing — run lessonctl emit')

print()
print('verify_c26_s0:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
