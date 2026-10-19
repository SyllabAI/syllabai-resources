---
note_id: "rn_y4MH9kkV7GtpW7SR"
title: "Processor Types"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/15-hardware-and-virtual-machines-/processors-parallel-processing-and-virtual-machines/processor-types
path: 15-hardware-and-virtual-machines-/processors-parallel-processing-and-virtual-machines/processor-types
updated_at: "2025-12-01T09:29:11.206Z"
spec_point_ids: ["spcpt_ZbWSzmYtMGRXPsSW", "spcpt_xQNZWgjMdJQxThH4"]
spec_point_codes: []
guided_study: false
---

# Processor Types

## RISC & CISC

> **Spec point** — `spcpt_ZbWSzmYtMGRXPsSW`

## RISC & CISC

- A computer processor will have an ***instruction set*** that it can use to execute programs
- This will **vary from one processor to the next**
- There are **2 types of processors**:

  - Reduced Instruction Set Computer (**RISC**)
  - Complex Instruction Set Computer (**CISC**)

### RISC

- **Reduced Instruction Set Computer** **(RISC)** consists of a **smaller instruction set **with more simple instructions
- Each instruction takes **one clock cycle to execute **which makes it more **suitable for pipelining**
- A RISC program** may require more instructions** because each instruction performs a simpler operation
- Has **fewer addressing modes**
- Is usually used in **smartphones and tablets**

### CISC

- **Complex Instruction Set Computer (CISC)** consists of a **larger instruction set **which includes more complex instructions
- As the instructions are more complex, they can **take more than one clock cycle to execute**
- Has** fewer general-purpose registers**
- Instructions take up **less space in memory**
- Is usually used in **laptops and desktop** computers

#### What’s the difference between RISC & CISC?

| **Feature** | **RISC** | **CISC** |
|---|---|---|
| **Instruction set size** | Small | Large |
| **Instruction complexity** | Simple | Complex |
| **Clock cycles per instruction** | One | Multiple |
| **Pipelining suitability** | Well suited | Less suited |
| **Compiler complexity** | More complex | Less complex |
| **Addressing modes** | Fewer | More |
| **General-purpose registers** | More | Fewer |
| **Power usage** | Lower | Higher |
| **Cost** | Lower | Higher |
| **Memory use** | More (due to more instructions) | Less (fewer instructions) |
| **Typical devices** | Smartphones, tablets | Laptops, desktops |

- A program that has been **written for a RISC **processor **won’t work on a CISC** processor and vice versa
- A program that has been **written for a RISC **processor **won’t necessarily work on another RISC** processor as they may have different instruction sets

## Interrupt handling on RISC & CISC

> **Spec point** — `spcpt_xQNZWgjMdJQxThH4`

## Interrupt handling on RISC & CISC

- The concept of interrupt handling is covered in [section 4, interrupts](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/4-processor-fundamentals-/central-processing-unit-cpu-architecture/interrupts/)

| **Feature** | **CISC** | **RISC** |
|---|---|---|
| **Instruction complexity** | CISC has **complex instructions**, often with built-in support for interrupt routines | RISC has **simple, fixed-length instructions**, interrupt handling done using simpler routines |
| **Interrupt handling** | Often uses **microcode and dedicated hardware instructions** to manage interrupts efficiently | Uses **software-based interrupt handlers**, managed through general-purpose registers and simple instructions |
| **Context switching** | May have **hardware support** to save and restore processor state automatically | Typically handled in **software**, giving more control but requiring more instructions |
| **Speed of response** | Generally **faster interrupt handling** due to built-in support | **Slower**, but more flexible and consistent across all instructions |
| **Instruction cycle impact** | CISC can handle **multiple tasks in a single instruction**, including context saving | RISC uses **multiple simple instructions**, giving the OS greater control |

- **CISC processors** often have **dedicated instructions** for handling interrupts, making the process more efficient but less flexible
- **RISC processors** rely more on **software routines**, making interrupt handling **slightly slower**, but simpler and more predictable
- Both architectures aim to **respond to interrupts quickly and resume execution** correctly, but they do so using different design philosophies

> **Worked Example**
> Reduced Instruction Set Computers (RISC) and Complex Instruction Set Computers (CISC) are two types of processor.
> 
> Tick (3) one box in each row to show if the statement applies to RISC or CISC processors.**[2]**
> 
> | Statement | RISC | CISC |
> |---|---|---|
> | uses a smaller instruction set |   |   |
> | uses single-cycle instructions and limited addressing modes |   |   |
> | uses fewer general-purpose registers |   |   |
> | uses both hardwired and micro-coded control unit |   |   |
> | uses a system where cache is split between data and<br><br>instructions |   |   |
> 
> **Final answer:** **Answer**
> 
> | Statement | RISC | CISC |
> |---|---|---|
> | uses a smaller instruction set | **✓** |   |
> | uses single-cycle instructions and limited addressing modes | **✓** |   |
> | uses fewer general-purpose registers |   | **✓** |
> | uses both hardwired and micro-coded control unit |   | **✓** |
> | uses a system where cache is split between data and<br><br>instructions | **✓** |   |
