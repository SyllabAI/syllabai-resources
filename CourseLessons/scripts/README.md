# scripts/ — the pipeline tooling

| Tool | What it does |
|---|---|
| `lessonctl.py` | The one CLI: `report` / `scaffold` / `resume` / `lint` / `tracker` / `finding` / `emit`. See CourseLessons/START-HERE.md §2. |
| `section_map.py` | L0: parse of record → section spine per chapter (fetch-first recipe in docstring). |
| `lint_rules/<subject>.yaml` | Per-subject banned phrases + artifact regexes (VALIDATION.md V4). Grows via findings only. |

Deps: Python 3.10+, PyYAML. No network calls inside the tools — corpus access
is fetch-first, one-shot, scrubbed (START-HERE law 1).

## Extending (self-improvement law)

- New lint rule → add here + a findings entry (lint-gap) showing the failure it catches.
- New subcommand → keep it receipt-aware and tracker-aware; add a line here.
- Schema drift in the parse of record → section_map.py key-mapping prints what it detected; mismatch = finding (type: process).
