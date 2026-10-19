---
note_id: "rn_9htS8wbZ7vbrdjNQ"
title: "Low-Level Programming"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/20-further-programming-/programming-paradigms/low-level-programming
path: 20-further-programming-/programming-paradigms/low-level-programming
updated_at: "2025-05-20T13:45:51.343Z"
spec_point_ids: ["spcpt_cR74VjzBDrfcj7VR"]
spec_point_codes: []
guided_study: false
---

# Low-Level Programming

## Low-level programming

> **Spec point** — `spcpt_cR74VjzBDrfcj7VR`

## Low-level programming

### How do I write low-level code using addressing modes?

- Machine code and assembly language are examples of low-level languages and were introduced in [section 4 - Assembly Language Basics](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/4-processor-fundamentals-/assembly-language-/assembly-language-basics/)
- Before continuing, make sure you understand the different [addressing modes](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/4-processor-fundamentals-/assembly-language-/addressing-modes/)

## Immediate addressing

- **Syntax**: `LOAD #value`
- **Meaning**: Load a constant value directly into the accumulator

- Use when you want to work with **literal values**, not data in memory

## Direct addressing

- **Syntax**: `LOAD address`
- **Meaning**: Load the value stored **at** the specified memory address

- Use when the data is stored at **known memory addresses**

## Indirect addressing

- **Syntax**: `LOAD @address`
- **Meaning**: The address given **points to another address**, where the data is stored

- Example:

  - Memory[150] = 300
  - Memory[300] = 42
  - `LOAD @150` loads 42 into the accumulator.
- Use when data is stored in **dynamically referenced locations**

## Indexed addressing

- **Syntax**: `LOAD base[X]`
- **Meaning**: Load from **base address + index register** (e.g. `X`)

- Assume:

  - `X = 2`
  - This will access address 502 and 503
- Use for working with **arrays or tables**, where the index changes

## Relative addressing

- **Syntax**: `BRANCH offset`
- **Meaning**: Jump to a new instruction **relative** to the current instruction

- Used in control flow:

- Use for **loops and conditional branches** without needing absolute addresses
