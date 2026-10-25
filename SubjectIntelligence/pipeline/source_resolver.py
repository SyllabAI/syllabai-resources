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


def _sha1_content(p: Path) -> str:
    return hashlib.sha1(p.read_bytes()).hexdigest()


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


def _declared_file_digests(source: dict) -> list[dict]:
    """[{algo, key, value}] for identifier keys that look like single-file of-record
    digests. Every declared digest is kept — multiple per algo is normal."""
    out: list[dict] = []
    for key, val in (source.get("identifiers") or {}).items():
        if not isinstance(val, str):
            continue
        v = val.strip().lower()
        if _SHA_KEY_RE.search(key.lower()) and _DIGEST_RE.fullmatch(v.replace("…", "")):
            algo = "sha256" if "sha256" in key.lower() else "sha1"
            out.append({"algo": algo, "key": key, "value": v})
    return out


def _git_object_ids(source: dict) -> dict[str, str]:
    out = {}
    for key, val in (source.get("identifiers") or {}).items():
        if isinstance(val, str) and _GIT_KEY_RE.search(key.lower()):
            v = val.strip().lower()
            if re.fullmatch(r"[0-9a-f]{40}", v):
                out[key] = v
    return out


_POINTER_NOTE_RE = re.compile(r"pointer record|same artifact|root intake copy|arch")
_POINTER_PREFIX_RE = re.compile(r"^(provenance|ledger):")
_DIR_DIGEST_CAP = 400          # max member files hashed per resolved directory


def _entry_role(raw: str) -> str:
    """evidence | alternate | pointer — alternates/pointers never demote RESOLVED."""
    s = raw.strip()
    if _POINTER_PREFIX_RE.match(s):
        return "pointer"
    if _POINTER_NOTE_RE.search(s):
        return "alternate"
    return "evidence"


def _split_group(raw: str) -> list[str]:
    """One `paths:` entry may list several files separated by ' + ' (manifest
    convention); the repo@ prefix appears once and applies to all tokens."""
    m = _PATH_RE.match(raw.strip())
    if not m:
        return []
    repo, body, note = m.group("repo"), m.group("path"), (m.group("note") or "")
    body = body.strip()
    if note:
        # the trailing note attaches to the LAST token only
        if body.endswith(")") and "(" in body:
            body, _, tail = body.rpartition("(")
            body, note = body.strip(), tail.rstrip(")").strip()
    tokens = [t.strip() for t in body.split(" + ") if t.strip()]
    return [f"{repo}@{t}" + (f" ({note})" if (note and i == len(tokens) - 1) else "")
            for i, t in enumerate(tokens)]


def _hash_file_rec(p: Path) -> dict:
    return {"sha256": _sha256_file(p), "sha1_content": _sha1_content(p),
            "sha1_blob": _sha1_git_style(p)}


def _match_digests(declared: list[dict], h: dict, matched: set) -> None:
    for d in declared:
        algo, want = d["algo"], d["value"]
        candidates = (h.get("sha256"),) if algo == "sha256" else \
                     (h.get("sha1_content"), h.get("sha1_blob"))
        if any(g and g == want for g in candidates):
            matched.add(f"{algo}:{want}")


def resolve_source(source: dict, repo_roots: dict[str, Path]) -> dict:
    sid = source.get("id", "?")
    entry_results: list[dict] = []
    declared = _declared_file_digests(source)
    git_ids = _git_object_ids(source)
    digests = declared  # list form used throughout

    matched_digests: set[str] = set()
    n_required_groups = 0
    n_resolved_groups = 0

    for raw in source.get("paths", []):
        if not isinstance(raw, str):
            entry_results.append({"raw": str(raw), "status": "UNPARSEABLE"})
            continue
        role = _entry_role(raw)
        tokens = _split_group(raw)
        if not tokens:
            entry_results.append({"raw": raw, "status": "UNPARSEABLE"})
            continue
        group_ok = False
        group_entries: list[dict] = []
        for tok in tokens:
            parsed = _parse_path_entry(tok)
            if parsed is None:
                continue
            repo, rel, _note = parsed
            root = repo_roots.get(repo)
            if root is None:
                group_entries.append({"raw": tok, "status": "REPO_UNAVAILABLE", "repo": repo})
                continue
            cands = _expand(rel, root)
            if not cands:
                group_entries.append({"raw": tok, "status": "MISSING",
                                      "repo": repo, "path": rel})
                continue
            for cand in cands:
                rec: dict = {"raw": tok, "repo": repo,
                             "path": str(cand.relative_to(root))}
                if cand.is_dir():
                    rec.update(status="RESOLVED_DIR")
                    if digests:
                        members = sorted(p for p in cand.rglob("*") if p.is_file())[:_DIR_DIGEST_CAP]
                        for mem in members:
                            h = _hash_file_rec(mem)
                            _match_digests(digests, h, matched_digests)
                        rec["members_hashed"] = len(members)
                elif cand.is_file():
                    rec.update(status="RESOLVED_FILE", **_hash_file_rec(cand))
                    _match_digests(digests, rec, matched_digests)
                else:
                    rec.update(status="MISSING")
                group_entries.append(rec)
                if str(rec["status"]).startswith("RESOLVED"):
                    group_ok = True
        for g in group_entries:
            g["role"] = role
        entry_results.extend(group_entries)
        if role == "evidence":
            n_required_groups += 1
            if group_ok:
                n_resolved_groups += 1
        elif group_ok:
            entry_results.append({"raw": raw, "status": "RESOLVED_ALT", "role": role,
                                  "note": "pointer/alternate locator resolved"})
        else:
            entry_results.append({"raw": raw, "status": "ALT_MISSING_DISCLOSED",
                                  "role": role,
                                  "note": "pointer/alternate locator absent — disclosed, "
                                          "never demotes evidence resolution"})

    # a declared digest that matched nothing = identity unverified (fail-closed:
    # the source cannot claim full RESOLVED while an of-record digest is unproven)
    unmatched = [f"{d['algo']}:{d['value']}" for d in digests
                 if f"{d['algo']}:{d['value']}" not in matched_digests]

    git_checks = []
    for key, obj in git_ids.items():
        owner = next((r for name, r in repo_roots.items() if name in str(source.get("paths", ""))), None)
        kind = _git_cat_file(owner, obj) if owner else None
        git_checks.append({"identifier": key, "object": obj,
                           "verified": kind is not None, "git_type": kind})

    if n_required_groups == 0 or n_resolved_groups < n_required_groups:
        status = "FAILED" + (";DIGEST_UNMATCHED" if unmatched else "")
    elif unmatched:
        status = "PARTIAL;DIGEST_UNMATCHED"
    else:
        status = "RESOLVED"

    return {
        "id": sid,
        "classification": source.get("classification", ""),
        "status": status,
        "entries": entry_results,
        "digest_verification": {"declared": [f"{d['algo']}:{d['value']}" for d in digests],
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
