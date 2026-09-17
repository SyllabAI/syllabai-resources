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
