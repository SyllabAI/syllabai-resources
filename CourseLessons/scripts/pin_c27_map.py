#!/usr/bin/env python3
"""pin_c27_map.py — u4:c27 Carboxylic acids S0 spine-pinning (T-BOOK-060, trace 1a1751c58a79c659)
1. Writes the REFINED 7-section lesson.yaml (raw 5 -> authored 7 with receipt-disclosed
   re-homings; chunk census 14/14 single-home; slots 1142..1156 = 15 with 1147 absent —
   the image-rendered p294 figure zone (Fig 27.3 photograph per position between the
   banner/caption chunk 1146 and Table 27.1 chunk 1148) taught in words; bookPage
   monotonic 293..295; authored page range [293,296] — delta from the pre-derived raw
   [293,295] disclosed: the questions close runs to printed p296 where END OF CHEMISTRY
   ONLY also prints).
2. Pins the course.yaml u4:c27 row: join_set (spine-derived 4.34C-4.37C ALL CHEMISTRY-ONLY
   0+4 — the SECOND consecutive all-C pack after c26, sixth overall) + learning_objective
   (spine-verbatim '; '.join of T4:SUBf titles — all 4 spine titles; the 4.34C spine title
   ends at "the functional group" with the group identity carried by the spec's DRAWING
   (the carboxyl group, -COOH) — spine-canonical pin carried as-is and disclosed as the
   f-0016 cover; the chunk renders the group garbled as "-CoOH" — l/I glyph class repaired
   to -COOH throughout) + section_count 7 + pages [293, 296]. chem_only stays true (spine
   applicability governs; the printed CHEMISTRY ONLY banner sits ABOVE the chapter heading
   on p293 and END OF CHEMISTRY ONLY closes p296 — whole-chapter block, f-0027 locator law).
Asserts all invariants BEFORE writing (c23/c24/c25/c26 pin precedent).
"""
import json, pathlib, yaml

ROOT = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons')
COURSE = ROOT / 'lessons/pearson-edexcel/international-gcse/chemistry-4ch1'
SPINE = pathlib.Path('/tmp/spine-c27.json')
RAW = COURSE / 'section-maps/u4-c27.json'
PARSE = pathlib.Path('/tmp/chunks_v3.jsonl')

spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subf = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBf'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT'
              and 'igcse-chemistry-T4:SUBf' in (n.get('parents') or [])], key=lambda x: x['order'])
codes = [p['code'] for p in pts]
assert codes == ['4.34C', '4.35C', '4.36C', '4.37C'], codes
assert subf['title'] == 'Carboxylic acids', subf['title']
app = [p['applicability'] for p in pts]
assert all(a['papers'] == ['2C'] and not a['double_award_shared'] for a in app), 'ALL-C expected'

# learning_objective: spine-verbatim
titles = {p['code']: p['title'] for p in pts}
assert 'functional group' in titles['4.34C'], titles['4.34C']
assert 'unbranched-chain carboxylic acids' in titles['4.35C'] and 'up to four carbon atoms' in titles['4.35C'], titles['4.35C']
assert 'metals and metal carbonates' in titles['4.36C'], titles['4.36C']
assert 'vinegar is an aqueous solution containing ethanoic acid' in titles['4.37C'], titles['4.37C']
learning_objective = '; '.join(titles[c] for c in codes)

P = 'chem_v3_u4_c27_pdf'
JOIN = codes
ALL4 = list(codes)
SECTIONS = [
 ('s01', 'Carboxylic acids', 293,
  [P+'302_1142', P+'302_1143'], ALL4,
  ['carboxylic-acid', 'functional-group', 'ethanoic-acid', 'vinegar']),
 ('s02', 'Drawing and naming the carboxylic acids', 294,
  [P+'303_1144', P+'303_1145', P+'303_1146', P+'303_1148', P+'303_1149'],
  ['4.34C', '4.35C'],
  ['molecular-formula', 'structural-formula', 'displayed-formula', 'methanoic-acid', 'homologous-series']),
 ('s03', 'Acid properties of the carboxylic acids', 294,
  [P+'303_1150'], ['4.36C'],
  ['weak-acid', 'ethanoic-acid']),
 ('s04', 'Reaction with metals', 294,
  [P+'303_1150', P+'304_1151', P+'304_1152'], ['4.36C'],
  ['salt', 'ethanoate-ion', 'reactivity-series', 'ionic-compound']),
 ('s05', 'Weak and strong acids', 295,
  [P+'304_1153'], ['4.36C'],
  ['strong-acid', 'weak-acid', 'dissociation']),
 ('s06', 'Reaction with carbonates', 295,
  [P+'304_1153'], ['4.36C'],
  ['metal-carbonate', 'salt', 'ethanoate-ion']),
 ('s07', 'Chapter 27 questions', 295,
  [P+'304_1154', P+'305_1155', P+'305_1156'], ALL4,
  ['carboxylic-acid', 'ethanoic-acid', 'weak-acid', 'ethanoate-ion', 'displayed-formula', 'vinegar']),
]

# ---- invariants BEFORE writing ----
rawmap = json.load(open(RAW))
if len(rawmap['sections']) != 5:
    # the committed map was already refined by the r0 run — re-derive the raw map
    # of record fresh (S0.8y byte-equality was asserted at r0; re-derivation keeps the
    # script re-runnable at r1+)
    import subprocess, tempfile
    tmp = tempfile.NamedTemporaryFile(suffix='.json', delete=False).name
    subprocess.run(['python3', str(ROOT / 'scripts/section_map.py'), '--parsed', str(PARSE),
                    '--chapter', 'u4:c27', '--out', tmp], check=True, capture_output=True)
    rawmap = json.load(open(tmp))
    assert len(rawmap['sections']) == 5, f're-derived raw != 5 sections: {len(rawmap["sections"])}'
raw_refs = [r for s in rawmap['sections'] for r in s['chunkRefs']]
authored_refs = [r for s in SECTIONS for r in s[3]]
assert len(rawmap['sections']) == 5, len(rawmap['sections'])
assert set(raw_refs) <= set(authored_refs), 'raw not subset of authored'
census = set()
for line in open(PARSE, encoding='utf-8'):
    c = json.loads(line)
    if c.get('unit_no') == 4 and c.get('chapter_no') == 27:
        census.add(c['id'])
assert len(census) == 14, len(census)
assert set(authored_refs) == census, 'authored != census'
# single-home law with the r1 DISCLOSED-shared-pointer exception: s03 lists 1150 and s06
# lists 1153 as PROVENANCE POINTERS to the split-source chunks they teach from (the contract
# honest-empty law requires >=1 chunkRef per section) — 15 pointers, 14 unique, the two
# duplicates shared with s04 (1150) and s05 (1153); exclusive census homes unchanged
assert len(authored_refs) == 16 and len(set(authored_refs)) == 14, 'shared-pointer shape changed'
shared = [c for c in set(authored_refs) if authored_refs.count(c) > 1]
assert set(shared) == {P+'303_1150', P+'304_1153'}, f'unexpected shared pointers: {shared}'
# the EXCLUSIVE census home of each shared chunk (first section listing it in the refined table
# is the s04/s05 bulk home; s03/s06 are the borrower sections)
def census_home(cid):
    return next(s[0] for s in SECTIONS if cid in s[3] and s[0] not in ('s03', 's06'))
assert census_home(P+'303_1150') == 's04' and census_home(P+'304_1153') == 's05'
# absent slot: chapter's global sequence 1142..1156 = 15 numbers, 1147 dropped by the parse.
# Position: between 1146 (REACTION WITH METALS banner + Fig 27.3 caption + DRAWING AND
# NAMING heading) and 1148 (Table 27.1) on printed p294 — the image-rendered p294 figure
# zone (Fig 27.3 photograph per position; page OCR of the full page shows no further
# uncaptured text object in that zone). Taught in words in s04 (photo) — figure-slot law.
suffixes = {int(c.rsplit('_', 1)[1]) for c in census}
assert suffixes == set(range(1142, 1157)) - {1147}, sorted(suffixes ^ set(range(1142, 1157)))
assert all(c.startswith(P) for c in census), 'unexpected id prefix in census'

# raw re-homing spot-asserts (receipt-disclosed)
def home(cid):
    # EXCLUSIVE census home (r1 law): skip the two disclosed borrower sections (s03/s06)
    # whose chunkRefs entries are provenance pointers to their split-source chunks
    return next(s[0] for s in SECTIONS if cid in s[3] and s[0] not in ('s03', 's06'))
assert home(P+'302_1142') == 's01' and home(P+'302_1143') == 's01', 'opener + LO box (2-col interleave deduped) -> s01'
assert home(P+'303_1144') == 's02', 'displayed-formula HINT + Fig 27.2 -> s02 (prints p294 beside the drawing section)'
assert home(P+'303_1145') == 's02', 'naming KEY POINT (count TOTAL carbons incl. -COOH) -> s02'
assert home(P+'303_1146') == 's02', '1146 home s02 by bulk (DRAWING AND NAMING heading + Table 27.1 intro; REACTION WITH METALS banner head + Fig 27.3 caption taught s04 — parse read the left margin first, c24 reading-order precedent)'
assert home(P+'303_1148') == 's02', 'Table 27.1 (linearized displayed-formula column garble, taught in words) -> s02'
assert home(P+'303_1149') == 's02', '1149 duplicate table garble -> s02 (deduped, no content loss)'
assert home(P+'303_1150') == 's04', '1150 home s04 by bulk (ACID PROPERTIES heading + weak-acid head taught s03; metals prose + Mg equation + ionic head home s04)'
assert home(P+'304_1151') == 's04', '1151 ionic-explanation tail home s04 (glued CHAPTER QUESTIONS banner is p295 furniture — stripped, the bank prints p295-296)'
assert home(P+'304_1152') == 's04', 'Fig 27.4 ethanoate ion + other metals + zinc ethanoate -> s04'
assert home(P+'304_1153') == 's05', '1153 home s05 by bulk (EXTENSION weak/strong box; REACTION WITH CARBONATES mid taught s06 — printed arrow-banner DROPPED by the parse, promoted to authored s06; Q1 tail taught s07)'
assert home(P+'304_1154') == 's07', 'Q2 + Q3 + Q4 stem -> s07 (questions close, c11-c26 precedent)'
assert home(P+'305_1155') == 's07' and home(P+'305_1156') == 's07', 'Q2 tick-table + Q4 equation frame -> s07'

pages = [s[2] for s in SECTIONS]
assert pages == sorted(pages), pages
assert pages[0] == 293 and pages[-1] == 295, pages

# join_set coverage: every spine point anchored by >=1 authored section
anchored = {c for s in SECTIONS for c in s[4]}
assert set(codes) <= anchored, f'spine points uncovered: {set(codes) - anchored}'

# ---- write lesson.yaml (refined) ----
lesson = {
    'lesson_id': 'u4-c27-carboxylic-acids',
    'chapter_key': 'u4:c27',
    'course_id': 'chemistry-4ch1',
    'title': 'Carboxylic acids',
    'chem_only': True,
    'stage': 'S0',
    'book_page_range': [293, 296],
    'sections': [
        {'id': f'u4:c27:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'glossary': list(glo), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
    'features': {k: False for k in [
        'prior_knowledge', 'cross_curricular', 'misconceptions',
        'ms_vocab', 'glossary_chips', 'quick_checks', 'summary', 'can_you']},
    'receipts': [],
    'notes': ('S0 refined spine pinned by pin_c27_map.py (T-BOOK-060 r0): raw 5 -> authored '
              '7 sections (printed-order mirror; questions close split, c11-c26 precedent), '
              '14/14 census chunks single-home, raw superset, slots 1142..1156 = 15 with 1147 '
              'absent (image-rendered p294 figure zone — Fig 27.3 photograph per position; '
              'taught in words, figure-slot law); join_set DERIVED at S0-L0 from the printed '
              'objectives box (chunk 1143: all FOUR bullets present but interleaved with the '
              'chapter intro prose by the parse — the c26 glue class with NO point missing; '
              'the LO box prints TWO-COLUMN, the parse linearized it mid-list) x spine '
              'igcse-chemistry-T4:SUBf = 4.34C-4.37C ALL CHEMISTRY-ONLY 0+4 (papers [2C]; '
              'double_award_shared false) — the SECOND consecutive all-C pack after c26 and '
              'the sixth overall (f-0015 sibling audit run SUBSTANTIVELY: u1 all-core x7 / '
              'all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 '
              'mixed 7+3; c18 all-core; c19 mixed 5+3; c20 mixed 7+1; c21 mixed 2+4; c22 '
              'ALL-CORE 6+0; c23 ALL-CORE 12+0; c24 ALL-CORE 4+0; c25 ALL-CORE 6+0; c26 ALL-C '
              '0+5; c27 ALL-C 0+4 — no mixed-shape drift). chem_only: true (spine '
              'applicability governs; the printed CHEMISTRY ONLY banner sits ABOVE the '
              'chapter heading on p293 — f-0027 class banner, located by page OCR since the '
              'parse dropped the standalone banner chunk — and END OF CHEMISTRY ONLY closes '
              'p296: whole-chapter block; BOTH banner lines are parse-absent). DISCLOSED '
              'f-0016 cover (spine-canonical pin, spine node igcse-chemistry-T4:SUBf): the '
              '4.34C spine title ends at "the functional group" with the group identity '
              'carried by the spec DRAWING (the carboxyl group -COOH) — taught in s01/s02; '
              'the chunk renders the group garbled as "-CoOH" — l/I glyph class repaired to '
              '-COOH throughout. Raw map verified byte-equal against a fresh section_map.py '
              'derivation BEFORE refinement (5 sections, pages [293,295], parse sha b2c67eaf '
              're-verified post-Wave-10); refined with receipt-disclosed re-homings mirroring '
              'the PRINTED book order: 1144/1145 raw-s01 -> s02 (HINT + KEY POINT print p294 '
              'beside the drawing section), 1146 home s02 by bulk (DRAWING AND NAMING tail; '
              'the REACTION WITH METALS marginal arrow-banner head + Fig 27.3 caption taught '
              's04 — the parse read the left margin first, c24 reading-order precedent), '
              '1150 home s04 by bulk (ACID PROPERTIES head + weak-acid prose taught s03), '
              '1151 home s04 (glued CHAPTER QUESTIONS banner is p295 furniture, stripped), '
              '1153 home s05 by bulk (EXTENSION weak/strong box; the REACTION WITH CARBONATES '
              'marginal arrow-banner mid taught s06 — SECOND printed banner DROPPED by the '
              'parse, promoted to authored s06 like c26 ETHANOL BURNS IN AIR; Q1 tail taught '
              's07), 1154/1155/1156 -> s07 (questions close). s03 + s06 are authored:true '
              'sections taught from disclosed head/mid splits (no census home of their own). '
              'THREE equations of record carried with in-chunk repairs (print-verified at '
              '300 dpi, f-0028 identity gate applied — pdfinfo 383pp + sha256 d48020e0): '
              'Mg(s) + 2CH3COOH(aq) -> (CH3COO)2Mg(aq) + H2(g) (chunk garbles "2CH3COH" and '
              '"(CH3CO)2Mg" repaired per the printed equation + the Zn/Ca analogues), '
              'Na2CO3(s) + 2CH3COOH(aq) -> 2CH3COONa(aq) + CO2(g) + H2O(l) and 2CH3COOH(aq) + '
              'CaCO3(s) -> (CH3COO)2Ca(aq) + CO2(g) + H2O(l) (flat-digit subscripts repaired); '
              'all three atom-balanced; zinc ethanoate (CH3COO)2Zn and the ethanoate-ion '
              'structure taught in words (Fig 27.4 slot); the extension ratio "About 1 in ~75" '
              'is PRINT-TRUE (parse + OCR + 300-dpi crop all agree) — taught as "about 1 in '
              'every 75". NO absent-equation restores needed (1147 is a photograph, not an '
              'equation object). f-0017 print-ref strips -> in-product pointers: Chapter 26 '
              'pages 289-290 oxidation reminder -> u4:c26 (Sections 4-5); metals-react-with-'
              'acids rule (book ch17 p174) -> u2:c14/u2:c16; carbonates-react-with-acids rule '
              '(book ch17 p177) -> u2:c16; no Figure/Table/page deflection in student prose '
              '(figure slots x4 taught in words: the nettle photo, the functional-group '
              'drawing, the magnesium-reaction photo, the ethanoate-ion structure; Table 27.1 '
              'taught as content). Safety: f-0029 recipe APPLIED (all four experiment-bearing '
              'pages p293-296 OCR-checked) — NO printed safety panel exists in this chapter '
              'and 0 safety census chunks: honest absence, disclosed. Questions bank: FOUR '
              'printed questions (Q1 draw/name, Q2 functional-group tick-table with skill '
              'chips, Q3 propan-1-ol oxidation cross-chapter callback to the alcohols, Q4 '
              'vinegar + sodium hydrogencarbonate balance frame) — page-jump-only per the '
              'licensing law, shapes taught not text; the glued CHAPTER QUESTIONS heading in '
              '1151 and the Q1-text tail in 1153 are the parse scrambling the bank assembly. '
              'Pages [293,296] authored range (raw pre-derived [293,295]; questions close '
              'runs to printed p296 where END OF CHEMISTRY ONLY also prints).'),
}
lp = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/'
                  'international-gcse/chemistry-4ch1/lessons/u4-c27-carboxylic-acids/lesson.yaml')
lp.parent.mkdir(parents=True, exist_ok=True)
lp.write_text(yaml.safe_dump(lesson, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- pin course.yaml row ----
cp = COURSE / 'course.yaml'
cfg = yaml.safe_load(cp.read_text(encoding='utf-8'))
hit = False
for rows in cfg['spine'].values():
    for r in rows:
        if r['key'] == 'u4:c27':
            r['join_set'] = JOIN
            r['learning_objective'] = learning_objective
            r['section_count'] = 7
            r['pages'] = [293, 296]
            hit = True
assert hit, 'u4:c27 row not found'
cp.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- regenerate committed section map to the REFINED authored set ----
refined_map = {
    'chapter_key': 'u4:c27',
    'key_mapping': rawmap['key_mapping'],
    'book_page_range': [293, 296],
    'sections': [
        {'id': f'u4:c27:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
}
sm_path = COURSE / 'section-maps/u4-c27.json'
sm_path.write_text(json.dumps(refined_map, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('pin_c27_map: OK — lesson.yaml refined (7 sections / 14 chunks single-home / 15 slots '
      'with 1147 absent), course row pinned (join_set 4.34C-4.37C ALL-C 0+4, section_count 7, '
      'pages [293,296]), section-maps/u4-c27.json regenerated to the refined authored set')
