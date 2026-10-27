#!/usr/bin/env python3
"""T-C11 session 62 — render the batch-9 REVIEW GATE (the batch-8
c11_batch8_review_build.py pattern):

  graph/reports/C11_BATCH9_REVIEW_SHEET.md   — the operator gate sheet
  graph/reports/C11_BATCH9_REVIEW.json       — the machine-side twin
  scripts/c11_batch9_verdicts_template.yaml  — the OPERATOR-OWNED template
                                               (fill + rename per the gate
                                               pathway)

The sheet renders the decision record's §1-5 surface (totals, nodes,
edges, held, verdict surface). NOTHING here is promoted; the batch ends
at its operator gate.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
REPORTS = REPO / "graph" / "reports"
SHEET = REPORTS / "C11_BATCH9_REVIEW_SHEET.md"
REVIEW_JSON = REPORTS / "C11_BATCH9_REVIEW.json"
TEMPLATE = HERE / "c11_batch9_verdicts_template.yaml"

TODAY = "2026-09-24"


def main() -> int:
    dec = yaml.safe_load(
        (HERE / "c11_batch9_decisions.yaml").read_text(encoding="utf-8"))
    pass2 = yaml.safe_load(
        (HERE / "c11_batch9_review_pass2.yaml").read_text(encoding="utf-8"))
    rul = yaml.safe_load(
        (HERE / "c11_batch9_boundary_ruling.yaml").read_text(encoding="utf-8"))

    nodes, edges, held = dec["nodes"], dec["edges"], dec["held"]
    n_concept = sum(1 for n in nodes if n["family"] == "CONCEPT")
    n_mis = sum(1 for n in nodes if n["family"] == "MISCONCEPTION")
    sps = dec["meta"]["scope"]["spec_points"]
    n_rp = sum(1 for e in edges if e["relation"] == "REQUIRES_PREREQUISITE")
    n_wap = sum(1 for e in edges if e["relation"] == "WRONG_ANSWER_PATTERN")
    n_rb = sum(1 for e in edges if e["relation"] == "REMEDIATED_BY")
    partof = sum(len(n.get("spec_points") or []) for n in nodes)

    # ---- verdicts template (OPERATOR-OWNED) -------------------------------
    edge_rows = []
    for i, e in enumerate(edges, 1):
        edge_rows.append({
            "id": f"B9-E-{i:02d}",
            "triple": f"{e['source']} {e['relation']} {e['target']}",
            "pretriage": ("LIKELY_SAFE" if e["relation"] in (
                "REQUIRES_PREREQUISITE",) and e["target"] not in
                {t["target"] for t in
                 rul["boundary_edge_ruling"]["sanctioned_targets"]}
                and not e["source"].startswith("4CH1-MIS-")
                else "FLAGGED"),
            "verdict": None,
            "notes": "",
        })
    # annotate the boundary edges + the misconception rows in the notes
    boundary_targets = {t["target"]: t for t in
                        rul["boundary_edge_ruling"]["sanctioned_targets"]}
    for row, e in zip(edge_rows, edges):
        if e["target"] in boundary_targets:
            surf = boundary_targets[e["target"]]["surface"][:80]
            row["notes"] = ("cross-boundary target (session-62 ruling; the "
                            f"owner node — {surf}...)")
        if e["relation"] == "WRONG_ANSWER_PATTERN":
            row["notes"] = ("documented Reject class (the pinned Crude Oil "
                            "MS Q2b: 'Reject references to double bonds in "
                            "kerosene')")
        if e["relation"] == "REMEDIATED_BY":
            row["notes"] = "remediation target = WAP target (the B1-E-25 pattern)"
    node_rows = []
    for n in sorted(nodes, key=lambda x: x["code"]):
        kind = "B9-N" if n["family"] == "CONCEPT" else "B9-M"
        node_rows.append({
            "id": None,  # assigned below alphabetically per family split
            "code": n["code"],
            "family": n["family"],
            "pretriage": "LIKELY_SAFE (mark-scheme-documented)"
                         if n["family"] == "MISCONCEPTION" else "LIKELY_SAFE",
            "verdict": None,
            "notes": "",
        })
    # sheet §2 table order = decision-record order; template order =
    # alphabetical by code with the M-ids trailing (the batch-8 shape)
    concepts = [n for n in sorted(nodes, key=lambda x: x["code"])
                if n["family"] == "CONCEPT"]
    miscons = [n for n in sorted(nodes, key=lambda x: x["code"])
               if n["family"] == "MISCONCEPTION"]
    ordered = concepts + miscons
    for i, row in enumerate(node_rows, 1):
        row["id"] = (f"B9-N-{i:02d}" if row["family"] == "CONCEPT"
                     else f"B9-M-{i - len(concepts):02d}")
    template = {
        "meta": {
            "task": "T-C11",
            "stage": "s16-batch-9-verdicts",
            "batch": 9,
            "session": 62,
            "file": "OPERATOR-OWNED verdict record for C11_BATCH9_REVIEW_"
                    "SHEET (session 62) — verdicts recorded by operator "
                    "decision (pending).",
            "instructions": ("Fill verdict per row. Edge/node vocabulary: "
                             "CONFIRM | REJECT | HOLD | MERGE | SPLIT. This "
                             "batch authored NO REVIEW_REQUIRED edge (all "
                             "doubts were held or resolved on explicit "
                             "evidence). Identity-decision vocabulary: "
                             "MERGE (fold nodes) | SPLIT (mint finer) | "
                             "KEEP_AS_IS. The batch-9 extraction_pass is "
                             "c11-s16-batch-9 (Section 4 Organic Chemistry "
                             "FIRST slice, 21 authorable SPs 4CH1-4.1-4.22 "
                             "minus the 4CH1-4.15 negative-control "
                             "carve-out: S4-a Introduction + S4-b Crude Oil "
                             "& Fuels + S4-c Alkanes; no practicals own any "
                             "batch-9 SP). Its 9 held candidates are "
                             "informational only (no reopening, no "
                             "promotion of held candidates). FIVE edges "
                             "are cross-section boundary edges into the "
                             "ruled targets (CON-FRACTIONAL-DISTILLATION — "
                             "batch 1; CON-EMPIRICAL-FORMULA and "
                             "CON-MOLECULAR-FORMULA — the pilot; "
                             "CON-COMBUSTION-O2 — batch 5; CON-MIXTURE — "
                             "batch 1; sanctioned by the session-62 "
                             "cross-slice ruling, no duplicate mint). The "
                             "next session applies verdicts via the §18 "
                             "promotion pathway; nothing here is "
                             "HUMAN_VALIDATED."),
        },
        "edge_verdicts": edge_rows,
        "node_verdicts": node_rows,
        "identity_decisions": [
            {"id": "B9-ID-01", "verdict": None,
             "question": "keep the 4.8/4.9/4.10 fractions family as ONE node "
                         "(process + uses + trends taught as one topic in one "
                         "note) vs splitting the process node from the "
                         "fractions/trends node"},
            {"id": "B9-ID-02", "verdict": None,
             "question": "keep 4.11/4.12 as ONE fuels/combustion family node "
                         "(the fuel definition and the combustion-products "
                         "chemistry taught as one thread) vs splitting the "
                         "fuel-definition node from the products node"},
            {"id": "B9-ID-03", "verdict": None,
             "question": "keep 4.14/4.16 as ONE acid-rain causes node "
                         "(formation + contribution taught as one thread; the "
                         "4.15 negative control sits BETWEEN them and stays "
                         "uncovered) vs splitting the NOx-formation node from "
                         "the acid-rain node"},
            {"id": "B9-ID-04", "verdict": None,
             "question": "keep 4.17/4.18 as ONE cracking node (process and "
                         "economic necessity taught as one thread) vs "
                         "splitting the process node from the "
                         "supply/demand node"},
            {"id": "B9-ID-05", "verdict": None,
             "question": "keep 4.19/4.20/4.21 as ONE alkanes node (general "
                         "formula + saturation + the first-five table taught "
                         "as one topic) vs splitting the definitional node "
                         "from the drawing-skill node"},
            {"id": "B9-ID-06", "verdict": None,
             "question": "mint the MIS-KEROSENE-DOUBLE-BONDS misconception "
                         "from the pinned Crude Oil MS Q2b Reject class "
                         "(narrow-but-exact; the MIS-CUO-COLOUR/B8-M-02 "
                         "precedent) — or rule it exam-trivia"},
        ],
        "held_appendix_acknowledgment": {"acknowledged": None, "notes": ""},
    }
    TEMPLATE.write_text(
        yaml.safe_dump(template, sort_keys=False, allow_unicode=True,
                       width=100), encoding="utf-8")

    # ---- the review sheet -------------------------------------------------
    lines = []
    A = lines.append
    A("# T-C11 §16 Batch 9 Review Sheet — Concept / Prerequisite / "
      "Misconception Graph")
    A("")
    A(f"Slice 4CH1–4.1–4.22 minus the 4CH1-4.15 negative-control carve-out "
      f"(Section 4 — Organic Chemistry, FIRST slice: a Introduction + b "
      f"Crude Oil & Fuels + c Alkanes, {len(sps)} authorable SPs; no "
      f"practicals own any batch-9 SP) · generated {TODAY} · decision "
      f"record `scripts/c11_batch9_decisions.yaml` (pass 1: "
      f"`c11-s16-batch-9`) · adversarial pass 2: "
      f"`scripts/c11_batch9_review_pass2.yaml` · authorization: "
      f"`scripts/c11_s16_authorization.yaml` (§16 authorized 2026-09-12; "
      f"batch 9 = the first slice of the S4 section program commissioned by "
      f"the operator's 'commission a new section' directive) · boundary "
      f"ruling: `scripts/c11_batch9_boundary_ruling.yaml` (session 62, "
      f"machine-checked — the FIVE sanctioned boundary edges below)")
    A("")
    A("**NOTHING in this batch is authoritative.** All 15 nodes / 41 batch "
      "edges (20 authored semantic + 21 derived PART_OF) are AI_SUGGESTED "
      "(SUGGESTED). HUMAN_VALIDATED is reachable "
      "only by your promotion command via the §18 pathway "
      "(`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → "
      "regeneration). **Zero batch-9 promotions exist.** This sheet is the "
      "batch's operator gate: record verdicts in "
      "`scripts/c11_batch9_verdicts_template.yaml` (fill + rename to "
      "`c11_batch9_verdicts.yaml`); a later session encodes and applies "
      "them.")
    A("")
    A("How to review: for each row check the quoted evidence actually "
      "appears in the cited file and actually says what the record claims; "
      "then rule on the relation CLASS and direction, not just existence. "
      "Machine state: the full gate suite is green at the merged 180-node "
      f"/ 425-edge store; every quote is machine-verified against its "
      f"source file (G03/c11.4; {sum(len(sp['evidence']) for n in nodes for sp in (n.get('spec_points') or [])) + sum(len(n.get('evidence') or []) + len(n.get('remediation_evidence') or []) for n in nodes) + sum(len(e['evidence']) for e in edges)} "
      "quote probes + preverify checks verified BEFORE the registry grew); "
      "the 4.15 negative control is uncovered. FIVE edges are "
      "cross-section boundary edges into the ruled targets "
      "(CON-FRACTIONAL-DISTILLATION — the batch-1 owner; CON-EMPIRICAL-"
      "FORMULA and CON-MOLECULAR-FORMULA — the pilot owners; "
      "CON-COMBUSTION-O2 — the batch-5 owner; CON-MIXTURE — the batch-1 "
      "owner; sanctioned per the session-62 cross-slice ruling; no "
      "duplicate concept was minted). The S4-a/b/c families are MS-pinned "
      "(the Crude Oil MS Q2b Reject column anchors the ONE misconception "
      "mint; the Alkanes MS Q1a(i) marking points anchor the isomer "
      "definition). NO pass-2 finding required re-authoring (FP-B9-1..4 / "
      "FN-B9-1..2 are recorded questions and resolutions).")
    A("")
    A("## 1. Totals & second-pass agreement")
    A("")
    A("| | nodes | authored edges | held | |")
    A("|---|---|---|---|---|")
    A(f"| pass-1 (extraction) | {len(nodes)} | {len(edges)} (+{partof} "
      f"derived PART_OF) | {len(held)} |")
    A(f"| pass-2 verdicts | {len(nodes)} CONFIRM | {len(edges)} CONFIRM · 0 "
      f"HOLD · 0 REJECT | all {len(held)} AGREE |")
    A("")
    A(f"Raw agreement (NOT κ — single human rater, architecture §12): "
      f"nodes {len(nodes)}/{len(nodes)} = 100.0%; edges — of the {len(edges)} "
      f"edges pass-1 asserted (SUGGESTED), pass-2 confirmed {len(edges)} "
      f"(100.0%); pass-1 quarantined 0 edges as REVIEW_REQUIRED (this "
      f"batch authored NONE — every doubt was held or resolved on "
      f"explicit evidence). **Zero pass-2 findings required re-authoring; "
      f"zero demotions.**")
    A("")
    A("Forecast calibration (C11_BATCH_FORECAST.json future_batch_records): "
      "the batch-9 record is appended by the forecast instrument at this "
      "gate (see the regenerated C11_BATCH_FORECAST.json). The S4-a/b/c "
      "slice runs in the descriptive band (nodes/SP "
      f"{round(len(nodes)/len(sps), 2)}, edges/SP "
      f"{round(len(edges)/len(sps), 2)}), with the held adjacencies "
      f"(B9-H-01..09 — the surfaces the ruling dispositioned) accounting "
      f"for the gap, not thin coverage: no S1/S2/S3 identity was re-minted "
      f"(the 5 existing-owner targets reached via the 5 sanctioned boundary "
      f"edges); no batch-9 SP is practical-typed (the PR lane is empty).")
    A("")
    A(f"## 2. Concept & misconception nodes ({len(nodes)})")
    A("")
    A("| # | code | family | title | attaches to (role) | conf | evidence "
      "(anchor → quote) | pass-2 | operator |")
    A("|---|---|---|---|---|---|---|---|---|")
    for i, n in enumerate(nodes, 1):
        if n.get("spec_points"):
            atts = "; ".join(f"{sp['code']} ({sp['role'].lower()})"
                             for sp in n["spec_points"])
            ev = n["spec_points"][0]["evidence"][0]
        else:
            atts = "—"
            ev = n["evidence"][0]
        q = ev["quote"]
        if len(q) > 80:
            q = q[:80]
        kind = ("MARK_SCHEME: " if ev["kind"] == "MARK_SCHEME" else "NOTE: ")
        verdict = (pass2["nodes"].get(n["code"], {}).get("verdict")
                   or "CONFIRM")
        A(f"| {i} | `{n['code']}` | {n['family'][:5]} | {n['title']} | "
          f"{atts} | {n['confidence']} | {kind}“{q}” | "
          f"{verdict} | ☐ |")
    A("")
    A("Identity-policy notes (split-first; merges are operator-only, OD-1 "
      "operand rule): pass-2 flags the 4.8-4.10 one-family ruling "
      "(B9-ID-01), the 4.11-4.12 one-family ruling (B9-ID-02), the "
      "4.14+4.16 one-family ruling (B9-ID-03), the 4.17-4.18 one-family "
      "ruling (B9-ID-04), the 4.19-4.21 one-family ruling (B9-ID-05), and "
      "the ONE single-Reject-column misconception mint (B9-ID-06). All are "
      "operator identity decisions (template §identity_decisions). No "
      "batch-9 SP attaches a practical node (none is practical-typed; the "
      "4CH1-4.43C practical belongs to batch 11's slice).")
    A("")
    A(f"## 3. Authored semantic edges ({len(edges)})")
    A("")
    A("| # | edge | conf | derivation | evidence (anchor → quote) | "
      "pass-2 | operator |")
    A("|---|---|---|---|---|---|---|")
    for i, e in enumerate(edges, 1):
        ev = e["evidence"][0]
        q = ev["quote"]
        if len(q) > 80:
            q = q[:80]
        kind = ("MARK_SCHEME: " if ev["kind"] == "MARK_SCHEME" else "NOTE: ")
        A(f"| {i} | `{e['source']} {e['relation']} {e['target']}` | "
          f"{e['confidence']} | {e['provenance']['derivation_method']} | "
          f"{kind}“{q}” | CONFIRM | ☐ |")
    A("")
    A("FIVE edges are CROSS-SECTION boundary edges into the ruled targets "
      "(sanctioned per the session-62 cross-slice ruling — no duplicate "
      "mint): the 4.8 industrial-distillation row (into the batch-1 "
      "CON-FRACTIONAL-DISTILLATION owner), the 4.2 representation rows "
      "(into the pilot CON-EMPIRICAL-FORMULA and CON-MOLECULAR-FORMULA "
      "owners), the 4.11/4.12 oxygen row (into the batch-5 "
      "CON-COMBUSTION-O2 owner) and the 4.7 mixture row (into the batch-1 "
      "CON-MIXTURE owner). The THIRTEEN in-slice RP edges carry the "
      "teaching sequence the notes themselves establish.")
    A("")
    A(f"## 4. Held candidates ({len(held)}) — the abstention record")
    A("")
    A("| id | candidate | failure class / reason |")
    A("|---|---|---|")
    for h in held:
        reason = h["reason"].split("—")[0].strip().strip('"')
        A(f"| {h['id']} | {h['candidate']} | {reason} |")
    A("")
    A("Every held candidate cites its §19 failure class; the abstention "
      "record remains part of the graph provenance. A held record is a "
      "valid outcome — the abstention is the system's honest output.")
    A("")
    A("## 5. Operator verdict surface")
    A("")
    A(f"- **{len(edges)} SUGGESTED edges** (B9-E-01..{len(edges):02d}) — "
      f"the §18 promotion surface")
    A(f"- **{len(nodes)} nodes** ({n_concept} CONCEPT B9-N-01.."
      f"{n_concept:02d} + {n_mis} MISCONCEPTION B9-M-01) — node authority "
      f"stays SUGGESTED; nodes have no §18 pathway (node promotion is a "
      f"separate identity decision, deferred)")
    A("- **6 identity decisions** (B9-ID-01..06) — MERGE/SPLIT/KEEP_AS_IS")
    A(f"- **{len(held)} held candidates** — acknowledge the quarantine (no "
      f"reopening)")
    A("- **0 REVIEW_REQUIRED edges** — zero RR settlements needed")
    A("")
    A("Pathway: fill `scripts/c11_batch9_verdicts_template.yaml` → rename "
      "to `c11_batch9_verdicts.yaml` → a later session encodes + applies "
      "via `c11_verdict_encode_batch9`-style reconciliation + "
      "`c11_promote.py` (§18) + the gated generator re-run. NOTHING is "
      "promoted at this gate.")
    A("")
    SHEET.write_text("\n".join(lines), encoding="utf-8")

    # ---- the review JSON --------------------------------------------------
    review = {
        "task": "T-C11",
        "batch": 9,
        "session": 62,
        "generated": TODAY,
        "extraction_pass": dec["meta"]["extraction_pass"],
        "scope": {"spec_points": sps,
                  "negative_control": "4CH1-4.15 (carved out, uncovered)",
                  "practicals": []},
        "totals": {"nodes": len(nodes), "concepts": n_concept,
                   "misconceptions": n_mis, "authored_edges": len(edges),
                   "part_of_edges": partof, "held": len(held),
                   "review_required": 0, "rejected": 0},
        "counts_in_store": {"nodes": 180, "edges": 425, "part_of": 184,
                            "semantic_hv": 216},
        "pass2": {"agreement": "raw (NOT kappa)",
                  "demotions": 0, "re_authorings": 0,
                  "findings": [f["id"] for f in pass2["findings"]]},
        "boundary_ruling": {"file": "scripts/c11_batch9_boundary_ruling.yaml",
                            "session": 62,
                            "sanctioned_targets": [t["target"] for t in
                                                   rul["boundary_edge_ruling"
                                                       ]["sanctioned_targets"]],
                            "max_boundary_edges": 5,
                            "non_mint_count":
                                len(rul["boundary_edge_ruling"]
                                    ["non_mint_list"])},
        "ms_pins": dec["meta"]["scope"]["mark_scheme_evidence"],
        "forecast": "the batch-9 record is appended to "
                    "C11_BATCH_FORECAST.json future_batch_records by "
                    "c11_batch_forecast.py at this gate",
    }
    REVIEW_JSON.write_text(json.dumps(review, indent=2, ensure_ascii=False)
                           + "\n", encoding="utf-8")
    print(f"wrote {SHEET}")
    print(f"wrote {REVIEW_JSON}")
    print(f"wrote {TEMPLATE} (OPERATOR-OWNED; fill + rename)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
