---
note_id: "rn_M6wSxbrqMMTpfpwt"
title: "Logic Gates"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/10-boolean-logic/boolean-logic/logic-gates
path: 10-boolean-logic/boolean-logic/logic-gates
updated_at: "2025-05-07T13:00:39.443Z"
spec_point_ids: ["spcpt_PYd6kWddn3J27m4s"]
spec_point_codes: []
guided_study: false
---

# Logic Gates

## Logic gates

> **Spec point** — `spcpt_PYd6kWddn3J27m4s` · "1 Identify and use the standard symbols for logic
gates"

## Logic gates

### What is Boolean logic?

> **Exam Hint**
> *Cambridge IGCSE 0478 expects you to identify logic gates, write Boolean expressions, and interpret simple logic circuits. This page covers exactly the gates and formats examiners use—nothing more, nothing less.*

- Boolean logic is used in computer science and electronics to make **logical decisions**
- Boolean operators are either **TRUE **or **FALSE**, often represented as **1 **or **0**
- Inputs and outputs are given **letters to represent them**
- To define Boolean logic we use **special symbols** to make **writing expressions** much **easier **

### What are logic gates?

- Logic gates are a **visual way** of representing a **Boolean expression**
- The logic gates covered in this course are:

  - **AND**
  - **OR**
  - **NOT**
  - **XOR**
  - **NAND**
  - **NOR**

#### AND

| **Expression operator** | **Circuit symbol** | **Explanation** |
|---|---|---|
| (A **AND **B) | ![and-gate](assets/e8e6485b0912-and-gate.png) | Returns TRUE only if** both** inputs are TRUE<br><br>**TRUE **AND **TRUE **= **TRUE**<br><br>Otherwise = FALSE |

#### OR

| **Expression operator** | **Circuit symbol** | **Explanation** |
|---|---|---|
| (A **OR **B) | ![or-gate](assets/5b7eee70ea7c-or-gate.png) | Returns TRUE if **either** input is TRUE<br><br>**TRUE **OR **FALSE **= **TRUE**<br><br>**FALSE **OR **FALSE **= **FALSE** |

#### NOT

| **Expression operator** | **Circuit symbol** | **Explanation** |
|---|---|---|
| (**NOT **A) | ![not-gate](assets/7ed9b463218d-not-gate.png) | **Reverses **the input value<br><br>NOT **TRUE **= **FALSE**<br><br>NOT **FALSE **= **TRUE** |

#### XOR (exclusive OR)

| **Expression operator** | **Circuit symbol** | **Explanation** |
|---|---|---|
| (A **XOR** B) | ![xor](assets/9e0424c74965-screenshot-2023-05-30-at-08-25-28.png) | Returns TRUE if **either** input is TRUE but **NOT **both<br><br>**TRUE **OR **FALSE **= **TRUE**<br><br>**FALSE **OR **FALSE **= **FALSE**<br><br>**TRUE **OR **TRUE **=** FALSE** |

> **Exam Hint**
> *The most common exam mistake is confusing *`OR`* and *`XOR`*. Remember: *`XOR`* is only ****true if exactly one input is true****. It’s false if both are true or both are false.*

#### NAND (not and)

| **Expression operator** | **Circuit symbol** | **Explanation** |
|---|---|---|
| (A **NAND **B) | ![screenshot-2023-05-30-at-08-25-01](assets/88cbded23e3f-screenshot-2023-05-30-at-08-25-01.png) | Returns TRUE if **either or both **inputs are FALSE<br><br>**TRUE **OR **FALSE **= **TRUE**<br><br>**FALSE **OR **FALSE **= **TRUE**<br><br>**TRUE **OR **TRUE **=** FALSE** |

#### NOR (not OR)

| **Expression operator** | **Circuit symbol** | **Explanation** |
|---|---|---|
| (A **NOR **B) | ![screenshot-2023-05-30-at-08-25-22](assets/dea8458c864e-screenshot-2023-05-30-at-08-25-22.png) | Returns TRUE if **both **inputs are FALSE<br><br>**TRUE **OR **FALSE **= **FALSE**<br><br>**FALSE **OR **FALSE **= **TRUE**<br><br>**TRUE **OR **TRUE **=** FALSE** |

> **Exam Hint**
> *“Draw the logic circuit for the expression (A AND B) OR (NOT C)”*
> Tip: **Draw from left to right**, and label all inputs clearly. Mislabelled inputs = lost marks
