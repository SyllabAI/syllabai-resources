#!/usr/bin/env python3
"""Refresh SME-ExamQuestion/manifest.json (registry) from per-course
manifests (scrape totals) + the sibling gap report (spec-index status).
Additive update: course entries keep their recon fields, gain/refresh
status, totals, spec_index."""
from __future__ import annotations

import json
import time
from pathlib import Path

CORPUS = Path("/home/z/my-project/download/syllabai-resources/SME-ExamQuestion")
GAP = Path("/home/z/my-project/.cache/sme_spcpt_sibling_report.json")

reg = json.loads((CORPUS / "manifest.json").read_text(encoding="utf-8"))
gap = json.loads(GAP.read_text(encoding="utf-8"))["courses"]

scraped = 0
with_idx = 0
for c in reg["courses"]:
    slug = c["slug"]
    mf = CORPUS / slug / "manifest.json"
    if mf.exists():
        m = json.loads(mf.read_text(encoding="utf-8"))
        t = m.get("totals") or {}
        c["status"] = "scraped"
        c["totals"] = {k: t.get(k) for k in
                       ("topics", "questions", "parts", "marks",
                        "assets", "asset_failures", "missing_questions",
                        "equations") if k in t}
        scraped += 1
    idx_path = CORPUS / slug / "spec_point_index.json"
    if idx_path.exists():
        idx_doc = json.loads(idx_path.read_text(encoding="utf-8"))
        cov = idx_doc["coverage"]
        g = gap.get(slug) or {}
        c["spec_index"] = {
            "schema": idx_doc["schema"],
            "source_pages": idx_doc.get("source_pages"),
            "spec_points": len(idx_doc["spec_points"]),
            "part_ids": cov["question_part_ids_total"],
            "covered": cov["covered_by_index"],
            "missing": len(cov["missing_from_index"]),
            "missing_resolved_in_sibling_trees":
                len(g.get("sibling_resolved_same_family", {})) +
                len(g.get("resolved_outside_family", {})),
            "missing_nowhere_corpus_wide":
                len(g.get("nowhere_corpus_wide",
                          cov["missing_from_index"])),
        }
        with_idx += 1

reg["generated_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
reg["scraped_courses"] = scraped
reg["spec_index_courses"] = with_idx

(CORPUS / "manifest.json").write_text(
    json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"registry refreshed: scraped {scraped}/{len(reg['courses'])}, "
      f"spec_index {with_idx}")
for c in reg["courses"][:2]:
    print(json.dumps(c, indent=1)[:400])
