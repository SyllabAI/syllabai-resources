#!/usr/bin/env python3
"""P11 step 3: agent judgment pass over EVERY Tier A (course, video) pair.

Class model (P10 shape, generalized):
  - Explicit-code class tables (fp1 = the P10 FP1 table; d1 = the IAL D1
    chapter series; eng_cie = 0500 skill specs; eng_p1 = 4EA1 paper-1
    sections). A table bind draws the spec from the pre-pass scored candidate
    list (the pre-pass proposed it — the rule only discriminates between topic
    siblings; it never invents a bind); direct rules validate the code in the
    spine and bind at low confidence (disclosed higher title-only bar).
  - CIE chapter-marker rows: leading "N.M" section markers (csm/yi/evm/…
    chapter series) narrow the candidate pool to specs whose code starts with
    the section; the top pool candidate binds (medium when distinctive, low
    otherwise — the disclosed P4 cross-subject-style higher title-only bar).
    fp1 is excluded from narrowing (UK CP1 section numbers ≠ IAL FP1 codes).
  - moduleNamed rows ("The whole of X"): class table / distinctive candidates
    only — no all-candidate fallback (a whole-module summary must not bind to
    one arbitrary spec).
  - Non-structured rows: distinctive candidates only (df<=3, the tightened bar).
Every (course, video) gets an explicit decision: keep / drop / unmapped."""
import json, re, collections

HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p11'

SPEC_CACHE = {}
def specs_of(course):
    if course in SPEC_CACHE:
        return SPEC_CACHE[course]
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    sp = {n['code']: n['title'] for n in cur['nodes'] if n['family'] == 'SPEC_POINT'}
    SPEC_CACHE[course] = sp
    return sp

def spine_n(course):
    return len(specs_of(course))

tierA = json.load(open(f'{OUT}/tier-a.json'))
by_course = collections.defaultdict(list)
for p in tierA:
    for c in p['courses']:
        by_course[c].append({**p, '_course': c})

# ---- explicit-code class tables ----
RULES = {
 'ial-maths-20-decision-1': [
    (r'bin[- ]?packing|bubble sort|quick sort|binary search', '1.2'),
    (r'general ideas of algorithms|flow ?chart', '1.1'),
    (r'algorithms? 1\b', '1.1', 'direct'),
    (r'algorithms? on graphs?', '2.1', 'direct'),
    (r'dijkstra|shortest path', '2.2'),
    (r'minimum spanning tree|spanning tree|prim|kruskal|graphs? and networks|networks', '2.1'),
    (r'route inspection', '3.1'),
    (r'travelling salesman|salesman', '3.2'),
    (r'upper and lower bounds|lower bounds?|upper bounds?', '3.3'),
    (r'nearest neighbour', '3.4'),
    (r'activity network|precedence', '4.1'),
    (r'critical path', '4.3'),
    (r'gantt|cascade|scheduling|float', '4.4'),
    (r'linear programming|simplex|graphical solution', '5.1'),
    (r'algorithm', '1.1'),
    (r'exam tips|exam questions|exam paper', None),
 ],
 'ial-further-maths-18-further-pure-1': [
    (r'induction', '8.1'),
    (r'summation|sums of (squares|natural)|series|sigma', '7.1'),
    (r'linear transformation|matrix representation|reflection|rotation|enlargement|stretch|transformation', '6.1'),
    (r'combination of transformations|successive', '6.3'),
    (r'inverse (of a )?transformation', '6.4'),
    (r'inverse (of a )?matrix|\(ab\)', '5.5'),
    (r'determinant|singular', '5.4'),
    (r'product.{0,20}matric|matrix (multiplication|product)', '5.3'),
    (r'scalar.{0,20}matrix|multiplication.{0,20}scalar', '5.2'),
    (r'addition.{0,20}matric|subtract.{0,20}matric|matrices', '5.1'),
    (r'focus|directrix|parabola', '4.3'),
    (r'tangents? and normals?', '4.4'),
    (r'parametric equation|rectangular hyperbola', '4.2'),
    (r'cartesian equation|hyperbola', '4.1'),
    (r'numerical|bisection|iteration|interval|linear interpolation', '3.1'),
    (r'sum of roots|product of roots|new roots|forming quadratics?', '2.1'),
    (r'roots of quadratics?|complex roots|conjugate', '1.5'),
    (r'complex solutions|quadratic equations', '1.4'),
    (r'argand|geometrical representation', '1.3'),
    (r'sum.{0,15}product.{0,15}quotient|complex (number|arithmetic)', '1.2'),
    (r'complex|imaginary', '1.1'),
    (r'modulus and argument', '1.1', 'direct'),
    (r'solving cubic and quartic', '1.6', 'direct'),
    (r'roots? of a quadratic', '2.1', 'direct'),
    (r'locating roots|newton.?raphson', '3.1', 'direct'),
    (r'invert(ing)? a 2x2 matrix|inverse of 2 ?x ?2', '5.5', 'direct'),
    (r'proving (statements|divisibility)|recurrence relation', '8.1', 'direct'),
 ],
 'cie-igcse-english-language-20': [
    (r'summary|summaris', 'S2.008', 'direct'),
    (r'directed writing|select.{0,20}information|facts, ideas and opinions', 'S2.009', 'direct'),
    (r'writers? achieve|effects?|linguistic device|figurative|imagery|question 2|marking|marked', 'S2.010', 'direct'),
    (r'reading paper|comprehension|understand|respond|question 1', 'S2.007', 'direct'),
    (r'paper 3|coursework|narrative|descriptive|describe', 'S3.001', 'direct'),
    (r'essay|report|article|review|email|persuade', 'S3.002', 'direct'),
    (r'audience|purpose|form', 'S3.005', 'direct'),
    (r'vocabulary', 'S3.003', 'direct'),
    (r'spelling|punctuation|grammar', 'S3.006', 'direct'),
 ],
 'igcse-english-language-a-16-paper-1-non-fiction-texts-and-transactional-writing': [
    (r'question (4|5|6)|q(4|5|6)|section ?b|transactional', 'IGCSE_ENGLISH_LANGUAGE_A:C1AB', 'direct'),
    (r'question (1|2|3)|q(1|2|3)|section ?a|non-fiction', 'IGCSE_ENGLISH_LANGUAGE_A:C1AA', 'direct'),
    (r'transactional', 'IGCSE_ENGLISH_LANGUAGE_A:C1AB', 'direct'),
    (r'reading|evaluate|analysis', 'IGCSE_ENGLISH_LANGUAGE_A:C1AA', 'direct'),
 ],
}
RULES['cie-igcse-english-language-25'] = RULES['cie-igcse-english-language-20']

# ---- explicit re-adjudications (the P10 rebind/drop law) ----
REBINDS = [
    ('1.1 Hardware and Software', 'cie-igcse-ict-21', ['1.1.1'], 'low',
     "narrowing tie (1.1.1/1.1.2/1.1.3 scored identically on the section pool) resolved to 1.1.1 'Hardware' — the title names hardware first; low confidence"),
]
DROPS = {
    ('cie-as-computer-science-19', 'Declarative Programming Prolog'): "degenerate vocabulary bind ('coding') — AS spine has no declarative-paradigm spec; honest drop",
    ('cie-as-computer-science-19', 'Object-Oriented Programming'): "degenerate vocabulary bind ('coding') — OOP is an A2 paradigm; AS spec 12.1.4 is the program-development cycle; honest drop",
    ('cie-as-computer-science-19', 'File Processing'): "degenerate vocabulary bind ('coding') — honest drop",
    ('cie-as-computer-science-19', 'Algorithm (Code'): "generic-token bind ('algorithm','diagram') — state-transition-diagram spec not named by the title; honest drop",
    ('cie-as-computer-science-19', 'Ethical Issues'): "single-token bind ('issue') onto a DBMS spec — ethics specs live in section 7 but the title carries no distinctive token; honest drop",
    ('cie-as-computer-science-19', 'Core Concepts of Processor'): "single-token bind ('functionality') onto an amend-a-program spec; honest drop",
    ('cie-as-computer-science-19', 'Computer Architecture'): "vocabulary-adjacent bind ('machine','processor') onto the assembly/machine-code spec; honest drop",
    ('cie-a-level-computer-science-19', 'Recursion'): "degenerate bind onto a compiler/translation spec — the A2 recursion spec does not carry the token; honest drop",
    ('cie-a-level-computer-science-19', 'Algorithm (Code'): "generic-token bind ('algorithm','diagram') onto a state-transition-diagram spec; honest drop",
    ('cie-a-level-computer-science-19', 'Digital Logic'): "single-token bind ('digital') onto a digital-certification spec; honest drop",
    ('cie-a-level-computer-science-19', 'Ethical Issues'): "single-token bind ('issue') onto a DBMS spec — ethics specs carry no distinctive token in the title; honest drop",
    ('cie-a-level-computer-science-19', 'Core Concepts of Processor'): "degenerate bind ('protocol') onto a protocol-implementation spec; honest drop",
    ('cie-igcse-history-18', 'Russia and USSR Depth Study Overview'): "degenerate bind ('russia' df3) onto a WW1 Eastern-Front spec — the USSR depth study has no matching spec in this 19th-century-core spine; honest drop",
    ('cie-igcse-history-18', 'Paper 4. Behind the Scenes'): "degenerate bind ('behind') onto an imperialism spec; teacher-resource video, honest drop",
    ('cie-igcse-history-18', 'Why do Debate'): "degenerate bind ('debate') onto a US-imperialism-debate spec; teacher-resource video, honest drop",
    ('cie-igcse-history-18', "Learner's Guide"): "degenerate bind ('have') onto a 1929-crash spec; teacher-resource video, honest drop",
    ('cie-igcse-history-18', 'Time Managements'): "degenerate bind ('time') onto a Versailles-justification spec; exam-technique video, honest drop",
    ('cie-igcse-history-18', 'Big Changes for the Final'): "degenerate bind ('big') onto the Big Three at Versailles spec; exam-technique video, honest drop",
    ('cie-igcse-history-18', 'Message Questions'): "degenerate bind ('get') onto a victors-aims spec; exam-technique video, honest drop",
    ('cie-igcse-history-18', 'Part C. The Big Question'): "degenerate bind ('big') onto the Big Three at Versailles spec; exam-technique video, honest drop",
    ('igcse-ict-17', 'Database Questions'): "bind onto a mail-merge output spec ('database','relationship' tokens) — the Edexcel DB specs are not distinctive to this title; honest drop",
    ('igcse-ict-17', 'Computer Controlled Systems'): "degenerate bind ('computer','system') onto a communication-software spec; honest drop",
    ('igcse-ict-17', 'Microprocessor controlled devices'): "degenerate bind ('device','microprocessor') onto a mainframe spec; honest drop",
    ('igcse-ict-17', 'Networks: Networks and the effects'): "single-token bind ('effect') onto a create-slides spec; honest drop",
    ('igcse-ict-17', 'Emerging Technologies'): "degenerate bind ('component','system') onto wired/wireless components spec; honest drop",
    ('igcse-ict-17', 'Types of Computers'): "degenerate bind ('component','system') onto wired/wireless components spec; honest drop",
    ('igcse-ict-17', 'Operating Systems'): "degenerate bind ('component','system') onto wired/wireless components spec; honest drop",
    ('igcse-ict-17', 'The Main Component'): "degenerate bind ('component','system') onto wired/wireless components spec; honest drop",
    ('igcse-ict-17', 'Input Devices and Their Uses'): "'output' token from the series suffix bound the input-devices video to an output-peripherals spec; honest drop",
    ('igcse-ict-17', '1.1 Hardware and Software'): "degenerate bind ('hardware'/'software') onto a mainframe-processing spec; honest drop",
    ('igcse-business-19', 'Business Activity (1.1)'): "degenerate bind ('business','activity') onto a government-influence spec; honest drop",
    ('igcse-business-19', 'Business Activities: 0450'): "degenerate bind onto the factors-of-production relationships spec; honest drop",
    ('igcse-business-19', 'Business and Stakeholder Objectives'): "degenerate bind onto a size-characteristics spec; honest drop",
    ('igcse-business-19', 'Economic Issues (6.1)'): "degenerate bind onto the functional-areas spec; honest drop",
    ('igcse-business-19', 'Environmental and Ethical Issues'): "degenerate bind onto the functional-areas spec; honest drop",
    ('igcse-business-19', 'Organisation and Management'): "degenerate bind onto a quality-concept spec; honest drop",
    ('igcse-business-19', 'Enterprise, Business Growth, Size'): "degenerate bind onto a forms-of-organisation spec; honest drop",
}

# course-level overrides: every keep re-adjudicated to honest unmapped
DROP_ALL = {
    'igcse-history-17': "cross-board 0470 content produced systematic degenerate binds (single-token 'behind'/'debate'/'big'/'time'/'russia' matches onto Edexcel topic specs) — re-adjudicated course-level to honest unmapped; igcse-history-17 stays honest-empty",
    'cie-igcse-history-18': "the channel's 0470 content follows the 20th-century syllabus while this spine is the 19th-century-European core, and every pre-pass keep was a single-token degenerate bind — re-adjudicated course-level to honest unmapped; cie-igcse-history-18 stays honest-empty",
    'igcse-economics-17': "cross-board 0455 chapter series produced mixed degenerate binds (skills videos onto content specs); the two defensible macro-aims binds ride the disclosed higher bar — re-adjudicated course-level to honest unmapped; igcse-economics-17 stays honest-empty",
}

SECTION_MARK = re.compile(r'(?:^|:\s+|Chapter\s+|\bCP\d+-\d+:\s+)(\d{1,2}\.\d)(?!\.\d)(?:\s|$|:| )')

def section_of(title):
    m = SECTION_MARK.search(title)
    return m.group(1) if m else None

CHAPTER_MARK = re.compile(r'\bChapter\s+(\d{1,2})(?!\.\d)(?:\b|:)')
CHAPTER_PROVIDERS = {'igcse-online'}  # chapter numbers verified syllabus-structured (0455 ch1-6, 0620 ch1-7)

def chapter_of(title):
    m = CHAPTER_MARK.search(title)
    return m.group(1) if m else None

def verdict_for(course, v, cl):
    """cl = ALL pre-pass candidates (any score) for this (course, video)."""
    title = v['title']
    # spine hygiene: teacher-guidance/administrative specs must never absorb binds
    cl = [x for x in cl if 'teacher guidance' not in x['title'].lower()]
    d = [x for x in cl if x['distinctive']]
    sec = section_of(title)
    structured = (sec is not None and course != 'ial-further-maths-18-further-pure-1') or bool(v.get('marker'))
    # 1. class table
    for rule in RULES.get(course, []):
        pat, code = rule[0], rule[1]
        direct = len(rule) > 2 and rule[2] == 'direct'
        if not re.search(pat, title, re.I):
            continue
        if direct:
            if code not in specs_of(course):
                continue
            ev = (f"title names the {code} skill/section unambiguously and spec {code} '{specs_of(course)[code][:48]}' is validated "
                  f"in the spine; direct class-table bind at the disclosed higher title-only bar, confidence low")
            return {'action': 'keep', 'specs': [code], 'confidence': 'low', 'reason': ev}
        pool = cl if structured else d
        if not pool:
            continue
        chosen = next((x for x in pool if x['code'] == code), None) if code else pool[0]
        if chosen is None:
            continue
        dist = chosen['minDf'] <= 3
        conf = 'medium' if dist else 'low'
        ev = (f"title names {chosen['code']} '{chosen['title'][:56]}' via token(s) {chosen['matched'][:4]}"
              f" (df {chosen['minDf']})")
        if not dist:
            ev += (f"; token df above the tightened bar within a {spine_n(course)}-spec spine — bound at the "
                   f"disclosed P4 cross-subject-style higher title-only bar, confidence low")
        return {'action': 'keep', 'specs': [chosen['code']], 'confidence': conf, 'reason': ev}
    # 2. chapter.section narrowing (CIE chapter series with N.M markers)
    if sec is not None and course != 'ial-further-maths-18-further-pure-1':
        pool = [x for x in cl if x['code'].startswith(sec + '.')]
        if pool:
            chosen = pool[0]
            dist = chosen['minDf'] <= 3
            conf = 'medium' if dist else 'low'
            ev = (f"chapter.section marker ({sec}) narrows the candidate pool to section specs; "
                  f"title binds {chosen['code']} '{chosen['title'][:56]}' via token(s) {chosen['matched'][:4]}"
                  f" (df {chosen['minDf']})")
            if not dist:
                ev += (f"; token df above the tightened bar — bound at the disclosed higher title-only bar, "
                       f"confidence low")
            return {'action': 'keep', 'specs': [chosen['code']], 'confidence': conf, 'reason': ev}
    # 2b. chapter-N narrowing (single-number Chapter series, verified syllabus-structured)
    ch = chapter_of(title)
    if ch and v.get('provider') in CHAPTER_PROVIDERS and not sec:
        pool = [x for x in cl if x['code'].startswith(ch + '.')]
        if pool:
            chosen = pool[0]
            dist = chosen['minDf'] <= 3
            conf = 'medium' if dist else 'low'
            ev = (f"Chapter {ch} marker of a syllabus-structured series narrows the pool to section {ch} specs; "
                  f"title binds {chosen['code']} '{chosen['title'][:56]}' via token(s) {chosen['matched'][:4]}"
                  f" (df {chosen['minDf']})")
            if not dist:
                ev += "; bound at the disclosed higher title-only bar, confidence low"
            return {'action': 'keep', 'specs': [chosen['code']], 'confidence': conf, 'reason': ev}
    # 3. distinctive top (non-structured or no section pool)
    if d:
        chosen = d[0]
        ev = (f"title names {chosen['code']} '{chosen['title'][:56]}' via token(s) {chosen['matched'][:4]}"
              f" (df {chosen['minDf']})")
        return {'action': 'keep', 'specs': [chosen['code']], 'confidence': 'medium', 'reason': ev}
    if cl:
        return {'action': 'unmapped',
                'reason': f"topic tokens ({cl[0]['matched'][:4]}) overlap the spine only above the tightened bar — routed-but-unmapped, honest"}
    return {'action': 'unmapped',
            'reason': 'zero token overlap with the spine in the pre-pass — routed-but-unmapped, honest'}

verdicts = {}
stats = collections.Counter()
for course, vids in sorted(by_course.items()):
    cands = json.load(open(f'{OUT}/candidates-{course}.json'))
    out = []
    for v in vids:
        cl = cands.get(v['id'], [])
        dec = verdict_for(course, v, cl)
        if course in DROP_ALL and dec['action'] == 'keep':
            dec = {'action': 'unmapped', 'reason': f"keep re-adjudicated course-level: {DROP_ALL[course]}"}
        rb = next((r for r in REBINDS if r[0] in v['title']), None)
        if rb and rb[1] == course:
            _, tgt, specs, conf, note = rb
            ok = all(s in specs_of(tgt) for s in specs)
            dec = ({'action': 'keep', 'specs': specs, 'confidence': conf, 'reason': note}
                   if ok else {'action': 'unmapped', 'reason': note + ' — target spec missing'})
        dk = next(((cc, frag) for (cc, frag), why in DROPS.items() if cc == course and frag in v['title']), None)
        if dk is not None:
            dec = {'action': 'unmapped', 'reason': 'drop on review: ' + DROPS[dk]}
        dec['id'] = v['id']
        dec['title'] = v['title']
        out.append(dec)
        stats[dec['action']] += 1
    verdicts[course] = out

json.dump(verdicts, open(f'{OUT}/judgment.json', 'w'), indent=1)
print(dict(stats.most_common()))
tot_rows = 0
for c, vs in verdicts.items():
    k = sum(1 for v in vs if v['action'] == 'keep')
    med = sum(1 for v in vs if v['action'] == 'keep' and v.get('confidence') == 'medium')
    lo = sum(1 for v in vs if v['action'] == 'keep' and v.get('confidence') == 'low')
    dr = sum(1 for v in vs if v['action'] == 'drop')
    u = sum(1 for v in vs if v['action'] == 'unmapped')
    tot_rows += k
    if vs:
        print(f'{c}: keep {k} (med {med}/low {lo}) unmapped {u}')
print('TOTAL kept rows', tot_rows)
