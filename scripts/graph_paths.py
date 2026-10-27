"""C28 graph-path registry resolver — single source of ratified-plane store paths.

Spec: graph/reports/C28_MULTI_SUBJECT_EXPANSION_SPEC.md §3.2.
Input: scripts/graph_paths.yaml (the registry). Tooling MUST resolve ratified
store paths through this module; hardcoded store paths outside the registry are
a check failure (scripts/check_no_hardcode.py, wired as an S0 gate in the sweep).

Stage resolution (layout.qual_prefix):
  ''                  pre-migration root layout   -> graph/<store>.yaml
  'igcse-chemistry'   post stage-2 git mv         -> graph/igcse-chemistry/<store>.yaml
legacy_rel(name) is stage-invariant: the historical root-form path string, for
record/ledger label compatibility (P5 — landed records are never edited).
resolve_rel(rel) maps any historical path through legacy_map (identity otherwise).
"""
from pathlib import Path

_HERE = Path(__file__).resolve().parent
REPO = _HERE.parent
_REG_CACHE = None


def _reg() -> dict:
    global _REG_CACHE
    if _REG_CACHE is None:
        import yaml
        _REG_CACHE = yaml.safe_load((_HERE / "graph_paths.yaml").read_text(encoding="utf-8"))
    return _REG_CACHE


def _norm(rel: str) -> str:
    """Collapse empty path segments ('graph/{QUAL}/x' with empty {QUAL})."""
    return "/".join(seg for seg in rel.split("/") if seg)


def default_qual() -> str:
    return _reg()["default_qual"]


def _qual_seg(qual: str) -> str:
    """Path segment for a qual's store dir under graph/.

    Pre-migration the migrating (default) qual lives at the graph/ root ('');
    post-migration — and for any future qual — it lives at graph/<qual>/."""
    reg = _reg()
    pre = (reg.get("layout") or {}).get("qual_prefix", "")
    if qual == reg.get("default_qual") and pre == "":
        return ""
    return qual


def store_names(qual: str = None) -> list:
    reg = _reg()
    q = qual or reg["default_qual"]
    return list(reg["quals"][q]["stores"].keys())


def store_rel(name: str, qual: str = None) -> str:
    """Canonical repo-relative store path as a posix string (post-stage state)."""
    reg = _reg()
    q = qual or reg["default_qual"]
    tpl = reg["quals"][q]["stores"][name]
    return _norm(tpl.replace("{QUAL}", _qual_seg(q)))


def store(name: str, qual: str = None) -> Path:
    """Canonical absolute store path."""
    return REPO / store_rel(name, qual)


def qual_dir(qual: str = None) -> Path:
    """Directory holding the qual's ratified stores."""
    reg = _reg()
    q = qual or reg["default_qual"]
    return REPO / "graph" / _qual_seg(q)


def reports_dir(qual: str = None) -> Path:
    """Shared audit-trail directory (graph/reports/ — never per-qual)."""
    reg = _reg()
    q = qual or reg["default_qual"]
    return REPO / _norm(reg["quals"][q]["reports_dir"])


def legacy_rel(name: str) -> str:
    """Historical root-form path (stage-invariant label, e.g. pinned in records)."""
    return f"graph/{name}.yaml"


def resolve_rel(rel: str) -> str:
    """Resolve any repo-relative path; historical root-form store paths map to
    their canonical location via the registry legacy_map (identity otherwise)."""
    lm = _reg().get("legacy_map") or {}
    return lm.get(rel, rel)


def legacy_allowlist() -> list:
    return list(_reg().get("legacy_allowlist") or [])
