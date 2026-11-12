#!/usr/bin/env python3
"""P5 step 2: oEmbed identity sweep over the target pool (author must be Cognito)."""
import json, urllib.request, urllib.parse, concurrent.futures

POOL = '/home/z/my-project/work/p5/target-pool.json'
OUT = '/home/z/my-project/work/p5/oembed-p5.json'

pool = json.load(open(POOL))

def oembed(vid):
    q = urllib.parse.quote(f"https://www.youtube.com/watch?v={vid}", safe="")
    u = f"https://www.youtube.com/oembed?url={q}&format=json"
    try:
        with urllib.request.urlopen(u, timeout=20) as r:
            d = json.loads(r.read())
        return vid, {"ok": True, "title": d.get("title"), "author": d.get("author_name"),
                     "authorUrl": d.get("author_url")}
    except Exception as e:
        return vid, {"ok": False, "err": f"{type(e).__name__}: {e}"}

with concurrent.futures.ThreadPoolExecutor(6) as ex:
    res = dict(ex.map(lambda p: oembed(p['id']), pool))

out = {p['id']: {'course': p['course'], **res[p['id']]} for p in pool}
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)
ok = [k for k, v in out.items() if v['ok']]
author_ok = [k for k in ok if (out[k]['author'] or '').lower() == 'cognito']
mismatch = [k for k in ok if (out[k]['author'] or '').lower() != 'cognito']
print(f"oEmbed: {len(ok)}/{len(pool)} live | author==Cognito: {len(author_ok)} | author mismatch: {len(mismatch)}")
for k in mismatch[:10]:
    print('  MISMATCH', k, out[k]['author'], '::', (out[k]['title'] or '')[:60])
dead = [k for k, v in out.items() if not v['ok']]
for k in dead[:10]:
    print('  DEAD', k, out[k]['err'][:80])
