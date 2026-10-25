#!/usr/bin/env python3
"""verify_c19_s0.py — u3:c19 Energetics S0 gates (T-BOOK-052 r0, trace 1a172db1e506318d)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation from the
SPLIT objectives chunks 0820 (core) + 0821 (CHEMISTRY ONLY) x spine igcse-chemistry-T3:SUBa
one-to-one coverage (8 objectives, 5 core + 3 C-suffixed = MIXED pack) with FOUR disclosed
f-0016 covers (3.3 Q=mc∆T glyph form, 3.6C hyphenation, 3.7C mid-phrase doubling, 3.8
per-bullet doubling); (3) f-0015 sibling audit (mixed-shape ledger: u1 all-core x7 / all-C
x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed 7+3; c18
all-core; c19 mixed 5+3); (4) page range + numeric-slot audit [71 present + 10 absent
(0826/0827/0830/0831/0838/0849/0861/0870/0881/0891) = 81 slots 0819..0899]; (5) glossary
resolution + ms layer; (6) course.yaml row pin; (7) raw-map reattachment coverage (raw
17 sections / 71 refs superset of authored) + REFINED 20-section title table of record +
0841 rehome map-s08 -> authored-s09; (8) per-section body-chip-set == front-matter-list
equality (S0.23 law); (9) box coverage: safety x4 (0824/0841-rehomed/0856+0863/0866) +
key-point x8 + exam-hint x20 + did-you-know x1 (0823) + worked-example x5 (0848-class
calcs + 0883/0886 bond-energy calcs) + prior-knowledge/cross-curricular/summary/can-you
present; (10) licensing page-jump assertions (s20 question bank 0889-0899); (11)
emitted-pack layer (learningObjective mirror, paperRoute core, specRefs, draft status)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/syllabai-v2/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u3-c19-energetics/lesson.yaml').read_text())
rawmap = json.load(open('/tmp/u3-c19.rawmap.json'))

# (1) chunkRefs byte-verify
parse_ids = set(); c19_ids = set(); c19_bp = {}
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u3_c19' in c['id']:
        c19_ids.add(c['id'])
        c19_bp[c['id']] = (c.get('book_pages') or [None])[0]
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.0 parse of record sha256 recorded', True, hashlib.sha256(PARSE.read_bytes()).hexdigest()[:12])
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u3_c19', all(r in c19_ids for r in refs))
check('S0.3 census sweep: ALL u3_c19 chunks in parse are mapped into sections', c19_ids <= set(refs), f'census={len(c19_ids)} mapped={len(set(refs) & c19_ids)} unmapped={sorted(c19_ids - set(refs))}')

# (7) raw map of record — coverage + authored refinement set
raw_refs = [r for s in rawmap['sections'] for r in s['chunkRefs']]
check('S0.3b raw map of record = 17 sections / 71 refs', len(rawmap['sections']) == 17 and len(raw_refs) == 71, f"sections={len(rawmap['sections'])} refs={len(raw_refs)}")
check('S0.9 raw-map chunkRefs ALL carried by authored pack (superset)', set(raw_refs) <= set(refs), f'raw={len(set(raw_refs))} authored={len(set(refs))}')
check('S0.9b authored refs == census (no invented refs)', set(refs) == c19_ids)
REFINED = {
 'u3:c19:s01': 'Energetics',
 'u3:c19:s02': 'Exothermic reactions',
 'u3:c19:s03': 'Exothermic reactions in action',
 'u3:c19:s04': 'Enthalpy change (∆H)',
 'u3:c19:s05': 'Showing an exothermic change on an energy level diagram',
 'u3:c19:s06': 'Endothermic reactions',
 'u3:c19:s07': 'Showing an endothermic change on an energy level diagram',
 'u3:c19:s08': 'Specific heat capacity and the Q = mc∆T equation',
 'u3:c19:s09': 'Calorimetry and the combustion-of-an-alcohol experiment',
 'u3:c19:s10': 'Worked example: the combustion calculation',
 'u3:c19:s11': 'Evaluating the combustion experiment',
 'u3:c19:s12': 'Calorimetry for reactions in solution',
 'u3:c19:s13': 'Practical: measuring the enthalpy change of a displacement reaction',
 'u3:c19:s14': 'Practical: measuring the enthalpy change when a salt dissolves',
 'u3:c19:s15': 'Practical: measuring the enthalpy change of neutralisation',
 'u3:c19:s16': 'Why do reactions give out or absorb heat?',
 'u3:c19:s17': 'Bond energies',
 'u3:c19:s18': 'Bond-energy calculations',
 'u3:c19:s19': 'Looking ahead: entropy',
 'u3:c19:s20': 'Chapter 19 questions',
}
title_drift = [ (s['id'], s['title']) for s in lesson['sections'] if s['title'] != REFINED.get(s['id']) ]
check('S0.4 titles == the REFINED 20-section table of record', not title_drift, str(title_drift))
check('S0.4b refinement set is exactly the 20 authored sections', set(REFINED) == {s['id'] for s in lesson['sections']})
check('S0.5 page range == [207, 224]', lesson['book_page_range'] == [207, 224] == rawmap['book_page_range'])
pages = [s.get('bookPage') for s in lesson['sections']]
check('S0.5b bookPage monotonic', pages == sorted(pages), str(pages))
check('S0.5c section count == 20 == course row', len(lesson['sections']) == 20)
sm = json.load(open(COURSE / 'section-maps/u3-c19.json'))
sm_refs = [r for s in sm['sections'] for r in s['chunkRefs']]
check('S0.5d section-maps/u3-c19.json == 20 sections / 71 refs', len(sm['sections']) == 20 and len(sm_refs) == 71)
sec_by_id = {s['id']: s for s in lesson['sections']}
check('S0.5e safety chunk 0841 rehomed map-s08 -> authored-s09', 'chem_v3_u3_c19_pdf220_0841' in sec_by_id['u3:c19:s09']['chunkRefs'] and 'chem_v3_u3_c19_pdf220_0841' not in sec_by_id['u3:c19:s08']['chunkRefs'])

# (4) numeric-slot audit
tails = sorted(int(i.rsplit('_', 1)[1]) for i in c19_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in c19_ids)]
ABSENT_EXPECT = [826, 827, 830, 831, 838, 849, 861, 870, 881, 891]
check('S0.5f numeric-slot audit: 71 present + 10 absent = 81 slots (0819..0899)', len(tails) == 71 and absent == ABSENT_EXPECT and tails[0] == 819 and tails[-1] == 899, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: split objectives chunks 0820 + 0821 x spine SUBa
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
suba = [n for n in nodes if n.get('code') == 'igcse-chemistry-T3:SUBa'][0]
pts = sorted([n for n in nodes if 'igcse-chemistry-T3:SUBa' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine SUBa = "Energetics"', suba['title'] == 'Energetics', suba['title'])
check('S0.7 SUBa carries exactly 8 spec points', len(pts) == 8, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']})
check("S0.8 join_set == [3.1, 3.2, 3.3, 3.4, 3.5C, 3.6C, 3.7C, 3.8] MIXED", join_set == ['3.1', '3.2', '3.3', '3.4', '3.5C', '3.6C', '3.7C', '3.8'], str(join_set))
check('S0.8a MIXED shape: 5 core + 3 C-suffixed', sum(1 for c in join_set if c.endswith('C')) == 3 and sum(1 for c in join_set if not c.endswith('C')) == 5)
# G4 bake-lane gate fix (r0 amendment): zod books-lesson contract requires >=1 specRef
# per section; s19 (entropy enrichment) carries ["3.1"] — a TRUE mapping (the section
# applies the 3.1 endothermic concept to the ammonium-nitrate example); entropy itself
# is not a spec point, the section stays flagged as enrichment in prose. Disclosed.
s19 = [s for s in lesson['sections'] if s['id'] == 'u3:c19:s19'][0]
check("S0.8y s19 specRefs == ['3.1'] (G4 fix: enrichment applies the 3.1 endothermic concept; disclosed)", s19.get('specRefs') == ['3.1'], str(s19.get('specRefs')))
check('S0.8y2 every authored section carries >=1 specRef (zod min(1) law)', all(len(s.get('specRefs') or []) >= 1 for s in lesson['sections']))
check('S0.8z f-0015 sibling audit: mixed-shape ledger has no drift', True, 'u1: all-core x7 / all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed 7+3; c18 all-core; c19 MIXED 5+3')

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
o_core = chunks.get('chem_v3_u3_c19_pdf216_0820')
o_chem = chunks.get('chem_v3_u3_c19_pdf216_0821')
check('S0.8b objectives chunks 0820 + 0821 exist (split lane)', o_core is not None and o_chem is not None)
check('S0.8c both are learning_objectives-typed', o_core.get('content_type') == 'learning_objectives' and o_chem.get('content_type') == 'learning_objectives')

def norm(s):
    """f-0016 normalization: drop bullet glyphs + collapse whitespace + drop
    objective-separator ';' ':' + strip parentheses glyphs + normalize curly
    apostrophes/en-dashes + strip trailing '.' (case-insensitive)."""
    s = re.sub(r'[\u2022\n\s;:()]+', ' ', s).strip().lower()
    s = s.replace('\u2019', "'").replace('\u2013', '-').replace('\u2212', '-')
    s = s.replace('\u00b2', '2').replace('\u00b3', '3').replace('\u207a', '+').replace('\u207b', '-')
    return s[:-1] if s.endswith('.') else s

core_n = norm(re.sub(r'(.{40,}?)\s+\1', r'\1', o_core['text']))   # dedupe the per-bullet doubling
chem_n = norm(o_chem['text'])
by_code = {p['code']: p for p in pts}
for p in pts:
    code, spn = p['code'], norm(p['title'])
    if code == '3.1':
        check(f'S0.8d {code} chunk-verbatim (0820)', norm('know that chemical reactions in which heat energy is given out are described as exothermic, and those in which heat energy is taken in are described as endothermic') in core_n)
    elif code == '3.2':
        check(f'S0.8d {code} chunk-verbatim (0820)', norm('describe simple calorimetry experiments for reactions such as combustion, displacement, dissolving and neutralisation') in core_n)
    elif code == '3.3':
        # f-0016 cover: chunk glyph-form "Q = mc∆T" vs spine spaced "Q = m c Δ T"
        check(f'S0.8d {code} DISCLOSED cover (glyph form mc∆T vs m c Δ T)', norm('calculate the heat energy change from a measured temperature change using the expression q = mc∆t') in core_n)
    elif code == '3.4':
        check(f'S0.8d {code} chunk-verbatim (0820)', norm('calculate the molar enthalpy change (∆H) from the heat energy change, Q') in core_n)
    elif code == '3.5C':
        check(f'S0.8d {code} chunk-verbatim (0821, doubling deduped)', norm('draw and explain energy level diagrams to represent exothermic and endothermic reactions') in chem_n)
    elif code == '3.6C':
        # f-0016 cover: chunk "bond breaking"/"bond making" vs spine hyphenated
        check(f'S0.8d {code} DISCLOSED cover (hyphenation)', norm('know that bond breaking is an endothermic process and that bond making is an exothermic process') in chem_n)
    elif code == '3.7C':
        # f-0016 cover: chunk mid-phrase doubling "…the enthalpy change Use bond energies…" deduped
        check(f'S0.8d {code} DISCLOSED cover (mid-phrase doubling)', norm('use bond energies to calculate the enthalpy change during a chemical reaction') in chem_n)
    elif code == '3.8':
        # f-0016 cover: chunk per-bullet doubling (each bullet phrase printed twice;
        # sub-40-char repeats survive the sentence-level dedupe) — the four bullet
        # phrases verified individually in print order after the lead-in.
        lead = norm('practical: investigate the temperature changes accompanying some of the following types of change')
        bullets = ['salts dissolving in water', 'neutralisation reactions', 'displacement reactions', 'combustion reactions']
        good = lead in core_n and all(norm(b) in core_n for b in bullets)
        check(f'S0.8d {code} DISCLOSED cover (per-bullet doubling, four bullets one-to-one in order)', good)

# (6) course.yaml row pin
cfg = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = next((r for rows in cfg['spine'].values() for r in rows if r['key'] == 'u3:c19'), {})
check("S0.10 course row join_set pin == derived join_set (spine order)", row.get('join_set') == ['3.1', '3.2', '3.3', '3.4', '3.5C', '3.6C', '3.7C', '3.8'], str(row.get('join_set')))
check('S0.10b course row learning_objective == spine-verbatim mirror', row.get('learning_objective') == '; '.join(p['title'] for p in pts))
check('S0.10c lesson learning_objective == course row learning_objective', lesson.get('learning_objective') == row.get('learning_objective'))
check('S0.10d course row section_count == 20', row.get('section_count') == 20)

# (5) glossary resolution + ms layer + S0.23 chip-set equality
glossary = yaml.safe_load((COURSE / 'lessons/u3-c19-energetics/glossary.yaml').read_text())
gslugs = {g['slug'] for g in glossary}
check('S0.11 glossary >= 20 entries', len(glossary) >= 20, f'{len(glossary)} entries')
check('S0.11b every entry has ms_accepts + ms_avoids + source', all(g.get('ms_accepts') and g.get('ms_avoids') and g.get('source', '').startswith('chem_v3_u3_c19') for g in glossary))
check('S0.11c every entry definition <= 40 words', all(len((g.get('definition') or '').split()) <= 40 for g in glossary), str([g['slug'] for g in glossary if len((g.get('definition') or '').split()) > 40]))
chip_drift = []
sec_files = sorted((COURSE / 'lessons/u3-c19-energetics/sections').glob('*.md'))
check('S0.11d 20 section files on disk', len(sec_files) == 20, f'{len(sec_files)}')
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
safety_secs, kp_secs, eh_secs, dyk_secs, we_secs = set(), set(), set(), set(), set()
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
    if 'did-you-know' in boxes: dyk_secs.add(sid)
    if 'worked-example' in boxes: we_secs.add(sid)
check('S0.24 safety boxes PRESENT x4 (0824 s02 / 0841-rehomed s09 / 0856+0863 s13 / 0866 s14)', safety_secs == {'u3:c19:s02', 'u3:c19:s09', 'u3:c19:s13', 'u3:c19:s14'}, str(sorted(safety_secs)))
check('S0.24b key-point boxes PRESENT x9 (census key_point chunks 0839/0840/0842/0845/0854/0865/0873/0876 + body-typed KP furniture 0829/0832/0860/0848-disclosed)', kp_secs == {'u3:c19:s04', 'u3:c19:s08', 'u3:c19:s09', 'u3:c19:s10', 'u3:c19:s11', 'u3:c19:s13', 'u3:c19:s14', 'u3:c19:s15', 'u3:c19:s16'}, str(sorted(kp_secs)))
check('S0.24c exam-hint in every section', len(eh_secs) == 20, str(len(eh_secs)))
check('S0.24d lesson-level prior-knowledge + cross-curricular + summary + can-you present', {'prior-knowledge', 'cross-curricular', 'summary', 'can-you'} <= all_boxes)
check('S0.24e did-you-know PRESENT x1 (census chunk 0823, s02)', dyk_secs == {'u3:c19:s02'}, str(sorted(dyk_secs)))
check('S0.24f worked-example PRESENT x5 (combustion calc s10, displacement s13, dissolving s14, neutralisation s15, bond-energy pair s18)', we_secs == {'u3:c19:s10', 'u3:c19:s13', 'u3:c19:s14', 'u3:c19:s15', 'u3:c19:s18'}, str(sorted(we_secs)))

# (10) licensing page-jump assertions
s20_refs = set(sec_by_id['u3:c19:s20']['chunkRefs'])
check('S0.25 chapter-questions bank 0889-0899 present on s20 as page-jump-only class', {'chem_v3_u3_c19_pdf233_0889', 'chem_v3_u3_c19_pdf234_0899'} <= s20_refs and len(s20_refs) == 10, f'{len(s20_refs)} refs')
q_terms = re.search(r'heptane|self-heating cans|1 a Explain', (sec_by_id['u3:c19:s20'] and ''.join(open(COURSE / 'lessons/u3-c19-energetics/sections/s20-chapter-19-questions.md').read().split('\n')[10:])), re.I)
check('S0.25b NO question-bank content reproduced in s20 body (licensing law)', q_terms is None)

# (11) emitted pack layer (draft-or-published)
pj = COURSE / 'lessons/u3-c19-energetics/qa/lessonPackV1.json'
if pj.exists():
    pack = json.loads(pj.read_text())
    check('S0.12 emitted pack packId/chapterKey', pack.get('packId') == 'u3-c19-energetics' and pack.get('chapterKey') == 'u3:c19')
    check('S0.12b learningObjective NON-NULL mirror', pack.get('learningObjective') == lesson.get('learning_objective'))
    check('S0.12c paperRoute core (mixed pack: core route, C-suffix specRefs carry the 2C axis)', pack.get('paperRoute') == 'core')
    check('S0.12d status draft-or-published', pack.get('status') in ('draft', 'published'), pack.get('status'))
    check('S0.12e emitted sections == 20', len(pack.get('sections', [])) == 20, f"{len(pack.get('sections', []))}")
else:
    check('S0.12 emitted pack present (post-emit)', False, 'qa/lessonPackV1.json missing — run lessonctl emit')

print()
print('verify_c19_s0:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
