#!/usr/bin/env python3
"""P8 lane pre-flight: fresh PhysicsOnline enumeration, 0-delta check vs P6 inventory."""
import json, subprocess, sys
URL='https://www.youtube.com/@PhysicsOnline/videos'
fmt='%(id)s	%(duration)s	%(view_count)s	%(timestamp)s	%(title)s'
r=subprocess.run(['yt-dlp','--flat-playlist','--print',fmt,'--no-warnings','--skip-download',URL],
                 capture_output=True, text=True, timeout=900)
if r.returncode!=0:
    print('ENUM FAIL rc=',r.returncode, r.stderr[-400:]); sys.exit(1)
rows=[l.split('\t') for l in r.stdout.strip().split('\n') if l.strip()]
vids={r0[0] for r0 in rows if r0 and r0[0]}
print('fresh enumeration:', len(rows), 'uploads')
old=json.load(open('/home/z/my-project/repos/syllabai-resources/Videos/inventory/channels/physicsonline-uploads.json'))
old_ids={v['id'] for v in old['videos']}
add=vids-old_ids; rem=old_ids-vids
print('delta: +',len(add),' -',len(rem))
if add: print('added:', sorted(add)[:10])
if rem: print('removed:', sorted(rem)[:10])
print('0-DELTAS' if not add and not rem else 'DELTAS PRESENT')
