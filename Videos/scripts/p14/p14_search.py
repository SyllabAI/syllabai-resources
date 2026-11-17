#!/usr/bin/env python3
"""P14 recon step 1b: search fallback for the unresolved pools.

yt-dlp ytsearch over likely query terms; each hit video reveals the owner
channel (channel_id + channel). We take the channel whose title matches the
pool label fuzzily, then verify it with the page-identity gate (externalId +
og:title) before accepting.
"""
import json, os, re, subprocess, sys

WORK = "/home/z/my-project/work/p14"
HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

QUERIES = {
    "dr-hanaa-assil": ["Dr Hanaa Assil chemistry", "Hanaa Assil IAL chemistry unit",
                       "Dr Hanaa Assil Edexcel", "أستاذة هناء عصيل chemistry"],
    "examsolutions": ["ExamSolutions maths revision", "ExamSolutions A Level maths",
                      "ExamSolutions core 1", "ExamSolutions past paper"],
}

def ytsearch_videos(query, n=8):
    try:
        p = subprocess.run(["yt-dlp", "--flat-playlist", "--no-warnings", "-i",
                            "--print", "%(channel_id)s\t%(channel)s\t%(title)s",
                            f"ytsearch{n}:{query}"],
                           capture_output=True, text=True, timeout=120)
        rows = []
        for l in p.stdout.splitlines():
            if l.count("\t") >= 2:
                cid, ch, t = l.split("\t", 2)
                rows.append({"channelId": cid, "channel": ch, "title": t})
        return rows
    except Exception as e:
        print(f"  search ERR {e}", flush=True)
        return []

def page_identity(uc):
    try:
        p = subprocess.run(["curl", "-s", "-L", "--max-time", "40", "-A", UA,
                            f"https://www.youtube.com/channel/{uc}"],
                           capture_output=True, text=True, timeout=50)
        h = p.stdout
        ext = re.findall(r'"externalId":"(UC[\w-]{22})"', h)
        title = re.findall(r'<meta property="og:title" content="([^"]*)"', h)
        return (ext[0] if ext else None, title[0] if title else None)
    except Exception:
        return (None, None)

def main():
    resolve_path = os.path.join(WORK, "resolve.json")
    recs = json.load(open(resolve_path))
    pools = json.load(open(os.path.join(HERE, "p14_pools.json")))["pools"]
    for rec in recs:
        if rec["status"] == "resolved":
            continue
        slug = rec["slug"]
        label_words = set(re.findall(r"[a-z0-9]+", slug.replace("-", " ")))
        print(f"== {slug}", flush=True)
        for q in QUERIES.get(slug, []):
            hits = ytsearch_videos(q)
            for h in hits:
                ch = (h["channel"] or "").lower()
                toks = set(re.findall(r"[a-z0-9]+", ch))
                score = len(label_words & toks)
                print(f"  [{score}] {h['channelId']}  {h['channel']!r}  via {q!r}", flush=True)
            # accept the best-scoring distinct channel id
            best, best_score = None, 0
            for h in hits:
                toks = set(re.findall(r"[a-z0-9]+", (h["channel"] or "").lower()))
                s = len(label_words & toks)
                if s > best_score:
                    best, best_score = h, s
            if best and best_score >= 1:
                ext, title = page_identity(best["channelId"])
                if ext == best["channelId"] and title:
                    rec.update(uc=ext, title=title, status="resolved")
                    rec["attempts"].append({"via": f"search {q!r} -> {best['channel']!r}", "ext": ext, "title": title})
                    print(f"  ACCEPTED {ext} {title!r}", flush=True)
                    break
        print(f"  -> {rec['status']}", flush=True)
    json.dump(recs, open(resolve_path, "w"), indent=1)
    bad = [r["slug"] for r in recs if r["status"] != "resolved"]
    print(f"now resolved {len(recs)-len(bad)}/{len(recs)}; unresolved: {bad}")

if __name__ == "__main__":
    main()
