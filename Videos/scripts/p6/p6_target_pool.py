#!/usr/bin/env python3
"""P6 step 1: build the target pool — unmapped PhysicsOnline uploads that can
honestly route to a SyllabAI parent course.

Routing:
  - '- A Level Physics' marker + physics vocabulary -> cie-a-level-physics-25
  - '- GCSE Physics' marker + physics vocabulary    -> best of the two IGCSE
    parent spines by distinctive-token idf overlap (CIE 0625 vs Edexcel 4PH0)
  - unmarked physics vocabulary                     -> best of all three spines
Sewage (exam news, paper predictions/walkthroughs, study advice, admissions-test
prep, BPhO, channel promos) and pure-maths masterclasses (no A-level-pure-maths
spine exists) are skipped with a count; every skip class is honest-empty."""
import json, math, re, os, collections

RES = '/home/z/my-project/repos/syllabai-resources/Videos'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p6'
os.makedirs(OUT, exist_ok=True)

PARENTS = ['cie-a-level-physics-25', 'cie-igcse-physics-23', 'igcse-physics-19']

STOP = set("""a an the of and or to in on for with without into from by at as is are be been being it its
this that these those how what why when which who whom do does did done can could should would will shall
may might must not no nor if then than so such about above below between during before after under over
again further once here there all any both each few more most other some own same too very just also
gcse physics maths math level cie edexcel aqa ocr igcse part vs using use used new explain explained
revision intro introduction basics basic lesson episode worked example examples calculate calculating
physics online lewis matheson""".split())

def toks(s):
    return [t[:-1] if len(t) > 3 and t.endswith('s') else t
            for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP and len(t) > 1]

# ---- spines: idf-weighted token docs per SPEC_POINT (parents as context)
spine_docs = {}
for course in PARENTS:
    cur = json.load(open(f'{HUB}/content/{course}/curriculum.json'))
    nb = {n['code']: n for n in cur['nodes']}
    specs = [n for n in cur['nodes'] if n['family'] == 'SPEC_POINT']
    docs = {}
    for sp in specs:
        parts = [sp['title']]
        for pc in sp.get('parents', []):
            pn = nb.get(pc)
            if pn:
                parts.append(pn['title'])
                for pc2 in pn.get('parents', []):
                    pn2 = nb.get(pc2)
                    if pn2:
                        parts.append(pn2['title'])
        docs[sp['code']] = toks(' '.join(parts))
    df = collections.Counter(t for d in docs.values() for t in set(d))
    idf = {t: math.log(len(docs) / df[t]) for t in df}
    spine_docs[course] = {'specs': specs, 'docs': docs, 'idf': idf}

def best_course(title, courses):
    q = set(toks(title))
    scored = []
    for c in courses:
        sd = spine_docs[c]
        s = sum(sd['idf'][t] for t in q if t in sd['idf'])
        scored.append((s, c))
    scored.sort(reverse=True)
    return scored

# ---- corpus exclusion: any PO video already declared in the union
corpus = set()
vmd = f'{HUB}/content/video-map'
for f in os.listdir(vmd):
    if not f.endswith('.json'):
        continue
    for v in json.load(open(f'{vmd}/{f}')).get('videos', []):
        if str(v.get('provider', '')) in ('physics-online', 'physicsonline') or \
           re.search(r'alevelphysicsonline|gcsephysicsonline', json.dumps(v), re.I):
            corpus.add(v['id'])

ups = json.load(open(f'{RES}/inventory/channels/physicsonline-uploads.json'))['videos']

# ---- classifiers
AL = re.compile(r'\ba[ -]?level\b|\bas level\b|\ba2\b', re.I)
GC = re.compile(r'\bgcse\b', re.I)
PHYSW = re.compile(r'physic|circuit|current|voltage|resistance|\bohm|wave|wavelength|frequency|amplitude'
    r'|refract|reflect|diffract|interfer|polaris|photoelectric|photon|quantum|nuclear|radioactiv'
    r'|\balpha\b|\bbeta\b|gamma|half.?life|fission|fusion|particle|quark|lepton|hadron|capacitor'
    r'|capacitan|electric field|magnetic|flux|faraday|lenz|alternating current|transformer|thermal'
    r'|specific heat|latent heat|ideal gas|gas law|boyle|charles|pressure|density|upthrust|archimedes'
    r'|astrophys|\bstar\b|telescope|red.?shift|doppler|hubbl|quasar|black hole|simple harmonic'
    r'|oscillat|damping|resonance|projectile|momentum|suvat|newton|friction|terminal veloc'
    r'|\bmoments?\b|gravitational|elastic|hooke|young modulus|kinetic|potential energy|impulse'
    r'|collision|protactinium|inverse square|\bshc\b|geiger|work function|stopping potential'
    r'|electronvolt|de broglie|line spectra|energy level|isotope|nuclide|becquerel|\bdecay\b'
    r'|ammeter|voltmeter|oscilloscope|pendulum|acceler|velocity|displacement|\bspeed\b'
    r'|distance.?time|velocity.?time|graph|equation of motion|charge|coulomb|\bemf\b'
    r'|internal resistance|potential divider|thermistor|\bldr\b|diode|superconduc|\bforces?\b'
    r'|free.?body|equilibrium|vector|scalar|springs?|sylvanas|ultrasound|echo|sonar|seismic'
    r'|magnet|induction|motor|generator|transformer|insulat|conduction|convection|radiation'
    r'|earth.?sun|solar|lunar|eclipse|orbit|satellite|weight|mass|gravity|momentum|stopping distance'
    r'|crumple|braking|terminal|parachut|skydiv|plane|balanc|seesaw|lever|pivot|centre of mass'
    r'|center of mass|hydraul|pascal|barometer|manometer|vacuum|atmospheric pressure|boiling'
    r'|melting|evaporat|condensat|sublimat|diffusion|brownian|kelvin|celsius|thermometer'
    r'|expansion|contraction|bimetallic|conductor|insulator|semiconductor|static|electrostatic'
    r'|van de graaff|lightning|electric shock|plug|fuse|earth wire|live wire|neutral wire|mains'
    r'|kwh|kilowatt|watt|power rating|efficiency|sankey|energy transfer|dissipation|lubricat'
    r'|streamlin|crumple zone|seat belt|air bag|work done|joule|newton meter|pulley|inclined plane'
    r'|screw|wedge|wheel and axle|gears?|linkage|cam|crank|piston|turbine|engine|motor fuel|battery')
SEWAGE = re.compile(r'grade \d|revision plan|past paper|paper \d|\bexams?\b|mark scheme|walkthrough of'
    r'|solutions? to|question \d|specimen|may.?june|oct.?nov|summer \d|20\d\d paper|results day'
    r'|grade boundar|live q|q ?& ?a|ask me|study with me|how i|tips|advice|prepare|revision timetable'
    r'|new course|coming soon|subscribe|merch|website tour|what.?s new|sponsor|ESAT|admissions test'
    r'|entrance|BPhO|olympiad|can you (get|answer|solve)|in \d+ (seconds|minutes)|year 1[23]'
    r'|struggling|for parents|\bbooks?\b|calculator|ten minutes|opportunit|awards|oxbridge|pat\b'
    r'|interview|personal statement|ucat|bmat|england|wales|cancelled|delayed|update|news|announce'
    r'|easter|christmas|holiday|summer break|my a\^|an a\^|get an a|full marks|equations? song'
    r'|revision checklist|revision guide|mock|predicted|prediction|grade 9|crossword|wordsearch'
    r'|quiz|flashcard|tiktok|instagram|discord|whatsapp|email|newsletter|coursework|isa\b|psa\b'
    r'|endorsement|lab book|commentary|demonstration ideas|teaching ideas|for teachers|lesson plan')
PUREMATH = re.compile(r'trigonom|pythagoras|sine rule|cosine rule|logarithm|natural log|log.?log'
    r'|quadratic|surds?|algebra|simultaneous|binomial|differentiat|integrat')

pool, skipped = [], collections.Counter()
for v in ups:
    vid, t = v['id'], v['title']
    if vid in corpus:
        continue
    s = t.lower()
    if PUREMATH.search(s) and not PHYSW.search(s):
        skipped['pure-maths masterclass (no target)'] += 1
        continue
    if SEWAGE.search(s):
        skipped['sewage (exam news / paper content / study advice / promo)'] += 1
        continue
    if not PHYSW.search(s):
        skipped['misc (no physics vocabulary, no honest spine target)'] += 1
        continue
    al, gc = bool(AL.search(s)), bool(GC.search(s))
    if al and not gc:
        route, level = 'cie-a-level-physics-25', 'a-level'
    else:
        cand = best_course(t, PARENTS if not gc else PARENTS[1:])
        s0, c0 = cand[0]
        if s0 <= 0:
            skipped['no spine overlap (no honest binding candidate)'] += 1
            continue
        route, level = c0, 'gcse' if c0 != 'cie-a-level-physics-25' else 'a-level'
    pool.append({'id': vid, 'title': t, 'duration': v.get('duration'), 'course': route,
                 'provider': 'physics-online', 'levelTag': level,
                 'watchUrl': f'https://www.youtube.com/watch?v={vid}'})

json.dump(pool, open(f'{OUT}/target-pool.json', 'w'), indent=1)
print(f'PO public pool: {len(ups)} | in corpus: {len(corpus)} | unmapped: {len(ups)-len(corpus)}')
print(f'routed: {len(pool)} | skipped: {dict(skipped)}')
print(dict(collections.Counter(p['course'] for p in pool)))
