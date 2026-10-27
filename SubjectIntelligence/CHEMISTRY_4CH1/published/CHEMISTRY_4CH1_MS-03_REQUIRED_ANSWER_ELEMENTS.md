---
sib_protocol: SIB-1.0
artifact_id: MS-03
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: mark_scheme_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: false
  textbook: false
  question_papers: true
  mark_schemes: true
  examiner_reports: false
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-QPMS-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-005"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "f61a5bafe6cacdf538e5e06d86f818e7737cbfe3"
    syllabai_resources: "367b5d61cd5f1ab115f9947ba2981f08389540ee"
---

# MS-03 — Required Answer Elements

## Purpose

This artifact identifies what each 4CH1 mark scheme actually requires for credit, as
parsed in the official exam corpus of record (SRC-QPMS-4CH1): the accepted-answer
element at the core of each mark point, the conditions attached to names versus
formulae, the named points that explanation items require, and the OWTTE latitude
that defines semantic equivalence. Reading these requirements off the parsed text is
exactly what the mark-scheme text is for — no requirement here is invented. Every
claim is carried on a bounded, locator-addressed excerpt from the run's evidence
pack. Research artifact; canonical planes untouched.

## Scope

**Covers:** the accepted-answer core; name/formula conditions; the required points
of linked explanations; OWTTE equivalence; alternative-element breadth; CSQ-linked
requirements.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 1C paper of the pack).

**Out of scope:** the full alternatives catalogue (MS-04), mark-loss patterns
(MS-05), partial-credit mechanics (MS-06).

## Executive Summary

Every mark point names its required element explicitly: a formula, a name, a value,
or a named semantic point. Where a name and a formula can both be given, the scheme
states the rule — the name suffices and a wrong formula is ignored, or both must be
correct. Explanation items decompose into named points (M1 the value, M2 the
mechanism), each independently required. OWTTE ("or words to that effect") marks the
schemes' semantic-equivalence latitude: the chemistry must be right, the wording is
free. And where multiple substances satisfy the chemistry, the requirement lists
them (Li+ ALLOW Sr2+). The required-element layer is therefore fully explicit in the
parsed text — candidates can rehearse against exactly what is required, in the
board's own terms.

## Main Analysis

### MS-013 — The accepted-answer core of a mark point

**Claim:** each mark point's required element is printed as the point's answer text.
**Evidence:** the flame-test ion point requires the formula — "> Li+ ALLOW Sr2+"
with its point line "- **(1)** Li+ ALLOW Sr2+" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 172-186); the precipitate point requires the name
or formula (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 174-188).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-014 — Name/formula conditions

**Claim:** where both a name and a formula are possible, the scheme prints the
condition — ignore a wrong formula if the name is right, or demand both correct.
**Evidence:** "silver bromide / AgBr If correct name given ignore incorrect formula"
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 174-188); the parsed excerpt on the salt-identity point (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 200-214).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-015 — Explanation items name their required points

**Claim:** linked explanations print the exact required points — M1 the fact, M2 the
mechanism — each independently credit-bearing.
**Evidence:** "An explanation linking the following two points: M1 33 ALLOW R has
two more protons than Q / M2 because the atomic number of R is two more (than Q)"
with its two point lines (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 140-154).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-016 — OWTTE: semantic equivalence, free wording

**Claim:** OWTTE marks where wording is free provided the chemistry is right.
**Evidence:** the clean-wire point accepts "Impurities/ other ions/ other substances
could alter/interfere with the colour of the flame ... OWTTE" — the parsed guidance
shows the accepted semantic field and the OWTTE marker (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 211-225).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-017 — Alternative elements widen the requirement

**Claim:** where more than one substance satisfies the chemistry, the requirement
itself lists the alternatives.
**Evidence:** "Li+ ALLOW Sr2+" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 172-186); the group-similarity point accepts the outer-shell formulation with its
own ALLOW column — "ACCEPT outer energy level / ALLOW they need to lose 1 electron
from the outer shell/ to gain a full outer shell" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 125-139).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-018 — CSQ-linked requirements

**Claim:** some required elements are consequential on earlier answers — the scheme
prints the CSQ note on the point itself.
**Evidence:** "lithium bromide / LiBr Mark CSQ on (a) and" — the salt point's
requirement is tied to the earlier parts' answers (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 200-214).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the 2019-06 1C official extraction (51 bounded
line-window excerpts, locators preserved; mark-scheme text cited verbatim). No
examiner reports consumed; no specimen material cited; supplementary sources not
consumed for claims.

## Limitations / Coverage Gaps

Required-element readings are anchored on one paper file of the pack; the inventory
is a demonstrated floor, not a claimed census of every required-element form across
all sessions. Excerpt-window truncation is respected — where a guidance cell is cut
off in the window, the unquoted remainder is not paraphrased. No canonical planes
were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
