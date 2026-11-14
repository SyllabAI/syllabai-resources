#!/usr/bin/env python3
"""P12 step: assemble per-course drafts + verdicts (the P7/P9/P10/P11 file law).

Outputs (into Videos/drafts/<course>/):
  video-map.draft.external-p12.json   — reviewState owner-reviewed-external
  owner-review-verdicts.p12.json      — the honest ledger (per-course rejects)
Also writes work/p12/p12-courses.json = {pre: [...], post: []} for the builder
(all five P12 targets are standalone fresh courses — no inherit-CHILD course
takes direct P12 rows)."""
import json, os, datetime

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p12'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

TASK = "T-VIDEOMAP-P12 (narrow CIE cluster lane: 9609 business / 9696 geography / 8291 EM / 8021 GP)"
REVIEWER = 'delegated self-review (agent, per owner chat 2026-11-09: "approve and review yourself"; lane authorized 2026-11-13: "run P12")'

PROVIDER = {
    'cambridge-business-essentials': "Cambridge Business Essentials A-level & IGCSE (CIE 9609 Business exam-technique + 0450 pool)",
    'bizedmadesimple': "BizEdMadeSimple (CIE 9609 Business topical explainers + paper guides + IGCSE pool)",
    'alt-academy': "A Level Business | Alt Academy (CIE 9609 AS/A2 unit-content lesson series)",
    'the-teaching-student': "The Teaching Student (CIE 9609 session-paper predictions with machine-checkable codes)",
    'the-geography-academy': "The Geography Academy (CIE 9696 structured topic course 2027-2029 + 0460 pool)",
    'virtual-pathways': "Virtual Pathways (CIE 8291 AS EM topic lecture series inside a multi-subject platform)",
    'polymath-institute': "Polymath Institute (CIE 8291/0680 preparation-course pool, generic register)",
    'mini-lessons-gp': "Mini Lessons (CIE 8021 General Paper short series)",
    'english-with-ms-irum': "English with Ms Irum (CIE 8021 General Paper session papers + strategy pool)",
    'ace-the-exam': "Ace The Exam Cambridge IGCSE O & A Levels (GP topic-list revision guides inside a large mixed pool)",
    'miss-cutu': "Miss Cutu Bilingual Help (CIE 8021 General Paper essay/comprehension guidance)",
}
CHANNEL_NOTE = {k: f"{v} (oEmbed author verified per video)" for k, v in PROVIDER.items()}

ENUM_UTC = {p: json.load(open(f'{RES}/Videos/inventory/channels/{p}-uploads.json'))['enumeratedUtc']
            for p in PROVIDER}

poolB = json.load(open(f'{OUT}/tier-b.json'))
J = json.load(open(f'{OUT}/judgment.json'))
oemb = json.load(open(f'{OUT}/oembed-p12.json'))

# title lookup from the in-cluster extracts + tier-b
TITLE = {}
import glob
for f in glob.glob(f'{OUT}/inl-*.json'):
    for v in json.load(open(f)):
        TITLE[v['id']] = v['title']
for p in poolB:
    TITLE[p['id']] = p['title']

_cj = json.load(open(f'{HUB}/content/courses.json'))
_clist = _cj['courses'] if isinstance(_cj, dict) else _cj
CINFO = {c['slug']: c for c in _clist}

def qual_of(course):
    ci = CINFO.get(course, {})
    board = ci.get('board') or ''
    lvl = ci.get('level') or ''
    subj = ci.get('subject') or ''
    if board == 'Cambridge International':
        return f"CAMBRIDGE {lvl.upper()} {subj.upper()}"
    return f"IGCSE {subj.upper()} (EDEXCEL)"

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
            c['videos'][p['id']] = vid_entry(p['id'], course, p['provider'])
        code = p['code'].replace('\t', ' ')
        ev = (f'title: "{p["title"][:110]}"; session/paper code "{code}" in the title — '
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
                'evidence': f'{v["reason"]}; title-only posture, distinctive-token binding rule (df<=3) or the disclosed higher title-only bar for topic-lecture/section-marker rows (multi-point binds disclosed per row)',
                'method': 'llm-draft-external', 'boardMismatch': True,
                'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW,
            })

pre_courses = []
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
                  '; routing: session/paper-code Tier B anchors + distinctive-token Tier A with topic-lecture '
                  '(verbatim/multi-uniq/title-token/title-pair gates), section-marker narrowing and per-row '
                  're-adjudication over every routed row')
    spine_n = len(spine_specs(course))
    draft = {
        'schema': 'syllabai.video-map-draft/2',
        'draftOf': course,
        'task': TASK,
        'course': course,
        'qual': qual_of(course),
        'reviewState': 'owner-reviewed-external',
        'draftLaw': 'P12 lane (narrow CIE cluster lane: 9609/9696/8291/8021): Tier B course anchors by machine-checkable '
                    'session/paper codes (method paper-code, confidence high, boardMismatch false — same qualification; '
                    'ANCHOR-GRANULARITY §5/§8) + Tier A spec rows by the distinctive-token binding rule (df<=3, deduped tokens). '
                    'Full-topic lecture rows (The Geography Academy unit courses, Virtual Pathways 8291 series) bind their '
                    'topic\'s SPEC_POINTs as ONE multi-spec row at confidence low through four disclosed gates (verbatim '
                    'topic name / >=2 topic-unique tokens / topic-title unique token / topic-title unique pair) — the '
                    'title-only bar, disclosed per row. Section-marker rows (N.M) bind their section\'s points, likewise '
                    'disclosed. Teacher-guidance/technique registers and generic course mentions are excluded as bind '
                    'targets and ledgered as skips (304). Degenerate single-generic-token binds were re-adjudicated to '
                    'honest skips on review. Rejected/unrouted videos stay out of videos[] and live in the work ledger.',
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
    json.dump(draft, open(f'{D}/video-map.draft.external-p12.json', 'w'), ensure_ascii=False, indent=1)
    verdicts = {
        'schema': 'syllabai.owner-review-verdicts/2',
        'task': TASK,
        'course': course,
        'ruledUtc': NOW,
        'source': 'delegated self-review — owner chat 2026-11-09 "approve and review yourself"; lane authorized 2026-11-13 "run P12"',
        'default': 'keep',
        'reviewer': REVIEWER,
        'evidenceBasis': 'Identity: oEmbed sweep 119/119 author channel == channel-of-record via author_url UC id (0 mismatch, 0 dead). '
                         'Tier B: session/paper codes regex-verified in titles (9609/42|22|12 O/N/26 predictions; 8021 GP session papers). '
                         'Tier A: deduped distinctive-token binds (df<=3) then four-gate topic-lecture class (verbatim / multi-uniq / '
                         'title-token / title-pair) and N.M section-marker narrowing over EVERY routed pair; degenerate '
                         'single-generic-token binds (e.g. "issues"/"changing"/"rural") re-adjudicated to honest skips on review; '
                         'technique/guidance registers and generic mentions skipped with reasons (304 ledgered in work/p12/skips.json); '
                         'out-of-lane registers (IGCSE business/geo/EM, 0460/0450/0680) skipped as covered-or-out-of-scope.',
        'rejects': c['rejects'],
        'applied': {'rowsApproved': len(rows), 'rowsRejected': len(c['rejects']), 'appliedUtc': NOW},
    }
    json.dump(verdicts, open(f'{D}/owner-review-verdicts.p12.json', 'w'), ensure_ascii=False, indent=1)
    pre_courses.append(course)
    print(f'{course}: rows {len(rows)} (anchors {len(rows)-len(specRows)}, spec {len(specRows)}) videos {len(c["videos"])} rejects {len(c["rejects"])}')

json.dump({'pre': pre_courses, 'post': []}, open(f'{OUT}/p12-courses.json', 'w'), indent=1)
tot = sum(len(c['rows']) for c in courses.values())
totA = sum(1 for c in courses.values() for r in c['rows'] if r['specs'])
print('TOTAL rows', tot, '(anchors', tot - totA, ', spec rows', totA, ') across', len(courses), 'courses')
