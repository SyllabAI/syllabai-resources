---
note_id: "rn_V5jBKWtnYDK6kdbm"
title: "Assembly process"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/4-processor-fundamentals-/assembly-language-/assembly-process-
path: 4-processor-fundamentals-/assembly-language-/assembly-process-
updated_at: "2025-04-23T13:22:26.093Z"
spec_point_ids: ["spcpt_znNKGg967WWw9MNQ", "spcpt_Sw7xjscGJpcy44GB"]
spec_point_codes: []
guided_study: false
---

# Assembly process

## Two-pass assembler

> **Spec point** — `spcpt_znNKGg967WWw9MNQ`

## Two-pass assembler

### What is a two-pass assembler?

- A two-pass assembler **translates assembly language into machine code** in two stages
- It produces an **object program** that can be **stored**, **loaded**, and **run later**
- To execute this program, another utility called a **loader** is needed
- The assembler scans the source code **twice**:

  - In the **first pass**, it identifies all **labels** and records their memory addresses
  - In the **second pass**, it replaces those labels with the correct **memory addresses** in the machine code
- This **ensures the final machine code is accurate** and ready to be executed

#### Example

- The following program loads the value of `A` (5), adds the value of `B` (3), stores the result (8) in `C`, then halts:

- **Pass 1:**

  - The assembler reads each line and assigns memory addresses to labels (e.g. A, B, C), but **does not translate the instructions yet**

| Address | Instruction | Label | Add to symbol table |
|---|---|---|---|
| `00` | LOAD A |   |   |
| `01` | ADD B |   |   |
| `02` | STORE C |   |   |
| `03` | HALT |   |   |
| `04` | DATA 5 | `A` | **A** = `04` |
| `05` | DATA 3 | `B` | **B **= `05` |
| `06` | DATA 0 | `C` | **C **= `06` |

**Symbol table created:**

| Label | Address |
|---|---|
| A | `04` |
| B | `05` |
| C | `06` |

- **Pass 2:**

  - The assembler replaces labels with their corresponding memory addresses and outputs machine code
  - In this example we assume the following opcodes for simplicity:

| Mnemonic | Opcode |
|---|---|
| LOAD | 01 |
| ADD | 02 |
| STORE | 03 |
| HALT | 00 |
| DATA | - |

- Now generate the object (machine) code:

| Address | Assembly | Machine code | Explanation |
|---|---|---|---|
| `00` | LOAD A | `01 04` | LOAD from address 04 |
| `01` | ADD B | `02 05` | ADD value at address 05 |
| `02` | STORE C | `03 06` | STORE into address 06 |
| `03` | HALT | `00 00` | Stop program |
| `04` | DATA 5 | `00 05` | Data value 5 |
| `05` | DATA 3 | `00 03` | Data value 3 |
| `06` | DATA 0 | `00 00` | Data value 0 (placeholder) |

**Final object program:**

## Program tracing

> **Spec point** — `spcpt_Sw7xjscGJpcy44GB`

## Program tracing

### What is a trace table?

- A **trace table** is a table used to **manually track the values of variables** as a program runs
- It helps to follow the flow of a program **line by line**, checking whether the logic works as expected
- Trace tables are used to:

  - **Understand how a program works**
  - **Debug errors** in the logic
  - **Predict outputs** before running the program
  - **Check variable values** at each step

#### Example

- An assembly program that loads the value from `A` (4) into the accumulator, adds the value from `B` (2), stores the result (6) into `C`, and halts

- To trace the program, assumptions must be made:

  - **Accumulator (ACC)**: Used for calculations
  - Memory is addressed from 00 onwards
  - Simple instructions:
  
    - `LOAD X` → ACC = memory[X]
    - `ADD X` → ACC = ACC + memory[X]
    - `STORE X` → memory[X] = ACC
    - `HALT` → Stop

**Trace table**

| Step | Instruction | ACC (Accumulator) | Memory[A] | Memory[B] | Memory[C] |
|---|---|---|---|---|---|
| 0 | (Start) | 0 | 4 | 2 | 0 |
| 1 | LOAD A | 4 | 4 | 2 | 0 |
| 2 | ADD B | 6 | 4 | 2 | 0 |
| 3 | STORE C | 6 | 4 | 2 | 6 |
| 4 | HALT | 6 | 4 | 2 | 6 |

**Final outcome:**

- **ACC = 6**
- **C = 6**
- The program has successfully added A and B, then stored the result in C
