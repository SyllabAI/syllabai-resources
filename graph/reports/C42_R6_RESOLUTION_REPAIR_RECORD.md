# T-C42 R6 — R1-Shaped Verdict Round over the R4 Defect Inventory (Resolution Repair Record)

| | |
|---|---|
| **Task** | T-C42 (K2-B rework, the scope §7 loop's second R1-shaped round — lane R6) |
| **Operator directive** | "R1-shaped verdict round over this inventory (then R2/R3/R4 re-run)" (2026-10-02, zai-web, inline) |
| **Inventory** | the R4 re-gate's defect inventory — 19 REJECT rows in `scripts/c42_r4_fresh_verdicts.yaml` (the R4 gate FAILED: Part A total 95.7% but the exact stratum 78/97 = 80.4% < 90%) |
| **Baseline** | syllabai-resources `origin/main` @ `d141c59`; resolution file blob `05a57b056874e8dd` (the R1-repaired file) |
| **Reviewer** | Super Z (GLM agent), operator-delegate under the fired R6 directive; the human operator retains final sign-off; zero promotion (the substrate stays SUGGESTED; the C41-promoted 73 edges untouched) |
| **Verification** | `scripts/c42_r6_resolution_repair_check.py` C1–C8 ALL PASS, exit 0; apply idempotent (verify-only re-run OK) |

---

## 1. What fired

The R4 re-gate (operator gate 2, `d141c59`) failed its ≥90%-per-class requirement and —
per the scope §7 loop — returned to the operator with a new defect inventory: 19 REJECT
rows over 10 notes (15 note-level / note-level-class rows + 4 section-level rows). The
scope pins the loop rule: *"the rework lane repeats R1-shaped rounds only by explicit
operator instruction; nothing self-repairs."* The operator's directive fired exactly that:
an R1-shaped verdict round (the R1 mechanics of scope §4: deterministic PROPOSAL-ONLY
proposals → operator-delegate verdicts → in-place resolution amendment with per-row
provenance → two-way audit), with R2/R3/R4 re-runs pre-announced as the follow-on lanes
(executed as R7/R8/R9).

## 2. Surfaces and dispositions

### Surface 1 — id-level (10 anchors, derived deterministically from the R4 fresh roots)

| Anchor | Note | Prior code | Disposition | New code |
|---|---|---|---|---|
| spcpt_4ZdHtGPdDjYdR6rK | Compound Measures | 4.4C | CORRECT | **4.4G** |
| spcpt_2nCMJhvvGsW7vMcV | Speed-Time Graphs | 2.8D | CORRECT | **4.4F** |
| spcpt_SYHWnwMWKxDNg9s8 | Solving Linear Equations | 2.4B | CORRECT | **2.4A** |
| spcpt_hrv7F8zpDwRXmcNg | Types of Graphs | 3.3I | CORRECT | **3.3A** |
| spcpt_zrrC3yxSp579jY7k | Finding Gradients of Tangents | 3.4C | CORRECT | **3.4A** |
| spcpt_pSX9GyS8bW7N5CH7 | Area | 4.8E | CORRECT | **4.9C** |
| spcpt_X8CSxK2dhn5rX34f | Solving Linear Inequalities | 2.8D | CORRECT | **2.8C** |
| spcpt_339DNssRW9x2NPKk | Basic Fractions | 1.2I | CORRECT | **1.2A** |
| spcpt_mVXT4jbXQPrzhHvz | Problem Solving with Volumes | 4.11C | UNRESOLVED | cleared, never forced |
| spcpt_hK2H8q4Y8NYv833v | Geometrical Proof | 5.1G | UNRESOLVED | cleared, never forced |

Key adjudications (full evidence in `scripts/c42_r6_repair_verdicts.yaml`):

- **Speed-Time Graphs → 4.4F, not 3.4E** — the R4 root named "the 3.4E/4.4F surfaces";
  3.4E demands *calculus* ("apply calculus to linear kinematics") and the note's methods
  are graphical (gradient = acceleration as rise/run, distance = area). 3.4E is recorded
  as the calculus-demanding sibling, the same reasoning shape as the R1 Distance-Time
  Graphs verdict (3.3F → 4.4F with the sibling recorded).
- **Basic Fractions → 1.2A** — the home question the R4 record deliberately left open is
  decided on the note-level evidence (ords 3–6 are the 1.2A surface; no multiply/divide
  content anywhere; that surface lives in the separately-CONFIRMed Multiplying & Dividing
  Fractions note). The R1 ord-6 override is **subsumed** by this repair.
- **Solving Linear Inequalities → 2.8C** — the note-level defect of which the operator's
  R1 ord-3 ruling was the section-level patch; that override is likewise **subsumed**.
- **Two UNRESOLVED clears** — Problem Solving with Volumes (the sibling of the R1-cleared
  Problem Solving with Areas) and Geometrical Proof (angle-fact proof apparatus; 5.1G
  demands vector methods; no 188 row teaches angle-fact proof per se). Wrong codes
  CLEARED, never forced.

### Surface 2 — residual continuity (1 row)

`spcpt_QWXhzVp2S3VYZdZc` ("Discrete & Continuous Data") re-affirmed **KEPT UNRESOLVED** —
the C32 §3 PDF-verified reason stands; unchanged from the R1 adjudication.

### Surface 3 — section-level (4 verdicted rows + 3 labeled extension rows)

| Note::ordinal | Current | Action | Target | Source |
|---|---|---|---|---|
| problem-solving-with-differentiation::3 | 3.4E | REATTRIBUTE | **3.4D** | R4 row f086a04bff035846 |
| types-of-number::9 | 1.1G | REATTRIBUTE | **1.4B** (ledger Foundation wording) | R4 row 260c61bcfeb157da |
| drawing-straight-line-graphs::2 | 3.3F | REATTRIBUTE | **3.3H** | R4 row 5e6ed91f25d0fdb4 |
| unit-conversions::1 | 4.10F | REATTRIBUTE | **4.9A** (ledger Foundation wording) | R4 row a49f8beecaf05779 |
| area::7 *(extension, R4-sampled)* | 4.9C (post-R6 join) | REATTRIBUTE | **4.9D** | R4 row c67208f06b9072e9 — its own root names the 4.9D surface |
| area::6 *(extension)* | 4.9C (post-R6 join) | REATTRIBUTE | **4.9D** | heading-verbatim trapezia + the ord-7 sibling |
| basic-fractions::2 *(extension)* | 1.2A (post-R6 join) | REATTRIBUTE | **1.2D** | heading-verbatim fraction-of-a-quantity |

The three extension rows sit OUTSIDE the 4 R4-section-level-root rows and are
transparently labeled with their sampling status. `area::7` IS an R4 inventory
row (c67208f06b9072e9): the R4 verdict classified it as note-level-root
evidence, but its own root note records the section surface ("the parallelogram
formula A = bh is the 4.9D surface") — the note-level repair to 4.9C fixes the
JOIN, and the section-level disposition is recorded in the same round rather
than knowingly re-created for the R9 re-gate to reject again. `area::6` and
`basic-fractions::2` are not R4-sampled; they carry heading-verbatim evidence
so the R8 build does not knowingly recreate the same scope difference on
sibling sections. Zero silent repair.

### Subsumptions (2) and observations (2)

- Subsumed R1 override entries (verified, recorded — not re-applied as no-ops):
  solving-linear-inequalities ord 3 → 2.8C; basic-fractions ord 6 → 1.2A.
- Observations recorded for the operator, NOT verdicted: the drawing-straight-line-graphs
  note-join question (ords 4–5 read as equation rearrangement + ax+by=c plotting — carried
  verbatim from the R4 record); the scorer-noise note (top-1 proposals are deliberately
  noisy and bound nothing).

## 3. Amendment mechanics

Exactly one file amended in place:
`SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json`
(baseline blob `05a57b056874e8dd` verified pre-write; the R1 repair block preserved by
moving it to `repair_history`; per-row provenance with `prior` values verbatim;
`counts` recomputed **222/216/6 → 222/214/8**; dated validation clause; the two cleared
ids appended to the unresolved allowlist). The R8-facing override projection
`scripts/c42_section_overrides_r6.yaml` is derived deterministically from the verdict
record (4 verdicted + 3 extension entries with `provenance_class`, the subsumption
registry, the observations).

Fail-closed preconditions P1–P6 all pass; the R6 surface is recomputed from the R4 fresh
verdict record (not hand-listed); the extension rows' `current_code` fields are validated
against the deterministically-computed post-R6 join-derived codes.

## 4. Audit (C1–C8 ALL PASS)

| Check | Asserts |
|---|---|
| C1 | verdicts↔file two-way agreement (dispositions, prior preservation, statement re-points per tier convention) |
| C2 | counts 222/214/8; the newly cleared set == the 2 UNRESOLVED verdicts; 8 null-code rows enumerated |
| C3 | zero drift on all 211 non-surface rows (byte-level vs the HEAD blob) |
| C4 | 0 foreign codes (every resolved_code ∈ the ratified 188) |
| C5 | top-level R6 repair block, R1 block preserved in `repair_history`, validation clause, allowlist note |
| C6 | apply re-run is verify-only (byte-identical) |
| C7 | the R8 override projection == the verdict record (4+2 entries + 2 subsumptions); `sme_spcpt_verify.py` green (BASE re-pointed to this repo, script unmodified) |
| C8 | the working-tree diff surface is exactly the one amended file |

## 5. Scope guards and staleness

Chemistry, the parsed canonical bundles, the Lane C stores (concepts 82 / edges 157 /
kinds 72 incl. the 73 HUMAN_VALIDATED), `spec-links/**`, the C25–C41 records and the C42
scope/R0–R4 records are byte-untouched. The C32 notes-join and the chunk substrate are now
**stale by design** — they refresh at R7/R8; the R9 re-gate re-renders the review surface.
R5 (the §18 substrate apply, operator gate 3) remains NOT armed by anything in this round.

## 6. What this round does not do

No store row is promoted; no EQ-side or spec-links-side repair is attempted (the R0
census items remain separate operator decisions); no observation is silently converted
into a verdict; the 66-uncovered-SP corpus-gap worklist is untouched (recomputed at R8).
