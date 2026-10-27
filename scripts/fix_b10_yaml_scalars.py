#!/usr/bin/env python3
"""One-shot YAML scalar fixer for c11_batch10_decisions.yaml: wraps any
plain single-line scalar value that contains ': ' (a second colon sequence
after the key separator) in single quotes, so the fail-closed probes can
parse the record. Idempotent: already-quoted or block-scalar lines are
skipped."""
import re
from pathlib import Path

P = Path(__file__).resolve().parent / "c11_batch10_decisions.yaml"
line_re = re.compile(r'^(\s*)([A-Za-z_][A-Za-z0-9_]*): (.*\S)\s*$')
changed = 0
out = []
for ln in P.read_text(encoding="utf-8").split("\n"):
    m = line_re.match(ln)
    if m and ": " in m.group(3) and not m.group(3).startswith(("'", '"', "|",
                                                              ">", "[")):
        val = m.group(3)
        if val.endswith(":") or ": " in val:
            val_q = "'" + val.replace("'", "''") + "'"
            out.append(f"{m.group(1)}{m.group(2)}: {val_q}")
            changed += 1
            continue
    out.append(ln)
P.write_text("\n".join(out), encoding="utf-8")
print(f"wrapped {changed} scalar values")
