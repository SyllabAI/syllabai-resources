#!/usr/bin/env python3
"""Merge LLM fidelity repairs into v2 JSONL; re-render markdown reading copy."""
import json

V2 = "/home/z/my-project/download/rag_chemistry/edexcel_igcse_chemistry_chunks_v2.jsonl"
REPAIRS = "/home/z/my-project/data/llm_repairs.jsonl"
MD_OUT = "/home/z/my-project/download/rag_chemistry/full_book_clean_v2.md"

repairs = {}
for src in ("/home/z/my-project/data/llm_repairs_round1.jsonl",
            "/home/z/my-project/data/llm_repairs.jsonl"):
    try:
        for line in open(src, encoding="utf-8"):
            r = json.loads(line)
            if r["status"] == "ok":
                repairs[r["id"]] = r["text"]   # later rounds overwrite
    except FileNotFoundError:
        pass

applied = 0
chunks = []
for line in open(V2, encoding="utf-8"):
    c = json.loads(line)
    if c["id"] in repairs:
        fixed = repairs[c["id"]].strip()
        # breadcrumb is the first line up to first blank line
        br_end = c["text"].find("\n\n")
        breadcrumb = c["text"][:br_end] if c["text"].startswith("[") and br_end > 0 else ""
        c["text_original"] = c["text"]          # pre-LLM (mechanical) version
        c["text"] = f"{breadcrumb}\n\n{fixed}" if breadcrumb else fixed
        c["llm_repaired"] = True
        applied += 1
    chunks.append(c)

with open(V2, "w", encoding="utf-8") as f:
    for c in chunks:
        f.write(json.dumps(c, ensure_ascii=False) + "\n")
print(f"chunks: {len(chunks)} | LLM repairs applied: {applied}")

# --- re-render markdown reading copy from final chunks ---
md = ["# Edexcel International GCSE (9-1) Chemistry Student Book - RAG corpus (v2)", "",
      "*Repaired text: mechanical OCR fixes + LLM fidelity pass on corrupted chunks. "
      "Original pre-repair text preserved per chunk in the JSONL (`text_original`).*", ""]
last_unit, last_chap = object(), object()
for c in chunks:
    md_meta = c["metadata"]
    if md_meta.get("unit_no") != last_unit and md_meta.get("unit_name"):
        md += [f"## Unit {md_meta['unit_no']}: {md_meta['unit_name']}", ""]
        last_unit = md_meta["unit_no"]
        last_chap = object()
    if md_meta.get("chapter_no") != last_chap and md_meta.get("chapter_no"):
        md += [f"### Chapter {md_meta['chapter_no']}: {md_meta['chapter_title']}", ""]
        last_chap = md_meta["chapter_no"]
    elif not md_meta.get("chapter_no") and last_chap is not None and md_meta.get("chapter_title"):
        if md_meta["chapter_title"] != getattr(last_chap, "__str__", lambda: "")():
            pass
    body = c["text"]
    br_end = body.find("\n\n")
    if body.startswith("[") and br_end > 0:
        body = body[br_end + 2:]
    md += [f"*{c['id']} | {md_meta['content_type']}*",
           "", body.replace("\n", "  \n"), ""]
with open(MD_OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(md))
print("markdown ->", MD_OUT)
