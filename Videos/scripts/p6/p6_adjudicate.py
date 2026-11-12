#!/usr/bin/env python3
"""P6 step 4: title-to-spec adjudication under the tightened binding rule.

Deterministic pre-pass (the distinctive-token gate): a spec binds only if the
title's matched tokens include a token that is distinctive for that spec
(in-course document frequency <= 3 across SPEC_POINTs) — generic physics words
alone ('energy', 'force', 'wave') can never bind. Confidence: medium when >= 2
distinctive tokens match (or 1 distinctive + the spec's head noun matches),
low for a single distinctive-token partial; high is never assigned (title-only
posture). At most two specs per row, the second only when independently
distinctive. Videos that clear no candidates or fail the gate go to the reject
ledger with a reason. The agent's judgment pass reviews this output afterwards
(drops/trims recorded in the assemble step)."""
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
    cands = json.load(open(f'{OUT}/candidates-{course}.json'))
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    node_by_code = {n['code']: n for n in cur['nodes']}
    specs = [n for n in cur['nodes'] if n['family'] == 'SPEC_POINT']
    spec_by = {sp['code']: sp for sp in specs}

    # in-course document frequency of every token across spec docs
    docs = {}
    for sp in specs:
        parts = [sp['title']]
        for pc in sp.get('parents', []):
            pn = node_by_code.get(pc)
            if pn:
                parts.append(pn['title'])
                for pc2 in pn.get('parents', []):
                    pn2 = node_by_code.get(pc2)
                    if pn2:
                        parts.append(pn2['title'])
        docs[sp['code']] = set(toks(' '.join(parts)))
    df = collections.Counter()
    for d in docs.values():
        df.update(d)

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
            if not matched:
                continue
            # head-noun check: does the title contain the spec title's last noun?
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
        ev = "; ".join(
            f"{b['code']} '{b['spec_title'][:46]}' via distinctive token(s) {', '.join(b['matched'][:4])}"
            for b in bound)
        rows.append({'video': vid, 'specs': specs_out, 'confidence': confidence,
                     'evidence': f"title '{title[:70]}' -> {ev}"})
    out = {'course': course, 'rows': rows, 'rejects': rejects}
    json.dump(out, open(f'{OUT}/adjudication-{course}.json', 'w'), indent=1)
    print(f'{course}: rows {len(rows)} (M{sum(1 for r in rows if r["confidence"]=="medium")}/'
          f'L{sum(1 for r in rows if r["confidence"]=="low")}) rejects {len(rejects)}')
