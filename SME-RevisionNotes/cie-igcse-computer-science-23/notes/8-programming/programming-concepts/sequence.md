---
note_id: "rn_WW44KmG5sRbNDDK9"
title: "Sequence"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/8-programming/programming-concepts/sequence
path: 8-programming/programming-concepts/sequence
updated_at: "2025-09-24T13:16:24.315Z"
spec_point_ids: ["spcpt_KcCh8pWNfC8QQsRF"]
spec_point_codes: []
guided_study: true
---

# Sequence

## Sequence

> **Spec point** — `spcpt_KcCh8pWNfC8QQsRF` · 4 (a) Understand and use the concept of sequence

## Sequence

### What is sequence?

- Sequence refers to lines of code which are run **one line at a time**
- The lines of code are run in the **order** that they written from the first line of code to the last line of code
- Sequence is **crucial to the flow** of a program, any instructions out of sequence can lead to **unexpected behaviour or errors**

#### Example 1

- A simple program to ask a user to input two numbers, number two is subtracted from number one and the result is outputted

| **Line** | **Pseudocode** |
|---|---|
| **01** | `OUTPUT "Enter the first number"` |
| **02** | `INPUT Num1` |
| **03** | `OUTPUT "Enter the second number"` |
| **04** | `INPUT Num2` |
| **05** | `Result ← Num1 - Num2` |
| **06** | `OUTPUT Result` |

- A simple swap of line 01 and line 02 would lead to an unexpected behaviour, the user would be prompted to input information without knowing what they should enter

#### Example 2

- This function calculates the area of a rectangle
- **Inputs**:

  - length: The length of the rectangle
  - width: The width of the rectangle
- **Returns**:

  - The area of the rectangle

| Pseudocode |
|---|
|   |
| **Python example** |
|   |

- In the example, the** sequence of instructions** is wrong and would cause a runtime error
- In the `calculate_area()` function a value is **returned before it is assigned **
- The correct sequence is:

`area ← length * width`
`RETURN area`

`OR`

`area = length * width`
`return area`
