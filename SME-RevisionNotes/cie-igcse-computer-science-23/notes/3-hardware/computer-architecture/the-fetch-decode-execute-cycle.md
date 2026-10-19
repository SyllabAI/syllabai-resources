---
note_id: "rn_FHFw7hjDSyNydjwV"
title: "The Fetch-Decode-Execute Cycle"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/3-hardware/computer-architecture/the-fetch-decode-execute-cycle
path: 3-hardware/computer-architecture/the-fetch-decode-execute-cycle
updated_at: "2025-11-28T06:09:32.548Z"
spec_point_ids: ["spcpt_dP3gX38Yj4BfDGC5"]
spec_point_codes: []
guided_study: false
---

# The Fetch-Decode-Execute Cycle

## Fetch-Decode-Execute Cycle (FDE)

> **Spec point** — `spcpt_dP3gX38Yj4BfDGC5` · "(b) Describe the process of the
fetch–decode–execute (FDE) cycle including
the role of each component in the process"

## Fetch-Decode-Execute Cycle (FDE)

### What is the purpose of the CPU?

- The purpose of the Central Processing Unit (CPU) is to **fetch**, **decode** and **execute** instructions
- The CPU is the brain of the computer and its job is to take an input, process data and produce an output

### What is the Fetch-Decode-Execute cycle?

- The **Fetch-Decode-Execute Cycle **is the cycle that the central processing unit (CPU) runs through billions of times per second to make a computer work
- A computer takes an input, processes the input and then delivers an output for the user

  - **Input:** Clicking a button on the gamepad
  - **Process: **The CPU inside the console follows a set of instructions to carry out the task
  - **Output:** The player moving on screen

![the-cpu](../../../assets/200bb8693d52-the-cpu.png)

### The Fetch-Decode-Execute cycle stages

#### Fetch stage

- During the fetch stage of the cycle, the **program counter** holds **the address of the next instruction** to be fetched from memory
- **The address of the next instruction or data** to be fetched is **copied into **the memory address register **(MAR)**
- The **address** of the instruction or data is then **sent along the address bus **and** awaits a signal **from the** control bus**
- The signal sent along the control bus is **sent from the control unit (CU) **to the main memory
- The data or instructions received from main memory is **fetched **to the memory data register** (MDR) **via the **data bus**
- A **copy of the instruction or data is stored** in the current instruction register **(CIR)**
- The program counter (PC)** increments by 1 **so it is pointing to the **next instruction to be executed**

#### Decode stage

- During the decode stage of the cycle, the CPU needs to** work out what is required from the instruction**
- This is done as the instruction is split into two parts:

  - Opcode - what the instruction is
  - Operand - what to do it to
  
    - This could be either data or an address where the data is stored

#### Execute stage

- During the execute stage of the cycle, the CPU will **carry out the instruction that was fetched**
- Some examples that would take place at this stage are

  - **Performing a calculation**
  - **Storing a result or data back in main memory (RAM)**
  - **Going to main memory to fetch data from a different location**

#### The important things to remember are:

- An instruction or data is fetched from memory
- The instruction is decoded
- The instruction is executed
- The cycle repeats billions of times per second

> **Exam Hint**
> Make sure you read the question carefully and look at the number of marks allocated to judge the level of detail required. Often questions on the fetch-decode-execute cycle only require you to describe the steps rather than explain how the registers and buses are used during each step

> **Worked Example**
> Explain how an instruction is fetched using Von Neumann architecture** **
> 
> **[6]**
> 
> **Answer**
> 
> - ** The Program Counter (PC) holds the  address/location of the next instruction to be fetched [1]**
> - **The address held in the PC is sent to the Memory Address Register (MAR) [1]**
> - **The memory address is sent using the address bus [1]**
> - **The Program Counter is incremented [1]**
> - **The instruction is sent from the address in memory to the Memory Data Register (MDR) [1]**
> - **The instruction is transferred using the data bus [1]**
> - **The instruction is sent to the Current Instruction Register (CIR) [1]**
