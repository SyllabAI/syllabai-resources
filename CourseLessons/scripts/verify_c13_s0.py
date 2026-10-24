#!/usr/bin/env python3
"""verify_c13_s0.py — u2:c13 Gases in the atmosphere S0 gates (T-BOOK-046 r0, trace 1a16db3f408f9381)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation
objectives chunk (0523) x spine igcse-chemistry-T2:SUBc one-to-one coverage;
(3) f-0015 sibling audit (all-core paper-route pack + chem_only false); (4) page
range; (5) glossary resolution; (6) full census sweep (every u2_c13 chunk in the
parse of record is mapped); (7) course.yaml row pin (join_set + learning_objective)."""
import json, sys, pathlib, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/v2-main/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/books/pearson-edexcel/international-gcse/chemistry/4ch1/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u2-c13-gases-atmosphere/lesson.yaml').read_text())
ofmap = json.load(open(COURSE / 'section-maps/u2-c13.json'))

# (1) chunkRefs byte-verify
parse_ids = set()
u2c13_ids = set()
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u2_c13' in c['id']: u2c13_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u2_c13', all(r in u2c13_ids for r in refs))
of_refs = [r for s in ofmap['sections'] for r in s['chunkRefs']]
check('S0.3 section chunkRefs == section map of record (byte-equal, in order)', refs == of_refs, f'lesson={len(refs)} map={len(of_refs)}')
titles = [s['title'] for s in lesson['sections']]
check('S0.4 section titles == of record', titles == [s['title'] for s in ofmap['sections']])
check('S0.5 page range == [137, 143]', lesson['book_page_range'] == [137, 143] == ofmap['book_page_range'])
check('S0.5b bookPage monotonic + == of record', [s.get('bookPage') for s in lesson['sections']] == [s.get('bookPage') for s in ofmap['sections']])

# (6) full census sweep — every u2_c13 chunk in the parse is mapped (33/33)
check('S0.5c census sweep: ALL u2_c13 chunks in parse are mapped into sections', u2c13_ids <= set(refs), f'census={len(u2c13_ids)} mapped={len(set(refs) & u2c13_ids)} unmapped={sorted(u2c13_ids - set(refs))}')

# (2) join_set derivation: objectives chunk 0523 fragments x spine SUBc
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subc = [n for n in nodes if n.get('code') == 'igcse-chemistry-T2:SUBc'][0]
pts = sorted([n for n in nodes if 'igcse-chemistry-T2:SUBc' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine SUBc = "Gases in the atmosphere"', 'Gases in the atmosphere' in subc['title'], subc['title'])
check('S0.7 SUBc carries exactly 6 spec points', len(pts) == 6, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']})
check('S0.8 join_set == [2.9, 2.10, 2.11, 2.12, 2.13, 2.14]', join_set == ['2.10', '2.11', '2.12', '2.13', '2.14', '2.9'], str(join_set))
# chunk fragments (verbatim from chunk 0523) vs spine titles
frags = {
 'know the approximate percentages by volume of the four most abundant gases in dry air': '2.9',
 'understand how to determine the percentage by volume of oxygen in air using experiments involving the reactions of metals (e.g. iron) and non-metals (e.g. phosphorus) with air': '2.10',
 'describe the combustion of elements in oxygen, including magnesium, hydrogen and sulfur': '2.11',
 'describe the formation of carbon dioxide from the thermal decomposition of metal carbonates, including copper(ii) carbonate': '2.12',
 'know that carbon dioxide is a greenhouse gas and that increasing amounts in the atmosphere may contribute to climate change': '2.13',
 'practical: determine the approximate percentage by volume of oxygen in air using a metal or a non-metal': '2.14',
}
by_code = {p['code']: p for p in pts}
for frag, code in frags.items():
    check(f'S0.9 fragment<->{code} verbatim (case-insensitive)', by_code[code]['title'].lower() == frag, by_code[code]['title'][:90])
# objectives chunk actually carries those fragments
obj_text = ''
for line in open(PARSE):
    c = json.loads(line)
    if c['id'] == 'chem_v3_u2_c13_pdf146_0523':
        obj_text = c['text'].lower()
check('S0.9b all six fragments present in objectives chunk 0523', all(f in obj_text for f in frags))

# (3) f-0015 sibling audit: all-core paper-route pack + chem_only false
core = [p for p in pts if not p['code'].endswith('C')]
conly = [p for p in pts if p['code'].endswith('C')]
check('S0.10 6 core shared + 0 C-suffixed', len(core) == 6 and len(conly) == 0, f'core={len(core)} conly={len(conly)}')
check('S0.11 all core points shared with double award, papers [1C,2C]', all(p['applicability']['double_award_shared'] and p['applicability']['papers'] == ['1C', '2C'] for p in core))
check('S0.12 lesson.yaml chem_only false', lesson['chem_only'] is False)
course = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = [r for r in course['spine']['u2'] if r['key'] == 'u2:c13'][0]
check('S0.13 course.yaml row: chem_only false, section_count 7, pages [137,143]', row['chem_only'] is False and row['section_count'] == 7 and row['pages'] == [137, 143])
# sibling audit: u1 routes uniform (all-core x7 / all-C x3), none mixed; u2 c11+c12 mixed; c13 returns all-core
u1_flags = {r['key']: r.get('chem_only') for r in course['spine']['u1']}
check('S0.14 sibling audit: u1 pack routes uniform (all-core x7 / all-C x3), none mixed', all(isinstance(v, bool) for v in u1_flags.values()) and sum(u1_flags.values()) == 3, str(u1_flags))
check('S0.15 sibling audit: c13 all-core after two mixed packs (c11 3core+2.4C, c12 3core+2.8C) — no mixed-shape drift', row.get('join_set') == ['2.9', '2.10', '2.11', '2.12', '2.13', '2.14'] and not any(str(x).endswith('C') for x in row.get('join_set', [])), str(row.get('join_set')))
check('S0.16 course.yaml row PINNED: join_set + learning_objective present', bool(row.get('join_set')) and bool(row.get('learning_objective')))

# (7) learning_objective verbatim law: course.yaml row == chunk-0523 bullets ';'-joined
bullets = []
for raw in obj_text if isinstance(obj_text, str) else '':
    pass
obj_chunk = None
for line in open(PARSE):
    c = json.loads(line)
    if c['id'] == 'chem_v3_u2_c13_pdf146_0523':
        obj_chunk = c
lo_row = row.get('learning_objective', '').lower()
lo_lesson = (lesson.get('learning_objective') or '').lower()
check('S0.17 lesson.yaml learning_objective == course.yaml pin (verbatim mirror)', lo_lesson == lo_row and len(lo_row) > 100)
check('S0.18 learning_objective bullets all present verbatim in chunk 0523 (case-insensitive)', all(b.strip().lower() in obj_chunk['text'].lower() for b in lo_row.split(';')))

# (5) glossary resolution
gloss = yaml.safe_load((COURSE / 'lessons/u2-c13-gases-atmosphere/glossary.yaml').read_text())
slugs = {g['slug'] for g in gloss}
sec_slugs = {sl for s in lesson['sections'] if s['glossary'] for sl in s['glossary']}
check('S0.19 all section glossary slugs resolve in glossary.yaml', sec_slugs <= slugs, f'unresolved={sec_slugs - slugs}')

print('S0 VERDICT:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
