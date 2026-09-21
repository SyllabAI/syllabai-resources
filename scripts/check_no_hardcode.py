"""C28 §3.2 mechanical no-hardcode check + registry consistency gate.

Legacy root-form store paths (graph/<store>.yaml) must not appear anywhere
under scripts/ outside the registry's allowlist — immutable verdict ledgers
are errata-bridged (P5: byte-untouched, resolved via graph_paths.resolve_rel).
Also validates registry integrity: store templates resolve on disk and, once
filled, legacy_map must equal the derived legacy->canonical mapping exactly.

Wired as S0 gates in scripts/c27_final_all_store_sweep.py; standalone run:
    python scripts/check_no_hardcode.py
"""
import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_PATTERN = re.compile(
    r"graph/(specification_points|topics|practicals|assessment_objectives|"
    r"command_words|relationships|concepts|concept_edges|spec_chunk_mappings|"
    r"spec_command_kinds)\.yaml"
)
# infra files that legitimately mention the mechanics (self-exclusion)
_INFRA = {"scripts/graph_paths.yaml", "scripts/graph_paths.py", "scripts/check_no_hardcode.py"}
_SCAN_SUFFIXES = {".py", ".yaml", ".yml", ".json", ".md", ".sh", ".txt"}


def scan():
    """Returns (bad, allowed): legacy-form hits outside/inside the allowlist.
    bad/allowed items are (repo_relative_path, hit_count)."""
    sys.path.insert(0, str(_HERE))
    import graph_paths as GP
    allow = set(GP.legacy_allowlist())
    bad, allowed = [], []
    for p in sorted(_HERE.rglob("*")):
        if not p.is_file() or p.suffix not in _SCAN_SUFFIXES:
            continue
        rel = p.relative_to(_HERE.parent).as_posix()
        if rel in _INFRA:
            continue
        try:
            txt = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        n = len(_PATTERN.findall(txt))
        if n:
            (allowed if rel in allow else bad).append((rel, n))
    return bad, allowed


def registry_consistency():
    """(ok, detail): every registered store resolves on disk; if legacy_map is
    filled it must equal the derived legacy->canonical mapping exactly."""
    sys.path.insert(0, str(_HERE))
    import graph_paths as GP
    reg_path = _HERE / "graph_paths.yaml"
    if not reg_path.exists():
        return False, "registry file missing"
    names = GP.store_names()
    missing = [n for n in names if not GP.store(n).exists()]
    if missing:
        return False, f"store paths do not resolve on disk: {missing[:3]}"
    lm = GP._reg().get("legacy_map") or {}
    derived = {GP.legacy_rel(n): GP.store_rel(n) for n in names}
    stage = (GP._reg().get("layout") or {}).get("qual_prefix", "")
    if lm and lm != derived:
        diff = {k for k in set(lm) | set(derived) if lm.get(k) != derived.get(k)}
        return False, f"legacy_map != derived mapping: {sorted(diff)[:3]}"
    if lm:
        return True, f"{len(names)}/{len(names)} stores resolve (post-migration layout); legacy_map == derived ({len(lm)})"
    return True, f"{len(names)}/{len(names)} stores resolve (pre-migration root layout, qual_prefix=''), legacy_map empty"


def main() -> int:
    bad, allowed = scan()
    print(f"no-hardcode scan (scripts/, C28 §3.2 pattern): {len(bad)} bad / {len(allowed)} allowlisted")
    for rel, n in bad:
        print(f"  FAIL {rel}: {n} legacy-form store ref(s)")
    for rel, n in allowed:
        print(f"  allowlisted (immutable ledger, P5 errata-bridged): {rel} ({n})")
    ok, detail = registry_consistency()
    print(f"registry consistency: {'OK' if ok else 'FAIL'} — {detail}")
    if bad or not ok:
        return 1
    print("CHECK GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
