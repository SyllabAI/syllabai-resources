# curated/

Hand-curated fixtures for the GradeBoundaries lane.

- `maths-genie-4ch1-golden.json` — the golden-master parity fixture: 8 sessions
  of 4CH1 overall boundaries as published by mathsgenie.co.uk's predicted-grade
  calculator (retrieved 2026-10-31, zai-web trace 1a191d55e2154601). Used by
  `scripts/validate.py` (G2): the parsed Pearson corpus must equal it exactly
  on every overlapping session. This is evidence, not a serving source — the
  bundle serves only sha256-proven official PDFs.

No hand-curated serving data exists yet (the hybrid doctrine: curated fallbacks
would land here with `reviewRequired: true` if an official source ever becomes
unreachable).
