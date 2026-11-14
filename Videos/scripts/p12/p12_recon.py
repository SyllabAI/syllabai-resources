#!/usr/bin/env python3
"""P12 recon: four-cluster narrow lane (CIE 9609 business / 9696 geography / 8291 EM / 8021 GP).
Verify channel identities via page HTML externalId, flat-enumerate uploads (1-2500),
then check 0-overlap vs the shipped union (hub video-map files + resources inventories).
Outputs: /home/z/my-project/work/p12/<slug>_raw.tsv + p12_summary.json
"""
import json, os, re, subprocess, sys, glob

WORK = "/home/z/my-project/work/p12"
HUB = "/home/z/my-project/repos/syllabai-v2-fresh/apps/hub/content"
RES = "/home/z/my-project/repos/syllabai-resources"
os.makedirs(WORK, exist_ok=True)

CHANNELS = [
    # 9609 AS+A Business -> cie-as-business-23, cie-a-level-business-23
    ("cambridge-business-essentials", "UCBghNFKu4_j9YpHg4o-TQOg"),
    ("bizedmadesimple",               "UCxPta4NlMZ3CBti0OUmvXrg"),
    ("alt-academy",                   "UCeXeReICIdkwR_V9ZJ2yGIg"),
    ("the-teaching-student",          "UC04KDImwBhCHu664PDV8uUg"),
    # 9696 A-level Geography -> cie-a-level-geography-21
    ("the-geography-academy",         "UCNth23RczrhjxL8lA5_sF7A"),
    # 8291 AS EM -> cie-as-environmental-management-20
    ("virtual-pathways",              "UCtEDR3qN4FmuTeTGLhFXT3A"),
    ("polymath-institute",            "UCXW5YKhzoppgzUIVIJQJAkg"),
    # 8021 AS General Paper -> cie-as-english-general-paper-21
    ("mini-lessons-gp",               "UCW-2dBZBvYpbsD08CRaa-Xw"),
    ("english-with-ms-irum",          "UCRz7wmPcMQiUTEmvjmhdAHQ"),
    ("ace-the-exam",                  "UCXfAcssq7aRN-f34V4KQVsg"),
    ("miss-cutu",                     "UCQvxMIfHaHps7wDSkX-biEA"),
]

def curl(url):
    return subprocess.run(["curl", "-s", "-L", url, "-H", "User-Agent: Mozilla/5.0"],
                          capture_output=True, text=True, timeout=60).stdout

def verify(slug, uc):
    html = curl(f"https://www.youtube.com/channel/{uc}")
    eid = re.search(r'"externalId":"(UC[\w-]{22})"', html)
    meta = re.search(r'"channelMetadataRenderer":\{"title":"([^"]+)"', html)
    ok = bool(eid and eid.group(1) == uc)
    title = meta.group(1) if meta else (eid.group(1) if eid else "?")
    print(f"  verify {slug}: externalId={'MATCH' if ok else 'MISMATCH/NA'} title={title!r}")
    return ok, title

def enum(slug, uc):
    out = os.path.join(WORK, f"{slug}_raw.tsv")
    fmt = "%(id)s\t%(title)s\t%(duration)s\t%(view_count)s\t%(timestamp)s"
    cmd = ["yt-dlp", "--flat-playlist", "--playlist-items", "1-2500", "--print", fmt,
           f"https://www.youtube.com/channel/{uc}/videos"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    lines = [l for l in r.stdout.splitlines() if "\t" in l and l.split("\t")[0]]
    with open(out, "w") as f:
        f.write("\n".join(lines) + ("\n" if lines else ""))
    print(f"  enum {slug}: {len(lines)} videos -> {out}")
    return len(lines), out

def shipped_union():
    ids = set()
    for f in glob.glob(os.path.join(HUB, "video-map", "*.json")):
        if f.endswith("registry.json"):
            continue
        ids |= set(re.findall(r"\b([A-Za-z0-9_-]{11})\b", open(f, errors="ignore").read()))
    for f in glob.glob(os.path.join(RES, "Videos/inventory/channels/*-uploads.json")):
        try:
            d = json.load(open(f))
            for v in d.get("videos", d if isinstance(d, list) else []):
                vid = v.get("id") if isinstance(v, dict) else v
                if isinstance(vid, str) and len(vid) == 11:
                    ids.add(vid)
        except Exception:
            pass
    return ids

def main():
    summary = []
    print("== verify ==")
    for slug, uc in CHANNELS:
        ok, title = verify(slug, uc)
        summary.append({"slug": slug, "uc": uc, "verified": ok, "title": title})
    print("== enumerate ==")
    for s in summary:
        n, path = enum(s["slug"], s["uc"])
        s["count"] = n
        s["path"] = path
    print("== overlap vs shipped union ==")
    union = shipped_union()
    print(f"  shipped union ids: {len(union)}")
    total, overlaps = 0, {}
    for s in summary:
        vids = [l.split("\t")[0] for l in open(s["path"]).read().splitlines() if l]
        hit = [v for v in vids if v in union]
        s["overlap"] = len(hit)
        total += len(vids)
        if hit:
            overlaps[s["slug"]] = hit
    print(f"  pool total: {total} videos; overlap: {sum(s['overlap'] for s in summary)}")
    if overlaps:
        print("  OVERLAP DETAIL:", json.dumps(overlaps, indent=1)[:800])
    out = os.path.join(WORK, "p12_summary.json")
    json.dump(summary, open(out, "w"), indent=1)
    print(f"== summary -> {out}")
    print(json.dumps([{k: s[k] for k in ('slug', 'verified', 'count', 'overlap')} for s in summary], indent=1))

if __name__ == "__main__":
    main()
