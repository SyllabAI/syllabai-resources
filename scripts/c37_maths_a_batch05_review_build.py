#!/usr/bin/env python3
"""T-C37 K2-C-5 — batch-B05 review-sheet builder (the c36_maths_a_batch04_
review_build.py shape, fifth-batch instance).

Builds graph/reports/C37_BATCH05_REVIEW_SHEET.md (+ .json twin) from the batch
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
DECISIONS = HERE / "c37_maths_a_batch05_decisions.yaml"
PASS2 = HERE / "c37_maths_a_batch05_review_pass2.yaml"
AUTH = HERE / "c37_maths_a_batch05_authorization.yaml"
SHEET = REPO / "graph/reports/C37_BATCH05_REVIEW_SHEET.md"
SHEET_JSON = REPO / "graph/reports/C37_BATCH05_REVIEW.json"

# the term-audit probe's observed map (run recorded in the batch record):
# the audit's non-slice matches — 1.4C is B03's row (nodes authored, unapplied;
# the 'index laws'/'negative powers' vocabulary B05's index family shares);
# 2.3B ('algebraic expressions' against the notational-conventions row) and
# 3.4B ('integer powers' against the differentiation row) are this audit's NEW
# matches
FUTURE_BOUNDARY_MAP = ["4MA1-1.4C", "4MA1-2.3B", "4MA1-3.4B"]
INHERITED_MAP = ["4MA1-1.6A", "4MA1-1.6B", "4MA1-4.4C", "4MA1-6.2A",
                 "4MA1-6.2D", "4MA1-6.3G"]
UNCITED_JOINS: list[str] = []


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
    A("# T-C37 K2-C-5 — Batch B05 Review Sheet — Concept / Prerequisite Graph "
      "(igcse-maths-a, 4MA1 Higher)")
    A("")
    slice_txt = ("4MA1-1.9A–2.2C (global_order 49–60 of the ratified K1 store; "
                 "a MIXED-TIER slice — 5 Higher rows (1.9A, 2.1A, 2.2A, 2.2B, "
                 "2.2C — the second-heaviest Higher share of the series) plus "
                 "7 Foundation rows (1.10A, 1.10B, 1.10C, 1.11A, 2.1B, 2.1C, "
                 "2.1D); spanning the 1.9/1.10/1.11 tail that closes Section 1 "
                 "and the 2.1/2.2 head that opens Section 2 — the FIRST batch "
                 "of the series to cross a section boundary; subsection titles "
                 "null by design, never invented)")
    A(f"Slice {slice_txt} · generated 2026-10-02 · decision record "
      f"`scripts/c37_maths_a_batch05_decisions.yaml` (pass 1: "
      f"`c37-k2c-batch-05`) · adversarial pass 2: "
      f"`scripts/c37_maths_a_batch05_review_pass2.yaml` · commissioning: "
      f"`scripts/c37_maths_a_batch05_authorization.yaml` (the operator's "
      f"**K2-C-5** directive, 2026-10-02 — gate K2-C-5 of the C31 §8 "
      f"sequence) · coverage substrate: the T-C32 K2-A notes join "
      f"(`Official-Specifications/parsed/_derived/notes-join/"
      f"igcse-maths-a-18-higher.json`)")
    A("")
    A("**NOTHING in this batch is authoritative.** All 15 nodes (12 concept + "
      "3 misconception) / 14 authored edges are AI_SUGGESTED (SUGGESTED). "
      "HUMAN_VALIDATED is reachable only by your promotion command via the §18 "
      "pathway after your verdicts are recorded. **Zero promotions exist** — "
      "the B01 (T-C33), B02 (T-C34), B03 (T-C35) and B04 (T-C36) packets "
      "likewise await your verdicts, so the maths-a graph dir still carries "
      "exactly the 5 K1 stores and nothing has grown from any batch. This "
      "sheet is the batch's operator gate: record verdicts against §2/§2a/§3/§4 "
      "below (a `c37_maths_a_batch05_verdicts.yaml` template lands with the "
      "verdict session); a later session encodes and applies them.")
    A("")
    A("How to review: for each row check the quoted evidence actually appears "
      "in the cited file and actually says what the record claims; then rule "
      "on the relation CLASS and direction, not just existence. Machine "
      f"state: preverify 36/36 PASS, quote probe {n_anc}/{n_anc} anchors "
      f"verbatim ({n_note} NOTE / {n_spec} SPEC / {n_ms} MARK_SCHEME), term "
      "audit 81 terms audited (12 match terms — all in-slice except three "
      "non-slice codes), the maths-a graph dir still carries exactly the 5 K1 "
      "stores (nothing has grown). The **unjoined-corpus negative control** "
      "holds at fifth-batch strength: every NOTE citation is one of the 14 "
      "join-carried notes, pair-backed at its SP (nodes) or at an endpoint SP "
      "(edges — the B02 strength, carried forward); the uncited-join census is "
      "EMPTY for this slice — all 14 join-carried pages are cited, each for "
      "exactly the SP it is joined to, with no anchor padded to force it; the "
      "corpus's nearby unjoined pages (laws-of-indices and powers-and-roots — "
      "joined to B03's 1.4C/1.4A; using-a-calculator — joined to 4.5C; "
      "exchange-rates; et al.) are NOT cited anywhere. THREE misconception "
      "mints (§2a) — the FIFTH, SIXTH and SEVENTH maths-a mints, on the "
      "algebraic-roots-and-indices and expanding-brackets MS documentation; "
      "none of the five prior classes is re-minted; the mint-vs-exam-trivia "
      "and home-row questions for the new mints are operator-reserved "
      "(B05-ID-02/B05-ID-03). TWO pass-2 findings recorded as resolved BEFORE "
      "landing (FP-B05-1 the substrate-alignment discovery — the five "
      "higher-preferred rows' notes carry the Foundation-variant substances of "
      "their own codes, recorded on the affected derivation notes per the C30 "
      "ledger; FP-B05-2 the YAML serialization colon collisions — zero "
      "substance changed; both re-verified by the machine gates).")
    A("")
    A("## 1. Totals & second-pass agreement")
    A("")
    A("| | concept nodes | misconception nodes | authored edges | held | "
      "derived PART_OF (at apply) |")
    A("|---|---|---|---|---|---|")
    A(f"| pass-1 (extraction) | {len(con_nodes)} | {len(mis_nodes)} | "
      f"{len(edges)} | {len(held)} | {n_att} |")
    A(f"| pass-2 verdicts | 12 CONFIRM | 3 CONFIRM | 14 CONFIRM · 0 HOLD · 0 "
      f"REJECT | 8/8 AGREE | — |")
    A("")
    A("Raw agreement (NOT κ — single human rater, the architecture §12 "
      "convention): nodes 15/15 = 100%; edges 14/14 = 100%; pass-1 "
      "quarantined 0 edges as REVIEW_REQUIRED — every doubt was held or "
      "resolved on explicit evidence. **Zero pass-2 findings required "
      "re-authoring; zero demotions** (FP-B05-1 and FP-B05-2 were a recorded "
      "discovery and serialization corrections the machine gates forced and "
      "verified — recorded in the pass-2 file).")
    A("")
    A("Forecast calibration (the C31 §5 adjusted forecast: 1.0 node / 1.6 "
      "edges per SP): B05 runs 12 concept nodes / 8 REQUIRES_PREREQUISITE "
      "edges (+3 misconception nodes and their 3 WAP/remediation edge pairs) "
      "over 12 SPs = 1.00 node / 0.67 prerequisite edge per SP. The node rate "
      "is on forecast. The edge shortfall against 1.6 is **structural, not "
      "thin coverage** (the FN-B03-3 mechanism, named at B02 and carried "
      "through B03 and B04): the registry is still absent (B01..B04 "
      "authored-to-gate, not applied), so the cross-batch boundary-edge class "
      "has no targets to reach — five of the eight held candidates (§4) are "
      "exactly those would-be edges, quoted with their evidence (four to "
      "B01/B03/B04 nodes, one to a future-batch family), with B05-H-05 the "
      "LANDING of held B04-H-07 and B05-H-02/B05-H-08 the ledger-bound and "
      "substrate-bound coverage holds. The 12 derived PART_OF rows materialize "
      "at the §18 apply step (one per node attachment, SPEC_VERBATIM "
      "derivation), not at this gate.")
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
      "**B05-ID-01** rules the bounds mirror pair — 1.8A (Higher, B04's "
      "`4MA1-CON-BOUNDS-PROBLEMS`) vs 1.10B (Foundation, this batch's "
      "`4MA1-CON-STANDARD-UNIT-CALCULATIONS`, whose own anchor "
      "spcpt_M5rhN2mwnR2yddc6 carries the calculations-using-bounds half) — "
      "authored as TWO nodes on the store's own row split; the landing of the "
      "B04-H-07-recorded identity question. The four spec-text-only nodes "
      "(calculator at 1.11A; generalised-arithmetic at 2.1B; integer-index at "
      "2.1C; index-laws at 2.1D) author from the ratified wording alone per "
      "the C31 §3 uncovered-span rule — the nearest pages by content are "
      "joined to OTHER rows (using-a-calculator.md to 4.5C; laws-of-indices.md "
      "and algebraic-roots-and-indices.md to B03's 1.4C) and citing them here "
      "would assert a relevance the substrate does not carry (held B05-H-08 "
      "records the disposition). **The substrate-alignment discovery (the "
      "batch's slice-honesty contribution):** the five higher-preferred rows' "
      "joined notes carry the FOUNDATION-variant substances of their own codes "
      "— standard-form conversion for 1.9A, algebraic vocabulary for 2.1A, "
      "substitution for 2.2A, collecting-like-terms for 2.2B, single-bracket "
      "expansion for 2.2C — exactly as the C30 tier-dedupe ledger's Foundation "
      "texts demand; the nodes CORE the ratified Higher wordings and cite the "
      "pages for the shared substrate (recorded, never repaired).")
    A("")
    A("## 2a. Misconception nodes (3) — the fifth, sixth and seventh maths-a "
      "mints")
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
    A("Each mint satisfies the chemistry contract's condition — a mark-scheme "
      "row documenting the wrong-answer class with the corrective content in "
      "the same file: M1 rides 4MA1-2.1D on the algebraic-roots-and-indices MS "
      "common-mistake row (multiplying the powers where the product law adds "
      "them — (w¹)⁰ read for w¹ × w⁰, giving w⁰ = 1 where w is wanted), with "
      "the MS's own product-law row as the REMEDIATED_BY evidence; M2 rides "
      "4MA1-2.2A on the expanding-brackets MS sign-loss rows (forgetting the "
      "negative sign gives 2x where −2x is meant; two sign-swap siblings), "
      "with the MS's own sign-care clause as the REMEDIATED_BY evidence; M3 "
      "rides 4MA1-2.2A on the expanding-brackets MS partial-distribution rows "
      "(multiplying only part of the terms gives 12x² + 5; two siblings), with "
      "the MS's own everything-by-everything row as the REMEDIATED_BY "
      "evidence. Each carries a WRONG_ANSWER_PATTERN edge and a REMEDIATED_BY "
      "edge into its home concept node (§3, rows 9–14 — the B1-E-25 pattern: "
      "remediation target = WAP target). **B05-ID-02** reserves M1's home row "
      "(2.1D index laws vs 2.1C integer-powers-including-zero) and "
      "**B05-ID-03** reserves, for each expansion mint separately, the "
      "mint-vs-exam-trivia ruling (the chemistry B10-ID-05 / B02-ID-03 / "
      "B03-ID-03 / B04-ID-03 precedent) AND the home row (2.2A expand-the-"
      "product vs the 2.2C Foundation-variant single-bracket surface vs the "
      "future 2.2E double-bracket family). NONE of the five prior maths-a "
      "classes is re-minted (B02's surds pair, B03's set-notation and "
      "percentage-quotient classes, B04's ratio-order class live in their own "
      "packets); the factorising MS \"allowing sign errors\" rows are "
      "credit-tolerance annotations and the algebraic-fractions MS "
      "\"incorrect middle term\" rows are verification-rejection moves — both "
      "recorded in the census with dispositions, neither minted; the "
      "algebra-toolkit MS ÷5-division row documents an inverse-variation "
      "reading whose home family (2.5A) is a future batch and is cited "
      "NOWHERE (the B04-H-06 sibling).")
    A("")
    A("## 3. Authored semantic edges (14)")
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
      "(expansion on the generalised arithmetic it distributes; factorising "
      "on the grid method that expands — 'as if you had used a grid to expand "
      "the brackets'; algebraic fractions on the factorise-and-cancel and "
      "expand-the-numerator mechanics they perform — 'Check at the end to see "
      "if the top factorises'; extended fractional/negative/zero powers on the "
      "integer notation they extend; index laws on the notation they operate "
      "on; integer notation on the generalised arithmetic it instantiates; "
      "quadratics on the x² notation they exercise). Rows 9–14 are the three "
      "documented WRONG_ANSWER_PATTERNs and their REMEDIATED_BY pairs (the "
      "B1-E-25 pattern: remediation target = WAP target). NO "
      "REQUIRES_PREREQUISITE edge reaches outside the batch — there is no "
      "registry to reach into, and the cross-batch candidates are HELD (§4) "
      "with the B04-inherited map as their ruling starting point.")
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
    A("The held-quarantine discipline continues from B01/B02/B03/B04: held "
      "rows carry failure classes — this batch's eight are "
      "CROSS-BATCH-TARGET-UNPROMOTED (four: to B03's laws-of-indices family "
      "behind the standard-form operations, to B04's rounding and "
      "proportionality nodes behind money and best-buys, and B05-H-05 the "
      "LANDING of held B04-H-07 — the would-be edge from B04's bounds-problems "
      "node now aimed at this batch's 1.10B node) or "
      "CROSS-BATCH-TARGET-FUTURE-BATCH (one: the 2.2E double/triple-bracket "
      "family) or COVERAGE-UNJOINED-SUBSTRATE (two: the 1.9A Foundation-"
      "variant co-substrate question ruled by the C30 ledger's own governance; "
      "the richer node shapes the substrate's own join split forbids for "
      "1.11A/2.1C/2.1D) — and are revisit-able at the verdict or at later "
      "gates, never silently dropped, never force-authored. **The B01 "
      "quarantine (B01-H-01..05), the B02 quarantine (B02-H-01..08), the B03 "
      "quarantine (B03-H-01..08) and the B04 quarantine (B04-H-01..08) are "
      "inherited untouched** and all five rule together at the verdict "
      "session. B05-H-05 is the LANDINGS of held B04-H-07 (the 1.10B "
      "calculations-using-bounds family) — pre-recorded at the B04 gate, now "
      "aimed at the authored B05 node and ruling at B05-ID-01, exactly as the "
      "T-C36 record anticipated.")
    A("")
    A("## 5. Coverage profile (the C31 §3 standing per-batch statement)")
    A("")
    A("| measure | value |")
    A("|---|---|")
    A("| slice SPs | 12 (global_order 49–60) |")
    A("| tier mix | 5 Higher (1.9A, 2.1A, 2.2A, 2.2B, 2.2C) + 7 Foundation "
      "(1.10A, 1.10B, 1.10C, 1.11A, 2.1B, 2.1C, 2.1D) — the second-heaviest "
      "Higher share of the series (B01 all-Foundation; B02 9F+3H; B03 5F+7H; "
      "B04 11F+1H); the FIRST batch to cross a section boundary (S1 → S2) |")
    A(f"| notes-joined SPs (NOTE evidence possible) | {cp['notes_joined_count']} "
      f"({', '.join(cp['notes_joined_sps'])}) — 15 join rows over 14 distinct "
      "note files (1.9A and 1.10B carry two each; 2.2B three; 2.2C four; "
      "expanding-single-brackets is one file joined twice — its Expand-&-"
      "Simplify anchor to 2.2B and its Expanding-One-Bracket anchor to 2.2C) |")
    A(f"| spec-text-only SPs (SPEC evidence only) | {cp['spec_text_only_count']} "
      f"({', '.join(cp['spec_text_only_sps'])}) |")
    A("| MS-evidenced SPs (MARK_SCHEME evidence on node attachments) | 12 — "
      "ALL slice rows, the first FULL MS profile of the series (a property of "
      "the slice: the S2 algebra topics and the 1.9/1.10/1.11 number tail are "
      "mark-scheme-dense across the ten B05-topic MS files; every cited row "
      "genuinely demonstrates its SP's substance; no anchor padded to force "
      "symmetry; MS evidence also rides the index-laws prerequisite edge and "
      "the three WAP/remediation pairs) |")
    A("| join-carried but uncited pages | 0 — the EMPTY uncited-join census "
      "(all 14 join-carried pages cited at their own SP; the second "
      "fully-cited batch of the series; no anchor padded to force it) |")
    A("| damage-flagged rows in the slice | 0 (the 8 math-fragment-assembly "
      "rows live outside this slice) |")
    A("| misconceptions minted | 3 — the algebraic-roots-and-indices MS "
      "multiply-the-powers class and the expanding-brackets MS sign-loss and "
      "partial-distribution classes (the FIFTH, SIXTH and SEVENTH maths-a "
      "mints; B01 zero, B02 two, B03 two, B04 one; no prior class re-minted; "
      "the tolerance/verification rows recorded with dispositions, not "
      "minted) |")
    A("| practicals | none (the maths-a practicals store is 0-row by design) |")
    A("")
    A("## 6. Verdict instructions")
    A("")
    A("Rule per row on §2 (12 concept nodes), §2a (3 misconception nodes — "
      "including the B05-ID-02/B05-ID-03 mint-vs-trivia and home-row "
      "rulings), §3 (14 edges) and §4 (8 held), plus the three identity "
      "decisions (B05-ID-01 the 1.8A/1.10B bounds mirror pair; B05-ID-02 the "
      "index-law mint's home row; B05-ID-03 the two expansion mints and their "
      "home rows). A `scripts/c37_maths_a_batch05_verdicts.yaml` template "
      "accompanies the verdict session; verdicts encode through the "
      "intake-conformance check, the §18 apply step then (and only then) "
      "materializes/grows the maths-a concepts/concept_edges/spec_command_"
      "kinds stores with exactly the promoted rows from ALL authored batches "
      "— B01's, B02's, B03's, B04's and B05's quarantines rule together there. "
      "Nothing here is live until your verdicts land.")
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
    A("Uncited-join census (the negative control's transparency annex): "
      "EMPTY for this slice — every one of the 14 join-carried pages "
      "(standard-form, operations-with-standard-form, best-buys, bounds, "
      "squared-and-cubic-units, money-calculations, algebraic-vocabulary, "
      "substitution, collecting-like-terms, expanding-single-brackets, "
      "factorising-harder-quadratics, adding-and-subtracting-algebraic-"
      "fractions, multiplying-and-dividing-algebraic-fractions, "
      "solving-algebraic-fractions) is cited for exactly the SP it is joined "
      "to. This is a property of the slice's join coverage, not an authoring "
      "choice: no anchor was padded, and the pages' UNJOINED neighbours "
      "(laws-of-indices and powers-and-roots — joined to B03's 1.4C/1.4A; "
      "using-a-calculator — joined to 4.5C; exchange-rates; expanding-double-"
      "brackets and expanding-triple-brackets — joined to the future 2.2E; et "
      "al.) are cited NOWHERE.")
    A("")
    A(f"Boundary map for B06.. (the term audit's non-slice matches, "
      f"{len(FUTURE_BOUNDARY_MAP)} codes): {', '.join(FUTURE_BOUNDARY_MAP)} — "
      "1.4C is B03's row (nodes authored, unapplied — the 'index laws' and "
      "'negative powers' vocabulary B05's index family shares); 2.3B "
      "('use correct notational conventions for algebraic expressions and "
      "formulae', via 'algebraic expressions') and 3.4B ('differentiate "
      "integer powers of x', via 'integer powers') are this audit's NEW "
      "matches (unbatched families). The B04-inherited codes 1.6A/1.6B/4.4C/"
      "6.2A/6.2D/6.3G drop out of the superseding map (no B05 vocabulary "
      "match — 1.6A and 1.6B stay B03's authored-unapplied rows, the "
      "measures/statistics rows stay future); 2.1D — the B03 audit's "
      "prediction ('index laws' against the S2 row) — is now IN-SLICE (its "
      "node mints here, the audit prediction landing with machine truth).")
    A("")
    SHEET.write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---- json twin ----
    review = {
        "schema": "syllabai.c37-batch05-review/1.0",
        "task": "T-C37",
        "gate": "K2-C-5",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "decision_record": {"path": "scripts/c37_maths_a_batch05_decisions.yaml",
                            "sha256_16": sha16(DECISIONS)},
        "pass2_record": {"path": "scripts/c37_maths_a_batch05_review_pass2.yaml",
                         "sha256_16": sha16(PASS2)},
        "authorization": {"path": "scripts/c37_maths_a_batch05_authorization.yaml",
                          "sha256_16": sha16(AUTH),
                          "directive_verbatim":
                              auth["authorization"]["operator_statement_verbatim"]},
        "totals": {"concept_nodes": len(con_nodes),
                   "misconception_nodes": len(mis_nodes),
                   "authored_edges": len(edges),
                   "requires_prerequisite_edges": n_rp,
                   "wap_edges": 3,
                   "remediated_by_edges": 3,
                   "held": len(held), "command_kinds": len(kinds),
                   "identity_decisions": len(ids),
                   "node_attachments": n_att,
                   "derived_partof_at_apply": n_att,
                   "evidence_anchors": n_anc},
        "pass2_agreement": {"nodes": "15/15 CONFIRM",
                            "edges": "14 CONFIRM / 0 HOLD / 0 REJECT",
                            "held": "8/8 AGREE",
                            "re_authoring_cases": 0,
                            "anchor_corrections_resolved_pre_landing":
                                ["FP-B05-1", "FP-B05-2"]},
        "coverage_profile": cp,
        "held_ids": [h["id"] for h in held],
        "inherited_held_quarantine": [f"B01-H-{i:02d}" for i in range(1, 6)]
        + [f"B02-H-{i:02d}" for i in range(1, 9)]
        + [f"B03-H-{i:02d}" for i in range(1, 9)]
        + [f"B04-H-{i:02d}" for i in range(1, 9)],
        "landed_holds": {"B05-H-05": "B04-H-07"},
        "identity_decisions": [i["id"] for i in ids],
        "misconception_mints": [x["code"] for x in mis_nodes],
        "not_re_minted": ["4MA1-MIS-SURD-FACTOR-SWAP",
                          "4MA1-MIS-CONJUGATE-EXPANSION-SIGN",
                          "4MA1-MIS-COMPLEMENT-INTERSECTION-CONFUSION",
                          "4MA1-MIS-PERCENTAGE-QUOTIENT-INVERSION",
                          "4MA1-MIS-RATIO-ORDER-INVERSION"],
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
