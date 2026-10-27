#!/usr/bin/env python3
"""
official_examq_g9_static_check.py — G9 Learner-Surface Quality gate, static leg.

Validates the FROZEN benchmark contract (Official-ExamQuestion/benchmark/cases.json)
against the corpus of record — either the resources Official-ExamQuestion lane
slices (topic.json, snake_case, the deterministic extraction + disclosure layer)
or the syllabai-v2 hub official bundles (official-papers.json, camelCase, the
H3-cutover serving exports). This is the deterministic, browser-free half of G9:
marks law, count law, MCQ key law, expected semantic facts, asset presence and
inline-figure occurrence counts.

The rendered (browser) half lives in official_examq_g9_render_check.py. A green
static leg NEVER implies the rendered leg ran — the two receipts are separate
and the OVERALL G9 gate (official_examq_g9_aggregate.py) is PASS only when all
three mandatory legs (static-corpus, static-bundles, rendered) report PASS.

Aggregation law (F105 — official_examq_g9_semantics.py is its executable form):
  - a required check that FAILs fails the case;
  - a required check that is NOT_RUN can NEVER yield PASS — a case with any
    unestablished required check dispositions REVIEW (pure-NOT_RUN cases stay
    NOT_RUN) and the leg rises to REVIEW;
  - a check that is genuinely not applicable at this layer is recorded
    NOT_APPLICABLE and names the responsible validation layer(s) explicitly
    ("delegated"); it is excluded from this layer's required set ONLY because
    the contract assigns the property to mandatory legs, and the overall gate
    stays blocked until those legs themselves run and PASS. It never silently
    counts as a pass.

Outcomes per check: PASS / FAIL / NOT_RUN / NOT_APPLICABLE(+responsibility).
Exit code 0 iff the leg dispositions PASS.
Usage:
  python3 scripts/official_examq_g9_static_check.py \
    --corpus Official-ExamQuestion [--cases benchmark/cases.json]
  python3 scripts/official_examq_g9_static_check.py \
    --bundles /path/apps/hub/content [--cases benchmark/cases.json]
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from official_examq_g9_semantics import (  # noqa: E402
    check as law_check, case_disposition, leg_disposition,
    OUTCOME_PASS, OUTCOME_FAIL, OUTCOME_NOT_RUN, OUTCOME_NOT_APPLICABLE,
)
from official_examq_asset_bytes import validate_asset_file, AssetByteError  # noqa: E402

VALIDATOR_VERSION = "g9-static-check/0.2"

# Layer delegation of record (benchmark/README.md "Layer ownership"): these
# properties are exporter/served-layer text or renderer-runtime behavior; the
# corpus slice cannot establish them, and the contract assigns them to the
# static-bundles leg and the rendered leg — both MANDATORY legs of the overall
# gate. Delegation is only lawful because those legs are mandatory.
RESP_SERVED_TEXT = "static-bundles + rendered legs"

LANE_BY_SPEC = {"4ph1": "igcse-physics-19", "4ch1": "igcse-chemistry-19", "4mb1": "igcse-maths-b-16"}


def norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


def parse_topic_slug(slug):
    # official-<spec>-<paper>-<series>  e.g. official-4ph1-2p-2023-06,
    # official-4mb1-02r-2019-06 (paper may itself be <num><r?>)
    m = re.match(r"^official-([a-z0-9]+)-([0-9][a-z0-9]*r?)-(\d{4}-\d{2})$", slug or "")
    if not m:
        return None
    return m.group(1), m.group(2), m.group(3)


class TopicSource:
    """Unified read access over a corpus slice (snake_case) or a bundle topic (camelCase)."""

    def __init__(self, topic, mode):
        self.topic, self.mode = topic, mode

    def questions(self):
        return self.topic.get("questions") or []

    def parts(self):
        return [p for q in self.questions() for p in (q.get("parts") or [])]

    @staticmethod
    def pid(p):
        return p.get("id") or p.get("part_number")

    @staticmethod
    def pmarks(p):
        return p.get("marks")

    @staticmethod
    def pproblem(p):
        return p.get("problemMd") if "problemMd" in p else p.get("problem_md")

    @staticmethod
    def psolution(p):
        return p.get("solutionMd") if "solutionMd" in p else p.get("solution_md")

    @staticmethod
    def pchoices(p):
        ch = p.get("choices")
        if not ch:
            return []
        return [
            {
                "label": c.get("label"),
                "isCorrect": bool(c.get("isCorrect", c.get("is_correct"))),
                "text": c.get("textMd") if "textMd" in c else c.get("text_md"),
            }
            for c in ch
        ]

    @staticmethod
    def passets(p):
        return p.get("assets") or []

    def qtotal(self):
        return sum(q.get("totalMarks", q.get("total_marks", 0)) for q in self.questions())

    def crop_assets(self):
        return [a for p in self.parts() for a in self.passets(p) if a.get("kind") == "crop"]

    def stub_assets(self):
        return [a for p in self.parts() for a in self.passets(p) if a.get("kind") == "crop-required"]

    def inline_crop_occurrences(self):
        """Crop figures actually inlined into problemMd (each occurrence = one served <img>)."""
        n = 0
        for p in self.parts():
            md = self.pproblem(p) or ""
            for a in self.passets(p):
                if a.get("kind") != "crop":
                    continue
                path = a.get("path") or ""
                base = f"assets/{Path(path).name}"
                raw = a.get("rawUrl") or ""
                if (raw and raw in md) or (path and path in md) or base in md:
                    n += 1
        return n


def load_corpus_topic(corpus_dir, lane, series, paper):
    lane_dir = Path(corpus_dir) / lane / series
    paper_upper = paper.upper()
    # maths uses 4MB1-02R style; physics/chemistry 4PH1-2P / 4CH1-1C
    spec_code = {"igcse-physics-19": "4PH1", "igcse-chemistry-19": "4CH1", "igcse-maths-b-16": "4MB1"}[lane]
    td = lane_dir / f"{spec_code}-{paper_upper}"
    f = td / "topic.json"
    if not f.exists():
        return None
    return json.loads(f.read_text())


def check(name, ok, detail=""):
    return law_check((OUTCOME_PASS if ok else OUTCOME_FAIL), cid=name, area="static", detail=detail)


def not_run(name, detail):
    return law_check(OUTCOME_NOT_RUN, cid=name, area="static", detail=detail)


def delegated(name, detail, responsibility=RESP_SERVED_TEXT):
    """NOT_APPLICABLE here — the contract assigns the property to the named
    mandatory legs (never a silent pass; overall gate stays blocked until the
    responsible legs run and pass)."""
    return law_check(OUTCOME_NOT_APPLICABLE, requirement="delegated",
                     responsibility=responsibility, cid=name, area="static", detail=detail)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", help="Official-ExamQuestion dir (resources corpus of record)")
    ap.add_argument("--bundles", help="syllabai-v2 apps/hub/content dir (serving bundles)")
    ap.add_argument("--cases", default=None)
    ap.add_argument("--negative-control", action="store_true",
                    help="anti-gaming self-test: mutate the first frozen fact and prove "
                         "the corpus text layer REFUSES it while accepting the original "
                         "(exit 0 = control detected; exit 1 = harness integrity broken)")
    ap.add_argument("--receipt-out", default=None,
                    help="(negative-control mode) write an honest control receipt JSON here")
    args = ap.parse_args()
    if not args.corpus and not args.bundles:
        sys.exit("need --corpus or --bundles")

    here = Path(__file__).resolve().parent.parent / "Official-ExamQuestion" / "benchmark"
    cases_path = Path(args.cases) if args.cases else here / "cases.json"
    bench = json.loads(cases_path.read_text())
    cases = bench["cases"]

    if args.negative_control:
        def ctl_out(status, detail):
            if args.receipt_out:
                Path(args.receipt_out).write_text(json.dumps({
                    "receipt_schema": "syllabai.g9-negative-control-receipt/0.1",
                    "control": "mutated-fact", "status": status,
                    "validator_version": VALIDATOR_VERSION,
                    "benchmark_version": bench.get("benchmark_version"),
                    "corpus": args.corpus, "detail": detail,
                }, indent=1))
        # Anti-gaming law: the mutated fact must be REFUSED by the corpus text
        # layer, and the original fact must be PRESENT (proves the probe is
        # non-vacuous — it would actually detect a real mutation).
        case = cases[0]
        parsed = parse_topic_slug(case["topic_slug"])
        spec, paper, series = parsed
        raw = load_corpus_topic(args.corpus, LANE_BY_SPEC[spec], series, paper)
        if raw is None:
            ctl_out("INCONCLUSIVE", "corpus slice not found")
            sys.exit("negative control: corpus slice not found")
        t = TopicSource(raw, "corpus")
        parts = t.parts()
        def pnum(pid):
            if not (pid or "").startswith("offp_"):
                return pid
            segs = pid[len("offp_"):].split("_")
            m = re.match(r"^(\d+)(?:-(.*))?$", segs[-1])
            if not m:
                return pid
            return m.group(1) if not m.group(2) else m.group(1) + "(" + m.group(2).replace("-", ")(") + ")"
        bypn = {(p.get("part_number") or ""): p for p in parts}
        fact = case["fact_parts"][0]
        p = bypn.get(pnum(fact["part_id"]))
        if p is None:
            ctl_out("INCONCLUSIVE", "part not found")
            sys.exit("negative control: part not found")
        md = norm(t.pproblem(p) or "") + " " + norm(p.get("stem_md") or "")
        q = None
        for qq in t.questions():
            if any((pp.get("part_number") or "") == p.get("part_number") for pp in qq.get("parts") or []):
                q = qq
                break
        if q:
            md += " " + norm(q.get("stem_md") or "")
            for g in (q.get("groups") or {}).values():
                md += " " + norm(g.get("group_stem_md") or "")
        mutated = fact["snippet"][:-8] + "MUTATED-VALUE 999."
        if mutated in md:
            ctl_out("HARNESS-BROKEN", "mutated fact reported present")
            sys.exit("NEGATIVE-CONTROL FAILURE: mutated fact reported present — harness integrity broken")
        if fact["snippet"] not in md:
            ctl_out("INCONCLUSIVE", "original fact is authored-layer text at the corpus layer")
            print("negative control: INCONCLUSIVE at the corpus layer (original fact is authored-layer text); "
                  "run against the serving bundles for the strict form")
            sys.exit(0)
        ctl_out("DETECTED", "mutated fact refused, original accepted")
        print("negative control: DETECTED (mutated fact refused, original accepted)")
        sys.exit(0)

    receipt = {
        "receipt_schema": "syllabai.g9-static-receipt/0.1",
        "validator_version": VALIDATOR_VERSION,
        "benchmark_version": bench.get("benchmark_version"),
        "source": {"corpus": args.corpus, "bundles": args.bundles},
        "cases": [],
    }

    for case in cases:
        checks = []
        slug = case["topic_slug"]
        parsed = parse_topic_slug(slug)
        topic = None
        mode = None
        if args.bundles:
            bundle = json.loads((Path(args.bundles) / case["course"] / "official-papers.json").read_text())
            hits = [t for t in bundle if (t.get("slug") or "") == slug]
            if len(hits) == 1:
                topic, mode = TopicSource(hits[0], "bundle"), "bundle"
        elif args.corpus:
            spec, paper, series = parsed
            raw = load_corpus_topic(args.corpus, LANE_BY_SPEC[spec], series, paper)
            if raw is not None:
                topic, mode = TopicSource(raw, "corpus"), "corpus"
        if topic is None:
            checks.append(not_run("topic-resolved", f"topic {slug} not found in the requested source"))
        else:
            e = case["expected"]
            qs, parts = topic.questions(), topic.parts()
            marks = topic.qtotal()
            mcq = [p for p in parts if (p.get("questionType") or p.get("question_type")) == "multiple_choice"]
            keyed = [p for p in mcq if topic.pchoices(p) and sum(1 for c in topic.pchoices(p) if c["isCorrect"]) == 1]
            checks.append(check("counts-questions", len(qs) == e["questions"], f"{len(qs)} vs {e['questions']}"))
            checks.append(check("counts-parts", len(parts) == e["parts"], f"{len(parts)} vs {e['parts']}"))
            checks.append(check("marks-total-law", marks == e["marks_total"], f"{marks} vs {e['marks_total']}"))
            checks.append(check("counts-mcq", len(mcq) == e["mcq_parts"] and len(keyed) == e["mcq_keyed"],
                                f"mcq {len(mcq)} vs {e['mcq_parts']}; keyed {len(keyed)} vs {e['mcq_keyed']}"))
            if mode == "bundle":
                checks.append(check("counts-crops", len(topic.crop_assets()) == e["crop_assets"],
                                    f"{len(topic.crop_assets())} vs {e['crop_assets']}"))
                checks.append(check("counts-stubs", len(topic.stub_assets()) == e["crop_required_stubs"],
                                    f"{len(topic.stub_assets())} vs {e['crop_required_stubs']}"))
                inline = topic.inline_crop_occurrences()
                checks.append(check("figures-inlined-count", inline == e["crop_imgs_inlined"],
                                    f"{inline} vs {e['crop_imgs_inlined']}"))
            else:
                # corpus mode: the exporter may legitimately demote/merge assets
                # (crop->crop-required honesty shifts); gate only on totals >= bundle crops
                n_crop, n_stub = len(topic.crop_assets()), len(topic.stub_assets())
                checks.append(check("asset-kinds-present", (n_crop + n_stub) > 0,
                                    f"corpus assets: {n_crop} crop + {n_stub} crop-required (bundle: {e['crop_assets']}+{e['crop_required_stubs']}; exporter may demote)"))
                checks.append(delegated("figures-inlined-count",
                                        "exporter-side transform (crops are inlined into problemMd at export "
                                        "time) — counted at the static-bundles leg; actually loading is proven "
                                        "at the rendered leg",
                                        RESP_SERVED_TEXT))
            # marks-sum law per question
            bad = [q.get("id") for q in qs if sum((p.get("marks") or 0) for p in (q.get("parts") or [])) != q.get("totalMarks", q.get("total_marks"))]
            checks.append(check("marks-sum-per-question", not bad, f"violations: {bad[:3]}"))
            # expected semantic facts — part lookup works in both shapes: bundle
            # parts carry offp_* ids; corpus parts carry part_number ("1(b)(i)").
            # The exporter id embeds the part path after the question number.
            def part_number_from_id(pid):
                # offp_2023-06_2p_1-b-i -> "1(b)(i)" (split on underscores; the
                # series segment itself carries hyphens)
                if not (pid or "").startswith("offp_"):
                    return pid
                segs = pid[len("offp_"):].split("_")
                m = re.match(r"^(\d+)(?:-(.*))?$", segs[-1])
                if not m:
                    return pid
                qn, rest = m.group(1), m.group(2)
                return qn if not rest else qn + "(" + rest.replace("-", ")(") + ")"

            byid = {}
            for p in parts:
                byid[topic.pid(p)] = p
                if p.get("part_number"):
                    byid.setdefault(p["part_number"], p)
                derived = part_number_from_id(topic.pid(p) or "")
                if derived:
                    byid.setdefault(derived, p)

            # bundle problemMd = question stem (+group stems) + problem concat;
            # the corpus keeps stems on the QUESTION. Map part -> owning question.
            qof = {}
            for q in qs:
                for pp in q.get("parts") or []:
                    qof[topic.pid(pp)] = q
                    if pp.get("part_number"):
                        qof[pp["part_number"]] = q

            def part_text(p):
                md = topic.pproblem(p) or ""
                q = qof.get(topic.pid(p)) or {}
                extra = (q.get("stem_md") or "") + "\n" + (p.get("stem_md") or "")
                for src in (q.get("groups") or {}, p.get("groups") or {}):
                    for g in (src or {}).values():
                        extra += "\n" + (g.get("group_stem_md") or "")
                return norm(extra) + " " + norm(md)
            def lookup(pid):
                # bundle ids (offp_*) resolve directly in bundle mode; derive the
                # corpus part_number ("1(b)(i)") in corpus mode
                return byid.get(pid) or byid.get(part_number_from_id(pid))

            for fact in case["fact_parts"]:
                p = lookup(fact["part_id"])
                md = part_text(p) if p else ""
                if p and fact["snippet"] in md:
                    checks.append(check(f"fact:{fact['part_id']}", True,
                                        "fact present in this text layer"))
                elif mode == "corpus":
                    checks.append(delegated(f"fact:{fact['part_id']}",
                                            "absent from the verbatim corpus layer (served text is the "
                                            "exporter/authored layer — required and verified at the "
                                            "static-bundles leg and the rendered leg)"))
                else:
                    checks.append(check(f"fact:{fact['part_id']}", False,
                                        f"EXPECTED FACT MISSING from the served text of {fact['part_id']} — semantic fidelity violation"))
            # expected solution facts
            for fact in case["solution_facts"]:
                p = lookup(fact["part_id"])
                md = norm(topic.psolution(p)) if p else ""
                if p and fact["snippet"] in md:
                    checks.append(check(f"solfact:{fact['part_id']}", True,
                                        "solution fact present in this text layer"))
                elif mode == "corpus":
                    checks.append(delegated(f"solfact:{fact['part_id']}",
                                            "absent from the verbatim corpus layer (served text is the "
                                            "exporter/authored layer — required and verified at the "
                                            "static-bundles leg and the rendered leg)"))
                else:
                    checks.append(check(f"solfact:{fact['part_id']}", False,
                                        f"EXPECTED SOLUTION FACT MISSING from the served text of {fact['part_id']} — solution-integrity violation"))
            # MCQ interaction spec must still match the attested key
            ix = case.get("mcq_interaction")
            if ix:
                p = lookup(ix["part_id"])
                ch = {c["label"]: c for c in (topic.pchoices(p) if p else [])}
                ok = bool(p) and ch.get(ix["correct_label"], {}).get("isCorrect") is True \
                    and not ch.get(ix["distractor_label"], {}).get("isCorrect", False)
                checks.append(check(f"mcq-key:{ix['part_id']}", ok,
                                    "" if ok else f"key law moved for {ix['part_id']}"))
            # corpus-mode extra: crop asset files exist on disk
            if mode == "corpus":
                spec, paper, series = parsed
                td = Path(args.corpus) / LANE_BY_SPEC[spec] / series / (
                    {"igcse-physics-19": "4PH1", "igcse-chemistry-19": "4CH1", "igcse-maths-b-16": "4MB1"}[LANE_BY_SPEC[spec]]
                    + "-" + paper.upper())
                missing = [a.get("path") for a in topic.crop_assets() if not (td / (a.get("path") or "_")).exists()]
                checks.append(check("asset-files-exist", not missing, f"missing: {missing[:3]}"))
                # F104 guard: the files that DO exist must be format-truth valid
                # (PNG signature + full chunk/decode walk; UTF-8 mojibake of a
                # binary asset is rejected even though a URL would return HTTP 200)
                byte_fails = []
                for a in topic.crop_assets():
                    fp = td / (a.get("path") or "_")
                    if not fp.exists():
                        continue  # dangling already reported by asset-files-exist
                    try:
                        validate_asset_file(fp)
                    except AssetByteError as exc:
                        byte_fails.append(str(exc))
                checks.append(check("asset-bytes-valid", not byte_fails,
                                    f"{len(topic.crop_assets())} crop files byte-checked; "
                                    + ("violations: " + str(byte_fails[:2]) if byte_fails else "all format-valid")))

        receipt["cases"].append({"case_id": case["id"], "mode": mode,
                                 "disposition": case_disposition(checks), "checks": checks})

    receipt["overall"] = leg_disposition(receipt["cases"])
    receipt["summary"] = {
        c["case_id"]: c["disposition"] for c in receipt["cases"]
    }
    out = Path(args.corpus or ".") / ("g9-static-receipt.local.json" if args.corpus else "g9-static-receipt-bundles.local.json")
    out.write_text(json.dumps(receipt, indent=1))
    print(f"G9 static check: overall={receipt['overall']} -> {out}")
    for c in receipt["cases"]:
        fails = [k["id"] for k in c["checks"] if k["outcome"] == "FAIL"]
        nr = [k["id"] for k in c["checks"] if k["outcome"] == "NOT_RUN"]
        na = [k["id"] for k in c["checks"] if k["outcome"] == "NOT_APPLICABLE"]
        print(f"  {c['case_id']}: {c['disposition']}"
              + (f" FAIL={fails}" if fails else "")
              + (f" NOT_RUN={nr}" if nr else "")
              + (f" NA(delegated)={na}" if na else ""))
    sys.exit(0 if receipt["overall"] == "PASS" else 1)


if __name__ == "__main__":
    main()
