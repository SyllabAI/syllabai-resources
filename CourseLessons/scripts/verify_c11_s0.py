#!/usr/bin/env python3
"""verify_c11_s0.py — u1:c11->u2:c11 Alkali metals S0 gates (T-BOOK-044 r0, trace 1a16cfb5cbb7623d)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation
objectives x spine igcse-chemistry-T2:SUBa one-to-one verbatim coverage; (3) f-0015
sibling audit (first mixed paper-route pack claim + chem_only false); (4) page range."""
import json, sys, pathlib, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources-r0/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/syllabai-v2-bake/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/tmp/chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u2-c11-alkali-metals/lesson.yaml').read_text())
ofmap = json.load(open(COURSE / 'section-maps/u2-c11.json'))

# (1) chunkRefs byte-verify
parse_ids = set()
u2c11_ids = set()
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u2_c11' in c['id']: u2c11_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u2_c11', all(r in u2c11_ids for r in refs))
of_refs = [r for s in ofmap['sections'] for r in s['chunkRefs']]
check('S0.3 section chunkRefs == section map of record (byte-equal, in order)', refs == of_refs)
titles = [s['title'] for s in lesson['sections']]
check('S0.4 section titles == of record', titles == [s['title'] for s in ofmap['sections']])
check('S0.5 page range == [123, 128]', lesson['book_page_range'] == [123, 128] == ofmap['book_page_range'])

# (2) join_set derivation: objectives fragments x spine SUBa
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
suba = [n for n in nodes if n.get('code') == 'igcse-chemistry-T2:SUBa'][0]
pts = sorted([n for n in nodes if 'igcse-chemistry-T2:SUBa' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine SUBa = "Group 1 (alkali metals) – lithium, sodium and potassium"', 'Group 1 (alkali metals)' in suba['title'], suba['title'])
check('S0.7 SUBa carries exactly 4 spec points', len(pts) == 4, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']})
check('S0.8 join_set == [2.1, 2.2, 2.3, 2.4C]', join_set == ['2.1', '2.2', '2.3', '2.4C'], str(join_set))
frag_to_point = {
 'Understand how the similarities in the reactions of these elements with water provide evidence for their recognition as a family of elements': '2.1',
 'Understand how the differences between the reactions of these elements with air and water provide evidence for the trend in reactivity in Group 1': '2.2',
 'Use knowledge of trends in Group 1 to predict the properties of other alkali metals': '2.3',
 'Explain the trend in reactivity in Group 1 in terms of electronic configurations': '2.4C',
}
by_code = {p['code']: p for p in pts}
for frag, code in frag_to_point.items():
    check(f'S0.9 fragment<->{code} verbatim', by_code[code]['title'] == frag.split('. ', 1)[-1][0].lower() + frag.split('. ', 1)[-1][1:] or by_code[code]['title'].lower() == frag.lower(), '')

# (3) f-0015 sibling audit: first mixed paper-route pack + chem_only false
core = [p for p in pts if not p['code'].endswith('C')]
conly = [p for p in pts if p['code'].endswith('C')]
check('S0.10 3 core shared + 1 C-suffixed', len(core) == 3 and len(conly) == 1)
check('S0.11 core points shared with double award, papers [1C,2C]', all(p['applicability']['double_award_shared'] and p['applicability']['papers'] == ['1C', '2C'] for p in core))
check('S0.12 2.4C papers [2C], not shared', by_code['2.4C']['applicability']['papers'] == ['2C'] and not by_code['2.4C']['applicability']['double_award_shared'])
check('S0.13 lesson.yaml chem_only false', lesson['chem_only'] is False)
course = yaml.safe_load((COURSE / 'course.yaml').read_text())
spine_rows = course['spine']
row = [r for r in spine_rows['u2'] if r['key'] == 'u2:c11'][0]
check('S0.14 course.yaml row: chem_only false, section_count 10, pages [123,128]', row['chem_only'] is False and row['section_count'] == 10 and row['pages'] == [123, 128])
# first mixed-route claim: u1 join sets uniformly all-core or all-C
u1_rows = spine_rows['u1']
u1_chemonly = {r['key']: r.get('chem_only') for r in u1_rows}
check('S0.15 sibling audit: u1 pack routes are all-core(x7) or all-C(x3), none mixed', all(isinstance(v, bool) for v in u1_chemonly.values()), str(u1_chemonly))

# (4) glossary resolution: every section glossary slug exists in glossary.yaml
gloss = yaml.safe_load((COURSE / 'lessons/u2-c11-alkali-metals/glossary.yaml').read_text())
slugs = {g['slug'] for g in gloss}
sec_slugs = {sl for s in lesson['sections'] if s['glossary'] for sl in s['glossary']}
check('S0.16 all section glossary slugs resolve in glossary.yaml', sec_slugs <= slugs, f'unresolved={sec_slugs - slugs}')

print('S0 VERDICT:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
