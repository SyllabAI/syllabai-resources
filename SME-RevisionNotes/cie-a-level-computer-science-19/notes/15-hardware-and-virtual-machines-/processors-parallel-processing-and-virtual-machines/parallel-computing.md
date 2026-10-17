---
note_id: "rn_4RtSYGdqyfK5WKDg"
title: "Parallel Computing"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/15-hardware-and-virtual-machines-/processors-parallel-processing-and-virtual-machines/parallel-computing
path: 15-hardware-and-virtual-machines-/processors-parallel-processing-and-virtual-machines/parallel-computing
updated_at: "2025-05-14T10:53:17.079Z"
spec_point_ids: ["spcpt_fC5Mj8ZrPJNw6zYP"]
spec_point_codes: []
guided_study: false
---

# Parallel Computing

## Massively parallel systems

> **Spec point** — `spcpt_fC5Mj8ZrPJNw6zYP`

## Massively parallel systems

### What are massively parallel computers?

- Massively parallel computers are systems made up of **thousands of processors** working **simultaneously** to solve a single large problem
- Each processor **executes part of a program**, and **results are combined** to produce the final output
- They are designed to tackle **complex, large-scale tasks** in fields like

  - **Scientific research**
  - **Weather simulation**
  - **Cryptography**
  - **AI**

#### Key characteristics

| **Feature** | **Description** |
|---|---|
| **Thousands of processors** | Many processors are connected and work together to execute different parts of the same task |
| **Shared or distributed memory** | Each processor may have its own memory or access shared memory resources |
| **High-speed interconnects** | Processors are linked via **fast communication pathways** to share results |
| **Data parallelism** | Many data items can be processed at once — often using **SIMD** or **MIMD** |
| **Task parallelism** | Different processors may perform **different tasks** on **different data sets** |
| **Specialised software** | Requires software written to **distribute the work efficiently** across processors |
| **Tightly coupled** | Processors **depend on one another** and work collaboratively as a single system |

#### Massively parallel vs cluster computers

| **Massively parallel computers** | **Cluster computers** |
|---|---|
| Thousands of processors form a **single tightly integrated system** | Multiple independent systems networked together |
| Processors **communicate continuously** via shared architecture | Communication occurs via network, often loosely coupled |
| Acts like **one machine** with distributed processing | A group of **co-operating systems** (can be SIMD-based) |
| Higher performance, used for **supercomputing tasks** | More general-purpose or batch processing systems |

### Link to computer architectures

- Massively parallel systems often use:

  - **SIMD**: Apply one instruction to many data points simultaneously
  - **MIMD**: Run different instructions on different data, fully independently
