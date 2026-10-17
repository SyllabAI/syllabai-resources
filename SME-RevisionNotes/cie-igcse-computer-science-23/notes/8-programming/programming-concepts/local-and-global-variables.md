---
note_id: "rn_Y9GWSTcpqNqWMJYS"
title: "Local & Global Variables"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/8-programming/programming-concepts/local-and-global-variables
path: 8-programming/programming-concepts/local-and-global-variables
updated_at: "2026-05-28T07:45:06.421Z"
spec_point_ids: ["spcpt_FDkyKHbB9TtqvxWH", "spcpt_QVqq7ynJBbPrkfQT"]
spec_point_codes: []
guided_study: true
---

# Local & Global Variables

## Local Variables

> **Spec point** — `spcpt_FDkyKHbB9TtqvxWH` · (c) Understand and use local and global variables

## Local Variables

### What is a local variable?

- A local variable is **a variable declared within a specific scope**, such as a function or a code block
- Local variables are accessible **only within the block in which they are defined**, and their lifetime is limited to that particular block
- Once the execution of the block ends, **the local variable is destroyed**, and its memory is released

#### Examples

- In this code, you can see that the` localVariable` (with the value 10) is declared **inside** of the function `printValue`
- This means that **only **this function can access and change the value in the local variable
- It **cannot be accessed** by other modules in the program

| **Psuedocode** |
|---|
|   |

| **Python** |
|---|
|   |

## Global Variables

> **Spec point** — `spcpt_QVqq7ynJBbPrkfQT` · (c) Understand and use local and global variables

## Global Variables

### What is a global variable?

- A global variable is **a variable declared at the outermost level of a program**.
- They are declared **outside any modules** such as functions or procedures
- Global variables have a **global scope**, which means they can be **accessed and modified** from **any part of the program**

#### Examples

- In this code, you can see that the` globalVariable` (with the value 10) is declared **outside** of the function `printValue`
- This means that this function and **any other modules **can access and change the value in the global variable

| **Psuedocode** |
|---|
|   |

| **Python** |
|---|
|   |
