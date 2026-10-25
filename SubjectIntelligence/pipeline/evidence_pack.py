#!/usr/bin/env python3
"""SIB evidence-pack builder — bounded excerpts with identity preserved (r0).

Licensing law (docs/PIPELINE.md §6): a pack carries source identity (repo, path,
sha256) and BOUNDED excerpts, each with its locator (page / line range / record
id). It never carries bulk corpus export or full documents. Caps are enforced in
code and recorded in the pack.

The extraction plan (which files, which locators) is supplied by the run agent as
a JSON spec — the builder enforces the caps and computes identities, the agent
decides where to look. Deterministic: same inputs -> same pack bytes.

Usage:
  python3 evidence_pack.py --library <LIBRARY> --artifact-id CUR-01 \
      --policy evidence_policy.yaml --resolution resolution_report.json \
      --spec pack_spec.json --out evidence_pack.json
"""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

MAX_EXCERPTS_PER_SOURCE = 60
MAX_CHARS_PER_EXCERPT = 1600
MAX_TOTAL_CHARS_PER_SOURCE = 40000
MAX_FILES_PER_SOURCE = 40


def _fail(msg: str):
    print(f"evidence_pack: FATAL: {msg}", file=sys.stderr)
    sys.exit(2)


def _sha256_text(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def _match(prefix: str, source_id: str) -> bool:
    if prefix == "*":
        return True
    return fnmatch.fnmatch(source_id, prefix)


def select_sources(policy: dict, family: str, manifest_sources: list[dict],
                   resolution: dict) -> tuple[list[dict], list[str]]:
    """Return (selected source dicts with policy role, blockers)."""
    fam = (policy.get("families") or {}).get(family)
    if fam is None:
        return [], [f"family {family} not declared in evidence policy"]
    selected, blockers = [], []
    res_by_id = {s["id"]: s for s in resolution.get("sources", [])}
    man_by_id = {s["id"]: s for s in manifest_sources}
    for role in ("primary", "supplementary", "legacy"):
        for prefix in fam.get(role, []) or []:
            for sid, man in man_by_id.items():
                if not _match(prefix, sid):
                    continue
                res = res_by_id.get(sid)
                status = (res or {}).get("status", "UNRESOLVED")
                if role == "primary" and status.startswith("FAILED"):
                    blockers.append(f"PRIMARY source {sid} failed preflight ({status})")
                    continue
                if status.startswith(("FAILED", "UNRESOLVED")):
                    continue
                selected.append({"source_id": sid, "role": role,
                                 "classification": man.get("classification", ""),
                                 "title": man.get("title", ""),
                                 "resolution_status": status})
    # dedupe (a source may match several role prefixes; strongest role wins)
    best: dict[str, dict] = {}
    order = {"primary": 0, "supplementary": 1, "legacy": 2}
    for s in selected:
        cur = best.get(s["source_id"])
        if cur is None or order[s["role"]] < order[cur["role"]]:
            best[s["source_id"]] = s
    return list(best.values()), blockers


def _md_locate(path: Path, query: re.Pattern | None, limit: int) -> list[dict]:
    """Line-window excerpts from markdown/text with line locators."""
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.split("\n")
    hits: list[int] = []
    if query is not None:
        for i, ln in enumerate(lines):
            if query.search(ln):
                hits.append(i)
    else:  # no query: structural index only (headings), never bulk text
        hits = [i for i, ln in enumerate(lines) if ln.startswith("#")]
    out, total = [], 0
    for h in hits[:limit]:
        lo, hi = max(0, h - 2), min(len(lines), h + 13)
        chunk = "\n".join(lines[lo:hi]).strip()
        if not chunk:
            continue
        chunk = chunk[:MAX_CHARS_PER_EXCERPT]
        total += len(chunk)
        if total > MAX_TOTAL_CHARS_PER_SOURCE:
            break
        out.append({"locator": f"lines {lo + 1}-{hi}", "chars": len(chunk), "text": chunk})
    return out


def _pdf_locate(path: Path, pages: list[int] | None, limit: int) -> list[dict]:
    """Page-ranged excerpts from PDF with page locators (pymupdf, optional)."""
    try:
        import fitz  # type: ignore
    except ImportError:
        return [{"locator": "file", "chars": 0,
                 "text": "(PDF text extraction unavailable: pymupdf not installed; "
                          "identity-only evidence entry)"}]
    doc = fitz.open(path)
    wanted = pages if pages else list(range(1, min(len(doc), limit) + 1))
    out, total = [], 0
    for pno in wanted[:limit]:
        if pno < 1 or pno > len(doc):
            continue
        text = doc[pno - 1].get_text("text").strip()
        if not text:
            continue
        text = text[:MAX_CHARS_PER_EXCERPT]
        total += len(text)
        if total > MAX_TOTAL_CHARS_PER_SOURCE:
            break
        out.append({"locator": f"page {pno}", "chars": len(text), "text": text})
    doc.close()
    return out


def build_pack(library: Path, artifact_id: str, family: str, run_id: str,
               policy: dict, resolution: dict, manifest_sources: list[dict],
               plan: dict) -> tuple[dict, list[str]]:
    """plan: {source_id: {files: [{path_suffix, repo}], md_query: regex, pdf_pages: [..]}}"""
    selected, blockers = select_sources(policy, family, manifest_sources, resolution)
    if blockers:
        return {}, blockers

    repo_roots = {k: Path(v) for k, v in (resolution.get("repo_roots") or {}).items()}
    res_by_id = {s["id"]: s for s in resolution.get("sources", [])}
    family_dir = library / "runs" / run_id / "evidence" / artifact_id
    family_dir.mkdir(parents=True, exist_ok=True)

    sources_out = []
    for sel in selected:
        sid = sel["source_id"]
        res = res_by_id[sid]
        plan_s = (plan or {}).get(sid, {})
        query = re.compile(plan_s["md_query"]) if plan_s.get("md_query") else None
        pages = plan_s.get("pdf_pages")
        files_out, total_chars = [], 0

        # candidate files: from the plan (exact) or from resolved entries (bounded)
        if plan_s.get("files"):
            cands = [(f.get("repo", ""), f["path_suffix"]) for f in plan_s["files"]]
        else:
            cands = [(e.get("repo", ""), e.get("path", ""))
                     for e in res.get("entries", [])
                     if str(e.get("status", "")).startswith("RESOLVED")][:MAX_FILES_PER_SOURCE]

        for repo, rel in cands:
            root = repo_roots.get(repo)
            if root is None:
                continue
            p = root / rel
            if not p.is_file():
                continue
            if p.suffix.lower() in (".md", ".txt"):
                excerpts = _md_locate(p, query, MAX_EXCERPTS_PER_SOURCE)
            elif p.suffix.lower() == ".pdf":
                excerpts = _pdf_locate(p, pages, MAX_EXCERPTS_PER_SOURCE)
            else:
                # binary/office: identity-only entry (no text extraction claimed)
                excerpts = []
            total_chars += sum(e["chars"] for e in excerpts)
            if total_chars > MAX_TOTAL_CHARS_PER_SOURCE:
                break
            files_out.append({
                "repo": repo, "path": rel,
                "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
                "excerpts": excerpts,
            })

        sources_out.append({**sel, "files": files_out,
                            "excerpt_caps": {"per_source_chars": MAX_TOTAL_CHARS_PER_SOURCE,
                                              "per_excerpt_chars": MAX_CHARS_PER_EXCERPT}})

    pack = {
        "schema": "sib-evidence-pack/1.0",
        "run_id": run_id,
        "artifact_id": artifact_id,
        "family": family,
        "library": library.name,
        "policy_version": policy.get("policy_version", ""),
        "sources": sources_out,
        "caps": {"max_excerpts_per_source": MAX_EXCERPTS_PER_SOURCE,
                  "max_chars_per_excerpt": MAX_CHARS_PER_EXCERPT,
                  "max_total_chars_per_source": MAX_TOTAL_CHARS_PER_SOURCE},
        "licensing_law": "bounded excerpts + locator identity preserved; no bulk export",
    }
    return pack, []


def main() -> int:
    ap = argparse.ArgumentParser(description="SIB evidence pack builder (SIB-GEN)")
    ap.add_argument("--library", required=True)
    ap.add_argument("--artifact-id", required=True)
    ap.add_argument("--family", default=None, help="override family (default: from artifact id prefix)")
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--policy", required=True)
    ap.add_argument("--resolution", required=True)
    ap.add_argument("--spec", default=None, help="extraction plan JSON (agent-authored, committed to the run record)")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    if yaml is None:
        _fail("PyYAML required")
    family = args.family or args.artifact_id.split("-")[0]
    policy = yaml.safe_load(Path(args.policy).read_text(encoding="utf-8"))
    resolution = json.loads(Path(args.resolution).read_text(encoding="utf-8"))
    library = Path(args.library)
    manifest = yaml.safe_load((library / "source_manifest.yaml").read_text(encoding="utf-8"))
    plan = json.loads(Path(args.spec).read_text(encoding="utf-8")) if args.spec else {}

    pack, blockers = build_pack(library, args.artifact_id, family, args.run_id,
                                 policy, resolution, manifest.get("sources", []), plan)
    if blockers:
        for b in blockers:
            print(f"evidence_pack: BLOCKED: {b}", file=sys.stderr)
        return 1

    pack_bytes = json.dumps(pack, indent=2, ensure_ascii=False) + "\n"
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(pack_bytes, encoding="utf-8")
    print(f"evidence_pack: {args.artifact_id} ({family}) "
          f"sources={len(pack['sources'])} sha256={_sha256_text(pack_bytes)} -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
