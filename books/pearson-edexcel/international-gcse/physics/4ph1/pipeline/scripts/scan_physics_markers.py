#!/usr/bin/env python3
"""Scan parsed physics pages for structural markers to refine the structure map."""
import json, glob, re, collections

pages = {}
for fp in sorted(glob.glob('/home/z/my-project/data/physics/docling_pages/page_*.json')):
    d = json.load(open(fp))
    pages[d['pdf_page']] = ' \n '.join(
        (it.get('text') or '') for it in d.get('items', []) if it.get('text'))

# 1) LEARNING OBJECTIVES pages (chapter openers)
print('=== LEARNING OBJECTIVES pages ===')
obj_pages = []
for p in sorted(pages):
    if re.search(r'LEARNING\s*OBJECTIVES', pages[p], re.I):
        obj_pages.append(p)
print(obj_pages)

# 2) chapter-question / unit-question / answers / glossary / index / appendix markers
print('\n=== other structural markers ===')
pats = {
    'CHAPTER QUESTIONS': r'CHAPTER\s+QUESTIONS',
    'UNIT QUESTIONS':    r'UNIT\s+QUESTIONS',
    'ANSWERS':           r'^ANSWERS\b|\bANSWERS\s*$',
    'GLOSSARY':          r'\bGLOSSARY\b',
    'INDEX':             r'^\s*INDEX\s*$',
    'APPENDIX':          r'\bAPPENDIX\b',
    'EXAM HINT':         r'EXAM\s+HINT',
    'WORKED EXAMPLE':    r'WORKED\s+EXAMPLE',
    'DID YOU KNOW':      r'DID\s+YOU\s+KNOW',
    'EXTENSION WORK':    r'EXTENSION\s+WORK',
    'KEY POINT':         r'KEY\s+POINTS?\b',
    'ACTIVITY':          r'^\s*ACTIVITY\b',
    'PRACTICAL':         r'\bPRACTICAL\b',
    'MATHS SKILLS':      r'MATHS\s+SKILLS',
    'HINT':              r'^\s*HINT\b',
}
hits = collections.defaultdict(list)
for p in sorted(pages):
    for name, rx in pats.items():
        if re.search(rx, pages[p], re.I | re.M):
            hits[name].append(p)
for name in pats:
    lst = hits[name]
    print(f'{name:18s} n={len(lst):3d}  first={lst[:6]} last={lst[-4:] if lst else []}')

# 3) heading census (section_header labels) to find all-caps feature headings
print('\n=== heading label census ===')
heads = collections.Counter()
for fp in sorted(glob.glob('/home/z/my-project/data/physics/docling_pages/page_*.json')):
    d = json.load(open(fp))
    for it in d.get('items', []):
        if it['label'] in ('section_header', 'section_head'):
            t = ' '.join((it.get('text') or '').split())[:48]
            if t:
                heads[t] += 1
for t, n in heads.most_common(40):
    print(f'{n:3d}  {t}')
