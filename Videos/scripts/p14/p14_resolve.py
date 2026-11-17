#!/usr/bin/env python3
"""P14 recon step 1: identity resolution for the identified pool set.

For each pool: try known UC first (verify externalId + og:title), else try each
handle candidate. A handle "resolves" when the channel page returns an
externalId AND an og:title (404 pages have neither). Squat detection: record
the title so a wrong-body handle (e.g. @SirPasha -> 'rusol') is visible.

Writes /home/z/my-project/work/p14/resolve.json
"""
import json, os, re, subprocess, sys

WORK = "/home/z/my-project/work/p14"
HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def fetch(url):
    try:
        p = subprocess.run(["curl", "-s", "-L", "--max-time", "40", "-A", UA, url],
                           capture_output=True, text=True, timeout=50)
        return p.stdout
    except Exception:
        return ""

def page_identity(url):
    h = fetch(url)
    ext = re.findall(r'"externalId":"(UC[\w-]{22})"', h)
    title = re.findall(r'<meta property="og:title" content="([^"]*)"', h)
    return (ext[0] if ext else None, title[0] if title else None)

def resolve_pool(pool):
    slug, label = pool["slug"], pool["label"]
    rec = {"slug": slug, "label": label, "attempts": [], "uc": None, "title": None, "status": "unresolved"}
    # 1. known UC verify
    if pool.get("knownUc"):
        uc = pool["knownUc"]
        ext, title = page_identity(f"https://www.youtube.com/channel/{uc}")
        rec["attempts"].append({"via": f"channel/{uc}", "ext": ext, "title": title})
        if ext == uc and title:
            rec.update(uc=uc, title=title, status="resolved")
            return rec
    # 2. handle candidates
    for h in pool.get("handles", []):
        ext, title = page_identity(f"https://www.youtube.com/{h}")
        rec["attempts"].append({"via": h, "ext": ext, "title": title})
        if ext and title:
            rec.update(uc=ext, title=title, status="resolved")
            return rec
    return rec

def main():
    os.makedirs(WORK, exist_ok=True)
    pools = json.load(open(os.path.join(HERE, "p14_pools.json")))["pools"]
    out = []
    for pool in pools:
        rec = resolve_pool(pool)
        out.append(rec)
        print(f"[{rec['status']:10s}] {rec['slug']:20s} {rec.get('uc') or '-'}  {rec.get('title') or '-'}", flush=True)
    json.dump(out, open(os.path.join(WORK, "resolve.json"), "w"), indent=1)
    bad = [r["slug"] for r in out if r["status"] != "resolved"]
    print(f"resolved {len(out)-len(bad)}/{len(out)}; unresolved: {bad}")

if __name__ == "__main__":
    main()
