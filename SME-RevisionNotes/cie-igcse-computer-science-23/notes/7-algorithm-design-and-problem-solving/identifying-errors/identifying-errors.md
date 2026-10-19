---
note_id: "rn_S7RDWHNYxbpjsr8v"
title: "Identifying Errors"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/7-algorithm-design-and-problem-solving/identifying-errors/identifying-errors
path: 7-algorithm-design-and-problem-solving/identifying-errors/identifying-errors
updated_at: "2025-05-07T13:57:02.303Z"
spec_point_ids: ["spcpt_bbfHbx6fNFZfXFzy", "spcpt_yt5Vwv5SW4wP7zvS", "spcpt_bk4PrThHpWZnkVZY"]
spec_point_codes: []
guided_study: false
---

# Identifying Errors

## Identifying errors

> **Exam Hint**
> *Cambridge IGCSE 0478 regularly assesses your ability to identify, describe, and fix ****syntax****, ****logic****, and ****runtime errors****, especially using ****trace tables**** and ****dry runs****. This page mirrors the question style and mark scheme language of Paper 2.*

- Designing algorithms is a skill that must be developed and when designing algorithms, mistakes and issues will occur
- Trace tables can also help to find any kind of error in a program or algorithm
- There are three main categories of errors that when designing algorithms a programmer must be able to identify & fix, they are:

  - **Syntax errors**
  - **Logic errors**
  - **Runtime errors**

> **Exam Hint**
> *When describing an error:*
> 
> - *Use “****prevents the program from running****” for syntax*
> - *Use “****produces incorrect output****” for logic*
> - *Use “****causes the program to crash****” for runtime*
> 
> *These are the exact phrases that earn marks in the exam.*

## Syntax Errors

> **Spec point** — `spcpt_bbfHbx6fNFZfXFzy` · "8 Identify errors in given algorithms and suggest
ways of correcting these errors"

## Syntax Errors

### What is a syntax error?

- A syntax error is **an error that breaks the grammatical rules of a programming language** and **stops it from running**
- Examples of syntax errors are:

  - **Typos and spelling errors **
  - **Missing or extra brackets or quotes**
  - **Misplaced or missing semicolons**
  - **Invalid variable or function names**
  - **Incorrect use of operators**
  - **Incorrectly nested loops & blocks of code**

| **Python code - with syntax errors** |
|---|
|   |
| **Python code - without syntax errors** |
|   |
| Syntax errors |
| 1. Missing semicolon `def generate_username(first_name, last_name)`<br>2. Incorrectly spelt function name `first_name = imput("Enter your first name: ")`<br>3. Typo in variable name `usdrname = generate_username(first_name, last_name)`<br>4. Missing parenthesis `main` |

> **Exam Hint**
> *Examiners won’t give marks for vague phrases like “the program didn’t work.”*
> *You must ****name the error type****, ****locate it****, and ****explain the impact**** on the output or execution.*

## Logic Errors

> **Spec point** — `spcpt_yt5Vwv5SW4wP7zvS` · "8 Identify errors in given algorithms and suggest
ways of correcting these errors"

## Logic Errors

### What is a logic error?

- A logic error is where** incorrect code is used that causes the program to run**, but **produces an incorrect output or result**
- Logic errors can be difficult to identify by the person who wrote the program, so one method of finding them is to use '**Trace Tables**'
- Examples of logic errors are:

  - **Incorrect use of operators  (< and >)**
  - **Logical operator confusion (AND for OR)**
  - **Looping one extra time**
  - **Indexing arrays incorrectly (arrays indexing starts from 0)**
  - **Using variables before they are assigned**
  - **Infinite loops**

| **Python code** |
|---|
|   |

#### Logic errors

| Test number | **Test data** | **Expected outcome** | **Actual outcome** | **Changes needed? (Y/N)** |
|---|---|---|---|---|
| **1** | Length = 5<br><br>Width = 5 | "The area of the rectangle is approximately 25 square units." | **Final answer:** **"The area of the rectangle is approximately 25.00 square units."** | **N** |
| **2** | Length = 10<br><br>Width = 0 | "Length and width must be positive values." | *"The area of the rectangle is approximately 0.00 square units."* | **Y **<br>**should not accept 0 input as not positive** |

- Logic error **located **on line `if length < 0 or width < 0:`
- Logic error **identified **in expression` < 0`, should be` <= 0 `so that 0 is not accepted as valid input for length or width

## Runtime Errors

> **Spec point** — `spcpt_bk4PrThHpWZnkVZY` · "8 Identify errors in given algorithms and suggest
ways of correcting these errors"

## Runtime Errors

### What is a runtime error?

- A runtime error is where** an error causes a program to crash**
- Examples of runtime errors are:

  - **Dividing a number by 0**
  - **Index out of the range of an array**
  - **Unable to read or write a drive**

| **Python code** |
|---|
|   |

#### Runtime errors

| Test number | **Test data** | **Expected outcome** | **Actual outcome** | **Changes needed? (Y/N)** |
|---|---|---|---|---|
| **1** | Length = 10<br><br>Width = 10 | "The area of the rectangle is approximately 100 square units." | **Final answer:** **"The area of the rectangle is approximately 100.00 square units."** | **N** |
| **2** | Length = "abc"<br><br>Width = 0 | "Program could not convert string to float, try again" | *Program crashed* | **Y **<br>**should give error message and ask user to enter again** |

- Runtime error **located **in

- Runtime error **identified **as **missing iteration**  (while loop) so program does not ask user to enter width and height again
- Corrected code now includes a while loop
