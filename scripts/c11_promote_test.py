#!/usr/bin/env python3
"""
T-C11 — c11_promote_test.py: positive and negative tests for the exact-edge-
identity promotion mechanism (architecture §18).

Runs in a throwaway SANDBOX copy of the repository (scripts + graph + notes
tree minus assets; ~2 MB): the sandbox's c11_promote.py, c11_concept_pilot.py
and graph_check.py operate on sandbox-local files, so the live store is never
touched. Session-45 note: the LIVE store now carries the 28 operator §18
promotions (the session-44 CONFIRM verdicts, applied 2026-09-12); this suite
tests the mechanism on a sandbox reset to the PRE-promotion pristine state
(restore() drops the sandbox promotions file and regenerates), which is the
state every case below was designed against.

Positive (the mechanism works, minimum contract):
  T01 promote one exact SUGGESTED edge -> promotions entry; generator green;
      the edge becomes HUMAN_VALIDATED + validated_by/date; all other 65
      edges byte-identical; concepts.yaml + spec_command_kinds.yaml
      byte-identical; graph_check green with 1 promoted; deterministic
      regeneration; idempotent re-promotion is a no-op; the decision record
      and held list are byte-untouched.
  T02 promote a REVIEW_REQUIRED edge (the "two RR edges accepted" pathway)
      -> RR count drops to 1, promoted=1, checker green.

Negative (fail closed — the tool/generator/checker refuse):
  T03 malformed --edge spec (2 tokens; promotion by partial identity)
  T04 unknown triple (no authored edge matches)
  T05 held candidate (HELD-04) -> "held candidates are not promotable"
  T06 PART_OF triple -> "derived, not promotable"
  T07 bad --date
  T08 edge whose evidence was deleted (missing evidence)
  T09 edge whose evidence quote was corrupted (fails byte-verification)
  T10 hand-forged promotions file, AI attribution (anti-forgery, G13)
  T11 hand-forged promotions file, unknown triple
  T12 hand-forged promotions file, missing validated_by
  T13 duplicate promotion entries
  T14 hand-forged HUMAN_VALIDATED in the graph without a promotion record
  T15 hand-forged HUMAN_VALIDATED in the DECISION record (anti-forgery G10)
  T16 stale graph: promotion recorded, generator NOT re-run
  T17 attribution drift: graph validated_by != promotions record
  T18 decision-record status drift vs the generated graph

Every negative case must exit non-zero (tool) or fail (checker/generator) AND
leave the underlying state consistent (nothing silently half-promoted).

Usage: python3 scripts/c11_promote_test.py
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
LIVE_REPO = HERE.parent
LIVE_GRAPH = LIVE_REPO / "graph"
LIVE_SCRIPTS = LIVE_REPO / "scripts"
LIVE_NOTES = LIVE_REPO / "Chemistry IGCSE Revision Notes"

PROMOTE = "scripts/c11_promote.py"
GENERATOR = "scripts/c11_concept_pilot.py"
CHECKER = "scripts/graph_check.py"
C11_FILES = ["concepts.yaml", "concept_edges.yaml", "spec_command_kinds.yaml"]

EDGE_A = "4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLE"          # SUGGESTED
EDGE_RR = "4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AVOGADRO-LAW"  # REVIEW_REQUIRED (operator HOLD, session 41)
EDGE_REJ = "4CH1-PR-03 REQUIRES_PREREQUISITE 4CH1-CON-MOLE"                  # operator-REJECTED session 41 -> HELD-13
HELD_04 = "4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE"       # held
PART_OF_EDGE = "4CH1-CON-AR PART_OF 4CH1-1.26"                              # derived

PASSED = FAILED = 0


def ok(name, cond, detail=""):
    global PASSED, FAILED
    if cond:
        print(f"PASS  {name}")
        PASSED += 1
    else:
        print(f"FAIL  {name} {detail}")
        FAILED += 1


def make_sandbox(root: Path) -> Path:
    sb = root / "repo"
    (sb / "scripts").mkdir(parents=True)
    (sb / "graph").mkdir()
    for f in LIVE_SCRIPTS.glob("*.py"):
        shutil.copy2(f, sb / "scripts" / f.name)
    # session-47: stage the WHOLE decision-record registry (pilot + batch-1)
    shutil.copy2(LIVE_SCRIPTS / "c11_pilot_decisions.yaml",
                 sb / "scripts" / "c11_pilot_decisions.yaml")
    shutil.copy2(LIVE_SCRIPTS / "c11_batch1_decisions.yaml",
                 sb / "scripts" / "c11_batch1_decisions.yaml")
    if (LIVE_SCRIPTS / "c11_evidence").exists():
        shutil.copytree(LIVE_SCRIPTS / "c11_evidence", sb / "scripts" / "c11_evidence")
    for f in LIVE_GRAPH.glob("*.yaml"):
        shutil.copy2(f, sb / "graph" / f.name)
    # reports (review sheets/architecture) so --review-ref file resolution works
    shutil.copytree(LIVE_GRAPH / "reports", sb / "graph" / "reports")
    # notes tree (minus assets — never read by the generator/checker)
    shutil.copytree(LIVE_NOTES, sb / "Chemistry IGCSE Revision Notes",
                    ignore=shutil.ignore_patterns("assets"))
    return sb


def restore(sb: Path):
    """Reset the mutable files to pristine (after a test mutated the sandbox).

    Session-45: the live graph now carries 28 §18 promotions; simply copying
    it while dropping the promotions file would leave the sandbox in an
    INCONSISTENT state (graph HV with no store). The tests are designed
    against the PRE-promotion pristine state, so after resetting the files we
    re-run the sandbox generator with an empty store: the graph returns to
    the frozen pilot snapshot (semantic edges SUGGESTED/REVIEW_REQUIRED),
    concepts.yaml + spec_command_kinds.yaml regenerate byte-identically.
    """
    # session-47: stage the WHOLE decision-record registry (pilot + batch-1)
    shutil.copy2(LIVE_SCRIPTS / "c11_pilot_decisions.yaml",
                 sb / "scripts" / "c11_pilot_decisions.yaml")
    shutil.copy2(LIVE_SCRIPTS / "c11_batch1_decisions.yaml",
                 sb / "scripts" / "c11_batch1_decisions.yaml")
    prom = sb / "scripts" / "c11_promotions.yaml"
    if prom.exists():
        prom.unlink()
    for fn in C11_FILES:
        shutil.copy2(LIVE_GRAPH / fn, sb / "graph" / fn)
    gen(sb)


def run(sb: Path, script: str, *args: str):
    return subprocess.run([sys.executable, str(sb / script), *args],
                          capture_output=True, text=True, cwd=str(sb))


def run_tool(sb: Path, *args: str):
    return run(sb, PROMOTE, *args)


def gen(sb: Path):
    return run(sb, GENERATOR)


def check(sb: Path):
    return run(sb, CHECKER)


def read_edges(sb: Path):
    return yaml.safe_load((sb / "graph" / "concept_edges.yaml")
                          .read_text(encoding="utf-8"))["edges"]


def find_edge(edges, src, rel, tgt):
    return next(e for e in edges
                if (e["source"], e["relation"], e["target"]) == (src, rel, tgt))


def edge_key(e):
    return (e["source"], e["relation"], e["target"])


def canon(edges):
    """Comparable projection: everything except validation fields."""
    return {edge_key(e): {k: v for k, v in e.items()
                          if k not in ("validation_status", "validated_by",
                                       "validated_date")}
            for e in edges}


def state_of(edges, src, rel, tgt):
    e = find_edge(edges, src, rel, tgt)
    return (e["validation_status"], e.get("validated_by"), e.get("validated_date"))


def promo_file(sb: Path) -> Path:
    return sb / "scripts" / "c11_promotions.yaml"


def main2():
    tmp = Path(tempfile.mkdtemp(prefix="c11_promo_test_"))
    try:
        sb = make_sandbox(tmp)
        pristine_edges = canon(read_edges(sb))
        pristine_concepts = (sb / "graph" / "concepts.yaml").read_bytes()
        pristine_cks = (sb / "graph" / "spec_command_kinds.yaml").read_bytes()
        pristine_decisions = (sb / "scripts" / "c11_pilot_decisions.yaml").read_bytes()
        a = tuple(EDGE_A.split())
        rr = tuple(EDGE_RR.split())

        # ---- T01 positive: promote one exact SUGGESTED edge -----------------
        r = run_tool(sb, "--edge", EDGE_A, "--by", "test-operator",
                     "--date", "2026-09-11")
        t01 = (r.returncode == 0
               and "PROMOTED" in r.stdout
               and promo_file(sb).exists()
               and len(yaml.safe_load(promo_file(sb).read_text(encoding="utf-8"))
                       ["promotions"]) == 1)
        ok("T01a tool exit 0 + promotions entry recorded", t01,
           f"rc={r.returncode} out={r.stdout[:200]} err={r.stderr[:300]}")
        if t01:
            edges = read_edges(sb)
            st = state_of(edges, *a)
            others = {k: v for k, v in canon(edges).items() if k != a}
            ok("T01b edge HUMAN_VALIDATED + attribution",
               st == ("HUMAN_VALIDATED", "test-operator", "2026-09-11"), str(st))
            ok("T01c other 64 edges byte-identical (non-validation fields)",
               others == {k: v for k, v in pristine_edges.items() if k != a})
            ok("T01d decision record byte-untouched",
               (sb / "scripts" / "c11_pilot_decisions.yaml").read_bytes()
               == pristine_decisions)
            ok("T01e concepts.yaml + spec_command_kinds.yaml untouched",
               (sb / "graph" / "concepts.yaml").read_bytes() == pristine_concepts
               and (sb / "graph" / "spec_command_kinds.yaml").read_bytes()
               == pristine_cks)
            c = check(sb)
            ok("T01f graph_check green with 1 promoted",
               c.returncode == 0 and "1 HUMAN_VALIDATED" in c.stdout,
               c.stdout[-300:] + c.stderr[-300:])
            g1 = (sb / "graph" / "concept_edges.yaml").read_bytes()
            gen(sb)
            ok("T01g deterministic regeneration byte-identical",
               (sb / "graph" / "concept_edges.yaml").read_bytes() == g1)
            r2 = run_tool(sb, "--edge", EDGE_A, "--by", "test-operator",
                          "--date", "2026-09-11")
            ok("T01h idempotent re-promotion is a no-op",
               r2.returncode == 0 and "already promoted" in r2.stdout
               and len(yaml.safe_load(promo_file(sb).read_text(encoding="utf-8"))
                       ["promotions"]) == 1)

        # ---- T02 positive: promote a REVIEW_REQUIRED edge --------------------
        # (the remaining RR edge — GAS-VOL-CALC -> AVOGADRO-LAW, operator HOLD:
        # promotion here proves the RR pathway mechanically; the live operator
        # HOLD means it is never exercised on the real store)
        restore(sb)
        r = run_tool(sb, "--edge", EDGE_RR, "--by", "operator",
                     "--date", "2026-09-11")
        edges = read_edges(sb)
        rr_st = state_of(edges, *rr)
        c = check(sb)
        # session-47: the sandbox registry also stages the batch-1 record,
        # whose subsumption-class quarantine edge (CRYSTALLISATION ->
        # SOLUTION) stays REVIEW_REQUIRED — the pilot RR edge's promotion
        # consumes only itself. Expected RR after T02: 1 (the batch
        # quarantine), not 0.
        ok("T02 RR-edge promotion pathway (pilot RR 1->0, promoted=1, batch quarantine RR stays, checker green)",
           r.returncode == 0
           and rr_st[0] == "HUMAN_VALIDATED"
           and sum(1 for e in edges
                   if e["validation_status"] == "REVIEW_REQUIRED") == 1
           and c.returncode == 0 and "1 HUMAN_VALIDATED" in c.stdout,
           f"rc={r.returncode} st={rr_st} err={r.stderr[:200]}")

        # ---- negative cases: tool fails closed, nothing written -------------
        neg_cases = [
            ("T03 malformed 2-token spec (partial identity)",
             ("--edge", "4CH1-CON-MOLE REQUIRES_PREREQUISITE",
              "--date", "2026-09-11"),
             "exact identity"),
            ("T04 unknown triple",
             ("--edge", "4CH1-CON-MOLE RELATED_TO 4CH1-CON-DOES-NOT-EXIST",
              "--date", "2026-09-11"),
             "no authored edge matches"),
            ("T05 held candidate HELD-04 not promotable",
             ("--edge", HELD_04, "--date", "2026-09-11"),
             "HELD-04"),
            ("T06 PART_OF not promotable",
             ("--edge", PART_OF_EDGE, "--date", "2026-09-11"),
             "PART_OF"),
            ("T07 bad date",
             ("--edge", EDGE_A, "--date", "2026/09/11"),
             "YYYY-MM-DD"),
            ("T19 operator-REJECTED identity not promotable (HELD-13, permanent)",
             ("--edge", EDGE_REJ, "--date", "2026-09-11"),
             "HELD-13"),
        ]
        for name, args, expect in neg_cases:
            restore(sb)
            r = run_tool(sb, *args, "--by", "test-operator")
            ok(name, r.returncode != 0 and expect in (r.stderr + r.stdout)
               and not promo_file(sb).exists(),
               f"rc={r.returncode} err={r.stderr[:200]}")

        # T08/T09: corrupted evidence in the decision record — fail pre-write
        for name, mutate, expect in [
                ("T08 missing evidence (empty evidence list)",
                 lambda sb_: _mut_empty_evidence(sb_),
                 "no evidence"),
                ("T09 corrupted evidence quote",
                 lambda sb_: _mut_corrupt_quote(sb_),
                 "byte-verify")]:
            restore(sb)
            mutate(sb)
            r = run_tool(sb, "--edge", EDGE_A, "--by", "test-operator",
                         "--date", "2026-09-11")
            ok(name, r.returncode != 0 and expect in (r.stderr + r.stdout)
               and not promo_file(sb).exists(),
               f"rc={r.returncode} err={r.stderr[:250]}")

        # T10-T13: hand-forged promotions files — generator G13 fails closed
        forged = [
            ("T10 AI attribution (anti-forgery)",
             _forge(EDGE_A, by="GLM (Super Z agent, z.ai)"),
             "AI cannot promote"),
            ("T11 unknown triple",
             _forge("4CH1-CON-MOLE RELATED_TO 4CH1-CON-DOES-NOT-EXIST"),
             "no authored edge matches"),
            ("T12 missing validated_by",
             [{"edge": {"source": a[0], "relation": a[1], "target": a[2]},
               "validated_date": "2026-09-11",
               "review_reference": "graph/reports/C11_PILOT_REVIEW_SHEET.md"}],
             "validated_by missing"),
            ("T13 duplicate entries",
             _forge(EDGE_A) + _forge(EDGE_A),
             "duplicate promotion"),
        ]
        for name, entries, expect in forged:
            restore(sb)
            _write_promotions(sb, entries)
            pre = (sb / "graph" / "concept_edges.yaml").read_bytes()
            g = gen(sb)
            # the generator must fail closed AND leave the graph untouched
            # (byte-equal to its pre-attempt state — session-45: no longer
            # the LIVE file, which now carries the 28 real promotions)
            ok(name, g.returncode != 0 and expect in g.stderr
               and (sb / "graph" / "concept_edges.yaml").read_bytes() == pre,
               f"rc={g.returncode} err={g.stderr[:250]}")

        # T20: forged promotion of the OPERATOR-REJECTED identity — G13 must
        # fail closed with the rejected-candidate diagnosis (permanence guard)
        restore(sb)
        _write_promotions(sb, _forge(EDGE_REJ))
        pre = (sb / "graph" / "concept_edges.yaml").read_bytes()
        g = gen(sb)
        ok("T20 forged promotion of the operator-rejected identity fails closed",
           g.returncode != 0 and "HELD-13" in g.stderr
           and (sb / "graph" / "concept_edges.yaml").read_bytes() == pre,
           f"rc={g.returncode} err={g.stderr[:250]}")

        # T14: forged HUMAN_VALIDATED in the graph (no promotion record)
        restore(sb)
        _forge_graph_status(sb, a, "HUMAN_VALIDATED", "attacker", "2026-09-11")
        c = check(sb)
        ok("T14 graph-forged HUMAN_VALIDATED without promotion record",
           c.returncode != 0 and "c11.10" in c.stdout
           and "matching promotion record" in c.stdout,
           c.stdout[-400:])

        # T15: forged HUMAN_VALIDATED in the DECISION record
        restore(sb)
        _mut_decision_status(sb, a)
        g = gen(sb)
        c = check(sb)
        ok("T15 decision-record HUMAN_VALIDATED rejected (G10 + c11.13)",
           g.returncode != 0 and "G10" in g.stderr
           and c.returncode != 0 and "c11.13" in c.stdout,
           f"gen={g.stderr[:150]} chk={c.stdout[-200:]}")

        # T16: stale graph — promotion recorded, generator not re-run
        restore(sb)
        _write_promotions(sb, _forge(EDGE_A))
        c = check(sb)   # graph still pristine (SUGGESTED)
        ok("T16 stale graph after promotion detected",
           c.returncode != 0 and "not reflected in the graph" in c.stdout,
           c.stdout[-300:])

        # T17: attribution drift between graph and promotion record
        restore(sb)
        r = run_tool(sb, "--edge", EDGE_A, "--by", "operator",
                     "--date", "2026-09-11")
        _forge_graph_status(sb, a, "HUMAN_VALIDATED", "someone-else", "2026-09-11")
        c = check(sb)
        ok("T17 attribution drift vs promotion record",
           c.returncode != 0 and "attribution mismatch" in c.stdout,
           c.stdout[-300:])

        # T18: status drift (graph SUGGESTED, decisions say REVIEW_REQUIRED)
        restore(sb)
        g = gen(sb)
        edges = read_edges(sb)
        e = find_edge(edges, *a)
        e["validation_status"] = "REVIEW_REQUIRED"
        e["ambiguity_note"] = "drifted"
        _save_edges(sb, edges)
        c = check(sb)
        ok("T18 status drift vs decision record detected",
           c.returncode != 0 and "status drift" in c.stdout,
           c.stdout[-300:])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if FAILED:
        print(f"c11_promote_test: {FAILED} FAILURE(S), {PASSED} passed")
        sys.exit(1)
    print(f"c11_promote_test: ALL PASS — {PASSED}/{PASSED + FAILED} "
          f"(promotion mechanism: exact identity, fail-closed, idempotent, "
          f"deterministic, anti-forgery; live store untouched)")


# --- sandbox mutations ---------------------------------------------------------

def _mut_empty_evidence(sb: Path):
    p = sb / "scripts" / "c11_pilot_decisions.yaml"
    d = yaml.safe_load(p.read_text(encoding="utf-8"))
    a = tuple(EDGE_A.split())
    for e in d["edges"]:
        if (e["source"], e["relation"], e["target"]) == a:
            e["evidence"] = []
    p.write_text(yaml.safe_dump(d, allow_unicode=True, sort_keys=False,
                                width=100), encoding="utf-8")


def _mut_corrupt_quote(sb: Path):
    p = sb / "scripts" / "c11_pilot_decisions.yaml"
    d = yaml.safe_load(p.read_text(encoding="utf-8"))
    a = tuple(EDGE_A.split())
    for e in d["edges"]:
        if (e["source"], e["relation"], e["target"]) == a:
            e["evidence"][0]["quote"] = "fabricated quote that appears nowhere"
    p.write_text(yaml.safe_dump(d, allow_unicode=True, sort_keys=False,
                                width=100), encoding="utf-8")


def _mut_decision_status(sb: Path, key):
    p = sb / "scripts" / "c11_pilot_decisions.yaml"
    d = yaml.safe_load(p.read_text(encoding="utf-8"))
    for e in d["edges"]:
        if (e["source"], e["relation"], e["target"]) == key:
            e["validation_status"] = "HUMAN_VALIDATED"
    p.write_text(yaml.safe_dump(d, allow_unicode=True, sort_keys=False,
                                width=100), encoding="utf-8")


def _forge(edge: str, by="operator", date="2026-09-11") -> list:
    src, rel, tgt = edge.split()
    return [{"edge": {"source": src, "relation": rel, "target": tgt},
             "validated_by": by, "validated_date": date,
             "review_reference": "graph/reports/C11_PILOT_REVIEW_SHEET.md"}]


def _write_promotions(sb: Path, entries: list):
    promo_file(sb).write_text(
        yaml.safe_dump({"meta": {"task": "T-C11", "stage": "pilot-promotion"},
                        "promotions": entries},
                       allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8")


def _forge_graph_status(sb: Path, key, status, by, date):
    edges = read_edges(sb)
    e = find_edge(edges, *key)
    e["validation_status"] = status
    if by:
        e["validated_by"] = by
        e["validated_date"] = date
    _save_edges(sb, edges)


def _save_edges(sb: Path, edges):
    p = sb / "graph" / "concept_edges.yaml"
    d = yaml.safe_load(p.read_text(encoding="utf-8"))
    d["edges"] = edges
    p.write_text(yaml.safe_dump(d, allow_unicode=True, sort_keys=False,
                                width=100), encoding="utf-8")


if __name__ == "__main__":
    main2()
