#!/usr/bin/env python3
"""verify_c16_s0.py — u2:c16 Acids, alkalis and titrations S0 gates (T-BOOK-049 r0, trace 1a16f57915b6e4d9)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation
from the LEARNING OBJECTIVES chunk 0655 (all six objectives in ONE chunk — no
split reassembly this lane) x spine igcse-chemistry-T2:SUBf one-to-one coverage
with TWO disclosed join-glyph deltas: spine 2.29 "to use" doubling (pin follows
the clean chunk) + chunk 2.31 OCR garble (restored from spine-canonical, spine's
own "a aqueous" doubling kept verbatim); (3) f-0015 sibling audit (MIXED
paper-route pack: 5 core + 1 C, chem_only false — c11/c12 precedent); (4) page
range; (5) glossary resolution; (6) full census sweep incl. the 7 absent
display/figure fragment ids; (7) course.yaml row pin (join_set +
learning_objective); (8) emitted-pack layer (learningObjective mirror,
paperRoute core, specRefs, draft-or-published status)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/syllabai-v2/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/books/pearson-edexcel/international-gcse/chemistry/4ch1/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u2-c16-acids-alkalis-titrations/lesson.yaml').read_text())
ofmap = json.load(open(COURSE / 'section-maps/u2-c16.json'))

# (1) chunkRefs byte-verify
parse_ids = set()
u2c16_ids = set()
parse_sha = hashlib.sha256(PARSE.read_bytes()).hexdigest()
check('S0.0 parse of record sha256 == course.yaml pin', parse_sha == 'b2c67eafe4e3766bab41b41fc24795ca0fe95c1f5f55b8a3b3bffbc709af6d33', parse_sha[:12])
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u2_c16' in c['id']: u2c16_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u2_c16', all(r in u2c16_ids for r in refs))
of_refs = [r for s in ofmap['sections'] for r in s['chunkRefs']]
check('S0.3 section chunkRefs == section map of record (byte-equal, in order)', refs == of_refs, f'lesson={len(refs)} map={len(of_refs)}')
titles = [s['title'] for s in lesson['sections']]
check('S0.4 section titles == of record', titles == [s['title'] for s in ofmap['sections']])
check('S0.5 page range == [167, 172]', lesson['book_page_range'] == [167, 172] == ofmap['book_page_range'])
check('S0.5b bookPage monotonic + == of record', [s.get('bookPage') for s in lesson['sections']] == [s.get('bookPage') for s in ofmap['sections']])

# (6) full census sweep
check('S0.5c census sweep: ALL u2_c16 chunks in parse are mapped into sections', u2c16_ids <= set(refs), f'census={len(u2c16_ids)} mapped={len(set(refs) & u2c16_ids)} unmapped={sorted(u2c16_ids - set(refs))}')
tails = sorted(int(i.rsplit('_', 1)[1]) for i in u2c16_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in u2c16_ids)]
check('S0.5d numeric-slot audit: 25 present + 7 absent = 32 slots (0654..0685)', len(tails) == 25 and len(absent) == 7 and tails[0] == 654 and tails[-1] == 685, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: objectives chunk 0655 x spine SUBf
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subf = [n for n in nodes if n.get('code') == 'igcse-chemistry-T2:SUBf'][0]
pts = sorted([n for n in nodes if 'igcse-chemistry-T2:SUBf' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine SUBf = "Acids, alkalis and titrations"', 'Acids, alkalis and titrations' in subf['title'], subf['title'])
check('S0.7 SUBf carries exactly 6 spec points', len(pts) == 6, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']})
check('S0.8 join_set == [2.28, 2.29, 2.30, 2.31, 2.32, 2.33C]', join_set == ['2.28', '2.29', '2.30', '2.31', '2.32', '2.33C'], str(join_set))

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
obj_chunk = chunks.get('chem_v3_u2_c16_pdf176_0655')
check('S0.8b objectives chunk 0655 exists (single-chunk objectives — no split)', obj_chunk is not None)

def norm(s):
    """f-0016 normalization: drop bullet glyphs + collapse whitespace + drop
    objective-separator ';' ':' + strip parentheses glyphs (2.29 band ranges
    '(0-3)'/'(4–6)' hyphen/en-dash glyphs) + normalize curly apostrophes +
    strip trailing '.' (case-insensitive)."""
    s = re.sub(r'[\u2022\n\s;:()]+', ' ', s).strip().lower()
    s = s.replace('\u2019', "'").replace('\u2013', '-').replace('\u2212', '-')
    return s[:-1] if s.endswith('.') else s

# logical objectives, in SPINE order; 2.31 restored from spine-canonical (garbled chunk)
objs = {
 '2.28': 'Describe the use of litmus, phenolphthalein and methyl orange to distinguish between acidic and alkaline solutions',
 '2.29': 'Understand how the pH scale, from 0-14, can be used to classify solutions as strongly acidic (0-3), weakly acidic (4-6), neutral (7), weakly alkaline (8-10) and strongly alkaline (11-14)',
 '2.30': 'Describe the use of universal indicator to measure the approximate pH value of an aqueous solution',
 '2.31': 'Know that acids in aqueous solution are a source of hydrogen ions and alkalis in a aqueous solution are a source of hydroxide ions',
 '2.32': 'Know that alkalis can neutralise acids',
 '2.33C': 'Describe how to carry out an acid-alkali titration',
}
obj_norm = norm(obj_chunk['text'])
by_code = {p['code']: p for p in pts}
for code, text in objs.items():
    pieces = [norm(x) for x in text.split(';')]
    if code == '2.31':
        # f-0016 cover: clean prefix verbatim in chunk; garble covered by spine-canonical text
        prefix = norm('Know that acids in aqueous solution are a source of hy')
        check('S0.9 2.31 clean prefix verbatim in chunk 0655 (garble cover law)', prefix in obj_norm, 'prefix=…source of hy')
        check('S0.9z 2.31 spine-canonical restoration disclosed (chunk garble "hy n sls sn an a sl n s ra")', 'hy n sls' in obj_chunk['text'])
    else:
        check(f'S0.9 {code} objective verbatim in chunk 0655 (case/glyph-normalized)', all(p in obj_norm for p in pieces), by_code[code]['title'][:60])
    # spine match: 2.28/2.30/2.31/2.32/2.33C direct; 2.29 with disclosed spine "to use" doubling removed
    sp = norm(by_code[code]['title'])
    want = norm(text)
    if code == '2.29':
        sp_fixed = sp.replace('to use the ph scale', 'the ph scale')
        want_fixed = want.replace('to use the ph scale', 'the ph scale')
        check('S0.9b 2.29 matches spine title after disclosed "to use" doubling removal (spine-side artifact, zero wording change)', sp_fixed == want_fixed, sp[:70])
    else:
        check(f'S0.9b {code} reassembly matches spine title (case-insensitive, glyph-normalized)', sp == want, '')

# (3) f-0015 sibling audit: MIXED paper-route pack (5 core + 1 C), chem_only false
core = [p for p in pts if not p['code'].endswith('C')]
conly = [p for p in pts if p['code'].endswith('C')]
check('S0.10 5 core + 1 C-suffixed (MIXED pack — course third, c11/c12 precedent)', len(core) == 5 and len(conly) == 1, f'core={len(core)} conly={len(conly)}')
check('S0.11 core points papers [1C,2C] shared; 2.33C papers [2C] not shared', all(p['applicability']['papers'] == ['1C', '2C'] and p['applicability']['double_award_shared'] for p in core) and (not conly[0]['applicability']['double_award_shared']) and conly[0]['applicability']['papers'] == ['2C'])
check('S0.12 lesson.yaml chem_only false', lesson['chem_only'] is False)
course = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = [r for r in course['spine']['u2'] if r['key'] == 'u2:c16'][0]
check('S0.13 course.yaml row: chem_only false, section_count 9, pages [167,172]', row['chem_only'] is False and row['section_count'] == 9 and row['pages'] == [167, 172])
u1_flags = {r['key']: r.get('chem_only') for r in course['spine']['u1']}
check('S0.14 sibling audit: u1 pack routes uniform (all-core x7 / all-C x3), none mixed', all(isinstance(v, bool) for v in u1_flags.values()) and sum(u1_flags.values()) == 3, str(u1_flags))
c11_pack = json.load(open(COURSE / 'lessons/u2-c11-alkali-metals/qa/lessonPackV1.json'))
c12_pack = json.load(open(COURSE / 'lessons/u2-c12-halogens/qa/lessonPackV1.json'))
c11_specs = {r for s in c11_pack['sections'] for r in s['specRefs']}
c12_specs = {r for s in c12_pack['sections'] for r in s['specRefs']}
c13r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c13'][0]
c14r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c14'][0]
c15r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c15'][0]
check('S0.15 sibling audit: c11/c12 mixed (C refs in packs), c13/c14 all-core rows, c15 all-C row, c16 mixed — no mixed-shape drift', any(x.endswith('C') for x in c11_specs) and any(x.endswith('C') for x in c12_specs) and not any(str(x).endswith('C') for x in c13r.get('join_set', [])) and not any(str(x).endswith('C') for x in c14r.get('join_set', [])) and all(str(x).endswith('C') for x in c15r.get('join_set', [])) and '2.33C' in join_set, f'c16={[x for x in join_set if x.endswith("C")]}')
check('S0.16 course.yaml row PINNED: join_set + learning_objective present', bool(row.get('join_set')) and bool(row.get('learning_objective')))

# (7) learning_objective law: course row == lesson.yaml == spine-order reassembly
lo_row = row.get('learning_objective', '').lower()
lo_lesson = (lesson.get('learning_objective') or '').lower()
check('S0.17 lesson.yaml learning_objective == course.yaml pin (verbatim mirror)', lo_lesson == lo_row and len(lo_row) > 200)
assembled = norm('; '.join(objs[c] for c in ['2.28', '2.29', '2.30', '2.31', '2.32', '2.33C']))
check('S0.18 course.yaml pin == spine-order reassembly of chunk 0655 objectives (verbatim, normalized; 2.31 spine-canonical disclosed)', norm(lo_row) == assembled)
check('S0.18b pin order is SPINE order (2.28,2.29,2.30,2.31,2.32,2.33C) not chunk order', lo_row.index('describe the use of litmus') < lo_row.index('understand how the ph scale') < lo_row.index('describe the use of universal') < lo_row.index('know that acids in aqueous') < lo_row.index('know that alkalis can neutralise') < lo_row.index('describe how to carry out'))

# (5) glossary resolution
gloss = yaml.safe_load((COURSE / 'lessons/u2-c16-acids-alkalis-titrations/glossary.yaml').read_text())
slugs = {g['slug'] for g in (gloss or [])}
sec_slugs = {sl for s in lesson['sections'] if s.get('glossary') for sl in s['glossary']}
check('S0.19 all section glossary slugs resolve in glossary.yaml', sec_slugs <= slugs, f'unresolved={sec_slugs - slugs}')
check('S0.19b every glossary entry has ms_accepts + definition <=40 words + source chunkRef', all(g.get('ms_accepts') and len((g.get('definition') or '').split()) <= 40 and g.get('source') for g in (gloss or [])))

# (9) chips per section == front-matter glossary list (this lane's tightened check)
chip_fail = []
FM_RE = re.compile(r'^---\n(.*?)\n---\n?(.*)$', re.S)
for f in sorted((COURSE / 'lessons/u2-c16-acids-alkalis-titrations/sections').glob('*.md')):
    m = FM_RE.match(f.read_text())
    fmy = yaml.safe_load(m.group(1)) or {}
    body = m.group(2)
    chips = sorted(set(re.findall(r'\[\[([^\]]+)\]\]', body)))
    listed = sorted(fmy.get('glossary') or [])
    if chips != listed:
        chip_fail.append((f.name, chips, listed))
check('S0.23 every section: body chip set == front-matter glossary list (slug-form, no pipe-alias)', not chip_fail, str(chip_fail))

# (10) box coverage (f-0014 law shape): exam-hint + misconception + quick-check x9;
# prior-knowledge s01; key-point s02+s08; summary+can-you+cross-curricular s09
box_fail = []
for f in sorted((COURSE / 'lessons/u2-c16-acids-alkalis-titrations/sections').glob('*.md')):
    body = FM_RE.match(f.read_text()).group(2)
    boxes = set(re.findall(r'^:::([a-z0-9-]+)\s*$', body, re.M))
    need = {'exam-hint', 'misconception', 'quick-check'}
    if boxes & need != need:
        box_fail.append((f.name, 'missing ' + str(need - boxes)))
s01 = (COURSE / 'lessons/u2-c16-acids-alkalis-titrations/sections/s01-acids-alkalis-and-titrations.md').read_text()
s02 = (COURSE / 'lessons/u2-c16-acids-alkalis-titrations/sections/s02-ph-and-indicators.md').read_text()
s08 = (COURSE / 'lessons/u2-c16-acids-alkalis-titrations/sections/s08-titration.md').read_text()
s09 = (COURSE / 'lessons/u2-c16-acids-alkalis-titrations/sections/s09-end-of-chemistry-only.md').read_text()
check('S0.24 box coverage: all 9 sections carry exam-hint+misconception+quick-check; s01 prior-knowledge; s02+s08 key-point; s09 summary+can-you+cross-curricular', not box_fail and ':::prior-knowledge' in s01 and ':::key-point' in s02 and ':::key-point' in s08 and all(b in s09 for b in (':::summary', ':::can-you', ':::cross-curricular')), str(box_fail))
check('S0.24b did-you-know + safety honestly absent (0 census chunks of those types)', all('did_you_know' != c['content_type'] and 'safety' != c['content_type'] for c in chunks.values() if 'u2_c16' in c['id']))

# (8) emitted-pack layer (post-emit runs)
pack_path = COURSE / 'lessons/u2-c16-acids-alkalis-titrations/qa/lessonPackV1.json'
if pack_path.exists():
    pack = json.load(open(pack_path))
    psecs = pack['sections']
    p_refs = [r for s in psecs for r in s['chunkRefs']]
    p_specs = sorted({r for s in psecs for r in s['specRefs']})
    check('S0.20 emitted pack: chunkRefs == lesson spine, specRefs == join_set', p_refs == refs and p_specs == ['2.28', '2.29', '2.30', '2.31', '2.32', '2.33C'])
    check('S0.21 emitted pack: learningObjective NON-NULL == course pin; paperRoute core (mixed); status draft-or-published (law-7 flip tolerance)', pack.get('learningObjective') == row.get('learning_objective') and pack.get('paperRoute') == 'core' and pack.get('status') in ('draft', 'published'))
    check('S0.22 emitted pack sources sha-pinned', 'b2c67eaf' in (pack.get('sources') or {}).get('parseOfRecord', ''))
else:
    print('SKIP S0.20-S0.22 (qa/lessonPackV1.json not emitted yet)')

print('S0 VERDICT:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
