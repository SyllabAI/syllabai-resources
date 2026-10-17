---
note_id: "rn_PTfX6FGp27Tg33yz"
title: "Assembly Language"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/4-software/types-of-programming-language-translators-and-ides/assembly-language
path: 4-software/types-of-programming-language-translators-and-ides/assembly-language
updated_at: "2025-10-22T07:51:59.636Z"
spec_point_ids: ["spcpt_hNS5xJzVywwR4KdQ"]
spec_point_codes: []
guided_study: false
---

# Assembly Language

## Assembly Language

> **Spec point** — `spcpt_hNS5xJzVywwR4KdQ` · "2 Understand that assembly language is a form
of low-level language that uses mnemonics,
and that an assembler is needed to translate an
assembly language program into machine code"

## Assembly Language

### What is assembly language?

- Assembly language is a **second-generation**, **low-level language** designed to simplify the writing of machine code instructions for programmers
- Programmers use assembly language for the following reasons:

  - Need to make use of** specific hardware** or parts of the hardware
  - To complete **specific machine-dependent** instructions
  - To ensure that too much space** is not taken up in RAM**
  - To ensure code can be completed much **faster**
- Assembly languages allow programmers to program with **mnemonics, **e.g.

  - **LDA Load** - this will ensure a value is added to the accumulator
  - **ADD Addition** - this will add the value input or loaded from memory to the value in the accumulator
  - **STO Store** - stores the value in the accumulator in RAM

- Assembly language allowed continuation of working **directly with the hardware** but removed an element of **complexity**
- A **mnemonic** is received by the computer and it is looked up within a specific table
- An **assembler** is needed to check the word so that it can be converted into machine code
- If a **match from the word is found** (e.g. **STO**),** **the word is replaced with the relevant binary code to match that sequence

> **Worked Example**
> Complete the table to identify whether each example of computer code is** High-level**, **Assembly language** or **Machine code**
> 
> | Computer code | High-level | Assembly | Machine code |
> |---|---|---|---|
> | `10110111`<br><br>`00110110`<br><br>`11100110` |   |   |   |
> | `FOR X = 1 to 10`<br><br>`  PRINT x`<br><br>`NEXT X` |   |   |   |
> | `INP X`<br><br>`STA X`<br><br>`LDA Y` |   |   |   |
> 
> **[3]**
> 
> **Answer**
> 
> | Computer code | High-level | Assembly | Machine code |
> |---|---|---|---|
> | `10110111`<br><br>`00110110`<br><br>`11100110` |   |   | **X ****[1 mark]** |
> | `FOR X = 1 to 10`<br><br>`  PRINT x`<br><br>`NEXT X` | **X ****[1 mark]** |   |   |
> | `INP X`<br><br>`STA X`<br><br>`LDA Y` |   | **X ****[1 mark]** |   |
