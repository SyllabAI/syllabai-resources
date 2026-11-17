#!/usr/bin/env python3
"""P14 recon step 2: flat enumeration of the resolved pools' /videos tab.

Per pool: yt-dlp --flat-playlist over the channel's UPLOADS PLAYLIST
(UU id — the complete public set: long-form + shorts + live replays; the
/videos tab alone under-counts channels that publish shorts/streams —
Prosperity Academy 510 tab vs 1,254 playlist), cap 15000 (the 4,000 default
truncation caught in the recon run), one TSV row per video:
id \t duration \t view_count \t timestamp \t title
Also probes /videos /shorts /streams tab counts (metadata only, recorded).

Usage: python3 p14_enumerate.py <slug> [<slug> ...]   (reads resolve.json)
Writes work/p14/<slug>_raw.tsv and tabcounts.json
"""
import json, os, subprocess, sys

WORK = "/home/z/my-project/work/p14"

def run(cmd, timeout):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)

def enum_tab(uc, tab, cap=15000):
    url = f"https://www.youtube.com/channel/{uc}/{tab}"
    p = run(["yt-dlp", "--flat-playlist", "--playlist-items", f"1-{cap}", "-i", "--no-warnings",
             "--print", "%(id)s\t%(duration)s\t%(view_count)s\t%(timestamp)s\t%(title)s", url], timeout=1800)
    lines = [l for l in p.stdout.splitlines() if l.count("\t") >= 4]
    return lines

def main():
    os.makedirs(WORK, exist_ok=True)
    resolve = {r["slug"]: r for r in json.load(open(os.path.join(WORK, "resolve.json"))) if r["status"] == "resolved"}
    slugs = sys.argv[1:] or list(resolve)
    tabcounts = {}
    tcp = os.path.join(WORK, "tabcounts.json")
    if os.path.exists(tcp):
        tabcounts = json.load(open(tcp))
    for slug in slugs:
        rec = resolve.get(slug)
        if not rec:
            print(f"[skip] {slug}: not resolved", flush=True)
            continue
        uc = rec["uc"]
        uu = "UU" + uc[2:]
        out = os.path.join(WORK, f"{slug}_up.tsv")
        if os.path.exists(out) and os.path.getsize(out) > 0:
            print(f"[done] {slug}: cached ({sum(1 for _ in open(out))} rows)", flush=True)
            continue
        print(f"[enum] {slug} {uc} -> {uu} ...", flush=True)
        try:
            url = f"https://www.youtube.com/playlist?list={uu}"
            p = run(["yt-dlp", "--flat-playlist", "--playlist-items", "1-15000", "-i", "--no-warnings",
                     "--print", "%(id)s\t%(duration)s\t%(view_count)s\t%(timestamp)s\t%(title)s", url],
                    timeout=2400)
            vids = [l for l in p.stdout.splitlines() if l.count("\t") >= 4]
            with open(out, "w", encoding="utf-8") as f:
                for l in vids:
                    f.write(l + "\n")
            print(f"  uploads: {len(vids)}", flush=True)
        except subprocess.TimeoutExpired:
            vids = []
            print("  uploads TIMEOUT", flush=True)
        tab = {"uploads": len(vids)}
        for t in ("videos", "shorts", "streams"):
            try:
                lines = enum_tab(uc, t, cap=2000)
                tab[t] = len(lines)
            except subprocess.TimeoutExpired:
                tab[t] = -1
        tabcounts[slug] = tab
        json.dump(tabcounts, open(tcp, "w"), indent=1)
        print(f"  tabs: {tab}", flush=True)

if __name__ == "__main__":
    main()
