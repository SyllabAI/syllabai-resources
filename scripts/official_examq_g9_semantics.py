#!/usr/bin/env python3
"""
official_examq_g9_semantics.py — the G9 aggregation law, as code.

Single source of truth for how G9 check outcomes aggregate into case
dispositions, leg dispositions and the OVERALL learner-surface gate
(consumed by official_examq_g9_static_check.py, official_examq_g9_render_check.py
and official_examq_g9_aggregate.py; the law is documented in
Official-ExamQuestion/benchmark/README.md — this module is its executable form).

THE LAW (F105)

Check outcome vocabulary:
  PASS            the check actually ran and passed
  FAIL            the check ran and the property is violated
  NOT_RUN         the check did NOT execute (renderer unreachable, dependency
                  missing, driver error, source not resolvable). Never a pass.
  NOT_APPLICABLE  the property is genuinely not checkable at this validation
                  layer, and the benchmark contract EXPLICITLY names the
                  responsible layer(s) in the check's "responsibility" field.
                  Excluded from this layer's required set — but the overall
                  gate may only PASS when every named responsible leg itself
                  ran and PASSED (delegation coverage). A NOT_APPLICABLE must
                  never silently count as a pass.

Check requirement classes:
  required     blocks the case disposition (PASS/FAIL/REVIEW per outcome)
  delegated    NOT_APPLICABLE here; responsibility names the owning leg(s)
  evidence     non-blocking evidence capture (e.g. screenshots); recorded,
               excluded from the required set

Case disposition:
  FAIL     any required check FAILs
  REVIEW   any required check is NOT_RUN (a required check could not be
           established — the documented blocking/review disposition; NEVER PASS)
  NOT_RUN  no required check executed at all (nothing was established)
  PASS     every required check PASSED (NOT_APPLICABLE/evidence checks are
           recorded alongside and excluded)

Leg disposition (over a leg's cases):
  FAIL     any case FAILs
  REVIEW   any case REVIEWs
  NOT_RUN  no case ran (all cases NOT_RUN, or the leg is missing entirely)
  PASS     every case PASSed

Overall learner-surface gate (over the MANDATORY legs — static-corpus,
static-bundles, rendered; all three are required for a PASS):
  FAIL     any mandatory leg FAILs
  REVIEW   any mandatory leg REVIEWs, OR any mandatory leg is NOT_RUN/missing,
           OR any delegated (NOT_APPLICABLE) check names responsible legs that
           are not themselves present-and-PASS (uncovered delegation)
  NOT_RUN  nothing ran at all (every leg missing)
  PASS     every mandatory leg ran and PASSED, and every delegation is covered
           by a leg that ran and PASSED

Missing evidence must not be masked by successful unrelated checks: a green
static leg can never promote a NOT_RUN rendered leg to PASS, and a PASSing
case can never launder a required check that did not run.
"""

VALIDATOR_VERSION = "g9-semantics/0.1"

OUTCOME_PASS = "PASS"
OUTCOME_FAIL = "FAIL"
OUTCOME_NOT_RUN = "NOT_RUN"
OUTCOME_NOT_APPLICABLE = "NOT_APPLICABLE"

REQ_REQUIRED = "required"
REQ_DELEGATED = "delegated"
REQ_EVIDENCE = "evidence"

# The mandatory validation legs of the overall learner-surface gate.
LEG_STATIC_CORPUS = "static-corpus"
LEG_STATIC_BUNDLES = "static-bundles"
LEG_RENDERED = "rendered"
MANDATORY_LEGS = (LEG_STATIC_CORPUS, LEG_STATIC_BUNDLES, LEG_RENDERED)


def check(outcome, *, requirement=REQ_REQUIRED, responsibility=None, cid="", area="", detail=""):
    """Build a normalized check record (additive fields; consumers may ignore)."""
    if outcome not in (OUTCOME_PASS, OUTCOME_FAIL, OUTCOME_NOT_RUN, OUTCOME_NOT_APPLICABLE):
        raise ValueError(f"invalid check outcome: {outcome!r}")
    if requirement not in (REQ_REQUIRED, REQ_DELEGATED, REQ_EVIDENCE):
        raise ValueError(f"invalid check requirement: {requirement!r}")
    rec = {"id": cid, "area": area, "outcome": outcome, "requirement": requirement,
           "detail": detail}
    if responsibility:
        rec["responsibility"] = responsibility
    # internal consistency law: NOT_APPLICABLE is always delegated and names its owner
    if outcome == OUTCOME_NOT_APPLICABLE and responsibility is None:
        raise ValueError("NOT_APPLICABLE check must declare its responsible layer(s)")
    if outcome == OUTCOME_NOT_APPLICABLE:
        rec["requirement"] = REQ_DELEGATED
    return rec


def is_required(rec):
    return rec.get("requirement", REQ_REQUIRED) == REQ_REQUIRED


def parse_responsibility(rec):
    """Extract the set of leg names a delegated check points at.

    Responsibility strings are free text in receipts ("static-bundles + rendered
    legs"); tokens are matched against the canonical leg names.
    """
    resp = rec.get("responsibility") or ""
    tokens = set()
    for leg in MANDATORY_LEGS:
        if leg in resp:
            tokens.add(leg)
    return tokens


def case_disposition(checks):
    """Aggregate one case's checks into its disposition (see module docstring)."""
    outcomes = [c.get("outcome") for c in checks if is_required(c)]
    if OUTCOME_FAIL in outcomes:
        return OUTCOME_FAIL
    if OUTCOME_NOT_RUN in outcomes:
        if all(o == OUTCOME_NOT_RUN for o in outcomes):
            return OUTCOME_NOT_RUN      # nothing was established
        return "REVIEW"                 # mixed: a required check could not be established
    if not outcomes:
        # no required check executed at all
        return OUTCOME_NOT_RUN
    return OUTCOME_PASS


def leg_disposition(cases):
    """Aggregate a leg's case dispositions into the leg disposition.

    `cases` is a list of dicts each carrying "disposition" (and possibly no
    checks — receipts from blocked runs).
    """
    if not cases:
        return OUTCOME_NOT_RUN
    disps = [c.get("disposition") for c in cases]
    if OUTCOME_FAIL in disps:
        return OUTCOME_FAIL
    if "REVIEW" in disps:
        return "REVIEW"
    if all(d == OUTCOME_NOT_RUN for d in disps):
        return OUTCOME_NOT_RUN
    if OUTCOME_NOT_RUN in disps:
        # mixed: some cases established, some not -> rises to REVIEW
        return "REVIEW"
    return OUTCOME_PASS


def leg_disposition_from_receipt(receipt):
    """Leg disposition from a committed receipt.

    Prefers the receipt's own "overall" (the leg-level verdict of record);
    recomputes from cases when "overall" is absent.
    """
    if receipt is None:
        return OUTCOME_NOT_RUN
    ov = receipt.get("overall")
    cases = receipt.get("cases") or []
    if ov is None and cases:
        ov = leg_disposition(cases)
    if ov not in (OUTCOME_PASS, OUTCOME_FAIL, "REVIEW", OUTCOME_NOT_RUN):
        ov = OUTCOME_NOT_RUN
    return ov


def collect_delegations(leg_receipts):
    """All NOT_APPLICABLE/delegated checks recorded by the given legs.

    Returns a list of (leg_name, check_record) pairs.
    """
    out = []
    for leg, receipt in leg_receipts.items():
        for case in (receipt or {}).get("cases") or []:
            for chk in case.get("checks") or []:
                if chk.get("outcome") == OUTCOME_NOT_APPLICABLE or \
                        chk.get("requirement") == REQ_DELEGATED:
                    out.append((leg, chk))
    return out


def delegation_covered(chk, green_legs):
    """True when every responsible leg named by a delegated check is green."""
    wanted = parse_responsibility(chk)
    return wanted and wanted.issubset(green_legs)


def overall_gate(leg_receipts):
    """The OVERALL learner-surface gate over the mandatory legs.

    `leg_receipts` maps leg name -> receipt dict (or None when the leg did not
    run / its receipt is missing). Returns (disposition, reasons[]) where
    reasons explains every non-PASS contribution (actionable, per-check).
    """
    receipts = {leg: leg_receipts.get(leg) for leg in MANDATORY_LEGS}
    disps = {leg: leg_disposition_from_receipt(receipts[leg]) for leg in MANDATORY_LEGS}
    reasons = []
    for leg in MANDATORY_LEGS:
        if disps[leg] == OUTCOME_FAIL:
            reasons.append(f"leg {leg}: FAIL")
    if any(d == OUTCOME_FAIL for d in disps.values()):
        return OUTCOME_FAIL, reasons
    for leg in MANDATORY_LEGS:
        if disps[leg] == "REVIEW":
            reasons.append(f"leg {leg}: REVIEW (a case could not be established)")
    if any(d == "REVIEW" for d in disps.values()):
        return "REVIEW", reasons
    for leg in MANDATORY_LEGS:
        if disps[leg] == OUTCOME_NOT_RUN:
            reasons.append(f"leg {leg}: NOT_RUN — mandatory leg missing or blocked")
    if all(d == OUTCOME_NOT_RUN for d in disps.values()):
        return OUTCOME_NOT_RUN, reasons
    if any(d == OUTCOME_NOT_RUN for d in disps.values()):
        return "REVIEW", reasons
    # every leg PASS: verify delegation coverage
    green = {leg for leg in MANDATORY_LEGS if disps[leg] == OUTCOME_PASS}
    for leg, chk in collect_delegations(receipts):
        if not delegation_covered(chk, green):
            reasons.append(
                f"delegated check {chk.get('id')!r} (recorded at leg {leg}) names "
                f"responsible legs {sorted(parse_responsibility(chk))} which are not "
                f"all present-and-PASS (green: {sorted(green)})")
    if reasons:
        return "REVIEW", reasons
    return OUTCOME_PASS, []
