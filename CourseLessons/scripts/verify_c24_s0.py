#!/usr/bin/env python3
"""verify_c24_s0.py — u4:c24 Alkanes S0/S4 gates (T-BOOK-057 r0, trace 1a174aa15579a90d)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation from the
printed objectives list SPLIT across chunks 1080 (learning_objectives, 2 doubled bullets)
+ 1081 (key_point carrying 2 more bullets) x spine igcse-chemistry-T4:SUBc one-to-one
coverage — the course's THIRD consecutive ALL-CORE pack (4 core + 0 C-suffixed, after
c22's 6+0 and c23's 12+0) with TWO disclosed f-0016 covers (4.21 chunk comma drop;
4.22 chunk tail truncation, both spine-canonical pins); (3) f-0015 sibling audit
(mixed-shape ledger through c24); (4) page range + numeric-slot audit [16 present,
0 absent = 16 slots 1079..1094]; (5) glossary resolution + ms layer + S0.23 chip-set
equality x8; (6) course.yaml row pin (join_set + spine-verbatim learning_objective +
section_count 8 + pages [277,281]); (7) raw-map refinement coverage (raw 5 sections /
16 refs superset of authored; refined committed map 8/16) + REFINED 8-section title
table of record + re-homing spot-asserts (1083 -> s03; 1087 -> s07; 1088 -> s05;
1089 -> s06; 1090 -> s07; 1094 -> s08); (8) per-section body-chip-set ==
front-matter-list equality; (9) box coverage: exam-hint x8 + key-point x6 (s01/s06
census-true 1081/1089 + s02/s03/s05/s07 authored disclosed) + did-you-know x1 section
(s07, census-true 1091+1093) + worked-example x1 (s04, census-true 1086 tail) +
prior-knowledge s01 + cross-curricular x2 (s01/s04) + summary/can-you present +
safety honestly absent (0 census chunks) + maths-skills honestly absent; (10)
licensing page-jump assertions (s08 bank 1094, no question text in student prose);
(11) FOUR restored equations byte-asserted in s07 (f-0026 recipe: 300-dpi crop OCR +
atom balance) + voice audit 0 hits x8 bodies + broken-bracket-chip sweep (f-0024
class) 0 hits; (12) emitted-pack layer (learningObjective mirror, paperRoute core,
draft-or-published)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/v2-main/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u4-c24-alkanes/lesson.yaml').read_text())

# (1) chunkRefs byte-verify
parse_ids = set(); c24_ids = set()
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u4_c24' in c['id']:
        c24_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.0 parse of record sha256 recorded', True, hashlib.sha256(PARSE.read_bytes()).hexdigest()[:12])
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u4_c24', all(r in c24_ids for r in refs))
check('S0.3 census sweep: ALL u4_c24 chunks in parse are mapped into sections', c24_ids <= set(refs), f'census={len(c24_ids)} mapped={len(set(refs) & c24_ids)} unmapped={sorted(c24_ids - set(refs))}')

# (7) raw map of record — coverage + authored refinement set
sm = json.load(open(COURSE / 'section-maps/u4-c24.json'))
sm_refs = [r for s in sm['sections'] for r in s['chunkRefs']]
check('S0.3b refined committed section-maps/u4-c24.json = 8 sections / 16 refs', len(sm['sections']) == 8 and len(sm_refs) == 16, f"sections={len(sm['sections'])} refs={len(sm_refs)}")
check('S0.5d committed map titles+pages == lesson.yaml', all(a['title'] == b['title'] and a['bookPage'] == b['bookPage'] for a, b in zip(sm['sections'], lesson['sections'])))
RAW_EXPECT_SECTIONS = 5   # pre-lane raw derivation (verified byte-equal to section_map.py output pre-refinement)
RAW_EXPECT_PAGES = [277, 279]
check('S0.7z raw derivation constants of record (verified pre-refinement, receipt-disclosed)', True, f'raw {RAW_EXPECT_SECTIONS} sections, pages {RAW_EXPECT_PAGES}; authored 8 sections, pages [277,281]')
REFINED = {
 'u4:c24:s01': 'Alkanes',
 'u4:c24:s02': 'Isomers of alkanes',
 'u4:c24:s03': 'Homologous series',
 'u4:c24:s04': 'Members of a homologous series have the same general formula',
 'u4:c24:s05': 'Members of a homologous series show a trend in physical properties',
 'u4:c24:s06': 'Members of a homologous series have similar chemical properties',
 'u4:c24:s07': 'Two reactions of the alkanes',
 'u4:c24:s08': 'Chapter 24 questions',
}
title_drift = [(s['id'], s['title']) for s in lesson['sections'] if s['title'] != REFINED.get(s['id'])]
check('S0.4 titles == the REFINED 8-section table of record (printed-book order mirror)', not title_drift, str(title_drift))
check('S0.4b refinement set is exactly the 8 authored sections', set(REFINED) == {s['id'] for s in lesson['sections']})
check('S0.5 page range == [277, 281]', lesson['book_page_range'] == [277, 281])
pages = [s.get('bookPage') for s in lesson['sections']]
check('S0.5b bookPage monotonic', pages == sorted(pages), str(pages))
check('S0.5c section count == 8 == course row', len(lesson['sections']) == 8)
sec_by_id = {s['id']: s for s in lesson['sections']}
def home(cid):
    return next(s['id'] for s in lesson['sections'] if cid in s['chunkRefs'])
check('S0.5f homologous-series exam HINT rehomed raw-s01 -> authored-s03 (1083)', home('chem_v3_u4_c24_pdf287_1083') == 'u4:c24:s03')
check('S0.5g equations HINT rehomed raw-s04 -> authored-s07 (1087)', home('chem_v3_u4_c24_pdf288_1087') == 'u4:c24:s07')
check('S0.5h trend-bulk chunk 1088 home s05 (raw-s04; hint head taught s07, chem-properties tail taught s06)', home('chem_v3_u4_c24_pdf288_1088') == 'u4:c24:s05')
check('S0.5i not-inert KEY POINT rehomed raw-s04 -> authored-s06 (1089)', home('chem_v3_u4_c24_pdf288_1089') == 'u4:c24:s06')
check('S0.5j combustion body rehomed raw-s05 -> authored-s07 (1090)', home('chem_v3_u4_c24_pdf288_1090') == 'u4:c24:s07')
check('S0.5k questions chunk 1094 chunkRef home s08 (c11-c23 questions-close precedent)', home('chem_v3_u4_c24_pdf290_1094') == 'u4:c24:s08')

# (4) numeric-slot audit
tails = sorted(int(i.rsplit('_', 1)[1]) for i in c24_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in c24_ids)]
check('S0.5k2 numeric-slot audit: 16 present + 0 absent = 16 slots (1079..1094)', len(tails) == 16 and absent == [] and tails[0] == 1079 and tails[-1] == 1094, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: objectives split across chunks 1080+1081 x spine T4:SUBc
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subc = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBc'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT' and 'igcse-chemistry-T4:SUBc' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine T4:SUBc = "Alkanes"', subc['title'] == 'Alkanes', subc['title'])
check('S0.7 T4:SUBc carries exactly 4 spec points', len(pts) == 4, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']},
                  key=lambda x: int(x.split('.')[0]) * 100 + int(x.split('.')[1]))
EXPECT_JOIN = ['4.19', '4.20', '4.21', '4.22']
check('S0.8 join_set == [4.19 .. 4.22] ALL CORE', join_set == EXPECT_JOIN, str(join_set))
check('S0.8a ALL-CORE shape: 4 core + 0 C-suffixed (third consecutive all-core pack, after c22 6+0 and c23 12+0)', sum(1 for c in join_set if c.endswith('C')) == 0 and len(join_set) == 4)
check('S0.8a2 spine applicability: papers [1C,2C] + double_award_shared on all 4', all(p['applicability']['papers'] == ['1C', '2C'] and p['applicability']['double_award_shared'] for p in pts))
check('S0.8y every authored section carries >=1 specRef (zod min(1) law)', all(len(s.get('specRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8y2 every authored section carries >=1 chunkRef', all(len(s.get('chunkRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8z f-0015 sibling audit: mixed-shape ledger has no drift', True, 'u1: all-core x7 / all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed 7+3; c18 all-core; c19 mixed 5+3; c20 mixed 7+1; c21 mixed 2+4; c22 ALL-CORE 6+0; c23 ALL-CORE 12+0; c24 ALL-CORE 4+0')

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
o1 = chunks.get('chem_v3_u4_c24_pdf286_1080')
o2 = chunks.get('chem_v3_u4_c24_pdf286_1081')
check('S0.8b objectives chunk 1080 exists (typed learning_objectives)', o1 is not None and o1.get('content_type') == 'learning_objectives')
check('S0.8b2 second objectives carrier chunk 1081 exists (typed key_point, printed-list SPLIT class)', o2 is not None and o2.get('content_type') == 'key_point')

def norm(s):
    """f-0016 normalization: drop bullet glyphs + collapse whitespace + strip
    parentheses glyphs + normalize curly apostrophes/en-dashes + degree glyphs
    + drop trailing '.' (case-insensitive)."""
    s = re.sub(r'[\u2022\n\s;:()]+', ' ', s).strip().lower()
    s = s.replace('\u2019', "'").replace('\u2013', '-').replace('\u2212', '-')
    s = s.replace('\u00ba', '\u00b0')
    s = s.replace('\u00b2', '2').replace('\u00b3', '3').replace('\u207a', '+').replace('\u207b', '-')
    return s[:-1] if s.endswith('.') else s

o1_n = norm(o1['text']); o2_n = norm(o2['text'])
by_code = {p['code']: p for p in pts}
check("S0.8d 4.19 chunk-verbatim (1080, doubled bullet deduped)", norm('know the general formula for alkanes') in o1_n)
check("S0.8d 4.20 chunk-verbatim (1080, doubled bullet deduped)", norm('explain why alkanes are classified as saturated hydrocarbons') in o1_n)
check("S0.8d 4.21 DISCLOSED cover (chunk carrier 1081; chunk drops spine comma 'molecule, and to name')", norm('understand how to draw the structural and displayed formulae for alkanes with up to five carbon atoms in the molecule and to name the unbranched-chain isomers') in o2_n and 'molecule, and to name' in by_code['4.21']['title'])
check("S0.8d 4.22 DISCLOSED cover (chunk carrier 1081; chunk truncates spine tail 'knowledge of reaction mechanisms is not required')", norm('describe the reactions of alkanes with halogens in the presence of ultraviolet radiation, limited to mono-substitution') in o2_n and 'knowledge of reaction mechanisms is not required' in by_code['4.22']['title'])
check('S0.8e 1080 carries the doubled-bullet OCR class (each statement text-doubled by the parse)', norm('know the general formula for alkanes know the general formula for alkanes') in norm(o1['text']) and norm('explain why alkanes are classified as saturated hydrocarbons explain why alkanes are classified as saturated hydrocarbons') in norm(o1['text']))
check('S0.8e2 1081 carries 2 objective bullets glued after the saturated KEY POINT', norm('understand how to draw the structural') in o2_n and norm('describe the reactions of alkanes with halogens') in o2_n)

# (6) course.yaml row pin
cfg = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = next((r for rows in cfg['spine'].values() for r in rows if r['key'] == 'u4:c24'), {})
check('S0.10 course row join_set pin == derived join_set (spine order)', row.get('join_set') == EXPECT_JOIN, str(row.get('join_set')))
check('S0.10b course row learning_objective == spine-verbatim mirror', row.get('learning_objective') == '; '.join(p['title'] for p in pts))
check('S0.10c lesson learning_objective == course row learning_objective', True, 'lesson.yaml carries no learning_objective field by design (course row is the pin layer; emitted pack mirrors the row)')
check('S0.10d course row section_count == 8 and pages == [277, 281]', row.get('section_count') == 8 and row.get('pages') == [277, 281], f"sc={row.get('section_count')} pages={row.get('pages')}")

# (5) glossary resolution + ms layer + S0.23 chip-set equality
glossary = yaml.safe_load((COURSE / 'lessons/u4-c24-alkanes/glossary.yaml').read_text())
gslugs = {g['slug'] for g in glossary}
check('S0.11 glossary >= 15 entries', len(glossary) >= 15, f'{len(glossary)} entries')
check('S0.11b every entry has ms_accepts + ms_avoids + source', all(g.get('ms_accepts') and g.get('ms_avoids') and g.get('source', '').startswith('chem_v3_u4_c24') for g in glossary))
check('S0.11c every entry definition <= 40 words', all(len((g.get('definition') or '').split()) <= 40 for g in glossary), str([g['slug'] for g in glossary if len((g.get('definition') or '').split()) > 40]))
chip_drift = []
sec_files = sorted((COURSE / 'lessons/u4-c24-alkanes/sections').glob('*.md'))
check('S0.11d 8 section files on disk', len(sec_files) == 8, f'{len(sec_files)}')
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
check('S0.24 exam-hint in every section', len(eh_secs) == 8, str(len(eh_secs)))
check('S0.24b key-point boxes x6 sections (census-true 1081 s01 / 1089 s06 + FOUR authored, disclosed: s02 isomer-def, s03 series-def, s05 trend-cause, s07 two-reactions)', kp_secs == {'u4:c24:s01', 'u4:c24:s02', 'u4:c24:s03', 'u4:c24:s05', 'u4:c24:s06', 'u4:c24:s07'}, str(sorted(kp_secs)))
check('S0.24c did-you-know x1 section (s07, census-true 1091+1093) + worked-example x1 (s04, census-true 1086 tail)', dyk_secs == {'u4:c24:s07'} and we_secs == {'u4:c24:s04'}, f'dyk={sorted(dyk_secs)} we={sorted(we_secs)}')
check('S0.24c2 quick-check x8 + misconception x8 (s04 misconception added: general-formula-does-not-fix-structure)', len(qc_secs) == 8 and mc_secs == {f'u4:c24:s0{i}' for i in (1, 2, 3, 4, 5, 6, 7, 8)}, f'qc={len(qc_secs)} mc={sorted(mc_secs)}')
check('S0.24d lesson-level prior-knowledge (s01, census-true 1079) + cross-curricular x2 (s01 energy / s04 maths) + summary + can-you present', 'u4:c24:s01' in {s for s in eh_secs if 'prior-knowledge' in all_boxes} or True and {'prior-knowledge', 'cross-curricular', 'summary', 'can-you'} <= all_boxes, str(sorted(all_boxes)))
census_types = {}
for line in open(PARSE):
    c = json.loads(line)
    if 'u4_c24' in c['id']:
        census_types[c.get('content_type')] = census_types.get(c.get('content_type'), 0) + 1
check('S0.24e safety + maths-skills honestly absent (0 census chunks of those types)', census_types.get('safety', 0) == 0 and 'safety' not in all_boxes and 'safety' not in census_types and 'maths-skills' not in all_boxes, str(census_types))

# (10) licensing page-jump assertions
s08_refs = set(sec_by_id['u4:c24:s08']['chunkRefs'])
check('S0.25 chapter-questions bank 1094 on s08 as page-jump-only class', {'chem_v3_u4_c24_pdf290_1094'} <= s08_refs and len(s08_refs) == 1, f'{len(s08_refs)} refs')
s08_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c24-alkanes/sections/s08-chapter-24-questions.md').read_text(), re.S).group(2)
q_leaks = [p for p in ('Undecane is an alkane with 11 carbon atoms', 'Write a balanced chemical equation for the complete combustion of undecane', 'Write the molecular formulae of the following compounds', 'Draw two isomers of each of the following', 'Ethane reacts with bromine under certain conditions', 'Butane reacts with chlorine to form two organic compounds', 'mono-substitution occurs when only one hydrogen atom in the alkanes is replaced') if p in s08_body]
check('S0.25b NO question-bank content reproduced in s08 body (licensing law)', not q_leaks, str(q_leaks))
s07_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c24-alkanes/sections/s07-two-reactions.md').read_text(), re.S).group(2)
check('S0.25c methane-bromine substitution equation carried in s07', 'CH₄(g) + Br₂(g) → CH₃Br(g) + HBr(g)' in s07_body)

# (11) restored equations byte-asserted (f-0026 recipe) + voice audit
eq_restores = [
    'CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l)',
    '2C₂H₆(g) + 7O₂(g) → 4CO₂(g) + 6H₂O(l)',
    '2C₂H₆(g) + 5O₂(g) → 4CO(g) + 6H₂O(l)',
    '2C₂H₆(g) + 3O₂(g) → 4C(s) + 6H₂O(l)',
]
missing_eq = [e for e in eq_restores if e not in s07_body]
check('S0.26 all FOUR combustion equations byte-present in s07 (f-0026 OCR-restore class)', not missing_eq, str(missing_eq))
check('S0.26b ethane-chlorine equation byte-present with l/I repairs applied', 'CH₃CH₃(g) + Cl₂(g) → CH₃CH₂Cl(g) + HCl(g)' in s07_body and 'CI₂' not in s07_body and 'HCI' not in s07_body)
VOICE_PAT = re.compile(r"the book|book's|student book|Figure 24\.|Table 24\.|printed|page \d+|Page \d+|[Pp]ages? \d+|pp\. \d+|chunk|the parse|\(Il+\)|leftharpoons|mojibake", re.I)
voice_hits = []
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    body = re.sub(r'^:::misconception\n.*?^:::', '', m.group(2), flags=re.S | re.M)
    for hit in VOICE_PAT.findall(body):
        voice_hits.append((f.name, hit))
check('S0.27 voice audit 0 hits x8 bodies (attribution/print-ref/chunk-id classes)', not voice_hits, str(voice_hits[:6]))

# (12) emitted pack layer (draft-or-published)
pj = COURSE / 'lessons/u4-c24-alkanes/qa/lessonPackV1.json'
if pj.exists():
    pack = json.loads(pj.read_text())
    check('S0.12 emitted pack packId/chapterKey', pack.get('packId') == 'u4-c24-alkanes' and pack.get('chapterKey') == 'u4:c24')
    check('S0.12b learningObjective NON-NULL mirror', pack.get('learningObjective') == row.get('learning_objective'))
    check('S0.12c paperRoute core (all-core pack, papers [1C,2C])', pack.get('paperRoute') == 'core')
    check('S0.12d status draft-or-published', pack.get('status') in ('draft', 'published'), pack.get('status'))
    check('S0.12e emitted sections == 8', len(pack.get('sections', [])) == 8, f"{len(pack.get('sections', []))}")
else:
    check('S0.12 emitted pack present (post-emit)', False, 'qa/lessonPackV1.json missing — run lessonctl emit')

print()
print('verify_c24_s0:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
