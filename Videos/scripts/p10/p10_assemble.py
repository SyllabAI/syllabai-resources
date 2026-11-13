#!/usr/bin/env python3
"""P10 step 4: assemble per-course drafts + verdicts (the P7/P9 file law).

Outputs (into Videos/drafts/<course>/):
  video-map.draft.external-p10.json   — reviewState owner-reviewed-external
  owner-review-verdicts.p10.json      — the honest ledger (drops + unmapped)
Also writes work/p10/p10-courses.json = {pre: [...], post: []} for the builder
(no inherit-CHILD course takes direct P10 rows: the IAL targets are standalone
courses and the Arnolds rows sit on the inherit PARENT a-18-higher, whose five
children cascade at build time)."""
import json, os, collections, datetime

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p10'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

TASK = "T-VIDEOMAP-P10 (two-pool maths completion: MrArnoldsMaths + Maths Deity)"
REVIEWER = 'delegated self-review (agent, per owner chat 2026-11-09: "approve and review yourself"; lane authorized 2026-11-13: "lane P10")'
PROVIDER = {
    'mrarnoldsmaths': "MrArnoldsMaths (MrArnoldsMaths Channel — legacy Edexcel GCSE/GCE walkthrough + topic-tutorial channel)",
    'mathsdeity': "Maths Deity (@MathsDeity — Edexcel IAL unit.section tutorial + paper-walkthrough channel)",
}
CHANNEL_NOTE = {
    'mrarnoldsmaths': ("MrArnoldsMaths — legacy Edexcel GCSE/GCE channel (channelId UCwa84m5RqSJEkP9pYdeDYnw); "
                       "oEmbed author verified per video"),
    'mathsdeity': ("Maths Deity — Edexcel IAL unit.section tutorial + paper-walkthrough channel "
                   "(channelId UCODyYjai6abd1N5KGc1KacQ); oEmbed author verified per video"),
}
ENUM = {
    'mrarnoldsmaths': json.load(open(f'{RES}/Videos/inventory/channels/mrarnoldsmaths-uploads.json'))['enumeratedUtc'],
    'mathsdeity': json.load(open(f'{RES}/Videos/inventory/channels/mathsdeity-uploads.json'))['enumeratedUtc'],
}

QUAL = {
    'ial-maths-20-pure-1': 'IAL Maths (Edexcel)', 'ial-maths-20-pure-2': 'IAL Maths (Edexcel)',
    'ial-maths-20-pure-3': 'IAL Maths (Edexcel)', 'ial-maths-20-pure-4': 'IAL Maths (Edexcel)',
    'ial-maths-20-statistics-1': 'IAL Maths (Edexcel)', 'ial-maths-20-statistics-2': 'IAL Maths (Edexcel)',
    'ial-maths-20-mechanics-1': 'IAL Maths (Edexcel)', 'ial-maths-20-mechanics-2': 'IAL Maths (Edexcel)',
    'ial-further-maths-18-further-pure-1': 'IAL Further Maths (Edexcel)',
    'igcse-maths-a-18-higher': 'IGCSE',
}

poolB = json.load(open(f'{OUT}/tier-b.json'))
J = json.load(open(f'{OUT}/judgment.json'))
tierA = {p['id']: p for p in json.load(open(f'{OUT}/tier-a.json'))}
oemb = json.load(open(f'{OUT}/oembed-p10.json'))

def spine_specs(course):
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    return {n['code'] for n in cur['nodes'] if n['family'] == 'SPEC_POINT'}

def level_tag(course):
    if course.startswith('ial-'):
        return 'ial'
    return 'igcse'

courses = {}
def get(course):
    if course not in courses:
        courses[course] = {'videos': {}, 'rows': [], 'rejects': []}
    return courses[course]

def vid_entry(v, course, provider):
    o = oemb.get(v['id'], {})
    return {'id': v['id'], 'title': v['title'], 'provider': provider,
            'watchUrl': v['watchUrl'], 'lessonRef': None, 'lessonUrl': None,
            'levelTag': level_tag(course), 'boardNote': CHANNEL_NOTE[provider],
            'identityMethod': o.get('method', 'oembed')}

# ---- Tier B anchors (one row per anchored course; ANCHOR-GRANULARITY §5)
for p in poolB:
    for course in p['courses']:
        c = get(course)
        if p['id'] not in c['videos']:
            c['videos'][p['id']] = vid_entry(p, course, p['provider'])
        ev = (f'title: "{p["title"][:110]}"; IAL module code {p["code"]} in the title — '
              f'machine-checkable course anchor (ANCHOR-GRANULARITY §5); oEmbed author verified')
        c['rows'].append({
            'anchor': {'level': 'course', 'ref': course}, 'kind': 'past-paper-walkthrough',
            'video': p['id'], 'lessonRef': None, 'lessonUrl': None, 'specs': [], 'unitScope': None,
            'confidence': 'high', 'method': 'paper-code', 'boardMismatch': False,
            'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW, 'evidence': ev,
        })

# ---- Tier A spec rows + rejects
for course, vs in J.items():
    if course == '__amb-unresolved__':
        for v in vs:
            src = tierA[v['id']]
            get('ial-maths-20-pure-1')['rejects'].append({'video': v['id'], 'reason': f"ambiguous route unresolved: {v['reason']}"})
        continue
    for v in vs:
        if v['action'] in ('keep', 'rebind'):
            tgt = v['course'] if v['action'] == 'rebind' else course
            c = get(tgt)
            src = tierA[v['id']]
            if v['id'] not in c['videos']:
                c['videos'][v['id']] = vid_entry(src, tgt, src['provider'])
            c['rows'].append({
                'video': v['id'], 'lessonRef': None, 'lessonUrl': None, 'specs': v['specs'],
                'confidence': v['confidence'],
                'evidence': f'{v["reason"]}; title-only posture, distinctive-token binding rule (df<=3) or the disclosed higher title-only bar for marker rows',
                'method': 'llm-draft-external', 'boardMismatch': True,
                'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW,
            })
            if v['action'] == 'rebind':
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
    provs = sorted({v2.get('provider') for v2 in c['videos'].values()} - {None})
    src_method = ('; '.join(f"{PROVIDER[pr]} flat-enumerated {ENUM[pr]}" for pr in provs) +
                  '; routing: module-code Tier B anchors + unit.section-marker/module-named Tier A with class-table judgment over every row')
    spine_n = len(spine_specs(course))
    draft = {
        'schema': 'syllabai.video-map-draft/2',
        'draftOf': course,
        'task': TASK,
        'course': course,
        'qual': QUAL[course],
        'reviewState': 'owner-reviewed-external',
        'draftLaw': 'P10 lane: Tier B course anchors by machine-checkable IAL module codes (method paper-code, confidence high, boardMismatch false — same qualification; ANCHOR-GRANULARITY §5/§8) + Tier A spec rows by the distinctive-token binding rule, with module-structured marker rows permitted the disclosed higher title-only bar (P4 cross-subject-style, confidence low, disclosed per row) where the small dense module spines make df<=3 structurally unable to discriminate. Rejected videos stay out of videos[] and live in the verdicts ledger.',
        'source': {
            'provider': ' + '.join(PROVIDER[pr] for pr in provs),
            'label': course,
            'method': src_method,
            'enumeratedUtc': NOW,
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
    json.dump(draft, open(f'{D}/video-map.draft.external-p10.json', 'w'), ensure_ascii=False, indent=1)
    verdicts = {
        'schema': 'syllabai.owner-review-verdicts/2',
        'task': TASK,
        'course': course,
        'ruledUtc': NOW,
        'source': 'delegated self-review — owner chat 2026-11-09 "approve and review yourself"; lane authorized 2026-11-13 "lane P10"',
        'default': 'keep',
        'reviewer': REVIEWER,
        'evidenceBasis': 'Identity: oEmbed sweep 358/358 author==channel-of-record (0 mismatch, 0 dead, 0 thumb-fallbacks needed). Tier B: IAL module codes regex-verified in titles. Tier A: deterministic distinctive-token pre-pass (df<=3) then explicit-code class tables over EVERY routed row; module-structured rows (unit.section marker / module-named title) permitted the disclosed higher title-only bar at low confidence; rebinds validated against the target spine; degenerate vocabulary binds (factor formulae -> P1 radian) dropped.',
        'rejects': c['rejects'],
        'applied': {'rowsApproved': len(rows), 'rowsRejected': len(c['rejects']), 'appliedUtc': NOW},
    }
    json.dump(verdicts, open(f'{D}/owner-review-verdicts.p10.json', 'w'), ensure_ascii=False, indent=1)
    pre_courses.append(course)
    print(f'{course}: rows {len(rows)} (anchors {len(rows)-len(specRows)}, spec {len(specRows)}) videos {len(c["videos"])} rejects {len(c["rejects"])}')

json.dump({'pre': pre_courses, 'post': post_courses}, open(f'{OUT}/p10-courses.json', 'w'), indent=1)
tot = sum(len(c['rows']) for c in courses.values())
totA = sum(1 for c in courses.values() for r in c['rows'] if r['specs'])
print('TOTAL rows', tot, '(anchors', tot - totA, ', spec rows', totA, ') across', len(courses), 'courses')
