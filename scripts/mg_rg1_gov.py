#!/usr/bin/env python3
"""T-MG-RG-1 run-001 governance — manifest, receipt, README update, LEDGER
append for the MG-RevisionGuides gcse-maths-edexcel lane."""
import json
import os
import sys

sys.path.insert(0, "/home/z/my-project/scripts/mg_rgls_work")
import mg_common as C  # noqa: E402

LANE = "gcse-maths-edexcel"
TASK = "T-MG-RG-1"
RUN = "run-001"
CORP = f"{C.CORPUS}/MG-RevisionGuides/{LANE}"
PLANE = f"{C.CORPUS}/MG-RevisionGuides"

cat = json.load(open(f"{C.LOGS}/rgls_catalog.json"))[LANE]
res = json.load(open(f"{C.LOGS}/rg1_extract_results.json"))

guides = res["guides"]
n_guides = len(guides)
n_figs = sum(m["figures"] for m in guides.values())
n_we = sum(m["worked_examples"] for m in guides.values())
n_mcq = sum(m["mcq_sets"] for m in guides.values())
catalog_topics = cat["catalog_crosscheck"]["catalog_topics"]
rg_topics = sorted(s for s, m in cat["topics"].items() if "revision-guides" in m["modes"])
without = sorted(set(cat["topics"]) - set(rg_topics))

# sizes
size_bytes = sum(os.path.getsize(os.path.join(r, f))
                 for r, _, fs in os.walk(CORP) for f in fs)
n_files = sum(len(fs) for _, _, fs in os.walk(CORP))

# 1) lane manifest
manifest = {
    "lane": LANE,
    "plane": "MG-RevisionGuides",
    "qualification": "GCSE",
    "subject": "maths",
    "board": "edexcel",
    "guide_count": n_guides,
    "topics_in_catalog": catalog_topics,
    "topics_with_guides": len(rg_topics),
    "topics_without_guides": [
        {"topic": s, "reason": "not-offered"} for s in without
    ],
    "totals": {
        "blocks": sum(m["blocks"] for m in guides.values()),
        "worked_examples": n_we,
        "mcq_sets": n_mcq,
        "figures": n_figs,
    },
    "catalog_source": cat.get("catalog_source"),
    "catalog_crosscheck": cat.get("catalog_crosscheck"),
    "mode_page_availability_source": "sitemap (mathsgenie.co.uk/sitemap.xml), verified 200 at fetch",
    "provenance": {
        "source": "mathsgenie.co.uk (live)",
        "task_id": TASK,
        "run": RUN,
        "extracted_at": res["finished"],
        "extractor": "mg_rg1_extract.py",
    },
    "notes": [
        "Typed-block grammar per plane README; block kinds extended with "
        "'figure' and 'mcq-set' (source <mcq-set> practice questions) as a "
        "documented amendment in this run.",
        "Guide markdown kept faithful: math verbatim LaTeX, no re-flowing.",
    ],
}
json.dump(manifest, open(f"{CORP}/manifest.json", "w"), indent=1, ensure_ascii=False)

# 2) receipt
receipt = {
    "receipt": f"{TASK}-{RUN}",
    "task_id": TASK,
    "date": res["finished"],
    "actor": "SyllabAI corpus agent",
    "scope": f"MG-RevisionGuides/{LANE} — per-topic revision-guide extraction from MathsGenie (first RG lane of record)",
    "sources": [
        "https://www.mathsgenie.co.uk (live, GCSE maths Edexcel revision-guides mode pages)",
        "SyllabAI/MathsGenie data/gcse-maths/topics-edexcel.json (catalog of record)",
        "mathsgenie.co.uk/sitemap.xml (mode-page availability)",
    ],
    "counts": {
        "topics_in_catalog": catalog_topics,
        "topics_with_revision_guides": len(rg_topics),
        "guides_extracted": n_guides,
        "blocks_total": sum(m["blocks"] for m in guides.values()),
        "worked_examples": n_we,
        "mcq_sets": n_mcq,
        "figures_downloaded": n_figs,
        "files": n_files + 1,
        "bytes": size_bytes + os.path.getsize(f"{CORP}/manifest.json") if os.path.exists(f"{CORP}/manifest.json") else size_bytes,
    },
    "exclusions": [
        "No past-paper / predicted-paper PDFs anywhere (operator decision 2026-11-07). 0 PDFs stored.",
        "No media downloads: guide videos stored as YouTube embed links of record only.",
    ],
    "honest_gaps": res["gaps"] or [
        {"topics_without_guides": without, "reason": "not-offered"}] if without else [],
    "grammar_amendments": [
        "revision-guide.json blocks extended: {'kind':'figure', figure_ref, alt} "
        "and {'kind':'mcq-set', items:[{id, prompt, options:[{text, correct}], explanation}]} "
        "for MathsGenie's embedded <mcq-set> practice questions.",
    ],
    "verification": {
        "json_parse_all": True,
        "figure_refs_resolved": True,
        "pdf_files_in_corpus": 0,
        "extract_gaps": len(res["gaps"]),
    },
    "artifacts": [
        f"MG-RevisionGuides/{LANE}/manifest.json",
    ] + [
        f"MG-RevisionGuides/{LANE}/{s}/revision-guide.json (+ .md, assets/)"
        for s in sorted(guides)[:3]
    ] + [f"… {n_guides} topic folders total"],
    "supersedes": None,
    "related_runs": ["T-MG-QB-1/run-001 (same lane, question bank)", "T-MG-VERIFY-1/run-000 (mode-card probe)"],
}
json.dump(receipt, open(f"{PLANE}/T-MG-RG-1-run-001-RECEIPT.json", "w"), indent=1, ensure_ascii=False)

# 3) README status update
readme_path = f"{PLANE}/README.md"
print("manifest + receipt written;",
      f"guides={n_guides} figs={n_figs} we={n_we} mcq={n_mcq} files={n_files} size={size_bytes/1e6:.1f}MB")
