#!/usr/bin/env python3
"""P10 step 1: deterministic router — TWO channel pools -> lanes.

Pool A  MrArnoldsMaths (UCwa84m5RqSJEkP9pYdeDYnw, 437 uploads): legacy Edexcel
  GCSE linear (1MA0-era) papers 2010-2014 + GCSE topic tutorials. The legacy
  GCSE qualification has NO course in the spine (the GCSE-shape courses are
  Edexcel IGCSE 4MA1/4MB0/4PM1), so paper walkthroughs are honest no-target
  skips per ANCHOR-GRANULARITY §6; the topic tutorials bind Tier A onto
  igcse-maths-a-18-higher (inherit PARENT — its 5 children cascade at build
  time). GCE C1-C4 / legacy GCE applied / AQA L2 FCSE: honest no-target.
Pool B  Maths Deity (UCODyYjai6abd1N5KGc1KacQ, 353 uploads): Edexcel IAL
  unit.section tutorial channel + IAL paper walkthroughs.
  Tier B (paper-code anchors, method paper-code, high, boardMismatch false):
    "Edexcel IAL P1..P4 <session> Exam Paper", "Practise Paper n (Edexcel IAL
    Pn)", "Edexcel style Pn Practise paper", "hardest questions (on|from)
    (Edexcel IAL) Pn/Mn/Sn", "Edexcel IAL M1/M2/S1/S2 <session> Exam Paper".
  Tier A (spec rows, llm-draft-external, medium/low, boardMismatch true):
    unit.section marker tutorials "(Edexcel IAL P1 3.7)" etc (lenient regex
    covers "( Edexcel", "E dexcel", "(IAL P4"), routed P1-P4 -> pure-1..4,
    M1 -> mechanics-1, M2 -> mechanics-2, S1 -> statistics-1, S2 ->
    statistics-2, FP1 -> further-pure-1; FP2 -> honest no-target (no FP2
    course in the spine, disclosed); non-marker topic rows routed by keyword.
  Skips: FP2 (no course), community/calculator content, no maths vocabulary.
Every video in both pools is dispositioned exactly once.
"""
import json, os, re, collections

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p10'
os.makedirs(OUT, exist_ok=True)

POOLS = {
    'mrarnoldsmaths': json.load(open(f'{RES}/Videos/inventory/channels/mrarnoldsmaths-uploads.json')),
    'mathsdeity': json.load(open(f'{RES}/Videos/inventory/channels/mathsdeity-uploads.json')),
}

corpus = set()
vmd = f'{HUB}/content/video-map'
for f in os.listdir(vmd):
    if f.endswith('.json'):
        for v in json.load(open(f'{vmd}/{f}')).get('videos', []):
            corpus.add(v['id'])

# ---------- shared skip patterns ----------
OL_CODE = re.compile(r'\b4037\s*/?', re.I)
GCE_CODE = re.compile(r'\b(9MA0|8MA0|666[3-9]|667[6-9]|668[3-9]|669[0-1])\s*/?', re.I)
OTHER_BOARD = re.compile(r'\b(AQA|OCR|MEI|WJEC)\b', re.I)
MATHW = re.compile(r'math|algebra|trigonom|geometr|calculus|differenti|integr|quadrat|vector|surds|'
    r'logarithm|binomial|factor|polynomial|inequal|coordinate|sequence|series|probabilit|statistic|'
    r'mechanic|kinemat|momentum|projectile|friction|pulley|matrix|complex number|argand|roots?|'
    r'indice|fraction|percent|ratio|circle|triangle|sine|cosine|tangent|curve|graph|equation|'
    r'proof|transform|function|asymptote|stationary|trapezium|arithmetic|geometric|'
    r'decision|algorithm|sort|critical path|histogram|normal distribution|correlation|'
    r'regression|discrete|continuous|limit|derivative|gradient|arc|sector|'
    r'volume|area|perimeter|mean|median|mode|variance|quantile|box ?plot|'
    r'permut|combinat|factorial|deviation|solomon|text book|textbook|tutorial|'
    r'number|decimal|negative|estimate|round|prime|multiple|divide|multiply|subtrac|add|'
    r'shape|angle|symmetry|conversion|currency|density|speed|distance|time|proportion|'
    r'poisson|uniform|hypothesis|sampling|population|lamina|centroid|restitution|'
    r'induction|recurrence|summation|loci|parabola|hyperbola|conjugate|determinant', re.I)

poolB, poolA, skips = [], [], []
cclass = collections.Counter()

# ================= MrArnoldsMaths =================
ARN = POOLS['mrarnoldsmaths']
GCE_CORE = re.compile(r'\bCore\s*[1-4]\b', re.I)
GCE_APPLIED = re.compile(r'A ?Level\s+Maths\s+(Stats|Mech|Statistics|Mechanics)\s*[1-6]?\s*:', re.I)
GCSE_PAPER = re.compile(r'(?:Higher|Foundation)', re.I)
GCSE_PNUM = re.compile(r'\bP[1-3]\b', re.I)
SESSION_Q = re.compile(r'\b(JAN|JUNE|JUN|NOV|OCT|MAY|MARCH|SUMMER|20\d\d)\b|\bQ\s*\d+', re.I)

for v in ARN['videos']:
    vid, t = v['id'], v['title']
    if vid in corpus:
        skips.append({'id': vid, 'title': t, 'class': 'already in shipped union'})
        cclass['arn corpus'] += 1
        continue
    if OTHER_BOARD.search(t) or re.search(r'AQA Level', t, re.I):
        skips.append({'id': vid, 'title': t, 'class': 'no-target (AQA/OCR/MEI qualification — board not in the spine; ANCHOR-GRANULARITY §6)'})
        cclass['arn skip other-board'] += 1
        continue
    if GCE_CODE.search(t):
        skips.append({'id': vid, 'title': t, 'class': 'no-target (Edexcel GCE/9MA0 paper — no GCE course in the spine; §6)'})
        cclass['arn skip GCE'] += 1
        continue
    if GCE_APPLIED.search(t) or (GCE_CORE.search(t) and SESSION_Q.search(t)):
        skips.append({'id': vid, 'title': t, 'class': 'no-target (legacy Edexcel GCE module paper/tutorial — C1-C4/Stats/Mech register, no GCE course in the spine; §6)'})
        cclass['arn skip GCE-core-applied'] += 1
        continue
    if OL_CODE.search(t):
        skips.append({'id': vid, 'title': t, 'class': 'no-target (CIE O-Level 4037; §6)'})
        cclass['arn skip 4037'] += 1
        continue
    if GCSE_PAPER.search(t) and GCSE_PNUM.search(t) and SESSION_Q.search(t):
        skips.append({'id': vid, 'title': t, 'class': 'no-target (legacy Edexcel GCSE linear 1MA0 paper — qualification not in the spine; GCSE-shape courses are Edexcel IGCSE 4MA1/4MB0/4PM1; §6)'})
        cclass['arn skip 1MA0-paper'] += 1
        continue
    if re.search(r'Core\s*Maths\s*:', t, re.I):
        # the channel's "Core Maths:" series is the legacy Edexcel GCE pure-core
        # (C1-C4) module teaching series — A-Level register, module unnumbered
        # in the title, no GCE course in the spine: honest no-target (§6)
        skips.append({'id': vid, 'title': t, 'class': 'no-target (legacy Edexcel GCE pure-core module tutorial ("Core Maths" series) — A-Level register with no numbered module in the title, no GCE course in the spine; §6)'})
        cclass['arn skip core-maths-series'] += 1
        continue
    ms_tut = re.search(r'Edexcel\s+S([12])\s+Tutorial', t, re.I)
    if ms_tut:
        # legacy GCE-register module TUTORIAL (no session, topic teaching not a
        # paper): cross-register topic row onto the same-numbered IAL module
        # course at the title-only bar (boardMismatch true, disclosed)
        poolA.append({'id': vid, 'title': t, 'duration': v.get('duration'),
                      'course': f'ial-maths-20-statistics-{ms_tut.group(1)}', 'tier': 'A',
                      'provider': 'mrarnoldsmaths', 'marker': False, 'moduleNamed': True,
                      'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
        cclass['arn A s' + ms_tut.group(1) + '-tutorial'] += 1
        continue
    if not MATHW.search(t):
        skips.append({'id': vid, 'title': t, 'class': 'misc (no maths vocabulary, no honest spine target)'})
        cclass['arn skip no-vocab'] += 1
        continue
    poolA.append({'id': vid, 'title': t, 'duration': v.get('duration'),
                  'course': 'igcse-maths-a-18-higher', 'tier': 'A',
                  'provider': 'mrarnoldsmaths', 'marker': False,
                  'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
    cclass['arn A topic'] += 1

# ================= Maths Deity =================
MD = POOLS['mathsdeity']
# lenient unit marker: "(Edexcel IAL P1 3.7)", "( Edexcel IAL P2 5.4)",
# "(E dexcel IAL FP1 1.7)", "(IAL P4 3.1)", "(IAL S1 Chapter 4)",
# "(Edexcel IAL M1 Chapter 2)", "(Edexcel IAL S1)", "(Edexcel IA S1)"
MD_MARKER = re.compile(r'\(?\s*(?:E\s?dexcel\s+)?\bIA\s?L?\s+(P[1-4]|M[12]|S[12]|FP[12]|D1)(?:\s*(?:Chapter\s*)?([0-9]+\s?\.[0-9]+|[0-9]+))?', re.I)
MD_UNIT = {'P1': 'ial-maths-20-pure-1', 'P2': 'ial-maths-20-pure-2',
           'P3': 'ial-maths-20-pure-3', 'P4': 'ial-maths-20-pure-4',
           'M1': 'ial-maths-20-mechanics-1', 'M2': 'ial-maths-20-mechanics-2',
           'S1': 'ial-maths-20-statistics-1', 'S2': 'ial-maths-20-statistics-2',
           'FP1': 'ial-further-maths-18-further-pure-1'}
MD_PAPER_P = re.compile(r'(?:IAL\s+P([1-4])[^.]{0,40}?Exam\s*Paper|Practise\s*Paper\s*([1-4])\s*\(Edexcel IAL|Edexcel style\s*P([1-4])\s*Practise|hardest\s*questions?\s*(?:on|from)\s*(?:Edexcel\s*IAL\s*)?P([1-4])\b|hardest\s*questions?\s*P([1-4])\b)', re.I)
MD_PAPER_SM = re.compile(r'hardest\s*questions?\s*from\s*(?:Edexcel\s*IAL\s*)?(S[12]|M[12])\b', re.I)
MD_PAPER_M = re.compile(r'IAL\s+M([12])\s+[^.]{0,40}?Exam\s*Paper', re.I)
MD_PAPER_S = re.compile(r'IAL\s+S([12])\s+[^.]{0,40}?Exam\s*Paper', re.I)
DROP = re.compile(r'Hasnain Ali|Casio|answer to|request\b', re.I)

for v in MD['videos']:
    vid, t = v['id'], v['title']
    if vid in corpus:
        skips.append({'id': vid, 'title': t, 'class': 'already in shipped union'})
        cclass['md corpus'] += 1
        continue
    if OL_CODE.search(t) or OTHER_BOARD.search(t) or GCE_CODE.search(t):
        skips.append({'id': vid, 'title': t, 'class': 'no-target (non-IAL qualification paper; §6)'})
        cclass['md skip other-qual'] += 1
        continue
    if DROP.search(t):
        skips.append({'id': vid, 'title': t, 'class': 'drop (community request / calculator how-to — not spec content, disclosed)'})
        cclass['md drop community-calc'] += 1
        continue
    # ---- Tier B: IAL paper walkthroughs (machine-checkable paper marker)
    mp = MD_PAPER_P.search(t)
    mm = MD_PAPER_M.search(t)
    ms = MD_PAPER_S.search(t)
    if mp:
        n = next(g for g in mp.groups() if g)
        poolB.append({'id': vid, 'title': t, 'duration': v.get('duration'),
                      'courses': [f'ial-maths-20-pure-{n}'], 'tier': 'B',
                      'code': f'IAL-P{n}', 'board': 'ial', 'provider': 'mathsdeity',
                      'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
        cclass['md B pure-' + n] += 1
        continue
    if mm:
        n = mm.group(1)
        poolB.append({'id': vid, 'title': t, 'duration': v.get('duration'),
                      'courses': [f'ial-maths-20-mechanics-{n}'], 'tier': 'B',
                      'code': f'IAL-M{n}', 'board': 'ial', 'provider': 'mathsdeity',
                      'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
        cclass['md B mech-' + n] += 1
        continue
    if ms:
        n = ms.group(1)
        poolB.append({'id': vid, 'title': t, 'duration': v.get('duration'),
                      'courses': [f'ial-maths-20-statistics-{n}'], 'tier': 'B',
                      'code': f'IAL-S{n}', 'board': 'ial', 'provider': 'mathsdeity',
                      'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
        cclass['md B stats-' + n] += 1
        continue
    msm = MD_PAPER_SM.search(t)
    if msm:
        u = msm.group(1).upper()
        course = MD_UNIT[u]
        poolB.append({'id': vid, 'title': t, 'duration': v.get('duration'),
                      'courses': [course], 'tier': 'B', 'code': 'IAL-' + u,
                      'board': 'ial', 'provider': 'mathsdeity',
                      'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
        cclass['md B ' + course] += 1
        continue
    # ---- FP2: honest no-target (no FP2 course in the spine, disclosed)
    if re.search(r'\bFP2\b', t):
        skips.append({'id': vid, 'title': t, 'class': 'no-target (Edexcel IAL FP2 — no further-pure-2 course in the spine; §6, disclosed)'})
        cclass['md skip FP2'] += 1
        continue
    # ---- Tier A: unit.section marker tutorials
    mk = MD_MARKER.search(t)
    if mk:
        unit = mk.group(1).upper()
        course = MD_UNIT.get(unit)
        if course:
            poolA.append({'id': vid, 'title': t, 'duration': v.get('duration'),
                          'course': course, 'tier': 'A', 'provider': 'mathsdeity',
                          'marker': True, 'unit': unit,
                          'section': (mk.group(2) or '').replace(' ', ''),
                          'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
            cclass['md A ' + course] += 1
            continue
    if not MATHW.search(t):
        skips.append({'id': vid, 'title': t, 'class': 'misc (no maths vocabulary, no honest spine target)'})
        cclass['md skip no-vocab'] += 1
        continue
    # non-marker topic rows -> ambiguous (cross-course pre-pass in judgment)
    poolA.append({'id': vid, 'title': t, 'duration': v.get('duration'),
                  'course': None, 'tier': 'A', 'provider': 'mathsdeity',
                  'marker': False,
                  'watchUrl': f'https://www.youtube.com/watch?v={vid}'})
    cclass['md A ambiguous'] += 1

json.dump(poolB, open(f'{OUT}/tier-b.json', 'w'), indent=1)
json.dump(poolA, open(f'{OUT}/tier-a.json', 'w'), indent=1)
json.dump(skips, open(f'{OUT}/skips.json', 'w'), indent=1)
n_pool = sum(len(p['videos']) for p in POOLS.values())
print('pools', n_pool, '| corpus overlap', cclass['arn corpus'] + cclass['md corpus'])
print('Tier B anchors:', len(poolB), '| rows:', sum(len(p['courses']) for p in poolB))
print('Tier A routed (marker+topic):', len(poolA), '| ambiguous:', sum(1 for p in poolA if p.get('course') is None))
print('skips:', len(skips))
print(dict(cclass.most_common()))
