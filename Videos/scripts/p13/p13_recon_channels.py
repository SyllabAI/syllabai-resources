#!/usr/bin/env python3
"""P13 recon: Alt Academy channel family survey.
Main handle @altacademyorg (UCTgPevMIji1ZyP4IPhmwDsQ) features 8 subject channels.
Verify each channel page's externalId == shelf id, then flat-enumerate uploads 1-2500.
Writes work/p13recon/<slug>_raw.tsv + p13_summary.json.
"""
import json, os, subprocess, re, sys

WORK = "/home/z/my-project/work/p13recon"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

# slug -> (expected UC id from the featured-channels shelf, label)
CHANNELS = [
    ("alt-org-main", "UCTgPevMIji1ZyP4IPhmwDsQ", "Alt Academy (main handle)"),
    ("alt-chemistry", "UC-d3d-0oU9iYsj-6pvpJX5g", "A Level Chemistry | Alt Academy"),
    ("alt-business", "UCeXeReICIdkwR_V9ZJ2yGIg", "A Level Business | Alt Academy (P12 pool)"),
    ("alt-economics", "UC1Ar1Z9I26a_R-lZ0qzW9UQ", "A Level Economics | Alt Academy"),
    ("alt-maths", "UCUeuU0fIwU8jHC5jdsr-wtg", "A Level Maths | Alt Academy"),
    ("alt-physics", "UCwLO28CtT1ewcP5wIhFF5bA", "A Level Physics | Alt Academy"),
    ("alt-biology", "UCEVYEqcUrnc5lJyO1zALMDw", "A Level Biology | Alt Academy"),
    ("alt-psychology", "UCa3bmJx38QfiGWT2pCCOWNQ", "A Level Psychology | Alt Academy"),
    ("alt-accounting", "UCIjJYpNevYcLZBxtfa8u5NQ", "A Level Accounting | Alt Academy"),
]

def verify(uc):
    """Fetch the channel page and confirm the externalId and title."""
    url = f"https://www.youtube.com/channel/{uc}"
    try:
        h = subprocess.run(["curl", "-s", "-L", "--max-time", "45", "-A", UA, url],
                           capture_output=True, text=True, timeout=60).stdout
        ext = re.findall(r'"externalId":"(UC[^"]+)"', h)
        title = re.findall(r'<meta property="og:title" content="([^"]+)"', h)
        return (ext[0] if ext else None, title[0] if title else None)
    except Exception as e:
        return (None, f"ERR {e}")

def enum(slug, uc):
    """Flat-enumerate uploads via yt-dlp into TSV: id, duration, view, timestamp, title, channel_id."""
    out = os.path.join(WORK, f"{slug}_raw.tsv")
    url = f"https://www.youtube.com/channel/{uc}/videos"
    cmd = ["yt-dlp", "--flat-playlist", "--playlist-items", "1-2500", "-i",
           "--print", "%(id)s\t%(duration)s\t%(view_count)s\t%(timestamp)s\t%(channel_id)s\t%(title)s",
           "-J", "--no-warnings", url]
    # use --flat-playlist with --print; run via subprocess, stream lines
    p = subprocess.run(["yt-dlp", "--flat-playlist", "--playlist-items", "1-2500", "-i", "--no-warnings",
                        "--print", "%(id)s\t%(duration)s\t%(view_count)s\t%(timestamp)s\t%(channel_id)s\t%(title)s", url],
                       capture_output=True, text=True, timeout=600)
    lines = [l for l in p.stdout.splitlines() if "\t" in l]
    with open(out, "w", encoding="utf-8") as f:
        for l in lines:
            f.write(l + "\n")
    return len(lines), p.stderr[-300:] if p.returncode != 0 else ""

def main():
    summary = {}
    for slug, uc, label in CHANNELS:
        ext, title = verify(uc)
        ok = (ext == uc)
        n, err = enum(slug, uc)
        # channel_id column consistency
        cids = set()
        with open(os.path.join(WORK, f"{slug}_raw.tsv"), encoding="utf-8") as f:
            for l in f:
                parts = l.rstrip("\n").split("\t")
                if len(parts) >= 6:
                    cids.add(parts[4])
        summary[slug] = {
            "expected_uc": uc, "label": label, "page_externalId": ext,
            "page_title": title, "identity_ok": ok,
            "n_uploads": n, "flat_channel_ids": sorted(cids),
            "err": err[:120],
        }
        print(f"{slug}: expected {uc} | page externalId {ext} | match={ok} | uploads={n} | flat cids={sorted(cids)} | title={title}")
        sys.stdout.flush()
    with open(os.path.join(WORK, "p13_summary.json"), "w") as f:
        json.dump(summary, f, indent=1)

if __name__ == "__main__":
    main()
