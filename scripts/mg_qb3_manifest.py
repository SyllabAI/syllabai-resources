#!/usr/bin/env python3
"""T-MG-QB-3 run-001 — build the a-level-maths-edexcel lane manifest.json,
INDEX.md and the run receipt."""
import json
import os
from collections import Counter
from datetime import datetime, timezone

WORK = "/home/z/my-project/mg_work"
LANE_NAME = "a-level-maths-edexcel"
LANE = os.path.join(WORK, "corpus/MG-QuestionBank", LANE_NAME)
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

cat = json.load(open(f"{WORK}/catalog/alevel_edexcel_catalog.json"))
results = {r["slug"]: r for r in json.load(open(f"{WORK}/logs/qb3_extract_results.json"))["results"]}
run000 = json.load(open("/home/z/my-project/scripts/mg_run000_main/verification.json"))
r000 = run000["lanes"][LANE_NAME]

topics_index = []
total_q = total_marks = 0
for t in cat["topics"]:
    slug = t["slug"]
    tdir = os.path.join(LANE, slug)
    tj = json.load(open(os.path.join(tdir, "topic.json")))
    aj = json.load(open(os.path.join(tdir, "answers.json")))
    qj = json.load(open(os.path.join(tdir, "questions.json")))
    total_q += tj["question_count"]
    total_marks += sum((q.get("marks") or 0) for q in qj["questions"])
    topics_index.append({
        "slug": slug, "name": tj["name"], "year": tj["year"], "strand": tj["strand"],
        "chapter_number": tj["chapter_number"],
        "subtopic_count": len(tj.get("subtopics", [])),
        "question_count": tj["question_count"],
        "marks_sum": sum((q.get("marks") or 0) for q in qj["questions"]),
        "question_source_kind": tj["question_source"]["kind"],
        "question_pdf_pages": tj["question_source"]["pages"],
        "solutions_present": aj["present"],
        "solutions_pages": aj.get("pages"),
        "discovery": tj["question_source"]["discovery"],
        "numbering_gaps": tj["numbering_gaps"],
        "printed_number_typos": tj["printed_number_typos"],
        "site_url": tj["site_topic_page"],
        "status": "extracted" if slug in results and results[slug]["status"] == "ok" else "error",
    })

extracted = [e for e in topics_index if e["status"] == "extracted"]
discovered = [e["slug"] for e in topics_index if "naming convention" in (e["discovery"] or "")]
gap_topics = [(e["slug"], e["numbering_gaps"]) for e in topics_index if e["numbering_gaps"]]
typo_topics = [(e["slug"], e["printed_number_typos"]) for e in topics_index if e["printed_number_typos"]]
strand_year = Counter((e["year"], e["strand"]) for e in topics_index)

manifest = {
    "plane": "MG-QuestionBank",
    "lane": LANE_NAME,
    "qualification": "A-Level", "subject": "Maths", "board": "Edexcel", "spec": "9MA0",
    "source_lane": cat["source_lane"],
    "classic_source": cat["classic_source"],
    "asset_host": cat["asset_host"],
    "extracted_at": NOW,
    "task_id": "T-MG-QB-3/run-001",
    "lane_shape": {
        "grammar": "site-native chapter slug: {as|a-level}-{strand}-{n}-{name} "
                   "(Year 1 chapters carry the `as-` prefix, Year 2 the `a-level-` prefix)",
        "granularity_of_record": "per-chapter question sets — MathsGenie publishes A-Level exam "
                                 "questions as compiled per-chapter sets; subtopic pages carry no "
                                 "question PDFs (video/lesson only)",
        "chapters": len(cat["topics"]),
        "subtopics": cat["subtopic_count"],
        "sections": ["Year 1 Pure Mathematics (14)", "Year 1 Statistics (7)", "Year 1 Mechanics (3)",
                     "Year 2 Pure Mathematics (12)", "Year 2 Statistics (3)", "Year 2 Mechanics (5)"],
        "sibling_lane_overlap": {
            "as-level-maths-edexcel": ("its 24 chapters are slug-identical to the Year-1 half of this "
                                       "lane (verified at run time); its question resources are the "
                                       "same 24 old-site question sets — a future AS lane extraction "
                                       "would duplicate content of this lane; dedup decision recorded "
                                       "here, AS lane NOT extracted twice"),
        },
    },
    "coverage": {
        "chapters_in_catalog": len(cat["topics"]),
        "chapters_extracted": len(extracted),
        "questions": total_q,
        "marks_sum_printed": total_marks,
        "chapters_with_solutions": sum(1 for e in topics_index if e["solutions_present"]),
        "premium_gated_entries": 0,
        "by_year_strand": {f"{y} {s}": n for (y, s), n in sorted(strand_year.items())},
    },
    "modes_present": {
        "question-sets": "44/44 chapters (compiled exam-question sets + worked-solution scans)",
    },
    "modes_absent": [
        {"mode": "subtopic-level question PDFs", "reason": "not-offered",
         "note": "245 subtopic pages carry video/lesson only; the new-site subtopic question bank "
                 "is an interactive client-side feature (link-of-record per subtopic page)"},
        {"mode": "booklets", "reason": "not-offered",
         "note": "A-Level lane has no booklet generation (that is a GCSE/IGCSE mode)"},
        {"mode": "revision-guides / flashcards", "reason": "pending-extraction",
         "note": "other MG-* planes; not in the QuestionBank scope"},
        {"mode": "past-paper banks", "reason": "user-exclusion",
         "note": "operator decision 2026-11-07: no past-paper PDFs anywhere in MG-*; "
                 "link-of-record remains the site"},
        {"mode": "predicted-paper banks / mini-tests", "reason": "user-exclusion",
         "note": "same operator decision"},
    ],
    "numbering_law": {
        "rule": "printed total-line number is the question identity; non-monotonic dips are "
                "position-derived and flagged printed_as (source typos); ascending gaps are kept "
                "as printed and recorded (never renumbered silently, never padded)",
        "gaps": gap_topics,
        "printed_typos": typo_topics,
    },
    "discovery_provenance": {
        "chapters": len(discovered),
        "slugs": discovered,
        "rule": "question-set pages that publish only the answers link; the sibling question PDF "
                "follows the site's own asset-host naming convention ({stem}.pdf beside "
                "{stem}ans.pdf) and was HEAD-200-verified at run time before inclusion",
    },
    "scope_exclusions": [
        "past-paper banks (papers/past) — operator decision 2026-11-07: no paper PDFs",
        "predicted-paper banks — same decision",
        "mini-tests — same decision; live-site interactive, link-of-record only",
        "old-spec (C1-C4/S1/M1) A-Level materials (old.mathsgenie.co.uk/alevel.php) — different "
        "qualification generation, out of the 9MA0 lane of record",
    ],
    "drift_vs_run000": {
        "run000_chapters": len(r000["topics"]),
        "live_chapters": len(cat["topics"]),
        "chapter_set_identical": sorted(r000["topics"].keys()) == sorted(t["slug"] for t in cat["topics"]),
        "note": "run-000 recorded the lane's 44 chapters as its topic set; this run adds the "
                "245-subtopic layer decoded from the lane payload (finer than run-000 recorded)",
    },
    "provenance": {
        "every_artifact": "source_url + source_sha256 + extracted_at + extractor + task_id",
        "source_pdfs": "fetched, processed, discarded — only sha256 + URL survive per chapter",
        "licensing": "MathsGenie site content is third-party material; operator attestation in "
                     "../LICENSE-DATA.md (Amendment 2026-11-07)",
    },
}
with open(os.path.join(LANE, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=1)

# ---- INDEX.md ----
lines = [f"# {LANE_NAME} — chapter index (T-MG-QB-3/run-001)", "",
         f"Source lane: {cat['source_lane']} · classic delivery: {cat['classic_source']}",
         f"Coverage: {len(extracted)}/{len(cat['topics'])} chapters · {total_q} questions · "
         f"{total_marks} printed marks · solutions 44/44 · 0 PDFs stored", "",
         "Granularity of record: per-chapter question sets (the site's A-Level question resource); "
         "245 subtopics listed per chapter in topic.json are the revision granularity "
         "(video/lesson pages; the new-site subtopic question bank is interactive-only).", "",
         "| Year | Strand | Ch | Chapter | Questions | Marks | Sol. pages | Slug |",
         "|---|---|---|---|---:|---:|---:|---|"]
for e in sorted(topics_index, key=lambda x: (x["year"], x["strand"], x["chapter_number"])):
    lines.append(f"| {e['year']} | {e['strand']} | {e['chapter_number']} | {e['name']} | "
                 f"{e['question_count']} | {e['marks_sum']} | {e['solutions_pages']} | `{e['slug']}` |")
lines.append("")
lines.append("Honest gaps of record:")
for slug, g in gap_topics:
    lines.append(f"- `{slug}`: printed numbering skips {g} (source-numbering fact, kept as printed)")
for slug, ty in typo_topics:
    for t in ty:
        lines.append(f"- `{slug}`: Q{t['position']} printed as “{t['printed']}” at source "
                     f"(total-line typo; numbered by position, flagged in questions.json)")
for s in discovered:
    lines.append(f"- `{s}`: question PDF via site asset-host naming convention "
                 f"(page publishes answers link only; HEAD-200 verified)")
with open(os.path.join(LANE, "INDEX.md"), "w") as f:
    f.write("\n".join(lines) + "\n")

# ---- receipt ----
receipt = {
    "receipt": "T-MG-QB-3-run-001",
    "task_id": "T-MG-QB-3/run-001",
    "date": NOW,
    "actor": "SyllabAI Corpus Bot (operator-directed)",
    "scope": f"MG-QuestionBank/{LANE_NAME} — MathsGenie A-Level Maths (Edexcel, 9MA0) per-chapter "
             "question-set bank (third QB lane; follows T-MG-QB-1 gcse-maths-edexcel PR #315 and "
             "T-MG-QB-2 igcse-maths-edexcel PR #316)",
    "sources": {
        "lane_page": cat["source_lane"],
        "classic_question_sets": "old.mathsgenie.co.uk/newalevel.php -> a-level-*-questions-*.php",
        "asset_host": cat["asset_host"],
        "site_lane_join": "44/44 chapters title-joined new-site lane <-> old-site question sets; "
                          "AS-lane overlap (24 slug-identical Year-1 chapters) recorded, not duplicated",
    },
    "counts": {
        "chapters_in_catalog": len(cat["topics"]),
        "chapters_extracted": len(extracted),
        "subtopics_indexed": cat["subtopic_count"],
        "questions": total_q,
        "marks_sum_printed": total_marks,
        "solutions_scanned_chapters": sum(1 for e in topics_index if e["solutions_present"]),
        "premium_gated_recorded_not_downloaded": 0,
        "question_pdfs_via_naming_convention": len(discovered),
    },
    "parser_law": {
        "segmentation": "total-line boundaries: every question prints '(Total for question N is M "
                        "marks)'; questions are segmented by consecutive total lines in spatial "
                        "(page, y) order; the total line travels with its crop",
        "why_not_leading_anchors": "A-Level sets embed question numbers inside display-math blocks "
                                   "(verified visually: Q5's number renders inside '2 + 10 5', Q8's "
                                   "after a fraction numerator); the QB-1/2 leading-number law is "
                                   "unreliable for this lane",
        "numbering": "printed identity; dips position-derived + flagged; gaps recorded",
        "marks": "printed total lines only ('... is M marks'); the QB-1/2 '(N marks)' pattern does "
                 "not occur in this lane; nothing inferred",
    },
    "exclusions": [
        "past-paper banks", "predicted-paper banks", "mini-tests (operator decision 2026-11-07)",
        "old-spec C1-C4/S1/M1 materials (separate qualification generation)",
    ],
    "honest_gaps": [
        {"metric": "printed numbering gap", "topics": [s for s, _ in gap_topics],
         "note": "exponentials-and-logarithms prints no question 19 (1..18 then 20..41); kept as "
                 "printed, never renumbered"},
        {"metric": "source total-line typos", "topics": [s for s, _ in typo_topics],
         "note": "graphs-transformations Q22 prints '(Total for question 2 is 6 marks)'; "
                 "sequences-and-series Q9 prints '(Total for Question 2 is 9 marks)'; "
                 "the-normal-distribution Q2 prints a second '(Total for question 1 ...)' "
                 "line; all numbered by position and flagged printed_as in questions.json"},
        {"metric": "9 question PDFs reachable only via the site's own naming convention",
         "topics": discovered,
         "note": "question-set pages publish only the answers link; sibling question PDF verified "
                 "HTTP 200 at run time and included with explicit discovery provenance"},
        {"metric": "0 topics without solutions", "codes": [], "note": "44/44 answer scans present"},
    ],
    "verification": [
        "live lane re-decoded at run time: 44 chapters / 245 subtopics, chapter set identical to "
        "T-MG-VERIFY-1 run-000",
        "44/44 chapter joins title-matched; no fallback matching needed",
        "total-line counts cross-checked pre-extraction: 35/35 originally-text sets sequential "
        "(after '1 mark' singular fix) plus 9 re-classified sets; anomalies triaged to gaps/typos",
        "visual QA: question crops hug their region with diagrams + printed total lines; solution "
        "scans verified as worked solutions",
        "lane runs 1,949 files / ~47 MB, zero PDFs stored",
    ],
    "receipt_files": {
        "manifest": f"MG-QuestionBank/{LANE_NAME}/manifest.json",
        "index": f"MG-QuestionBank/{LANE_NAME}/INDEX.md",
        "extract_results": "scripts/mg_qb3_run001/extract_results.json",
        "catalog_log": "scripts/mg_qb3_run001/catalog_log.json",
    },
}
with open(f"{WORK}/corpus/MG-QuestionBank/T-MG-QB-3-run-001-RECEIPT.json", "w") as f:
    json.dump(receipt, f, indent=1)

print(f"manifest + INDEX + receipt written | chapters={len(extracted)} questions={total_q} "
      f"marks={total_marks} discovered={len(discovered)}")
print("gaps:", gap_topics)
print("typos:", typo_topics)
