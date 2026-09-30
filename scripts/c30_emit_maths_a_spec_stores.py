#!/usr/bin/env python3
"""T-C30 — c30_emit_maths_a_spec_stores.py

K1 of the C28 per-subject commissioning playbook (spec §6) for igcse-maths-a
(4MA1, Maths A Higher — the operator's D4 selection, K0/T-C29 commissioned):
emit the 5 spec-text ratified stores from the canonical PDF-direct parse:

    graph/igcse-maths-a/specification_points.yaml
    graph/igcse-maths-a/topics.yaml
    graph/igcse-maths-a/practicals.yaml
    graph/igcse-maths-a/assessment_objectives.yaml
    graph/igcse-maths-a/command_words.yaml

c23-pattern (T-C23/T-C26 precedents): canonical JSON is the sole content
source; wording is verbatim (whitespace-normalised only); damage is preserved
and flagged, never fixed; explicit meta/lineage per row (no dict(old_meta)
inheritance — the C26 root-cause rule); fail-closed pre/post conditions;
deterministic (GENERATED constant, no wall-clock); byte-identical re-runs.

THE TIER-DEDUPE RULE (recorded in meta.tier_dedupe + the C30 ledger; this is
the one semantics decision this emitter makes, everything else is verbatim):

  The 4MA1 specification presents its content in TWO tier walks (Foundation
  pp. 17-30, Higher pp. 35-45). 242 parse rows dedupe to 188 unique
  official_codes: 54 codes appear in BOTH walks, 53 of them with DIFFERENT
  statements per tier (e.g. 1.3A Foundation "use decimal notation" vs Higher
  "convert recurring decimals into fractions"), 1 with identical text.
  For the commissioned Higher program the HIGHER-tier statement is the
  operative wording wherever the code exists in the Higher walk; the 108
  Foundation-only codes are carried verbatim from their Foundation rows
  (the spec's own applicability rule: "Foundation statements are assumed
  knowledge for Higher Tier papers"). Every per-code choice and both wording
  variants are written to the ledger — nothing is silently dropped
  (the C26 "never silently fixes" rule, applied to tier dedupe).

Section/subsection titles follow the same rule: the Higher walk's topic
titles are the store titles (section 4 is "Geometry and trigonometry" in the
Higher walk, "Geometry" in the Foundation walk — ledger records the variant).
Content subsections in this specification are numbered WITHOUT titles
(canonical subsection.title is empty on all 242 rows) — subtopic titles are
emitted as null with that fact recorded, never invented.

Not derived for this qual (documented, not silently missing):
  draft_skill_tags (chemistry's c09-era authoring aid; no canonical source
  in the maths parse), spec_issue (no issue string asserted by the parse),
  practicals (0 by the parse's practical: prefix rule), command_words (the
  source specification has no command-word taxonomy table — canonical note
  carried verbatim into the store meta).

Usage: python3 scripts/c30_emit_maths_a_spec_stores.py [--check-only]
"""
from __future__ import annotations

import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # C28 §3.2 path registry — single source of store paths

QUAL = "igcse-maths-a"
CODE = "4MA1"
CURRICULUM_CODE = "4MA1-2016"
QUALIFICATION = "Pearson Edexcel International GCSE (9-1) Mathematics A"
SYLLABUS_VERSION = "2016"
TIER_PROGRAM = "Higher"
PDF_NAME = "international-gcse-in-mathematics-spec-a.pdf"
PDF_SHA1 = "b71a6432b8e34c155efb510d79a7b6e97611ba01"
CANON = REPO / "Official-Specifications/parsed/igcse-maths-a"
GENERATOR = "scripts/c30_emit_maths_a_spec_stores.py"
GENERATED = "2026-10-01"
LEDGER_REL = "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"

CANON_BUILDER = "canonical-builder-2.0"
POLICY = ("verbatim from the official PDF (canonical PDF-direct parse, "
          "whitespace-normalised only); notation damage preserved and "
          "flagged, never fixed")
EDGE_VOCAB = ("live V2 knowledge_edges enum (V2__curriculum_knowledge.sql): "
              "PART_OF, REQUIRES_PREREQUISITE, RELATED_TO, MISCONCEPTION_OF, "
              "EXPLAINED_BY, REMEDIATED_BY")

EXPECT = {"rows": 242, "unique": 188, "dup_codes": 54, "reworded": 53,
          "same_text": 1, "higher_only": 26, "foundation_only": 108,
          "flagged": 8, "topics": 6, "subtopics": 39, "practicals": 0,
          "command_words": 0, "ao_statements": 3, "unit_weightings": 3}

YAML_KW = dict(sort_keys=False, default_flow_style=False, allow_unicode=True,
               width=100)

failures: list[str] = []


def die(msg: str):
    failures.append(msg)


def norm(s) -> str:
    return re.sub(r"\s+", " ", str(s)).strip()


def sub_num(code: str) -> tuple:
    """Numeric sort key for subsection codes: '1.2' < '1.10'."""
    a, b = code.split(".")
    return (int(a), int(b))


def point_key(oc: str) -> tuple:
    m = re.match(r"^(\d+)\.(\d+)([A-Z]?)$", oc)
    return (int(m.group(1)), int(m.group(2)), m.group(3))


def base_provenance(source_file: str, extraction: str) -> dict:
    return {
        "tier": "RULE_DERIVED",
        "source_file": source_file,
        "extraction_method": extraction,
        "generated_by": GENERATOR,
        "generated_date": GENERATED,
        "pdf_source": PDF_NAME,
        "pdf_sha1": PDF_SHA1,
        "canonical_builder": f"{CANON_BUILDER} (2026-09-17)",
    }


def main() -> int:
    # ---- load canonical plane ------------------------------------------------
    spec = json.loads((CANON / "spec_points.json").read_text(encoding="utf-8"))
    rows = spec["spec_points"] if isinstance(spec, dict) else spec
    topics_c = json.loads((CANON / "topics.json").read_text(encoding="utf-8"))
    practicals_c = json.loads((CANON / "practicals.json").read_text(encoding="utf-8"))
    ao_c = json.loads((CANON / "assessment_objectives.json").read_text(encoding="utf-8"))
    cw_c = json.loads((CANON / "command_words.json").read_text(encoding="utf-8"))
    parse_report = json.loads((CANON / "parse_report.json").read_text(encoding="utf-8"))

    # ---- fail-closed preconditions ------------------------------------------
    if not parse_report.get("gates", {}).get("ALL_PASS"):
        die("parse_report gates are not ALL_PASS")
    if len(rows) != EXPECT["rows"]:
        die(f"canonical rows {len(rows)} != {EXPECT['rows']}")
    if rows[0]["provenance"]["pdf_sha1"] != PDF_SHA1:
        die("canonical pdf_sha1 mismatch")

    # ---- tier dedupe (higher-preferred) + census -----------------------------
    by_code: "OrderedDict[str, list[dict]]" = OrderedDict()
    for r in rows:
        by_code.setdefault(r["official_code"], []).append(r)

    chosen: dict[str, dict] = {}
    ledger_rows: list[dict] = []
    for oc, group in by_code.items():
        if len(group) == 1:
            chosen[oc] = group[0]
            continue
        hi = [g for g in group if g["applicability"]["tier"] == "Higher"]
        fo = [g for g in group if g["applicability"]["tier"] == "Foundation"]
        if len(hi) != 1 or len(fo) != 1:
            die(f"unexpected tier multiplicity for {oc}: "
                f"higher={len(hi)} foundation={len(fo)}")
        h, f = hi[0], fo[0]
        chosen[oc] = h  # higher-preferred
        same = norm(h["text"]) == norm(f["text"])
        ledger_rows.append({
            "official_code": oc,
            "same_text_normalized": same,
            "higher_preferred": True,
            "higher": {"text": h["text"], "pdf_page": h["provenance"]["page"],
                       "ordering": h["ordering"]},
            "foundation": {"text": f["text"], "pdf_page": f["provenance"]["page"],
                           "ordering": f["ordering"]},
        })

    reworded = [r for r in ledger_rows if not r["same_text_normalized"]]
    higher_only = [oc for oc, g in by_code.items()
                   if len(g) == 1 and g[0]["applicability"]["tier"] == "Higher"]
    foundation_only = [oc for oc, g in by_code.items()
                       if len(g) == 1 and g[0]["applicability"]["tier"] == "Foundation"]
    census = {"dup_codes": len(ledger_rows), "reworded": len(reworded),
              "same_text": len(ledger_rows) - len(reworded),
              "higher_only": len(higher_only),
              "foundation_only": len(foundation_only)}
    for k, v in EXPECT.items():
        if k in census and census[k] != v:
            die(f"census {k}={census[k]} != {v}")

    # ---- store-row order + global_order --------------------------------------
    store_order = sorted(chosen, key=lambda oc: (point_key(oc)[0],
                                                 point_key(oc)[1],
                                                 point_key(oc)[2] or ""))
    flag_vocab = sorted({f for r in rows for f in (r.get("flags") or [])})
    flagged_expected = sorted(r["official_code"] for r in rows if r.get("flags"))

    # ---- 1. specification_points.yaml ----------------------------------------
    sp_rows = []
    for i, oc in enumerate(store_order, start=1):
        c = chosen[oc]
        m = re.match(r"^(\d+)\.(\d+)([A-Z]?)$", oc)
        sec, sub, letter = m.group(1), m.group(2), m.group(3)
        secn, subn = f"{sec}.{sub}", f"{int(sec)}.{int(sub)}"
        prov = base_provenance(
            "Official-Specifications/parsed/igcse-maths-a/spec_points.json",
            c["provenance"].get("extraction_method", "pdf-span-geometry"))
        prov["pdf_page"] = c["provenance"]["page"]
        prov["pdf_oy"] = c["provenance"]["oy"]
        prov["tier_walk"] = c["applicability"]["tier"]
        row = {
            "code": f"{CODE}-{oc}",
            "official_code": oc,
            "official_wording": c["text"],
            "section": f"{CODE}-S{int(sec)}",
            "subsection": f"{CODE}-S{int(sec)}-{subn}",
            "ordering": c["ordering"],
            "global_order": i,
            "c_point": False,
            "practical": bool(c.get("practical")),
            "applicability": {
                "tier": c["applicability"]["tier"],
                "papers": list(c["applicability"]["papers"]),
                "rule": c["applicability"]["rule"],
            },
            "leading_verb": c.get("leading_verb"),
            "scope": c.get("scope"),
            "validation_status": "RULE_DERIVED",
            "confidence": 1.0,
            "version": 1,
            "provenance": prov,
            "damage_flags": list(c.get("flags") or []),
        }
        if oc in {r["official_code"] for r in reworded}:
            row["tier_dedupe_note"] = (
                "higher-preferred: the Foundation walk carries a different "
                "statement under this code — both variants recorded in the "
                "C30 tier-dedupe ledger")
        sp_rows.append(row)

    # ---- 2. topics.yaml --------------------------------------------------------
    sec_numbers = sorted({point_key(oc)[0] for oc in store_order})
    # Higher-walk titles: the topic.title carried by Higher-tier rows per section
    hi_titles, fo_titles = {}, {}
    for r in rows:
        n = int(r["topic"]["number"])
        (hi_titles if r["applicability"]["tier"] == "Higher"
         else fo_titles).setdefault(n, r["topic"]["title"])
    topic_titles, title_variants = {}, []
    for n in sec_numbers:
        if n in hi_titles:
            topic_titles[n] = hi_titles[n]
            if n in fo_titles and fo_titles[n] != hi_titles[n]:
                title_variants.append({"section": n, "higher": hi_titles[n],
                                       "foundation": fo_titles[n]})
        else:
            topic_titles[n] = fo_titles.get(n)
            die(f"section {n} has no Higher-walk title")
    # canonical topics.json numbered rows must agree with the SP-row titles
    for t in topics_c.get("topics", []):
        num = str(t.get("number"))
        if num.isdigit() and int(num) in topic_titles:
            if norm(t["title"]) not in {norm(topic_titles[int(num)]),
                                        norm(fo_titles.get(int(num), "")),
                                        norm(hi_titles.get(int(num), ""))}:
                die(f"topics.json title for section {num} not recognized: {t['title']!r}")

    topic_rows = [{
        "code": f"{CODE}-S{n}",
        "title": topic_titles[n],
        "title_md": topic_titles[n],
        "ordering": i,
        "header_source": ("canonical-pdf-direct-parse (Higher-tier walk title; "
                          "Foundation variant in the C30 ledger)" if any(
                              v["section"] == n for v in title_variants)
                          else "canonical-pdf-direct-parse"),
        "validation_status": "RULE_DERIVED",
        "confidence": 1.0,
        "version": 1,
        "provenance": base_provenance(
            "Official-Specifications/parsed/igcse-maths-a/topics.json",
            "at-a-glance content-table row + content-walk topic headers"),
        "damage_flags": [],
    } for i, n in enumerate(sec_numbers, start=1)]

    sub_codes = sorted({f"{point_key(oc)[0]}.{point_key(oc)[1]}" for oc in store_order},
                       key=sub_num)
    members: dict[str, list] = {sc: [] for sc in sub_codes}
    for oc in store_order:
        k = point_key(oc)
        members[f"{k[0]}.{k[1]}"].append(f"{CODE}-{oc}")
    subtopic_rows = [{
        "code": f"{CODE}-S{int(sc.split('.')[0])}-{sc}",
        "parent": f"{CODE}-S{int(sc.split('.')[0])}",
        "letter": sc,
        "title": None,
        "title_md": None,
        "header_source": ("none — the specification numbers content "
                          "subsections without titles"),
        "ordering": i,
        "spec_points": members[sc],
        "validation_status": "RULE_DERIVED",
        "confidence": 1.0,
        "version": 1,
        "provenance": base_provenance(
            "Official-Specifications/parsed/igcse-maths-a/spec_points.json",
            "content-walk subsection groupings (span-geometry)"),
        "damage_flags": [],
    } for i, sc in enumerate(sub_codes, start=1)]

    # ---- 3. practicals.yaml (empty by parse) ----------------------------------
    prac_note = practicals_c.get("note", "")
    if len(practicals_c.get("practicals", [])) != EXPECT["practicals"]:
        die("practicals canonical count != 0 — emitter precondition changed")

    # ---- 4. assessment_objectives.yaml ----------------------------------------
    ao_rows = [{
        "code": s["ao"],
        "description": s["description"],
        "weighting_overall": s["weighting_overall"],
        "validation_status": "RULE_DERIVED",
        "confidence": 1.0,
        "version": 1,
        "provenance": {**base_provenance(
            "Official-Specifications/parsed/igcse-maths-a/assessment_objectives.json",
            "assessment-objectives table (canonical PDF-direct parse)"),
            "pdf_page": s["page"]},
        "damage_flags": [],
    } for s in ao_c["statements"]]
    uw_rows = [{
        "unit": u["unit"],
        "weightings": list(u["weightings"]),
        "table_title": u["table_title"],
        "pdf_page": u["page"],
        "validation_status": "RULE_DERIVED",
        "confidence": 1.0,
        "version": 1,
        "provenance": {**base_provenance(
            "Official-Specifications/parsed/igcse-maths-a/assessment_objectives.json",
            "relationship-of-assessment-objectives-to-units table"),
            "pdf_page": u["page"]},
        "damage_flags": [],
    } for u in ao_c["unit_weightings"]]

    # ---- 5. command_words.yaml (empty by parse) --------------------------------
    cw_note = cw_c.get("note", "")
    if len(cw_c.get("command_words", [])) != EXPECT["command_words"]:
        die("command_words canonical count != 0 — emitter precondition changed")

    # ---- meta (shared block, per-store source_documents) -----------------------
    def meta(src_file: str) -> dict:
        return {
            "curriculum_code": CURRICULUM_CODE,
            "qualification": QUALIFICATION,
            "syllabus_version": SYLLABUS_VERSION,
            "tier_program": TIER_PROGRAM,
            "phase": 1,
            "node_families": ["TOPIC", "SUBTOPIC", "SPEC_POINT"],
            "graph_format_version": 1,
            "source_documents": [
                {"file": PDF_NAME, "role": "official-pdf", "sha1": PDF_SHA1},
                {"file": src_file, "role": "canonical-pdf-direct-parse",
                 "builder": CANON_BUILDER},
            ],
            "edge_vocabulary": EDGE_VOCAB,
            "provenance_default": "RULE_DERIVED",
            "statement_text_policy": POLICY,
            "tier_dedupe": {
                "rule": ("higher-preferred — where an official_code appears in "
                         "both tier walks the Higher-tier statement is the "
                         "operative wording for the commissioned Higher "
                         "program; Foundation-only statements are carried "
                         "verbatim (assumed knowledge per the spec's own "
                         "applicability rule)"),
                "ledger": LEDGER_REL,
                **census,
            },
            "notes": [
                "content subsections are numbered without titles in this "
                "specification (canonical subsection.title empty on all 242 "
                "rows) — subtopic titles are null, never invented",
                "no spec-issue string is asserted by the canonical parse; "
                "syllabus_version 2016 per the hub registry and s105 usage",
                "draft_skill_tags are a chemistry c09-era authoring aid with "
                "no canonical source in this parse — not derived for this qual",
            ],
            "counts": {
                "spec_points": len(sp_rows),
                "topics": len(topic_rows),
                "subtopics": len(subtopic_rows),
                "practicals": EXPECT["practicals"],
                "command_words": EXPECT["command_words"],
                "flagged_spec_points": len(flagged_expected),
                "damage_flag_vocabulary": flag_vocab,
            },
            "generator": GENERATOR,
            "generated": GENERATED,
        }

    docs = {
        "specification_points.yaml": {
            "meta": meta("Official-Specifications/parsed/igcse-maths-a/spec_points.json"),
            "specification_points": sp_rows},
        "topics.yaml": {
            "meta": meta("Official-Specifications/parsed/igcse-maths-a/topics.json"),
            "topics": topic_rows,
            "subtopics": subtopic_rows},
        "practicals.yaml": {
            "meta": meta("Official-Specifications/parsed/igcse-maths-a/practicals.json"),
            "practicals": [],
            "note": prac_note},
        "assessment_objectives.yaml": {
            "meta": meta("Official-Specifications/parsed/igcse-maths-a/assessment_objectives.json"),
            "assessment_objectives": ao_rows,
            "unit_weightings": uw_rows},
        "command_words.yaml": {
            "meta": meta("Official-Specifications/parsed/igcse-maths-a/command_words.json"),
            "command_words": [],
            "note": cw_note},
    }

    # ---- fail-closed postconditions (before any write) -------------------------
    if len(sp_rows) != EXPECT["unique"]:
        die(f"store rows {len(sp_rows)} != {EXPECT['unique']}")
    if [r["global_order"] for r in sp_rows] != list(range(1, EXPECT["unique"] + 1)):
        die("global_order not contiguous 1..188")
    if sorted(r["official_code"] for r in sp_rows) != sorted(by_code):
        die("store code set != canonical unique code set")
    flagged_stored = sorted(r["official_code"] for r in sp_rows if r["damage_flags"])
    if flagged_stored != flagged_expected:
        die(f"flagged rows not preserved: {flagged_stored} != {flagged_expected}")
    if len(topic_rows) != EXPECT["topics"] or len(subtopic_rows) != EXPECT["subtopics"]:
        die("topic/subtopic counts off")
    declared = sorted(p for s in subtopic_rows for p in s["spec_points"])
    if declared != sorted(r["code"] for r in sp_rows):
        die("subtopic.spec_points membership != SP store codes")
    for s in subtopic_rows:
        parent_ok = any(t["code"] == s["parent"] for t in topic_rows)
        if not parent_ok:
            die(f"subtopic {s['code']} parent unresolved")
    if len(ao_rows) != EXPECT["ao_statements"] or len(uw_rows) != EXPECT["unit_weightings"]:
        die("AO counts off")
    for r in sp_rows:
        if not r["official_wording"].strip():
            die(f"empty wording for {r['official_code']}")
    if failures:
        for f in failures:
            print(f"PRE/POST FAIL: {f}", file=sys.stderr)
        return 1

    if "--check-only" in sys.argv:
        print("check-only: all pre/post conditions green; nothing written")
        return 0

    # ---- write ------------------------------------------------------------------
    out_dir = GP.qual_dir(QUAL)
    out_dir.mkdir(parents=True, exist_ok=True)
    for fname, doc in docs.items():
        (out_dir / fname).write_text(
            yaml.safe_dump(doc, **YAML_KW), encoding="utf-8")
        print(f"wrote graph/{QUAL}/{fname}")
    ledger = {
        "schema": "syllabai.c30-tier-dedupe-ledger/1.0",
        "task": "T-C30 (K1 spec store build, igcse-maths-a)",
        "rule": docs["specification_points.yaml"]["meta"]["tier_dedupe"]["rule"],
        "generated": GENERATED,
        "census": census,
        "title_variants": title_variants,
        "rows": ledger_rows,
    }
    (REPO / LEDGER_REL).write_text(json.dumps(ledger, indent=1) + "\n",
                                   encoding="utf-8")
    print(f"wrote {LEDGER_REL} ({len(ledger_rows)} rows, census {census})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
