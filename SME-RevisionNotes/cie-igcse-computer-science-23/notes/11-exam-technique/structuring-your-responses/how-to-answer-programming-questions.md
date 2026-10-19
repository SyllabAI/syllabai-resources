---
note_id: "rn_zkVQ7zXzM6x8j8Q4"
title: "How to Answer Programming Questions"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/11-exam-technique/structuring-your-responses/how-to-answer-programming-questions
path: 11-exam-technique/structuring-your-responses/how-to-answer-programming-questions
updated_at: "2025-08-01T15:03:34.040Z"
spec_point_ids: ["spcpt_ZQP6RTpbGm4qzMFD"]
spec_point_codes: []
guided_study: false
---

# How to Answer Programming Questions

## How do I answer an OCR GCSE (9-1) Computer Science programming question?

> **Spec point** — `spcpt_ZQP6RTpbGm4qzMFD`

## How do I answer a CIE IGCSE Computer Science programming question?

- Programming questions can appear in** both papers**
- **Paper 1** may include questions that test understanding and interpretation of **algorithms** and **computational thinking principles**, including the ability to **trace and explain pseudocode**
- **Paper 2** is the paper that primarily assesses the ability to **design, write, test**, and **refine programs**

  - It also includes a **fixed 15‑mark programming question** at the end of the paper
- **All questions** must be answered using:

  - CIE **pseudocode **notation
  - **Structured English**
  - **High‑level** programming language
- To attempt a programming question that requires the writing of a new program,  you should always ask yourself the following** five key questions**:

  - What are the ***inputs***?
  - What are the ***outputs***?
  - What ***processes***** **take place?
  - What ***constructs ***will I need to use?
  - Do I need to use ***subprograms***?

#### Example

| Question |
|---|
| The string operation `SUBSTRING(Quote, Start, Number)` returns a string from `Quote`<br><br>beginning at position `Start` that is `Number` characters long. The first character in `Quote` is in position 1.<br><br>**Write **pseudocode statements to:<br><br>- store the string "`Learning Never Exhausts The Mind`" in `Quote`<br>- extract and display the words "`The Mind`" from the string<br>- output the original string in lower case.<br><br>**[5 marks]** |
| What are the **inputs**? What are the **outputs**? What **processes **take place? |
| The string operation *SUBSTRING(Quote, Start, Number) returns a string from Quote*<br><br>beginning at position `Start` that is `Number` characters long. The first character in `Quote` is in position 1.<br><br>- *store the string* "`Learning Never Exhausts The Mind`" in `Quote`<br>- *extract* and *display the words* "`The Mind`" from the string<br>- *output the original string* in *lower case*. |
| What **constructs **will I need to use? |
| - **Sequence**<br><br>  - Each pseudocode instruction is executed in order<br>- **Assignment**<br><br>  - Assigning the string to `Quote`<br>- **String manipulation**<br><br>  - Using `SUBSTRING()` to extract part of a string<br>- **Case conversion**<br><br>  - Using `LCASE()` (or similar function) to convert the string to lowercase |
| Do I need to use **subprograms**? |
| - In this question, the subprograms are **built-in string handling functions**:<br><br>  - `SUBSTRING(Quote, Start, Number)` – extracts part of a string<br>  - `LCASE(Quote)` – returns the lowercase version of the string |
| **Final answer:** **Answer** |
| **Pseudocode** |
| Quote ← "Learning Never Exhausts The Mind"<br><br>Start ← 25<br><br>Number ← 8<br><br>OUTPUT SUBSTRING(Quote, Start, Number)<br><br>OUTPUT LCASE(Quote) |
