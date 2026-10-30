#!/usr/bin/env python3
"""
official_examq_g9_tests.py — G9 gate tests: aggregation law + asset-byte guard.

Zero-network, zero-corpus test battery (CI-safe; runs as the corpus-gates step
`g9 aggregation + asset-byte guard tests`). Covers the F105 aggregation law
(official_examq_g9_semantics.py) end-to-end through the real CLIs and the F104
asset-byte guard (official_examq_asset_bytes.py):

  aggregation mixed outcomes (the seven required scenarios):
    1. required checks all pass            -> PASS (case, leg, overall)
    2. a required check fails              -> FAIL (never softened)
    3. a required check is NOT_RUN         -> REVIEW disposition, never PASS
    4. a check not applicable at the corpus layer, required + verified at the
       serving (bundles) layer             -> corpus case PASS with the
       delegation recorded; overall PASS only because the responsible legs
       themselves run green (and NOT PASS when they are missing)
    5. renderer unavailable                -> rendered leg NOT_RUN; overall
       gate cannot pass
    6. static legs pass, rendered leg missing -> overall gate cannot pass
    7. negative controls still detect mutations and cannot pass vacuously:
       - mutated frozen fact through the real bundles leg   -> FAIL, exit 1
       - mutated-fact control through the real corpus CLI   -> DETECTED
       - dead renderer through the real render check        -> NOT_RUN, exit 2
       - mojibake/corrupt/empty assets rejected by the guard
       - NOT_APPLICABLE without an explicit responsible layer is refused
       - publisher read-back mismatch is refused even when the API says 200

  asset regression fixtures: valid PNG/JPEG/GIF/PDF/SVG, CRC-corrupted PNG,
  truncated PNG, wrong signature, UTF-8-mojibake binary (C2 89 50 4E 47),
  empty file, dangling asset reference in a topic.json.

  F120 label-visibility contract (benchmark v3):
    - the shared label grammar/derivation law (semantics helpers) on attested
      and off-grammar shapes;
    - the static legs enforce the frozen part_labels samples + the
      labelled_parts census on BOTH layers (served field / derivation source);
    - a mutated SERVED label FAILs the bundles leg; the mutated-label control
      through the real corpus CLI DETECTs it while the original still derives;
    - the committed benchmark contract of record carries the v3 label shape.

Usage: python3 scripts/official_examq_g9_tests.py
Exit: 0 all green; 1 any failure.
"""
import base64
import json
import struct
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from official_examq_g9_semantics import (  # noqa: E402
    check as law_check, case_disposition, leg_disposition, overall_gate,
    LEG_STATIC_CORPUS, LEG_STATIC_BUNDLES, LEG_RENDERED,
    OUTCOME_PASS, OUTCOME_FAIL, OUTCOME_NOT_RUN, OUTCOME_NOT_APPLICABLE,
    REQ_REQUIRED, REQ_DELEGATED, REQ_EVIDENCE,
    LABEL_GRAMMAR_SRC, LABEL_GRAMMAR_RE, wrap_label_segments, label_from_offp_id,
    derive_label_from_part_number, bundle_label_of,
)
from official_examq_g9_static_check import (  # noqa: E402
    mutate_label, offp_part_number,
)
from official_examq_asset_bytes import (  # noqa: E402
    validate_asset_bytes, validate_asset_file, AssetByteError, publish_git_blob,
    scan_corpus, PNG_SIG,
)

STATIC = HERE / "official_examq_g9_static_check.py"
RENDER = HERE / "official_examq_g9_render_check.py"
AGGREGATE = HERE / "official_examq_g9_aggregate.py"

FAILURES = []


def check(name, ok, detail=""):
    print(("  PASS  " if ok else "  FAIL  ") + name + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        FAILURES.append(f"{name}: {detail}")


# ── fixture builders ─────────────────────────────────────────────────────────

def make_png(w=6, h=4, color=0):
    """A genuinely valid PNG (grayscale), built with real zlib streams."""
    raw = b""
    for y in range(h):
        raw += b"\x00" + bytes(((x * 7 + y * 13 + color) % 256) for x in range(w))
    def chunk(t, d):
        return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)
    return (PNG_SIG + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, color, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


def make_jpeg():
    """Structurally valid minimal JPEG: SOI + APP0 + DQT + SOF0 + DHT + SOS + EOI."""
    def seg(marker, payload):
        return bytes([0xFF, marker]) + struct.pack(">H", len(payload) + 2) + payload
    return (b"\xff\xd8"
            + seg(0xE0, b"JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00")
            + seg(0xDB, bytes([0x00] + [16] * 64))
            + seg(0xC0, bytes([0x08, 0x00, 0x02, 0x00, 0x04, 0x01, 0x00, 0x11, 0x00]))
            + seg(0xC4, bytes([0x00, 0x00]) + bytes(range(16)))
            + b"\xff\xda" + struct.pack(">H", 8) + b"\x01\x00\x00\x00\x00" + b"\x10\x82"
            + b"\xff\xd9")


def make_gif():
    return (b"GIF89a" + struct.pack("<HH", 4, 3) + bytes([0x80, 0x00, 0x00])
            + bytes([0, 0, 0, 255, 255, 255]) + b"\x2c" + struct.pack("<HHHH", 0, 0, 4, 3)
            + b"\x00" + b"\x02\x02\x44\x01\x00" + b"\x3b")


def make_pdf():
    return b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog >>\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF\n"


def make_svg():
    return b'<?xml version="1.0"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="4" height="4"></svg>'


FACT_SNIPPET = "The fuse wire melts at 5 amps."
SOL_SNIPPET = "R = 5/3 = 1.7 ohms"


def make_case(case_id="mini-1p", mutated=False):
    snip = FACT_SNIPPET[:-8] + "MUTATED-VALUE 999." if mutated else FACT_SNIPPET
    return {
        "id": case_id, "course": "igcse-physics-19",
        "topic_slug": "official-4ph1-1p-2023-06",
        "url_path": "/courses/igcse-physics-19/past-papers/x",
        "fact_parts": [{"part_id": "offp_2023-06_1p_1-a", "snippet": snip}],
        "solution_facts": [{"part_id": "offp_2023-06_1p_1-a", "snippet": SOL_SNIPPET}],
        "part_labels": [
            {"part_id": "offp_2023-06_1p_1-b-i", "label": "(b)(i)",
             "text_start": "The pencil has a weight of 0.16 N.", "kind": "labelled"},
            {"part_id": "offp_2023-06_1p_2", "label": None,
             "text_start": "State one hazard of damaged wiring.", "kind": "null"},
        ],
        "expected": {"questions": 1, "parts": 3, "marks_total": 6, "mcq_parts": 0,
                     "mcq_keyed": 0, "crop_assets": 1, "crop_required_stubs": 0,
                     "mark_points": 2, "crop_imgs_inlined": 1, "solutions": 3,
                     "labelled_parts": 2},
    }


CORPUS_TOPIC = {
    "questions": [{
        "id": "offq_2023-06_1p_1", "stem_md": "A fuse wire is used in a plug.",
        "total_marks": 6,
        "parts": [{
            "id": "offp_2023-06_1p_1-a", "part_number": "1(a)", "marks": 3,
            "problem_md": "A fuse wire is used in a plug.\n" + FACT_SNIPPET + " State the resistance.",
            "solution_md": SOL_SNIPPET,
            "assets": [{"kind": "crop", "path": "assets/asset_1_a_fig.png",
                        "rawUrl": "https://raw.example/asset_1_a_fig.png"}],
        }, {
            "id": "offp_2023-06_1p_1-b-i", "part_number": "1(b)(i)", "marks": 2,
            "problem_md": "The pencil has a weight of 0.16 N. State the moment.",
            "solution_md": "substitution into the formula",
        }, {
            "id": "offp_2023-06_1p_2", "part_number": "2", "marks": 1,
            "problem_md": "State one hazard of damaged wiring.",
            "solution_md": "any sensible hazard",
        }],
    }]
}

BUNDLE_TOPIC = {
    "slug": "official-4ph1-1p-2023-06",
    "questions": [{
        "id": "offq_2023-06_1p_1", "stemMd": "A fuse wire is used in a plug.", "totalMarks": 6,
        "parts": [{
            "id": "offp_2023-06_1p_1-a", "marks": 3,
            "sourcePaper": {"date": "June 2023", "number": "4PH1/1P", "questionPart": "(a)"},
            "problemMd": "A fuse wire is used in a plug.\n![fig](https://raw.example/asset_1_a_fig.png)\n"
                         + FACT_SNIPPET + " State the resistance.",
            "solutionMd": SOL_SNIPPET,
            "assets": [{"kind": "crop", "path": "igcse-physics-19/2023-06/4PH1-1P/assets/asset_1_a_fig.png",
                        "rawUrl": "https://raw.example/asset_1_a_fig.png"}],
        }, {
            "id": "offp_2023-06_1p_1-b-i", "marks": 2,
            "sourcePaper": {"date": "June 2023", "number": "4PH1/1P", "questionPart": "(b)(i)"},
            "problemMd": "The pencil has a weight of 0.16 N. State the moment.",
            "solutionMd": "substitution into the formula",
        }, {
            "id": "offp_2023-06_1p_2", "marks": 1,
            "sourcePaper": {"date": "June 2023", "number": "4PH1/1P", "questionPart": None},
            "problemMd": "State one hazard of damaged wiring.",
            "solutionMd": "any sensible hazard",
        }],
    }]
}


def build_world(tmp: Path, *, mutated=False, asset_bytes=None, dangling=False):
    """Fabricate a mini corpus + mini bundles + mini cases (real fixture files).

    The CASE is the frozen contract — it ALWAYS carries the original expectation.
    `mutated=True` mutates the SERVED BUNDLE text away from the frozen fact
    (the negative-control direction of record: harness detects the served text
    losing a frozen fact)."""
    corpus = tmp / "corpus"
    slice_dir = corpus / "igcse-physics-19" / "2023-06" / "4PH1-1P"
    (slice_dir / "assets").mkdir(parents=True)
    (slice_dir / "topic.json").write_text(json.dumps(CORPUS_TOPIC))
    topic = json.loads(json.dumps(CORPUS_TOPIC))
    if dangling:
        topic["questions"][0]["parts"][0]["assets"][0]["path"] = "assets/asset_MISSING.png"
    (slice_dir / "topic.json").write_text(json.dumps(topic))
    if asset_bytes is not None:
        (slice_dir / "assets" / "asset_1_a_fig.png").write_bytes(asset_bytes)
    else:
        (slice_dir / "assets" / "asset_1_a_fig.png").write_bytes(make_png())

    bundles_root = tmp / "bundles"
    bundles = bundles_root / "igcse-physics-19"
    bundles.mkdir(parents=True)
    bt = json.loads(json.dumps(BUNDLE_TOPIC))
    if mutated:
        bt["questions"][0]["parts"][0]["problemMd"] = bt["questions"][0]["parts"][0][
            "problemMd"].replace(FACT_SNIPPET, FACT_SNIPPET[:-8] + "MUTATED-VALUE 999.")
    (bundles / "official-papers.json").write_text(json.dumps([bt]))

    cases = tmp / "cases.json"
    cases.write_text(json.dumps({
        "benchmark_schema": "syllabai.g9-benchmark/1", "benchmark_version": 0,
        "note": "synthetic test world", "cases": [make_case()]}))  # frozen: original facts
    # the static check expects --bundles to point at the CONTENT root
    # (<content>/<course>/official-papers.json), matching apps/hub/content
    return corpus, bundles_root, cases


def run(*cmd, timeout=300, cwd=None):
    return subprocess.run([sys.executable, *map(str, cmd)], capture_output=True, text=True,
                          timeout=timeout, cwd=str(cwd) if cwd else None)


# ── Part A: the seven aggregation scenarios (law module + real CLIs) ────────

def test_scenario_1_all_required_pass():
    print("[1] required checks all pass -> PASS")
    req = lambda o: law_check(o, cid="c")
    case = case_disposition([req(OUTCOME_PASS), req(OUTCOME_PASS)])
    check("case disposition PASS", case == OUTCOME_PASS, case)
    leg = leg_disposition([{"disposition": case}])
    check("leg disposition PASS", leg == OUTCOME_PASS, leg)
    green = {l: {"overall": OUTCOME_PASS, "cases": []} for l in
             (LEG_STATIC_CORPUS, LEG_STATIC_BUNDLES, LEG_RENDERED)}
    ov, reasons = overall_gate(green)
    check("overall gate PASS", ov == OUTCOME_PASS, str(reasons))


def test_scenario_2_required_fail():
    print("[2] a required check fails -> FAIL")
    req = lambda o: law_check(o, cid="c")
    case = case_disposition([req(OUTCOME_PASS), req(OUTCOME_FAIL), req(OUTCOME_PASS)])
    check("case disposition FAIL", case == OUTCOME_FAIL, case)
    leg = leg_disposition([{"disposition": OUTCOME_PASS}, {"disposition": case}])
    check("leg disposition FAIL", leg == OUTCOME_FAIL, leg)
    legs = {l: {"overall": OUTCOME_PASS, "cases": []} for l in (LEG_STATIC_CORPUS, LEG_STATIC_BUNDLES)}
    legs[LEG_RENDERED] = {"overall": OUTCOME_FAIL, "cases": []}
    ov, _ = overall_gate(legs)
    check("overall gate FAIL (dominates everything)", ov == OUTCOME_FAIL, ov)


def test_scenario_3_required_not_run():
    print("[3] a required check is NOT_RUN -> REVIEW, never PASS")
    req = lambda o: law_check(o, cid="c")
    mixed = case_disposition([req(OUTCOME_PASS), req(OUTCOME_NOT_RUN)])
    check("mixed PASS+NOT_RUN case -> REVIEW", mixed == "REVIEW", mixed)
    check("mixed case is NEVER PASS", mixed != OUTCOME_PASS)
    pure = case_disposition([req(OUTCOME_NOT_RUN)])
    check("pure NOT_RUN case -> NOT_RUN", pure == OUTCOME_NOT_RUN, pure)
    leg = leg_disposition([{"disposition": OUTCOME_PASS}, {"disposition": mixed}])
    check("leg rises to REVIEW", leg == "REVIEW", leg)
    green = {l: {"overall": OUTCOME_PASS, "cases": []} for l in (LEG_STATIC_CORPUS, LEG_STATIC_BUNDLES)}
    green[LEG_RENDERED] = {"overall": "REVIEW", "cases": []}
    ov, reasons = overall_gate(green)
    check("overall REVIEW (missing evidence not masked)", ov == "REVIEW", str(reasons))
    check("blocking reason names the leg", any(LEG_RENDERED in r for r in reasons), str(reasons))


def test_scenario_4_na_delegated(tmp):
    print("[4] not-applicable at corpus, required + verified at the serving layer")
    corpus, bundles, cases = build_world(tmp / "s4")
    r = run(STATIC, "--corpus", corpus, "--cases", cases)
    check("corpus CLI exit 0", r.returncode == 0, r.stdout + r.stderr)
    receipt = json.loads((corpus / "g9-static-receipt.local.json").read_text())
    case = receipt["cases"][0]
    na = [c for c in case["checks"] if c["outcome"] == OUTCOME_NOT_APPLICABLE]
    check("figures-inlined-count recorded NOT_APPLICABLE", any(c["id"] == "figures-inlined-count" for c in na), str([c["id"] for c in na]))
    check("delegation names responsible legs", all("static-bundles" in c["responsibility"] and "rendered" in c["responsibility"] for c in na), str(na))
    check("corpus case PASS with delegation recorded", case["disposition"] == OUTCOME_PASS, case["disposition"])
    check("corpus receipt overall PASS", receipt["overall"] == OUTCOME_PASS, receipt["overall"])

    r2 = run(STATIC, "--bundles", bundles, "--cases", cases, cwd=tmp / "s4")
    check("bundles CLI exit 0", r2.returncode == 0, r2.stdout + r2.stderr)
    rcp = corpus / "g9-static-receipt-bundles.local.json"
    if not rcp.exists():  # bundles-mode receipts land in CWD; the run pinned cwd=tmp/s4
        rcp = tmp / "s4" / "g9-static-receipt-bundles.local.json"
    breceipt = json.loads(rcp.read_text())
    bfact = [c for c in breceipt["cases"][0]["checks"] if c["id"].startswith("fact:")][0]
    check("fact check REQUIRED and PASS at the serving layer",
          bfact["outcome"] == OUTCOME_PASS and bfact.get("requirement", REQ_REQUIRED) == REQ_REQUIRED, str(bfact))

    # overall PASS only because BOTH responsible legs are green
    agg_green = {LEG_STATIC_CORPUS: receipt, LEG_STATIC_BUNDLES: breceipt,
                 LEG_RENDERED: {"overall": OUTCOME_PASS, "cases": [], "validator_version": "synthetic"}}
    ov, reasons = overall_gate(agg_green)
    check("overall PASS with covered delegation", ov == OUTCOME_PASS, str(reasons))
    # counterfactual: bundles leg missing -> delegation uncovered -> NOT PASS
    agg_missing = {LEG_STATIC_CORPUS: receipt, LEG_STATIC_BUNDLES: None,
                   LEG_RENDERED: {"overall": OUTCOME_PASS, "cases": []}}
    ov2, reasons2 = overall_gate(agg_missing)
    check("overall NOT PASS when a responsible leg is missing", ov2 != OUTCOME_PASS, ov2)
    check("uncovered delegation reported", any("delegated" in r or "NOT_RUN" in r for r in reasons2), str(reasons2))
    # counterfactual: bundles leg present but NOT_RUN -> NOT PASS
    agg_blocked = dict(agg_missing, static_bundles={"overall": OUTCOME_NOT_RUN, "cases": []})
    ov3, _ = overall_gate(agg_blocked)
    check("overall NOT PASS when a responsible leg is NOT_RUN", ov3 != OUTCOME_PASS, ov3)


def test_scenario_5_renderer_unavailable():
    print("[5] renderer unavailable -> rendered leg cannot pass")
    green = {LEG_STATIC_CORPUS: {"overall": OUTCOME_PASS, "cases": []},
             LEG_STATIC_BUNDLES: {"overall": OUTCOME_PASS, "cases": []}}
    # the real blocked-render receipt shape (from the dead-renderer control)
    blocked = {"overall": OUTCOME_NOT_RUN, "renderer": {"class": None},
               "cases": [{"case_id": "x", "disposition": OUTCOME_NOT_RUN,
                          "checks": [{"id": "renderer-available", "outcome": OUTCOME_NOT_RUN,
                                      "requirement": REQ_REQUIRED, "detail": "unreachable"}]}]}
    legs = dict(green, rendered=blocked)
    ov, reasons = overall_gate(legs)
    check("overall NOT PASS", ov != OUTCOME_PASS, ov)
    check("overall REVIEW with reason", ov == "REVIEW" and any(LEG_RENDERED in r for r in reasons), str(reasons))


def test_scenario_6_static_pass_rendered_missing():
    print("[6] static legs pass, rendered leg missing -> overall cannot pass")
    legs = {LEG_STATIC_CORPUS: {"overall": OUTCOME_PASS, "cases": []},
            LEG_STATIC_BUNDLES: {"overall": OUTCOME_PASS, "cases": []},
            LEG_RENDERED: None}
    ov, reasons = overall_gate(legs)
    check("overall NOT PASS (missing leg)", ov != OUTCOME_PASS, ov)
    check("reason names the missing leg", any(LEG_RENDERED in r for r in reasons), str(reasons))


# ── Part A-F120: the label-visibility contract (benchmark v3) ────────────────

def test_f120_label_contract(tmp):
    print("[F120] the printed-label contract: law, both static layers, controls")

    # a. the shared derivation/grammar law (single source in semantics)
    lab, st = label_from_offp_id("offp_2023-06_2p_1-b-i")
    check("id slug derives (b)(i)", lab == "(b)(i)" and st == "labelled", f"{lab!r} {st!r}")
    lab2, st2 = label_from_offp_id("offp_2018-06_01_1")
    check("path-less id is honestly null", lab2 is None and st2 == "pathless", f"{lab2!r} {st2!r}")
    lab3, st3 = label_from_offp_id("offp_weird")
    check("off-grammar id never guesses", lab3 is None and st3 == "off-grammar", f"{lab3!r} {st3!r}")
    check("segment over 5 chars refused", wrap_label_segments(["abcdef"]) is None)
    check("4+ group labels refused by grammar", not LABEL_GRAMMAR_RE.match("(a)(b)(c)(d)"))
    check("grammar source is JS-compatible (no python-only syntax)",
          "(?P<" not in LABEL_GRAMMAR_SRC and "\\\\" not in LABEL_GRAMMAR_SRC, LABEL_GRAMMAR_SRC)
    check("part_number tail derivation (1(b)(i) -> (b)(i))",
          derive_label_from_part_number("1(b)(i)") == "(b)(i)")
    check("bare part_number derives None", derive_label_from_part_number("2") is None)
    check("off-grammar tail derives None (never invented)",
          derive_label_from_part_number("1(a)(b)(c)(d)") is None and derive_label_from_part_number("1 a i") is None)
    check("mutate_label produces a plausible-but-wrong label",
          mutate_label("(b)(i)") == "(z)(i)" and mutate_label("(b)(i)") != "(b)(i)")
    check("offp_part_number mapping (shared with the controls)",
          offp_part_number("offp_2023-06_2p_12-b-i") == "12(b)(i)")

    # b. both static layers enforce the frozen samples + census
    corpus, bundles, cases = build_world(tmp / "f120")
    r1 = run(STATIC, "--corpus", corpus, "--cases", cases)
    check("corpus leg green with label contract", r1.returncode == 0, r1.stdout[-400:] + r1.stderr[-200:])
    crec = json.loads((corpus / "g9-static-receipt.local.json").read_text())
    cchecks = crec["cases"][0]["checks"]
    check("corpus label check present + PASS",
          any(c["id"] == "label:offp_2023-06_1p_1-b-i" and c["outcome"] == OUTCOME_PASS for c in cchecks),
          str([c["id"] for c in cchecks]))
    check("corpus null-label check present + PASS",
          any(c["id"] == "label-null:offp_2023-06_1p_2" and c["outcome"] == OUTCOME_PASS for c in cchecks))
    check("corpus labels-field-count is delegated (served-field property)",
          any(c["id"] == "labels-field-count" and c["outcome"] == OUTCOME_NOT_APPLICABLE
              and "static-bundles" in c.get("responsibility", "") for c in cchecks))
    r2 = run(STATIC, "--bundles", bundles, "--cases", cases, cwd=tmp / "f120")
    check("bundles leg green with label contract", r2.returncode == 0, r2.stdout[-400:] + r2.stderr[-200:])
    brcp = tmp / "f120" / "g9-static-receipt-bundles.local.json"
    brec = json.loads(brcp.read_text())
    bchecks = brec["cases"][0]["checks"]
    check("bundles labels-field-count REQUIRED + PASS",
          any(c["id"] == "labels-field-count" and c["outcome"] == OUTCOME_PASS
              and c.get("requirement", REQ_REQUIRED) == REQ_REQUIRED for c in bchecks))
    check("bundles served-label check pins field AND id slug",
          any(c["id"] == "label:offp_2023-06_1p_1-b-i" and c["outcome"] == OUTCOME_PASS for c in bchecks))
    check("bundles null-class check PASS",
          any(c["id"] == "label-null:offp_2023-06_1p_2" and c["outcome"] == OUTCOME_PASS for c in bchecks))

    # c. a mutated SERVED label FAILs the bundles leg (the class the gate now sees)
    bundles_m = tmp / "f120m"
    bundles_m.mkdir()
    bt = json.loads(json.dumps(BUNDLE_TOPIC))
    bt["questions"][0]["parts"][1]["sourcePaper"]["questionPart"] = "(z)(i)"
    (bundles_m / "igcse-physics-19").mkdir()
    (bundles_m / "igcse-physics-19" / "official-papers.json").write_text(json.dumps([bt]))
    r3 = run(STATIC, "--bundles", bundles_m, "--cases", cases, cwd=tmp / "f120m")
    check("mutated served label FAILs the bundles leg (exit 1)", r3.returncode == 1, r3.stdout[-300:])
    mrec = json.loads((tmp / "f120m" / "g9-static-receipt-bundles.local.json").read_text())
    mchk = [c for c in mrec["cases"][0]["checks"] if c["id"] == "label:offp_2023-06_1p_1-b-i"][0]
    check("mutated label recorded as FAIL naming the drift", mchk["outcome"] == OUTCOME_FAIL
          and "(z)(i)" in mchk["detail"], str(mchk))

    # d. mutated-label control through the real corpus CLI -> DETECTED (exit 0)
    ctl_out = tmp / "f120" / "mutated-label-control.receipt.json"
    r4 = run(STATIC, "--corpus", corpus, "--cases", cases, "--negative-control-label",
             "--receipt-out", ctl_out)
    check("mutated-label control DETECTED", r4.returncode == 0 and "DETECTED" in r4.stdout,
          r4.stdout + r4.stderr)
    lrec = json.loads(ctl_out.read_text()) if ctl_out.exists() else {}
    check("label control receipt honest (status DETECTED, control=mutated-label)",
          lrec.get("status") == "DETECTED" and lrec.get("control") == "mutated-label", str(lrec))

    # e. the committed contract of record carries the v3 label shape
    committed = HERE.parent / "Official-ExamQuestion" / "benchmark" / "cases.json"
    if committed.exists():
        cb = json.loads(committed.read_text())
        check("committed contract is benchmark_version 3", cb.get("benchmark_version") == 3,
              str(cb.get("benchmark_version")))
        bad = [c["id"] for c in cb["cases"]
               if not c.get("part_labels") or "labelled_parts" not in c.get("expected", {})]
        check("every case freezes part_labels + labelled_parts", not bad, str(bad))
        bads = [(c["id"], s.get("part_id")) for c in cb["cases"] for s in c.get("part_labels") or []
                if s.get("label") and not LABEL_GRAMMAR_RE.match(s["label"])]
        check("every frozen labelled sample is on the attested grammar", not bads, str(bads))
        drift = []
        for c in cb["cases"]:
            for s in c.get("part_labels") or []:
                id_lab, state = label_from_offp_id(s["part_id"])
                if s.get("label"):
                    if id_lab != s["label"]:
                        drift.append((c["id"], s["part_id"], "label vs id slug"))
                elif state != "pathless":
                    drift.append((c["id"], s["part_id"], f"null sample but id state {state}"))
        check("frozen samples resolve on their own identity (G-E6 pin)", not drift, str(drift[:3]))
        census_bad = [c["id"] for c in cb["cases"]
                      if sum(1 for s in c.get("part_labels") or [] if s.get("label")) < 1]
        check("every case freezes at least one labelled sample", not census_bad, str(census_bad))
    else:
        check("committed contract present", False, f"missing: {committed}")


def test_scenario_7_negative_controls(tmp):
    print("[7] negative controls detect mutations; vacuous passes impossible")

    # 7a. mutated frozen fact through the real bundles leg -> FAIL, exit 1
    corpus, bundles, cases = build_world(tmp / "s7a", mutated=True)
    r = run(STATIC, "--bundles", bundles, "--cases", cases, cwd=tmp / "s7a")
    check("mutated fact FAILs the bundles leg (exit 1)", r.returncode == 1, r.stdout[-400:])
    receipt = json.loads((tmp / "s7a" / "g9-static-receipt-bundles.local.json").read_text())
    fact = [c for c in receipt["cases"][0]["checks"] if c["id"].startswith("fact:")][0]
    check("mutation recorded as FAIL on the fact check", fact["outcome"] == OUTCOME_FAIL, str(fact))
    check("leg overall FAIL", receipt["overall"] == OUTCOME_FAIL, receipt["overall"])

    # 7b. mutated-fact control through the real corpus CLI -> DETECTED (exit 0)
    corpus2, _, cases2 = build_world(tmp / "s7b")
    ctl_out = tmp / "s7b" / "mutated-fact-control.receipt.json"
    r2 = run(STATIC, "--corpus", corpus2, "--cases", cases2, "--negative-control",
             "--receipt-out", ctl_out)
    check("mutated-fact control DETECTED", r2.returncode == 0 and "DETECTED" in r2.stdout,
          r2.stdout + r2.stderr)
    creceipt = json.loads(ctl_out.read_text()) if ctl_out.exists() else {}
    check("control receipt honest (status DETECTED)", creceipt.get("status") == "DETECTED", str(creceipt))

    # 7c. dead renderer through the real render check -> all NOT_RUN, exit 2
    r3 = run(RENDER, "--base-url", "http://127.0.0.1:9", "--cases", cases,
             "--out-dir", tmp / "s7c", timeout=120)
    check("dead renderer exits 2 (blocked)", r3.returncode == 2, r3.stdout[-300:] + r3.stderr[-300:])
    rr = json.loads((tmp / "s7c" / "g9-render-receipt.json").read_text())
    check("dead renderer overall NOT_RUN", rr["overall"] == OUTCOME_NOT_RUN, rr["overall"])
    check("dead renderer never PASS", rr["overall"] != OUTCOME_PASS)
    check("dead renderer recorded with renderer class None", rr["renderer"]["class"] is None)

    # 7d. asset guard: mojibake of a valid PNG (the F104 signature) is refused
    png = make_png()
    moji = png.decode("latin-1").encode("utf-8")
    check("fixture sanity: mojibake starts C2 89 50 4E 47", moji[:5].hex() == "c289504e47", moji[:5].hex())
    try:
        validate_asset_bytes(moji, "asset_1_a_fig.png")
        check("mojibake rejected", False, "no exception raised")
    except AssetByteError as exc:
        check("mojibake rejected", True)
        check("mojibake error is actionable (names class + recovery)",
              "UTF-8 mojibake" in str(exc) and "C2 89 50 4E 47" in str(exc) and "base64" in str(exc), str(exc))

    # 7e. NOT_APPLICABLE without an explicit responsible layer is refused
    try:
        law_check(OUTCOME_NOT_APPLICABLE, cid="silent-na")
        check("silent NOT_APPLICABLE refused", False, "no exception")
    except ValueError:
        check("silent NOT_APPLICABLE refused", True)

    # 7f. publisher read-back mismatch refused even though the API returned 200
    good_gh = {"calls": [], "bodies": []}
    pushed = {}

    def fake_gh(path, method="GET", body=None, token=None):
        good_gh["calls"].append((method, path))
        good_gh["bodies"].append(body)
        if method == "POST" and path.endswith("/git/blobs"):
            data = base64.b64decode(body["content"])
            pushed["bytes"] = data
            pushed["sha"] = "b_" + __import__("hashlib").sha256(data).hexdigest()
            return {"sha": pushed["sha"]}
        if method == "GET" and "/git/blobs/" in path:
            return {"encoding": "base64", "content": base64.b64encode(pushed["bytes"]).decode()}
        raise AssertionError(f"unexpected call {method} {path}")

    res = publish_git_blob("SyllabAI/fake", "assets/asset_1_a_fig.png", png, "t", gh=fake_gh)
    check("publisher happy path read-back verified", res["readback_verified"] is True, str(res))
    posts = [(m, p) for (m, p), b in zip(good_gh["calls"], good_gh["bodies"]) if m == "POST"]
    post_bodies = [b for b in good_gh["bodies"] if b]
    check("publisher always base64 (never text encoding)",
          post_bodies and all(b.get("encoding") == "base64" for b in post_bodies), str(post_bodies))
    check("exactly one blob POST", len(posts) == 1, str(good_gh["calls"]))
    check("read-back GET performed", any("GET" == m for m, _ in good_gh["calls"]), str(good_gh["calls"]))

    lying = {"calls": []}
    def lying_gh(path, method="GET", body=None, token=None):
        lying["calls"].append((method, path))
        if method == "POST" and path.endswith("/git/blobs"):
            data = base64.b64decode(body["content"])
            return {"sha": "b_liar"}
        if method == "GET" and "/git/blobs/" in path:
            return {"encoding": "base64", "content": base64.b64encode(make_png(color=99)).decode()}
        raise AssertionError("unexpected")
    try:
        publish_git_blob("SyllabAI/fake", "assets/asset_1_a_fig.png", png, "t", gh=lying_gh)
        check("read-back mismatch refused", False, "no exception")
    except AssetByteError as exc:
        check("read-back mismatch refused", "DOES NOT MATCH SOURCE BYTES" in str(exc), str(exc))

    refused = {"calls": []}
    def refused_gh(path, method="GET", body=None, token=None):
        refused["calls"].append((method, path))
        return {"sha": "b_never"}
    try:
        publish_git_blob("SyllabAI/fake", "assets/asset_1_a_fig.png", moji, "t", gh=refused_gh)
        check("invalid bytes never pushed", False, "no exception")
    except AssetByteError:
        check("invalid bytes never pushed (guard fires before any POST)", len(refused["calls"]) == 0, str(refused["calls"]))


# ── Part B: asset-byte guard regression fixtures ────────────────────────────

def test_asset_formats(tmp):
    print("[B1] valid asset formats validate; corruptions are caught")
    fixtures = [("x.png", make_png(), "png"), ("x.jpg", make_jpeg(), "jpeg"),
                ("x.gif", make_gif(), "gif"), ("x.pdf", make_pdf(), "pdf"),
                ("x.svg", make_svg(), "svg")]
    for name, data, fmt in fixtures:
        got = validate_asset_bytes(data, name)
        check(f"valid {fmt} accepted", got == fmt, got)
    # corruptions
    png = make_png()
    bad_crc = bytearray(png); bad_crc[64] ^= 0xFF
    corruptions = [
        ("CRC-corrupted PNG", bytes(bad_crc)),
        ("truncated PNG", png[:30]),
        ("wrong signature (PNG body, GIF head)", b"GIF89a" + png[8:]),
        ("empty file", b""),
        ("text garbage", b"this is definitely not an image"),
    ]
    for name, data in corruptions:
        try:
            validate_asset_bytes(data, "bad.png")
            check(f"{name} rejected", False, "no exception")
        except AssetByteError as exc:
            check(f"{name} rejected", True)
            check(f"{name} error names the asset path", "bad.png" in str(exc), str(exc))
    # extension pinning: JPEG bytes in a .png file must NOT pass
    (tmp / "jpeg-as-png.png").write_bytes(make_jpeg())
    try:
        validate_asset_file(tmp / "jpeg-as-png.png")
        check("jpeg bytes in .png file refused", False, "no exception")
    except AssetByteError as exc:
        check("jpeg bytes in .png file refused", "format mismatch" in str(exc), str(exc))
    # HTTP 200 proves nothing: the guard is byte-based, never URL-based
    check("guard has no URL/HTTP input path",
          "url" not in validate_asset_bytes.__code__.co_varnames, "signature changed")


def test_corpus_scan(tmp):
    print("[B2] corpus scan: dangling references + corrupt bytes are actionable")
    # dangling reference
    corpus, bundles, cases = build_world(tmp / "scan1", dangling=True)
    ok, report = scan_corpus(corpus)
    check("dangling scan reports failure", ok is False, str(report["errors"]))
    check("dangling scan names the missing asset", any("asset_MISSING.png" in e["path"] and "dangling" in e["reason"] for e in report["errors"]), str(report["errors"]))
    # mojibake file on disk
    corpus2, _, _ = build_world(tmp / "scan2", asset_bytes=make_png().decode("latin-1").encode("utf-8"))
    ok2, report2 = scan_corpus(corpus2)
    check("mojibake on disk rejected by scan", ok2 is False and any("mojibake" in e["reason"] for e in report2["errors"]), str(report2["errors"]))
    # clean world
    corpus3, _, _ = build_world(tmp / "scan3")
    ok3, report3 = scan_corpus(corpus3)
    check("clean world scans ok", ok3 is True and report3["error_count"] == 0, str(report3))
    check("clean world file census", report3["asset_files_checked"] == 1, str(report3))


def test_end_to_end_aggregate(tmp):
    print("[B3] end-to-end: static legs + aggregate CLI reproduce the seven laws")
    corpus, bundles, cases = build_world(tmp / "e2e")
    r1 = run(STATIC, "--corpus", corpus, "--cases", cases)
    r2 = run(STATIC, "--bundles", bundles, "--cases", cases, cwd=tmp / "e2e")
    check("both static legs green", r1.returncode == 0 and r2.returncode == 0,
          (r1.stdout + r2.stdout)[-500:] + (r1.stderr + r2.stderr)[-500:])
    rcpt_corpus = corpus / "g9-static-receipt.local.json"
    rcpt_bundles = corpus / "g9-static-receipt-bundles.local.json"
    if not rcpt_bundles.exists():
        rcpt_bundles = tmp / "e2e" / "g9-static-receipt-bundles.local.json"
    render_receipt = tmp / "e2e" / "g9-render-receipt.json"
    render_receipt.write_text(json.dumps({"overall": OUTCOME_PASS, "cases": [], "validator_version": "synthetic"}))
    agg = tmp / "e2e" / "g9-aggregate.receipt.json"
    r3 = run(AGGREGATE, "--static-corpus", rcpt_corpus, "--static-bundles", rcpt_bundles,
             "--render", render_receipt, "--out", agg)
    check("aggregate exit 0 (all legs green)", r3.returncode == 0, r3.stdout + r3.stderr)
    areceipt = json.loads(agg.read_text())
    check("aggregate receipt overall PASS", areceipt["overall"] == OUTCOME_PASS, str(areceipt))
    # missing rendered leg blocks the CLI too
    r4 = run(AGGREGATE, "--static-corpus", rcpt_corpus, "--static-bundles", rcpt_bundles, "--out", agg)
    check("aggregate refuses PASS without the rendered leg", r4.returncode == 1, r4.stdout)
    a4 = json.loads(agg.read_text())
    check("aggregate receipt honest (REVIEW + reason)", a4["overall"] == "REVIEW" and a4["blocking_reasons"], str(a4["overall"]) + str(a4["blocking_reasons"])[:200])
    # a FAIL leg propagates
    render_receipt.write_text(json.dumps({"overall": OUTCOME_FAIL, "cases": []}))
    r5 = run(AGGREGATE, "--static-corpus", rcpt_corpus, "--static-bundles", rcpt_bundles,
             "--render", render_receipt, "--out", agg)
    check("aggregate propagates FAIL", r5.returncode == 1 and json.loads(agg.read_text())["overall"] == OUTCOME_FAIL, r5.stdout)


def main():
    print("G9 gate tests — aggregation law + asset-byte guard")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        test_scenario_1_all_required_pass()
        test_scenario_2_required_fail()
        test_scenario_3_required_not_run()
        test_scenario_4_na_delegated(tmp)
        test_scenario_5_renderer_unavailable()
        test_scenario_6_static_pass_rendered_missing()
        test_scenario_7_negative_controls(tmp)
        test_f120_label_contract(tmp)
        test_asset_formats(tmp)
        test_corpus_scan(tmp)
        test_end_to_end_aggregate(tmp)
    if FAILURES:
        print(f"\n{len(FAILURES)} FAILURE(S):")
        for f in FAILURES:
            print("  -", f)
        sys.exit(1)
    print("\nALL G9 GATE TESTS GREEN")


if __name__ == "__main__":
    main()
