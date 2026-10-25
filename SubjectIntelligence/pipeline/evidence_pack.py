#!/usr/bin/env python3
"""SIB evidence-pack builder — bounded, identity-preserving source context.

Law of record (SIB-GEN): the Z.ai agent is grounded exclusively in the evidence
pack. The pack records for every item the canonical source id, repo, path,
sha256/bytes (identity) and LOCATORS (page/chunk/question ranges where known);
verbatim excerpts are included ONLY for text-structured files within per-item
bounds — licensing law: bounded excerpts with preserved identity, never bulk
corpus export. PDFs are recorded by identity + locator guidance; text extraction
is a separate, disclosed step, never faked in-pack.

Policy input: <LIBRARY>/evidence_policy.yaml — per family:
    families:
      CUR:
        primary_sources: [SRC-SPEC-4CH1, ...]     # must resolve (fail-closed)
        optional_sources: [...]                   # resolved if present, else disclosed
        restrictions: [ ... free-text laws ... ]
        max_items: 24
        max_excerpt_chars: 12000
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

TEXT_SUFFIXES = {".json", ".yaml", ".yml", ".txt", ".md", ".csv", ".tsv", ".py"}


class PackError(SystemExit):
    def __init__(self, msg: str):
        super().__init__(f"FATAL (evidence pack): {msg}")


def load_policy(library: Path) -> dict:
    if yaml is None:
        raise PackError("PyYAML is required by the SIB evidence-pack builder")
    path = library / "evidence_policy.yaml"
    if not path.is_file():
        raise PackError(f"evidence policy missing: {path}")
    policy = yaml.safe_load(path.read_text())
    if not isinstance(policy, dict) or "families" not in policy:
        raise PackError(f"evidence policy malformed: {path}")
    return policy


def family_of(artifact_id: str) -> str:
    fam = artifact_id.split("-")[0].strip().upper()
    if not fam.isalpha() or not (2 <= len(fam) <= 4):
        raise PackError(f"cannot derive family from artifact id {artifact_id!r}")
    return fam


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build_item(source: dict, path: Path, max_excerpt: int) -> dict:
    item = {
        "source_id": source.get("id"),
        "classification": source.get("classification"),
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": _sha256(path),
        "locator": {},
    }
    if path.suffix.lower() in TEXT_SUFFIXES and item["bytes"] <= 4 * (1 << 20):
        text = path.read_text(errors="replace")
        item["excerpt"] = text[:max_excerpt]
        item["excerpt_chars"] = len(item["excerpt"])
        item["truncated"] = len(text) > max_excerpt
        if path.suffix.lower() == ".json" and not item["truncated"]:
            try:
                data = json.loads(text)
                if isinstance(data, dict):
                    item["locator"]["json_keys"] = sorted(data.keys())[:32]
            except Exception:
                pass
    else:
        item["excerpt"] = None
        item["excerpt_chars"] = 0
        item["truncated"] = False
        item["locator"]["note"] = (
            "binary/document source — identity pinned above; text extraction is a "
            "separate disclosed step; cite by document + page/question locator")
    return item


def build_pack(library: Path, artifact_id: str, resolution: dict,
               policy: dict | None = None, max_items: int = 24,
               max_excerpt_chars: int = 12000) -> dict:
    if yaml is None:
        raise PackError("PyYAML is required by the SIB evidence-pack builder")
    policy = policy or load_policy(library)
    fam = family_of(artifact_id)
    entry = (policy.get("families") or {}).get(fam)
    if entry is None:
        raise PackError(f"no evidence-policy entry for family {fam} (artifact {artifact_id})")
    by_id = {s["source_id"]: s for s in resolution.get("sources", []) if s.get("ok")}
    primary = list(entry.get("primary_sources") or [])
    optional = list(entry.get("optional_sources") or [])
    missing = [sid for sid in primary if sid not in by_id]
    if missing:
        raise PackError(
            f"required primary sources did not resolve: {missing} — "
            "fail-closed; fix the preflight before generating")
    fam_limits = {k: entry[k] for k in ("max_items", "max_excerpt_chars") if k in entry}
    max_items = fam_limits.get("max_items", max_items)
    max_excerpt = fam_limits.get("max_excerpt_chars", max_excerpt_chars)

    manifest_path = library / "source_manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text())
    src_meta = {s.get("id"): s for s in manifest.get("sources") or []}

    items = []
    for sid in primary + optional:
        rec = by_id.get(sid)
        files = [] if rec is None else _collect_files(resolution, sid)
        if rec is None:
            items.append({"source_id": sid, "status": "UNRESOLVED",
                          "role": "optional" if sid in optional else "primary",
                          "disclosure": "did not resolve; disclosed, never fabricated"})
            continue
        if not files:
            items.append({"source_id": sid, "status": "DECLARED_ONLY",
                          "role": "primary" if sid in primary else "optional",
                          "disclosure": "resolved as directory/manifest pointer without "
                                        "direct file hits in this run; identity recorded "
                                        "in the resolution record"})
            continue
        for path in files[:max_items]:
            item = build_item(src_meta.get(sid, {}), path, max_excerpt)
            item["role"] = "primary" if sid in primary else "optional"
            items.append(item)
    pack = {
        "pack_version": 1,
        "artifact_id": artifact_id,
        "family": fam,
        "library": str(library),
        "built_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "restrictions": list(entry.get("restrictions") or []),
        "primary_sources": primary,
        "optional_sources": optional,
        "unresolved_optional": [i["source_id"] for i in items if i.get("status") == "UNRESOLVED"],
        "items": items,
    }
    canonical = json.dumps(pack, sort_keys=True, ensure_ascii=True).encode()
    pack["pack_sha256"] = hashlib.sha256(canonical).hexdigest()
    return pack


def _collect_files(resolution: dict, sid: str) -> list[Path]:
    files = []
    for src in resolution.get("sources", []):
        if src.get("source_id") != sid:
            continue
        for p in src.get("paths", []):
            if p.get("result") == "RESOLVED_FILE" and p.get("file"):
                files.append(Path(p["file"]))
            elif p.get("result") == "RESOLVED_DIR" and p.get("dir"):
                d = Path(p["dir"])
                files.extend(sorted(q for q in d.rglob("*") if q.is_file()))
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description="SIB evidence-pack builder")
    ap.add_argument("--library", type=Path, required=True)
    ap.add_argument("--artifact", required=True)
    ap.add_argument("--resolution", type=Path, required=True,
                    help="resolution record json from source_resolver.py")
    ap.add_argument("--out", type=Path, required=True, help="pack json output path")
    args = ap.parse_args()
    resolution = json.loads(args.resolution.read_text())
    pack = build_pack(args.library, args.artifact, resolution)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(pack, indent=2, ensure_ascii=False) + "\n")
    print(f"pack {pack['pack_sha256'][:16]}… items={len(pack['items'])} -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
