#!/usr/bin/env python3
"""P7 step 1: build the target pool — unmapped remainder of the four remaining
external channel pools (amoeba-sisters / freesciencelessons / malmesbury-education /
doodlescience) routed onto the 12 science parent courses.

Routing follows each channel's title shape:
  - freesciencelessons: subject self-annotated ('GCSE Biology Revision \"...\"',
    'A Level Chemistry Revision (Year 13) \"...\"'); GCSE -> best of {igcse-19,
    cie-igcse-23} spines by idf; A-level -> best of {cie-a-level-25, ial-*};
    unmarked -> best of the subject's four parents
  - amoeba-sisters: US-curriculum biology -> best of the four biology parents
  - malmesbury-education: subject word in title (practicals mostly); non-science
    (English Lit poems, Spanish/German/French, KS3, DT, PE) skipped honest
  - doodlescience: '| GCSE Physics |' markers -> physics parents; unmarked -> any
    science course by idf
Sewage (promos, exam-technique, channel announcements) skipped with reasons."""
import json, math, re, os, collections

RES = '/home/z/my-project/repos/syllabai-resources/Videos'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p7'
os.makedirs(OUT, exist_ok=True)

COURSES = {
    'bio':  ['igcse-biology-19', 'cie-igcse-biology-23', 'cie-a-level-biology-25', 'ial-biology-18'],
    'chem': ['igcse-chemistry-19', 'cie-igcse-chemistry-23', 'cie-a-level-chemistry-25', 'ial-chemistry-17'],
    'phys': ['igcse-physics-19', 'cie-igcse-physics-23', 'cie-a-level-physics-25', 'ial-physics-19'],
    'maths': ['igcse-maths-a-18-higher'],
}
ALLC = COURSES['bio'] + COURSES['chem'] + COURSES['phys'] + COURSES['maths']

STOP = set("""a an the of and or to in on for with without into from by at as is are be been being it its
this that these those how what why when which who whom do does did done can could should would will shall
may might must not no nor if then than so such about above below between during before after under over
again further once here there all any both each few more most other some own same too very just also
gcse science sciences maths math level cie edexcel aqa ocr igcse part vs using use used
new explain explained revision intro introduction basics basic lesson episode worked example examples
calculate calculating required practical practicals triple higher foundation paper biology chemistry
physics freesciencelessons amoeba sisters malmesbury education doodle doodlescience year""".split())

def toks(s):
    return [t[:-1] if len(t) > 3 and t.endswith('s') else t
            for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP and len(t) > 1]

# ---- spines: idf-weighted token docs per SPEC_POINT (parents as context)
spine_docs = {}
for course in ALLC:
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
    spine_docs[course] = {'docs': docs, 'idf': idf}

def best_course(title, courses):
    q = set(toks(title))
    scored = []
    for c in courses:
        sd = spine_docs[c]
        s = sum(sd['idf'][t] for t in q if t in sd['idf'])
        scored.append((s, c))
    scored.sort(reverse=True)
    return scored

# ---- corpus exclusion: union of mapped video ids (any course, any provider)
corpus = set()
vmd = f'{HUB}/content/video-map'
for f in os.listdir(vmd):
    if not f.endswith('.json'): continue
    for m in json.load(open(f'{vmd}/{f}')).get('mappings', []):
        corpus.add(m['video'])

# ---- subject vocab gates per pool
BIO = re.compile(r'biolog|cell|enzyme|genetic|dna|gene|chromosom|mitosis|meiosis|osmosis|photosynthes'
    r'|respiration|digest|nervous|neuron|homeostasis|hormone|protein|enzyme|pathogen|immune|virus'
    r'|bacteri|ecosystem|evolution|selection|species|adaptation|food chain|food web|ecology'
    r'|heart|blood|circulator|lung|breath|kidney|brain|eye|ear|plant|root|stem|leaf|xylem|phloem'
    r'|transpir|germinat|seed|flower|pollinat|reproduc|menstrual|fertilis|embryo|cloning|tissue'
    r'|organ|microscope|microbio|culture|agar|quadrat|sampling|biodivers|deforest|eutrophic'
    r'|amino|protein synthesis|ribosome|mitochondri|chloroplast|membrane|diffusion|active transport'
    r'|carbohydrate|lipid|starch|glucose|biomolecul|food test|starch|iodine|biuret|ethanol emulsion'
    r'|fossil|extinction|classification|kingdom|vertebrat|invertebrat|arthropod|insect|mammal'
    r'|decompos|carbon cycle|nitrogen cycle|water cycle|abiotic|biotic|population|community'
    r'|reflex|synapse|receptor|effector|stimulus|insulin|glucagon|diabetes|thermoregulat|osmoregulat'
    r'|excretion|nephron|urea|pregnancy|fetus|foetus|placenta|umbilical|amenorrhea|menstruation'
    r'|immunity|vaccination|antibod|antigen|memory cell|lymphocyte|phagocyt|platelet|anaemia'
    r'|spirometer|tidal volume|ventilation|alveoli|trachea|bronchi|myofibril|actin|myosin|sarcomere'
    r'|tropism|auxin|phototropism|geotropism|gravitropism|homeobox|body plan|apoptosis|meiosis'
    r'|deamination|ornithine|urea|monogenic|dihybrid|autosomal|sex.?linked|codominant|allele|genotype|phenotype', re.I)
CHEM = re.compile(r'chemi|\bion\b|ionic|covalent|bonding|electrolysis|electrolyt|titration|neutralis'
    r'|acid|\bbase\b|alkali|\bpH\b|salt|halide|halogen|alkane|alkene|alcohol|ethanol|carboxylic'
    r'|ester|polymer|polymaris|cracking|fractional distillation|hydrocarbon|combustion|oxidation'
    r'|reduction|redox|displacement|reactivity|metal|ore|alloy|extraction|blast furnace|rust'
    r'|periodic table|group \d|noble gas|electron shell|configuration|isotope|atomic number|mass number'
    r'|mole|avogadro|concentration|molar|titration|yield|percentage|atom economy|equilibrium|haber'
    r'|contact process|exothermic|endothermic|enthalpy|bond energy|calorimetry|rate of reaction'
    r'|catalyst|catalys|collision theory|chromatography|distillation|filtration|crystallis'
    r'|flame test|flame emission|test for|positive ion|negative ion|anion|cation|precipitate'
    r'|spectra|mass spectrometry|infra.?red|infrared spectroscopy|nmr|water of crystallisation'
    r'|reflux|iodination|propanone|colourimetry|colorimetry|making salts|chloride|sulfate|sulphate'
    r'|nitrate|carbonate|gas tests?|limewater|glowing splint|damp litmus|bleach|naming salts'
    r'|nanoparticle|nanoscience|ceramics|composites|polymers|alloys|corrosion|life.?cycle'
    r'|atmosphere|greenhouse|global warming|climate change|pollution|carbon footprint|crude oil'
    r'|biofuel|hydrogen|fuel cell|battery|cell\b|electrode|half.?equation', re.I)
PHYS = re.compile(r'physic|circuit|current|voltage|resistance|\bohm|wave|wavelength|frequency|amplitude'
    r'|refract|reflect|diffract|interfer|polaris|photoelectric|photon|quantum|nuclear|radioactiv'
    r'|\balpha\b|\bbeta\b|gamma|half.?life|fission|fusion|particle|capacitor|electric field|magnetic'
    r'|flux|faraday|lenz|alternating current|transformer|thermal|specific heat|latent heat|ideal gas'
    r'|gas law|boyle|pressure|density|upthrust|archimedes|astrophys|\bstar\b|telescope|red.?shift'
    r'|doppler|hubbl|quasar|black hole|simple harmonic|oscillat|damping|resonance|projectile|momentum'
    r'|suvat|newton|friction|terminal veloc|\bmoments?\b|gravitational|elastic|hooke|young modulus'
    r'|kinetic|potential energy|impulse|collision|inverse square|geiger|work function|electronvolt'
    r'|line spectra|energy level|nuclide|becquerel|\bdecay\b|ammeter|voltmeter|oscilloscope|pendulum'
    r'|acceler|velocity|displacement|\bspeed\b|distance.?time|velocity.?time|graph|charge|coulomb'
    r'|\bemf\b|internal resistance|potential divider|thermistor|\bldr\b|diode|superconduc|\bforces?\b'
    r'|free.?body|equilibrium|vector|scalar|springs?|ultrasound|echo|sonar|seismic|magnet|induction'
    r'|motor|generator|insulat|conduction|convection|radiation|solar|lunar|eclipse|orbit|satellite'
    r'|weight|mass|gravity|stopping distance|crumple|braking|terminal|parachut|skydiv|balanc|seesaw'
    r'|lever|pivot|centre of mass|center of mass|hydraul|pascal|barometer|manometer|atmospheric pressure'
    r'|boiling|melting|evaporat|condensat|sublimat|brownian|kelvin|celsius|thermometer|expansion'
    r'|bimetallic|conductor|semiconductor|static|electrostatic|van de graaff|lightning|fuse|mains'
    r'|kwh|kilowatt|watt|power rating|efficiency|sankey|energy transfer|dissipation|work done|joule'
    r'|pulley|inclined plane|gears?|piston|turbine|engine|battery|ripple tank|u.?value|national grid'
    r'|fuse|ac and dc|renewable|non.?renewable|energy resource|kinetic theory|eye|lens|focal|myopia'
    r'|colour vision|correcting vision|camera|ray diagram|convex|concave|x.?ray|ripples|u.?value', re.I)
SEWAGE = re.compile(r'grade \d|revision plan|past paper|paper \d|\bexams?\b|mark scheme|walkthrough of'
    r'|solutions? to|specimen|may.?june|oct.?nov|20\d\d paper|results day|grade boundar|live q'
    r'|q ?& ?a|ask me|study with me|how i|tips|advice|prepare|revision timetable|new course|coming soon'
    r'|subscribe|merch|website tour|what.?s new|sponsor|admissions test|entrance|olympiad|can you (get|answer)'
    r'|in \d+ (seconds|minutes)|struggling|for parents|\bbooks?\b|calculator|opportunit|awards'
    r'|interview|personal statement|ucat|bmat|cancelled|delayed|update|news|announce|easter|christmas'
    r'|holiday|get an a|full marks|equations? song|revision checklist|revision guide|mock|predicted'
    r'|prediction|grade 9|crossword|wordsearch|quiz|flashcard|tiktok|instagram|discord|email|newsletter'
    r'|play button|welcome to|learn smarter|\bplus\b$|how to (revise|answer)|revise effectively'
    r'|teaching ideas|for teachers|lesson plan|demonstration ideas|endorsement|lab book|coursework'
    r'|poem analysis|poetry|english lit|literature|spanish lesson|german lesson|french lesson'
    r'|\bks3\b|design technology|scroll saw|frisbee|plural|verb|conjugation|nominative|accusative'
    r'|genitive|dative|ser and estar|ser or estar|reflexive|preorder|cartoon guide|meet the stars'
    r'|corresponding angles|transversals|parallel lines', re.I)

# NOTE: malmesbury GCSE-maths angle videos also land in sewage via 'parallel lines'
# (no honest maths-video lane for angle facts remains after P4 shelf-direct); disclosed below.

ups = {}
for pool, prov in [('amoeba-uploads', 'amoeba-sisters'), ('fsl-uploads', 'freesciencelessons'),
                   ('malmesbury-uploads', 'malmesbury-education'), ('doodle-uploads', 'doodlescience')]:
    for v in json.load(open(f'{RES}/inventory/channels/{pool}.json'))['videos']:
        ups[v['id']] = {**v, 'provider': prov}

def subj_of(title):
    """subject votes by vocab; returns ordered subjects"""
    votes = []
    if BIO.search(title): votes.append('bio')
    if CHEM.search(title): votes.append('chem')
    if PHYS.search(title): votes.append('phys')
    return votes

pool, skipped = [], collections.Counter()
for vid, v in sorted(ups.items()):
    if vid in corpus:
        continue
    t = v['title']; s = t.lower(); prov = v['provider']
    if SEWAGE.search(s):
        skipped['sewage (promo / exam-technique / non-science channel content)'] += 1
        continue
    if prov == 'fsl-uploads' or prov == 'freesciencelessons':
        m = re.search(r'gcse (biology|chemistry|physics)', s)
        al = re.search(r'a[- ]?level (biology|chemistry|physics)', s)
        if m:
            subj = {'biology': 'bio', 'chemistry': 'chem', 'physics': 'phys'}[m.group(1)]
            if 'gcse' in s: level = 'gcse'
        elif al:
            subj = {'biology': 'bio', 'chemistry': 'chem', 'physics': 'phys'}[al.group(1)]
            level = 'a-level'
        else:
            vs = subj_of(t)
            if not vs:
                skipped['misc (no subject vocabulary)'] += 1
                continue
            subj = vs[0]; level = 'gcse' if re.search(r'gcse', s) else ('a-level' if re.search(r'a[- ]?level', s) else None)
        if subj == 'bio': cands = COURSES['bio']
        elif subj == 'chem': cands = COURSES['chem']
        else: cands = COURSES['phys']
        if level == 'gcse':
            cands = [c for c in cands if 'igcse' in c or c.startswith('cie-igcse')]
        elif level == 'a-level':
            cands = [c for c in cands if 'a-level' in c or c.startswith('ial')]
        scored = best_course(t, cands)
        s0, c0 = scored[0]
        if s0 <= 0:
            skipped['no spine overlap (no honest binding candidate)'] += 1
            continue
        route = c0; levelTag = level or ('a-level' if 'a-level' in c0 or c0.startswith('ial') else 'gcse')
    elif prov == 'amoeba-sisters':
        vs = subj_of(t)
        if not vs or vs[0] != 'bio':
            skipped['misc (no biology vocabulary)'] += 1
            continue
        scored = best_course(t, COURSES['bio'])
        s0, c0 = scored[0]
        if s0 <= 0:
            skipped['no spine overlap (no honest binding candidate)'] += 1
            continue
        route = c0
        levelTag = 'a-level' if 'a-level' in c0 or c0.startswith('ial') else 'gcse'
    elif prov == 'malmesbury-education':
        vs = subj_of(t)
        if not vs:
            skipped['non-science channel content (languages / english lit / KS3 / DT / PE)'] += 1
            continue
        # prefer A-level courses for 'A-level' titles, igcse for GCSE
        level = 'a-level' if re.search(r'a[- ]?level', s) else ('gcse' if re.search(r'gcse', s) else None)
        subj = vs[0]
        cands = COURSES[subj]
        if level == 'a-level':
            cands = [c for c in cands if 'a-level' in c or c.startswith('ial')]
        elif level == 'gcse':
            cands = [c for c in cands if 'igcse' in c]
        scored = best_course(t, cands)
        s0, c0 = scored[0]
        if s0 <= 0:
            skipped['no spine overlap (no honest binding candidate)'] += 1
            continue
        route = c0
        levelTag = level or ('a-level' if 'a-level' in c0 or c0.startswith('ial') else 'gcse')
    elif prov == 'doodlescience':
        vs = subj_of(t)
        if not vs:
            skipped['misc (no subject vocabulary)'] += 1
            continue
        cands = COURSES[vs[0]]
        if re.search(r'gcse', s):
            cands = [c for c in cands if 'igcse' in c]
        elif re.search(r'a[- ]?level', s):
            cands = [c for c in cands if 'a-level' in c or c.startswith('ial')]
        scored = best_course(t, cands)
        s0, c0 = scored[0]
        if s0 <= 0:
            skipped['no spine overlap (no honest binding candidate)'] += 1
            continue
        route = c0
        levelTag = 'a-level' if ('a-level' in c0 or c0.startswith('ial')) else 'gcse'
    else:
        continue
    pool.append({'id': vid, 'title': t, 'duration': v.get('duration'), 'course': route,
                 'provider': {'freesciencelessons': 'freesciencelessons', 'amoeba-sisters': 'amoeba-sisters',
                              'malmesbury-education': 'malmesbury-education', 'doodlescience': 'doodlescience'}[prov],
                 'levelTag': levelTag,
                 'watchUrl': f'https://www.youtube.com/watch?v={vid}'})

json.dump(pool, open(f'{OUT}/target-pool.json', 'w'), indent=1)
print(f'four pools public: {len(ups)} | in corpus (any course): {len(corpus & set(ups))} | unmapped: {len(ups) - len(corpus & set(ups))}')
print(f'routed: {len(pool)} | skipped: {dict(skipped)}')
print('routed per course:', dict(collections.Counter(p['course'] for p in pool)))
print('routed per provider:', dict(collections.Counter(p['provider'] for p in pool)))
