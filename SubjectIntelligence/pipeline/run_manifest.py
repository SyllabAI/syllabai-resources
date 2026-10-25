#!/usr/bin/env python3
"""SIB run-record writer — receipted generation runs (SIB-GEN law 7).

Every generation run opens a run record under <LIBRARY>/runs/<RUN_ID>/:
    run_manifest.yaml   inputs (source revisions, evidence-pack hash, generator
                        provider/model, prompt-pack version, settings)
    receipt.yaml        outputs (artifact files + sha256, per-artifact outcomes,
                        validator QA result when available)

Run-ID convention: SIB-<LIBRARY>-<ARTIFACT>-RUN-<NNN> (NNN = 001, 002, … per
library+artifact; the number is derived from existing run dirs, never guessed).
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None


class RunError(SystemExit):
    def __init__(self, msg: str):
        super().__init__(f"FATAL (run record): {msg}")


def _require_yaml() -> None:
    if yaml is None:
        raise RunError("PyYAML is required by the SIB run-record writer")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def next_run_id(library: Path, course: str, artifact_id: str) -> str:
    runs = library / "runs"
    prefix = f"SIB-{course}-{artifact_id}-RUN-"
    n = 0
    if runs.is_dir():
        for child in runs.iterdir():
            if child.name.startswith(prefix):
                try:
                    n = max(n, int(child.name[len(prefix):]))
                except ValueError:
                    continue
    return f"{prefix}{n + 1:03d}"


def open_run(library: Path, course: str, artifact_ids: list[str], resolution: dict,
             packs: dict, generator: dict, settings: dict | None = None) -> dict:
    """Create runs/<RUN_ID>/run_manifest.yaml. One run per artifact (pilot law)."""
    _require_yaml()
    if len(artifact_ids) != 1:
        raise RunError("one run per artifact (batch orchestration lands after the pilot)")
    artifact_id = artifact_ids[0]
    run_id = next_run_id(library, course, artifact_id)
    run_dir = library / "runs" / run_id
    if run_dir.exists():
        raise RunError(f"run dir already exists: {run_dir} (never overwrite a run record)")
    run_dir.mkdir(parents=True)
    manifest = {
        "run_id": run_id,
        "course": course,
        "artifact_ids": artifact_ids,
        "opened_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_revisions": resolution.get("source_revisions", {}),
        "resolution_record_sha256": sha256_text(
            json.dumps(resolution, sort_keys=True, ensure_ascii=True)),
        "evidence_packs": {aid: {"pack_sha256": p["pack_sha256"],
                                 "items": len(p["items"])}
                           for aid, p in packs.items()},
        "generator": {
            "provider": generator.get("provider", "z.ai"),
            "model": generator.get("model", ""),
            "prompt_pack": generator.get("prompt_pack", "SIB_ZAI_PROMPTS_V1"),
            "agent_notes": generator.get("agent_notes", ""),
        },
        "settings": settings or {},
        "outcomes": {},  # artifact_id -> {state, artifact_file, artifact_sha256, ...}
    }
    (run_dir / "run_manifest.yaml").write_text(
        yaml.safe_dump(manifest, sort_keys=True, allow_unicode=True))
    return {"run_id": run_id, "run_dir": run_dir, "manifest": manifest}


def record_outcome(run: dict, artifact_id: str, state: str, **details) -> None:
    manifest = run["manifest"]
    manifest["outcomes"][artifact_id] = {"state": state, **details}
    path = run["run_dir"] / "run_manifest.yaml"
    path.write_text(yaml.safe_dump(manifest, sort_keys=True, allow_unicode=True))


def close_run(run: dict, summary: str) -> None:
    _require_yaml()
    manifest = run["manifest"]
    manifest["closed_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    manifest["summary"] = summary
    (run["run_dir"] / "run_manifest.yaml").write_text(
        yaml.safe_dump(manifest, sort_keys=True, allow_unicode=True))


def attach_resolution(run: dict, resolution: dict) -> None:
    (run["run_dir"] / "resolution.json").write_text(
        json.dumps(resolution, indent=2, sort_keys=True) + "\n")


def attach_pack(run: dict, artifact_id: str, pack: dict) -> None:
    ev = run["run_dir"] / "evidence"
    ev.mkdir(exist_ok=True)
    (ev / f"{artifact_id}.pack.json").write_text(
        json.dumps(pack, indent=2, ensure_ascii=False) + "\n")


def main() -> int:  # pragma: no cover - thin CLI for ad-hoc inspection
    ap = argparse.ArgumentParser(description="Inspect a SIB run record")
    ap.add_argument("run_dir", type=Path)
    args = ap.parse_args()
    _require_yaml()
    print((args.run_dir / "run_manifest.yaml").read_text())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
