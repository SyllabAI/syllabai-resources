---
note_id: "rn_4YCPw5grTQQp6GcJ"
title: "String Handling"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/8-programming/programming-concepts/string-handling
path: 8-programming/programming-concepts/string-handling
updated_at: "2026-01-26T10:48:32.513Z"
spec_point_ids: ["spcpt_X4k5ZCwB6PZxYWJV"]
spec_point_codes: []
guided_study: true
---

# String Handling

## String Handling

> **Spec point** — `spcpt_X4k5ZCwB6PZxYWJV` · "e) Understand and use the concept of string
handling "

## String Handling

### What is string manipulation?

- String manipulation is the use of** programming techniques** to **modify**, **analyse **or **extract **information **from a string**
- Examples of string manipulation include:

  - **Case conversion **(modify)
  - **Length **(analyse)
  - **Substrings **(extract)

#### Case conversion

- The ability to **change a string from one case to another**, for example, lower case to upper case

| **Function** | Pseudocode | **Python** | **Output** |
|---|---|---|---|
| **Uppercase** |   |   | `"SARAH"` |
| **Lowercase** |   |   | `"sarah"` |

#### Length

- The ability to **count the number of characters in a string**, for example, checking a password meets the minimum requirement of 8 characters

| Pseudocode | **Python** | **Output** |
|---|---|---|
|   |   | `7` |
|   |   | `"Password too short"` |

#### Substring

- The ability to **extract a sequence of characters from a larger string **in order to be used by another function in the program, for example, data validation or combining it with other strings
- Extracting substrings is done by specifying a **start position** and **length **in pseudocode, or a **start **and **end **index in Python.
- Substring has a **start position of 1** in pseudocode and 0 in Python

| Pseudocode | **Python** | **Output** |
|---|---|---|
|   |   | `"Rev"` |
|   |   | `"vision"` |

> **Worked Example**
> The function Length(x) finds the length of a string x. The function substring(x,y,z) finds a substring of x starting at position y and z characters long. The first character in x is in position 1.
> 
> Write pseudocode statements to:
> 
> - Store the string “Save my exams” in x
> - Find the length of the string and output it
> - Extract the word exams from the string and output it
> 
> **[6]**
> 
> **Answer**
