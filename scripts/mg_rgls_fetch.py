#!/usr/bin/env python3
"""mg_rgls_fetch.py — download every (topic, mode) page in the RG/FC/LS
catalog to the local HTML cache (resumable)."""
import json
import sys
import time
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, "/home/z/my-project/scripts/mg_rgls_work")
import mg_common as C  # noqa: E402

cat = json.load(open(f"{C.LOGS}/rgls_catalog.json"))
jobs = []
for lane, entry in cat.items():
    for slug, meta in entry["topics"].items():
        for mode in meta["modes"]:
            jobs.append((lane, entry["lane_dir"], slug, mode))
print("jobs:", len(jobs))

done = fail = 0
t0 = time.time()


def run(job):
    lane, lane_dir, slug, mode = job
    try:
        C.fetch_mode_page(lane_dir, slug, mode, lane_dir)
        return job, None
    except urllib.error.HTTPError as e:
        return job, f"HTTP {e.code}"
    except Exception as e:
        return job, str(e)[:120]


with ThreadPoolExecutor(max_workers=5) as ex:
    futs = {ex.submit(run, j): j for j in jobs}
    for fu in as_completed(futs):
        job, err = fu.result()
        if err:
            fail += 1
            print("FAIL", job[0], job[2], job[3], err, flush=True)
        else:
            done += 1
        if (done + fail) % 100 == 0:
            print(f"{done+fail}/{len(jobs)} done={done} fail={fail} {time.time()-t0:.0f}s", flush=True)

print(f"FINISHED done={done} fail={fail} in {time.time()-t0:.0f}s")
