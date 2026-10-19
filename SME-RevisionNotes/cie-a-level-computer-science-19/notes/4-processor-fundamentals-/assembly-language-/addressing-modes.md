---
note_id: "rn_zh9Mc6r3mhmhW69g"
title: "Addressing Modes"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/4-processor-fundamentals-/assembly-language-/addressing-modes
path: 4-processor-fundamentals-/assembly-language-/addressing-modes
updated_at: "2025-04-08T11:01:26.428Z"
spec_point_ids: ["spcpt_9s6ft5c2ryVvfNMH"]
spec_point_codes: []
guided_study: false
---

# Addressing Modes

## Addressing methods

> **Spec point** — `spcpt_9s6ft5c2ryVvfNMH`

## Addressing methods

### What is an addressing method?

- An addressing method is a way in which **an instruction in assembly language or machine code** can **access data stored in memory**
- There are five main addressing methods:

  - **Immediate**
  - **Direct**
  - **Indirect**
  - **Indexed**
  - **Relative**

| **Addressing mode** | **Description** | **Example instruction** | **Explanation** |
|---|---|---|---|
| **Immediate** | The **operand is a constant value** included directly in the instruction | `MOV AX, 1234h` | Moves the **immediate value** `1234h` into the `AX` register |
| **Direct** | The **exact memory address** of the operand is given in the instruction | `MOV AX, [1234h]` | Moves the value **stored at memory location** `1234h` into the `AX` register |
| **Indirect** | A **register contains the memory address** of the operand | `MOV AX, [BX]` | If `BX = 2000h`, this moves the value **at memory location **`2000h` into `AX` |
| **Indexed** | Uses a **base register and an index** to calculate the memory address | `MOV AX, [BX + SI]` | If `BX = 0050h` and `SI = 1000h`, this moves the value **at **`1050h` into the `AX` register |
| **Relative** | The operand is an **offset** relative to the **current instruction address** | `JMP +5` | Tells the program to **jump forward 5 instructions** from the current line<br><br>Used in branching |
