#!/usr/bin/env python3
"""T-C11 session 58 — encode the OPERATOR VERDICT SET for §16 batch 6 into
the operator-owned verdict record scripts/c11_batch6_verdicts.yaml.

The operator ruled on the batch-6 gate (review sheet
graph/reports/C11_BATCH6_REVIEW_SHEET.md, session-57 package) with the
completed review sheet section 6 ("Completed operator verdict", delivered
to the verdict session as C11_BATCH6_REVIEW_SHEET_COMPLETED.md, 2026-09-22):
all 13 node verdicts accepted with the pass-2 statuses retained (10 CONFIRM
+ 3 CONFIRM_WITH_NOTE), all 16 edge verdicts CONFIRM with exactly one
explicit qualification (B6-E-09 CONFIRM_WITH_NOTE — the route-specific
oxygen-percentage guardrail), the six identity decisions KEEP_AS_IS each
with a recorded rationale, the 9 held candidates acknowledged/quarantined,
zero RR, and the final directive "Operator verdict: PASS WITH NOTE —
proceed to verdict encoding/reconciliation and the separately governed §18
promotion step." This script encodes the per-row decisions from that
completed sheet — no verdict invented, no evidence reinterpreted, no ID
guessed. Fail-closed:

  * refuses if the filled verdict record already exists (no double-apply);
  * refuses if any verdict field in the template is already filled;
  * refuses if the completed sheet's §1-5 drift against the in-repo gate
    sheet exceeds the FOUR characterized typographic lines (session-58
    drift record — machine-checked below, exact strings only);
  * refuses if the template rows do not reconcile 1:1 against the batch-6
    decision record (16 SUGGESTED edge triples / ZERO RR triples / 13 node
    codes [12 CONCEPT + 1 MISCONCEPTION] / 9 held candidates);
  * refuses if the live store is not in the sanctioned pre-verdict state
    (171 semantic HUMAN_VALIDATED = 28 pilot + 28 batch-1 + 23 batch-2 +
    39 batch-3 + 35 batch-4 + 18 batch-5 §18 promotions; 0 batch-6
    promotions; §16 authorization AUTHORIZED; pilot HOLDs + both RR
    settlements frozen; 142 nodes / 334 edges).

Encoding rules (recorded verbatim in the file's operator_ruling.mapping):
  * every edge row          -> CONFIRM  (B6-E-09 carries the operator's
    CONFIRM_WITH_NOTE qualification in notes — the verdict-record
    vocabulary CONFIRM|REJECT|HOLD|MERGE|SPLIT has no WITH_NOTE value, the
    batch-1..5 precedent is that qualifications ride in notes)
  * every node row          -> CONFIRM  (the three pass-2 CONFIRM_WITH_NOTE
    rows — CON-OX-RED-AGENTS, CON-EXTRACTION-EVALUATION,
    MIS-ION-OXIDE-REASONING — carry the retained pass-2 qualification in
    notes)
  * every identity decision -> KEEP_AS_IS (the operator's §6 rationale
    table, verbatim)
  * RR settlement           -> NONE RECORDED: this batch authored no
    REVIEW_REQUIRED edge, so no settlement row exists in the template
  * held appendix           -> acknowledged (9 preserved, quarantined)

IDENTITY-SAFETY NOTE (the sheet-vs-template numbering hazard): the review
sheet's section-2/6 rows number nodes in table order (sheet B6-N-01 =
CON-REACT-ARRANGE) while the template numbers them alphabetically by code
(template B6-N-01 = CON-ALLOY-HARDNESS). Verdicts and notes here are
therefore keyed by TRIPLE (edges) and CODE (nodes), never by row id, and
each template row's id<->code/triple correspondence is asserted against the
decision record before anything is written. The sheet's §6 pairs every
node id with its code explicitly, so the three WITH_NOTE rows are
unambiguous by CODE: the sheet's B6-N-06/B6-N-09 (table order) are
CON-OX-RED-AGENTS / CON-EXTRACTION-EVALUATION; the sheet's B6-N-01..12
edge numbering coincides with the template for edges (both orders agree),
and the explicitly named B6-E-09 triple is identical in both.

COMPLETED-SHEET DRIFT RECORD (session 58): the completed copy's §1-5 is
NOT byte-identical to the in-repo gate sheet — exactly FOUR lines differ,
all typographic/wording-level with zero verdict-relevant semantic change,
each machine-checked below against its exact expected string pair:
  1. line 12  — the §1 totals table separator is 4-column in the gate
     sheet under a 5-column header; the completed copy normalizes it to
     5 columns (a markdown table-shape repair; same data);
  2. line 61  — "no duplicate mint" (gate) vs "no duplicate concept"
     (completed) — one-word wording; the completed sheet's own §6 text
     says "No duplicate concept is to be minted", so the completed copy is
     internally consistent and the ruling is identical either way;
  3. line 69  — the gate sheet truncates mid-word ("conventio |"); the
     completed copy completes it ("convention) |") (a truncation repair;
     same data);
  4. line 87  — the gate sheet's pathway line names the tooling chain;
     the completed copy states the generic §18 wording (the batch-5 sheet
     form). The instruction is identical, and the completed sheet's §6
     final line names the full mechanical chain itself.
Anything beyond these four lines fails the encode.

This script WRITES ONLY scripts/c11_batch6_verdicts.yaml (and removes the
now-renamed template, per the sheet's gate pathway). It promotes nothing
and re-authors no decision record; application (§18 promotion) is the
separate sanctioned step in this same session per the operator's §6
directive ("proceed to verdict encoding/reconciliation and the separately
governed §18 promotion step") — the completed sheet's final line names the
chain: encode/reconcile -> c11_promote.py -> regenerate -> rerun the
complete gate suite.

Usage:
  python3 scripts/c11_verdict_encode_batch6.py COMPLETED_SHEET.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry (post-C28 layout)

GRAPH = GP.qual_dir()          # the qual's ratified store dir
TEMPLATE = HERE / "c11_batch6_verdicts_template.yaml"
VERDICTS = HERE / "c11_batch6_verdicts.yaml"
DECISIONS = HERE / "c11_batch6_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"
S16_AUTH = HERE / "c11_s16_authorization.yaml"
GATE_SHEET = GP.reports_dir() / "C11_BATCH6_REVIEW_SHEET.md"

SESSION = 58
TODAY = "2026-09-22"
# Verbatim operative text from the operator's completed review sheet §6
# ("Final operator gate" + "Operator verdict", C11_BATCH6_REVIEW_SHEET_
# COMPLETED.md, 2026-09-22).
OPERATOR_STATEMENT = (
    "Final operator gate: Nodes 13/13 confirmed; Authored edges 16/16 "
    "confirmed; Edge qualification: 1 CONFIRM_WITH_NOTE; Identity "
    "decisions 6/6 KEEP_AS_IS; Held candidates 9/9 acknowledged and "
    "quarantined; REVIEW_REQUIRED edges 0; Rejected authored edges 0; "
    "Batch-6 promotions 0; Authority status SUGGESTED until the governed "
    "promotion pathway is executed. Operator verdict: PASS WITH NOTE — "
    "proceed to verdict encoding/reconciliation and the separately "
    "governed §18 promotion step. The note on B6-E-09 is a semantic "
    "guardrail, not a rejection. It prevents the graph from turning a "
    "route-specific experimental dependency into a universal prerequisite. "
    "This verdict does not itself perform promotion. The next mechanical "
    "step remains: c11_batch6_verdicts_template.yaml -> "
    "c11_batch6_verdicts.yaml -> encode/reconcile -> c11_promote.py -> "
    "regenerate -> rerun the complete gate suite.")

# ---------------------------------------------------------------------------
# The FOUR characterized completed-sheet drift lines (session-58 record;
# exact string pairs, machine-checked — anything else fails the encode).
# (1-indexed line number, gate-sheet form, completed-sheet form)
# ---------------------------------------------------------------------------
DRIFT_EXPECTED = [
    (12,
     "|---|---|---|---|",
     "|---|---|---|---|---|"),
    (61,
     "Four edges are CROSS-SECTION boundary edges into the ruled targets "
     "(sanctioned per the session-57 cross-slice ruling — no duplicate "
     "mint): the 2.23C electrolysis row and the 2.25C properties row "
     "(batch-3 owners), and the TWO deferral closures the batch-5 ruling "
     "explicitly deferred to this batch (the 2.12 carbonate-decomposition "
     "row into CON-REACT-ORDER and the 2.10 iron-route row into "
     "CON-RUSTING — closing its future_boundary_notes and held B5-H-10).",
     "Four edges are CROSS-SECTION boundary edges into the ruled targets "
     "(sanctioned per the session-57 cross-slice ruling — no duplicate "
     "concept): the 2.23C electrolysis row and the 2.25C properties row "
     "(batch-3 owners), and the TWO deferral closures the batch-5 ruling "
     "explicitly deferred to this batch (the 2.12 carbonate-decomposition "
     "row into CON-REACT-ORDER and the 2.10 iron-route row into "
     "CON-RUSTING — closing its future_boundary_notes and held B5-H-10)."),
    (69,
     "| B6-H-03 | MISCONCEPTION \"naming the acid or water as the factor "
     "that changes the metal-acid vigour\" (the REACTIVITY_MS Q1ai IGNORE "
     "class) | INSUFFICIENT CHARACTERIZATION (the B5-H-04/B5-H-05 "
     "conventio |",
     "| B6-H-03 | MISCONCEPTION \"naming the acid or water as the factor "
     "that changes the metal-acid vigour\" (the REACTIVITY_MS Q1ai IGNORE "
     "class) | INSUFFICIENT CHARACTERIZATION (the B5-H-04/B5-H-05 "
     "convention) |"),
    (87,
     "Pathway: fill `scripts/c11_batch6_verdicts_template.yaml` → rename "
     "to `c11_batch6_verdicts.yaml` → a later session encodes + applies "
     "via `c11_verdict_encode_batch6`-style reconciliation + "
     "`c11_promote.py` (§18) + the gated generator re-run. NOTHING is "
     "promoted at this gate.",
     "Pathway: fill `scripts/c11_batch6_verdicts_template.yaml` → rename "
     "to `c11_batch6_verdicts.yaml` → a later session encodes + applies "
     "via §18. NOTHING is promoted at this gate."),
]

# ---------------------------------------------------------------------------
# Verdict notes (evidence-grounded context per row; verdicts all CONFIRM per
# the mapping above — the operator's §6 CONFIRM_WITH_NOTE qualifications ride
# in notes). Keyed by TRIPLE (edges) / CODE (nodes).
# ---------------------------------------------------------------------------
EDGE_NOTES = {
    # The one operator-qualified row (the sheet's §6 Edge verdicts section).
    "4CH1-CON-O2-PERCENT-DETERMINATION REQUIRES_PREREQUISITE 4CH1-CON-RUSTING": (
        "Operator §6 (session 58): CONFIRM_WITH_NOTE retained — this "
        "dependency is route-specific: the iron-based oxygen-percentage "
        "determination uses iron oxidation/rusting-related knowledge; the "
        "edge must not be interpreted as saying that every possible "
        "oxygen-percentage determination method universally requires the "
        "rusting concept. Pass-2: sanctioned boundary target — closes the "
        "batch-5 ruling's other future_boundary_note verbatim; the "
        "iron-wool route IS the rusting phenomenon applied."),
    # The three other sanctioned cross-section boundary edges (session-57
    # ruling; the operator's §6 four-edge list + no-duplicate directive).
    "4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS": (
        "Operator §6: CONFIRM — a sanctioned cross-section boundary edge "
        "(session-57 ruling; batch-3 owner CON-ELECTROLYSIS; the "
        "electrolysis route applies the cell framework as given, never "
        "re-defined); the operator's directive: the four sanctioned "
        "cross-section edges 'remain confirmed and must continue to "
        "reference their governed owners/mints. No duplicate concept is "
        "to be minted.'"),
    "4CH1-CON-METAL-USES REQUIRES_PREREQUISITE 4CH1-CON-METAL-PROPERTIES": (
        "Operator §6: CONFIRM — a sanctioned cross-section boundary edge "
        "(session-57 ruling; batch-3 owner CON-METAL-PROPERTIES; the "
        "spec's own 'in terms of their properties' demand with the "
        "property vocabulary applied as given); the boundary edges 'must "
        "continue to reference their governed owners/mints. No duplicate "
        "concept is to be minted.'"),
    "4CH1-CON-CO2-FROM-CARBONATES REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER": (
        "Operator §6: CONFIRM — a sanctioned cross-section boundary edge "
        "AND a deferral closure (closes the batch-5 ruling's "
        "future_boundary_note and held B5-H-10 verbatim: 'Carbonates of "
        "metals from the LOWER HALF of the reactivity series'); the "
        "target is the batch-6 mint CON-REACT-ORDER — 'No duplicate "
        "concept is to be minted.'"),
    # The definitional/containment core of the slice.
    "4CH1-CON-ALLOY-HARDNESS REQUIRES_PREREQUISITE 4CH1-CON-ALLOYS": (
        "Operator §6: CONFIRM as authored — definitional containment "
        "('Alloys are harder than pure metals because: Alloys contain "
        "atoms of DIFFERENT sizes'); the different-sized atoms are the "
        "alloy definition applied."),
    "4CH1-CON-REACT-ORDER REQUIRES_PREREQUISITE 4CH1-CON-REACT-ARRANGE": (
        "Operator §6: CONFIRM as authored — the order is the PRODUCT of "
        "the arrangement comparisons ('Based on these reactions a "
        "reactivity series of metals can be produced'); definitional "
        "containment, direction correct."),
    "4CH1-CON-METAL-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER": (
        "Operator §6: CONFIRM as authored — definitional containment ('The "
        "reactivity of metals decreases going down the reactivity series. "
        "This means that a more reactive metal will displace a less "
        "reactive metal'); the B6-H-06 reverse-direction hold quarantined "
        "by the operator (would double-count the arrangement demand)."),
    "4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-RUSTING": (
        "Operator §6: CONFIRM as authored — the barrier method is DEFINED "
        "over the 2.18 condition pair ('barriers that prevent the iron "
        "from coming into contact with water and oxygen'); the B6-ID-04 "
        "conditions-vs-prevention split is KEEP_AS_IS."),
    "4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER": (
        "Operator §6: CONFIRM as authored — 'Iron can be prevented from "
        "rusting using the reactivity series'; the sacrificial-metal "
        "selection operates on the taught order as given "
        "(used-without-reteaching)."),
    "4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-OX-RED-AGENTS": (
        "Operator §6: CONFIRM as authored — the sacrificial MECHANISM is "
        "stated via oxidation ('will oxidise and therefore corrode "
        "first'; 'is oxidised more easily'); explains why sacrifice "
        "protects."),
    "4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER": (
        "Operator §6: CONFIRM as authored — the spec's own 2.23C demand "
        "verbatim ('The position of the metal on the reactivity series "
        "determines the method of extraction') plus the note's thesis "
        "line; the strongest in-batch dependency, direction correct."),
    "4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-OX-RED-AGENTS": (
        "Operator §6: CONFIRM as authored — the carbon-reduction route "
        "applies reduction as given ('heating with carbon which reduces "
        "them'; 'Carbon monoxide reduces the iron(III) oxide')."),
    "4CH1-CON-EXTRACTION-EVALUATION REQUIRES_PREREQUISITE 4CH1-CON-EXTRACTION-METHOD": (
        "Operator §6: CONFIRM as authored — the evaluation operates ON "
        "the method-position framework ('Make sure you can explain why "
        "aluminium is extracted by electrolysis while iron is extract…'); "
        "the B6-ID-02 method-vs-evaluation split is KEEP_AS_IS."),
    # The misconception pair (the one clean Reject-column pattern).
    "4CH1-MIS-ION-OXIDE-REASONING WRONG_ANSWER_PATTERN 4CH1-CON-METAL-DISPLACEMENT": (
        "Operator §6: CONFIRM as authored — the REACTIVITY_MS Q2a Reject "
        "column ('Reject references to ions and oxides') documents the "
        "wrong-answer class against the reactivity-comparison expected "
        "answer; the WAP target is the concept whose wrong explanations "
        "the MS caps."),
    "4CH1-MIS-ION-OXIDE-REASONING REMEDIATED_BY 4CH1-CON-METAL-DISPLACEMENT": (
        "Operator §6: CONFIRM as authored — remediation target = WAP "
        "target (the B1-E-25 pattern); the corrective content IS the "
        "displacement rule and the MS's own expected answer is the same "
        "statement."),
    # The practical-ownership edge (the 1.13/1.60C/2.14 precedent).
    "4CH1-PR-06 REQUIRES_PREREQUISITE 4CH1-CON-REACT-ARRANGE": (
        "Operator §6: CONFIRM as authored — practical->conceptual (the "
        "PR-05 shape): the 2.21 practical RUNS the acid-metal comparison "
        "its concept owns and its conclusion is the ranking ('The metals "
        "can be ranked in reactivity order Mg > Zn > Fe'); 2.21 attaches "
        "NO concept node — PR-06 owns it (the 1.13/1.60C/2.14 precedent, "
        "B6-ID surface intact)."),
}
NODE_NOTES = {
    # The three pass-2 CONFIRM_WITH_NOTE rows (operator §6 accepted all 13
    # with the pass-2 statuses retained; recorded CONFIRM per the
    # vocabulary rule).
    "4CH1-CON-OX-RED-AGENTS": (
        "Operator §6: CONFIRM_WITH_NOTE retained (recorded CONFIRM; the "
        "qualification carries here per the vocabulary rule). Pass-2 "
        "(B6-ID-01 for the operator): the 2.20 term-family node is "
        "BROADER than the batch-3 CON-REDOX-ELECTRONS owner (oxygen "
        "framework + agent terms + redox simultaneity vs the "
        "electron-transfer definition in the displacement context) and "
        "the note RE-TEACHES the electron framework inline (definitions, "
        "half equations, OIL RIG) — no boundary edge and no re-mint (the "
        "B5-H-02 rule); a MERGE would corrupt the distinct-SP structure. "
        "Attack result: keep the split."),
    "4CH1-CON-EXTRACTION-EVALUATION": (
        "Operator §6: CONFIRM_WITH_NOTE retained (recorded CONFIRM; the "
        "qualification carries here per the vocabulary rule). Pass-2 "
        "(B6-ID-02 for the operator): the comment-given-information skill "
        "is a SEPARATE demand from the 2.23C method relation (the "
        "B5-ID-03 know-vs-method precedent); the spec's own 'detailed "
        "knowledge ... not required' waiver is recorded in the "
        "derivation_notes; the evaluation node's single dependency edge "
        "into the method node keeps the surface honest."),
    "4CH1-MIS-ION-OXIDE-REASONING": (
        "Operator §6: CONFIRM_WITH_NOTE retained (recorded CONFIRM; the "
        "qualification carries here per the vocabulary rule). Pass-2 "
        "(B6-ID-06 for the operator): the single clean Reject column "
        "('Reject references to ions and oxides' against the "
        "reactivity-comparison expected answer) is the MIS-CUO-COLOUR-"
        "class narrow-but-exact documentation; the pdftotext line-wrap "
        "attribution is recorded in the derivation_notes (the batch-4/5 "
        "convention); the mint is defensible because the reactivity "
        "comparison is the most assessable 2.16 surface."),
}
ID_NOTES = {
    "B6-ID-01": (
        "Operator §6: KEEP_AS_IS — keep 2.20 oxidation/reduction/agent "
        "knowledge distinct from the existing electron-framework owner. "
        "The concepts overlap in instructional use but have different "
        "canonical operands and roles."),
    "B6-ID-02": (
        "Operator §6: KEEP_AS_IS — keep 2.23C extraction method distinct "
        "from 2.24C extraction evaluation: method selection and "
        "evaluation/commentary are different learning operations."),
    "B6-ID-03": (
        "Operator §6: KEEP_AS_IS — keep 2.15 arranging the series, 2.16 "
        "displacement evidence, and 2.17 the named-metal order as "
        "distinct concepts rather than collapsing three different "
        "representations/uses of reactivity."),
    "B6-ID-04": (
        "Operator §6: KEEP_AS_IS — keep 2.18 rusting conditions distinct "
        "from 2.19 prevention: establishing what causes rust and "
        "controlling/preventing rust are different operands."),
    "B6-ID-05": (
        "Operator §6: KEEP_AS_IS — keep 2.26 alloy definition distinct "
        "from 2.27C alloy hardness mechanism."),
    "B6-ID-06": (
        "Operator §6: KEEP_AS_IS — keep the single assessment-documented "
        "ion/oxide misconception as one misconception node; the evidence "
        "does not justify splitting it into multiple misconception "
        "identities."),
}
HELD_NOTE = (
    "Operator §6: all 9 held candidates (B6-H-01..09) are ACKNOWLEDGED / "
    "KEEP QUARANTINED — no held candidate is reopened, promoted, or "
    "converted into an authored edge/node by this review; the abstentions "
    "are preserved as part of the evidence record. The operator explicitly "
    "upholds: B6-H-03 remains quarantined because the cited IGNORE class "
    "is not sufficiently characterized to establish a governed "
    "misconception; B6-H-06 remains quarantined because the reverse "
    "reactivity-order dependency would duplicate the arrangement demand; "
    "B6-H-07 remains quarantined because it would create a denser "
    "shortcut around the explicit extraction-method node; B6-H-08 and "
    "B6-H-09 remain quarantined because the proposed bridges exceed the "
    "demonstrated prerequisite surface. A held record is a valid outcome — "
    "the abstention is the system's honest output.")

META_FILE = (
    "OPERATOR-OWNED verdict record for C11_BATCH6_REVIEW_SHEET (session-57 "
    "package) — verdicts recorded by operator decision, session 58 "
    "(2026-09-22), from the completed review sheet §6 "
    "(C11_BATCH6_REVIEW_SHEET_COMPLETED.md).")

META_RULING = {
    "statement": OPERATOR_STATEMENT,
    "session": SESSION,
    "decided_by": "operator",
    "decided_date": TODAY,
    "completed_sheet": (
        "C11_BATCH6_REVIEW_SHEET_COMPLETED.md (2026-09-22) — the "
        "operator-completed copy of the session-57 gate package review "
        "sheet graph/reports/C11_BATCH6_REVIEW_SHEET.md with section 6 "
        "('Completed operator verdict') appended."),
    "completed_sheet_drift": (
        "Session-58 drift record: the completed copy's §1-5 is NOT "
        "byte-identical to the in-repo gate sheet — exactly FOUR lines "
        "differ, all typographic/wording-level with zero verdict-"
        "relevant semantic change, machine-checked by the encoding "
        "script against exact string pairs: line 12 (the §1 totals "
        "separator normalized 4-col -> 5-col under the 5-column header — "
        "a markdown table-shape repair, same data); line 61 ('no "
        "duplicate mint' -> 'no duplicate concept' — one-word wording, "
        "the completed sheet's own §6 text reads 'No duplicate concept "
        "is to be minted', identical ruling); line 69 (the gate sheet's "
        "mid-word truncation 'conventio |' completed to 'convention) |' "
        "— same data); line 87 (the pathway line's tooling-chain naming "
        "replaced by the generic §18 wording — the batch-5 sheet form; "
        "the instruction is identical and the completed §6 final line "
        "names the full mechanical chain itself). Anything beyond these "
        "four lines would fail the encode. The §6 verdict content itself "
        "is complete and self-consistent: 13 node verdicts, 16 edge "
        "verdicts (B6-E-09 explicitly CONFIRM_WITH_NOTE), 6 identity "
        "rationales, 9 held acknowledgments, the final directive."),
    "mapping": (
        "The operator reviewed the session-57 gate package and returned "
        "the completed sheet §6 'Completed operator verdict': all 13 "
        "pass-2 node verdicts accepted with the statuses retained (12 "
        "CONCEPT rows CONFIRM — the 2.20 term-family row and the 2.24C "
        "evaluation row as CONFIRM_WITH_NOTE; the single MISCONCEPTION "
        "row CONFIRM_WITH_NOTE); all 16 authored semantic edges CONFIRM "
        "except the explicitly qualified B6-E-09 "
        "(O2-PERCENT-DETERMINATION REQUIRES_PREREQUISITE RUSTING) — "
        "CONFIRM_WITH_NOTE: 'this dependency is route-specific. The "
        "iron-based oxygen-percentage determination uses iron "
        "oxidation/rusting-related knowledge; the edge must not be "
        "interpreted as saying that every possible oxygen-percentage "
        "determination method universally requires the rusting concept' "
        "(a semantic guardrail, not a rejection); 'The four sanctioned "
        "cross-section edges remain confirmed and must continue to "
        "reference their governed owners/mints' (extraction method -> "
        "existing CON-ELECTROLYSIS; metal uses -> existing "
        "CON-METAL-PROPERTIES; carbonate decomposition -> batch-6 "
        "CON-REACT-ORDER; oxygen-percentage iron route -> batch-6 "
        "CON-RUSTING; 'No duplicate concept is to be minted'); the six "
        "identity decisions resolved KEEP_AS_IS each with a recorded "
        "rationale (the 2.20-vs-electron-framework operand split, the "
        "2.23C/2.24C method-vs-evaluation split, the 2.15/2.16/2.17 "
        "trio, the 2.18/2.19 conditions-vs-prevention split, the "
        "2.26C/2.27C definition-vs-mechanism split, the single "
        "misconception mint); the 9 held candidates 'ACKNOWLEDGED / "
        "KEEP QUARANTINED' — none reopened, promoted, or converted "
        "(B6-H-03/06/07/08/09 explicitly upheld); zero RR rows (the "
        "batch authored none); zero REJECTED authored edges; final "
        "directive: 'Operator verdict: PASS WITH NOTE — proceed to "
        "verdict encoding/reconciliation and the separately governed "
        "§18 promotion step.' The operator verdict file itself is the "
        "authorization (the session-54/56 precedent). ENCODING RULES: "
        "the verdict-record vocabulary (CONFIRM|REJECT|HOLD|MERGE|SPLIT) "
        "has no WITH_NOTE value, so the operator's four "
        "CONFIRM_WITH_NOTE statuses (three nodes + one edge) are "
        "recorded as CONFIRM with the qualification carried verbatim in "
        "the row's notes (the batch-1..5 precedent that qualifications "
        "ride in notes); node verdicts are keyed by CODE and edge "
        "verdicts by TRIPLE — never by row id — because the sheet's "
        "§2/§6 node numbering (table order: sheet B6-N-01 = "
        "CON-REACT-ARRANGE) differs from the template's "
        "alphabetical-by-code numbering (template B6-N-01 = "
        "CON-ALLOY-HARDNESS), while the edge ids coincide in both "
        "orderings and the explicitly named B6-E-09 triple is identical "
        "in both; each template row's id<->code/triple correspondence "
        "was asserted against the decision record before encoding; node "
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
# Load + pre-state assertions
# ---------------------------------------------------------------------------
if len(sys.argv) != 2:
    die("usage: c11_verdict_encode_batch6.py COMPLETED_SHEET.md "
        "(the operator's completed review sheet, e.g. "
        "C11_BATCH6_REVIEW_SHEET_COMPLETED.md)")
COMPLETED = Path(sys.argv[1]).resolve()
if not COMPLETED.exists():
    die(f"completed sheet not found: {COMPLETED}")
if VERDICTS.exists():
    die("scripts/c11_batch6_verdicts.yaml already exists — refusing to "
        "double-apply (the verdict round is recorded)")
if not TEMPLATE.exists():
    die("scripts/c11_batch6_verdicts_template.yaml missing — the "
        "session-57 package must be intact")
if not GATE_SHEET.exists():
    die("gate sheet missing from graph/reports/ — the session-57 "
        "package must be intact")
doc = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
if doc is None:
    die("verdict template empty")

# 0. the completed sheet's §1-5 must differ from the in-repo gate sheet by
#    EXACTLY the four characterized typographic lines (session-58 drift
#    record) and carry the §6 verdict section.
gate_lines = GATE_SHEET.read_text(encoding="utf-8").splitlines()
comp_lines = COMPLETED.read_text(encoding="utf-8").splitlines()
reconstructed = list(gate_lines)
for lineno, gate_form, comp_form in DRIFT_EXPECTED:
    idx = lineno - 1
    _require(0 <= idx < len(reconstructed)
             and reconstructed[idx] == gate_form,
             f"drift line {lineno}: in-repo gate sheet text does not "
             f"match the characterized gate form — re-characterize "
             f"before encoding")
    reconstructed[idx] = comp_form
_require(reconstructed == comp_lines[:len(gate_lines)],
         "completed sheet §1-5 drift EXCEEDS the four characterized "
         "lines — fail-closed (no encoding on uncharacterized drift)")
_require(len(comp_lines) > len(gate_lines),
         "completed sheet carries no §6 section")
_require(comp_lines[len(gate_lines)].startswith(
             "## 6. Completed operator verdict"),
         "§6 header not found where expected in the completed sheet")
for marker in ("PASS WITH NOTE", "B6-E-09",
               "route-specific", "13/13 confirmed",
               "16/16 confirmed", "6/6 KEEP_AS_IS",
               "9/9 acknowledged and quarantined"):
    _require(any(marker in ln for ln in comp_lines[len(gate_lines):]),
             f"§6 missing an expected verdict marker: {marker}")

# 1. the template must be untouched (no verdict filled anywhere)
for section in ("edge_verdicts", "node_verdicts", "identity_decisions"):
    for row in doc[section]:
        if row.get("verdict"):
            die(f"{section} {row['id']} already has a verdict — refusing")
if doc.get("rr_settlement"):
    die("unexpected rr_settlement section — the batch-6 template must "
        "carry none (zero RR edges authored)")
if doc["held_appendix_acknowledgment"].get("acknowledged"):
    die("held_appendix_acknowledgment already acknowledged — refusing")

# 2. row-shape assertions (exact session-57 surface)
assert [r["id"] for r in doc["edge_verdicts"]] == \
    [f"B6-E-{i:02d}" for i in range(1, 17)]
assert [r["id"] for r in doc["node_verdicts"]] == \
    [f"B6-N-{i:02d}" for i in range(1, 13)] + ["B6-M-01"]
assert [r["id"] for r in doc["identity_decisions"]] == \
    [f"B6-ID-{i:02d}" for i in range(1, 7)]

# 3. reconcile against the batch-6 decision record + the live store
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
_require(len(b_edges) == 16, f"batch-6 decision record carries "
         f"{len(b_edges)} edges, expected 16")
_require(len(b_suggested) == 16 and len(b_rr) == 0,
         "batch-6 edges must be 16 SUGGESTED / 0 RR at the pre-verdict "
         "state")
_require(sorted(tmpl_triples) == sorted(b_suggested)
         and len(set(tmpl_triples)) == 16,
         "edge triple mismatch between verdict template and the batch-6 "
         "decision record")
b_codes = [n["code"] for n in dec["nodes"]]
tmpl_codes = [r["code"] for r in doc["node_verdicts"]]
_require(sorted(tmpl_codes) == sorted(b_codes) and len(set(tmpl_codes)) == 13,
         "node code mismatch between verdict template and the batch-6 "
         "decision record")
_require(len(dec["held"]) == 9, f"batch-6 held count "
         f"{len(dec['held'])}, expected 9")
_require([h["id"] for h in dec["held"]]
         == [f"B6-H-{i:02d}" for i in range(1, 10)],
         "batch-6 held ids drifted from B6-H-01..09")
# every note key must hit a real row (no stale keys)
for k in EDGE_NOTES:
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
_require(len(hv) == 171 and hv == store_triples,
         "live HUMAN_VALIDATED set != the 171 pilot+batch-1+batch-2"
         "+batch-3+batch-4+batch-5 §18 promotions (the pre-verdict state "
         "must be frozen before recording batch-6 verdicts)")
_require(not (hv & set(b_suggested)),
         "a batch-6 edge is already HUMAN_VALIDATED — pre-verdict state "
         "violated")
_require(auth.get("authorization", {}).get("decision") == "AUTHORIZED",
         "§16 is not AUTHORIZED (scripts/c11_s16_authorization.yaml)")
_require(all(p.get("validated_by") == "operator"
             for p in promo["promotions"]),
         "existing promotions carry non-operator attribution (anti-forgery)")
_require(len(nodes_doc["nodes"]) == 142, f"store nodes "
         f"{len(nodes_doc['nodes'])}, expected 142")
_require(len(edges_doc["edges"]) == 334, f"store edges "
         f"{len(edges_doc['edges'])}, expected 334")
_require(len(partof) == 142
         and sum(1 for e in partof
                 if e["validation_status"] == "HUMAN_VALIDATED") == 117,
         "PART_OF layer drifted (expected 142 rows, 117 HUMAN_VALIDATED — "
         "the T-C19 G19 record; batch-6 PART_OF rows stay SUGGESTED)")

# ---------------------------------------------------------------------------
# Encode (in-place; key order preserved)
# ---------------------------------------------------------------------------
doc["meta"]["session"] = SESSION
doc["meta"]["file"] = META_FILE
doc["meta"]["operator_ruling"] = META_RULING

for row in doc["edge_verdicts"]:
    row["verdict"] = "CONFIRM"
    row["notes"] = EDGE_NOTES.get(row["triple"], "")
for row in doc["node_verdicts"]:
    row["verdict"] = "CONFIRM"
    row["notes"] = NODE_NOTES.get(row["code"], "")
for row in doc["identity_decisions"]:
    row["verdict"] = "KEEP_AS_IS"
    row["notes"] = ID_NOTES[row["id"]]
doc["held_appendix_acknowledgment"]["acknowledged"] = True
doc["held_appendix_acknowledgment"]["notes"] = HELD_NOTE

header = (
    "# T-C11 §16 batch 6 — OPERATOR verdict record (session-57 package), "
    "FILLED by operator decision session 58 (2026-09-22). OPERATOR-OWNED.\n"
    "# Operator verdict (completed review sheet §6, "
    "C11_BATCH6_REVIEW_SHEET_COMPLETED.md): all 13 node verdicts and all "
    "16\n# edge verdicts accepted with the pass-2 statuses retained (the "
    "four CONFIRM_WITH_NOTE qualifications — three nodes + edge B6-E-09 —\n"
    "# recorded in notes per the vocabulary rule); the six identity\n"
    "# decisions KEEP_AS_IS; the 9 held candidates acknowledged and "
    "quarantined; zero RR; zero REJECT.\n"
    "# Completed-sheet drift: exactly FOUR characterized typographic lines "
    "(machine-checked — see meta.operator_ruling.completed_sheet_drift).\n"
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

_require(ec == {"CONFIRM": 16},
         f"post-write: edge verdict counts drifted: {ec}")
_require(nc == {"CONFIRM": 13},
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
_e09 = next(r for r in chk["edge_verdicts"]
            if r["triple"] == "4CH1-CON-O2-PERCENT-DETERMINATION "
                              "REQUIRES_PREREQUISITE 4CH1-CON-RUSTING")
_require(_e09["notes"].startswith(
             "Operator §6 (session 58): CONFIRM_WITH_NOTE retained"),
         "post-write: the B6-E-09 qualification note drifted")
_wn_nodes = [r for r in chk["node_verdicts"]
             if r["code"] in NODE_NOTES]
_require(len(_wn_nodes) == 3
         and all(r["notes"].startswith(
                     "Operator §6: CONFIRM_WITH_NOTE retained")
                 for r in _wn_nodes),
         "post-write: the three node qualification notes drifted")
_require(not TEMPLATE.exists(),
         "post-write: verdict template was not consumed")

print("wrote", VERDICTS)
print("operator verdict recorded verbatim from the completed review sheet "
      f"§6 (decided_by operator, {TODAY})")
print("completed-sheet drift: exactly the 4 characterized typographic "
      "lines (machine-checked, nothing else)")
print(f"edge verdicts: {ec}")
print(f"node verdicts: {nc}")
print("identity decisions: 6 x KEEP_AS_IS")
print("RR settlement: none recorded (zero RR edges authored in batch 6)")
print("held_appendix: acknowledged (9 preserved, quarantined)")
print("template removed (fill + rename per the gate pathway)")
print("ENCODE COMPLETE — verdict layer established; nothing applied.")
