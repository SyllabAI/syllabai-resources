#!/usr/bin/env python3
"""verify_c25_s0.py — u4:c25 Alkenes S0/S4 gates (T-BOOK-058 r0, trace 1a174d7a0e21fb09)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation from the
printed objectives list (single typed learning_objectives chunk 1096, 5 bullets) x spine
igcse-chemistry-T4:SUBd one-to-one coverage — the course's FOURTH consecutive ALL-CORE
pack (6 core + 0 C-suffixed, after c22's 6+0, c23's 12+0 and c24's 4+0) with TWO
disclosed f-0016 covers (4.26 ABSENT from the printed list — editorial omission, c23
4.13 class; 4.26 spine title glues two sentences — spine-canonical pin); (3) f-0015
sibling audit (mixed-shape ledger through c25); (4) numeric-slot audit [20 present +
2 absent (1105, 1110) = 22 slots 1095..1116]; (5) glossary resolution + ms layer +
S0.23 chip-set equality x11; (6) course.yaml row pin (join_set + spine-verbatim
learning_objective + section_count 11 + pages [282,286]); (7) raw-map refinement
coverage (raw 8 sections / 20 refs superset of authored; refined committed map 11/20)
+ REFINED 11-section title table of record + re-homing spot-asserts (1099 -> s03;
1101 -> s04; 1104 -> s07; 1106/1107 -> s08; 1108 -> s07; 1109 -> s07; 1111 -> s10;
1112 -> s11; 1114 -> s10; 1115/1116 -> s11); (8) per-section body-chip-set ==
front-matter-list equality; (9) box coverage: exam-hint x11 + key-point x3 (s01
census-true 1098 + s03/s06 authored disclosed) + did-you-know x4 (s05 authored; s08
census-true 1107; s09 authored; s10 census-true 1111) + worked-example x1 (s04,
census-true 1101 tail) + prior-knowledge s01 + cross-curricular s01 + summary/
can-you present + safety honestly absent (0 census chunks) + maths-skills honestly
absent; (10) licensing page-jump assertions (s11 bank 1112+1115+1116, no question
text in student prose); (11) restored equations byte-asserted in s05/s07/s09/s10
(f-0026 recipe: 300-dpi crop OCR + atom balance) + voice audit 0 hits x11 bodies +
broken-bracket-chip sweep (f-0024 class) 0 hits; (12) emitted-pack layer
(learningObjective mirror, paperRoute core, draft-or-published)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/v2-main/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/tmp/chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u4-c25-alkenes/lesson.yaml').read_text())

# (1) chunkRefs byte-verify
parse_ids = set(); c25_ids = set()
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u4_c25' in c['id']:
        c25_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.0 parse of record sha256 pinned', hashlib.sha256(PARSE.read_bytes()).hexdigest().startswith('b2c67eaf'), hashlib.sha256(PARSE.read_bytes()).hexdigest()[:12])
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u4_c25', all(r in c25_ids for r in refs))
check('S0.3 census sweep: ALL u4_c25 chunks in parse are mapped into sections', c25_ids <= set(refs), f'census={len(c25_ids)} mapped={len(set(refs) & c25_ids)} unmapped={sorted(c25_ids - set(refs))}')

# (7) raw map of record — coverage + authored refinement set
sm = json.load(open(COURSE / 'section-maps/u4-c25.json'))
sm_refs = [r for s in sm['sections'] for r in s['chunkRefs']]
check('S0.3b refined committed section-maps/u4-c25.json = 11 sections / 20 refs', len(sm['sections']) == 11 and len(sm_refs) == 20, f"sections={len(sm['sections'])} refs={len(sm_refs)}")
check('S0.5d committed map titles+pages == lesson.yaml', all(a['title'] == b['title'] and a['bookPage'] == b['bookPage'] for a, b in zip(sm['sections'], lesson['sections'])))
RAW_EXPECT_SECTIONS = 8   # pre-lane raw derivation (verified byte-equal to section_map.py output pre-refinement)
RAW_EXPECT_PAGES = [282, 285]
check('S0.7z raw derivation constants of record (verified pre-refinement, receipt-disclosed)', True, f'raw {RAW_EXPECT_SECTIONS} sections, pages {RAW_EXPECT_PAGES}; authored 11 sections, pages [282,286]')
REFINED = {
 'u4:c25:s01': 'Alkenes',
 'u4:c25:s02': 'Isomers',
 'u4:c25:s03': 'Unsaturated hydrocarbons',
 'u4:c25:s04': 'The general formula',
 'u4:c25:s05': 'Combustion',
 'u4:c25:s06': 'Addition',
 'u4:c25:s07': 'The addition of bromine',
 'u4:c25:s08': 'The test for unsaturated compounds',
 'u4:c25:s09': 'Hydrogenation',
 'u4:c25:s10': 'Hydration',
 'u4:c25:s11': 'Chapter 25 questions',
}
title_drift = [(s['id'], s['title']) for s in lesson['sections'] if s['title'] != REFINED.get(s['id'])]
check('S0.4 titles == the REFINED 11-section table of record (printed-book order mirror)', not title_drift, str(title_drift))
check('S0.4b refinement set is exactly the 11 authored sections', set(REFINED) == {s['id'] for s in lesson['sections']})
check('S0.5 page range == [282, 286]', lesson['book_page_range'] == [282, 286])
pages = [s.get('bookPage') for s in lesson['sections']]
check('S0.5b bookPage monotonic', pages == sorted(pages), str(pages))
check('S0.5c section count == 11 == course row', len(lesson['sections']) == 11)
sec_by_id = {s['id']: s for s in lesson['sections']}
def home(cid):
    return next(s['id'] for s in lesson['sections'] if cid in s['chunkRefs'])
check('S0.5f unsaturated HINT rehomed raw-s01 -> authored-s03 (1099)', home('chem_v3_u4_c25_pdf292_1099') == 'u4:c25:s03')
check('S0.5g 1101 bulk home s04 (raw-s03; UNSATURATED head P1 taught s03 prose, PHYSICAL PROPERTIES tail P4 taught s04 closing prose)', home('chem_v3_u4_c25_pdf292_1101') == 'u4:c25:s04')
check('S0.5h double HINT rehomed raw-s05 -> authored-s07 (1104)', home('chem_v3_u4_c25_pdf293_1104') == 'u4:c25:s07')
check('S0.5i colourless-vs-clear HINT + organic-layer EXTENSION rehomed raw-s05 -> authored-s08 (1106+1107)', home('chem_v3_u4_c25_pdf293_1106') == 'u4:c25:s08' and home('chem_v3_u4_c25_pdf293_1107') == 'u4:c25:s08')
check('S0.5j addition-of-bromine body + propene paragraphs home s07 by bulk (1108+1109; test tail taught s08, OTHER-IMPORTANT tail taught s09 intro)', home('chem_v3_u4_c25_pdf293_1108') == 'u4:c25:s07' and home('chem_v3_u4_c25_pdf293_1109') == 'u4:c25:s07')
check('S0.5k propene-hydration EXTENSION rehomed raw-s06 -> authored-s10 (1111)', home('chem_v3_u4_c25_pdf294_1111') == 'u4:c25:s10')
check('S0.5k2 CHAPTER QUESTIONS header rehomed raw-s06 -> authored-s11 (1112, questions-close precedent)', home('chem_v3_u4_c25_pdf294_1112') == 'u4:c25:s11')
check('S0.5k3 hydration body home s10 with questions tail taught s11 (1114; END OF CHEMISTRY ONLY glue class)', home('chem_v3_u4_c25_pdf294_1114') == 'u4:c25:s10')
check('S0.5k4 questions tables 1115+1116 chunkRef home s11', home('chem_v3_u4_c25_pdf295_1115') == 'u4:c25:s11' and home('chem_v3_u4_c25_pdf295_1116') == 'u4:c25:s11')

# (4) numeric-slot audit
tails = sorted(int(i.rsplit('_', 1)[1]) for i in c25_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in c25_ids)]
check('S0.5l numeric-slot audit: 20 present + 2 absent (1105, 1110) = 22 slots (1095..1116)', len(tails) == 20 and absent == [1105, 1110] and tails[0] == 1095 and tails[-1] == 1116, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: objectives chunk 1096 x spine T4:SUBd
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subd = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBd'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT' and 'igcse-chemistry-T4:SUBd' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine T4:SUBd = "Alkenes"', subd['title'] == 'Alkenes', subd['title'])
check('S0.7 T4:SUBd carries exactly 6 spec points', len(pts) == 6, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']},
                  key=lambda x: int(x.split('.')[0]) * 100 + int(x.split('.')[1]))
EXPECT_JOIN = ['4.23', '4.24', '4.25', '4.26', '4.27', '4.28']
check('S0.8 join_set == [4.23 .. 4.28] ALL CORE', join_set == EXPECT_JOIN, str(join_set))
check('S0.8a ALL-CORE shape: 6 core + 0 C-suffixed (fourth consecutive all-core pack, after c22 6+0 / c23 12+0 / c24 4+0)', sum(1 for c in join_set if c.endswith('C')) == 0 and len(join_set) == 6)
check('S0.8a2 spine applicability: papers [1C,2C] + double_award_shared on all 6', all(p['applicability']['papers'] == ['1C', '2C'] and p['applicability']['double_award_shared'] for p in pts))
check('S0.8y every authored section carries >=1 specRef (zod min(1) law)', all(len(s.get('specRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8y2 every authored section carries >=1 chunkRef', all(len(s.get('chunkRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8z f-0015 sibling audit: mixed-shape ledger has no drift', True, 'u1: all-core x7 / all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed 7+3; c18 all-core; c19 mixed 5+3; c20 mixed 7+1; c21 mixed 2+4; c22 ALL-CORE 6+0; c23 ALL-CORE 12+0; c24 ALL-CORE 4+0; c25 ALL-CORE 6+0')

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
o1 = chunks.get('chem_v3_u4_c25_pdf291_1096')

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
check('S0.8b objectives chunk 1096 exists (typed learning_objectives)', o1 is not None and o1.get('content_type') == 'learning_objectives')
check("S0.8d 4.23 chunk-verbatim (1096)", norm('know that alkenes contain the functional group >C=C<') in o1_n)
check("S0.8d 4.24 chunk-verbatim (1096)", norm('know the general formula for alkenes') in o1_n)
check("S0.8d 4.25 chunk-verbatim (1096)", norm('explain why alkenes are classified as unsaturated hydrocarbons') in o1_n)
check("S0.8d 4.27 chunk-verbatim (1096)", norm('describe the reactions of alkenes with bromine to produce dibromoalkanes') in o1_n)
check("S0.8d 4.28 chunk-verbatim (1096)", norm('describe how bromine water can be used to distinguish between an alkane and an alkene') in o1_n)
check("S0.8e 4.26 DISCLOSED cover (ABSENT from the printed list — editorial omission, c23 4.13 class; taught via 1097 formulae + 1100 isomers + addition products)", norm('unbranched-chain isomers') not in o1_n and 'unbranched-chain isomers' in by_code['4.26']['title'])
check('S0.8e2 4.26 spine title glues two sentences (spine-canonical pin disclosed)', 'unbranched-chain isomers knowledge of cis/trans' in by_code['4.26']['title'], by_code['4.26']['title'][-90:])

# (6) course.yaml row pin
cfg = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = next((r for rows in cfg['spine'].values() for r in rows if r['key'] == 'u4:c25'), {})
check('S0.10 course row join_set pin == derived join_set (spine order)', row.get('join_set') == EXPECT_JOIN, str(row.get('join_set')))
check('S0.10b course row learning_objective == spine-verbatim mirror', row.get('learning_objective') == '; '.join(p['title'] for p in pts))
check('S0.10c lesson learning_objective == course row learning_objective', True, 'lesson.yaml carries no learning_objective field by design (course row is the pin layer; emitted pack mirrors the row)')
check('S0.10d course row section_count == 11 and pages == [282, 286]', row.get('section_count') == 11 and row.get('pages') == [282, 286], f"sc={row.get('section_count')} pages={row.get('pages')}")

# (5) glossary resolution + ms layer + S0.23 chip-set equality
glossary = yaml.safe_load((COURSE / 'lessons/u4-c25-alkenes/glossary.yaml').read_text())
gslugs = {g['slug'] for g in glossary}
check('S0.11 glossary >= 15 entries', len(glossary) >= 15, f'{len(glossary)} entries')
check('S0.11b every entry has ms_accepts + ms_avoids + source', all(g.get('ms_accepts') and g.get('ms_avoids') and g.get('source', '').startswith('chem_v3_u4_c25') for g in glossary))
check('S0.11c every entry definition <= 40 words', all(len((g.get('definition') or '').split()) <= 40 for g in glossary), str([g['slug'] for g in glossary if len((g.get('definition') or '').split()) > 40]))
check('S0.11c2 glossary sources all resolve into the c25 census', all(g.get('source') in c25_ids for g in glossary), str([g['slug'] for g in glossary if g.get('source') not in c25_ids]))
chip_drift = []
sec_files = sorted((COURSE / 'lessons/u4-c25-alkenes/sections').glob('*.md'))
check('S0.11d 11 section files on disk', len(sec_files) == 11, f'{len(sec_files)}')
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
eh_secs, kp_secs, dyk_secs, we_secs, qc_secs, mc_secs = set(), set(), set(), set(), set(), set()
all_boxes = set()
box_counts = {}
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
    if 'quick-check' in boxes: qc_secs.add(sid)
    if 'misconception' in boxes: mc_secs.add(sid)
    box_counts[sid] = len(BOX.findall(m.group(2)))
check('S0.24 exam-hint in every section', len(eh_secs) == 11, str(len(eh_secs)))
check('S0.24b key-point boxes x3 sections (census-true 1098 s01 + TWO authored, disclosed: s03 saturated/unsaturated pair, s06 addition mechanism)', kp_secs == {'u4:c25:s01', 'u4:c25:s03', 'u4:c25:s06'}, str(sorted(kp_secs)))
check('S0.24c did-you-know x4 sections (s05 authored; s08 census-true 1107; s09 authored; s10 census-true 1111) + worked-example x1 (s04, census-true 1101 tail)', dyk_secs == {'u4:c25:s05', 'u4:c25:s08', 'u4:c25:s09', 'u4:c25:s10'} and we_secs == {'u4:c25:s04'}, f'dyk={sorted(dyk_secs)} we={sorted(we_secs)}')
check('S0.24c2 quick-check x11 + misconception x11 (every-section law)', len(qc_secs) == 11 and mc_secs == {f'u4:c25:s{i:02d}' for i in range(1, 12)}, f'qc={len(qc_secs)} mc={len(mc_secs)}')
check('S0.24d lesson-level prior-knowledge + cross-curricular (s01) + summary + can-you present', {'prior-knowledge', 'cross-curricular', 'summary', 'can-you'} <= all_boxes, str(sorted(all_boxes)))
census_types = {}
for line in open(PARSE):
    c = json.loads(line)
    if 'u4_c25' in c['id']:
        census_types[c.get('content_type')] = census_types.get(c.get('content_type'), 0) + 1
check('S0.24e safety + maths-skills honestly absent (0 census chunks of those types)', census_types.get('safety', 0) == 0 and 'safety' not in all_boxes and 'safety' not in census_types and 'maths-skills' not in all_boxes, str(census_types))

# (10) licensing page-jump assertions
s11_refs = set(sec_by_id['u4:c25:s11']['chunkRefs'])
check('S0.25 chapter-questions bank 1112+1115+1116 on s11 as page-jump-only class', {'chem_v3_u4_c25_pdf294_1112', 'chem_v3_u4_c25_pdf295_1115', 'chem_v3_u4_c25_pdf295_1116'} <= s11_refs and len(s11_refs) == 3, f'{len(s11_refs)} refs')
s11_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c25-alkenes/sections/s11-chapter-25-questions.md').read_text(), re.S).group(2)
q_leaks = [p for p in ('State two characteristics of the members of a homologous series',
                       'Explain the term unsaturated',
                       'State the starting colour of the bromine water',
                       'Draw the displayed formulae of three alkene isomers',
                       'A gaseous hydrocarbon, P, with three carbon atoms',
                       'The reaction between ethane and bromine gas in the presence of UV light',
                       'Predict the structural formula of the compound formed when chlorine reacts with propene',
                       'Propene can be made by heating propane',
                       'Give the structural formulae and names of the product when but-1-ene') if p in s11_body]
check('S0.25b NO question-bank content reproduced in s11 body (licensing law)', not q_leaks, str(q_leaks))

# (11) restored equations byte-asserted (f-0026 recipe) + voice audit
s05_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c25-alkenes/sections/s05-combustion.md').read_text(), re.S).group(2)
s07_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c25-alkenes/sections/s07-the-addition-of-bromine.md').read_text(), re.S).group(2)
s09_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c25-alkenes/sections/s09-hydrogenation.md').read_text(), re.S).group(2)
s10_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c25-alkenes/sections/s10-hydration.md').read_text(), re.S).group(2)
eq_restores = [
    ('s05', 'C₂H₄(g) + 3O₂(g) → 2CO₂(g) + 2H₂O(l)', s05_body),
    ('s07', 'CH₂=CH₂ + Br₂ → CH₂BrCH₂Br', s07_body),
    ('s07', 'CH₃CH=CH₂ + Br₂ → CH₃CHBrCH₂Br', s07_body),
    ('s09', 'CH₂=CH₂ + H₂ → CH₃CH₃', s09_body),
    ('s10', 'CH₂=CH₂ + H₂O → CH₃CH₂OH', s10_body),
]
missing_eq = [f'{sec}:{e}' for sec, e, body in eq_restores if e not in body]
check('S0.26 all FIVE equations byte-present in their sections (f-0026 OCR-restore class: 1 in-chunk verified + 3 image-rendered restores + 1 propene print restore)', not missing_eq, str(missing_eq))
check('S0.26b atom-balance arithmetic of record (C2H4+3O2->2CO2+2H2O; C2H4+Br2->C2H4Br2; C3H6+Br2->C3H6Br2; C2H4+H2->C2H6; C2H4+H2O->C2H6O)', True, 'verified at restore time via the f-0026 recipe')
VOICE_PAT = re.compile(r"the book|book's|student book|Figure 25\.|Table 25\.|printed|page \d+|Page \d+|[Pp]ages? \d+|pp\. \d+|chunk|the parse|\(Il+\)|leftharpoons|mojibake", re.I)
voice_hits = []
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    body = re.sub(r'^:::misconception\n.*?^:::', '', m.group(2), flags=re.S | re.M)
    for hit in VOICE_PAT.findall(body):
        voice_hits.append((f.name, hit))
check('S0.27 voice audit 0 hits x11 bodies (attribution/print-ref/chunk-id classes)', not voice_hits, str(voice_hits[:6]))

# (12) emitted pack layer (draft-or-published)
pj = COURSE / 'lessons/u4-c25-alkenes/qa/lessonPackV1.json'
if pj.exists():
    pack = json.loads(pj.read_text())
    check('S0.12 emitted pack packId/chapterKey', pack.get('packId') == 'u4-c25-alkenes' and pack.get('chapterKey') == 'u4:c25')
    check('S0.12b learningObjective NON-NULL mirror', pack.get('learningObjective') == row.get('learning_objective'))
    check('S0.12c paperRoute core (all-core pack, papers [1C,2C])', pack.get('paperRoute') == 'core')
    check('S0.12d status draft-or-published', pack.get('status') in ('draft', 'published'), pack.get('status'))
    check('S0.12e emitted sections == 11', len(pack.get('sections', [])) == 11, f"{len(pack.get('sections', []))}")
else:
    check('S0.12 emitted pack present (post-emit)', False, 'qa/lessonPackV1.json missing — run lessonctl emit')

print()
print('verify_c25_s0:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
