---
note_id: "rn_VRrwVG8K53bNNK3S"
title: "Test Data & Finding Errors"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/key-exam-skills/test-data-and-finding-errors
path: 21-exam-skills/key-exam-skills/test-data-and-finding-errors
updated_at: "2026-10-16T12:09:29.271Z"
spec_point_ids: ["spcpt_BmNGryXnMMH7WgwC", "spcpt_FrvxVnNx46TCCkvZ", "spcpt_T66sF64nsCsGqWvc", "spcpt_GkTZs7mtgYmc6fGX", "spcpt_pBtSFBHmNrnJXhPd"]
spec_point_codes: []
guided_study: false
---

# Test Data & Finding Errors

## Types of test data

> **Spec point** — `spcpt_BmNGryXnMMH7WgwC`

## Types of test data

### What test data does Cambridge expect?

- The 9618 syllabus names three types of test data: **normal**, **abnormal** and **extreme/boundary**
- Cambridge treats **extreme** and **boundary** as one category, and mark schemes accept either word
- If you have studied GCSE Computer Science, note that the word "erroneous" does not appear in 9618 mark schemes; use **abnormal** instead

| Type of test data | What it is | Expected result | Example for a range of 150 to 155 inclusive |
|---|---|---|---|
| **Normal** | Data inside the acceptable range, of the correct type | Accepted and processed | 153 |
| **Extreme/boundary** | The largest and smallest acceptable values | Accepted | 150 and 155 |
| **Abnormal** | Data that should be rejected, such as a value outside the range | Rejected | 149, 156 or 200 |

- Values **just outside** the range, such as 149 and 156, test the boundary from the other side

  - Mark schemes accept these as **abnormal** or **boundary**, as long as the expected result is "rejected"
- The marks come from the **value and its expected result**; the label alone rarely scores

## How to choose test data for a validation rule

> **Spec point** — `spcpt_FrvxVnNx46TCCkvZ`

## How to choose test data for a validation rule

### How do you write a test plan in the exam?

- Most 9618 test plan questions give one completed row and ask you to "complete the table by writing additional tests", usually for **4 marks**, one per row
- Follow these steps:

  1. **Find the exact limits**: "24 to 37, inclusive" means 24 and 37 are both valid; examiners note that "30 to 40" also includes both boundary values
  2. **Test each boundary from both sides**: the lowest valid value, the highest valid value and the value just outside each one
  3. **Give the expected result** in the form the code produces, such as `TRUE`, `FALSE`, `"PASS"` or `"FAIL"`
  4. **Make every test different**: each row must test something new
- Keep every test value the **data type the question states**; if the function takes an integer, real numbers and characters are not valid test data for that question
- Some questions ask for **test data sequences** for a loop that ends on a terminator value, such as 99; each sequence should end with the terminator and test something different, such as only odd values, only even values, or just the terminator with no values before it

### What mistakes do examiners see in test plans?

- Examiner reports for 9618 Paper 2 highlight these mistakes:

  - **Repeating normal data**: for a range of 150 to 155, students gave several values from 151 to 154, which all test the same thing
  - **Ignoring the stated data type**: when the question said the sensor produces an integer, many students gave characters and real numbers
  - **Copying the example**: using test data that was too similar to the example given in the question was a common mistake

## Types of error

> **Spec point** — `spcpt_T66sF64nsCsGqWvc`

## Types of error

### What are syntax, logic and run-time errors?

- **Syntax error**: a statement breaks the rules (grammar) of the language, so the program cannot be translated

  - Example: `NEXT Index` used to end a `WHILE` loop, instead of `ENDWHILE`
- **Logic error**: the program runs but does not produce the expected result

  - Example: `IF Num > Min THEN` in an algorithm that should find the minimum
- **Run-time error**: the program fails while it is running, for example by crashing or stopping responding

  - Example: accessing `Data[0]` when the array is declared `ARRAY[1:200]`, or dividing by zero

### How do examiners ask about errors?

- Questions give pseudocode that contains a stated number of errors, and ask you to find them, for example:

  - "The pseudocode contains two syntax errors and one other error. Identify the errors." [3]
  - "The pseudocode contains three errors due to the incorrect use of operators. Identify each error and state the correction required." [3]
  - "Write the three statements and explain how each could generate a run-time error."
- When a question asks about errors in a given scenario, answer **about that code**; examiners report that some students gave only a textbook definition of a syntax error, without relating it to the scenario

> **Exam Hint**
> - In one recent series, many students found all three errors in a piece of pseudocode but lost marks by putting them in the wrong category, so decide the category of each error before you write it

## Identifying and correcting errors in given code

> **Spec point** — `spcpt_GkTZs7mtgYmc6fGX`

## Identifying and correcting errors in given code

### How do you find errors in pseudocode?

- Check the code in this order:

  1. **Structure**: every `IF` has an `ENDIF`, every `WHILE` has an `ENDWHILE`, every `FOR` has a `NEXT` with the same variable
  2. **Operators**: `←` for assignment and `=` for comparison; `&` joins strings and `+` adds numbers
  3. **Array indexes**: every index stays within the declared bounds, including the first and last time round the loop
  4. **Conditions**: `>` vs `>=`, `AND` vs `OR`, and whether the loop ends at the right point
  5. **Initial values**: whether a starting value such as `Min ← 999` could give a wrong answer for some inputs
- Write your answer in the form the question asks for

  - If it asks you to **identify** the error, quote or describe the faulty statement
  - If it also asks for the **correction**, give the corrected statement as well
  - Examiners report that some students only gave a corrected line when the question asked them to identify the error

### Example: errors due to operators

- The pseudocode below should find the **minimum** of a series of numbers and count them

- The three operator errors, and their corrections, are:

  - `Num > Min` should be `Num < Min`
  - `Count & 1` should be `Count + 1`
  - `NextInput ← "END"` should be `NextInput = "END"`

> **Worked Example**
> A function `ValidTickets()` will:
> 
> - take an integer value as a parameter
> - return `TRUE` if the value is within the range 1 to 8, inclusive
> - otherwise return `FALSE`
> 
> **(a)** Complete the table to define a test plan to thoroughly test the function. The first row has been completed.
> 
> | Type of test data | Test data value | Expected result |
> |---|---|---|
> | Normal | 5 | TRUE |
> |   |   |   |
> |   |   |   |
> |   |   |   |
> |   |   |   |
> 
> **[4]**
> 
> **(b)** The function is written in pseudocode:
> 
> The function contains a logic error. Identify which test from your test plan would reveal the error and state the correction required.
> 
> **[2]**
> 
> **Answer**:
> 
> **(a)** One mark per row:
> 
> - Extreme/boundary, 1, TRUE **[1 mark]**
> - Extreme/boundary, 8, TRUE **[1 mark]**
> - Abnormal (or boundary), 0, FALSE **[1 mark]**
> - Abnormal (or boundary), 9, FALSE **[1 mark]**
> 
> **(b)** The test with value 1 would return `FALSE` instead of `TRUE` **[1 mark]**
> 
> `Number > 1` should be `Number >= 1` **[1 mark]**
> 
> Only the boundary test reveals the error, because 5, 8, 0 and 9 all give the expected result even with the faulty condition.

## Testing methods

> **Spec point** — `spcpt_pBtSFBHmNrnJXhPd`

## Testing methods

### Which testing method should you name?

- The 9618 syllabus lists nine testing methods; questions often describe a situation and ask you to name or describe the method

  - **Dry run**: working through the code by hand, often by completing a trace table
  - **Walkthrough**: going through the code or algorithm step by step, often with other people, to check its logic
  - **White-box testing**: testing every possible path through the code, using knowledge of the code itself
  - **Black-box testing**: testing that inputs give the expected outputs, without looking at the code
  - **Stub testing**: replacing modules that are not yet written with simple dummy modules that return a known result or output a message to show they have been called
  - **Integration testing**: testing modules together once each one has been shown to work on its own
  - **Alpha testing**: testing by the developer's own team before the software is released to users
  - **Beta testing**: testing by a small group of potential users, who report problems and suggest improvements
  - **Acceptance testing**: testing by the client to check that the finished program meets the agreed requirements
- **Stub testing** and **integration testing** are often confused

  - Stub testing happens **before** a module exists, using a dummy in its place
  - Integration testing happens **after** modules are written and individually tested, by combining them
