#!/usr/bin/env python3
"""
T-C12 — c12_review_test.py: positive and negative tests for the operator
review gate (c12_review_render.py + c12_promote.py).

Runs in a throwaway SANDBOX copy of the repo (scripts/ subset + graph/
registries; ~1 MB): every subprocess operates on sandbox-local files, so the
live store is never touched. The sandbox starts pristine (no promotions
record) — the state before any operator has ruled.

Positive (the mechanism works, minimum contract):
  T01 review sheet renders over the live demo pass: all 5 records, hash
      bindings, verdict boxes; byte-identical on re-render (deterministic)
  T02 accept a clean SUGGESTED record -> RATIFIED entry (tier
      HUMAN_VALIDATED, ai_suggestion preserved); `promote check` green; the
      AI decisions file byte-untouched; no YAML anchors in the record
  T03 accept the abstention WITH a note -> accepted-exclusion ruling
  T04 amend -> operator mapping ratified, AI suggestion preserved verbatim
  T05 reject -> recorded in rejections, absent from promotions
  T06 idempotent re-run -> reported no-op, promotions file byte-identical
  T07 full mixed verdict set (all 5 demo records) -> 4 promotions
      (2 accepted incl. 1 exclusion + 2 amended) + 1 rejection, check green

Negative (fail closed — the tool refuses, nothing half-written):
  T08 --by "GLM agent" (AI attribution)
  T09 verdict meta.reviewed_by "Super Z" (AI attribution)
  T10 verdict for an unknown question id
  T11 accept of a REVIEW_REQUIRED (demoted) record
  T12 accept of an abstention WITHOUT the required note
  T13 amend with an invented spec point 4CH1-9.99
  T14 amend with a non-registry command word ("Understand")
  T15 amend whose mapping is identical to the AI suggestion
  T16 mutated questions file (text-hash binding)
  T17 conflicting re-verdict of an already-ratified record
  T18 duplicate keys in the verdict YAML
  T19 hand-forged promotions record: tier flipped to AI_SUGGESTED -> check fails
  T20 hand-forged: validated_by "GLM" -> check fails (attribution)
  T21 hand-forged: primary 4CH1-4.99 -> check fails (registry)
  T22 hand-forged: same question promoted AND rejected -> check fails

Usage: python3 scripts/c12_review_test.py   (no network, no key)
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
LIVE_REPO = HERE.parent

SCRIPTS_TO_COPY = ["c12_promote.py", "c12_review_render.py", "c12_spec_tagger.py"]
GRAPH_TO_COPY = ["specification_points.yaml", "command_words.yaml", "topics.yaml",
                 "spec_command_kinds.yaml"]

PASS = 0
DECISIONS = "scripts/c12_decisions/smoke-demo.agent-pass-1.yaml"


def ok(name: str) -> None:
    global PASS
    PASS += 1
    print(f"  ok  {name}")


def fail(name: str, detail: str = "") -> None:
    print(f"FAIL  {name}  {detail}", file=sys.stderr)
    sys.exit(1)


def make_sandbox() -> Path:
    sb = Path(tempfile.mkdtemp(prefix="c12-review-test-"))
    (sb / "scripts").mkdir()
    for name in SCRIPTS_TO_COPY:
        shutil.copy2(HERE / name, sb / "scripts" / name)
    shutil.copytree(HERE / "c12_decisions", sb / "scripts" / "c12_decisions")
    shutil.copytree(HERE / "c12_fixtures", sb / "scripts" / "c12_fixtures")
    (sb / "graph").mkdir()
    for name in GRAPH_TO_COPY:
        shutil.copy2(LIVE_REPO / "graph" / name, sb / "graph" / name)
    return sb


def run(sb: Path, *argv) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *[str(a) for a in argv]],
                          capture_output=True, text=True, timeout=120)


def expect_ok(sb: Path, name: str, *argv, marker: str | None = None) -> subprocess.CompletedProcess:
    r = run(sb, *argv)
    if r.returncode != 0:
        fail(name, f"exit {r.returncode}\nstdout: {r.stdout[-600:]}\nstderr: {r.stderr[-600:]}")
    if marker and marker not in r.stdout:
        fail(name, f"expected marker {marker!r}\nstdout: {r.stdout[-600:]}")
    return r


def expect_fail(sb: Path, name: str, *argv, marker: str | None = None) -> subprocess.CompletedProcess:
    r = run(sb, *argv)
    if r.returncode == 0:
        fail(name, f"expected refusal, got exit 0\nstdout: {r.stdout[-600:]}")
    if marker and marker not in (r.stdout + r.stderr):
        fail(name, f"expected marker {marker!r}\nstderr: {r.stderr[-600:]}")
    return r


def write_verdicts(sb: Path, name: str, verdicts: dict, reviewed_by: str = "Test Operator",
                   source: str = DECISIONS) -> Path:
    p = sb / "scripts" / name
    doc = {"meta": {"task": "T-C12", "source": source,
                    "reviewed_by": reviewed_by,
                    "review_reference": "graph/reports/C12_SMOKE_REVIEW_SHEET.md",
                    "review_date": "2026-09-14"},
           "verdicts": verdicts}
    p.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return p


def promote_argv(sb: Path, *extra) -> list:
    return [sb / "scripts" / "c12_promote.py", "promote", *extra]


def check_argv(sb: Path) -> list:
    return [sb / "scripts" / "c12_promote.py", "check"]


def main() -> int:
    # ── T01: review sheet renders, deterministic ─────────────────────────────
    sb = make_sandbox()
    out1, out2 = sb / "sheet1.md", sb / "sheet2.md"
    render = sb / "scripts" / "c12_review_render.py"
    expect_ok(sb, "T01 render", render, "--decisions", sb / DECISIONS, "--out", out1)
    expect_ok(sb, "T01 render re-run", render, "--decisions", sb / DECISIONS, "--out", out2)
    text = out1.read_text(encoding="utf-8")
    for qid in ["smoke-q-fractional-distillation", "smoke-q-ionic-conduction",
                "smoke-q-acid-rain", "smoke-q-physics-newtons-cradle",
                "smoke-q-fuels-sulfur-negative-control"]:
        if qid not in text:
            fail("T01 render", f"missing record {qid}")
    for marker in ["4CH1-4.8", "C-point", "Verdict", "unit_text_hash"]:
        if marker not in text:
            fail("T01 render", f"missing marker {marker!r}")
    if "9692542870e26978" not in text:
        fail("T01 render", "hash binding line missing")
    if out1.read_bytes() != out2.read_bytes():
        fail("T01 render", "render is not byte-deterministic")
    ok("T01 review sheet: 5 records, hash bindings, verdict boxes, deterministic")

    # ── T02: accept a clean SUGGESTED record ─────────────────────────────────
    sb = make_sandbox()
    v = write_verdicts(sb, "v_t02.yaml", {
        "smoke-q-fractional-distillation": {"decision": "accept",
                                            "note": "wording matches verbatim"}})
    before = (sb / DECISIONS).read_bytes()
    expect_ok(sb, "T02 accept", *promote_argv(sb, "--verdicts", v, "--date", "2026-09-14"),
              marker="RATIFIED smoke-q-fractional-distillation [accepted]")
    if (sb / DECISIONS).read_bytes() != before:
        fail("T02 accept", "the AI decisions file was modified")
    promo = yaml.safe_load((sb / "scripts" / "c12_promotions.yaml").read_text(encoding="utf-8"))
    e = promo["promotions"][0]
    if e["provenance"]["tier"] != "HUMAN_VALIDATED" or e["decision"] != "accepted":
        fail("T02 accept", "wrong tier/decision")
    if e["mapping"]["primary_spec_point"] != "4CH1-4.8" or e["ai_suggestion"]["primary_spec_point"] != "4CH1-4.8":
        fail("T02 accept", "mapping/ai_suggestion wrong")
    promo_text = (sb / "scripts" / "c12_promotions.yaml").read_text(encoding="utf-8")
    if "&id0" in promo_text or "*id0" in promo_text:
        fail("T02 accept", "YAML anchors leaked into the audit record")
    expect_ok(sb, "T02 check", *check_argv(sb), marker="check: OK — 1 promotion(s)")
    ok("T02 accept clean SUGGESTED: ratified, AI file untouched, check green")

    # ── T03: accept the abstention with a note (exclusion ruling) ────────────
    sb = make_sandbox()
    v = write_verdicts(sb, "v_t03.yaml", {
        "smoke-q-physics-newtons-cradle": {"decision": "accept",
                                           "note": "WPH11 physics: out of the 4CH1 curriculum"}})
    expect_ok(sb, "T03 exclusion", *promote_argv(sb, "--verdicts", v, "--date", "2026-09-14"))
    promo = yaml.safe_load((sb / "scripts" / "c12_promotions.yaml").read_text(encoding="utf-8"))
    e = promo["promotions"][0]
    if e["decision"] != "accepted-exclusion" or e["mapping"] is not None:
        fail("T03 exclusion", "wrong decision/mapping")
    expect_ok(sb, "T03 check", *check_argv(sb))
    ok("T03 abstention accept with note: accepted-exclusion ruling recorded")

    # ── T04: amend ────────────────────────────────────────────────────────────
    sb = make_sandbox()
    v = write_verdicts(sb, "v_t04.yaml", {
        "smoke-q-ionic-conduction": {
            "decision": "amend",
            "mapping": {"primary_spec_point": "4CH1-1.43",
                        "secondary_spec_points": ["4CH1-1.56C"],
                        "command_word": "Explain", "confidence": 0.9,
                        "rationale": "The question restates 1.43's wording; 1.56C is the 2C-only why-point"},
            "note": "operator swaps primary to the knowledge point"}})
    expect_ok(sb, "T04 amend", *promote_argv(sb, "--verdicts", v, "--date", "2026-09-14"))
    promo = yaml.safe_load((sb / "scripts" / "c12_promotions.yaml").read_text(encoding="utf-8"))
    e = promo["promotions"][0]
    if e["decision"] != "amended" or e["mapping"]["primary_spec_point"] != "4CH1-1.43":
        fail("T04 amend", "wrong decision/mapping")
    if e["ai_suggestion"]["primary_spec_point"] != "4CH1-1.56C":
        fail("T04 amend", "ai_suggestion not preserved")
    expect_ok(sb, "T04 check", *check_argv(sb))
    ok("T04 amend: operator mapping ratified, AI suggestion preserved")

    # ── T05 + T06: reject, then idempotent re-run ─────────────────────────────
    sb = make_sandbox()
    v = write_verdicts(sb, "v_t05.yaml", {
        "smoke-q-acid-rain": {"decision": "reject",
                              "reason": "fixture text is a spec recast, not a real exam command"}})
    expect_ok(sb, "T05 reject", *promote_argv(sb, "--verdicts", v, "--date", "2026-09-14"))
    promo = yaml.safe_load((sb / "scripts" / "c12_promotions.yaml").read_text(encoding="utf-8"))
    if promo["promotions"] or not promo["rejections"]:
        fail("T05 reject", "rejection landed in the wrong list")
    expect_ok(sb, "T05 check", *check_argv(sb))
    ok("T05 reject: recorded in rejections, promotions untouched")
    before = (sb / "scripts" / "c12_promotions.yaml").read_bytes()
    expect_ok(sb, "T06 idempotent", *promote_argv(sb, "--verdicts", v, "--date", "2026-09-14"),
              marker="nothing new to record")
    if (sb / "scripts" / "c12_promotions.yaml").read_bytes() != before:
        fail("T06 idempotent", "no-op re-run changed the promotions file")
    ok("T06 idempotent re-run: no-op, promotions file byte-identical")

    # ── T07: full mixed verdict set ───────────────────────────────────────────
    sb = make_sandbox()
    v = write_verdicts(sb, "v_t07.yaml", {
        "smoke-q-fractional-distillation": {"decision": "accept", "note": "verbatim match"},
        "smoke-q-ionic-conduction": {"decision": "amend",
                                     "mapping": {"primary_spec_point": "4CH1-1.43",
                                                 "secondary_spec_points": ["4CH1-1.56C"],
                                                 "command_word": "Explain", "confidence": 0.9,
                                                 "rationale": "operator: 1.43 is the restated knowledge point"}},
        "smoke-q-acid-rain": {"decision": "amend",
                              "mapping": {"primary_spec_point": "4CH1-4.16",
                                          "secondary_spec_points": ["4CH1-4.14"],
                                          "command_word": "Explain", "confidence": 0.85,
                                          "rationale": "operator: 'Understand' is not an exam command; Explain fits"}},
        "smoke-q-physics-newtons-cradle": {"decision": "accept",
                                           "note": "out-of-curriculum WPH11 physics"},
        "smoke-q-fuels-sulfur-negative-control": {"decision": "reject",
                                                  "reason": "premise+consequence aggregation; needs a two-SP ruling"}})
    expect_ok(sb, "T07 mixed", *promote_argv(sb, "--verdicts", v, "--date", "2026-09-14"))
    promo = yaml.safe_load((sb / "scripts" / "c12_promotions.yaml").read_text(encoding="utf-8"))
    dec = sorted(p["decision"] for p in promo["promotions"])
    if dec != ["accepted", "accepted-exclusion", "amended", "amended"] or len(promo["rejections"]) != 1:
        fail("T07 mixed", f"unexpected composition: {dec} / {len(promo['rejections'])} rejections")
    expect_ok(sb, "T07 check", *check_argv(sb), marker="check: OK — 4 promotion(s)")
    ok("T07 full mixed set: 4 promotions (incl. exclusion) + 1 rejection, check green")

    # ── T08–T18: negative promote cases (fresh sandbox each) ─────────────────
    sb = make_sandbox()
    v = write_verdicts(sb, "v.yaml", {"smoke-q-fractional-distillation": {"decision": "accept"}})
    expect_fail(sb, "T08 AI attribution (--by)", *promote_argv(sb, "--verdicts", v,
                "--by", "GLM agent"), marker="attribution gate")
    ok("T08 AI attribution via --by refused")

    sb = make_sandbox()
    v = write_verdicts(sb, "v.yaml",
                       {"smoke-q-fractional-distillation": {"decision": "accept"}},
                       reviewed_by="Super Z operator")
    expect_fail(sb, "T09 AI attribution (meta)", *promote_argv(sb, "--verdicts", v),
                marker="attribution gate")
    ok("T09 AI attribution via meta.reviewed_by refused")

    sb = make_sandbox()
    v = write_verdicts(sb, "v.yaml", {"smoke-q-does-not-exist": {"decision": "accept"}})
    expect_fail(sb, "T10 unknown qid", *promote_argv(sb, "--verdicts", v), marker="unknown question")
    ok("T10 unknown question id refused")

    sb = make_sandbox()
    v = write_verdicts(sb, "v.yaml",
                       {"smoke-q-acid-rain": {"decision": "accept", "note": "trying to accept a demoted record"}})
    expect_fail(sb, "T11 accept demoted", *promote_argv(sb, "--verdicts", v),
                marker="accept is blocked")
    ok("T11 accept of a REVIEW_REQUIRED (demoted) record blocked")

    sb = make_sandbox()
    v = write_verdicts(sb, "v.yaml", {"smoke-q-physics-newtons-cradle": {"decision": "accept"}})
    expect_fail(sb, "T12 exclusion without note", *promote_argv(sb, "--verdicts", v),
                marker="EXCLUSION RULING")
    ok("T12 abstention accept without note refused")

    sb = make_sandbox()
    v = write_verdicts(sb, "v.yaml", {
        "smoke-q-fractional-distillation": {"decision": "amend",
                                            "mapping": {"primary_spec_point": "4CH1-9.99",
                                                        "command_word": "Describe",
                                                        "confidence": 1.0,
                                                        "rationale": "invented"}}})
    expect_fail(sb, "T13 invented code", *promote_argv(sb, "--verdicts", v),
                marker="not in the 4CH1-2017 registry")
    ok("T13 amend with invented spec point refused")

    sb = make_sandbox()
    v = write_verdicts(sb, "v.yaml", {
        "smoke-q-fractional-distillation": {"decision": "amend",
                                            "mapping": {"primary_spec_point": "4CH1-4.8",
                                                        "secondary_spec_points": ["4CH1-4.7"],
                                                        "command_word": "Understand",
                                                        "confidence": 1.0,
                                                        "rationale": "keeping the model's word"}}})
    expect_fail(sb, "T14 bad command word", *promote_argv(sb, "--verdicts", v),
                marker="command-word registry")
    ok("T14 amend with non-registry command word refused")

    sb = make_sandbox()
    v = write_verdicts(sb, "v.yaml", {
        "smoke-q-fractional-distillation": {"decision": "amend",
                                            "mapping": {"primary_spec_point": "4CH1-4.8",
                                                        "secondary_spec_points": ["4CH1-4.7"],
                                                        "command_word": "Describe",
                                                        "confidence": 1.0,
                                                        "rationale": "identical to the AI proposal"}}})
    expect_fail(sb, "T15 amend identical", *promote_argv(sb, "--verdicts", v),
                marker="use decision: accept")
    ok("T15 amend identical to the AI suggestion refused")

    sb = make_sandbox()
    v = write_verdicts(sb, "v.yaml", {"smoke-q-fractional-distillation": {"decision": "accept"}})
    qf = sb / "scripts" / "c12_fixtures" / "smoke_questions.json"
    qdata = json.loads(qf.read_text(encoding="utf-8"))
    qdata["questions"][0]["text"] += " Mutated."
    qf.write_text(json.dumps(qdata, indent=2, ensure_ascii=False), encoding="utf-8")
    expect_fail(sb, "T16 hash binding", *promote_argv(sb, "--verdicts", v), marker="hash mismatch")
    ok("T16 mutated questions file refused (text-hash binding)")

    sb = make_sandbox()
    v = write_verdicts(sb, "v.yaml", {"smoke-q-fractional-distillation": {"decision": "accept"}})
    expect_ok(sb, "T17 first run", *promote_argv(sb, "--verdicts", v, "--date", "2026-09-14"))
    v2 = write_verdicts(sb, "v2.yaml",
                        {"smoke-q-fractional-distillation": {"decision": "reject", "reason": "changed my mind"}})
    expect_fail(sb, "T17 conflicting re-verdict", *promote_argv(sb, "--verdicts", v2),
                marker="already RATIFIED")
    ok("T17 conflicting re-verdict of a ratified record refused")

    sb = make_sandbox()
    vpath = sb / "scripts" / "v_dup.yaml"
    vpath.write_text(
        "meta:\n  reviewed_by: Test Operator\n"
        "  source: scripts/c12_decisions/smoke-demo.agent-pass-1.yaml\n"
        "  review_reference: graph/reports/C12_SMOKE_REVIEW_SHEET.md\n"
        "verdicts:\n  smoke-q-fractional-distillation:\n    decision: accept\n"
        "  smoke-q-fractional-distillation:\n    decision: reject\n    reason: dup\n",
        encoding="utf-8")
    expect_fail(sb, "T18 duplicate keys", *promote_argv(sb, "--verdicts", vpath),
                marker="duplicate keys")
    ok("T18 duplicate verdict keys refused")

    # ── T19–T22: hand-forged promotions records caught by check ──────────────
    def forge(mutate) -> Path:
        sb2 = make_sandbox()
        v = write_verdicts(sb2, "v.yaml", {"smoke-q-fractional-distillation": {"decision": "accept"}})
        expect_ok(sb2, "forge base", *promote_argv(sb2, "--verdicts", v, "--date", "2026-09-14"))
        p = sb2 / "scripts" / "c12_promotions.yaml"
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
        mutate(data)
        p.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
        return sb2

    sb2 = forge(lambda d: d["promotions"][0]["provenance"].__setitem__("tier", "AI_SUGGESTED"))
    expect_fail(sb2, "T19 forged tier", *check_argv(sb2), marker="HUMAN_VALIDATED")
    ok("T19 hand-forged tier flip caught by check")

    sb2 = forge(lambda d: d["promotions"][0]["provenance"].__setitem__("validated_by", "GLM"))
    expect_fail(sb2, "T20 forged attribution", *check_argv(sb2), marker="attribution gate")
    ok("T20 hand-forged AI validated_by caught by check")

    sb2 = forge(lambda d: d["promotions"][0]["mapping"].__setitem__("primary_spec_point", "4CH1-4.99"))
    expect_fail(sb2, "T21 forged code", *check_argv(sb2), marker="not in the 4CH1-2017 registry")
    ok("T21 hand-forged registry-invalid mapping caught by check")

    def both(d):
        d["rejections"].append(
            {"source": d["promotions"][0]["source"],
             "question_id": d["promotions"][0]["question_id"],
             "reason": "double-booked", "validated_by": "Test Operator",
             "validated_date": "2026-09-14",
             "review_reference": "graph/reports/C12_SMOKE_REVIEW_SHEET.md"})

    sb2 = forge(both)
    expect_fail(sb2, "T22 promoted+rejected", *check_argv(sb2), marker="both promoted and rejected")
    ok("T22 question both promoted and rejected caught by check")

    print(f"\nc12_review_test: {PASS} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
