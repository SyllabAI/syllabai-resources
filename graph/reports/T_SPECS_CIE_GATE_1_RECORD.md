# T-SPECS-CIE-GATE-1 — review/promotion gate record

- Date: 2026-10-19 (Asia/Dhaka; session zai-web `web-64d10b73-…`, gateway trace `1a150fee04d54d6d`)
- Operator directive: *"review/promotion gate proceed"* — fires NEXT lane #1 of the
  T-SPECS-CIE-JOIN-1 record ("the review/promotion gate — accept or reject the SUGGESTED
  sidecars (AGENT.md rule 2)").
- Base commit: `981bb271` (T-SPECS-CIE-JOIN-1, on origin/main).
- Gate scripts: `scripts/cie_gate_verify.py` (independent verification),
  `scripts/cie_gate_apply.py` (disposition), `scripts/cie_gate_check.py` (K battery).

## Disposition

**PROMOTED — all 44 `spec-links/cie-*.json` sidecars SUGGESTED → ACCEPTED.**

- `review_state` per sidecar now carries: state ACCEPTED, gate T-SPECS-CIE-GATE-1,
  accepted_utc, accepted_by = the operator directive + gateway trace, tier_policy, note.
- `spec-links/manifest.json` gains the `cie_gate` block (same metadata + verification totals).
- `spec-links/README.md` CIE section updated to the gate outcome.
- **The links themselves moved ZERO**: items/codes/pending/totals/anchors are deep-equal to the
  pre-gate HEAD blobs (K2) and the tier/method distribution is identical (K6). Unresolved anchors
  stay `pending` (AGENT.md rule 3 continues to hold post-gate).

## Tier policy (recorded, per AGENT.md rule 1)

| tier | post-gate status |
|------|------------------|
| `T1_verbatim` | **authoritative** — normalized text identity, independently re-verified 3,547/3,547 |
| `T2_near` | **accepted-near; non-authoritative hint** — conservative overlap joins, lower-bound audited 584/584 |
| pending | unresolved — quarantined for the operator-verdict fill lane |

## Verification rounds (the gate's own work)

- **V1 — join battery**: `cie_join_check.py` J1–J10 **12/12 PASS** at gate time (re-run post-gate
  as K3 with the evolved battery).
- **V2 — independent T1 re-verification** (fresh implementation, shares the normalization SPEC not
  the join's code; 7-probe equivalence self-test): every `T1_verbatim` link re-derived from SOURCE
  blobs — the item's spcpt anchors must carry a definition line equal (or ≥8-token containment)
  to the official point text against either official pool (bare / +sub_items).
  **Result: 3,547/3,547 verified, zero failures.**
- **V3 — T2 lower-bound audit**: every `T2_near` link must satisfy, on a SINGLE anchor, one of:
  jaccard ≥ 0.55 against either official pool; the name-weak rule (name == point-text tokens ∧
  some line jaccard ≥ 0.35); or the head rule (name == subsection title).
  **Result: 584/584 verified.**
- **V4 — stratified evidence**: 58 SME↔official sample pairs (family × tier) written to
  `T_SPECS_CIE_GATE_1_VERIFY.json` for operator inspection.

### Verifier evolution caught by the gate itself (recorded honestly)

The 11 initial V3 flags were ALL verifier coverage gaps, not join bugs, and drove the audit to its
final form: (1) the lower bound omitted the join's name-weak rule (name == point-text tokens,
e.g. "Definition of Opportunity Cost" == 0455 `1.3.1` "definition of opportunity cost"); (2) the
verifier collapsed an item's multiple anchors into one `name_tk`, but the join evaluated the
name/head rules PER spcpt record (e.g. 9701 `3.7.1` via the second anchor "Dot & Cross Diagrams"
== subsection title "Dot-and-cross diagrams"). After both fixes: **zero defects, verdict PASS.**
Also fixed en route: `norm_v` unicode-punctuation divergence (caught by the self-test),
a null-`subsection` crash (front-matter points), and a loop-nesting bug (tokens vs lines).

## Join-battery evolution (documented, part of this gate)

- **J1** now accepts state ∈ {SUGGESTED (pre-gate), ACCEPTED (post-gate, gate lane recorded)}.
- **J9** footprint guard widened: gate files declared; post-gate sidecar modifications declared.
- **J10** reproducibility now compares the join **payload modulo `review_state`** (the gate's only
  legal change) instead of raw bytes.
- **Incident on the record**: J10's rerun REGENERATED its first sample sidecar from the join script
  (SUGGESTED state), de-promoting `cie-igcse-chemistry-23` in the working tree mid-gate-check and
  failing K1 — caught immediately, root-caused, and resolved structurally: the K battery now
  re-applies the gate after the J battery (idempotent) and **K7 pins the final working-tree state
  44/44 ACCEPTED** before commit.

## Gate check battery

`scripts/cie_gate_check.py` **K1–K7: 7/7 PASS** (`graph/reports/T_SPECS_CIE_GATE_1_CHECK.json`):

| id | check |
|----|-------|
| K1 | 44/44 ACCEPTED with gate provenance (gate id + operator trace + tier_policy) |
| K2 | items/codes/pending deep-equal vs pre-gate HEAD — zero links moved |
| K3 | join battery J1–J10 12/12 post-gate (with the de-promotion re-apply cycle) |
| K4 | manifest `cie_gate` block consistent; pre-existing rows value-identical vs HEAD |
| K5 | footprint guard (gate-declared paths only) |
| K6 | tier/method distribution identical vs pre-gate HEAD |
| K7 | final working-tree state 44/44 ACCEPTED (commit-state guarantee) |

## Footprint

- Modified: `spec-links/cie-*.json` (44 — review_state block only), `spec-links/manifest.json`
  (cie_gate block), `spec-links/README.md` (gate note), `scripts/cie_join_check.py` (battery
  evolution J1/J9/J10).
- Added: `scripts/cie_gate_verify.py`, `scripts/cie_gate_apply.py`, `scripts/cie_gate_check.py`,
  `graph/reports/T_SPECS_CIE_GATE_1_RECORD.md`, `T_SPECS_CIE_GATE_1_VERIFY.json`,
  `T_SPECS_CIE_GATE_1_CHECK.json`.
- Byte-untouched: everything else (SME trees, Official-Specifications/**, Edexcel spec-links,
  graph/ beyond the gate records).

## NEXT (operator-gated, NOT fired by this gate)

1. **Operator-verdict fill lane** for the honest-zero lanes (maths/English/ICT/RS/accounting/…)
   — the Edexcel T-SPEC-2b/2c evolution; its verdicts land authoritative by construction.
2. **SME-native spec-point index harvest for the CIE lanes** — resolves the dangling
   EQ-referenced spcpt ids currently held pending.
3. **Learner-UI consumption** — the ACCEPTED sidecars are consumable; `T2_near` entries should be
   rendered with their non-authoritative-hint semantics.
4. R41-shaped validation re-gate — explicit instruction only; standing Render console disable lever;
   PAT rotation still CRITICAL-OVERDUE (fingerprint `a8ccee736aa8c75b`, 13 plaintext transits).
