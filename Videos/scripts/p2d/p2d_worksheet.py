#!/usr/bin/env python3
"""P2D worksheet: compact per-spec candidate table for LLM adjudication (CIE A-level trio).

Filters (stricter than P2C per tracker deferral note):
  - candidate score >= 3.5
  - cognito candidates must be channel-only (else they belong to the site lane)
Output: work/channels/p2d-worksheet-<subj>.tsv  one line per spec with up to 3 candidates.
"""
import json, re, sys

CH = "/home/z/my-project/work/channels"
V2 = "/home/z/my-project/repos/syllabai-v2-fresh"

ch_only = {v["id"] for v in json.load(open(f"{CH}/cognito-channel-only.json"))["channelOnly"]}

def prov_name(p):
    return {"cognito": "COG", "freesciencelessons": "FSL", "malmesbury-education": "MAL",
            "amoeba-sisters": "AMO", "doodlescience": "DOO"}[p]

for subj in ("biology", "chemistry", "physics"):
    match = json.load(open(f"{CH}/match-cie-a-level-{subj}-25.json"))
    out = []
    for row in match:
        code, title = row["code"], row["title"]
        cands = []
        for c in row["top"]:
            if c["score"] < 3.5:
                continue
            if c["provider"] == "cognito" and c["id"] not in ch_only:
                continue  # site-lane video, not allowed in external draft
            lvl = "AL" if re.search(r"a[ -]?level", c["title"], re.I) else ("GCSE" if re.search(r"gcse", c["title"], re.I) else "?")
            cands.append(f"{c['id']}|{prov_name(c['provider'])}|{lvl}|{c['score']:g}|{c['title'][:90]}")
        if cands:
            t = title.replace("\t", " ").strip()
            out.append(f"{code}\t{t[:160]}\t" + " ~ ".join(cands[:3]))
    with open(f"{CH}/p2d-worksheet-{subj}.tsv", "w") as f:
        f.write("\n".join(out) + "\n")
    print(subj, "rows kept:", len(out), "/", len(match), "specs")
