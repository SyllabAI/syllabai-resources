---
note_id: "rn_hqGV8kcwvBr8hr45"
title: "Exam Tips"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/exam-technique/exam-tips
path: 21-exam-skills/exam-technique/exam-tips
updated_at: "2026-10-16T11:54:10.668Z"
spec_point_ids: ["spcpt_m7hC7FTwnS25h38t", "spcpt_nwYm7Z2rQ7WMMhqF", "spcpt_GHCBGtWx5yR43dYY", "spcpt_ySP4Yj9bfsBCGmVg", "spcpt_Zzw9XyHdgKpXf32D"]
spec_point_codes: []
guided_study: false
---

# Exam Tips

## How the 9618 exams are structured

> **Spec point** — `spcpt_m7hC7FTwnS25h38t`

## How the 9618 exams are structured

### What papers do you sit?

- Cambridge International AS & A Level Computer Science (9618) is assessed by up to **four papers**, each worth **75 marks**
- **AS Level** students sit Papers 1 and 2
- **A Level** students sit all four papers, either all at once or staged over two years (Papers 1 and 2 first, then Papers 3 and 4)
- **Calculators are not allowed in any paper**, so binary, hexadecimal and file size calculations must be done by hand

| Paper | Duration | Weighting | What it involves |
|---|---|---|---|
| Paper 1: Theory Fundamentals | 1 hour 30 minutes | 50% of AS, 25% of A Level | Written paper on syllabus sections 1 to 8; short and longer answers |
| Paper 2: Fundamental Problem-solving and Programming Skills | 2 hours | 50% of AS, 25% of A Level | Written paper on sections 9 to 12; answers in pseudocode, with an **Insert** listing the built-in functions and operators |
| Paper 3: Advanced Theory | 1 hour 30 minutes | 25% of A Level | Written paper on sections 13 to 20 |
| Paper 4: Practical | 2 hours 30 minutes | 25% of A Level | Programming on a computer in Java, Visual Basic or Python (console mode), with no internet; code and test evidence go in an **evidence document** |

### How long should you spend per mark?

- Every paper is out of 75, so the time per mark depends on the paper's length

  - **Papers 1 and 3**: about 1 minute 10 seconds per mark
  - **Paper 2**: about 1 minute 35 seconds per mark
  - **Paper 4**: about 2 minutes per mark
- A 6-mark algorithm question in Paper 2 is therefore worth about 10 minutes, so if you have spent 20 minutes on it, move on and come back later

## What examiners are looking for

> **Spec point** — `spcpt_nwYm7Z2rQ7WMMhqF`

## What examiners are looking for

### What are the assessment objectives?

- Every mark in 9618 is awarded against one of three **assessment objectives (AOs)**:

  - **AO1**: demonstrate knowledge and understanding of the principles and concepts of computer science
  - **AO2**: apply that knowledge and understanding, including to analyse problems in computational terms
  - **AO3**: design, program and evaluate computer systems to solve problems, making reasoned judgements about these
- The balance changes between papers:

  - Papers 1 and 3 are **60% AO1 and 40% AO2**, so nearly half of the marks need you to apply knowledge, not just recall it
  - Paper 2 is **40% AO2 and 60% AO3**, so most marks come from designing and writing pseudocode
  - Paper 4 is **100% AO3**, so every mark comes from working code and testing evidence
- Across the full A Level, the split is AO1 30%, AO2 30% and AO3 40%: **more marks come from programming and problem-solving than from recall**

## Top exam tips for 9618

> **Spec point** — `spcpt_GHCBGtWx5yR43dYY`

## Top exam tips for 9618

### Answer in the context of the scenario

- Many questions are set around a scenario, such as a company, a school system or a device
- Examiner reports note in almost every series that **generic answers lose marks** when the question gives a scenario
- For example, if a question asks why lossy compression would not be used for a particular file, a description of lossy compression on its own scores nothing; the answer must say why it is unsuitable **for that file**

### Use technical terms precisely

- Computer science terms have exact meanings, and using the wrong one can change the meaning of the whole answer
- Examiners give this example: compression does **not** make "the transmission speed faster"; it makes **the time taken to transmit the file shorter**, because transmission speed depends on the connection, not the file
- Other distinctions examiners check include data vs information, memory vs storage, record vs file, identifier vs literal value, and `OUTPUT` vs `RETURN`
- Avoid brand names: write "a word processor" rather than naming a product, as brand and company names cannot be credited

### Match your answer to the command word

- The command word tells you how much detail is needed

  - **Identify** or **State** needs a short, precise answer
  - **Describe** needs the features or steps
  - **Explain** needs the reason why or how, usually with a "because" or "so that"
- Examiners point out that an "explain" question needs more detail than an "identify" question, so match the length and depth of your answer to the word
- See the [9618 command words](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/exam-technique/command-words/) page for every word used in 9618 and how to answer each one

### Do not repeat the question

- Paper 2 examiner reports give this warning in most series: **answering by repeating phrases from the question gains no marks**
- If the question says "a program stores scores in an array", writing "the program uses an array to store scores" adds nothing; each mark needs a new point

### Read the whole question before you start

- Some questions give an example in the stem and then **exclude it from the answer**
- For example, if a question states that a range check is a validation check and asks for **two other** validation checks, a range check scores nothing
- Look for words such as "other", "different", "apart from" and "using the given data"

### Use Cambridge pseudocode, not your programming language

- In Papers 2 and 3, pseudocode must follow the Cambridge **Pseudocode Guide for Teachers**
- Python syntax such as `len()`, `+=` or `elif` is **not** acceptable when a question asks for pseudocode
- In Paper 2, only use the functions listed in the **Insert**; examiners will not credit language-specific functions that are not in it
- Do not use *reserved words* as identifiers: `DECLARE Input : STRING` and `DECLARE Integer : INTEGER` both lost marks in recent series

### Show your working and make the final answer clear

- For number base conversions, floating-point questions and low-level program traces, write out your working
- Some questions say "show your working" and award marks for it, so a correct answer alone may not get full credit
- **Underline or box your final answer** so the examiner can find it

### Attempt every question

- Examiners report that even the hardest Paper 2 algorithm questions **contain accessible marks**, such as declaring variables, setting up a loop or returning a value
- In Paper 4, students who skipped an earlier part could still gain marks on later parts, for example by calling a subroutine they had not managed to write
- A blank answer is guaranteed to score zero

> **Worked Example**
> A photographer emails high-resolution photographs to a client. The client prints the photographs as large posters.
> 
> Explain why the photographer should **not** use lossy compression for these files.
> 
> **[2]**
> 
> **Answer**:
> 
> **Weak answer (0 marks):** "Lossy compression removes data from the file to make it smaller. It is used for images and sound."
> 
> This only describes lossy compression and never mentions the photographs or the posters.
> 
> **Strong answer (2 marks):**
> 
> - Lossy compression permanently removes data from the file, so the original image cannot be restored **[1 mark]**
> - The posters are printed at a large size, so the lost detail would make them visibly lower in quality **[1 mark]**
> 
> The second mark is only available because the answer links the lost data to the client printing large posters.

> **Exam Hint**
> - Before you write, underline the scenario details in the question; aim to use at least one of them in every answer that is worth more than 1 mark
> - When you finish a question, check that every point you have written is a new point, not the question reworded, because each mark needs a separate, creditworthy idea

## Common mistakes that lose marks

> **Spec point** — `spcpt_ySP4Yj9bfsBCGmVg`

## Common mistakes that lose marks

- These mistakes all appear in Cambridge examiner reports for 9618, most of them in more than one series

| Mistake | Why it loses marks | Instead |
|---|---|---|
| Describing a concept without linking it to the scenario | Application (AO2) marks need the scenario | Name the scenario in your answer and explain the effect on it |
| `Average ← Num1 + Num2 + Num3 / 3` | Without brackets, only `Num3` is divided by 3 | `Average ← (Num1 + Num2 + Num3) / 3` |
| `X` used for multiplication in pseudocode | `X` is not an arithmetic operator | Use `*` |
| `OUTPUT` used inside a function that should return a value | The value never reaches the calling code | Use `RETURN` |
| Using `INPUT` statements inside a subroutine instead of parameters | The question asked for values to be passed in | Use the parameters given in the subroutine header |
| Writing in pencil and then going over it in ink | Scanned scripts pick up both, and illegible answers score nothing | Plan on a blank page and cross the plan out |
| Squeezing a corrected answer into the original space | The examiner may not be able to read it | Write it on a blank page and add a note such as "see additional page 1" |
| Giving more answers than the question asks for | Only the first answers up to the number asked for are marked, and only the first answer in each numbered space | Give exactly the number asked for, one per numbered space |

### Paper 4: how do you lose marks on evidence?

- In Paper 4, **marks can only be given for what is in the evidence document**
- Examiner reports highlight these problems:

  - Code pasted as a **screenshot** instead of copied as text, which can be unreadable (especially on a dark integrated development environment (*IDE*) background)
  - Code cut off at the edge of the page, or the start of a subroutine missing
  - Test screenshots that do not show the **input data**, so the examiner cannot check that the output matches it
- Paste code as text, check that every line is visible, and make sure each test screenshot shows both the input and the output

## How to revise for each paper

> **Spec point** — `spcpt_Zzw9XyHdgKpXf32D`

## How to revise for each paper

- Each paper needs a different kind of practice:

  - **Paper 1**: learn definitions precisely, then practise applying them to unfamiliar scenarios
  - **Paper 2**: write pseudocode by hand under timed conditions, using the Insert
  - **Paper 3**: practise the multi-step methods (floating-point normalisation, Boolean algebra, Karnaugh maps, Dijkstra's algorithm) until each step is automatic
  - **Paper 4**: write and test full programs on a computer in your chosen language, and practise filling in an evidence document
- See the guide for each paper for its question types, plus the command words and pseudocode pages:

  - [How to answer Paper 1: Theory Fundamentals](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/paper-guides/paper-1-theory-fundamentals/)
  - [How to answer Paper 2: Problem-solving and Programming](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/paper-guides/paper-2-problem-solving-and-programming/)
  - [How to answer Paper 3: Advanced Theory](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/paper-guides/paper-3-advanced-theory/)
  - [How to approach Paper 4: Practical](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/paper-guides/paper-4-practical/)
  - [9618 command words](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/exam-technique/command-words/)
  - [Writing Cambridge pseudocode in the exam](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/key-exam-skills/writing-pseudocode-in-the-exam/)
