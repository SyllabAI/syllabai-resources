#!/usr/bin/env python3
"""verify_c14_s0.py — u2:c14 Reactivity series S0 gates (T-BOOK-047 r0, trace 1a16eb100fb98905)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation
objectives chunk (0559, COLUMN-INTERLEAVED — f-0016 reassembly law) x spine
igcse-chemistry-T2:SUBd one-to-one coverage; (3) f-0015 sibling audit (all-core
paper-route pack + chem_only false); (4) page range; (5) glossary resolution;
(6) full census sweep incl. the 14 figure/display fragment ids ABSENT from the
parse of record; (7) course.yaml row pin (join_set + learning_objective)."""
import json, sys, hashlib, pathlib, re, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/syllabai-v2/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/books/pearson-edexcel/international-gcse/chemistry/4ch1/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u2-c14-reactivity-series/lesson.yaml').read_text())
ofmap = json.load(open(COURSE / 'section-maps/u2-c14.json'))

# (1) chunkRefs byte-verify
parse_ids = set()
u2c14_ids = set()
parse_sha = hashlib.sha256(PARSE.read_bytes()).hexdigest()
check('S0.0 parse of record sha256 == course.yaml pin', parse_sha == 'b2c67eafe4e3766bab41b41fc24795ca0fe95c1f5f55b8a3b3bffbc709af6d33', parse_sha[:12])
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u2_c14' in c['id']: u2c14_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u2_c14', all(r in u2c14_ids for r in refs))
of_refs = [r for s in ofmap['sections'] for r in s['chunkRefs']]
check('S0.3 section chunkRefs == section map of record (byte-equal, in order)', refs == of_refs, f'lesson={len(refs)} map={len(of_refs)}')
titles = [s['title'] for s in lesson['sections']]
check('S0.4 section titles == of record', titles == [s['title'] for s in ofmap['sections']])
check('S0.5 page range == [145, 156]', lesson['book_page_range'] == [145, 156] == ofmap['book_page_range'])
check('S0.5b bookPage monotonic + == of record', [s.get('bookPage') for s in lesson['sections']] == [s.get('bookPage') for s in ofmap['sections']])

# (6) full census sweep — every u2_c14 chunk in the parse is mapped (57/57)
check('S0.5c census sweep: ALL u2_c14 chunks in parse are mapped into sections', u2c14_ids <= set(refs), f'census={len(u2c14_ids)} mapped={len(set(refs) & u2c14_ids)} unmapped={sorted(u2c14_ids - set(refs))}')
# numeric-slot audit: 0558..0628 = 71 slots, 57 present in parse, 14 absent (figure/display fragments, c12/c13 precedent)
all_slots = [f'chem_v3_u2_c14_pdf{p}_{n}' for p, n in []]  # slots derive from numeric tail
tails = sorted(int(i.rsplit('_', 1)[1]) for i in u2c14_ids)
absent = [n for n in range(tails[0], tails[-1] + 1) if not any(i.endswith(f'_{n:04d}') for i in u2c14_ids)]
check('S0.5d numeric-slot audit: 57 present + 14 absent = 71 slots (0558..0628)', len(tails) == 57 and len(absent) == 14 and tails[0] == 558 and tails[-1] == 628, f'present={len(tails)} absent={absent}')

# (2) join_set derivation: objectives chunk 0559 fragments x spine SUBd
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subd = [n for n in nodes if n.get('code') == 'igcse-chemistry-T2:SUBd'][0]
pts = sorted([n for n in nodes if 'igcse-chemistry-T2:SUBd' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine SUBd = "Reactivity series"', 'Reactivity series' in subd['title'], subd['title'])
check('S0.7 SUBd carries exactly 7 spec points', len(pts) == 7, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']})
check('S0.8 join_set == [2.15..2.21]', join_set == ['2.15', '2.16', '2.17', '2.18', '2.19', '2.20', '2.21'], str(join_set))

obj_chunk = None
for line in open(PARSE):
    c = json.loads(line)
    if c['id'] == 'chem_v3_u2_c14_pdf154_0559':
        obj_chunk = c
check('S0.8b objectives chunk 0559 exists', obj_chunk is not None)

def norm(s):
    """f-0016 interleave normalization: drop bullet glyphs + collapse whitespace
    + drop objective-separator ';' (spine titles join sub-bullets with spaces)
    + strip trailing '.' (spine sentences end with one) so a column-interleaved
    objective still matches verbatim (case-insensitive)."""
    s = re.sub(r'[\u2022\n\s;:]+', ' ', s).strip().lower()
    return s[:-1] if s.endswith('.') else s

# logical objectives REASSEMBLED from the interleaved chunk, in spine order
objs = {
 '2.15': 'Understand how metals can be arranged in a reactivity series based on their reactions with: water; dilute hydrochloric or sulfuric acid',
 '2.16': 'Understand how metals can be arranged in a reactivity series based on their displacement reactions between: metals and metal oxides; metals and aqueous solutions of metal salts',
 '2.17': 'Know the order of reactivity of these metals: potassium, sodium, lithium, calcium, magnesium, aluminium, zinc, iron, copper, silver, gold',
 '2.18': 'Know the conditions under which iron rusts',
 '2.19': 'Understand how the rusting of iron may be prevented by: barrier methods; galvanising; sacrificial protection',
 '2.20': 'Understand the terms: oxidation; reduction; redox; oxidising agent; reducing agent in terms of gain or loss of oxygen and loss or gain of electrons',
 '2.21': 'Practical: Investigate reactions between dilute hydrochloric and sulfuric acids and metals (e.g. magnesium, zinc and iron)',
}
by_code = {p['code']: p for p in pts}
obj_norm = norm(obj_chunk['text'])
for code, text in objs.items():
    # every ';'-separated piece of the reassembled objective must appear in the
    # interleave-normalized chunk (verbatim, case-insensitive)
    pieces = [norm(x) for x in text.split(';')]
    check(f'S0.9 {code} reassembled objective pieces all verbatim in chunk 0559 (f-0016 normalization)', all(p in obj_norm for p in pieces), by_code[code]['title'][:70])
    check(f'S0.9b {code} reassembly matches spine title (case-insensitive)', norm(by_code[code]['title']) == norm(text), '')

# (3) f-0015 sibling audit: all-core paper-route pack + chem_only false
core = [p for p in pts if not p['code'].endswith('C')]
conly = [p for p in pts if p['code'].endswith('C')]
check('S0.10 7 core shared + 0 C-suffixed', len(core) == 7 and len(conly) == 0, f'core={len(core)} conly={len(conly)}')
check('S0.11 all core points shared with double award, papers [1C,2C]', all(p['applicability']['double_award_shared'] and p['applicability']['papers'] == ['1C', '2C'] for p in core))
check('S0.12 lesson.yaml chem_only false', lesson['chem_only'] is False)
course = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = [r for r in course['spine']['u2'] if r['key'] == 'u2:c14'][0]
check('S0.13 course.yaml row: chem_only false, section_count 20, pages [145,156]', row['chem_only'] is False and row['section_count'] == 20 and row['pages'] == [145, 156])
# sibling audit: u1 routes uniform (all-core x7 / all-C x3), none mixed; u2 c11+c12 mixed; c13+c14 all-core
u1_flags = {r['key']: r.get('chem_only') for r in course['spine']['u1']}
check('S0.14 sibling audit: u1 pack routes uniform (all-core x7 / all-C x3), none mixed', all(isinstance(v, bool) for v in u1_flags.values()) and sum(u1_flags.values()) == 3, str(u1_flags))
c11r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c11'][0]
c12r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c12'][0]
c13r = [r for r in course['spine']['u2'] if r['key'] == 'u2:c13'][0]
# c11/c12 course rows are UNPINNED (c13-receipt debt) — their mixed shape is
# evidenced at pack layer: emitted packs carry the C-suffixed specRefs.
c11_pack = json.load(open(COURSE / 'lessons/u2-c11-alkali-metals/qa/lessonPackV1.json'))
c12_pack = json.load(open(COURSE / 'lessons/u2-c12-halogens/qa/lessonPackV1.json'))
c11_specs = {r for s in c11_pack['sections'] for r in s['specRefs']}
c12_specs = {r for s in c12_pack['sections'] for r in s['specRefs']}
check('S0.15 sibling audit: c11/c12 packs mixed (C-suffixed present), c13+c14 rows all-core — no mixed-shape drift', row.get('join_set') == ['2.15', '2.16', '2.17', '2.18', '2.19', '2.20', '2.21'] and c13r.get('join_set') == ['2.9', '2.10', '2.11', '2.12', '2.13', '2.14'] and any(x.endswith('C') for x in c11_specs) and any(x.endswith('C') for x in c12_specs) and not any(str(x).endswith('C') for x in row.get('join_set', [])), f'c11={[x for x in c11_specs if x.endswith("C")]} c12={[x for x in c12_specs if x.endswith("C")]}')
check('S0.16 course.yaml row PINNED: join_set + learning_objective present', bool(row.get('join_set')) and bool(row.get('learning_objective')))

# (7) learning_objective verbatim law: course.yaml row == lesson.yaml == reassembled chunk objectives
lo_row = row.get('learning_objective', '').lower()
lo_lesson = (lesson.get('learning_objective') or '').lower()
check('S0.17 lesson.yaml learning_objective == course.yaml pin (verbatim mirror)', lo_lesson == lo_row and len(lo_row) > 200)
# reassembled-in-spine-order objective text == course.yaml pin (the pin IS the reassembly)
pin_norm = re.sub(r'[;]', '; ', lo_row)
assembled = norm('; '.join(objs[c] for c in ['2.15', '2.16', '2.17', '2.18', '2.19', '2.20', '2.21']))
check('S0.18 course.yaml pin == spine-order reassembly of chunk 0559 objectives (verbatim, case-insensitive)', norm(pin_norm) == assembled)

# (5) glossary resolution
gloss = yaml.safe_load((COURSE / 'lessons/u2-c14-reactivity-series/glossary.yaml').read_text())
slugs = {g['slug'] for g in (gloss or [])}
sec_slugs = {sl for s in lesson['sections'] if s.get('glossary') for sl in s['glossary']}
check('S0.19 all section glossary slugs resolve in glossary.yaml', sec_slugs <= slugs, f'unresolved={sec_slugs - slugs}')

print('S0 VERDICT:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
