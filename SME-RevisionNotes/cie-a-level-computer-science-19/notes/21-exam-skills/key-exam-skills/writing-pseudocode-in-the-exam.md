---
note_id: "rn_TzSKxcSCgPsmBFc9"
title: "Writing Pseudocode in the Exam"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/key-exam-skills/writing-pseudocode-in-the-exam
path: 21-exam-skills/key-exam-skills/writing-pseudocode-in-the-exam
updated_at: "2026-10-16T12:07:49.211Z"
spec_point_ids: ["spcpt_gNwTnjwvWBmmGq37", "spcpt_vFp8Gkqnpk5YsFPv", "spcpt_jXybnp3BGRphTpcm"]
spec_point_codes: []
guided_study: false
---

# Writing Pseudocode in the Exam

## Why Cambridge pseudocode matters

> **Spec point** — `spcpt_gNwTnjwvWBmmGq37`

## Why Cambridge pseudocode matters

### What is Cambridge pseudocode?

- **Cambridge pseudocode** is the standard way of writing algorithms in 9618 exams
- Its rules are set out in the **Pseudocode Guide for Teachers**, published by Cambridge for each syllabus period
- Questions in **Paper 2** and **Paper 3** ask for answers in pseudocode, and any pseudocode printed in those papers is written in this style (Paper 3 also prints assembly language and declarative code, which follow their own rules)
- Examiners state that following the recommended pseudocode lets them **follow the structure and logic** of an answer and credit it; answers written in a programming language are not accepted when a question asks for pseudocode
- For how to work through Paper 2 itself, including using the Insert, see the [Paper 2 guide](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/paper-guides/paper-2-problem-solving-and-programming/)

### Why do Python users lose marks?

- Most students practise programming in Python (or Java or Visual Basic) for Paper 4
- Examiners warn that the syntax of the language you have studied **is not acceptable** in a pseudocode answer
- The table shows the most common Python habits and the Cambridge equivalent

| Python habit | Cambridge pseudocode |
|---|---|
| `x = 5` | `X ← 5` |
| `if x == 5:` | `IF X = 5 THEN` |
| `!=` | `<>` |
| `elif` | no `ELSEIF`: use a nested `IF` inside `ELSE`, or a `CASE` statement |
| `"Hi " + name` | `"Hi " & Name` |
| `//` and `%` | `DIV` and `MOD` |
| `for i in range(1, 11):` | `FOR Index ← 1 TO 10` ... `NEXT Index` |
| `for item in items:` | no equivalent: loop through the index with a `FOR` loop |
| `len(s)`, `s.upper()` | `LENGTH(S)`, `TO_UPPER(S)` (from the Insert) |
| `print()` and `input()` | `OUTPUT` and `INPUT` |
| `return` inside `def` | `RETURN` inside `FUNCTION ... RETURNS <data type>` |
| `# comment` | `// comment` |

- For changing case, use `TO_UPPER` and `TO_LOWER` from the Insert; the Pseudocode Guide lists `UCASE` and `LCASE` instead, but the Insert is what you have in the exam, so use its function names

## Conventions examiners check

> **Spec point** — `spcpt_vFp8Gkqnpk5YsFPv`

## Conventions examiners check

### How do you set out pseudocode?

- **Keywords** are in upper case: `IF`, `WHILE`, `PROCEDURE`
- **Identifiers** (names of variables, constants and modules) are in mixed case, such as `NumberOfPlayers`

  - They may only contain letters, digits and underscores, and must start with a letter
  - They must **never be keywords**, so `String`, `Input` and `Integer` are not valid names
  - They are not case sensitive, so `Total` and `TOTAL` are the same identifier
- Indent the contents of every `IF`, loop and module (usually by three spaces)
- Comments start with `//`

### Declarations and assignment

- Declare each variable with its data type: `INTEGER`, `REAL`, `CHAR`, `STRING`, `BOOLEAN` or `DATE`
- Constants use `=` and can only be given a *literal value*
- Arrays use **square brackets** and state the lower and upper bound
- Assignment always uses the arrow `←`; the `=` sign is only for comparison (and constants)
- On Paper 3, define user-defined types with `TYPE`: a record with `TYPE ... ENDTYPE`, and an enumerated type with `TYPE Season = (Spring, Summer, ...)`; examiners report students using `ENUM` or `DECLARE` where `TYPE` was needed

- String values go in double quotes (`"Ali"`) and single characters in single quotes (`'A'`)
- To access a field of a record stored in an array, put the index on the **array**, then use dot notation: `Batch[Index].Weight`

### Operators

- Arithmetic: `+`, `-`, `*`, `/`, `DIV` (whole-number quotient) and `MOD` (remainder)

  - `/` always gives a `REAL` result, even if both values are integers
- Comparison: `=`, `<>`, `<`, `>`, `<=`, `>=`
- Logic: `AND`, `OR`, `NOT`; each side of `AND` and `OR` must be a complete condition
- Concatenation: `&`
- Use brackets to make the order of operations clear

### Selection

- Every `IF` needs `THEN` and a matching `ENDIF`
- `CASE` clauses are checked **in order**, and only the first one that matches runs; `OTHERWISE` must come last
- A `CASE` clause can test a range, such as `1 TO 10 : ...`

### Iteration

- `FOR` loops include the `←` and repeat the loop variable after `NEXT`; add `STEP` to count in steps other than 1 (including negative steps)
- `REPEAT ... UNTIL` always runs **at least once**
- `WHILE ... ENDWHILE` may run **zero times**, because the condition is tested first

### Procedures and functions

- A **procedure** is called with `CALL`, as a statement on its own
- A **function** is **never** called with `CALL`; it is used inside an expression, such as an assignment, an `IF` condition or an `OUTPUT`
- When you call a module, write only its name and the values, not the full header with data types
- Parameters are passed **by value** unless `BYREF` is written before them; once written, `BYREF` also applies to the parameters that follow it in the same header

### File handling

- Open a file in `READ`, `WRITE` or `APPEND` mode before using it; `WRITE` creates a new file and wipes any existing data
- Use `READFILE` and `WRITEFILE` (not `READ` or `WRITE` on their own) and close every file with `CLOSEFILE`
- The file name must be in **quotes** when it is written directly, and must be included in `EOF()` and `CLOSEFILE`

## Mistakes that cost marks

> **Spec point** — `spcpt_jXybnp3BGRphTpcm`

## Mistakes that cost marks

### Which pseudocode errors do examiners see most?

- Cambridge examiner reports list invalid pseudocode like the examples below; each one loses marks

| What students wrote | What is wrong | Correct pseudocode |
|---|---|---|
| `FOR X 1 TO 100` | The assignment arrow is missing | `FOR X ← 1 TO 100` |
| `FOR Index ← 1 TO EOF(Filename)` | `EOF` returns `TRUE` or `FALSE`, not a number of lines | `WHILE NOT EOF(Filename)` |
| `IF X = 3 OR 4 OR 5 THEN` | Each side of `OR` must be a full comparison | `IF X = 3 OR X = 4 OR X = 5 THEN` |
| `WHILE Number >= 100 AND <= 200` | The second condition has no left-hand side | `WHILE Number >= 100 AND Number <= 200` |
| `IF Num ← 43 THEN` | `←` assigns a value; it does not compare | `IF Num = 43 THEN` |
| `DECLARE String : STRING` | A keyword is used as an identifier | `DECLARE UserName : STRING` |
| `CALL Valid(MyString)` then `IF RESULT = TRUE THEN` | Functions are not called with `CALL`, and `RESULT` does not exist | `IF Valid(MyString) = TRUE THEN` |
| `Batch.Weight(Index)` | The index belongs to the array of records, in square brackets | `Batch[Index].Weight` |
| `OPENFILE Stock.txt FOR READ` | A file name written directly needs quotes | `OPENFILE "Stock.txt" FOR READ` |
| `OUTPUT "Total: " & Total` (where `Total` is an `INTEGER`) | `&` only joins strings, so an integer must be converted or separated with a comma | `OUTPUT "Total: ", Total` or `OUTPUT "Total: " & NUM_TO_STR(Total)` |
| `FOR WebName in Secret` | This is programming language syntax | Loop through the indexes with `FOR Index ← 1 TO ...` |

- To practise finding and correcting errors like these in a given algorithm, see [Test Data & Finding Errors](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/key-exam-skills/test-data-and-finding-errors/)

### Missing end statements

- Examiners report that many marks are lost through small omissions, such as:

  - a correct procedure or function header with no `ENDPROCEDURE` or `ENDFUNCTION`
  - an `IF` with no `ENDIF`
  - a loop with no `ENDWHILE`, `UNTIL` or `NEXT`

> **Worked Example**
> A global 1D array `Marks` stores the test marks of 30 students. The lower bound of the array is 1.
> 
> A student was asked to write pseudocode for a function `Average()` that returns the mean of the marks in `Marks`. This is their answer:
> 
> Rewrite the answer as valid Cambridge pseudocode.
> 
> **[5]**
> 
> **Answer**:
> 
> - Function header with `RETURNS REAL`, and `ENDFUNCTION` **[1 mark]**
> - Declare and initialise `Total` using `←` **[1 mark]**
> - `FOR` loop from 1 to 30 with `NEXT Index` **[1 mark]**
> - Add each element to `Total` using `←` inside the loop **[1 mark]**
> - `RETURN` the total divided by 30** [1 mark]**
> 
> - `range(30)` counts from 0 to 29, so with a lower bound of 1 it would try to read `Marks[0]`, which does not exist, and would miss `Marks[30]`
> - `print` outputs the value instead of returning it to the calling code

> **Exam Hint**
> - Write the closing keyword (`ENDIF`, `NEXT`, `ENDWHILE`, `ENDFUNCTION`) straight after the opening line, then fill in the body, so you never lose a mark for a missing end statement
> - In a function, finish with `RETURN`, not `OUTPUT`: examiners regularly see `OUTPUT` used where the value should be returned, and it does not gain the mark
