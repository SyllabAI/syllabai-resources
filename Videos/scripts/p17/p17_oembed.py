#!/usr/bin/env python3
"""P14 identity sweep: oEmbed over every video entering a P14 draft
(Tier B anchors + Tier A kept rows), author_url channel must equal the
channel of record. Checkpointed, resumable; thumbnail-liveness fallback (P2D law).
UC ids come from the committed inventories' channelId fields (page-verified at filing)."""
import json, urllib.request, urllib.parse, concurrent.futures, os, html

WORK = '/home/z/my-project/work/p17'
RES = '/home/z/my-project/repos/syllabai-resources'
OUT = f'{WORK}/oembed-p17.json'
CKPT = f'{WORK}/oembed-p17.ckpt.json'

POOLS = ["chem-bio-math-revision-hub", "wilson-chong", "daniyal-aslam", "nevdoes-econ", "edexcel-science-channel", "gcse-ready", "adebayo-business-abt", "business-teacher-t", "aravinth-physics-maths", "a2z-physics", "biology-zhan-xuan", "mrimmoaee-ahmed", "click-ict", "state-of-math", "first-rate-tutors", "fundoo-tutor", "team-elevare", "mathman-oa-levels", "pinnacle-education", "dr-sarah-biology", "mr-quakers-teaches"]

UC, EXPECTED, PROV = {}, {}, {}
for slug in POOLS:
    d = json.load(open(f'{RES}/Videos/inventory/channels/{slug}-uploads.json'))
    UC[slug] = d.get('channelId')
    EXPECTED[slug] = (d.get('channel') or slug)
    for v in d['videos']:
        PROV.setdefault(v['id'], slug)

poolB = json.load(open(f'{WORK}/tier-b.json'))
J = json.load(open(f'{WORK}/judgment.json'))

targets = {}
for p in poolB:
    targets[p['id']] = (p['title'], PROV.get(p['id']))
for c, vs in J.items():
    for v in vs:
        if v['action'] == 'keep':
            targets.setdefault(v['id'], (v.get('reason', v['id']), PROV.get(v['id'])))
print('unique videos to verify:', len(targets), flush=True)

done = {}
if os.path.exists(CKPT):
    done = json.load(open(CKPT))
    print('resuming with', len(done), 'already done', flush=True)
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
def _nm(s):
    return html.unescape(s or '').strip().lower().rstrip('.').replace('\u2019', "'")
for vid, res in out.items():
    t, prov = targets[vid]
    exp = EXPECTED[prov]
    uc = UC[prov]
    if not res['ok']:
        bad.append((vid, prov, 'DEAD ' + res.get('err', '')[:60]))
    elif res['method'] == 'oembed':
        au = (res.get('authorUrl') or '')
        auc = (au.split('/channel/')[1].split('/')[0] if '/channel/' in au else None)
        if auc is not None and uc is not None:
            if auc != uc:
                bad.append((vid, prov, f"CHANNEL {auc} != {uc} (author {res.get('author')!r})"))
        elif _nm(res.get('author')) != _nm(exp):
            bad.append((vid, prov, f"AUTHOR {res.get('author')!r} != {exp!r}"))
print(f'verified: {len(out)} | bad: {len(bad)}')
for b in bad[:20]:
    print('  BAD', b)
