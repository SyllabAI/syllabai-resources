#!/usr/bin/env python3
"""p7_enumerate.py — fresh yt-dlp flat enumeration of the four remaining channel
pools (P6 law: re-enumerate before the lane). Writes/updates
Videos/inventory/channels/<pool>.json and prints the delta vs the cache."""
import json, subprocess, sys, os

RES = '/home/z/my-project/repos/syllabai-resources/Videos/inventory/channels'
CHANNELS = [
    ('amoeba-uploads',    'https://www.youtube.com/@AmoebaSisters/videos'),
    ('fsl-uploads',       'https://www.youtube.com/@Freesciencelessons/videos'),
    ('malmesbury-uploads','https://www.youtube.com/@MalmesburyEducation/videos'),
    ('doodle-uploads',    'https://www.youtube.com/@DoodleScience/videos'),
]

def enum(url):
    # structured print: id, duration, view_count, timestamp, title
    out = subprocess.run(
        ['yt-dlp', '--flat-playlist', '--print', '%(id)s\t%(duration)s\t%(view_count)s\t%(timestamp)s\t%(title)s', url],
        capture_output=True, text=True, timeout=480)
    vids = []
    for line in out.stdout.splitlines():
        parts = line.split('\t')
        if len(parts) < 5: continue
        vid, dur, views, ts, title = parts[:5]
        def num(x):
            try: return int(float(x))
            except (ValueError, TypeError): return None
        vids.append({'id': vid, 'title': title, 'duration': num(dur),
                     'viewCount': num(views), 'timestamp': num(ts)})
    return vids

for name, url in CHANNELS:
    cache_path = f'{RES}/{name}.json'
    old = json.load(open(cache_path)) if os.path.exists(cache_path) else {}
    old_ids = {v['id'] for v in old.get('videos', [])}
    vids = enum(url)
    new = [v for v in vids if v['id'] not in old_ids]
    gone = [i for i in old_ids if i not in {v['id'] for v in vids}]
    doc = {'channel': url, 'playlistTitle': 'Videos', 'count': len(vids),
           'enumeratedUtc': __import__('datetime').datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
           'videos': vids}
    json.dump(doc, open(cache_path, 'w'), indent=1, ensure_ascii=False)
    print(f'{name}: fresh={len(vids)} cached={old.get("count")} delta=+{len(new)} -{len(gone)}')
    for v in new[:10]:
        print(f'    NEW {v["id"]} {v["title"][:70]}')
    for i in gone[:10]:
        print(f'    GONE {i}')
    sys.stdout.flush()
