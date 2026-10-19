---
note_id: "rn_mr8Zz9FRbsBsSH55"
title: "Exception Handling"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/20-further-programming-/file-processing-and-exception-handling/exception-handling
path: 20-further-programming-/file-processing-and-exception-handling/exception-handling
updated_at: "2025-05-21T11:32:31.114Z"
spec_point_ids: ["spcpt_fSKbbshqWdC8Mnnz"]
spec_point_codes: []
guided_study: false
---

# Exception Handling

## Exception handling

> **Spec point** — `spcpt_fSKbbshqWdC8Mnnz`

## Exception handling

### What is exception handling?

- An exception is an **unexpected event** that disrupts normal program execution
- Exception handling is **how a program detects and responds to these errors**, allowing it to **recover **or **shut down cleanly**

#### Why use exception handling?

- Prevents programs from **crashing unexpectedly**
- Allows for** user-friendly error messages**
- Makes programs more **robust** and **reliable**
- Handles problems caused by:

  - Division by zero
  - File not found or end-of-file errors
  - Hardware or device failures (e.g. printers, lost connections)
  - Invalid input from users

#### Causes of exceptions

| **Cause** | **Example** |
|---|---|
| Programming errors | Uninitialised variables, logic errors |
| User errors | Entering text instead of a number |
| Hardware failure | Lost connection to printer, disk error |

### Pseudocode

#### Key terms

| **Keyword** | **Purpose** |
|---|---|
| `TRY` | Starts a block of code that may raise an error |
| `EXCEPT` | Executes if an error occurs in the `TRY` block |
| `ENDTRY` | Marks the end of the exception handling structure |

### Python

### Java
