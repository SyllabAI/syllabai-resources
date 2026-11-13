#!/usr/bin/env python3
"""P11 recon: verify identity + flat-enumerate uploads for 14 candidate channels.
Identity law: page HTML "externalId":"UC..." is authoritative (flat-mode returns NA).
Output: /home/z/my-project/work/p11/<slug>_raw.tsv + p11_summary.json
"""
import json, os, re, subprocess, sys, urllib.request

WORK = "/home/z/my-project/work/p11"
os.makedirs(WORK, exist_ok=True)

CHANNELS = [
    ("enhancetuition", "UC-JtWwjn16J5aqMfvmxkceg"),          # CIE AS/A econ 9708
    ("econplusdal", "UCQbBh9Jn2IjcSPZOiNKJu0g"),             # Edexcel A/IAL econ
    ("yimakesiteasy", "UCpH_SaN8pH5dkf1TVN4Ja8w"),           # CIE business + geo multi
    ("cambridge-study-materials", "UCyZdlkz3Oc2I4hkPimjVi8Q"),# CIE IGCSE/AS/A multi
    ("james-gan", "UCzH8c5HRgdxNdC8igHtXCtg"),               # CIE IGCSE CS 0478
    ("igcse-online", "UCQsOJB-oUEX_Q3Ie6xGBKKg"),            # IGCSE CS 0478
    ("igcse-computer-science", "UC-2VV9ZMEN-h6L6MlNiwfcw"),  # IGCSE CS 0478
    ("purple-shirt-history", "UCiEKSuhYV8qUb3wup6eKziQ"),    # CIE IGCSE History 0470
    ("mindful-maths", "UC1QKwZGLOriJQRhngH4919A"),           # Edexcel IAL D1
    ("cambridge-accounting", "UCyXQ7oORWXppb0NBPAtpQ5A"),    # CIE 0452/9706
    ("ar-accounting", "UCMUXpRwc-dKaNkKs8ip555A"),           # CIE 0452/9706
    ("evm-dr-mohamed-saber", "UCR6nfQLaG5iMSb5idA7tDRw"),    # CIE EM 0680
    ("mr-salles", "UCEB4IwW-eVk9SxHBIGhrY3w"),               # Edexcel IGCSE/GCSE English
    ("the-igcse-geographer", "UCkIQLDXJlNlh3n-B_ilOYwQ"),    # CIE IGCSE Geo 0460
]

FMT = "%(id)s\t%(title).200s\t%(duration)s\t%(view_count)s\t%(timestamp)s"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "ignore")

def verify(slug, uc):
    """Return (verified, title) from channel page HTML externalId."""
    try:
        h = fetch(f"https://www.youtube.com/channel/{uc}/videos")
        m = re.search(r'"externalId":"(UC[^"]+)"', h)
        t = re.search(r'"title":"([^"]+)"', h)
        got = m.group(1) if m else None
        title = (t.group(1) if t else "?").encode().decode("unicode_escape")
        return (got == uc, title, got)
    except Exception as e:
        return (False, f"FETCH-ERR:{e}", None)

def enum(slug, uc):
    """Flat-enumerate uploads; return list of dicts."""
    out = subprocess.run(
        ["yt-dlp", "--flat-playlist", "--playlist-items", "1-2500", "--print", FMT,
         f"https://www.youtube.com/channel/{uc}/videos"],
        capture_output=True, text=True, timeout=900)
    rows, seen = [], set()
    for line in out.stdout.splitlines():
        parts = line.split("\t")
        if len(parts) < 5 or not parts[0] or parts[0] == "NA":
            continue
        vid, title, dur, views, ts = parts[0], parts[1], parts[2], parts[3], parts[4]
        if vid in seen:
            continue
        seen.add(vid)
        rows.append({"id": vid, "title": title, "duration": dur,
                     "viewCount": views, "timestamp": ts})
    return rows

def main():
    summary = []
    for slug, uc in CHANNELS:
        ok, title, got = verify(slug, uc)
        print(f"[{slug}] expected {uc} -> got {got} title={title!r} verified={ok}", flush=True)
        if not ok:
            summary.append({"slug": slug, "uc": uc, "verified": False, "title": title})
            continue
        try:
            rows = enum(slug, uc)
        except Exception as e:
            print(f"[{slug}] ENUM-ERR {e}", flush=True)
            summary.append({"slug": slug, "uc": uc, "verified": True, "title": title, "error": str(e)})
            continue
        with open(f"{WORK}/{slug}_raw.tsv", "w", encoding="utf-8") as f:
            for r_ in rows:
                f.write("\t".join([r_["id"], r_["title"], r_["duration"], r_["viewCount"], r_["timestamp"]]) + "\n")
        summary.append({"slug": slug, "uc": uc, "verified": True, "title": title,
                        "count": len(rows)})
        print(f"[{slug}] enumerated {len(rows)} videos", flush=True)
    with open(f"{WORK}/p11_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
