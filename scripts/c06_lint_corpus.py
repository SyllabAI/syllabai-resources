#!/usr/bin/env python3
"""T-C06 corpus lint for SME-RevisionNotes tranches (scraper schema
`syllabai.sme-revision-notes-course/1.0` notes).

Deterministic machine checks (CONTENT_CORPUS_ARCHITECTURE.md §5 adapted to the
scraped corpus shape): identity agreement md↔sidecar↔manifest, heading
grammar, spec-point id ↔ body-marker agreement, asset-ref resolution, sub/sup
tag balance, OCR-decay warnings (unicode sub/sup, bare formula digits, ASCII
arrows, LaTeX presence), duplicate note ids and duplicate content
fingerprints. Hard errors block conversion; warnings are recorded only.

Usage: python3 c06_lint_corpus.py <corpus-dir> <out-dir>
  corpus-dir holds manifest.json, assets_listing.json, mirror_index.json and
  the mirrored notes/ tree (produce it by mirroring the tranche folder at a
  pinned commit; index the md sha256 per note as in mirror_index.json).
Writes C06_LINT_REPORT.json + C06_LINT_REPORT.md; exit 1 iff hard errors.
"""
import hashlib
import json
import os
import re
import sys

UNICODE_SUBSUP = re.compile(r"[\u00b2\u00b3\u00b9\u2070-\u209f\u207b\u207c\u207a]")
FM_KEYS_REQUIRED = ["note_id", "title", "source", "path", "updated_at",
                    "spec_point_ids", "spec_point_codes", "guided_study"]
SIDECAR_SCHEMA = "syllabai.sme-revision-note/1.0"
SPEC_MARKER = re.compile(r"^>\s*\*\*Spec point\*\*\s*—\s*`?(spcpt_[A-Za-z0-9]+)`?\s*$")
IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
LATEX = re.compile(r"\$\$?[^$]+\$\$?|\\frac\{|\\times\b|\\cdot\b|\\leq\b|\\geq\b")
FORMULA_BARE = re.compile(r"\b[A-Z][a-z]?\d")


def parse_front_matter(md_text):
    if not md_text.startswith("---\n"):
        return None, ["front matter missing (file must start with '---')"]
    end = md_text.find("\n---\n", 4)
    if end < 0:
        return None, ["front matter not closed with '---'"]
    block = md_text[4:end]
    fm, problems, order = {}, [], []
    for line in block.split("\n"):
        if not line.strip():
            continue
        if ":" not in line:
            problems.append(f"front matter line without ':' : {line[:60]!r}")
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        if key in fm:
            problems.append(f"duplicate front-matter key {key}")
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            fm[key] = [s.strip().strip('"') for s in inner.split(",")] if inner else []
        elif val.startswith('"') and val.endswith('"'):
            fm[key] = val[1:-1]
        elif val in ("true", "false"):
            fm[key] = val == "true"
        else:
            fm[key] = val
        order.append(key)
    missing = [k for k in FM_KEYS_REQUIRED if k not in fm]
    if missing:
        problems.append(f"missing required front-matter keys: {missing}")
    return fm, problems


def body_after_front_matter(md_text):
    end = md_text.find("\n---\n", 4)
    return md_text[end + 5:] if end >= 0 else md_text


def lint_note(rel_md, md_b, js_b, manifest_page, asset_names):
    hard, warn = [], []
    md_text = md_b.decode("utf-8", errors="strict")
    try:
        sidecar = json.loads(js_b.decode("utf-8"))
    except Exception as e:
        return {"path": rel_md, "hard": [f"sidecar JSON unparsable: {e}"], "warn": []}

    fm, fm_problems = parse_front_matter(md_text)
    hard.extend(fm_problems)
    if fm is None:
        return {"path": rel_md, "hard": hard, "warn": warn}

    if sidecar.get("schema") != SIDECAR_SCHEMA:
        hard.append(f"sidecar schema {sidecar.get('schema')!r} != {SIDECAR_SCHEMA}")
    if fm.get("note_id") != sidecar.get("note_id"):
        hard.append(f"note_id mismatch md={fm.get('note_id')!r} sidecar={sidecar.get('note_id')!r}")
    if fm.get("note_id") != manifest_page.get("rn_id"):
        hard.append(f"note_id mismatch manifest={manifest_page.get('rn_id')!r}")
    if fm.get("title") != sidecar.get("title"):
        hard.append(f"title mismatch md={fm.get('title')!r} sidecar={sidecar.get('title')!r}")
    if fm.get("title") != manifest_page.get("title"):
        hard.append(f"title mismatch manifest={manifest_page.get('title')!r}")
    if not re.fullmatch(r"rn_[A-Za-z0-9]+", str(fm.get("note_id", ""))):
        hard.append(f"note_id format unexpected: {fm.get('note_id')!r}")
    leaf = sidecar.get("path", {}).get("leaf")
    if leaf and not rel_md.endswith("/" + leaf + ".md"):
        hard.append(f"sidecar leaf {leaf!r} disagrees with file path {rel_md!r}")

    body = body_after_front_matter(md_text)
    lines = body.split("\n")

    h1 = [ln[2:].strip() for ln in lines if re.match(r"^# (?!#)", ln)]
    if len(h1) != 1:
        hard.append(f"H1 count {len(h1)} != 1")
    elif h1[0] != fm.get("title"):
        hard.append(f"H1 {h1[0]!r} != front-matter title {fm.get('title')!r}")
    levels = [len(m.group(1)) for ln in lines
              if (m := re.match(r"^(#{1,6})(?!#)", ln))]
    for prev, cur in zip(levels, levels[1:]):
        if cur > prev + 1:
            warn.append(f"heading level skip {prev}->{cur}")

    marker_ids = [m.group(1) for ln in lines if (m := SPEC_MARKER.match(ln.strip()))]
    fm_ids = fm.get("spec_point_ids") or []
    for mid in marker_ids:
        if mid not in fm_ids:
            hard.append(f"marker {mid} not in front-matter spec_point_ids")
    for fid in fm_ids:
        if fid not in marker_ids:
            warn.append(f"front-matter id {fid} has no body spec-point marker")
    if not fm_ids:
        warn.append("note declares no spec points")

    figs = IMG.findall(body)
    remote_refs = [ref for _a, ref in figs if ref.startswith(("http://", "https://"))]
    local_refs = [ref for _a, ref in figs if not ref.startswith(("http://", "https://"))]
    unres = [ref for ref in local_refs if ref.rsplit("/", 1)[-1] not in asset_names]
    if unres:
        hard.append(f"{len(unres)} image ref(s) not in assets/: {sorted(set(unres))[:3]}")
    if remote_refs:
        warn.append(f"{len(remote_refs)} remote (non-mirrored) figure ref(s) — kept verbatim per house rule")
    no_alt = sum(1 for alt, _r in figs if not alt.strip())

    opens = len(re.findall(r"<sub>", body)) + len(re.findall(r"<sup>", body))
    closes = len(re.findall(r"</sub>", body)) + len(re.findall(r"</sup>", body))
    if opens != closes:
        hard.append(f"unbalanced sub/sup tags: {opens} open vs {closes} close")

    if UNICODE_SUBSUP.search(body):
        warn.append("unicode sub/superscript characters present")
    bare = FORMULA_BARE.findall(re.sub(r"<su[bp]>.{0,40}?</su[bp]>", "", body))
    if bare:
        warn.append(f"{len(bare)} formula-adjacent bare digit(s) e.g. {bare[:3]}")
    if re.search(r"(?<!-)->(?!>)|<->|=>", body):
        warn.append("ASCII arrow present")
    if LATEX.search(body):
        warn.append("LaTeX constructs present")

    norm = re.sub(r"\s+", " ", re.sub(r"[#*`>\-\[\]()!_|:,.']", "", body)).strip().lower()
    fingerprint = hashlib.sha256(norm.encode()).hexdigest()[:16]

    stats = {
        "headings": sum(1 for ln in lines if re.match(r"^#{1,6}(?!#)\s", ln)),
        "list_items": sum(1 for ln in lines if re.match(r"^[-*]\s+", ln)),
        "figures": len(figs),
        "figures_remote": len(remote_refs),
        "figures_no_alt": no_alt,
        "spec_markers": len(marker_ids),
        "spec_point_ids": len(fm_ids),
        "latex_inline_math": len(re.findall(r"\$[^$]+\$", body)),
        "chars": len(md_text),
        "fingerprint": fingerprint,
    }
    return {"path": rel_md, "note_id": fm.get("note_id"), "hard": hard,
            "warn": warn, "stats": stats}


def main():
    corpus, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    manifest = json.load(open(f"{corpus}/manifest.json"))
    index = json.load(open(f"{corpus}/mirror_index.json"))
    assets = json.load(open(f"{corpus}/assets_listing.json"))
    asset_names = set(assets["names"])

    by_path = {e["path"]: e for e in index["pages"]}
    records, seen_ids, seen_fp = [], {}, {}
    for page in manifest["pages"]:
        rel = page["path"]
        entry = by_path.get(rel)
        if entry is None:
            records.append({"path": rel, "hard": ["mirrored file missing"], "warn": []})
            continue
        md_b = open(f"{corpus}/{entry['md_path']}", "rb").read()
        js_b = open(f"{corpus}/{rel}", "rb").read()
        if hashlib.sha256(md_b).hexdigest() != entry["md_sha256"]:
            records.append({"path": rel, "hard": ["mirror checksum drift"], "warn": []})
            continue
        rec = lint_note(entry["md_path"], md_b, js_b, page, asset_names)
        if rec.get("note_id"):
            seen_ids.setdefault(rec["note_id"], []).append(rel)
        fp = rec.get("stats", {}).get("fingerprint")
        if fp:
            seen_fp.setdefault(fp, []).append(rel)
        records.append(rec)

    for nid, paths in seen_ids.items():
        if len(paths) > 1:
            for r in records:
                if r.get("note_id") == nid:
                    r["hard"].append(f"duplicate note_id across corpus ({len(paths)} files)")
    for fp, paths in seen_fp.items():
        if len(paths) > 1:
            for r in records:
                if r.get("stats", {}).get("fingerprint") == fp:
                    r["warn"].append(f"duplicate content fingerprint across {len(paths)} notes")

    hard_count = sum(1 for r in records if r["hard"])
    warn_count = sum(1 for r in records if r["warn"])
    totals = {
        "notes": len(records),
        "notes_with_hard_errors": hard_count,
        "notes_with_warnings": warn_count,
        "hard_findings": sum(len(r["hard"]) for r in records),
        "warning_findings": sum(len(r["warn"]) for r in records),
        "figures": sum(r.get("stats", {}).get("figures", 0) for r in records),
        "figures_remote": sum(r.get("stats", {}).get("figures_remote", 0) for r in records),
        "figures_no_alt": sum(r.get("stats", {}).get("figures_no_alt", 0) for r in records),
        "latex_inline_math": sum(r.get("stats", {}).get("latex_inline_math", 0) for r in records),
        "spec_markers": sum(r.get("stats", {}).get("spec_markers", 0) for r in records),
        "spec_point_ids": sum(r.get("stats", {}).get("spec_point_ids", 0) for r in records),
        "list_items": sum(r.get("stats", {}).get("list_items", 0) for r in records),
        "chars": sum(r.get("stats", {}).get("chars", 0) for r in records),
        "assets_mirrored": len(asset_names),
    }
    warn_kinds = {}
    for r in records:
        for w in r["warn"]:
            key = re.sub(r"\d+", "N", w)
            warn_kinds[key] = warn_kinds.get(key, 0) + 1

    report = {
        "tool": "c06_lint_corpus.py",
        "version": "1.0.0",
        "pinned_commit": index["pinned_commit"],
        "manifest_sha256": index["manifest_sha256"],
        "totals": totals,
        "warning_kinds": dict(sorted(warn_kinds.items(), key=lambda kv: -kv[1])),
        "records": sorted(records, key=lambda r: r["path"]),
    }
    with open(f"{out}/C06_LINT_REPORT.json", "w") as f:
        json.dump(report, f, indent=1)
    verdict = "PASS" if hard_count == 0 else "FAIL"
    with open(f"{out}/C06_LINT_REPORT.md", "w") as f:
        f.write(f"# C06 Corpus Lint — pinned {index['pinned_commit'][:12]}\n\n"
                f"Verdict: **{verdict}** — {totals['notes']} notes, "
                f"{hard_count} with hard errors, {warn_count} with warnings.\n")
    print(f"LINT {verdict}: {totals['notes']} notes, {totals['hard_findings']} hard, "
          f"{totals['warning_findings']} warnings -> {out}")
    return 0 if hard_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
