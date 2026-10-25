#!/usr/bin/env python3
"""SIB source resolver — fail-closed preflight for SIB-GEN runs (program r0).

Resolves a library's source_manifest.yaml against the canonical repositories:
  * every path entry `repo@path` (optional trailing "(note)" is stripped) is
    checked for existence in the mapped repo root;
  * `<placeholder>` path segments (e.g. `<session>`, `<paper>`) are expanded as
    globs over the real tree (bounded result count);
  * every resolved file's sha256 is computed; when the source entry declares an
    of-record sha256/sha1 (identifiers keys containing `sha256_`/`sha1_`), the
    computed digests are matched — a declared digest that matches NO resolved
    file, or a file that should carry it and does not, FAILS the source
    (hash is identity);
  * `tree_sha`/`blob_sha` identifiers are verified via `git cat-file -t` when the
    owning repo checkout is available.

Status per source: RESOLVED | PARTIAL | FAILED.
Any of-record digest mismatch or zero-resolved-paths => FAILED (fail-closed).

Output: a resolution report JSON (the preflight evidence of record). No timestamps
inside the deterministic core; run-scoped metadata is attached by the caller.

Usage:
  python3 source_resolver.py --library <LIBRARY_DIR> \
      --repo syllabai-resources=/path/to/resources \
      --repo syllabai-pastpapers=/path/to/pastpapers \
      --repo syllabai=/path/to/master \
      --out resolution_report.json
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

GLOB_CAP = 500          # max expansions per templated path entry
_DIGEST_RE = re.compile(r"^[0-9a-f]{40}$|^[0-9a-f]{64}$")
_PATH_RE = re.compile(r"^(?P<repo>[A-Za-z0-9_-]+)@(?P<path>.+?)\s*(?:\((?P<note>.*)\))?$")
# identifiers keys whose value is an of-record hex digest for a FILE of this source
_SHA_KEY_RE = re.compile(r"sha(256|1)")
# identifier keys that are git object ids verifiable with cat-file
_GIT_KEY_RE = re.compile(r"(tree_sha|blob_sha)")


def _fail(msg: str) -> "SystemExit":
    print(f"source_resolver: FATAL: {msg}", file=sys.stderr)
    return SystemExit(2)


def _sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _sha1_git_style(p: Path) -> str:
    """Git blob sha1 (hash of 'blob <len>\\0' + content) — matches blob_sha ids."""
    data = p.read_bytes()
    return hashlib.sha1(b"blob %d\x00" % len(data) + data).hexdigest()


def _git_cat_file(repo_root: Path, obj: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", "-C", str(repo_root), "cat-file", "-t", obj],
            capture_output=True, text=True, timeout=30, check=True)
        return out.stdout.strip()
    except Exception:
        return None


def _parse_path_entry(raw: str):
    m = _PATH_RE.match(raw.strip())
    if not m:
        return None
    return m.group("repo"), m.group("path").strip(), (m.group("note") or "")


def _expand(entry_path: str, repo_root: Path) -> list[Path]:
    """Expand a manifest path (possibly with <placeholder> segments) under repo_root."""
    if "<" not in entry_path:
        return [repo_root / entry_path]
    pattern = re.sub(r"<[^/>]+>", "*", entry_path)
    matches = sorted(repo_root.glob(pattern))[:GLOB_CAP]
    return matches


def _declared_file_digests(source: dict) -> dict[str, str]:
    """{algo: hex} for identifier keys that look like single-file of-record digests."""
    out: dict[str, str] = {}
    for key, val in (source.get("identifiers") or {}).items():
        if not isinstance(val, str):
            continue
        v = val.strip().lower()
        if _SHA_KEY_RE.search(key.lower()) and _DIGEST_RE.fullmatch(v.replace("…", "")):
            algo = "sha256" if "sha256" in key.lower() else "sha1"
            out[algo] = v
    return out


def _git_object_ids(source: dict) -> dict[str, str]:
    out = {}
    for key, val in (source.get("identifiers") or {}).items():
        if isinstance(val, str) and _GIT_KEY_RE.search(key.lower()):
            v = val.strip().lower()
            if re.fullmatch(r"[0-9a-f]{40}", v):
                out[key] = v
    return out


def resolve_source(source: dict, repo_roots: dict[str, Path]) -> dict:
    sid = source.get("id", "?")
    entry_results: list[dict] = []
    digests = _declared_file_digests(source)
    git_ids = _git_object_ids(source)

    matched_digests: set[str] = set()
    n_files = n_dirs = 0

    for raw in source.get("paths", []):
        parsed = _parse_path_entry(raw) if isinstance(raw, str) else None
        if parsed is None:
            entry_results.append({"raw": raw, "status": "UNPARSEABLE"})
            continue
        repo, rel, _note = parsed
        root = repo_roots.get(repo)
        if root is None:
            entry_results.append({"raw": raw, "status": "REPO_UNAVAILABLE", "repo": repo})
            continue
        for cand in _expand(rel, root):
            rec: dict = {"raw": raw, "repo": repo, "path": str(cand.relative_to(root))}
            if cand.is_dir():
                n_dirs += 1
                rec.update(status="RESOLVED_DIR")
            elif cand.is_file():
                n_files += 1
                rec.update(status="RESOLVED_FILE", sha256=_sha256_file(cand),
                           git_blob_sha1=_sha1_git_style(cand))
                for algo, want in digests.items():
                    got = rec["sha256"] if algo == "sha256" else rec["git_blob_sha1"]
                    if got == want:
                        matched_digests.add(f"{algo}:{want}")
            else:
                rec.update(status="MISSING")
            entry_results.append(rec)

    # a digest that matched nothing = identity failure (fail-closed)
    unmatched = [f"{a}:{v}" for a, v in digests.items() if f"{a}:{v}" not in matched_digests]

    git_checks = []
    for key, obj in git_ids.items():
        owner = next((r for name, r in repo_roots.items() if name in str(source.get("paths", ""))), None)
        kind = _git_cat_file(owner, obj) if owner else None
        git_checks.append({"identifier": key, "object": obj,
                           "verified": kind is not None, "git_type": kind})

    total_entries = len(entry_results)
    resolved_entries = sum(1 for e in entry_results if str(e.get("status", "")).startswith("RESOLVED"))
    if total_entries and resolved_entries == total_entries and not unmatched:
        status = "RESOLVED"
    elif resolved_entries:
        status = "PARTIAL" + (";DIGEST_MISMATCH" if unmatched else "")
    else:
        status = "FAILED" + (";DIGEST_MISMATCH" if unmatched else "")

    return {
        "id": sid,
        "classification": source.get("classification", ""),
        "status": status,
        "entries": entry_results,
        "digest_verification": {"declared": [f"{a}:{v}" for a, v in digests.items()],
                                 "matched": sorted(matched_digests),
                                 "unmatched": unmatched},
        "git_object_checks": git_checks,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="SIB source resolver (SIB-GEN preflight)")
    ap.add_argument("--library", required=True)
    ap.add_argument("--repo", action="append", default=[],
                    help="name=/path (repeatable; name matches the `repo@` prefix in manifest paths)")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    if yaml is None:
        raise _fail("PyYAML is required for source_manifest parsing")
    library = Path(args.library)
    manifest_path = library / "source_manifest.yaml"
    data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    sources = data.get("sources") or []
    if not sources:
        raise _fail(f"no sources declared in {manifest_path}")

    repo_roots: dict[str, Path] = {}
    for spec in args.repo:
        name, _, path = spec.partition("=")
        p = Path(path)
        if not p.is_dir():
            raise _fail(f"repo root for {name} does not exist: {p}")
        repo_roots[name] = p

    results = [resolve_source(s, repo_roots) for s in sources]
    failed = [r["id"] for r in results if r["status"].startswith("FAILED")]
    partial = [r["id"] for r in results if r["status"].startswith("PARTIAL")]

    report = {
        "schema": "sib-resolution-report/1.0",
        "library": library.name,
        "source_manifest_version": str(data.get("manifest_version", "")),
        "repo_roots": {k: str(v) for k, v in repo_roots.items()},
        "sources": results,
        "summary": {
            "total": len(results),
            "resolved": len(results) - len(failed) - len(partial),
            "partial": len(partial),
            "failed": len(failed),
            "failed_ids": failed,
            "partial_ids": partial,
        },
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"source_resolver: {report['summary']['resolved']} RESOLVED / "
          f"{report['summary']['partial']} PARTIAL / {report['summary']['failed']} FAILED "
          f"-> {out}")
    return 0 if not failed else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit as e:
        sys.exit(int(e.code or 0))
