---
note_id: "rn_Pd4hTqcPWRZVBnMq"
title: "Processor Features"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/15-hardware-and-virtual-machines-/processors-parallel-processing-and-virtual-machines/processor-features
path: 15-hardware-and-virtual-machines-/processors-parallel-processing-and-virtual-machines/processor-features
updated_at: "2025-06-04T08:24:46.577Z"
spec_point_ids: ["spcpt_wrYpPwbDRqWRBC2B"]
spec_point_codes: []
guided_study: false
---

# Processor Features

## Pipelining

> **Spec point** — `spcpt_wrYpPwbDRqWRBC2B`

## Pipelining

### What is pipelining?

- Pipelining is the process of carrying out multiple instructions ***concurrently***
- Each instruction will be at a different stage of the **fetch-decode-execute cycle**
- One instruction can be **fetched** while the previous one is being **decoded** and the one before is being **executed**
- In the case of a ***branch***, the pipeline is flushed
- This table shows which stage each instruction is at during each step:

| ** ** | **Fetch** | **Decode** | **Execute** |
|---|---|---|---|
| Step 1 | Instruction A |   |   |
| Step 2 | Instruction B | Instruction A |   |
| Step 3 | Instruction C | Instruction B | Instruction A |
| Step 4 | Instruction D | Instruction C | Instruction B |

- While one instruction is being executed, the next instruction will be decoded and the following instruction will be fetched

#### Pipelining in RISC processors

- RISC (Reduced Instruction Set Computer) processors are **designed for pipelining efficiency**
- Key features that support pipelining:

  - **Each instruction takes one clock cycle** (or close to it)
  - **Fixed-length instructions**, making decoding easier
  - **Limited instruction set**, reducing complexity and stage duration
  - **A large number of general-purpose registers**, reducing memory access

#### Role of registers in RISC pipelining

- Registers are **fast, temporary storage** inside the CPU
- RISC processors rely heavily on **registers for operand storage** rather than accessing RAM
- Intermediate values are stored in registers between stages
- Register usage reduces **memory bottlenecks**, allowing pipelining to run smoothly
- **Example:**

  - Instruction A loads value into **Register R1**
  - Instruction B adds **R1 + R2** and stores result in **R3**
  - All of these can be done efficiently **within the CPU** using registers

#### Benefits of pipelining

| **Advantage** | **Explanation** |
|---|---|
| **Increased throughput** | Multiple instructions handled at once |
| **Better use of CPU components** | Fetch, decode, and execute units are all in use simultaneously |
| **Reduced idle time** | No waiting between stages |
| **Faster execution of instruction stream** | Even if individual instructions don’t run faster |

> **Worked Example**
> Describe the process of pipelining during the fetch-execute cycle in RISC processors.**[4]**
> 
> **Final answer:** **Answer**
> 
> - Instructions are divided into subtasks / 5 stages **[1 mark]**
> - … Instruction fetch / IF, Instruction decode / ID, operand fetch / OF, opcode/instruction execute IE, result store / write back result / WB **[1 mark]**
> - Each subtask is completed during one clock cycle **[1 mark]**
> - No two instructions can execute their same stage at the same clock cycle **[1 mark]**
> - The second instruction begins in the second clock cycle, while the first instruction has moved on to its second subtask **[1 mark]**
> - The third instruction begins in the third clock cycle while the first and second instructions move on to their second and third subtasks, respectively, etc. **[1 mark]**
