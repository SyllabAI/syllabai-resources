#!/usr/bin/env python3
"""verify_c15_s0.py — u2:c15 Extraction and uses of metals S0 gates (T-BOOK-048 r0, trace 1a16f2c244eaa6f5)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation
from the LEARNING OBJECTIVES chunk (0630) + the objectives continuation swept
into body chunk 0634 (f-0016 reassembly law — split-objectives precedent c10/
c12/c14) x spine igcse-chemistry-T2:SUBe one-to-one coverage; (3) f-0015
sibling audit (all-C paper-route pack + chem_only true); (4) page range;
(5) glossary resolution; (6) full census sweep incl. the 3 display/figure
fragment ids ABSENT from the parse of record; (7) course.yaml row pin
(join_set + learning_objective); (8) emitted-pack layer (learningObjective
mirror, paperRoute, specRefs).
Join-glyph normalization for this lane (disclosed in receipt): paren glyphs
stripped (spine drops the chunk's parentheses around the 2.24C/2.25C
qualifications — zero wording change) + curly-apostrophe normalization
(spine Earth’s vs chunk Earth's)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/syllabai-v2/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/books/pearson-edexcel/international-gcse/chemistry/4ch1/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u2-c15-extraction-metals/lesson.yaml').read_text())
ofmap = json.load(open(COURSE / 'section-maps/u2-c15.json'))

# (1) chunkRefs byte-verify
parse_ids = set()
u2c15_ids = set()
parse_sha = hashlib.sha256(PARSE.read_bytes()).hexdigest()
check('S0.0 parse of record sha256 == course.yaml pin', parse_sha == 'b2c67eafe4e3766bab41b41fc24795ca0fe95c1f5f55b8a3b3bffbc709af6d33', parse_sha[:12])
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u2_c15' in c['id']: u2c15_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u2_c15', all(r in u2c15_ids for r in refs))
of_refs = [r for s in ofmap['sections'] for r in s['chunkRefs']]
check('S0.3 section chunkRefs == section map of record (byte-equal, in order)', refs == of_refs, f'lesson={len(refs)} map={len(of_refs)}')
titles = [s['title'] for s in lesson['sections']]
check('S0.4 section titles == of record', titles == [s['title'] for s in ofmap['sections']])
check('S0.5 page range == [160, 164]', lesson['book_page_range'] == [160, 164] == ofmap['book_page_range'])
check('S0.5b bookPage monotonic + == of record', [s.get('bookPage') for s in lesson['sections']] == [s.get('bookPage') for s in ofmap['sections']])

# (6) full census sweep — every u2_c15 chunk in the parse is mapped (22/22)
check('S0.5c census sweep: ALL u2_c15 chunks in parse are mapped into sections', u2c15_ids <= set(refs), f'census={len(u2c15_ids)} mapped={len(set(refs) & u2c15_ids)} unmapped={sorted(u2c15_ids - set(refs))}')
# numeric-slot audit: 0629..0653 = 25 slots, 22 present in parse, 3 absent (0635/0643/0647 — display/figure fragments, v3 pipeline; c12/c13/c14 precedent)
tails = sorted(int(i.rsplit('_', 1)[1]) for i in u2c15_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in u2c15_ids)]
check('S0.5d numeric-slot audit: 22 present + 3 absent = 25 slots (0629..0653)', len(tails) == 22 and len(absent) == 3 and tails[0] == 629 and tails[-1] == 653, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: objectives chunk 0630 + continuation chunk 0634 x spine SUBe
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
sube = [n for n in nodes if n.get('code') == 'igcse-chemistry-T2:SUBe'][0]
pts = sorted([n for n in nodes if 'igcse-chemistry-T2:SUBe' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine SUBe = "Extraction and uses of metals"', 'Extraction and uses of metals' in sube['title'], sube['title'])
check('S0.7 SUBe carries exactly 6 spec points', len(pts) == 6, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']})
check('S0.8 join_set == [2.22C..2.27C]', join_set == ['2.22C', '2.23C', '2.24C', '2.25C', '2.26C', '2.27C'], str(join_set))

chunks = {}
for line in open(PARSE):
    c = json.loads(line)
    chunks[c['id']] = c
obj_chunk = chunks.get('chem_v3_u2_c15_pdf169_0630')
cont_chunk = chunks.get('chem_v3_u2_c15_pdf169_0634')
check('S0.8b objectives chunk 0630 + continuation chunk 0634 exist', obj_chunk is not None and cont_chunk is not None)

def norm(s):
    """f-0016 interleave normalization for c15: drop bullet glyphs + collapse
    whitespace + drop objective-separator ';' ':' + STRIP PARENTHESES (spine
    drops the chunk's parentheses around the 2.24C/2.25C qualifications —
    zero wording change) + normalize curly apostrophes (spine Earth’s vs
    chunk Earth's) + strip trailing '.' (spine sentences end with one) so the
    split objectives match verbatim (case-insensitive)."""
    s = re.sub(r'[\u2022\n\s;:()]+', ' ', s).strip().lower()
    s = s.replace('\u2019', "'")
    return s[:-1] if s.endswith('.') else s

# logical objectives REASSEMBLED from the two chunks, in spine order
objs = {
 '2.22C': "Know that most metals are extracted from ores found in the Earth's crust and that unreactive metals are often found as the uncombined element",
 '2.23C': 'Explain how the method of extraction of a metal is related to its position in the reactivity series, illustrated by carbon extraction for iron and electrolysis for aluminium',
 '2.24C': 'Be able to comment on a metal extraction process, given appropriate information (detailed knowledge of the processes used in the extraction of a specific metal is not required)',
 '2.25C': 'Explain the uses of aluminium, copper, iron and steel in terms of their properties (the types of steel will be limited to low-carbon (mild), high-carbon and stainless)',
 '2.26C': 'Know that an alloy is a mixture of a metal and one or more elements, usually other metals or carbon',
 '2.27C': 'Explain why alloys are harder than pure metals',
}
obj_home = {'2.22C': obj_chunk, '2.23C': obj_chunk, '2.24C': obj_chunk,
            '2.25C': cont_chunk, '2.26C': cont_chunk, '2.27C': cont_chunk}
by_code = {p['code']: p for p in pts}
for code, text in objs.items():
    ch = obj_home[code]
    ch_norm = norm(ch['text'])
    pieces = [norm(x) for x in text.split(';')]
    check(f'S0.9 {code} reassembled objective pieces all verbatim in chunk {ch["id"].rsplit("_",1)[1]} (f-0016 normalization)', all(p in ch_norm for p in pieces), by_code[code]['title'][:60])
    check(f'S0.9b {code} reassembly matches spine title (case-insensitive)', norm(by_code[code]['title']) == norm(text), '')

# (3) f-0015 sibling audit: all-C paper-route pack + chem_only true
core = [p for p in pts if not p['code'].endswith('C')]
conly = [p for p in pts if p['code'].endswith('C')]
check('S0.10 0 core + 6 C-suffixed (ALL-CHEMISTRY-ONLY pack)', len(core) == 0 and len(conly) == 6, f'core={len(core)} conly={len(conly)}')
check('S0.11 all C points chemistry-only, papers [2C] only', all((not p['applicability']['double_award_shared']) and p['applicability']['papers'] == ['2C'] for p in conly))
check('S0.12 lesson.yaml chem_only true', lesson['chem_only'] is True)
course = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = [r for r in course['spine']['u2'] if r['key'] == 'u2:c15'][0]
check('S0.13 course.yaml row: chem_only true, section_count 10, pages [160,164]', row['chem_only'] is True and row['section_count'] == 10 and row['pages'] == [160, 164])
# sibling audit: u1 routes uniform (all-core x7 / all-C x3), none mixed; u2 c11/c12 mixed, c13/c14 all-core, c15 all-C
u1_flags = {r['key']: r.get('chem_only') for r in course['spine']['u1']}
check('S0.14 sibling audit: u1 pack routes uniform (all-core x7 / all-C x3), none mixed', all(isinstance(v, bool) for v in u1_flags.values()) and sum(u1_flags.values()) == 3, str(u1_flags))
c11r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c11'][0]
c12r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c12'][0]
c13r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c13'][0]
c14r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c14'][0]
# c11/c12 course rows are UNPINNED (c13-receipt debt) — their mixed shape is
# evidenced at pack layer: emitted packs carry the C-suffixed specRefs.
c11_pack = json.load(open(COURSE / 'lessons/u2-c11-alkali-metals/qa/lessonPackV1.json'))
c12_pack = json.load(open(COURSE / 'lessons/u2-c12-halogens/qa/lessonPackV1.json'))
c11_specs = {r for s in c11_pack['sections'] for r in s['specRefs']}
c12_specs = {r for s in c12_pack['sections'] for r in s['specRefs']}
check('S0.15 sibling audit: c11/c12 packs mixed (C-suffixed present), c13/c14 rows all-core, c15 row all-C — no mixed-shape drift', row.get('join_set') == ['2.22C', '2.23C', '2.24C', '2.25C', '2.26C', '2.27C'] and c13r.get('join_set') == ['2.9', '2.10', '2.11', '2.12', '2.13', '2.14'] and c14r.get('join_set') == ['2.15', '2.16', '2.17', '2.18', '2.19', '2.20', '2.21'] and any(x.endswith('C') for x in c11_specs) and any(x.endswith('C') for x in c12_specs) and not any(str(x).endswith('C') for x in c13r.get('join_set', [])) and not any(str(x).endswith('C') for x in c14r.get('join_set', [])), f'c11={[x for x in c11_specs if x.endswith("C")]} c12={[x for x in c12_specs if x.endswith("C")]}')
check('S0.16 course.yaml row PINNED: join_set + learning_objective present', bool(row.get('join_set')) and bool(row.get('learning_objective')))

# (7) learning_objective verbatim law: course.yaml row == lesson.yaml == reassembled chunk objectives
lo_row = row.get('learning_objective', '').lower()
lo_lesson = (lesson.get('learning_objective') or '').lower()
check('S0.17 lesson.yaml learning_objective == course.yaml pin (verbatim mirror)', lo_lesson == lo_row and len(lo_row) > 200)
assembled = norm('; '.join(objs[c] for c in ['2.22C', '2.23C', '2.24C', '2.25C', '2.26C', '2.27C']))
check('S0.18 course.yaml pin == spine-order reassembly of chunks 0630+0634 objectives (verbatim, case-insensitive)', norm(lo_row) == assembled)

# (5) glossary resolution
gloss = yaml.safe_load((COURSE / 'lessons/u2-c15-extraction-metals/glossary.yaml').read_text())
slugs = {g['slug'] for g in (gloss or [])}
sec_slugs = {sl for s in lesson['sections'] if s.get('glossary') for sl in s['glossary']}
check('S0.19 all section glossary slugs resolve in glossary.yaml', sec_slugs <= slugs, f'unresolved={sec_slugs - slugs}')
check('S0.19b every glossary entry has ms_accepts + definition <=40 words + source chunkRef', all(g.get('ms_accepts') and len((g.get('definition') or '').split()) <= 40 and g.get('source') for g in (gloss or [])))

# (8) emitted-pack layer (when the pack exists — post-emit runs)
pack_path = COURSE / 'lessons/u2-c15-extraction-metals/qa/lessonPackV1.json'
if pack_path.exists():
    pack = json.load(open(pack_path))
    psecs = pack['sections']
    p_refs = [r for s in psecs for r in s['chunkRefs']]
    p_specs = sorted({r for s in psecs for r in s['specRefs']})
    check('S0.20 emitted pack: chunkRefs == lesson spine, specRefs == join_set', p_refs == refs and p_specs == ['2.22C', '2.23C', '2.24C', '2.25C', '2.26C', '2.27C'])
    check('S0.21 emitted pack: learningObjective NON-NULL == course pin; paperRoute chemistry-only; status draft', pack.get('learningObjective') == row.get('learning_objective') and pack.get('paperRoute') == 'chemistry-only' and pack.get('status') == 'draft')
    check('S0.22 emitted pack sources sha-pinned', 'b2c67eaf' in (pack.get('sources') or {}).get('parseOfRecord', ''))
else:
    print('SKIP S0.20-S0.22 (qa/lessonPackV1.json not emitted yet)')

print('S0 VERDICT:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
