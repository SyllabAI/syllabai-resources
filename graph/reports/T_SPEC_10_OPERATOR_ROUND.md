# T-SPEC-10 — operator reasoning round: the id-level pendings mapped in-house

Operator instruction (Nawaf Al Hussain Khondokar, 2026-09-19, IM):
**"You can go through all of them and use your reasoning to map the remaining
right? Without using any scripts and stuff, using your own reasoning powers?
Or will you start hallucinating?"** — i.e. the remaining unresolved tag ids
are decided by direct operator reasoning against the committed registries and
the official Pearson PDFs, not by scripted matching, with **no upstream
tickets**. The anti-hallucination discipline is procedural: every resolved
code was read verbatim from the committed registry (the applier pair-checks
`official_id` against `official_code`); every absence claim was re-verified
against the `pdftotext -layout` extraction of the official PDF
(`scripts/t_spec_10_work/pdfcache/`); anything not defensible stayed pending
with a sharpened honest reason. PMT excluded as source throughout.

## 1. Starting point

After T-SPEC-9 the sidecars carried **258 unresolved exam-lane tag ids**
(referencing zero uncoded parts — every exam part was already coded). A
per-tag reasoning pass over all 258 (plus the separate RevisionNotes
chemistry sidecar, whose 162 blank entries are a counts-field artifact of
its legacy schema — `unresolved_ids: 0` per its own accounting, not
pendings) found three kinds of truth:

1. **stale pendings** — the claimed blocker no longer exists (mostly because
   the T-SPEC-9 economics parse repair restored rows nobody revisited, or
   because an earlier round's claim was simply wrong);
2. **wrong recorded mappings** — four existing resolutions whose code did
   not match the tag subject;
3. **honest absences** — content the published print genuinely lacks
   (PDF-verified), or names with no single carrier statement.

## 2. What was decided (83 ids / 87 lane-records)

- **45 resolves** (43 new + recorded in `scripts/t_spec_10_verdicts.yaml`
  with tiers `P2_operator_content_join` / `S0_operator_override`):
  economics 8 (fiscal policy x2 -> restored 2.1.2a; globalisation ->
  restored 2.2.1a; free-trade costs/benefits -> restored 2.2.2a;
  nationalisation S0 -> 1.1.5j inverse-policy note; GDP-limitations S0 ->
  2.1.1a; cost graphs S0 -> 1.2.3a), accounting 4 (irrecoverable-debt
  recovery -> S2.143; direct/indirect costs S0 -> S4.174; balancing S0 ->
  S2.134; expenses transfer S0 -> S4.158), business 1 (government economic
  objectives S0 -> 1.6.1), further-maths 1 (exact trig values -> 10B — the
  print's own inclusion note names "the exact values for sine, cosine and
  tangent of 30, 45, 60"), geography 5 (risk assessment -> S9.107 verbatim;
  data presentation -> S9.116; enquiry question -> S9.105; location & site
  -> S4.187 part-evidenced; limitations S0 -> S9.111), ICT 2 (head/body
  elements S0 -> 6.4.4, the print's only HTML-code statement), SDA physics
  18 (Snell's law -> 3.18; the refraction/snell/density core practicals ->
  3.17/3.19/5.4; transverse & longitudinal -> 3.2; EM dangers -> 3.13;
  resultant force -> 1.15; friction -> 1.16; selecting fuses -> 2.2;
  electrical power -> 2.4; charge calculation -> 2.15; V=IR joins -> 2.13;
  pressure -> 5.5; density -> 5.3; work done -> 4.11; power -> 4.16),
  modular maths 5 (perpendicular lines -> U1H-3.3G part-verbatim;
  congruence -> U2F-4.2F cross_unit; ordering FDP -> U1F-1.3C cross_unit;
  two-way tables -> U2F-6.1B cross_unit; problem solving with areas ->
  U2H-4.11C cross_unit).
- **2 refinements** (wrong recorded codes corrected, old code asserted and
  audited): `spcpt_3dwTMtMPJqHpnmch` (Perpendicular Lines) on
  igcse-maths-a-18-higher 4.5A ("measure and draw lines to the nearest
  millimetre") -> 3.3G — the referencing parts verbatim ask to "find the
  equation of" a perpendicular line (31 parts re-pointed);
  `spcpt_3fMGfNtg3hXMg6gC` (Problem Solving with Areas) on modH1 4.4F
  ("average speed, distance and time") -> U2H-4.11C "use areas and volumes
  of similar figures in solving problems" (24 parts re-pointed).
- **2 unresolves** (mappings reverted to the tail where no honest target
  exists, old code asserted): Speed-Time Graphs on igcse-maths-a-18-foundation
  was 2.8D ("represent simple linear inequalities") — the 4MA1 print carries
  no speed-time statement (PDF-verified); Nets of Solids was 4.10A
  ("recognise and give the names of solids") — the print carries no nets
  statement (PDF-verified). Both referenced zero parts, so the learner tail
  stays at zero.
- **40 pending-reason corrections** — stale claims replaced with the
  verified truth: the "flagged for parse repair" clauses on sectors (the
  statement exists as H-4.9A/U1H-4.9A — the real blocker is the Higher-only
  tier scope), on comparing-data/discrete-continuous (print-level
  absences), the further-maths "mangled fragment" (the print's 9A exclusion
  clause IS the committed text), the geography "no content statements to
  name-match" claim (the S9 fieldwork-skills rows exist), the accounting
  "parse carries no irrecoverable-debts statements" claim (S2.141-143
  exist), and the SDA-physics name-only tags (14 sharpened reasons:
  topic-family / concept-family / ambiguous / video-page, each naming the
  statements it spans — the one-code schema must not collapse families,
  per the operator's T-SPEC-2b Alkenes ruling).

## 3. What stays pending, and why (honest tail)

- **ial-physics-19 (56)** — WPH13/WPH16 practical-skills tags: the IAL print
  carries no numbered unit-3/6 statements (PDF-verified, T-SPEC-5); the
  parts already carry part-level nearest-neighbour overrides (T-SPEC-9).
- **ial-maths (9)** — Eulerian/Hamiltonian/graph-theory introductions,
  centre-of-mass rods/laminae/frameworks, trig definitions/exact values,
  decision-making strategy: statements absent from the print (PDF-verified).
- **igcse-english-literature-16 (77)** — 72 aspect-only set-text/exam-skill
  pages (Klara and the Sun, Modern Drama/Prose, Literary Heritage
  walkthroughs) with no single-statement home, plus 5 nameless ids.
- **igcse-science-double-award-17-physics (14)** — topic/concept-family
  names (Light, Sound, Charge, Current, Voltage, EM spectrum...) that the
  one-code schema must not collapse, two genuinely ambiguous "calculating"
  pages, two video tags.
- **The rest (~30)** — operator-confirmed pendings (chem-modular x9,
  SDA-chem x1 — T-SPEC-2b rulings, untouched), nameless/empty ids
  (nothing to reason from), exam-structure guides, GCSE-bridge content
  (planes of symmetry, population & sampling, speed-time graphs), and
  lane-pool exclusions by design (Foundation lanes exclude Higher-only
  statements).

## 4. Result

- applier `scripts/t_spec_10_apply.py`: fail-closed (pair-checks, was_code
  assertions, population closure) — **zero errors**;
- verify `scripts/sme_spcpt_verify.py`: **ALL GATES PASSED** — 39 courses,
  27,700 parts, question parts 26,867/26,867 = 100% coded, uncoded tail 0;
- spec-links rebuilt: 45,501 items, **36,766 coded** (was 36,743; +23 from
  the newly resolved ids);
- audit trail: `graph/reports/T_SPEC_10_APPLY.json` (per-lane stats +
  refinement/unresolve audit);
- unresolved exam-lane ids: **258 -> 182** — every one re-examined this
  round, each carrying a verified-honest reason (no-guess discipline).

## 5. Mechanics

- decision record: `scripts/t_spec_10_verdicts.yaml` (83 ids, 87
  lane-records: 45 resolves, 2 refinements, 2 unresolves, 40
  pending-reason updates — every rationale quotes the registry row or the
  PDF finding);
- applier: `scripts/t_spec_10_apply.py` (T-SPEC-9 machinery extended with
  fail-closed refinement/unresolve/pending-reason classes);
- PDF verification cache: `scripts/t_spec_10_work/pdfcache/` (workspace
  only, not committed);
- no parse repairs were needed (no registry rows added or changed — the
  suspected parse gaps turned out to be stale claims or genuine absences);
- canonical bundles and graph YAMLs untouched by construction.

## 6. Post-round audit (random-sample re-check, 2026-09-19)

The operator requested random checks of the 45 coded judgments
(43 resolves + 2 refinements). A seed-fixed random sample of 12
(seed 20260919) was re-verified by direct reading of the SME tag entry,
the committed registry row and the official PDF extraction:

- 12/12 sampled **codes correct** (PerpLines refinement's old 4.5A row
  verbatim = "measure and draw lines to the nearest millimetre" — the
  correction to 3.3G stands; free-trade pair, SDA physics x5, geography,
  economics pair all confirmed against the registry wording);
- all 10 S0 absence claims re-verified against the PDF cache: 9 TRUE,
  **1 FALSE** — `spcpt_XGQK9rtnFdFvHqhW` (Limitations of Using GDP to
  Measure Growth): the 4EC1 print DOES carry "limitations of GDP as a
  measure of growth" (PDF lines 880-882) and the committed registry row
  2.1.1a carries it as a sub-item, so the record is re-tiered
  **S0 -> P2_operator_content_join** (verbatim sub-item join);
  **code 2.1.1a unchanged** (no learner-facing change, spec-links
  unaffected);
- audit corrections applied in
  `scripts/t_spec_10_verdicts.yaml` (tier + rationale quoting the
  sub-item and PDF lines) and re-applied via
  `scripts/t_spec_10_apply.py`;
- applier hardened while re-applying: unresolve records are now
  idempotent on re-run (previously errored "unresolve but not mapped"),
  same-code tier changes are counted as `record_updated` instead of
  `idempotent`, unchanged lanes/manifests are no longer rewritten, and
  the manifest pipeline list is `sorted(set(...))` (was
  order-nondeterministic `list(set(...))`);
- post-audit verify: **ALL GATES PASSED** (39 courses, 27,700 parts,
  question parts 26,867/26,867 = 100% coded).

**Extension to full coverage (same day, operator request):** the remaining
33 coded records were audited with the same method (evidence pack r2:
tag entry + registry row/sub-items + applied sidecar + referencing-part
text). Result: **33/33 confirmed, 0 defects** —
- accounting 3 (S2.143 best available home — no explicit recovery-of-
  written-off-debts row exists in either the S2.14x or S5.18x family;
  S2.134/S4.158 S0 absence claims TRUE), business 1 (1.6.1 S0 TRUE),
  economics 4 (2.2.1a/2.1.2a x2 verbatim; 1.2.3a S0 TRUE),
- further-maths 1: 10B's inclusion note verbatim in the print (PDF lines
  683-685, "To include the exact values for sine, cosine and tangent of
  30°, 45°, 60°"),
- geography 4 (S9.105/107/116 verbatim; S9.111 S0 TRUE) — the round-1
  S4.187 part quote also verified verbatim ("Suggest one reason for the
  choice of economic activity in this location", Port of Barcelona figure),
- ICT 2 (6.4.4 S0 pair, registry-verified), maths modular 5 (cross-lane
  twin consistency proven for Two-Way-Tables/Congruence/Ordering-FDP;
  refinement's old U1F-4.4F verified verbatim as the average-speed row —
  wrong subject, correction to U2H-4.11C stands; the Perpendicular-Lines
  part quote located verbatim in the lane's linear-graphs topic in
  problem_md LaTeX form),
- SDA physics 13 (all verbatim relationship/practical joins; the 4.11 vs
  4.12 and 4.16 vs 2.4 discriminations confirmed against the registry).

Full-audit verdict: **45/45 codes correct**; the single defect found in
the whole set was the round-1 GDP annotation (tier + rationale, code
unaffected, already repaired). Every quoted evidence fragment across the
45 rationales (part texts, registry rows, PDF inclusion note, all 10
absence claims) is now independently verified.
