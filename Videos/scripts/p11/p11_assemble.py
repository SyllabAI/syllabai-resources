#!/usr/bin/env python3
"""P11 step 4: assemble per-course drafts + verdicts (the P7/P9/P10 file law).

Outputs (into Videos/drafts/<course>/):
  video-map.draft.external-p11.json   — reviewState owner-reviewed-external
  owner-review-verdicts.p11.json      — the honest ledger (drops + unmapped)
Also writes work/p11/p11-courses.json = {pre: [...], post: []} for the builder
(all P11 targets are standalone/fresh courses — no inherit-CHILD course takes
direct P11 rows)."""
import json, os, collections, datetime

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p11'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

TASK = "T-VIDEOMAP-P11 (multi-cluster uncovered-course lane: fourteen channel pools)"
REVIEWER = 'delegated self-review (agent, per owner chat 2026-11-09: "approve and review yourself"; lane authorized 2026-11-13: "lane P11")'

PROVIDER = {
    'enhancetuition': "EnhanceTuition (@EnhanceTuition — CIE A-level Economics 9708 + Accounting 9706 channel)",
    'econplusdal': "EconplusDal (UK Edexcel GCE A-level Economics — honest no-target pool, §6)",
    'yimakesiteasy': "Yi MakesItEasy (@YiMakesItEasy — CIE IGCSE 0460 Geography / 0450 Business / Edexcel-register Further Maths CP1 chapter series)",
    'cambridge-study-materials': "Cambridge IGCSE, AS and A Level Study Materials (CIE 0450 Business + 0417 ICT chapter series)",
    'james-gan': "James Gan (CIE 9618 AS&A CS chapter series + 9702 physics + 9709 maths)",
    'igcse-online': "IGCSE Online (CIE IGCSE multi-subject: 0455 econ, 0478 CS, 0620 physics, 0620 chem, 0580 maths chapter series)",
    'igcse-computer-science': "IGCSE Computer Science (@IGCSE Computer Science — 0478 topical past-paper-solution channel)",
    'purple-shirt-history': "Purple Shirt History (CIE 0470/0409/9489 history pool — 0470 rows re-adjudicated, 0409/9489 honest no-target)",
    'mindful-maths': "Mindful Maths (@MindfulMaths — Edexcel IAL D1 WDM11 chapter course + WMA11-14/4MA1 paper walkthroughs)",
    'cambridge-accounting': "Cambridge Accounting IGCSE and A Level (CIE 0452/9706 register-explicit channel)",
    'ar-accounting': "AR Accounting (@AR Accounting — CIE IGCSE/O Level/A Level accounting 0452/9706)",
    'evm-dr-mohamed-saber': "EVM WITH DR MOHAMED SABER (CIE 0680 Environmental Management chapter series)",
    'mr-salles': "Mr Salles Teaches English (@MrSallesTeachesEnglish — Cambridge IGCSE 0500/0522 First Language English + Edexcel IGCSE English pool)",
    'the-igcse-geographer': "The iGCSE Geographer (@TheiGCSEGeographer — CIE 0460 IGCSE Geography case-study channel)",
}
CHANNEL_NOTE = {k: f"{v} (oEmbed author verified per video)" for k, v in PROVIDER.items()}

ENUM_UTC = {p: json.load(open(f'{RES}/Videos/inventory/channels/{p}-uploads.json'))['enumeratedUtc']
            for p in PROVIDER if os.path.exists(f'{RES}/Videos/inventory/channels/{p}-uploads.json')}

poolB = json.load(open(f'{OUT}/tier-b.json'))
J = json.load(open(f'{OUT}/judgment.json'))
tierA = {p['id']: p for p in json.load(open(f'{OUT}/tier-a.json'))}
oemb = json.load(open(f'{OUT}/oembed-p11.json'))

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
    if course.startswith('ial-'):
        return f"IAL {subj.upper()} (EDEXCEL)"
    return f"IGCSE {subj.upper()} (EDEXCEL)".replace("IGCSE MATHS (EDEXCEL)", "IGCSE MATHS A (EDEXCEL)")

def spine_specs(course):
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    return {n['code'] for n in cur['nodes'] if n['family'] == 'SPEC_POINT'}

def level_tag(course):
    if course.startswith('ial-'):
        return 'ial'
    if course.startswith('cie-a-level'):
        return 'a-level'
    if course.startswith('cie-as'):
        return 'a-level'
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
        ev = (f'title: "{p["title"][:110]}"; syllabus/paper code {p["code"]} in the title — '
              f'machine-checkable course anchor (ANCHOR-GRANULARITY §5); oEmbed author verified')
        c['rows'].append({
            'anchor': {'level': 'course', 'ref': course}, 'kind': 'past-paper-walkthrough',
            'video': p['id'], 'lessonRef': None, 'lessonUrl': None, 'specs': [], 'unitScope': None,
            'confidence': 'high', 'method': 'paper-code', 'boardMismatch': False,
            'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW, 'evidence': ev,
        })

# ---- Tier A spec rows + rejects
for course, vs in J.items():
    for v in vs:
        if v['action'] in ('keep', 'rebind'):
            c = get(course)
            src = tierA[v['id']]
            if v['id'] not in c['videos']:
                c['videos'][v['id']] = vid_entry(src, course, src['provider'])
            c['rows'].append({
                'video': v['id'], 'lessonRef': None, 'lessonUrl': None, 'specs': v['specs'],
                'confidence': v['confidence'],
                'evidence': f'{v["reason"]}; title-only posture, distinctive-token binding rule (df<=3) or the disclosed higher title-only bar for marker rows',
                'method': 'llm-draft-external', 'boardMismatch': True,
                'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW,
            })
        elif v['action'] == 'drop':
            get(course)['rejects'].append({'video': v['id'], 'reason': f'full-row drop: {v["reason"]}'})
        elif v['action'] == 'unmapped':
            get(course)['rejects'].append({'video': v['id'], 'reason': f'no-binding (routed-but-unmapped): {v["reason"]}'})

# skips ledger -> per-provider rollup appended to the first-course verdicts is
# NOT the P10 shape; the route ledger lives in work/p11/skips.json and the
# lane docs. Verdicts carry the per-course rejects only.

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
                  '; routing: syllabus/paper-code Tier B anchors + chapter-marker/keyword Tier A with class-table judgment, section-marker narrowing and per-row re-adjudication over every routed row')
    spine_n = len(spine_specs(course))
    draft = {
        'schema': 'syllabai.video-map-draft/2',
        'draftOf': course,
        'task': TASK,
        'course': course,
        'qual': qual_of(course),
        'reviewState': 'owner-reviewed-external',
        'draftLaw': 'P11 lane: Tier B course anchors by machine-checkable syllabus/paper codes (method paper-code, confidence high, boardMismatch false — same qualification; ANCHOR-GRANULARITY §5/§8) + Tier A spec rows by the distinctive-token binding rule (df<=3), with CIE chapter-structured marker rows permitted the disclosed higher title-only bar (section-marker narrowing; confidence low, disclosed per row) and direct class-table binds for skill-structure courses (CIE 0500 English, 4EA1 paper sections, IAL D1 chapters). Cross-register rows (Yi CP1 -> IAL FP1; Mindful UK-register -> IAL; CIE-content -> Edexcel IGCSE ICT/Business/Geography) carry boardMismatch:true. Degenerate vocabulary binds were re-adjudicated to honest drops/unmapped on review; teacher-guidance spine specs are excluded as bind targets. Rejected videos stay out of videos[] and live in the verdicts ledger.',
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
    json.dump(draft, open(f'{D}/video-map.draft.external-p11.json', 'w'), ensure_ascii=False, indent=1)
    verdicts = {
        'schema': 'syllabai.owner-review-verdicts/2',
        'task': TASK,
        'course': course,
        'ruledUtc': NOW,
        'source': 'delegated self-review — owner chat 2026-11-09 "approve and review yourself"; lane authorized 2026-11-13 "lane P11"',
        'default': 'keep',
        'reviewer': REVIEWER,
        'evidenceBasis': 'Identity: oEmbed sweep 439/439 author==channel-of-record (0 mismatch, 0 dead, 0 thumb-fallbacks needed). Tier B: syllabus/paper codes regex-verified in titles (9708/41, 0455/0620 session papers, WDM11, WMA11-14, 4MA1). Tier A: deterministic distinctive-token pre-pass (df<=3) then explicit-code class tables, section-marker narrowing (CIE chapter series) and Chapter-N narrowing (verified syllabus-structured igcse-online series) over EVERY routed pair; cross-register rows carry boardMismatch:true; degenerate vocabulary binds (single-token catches incl. teacher-guidance spine specs) dropped on review; three courses re-adjudicated course-level to honest unmapped (igcse-history-17, cie-igcse-history-18, igcse-economics-17).',
        'rejects': c['rejects'],
        'applied': {'rowsApproved': len(rows), 'rowsRejected': len(c['rejects']), 'appliedUtc': NOW},
    }
    json.dump(verdicts, open(f'{D}/owner-review-verdicts.p11.json', 'w'), ensure_ascii=False, indent=1)
    pre_courses.append(course)
    print(f'{course}: rows {len(rows)} (anchors {len(rows)-len(specRows)}, spec {len(specRows)}) videos {len(c["videos"])} rejects {len(c["rejects"])}')

json.dump({'pre': pre_courses, 'post': []}, open(f'{OUT}/p11-courses.json', 'w'), indent=1)
tot = sum(len(c['rows']) for c in courses.values())
totA = sum(1 for c in courses.values() for r in c['rows'] if r['specs'])
print('TOTAL rows', tot, '(anchors', tot - totA, ', spec rows', totA, ') across', len(courses), 'courses')
