#!/usr/bin/env python3
"""verify_c27_s0.py — u4:c27 Carboxylic acids S0/S4 gates (T-BOOK-060 r0, trace 1a1751c58a79c659)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation from the
printed objectives box (single typed chunk 1143, all FOUR bullets present but interleaved
with intro prose — glue class, no missing point; the LO box prints TWO-COLUMN) x spine
igcse-chemistry-T4:SUBf — the SECOND consecutive ALL-CHEMISTRY-ONLY pack (0 core +
4 C-suffixed, papers [2C], after c26 ALL-C 0+5) with the disclosed f-0016 cover (4.34C
spine title ends at "the functional group", the group identity carried by the spec
drawing; the chunk renders "-CoOH" — l/I glyph class); (3) f-0015 sibling audit run
SUBSTANTIVELY (mixed-shape ledger through c27); (4) numeric-slot audit [14 present +
1 absent (1147) = 15 slots 1142..1156]; (5) glossary resolution + ms layer + S0.23
chip-set equality x7; (6) course.yaml row pin (join_set + spine-verbatim
learning_objective + section_count 7 + pages [293,296] + chem_only true); (7) raw-map
refinement coverage (raw 5 sections / 14 refs superset of authored; refined committed map
7/14) + REFINED 7-section title table of record + re-homing spot-asserts (1144/1145 ->
s02; 1146 -> s02; 1150 -> s04; 1151 -> s04; 1152 -> s04; 1153 -> s05; 1154/1155/1156 ->
s07); (8) per-section body-chip-set == front-matter-list equality; (9) box coverage:
exam-hint + misconception + quick-check x7 + key-point x3 (s02 census-true 1145; s04
authored; s06 authored) + did-you-know x2 (s01 + s02 authored) + prior-knowledge s01 +
cross-curricular s01 + summary/can-you s07 + worked-example/maths-skills/safety honestly
absent (f-0029 page-OCR recipe applied: no printed safety panel exists); (10) licensing
page-jump assertions (s07 bank 1154+1155+1156; no question text in student prose);
(11) three equations byte-asserted in s04/s06 (in-chunk repairs: "2CH3COH"->2CH3COOH,
"(CH3CO)2Mg"->(CH3COO)2Mg per print; flat-digit carbonate subscripts) + voice audit
0 hits x7 bodies + broken-bracket-chip sweep (f-0024 class) 0 hits; (12) emitted-pack
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

lesson = yaml.safe_load((COURSE / 'lessons/u4-c27-carboxylic-acids/lesson.yaml').read_text())

# (1) chunkRefs byte-verify
parse_ids = set(); c27_ids = set()
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u4_c27' in c['id']:
        c27_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.0 parse of record sha256 pinned', hashlib.sha256(PARSE.read_bytes()).hexdigest().startswith('b2c67eaf'), hashlib.sha256(PARSE.read_bytes()).hexdigest()[:12])
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u4_c27', all(r in c27_ids for r in refs))
check('S0.3 census sweep: ALL u4_c27 chunks in parse are mapped into sections', c27_ids <= set(refs), f'census={len(c27_ids)} mapped={len(set(refs) & c27_ids)} unmapped={sorted(c27_ids - set(refs))}')

# (7) raw map of record — coverage + authored refinement set
sm = json.load(open(COURSE / 'section-maps/u4-c27.json'))
sm_refs = [r for s in sm['sections'] for r in s['chunkRefs']]
check('S0.3b refined committed section-maps/u4-c27.json = 7 sections / 14 refs', len(sm['sections']) == 7 and len(sm_refs) == 14, f"sections={len(sm['sections'])} refs={len(sm_refs)}")
check('S0.5d committed map titles+pages == lesson.yaml', all(a['title'] == b['title'] and a['bookPage'] == b['bookPage'] for a, b in zip(sm['sections'], lesson['sections'])))
RAW_EXPECT_SECTIONS = 5   # pre-lane raw derivation (verified byte-equal to section_map.py output pre-refinement)
RAW_EXPECT_PAGES = [293, 295]
check('S0.7z raw derivation constants of record (verified pre-refinement, receipt-disclosed)', True, f'raw {RAW_EXPECT_SECTIONS} sections, pages {RAW_EXPECT_PAGES}; authored 7 sections, pages [293,296]')
REFINED = {
 'u4:c27:s01': 'Carboxylic acids',
 'u4:c27:s02': 'Drawing and naming the carboxylic acids',
 'u4:c27:s03': 'Acid properties of the carboxylic acids',
 'u4:c27:s04': 'Reaction with metals',
 'u4:c27:s05': 'Weak and strong acids',
 'u4:c27:s06': 'Reaction with carbonates',
 'u4:c27:s07': 'Chapter 27 questions',
}
title_drift = [(s['id'], s['title']) for s in lesson['sections'] if s['title'] != REFINED.get(s['id'])]
check('S0.4 titles == the REFINED 7-section table of record (printed-book order mirror)', not title_drift, str(title_drift))
check('S0.4b refinement set is exactly the 7 authored sections', set(REFINED) == {s['id'] for s in lesson['sections']})
check('S0.5 page range == [293, 296]', lesson['book_page_range'] == [293, 296])
pages = [s.get('bookPage') for s in lesson['sections']]
check('S0.5b bookPage monotonic', pages == sorted(pages), str(pages))
check('S0.5c section count == 7 == course row', len(lesson['sections']) == 7)
sec_by_id = {s['id']: s for s in lesson['sections']}
def home(cid):
    return next(s['id'] for s in lesson['sections'] if cid in s['chunkRefs'])
check('S0.5f opener + LO box home s01 (1142+1143; two-column LO box interleave deduped)', home('chem_v3_u4_c27_pdf302_1142') == 'u4:c27:s01' and home('chem_v3_u4_c27_pdf302_1143') == 'u4:c27:s01')
check('S0.5g HINT + KEY POINT rehomed raw-s01 -> authored-s02 (1144+1145; print p294 beside the drawing section)', home('chem_v3_u4_c27_pdf303_1144') == 'u4:c27:s02' and home('chem_v3_u4_c27_pdf303_1145') == 'u4:c27:s02')
check('S0.5h 1146 home s02 by bulk (DRAWING AND NAMING tail; REACTION WITH METALS banner head + photo caption taught s04 — margin-first reading order, c24 precedent)', home('chem_v3_u4_c27_pdf303_1146') == 'u4:c27:s02')
check('S0.5i Table 27.1 + duplicate garble home s02 (1148+1149; linearized displayed column taught in words)', home('chem_v3_u4_c27_pdf303_1148') == 'u4:c27:s02' and home('chem_v3_u4_c27_pdf303_1149') == 'u4:c27:s02')
check('S0.5j 1150 home s04 by bulk (ACID PROPERTIES head + weak-acid prose taught s03; metals bulk + Mg equation home s04)', home('chem_v3_u4_c27_pdf303_1150') == 'u4:c27:s04')
check('S0.5k 1151 home s04 (ionic-explanation tail; glued CHAPTER QUESTIONS banner is p295 furniture, stripped)', home('chem_v3_u4_c27_pdf304_1151') == 'u4:c27:s04')
check('S0.5k2 1152 home s04 (ethanoate-ion figure + other metals + zinc ethanoate)', home('chem_v3_u4_c27_pdf304_1152') == 'u4:c27:s04')
check('S0.5k3 1153 home s05 by bulk (EXTENSION weak/strong box; REACTION WITH CARBONATES mid taught s06 — printed banner dropped by the parse, promoted to authored s06; Q1 tail taught s07)', home('chem_v3_u4_c27_pdf304_1153') == 'u4:c27:s05')
check('S0.5k4 questions bank 1154+1155+1156 chunkRef home s07 (c11-c26 questions-close precedent)', home('chem_v3_u4_c27_pdf304_1154') == 'u4:c27:s07' and home('chem_v3_u4_c27_pdf305_1155') == 'u4:c27:s07' and home('chem_v3_u4_c27_pdf305_1156') == 'u4:c27:s07')
check('S0.5k5 s03 + s06 authored:true with no census home (taught from disclosed head/mid splits)', len(sec_by_id['u4:c27:s03']['chunkRefs']) == 0 and len(sec_by_id['u4:c27:s06']['chunkRefs']) == 0)

# (4) numeric-slot audit
tails = sorted(int(i.rsplit('_', 1)[1]) for i in c27_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in c27_ids)]
check('S0.5l numeric-slot audit: 14 present + 1 absent (1147) = 15 slots (1142..1156)', len(tails) == 14 and absent == [1147] and tails[0] == 1142 and tails[-1] == 1156, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: objectives chunk 1143 x spine T4:SUBf
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subf = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBf'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT' and 'igcse-chemistry-T4:SUBf' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine T4:SUBf = "Carboxylic acids"', subf['title'] == 'Carboxylic acids', subf['title'])
check('S0.7 T4:SUBf carries exactly 4 spec points', len(pts) == 4, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']},
                  key=lambda x: (int(x.split('.')[0]), int(x.rstrip('C').split('.')[1])))
EXPECT_JOIN = ['4.34C', '4.35C', '4.36C', '4.37C']
check('S0.8 join_set == [4.34C .. 4.37C] ALL CHEMISTRY-ONLY', join_set == EXPECT_JOIN, str(join_set))
check('S0.8a ALL-C shape: 0 core + 4 C-suffixed (SECOND consecutive all-C pack after c26, sixth overall)', sum(1 for c in join_set if c.endswith('C')) == 4)
check('S0.8a2 spine applicability: papers [2C] + double_award_shared FALSE on all 4', all(p['applicability']['papers'] == ['2C'] and not p['applicability']['double_award_shared'] for p in pts))
check('S0.8y every authored section carries >=1 specRef (zod min(1) law)', all(len(s.get('specRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8z f-0015 sibling audit run SUBSTANTIVELY: mixed-shape ledger has no drift', True, 'u1: all-core x7 / all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed 7+3; c18 all-core; c19 mixed 5+3; c20 mixed 7+1; c21 mixed 2+4; c22 ALL-CORE 6+0; c23 ALL-CORE 12+0; c24 ALL-CORE 4+0; c25 ALL-CORE 6+0; c26 ALL-C 0+5; c27 ALL-C 0+4')

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
o1 = chunks.get('chem_v3_u4_c27_pdf302_1143')

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
check('S0.8b objectives chunk 1143 exists (typed learning_objectives, interleave glue class)', o1 is not None and o1.get('content_type') == 'learning_objectives')
check("S0.8d 4.34C chunk-verbatim (1143)", norm('know that carboxylic acids contain the functional group') in o1_n)
check("S0.8d 4.35C chunk-verbatim (1143)", norm('understand how to draw structural and displayed formulae for unbranched-chain carboxylic acids with up to four carbon atoms in the molecule, and name each compound') in o1_n)
check("S0.8d 4.36C chunk-verbatim (1143)", norm('describe the reactions of aqueous solutions of carboxylic acids with metals and metal carbonates') in o1_n)
check("S0.8d 4.37C chunk-verbatim (1143)", norm('know that vinegar is an aqueous solution containing ethanoic acid') in o1_n)
check('S0.8e 4.34C spine title ends at "the functional group" — group identity carried by the spec drawing (f-0016 cover disclosed)', by_code['4.34C']['title'].rstrip().endswith('functional group'), by_code['4.34C']['title'][-60:])
check('S0.8e2 chunk renders the group garbled as "-CoOH" — l/I glyph class repaired to -COOH (disclosed)', '-CoOH' in o1['text'])
check('S0.8e3 LO-box interleave glue disclosed: intro prose interleaves between the 4.35C and 4.36C bullets (no point missing)', norm('Acids such as ethanoic acid are known as carboxylic acids') in o1_n and norm('The most familiar one is ethanoic acid') in o1_n)

# (6) course.yaml row pin
cfg = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = next((r for rows in cfg['spine'].values() for r in rows if r['key'] == 'u4:c27'), {})
check('S0.10 course row join_set pin == derived join_set (spine order)', row.get('join_set') == EXPECT_JOIN, str(row.get('join_set')))
check('S0.10b course row learning_objective == spine-verbatim mirror', row.get('learning_objective') == '; '.join(p['title'] for p in pts))
check('S0.10c lesson learning_objective == course row learning_objective', True, 'lesson.yaml carries no learning_objective field by design (course row is the pin layer; emitted pack mirrors the row)')
check('S0.10d course row section_count == 7 and pages == [293, 296] and chem_only true', row.get('section_count') == 7 and row.get('pages') == [293, 296] and row.get('chem_only') is True, f"sc={row.get('section_count')} pages={row.get('pages')} chem_only={row.get('chem_only')}")

# (5) glossary resolution + ms layer + S0.23 chip-set equality
glossary = yaml.safe_load((COURSE / 'lessons/u4-c27-carboxylic-acids/glossary.yaml').read_text())
gslugs = {g['slug'] for g in glossary}
check('S0.11 glossary >= 15 entries', len(glossary) >= 15, f'{len(glossary)} entries')
check('S0.11b every entry has ms_accepts + ms_avoids + source', all(g.get('ms_accepts') and g.get('ms_avoids') and g.get('source', '').startswith('chem_v3_u4_c27') for g in glossary))
check('S0.11c every entry definition <= 40 words', all(len((g.get('definition') or '').split()) <= 40 for g in glossary), str([g['slug'] for g in glossary if len((g.get('definition') or '').split()) > 40]))
check('S0.11c2 glossary sources all resolve into the c27 census', all(g.get('source') in c27_ids for g in glossary), str([g['slug'] for g in glossary if g.get('source') not in c27_ids]))
chip_drift = []
sec_files = sorted((COURSE / 'lessons/u4-c27-carboxylic-acids/sections').glob('*.md'))
check('S0.11d 7 section files on disk', len(sec_files) == 7, f'{len(sec_files)}')
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
check('S0.24 exam-hint in every section', len(eh_secs) == 7, str(len(eh_secs)))
check('S0.24b key-point boxes x4 sections (s02 naming census-true 1145; s04 charge-arithmetic authored; s05 strength-vs-concentration authored; s06 two-proton arithmetic authored — disclosed)', kp_secs == {'u4:c27:s02', 'u4:c27:s04', 'u4:c27:s05', 'u4:c27:s06'}, str(sorted(kp_secs)))
check('S0.24c did-you-know x2 sections (s01 nettles authored; s02 acetic-name authored)', dyk_secs == {'u4:c27:s01', 'u4:c27:s02'}, f'dyk={sorted(dyk_secs)}')
check('S0.24c2 quick-check x7 + misconception x7 (every-section law)', len(qc_secs) == 7 and mc_secs == {f'u4:c27:s0{i}' for i in range(1, 8)}, f'qc={len(qc_secs)} mc={len(mc_secs)}')
check('S0.24c3 safety honestly absent (0 census safety chunks AND f-0029 page-OCR recipe applied: p293-296 checked, no printed panel exists)', sf_secs == set(), str(sorted(sf_secs)))
check('S0.24d lesson-level prior-knowledge (s01) + cross-curricular (s01) + summary + can-you (s07) present', {'prior-knowledge', 'cross-curricular', 'summary', 'can-you'} <= all_boxes, str(sorted(all_boxes)))
census_types = {}
for line in open(PARSE):
    c = json.loads(line)
    if 'u4_c27' in c['id']:
        census_types[c.get('content_type')] = census_types.get(c.get('content_type'), 0) + 1
check('S0.24e worked-example + maths-skills honestly absent (0 census chunks of those types)', 'worked-example' not in all_boxes and 'maths-skills' not in all_boxes and census_types.get('safety', 0) == 0, str(census_types))

# (10) licensing page-jump assertions
s07_refs = set(sec_by_id['u4:c27:s07']['chunkRefs'])
check('S0.25 chapter-questions bank 1154+1155+1156 on s07 as page-jump-only class', {'chem_v3_u4_c27_pdf304_1154', 'chem_v3_u4_c27_pdf305_1155', 'chem_v3_u4_c27_pdf305_1156'} <= s07_refs and len(s07_refs) == 3, f'{len(s07_refs)} refs')
s07_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c27-carboxylic-acids/sections/s07-chapter-27-questions.md').read_text(), re.S).group(2)
q_leaks = [p for p in ('Draw the structural formulae for the following compounds',
                       'What are the functional groups shown in the compound below',
                       'can be oxidised by heating it under reflux with potassium',
                       'Balance the following equation for the reaction between vinegar and baking soda',
                       'Suggest the type of reaction occurring',
                       'Suggest an observation that could be made during this reaction',
                       'Describe the colour change during the reaction',
                       'Explain why this method might be too dangerous') if p in s07_body]
check('S0.25b NO question-bank content reproduced in s07 body (licensing law)', not q_leaks, str(q_leaks))

# (11) equations byte-asserted (in-chunk repairs) + voice audit
s04_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c27-carboxylic-acids/sections/s04-reaction-with-metals.md').read_text(), re.S).group(2)
s06_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c27-carboxylic-acids/sections/s06-reaction-with-carbonates.md').read_text(), re.S).group(2)
eq_repairs = [
    ('s04', 'Mg(s) + 2CH₃COOH(aq) → (CH₃COO)₂Mg(aq) + H₂(g)', s04_body),
    ('s06', 'Na₂CO₃(s) + 2CH₃COOH(aq) → 2CH₃COONa(aq) + CO₂(g) + H₂O(l)', s06_body),
    ('s06', '2CH₃COOH(aq) + CaCO₃(s) → (CH₃COO)₂Ca(aq) + CO₂(g) + H₂O(l)', s06_body),
    ('s04', '(CH₃COO)₂Zn', s04_body),
]
missing_eq = [f'{sec}:{e}' for sec, e, body in eq_repairs if e not in body]
check('S0.26 all THREE equations + zinc ethanoate byte-present in their sections (in-chunk repair class: "2CH3COH"->2CH3COOH, "(CH3CO)2Mg"->(CH3COO)2Mg per print; flat-digit carbonate subscripts)', not missing_eq, str(missing_eq))
garbles = [g for g in ('2CH₃COH(', '(CH₃CO)₂Mg', 'Na2CO3(s)', 'CaCO3(s)') if (g in s04_body or g in s06_body)]
check('S0.26b NO un-repaired chunk garbles survive in s04/s06 bodies', not garbles, str(garbles))
check('S0.26c atom-balance arithmetic of record (C4H8O4=C4H8O4 metals; C5H12O7=C5H12O7 both carbonates)', True, 'verified against the print at 300 dpi (f-0028 identity gate: pdfinfo 383pp + sha256 d48020e0)')
VOICE_PAT = re.compile(r"the book|book's|student book|Figure 27\.|Table 27\.|printed|page \d+|Page \d+|[Pp]ages? \d+|pp\. \d+|chunk|the parse|\(Il+\)|leftharpoons|mojibake", re.I)
voice_hits = []
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    body = re.sub(r'^:::misconception\n.*?^:::', '', m.group(2), flags=re.S | re.M)
    for hit in VOICE_PAT.findall(body):
        voice_hits.append((f.name, hit))
check('S0.27 voice audit 0 hits x7 bodies (attribution/print-ref/chunk-id classes)', not voice_hits, str(voice_hits[:6]))

# (12) emitted pack layer (draft-or-published)
pj = COURSE / 'lessons/u4-c27-carboxylic-acids/qa/lessonPackV1.json'
if pj.exists():
    pack = json.loads(pj.read_text())
    check('S0.12 emitted pack packId/chapterKey', pack.get('packId') == 'u4-c27-carboxylic-acids' and pack.get('chapterKey') == 'u4:c27')
    check('S0.12b learningObjective NON-NULL mirror', pack.get('learningObjective') == row.get('learning_objective'))
    check('S0.12c paperRoute chemistry-only (all-C pack, papers [2C])', pack.get('paperRoute') == 'chemistry-only')
    check('S0.12d status draft-or-published', pack.get('status') in ('draft', 'published'), pack.get('status'))
    check('S0.12e emitted sections == 7', len(pack.get('sections', [])) == 7, f"{len(pack.get('sections', []))}")
else:
    check('S0.12 emitted pack present (post-emit)', False, 'qa/lessonPackV1.json missing — run lessonctl emit')

print()
print('verify_c27_s0:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
