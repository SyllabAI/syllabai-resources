#!/usr/bin/env python3
"""
official_examq_g9_casegen.py — deterministic generator for the G9 benchmark
case manifest (Official-ExamQuestion/benchmark/cases.json).

G9 = Learner-Surface Quality gate (rendered). The case manifest is the FROZEN
benchmark contract: expected semantic facts, counts, censuses, MCQ
interactions, solution expectations and label samples, all derived from the
hub official bundles of record (syllabai-v2
apps/hub/content/<course>/official-papers.json — the H3-cutover exports of
the resources corpus of record).

Re-derivation discipline: cases.json is versioned and committed; this script
documents its derivation. Editing expectations by hand requires a BUMP of
`benchmark_version` and a LEDGER entry (benchmark anti-gaming rule).

Usage:
  python3 official_examq_g9_casegen.py \
    --bundles-dir /path/to/apps/hub/content \
    --out cases.json
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from official_examq_g9_semantics import (  # noqa: E402 — the F120 shared label law
    LABEL_GRAMMAR_RE, bundle_label_of, label_from_offp_id,
)

# F129 bump (v3 -> v4): the ALL-PAPERS contract. The 2026-11-01 full-paper
# rendered audit ("check all the papers") swept every official paper of the
# three ADR-037 lanes through the real hub — 175 paper surfaces. The frozen
# 8-case contract cannot describe that surface, so the contract is
# RE-DERIVED at full breadth: every official paper topic of the three lanes
# is a frozen case (CASE_DEFS below is the complete static list), and each
# case additionally freezes the 0.7 census expectations (ordered question
# ids, exact content-image count, exact MCQ option count). Two contract
# derivation fixes rode the audit (both fail-closed, both receipted):
#   FIX-4 (solution-fact picker): the picker could freeze (a) markdown
#   list-item lines ("- Carbon (C): 38.4 ÷ 12 = 3.2") whose rendered form
#   drops the leading marker, and (b) squashed mark-scheme table debris
#   ("124 + 180 oe 2 M1 270 + 34 commonly seen.") that no surface renders
#   verbatim. The hardened picker refuses list-marker heads and mark-scheme
#   debris patterns; papers whose solutionMd carries no clean prose freeze
#   NO solution fact (their case then runs the honest reveal-presence
#   path) — never a snippet the surface cannot render.
#   FIX-5 is a runner fix (either-surface solution probing) and lives in
#   official_examq_g9_render_check.py 0.7.
BENCHMARK_VERSION = 4
VALIDATOR_VERSION = "g9-render-check/0.7"

# (case_id, lane, course, topic_slug_suffix) — the COMPLETE official paper
# universe of the three lanes at the bundles of record (175 papers:
# chemistry 54, physics 55, maths-B 66), sorted per lane by slug.
CASE_DEFS = [
    ("chemistry-1c-2019-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2019-06"),
    ("chemistry-1c-2020-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2020-01"),   # v3 legacy case (hand rationale kept)
    ("chemistry-1c-2020-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2020-11"),
    ("chemistry-1c-2021-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2021-01"),
    ("chemistry-1c-2021-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2021-06"),
    ("chemistry-1c-2021-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2021-11"),
    ("chemistry-1c-2022-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2022-01"),
    ("chemistry-1c-2022-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2022-06"),
    ("chemistry-1c-2023-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2023-01"),
    ("chemistry-1c-2023-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2023-06"),   # v3 legacy case (hand rationale kept)
    ("chemistry-1c-2023-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2023-11"),
    ("chemistry-1c-2024-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2024-06"),
    ("chemistry-1c-2024-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2024-11"),
    ("chemistry-1c-2025-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2025-06"),
    ("chemistry-1c-2025-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2025-11"),
    ("chemistry-1c-2026-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1c-2026-06"),
    ("chemistry-1cr-2019-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1cr-2019-06"),
    ("chemistry-1cr-2020-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1cr-2020-01"),
    ("chemistry-1cr-2020-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1cr-2020-11"),
    ("chemistry-1cr-2021-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1cr-2021-01"),
    ("chemistry-1cr-2022-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1cr-2022-01"),
    ("chemistry-1cr-2022-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1cr-2022-06"),
    ("chemistry-1cr-2023-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1cr-2023-01"),
    ("chemistry-1cr-2023-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1cr-2023-06"),
    ("chemistry-1cr-2024-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1cr-2024-06"),
    ("chemistry-1cr-2025-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1cr-2025-06"),
    ("chemistry-1cr-2026-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-1cr-2026-06"),
    ("chemistry-2c-2019-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2019-06"),   # v3 legacy case (hand rationale kept)
    ("chemistry-2c-2020-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2020-01"),
    ("chemistry-2c-2020-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2020-11"),
    ("chemistry-2c-2021-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2021-01"),
    ("chemistry-2c-2021-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2021-06"),
    ("chemistry-2c-2021-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2021-11"),
    ("chemistry-2c-2022-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2022-01"),
    ("chemistry-2c-2022-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2022-06"),
    ("chemistry-2c-2023-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2023-01"),
    ("chemistry-2c-2023-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2023-06"),
    ("chemistry-2c-2023-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2023-11"),
    ("chemistry-2c-2024-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2024-06"),
    ("chemistry-2c-2024-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2024-11"),
    ("chemistry-2c-2025-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2025-06"),
    ("chemistry-2c-2025-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2025-11"),
    ("chemistry-2c-2026-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2c-2026-06"),
    ("chemistry-2cr-2019-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2cr-2019-06"),
    ("chemistry-2cr-2020-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2cr-2020-01"),
    ("chemistry-2cr-2020-11", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2cr-2020-11"),
    ("chemistry-2cr-2021-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2cr-2021-01"),
    ("chemistry-2cr-2022-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2cr-2022-01"),
    ("chemistry-2cr-2022-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2cr-2022-06"),
    ("chemistry-2cr-2023-01", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2cr-2023-01"),
    ("chemistry-2cr-2023-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2cr-2023-06"),
    ("chemistry-2cr-2024-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2cr-2024-06"),
    ("chemistry-2cr-2025-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2cr-2025-06"),
    ("chemistry-2cr-2026-06", "igcse-chemistry-19", "igcse-chemistry-19", "official-4ch1-2cr-2026-06"),
    ("physics-1p-2019-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2019-06"),   # v3 legacy case (hand rationale kept)
    ("physics-1p-2020-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2020-01"),
    ("physics-1p-2020-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2020-06"),
    ("physics-1p-2020-11", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2020-11"),
    ("physics-1p-2021-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2021-01"),
    ("physics-1p-2021-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2021-06"),
    ("physics-1p-2021-11", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2021-11"),
    ("physics-1p-2022-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2022-01"),
    ("physics-1p-2022-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2022-06"),
    ("physics-1p-2023-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2023-01"),
    ("physics-1p-2023-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2023-06"),   # v3 legacy case (hand rationale kept)
    ("physics-1p-2023-11", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2023-11"),
    ("physics-1p-2024-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2024-06"),
    ("physics-1p-2024-11", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2024-11"),
    ("physics-1p-2025-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2025-06"),
    ("physics-1p-2025-11", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2025-11"),
    ("physics-1p-2026-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1p-2026-06"),
    ("physics-1pr-2019-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1pr-2019-06"),
    ("physics-1pr-2020-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1pr-2020-01"),
    ("physics-1pr-2020-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1pr-2020-06"),
    ("physics-1pr-2021-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1pr-2021-01"),
    ("physics-1pr-2022-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1pr-2022-01"),
    ("physics-1pr-2022-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1pr-2022-06"),
    ("physics-1pr-2023-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1pr-2023-01"),
    ("physics-1pr-2023-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1pr-2023-06"),
    ("physics-1pr-2024-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1pr-2024-06"),
    ("physics-1pr-2025-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1pr-2025-06"),
    ("physics-1pr-2026-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-1pr-2026-06"),
    ("physics-2p-2019-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2019-06"),
    ("physics-2p-2020-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2020-01"),
    ("physics-2p-2020-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2020-06"),
    ("physics-2p-2021-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2021-01"),
    ("physics-2p-2021-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2021-06"),
    ("physics-2p-2021-11", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2021-11"),
    ("physics-2p-2022-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2022-01"),
    ("physics-2p-2022-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2022-06"),
    ("physics-2p-2023-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2023-01"),
    ("physics-2p-2023-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2023-06"),   # v3 legacy case (hand rationale kept)
    ("physics-2p-2023-11", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2023-11"),
    ("physics-2p-2024-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2024-06"),   # v3 legacy case (hand rationale kept)
    ("physics-2p-2024-11", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2024-11"),
    ("physics-2p-2025-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2025-06"),
    ("physics-2p-2025-11", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2025-11"),
    ("physics-2p-2026-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2p-2026-06"),
    ("physics-2pr-2019-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2pr-2019-06"),
    ("physics-2pr-2020-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2pr-2020-01"),
    ("physics-2pr-2020-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2pr-2020-06"),
    ("physics-2pr-2021-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2pr-2021-01"),
    ("physics-2pr-2022-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2pr-2022-01"),
    ("physics-2pr-2022-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2pr-2022-06"),
    ("physics-2pr-2023-01", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2pr-2023-01"),
    ("physics-2pr-2023-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2pr-2023-06"),
    ("physics-2pr-2024-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2pr-2024-06"),
    ("physics-2pr-2025-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2pr-2025-06"),
    ("physics-2pr-2026-06", "igcse-physics-19", "igcse-physics-19", "official-4ph1-2pr-2026-06"),
    ("maths-01-2018-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2018-06"),
    ("maths-01-2019-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2019-01"),
    ("maths-01-2019-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2019-06"),
    ("maths-01-2020-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2020-01"),
    ("maths-01-2020-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2020-06"),
    ("maths-01-2020-11", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2020-11"),
    ("maths-01-2021-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2021-01"),
    ("maths-01-2021-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2021-06"),
    ("maths-01-2021-11", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2021-11"),
    ("maths-01-2022-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2022-01"),
    ("maths-01-2022-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2022-06"),
    ("maths-01-2023-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2023-01"),
    ("maths-01-2023-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2023-06"),
    ("maths-01-2023-11", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2023-11"),
    ("maths-01-2024-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2024-06"),
    ("maths-01-2024-11", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2024-11"),
    ("maths-01-2025-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2025-06"),
    ("maths-01-2025-10", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2025-10"),
    ("maths-01-2026-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01-2026-06"),
    ("maths-01r-2018-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2018-06"),
    ("maths-01r-2019-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2019-01"),
    ("maths-01r-2019-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2019-06"),
    ("maths-01r-2020-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2020-01"),
    ("maths-01r-2020-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2020-06"),
    ("maths-01r-2020-11", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2020-11"),
    ("maths-01r-2021-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2021-01"),
    ("maths-01r-2022-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2022-01"),
    ("maths-01r-2022-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2022-06"),
    ("maths-01r-2023-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2023-01"),
    ("maths-01r-2023-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2023-06"),
    ("maths-01r-2024-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2024-06"),
    ("maths-01r-2025-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2025-06"),
    ("maths-01r-2026-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-01r-2026-06"),
    ("maths-02-2018-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2018-06"),
    ("maths-02-2019-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2019-01"),
    ("maths-02-2019-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2019-06"),
    ("maths-02-2020-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2020-01"),
    ("maths-02-2020-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2020-06"),
    ("maths-02-2020-11", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2020-11"),
    ("maths-02-2021-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2021-01"),
    ("maths-02-2021-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2021-06"),
    ("maths-02-2021-11", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2021-11"),
    ("maths-02-2022-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2022-01"),
    ("maths-02-2022-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2022-06"),
    ("maths-02-2023-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2023-01"),
    ("maths-02-2023-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2023-06"),
    ("maths-02-2023-11", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2023-11"),
    ("maths-02-2024-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2024-06"),
    ("maths-02-2024-11", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2024-11"),
    ("maths-02-2025-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2025-06"),
    ("maths-02-2025-11", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2025-11"),
    ("maths-02-2026-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02-2026-06"),
    ("maths-02r-2018-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2018-06"),
    ("maths-02r-2019-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2019-01"),
    ("maths-02r-2019-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2019-06"),   # v3 legacy case (hand rationale kept)
    ("maths-02r-2020-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2020-01"),
    ("maths-02r-2020-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2020-06"),
    ("maths-02r-2020-11", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2020-11"),
    ("maths-02r-2021-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2021-01"),
    ("maths-02r-2022-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2022-01"),
    ("maths-02r-2022-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2022-06"),
    ("maths-02r-2023-01", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2023-01"),
    ("maths-02r-2023-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2023-06"),
    ("maths-02r-2024-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2024-06"),
    ("maths-02r-2025-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2025-06"),
    ("maths-02r-2026-06", "igcse-maths-b-16", "igcse-maths-b-16", "official-4mb1-02r-2026-06"),
]

# v3 legacy cases keep their hand-written selection records verbatim; the
# F129 full-coverage cases derive their risk classes mechanically from the
# same frozen expectations (mcq / figures / stubs / no-mcq / long-paper).
RISKS = {
    "physics-2p-2023-06": ["multipart", "mcq", "figures", "crop-required-stubs", "repaired-source-F102"],
    "physics-1p-2019-06": ["damaged-source-OCR-F101", "page-anchors", "mcq", "figures", "multipart"],
    "physics-2p-2024-06": ["figures", "graph-assets", "multipart"],
    "physics-1p-2023-06": ["figures", "heavy-crop-surface", "multipart", "marks-law-110"],
    "chemistry-1c-2023-06": ["chemistry-notation", "mark-points", "mcq", "figures"],
    "chemistry-1c-2020-01": ["mcq-adjudication-ledger", "figures", "multipart"],
    "chemistry-2c-2019-06": ["rasterized-source-legacy", "figures", "multipart"],
    "maths-02r-2019-06": ["math-typesetting", "mark-codes-M1A1", "figures", "no-mcq"],
}

RATIONALES = {
    "physics-2p-2023-06": "The F102 repair-reconversion slice (archive mislabel repaired, Task 15/22): end-to-end serving proof of the repaired bytes; carries MCQ, multipart, crops and honest crop-required stubs.",
    "physics-1p-2019-06": "The F101 OCR slice: image-only source scan recovered through the OCR source layer; page anchors must survive the serving path; the damaged-source regression class.",
    "physics-2p-2024-06": "Graph-asset class: line-graph crops must resolve and load in the served DOM.",
    "physics-1p-2023-06": "Heaviest crop surface of the 1P lane (16 crop assets) + the exact 110-mark footer law; figure-association stress case.",
    "chemistry-1c-2023-06": "The chemistry corpus-of-record slice: ce{} chemistry notation through KaTeX-mhchem, multi-point mark schemes, keyed MCQ.",
    "chemistry-1c-2020-01": "The MCQ adjudication-ledger class (MCQ-KEYS.json history): keys must stay attested, never auto-derived, in the served player.",
    "chemistry-2c-2019-06": "The rasterized-archive legacy slice (2019-06 G1/G5 REVIEW history, later closed): serving-state proof for the oldest chemistry paper.",
    "maths-02r-2019-06": "The maths typesetting class: LaTeX fractions/working through remark-math + KaTeX, M1/A1 mark codes through the MarkScheme component, zero MCQ.",
}


def norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


def slugify(s):
    return re.sub(r"^-+|-+$", "", re.sub(r"[^a-z0-9]+", "-", (s or "").lower().strip()))


def md_first_prose(md, minlen=14, maxlen=110):
    """F120: the first rendered prose of a part's problemMd — the exact words
    the printed label sits in front of on the SAME rendered line. None when
    the head of the md is not plain prose (TeX/markdown/table/option-line/
    figure-first heads, or an md that carries its own parenthesized label —
    any of which would make the label-adjacency assertion ambiguous)."""
    s = norm(md or "")
    if not s:
        return None
    s = re.sub(r"^(?:\*{1,2}|#{1,6}|_)+\s*", "", s).strip()
    if not s or s.startswith(("![", "[!", "<", "|")):
        return None
    if re.match(r"^\([a-z0-9]{1,5}\)", s):  # md carries its own printed label
        return None
    if re.match(r"^[A-Fa-f][).]\s", s):  # option-line head (MCQ inline options)
        return None
    sent = re.split(r"(?<=[.?!])\s+", s)[0].strip()
    if not (minlen <= len(sent) <= maxlen):
        return None
    if re.search(r"[$<>|_\\*]|https?:", sent):
        return None
    return sent


def pick_label_samples(parts, want_labelled=3):
    """F120: the frozen part_labels sample — deterministic, risk-class-driven:
    one roman-nested label (the (a)(i) class the original defect mislabelled),
    one labelled MCQ part, one further labelled part, plus up to ONE null
    (path-less) part — the fail-closed class whose rendered surface must show
    NO invented chip. Every sample needs a plain-prose first text (md_first_prose)."""
    roman = mcq = single = null = None
    for p in parts:
        pid = p.get("id") or ""
        lab = bundle_label_of(p)
        label, state = label_from_offp_id(pid)
        ts = md_first_prose(p.get("problemMd"))
        if lab is None or state == "pathless":
            if null is None and ts and state == "pathless" and lab is None:
                null = {"part_id": pid, "label": None, "text_start": ts, "kind": "null"}
            continue
        if ts is None or not LABEL_GRAMMAR_RE.match(lab):
            continue
        if label is not None and label != lab:
            continue  # G-E6 drift at derivation time — not a valid sample
        rec = {"part_id": pid, "label": lab, "text_start": ts, "kind": "labelled"}
        segs = (label_from_offp_id(pid)[0] or "").count("(") if label else 0
        if roman is None and segs >= 2:
            roman = rec
        elif mcq is None and p.get("questionType") == "multiple_choice":
            mcq = rec
        elif single is None:
            single = rec
        if all(x is not None for x in (roman, mcq, single, null)):
            break
    return [x for x in (roman, mcq, single, null) if x]


def pick_facts(parts, want=3, minlen=40, maxlen=110):
    """Pick stable plain-prose snippets from problemMd (no md/TeX syntax)."""
    out, seen = [], set()
    for p in parts:
        md = p.get("problemMd") or ""
        for sentence in re.split(r"(?<=[.?!])\s+", norm(md)):
            cand = sentence.strip()
            if not (minlen <= len(cand) <= maxlen):
                continue
            if re.search(r"[$<>|_*\\]|https?:", cand):
                continue
            if cand in seen:
                continue
            seen.add(cand)
            out.append({"part_id": p["id"], "snippet": cand})
            break
        if len(out) >= want:
            break
    return out


# FIX-4 (F129): mark-scheme debris signature. maths-B solutionMds (and some
# physics mark-scheme rows) are squashed MS table rows, not prose: mark codes
# (M1/A1/B1/...), MS verdict verbs (Allow / Do not / Condone / Ignore / Alt),
# the squashed-row separator ";;;", or the "oe/cao/isw/awrt/soi/ft" family.
# A line matching this pattern is never frozen as an expected fact — the
# surface renders those rows through the structured MarkScheme component and
# can never reproduce the squashed form verbatim.
MS_DEBRIS_RE = re.compile(
    r"\bM1\b|\bA1\b|\bB1\b|\bB2\b|\bB3\b|\bC1\b|\bcao\b|\boe\b|\bisw\b"
    r"|\bawrt\b|\bsoi\b|\bft\b|\bAlt\b|;;;|\bAllow\b|\bDo not\b"
    r"|\bCondone\b|\bIgnore\b|\bmark for each\b")


def pick_solution_facts(parts, want=2, minlen=24, maxlen=120):
    out = []
    for p in parts:
        md = p.get("solutionMd") or ""
        for line in md.split("\n"):
            cand = norm(line)
            if not (minlen <= len(cand) <= maxlen):
                continue
            if re.search(r"[$<>|_\\*]|https?:", cand):
                continue
            if re.match(r"^\s*[-*•]\s", cand):  # FIX-4: list-item head —
                continue                           # rendered form drops the marker
            if MS_DEBRIS_RE.search(cand):          # FIX-4: MS table debris
                continue
            out.append({"part_id": p["id"], "snippet": cand})
            break
        if len(out) >= want:
            break
    return out


def first_keyed_mcq(parts):
    for p in parts:
        if p.get("questionType") != "multiple_choice":
            continue
        ch = p.get("choices") or []
        correct = [c for c in ch if c.get("isCorrect")]
        wrong = [c for c in ch if not c.get("isCorrect") and c.get("textMd", "").strip()]
        if len(correct) == 1 and wrong and norm(correct[0].get("textMd")):
            c0 = correct[0]
            return {
                "part_id": p["id"],
                "correct_label": c0["label"],
                "correct_text_snippet": norm(c0["textMd"])[:60],
                "distractor_label": wrong[0]["label"],
            }
    return None


def crop_img_occurrences(parts):
    """Crop images actually inlined into problemMd (each occurrence renders an <img>)."""
    n = 0
    missing_inline = []
    for p in parts:
        md = p.get("problemMd") or ""
        for a in p.get("assets") or []:
            if a.get("kind") == "crop" and a.get("path"):
                if a.get("rawUrl") and a["rawUrl"] in md:
                    n += 1
                elif a.get("path") in md or f"assets/{a['path'].split('/')[-1]}" in md:
                    n += 1
                else:
                    missing_inline.append({"part_id": p["id"], "path": a["path"]})
    return n, missing_inline


def content_imgs_inlined(parts):
    """F129 census: ALL asset occurrences actually inlined into problemMd
    (any asset kind) — the exact number of content <img> elements the
    rendered page must show before any interaction."""
    n = 0
    for p in parts:
        md = p.get("problemMd") or ""
        for a in p.get("assets") or []:
            url = a.get("rawUrl") or ""
            path = a.get("path") or ""
            if url and url in md:
                n += 1
            elif path and (path in md or f"assets/{path.split('/')[-1]}" in md):
                n += 1
    return n


def mechanical_risks(case_id, e):
    risks = ["full-coverage-F129"]
    if e["mcq_parts"]:
        risks.append("mcq")
    else:
        risks.append("no-mcq")
    if e["crop_assets"]:
        risks.append("figures")
    if e["crop_required_stubs"]:
        risks.append("crop-required-stubs")
    if e["parts"] > 45:
        risks.append("long-paper")
    if e["mark_points"]:
        risks.append("mark-points")
    return risks


def mechanical_rationale(case_id, lane_course, e):
    return ("Full-coverage class (F129 all-papers re-derivation): every official paper of "
            f"the {lane_course} lane is a frozen case, derived from the bundles of record "
            f"with the 0.7 validator (q={e['questions']}, parts={e['parts']}, "
            f"marks={e['marks_total']}).")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundles-dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    bundles = {}
    for _course in ("igcse-chemistry-19", "igcse-physics-19", "igcse-maths-b-16"):
        bundles[_course] = json.load(open(f"{args.bundles_dir}/{_course}/official-papers.json"))

    cases = []
    for case_id, lane, course, slug_suffix in CASE_DEFS:
        topics = [t for t in bundles[course] if (t.get("slug") or "").endswith(slug_suffix)]
        if len(topics) != 1:
            sys.exit(f"casegen: expected exactly 1 topic for {slug_suffix}, got {len(topics)}")
        t = topics[0]
        qs = t["questions"]
        parts = [p for q in qs for p in q["parts"]]
        marks = sum(q["totalMarks"] for q in qs)
        mcq_parts = [p for p in parts if p.get("questionType") == "multiple_choice"]
        keyed = [p for p in mcq_parts if p.get("choices") and sum(1 for c in p["choices"] if c.get("isCorrect")) == 1]
        crops = [a for p in parts for a in (p.get("assets") or []) if a.get("kind") == "crop"]
        stubs = [a for p in parts for a in (p.get("assets") or []) if a.get("kind") == "crop-required"]
        imgs_expected, missing_inline = crop_img_occurrences(parts)
        src = next((p.get("sourcePaper") or {} for p in parts if p.get("sourcePaper")), {})
        date, number = src.get("date") or "", src.get("number") or ""
        paper_key = f"{slugify(date)}-{slugify(number)}"
        mcq = first_keyed_mcq(keyed) if keyed else None
        e = {
            "questions": len(qs),
            "parts": len(parts),
            "marks_total": marks,
            "mcq_parts": len(mcq_parts),
            "mcq_keyed": len(keyed),
            "crop_assets": len(crops),
            "crop_required_stubs": len(stubs),
            "mark_points": sum(len(p.get("markPoints") or []) for p in parts),
            "crop_imgs_inlined": imgs_expected,
            "solutions": sum(1 for p in parts if (p.get("solutionMd") or "").strip()),
            # F120: the labelled-parts census of the case (parts whose
            # served sourcePaper.questionPart is non-null) — enforced at
            # the static-bundles leg AND as the rendered chip census.
            "labelled_parts": sum(1 for p in parts if bundle_label_of(p)),
            # F129 (v4): the 0.7 census expectations.
            "question_ids": [q["id"] for q in qs],
            "content_imgs_inlined": content_imgs_inlined(parts),
            "mcq_options_total": sum(len(p.get("choices") or []) for p in mcq_parts),
        }
        case = {
            "id": case_id,
            "lane": lane,
            "course": course,
            "topic_slug": t["slug"],
            "topic_id": t["topicId"],
            "paper": {"date": date, "number": number},
            "paper_key": paper_key,
            "url_path": f"/courses/{course}/past-papers/{paper_key}",
            "selection": {
                "rationale": RATIONALES.get(case_id) or mechanical_rationale(case_id, course, e),
                "risk_classes": RISKS.get(case_id) or mechanical_risks(case_id, e),
            },
            "expected": e,
            "fact_parts": pick_facts(parts),
            "solution_facts": pick_solution_facts(parts),
            "mcq_interaction": mcq,
            "part_labels": pick_label_samples(parts),
        }
        if missing_inline:
            case["expected"]["crop_inline_gaps"] = missing_inline
        cases.append(case)

    out = {
        "benchmark_schema": "syllabai.g9-benchmark-cases/0.1",
        "benchmark_version": BENCHMARK_VERSION,
        "validator_version": VALIDATOR_VERSION,
        "note": "Frozen rendered-question benchmark contract. Expected facts derived from the "
                "syllabai-v2 hub official bundles of record (H3-cutover exports of the "
                "resources corpus of record). Re-derive only via official_examq_g9_casegen.py "
                "with a benchmark_version BUMP + LEDGER entry (anti-gaming rule). v4 (F129): "
                "the all-papers contract — every official paper of the three ADR-037 lanes "
                "is a frozen case, with the 0.7 census expectations.",
        "cases": cases,
    }
    json.dump(out, open(args.out, "w"), indent=1, ensure_ascii=False)
    print(f"wrote {args.out}: {len(cases)} cases")
    for c in cases[:3]:
        e = c["expected"]
        print(f"  {c['id']}: q={e['questions']} parts={e['parts']} marks={e['marks_total']} "
              f"mcq={e['mcq_parts']}/{e['mcq_keyed']} crops={e['crop_assets']} "
              f"imgs_inline={e['crop_imgs_inlined']} facts={len(c['fact_parts'])} "
              f"solfacts={len(c['solution_facts'])} labels={e['labelled_parts']}/{e['parts']} "
              f"url={c['url_path']}")


if __name__ == "__main__":
    main()
