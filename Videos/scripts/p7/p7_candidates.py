#!/usr/bin/env python3
"""P7 step 2+3: top-K SPEC_POINT candidates per routed video (idf token overlap
against the course spine) + the deterministic distinctive-token binding pre-pass.
Faithful port of the P6 machinery, parameterized by the P7 work dir."""
import json, math, re, os, collections

HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p7'
K = 8

STOP = set("""a an the of and or to in on for with without into from by at as is are be been being it its
this that these those how what why when which who whom do does did done can could should would will shall
may might must not no nor if then than so such about above below between during before after under over
again further once here there all any both each few more most other some own same too very just also
gcse science sciences maths math level cie edexcel aqa ocr igcse part vs using use used
new explain explained revision intro introduction basics basic lesson episode worked example examples
calculate calculating required practical practicals triple higher foundation paper biology chemistry
physics freesciencelessons amoeba sisters malmesbury education doodle doodlescience year""".split())

def toks(s):
    return [t[:-1] if len(t) > 3 and t.endswith('s') else t
            for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP and len(t) > 1]

pool = json.load(open(f'{OUT}/target-pool.json'))
by_course = collections.defaultdict(list)
for p in pool:
    by_course[p['course']].append(p)

def spine(course):
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    nb = {n['code']: n for n in cur['nodes']}
    specs = [n for n in cur['nodes'] if n['family'] == 'SPEC_POINT']
    def context(sp):
        parts = []
        for pc in sp.get('parents', []):
            pn = nb.get(pc)
            if pn:
                parts.append(pn['title'])
                for pc2 in pn.get('parents', []):
                    pn2 = nb.get(pc2)
                    if pn2: parts.append(pn2['title'])
        return parts
    docs = {sp['code']: toks(sp['title'] + ' ' + ' '.join(context(sp))) for sp in specs}
    df = collections.Counter()
    for d in docs.values(): df.update(set(d))
    N = len(docs)
    idf = {t: math.log(N / df[t]) for t in df}
    return specs, docs, df, idf, context

# ---- step 2: candidates
for course, vids in sorted(by_course.items()):
    specs, docs, df, idf, context = spine(course)
    sp_by = {sp['code']: sp for sp in specs}
    cands = {}
    for v in vids:
        q = set(toks(v['title']))
        scored = []
        for code, d in docs.items():
            s = sum(idf[t] for t in q & set(d))
            if s > 0: scored.append((s, code, q & set(d)))
        scored.sort(reverse=True)
        if scored:
            best = scored[0][0]
            cands[v['id']] = [
                {'code': c, 'title': sp_by[c]['title'], 'score': round(s, 2),
                 'matched': sorted(mt), 'context': ' > '.join(dict.fromkeys(context(sp_by[c])))}
                for s, c, mt in scored[:K] if s >= 0.3 * best]
        else:
            cands[v['id']] = []
    json.dump(cands, open(f'{OUT}/candidates-{course}.json', 'w'), indent=1)
    print(f'{course}: {len(vids)} videos -> candidates | empty {sum(1 for c in cands.values() if not c)}')

# ---- step 3: deterministic binding pre-pass (distinctive-token gate df<=3)
print()
total_rows = 0
for course, vids in sorted(by_course.items()):
    cands = json.load(open(f'{OUT}/candidates-{course}.json'))
    specs, docs, df, idf, context = spine(course)
    spec_by = {sp['code']: sp for sp in specs}
    rows, rejects = [], []
    for v in vids:
        vid, title = v['id'], v['title']
        cl = cands.get(vid) or []
        if not cl:
            rejects.append({'video': vid, 'reason': 'no candidate named the title content (idf overlap empty)'})
            continue
        q = set(toks(title))
        bound = []
        for c in cl:
            matched = [t for t in c['matched'] if df.get(t, 99) <= 3]
            if not matched: continue
            spec_head = re.findall(r"[a-z0-9]+", spec_by[c['code']]['title'].lower())
            head_hit = bool(set(spec_head[-2:]) & q)
            conf = 'medium' if (len(matched) >= 2 or head_hit) else 'low'
            bound.append({'code': c['code'], 'conf': conf, 'matched': matched,
                          'spec_title': spec_by[c['code']]['title']})
        if not bound:
            best = cl[0]
            rejects.append({'video': vid,
                            'reason': f'best candidate "{best["title"][:60]}" ({best["code"]}) binds only on generic vocabulary: {", ".join(best["matched"][:6])}'})
            continue
        bound = bound[:2] if len(bound) > 1 else bound
        if len(bound) == 2:
            confs = [b['conf'] for b in bound]
            confidence = 'medium' if confs[0] == 'medium' else 'low'
        else:
            confidence = bound[0]['conf']
        specs_out = [b['code'] for b in bound]
        ev = "; ".join(f"{b['code']} '{b['spec_title'][:46]}' via distinctive token(s) {', '.join(b['matched'][:4])}" for b in bound)
        rows.append({'video': vid, 'specs': specs_out, 'confidence': confidence,
                     'evidence': f"title '{title[:70]}' -> {ev}", 'title': title})
    json.dump({'course': course, 'rows': rows, 'rejects': rejects},
              open(f'{OUT}/adjudication-{course}.json', 'w'), indent=1)
    total_rows += len(rows)
    print(f'{course}: rows {len(rows)} (M{sum(1 for r in rows if r["confidence"]=="medium")}/L{sum(1 for r in rows if r["confidence"]=="low")}) rejects {len(rejects)}')
print(f'TOTAL pre-pass rows: {total_rows}')
