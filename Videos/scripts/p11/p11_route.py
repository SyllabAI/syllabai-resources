#!/usr/bin/env python3
"""P11 step 1: deterministic router — FOURTEEN channel pools -> lanes.

Targets are the 38 uncovered courses' clusters plus disclosed cross-board
candidates and small increments onto covered courses (P5/P7/P10 precedent).
Every video in every pool is dispositioned exactly once:
  - 'already in shipped union' -> skip
  - Tier B: machine-checkable syllabus/paper codes in titles (9708/41, WDM11,
    WMA11-14, 4MA1 Paper n, 0455 paper walkthroughs, 0620 walkthroughs)
    -> course-level anchors, method paper-code, confidence high,
       boardMismatch false (same qualification).
  - Tier A: spec rows routed to per-course candidate lists; binding happens in
    the judgment pass over the distinctive-token pre-pass + class tables.
    All Tier A rows carry boardMismatch:true (title-only posture) at emit.
  - honest skips: no-target qualifications (UK GCE econ 9EC0, CIE A-level
    history 9489, O-level US history 0409, ESL 0510/0511, IB economics,
    GCSE English 1EN0/8700, GCSE maths 1MA1, Edexcel IGCSE accounting 4AC
    has no CIE-independent candidate), predicted/guess papers, summaries,
    community/misc.
"""
import json, os, re, collections

RES = '/home/z/my-project/repos/syllabai-resources'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p11'
os.makedirs(OUT, exist_ok=True)

POOLS = ['enhancetuition', 'econplusdal', 'yimakesiteasy', 'cambridge-study-materials',
         'james-gan', 'igcse-online', 'igcse-computer-science', 'purple-shirt-history',
         'mindful-maths', 'cambridge-accounting', 'ar-accounting',
         'evm-dr-mohamed-saber', 'mr-salles', 'the-igcse-geographer']

T = {
    'business_ig':  ['cie-igcse-business-23', 'cie-igcse-business-25', 'igcse-business-19'],
    'econ_ig':      ['cie-igcse-economics-20', 'cie-igcse-economics-25', 'igcse-economics-17'],
    'econ_ig_cie':  ['cie-igcse-economics-20', 'cie-igcse-economics-25'],
    'econ_al':      ['cie-a-level-economics-23'],
    'ict':          ['cie-igcse-ict-21', 'igcse-ict-17'],
    'cs_ig':        ['cie-igcse-computer-science-23'],
    'cs_al':        ['cie-as-computer-science-19', 'cie-a-level-computer-science-19'],
    'phys_al':      ['cie-as-physics-25', 'cie-a-level-physics-25'],
    'maths9709':    ['cie-as-maths-20-pure-1', 'cie-a-level-maths-20-pure-1'],
    'accounting_al': ['cie-as-accounting-21', 'cie-a-level-accounting-21'],
    'accounting_ig': ['cie-igcse-accounting-21', 'cie-igcse-accounting-25'],
    'history':      ['cie-igcse-history-18', 'igcse-history-17'],
    'em_ig':        ['cie-igcse-environmental-management-25'],
    'geo':          ['cie-igcse-geography-20', 'cie-igcse-geography-25', 'igcse-geography-19'],
    'eng_cie':      ['cie-igcse-english-language-20', 'cie-igcse-english-language-25'],
    'eng_lit_ed':   ['igcse-english-literature-16'],
    'eng_p1':       ['igcse-english-language-a-16-paper-1-non-fiction-texts-and-transactional-writing'],
    'eng_p2':       ['igcse-english-language-a-16-paper-2-poetry-and-prose-texts-and-imaginative-writing'],
    'eng_p3':       ['igcse-english-language-a-16-paper-3-coursework'],
    'd1':           ['ial-maths-20-decision-1'],
    'pure-1':       ['ial-maths-20-pure-1'],
    'pure-2':       ['ial-maths-20-pure-2'],
    'pure-3':       ['ial-maths-20-pure-3'],
    'pure-4':       ['ial-maths-20-pure-4'],
    'stats-1':      ['ial-maths-20-statistics-1'],
    'stats-2':      ['ial-maths-20-statistics-2'],
    'fp1':          ['ial-further-maths-18-further-pure-1'],
    'a18h':         ['igcse-maths-a-18-higher'],
    'chem0620':     ['cie-igcse-chemistry-23'],
    'phys0625':     ['cie-igcse-physics-23'],
    'maths0580':    ['cie-igcse-maths-25-extended'],
}

# shared skip patterns
IB = re.compile(r'\bIB\b|International Baccalaureate', re.I)

corpus = set()
vmd = f'{HUB}/content/video-map'
for f in os.listdir(vmd):
    if f.endswith('.json'):
        for v in json.load(open(f'{vmd}/{f}')).get('videos', []):
            corpus.add(v['id'])

tierB, tierA, skips = [], [], []
cclass = collections.Counter()

def W(vid):
    return f'https://www.youtube.com/watch?v={vid}'

def route_A(vid, title, dur, provider, key, marker=False, moduleNamed=False):
    tierA.append({'id': vid, 'title': title, 'duration': dur, 'provider': provider,
                  'courses': T[key], 'tier': 'A', 'marker': marker,
                  'moduleNamed': moduleNamed, 'watchUrl': W(vid)})
    cclass[f'{provider} A {key}'] += 1

def route_B(vid, title, dur, provider, key, code, kind='past-paper-walkthrough'):
    tierB.append({'id': vid, 'title': title, 'duration': dur, 'provider': provider,
                  'courses': T[key], 'tier': 'B', 'code': code,
                  'watchUrl': W(vid)})
    cclass[f'{provider} B {key}'] += 1

def skip(vid, title, cls):
    skips.append({'id': vid, 'title': title, 'class': cls})
    cclass[cls] += 1

def dur_of(v):
    return v.get('duration')

def route_pools():
    # ---------------- EnhanceTuition (CIE 9708 econ + 9706 accounting) -------
    for v in POOLS_V['enhancetuition']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if IB.search(t): skip(vid, t, 'no-target (IB qualification — not in the spine; ANCHOR-GRANULARITY §6)'); continue
        if re.search(r'9706|accounting', t, re.I):
            route_A(vid, t, dur_of(v), 'enhancetuition', 'accounting_al'); continue
        pw = re.search(r'\b9708\s*/\s*(\d{2})\s*/\s*s?(\d{4})', t, re.I) or \
             re.search(r'Exam Walkthrough[^)]*9708', t, re.I)
        if pw:
            route_B(vid, t, dur_of(v), 'enhancetuition', 'econ_al', '9708/' + (pw.group(1) or 'paper'))
            continue
        if re.search(r'9708|CIE\s+(AS|A2)\s+Economics|CIE Economics|CIE A.?Level Economics|A2 Economics|AS Economics|CIE A2|CIE AS', t, re.I):
            route_A(vid, t, dur_of(v), 'enhancetuition', 'econ_al'); continue
        if re.search(r'economics|elastic|inflation|demand|supply|macro|micro|fiscal|monetary|tariff|\bGDP\b|unemploy|trade|laffer|tax|subsid|market|price', t, re.I):
            route_A(vid, t, dur_of(v), 'enhancetuition', 'econ_al'); continue
        skip(vid, t, 'misc (no CIE econ/accounting vocabulary, no honest spine target)')

    # ---------------- EconplusDal (UK Edexcel GCE econ — no target) ----------
    for v in POOLS_V['econplusdal']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        skip(vid, t, 'no-target (UK Edexcel GCE A-level Economics 9EC0 register — no Edexcel econ qualification in the spine (IAL/IGCSE econ only); GCSE-econ titles 0; ANCHOR-GRANULARITY §6, disclosed)')

    # ---------------- Yi MakesItEasy (0460 geo + 0450 business + FM CP1) -----
    for v in POOLS_V['yimakesiteasy']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'A-?Level Further Maths|Further Maths CP\d|Core Pure', t, re.I):
            route_A(vid, t, dur_of(v), 'yimakesiteasy', 'fp1'); continue
        if re.search(r'IGCSE Geography|0460', t, re.I):
            route_A(vid, t, dur_of(v), 'yimakesiteasy', 'geo'); continue
        if re.search(r'0450|Business', t, re.I):
            route_A(vid, t, dur_of(v), 'yimakesiteasy', 'business_ig'); continue
        if re.search(r'0455|Economics', t, re.I):
            route_A(vid, t, dur_of(v), 'yimakesiteasy', 'econ_ig'); continue
        if re.search(r'0680|Environmental', t, re.I):
            route_A(vid, t, dur_of(v), 'yimakesiteasy', 'em_ig'); continue
        skip(vid, t, 'misc (no syllabus marker, no honest spine target)')

    # ------------- Cambridge IGCSE/AS/A Study Materials (0450 + 0417) --------
    for v in POOLS_V['cambridge-study-materials']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'0510|0511|ESL|English as a Second Language', t, re.I):
            skip(vid, t, 'no-target (CIE ESL 0510/0511 qualification — spine English courses are 0500 First Language; §6, disclosed)'); continue
        if re.search(r'0450|Business', t, re.I):
            route_A(vid, t, dur_of(v), 'cambridge-study-materials', 'business_ig'); continue
        if re.search(r'0417|\bICT\b', t, re.I):
            route_A(vid, t, dur_of(v), 'cambridge-study-materials', 'ict'); continue
        if re.search(r'0455|Economics', t, re.I):
            route_A(vid, t, dur_of(v), 'cambridge-study-materials', 'econ_ig'); continue
        if re.search(r'0452|Accounting', t, re.I):
            route_A(vid, t, dur_of(v), 'cambridge-study-materials', 'accounting_ig'); continue
        skip(vid, t, 'misc (no syllabus marker, no honest spine target)')

    # ---------------- James Gan (9618 + 9702 + 9709 + 0478) ------------------
    for v in POOLS_V['james-gan']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'\(?\s*9618\s*\)?', t):
            route_A(vid, t, dur_of(v), 'james-gan', 'cs_al'); continue
        if re.search(r'\(?\s*9702\s*\)?', t):
            route_A(vid, t, dur_of(v), 'james-gan', 'phys_al'); continue
        if re.search(r'\(?\s*9709\s*\)?', t):
            route_A(vid, t, dur_of(v), 'james-gan', 'maths9709'); continue
        if re.search(r'0478|IGCSE Computer Science', t, re.I):
            route_A(vid, t, dur_of(v), 'james-gan', 'cs_ig'); continue
        skip(vid, t, 'misc (no syllabus code, no honest spine target)')

    # ---------------- IGCSE Online (multi-subject CIE IGCSE) -----------------
    for v in POOLS_V['igcse-online']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'prediction|predict|guess paper', t, re.I):
            skip(vid, t, 'skip (predicted/guess paper — no machine-checkable real paper code, honest)'); continue
        if re.search(r'All (of|Igcse|IGCSE)|summary', t, re.I) and re.search(r'\bin \d+ minutes?\b', t, re.I):
            skip(vid, t, 'skip (whole-subject summary compilation — cannot bind honestly, honest)'); continue
        pw = re.search(r'0455[^.]{0,30}(May/June|Feb/March|Oct/Nov)\s+20\d\d\s+paper\s+(\d+)', t, re.I)
        if pw and re.search(r'0455', t):
            route_B(vid, t, dur_of(v), 'igcse-online', 'econ_ig_cie', '0455/' + pw.group(2)); continue
        pw2 = re.search(r'0620[^.]{0,30}(Feb/March|May/June|Oct/Nov)\s+20\d\d\s+paper\s+(\d+)', t, re.I)
        if pw2 and re.search(r'0620', t):
            route_B(vid, t, dur_of(v), 'igcse-online', 'chem0620', '0620/' + pw2.group(2)); continue
        if re.search(r'0478|Computer Science', t, re.I):
            route_A(vid, t, dur_of(v), 'igcse-online', 'cs_ig'); continue
        if re.search(r'0455|Economics', t, re.I):
            route_A(vid, t, dur_of(v), 'igcse-online', 'econ_ig'); continue
        if re.search(r'0452|Accounts|Accounting', t, re.I):
            route_A(vid, t, dur_of(v), 'igcse-online', 'accounting_ig'); continue
        if re.search(r'0620|Chemistry', t, re.I):
            route_A(vid, t, dur_of(v), 'igcse-online', 'chem0620'); continue
        if re.search(r'0625|Physics', t, re.I):
            route_A(vid, t, dur_of(v), 'igcse-online', 'phys0625'); continue
        if re.search(r'0580|Mathematics', t, re.I):
            route_A(vid, t, dur_of(v), 'igcse-online', 'maths0580'); continue
        if re.search(r'0470|History', t, re.I):
            route_A(vid, t, dur_of(v), 'igcse-online', 'history'); continue
        if re.search(r'0450|Business', t, re.I):
            route_A(vid, t, dur_of(v), 'igcse-online', 'business_ig'); continue
        skip(vid, t, 'misc (no syllabus marker, no honest spine target)')

    # ---------------- IGCSE Computer Science (0478 topical) ------------------
    for v in POOLS_V['igcse-computer-science']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'computer science|pseudocode|binary|fetch|sensor|translator|database|logic', t, re.I):
            route_A(vid, t, dur_of(v), 'igcse-computer-science', 'cs_ig'); continue
        skip(vid, t, 'misc (no CS vocabulary, no honest spine target)')

    # ---------------- Purple Shirt History (0470 / 0409 / 9489) --------------
    for v in POOLS_V['purple-shirt-history']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'\b0409\b|US History', t, re.I):
            skip(vid, t, 'no-target (CIE O-level US History 0409 — not in the spine; §6)'); continue
        if re.search(r'\b9489\b|Cambridge AL History', t, re.I):
            skip(vid, t, 'no-target (CIE A-level History 9489 — not in the spine; §6)'); continue
        if re.search(r'0470|IGCSE History|IGCSE HISTORY', t, re.I):
            route_A(vid, t, dur_of(v), 'purple-shirt-history', 'history'); continue
        skip(vid, t, 'misc (no syllabus marker, no honest spine target)')

    # ---------------- Mindful Maths (IAL D1 + WMA/WDM/4MA1 papers) -----------
    for v in POOLS_V['mindful-maths']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'Predicted Paper', t, re.I):
            skip(vid, t, 'skip (predicted paper — no real session code, honest)'); continue
        if re.search(r'\bWDM11\b', t):
            route_B(vid, t, dur_of(v), 'mindful-maths', 'd1', 'WDM11'); continue
        wm = re.search(r'\bWMA1([1-4])\b', t)
        if wm:
            route_B(vid, t, dur_of(v), 'mindful-maths', f'pure-{wm.group(1)}', f'WMA1{wm.group(1)}'); continue
        if re.search(r'\b4MA1\b', t) and re.search(r'Paper\s+\d', t, re.I):
            route_B(vid, t, dur_of(v), 'mindful-maths', 'a18h', '4MA1'); continue
        if re.search(r'Decision\s*1', t, re.I):
            route_A(vid, t, dur_of(v), 'mindful-maths', 'd1', marker=True); continue
        wm2 = re.search(r'whole of (?:AS Level|A Level) (Pure [1-4]|Statistics [1-2]|Mechanics|Decision)', t, re.I)
        if wm2:
            name = wm2.group(1)
            key = {'Pure 1': 'pure-1', 'Pure 2': 'pure-2', 'Pure 3': 'pure-3', 'Pure 4': 'pure-4',
                   'Statistics 1': 'stats-1', 'Statistics 2': 'stats-2',
                   'Mechanics': None, 'Decision': 'd1'}.get(name)
            if key in (None,):
                skip(vid, t, 'no-target (UK-register A-level Mechanics module — spine mechanics courses are Edexcel IAL M1/M2; UK module name unnumbered; §6)')
            else:
                tierA.append({'id': vid, 'title': t, 'duration': dur_of(v), 'provider': 'mindful-maths',
                              'courses': T[key], 'tier': 'A', 'marker': False,
                              'moduleNamed': True, 'watchUrl': W(vid)})
                cclass['mindful-maths A module-' + key] += 1
            continue
        if re.search(r'GCSE Mathematics', t, re.I):
            skip(vid, t, 'no-target (Edexcel GCSE maths 1MA1 — qualification not in the spine; §6)'); continue
        if re.search(r'4MA1|IGCSE', t):
            route_A(vid, t, dur_of(v), 'mindful-maths', 'a18h'); continue
        skip(vid, t, 'misc (no maths-qualification marker, no honest spine target)')

    # ---------------- Cambridge Accounting (0452/9706 explicit) --------------
    for v in POOLS_V['cambridge-accounting']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'A Level', t):
            route_A(vid, t, dur_of(v), 'cambridge-accounting', 'accounting_al'); continue
        if re.search(r'IGCSE', t):
            route_A(vid, t, dur_of(v), 'cambridge-accounting', 'accounting_ig'); continue
        skip(vid, t, 'misc (no register marker, no honest spine target)')

    # ---------------- AR Accounting (0452/9706 mixed register) ---------------
    for v in POOLS_V['ar-accounting']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'A Level', t):
            route_A(vid, t, dur_of(v), 'ar-accounting', 'accounting_al'); continue
        route_A(vid, t, dur_of(v), 'ar-accounting', 'accounting_ig')
        cclass['ar-accounting A accounting_ig-default'] += 1

    # ---------------- EVM With Dr Mohamed Saber (0680) -----------------------
    for v in POOLS_V['evm-dr-mohamed-saber']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'0680|Environmental Management|EVM|Env.? ?Management', t, re.I):
            route_A(vid, t, dur_of(v), 'evm-dr-mohamed-saber', 'em_ig'); continue
        skip(vid, t, 'misc (no EM vocabulary, no honest spine target)')

    # ---------------- Mr Salles Teaches English (0500/0522 + 4EA1/4ET1) ------
    for v in POOLS_V['mr-salles']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'0522|0500|Cambridge IGCSE', t, re.I):
            route_A(vid, t, dur_of(v), 'mr-salles', 'eng_cie'); continue
        if re.search(r'4EA1', t, re.I):
            if re.search(r'Paper 3|coursework', t, re.I):
                route_A(vid, t, dur_of(v), 'mr-salles', 'eng_p3')
            elif re.search(r'Paper 2', t, re.I):
                route_A(vid, t, dur_of(v), 'mr-salles', 'eng_p2')
            else:
                route_A(vid, t, dur_of(v), 'mr-salles', 'eng_p1')
            continue
        if re.search(r'4ET1|IGCSE\s+Literature|Literature\s+IGCSE', t, re.I):
            route_A(vid, t, dur_of(v), 'mr-salles', 'eng_lit_ed'); continue
        if re.search(r'Edexcel IGCSE|IGCSE English Language', t, re.I):
            route_A(vid, t, dur_of(v), 'mr-salles', 'eng_p1'); continue
        if re.search(r'IGCSE', t, re.I) and re.search(r'writing|describe|narrative|directed|summary|mark scheme', t, re.I):
            route_A(vid, t, dur_of(v), 'mr-salles', 'eng_cie'); continue
        if re.search(r'AQA|OCR\b|\bGCSE\b', t, re.I):
            skip(vid, t, 'no-target (UK GCSE English Language 1EN0 / AQA 8700 register — no GCSE English course in the spine; §6)'); continue
        skip(vid, t, 'misc (no English-qualification marker, no honest spine target)')

    # ---------------- The iGCSE Geographer (0460) ----------------------------
    for v in POOLS_V['the-igcse-geographer']:
        vid, t = v['id'], v['title']
        if vid in corpus: skip(vid, t, 'already in shipped union'); continue
        if re.search(r'0460|GEOGRAPHY|Geography', t, re.I):
            route_A(vid, t, dur_of(v), 'the-igcse-geographer', 'geo'); continue
        skip(vid, t, 'misc (no geography marker, no honest spine target)')


POOLS_V = {p: json.load(open(f'{RES}/Videos/inventory/channels/{p}-uploads.json'))['videos'] for p in POOLS}
route_pools()

json.dump(tierB, open(f'{OUT}/tier-b.json', 'w'), indent=1)
json.dump(tierA, open(f'{OUT}/tier-a.json', 'w'), indent=1)
json.dump(skips, open(f'{OUT}/skips.json', 'w'), indent=1)
n_pool = sum(len(x) for x in POOLS_V.values())
print('pools', n_pool, '| corpus overlap', cclass['already in shipped union'])
print('Tier B anchors:', len(tierB), '| rows:', sum(len(p['courses']) for p in tierB))
print('Tier A routed:', len(tierA), '| rows:', sum(len(p['courses']) for p in tierA))
print('skips:', len(skips))
print(dict(cclass.most_common(30)))
