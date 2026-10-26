#!/usr/bin/env python3
"""pin_c28_map.py — u4:c28 Esters S0 spine-pinning (T-BOOK-061, trace 1a177472e66eb2e5)
1. Writes the REFINED 6-section lesson.yaml (raw 4 -> authored 6 with receipt-disclosed
   re-homings mirroring the PRINTED book order; chunk census 17/17 single-home; slots
   1157..1174 = 18 with 1165 ABSENT — the image-rendered p299 Table 28.1 zone (nine-ester
   displayed-formula grid per position between the KEY POINT chunk 1164 and the HINT chunk
   1166) taught as content; bookPage monotonic 297..300; authored page range [297, 301] —
   delta from the pre-derived raw [297,299] disclosed: the practical box prints p300 (the
   parse kept it under the USES heading run) and the questions close runs to printed p301
   where END OF CHEMISTRY ONLY also prints).
2. Pins the course.yaml u4:c28 row: join_set (spine-derived 4.38C-4.43C ALL CHEMISTRY-ONLY
   0+6 — the THIRD consecutive all-C pack after c26 0+5 and c27 0+4, seventh overall) +
   learning_objective (spine-verbatim '; '.join of T4:SUBg titles) + section_count 6 +
   pages [297, 301]. chem_only stays true (spine applicability governs; the printed
   CHEMISTRY ONLY banner sits ABOVE the chapter heading on p297 — located by page OCR +
   300-dpi image inspection since the parse dropped the standalone banner chunk, f-0027
   locator law — and END OF CHEMISTRY ONLY closes p301: whole-chapter block).
Asserts all invariants BEFORE writing (c23-c27 pin precedent).
"""
import json, pathlib, yaml

ROOT = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons')
COURSE = ROOT / 'lessons/pearson-edexcel/international-gcse/chemistry-4ch1'
SPINE = pathlib.Path('/tmp/spine-c28.json')
RAW = COURSE / 'section-maps/u4-c28.json'
PARSE = pathlib.Path('/tmp/chunks_v3.jsonl')

spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subg = [n for n in nodes if n.get('code') == 'igcse-chemistry-T4:SUBg'][0]
pts = sorted([n for n in nodes if n.get('family') == 'SPEC_POINT'
              and 'igcse-chemistry-T4:SUBg' in (n.get('parents') or [])], key=lambda x: x['order'])
codes = [p['code'] for p in pts]
assert codes == ['4.38C', '4.39C', '4.40C', '4.41C', '4.42C', '4.43C'], codes
assert subg['title'] == 'Esters', subg['title']
app = [p['applicability'] for p in pts]
assert all(a['papers'] == ['2C'] and not a['double_award_shared'] for a in app), 'ALL-C expected'

# learning_objective: spine-verbatim
titles = {p['code']: p['title'] for p in pts}
assert 'esters contain the functional group' in titles['4.38C'], titles['4.38C']
assert 'ethyl ethanoate is the ester produced' in titles['4.39C'], titles['4.39C']
assert 'structural and displayed formulae of ethyl ethanoate' in titles['4.40C'], titles['4.40C']
assert 'given the name or formula of the alcohol and carboxylic acid' in titles['4.41C'], titles['4.41C']
assert 'volatile compounds with distinctive smells' in titles['4.42C'], titles['4.42C']
assert 'practical: prepare a sample of an ester' in titles['4.43C'], titles['4.43C']
learning_objective = '; '.join(titles[c] for c in codes)

P = 'chem_v3_u4_c28_pdf'
JOIN = codes
ALL6 = list(codes)
# printed-order mirror: s01 opener+LO (297) -> s02 making (298, DYK re-homed by print
# position) -> s03 drawing/naming (298-299; EXTENSION 1160 + KEY POINT 1161 re-homed by
# print position) -> s04 uses (299-300; solubility EXTENSION 1170 home by bulk) ->
# s05 practical (300; printed PRACTICAL heading promoted — safety 1169 prints beside it)
# -> s06 questions close (301).
SECTIONS = [
 ('s01', 'Esters', 297,
  [P+'306_1157', P+'306_1158'], ['4.38C', '4.42C'],
  ['ester', 'functional-group', 'carboxylic-acid', 'alcohol']),
 ('s02', 'Making a simple ester: ethyl ethanoate', 298,
  [P+'307_1162', P+'307_1159'], ['4.39C'],
  ['esterification', 'condensation-reaction', 'catalyst', 'glacial-ethanoic-acid',
   'reversible-reaction', 'ethyl-ethanoate']),
 ('s03', 'Drawing and naming esters', 298,
  [P+'307_1163', P+'307_1160', P+'307_1161', P+'308_1164', P+'308_1166', P+'308_1167'],
  ['4.40C', '4.41C'],
  ['structural-formula', 'displayed-formula', 'alkyl-group', 'alkanoate']),
 ('s04', 'Uses of esters', 299,
  [P+'308_1168', P+'309_1170'], ['4.42C'],
  ['volatile', 'hydrogen-bond', 'solvent']),
 ('s05', 'Making and testing the smell of some esters in the lab', 300,
  [P+'309_1169', P+'309_1171', P+'309_1172'], ['4.43C'],
  ['sodium-carbonate']),
 ('s06', 'Chapter 28 questions', 301,
  [P+'310_1173', P+'310_1174'], ALL6,
  ['ester', 'ethyl-ethanoate', 'displayed-formula', 'esterification']),
]

# ---- invariants BEFORE writing ----
rawmap = json.load(open(RAW))
assert len(rawmap['sections']) == 4, len(rawmap['sections'])
raw_refs = [r for s in rawmap['sections'] for r in s['chunkRefs']]
authored_refs = [r for s in SECTIONS for r in s[3]]
assert set(raw_refs) <= set(authored_refs), 'raw not subset of authored'
census = set()
for line in open(PARSE, encoding='utf-8'):
    c = json.loads(line)
    if c.get('unit_no') == 4 and c.get('chapter_no') == 28:
        census.add(c['id'])
assert len(census) == 17, len(census)
assert set(authored_refs) == census, 'authored != census'
# single-home law: every chunk exactly one census home (no borrower sections this lane —
# every authored section owns at least one exclusive census chunk)
assert len(authored_refs) == 17 and len(set(authored_refs)) == 17, 'single-home shape changed'
def home(cid):
    return next(s[0] for s in SECTIONS if cid in s[3])
# raw re-homing spot-asserts (receipt-disclosed; print positions from the 300-dpi OCR pass)
assert home(P+'306_1157') == 's01' and home(P+'306_1158') == 's01', 'opener + LO box -> s01'
assert home(P+'307_1159') == 's02', 'nail-polish DYK prints p298 left margin beside MAKING -> s02 (raw s01)'
assert home(P+'307_1160') == 's03', 'EXTENSION H/OH detail prints p298 margin beside Fig 28.2 formation -> s03 (raw s01)'
assert home(P+'307_1161') == 's03', "KEY POINT 'oate' naming rule prints p298-299 beside Fig 28.3 -> s03 (raw s01)"
assert home(P+'307_1162') == 's02', 'MAKING bulk (equation + catalyst/conditions + esterification + equilibrium) -> s02'
assert home(P+'307_1163') == 's03', 'DRAWING AND NAMING bulk (formation method + two-ways-round + Table 28.1 intro) -> s03'
assert home(P+'308_1164') == 's03', 'TWO KEY POINTs (colours + which-bond) print p299 margin beside Table 28.1 -> s03 (raw s03)'
assert home(P+'308_1166') == 's03', "HINT yl/oate decode prints p299 margin -> s03"
assert home(P+'308_1167') == 's03', 'DYK fruity-smell + reverse-method prose + Fig 28.4 glue -> s03 (raw s03; glue split in prose, DYK box)'
assert home(P+'308_1168') == 's04', 'USES bulk -> s04'
assert home(P+'309_1169') == 's05', 'Safety Note prints p300 left margin directly beside the PRACTICAL box -> s05 (raw s04; parse kept it under the USES heading run)'
assert home(P+'309_1170') == 's04', 'EXTENSION solubility prints p300 margin above the practical heading -> s04 by bulk (uses context)'
assert home(P+'309_1171') == 's05', 'PRACTICAL bulk (apparatus + steps 1-7) -> s05'
assert home(P+'309_1172') == 's05', 'PRACTICAL repeat step + Fig 28.6 caption -> s05'
assert home(P+'310_1173') == 's06' and home(P+'310_1174') == 's06', 'questions close -> s06'
# absent slot: chapter's global sequence 1157..1174 = 18 numbers, 1165 dropped by the parse.
# Position: between 1164 (KEY POINTs, p299 margin) and 1166 (HINT, p299 margin) on printed
# p299 — the image-rendered Table 28.1 nine-ester grid (recovered by 300-dpi OCR and taught
# as content in s03; the book prints the caption "Table 28.1 Examples of esters" above it).
suffixes = {int(c.rsplit('_', 1)[1]) for c in census}
assert suffixes == set(range(1157, 1175)) - {1165}, sorted(suffixes ^ set(range(1157, 1175)))
assert all(c.startswith(P) for c in census), 'unexpected id prefix in census'

pages = [s[2] for s in SECTIONS]
assert pages == sorted(pages), pages
assert pages[0] == 297 and pages[-1] == 301, pages

# join_set coverage: every spine point anchored by >=1 authored section
anchored = {c for s in SECTIONS for c in s[4]}
assert set(codes) <= anchored, f'spine points uncovered: {set(codes) - anchored}'

# ---- write lesson.yaml (refined) ----
lesson = {
    'lesson_id': 'u4-c28-esters',
    'chapter_key': 'u4:c28',
    'course_id': 'chemistry-4ch1',
    'title': 'Esters',
    'chem_only': True,
    'stage': 'S0',
    'book_page_range': [297, 301],
    'sections': [
        {'id': f'u4:c28:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'glossary': list(glo), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
    'features': {k: False for k in [
        'prior_knowledge', 'cross_curricular', 'misconceptions',
        'ms_vocab', 'glossary_chips', 'quick_checks', 'summary', 'can_you']},
    'receipts': [],
    'notes': ('S0 refined spine pinned by pin_c28_map.py (T-BOOK-061 r0): raw 4 -> authored '
              '6 sections (printed-order mirror; the practical box promoted from the USES '
              'heading run to its own section on its printed PRACTICAL heading — c26/c27 '
              'banner-promotion precedent; questions close split, c11-c27 precedent), 17/17 '
              'census chunks single-home (no borrower sections — every authored section owns '
              'an exclusive census home, the c27 shared-pointer class not needed), raw '
              'superset, slots 1157..1174 = 18 with 1165 ABSENT (image-rendered p299 Table '
              '28.1 nine-ester grid per position between KEY POINT 1164 and HINT 1166; '
              'recovered by 300-dpi OCR and taught as content, figure-slot law). join_set '
              'DERIVED at S0-L0 from the printed objectives box (chunk 1158: all SIX bullets '
              'present; the LO box prints TWO-COLUMN — left column 4.38C/4.39C/4.40C, right '
              'column 4.41C/4.42C/4.43C — and the parse linearized it with the third/fifth '
              'bullets transposed [4.41C read before 4.40C]; mapping by title to the spine '
              'is unambiguous, NO point missing) x spine igcse-chemistry-T4:SUBg = 4.38C-'
              '4.43C ALL CHEMISTRY-ONLY 0+6 (papers [2C]; double_award_shared false on all '
              'six) — the THIRD consecutive all-C pack after c26 0+5 and c27 0+4 and the '
              'seventh overall (f-0015 sibling audit run SUBSTANTIVELY: u1 all-core x7 / '
              'all-C x3; c11/c12 mixed 3+1; c13/c14 all-core; c15 all-C; c16 mixed 5+1; c17 '
              'mixed 7+3; c18 all-core; c19 mixed 5+3; c20 mixed 7+1; c21 mixed 2+4; c22 '
              'ALL-CORE 6+0; c23 ALL-CORE 12+0; c24 ALL-CORE 4+0; c25 ALL-CORE 6+0; c26 '
              'ALL-C 0+5; c27 ALL-C 0+4; c28 ALL-C 0+6 — no mixed-shape drift). chem_only: '
              'true (spine applicability governs; the printed CHEMISTRY ONLY banner sits '
              'ABOVE the chapter heading on p297 — f-0027 class banner, located by page OCR '
              '+ 300-dpi image inspection since the parse dropped the standalone banner '
              'chunk — and END OF CHEMISTRY ONLY closes p301: whole-chapter block; BOTH '
              'banner lines are parse-absent). DISCLOSED f-0016 cover (spine-canonical pin, '
              'spine node igcse-chemistry-T4:SUBg): the 4.38C spine title ends at "the '
              'functional group" with the group identity carried by the spec DRAWING (the '
              'ester group, printed in the objectives bullet as C=O joined through —C—O—, '
              'condensed -COO-) — taught in s01/s03; the chunk renders the condensed form '
              'garbled as "-Coo-" — l/I glyph class repaired to -COO- throughout. Raw map '
              'verified byte-equal against the committed pre-derived section-maps/u4-c28.json '
              '(4 sections, pages [297,299], parse sha b2c67eaf re-verified at lane start), '
              'then refined with receipt-disclosed re-homings mirroring the PRINTED book '
              'order: 1159 raw-s01 -> s02 (nail-polish DYK prints p298 left margin beside '
              'MAKING), 1160/1161 raw-s01 -> s03 (EXTENSION H/OH detail prints beside Fig '
              '28.2; the oate KEY POINT prints beside Fig 28.3), 1164/1166/1167 stay s03, '
              '1169 raw-s04 -> s05 (the Safety Note prints p300 left margin directly beside '
              'the PRACTICAL box; the parse kept it under the USES heading run), 1170 home '
              's04 by bulk (solubility EXTENSION prints p300 margin above the practical '
              'heading, uses context), 1173/1174 -> s06 (questions close). ONE equation of '
              'record carried with in-chunk repairs (print-verified at 300 dpi, f-0028 '
              'identity gate applied — pdfinfo 383pp + sha256 d48020e0): CH3COOH(l) + '
              'CH3CH2OH(l) -> CH3COOCH2CH3(l) + H2O(l) (chunk garbles: doubled subscript '
              'glyph "CH₃3COOH", letter-I state symbols "(I)" x3, arrow lost to "=" — all '
              'repaired per the printed equation; atom-balanced C4H10O3 = C4H10O3); the '
              'reverse splitting equation (Fig 28.4 zone) print-true and taught in s03: '
              'CH3COOCH2CH3(l) + H2O(l) -> CH3COOH(l) + CH3CH2OH(l). ONE absent-content '
              'restore: the opener band first sentence (chunk 1157 renders it as a garble '
              '"Alel as s..." — restored per print to "Alcohols, carboxylic acids and esters '
              'are organic compounds that contain oxygen as well as carbon and hydrogen. '
              'They are closely related."). ONE parse-truncation repair (NEW f-0031 class): '
              'chunk 1171 ends mid-word ("easy to sm") — the printed step 7 (wafting '
              'instruction) truncated by the parse; restored per print in s05. Table 28.1 '
              'taught as content (nine esters: methanol/ethanol/propan-1-ol rows x '
              'methanoic/ethanoic/propanoic acid columns). f-0017 print-ref strips -> '
              'in-product pointers: carboxylic-acids-from-oxidation opener -> u4:c26; '
              'Chapter 21 equilibrium callback -> u3:c21; condensation forward reference -> '
              'u4:c29; no Figure/Table/page deflection in student prose (figure slots x6 '
              'taught in words: the fats-and-oils photo, the formation diagram, the '
              'two-ways-round drawing, the splitting diagram, the cosmetics-researcher '
              'photo, the test-tube practical diagram; Table 28.1 taught as content). '
              'Safety: the f-0029 recipe APPLIED (all five experiment-bearing pages p297-301 '
              'OCR-checked) — ONE printed safety panel exists and IS parse-present (chunk '
              '1169, the acids/fume-cupboard/wafting panel): honest presence, carried as the '
              's05 census-true safety box (c27 was honest ABSENCE; c28 is the first pack to '
              'carry a parse-present printed safety panel as a box). Questions bank: FIVE '
              'printed questions (Q1 draw/name six compounds at structural+displayed+named '
              'levels; Q2 four-part all-esters-from-two-alcohols-two-acids set with method '
              '+ detection + uses; Q3 decode methyl propanoate / a drawn structure / butyl '
              'ethanoate to their alcohol+acid pairs; Q4 ethanol-as-only-organic-starting-'
              'material multi-step route to ethyl ethanoate; Q5 unlabelled-samples '
              'identification without smelling) — page-jump-only per the licensing law, '
              'shapes taught not text. Pages [297,301] authored range (raw pre-derived '
              '[297,299]; the practical prints p300 and the questions close runs to printed '
              'p301 where END OF CHEMISTRY ONLY also prints).'),
}
lp = ROOT / 'lessons/pearson-edexcel/international-gcse/chemistry-4ch1/lessons/u4-c28-esters/lesson.yaml'
lp.parent.mkdir(parents=True, exist_ok=True)
lp.write_text(yaml.safe_dump(lesson, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- pin course.yaml row ----
cp = COURSE / 'course.yaml'
cfg = yaml.safe_load(cp.read_text(encoding='utf-8'))
hit = False
for rows in cfg['spine'].values():
    for r in rows:
        if r['key'] == 'u4:c28':
            r['join_set'] = JOIN
            r['learning_objective'] = learning_objective
            r['section_count'] = 6
            r['pages'] = [297, 301]
            hit = True
assert hit, 'u4:c28 row not found'
cp.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True, width=100), encoding='utf-8')

# ---- regenerate committed section map to the REFINED authored set ----
refined_map = {
    'chapter_key': 'u4:c28',
    'key_mapping': rawmap['key_mapping'],
    'book_page_range': [297, 301],
    'sections': [
        {'id': f'u4:c28:{sid}', 'title': title, 'bookPage': page,
         'chunkRefs': list(refs), 'specRefs': list(spec), 'status': 'todo'}
        for (sid, title, page, refs, spec, glo) in SECTIONS
    ],
}
sm_path = COURSE / 'section-maps/u4-c28.json'
sm_path.write_text(json.dumps(refined_map, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print('pin_c28_map: OK — lesson.yaml refined (6 sections / 17 chunks single-home / 18 slots '
      'with 1165 absent), course row pinned (join_set 4.38C-4.43C ALL-C 0+6, section_count 6, '
      'pages [297,301]), section-maps/u4-c28.json regenerated to the refined authored set')
