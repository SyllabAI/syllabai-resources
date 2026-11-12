#!/usr/bin/env python3
"""P8 lane: physics-trio re-adjudication candidates.
For each trio empty SPEC_POINT, find unmapped pool videos whose title shares a distinctive
token (in-course df<=3). Cross-reference P6/P7 verdict ledgers for prior drops."""
import json, re, os, sys
from collections import defaultdict

RES='/home/z/my-project/repos/syllabai-resources'
HUB='/home/z/my-project/repos/syllabai-v2-fresh'
TRIO=['cie-a-level-physics-25','cie-igcse-physics-23','igcse-physics-19']
POOLS={'amoeba-uploads.json':'Amoeba Sisters','fsl-uploads.json':'freesciencelessons',
       'malmesbury-uploads.json':'Malmesbury Education','doodle-uploads.json':'DoodleScience',
       'physicsonline-uploads.json':'PhysicsOnline'}
STOP=set('the a an of and or to in on for with from by is are be as at into onto vs using use when between during'.split())
DRILL=re.compile(r"practise|practice question|exam solution|past paper|test yourself|revision lesson|walkthrough|mark scheme", re.I)

mapped_vids=set()
vd=f'{HUB}/apps/hub/content/video-map'
for f in os.listdir(vd):
    if f.endswith('.json'):
        d=json.load(open(f'{vd}/{f}'))
        for v in d.get('videos') or []:
            vid=v.get('id') or v.get('videoId')
            if vid: mapped_vids.add(vid)

pool={}
for f,ch in POOLS.items():
    d=json.load(open(f'{RES}/Videos/inventory/channels/{f}'))
    for v in d['videos']:
        pool[v['id']]={'title':v['title'],'channel':ch}
unmapped={k:v for k,v in pool.items() if k not in mapped_vids}

# prior trio verdict drops (P6+P7): video -> set(course)
prior=defaultdict(set)
for c in TRIO:
    for suf in ('p6','p7'):
        p=f'{RES}/Videos/drafts/{c}/owner-review-verdicts.{suf}.json'
        if os.path.exists(p):
            d=json.load(open(p))
            for r in d.get('rejects') or []:
                prior[r['video']].add(f'{c}:{suf}')

def toks(s): return [t for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP and len(t)>2]

rows=[]; stats={}
for c in TRIO:
    cur=json.load(open(f'{HUB}/apps/hub/content/{c}/curriculum.json'))
    specs=[n for n in cur['nodes'] if n.get('family')=='SPEC_POINT']
    vm=json.load(open(f'{HUB}/apps/hub/content/video-map/{c}.json'))
    mapped=set()
    for m in vm['mappings']:
        for s in m.get('specs') or []: mapped.add(s)
    empty={n['code']:n for n in specs if n['code'] not in mapped}
    df=defaultdict(int)
    for n in specs:
        for t in set(toks(n.get('title') or '')): df[t]+=1
    nrow=0
    for vid,meta in unmapped.items():
        if DRILL.search(meta['title']): continue
        tt=set(toks(meta['title']))
        for code,n in empty.items():
            st=set(toks(n.get('title') or ''))
            dist={t for t in (tt & st) if df[t]<=3}
            if not dist: continue
            # score = number of distinctive shared tokens; require >=1, weight by rarity
            rows.append({'video':vid,'channel':meta['channel'],'title':meta['title'][:110],
                         'course':c,'spec':code,'specTitle':(n.get('title') or '')[:130],
                         'tokens':sorted(dist),'prior':sorted(prior.get(vid,[]))})
            nrow+=1
    stats[c]=nrow
print('candidate pairs per course:', stats, file=sys.stderr)
by_spec=defaultdict(set)
for r in rows: by_spec[(r['course'],r['spec'])].add(r['video'])
print('distinct empty specs with candidates:', len(by_spec), file=sys.stderr)
seen=set(); dedup=[]
for r in rows:
    k=(r['video'],r['course'],r['spec'])
    if k in seen: continue
    seen.add(k); dedup.append(r)
print('candidate rows:', len(dedup), file=sys.stderr)
json.dump(dedup, open('/tmp/p8_candidate_rows.json','w'), ensure_ascii=False, indent=1)
# compact per-video grouping for judgment
byvid=defaultdict(list)
for r in dedup: byvid[r['video']].append(r)
out=[]
for vid,rs in byvid.items():
    out.append({'video':vid,'channel':rs[0]['channel'],'title':rs[0]['title'],
                'prior':rs[0]['prior'],'binds':[{'course':r['course'],'spec':r['spec'],'specTitle':r['specTitle'],'tokens':r['tokens']} for r in rs]})
out.sort(key=lambda x:(-len(x['binds']),x['channel']))
json.dump(out, open('/tmp/p8_judgment_input.json','w'), ensure_ascii=False, indent=1)
print('distinct videos to judge:', len(out), file=sys.stderr)
