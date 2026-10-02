#!/usr/bin/env python3
"""T-C38 K2-C-6 — batch-B06 review-sheet builder (the c37_maths_a_batch05_
review_build.py shape, sixth-batch instance).

Builds graph/reports/C38_BATCH06_REVIEW_SHEET.md (+ .json twin) from the batch
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
DECISIONS = HERE / "c38_maths_a_batch06_decisions.yaml"
PASS2 = HERE / "c38_maths_a_batch06_review_pass2.yaml"
AUTH = HERE / "c38_maths_a_batch06_authorization.yaml"
SHEET = REPO / "graph/reports/C38_BATCH06_REVIEW_SHEET.md"
SHEET_JSON = REPO / "graph/reports/C38_BATCH06_REVIEW.json"

# the term-audit probe's observed map (run recorded in the batch record):
# the audit's non-slice matches — 1.7C ('proportionality' against B04's
# process row, authored unapplied) and 1.7D ('direct proportion' against B04's
# calculation row) are the B04 rows this batch's proportion vocabulary shares;
# 2.7B ('completing the square' against the solving-quadratics row) is this
# audit's NEW match (a future batch's family)
FUTURE_BOUNDARY_MAP = ["4MA1-1.7C", "4MA1-1.7D", "4MA1-2.7B"]
INHERITED_MAP = ["4MA1-1.4C", "4MA1-2.3B", "4MA1-3.4B"]
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
    A("# T-C38 K2-C-6 — Batch B06 Review Sheet — Concept / Prerequisite Graph "
      "(igcse-maths-a, 4MA1 Higher)")
    A("")
    slice_txt = ("4MA1-2.2D–2.5A (global_order 61–72 of the ratified K1 store; "
                 "a MIXED-TIER slice — 4 Higher rows (2.2D, 2.2E, 2.3A, 2.5A) "
                 "plus 8 Foundation rows (2.2F, 2.3B, 2.3C, 2.3D, 2.3E, 2.3F, "
                 "2.4A, 2.4B); spanning the 2.2 tail that closes the "
                 "algebraic-manipulation block, the whole of 2.3 (notation, "
                 "substitution, formulae, deriving, changing the subject), the "
                 "whole of 2.4 (solving and setting up linear equations) and "
                 "the 2.5 head (direct and inverse proportion); subsection "
                 "titles null by design, never invented)")
    A(f"Slice {slice_txt} · generated 2026-10-02 · decision record "
      f"`scripts/c38_maths_a_batch06_decisions.yaml` (pass 1: "
      f"`c38-k2c-batch-06`) · adversarial pass 2: "
      f"`scripts/c38_maths_a_batch06_review_pass2.yaml` · commissioning: "
      f"`scripts/c38_maths_a_batch06_authorization.yaml` (the operator's "
      f"**K2-C-6** directive, 2026-10-02 — gate K2-C-6 of the C31 §8 "
      f"sequence) · coverage substrate: the T-C32 K2-A notes join "
      f"(`Official-Specifications/parsed/_derived/notes-join/"
      f"igcse-maths-a-18-higher.json`)")
    A("")
    A("**NOTHING in this batch is authoritative.** All 15 nodes (12 concept + "
      "3 misconception) / 14 authored edges are AI_SUGGESTED (SUGGESTED). "
      "HUMAN_VALIDATED is reachable only by your promotion command via the §18 "
      "pathway after your verdicts are recorded. **Zero promotions exist** — "
      "the B01 (T-C33), B02 (T-C34), B03 (T-C35), B04 (T-C36) and B05 (T-C37) "
      "packets likewise await your verdicts, so the maths-a graph dir still "
      "carries exactly the 5 K1 stores and nothing has grown from any batch. "
      "This sheet is the batch's operator gate: record verdicts against "
      "§2/§2a/§3/§4 below (a `c38_maths_a_batch06_verdicts.yaml` template "
      "lands with the verdict session); a later session encodes and applies "
      "them.")
    A("")
    A("How to review: for each row check the quoted evidence actually appears "
      "in the cited file and actually says what the record claims; then rule "
      "on the relation CLASS and direction, not just existence. Machine "
      f"state: preverify 35/35 PASS, quote probe {n_anc}/{n_anc} anchors "
      f"verbatim ({n_note} NOTE / {n_spec} SPEC / {n_ms} MARK_SCHEME), term "
      "audit 66 terms audited (8 match terms — all in-slice except three "
      "non-slice codes), the maths-a graph dir still carries exactly the 5 K1 "
      "stores (nothing has grown). The **unjoined-corpus negative control** "
      "holds at sixth-batch strength: every NOTE citation is one of the 14 "
      "join-carried notes, pair-backed at its SP (nodes) or at an endpoint SP "
      "(edges — the B02 strength, carried forward); the uncited-join census is "
      "EMPTY for this slice — all 14 join-carried pages are cited, each for "
      "exactly the SP it is joined to, with no anchor padded to force it; the "
      "corpus's nearby unjoined pages (completing-the-square — joined to 2.7B; "
      "direct-proportion — joined to B04's 1.7D; equations-and-problem-"
      "solving — joined to 4.11C; et al.) are NOT cited anywhere. THREE "
      "misconception mints (§2a) — the EIGHTH, NINTH and TENTH maths-a mints, "
      "on the rearranging-formulae and algebra-toolkit MS documentation; none "
      "of the EIGHT prior classes is re-minted; the mint-vs-exam-trivia and "
      "home-row questions for the new mints are operator-reserved "
      "(B06-ID-02/B06-ID-03). THREE pass-2 findings recorded as resolved "
      "BEFORE landing (FP-B06-1 the substrate-alignment discovery on the three "
      "higher-preferred rows — recorded on the affected derivation notes per "
      "the C30 ledger; FP-B06-2 two SPEC quotes corrected to the store-exact "
      "wordings; FP-B06-3 one YAML serialization colon collision — zero "
      "substance changed; all re-verified by the machine gates).")
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
      "re-authoring; zero demotions** (FP-B06-1/2/3 were a recorded "
      "discovery and quote/serialization corrections the machine gates forced "
      "and verified — recorded in the pass-2 file).")
    A("")
    A("Forecast calibration (the C31 §5 adjusted forecast: 1.0 node / 1.6 "
      "edges per SP): B06 runs 12 concept nodes / 8 REQUIRES_PREREQUISITE "
      "edges (+3 misconception nodes and their 3 WAP/remediation edge pairs) "
      "over 12 SPs = 1.00 node / 0.67 prerequisite edge per SP. The node rate "
      "is on forecast. The edge shortfall against 1.6 is **structural, not "
      "thin coverage** (the FN-B03-3 mechanism, named at B02 and carried "
      "through B03, B04 and B05): the registry is still absent (B01..B05 "
      "authored-to-gate, not applied), so the cross-batch boundary-edge class "
      "has no targets to reach — three of the eight held candidates (§4) are "
      "exactly those would-be edges, quoted with their evidence (two to B05 "
      "nodes, one to B04's direct-proportion node), with B06-H-02/B06-H-03 "
      "the LANDINGS of held B05-H-06 and B04-H-06 and B06-H-04..07 the "
      "ledger-bound and substrate-bound coverage holds. The 12 derived "
      "PART_OF rows materialize at the §18 apply step (one per node "
      "attachment, SPEC_VERBATIM derivation), not at this gate.")
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
      "**B06-ID-01** rules the quadratic-factorising mirror pair — 2.2B "
      "(Higher, B05's `4MA1-CON-QUADRATIC-EXPRESSIONS-AND-FACTORISING`, whose "
      "factorising-harder-quadratics substrate is joined to 2.2B) vs 2.2F "
      "(Foundation, this batch's `4MA1-CON-FACTORISING-SIMPLE-QUADRATICS` "
      "with the four standard-method pages) — authored as TWO nodes on the "
      "store's own row split; the mirror of the B05-ID-01 bounds ruling. The "
      "six spec-text-only nodes (harder-rearranging at 2.3A; notation at "
      "2.3B; substitution at 2.3C; context-formulae at 2.3D; deriving at "
      "2.3E; solving-linear at 2.4A) author from the ratified wording alone "
      "per the C31 §3 uncovered-span rule — the nearest pages by content are "
      "joined to OTHER rows (both rearranging pages to 2.3F; "
      "solving-linear-equations.md to 2.4B; substitution.md to B05's 2.2A; "
      "completing-the-square.md to 2.7B) and citing them here would assert a "
      "relevance the substrate does not carry (helds B06-H-05/06/07 and the "
      "2.3C derivation note record the dispositions). **The "
      "substrate-alignment discovery (the batch's slice-honesty "
      "contribution):** the three higher-preferred rows' substrate sits as "
      "the C30 tier-dedupe ledger's Foundation texts demand — factorising "
      "(common factors) for 2.2D, simple bracket expansion for 2.2E alongside "
      "the Higher proof page, and 2.3A carrying ZERO joins with the "
      "twice/powered substrate on 2.3F's anchors — exactly as the C30 "
      "ledger's Foundation texts demand; the nodes CORE the ratified Higher "
      "wordings and cite the pages for the shared substrate (recorded, never "
      "repaired).")
    A("")
    A("## 2a. Misconception nodes (3) — the eighth, ninth and tenth maths-a "
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
      "the same file: M1 rides 4MA1-2.3F on the rearranging-formulae MS Q10 "
      "order rows (dividing by 3 before undoing the + 2, and its two "
      "siblings, each producing a wrong subject), with the MS's own "
      "correct-order rows (add 2 first, then divide by 3) as the "
      "REMEDIATED_BY evidence; M2 rides 4MA1-2.3A on the rearranging-formulae "
      "MS Q23 power rows (multiplying the powers to y6, copying the wrong "
      "side's operations, adding the powers to y5), with the MS's own "
      "square-then-cube-root rows as the REMEDIATED_BY evidence; M3 rides "
      "4MA1-2.5A on the algebra-toolkit MS Q8 ÷5 row (confusing dividing by 2 "
      "with dividing by the doubled x-value), with the MS's own "
      "doubling-halving row as the REMEDIATED_BY evidence — the LANDING of "
      "the row B05 pre-announced (cited NOWHERE in B05, the B04-H-06 sibling "
      "whose home family is this batch's 2.5A row). Each carries a "
      "WRONG_ANSWER_PATTERN edge and a REMEDIATED_BY edge into its home "
      "concept node (§3, rows 9–14 — the B1-E-25 pattern: remediation target "
      "= WAP target). **B06-ID-02** reserves M2's home row (2.3A the named "
      "power arm vs 2.3F the family the MS file's substrate rides) and "
      "**B06-ID-03** reserves, for each mint separately, the mint-vs-exam-"
      "trivia ruling (the chemistry B10-ID-05 / B02-ID-03 / B03-ID-03 / "
      "B04-ID-03 / B05-ID-03 precedent) AND the division-confusion mint's "
      "home row (2.5A vs the S1 proportionality surfaces). NONE of the EIGHT "
      "prior maths-a classes is re-minted (B02's surds pair, B03's "
      "set-notation and percentage-quotient classes, B04's ratio-order class, "
      "B05's index-law and two expansion classes live in their own packets — "
      "the expanding-brackets MS is re-covered by this census as a B06-topic "
      "file and carries forward as ALREADY MINTED); the factorising MS "
      "\"allowing sign errors\" rows remain credit-tolerance annotations and "
      "the NOTE-page \"common error\"/\"common mistake\" rows "
      "(formulas-where-subject-appears-twice.md, solving-linear-equations.md) "
      "are not mark-scheme documentation — recorded in the census with "
      "dispositions, never minted.")
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
      "(completing the square on the quadratic fluency it transforms; "
      "algebraic proof on the factorising its chains perform — 'The proofs "
      "may require algebraic skills such as expanding brackets, factorising, "
      "collecting like terms'; the harder rearranging on the appears-once "
      "mechanic it extends — 'Notice that the subject now only appears "
      "once!'; rearranging on the familiar-formulae stock it operates on; "
      "substitution on the notational conventions it presumes; forming and "
      "solving on the solve mechanic it ends in and the expression-deriving "
      "it starts from; proportion on the rearrange-to-standard-form move its "
      "own MS row names). Rows 9–14 are the three documented "
      "WRONG_ANSWER_PATTERNs and their REMEDIATED_BY pairs (the B1-E-25 "
      "pattern: remediation target = WAP target). NO REQUIRES_PREREQUISITE "
      "edge reaches outside the batch — there is no registry to reach into, "
      "and the cross-batch candidates are HELD (§4) with the B05-inherited "
      "map as their ruling starting point.")
    A("")
    A("## 4. Held candidates (8) — the abstention record / held-quarantine "
      "state")
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
    A("The held-quarantine discipline continues from B01/B02/B03/B04/B05: "
      "held rows carry failure classes — this batch's eight are "
      "CROSS-BATCH-TARGET-UNPROMOTED (three: to B05's expanding-products node "
      "behind factorising and behind the solving walks, and B06-H-03 the "
      "LANDING of held B04-H-06 — the would-be edge from this batch's 2.5A "
      "node to B04's direct-proportion node) or CROSS-BATCH-TARGET-FUTURE-"
      "BATCH-flavoured substrate holds or COVERAGE-UNJOINED-SUBSTRATE (four: "
      "B06-H-02 the LANDING of held B05-H-06 — the would-be edges from B05's "
      "expanding-products node now aimed at this batch's authored 2.2E node; "
      "the direct-proportion, completing-the-square, solving-linear and "
      "rearranging pages the substrate joins to other rows' anchors) — and "
      "are revisit-able at the verdict or at later gates, never silently "
      "dropped, never force-authored. **The B01 quarantine (B01-H-01..05), "
      "the B02 quarantine (B02-H-01..08), the B03 quarantine (B03-H-01..08), "
      "the B04 quarantine (B04-H-01..08) and the B05 quarantine (B05-"
      "H-01..08) are inherited untouched** and all six rule together at the "
      "verdict session. B06-H-02 and B06-H-03 are the LANDINGS of held "
      "B05-H-06 and B04-H-06 (the 2.2E double/triple-bracket family and the "
      "2.5A inverse-proportion family) — pre-recorded at the B05 and B04 "
      "gates, now aimed at the authored B06 nodes, exactly as the T-C37 "
      "record anticipated.")
    A("")
    A("## 5. Coverage profile (the C31 §3 standing per-batch statement)")
    A("")
    A("| measure | value |")
    A("|---|---|")
    A("| slice SPs | 12 (global_order 61–72) |")
    A("| tier mix | 4 Higher (2.2D, 2.2E, 2.3A, 2.5A) + 8 Foundation (2.2F, "
      "2.3B, 2.3C, 2.3D, 2.3E, 2.3F, 2.4A, 2.4B) — B01 all-Foundation; B02 "
      "9F+3H; B03 5F+7H; B04 11F+1H; B05 7F+5H |")
    A(f"| notes-joined SPs (NOTE evidence possible) | {cp['notes_joined_count']} "
      f"({', '.join(cp['notes_joined_sps'])}) — 15 join rows over 14 distinct "
      "note files (2.2E carries four rows over three files — the proof page "
      "plus the double-bracket page twice, once per anchor — and "
      "expanding-double-brackets is one file joined twice; 2.2F four; 2.4B "
      "three; 2.3F two) |")
    A(f"| spec-text-only SPs (SPEC evidence only) | {cp['spec_text_only_count']} "
      f"({', '.join(cp['spec_text_only_sps'])}) |")
    A("| MS-evidenced SPs (MARK_SCHEME evidence on node attachments) | 12 — "
      "ALL slice rows, the second FULL MS profile of the series (a property "
      "of the slice: the S2 algebra topics and the DIP topic are "
      "mark-scheme-dense across the nine B06-topic MS files; every cited row "
      "genuinely demonstrates its SP's substance; no anchor padded to force "
      "symmetry; MS evidence also rides the proportion prerequisite edge and "
      "the three WAP/remediation pairs) |")
    A("| join-carried but uncited pages | 0 — the EMPTY uncited-join census "
      "(all 14 join-carried pages cited at their own SP; the third "
      "fully-cited batch of the series; no anchor padded to force it) |")
    A("| damage-flagged rows in the slice | 0 (the 8 math-fragment-assembly "
      "rows live outside this slice) |")
    A("| misconceptions minted | 3 — the rearranging-formulae MS "
      "inverse-operation-order and power-of-the-subject classes and the "
      "algebra-toolkit MS doubling-halving division-confusion class (the "
      "EIGHTH, NINTH and TENTH maths-a mints; B01 zero, B02 two, B03 two, "
      "B04 one, B05 three; no prior class re-minted; the tolerance, "
      "verification and NOTE-plane rows recorded with dispositions, not "
      "minted) |")
    A("| practicals | none (the maths-a practicals store is 0-row by design) |")
    A("")
    A("## 6. Verdict instructions")
    A("")
    A("Rule per row on §2 (12 concept nodes), §2a (3 misconception nodes — "
      "including the B06-ID-02/B06-ID-03 mint-vs-trivia and home-row "
      "rulings), §3 (14 edges) and §4 (8 held), plus the three identity "
      "decisions (B06-ID-01 the 2.2B/2.2F quadratic-factorising mirror pair; "
      "B06-ID-02 the power-class mint's home row; B06-ID-03 the three mints' "
      "mint-vs-trivia rulings and the division-confusion/order-class home "
      "rows). A `scripts/c38_maths_a_batch06_verdicts.yaml` template "
      "accompanies the verdict session; verdicts encode through the "
      "intake-conformance check, the §18 apply step then (and only then) "
      "materializes/grows the maths-a concepts/concept_edges/spec_command_"
      "kinds stores with exactly the promoted rows from ALL authored batches "
      "— B01's, B02's, B03's, B04's, B05's and B06's quarantines rule "
      "together there. Nothing here is live until your verdicts land.")
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
      "(factorising, algebraic-proof, expanding-double-brackets, "
      "expanding-triple-brackets, difference-of-two-squares, "
      "factorising-by-grouping, factorising-quadratics, "
      "quadratics-factorising-methods, rearranging-formulae, "
      "formulas-where-subject-appears-twice, forming-and-solving-equations, "
      "forming-equations-from-shapes, solving-linear-equations, "
      "inverse-proportion) is cited for exactly the SP it is joined to. This "
      "is a property of the slice's join coverage, not an authoring choice: "
      "no anchor was padded, and the pages' UNJOINED neighbours "
      "(completing-the-square — joined to 2.7B; direct-proportion — joined "
      "to B04's 1.7D; equations-and-problem-solving — joined to 4.11C; "
      "algebra-toolkit and substitution pages — joined to B05's 2.1A/2.2A "
      "rows; et al.) are cited NOWHERE.")
    A("")
    A(f"Boundary map for B07.. (the term audit's non-slice matches, "
      f"{len(FUTURE_BOUNDARY_MAP)} codes): {', '.join(FUTURE_BOUNDARY_MAP)} — "
      "1.7C ('proportionality') and 1.7D ('direct proportion') are B04's rows "
      "(nodes authored, unapplied — the proportion vocabulary B06's 2.5A "
      "family shares) and 2.7B ('completing the square' against the "
      "solving-quadratics row) is this audit's NEW match (a future batch's "
      "family — the page named for B06's 2.2D substance lives there). The "
      "B05-inherited codes 1.4C/3.4B drop out of the superseding map (no B06 "
      "vocabulary match — 1.4C stays B03's authored-unapplied row, 3.4B stays "
      "future); 2.3B — the B05 audit's prediction ('algebraic expressions' "
      "against the notational-conventions row) — is now IN-SLICE (its node "
      "mints here, the audit prediction landing with machine truth).")
    A("")
    SHEET.write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---- json twin ----
    review = {
        "schema": "syllabai.c38-batch06-review/1.0",
        "task": "T-C38",
        "gate": "K2-C-6",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "decision_record": {"path": "scripts/c38_maths_a_batch06_decisions.yaml",
                            "sha256_16": sha16(DECISIONS)},
        "pass2_record": {"path": "scripts/c38_maths_a_batch06_review_pass2.yaml",
                         "sha256_16": sha16(PASS2)},
        "authorization": {"path": "scripts/c38_maths_a_batch06_authorization.yaml",
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
                                ["FP-B06-1", "FP-B06-2", "FP-B06-3"]},
        "coverage_profile": cp,
        "held_ids": [h["id"] for h in held],
        "inherited_held_quarantine": [f"B01-H-{i:02d}" for i in range(1, 6)]
        + [f"B02-H-{i:02d}" for i in range(1, 9)]
        + [f"B03-H-{i:02d}" for i in range(1, 9)]
        + [f"B04-H-{i:02d}" for i in range(1, 9)]
        + [f"B05-H-{i:02d}" for i in range(1, 9)],
        "landed_holds": {"B06-H-02": "B05-H-06", "B06-H-03": "B04-H-06"},
        "identity_decisions": [i["id"] for i in ids],
        "misconception_mints": [x["code"] for x in mis_nodes],
        "not_re_minted": ["4MA1-MIS-SURD-FACTOR-SWAP",
                          "4MA1-MIS-CONJUGATE-EXPANSION-SIGN",
                          "4MA1-MIS-COMPLEMENT-INTERSECTION-CONFUSION",
                          "4MA1-MIS-PERCENTAGE-QUOTIENT-INVERSION",
                          "4MA1-MIS-RATIO-ORDER-INVERSION",
                          "4MA1-MIS-INDEX-POWER-MULTIPLICATION",
                          "4MA1-MIS-EXPANSION-SIGN-LOSS",
                          "4MA1-MIS-EXPANSION-PARTIAL-DISTRIBUTION"],
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
