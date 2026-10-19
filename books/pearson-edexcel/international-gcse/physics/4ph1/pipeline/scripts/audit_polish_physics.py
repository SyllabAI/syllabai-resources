#!/usr/bin/env python3
"""Post-polish audit for physics v1 (chemistry-style): re-score the polished
corpus with the same selector patterns and report before/after on the 300
polished ids plus corpus-wide space-glue totals."""
import json, re, sys
from collections import Counter

sys.path.insert(0, "/home/z/my-project/scripts")

POLISHED = "/home/z/my-project/download/rag_physics/edexcel_igcse_physics_chunks_v1.jsonl"
PRISTINE = "/home/z/my-project/physics_work/edexcel_igcse_physics_chunks_v1.jsonl"
REPAIRS = "/home/z/my-project/data/llm_repairs_physics.jsonl"

PATTERNS = {
    "space_run":     re.compile(r"\b[a-z]{18,}\b"),
    "caps_glue":     re.compile(r"\b[A-Z]{12,}\b"),
    "camel_glue":    re.compile(r"\b[a-z]{3,}[A-Z][a-z]{2,}\b"),
    "latex_remnant": re.compile(r"\\|\{|\}"),
    "repeated_punct": re.compile(r"(\W)\1{3,}"),
}
CAPS_OK = {"INTERPRETATION", "ELECTROMAGNETISM", "ELECTROMAGNETIC", "ELECTROSTATIC",
           "ACCELERATION", "ACCELERATORS", "ASTROPHYSICS", "INVESTIGATION",
           "INTERNATIONAL", "RADIOACTIVITY", "GRAVITATIONAL", "GRAVITATIONALLY",
           "CHARACTERISTIC", "CHARACTERISTICS", "PROPORTIONALITY", "MILLIMETRE",
           "MILLIMETRES", "MICROAMMETER", "MICROAMMETERS", "THERMOCOUPLE",
           "THERMOMETERS", "THERMOMETER", "PHOTOSYNTHESIS", "SUPERCONDUCTORS",
           "SEMICONDUCTORS", "CENTRIPETALLY", "UNDERSTANDING", "MEASUREMENTS",
           "PHOTOGRAPHS", "PHOTOGRAPHIC", "TEMPERATURES", "OSCILLOSCOPE",
           "OSCILLOSCOPES", "MANOMETERS", "EXTRAPOLATION", "OBSERVATIONS"}

def hits_of(txt):
    h = {}
    for name, pat in PATTERNS.items():
        n = len(pat.findall(txt))
        if name == "caps_glue":
            n = len([m for m in pat.findall(txt) if m not in CAPS_OK])
        if n:
            h[name] = n
    return h

pre = {}
for l in open(PRISTINE, encoding="utf-8"):
    c = json.loads(l)
    pre[c["id"]] = c
post = {}
for l in open(POLISHED, encoding="utf-8"):
    c = json.loads(l)
    post[c["id"]] = c
reps = {}
for l in open(REPAIRS, encoding="utf-8"):
    r = json.loads(l)
    if r["status"] == "ok":
        reps[r["id"]] = r

polished_ids = {c["id"] for c in post.values() if c.get("llm_repaired")}
changed_ids = {rid for rid, r in reps.items() if rid in post and post[rid]["text_original"] != post[rid]["text"]}

print(f"llm_repaired flags in corpus: {len(polished_ids)}  text actually changed: {len(changed_ids)}")

# corpus-wide before/after of each class
tb = Counter()
ta = Counter()
for cid, c in pre.items():
    for k, v in hits_of(c["text"]).items():
        tb[k] += v
for cid, c in post.items():
    for k, v in hits_of(c["text"]).items():
        ta[k] += v
print("\nclass totals  before -> after (corpus-wide):")
for k in sorted(set(tb) | set(ta)):
    print(f"  {k:15s} {tb.get(k,0):5d} -> {ta.get(k,0):5d}")

# focus: changed chunks only
print("\non changed chunks only:")
for k in sorted(PATTERNS):
    b = a = 0
    for cid in changed_ids:
        b += hits_of(pre[cid]["text"]).get(k, 0)
        a += hits_of(post[cid]["text"]).get(k, 0)
    print(f"  {k:15s} {b:5d} -> {a:5d}")

# residual examples of space_run on changed chunks (if any)
res = []
for cid in changed_ids:
    h = hits_of(post[cid]["text"])
    if h.get("space_run"):
        m = re.findall(r"\b[a-z]{18,}\b", post[cid]["text"])
        res.append((cid, m[:4]))
print(f"\nchanged chunks still containing 18+ lowercase runs: {len(res)}/(changed={len(changed_ids)})")
for cid, m in res[:10]:
    print(f"  {cid}: {m}")

# safety: any llm_repaired chunk whose unicode unit chars dropped vs original?
UNI = re.compile(r"[₀-₉⁰¹²³⁴-⁹⁺⁻°×μΩ·]")
drop = 0
for cid in changed_ids:
    c = post[cid]
    if len(UNI.findall(c["text"])) < len(UNI.findall(c["text_original"])):
        drop += 1
print(f"chunks with unicode-unit regression vs text_original: {drop}")
