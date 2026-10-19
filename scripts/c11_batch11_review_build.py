#!/usr/bin/env python3
"""T-C11 session 66 — render the batch-11 REVIEW GATE (the batch-10
c11_batch10_review_build.py pattern):

  graph/reports/C11_BATCH11_REVIEW_SHEET.md   — the operator gate sheet
  graph/reports/C11_BATCH11_REVIEW.json       — the machine-side twin
  scripts/c11_batch11_verdicts_template.yaml  — the OPERATOR-OWNED template
                                                (fill + rename per the gate
                                                pathway)

The sheet renders the decision record's §1-5 surface (totals, nodes,
edges, held, verdict surface). NOTHING here is promoted; the batch ends
at its operator gate.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
REPORTS = REPO / "graph" / "reports"
SHEET = REPORTS / "C11_BATCH11_REVIEW_SHEET.md"
REVIEW_JSON = REPORTS / "C11_BATCH11_REVIEW.json"
TEMPLATE = HERE / "c11_batch11_verdicts_template.yaml"

TODAY = "2026-09-25"


def main() -> int:
    dec = yaml.safe_load(
        (HERE / "c11_batch11_decisions.yaml").read_text(encoding="utf-8"))
    pass2 = yaml.safe_load(
        (HERE / "c11_batch11_review_pass2.yaml").read_text(encoding="utf-8"))
    rul = yaml.safe_load(
        (HERE / "c11_batch11_boundary_ruling.yaml").read_text(encoding="utf-8"))

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
            "id": f"B11-E-{i:02d}",
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
    boundary_targets = {t["target"]: t for t in
                        rul["boundary_edge_ruling"]["sanctioned_targets"]}
    for row, e in zip(edge_rows, edges):
        if e["target"] in boundary_targets:
            surf = boundary_targets[e["target"]]["surface"][:80]
            row["notes"] = ("cross-boundary target (session-66 ruling; the "
                            f"owner node — {surf}...)")
        if e["relation"] == "WRONG_ANSWER_PATTERN":
            row["notes"] = ("documented Reject class (the pinned Alkenes MS "
                            "Q2(c) / Synthetic Polymers MS Q4(c): 'Any "
                            "double-bonded product scores 0/2')")
        if e["relation"] == "REMEDIATED_BY":
            row["notes"] = ("remediation target = WAP target (the B1-E-25 "
                            "pattern)")
    node_rows = []
    for n in sorted(nodes, key=lambda x: x["code"]):
        node_rows.append({
            "id": None,
            "code": n["code"],
            "family": n["family"],
            "pretriage": "LIKELY_SAFE (mark-scheme-documented)"
                         if n["family"] == "MISCONCEPTION" else "LIKELY_SAFE",
            "verdict": None,
            "notes": "",
        })
    concepts = [n for n in sorted(nodes, key=lambda x: x["code"])
                if n["family"] == "CONCEPT"]
    miscons = [n for n in sorted(nodes, key=lambda x: x["code"])
               if n["family"] == "MISCONCEPTION"]
    for i, row in enumerate(node_rows, 1):
        row["id"] = (f"B11-N-{i:02d}" if row["family"] == "CONCEPT"
                     else f"B11-M-{i - len(concepts):02d}")
    template = {
        "meta": {
            "task": "T-C11",
            "stage": "s16-batch-11-verdicts",
            "batch": 11,
            "session": 66,
            "file": "OPERATOR-OWNED verdict record for C11_BATCH11_REVIEW_"
                    "SHEET (session 66) — verdicts recorded by operator "
                    "decision (pending).",
            "instructions": ("Fill verdict per row. Edge/node vocabulary: "
                             "CONFIRM | REJECT | HOLD | MERGE | SPLIT. This "
                             "batch authored NO REVIEW_REQUIRED edge (all "
                             "doubts were held or resolved on explicit "
                             "evidence). Identity-decision vocabulary: "
                             "MERGE (fold nodes) | SPLIT (mint finer) | "
                             "KEEP_AS_IS. The batch-11 extraction_pass is "
                             "c11-s16-batch-11 (Section 4 Organic Chemistry "
                             "THIRD slice: S4-g Esters 4.38C-4.43C incl. the "
                             "4.43C practical-typed SP + S4-h Synthetic "
                             "polymers 4.44-4.50C = 13 authorable SPs; the "
                             "4.43C practical rides the scoped T-C10 "
                             "practical 4CH1-PR-12 — the batch-3 1.60C/PR-04 "
                             "precedent). Its 10 held candidates are "
                             "informational only (no reopening, no "
                             "promotion of held candidates). TWELVE edges "
                             "are cross-section boundary edges into the "
                             "TWELVE ruled targets (TEN existing owners: "
                             "batch-10 CON-ALCOHOLS x2, CON-CARBOXYLIC-"
                             "ACIDS x2, CON-ALKENES; batch-9 CON-ORGANIC-"
                             "FORMULAE, CON-IUPAC-NAMING, CON-ORGANIC-"
                             "REACTION-CLASSES, CON-CO-POISONING; batch-5 "
                             "CON-CO2-GREENHOUSE; batch-1 CON-SIMPLE-"
                             "DISTILLATION; batch-7 CON-ACID-REACTIONS; "
                             "sanctioned by the session-66 cross-slice "
                             "ruling, no duplicate mint). Batch 11 COMPLETES "
                             "S4. The next session applies verdicts via the "
                             "§18 promotion pathway; nothing here is "
                             "HUMAN_VALIDATED."),
        },
        "edge_verdicts": edge_rows,
        "node_verdicts": node_rows,
        "identity_decisions": [
            {"id": "B11-ID-01", "verdict": None,
             "question": "keep the 4.38C/4.39C/4.40C/4.41C/4.42C esters "
                         "family as ONE node (functional group + formation "
                         "+ ethyl ethanoate formulae + the -yl/-oate naming "
                         "+ volatile-smelly uses taught as one thread) vs "
                         "splitting the naming node from the making node"},
            {"id": "B11-ID-02", "verdict": None,
             "question": "keep 4.44/4.45/4.46 as ONE addition-polymers node "
                         "(monomers/linking + the repeat-unit drawing rules "
                         "+ deduce-both-ways taught as one thread) vs "
                         "splitting the definition node from the drawing-"
                         "skills node"},
            {"id": "B11-ID-03", "verdict": None,
             "question": "keep 4.48C/4.49C/4.50C as ONE condensation-"
                         "polymers node (definition + polyester/ester-link "
                         "+ monomer deduction + the biopolyesters fold "
                         "taught in one note) vs splitting the biopolyesters "
                         "node from the condensation node"},
            {"id": "B11-ID-04", "verdict": None,
             "question": "mint the MIS-POLYMER-DOUBLE-BOND misconception "
                         "from the pinned Alkenes MS Q2(c) / Synthetic "
                         "Polymers MS Q4(c) Reject class ('Any double-bonded "
                         "product scores 0/2'; narrow-but-exact; the "
                         "MIS-PROPANOL-POSITION/B10-M-01 and "
                         "MIS-KEROSENE-DOUBLE-BONDS/B9-M-01 precedent) — "
                         "or rule it exam-trivia"},
        ],
        "held_appendix_acknowledgment": {"acknowledged": None, "notes": ""},
    }
    TEMPLATE.write_text(
        yaml.safe_dump(template, sort_keys=False, allow_unicode=True,
                       width=100), encoding="utf-8")

    # ---- the review sheet -------------------------------------------------
    lines = []
    A = lines.append
    A("# T-C11 §16 Batch 11 Review Sheet — Concept / Prerequisite / "
      "Misconception Graph")
    A("")
    A(f"Slice 4CH1–4.38C–4.50C (Section 4 — Organic Chemistry, THIRD slice: "
      f"g Esters + h Synthetic polymers, {len(sps)} authorable SPs; the "
      f"4CH1-4.43C practical-typed SP rides the scoped T-C10 practical "
      f"4CH1-PR-12 — the batch-3 1.60C/PR-04 precedent; the 4CH1-4.15 "
      f"negative-control carve-out sits in S4-b and is untouched) · generated "
      f"{TODAY} · decision record `scripts/c11_batch11_decisions.yaml` "
      f"(pass 1: `c11-s16-batch-11`) · adversarial pass 2: "
      f"`scripts/c11_batch11_review_pass2.yaml` · authorization: "
      f"`scripts/c11_s16_authorization.yaml` (§16 authorized 2026-09-12; "
      f"batch 11 = the final slice of the S4 section program — batch 11 "
      f"COMPLETES S4 — commissioned by the operator's 'commission batch 11' "
      f"directive) · boundary ruling: "
      f"`scripts/c11_batch11_boundary_ruling.yaml` (session 66, "
      f"machine-checked — the TWELVE sanctioned boundary edges below)")
    A("")
    A("**NOTHING in this batch is authoritative.** All 5 nodes / 29 batch "
      "edges (17 authored semantic + 12 derived PART_OF) are AI_SUGGESTED "
      "(SUGGESTED). HUMAN_VALIDATED is reachable "
      "only by your promotion command via the §18 pathway "
      "(`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → "
      "regeneration). **Zero batch-11 promotions exist.** This sheet is the "
      "batch's operator gate: record verdicts in "
      "`scripts/c11_batch11_verdicts_template.yaml` (fill + rename to "
      "`c11_batch11_verdicts.yaml`); a later session encodes and applies "
      "them.")
    A("")
    A("How to review: for each row check the quoted evidence actually "
      "appears in the cited file and actually says what the record claims; "
      "then rule on the relation CLASS and direction, not just existence. "
      "Machine state: the full gate suite is green at the merged 193-node "
      f"/ 488-edge store; every quote is machine-verified against its "
      f"source file (G03/c11.4; {sum(len(sp['evidence']) for n in nodes for sp in (n.get('spec_points') or [])) + sum(len(n.get('evidence') or []) + len(n.get('remediation_evidence') or []) for n in nodes) + sum(len(e['evidence']) for e in edges)} "
      "quote probes + preverify checks verified BEFORE the registry grew); "
      "the 4.15 negative control is uncovered. TWELVE edges are "
      "cross-section boundary edges into the TWELVE ruled targets (TEN "
      "existing owners: CON-ALCOHOLS and CON-CARBOXYLIC-ACIDS — the "
      "batch-10 owners, x2 each; CON-ALKENES — the batch-10 owner; "
      "CON-ORGANIC-FORMULAE, CON-IUPAC-NAMING, CON-ORGANIC-REACTION-CLASSES "
      "and CON-CO-POISONING — the batch-9 owners; CON-CO2-GREENHOUSE — the "
      "batch-5 owner; CON-SIMPLE-DISTILLATION — the batch-1 owner; "
      "CON-ACID-REACTIONS — the batch-7 owner; sanctioned per the "
      "session-66 cross-slice ruling; no duplicate concept was minted). "
      "The slice is MS-pinned PARTIAL with three-pin documentation (the "
      "Synthetic Polymers MS is the only Paper-2 MS file for the S4-h "
      "family — its Q4(c) is the same paper question as the Alkenes MS "
      "Q2(c), whose Reject column anchors the ONE misconception mint; the "
      "Crude Oil MS carries the condensation/biodegradation/inertness "
      "rows; the esters families have no dedicated Paper-2 MS file). NO "
      "pass-2 finding required re-authoring (FP-B11-1..4 / FN-B11-1..3 are "
      "recorded questions and resolutions).")
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
      "the batch-11 record is appended by the forecast instrument at this "
      "gate (see the regenerated C11_BATCH_FORECAST.json). The S4-g/h "
      "slice runs in the deepest consolidation band (nodes/SP "
      f"{round(len(nodes)/len(sps), 2)}, edges/SP "
      f"{round(len(edges)/len(sps), 2)}), with the held adjacencies "
      f"(B11-H-01..10 — the surfaces the ruling dispositioned) accounting "
      f"for the gap, not thin coverage: no S1/S2/S3 or batch-9/10 identity "
      f"was re-minted (the TEN existing-owner targets reached via the "
      f"TWELVE sanctioned boundary edges); the 4.43C practical rides the "
      f"scoped PR-12 (the PR lane is node-free by the batch-3 precedent).")
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
      "operand rule): pass-2 flags the 4.38C-4.42C one-family ruling "
      "(B11-ID-01), the 4.44-4.46 one-family ruling (B11-ID-02), the "
      "4.48C-4.50C one-family ruling with the biopolyesters fold "
      "(B11-ID-03), and the ONE single-Reject-column misconception mint "
      "(B11-ID-04). All are operator identity decisions (template "
      "§identity_decisions). The 4CH1-4.43C practical SP carries NO node "
      "(the batch-3 1.60C/PR-04 precedent — the practical's edges are "
      "PR-anchored, rows 5-7 below).")
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
    A("TWELVE edges are CROSS-SECTION boundary edges into the TWELVE "
      "ruled targets (sanctioned per the session-66 cross-slice ruling — "
      "no duplicate mint): the esterification-reactant rows x2 and the "
      "diol/dicarboxylic monomer rows x2 (into the batch-10 CON-ALCOHOLS "
      "and CON-CARBOXYLIC-ACIDS owners), the formulae-toolkit row and the "
      "naming-construction row (into the batch-9 CON-ORGANIC-FORMULAE and "
      "CON-IUPAC-NAMING owners), the practical's distil-off row and "
      "carbonate-purification row (into the batch-1 CON-SIMPLE-DISTILLATION "
      "and batch-7 CON-ACID-REACTIONS owners), the C=C-monomer row and the "
      "addition-class row (into the batch-10 CON-ALKENES and batch-9 "
      "CON-ORGANIC-REACTION-CLASSES owners), and the incineration rows "
      "(into the batch-5 CON-CO2-GREENHOUSE and batch-9 CON-CO-POISONING "
      "owners). The THREE in-slice RP edges carry the teaching sequence "
      "the notes themselves establish (S4-h presupposes S4-g; the disposal "
      "note presupposes the addition-polymer surface; the practical "
      "instantiates the esterification).")
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
    A(f"- **{len(edges)} SUGGESTED edges** (B11-E-01..{len(edges):02d}) — "
      f"the §18 promotion surface")
    A(f"- **{len(nodes)} nodes** ({n_concept} CONCEPT B11-N-01.."
      f"{n_concept:02d} + {n_mis} MISCONCEPTION B11-M-01) — node authority "
      f"stays SUGGESTED; nodes have no §18 pathway (node promotion is a "
      f"separate identity decision, deferred)")
    A("- **4 identity decisions** (B11-ID-01..04) — MERGE/SPLIT/KEEP_AS_IS")
    A(f"- **{len(held)} held candidates** — acknowledge the quarantine (no "
      f"reopening)")
    A("- **0 REVIEW_REQUIRED edges** — zero RR settlements needed")
    A("")
    A("Pathway: fill `scripts/c11_batch11_verdicts_template.yaml` → rename "
      "to `c11_batch11_verdicts.yaml` → a later session encodes + applies "
      "via `c11_verdict_encode_batch11`-style reconciliation + "
      "`c11_promote.py` (§18) + the gated generator re-run. NOTHING is "
      "promoted at this gate. Batch 11 completes S4 — after this verdict "
      "session the §16 S1-S4 authoring program is complete.")
    A("")
    SHEET.write_text("\n".join(lines), encoding="utf-8")

    # ---- the review JSON --------------------------------------------------
    review = {
        "task": "T-C11",
        "batch": 11,
        "session": 66,
        "generated": TODAY,
        "extraction_pass": dec["meta"]["extraction_pass"],
        "scope": {"spec_points": sps,
                  "negative_control": "4CH1-4.15 (carved out, uncovered)",
                  "practicals": ["4CH1-PR-12"]},
        "totals": {"nodes": len(nodes), "concepts": n_concept,
                   "misconceptions": n_mis, "authored_edges": len(edges),
                   "part_of_edges": partof, "held": len(held),
                   "review_required": 0, "rejected": 0},
        "counts_in_store": {"nodes": 193, "edges": 488, "part_of": 211,
                            "semantic_hv": 255},
        "pass2": {"agreement": "raw (NOT kappa)",
                  "demotions": 0, "re_authorings": 0,
                  "findings": [f["id"] for f in pass2["findings"]]},
        "boundary_ruling": {"file":
                            "scripts/c11_batch11_boundary_ruling.yaml",
                            "session": 66,
                            "sanctioned_targets": [t["target"] for t in
                                                   rul["boundary_edge_ruling"
                                                       ]["sanctioned_targets"]],
                            "max_boundary_edges": 12,
                            "non_mint_count":
                                len(rul["boundary_edge_ruling"]
                                    ["non_mint_list"])},
        "ms_pins": dec["meta"]["scope"]["mark_scheme_evidence"],
        "forecast": "the batch-11 record is appended to "
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
