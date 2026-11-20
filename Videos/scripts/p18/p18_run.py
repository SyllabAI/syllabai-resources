#!/usr/bin/env python3
"""P18 gap-profile lane: resolve (identity gate) + enumerate (uploads playlist) + classify.

Per pool in p18_pools.json:
  1. resolve: UC verify via page-identity gate (externalId + og:title must agree)
  2. enumerate: yt-dlp flat over UU<id> uploads playlist, cap 15000, TSV rows
  3. classify: textual register families over titles — the P14/P15 shape with the
     CORRECTED codes (4GE1 / 4IT1 / 4XM / 4WS+4XS / 4WB+4XB / 4WC+4XC / 4MB1 /
     4CH1 / 0607 / 8021 / 4PM0-further-pure added; P15/P17 carried forward).
Writes work/p18/<slug>_up.tsv, resolve.json, tabcounts.json, classify.json.

Usage: python3 p18_run.py resolve|enum|classify [slug ...]
"""
import json, os, re, subprocess, sys

WORK = "/home/z/my-project/work/p18"
HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
os.makedirs(WORK, exist_ok=True)


def run(cmd, timeout):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def fetch(url):
    try:
        return run(["curl", "-s", "-L", "--max-time", "40", "-A", UA, url], 50).stdout
    except Exception:
        return ""


def page_identity(url):
    h = fetch(url)
    ext = re.findall(r'"externalId":"(UC[\w-]{22})"', h)
    title = re.findall(r'<meta property="og:title" content="([^"]*)"', h)
    return (ext[0] if ext else None, title[0] if title else None)


FAMILIES = {
    "0610/0973 biology": r"\b0?610\b|\b0973\b|IGCSE\s*Biology|igcse\s*bio",
    "0620 chemistry": r"\b0620\b|\b0971\b|IGCSE\s*Chem",
    "0625 physics": r"\b0625\b|\b0972\b|IGCSE\s*Physics",
    "0654 co-ordinated": r"\b0654\b|co-?ordinated\s*science|double\s*award",
    "0653 combined": r"\b0653\b|combined\s*science",
    "0452 accounting": r"\b0452\b|IGCSE\s*Account",
    "0455 economics": r"\b0455\b|IGCSE\s*Economics|IGCSE\s*econ",
    "0680 env-mgmt": r"\b0680\b|environmental\s*management|\bE\.M\.\b|\bEM\b\s*paper",
    "8291 AS env-mgmt": r"\b8291\b|AS\s*Environmental",
    "8021 general paper": r"\b8021\b|general\s*paper",
    "0417 ICT": r"\b0417\b|IGCSE\s*ICT",
    "Ed-IGCSE ICT 4IT1": r"\b4IT1\b|\b4IT0\b|ICT\s*Paper|Edexcel\s*i?GCSE\s*ICT|Edexcel\s*i?GCSE\s*Computer\s*Science|pseudocode",
    "4MA1 maths A": r"\b4MA1\b|IGCSE\s*Maths|IGCSE\s*Math|Maths\s*A\b",
    "4MB1 maths B": r"\b4MB1\b|Maths\s*B\b",
    "4XM modular maths": r"\b4XM\d?\b|IGCSE\s*Maths\s*modular|modular\s*(higher|foundation)\s*unit",
    "0460 geography": r"\b0460\b|\b0976\b|IGCSE\s*Geography",
    "4GE1 geography A": r"\b4GE1\b|Edexcel\s*IGCSE\s*Geography",
    "4GE0 geography B": r"\b4GE0\b",
    "Ed-IGCSE sciences": r"\b4CH1\b|\b4CH0\b|\b4PH1\b|\b4PH0\b|\b4BI1\b|\b4BI0\b|\b4SD0\b|\b4SS0\b|Edexcel\s*i?GCSE\s*(Chemistry|Physics|Biology|Science)",
    "4WS/4XS modular science": r"\b4WS\d?\b|\b4XS\d?\b|IGCSE\s*science\s*modular|science\s*double\s*award\s*modular",
    "4WB/4XB modular biology": r"\b4WB\d?\b|\b4XB\d?\b",
    "4WC/4XC modular chemistry": r"\b4WC\d?\b|\b4XC\d?\b",
    "WPH11-16 physics": r"\bWPH\d?\d?\b|IAL\s*[Pp]hysics|IAS\s*[Pp]hysics|IA2\s*[Pp]hysics",
    "WBI11-16 biology": r"\bWBI\d?\d?\b|IAL\s*[Bb]iology|IAS\s*[Bb]iology|IA2\s*[Bb]iology",
    "WCH11-16 chemistry": r"\bWCH\d?\d?\b|IAL\s*[Cc]hemistry|IAS\s*[Cc]hemistry|IA2\s*[Cc]hemistry|IAL\s*Chem|Unit\s*[1-6]\s*.{0,14}IAL",
    "IAL unit-session (Pearson)": r"[Aa]\s*[Ll]evel\s*\|?\s*(Biology|Chemistry|Physics)\s*\|?\s*Unit\s*[1-6]",
    "0607 international maths": r"\b0607\b|international\s*mathematics",
    "4PM0 further pure": r"\b4PM\d?\b|[Ff]urther\s*[Pp]ure|IGCSE\s*Further\s*Maths",
    "0606 add-maths": r"\b0606\b|[Aa]dd(itional)?\s*[Mm]aths",
    "0500 FLE": r"\b0500\b|[Ff]irst\s*[Ll]anguage\s*[Ee]nglish|directed\s*writing",
    "0475 literature": r"\b0475\b|[Ss]ongs\s*of\s*[Oo]urselves|[Ss]tories\s*of\s*[Oo]urselves|Study\s*Guide\s*for\s*Cambridge|i?GCSE\s*English\s*Lit(erature)?",
    "9708 econ": r"\b9708\b|A\s*[Ll]evel\s*[Ee]conomics",
    "9609 business": r"\b9609\b|A\s*[Ll]evel\s*[Bb]usiness",
    "4BS1 business": r"\b4BS1\b|\b4BS0\b|Edexcel\s*i?GCSE\s*Business|IGCSE\s*Business\s*Studies",
    "session pattern": r"(M/J|O/N|F/M|ON|MJ|FM)\s*'?2?\d|May[/ ]?June|Oct[/ ]?(Nov)?|Feb[/ ]?March|Paper\s*[1-6]\b|qp\s?_?\s?[0-9]{2}|9702|9701|9700|9709",
    "NT AQA/OCR/IB": r"\bAQA\b|\bOCR\b|\bIB\b|MYP|CBSE|NCERT|GCSE\s*Computer\s*Science\s*New\s*Specification",
}


def classify_titles(titles):
    out = {k: 0 for k in FAMILIES}
    for t in titles:
        for k, rx in FAMILIES.items():
            if re.search(rx, t, re.IGNORECASE):
                out[k] += 1
    return out


def cmd_resolve(slugs):
    pools = json.load(open(os.path.join(HERE, "p18_pools.json")))["pools"]
    pools = [p for p in pools if not slugs or p["slug"] in slugs]
    rp = os.path.join(WORK, "resolve.json")
    recs = []
    if os.path.exists(rp):
        recs = [r for r in json.load(open(rp)) if r["slug"] not in {p["slug"] for p in pools}]
    for p in pools:
        uc, title = page_identity(f"https://www.youtube.com/channel/{p['knownUc']}")
        status = "resolved" if uc == p["knownUc"] and title else "FAILED"
        recs.append({"slug": p["slug"], "label": p["label"], "uc": uc if uc == p["knownUc"] else None,
                     "title": title, "status": status, "provenance": p.get("provenance")})
        print(f"[resolve] {p['slug']}: {status} title={title!r}", flush=True)
    json.dump(recs, open(rp, "w"), indent=1)


def cmd_enum(slugs):
    recs = [r for r in json.load(open(os.path.join(WORK, "resolve.json"))) if r["status"] == "resolved" and (not slugs or r["slug"] in slugs)]
    tcp = os.path.join(WORK, "tabcounts.json")
    tabcounts = json.load(open(tcp)) if os.path.exists(tcp) else {}
    for rec in recs:
        slug, uc = rec["slug"], rec["uc"]
        uu = "UU" + uc[2:]
        out = os.path.join(WORK, f"{slug}_up.tsv")
        if os.path.exists(out) and os.path.getsize(out) > 0:
            print(f"[enum] {slug}: cached ({sum(1 for _ in open(out))} rows)", flush=True)
            continue
        print(f"[enum] {slug} {uc} -> {uu} ...", flush=True)
        try:
            p = run(["yt-dlp", "--flat-playlist", "--playlist-items", "1-15000", "-i", "--no-warnings",
                     "--print", "%(id)s\t%(duration)s\t%(view_count)s\t%(timestamp)s\t%(title)s",
                     f"https://www.youtube.com/playlist?list={uu}"], 2400)
            vids = [l for l in (p.stdout or "").splitlines() if l.count("\t") >= 4]
        except subprocess.TimeoutExpired:
            vids = []
            print("  uploads TIMEOUT", flush=True)
        with open(out, "w", encoding="utf-8") as f:
            for l in vids:
                f.write(l + "\n")
        tabcounts[slug] = {"uploads": len(vids)}
        print(f"  uploads: {len(vids)}", flush=True)
        json.dump(tabcounts, open(tcp, "w"), indent=1)


def cmd_classify(slugs):
    recs = {r["slug"]: r for r in json.load(open(os.path.join(WORK, "resolve.json"))) if r["status"] == "resolved"}
    out = {}
    for slug in (slugs or sorted(recs)):
        tsv = os.path.join(WORK, f"{slug}_up.tsv")
        if not os.path.exists(tsv):
            continue
        titles = []
        for l in open(tsv, encoding="utf-8"):
            parts = l.rstrip("\n").split("\t")
            if len(parts) >= 5:
                titles.append("\t".join(parts[4:]))
        fam = classify_titles(titles)
        out[slug] = {"title": recs[slug]["title"], "uc": recs[slug]["uc"], "uploads": len(titles),
                     "families": {k: v for k, v in sorted(fam.items(), key=lambda x: -x[1]) if v}}
        print(f"[classify] {slug}: {len(titles)} uploads; top: {dict(list(out[slug]['families'].items())[:4])}", flush=True)
    json.dump(out, open(os.path.join(WORK, "classify.json"), "w"), indent=1)


if __name__ == "__main__":
    cmd = sys.argv[1]
    slugs = sys.argv[2:]
    {"resolve": cmd_resolve, "enum": cmd_enum, "classify": cmd_classify}[cmd](slugs)
