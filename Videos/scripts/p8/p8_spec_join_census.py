#!/usr/bin/env python3
"""Independent spec-join census: every mapping spec code in every hub video-map
course must resolve against that course's spine via the full-string universe
(spine titles+codes as one string universe, exact code membership or
token-bounded containment). The P7-era census law."""
import json, re, os, sys
HUB='/home/z/my-project/repos/syllabai-v2-fresh'
vd=f'{HUB}/apps/hub/content/video-map'
courses=sorted(f[:-5] for f in os.listdir(vd) if f.endswith('.json') and f!='registry.json')
total_rows=0; violations=[]; covered=0
for c in courses:
    cur=json.load(open(f'{HUB}/apps/hub/content/{c}/curriculum.json'))
    spec={n['code'] for n in cur['nodes'] if n.get('family')=='SPEC_POINT'}
    # full-string universe: any spine title/code string
    universe=' \n '.join([(n.get('code') or '')+' '+(n.get('title') or '') for n in cur['nodes']])
    vm=json.load(open(f'{vd}/{c}.json'))
    for m in vm.get('mappings') or []:
        total_rows+=1
        for s in m.get('specs') or []:
            if s in spec: covered+=1; continue
            # token-bounded containment of the code string inside the universe
            if re.search(r'(?<![0-9A-Za-z])'+re.escape(s)+r'(?![0-9A-Za-z])', universe): covered+=1; continue
            violations.append((c, m.get('video'), s))
print(f'courses={len(courses)} mapping rows={total_rows} spec refs={covered} violations={len(violations)}')
for v in violations[:12]: print('VIOLATION:', v)
sys.exit(1 if violations else 0)
