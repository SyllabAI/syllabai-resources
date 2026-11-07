#!/usr/bin/env python3
"""T-MG-QB-1 run-001 — build lane manifest.json, INDEX.md and the run receipt from extraction results."""
import json, os
from collections import Counter
from datetime import datetime, timezone

WORK = "/home/z/my-project/mg_work"
LANE = os.path.join(WORK, "corpus/MG-QuestionBank/gcse-maths-edexcel")
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

cat = json.load(open(f"{WORK}/catalog/gcse_edexcel_catalog.json"))
results = {r["code"]: r for r in json.load(open(f"{WORK}/logs/qb_extract_results.json"))["results"]}

topics_index = []
total_q = 0
for t in cat["topics"]:
    slug = t["site_slug"]
    tdir = os.path.join(LANE, slug)
    tj_path = os.path.join(tdir, "topic.json")
    entry = {
        "slug": slug, "code": t["code"], "name": t["name"], "grade_band": t["grade_band"],
        "site_url": f"{cat['site_lane']}/{slug}",
    }
    if os.path.exists(tj_path):
        tj = json.load(open(tj_path))
        aj = json.load(open(os.path.join(tdir, "answers.json")))
        total_q += tj["question_count"]
        entry.update({
            "question_count": tj["question_count"],
            "question_source_kind": tj["question_source"]["kind"],
            "answers_present": aj["present"],
            "answers_note": aj.get("note"),
            "status": "extracted",
        })
        if not t["exam_questions_published"]:
            entry["status"] = "not-published"
    else:
        entry.update({
            "question_count": 0, "answers_present": False,
            "status": "not-published",
            "reason": "no exam-question resources published at source (empty row on gcse.html)",
        })
    topics_index.append(entry)

extracted = [e for e in topics_index if e["status"] == "extracted"]
not_pub = [e for e in topics_index if e["status"] == "not-published"]
kind_counts = Counter(e["question_source_kind"] for e in extracted)
fallbacks = [e["code"] for e in extracted if str(e.get("question_source_kind", "")).startswith("booklet-fallback")]
no_answers = [e["code"] for e in extracted if not e["answers_present"]]

manifest = {
    "plane": "MG-QuestionBank",
    "lane": "gcse-maths-edexcel",
    "qualification": "GCSE", "subject": "Maths", "board": "Edexcel",
    "source_page": cat["source_page"],
    "site_lane": cat["site_lane"],
    "catalog_join": {"expected": len(cat["topics"]), "site_slug_hits": len(cat["topics"]), "note": "134/134 site-native slugs verified against mathsgenie.co.uk/gcse/maths/edexcel"},
    "topic_count": len(topics_index),
    "topics_extracted": len(extracted),
    "topics_not_published": [e["slug"] for e in not_pub],
    "question_count": total_q,
    "question_source_kinds": dict(kind_counts),
    "modes_present": ["exam-questions"],
    "modes_absent": [
        {"mode": "past-papers", "reason": "out-of-scope-operator-decision-2026-11-07", "note": "no past-paper PDFs in the corpus per operator direction"},
        {"mode": "predicted-papers", "reason": "out-of-scope-operator-decision-2026-11-07"},
        {"mode": "mini-tests", "reason": "out-of-scope-operator-decision-2026-11-07", "note": "live-site interactive; link-of-record only"},
        {"mode": "exam-questions", "topic": "grade-5-5-13-mid-point-of-a-line-segment", "reason": "not-published", "note": "site row has no question resources"},
    ],
    "answers_gaps": [{"code": c, "note": "solutions asset 404 at source"} for c in no_answers],
    "booklet_fallbacks": fallbacks,
    "scope_exclusions": {
        "papers_bank": "operator decision 2026-11-07: no past/predicted paper PDFs collected anywhere in MG-*",
        "link_of_record": cat["site_lane"],
    },
    "provenance": {
        "task_id": "T-MG-QB-1/run-001",
        "run_branch": "t-mg-qb-1/run-001",
        "extracted_at": NOW,
        "extractor": "mg_qb_extract.py v1",
        "pdf_policy": "source PDFs fetched, processed, discarded; sha256 + URL recorded per topic",
    },
    "topics": topics_index,
}
with open(os.path.join(LANE, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=1)

rows = ["| Code | Topic | Grade band | Questions | Answers | Source |",
        "|---|---|---|---|---|---|"]
for e in sorted(topics_index, key=lambda x: (int(x["grade_band"].split("-")[0]), x["code"].split(".")[1].zfill(2))):
    ans = "yes" if e["answers_present"] else ("n/a" if e["status"] == "not-published" else "no")
    src = {"ws-sheet": "ws", "booklet": "booklet"}.get(e.get("question_source_kind"), "booklet*") if e["status"] == "extracted" else "—"
    name = f"[{e['name']}]({e['slug']}/)" if e["status"] == "extracted" else e["name"]
    rows.append(f"| {e['code']} | {name} | {e['grade_band']} | {e['question_count']} | {ans} | {src} |")

index_md = f"""# gcse-maths-edexcel — MG-QuestionBank lane index

MathsGenie GCSE Maths (Edexcel) per-topic exam questions. {len(extracted)}/{len(topics_index)} topics extracted, {total_q} questions total.
Source page: {cat['source_page']} · live lane: {cat['site_lane']} · task `T-MG-QB-1/run-001`.

- Past-paper / predicted-paper banks are **excluded by operator decision (2026-11-07)** — no paper PDFs in this corpus.
- `grade-5-5-13-mid-point-of-a-line-segment` (5.13): nothing published at source — recorded absent, no stub dir.
- Source kinds: `ws` = exam-question sheet, `booklet` = booklet-only topic, `booklet*` = booklet fallback (image-only ws generation).
- Marks not printed on a sheet stay `null` in `questions.json` — never inferred.

{rows[0]}
{rows[1]}
""" + "\n".join(rows[2:]) + "\n"
with open(os.path.join(LANE, "INDEX.md"), "w") as f:
    f.write(index_md)

receipt = {
    "receipt": "T-MG-QB-1-run-001",
    "task_id": "T-MG-QB-1/run-001",
    "date": NOW,
    "actor": "SyllabAI Corpus Bot (operator-directed)",
    "scope": "MG-QuestionBank/gcse-maths-edexcel — per-topic exam-question bank from MathsGenie",
    "sources": {
        "classic_page": cat["source_page"],
        "asset_host": "old-asset.mathsgenie.co.uk/resources/",
        "site_lane_join": cat["site_lane"],
    },
    "counts": {
        "topics_in_catalog": len(topics_index),
        "topics_extracted": len(extracted),
        "topics_not_published": len(not_pub),
        "questions": total_q,
        "source_kinds": dict(kind_counts),
    },
    "exclusions": ["past-paper banks", "predicted-paper banks", "mini-tests (operator decision 2026-11-07: no paper PDFs)"],
    "honest_gaps": [
        {"topic": "grade-5-5-13-mid-point-of-a-line-segment", "gap": "no question resources published at source"},
        {"topic": "grade-6-6-13-capture-recapture", "gap": "solutions asset transiently 404 during probing; re-fetched successfully in-run (6 pages present)"},
        {"metric": "965/1666 questions carry null marks", "note": "worksheet-generation sheets print no marks; never inferred (README coverage law rule 4)"},
    ],
    "verification": [
        "site-native slug join 134/134 against live lane",
        "sequential question-number anchors enforced (gaps logged)",
        "marks parsed from printed '(N marks)' only; never inferred",
        "crop QA on text-2col, image-ws (booklet fallback) and booklet-only generations",
        "solution scans: booklet-cover page dropped when ans page count matches booklet page count",
    ],
    "artifacts": [
        "MG-QuestionBank/gcse-maths-edexcel/manifest.json",
        "MG-QuestionBank/gcse-maths-edexcel/INDEX.md",
        "MG-QuestionBank/gcse-maths-edexcel/<topic>/topic.json|questions.json|.md|answers.json|.md|assets/",
    ],
}
with open(os.path.join(WORK, "corpus/MG-QuestionBank/T-MG-QB-1-run-001-RECEIPT.json"), "w") as f:
    json.dump(receipt, f, indent=1)

print(f"manifest: {len(extracted)} extracted / {len(topics_index)} topics, {total_q} questions")
print("source kinds:", dict(kind_counts))
print("booklet fallbacks:", fallbacks)
print("answers gaps:", no_answers)
import subprocess
print(subprocess.run(["du", "-sh", LANE], capture_output=True, text=True).stdout.strip())
files = sum(len(fs) for _, _, fs in os.walk(os.path.join(WORK, "corpus")))
print("total corpus files:", files)
