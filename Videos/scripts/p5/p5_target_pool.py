#!/usr/bin/env python3
"""P5 step 1: build the target pool — unmapped Cognito uploads that can honestly
route to a SyllabAI parent course. Excludes KS3 / psychology / announcements
(no honest spine target) and the already-mapped set."""
import json, re, os

RES = '/home/z/my-project/repos/syllabai-resources/Videos'
HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub'
OUT = '/home/z/my-project/work/p5'
os.makedirs(OUT, exist_ok=True)

ups = json.load(open(f'{RES}/inventory/channels/cognito-uploads.json'))['videos']

uni = set()
for f in os.listdir(f'{HUB}/content/video-map'):
    if not f.endswith('.json') or f == 'registry.json':
        continue
    d = json.load(open(f'{HUB}/content/video-map/{f}'))
    src = (d.get('source') or {}).get('provider') or ''
    for v in d.get('videos', []):
        p = (v.get('provider') or '')
        if p.startswith('cognito') or 'cognito' in ((v.get('lessonUrl') or '') + (v.get('watchUrl') or '')) \
           or (src == 'cognito' and 'provider' not in v):
            uni.add(v['id'])

ROUTE = [
    # (course, title regex on the LOWERED title)
    ('cie-a-level-biology-25', r'\ba[ -]?level\b.*(?:bio|photosynthes|respirat|enzyme|dna|genetic|mitosis|osmosis|neuron|heart|hormone|ecosystem|immun|pathogen|homeostasis|kidney|nerve|synapse|chloroplast|phosphoryl|krebs|glycolysis|punnett|meiosis|transpiration|tropism|statolith|abiotic|quadrat|spearman|chi|t-test|student|biodivers|classification|selective|extinction| Succession|Plotting|Graphs?)'),
    ('cie-igcse-biology-23', r'GCSE Biology|microscope|binary fission'),
    ('cie-igcse-chemistry-23', r'GCSE Chemistry|electrolysis|atoms & ions'),
    ('cie-igcse-physics-23', r'GCSE Physics|light years|universe'),
    ('igcse-maths-a-18-higher', r'GCSE Maths'),
]
KS3 = re.compile(r'\bks3\b', re.I)

pool, skipped = [], {'ks3': 0, 'psych': 0, 'announcement': 0, 'no-route': 0}
for v in ups:
    if v['id'] in uni:
        continue
    t = v['title']
    if KS3.search(t):
        skipped['ks3'] += 1
        continue
    if re.search(r'psycholog', t, re.I):
        skipped['psych'] += 1
        continue
    if re.search(r'cognito platform|our new gcse|a level launch|walk through|new gcse|exam qs launch|past paper and questions website', t, re.I):
        skipped['announcement'] += 1
        continue
    route = next((c for c, pat in ROUTE if re.search(pat, t, re.I)), None)
    if not route:
        skipped['no-route'] += 1
        continue
    pool.append({'id': v['id'], 'title': t, 'duration': v.get('duration'),
                 'course': route, 'provider': 'cognito',
                 'watchUrl': f'https://www.youtube.com/watch?v={v["id"]}',
                 'levelTag': 'a-level' if 'a-level' in route.lower() or route.startswith('cie-a') else 'gcse'})

json.dump(pool, open(f'{OUT}/target-pool.json', 'w'), indent=1)
import collections
print('target pool:', len(pool), '| skipped:', skipped)
print(dict(collections.Counter(p['course'] for p in pool)))
