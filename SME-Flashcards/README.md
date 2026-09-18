# SME Flashcards corpus (Edexcel)

Scraped from Save My Exams flashcards decks via `scripts/sme_flashcards_scrape.py` (registry-driven; see that file for the course registry incl. courses with no SME decks).

- Layout: `{course}/{section}/{deck}/deck.json` (schema `syllabai.sme-flashcard-deck/1.0`) + `cards.md` + `assets/`
- Card types kept first-class: keyword_definition, question_and_answer, true_or_false, fill_in_the_blanks
- front/back typed TipTap blocks (+ md render); bold/italic/underline/sub/sup preserved
- Math: Wiris MathML -> KaTeX latex (raw mathml + alt retained)
- fill_in_the_blanks: blanks counted, answers extracted; blank_answer_mismatch flagged (never guessed)
- `spec_links`: SME spcpt_* anchors as printed (join to spec_point_index harvest happens at mapping stage)
- Operator authorization: LICENSE-DATA.md (SME attestation)

Global manifest: `manifest.json` (registry + per-course totals).

## Content-join coverage note (T-SPEC-1, 2026-09-18)

`igcse-chemistry-19` (linear) cards carry no SME `spec_links`, and the
containment join added to `map_flashcards.py` (token containment >= 0.90 +
deck/official section agreement + runner-up ambiguity guard; tier stays
T3_section_anchored) correctly fires on 0 of 909 cards: their answers are
SME-authored pedagogical facts (Q&A / keyword answers), not transcriptions of
official statements. Observed best containment ~0.4, and relaxing thresholds
already mis-targets (e.g. a "freezing" interconversion answer's best
section-agreeing candidate was the ionic-conduction statement 1.43) — so they
stay honestly unmapped until SME publishes anchors for this course.
Modular/SDA chemistry decks remain fully SME-anchor-inherited
(334/222/479 joins; reproduced unchanged by the updated script).
