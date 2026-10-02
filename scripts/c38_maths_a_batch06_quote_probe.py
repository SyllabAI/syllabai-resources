#!/usr/bin/env python3
"""T-C38 K2-C-6 — batch-B06 quote probe (fail-closed; the c37_maths_a_batch05_
quote_probe.py convention, sixth-batch instance with the pair-back at B02
strength).

Walks scripts/c38_maths_a_batch06_decisions.yaml and verifies EVERY evidence
quote (node attachments + node-level MIS evidence + edges) matches its cited
file under the batch-8 G03/c11.4 normalization convention (NFC, markdown
link-unwrap, HTML tag strip, emphasis strip, dash/quote translation, whitespace
collapse).

The maths-a corpora are git-only in this workspace (C28-F1 sparse-checkout
mechanism), so reads go disk-first with a single persistent
`git cat-file --batch` process as fallback and the channel is recorded.

Negative control re-asserted here (independent of the preverify): every NOTE
citation is one of the 14 join-carried notes and is pair-backed — node
attachments against their attached SP, edge evidence against one of the edge's
endpoint SPs; every MARK_SCHEME citation lives under the slice course's EQ
tree; every SPEC citation is the ratified store. All NOTE/MS quotes are checked
byte-exactly under the convention; nothing is silently normalized into
matching.
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
QUAL = "igcse-maths-a"
COURSE = "igcse-maths-a-18-higher"
DECISIONS = HERE / "c38_maths_a_batch06_decisions.yaml"
JOIN_ARTIFACT = (REPO / "Official-Specifications/parsed/_derived/notes-join/"
                 f"{COURSE}.json")
SPEC_FILE = f"graph/{QUAL}/specification_points.yaml"

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
        for ev in nd.get("evidence") or []:
            probe(ev, f"{nd['code']} (node-level MIS evidence)")
    for e in doc["edges"]:
        for ev in e["evidence"]:
            probe(ev, f"{e['source']} -> {e['target']} ({e['relation']})")

    # NOTE pair-back: node attachments against the attached SP; edge evidence
    # against one of the edge's endpoint SPs (the B02 strength, carried forward)
    join = json.loads(JOIN_ARTIFACT.read_text(encoding="utf-8"))
    store = yaml.safe_load((REPO / SPEC_FILE).read_text(encoding="utf-8"))
    code_by_official = {r_["official_code"]: r_["code"]
                        for r_ in store["specification_points"]}
    join_by_note: dict[str, set[str]] = {}
    for j in join["joins"]:
        md = f"SME-RevisionNotes/{COURSE}/" + j["note_path"][:-len(".json")] \
            + ".md"
        rc = code_by_official.get(j["resolved_code"], j["resolved_code"])
        join_by_note.setdefault(md, set()).add(rc)
    for nd in doc["nodes"]:
        for sp in nd.get("spec_points") or []:
            for ev in sp["evidence"]:
                if ev["kind"] == "NOTE" and sp["code"] not in \
                        join_by_note.get(ev["file"], set()):
                    fails.append(f"{nd['code']} ({sp['code']}): NOTE row not "
                                 f"backed by the join pair")
    for e in doc["edges"]:
        endpts = {e["source"], e["target"]}
        endpt_sps = {sp["code"] for x in doc["nodes"] if x["code"] in endpts
                     for sp in (x.get("spec_points") or [])}
        for ev in e["evidence"]:
            if ev["kind"] == "NOTE" and not (
                    join_by_note.get(ev["file"], set()) & endpt_sps):
                fails.append(f"{e['source']} -> {e['target']}: edge NOTE "
                             f"evidence not joined to any endpoint SP")
    r.close()

    print(f"quote probe: {checks} evidence anchors checked "
          f"(kinds: {kinds}; read channels: {r.methods})")
    if not fails:
        print("c38_maths_a_batch06_quote_probe: ALL PASS — every quote "
              "verbatim under the batch-8 anchor convention; every NOTE row "
              "pair-backed (nodes at their SP, edges at an endpoint SP); the "
              "unjoined-corpus negative control carries no anchor")
        return 0
    print(f"FAILED: {len(fails)}")
    for f in fails:
        print("  -", f)
    return 1


if __name__ == "__main__":
    sys.exit(main())
