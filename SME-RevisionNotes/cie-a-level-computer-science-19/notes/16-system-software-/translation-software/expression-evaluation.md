---
note_id: "rn_ZWXcPSbh8YQbNs7r"
title: "Expression Evaluation"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/16-system-software-/translation-software/expression-evaluation
path: 16-system-software-/translation-software/expression-evaluation
updated_at: "2025-05-23T11:23:16.072Z"
spec_point_ids: ["spcpt_52qhP4gsvByRBtJB"]
spec_point_codes: []
guided_study: false
---

# Expression Evaluation

## Reverse Polish Notation (RPN)

> **Spec point** — `spcpt_52qhP4gsvByRBtJB`

## Reverse Polish Notation (RPN)

### What is RPN?

- Reverse Polish Notation (RPN) is a method of writing **mathematical expressions** where the **operator comes after the operands**
- This is also known as **postfix notation**

  - *Infix*: `3 + 4`
  - RPN: `3 4 +`

#### Why use RPN?

- **No need for brackets**: The order of operations is determined by position, not parentheses
- **Easier for computers to evaluate** using a **stack**
- Always **unambiguous**

#### How RPN works

- RPN uses a [stack](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/10-data-types-and-structures-/introduction-to-abstract-data-types-adt/adt-overview/) to evaluate expressions

1. **Read from left to right**
2. **Push numbers onto the stack**
3. When an **operator** is read:

  - **Pop the top two values** from the stack
  - **Apply the operator**
  - **Push the result** back onto the stack
4. When the expression ends, the final result is at the **top of the stack**

#### Example: evaluate 3 4 + 2 ×

| Step | Action | Stack |
|---|---|---|
| Read `3` | Push to stack | `3` |
| Read `4` | Push to stack | `3 4` |
| Read `+` | Add 3 + 4 → 7 | `7` |
| Read `2` | Push to stack | `7 2` |
| Read `×` | Multiply 7 × 2 → 14 | `14` |

- Final result: `14`

#### Example: convert this infix expression to RPN

- **Split the expression into parts:**
- Left-hand side:

`(7 − 2 + 8)`

- This becomes:

`( (7 − 2) + 8 )`

- Which in RPN is:

`7 2 − 8 +`

- Right-hand side:

`(9 − 5)`

- In RPN:

`9 5 −`

- **Combine with the division**
- In RPN, that becomes:

`7 2 − 8 + 9 5 − ÷`

> **Exam Hint**
> RPN **follows the evaluation order naturally**, so there’s **no need for brackets** or precedence rules. Just:
> 
> - Work from inside brackets out
> - Convert each sub-expression
> - Add the operator after its operands

### Summary

| **Concept** | **Description** |
|---|---|
| RPN (Postfix) | Operators follow operands |
| Stack | Used to store and evaluate values |
| Evaluation method | Push numbers, pop and evaluate on operator |
| Benefits | No brackets, no ambiguity, easy to compute with stack |
