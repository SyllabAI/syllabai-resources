# Processors, Parallel Processing & Virtual Machines

Course: cie-a-level-computer-science-19 · Section: 15. Hardware & Virtual Machines

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/15-hardware-and-virtual-machines-/processors-parallel-processing-and-virtual-machines/


## Card 1 — keyword_definition (`fl_YZn8VDdHkH5qq6xh`)

**FRONT**

Define **RISC**.


**BACK**

Reduced Instruction Set Computer: a processor with a **smaller instruction set** made up of **simpler instructions**.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 2 — keyword_definition (`fl_7VRqp8CfhW28WXQw`)

**FRONT**

Define **CISC**.


**BACK**

Complex Instruction Set Computer: a processor with a **larger instruction set** that includes **more complex instructions**.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 3 — question_and_answer (`fl_5h4MnVjx8PYY2MrS`)

**FRONT**

How many clock cycles does a RISC instruction take?


**BACK**

**One clock cycle**, which is what makes RISC more suitable for pipelining.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 4 — question_and_answer (`fl_yKq9Hkx9T2XfxKtV`)

**FRONT**

How many clock cycles does a CISC instruction take?


**BACK**

**More than one clock cycle**, because the instructions are more complex.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 5 — fill_in_the_blanks (`fl_nFHsqHpPzBtVc4yp`)

**FRONT**

RISC is better suited to <u>**                    **</u> because each instruction takes one clock cycle.


**BACK**

RISC is better suited to **pipelining** because each instruction takes one clock cycle.


*Blanks: 1 — answers: []*

Spec links: `spcpt_ZbWSzmYtMGRXPsSW`

Flags: blank_answer_mismatch


## Card 6 — question_and_answer (`fl_khyhwmCnJVf836vx`)

**FRONT**

Why might a RISC program require more instructions?


**BACK**

Because **each instruction performs a simpler operation**.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 7 — question_and_answer (`fl_vjxBNG3FJ9dfMtHG`)

**FRONT**

Which has more general-purpose registers, RISC or CISC?


**BACK**

**RISC** has more general-purpose registers. **CISC** has fewer.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 8 — question_and_answer (`fl_Z5RrxJqvthxqSwNr`)

**FRONT**

Which has more addressing modes, RISC or CISC?


**BACK**

**CISC** has more addressing modes. **RISC** has fewer.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 9 — question_and_answer (`fl_ZgGBDPcHpwvVch2r`)

**FRONT**

Which uses more memory, and why?


**BACK**

**RISC** uses more memory, because it needs **more instructions**. CISC instructions take up **less space in memory**.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 10 — question_and_answer (`fl_q4q4TKGnXHrkMTMV`)

**FRONT**

Which has the more complex compiler?


**BACK**

**RISC** has a **more complex** compiler. CISC's compiler is less complex.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 11 — question_and_answer (`fl_jjmq4d3hDBNsc5Hg`)

**FRONT**

Compare RISC and CISC on power usage and cost.


**BACK**

**RISC** has **lower** power usage and **lower** cost. **CISC** is **higher** on both.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 12 — question_and_answer (`fl_yfFrcX3NnZx2hVSN`)

**FRONT**

Which devices typically use RISC, and which use CISC?


**BACK**

**RISC** is usually used in **smartphones and tablets**. **CISC** is usually used in **laptops and desktop computers**.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 13 — question_and_answer (`fl_xSbYgx3P8Rb3g9Xb`)

**FRONT**

Which processor type uses both a hardwired and a micro-coded control unit?


**BACK**

**CISC**


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 14 — question_and_answer (`fl_Sw8RMcgK2vnFYyfX`)

**FRONT**

Which processor type splits cache between data and instructions?


**BACK**

**RISC**


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 15 — true_or_false (`fl_pw7pmnPRJT8H9KtT`)

**FRONT**

**True or False?**

A program written for a RISC processor will run on a CISC processor.


**BACK**

**False.**

It **will not work**. It will not necessarily work on **another RISC** processor either, because they may have different instruction sets.


Spec links: `spcpt_ZbWSzmYtMGRXPsSW`


## Card 16 — question_and_answer (`fl_mmsndyt7BBPjh3g4`)

**FRONT**

How does CISC handle interrupts?


**BACK**

Using **microcode and dedicated hardware instructions**, which manages interrupts efficiently.


Spec links: `spcpt_xQNZWgjMdJQxThH4`


## Card 17 — question_and_answer (`fl_kQ5pBt6Hvn7X6K3j`)

**FRONT**

How does RISC handle interrupts?


**BACK**

Using **software-based interrupt handlers**, managed through general-purpose registers and simple instructions.


Spec links: `spcpt_xQNZWgjMdJQxThH4`


## Card 18 — question_and_answer (`fl_HPvG2qyzvCt2Jd3k`)

**FRONT**

How does context switching differ between RISC and CISC?


**BACK**

**CISC** may have **hardware support** to save and restore the processor state automatically. **RISC** typically handles it in **software**, giving more control but requiring more instructions.


Spec links: `spcpt_xQNZWgjMdJQxThH4`


## Card 19 — fill_in_the_blanks (`fl_9zFcVYYZcqZHmQpK`)

**FRONT**

CISC can handle multiple tasks in a single instruction, including context <u>**            **</u>.


**BACK**

CISC can handle multiple tasks in a single instruction, including context **saving**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_xQNZWgjMdJQxThH4`

Flags: blank_answer_mismatch


## Card 20 — question_and_answer (`fl_tbTWWTx3bhPrwyvm`)

**FRONT**

Which responds to interrupts faster, and why?


**BACK**

**CISC**, because of its **built-in support**. RISC is slower, but **more flexible and consistent** across all instructions.


Spec links: `spcpt_xQNZWgjMdJQxThH4`


## Card 21 — true_or_false (`fl_QfVZv2MMd8pBqxP6`)

**FRONT**

**True or False?**

RISC handles interrupts faster than CISC.


**BACK**

**False.**

**CISC** is generally faster due to built-in support. RISC is **slower but more flexible**.


Spec links: `spcpt_xQNZWgjMdJQxThH4`


## Card 22 — question_and_answer (`fl_ksWryT9Sg7rh3XzX`)

**FRONT**

What is the trade-off in CISC interrupt handling?


**BACK**

It is **more efficient but less flexible**.


Spec links: `spcpt_xQNZWgjMdJQxThH4`


## Card 23 — question_and_answer (`fl_fjxMC8SFcBKVvxnZ`)

**FRONT**

What is the advantage of RISC interrupt handling?


**BACK**

It is **simpler and more predictable**, and gives the operating system **greater control**.


Spec links: `spcpt_xQNZWgjMdJQxThH4`


## Card 24 — question_and_answer (`fl_6ZxbWchmYQz3cSYc`)

**FRONT**

What do both architectures aim to do with interrupts?


**BACK**

**Respond to interrupts quickly and resume execution correctly**, using different design philosophies.


Spec links: `spcpt_xQNZWgjMdJQxThH4`


## Card 25 — keyword_definition (`fl_VvRyzf6f2VTFdRXR`)

**FRONT**

Define **pipelining**.


**BACK**

Pipelining is the process of **carrying out multiple instructions concurrently**, with each instruction at a different stage of the fetch-decode-execute cycle.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 26 — true_or_false (`fl_RdQjjJvJR4499bPG`)

**FRONT**

**True or False?**

In pipelining, all instructions are at the same stage at the same time.


**BACK**

**False.**

Each instruction is at a **different stage** of the fetch-decode-execute cycle.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 27 — question_and_answer (`fl_tHjHQMXGv8kbxp9f`)

**FRONT**

Give an example of what happens at once during pipelining.


**BACK**

One instruction can be **fetched** while the previous one is being **decoded** and the one before that is being **executed**.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 28 — question_and_answer (`fl_x4GhjpWWFFk57tBz`)

**FRONT**

What happens to the pipeline in the case of a branch?


**BACK**

The pipeline is **flushed**.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 29 — question_and_answer (`fl_ws23N7YVnKSkHfJV`)

**FRONT**

At step 3 of a pipeline, which instructions are at which stage?


**BACK**

Instruction **C is being fetched**, instruction **B is being decoded**, and instruction **A is being executed**.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 30 — question_and_answer (`fl_CPhbvd55b3Fz9wmy`)

**FRONT**

Name the five stages of the pipeline in a RISC processor.


**BACK**

**Instruction fetch (IF)**, **instruction decode (ID)**, **operand fetch (OF)**, **instruction execute (IE)**, and **write back result (WB)**.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 31 — question_and_answer (`fl_tzHrV7jmpmDBzvMf`)

**FRONT**

How long does each pipeline subtask take?


**BACK**

**One clock cycle**.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 32 — question_and_answer (`fl_GjB4b6Jw7GWBJqWc`)

**FRONT**

Can two instructions execute the same stage in the same clock cycle?


**BACK**

**No.** No two instructions can execute their same stage at the same clock cycle.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 33 — question_and_answer (`fl_Mz4qJK9Pk8tqfv54`)

**FRONT**

When does the second instruction begin?


**BACK**

In the **second clock cycle**, while the first instruction has moved on to its second subtask.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 34 — question_and_answer (`fl_gwXptMYGHjrpQ6Jw`)

**FRONT**

Why are RISC processors designed for pipelining efficiency?


**BACK**

Each instruction takes **one clock cycle**, instructions are **fixed-length**, the **instruction set is limited**, and there are **many general-purpose registers**.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 35 — question_and_answer (`fl_PdRhbqhb8mgYxhY9`)

**FRONT**

How do fixed-length instructions help pipelining?


**BACK**

They make **decoding easier**.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 36 — question_and_answer (`fl_D7NPNYZVqQ68mM8W`)

**FRONT**

How does a limited instruction set help pipelining?


**BACK**

It **reduces complexity and stage duration**.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 37 — keyword_definition (`fl_KtC2pWcnGJ34BbhY`)

**FRONT**

Define **register** in the context of pipelining.


**BACK**

Registers are **fast, temporary storage inside the CPU**.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 38 — fill_in_the_blanks (`fl_cPjdwyVT4d7tTDqJ`)

**FRONT**

RISC processors rely heavily on registers for <u>**              **</u> storage rather than accessing RAM.


**BACK**

RISC processors rely heavily on registers for **operand** storage rather than accessing RAM.


*Blanks: 1 — answers: []*

Spec links: `spcpt_wrYpPwbDRqWRBC2B`

Flags: blank_answer_mismatch


## Card 39 — question_and_answer (`fl_7rwdbQkXtyw3xkyT`)

**FRONT**

Why do RISC processors rely on registers rather than RAM?


**BACK**

Register usage **reduces memory bottlenecks**, allowing pipelining to run smoothly.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 40 — question_and_answer (`fl_d7P57CjSsmS24H32`)

**FRONT**

Where are intermediate values stored during pipelining?


**BACK**

In **registers between stages**.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 41 — question_and_answer (`fl_cCkMb9TTFsn39mN5`)

**FRONT**

Name four benefits of pipelining.


**BACK**

**Increased throughput**, **better use of CPU components**, **reduced idle time**, and **faster execution of the instruction stream**.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 42 — fill_in_the_blanks (`fl_pTmn8WtD6J5PtSdm`)

**FRONT**

Pipelining means the fetch, decode and execute units are all in use <u>**                            **</u>.


**BACK**

Pipelining means the fetch, decode and execute units are all in use **simultaneously**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_wrYpPwbDRqWRBC2B`

Flags: blank_answer_mismatch


## Card 43 — true_or_false (`fl_c4Y3ZcVPJSD2TpYb`)

**FRONT**

**True or False?**

Pipelining makes each individual instruction execute faster.


**BACK**

**False.**

Individual instructions do not run faster. It is the **instruction stream** as a whole that executes faster.


Spec links: `spcpt_wrYpPwbDRqWRBC2B`


## Card 44 — keyword_definition (`fl_HJ6V5VrpMBFsHv7W`)

**FRONT**

Define **computer architecture**.


**BACK**

A computer architecture is the **design and structure of a computer system**, describing how it **fetches, processes and stores data and instructions**.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 45 — question_and_answer (`fl_MtK6gsJ7HfpmkbRp`)

**FRONT**

What does a computer architecture define?


**BACK**

How components like the **CPU, memory and input/output devices work together to execute programs**.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 46 — question_and_answer (`fl_WZF6PK3PR28fbbBC`)

**FRONT**

What two things is each architecture categorised by?


**BACK**

Whether it has a **single or multiple instruction stream**, and a **single or multiple data stream**.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 47 — keyword_definition (`fl_f7zhkMxHRVg82y8t`)

**FRONT**

Define **SISD**.


**BACK**

Single Instruction, Single Data: one processor executes **one instruction on one data stream at a time**.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 48 — fill_in_the_blanks (`fl_NBhZx66vrtv7XrQF`)

**FRONT**

SISD is a traditional <u>**            **</u>, non-parallel architecture.


**BACK**

SISD is a traditional **serial**, non-parallel architecture.


*Blanks: 1 — answers: []*

Spec links: `spcpt_hn7PRVxWyP4SzNWt`

Flags: blank_answer_mismatch


## Card 49 — question_and_answer (`fl_HpGD8VC9F7dhd2kv`)

**FRONT**

Where is SISD used?


**BACK**

In **basic, single-core processors**, for example a classic desktop CPU running one task at a time.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 50 — keyword_definition (`fl_ng6jgFXNnfGnJSs7`)

**FRONT**

Define **SIMD**.


**BACK**

Single Instruction, Multiple Data: **one instruction is applied to multiple pieces of data at once**.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 51 — question_and_answer (`fl_5ZrBDkJgkTMQF9mR`)

**FRONT**

What do all processing units do in SIMD?


**BACK**

They perform the **same operation in parallel**.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 52 — true_or_false (`fl_VCjxPCrfvpm4N8wn`)

**FRONT**

**True or False?**

In SIMD, each processing unit performs a different operation.


**BACK**

**False.**

All processing units perform the **same operation** in parallel.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 53 — fill_in_the_blanks (`fl_VPvftdsx9BMkxY4B`)

**FRONT**

SIMD is ideal for graphics or <u>**                    **</u> computation.


**BACK**

SIMD is ideal for graphics or **scientific** computation.


*Blanks: 1 — answers: []*

Spec links: `spcpt_hn7PRVxWyP4SzNWt`

Flags: blank_answer_mismatch


## Card 54 — question_and_answer (`fl_b4QtC9PHdvPg8Mg8`)

**FRONT**

Where is SIMD used?


**BACK**

In **GPU operations and image processing**, where it is useful for parallel processing.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 55 — keyword_definition (`fl_hpWdT8NP8dj9nTyg`)

**FRONT**

Define **MISD**.


**BACK**

Multiple Instruction, Single Data: multiple processors execute **different instructions on the same data**.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 56 — question_and_answer (`fl_NvcWGwBxgcvpcWPZ`)

**FRONT**

How common is MISD in practice?


**BACK**

**Very uncommon**.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 57 — question_and_answer (`fl_BJSM8gqRzZy9Jk2G`)

**FRONT**

What is MISD used for?


**BACK**

Specialised systems for **fault tolerance**, where each unit **checks the same input differently**, such as redundant systems in safety-critical environments.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 58 — keyword_definition (`fl_RSFxZR2rMsY7NN7s`)

**FRONT**

Define **MIMD**.


**BACK**

Multiple Instruction, Multiple Data: multiple processors execute **different instructions on different data sets**.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 59 — question_and_answer (`fl_xTq5XmD7CBs3CT8z`)

**FRONT**

What does MIMD allow?


**BACK**

Full **concurrent processing of independent tasks**, making it flexible and scalable for parallel programs.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 60 — question_and_answer (`fl_FbYkVPxxWg9r3pFG`)

**FRONT**

Where is MIMD used?


**BACK**

In **most modern multi-core processors**, distributed systems and cloud computing.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 61 — true_or_false (`fl_wYtj9q5wHkTHnhvQ`)

**FRONT**

**True or False?**

MISD is the architecture used by most modern multi-core processors.


**BACK**

**False.**

**MIMD** is used by most modern multi-core processors. MISD is **very uncommon** in practice.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 62 — question_and_answer (`fl_VMKKCBnFD5ChXwWN`)

**FRONT**

What is the difference between SIMD and MIMD?


**BACK**

**SIMD** applies **one instruction to many data items** at once. **MIMD** runs **different instructions on different data**, fully independently.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 63 — question_and_answer (`fl_hKGMBhD9DWckYz9Y`)

**FRONT**

Which architecture is used for vector processing?


**BACK**

**SIMD**, for example in GPUs.


Spec links: `spcpt_hn7PRVxWyP4SzNWt`


## Card 64 — keyword_definition (`fl_27BBBRz3KJj9Rcy2`)

**FRONT**

Define **massively parallel computer**.


**BACK**

A system made up of **thousands of processors working simultaneously** to solve a single large problem.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 65 — question_and_answer (`fl_FGXFhsT76hpnMpCv`)

**FRONT**

How does a massively parallel system work?


**BACK**

Each processor **executes part of a program**, and the **results are combined** to produce the final output.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 66 — true_or_false (`fl_7BZVSm7kHYK6vy38`)

**FRONT**

**True or False?**

Each processor in a massively parallel system solves a separate problem.


**BACK**

**False.**

They work **simultaneously to solve a single large problem**, each executing **part of a program**.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 67 — question_and_answer (`fl_d5tFckWhGXpM6V78`)

**FRONT**

Name three fields that use massively parallel computers.


**BACK**

**Scientific research**, **weather simulation**, **cryptography** and **AI**.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 68 — question_and_answer (`fl_gs3mFT8JxYgk2bFS`)

**FRONT**

How is memory arranged in a massively parallel system?


**BACK**

Each processor may have **its own memory**, or access **shared memory resources**.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 69 — fill_in_the_blanks (`fl_rtxgPVTR5d4NKqYV`)

**FRONT**

Processors in a massively parallel system are linked by high-speed <u>**                          **</u>.


**BACK**

Processors in a massively parallel system are linked by high-speed **interconnects**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`

Flags: blank_answer_mismatch


## Card 70 — question_and_answer (`fl_QDGTpfFYzFMQ9XWz`)

**FRONT**

What links the processors together?


**BACK**

**High-speed interconnects**, which are fast communication pathways used to share results.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 71 — keyword_definition (`fl_6stxxy7rB85mHJN5`)

**FRONT**

Define **data parallelism**.


**BACK**

Data parallelism is where **many data items are processed at once**, often using SIMD or MIMD.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 72 — keyword_definition (`fl_dwkn63Sk8csGNcjb`)

**FRONT**

Define **task parallelism**.


**BACK**

Task parallelism is where different processors perform **different tasks on different data sets**.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 73 — question_and_answer (`fl_ZNsbbrTjqyFyjfzg`)

**FRONT**

What kind of software does a massively parallel system need?


**BACK**

**Specialised software**, written to **distribute the work efficiently** across the processors.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 74 — fill_in_the_blanks (`fl_KcDczF5xCrtdCW2J`)

**FRONT**

Massively parallel systems are <u>**              **</u> coupled, so the processors depend on one another.


**BACK**

Massively parallel systems are **tightly** coupled, so the processors depend on one another.


*Blanks: 1 — answers: []*

Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`

Flags: blank_answer_mismatch


## Card 75 — question_and_answer (`fl_5jKNFBvFCDVWWX3n`)

**FRONT**

What does 'tightly coupled' mean for a massively parallel system?


**BACK**

Processors **depend on one another** and work collaboratively as a **single system**.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 76 — question_and_answer (`fl_PKfFqNqq8S9prvZZ`)

**FRONT**

How do massively parallel computers differ from clusters in structure?


**BACK**

Massively parallel systems are **thousands of processors forming a single tightly integrated system**. Clusters are **multiple independent systems networked together**.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 77 — true_or_false (`fl_75BYh49f75Bp7kq8`)

**FRONT**

**True or False?**

A cluster computer is a single tightly integrated system.


**BACK**

**False.**

A cluster is **multiple independent systems networked together**, often **loosely coupled**. It is the massively parallel computer that is tightly integrated.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 78 — question_and_answer (`fl_PRDSytTq6gJC4yM3`)

**FRONT**

How does communication differ between a massively parallel system and a cluster?


**BACK**

Massively parallel processors **communicate continuously via shared architecture**. Clusters communicate **via a network**, often loosely coupled.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 79 — question_and_answer (`fl_KzDQDr9krxjrwD5Y`)

**FRONT**

How do a massively parallel system and a cluster differ in behaviour?


**BACK**

A massively parallel system acts like **one machine** with distributed processing. A cluster is a group of **co-operating systems**.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 80 — question_and_answer (`fl_8sJdtYV65hDz6kvp`)

**FRONT**

How do a massively parallel system and a cluster differ in use?


**BACK**

Massively parallel systems give **higher performance** and are used for **supercomputing tasks**. Clusters are **more general-purpose or batch processing** systems.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 81 — question_and_answer (`fl_HHNSN8Gjr8bczCWB`)

**FRONT**

Which two architectures do massively parallel systems often use?


**BACK**

**SIMD**, applying one instruction to many data points at once, and **MIMD**, running different instructions on different data.


Spec links: `spcpt_fC5Mj8ZrPJNw6zYP`


## Card 82 — keyword_definition (`fl_DRBfgBqbMGb63xgN`)

**FRONT**

Define **virtual machine (VM)**.


**BACK**

A virtual machine is an **entire operating system running inside another operating system**.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 83 — question_and_answer (`fl_Qy3cWzhTKKF8zvFz`)

**FRONT**

What can a user do with a virtual machine of another operating system?


**BACK**

**Navigate its GUI** and **install software** on it.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 84 — question_and_answer (`fl_ycGvryj4WFnYdT4q`)

**FRONT**

Why is running a virtual machine useful?


**BACK**

It helps **access software that is only designed to run on specific operating systems**.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 85 — keyword_definition (`fl_Bm8xGbTMH4pJ8pyQ`)

**FRONT**

Define **hypervisor**.


**BACK**

A hypervisor is VM management software that **monitors all activity happening inside the virtual machine**.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 86 — question_and_answer (`fl_Fmct3TRrp8t4NTCQ`)

**FRONT**

Why might a Windows user run a MacOS virtual machine?


**BACK**

Because some software is written to **run only on MacOS**, so the virtual machine lets them install and use it.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 87 — question_and_answer (`fl_JQGdBnXDzr6vjDpX`)

**FRONT**

What is forwards compatibility in the context of virtual machines?


**BACK**

Most software **needs updating to work on the latest operating system versions**, so a user on the newest release may run a VM of a **previous release** to use an application that has not had a forwards-compatibility update.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 88 — question_and_answer (`fl_dpcWhccrZX8QQBdQ`)

**FRONT**

How are virtual machines used in software testing?


**BACK**

They create **isolated test environments** that leave the host operating system **unaffected**.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 89 — true_or_false (`fl_W8GbtV9t2MZCBPDN`)

**FRONT**

**True or False?**

Testing inside a virtual machine affects the host operating system.


**BACK**

**False.**

Virtual machines create **isolated test environments** that leave the host operating system **unaffected**.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 90 — question_and_answer (`fl_z84BRPkJK26kN9pR`)

**FRONT**

Name two things an isolated test environment lets a developer do.


**BACK**

**Monitor how their software affects system performance**, and **test on a clean-slate system** with no other applications running.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 91 — question_and_answer (`fl_scwZqZPh5vrRBBRx`)

**FRONT**

How can virtual machines help software reach more users?


**BACK**

VM software can create machines that **act like they have older hardware**, so developers can build software that runs on older hardware too.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 92 — question_and_answer (`fl_GHbpCY7xVm9zFBY4`)

**FRONT**

How do virtual machines help with cross-platform compatibility?


**BACK**

A developer can **test against various operating systems**, such as MacOS, Linux and Windows, for greater compatibility.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 93 — question_and_answer (`fl_Yhxb9swMWshSKyGB`)

**FRONT**

What allows programs to run across different operating systems?


**BACK**

**Intermediate code**, which is generated through compilation.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 94 — question_and_answer (`fl_sF338RnBShHWfBSY`)

**FRONT**

What hardware do virtual machines use?


**BACK**

VMs **share the same system hardware as the host operating system**.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 95 — true_or_false (`fl_jKwWhds5P7nY7w9g`)

**FRONT**

**True or False?**

A virtual machine has its own dedicated hardware, separate from the host.


**BACK**

**False.**

Virtual machines **share the same system hardware as the host operating system**.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 96 — question_and_answer (`fl_F5rT98WPgFK7rzgD`)

**FRONT**

What is the risk of over-using virtual machines?


**BACK**

It can **exhaust the host system of CPU, hard disk and memory**.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 97 — question_and_answer (`fl_FGD82xX373hymTCX`)

**FRONT**

How can the resource risk of virtual machines be managed?


**BACK**

VM software can **set maximum limits on system resources**.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 98 — question_and_answer (`fl_VtbJbn3Bb3QcH5yq`)

**FRONT**

How might a low-specification machine be configured to run a VM?


**BACK**

To allocate only **1GB of memory and 20% of the CPU**.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 99 — question_and_answer (`fl_3DFgfW5C4km7jyXX`)

**FRONT**

How might a high-specification machine be configured to run a VM?


**BACK**

Up to **8GB of memory and 50% of the CPU**.


Spec links: `spcpt_t4rHbRNyK8FV5Qx2`


## Card 100 — fill_in_the_blanks (`fl_gV4tFymMfVhxqJJD`)

**FRONT**

Operating systems are commonly free to download, but require an <u>**                    **</u> payment to access all features.


**BACK**

Operating systems are commonly free to download, but require an **activation** payment to access all features.


*Blanks: 1 — answers: []*

Spec links: `spcpt_t4rHbRNyK8FV5Qx2`

Flags: blank_answer_mismatch

