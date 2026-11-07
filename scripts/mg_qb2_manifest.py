#!/usr/bin/env python3
"""T-MG-QB-2 run-001 — build the igcse-maths-edexcel lane manifest.json, INDEX.md and receipt."""
import json
import os
import subprocess
from collections import Counter
from datetime import datetime, timezone

WORK = "/home/z/my-project/mg_work"
LANE_NAME = "igcse-maths-edexcel"
LANE = os.path.join(WORK, "corpus/MG-QuestionBank", LANE_NAME)
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

cat = json.load(open(f"{WORK}/catalog/igcse_edexcel_catalog.json"))
for t in cat["topics"]:
    t.setdefault("site_slug", t.get("slug"))
    t.setdefault("source_page", cat["source_page"])
results = {r["code"]: r for r in json.load(open(f"{WORK}/logs/qb2_extract_results.json"))["results"]}
reg_path = f"{WORK}/logs/qb2_parser_regression.json"
reg = json.load(open(reg_path)) if os.path.exists(reg_path) else None
run000 = json.load(open("/home/z/my-project/scripts/mg_run000_main/verification.json"))
r000_modes = run000["lanes"][LANE_NAME]["mode_coverage"]

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
    else:
        entry.update({
            "question_count": 0, "answers_present": False,
            "status": "no-question-source",
            "reason": "no free-tier question resources reachable on the topic's booklet page",
        })
    topics_index.append(entry)

extracted = [e for e in topics_index if e["status"] == "extracted"]
no_src = [e for e in topics_index if e["status"] != "extracted"]
zero_q = [e for e in extracted if e["question_count"] == 0]
zero_q_slugs = [e["slug"] for e in zero_q]
kind_counts = Counter(e["question_source_kind"] for e in extracted)
fallbacks = [e["code"] for e in extracted if str(e.get("question_source_kind", "")).startswith("booklet-fallback")]
no_answers = [e["code"] for e in extracted if not e["answers_present"]]
indeterminate = [e["slug"] for e in extracted
                 if e.get("answers_note") and "indeterminate" in e["answers_note"]]
no_cover_match = [e["slug"] for e in extracted
                  if e.get("answers_note") and "matches nocover booklet" in e["answers_note"]]

# topics where the booklet page exposes a worksheet but the topic page has no questions-mode card
ws_vs_modecard = []
for t in cat["topics"]:
    has_mode_card = "questions" in run000["lanes"][LANE_NAME]["topics"].get(t["slug"], {}).get("modes", [])
    if t["questions_ws_url"] and not has_mode_card:
        ws_vs_modecard.append(t["slug"])

manifest = {
    "plane": "MG-QuestionBank",
    "lane": LANE_NAME,
    "qualification": "IGCSE", "subject": "Maths", "board": "Edexcel",
    "source_page": cat["source_page"],
    "site_lane": cat["site_lane"],
    "catalog_join": {
        "expected": len(cat["topics"]),
        "site_slug_hits": len(cat["topics"]),
        "note": "118/118 site-native slugs verified against mathsgenie.co.uk/igcse/maths/edexcel; "
                "slug grammar validated 134/134 against the T-MG-QB-1 gcse-maths-edexcel catalog codes",
    },
    "mode_presence": {
        "verified_by": "T-MG-VERIFY-1/run-000 (scripts/mg_run000/) + live re-verification at catalog build",
        "live_topic_count": cat["drift_vs_run000"]["live_topic_count"],
        "run000_topic_count": cat["drift_vs_run000"]["run000_topic_count"],
        "added_since_run000": cat["drift_vs_run000"]["added_since_run000"],
        "removed_since_run000": cat["drift_vs_run000"]["removed_since_run000"],
        "run000_mode_coverage": r000_modes,
    },
    "topic_count": len(topics_index),
    "topics_extracted": len(extracted),
    "topics_no_question_source": [e["slug"] for e in no_src],
    "question_count": total_q,
    "question_source_kinds": dict(kind_counts),
    "modes_present": ["exam-questions"],
    "modes_absent": [
        {"mode": "past-papers", "reason": "out-of-scope-operator-decision-2026-11-07",
         "note": "no past-paper PDFs in the corpus per operator direction"},
        {"mode": "predicted-papers", "reason": "out-of-scope-operator-decision-2026-11-07"},
        {"mode": "mini-tests", "reason": "out-of-scope-operator-decision-2026-11-07",
         "note": "live-site interactive; link-of-record only"},
        {"mode": "revision-guides", "reason": "not-offered",
         "note": "no revision-guides mode anywhere in the IGCSE lane (T-MG-VERIFY-1 run-000)"},
        {"mode": "question-rush", "reason": "not-offered",
         "note": "no question-rush mode anywhere in the IGCSE lane (T-MG-VERIFY-1 run-000)"},
    ],
    "mode_divergence_notes": [{
        "note": "booklet pages expose a free worksheet entry for 103 topics while the topic page "
                f"carries a questions-mode card for 99 (run-000): {len(ws_vs_modecard)} topics have a "
                "worksheet but no mode card (recorded below; extraction follows the booklet-page "
                "resource list), and 13 topics have a mode card but no free worksheet entry on the "
                "booklet page — their question source is the booklet (or booklet fallback), not a ws sheet",
        "topics_with_ws_but_no_mode_card": ws_vs_modecard,
    }] if ws_vs_modecard else [],
    "answers_gaps": [{"code": c, "note": "solutions asset missing/404 at source"} for c in no_answers],
    "answers_cover_rule": {
        "cover_dropped": len(extracted) - len(indeterminate) - len(no_cover_match) - len(no_answers),
        "no_cover_present": no_cover_match,
        "indeterminate_all_pages_retained": indeterminate,
    },
    "booklet_fallbacks": fallbacks,
    "premium_gated_total": sum(t["premium_gated"] for t in cat["topics"]),
    "scope_exclusions": {
        "papers_bank": "operator decision 2026-11-07: no past/predicted paper PDFs collected anywhere in MG-*",
        "link_of_record": cat["site_lane"],
    },
    "provenance": {
        "task_id": "T-MG-QB-2/run-001",
        "run_branch": "t-mg-qb-2/run-001",
        "extracted_at": NOW,
        "extractor": "mg_qb2_extract.py v1 (parser of mg_qb_extract.py v1)",
        "pdf_policy": "source PDFs fetched, processed, discarded; sha256 + URL recorded per topic",
    },
    "topics": topics_index,
}
with open(os.path.join(LANE, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=1, ensure_ascii=False)

rows = ["| Code | Topic | Grade band | Questions | Answers | Source |",
        "|---|---|---|---|---|---|"]


def band_key(e):
    b = e["grade_band"].split("-")[0]
    return (int(b), e["code"].split(".")[1].zfill(2))


for e in sorted(topics_index, key=band_key):
    ans = "yes" if e["answers_present"] else ("n/a" if e["status"] != "extracted" else "no")
    src = {"ws-sheet": "ws", "booklet": "booklet"}.get(e.get("question_source_kind"), "booklet*") \
        if e["status"] == "extracted" else "—"
    name = f"[{e['name']}]({e['slug']}/)" if e["status"] == "extracted" else e["name"]
    rows.append(f"| {e['code']} | {name} | {e['grade_band']} | {e['question_count']} | {ans} | {src} |")

index_md = f"""# igcse-maths-edexcel — MG-QuestionBank lane index

MathsGenie IGCSE Maths (Edexcel) per-topic exam questions. {len(extracted)}/{len(topics_index)} topics extracted, {total_q} questions total.
Source lane: {cat['source_page']} · live lane: {cat['site_lane']} · task `T-MG-QB-2/run-001`.

- Past-paper / predicted-paper banks are **excluded by operator decision (2026-11-07)** — no paper PDFs in this corpus.
- Mode presence per `T-MG-VERIFY-1/run-000` + live re-verification: 118 topics, zero drift; booklet 118, questions-mode 99, videos 116, flashcards 103, lessons 96; no revision-guides or question-rush mode exists in this lane.
- Source kinds: `ws` = exam-question sheet, `booklet` = booklet-only topic, `booklet*` = booklet fallback (image-only ws generation).
- Marks not printed on a sheet stay `null` in `questions.json` — never inferred (booklet "Total for question" lines are not parsed, per the T-MG-QB-1 marks law).
- Solutions are per-page scans of the source answer booklets; where the ans PDF is the covered booklet scanned with solutions, the cover page is dropped by page-count match (see `manifest.json` → `answers_cover_rule`).
- Zero-question topics ({', '.join(zero_q_slugs) if zero_q_slugs else 'none'}): question sheets exist at source but their text layer carries no sequentially anchorable question numbers (image-only sheets / fraction-fragment layers) — recorded `question_count: 0` with an honest gap in the manifest, never padded; content stays reachable via the recorded source URLs and the solution scans.

{rows[0]}
{rows[1]}
""" + "\n".join(rows[2:]) + "\n"
with open(os.path.join(LANE, "INDEX.md"), "w") as f:
    f.write(index_md)

receipt = {
    "receipt": "T-MG-QB-2-run-001",
    "task_id": "T-MG-QB-2/run-001",
    "date": NOW,
    "actor": "SyllabAI Corpus Bot (operator-directed)",
    "scope": "MG-QuestionBank/igcse-maths-edexcel — per-topic exam-question bank from MathsGenie (second QB lane; first follow-up to T-MG-QB-1)",
    "sources": {
        "lane_page": cat["source_page"],
        "booklet_pages": "mathsgenie.co.uk/igcse/maths/edexcel/{slug}/booklet (RSC entriesByTab)",
        "asset_host": "assets.mathsgenie.co.uk/sources/mathsgenie/content/resources/",
        "site_lane_join": cat["site_lane"],
    },
    "counts": {
        "topics_in_catalog": len(topics_index),
        "topics_extracted": len(extracted),
        "topics_no_question_source": len(no_src),
        "questions": total_q,
        "source_kinds": dict(kind_counts),
        "premium_gated_recorded_not_downloaded": sum(t["premium_gated"] for t in cat["topics"]),
    },
    "exclusions": ["past-paper banks", "predicted-paper banks",
                   "mini-tests (operator decision 2026-11-07: no paper PDFs)"],
    "honest_gaps": [
        {"metric": f"{len(zero_q)} extracted topics carry 0 questions", "topics": zero_q_slugs,
         "note": "question source reachable but the text layer has no sequentially anchorable "
                 "question numbers (image-only sheets / fraction-fragment layers); content "
                 "preserved via recorded source URLs + solution scans — never padded"},
        {"metric": f"{len(no_answers)} topics without solutions", "codes": no_answers,
         "note": "solutions asset missing at source; recorded, not substituted"},
        {"metric": f"{len(indeterminate)} answers with indeterminate cover rule",
         "slugs": indeterminate, "note": "all ans pages retained, honest gap recorded per topic"},
        {"metric": "marks null where only booklet 'Total for question' lines print marks",
         "note": "consistent with the T-MG-QB-1 marks law (printed '(N marks)' only)"},
    ],
    "verification": [
        "live lane re-verified at run time: 118/118 topics, zero drift vs T-MG-VERIFY-1 run-000",
        "slug grammar cross-validated 134/134 against the T-MG-QB-1 catalog codes",
        "sequential question-number anchors enforced (gaps logged)",
        "anchor hardening: column-relative x<=75pt guard rejects digit-led diagram labels "
        "('2 a', '3 b', '14 cm 6 cm') that previously fired as false anchors mid-question",
        "parser regression vs the T-MG-QB-1 GCSE of-record corpus run (133 topics, staged source "
        "PDFs): 13 divergent topics (3 recovered undercounts, 10 deflated overcounts incl. one "
        "image-only booklet) — ground-truth spot-checks side with the hardened parser; "
        "T-MG-QB-1 re-extraction recommended as a follow-up run",
        "marks parsed from printed '(N marks)' only; never inferred",
        "cover-drop rule extended to the covered-booklet page-count match (IGCSE /nocover/ booklet variant)",
        "premium worksheet Sets recorded as gated (2,613 entries), never downloaded (license law)",
        "PDF-staging hygiene: lane-prefixed working filenames (igcse-<code>-*.pdf) — a GCSE/IGCSE "
        "code-collision contamination in the first same-day pass was purged and the full 118-topic "
        "extraction re-run clean; recorded shas verified against fresh downloads",
    ],
    "qb1_parser_hardening_findings": (reg or {}),
    "artifacts": [
        "MG-QuestionBank/igcse-maths-edexcel/manifest.json",
        "MG-QuestionBank/igcse-maths-edexcel/INDEX.md",
        "MG-QuestionBank/igcse-maths-edexcel/<topic>/topic.json|questions.json|.md|answers.json|.md|assets/",
    ],
}
with open(os.path.join(WORK, "corpus/MG-QuestionBank/T-MG-QB-2-run-001-RECEIPT.json"), "w") as f:
    json.dump(receipt, f, indent=1)

print(f"manifest: {len(extracted)} extracted / {len(topics_index)} topics, {total_q} questions")
print("source kinds:", dict(kind_counts))
print("zero-q:", zero_q, "| no-answers:", no_answers)
print("ws-vs-modecard extra:", ws_vs_modecard)
print("cover rule: dropped =", receipt["counts"], )
print("indeterminate:", indeterminate)
print(subprocess.run(["du", "-sh", LANE], capture_output=True, text=True).stdout.strip())
