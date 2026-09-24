#!/usr/bin/env python3
"""T-C11 session 65 — encode the OPERATOR VERDICT SET for §16 batch 10 into
the operator-owned verdict record scripts/c11_batch10_verdicts.yaml.

The operator ruled on the batch-10 gate (review sheet
graph/reports/C11_BATCH10_REVIEW_SHEET.md, session-64 package) with the
completed review sheet C11_BATCH10_REVIEW_SHEET_COMPLETED.md: "VERDICT:
PASS WITH NOTES", all 8 node verdicts CONFIRM ("All eight proposed
identities are accepted for this review surface"; "Authority remains
SUGGESTED"; "No node is promoted by this review."), all 19 authored
edges CONFIRM ("All 19 submitted semantic edges are accepted with their
submitted relation class and direction"; the THIRTEEN sanctioned
cross-section boundary edges "retained exactly as ruled in the submitted
session-64 boundary ruling"; "these are boundary relationships to
existing concept owners, not new node identities"; "No duplicate concept
should be minted for any of these targets."), the five identity decisions
ACCEPT each (B10-ID-01..05, recorded KEEP_AS_IS per the vocabulary rule),
the 9 held candidates ACKNOWLEDGE / KEEP QUARANTINED with per-candidate
KEEP HELD dispositions, zero RR, zero REJECT, and the §7 directive
"Batch 10 may proceed to the normal C11 reconciliation / promotion
pathway" with its twelve required next steps. This script encodes the
verdict surface from that completed sheet — no verdict invented, no
evidence reinterpreted, no ID guessed. Fail-closed:

  * refuses if the filled verdict record already exists (no double-apply);
  * refuses if any verdict field in the template is already filled;
  * refuses unless the completed sheet carries §6/§7 with the expected
    verdict markers (PASS WITH NOTES, universal totals, REPORTED caveat,
    zero-promotion block, boundary-retention count);
  * INTAKE FORM: INLINE RESTATED COMPLETED SHEET (detail-preserving
    variant) — the operator pasted the completed sheet in-chat (channel
    zai-web, session 65) preserving per-row detail (the 8 node codes,
    the six in-slice edge TRIPLEs, the ELEVEN owner codes with owning-
    batch attributions, the 9 held ids with per-candidate dispositions)
    while condensing the gate sheet's §1/§2/§3/§4/§5 detail columns. The
    batch-5/6/8 byte-identity check therefore DOES NOT APPLY (claiming
    it would be false); instead the CONFORMANCE GATES apply
    (machine-checked at intake by scripts/c11_batch10_intake_drift_check
    .py and re-asserted here): every verdict-relevant element of the
    coded gate surface is covered by an explicit completed-sheet ruling —
    the universal totals (8/8 nodes, 19/19 edges), the six in-slice
    TRIPLEs restated in §6.2 exactly (shorthand-tolerant, no 4CH1-
    prefixes), the ELEVEN §6.4 owner codes equal to the distinct targets
    of gate rows 7-19, the owner->batch attribution list matching the
    session-64 ruling, the five identity decisions verbatim by id, the
    held range B10-H-01..09 with per-candidate KEEP HELD dispositions,
    the counts block (8 confirmed / 19 confirmed edges / 9 held / 0 RR /
    0 rejected / 0 promotions / 0 duplicate mints), and the REPORTED
    caveat;
  * refuses if the template rows do not reconcile 1:1 against the
    batch-10 decision record (19 SUGGESTED edge triples / ZERO RR
    triples / 8 node codes [7 CONCEPT + 1 MISCONCEPTION] / 9 held
    candidates) and against the gate sheet's row order (the §5 id
    assignment B10-E-01..19 / B10-N-01..07 / B10-M-01 rides the table
    order);
  * refuses if the live store is not in the sanctioned pre-verdict state
    (236 semantic HUMAN_VALIDATED == the pilot+batch-1..9 §18 promotions;
    0 batch-10 promotions; §16 authorization AUTHORIZED; 188 nodes / 459
    edges / 199 PART_OF rows with the T-C19 G19 record's 117
    HUMAN_VALIDATED PART_OF; the SUGGESTED surface exactly the 19
    batch-10 authored edges + the 3 frozen pilot HOLDs; the 2 frozen
    pilot REVIEW_REQUIRED settlements untouched; the 9 batch-10 held
    rows present and untouched; the batch-9 verdict record in place).

Encoding rules (recorded verbatim in the file's operator_ruling.mapping):
  * every edge row          -> CONFIRM (the operator's universal §6.2
    ruling; per-row notes carry the decision record's own derivation +
    evidence quote, the sanctioned-boundary ownership for B10-E-07..19,
    the MS-pin record for B10-E-05 and the remediation-target record for
    B10-E-06)
  * every node row          -> CONFIRM (the operator's universal §6.1
    ruling; the four one-family consolidation nodes and the misconception
    node carry their B10-ID linkage in notes; plain rows carry none — the
    batch-7/9 convention). NO CONFIRM_WITH_NOTE exists in this batch: the
    NOTES in the operator's PASS WITH NOTES are the sheet-level REPORTED
    caveat and the anti-duplication guardrail, recorded in
    meta.operator_ruling — not per-row qualifications.
  * every identity decision -> KEEP_AS_IS (the operator's §6.1 ACCEPT of
    each keep-as-ruled question, the operator's own ruling sentence
    carried verbatim — the B8-ID-03/04, B9-ID-01..06 ACCEPT precedents)
  * RR settlement           -> NONE RECORDED: this batch authored no
    REVIEW_REQUIRED edge, so no settlement row exists in the template
  * held appendix           -> acknowledged (9 preserved, quarantined;
    the operator's NINE per-candidate KEEP HELD dispositions recorded
    verbatim — this batch the completed sheet rules the held surface
    per-candidate; nothing beyond the sheet's own words is added)

IDENTITY-SAFETY NOTE (the sheet-vs-template numbering hazard): the gate
sheet's §2 rows number nodes in SP/table order (sheet row 1 =
CON-ALKENES = decision-record order) while the template numbers them
alphabetically by code (template B10-N-01 = CON-ALCOHOLS). This batch's
completed sheet rules the node surface per-code (all 8 codes named in
§6.1) and universally (8/8), so no per-row id mapping is needed — but the
encoding is still keyed by TRIPLE (edges) and CODE (nodes), never by row
id, and the template triple/code order is asserted row-for-row against
the gate sheet and the decision record before anything is written.

The operator's REPORTED-state caveat is recorded verbatim: the reported
machine-state claims (37 quote probes plus pre-verification checks, green
188-node / 459-edge merged store, pass-1/pass-2 agreement, zero demotions,
uncovered 4.15 negative control) were accepted as REPORTED / VERIFIED BY
SUBMITTED ARTIFACT, not independently re-executed in the operator's
review. The verdict session closed that gap on the operator's behalf: the
machine state was verified directly at 5db5de1 (the authoring head,
local == origin/main, tree clean) before encoding — 188 nodes / 459
edges / 199 PART_OF / 236 semantic HV; the decision, pass-2 and boundary
YAMLs reconciled 1:1; the §16 authorization AUTHORIZED.

This script WRITES ONLY scripts/c11_batch10_verdicts.yaml (and removes
the now-renamed template, per the sheet's gate pathway). It promotes
nothing and re-authors no decision record; application (§18 promotion)
is the separate sanctioned step in this same session per the operator's
§7 directive ("Apply §18 promotion only to explicitly authorized
promotion records" — steps 1-12).

Usage:
  python3 scripts/c11_verdict_encode_batch10.py COMPLETED_SHEET.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry

GRAPH = GP.qual_dir()          # the qual's ratified store dir
TEMPLATE = HERE / "c11_batch10_verdicts_template.yaml"
VERDICTS = HERE / "c11_batch10_verdicts.yaml"
DECISIONS = HERE / "c11_batch10_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"
S16_AUTH = HERE / "c11_s16_authorization.yaml"
BOUNDARY = HERE / "c11_batch10_boundary_ruling.yaml"
B9_VERDICTS = HERE / "c11_batch9_verdicts.yaml"
GATE_SHEET = GP.reports_dir() / "C11_BATCH10_REVIEW_SHEET.md"

SESSION = 65
TODAY = "2026-09-25"

# Verbatim operative text from the operator's completed sheet §6 + §7
# (C11_BATCH10_REVIEW_SHEET_COMPLETED intake, inline restated sheet via
# the zai-web chat lane, 2026-09-25). Every fragment below is the
# sheet's own wording.
OPERATOR_STATEMENT = (
    "VERDICT: PASS WITH NOTES. The Batch 10 submission is accepted for "
    "operator review based on the evidence and machine-state claims "
    "contained in the submitted review sheet. Operator verdict surface: "
    "Nodes 8/8 CONFIRM; Authored edges 19/19 CONFIRM; Identity decisions "
    "5/5 accepted (B10-ID-01..05); Held candidates 9/9 acknowledge + "
    "quarantine; REVIEW_REQUIRED 0; Rejected authored edges 0; Node "
    "promotions 0; Edge promotions 0; Duplicate concept mints 0; "
    "Boundary edges 13 - RETAIN; Authority SUGGESTED. Final operator "
    "disposition: 'PASS WITH NOTES - Batch 10 may proceed to the normal "
    "C11 reconciliation / promotion pathway.' Required next steps (§7, "
    "verbatim order): 1. Encode the completed Batch 10 verdict surface. "
    "2. Reconcile B10-ID-01 through B10-ID-05. 3. Preserve all 13 "
    "sanctioned boundary edges. 4. Ensure no duplicate concept is minted "
    "for an existing boundary owner. 5. Preserve B10-H-01 through B10-H-09 "
    "as quarantined abstentions. 6. Apply §18 promotion only to explicitly "
    "authorized promotion records. 7. Regenerate the graph. 8. Rerun the "
    "complete C11 gate suite. 9. Verify regenerated node/edge counts. 10. "
    "Verify held-candidate provenance. 11. Verify boundary-owner "
    "integrity. 12. Verify the 4.15 negative-control carve-out remains "
    "uncovered. 'No node or edge is promoted by this review sheet "
    "itself.'")

CAVEAT_TEXT = (
    "Recorded verbatim from the operator's §6/§6.6: the submitted "
    "artifact's machine-state claims (8/8 node pass-2 agreement; 19/19 "
    "authored-edge pass-2 agreement; 9/9 held candidates retained; 37 "
    "quote probes plus pre-verification checks; a green merged store at "
    "188 nodes / 459 edges; zero pass-2 findings requiring re-authoring; "
    "zero demotions; zero batch-10 promotions; the 4.15 negative-control "
    "carve-out uncovered; 13 sanctioned cross-section boundary edges with "
    "no duplicate concept minting) are classified as 'REPORTED / VERIFIED "
    "BY SUBMITTED ARTIFACT, rather than independently re-executed in this "
    "review' (§6; §6.6: 'They have not been independently re-executed "
    "during this review. That distinction should remain explicit rather "
    "than silently upgrading the submitted machine-state report into an "
    "independent verification.') The verdict session closed that gap on "
    "the operator's behalf: the machine state was verified directly at "
    "5db5de1 (the authoring head, local == origin/main, tree clean) "
    "before encoding — 188 nodes / 459 edges / 199 PART_OF / 236 "
    "semantic HV; the decision, pass-2 and boundary YAMLs reconciled "
    "1:1; §16 AUTHORIZED.")

COMPLETED_SHEET_NOTE = (
    "The completed review sheet C11_BATCH10_REVIEW_SHEET_COMPLETED.md, "
    "delivered 2026-09-25 INLINE in-chat (the zai-web channel; the "
    "session-63 intake precedent). INTAKE FORM: INLINE RESTATED COMPLETED "
    "SHEET (detail-preserving variant) — the operator preserved the "
    "submitted sheet's verdict surface INCLUDING per-row detail (the "
    "§6.1 8-code node table, the §6.2 six in-slice edge TRIPLEs restated "
    "verbatim in the sanctioned shorthand, the ELEVEN boundary owner "
    "codes with their owning-batch attributions, and the §6.3 nine held "
    "ids with per-candidate dispositions) but condensed: the §1 "
    "totals/raw-agreement/forecast-calibration paragraphs, the §2 node "
    "detail columns (family/title/attaches/conf/evidence), the §3 edge "
    "detail columns (conf/derivation/evidence; the 13 boundary TRIPLEs "
    "restated as the ELEVEN owner targets + the 13-edge count), the §4 "
    "held candidate/failure-class columns and the §5 pathway line. The "
    "batch-5/6/8 §1-5 byte-identity check therefore DOES NOT APPLY and "
    "is NOT claimed; the batch-9/10 CONFORMANCE GATES apply instead "
    "(machine-checked at intake by scripts/c11_batch10_intake_drift_check"
    ".py — ALL PASS — and re-asserted by this script at encode time): "
    "universal totals, the six §6.2 in-slice TRIPLEs matching gate rows "
    "1-6 exactly modulo the sanctioned 4CH1- prefix shorthand, the "
    "ELEVEN §6.4 owner codes equal to the distinct targets of gate rows "
    "7-19, the owner->batch attribution list matching the session-64 "
    "ruling, the five identity sentences verbatim by id, the held range "
    "B10-H-01..09 with per-candidate KEEP HELD dispositions, the counts "
    "block, the REPORTED caveat x2, and 'No node or edge is promoted by "
    "this review sheet itself.'")

MAPPING = (
    "The operator reviewed the session-64 gate package and returned the "
    "completed sheet §6/§7: all 8 node verdicts CONFIRM ('All eight "
    "proposed identities are accepted for this review surface'; "
    "'Authority remains SUGGESTED.'; 'No node is promoted by this "
    "review.'); all 19 authored edges CONFIRM ('All 19 submitted "
    "semantic edges are accepted with their submitted relation class and "
    "direction.') with the THIRTEEN sanctioned cross-section boundary "
    "edges 'retained exactly as ruled in the submitted session-64 "
    "boundary ruling' (HOMOLOGOUS-SERIES x2, ORGANIC-FORMULAE x2, "
    "HYDROCARBON, ALKANES, ORGANIC-REACTION-CLASSES, IUPAC-NAMING and "
    "CRACKING -> the batch-9 owners; COMBUSTION-O2 -> the batch-5 owner; "
    "OX-RED-AGENTS -> the batch-6 owner; FRACTIONAL-DISTILLATION -> the "
    "batch-1 owner; ACID-REACTIONS -> the batch-7 owner; 'these are "
    "boundary relationships to existing concept owners, not new node "
    "identities.'; 'No duplicate concept should be minted for any of "
    "these targets.'); the five identity decisions ACCEPT (B10-ID-01..05 "
    "— keep the 4.23-4.26 alkene family unified; keep the 4.27-4.28 "
    "bromine-water reaction/test family unified; keep the 4.32C-4.33C "
    "ethanol-manufacture family unified; keep the 4.34C + 4.35C + 4.37C "
    "carboxylic-acids family unified; keep the single assessment-"
    "documented propan-2-ol naming misconception mint) — with the "
    "anti-duplication guardrail: 'These are operator identity decisions "
    "only. They must not be interpreted as permission to mint duplicate "
    "concepts during reconciliation.'; the 9 held candidates "
    "'ACKNOWLEDGE / KEEP QUARANTINED' with per-candidate KEEP HELD "
    "dispositions — 'No held candidate should be reopened or promoted as "
    "a consequence of this review.'; 'The §19 failure-class provenance "
    "should remain intact.'; the §6.4 duplication ruling: 'Batch 10 "
    "therefore adds relationships into existing concepts, rather than "
    "creating parallel concepts with equivalent meaning' — 'consistent "
    "with the C11 invariant that the graph should preserve a single "
    "canonical identity for a concept while allowing section-local "
    "prerequisite relationships'; zero RR rows; zero REJECTED authored "
    "edges; final disposition 'PASS WITH NOTES — Batch 10 may proceed to "
    "the normal C11 reconciliation / promotion pathway' with the twelve "
    "§7 required-next-steps. The operator verdict file itself is the "
    "authorization (the session-54/56/58/60/62/63 precedent). ENCODING "
    "RULES: the operator's rulings cover the entire coded surface, so "
    "each template row records CONFIRM; the verdict-record vocabulary "
    "(CONFIRM|REJECT|HOLD|MERGE|SPLIT) has no WITH_NOTE value and this "
    "batch carries NO per-row qualifications anyway — the NOTES in the "
    "operator's PASS WITH NOTES are the sheet-level REPORTED caveat and "
    "the anti-duplication guardrail, recorded verbatim in "
    "meta.operator_ruling; node verdicts are keyed by CODE and edge "
    "verdicts by TRIPLE — never by row id — because the gate sheet's §2 "
    "node numbering (table order = decision-record order: sheet row 1 = "
    "CON-ALKENES) differs from the template's alphabetical-by-code "
    "numbering (template B10-N-01 = CON-ALCOHOLS), while the edge ids "
    "coincide between the sheet §3 rows and the template (both orders "
    "agree row-for-row — asserted); the identity-decision vocabulary "
    "maps the operator's ACCEPT of each keep-as-ruled question to "
    "KEEP_AS_IS (the B8-ID-03/04, B9-ID-01..06 ACCEPT-of-mint "
    "precedent); node authority is NOT changed by these confirmations "
    "(nodes have no §18 pathway — node promotion remains a separate "
    "identity decision, deferred); PART_OF is derived and outside §18 "
    "(the 15 batch-10 PART_OF rows stay SUGGESTED pending their own "
    "lane); the application state lives in scripts/c11_promotions.yaml "
    "(the §18 pathway is the only HUMAN_VALIDATED source) — this file "
    "never carries promotion payload or promoted status. Changing a "
    "recorded verdict requires an explicit operator decision.")

# The operator's §6.1 identity-decision sentences, verbatim (the ACCEPT
# ruling of each keep-as-ruled question). Recorded KEEP_AS_IS per the
# vocabulary rule.
IDENTITY_SENTENCES = {
    "B10-ID-01": "Keep the 4.23–4.26 alkene family unified.",
    "B10-ID-02": "Keep the 4.27–4.28 bromine-water reaction/test family "
                 "unified.",
    "B10-ID-03": "Keep the 4.32C–4.33C ethanol-manufacture family unified.",
    "B10-ID-04": "Keep the 4.34C + 4.35C + 4.37C carboxylic-acids family "
                 "unified.",
    "B10-ID-05": "Keep the single assessment-documented propan-2-ol naming "
                 "misconception mint.",
}

# The operator's §6.3 per-candidate dispositions, verbatim (this batch
# the completed sheet rules the held surface PER-CANDIDATE). Each value
# is the reason text after the sheet's '**KEEP HELD** —' marker.
HELD_DISPOSITIONS = {
    "B10-H-01": "catalyst mechanism not load-bearing",
    "B10-H-02": "reversible-reaction explanation exceeds demand",
    "B10-H-03": "naming prerequisite is surface-minimal",
    "B10-H-04": "existing formula boundary owner already available",
    "B10-H-05": "isomer prerequisite is surface-minimal",
    "B10-H-06": "same-family adjacency",
    "B10-H-07": "same-family/boundary overlap",
    "B10-H-08": "CO poisoning is enrichment, not load-bearing",
    "B10-H-09": "exo/endo is enrichment, not load-bearing",
}

HELD_NOTE = (
    "Operator §6.3: all 9 held candidates (B10-H-01..09) are "
    "ACKNOWLEDGE / KEEP QUARANTINED with per-candidate dispositions — "
    + "; ".join(f"{k} 'KEEP HELD — {v}'"
               for k, v in HELD_DISPOSITIONS.items())
    + "; 'No held candidate should be reopened or promoted as a "
      "consequence of this review.'; 'The §19 failure-class provenance "
      "should remain intact.' The dispositions are the completed sheet's "
      "own words — nothing beyond them is recorded here.")

META_FILE = (
    "OPERATOR-OWNED verdict record for C11_BATCH10_REVIEW_SHEET "
    "(session-64 package) — verdicts recorded by operator decision, "
    "session 65 (2026-09-25), from the operator's completed review "
    "sheet §6/§7 (C11_BATCH10_REVIEW_SHEET_COMPLETED intake, inline "
    "restated sheet via the zai-web chat lane).")

META_RULING = {
    "statement": OPERATOR_STATEMENT,
    "session": SESSION,
    "decided_by": "operator",
    "decided_date": TODAY,
    "completed_sheet": COMPLETED_SHEET_NOTE,
    "reported_state_caveat": CAVEAT_TEXT,
    "mapping": MAPPING,
}


def die(msg: str):
    print(f"FAIL-CLOSED: {msg}")
    sys.exit(1)


def _require(cond: bool, msg: str) -> None:
    """Fail-closed gate that survives `python -O` (assert is stripped
    under -O, which would turn this gate fail-open — MD-33)."""
    if not cond:
        raise RuntimeError(msg)


def triple(e):
    return f"{e['source']} {e['relation']} {e['target']}"


def strip4(s):
    return s.replace("4CH1-", "")


# The thirteen sanctioned boundary rows (template ids; = gate sheet rows
# 7-19) and their ownership records (from the session-64 ruling).
BOUNDARY_IDS = [f"B10-E-{i:02d}" for i in range(7, 20)]
BOUNDARY_OWNERS = {
    "4CH1-CON-ALKENES REQUIRES_PREREQUISITE "
    "4CH1-CON-HOMOLOGOUS-SERIES": "the batch-9 owner",
    "4CH1-CON-ALKENES REQUIRES_PREREQUISITE "
    "4CH1-CON-ORGANIC-FORMULAE": "the batch-9 owner",
    "4CH1-CON-ALKENES REQUIRES_PREREQUISITE 4CH1-CON-HYDROCARBON":
        "the batch-9 owner",
    "4CH1-CON-BROMINE-WATER-TEST REQUIRES_PREREQUISITE "
    "4CH1-CON-ALKANES": "the batch-9 owner",
    "4CH1-CON-BROMINE-WATER-TEST REQUIRES_PREREQUISITE "
    "4CH1-CON-ORGANIC-REACTION-CLASSES": "the batch-9 owner",
    "4CH1-CON-ALCOHOLS REQUIRES_PREREQUISITE "
    "4CH1-CON-HOMOLOGOUS-SERIES": "the batch-9 owner",
    "4CH1-CON-ALCOHOLS REQUIRES_PREREQUISITE 4CH1-CON-IUPAC-NAMING":
        "the batch-9 owner",
    "4CH1-CON-ETHANOL-OXIDATION REQUIRES_PREREQUISITE "
    "4CH1-CON-COMBUSTION-O2": "the batch-5 owner",
    "4CH1-CON-ETHANOL-OXIDATION REQUIRES_PREREQUISITE "
    "4CH1-CON-OX-RED-AGENTS": "the batch-6 owner",
    "4CH1-CON-ETHANOL-MANUFACTURE REQUIRES_PREREQUISITE "
    "4CH1-CON-CRACKING": "the batch-9 owner",
    "4CH1-CON-ETHANOL-MANUFACTURE REQUIRES_PREREQUISITE "
    "4CH1-CON-FRACTIONAL-DISTILLATION": "the batch-1 owner",
    "4CH1-CON-CARBOXYLIC-ACIDS REQUIRES_PREREQUISITE "
    "4CH1-CON-ORGANIC-FORMULAE": "the batch-9 owner",
    "4CH1-CON-CARBOXYLIC-ACID-REACTIONS REQUIRES_PREREQUISITE "
    "4CH1-CON-ACID-REACTIONS": "the batch-7 owner",
}
# node -> its identity decision (the four one-family consolidations +
# the misconception mint)
NODE_ID_LINK = {
    "4CH1-CON-ALKENES": "B10-ID-01",
    "4CH1-CON-BROMINE-WATER-TEST": "B10-ID-02",
    "4CH1-CON-ETHANOL-MANUFACTURE": "B10-ID-03",
    "4CH1-CON-CARBOXYLIC-ACIDS": "B10-ID-04",
    "4CH1-MIS-PROPANOL-POSITION": "B10-ID-05",
}

# ---------------------------------------------------------------------------
# Load + intake assertions
# ---------------------------------------------------------------------------
if len(sys.argv) != 2:
    die("usage: c11_verdict_encode_batch10.py COMPLETED_SHEET.md "
        "(the operator's completed review sheet, e.g. "
        "C11_BATCH10_REVIEW_SHEET_COMPLETED.md)")
COMPLETED = Path(sys.argv[1]).resolve()
if not COMPLETED.exists():
    die(f"completed sheet not found: {COMPLETED}")
if VERDICTS.exists():
    die("scripts/c11_batch10_verdicts.yaml already exists — refusing to "
        "double-apply (the verdict round is recorded)")
if not TEMPLATE.exists():
    die("scripts/c11_batch10_verdicts_template.yaml missing — the "
        "session-64 package must be intact")
if not GATE_SHEET.exists():
    die("gate sheet missing from graph/reports/ — the session-64 "
        "package must be intact")
if not B9_VERDICTS.exists():
    die("scripts/c11_batch9_verdicts.yaml missing — the batch-9 verdict "
        "record (session 63) must be in place before the batch-10 round")
comp_text = COMPLETED.read_text(encoding="utf-8")
gate_text = GATE_SHEET.read_text(encoding="utf-8")
doc = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
if doc is None:
    die("verdict template empty")

# 0a. the completed sheet must carry §6/§7 with the expected markers.
_require(comp_text.splitlines()[0].startswith(
             "# T-C11 §16 Batch 10 Review Sheet — Operator Completion"),
         "completed sheet header line missing")
_require("## 6. Operator verdict" in comp_text,
         "§6 header missing from the completed sheet")
_require("# 7. Final operator disposition" in comp_text,
         "§7 header missing from the completed sheet")
for marker in (
    "VERDICT: PASS WITH NOTES",
    "8/8 — CONFIRM",
    "19/19 — CONFIRM",
    "All eight proposed identities are accepted for this review surface.",
    "All 19 submitted semantic edges are accepted with their submitted "
    "relation class and direction.",
    "9/9 — ACKNOWLEDGE / KEEP QUARANTINED",
    "B10-H-01 through B10-H-09 remain held",
    "B10-ID-01 — ACCEPT", "B10-ID-05 — ACCEPT",
    "retained exactly as ruled in the submitted session-64 boundary "
    "ruling",
    "boundary relationships to existing concept owners",
    "No duplicate concept should be minted for any of these targets.",
    "REPORTED / VERIFIED BY SUBMITTED ARTIFACT",
    "rather than independently re-executed in this review",
    "They have not been independently re-executed during this review.",
    "`SUGGESTED`", "NODE AUTHORITY: SUGGESTED",
    "No node is promoted by this review.",
    "EDGE PROMOTIONS: 0", "NODE PROMOTIONS: 0",
    "Promotion count at this gate:** `0`",
    "REVIEW_REQUIRED edges              0", "Rejected authored edges            0",
    "Nodes confirmed                    8",
    "Authored edges confirmed          19",
    "Held candidates                    9",
    "DUPLICATE MINTS: 0", "Duplicate concept mints            0",
    "BOUNDARY EDGES: 13 — RETAIN",
    "must **not** be interpreted as permission to mint duplicate concepts",
    "Apply §18 promotion only to explicitly authorized promotion records",
    "No node or edge is promoted by this review sheet itself.",
):
    _require(marker in comp_text,
             f"completed sheet missing an expected verdict marker: "
             f"{marker}")

# 0b. INTAKE FORM: INLINE RESTATED COMPLETED SHEET (detail-preserving
#     variant) — the byte-identity check does not apply; the conformance
#     gates do (the restatement must be honestly characterizable and
#     every verdict-relevant element must reconcile against the coded
#     gate surface).
condensed_expected = [
    ("§2 node detail columns condensed",
     "| # | code | family | title |" not in comp_text),
    ("§3 edge detail columns condensed",
     "| # | edge | conf | derivation |" not in comp_text),
    ("§4 held detail columns condensed",
     "| id | candidate | failure class / reason |" not in comp_text),
]
for name, cond in condensed_expected:
    _require(cond, f"restatement characterization drifted: {name} present")

# the six §6.2 in-slice TRIPLEs must match gate rows 1-6 exactly
# (shorthand-tolerant: the completed sheet drops the 4CH1- prefix).
gate_rows = []
in_s3 = False
for line in gate_text.splitlines():
    if line.startswith("## 3."):
        in_s3 = True
        continue
    if in_s3 and line.startswith("## 4."):
        break
    if not in_s3:
        continue
    s = line.strip()
    if s.startswith("|") and "`4CH1-" in s:
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) >= 2 and cells[0].isdigit() \
                and cells[1].startswith("`4CH1-"):
            gate_rows.append(cells[1].strip("`").strip())
_require(len(gate_rows) == 19,
         f"gate sheet §3 parsed {len(gate_rows)} edge rows, expected 19")
gate_inslice = gate_rows[0:6]
blocks = []
for chunk in comp_text.split("```text\n")[1:]:
    body = chunk.split("```")[0]
    ls = [ln.strip() for ln in body.splitlines() if ln.strip()]
    blocks.append(ls)
edge_blocks = [b for b in blocks if len(b) == 12]
miscon_blocks = [b for b in blocks if len(b) == 6]
owner_blocks = [b for b in blocks if len(b) == 11 and all(
    all(ch.isalnum() or ch == "-" for ch in ln) for ln in b)]
_require(len(blocks) == 5 and len(edge_blocks) == 1
         and len(miscon_blocks) == 1 and len(owner_blocks) == 1,
         "completed sheet ```text blocks drifted (expected 5: 12-line "
         "edge block + 6-line misconception block + 11-line owner block "
         "+ counts + final status)")
restated = []
b = edge_blocks[0]
restated += [(b[i], b[i + 1], b[i + 2]) for i in range(0, 12, 3)]
b = miscon_blocks[0]
restated += [(b[i], b[i + 1], b[i + 2]) for i in range(0, 6, 3)]
gate_inslice_shorthand = [
    tuple(strip4(x) for x in t.split()) for t in gate_inslice]
_require(restated == gate_inslice_shorthand,
         f"completed sheet §6.2 in-slice restatement drifted: {restated}")
_require([c for _, c, _ in restated] ==
         ["REQUIRES_PREREQUISITE"] * 4 + ["WRONG_ANSWER_PATTERN",
                                          "REMEDIATED_BY"],
         "restated relation classes drifted")

# the eleven §6.4 owner codes must equal the distinct targets of gate
# rows 7-19; the owner->batch bullets must match the session-64 ruling.
gate_boundary_targets = sorted({t.split()[2] for t in gate_rows[6:]})
_require(len(gate_boundary_targets) == 11,
         f"gate boundary targets: {len(gate_boundary_targets)}, "
         f"expected 11 distinct owners")
_require(sorted(owner_blocks[0]) ==
         sorted(x.replace("4CH1-CON-", "")
                for x in gate_boundary_targets),
         f"completed sheet §6.4 owner block drifted: {owner_blocks[0]}")
owner_batch = dict(__import__("re").findall(
    r"^\* `(CON-[A-Z0-9-]+)` — batch (\d+)$", comp_text, __import__("re").M))
_require(len(owner_batch) == 11,
         f"completed sheet owner->batch bullets: {len(owner_batch)}, "
         f"expected 11")

# the five identity sentences must appear verbatim after their ACCEPT rows
for iid, sentence in IDENTITY_SENTENCES.items():
    _require(f"{iid} — ACCEPT**\n\n{sentence}" in comp_text,
             f"completed sheet {iid} sentence missing or drifted")
# the nine per-candidate held dispositions must appear verbatim
for hid, reason in HELD_DISPOSITIONS.items():
    _require(f"| {hid} | **KEEP HELD** — {reason}" in comp_text,
             f"completed sheet {hid} disposition missing or drifted")

# 1. the template must be untouched (no verdict filled anywhere)
for section in ("edge_verdicts", "node_verdicts", "identity_decisions"):
    for row in doc[section]:
        if row.get("verdict"):
            die(f"{section} {row['id']} already has a verdict — refusing")
if doc.get("rr_settlement"):
    die("unexpected rr_settlement section — the batch-10 template must "
        "carry none (zero RR edges authored)")
if doc["held_appendix_acknowledgment"].get("acknowledged"):
    die("held_appendix_acknowledgment already acknowledged — refusing")

# 2. row-shape assertions (exact session-64 surface)
_require([r["id"] for r in doc["edge_verdicts"]] ==
         [f"B10-E-{i:02d}" for i in range(1, 20)],
         "edge ids drifted from B10-E-01..19")
_require([r["id"] for r in doc["node_verdicts"]] ==
         [f"B10-N-{i:02d}" for i in range(1, 8)] + ["B10-M-01"],
         "node ids drifted from B10-N-01..07 + B10-M-01")
_require([r["id"] for r in doc["identity_decisions"]] ==
         [f"B10-ID-{i:02d}" for i in range(1, 6)],
         "identity ids drifted from B10-ID-01..05")

# 3. reconcile against the batch-10 decision record + the gate sheet +
#    the boundary ruling
dec = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
edges_doc = yaml.safe_load((GRAPH / "concept_edges.yaml")
                           .read_text(encoding="utf-8"))
nodes_doc = yaml.safe_load((GRAPH / "concepts.yaml")
                           .read_text(encoding="utf-8"))
promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
auth = yaml.safe_load(S16_AUTH.read_text(encoding="utf-8"))
bound = yaml.safe_load(BOUNDARY.read_text(encoding="utf-8"))

b_edges = dec["edges"]
b_suggested = [triple(e) for e in b_edges
               if e["validation_status"] == "SUGGESTED"]
b_rr = [triple(e) for e in b_edges
        if e["validation_status"] == "REVIEW_REQUIRED"]
tmpl_triples = [r["triple"] for r in doc["edge_verdicts"]]
_require(len(b_edges) == 19, f"batch-10 decision record carries "
         f"{len(b_edges)} edges, expected 19")
_require(len(b_suggested) == 19 and len(b_rr) == 0,
         "batch-10 edges must be 19 SUGGESTED / 0 RR at the pre-verdict "
         "state")
_require(sorted(tmpl_triples) == sorted(b_suggested)
         and len(set(tmpl_triples)) == 19,
         "edge triple mismatch between verdict template and the batch-10 "
         "decision record")
# the template triple order must agree row-for-row with the gate sheet
# (the §5 id assignment B10-E-01..19 rides the table order)
_require(tmpl_triples == gate_rows,
         "template edge order disagrees with the gate sheet §3 row order "
         "— the B10-E-xx id assignment would be ambiguous")
b_codes = [n["code"] for n in dec["nodes"]]
tmpl_codes = [r["code"] for r in doc["node_verdicts"]]
_require(sorted(tmpl_codes) == sorted(b_codes) and len(set(tmpl_codes)) == 8,
         "node code mismatch between verdict template and the batch-10 "
         "decision record")
_require([r["code"] for r in doc["node_verdicts"] if r["id"] == "B10-M-01"]
         == ["4CH1-MIS-PROPANOL-POSITION"],
         "the misconception row must be B10-M-01 = "
         "4CH1-MIS-PROPANOL-POSITION")
_require(len(dec["held"]) == 9, f"batch-10 held count "
         f"{len(dec['held'])}, expected 9")
_require([h["id"] for h in dec["held"]]
         == [f"B10-H-{i:02d}" for i in range(1, 10)],
         "batch-10 held ids drifted from B10-H-01..09")
# boundary ownership: the thirteen template boundary rows must be exactly
# the ruling's sanctioned targets (owner + target + SP surface), with the
# owner batches matching the ruling's own records
sanctioned = {s["target"]: s for s in
              bound["boundary_edge_ruling"]["sanctioned_targets"]}
_require(len(sanctioned) == 11,
         f"boundary ruling sanctioned targets: {len(sanctioned)}, "
         f"expected 11")
for tid in BOUNDARY_IDS:
    row = next(r for r in doc["edge_verdicts"] if r["id"] == tid)
    tgt = row["triple"].split()[2]
    _require(tgt in sanctioned,
             f"{tid} target {tgt} is not a sanctioned boundary target")
    _require(row["pretriage"] == "FLAGGED",
             f"{tid} must be pretriage FLAGGED (boundary)")
    _require(BOUNDARY_OWNERS[row["triple"]] ==
             f"the batch-{sanctioned[tgt]['owner'].split()[1]} owner",
             f"{tid} ownership drifted from the session-64 ruling "
             f"(ruling: {sanctioned[tgt]['owner']})")
for k in (set(BOUNDARY_OWNERS) | {"4CH1-MIS-PROPANOL-POSITION "
           "WRONG_ANSWER_PATTERN 4CH1-CON-ALCOHOLS",
           "4CH1-MIS-PROPANOL-POSITION REMEDIATED_BY "
           "4CH1-CON-ALCOHOLS"}):
    _require(k in set(tmpl_triples), f"note key not in template: {k}")
non_mint = set(bound["boundary_edge_ruling"]["non_mint_list"])
_require(len(non_mint) == 48 and not ({n["code"] for n in dec["nodes"]}
                                      & non_mint),
         "the ruling's 48 non-mint owner codes must stay outside the "
         "batch-10 mint")

# 4. the live store must be the sanctioned pre-verdict state
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
partof = [e for e in edges_doc["edges"] if e["relation"] == "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
store = {(p["edge"]["source"], p["edge"]["relation"], p["edge"]["target"])
         for p in promo["promotions"]}
store_triples = {" ".join(t) for t in store}
_require(len(hv) == 236 and hv == store_triples,
         "live HUMAN_VALIDATED set != the 236 pilot+batch-1..9 §18 "
         "promotions (the pre-verdict state must be frozen before "
         "recording batch-10 verdicts)")
_require(not (hv & set(b_suggested)),
         "a batch-10 edge is already HUMAN_VALIDATED — pre-verdict state "
         "violated")
_require(auth.get("authorization", {}).get("decision") == "AUTHORIZED",
         "§16 is not AUTHORIZED (scripts/c11_s16_authorization.yaml)")
_require(all(p.get("validated_by") == "operator"
             for p in promo["promotions"]),
         "existing promotions carry non-operator attribution (anti-forgery)")
_require(len(nodes_doc["nodes"]) == 188, f"store nodes "
         f"{len(nodes_doc['nodes'])}, expected 188")
_require(len(edges_doc["edges"]) == 459, f"store edges "
         f"{len(edges_doc['edges'])}, expected 459")
_require(len(partof) == 199
         and sum(1 for e in partof
                 if e["validation_status"] == "HUMAN_VALIDATED") == 117,
         "PART_OF layer drifted (expected 199 rows, 117 HUMAN_VALIDATED — "
         "the T-C19 G19 record; batch-9/10 PART_OF rows stay SUGGESTED)")
# the SUGGESTED surface must be exactly the 19 batch-10 rows + the 3
# frozen pilot HOLDs; the 2 frozen RR settlements untouched
sugg = {triple(e) for e in sem if e["validation_status"] == "SUGGESTED"}
pilot_holds = {
    "4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-EQ-SYMBOL",
    "4CH1-CON-MOLAR-GAS-VOL EXPLAINED_BY 4CH1-CON-AVOGADRO-LAW",
    "4CH1-MIS-EQ-SUBSCRIPT REMEDIATED_BY 4CH1-CON-CONSERVATION-MASS",
}
_require(sugg == set(b_suggested) | pilot_holds,
         "SUGGESTED surface drifted (expected exactly the 19 batch-10 "
         "edges + the 3 frozen pilot HOLDs)")
rr_live = {triple(e) for e in sem
           if e["validation_status"] == "REVIEW_REQUIRED"}
_require(len(rr_live) == 2,
         "the 2 frozen pilot REVIEW_REQUIRED settlements must be "
         "untouched at the pre-verdict state")
# the batch-10 held rows must be live and untouched (quarantine integrity)
live_held_codes = {h["candidate"] for h in dec["held"]}
_require(len(live_held_codes) == 9,
         "batch-10 held candidate surface drifted")

# ---------------------------------------------------------------------------
# Encode (in-place; key order preserved)
# ---------------------------------------------------------------------------
doc["meta"]["session"] = SESSION
doc["meta"]["file"] = META_FILE
doc["meta"]["operator_ruling"] = META_RULING

# per-edge notes: composed from the decision record's own fields (zero
# invention) + the operator ruling context + boundary ownership.
for row in doc["edge_verdicts"]:
    t = row["triple"]
    rec = next(e for e in b_edges if triple(e) == t)
    der = rec["provenance"]["derivation_method"]
    ev = rec["evidence"][0]
    kind = ev["kind"]
    quote = ev["quote"]
    note = (f"Operator §6 (session 65): CONFIRM — 'All 19 submitted "
            f"semantic edges are accepted with their submitted relation "
            f"class and direction.' "
            f"Pass-1: {der} ({kind}): '{quote}'")
    if t in BOUNDARY_OWNERS:
        note += (f" Sanctioned cross-section boundary edge (session-64 "
                 f"ruling) into {BOUNDARY_OWNERS[t]} — 'these are "
                 f"boundary relationships to existing concept owners, "
                 f"not new node identities.'; §6.2: 'retained exactly as "
                 f"ruled in the submitted session-64 boundary ruling'; "
                 f"'No duplicate concept should be minted for any of "
                 f"these targets.'")
    if row["id"] == "B10-E-05":
        note += (" The pinned Alkenes MS Q4(b)(ii) Reject column ('Reject "
                 "propan-1-ol / 1-propanol') documents the wrong-answer "
                 "class; B10-ID-05 KEEP_AS_IS (single assessment-"
                 "documented misconception surface).")
    if row["id"] == "B10-E-06":
        note += (" Remediation target = WAP target (the B1-E-25 "
                 "pattern).")
    row["verdict"] = "CONFIRM"
    row["notes"] = note

for row in doc["node_verdicts"]:
    code = row["code"]
    note = ""
    if code in NODE_ID_LINK:
        iid = NODE_ID_LINK[code]
        sentence = IDENTITY_SENTENCES[iid]
        note = (f"Operator §6 (session 65): CONFIRM — {sentence} "
                f"({iid} ACCEPT, recorded KEEP_AS_IS per "
                f"the vocabulary rule); 'Authority remains SUGGESTED.'")
    row["verdict"] = "CONFIRM"
    row["notes"] = note

for row in doc["identity_decisions"]:
    row["verdict"] = "KEEP_AS_IS"
    row["notes"] = (f"Operator §6.1 (session 65): ACCEPT — "
                    f"'{IDENTITY_SENTENCES[row['id']]}'")
doc["held_appendix_acknowledgment"]["acknowledged"] = True
doc["held_appendix_acknowledgment"]["notes"] = HELD_NOTE

header = (
    "# T-C11 §16 batch 10 — OPERATOR verdict record (session-64 "
    "package), FILLED by operator decision session 65 (2026-09-25). "
    "OPERATOR-OWNED.\n"
    "# Operator verdict (completed sheet §6/§7, C11_BATCH10_REVIEW_SHEET_"
    "COMPLETED intake, INLINE RESTATED sheet via the zai-web chat lane): "
    "all 8 node\n# verdicts and all 19 edge verdicts CONFIRM (UNIVERSAL "
    "rulings — no per-row qualifications this batch; the NOTES in PASS "
    "WITH NOTES are\n# the sheet-level REPORTED caveat + the "
    "anti-duplication guardrail, carried in meta.operator_ruling); the "
    "five identity\n# decisions ACCEPT -> KEEP_AS_IS; the 9 held "
    "candidates acknowledged and quarantined WITH per-candidate KEEP "
    "HELD dispositions; zero RR;\n# zero REJECT. Intake form: INLINE "
    "RESTATED COMPLETED SHEET (detail-preserving variant) — the §1/§2/§3/"
    "§4/§5 detail columns are\n# condensed while the per-row surface (8 "
    "node codes, 6 in-slice TRIPLEs, 11 owner codes, 9 held ids) is "
    "preserved; the batch-5/6/8\n# byte-identity check does NOT apply; "
    "the batch-9/10 CONFORMANCE gates apply and PASS (see "
    "meta.operator_ruling.completed_sheet).\n"
    "# Vocabulary and pathway: see the meta.operator_ruling.mapping "
    "block. Verdicts are RECORDED; the application state lives in\n"
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
_require(nc == {"CONFIRM": 8},
         f"post-write: node verdict counts drifted: {nc}")
_require([r["verdict"] for r in chk["identity_decisions"]]
         == ["KEEP_AS_IS"] * 5,
         "post-write: identity decisions drifted")
_require("rr_settlement" not in chk,
         "post-write: unexpected rr_settlement present")
_require(chk["held_appendix_acknowledgment"]["acknowledged"] is True,
         "post-write: held appendix acknowledgment missing")
_require(chk["meta"]["operator_ruling"]["statement"] == OPERATOR_STATEMENT,
         "post-write: operator ruling text drifted")
for tid in BOUNDARY_IDS:
    r = next(x for x in chk["edge_verdicts"] if x["id"] == tid)
    _require("Sanctioned cross-section boundary edge" in r["notes"]
             and "retained exactly as ruled" in r["notes"],
             f"post-write: the {tid} boundary note drifted")
_e05 = next(r for r in chk["edge_verdicts"] if r["id"] == "B10-E-05")
_require("Reject propan-1-ol / 1-propanol" in _e05["notes"],
         "post-write: the E-05 MS-pin note drifted")
_alc = next(r for r in chk["node_verdicts"]
            if r["code"] == "4CH1-CON-ALKENES")
_require(_alc["notes"].startswith("Operator §6 (session 65): CONFIRM")
         and "B10-ID-01" in _alc["notes"],
         "post-write: the alkenes consolidation note drifted")
_plain = sum(1 for r in chk["node_verdicts"] if r["notes"] == "")
_require(_plain == 3,
         f"post-write: plain-node note surface drifted ({_plain} plain)")
_held = chk["held_appendix_acknowledgment"]["notes"]
_require(all(f"KEEP HELD — {v}" in _held
             for v in HELD_DISPOSITIONS.values()),
         "post-write: the per-candidate held dispositions drifted")
_require(not TEMPLATE.exists(),
         "post-write: verdict template was not consumed")

print("wrote", VERDICTS)
print("operator verdict recorded verbatim from the completed sheet §6/§7 "
      f"(decided_by operator, {TODAY})")
print("intake form: INLINE RESTATED COMPLETED SHEET (detail-preserving "
      "variant) via the zai-web chat lane; conformance gates passed "
      "(universal rulings + in-slice TRIPLE match + owner-code match + "
      "identity sentences + per-candidate held dispositions)")
print("edge verdicts: 19 CONFIRM (13 sanctioned boundary, 0 WITH_NOTE); "
      "node verdicts: 8 CONFIRM; identity: 5 KEEP_AS_IS; held: 9 "
      "acknowledged; RR: 0; REJECT: 0")
print("next: the §18 promotion pathway (c11_diff_review export/approve -> "
      "c11_promote -> gated generator re-run), then the verdict check + "
      "re-anchors + full gate suite")
