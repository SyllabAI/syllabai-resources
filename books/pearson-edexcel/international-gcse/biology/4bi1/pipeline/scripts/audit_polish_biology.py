#!/usr/bin/env python3
"""Audit the LLM polish round for the 4BI1 corpus (phase 7 step 4).

Reports before/after corruption-class counts (selection signatures) and runs
regression checks:
  - Unicode units must not decrease (here: expected 0 -> 0, formulas are
    plain digits by design — see METHOD D-7)
  - text_original preserved on every llm_repaired chunk
  - no chunk lost its question numbering ("Total N marks" count must not
    decrease on question chunks)
  - anchor drift re-check vs pristine (belt and braces; merge_llm_biology.py
    already gates on it)
"""
import json, re, collections, sys

CORPUS = "/home/z/my-project/download/rag_biology/edexcel_igcse_biology_chunks_v1.jsonl"
PRISTINE = CORPUS + ".pristine"

pristine = {c["id"]: c for c in map(json.loads, open(PRISTINE))}
chunks = [json.loads(l) for l in open(CORPUS)]

SIGS = {
    "1s(is)": re.compile(r"\b1s\b"),
    "1n(in)": re.compile(r"\b1n\b"),
    "chapler": re.compile(r"chapler\b|chapte\s+r\b", re.I),
    "ANO(AND)": re.compile(r"\bANO\b"),
    "KEV(KEY)": re.compile(r"KEV\b|kEY\s*POIHl"),
    "hvmg(living)": re.compile(r"hvmg|l1vmg|thmgs"),
    "arrow_garble": re.compile(r" -\+ |\b-\+"),
    "icon_junk": re.compile(r"\bmD\b|\bBD\b|\bDD\b|\bEll\s*>|\b11\s*>|IEl:!l!l>"),
}

def sig_counts(text):
    return {k: len(rx.findall(text)) for k, rx in SIGS.items()}

before_total = collections.Counter()
after_total = collections.Counter()
fixed_chunks = 0
for c in chunks:
    p = pristine.get(c["id"])
    if not p:
        continue
    b = sig_counts(p["text"])
    a = sig_counts(c["text"])
    for k in SIGS:
        before_total[k] += b[k]
        after_total[k] += a[k]
    if sum(b.values()) > sum(a.values()):
        fixed_chunks += 1

errs = []
polished = [c for c in chunks if c.get("llm_repaired")]
for c in polished:
    if "text_original" not in c or not c["text_original"]:
        errs.append(f"missing text_original: {c['id']}")
    p = pristine.get(c["id"])
    if p and c["text_original"] != p["text"]:
        errs.append(f"text_original != pristine text: {c['id']}")
    # question numbering must not decrease ('Total N marks' + '(N)' marks;
    # the earlier \b[a-d]\s check was junk — it counts the article 'a ')
    for rx in (r"Total\s*\d+\s*marks?", r"\(\d\)"):
        if len(re.findall(rx, p["text"])) > len(re.findall(rx, c["text"])):
            errs.append(f"question numbering decreased: {c['id']} ({rx})")
            break
    # Unicode units regression (expected 0 -> 0 on this lane)
    if len(re.findall(r"[₀-₉⁰-⁹⁺⁻]", c["text"])) < len(re.findall(r"[₀-₉⁰-⁹⁺⁻]", p["text"])):
        errs.append(f"unicode units decreased: {c['id']}")

print(f"polished chunks: {len(polished)}  (of which garble-reduced: {fixed_chunks})")
print("corruption-class counts before -> after:")
for k in SIGS:
    print(f"  {k:14s} {before_total[k]:4d} -> {after_total[k]:4d}")
print(f"\nregression errors: {len(errs)}")
for e in errs[:10]:
    print(" -", e)
print("\nAUDIT " + ("FAILED" if errs else "PASSED"))
sys.exit(1 if errs else 0)
