#!/usr/bin/env python3
"""P2D worksheet v2: tighter mechanical pre-filter for LLM adjudication.

Drops (junk classes, aligned with census honesty notes):
  - Cognito Psychology videos (no SyllabAI psychology course exists)
  - Cognito KS3 videos (A-level depth mismatch)
  - candidate score < 4.0
  - cognito candidates not channel-only (site lane owns those)
Prints survivors to work/channels/p2d-ws2-<subj>.tsv sorted by best score desc.
"""
import json, re

CH = "/home/z/my-project/work/channels"

ch_only = {v["id"] for v in json.load(open(f"{CH}/cognito-channel-only.json"))["channelOnly"]}

def junk(c):
    t = c["title"]
    if c["provider"] == "cognito" and re.search(r"psychology", t, re.I):
        return True
    if c["provider"] == "cognito" and re.search(r"\bKS3\b", t):
        return True
    return False

for subj in ("biology", "chemistry", "physics"):
    match = json.load(open(f"{CH}/match-cie-a-level-{subj}-25.json"))
    out = []
    for row in match:
        cands = []
        for c in row["top"]:
            if c["score"] < 4.0:
                continue
            if c["provider"] == "cognito" and c["id"] not in ch_only:
                continue
            if junk(c):
                continue
            lvl = "AL" if re.search(r"a[ -]?level", c["title"], re.I) else ("GCSE" if re.search(r"gcse", c["title"], re.I) else "?")
            cands.append(f"{c['id']}|{'COG' if c['provider']=='cognito' else 'FSL' if c['provider']=='freesciencelessons' else 'MAL' if c['provider']=='malmesbury-education' else 'AMO'}|{lvl}|{c['score']:g}|{c['title'][:60]}")
        if cands:
            t = row["title"].replace("\t", " ").strip()
            out.append((cands[0] and float(cands[0].split("|")[3]), f"{row['code']}\t{t[:95]}\t" + " ~ ".join(cands[:2])))
    out.sort(key=lambda x: -x[0])
    with open(f"{CH}/p2d-ws2-{subj}.tsv", "w") as f:
        for _, line in out:
            f.write(line + "\n")
    print(subj, "survivors:", len(out))
