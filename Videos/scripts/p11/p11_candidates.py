#!/usr/bin/env python3
"""P11 step 2: distinctive-token pre-pass (the P9/P10 candidates shape,
generalized to course-list routing: one (course, video) scoring per routed
pair; candidates keyed per course by video id)."""
import json, math, re, os, collections

HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p11'
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

tierA = json.load(open(f'{OUT}/tier-a.json'))
pairs = collections.defaultdict(set)  # course -> {video ids}
vidmeta = {}
for p in tierA:
    vidmeta[p['id']] = p
    for c in p['courses']:
        pairs[c].add(p['id'])

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

for course in sorted(pairs):
    cur, specs, docs, df, idf = course_ctx(course)
    cands = {}
    for vid in pairs[course]:
        q = set(toks(vidmeta[vid]['title']))
        cands[vid] = score(q, docs, df, idf, specs)
    json.dump(cands, open(f'{OUT}/candidates-{course}.json', 'w'), indent=1)
    n_empty = sum(1 for c in cands.values() if not c)
    wd = sum(1 for c in cands.values() if any(x['distinctive'] for x in c))
    print(f'{course}: {len(cands)} videos | empty {n_empty} | with-distinctive {wd}')
