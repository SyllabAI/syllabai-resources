#!/usr/bin/env python3
"""
T-C12 — c12_review_render.py: render the operator review sheet for a c12
decisions file (the human half of the section-7 gate).

Pipeline position:

  verify (AI, SUGGESTED/REVIEW_REQUIRED) -> THIS TOOL (review sheet, zero-LLM)
  -> operator reads the sheet and dictates verdicts
  -> scripts/c12_promote.py records HUMAN_VALIDATED rulings in
     scripts/c12_promotions.yaml (the AI decisions file is NEVER touched).

The sheet gives the operator everything needed to rule on each record:
  * the verbatim question text (bound to unit_text_hash — promote re-verifies
    the hash, so a mutated question can never be ratified);
  * the AI proposal (primary/secondary spec points, command word, confidence,
    rationale) with the actual registry wording of every proposed point;
  * the deterministic prefilter view (top-K candidates + weak flag) so the
    operator can see what the keyword stage anchored on;
  * computed checkpoints (registry membership, threshold, demotion status,
    C-point paper applicability, abstention) — mechanical facts only; the
    SEMANTIC ruling (does the wording truly match?) is the operator's.

Zero network, zero LLM, no key. Deterministic: same inputs -> same bytes.

Usage:
  python3 scripts/c12_review_render.py \
      --decisions scripts/c12_decisions/smoke-demo.agent-pass-1.yaml \
      [--questions scripts/c12_fixtures/smoke_questions.json] \
      [--out graph/reports/C12_SMOKE_REVIEW_SHEET.md] [--date 2026-09-14]
"""
from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import c12_spec_tagger as tagger  # noqa: E402  (shared registries/prefilter/hash)


def die(msg: str) -> "None":
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def questions_path_for(decisions_path: Path, override: str | None,
                       meta: dict) -> Path:
    if override:
        return Path(override)
    raw = str((meta.get("source_questions") or "").strip())
    if not raw:
        die("decisions meta.source_questions is empty — pass --questions")
    p = Path(raw)
    # resolve against THIS tool's repo, never the cwd (hermetic sandboxes, CI)
    qpath = p if p.is_absolute() else HERE.parent / raw
    if not qpath.exists():
        die(f"questions file not found: {raw} — pass --questions")
    return qpath


def yes_no(b: bool) -> str:
    return "yes" if b else "no"


def sp_bullet(code: str, reg: dict) -> list[str]:
    p = reg["points"].get(code)
    if p is None:
        return [f"  - `{code}` — NOT IN REGISTRY"]
    lines = [f"  - `{code}` ({p.get('subsection') or '?'}): {p.get('official_wording') or ''}"]
    app = p.get("applicability") or {}
    flags = []
    if p.get("c_point"):
        flags.append("**C-point — examined on Paper 2C only**")
    if app.get("papers"):
        flags.append("papers: %s" % ", ".join(app["papers"]))
    if app.get("double_award_shared"):
        flags.append("double-award shared")
    if flags:
        lines[-1] += "  \n    - " + " · ".join(flags)
    return lines


def checkpoint_block(rec: dict, reg: dict, threshold: float,
                     cand: list[dict], qhash: str) -> list[str]:
    m = rec.get("mapping")
    status = rec.get("validation_status")
    prov_tier = (rec.get("provenance") or {}).get("tier")
    max_score = cand[0]["score"] if cand else 0.0
    weak = bool(cand) and max_score < tagger.WEAK_SCORE
    rows = [
        f"- text hash binding: `{qhash[:16]}…` — must match the source questions file (promote re-verifies)",
        f"- provenance tier: {prov_tier} (must be AI_SUGGESTED in the AI file; becomes "
        f"HUMAN_VALIDATED only via c12_promote.py)",
        f"- prefilter: max score {max_score:.2f} · weak={yes_no(weak)} · "
        f"{len(cand)} candidate(s) above floor {tagger.SCORE_FLOOR}",
    ]
    if m is None:
        rows.append("- **abstention** (no mapping proposed) — accept = operator confirms the "
                    "out-of-curriculum/unmapped ruling (a note is REQUIRED); reject = leave in the queue")
        return rows
    cw_ok = tagger._norm_word(m["command_word"]) in reg["command_words"]
    rows.append(f"- command word `{m['command_word']}`: "
                + ("in registry" if cw_ok else "**NOT in the command-word registry**"))
    rows.append(f"- confidence {m['confidence']:.2f} vs threshold {threshold:.2f}: "
                + ("at/above" if m["confidence"] >= threshold else "**below**"))
    if m.get("secondary_spec_points"):
        rows.append("- secondary points: %s (each must be genuinely relevant, not keyword-noise)"
                    % ", ".join(f"`{s}`" for s in m["secondary_spec_points"]))
    if status == "REVIEW_REQUIRED":
        rows.append("- **status REVIEW_REQUIRED (demoted)** — accept is BLOCKED by c12_promote.py; "
                    "amend (fix the documented violation) or reject. Ambiguity note: %s"
                    % (rec.get("ambiguity_note") or "(none)"))
    else:
        rows.append("- status SUGGESTED — accept is available if you judge the mapping semantically correct")
    return rows


def render_record(idx: int, rec: dict, unit: dict, reg: dict, threshold: float,
                  pf: tagger.Prefilter) -> str:
    qid = rec["question_id"]
    status = rec["validation_status"]
    conf = (rec.get("mapping") or {}).get("confidence")
    head = f"### R{idx} · `{qid}` — {status}" + (f" · confidence {conf:.2f}" if conf is not None else "")
    out = [head, "", "> " + unit["text"].replace("\n", "\n> "), "",
           f"`unit_text_hash: {rec['unit_text_hash']}`", ""]

    cand = pf.rank(unit["text"])
    m = rec.get("mapping")
    if m is None:
        out += ["**AI proposal: none (abstention)** — %s" % (rec.get("ambiguity_note") or ""), ""]
    else:
        out += ["**AI proposal:**", ""]
        out += ["| field | value |", "|---|---|"]
        out.append("| primary | `%s` |" % m["primary_spec_point"])
        secs = m.get("secondary_spec_points") or []
        out.append("| secondary | %s |" % (", ".join(f"`{s}`" for s in secs) or "—"))
        out.append("| command word | %s |" % m["command_word"])
        out.append("| confidence | %.2f |" % m["confidence"])
        out.append("| rationale | %s |" % m["rationale"].replace("|", "\\|"))
        out += ["", "Registry wording of the proposed points:"]
        out += sp_bullet(m["primary_spec_point"], reg)
        for s in secs:
            out += sp_bullet(s, reg)
        out.append("")

    out.append("Deterministic prefilter (IDF token overlap, top %d):" % tagger.TOP_K)
    if cand:
        out.append("  " + " · ".join(f"`{c['code']}` ({c['score']:.2f})" for c in cand))
    else:
        out.append("  (no candidate above the %.2f floor — the keyword stage abstained)" % tagger.SCORE_FLOOR)
    out += ["", "Operator checkpoints (mechanical facts — the semantic ruling is yours):"]
    out += checkpoint_block(rec, reg, threshold, cand, rec["unit_text_hash"])
    out += ["", "**Verdict:** `accept` / `amend` / `reject` — operator note: ______", "",
            "---", ""]
    return "\n".join(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="render the c12 operator review sheet (zero-LLM)")
    ap.add_argument("--decisions", required=True, help="AI decisions YAML (c12 verify output)")
    ap.add_argument("--questions", help="source questions JSON (default: resolved from decisions meta)")
    ap.add_argument("--graph", help="alternate graph dir (default: repo graph/)")
    ap.add_argument("--out", help="write markdown here (default: stdout)")
    ap.add_argument("--date", help="rendered-on date for the header (default: today UTC)")
    args = ap.parse_args(argv)

    dec_path = Path(args.decisions)
    if not dec_path.exists():
        die(f"decisions file not found: {dec_path}")
    doc = yaml.safe_load(dec_path.read_text(encoding="utf-8"))
    meta = doc.get("meta") or {}
    records = doc.get("decisions") or []
    if not records:
        die("decisions file has no records")

    reg = tagger.load_registries(Path(args.graph)) if args.graph else tagger.load_registries()
    qpath = questions_path_for(dec_path, args.questions, meta)
    units = {u["id"]: u for u in tagger.load_questions(qpath)}
    pf = tagger.Prefilter(reg)
    threshold = float(meta.get("high_confidence_threshold") or tagger.DEFAULT_THRESHOLD)
    rendered_on = args.date or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")

    # hash binding up front: the sheet quotes the text the operator is ruling on,
    # so a mismatch means the questions file drifted since the pass — refuse.
    for rec in records:
        u = units.get(rec["question_id"])
        if u is None:
            die("question %r missing from %s" % (rec["question_id"], qpath))
        if tagger.text_hash(u["text"]) != rec["unit_text_hash"]:
            die("text hash mismatch for %s — the questions file changed since the "
                "decisions pass; refusing to render a sheet against drifted text" % rec["question_id"])

    rel_dec = dec_path.resolve().relative_to(HERE.parent) \
        if dec_path.resolve().is_relative_to(HERE.parent) else str(dec_path)
    rel_q = qpath.resolve().relative_to(HERE.parent) \
        if qpath.resolve().is_relative_to(HERE.parent) else str(qpath)

    out = [f"# C12 review sheet — {meta.get('extraction_pass') or dec_path.stem}",
           "",
           "Operator review artifact for the section-7 gate. Generated by "
           "`scripts/c12_review_render.py` (zero-LLM, deterministic); reviewed by a human; "
           "verdicts are recorded by `scripts/c12_promote.py` in `scripts/c12_promotions.yaml`. "
           "The AI decisions file below is never modified.",
           "",
           "| | |", "|---|---|",
           "| decisions (AI_SUGGESTED) | `%s` |" % rel_dec,
           "| questions (hash-bound) | `%s` |" % rel_q,
           "| extraction pass / model | %s · %s |" % (meta.get("extraction_pass"), meta.get("model_version")),
           "| generated / rendered | %s / %s |" % (meta.get("generated_date"), rendered_on),
           "| threshold | %.2f |" % threshold,
           "| counts | %s |" % (meta.get("counts") or {}),
           "",
           "## How to review (the section-7 operator gate)",
           "",
           "1. Read the verbatim question, then the AI proposal and the registry wording of every "
           "proposed point. The question is: does the official wording genuinely assess what the "
           "question asks — not merely share keywords? (AGENT.md rule 3: coverage is never "
           "manufactured through similarity.)",
           "2. Check the command word against the question's actual demand, and the paper "
           "applicability flags (C-points are examined on Paper 2C only).",
           "3. Rule per record: `accept` (ratify the AI mapping as-is; only available to clean "
           "SUGGESTED records, or to confirm an abstention with a note), `amend` (your corrected "
           "mapping — fully re-validated against the registries), or `reject` (decline; the record "
           "stays in the manual-review queue and the rejection is recorded).",
           "4. Hand the verdicts back in chat (`R1: accept`, `R2: amend primary=… command=… "
           "confidence=… note=\"…\"`, …) or as a verdict YAML for "
           "`python3 scripts/c12_promote.py --verdicts <file> --by <operator-name>`.",
           "",
           "Summary:",
           "",
           "| # | question | status | primary | conf | prefilter max |",
           "|---|---|---|---|---|---|"]
    idx = 0
    for rec in records:
        idx += 1
        u = units[rec["question_id"]]
        cand = pf.rank(u["text"])
        m = rec.get("mapping")
        out.append("| R%d | `%s` | %s | %s | %s | %s |" % (
            idx, rec["question_id"], rec["validation_status"],
            (m or {}).get("primary_spec_point") or "—",
            ("%.2f" % m["confidence"]) if m else "—",
            ("%.2f" % cand[0]["score"]) if cand else "—"))
    out += ["", "---", ""]

    idx = 0
    for rec in records:
        idx += 1
        out.append(render_record(idx, rec, units[rec["question_id"]], reg, threshold, pf))

    text = "\n".join(out)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print("review sheet: %s (%d records)" % (args.out, len(records)), file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
