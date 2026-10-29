---
note_id: "rn_34zBXftcgbc6drNT"
title: "Variables & Constants"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/8-programming/programming-concepts/variables-and-constants
path: 8-programming/programming-concepts/variables-and-constants
updated_at: "2024-12-03T16:05:24.556Z"
spec_point_ids: ["spcpt_N9ysmqPWTHkn4yct"]
spec_point_codes: []
guided_study: true
---

# Variables & Constants

## Variables & Constants

> **Spec point** — `spcpt_N9ysmqPWTHkn4yct` · 1 Declare and use variables and constants

## Variables & Constants

### What is a variable?

- A variable is an **identifier **that **can change** in the lifetime of a program
- Identifiers should be:

  - In **mixed case** (Pascal case)
  - Only** contain letters** (A-Z, a-z)
  - Only **contain digits** (0-9)
  - **Start with a capital** letter and not a digit
- A variable can be** associated a datatype** when it is declared
- When a variable is declared, **memory is allocated**  based on the data type indicated

| **Pseudocode ** |
|---|
| **DECLARE <identifier> : <datatype>** |
| `DECLARE Age : INTEGER` |
| `DECLARE  Price : REAL` |
| `DECLARE GameOver : BOOLEAN` |

| **Python** |
|---|
| `score = int() `*# whole number* |
| `cost = float() `*# decimal number* |
| `light = bool()` *# data can only have one or two values* |

### What is a constant?

- A constant is an **identifier set once in the lifetime of a program **
- Constants are generally named in **all uppercase characters**
- Constants **aid **the **readability **and **maintainability**
- If a constant needs to be changed, it should only need to be altered **in one place** in the whole program

| **Pseudocode** |
|---|
| ** CONSTANT <identifier> **←** <value>** |
| `CONSTANT PI ← 3.142` |
| `CONSTANT PASSWORD ← "letmein"` |
| `CONSTANT HIGHSCORE ← 9999` |

| **Python** |
|---|
| `PI = 3.142` |
| `VAT = 0.20` |
| `PASSWORD = "letmein"` |
