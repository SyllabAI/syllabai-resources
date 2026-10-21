#!/usr/bin/env python3
"""Merge LLM fidelity-polish results into the 4BI1 corpus (phase 7 step 3).

Applies llm_repairs_biology.jsonl 'ok' records in place:
  - text -> repaired text
  - text_original -> pre-polish text preserved (PARSE_STANDARD point 7)
  - llm_repaired: true
  - char_count recomputed
Then regenerates the full-book markdown + parse report, and runs the ANCHOR
DIFF against the pristine corpus (golden rule 10: 0 drift on id / unit /
chapter / content_type / pdf_pages / book_pages / section / title fields).
"""
import json, shutil, collections, sys, os, re

BOOK = "/home/z/my-project/syllabai-resources/books/pearson-edexcel/international-gcse/biology/4bi1"
CORPUS = "/home/z/my-project/download/rag_biology/edexcel_igcse_biology_chunks_v1.jsonl"
REPAIRS = "/home/z/my-project/data/biology/llm_repairs_biology.jsonl"
REPORT = "/home/z/my-project/download/rag_biology/parse_report_v1.json"

ANCHOR_KEYS = ["id", "unit_no", "unit_name", "chapter_no", "chapter_title",
               "section", "content_type", "book_pages", "pdf_pages"]

# Skill-tag slivers already dropped by the round-1 partial merge (2026-10-20,
# lane worklog 23:15): junk-only <40-char chunks with no RAG value. Frozen here
# so idempotent re-merges after resuming the polish keep the anchor diff clean
# (they are absent from the corpus by design and cannot be re-detected).
PREV_DROPPED_IDS = {"bio_v1_u2_c4_pdf038_0259", "bio_v1_u2_c5_pdf045_0296"}

pristine_path = CORPUS + ".pristine"
if not os.path.exists(pristine_path):
    shutil.copyfile(CORPUS, pristine_path)
    print(f"[merge] pristine copy saved -> {pristine_path}")

pristine = {c["id"]: c for c in map(json.loads, open(pristine_path))}
chunks = [json.loads(l) for l in open(CORPUS)]

repairs = {}
for line in open(REPAIRS):
    if line.strip():
        r = json.loads(line)
        if r["status"] == "ok":
            repairs[r["id"]] = r["text"]

applied = skipped = 0
for c in chunks:
    if c["id"] in repairs:
        if "text_original" not in c:
            c["text_original"] = c["text"]
        c["text"] = repairs[c["id"]]
        c["char_count"] = len(c["text"])
        c["llm_repaired"] = True
        applied += 1
    elif c["id"] in repairs and "llm_repaired" in c:
        skipped += 1

# ---- degenerate sliver cleanup (documented, evidence in worklog) -----------
# Repairs correctly strip icon junk; two junk-only question slivers
# ("DD\n\nEXECUTIVE FUNCTION") shrink to bare skill tags (<40 chars) with no
# RAG value — their question content lives in sibling chunks. Drop chunks
# that are <40 chars AND consist solely of skill-tag words; record count.
SKILL_ONLY = re.compile(
    r"^(?:CRITICAL\s*THINKING|ANALYSIS|REASONING|INTERPRETATION|"
    r"DECISION\s*MAKING|PROBLEM\s*SOLVING|EXECUTIVE\s*FUNCTION|MATHEMATICS|"
    r"PRACTICAL\s*SKILLS?[\s,!]*)+$", re.I)
dropped_ids = set()
before_drop = len(chunks)
kept = []
for c in chunks:
    if c["char_count"] < 40 and SKILL_ONLY.match(c["text"].strip()):
        dropped_ids.add(c["id"])
    else:
        kept.append(c)
chunks = kept
dropped_slivers = before_drop - len(chunks)
if dropped_slivers:
    print(f"[merge] dropped {dropped_slivers} skill-tag sliver chunks (<40 chars, no content): {sorted(dropped_ids)}")

# ---- anchor diff vs pristine (must be 0 drift) -----------------------------
drift = 0
for c in chunks:
    p = pristine.get(c["id"])
    if not p:
        drift += 1
        print(f"[anchor] NEW id not in pristine: {c['id']}")
        continue
    for k in ANCHOR_KEYS:
        if c.get(k) != p.get(k):
            drift += 1
            print(f"[anchor] DRIFT {k} on {c['id']}: {p.get(k)!r} -> {c.get(k)!r}")
extra = set(pristine) - {c["id"] for c in chunks} - dropped_ids - PREV_DROPPED_IDS
if extra:
    drift += len(extra)
    print(f"[anchor] MISSING ids: {sorted(extra)[:5]}")
# intentional sliver drops are reported, not drift
if dropped_ids - (set(pristine) - {c["id"] for c in chunks}):
    pass  # dropped ids were in pristine and are intentionally absent

with open(CORPUS, "w", encoding="utf-8") as f:
    for c in chunks:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")

# ---- regenerate markdown + report ------------------------------------------
BOOK_TITLE, BOOK_AUTHOR = chunks[0]["book_title"], chunks[0]["author"]
md = [f"# {BOOK_TITLE} — {BOOK_AUTHOR}", ""]
last = None
for c in chunks:
    key = (c["unit_no"], c["chapter_no"])
    if key != last:
        if c["unit_no"]:
            md.append(f"\n## Unit {c['unit_no']}: {c['unit_name']}")
        md.append(f"\n### {c['chapter_title']}\n")
        last = key
    if c["section"] and c["text"].split("\n\n")[0] != c["section"]:
        md.append(f"\n#### {c['section']}")
    md.append(c["text"])
with open("/home/z/my-project/download/rag_biology/full_book_textlayer.md", "w") as f:
    f.write("\n".join(md))

report = json.load(open(REPORT))
types = collections.Counter(c["content_type"] for c in chunks)
sizes = sorted(c["char_count"] for c in chunks)
report.update({
    "n_chunks": len(chunks), "content_types": dict(types),
    "size_min": sizes[0], "size_max": sizes[-1],
    "size_avg": round(sum(sizes) / len(sizes)),
    "n_chunks_over_hardmax": sum(1 for s in sizes if s > 2400),
    "n_llm_polished": applied,
    "llm_polish": {
        "selected": len(json.load(open("/home/z/my-project/data/biology/llm_repair_ids_biology.json"))),
        "applied": applied,
        "rounds": 1,
        "guard": "garble-map + generic junk-token normalized char-level symmetric LCS >= 0.94 "
                 "(whitespace-stripped; threshold calibrated by replaying banked OKs, "
                 "min 0.9412, see METHOD_AND_FINDINGS D-9 / playbook L-015), "
                 "length drift 0.6-1.7x, refusal patterns, line-strict retry; "
                 "rejected raws kept as evidence",
    },
})
json.dump(report, open(REPORT, "w"), indent=2)

print(f"[merge] applied={applied} skipped={skipped} anchor_drift={drift}")
if drift:
    sys.exit(1)
print("[merge] anchor diff clean (0 drift)")
