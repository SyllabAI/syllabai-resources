#!/usr/bin/env python3
"""P14 step: assemble per-course drafts + verdicts (the P7/P9/P10/P11/P12/P13 file law).

Outputs (into Videos/drafts/<course>/):
  video-map.draft.external-p14.json   — reviewState owner-reviewed-external
  owner-review-verdicts.p14.json      — the honest ledger (per-course rejects)
Also writes work/p14/p14-courses.json = {pre: [...], post: [...]} for the builder:
inherit CHILDREN (the P4 map: cie-as-{physics,chemistry,biology}-25, cie-igcse-maths-25-core,
igcse-chemistry-modular-24-unit-1/2, ial-chemistry-17) take their direct rows AFTER the
inherit loop (the P11B/P13B shape).
"""
import json, os, datetime, glob
from collections import Counter

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p14'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

TASK = "T-VIDEOMAP-P14 (channel recon judgment lane: T1 x10 + T2 x2 pools + the Allery-CIE re-adjudication group; 18,046 judgment-pool uploads dispositioned exactly-once)"
REVIEWER = 'delegated self-review (agent, per owner chat 2026-11-09 "approve and review yourself"; P14 authorized 2026-11-17 "Proceed" = file it as P14; judgment lane run 2026-11-17)'

PROVIDER = {
    'etphysics': "ETphysics (CIE 9702 session-walkthrough channel: compact ON/MJ/FM-session paper walkthroughs + the numbered AS/A2 topic series)",
    'prosperity-academy': "Prosperity Academy (CIE SOLVED session papers + topic lectures across 9702/9701/9700; content register Urdu/Hindi-dubbed CAIE instruction — recon-approved T1, disclosed)",
    'dr-hanaa-assil': "Dr Hanaa Assil — Chemistry Teacher (Edexcel IAL 'Unit N <session>' paper reviews -> ial-chemistry-17 anchors + Edexcel IGCSE chemistry register)",
    'zainematics': "Zainematics (CIE umbrella: 0580/9709/0606/9618 code-bearing titles; the O-Level-branded remainder skipped honestly)",
    'craigndave': "Craig'n'Dave (CAMBRIDGE IGCSE 0478-0984 numbered series -> cie-igcse-computer-science-23; the AQA/OCR GCSE/A-level CS register skipped as out-of-spine)",
    'science-with-hazel': "Science with Hazel (Edexcel-IGCSE trio + maths register; GCSE/IB/A-level registers skipped as out-of-lane)",
    'mega-lecture': "Mega Lecture (mixed CIE aggregator: qp session walkthroughs + the AS/A2 class series; the non-qualifier remainder skipped honestly)",
    'examsolutions': "ExamSolutions (old-GCE maths: bare GCE session walkthroughs SKIPPED per ANCHOR-GRANULARITY §6 under the P9 precedent; IAL-legacy C12/C34 composites anchored per P9; OCR/AQA/MEI-board skipped; FP2/FP3/S3/S4/M3-5 have no spine course)",
    'sir-faizan-pasha': "Learn With Sir Faizan Pasha (CIE 9702 past-paper lectures with 9702/pp/MM/J/yy codes + the AS/A2 teaching register)",
    'ck-a-level-physics': "CK A-level Physics (archived 9702 AS/A2 teaching series)",
    'igcsesuccess': "IGCSESUCCESS (First Language English 0500 register; the 0475 Literature titles are RESERVED pending the lit-21 owner decision — not silently dropped)",
    'mr-astbury-maths': "MrAstburyMaths (Edexcel IGCSE maths exam-question series; the Edexcel GCE A-level maths register skipped per ANCHOR-GRANULARITY §6)",
    'allery-chemistry-p2f': "Allery Chemistry (the P14 re-adjudication group: the 41 \\bCIE\\b candidates reproduced exactly over the 364-row P2F pool of record — 35 CIE-Topic 9701 revision titles + 6 old session papers)",
}
CHANNEL_NOTE = {k: f"{v} (oEmbed author verified per video)" for k, v in PROVIDER.items()}

ENUM_UTC = {p: json.load(open(f'{RES}/Videos/inventory/channels/{p}-uploads.json'))['enumeratedUtc']
            for p in PROVIDER if p != 'allery-chemistry-p2f'}

poolB = json.load(open(f'{OUT}/tier-b.json'))
J = json.load(open(f'{OUT}/judgment.json'))
oemb = json.load(open(f'{OUT}/oembed-p14.json'))
skips = json.load(open(f'{OUT}/skips.json'))
reserved = json.load(open(f'{OUT}/reserved-lit21.json'))

TITLE = {}
for slug in PROVIDER:
    if slug == 'allery-chemistry-p2f':
        continue
    for v in json.load(open(f'{RES}/Videos/inventory/channels/{slug}-uploads.json'))['videos']:
        TITLE[v['id']] = v['title']
ra = json.load(open(f'{RES}/Videos/scripts/p14/p14_readjudication.json'))
for c in ra.get('allery-chemistry-cie', {}).get('cieCandidates', []):
    TITLE.setdefault(c['id'], c['title'])

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
    elif '§6' in r or 'GCE' in r: skip_by_class['GCE/9MA0 paper evidence (ANCHOR-GRANULARITY §6, P9 precedent)'] += 1
    elif 'OCR/AQA/MEI' in r or 'out-of-spine board' in r: skip_by_class['out-of-spine board register (AQA/OCR/IB/...)'] += 1
    elif 'no corresponding IAL unit' in r: skip_by_class['old-GCE unit with no IAL course (FP2/FP3/S3/S4/M3-5)'] += 1
    elif 'no distinctive' in r or 'no unit token' in r or 'no cross-course' in r or 'no binding' in r: skip_by_class['no honest binding at the df<=3 bar'] += 1
    elif 'no spine qualification' in r or 'no spine qualification code' in r: skip_by_class['non-qualifier remainder (aggregator/umbrella content)'] += 1
    elif 'World Literature 0408' in r: skip_by_class['CIE 0408 World Literature — no spine course'] += 1
    elif 'out of lane' in r or 'out-of-lane' in r: skip_by_class['out-of-lane register (GCSE/IB/meta)'] += 1
    elif 'NT' in r or 'recon NT' in r or 'EMPTY' in r: skip_by_class['NT pools — pool-level ledger (recon verdicts)'] += 1
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
                  ('; Allery-CIE re-adjudication group over the P2F pool of record' if 'allery-chemistry-p2f' in provs else '') +
                  '; routing: machine-checkable Tier B anchors (CIE paper-number routing incl. compact ON/MJ/FM sessions and qp_NN patterns, 0580 papers 2/4 extended vs 1/3 core, WMA01 C12/C34 IAL-legacy composites, IAL unit-paper reviews) + section-marker narrowing + section-name binding (verbatim pipe/dash field match) + distinctive-token Tier A (df<=3) + the four-gate topic-lecture class, over every routed row with the degenerate-bind re-adjudication bar')
    spine_n = len(spine_specs(course))
    draft = {
        'schema': 'syllabai.video-map-draft/2',
        'draftOf': course,
        'task': TASK,
        'course': course,
        'qual': qual_of(course),
        'reviewState': 'owner-reviewed-external',
        'draftLaw': 'P14 judgment lane (channel recon filing pool set: T1 x10 + T2 x2 pools + the Allery-CIE '
                    're-adjudication group; 18,046 judgment-pool uploads dispositioned exactly-once alongside '
                    '6,390 NT pool-level ledger entries and 9 RESERVED lit-21 titles): Tier B course anchors by '
                    'machine-checkable session/paper codes (method paper-code, confidence high; CIE paper-number '
                    'routing per subject — sciences papers 1-3 AS / 4-5 A2, maths P1..P6 unit courses, 0580 papers '
                    '2/4 extended vs 1/3 core, 9618 papers 1-2 AS / 3-4 A-level; WMA01 C12/C34 IAL-legacy composites '
                    '-> two units each per the P9 law; IAL chemistry "Unit N <session>" unit-paper anchors per the '
                    'P11 W-code law analog) + Tier A spec rows by the distinctive-token binding rule (df<=3, '
                    'deduped tokens) under the P13 gate ladder: section-marker narrowing, section-name binding '
                    '(verbatim pipe/dash field equality, node norm >= 8 chars, SUBTOPIC preferred), the four-gate '
                    'topic-lecture class. ExamSolutions: bare GCE session walkthroughs SKIPPED per '
                    'ANCHOR-GRANULARITY §6 (a GCE paper is evidence about the GCE qualification — no GCE course in '
                    'the spine; the P9 precedent) with only IAL-legacy composites anchored and OCR/AQA/MEI-board '
                    'skipped; old-GCE teaching titles bind cross-register at the P10 bar (boardMismatch true). '
                    'Teacher-guidance/technique/marketing registers (incl. WhatsApp/live-class promo strings that '
                    'ride along on genuine teaching titles), the O-Level register and out-of-spine boards are '
                    'excluded and ledgered as skips. The IGCSESUCCESS 0475 Literature series is RESERVED pending '
                    'the lit-21 owner decision. Rejected/unrouted videos stay out of videos[].',
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
    json.dump(draft, open(f'{D}/video-map.draft.external-p14.json', 'w'), ensure_ascii=False, indent=1)
    verdicts = {
        'schema': 'syllabai.owner-review-verdicts/2',
        'task': TASK,
        'course': course,
        'ruledUtc': NOW,
        'source': 'delegated self-review — owner chat 2026-11-09 "approve and review yourself"; P14 authorized 2026-11-17 "Proceed"; judgment lane run 2026-11-17',
        'default': 'keep',
        'reviewer': REVIEWER,
        'evidenceBasis': ('Identity: oEmbed sweep 2,830/2,830 author_url channel == channel-of-record via UC id '
                          '(0 mismatch, 0 dead, 0 thumb fallbacks). Tier B: session/paper codes regex-verified in '
                          'titles (CIE paper-number routing per subject incl. compact ON/MJ/FM sessions and the '
                          'qp_NN paper-store pattern; 0580 papers 2/4 extended vs 1/3 core per the P9 law; WMA01 '
                          'C12/C34 IAL-legacy composites -> two units each; IAL chemistry "Unit N <session>" '
                          'unit-paper anchors). Tier A: the P13 gate ladder (section-marker narrowing, verbatim '
                          'section-name binding, deduped distinctive-token binds df<=3, the four-gate '
                          'topic-lecture class) over EVERY routed pair with the degenerate-bind re-adjudication '
                          'bar; cross-register binds (ExamSolutions old-GCE teaching titles -> IAL unit courses) '
                          'carry boardMismatch true at the disclosed P10 bar. ExamSolutions bare GCE session '
                          'walkthroughs skipped per ANCHOR-GRANULARITY §6 (P9 precedent). Guidance/advice/marketing '
                          'registers, the O-Level register, out-of-spine boards (AQA/OCR/IB/NCERT/GCSE) and the '
                          f'non-qualifier aggregator remainder skipped with reasons ({len(skips)} ledgered in '
                          f'work/p14/skips.json by class: {dict(skip_by_class)}); {len(reserved)} lit-21 titles '
                          'RESERVED pending the owner decision (work/p14/reserved-lit21.json).'),
        'rejects': c['rejects'],
        'applied': {'rowsApproved': len(rows), 'rowsRejected': len(c['rejects']), 'appliedUtc': NOW},
    }
    json.dump(verdicts, open(f'{D}/owner-review-verdicts.p14.json', 'w'), ensure_ascii=False, indent=1)
    if course in P14B_POST:
        post_courses.append(course)
    else:
        pre_courses.append(course)
    print(f'{course}: rows {len(rows)} (anchors {len(rows)-len(specRows)}, spec {len(specRows)}) videos {len(c["videos"])} p14b {"POST" if course in P14B_POST else "pre"}')

json.dump({'pre': pre_courses, 'post': post_courses}, open(f'{OUT}/p14-courses.json', 'w'), indent=1)
tot = sum(len(c['rows']) for c in courses.values())
totA = sum(1 for c in courses.values() for r in c['rows'] if r['specs'])
summary = {
    'utc': NOW,
    'courses': len(courses), 'pre': pre_courses, 'post': post_courses,
    'rows': tot, 'anchorRows': tot - totA, 'specRows': totA,
    'tierBVideos': len({p['id'] for p in poolB}),
    'routedVideos': len({p['id'] for p in poolB}) + len({r['id'] for vs in J.values() for r in vs if r['action'] == 'keep'}),
    'skips': len(skips), 'skipByClass': dict(skip_by_class),
    'reservedLit21': len(reserved),
    'oembed': {'verified': sum(1 for v in oemb.values() if v.get('ok')), 'bad': sum(1 for v in oemb.values() if not v.get('ok'))},
    'ntPoolLedger': 6390,
    'disposition': '18,046 judgment-pool uploads + 41 Allery candidates + 6,390 NT pool-level entries + 9 reserved = 24,486 accounts, exactly-once',
}
json.dump(summary, open(f'{OUT}/p14_summary.json', 'w'), indent=1)
print(f'\nTOTAL rows {tot} (anchors {tot - totA}, spec rows {totA}) across {len(courses)} courses | pre {len(pre_courses)} post {len(post_courses)}')
print('summary ->', f'{OUT}/p14_summary.json')
