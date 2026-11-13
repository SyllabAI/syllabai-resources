#!/usr/bin/env python3
"""P10 identity sweep: oEmbed over every video entering a P10 draft
(Tier B anchors + Tier A kept/rebind rows), author must be the channel of
record. Checkpointed, resumable; thumbnail-liveness fallback (P2D law)."""
import json, urllib.request, urllib.parse, concurrent.futures, os

OUT = '/home/z/my-project/work/p10/oembed-p10.json'
CKPT = '/home/z/my-project/work/p10/oembed-p10.ckpt.json'
EXPECTED = {
    'mrarnoldsmaths': 'mrarnoldsmaths',
    'mathsdeity': 'maths deity',
}

poolB = json.load(open('/home/z/my-project/work/p10/tier-b.json'))
J = json.load(open('/home/z/my-project/work/p10/judgment.json'))
tierA = json.load(open('/home/z/my-project/work/p10/tier-a.json'))
ta_by_id = {p['id']: p for p in tierA}

targets = {}
for p in poolB:
    targets[p['id']] = (p['title'], p['provider'])
for c, vs in J.items():
    for v in vs:
        if v['action'] in ('keep', 'rebind'):
            src = ta_by_id.get(v['id'])
            if src:
                targets[v['id']] = (v['title'], src['provider'])
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
        tu = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
        try:
            with urllib.request.urlopen(tu, timeout=20) as r:
                ok = r.status == 200 and r.headers.get('content-type', '').startswith('image')
            return vid, {"ok": ok, "method": "thumb-fallback",
                         "err": f"oembed {type(e).__name__}" + ("" if ok else " + thumb dead")}
        except Exception as e2:
            return vid, {"ok": False, "method": "thumb-fallback",
                         "err": f"oembed {type(e).__name__}; thumb {type(e2).__name__}"}

batch = 400
todo_now = todo[:]
for i in range(0, len(todo_now), batch):
    chunk = todo_now[i:i + batch]
    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        for vid, res in ex.map(oembed, chunk):
            done[vid] = res
    json.dump(done, open(CKPT, 'w'))
    print(f'  {min(i + batch, len(todo_now))}/{len(todo_now)}', flush=True)

json.dump(done, open(CKPT, 'w'))
out = {}
for vid, res in done.items():
    t, prov = targets[vid]
    out[vid] = {'title': t, 'provider': prov, **res}
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)

bad = []
for vid, res in out.items():
    t, prov = targets[vid]
    exp = EXPECTED[prov]
    if not res['ok']:
        bad.append((vid, prov, 'DEAD ' + res.get('err', '')[:60]))
    elif res['method'] == 'oembed' and (res.get('author') or '').strip().lower() != exp:
        bad.append((vid, prov, f"AUTHOR {res.get('author')!r} != {exp!r}"))
print(f'verified: {len(out)} | bad: {len(bad)}')
for b in bad[:15]:
    print('  BAD', b)
