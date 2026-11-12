#!/usr/bin/env python3
"""P7 step 5: identity sweep over the judged pool. oEmbed author check with
expected authors per provider; oEmbed-401 videos (freesciencelessons disables
embedding on most A-level videos) fall back to i.ytimg.com thumbnail liveness
+ the first-party yt-dlp uploads-playlist enumeration (identityMethod:
'thumb-fallback' per video, the P2D pattern)."""
import json, urllib.request, urllib.parse, concurrent.futures, os

OUT = '/home/z/my-project/work/p7'
POOL = f'{OUT}/target-pool.json'
JUDG = f'{OUT}/judgment-{{course}}.json'
EXPECT = {'freesciencelessons': 'freesciencelessons', 'amoeba-sisters': 'amoeba sisters',
          'malmesbury-education': 'malmesbury education', 'doodlescience': 'doodlescience'}

pool = {p['id']: p for p in json.load(open(POOL))}
keep_ids = set()
for f in os.listdir(OUT):
    if f.startswith('judgment-'):
        d = json.load(open(f'{OUT}/{f}'))
        for k, v in d['decisions'].items():
            if v[0] in ('keep', 'rebind'):
                keep_ids.add(d['decisions'][k] and list(json.load(open(f'{OUT}/adjudication-{d["course"]}.json'))['rows'])[int(k)]['video'])

# rebuild keep_ids properly from adjudication rows
keep_ids = set()
for f in os.listdir(OUT):
    if f.startswith('judgment-'):
        course = f[len('judgment-'):-len('.json')]
        d = json.load(open(f'{OUT}/{f}'))
        rows = json.load(open(f'{OUT}/adjudication-{course}.json'))['rows']
        for k, v in d['decisions'].items():
            if v[0] in ('keep', 'rebind'):
                keep_ids.add(rows[int(k)]['video'])

targets = [pool[i] for i in keep_ids]
print(f'identity sweep over {len(targets)} judged-keep videos')

def oembed(vid):
    q = urllib.parse.quote(f"https://www.youtube.com/watch?v={vid}", safe="")
    u = f"https://www.youtube.com/oembed?url={q}&format=json"
    try:
        with urllib.request.urlopen(u, timeout=20) as r:
            d = json.loads(r.read())
        return vid, {"oembed": True, "title": d.get("title"), "author": d.get("author_name")}
    except urllib.error.HTTPError as e:
        return vid, {"oembed": False, "status": e.code}
    except Exception as e:
        return vid, {"oembed": False, "status": f"{type(e).__name__}"}

def thumb_live(vid):
    u = f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"
    try:
        req = urllib.request.Request(u, method='HEAD')
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status == 200
    except Exception:
        return False

with concurrent.futures.ThreadPoolExecutor(8) as ex:
    res = dict(ex.map(lambda p: oembed(p['id']), targets))

out = {}
for p in targets:
    vid = p['id']
    r = res[vid]
    exp = EXPECT[p['provider']]
    if r['oembed']:
        author_ok = (r['author'] or '').lower() == exp
        out[vid] = {'ok': author_ok, 'identityMethod': 'oembed', 'author': r['author'],
                    'title': r['title'], 'expected': exp}
    else:
        # thumb fallback (P2D law): thumbnail liveness + uploads-playlist enumeration membership
        live = thumb_live(vid)
        in_playlist = vid in {v['id'] for v in json.load(open(
            f"/home/z/my-project/repos/syllabai-resources/Videos/inventory/channels/{p['provider'] and {'freesciencelessons':'fsl-uploads','amoeba-sisters':'amoeba-uploads','malmesbury-education':'malmesbury-uploads','doodlescience':'doodle-uploads'}[p['provider']]}.json"))['videos']}
        out[vid] = {'ok': live and in_playlist, 'identityMethod': 'thumb-fallback',
                    'author': f'{p["provider"]} (uploads-playlist + thumbnail liveness)',
                    'title': p['title'], 'expected': exp, 'thumbLive': live, 'inPlaylist': in_playlist}

json.dump(out, open(f'{OUT}/oembed-p7.json', 'w'), indent=1, ensure_ascii=False)
ok = [k for k, v in out.items() if v['ok']]
bad = [k for k, v in out.items() if not v['ok']]
thumb = [k for k, v in out.items() if v['identityMethod'] == 'thumb-fallback']
print(f"identity: {len(ok)}/{len(out)} verified (oEmbed {len(out)-len(thumb)}, thumb-fallback {len(thumb)})")
for k in bad[:15]:
    print('  FAIL', k, out[k].get('expected'), out[k].get('status') or out[k].get('thumbLive'), out[k].get('inPlaylist'), out[k].get('title', '')[:50])
mism = [k for k, v in out.items() if v['ok'] and v['identityMethod'] == 'oembed' and (v['author'] or '').lower() != v['expected']]
print('author mismatches (ok but different):', len(mism))
for k in mism[:8]:
    print('  MISMATCH', k, repr(out[k]['author']), out[k]['title'][:50])
