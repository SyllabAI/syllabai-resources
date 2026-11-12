#!/usr/bin/env python3
"""Tighten P8 candidate rows before agent judgment (the P7 pre-pass shape)."""
import json, re, os
RES='/home/z/my-project/repos/syllabai-resources'
from collections import defaultdict

HUB='/home/z/my-project/repos/syllabai-v2-fresh'
TRIO=['cie-a-level-physics-25','cie-igcse-physics-23','igcse-physics-19']
rows=json.load(open('/tmp/p8_candidate_rows.json'))

# rebuild df per course for rarity scoring
STOP=set('the a an of and or to in on for with from by is are be as at into onto vs using use when between during'.split())
def toks(s): return [t for t in re.findall(r"[a-z0-9]+", s.lower()) if t not in STOP and len(t)>2]
dfs={}
for c in TRIO:
    cur=json.load(open(f'{HUB}/apps/hub/content/{c}/curriculum.json'))
    specs=[n for n in cur['nodes'] if n.get('family')=='SPEC_POINT']
    df=defaultdict(int)
    for n in specs:
        for t in set(toks(n.get('title') or '')): df[t]+=1
    dfs[c]=df

def rar(c,tok): return dfs[c][tok]

# score each pair
scored=[]
for r in rows:
    c=r['course']
    d2=[t for t in r['tokens'] if rar(c,t)<=2]
    d3=[t for t in r['tokens'] if rar(c,t)<=3]
    strong = bool(d2) or len(d3)>=2
    score = (len(d2), len(d3))
    r['d2']=d2; r['d3']=d3; r['score']=score; r['strong']=strong
    if strong: scored.append(r)
print('strong rows:', len(scored))

# collapse per (video,course): keep best 2 specs by score
byvc=defaultdict(list)
for r in scored: byvc[(r['video'],r['course'])].append(r)
kept=[]
for k,rs in byvc.items():
    rs.sort(key=lambda r:(-len(r['d2']),-len(r['d3'])))
    kept.extend(rs[:2])
print('rows after per-(video,course) collapse:', len(kept))
vids=set(r['video'] for r in kept)
print('distinct videos:', len(vids))
specs=set((r['course'],r['spec']) for r in kept)
print('distinct (course,spec) targets:', len(specs))
json.dump(kept, open('/tmp/p8_tight_rows.json','w'), ensure_ascii=False, indent=1)

# ---- second tighten: pool-corpus token rarity ----
import json as _json
pool_df=defaultdict(int)
for f in ('amoeba-uploads.json','fsl-uploads.json','malmesbury-uploads.json','doodle-uploads.json','physicsonline-uploads.json'):
    d=_json.load(open(f'{RES}/Videos/inventory/channels/{f}'))
    for v in d['videos']:
        for t in set(toks(v['title'])): pool_df[t]+=1
kept2=[r for r in kept if all(pool_df[t]<=8 for t in r['d2']) or all(pool_df[t]<=8 for t in r['d3'])]
print('rows after pool-rarity gate:', len(kept2))
vids2=set(r['video'] for r in kept2); specs2=set((r['course'],r['spec']) for r in kept2)
print('distinct videos:', len(vids2), 'distinct targets:', len(specs2))
_json.dump(kept2, open('/tmp/p8_judgment_rows.json','w'), ensure_ascii=False, indent=1)
# compact judgment TSV grouped by video
byv=defaultdict(list)
for r in kept2: byv[r['video']].append(r)
out=[]
for vid,rs in byv.items():
    out.append({'video':vid,'channel':rs[0]['channel'],'title':rs[0]['title'],
                'prior':rs[0]['prior'],
                'binds':[{'course':r['course'],'spec':r['spec'],'specTitle':r['specTitle'],'tokens':sorted(set(r['d2']+r['d3']))} for r in rs]})
out.sort(key=lambda x:(x['channel'],x['title']))
_json.dump(out, open('/tmp/p8_judgment_input.json','w'), ensure_ascii=False, indent=1)
print('judgment videos:', len(out))
