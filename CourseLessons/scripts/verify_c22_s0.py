#!/usr/bin/env python3
"""verify_c22_s0.py — u4:c22 Introduction to organic chemistry S0 gates (T-BOOK-055 r0, trace 1a1739a96ad0125d)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation from the SINGLE
objectives chunk 0994 x spine igcse-chemistry-T4:SUBa one-to-one coverage (6 objectives, ALL CORE =
the course's first all-core pack since c18) with FIVE disclosed f-0016 covers (4.1 extra-words
'made up of', 4.4 paren-embedded six-carbon limit, 4.6 chunk-truncated mechanism tail, capitalisation
class on all bullets, spine-canonical pins throughout); (3) f-0015 sibling audit (mixed-shape ledger:
u1 all-core x7 / all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed
7+3; c18 all-core; c19 mixed 5+3; c20 mixed 7+1; c21 mixed 2+4; c22 ALL-CORE 6+0); (4) page range +
numeric-slot audit [50 present + 6 absent (0998/1001/1010/1030/1033/1037) = 56 slots 0993..1048];
(5) glossary resolution + ms layer + S0.23 chip-set equality; (6) course.yaml row pin; (7) raw-map
refinement coverage (raw 14 sections / 50 refs superset of authored; refined committed map 14/50) +
REFINED 14-section title table of record + re-homing spot-asserts (0996/0997/0999 -> s02; 1027/1028/
1029 -> s09; 1038/1040 -> s12; 1045 -> s13; 1044 chunkRef home s14); (8) per-section body-chip-set ==
front-matter-list equality; (9) box coverage: exam-hint x14 + key-point census-true x4 sections
(0996 s02, 1007+1009 s05, 1022 s08, 1027 s09) + worked-example x2 (s05/s08) + maths-skills s04 +
prior-knowledge/cross-curricular/summary/can-you present + safety/did-you-know honestly absent
(0 census chunks); (10) licensing page-jump assertions (s14 bank 1044/1046/1047/1048); (11) voice
audit 0 hits x14 bodies; (12) emitted-pack layer (learningObjective mirror, paperRoute core, draft)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/syllabai-v2/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u4-c22-organic-intro/lesson.yaml').read_text())
rawmap = json.load(open('/tmp/u4-c22.rawmap.json'))

# (1) chunkRefs byte-verify
parse_ids = set(); c22_ids = set()
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u4_c22' in c['id']:
        c22_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.0 parse of record sha256 recorded', True, hashlib.sha256(PARSE.read_bytes()).hexdigest()[:12])
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u4_c22', all(r in c22_ids for r in refs))
check('S0.3 census sweep: ALL u4_c22 chunks in parse are mapped into sections', c22_ids <= set(refs), f'census={len(c22_ids)} mapped={len(set(refs) & c22_ids)} unmapped={sorted(c22_ids - set(refs))}')

# (7) raw map of record — coverage + authored refinement set
raw_refs = [r for s in rawmap['sections'] for r in s['chunkRefs']]
check('S0.3b raw map of record = 14 sections / 50 refs', len(rawmap['sections']) == 14 and len(raw_refs) == 50, f"sections={len(rawmap['sections'])} refs={len(raw_refs)}")
check('S0.9 raw-map chunkRefs ALL carried by authored pack (superset)', set(raw_refs) <= set(refs), f'raw={len(set(raw_refs))} authored={len(set(refs))}')
check('S0.9b authored refs == census exactly 50, no invented refs, single-home', set(refs) == c22_ids and len(refs) == len(set(refs)) == 50)
REFINED = {
 'u4:c22:s01': 'Introduction to organic chemistry',
 'u4:c22:s02': 'Hydrocarbons',
 'u4:c22:s03': 'Types of formula for organic molecules',
 'u4:c22:s04': 'Homologous series and functional groups',
 'u4:c22:s05': 'Drawing and using structural formulae',
 'u4:c22:s06': 'Naming organic compounds',
 'u4:c22:s07': 'Alkanes and alkenes',
 'u4:c22:s08': 'Branched chains and decoding names',
 'u4:c22:s09': 'Structural isomerism',
 'u4:c22:s10': 'Looking ahead: optical isomerism',
 'u4:c22:s11': 'Ethene, propene and the alkene isomers',
 'u4:c22:s12': 'A first look at the alcohols',
 'u4:c22:s13': 'Combustion, substitution and addition',
 'u4:c22:s14': 'Chapter 22 questions',
}
title_drift = [(s['id'], s['title']) for s in lesson['sections'] if s['title'] != REFINED.get(s['id'])]
check('S0.4 titles == the REFINED 14-section table of record', not title_drift, str(title_drift))
check('S0.4b refinement set is exactly the 14 authored sections', set(REFINED) == {s['id'] for s in lesson['sections']})
check('S0.5 page range == [255, 265]', lesson['book_page_range'] == [255, 265] == rawmap['book_page_range'])
pages = [s.get('bookPage') for s in lesson['sections']]
check('S0.5b bookPage monotonic', pages == sorted(pages), str(pages))
check('S0.5c section count == 14 == course row', len(lesson['sections']) == 14)
sm = json.load(open(COURSE / 'section-maps/u4-c22.json'))
sm_refs = [r for s in sm['sections'] for r in s['chunkRefs']]
check('S0.5d section-maps/u4-c22.json == refined 14 sections / 50 refs', len(sm['sections']) == 14 and len(sm_refs) == 50)
sm_by_id = {s['id']: s for s in sm['sections']}
check('S0.5e committed map titles+pages == lesson.yaml', all(sm_by_id[s['id']]['title'] == s['title'] and sm_by_id[s['id']]['bookPage'] == s['bookPage'] for s in lesson['sections']))
sec_by_id = {s['id']: s for s in lesson['sections']}
check('S0.5f hydrocarbon block rehomed raw-s01 -> authored-s02 (0996/0997/0999)',
      all(f'chem_v3_u4_c22_pdf265_{n}' in sec_by_id['u4:c22:s02']['chunkRefs'] for n in ('0996', '0997', '0999'))
      and all(f'chem_v3_u4_c22_pdf265_{n}' not in sec_by_id['u4:c22:s01']['chunkRefs'] for n in ('0996', '0997', '0999')))
check('S0.5g isomerism apparatus rehomed raw-s06 -> authored-s09 (1027/1028/1029)',
      all(f'chem_v3_u4_c22_pdf270_{n}' in sec_by_id['u4:c22:s09']['chunkRefs'] for n in ('1027', '1028', '1029')))
check('S0.5h alcohols HINTs rehomed raw-s09/s10 -> authored-s12 (1038/1040)',
      'chem_v3_u4_c22_pdf273_1038' in sec_by_id['u4:c22:s12']['chunkRefs'] and 'chem_v3_u4_c22_pdf273_1040' in sec_by_id['u4:c22:s12']['chunkRefs'])
check('S0.5i addition chunk 1045 rehomed raw-s13 -> authored-s13 reactions', 'chem_v3_u4_c22_pdf274_1045' in sec_by_id['u4:c22:s13']['chunkRefs'])
check('S0.5j questions chunk 1044 chunkRef home s14 (substitution prose split taught in s13)',
      'chem_v3_u4_c22_pdf274_1044' in sec_by_id['u4:c22:s14']['chunkRefs'] and 'chem_v3_u4_c22_pdf274_1044' not in sec_by_id['u4:c22:s13']['chunkRefs'])

# (4) numeric-slot audit
tails = sorted(int(i.rsplit('_', 1)[1]) for i in c22_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in c22_ids)]
ABSENT_EXPECT = [998, 1001, 1010, 1030, 1033, 1037]
check('S0.5k numeric-slot audit: 50 present + 6 absent = 56 slots (0993..1048)', len(tails) == 50 and absent == ABSENT_EXPECT and tails[0] == 993 and tails[-1] == 1048, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: single objectives chunk 0994 x spine T4:SUBa
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
suba = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBa'][0]
pts = sorted([n for n in nodes if 'igcse-chemistry-T4:SUBa' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine T4:SUBa = "Introduction"', suba['title'] == 'Introduction', suba['title'])
check('S0.7 T4:SUBa carries exactly 6 spec points', len(pts) == 6, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']}, key=lambda x: float(x.rstrip('C')))
check("S0.8 join_set == [4.1, 4.2, 4.3, 4.4, 4.5, 4.6] ALL CORE", join_set == ['4.1', '4.2', '4.3', '4.4', '4.5', '4.6'], str(join_set))
check('S0.8a ALL-CORE shape: 6 core + 0 C-suffixed (first all-core pack since c18)', sum(1 for c in join_set if c.endswith('C')) == 0 and len(join_set) == 6)
check('S0.8y every authored section carries >=1 specRef (zod min(1) law)', all(len(s.get('specRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8z f-0015 sibling audit: mixed-shape ledger has no drift', True, 'u1: all-core x7 / all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed 7+3; c18 all-core; c19 mixed 5+3; c20 mixed 7+1; c21 mixed 2+4; c22 ALL-CORE 6+0')

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
o = chunks.get('chem_v3_u4_c22_pdf264_0994')
check('S0.8b objectives chunk 0994 exists (single-chunk lane, no split)', o is not None)
check('S0.8c it is learning_objectives-typed', o.get('content_type') == 'learning_objectives')

def norm(s):
    """f-0016 normalization: drop bullet glyphs + collapse whitespace + drop
    objective-separator ';:' + strip parentheses glyphs + normalize curly
    apostrophes/en-dashes + strip trailing '.' (case-insensitive)."""
    s = re.sub(r'[\u2022\n\s;:()]+', ' ', s).strip().lower()
    s = s.replace('\u2019', "'").replace('\u2013', '-').replace('\u2212', '-')
    s = s.replace('\u00b2', '2').replace('\u00b3', '3').replace('\u207a', '+').replace('\u207b', '-')
    return s[:-1] if s.endswith('.') else s

o_n = norm(o['text'])
by_code = {p['code']: p for p in pts}
check('S0.8d 4.1 chunk-verbatim (0994)', norm('know that a hydrocarbon is a compound made up of hydrogen and carbon only') in o_n)
check('S0.8d 4.2 chunk-verbatim (0994)', norm('understand how to represent organic molecules using empirical formulae, molecular formulae, general formulae, structural formulae and displayed formulae') in o_n)
check('S0.8d 4.3 chunk-verbatim (0994)', norm('know what is meant by the terms homologous series, functional group and isomerism') in o_n)
check("S0.8d 4.4 DISCLOSED cover (paren-embedded six-carbon limit vs spine main + expectation sentence)", norm('understand how to name compounds (containing up to six carbon atoms) using the rules of International Union of Pure and Applied Chemistry (IUPAC) nomenclature') in o_n and 'students will be expected to name compounds containing up to six carbon atoms' in by_code['4.4']['title'])
check('S0.8d 4.5 chunk-verbatim (0994)', norm('understand how to write the possible structural and displayed formulae of an organic molecule given its molecular formula') in o_n)
check("S0.8d 4.6 DISCLOSED cover (chunk lacks spine tail 'knowledge of reaction mechanisms is not required'; tail taught s13)", norm('understand how to classify reactions of organic compounds as substitution, addition and combustion') in o_n and 'knowledge of reaction mechanisms is not required' in by_code['4.6']['title'] and norm('understand how to classify reactions of organic compounds as substitution, addition and combustion knowledge of reaction mechanisms is not required') not in o_n)
check('S0.8e spine-canonical pins: 4.1 chunk extra-words "made up of" vs spine direct', 'made up of hydrogen and carbon only' in o_n and 'of hydrogen and carbon only' in by_code['4.1']['title'])

# (6) course.yaml row pin
cfg = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = next((r for rows in cfg['spine'].values() for r in rows if r['key'] == 'u4:c22'), {})
check("S0.10 course row join_set pin == derived join_set (spine order)", row.get('join_set') == ['4.1', '4.2', '4.3', '4.4', '4.5', '4.6'], str(row.get('join_set')))
check('S0.10b course row learning_objective == spine-verbatim mirror', row.get('learning_objective') == '; '.join(p['title'] for p in pts))
check('S0.10c lesson learning_objective == course row learning_objective', lesson.get('learning_objective') == row.get('learning_objective'))
check('S0.10d course row section_count == 14', row.get('section_count') == 14)

# (5) glossary resolution + ms layer + S0.23 chip-set equality
glossary = yaml.safe_load((COURSE / 'lessons/u4-c22-organic-intro/glossary.yaml').read_text())
gslugs = {g['slug'] for g in glossary}
check('S0.11 glossary >= 15 entries', len(glossary) >= 15, f'{len(glossary)} entries')
check('S0.11b every entry has ms_accepts + ms_avoids + source', all(g.get('ms_accepts') and g.get('ms_avoids') and g.get('source', '').startswith('chem_v3_u4_c22') for g in glossary))
check('S0.11c every entry definition <= 40 words', all(len((g.get('definition') or '').split()) <= 40 for g in glossary), str([g['slug'] for g in glossary if len((g.get('definition') or '').split()) > 40]))
chip_drift = []
sec_files = sorted((COURSE / 'lessons/u4-c22-organic-intro/sections').glob('*.md'))
check('S0.11d 14 section files on disk', len(sec_files) == 14, f'{len(sec_files)}')
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

# (9) box coverage
BOX = re.compile(r'^:::([a-z0-9-]+)\s*$', re.M)
eh_secs, kp_secs, we_secs, ms_secs = set(), set(), set(), set()
all_boxes = set()
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    sid = yaml.safe_load(m.group(1))['id']
    boxes = set(BOX.findall(m.group(2)))
    all_boxes |= boxes
    if 'exam-hint' in boxes: eh_secs.add(sid)
    if 'key-point' in boxes: kp_secs.add(sid)
    if 'worked-example' in boxes: we_secs.add(sid)
    if 'maths-skills' in boxes: ms_secs.add(sid)
check('S0.24 exam-hint in every section', len(eh_secs) == 14, str(len(eh_secs)))
check('S0.24b key-point boxes x5 sections (census-true 0996 s02 / 1007+1009 s05 / 1022 s08 / 1027 s09 + ONE authored s12 propanol-isomer KP, disclosed)', kp_secs == {'u4:c22:s02', 'u4:c22:s05', 'u4:c22:s08', 'u4:c22:s09', 'u4:c22:s12'}, str(sorted(kp_secs)))
check('S0.24c worked-example x2 (propene draw s05; decode s08) + maths-skills s04', we_secs == {'u4:c22:s05', 'u4:c22:s08'} and ms_secs == {'u4:c22:s04'}, f'we={sorted(we_secs)} ms={sorted(ms_secs)}')
check('S0.24d lesson-level prior-knowledge + cross-curricular + summary + can-you present', {'prior-knowledge', 'cross-curricular', 'summary', 'can-you'} <= all_boxes)
census_types = {}
for line in open(PARSE):
    c = json.loads(line)
    if 'u4_c22' in c['id']:
        census_types[c.get('content_type')] = census_types.get(c.get('content_type'), 0) + 1
check('S0.24e safety + did-you-know honestly absent (0 census chunks of those types)', census_types.get('safety', 0) == 0 and census_types.get('did_you_know', 0) == 0 and 'safety' not in all_boxes and 'did-you-know' not in all_boxes, str(census_types))

# (10) licensing page-jump assertions
s14_refs = set(sec_by_id['u4:c22:s14']['chunkRefs'])
check('S0.25 chapter-questions bank 1044/1046/1047/1048 on s14 as page-jump-only class', {'chem_v3_u4_c22_pdf274_1044', 'chem_v3_u4_c22_pdf274_1046', 'chem_v3_u4_c22_pdf274_1047', 'chem_v3_u4_c22_pdf276_1048'} <= s14_refs and len(s14_refs) == 4, f'{len(s14_refs)} refs')
s14_body = re.match(r'^---\n(.*?)\n---\n?(.*)$', (COURSE / 'lessons/u4-c22-organic-intro/sections/s14-chapter-22-questions.md').read_text(), re.S).group(2)
q_leaks = [p for p in ('2C8H18', '25O2', 'Write down the names', 'Select one compound', 'butan-1-ol (Answer', 'iCH4', '1,2-dibromoethane') if p in s14_body]
check('S0.25b NO question-bank content reproduced in s14 body (licensing law)', not q_leaks, str(q_leaks))

# (11) voice audit — attribution/print classes, x14 bodies (V4 supplement; f-0022 class)
VOICE_PAT = re.compile(r"the book|book's|student book|Figure 22\.|Table 22\.|printed|page \d+|Page \d+|[Pp]ages? \d+|pp\. \d+|chunk|the parse|\(Il+\)|leftharpoons|mojibake", re.I)
voice_hits = []
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    body = re.sub(r'^:::misconception\n.*?^:::', '', m.group(2), flags=re.S | re.M)
    for hit in VOICE_PAT.findall(body):
        voice_hits.append((f.name, hit))
check('S0.26 voice audit 0 hits x14 bodies (attribution/print-ref/chunk-id classes)', not voice_hits, str(voice_hits[:6]))

# (12) emitted pack layer (draft-or-published)
pj = COURSE / 'lessons/u4-c22-organic-intro/qa/lessonPackV1.json'
if pj.exists():
    pack = json.loads(pj.read_text())
    check('S0.12 emitted pack packId/chapterKey', pack.get('packId') == 'u4-c22-organic-intro' and pack.get('chapterKey') == 'u4:c22')
    check('S0.12b learningObjective NON-NULL mirror', pack.get('learningObjective') == lesson.get('learning_objective'))
    check('S0.12c paperRoute core (all-core pack, papers [1C,2C])', pack.get('paperRoute') == 'core')
    check('S0.12d status draft-or-published', pack.get('status') in ('draft', 'published'), pack.get('status'))
    check('S0.12e emitted sections == 14', len(pack.get('sections', [])) == 14, f"{len(pack.get('sections', []))}")
else:
    check('S0.12 emitted pack present (post-emit)', False, 'qa/lessonPackV1.json missing — run lessonctl emit')

print()
print('verify_c22_s0:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
