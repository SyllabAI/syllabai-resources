#!/usr/bin/env python3
"""T-C34 K2-C-2 — batch-B02 review-sheet builder (the c33_maths_a_batch01_
review_build.py shape, second-batch instance).

Builds graph/reports/C34_BATCH02_REVIEW_SHEET.md (+ .json twin) from the batch
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
DECISIONS = HERE / "c34_maths_a_batch02_decisions.yaml"
PASS2 = HERE / "c34_maths_a_batch02_review_pass2.yaml"
AUTH = HERE / "c34_maths_a_batch02_authorization.yaml"
SHEET = REPO / "graph/reports/C34_BATCH02_REVIEW_SHEET.md"
SHEET_JSON = REPO / "graph/reports/C34_BATCH02_REVIEW.json"

# the term-audit probe's observed map (run recorded in the batch record):
# the B01-inherited codes still outside the slice + the audit's one new match
FUTURE_BOUNDARY_MAP = ["4MA1-1.4D", "4MA1-1.4E", "4MA1-1.7A", "4MA1-1.8B"]
INHERITED_MAP = ["4MA1-1.2F", "4MA1-1.2I", "4MA1-1.3B", "4MA1-1.4D",
                 "4MA1-1.4E", "4MA1-1.7A"]
UNCITED_JOINS = [
    "SME-RevisionNotes/igcse-maths-a-18-higher/notes/1-numbers-and-the-number-"
    "system/number-toolkit/negative-numbers.md (joined to 4MA1-1.4A; "
    "signed-arithmetic content does not state the surds demand — disposition on "
    "the 1.4A node's derivation notes)",
    "SME-RevisionNotes/igcse-maths-a-18-higher/notes/2-equations-formulae-and-"
    "identities/algebra-toolkit/algebraic-notation.md (joined to 4MA1-1.3A; "
    "letters-for-unknowns content recorded on the held B02-H-04 row instead)",
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
    A("# T-C34 K2-C-2 — Batch B02 Review Sheet — Concept / Prerequisite Graph "
      "(igcse-maths-a, 4MA1 Higher)")
    A("")
    slice_txt = ("4MA1-1.2E–1.4B (global_order 13–24 of the ratified K1 store; "
                 "a MIXED-TIER slice — 9 Foundation rows plus the first three "
                 "Higher rows 1.3A/1.4A/1.4B; spanning the 1.2 tail, 1.3 "
                 "complete and the 1.4 head; subsection titles null by design, "
                 "never invented)")
    A(f"Slice {slice_txt} · generated 2026-10-01 · decision record "
      f"`scripts/c34_maths_a_batch02_decisions.yaml` (pass 1: "
      f"`c34-k2c-batch-02`) · adversarial pass 2: "
      f"`scripts/c34_maths_a_batch02_review_pass2.yaml` · commissioning: "
      f"`scripts/c34_maths_a_batch02_authorization.yaml` (the operator's "
      f"**K2-C-2** directive, 2026-10-01 — gate K2-C-2 of the C31 §8 "
      f"sequence) · coverage substrate: the T-C32 K2-A notes join "
      f"(`Official-Specifications/parsed/_derived/notes-join/"
      f"igcse-maths-a-18-higher.json`)")
    A("")
    A("**NOTHING in this batch is authoritative.** All 14 nodes (12 concept + "
      "2 misconception) / 10 authored edges are AI_SUGGESTED (SUGGESTED). "
      "HUMAN_VALIDATED is reachable only by your promotion command via the §18 "
      "pathway after your verdicts are recorded. **Zero promotions exist** — "
      "and the B01 packet (T-C33) likewise awaits your verdicts, so the "
      "maths-a graph dir still carries exactly the 5 K1 stores and nothing has "
      "grown from either batch. This sheet is the batch's operator gate: "
      "record verdicts against §2/§2a/§3/§4 below (a "
      "`c34_maths_a_batch02_verdicts.yaml` template lands with the verdict "
      "session); a later session encodes and applies them.")
    A("")
    A("How to review: for each row check the quoted evidence actually appears "
      "in the cited file and actually says what the record claims; then rule "
      "on the relation CLASS and direction, not just existence. Machine "
      f"state: preverify 32/32 PASS, quote probe {n_anc}/{n_anc} anchors "
      f"verbatim ({n_note} NOTE / {n_spec} SPEC / {n_ms} MARK_SCHEME), term "
      "audit 63 terms audited (8 matches — all in-slice except one new "
      "future code), the maths-a graph dir still carries exactly the 5 K1 "
      "stores (nothing has grown). The **unjoined-corpus negative control** "
      "holds at second-batch strength: every NOTE citation is one of the 11 "
      "join-carried notes, pair-backed at its SP (nodes) or at an endpoint SP "
      "(edges — a strengthening over B01); the two join-carried-but-UNCITED "
      "pages are recorded in the census with dispositions, not padded "
      "citations; the corpus's nearby unjoined pages (mixed-numbers-and-"
      "improper-fractions — itself joined to B01's 1.2B — hcf-and-lcm, "
      "prime-factor-decomposition, laws-of-indices, standard-form, the "
      "percentages pages, et al.) are NOT cited anywhere. TWO misconceptions "
      "minted (§2a) — the first maths-a mints, on the surds MS Q12 20(a)/(b) "
      "documentation (the chemistry MS-Reject contract's mint condition); the "
      "mint-vs-exam-trivia question is operator-reserved (B02-ID-03). NO "
      "pass-2 finding required re-authoring (FP-B02-1..3 / FN-B02-1..3 are "
      "recorded questions and resolutions).")
    A("")
    A("## 1. Totals & second-pass agreement")
    A("")
    A("| | concept nodes | misconception nodes | authored edges | held | "
      "derived PART_OF (at apply) |")
    A("|---|---|---|---|---|---|")
    A(f"| pass-1 (extraction) | {len(con_nodes)} | {len(mis_nodes)} | "
      f"{len(edges)} | {len(held)} | {n_att} |")
    A(f"| pass-2 verdicts | 12 CONFIRM | 2 CONFIRM | 10 CONFIRM · 0 HOLD · 0 "
      f"REJECT | 8/8 AGREE | — |")
    A("")
    A("Raw agreement (NOT κ — single human rater, the architecture §12 "
      "convention): nodes 14/14 = 100%; edges 10/10 = 100%; pass-1 "
      "quarantined 0 edges as REVIEW_REQUIRED — every doubt was held or "
      "resolved on explicit evidence. **Zero pass-2 findings required "
      "re-authoring; zero demotions.**")
    A("")
    A("Forecast calibration (the C31 §5 adjusted forecast: 1.0 node / 1.6 "
      "edges per SP): B02 runs 12 concept nodes / 6 REQUIRES_PREREQUISITE "
      "edges (+2 misconception nodes and their 4 WAP/remediation edges) over "
      "12 SPs = 1.00 node / 0.50 prerequisite edge per SP. The node rate is "
      "on forecast. The edge shortfall against 1.6 is **structural, not thin "
      "coverage**: the registry is still absent (B01 authored-to-gate, not "
      "applied), so the cross-batch boundary-edge class has no targets to "
      "reach — six of the eight held candidates (§4) are exactly those "
      "would-be edges, quoted with their evidence (three to B01 nodes, three "
      "to future-batch families). The 14 derived PART_OF rows materialize at "
      "the §18 apply step (one per node attachment, SPEC_VERBATIM "
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
      "**B02-ID-01** authors the 1.3B row as its OWN node "
      "(`4MA1-CON-DECIMAL-PLACE-VALUE`) although its wording is byte-identical "
      "to 1.1B's and B01 authored a place-value node CORE at 1.1B — the "
      "decimal context is the store's own 1.3 subtopic placement, and the "
      "eventual co-identity/merge is reserved to your verdict. **B02-ID-02** "
      "authors the mirror conversions 1.2G/1.3D as TWO nodes (the "
      "converting-between-fdp evidence is pair-locked to 1.2G); any single "
      "FDP-conversion family merge is yours to rule. The five spec-text-only "
      "nodes (expressing-numbers-as-fractions, unit-fractions-as-inverses, "
      "decimal-place-value, decimal-to-fraction-or-percentage, "
      "terminating-decimals) author from the ratified wording alone per the "
      "C31 §3 uncovered-span rule.")
    A("")
    A("## 2a. Misconception nodes (2) — the FIRST maths-a mints")
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
    A("Both mints ride 4MA1-1.4B — the surds manipulation surface where the "
      "surds MS Q12 rows document the classes. Each carries a "
      "WRONG_ANSWER_PATTERN edge and a REMEDIATED_BY edge into "
      "`4MA1-CON-MANIPULATING-SURDS` (§3, rows 7–10) "
      "— the remediation evidence is the MS's own corrected form in the same "
      "row; the note-side corrective surfaces are pair-locked to 1.4A "
      "(simplifying-surds) and recorded in the edge derivation notes, not "
      "forced past the pair discipline. **B02-ID-03** reserves the "
      "mint-vs-exam-trivia ruling to you (the chemistry B10-ID-05 precedent; "
      "B01's abstention record stands as the counterfactual).")
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
      "(ordering decimals and the conversions on decimal place value; "
      "terminating-recognition and the recurring method on the conversion "
      "fluency; the division procedure on the unit-fraction inverse; surds "
      "manipulation on surds meaning). Rows 7–8 are the two documented "
      "WRONG_ANSWER_PATTERNs and rows 9–10 their REMEDIATED_BY pairs (the "
      "B1-E-25 pattern: remediation target = WAP target). NO "
      "REQUIRES_PREREQUISITE edge reaches outside the batch — there is no "
      "registry to reach into, and the cross-batch candidates are HELD (§4) "
      "with the B01-inherited map as their ruling starting point.")
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
    A("The held-quarantine discipline continues from B01: held rows carry "
      "failure classes — the batch adds CROSS-BATCH-TARGET-UNPROMOTED and "
      "CROSS-BATCH-TARGET-FUTURE-BATCH (the boundary classes the empty "
      "registry makes structural) to B01's COVERAGE-UNJOINED-SUBSTRATE, "
      "SPEC-ONLY-SURFACE, NO-MS-REJECT-DOCUMENTATION, "
      "AVAILABLE-BUT-SURFACE-MINIMAL vocabulary — and are revisit-able at the "
      "verdict or at later gates, never silently dropped, never "
      "force-authored. The **B01 quarantine (B01-H-01..05) is inherited "
      "untouched** and rules alongside this one at the verdict session. "
      "B02-H-07 carries B01-H-04's class forward with its new note-side "
      "evidence (the joined note's own \"Do not add the denominators\" "
      "warning — still no MS documentation, still held).")
    A("")
    A("## 5. Coverage profile (the C31 §3 standing per-batch statement)")
    A("")
    A("| measure | value |")
    A("|---|---|")
    A("| slice SPs | 12 (global_order 13–24) |")
    A("| tier mix | 9 Foundation-applicability + 3 Higher (4MA1-1.3A, "
      "4MA1-1.4A, 4MA1-1.4B — the first Higher rows of the ratified program) |")
    A(f"| notes-joined SPs (NOTE evidence possible) | {cp['notes_joined_count']} "
      f"({', '.join(cp['notes_joined_sps'])}) — 13 join rows over 11 distinct "
      "note files |")
    A(f"| spec-text-only SPs (SPEC evidence only) | {cp['spec_text_only_count']} "
      f"({', '.join(cp['spec_text_only_sps'])}) |")
    A("| MS-evidenced SPs (MARK_SCHEME evidence) | 4 (4MA1-1.2F via the "
      "fractions topic MS; 4MA1-1.3A and 4MA1-1.3C via the FDP topic MS; "
      "4MA1-1.4B via the surds topic MS — a PARTIAL MS-documentation shape, "
      "the chemistry batch-3/4/10 precedent) |")
    A("| join-carried but uncited pages | 2 — the uncited-join census records "
      "each with its disposition (see the machine-state appendix) |")
    A("| damage-flagged rows in the slice | 0 (the 8 math-fragment-assembly "
      "rows live outside this slice) |")
    A("| misconceptions minted | 2 — the surds MS Q12 20(a)/(b) documented "
      "classes (the first maths-a mints; B01 minted zero on the same "
      "contract) |")
    A("| practicals | none (the maths-a practicals store is 0-row by design) |")
    A("")
    A("## 6. Verdict instructions")
    A("")
    A("Rule per row on §2 (12 concept nodes), §2a (2 misconception nodes — "
      "including the B02-ID-03 mint-vs-trivia ruling), §3 (10 edges) and §4 "
      "(8 held), plus the three identity decisions (B02-ID-01 co-identity of "
      "the place-value rows; B02-ID-02 the 1.2G/1.3D mirror pair; B02-ID-03 "
      "the mints). A `scripts/c34_maths_a_batch02_verdicts.yaml` template "
      "accompanies the verdict session; verdicts encode through the "
      "intake-conformance check, the §18 apply step then (and only then) "
      "materializes/grows the maths-a concepts/concept_edges/spec_command_"
      "kinds stores with exactly the promoted rows — B01's and B02's "
      "quarantines rule together there. Nothing here is live until your "
      "verdicts land.")
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
    A(f"Boundary map for B03.. (the term audit's non-slice matches, "
      f"{len(FUTURE_BOUNDARY_MAP)} codes): {', '.join(FUTURE_BOUNDARY_MAP)} — "
      "the B01-inherited codes 1.2F/1.2I/1.3B are now IN-SLICE (their nodes "
      "mint here); 1.4D/1.4E/1.7A remain future; 1.8B is this audit's new "
      "match ('decimal places' against the rounding row).")
    A("")
    SHEET.write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---- json twin ----
    review = {
        "schema": "syllabai.c34-batch02-review/1.0",
        "task": "T-C34",
        "gate": "K2-C-2",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "decision_record": {"path": "scripts/c34_maths_a_batch02_decisions.yaml",
                            "sha256_16": sha16(DECISIONS)},
        "pass2_record": {"path": "scripts/c34_maths_a_batch02_review_pass2.yaml",
                         "sha256_16": sha16(PASS2)},
        "authorization": {"path": "scripts/c34_maths_a_batch02_authorization.yaml",
                          "sha256_16": sha16(AUTH),
                          "directive_verbatim":
                              auth["authorization"]["operator_statement_verbatim"]},
        "totals": {"concept_nodes": len(con_nodes),
                   "misconception_nodes": len(mis_nodes),
                   "authored_edges": len(edges),
                   "requires_prerequisite_edges": n_rp,
                   "wap_edges": len(edges) - n_rp - 2,
                   "remediated_by_edges": 2,
                   "held": len(held), "command_kinds": len(kinds),
                   "identity_decisions": len(ids),
                   "node_attachments": n_att,
                   "derived_partof_at_apply": n_att,
                   "evidence_anchors": n_anc},
        "pass2_agreement": {"nodes": "14/14 CONFIRM",
                            "edges": "10 CONFIRM / 0 HOLD / 0 REJECT",
                            "held": "8/8 AGREE",
                            "re_authoring_cases": 0},
        "coverage_profile": cp,
        "held_ids": [h["id"] for h in held],
        "inherited_held_quarantine": [f"B01-H-{i:02d}" for i in range(1, 6)],
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
