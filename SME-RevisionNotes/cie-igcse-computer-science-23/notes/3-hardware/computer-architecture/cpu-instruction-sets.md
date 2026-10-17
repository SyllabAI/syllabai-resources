---
note_id: "rn_mYKc6qQTPxTCQ8t7"
title: "CPU Instruction Sets"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/3-hardware/computer-architecture/cpu-instruction-sets
path: 3-hardware/computer-architecture/cpu-instruction-sets
updated_at: "2026-01-05T13:05:10.616Z"
spec_point_ids: ["spcpt_CFyzx6dZ8HqXdGfY"]
spec_point_codes: []
guided_study: false
---

# CPU Instruction Sets

## CPU Instruction Sets

> **Spec point** — `spcpt_CFyzx6dZ8HqXdGfY` · "4 Understand the purpose and use of an instruction
set for a CPU"

## CPU Instruction Sets

### What is an Instruction set?

- An instruction set is a list of **all the commands** that can be **processed by a CPU**
- Each command has a **binary code** which is called **machine code**
- The table below shows an example instruction set
- Each instruction has a **mnemonic** that indicates **what the instruction does** alongside an example binary code
- After an instruction is decoded, the CPU** matches it to an instruction** in its instruction set
- It then knows what operation to perform when executing the instruction

| Instruction | Mnemonic | Binary code | Command |
|---|---|---|---|
| **Add** | ADD | *10100001* | **Adds **a value to the value currently stored in the accumulator (ACC) |
| **Subtract** | SUB | *00100010* | **Subtract **a value from the values stored in the accumulator |
| **Load** | LDA | *10111111* | **Load **the value stored in a memory location into the accumulator |
| **Store** | STA | *01100000* | **Store **the value in the accumulator in a specific location in memory |
| **Stop** | HLT | *00000000* | **Stop **the program |

- Instruction lists are **machine-specific**

  - A program created using one computer’s instruction set would not run on a computer containing a processor made by a different manufacturer
  - For example, a computer program created using Intel’s instruction set would not run on a device containing an ARM processor

> **Worked Example**
> Using the instruction set in the table above, what operation would be performed if the instruction was *00100010 00000010*?
> 
> **[1]**
> 
> **Answer**
> 
> Either of:
> 
> - **The operation would be ****SUB**** ****[1]**
> - **This instruction subtracts a value from the value stored in the accumulator ****[1]**
