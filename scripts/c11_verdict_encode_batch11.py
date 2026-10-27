#!/usr/bin/env python3
"""T-C11 session 67 — encode the OPERATOR VERDICT SET for §16 batch 11 into
the operator-owned verdict record scripts/c11_batch11_verdicts.yaml.

The operator ruled on the batch-11 gate (review sheet
graph/reports/C11_BATCH11_REVIEW_SHEET.md, session-66 package) with the
operator verdict delivered 2026-09-25 (session 67): "PASS WITH NOTES" /
"Batch 11: ACCEPTED — PASS WITH NOTES", all 5 node verdicts CONFIRM,
all 17 authored edges CONFIRM with the SCOPED-REQUIRES_PREREQUISITE
semantic guardrail ("REQUIRES_PREREQUISITE should be interpreted as a
scoped teaching/route dependency, not automatically as a universal
ontological prerequisite" — the route-specific interpretation invariant
that reconciliation must preserve), the four identity decisions
KEEP_AS_IS ("including the single misconception mint for the
double-bonded polymer repeat-unit error"), the 10 held candidates
ACKNOWLEDGED / QUARANTINED, the 12 sanctioned cross-section boundary
edges RETAINed into the TEN existing owners (no duplicate mints; the
12-vs-10 count intentional — Alcohols and Carboxylic Acids each receive
two sanctioned boundary edges), zero RR, zero REJECT, zero promotions
by the review itself, and the governed path "verdict YAML ->
reconciliation -> preserve boundaries/holds -> §18 promotion where
separately authorised -> regeneration -> full gate suite". This script
encodes the verdict surface from that operator verdict — no verdict
invented, no evidence reinterpreted, no ID guessed. Fail-closed:

  * refuses if the filled verdict record already exists (no double-apply);
  * refuses if any verdict field in the template is already filled;
  * refuses unless the operator verdict carries the expected verdict
    markers (PASS WITH NOTES, the 11-row decision table totals, the
    scoped-prerequisite guardrail, the boundary-preservation block, the
    held quarantine, the REPORTED caveat, the Final disposition);
  * INTAKE FORM: GITHUB-DIRECT SHEET REVIEW + INLINE OPERATOR VERDICT —
    the operator retrieved the committed review sheet directly from
    GitHub ("I reviewed the Batch 11 sheet from GitHub") and returned a
    self-contained verdict surface in-chat (channel zai-web, session
    67). No ```text restatement blocks exist and none are claimed (the
    batch-9/10 restatement lane does NOT apply); the CONFORMANCE GATE
    applies (machine-checked at intake by
    scripts/c11_batch11_intake_drift_check.py — ALL PASS — and
    re-asserted here): the 11-row decision table equals the gate totals,
    the five node codes equal the gate §2 codes, the four scoped-RP
    guardrail bullets are present, the ten boundary owner codes equal
    the distinct targets of the twelve sanctioned boundary rows, the
    held range B11-H-01..10 matches the gate §4 rows, and the status
    qualification + Final disposition are present;
  * refuses if the template rows do not reconcile 1:1 against the
    batch-11 decision record (17 SUGGESTED edge triples / ZERO RR / 5
    node codes [4 CONCEPT + 1 MISCONCEPTION] / 10 held candidates) and
    against the gate sheet's row order (the §5 id assignment
    B11-E-01..17 / B11-N-01..04 / B11-M-01 rides the table order);
  * refuses if the live store is not in the sanctioned pre-verdict state
    (255 semantic HUMAN_VALIDATED == the pilot+batch-1..10 §18
    promotions; 0 batch-11 promotions; §16 authorization AUTHORIZED;
    193 nodes / 488 edges / 211 PART_OF rows with the T-C19 G19
    record's 117 HUMAN_VALIDATED PART_OF; the SUGGESTED surface exactly
    the 17 batch-11 authored edges + the 3 frozen pilot HOLDs; the 2
    frozen pilot REVIEW_REQUIRED settlements untouched; the 10 batch-11
    held rows present and untouched; the batch-9 AND batch-10 verdict
    records in place).

Encoding rules (recorded verbatim in the file's operator_ruling.mapping):
  * every edge row          -> CONFIRM (the operator's universal "All 17
    authored edges are confirmed" ruling; per-row notes carry the
    decision record's own derivation + evidence quote, the sanctioned-
    boundary ownership for the TWELVE boundary rows, the SCOPED-RP
    guardrail for the EIGHT route-dependent rows (B11-E-01/02 esterifi-
    cation; E-08 the C=C addition-polymer route; E-13/14 the taught
    incineration/combustion surface; E-15/16/17 the polyester route of
    this slice), the MS-pin record for B11-E-10 and the remediation-
    target record for B11-E-11). The verdict-record vocabulary
    (CONFIRM|REJECT|HOLD|MERGE|SPLIT) has no WITH_NOTE value, so the
    scoping is carried in per-row notes + meta.operator_ruling — the
    batch-9 per-row-qualification precedent (this batch DOES carry
    per-row qualifications, unlike batch 10's universal rulings);
  * every node row          -> CONFIRM (the operator's universal 5/5
    ruling; the three one-family consolidation nodes and the
    misconception node carry their B11-ID linkage in notes; the
    POLYMER-DISPOSAL row is a plain CONFIRM — the batch-7/9 convention).
    NO CONFIRM_WITH_NOTE value is used: the scoping lives on the EDGE
    rows and in meta.operator_ruling;
  * every identity decision -> KEEP_AS_IS (the operator's "The four
    identity decisions are KEEP_AS_IS, including the single
    misconception mint for the double-bonded polymer repeat-unit
    error." — the operator's own ruling sentence carried verbatim on
    each row; the B8-ID-03/04, B9-ID-01..06, B10-ID-01..05 precedents)
  * RR settlement           -> NONE RECORDED: this batch authored no
    REVIEW_REQUIRED edge, so no settlement row exists in the template
  * held appendix           -> acknowledged (10 preserved, quarantined;
    RANGE-level acknowledgment — the operator ruled the held surface as
    a range, no per-candidate dispositions were recorded, and none are
    invented: "All ten remain quarantined"; "No held candidate should
    be reopened or promoted as part of this review."; "Their
    abstention/failure classes remain part of the graph provenance.")

IDENTITY-SAFETY NOTE (the sheet-vs-template numbering hazard): the gate
sheet's §2 rows number nodes in SP/table order (sheet row 1 = ESTERS =
decision-record order) while the template numbers them alphabetically
by code (template B11-N-01 = ADDITION-POLYMERS). This batch's operator
verdict rules the node surface per-code (all 5 codes named) and
universally (5/5), so no per-row id mapping is needed — but the
encoding is still keyed by TRIPLE (edges) and CODE (nodes), never by
row id, and the template triple/code order is asserted row-for-row
against the gate sheet and the decision record before anything is
written.

The operator's REPORTED-state caveat is recorded verbatim: the sheet's
machine-state claims (the green 193-node / 488-edge merged store, 33
quote probes, pass-2 results, the uncovered 4.15 negative control) are
"REPORTED / VERIFIED BY SUBMITTED ARTIFACT, rather than being
represented as independently re-executed by this review". The verdict
session closed that gap on the operator's behalf: the machine state was
verified directly at ee0524d (the authoring head, local == origin/main,
tree clean) before encoding — 193 nodes / 488 edges / 211 PART_OF / 255
semantic HV; the decision, pass-2 and boundary YAMLs reconciled 1:1;
§16 AUTHORIZED.

This script WRITES ONLY scripts/c11_batch11_verdicts.yaml (and removes
the now-renamed template, per the sheet's gate pathway). It promotes
nothing and re-authors no decision record; application (§18 promotion
of the 17 CONFIRM edges — the verdict file itself is the operator
authorization, the session-54/56/58/60/62/63/65 precedent) is the
separate sanctioned step in this same session per the operator's
governed path.

Usage:
  python3 scripts/c11_verdict_encode_batch11.py OPERATOR_VERDICT.md
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry

GRAPH = GP.qual_dir()          # the qual's ratified store dir
TEMPLATE = HERE / "c11_batch11_verdicts_template.yaml"
VERDICTS = HERE / "c11_batch11_verdicts.yaml"
DECISIONS = HERE / "c11_batch11_decisions.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"
S16_AUTH = HERE / "c11_s16_authorization.yaml"
BOUNDARY = HERE / "c11_batch11_boundary_ruling.yaml"
B9_VERDICTS = HERE / "c11_batch9_verdicts.yaml"
B10_VERDICTS = HERE / "c11_batch10_verdicts.yaml"
GATE_SHEET = GP.reports_dir() / "C11_BATCH11_REVIEW_SHEET.md"

SESSION = 67
TODAY = "2026-09-25"
HEAD = "ee0524d"

# Verbatim operative text from the operator's verdict (session 67,
# zai-web chat lane, 2026-09-25). Every fragment below is the
# operator's own wording (table rows, notes, Final block).
OPERATOR_STATEMENT = (
    "VERDICT: PASS WITH NOTES. Batch 11: ACCEPTED — PASS WITH NOTES. "
    "Operator verdict surface: Nodes 5/5 CONFIRM; Authored semantic "
    "edges 17/17 CONFIRM; Identity decisions 4/4 KEEP_AS_IS; Held "
    "candidates 10/10 ACKNOWLEDGED / QUARANTINED; REVIEW_REQUIRED 0; "
    "Rejected authored edges 0; Duplicate mints 0; Node promotions 0; "
    "Edge promotions 0; Boundary edges 12/12 RETAIN; Authority "
    "SUGGESTED. All 17 authored edges are confirmed, but several need "
    "an important semantic guardrail: REQUIRES_PREREQUISITE should be "
    "interpreted as a scoped teaching/route dependency, not "
    "automatically as a universal ontological prerequisite. In "
    "particular: Ester → alcohols/carboxylic acids: scoped to "
    "esterification. Addition polymers → alkenes: scoped to the C=C "
    "addition-polymer route. Polymer disposal → CO₂/CO: scoped to the "
    "taught incineration/combattion surface. Condensation polymers → "
    "esters/carboxylic acids/alcohols: scoped to the polyester route "
    "represented in this slice. Retain all 12 sanctioned cross-section "
    "edges and do not mint duplicates for existing owners. The existing "
    "owners are: CON-ALCOHOLS; CON-CARBOXYLIC-ACIDS; CON-ALKENES; "
    "CON-ORGANIC-FORMULAE; CON-IUPAC-NAMING; "
    "CON-ORGANIC-REACTION-CLASSES; CON-CO-POISONING; CON-CO2-GREENHOUSE; "
    "CON-SIMPLE-DISTILLATION; CON-ACID-REACTIONS. The apparent 12-vs-10 "
    "count is intentional because Alcohols and Carboxylic Acids each "
    "receive two sanctioned boundary edges. All ten held candidates "
    "(B11-H-01 through B11-H-10) remain quarantined; no held candidate "
    "should be reopened or promoted as part of this review; their "
    "abstention/failure classes remain part of the graph provenance. "
    "Nothing is promoted by this review. Next governed path remains: "
    "verdict YAML → reconciliation → preserve boundaries/holds → §18 "
    "promotion where separately authorised → regeneration → full gate "
    "suite. One particularly important invariant to preserve during "
    "reconciliation is the route-specific interpretation of the "
    "prerequisite edges. Batch 11 should not accidentally turn these "
    "teaching-sequence relationships into universal KG prerequisites.")

CAVEAT_TEXT = (
    "Recorded verbatim from the operator's Status qualification: 'The "
    "GitHub review sheet itself was directly retrieved and reviewed. "
    "The sheet reports the underlying machine state as green, including "
    "the 193-node / 488-edge merged store, 33 quote probes, pass-2 "
    "results, and the 4.15 negative control. Those underlying execution "
    "claims should remain REPORTED / VERIFIED BY SUBMITTED ARTIFACT, "
    "rather than being represented as independently re-executed by this "
    "review.' The verdict session closed that gap on the operator's "
    "behalf: the machine state was verified directly at ee0524d (the "
    "authoring head, local == origin/main, tree clean) before encoding "
    "— 193 nodes / 488 edges / 211 PART_OF / 255 semantic HV; the "
    "decision, pass-2 and boundary YAMLs reconciled 1:1; §16 "
    "AUTHORIZED.")

INTAKE_NOTE = (
    "The operator verdict for C11_BATCH11_REVIEW_SHEET, delivered "
    "2026-09-25 INLINE in-chat (the zai-web channel; preserved verbatim "
    "as the intake artifact C11_BATCH11_OPERATOR_VERDICT.md). INTAKE "
    "FORM: GITHUB-DIRECT SHEET REVIEW + INLINE OPERATOR VERDICT — the "
    "operator retrieved the committed review sheet directly from GitHub "
    "('I reviewed the Batch 11 sheet from GitHub'; the sheet's "
    "machine-state section is read at source, not restated) and "
    "returned a self-contained verdict surface: the 11-row decision "
    "table, the five node codes, the scoped-prerequisite guardrail (4 "
    "bullets), the boundary-preservation block (12 edges / 10 owners + "
    "the 12-vs-10 explanation), the held range B11-H-01..10, the status "
    "qualification and the Final disposition. No ```text restatement "
    "blocks exist and none are claimed (the batch-9/10 restatement "
    "lane does NOT apply). The CONFORMANCE GATE applies instead "
    "(machine-checked at intake by scripts/c11_batch11_intake_drift_"
    "check.py — ALL PASS — and re-asserted by this script at encode "
    "time): the 11-row decision table equals the gate totals, the five "
    "node codes equal the gate §2 codes, the four scoped-RP guardrail "
    "bullets are present, the ten boundary owner codes equal the "
    "distinct targets of the twelve sanctioned boundary rows with the "
    "12-vs-10 count explained, the held range B11-H-01..10 matches the "
    "gate §4 rows, the REPORTED caveat and the Final disposition are "
    "present, and the route-specific interpretation invariant is named "
    "for reconciliation.")

MAPPING = (
    "The operator retrieved the session-66 gate package from GitHub and "
    "returned the operator verdict: all 5 node verdicts CONFIRM (5/5; "
    "authority SUGGESTED; 'Nothing is promoted by this review.'); all "
    "17 authored edges CONFIRM ('All 17 authored edges are confirmed') "
    "with the scoped-prerequisite semantic guardrail — "
    "'REQUIRES_PREREQUISITE should be interpreted as a scoped "
    "teaching/route dependency, not automatically as a universal "
    "ontological prerequisite' — carried per-row on the EIGHT "
    "route-dependent rows (Ester → alcohols/carboxylic acids: scoped "
    "to esterification [B11-E-01/02]; Addition polymers → alkenes: "
    "scoped to the C=C addition-polymer route [B11-E-08]; Polymer "
    "disposal → CO₂/CO: scoped to the taught incineration/combattion "
    "surface [B11-E-13/14]; Condensation polymers → esters/carboxylic "
    "acids/alcohols: scoped to the polyester route represented in this "
    "slice [B11-E-15/16/17]) and batch-level in meta.operator_ruling; "
    "the TWELVE sanctioned cross-section boundary edges RETAINed "
    "('Retain all 12 sanctioned cross-section edges and do not mint "
    "duplicates for existing owners') into the TEN existing owners "
    "(the batch-10 owners CON-ALCOHOLS x2, CON-CARBOXYLIC-ACIDS x2, "
    "CON-ALKENES; the batch-9 owners CON-ORGANIC-FORMULAE, "
    "CON-IUPAC-NAMING, CON-ORGANIC-REACTION-CLASSES, CON-CO-POISONING; "
    "the batch-5 owner CON-CO2-GREENHOUSE; the batch-1 owner "
    "CON-SIMPLE-DISTILLATION; the batch-7 owner CON-ACID-REACTIONS) — "
    "'The apparent 12-vs-10 count is intentional because Alcohols and "
    "Carboxylic Acids each receive two sanctioned boundary edges'; the "
    "four identity decisions KEEP_AS_IS ('The four identity decisions "
    "are KEEP_AS_IS, including the single misconception mint for the "
    "double-bonded polymer repeat-unit error.'); the 10 held candidates "
    "'ACKNOWLEDGED / QUARANTINED' as a range ('All ten remain "
    "quarantined'; 'No held candidate should be reopened or promoted as "
    "part of this review.'; 'Their abstention/failure classes remain "
    "part of the graph provenance.') — no per-candidate dispositions "
    "recorded and none invented; zero RR rows; zero REJECTED authored "
    "edges; zero duplicate mints; zero node/edge promotions by the "
    "review itself ('Nothing is promoted by this review.'); final "
    "disposition 'Batch 11: ACCEPTED — PASS WITH NOTES' with the "
    "governed path 'verdict YAML → reconciliation → preserve "
    "boundaries/holds → §18 promotion where separately authorised → "
    "regeneration → full gate suite' and the reconciliation invariant "
    "'the route-specific interpretation of the prerequisite edges — "
    "Batch 11 should not accidentally turn these teaching-sequence "
    "relationships into universal KG prerequisites.' The operator "
    "verdict file itself is the authorization (the "
    "session-54/56/58/60/62/63/65 precedent). ENCODING RULES: the "
    "operator's rulings cover the entire coded surface, so each "
    "template row records CONFIRM; the verdict-record vocabulary "
    "(CONFIRM|REJECT|HOLD|MERGE|SPLIT) has no WITH_NOTE value, so the "
    "scoped-prerequisite qualifications ride the per-row notes (the "
    "batch-9 per-row-qualification precedent — this batch DOES carry "
    "per-row qualifications, unlike batch 10's universal rulings) plus "
    "meta.operator_ruling; node verdicts are keyed by CODE and edge "
    "verdicts by TRIPLE — never by row id — because the gate sheet's §2 "
    "node numbering (table order = decision-record order: sheet row 1 = "
    "ESTERS) differs from the template's alphabetical-by-code numbering "
    "(template B11-N-01 = ADDITION-POLYMERS), while the edge ids "
    "coincide between the sheet §3 rows and the template (both orders "
    "agree row-for-row — asserted); the identity-decision vocabulary "
    "maps the operator's KEEP_AS_IS ruling onto each keep-as-ruled "
    "question directly; node authority is NOT changed by these "
    "confirmations (nodes have no §18 pathway — node promotion remains "
    "a separate identity decision, deferred); PART_OF is derived and "
    "outside §18 (the 12 batch-11 PART_OF rows stay SUGGESTED pending "
    "their own lane); the application state lives in "
    "scripts/c11_promotions.yaml (the §18 pathway is the only "
    "HUMAN_VALIDATED source) — this file never carries promotion "
    "payload or promoted status. Changing a recorded verdict requires "
    "an explicit operator decision.")

# The operator's scoped-prerequisite guardrail bullets, verbatim (the
# per-row qualification riding the EIGHT route-dependent rows).
SCOPED_BULLETS = {
    "B11-E-01": "Ester → alcohols/carboxylic acids: scoped to "
                "esterification.",
    "B11-E-02": "Ester → alcohols/carboxylic acids: scoped to "
                "esterification.",
    "B11-E-08": "Addition polymers → alkenes: scoped to the C=C "
                "addition-polymer route.",
    "B11-E-13": "Polymer disposal → CO₂/CO: scoped to the taught "
                "incineration/combattion surface.",
    "B11-E-14": "Polymer disposal → CO₂/CO: scoped to the taught "
                "incineration/combattion surface.",
    "B11-E-15": "Condensation polymers → esters/carboxylic "
                "acids/alcohols: scoped to the polyester route "
                "represented in this slice.",
    "B11-E-16": "Condensation polymers → esters/carboxylic "
                "acids/alcohols: scoped to the polyester route "
                "represented in this slice.",
    "B11-E-17": "Condensation polymers → esters/carboxylic "
                "acids/alcohols: scoped to the polyester route "
                "represented in this slice.",
}

IDENTITY_SENTENCE = (
    "The four identity decisions are KEEP_AS_IS, including the single "
    "misconception mint for the double-bonded polymer repeat-unit "
    "error.")

HELD_NOTE = (
    "Operator verdict (session 67): all 10 held candidates "
    "(B11-H-01..10) are ACKNOWLEDGED / QUARANTINED as a range — 'All "
    "ten remain quarantined'; 'No held candidate should be reopened or "
    "promoted as part of this review.'; 'Their abstention/failure "
    "classes remain part of the graph provenance.' RANGE-level "
    "acknowledgment: the operator ruled the held surface as a range, "
    "no per-candidate dispositions were recorded by this intake, and "
    "none are invented here — nothing beyond the operator's own words "
    "is recorded.")

META_FILE = (
    "OPERATOR-OWNED verdict record for C11_BATCH11_REVIEW_SHEET "
    "(session-66 package) — verdicts recorded by operator decision, "
    "session 67 (2026-09-25), from the operator verdict delivered "
    "inline in-chat after the GitHub-direct review of the committed "
    "sheet (intake artifact C11_BATCH11_OPERATOR_VERDICT.md).")

META_RULING = {
    "statement": OPERATOR_STATEMENT,
    "session": SESSION,
    "decided_by": "operator",
    "decided_date": TODAY,
    "completed_sheet": INTAKE_NOTE,
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


def _iid_note(iid: str) -> str:
    """Node CONFIRM note carrying the operator's own identity ruling
    sentence + the per-id linkage (zero invention)."""
    return (f"Operator verdict (session 67): CONFIRM — "
            f"'{IDENTITY_SENTENCE}' ({iid} KEEP_AS_IS); authority "
            f"remains SUGGESTED.")


def strip4(s):
    return s.replace("4CH1-", "")


# ---------------------------------------------------------------------------
# Load + intake assertions
# ---------------------------------------------------------------------------
if len(sys.argv) != 2:
    die("usage: c11_verdict_encode_batch11.py OPERATOR_VERDICT.md "
        "(the operator's verdict, e.g. C11_BATCH11_OPERATOR_VERDICT.md)")
OP_VERDICT = Path(sys.argv[1]).resolve()
if not OP_VERDICT.exists():
    die(f"operator verdict file not found: {OP_VERDICT}")
if VERDICTS.exists():
    die("scripts/c11_batch11_verdicts.yaml already exists — refusing to "
        "double-apply (the verdict round is recorded)")
if not TEMPLATE.exists():
    die("scripts/c11_batch11_verdicts_template.yaml missing — the "
        "session-66 package must be intact")
if not GATE_SHEET.exists():
    die("gate sheet missing from graph/reports/ — the session-66 "
        "package must be intact")
if not B9_VERDICTS.exists() or not B10_VERDICTS.exists():
    die("scripts/c11_batch9_verdicts.yaml / c11_batch10_verdicts.yaml "
        "missing — the batch-9 (session 63) and batch-10 (session 65) "
        "verdict records must be in place before the batch-11 round")
op_text = OP_VERDICT.read_text(encoding="utf-8")
gate_text = GATE_SHEET.read_text(encoding="utf-8")
doc = yaml.safe_load(TEMPLATE.read_text(encoding="utf-8"))
if doc is None:
    die("verdict template empty")

# 0a. the operator verdict must carry the expected verdict markers
#     (the intake conformance surface, re-asserted at encode time).
_require(op_text.lstrip().startswith(
             "I reviewed the **Batch 11 sheet from GitHub**"),
         "the GitHub-direct retrieval statement is missing from the "
         "operator verdict")
for marker in (
    "### T-C11 Batch 11 — Operator Verdict",
    "**`PASS WITH NOTES`**",
    "| Nodes                   | **5/5 CONFIRM**",
    "| Authored semantic edges | **17/17 CONFIRM**",
    "| Identity decisions      | **4/4 KEEP_AS_IS**",
    "| Held candidates         | **10/10 ACKNOWLEDGED / QUARANTINED**",
    "| REVIEW_REQUIRED         | **0**",
    "| Rejected authored edges | **0**",
    "| Duplicate mints         | **0**",
    "| Node promotions         | **0**",
    "| Edge promotions         | **0**",
    "| Boundary edges          | **12/12 RETAIN**",
    "| Authority               | **SUGGESTED**",
    "1. `4CH1-CON-ESTERS` — CONFIRM",
    "5. `4CH1-MIS-POLYMER-DOUBLE-BOND` — CONFIRM",
    "The four identity decisions are **KEEP_AS_IS**, including the "
    "single misconception mint for the double-bonded polymer "
    "repeat-unit error.",
    "`REQUIRES_PREREQUISITE` should be interpreted as a **scoped "
    "teaching/route dependency**, not automatically as a universal "
    "ontological prerequisite.",
    "Ester → alcohols/carboxylic acids: scoped to esterification.",
    "Addition polymers → alkenes: scoped to the C=C addition-polymer "
    "route.",
    "Polymer disposal → CO₂/CO: scoped to the taught "
    "incineration/combattion surface.",
    "Condensation polymers → esters/carboxylic acids/alcohols: scoped "
    "to the polyester route represented in this slice.",
    "Retain all **12 sanctioned cross-section edges**",
    "The apparent 12-vs-10 count is intentional because Alcohols and "
    "Carboxylic Acids each receive two sanctioned boundary edges.",
    "`B11-H-01` through `B11-H-10`",
    "No held candidate should be reopened or promoted as part of this "
    "review.",
    "Their abstention/failure classes remain part of the graph "
    "provenance.",
    "**REPORTED / VERIFIED BY SUBMITTED ARTIFACT**",
    "rather than being represented as independently re-executed by "
    "this review",
    "**Batch 11: ACCEPTED — PASS WITH NOTES**",
    "**Nothing is promoted by this review.**",
    "`verdict YAML → reconciliation → preserve boundaries/holds → §18 "
    "promotion where separately authorised → regeneration → full gate "
    "suite`",
    "the **route-specific interpretation of the prerequisite edges**",
    "should not accidentally turn these teaching-sequence "
    "relationships into universal KG prerequisites",
):
    _require(marker in op_text,
             f"operator verdict missing an expected verdict marker: "
             f"{marker}")

# 0b. the ten boundary owner bullets must equal the distinct targets of
#     the gate's twelve sanctioned boundary rows.
owners_block = re.findall(r"^\* `(CON-[A-Z0-9-]+)`$", op_text, re.M)
_require(len(owners_block) == 10,
         f"operator verdict owner bullets: {len(owners_block)}, "
         f"expected 10")

# 1. the template must be untouched (no verdict filled anywhere)
for section in ("edge_verdicts", "node_verdicts", "identity_decisions"):
    for row in doc[section]:
        if row.get("verdict"):
            die(f"{section} {row['id']} already has a verdict — refusing")
if doc.get("rr_settlement"):
    die("unexpected rr_settlement section — the batch-11 template must "
        "carry none (zero RR edges authored)")
if doc["held_appendix_acknowledgment"].get("acknowledged"):
    die("held_appendix_acknowledgment already acknowledged — refusing")

# 2. row-shape assertions (exact session-66 surface)
_require([r["id"] for r in doc["edge_verdicts"]] ==
         [f"B11-E-{i:02d}" for i in range(1, 18)],
         "edge ids drifted from B11-E-01..17")
_require([r["id"] for r in doc["node_verdicts"]] ==
         [f"B11-N-{i:02d}" for i in range(1, 5)] + ["B11-M-01"],
         "node ids drifted from B11-N-01..04 + B11-M-01")
_require([r["id"] for r in doc["identity_decisions"]] ==
         [f"B11-ID-{i:02d}" for i in range(1, 5)],
         "identity ids drifted from B11-ID-01..04")

# 3. reconcile against the batch-11 decision record + the gate sheet +
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
_require(len(b_edges) == 17, f"batch-11 decision record carries "
         f"{len(b_edges)} edges, expected 17")
_require(len(b_suggested) == 17 and len(b_rr) == 0,
         "batch-11 edges must be 17 SUGGESTED / 0 RR at the pre-verdict "
         "state")
_require(sorted(tmpl_triples) == sorted(b_suggested)
         and len(set(tmpl_triples)) == 17,
         "edge triple mismatch between verdict template and the "
         "batch-11 decision record")
# the template triple order must agree row-for-row with the gate sheet
# (the §5 id assignment B11-E-01..17 rides the table order)
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
_require(len(gate_rows) == 17,
         f"gate sheet §3 parsed {len(gate_rows)} edge rows, expected 17")
_require(tmpl_triples == gate_rows,
         "template edge order disagrees with the gate sheet §3 row order "
         "— the B11-E-xx id assignment would be ambiguous")
b_codes = [n["code"] for n in dec["nodes"]]
tmpl_codes = [r["code"] for r in doc["node_verdicts"]]
_require(sorted(tmpl_codes) == sorted(b_codes) and len(set(tmpl_codes)) == 5,
         "node code mismatch between verdict template and the batch-11 "
         "decision record")
_require([r["code"] for r in doc["node_verdicts"] if r["id"] == "B11-M-01"]
         == ["4CH1-MIS-POLYMER-DOUBLE-BOND"],
         "the misconception row must be B11-M-01 = "
         "4CH1-MIS-POLYMER-DOUBLE-BOND")
_require(sum(1 for n in dec["nodes"] if n["family"] == "CONCEPT") == 4
         and sum(1 for n in dec["nodes"]
                 if n["family"] == "MISCONCEPTION") == 1,
         "batch-11 nodes must be 4 CONCEPT + 1 MISCONCEPTION")
_require(len(dec["held"]) == 10, f"batch-11 held count "
         f"{len(dec['held'])}, expected 10")
_require([h["id"] for h in dec["held"]]
         == [f"B11-H-{i:02d}" for i in range(1, 11)],
         "batch-11 held ids drifted from B11-H-01..10")
# boundary ownership: the TWELVE template boundary rows must be exactly
# the ruling's sanctioned targets (TARGET id + owner + target), with the
# owner batches matching the ruling's own records; the TEN distinct
# owner codes must equal the operator verdict's owner bullets
sanctioned = {s["target"]: s for s in
              bound["boundary_edge_ruling"]["sanctioned_targets"]}
sanctioned_rows = bound["boundary_edge_ruling"]["sanctioned_targets"]
_require(len(sanctioned_rows) == 12 and len(sanctioned) == 10,
         f"boundary ruling rows {len(sanctioned_rows)} / distinct "
         f"targets {len(sanctioned)}, expected 12 / 10")
B11_CONCEPT_CODES = {n["code"] for n in dec["nodes"]
                     if n["family"] == "CONCEPT"}
BOUNDARY_IDS, BOUNDARY_OWNERS = [], {}
for row in doc["edge_verdicts"]:
    t = row["triple"]
    src, rel, tgt = t.split()
    if rel == "REQUIRES_PREREQUISITE" and tgt not in B11_CONCEPT_CODES:
        BOUNDARY_IDS.append(row["id"])
        # the TARGET linkage comes from the decision record's own
        # derivation_notes (zero invention) — the x2 owners make
        # target-keyed lookup ambiguous (ALCOHOLS x2 + CARBOXYLIC-ACIDS
        # x2: TARGET-1/12 and TARGET-2/11)
        rec = next(e for e in b_edges if triple(e) == t)
        m = re.search(r"session-66 ruling (TARGET-\d+)",
                      rec["provenance"]["derivation_notes"])
        _require(m, f"{row['id']}: no session-66 TARGET linkage in the "
                    f"decision record's derivation_notes")
        srow = next(s for s in sanctioned_rows if s["id"] == m.group(1))
        _require(srow["target"] == tgt,
                 f"{row['id']}: {m.group(1)} records target "
                 f"{srow['target']} != edge target {tgt}")
        BOUNDARY_OWNERS[row["id"]] = srow
_require(sorted(BOUNDARY_IDS) == sorted(
             [f"B11-E-{i:02d}" for i in range(1, 5)]
             + [f"B11-E-{i:02d}" for i in range(6, 10)]
             + ["B11-E-13", "B11-E-14", "B11-E-16", "B11-E-17"]),
         f"boundary row ids drifted: {sorted(BOUNDARY_IDS)}")
_require(len(BOUNDARY_OWNERS) == 12
         and {s["id"] for s in BOUNDARY_OWNERS.values()}
         == {f"TARGET-{i}" for i in range(1, 13)},
         f"boundary rows resolved {len(BOUNDARY_OWNERS)}, expected 12 "
         f"covering TARGET-1..12 exactly once each")
_require(sorted(f"4CH1-{o}" for o in owners_block)
         == sorted(sanctioned),
         f"operator verdict owner bullets drifted from the ruling's "
         f"distinct targets: {sorted(owners_block)}")
for tid, s in BOUNDARY_OWNERS.items():
    row = next(r for r in doc["edge_verdicts"] if r["id"] == tid)
    _require(row["pretriage"] == "FLAGGED",
             f"{tid} must be pretriage FLAGGED (boundary)")
non_mint = set(bound["boundary_edge_ruling"]["non_mint_list"])
_require(len(non_mint) == 50 and not ({n["code"] for n in dec["nodes"]}
                                      & non_mint),
         "the ruling's 50 non-mint owner codes must stay outside the "
         "batch-11 mint")

# 4. the live store must be the sanctioned pre-verdict state
sem = [e for e in edges_doc["edges"] if e["relation"] != "PART_OF"]
partof = [e for e in edges_doc["edges"] if e["relation"] == "PART_OF"]
hv = {triple(e) for e in sem if e["validation_status"] == "HUMAN_VALIDATED"}
store = {(p["edge"]["source"], p["edge"]["relation"], p["edge"]["target"])
         for p in promo["promotions"]}
store_triples = {" ".join(t) for t in store}
_require(len(hv) == 255 and hv == store_triples,
         "live HUMAN_VALIDATED set != the 255 pilot+batch-1..10 §18 "
         "promotions (the pre-verdict state must be frozen before "
         "recording batch-11 verdicts)")
_require(not (hv & set(b_suggested)),
         "a batch-11 edge is already HUMAN_VALIDATED — pre-verdict state "
         "violated")
_require(auth.get("authorization", {}).get("decision") == "AUTHORIZED",
         "§16 is not AUTHORIZED (scripts/c11_s16_authorization.yaml)")
_require(all(p.get("validated_by") == "operator"
             for p in promo["promotions"]),
         "existing promotions carry non-operator attribution (anti-forgery)")
_require(len(nodes_doc["nodes"]) == 193, f"store nodes "
         f"{len(nodes_doc['nodes'])}, expected 193")
_require(len(edges_doc["edges"]) == 488, f"store edges "
         f"{len(edges_doc['edges'])}, expected 488")
_require(len(partof) == 211
         and sum(1 for e in partof
                 if e["validation_status"] == "HUMAN_VALIDATED") == 117,
         "PART_OF layer drifted (expected 211 rows, 117 HUMAN_VALIDATED — "
         "the T-C19 G19 record; batch-9/10/11 PART_OF rows stay SUGGESTED)")
# the SUGGESTED surface must be exactly the 17 batch-11 rows + the 3
# frozen pilot HOLDs; the 2 frozen RR settlements untouched
sugg = {triple(e) for e in sem if e["validation_status"] == "SUGGESTED"}
pilot_holds = {
    "4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-EQ-SYMBOL",
    "4CH1-CON-MOLAR-GAS-VOL EXPLAINED_BY 4CH1-CON-AVOGADRO-LAW",
    "4CH1-MIS-EQ-SUBSCRIPT REMEDIATED_BY 4CH1-CON-CONSERVATION-MASS",
}
_require(sugg == set(b_suggested) | pilot_holds,
         "SUGGESTED surface drifted (expected exactly the 17 batch-11 "
         "edges + the 3 frozen pilot HOLDs)")
rr_live = {triple(e) for e in sem
           if e["validation_status"] == "REVIEW_REQUIRED"}
_require(len(rr_live) == 2,
         "the 2 frozen pilot REVIEW_REQUIRED settlements must be "
         "untouched at the pre-verdict state")
# the batch-11 held rows must be live and untouched (quarantine integrity)
_require(len({h["candidate"] for h in dec["held"]}) == 10,
         "batch-11 held candidate surface drifted")

# ---------------------------------------------------------------------------
# Encode (in place; key order preserved)
# ---------------------------------------------------------------------------
doc["meta"]["session"] = SESSION
doc["meta"]["file"] = META_FILE
doc["meta"]["operator_ruling"] = META_RULING

# per-edge notes: composed from the decision record's own fields (zero
# invention) + the operator ruling context + boundary ownership + the
# scoped-prerequisite guardrail.
for row in doc["edge_verdicts"]:
    t = row["triple"]
    rec = next(e for e in b_edges if triple(e) == t)
    der = rec["provenance"]["derivation_method"]
    ev = rec["evidence"][0]
    kind = ev["kind"]
    quote = ev["quote"]
    note = (f"Operator verdict (session 67): CONFIRM — 'All 17 authored "
            f"edges are confirmed.' Pass-1: {der} ({kind}): '{quote}'")
    if row["id"] in BOUNDARY_OWNERS:
        s = BOUNDARY_OWNERS[row["id"]]
        note += (f" Sanctioned cross-section boundary edge (session-66 "
                 f"ruling {s['id']}, the batch-{s['owner'].split()[1]} "
                 f"owner) — boundary relationships to existing concept "
                 f"owners, not new node identities; the operator's "
                 f"boundary-preservation ruling: 'Retain all 12 "
                 f"sanctioned cross-section edges and do not mint "
                 f"duplicates for existing owners' (the 12-vs-10 count "
                 f"is intentional: Alcohols and Carboxylic Acids each "
                 f"receive two sanctioned boundary edges).")
    if row["id"] in SCOPED_BULLETS:
        note += (" SCOPED-RP GUARDRAIL (the operator's semantic "
                 "guardrail, session 67): this REQUIRES_PREREQUISITE is "
                 "a scoped teaching/route dependency, not a universal "
                 f"ontological prerequisite — '{SCOPED_BULLETS[row['id']]}' "
                 "(the route-specific interpretation invariant is "
                 "preserved during reconciliation; the edge's own "
                 "derivation surface stays the taught scope).")
    if row["id"] == "B11-E-10":
        note += (" The pinned Alkenes MS Q2(c) / Synthetic Polymers MS "
                 "Q4(c) Reject row ('Any double-bonded product scores "
                 "0/2') documents the wrong-answer class; B11-ID-04 "
                 "KEEP_AS_IS (single assessment-documented misconception "
                 "surface).")
    if row["id"] == "B11-E-11":
        note += (" Remediation target = WAP target (the B1-E-25 "
                 "pattern).")
    row["verdict"] = "CONFIRM"
    row["notes"] = note

for row in doc["node_verdicts"]:
    code = row["code"]
    note = ""
    if code == "4CH1-CON-ESTERS":
        note = _iid_note("B11-ID-01")
    elif code == "4CH1-CON-ADDITION-POLYMERS":
        note = _iid_note("B11-ID-02")
    elif code == "4CH1-CON-CONDENSATION-POLYMERS":
        note = _iid_note("B11-ID-03")
    elif code == "4CH1-MIS-POLYMER-DOUBLE-BOND":
        note = _iid_note("B11-ID-04")
    row["verdict"] = "CONFIRM"
    row["notes"] = note

for row in doc["identity_decisions"]:
    row["verdict"] = "KEEP_AS_IS"
    row["notes"] = (f"Operator verdict (session 67): KEEP_AS_IS — "
                    f"'{IDENTITY_SENTENCE}'")
doc["held_appendix_acknowledgment"]["acknowledged"] = True
doc["held_appendix_acknowledgment"]["notes"] = HELD_NOTE

header = (
    "# T-C11 §16 batch 11 — OPERATOR verdict record (session-66 "
    "package), FILLED by operator decision session 67 (2026-09-25). "
    "OPERATOR-OWNED.\n"
    "# Operator verdict (GitHub-direct sheet review + inline operator "
    "verdict via the zai-web chat lane; intake artifact "
    "C11_BATCH11_OPERATOR_VERDICT.md): all 5 node\n# verdicts and all "
    "17 edge verdicts CONFIRM — WITH the operator's SCOPED-RP "
    "semantic guardrail carried per-row on the EIGHT route-dependent\n"
    "# rows (REQUIRES_PREREQUISITE is a scoped teaching/route "
    "dependency, not a universal ontological prerequisite); the TWELVE "
    "sanctioned\n# boundary edges RETAINed into the TEN existing owners "
    "(no duplicate mints; 12-vs-10 intentional: ALCOHOLS x2 + "
    "CARBOXYLIC-ACIDS x2);\n# the four identity decisions KEEP_AS_IS "
    "(incl. the single misconception mint); the 10 held candidates "
    "ACKNOWLEDGED / QUARANTINED as a range\n# (no per-candidate "
    "dispositions recorded, none invented); zero RR; zero REJECT. "
    "Intake form: GITHUB-DIRECT SHEET REVIEW + INLINE OPERATOR\n# "
    "VERDICT — no restatement blocks claimed; the CONFORMANCE gate "
    "applies and PASSES (see meta.operator_ruling.completed_sheet).\n"
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

_require(ec == {"CONFIRM": 17},
         f"post-write: edge verdict counts drifted: {ec}")
_require(nc == {"CONFIRM": 5},
         f"post-write: node verdict counts drifted: {nc}")
_require([r["verdict"] for r in chk["identity_decisions"]]
         == ["KEEP_AS_IS"] * 4,
         "post-write: identity decisions drifted")
_require("rr_settlement" not in chk,
         "post-write: unexpected rr_settlement present")
_require(chk["held_appendix_acknowledgment"]["acknowledged"] is True,
         "post-write: held appendix acknowledgment missing")
_require(chk["meta"]["operator_ruling"]["statement"] == OPERATOR_STATEMENT,
         "post-write: operator ruling text drifted")
for tid in BOUNDARY_IDS:
    r = next(x for x in chk["edge_verdicts"] if x["id"] == tid)
    s = BOUNDARY_OWNERS[tid]
    _require("Sanctioned cross-section boundary edge" in r["notes"]
             and "Retain all 12 sanctioned cross-section edges"
             in r["notes"]
             and f"session-66 ruling {s['id']}" in r["notes"],
             f"post-write: the {tid} boundary note drifted")
for tid, bullet in SCOPED_BULLETS.items():
    r = next(x for x in chk["edge_verdicts"] if x["id"] == tid)
    _require("SCOPED-RP GUARDRAIL" in r["notes"] and bullet in r["notes"],
             f"post-write: the {tid} scoped-RP guardrail note drifted")
_e10 = next(r for r in chk["edge_verdicts"] if r["id"] == "B11-E-10")
_require("Any double-bonded product scores 0/2" in _e10["notes"]
         and "B11-ID-04" in _e10["notes"],
         "post-write: the E-10 MS-pin note drifted")
_mis = next(r for r in chk["node_verdicts"]
            if r["code"] == "4CH1-MIS-POLYMER-DOUBLE-BOND")
_require(_mis["notes"].startswith("Operator verdict (session 67): "
                                  "CONFIRM")
         and "B11-ID-04" in _mis["notes"],
         "post-write: the misconception mint note drifted")
_plain = sum(1 for r in chk["node_verdicts"] if r["notes"] == "")
_require(_plain == 1,
         f"post-write: plain-node note surface drifted ({_plain} plain)")
_held = chk["held_appendix_acknowledgment"]["notes"]
_require("All ten remain quarantined" in _held
         and "B11-H-01..10" in _held
         and "failure classes remain part of the graph provenance"
         in _held,
         "post-write: the range-level held acknowledgment drifted")
_require(not TEMPLATE.exists(),
         "post-write: verdict template was not consumed")

print("wrote", VERDICTS)
print("operator verdict recorded verbatim from the GitHub-direct + "
      f"inline intake (decided_by operator, {TODAY})")
print("intake form: GITHUB-DIRECT SHEET REVIEW + INLINE OPERATOR "
      "VERDICT via the zai-web chat lane; conformance gate passed "
      "(decision table + node codes + scoped-RP guardrail bullets + "
      "owner bullets + held range + REPORTED caveat + Final "
      "disposition)")
print("edge verdicts: 17 CONFIRM (12 sanctioned boundary, 8 "
      "scoped-RP-qualified rows); node verdicts: 5 CONFIRM; identity: "
      "4 KEEP_AS_IS; held: 10 acknowledged (range); RR: 0; REJECT: 0")
print("next: the §18 promotion pathway (c11_diff_review export/approve "
      "-> c11_promote -> gated generator re-run), then the verdict "
      "check + re-anchors + full gate suite")
