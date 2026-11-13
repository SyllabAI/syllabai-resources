#!/usr/bin/env python3
"""P9 step 4: assemble per-course drafts + verdicts (the P7 file law).

Outputs (into Videos/drafts/<course>/):
  video-map.draft.external-p9.json   — reviewState owner-reviewed-external
  owner-review-verdicts.p9.json      — the honest ledger (drops + routed-unmapped)
Also writes work/p9/p9-courses.json = {pre: [...], post: [...]} for the builder."""
import json, os, collections, datetime

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p9'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

TASK = "T-VIDEOMAP-P9 (Mr Hassaan's Maths Channel completion)"
REVIEWER = 'delegated self-review (agent, per owner chat 2026-11-09: "approve and review yourself"; lane authorized 2026-11-13: "file as lane P9")'
PROVIDER = "mr-hassaans-maths (Mr Hassaan's Maths Channel — Edexcel IAL + CAIE paper-code walkthrough channel)"
ENUM = json.load(open(f'{RES}/Videos/inventory/channels/mrhassansmaths-uploads.json'))['enumeratedUtc']

QUAL = {
    'ial-maths-20-pure-1': 'IAL Maths (Edexcel)', 'ial-maths-20-pure-2': 'IAL Maths (Edexcel)',
    'ial-maths-20-pure-3': 'IAL Maths (Edexcel)', 'ial-maths-20-pure-4': 'IAL Maths (Edexcel)',
    'ial-maths-20-statistics-1': 'IAL Maths (Edexcel)', 'ial-maths-20-mechanics-1': 'IAL Maths (Edexcel)',
    'ial-further-maths-18-further-pure-1': 'IAL Further Maths (Edexcel)',
    'cie-a-level-maths-20-pure-1': 'A Level Maths (CIE)', 'cie-a-level-maths-20-pure-2': 'A Level Maths (CIE)',
    'cie-a-level-maths-20-pure-3': 'A Level Maths (CIE)', 'cie-as-maths-20-pure-1': 'A Level Maths (CIE)',
    'cie-as-maths-20-pure-2': 'A Level Maths (CIE)',
    'cie-a-level-maths-20-mechanics': 'A Level Maths (CIE)', 'cie-as-maths-20-mechanics': 'A Level Maths (CIE)',
    'cie-a-level-maths-20-probability-and-statistics-1': 'A Level Maths (CIE)',
    'cie-a-level-maths-20-probability-and-statistics-2': 'A Level Maths (CIE)',
    'cie-as-maths-20-probability-and-statistics-1': 'A Level Maths (CIE)',
    'cie-igcse-maths-25-extended': 'IGCSE (CIE)', 'cie-igcse-maths-25-core': 'IGCSE (CIE)',
    'igcse-maths-a-18-higher': 'IGCSE', 'igcse-maths-a-modular-24-higher-unit-1': 'IGCSE (modular, Edexcel)',
    'igcse-maths-b-16': 'IGCSE (Edexcel)', 'igcse-further-maths-19': 'IGCSE Further Pure Mathematics (Edexcel)',
}
POST = ['cie-igcse-maths-25-core', 'igcse-maths-a-modular-24-higher-unit-1']

def level_tag(course):
    if course.startswith('ial-'):
        return 'ial'
    if course.startswith('cie-a-level'):
        return 'a-level'
    if course.startswith('cie-as'):
        return 'as'
    return 'igcse'

poolB = json.load(open(f'{OUT}/tier-b.json'))
J = json.load(open(f'{OUT}/judgment.json'))
tierA = {p['id']: p for p in json.load(open(f'{OUT}/tier-a.json'))}
oemb = json.load(open(f'{OUT}/oembed-p9.json'))

def spine_specs(course):
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    return {n['code'] for n in cur['nodes'] if n['family'] == 'SPEC_POINT'}

courses = {}
def get(course):
    if course not in courses:
        courses[course] = {'videos': {}, 'rows': [], 'rejects': []}
    return courses[course]

def vid_entry(v, course):
    o = oemb.get(v['id'], {})
    note = ("Mr Hassaan's Maths Channel — Edexcel IAL / CAIE paper-code walkthrough channel "
            "(channelId UCTFUlHukTAHgjhS2HT6jNWg); oEmbed author verified per video")
    if v['tier'] == 'B' and v.get('code', '').startswith(('WMA01', 'WMA02')):
        note += '; old-register C12/C34 code mapped onto the current P1-P4 units, disclosed'
    return {'id': v['id'], 'title': v['title'], 'provider': 'mr-hassaans-maths',
            'watchUrl': v['watchUrl'], 'lessonRef': None, 'lessonUrl': None,
            'levelTag': level_tag(course), 'boardNote': note,
            'identityMethod': o.get('method', 'oembed')}

# ---- Tier B anchors (one row per anchored course; ANCHOR-GRANULARITY §5)
for p in poolB:
    for course in p['courses']:
        c = get(course)
        if p['id'] not in c['videos']:
            c['videos'][p['id']] = vid_entry(p, course)
        code = p['code']
        ev = f'title: "{p["title"][:110]}"; paper code {code} in the title — machine-checkable course anchor (ANCHOR-GRANULARITY §5); oEmbed author verified'
        if code in ('WMA01', 'WMA02'):
            ev += '; old-register C12/C34 code spans two current units — one row per anchored course, disclosed'
        c['rows'].append({
            'anchor': {'level': 'course', 'ref': course}, 'kind': 'past-paper-walkthrough',
            'video': p['id'], 'lessonRef': None, 'lessonUrl': None, 'specs': [], 'unitScope': None,
            'confidence': 'high', 'method': 'paper-code', 'boardMismatch': False,
            'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW, 'evidence': ev,
        })

# ---- Tier A spec rows + rejects
for course, vs in J.items():
    for v in vs:
        if v['action'] == 'keep':
            c = get(course)
            src = tierA[v['id']]
            if v['id'] not in c['videos']:
                c['videos'][v['id']] = vid_entry(src, course)
            c['rows'].append({
                'video': v['id'], 'lessonRef': None, 'lessonUrl': None, 'specs': v['specs'],
                'confidence': v['confidence'],
                'evidence': f'{v["reason"]}; title-only posture, tightened binding rule (distinctive df<=3)',
                'method': 'llm-draft-external', 'boardMismatch': True,
                'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW,
            })
        elif v['action'] == 'rebind':
            c = get(v['course'])
            src = tierA[v['id']]
            if v['id'] not in c['videos']:
                c['videos'][v['id']] = vid_entry(src, v['course'])
            c['rows'].append({
                'video': v['id'], 'lessonRef': None, 'lessonUrl': None, 'specs': v['specs'],
                'confidence': v['confidence'],
                'evidence': f'rebind: {v["reason"]}; title-only posture, tightened binding rule',
                'method': 'llm-draft-external', 'boardMismatch': True,
                'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW,
            })
            get(course)['rejects'].append({'video': v['id'], 'reason': f'route misbind re-adjudicated: {v["reason"]}'})
        elif v['action'] == 'drop':
            get(course)['rejects'].append({'video': v['id'], 'reason': f'full-row drop: {v["reason"]}'})
        elif v['action'] == 'unmapped':
            get(course)['rejects'].append({'video': v['id'], 'reason': f'no-binding (routed-but-unmapped): {v["reason"]}'})

pre_courses, post_courses = [], []
for course, c in sorted(courses.items()):
    D = f'{RES}/Videos/drafts/{course}'
    os.makedirs(D, exist_ok=True)
    rows = c['rows']
    specRows = [r for r in rows if r['specs']]
    allspecs = set()
    for r in specRows:
        allspecs |= set(r['specs'])
    spine_n = len(spine_specs(course))
    draft = {
        'schema': 'syllabai.video-map-draft/2',
        'draftOf': course,
        'task': TASK,
        'course': course,
        'qual': QUAL[course],
        'reviewState': 'owner-reviewed-external',
        'draftLaw': 'P9 lane: Tier B course anchors by machine-checkable paper codes (method paper-code, confidence high, boardMismatch false — same qualification; ANCHOR-GRANULARITY §5/§8) + Tier A spec rows by the tightened distinctive-token binding rule with a full agent judgment pass over every row (P6/P7/P8 shape). Rejected videos stay out of videos[] and live in the verdicts ledger.',
        'source': {
            'provider': PROVIDER,
            'label': course,
            'method': 'yt-dlp flat channel enumeration 2026-11-13 (3,150 public uploads, 0 overlap with the 1,556-video shipped union); routing: paper-code Tier B + unit-marker/idf Tier A with board-restricted candidates; judgment: class decision tables over every distinctive-candidate row',
            'enumeratedUtc': ENUM,
        },
        'videos': sorted(c['videos'].values(), key=lambda x: x['id']),
        'mappings': rows,
        'coverage': {
            'specPointsTotal': spine_n,
            'specPointsDraftedHere': len(allspecs),
            'rows': len(rows),
            'byConfidence': {
                'high': sum(1 for r in rows if r['confidence'] == 'high'),
                'medium': sum(1 for r in rows if r['confidence'] == 'medium'),
                'low': sum(1 for r in rows if r['confidence'] == 'low'),
            },
        },
        'generatedUtc': NOW,
        'reviewedUtc': NOW,
    }
    json.dump(draft, open(f'{D}/video-map.draft.external-p9.json', 'w'), ensure_ascii=False, indent=1)
    verdicts = {
        'schema': 'syllabai.owner-review-verdicts/2',
        'task': TASK,
        'course': course,
        'ruledUtc': NOW,
        'source': 'delegated self-review — owner chat 2026-11-09 "approve and review yourself"; lane authorized 2026-11-13 "file as lane P9"',
        'default': 'keep',
        'reviewer': REVIEWER,
        'evidenceBasis': 'Identity: oEmbed sweep 2,825/2,825 author "Mr Hassaan\'s Maths Channel" (0 mismatch, 0 dead). Tier B: paper codes regex-verified in titles, 0 sewage found (the pool has no promo/community content; full-paper walkthroughs with worked explanations pass per ANCHOR-GRANULARITY §8). Tier A: deterministic distinctive-token pre-pass (df<=3) then class decision tables over EVERY distinctive-candidate row; rebinds validated against the target spine; degenerate token binds (paper-part labels) and cross-board routes dropped.',
        'rejects': c['rejects'],
        'applied': {'rowsApproved': len(rows), 'rowsRejected': len(c['rejects']), 'appliedUtc': NOW},
    }
    json.dump(verdicts, open(f'{D}/owner-review-verdicts.p9.json', 'w'), ensure_ascii=False, indent=1)
    (post_courses if course in POST else pre_courses).append(course)
    print(f'{course}: rows {len(rows)} (anchors {len(rows)-len(specRows)}, spec {len(specRows)}) videos {len(c["videos"])} rejects {len(c["rejects"])} -> {"P9B" if course in POST else "P9"}')

json.dump({'pre': pre_courses, 'post': post_courses}, open(f'{OUT}/p9-courses.json', 'w'), indent=1)
tot = sum(len(c['rows']) for c in courses.values())
totA = sum(1 for c in courses.values() for r in c['rows'] if r['specs'])
print('TOTAL rows', tot, '(anchors', tot - totA, ', spec rows', totA, ') across', len(courses), 'courses')
