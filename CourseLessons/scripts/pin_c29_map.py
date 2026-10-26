#!/usr/bin/env python3
"""pin_c29_map.py — u4:c29 Synthetic polymers S0 spine-pinning (T-BOOK-062, trace 1a1777fe131bbf09)
1. Writes the REFINED 9-section lesson.yaml (raw 10 -> authored 9 with receipt-disclosed
   re-homings mirroring the PRINTED book order; chunk census 30/30 single-home; slots
   1175..1206 = 32 with 1186 and 1200 ABSENT — image-rendered equation/diagram zones
   recovered by 300-dpi print inspection and taught as content; bookPage monotonic
   302..311; authored page range [302, 312] — delta from the pre-derived raw [302,308]
   disclosed: the condensation block prints p308-310 under a STANDALONE parse-dropped
   CHEMISTRY ONLY banner (f-0027 class), and the questions close runs across printed
   p311-312 where a second standalone CHEMISTRY ONLY banner (p311, between Q2 and Q3)
   and a second END OF CHEMISTRY ONLY banner (p312, closing the C-only questions) print
   — the parse glued Q4/Q5 into pdf320-tagged chunks while they print on pdf321/book
   p312 (page-attribution drift class, filed f-0032).
2. Pins the course.yaml u4:c29 row: join_set (spine-derived 4.44-4.47 SHARED + 4.48C-4.50C
   CHEMISTRY-ONLY = mixed 4+3 — the FIRST mixed-shape pack after three consecutive all-C
   packs c26/c27/c28; papers [1C,2C] on the shared four, [2C] on the C-suffixed three) +
   learning_objective (spine-verbatim '; '.join of T4:SUBh titles) + section_count 9 +
   pages [302, 312]. chem_only stays FALSE (spine applicability governs: four of the seven
   points are double-award-shared; the printed banners fence only the condensation block,
   the last three objectives bullets, and questions Q3-Q5).
Asserts all invariants BEFORE writing (c23-c28 pin precedent).
"""
import json, pathlib, yaml

ROOT = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons')
COURSE = ROOT / 'lessons/pearson-edexcel/international-gcse/chemistry-4ch1'
SPINE = pathlib.Path('/home/z/my-project/c29_prints/spine-c29.json')
RAW = COURSE / 'section-maps/u4-c29.json'

spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subh = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBh'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT'
              and 'igcse-chemistry-T4:SUBh' in (n.get('parents') or [])], key=lambda x: x['order'])
codes = [p['code'] for p in pts]
assert codes == ['4.44', '4.45', '4.46', '4.47', '4.48C', '4.49C', '4.50C'], codes
assert subh['title'] == 'Synthetic polymers', subh['title']
app = [p['applicability'] for p in pts]
# mixed shape: 4.44-4.47 shared papers [1C,2C]; 4.48C-4.50C chemistry-only papers [2C]
for a in app[:4]:
    assert a['papers'] == ['1C', '2C'] and a['double_award_shared'], a
for a in app[4:]:
    assert a['papers'] == ['2C'] and not a['double_award_shared'], a

# learning_objective: spine-verbatim
titles = {p['code']: p['title'] for p in pts}
assert 'addition polymer is formed by joining up many small molecules called monomers' in titles['4.44']
assert 'draw the repeat unit of an addition polymer' in titles['4.45']
assert 'deduce the structure of a monomer from the repeat unit' in titles['4.46']
assert 'problems in the disposal of addition polymers' in titles['4.47']
assert 'condensation polymerisation, in which a dicarboxylic acid reacts with a diol' in titles['4.48C']
assert 'structural and displayed formula of a polyester' in titles['4.49C']
assert 'biopolyesters, are biodegradable' in titles['4.50C']
learning_objective = '; '.join(titles[c] for c in codes)

P = 'chem_v3_u4_c29_pdf'
JOIN = codes
ALL7 = list(codes)
# printed-order mirror: s01 opener+LO (302; the LO box prints TWO-COLUMN with a red
# CHEMISTRY ONLY sub-banner fencing bullets 5-7; parse linearized [4.44, 4.47-head,
# 4.45, 4.46] then the 4.47 sub-bullets bleed into the s02 opener chunk 1178 — mapping
# by title unambiguous, all seven present) -> s02 addition polymerisation (302-303;
# poly(ethene) formation + repeat unit + initiator + LDPE/HDPE uses) -> s03 deduce the
# reaction for any alkene (304-305; propene then chloroethene/PVC; absent 1186 = the
# image-rendered Fig 29.9 poly(propene) formation-equation zone) -> s04 tetrafluoroethene
# (306; the TEF heading tail runs at the end of chunk 1188 but PRINTS on p306 — 1188
# single-home s03 by bulk, disclosed) -> s05 working out the monomer (307; poly(styrene)
# worked example) -> s06 disposal (307-308; landfill vs incineration + the advantages/
# disadvantages table; the incineration sentence crosses the p307->p308 page break and
# the parse split it across chunks 1193/1194 — joined per print) -> s07 condensation
# polymerisation (308-309; C-ONLY block opens here under the STANDALONE parse-dropped
# CHEMISTRY ONLY banner; diol + dicarboxylic acid monomers + the polyester equation,
# image-rendered and restored from the p309 print) -> s08 biodegradable polyesters
# (310; 4.50C; absent 1200 = the image-rendered Fig 29.26/29.27 zones — the biopolyester
# prose survives in 1202 with its tail garble restored per print) -> s09 questions close
# (311-312; shared Q1-Q2 then a SECOND standalone parse-dropped CHEMISTRY ONLY banner
# before Q3; Q4/Q5 print on p312 though the parse tagged their chunks pdf320 — drift
# disclosed; a second END OF CHEMISTRY ONLY closes p312).
SECTIONS = [
 ('s01', 'Synthetic polymers', 302,
  [P+'311_1175', P+'311_1176', P+'311_1177'], ALL7,
  ['polymer', 'monomer', 'addition-polymerisation', 'condensation-polymerisation', 'polyester']),
 ('s02', 'Addition polymerisation', 302,
  [P+'311_1178', P+'312_1179', P+'312_1180', P+'312_1181', P+'312_1182', P+'312_1183'],
  ['4.44', '4.45'],
  ['addition-polymerisation', 'monomer', 'polymer', 'repeat-unit', 'initiator', 'polyethene', 'saturated']),
 ('s03', 'How to deduce the polymerisation reaction for any alkene', 304,
  [P+'313_1184', P+'314_1185', P+'314_1187', P+'314_1188'], ['4.45'],
  ['polypropene', 'polychloroethene', 'plasticiser', 'repeat-unit']),
 ('s04', 'The polymerisation of tetrafluoroethene', 306,
  [P+'315_1189', P+'315_1190', P+'315_1191'], ['4.45'],
  ['ptfe', 'monomer']),
 ('s05', 'Working out the monomer for a given addition polymer', 307,
  [P+'316_1192'], ['4.46'],
  ['repeat-unit', 'monomer']),
 ('s06', 'Disposal of addition polymers', 307,
  [P+'316_1193', P+'317_1194', P+'317_1195'], ['4.47'],
  ['non-biodegradable', 'landfill', 'incineration', 'polymer']),
 ('s07', 'Condensation polymerisation', 308,
  [P+'317_1196', P+'318_1197', P+'318_1198', P+'318_1199'], ['4.48C', '4.49C'],
  ['condensation-polymerisation', 'diol', 'dicarboxylic-acid', 'polyester', 'ester-link']),
 ('s08', 'Biodegradable polyesters', 310,
  [P+'319_1201', P+'319_1202', P+'319_1203'], ['4.50C'],
  ['biopolyester', 'polylactic-acid', 'polyester']),
 ('s09', 'Chapter 29 questions', 311,
  [P+'320_1204', P+'320_1205', P+'320_1206'], ALL7,
  ['polymer', 'monomer', 'repeat-unit', 'polyester', 'condensation-polymerisation']),
]

# ---- census asserts BEFORE writing ----
rawmap = json.load(open(RAW))
assert len(rawmap['sections']) == 10, f'raw map expected 10 pre-derived sections, got {len(rawmap["sections"])}'
assert rawmap['book_page_range'] == [302, 308], rawmap['book_page_range']
assert all(s['specRefs'] == [] and s['status'] == 'todo' for s in rawmap['sections']), 'raw map not raw'
raw_refs = [r for s in rawmap['sections'] for r in s['chunkRefs']]
authored_refs = [r for s in SECTIONS for r in s[3]]
assert len(authored_refs) == 30 and len(set(authored_refs)) == 30, 'census must be 30 single-home'
assert set(raw_refs) == set(authored_refs), 'authored set must equal the raw census set (pure re-homing)'
# slot ledger: 1175..1206 = 32 slots, 1186 + 1200 absent, 30 present
expected_present = {f'{P}{pg}_{n}' for pg, lo, hi in [(311, 1175, 1178), (312, 1179, 1183), (313, 1184, 1184),
                 (314, 1185, 1185), (314, 1187, 1188), (315, 1189, 1191), (316, 1192, 1193),
                 (317, 1194, 1196), (318, 1197, 1199), (319, 1201, 1203), (320, 1204, 1206)]
                 for n in range(lo, hi + 1)}
assert set(authored_refs) == expected_present, sorted(set(authored_refs) ^ expected_present)
pages = [s[2] for s in SECTIONS]
assert pages == sorted(pages), pages
assert pages[0] == 302 and pages[-1] == 311, pages
# join_set coverage: every spine point anchored by >=1 authored section
covered = set()
for s in SECTIONS:
    covered |= set(s[4])
assert covered == set(JOIN), sorted(set(JOIN) - covered)

lesson = {
 'lesson_id': 'u4-c29-synthetic-polymers',
 'chapter_key': 'u4:c29',
 'course_id': 'chemistry-4ch1',
 'title': 'Synthetic polymers',
 'chem_only': False,
 'stage': 'S0',
 'book_page_range': [302, 312],
 'sections': [
   {'id': f'u4:c29:{sid}', 'title': title, 'bookPage': page,
    'chunkRefs': list(refs), 'specRefs': list(spec), 'glossary': list(glo), 'status': 'todo'}
   for (sid, title, page, refs, spec, glo) in SECTIONS
 ],
 'features': {k: False for k in [
   'prior_knowledge', 'cross_curricular', 'misconceptions', 'ms_vocab',
   'glossary_chips', 'quick_checks', 'summary', 'can_you']},
 'receipts': [
   {'date': '2026-10-26', 'stage': 'S4', 'sections_done': '9', 'sections_total': '9',
    'pack_status': 'draft',
    'last_agent': 'T-BOOK-062 r0 (author; trace 1a1777fe131bbf09)'},
 ],
 'notes': (
  'S0 refined spine pinned by pin_c29_map.py (T-BOOK-062 r0): raw 10 -> authored 9 sections '
  '(printed-order mirror; the three garbage raw "Write This As:" pseudo-sections dissolved into their '
  'printed host sections — they are the book mini-features before the formation equations, not section '
  'headings; BIODEGRADABLE POLYESTERS promoted to its own section on its printed heading — c28 '
  'banner-promotion precedent; questions close split, c11-c28 precedent), 30/30 census chunks '
  'single-home, NO borrower sections (every authored section owns an exclusive census home), raw '
  'superset, slots 1175..1206 = 32 with 1186 and 1200 ABSENT (1186 = the image-rendered Fig 29.9 '
  'poly(propene) formation-equation zone on p305; 1200 = the image-rendered Fig 29.26/29.27 '
  'block-diagram and lactic-acid zones on p310 — both recovered by 300-dpi print inspection and taught '
  'as content, figure-slot law; all prose survives in neighbouring chunks). join_set DERIVED at S0-L0 '
  'from the printed objectives box (chunks 1176+1177: all SEVEN bullets present; the LO box prints '
  'TWO-COLUMN — left column 4.44/4.45/4.46, right column 4.47 with its two sub-bullets — with a red '
  'CHEMISTRY ONLY sub-banner fencing bullets 5-7 inside the box; the parse linearized it as '
  '[4.44, 4.47-head, 4.45, 4.46] and bled the 4.47 sub-bullets into the s02 opener chunk 1178 with the '
  'second sub-bullet garbled to "th n ned"; mapping by title to the spine is unambiguous, NO point '
  'missing) x spine igcse-chemistry-T4:SUBh = 4.44-4.47 SHARED (papers [1C,2C], double_award_shared '
  'true) + 4.48C-4.50C CHEMISTRY-ONLY (papers [2C], double_award_shared false) = MIXED 4+3 — the '
  'FIRST mixed-shape pack after three consecutive all-C packs c26/c27/c28 and the eighth mixed overall '
  '(f-0015 sibling audit run SUBSTANTIVELY across the whole ledger: u1 all-core x7 / all-C x3; '
  'c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 mixed 7+3; c18 all-core; '
  'c19 mixed 5+3; c20 mixed 7+1; c21 mixed 2+4; c22 ALL-CORE 6+0; c23 ALL-CORE 12+0; c24 ALL-CORE '
  '4+0; c25 ALL-CORE 6+0; c26 ALL-C 0+5; c27 ALL-C 0+4; c28 ALL-C 0+6; c29 MIXED 4+3 — no '
  'mixed-shape drift). chem_only: false (spine applicability governs, never the book banner: four of '
  'the seven points are double-award-shared; the printed banners fence only the last three objectives '
  'bullets, the condensation block, and questions Q3-Q5). CHEMISTRY ONLY banner census (f-0027 class, '
  'ALL located by 300-dpi print inspection): (1) INSIDE the LO box on p302 as a red sub-banner fencing '
  'bullets 5-7 — parse-glued into chunk 1177; (2) STANDALONE on p308 between the disposal table and '
  'CONDENSATION POLYMERISATION — parse-DROPPED entirely; (3) END OF CHEMISTRY ONLY on p310 closing '
  'the C-only content — parse-glued into 1203 tail, position correct; (4) STANDALONE on p311 between '
  'Q2 and Q3 — parse-glued into 1205 head; (5) a SECOND END OF CHEMISTRY ONLY on p312 closing the '
  'C-only questions — parse-glued into 1206 tail, position correct. DISCLOSED PAGE-ATTRIBUTION DRIFT '
  '(f-0032 FILED closed in-lane, NEW class): chunks 1205/1206 carry pdf320 tags but Q4/Q5 PRINT on '
  'pdf321 = book p312 (verified by 300-dpi render of pdf321); pdf321 has NO chunk of its own and '
  'chunk 1207 (UNIT QUESTIONS) already runs on pdf322/book p313 — the parse glued the p312 question '
  'text into pdf320-tagged chunks; the authored book range is therefore [302, 312], not the raw '
  'pre-derived [302, 308] (the raw map chunkRefs are byte-identical to the parse census — the drift '
  'is print-page, not id-level; CONDENSATION chunk 1196 = pdf317 = book p308 matches the printed '
  'heading position exactly). Repairs ledger (ALL print-verified at 300 dpi, f-0028 identity gate: '
  'pdfinfo 383pp + sha256 d48020e0 PASS): opener garble chunk 1175 "Polymers are lr o s n m o s ion '
  'polymerisation..." restored per print to "Polymers are large molecules consisting of many repeating '
  'units. This chapter looks at two different ways that polymers can be made: addition polymerisation '
  'for polymers such as poly(ethene) and PVC, and condensation polymerisation for polymers such as '
  'polyester." (+ "botties" -> bottles); C-only LO bullet garble chunk 1177 "Krn d a sd o a s w a e s '
  'o do wter." restored to the 4.48C spine-verbatim statement; 4.47 sub-bullet garble in 1178 ("th n '
  'ned") restored to "the production of toxic gases when they are burned"; MISSING EQUATION restore '
  '(f-0026 class): the 4.49C ethanedioic-acid + ethane-1,2-diol equation prints in the LO box on p302 '
  'and again as the balanced equation on p309 — the parse dropped BOTH (image-rendered); restored and '
  'taught in s07 with atom-balance asserted (n C2H2O4 + n C2H6O2 -> (C4H4O4)n + 2n H2O); chunk 1184 '
  '"CH3CH=CH" lost the propene subscript 2 -> CH3CH=CH2 per print; chunk 1188 ":Sp suouu" = Fig 29.14 '
  'drawing residue (dropped) and "sheet tlo o o i o ity." restored to "sheet floor coverings, and even '
  'clothing. These polymers don\'t conduct electricity, therefore PVC can be used for electrical '
  'insulation."; chunk 1192 "wasmade"/"howto" spacing + "CHs" -> C6H5 (styryl group) per print; chunk '
  '1193 "strong cov a , hey arenon-biodegradable" restored to "strong covalent bonds, making them '
  'essentially inert at ordinary temperatures. They are non-biodegradable"; chunk 1193->1194 '
  'CROSS-CHUNK sentence join ("...carbon dioxide is produced, which" + "contributes to global '
  'warming. Toxic gases are also released, including carbon monoxide and hydrogen chloride." — the '
  'printed sentence crosses the p307->p308 page break); chunk 1194 KEY POINT garble "e is an extra '
  '\'e\' s. We talk about ne-1,3-diol." restored to "It is not a mistake, there is an extra \'e\' in '
  'each of these names. We talk about propan-1-ol but propane-1,3-diol."; chunk 1196 "you often hav i '
  'a small molecule" restored to "you often have two, joining together alternately. Each time two '
  'monomers combine, a small molecule such as water or hydrogen chloride is lost." + stray CJK glyph '
  '"二" (Fig 29.21 diagram residue) dropped; chunk 1197 DUPLICATED HINT sentence (dash-variant '
  'repeat) carried once; chunk 1198 caption typo "ethanedoic" -> "ethanedioic" x2 per print; chunk '
  '1202 tail garble "used for mas n s hes." restored to "which can be used for making biodegradable '
  'plastic bags or in surgery for internal stitches."; chunk 1190 carries the Fig 29.15 PVC photo '
  'caption mis-glued under the USES OF POLY(TETRAFLUOROETHENE) label (the photo prints top of p306 '
  'closing the PVC uses; taught in s03 PVC context, chunk 1190 single-home s04 by bulk — disclosed). '
  'Safety: the f-0029 recipe APPLIED (all eleven chapter pages p302-312 print-checked at 300 dpi) — '
  'NO printed safety panel exists in this chapter (no PRACTICAL box either): honest ABSENCE, c27 '
  'class. f-0017 print-ref strips -> in-product pointers: alkenes/C=C -> u4:c25; cracking -> u4:c23; '
  'bromine-water test -> u4:c25; ester groups/ester linkage -> u4:c28; amino acids/polypeptides '
  'extension -> biology forward pointer taught generically; no Figure/Table/page deflection in '
  'student prose (figure slots taught in words: the everyday-polymers photo strip, the ethene '
  'representations, the ball-and-stick polymerisation drawings x3, the formation equations x4, the '
  'PP recycling symbol and crates/ropes photos, the PVC-uses photo, the frying-pan photo, the '
  'landfill photo, the disposal trade-off table taught as content, the block diagrams, the '
  'biodegradable-bag photo, the lactic-acid structure). Questions bank: FIVE printed questions '
  '(Q1 ethene three-part set: terms + combustion equation + why-too-valuable-as-fuel; Q2 propene '
  'seven-part set: polymerisation term + displayed formula + three-repeat-unit chain + addition '
  'meaning + styrene equation + Perspex monomer decode + landfill-vs-incineration decision; '
  'Q3 C-only block-diagram polyester identify-and-decode; Q4 C-only Terylene/PET two-repeat-unit '
  'chain + balanced equation; Q5 C-only nylon-6,6/nylon-6,10 block-diagram pair with the amide '
  'analogy) — page-jump-only per the licensing law, shapes taught not text; the questions zone '
  'carries the second standalone CHEMISTRY ONLY banner (p311) and closes with the second END OF '
  'CHEMISTRY ONLY (p312). Pages [302,312] authored range (raw pre-derived [302,308]; the '
  'condensation block prints p308-310 and the questions close runs to printed p312 where the '
  'second END OF CHEMISTRY ONLY prints).'),
}
lp = ROOT / 'lessons/pearson-edexcel/international-gcse/chemistry-4ch1/lessons/u4-c29-synthetic-polymers/lesson.yaml'
lp.parent.mkdir(parents=True, exist_ok=True)
lp.write_text(yaml.safe_dump(lesson, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- pin course.yaml row ----
cp = COURSE / 'course.yaml'
cfg = yaml.safe_load(cp.read_text(encoding='utf-8'))
hit = False
for rows in cfg['spine'].values():
    for r in rows:
        if r['key'] == 'u4:c29':
            r['join_set'] = JOIN
            r['learning_objective'] = learning_objective
            r['section_count'] = 9
            r['pages'] = [302, 312]
            hit = True
assert hit, 'u4:c29 row not found'
cp.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- regenerate committed section map to the REFINED authored set ----
refined_map = {
    'chapter_key': 'u4:c29',
    'key_mapping': rawmap['key_mapping'],
    'book_page_range': [302, 312],
    'sections': [
        {'id': f'u4:c29:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
}
sm_path = COURSE / 'section-maps/u4-c29.json'
sm_path.write_text(json.dumps(refined_map, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('pin_c29_map: OK — lesson.yaml refined (9 sections / 30 chunks single-home / 32 slots '
      'with 1186+1200 absent), course row pinned (join_set 4.44-4.47+4.48C-4.50C MIXED 4+3, '
      'section_count 9, pages [302,312]), section-maps/u4-c29.json regenerated to the refined '
      'authored set')
