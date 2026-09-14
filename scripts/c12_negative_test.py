#!/usr/bin/env python3
"""
T-C12 — negative tests for the c12_spec_tagger check gate.

Corruption classes are injected into decision records; each class MUST be
caught by `check` (exit 1 with a precise marker). A missing catch fails this
script. Then positive controls verify that honest records pass and that the
deterministic stages behave (prefilter anchors, physics abstention control,
determinism, from-paper adapter, verify-stage record assembly without network).

Classes (check gate):
  1. tier flipped to HUMAN_VALIDATED (premature authority, anti-forgery)
  2. validation_status = HUMAN_VALIDATED from generation
  3. invented spec point 4CH1-9.99 as primary
  4. foreign-curriculum code 4CH0-1.15 as primary
  5. command_word not in the command-word registry
  6. confidence 1.7 (outside [0,1]) — strict-schema failure
  7. SUGGESTED with confidence below the meta threshold
  8. unmatched record (mapping null) marked SUGGESTED
  9. REVIEW_REQUIRED without ambiguity_note
 10. duplicate question_id
 11. queue mismatch (id missing from manualReview)
 12. provenance derivation_notes emptied — strict-schema failure
 13. secondary spec point duplicating the primary
 14. SUGGESTED with empty rationale

Positive controls:
  A. honest file (1 SUGGESTED + 1 unmatched REVIEW_REQUIRED) -> check OK
  B. verify-stage assembly rules without network: anti-forgery hard-fail on
     HUMAN_VALIDATED in a raw response; low confidence -> REVIEW_REQUIRED;
     clean high-confidence response -> SUGGESTED
  C. prefilter over the committed smoke fixture: anchored chemistry units hit
     their registry anchors (top-3, weak=false); the REAL June-2025 WPH11
     physics question is weak=true (out-of-curriculum control); run is
     byte-identical twice
  D. from-paper adapter over the committed sample paper.json: one unit per
     part + stemless MCQ, tool-name guard enforced

Usage: python3 scripts/c12_negative_test.py   (no network, no key)
"""
from __future__ import annotations

import contextlib
import io
import json
import shutil
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import c12_spec_tagger as t  # noqa: E402

REPO = HERE.parent
FIXTURES = HERE / "c12_fixtures"
THRESHOLD = 0.75
RUN_DATE = "2026-09-14"

_failures: list[str] = []
_passed = 0


def report(name: str, ok: bool, detail: str = "") -> None:
    global _passed
    if ok:
        _passed += 1
        print("  ok  %s" % name)
    else:
        _failures.append("%s %s" % (name, detail))
        print("FAIL  %s %s" % (name, detail))


# ── record builders (exercise the real assembly path) ────────────────────────

UNIT_DISTILL = {"id": "unit-distill",
                "text": "Describe how the industrial process of fractional distillation "
                        "separates crude oil into fractions."}
RAW_GOOD = {"primary_spec_point": "4CH1-4.8", "secondary_spec_points": ["4CH1-4.7"],
            "command_word": "Describe", "confidence": 0.9,
            "rationale": "Matches the registry wording on fractional distillation of crude oil.",
            "ambiguous": False}
RAW_UNMATCHED = {"primary_spec_point": None, "secondary_spec_points": [],
                 "command_word": None, "confidence": 0.05,
                 "rationale": "Out-of-curriculum physics text.", "ambiguous": False}


def good_record() -> t.DecisionRecord:
    return t.assemble_record(UNIT_DISTILL, RAW_GOOD, "GLM glm-4.6 (test)", "c12-test",
                             RUN_DATE, THRESHOLD)


def unmatched_record(qid: str = "unit-physics") -> t.DecisionRecord:
    unit = dict(UNIT_DISTILL, id=qid)
    return t.assemble_record(unit, RAW_UNMATCHED, "GLM glm-4.6 (test)", "c12-test",
                             RUN_DATE, THRESHOLD)


def write_decisions(tmp: Path, records: list[t.DecisionRecord], queues=None) -> Path:
    if queues is None:
        queues = {
            "highConfidence": [r.question_id for r in records if r.validation_status == "SUGGESTED"],
            "manualReview": [r.question_id for r in records if r.validation_status != "SUGGESTED"],
        }
    doc = {"meta": {"task": "T-C12", "extraction_pass": "c12-test", "curriculum_code": t.CURRICULUM,
                    "generated_date": RUN_DATE, "model_version": "GLM glm-4.6 (test)",
                    "high_confidence_threshold": THRESHOLD, "source_questions": "fixture",
                    "queues": queues, "counts": {}},
           "decisions": [r.model_dump() for r in records]}
    path = tmp / "decisions.yaml"
    path.write_text(yaml.safe_dump(doc, sort_keys=True), encoding="utf-8")
    return path


def run_check(path: Path) -> tuple[int, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        rc = t.main(["check", str(path)])
    return rc, out.getvalue() + err.getvalue()


def check_catches(tmp: Path, name: str, records, marker: str, queues=None) -> None:
    path = write_decisions(tmp, records, queues)
    rc, err = run_check(path)
    caught = rc != 0 and marker in err
    report(name, caught, "" if caught else "(rc=%d, wanted marker %r in:\n%s)" % (rc, marker, err))


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    print("T-C12 negative tests (no network, no key)")
    reg = t.load_registries()
    tmp = Path(tempfile.mkdtemp(prefix="c12-neg-"))
    try:
        # ── negative classes: the check gate MUST catch each corruption ──
        print("- check gate: corruption classes")

        r1 = good_record()
        r1.provenance.tier = t.FORBIDDEN_STATE
        check_catches(tmp, "1 tier flipped to HUMAN_VALIDATED", [r1], "anti-forgery")

        r2 = good_record()
        r2.validation_status = t.FORBIDDEN_STATE
        check_catches(tmp, "2 status HUMAN_VALIDATED from generation", [r2],
                      "generation may only emit")

        r3 = good_record()
        r3.mapping.primary_spec_point = "4CH1-9.99"
        check_catches(tmp, "3 invented spec point 4CH1-9.99", [r3],
                      "not in the %s registry" % t.CURRICULUM)

        r4 = good_record()
        r4.mapping.primary_spec_point = "4CH0-1.15"
        check_catches(tmp, "4 foreign-curriculum 4CH0 code", [r4],
                      "not in the %s registry" % t.CURRICULUM)

        r5 = good_record()
        r5.mapping.command_word = "Shout"
        check_catches(tmp, "5 command_word outside registry", [r5], "command_word")

        r6 = good_record()
        r6.mapping.confidence = 1.7
        check_catches(tmp, "6 confidence outside [0,1]", [r6], "strict schema")

        r7 = good_record()
        r7.mapping.confidence = 0.3
        check_catches(tmp, "7 SUGGESTED below threshold", [r7], "SUGGESTED with confidence")

        r8 = unmatched_record()
        r8.validation_status = "SUGGESTED"
        r8.ambiguity_note = None
        check_catches(tmp, "8 unmatched marked SUGGESTED", [r8],
                      "unmatched record must be REVIEW_REQUIRED")

        r9 = good_record()
        r9.mapping.confidence = 0.3
        r9.validation_status = "REVIEW_REQUIRED"
        r9.ambiguity_note = None
        check_catches(tmp, "9 REVIEW_REQUIRED without ambiguity_note", [r9],
                      "REVIEW_REQUIRED needs ambiguity_note")

        r10a, r10b = good_record(), good_record()
        check_catches(tmp, "10 duplicate question_id", [r10a, r10b], "duplicate question_id")

        r11 = unmatched_record()
        check_catches(tmp, "11 queue mismatch (manual review id dropped)", [r11],
                      "manualReview does not match",
                      queues={"highConfidence": [], "manualReview": []})

        r12 = good_record()
        r12.provenance.derivation_notes = ""
        check_catches(tmp, "12 provenance derivation_notes emptied", [r12], "strict schema")

        r13 = good_record()
        r13.mapping.secondary_spec_points = ["4CH1-4.8"]
        check_catches(tmp, "13 secondary duplicates primary", [r13], "duplicates primary")

        r14 = good_record()
        r14.mapping.rationale = "   "
        check_catches(tmp, "14 SUGGESTED with blank rationale", [r14],
                      "SUGGESTED needs a non-empty rationale")

        # ── positive control A: honest file passes ──
        print("- check gate: positive control")
        ok_rec = good_record()
        um_rec = unmatched_record()
        path = write_decisions(tmp, [ok_rec, um_rec])
        rc, err = run_check(path)
        report("A honest file (1 SUGGESTED + 1 unmatched REVIEW_REQUIRED) passes",
               rc == 0 and "check: OK" in err, err)

        # ── positive control B: verify-stage assembly rules (no network) ──
        print("- verify-stage assembly rules")
        try:
            t.assemble_record(UNIT_DISTILL,
                              dict(RAW_GOOD, rationale="proposed by HUMAN_VALIDATED data"),
                              "GLM test", "c12-test", RUN_DATE, THRESHOLD)
            report("B1 anti-forgery hard-fail on HUMAN_VALIDATED in raw response", False,
                   "(no SystemExit raised)")
        except SystemExit:
            report("B1 anti-forgery hard-fail on HUMAN_VALIDATED in raw response", True)

        rec_low = t.assemble_record(UNIT_DISTILL, dict(RAW_GOOD, confidence=0.4),
                                    "GLM test", "c12-test", RUN_DATE, THRESHOLD)
        report("B2 low confidence -> REVIEW_REQUIRED with note",
               rec_low.validation_status == "REVIEW_REQUIRED"
               and bool(rec_low.ambiguity_note)
               and "below threshold" in rec_low.ambiguity_note,
               str(rec_low.ambiguity_note))

        rec_ok = good_record()
        errs = t.registry_errors(rec_ok, reg, THRESHOLD)
        report("B3 clean high-confidence record -> SUGGESTED, zero registry errors",
               rec_ok.validation_status == "SUGGESTED" and not errs, str(errs))

        fenced = "```json\n" + json.dumps(RAW_GOOD) + "\n```"
        report("B4 extract_json_object survives code fences",
               t.extract_json_object(fenced)["primary_spec_point"] == "4CH1-4.8")
        prose = 'Sure! {"a": {"b": 1}} done'
        report("B5 extract_json_object takes first balanced block",
               t.extract_json_object(prose) == {"a": {"b": 1}})

        # ── positive control C: prefilter over the committed smoke fixture ──
        print("- prefilter determinism + adversarial controls")
        units = t.load_questions(FIXTURES / "smoke_questions.json")
        pf = t.Prefilter(reg)
        runs = [json.dumps({u["id"]: pf.rank(u["text"]) for u in units},
                           sort_keys=True) for _ in range(2)]
        report("C0 prefilter deterministic (byte-identical twice)", runs[0] == runs[1])

        expect_anchors = {
            "smoke-q-fractional-distillation": ("4CH1-4.8", {"4CH1-4.7", "4CH1-4.8"}),
            "smoke-q-ionic-conduction": ("4CH1-1.43", {"4CH1-1.42", "4CH1-1.43"}),
            "smoke-q-acid-rain": ("4CH1-4.14", {"4CH1-4.14", "4CH1-4.16"}),
        }
        by_id = {}
        for entry in [{"id": u["id"], "cand": pf.rank(u["text"]), "max": None} for u in units]:
            by_id[entry["id"]] = entry["cand"]

        for qid, (top, trio) in expect_anchors.items():
            cand = by_id[qid]
            codes = {c["code"] for c in cand[:3]}
            report("C1 %s: top=%s weak=false" % (qid, top),
                   bool(cand) and cand[0]["code"] == top
                   and trio.issubset(codes | {c["code"] for c in cand})
                   and cand[0]["score"] >= t.WEAK_SCORE,
                   str([(c["code"], c["score"]) for c in cand[:3]]))

        phys = by_id["smoke-q-physics-newtons-cradle"]
        report("C2 REAL WPH11 physics question marks weak (out-of-curriculum control)",
               bool(phys) and phys[0]["score"] < t.WEAK_SCORE,
               str([(c["code"], c["score"]) for c in phys[:2]]))

        neg = by_id["smoke-q-fuels-sulfur-negative-control"]
        report("C3 4.15-style negative control also weak (never confident)",
               bool(neg) and neg[0]["score"] < t.WEAK_SCORE,
               str([(c["code"], c["score"]) for c in neg[:2]]))

        # ── positive control D: from-paper adapter ──
        print("- from-paper adapter")
        units_paper = t.from_paper(FIXTURES / "sample_paper.json")
        ids = [u["id"] for u in units_paper]
        report("D1 one unit per part + stemless MCQ (3 units)",
               len(units_paper) == 3 and ids == ["SYN-4CH1-P1-Q1:a", "SYN-4CH1-P1-Q1:b",
                                                  "SYN-4CH1-P1-Q2"], str(ids))
        report("D2 part units use self-contained renderedPrompt",
               all("separating mixtures" in u["text"] for u in units_paper[:2]))
        try:
            bad = json.loads((FIXTURES / "sample_paper.json").read_text(encoding="utf-8"))
            bad["tool"] = "something-else"
            p = tmp / "bad_paper.json"
            p.write_text(json.dumps(bad), encoding="utf-8")
            t.from_paper(p)
            report("D3 tool-name guard refuses non-atomizer files", False, "(no SystemExit)")
        except SystemExit:
            report("D3 tool-name guard refuses non-atomizer files", True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    if _failures:
        print("FAILED: %d problem(s):" % len(_failures))
        for f in _failures:
            print("  - %s" % f)
        return 1
    print("PASS: %d/%d checks (14 corruption classes caught, controls green)" % (_passed, _passed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
