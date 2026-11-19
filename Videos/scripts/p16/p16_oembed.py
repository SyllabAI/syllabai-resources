#!/usr/bin/env python3
"""P16 identity sweep: oEmbed over every video entering the lit-21 draft,
author_name must equal the channel of record (UC ids from the committed
inventories' channelId fields). Checkpointed, resumable; thumbnail-liveness
fallback (P2D law) on oEmbed failure."""
import json, urllib.request, urllib.parse, os, html, time

WORK = '/home/z/my-project/work/p16'
RES = '/home/z/my-project/repos/syllabai-resources'
OUT = f'{WORK}/oembed-p16.json'
CKPT = f'{WORK}/oembed-p16.ckpt.json'

UC, EXPECTED, PROV = {}, {}, {}
for slug in ("claires-notes", "igcsesuccess"):
    d = json.load(open(f'{RES}/Videos/inventory/channels/{slug}-uploads.json'))
    UC[slug] = d.get('channelId')
    EXPECTED[slug] = html.unescape(d.get('channel') or slug)
    for v in d['videos']:
        PROV.setdefault(v['id'], slug)

keeps = json.load(open(f'{WORK}/keeps.json'))
targets = {k['video']: (k['title'], k['provider']) for k in keeps}
print('videos to verify:', len(targets), '| expected authors:', EXPECTED, flush=True)

done = {}
if os.path.exists(CKPT):
    done = json.load(open(CKPT))
    print('resuming with', len(done), 'already done', flush=True)

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "syllabai-p16-identity/1"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())

def oembed(vid):
    q = urllib.parse.quote(f"https://www.youtube.com/watch?v={vid}", safe="")
    u = f"https://www.youtube.com/oembed?url={q}&format=json"
    try:
        d = fetch(u)
        return {"ok": True, "author": d.get("author_name"), "author_url": d.get("author_url"),
                "title": d.get("title"), "method": "oembed"}
    except Exception as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}"}

todo = [k for k in targets if k not in done]
for i, vid in enumerate(todo):
    title, prov = targets[vid]
    r = oembed(vid)
    if r.get("ok"):
        exp = EXPECTED[prov]
        r["match"] = (html.unescape(r.get("author") or "") == exp)
        r["uc"] = UC.get(prov)
        if not r["match"]:
            r["fallback"] = None
    else:
        # thumbnail-liveness fallback (P2D law) — identity via UC id of record
        try:
            tu = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
            req = urllib.request.Request(tu, method="HEAD", headers={"User-Agent": "syllabai-p16-identity/1"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                r["thumbStatus"] = resp.status
        except Exception as e2:
            r["thumbStatus"] = f"{type(e2).__name__}"
        r["match"] = False
    done[vid] = r
    if (i + 1) % 25 == 0 or i == len(todo) - 1:
        json.dump(done, open(CKPT, "w"))
        print(f"  {i+1}/{len(todo)} done", flush=True)
    time.sleep(0.15)

json.dump(done, open(OUT, "w"))
json.dump(done, open(CKPT, "w"))
ok = [v for v in done.values() if v.get("match")]
bad = [v for v in done.items() if not v[1].get("match")]
fb = [v for v in done.items() if v[1].get("fallback") is not None or ("thumbStatus" in v[1] and v[1].get("thumbStatus") == 200)]
print(f"oEmbed sweep: {len(ok)}/{len(done)} author==channel-of-record; mismatches/failures: {len(bad)}")
for vid, r in bad[:10]:
    print('  BAD', vid, targets[vid][1], r.get('author') or r.get('error'), r.get('thumbStatus'))
