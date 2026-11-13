#!/usr/bin/env python3
"""P9 step 1b: idf best-of routing for the 270 ambiguous Tier A titles (the P6
best_course pattern over the maths spines). Output merges into tier-a.json."""
import json, math, re, os, collections

HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p9'

CANDS = ['ial-maths-20-pure-1', 'ial-maths-20-pure-2', 'ial-maths-20-pure-3', 'ial-maths-20-pure-4',
         'ial-maths-20-mechanics-1', 'ial-maths-20-statistics-1', 'ial-maths-20-decision-1',
         'ial-further-maths-18-further-pure-1',
         'cie-a-level-maths-20-pure-1', 'cie-a-level-maths-20-pure-2', 'cie-a-level-maths-20-pure-3',
         'cie-a-level-maths-20-probability-and-statistics-1', 'cie-a-level-maths-20-probability-and-statistics-2',
         'cie-igcse-maths-25-core', 'cie-igcse-maths-25-extended',
         'igcse-maths-a-18-higher', 'igcse-maths-b-16', 'igcse-further-maths-19']

STOP = set("""a an the of and or to in on for with without into from by at as is are be been being it its
this that these those how what why when which who whom do does did done can could should would will shall
may might must not no nor if then than so such about above below between during before after under over
again further once here there all any both each few more most other some own same too very just also
maths math level cie edexcel aqa ocr igcse ial solomon paper part vs using use used
new explain explained revision intro introduction basics basic lesson episode worked example examples
calculate calculating chapter unit page question questions june january october november march exam""".split())

def toks(s):
    return [t[:-1] if len(t) > 3 and t.endswith('s') else t
            for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP and len(t) > 1]

spine_docs = {}
for course in CANDS:
    try:
        cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    except FileNotFoundError:
        continue
    nb = {n['code']: n for n in cur['nodes']}
    specs = [n for n in cur['nodes'] if n['family'] == 'SPEC_POINT']
    docs = {}
    for sp in specs:
        parts = [sp['title']]
        for pc in sp.get('parents', []):
            pn = nb.get(pc)
            if pn:
                parts.append(pn['title'])
                for pc2 in pn.get('parents', []):
                    pn2 = nb.get(pc2)
                    if pn2:
                        parts.append(pn2['title'])
        docs[sp['code']] = toks(' '.join(parts))
    df = collections.Counter()
    for d in docs.values():
        df.update(set(d))
    idf = {t: math.log(len(docs) / df[t]) for t in df}
    spine_docs[course] = {'n': len(docs), 'idf': idf, 'docs': docs}

amb = json.load(open(f'{OUT}/tier-a-ambiguous.json'))
routed, still = [], []
dist = collections.Counter()
for v in amb:
    t = v['title']
    # board restriction: never let idf cross the board boundary (P7 misbind class)
    if re.search(r'9709|CAIE', t, re.I):
        allowed = [c for c in CANDS if c.startswith('cie-')]
    elif re.search(r'IAL|Edexcel|Solomon|WMA|WME|WST|C12|C34', t, re.I):
        allowed = [c for c in CANDS if not c.startswith('cie-')]
    else:
        allowed = CANDS
    q = set(toks(t))
    scored = []
    for c in allowed:
        sd = spine_docs.get(c)
        if not sd:
            continue
        s = sum(sd['idf'][t] for t in q if t in sd['idf'])
        if s > 0:
            scored.append((s, c))
    scored.sort(reverse=True)
    if scored and scored[0][0] >= 2.0:
        best = scored[0][1]
        v2 = dict(v)
        v2['course'] = best
        v2['routeEvidence'] = f'idf best-of {scored[0][0]:.2f} vs runner-up {scored[1][0]:.2f}' if len(scored) > 1 else f'idf {scored[0][0]:.2f} (sole)'
        routed.append(v2)
        dist[best] += 1
    else:
        still.append(v['title'])

json.dump(routed, open(f'{OUT}/tier-a-ambiguous-routed.json', 'w'), indent=1)
json.dump(still, open(f'{OUT}/tier-a-still-ambiguous.json', 'w'), indent=1)
# merged tier-a
base = json.load(open(f'{OUT}/tier-a.json'))
merged = base + routed
json.dump(merged, open(f'{OUT}/tier-a.json', 'w'), indent=1)
print('routed:', len(routed), '| still ambiguous:', len(still))
print(dict(dist.most_common()))
for s in still[:15]:
    print('   STILL:', s[:100])
