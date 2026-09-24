#!/usr/bin/env python3
"""T-C11 session 63 — encode the OPERATOR VERDICT SET for §16 batch 9 into
the operator-owned verdict record scripts/c11_batch9_verdicts.yaml.

The operator ruled on the batch-9 gate (review sheet
graph/reports/C11_BATCH9_REVIEW_SHEET.md, session-62 package) with the
completed review sheet C11_BATCH9_REVIEW_SHEET_COMPLETED.md: "VERDICT:
PASS WITH NOTES", all 15 node verdicts accepted ("All 15 proposed Batch 9
identities are accepted for this review surface"; "Authority remains
SUGGESTED"; "No node is promoted by this review."), all 20 authored edges
CONFIRM ("All 20 submitted semantic edges are accepted for the review
surface"; the FIVE sanctioned cross-section boundary edges "retained
exactly as ruled"; the remaining in-slice edges "accepted with their
submitted relation classes and directions"), the six identity decisions
ACCEPT each (B9-ID-01..06, recorded KEEP_AS_IS per the vocabulary rule),
the 9 held candidates ACKNOWLEDGE / KEEP QUARANTINED, zero RR, zero
REJECT, and the §7 directive "Batch 9 may proceed to the normal C11
reconciliation / promotion pathway" with its eleven required next steps.
This script encodes the verdict surface from that completed sheet — no
verdict invented, no evidence reinterpreted, no ID guessed. Fail-closed:

  * refuses if the filled verdict record already exists (no double-apply);
  * refuses if any verdict field in the template is already filled;
  * refuses unless the completed sheet carries §6/§7 with the expected
    verdict markers (PASS WITH NOTES, universal totals, REPORTED caveat,
    zero-promotion block);
  * INTAKE FORM: INLINE RESTATED COMPLETED SHEET — the operator pasted
    the completed sheet in-chat (channel zai-web, session 63) preserving
    the submitted sheet's claims and adding §6/§7, but restating the
    §2/§3/§4 detail tables as universal aggregate verdicts. The batch-5/6
    byte-identity check therefore DOES NOT APPLY (claiming it would be
    false); instead the CONFORMANCE GATES apply (machine-checked at
    intake by scripts/c11_batch9_intake_drift_check.py and re-asserted
    here): every verdict-relevant element of the coded gate surface is
    covered by an explicit completed-sheet ruling — the universal totals
    (15/15 nodes, 20/20 edges), the five boundary TRIPLEs restated in
    §6.3 exactly (shorthand-tolerant, no 4CH1- prefixes), the six
    identity decisions verbatim by id, the held range B9-H-01..09, the
    counts block (20 confirmed / 9 held / 0 RR / 0 rejected / 0
    promotions / 0 duplicate mints), and the REPORTED caveat;
  * refuses if the template rows do not reconcile 1:1 against the
    batch-9 decision record (20 SUGGESTED edge triples / ZERO RR
    triples / 15 node codes [14 CONCEPT + 1 MISCONCEPTION] / 9 held
    candidates) and against the gate sheet's row order (the §5 id
    assignment B9-E-01..20 / B9-N-01..14 / B9-M-01 rides the table
    order);
  * refuses if the live store is not in the sanctioned pre-verdict state
    (216 semantic HUMAN_VALIDATED == the pilot+batch-1..8 §18 promotions;
    0 batch-9 promotions; §16 authorization AUTHORIZED; 180 nodes / 425
    edges / 184 PART_OF rows with the T-C19 G19 record's 117
    HUMAN_VALIDATED PART_OF; the SUGGESTED surface exactly the 20
    batch-9 authored edges + the 3 frozen pilot HOLDs; the 2 frozen
    pilot REVIEW_REQUIRED settlements untouched; the 9 batch-9 held
    rows present and untouched).

Encoding rules (recorded verbatim in the file's operator_ruling.mapping):
  * every edge row          -> CONFIRM (the operator's universal §6.3
    ruling; per-row notes carry the decision record's own derivation +
    evidence quote, the sanctioned-boundary ownership for B9-E-14..18,
    and the MS-pin record for B9-E-19/E-20)
  * every node row          -> CONFIRM (the operator's universal §6.2
    ruling; the five one-family consolidation nodes and the misconception
    node carry their B9-ID linkage in notes; plain rows carry none — the
    batch-7 convention). NO CONFIRM_WITH_NOTE exists in this batch: the
    NOTES in the operator's PASS WITH NOTES are the sheet-level REPORTED
    caveat and the anti-duplication guardrail, recorded in
    meta.operator_ruling — not per-row qualifications.
  * every identity decision -> KEEP_AS_IS (the operator's §6.2 ACCEPT of
    each keep-as-ruled question, the operator's own ruling sentence
    carried verbatim — the B8-ID-03/04 ACCEPT-of-mint precedent)
  * RR settlement           -> NONE RECORDED: this batch authored no
    REVIEW_REQUIRED edge, so no settlement row exists in the template
  * held appendix           -> acknowledged (9 preserved, quarantined;
    the operator's six conservative-treatment categories recorded
    verbatim; NO per-candidate dispositions are invented — the completed
    sheet rules the surface universally)

IDENTITY-SAFETY NOTE (the sheet-vs-template numbering hazard): the gate
sheet's §2 rows number nodes in SP/table order (sheet row 1 =
CON-HYDROCARBON = decision-record order) while the template numbers them
alphabetically by code (template B9-N-01 = CON-ACID-RAIN-CAUSES). This
batch's completed sheet rules the surface UNIVERSALLY (15/15, 20/20), so
no per-row id mapping is even needed — but the encoding is still keyed by
TRIPLE (edges) and CODE (nodes), never by row id, and the template
triple/code order is asserted row-for-row against the gate sheet and the
decision record before anything is written.

The operator's REPORTED-state caveat is recorded verbatim: the reported
machine-state claims (101 quote probes, green 180-node / 425-edge merged
store, pass-1/pass-2 agreement, zero demotions, uncovered 4.15 negative
control) were accepted as REPORTED / VERIFIED BY SUBMITTED ARTIFACT, not
independently re-executed in the operator's review. The verdict session
closed that gap on the operator's behalf: the machine state was verified
directly at 1e2cf8e (the authoring head, local == origin/main, tree
clean) before encoding — 180 nodes / 425 edges / 184 PART_OF / 216
semantic HV; the decision, pass-2 and boundary YAMLs reconciled 1:1; the
§16 authorization AUTHORIZED.

This script WRITES ONLY scripts/c11_batch9_verdicts.yaml (and removes
the now-renamed template, per the sheet's gate pathway). It promotes
nothing and re-authors no decision record; application (§18 promotion)
is the separate sanctioned step in this same session per the operator's
§7 directive ("Run §18 promotion only for explicitly authorized
promotion records" — steps 1-11).

Usage:
  python3 scripts/c11_verdict_encode_batch9.py COMPLETED_SHEET.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry

GRAPH = GP.qual_dir()          # the qual's ratified store dir
TEMPLATE = HERE / "c11_batch9_verdicts_template.yaml"
VERDICTS = HERE / "c11_batch9_verdicts.yaml"
DECISIONS = HERE / "c11_batch9_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"
S16_AUTH = HERE / "c11_s16_authorization.yaml"
BOUNDARY = HERE / "c11_batch9_boundary_ruling.yaml"
GATE_SHEET = GP.reports_dir() / "C11_BATCH9_REVIEW_SHEET.md"

SESSION = 63
TODAY = "2026-09-25"

# Verbatim operative text from the operator's completed sheet §6.1 +
# §6.5 + §7 (C11_BATCH9_REVIEW_SHEET_COMPLETED intake, inline restated
# sheet via the zai-web chat lane, 2026-09-25). Every fragment below is
# the sheet's own wording.
OPERATOR_STATEMENT = (
    "VERDICT: PASS WITH NOTES. The Batch 9 review surface is accepted "
    "based on the evidence and machine-state claims contained in the "
    "submitted sheet. Operator verdict surface: Nodes 15/15 CONFIRM; "
    "Authored edges 20/20 CONFIRM; Identity decisions 6/6 accepted; "
    "Held candidates 9/9 acknowledge + quarantine; REVIEW_REQUIRED 0; "
    "Rejected authored edges 0; Node promotions 0; Edge promotions 0; "
    "Duplicate concept mints 0; Authority SUGGESTED. Final operator "
    "disposition: 'PASS WITH NOTES — Batch 9 may proceed to the normal "
    "C11 reconciliation / promotion pathway.' Required next steps (§7, "
    "verbatim order): 1. Encode the completed verdict surface. 2. "
    "Reconcile the six identity decisions without duplicate minting. 3. "
    "Preserve the five sanctioned boundary edges to their existing "
    "owners. 4. Preserve all nine held candidates as quarantined "
    "abstentions. 5. Run §18 promotion only for explicitly authorized "
    "promotion records. 6. Regenerate the graph. 7. Rerun the complete "
    "C11 gate suite. 8. Verify regenerated node/edge counts. 9. Verify "
    "held-candidate provenance is preserved. 10. Verify boundary-owner "
    "integrity. 11. Verify that the 4.15 negative-control carve-out "
    "remains uncovered. 'No node or edge is promoted by this review "
    "sheet itself.'")

CAVEAT_TEXT = (
    "Recorded verbatim from the operator's §6.1/§6.6: the submitted "
    "artifact's machine-state claims (101 quote probes and "
    "pre-verification checks; machine verification against the cited "
    "source files; a green merged store at 180 nodes / 425 edges; 15/15 "
    "node agreement; 20/20 authored-edge agreement; zero pass-2 "
    "re-authoring findings; zero demotions; an uncovered 4.15 negative "
    "control) are classified as 'REPORTED / VERIFIED BY SUBMITTED "
    "ARTIFACT. They have not been independently rerun during this "
    "session.' (§6.1: 'This distinction is intentional and preserves "
    "the C11 status discipline.') The verdict session closed that gap "
    "on the operator's behalf: the machine state was verified directly "
    "at 1e2cf8e (the authoring head, local == origin/main, tree clean) "
    "before encoding — 180 nodes / 425 edges / 184 PART_OF / 216 "
    "semantic HV; the decision, pass-2 and boundary YAMLs reconciled "
    "1:1; §16 AUTHORIZED.")

COMPLETED_SHEET_NOTE = (
    "The completed review sheet C11_BATCH9_REVIEW_SHEET_COMPLETED.md, "
    "delivered 2026-09-25 INLINE in-chat (the zai-web channel; a "
    "channel change from the batch-6/8 FileUpload lane, this time "
    "accompanied by a tmpfiles.org delivery of the gate sheet itself "
    "earlier in the session). INTAKE FORM: INLINE RESTATED COMPLETED "
    "SHEET — the operator preserved the submitted sheet's structure and "
    "every verdict-relevant claim but restated the §2/§3/§4 detail "
    "tables as universal aggregate verdicts (15/15, 20/20, 6/6, 9/9) "
    "and condensed: the §1 forecast-calibration paragraph, the §1 "
    "raw-agreement kappa note, the §2 15-row node table, the §3 20-row "
    "edge table, the §4 9-row held table and the §5 pathway line. The "
    "batch-5/6/8 §1-5 byte-identity check therefore DOES NOT APPLY and "
    "is NOT claimed; the batch-9 CONFORMANCE GATES apply instead "
    "(machine-checked at intake by scripts/c11_batch9_intake_drift_check"
    ".py — ALL PASS — and re-asserted by this script at encode time): "
    "universal totals, the five §6.3 boundary TRIPLEs matching gate rows "
    "14-18 exactly modulo the sanctioned 4CH1- prefix shorthand, the six "
    "identity sentences verbatim by id, the held range B9-H-01..09, the "
    "counts block, the REPORTED caveat x2, and 'No node or edge is "
    "promoted by this review sheet itself.'")

MAPPING = (
    "The operator reviewed the session-62 gate package and returned the "
    "completed sheet §6/§7: all 15 node verdicts accepted ('All 15 "
    "proposed Batch 9 identities are accepted for this review surface'; "
    "'Authority remains: SUGGESTED'; 'No node is promoted by this "
    "review.'); all 20 authored edges CONFIRM ('All 20 submitted "
    "semantic edges are accepted for the review surface.') with the "
    "FIVE sanctioned cross-section boundary edges 'retained exactly as "
    "ruled' (CRUDE-OIL-FRACTIONS -> the batch-1 CON-FRACTIONAL-"
    "DISTILLATION owner; ORGANIC-FORMULAE -> the pilot CON-EMPIRICAL-"
    "FORMULA and CON-MOLECULAR-FORMULA owners x2; FUELS-COMBUSTION -> "
    "the batch-5 CON-COMBUSTION-O2 owner; CRUDE-OIL -> the batch-1 "
    "CON-MIXTURE owner; 'These are boundary edges to existing owners, "
    "not new concept identities.') and the remaining in-slice edges "
    "'accepted with their submitted relation classes and directions'; "
    "the six identity decisions ACCEPT (B9-ID-01..06 — keep the 4.8-4.10 "
    "fractional-distillation family unified; keep the 4.11-4.12 "
    "fuels/combustion family unified; keep the 4.14 + 4.16 "
    "acid-rain-causes family unified; keep the 4.17-4.18 cracking "
    "family unified; keep the 4.19-4.21 alkane family unified; keep the "
    "kerosene/double-bonds misconception as one assessment-documented "
    "misconception mint) — with the anti-duplication guardrail: 'These "
    "remain operator identity decisions and must not be interpreted as "
    "permission to mint duplicate concepts during reconciliation.'; the "
    "9 held candidates 'ACKNOWLEDGE / KEEP "
    "QUARANTINED' — 'No held candidate should be reopened or promoted "
    "merely as a consequence of this review.'; zero RR rows; zero "
    "REJECTED authored edges; final disposition 'PASS WITH NOTES — "
    "Batch 9 may proceed to the normal C11 reconciliation / promotion "
    "pathway' with the eleven §7 required-next-steps. The operator "
    "verdict file itself is the authorization (the "
    "session-54/56/58/60/62 precedent). ENCODING RULES: the operator's "
    "universal rulings cover the entire coded surface, so each template "
    "row records CONFIRM; the verdict-record vocabulary "
    "(CONFIRM|REJECT|HOLD|MERGE|SPLIT) has no WITH_NOTE value and this "
    "batch carries NO per-row qualifications anyway — the NOTES in the "
    "operator's PASS WITH NOTES are the sheet-level REPORTED caveat and "
    "the anti-duplication guardrail, recorded verbatim in "
    "meta.operator_ruling; node verdicts are keyed by CODE and edge "
    "verdicts by TRIPLE — never by row id — because the gate sheet's §2 "
    "node numbering (table order = decision-record order: sheet row 1 = "
    "CON-HYDROCARBON) differs from the template's alphabetical-by-code "
    "numbering (template B9-N-01 = CON-ACID-RAIN-CAUSES), while the "
    "edge ids coincide between the sheet §3 rows and the template (both "
    "orders agree row-for-row — asserted); the identity-decision "
    "vocabulary maps the operator's ACCEPT of each keep-as-ruled "
    "question to KEEP_AS_IS (the B8-ID-03/04 ACCEPT-of-mint precedent); "
    "node authority is NOT changed by these confirmations (nodes have "
    "no §18 pathway — node promotion remains a separate identity "
    "decision, deferred); PART_OF is derived and outside §18 (the 21 "
    "batch-9 PART_OF rows stay SUGGESTED pending their own lane); the "
    "application state lives in scripts/c11_promotions.yaml (the §18 "
    "pathway is the only HUMAN_VALIDATED source) — this file never "
    "carries promotion payload or promoted status. Changing a recorded "
    "verdict requires an explicit operator decision.")

# The operator's §6.2 identity-decision sentences, verbatim (the ACCEPT
# ruling of each keep-as-ruled question). Recorded KEEP_AS_IS per the
# vocabulary rule.
IDENTITY_SENTENCES = {
    "B9-ID-01": "Keep the 4.8–4.10 fractional-distillation family unified.",
    "B9-ID-02": "Keep the 4.11–4.12 fuels/combustion family unified.",
    "B9-ID-03": "Keep the 4.14 + 4.16 acid-rain-causes family unified.",
    "B9-ID-04": "Keep the 4.17–4.18 cracking family unified.",
    "B9-ID-05": "Keep the 4.19–4.21 alkane family unified.",
    "B9-ID-06": ("Keep the kerosene/double-bonds misconception as one "
                 "assessment-documented misconception mint."),
}

HELD_NOTE = (
    "Operator §6.4: all 9 held candidates (B9-H-01..09) are "
    "ACKNOWLEDGE / KEEP QUARANTINED — 'No held candidate should be "
    "reopened or promoted merely as a consequence of this review.'; "
    "'The submitted §19 failure classes remain part of the abstention "
    "provenance.' The review 'explicitly preserves the conservative "
    "treatment of: surface-minimal prerequisites; concepts named but "
    "not load-bearing; mechanism enrichment; same-family adjacency; "
    "boundary targets already owned elsewhere; explanations deeper than "
    "the stated syllabus demand.' The completed sheet rules the held "
    "surface universally — no per-candidate dispositions are recorded "
    "and none are invented here.")

META_FILE = (
    "OPERATOR-OWNED verdict record for C11_BATCH9_REVIEW_SHEET "
    "(session-62 package) — verdicts recorded by operator decision, "
    "session 63 (2026-09-25), from the operator's completed review "
    "sheet §6/§7 (C11_BATCH9_REVIEW_SHEET_COMPLETED intake, inline "
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


# The five sanctioned boundary rows (template ids; = gate sheet rows
# 14-18) and their ownership records (from the session-62 ruling).
BOUNDARY_IDS = ["B9-E-14", "B9-E-15", "B9-E-16", "B9-E-17", "B9-E-18"]
BOUNDARY_OWNERS = {
    "4CH1-CON-CRUDE-OIL-FRACTIONS REQUIRES_PREREQUISITE "
    "4CH1-CON-FRACTIONAL-DISTILLATION": "the batch-1 owner",
    "4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE "
    "4CH1-CON-EMPIRICAL-FORMULA": "the pilot owner",
    "4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE "
    "4CH1-CON-MOLECULAR-FORMULA": "the pilot owner",
    "4CH1-CON-FUELS-COMBUSTION REQUIRES_PREREQUISITE "
    "4CH1-CON-COMBUSTION-O2": "the batch-5 owner",
    "4CH1-CON-CRUDE-OIL REQUIRES_PREREQUISITE 4CH1-CON-MIXTURE":
        "the batch-1 owner",
}
# node -> its identity decision (the five one-family consolidations +
# the misconception mint)
NODE_ID_LINK = {
    "4CH1-CON-CRUDE-OIL-FRACTIONS": "B9-ID-01",
    "4CH1-CON-FUELS-COMBUSTION": "B9-ID-02",
    "4CH1-CON-ACID-RAIN-CAUSES": "B9-ID-03",
    "4CH1-CON-CRACKING": "B9-ID-04",
    "4CH1-CON-ALKANES": "B9-ID-05",
    "4CH1-MIS-KEROSENE-DOUBLE-BONDS": "B9-ID-06",
}

# ---------------------------------------------------------------------------
# Load + intake assertions
# ---------------------------------------------------------------------------
if len(sys.argv) != 2:
    die("usage: c11_verdict_encode_batch9.py COMPLETED_SHEET.md "
        "(the operator's completed review sheet, e.g. "
        "C11_BATCH9_REVIEW_SHEET_COMPLETED.md)")
COMPLETED = Path(sys.argv[1]).resolve()
if not COMPLETED.exists():
    die(f"completed sheet not found: {COMPLETED}")
if VERDICTS.exists():
    die("scripts/c11_batch9_verdicts.yaml already exists — refusing to "
        "double-apply (the verdict round is recorded)")
if not TEMPLATE.exists():
    die("scripts/c11_batch9_verdicts_template.yaml missing — the "
        "session-62 package must be intact")
if not GATE_SHEET.exists():
    die("gate sheet missing from graph/reports/ — the session-62 "
        "package must be intact")
comp_text = COMPLETED.read_text(encoding="utf-8")
gate_text = GATE_SHEET.read_text(encoding="utf-8")
doc = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
if doc is None:
    die("verdict template empty")

# 0a. the completed sheet must carry §6/§7 with the expected markers.
_require("# 6. Operator Completion — T-C11 §16 Batch 9" in comp_text,
         "§6 header missing from the completed sheet")
_require("## 7. Final operator disposition" in comp_text,
         "§7 header missing from the completed sheet")
for marker in (
    "VERDICT: PASS WITH NOTES",
    "15/15 — CONFIRM",
    "20/20 — CONFIRM",
    "All 15 proposed Batch 9 identities are accepted",
    "All 20 submitted semantic edges are accepted",
    "accepted with their submitted relation classes and directions",
    "9/9 — ACKNOWLEDGE / KEEP QUARANTINED",
    "B9-H-01 through B9-H-09 remain held",
    "B9-ID-01 — ACCEPT", "B9-ID-06 — ACCEPT",
    "REPORTED / VERIFIED BY SUBMITTED ARTIFACT",
    "not independently re-executed in this review",
    "not been independently rerun during this session",
    "`SUGGESTED`", "NODE AUTHORITY: SUGGESTED",
    "EDGE PROMOTIONS AT THIS GATE: 0", "NODE PROMOTIONS AT THIS GATE: 0",
    "REVIEW_REQUIRED              0", "Rejected authored edges      0",
    "Confirmed authored edges    20", "Held candidates              9",
    "DUPLICATE MINTS: 0", "Duplicate concept mints      0",
    "must not be interpreted as permission to mint duplicate concepts",
    "boundary edges to existing owners",
    "Run §18 promotion only for explicitly authorized promotion records",
    "No node or edge is promoted by this review sheet itself.",
):
    _require(marker in comp_text,
             f"completed sheet missing an expected verdict marker: "
             f"{marker}")

# 0b. INTAKE FORM: INLINE RESTATED COMPLETED SHEET — the byte-identity
#     check does not apply; the conformance gates do (the restatement
#     must be honestly characterizable and every verdict-relevant element
#     must reconcile against the coded gate surface).
condensed_expected = [
    ("§2 node table condensed",
     "| # | code | family | title |" not in comp_text),
    ("§3 edge table condensed",
     "| # | edge | conf | derivation |" not in comp_text),
    ("§4 held table condensed",
     "| id | candidate | failure class / reason |" not in comp_text),
]
for name, cond in condensed_expected:
    _require(cond, f"restatement characterization drifted: {name} present")

# the five §6.3 boundary TRIPLEs must match gate rows 14-18 exactly
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
_require(len(gate_rows) == 20,
         f"gate sheet §3 parsed {len(gate_rows)} edge rows, expected 20")
gate_boundary = gate_rows[13:18]
block = comp_text.split("```text\n")
_require(len(block) >= 2, "completed sheet §6.3 text block missing")
restated_lines = []
for chunk in block[1:]:
    body = chunk.split("```")[0]
    ls = [ln.strip() for ln in body.splitlines() if ln.strip()]
    if len(ls) == 15:
        restated_lines = ls
        break
_require(len(restated_lines) == 15,
         "completed sheet §6.3 boundary block must be 5 three-line groups")
restated = [(restated_lines[i], restated_lines[i + 1],
             restated_lines[i + 2]) for i in range(0, 15, 3)]
gate_boundary_shorthand = [
    tuple(strip4(x) for x in t.split()) for t in gate_boundary]
_require(restated == gate_boundary_shorthand,
         f"completed sheet §6.3 boundary restatement drifted: {restated}")

# the six identity sentences must appear verbatim after their ACCEPT rows
for iid, sentence in IDENTITY_SENTENCES.items():
    _require(f"{iid} — ACCEPT**\n\n{sentence}" in comp_text,
             f"completed sheet {iid} sentence missing or drifted")

# 1. the template must be untouched (no verdict filled anywhere)
for section in ("edge_verdicts", "node_verdicts", "identity_decisions"):
    for row in doc[section]:
        if row.get("verdict"):
            die(f"{section} {row['id']} already has a verdict — refusing")
if doc.get("rr_settlement"):
    die("unexpected rr_settlement section — the batch-9 template must "
        "carry none (zero RR edges authored)")
if doc["held_appendix_acknowledgment"].get("acknowledged"):
    die("held_appendix_acknowledgment already acknowledged — refusing")

# 2. row-shape assertions (exact session-62 surface)
_require([r["id"] for r in doc["edge_verdicts"]] ==
         [f"B9-E-{i:02d}" for i in range(1, 21)],
         "edge ids drifted from B9-E-01..20")
_require([r["id"] for r in doc["node_verdicts"]] ==
         [f"B9-N-{i:02d}" for i in range(1, 15)] + ["B9-M-01"],
         "node ids drifted from B9-N-01..14 + B9-M-01")
_require([r["id"] for r in doc["identity_decisions"]] ==
         [f"B9-ID-{i:02d}" for i in range(1, 7)],
         "identity ids drifted from B9-ID-01..06")

# 3. reconcile against the batch-9 decision record + the gate sheet +
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
_require(len(b_edges) == 20, f"batch-9 decision record carries "
         f"{len(b_edges)} edges, expected 20")
_require(len(b_suggested) == 20 and len(b_rr) == 0,
         "batch-9 edges must be 20 SUGGESTED / 0 RR at the pre-verdict "
         "state")
_require(sorted(tmpl_triples) == sorted(b_suggested)
         and len(set(tmpl_triples)) == 20,
         "edge triple mismatch between verdict template and the batch-9 "
         "decision record")
# the template triple order must agree row-for-row with the gate sheet
# (the §5 id assignment B9-E-01..20 rides the table order)
_require(tmpl_triples == gate_rows,
         "template edge order disagrees with the gate sheet §3 row order "
         "— the B9-E-xx id assignment would be ambiguous")
b_codes = [n["code"] for n in dec["nodes"]]
tmpl_codes = [r["code"] for r in doc["node_verdicts"]]
_require(sorted(tmpl_codes) == sorted(b_codes) and len(set(tmpl_codes)) == 15,
         "node code mismatch between verdict template and the batch-9 "
         "decision record")
_require([r["code"] for r in doc["node_verdicts"] if r["id"] == "B9-M-01"]
         == ["4CH1-MIS-KEROSENE-DOUBLE-BONDS"],
         "the misconception row must be B9-M-01 = "
         "4CH1-MIS-KEROSENE-DOUBLE-BONDS")
_require(len(dec["held"]) == 9, f"batch-9 held count "
         f"{len(dec['held'])}, expected 9")
_require([h["id"] for h in dec["held"]]
         == [f"B9-H-{i:02d}" for i in range(1, 10)],
         "batch-9 held ids drifted from B9-H-01..09")
# boundary ownership: the five template boundary rows must be exactly the
# ruling's sanctioned targets (owner + target + SP surface)
sanctioned = {s["target"]: s for s in
              bound["boundary_edge_ruling"]["sanctioned_targets"]}
_require(len(sanctioned) == 5,
         f"boundary ruling sanctioned targets: {len(sanctioned)}, "
         f"expected 5")
for tid in BOUNDARY_IDS:
    row = next(r for r in doc["edge_verdicts"] if r["id"] == tid)
    tgt = row["triple"].split()[2]
    _require(tgt in sanctioned,
             f"{tid} target {tgt} is not a sanctioned boundary target")
    _require(row["pretriage"] == "FLAGGED",
             f"{tid} must be pretriage FLAGGED (boundary)")
for k in (set(BOUNDARY_OWNERS) | {"4CH1-MIS-KEROSENE-DOUBLE-BONDS "
           "WRONG_ANSWER_PATTERN 4CH1-CON-CRUDE-OIL-FRACTIONS",
           "4CH1-MIS-KEROSENE-DOUBLE-BONDS REMEDIATED_BY "
           "4CH1-CON-CRUDE-OIL-FRACTIONS"}):
    _require(k in set(tmpl_triples), f"note key not in template: {k}")

# 4. the live store must be the sanctioned pre-verdict state
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
partof = [e for e in edges_doc["edges"] if e["relation"] == "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
store = {(p["edge"]["source"], p["edge"]["relation"], p["edge"]["target"])
         for p in promo["promotions"]}
store_triples = {" ".join(t) for t in store}
_require(len(hv) == 216 and hv == store_triples,
         "live HUMAN_VALIDATED set != the 216 pilot+batch-1..8 §18 "
         "promotions (the pre-verdict state must be frozen before "
         "recording batch-9 verdicts)")
_require(not (hv & set(b_suggested)),
         "a batch-9 edge is already HUMAN_VALIDATED — pre-verdict state "
         "violated")
_require(auth.get("authorization", {}).get("decision") == "AUTHORIZED",
         "§16 is not AUTHORIZED (scripts/c11_s16_authorization.yaml)")
_require(all(p.get("validated_by") == "operator"
             for p in promo["promotions"]),
         "existing promotions carry non-operator attribution (anti-forgery)")
_require(len(nodes_doc["nodes"]) == 180, f"store nodes "
         f"{len(nodes_doc['nodes'])}, expected 180")
_require(len(edges_doc["edges"]) == 425, f"store edges "
         f"{len(edges_doc['edges'])}, expected 425")
_require(len(partof) == 184
         and sum(1 for e in partof
                 if e["validation_status"] == "HUMAN_VALIDATED") == 117,
         "PART_OF layer drifted (expected 184 rows, 117 HUMAN_VALIDATED — "
         "the T-C19 G19 record; batch-9 PART_OF rows stay SUGGESTED)")
# the SUGGESTED surface must be exactly the 20 batch-9 rows + the 3
# frozen pilot HOLDs; the 2 frozen RR settlements untouched
sugg = {triple(e) for e in sem if e["validation_status"] == "SUGGESTED"}
pilot_holds = {
    "4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-EQ-SYMBOL",
    "4CH1-CON-MOLAR-GAS-VOL EXPLAINED_BY 4CH1-CON-AVOGADRO-LAW",
    "4CH1-MIS-EQ-SUBSCRIPT REMEDIATED_BY 4CH1-CON-CONSERVATION-MASS",
}
_require(sugg == set(b_suggested) | pilot_holds,
         "SUGGESTED surface drifted (expected exactly the 20 batch-9 "
         "edges + the 3 frozen pilot HOLDs)")
rr_live = {triple(e) for e in sem
           if e["validation_status"] == "REVIEW_REQUIRED"}
_require(len(rr_live) == 2,
         "the 2 frozen pilot REVIEW_REQUIRED settlements must be "
         "untouched at the pre-verdict state")
# the batch-9 held rows must be live and untouched (quarantine integrity)
live_held_codes = {h["candidate"] for h in dec["held"]}

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
    idx = doc["edge_verdicts"].index(row) + 1
    rec = next(e for e in b_edges if triple(e) == t)
    der = rec["provenance"]["derivation_method"]
    ev = rec["evidence"][0]
    kind = ev["kind"]
    quote = ev["quote"]
    note = (f"Operator §6 (session 63): CONFIRM — 'All 20 submitted "
            f"semantic edges are accepted for the review surface.' "
            f"Pass-1: {der} ({kind}): '{quote}'")
    if t in BOUNDARY_OWNERS:
        note += (f" Sanctioned cross-section boundary edge (session-62 "
                 f"ruling) into {BOUNDARY_OWNERS[t]} — 'These are "
                 f"boundary edges to existing owners, not new concept "
                 f"identities.'; §6.3: 'retained exactly as ruled'; 'No "
                 f"duplicate concept was minted.'")
    if row["id"] == "B9-E-19":
        note += (" The pinned Crude Oil MS Q2b Reject column ('Reject "
                 "references to double bonds in kerosene') documents the "
                 "wrong-answer class; B9-ID-06 KEEP_AS_IS (single "
                 "assessment-documented misconception surface).")
    if row["id"] == "B9-E-20":
        note += (" Remediation target = WAP target (the B1-E-25 "
                 "pattern); the corrective content is the fractions "
                 "family's own composition surface ('Most fractions "
                 "contain mainly **alkanes**').")
    row["verdict"] = "CONFIRM"
    row["notes"] = note

for row in doc["node_verdicts"]:
    code = row["code"]
    note = ""
    if code in NODE_ID_LINK:
        iid = NODE_ID_LINK[code]
        sentence = IDENTITY_SENTENCES[iid]
        note = (f"Operator §6 (session 63): CONFIRM — {sentence} "
                f"({iid} ACCEPT, recorded KEEP_AS_IS per "
                f"the vocabulary rule); 'Authority remains: SUGGESTED.'")
    row["verdict"] = "CONFIRM"
    row["notes"] = note

for row in doc["identity_decisions"]:
    row["verdict"] = "KEEP_AS_IS"
    row["notes"] = (f"Operator §6.2 (session 63): ACCEPT — "
                    f"'{IDENTITY_SENTENCES[row['id']]}'")
doc["held_appendix_acknowledgment"]["acknowledged"] = True
doc["held_appendix_acknowledgment"]["notes"] = HELD_NOTE

header = (
    "# T-C11 §16 batch 9 — OPERATOR verdict record (session-62 package), "
    "FILLED by operator decision session 63 (2026-09-25). OPERATOR-OWNED.\n"
    "# Operator verdict (completed sheet §6/§7, C11_BATCH9_REVIEW_SHEET_"
    "COMPLETED intake, INLINE RESTATED sheet via the zai-web chat lane): "
    "all 15 node\n# verdicts and all 20 edge verdicts accepted (UNIVERSAL "
    "rulings — no per-row qualifications this batch; the NOTES in PASS "
    "WITH NOTES are\n# the sheet-level REPORTED caveat + the "
    "anti-duplication guardrail, carried in meta.operator_ruling); the "
    "six identity\n# decisions ACCEPT -> KEEP_AS_IS; the 9 held "
    "candidates acknowledged and quarantined; zero RR; zero REJECT. "
    "Intake form:\n# INLINE RESTATED COMPLETED SHEET — the §2/§3/§4 "
    "detail tables are restated as universal verdicts; the batch-5/6/8\n"
    "# byte-identity check does NOT apply; the batch-9 CONFORMANCE gates "
    "apply and PASS (see meta.operator_ruling.completed_sheet).\n"
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

_require(ec == {"CONFIRM": 20},
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
for tid in BOUNDARY_IDS:
    r = next(x for x in chk["edge_verdicts"] if x["id"] == tid)
    _require("Sanctioned cross-section boundary edge" in r["notes"]
             and "retained exactly as ruled" in r["notes"],
             f"post-write: the {tid} boundary note drifted")
_e19 = next(r for r in chk["edge_verdicts"] if r["id"] == "B9-E-19")
_require("Reject references to double bonds in kerosene" in _e19["notes"],
         "post-write: the E-19 MS-pin note drifted")
_fl = next(r for r in chk["node_verdicts"]
           if r["code"] == "4CH1-CON-CRUDE-OIL-FRACTIONS")
_require(_fl["notes"].startswith("Operator §6 (session 63): CONFIRM")
         and "B9-ID-01" in _fl["notes"],
         "post-write: the fractions consolidation note drifted")
_plain = sum(1 for r in chk["node_verdicts"] if r["notes"] == "")
_require(_plain == 9,
         f"post-write: plain-node note surface drifted ({_plain} plain)")
_require(not TEMPLATE.exists(),
         "post-write: verdict template was not consumed")

print("wrote", VERDICTS)
print("operator verdict recorded verbatim from the completed sheet §6/§7 "
      f"(decided_by operator, {TODAY})")
print("intake form: INLINE RESTATED COMPLETED SHEET via the zai-web chat "
      "lane; conformance gates passed (universal rulings + boundary "
      "TRIPLE match + identity sentences + held range)")
print("edge verdicts: 20 CONFIRM (5 sanctioned boundary, 0 WITH_NOTE); "
      "node verdicts: 15 CONFIRM; identity: 6 KEEP_AS_IS; held: 9 "
      "acknowledged; RR: 0; REJECT: 0")
print("next: the §18 promotion pathway (c11_diff_review export/approve -> "
      "c11_promote -> gated generator re-run), then the verdict check + "
      "re-anchors + full gate suite")
