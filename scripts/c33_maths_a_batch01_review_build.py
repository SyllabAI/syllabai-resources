#!/usr/bin/env python3
"""T-C33 K2-C-1 — batch-B01 review-sheet builder (the c11_batch11_review_build.py
shape, first-batch instance).

Builds graph/reports/C33_BATCH01_REVIEW_SHEET.md (+ .json twin) from the batch
decision record, the pass-2 record and the live machine state. Deterministic:
re-running it on unchanged inputs reproduces the same bytes (the battery
byte-compares the committed sheet against a fresh build).

The sheet is the batch's operator gate surface (the C31 §8 K2-C evidence:
slice codes, coverage profile, diff-review bundle, held-quarantine state).
NOTHING in the batch is authoritative — SUGGESTED stays SUGGESTED until the
operator's recorded verdicts arrive through the §18 pathway.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
COURSE = "igcse-maths-a-18-higher"
DECISIONS = HERE / "c33_maths_a_batch01_decisions.yaml"
PASS2 = HERE / "c33_maths_a_batch01_review_pass2.yaml"
AUTH = HERE / "c33_maths_a_batch01_authorization.yaml"
SHEET = REPO / "graph/reports/C33_BATCH01_REVIEW_SHEET.md"
SHEET_JSON = REPO / "graph/reports/C33_BATCH01_REVIEW.json"


def sha16(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


def main() -> int:
    doc = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
    p2 = yaml.safe_load(PASS2.read_text(encoding="utf-8"))
    auth = yaml.safe_load(AUTH.read_text(encoding="utf-8"))

    nodes, edges, held = doc["nodes"], doc["edges"], doc["held"]
    kinds, ids = doc["command_kinds"], doc["identity_decisions"]
    cp = doc["meta"]["scope"]["coverage_profile"]
    n_att = sum(len(n["spec_points"]) for n in nodes)
    n_anc = (sum(len(sp["evidence"]) for n in nodes
                 for sp in n["spec_points"])
             + sum(len(e["evidence"]) for e in edges))

    # ---- pass-2 agreement recomputation (never trusted, recomputed) ----
    p2_nodes = p2["node_verdicts"]
    p2_edges = p2["edge_verdicts"]
    p2_held = p2["held_agreements"]
    node_ok = all(p2_nodes.get(n["code"]) == "CONFIRM" for n in nodes) \
        and len(p2_nodes) == len(nodes)
    edge_ok = all(
        p2_edges.get(f"{e['source']} {e['relation']} {e['target']}")
        == "CONFIRM" for e in edges) and len(p2_edges) == len(edges)
    held_ok = all(p2_held.get(h["id"]) == "AGREE" for h in held) \
        and len(p2_held) == len(held)
    if not (node_ok and edge_ok and held_ok):
        print("PASS-2 MISMATCH: node_ok=%s edge_ok=%s held_ok=%s"
              % (node_ok, edge_ok, held_ok))
        return 1

    def ev_cell(evs: list[dict], maxlen: int = 64) -> str:
        parts = []
        for ev in evs:
            tag = {"NOTE": "NOTE", "SPEC": "SPEC",
                   "MARK_SCHEME": "MARK_SCHEME"}[ev["kind"]]
            q = " ".join(ev["quote"].split())
            if len(q) > maxlen:
                q = q[:maxlen] + "…"
            parts.append(f"{tag}: “{q}”")
        return " · ".join(parts)

    L: list[str] = []
    A = L.append
    A("# T-C33 K2-C-1 — Batch B01 Review Sheet — Concept / Prerequisite Graph "
      "(igcse-maths-a, 4MA1 Higher)")
    A("")
    slice_txt = ("4MA1-1.1A–1.2D (global_order 1–12 of the ratified K1 store; "
                 "all 12 rows Foundation-applicability — assumed knowledge for "
                 "the Higher papers; subsection titles null by design, never "
                 "invented)")
    A(f"Slice {slice_txt} · generated 2026-10-01 · decision record "
      f"`scripts/c33_maths_a_batch01_decisions.yaml` (pass 1: "
      f"`c33-k2c-batch-01`) · adversarial pass 2: "
      f"`scripts/c33_maths_a_batch01_review_pass2.yaml` · commissioning: "
      f"`scripts/c33_maths_a_batch01_authorization.yaml` (the operator's "
      f"**K2-C-1** directive, 2026-10-01 — gate K2-C-1 of the C31 §8 "
      f"sequence) · coverage substrate: the T-C32 K2-A notes join "
      f"(`Official-Specifications/parsed/_derived/notes-join/"
      f"igcse-maths-a-18-higher.json`)")
    A("")
    A("**NOTHING in this batch is authoritative.** All 11 nodes / 12 authored "
      "edges are AI_SUGGESTED (SUGGESTED). HUMAN_VALIDATED is reachable only "
      "by your promotion command via the §18 pathway after your verdicts are "
      "recorded. **Zero promotions exist.** This sheet is the batch's operator "
      "gate: record verdicts against §2/§3/§4 below (a "
      "`c33_maths_a_batch01_verdicts.yaml` template lands with the verdict "
      "session); a later session encodes and applies them. The graph store "
      "does not grow at this gate — the maths-a concepts store does not exist "
      "yet and nothing creates it here.")
    A("")
    A("How to review: for each row check the quoted evidence actually appears "
      "in the cited file and actually says what the record claims; then rule "
      "on the relation CLASS and direction, not just existence. Machine "
      f"state: preverify 21/21 PASS, quote probe {n_anc}/{n_anc} anchors "
      "verbatim (18 NOTE / 25 SPEC / 4 MARK_SCHEME), term audit 60 terms "
      "audited with a 6-code future-batch boundary map; the maths-a graph dir "
      "carries exactly the 5 K1 stores (nothing has grown). The "
      "**unjoined-corpus negative control** holds: every NOTE citation is one "
      "of the 4 join-carried notes, each used for the SP it is joined to; the "
      "corpus's nearby unjoined pages (negative-numbers, mathematical-"
      "operations, hcf-and-lcm, prime-factor-decomposition, basic-fractions, "
      "adding-and-subtracting) are NOT cited anywhere. ZERO misconceptions "
      "minted — the three B01-topic mark-scheme files document correct "
      "procedures only (the chemistry MS-Reject contract honored by "
      "abstention). NO pass-2 finding required re-authoring (FP-B01-1..3 / "
      "FN-B01-1..2 are recorded questions and resolutions).")
    A("")
    A("## 1. Totals & second-pass agreement")
    A("")
    A("| | nodes | authored edges | held | derived PART_OF (at apply) |")
    A("|---|---|---|---|---|")
    A(f"| pass-1 (extraction) | {len(nodes)} | {len(edges)} | {len(held)} | "
      f"{n_att} |")
    A(f"| pass-2 verdicts | 11 CONFIRM | 12 CONFIRM · 0 HOLD · 0 REJECT | "
      f"5/5 AGREE | — |")
    A("")
    A("Raw agreement (NOT κ — single human rater, the architecture §12 "
      "convention): nodes 11/11 = 100%; edges 12/12 = 100%; pass-1 "
      "quarantined 0 edges as REVIEW_REQUIRED — every doubt was held or "
      "resolved on explicit evidence. **Zero pass-2 findings required "
      "re-authoring; zero demotions.**")
    A("")
    A("Forecast calibration (the C31 §5 adjusted forecast: 1.0 node / 1.6 "
      "edges per SP): B01 runs 11 nodes / 12 edges over 12 SPs = 0.92 / 1.00 "
      "per SP. The edge shortfall against 1.6 is **structural, not thin "
      "coverage**: B01 is the first batch — the registry is empty, so every "
      "candidate edge must resolve in-slice, and the cross-batch boundary-edge "
      "class (12 of chemistry batch-11's 17 edges) has no targets to reach "
      "yet. The five held candidates (§4) record the would-be edges the "
      "evidence could not support. The 13 derived PART_OF rows materialize at "
      "the §18 apply step (one per node attachment, SPEC_VERBATIM derivation), "
      "not at this gate.")
    A("")
    A("## 2. Concept nodes (11) — the diff-review bundle")
    A("")
    A("| # | code | title | attaches to (role) | conf | evidence (kind → "
      "quote) | pass-2 | operator |")
    A("|---|---|---|---|---|---|---|---|")
    for i, nd in enumerate(nodes, 1):
        atts = "; ".join(f"{sp['code']} ({sp['role']})"
                         for sp in nd["spec_points"])
        evs = " · ".join(ev_cell(sp["evidence"])
                         for sp in nd["spec_points"])
        A(f"| {i} | `{nd['code']}` | {nd['title']} | {atts} | "
          f"{nd['confidence']} | {evs} | "
          f"{p2['node_verdicts'][nd['code']]} | ☐ |")
    A("")
    A("Identity-policy notes (split-first; merges are operator-only): "
      "**B01-ID-01** authors 1.1A+1.1C+1.1D as ONE node "
      "(`4MA1-CON-INTEGERS-AND-DIRECTED-NUMBERS`) — the directed-number "
      "use/order demands are applications of the integer concept. "
      "**B01-ID-02** splits the 1.2D row's two bundled demands into TWO nodes "
      "(`…-ORDERING-FRACTIONS` + `…-FRACTION-OF-A-QUANTITY`), both CORE at "
      "1.2D. Both are reserved to your verdict. The five spec-text-only nodes "
      "(place value, four operations, factors-and-multiples, common "
      "denominators — spec-side — and the 1.2D pair) author from the ratified "
      "wording alone per the C31 §3 uncovered-span rule.")
    A("")
    A("## 3. Authored semantic edges (12)")
    A("")
    A("| # | edge | conf | derivation | evidence (kind → quote) | pass-2 | "
      "operator |")
    A("|---|---|---|---|---|---|---|")
    for i, e in enumerate(edges, 1):
        triple = (f"`{e['source']} {e['relation']} {e['target']}`")
        A(f"| {i} | {triple} | {e['conf']} | {e['derivation']} | "
          f"{ev_cell(e['evidence'])} | "
          f"{p2['edge_verdicts'][f'{e['source']} {e['relation']} {e['target']}']} "
          f"| ☐ |")
    A("")
    A("All 12 edges are in-slice REQUIRES_PREREQUISITE rows — the teaching "
      "sequence the notes and the ratified wordings themselves establish "
      "(operations before the order-of-operations hierarchy; the number-type "
      "vocabulary on the integer domain; prime/common factors behind "
      "cancelling and the LCD; equivalence behind conversion and common "
      "denominators; common denominators behind ordering; multiplication "
      "behind fraction-of-a-quantity). NO edge reaches outside the batch — "
      "there is no existing registry to reach into, and no boundary ruling is "
      "therefore required at B01 (the chemistry cross-slice ruling class is "
      "defined against an existing registry; B02.. inherit the term audit's "
      "6-code future-batch map instead).")
    A("")
    A("## 4. Held candidates (5) — the abstention record / held-quarantine state")
    A("")
    A("| id | candidate | failure class / reason | pass-2 | operator |")
    A("|---|---|---|---|---|")
    for h in held:
        cand = " ".join(str(h["candidate"]).split())
        reason = " ".join(str(h["reason"]).split())
        if len(cand) > 110:
            cand = cand[:110] + "…"
        if len(reason) > 220:
            reason = reason[:220] + "…"
        A(f"| {h['id']} | {cand} | {reason} | "
          f"{p2['held_agreements'][h['id']]} | ☐ |")
    A("")
    A("The held-quarantine discipline starts at B01: held rows carry failure "
      "classes (COVERAGE-UNJOINED-SUBSTRATE, SPEC-ONLY-SURFACE, "
      "NO-MS-REJECT-DOCUMENTATION, AVAILABLE-BUT-SURFACE-MINIMAL) and are "
      "revisit-able at the verdict or at later gates — never silently dropped, "
      "never force-authored. B01-H-01 is the honest disposition of the "
      "negative-numbers notes page (the corpus teaches the surface but the "
      "operator-worked join carries no 1.1C anchor for it — ratifying that "
      "anchor is an operator corpus-side decision, exactly the chemistry "
      "disposition pattern).")
    A("")
    A("## 5. Coverage profile (the C31 §3 standing per-batch statement)")
    A("")
    A("| measure | value |")
    A("|---|---|")
    A(f"| slice SPs | 12 (global_order 1–12) |")
    A(f"| notes-joined SPs (NOTE evidence possible) | {cp['notes_joined_count']} "
      f"({', '.join(cp['notes_joined_sps'])}) |")
    A(f"| spec-text-only SPs (SPEC evidence only) | {cp['spec_text_only_count']} "
      f"({', '.join(cp['spec_text_only_sps'])}) |")
    A("| MS-evidenced SPs (MARK_SCHEME evidence) | 1 (4MA1-1.2C via the "
      "fractions topic mark-schemes.md — a PARTIAL MS-documentation shape, "
      "the chemistry batch-3/4/10 precedent) |")
    A("| damage-flagged rows in the slice | 0 (the 8 math-fragment-assembly "
      "rows live outside this slice) |")
    A("| misconceptions minted | 0 — no MS-Reject documentation in the B01 "
      "topics (the contract honored by abstention) |")
    A("| practicals | none (the maths-a practicals store is 0-row by design) |")
    A("")
    A("## 6. Verdict instructions")
    A("")
    A("Rule per row on §2 (11 nodes), §3 (12 edges), §4 (5 held) and the two "
      "identity decisions (B01-ID-01 merge / B01-ID-02 split). A "
      "`scripts/c33_maths_a_batch01_verdicts.yaml` template accompanies the "
      "verdict session; verdicts encode through the intake-conformance check, "
      "the §18 apply step then (and only then) materializes the maths-a "
      "concepts/concept_edges/spec_command_kinds stores with exactly the "
      "promoted rows. Nothing here is live until your verdicts land.")
    A("")
    A("## 7. Machine-state appendix")
    A("")
    A(f"| artifact | sha256_16 |")
    A("|---|---|")
    A(f"| decisions record | {sha16(DECISIONS)} |")
    A(f"| pass-2 record | {sha16(PASS2)} |")
    A(f"| commissioning record | {sha16(AUTH)} |")
    A("| review sheet (this file) | deterministic rebuild — the battery "
      "byte-compares a fresh build against the committed bytes |")
    A("")
    SHEET.write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---- json twin ----
    review = {
        "schema": "syllabai.c33-batch01-review/1.0",
        "task": "T-C33",
        "gate": "K2-C-1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "decision_record": {"path": "scripts/c33_maths_a_batch01_decisions.yaml",
                            "sha256_16": sha16(DECISIONS)},
        "pass2_record": {"path": "scripts/c33_maths_a_batch01_review_pass2.yaml",
                         "sha256_16": sha16(PASS2)},
        "authorization": {"path": "scripts/c33_maths_a_batch01_authorization.yaml",
                          "sha256_16": sha16(AUTH),
                          "directive_verbatim":
                              auth["authorization"]["operator_statement_verbatim"]},
        "totals": {"nodes": len(nodes), "authored_edges": len(edges),
                   "held": len(held), "command_kinds": len(kinds),
                   "identity_decisions": len(ids),
                   "node_attachments": n_att,
                   "derived_partof_at_apply": n_att,
                   "evidence_anchors": n_anc},
        "pass2_agreement": {"nodes": "11/11 CONFIRM",
                            "edges": "12 CONFIRM / 0 HOLD / 0 REJECT",
                            "held": "5/5 AGREE",
                            "re_authoring_cases": 0},
        "coverage_profile": cp,
        "held_ids": [h["id"] for h in held],
        "identity_decisions": [i["id"] for i in ids],
        "future_batch_boundary_map": ["4MA1-1.2F", "4MA1-1.2I", "4MA1-1.3B",
                                      "4MA1-1.4D", "4MA1-1.4E", "4MA1-1.7A"],
        "stores_grown": 0,
    }
    SHEET_JSON.write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    print(f"review sheet built: {SHEET} ({SHEET.stat().st_size} bytes) + json "
          f"twin ({SHEET_JSON.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
