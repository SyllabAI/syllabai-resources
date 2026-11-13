#!/usr/bin/env python3
"""P10 step 2: distinctive-token pre-pass (the P9 candidates shape, plus a
cross-course best-of for the 3 ambiguous Maths Deity rows)."""
import json, math, re, os, collections

HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p10'
K = 8

STOP = set("""a an the of and or to in on for with without into from by at as is are be been being it its
this that these those how what why when which who whom do does did done can could should would will shall
may might must not no nor if then than so such about above below between during before after under over
again further once here there all any both each few more most other some own same too very just also
maths math level cie edexcel aqa ocr igcse ial solomon paper part vs using use used
new explain explained revision intro introduction basics basic lesson episode worked example examples
calculate calculating chapter unit page question questions june january october november march exam
text book textbook tutorial need even learn pt""".split())

def toks(s):
    return [t[:-1] if len(t) > 3 and t.endswith('s') else t
            for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP and len(t) > 1]

pool = json.load(open(f'{OUT}/tier-a.json'))
by_course = collections.defaultdict(list)
for p in pool:
    if p.get('course'):
        by_course[p['course']].append(p)

def course_ctx(course):
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
    df = collections.Counter()
    for d in docs.values():
        df.update(set(d))
    N = len(docs)
    idf = {t: math.log(N / df[t]) for t in df}
    return cur, specs, docs, df, idf

def score(q, docs, df, idf, specs):
    sp_by = {sp['code']: sp for sp in specs}
    scored = []
    for code, d in docs.items():
        inter = q & set(d)
        s = sum(idf[t] for t in inter)
        if s > 0:
            mind = min(df[t] for t in inter)
            scored.append((s, code, sorted(inter), mind))
    scored.sort(reverse=True)
    lst = []
    if scored:
        best = scored[0][0]
        for s, c, mt, mind in scored[:K]:
            if s < 0.3 * best:
                continue
            lst.append({'code': c, 'title': sp_by[c]['title'], 'score': round(s, 2),
                        'matched': mt, 'minDf': mind,
                        'distinctive': mind <= 3,
                        'context': ' > '.join([])})
    return lst

for course, vids in sorted(by_course.items()):
    cur, specs, docs, df, idf = course_ctx(course)
    cands = {}
    for v in vids:
        q = set(toks(v['title']))
        cands[v['id']] = score(q, docs, df, idf, specs)
    json.dump(cands, open(f'{OUT}/candidates-{course}.json', 'w'), indent=1)
    n_empty = sum(1 for c in cands.values() if not c)
    wd = sum(1 for c in cands.values() if any(x['distinctive'] for x in c))
    print(f'{course}: {len(vids)} videos | empty {n_empty} | with-distinctive {wd}')

# ambiguous rows: cross-course best-of over the four IAL pure courses
amb = [p for p in pool if p.get('course') is None]
cc = {}
for course in ('ial-maths-20-pure-1', 'ial-maths-20-pure-2', 'ial-maths-20-pure-3', 'ial-maths-20-pure-4'):
    cur, specs, docs, df, idf = course_ctx(course)
    cc[course] = (docs, df, idf, specs)
amb_out = {}
for p in amb:
    q = set(toks(p['title']))
    best = None
    for course, (docs, df, idf, specs) in cc.items():
        for x in score(q, docs, df, idf, specs):
            if best is None or x['score'] > best['score']:
                x = dict(x)
                x['course'] = course
                best = x
    amb_out[p['id']] = [best] if best and best['distinctive'] else []
    print('AMB', p['title'][:52], '->', (best['course'], best['code']) if amb_out[p['id']] else 'none')
json.dump(amb_out, open(f'{OUT}/candidates-ambiguous.json', 'w'), indent=1)
