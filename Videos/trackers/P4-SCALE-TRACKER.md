# P4 — Scale tracker (T-VIDEOMAP-P4)

| step | status | artifact / gate |
| --- | --- | --- |
| 106-course decision matrix | ✅ done | `work/p4/matrix.json` (analysis) — classes: mapped 10 · inherit 35 · shelf-direct 4 · mechanics 4 · honest-empty 53 |
| inheritance map (committed) | ✅ done | `Videos/drafts/_p4/inheritance-map.json` + `Videos/scripts/build-p4-inheritance.py` (containment ≥0.55, ≥3 informative tokens) |
| shelf-direct drafts ×4 | ✅ done — reviewed | `drafts/<4 maths courses>/video-map.draft.external.json` + verdicts; 259 rows; oEmbed 128/128 |
| mechanics drafts ×4 | ✅ done — reviewed | `drafts/<4 mechanics courses>/video-map.draft.external.json` + verdicts; 214 rows; crossSubject disclosed |
| delegated self-review | ✅ applied | 15 spec-level rejects + 8 full-row drops applied; `drafts/review-file-external-p4.md` |
| inheritance derivation spot-check | ✅ passed (after fix) | degenerate short-title matches eliminated by token guard; `_p4/owner-review-verdicts.p4-inherit.json` |
| builder P4 extension | ✅ done — exit 0 | `Videos/scripts/build-content-map-external.mjs`: P4_FRESH fresh path + 35-course derive-from-emitted-parent section; zero unreviewed rows; spec/video/spine integrity re-verified per file |
| hub emit | ✅ done | registry **53 courses** · rows 2827 · flags `videoMap.courses` = 53 · status `live (T-VIDEOMAP-P3+P4)` |
| honest-empty record | ✅ recorded | 53 courses with reason; `docs/P4-SCALE-REPORT.md` §2d |
