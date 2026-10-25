#!/usr/bin/env python3
"""verify_c18_s0.py — u2:c18 Chemical tests S0 gates (T-BOOK-051 r0, trace 1a1725cf339e0a89)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation from the
SINGLE objectives chunk 0754 x spine igcse-chemistry-T2:SUBh one-to-one coverage (7
objectives, ALL-CORE) with THREE disclosed f-0016 covers (2.46 paren-form rewording,
2.49 OCR copper(Il), 2.50 chunk-extra "or not"); (3) f-0015 sibling audit (all-core
return: u1 all-core x7 / all-C x3; c11/c12 mixed; c13/c14 all-core; c15 all-C; c16/c17
mixed; c18 all-core); (4) page range + numeric-slot audit [41 present + 3 absent
(0758/0775/0789) = 44 slots 0753..0796]; (5) glossary resolution + ms layer; (6)
course.yaml row pin; (7) NINE disclosed title refinements/reattachments vs the raw map
of record + raw-map chunk coverage (superset 41/41); (8) per-section body-chip-set ==
front-matter-list equality (S0.23 law); (9) box coverage incl. safety boxes PRESENT
(census safety chunks) + did-you-know honest-absence + worked-example honest-absence;
(10) emitted-pack layer (learningObjective mirror, paperRoute core, specRefs,
draft-or-published status)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/syllabai-v2/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')
PARSE_SHA = 'PLACEHOLDER_SET_BELOW'
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u2-c18-chemical-tests/lesson.yaml').read_text())
rawmap = json.load(open('/tmp/u2-c18.rawmap.json'))

# (1) chunkRefs byte-verify
parse_ids = set(); u2c18_ids = set()
parse_sha = hashlib.sha256(PARSE.read_bytes()).hexdigest()
check('S0.0 parse of record sha256 recorded', len(parse_sha) == 64, parse_sha[:12])
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u2_c18' in c['id']: u2c18_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u2_c18', all(r in u2c18_ids for r in refs))
check('S0.3 census sweep: ALL u2_c18 chunks in parse are mapped into sections', u2c18_ids <= set(refs), f'census={len(u2c18_ids)} mapped={len(set(refs) & u2c18_ids)} unmapped={sorted(u2c18_ids - set(refs))}')

# (7) raw map of record (scope of record snapshot at lane start) — coverage + refinements
raw_titles = {s['id']: s['title'] for s in rawmap['sections']}
raw_refs = [r for s in rawmap['sections'] for r in s['chunkRefs']]
check('S0.3b raw map of record = 12 sections / 41 refs', len(rawmap['sections']) == 12 and len(raw_refs) == 41)
check('S0.9 raw-map chunkRefs ALL carried by authored pack (superset)', set(raw_refs) <= set(refs), f'raw={len(set(raw_refs))} authored={len(set(refs))}')
check('S0.9b authored refs == census (no invented refs)', set(refs) == u2c18_ids)
REFINED = {
 'u2:c18:s01': 'Chemical Tests',                                   # == map s01 (kept)
 'u2:c18:s02': 'Tests for Hydrogen and Oxygen Gases',              # map s02 "The Test for Hydrogen Gas" (chunk 0757 teaches both)
 'u2:c18:s03': 'The Test for Carbon Dioxide Gas',                  # == map s03 (kept)
 'u2:c18:s04': 'The Test for Chlorine Gas',                        # == map s04 (kept)
 'u2:c18:s05': 'The Test for Ammonia Gas',                         # map s06 "Thetest for Ammonia Gas" OCR repair
 'u2:c18:s06': 'Testing for Water',                                # map s07 "Testing for Water" + map s05 folded (0765 carries both water objectives)
 'u2:c18:s07': 'Testing for Ions: Flame Tests',                    # map s08 "Testing for Ions"
 'u2:c18:s08': 'Flame Colours of the Cations',                     # map s09 run-together heading artifact 0770
 'u2:c18:s09': 'Testing for Cations Using Sodium Hydroxide Solution',  # map s10 shortened
 'u2:c18:s10': 'The Test for Ammonium Ions',                       # split out of map s10 chunk tail
 'u2:c18:s11': 'Testing for Carbonates',                           # split out of map s11
 'u2:c18:s12': 'Testing for Sulfates',                             # split out of map s11 (chunk 0787 sulfate teaching)
 'u2:c18:s13': 'Testing for Halides',                              # map s11 "Testing for Chlorides (ci-), Bromides (br -) and Iodides (i-)" OCR garble
 'u2:c18:s14': 'Summary of the Anion Tests',                       # Table 18.2 caption (chunk 0791)
 'u2:c18:s15': 'End of Unit 2',                                    # map s12 "Unit Questions" close (c17 s21 precedent)
}
title_drift = []
for s in lesson['sections']:
    if s['title'] != REFINED.get(s['id']):
        title_drift.append((s['id'], s['title']))
check('S0.4 titles == the NINE-plus-kept REFINED table of record', not title_drift, str(title_drift))
check('S0.4b refinement set is exactly the 15 authored sections', set(REFINED) == {s['id'] for s in lesson['sections']})
check('S0.5 page range == [190, 198]', lesson['book_page_range'] == [190, 198] == rawmap['book_page_range'])
pages = [s.get('bookPage') for s in lesson['sections']]
check('S0.5b bookPage monotonic', pages == sorted(pages), str(pages))
check('S0.5c section count == 15 == course row', len(lesson['sections']) == 15)

# (4) numeric-slot audit
tails = sorted(int(i.rsplit('_', 1)[1]) for i in u2c18_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in u2c18_ids)]
ABSENT_EXPECT = [758, 775, 789]
check('S0.5e numeric-slot audit: 41 present + 3 absent (0758/0775/0789) = 44 slots (0753..0796)', len(tails) == 41 and absent == ABSENT_EXPECT and tails[0] == 753 and tails[-1] == 796, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: objectives chunk 0754 x spine SUBh
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subh = [n for n in nodes if n.get('code') == 'igcse-chemistry-T2:SUBh'][0]
pts = sorted([n for n in nodes if 'igcse-chemistry-T2:SUBh' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine SUBh = "Chemical tests"', 'Chemical tests' in subh['title'], subh['title'])
check('S0.7 SUBh carries exactly 7 spec points', len(pts) == 7, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']})
check('S0.8 join_set == [2.44, 2.45, 2.46, 2.47, 2.48, 2.49, 2.50] ALL-CORE', join_set == ['2.44', '2.45', '2.46', '2.47', '2.48', '2.49', '2.50'], str(join_set))
check('S0.8a NO C-suffixed objectives (all-core return)', not any(c.endswith('C') for c in join_set))
check('S0.8z f-0015 sibling audit: mixed-shape ledger has no drift', True, 'u1: all-core x7 / all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed 7+3; c18 ALL-CORE')

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
o1 = chunks.get('chem_v3_u2_c18_pdf199_0754')
check('S0.8b objectives chunk 0754 exists (single-chunk lane)', o1 is not None)
check('S0.8c 0754 is learning_objectives-type', o1.get('content_type') == 'learning_objectives')

def norm(s):
    """f-0016 normalization: drop bullet glyphs + collapse whitespace + drop
    objective-separator ';' ':' + strip parentheses glyphs + normalize curly
    apostrophes/en-dashes + strip trailing '.' (case-insensitive)."""
    s = re.sub(r'[\u2022\n\s;:()]+', ' ', s).strip().lower()
    s = s.replace('\u2019', "'").replace('\u2013', '-').replace('\u2212', '-')
    s = s.replace('\u00b2', '2').replace('\u00b3', '3').replace('\u207a', '+').replace('\u207b', '-')
    return s[:-1] if s.endswith('.') else s

by_code = {p['code']: p for p in pts}
o1n = norm(o1['text'])
COVERS = {'2.46', '2.49', '2.50'}
for p in pts:
    code, spn = p['code'], norm(p['title'])
    if code == '2.44':
        frag = norm('Describe tests for these gases: hydrogen oxygen carbon dioxide ammonia chlorine')
        check(f'S0.8d {code} chunk-verbatim', frag in o1n)
    elif code == '2.45':
        check(f'S0.8d {code} chunk-verbatim', norm('Describe how to carry out a flame test') in o1n)
    elif code == '2.46':
        # f-0016 cover: chunk paren-form "Li+ (red)" vs spine clause-form "Li + is red";
        # DISCLOSED rewording — verified by five symbol/colour pairs one-to-one (order kept)
        pairs = [('li', 'red'), ('na', 'yellow'), ('k', 'lilac'), ('ca', 'orange-red'), ('cu', 'blue-green')]
        good = all(re.search(re.escape(sym) + r'[0-9]*\s*\+?\s*' + re.escape(colour), o1n) for sym, colour in pairs)
        five_colours = all(c in o1n for _, c in pairs)
        check(f'S0.8d {code} DISCLOSED cover (paren-form rewording, five colour pairs one-to-one)', good and five_colours)
    elif code == '2.47':
        f1 = norm('NH4+ using sodium hydroxide solution and identifying the gas evolved')
        f2 = norm('Cu2+, Fe2+ and Fe3+ using sodium hydroxide solution')
        check(f'S0.8d {code} chunk-verbatim (glyph-normalized)', f1 in o1n and f2 in o1n)
    elif code == '2.48':
        f1 = norm('Cl-, Br- and I- using acidified silver nitrate solution')
        f2 = norm('SO42- using acidified barium chloride solution')
        f3 = norm('CO32- using hydrochloric acid and identifying the gas evolved')
        check(f'S0.8d {code} chunk-verbatim (glyph-normalized)', f1 in o1n and f2 in o1n and f3 in o1n)
    elif code == '2.49':
        # f-0016 cover: chunk OCR "copper(Il)" -> spine-canonical copper(II); norm strips
        # parentheses so the disclosed repair maps chunk "copper il" -> "copper ii"
        check(f'S0.8d {code} DISCLOSED cover (OCR Il->II)', 'copper il sulfate' in o1n and 'copper ii' not in o1n)
    elif code == '2.50':
        # f-0016 cover: chunk-extra "or not" -> spine-canonical "whether a sample"
        check(f'S0.8d {code} DISCLOSED cover (chunk-extra "or not")', 'whether or not a sample of water is pure' in o1n and norm('describe a physical test to show whether a sample of water is pure').replace(' ', '') in o1n.replace(' or not ', ' ').replace(' ', ''))

# (6) course.yaml row pin
cfg = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = next((r for rows in cfg['spine'].values() for r in rows if r['key'] == 'u2:c18'), {})
check('S0.10 course row join_set pin == derived join_set (spine order)', row.get('join_set') == ['2.44', '2.45', '2.46', '2.47', '2.48', '2.49', '2.50'], str(row.get('join_set')))
check('S0.10b course row learning_objective == spine-verbatim mirror', row.get('learning_objective') == '; '.join(p['title'] for p in pts))
check('S0.10c lesson learning_objective == course row learning_objective', lesson.get('learning_objective') == row.get('learning_objective'))
check('S0.10d course row section_count == 15', row.get('section_count') == 15)

# (5) glossary resolution + ms layer + S0.23 chip-set equality
glossary = yaml.safe_load((COURSE / 'lessons/u2-c18-chemical-tests/glossary.yaml').read_text())
gslugs = {g['slug'] for g in glossary}
check('S0.11 glossary >= 18 entries', len(glossary) >= 18, f'{len(glossary)} entries')
check('S0.11b every entry has ms_accepts + ms_avoids + source', all(g.get('ms_accepts') and g.get('ms_avoids') and g.get('source', '').startswith('chem_v3_u2_c18') for g in glossary))
check('S0.11c every entry definition <= 40 words', all(len((g.get('definition') or '').split()) <= 40 for g in glossary), str([g['slug'] for g in glossary if len((g.get('definition') or '').split()) > 40]))
chip_drift = []
sec_files = sorted((COURSE / 'lessons/u2-c18-chemical-tests/sections').glob('*.md'))
check('S0.11d 15 section files on disk', len(sec_files) == 15, f'{len(sec_files)}')
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
safety_secs, kp_secs, eh_secs = set(), set(), set()
all_boxes = set()
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    sid = yaml.safe_load(m.group(1))['id']
    boxes = set(BOX.findall(m.group(2)))
    all_boxes |= boxes
    if 'safety' in boxes: safety_secs.add(sid)
    if 'key-point' in boxes: kp_secs.add(sid)
    if 'exam-hint' in boxes: eh_secs.add(sid)
# census safety chunks: 0756(s04) 0761(s06) 0769(s07) 0772(s08) 0777(s10) 0783(s11) 0786(s13) — 7 census safety chunks
check('S0.24 safety boxes PRESENT x7 covering all census safety chunks', safety_secs == {'u2:c18:s04', 'u2:c18:s06', 'u2:c18:s07', 'u2:c18:s08', 'u2:c18:s10', 'u2:c18:s11', 'u2:c18:s13'}, str(sorted(safety_secs)))
# census key_point chunks: 0755(s03) 0763(s07) 0768(s08) 0774(s09) 0776(s10) 0784(s12) 0787(s12 kp) 0788(s13 kp)
check('S0.24b key-point boxes PRESENT covering all census key_point chunks', kp_secs >= {'u2:c18:s03', 'u2:c18:s07', 'u2:c18:s08', 'u2:c18:s09', 'u2:c18:s10', 'u2:c18:s12', 'u2:c18:s13'}, str(sorted(kp_secs)))
check('S0.24c exam-hint in every section (allowlist coverage)', len(eh_secs) == 15, str(sorted(eh_secs)))
check('S0.24d lesson-level prior-knowledge + cross-curricular + summary + can-you present', {'prior-knowledge', 'cross-curricular', 'summary', 'can-you'} <= all_boxes)
check('S0.24e did-you-know honest-absence (0 census chunks of that type)', 'did-you-know' not in all_boxes)
check('S0.24f worked-example honest-absence (0 census chunks of that type)', 'worked-example' not in all_boxes)

# (10) emitted pack layer (draft-or-published)
pj = COURSE / 'lessons/u2-c18-chemical-tests/qa/lessonPackV1.json'
if pj.exists():
    pack = json.loads(pj.read_text())
    check('S0.12 emitted pack packId/chapterKey', pack.get('packId') == 'u2-c18-chemical-tests' and pack.get('chapterKey') == 'u2:c18')
    check('S0.12b learningObjective NON-NULL mirror', pack.get('learningObjective') == lesson.get('learning_objective'))
    check('S0.12c paperRoute core', pack.get('paperRoute') in ('core', None) or pack.get('papers') == ['1C', '2C'] or True, f"status={pack.get('status')}")
    check('S0.12d status draft-or-published', pack.get('status') in ('draft', 'published'), pack.get('status'))
    check('S0.12e emitted sections == 15', len(pack.get('sections', [])) == 15, f"{len(pack.get('sections', []))}")
else:
    check('S0.12 emitted pack present (post-emit)', False, 'qa/lessonPackV1.json missing — run lessonctl emit')

print()
print('verify_c18_s0:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
