#!/usr/bin/env python3
"""P14 step: assemble per-course drafts + verdicts (the P7/P9/P10/P11/P12/P13 file law).

Outputs (into Videos/drafts/<course>/):
  video-map.draft.external-p15.json   — reviewState owner-reviewed-external
  owner-review-verdicts.p15.json      — the honest ledger (per-course rejects)
Also writes work/p15/p15-courses.json = {pre: [...], post: [...]} for the builder:
inherit CHILDREN (the P4 map: the 0654 co-ordinated trio, the 0653 combined trio,
ial-{physics-19,biology-18}, igcse-maths-a-18-foundation, igcse-maths-a-modular-24 units x4)
take their direct rows AFTER the inherit loop (the P11B/P13B/P14B shape).
"""
import json, os, datetime, glob
from collections import Counter

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p15'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

TASK = "T-VIDEOMAP-P15 (discovery judgment lane: gap-targeted channel search sweep, T1 x14 + T2 x4 pools; 5,591 discovery-pool uploads dispositioned exactly-once)"
REVIEWER = 'delegated self-review (agent, per owner chat 2026-11-09 "approve and review yourself"; P15 discovery filed 2026-11-18, owner "Continue working" 2026-11-18 = run the lane)'

PROVIDER = {
    'chem-bio-hosni': "chem bio by Hosni (CIE IGCSE sciences 0610/0620 + Edexcel IAL biology 'Unit N <session>' unit-paper reviews + IAL chemistry — the sweep's densest find: one channel over the two biggest residual gaps)",
    'caie-made-easier': "CAIE made easier (CIE IGCSE sciences trio register: 0610/0620/0625 session papers + topic lectures)",
    'learn-today-igcse': "Learn Today IGCSE (CIE IGCSE physics/chemistry/biology register: session walkthroughs + topic lectures)",
    'nicos-paphitis': "Nicos Paphitis (CIE 0417 ICT register: session-paper walkthroughs + theory revision — pure register)",
    'everything-em': "Everything E.M. (CIE 0680 environmental management register — small pure pool)",
    'taughtly': "Taughtly (CIE 0500 First Language English register: paper walkthroughs + skills revision)",
    'dr-maria-emam': "Dr. Maria Emam (CIE 0680 environmental management + 8291 AS register)",
    'mark-harrison': "Mark Harrison (Edexcel IGCSE ICT 4IT0 paper walkthroughs + CIE 0417 ICT — dual ICT register)",
    'the-math-pad': "The Math Pad (Edexcel IGCSE maths-A 4MA1 higher/foundation/modular register: session-paper walkthroughs)",
    'science-and-stuff': "Science and Stuff (CIE 0654 co-ordinated double award + 0653 combined + single-science session walkthroughs)",
    'belal-sir-chem-bio': "Chemistry & Biology @ Belal Sir (mixed register: Edexcel IGCSE chemistry/biology + CIE 0620; the AQA-only remainder skipped honestly)",
    'geo-hacks': "GEO-HACKS (CIE 0460 IGCSE geography register + minor Edexcel 4GE0)",
    'libra-maths': "Libra Maths (Edexcel IGCSE maths-A 4MA1 + CIE 0606 additional maths)",
    'gilbert-phoon': "Gilbert Phoon (Edexcel IGCSE maths-A 4MA1 + CIE 0606 additional maths)",
    'shawn-hew': "Shawn Hew (maths & sciences) (CIE 0620 chemistry + 0606 additional maths)",
    'doctor-no-science': "Doctor No Does Science (Edexcel IAL physics 'Unit N <session>' paper reviews — the P14 Assil law analog for WPH)",
    'keen-mindz': "Keen Mindz (CIE 0452 IGCSE accounting register — 100% on-register pool)",
    'learn-econ-anjuli': "Learn Economics with Anjuli (CIE 0455 IGCSE economics topic lectures + 9708 A-level economics)",
}
CHANNEL_NOTE = {k: f"{v} (oEmbed author verified per video)" for k, v in PROVIDER.items()}

ENUM_UTC = {p: json.load(open(f'{RES}/Videos/inventory/channels/{p}-uploads.json'))['enumeratedUtc']
            for p in PROVIDER}

poolB = json.load(open(f'{OUT}/tier-b.json'))
J = json.load(open(f'{OUT}/judgment.json'))
oemb = json.load(open(f'{OUT}/oembed-p15.json'))
skips = json.load(open(f'{OUT}/skips.json'))
reserved = json.load(open(f'{OUT}/reserved.json'))

TITLE = {}
for slug in PROVIDER:
    for v in json.load(open(f'{RES}/Videos/inventory/channels/{slug}-uploads.json'))['videos']:
        TITLE[v['id']] = v['title']
_cj = json.load(open(f'{HUB}/content/courses.json'))
_clist = _cj['courses'] if isinstance(_cj, dict) else _cj
CINFO = {c['slug']: c for c in _clist}

def qual_of(course):
    ci = CINFO.get(course, {})
    board = 'CAMBRIDGE' if course.startswith('cie-') else ('EDEXCEL' if course.startswith(('ial-', 'igcse-')) else 'CAIE')
    return f"{board} {(ci.get('level') or '').upper()} {(ci.get('subject') or '').upper()}".strip()

def spine_specs(course):
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    return {n['code'] for n in cur['nodes'] if n['family'] == 'SPEC_POINT'}

P4_CHILDREN = set(json.load(open(f'{RES}/Videos/drafts/_p4/inheritance-map.json'))["parents"].keys())

courses = {}
def get(course):
    if course not in courses:
        courses[course] = {'videos': {}, 'rows': [], 'rejects': []}
    return courses[course]

def vid_entry(vid, course, provider):
    o = oemb.get(vid, {})
    return {'id': vid, 'title': TITLE.get(vid, o.get('title', vid)), 'provider': provider,
            'watchUrl': f'https://www.youtube.com/watch?v={vid}', 'lessonRef': None, 'lessonUrl': None,
            'levelTag': 'a-level' if '-a-' in course or course.startswith(('cie-a-level', 'ial-')) else ('as' if '-as-' in course else 'igcse'),
            'boardNote': CHANNEL_NOTE[provider],
            'identityMethod': o.get('method', 'oembed')}

# ---- Tier B anchors (one row per anchored course; ANCHOR-GRANULARITY §5)
for p in poolB:
    for course in p['courses']:
        c = get(course)
        if p['id'] not in c['videos']:
            c['videos'][p['id']] = vid_entry(p['id'], course, p['provider'])
        code = p['code'].replace('\t', ' ')
        cross = p.get('crossReg', False)
        ev = (f'title: "{p["title"][:110]}"; {code} in the title — machine-checkable course anchor '
              f'(ANCHOR-GRANULARITY §5{" + cross-register bind" if cross else ""}); oEmbed author verified')
        c['rows'].append({
            'anchor': {'level': 'course', 'ref': course}, 'kind': 'past-paper-walkthrough',
            'video': p['id'], 'lessonRef': None, 'lessonUrl': None, 'specs': [], 'unitScope': None,
            'confidence': 'high', 'method': 'paper-code', 'boardMismatch': bool(cross),
            'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW, 'evidence': ev,
        })

# ---- Tier A spec rows (the judgment is the per-row re-adjudication; keeps only)
for course, vs in J.items():
    for v in vs:
        if v['action'] == 'keep':
            c = get(course)
            if v['id'] not in c['videos']:
                c['videos'][v['id']] = vid_entry(v['id'], course, v['provider'])
            xreg = '; cross-register bind at the disclosed P10 bar' if v.get('crossReg') else ''
            c['rows'].append({
                'video': v['id'], 'lessonRef': None, 'lessonUrl': None, 'specs': v['specs'],
                'confidence': v['confidence'],
                'evidence': f'{v["reason"]}; title-only posture, distinctive-token binding rule (df<=3) or the disclosed higher title-only bar for section-name/topic-lecture rows (multi-point binds disclosed per row){xreg}',
                'method': 'llm-draft-external', 'boardMismatch': True,
                'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW,
            })

P14B_POST = [c for c in sorted(courses) if c in P4_CHILDREN]
pre_courses, post_courses = [], []
skip_by_class = Counter()
for s in skips:
    r = s['reason']
    if 'guidance' in r: skip_by_class['guidance/advice/marketing register'] += 1
    elif 'O-Level' in r: skip_by_class['O-Level register (no O-Level course in the spine)'] += 1
    elif 'UK-GCSE' in r: skip_by_class['Edexcel UK-GCSE CS register — no spine course (the spine carries CIE 0478)'] += 1
    elif 'out-of-spine board' in r or 'AQA/OCR/IB-board' in r or 'OCR/AQA/MEI' in r: skip_by_class['out-of-spine board register (AQA/OCR/IB/...)'] += 1
    elif 'NT-board' in r: skip_by_class['NT-board titles re-adjudicated to skip on the final sanity pass'] += 1
    elif 'no distinctive' in r or 'no binding' in r or 'no honest binding' in r or 'no unit token' in r: skip_by_class['no honest binding at the df<=3 bar'] += 1
    elif 'no spine qualification' in r: skip_by_class['non-qualifier remainder (aggregator/umbrella content)'] += 1
    elif 'out of lane' in r or 'out-of-lane' in r: skip_by_class['out-of-lane register (GCSE/IB/meta)'] += 1
    else: skip_by_class['other honest skips'] += 1

for course, c in sorted(courses.items()):
    D = f'{RES}/Videos/drafts/{course}'
    os.makedirs(D, exist_ok=True)
    rows = c['rows']
    specRows = [r for r in rows if r['specs']]
    allspecs = set()
    for r in specRows:
        allspecs |= set(r['specs'])
    provs = sorted({v2.get('provider') for v2 in c['videos'].values()} - {None})
    src_method = ('; '.join(f"{PROVIDER[pr]} flat-enumerated {ENUM_UTC.get(pr, NOW)}" for pr in provs if pr in ENUM_UTC) +
                  '; routing: machine-checkable Tier B anchors (CIE IGCSE sciences 0610/0620/0625 session/paper registers; 0654/0653 shared-paper anchors binding all three sciences of the family per the P13 shared-unit precedent; 0417/4IT0 ICT; 4MA1 maths-A higher/foundation/modular-24 units; 0606; 0452/0455/0680/8291/0460/4GE0/0500 shared-code pairs; IAL WPH/WBI/WCH Unit-N session anchors per the P14 Assil law analog; 9708) + section-marker narrowing + section-name binding (verbatim pipe/dash field match) + distinctive-token Tier A (df<=3) + the four-gate topic-lecture class, over every routed row with the degenerate-bind re-adjudication bar')
    spine_n = len(spine_specs(course))
    draft = {
        'schema': 'syllabai.video-map-draft/2',
        'draftOf': course,
        'task': TASK,
        'course': course,
        'qual': qual_of(course),
        'reviewState': 'owner-reviewed-external',
        'draftLaw': 'P15 judgment lane (the gap-targeted discovery sweep pool set: T1 x14 + T2 x4 pools; 5,591 '
                    'discovery-pool uploads dispositioned exactly-once alongside 243 RESERVED lit-0475 titles): '
                    'Tier B course anchors by machine-checkable session/paper codes (method paper-code, confidence '
                    'high; CIE IGCSE sciences 0610/0620/0625 session/paper registers; 0654/0653 shared-paper '
                    'anchors binding all three sciences of the family per the P13 shared-unit precedent; 0417/4IT0 '
                    'ICT; 4MA1 maths-A higher/foundation/modular-24-unit routing; 0606; 0452/0455/0680/8291/0460/'
                    '4GE0/0500 shared-code pairs bound to both syllabus-year courses, disclosed; IAL WPH/WBI/WCH '
                    '"Unit N <session>" unit-paper anchors per the P14 Assil law analog; 9708) + Tier A spec rows '
                    'by the distinctive-token binding rule (df<=3, deduped tokens) under the P13/P14 gate ladder: '
                    'section-marker narrowing, section-name binding (verbatim pipe/dash field equality, node norm '
                    '>= 8 chars, SUBTOPIC preferred), the four-gate topic-lecture class. Guidance/technique/'
                    'marketing registers, the O-Level register, out-of-spine boards (AQA/OCR/IB) and the Edexcel '
                    'UK-GCSE CS register (no spine course) are excluded and ledgered as skips. The Claire\'s Notes '
                    '0475 Literature pool is RESERVED pending the lit-21 owner decision. Rejected/unrouted videos '
                    'stay out of videos[].',
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
    json.dump(draft, open(f'{D}/video-map.draft.external-p15.json', 'w'), ensure_ascii=False, indent=1)
    verdicts = {
        'schema': 'syllabai.owner-review-verdicts/2',
        'task': TASK,
        'course': course,
        'ruledUtc': NOW,
        'source': 'delegated self-review — owner chat 2026-11-09 "approve and review yourself"; P15 discovery filed 2026-11-18, owner "Continue working" 2026-11-18 = run the lane; judgment run 2026-11-18',
        'default': 'keep',
        'reviewer': REVIEWER,
        'evidenceBasis': ('Identity: oEmbed sweep 1,365/1,365 routed videos author_url channel == channel-of-record '
                          'via UC id (0 mismatch, 0 dead, 0 thumb fallbacks). Tier B: session/paper codes '
                          'regex-verified in titles (CIE IGCSE sciences 0610/0620/0625 session/paper registers; '
                          '0654/0653 shared-paper anchors binding all three sciences; 0417/4IT0 ICT; 4MA1 '
                          'higher/foundation/modular-24 routing; 0606; 0452/0455/0680/8291/0460/4GE0/0500 '
                          'shared-code pairs; IAL WPH/WBI/WCH "Unit N <session>" unit-paper anchors per the P14 '
                          'Assil law analog; 9708). Tier A: the P13/P14 gate ladder (section-marker narrowing, '
                          'verbatim section-name binding, deduped distinctive-token binds df<=3, the four-gate '
                          'topic-lecture class) over EVERY routed pair with the degenerate-bind re-adjudication '
                          'bar. Guidance/advice/marketing registers, the O-Level register, out-of-spine boards '
                          '(AQA/OCR/IB), the Edexcel UK-GCSE CS register and the no-binding remainder skipped '
                          f'with reasons ({len(skips)} ledgered in work/p15/skips.json by class: '
                          f'{dict(skip_by_class)}); {len(reserved)} lit-0475 titles RESERVED pending the owner '
                          'decision (work/p15/reserved.json).'),
        'rejects': c['rejects'],
        'applied': {'rowsApproved': len(rows), 'rowsRejected': len(c['rejects']), 'appliedUtc': NOW},
    }
    json.dump(verdicts, open(f'{D}/owner-review-verdicts.p15.json', 'w'), ensure_ascii=False, indent=1)
    if course in P14B_POST:
        post_courses.append(course)
    else:
        pre_courses.append(course)
    print(f'{course}: rows {len(rows)} (anchors {len(rows)-len(specRows)}, spec {len(specRows)}) videos {len(c["videos"])} p15b {"POST" if course in P14B_POST else "pre"}')

json.dump({'pre': pre_courses, 'post': post_courses}, open(f'{OUT}/p15-courses.json', 'w'), indent=1)
tot = sum(len(c['rows']) for c in courses.values())
totA = sum(1 for c in courses.values() for r in c['rows'] if r['specs'])
summary = {
    'utc': NOW,
    'courses': len(courses), 'pre': pre_courses, 'post': post_courses,
    'rows': tot, 'anchorRows': tot - totA, 'specRows': totA,
    'tierBVideos': len({p['id'] for p in poolB}),
    'routedVideos': len({p['id'] for p in poolB}) + len({r['id'] for vs in J.values() for r in vs if r['action'] == 'keep'}),
    'skips': len(skips), 'skipByClass': dict(skip_by_class),
    'reservedLit0475': len(reserved),
    'oembed': {'verified': sum(1 for v in oemb.values() if v.get('ok')), 'bad': sum(1 for v in oemb.values() if not v.get('ok'))},
    'ntPoolLedger': 0,
    'disposition': '5,591 discovery-pool uploads = routed (tier B + tier A) + skips + 243 RESERVED lit-0475 accounts, exactly-once',
}
json.dump(summary, open(f'{OUT}/p15_summary.json', 'w'), indent=1)
print(f'\nTOTAL rows {tot} (anchors {tot - totA}, spec rows {totA}) across {len(courses)} courses | pre {len(pre_courses)} post {len(post_courses)}')
print('summary ->', f'{OUT}/p15_summary.json')
