---
note_id: "rn_DyQ99xJcdcV2DKXw"
title: "Computer Architectures"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/15-hardware-and-virtual-machines-/processors-parallel-processing-and-virtual-machines/computer-architectures
path: 15-hardware-and-virtual-machines-/processors-parallel-processing-and-virtual-machines/computer-architectures
updated_at: "2025-05-14T10:38:17.071Z"
spec_point_ids: ["spcpt_hn7PRVxWyP4SzNWt"]
spec_point_codes: []
guided_study: false
---

# Computer Architectures

## Architecture types

> **Spec point** — `spcpt_hn7PRVxWyP4SzNWt`

## Architecture types

### What is a computer architecture?

- A computer architecture is the design and structure of a computer system
- It describes how it **fetches, processes, and stores data and instructions**
- It defines how components like the CPU, memory, and input/output devices **work together to execute programs**
- Each architecture is categorised as:

  - **S**ingle or **M**ultiple **Instruction** stream
  - **S**ingle or **M**ultiple **Data** stream

### SISD – Single Instruction, Single Data

| **Description** | **Key Features** |
|---|---|
| One processor executes **one instruction** on **one data stream** at a time | Traditional serial (non-parallel) architecture |
| Used in **basic, single-core processors** | Step-by-step processing |

**Example**: Classic desktop CPU running one task at a time

![Diagram showing data flow: blue box labelled 'Data' connected by arrow to green 'Processor', leading to orange box labelled 'Instructions'.](../../../assets/35b74df1b24e-48364-1.png)

*Single Instruction, Single Data Diagram*

### SIMD – Single Instruction, Multiple Data

| **Description** | **Key Features** |
|---|---|
| One instruction is applied to **multiple pieces of data** at once | Useful for **parallel processing** |
| All processing units perform the **same operation** in parallel | Ideal for graphics or scientific computation |

**Example**: GPU operations, image processing

![Flowchart depicting data flowing from a blue "Data" block to three "Processor" blocks, and orange arrows to an "Instructions" block.](../../../assets/505c829ce8c5-18769-2.png)

*Single Instruction, Multiple Data Diagram*

### MISD – Multiple Instruction, Single Data

| **Description** | **Key Features** |
|---|---|
| Multiple processors execute **different instructions** on the **same data** | Very uncommon in practice |
| Used in specialised systems for **fault tolerance** | Each unit checks the same input differently |

**Example**: Redundant systems in safety-critical environments

![Diagram with a blue "Data" box connected to four green "Processor" boxes, which in turn connect to an orange "Instructions" box.](../../../assets/43de77e9cefe-28038-3.png)

*Multiple Instruction, Single Data Diagram*

### MIMD – Multiple Instruction, Multiple Data

| **Description** | **Key Features** |
|---|---|
| **Multiple processors** execute **different instructions** on **different data sets** | Most **modern multi-core processors** use this model |
| Allows full **concurrent processing** of independent tasks | Flexible and scalable for parallel programs |

**Example**: Multi-core CPUs, distributed systems, cloud computing

![Diagram showing data and instructions connecting to several processors with blue and orange arrows indicating data and instruction flow.](../../../assets/e10cdd802e30-48232-4.png)

*Multiple Instruction, Multiple Data Diagram*

#### Summary table

| **Architecture** | **Instruction Stream** | **Data Stream** | **Used In** |
|---|---|---|---|
| **SISD** | Single | Single | Standard sequential processors |
| **SIMD** | Single | Multiple | Vector processing (e.g. GPUs) |
| **MISD** | Multiple | Single | Specialised fault-tolerant systems |
| **MIMD** | Multiple | Multiple | Multi-core processors, parallel systems |
