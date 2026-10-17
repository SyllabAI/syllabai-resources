---
note_id: "rn_DJTBpVvwmvrwpdNJ"
title: "Logic Expressions"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/10-boolean-logic/boolean-logic/logic-expressions
path: 10-boolean-logic/boolean-logic/logic-expressions
updated_at: "2024-10-11T07:32:30.605Z"
spec_point_ids: ["spcpt_Bqr6RvC637zVPvBS"]
spec_point_codes: []
guided_study: false
---

# Logic Expressions

## Logic Expressions

> **Spec point** — `spcpt_Bqr6RvC637zVPvBS` · "(c) Write a logic expression from a:
 (i) problem statement
 (ii) logic circuit
 (iii) truth table"

## Logic Expressions

- A **logic expression** is a way of expressing a logic gate or logic circuit as an **equation**
- The **output **appears on the **left **of the equals sign with the **inputs **and **logic gates** on the **right**

| **Gate** | **Symbol** | **Truth Table** | **Logic Expression** |
|---|---|---|---|
| **NOT** | ![not](assets/a35d1c8ac2f8-screenshot-2023-05-30-at-08-24-28.png) | \| **A** \| **Z** \|<br>\|---\|---\|<br>\| 0 \| 1 \|<br>\| 1 \| 0 \| | Z = NOT A |
| **AND** | ![and](assets/28bda956492e-screenshot-2023-05-30-at-08-24-36.png) | \| **A** \| **B** \| **Z** \|<br>\|---\|---\|---\|<br>\| 0 \| 0 \| 0 \|<br>\| 0 \| 1 \| 0 \|<br>\| 1 \| 0 \| 0 \|<br>\| 1 \| 1 \| 1 \| | Z = A AND B |
| **OR** | ![or](assets/46087ced0a82-screenshot-2023-05-30-at-08-24-49.png) | \| **A** \| **B** \| **Z** \|<br>\|---\|---\|---\|<br>\| 0 \| 0 \| 0 \|<br>\| 0 \| 1 \| 1 \|<br>\| 1 \| 0 \| 1 \|<br>\| 1 \| 1 \| 1 \| | Z = A OR B |
| **NAND** | ![nand](assets/88cbded23e3f-screenshot-2023-05-30-at-08-25-01.png) | \| **A** \| **B** \| **Z** \|<br>\|---\|---\|---\|<br>\| 0 \| 0 \| 1 \|<br>\| 0 \| 1 \| 1 \|<br>\| 1 \| 0 \| 1 \|<br>\| 1 \| 1 \| 0 \| | Z = A NAND B |
| **NOR** | ![nor](assets/dea8458c864e-screenshot-2023-05-30-at-08-25-22.png) | \| **A** \| **B** \| **Z** \|<br>\|---\|---\|---\|<br>\| 0 \| 0 \| 1 \|<br>\| 0 \| 1 \| 0 \|<br>\| 1 \| 0 \| 0 \|<br>\| 1 \| 1 \| 0 \| | Z = A NOR B |
| **XOR** | ![xor](assets/9e0424c74965-screenshot-2023-05-30-at-08-25-28.png) | \| **A** \| **B** \| **Z** \|<br>\|---\|---\|---\|<br>\| 0 \| 0 \| 0 \|<br>\| 0 \| 1 \| 1 \|<br>\| 1 \| 0 \| 1 \|<br>\| 1 \| 1 \| 0 \| | Z = A XOR B |

- Logic circuits containing multiple gates can also be expressed as logic expressions/statements

**An example logic circuit containing two inputs**

![screenshot-2023-05-30-at-09-28-55](../../../assets/7cd17a4e3c6a-screenshot-2023-05-30-at-09-28-55.png)

- The logic circuit above can be expressed as the logic expression **Q= NOT(A OR B)**

** **

**An example logic circuit containing two inputs**

![screenshot-2023-05-30-at-09-29-06](../../../assets/6ff4dde71d02-screenshot-2023-05-30-at-09-29-06.png)

- The logic circuit above can be expressed as the logic expression **Q= (NOT A) AND B **

**An example logic circuit containing three inputs**

- The logic circuit above can be expressed as the logic expression **P = ((NOT A) OR B) NAND C**

** **

**An example logic circuit containing three inputs**

![screenshot-2023-05-30-at-09-35-30](../../../assets/0f6f0c87413b-screenshot-2023-05-30-at-09-35-30.png)

- This logic circuit above can be expressed as **X = NOT (A NAND B) OR (B NOR C)**

> **Exam Hint**
> - You may be required to write a logic expression/statement from a **truth table** or a **logic circuit**. You may also have to do the opposite - **draw a logic circuit** and **complete a truth table for a logic expression**

> **Worked Example**
> Consider the logic statement: **X = (((A AND B) OR (C AND NOT B)) XOR NOT C) **
> 
> a. Draw a logic circuit to represent the given logic statement. **[6]**
> 
> **Final answer:** **Answer**
> 
> ![screenshot-2023-05-30-at-09-37-21](assets/633425a0f395-screenshot-2023-05-30-at-09-37-21.png)
> 
> One mark per correct logic gate, with the correct input
