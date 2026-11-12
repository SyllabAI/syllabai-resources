#!/usr/bin/env python3
"""P6 step 3: for each routed video, generate the top-K SPEC_POINT candidates
from its course's content-plane spine (idf token overlap, parents as context).
Output feeds the adjudication pass."""
import json, math, re, os, collections

HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p6'
K = 8

STOP = set("""a an the of and or to in on for with without into from by at as is are be been being it its
this that these those how what why when which who whom do does did done can could should would will shall
may might must not no nor if then than so such about above below between during before after under over
again further once here there all any both each few more most other some own same too very just also
gcse physics maths math level cie edexcel aqa ocr igcse part vs using use used
new explain explained revision intro introduction basics basic lesson episode worked example examples
calculate calculating""".split())

def toks(s):
    return [t[:-1] if len(t) > 3 and t.endswith('s') else t
            for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP and len(t) > 1]

pool = json.load(open(f'{OUT}/target-pool.json'))
by_course = collections.defaultdict(list)
for p in pool:
    by_course[p['course']].append(p)

for course, vids in sorted(by_course.items()):
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    node_by_code = {n['code']: n for n in cur['nodes']}
    specs = [n for n in cur['nodes'] if n['family'] == 'SPEC_POINT']

    def context(spec):
        parts = []
        for pc in spec.get('parents', []):
            pn = node_by_code.get(pc)
            if pn:
                parts.append(pn['title'])
                for pc2 in pn.get('parents', []):
                    pn2 = node_by_code.get(pc2)
                    if pn2:
                        parts.append(pn2['title'])
        return parts

    docs = {}
    for sp in specs:
        docs[sp['code']] = toks(sp['title'] + ' ' + ' '.join(context(sp)))
    df = collections.Counter(t for d in docs.values() for t in set(d))
    idf = {t: math.log(N / df[t]) for N, df in [(len(docs), collections.Counter(t for d in docs.values() for t in set(d)))][1:]}
    # recompute properly (clarity over cleverness)
    df = collections.Counter()
    for d in docs.values():
        df.update(set(d))
    N = len(docs)
    idf = {t: math.log(N / df[t]) for t in df}

    cands = {}
    for v in vids:
        q = set(toks(v['title']))
        scored = []
        for code, d in docs.items():
            s = sum(idf[t] for t in q & set(d))
            if s > 0:
                scored.append((s, code, q & set(d)))
        scored.sort(reverse=True)
        sp_by = {sp['code']: sp for sp in specs}
        if scored:
            best = scored[0][0]
            cands[v['id']] = [
                {'code': c, 'title': sp_by[c]['title'], 'score': round(s, 2),
                 'matched': sorted(mt), 'context': ' > '.join(dict.fromkeys(context(sp_by[c])))}
                for s, c, mt in scored[:K] if s >= 0.3 * best
            ]
        else:
            cands[v['id']] = []

    json.dump(cands, open(f'{OUT}/candidates-{course}.json', 'w'), indent=1)
    n_empty = sum(1 for c in cands.values() if not c)
    print(f'{course}: {len(vids)} videos -> candidates written | empty {n_empty}')
