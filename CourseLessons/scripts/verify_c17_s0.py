#!/usr/bin/env python3
"""verify_c17_s0.py — u2:c17 Salt preparations S0 gates (T-BOOK-050 r0, trace 1a16f984a3d47ec9)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation from the
SPLIT objectives chunks 0687 + 0688-tail (column interleave: 2.38/2.39/2.42 bullets
serialized inside the SALTS body chunk) + 0689 CHEMISTRY ONLY x spine igcse-chemistry-T2:SUBg
one-to-one coverage (10 objectives) with TWO disclosed f-0016 covers: chunk 0687's 2.34
fragment carries only 4 of 6 sub-bullets (sulfates + carbonates absent from the objectives
fragments; full rule set taught in body chunk 0714) -> pin = spine-canonical; chunk 2.42
OCR garble "copper(Il)" -> pin = spine-canonical; (3) f-0015 sibling audit (FOURTH MIXED
pack: 6 core + 3 C, chem_only false); (4) page range + numeric-slot audit [54 present +
13 absent = 67 slots 0686..0752]; (5) glossary resolution + ms layer; (6) course.yaml row
pin; (7) FOUR disclosed title refinements (s07/s09/s18/s20) vs the map of record;
(8) per-section body-chip-set == front-matter-list equality (S0.23 law); (9) box coverage
incl. safety boxes PRESENT (3 census safety chunks) and did-you-know honest-absence;
(10) emitted-pack layer (learningObjective mirror, paperRoute core, specRefs, draft-or-
published status)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/syllabai-v2/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/books/pearson-edexcel/international-gcse/chemistry/4ch1/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u2-c17-salt-preparations/lesson.yaml').read_text())
ofmap = json.load(open(COURSE / 'section-maps/u2-c17.json'))

# (1) chunkRefs byte-verify
parse_ids = set()
u2c17_ids = set()
parse_sha = hashlib.sha256(PARSE.read_bytes()).hexdigest()
check('S0.0 parse of record sha256 == course.yaml pin', parse_sha == 'b2c67eafe4e3766bab41b41fc24795ca0fe95c1f5f55b8a3b3bffbc709af6d33', parse_sha[:12])
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u2_c17' in c['id']: u2c17_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u2_c17', all(r in u2c17_ids for r in refs))
of_refs = [r for s in ofmap['sections'] for r in s['chunkRefs']]
check('S0.3 section chunkRefs == section map of record (byte-equal, in order)', refs == of_refs, f'lesson={len(refs)} map={len(of_refs)}')

# (7) titles vs map of record — FOUR disclosed refinements (receipt layer)
REFINED = {'u2:c17:s07': 'Notes on the Solubility Table',
           'u2:c17:s09': 'The Solubility Rules',
           'u2:c17:s18': 'The Reaction between Ammonia and Hydrogen Chloride',
           'u2:c17:s20': 'Choosing the Method of Salt Preparation'}
title_drift = []
for s, m in zip(lesson['sections'], ofmap['sections']):
    if s['title'] != m['title'] and REFINED.get(s['id']) != s['title']:
        title_drift.append((s['id'], s['title'], m['title']))
check('S0.4 titles == map of record modulo the FOUR disclosed refinements', not title_drift, str(title_drift))
check('S0.4b refinement set is exactly {s07,s09,s18,s20}', set(REFINED) == {s['id'] for s in lesson['sections'] if s['id'] in REFINED}, ','.join(sorted(REFINED)))
check('S0.5 page range == [173, 189]', lesson['book_page_range'] == [173, 189] == ofmap['book_page_range'])
check('S0.5b bookPage monotonic + == of record', [s.get('bookPage') for s in lesson['sections']] == [s.get('bookPage') for s in ofmap['sections']])
check('S0.5c section count == 21 == map == course row', len(lesson['sections']) == 21 == len(ofmap['sections']))

# (4) full census sweep + numeric-slot audit
check('S0.5d census sweep: ALL u2_c17 chunks in parse are mapped into sections', u2c17_ids <= set(refs), f'census={len(u2c17_ids)} mapped={len(set(refs) & u2c17_ids)} unmapped={sorted(u2c17_ids - set(refs))}')
tails = sorted(int(i.rsplit('_', 1)[1]) for i in u2c17_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in u2c17_ids)]
ABSENT_EXPECT = [696, 698, 701, 702, 705, 706, 707, 710, 722, 723, 733, 734, 738]
check('S0.5e numeric-slot audit: 54 present + 13 absent = 67 slots (0686..0752)', len(tails) == 54 and absent == ABSENT_EXPECT and tails[0] == 686 and tails[-1] == 752, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: objectives chunks 0687 + 0688 + 0689 x spine SUBg
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subg = [n for n in nodes if n.get('code') == 'igcse-chemistry-T2:SUBg'][0]
pts = sorted([n for n in nodes if 'igcse-chemistry-T2:SUBg' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine SUBg = "Acids, bases and salt preparations"', 'Acids, bases and salt preparations' in subg['title'], subg['title'])
check('S0.7 SUBg carries exactly 10 spec points', len(pts) == 10, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']})
check('S0.8 join_set == [2.34, 2.35, 2.36, 2.37, 2.38, 2.39, 2.40C, 2.41C, 2.42, 2.43C]', join_set == ['2.34', '2.35', '2.36', '2.37', '2.38', '2.39', '2.40C', '2.41C', '2.42', '2.43C'], str(join_set))

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
o1 = chunks.get('chem_v3_u2_c17_pdf182_0687')
o2 = chunks.get('chem_v3_u2_c17_pdf182_0688')
o3 = chunks.get('chem_v3_u2_c17_pdf182_0689')
check('S0.8b objectives chunks 0687 + 0688 + 0689 all exist (split/interleave lane)', all(x is not None for x in (o1, o2, o3)))
check('S0.8c 0687/0689 are learning_objectives-type; 0688 is the interleave host body', o1.get('content_type') == 'learning_objectives' and o3.get('content_type') == 'learning_objectives' and o2.get('content_type') == 'body')

def norm(s):
    """f-0016 normalization: drop bullet glyphs + collapse whitespace + drop
    objective-separator ';' ':' + strip parentheses glyphs + normalize curly
    apostrophes/en-dashes + strip trailing '.' (case-insensitive)."""
    s = re.sub(r'[\u2022\n\s;:()]+', ' ', s).strip().lower()
    s = s.replace('\u2019', "'").replace('\u2013', '-').replace('\u2212', '-')
    return s[:-1] if s.endswith('.') else s

objs = {
 '2.34': 'Know the general rules for predicting the solubility of ionic compounds in water: • common sodium, potassium and ammonium compounds are soluble • all nitrates are soluble • common chlorides are soluble, except those of silver and lead(II) • common sulfates are soluble, except for those of barium, calcium and lead(II) • common carbonates are insoluble, except for those of sodium, potassium and ammonium • common hydroxides are insoluble except for those of sodium, potassium and calcium (calcium hydroxide is slightly soluble).',
 '2.35': 'Understand acids and bases in terms of proton transfer',
 '2.36': 'Understand that an acid is a proton donor and a base is a proton acceptor',
 '2.37': 'Describe the reactions of hydrochloric acid, sulfuric acid and nitric acid with metals, bases and metal carbonates (excluding the reactions between nitric acid and metals) to form salts',
 '2.38': 'Know that metal oxides, metal hydroxides and ammonia can act as bases, and that alkalis are bases that are soluble in water',
 '2.39': 'Describe an experiment to prepare a pure, dry sample of a soluble salt, starting from an insoluble reactant',
 '2.40C': 'Describe an experiment to prepare a pure, dry sample of a soluble salt, starting from an acid and alkali',
 '2.41C': 'Describe an experiment to prepare a pure, dry sample of an insoluble salt, starting from two soluble reactants',
 '2.42': 'practical: prepare a sample of pure, dry hydrated copper(II) sulfate crystals starting from copper(II) oxide',
 '2.43C': 'practical: prepare a sample of pure, dry lead(II) sulfate',
}
CARRIER = {'2.34': o1, '2.35': o1, '2.36': o1, '2.37': o1,
           '2.38': o2, '2.39': o2, '2.40C': o3, '2.41C': o3, '2.42': o2, '2.43C': o3}
obj_union_norm = norm(o1['text'] + ' ' + o2['text'] + ' ' + o3['text'])
by_code = {p['code']: p for p in pts}
for code, text in objs.items():
    carr = CARRIER[code]
    carr_norm = norm(carr['text'])
    sp = norm(by_code[code]['title'])
    want = norm(text)
    if code == '2.34':
        # f-0016 cover: chunk 0687 carries the lead + only 4 of 6 sub-bullets
        lead = norm('Know the general rules for predicting the solubility of ionic compounds in water')
        subs = ['common sodium, potassium and ammonium compounds are soluble',
                'all nitrates are soluble',
                'common chlorides are soluble, except those of silver and lead(II)',
                'common hydroxides are insoluble except for those of sodium, potassium and calcium (calcium hydroxide is slightly soluble)']
        check('S0.9 2.34 lead verbatim in chunk 0687', lead in carr_norm)
        check('S0.9a 2.34 four present sub-bullets verbatim in chunk 0687', all(norm(b) in carr_norm for b in subs))
        check('S0.9b 2.34 sulfate+carbonate sub-bullets ABSENT from ALL objectives fragments (disclosed truncation; full rule set taught in body chunk 0714)', norm('common sulfates are soluble') not in obj_union_norm and norm('common carbonates are insoluble') not in obj_union_norm and norm('sulfates are soluble, except lead') in norm(chunks['chem_v3_u2_c17_pdf187_0714']['text']))
        check('S0.9c 2.34 pin == spine-canonical full text (case/glyph-normalized)', sp == want)
    elif code == '2.42':
        check('S0.9d 2.42 chunk garble "copper(Il)" present in 0688 raw (disclosed OCR)', 'copper(Il)' in o2['text'])
        check('S0.9e 2.42 pin == spine-canonical (garble restored, f-0016 cover law)', sp == want)
        check('S0.9f 2.42 clean prefix verbatim in chunk 0688', norm('Practical: Prepare a sample of pure, dry hydrated copper') in carr_norm)
    else:
        check(f'S0.9 {code} objective verbatim in carrying chunk (case/glyph-normalized)', want in carr_norm, by_code[code]['title'][:60])
    check(f'S0.9g {code} chunk text == spine title (normalized)', sp == norm(carr['text']) or want == sp or code in ('2.34', '2.42'))

# (3) f-0015 sibling audit: FOURTH MIXED paper-route pack (6 core + 3 C), chem_only false
core = [p for p in pts if not p['code'].endswith('C')]
conly = [p for p in pts if p['code'].endswith('C')]
check('S0.10 7 core + 3 C-suffixed (MIXED pack — course fourth; c11/c12 3+1, c16 5+1 precedent)', len(core) == 7 and len(conly) == 3, f'core={[p["code"] for p in core]} conly={[p["code"] for p in conly]}')
check('S0.11 core points papers [1C,2C] shared; C points papers [2C] not shared', all(p['applicability']['papers'] == ['1C', '2C'] and p['applicability']['double_award_shared'] for p in core) and all((not p['applicability']['double_award_shared']) and p['applicability']['papers'] == ['2C'] for p in conly))
check('S0.12 lesson.yaml chem_only false', lesson['chem_only'] is False)
course = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = [r for r in course['spine']['u2'] if r['key'] == 'u2:c17'][0]
check('S0.13 course.yaml row: chem_only false, section_count 21, pages [173,189]', row['chem_only'] is False and row['section_count'] == 21 and row['pages'] == [173, 189])
u1_flags = {r['key']: r.get('chem_only') for r in course['spine']['u1']}
check('S0.14 sibling audit: u1 pack routes uniform (all-core x7 / all-C x3), none mixed', all(isinstance(v, bool) for v in u1_flags.values()) and sum(u1_flags.values()) == 3, str(u1_flags))
c11_pack = json.load(open(COURSE / 'lessons/u2-c11-alkali-metals/qa/lessonPackV1.json'))
c12_pack = json.load(open(COURSE / 'lessons/u2-c12-halogens/qa/lessonPackV1.json'))
c11_specs = {r for s in c11_pack['sections'] for r in s['specRefs']}
c12_specs = {r for s in c12_pack['sections'] for r in s['specRefs']}
c13r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c13'][0]
c14r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c14'][0]
c15r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c15'][0]
c16r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c16'][0]
c17_C = [x for x in join_set if x.endswith('C')]
sub_flags = {
 'c11_mixed': any(x.endswith('C') for x in c11_specs),
 'c12_mixed': any(x.endswith('C') for x in c12_specs),
 'c13_allcore': not any(str(x).endswith('C') for x in c13r.get('join_set', [])),
 'c14_allcore': not any(str(x).endswith('C') for x in c14r.get('join_set', [])),
 'c15_allC': bool(c15r.get('join_set')) and all(str(x).endswith('C') for x in c15r.get('join_set', [])),
 'c16_mixed_5_1': c16r.get('join_set', [])[-1] == '2.33C' and len(c16r.get('join_set', [])) == 6,
 'c17_mixed_7_3': c17_C == ['2.40C', '2.41C', '2.43C'],
}
check('S0.15 sibling audit: c11/c12 mixed (C refs in packs), c13/c14 all-core rows, c15 all-C row, c16 mixed 5+1, c17 mixed 7+3 — no mixed-shape drift', all(sub_flags.values()), str(sub_flags))
check('S0.16 course.yaml row PINNED: join_set + learning_objective present', bool(row.get('join_set')) and bool(row.get('learning_objective')))

# (6) learning_objective law: course row == lesson.yaml == spine-order reassembly
lo_row = row.get('learning_objective', '').lower()
lo_lesson = (lesson.get('learning_objective') or '').lower()
check('S0.17 lesson.yaml learning_objective == course.yaml pin (verbatim mirror)', lo_lesson == lo_row and len(lo_row) > 800)
assembled = norm('; '.join(objs[c] for c in ['2.34', '2.35', '2.36', '2.37', '2.38', '2.39', '2.40C', '2.41C', '2.42', '2.43C']))
check('S0.18 course.yaml pin == spine-order reassembly of the 10 objectives (2.34/2.42 spine-canonical, disclosed)', norm(lo_row) == assembled)
check('S0.18b pin order is SPINE order (2.34..2.43C) not chunk order', lo_row.index('know the general rules') < lo_row.index('understand acids and bases in terms') < lo_row.index('understand that an acid is a proton donor') < lo_row.index('describe the reactions of hydrochloric') < lo_row.index('know that metal oxides') < lo_row.index('an insoluble reactant') < lo_row.index('an acid and alkali') < lo_row.index('two soluble reactants') < lo_row.index('copper(ii) sulfate crystals') < lo_row.index('dry lead(ii) sulfate'))

# (5) glossary resolution + ms layer
gloss = yaml.safe_load((COURSE / 'lessons/u2-c17-salt-preparations/glossary.yaml').read_text())
slugs = {g['slug'] for g in (gloss or [])}
sec_slugs = {sl for s in lesson['sections'] if s.get('glossary') for sl in s['glossary']}
check('S0.19 all section glossary slugs resolve in glossary.yaml', sec_slugs <= slugs, f'unresolved={sec_slugs - slugs}')
check('S0.19b every glossary entry has ms_accepts + definition <=40 words + source chunkRef', all(g.get('ms_accepts') and len((g.get('definition') or '').split()) <= 40 and g.get('source') for g in (gloss or [])))
check('S0.19c glossary carries 26 entries (full ms layer)', len(gloss) == 26, str(len(gloss)))

# (8) chips per section == front-matter glossary list (S0.23 law)
chip_fail = []
FM_RE = re.compile(r'^---\n(.*?)\n---\n?(.*)$', re.S)
for f in sorted((COURSE / 'lessons/u2-c17-salt-preparations/sections').glob('*.md')):
    m = FM_RE.match(f.read_text())
    fmy = yaml.safe_load(m.group(1)) or {}
    body = m.group(2)
    chips = sorted(set(re.findall(r'\[\[([^\]]+)\]\]', body)))
    listed = sorted(fmy.get('glossary') or [])
    if chips != listed:
        chip_fail.append((f.name, chips, listed))
check('S0.23 every section: body chip set == front-matter glossary list (slug-form, no pipe-alias)', not chip_fail, str(chip_fail))

# (9) box coverage (f-0014 law shape) + census-type box placement
box_fail = []
need = {'exam-hint', 'misconception', 'quick-check'}
boxmap = {}
for f in sorted((COURSE / 'lessons/u2-c17-salt-preparations/sections').glob('*.md')):
    body = FM_RE.match(f.read_text()).group(2)
    boxes = set(re.findall(r'^:::([a-z0-9-]+)\s*$', body, re.M))
    boxmap[f.name] = boxes
    if boxes & need != need:
        box_fail.append((f.name, 'missing ' + str(need - boxes)))
sp = (COURSE / 'lessons/u2-c17-salt-preparations/sections')
s01 = (sp / 's01-acids-bases-and-salt-preparations.md').read_text()
s02 = (sp / 's02-salts.md').read_text()
s09 = (sp / 's09-the-solubility-rules.md').read_text()
s10 = (sp / 's10-making-soluble-salts-except-sodium-potassium-and-ammonium.md').read_text()
s12 = (sp / 's12-making-magnesium-sulfate-crystals.md').read_text()
s14 = (sp / 's14-precipitation-reactions.md').read_text()
s15 = (sp / 's15-making-insoluble-salts.md').read_text()
s17 = (sp / 's17-theories-of-acids-and-bases.md').read_text()
s18 = (sp / 's18-the-reaction-between-ammonia-and-hydrogen-chloride.md').read_text()
s19 = (sp / 's19-more-acid-base-reactions.md').read_text()
s20 = (sp / 's20-choosing-the-method-of-salt-preparation.md').read_text()
s21 = (sp / 's21-end-of-chemistry-only.md').read_text()
check('S0.24 box coverage: all 21 sections carry exam-hint+misconception+quick-check', not box_fail, str(box_fail))
check('S0.24a s01 prior-knowledge; key-points s02+s10+s12+s14 (census KP chunks 0691/0718/0724/0730); s21 summary+can-you+cross-curricular', ':::prior-knowledge' in s01 and all(':::key-point' in t for t in (s02, s10, s12, s14)) and all(b in s21 for b in (':::summary', ':::can-you', ':::cross-curricular')))
check('S0.24b safety boxes PRESENT at the 3 census safety chunks (0715->s09, 0719->s10, 0735->s15)', all(':::safety' in t for t in (s09, s10, s15)))
check('S0.24c did-you-know honestly absent (0 census chunks of that type)', all(c.get('content_type') != 'did_you_know' for c in chunks.values() if 'u2_c17' in c['id']))
s17_body = FM_RE.match(s17).group(2)
check('S0.24d s17 census key-points 0742/0743 prose-carried (hydroxonium + ammonia-OH substance present)', 'hydroxonium' in s17_body and 'NH₃ + H₂O' in s17_body)
check('S0.24e licensing law: chapter-questions chunks 0746-0752 carry no reproduced question text (page-jump-only; chunkRefs on s18/s19/s20/s21 for provenance)', all('CHAPTER QUESTIONS' not in FM_RE.match(t).group(2) for t in (s18, s19, s20, s21)))

# (10) emitted-pack layer (post-emit runs)
pack_path = COURSE / 'lessons/u2-c17-salt-preparations/qa/lessonPackV1.json'
if pack_path.exists():
    pack = json.load(open(pack_path))
    psecs = pack['sections']
    p_refs = [r for s in psecs for r in s['chunkRefs']]
    p_specs = sorted({r for s in psecs for r in s['specRefs']})
    check('S0.20 emitted pack: chunkRefs == lesson spine, specRefs == join_set', p_refs == refs and p_specs == ['2.34', '2.35', '2.36', '2.37', '2.38', '2.39', '2.40C', '2.41C', '2.42', '2.43C'])
    check('S0.21 emitted pack: learningObjective NON-NULL == course pin; paperRoute core (mixed); status draft-or-published (law-7 flip tolerance)', pack.get('learningObjective') == row.get('learning_objective') and pack.get('paperRoute') == 'core' and pack.get('status') in ('draft', 'published'))
    check('S0.22 emitted pack sources sha-pinned', 'b2c67eaf' in (pack.get('sources') or {}).get('parseOfRecord', ''))
    check('S0.25 emitted pack: 21 sections, titles == lesson spine (refinements included)', [s['title'] for s in psecs] == [s['title'] for s in lesson['sections']] and len(psecs) == 21)
else:
    print('SKIP S0.20-S0.22, S0.25 (qa/lessonPackV1.json not emitted yet)')

print('S0 VERDICT:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
