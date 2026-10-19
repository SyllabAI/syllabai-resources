#!/usr/bin/env python3
"""
T-C12 — c12_promote.py: operator-only promotion of AI-suggested question<->
spec-point mappings to HUMAN_VALIDATED (c11_promote pattern, decisions-side).

Promotion path (C11_ARCHITECTURE.md section 7, operator review gate):

  verify (AI_SUGGESTED decisions) -> review sheet (c12_review_render.py)
  -> operator dictates verdicts (chat or verdict YAML) -> THIS TOOL, the only
  writer of scripts/c12_promotions.yaml.

The AI decisions file is NEVER touched: it stays the frozen record of what the
model proposed. Ratifications (accept / amend), abstention-exclusion rulings,
and rejections live in the operator-side promotions record. Hand-editing that
record is forbidden and caught by `--check` (CI re-runs it).

Hard properties (all fail closed):
  * operator-only: --by / meta.reviewed_by must be a human identity; AI
    self-attribution is forbidden (same attribution gate as c11_promote.py);
  * exact identity only: every verdict qid must exist in the referenced AI
    decisions file, and the question text hash must re-verify against the
    source questions file (a mutated question can never be ratified);
  * accept is only available to clean SUGGESTED records (any registry
    violation blocks it — amend or reject instead) and to abstention records
    WITH an operator note (an exclusion ruling must say why);
  * amend re-validates the operator's mapping against the full registry set
    (spec points, command word, confidence, rationale) and must differ from
    the AI suggestion — an identical "amend" is told to use accept;
  * rejections are recorded (qid + reason) and never silently dropped;
  * idempotent — re-submitting the same verdicts is a reported no-op; a
    conflicting re-verdict of an already-ratified record is refused (revert
    via git if a ruling must be overturned);
  * atomic writes, parse-before-replace, deterministic output ordering;
  * `--check` re-validates the promotions record standalone (CI): tier must
    be HUMAN_VALIDATED, validated_by must be human, every mapping must pass
    the registry gates, promotions/rejections must agree with their source
    decision files (hashes included).

Usage:
  python3 scripts/c12_promote.py --verdicts scripts/c12_smoke_verdicts.yaml \
      --by "Nawaf Al Hussain Khondokar" \
      [--source scripts/c12_decisions/smoke-demo.agent-pass-1.yaml] \
      [--questions scripts/c12_fixtures/smoke_questions.json] \
      [--date 2026-09-14] [--review-ref graph/reports/C12_SMOKE_REVIEW_SHEET.md]

  python3 scripts/c12_promote.py --check [PROMOTIONS.yaml]

Exit 0 = verdicts recorded (or clean check). Exit 1 = refused (nothing half-written).
"""
from __future__ import annotations

import argparse
import copy
import datetime
import json
import os
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import c12_spec_tagger as tagger  # noqa: E402  (registries, hash, gates)

PROMOTIONS = HERE / "c12_promotions.yaml"
DECISIONS = HERE / "c12_decisions"

AI_NAME_RE = re.compile(r"glm|super\s*z|gpt|claude|openai|anthropic|\bai\b"
                        r"|llm|agent|model|bot", re.I)
RE_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VALID_DECISIONS = ("accept", "amend", "reject")


def die(msg: str) -> "None":
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        die(f"{path.name} does not parse: {e}")


def dup_keys(path: Path) -> list[str]:
    """Duplicate mapping keys are silently last-wins in yaml.safe_load —
    surface them before anything trusts the file (fail closed)."""
    dups: list[str] = []

    def walk(node):
        if isinstance(node, yaml.MappingNode):
            seen = set()
            for k, _ in node.value:
                key = getattr(k, "value", None)
                if key is not None:
                    if key in seen and str(key) not in dups:
                        dups.append(str(key))
                    seen.add(key)
            for _, v in node.value:
                walk(v)
        elif isinstance(node, yaml.SequenceNode):
            for v in node.value:
                walk(v)

    try:
        walk(yaml.compose(path.read_text(encoding="utf-8")))
    except yaml.YAMLError as e:
        die(f"{path.name} does not parse: {e}")
    return dups


def human_identity(name: str, where: str) -> str:
    if not name or not name.strip():
        die(f"{where} is empty — promotion is operator-only")
    if AI_NAME_RE.search(name):
        die(f"{where} {name!r} fails the attribution gate: promotion is "
            f"operator-only and AI self-attribution is forbidden (fail closed)")
    return name.strip()


def load_source(path: Path,
                questions_override: str | None = None) -> tuple[dict, dict, Path]:
    """source decisions YAML -> (doc, {qid: record}, resolved questions path)."""
    if not path.exists():
        die(f"source decisions file not found: {path}")
    doc = load_yaml(path)
    records = {r["question_id"]: r for r in (doc.get("decisions") or [])}
    if not records:
        die(f"source decisions file {path.name} has no records")
    # explicit --questions wins; otherwise the decisions file's own meta
    raw = str(questions_override or "").strip() \
        or str((doc.get("meta") or {}).get("source_questions") or "").strip()
    if not raw:
        die("source decisions meta.source_questions is empty — pass --questions")
    p = Path(raw)
    # resolve against THIS tool's repo, never the cwd (hermetic sandboxes, CI)
    qpath = p if p.is_absolute() else REPO / raw
    if not qpath.exists():
        die(f"questions file not found: {raw} — pass --questions")
    return doc, records, qpath


def bind_hashes(records: dict, qpath: Path) -> dict:
    """question_id -> unit_text_hash, re-verified against the questions file."""
    units = {u["id"]: u for u in tagger.load_questions(qpath)}
    out = {}
    for qid, rec in records.items():
        u = units.get(qid)
        if u is None:
            die(f"question {qid!r} missing from {qpath.name}")
        h = tagger.text_hash(u["text"])
        if h != rec.get("unit_text_hash"):
            die(f"text hash mismatch for {qid} — the questions file changed since "
                f"the decisions pass; refusing to ratify against drifted text")
        out[qid] = h
    return out


def check_mapping(m: dict, where: str, reg: dict, require_diff_from: dict | None = None):
    if not isinstance(m, dict):
        die(f"{where}: mapping must be a mapping")
    primary = m.get("primary_spec_point")
    if primary not in reg["points"]:
        die(f"{where}: primary {primary!r} is not in the {tagger.CURRICULUM} registry")
    secs = m.get("secondary_spec_points") or []
    if not isinstance(secs, list):
        die(f"{where}: secondary_spec_points must be a list")
    for s in secs:
        if s not in reg["points"]:
            die(f"{where}: secondary {s!r} is not in the {tagger.CURRICULUM} registry")
        if s == primary:
            die(f"{where}: secondary {s} duplicates the primary")
    cw = m.get("command_word")
    if tagger._norm_word(cw) not in reg["command_words"]:
        die(f"{where}: command_word {cw!r} is not in the command-word registry — "
            f"an operator ratification may never carry a registry violation")
    conf = m.get("confidence")
    if not isinstance(conf, (int, float)) or isinstance(conf, bool) or not (0.0 <= float(conf) <= 1.0):
        die(f"{where}: confidence must be a number in [0, 1], got {conf!r}")
    if not str(m.get("rationale") or "").strip():
        die(f"{where}: rationale is required — say IN YOUR OWN WORDS why this mapping holds")
    if require_diff_from is not None:
        a = {k: v for k, v in m.items()}
        b = require_diff_from
        if (a.get("primary_spec_point") == b.get("primary_spec_point")
                and sorted(a.get("secondary_spec_points") or [])
                == sorted(b.get("secondary_spec_points") or [])
                and tagger._norm_word(a.get("command_word") or "")
                == tagger._norm_word(b.get("command_word") or "")):
            die(f"{where}: the amended mapping matches the AI suggestion — "
                f"use decision: accept instead")


def gate_accept(rec: dict, reg: dict, threshold: float, where: str):
    """accept = ratify as-is. Only clean SUGGESTED records qualify."""
    if rec.get("mapping") is None:
        return  # abstention accept = exclusion ruling; note required by caller
    if rec.get("validation_status") != "SUGGESTED":
        die(f"{where}: record is REVIEW_REQUIRED (demoted: {rec.get('ambiguity_note')}) — "
            f"accept is blocked; amend the corrected mapping or reject")
    dr = tagger.DecisionRecord.model_validate(rec)
    errs = tagger.hard_errors(dr, reg) + tagger.demotable_errors(dr, reg, threshold)
    if errs:
        die(f"{where}: record still carries registry violations ({'; '.join(errs)}) — "
            f"accept is blocked; amend or reject")


def verdict_record(v: dict, qid: str) -> dict:
    if not isinstance(v, dict):
        die(f"verdict for {qid} must be a mapping")
    d = v.get("decision")
    if d not in VALID_DECISIONS:
        die(f"{qid}: decision must be one of {VALID_DECISIONS}, got {d!r}")
    if d == "reject" and not str(v.get("reason") or "").strip():
        die(f"{qid}: reject requires a reason — a silent rejection is not auditable")
    return v


def promote(args) -> int:
    vpath = Path(args.verdicts)
    if not vpath.exists():
        die(f"verdict file not found: {vpath}")
    dups = dup_keys(vpath)
    if dups:
        die(f"verdict file has duplicate keys {dups} — refusing last-wins ambiguity")
    vf = load_yaml(vpath)
    vmeta = vf.get("meta") or {}
    verdicts = vf.get("verdicts") or {}
    if not verdicts:
        die("verdict file has no verdicts")

    operator = human_identity(args.by or vmeta.get("reviewed_by") or "", "operator identity")
    review_ref = (args.review_ref or vmeta.get("review_reference") or "").strip()
    if not review_ref:
        die("--review-ref (or meta.review_reference) must name the review artifact "
            "that the operator ruled from")
    if vmeta.get("reviewed_by"):
        human_identity(str(vmeta["reviewed_by"]), "meta.reviewed_by")
    date = args.date or datetime.date.today().isoformat()
    if not RE_ISO_DATE.match(date):
        die(f"--date must be YYYY-MM-DD, got {date!r}")
    if vmeta.get("review_date") and not RE_ISO_DATE.match(str(vmeta["review_date"])):
        die(f"meta.review_date must be YYYY-MM-DD, got {vmeta['review_date']!r}")

    source = Path(args.source or vmeta.get("source") or "")
    doc, records, qpath = load_source(source, getattr(args, "questions", None))
    hashes = bind_hashes(records, qpath)
    reg = tagger.load_registries(Path(args.graph)) if args.graph else tagger.load_registries()
    threshold = float((doc.get("meta") or {}).get("high_confidence_threshold")
                      or tagger.DEFAULT_THRESHOLD)
    src_rel = source.resolve().relative_to(REPO).as_posix() \
        if source.resolve().is_relative_to(REPO) else str(source)

    promoted, rejected, noop = [], [], []
    for qid, v in verdicts.items():
        if qid not in records:
            die(f"verdict for unknown question {qid!r} — not in {src_rel} "
                f"(exact identities only)")
        v = verdict_record(v, qid)
        rec = records[qid]
        where = f"{qid} ({v['decision']})"

        if v["decision"] == "reject":
            rejected.append((qid, str(v["reason"]).strip()))
            continue

        if v["decision"] == "accept":
            if rec.get("mapping") is None:
                if not str(v.get("note") or "").strip():
                    die(f"{where}: accepting an abstention is an out-of-curriculum/"
                        f"unmapped EXCLUSION RULING — a note explaining it is required")
                mapping = None
                decision = "accepted-exclusion"
            else:
                gate_accept(rec, reg, threshold, where)
                mapping = rec["mapping"]
                decision = "accepted"
            ai_suggestion = copy.deepcopy(rec["mapping"])
        else:  # amend
            if rec.get("mapping") is None:
                die(f"{where}: the AI abstained — there is nothing to amend; "
                    f"use accept-with-note to rule it out-of-curriculum, or reject")
            check_mapping(v.get("mapping"), f"{qid} (amended)", reg,
                          require_diff_from=rec["mapping"])
            mapping = v["mapping"]
            decision = "amended"
            ai_suggestion = copy.deepcopy(rec["mapping"])

        promoted.append({
            "source": src_rel,
            "question_id": qid,
            "unit_text_hash": hashes[qid],
            "decision": decision,
            "mapping": mapping,
            "ai_suggestion": ai_suggestion,
            "provenance": {
                "tier": "HUMAN_VALIDATED",
                "source_tier": "AI_SUGGESTED",
                "model_version": (doc.get("meta") or {}).get("model_version"),
                "extraction_pass": (doc.get("meta") or {}).get("extraction_pass"),
                "validated_by": operator,
                "validated_date": date,
                "review_reference": review_ref,
                "operator_note": str(v.get("note") or "").strip() or None,
            },
        })

    # ---- load existing promotions (idempotence / conflict) ------------------
    promo = load_yaml(PROMOTIONS) if PROMOTIONS.exists() else {
        "meta": {"task": "T-C12", "stage": "operator-promotion",
                 "contract": "C11_ARCHITECTURE.md section 7 (operator review gate)",
                 "tool": "scripts/c12_promote.py"},
        "promotions": [], "rejections": []}
    promo.setdefault("promotions", [])
    promo.setdefault("rejections", [])
    existing = {(p["source"], p["question_id"]): p for p in promo["promotions"]}
    rejected_existing = {(r["source"], r["question_id"]): r for r in promo["rejections"]}

    def same_mapping(a, b):
        return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)

    fresh_p, fresh_r = [], []
    for entry in promoted:
        key = (entry["source"], entry["question_id"])
        prev = existing.get(key)
        if prev:
            if (prev.get("decision") == entry["decision"]
                    and same_mapping(prev.get("mapping"), entry.get("mapping"))):
                noop.append(f"{entry['question_id']} (already ratified by "
                            f"{prev['provenance']['validated_by']} on "
                            f"{prev['provenance']['validated_date']})")
            else:
                die(f"{entry['question_id']} is already ratified ({prev.get('decision')} "
                    f"on {prev['provenance']['validated_date']}) — a conflicting "
                    f"re-verdict is refused; revert via git if the ruling must change")
            continue
        if key in rejected_existing:
            die(f"{entry['question_id']} was already REJECTED for this source — "
                f"re-promotion after rejection needs a new review; revert via git")
        fresh_p.append(entry)
    for qid, reason in rejected:
        key = (src_rel, qid)
        if key in existing:
            die(f"{qid} is already RATIFIED for this source — it cannot also be "
                f"rejected; revert via git if the ruling must change")
        prev = rejected_existing.get(key)
        if prev:
            if prev.get("reason") == reason:
                noop.append(f"{qid} (already rejected on {prev['validated_date']})")
            else:
                die(f"{qid} is already rejected with a different reason — "
                    f"conflicting rejections are refused; revert via git")
            continue
        fresh_r.append({
            "source": src_rel, "question_id": qid, "reason": reason,
            "validated_by": operator, "validated_date": date,
            "review_reference": review_ref,
        })

    if not fresh_p and not fresh_r:
        for m in noop:
            print("-", m)
        print("nothing new to record")
        return 0

    promo["promotions"] = sorted(
        promo["promotions"] + fresh_p,
        key=lambda p: (p["source"], p["question_id"]))
    promo["rejections"] = sorted(
        promo["rejections"] + fresh_r,
        key=lambda r: (r["source"], r["question_id"]))
    meta = promo.setdefault("meta", {})
    meta.update({
        "task": "T-C12", "stage": "operator-promotion",
        "contract": "C11_ARCHITECTURE.md section 7 (operator review gate)",
        "tool": "scripts/c12_promote.py",
        "generated_date": meta.get("generated_date") or date,
    })
    text = ("# T-C12 promotion record — operator ratifications of AI-suggested "
            "question<->spec-point mappings.\n# Written ONLY by "
            "scripts/c12_promote.py; see C11_ARCHITECTURE.md section 7. "
            "Hand-editing is forbidden.\n"
            + yaml.safe_dump(promo, allow_unicode=True, sort_keys=False, width=100))
    yaml.safe_load(text)  # fail-closed: parse before replacing the record
    _tmp = PROMOTIONS.with_suffix(".yaml.tmp")
    _tmp.write_text(text, encoding="utf-8")
    os.replace(_tmp, PROMOTIONS)  # atomic: no truncated record on crash

    print(f"promotions recorded: {PROMOTIONS.name}")
    for e in fresh_p:
        print("RATIFIED %s [%s] %s" % (
            e["question_id"], e["decision"],
            (e.get("mapping") or {}).get("primary_spec_point") or "(exclusion)"))
    for r in fresh_r:
        print("REJECTED %s — %s" % (r["question_id"], r["reason"]))
    for m in noop:
        print("-", m)
    return 0


# ── --check: standalone re-validation of the promotions record (CI) ──────────

def check_promotions(path: Path, reg: dict) -> int:
    if not path.exists():
        print(f"check: no promotions record at {path} yet — nothing to validate (ok)")
        return 0
    dups = dup_keys(path)
    if dups:
        print(f"FAIL: duplicate keys {dups} in {path.name}", file=sys.stderr)
        return 1
    promo = load_yaml(path)
    errs: list[str] = []
    sources_cache: dict[str, tuple[dict, dict]] = {}
    seen_promoted = set()
    seen_rejected = set()

    def source_records(rel: str):
        if rel not in sources_cache:
            p = REPO / rel
            if not p.exists():
                sources_cache[rel] = ({}, {})
            else:
                doc = load_yaml(p)
                recs = {r["question_id"]: r for r in (doc.get("decisions") or [])}
                sources_cache[rel] = (doc, recs)
        return sources_cache[rel]

    for p in promo.get("promotions") or []:
        qid = p.get("question_id")
        where = f"promotion {qid}"
        key = (p.get("source"), qid)
        if key in seen_promoted:
            errs.append(f"{where}: duplicate promotion entry")
        seen_promoted.add(key)
        prov = p.get("provenance") or {}
        if prov.get("tier") != "HUMAN_VALIDATED":
            errs.append(f"{where}: tier must be HUMAN_VALIDATED, got {prov.get('tier')!r}")
        if prov.get("source_tier") != "AI_SUGGESTED":
            errs.append(f"{where}: source_tier must be AI_SUGGESTED, got {prov.get('source_tier')!r}")
        try:
            human_identity(str(prov.get("validated_by")), f"{where}: validated_by")
        except SystemExit:
            errs.append(f"{where}: validated_by fails the attribution gate")
        if not RE_ISO_DATE.match(str(prov.get("validated_date") or "")):
            errs.append(f"{where}: validated_date must be YYYY-MM-DD")
        if not str(prov.get("review_reference") or "").strip():
            errs.append(f"{where}: review_reference missing")
        src = p.get("source")
        doc, recs = source_records(src)
        rec = recs.get(qid)
        if rec is None:
            errs.append(f"{where}: question not present in source decisions {src}")
            continue
        if rec.get("unit_text_hash") != p.get("unit_text_hash"):
            errs.append(f"{where}: unit_text_hash does not match the source decisions file")
        decision = p.get("decision")
        mapping = p.get("mapping")
        if decision == "accepted-exclusion":
            if mapping is not None or rec.get("mapping") is not None:
                errs.append(f"{where}: exclusion ruling but a mapping is present")
            if not str(prov.get("operator_note") or "").strip():
                errs.append(f"{where}: exclusion ruling without an operator note")
        elif decision in ("accepted", "amended"):
            if mapping is None:
                errs.append(f"{where}: {decision} without a mapping")
                continue
            try:
                check_mapping(dict(mapping), where, reg,
                              require_diff_from=rec.get("mapping") if decision == "amended" else None)
            except SystemExit as exc:
                errs.append(f"{where}: {exc}")
            if decision == "accepted":
                ai = rec.get("mapping") or {}
                if (mapping.get("primary_spec_point") != ai.get("primary_spec_point")
                        or sorted(mapping.get("secondary_spec_points") or [])
                        != sorted(ai.get("secondary_spec_points") or [])
                        or tagger._norm_word(mapping.get("command_word") or "")
                        != tagger._norm_word(ai.get("command_word") or "")):
                    errs.append(f"{where}: 'accepted' mapping differs from the AI "
                                f"suggestion — must be 'amended'")
        else:
            errs.append(f"{where}: unknown decision {decision!r}")

    for r in promo.get("rejections") or []:
        qid = r.get("question_id")
        where = f"rejection {qid}"
        key = (r.get("source"), qid)
        if key in seen_rejected:
            errs.append(f"{where}: duplicate rejection entry")
        seen_rejected.add(key)
        if key in seen_promoted:
            errs.append(f"{where}: question is both promoted and rejected for the same source")
        if not str(r.get("reason") or "").strip():
            errs.append(f"{where}: rejection without a reason")
        try:
            human_identity(str(r.get("validated_by")), f"{where}: validated_by")
        except SystemExit:
            errs.append(f"{where}: validated_by fails the attribution gate")
        _, recs = source_records(r.get("source") or "")
        if r.get("question_id") not in recs:
            errs.append(f"{where}: question not present in source decisions {r.get('source')}")

    if errs:
        print("FAIL: %d problem(s) in %s:" % (len(errs), path.name), file=sys.stderr)
        for e in errs:
            print("  - %s" % e, file=sys.stderr)
        return 1
    n = len(promo.get("promotions") or [])
    m = len(promo.get("rejections") or [])
    print("check: OK — %d promotion(s), %d rejection(s), all gates passed" % (n, m))
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="T-C12 operator-only promotion "
                                             "(section-7 review gate)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("promote", help="record operator verdicts (accept/amend/reject)")
    p.add_argument("--verdicts", required=True, help="operator verdict YAML")
    p.add_argument("--source", help="AI decisions YAML (default: verdict meta.source)")
    p.add_argument("--questions", help="source questions JSON (default: resolved from decisions meta)")
    p.add_argument("--by", help="operator identity (default: verdict meta.reviewed_by)")
    p.add_argument("--date", help="ratification date (default: today UTC)")
    p.add_argument("--review-ref", help="review artifact (default: verdict meta.review_reference)")
    p.add_argument("--graph", help="alternate graph dir")
    p.set_defaults(fn=lambda a: promote(a))

    c = sub.add_parser("check", help="re-validate the promotions record (CI gate)")
    c.add_argument("file", nargs="?", default=str(PROMOTIONS))
    c.add_argument("--graph", help="alternate graph dir")
    c.set_defaults(fn=lambda a: check_promotions(Path(a.file), tagger.load_registries(
        Path(a.graph)) if a.graph else tagger.load_registries()))

    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
