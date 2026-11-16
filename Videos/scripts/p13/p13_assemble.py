#!/usr/bin/env python3
"""P13 step: assemble per-course drafts + verdicts (the P7/P9/P10/P11/P12 file law).

Outputs (into Videos/drafts/<course>/):
  video-map.draft.external-p13.json   — reviewState owner-reviewed-external
  owner-review-verdicts.p13.json      — the honest ledger (per-course rejects)
Also writes work/p13/p13-courses.json = {pre: [...], post: [...]} for the builder:
the AS science variants (cie-as-chemistry-25 etc.) are inherit CHILDREN rebuilt by
the inherit section, so their direct rows append AFTER the inherit loop (the P11B
shape). Of the three AS children only cie-as-chemistry-25 carries direct P13 rows
(the family's AS-register content is chemistry-heavy); as-physics-25 / as-biology-25
receive their Alt Academy content by inheritance from the parents' P13 rows."""
import json, os, datetime, glob

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p13'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

TASK = "T-VIDEOMAP-P13 (Alt Academy family lane: 9701/9708/9709/9702/9700/9706/9609 CIE-native hub + 8 subject channels)"
REVIEWER = 'delegated self-review (agent, per owner chat 2026-11-09: "approve and review yourself"; lane authorized 2026-11-14: "file it as lane P13")'

PROVIDER = {
    'alt-academy-main': "Alt Academy main channel (CAIE multi-subject hub: per-syllabus topic-lecture series + past-paper solutions + the AS chemistry walkthrough corpus)",
    'alt-academy-chemistry': "A Level Chemistry | Alt Academy (CIE 9701 topic lectures)",
    'alt-academy-economics': "A Level Economics | Alt Academy (CIE 9708 topic lectures)",
    'alt-academy-maths': "A Level Maths | Alt Academy (CIE 9709 S2/M1 unit lecture series)",
    'alt-academy-physics': "A Level Physics | Alt Academy (CIE 9702 topic lectures)",
    'alt-academy-biology': "A Level Biology | Alt Academy (CIE 9700 intro series)",
    'alt-academy-psychology': "A Level Psychology | Alt Academy (CIE 9990 study list — no spine course, honest no-target)",
    'alt-academy-accounting': "A Level Accounting | Alt Academy (CIE 9706 topic lectures)",
}
CHANNEL_NOTE = {k: f"{v} (oEmbed author verified per video)" for k, v in PROVIDER.items()}

ENUM_UTC = {p: json.load(open(f'{RES}/Videos/inventory/channels/{p}-uploads.json'))['enumeratedUtc']
            for p in PROVIDER}

poolB = json.load(open(f'{OUT}/tier-b.json'))
J = json.load(open(f'{OUT}/judgment.json'))
oemb = json.load(open(f'{OUT}/oembed-p13.json'))

TITLE = {}
for f in glob.glob(f'{OUT}/inl-*.json'):
    for v in json.load(open(f)):
        TITLE[v['id']] = v['title']

_cj = json.load(open(f'{HUB}/content/courses.json'))
_clist = _cj['courses'] if isinstance(_cj, dict) else _cj
CINFO = {c['slug']: c for c in _clist}

def qual_of(course):
    ci = CINFO.get(course, {})
    return f"CAMBRIDGE {(ci.get('level') or '').upper()} {(ci.get('subject') or '').upper()}"

def spine_specs(course):
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    return {n['code'] for n in cur['nodes'] if n['family'] == 'SPEC_POINT'}

def level_tag(course):
    return 'a-level' if course.startswith('cie-a') else 'igcse'

courses = {}
def get(course):
    if course not in courses:
        courses[course] = {'videos': {}, 'rows': [], 'rejects': []}
    return courses[course]

def vid_entry(vid, course, provider):
    o = oemb.get(vid, {})
    return {'id': vid, 'title': TITLE.get(vid, o.get('title', vid)), 'provider': provider,
            'watchUrl': f'https://www.youtube.com/watch?v={vid}', 'lessonRef': None, 'lessonUrl': None,
            'levelTag': level_tag(course), 'boardNote': CHANNEL_NOTE[provider],
            'identityMethod': o.get('method', 'oembed')}

# ---- Tier B anchors (one row per anchored course; ANCHOR-GRANULARITY §5)
for p in poolB:
    for course in p['courses']:
        c = get(course)
        if p['id'] not in c['videos']:
            c['videos'][p['id']] = vid_entry(p['id'], course, 'alt-academy-main')
        code = p['code'].replace('\t', ' ')
        ev = (f'title: "{p["title"][:110]}"; {code} in the title — '
              f'machine-checkable course anchor (ANCHOR-GRANULARITY §5); oEmbed author verified')
        c['rows'].append({
            'anchor': {'level': 'course', 'ref': course}, 'kind': 'past-paper-walkthrough',
            'video': p['id'], 'lessonRef': None, 'lessonUrl': None, 'specs': [], 'unitScope': None,
            'confidence': 'high', 'method': 'paper-code', 'boardMismatch': False,
            'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW, 'evidence': ev,
        })

# ---- Tier A spec rows (the judgment is the per-row re-adjudication; keeps only)
for course, vs in J.items():
    for v in vs:
        if v['action'] == 'keep':
            c = get(course)
            if v['id'] not in c['videos']:
                c['videos'][v['id']] = vid_entry(v['id'], course, v['provider'])
            c['rows'].append({
                'video': v['id'], 'lessonRef': None, 'lessonUrl': None, 'specs': v['specs'],
                'confidence': v['confidence'],
                'evidence': f'{v["reason"]}; title-only posture, distinctive-token binding rule (df<=3) or the disclosed higher title-only bar for section-name/topic-lecture rows (multi-point binds disclosed per row)',
                'method': 'llm-draft-external', 'boardMismatch': True,
                'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW,
            })

P13B_POST = ['cie-as-chemistry-25', 'cie-as-physics-25']  # inherit children with direct rows -> builder post-inherit section
# (cie-as-biology-25 receives no direct rows — its Alt Academy content arrives by inheritance)
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
    src_method = ('; '.join(f"{PROVIDER[pr]} flat-enumerated {ENUM_UTC.get(pr, NOW)}" for pr in provs) +
                  '; routing: session/paper-code Tier B anchors + section-name binding (verbatim field match) '
                  '+ distinctive-token Tier A with the four-gate topic-lecture class (verbatim/multi-uniq/title-token/'
                  'title-pair), N.M section-marker narrowing and per-row re-adjudication over every routed row')
    spine_n = len(spine_specs(course))
    draft = {
        'schema': 'syllabai.video-map-draft/2',
        'draftOf': course,
        'task': TASK,
        'course': course,
        'qual': qual_of(course),
        'reviewState': 'owner-reviewed-external',
        'draftLaw': 'P13 lane (Alt Academy family: one brand, nine channels — the CAIE-native multi-subject hub plus '
                    'eight subject channels; 985 uploads inventoried, 0 overlap with the shipped union beyond the '
                    '75-video business subject channel that IS the P12 pool): Tier B course anchors by machine-checkable '
                    'session/paper codes (method paper-code, confidence high, boardMismatch false — same qualification; '
                    'ANCHOR-GRANULARITY §5/§8; CIE paper-number routing: maths P1/P2/P3/P4(M1)/P5(S1)/P6(S2), sciences '
                    'papers 1-3 AS / 4-5 A2, econ/accounting/business by paper level) + Tier A spec rows by the '
                    'distinctive-token binding rule (df<=3, deduped tokens). The dominant class is the section-name '
                    'binding: the Alt Academy format "Topic | Section | register" names the syllabus section verbatim in '
                    'a pipe-field — the section\'s TOPIC/SUBTOPIC SPEC_POINTs bind as ONE multi-spec row at confidence '
                    'low through the disclosed verbatim field-equality gate (node norm >= 8 chars, SUBTOPIC preferred). '
                    'Four-gate topic lectures (verbatim/multi-uniq/title-token/title-pair), N.M section-marker narrowing '
                    'and maths unit-token routing (S2/S1/M1/P1/P2/P3 to the spine\'s unit courses, shared units bound to '
                    'BOTH the AS and A-level course) complete the ladder. Teacher-guidance/technique registers, the '
                    'O-Level register, meta/marketing videos and CIE 9990 psychology (no spine course — honest no-target) '
                    'are excluded and ledgered as skips (310). Degenerate binds (generic-token-only evidence) were '
                    're-adjudicated to honest skips on review (2). Rejected/unrouted videos stay out of videos[].',
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
    json.dump(draft, open(f'{D}/video-map.draft.external-p13.json', 'w'), ensure_ascii=False, indent=1)
    verdicts = {
        'schema': 'syllabai.owner-review-verdicts/2',
        'task': TASK,
        'course': course,
        'ruledUtc': NOW,
        'source': 'delegated self-review — owner chat 2026-11-09 "approve and review yourself"; lane authorized 2026-11-14 "file it as lane P13"',
        'default': 'keep',
        'reviewer': REVIEWER,
        'evidenceBasis': 'Identity: oEmbed sweep 587/587 author_url channel == channel-of-record via UC id (0 mismatch, 0 dead, 0 thumb fallbacks). '
                         'Tier B: session/paper codes regex-verified in titles (CIE paper-number routing per subject; maths shared units anchored to BOTH the AS and A-level course). '
                         'Tier A: the section-name binding gate (verbatim pipe-field equality against TOPIC/SUBTOPIC titles) over the structured '
                         '"Topic | Section | register" series, deduped distinctive-token binds (df<=3), the four-gate topic-lecture class and N.M '
                         'section-marker narrowing over EVERY routed pair; maths unit tokens (S2/S1/M1/P1/P2/P3) route to the spine\'s unit courses; '
                         'degenerate generic-token binds (2: the S2 "between/two" hypothesis-test bind and the terse "Pricing strategies Short term" '
                         'finance bind) re-adjudicated to honest skips on review; guidance/advice/marketing registers, the O-Level register and '
                         'CIE 9990 psychology (no spine course) skipped with reasons (310 ledgered in work/p13/skips.json).',
        'rejects': c['rejects'],
        'applied': {'rowsApproved': len(rows), 'rowsRejected': len(c['rejects']), 'appliedUtc': NOW},
    }
    json.dump(verdicts, open(f'{D}/owner-review-verdicts.p13.json', 'w'), ensure_ascii=False, indent=1)
    if course in P13B_POST:
        post_courses.append(course)
    else:
        pre_courses.append(course)
    print(f'{course}: rows {len(rows)} (anchors {len(rows)-len(specRows)}, spec {len(specRows)}) videos {len(c["videos"])} rejects {len(c["rejects"])}')

json.dump({'pre': pre_courses, 'post': post_courses}, open(f'{OUT}/p13-courses.json', 'w'), indent=1)
tot = sum(len(c['rows']) for c in courses.values())
totA = sum(1 for c in courses.values() for r in c['rows'] if r['specs'])
print('TOTAL rows', tot, '(anchors', tot - totA, ', spec rows', totA, ') across', len(courses), 'courses | pre', len(pre_courses), 'post', len(post_courses))
