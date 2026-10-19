---
note_id: "rn_hF2VSWbJDZtND5MS"
title: "Iteration"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/11-programming-/constructs/iteration
path: 11-programming-/constructs/iteration
updated_at: "2025-05-06T12:17:16.854Z"
spec_point_ids: ["spcpt_YFT6RKY5hvgMzdtv", "spcpt_p6gdsGKbBwW2jTbr"]
spec_point_codes: []
guided_study: false
---

# Iteration

## What is iteration?

- Iteration is **repeating a line or a block of code **using a loop
- Iteration can be:

  - **Count-controlled**
  - **Condition-controlled**

## Count-controlled loops

> **Spec point** — `spcpt_YFT6RKY5hvgMzdtv`

## Count-controlled loops

### What is a count-controlled loop?

- A count-controlled loop is when the code is repeated **a fixed number of times** (e.g. using a FOR loop)
- A count-controlled loop can be written as:

| Pseudocode |   |
|---|---|
|   |   |

- In a **FOR loop**, the **increment** must be an **expression that evaluates to an integer**

  - The loop **starts** at `value1`
  - The identifier is updated by the **increment** value on each iteration
  - The loop continues until the identifier **passes value2**
- The increment can be **positive** or **negative**, depending on the direction you want the loop to count

#### Nested count-controlled loops

- The **outer loop** runs `i` from 1 to 3
- For **each value of **`i`, the **inner loop** runs `j` from 1 to 3
- It outputs all combinations of `i × j`

### Count-controlled loops in different languages

| Python | VB.net | Java |
|---|---|---|
| Print the numbers 1 to 5 |   |   |
|   |   |   |

## Condition-controlled loops

> **Spec point** — `spcpt_p6gdsGKbBwW2jTbr`

## Condition-controlled loops

### What is a condition controlled loop?

- A condition controlled loop is when the code is repeated **until a condition is met**
- There are two types of condition controlled loops:

  - **Post-condition (REPEAT)**
  - **Pre-condition (WHILE)**

#### Post-condition loops (REPEAT)

- A post-condition loop** is executed at least once**
- The condition must be an **expression **that evaluates to a **Boolean **(True/False)
- The condition is tested** after the statements are executed** and only stops once the condition is evaluated to True
- It can be written as:

| Pseudocode |
|---|
|   |

#### Pre-condition loops (WHILE)

- The condition must be an **expression **that evaluates to a **Boolean **(True/False)
- The condition is tested and statements are **only executed if the condition evaluates to True**
- After statements have been executed the condition is **tested again**
- The loop ends when the condition **evaluates to False**
- It can be written as:

| Pseudocode |
|---|
|   |

#### Nested condition-controlled loops

- Ask the user to **enter up to 3 usernames**
- For each one, keep asking **until a non-empty name** is entered
- **Outer WHILE** runs 3 times (for 3 usernames)
- **Inner WHILE** ensures that each username is **not blank**

### Condition-controlled loops in different languages

| Python | VB.net | Java |
|---|---|---|
| Keep asking the user to enter a password until they type `"admin"` |   |   |
|   |   |   |

## When to use each type of loop

| **Loop type** | **When to use** | **Example scenario** |
|---|---|---|
| **Count-controlled loop** (`FOR`) | When you know **in advance** how many times you want the loop to run | Repeating an action 5 times, generating a multiplication table |
| **Pre-condition loop** (`WHILE`) | When you want to **check a condition before** running the loop. It may run **0 or more** times | Keep asking for a valid password before granting access |
| **Post-condition loop** (`REPEAT ... UNTIL`) | When you want the loop to run **at least once**, and then stop when a condition becomes true | Ask the user for input and validate it after first run |
