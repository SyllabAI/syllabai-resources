#!/usr/bin/env python3
"""T-C33 K2-C-1 — batch-B01 quote probe (fail-closed; the c11_batch11_quote_probe.py
convention adapted to the maths-a substrate).

Walks scripts/c33_maths_a_batch01_decisions.yaml and verifies EVERY evidence
quote (node attachments + edges) matches its cited file under the batch-8
G03/c11.4 normalization convention (NFC, markdown link-unwrap, HTML tag strip,
emphasis strip, dash/quote translation, whitespace collapse).

The maths-a corpora are git-only in this workspace (C28-F1 sparse-checkout
mechanism), so reads go disk-first with a single persistent
`git cat-file --batch` process as fallback and the channel is recorded.

Negative control re-asserted here (independent of the preverify): every NOTE
citation is one of the 4 join-carried notes; every MARK_SCHEME citation lives
under the slice course's EQ tree; every SPEC citation is the ratified store.
The 1.1G SPEC quote carries the official wording's typographic-quote damage
verbatim ('’prime numbers’') — damage preserved, never fixed, per the K1
statement_text_policy.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
COURSE = "igcse-maths-a-18-higher"
DECISIONS = HERE / "c33_maths_a_batch01_decisions.yaml"
JOIN_ARTIFACT = (REPO / "Official-Specifications/parsed/_derived/notes-join/"
                 f"{COURSE}.json")
NOTE_FILES = {
    f"SME-RevisionNotes/{COURSE}/notes/1-numbers-and-the-number-system/"
    "number-toolkit/order-of-operations-bidmas-bodmas.md",
    f"SME-RevisionNotes/{COURSE}/notes/1-numbers-and-the-number-system/"
    "prime-factors-hcf-and-lcm/types-of-number.md",
    f"SME-RevisionNotes/{COURSE}/notes/2-equations-formulae-and-identities/"
    "algebraic-fractions/algebraic-fractions.md",
    f"SME-RevisionNotes/{COURSE}/notes/1-numbers-and-the-number-system/"
    "fractions/mixed-numbers-and-improper-fractions.md",
}
SPEC_FILE = "graph/igcse-maths-a/specification_points.yaml"

_TRANS = {ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


class R:
    """disk-first reader with a single persistent cat-file --batch fallback."""

    def __init__(self) -> None:
        self._proc = None
        self._cache: dict[str, str] = {}
        self.methods = {"disk": 0, "git-batch": 0}

    def _show(self, rel: str) -> str:
        if self._proc is None:
            self._proc = subprocess.Popen(
                ["git", "-C", str(REPO), "cat-file", "--batch"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self._proc.stdin.write(f"HEAD:{rel}\n".encode())
        self._proc.stdin.flush()
        header = self._proc.stdout.readline().decode()
        parts = header.split()
        if len(parts) < 3 or parts[1] == "missing":
            raise FileNotFoundError(rel)
        size = int(parts[2])
        body = self._proc.stdout.read(size)
        self._proc.stdout.read(1)
        return body.decode("utf-8")

    def read(self, rel: str) -> str:
        if rel in self._cache:
            return self._cache[rel]
        p = REPO / rel
        if p.is_file():
            self.methods["disk"] += 1
            text = p.read_text(encoding="utf-8")
        else:
            self.methods["git-batch"] += 1
            text = self._show(rel)
        self._cache[rel] = text
        return text

    def close(self) -> None:
        if self._proc is not None:
            try:
                self._proc.stdin.close()
                self._proc.kill()
            except Exception:
                pass


def main() -> int:
    doc = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
    r = R()
    checks = 0
    fails: list[str] = []
    kinds: dict[str, int] = {"NOTE": 0, "SPEC": 0, "MARK_SCHEME": 0}

    def probe(ev: dict, where: str) -> None:
        nonlocal checks
        checks += 1
        kind, f, quote = ev["kind"], ev["file"], ev["quote"]
        kinds[kind] = kinds.get(kind, 0) + 1
        if kind == "NOTE" and f not in NOTE_FILES:
            fails.append(f"{where}: NOTE file outside the join-carried set: {f}")
        if kind == "SPEC" and f != SPEC_FILE:
            fails.append(f"{where}: SPEC file is not the ratified store: {f}")
        if kind == "MARK_SCHEME" and not f.startswith(
                f"SME-ExamQuestion/{COURSE}/"):
            fails.append(f"{where}: MS file outside the slice course: {f}")
        try:
            hay = norm(r.read(f))
        except FileNotFoundError:
            fails.append(f"{where}: missing file {f}")
            return
        if norm(quote) not in hay:
            fails.append(f"{where}: quote not verbatim in {f}: {quote[:70]!r}")

    for nd in doc["nodes"]:
        for sp in nd.get("spec_points") or []:
            for ev in sp["evidence"]:
                probe(ev, f"{nd['code']} ({sp['code']})")
    for e in doc["edges"]:
        for ev in e["evidence"]:
            probe(ev, f"{e['source']} -> {e['target']} ({e['relation']})")

    # NOTE citations must hit the joined note for the attached SP (row-level)
    join = json.loads(JOIN_ARTIFACT.read_text(encoding="utf-8"))
    store = yaml.safe_load((REPO / SPEC_FILE).read_text(encoding="utf-8"))
    code_by_official = {r_["official_code"]: r_["code"]
                        for r_ in store["specification_points"]}
    pair_ok = True
    for j in join["joins"]:
        pass
    join_pairs = {(f"SME-RevisionNotes/{COURSE}/"
                   + j["note_path"][:-len(".json")] + ".md",
                   code_by_official.get(j["resolved_code"],
                                        j["resolved_code"]))
                  for j in join["joins"]}
    for nd in doc["nodes"]:
        for sp in nd.get("spec_points") or []:
            for ev in sp["evidence"]:
                if ev["kind"] == "NOTE" and (ev["file"], sp["code"]) \
                        not in join_pairs:
                    pair_ok = False
                    fails.append(f"{nd['code']} ({sp['code']}): NOTE row not "
                                 f"backed by the join pair")
    r.close()

    print(f"quote probe: {checks} evidence anchors checked "
          f"(kinds: {kinds}; read channels: {r.methods})")
    if pair_ok and not fails:
        print("c33_maths_a_batch01_quote_probe: ALL PASS — every quote "
              "verbatim under the batch-8 anchor convention; every NOTE row "
              "backed by its join pair; the unjoined-corpus negative control "
              "carries no anchor")
        return 0
    print(f"FAILED: {len(fails)}")
    for f in fails:
        print("  -", f)
    return 1


if __name__ == "__main__":
    sys.exit(main())
