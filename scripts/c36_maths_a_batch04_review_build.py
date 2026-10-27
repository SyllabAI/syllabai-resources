#!/usr/bin/env python3
"""T-C36 K2-C-4 — batch-B04 review-sheet builder (the c35_maths_a_batch03_
review_build.py shape, fourth-batch instance).

Builds graph/reports/C36_BATCH04_REVIEW_SHEET.md (+ .json twin) from the batch
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
DECISIONS = HERE / "c36_maths_a_batch04_decisions.yaml"
PASS2 = HERE / "c36_maths_a_batch04_review_pass2.yaml"
AUTH = HERE / "c36_maths_a_batch04_authorization.yaml"
SHEET = REPO / "graph/reports/C36_BATCH04_REVIEW_SHEET.md"
SHEET_JSON = REPO / "graph/reports/C36_BATCH04_REVIEW.json"

# the term-audit probe's observed map (run recorded in the batch record):
# the audit's non-slice matches — 1.6A/1.6B are B03's rows (nodes authored,
# unapplied); 4.4C/6.2A/6.2D/6.3G are this audit's NEW matches (the
# 'estimate' vocabulary against the measures/statistics rows)
FUTURE_BOUNDARY_MAP = ["4MA1-1.6A", "4MA1-1.6B", "4MA1-4.4C", "4MA1-6.2A",
                       "4MA1-6.2D", "4MA1-6.3G"]
INHERITED_MAP = ["4MA1-1.1H", "4MA1-1.2A", "4MA1-1.6G", "4MA1-2.1D"]
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
    A("# T-C36 K2-C-4 — Batch B04 Review Sheet — Concept / Prerequisite Graph "
      "(igcse-maths-a, 4MA1 Higher)")
    A("")
    slice_txt = ("4MA1-1.6E–1.8D (global_order 37–48 of the ratified K1 store; "
                 "a MIXED-TIER slice — 1 Higher row (1.8A, the lightest Higher "
                 "share of the series) plus 11 Foundation rows (1.6E–1.7E "
                 "complete, 1.8B, 1.8C, 1.8D); spanning the 1.6 tail, 1.7 "
                 "complete and the 1.8 complete block; subsection titles null "
                 "by design, never invented)")
    A(f"Slice {slice_txt} · generated 2026-10-02 · decision record "
      f"`scripts/c36_maths_a_batch04_decisions.yaml` (pass 1: "
      f"`c36-k2c-batch-04`) · adversarial pass 2: "
      f"`scripts/c36_maths_a_batch04_review_pass2.yaml` · commissioning: "
      f"`scripts/c36_maths_a_batch04_authorization.yaml` (the operator's "
      f"**K2-C-4** directive, 2026-10-02 — gate K2-C-4 of the C31 §8 "
      f"sequence) · coverage substrate: the T-C32 K2-A notes join "
      f"(`Official-Specifications/parsed/_derived/notes-join/"
      f"igcse-maths-a-18-higher.json`)")
    A("")
    A("**NOTHING in this batch is authoritative.** All 13 nodes (12 concept + "
      "1 misconception) / 10 authored edges are AI_SUGGESTED (SUGGESTED). "
      "HUMAN_VALIDATED is reachable only by your promotion command via the §18 "
      "pathway after your verdicts are recorded. **Zero promotions exist** — "
      "the B01 (T-C33), B02 (T-C34) and B03 (T-C35) packets likewise await "
      "your verdicts, so the maths-a graph dir still carries exactly the 5 K1 "
      "stores and nothing has grown from any batch. This sheet is the batch's "
      "operator gate: record verdicts against §2/§2a/§3/§4 below (a "
      "`c36_maths_a_batch04_verdicts.yaml` template lands with the verdict "
      "session); a later session encodes and applies them.")
    A("")
    A("How to review: for each row check the quoted evidence actually appears "
      "in the cited file and actually says what the record claims; then rule "
      "on the relation CLASS and direction, not just existence. Machine "
      f"state: preverify 35/35 PASS, quote probe {n_anc}/{n_anc} anchors "
      f"verbatim ({n_note} NOTE / {n_spec} SPEC / {n_ms} MARK_SCHEME), term "
      "audit 72 terms audited (16 match terms — all in-slice except six "
      "non-slice codes), the maths-a graph dir still carries exactly the 5 K1 "
      "stores (nothing has grown). The **unjoined-corpus negative control** "
      "holds at fourth-batch strength: every NOTE citation is one of the 14 "
      "join-carried notes, pair-backed at its SP (nodes) or at an endpoint SP "
      "(edges — the B02 strength, carried forward); the uncited-join census is "
      "EMPTY for this slice — all 14 join-carried pages are cited, each for "
      "exactly the SP it is joined to, with no anchor padded to force it; the "
      "corpus's nearby unjoined pages (inverse-proportion — joined to 2.5A, "
      "best-buys, exchange-rates, et al.) are NOT cited anywhere. ONE "
      "misconception minted (§2a) — the FOURTH maths-a mint, on the "
      "ratio-toolkit MS part-order documentation; the B03-documented "
      "percentage-quotient class is NOT re-minted (it lives in the B03 "
      "packet) and its home-row question is inherited (B04-ID-02); the "
      "mint-vs-exam-trivia and home-row questions for the new mint are "
      "operator-reserved (B04-ID-03). NO pass-2 finding required re-authoring "
      "(FP-B04-1/FP-B04-2 are anchor-placement corrections resolved BEFORE "
      "landing, re-verified by the machine gates).")
    A("")
    A("## 1. Totals & second-pass agreement")
    A("")
    A("| | concept nodes | misconception nodes | authored edges | held | "
      "derived PART_OF (at apply) |")
    A("|---|---|---|---|---|---|")
    A(f"| pass-1 (extraction) | {len(con_nodes)} | {len(mis_nodes)} | "
      f"{len(edges)} | {len(held)} | {n_att} |")
    A(f"| pass-2 verdicts | 12 CONFIRM | 1 CONFIRM | 10 CONFIRM · 0 HOLD · 0 "
      f"REJECT | 8/8 AGREE | — |")
    A("")
    A("Raw agreement (NOT κ — single human rater, the architecture §12 "
      "convention): nodes 13/13 = 100%; edges 10/10 = 100%; pass-1 "
      "quarantined 0 edges as REVIEW_REQUIRED — every doubt was held or "
      "resolved on explicit evidence. **Zero pass-2 findings required "
      "re-authoring; zero demotions** (FP-B04-1 and FP-B04-2 were "
      "anchor-placement corrections the machine gates forced and verified — "
      "recorded in the pass-2 file).")
    A("")
    A("Forecast calibration (the C31 §5 adjusted forecast: 1.0 node / 1.6 "
      "edges per SP): B04 runs 12 concept nodes / 8 REQUIRES_PREREQUISITE "
      "edges (+1 misconception node and its 2 WAP/remediation edges) over "
      "12 SPs = 1.00 node / 0.67 prerequisite edge per SP. The node rate is "
      "on forecast. The edge shortfall against 1.6 is **structural, not thin "
      "coverage** (the FN-B03-3 mechanism, named at B02 and carried through "
      "B03): the registry is still absent (B01, B02 and B03 authored-to-gate, "
      "not applied), so the cross-batch boundary-edge class has no targets to "
      "reach — seven of the eight held candidates (§4) are exactly those "
      "would-be edges, quoted with their evidence (five to B01/B02/B03 nodes, "
      "two to future-batch families). The 12 derived PART_OF rows materialize "
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
      "**B04-ID-01** rules the compound-interest mirror pair — 1.6B (Higher, "
      "B03's `4MA1-CON-COMPOUND-INTEREST`) vs 1.6G (Foundation, this batch's "
      "`4MA1-CON-COMPOUND-INTEREST-AND-DEPRECIATION`) — authored as TWO nodes "
      "on the store's own row split; the landing of held B03-H-07. The two "
      "spec-text-only nodes (ratio-notation at 1.7A; bounds-problems at 1.8A) "
      "author from the ratified wording alone per the C31 §3 uncovered-span "
      "rule — the nearest pages by content are joined to OTHER rows "
      "(simple-ratio.md to 1.7B; the bounds page's calculations half to "
      "1.10B) and citing them here would assert a relevance the substrate "
      "does not carry (held B04-H-08 records the disposition).")
    A("")
    A("## 2a. Misconception node (1) — the fourth maths-a mint")
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
    A("The mint satisfies the chemistry contract's condition — a mark-scheme "
      "row documenting the wrong-answer class with the corrected form in the "
      "same row: M1 rides 4MA1-1.7A on the ratio-toolkit MS part-order row "
      "(writing \"32 : 27\" where 27 : 32 is meant — the radius is 27/32 of "
      "the height, so the radius must be the smaller part). It carries a "
      "WRONG_ANSWER_PATTERN edge and a REMEDIATED_BY edge into its home "
      "concept node (§3, rows 9–10) — the remediation evidence is the MS's "
      "own corrected clause. **B04-ID-03** reserves the mint-vs-exam-trivia "
      "ruling to you (the chemistry B10-ID-05 / B02-ID-03 / B03-ID-03 "
      "precedent) AND M1's home row (1.7A ratio notation vs 1.7B "
      "divide-in-a-ratio). The percentages MS Q10/Q11 inverted-quotient class "
      "documented in these same B04-topic files is NOT re-minted — it lives "
      "in the B03 packet (4MA1-MIS-PERCENTAGE-QUOTIENT-INVERSION riding "
      "1.6D) — and its home-row question (the MS questions sit closest to "
      "this slice's 1.6E) is inherited as **B04-ID-02** exactly as the "
      "T-C35 record anticipated.")
    A("")
    A("## 3. Authored semantic edges (10)")
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
      "(reverse percentages and compound interest/depreciation on the "
      "single-change multiplier walk; ratio division on the ratio notation it "
      "writes; the word-problem tier on the sharing walk it presupposes — "
      "'Simple ratio problems are discussed earlier'; direct proportion on "
      "the factor/unitary process it applies; bounds problems on bound "
      "identification, identification on the rounding that produces the "
      "degree of accuracy, and estimation on the 1-s.f. rounding rule it "
      "applies). Rows 9–10 are the documented WRONG_ANSWER_PATTERN and its "
      "REMEDIATED_BY pair (the B1-E-25 pattern: remediation target = WAP "
      "target). NO REQUIRES_PREREQUISITE edge reaches outside the batch — "
      "there is no registry to reach into, and the cross-batch candidates are "
      "HELD (§4) with the B03-inherited map as their ruling starting point.")
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
    A("The held-quarantine discipline continues from B01/B02/B03: held rows "
      "carry failure classes — this batch's eight are all "
      "CROSS-BATCH-TARGET-UNPROMOTED (five: to B03's multiplier-operator and "
      "repeated-change nodes behind the 1.6E chain, to B03's compound-"
      "interest twin, to B01's equivalent-fractions node and B03's HCF/LCM "
      "node behind the ratio-notation row) or CROSS-BATCH-TARGET-FUTURE-BATCH "
      "(two: the 2.5A inverse-proportion family; the 1.10B "
      "calculations-using-bounds family) or COVERAGE-UNJOINED-SUBSTRATE (one: "
      "the richer node shapes the substrate's own join split forbids) — and "
      "are revisit-able at the verdict or at later gates, never silently "
      "dropped, never force-authored. **The B01 quarantine (B01-H-01..05), "
      "the B02 quarantine (B02-H-01..08) and the B03 quarantine (B03-H-01..08) "
      "are inherited untouched** and all four rule together at the verdict "
      "session. B04-H-02 and B04-H-03 are the LANDINGS of held B03-H-06 "
      "(the 1.6E single-change fluency) and B03-H-07 (the 1.6B/1.6G "
      "compound-interest mirror pair) — pre-recorded at the B03 gate, now "
      "aimed at authored B04 nodes and ruling at B04-ID-01.")
    A("")
    A("## 5. Coverage profile (the C31 §3 standing per-batch statement)")
    A("")
    A("| measure | value |")
    A("|---|---|")
    A("| slice SPs | 12 (global_order 37–48) |")
    A("| tier mix | 1 Higher (4MA1-1.8A) + 11 Foundation (1.6E, 1.6F, 1.6G, "
      "1.7A, 1.7B, 1.7C, 1.7D, 1.7E, 1.8B, 1.8C, 1.8D) — the lightest Higher "
      "share of the series (B01 all-Foundation; B02 9F+3H; B03 5F+7H) |")
    A(f"| notes-joined SPs (NOTE evidence possible) | {cp['notes_joined_count']} "
      f"({', '.join(cp['notes_joined_sps'])}) — 14 join rows over 14 distinct "
      "note files (1.6F and 1.6G carry two each; 1.7B three; 1.8D one) |")
    A(f"| spec-text-only SPs (SPEC evidence only) | {cp['spec_text_only_count']} "
      f"({', '.join(cp['spec_text_only_sps'])}) |")
    A("| MS-evidenced SPs (MARK_SCHEME evidence on node attachments) | 7 "
      "(4MA1-1.6E and 1.6F via the percentages topic MS; 1.6G via the "
      "compound-interest topic MS; 1.7B via the ratio-toolkit and "
      "ratio-problem-solving topic MSes; 1.7D via the direct-and-inverse-"
      "proportion topic MS; 1.8C and 1.8D via the rounding-estimation-and-"
      "bounds topic MS — a PARTIAL MS-documentation shape, the chemistry "
      "batch-3/4/10 precedent; 1.7A additionally carries the mint's "
      "node-level MS documentation; MS evidence also rides three edges: the "
      "ratio parts walks, the connecting-link row, and the WAP/remediation "
      "pair) |")
    A("| join-carried but uncited pages | 0 — the EMPTY uncited-join census "
      "(all 14 join-carried pages cited at their own SP; the first "
      "fully-cited batch of the series; no anchor padded to force it) |")
    A("| damage-flagged rows in the slice | 0 (the 8 math-fragment-assembly "
      "rows live outside this slice) |")
    A("| misconceptions minted | 1 — the ratio-toolkit MS part-order "
      "documented class (the FOURTH maths-a mint; B01 minted zero, B02 two, "
      "B03 two; the B03-documented percentage-quotient class NOT re-minted) |")
    A("| practicals | none (the maths-a practicals store is 0-row by design) |")
    A("")
    A("## 6. Verdict instructions")
    A("")
    A("Rule per row on §2 (12 concept nodes), §2a (1 misconception node — "
      "including the B04-ID-03 mint-vs-trivia and home-row rulings), §3 (10 "
      "edges) and §4 (8 held), plus the three identity decisions (B04-ID-01 "
      "the 1.6B/1.6G compound-interest mirror pair; B04-ID-02 the inherited "
      "percentage-quotient-inversion home-row question; B04-ID-03 the mint "
      "and its home row). A `scripts/c36_maths_a_batch04_verdicts.yaml` "
      "template accompanies the verdict session; verdicts encode through the "
      "intake-conformance check, the §18 apply step then (and only then) "
      "materializes/grows the maths-a concepts/concept_edges/spec_command_"
      "kinds stores with exactly the promoted rows from ALL authored batches "
      "— B01's, B02's, B03's and B04's quarantines rule together there. "
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
      "(percentage-increases-and-decreases, basic-percentages, reverse-"
      "percentages, compound-interest, depreciation, simple-ratio, "
      "ratios-and-fdp, multiple-ratios, working-with-proportion, "
      "direct-proportion, sharing-in-a-ratio, rounding-and-estimation, "
      "bounds, related-calculations) is cited for exactly the SP it is "
      "joined to. This is a property of the slice's join coverage, not an "
      "authoring choice: no anchor was padded, and the pages' UNJOINED "
      "neighbours (inverse-proportion — joined to 2.5A; best-buys, "
      "exchange-rates, converting-between-fdp — joined to B02's 1.2G; et "
      "al.) are cited NOWHERE.")
    A("")
    A(f"Boundary map for B05.. (the term audit's non-slice matches, "
      f"{len(FUTURE_BOUNDARY_MAP)} codes): {', '.join(FUTURE_BOUNDARY_MAP)} — "
      "1.6A and 1.6B are B03's rows (nodes authored, unapplied — the "
      "percentage-change and compound-interest vocabulary B04's percentage "
      "chain shares); 4.4C ('make sensible estimates of a range of measures'), "
      "6.2A and 6.2D (the estimate-the-median/IQR rows) and 6.3G ('estimate "
      "probabilities') are this audit's NEW matches (the 'estimate' "
      "vocabulary against the measures and statistics rows — unbatched "
      "families). The B03-inherited codes 1.1H/1.2A/2.1D drop out of the "
      "superseding map (no B04 vocabulary match — 1.1H and 1.2A stay B01's "
      "authored-unapplied rows, 2.1D stays future); 1.6G is now IN-SLICE (its "
      "node mints here, confirming held B03-H-07).")
    A("")
    SHEET.write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---- json twin ----
    review = {
        "schema": "syllabai.c36-batch04-review/1.0",
        "task": "T-C36",
        "gate": "K2-C-4",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "decision_record": {"path": "scripts/c36_maths_a_batch04_decisions.yaml",
                            "sha256_16": sha16(DECISIONS)},
        "pass2_record": {"path": "scripts/c36_maths_a_batch04_review_pass2.yaml",
                         "sha256_16": sha16(PASS2)},
        "authorization": {"path": "scripts/c36_maths_a_batch04_authorization.yaml",
                          "sha256_16": sha16(AUTH),
                          "directive_verbatim":
                              auth["authorization"]["operator_statement_verbatim"]},
        "totals": {"concept_nodes": len(con_nodes),
                   "misconception_nodes": len(mis_nodes),
                   "authored_edges": len(edges),
                   "requires_prerequisite_edges": n_rp,
                   "wap_edges": 1,
                   "remediated_by_edges": 1,
                   "held": len(held), "command_kinds": len(kinds),
                   "identity_decisions": len(ids),
                   "node_attachments": n_att,
                   "derived_partof_at_apply": n_att,
                   "evidence_anchors": n_anc},
        "pass2_agreement": {"nodes": "13/13 CONFIRM",
                            "edges": "10 CONFIRM / 0 HOLD / 0 REJECT",
                            "held": "8/8 AGREE",
                            "re_authoring_cases": 0,
                            "anchor_corrections_resolved_pre_landing":
                                ["FP-B04-1", "FP-B04-2"]},
        "coverage_profile": cp,
        "held_ids": [h["id"] for h in held],
        "inherited_held_quarantine": [f"B01-H-{i:02d}" for i in range(1, 6)]
        + [f"B02-H-{i:02d}" for i in range(1, 9)]
        + [f"B03-H-{i:02d}" for i in range(1, 9)],
        "landed_holds": {"B04-H-02": "B03-H-06", "B04-H-03": "B03-H-07"},
        "identity_decisions": [i["id"] for i in ids],
        "misconception_mints": [x["code"] for x in mis_nodes],
        "not_re_minted": ["4MA1-MIS-PERCENTAGE-QUOTIENT-INVERSION"],
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
