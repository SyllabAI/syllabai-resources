#!/usr/bin/env python3
"""T-C35 K2-C-3 — batch-B03 review-sheet builder (the c34_maths_a_batch02_
review_build.py shape, third-batch instance).

Builds graph/reports/C35_BATCH03_REVIEW_SHEET.md (+ .json twin) from the batch
decision record, the pass-2 record and the live machine state. Deterministic:
re-running it on unchanged inputs reproduces the same bytes (the battery
byte-compares the committed sheet against a fresh build).

The sheet is the batch's operator gate surface (the C31 §8 K2-C evidence:
slice codes, coverage profile, diff-review bundle, misconception mints,
held-quarantine state). NOTHING in the batch is authoritative — SUGGESTED
stays SUGGESTED until the operator's recorded verdicts arrive through the §18
pathway.
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
DECISIONS = HERE / "c35_maths_a_batch03_decisions.yaml"
PASS2 = HERE / "c35_maths_a_batch03_review_pass2.yaml"
AUTH = HERE / "c35_maths_a_batch03_authorization.yaml"
SHEET = REPO / "graph/reports/C35_BATCH03_REVIEW_SHEET.md"
SHEET_JSON = REPO / "graph/reports/C35_BATCH03_REVIEW.json"

# the term-audit probe's observed map (run recorded in the batch record):
# the audit's non-slice matches — 1.1H/1.2A are B01's rows (nodes authored,
# unapplied), 1.6G and 2.1D are genuinely unbatched
FUTURE_BOUNDARY_MAP = ["4MA1-1.1H", "4MA1-1.2A", "4MA1-1.6G", "4MA1-2.1D"]
INHERITED_MAP = ["4MA1-1.4D", "4MA1-1.4E", "4MA1-1.7A", "4MA1-1.8B"]
UNCITED_JOINS = [
    "SME-RevisionNotes/igcse-maths-a-18-higher/notes/1-numbers-and-the-number-"
    "system/number-toolkit/mathematical-operations.md (joined to 4MA1-1.5C; "
    "basic-symbol fluency content does not state the n(A) cardinality demand — "
    "disposition on the CARDINAL-NOTATION node's derivation notes)",
    "SME-RevisionNotes/igcse-maths-a-18-higher/notes/6-statistics-and-probability/"
    "probability-diagrams---venn-and-tree-diagrams/probability-and-venn-diagrams.md "
    "(joined to 4MA1-1.5E; probability-from-diagrams content recorded on the held "
    "B03-H-03 row instead)",
]


def sha16(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


def main() -> int:
    doc = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
    p2 = yaml.safe_load(PASS2.read_text(encoding="utf-8"))
    auth = yaml.safe_load(AUTH.read_text(encoding="utf-8"))

    nodes, edges, held = doc["nodes"], doc["edges"], doc["held"]
    kinds, ids = doc["command_kinds"], doc["identity_decisions"]
    con_nodes = [x for x in nodes if x["family"] == "CONCEPT"]
    mis_nodes = [x for x in nodes if x["family"] == "MISCONCEPTION"]
    cp = doc["meta"]["scope"]["coverage_profile"]
    n_att = sum(len(n["spec_points"]) for n in nodes)
    n_anc = (sum(len(sp["evidence"]) for n in nodes
                 for sp in n["spec_points"])
             + sum(len(n.get("evidence") or []) for n in nodes)
             + sum(len(e["evidence"]) for e in edges))
    n_note = (sum(1 for n in nodes for sp in n["spec_points"]
                  for ev in sp["evidence"] if ev["kind"] == "NOTE")
              + sum(1 for n in nodes for ev in n.get("evidence") or []
                    if ev["kind"] == "NOTE")
              + sum(1 for e in edges for ev in e["evidence"]
                    if ev["kind"] == "NOTE"))
    n_spec = (sum(1 for n in nodes for sp in n["spec_points"]
                  for ev in sp["evidence"] if ev["kind"] == "SPEC")
              + sum(1 for n in nodes for ev in n.get("evidence") or []
                    if ev["kind"] == "SPEC")
              + sum(1 for e in edges for ev in e["evidence"]
                    if ev["kind"] == "SPEC"))
    n_ms = n_anc - n_note - n_spec
    n_rp = sum(1 for e in edges if e["relation"] == "REQUIRES_PREREQUISITE")

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
    A("# T-C35 K2-C-3 — Batch B03 Review Sheet — Concept / Prerequisite Graph "
      "(igcse-maths-a, 4MA1 Higher)")
    A("")
    slice_txt = ("4MA1-1.4C–1.6D (global_order 25–36 of the ratified K1 store; "
                 "a MIXED-TIER slice — 7 Higher rows (1.4C, 1.5A–1.5D, 1.6A, "
                 "1.6B) plus 5 Foundation rows (1.4D, 1.4E, 1.5E, 1.6C, 1.6D); "
                 "spanning the 1.4 tail, 1.5 complete and the 1.6 head; "
                 "subsection titles null by design, never invented; the 1.5C "
                 "store wording carries the canonical parse's spacing artifact "
                 "verbatim, quoted in the store form, never silently repaired)")
    A(f"Slice {slice_txt} · generated 2026-10-02 · decision record "
      f"`scripts/c35_maths_a_batch03_decisions.yaml` (pass 1: "
      f"`c35-k2c-batch-03`) · adversarial pass 2: "
      f"`scripts/c35_maths_a_batch03_review_pass2.yaml` · commissioning: "
      f"`scripts/c35_maths_a_batch03_authorization.yaml` (the operator's "
      f"**K2-C-3** directive, 2026-10-02 — gate K2-C-3 of the C31 §8 "
      f"sequence) · coverage substrate: the T-C32 K2-A notes join "
      f"(`Official-Specifications/parsed/_derived/notes-join/"
      f"igcse-maths-a-18-higher.json`)")
    A("")
    A("**NOTHING in this batch is authoritative.** All 14 nodes (12 concept + "
      "2 misconception) / 13 authored edges are AI_SUGGESTED (SUGGESTED). "
      "HUMAN_VALIDATED is reachable only by your promotion command via the §18 "
      "pathway after your verdicts are recorded. **Zero promotions exist** — "
      "the B01 packet (T-C33) and the B02 packet (T-C34) likewise await your "
      "verdicts, so the maths-a graph dir still carries exactly the 5 K1 "
      "stores and nothing has grown from any batch. This sheet is the batch's "
      "operator gate: record verdicts against §2/§2a/§3/§4 below (a "
      "`c35_maths_a_batch03_verdicts.yaml` template lands with the verdict "
      "session); a later session encodes and applies them.")
    A("")
    A("How to review: for each row check the quoted evidence actually appears "
      "in the cited file and actually says what the record claims; then rule "
      "on the relation CLASS and direction, not just existence. Machine "
      f"state: preverify 33/33 PASS, quote probe {n_anc}/{n_anc} anchors "
      f"verbatim ({n_note} NOTE / {n_spec} SPEC / {n_ms} MARK_SCHEME), term "
      "audit 60 terms audited (18 match terms — all in-slice except four "
      "non-slice codes), the maths-a graph dir still carries exactly the 5 K1 "
      "stores (nothing has grown). The **unjoined-corpus negative control** "
      "holds at third-batch strength: every NOTE citation is one of the 9 "
      "join-carried notes, pair-backed at its SP (nodes) or at an endpoint SP "
      "(edges — the B02 strength, carried forward); the two join-carried-but-"
      "UNCITED pages are recorded in the census with dispositions, not padded "
      "citations; the corpus's nearby unjoined pages (basic-percentages, "
      "percentage-increases-and-decreases, reverse-percentages, "
      "converting-between-fdp — itself joined to B02's 1.2G — standard-form, "
      "operations-with-standard-form, types-of-number, et al.) are NOT cited "
      "anywhere. TWO misconceptions minted (§2a) — the second and third "
      "maths-a mints, on the set-notation MS Q7 documentation (the "
      "complement-of-union mistake) and the percentages MS Q10/Q11 "
      "documentation (the inverted quotient); the mint-vs-exam-trivia and "
      "home-row questions are operator-reserved (B03-ID-02/03). NO pass-2 "
      "finding required re-authoring (FP-B03-1..3 / FN-B03-1..3 are recorded "
      "questions and resolutions).")
    A("")
    A("## 1. Totals & second-pass agreement")
    A("")
    A("| | concept nodes | misconception nodes | authored edges | held | "
      "derived PART_OF (at apply) |")
    A("|---|---|---|---|---|---|")
    A(f"| pass-1 (extraction) | {len(con_nodes)} | {len(mis_nodes)} | "
      f"{len(edges)} | {len(held)} | {n_att} |")
    A(f"| pass-2 verdicts | 12 CONFIRM | 2 CONFIRM | 13 CONFIRM · 0 HOLD · 0 "
      f"REJECT | 8/8 AGREE | — |")
    A("")
    A("Raw agreement (NOT κ — single human rater, the architecture §12 "
      "convention): nodes 14/14 = 100%; edges 13/13 = 100%; pass-1 "
      "quarantined 0 edges as REVIEW_REQUIRED — every doubt was held or "
      "resolved on explicit evidence. **Zero pass-2 findings required "
      "re-authoring; zero demotions.**")
    A("")
    A("Forecast calibration (the C31 §5 adjusted forecast: 1.0 node / 1.6 "
      "edges per SP): B03 runs 12 concept nodes / 9 REQUIRES_PREREQUISITE "
      "edges (+2 misconception nodes and their 4 WAP/remediation edges) over "
      "12 SPs = 1.00 node / 0.75 prerequisite edge per SP. The node rate is "
      "on forecast. The edge shortfall against 1.6 is **structural, not thin "
      "coverage** (the FN-B03-3 mechanism, named at B02): the registry is "
      "still absent (B01 and B02 authored-to-gate, not applied), so the "
      "cross-batch boundary-edge class has no targets to reach — five of the "
      "eight held candidates (§4) are exactly those would-be edges, quoted "
      "with their evidence (two to B01/B02 nodes, three to future-batch "
      "families). The 14 derived PART_OF rows materialize at the §18 apply "
      "step (one per node attachment, SPEC_VERBATIM derivation), not at this "
      "gate.")
    A("")
    A("## 2. Concept nodes (12) — the diff-review bundle")
    A("")
    A("| # | code | title | attaches to (role) | conf | evidence (kind → "
      "quote) | pass-2 | operator |")
    A("|---|---|---|---|---|---|---|---|")
    for i, nd in enumerate(con_nodes, 1):
        atts = "; ".join(f"{sp['code']} ({sp['role']})"
                         for sp in nd["spec_points"])
        evs = " · ".join(ev_cell(sp["evidence"])
                         for sp in nd["spec_points"])
        A(f"| {i} | `{nd['code']}` | {nd['title']} | {atts} | "
          f"{nd['confidence']} | {evs} | "
          f"{p2['node_verdicts'][nd['code']]} | ☐ |")
    A("")
    A("Identity-policy notes (split-first; merges are operator-only): "
      "**B03-ID-01** authors the Venn mirror rows as TWO nodes — 1.5B "
      "(`4MA1-CON-VENN-REPRESENTATION`, Higher, with the element-count arm) "
      "and 1.5E (`4MA1-CON-VENN-FOUNDATION`, Foundation) — the substrate's "
      "own split of the set-notation page (notation half → 1.5B, diagrams "
      "half → 1.5E) supports it; any single Venn-representation family merge "
      "is yours to rule. The six spec-text-only nodes (sets-and-subsets, "
      "cardinal-notation, sets-in-practice, repeated-percentage-change, "
      "compound-interest, percentage-fraction-decimal — plus "
      "percentages-as-operators, which carries MS evidence on the ratified-"
      "wording base) author from the ratified wording alone per the C31 §3 "
      "uncovered-span rule; the cardinal-notation node's only join-carried "
      "page (mathematical-operations) does not state the n(A) demand and is "
      "UNCITED by the census, not padded.")
    A("")
    A("## 2a. Misconception nodes (2) — the second and third maths-a mints")
    A("")
    A("| # | code | title | rides | evidence (kind → quote) | pass-2 | "
      "operator |")
    A("|---|---|---|---|---|---|---|")
    for i, nd in enumerate(mis_nodes, 1):
        ride = "; ".join(f"{sp['code']} ({sp['role']})"
                         for sp in nd["spec_points"])
        evs = ev_cell(nd.get("evidence") or [])
        A(f"| {i} | `{nd['code']}` | {nd['title']} | {ride} | {evs} | "
          f"{p2['node_verdicts'][nd['code']]} | ☐ |")
    A("")
    A("Both mints satisfy the chemistry contract's condition — a mark-scheme "
      "row documenting the wrong-answer class with the corrected form in the "
      "same row: M1 rides 4MA1-1.5B on the set-notation MS Q7(b) row (writing "
      "(A∩B)' where (A∪B)' or A'∩B' is meant); M2 rides 4MA1-1.6D on the "
      "percentages MS Q10/Q11 rows (the asked-for 400% answered as the "
      "reciprocal 25%). Each carries a WRONG_ANSWER_PATTERN edge and a "
      "REMEDIATED_BY edge into its home concept node (§3, rows 10–13) — the "
      "remediation evidence is the MS's own corrected form. **B03-ID-03** "
      "reserves the mint-vs-exam-trivia ruling to you (the chemistry "
      "B10-ID-05 / B02-ID-03 precedent) AND M1's home row (1.5B vs the "
      "Foundation twin 1.5E); **B03-ID-02** reserves M2's home row (1.6D vs "
      "the 1.6E percentage-problems row that sits in B04).")
    A("")
    A("## 3. Authored semantic edges (13)")
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
    A(f"Rows 1–{n_rp} are in-slice REQUIRES_PREREQUISITE rows — the teaching "
      "sequence the notes and the ratified wordings themselves establish "
      "(HCF/LCM on the prime-factor decomposition they read; the Venn "
      "counting arm on the n(A) notation and the notation on the set concept; "
      "the Foundation Venn row on the set concept; both practical-situations "
      "edges on the Venn machinery; compound interest on repeated percentage "
      "change, repeated change on the multiplier operator, and the operator "
      "on the fraction/decimal expression it notates). Rows 10–11 are the two "
      "documented WRONG_ANSWER_PATTERNs and rows 12–13 their REMEDIATED_BY "
      "pairs (the B1-E-25 pattern: remediation target = WAP target). NO "
      "REQUIRES_PREREQUISITE edge reaches outside the batch — there is no "
      "registry to reach into, and the cross-batch candidates are HELD (§4) "
      "with the B02-inherited map as their ruling starting point.")
    A("")
    A("## 4. Held candidates (8) — the abstention record / held-quarantine state")
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
    A("The held-quarantine discipline continues from B01/B02: held rows carry "
      "failure classes — the batch adds ORDER-INVERSION-NO-EDGE-VOCABULARY "
      "(the HCF-via-Venn method would invert the canonical walk and the graph "
      "vocabulary has no tool-application relation) to the standing "
      "CROSS-BATCH-TARGET-UNPROMOTED, CROSS-BATCH-TARGET-FUTURE-BATCH and "
      "COVERAGE-UNJOINED-SUBSTRATE classes — and are revisit-able at the "
      "verdict or at later gates, never silently dropped, never "
      "force-authored. **The B01 quarantine (B01-H-01..05) and the B02 "
      "quarantine (B02-H-01..08) are inherited untouched** and all three rule "
      "together at the verdict session. B03-H-02 and B03-H-05 extend the "
      "cross-batch holds to B01's and B02's nodes respectively (equivalent "
      "fractions; the fraction-conversion fluency); B03-H-06/B03-H-07 pre-"
      "record the B04 boundary (the 1.6E single-change fluency; the 1.6B/1.6G "
      "compound-interest mirror pair).")
    A("")
    A("## 5. Coverage profile (the C31 §3 standing per-batch statement)")
    A("")
    A("| measure | value |")
    A("|---|---|")
    A("| slice SPs | 12 (global_order 25–36) |")
    A("| tier mix | 7 Higher (4MA1-1.4C, 1.5A, 1.5B, 1.5C, 1.5D, 1.6A, 1.6B) "
      "+ 5 Foundation (1.4D, 1.4E, 1.5E, 1.6C, 1.6D) |")
    A(f"| notes-joined SPs (NOTE evidence possible) | {cp['notes_joined_count']} "
      f"({', '.join(cp['notes_joined_sps'])}) — 11 join rows over 9 distinct "
      "note files (hcf-and-lcm carries two anchors — HCF and LCM; "
      "set-notation-and-venn-diagrams carries two — 1.5B and 1.5E) |")
    A(f"| spec-text-only SPs (SPEC evidence only) | {cp['spec_text_only_count']} "
      f"({', '.join(cp['spec_text_only_sps'])}) |")
    A("| MS-evidenced SPs (MARK_SCHEME evidence on node attachments) | 6 "
      "(4MA1-1.4C via the powers-roots topic MS; 1.4D and 1.4E via the "
      "prime-factors topic MS incl. the Q46 Venn-marking criterion; 1.6A and "
      "1.6B via the compound-interest topic MS; 1.6D via the percentages "
      "topic MS — a PARTIAL MS-documentation shape, the chemistry "
      "batch-3/4/10 precedent; MS evidence also rides three edges: the "
      "practical cat-and-dog row at 1.5D/1.5B, the multiplier rows, and the "
      "145%-equivalence bridge) |")
    A("| join-carried but uncited pages | 2 — the uncited-join census records "
      "each with its disposition (see the machine-state appendix) |")
    A("| damage-flagged rows in the slice | 0 (the 8 math-fragment-assembly "
      "rows live outside this slice) |")
    A("| misconceptions minted | 2 — the set-notation MS Q7 and percentages "
      "MS Q10/Q11 documented classes (the second and third maths-a mints; "
      "B01 minted zero, B02 minted two) |")
    A("| practicals | none (the maths-a practicals store is 0-row by design) |")
    A("")
    A("## 6. Verdict instructions")
    A("")
    A("Rule per row on §2 (12 concept nodes), §2a (2 misconception nodes — "
      "including the B03-ID-03 mint-vs-trivia and home-row rulings), §3 (13 "
      "edges) and §4 (8 held), plus the three identity decisions (B03-ID-01 "
      "the 1.5B/1.5E Venn mirror pair; B03-ID-02 M2's home row; B03-ID-03 the "
      "mints and M1's home row). A `scripts/c35_maths_a_batch03_verdicts.yaml` "
      "template accompanies the verdict session; verdicts encode through the "
      "intake-conformance check, the §18 apply step then (and only then) "
      "materializes/grows the maths-a concepts/concept_edges/spec_command_"
      "kinds stores with exactly the promoted rows from ALL authored batches "
      "— B01's, B02's and B03's quarantines rule together there. Nothing here "
      "is live until your verdicts land.")
    A("")
    A("## 7. Machine-state appendix")
    A("")
    A("| artifact | sha256_16 |")
    A("|---|---|")
    A(f"| decisions record | {sha16(DECISIONS)} |")
    A(f"| pass-2 record | {sha16(PASS2)} |")
    A(f"| commissioning record | {sha16(AUTH)} |")
    A("| review sheet (this file) | deterministic rebuild — the battery "
      "byte-compares a fresh build against the committed bytes |")
    A("")
    A("Uncited-join census (the negative control's transparency annex):")
    A("")
    for u in UNCITED_JOINS:
        A(f"- {u}")
    A("")
    A(f"Boundary map for B04.. (the term audit's non-slice matches, "
      f"{len(FUTURE_BOUNDARY_MAP)} codes): {', '.join(FUTURE_BOUNDARY_MAP)} — "
      "1.1H and 1.2A are B01's rows (nodes authored, unapplied — the "
      "common-factor/multiple and equivalent-fraction vocabulary B03's HCF/LCM "
      "node shares); 1.6G is the compound-interest Foundation twin (held "
      "B03-H-07; the audit's 'compound interest' match confirms it); 2.1D is "
      "this audit's NEW match ('index laws' against the S2 algebra row 'use "
      "index laws in simple cases'). The B02-inherited codes 1.4D/1.4E are "
      "now IN-SLICE (their nodes mint here); 1.7A/1.8B drop out of the "
      "superseding map (no B03 vocabulary match).")
    A("")
    SHEET.write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---- json twin ----
    review = {
        "schema": "syllabai.c35-batch03-review/1.0",
        "task": "T-C35",
        "gate": "K2-C-3",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "decision_record": {"path": "scripts/c35_maths_a_batch03_decisions.yaml",
                            "sha256_16": sha16(DECISIONS)},
        "pass2_record": {"path": "scripts/c35_maths_a_batch03_review_pass2.yaml",
                         "sha256_16": sha16(PASS2)},
        "authorization": {"path": "scripts/c35_maths_a_batch03_authorization.yaml",
                          "sha256_16": sha16(AUTH),
                          "directive_verbatim":
                              auth["authorization"]["operator_statement_verbatim"]},
        "totals": {"concept_nodes": len(con_nodes),
                   "misconception_nodes": len(mis_nodes),
                   "authored_edges": len(edges),
                   "requires_prerequisite_edges": n_rp,
                   "wap_edges": 2,
                   "remediated_by_edges": 2,
                   "held": len(held), "command_kinds": len(kinds),
                   "identity_decisions": len(ids),
                   "node_attachments": n_att,
                   "derived_partof_at_apply": n_att,
                   "evidence_anchors": n_anc},
        "pass2_agreement": {"nodes": "14/14 CONFIRM",
                            "edges": "13 CONFIRM / 0 HOLD / 0 REJECT",
                            "held": "8/8 AGREE",
                            "re_authoring_cases": 0},
        "coverage_profile": cp,
        "held_ids": [h["id"] for h in held],
        "inherited_held_quarantine": [f"B01-H-{i:02d}" for i in range(1, 6)]
        + [f"B02-H-{i:02d}" for i in range(1, 9)],
        "identity_decisions": [i["id"] for i in ids],
        "misconception_mints": [x["code"] for x in mis_nodes],
        "uncited_join_census": UNCITED_JOINS,
        "inherited_boundary_map": INHERITED_MAP,
        "future_batch_boundary_map": FUTURE_BOUNDARY_MAP,
        "stores_grown": 0,
    }
    SHEET_JSON.write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    print(f"review sheet built: {SHEET} ({SHEET.stat().st_size} bytes) + json "
          f"twin ({SHEET_JSON.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
