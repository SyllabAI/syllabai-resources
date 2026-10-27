#!/usr/bin/env python3
"""Apply LLM polish results to YPH11 SB2 v1 JSONL (chemistry-style, in place):
text_original preserved, llm_repaired flag, char_count recomputed, markdown +
report regenerated. Serving-critical guarantee: id / unit_no / chapter_no /
content_type / pdf_pages / book_pages / section are NEVER touched; an
anchor-preservation diff against the pristine pre-polish snapshot is printed.
"""
import json, os, sys, collections

sys.path.insert(0, "/home/z/my-project/gh_repos/syllabai-resources/books/pearson-edexcel/international-a-level/chemistry/ych12/pipeline/scripts")
from book_structure_ych12 import BOOK_TITLE, BOOK_AUTHOR

# v2-lane convention (T-PARSE-YCH12-2): paths via env, defaults = v1
# (byte-proven unchanged). CLOBBER LAW: for a v2 merge, YCH12_CORPUS must be
# seeded from the v2 .pristine BEFORE this script runs — a landed/seeded
# corpus gets its text_original re-clobbered by the re-apply.
ZJSONL = os.environ.get("YCH12_CORPUS", "/home/z/my-project/data/ych12_sb2/out/edexcel_ial_chemistry_ych12_sb2_chunks_v1.jsonl")
PRISTINE = os.environ.get("YCH12_PRISTINE", "/home/z/my-project/data/ych12_sb2/out/edexcel_ial_chemistry_ych12_sb2_chunks_v1.pristine")
REPAIRS = os.environ.get("YCH12_REPAIRS", "/home/z/my-project/data/ych12_sb2/llm_repairs_ych12.jsonl")
MD_OUT = os.environ.get("YCH12_MD", "/home/z/my-project/data/ych12_sb2/out/full_book_docling.md")
REPORT = os.environ.get("YCH12_REPORT", "/home/z/my-project/data/ych12_sb2/out/parse_report_v1.json")
ANCHOR_KEYS = ("id", "unit_no", "chapter_no", "content_type",
               "pdf_pages", "book_pages", "section", "unit_name", "chapter_title")

repairs = {}
for line in open(REPAIRS, encoding="utf-8"):
    r = json.loads(line)
    repairs[r["id"]] = r  # latest wins

chunks = [json.loads(l) for l in open(ZJSONL, encoding="utf-8")]
applied = changed = 0
for c in chunks:
    r = repairs.get(c["id"])
    if r and r["status"] == "ok":
        c["text_original"] = c["text"]
        if r["text"] != c["text"]:
            c["text"] = r["text"]
            changed += 1
        c["char_count"] = len(c["text"])
        c["llm_repaired"] = True
        applied += 1

with open(ZJSONL, "w", encoding="utf-8") as f:
    for c in chunks:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")
print(f"chunks: {len(chunks)}  llm_repaired: {applied}  text changed: {changed}")

# ---- serving-critical: anchor fields identical to pristine snapshot ----
pre = {}
for line in open(PRISTINE, encoding="utf-8"):
    p = json.loads(line)
    pre[p["id"]] = p
anchor_drift = 0
for c in chunks:
    p = pre.get(c["id"])
    if p is None:
        anchor_drift += 1
        print(f"  ANCHOR MISSING PRISTINE: {c['id']}")
        continue
    for k in ANCHOR_KEYS:
        if c.get(k) != p.get(k):
            anchor_drift += 1
            print(f"  ANCHOR DRIFT {c['id']} field={k}: {p.get(k)!r} -> {c.get(k)!r}")
# no chunk created/lost
if set(pre) != {c["id"] for c in chunks}:
    anchor_drift += 1
    print("  ANCHOR DRIFT: chunk id set changed")
print(f"anchor check: {'PASS (0 drift)' if anchor_drift == 0 else f'FAIL ({anchor_drift})'}")

# ---- regenerate full markdown ----
md = [f"# {BOOK_TITLE} — {BOOK_AUTHOR}", ""]
last = None
for c in chunks:
    key = (c["unit_no"], c["chapter_no"])
    if key != last:
        if c["unit_no"]:
            md.append(f"\n## Topic {c['unit_no']}: {c['unit_name']}")
        md.append(f"\n### {c['chapter_title']}\n")
        last = key
    if c["section"] and c["text"].split("\n\n")[0] != c["section"]:
        md.append(f"\n#### {c['section']}")
    md.append(c["text"])
with open(MD_OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

# ---- refresh report ----
types = collections.Counter(c["content_type"] for c in chunks)
sizes = sorted(c["char_count"] for c in chunks)
rep = json.load(open(REPORT)) if os.path.exists(REPORT) else {}
rep.update({
    "n_chunks": len(chunks),
    "llm_polished": applied,
    "llm_polished_changed": changed,
    "content_types": dict(types),
    "size_min": sizes[0], "size_max": sizes[-1],
    "size_avg": round(sum(sizes) / len(sizes)),
})
json.dump(rep, open(REPORT, "w"), indent=2)
print("markdown + report regenerated")
print("ANCHOR_FAIL" if anchor_drift else "ANCHOR_PASS")
