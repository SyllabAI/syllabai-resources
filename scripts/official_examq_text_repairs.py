#!/usr/bin/env python3
"""T-OEQ-MATHSB-SERVE-1 hygiene wave (run-001): source-layer text repairs.

Law of record (ADR-039 §3.4 family — the F52/F64 precedent class): the staged
pdftotext extraction layers of five maths-B QPs, one maths-B MS (2019-06/02,
the OCR-sandwich paper) and the 2025-06/01R QP carry broken-symbol-font
artifacts that the extraction of record cannot serve: C0/C1 glyph-slot
mis-maps (SymbolMT subsets whose glyph codes land in the control ranges),
a uniform -29 ASCII shift class (broken TimesNewRoman subsets: space->0x03,
'.'->0x11, digits->0x13..0x1c, lowercase->uppercase-29), U+FFFD
unresolvable-OCR glyphs (fraction bars, radicals, matrix parens), RTL/bidi
wrapper marks, and Cyrillic/Thaana/Latin-1 oddball slots.

Every repair is a per-line rule adjudicated eyes-on against 150/300/600dpi
page renders of the printed paper (evidence pack: wave receipts,
evidence-r2/) and — for the 2019-06/02 MS — cross-checked against the SME
twin's UIUX-TIER-B-RUN-004 repair lineage (58 eyes-on line rules). The table
carries a sha1 guard per rule: at apply time the raw line MUST hash-match
its recorded raw bytes or the run aborts (fail-closed; the staged layer is
not silently re-interpreted).

Application point: the txt read inside official_examq_extract.main(), before
clean_lines()/parse — i.e. the repaired text IS the extraction of record, so
G2-D 5-gram provenance, source_norm and the emission move together. Lane-
scoped to igcse-maths-b-16 by the caller; chemistry/physics runs never see a
rule (their staging names carry no table entries) and the U+FFFC strip is a
measured no-op on their layers (census of record: 11 instances, all maths-B).

G4 (U+FFFC): OBJECT-REPLACEMENT-CHARACTER placeholders are anchored embedded-
object boxes with zero printed content — stripped unconditionally, corpus-
wide, logged here in the run receipt.
"""
import hashlib
import json
from pathlib import Path

_TABLE_PATH = Path(__file__).resolve().parent / "official_examq_text_repairs.json"
_TABLE = None


def _table():
    global _TABLE
    if _TABLE is None:
        _TABLE = json.loads(_TABLE_PATH.read_text(encoding="utf-8"))
    return _TABLE


def table_sha256():
    return hashlib.sha256(_TABLE_PATH.read_bytes()).hexdigest()


def repair_source_text(text: str, path, lane: str):
    """Return (repaired_text, receipt_dict). Fail-closed on guard mismatch.

    receipt_dict: {"applied": n, "fffc_stripped": n, "table_sha256": ...,
                   "rules": [{file, line, sha1_12}]} — empty for untouched
    layers so clean runs disclose nothing (byte-identical reports).
    """
    raw = text
    rules = []
    applied = 0
    lines = None
    # v0.23.0 (F98): lane-gate generalized to FILE-scoped application. The
    # v0.22.0 gate (`lane == "igcse-maths-b-16"`) hard-coded the hygiene wave's
    # lane; the Task 19 deep-audit wave adds chemistry rules for the 2026-06 2C
    # drawing-linearization tranche, and the rule keys ARE exact staged file
    # names — a lane can never see another lane's rules. The gate now simply
    # checks whether the staged file has rules; behavior for maths-B files is
    # byte-identical to v0.22.0 by construction.
    fname = Path(path).name
    file_rules = _table()["rules_by_file"].get(fname) or {}
    if file_rules:
        lines = raw.splitlines()
        # ordinals are 1-based over splitlines() of the exact staged file
        for ord_str, rule in sorted(file_rules.items(), key=lambda kv: int(kv[0])):
            ordinal = int(ord_str)
            if ordinal < 1 or ordinal > len(lines):
                raise SystemExit(
                    f"text-repairs FAIL-CLOSED: {fname}:{ordinal} out of range "
                    f"(file has {len(lines)} lines) — staged layer drifted?")
            cur = lines[ordinal - 1]
            digest = hashlib.sha1(cur.encode("utf-8")).hexdigest()[:12]
            if digest != rule["sha1_12"]:
                raise SystemExit(
                    f"text-repairs FAIL-CLOSED: {fname}:{ordinal} sha1 guard "
                    f"mismatch (table {rule['sha1_12']} != staged {digest}) — "
                    "the staged extraction layer is not the layer of record "
                    "the evidence pack adjudicated. Re-stage or re-adjudicate.")
            lines[ordinal - 1] = "" if rule["repaired"] is None else rule["repaired"]
            applied += 1
            rules.append({"line": ordinal, "sha1_12": rule["sha1_12"]})
        raw = "\n".join(lines)
    # G4: U+FFFC object placeholders never carry printed content
    fffc = raw.count("\ufffc")
    if fffc:
        raw = raw.replace("\ufffc", "")
    receipt = {"applied": applied, "fffc_stripped": fffc,
               "table_sha256": table_sha256(), "rules": rules}
    return raw, receipt
