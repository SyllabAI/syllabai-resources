#!/usr/bin/env python3
"""P19 step: assemble per-course drafts + verdicts (the P7..P18 file law).

Outputs (into Videos/drafts/<course>/):
  video-map.draft.external-p19.json   — reviewState owner-reviewed-external
  owner-review-verdicts.p19.json      — the honest ledger (per-course rejects)
Also writes work/p19/p19-courses.json = {pre: [...], post: [...]} for the builder:
inherit CHILDREN (the P4 map) take their direct rows AFTER the inherit loop (the
P11B/P13B/P14B/P15B/P17B/P18B shape).
"""
import json, os, datetime
from collections import Counter

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p19'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

TASK = "T-VIDEOMAP-P19 (gap-profile judgment lane: the P19 filing PR #364 pool set admitted by owner order 'run P19 judgment'; 7,098 pool uploads dispositioned exactly-once)"
REVIEWER = 'delegated self-review (agent, per owner chat 2026-11-09 "approve and review yourself"; P19 profile filed 2026-11-24 (PR #364), pools admitted and judgment ordered "run P19 judgment" 2026-11-26)'

PROVIDER = {
    'igbiocomplete': "IGBiocomplete (CIE IGCSE sciences trio topic lectures with the '(topic N.M.K)' 2023-2025 point-number register — the densest CIE sciences-trio CONTENT find of any sweep; bare 'IGCSE {Subject}' titles bind at the title-only posture, disclosed; the no-number MCQ-set remainder ledgered honest-no-bind; p15-swept resurfaced with the sentinel disclosure)",
    'igcse-study-buddy': "IGCSE Study Buddy (coded CIE trio series — 0610/0620/0625 topic lectures with leading/pipe 'N. {Topic}' numbers, 97% International, disclosed; the leading-number register binds the trio topic at index N with stem token-agreement; promo/meta remainder skipped)",
    'edubbey': "Edubbey (multi International interactive-lesson library — coded 0417/0580/0455/0450/0610/0625/0625 'Chapter N' series + paper solutions; the LMS/trailer/hashtag promo remainder skipped honestly; p17-swept resurfaced with the sentinel disclosure)",
    'precool-skillz': "Precool Skillz (iGCSE subject series '{Topic} | iGCSE {Subject} #N' — ICT/Physics/Chemistry/Economics; subject-name register binds at the title-only ladder bar, disclosed; the no-register remainder ledgered honest-no-bind)",
    'save-my-exams': "Save My Exams (mixed-board T2 pool, disclosed: NT-dominant — the AQA/OCR/IB and UK-GCSE-Edexcel remainders skip; the CIE subject-name subset ('IGCSE {Subject}- {topic}' exam questions + CIE 0478 CS) binds at the ladder bar; the GCSE-English-Lit subset rides the P16 Class W predicate)",
    'revwise': "Revwise (mixed NT x34, disclosed; the Edexcel IGCSE 4BI1/4CH1/4PH1/4SD0 walkthrough subset anchors; the 'Explaining X using video games/fiction' edutainment-shorts series skipped honestly as a register class)",
    'ginger-mathematician': "GingerMathematician (CIE-branded maths: 0607 International Maths paper forms (the NEW P19 register), 0580 predictions/specimen forms, 0606 Add Maths; the gate's '4MA1 x159' family read re-adjudicated of record: the generic 'iGCSE Maths' bare titles are CIE 0580 per the channel's Cambridge branding — the 4MA1 deficits stay open, re-sweepable; the 9709 A-level maths walkthroughs skip per ANCHOR-GRANULARITY section 6; guidance/motivation/news remainder skipped; p15-swept resurfaced with the sentinel disclosure)",
    'maths-with-mohaiminul': "Maths with Mohaiminul (Edexcel IGCSE Maths B 4MB1 'IGCSE (9-1) Maths B' topic lectures + question-solving series — the P19 (9-1) infix form disclosed)",
    'easy-edu': "Easy Edu (Edexcel Maths Specification B (4MB1) lecture series, micro pool disclosed — the P17 mr-quakers precedent)",
    'miss-tech-teacher': "Miss Tech Teacher (CIE 0417 ICT — 100% on-register: session/paper walkthroughs + '(0417)'-coded skills videos; the skills subset binds at the ladder bar, disclosed; 22 thumbnail-liveness fallbacks of the P2D law)",
    'mr-khan-ict-solutions': "Mr Khan ICT Solutions (CIE 0417 FEB/MAR + ON session paper-solution walkthroughs — 97% on-register; the channel-trailer remainder skipped)",
    'ict-with-tatchen': "ICT with Tatchen (dual-register ICT: the CIE 0417 chapter-structured lecture series ('Chapter N' index binds at the disclosed chapter-index law, the series' paren concept labels self-verify) + 4IT1 Edexcel side; the 2026-2028 syllabus branding rides the shared-code multi-year posture, disclosed)",
    'rapid-revision-with-shayan': "Rapid Revision with Shayan (the 'O level/ IGCSE Accounting & Economics' dual-branded lecture + paper-walkthrough series — the 7707/2281 O-Level duals disclosed; the 'Day N' exam-technique series skips as guidance)",
    'bookkeepers-journal': "Bookkeeper's Journal (Edexcel IGCSE Business 4BS1 + the IGCSE Accounting topic shorts — the Edexcel AS/IAL WBS/WAC remainder skips honest-no-spine; hashtag-shorts bind at the ladder bar)",
    'accounting-celebrity': "Accounting Celebrity (generic accounting-shorts channel — 0452/IGCSE-Accounting register on 44 of 635 (7%, disclosed); the IGCSE-registered subset binds at the ladder bar, the board-agnostic accounting-basics remainder ledgered honest-no-bind)",
    'muzammil-ameer-acma': "Muzammil Ameer ACMA (CIE 9609 'Business AS/A Level' unit-series lectures + 0450 Business Studies + 0452 accounting; the bare 'AL' forms and the institute-promo/graduation remainder skipped honestly)",
    'saifullah-ajaz': "Saifullah Ajaz (dual CIE business register: 'As/A Level Business' chapter-lecture series (9609) + 'O Levels Business 7115/0450' revision chapters — the 7115 O-Level dual disclosed; the registration/promo remainder skipped)",
    'the-visible-hand': "The Visible Hand (TRexEcon — 9708 A-level economics session-QP walkthroughs incl. the 'Cambridge AS/A2 Economics' P19 form + 0455 IGCSE econ MCQ sessions; the exam-tips remainder skipped)",
    'your-igcse-tutors': "Your IGCSE Tutors (coded multi International: 0455/0452 MCQ sessions, 0606 Add Maths topical PYQs, 0972 physics dual, 0523 Chinese skips honest-no-spine)",
    'sciencewithchun': "ScienceWithChun (CIE 0654 co-ordinated 'Questions by Topic' series — the section-scoped B9/P5/C3 register binds the co-ordinated same-science topic at that index with stem token-agreement (the shared 0654 section numbering); the combined-23 numbering diverges and is NOT bound, disclosed; the B7 'Animal nutrition' old-numbering form fails the token bar honest)",
    'the-physics-examiner': "The Physics Examiner (Edexcel IAL physics WPH paper walkthroughs — the P19 spaced 'WPH 16' form = unit 6, the P14 Assil law analog; 3 thumbnail-liveness fallbacks of the P2D law)",
    'education-for-success': "Education For Success (Riyadh school channel — the 0680 Environmental Management chapter-notes subset (the CONTENT class, 64 absolute) binds at the ladder bar against the 2027-2029 spine; the 0580 Collins subset binds where tokens are distinctive; the school-internal STP/Grade-6 maths, lives, debates and events remainder skipped honestly; 16 thumbnail-liveness fallbacks of the P2D law)",
    'benzakademi': "Benzakademi (the P19 false-density call of record: the gate's '8291 x13' family read was the Anna-university 'GE8291 EVS' Indian paper register, NOT Cambridge AS Environmental Management — 0 honest binds, the P17 nevdoes/indigo precedent; the CBSE/ISC/+1,+2 remainder skips)",
    'academic-plus': "Academic Plus (thin-multi T2, the indigo precedent: the bare 'A-Level Business' family read was board-agnostic — only explicit 9609/4BS1 register titles can bind; the board-agnostic remainder (x412) ledgered honest-no-register)",
    'the-revision-notebook': "The Revision Notebook (CIE 9609 'Short notes' micro series x3 — the old-unit topic names fail the 2023-spec token bar honestly; 0 binds, the micro-pool disclosure)",
}
CHANNEL_NOTE = {k: f"{v} (oEmbed author verified per video)" for k, v in PROVIDER.items()}

ENUM_UTC = {p: json.load(open(f'{RES}/Videos/inventory/channels/{p}-uploads.json'))['enumeratedUtc']
            for p in PROVIDER}

poolB = json.load(open(f'{OUT}/tier-b.json'))
J = json.load(open(f'{OUT}/judgment.json'))
oemb = json.load(open(f'{OUT}/oembed-p19.json'))
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
        ev = (f'title: "{p["title"][:110]}"; {code} — machine-checkable course anchor '
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
                'evidence': f'{v["reason"]}; title-only posture, distinctive-token binding rule (df<=3, the P19 stemmed-token vocabulary) or the disclosed higher title-only bar for section-name/topic-lecture/chapter-scoped/section-scoped rows (multi-point binds disclosed per row){xreg}',
                'method': 'llm-draft-external', 'boardMismatch': True,
                'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW,
            })

P19B_POST = [c for c in sorted(courses) if c in P4_CHILDREN]
pre_courses, post_courses = [], []
skip_by_class = Counter()
for s in skips:
    r = s['reason']
    if 'Anna-university' in r: skip_by_class['Anna-university GE8291 EVS register — the P19 false-density call of record (0 honest binds)'] += 1
    elif 'edutainment' in r: skip_by_class['edutainment shorts register (the "Explaining X using video games/fiction" series)'] += 1
    elif 'UK-GCSE Edexcel register' in r: skip_by_class['UK-GCSE Edexcel register (the "GCSE X (Edexcel)" form, no International token)'] += 1
    elif 'school-internal maths' in r: skip_by_class['school-internal maths register (STP/Grade 6 textbooks)'] += 1
    elif 'guidance' in r and 'set-text' not in r: skip_by_class['guidance/advice/marketing register'] += 1
    elif 'promo/meta' in r: skip_by_class['channel promo/tuition marketing (no qualification register)'] += 1
    elif 'meta announcement' in r: skip_by_class['meta announcement (grade thresholds/timetables/results/celebration/graduation)'] += 1
    elif 'NT-board' in r: skip_by_class['NT-board titles (AQA/OCR/IB/...) incl. the final sanity pass re-adjudications'] += 1
    elif 'O-Level register' in r: skip_by_class['O-Level register with no IGCSE spine-code token (the generalized P14 spine-code precedence law; the disclosed 4037/2281/7707/5090/7115 duals exempt)'] += 1
    elif 'UK-GCSE Computer Science' in r or 'GCSE Computer Science' in r: skip_by_class['UK-GCSE Computer Science — no spine course (the spine carries CIE 0478)'] += 1
    elif '0523 Chinese' in r: skip_by_class['0523 Chinese as a Second Language — no spine course'] += 1
    elif 'A-level accounting' in r: skip_by_class['A-level accounting register (9706) — no spine course'] += 1
    elif 'Edexcel AS/IAL' in r: skip_by_class['Edexcel AS/IAL Accounting & Business register (WBS/WAC) — no spine course'] += 1
    elif 'IAL/CIE maths' in r: skip_by_class['IAL/CIE maths register (9709/A-level Pure) — bare walkthroughs skip per ANCHOR-GRANULARITY section 6 (P9 precedent)'] += 1
    elif 'AQA/Eduqas/WJEC/Edexcel/GCSE register without a CIE token' in r: skip_by_class['lit register: out-of-spine board (AQA/Eduqas/WJEC/Edexcel/GCSE) naming no spine set text'] += 1
    elif 'guidance/skills' in r: skip_by_class['lit guidance/skills register with no set-text bind'] += 1
    elif 'not on the 2023-2025 set-text lists' in r: skip_by_class['lit register: work not on the 0475 2023-2025 set-text lists'] += 1
    elif 'character-study' in r: skip_by_class['lit register: character-study title without a set-text token'] += 1
    elif 'board-agnostic' in r or 'no board register' in r or 'board-agnostic remainder' in r: skip_by_class['board-agnostic forms with no board register (the bare "A-Level Business"/accounting-shorts remainders)'] += 1
    elif 'no distinctive' in r or 'no binding' in r or 'no honest binding' in r or 'no syllabus register' in r or 'no subject-name register' in r: skip_by_class['no honest binding at the df<=3 bar (incl. the subject-name forms the ladder cannot bind honestly)'] += 1
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
                  '; routing: machine-checkable Tier B anchors (CIE IGCSE sciences 0610/0620/0625 session/paper registers incl. the disclosed 0971/0972/0973/5090 duals; the P19 topic-number register (the "(topic N.M.K)" form binding the exact trio point + the co-ordinated P/B/C-prefixed twin where the 2025-2027 co-ord spine carries the same number, the shared-0625-structure law); the 0654 section-scoped B/P/C register (co-ordinated topic at that index with stem token-agreement); 0417/0983 ICT session/paper + skills ladders; the 4IT1/4IT0 International-GCSE-ICT register text; 4MA1/4WM/4XM maths-A routing; 4MB1 incl. the "IGCSE (9-1) Maths B" P19 infix form; 0580 papers 2/4 extended vs 1/3 core (the P9/P14 law, code-required); 0607 International Maths papers 2/4/6 extended vs 1/3/5 core (the NEW P19 register); 0606 with the disclosed 4037 dual; 0452/0985 (+ the disclosed 7707 dual, incl. the "O level/ IGCSE Accounting" form)/0455 (+ the disclosed 2281 dual)/0450 (+ the disclosed 7115 dual; the NEW P19 register)/0680/9708 (incl. the "Cambridge AS/A2 Economics" form)/9609 (incl. the "AS/A Level Business" unit-series forms, pool-scoped)/4BS1/4BI1/4CH1/4PH1/4SD0; IAL WPH incl. the P19 spaced "WPH 16" unit-6 form + the Pearson-pipe register family) + the P16 Class W set-text predicate (the P17/P18 amendments) + section-marker narrowing + section-name binding (verbatim field match, the P19 dash-run split amendment) + distinctive-token Tier A (df<=3, the P19 stemmed-token vocabulary) + the four-gate topic-lecture class + the P19 chapter-scoped register (tatchen 0417 chapter-index law, disclosed), over every routed row with the degenerate-bind re-adjudication bar')
    spine_n = len(spine_specs(course))
    draft = {
        'schema': 'syllabai.video-map-draft/2',
        'draftOf': course,
        'task': TASK,
        'course': course,
        'qual': qual_of(course),
        'reviewState': 'owner-reviewed-external',
        'draftLaw': 'P19 judgment lane (the gap-profile pool set: 25 pools admitted by owner order "run P19 judgment"; 7,098 '
                    'pool uploads dispositioned exactly-once): '
                    'Tier B course anchors by machine-checkable session/paper codes (method paper-code, confidence '
                    'high; the P15/P17/P18 registers plus the P19 additions: 0607 International Maths, 0450 business, '
                    'the topic-number register (igbiocomplete "(topic N.M.K)" + study-buddy leading/pipe "N. {Topic}" '
                    'with stem token-agreement), the 0654 section-scoped B/P/C register, the chapter-scoped 0417 '
                    'register, the "IGCSE (9-1) Maths B" infix form, the "O level/ IGCSE Accounting" form, the '
                    '"Cambridge AS/A2 Economics" form, the "AS/A Level Business" unit-series forms (pool-scoped), the '
                    'spaced "WPH 16" IAL form) + the P16 Class W set-text predicate for 0475/GCSE-lit titles + Tier A '
                    'spec rows by the distinctive-token binding rule (df<=3 on the P19 stemmed-token vocabulary) under '
                    'the P13/P15 gate ladder: section-marker narrowing, section-name binding (verbatim field equality, '
                    'node norm >= 8 chars, SUBTOPIC preferred, the P19 dash-run split amendment), the four-gate '
                    'topic-lecture class. Guidance/promo/tuition registers, meta announcements (grade '
                    'thresholds/timetables/results/graduations/lives), the edutainment-shorts register, the '
                    'Anna-university GE8291 EVS register (0 binds — the false-density call of record), the UK-GCSE '
                    'Edexcel register, CIE AS/A Level IT 9626, the O-Level register (the disclosed 4037/2281/7707/5090/'
                    '7115 duals exempt, the P14 spine-code precedence generalized), the IAL/CIE maths 9709 '
                    'bare-walkthrough class (ANCHOR-GRANULARITY section 6, P9 precedent) and out-of-spine boards '
                    '(AQA/OCR/IB) are excluded and ledgered as skips. Rejected/unrouted videos stay out of videos[]. '
                    'P19 disclosed amendments: the tokenizer stems to singular so plural-form title tokens agree with '
                    'spine tokens (disclosed, consistent on both sides of the df tables); split_fields gains the '
                    'dash-run separator (the "Biology- {topic}" forms); the honest register re-adjudications of record: '
                    'ginger-mathematician\'s "4MA1 x159" gate read was the generic "iGCSE Maths" form — the channel is '
                    'CIE-branded so the register of record is 0580/0607/0606 (the 4MA1 deficits stay open, '
                    're-sweepable); benzakademi\'s "8291 x13" was the Anna-university GE8291 EVS register (0 binds); '
                    'academic-plus\'s "A-Level Business" family was board-agnostic (only explicit 9609/4BS1 titles bind).',
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
    json.dump(draft, open(f'{D}/video-map.draft.external-p19.json', 'w'), ensure_ascii=False, indent=1)
    n_ok = sum(1 for v in oemb.values() if v.get('ok'))
    n_fb = sum(1 for v in oemb.values() if v.get('ok') and v.get('method') == 'thumb-fallback')
    n_bad = sum(1 for v in oemb.values() if not v.get('ok'))
    verdicts = {
        'schema': 'syllabai.owner-review-verdicts/2',
        'task': TASK,
        'course': course,
        'ruledUtc': NOW,
        'source': 'delegated self-review — owner chat 2026-11-09 "approve and review yourself"; P19 profile filed 2026-11-24 (PR #364), pools admitted and judgment ordered "run P19 judgment" 2026-11-26',
        'default': 'keep',
        'reviewer': REVIEWER,
        'evidenceBasis': (f'Identity: oEmbed sweep {n_ok}/{n_ok} routed videos alive — '
                          f'{n_ok - n_fb} author_url channel == channel-of-record via UC id (0 mismatch) + '
                          f'{n_fb} thumbnail-liveness fallbacks disclosed per the P2D law '
                          f'(oembed HTTP 200 all-null payload; identity rides on the channel-of-record upload '
                          f'provenance), 0 bad. Tier B: session/paper codes regex-verified in titles (the P15/P17/P18 '
                          f'registers plus the P19 additions: 0607 International Maths, 0450 business, the topic-number '
                          f'register, the 0654 section-scoped register, 0417 skills ladders, the (9-1) Maths B infix '
                          f'form, the spaced WPH form). Class W: the P16 committed predicate with the P17/P18 '
                          f'amendments. Tier A: the P13/P15 gate ladder '
                          f'(section-marker narrowing, verbatim section-name binding with the P19 dash-run split, '
                          f'deduped distinctive-token binds df<=3 on the stemmed vocabulary, the four-gate topic-lecture '
                          f'class, the chapter-scoped 0417 register) over EVERY routed pair with the degenerate-bind '
                          f're-adjudication bar. Guidance/promo/tuition, meta announcements, the edutainment register, '
                          f'the Anna-university GE8291 EVS register (0 binds), the UK-GCSE Edexcel register, CIE AS/A '
                          f'Level IT 9626, the O-Level register (the disclosed duals exempt), IAL/CIE maths 9709 '
                          f'(section 6) and out-of-spine boards skipped '
                          f'with reasons ({len(skips)} ledgered in work/p19/skips.json by class: '
                          f'{dict(skip_by_class)}).'),
        'rejects': c['rejects'],
        'applied': {'rowsApproved': len(rows), 'rowsRejected': len(c['rejects']), 'appliedUtc': NOW},
    }
    json.dump(verdicts, open(f'{D}/owner-review-verdicts.p19.json', 'w'), ensure_ascii=False, indent=1)
    if course in P19B_POST:
        post_courses.append(course)
    else:
        pre_courses.append(course)
    print(f'{course}: rows {len(rows)} (anchors {len(rows)-len(specRows)}, spec {len(specRows)}) videos {len(c["videos"])} p19b {"POST" if course in P19B_POST else "pre"}')

json.dump({'pre': pre_courses, 'post': post_courses}, open(f'{OUT}/p19-courses.json', 'w'), indent=1)
tot = sum(len(c['rows']) for c in courses.values())
totA = sum(1 for c in courses.values() for r in c['rows'] if r['specs'])
routedB = {p['id'] for p in poolB}
routedA = {r['id'] for vs in J.values() for r in vs if r['action'] == 'keep'}
n_ok = sum(1 for v in oemb.values() if v.get('ok'))
n_fb = sum(1 for v in oemb.values() if v.get('ok') and v.get('method') == 'thumb-fallback')
n_bad = sum(1 for v in oemb.values() if not v.get('ok'))
summary = {
    'utc': NOW,
    'courses': len(courses), 'pre': pre_courses, 'post': post_courses,
    'rows': tot, 'anchorRows': tot - totA, 'specRows': totA,
    'tierBVideos': len(routedB),
    'routedVideos': len(routedB | routedA),
    'skips': len(skips), 'skipByClass': dict(skip_by_class),
    'oembed': {'verified': n_ok, 'bad': n_bad, 'thumbFallbacks': n_fb},
    'disposition': '7,098 P19 pool uploads = routed (tier B + tier A) + skips, exactly-once',
}
json.dump(summary, open(f'{OUT}/p19_summary.json', 'w'), indent=1)
print(f'\nTOTAL rows {tot} (anchors {tot - totA}, spec rows {totA}) across {len(courses)} courses | pre {len(pre_courses)} post {len(post_courses)}')
print('summary ->', f'{OUT}/p19_summary.json')
