#!/usr/bin/env python3
"""Apply LLM polish results to v3 JSONL: text_original preserved, llm_repaired
flag set, char_count recomputed, full markdown + report regenerated."""
import json, sys

sys.path.insert(0, "/home/z/my-project/scripts")
from book_structure import BOOK_TITLE

ZJSONL = "/home/z/my-project/download/rag_chemistry/edexcel_igcse_chemistry_chunks_v3.jsonl"
REPAIRS = "/home/z/my-project/data/llm_repairs_v3.jsonl"
MD_OUT = "/home/z/my-project/download/rag_chemistry/full_book_docling.md"
REPORT = "/home/z/my-project/download/rag_chemistry/parse_report_v3.json"

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

# regenerate full markdown
md = [f"# {BOOK_TITLE} — Jim Clark", ""]
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
with open(MD_OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

# refresh report
import collections
types = collections.Counter(c["content_type"] for c in chunks)
sizes = sorted(c["char_count"] for c in chunks)
rep = json.load(open(REPORT)) if __import__("os").path.exists(REPORT) else {}
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
