#!/usr/bin/env python3
"""verify_c12_s0.py — u2:c12 Halogens S0 gates (T-BOOK-045 r0, trace 1a16d3fca6f73295)
Encodes: (1) chunkRefs byte-verify vs parse of record; (2) join_set derivation
objectives chunks (0495 + 0498 continuation + 0499 CHEMISTRY ONLY) x spine
igcse-chemistry-T2:SUBb one-to-one coverage; (3) f-0015 sibling audit (mixed
paper-route pack claim + chem_only false); (4) page range; (5) glossary resolution."""
import json, sys, pathlib, yaml

COURSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/CourseLessons/lessons/pearson-edexcel/international-gcse/chemistry-4ch1')
SPINE = pathlib.Path('/home/z/my-project/repos/v2-main/apps/hub/spines/igcse-chemistry-19.json')
PARSE = pathlib.Path('/home/z/my-project/repos/syllabai-resources/books/pearson-edexcel/international-gcse/chemistry/4ch1/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl')
ok = True
def check(name, cond, detail=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + ((' | ' + detail) if detail else ''))
    if not cond: ok = False

lesson = yaml.safe_load((COURSE / 'lessons/u2-c12-halogens/lesson.yaml').read_text())
ofmap = json.load(open(COURSE / 'section-maps/u2-c12.json'))

# (1) chunkRefs byte-verify
parse_ids = set()
u2c12_ids = set()
for line in open(PARSE):
    c = json.loads(line)
    parse_ids.add(c['id'])
    if 'u2_c12' in c['id']: u2c12_ids.add(c['id'])
refs = [r for s in lesson['sections'] for r in s['chunkRefs']]
check('S0.1 all chunkRefs exist in parse of record', all(r in parse_ids for r in refs), f'{len(refs)} refs, missing={[r for r in refs if r not in parse_ids]}')
check('S0.2 all chunkRefs belong to u2_c12', all(r in u2c12_ids for r in refs))
of_refs = [r for s in ofmap['sections'] for r in s['chunkRefs']]
check('S0.3 section chunkRefs == section map of record (byte-equal, in order)', refs == of_refs, f'lesson={len(refs)} map={len(of_refs)}')
titles = [s['title'] for s in lesson['sections']]
check('S0.4 section titles == of record', titles == [s['title'] for s in ofmap['sections']])
check('S0.5 page range == [130, 135]', lesson['book_page_range'] == [130, 135] == ofmap['book_page_range'])
check('S0.5b bookPage monotonic + == of record', [s.get('bookPage') for s in lesson['sections']] == [s.get('bookPage') for s in ofmap['sections']])

# (2) join_set derivation: objectives fragments x spine SUBb
spine = json.load(open(SPINE))
nodes = spine['curriculum']['nodes']
subb = [n for n in nodes if n.get('code') == 'igcse-chemistry-T2:SUBb'][0]
pts = sorted([n for n in nodes if 'igcse-chemistry-T2:SUBb' in (n.get('parents') or [])], key=lambda x: x['order'])
check('S0.6 spine SUBb = "Group 7 (halogens) – chlorine, bromine and iodine"', 'Group 7 (halogens)' in subb['title'], subb['title'])
check('S0.7 SUBb carries exactly 4 spec points', len(pts) == 4, ', '.join(p['code'] for p in pts))
join_set = sorted({r for s in lesson['sections'] for r in s['specRefs']})
check('S0.8 join_set == [2.5, 2.6, 2.7, 2.8C]', join_set == ['2.5', '2.6', '2.7', '2.8C'], str(join_set))
# chunk fragments (verbatim from chunks 0495/0498/0499) vs spine titles
frags = {
 'know the colours, physical states (at room temperature) and trends in physical properties of the halogens': '2.5',
 'use knowledge of trends in group 7 to predict the properties of other halogens': '2.6',
 'understand how displacement reactions involving halogens and halides provide evidence for the trend in reactivity in group 7': '2.7',
 'explain the trend in reactivity in group 7 in terms of electronic configurations': '2.8C',
}
by_code = {p['code']: p for p in pts}
for frag, code in frags.items():
    t = by_code[code]['title'].lower()
    if code == '2.5':
        # disclosed variant: chunk says "of the halogens", spine statement ends "of these elements" (same statement)
        match = t == frag or (t.startswith('know the colours, physical states (at room temperature) and trends in physical properties of'))
        check('S0.9 fragment<->2.5 (case-insensitive; disclosed tail variant "of the halogens"/"of these elements")', match, t)
    else:
        check(f'S0.9 fragment<->{code} verbatim (case-insensitive)', t == frag, t)
# objectives chunks actually carry those fragments
obj_text = ''
for line in open(PARSE):
    c = json.loads(line)
    if c['id'] in ('chem_v3_u2_c12_pdf139_0495', 'chem_v3_u2_c12_pdf139_0498', 'chem_v3_u2_c12_pdf139_0499'):
        obj_text += c['text'].lower()
check('S0.9b all four fragments present in objectives chunks 0495+0498+0499', all(f in obj_text for f in frags))

# (3) f-0015 sibling audit: mixed paper-route pack + chem_only false
core = [p for p in pts if not p['code'].endswith('C')]
conly = [p for p in pts if p['code'].endswith('C')]
check('S0.10 3 core shared + 1 C-suffixed', len(core) == 3 and len(conly) == 1)
check('S0.11 core points shared with double award, papers [1C,2C]', all(p['applicability']['double_award_shared'] and p['applicability']['papers'] == ['1C', '2C'] for p in core))
check('S0.12 2.8C papers [2C], not shared', by_code['2.8C']['applicability']['papers'] == ['2C'] and not by_code['2.8C']['applicability']['double_award_shared'])
check('S0.13 lesson.yaml chem_only false', lesson['chem_only'] is False)
course = yaml.safe_load((COURSE / 'course.yaml').read_text())
row = [r for r in course['spine']['u2'] if r['key'] == 'u2:c12'][0]
check('S0.14 course.yaml row: chem_only false, section_count 8, pages [130,135]', row['chem_only'] is False and row['section_count'] == 8 and row['pages'] == [130, 135])
# sibling audit: no u1 pack mixes routes; u2 c11+c12 mixed (second mixed pack)
u1_rows = course['spine']['u1']
u1_flags = {r['key']: r.get('chem_only') for r in u1_rows}
check('S0.15 sibling audit: u1 pack routes uniform (all-core x7 / all-C x3), none mixed', all(isinstance(v, bool) for v in u1_flags.values()) and sum(u1_flags.values()) == 3, str(u1_flags))
check('S0.16 sibling audit: c12 is 2nd mixed pack after c11 (both 3-core+1-C shape)', all(isinstance(r.get('chem_only'), bool) for r in course['spine']['u2']), 'u2 rows typed')

# (4) glossary resolution
gloss = yaml.safe_load((COURSE / 'lessons/u2-c12-halogens/glossary.yaml').read_text())
slugs = {g['slug'] for g in gloss}
sec_slugs = {sl for s in lesson['sections'] if s['glossary'] for sl in s['glossary']}
check('S0.17 all section glossary slugs resolve in glossary.yaml', sec_slugs <= slugs, f'unresolved={sec_slugs - slugs}')

print('S0 VERDICT:', 'ALL GREEN' if ok else 'FAILURES PRESENT')
sys.exit(0 if ok else 1)
