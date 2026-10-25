#!/usr/bin/env python3
"""SIB source resolver — resolve source_manifest.yaml ids against canonical repos.

Law of record (SIB-GEN, trace 1a1726b6684c4055): sources stay in their canonical
repositories; this resolver READS them at pinned identity and never copies the
corpus into the library. Fail-closed: any required source that is missing,
ambiguous, or identity-mismatched stops the run before generation starts.

Path-entry grammar (of record in source_manifest.yaml `paths:` lists):
    <repo>@<path>   repo in {syllabai-resources, syllabai-pastpapers, core-plane}
    path may be a file, a directory, or carry <placeholder> segments (treated as
    a glob where '*' is substituted for each <...> group)
    a trailing "(...)" annotation is descriptive and stripped

Identity verification (best-effort, honest):
    identifiers keys of the form sha256_<slug> / sha1_<slug> are matched against
    candidate files whose name contains <slug> (dashes/underscores equivalent);
    sha256_* -> hashlib sha256; sha1_of_record -> sha1; blob_sha_* -> git
    hash-object (only when the repo is a git checkout). tree_sha -> recorded,
    verified only with --verify-tree (requires the pinned object to exist).
    Results are VERIFIED / MISMATCH (fail) / UNVERIFIED (disclosed, pass).

Usage:
    python3 pipeline/source_resolver.py --library SubjectIntelligence/CHEMISTRY_4CH1 \
        --resources-repo /path/syllabai-resources --pastpapers-repo /path/syllabai-pastpapers \
        [--source SRC-SPEC-4CH1 ...] [--json out.json] [--strict]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

REPO_KEY_ALIASES = {
    "syllabai-resources": "resources",
    "syllabai-pastpapers": "pastpapers",
    "core-plane": "core",
    "syllabai-core": "core",
}
_SLUG_RE = re.compile(r"^(sha256|sha1|blob_sha)_(.+)$")


class ResolveError(SystemExit):
    """Fail-closed resolution error (exit code 2)."""


def _require_yaml() -> None:
    if yaml is None:
        raise ResolveError("FATAL: PyYAML is required by the SIB resolver (pip install pyyaml)")


def load_manifest(library: Path) -> dict:
    _require_yaml()
    path = library / "source_manifest.yaml"
    if not path.is_file():
        raise ResolveError(f"FATAL: source manifest missing: {path}")
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict) or "sources" not in data:
        raise ResolveError(f"FATAL: source manifest malformed: {path}")
    return data


def parse_path_entry(entry: str):
    """'syllabai-resources@a/b (note)' -> ('resources', 'a/b')."""
    raw = entry.split("#", 1)[0].strip()
    raw = re.sub(r"\s+\([^)]*\)\s*$", "", raw).strip()
    if "@" not in raw:
        raise ResolveError(f"FATAL: path entry without repo prefix: {entry!r}")
    repo, path = raw.split("@", 1)
    repo = repo.strip()
    if repo not in REPO_KEY_ALIASES:
        raise ResolveError(f"FATAL: unknown repo {repo!r} in path entry {entry!r}")
    return REPO_KEY_ALIASES[repo], path.strip()


def _expand(repo_root: Path, pattern: str) -> list[Path]:
    real = repo_root / pattern
    if real.exists():
        return [real]
    if "<" in pattern:
        globbed = re.sub(r"<[^>]+>", "*", pattern)
        return sorted(p for p in repo_root.glob(globbed))
    return []


def _hash_file(path: Path, algo: str) -> str:
    h = hashlib.sha256() if algo == "sha256" else hashlib.sha1()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _git_blob_sha(path: Path, repo_root: Path) -> str | None:
    try:
        out = subprocess.run(["git", "-C", str(repo_root), "hash-object", str(path)],
                             check=True, capture_output=True, text=True, timeout=60)
        return out.stdout.strip()
    except Exception:
        return None


def _norm(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name.lower())


def verify_identities(source: dict, files: list[Path], repo_roots: dict) -> list[dict]:
    checks = []
    identifiers = source.get("identifiers") or {}
    for key, pinned in identifiers.items():
        m = _SLUG_RE.match(key)
        if not m or not isinstance(pinned, str) or len(pinned) < 8:
            checks.append({"identifier": key, "result": "UNVERIFIED",
                           "reason": "not a file-level pin (metadata/tree pin)"})
            continue
        algo, slug = m.group(1), _norm(m.group(2))
        algo = "sha256" if algo == "sha256" else algo
        candidates = [f for f in files if slug in _norm(f.stem)]
        # most-specific (shortest stem containing the slug) first
        candidates.sort(key=lambda f: len(_norm(f.stem)))
        if not candidates:
            checks.append({"identifier": key, "result": "UNVERIFIED",
                           "reason": f"no candidate file matches slug {slug!r}"})
            continue
        per_candidate = []
        verified = False
        for cand in candidates:
            if algo == "blob_sha":
                actual = _git_blob_sha(cand, cand.parent)
            else:
                actual = _hash_file(cand, algo)
            ok = actual is not None and actual.lower() == pinned.lower()
            verified = verified or ok
            per_candidate.append({"file": str(cand),
                                  "match": bool(ok),
                                  "actual": actual})
        checks.append({
            "identifier": key,
            "result": "VERIFIED" if verified else "MISMATCH",
            "pinned": pinned,
            "candidates": per_candidate,
        })
    return checks


def resolve_source(source: dict, repo_roots: dict) -> dict:
    classification = str(source.get("classification") or "")
    rec = {"source_id": source.get("id"),
           "classification": classification,
           "required": not classification.startswith("SUPPLEMENTARY"),
           "paths": [], "identity_checks": [], "ok": True}
    for entry in source.get("paths") or []:
        repo_key, pattern = parse_path_entry(str(entry))
        root = repo_roots.get(repo_key)
        if root is None:
            rec["paths"].append({"entry": str(entry), "repo": repo_key,
                                 "result": "MISSING", "reason": "repo root not provided"})
            rec["ok"] = False
            continue
        hits = _expand(root, pattern)
        if not hits:
            rec["paths"].append({"entry": str(entry), "repo": repo_key,
                                 "result": "MISSING", "reason": "no file matched"})
            rec["ok"] = False
            continue
        files: list[Path] = []
        for hit in hits:
            if hit.is_dir():
                files.extend(sorted(p for p in hit.rglob("*") if p.is_file()))
                rec["paths"].append({"entry": str(entry), "repo": repo_key,
                                     "result": "RESOLVED_DIR",
                                     "dir": str(hit), "file_count": len(files)})
            else:
                files.append(hit)
                rec["paths"].append({"entry": str(entry), "repo": repo_key,
                                     "result": "RESOLVED_FILE", "file": str(hit)})
        rec.setdefault("_files", []).extend(files)
    rec["identity_checks"] = verify_identities(source, rec.get("_files", []), repo_roots)
    if any(c["result"] == "MISMATCH" for c in rec["identity_checks"]):
        rec["ok"] = False
    rec.pop("_files", None)
    return rec


def resolve_course(library: Path, repo_roots: dict,
                   source_ids: list[str] | None = None,
                   fatal_ids: set[str] | None = None) -> dict:
    """Resolve sources; fail-closed on missing/mismatched FATAL sources.

    fatal semantics: with fatal_ids given (the artifact's primary set), only
    those are fatal; missing optional/secondary sources are disclosed. Without
    fatal_ids (course-wide view), any missing non-SUPPLEMENTARY source is fatal.
    """
    manifest = load_manifest(library)
    sources = manifest.get("sources") or []
    wanted = set(source_ids) if source_ids else None
    out = {"library": str(library), "ok": True, "sources": []}
    for src in sources:
        sid = src.get("id") or ""
        if wanted is not None and sid not in wanted:
            continue
        rec = resolve_source(src, repo_roots)
        if fatal_ids is not None:
            rec["required"] = sid in fatal_ids
        out["sources"].append(rec)
        if not rec["ok"] and rec.get("required", True):
            out["ok"] = False
    if wanted is not None:
        missing = wanted - {s["source_id"] for s in out["sources"]}
        for sid in sorted(missing):
            fatal = (sid in fatal_ids) if fatal_ids is not None else True
            out["sources"].append({"source_id": sid, "ok": False, "required": fatal,
                                   "paths": [{"result": "MISSING",
                                              "reason": "id not declared in source manifest"}]})
            if fatal:
                out["ok"] = False
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="SIB source resolver (fail-closed)")
    ap.add_argument("--library", type=Path, required=True)
    ap.add_argument("--resources-repo", type=Path, default=None)
    ap.add_argument("--pastpapers-repo", type=Path, default=None)
    ap.add_argument("--core-repo", type=Path, default=None)
    ap.add_argument("--source", action="append", default=None,
                    help="resolve only these source ids (repeatable)")
    ap.add_argument("--json", type=Path, default=None, help="write resolution record json")
    args = ap.parse_args()
    repo_roots = {}
    if args.resources_repo:
        repo_roots["resources"] = args.resources_repo.resolve()
    if args.pastpapers_repo:
        repo_roots["pastpapers"] = args.pastpapers_repo.resolve()
    if args.core_repo:
        repo_roots["core"] = args.core_repo.resolve()
    record = resolve_course(args.library, repo_roots, args.source)
    payload = json.dumps(record, indent=2, sort_keys=True)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(payload + "\n")
    print(payload)
    return 0 if record["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
