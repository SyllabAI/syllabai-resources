#!/usr/bin/env python3
"""P2F execution step 1: complete the channel pool.

- Omar's Biology Lab: enumerate the full uploads playlist (UU<id>) — the /videos
  tab undercounted (17 vs search-evidenced walkthroughs).
- A-star Solution: resolve channel id via ytsearch, enumerate.
- WPH11 physics walkthrough channel: resolve via ytsearch ("Edexcel IAL Physics
  Unit 1 WPH11 full paper walkthrough"), enumerate.
Writes work/channels/p2f-<slug>.tsv and prints counts + paper-code hits.
"""
import json, re, subprocess, pathlib

ROOT = pathlib.Path("/home/z/my-project")
WORK = ROOT / "work/channels"
SEP = chr(9)

CODE_RE = re.compile(r"\b(WCH1[1-6]|WBI1[1-6]|WPH1[1-6]|4CH1|4BI1|4PH1|9CH0|9BI0|9PH0)\b", re.I)


def sh(cmd, timeout):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)


def enum(url, timeout=300):
    fmt = SEP.join(["%(id)s", "%(title)s", "%(duration)s"])
    r = sh(f'yt-dlp --flat-playlist --print "{fmt}" "{url}"', timeout)
    rows = []
    for line in r.stdout.splitlines():
        parts = line.split(SEP)
        if len(parts) >= 2 and parts[0]:
            rows.append((parts[0], parts[1], parts[2] if len(parts) > 2 else ""))
    return rows


def resolve(query, timeout=120):
    fmt = SEP.join(["%(channel_id)s", "%(channel)s"])
    r = sh(f'yt-dlp --flat-playlist --print "{fmt}" "ytsearch5:{query}"', timeout)
    for line in r.stdout.splitlines():
        parts = line.split(SEP)
        if len(parts) == 2 and parts[0].startswith("UC"):
            return parts
    return None


def main():
    targets = [("omars-biology-lab-uploads", "https://www.youtube.com/playlist?list=UUEITENvnLnJ4bRpocLmvSow")]
    for slug, q in [
        ("a-star-solution", "A-star Solution Edexcel IAL biology paper walkthrough"),
        ("ial-physics-walkthrough", "Edexcel IAL Physics Unit 1 WPH11 full paper walkthrough channel"),
    ]:
        got = resolve(q)
        if got:
            print(f"resolved {slug}: {got[1]} ({got[0]})")
            targets.append((slug, f"https://www.youtube.com/channel/{got[0]}/videos"))
        else:
            print(f"resolve FAILED: {slug}")
    for slug, url in targets:
        try:
            rows = enum(url)
        except subprocess.TimeoutExpired:
            print(f"{slug}: TIMEOUT"); rows = []
        seen, dedup = set(), []
        for vid, title, dur in rows:
            if vid and vid not in seen:
                seen.add(vid); dedup.append((vid, title, dur))
        (WORK / f"p2f-{slug}.tsv").write_text("\n".join(SEP.join(r) for r in dedup))
        coded = [t for _, t, _ in dedup if CODE_RE.search(t)]
        print(f"{slug}: videos={len(dedup)} coded={len(coded)}")
        for t in coded[:5]:
            print(f"   e.g. {t[:100]}")


if __name__ == "__main__":
    main()
