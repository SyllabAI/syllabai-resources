---
note_id: "rn_yzt5KPtSyJ6g9Gpv"
title: "Faults & errors"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/12-software-development/program-testing-and-maintenance/faults-and-errors
path: 12-software-development/program-testing-and-maintenance/faults-and-errors
updated_at: "2026-10-01T11:52:50.787Z"
spec_point_ids: ["spcpt_jV3jdn2q4Wv6vVmY"]
spec_point_codes: []
guided_study: false
---

# Faults & errors

## Error types

> **Spec point** — `spcpt_jV3jdn2q4Wv6vVmY`

## Error types

### What are the common types of error?

- Designing algorithms is a skill that must be developed and when designing algorithms, **mistakes and issues will occur**
- **Trace tables** can also help to find any kind of error in a program or algorithm
- There are three main categories of errors that when designing algorithms a programmer must be able to identify & fix, they are:

  - **Syntax errors**
  - **Logic errors**
  - **Runtime errors**

## Syntax errors

### What is a syntax error?

- A syntax error is **an error that breaks the grammatical rules of a programming language** and **stops it from running**
- Examples of syntax errors are:

  - **Typos and spelling errors **
  - **Missing or extra brackets or quotes**
  - **Misplaced or missing semicolons**
  - **Invalid variable or function names**
  - **Incorrect use of operators**
  - **Incorrectly nested loops & blocks of code**

| **Pseudocode - with syntax errors** |
|---|
|   |
| **Pseudocode - without syntax errors** |
|   |
| **Syntax errors** |
| - `FUNCTION GenerateUsername(FirstName STRING, ...)`<br><br>  - **Missing colon** between the parameter name and its data type<br>  - Should be `FirstName : STRING`<br>- `Username = LEFT(...)`<br><br>  - **Uses =** instead of the assignment operator ←<br>  - Should be `Username ← ...`<br>- `Username ← GenerateUsername[FirstName, LastName]`<br><br>  - **Square brackets []** used instead of parentheses () for a function call<br>  - Should be `GenerateUsername(FirstName, LastName)`<br>- `CALL Main`<br><br>  - **Missing parentheses** in the procedure call<br>  - Should be `CALL Main()` |

## Logic errors

### What is a logic error?

- A logic error is where** incorrect code is used that causes the program to run**, but **produces an incorrect output or result**
- Logic errors can be difficult to identify by the person who wrote the program, so one method of finding them is to use '**Trace Tables**'
- Examples of logic errors are:

  - **Incorrect use of operators  (< and >)**
  - **Logical operator confusion (AND for OR)**
  - **Looping one extra time**
  - **Indexing arrays incorrectly (arrays indexing starts from 0)**
  - **Using variables before they are assigned**
  - **Using an array index that is one too high or one too low**

| Pseudocode |
|---|
|   |

#### Logic errors

| **Line** | **Error** | **Correction** |
|---|---|---|
| `IF Length > 0 OR Width > 0 THEN` | The check allows one value to be negative or zero, which is not valid | Should be `IF Length > 0 AND Width > 0 THEN` |
| `Area ← Width - Length` | Incorrect calculation: subtracts instead of multiplying to find the area | Should be `Area ← Length * Width` |

## Runtime errors

### What is a runtime error?

- A run-time error is an error that occurs **while the program is running** and causes it to **crash** or **stop responding** ('freeze')
- Examples of run-time errors are:

  - **Dividing a number by 0**
  - **Using an array index outside the bounds of the array**
  - **Calling a function with invalid parameters**
  - **A conditional loop whose terminating condition is never satisfied**, so the program stops responding
  - **Being unable to read or write a file**

| **Pseudocode** |
|---|
|   |

#### Runtime error

| **Line** | **Error** | **Correction** |
|---|---|---|
|   | If the user enters 0 for the number of students, the program tries to divide by zero and crashes while it is running | Check the value before dividing:<br><br>`IF NumberOfStudents > 0 THEN`<br><br>`  RETURN Total /  NumberOfStudents`<br><br>`ELSE`<br><br>`  RETURN 0`<br><br>`ENDIF` |

> **Worked Example**
> Each pseudocode statement in the following table may contain an error due to the incorrect use of the function or operator.
> 
> Describe the error in each case, or write ‘NO ERROR’ if the statement contains no error.
> 
> You can assume that none of the variables referenced are of an incorrect type.**[5]**
> 
> | Statement | Error |
> |---|---|
> | `Result ← 2 & 4` |   |
> | `SubString ← MID("pseudocode", 4, 1)` |   |
> | `IF x = 3 OR 4 THEN` |   |
> | `Result ← Status AND INT(x/2)` |   |
> | `Message ← "Done" + LENGTH(MyString)` |   |
> 
> **Final answer:** **Answer**
> 
> | Statement | Error |
> |---|---|
> | `Result ← 2 & 4` | Should be arithmetic<br><br>operator (not &) **OR** 2 and 4<br><br>should be CHAR / STRING |
> | `SubString ← MID("pseudocode", 4, 1)` | NO ERROR |
> | `IF x = 3 OR 4 THEN` | Not Boolean values /<br><br>incorrect operator **OR**<br><br>Condition incorrect |
> | `Result ← Status AND INT(x/2)` | `INT(X/2)` doesn't evaluate<br><br>to a Boolean value /<br><br>incorrect operator |
> | `Message ← "Done" + LENGTH(MyString)` | Can’t add string to number /<br><br>"Done" is not a number |
