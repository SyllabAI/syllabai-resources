#!/usr/bin/env python3
"""
lessonctl.py — the CourseLessons pipeline CLI (stdlib + PyYAML).

Any agent, any stage, one entrypoint:

  python3 scripts/lessonctl.py report  --course chemistry-4ch1
  python3 scripts/lessonctl.py scaffold --course chemistry-4ch1 --chapter u1:c02
  python3 scripts/lessonctl.py resume  <lesson-dir>
  python3 scripts/lessonctl.py lint    <lesson-dir>
  python3 scripts/lessonctl.py tracker --lesson <lesson-dir> --set stage=S2 --receipt qa/receipt.yaml
  python3 scripts/lessonctl.py finding --course chemistry-4ch1 --type content-error --lesson u1-c01 ... 
  python3 scripts/lessonctl.py emit    <lesson-dir>     # S4: lessonPackV1 JSON

Laws this tool enforces: see VALIDATION.md (rules) and START-HERE.md (hard laws).
Design note: ONE cli, not many scripts — easier for any-agent pickup, one
receipt/tracker discipline, one place to extend (self-improvement law).
"""
import argparse, hashlib, json, os, re, sys, datetime
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent          # CourseLessons/
SEC_RE = re.compile(r"^u\d+:c\d{2}:s\d{2}$")
BOX_MARKER = re.compile(r"^:::([a-z0-9-]+)\s*$", re.M)


def now() -> str:
    return datetime.datetime.now().astimezone().strftime("%Y-%m-%d")


def load_yaml(p: Path):
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f)


def course_path(course: str) -> Path:
    hits = list((ROOT / "lessons").glob(f"**/*/{course}")) if course else []
    if not hits:
        sys.exit(f"course not found: {course}")
    return hits[0]


def section_files(lesson: Path):
    return sorted((lesson / "sections").glob("*.md"))


def parse_section(p: Path):
    """front-matter (--- yaml ---) + body; returns (fm, body, err)."""
    text = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return None, text, "missing front-matter block"
    try:
        return yaml.safe_load(m.group(1)) or {}, m.group(2), None
    except yaml.YAMLError as e:
        return None, m.group(2), f"bad front-matter yaml: {e}"


# ─────────────────────────────── report ───────────────────────────────────────
def cmd_report(args):
    tr = load_yaml(ROOT / "tracker.yaml")
    if args.all or not args.course:
        courses = list(tr["courses"].items())
    else:
        courses = [(args.course, tr["courses"][args.course])]
    for name, c in courses:
        print(f"== {name} ({c['board']}/{c['qualification']}) status={c['status']} ==")
        lessons = c.get("lessons") or {}
        if not lessons:
            print("  (no lessons registered yet — run `scaffold`)")
        for lid, l in lessons.items():
            print(f"  {lid:34s} stage={l.get('stage')} sections={l.get('sections_done')}/{l.get('sections_total')} last_agent={l.get('last_agent')}")
        cdir = Path(ROOT) / c["path"]
        fjsonl = cdir / "findings.jsonl"
        if fjsonl.exists():
            lines = [json.loads(x) for x in fjsonl.read_text(encoding="utf-8").splitlines() if x.strip()]
            open_f = [f for f in lines if f.get("status") != "closed"]
            by_type = {}
            for f in lines:
                by_type[f.get("type", "?")] = by_type.get(f.get("type", "?"), 0) + 1
            print(f"  findings: {len(lines)} total, {len(open_f)} open, by-type={by_type}")
            if args.verbose:
                for f in lines[-5:]:
                    print(f"    [{f['id']}] {f.get('type')} {f.get('severity','?')}: {f.get('what','')[:90]}")
    return 0


# ─────────────────────────────── scaffold ─────────────────────────────────────
def cmd_scaffold(args):
    cdir = course_path(args.course)
    cfg = load_yaml(cdir / "course.yaml")
    row = next((r for rows in cfg["spine"].values() for r in rows if r["key"] == args.chapter), None)
    if not row:
        sys.exit(f"chapter {args.chapter} not in course spine")
    lesson_dir = cdir / "lessons" / f"{row['key'].replace(':', '-')}-{row['slug']}"
    if lesson_dir.exists():
        sys.exit(f"lesson folder already exists: {lesson_dir} — use `resume` (resume wins, START-HERE §3)")
    (lesson_dir / "sections").mkdir(parents=True)
    (lesson_dir / "qa").mkdir()
    sections_placeholder = ["TBD-at-S0"]
    lesson_yaml = {
        "lesson_id": f"{row['key'].replace(':', '-')}-{row['slug']}",
        "chapter_key": row["key"],
        "course_id": args.course,
        "title": row["title"],
        "chem_only": bool(row.get("chem_only")),
        "stage": "S0",
        "book_page_range": row.get("pages"),
        "sections": [
            {"id": f"{row['key']}:s{i+1:02d}", "title": None, "status": "todo"}
            for i in range(args.sections)
        ],
        "features": {k: False for k in [
            "prior_knowledge", "cross_curricular", "misconceptions",
            "ms_vocab", "glossary_chips", "quick_checks", "summary", "can_you"]},
        "receipts": [],
        "notes": "pages/section-count pinned from parse of record at S0 (section_map.py) — never guessed",
    }
    (lesson_dir / "lesson.yaml").write_text(
        yaml.safe_dump(lesson_yaml, sort_keys=False, allow_unicode=True), encoding="utf-8")
    (lesson_dir / "glossary.yaml").write_text("# glossary entries: term/slug/definition/ms_accepts/ms_avoids/aliases/source\n[]\n", encoding="utf-8")
    print(f"scaffolded {lesson_dir} (stage S0, {args.sections} placeholder sections — pin real spine via section_map.py)")
    return 0


# ─────────────────────────────── resume ───────────────────────────────────────
def cmd_resume(args):
    lesson = Path(args.lesson_dir).resolve()
    ly = load_yaml(lesson / "lesson.yaml")
    files = section_files(lesson)
    done, missing = [], []
    for sec in ly["sections"]:
        match = [f for f in files if f.name.startswith(sec["id"].split(":")[-1] + "-")]
        if match:
            fm, body, err = parse_section(match[0])
            if err is None and body.strip():
                done.append((sec["id"], match[0].name))
            else:
                missing.append((sec["id"], err or "empty body"))
        else:
            missing.append((sec["id"], "no file"))
    print(f"WORK-ORDER — {ly['lesson_id']} (stage {ly['stage']})")
    print(f"  sections done: {len(done)}/{len(ly['sections'])}")
    for sid, name in done:
        print(f"    ✓ {sid} ({name})")
    for sid, why in missing[:12]:
        print(f"    ✗ {sid}: {why}")
    if len(missing) > 12:
        print(f"    … +{len(missing)-12} more")
    feats = ly.get("features", {})
    print(f"  features checklist: " + ", ".join(f"{k}={'Y' if v else 'n'}" for k, v in feats.items()))
    # f-0004 fix (root cause: stage label was the sole NEXT signal, so a
    # lesson mid-stage reported the NEXT stage while section files were
    # still missing). NEXT now respects per-section file reality: missing
    # files always make "finish them at the current stage" the smallest
    # useful unit; only a complete stage advances the pointer.
    stage_order = ["S0", "S1", "S2", "S3", "S4"]
    cur = ly["stage"]
    cur_label = {"S0": "S1 prose", "S1": "S1 prose", "S2": "S2 boxes",
                 "S3": "S3 practice", "S4": "S4 emit+handoff"}.get(cur, "current-stage work")
    if missing:
        nxt = f"{cur_label} — {len(missing)} section file(s) still missing; finish these before advancing"
    elif cur in stage_order[:-1]:
        nxt_stage = stage_order[stage_order.index(cur) + 1]
        nxt = {"S1": "S1 prose", "S2": "S2 boxes", "S3": "S3 practice",
               "S4": "S4 emit+handoff"}.get(nxt_stage, "S4 emit+handoff")
    else:
        nxt = "already handed off — check tracker/receipts"
    print(f"  NEXT (smallest useful unit): {nxt}")
    print("  run: lint → receipt → tracker transaction → report (BUILD-PLAYBOOK §5)")
    return 0


# ─────────────────────────────── lint ─────────────────────────────────────────
def lint_lesson(lesson: Path, cdir: Path):
    """Returns (errors, warns, infos) as string lists. Rules: VALIDATION.md."""
    errors, warns, infos = [], [], []
    ly_path = lesson / "lesson.yaml"
    if not ly_path.exists():
        return [f"V1 lesson.yaml missing"], [], []
    ly = load_yaml(ly_path)
    cfg = load_yaml(cdir / "course.yaml")
    subject_lint = cdir / "course.yaml"  # banned list resolved below
    rules = load_yaml(ROOT / "scripts" / "lint_rules" / "chem.yaml")
    join = set()
    for rows in cfg["spine"].values():
        for r in rows:
            if r["key"] == ly["chapter_key"]:
                join |= set(r.get("join_set") or [])

    # V1 schema + grammar
    for key in ("lesson_id", "chapter_key", "course_id", "title", "stage", "sections"):
        if key not in ly:
            errors.append(f"V1 lesson.yaml missing key: {key}")
    seen_pages = []
    boxes_per_sec = {}
    for sec in ly.get("sections", []):
        if not SEC_RE.match(sec.get("id", "")):
            errors.append(f"V1 bad section id grammar: {sec.get('id')}")
        if sec.get("bookPage"):
            seen_pages.append(sec["bookPage"])
    if seen_pages != sorted(seen_pages):
        errors.append("V1 bookPage not monotonic across sections")
    stage = ly.get("stage", "S0")

    glossary = load_yaml(lesson / "glossary.yaml") if (lesson / "glossary.yaml").exists() else []
    gslugs = {g.get("slug") for g in (glossary or [])}
    for g in (glossary or []):
        if not g.get("ms_accepts"):
            warns.append(f"V6 glossary entry without ms_accepts: {g.get('slug')}")
        if len((g.get("definition") or "").split()) > 40:
            warns.append(f"V6 definition >40 words: {g.get('slug')}")

    n_secs = 0
    for f in section_files(lesson):
        fm, body, err = parse_section(f)
        if err:
            errors.append(f"V1 {f.name}: {err}")
            continue
        if not body.strip():
            errors.append(f"V8 empty section file: {f.name}")
            continue
        n_secs += 1
        sid = (fm or {}).get("id", "?")
        boxes = set(BOX_MARKER.findall(body))
        boxes_per_sec[f.name] = boxes
        # V2 provenance
        if not (fm or {}).get("authored"):
            if not (fm or {}).get("chunkRefs"):
                warns.append(f"V2 {f.name}: no chunkRefs provenance (PIN from parse of record)")
            if fm.get("bookPage") is None:
                warns.append(f"V2 {f.name}: bookPage unpinned")
        # V3 spec subset (warn when absent; error only if join_set known and violated)
        refs = (fm or {}).get("specRefs") or []
        if join and refs and not set(refs) <= join:
            errors.append(f"V3 {f.name}: specRefs outside chapter join set: {sorted(set(refs)-join)}")
        if stage >= "S3" and not refs:
            warns.append(f"V3 {f.name}: no specRefs (needed for derived links at S3+)")
        # V4 banned phrases — misconception boxes are EXCLUDED: quoting the
        # wrong idea is their job (lint-false-positive f-0002).
        misconception_blocks = re.findall(
            r"^:::misconception\n(.*?)^:::", body, re.S | re.M)
        scan_body = re.sub(
            r"^:::misconception\n.*?^:::", "", body, flags=re.S | re.M)
        low = scan_body.lower()
        for phrase in rules.get("banned_phrases", []):
            if phrase.lower() in low:
                errors.append(f"V4 banned phrase '{phrase}' in {f.name}")
        for pat in rules.get("banned_regex", []):
            if re.search(pat, body):
                errors.append(f"V4 OCR-artifact pattern /{pat}/ in {f.name}")
        # V6 chips
        for chip in re.findall(r"\[\[([^\]]+)\]\]", body):
            if chip not in gslugs:
                errors.append(f"V6 unresolved glossary chip [[{chip}]] in {f.name}")
        # V5 per-section coverage (only when stage >= S2)
        if stage >= "S2":
            if "exam-hint" not in boxes:
                warns.append(f"V5 {f.name}: no :::exam-hint box")
            if "misconception" not in boxes:
                warns.append(f"V5 {f.name}: no :::misconception box")
            if "quick-check" not in boxes and stage >= "S3":
                warns.append(f"V5 {f.name}: no quick-check")
    all_boxes = set().union(*boxes_per_sec.values()) if boxes_per_sec else set()
    if stage >= "S2":
        if "prior-knowledge" not in all_boxes:
            warns.append("V5 lesson missing a :::prior-knowledge box (first section)")
        if "cross-curricular" not in all_boxes:
            warns.append("V5 lesson missing a :::cross-curricular box")
        if "summary" not in all_boxes or "can-you" not in all_boxes:
            warns.append("V5 lesson missing closing :::summary / :::can-you boxes")

    # V9 receipts + tracker
    if not (lesson / "qa" / "receipt.yaml").exists():
        errors.append("V9 no qa/receipt.yaml — a stage without a receipt never happened")
    return errors, warns, infos


def cmd_lint(args):
    lesson = Path(args.lesson_dir).resolve()
    cdir = lesson.parent.parent
    errors, warns, _ = lint_lesson(lesson, cdir)
    for e in errors:
        print(f"ERROR {e}")
    for w in warns:
        print(f"WARN  {w}")
    print(f"lint: {len(errors)} errors, {len(warns)} warnings"
          + ("  → FAIL (exit 1)" if errors else "  → PASS"))
    return 1 if errors else 0


# ─────────────────────────────── tracker / findings ───────────────────────────
def cmd_tracker(args):
    lesson = Path(args.lesson_dir).resolve()
    ly = load_yaml(lesson / "lesson.yaml")
    tr_path = ROOT / "tracker.yaml"
    tr = load_yaml(tr_path)
    course = tr["courses"][ly["course_id"]]
    lid = ly["lesson_id"]
    entry = course.setdefault("lessons", {}).setdefault(lid, {})
    if args.receipt:
        rc = lesson / args.receipt
        if not rc.exists():
            sys.exit(f"receipt not found: {rc} (tracker law: no change without receipt)")
        entry["last_receipt"] = args.receipt
    for kv in args.set or []:
        k, v = kv.split("=", 1)
        if k == "sections_done":
            v = int(v)
        entry[k] = v
    entry["updated_at"] = now()
    tr["generated_at"] = now()
    tr_path.write_text(yaml.safe_dump(tr, sort_keys=False, allow_unicode=True), encoding="utf-8")
    # mirror into lesson.yaml receipts
    ly.setdefault("receipts", []).append({"date": now(), **{kv.split("=",1)[0]: kv.split("=",1)[1] for kv in (args.set or [])}})
    (lesson / "lesson.yaml").write_text(yaml.safe_dump(ly, sort_keys=False, allow_unicode=True), encoding="utf-8")
    # f-0006 fix: never print instructions for flags this CLI does not have.
    print(f"tracker updated: {lid} {args.set} (receipt: {args.receipt or 'n/a'}) — sync TRACKER.md (human doc of record) in the same commit")
    return 0


def cmd_finding(args):
    cdir = course_path(args.course)
    fjsonl = cdir / "findings.jsonl"
    lines = [json.loads(x) for x in fjsonl.read_text(encoding="utf-8").splitlines() if x.strip()] if fjsonl.exists() else []
    fid = f"f-{len(lines)+1:04d}"
    rec = {
        "id": fid, "date": now(), "agent": args.agent or os.environ.get("CL_AGENT", "unknown"),
        "type": args.type, "lesson": args.lesson, "section": args.section,
        "severity": args.severity, "what": args.what, "why": args.why,
        "fix": args.fix, "root_cause": args.root_cause, "system_change": args.system_change,
        "status": "open" if not args.fix else "closed",
    }
    with open(fjsonl, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"finding {fid} filed ({args.type}, {args.severity}) — root-cause-twice law applies on recurrence")
    return 0


# ─────────────────────────────── emit (S4) ────────────────────────────────────
def cmd_emit(args):
    lesson = Path(args.lesson_dir).resolve()
    ly = load_yaml(lesson / "lesson.yaml")
    errors, warns, _ = lint_lesson(lesson, lesson.parent.parent)
    if errors:
        print("emit blocked — lint errors:"); [print(" ", e) for e in errors]
        return 1
    sections = []
    for f in section_files(lesson):
        fm, body, _ = parse_section(f)
        sections.append({
            "id": fm.get("id"), "title": fm.get("title"), "bookPage": fm.get("bookPage"),
            "chunkRefs": fm.get("chunkRefs", []), "blockIds": fm.get("blocks", []),
            "glossarySlugs": fm.get("glossary", []), "specRefs": fm.get("specRefs", []),
            "markdown": body.strip(),
        })
    cfg = load_yaml(lesson.parent.parent / "course.yaml")
    row = next((r for rows in cfg["spine"].values()
                for r in rows if r["key"] == ly["chapter_key"]), {})
    bor, por = cfg["book_of_record"], cfg["parse_of_record"]
    pack = {
        "packId": ly["lesson_id"], "chapterKey": ly["chapter_key"],
        "courseId": cfg["course_slug"], "title": ly["title"],
        # verbatim from the chapter's learning_objective (course.yaml, chunk-derived)
        "learningObjective": row.get("learning_objective"),
        "paperRoute": "chemistry-only" if ly.get("chem_only") else "core",
        "sections": sections, "status": "draft", "version": 1,
        "sources": {
            # L1 provenance of record: path + sha256 (pinned at S0/first receipt)
            "bookOfRecord": f"{bor['path']} (sha256 {bor.get('sha256', 'unpinned')})",
            "parseOfRecord": f"{por['path']} (sha256 {por.get('sha256', 'unpinned')})",
            "blockPackReceipt": None,
        },
        "lintPack": cfg["lint_pack"],
    }
    out = lesson / "qa" / "lessonPackV1.json"
    out.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"emitted {out} (status=draft — SUGGESTED law; operator flip is separate)")
    return 0


def main():
    ap = argparse.ArgumentParser(prog="lessonctl")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("report"); r.add_argument("--course"); r.add_argument("--all", action="store_true"); r.add_argument("-v", "--verbose", action="store_true"); r.set_defaults(fn=cmd_report)
    s = sub.add_parser("scaffold"); s.add_argument("--course", required=True); s.add_argument("--chapter", required=True); s.add_argument("--sections", type=int, default=12); s.set_defaults(fn=cmd_scaffold)
    z = sub.add_parser("resume"); z.add_argument("lesson_dir"); z.set_defaults(fn=cmd_resume)
    l = sub.add_parser("lint"); l.add_argument("lesson_dir"); l.set_defaults(fn=cmd_lint)
    t = sub.add_parser("tracker"); t.add_argument("lesson_dir"); t.add_argument("--set", nargs="*"); t.add_argument("--receipt"); t.set_defaults(fn=cmd_tracker)
    f = sub.add_parser("finding"); f.add_argument("--course", required=True); f.add_argument("--type", required=True); f.add_argument("--lesson"); f.add_argument("--section"); f.add_argument("--severity", default="warn", choices=["info", "warn", "error"]); f.add_argument("--what", required=True); f.add_argument("--why"); f.add_argument("--fix"); f.add_argument("--root-cause", dest="root_cause"); f.add_argument("--system-change", dest="system_change"); f.add_argument("--agent"); f.set_defaults(fn=cmd_finding)
    e = sub.add_parser("emit"); e.add_argument("lesson_dir"); e.set_defaults(fn=cmd_emit)
    args = ap.parse_args()
    sys.exit(args.fn(args))


if __name__ == "__main__":
    main()
