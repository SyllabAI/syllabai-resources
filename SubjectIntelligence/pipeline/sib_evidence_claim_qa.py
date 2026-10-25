#!/usr/bin/env python3
"""SIB evidence-claim QA — every citation must resolve to the artifact's own evidence
pack (r2, BL-008 pass 3).

r2 (BL-008 pass 3, EXP wave):
  * FAMILY-GENERAL record blocks: `### <FAM>-NNN —` any family prefix (r1 was
    MIS-only; pass 3 authors EXP records);
  * JSONL LINE LOCATORS: citation path grammar accepts `.jsonl`; a locator spec
    may carry `line N` (book-chunk citations) alongside the `pN`/`ppN-M` page
    forms; every requested page/line must exist as an excerpt of the cited
    pack file, and quoted fragments bind to the cited excerpts as before.

Upgrade over the wave-1 script (which was never committed — disclosed in the BL-008
pass-4 receipts):
  * r1 CITATION BINDING: quoted fragments in a record's Evidence line must appear in
    the cited pack excerpt (normalised whitespace/punctuation matching); an ellipsis
    (…) splits a quote into fragments, each of which must resolve;
  * r1 REGEX REPAIR (single-page-citation fail-open hole closed): the page grammar now
    parses `pN`, `pN and pM`, `ppN` and `ppN-M` forms; a parenthetical that STARTS with
    a source id or census.json but fails to parse is a VIOLATION (never skipped).

Citation grammar checked (inside parentheses):
  (SRC-<ID>, identity)                      — source must exist in the pack (any role)
  (SRC-<ID>, <path-suffix> <page-spec>)     — path must suffix-match a pack file of that
                                              source; every page (pN/ppN-M) or JSONL line
                                              (line N) in <page-spec> must have a matching
                                              excerpt in that file
  (census.json, <dotted.path>)              — path must resolve inside the run census annex

Exit code 0 = 0 violations across all artifacts; 1 = violations found (fail-closed).

Usage:
  python3 sib_evidence_claim_qa.py --library <LIB> --run-dir <runs/RUN> \
      --artifacts MIS-02 MIS-03 ... [--out <report.json>]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

_CITE_RE = re.compile(r"\((SRC-[A-Z0-9][A-Z0-9-]*|census\.json)\s*,\s*([^)]+)\)")
_PAGE_RE = re.compile(r"p{1,2}\s*(\d+)")
_LINE_RE = re.compile(r"lines?\s*(\d+)")
_PATH_RE = re.compile(r"^[^,]+?\.(?:pdf|md|yaml|yml|json|jsonl|txt)$")


def _norm(t: str) -> str:
    t = unicodedata.normalize("NFKC", t)
    for a, b in (("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"'),
                 ("\u2013", "-"), ("\u2014", "-"), ("\u00ba", "\u00b0"),
                 ("\u2192", "->"), ("\u2212", "-")):
        t = t.replace(a, b)
    t = re.sub(r"\s+", " ", t)
    return t.lower().strip()


def load_pack(run_dir: Path, aid: str) -> dict:
    return json.loads((run_dir / "evidence" / aid / "evidence_pack.json").read_text(encoding="utf-8"))


def check_artifact(aid: str, text: str, pack: dict, census: dict) -> dict:
    violations: list[str] = []
    checked = 0

    pack_files: dict[str, dict] = {}   # source_id -> {path -> {"pages": {..}, "lines": {..}}}
    pack_ids = set()
    for s in pack.get("sources", []):
        sid = s["source_id"]
        pack_ids.add(sid)
        for f in s.get("files", []):
            pages = {int(m.group(1)): e.get("text", "") for e in f.get("excerpts", [])
                     for m in [re.match(r"page (\d+)$", e.get("locator", ""))] if m}
            lines = {int(m.group(1)): e.get("text", "") for e in f.get("excerpts", [])
                     for m in [re.match(r"line (\d+) ", e.get("locator", ""))] if m}
            pack_files.setdefault(sid, {})[f["path"]] = {"pages": pages, "lines": lines}

    def parse_citation(target: str, payload: str) -> tuple[str | None, set | None]:
        """Returns (matched_pack_path|None|'identity', locator keys|None).
        Keys are (kind, n) with kind in {"page", "line"}. Appends violations."""
        if _norm(payload) == "identity":
            return "identity", None
        pm = re.match(r"(.+?\.(?:pdf|md|yaml|yml|jsonl|json|txt))\s*(.*)", payload)
        if not pm:
            violations.append(f"{aid}: citation unparseable (fail-closed): ({target}, {payload})")
            return None, None
        path_part, page_spec = pm.group(1).strip(), pm.group(2).strip()
        files = pack_files.get(target, {})
        matched = {p: locs for p, locs in files.items() if p.endswith(path_part) or path_part.endswith(p)}
        if not matched:
            violations.append(f"{aid}: cited path not in pack: {target}, {path_part}")
            return None, None
        if not page_spec:
            violations.append(f"{aid}: file citation without locator (fail-closed): ({target}, {payload})")
            return None, None
        page_ns = {int(x) for x in _PAGE_RE.findall(page_spec)}
        line_ns = {int(x) for x in _LINE_RE.findall(page_spec)}
        keys = {("page", n) for n in page_ns} | {("line", n) for n in line_ns}
        if not keys:
            violations.append(f"{aid}: no page/line parsed from '{page_spec}' (fail-closed): ({target}, {payload})")
            return None, None
        for kind, n in sorted(keys):
            bucket = "pages" if kind == "page" else "lines"
            if not any(n in locs[bucket] for locs in matched.values()):
                violations.append(f"{aid}: {kind} {n} not in pack excerpts: {target}, {path_part}")
        return next(iter(matched)), keys

    # locate record blocks (### <FAM>-NNN — ... up to next ###/## heading; r2: any family)
    blocks: list[tuple[str, str, int]] = []  # (record_id, block_text, offset)
    for m in re.finditer(r"^###\s+([A-Z]{2,4}-\d{3})\s+—", text, re.M):
        start = m.start()
        nxt = re.search(r"^###[ \t]|^##[ \t]", text[m.end():], re.M)
        end = m.end() + (nxt.start() if nxt else len(text) - m.end())
        blocks.append((m.group(1), text[start:end], start))

    for rid, block, _off in blocks:
        cites = []  # (matched_path, pages, target)
        for m in _CITE_RE.finditer(block):
            checked += 1
            target, payload = m.group(1), m.group(2).strip()
            if target == "census.json":
                node = census
                ok = True
                for part in payload.strip().rstrip(".").split("."):
                    if isinstance(node, list):
                        try:
                            node = node[int(part)]
                        except Exception:
                            ok = False; break
                    elif isinstance(node, dict) and part in node:
                        node = node[part]
                    else:
                        ok = False; break
                if not ok:
                    violations.append(f"{aid}/{rid}: census path unresolved: {payload}")
                continue
            if target not in pack_ids:
                violations.append(f"{aid}/{rid}: source not in pack: {target}")
                continue
            path, keys = parse_citation(target, payload)
            if path and path != "identity" and keys:
                cites.append((path, keys))
        # r2 per-record quote binding: every quoted fragment (>=25 chars, >=4 words)
        # in the record must appear in the union of THAT record's cited excerpts
        corpus = _norm(" ".join(
            t for path, keys in cites
            for kind, n in keys
            for t in [pack_excerpt_texts(pack, path).get("pages" if kind == "page" else "lines", {}).get(n, "")]))
        # drop the heading line from quote scanning (titles may quote short phrases)
        block_body = "\n".join(block.splitlines()[1:])
        for frag in re.split(r"\u2026|\.\.\.", block_body):
            for q in _grounded_quotes(frag):
                words = q.split()
                if len(words) >= 4 and _norm(q) not in corpus:
                    violations.append(
                        f"{aid}/{rid}: quote not grounded in the record's own cited pack "
                        f"excerpts: \"{q[:70]}...\"")
    return {"artifact_id": aid, "citations_checked": checked, "violations": violations,
            "violation_count": len(violations)}


def _grounded_quotes(frag: str) -> list[str]:
    """Quoted spans whose opening quote follows a citation-ish context (start of text,
    ':', ';', '(', or an em/en dash) — prevents mis-pairing across adjacent short
    phrase-quotes."""
    out = []
    for m in re.finditer(r'"([^"]{25,})"', frag):
        before = frag[:m.start()].rstrip()
        prev = before[-1:] or "\n"
        if prev in ":;(-\u2014\u2013" or before == "":
            out.append(m.group(1))
    return out


def pack_excerpt_texts(pack: dict, path: str) -> dict[str, dict[int, str]]:
    """All excerpt texts for one pack file path, keyed by locator kind (r2).
    Returns {"pages": {n: text}, "lines": {n: text}}."""
    out: dict[str, dict[int, str]] = {"pages": {}, "lines": {}}
    for s in pack.get("sources", []):
        for f in s.get("files", []):
            if f["path"] == path:
                for e in f.get("excerpts", []):
                    mp = re.match(r"page (\d+)$", e.get("locator", ""))
                    ml = re.match(r"line (\d+) ", e.get("locator", ""))
                    if mp:
                        out["pages"][int(mp.group(1))] = e.get("text", "")
                    elif ml:
                        out["lines"][int(ml.group(1))] = e.get("text", "")
                return out
    return {}


def main() -> int:
    ap = argparse.ArgumentParser(description="SIB evidence-claim QA (r2, citation binding)")
    ap.add_argument("--library", required=True)
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--artifacts", nargs="+", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    run_dir = Path(args.run_dir)
    census = json.loads((run_dir / "census.json").read_text(encoding="utf-8"))
    results = []
    for aid in args.artifacts:
        pack = load_pack(run_dir, aid)
        art_dir = Path(args.library) / "artifacts"
        fname = next(f for f in sorted(art_dir.glob(f"*_{aid}_*.md")))
        text = fname.read_text(encoding="utf-8")
        results.append(check_artifact(aid, text, pack, census))

    report = {
        "schema": "sib-evidence-claim-qa/1.2",
        "script": "SubjectIntelligence/pipeline/sib_evidence_claim_qa.py r2",
        "law": "every (SRC-*, locator) resolves to the artifact's own pack; every "
               "(census.json, path) resolves to the run census annex; quoted fragments "
               "bind to the cited excerpts (r1); page or JSONL-line locators verified "
               "against pack excerpts (r2); unparseable citations fail closed",
        "artifacts": results,
        "totals": {"citations_checked": sum(r["citations_checked"] for r in results),
                   "violations": sum(r["violation_count"] for r in results)},
    }
    out = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(out, encoding="utf-8")
    print(out)
    return 1 if report["totals"]["violations"] else 0


if __name__ == "__main__":
    sys.exit(main())
