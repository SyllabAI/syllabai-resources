# T-C12 decision records

Decision files produced by `c12_spec_tagger.py verify` land here, named
`<scope>.<extraction_pass>.yaml`, each with its raw model trace
(`<...>.raw-trace.json`) as durable evidence (AGENT.md rule 6). Everything
in this directory is AI_SUGGESTED output: it is NOT authoritative corpus
data, and promotion to HUMAN_VALIDATED happens only through the operator
review gate downstream (C11_ARCHITECTURE.md §7).

- `smoke-demo.agent-pass-1.yaml` + `.raw-trace.json` — DEMO pass over
  `scripts/c12_fixtures/smoke_questions.json` (2026-09-14, extraction pass
  c12-agent-pass-1, model "GLM (Super Z agent, z.ai)" via the sandbox SDK;
  replayed through `verify --from-raw`, zero user keys). Findings preserved
  on purpose: the model abstained on the out-of-curriculum WPH11 physics
  question, proposed a non-registry command word ("Understand") on the
  acid-rain unit (demoted to REVIEW_REQUIRED with the documented violation),
  picked registry-valid but questionable 1.56C on ionic conduction, and took
  the bait on the 4CH1-4.15-style premise+consequence negative control —
  exactly the failure mode the operator review queue exists to catch.
  `check` passes on this file; CI re-checks it as a positive control.
