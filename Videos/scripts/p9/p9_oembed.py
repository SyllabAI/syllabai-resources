#!/usr/bin/env python3
"""P9 identity sweep: oEmbed over every video that will enter a P9 draft
(Tier B anchors + Tier A kept/rebind rows), author must be the channel of
record. Checkpointed — resumable. Thumb-liveness fallback for oEmbed failures
(the P2D identity law) via the thumbnail endpoint."""
import json, urllib.request, urllib.parse, concurrent.futures, os, time, re

OUT = '/home/z/my-project/work/p9/oembed-p9.json'
CKPT = '/home/z/my-project/work/p9/oembed-p9.ckpt.json'
EXPECTED = "mr hassaan's maths channel"

poolB = json.load(open('/home/z/my-project/work/p9/tier-b.json'))
J = json.load(open('/home/z/my-project/work/p9/judgment.json'))
tierA = json.load(open('/home/z/my-project/work/p9/tier-a.json'))
ta_by_id = {p['id']: p for p in tierA}

targets = {}
for p in poolB:
    targets[p['id']] = p['title']
for c, vs in J.items():
    for v in vs:
        if v['action'] in ('keep', 'rebind'):
            targets[v['id']] = v['title']
print('unique videos to verify:', len(targets))

done = {}
if os.path.exists(CKPT):
    done = json.load(open(CKPT))
    print('resuming with', len(done), 'already done')

todo = [k for k in targets if k not in done]

def oembed(vid):
    q = urllib.parse.quote(f"https://www.youtube.com/watch?v={vid}", safe="")
    u = f"https://www.youtube.com/oembed?url={q}&format=json"
    try:
        with urllib.request.urlopen(u, timeout=20) as r:
            d = json.loads(r.read())
        return vid, {"ok": True, "method": "oembed", "title": d.get("title"),
                     "author": d.get("author_name"), "authorUrl": d.get("author_url")}
    except Exception as e:
        # thumb fallback (P2D law): thumbnail liveness proves the video exists
        tu = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
        try:
            with urllib.request.urlopen(tu, timeout=20) as r:
                ok = r.status == 200 and r.headers.get('content-type', '').startswith('image')
            return vid, {"ok": ok, "method": "thumb-fallback",
                         "err": f"oembed {type(e).__name__}" + ("" if ok else " + thumb dead")}
        except Exception as e2:
            return vid, {"ok": False, "method": "thumb-fallback",
                         "err": f"oembed {type(e).__name__}; thumb {type(e2).__name__}"}

def flush():
    json.dump(done, open(CKPT, 'w'))

import sys
batch = 400
for i in range(0, len(todo), batch):
    chunk = todo[i:i + batch]
    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        for vid, res in ex.map(lambda k: oembed(k), chunk):
            done[vid] = res
    flush()
    print(f'  {min(i + batch, len(todo))}/{len(todo)}', flush=True)

json.dump(done, open(CKPT, 'w'))
out = {}
for vid, res in done.items():
    out[vid] = {'title': targets[vid], **res}
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)

ok = [k for k, v in out.items() if v['ok']]
author_ok = [k for k in ok if (out[k].get('author') or '').strip().lower() == EXPECTED]
mismatch = [k for k in ok if (out[k].get('author') or '').strip().lower() != EXPECTED and out[k]['method'] == 'oembed']
fallback_ok = [k for k in ok if out[k]['method'] == 'thumb-fallback']
dead = [k for k, v in out.items() if not v['ok']]
print(f"verified: {len(ok)}/{len(out)} | oembed author==expected: {len(author_ok)} | thumb-fallback: {len(fallback_ok)} | author mismatch: {len(mismatch)} | dead: {len(dead)}")
for k in mismatch[:10]:
    print('  MISMATCH', k, repr(out[k].get('author')), '::', (out[k].get('title') or '')[:60])
for k in dead[:10]:
    print('  DEAD', k, out[k].get('err', '')[:80])
