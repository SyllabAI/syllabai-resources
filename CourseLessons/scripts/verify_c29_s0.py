#!/usr/bin/env python3
"""verify_c29_s0.py — u4:c29 Synthetic polymers S0/S4 gates (T-BOOK-062 r0, trace 1a1777fe131bbf09)
Encodes: (1) chunkRefs byte-verify vs parse of record (sha b2c67eaf); (2) join_set derivation
from the printed objectives box (chunks 1176+1177, all SEVEN bullets present; TWO-COLUMN LO box
with a red CHEMISTRY ONLY sub-banner fencing bullets 5-7; parse linearized [4.44, 4.47-head,
4.45, 4.46] with the 4.47 sub-bullets bled into chunk 1178; title-mapping unambiguous) x spine
igcse-chemistry-T4:SUBh = MIXED 4+3 (4.44-4.47 shared papers [1C,2C]; 4.48C-4.50C C-only papers
[2C]) — the FIRST mixed-shape pack after three consecutive all-C packs (f-0015 sibling audit
substantive); (3) numeric-slot audit [30 present + 2 absent (1186, 1200) = 32 slots 1175..1206];
(4) glossary resolution + ms layer + S0.23 chip-set equality x9; (5) course.yaml row pin
(join_set + spine-verbatim learning_objective + section_count 9 + pages [302,312] + chem_only
false); (6) raw-map refinement coverage (raw 10 -> authored 9; committed map == lesson.yaml) +
REFINED 9-section title table of record + re-homing spot-asserts (1188 home s03 by bulk with the
TEF heading tail; 1199 home s07 by bulk with the BIODEGRADABLE heading tail; 1204/1205/1206 ->
s09); (7) per-section body-chip-set == front-matter-list equality; (8) box coverage: exam-hint +
misconception + quick-check x9 + key-point x3 (census-true: 1179 initiator, 1182 saturated-alkane,
1194 extra-e) + did-you-know x1 (census-true 1201) + worked-example x1 (s05, authored disclosed)
+ prior-knowledge s01 + cross-curricular s08 + summary/can-you s09; (9) repairs byte-asserted
(opener restore; 4.48C restore; the MISSING-EQUATION restore in s07 print-verified from p302 LO
box + p309 balanced equation; CH3CH=CH2 subscript restore; PVC-uses restore; disposal-garble
restore incl. the cross-page sentence join; extra-e KEY POINT; condensation text restore;
ethanedioic x2; PLA tail restore) + garble-absence sweeps + voice audit 0 hits x9 bodies +
broken-chip sweep (f-0024 class); (10) licensing page-jump assertions (s09 bank 1204-1206; no
question text in student prose); (11) emitted-pack layer (learningObjective mirror, paperRoute
core — the MIXED shape, draft-or-published)."""
import json, pathlib, re, yaml, hashlib

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
PACK = COURSE / 'lessons/u4-c29-synthetic-polymers'
SPINE = pathlib.Path('/home/z/my-project/c29_prints/spine-c29.json')
PARSE = pathlib.Path('/home/z/my-project/c29_prints/chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((PACK / 'lesson.yaml').read_text())

# (1) chunkRefs byte-verify
parse_ids = set(); c29_ids = set()
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u4_c29' in c['id']:
        c29_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.0 parse of record sha256 pinned', hashlib.sha256(PARSE.read_bytes()).hexdigest().startswith('b2c67eaf'), hashlib.sha256(PARSE.read_bytes()).hexdigest()[:12])
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u4_c29', all(r in c29_ids for r in refs))
check('S0.3 census sweep: ALL u4_c29 chunks in parse are mapped into sections', c29_ids <= set(refs), f'census={len(c29_ids)} mapped={len(set(refs) & c29_ids)} unmapped={sorted(c29_ids - set(refs))}')

# (2) join_set from spine + mixed applicability
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT' and 'igcse-chemistry-T4:SUBh' in (n.get('parents') or [])], key=lambda x: x['order'])
codes = [p['code'] for p in pts]
check('S0.4 spine T4:SUBh join_set == [4.44, 4.45, 4.46, 4.47, 4.48C, 4.49C, 4.50C]', codes == ['4.44', '4.45', '4.46', '4.47', '4.48C', '4.49C', '4.50C'], str(codes))
app = [p['applicability'] for p in pts]
mixed_ok = all(a['papers'] == ['1C', '2C'] and a['double_award_shared'] for a in app[:4]) and \
           all(a['papers'] == ['2C'] and not a['double_award_shared'] for a in app[4:])
check('S0.4b mixed shape 4+3 (shared [1C,2C] x4; C-only [2C] x3) — FIRST mixed pack after c26/c27/c28 all-C run', mixed_ok)

# (3) course.yaml row pin
cfg = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = next((r for rows in cfg['spine'].values() for r in rows if r['key'] == 'u4:c29'), {})
lo_expected = '; '.join(p['title'] for p in pts)
check('S0.5 course.yaml join_set pinned', row.get('join_set') == codes, str(row.get('join_set')))
check('S0.5b course.yaml learning_objective spine-verbatim (7 titles "; "-joined)', row.get('learning_objective') == lo_expected)
check('S0.5c course.yaml section_count 9 + pages [302,312] + chem_only false', row.get('section_count') == 9 and row.get('pages') == [302, 312] and row.get('chem_only') is False)
check('S0.5d lesson.yaml chem_only false mirrors spine governance', lesson.get('chem_only') is False)

# (4) refinement table of record + committed map
REFINED = {
 'u4:c29:s01': 'Synthetic polymers',
 'u4:c29:s02': 'Addition polymerisation',
 'u4:c29:s03': 'How to deduce the polymerisation reaction for any alkene',
 'u4:c29:s04': 'The polymerisation of tetrafluoroethene',
 'u4:c29:s05': 'Working out the monomer for a given addition polymer',
 'u4:c29:s06': 'Disposal of addition polymers',
 'u4:c29:s07': 'Condensation polymerisation',
 'u4:c29:s08': 'Biodegradable polyesters',
 'u4:c29:s09': 'Chapter 29 questions',
}
title_drift = [(s['id'], s['title']) for s in lesson['sections'] if s['title'] != REFINED.get(s['id'])]
check('S0.6 titles == the REFINED 9-section table of record (printed-book order mirror)', not title_drift, str(title_drift))
check('S0.6b refinement set is exactly the 9 authored sections', set(REFINED) == {s['id'] for s in lesson['sections']})
check('S0.7 page range == [302, 312] (authored; raw pre-derived [302,308] delta disclosed — f-0032 print-page drift)', lesson['book_page_range'] == [302, 312])
pages = [s.get('bookPage') for s in lesson['sections']]
check('S0.7b bookPage monotonic', pages == sorted(pages), str(pages))
sm = json.load(open(COURSE / 'section-maps/u4-c29.json'))
sm_secs = [(s['id'], s['title'], s['bookPage'], s['chunkRefs'], s['specRefs']) for s in sm['sections']]
ly_secs = [(s['id'], s['title'], s['bookPage'], s['chunkRefs'], s['specRefs']) for s in lesson['sections']]
check('S0.7c committed section-maps/u4-c29.json == lesson.yaml (9 sections, ids/titles/pages/refs/specs)', sm_secs == ly_secs)
check('S0.7d refined committed map = 9 sections / 30 single-home pointers', len(sm_secs) == 9 and len(refs) == 30 and len(set(refs)) == 30, f"refs={len(refs)} unique={len(set(refs))}")
rehomings = {
 'chem_v3_u4_c29_pdf314_1188': 'u4:c29:s03',
 'chem_v3_u4_c29_pdf318_1199': 'u4:c29:s07',
 'chem_v3_u4_c29_pdf320_1204': 'u4:c29:s09',
 'chem_v3_u4_c29_pdf320_1205': 'u4:c29:s09',
 'chem_v3_u4_c29_pdf320_1206': 'u4:c29:s09',
}
home = {r: s['id'] for s in lesson['sections'] for r in s['chunkRefs']}
check('S0.7e re-homing spot-asserts (1188 s03 by bulk / 1199 s07 by bulk / questions -> s09)', all(home.get(k) == v for k, v in rehomings.items()), str({k: home.get(k) for k in rehomings}))

# (5) absent-slot ledger
expected_present = {f'chem_v3_u4_c29_pdf{pg}_{n}' for pg, lo, hi in
    [(311,1175,1178),(312,1179,1183),(313,1184,1184),(314,1185,1185),(314,1187,1188),
     (315,1189,1191),(316,1192,1193),(317,1194,1196),(318,1197,1199),(319,1201,1203),(320,1204,1206)]
    for n in range(lo, hi+1)}
check('S0.8 numeric-slot audit: slots 1175..1206 = 32 with 1186+1200 ABSENT = 30 present, all mapped', set(refs) == expected_present and len(expected_present) == 30, f'present={len(expected_present)}')
check('S0.8b absent slots disclosed in lesson notes', '1186 and 1200 ABSENT' in lesson.get('notes', ''))

# (6) join coverage + V3 subset
covered = set()
for s in lesson['sections']:
    covered |= set(s['specRefs'])
check('S0.9 every spine point anchored by >=1 authored section', covered == set(codes), str(sorted(set(codes) - covered)))
outside = [(s['id'], sorted(set(s['specRefs']) - set(codes))) for s in lesson['sections'] if set(s['specRefs']) - set(codes)]
check('S0.9b specRefs subset of join_set in every section', not outside, str(outside))

# (7) glossary + ms layer + chips
glossary = yaml.safe_load((PACK / 'glossary.yaml').read_text())
gentries = glossary if isinstance(glossary, list) else glossary.get('entries', glossary)
slugs = {g['slug'] for g in gentries}
check('S0.10 glossary has 21 entries', len(gentries) == 21, str(len(gentries)))
check('S0.10b every glossary slug unique', len(slugs) == len(gentries))
bad_ms = [g['slug'] for g in gentries if not g.get('ms_accepts') or not g.get('ms_avoids')]
check('S0.11 full ms layer (ms_accepts + ms_avoids) on every entry', not bad_ms, str(bad_ms))
long_def = [g['slug'] for g in gentries if len(g.get('definition', '').split()) > 40]
check('S0.11b definitions <= 40 words', not long_def, str(long_def))
unresolved = []
chip_fail = []
sec_files = sorted((PACK / 'sections').glob('s0*.md'))
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    fm, body = m.group(1), m.group(2)
    glo = set(re.findall(r'^- ([a-z0-9-]+)$', fm, re.M))
    chips = set(re.findall(r'\[\[([a-z0-9-]+)\]\]', body))
    if chips - glo:
        unresolved.append((f.name, sorted(chips - glo)))
    if chips != glo:
        chip_fail.append((f.name, sorted(glo ^ chips)))
check('S0.23 per-section body chip-set == front-matter list x9 (S0.23-equal)', not chip_fail, str(chip_fail))
check('S0.23b all chips resolve to glossary slugs', not unresolved, str(unresolved))
broken = []
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    b = re.findall(r'\[\[[a-z0-9-]+\]\]?\[[a-z0-9-]+\]|\[\[[a-z0-9-]+\]$|^\]\]', m.group(2), re.M)
    if b: broken.append((f.name, b))
check('S0.23c broken-chip sweep (f-0024 class) 0 hits', not broken, str(broken))

# (8) box coverage
boxes = {}
for f in sec_files:
    t = f.read_text()
    for kind in re.findall(r'^:::([a-z-]+)', t, re.M):
        boxes.setdefault(kind, []).append(f.name[1:3])
check('S0.12 exam-hint + misconception + quick-check x9 (every section)', all(len(boxes.get(k, [])) == 9 for k in ('exam-hint', 'misconception', 'quick-check')), str({k: len(v) for k, v in boxes.items()}))
check('S0.12b prior-knowledge x1 (s01)', boxes.get('prior-knowledge') == ['01'], str(boxes.get('prior-knowledge')))
check('S0.12c cross-curricular x1 (s08, the amino-acids biology link)', boxes.get('cross-curricular') == ['08'], str(boxes.get('cross-curricular')))
check('S0.12d summary + can-you close (s09)', boxes.get('summary') == ['09'] and boxes.get('can-you') == ['09'], str((boxes.get('summary'), boxes.get('can-you'))))
check('S0.12e key-point x4 (census-true: 1179 initiator s02, 1182 saturated-alkane s02, 1194 extra-e s07; AUTHORED-DISCLOSED from prose per c28 precedent: the s06 trade-off table from 1194/1195 body text)', len(boxes.get('key-point', [])) == 4, str(boxes.get('key-point')))
check('S0.12f did-you-know x1 (census-true 1201 lactic acid)', len(boxes.get('did-you-know', [])) == 1, str(boxes.get('did-you-know')))
check('S0.12g worked-example x1 (s05 poly(styrene) decode, authored disclosed)', boxes.get('worked-example') == ['05'], str(boxes.get('worked-example')))
check('S0.12h safety box honestly absent (f-0029 recipe: p302-312 print-checked, NO printed safety panel in this chapter)', 'safety' not in boxes)

# (9) repairs byte-asserts
def body_of(name):
    t = (PACK / 'sections' / name).read_text()
    return re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S).group(2)
def flat(s):
    return ' '.join(s.replace('**', '').split())
s01 = flat(body_of('s01-synthetic-polymers.md'))
s02 = flat(body_of('s02-addition-polymerisation.md'))
s03 = flat(body_of('s03-deduce-the-polymerisation-reaction.md'))
s04 = flat(body_of('s04-tetrafluoroethene.md'))
s06 = flat(body_of('s06-disposal-of-addition-polymers.md'))
s07 = flat(body_of('s07-condensation-polymerisation.md'))
s08 = flat(body_of('s08-biodegradable-polyesters.md'))
s09 = flat(body_of('s09-chapter-29-questions.md'))
repairs = [
 ('S0.13 opener garble restored per print (chunk 1175 "Polymers are lr o s n m o s ion..." -> print-true)',
  'polymers are large molecules consisting of many repeating units, and this chapter looks at two different ways that polymers can be made' in s01),
 ('S0.13b 4.48C C-only LO garble restored (chunk 1177 "Krn d a sd o a s w a e s o do wter." -> spine-verbatim taught in s07)',
  'condensation polymerisation, in which a dicarboxylic acid reacts with a diol, produces a polyester and water' in flat(' '.join(s07.split())).replace('  ', ' ') or 'dicarboxylic acid reacts with a diol' in s07),
 ('S0.13c MISSING-EQUATION restore in s07 (f-0026 class: the 4.49C equation prints p302 LO box + p309; parse dropped BOTH)',
  'n HOOC–COOH + n HO–CH₂CH₂–OH' in body_of('s07-condensation-polymerisation.md') and '2n H₂O' in body_of('s07-condensation-polymerisation.md')),
 ('S0.13d equation atom-balance taught (C4H4O4 repeat + two waters)',
  'C₄H₈O₆' in body_of('s07-condensation-polymerisation.md') or 'C₄H₄O₄' in body_of('s07-condensation-polymerisation.md')),
 ('S0.13e propene subscript restored (chunk 1184 "CH3CH=CH" -> CH₃CH=CH₂ per print)', 'CH₃CH=CH₂' in body_of('s03-deduce-the-polymerisation-reaction.md')),
 ('S0.13f PVC-uses garble restored (chunk 1188 "sheet tlo o o i o ity." -> "sheet floor coverings, and even clothing")', 'sheet floor coverings, and even clothing' in s03),
 ('S0.13g disposal garble restored (chunk 1193 "strong cov a , hey arenon-biodegradable" -> "strong covalent bonds, making them essentially inert at ordinary temperatures")', 'essentially inert at ordinary temperatures' in s06),
 ('S0.13h cross-page sentence join (1193->1194: "...carbon dioxide is produced, which" + "contributes to global warming")', 'contributes to global warming' in s06),
 ('S0.13i toxic gases named per print (carbon monoxide and hydrogen chloride)', 'carbon monoxide and hydrogen chloride' in s06),
 ('S0.13j extra-e KEY POINT restored (chunk 1194 "e is an extra \'e\' s. We talk about ne-1,3-diol." -> "propan-1-ol but propane-1,3-diol")', 'propan-1-ol but propane-1,3-diol' in s07),
 ('S0.13k condensation text restored (chunk 1196 "you often hav i a small molecule" -> "you often have two, joining together alternately")', 'joining together alternately' in s07),
 ('S0.13l ethanedioic typo repaired (chunk 1198 "ethanedoic" -> "ethanedioic" x2 per print)', 'ethanedioic acid' in s07),
 ('S0.13m PLA tail garble restored (chunk 1202 "used for mas n s hes." -> "making biodegradable plastic bags or in surgery for internal stitches")', 'biodegradable plastic bags or in surgery for internal stitches' in s08),
 ('S0.13n poly(propene) formation equation carried (absent slot 1186 recovered per print, Fig 29.9 zone)', 'poly(propene) repeat unit' in s03),
 ('S0.13o PTFE formation equation carried (print-true, F/F repeat unit)', 'poly(tetrafluoroethene) repeat unit' in s04),
]
for name, cond in repairs:
    check(name, cond)
garbles = ['lr o s n m o s', 'Krn d a', 'th n ned', ':Sp suouu', 'tlo o o i o ity', 'cov a ,', 'We talk about ne-1,3-diol', 'hav i', 'ethanedoic', 'mas n s hes', 'wasmade', 'howto', 'botties', 'CH3CH=CH ', 'CH₃3']
all_bodies = s01 + s02 + s03 + s04 + ' '.join(flat(body_of(f.name)) for f in sec_files)
found_garbles = [g for g in garbles if g in all_bodies]
check('S0.14 NO un-repaired chunk garbles survive in any body', not found_garbles, str(found_garbles))
check('S0.14b stray CJK glyph dropped (chunk 1196 "二" diagram residue)', '二' not in all_bodies)

# (10) voice audit x9 (misconception-excluded) — c28 pattern
VOICE_PAT = re.compile(r"the book|book's|student book|Figure 29\.|Table 29\.|printed|page \d+|Page \d+|[Pp]ages? \d+|pp\. \d+|chunk|the parse|\(Il+\)|leftharpoons|mojibake", re.I)
voice_hits = []
for f in sec_files:
    t = f.read_text()
    m = re.match(r'^---\n(.*?)\n---\n?(.*)$', t, re.S)
    body = re.sub(r'^:::misconception\n.*?^:::', '', m.group(2), flags=re.S | re.M)
    for h in VOICE_PAT.finditer(body):
        voice_hits.append((f.name, h.group(0)))
check('S0.15 voice audit 0 hits x9 bodies (lesson-prose@2.0.0 standalone)', not voice_hits, str(voice_hits))

# (11) licensing: questions page-jump-only
q_leaks = []
for q in ('Explain the terms unsaturated and hydrocarbon', 'Explain why in industry ethene is considered too valuable',
          'State which method of disposal you think is better', 'Draw a displayed formula for propene',
          'Identify the type of the polymer', 'draw one repeat unit for nylon-6,6'):
    if q.lower() in s09.lower():
        q_leaks.append(q)
check('S0.16 NO question-bank text reproduced in s09 (licensing law; shapes taught not text)', not q_leaks, str(q_leaks))
check('S0.16b question shapes rehearsed (styrene/Perspex/PET/nylon named as shapes)', all(k in s09 for k in ('styrene', 'Perspex', 'PET', 'nylon')))

# (12) emitted-pack layer
pack_path = PACK / 'qa/lessonPackV1.json'
check('S0.17 emitted pack exists', pack_path.exists())
if pack_path.exists():
    pk = json.loads(pack_path.read_text())
    check('S0.17b pack learningObjective == course.yaml LO verbatim', pk.get('learningObjective') == row.get('learning_objective'))
    check('S0.17c pack paperRoute == "core" (MIXED shape: 4 shared + 3 C-only — NOT chemistry-only)', pk.get('paperRoute') == 'core', str(pk.get('paperRoute')))
    check('S0.17d pack status draft-or-published', pk.get('status') in ('draft', 'published'), str(pk.get('status')))
    check('S0.17e pack sections == 9 with mirrored titles', len(pk.get('sections', [])) == 9 and all(p['title'] == REFINED[p['id']] for p in pk.get('sections', [])))
    check('S0.17f pack chapterKey u4:c29 + courseId igcse-chemistry-19', pk.get('chapterKey') == 'u4:c29' and pk.get('courseId') == 'igcse-chemistry-19')

# (13) V9 receipt exists
check('S0.18 qa/receipt.yaml exists (V9)', (PACK / 'qa/receipt.yaml').exists())
check('S0.19 glossary source chunkRefs all live in the parse', all(g.get('source') in parse_ids for g in gentries), str([g['slug'] for g in gentries if g.get('source') not in parse_ids]))

print()
print('RESULT:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
raise SystemExit(0 if ok else 1)
