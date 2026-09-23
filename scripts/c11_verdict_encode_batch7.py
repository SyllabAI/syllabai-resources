#!/usr/bin/env python3
"""T-C11 session 60 — encode the OPERATOR VERDICT SET for §16 batch 7 into
the operator-owned verdict record scripts/c11_batch7_verdicts.yaml.

The operator ruled on the batch-7 gate (review sheet
graph/reports/C11_BATCH7_REVIEW_SHEET.md, session-59 package) with the
operator verdict ADDENDUM (delivered to the verdict session in-chat,
2026-09-23, after the web-lane upload of
C11_BATCH7_REVIEW_SHEET_COMPLETED.md failed to land — the delivery-gap
record is in meta.operator_ruling.delivery): "Status: PASS WITH NOTES",
all 15 node verdicts accepted (13 CONCEPT + 2 MISCONCEPTION; the retained
pass-2 CONFIRM_WITH_NOTE on CON-NEUTRALISATION), all 19 authored edges
CONFIRM with TWO explicit semantic guardrails (B7-E-02 the acid+metal
route dependency; B7-E-10 the sanctioned-boundary ownership), the six
identity decisions KEEP_AS_IS each with a recorded rationale, the 9 held
candidates ACKNOWLEDGED / KEEP QUARANTINED with per-candidate reasons,
zero RR, zero REJECT, and the final directive to proceed through the
normal C11 pathway (template -> verdicts.yaml -> encode/reconcile ->
c11_promote.py -> regenerate -> rerun the complete gate suite). This
script encodes the per-row decisions from that addendum — no verdict
invented, no evidence reinterpreted, no ID guessed. Fail-closed:

  * refuses if the filled verdict record already exists (no double-apply);
  * refuses if any verdict field in the template is already filled;
  * refuses unless the addendum carries the §6/§7 verdict surface with
    the expected markers (this intake is an ADDENDUM, not a §1-5+§6
    completed-sheet copy — the §1-5 drift check of the batch-5/6 intakes
    does not apply; the addendum's verdict content is instead reconciled
    1:1 against the in-repo gate sheet §2/§3 surfaces and the batch-7
    decision record, machine-checked below);
  * refuses if the addendum's node (id, code) pairs do not match the
    gate sheet's §2 table order exactly, or its named edge triples do not
    match the template rows (E-02 / E-10 / the two practical edges);
  * refuses if the template rows do not reconcile 1:1 against the batch-7
    decision record (19 SUGGESTED edge triples / ZERO RR triples / 15 node
    codes [13 CONCEPT + 2 MISCONCEPTION] / 9 held candidates);
  * refuses if the live store is not in the sanctioned pre-verdict state
    (187 semantic HUMAN_VALIDATED == the pilot+batch-1..6 §18 promotions;
    0 batch-7 promotions; §16 authorization AUTHORIZED; 157 nodes / 367
    edges / 156 PART_OF rows with the T-C19 G19 record's 117
    HUMAN_VALIDATED PART_OF; the SUGGESTED surface exactly the 19
    batch-7 authored edges + the 3 frozen pilot HOLDs; the 2 frozen pilot
    REVIEW_REQUIRED settlements untouched).

Encoding rules (recorded verbatim in the file's operator_ruling.mapping):
  * every edge row          -> CONFIRM  (B7-E-02 and B7-E-10 carry the
    operator's CONFIRM_WITH_NOTE qualifications in notes — the
    verdict-record vocabulary CONFIRM|REJECT|HOLD|MERGE|SPLIT has no
    WITH_NOTE value; the batch-1..6 precedent is that qualifications ride
    in notes)
  * every node row          -> CONFIRM  (the retained pass-2
    CONFIRM_WITH_NOTE row — CON-NEUTRALISATION — carries the retained
    pass-2 qualification in notes)
  * every identity decision -> KEEP_AS_IS (the operator's §6 rationale
    table, verbatim)
  * RR settlement           -> NONE RECORDED: this batch authored no
    REVIEW_REQUIRED edge, so no settlement row exists in the template
  * held appendix           -> acknowledged (9 preserved, quarantined)

IDENTITY-SAFETY NOTE (the sheet-vs-template numbering hazard): the review
sheet's section-2 rows and the operator addendum's node table number
nodes in TABLE order (sheet B7-N-01 = CON-INDICATORS = decision-record
order) while the template numbers them alphabetically by code (template
B7-N-01 = CON-ACID-ALKALI-IONS). Verdicts and notes here are therefore
keyed by TRIPLE (edges) and CODE (nodes), never by row id, and the
addendum's (id, code) pairs are asserted against the gate sheet §2 table
order before anything is written. The edge ids COINCIDE between the
sheet §3 rows and the template (both orders agree row-for-row), and the
explicitly named B7-E-02 / B7-E-10 / PR-07 / PR-08 triples are identical
in both — each asserted against the template before encoding.

The operator's REPORTED-state caveat is recorded verbatim: the reported
157-node / 367-edge store and 95/0/0 battery were treated by the operator
as REPORTED (the decision/pass-2/boundary YAMLs were not independently
accessible through the GitHub connector); the verdict session verified
the machine state directly at d6eba2d (the authoring head) before
encoding, closing that verification gap.

This script WRITES ONLY scripts/c11_batch7_verdicts.yaml (and removes the
now-renamed template, per the sheet's gate pathway). It promotes nothing
and re-authors no decision record; application (§18 promotion) is the
separate sanctioned step in this same session per the operator's §7
directive — the addendum names the chain: encode/reconcile ->
c11_promote.py -> regenerate -> rerun the complete gate suite.

Usage:
  python3 scripts/c11_verdict_encode_batch7.py COMPLETED_ADDENDUM.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry

GRAPH = GP.qual_dir()          # the qual's ratified store dir
TEMPLATE = HERE / "c11_batch7_verdicts_template.yaml"
VERDICTS = HERE / "c11_batch7_verdicts.yaml"
DECISIONS = HERE / "c11_batch7_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"
S16_AUTH = HERE / "c11_s16_authorization.yaml"
GATE_SHEET = GP.reports_dir() / "C11_BATCH7_REVIEW_SHEET.md"

SESSION = 60
TODAY = "2026-09-23"
# Verbatim operative text from the operator's verdict addendum §7 ("Final
# operator gate" + directive, C11_BATCH7_REVIEW_SHEET_COMPLETED intake,
# 2026-09-23).
OPERATOR_STATEMENT = (
    "Final operator gate: Nodes 15/15 confirmed; Authored semantic edges "
    "19/19 confirmed; Semantic guardrails 2 CONFIRM_WITH_NOTE; Identity "
    "decisions 6/6 KEEP_AS_IS; Held candidates 9/9 acknowledged and "
    "quarantined; REVIEW_REQUIRED edges 0; Rejected authored edges 0; "
    "Batch-7 promotions 0; Authority status SUGGESTED. Operator verdict: "
    "PASS WITH NOTES — proceed through the normal C11 pathway: "
    "c11_batch7_verdicts_template.yaml -> c11_batch7_verdicts.yaml -> "
    "encode/reconcile -> c11_promote.py -> regenerate -> rerun the "
    "complete gate suite. This operator verdict does not itself "
    "constitute HUMAN_VALIDATED promotion.")

# The operator's two semantic guardrails (§6 Edge verdicts), verbatim —
# recorded CONFIRM per the vocabulary rule with the qualification here.
GUARDRAIL_NOTES = {
    "4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER": (
        "Operator §6 (session 60): CONFIRM_WITH_NOTE retained — 'Treat "
        "this as the acid+metal route dependency evidenced by the sheet. "
        "Do not generalize it into a universal prerequisite for every "
        "acid reaction represented by 4CH1-CON-ACID-REACTIONS.' Pass-2: "
        "sanctioned cross-section boundary edge (session-59 ruling) into "
        "the batch-6 CON-REACT-ORDER owner — the 2.37 placement row is "
        "the above-hydrogen reactivity fact applied, never re-defined."),
    "4CH1-CON-SOLUBILITY-RULES REQUIRES_PREREQUISITE "
    "4CH1-CON-ION-CHARGE-RULES": (
        "Operator §6 (session 60): CONFIRM_WITH_NOTE retained — "
        "'Preserve the sanctioned boundary ownership and do not mint a "
        "duplicate CON-ION-CHARGE-RULES concept inside Batch 7.' Pass-2: "
        "sanctioned cross-section boundary edge (session-59 ruling) into "
        "the batch-3 CON-ION-CHARGE-RULES owner — the 2.34 ion-family "
        "rules row applies the owner's framework as given."),
}

# The remaining operator CONFIRM notes (evidence-grounded context per row;
# keyed by TRIPLE). The operator's blanket §6 ruling covers all 19 edges;
# these notes carry the per-row grounding, the practical-ownership shape,
# and the misconception-pair documentation.
EDGE_NOTES = {
    "4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION": (
        "Operator §6: CONFIRM — definitional dependency ('When an acid "
        "reacts with a base, a neutralisation reaction occurs'); the "
        "base/carbonate rows of 2.37 are classified by the 2.32 concept."),
    "4CH1-CON-BASES-ALKALIS REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION": (
        "Operator §6: CONFIRM — definitional containment ('Bases are "
        "substances which can neutralise an acid, forming a salt and "
        "water'); the neutralising function is the base definition "
        "applied."),
    "4CH1-CON-NEUTRALISATION REQUIRES_PREREQUISITE 4CH1-CON-ACID-ALKALI-IONS": (
        "Operator §6: CONFIRM — the mechanism sentence is the "
        "definitional dependency verbatim ('A neutralisation reaction "
        "occurs when an acid reacts with an alkali')."),
    "4CH1-CON-PROTON-TRANSFER REQUIRES_PREREQUISITE 4CH1-CON-ACID-ALKALI-IONS": (
        "Operator §6: CONFIRM — '\"extends the earlier definition\" is "
        "the teach-sequence statement verbatim'; the transfer framework "
        "presupposes the solution-ion picture (B7-ID-01 KEEP_AS_IS)."),
    "4CH1-CON-SALT-INSOLUBLE-REACTANT REQUIRES_PREREQUISITE "
    "4CH1-CON-ACID-REACTIONS": (
        "Operator §6: CONFIRM — the excess-base route RUNS the acid "
        "reaction family ('A soluble salt can be made from the reaction "
        "of an acid with an insoluble base'); route presupposes the "
        "reaction class."),
    "4CH1-CON-SALT-INSOLUBLE-REACTANT REQUIRES_PREREQUISITE "
    "4CH1-CON-SOLUBILITY-RULES": (
        "Operator §6: CONFIRM — method selection IS the solubility frame "
        "applied ('A knowledge of the solubility of ionic compounds "
        "helps us to determine the most appropriate method'); "
        "load-bearing, not framing."),
    "4CH1-CON-SALT-PRECIPITATION REQUIRES_PREREQUISITE "
    "4CH1-CON-SOLUBILITY-RULES": (
        "Operator §6: CONFIRM — the precipitation route presupposes the "
        "insolubility rule ('Insoluble salts can be prepared using a "
        "precipitation reaction'; 'The solid salt obtained is the "
        "precipitate')."),
    "4CH1-CON-SALT-TITRATION-ROUTE REQUIRES_PREREQUISITE 4CH1-CON-TITRATION": (
        "Operator §6: CONFIRM — the route names the technique ('A "
        "titration can be used for this'); explicit teach-sequence."),
    "4CH1-CON-TITRATION REQUIRES_PREREQUISITE 4CH1-CON-INDICATORS": (
        "Operator §6: CONFIRM — the sharp-change requirement makes "
        "indicator knowledge load-bearing for the method ('Add a few "
        "drops of a suitable indicator'); the litmus-unsuitable teaching "
        "is the negative case of the same dependency."),
    "4CH1-CON-TITRATION REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION": (
        "Operator §6: CONFIRM — the purpose sentence defines the "
        "endpoint as the neutralisation point ('exactly how much alkali "
        "is needed to neutralise a quantity of acid') — load-bearing."),
    "4CH1-CON-UNIVERSAL-INDICATOR REQUIRES_PREREQUISITE 4CH1-CON-PH-SCALE": (
        "Operator §6: CONFIRM — measuring presupposes the measured "
        "quantity ('the colour is matched with a colour chart'); "
        "direction correct."),
    "4CH1-MIS-ENDPOINT-PH-ABOVE-7 WRONG_ANSWER_PATTERN 4CH1-CON-NEUTRALISATION": (
        "Operator §6: CONFIRM — the pinned Titrations MS Q2a(iv) Reject "
        "column ('Reject changing to any pH value > 7') documents the "
        "wrong-answer class against the neutralisation-endpoint "
        "expected answer; B7-ID-05 KEEP_AS_IS (single assessment-"
        "documented misconception surface)."),
    "4CH1-MIS-ENDPOINT-PH-ABOVE-7 REMEDIATED_BY 4CH1-CON-NEUTRALISATION": (
        "Operator §6: CONFIRM — remediation target = WAP target (the "
        "B1-E-25 pattern); the corrective content is the concept's own "
        "mechanism sentence ('A neutralisation reaction occurs when an "
        "acid reacts with an alkali'); ruled WITH the concept row "
        "(B7-ID-05)."),
    "4CH1-MIS-PRECIPITATE-IN-FILTRATE WRONG_ANSWER_PATTERN "
    "4CH1-CON-SALT-PRECIPITATION": (
        "Operator §6: CONFIRM — the pinned Salt-Prep MS Q2a(iii) class "
        "('they would obtain sodium nitrate instead') documents the "
        "filtrate/residue confusion; B7-ID-06 KEEP_AS_IS (single "
        "assessment-documented misconception surface)."),
    "4CH1-MIS-PRECIPITATE-IN-FILTRATE REMEDIATED_BY 4CH1-CON-SALT-PRECIPITATION": (
        "Operator §6: CONFIRM — remediation target = WAP target; the "
        "corrective content is the route's own separation step ('The "
        "precipitate is recovered by filtration')."),
    "4CH1-PR-07 REQUIRES_PREREQUISITE 4CH1-CON-SALT-INSOLUBLE-REACTANT": (
        "Operator §6: CONFIRM — practical->conceptual (the "
        "PR-05/PR-06 shape): the 2.42 practical RUNS the excess-base "
        "route its concept owns ('To prepare a pure, dry sample of "
        "hydrated copper(II) sulfate crystals'); 2.42 attaches NO "
        "concept node (the 1.13/1.60C/2.14/2.21 precedent)."),
    "4CH1-PR-08 REQUIRES_PREREQUISITE 4CH1-CON-SALT-PRECIPITATION": (
        "Operator §6: CONFIRM — practical->conceptual (the "
        "PR-05/PR-06 shape): the 2.43C practical RUNS the precipitation "
        "route its concept owns; 2.43C attaches NO concept node. Pass-2 "
        "FP-B7-4: the edge anchors sit on the aim + filtration sentences "
        "(the lead-sulfate source-note 'Wash filtrate' conflict with the "
        "pinned MS Q7a(iii) was re-authored BEFORE the gate and recorded "
        "as a finding for the corpus owner)."),
}

# Node notes (keyed by CODE). The one retained pass-2 CONFIRM_WITH_NOTE
# row carries the qualification; the misconception rows note the ruled-
# WITH linkage.
NODE_NOTES = {
    "4CH1-CON-NEUTRALISATION": (
        "Operator §6: CONFIRM_WITH_NOTE retained (recorded CONFIRM; the "
        "qualification carries here per the vocabulary rule). Pass-2: "
        "the H+/OH- mechanism + the not-all-acid-reactions scope limit "
        "are both carried; the node's mechanism sentence is also the "
        "remediation surface for MIS-ENDPOINT-PH-ABOVE-7 — the operator "
        "ruled the misconception WITH the concept row (B7-ID-05 "
        "KEEP_AS_IS, the mint ratified)."),
    "4CH1-MIS-ENDPOINT-PH-ABOVE-7": (
        "Operator §6: CONFIRM (B7-ID-05 KEEP_AS_IS) — the pinned "
        "Titrations MS Q2a(iv) Reject column is the narrow-but-exact "
        "documentation (the MIS-CUO-COLOUR/B6-ID-06 precedent)."),
    "4CH1-MIS-PRECIPITATE-IN-FILTRATE": (
        "Operator §6: CONFIRM (B7-ID-06 KEEP_AS_IS) — the pinned "
        "Salt-Prep MS Q2a(iii) class is the strongest documented pattern "
        "of the batch."),
}

ID_NOTES = {
    "B7-ID-01": (
        "Operator §6: KEEP_AS_IS — keep 2.35/2.36 as one proton-transfer "
        "concept, matching the sheet's single-family treatment."),
    "B7-ID-02": (
        "Operator §6: KEEP_AS_IS — keep the qualitative solubility-rule "
        "concept separate from quantitative/S3 calculation surfaces."),
    "B7-ID-03": (
        "Operator §6: KEEP_AS_IS — keep the 2.31 aqueous acid/alkali ion "
        "concept self-contained without absorbing broader ion-rule "
        "ownership."),
    "B7-ID-04": (
        "Operator §6: KEEP_AS_IS — keep the three salt-preparation "
        "routes separate: insoluble reactant, titration, and "
        "precipitation."),
    "B7-ID-05": (
        "Operator §6: KEEP_AS_IS — keep the endpoint/pH misconception as "
        "one assessment-documented misconception surface."),
    "B7-ID-06": (
        "Operator §6: KEEP_AS_IS — keep the precipitate/filtrate "
        "misconception as one assessment-documented misconception "
        "surface."),
}

HELD_NOTE = (
    "Operator §6: all 9 held candidates (B7-H-01..09) are ACKNOWLEDGED / "
    "KEEP QUARANTINED — no held candidate is reopened, promoted, or "
    "converted into a new authored edge/node; the abstention record is "
    "preserved. The operator explicitly upholds: B7-H-01 (the proposed "
    "dependency is not load-bearing); B7-H-02 (the pH-scale relation is "
    "incidental to the stated base/alkali demand); B7-H-03 (the "
    "practical uses the water/crystal context as given rather than "
    "establishing a governed prerequisite); B7-H-04 (the "
    "reagent-selection wrong-answer surface is insufficiently "
    "characterized under the established Step-3 rule); B7-H-05 "
    "(concentration/calculation is an S3-owner surface); B7-H-06 (the "
    "universal-indicator-for-titration misconception is note-anchored "
    "rather than mark-scheme documented); B7-H-07 (adjacency does not "
    "establish a prerequisite relation); B7-H-08 (the omitted-excess-base "
    "error is note-anchored and risks owner duplication); B7-H-09 "
    "(concentration is context framing rather than demonstrated "
    "load-bearing prerequisite evidence).")

META_FILE = (
    "OPERATOR-OWNED verdict record for C11_BATCH7_REVIEW_SHEET (session-59 "
    "package) — verdicts recorded by operator decision, session 60 "
    "(2026-09-23), from the operator verdict addendum §6/§7 "
    "(C11_BATCH7_REVIEW_SHEET_COMPLETED intake).")

META_RULING = {
    "statement": OPERATOR_STATEMENT,
    "session": SESSION,
    "decided_by": "operator",
    "decided_date": TODAY,
    "completed_sheet": (
        "Operator verdict addendum §6 ('Completed operator verdict') + §7 "
        "('Final operator gate'), delivered in-chat 2026-09-23 and "
        "materialized by the verdict session as "
        "C11_BATCH7_REVIEW_SHEET_COMPLETED.md. Delivery record: the "
        "web-lane upload of that filename did not reach the verdict "
        "workspace (upload/ held only the batch-5/6 completed sheets); "
        "the FileUpload-lane advance 8b03d1c (2026-09-23 00:36 +0600) "
        "carried the BLANK gate sheet C11_BATCH7_REVIEW_SHEET.md, "
        "byte-identical to the in-repo gate sheet (diff -q clean — the "
        "batch-6 gate-sheet-upload precedent). The operator therefore "
        "delivered the §6/§7 verdict content directly; the addendum is "
        "an ADDENDUM (no §1-5), so the batch-5/6 §1-5 byte-drift check "
        "does not apply — the verdict content is reconciled 1:1 against "
        "the in-repo gate sheet §2/§3 surfaces and the batch-7 decision "
        "record instead (machine-checked)."),
    "reported_state_caveat": (
        "Recorded verbatim from the operator's §6 assessment: 'The "
        "reported 157-node / 367-edge store and 95/0/0 gate battery are "
        "treated here as REPORTED by the submitted artifact; the "
        "underlying Batch 7 decision/pass-2/boundary YAMLs were not "
        "independently accessible through the GitHub connector. This "
        "does not change the operator verdict, but it limits independent "
        "verification of the machine-state claims.' The verdict session "
        "closed that gap on the operator's behalf: the machine state was "
        "verified directly at d6eba2d (the authoring head, local == "
        "origin/main, tree clean) before encoding — 157 nodes / 367 "
        "edges / 156 PART_OF / 187 semantic HV / S4 pins; the decision, "
        "pass-2 and boundary YAMLs reconciled 1:1."),
    "mapping": (
        "The operator reviewed the session-59 gate package and returned "
        "the verdict addendum §6/§7: all 15 node verdicts accepted (13 "
        "CONCEPT + 2 MISCONCEPTION; CON-NEUTRALISATION as the retained "
        "pass-2 CONFIRM_WITH_NOTE; 'Node authority remains SUGGESTED. No "
        "node is promoted by this review.'); all 19 authored edges "
        "CONFIRM with TWO semantic guardrails — B7-E-02 (ACID-REACTIONS "
        "REQUIRES_PREREQUISITE REACT-ORDER) CONFIRM_WITH_NOTE: 'Treat "
        "this as the acid+metal route dependency evidenced by the sheet. "
        "Do not generalize it into a universal prerequisite for every "
        "acid reaction represented by 4CH1-CON-ACID-REACTIONS.'; B7-E-10 "
        "(SOLUBILITY-RULES REQUIRES_PREREQUISITE ION-CHARGE-RULES) "
        "CONFIRM_WITH_NOTE: 'Preserve the sanctioned boundary ownership "
        "and do not mint a duplicate CON-ION-CHARGE-RULES concept inside "
        "Batch 7.'; the two practical edges confirmed by triple "
        "(PR-07 -> CON-SALT-INSOLUBLE-REACTANT; PR-08 -> "
        "CON-SALT-PRECIPITATION); the two sanctioned boundary edges "
        "'remain owned as stated in the review sheet' (acid-metal "
        "placement -> batch-6 CON-REACT-ORDER; solubility -> batch-3 "
        "CON-ION-CHARGE-RULES; 'No duplicate concept is to be minted'); "
        "the six identity decisions resolved KEEP_AS_IS each with a "
        "recorded rationale; the 9 held candidates 'ACKNOWLEDGED / KEEP "
        "QUARANTINED' with per-candidate reasons — none reopened, "
        "promoted, or converted; zero RR rows; zero REJECTED authored "
        "edges; final directive: 'Operator verdict: PASS WITH NOTES — "
        "proceed through the normal C11 pathway ... encode/reconcile -> "
        "c11_promote.py -> regenerate -> rerun the complete gate suite.' "
        "The operator verdict file itself is the authorization (the "
        "session-54/56/58 precedent). ENCODING RULES: the verdict-record "
        "vocabulary (CONFIRM|REJECT|HOLD|MERGE|SPLIT) has no WITH_NOTE "
        "value, so the operator's three CONFIRM_WITH_NOTE statuses (node "
        "CON-NEUTRALISATION + edges B7-E-02/B7-E-10) are recorded as "
        "CONFIRM with the qualification carried verbatim in the row's "
        "notes (the batch-1..6 precedent that qualifications ride in "
        "notes); node verdicts are keyed by CODE and edge verdicts by "
        "TRIPLE — never by row id — because the sheet's §2 node "
        "numbering (table order = decision-record order: sheet B7-N-01 = "
        "CON-INDICATORS) differs from the template's "
        "alphabetical-by-code numbering (template B7-N-01 = "
        "CON-ACID-ALKALI-IONS), while the edge ids coincide between the "
        "sheet §3 rows and the template (both orders agree row-for-row) "
        "and the explicitly named B7-E-02/B7-E-10/PR-07/PR-08 triples "
        "are identical in both; each correspondence was asserted against "
        "the gate sheet and the decision record before encoding; node "
        "authority is NOT changed by these confirmations (nodes have no "
        "§18 pathway — node promotion remains a separate identity "
        "decision, deferred); PART_OF is derived and outside §18; the "
        "application state lives in scripts/c11_promotions.yaml (the "
        "§18 pathway is the only HUMAN_VALIDATED source) — this file "
        "never carries promotion payload or promoted status. Changing a "
        "recorded verdict requires an explicit operator decision."),
}


def die(msg: str):
    print(f"FAIL-CLOSED: {msg}")
    sys.exit(1)


def _require(cond: bool, msg: str) -> None:
    """Fail-closed gate that survives `python -O` (assert is stripped
    under -O, which would turn this gate fail-open — MD-33)."""
    if not cond:
        raise RuntimeError(msg)


# ---------------------------------------------------------------------------
# Addendum parsing (fail-closed; keyed by CODE/TRIPLE, never by row id)
# ---------------------------------------------------------------------------

def parse_addendum(text: str):
    """Extract the verdict surface from the operator addendum.
    Returns (node_pairs, guardrail_triples, practical_triples,
    identity_ids, held_ids)."""
    node_pairs = []       # (B7-N-xx, CODE, VERDICT)
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("| B7-N-") or s.startswith("| B7-M-"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) >= 3 and cells[0].startswith("B7-"):
                nid, code, verdict = cells[0], cells[1], cells[2]
                code = code.strip("`*").strip()
                verdict = verdict.strip("*").strip()
                node_pairs.append((nid, code, verdict))
    guardrails, practicals = {}, []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("- **B7-E-") and "`" in s \
                and " REQUIRES_PREREQUISITE " in s:
            # addendum guardrail shape: - **B7-E-xx** `SRC REL TGT` — ...
            parts = s.split("**")
            nid = parts[1]
            rest = parts[2]
            t = rest[rest.index("`") + 1: rest.index("`", rest.index("`") + 1)]
            if nid in ("B7-E-02", "B7-E-10"):
                guardrails[nid] = t
        elif s.startswith("- `4CH1-PR-") and " REQUIRES_PREREQUISITE " in s:
            t = s[s.index("`") + 1: s.index("`", s.index("`") + 1)]
            practicals.append(t)
    identity_ids = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("| B7-ID-") and "KEEP_AS_IS" in s:
            identity_ids.append(s.strip("|").split("|")[0].strip())
    held_ids = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("- B7-H-") and "remains quarantined" in s:
            held_ids.append(s.split()[1].rstrip(":"))
    return node_pairs, guardrails, practicals, identity_ids, held_ids


# ---------------------------------------------------------------------------
# Load + pre-state assertions
# ---------------------------------------------------------------------------
if len(sys.argv) != 2:
    die("usage: c11_verdict_encode_batch7.py COMPLETED_ADDENDUM.md "
        "(the operator's verdict addendum, e.g. "
        "C11_BATCH7_REVIEW_SHEET_COMPLETED.md)")
COMPLETED = Path(sys.argv[1]).resolve()
if not COMPLETED.exists():
    die(f"completed addendum not found: {COMPLETED}")
if VERDICTS.exists():
    die("scripts/c11_batch7_verdicts.yaml already exists — refusing to "
        "double-apply (the verdict round is recorded)")
if not TEMPLATE.exists():
    die("scripts/c11_batch7_verdicts_template.yaml missing — the "
        "session-59 package must be intact")
if not GATE_SHEET.exists():
    die("gate sheet missing from graph/reports/ — the session-59 "
        "package must be intact")
comp_text = COMPLETED.read_text(encoding="utf-8")
doc = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
if doc is None:
    die("verdict template empty")

# 0. the addendum must carry the §6/§7 verdict surface with the expected
#    markers (addendum-form intake — see the module docstring).
_require("## 6. Completed operator verdict" in comp_text,
         "§6 header missing from the addendum")
_require("## 7. Final operator gate" in comp_text,
         "§7 header missing from the addendum")
for marker in ("PASS WITH NOTES", "15/15 confirmed", "19/19 confirmed",
               "6/6 KEEP_AS_IS", "9/9 acknowledged and quarantined",
               "REVIEW_REQUIRED edges: **0**",
               "Rejected authored edges: **0**",
               "Authority status: **SUGGESTED**",
               "does not itself constitute",
               "No duplicate concept is to be minted"):
    _require(marker in comp_text,
             f"addendum missing an expected verdict marker: {marker}")

node_pairs, guardrails, practicals, identity_ids, held_ids = \
    parse_addendum(comp_text)
_require(len(node_pairs) == 15,
         f"addendum node table parsed {len(node_pairs)} rows, expected 15")
_require(all(v in ("CONFIRM", "CONFIRM_WITH_NOTE")
             for _, _, v in node_pairs),
         "addendum node verdicts outside the CONFIRM vocabulary")
_wn = [(nid, code) for nid, code, v in node_pairs
       if v == "CONFIRM_WITH_NOTE"]
_require(len(_wn) == 1 and _wn[0][1] == "4CH1-CON-NEUTRALISATION",
         f"addendum WITH_NOTE node surface drifted: {_wn}")

# the addendum's (id, code) pairs must match the GATE SHEET §2 table order
# exactly (the sheet-order identity — the addendum was ruled against the
# session-59 package).
gate_text = GATE_SHEET.read_text(encoding="utf-8")
sheet_pairs = []
in_s2 = False
for line in gate_text.splitlines():
    if line.startswith("## 2. Concept & misconception nodes"):
        in_s2 = True
        continue
    if in_s2 and line.startswith("## 3."):
        break
    if in_s2:
        s = line.strip()
        if "`4CH1-" in s and "| " in s:
            cells = [c.strip() for c in s.strip("|").split("|")]
            # sheet §2 row shape: | <row#> | `CODE` | family | ... — the
            # sheet's §1 assigns ids positionally over these rows:
            # rows 1-13 = B7-N-01..13, rows 14-15 = B7-M-01..02.
            if len(cells) >= 2 and cells[0].isdigit() \
                    and cells[1].startswith("`4CH1-"):
                k = int(cells[0])
                nid = (f"B7-N-{k:02d}" if k <= 13
                       else f"B7-M-{k - 13:02d}")
                sheet_pairs.append((nid, cells[1].strip("`*").strip()))
_require(len(sheet_pairs) == 15,
         f"gate sheet §2 parsed {len(sheet_pairs)} node rows, expected 15")
_require([(n, c) for n, c, _ in node_pairs] == sheet_pairs,
         "addendum node (id, code) pairs do not match the gate sheet §2 "
         "table order — re-characterize before encoding")

# 1. the template must be untouched (no verdict filled anywhere)
for section in ("edge_verdicts", "node_verdicts", "identity_decisions"):
    for row in doc[section]:
        if row.get("verdict"):
            die(f"{section} {row['id']} already has a verdict — refusing")
if doc.get("rr_settlement"):
    die("unexpected rr_settlement section — the batch-7 template must "
        "carry none (zero RR edges authored)")
if doc["held_appendix_acknowledgment"].get("acknowledged"):
    die("held_appendix_acknowledgment already acknowledged — refusing")

# 2. row-shape assertions (exact session-59 surface)
_require([r["id"] for r in doc["edge_verdicts"]] ==
         [f"B7-E-{i:02d}" for i in range(1, 20)],
         "edge ids drifted from B7-E-01..19")
_require([r["id"] for r in doc["node_verdicts"]] ==
         [f"B7-N-{i:02d}" for i in range(1, 14)] + ["B7-M-01", "B7-M-02"],
         "node ids drifted from B7-N-01..13 + B7-M-01..02")
_require([r["id"] for r in doc["identity_decisions"]] ==
         [f"B7-ID-{i:02d}" for i in range(1, 7)],
         "identity ids drifted from B7-ID-01..06")

# 3. reconcile against the batch-7 decision record + the gate sheet + the
#    addendum's named rows
dec = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
edges_doc = yaml.safe_load((GRAPH / "concept_edges.yaml")
                           .read_text(encoding="utf-8"))
nodes_doc = yaml.safe_load((GRAPH / "concepts.yaml")
                           .read_text(encoding="utf-8"))
promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
auth = yaml.safe_load(S16_AUTH.read_text(encoding="utf-8"))


def triple(e):
    return f"{e['source']} {e['relation']} {e['target']}"


b_edges = dec["edges"]
b_suggested = [triple(e) for e in b_edges
               if e["validation_status"] == "SUGGESTED"]
b_rr = [triple(e) for e in b_edges
        if e["validation_status"] == "REVIEW_REQUIRED"]
tmpl_triples = [r["triple"] for r in doc["edge_verdicts"]]
_require(len(b_edges) == 19, f"batch-7 decision record carries "
         f"{len(b_edges)} edges, expected 19")
_require(len(b_suggested) == 19 and len(b_rr) == 0,
         "batch-7 edges must be 19 SUGGESTED / 0 RR at the pre-verdict "
         "state")
_require(sorted(tmpl_triples) == sorted(b_suggested)
         and len(set(tmpl_triples)) == 19,
         "edge triple mismatch between verdict template and the batch-7 "
         "decision record")
b_codes = [n["code"] for n in dec["nodes"]]
tmpl_codes = [r["code"] for r in doc["node_verdicts"]]
_require(sorted(tmpl_codes) == sorted(b_codes) and len(set(tmpl_codes)) == 15,
         "node code mismatch between verdict template and the batch-7 "
         "decision record")
_require(len(dec["held"]) == 9, f"batch-7 held count "
         f"{len(dec['held'])}, expected 9")
_require([h["id"] for h in dec["held"]]
         == [f"B7-H-{i:02d}" for i in range(1, 10)],
         "batch-7 held ids drifted from B7-H-01..09")
# the addendum's named rows must hit real template rows (no stale ids)
tmpl_by_id = {r["id"]: r for r in doc["edge_verdicts"]}
for gid in ("B7-E-02", "B7-E-10"):
    _require(gid in guardrails, f"addendum missing the {gid} guardrail")
    _require(guardrails[gid] == tmpl_by_id[gid]["triple"],
             f"addendum {gid} triple does not match the template row")
_require(sorted(practicals) == sorted(
    t for t in tmpl_triples if t.startswith("4CH1-PR-")),
    "addendum practical triples do not match the template's PR rows")
_require(identity_ids == [f"B7-ID-{i:02d}" for i in range(1, 7)],
         "addendum identity ids drifted from B7-ID-01..06 KEEP_AS_IS")
_require(held_ids == [f"B7-H-{i:02d}" for i in range(1, 10)],
         "addendum held ids drifted from B7-H-01..09")
# every note key must hit a real row (no stale keys)
for k in list(GUARDRAIL_NOTES) + list(EDGE_NOTES):
    _require(k in set(tmpl_triples), f"EDGE_NOTES key not in template: {k}")
for k in NODE_NOTES:
    _require(k in set(tmpl_codes), f"NODE_NOTES key not in template: {k}")

# 4. the live store must be the sanctioned pre-verdict state
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
partof = [e for e in edges_doc["edges"] if e["relation"] == "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
store = {(p["edge"]["source"], p["edge"]["relation"], p["edge"]["target"])
         for p in promo["promotions"]}
store_triples = {" ".join(t) for t in store}
_require(len(hv) == 187 and hv == store_triples,
         "live HUMAN_VALIDATED set != the 187 pilot+batch-1+batch-2"
         "+batch-3+batch-4+batch-5+batch-6 §18 promotions (the "
         "pre-verdict state must be frozen before recording batch-7 "
         "verdicts)")
_require(not (hv & set(b_suggested)),
         "a batch-7 edge is already HUMAN_VALIDATED — pre-verdict state "
         "violated")
_require(auth.get("authorization", {}).get("decision") == "AUTHORIZED",
         "§16 is not AUTHORIZED (scripts/c11_s16_authorization.yaml)")
_require(all(p.get("validated_by") == "operator"
             for p in promo["promotions"]),
         "existing promotions carry non-operator attribution (anti-forgery)")
_require(len(nodes_doc["nodes"]) == 157, f"store nodes "
         f"{len(nodes_doc['nodes'])}, expected 157")
_require(len(edges_doc["edges"]) == 367, f"store edges "
         f"{len(edges_doc['edges'])}, expected 367")
_require(len(partof) == 156
         and sum(1 for e in partof
                 if e["validation_status"] == "HUMAN_VALIDATED") == 117,
         "PART_OF layer drifted (expected 156 rows, 117 HUMAN_VALIDATED — "
         "the T-C19 G19 record; batch-7 PART_OF rows stay SUGGESTED)")
# the SUGGESTED surface must be exactly the 19 batch-7 rows + the 3
# frozen pilot HOLDs; the 2 frozen RR settlements untouched
sugg = {triple(e) for e in sem if e["validation_status"] == "SUGGESTED"}
pilot_holds = {
    "4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-EQ-SYMBOL",
    "4CH1-CON-MOLAR-GAS-VOL EXPLAINED_BY 4CH1-CON-AVOGADRO-LAW",
    "4CH1-MIS-EQ-SUBSCRIPT REMEDIATED_BY 4CH1-CON-CONSERVATION-MASS",
}
_require(sugg == set(b_suggested) | pilot_holds,
         "SUGGESTED surface drifted (expected exactly the 19 batch-7 "
         "edges + the 3 frozen pilot HOLDs)")
rr_live = {triple(e) for e in sem
           if e["validation_status"] == "REVIEW_REQUIRED"}
_require(len(rr_live) == 2,
         "the 2 frozen pilot REVIEW_REQUIRED settlements must be "
         "untouched at the pre-verdict state")

# ---------------------------------------------------------------------------
# Encode (in-place; key order preserved)
# ---------------------------------------------------------------------------
doc["meta"]["session"] = SESSION
doc["meta"]["file"] = META_FILE
doc["meta"]["operator_ruling"] = META_RULING

for row in doc["edge_verdicts"]:
    row["verdict"] = "CONFIRM"
    row["notes"] = GUARDRAIL_NOTES.get(row["triple"],
                                       EDGE_NOTES.get(row["triple"], ""))
for row in doc["node_verdicts"]:
    row["verdict"] = "CONFIRM"
    row["notes"] = NODE_NOTES.get(row["code"], "")
for row in doc["identity_decisions"]:
    row["verdict"] = "KEEP_AS_IS"
    row["notes"] = ID_NOTES[row["id"]]
doc["held_appendix_acknowledgment"]["acknowledged"] = True
doc["held_appendix_acknowledgment"]["notes"] = HELD_NOTE

header = (
    "# T-C11 §16 batch 7 — OPERATOR verdict record (session-59 package), "
    "FILLED by operator decision session 60 (2026-09-23). OPERATOR-OWNED.\n"
    "# Operator verdict (addendum §6/§7, C11_BATCH7_REVIEW_SHEET_COMPLETED "
    "intake): all 15 node verdicts and all 19\n# edge verdicts accepted "
    "(the three CONFIRM_WITH_NOTE qualifications — node CON-NEUTRALISATION "
    "+ edges B7-E-02/B7-E-10 —\n# recorded in notes per the vocabulary "
    "rule); the six identity decisions KEEP_AS_IS; the 9 held candidates "
    "acknowledged and\n# quarantined; zero RR; zero REJECT. Intake form: "
    "ADDENDUM (no §1-5) — verdict content reconciled 1:1 against the\n"
    "# gate sheet §2/§3 surfaces and the decision record (machine-checked; "
    "see meta.operator_ruling.delivery).\n"
    "# Vocabulary and pathway: see the meta.operator_ruling.mapping block. "
    "Verdicts are RECORDED; the application state lives in\n"
    "# scripts/c11_promotions.yaml (§18) — never here.\n"
)
VERDICTS.write_text(
    header + yaml.safe_dump(doc, sort_keys=False, allow_unicode=True,
                            width=100),
    encoding="utf-8")
TEMPLATE.unlink()  # the sheet's gate pathway: fill + RENAME

# ---------------------------------------------------------------------------
# Post-write verification (re-parse + counts)
# ---------------------------------------------------------------------------
chk = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
ec = {}
for r in chk["edge_verdicts"]:
    ec[r["verdict"]] = ec.get(r["verdict"], 0) + 1
nc = {}
for r in chk["node_verdicts"]:
    nc[r["verdict"]] = nc.get(r["verdict"], 0) + 1

_require(ec == {"CONFIRM": 19},
         f"post-write: edge verdict counts drifted: {ec}")
_require(nc == {"CONFIRM": 15},
         f"post-write: node verdict counts drifted: {nc}")
_require([r["verdict"] for r in chk["identity_decisions"]]
         == ["KEEP_AS_IS"] * 6,
         "post-write: identity decisions drifted")
_require("rr_settlement" not in chk,
         "post-write: unexpected rr_settlement present")
_require(chk["held_appendix_acknowledgment"]["acknowledged"] is True,
         "post-write: held appendix acknowledgment missing")
_require(chk["meta"]["operator_ruling"]["statement"] == OPERATOR_STATEMENT,
         "post-write: operator ruling text drifted")
for gid, t in (("B7-E-02",
                "4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE "
                "4CH1-CON-REACT-ORDER"),
               ("B7-E-10",
                "4CH1-CON-SOLUBILITY-RULES REQUIRES_PREREQUISITE "
                "4CH1-CON-ION-CHARGE-RULES")):
    r = next(x for x in chk["edge_verdicts"] if x["triple"] == t)
    _require(r["id"] == gid and r["notes"].startswith(
                 "Operator §6 (session 60): CONFIRM_WITH_NOTE retained"),
             f"post-write: the {gid} qualification note drifted")
_n05 = next(r for r in chk["node_verdicts"]
            if r["code"] == "4CH1-CON-NEUTRALISATION")
_require(_n05["notes"].startswith(
             "Operator §6: CONFIRM_WITH_NOTE retained"),
         "post-write: the CON-NEUTRALISATION qualification note drifted")
_require(not TEMPLATE.exists(),
         "post-write: verdict template was not consumed")

print("wrote", VERDICTS)
print("operator verdict recorded verbatim from the addendum §6/§7 "
      f"(decided_by operator, {TODAY})")
print("intake form: ADDENDUM — reconciled 1:1 against the gate sheet "
      "§2/§3 + decision record (machine-checked)")
print(f"edge verdicts: {ec}")
print(f"node verdicts: {nc}")
print("identity decisions: 6 x KEEP_AS_IS")
print("RR settlement: none recorded (zero RR edges authored in batch 7)")
print("held_appendix: acknowledged (9 preserved, quarantined)")
print("template removed (fill + rename per the gate pathway)")
print("ENCODE COMPLETE — verdict layer established; nothing applied.")
