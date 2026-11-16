#!/usr/bin/env python3
"""P13 identity sweep: oEmbed over every video entering a P13 draft
(Tier B anchors + Tier A kept rows), author_url channel must equal the
channel of record. Checkpointed, resumable; thumbnail-liveness fallback (P2D law)."""
import json, urllib.request, urllib.parse, concurrent.futures, os

OUT = '/home/z/my-project/work/p13/oembed-p13.json'
CKPT = '/home/z/my-project/work/p13/oembed-p13.ckpt.json'
EXPECTED = {
    'alt-academy-main': 'alt academy',
    'alt-academy-chemistry': 'a level chemistry | alt academy',
    'alt-academy-economics': 'a level economics | alt academy',
    'alt-academy-maths': 'a level maths | alt academy',
    'alt-academy-physics': 'a level physics | alt academy',
    'alt-academy-biology': 'a level biology | alt academy',
    'alt-academy-psychology': 'a level psychology | alt academy',
    'alt-academy-accounting': 'a level accounting | alt academy',
}
UC = {
    'alt-academy-main': 'UCTgPevMIji1ZyP4IPhmwDsQ',
    'alt-academy-chemistry': 'UC-d3d-0oU9iYsj-6pvpJX5g',
    'alt-academy-economics': 'UC1Ar1Z9I26a_R-lZ0qzW9UQ',
    'alt-academy-maths': 'UCUeuU0fIwU8jHC5jdsr-wtg',
    'alt-academy-physics': 'UCwLO28CtT1ewcP5wIhFF5bA',
    'alt-academy-biology': 'UCEVYEqcUrnc5lJyO1zALMDw',
    'alt-academy-psychology': 'UCa3bmJx38QfiGWT2pCCOWNQ',
    'alt-academy-accounting': 'UCIjJYpNevYcLZBxtfa8u5NQ',
}

WORK = '/home/z/my-project/work/p13'
poolB = json.load(open(f'{WORK}/tier-b.json'))
J = json.load(open(f'{WORK}/judgment.json'))

targets = {}
for p in poolB:
    targets[p['id']] = (p['title'], 'alt-academy-family')  # provider resolved below
# resolve provider per video from the pool extracts
PROV = {}
for slug in EXPECTED:
    try:
        for v in json.load(open(f'{WORK}/inl-{slug}.json')):
            PROV.setdefault(v['id'], slug)
    except FileNotFoundError:
        pass
targets = {}
for p in poolB:
    targets[p['id']] = (p['title'], PROV.get(p['id'], 'alt-academy-main'))
for c, vs in J.items():
    for v in vs:
        if v['action'] == 'keep':
            targets.setdefault(v['id'], (v.get('reason', v['id']), PROV.get(v['id'], 'alt-academy-main')))
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
    if vid not in targets:
        continue
    t, prov = targets[vid]
    out[vid] = {'title': t, 'provider': prov, **res}
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)

bad = []
for vid, res in out.items():
    t, prov = targets[vid]
    exp = EXPECTED[prov]
    uc = UC[prov]
    if not res['ok']:
        bad.append((vid, prov, 'DEAD ' + res.get('err', '')[:60]))
    elif res['method'] == 'oembed':
        au = (res.get('authorUrl') or '')
        auc = (au.split('/channel/')[1].split('/')[0] if '/channel/' in au else None)
        if auc is not None:
            if auc != uc:
                bad.append((vid, prov, f"CHANNEL {auc} != {uc} (author {res.get('author')!r})"))
        elif (res.get('author') or '').strip().lower().rstrip('.') != exp.strip().lower().rstrip('.'):
            bad.append((vid, prov, f"AUTHOR {res.get('author')!r} != {exp!r}"))
print(f'verified: {len(out)} | bad: {len(bad)}')
for b in bad[:20]:
    print('  BAD', b)
