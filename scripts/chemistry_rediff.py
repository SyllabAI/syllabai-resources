#!/usr/bin/env python3
"""Chemistry rediff: fresh PDF-direct parse (parsed/igcse-chemistry) vs the
existing graph/igcse-chemistry/specification_points (built from raw-OCR markdown).
Outputs: code-set equality + per-code text diff quantifying OCR damage."""
import json, glob, re, difflib
import yaml

RES = '/home/z/my-project/download/syllabai-resources'

g = yaml.safe_load(open(f'{RES}/graph/igcse-chemistry/specification_points'))
graph = {}
for sp in g['specification_points']:
    graph[sp['official_code']] = {
        'text': re.sub(r'\s+', ' ', sp.get('official_wording') or '').strip(),
        'section': sp.get('section'), 'subsection': sp.get('subsection'),
    }

parsed = {}
for f in glob.glob(f'{RES}/Official-Specifications/parsed/igcse-chemistry/*.parsed.json'):
    for st in json.load(open(f))['spec_points']:
        parsed[st['official_code']] = st

g_codes, p_codes = set(graph), set(parsed)
equal_codes = g_codes == p_codes
only_g, only_p = sorted(g_codes - p_codes), sorted(p_codes - g_codes)

def wnorm(s):
    s = (s.replace('\u2019', "'").replace('\u2018', "'").replace('\u2013', '-')
          .replace('\u2014', '-').replace('\u00d7', 'x').replace('\ufb01', 'fi'))
    # OCR-md artifacts: latex math + inline bullet markers
    for ch in ('$','_','{','}','^','\u00b7','\u2022','，'):
        s = s.replace(ch, ' ')
    return re.sub(r'\s+', ' ', s).strip().lower()

diffs = []
for code in sorted(g_codes & p_codes, key=lambda c: [int(x) for x in re.findall(r'\d+', c)]):
    a = wnorm(graph[code]['text'])
    st = parsed[code]
    b = wnorm(' '.join([st['text']] + list(st.get('sub_items') or [])))
    if a == b:
        continue
    ratio = difflib.SequenceMatcher(None, a, b).ratio()
    diffs.append({'code': code, 'ratio': round(ratio, 3),
                  'graph_ocr': graph[code]['text'][:160],
                  'pdf_direct': ' '.join([st['text']] + list(st.get('sub_items') or []))[:160]})

total = len(g_codes & p_codes)
print(f'graph codes: {len(g_codes)}  parsed codes: {len(p_codes)}')
print(f'code-set equality: {equal_codes}')
if only_g: print('only in graph:', only_g)
if only_p: print('only in parsed:', only_p)
print(f'identical text: {total - len(diffs)}/{total}  '
      f'({(total - len(diffs)) / total * 100:.1f}%)')
print(f'differing: {len(diffs)}')
for d in sorted(diffs, key=lambda x: x['ratio'])[:8]:
    print(f"  {d['code']:>6} ratio={d['ratio']:.3f}")
    print(f'     OCR: {d["graph_ocr"][:110]}')
    print(f'     PDF: {d["pdf_direct"][:110]}')

out = {'generated_utc': '2026-09-17', 'graph_codes': len(g_codes),
       'parsed_codes': len(p_codes), 'code_set_equal': equal_codes,
       'only_in_graph': only_g, 'only_in_parsed': only_p,
       'text_identical': total - len(diffs), 'text_differing': len(diffs),
       'diffs': diffs}
with open(f'{RES}/Official-Specifications/parsed/chemistry-rediff.json', 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)

md = ['# Chemistry parse rediff — PDF-direct vs OCR-markdown graph', '',
      f'- Graph (`graph/igcse-chemistry/specification_points`, from raw-OCR md): **{len(g_codes)} codes**',
      f'- Fresh parse (`parsed/igcse-chemistry`, PDF text layer): **{len(p_codes)} codes**',
      f'- Code-set equality: **{"PASS" if equal_codes else "FAIL"}**'
      + (f' (only in graph: {only_g}; only in parsed: {only_p})' if (only_g or only_p) else ''),
      f'- Statement text identical (whitespace/quote-normalised): '
      f'**{total - len(diffs)}/{total} ({(total - len(diffs)) / total * 100:.1f}%)**',
      f'- Differing: {len(diffs)} (notation-level differences; OCR damage examples below)', '']
for d in sorted(diffs, key=lambda x: x['ratio'])[:15]:
    md += [f"## {d['code']} (similarity {d['ratio']:.3f})", '',
           f'- OCR md: `{d["graph_ocr"]}`', f'- PDF direct: `{d["pdf_direct"]}`', '']
with open(f'{RES}/Official-Specifications/parsed/chemistry-rediff.md', 'w') as f:
    f.write('\n'.join(md))
print('\nwrote chemistry-rediff.json / .md')
