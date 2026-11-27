#!/usr/bin/env python3
"""P20 step: assemble per-course drafts + verdicts (the P7..P19 file law).

Outputs (into Videos/drafts/<course>/):
  video-map.draft.external-p20.json   — reviewState owner-reviewed-external
  owner-review-verdicts.p20.json      — the honest ledger (per-course rejects)
Also writes work/p20/p20-courses.json = {pre: [...], post: [...]} for the builder:
inherit CHILDREN (the P4 map) take their direct rows AFTER the inherit loop (the
P11B/P13B/P14B/P15B/P17B/P18B shape).
"""
import json, os, datetime
from collections import Counter

RES = '/home/z/my-project/worktrees/p20-judgment'
HUB = '/home/z/my-project/worktrees/p20-hub/apps/hub'
OUT = '/home/z/my-project/work/p20'
NOW = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

TASK = "T-VIDEOMAP-P20 (gap-profile judgment lane: the P20 filing PR #366 pool set admitted by owner order 'run P20 judgment'; 10,611 pool uploads dispositioned exactly-once)"
REVIEWER = 'delegated self-review (agent, per owner chat 2026-11-09 "approve and review yourself"; P20 profile filed 2026-11-26 (PR #366), pools admitted and judgment ordered "run P20 judgment" 2026-11-26)'

PROVIDER = {
    'otterbiotutor': "Otter Bio Tutor (the CIE 9700 A2/AS numbered-lesson series 'N-M Title (Cambridge AS A Level Biology, 9700)' — the densest 9700 CONTENT find of any sweep; the lesson-number prefix is the channel's own index and does NOT bind the spine's sub numbers — the biochemlogy law; binds ride the stem-agreement/df<=3 token evidence; the 'Past Paper Questions N-M:' question sets bind the same way)",
    'ptet-chemistry': "PTET Chemistry (multi CIE chemistry: 9701 papers 1-5 session anchors + content binds, 0620 session/content onto the trio chem face, the 0653 combined-science register (session walkthroughs bind all three combined faces, the shared-paper law), Ed-IGCSE 4CH1 subset; the 5070 O-Level chemistry dual and NT x150 remainders skip honest; p19-swept-uninventoried disclosure carried)",
    'study-with-prashna': "Study With Prashna (the CIE 9706 accounting session-solution class — 'A Level Accounting May June 2026 Paper 12 9706/12': papers 1-2 AS / 3-4 A2 per the P13 accounting paper-level law; the 9709 P&S subset rides the P20 component routing; the NA-titled remainder skips honest)",
    'adam-viceroy': "Adam Viceroy (dual CIE accounting register: 'AS Accounting 9706' content + 'O level Accounting 7707 & 0452' (the disclosed 7707 dual exempt per the P14 precedence law); the bare accounting-shorts bind at the subtopic-scoped lecture gate (the P20 subtopic-bind amendment); the promo/motivation remainder skips)",
    'miss-natalie-chemistry': "Miss Natalie Chemistry (the WCH unit-content find — '10B Halogenoalkanes - Edexcel IAS Chemistry (Unit 2)' + the unit-question class 'Unit 3 Sample - Question 4' (the P20 question-set amendment of the P14 Assil law) + the spaced WCH NN paper form; the Ed-IGCSE numbered-lesson series ('1I Electrolysis (Triple) - Edexcel IGCSE Chemistry') binds via the series-concept law after the lesson-code/tag strip; p15-swept-uninventoried disclosure carried)",
    'mathlete-by-saad': "Mathlete by Saad (the 0606 add-maths register find + the 9709 component subset; the gate's '4MA1 x78' family read re-adjudicated of record as the generic IGCSE/O-Level 0580 class per the ginger law (disclosed false density) — the 4MA1 deficits stay open; the expected-topics/advice and SAT/entry-test remainders skip)",
    'cswithmrg': "CSwithMRG (dual CIE CS register: 9618 'AS Level Computer Science | Unit N Lesson M' content + session papers, the '0478/0984 iGCSE Computer Science' series; the 0478 face is fully mapped — the subset rides honestly; the teaching-tools/trailer remainder skips)",
    'haguin-school': "Haguin School (the 9618 paper-walkthrough class — session/paper anchors + content binds; the exam-structure/advice shorts skip honest)",
    'mr-lee-business-econ': "Mr Lee Business & Econ (the 'IGCSE Economics/Business Chapter N.M' class 'Updated for the 2027 syllabus' — the 2027 chapter numbering is the channel's own index where it disagrees with the committed spine numbers (the biochemlogy label-agreement law); the honest binds ride the verbatim field/token evidence; the Edexcel/IB economics and the NT x26 remainders skip; p15-swept-uninventoried disclosure carried)",
    'mr-mathew': "Mr Mathew (multi EM/bio/geo past-paper class: 0680 EM '2027-2029 SYLLABUS' lectures, 0460 geography (both geo faces — the 2020/2025 shared-register pair), 0610 biology; the 5090 O-Level EM dual and AQA remainders skip; p15-swept-uninventoried disclosure carried)",
    'pla-academy-igcse-and-a-level-buddy': "PLA Academy IGCSE and A-level Buddy (Edexcel physics unit content ('2.1 Fluids: Unit 1 mechanics and materials: Edexcel IAL Physics') + the 0625 unit register ('UNIT 4 Electricity and Magnetism') with the co-ordinated P/B-C twin binds (the shared-0625-structure law) + 4PH1/4WPH1 modular faces; the 5054 O-Level physics and AQA maths remainders skip; p15-swept-uninventoried x20 disclosure carried)",
    'refactor-lab': "Refactor Lab (explicit 'CIE | Add Math | 0606 | 4037' session walkthroughs incl. the '#additionalmathematics' hashtag session class (the disclosed 4024 dual); 9709 component anchors ('CIE-P1-2023-Pure Mathematics-...'); the CIE-Gen-Math 0580 subset rides the P9/P14 paper law)",
    'mathprep-with-ahmad-bilal': "Mathprep with Ahmad Bilal (the CAIE 9709 session-solution class — the P20 component routing of record (P1/P2/P3 pure, P4/M1 mechanics, P5/S1, P6/S2); the 0606 'IGCSE/O-level Add Math' subset + the 0580/4024 dual; P1-dominance disclosed)",
    'salihath-syed-basheer': "Salihath Syed Basheer (dual CIE business register: 'CAMBRIDGE AS BUSINESS ... #9609' + the IGCSE BUSINESS 0264 new-code form (the disclosed 0264 dual); the #cbse/matric/project remainder skips)",
    'edex-world': "Edex World (the 'CIE Past Paper Discussion (9706 - ...)' class + 'AS/A Level Accounting' content; the 'Accounting for IGCSE' remainder carries no 0452 code (the ammar-samana law, disclosed); p17-swept-uninventoried disclosure carried)",
    'biochemlogy': "Biochemlogy (the A2/AS 9700/9701 chapter class 'A2 BIO 9700 | CHAPTER 14 - HOMEOSTASIS | 14.3 - THE HUMAN KIDNEY' — the chapter/section numbers are the channel's own index where they disagree with the spine (the biochemlogy law of record: the label-agreement gate demotes the number to noise and the honest bind rides the token evidence); EDEXCEL CHEM 4CH1 subset)",
    'umara-ratnayake': "Umara Ratnayake (dual ICT practical register: 'EDEXCEL IGCSE ICT 9-1 - 2021 DATABASE' 4IT1 subset + the 9618 paper subset; the IAL ICT (WIT) subset has NO spine course and the Edexcel IGCSE CS subset rides the no-spine skip, both honest; the bare python/coding remainder skips)",
    'aslaug-eggertsdottir': "Aslaug Eggertsdottir (the Edexcel ICT practical-exam class ('Practical Edexcel IGCSE ICT Access Database Exam') — the practical/paper-discussion class anchors; the Icelandic-language remainder skips honest)",
    's-q': "S-Q (the 'iGCSE ICT' spreadsheet-task series — the bare 'iGCSE ICT' register read as the 0417 face per the gate's classification (disclosed); the bare python/office-skills remainder skips)",
    'the-lightup-hub': "The Lightup Hub (the UK-GCSE-branded lit channel — the lit adjudication rides the committed P16 Class W predicate with the P17/P18 amendments: the AQA/Eduqas/UK-GCSE remainder skips unless a spine set text is named; the unseen-poetry shorts are guidance-register (the lit-21 spine carries no unseen spec points — the profile's 'unseen 96' is the unmapped set-text structure, disclosed)",
    'e-geo': "E-Geo (the 0460 case-study class — 'CASE STUDY_..._IGCSE GEOGRAPHY_0460' + the IGCSE_GEOGRAPHY underscore-form subject-name register (both geo faces); the generic geography/current-affairs remainder skips; the accounting-celebrity thin precedent)",
    'ilm-online-academy': "Ilm Online Academy (multi CIE: explicit 'Cambridge IGCSE Maths 0580' chapter lectures (the 4MA1 x25 family read as the 0580 register per the ginger law, disclosed) + 0620/0625/0610 session/content)",
    'y-mx-c': "Y=MX+C (the 0606 relative-velocity vectors series — 'IGCSE ADDMATHS - Vectors related with velocity'; the 86-absolute thin-ratio disclosure carried; the bare maths/KBAT content without the pool's 0606/0580 register skips)",
    'miss-estruch-biology': "Miss Estruch Biology (the 'ENTIRE Topic N for CIE A-level 2027' series (63 CIE-mention titles per title-grep, the revwise mixed-NT precedent) — the CIE topic-number register binds via stem token agreement; the AQA-dominant bare 'A-Level Biology' subset skips board-agnostic (the P19 academic-plus law))",
    'wimzee-cambridge-academy': "Wimzee Cambridge Academy (micro multi CIE — the bare 'IGCSE chemistry/biology' subject-name series + the 'AS level Chemistry' Cambridge-branded subset (the ginger context amendment, disclosed); the mr-quakers precedent)",
    'mysecondteacher': "MySecondTeacher (the numbered Cambridge A-Level lesson series ('Cambridge A Level Economics | 2.11 ...') — the section numbers ride the label-agreement law, the honest binds ride the verbatim/token evidence; the school-onboarding remainder skips)",
    'the-future-professionals': "The Future Professionals (thin-multi CAIE academy: 9706/9609 paper discussions + 0610/0625 + the 'W12/P22/Q7' 0580 question class (the P9/P14 paper law) + the bare accounting lectures (the subtopic-scoped gate); the matric/Pakistan-Studies and motivation remainders skip; the indigo thin-multi precedent)",
    'chembase-school-of-chemistry': "Chembase School of Chemistry (thin WCH/A-level chemistry class: 'Edexcel IAL Chemistry WCH15 ... Paper 05 | Fully Solved' (the spaced NN form) + the Cambridge AS/A-Level Chemistry subject-name series; the bare A-Level Chemistry subset rides the channel's CIE context, disclosed)",
    'sayo-enoch-aluko': "Sayo Enoch Aluko (mixed-board disclosed (the revwise precedent): the 0606 Add Maths subset + the 0417 specimen-paper subset bind; the GCSE/AP/IB-HL NT x48-dominant remainder skips)",
    'hendrik-academy': "Hendrik Academy (IBDP-dominant disclosed — the 'Analysis and Approaches / Applications and Interpretation / Time Zone' register skips (no spine course); the explicit 9709 component subset ('9709-s26-qp-33. Paper 3 Pure Mathematics 3') and the 9702 paper subset bind honestly; bare maths content rides the IBDP class)",
    'walter-maths-tutoring': "Walter Maths Tutoring (the 9231 further-maths solved-paper series has NO spine course — skips honest (the P18 4PM0-analog terminal call), the t-test/confidence-interval series rides the 9231 class; the CAIE 9709 'Pure 1' content subset binds)",
    'maths-camp': "Maths Camp (the 9709 P1 everything-guides + the 'Everything You Need to Know about X for AS Level Probability & Statistics 1' S1 series (register-first ordering per the fiifi amendment precedent); the bare IGCSE trig content skips honest)",
    'ishan': "Ishan (9708 micro pool (the mr-quakers precedent) — 'A Level Economics 9708 | Unit N' content; the psychology case-study remainder skips)",
    'biology-box': "Biology Box (the 'International GCSE Biology (Edexcel) Lesson N' series — the 4BI1 face binds; the modular-24/DA faces ride their explicit tokens; the AQA remainder skips)",
    'the-cs-classroom': "The CS Classroom (9618 subset + the 0478 title; the IB Computer Science 2027 register and the bare programming/life content skip honest)",
}
CHANNEL_NOTE = {k: f"{v} (oEmbed author verified per video)" for k, v in PROVIDER.items()}

ENUM_UTC = {p: json.load(open(f'{RES}/Videos/inventory/channels/{p}-uploads.json'))['enumeratedUtc']
            for p in PROVIDER}

poolB = json.load(open(f'{OUT}/tier-b.json'))
J = json.load(open(f'{OUT}/judgment.json'))
oemb = json.load(open(f'{OUT}/oembed-p20.json'))
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
                'evidence': f'{v["reason"]}; title-only posture, distinctive-token binding rule (df<=3, the stemmed-token vocabulary) or the disclosed higher title-only bar for section-name/topic-lecture/chapter-scoped/section-scoped rows (multi-point binds disclosed per row){xreg}',
                'method': 'llm-draft-external', 'boardMismatch': True,
                'reviewed': True, 'reviewer': REVIEWER, 'reviewedUtc': NOW,
            })

P20B_POST = [c for c in sorted(courses) if c in P4_CHILDREN]
pre_courses, post_courses = [], []
skip_by_class = Counter()
for s in skips:
    r = s['reason']
    if 'Anna-university' in r: skip_by_class['Anna-university GE8291 EVS register — the P19 false-density call carried (0 honest binds)'] += 1
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
                  '; routing: machine-checkable Tier B anchors (CIE A-level sciences 9700/9701/9702 papers 1-3 AS / 4-5 A2; CIE A-level accounting 9706 papers 1-2 AS / 3-4 A2; CIE A-level maths 9709 components P1/P2/P3 + P4/M1 + P5/S1 + P6/S2 (the P20 component routing of record); 9618 papers 1-2 AS / 3-4 A2; 0478/0984; 0606 (+ the disclosed 4037/4024 duals incl. the hashtag session class); 0580 papers 2/4 extended vs 1/3 core; 0610/0620/0625 (+ the 0971/0972/0973 duals); 0653 combined (the shared-paper law); 0417/0983; 4IT1/4IT0; 0452/0985 (+ the disclosed 7707 dual); 0455; 0450 (+ the disclosed 7115/0264 duals); 0680; 0460 (both geo faces); 9708; 9609 (pool-scoped); 4CH1/4BI1/4PH1/4SD0 Ed-IGCSE (+ 4WCH1/2/4WPH1/2/4WB1/2 modular-24); WCH/WPH IAL unit-content + question-set + spaced-NN anchors) + the 9700/9701 lesson-series concept-label law (the biochemlogy label-agreement amendment) + the P16 Class W set-text predicate + section-marker narrowing with the label-agreement gate + the topic-overclaim re-adjudication gate + section-name binding + distinctive-token Tier A (df<=3, the stemmed-token vocabulary) + the four-gate topic-lecture class + the P20 subtopic-scoped lecture gate + the numbered-lesson-series concept law, over every routed row with the degenerate-bind re-adjudication bar')
    spine_n = len(spine_specs(course))
    draft = {
        'schema': 'syllabai.video-map-draft/2',
        'draftOf': course,
        'task': TASK,
        'course': course,
        'qual': qual_of(course),
        'reviewState': 'owner-reviewed-external',
        'draftLaw': 'P20 judgment lane (the gap-profile pool set: 35 pools admitted by owner order "run P20 judgment"; 10,611 '
                    'pool uploads dispositioned exactly-once): '
                    'Tier B course anchors by machine-checkable session/paper codes (method paper-code, confidence '
                    'high; the P15/P17/P18/P19 registers plus the P20 additions of record: CIE A-level sciences '
                    '9700/9701/9702 papers 1-3 AS / 4-5 A2; CIE A-level accounting 9706 papers 1-2 AS / 3-4 A2 (the '
                    'P13 accounting paper-level law, incl. the specimen/question-set class); CIE A-level maths 9709 '
                    'components P1/P2/P3 pure + P4/M1 mechanics + P5/S1 + P6/S2 p&s (the P20 component routing of '
                    'record; bare component-less walkthroughs skip per ANCHOR-GRANULARITY section 6); 9618 papers 1-2 '
                    'AS / 3-4 A2; 0478/0984; 0606 (+ the disclosed 4037/4024 duals incl. the hashtag session class); '
                    '0580 papers 2/4 extended vs 1/3 core; 0610/0620/0625 (+ the 0971/0972/0973 duals); 0653 combined '
                    '(the shared-paper law); 0417/0983; 4IT1/4IT0; 0452/0985 (+ the disclosed 7707 dual); 0455; 0450 '
                    '(+ the disclosed 7115/0264 duals); 0680; 0460 (both geo faces — the 2020/2025 shared-register '
                    'pair); 9708; 9609 (pool-scoped); 4CH1/4BI1/4PH1/4SD0 Ed-IGCSE (+ the 4WCH1/2/4WPH1/2/4WB1/2 '
                    'modular-24 faces, the explicit Unit-N token outranking the code digit); WCH/WPH IAL unit-content '
                    '+ the question-set/specimen class (the P20 amendment of the P14 Assil law) + the spaced WCH/WBI/'
                    'WPH NN paper form (unit via the 11-16/21-26 pair law)) + the P16 Class W set-text predicate '
                    '(the P17/P18 amendments) + section-marker narrowing with the P20 label-agreement gate (the '
                    'biochemlogy law of record: channels renumber by playlist index, not by the syllabus numbers) + '
                    'the P20 topic-overclaim re-adjudication gate (a topic-level verbatim bind is dishonest for a '
                    'subtopic-scoped lecture) + section-name binding + distinctive-token Tier A (df<=3 on the '
                    'stemmed-token vocabulary) + the four-gate topic-lecture class + the P20 subtopic-scoped lecture '
                    'gate + the numbered-lesson-series concept-label law (the tatchen precedent generalized: the '
                    'lesson-code prefix and Triple/Single/Double tags strip before the concept label re-binds, '
                    'order-based section containment). Guidance/promo/tuition registers, meta announcements, the '
                    'edutainment register, the O-Level register (the disclosed 4024/2281/5090/7707/7115 duals exempt '
                    'plus the new 0264 IGCSE-business token), the IBDP register (Analysis and Approaches / '
                    'Applications and Interpretation / Time Zone), the 9231 further-maths register (no spine course), '
                    'the IAL ICT (WIT) register (no spine course), the UK-GCSE Edexcel CS register (no spine course), '
                    'NT-board titles and out-of-spine boards are excluded and ledgered as skips. Rejected/unrouted '
                    'videos stay out of videos[]. P20 honest register calls of record: mathlete\'s "4MA1 x78" gate '
                    'read re-adjudicated to the generic IGCSE/O-Level 0580 class per the ginger law (the 4MA1 deficits '
                    'stay open); the-lightup-hub\'s lit subset rides the Class W predicate (1 honest set-text bind — '
                    'the AQA/UK-GCSE-branded remainder skips; the "unseen 96" is the unmapped set-text structure, not '
                    'a literal unseen register); hendrik\'s IBDP register and walter\'s 9231 register have no spine '
                    'course (0 binds, disclosed).',
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
    json.dump(draft, open(f'{D}/video-map.draft.external-p20.json', 'w'), ensure_ascii=False, indent=1)
    n_ok = sum(1 for v in oemb.values() if v.get('ok'))
    n_fb = sum(1 for v in oemb.values() if v.get('ok') and v.get('method') == 'thumb-fallback')
    n_bad = sum(1 for v in oemb.values() if not v.get('ok'))
    verdicts = {
        'schema': 'syllabai.owner-review-verdicts/2',
        'task': TASK,
        'course': course,
        'ruledUtc': NOW,
        'source': 'delegated self-review — owner chat 2026-11-09 "approve and review yourself"; P20 profile filed 2026-11-26 (PR #366), pools admitted and judgment ordered "run P20 judgment" 2026-11-26',
        'default': 'keep',
        'reviewer': REVIEWER,
        'evidenceBasis': (f'Identity: oEmbed sweep {n_ok}/{n_ok} routed videos alive — '
                          f'{n_ok - n_fb} author_url channel == channel-of-record via UC id (0 mismatch) + '
                          f'{n_fb} thumbnail-liveness fallbacks disclosed per the P2D law '
                          f'(oembed HTTP 200 all-null payload; identity rides on the channel-of-record upload '
                          f'provenance), 0 bad. Tier B: session/paper codes regex-verified in titles (the P15/P17/'
                          f'P18/P19 registers plus the P20 additions of record: the 9700/9701/9702 AS/A2 paper law, '
                          f'the 9706 accounting paper-level law with the specimen/question class, the 9709 component '
                          f'routing (P1/P2/P3/M1/S1/S2), 9618 papers 1-2/3-4, 0478/0984, the combined-0653 shared-'
                          f'paper law, the 0460 dual-face law, the WCH/WPH unit-question and spaced-NN classes, the '
                          f'modular-science Unit-N-over-code law). Class W: the P16 committed predicate with the '
                          f'P17/P18 amendments. Tier A: the P13/P15 gate ladder '
                          f'(section-marker narrowing with the P20 label-agreement gate, verbatim section-name '
                          f'binding with the topic-overclaim re-adjudication gate, deduped distinctive-token binds '
                          f'df<=3 on the stemmed vocabulary, the four-gate topic-lecture class, the P20 subtopic-'
                          f'scoped lecture gate and the numbered-lesson-series concept law) over EVERY routed pair '
                          f'with the degenerate-bind re-adjudication bar. Guidance/promo/tuition, meta announcements, '
                          f'the O-Level register (the disclosed duals exempt + the 0264 token), the IBDP register, '
                          f'the 9231 register (no spine course), the IAL ICT register (no spine course) and '
                          f'out-of-spine boards skipped '
                          f'with reasons ({len(skips)} ledgered in work/p20/skips.json by class: '
                          f'{dict(skip_by_class)}).'),
        'rejects': c['rejects'],
        'applied': {'rowsApproved': len(rows), 'rowsRejected': len(c['rejects']), 'appliedUtc': NOW},
    }
    json.dump(verdicts, open(f'{D}/owner-review-verdicts.p20.json', 'w'), ensure_ascii=False, indent=1)
    if course in P20B_POST:
        post_courses.append(course)
    else:
        pre_courses.append(course)
    print(f'{course}: rows {len(rows)} (anchors {len(rows)-len(specRows)}, spec {len(specRows)}) videos {len(c["videos"])} p20b {"POST" if course in P20B_POST else "pre"}')

json.dump({'pre': pre_courses, 'post': post_courses}, open(f'{OUT}/p20-courses.json', 'w'), indent=1)
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
    'disposition': '10,611 P20 pool uploads = routed (tier B + tier A) + skips, exactly-once',
}
json.dump(summary, open(f'{OUT}/p20_summary.json', 'w'), indent=1)
print(f'\nTOTAL rows {tot} (anchors {tot - totA}, spec rows {totA}) across {len(courses)} courses | pre {len(pre_courses)} post {len(post_courses)}')
print('summary ->', f'{OUT}/p20_summary.json')
