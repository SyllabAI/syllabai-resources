#!/usr/bin/env python3
"""p7_pool_census.py — overlap census of the remaining channel pools vs the
current hub video-map corpus (post P2B/P2C/P2D/P4/P5/P6)."""
import json, glob, collections, re

HUB = '/home/z/my-project/repos/syllabai-v2-fresh/apps/hub/content/video-map'
RES = '/home/z/my-project/repos/syllabai-resources/Videos/inventory/channels'
POOLS = ['amoeba-uploads', 'fsl-uploads', 'malmesbury-uploads', 'doodle-uploads']

# 1. mapped video IDs -> set of courses (from hub mappings)
mapped = collections.defaultdict(set)
prov_by_course = collections.defaultdict(collections.Counter)
for f in sorted(glob.glob(f'{HUB}/*.json')):
    if f.endswith('registry.json'): continue
    d = json.load(open(f))
    course = d['course']
    for v in d.get('videos', []):
        if v.get('provider'): prov_by_course[course][v['provider']] += 1
    for m in d.get('mappings', []):
        mapped[m['video']].add(course)

print(f'corpus: {sum(len(s) for s in mapped.values())} rows over {len(mapped)} distinct video ids')
print()

# 2. per-pool census
summary = {}
for pool in POOLS:
    d = json.load(open(f'{RES}/{pool}.json'))
    vids = d['videos']
    ids = [v['id'] for v in vids]
    mapped_ids = [i for i in ids if i in mapped]
    unmapped_ids = [i for i in ids if i not in mapped]
    by_course = collections.Counter()
    for i in mapped_ids:
        for c in mapped[i]: by_course[c] += 1
    summary[pool] = (len(ids), len(mapped_ids), len(unmapped_ids), by_course, unmapped_ids, vids)
    print(f'{pool}: {len(ids)} uploads | mapped={len(mapped_ids)} | unmapped={len(unmapped_ids)}')
    for c, n in by_course.most_common(8):
        print(f'    {c}: {n}')

# 3. provider spellings present in the corpus (for later provider-field normalization)
print()
all_prov = collections.Counter()
for c, ctr in prov_by_course.items():
    for p, n in ctr.items(): all_prov[p] += n
print('corpus provider spellings:', dict(all_prov))

# 4. title-shape histogram of the unmapped remainder (routing prior)
def bucket(title):
    t = title.lower()
    if re.search(r'\ba[- ]?level\b|\ba2\b|\bas level\b', t): return 'a-level'
    if re.search(r'\bgcse\b', t): return 'gcse'
    if re.search(r'\bks3\b', t): return 'ks3'
    return 'unmarked'
print()
for pool in POOLS:
    _, _, _, _, unmapped_ids, vids = summary[pool]
    byid = {v['id']: v['title'] for v in vids}
    hist = collections.Counter(bucket(byid[i]) for i in unmapped_ids)
    print(f'{pool} unmapped title-shape: {dict(hist)}')
    # sample 5 unmapped titles
    for i in unmapped_ids[:5]:
        print(f'    e.g. {byid[i][:80]}')
