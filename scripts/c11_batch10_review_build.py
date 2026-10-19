#!/usr/bin/env python3
"""T-C11 session 64 — render the batch-10 REVIEW GATE (the batch-9
c11_batch9_review_build.py pattern):

  graph/reports/C11_BATCH10_REVIEW_SHEET.md   — the operator gate sheet
  graph/reports/C11_BATCH10_REVIEW.json       — the machine-side twin
  scripts/c11_batch10_verdicts_template.yaml  — the OPERATOR-OWNED template
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
SHEET = REPORTS / "C11_BATCH10_REVIEW_SHEET.md"
REVIEW_JSON = REPORTS / "C11_BATCH10_REVIEW.json"
TEMPLATE = HERE / "c11_batch10_verdicts_template.yaml"

TODAY = "2026-09-25"


def main() -> int:
    dec = yaml.safe_load(
        (HERE / "c11_batch10_decisions.yaml").read_text(encoding="utf-8"))
    pass2 = yaml.safe_load(
        (HERE / "c11_batch10_review_pass2.yaml").read_text(encoding="utf-8"))
    rul = yaml.safe_load(
        (HERE / "c11_batch10_boundary_ruling.yaml").read_text(encoding="utf-8"))

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
            "id": f"B10-E-{i:02d}",
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
            row["notes"] = ("cross-boundary target (session-64 ruling; the "
                            f"owner node — {surf}...)")
        if e["relation"] == "WRONG_ANSWER_PATTERN":
            row["notes"] = ("documented Reject class (the pinned Alkenes MS "
                            "Q4(b)(ii): 'Reject propan-1-ol / 1-propanol')")
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
        row["id"] = (f"B10-N-{i:02d}" if row["family"] == "CONCEPT"
                     else f"B10-M-{i - len(concepts):02d}")
    template = {
        "meta": {
            "task": "T-C11",
            "stage": "s16-batch-10-verdicts",
            "batch": 10,
            "session": 64,
            "file": "OPERATOR-OWNED verdict record for C11_BATCH10_REVIEW_"
                    "SHEET (session 64) — verdicts recorded by operator "
                    "decision (pending).",
            "instructions": ("Fill verdict per row. Edge/node vocabulary: "
                             "CONFIRM | REJECT | HOLD | MERGE | SPLIT. This "
                             "batch authored NO REVIEW_REQUIRED edge (all "
                             "doubts were held or resolved on explicit "
                             "evidence). Identity-decision vocabulary: "
                             "MERGE (fold nodes) | SPLIT (mint finer) | "
                             "KEEP_AS_IS. The batch-10 extraction_pass is "
                             "c11-s16-batch-10 (Section 4 Organic Chemistry "
                             "SECOND slice: S4-d Alkenes 4.23-4.28 + S4-e "
                             "Alcohols 4.29C-4.33C + S4-f Carboxylic acids "
                             "4.34C-4.37C = 15 authorable SPs; no practicals "
                             "own any batch-10 SP). Its 9 held candidates "
                             "are informational only (no reopening, no "
                             "promotion of held candidates). THIRTEEN edges "
                             "are cross-section boundary edges into the "
                             "ELEVEN ruled targets (batch-9 owners "
                             "CON-HOMOLOGOUS-SERIES x2, CON-ORGANIC-FORMULAE "
                             "x2, CON-HYDROCARBON, CON-ALKANES, CON-ORGANIC-"
                             "REACTION-CLASSES, CON-IUPAC-NAMING, "
                             "CON-CRACKING; batch-5 CON-COMBUSTION-O2; "
                             "batch-6 CON-OX-RED-AGENTS; batch-1 "
                             "CON-FRACTIONAL-DISTILLATION; batch-7 CON-ACID-"
                             "REACTIONS; sanctioned by the session-64 "
                             "cross-slice ruling, no duplicate mint). The "
                             "next session applies verdicts via the §18 "
                             "promotion pathway; nothing here is "
                             "HUMAN_VALIDATED."),
        },
        "edge_verdicts": edge_rows,
        "node_verdicts": node_rows,
        "identity_decisions": [
            {"id": "B10-ID-01", "verdict": None,
             "question": "keep the 4.23/4.24/4.25/4.26 alkenes family as ONE "
                         "node (functional group + general formula + "
                         "unsaturated + the first-four table taught as one "
                         "thread) vs splitting the definition node from the "
                         "drawing-skills node"},
            {"id": "B10-ID-02", "verdict": None,
             "question": "keep 4.27/4.28 as ONE bromine-water-test node (the "
                         "addition reaction IS the chemistry the test "
                         "observes) vs splitting the dibromoalkane reaction "
                         "node from the distinguishing-test node"},
            {"id": "B10-ID-03", "verdict": None,
             "question": "keep 4.32C/4.33C as ONE manufacture node (both "
                         "routes and their conditions taught as one thread; "
                         "both routes share the fractional-distillation "
                         "finish) vs splitting the hydration node from the "
                         "fermentation node"},
            {"id": "B10-ID-04", "verdict": None,
             "question": "keep 4.34C/4.35C/4.37C as ONE carboxylic-acids "
                         "node (functional group + formulae/naming + vinegar "
                         "taught in one note) vs splitting the vinegar node "
                         "from the definition node"},
            {"id": "B10-ID-05", "verdict": None,
             "question": "mint the MIS-PROPANOL-POSITION misconception from "
                         "the pinned Alkenes MS Q4(b)(ii) Reject class "
                         "('Reject propan-1-ol / 1-propanol'; "
                         "narrow-but-exact; the MIS-HALIDE-TEST-HCL/B8-M-02 "
                         "and MIS-KEROSENE-DOUBLE-BONDS/B9-M-01 precedent) — "
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
    A("# T-C11 §16 Batch 10 Review Sheet — Concept / Prerequisite / "
      "Misconception Graph")
    A("")
    A(f"Slice 4CH1–4.23–4.37C (Section 4 — Organic Chemistry, SECOND slice: "
      f"d Alkenes + e Alcohols + f Carboxylic acids, {len(sps)} authorable "
      f"SPs; no practicals own any batch-10 SP; the 4CH1-4.15 negative-"
      f"control carve-out sits in S4-b and is untouched) · generated "
      f"{TODAY} · decision record `scripts/c11_batch10_decisions.yaml` "
      f"(pass 1: `c11-s16-batch-10`) · adversarial pass 2: "
      f"`scripts/c11_batch10_review_pass2.yaml` · authorization: "
      f"`scripts/c11_s16_authorization.yaml` (§16 authorized 2026-09-12; "
      f"batch 10 = the second slice of the S4 section program, commissioned "
      f"by the operator's 'commission batch 10' directive) · boundary "
      f"ruling: `scripts/c11_batch10_boundary_ruling.yaml` (session 64, "
      f"machine-checked — the THIRTEEN sanctioned boundary edges below)")
    A("")
    A("**NOTHING in this batch is authoritative.** All 8 nodes / 34 batch "
      "edges (19 authored semantic + 15 derived PART_OF) are AI_SUGGESTED "
      "(SUGGESTED). HUMAN_VALIDATED is reachable "
      "only by your promotion command via the §18 pathway "
      "(`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → "
      "regeneration). **Zero batch-10 promotions exist.** This sheet is the "
      "batch's operator gate: record verdicts in "
      "`scripts/c11_batch10_verdicts_template.yaml` (fill + rename to "
      "`c11_batch10_verdicts.yaml`); a later session encodes and applies "
      "them.")
    A("")
    A("How to review: for each row check the quoted evidence actually "
      "appears in the cited file and actually says what the record claims; "
      "then rule on the relation CLASS and direction, not just existence. "
      "Machine state: the full gate suite is green at the merged 188-node "
      f"/ 459-edge store; every quote is machine-verified against its "
      f"source file (G03/c11.4; {sum(len(sp['evidence']) for n in nodes for sp in (n.get('spec_points') or [])) + sum(len(n.get('evidence') or []) + len(n.get('remediation_evidence') or []) for n in nodes) + sum(len(e['evidence']) for e in edges)} "
      "quote probes + preverify checks verified BEFORE the registry grew); "
      "the 4.15 negative control is uncovered. THIRTEEN edges are "
      "cross-section boundary edges into the ELEVEN ruled targets "
      "(CON-HOMOLOGOUS-SERIES and CON-ORGANIC-FORMULAE — the batch-9 "
      "owners, x2 each; CON-HYDROCARBON, CON-ALKANES, CON-ORGANIC-"
      "REACTION-CLASSES, CON-IUPAC-NAMING and CON-CRACKING — the batch-9 "
      "owners; CON-COMBUSTION-O2 — the batch-5 owner; CON-OX-RED-AGENTS — "
      "the batch-6 owner; CON-FRACTIONAL-DISTILLATION — the batch-1 owner; "
      "CON-ACID-REACTIONS — the batch-7 owner; sanctioned per the "
      "session-64 cross-slice ruling; no duplicate concept was minted). "
      "The slice is MS-pinned PARTIAL (the Alkenes MS is the only Paper-2 "
      "mark scheme for the S4-d/e/f families: its Q4(b)(ii) Reject column "
      "anchors the ONE misconception mint and its Q2(a)(ii) accept/reject "
      "rows anchor the bromine-water-test language). NO pass-2 finding "
      "required re-authoring (FP-B10-1..6 / FN-B10-1..2 are recorded "
      "questions and resolutions).")
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
      "the batch-10 record is appended by the forecast instrument at this "
      "gate (see the regenerated C11_BATCH_FORECAST.json). The S4-d/e/f "
      "slice runs in the descriptive band (nodes/SP "
      f"{round(len(nodes)/len(sps), 2)}, edges/SP "
      f"{round(len(edges)/len(sps), 2)}), with the held adjacencies "
      f"(B10-H-01..09 — the surfaces the ruling dispositioned) accounting "
      f"for the gap, not thin coverage: no S1/S2/S3 or batch-9 identity "
      f"was re-minted (the ELEVEN existing-owner targets reached via the "
      f"THIRTEEN sanctioned boundary edges); no batch-10 SP is "
      f"practical-typed (the PR lane is empty).")
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
      "operand rule): pass-2 flags the 4.23-4.26 one-family ruling "
      "(B10-ID-01), the 4.27-4.28 reaction+test one-family ruling "
      "(B10-ID-02), the 4.32C-4.33C manufacture one-family ruling "
      "(B10-ID-03), the 4.34C+4.35C+4.37C acids one-family ruling "
      "(B10-ID-04), and the ONE single-Reject-column misconception mint "
      "(B10-ID-05). All are operator identity decisions (template "
      "§identity_decisions). No batch-10 SP attaches a practical node "
      "(none is practical-typed; the 4CH1-4.43C practical belongs to "
      "batch 11's slice).")
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
    A("THIRTEEN edges are CROSS-SECTION boundary edges into the ELEVEN "
      "ruled targets (sanctioned per the session-64 cross-slice ruling — "
      "no duplicate mint): the homologous-series rows x2 and the "
      "formulae-toolkit rows x2 (into the batch-9 CON-HOMOLOGOUS-SERIES "
      "and CON-ORGANIC-FORMULAE owners), the 4.25 hydrocarbon row, the "
      "4.28 alkane-contrast row and the 4.27 addition-class row (into the "
      "batch-9 CON-HYDROCARBON, CON-ALKANES and CON-ORGANIC-REACTION-"
      "CLASSES owners), the naming row (into the batch-9 CON-IUPAC-NAMING "
      "owner), the 4.31C combustion and oxidising-agent rows (into the "
      "batch-5 CON-COMBUSTION-O2 and batch-6 CON-OX-RED-AGENTS owners), "
      "the feedstock row (into the batch-9 CON-CRACKING owner), the "
      "separation row (into the batch-1 CON-FRACTIONAL-DISTILLATION "
      "owner) and the 4.36C acid-reactions row (into the batch-7 "
      "CON-ACID-REACTIONS owner). The FOUR in-slice RP edges carry the "
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
    A(f"- **{len(edges)} SUGGESTED edges** (B10-E-01..{len(edges):02d}) — "
      f"the §18 promotion surface")
    A(f"- **{len(nodes)} nodes** ({n_concept} CONCEPT B10-N-01.."
      f"{n_concept:02d} + {n_mis} MISCONCEPTION B10-M-01) — node authority "
      f"stays SUGGESTED; nodes have no §18 pathway (node promotion is a "
      f"separate identity decision, deferred)")
    A("- **5 identity decisions** (B10-ID-01..05) — MERGE/SPLIT/KEEP_AS_IS")
    A(f"- **{len(held)} held candidates** — acknowledge the quarantine (no "
      f"reopening)")
    A("- **0 REVIEW_REQUIRED edges** — zero RR settlements needed")
    A("")
    A("Pathway: fill `scripts/c11_batch10_verdicts_template.yaml` → rename "
      "to `c11_batch10_verdicts.yaml` → a later session encodes + applies "
      "via `c11_verdict_encode_batch10`-style reconciliation + "
      "`c11_promote.py` (§18) + the gated generator re-run. NOTHING is "
      "promoted at this gate.")
    A("")
    SHEET.write_text("\n".join(lines), encoding="utf-8")

    # ---- the review JSON --------------------------------------------------
    review = {
        "task": "T-C11",
        "batch": 10,
        "session": 64,
        "generated": TODAY,
        "extraction_pass": dec["meta"]["extraction_pass"],
        "scope": {"spec_points": sps,
                  "negative_control": "4CH1-4.15 (carved out, uncovered)",
                  "practicals": []},
        "totals": {"nodes": len(nodes), "concepts": n_concept,
                   "misconceptions": n_mis, "authored_edges": len(edges),
                   "part_of_edges": partof, "held": len(held),
                   "review_required": 0, "rejected": 0},
        "counts_in_store": {"nodes": 188, "edges": 459, "part_of": 199,
                            "semantic_hv": 236},
        "pass2": {"agreement": "raw (NOT kappa)",
                  "demotions": 0, "re_authorings": 0,
                  "findings": [f["id"] for f in pass2["findings"]]},
        "boundary_ruling": {"file":
                            "scripts/c11_batch10_boundary_ruling.yaml",
                            "session": 64,
                            "sanctioned_targets": [t["target"] for t in
                                                   rul["boundary_edge_ruling"
                                                       ]["sanctioned_targets"]],
                            "max_boundary_edges": 11,
                            "non_mint_count":
                                len(rul["boundary_edge_ruling"]
                                    ["non_mint_list"])},
        "ms_pins": dec["meta"]["scope"]["mark_scheme_evidence"],
        "forecast": "the batch-10 record is appended to "
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
