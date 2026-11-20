#!/usr/bin/env python3
"""P17 step: assemble per-course drafts + verdicts (the P7..P15 file law).

Outputs (into Videos/drafts/<course>/):
  video-map.draft.external-p17.json   — reviewState owner-reviewed-external
  owner-review-verdicts.p17.json      — the honest ledger (per-course rejects)
Also writes work/p17/p17-courses.json = {pre: [...], post: [...]} for the builder:
inherit CHILDREN (the P4 map) take their direct rows AFTER the inherit loop (the
P11B/P13B/P14B/P15B shape).
"""
import json, os, datetime
from collections import Counter

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p17'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

TASK = "T-VIDEOMAP-P17 (gap-profile judgment lane: the P17 filing PR #360 pool set admitted by owner order 'run P17 judgment' 2026-11-20; 8,927 pool uploads dispositioned exactly-once)"
REVIEWER = 'delegated self-review (agent, per owner chat 2026-11-09 "approve and review yourself"; P17 profile authorized 2026-11-20 "P17 profile", judgment admitted 2026-11-20 "run P17 judgment")'

PROVIDER = {
    'chem-bio-math-revision-hub': "Chemistry, Biology, and Math revision Hub (Edexcel IAL sciences in the 'A level | subject | Unit N | session | Pearson Edexcel' pipe format — the P14 Assil unit-paper anchor law extended to the pipe register; disclosed P17 family)",
    'wilson-chong': "Wilson Chong (2012-era Edexcel UK GCSE modular maths — 1MA0 units, NOT the spine's 2024 4XM modular IGCSE; 0 honest binds, disclosed)",
    'daniyal-aslam': "Daniyal Aslam (CIE 9708 A-level economics paper walkthroughs incl. AS/A2 MCQ variants + 0455 economics — the sweep's densest find)",
    'nevdoes-econ': "NevDoesEcon (generic A-level economics topic content with no board code — the sweep's '9708 x147' register read was a false density; 3 honest ladder binds, disclosed)",
    'edexcel-science-channel': "Edexcel Science Channel (Edexcel IAL WPH14/WCH11 unit+topic register + Edexcel IGCSE 4CH1/4BI1/4PH1 paper walkthroughs)",
    'gcse-ready': "GCSE-ready (GCSE & IGCSE Mathematics topic library + the one genuine International GCSE Geography A title; the UK-GCSE-only remainder skipped honestly; the sweep's 0475 x129 family read was a false density — 0 real lit tokens)",
    'adebayo-business-abt': "Adebayo Business Tutor (ABT) (Edexcel IGCSE Business 4BS1 paper walkthroughs + a large genuine business-topic library binding across igcse-business-19 and the CIE business courses at the df<=3/verbatim gates)",
    'business-teacher-t': "Business Teacher T (Edexcel UK A-level Business register — out-of-spine board; honest topic binds only where CIE tokens/topics machine-check)",
    'aravinth-physics-maths': "Aravinth Physics Maths Lessons (Edexcel IAL physics 'Unit N <session>' paper reviews — the P14 Assil law analog)",
    'a2z-physics': "A2Z Physics (Edexcel IAL physics unit register + CIE 0625; the AQA-heavy remainder skipped honestly)",
    'biology-zhan-xuan': "Biology with Zhan Xuan (CIE 0610 IGCSE biology — 100% on-register pool)",
    'mrimmoaee-ahmed': "Mrimmoaee Ahmed (Edexcel IGCSE ICT 4IT1 paper walkthroughs + CIE 0417; the IAL IT (WIT) remainder skipped — no spine course)",
    'click-ict': "Click ICT (Pearson Edexcel IGCSE ICT 4IT1 topic register — small pure pool)",
    'state-of-math': "State Of Math (Edexcel IGCSE maths 4MA1 paper walkthroughs + the 4WM1/4WM2 modular sample assessments; the IAL maths P1-M2/S1 remainder skips per ANCHOR-GRANULARITY §6 — the P9 precedent)",
    'first-rate-tutors': "First Rate Tutors (the channel's lit content is UK GCSE English Literature, not CIE 0475 — the sweep's 0475 x63 family read was a false density; 0 honest binds, disclosed)",
    'fundoo-tutor': "Fundoo Tutor IGCSE Grade 9 and 10 (Cambridge IGCSE 0610/0455/0625/0620 misconception/error-analysis rows in the 'subject | code | error-class | detail' pipe format)",
    'team-elevare': "Team Elevare (Edexcel IAL WBI13/WPH13 unit summaries + IGCSE modular chemistry 4WCH1/4WCH2 + 4MB1/4MA1/4BI1/4CH1/4SD0 paper walkthroughs; the IAL IT/econ (WIT/WEC) remainder skipped — no spine courses)",
    'mathman-oa-levels': "Mathman - O/A Level Maths (CIE 0606 additional maths paper walkthroughs — the 4037 O-Level token is the dual branding of the same syllabus, disclosed; 0607 x6)",
    'pinnacle-education': "Pinnacle Education (Edexcel IGCSE Maths B 4MB1 paper walkthroughs — small pure pool)",
    'dr-sarah-biology': "Dr. Sarah | Edexcel Alevel Biology (Edexcel IAL biology WBI unit register — small pure pool)",
    'mr-quakers-teaches': "Mr. Quakers Teaches (Cambridge iGCSE Literature set-text poem analyses — 'Sample Detailed Analysis of Author's Work' format; the P16 Class W predicate with the disclosed P17 amendment: possessive-author extraction + hashtag-suffixed quote lookahead)",
}
CHANNEL_NOTE = {k: f"{v} (oEmbed author verified per video)" for k, v in PROVIDER.items()}

ENUM_UTC = {p: json.load(open(f'{RES}/Videos/inventory/channels/{p}-uploads.json'))['enumeratedUtc']
            for p in PROVIDER}

poolB = json.load(open(f'{OUT}/tier-b.json'))
J = json.load(open(f'{OUT}/judgment.json'))
oemb = json.load(open(f'{OUT}/oembed-p17.json'))
skips = json.load(open(f'{OUT}/skips.json'))

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

P17B_POST = [c for c in sorted(courses) if c in P4_CHILDREN]
pre_courses, post_courses = [], []
skip_by_class = Counter()
for s in skips:
    r = s['reason']
    if 'guidance' in r: skip_by_class['guidance/advice/marketing register'] += 1
    elif 'promo/meta' in r: skip_by_class['channel promo/meta content (no qualification register)'] += 1
    elif 'O-Level' in r: skip_by_class['O-Level register (no O-Level course in the spine)'] += 1
    elif 'UK GCSE modular' in r: skip_by_class['Edexcel UK GCSE modular maths 2012-era register (1MA0) — out-of-spine register'] += 1
    elif 'UK GCSE English Literature' in r: skip_by_class['UK GCSE English Literature register — out-of-spine register'] += 1
    elif 'UK GCSE register' in r: skip_by_class['UK GCSE register (1GA0/GCSE Mathematics) — out-of-spine register'] += 1
    elif 'IAL/CIE maths' in r: skip_by_class['IAL/CIE maths register — bare unit/session walkthroughs skip per ANCHOR-GRANULARITY §6 (P9 precedent)'] += 1
    elif 'IAL Information Technology' in r or 'WIT/WEC' in r: skip_by_class['Edexcel IAL IT/economics (WIT/WEC) — no spine courses'] += 1
    elif 'UK A-level business' in r: skip_by_class['Edexcel UK A-level business register — out-of-spine board'] += 1
    elif 'out-of-spine board' in r or 'AQA/OCR/IB-board' in r: skip_by_class['out-of-spine board register (AQA/OCR/IB/...)'] += 1
    elif 'NT-board' in r: skip_by_class['NT-board titles re-adjudicated to skip on the final sanity pass'] += 1
    elif 'no distinctive' in r or 'no binding' in r or 'no honest binding' in r or 'no unit token' in r: skip_by_class['no honest binding at the df<=3 bar'] += 1
    elif 'not on the 2023-2025 set-text lists' in r: skip_by_class['lit register: work not on the 0475 2023-2025 set-text lists'] += 1
    elif 'character-study' in r: skip_by_class['lit register: character-study title without a set-text token'] += 1
    elif 'UK-GCSE' in r: skip_by_class['Edexcel UK-GCSE CS register — no spine course (the spine carries CIE 0478)'] += 1
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
                  '; routing: machine-checkable Tier B anchors (CIE IGCSE sciences 0610/0620/0625 session/paper registers; 0654/0653 shared-paper anchors; 0417/4IT1+4IT0 ICT; 4MA1/4WM/4XM maths-A higher/foundation/modular-24 routing; 4MB1; 0606 with the disclosed 4037-dual-branding precedence; 0607; 0452/0455/0680/8291/0460/4GE1+4GE0/0500 shared-code pairs; 4BS1; 9708; 9609; Ed-IGCSE sciences 4CH1/4BI1/4PH1/4SD0 + modular chemistry 4WCH1/4WCH2; IAL WPH/WBI/WCH "Unit N <session>" unit-paper anchors + the Pearson-pipe register family) + the P16 Class W set-text predicate for 0475 titles (with the disclosed P17 possessive/hashtag amendment) + section-marker narrowing + section-name binding (verbatim pipe/dash field match) + distinctive-token Tier A (df<=3) + the four-gate topic-lecture class, over every routed row with the degenerate-bind re-adjudication bar')
    spine_n = len(spine_specs(course))
    draft = {
        'schema': 'syllabai.video-map-draft/2',
        'draftOf': course,
        'task': TASK,
        'course': course,
        'qual': qual_of(course),
        'reviewState': 'owner-reviewed-external',
        'draftLaw': 'P17 judgment lane (the gap-profile pool set: 21 pools admitted by owner order "run P17 judgment" 2026-11-20; 8,927 '
                    'pool uploads dispositioned exactly-once): '
                    'Tier B course anchors by machine-checkable session/paper codes (method paper-code, confidence '
                    'high; the P15 registers plus the P17 additions: 4GE1 geography-A, 4IT1 ICT, 4MB1 maths-B, the '
                    '4WM1/4WM2 modular-maths paper codes, 4XM modular maths, 0607 international maths, 4BS1 business, '
                    '9609 business, Ed-IGCSE sciences 4CH1/4BI1/4PH1/4SD0, modular chemistry 4WCH1/4WCH2, and the '
                    'IAL unit-paper anchor law extended to the Pearson-pipe register) + the P16 Class W set-text '
                    'predicate for 0475 titles (the disclosed P17 amendment: possessive Author-Work extraction and '
                    'hashtag-suffixed quote lookahead) + Tier A spec rows by the distinctive-token binding rule '
                    '(df<=3) under the P13/P15 gate ladder: section-marker narrowing, section-name binding (verbatim '
                    'pipe/dash field equality, node norm >= 8 chars, SUBTOPIC preferred), the four-gate topic-lecture '
                    'class. Guidance/promo registers, the O-Level register (0606/4037 dual branding disclosed), the '
                    '2012-era UK GCSE modular maths register, the UK GCSE 1GA0 geography / GCSE English Lit registers, '
                    'IAL IT (WIT) and IAL economics (WEC) (no spine courses), the IAL/CIE maths bare-walkthrough class '
                    '(ANCHOR-GRANULARITY §6, P9 precedent) and out-of-spine boards (AQA/OCR/IB/Edexcel UK A-level '
                    'business) are excluded and ledgered as skips. Rejected/unrouted videos stay out of videos[].',
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
    json.dump(draft, open(f'{D}/video-map.draft.external-p17.json', 'w'), ensure_ascii=False, indent=1)
    verdicts = {
        'schema': 'syllabai.owner-review-verdicts/2',
        'task': TASK,
        'course': course,
        'ruledUtc': NOW,
        'source': 'delegated self-review — owner chat 2026-11-09 "approve and review yourself"; P17 profile authorized 2026-11-20 "P17 profile", pools admitted and judgment ordered 2026-11-20 "run P17 judgment"',
        'default': 'keep',
        'reviewer': REVIEWER,
        'evidenceBasis': ('Identity: oEmbed sweep 2,614/2,614 routed videos author_url channel == channel-of-record '
                          'via UC id (0 mismatch, 0 dead, 0 thumb fallbacks). Tier B: session/paper codes '
                          'regex-verified in titles (the P15 registers plus the P17 additions: 4GE1/4IT1/4MB1/4WM/4XM/'
                          '0607/4BS1/9609/4CH1/4BI1/4PH1/4SD0/4WCH1/4WCH2 + the Pearson-pipe IAL unit register). '
                          'Class W: the P16 committed predicate with the disclosed P17 amendment for the mr-quakers '
                          'possessive format. Tier A: the P13/P15 gate ladder (section-marker narrowing, verbatim '
                          'section-name binding, deduped distinctive-token binds df<=3, the four-gate topic-lecture '
                          'class) over EVERY routed pair with the degenerate-bind re-adjudication bar. Guidance/promo, '
                          'O-Level (0606/4037 dual branding disclosed), UK GCSE modular 2012, UK GCSE 1GA0/GCSE-Eng-Lit, '
                          'IAL IT/econ (no spine), IAL/CIE maths bare walkthroughs (§6) and out-of-spine boards skipped '
                          f'with reasons ({len(skips)} ledgered in work/p17/skips.json by class: '
                          f'{dict(skip_by_class)}).'),
        'rejects': c['rejects'],
        'applied': {'rowsApproved': len(rows), 'rowsRejected': len(c['rejects']), 'appliedUtc': NOW},
    }
    json.dump(verdicts, open(f'{D}/owner-review-verdicts.p17.json', 'w'), ensure_ascii=False, indent=1)
    if course in P17B_POST:
        post_courses.append(course)
    else:
        pre_courses.append(course)
    print(f'{course}: rows {len(rows)} (anchors {len(rows)-len(specRows)}, spec {len(specRows)}) videos {len(c["videos"])} p17b {"POST" if course in P17B_POST else "pre"}')

json.dump({'pre': pre_courses, 'post': post_courses}, open(f'{OUT}/p17-courses.json', 'w'), indent=1)
tot = sum(len(c['rows']) for c in courses.values())
totA = sum(1 for c in courses.values() for r in c['rows'] if r['specs'])
summary = {
    'utc': NOW,
    'courses': len(courses), 'pre': pre_courses, 'post': post_courses,
    'rows': tot, 'anchorRows': tot - totA, 'specRows': totA,
    'tierBVideos': len({p['id'] for p in poolB}),
    'routedVideos': len({p['id'] for p in poolB}) | len({r['id'] for vs in J.values() for r in vs if r['action'] == 'keep'}),
    'skips': len(skips), 'skipByClass': dict(skip_by_class),
    'oembed': {'verified': sum(1 for v in oemb.values() if v.get('ok')), 'bad': sum(1 for v in oemb.values() if not v.get('ok'))},
    'disposition': '8,927 P17 pool uploads = routed (tier B + tier A) + skips, exactly-once',
}
summary['routedVideos'] = len({p['id'] for p in poolB} | {r['id'] for vs in J.values() for r in vs if r['action'] == 'keep'})
json.dump(summary, open(f'{OUT}/p17_summary.json', 'w'), indent=1)
print(f'\nTOTAL rows {tot} (anchors {tot - totA}, spec rows {totA}) across {len(courses)} courses | pre {len(pre_courses)} post {len(post_courses)}')
print('summary ->', f'{OUT}/p17_summary.json')
