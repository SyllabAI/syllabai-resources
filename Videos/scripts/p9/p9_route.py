#!/usr/bin/env python3
"""P9 step 1: deterministic router — Mr Hassaan's Maths Channel pool -> lanes.

Two tiers per docs/ANCHOR-GRANULARITY.md:
  TIER B (course anchors, method paper-code, high, boardMismatch false):
    titles carrying machine-checkable paper codes — IAL W-codes (WMA11-14 ->
    ial-maths-20-pure-1..4, WME01 -> mechanics-1, WST01 -> stats-1; old-register
    WMA01 C12 -> pure-1+pure-2, WMA02 C34 -> pure-3+pure-4), CIE 9709 codes and
    textual "Paper NN" forms (P1,P2 -> a-level+as pure; P3 -> a-level pure-3;
    P4 -> cie mechanics pair; P5 -> p&s-1 pair; P6 -> a-level p&s-2), CIE 0580
    codes (papers 1,3 -> 25-core via P9B; 2,4 -> 25-extended), Edexcel 4MA1
    (H -> igcse-maths-a-18-higher; F -> foundation via P9B).
  TIER A (spec rows, llm-draft-external, medium/low, boardMismatch true):
    uncoded titles routed by explicit unit markers (IAL P1-P4/M1/S1/D1/FP1,
    Solomon papers, textbook chapters) or idf best-of for the remainder;
    candidates generated in step 2.
  SKIPS (honest, counted):
    GCE-qualified paper content (9MA0/8MA0, 666x-669x, 'GCE' session walkthroughs —
    per ANCHOR-GRANULARITY §6 a GCE paper is evidence about the GCE qualification,
    no such course in the spine), CIE O-Level 4037, non-maths / no-vocabulary.
Every video in the 3,150 pool is dispositioned exactly once.
"""
import json, os, re, collections

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p9'
os.makedirs(OUT, exist_ok=True)

ups = json.load(open(f'{RES}/Videos/inventory/channels/mrhassansmaths-uploads.json'))

# corpus exclusion: any pool video already declared in the shipped union
corpus = set()
vmd = f'{HUB}/content/video-map'
for f in os.listdir(vmd):
    if f.endswith('.json'):
        for v in json.load(open(f'{vmd}/{f}')).get('videos', []):
            corpus.add(v['id'])

IAL_CODE = re.compile(r'\b(WMA1[1-4]|WME0[1-2]|WST0[1-2]|WFD0[1-2]|WFM0[1-3]|WFM1[1-3]|WFP0[1-3]|WMA0[12])\s*/?')
CIE_CODE = re.compile(r'\b9709\s*/\s*(\d{2})')
CIE_SESS = re.compile(r'\b9709\s*/\s*[MFONJS]{1,2}\s*/\s*[MFONJS]{1,2}\s*/\s*(\d{2})\s*/', re.I)
CIE_TEXT = re.compile(r'9709[^.]{0,40}?\bPaper\s*(\d{1,2})\b', re.I)
CIE_BARE = re.compile(r'9709\s+(\d{2})\b')
CIE_PM = re.compile(r'\(P([1-6])\s*CAIE\)|CAIE.{0,30}?[-\s]*\(?\s*P([1-6])\s*\)?|CAIE\s+P([1-6])\b|\bM([1-3])\s*\(CAIE\)|\bS([1-3])\s*\(CAIE\)', re.I)
IG_CODE = re.compile(r'\b0580\s*/\s*(\d{2})')
IG_SESS = re.compile(r'\b0580\s*/\s*[MFONJS]{1,2}\s*/\s*[MFONJS]{1,2}\s*/\s*(\d{2})\s*/', re.I)
IG_TEXT = re.compile(r'0580[^.]{0,40}?\bPaper\s*(\d{1,2})\b', re.I)
IG_BARE = re.compile(r'\b0580\s+(\d{2})\b')
C12 = re.compile(r'\bC12\b')
C34 = re.compile(r'\bC34\b')
MA_CODE = re.compile(r'\b4MA1\s*/\s*([1-4])\s*([HF])\b', re.I)
MB_CODE = re.compile(r'\b4MB[012]\b', re.I)
PM_CODE = re.compile(r'\b4PM[01]\b', re.I)
XM_CODE = re.compile(r'\b4XMA\b', re.I)
CIE_SPEC = re.compile(r'\b9709\s*/\s*[A-Z]{1,2}\s*/\s*(\d{2})\b', re.I)
GCE_CODE = re.compile(r'\b(9MA0|8MA0|666[3-9]|667[6-9]|668[3-9]|669[0-1])\s*/?', re.I)
OTHER_BOARD = re.compile(r'\b(OCR|AQA|MM1[AB]|MEI|WJEC|4728|MS1[AB]|SS1[AB]|MM|S1B|M1B)\b', re.I)
GCE_LABEL = re.compile(r'\bGCE\b', re.I)
C_UNIT = re.compile(r'\bC[1-4]\b')
SESSION = re.compile(r'JAN|JUNE|JUN\b|OCT|NOV|MAY|SPECIMEN|SAMPLE|MOCK|20\d\d', re.I)
OL_CODE = re.compile(r'\b4037\s*/?', re.I)

M_P = re.compile(r'\bP([1-4])\b')
M_M = re.compile(r'\bM1\b')
M_S = re.compile(r'\bS1\b')
M_D = re.compile(r'\bD1\b')
M_FP = re.compile(r'\bFP1\b')

P2C = {  # IAL unit code -> ial course(s)
    'WMA11': ['ial-maths-20-pure-1'], 'WMA12': ['ial-maths-20-pure-2'],
    'WMA13': ['ial-maths-20-pure-3'], 'WMA14': ['ial-maths-20-pure-4'],
    'WME01': ['ial-maths-20-mechanics-1'], 'WME02': ['ial-maths-20-mechanics-2'],
    'WST01': ['ial-maths-20-statistics-1'], 'WST02': ['ial-maths-20-statistics-2'],
    'WFD01': ['ial-maths-20-decision-1'],
    'WMA01': ['ial-maths-20-pure-1', 'ial-maths-20-pure-2'],   # old C12 spans P1+P2
    'WMA02': ['ial-maths-20-pure-3', 'ial-maths-20-pure-4'],   # old C34 spans P3+P4
}
CIE_P = {  # 9709 paper digit -> cie course(s)  (P4 precedent: same rows in the a-level/as pair)
    '1': ['cie-a-level-maths-20-pure-1', 'cie-as-maths-20-pure-1'],
    '2': ['cie-a-level-maths-20-pure-2', 'cie-as-maths-20-pure-2'],
    '3': ['cie-a-level-maths-20-pure-3'],
    '4': ['cie-a-level-maths-20-mechanics', 'cie-as-maths-20-mechanics'],
    '5': ['cie-a-level-maths-20-probability-and-statistics-1', 'cie-as-maths-20-probability-and-statistics-1'],
    '6': ['cie-a-level-maths-20-probability-and-statistics-2'],
}
IG_MAP = {'1': 'cie-igcse-maths-25-core', '3': 'cie-igcse-maths-25-core',
          '2': 'cie-igcse-maths-25-extended', '4': 'cie-igcse-maths-25-extended'}

def cie_paper(code2):
    return code2[1] if code2[0] == '0' else code2[0]

def ig_paper(code2):
    return code2[1] if code2[0] == '0' else code2[0]

MATHW = re.compile(r'math|algebra|trigonom|geometr|calculus|differenti|integr|quadrat|vector|surds|'
    r'logarithm|binomial|factor|polynomial|inequal|coordinate|sequence|series|probabilit|statistic|'
    r'mechanic|kinemat|momentum|projectile|friction|pulley|matrix|complex number|argand|roots?|'
    r'indice|fraction|percent|ratio|circle|triangle|sine|cosine|tangent|curve|graph|equation|'
    r'proof|transform|function|asymptote|stationary|trapezium|arithmetic|geometric progress|'
    r'decision|algorithm|sort|critical path|histogram|normal distribution|correlation|'
    r'regression|discrete|continuous|limit|derivative|gradient|arc|sector|'
    r'volume|area|perimeter|mean|median|mode|variance|quantile|box ?plot|'
    r'permut|combinat|factorial|deviation|solomon|text book|textbook|tutorial', re.I)

poolB, poolA, skips = [], [], []
cclass = collections.Counter()

for v in ups['videos']:
    vid, t = v['id'], v['title']
    if vid in corpus:
        cclass['already in shipped union'] += 1
        continue
    # ---- GCE / O-Level: honest no-target (ANCHOR-GRANULARITY §6)
    if OL_CODE.search(t):
        skips.append({'id': vid, 'title': t, 'class': 'no-target (CIE O-Level 4037 — no such course in the spine)'})
        cclass['skip 4037'] += 1
        continue
    if GCE_CODE.search(t) or (GCE_LABEL.search(t) and re.search(r'Q\d|JAN|JUNE|OCT|NOV|MAY|SPECIMEN|SAMPLE|MOCK', t, re.I)) or (C_UNIT.search(t) and SESSION.search(t) and not re.search(r'C12|C34|Text Book|Textbook|Text Bk', t, re.I)):
        skips.append({'id': vid, 'title': t, 'class': 'no-target (Edexcel GCE/9MA0 qualification paper — no GCE course in the spine; ANCHOR-GRANULARITY §6)'})
        cclass['skip GCE'] += 1
        continue
    if OTHER_BOARD.search(t):
        skips.append({'id': vid, 'title': t, 'class': 'no-target (OCR/AQA/MEI/WJEC qualification paper — board not in the spine; ANCHOR-GRANULARITY §6)'})
        cclass['skip other-board'] += 1
        continue
    # ---- Tier B: machine-checkable paper codes
    if C12.search(t) and not IAL_CODE.search(t):
        code = 'WMA01'
    elif C34.search(t) and not IAL_CODE.search(t):
        code = 'WMA02'
    else:
        m = IAL_CODE.search(t)
        code = m.group(1) if m else None
    if code:
        courses = P2C.get(code)
        if courses:
            poolB.append({'id': vid, 'title': t, 'duration': v.get('duration'), 'courses': courses,
                          'tier': 'B', 'code': code, 'board': 'ial', 'provider': 'mr-hassaans-maths',
                          'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
            cclass['B ial ' + code] += 1
            continue
    paper = None
    cie_tag = bool(re.search(r'9709|CAIE', t, re.I))
    m = CIE_CODE.search(t)
    if m:
        paper = m.group(1)
    else:
        m2 = CIE_SESS.search(t) or CIE_SPEC.search(t) or CIE_TEXT.search(t) or CIE_BARE.search(t)
        if m2:
            g = m2.group(1)
            paper = g if len(g) == 2 else '0' + g
    if not paper and cie_tag:
        mp = CIE_PM.search(t)
        if mp:
            gs = mp.groups()
            if gs[0] or gs[1] or gs[2]:
                g = next(g for g in gs[:3] if g)
                paper = g if len(g) == 2 else '0' + g       # P1-P6 marker -> paper n
            elif gs[3]:
                paper = '4'                                  # M n (CAIE) -> 9709 Paper 4 Mechanics
            elif gs[4]:
                paper = '5' if gs[4] == '1' else '6'         # S1 -> Paper 5, S2/S3 -> Paper 6
    if paper and cie_tag:
        pd = cie_paper(paper)
        courses = CIE_P.get(pd)
        if courses:
            poolB.append({'id': vid, 'title': t, 'duration': v.get('duration'), 'courses': courses,
                          'tier': 'B', 'code': f'9709/{paper}', 'board': 'cie', 'provider': 'mr-hassaans-maths',
                          'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
            cclass['B cie 9709 P' + pd] += 1
            continue
    paper = None
    m = IG_CODE.search(t)
    if m:
        paper = m.group(1)
    else:
        m2 = IG_SESS.search(t) or IG_TEXT.search(t) or IG_BARE.search(t)
        if m2:
            g = m2.group(1)
            paper = g if len(g) == 2 else '0' + g
    if paper and re.search(r'0580', t):
        course = IG_MAP.get(ig_paper(paper))
        if course:
            poolB.append({'id': vid, 'title': t, 'duration': v.get('duration'), 'courses': [course],
                          'tier': 'B', 'code': f'0580/{paper}', 'board': 'cie-igcse',
                          'p9b': course.endswith('-core'), 'provider': 'mr-hassaans-maths',
                          'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
            cclass['B cie 0580 P' + ig_paper(paper)] += 1
            continue
    m = MA_CODE.search(t)
    if m:
        num, hf = m.group(1), m.group(2).upper()
        course = 'igcse-maths-a-18-higher' if hf == 'H' else 'igcse-maths-a-18-foundation'
        poolB.append({'id': vid, 'title': t, 'duration': v.get('duration'), 'courses': [course],
                      'tier': 'B', 'code': f'4MA1/{num}{hf}', 'board': 'edexcel-igcse',
                      'p9b': hf == 'F', 'provider': 'mr-hassaans-maths',
                      'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
        cclass['B 4MA1 ' + hf] += 1
        continue
    if MB_CODE.search(t):
        poolB.append({'id': vid, 'title': t, 'duration': v.get('duration'), 'courses': ['igcse-maths-b-16'],
                      'tier': 'B', 'code': '4MB', 'board': 'edexcel-igcse', 'provider': 'mr-hassaans-maths',
                      'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
        cclass['B 4MB'] += 1
        continue
    if PM_CODE.search(t):
        poolB.append({'id': vid, 'title': t, 'duration': v.get('duration'), 'courses': ['igcse-further-maths-19'],
                      'tier': 'B', 'code': '4PM', 'board': 'edexcel-igcse', 'provider': 'mr-hassaans-maths',
                      'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
        cclass['B 4PM'] += 1
        continue
    if XM_CODE.search(t):
        # modular-sample content without a unit code: unit-1 topics -> P9B Tier A
        poolA.append({'id': vid, 'title': t, 'duration': v.get('duration'),
                      'course': 'igcse-maths-a-modular-24-higher-unit-1', 'tier': 'A',
                      'p9b': True, 'provider': 'mr-hassaans-maths',
                      'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
        cclass['A 4XMA modular-u1'] += 1
        continue
    # ---- Tier A: uncoded, route by unit marker / vocabulary
    if not MATHW.search(t):
        skips.append({'id': vid, 'title': t, 'class': 'misc (no maths vocabulary, no honest spine target)'})
        cclass['skip no-vocab'] += 1
        continue
    course = None
    mm = re.search(r'Pure\s*Math\w*\s*\(?\s*P([1-4])\s*\)?', t, re.I)
    if mm:
        course = f'ial-maths-20-pure-{mm.group(1)}'
    elif M_FP.search(t):
        course = 'ial-further-maths-18-further-pure-1'
    elif M_D.search(t):
        course = 'ial-maths-20-decision-1'
    elif M_M.search(t):
        course = 'ial-maths-20-mechanics-1'
    elif M_S.search(t):
        course = 'ial-maths-20-statistics-1'
    else:
        mp = M_P.search(t)
        if mp and re.search(r'IAL|Edexcel|Solomon|Text Book|Textbook', t, re.I):
            course = f'ial-maths-20-pure-{mp.group(1)}'
    if course:
        poolA.append({'id': vid, 'title': t, 'duration': v.get('duration'), 'course': course,
                      'tier': 'A', 'provider': 'mr-hassaans-maths',
                      'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
        cclass['A ' + course] += 1
        continue
    skips.append({'id': vid, 'title': t, 'class': 'ambiguous (held for idf best-of / judgment)'})
    cclass['A-ambiguous'] += 1

json.dump(poolB, open(f'{OUT}/tier-b.json', 'w'), indent=1)
json.dump(poolA, open(f'{OUT}/tier-a.json', 'w'), indent=1)
json.dump(skips, open(f'{OUT}/skips.json', 'w'), indent=1)
amb = [s for s in skips if s['class'].startswith('ambiguous')]
json.dump([{'id': s['id'], 'title': s['title'], 'duration': next(v['duration'] for v in ups['videos'] if v['id'] == s['id']),
            'course': None, 'tier': 'A', 'provider': 'mr-hassaans-maths',
            'watchUrl': f"https://www.youtube.com/watch?v={s['id']}"} for s in amb],
          open(f'{OUT}/tier-a-ambiguous.json', 'w'), indent=1)
print('pool', len(ups['videos']), '| corpus overlap', cclass['already in shipped union'])
print('Tier B anchors:', len(poolB), '| rows:', sum(len(p['courses']) for p in poolB))
print('Tier A marker-routed:', len(poolA), '| ambiguous (held):', len(amb))
print('skips:', len(skips))
print(dict(cclass.most_common()))
