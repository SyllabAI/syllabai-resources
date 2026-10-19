---
note_id: "rn_wSWQ5Mp2HBSwb9tZ"
title: "Instruction Groups"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/4-processor-fundamentals-/assembly-language-/instruction-groups
path: 4-processor-fundamentals-/assembly-language-/instruction-groups
updated_at: "2025-04-08T10:54:54.088Z"
spec_point_ids: ["spcpt_Yr56xgwmtZfJRwFS"]
spec_point_codes: []
guided_study: false
---

# Instruction Groups

## Categories of instructions

> **Spec point** — `spcpt_Yr56xgwmtZfJRwFS`

## Categories of instructions

### What are the categories of instructions?

- Assembly language instructions can be grouped into:

  - **Data movement**
  - **Input and output of data**
  - **Arithmetic operations**
  - **Unconditional and conditional instructions**
  - **Compare instructions**
- For each category, a table containing the instruction (Opcode and Operand), and an explanation is given

| **Category** | **Opcode** | **Operand** | **Explanation** |
|---|---|---|---|
| **Data Movement** | `LOAD` | `A` | Loads the value stored at memory location `A` into the accumulator. |
|   | `STORE` | `B` | Stores the value from the accumulator into memory location `B`. |
|   | `MOV` | `A, B` | Copies the value from register/memory `A` to register/memory `B`. |
|   | `CLEAR` | `ACC` | Clears the accumulator (sets it to 0). |
|   | `DATA` | `5` | Declares a constant or data value (e.g. `DATA 5` stores the value 5). |
| **Input and Output of Data** | `IN` |   | Takes input from a user or input device and stores it in the accumulator. |
|   | `OUT` |   | Outputs the value in the accumulator to a screen or output device. |
| **Arithmetic Operations** | `ADD` | `A` | Adds the value at memory location `A` to the accumulator. |
|   | `SUB` | `B` | Subtracts the value at memory location `B` from the accumulator. |
|   | `INC` |   | Increments the accumulator by 1. |
|   | `DEC` |   | Decrements the accumulator by 1. |
| **Unconditional and Conditional** | `JMP` | `LABEL` | Unconditionally jumps to the instruction at `LABEL`. |
|   | `JZ` | `LABEL` | Jumps to `LABEL` if the accumulator is zero. |
|   | `JNZ` | `LABEL` | Jumps to `LABEL` if the accumulator is **not** zero. |
|   | `JC` | `LABEL` | Jumps to `LABEL` if the carry flag is set. |
|   | `HLT` |   | Stops the program (halts execution). |
| **Compare Instructions** | `CMP` | `A` | Compares the accumulator with the value at memory location `A`. |
|   | `TEST` | `A` | Performs a logical AND between accumulator and `A`; sets flags, no output. |
