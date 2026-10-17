# Purposes of an Operating System (OS)

Course: cie-a-level-computer-science-19 · Section: 16. System Software

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/16-system-software-/purposes-of-an-operating-system-os/


## Card 1 — keyword_definition (`fl_mFzsf83cVmyrb5x9`)

**FRONT**

Define **resource management**.


**BACK**

Resource management is the operating system **managing the computer's hardware efficiently** to ensure the system runs smoothly.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 2 — question_and_answer (`fl_6d43PJ34NdCZ8SCW`)

**FRONT**

Name three things resource management is vital for.


**BACK**

**Maximising performance**, **reducing bottlenecks**, and **ensuring multitasking works correctly**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 3 — question_and_answer (`fl_JBH5zvGXCGZwP9mc`)

**FRONT**

What runs when a computer is switched on?


**BACK**

The **BIOS**, stored in ROM, runs a **bootstrap** program.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 4 — fill_in_the_blanks (`fl_Q4VK659nW4bbQNj9`)

**FRONT**

The BIOS is stored in <u>**        **</u> and runs the bootstrap program.


**BACK**

The BIOS is stored in **ROM** and runs the bootstrap program.


*Blanks: 1 — answers: []*

Spec links: `spcpt_CsXnJscqXWtXVj5V`

Flags: blank_answer_mismatch


## Card 5 — question_and_answer (`fl_SrTkS8Shyjs35b7D`)

**FRONT**

What does the bootstrap program load?


**BACK**

The **kernel** and essential parts of the OS, from hard disk or flash storage into **main memory (RAM)**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 6 — question_and_answer (`fl_5H2vM6tzXk4z8xp2`)

**FRONT**

How is flash memory organised on tablets and smartphones?


**BACK**

A **read-only section for the operating system**, and a **second section for apps and user data**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 7 — keyword_definition (`fl_GP7DQHbws84vs6rn`)

**FRONT**

Define **kernel**.


**BACK**

The kernel is the **core of the operating system**, responsible for process, memory, device, interrupt and file management.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 8 — true_or_false (`fl_pz6kbSCWKvCCFskm`)

**FRONT**

**True or False?**

The kernel is responsible only for memory management.


**BACK**

**False.**

The kernel manages **processes, memory, devices, interrupts and files**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 9 — question_and_answer (`fl_7NCD2DhbZYSxFJ3d`)

**FRONT**

What does the kernel do for process management?


**BACK**

It **schedules processes**, **allocates CPU time**, and **handles multitasking**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 10 — question_and_answer (`fl_Fs2J7mZZTRfrY4yx`)

**FRONT**

What does the kernel do for memory management?


**BACK**

It **allocates RAM to processes**, handles **virtual memory**, and **prevents clashes**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 11 — question_and_answer (`fl_fFt4qQcJcVzK5gMZ`)

**FRONT**

What does the kernel use to control input and output devices?


**BACK**

**Device drivers**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 12 — question_and_answer (`fl_QCQZcW3ZQ9Rn8VXT`)

**FRONT**

How does the OS maximise CPU usage?


**BACK**

Through **scheduling**, which allows multiple processes to be managed efficiently.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 13 — question_and_answer (`fl_dPg7YD2X46VJNfFr`)

**FRONT**

What does multitasking ensure?


**BACK**

That the CPU **switches rapidly between processes**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 14 — question_and_answer (`fl_MncXhJQFnZf2wK7r`)

**FRONT**

What happens when RAM is full?


**BACK**

The OS may use **virtual memory** on disk to simulate extra memory, which allows more programs to run than would otherwise fit.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 15 — question_and_answer (`fl_PdH4GvgdwdRVsXPF`)

**FRONT**

Why do input and output devices need optimising?


**BACK**

They are **much slower than the CPU**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 16 — keyword_definition (`fl_PBbCdpfRK87zmnvR`)

**FRONT**

Define **Direct Memory Access (DMA) controller**.


**BACK**

A DMA controller allows **data transfer between memory and devices without CPU involvement**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 17 — true_or_false (`fl_wjpnrDsTVSgVHQkV`)

**FRONT**

**True or False?**

The DMA controller requires the CPU to manage each data transfer.


**BACK**

**False.**

DMA allows transfer **without CPU involvement**, which frees the CPU to perform other tasks.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 18 — question_and_answer (`fl_gGGGk7QPZrkc7Z8D`)

**FRONT**

What is the benefit of DMA?


**BACK**

It **frees up the CPU** to perform other tasks while data is being moved.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 19 — question_and_answer (`fl_yWYNsvBx7gprrNYN`)

**FRONT**

What does the DMA controller do when a transfer is complete?


**BACK**

It sends an **interrupt** to the CPU.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 20 — question_and_answer (`fl_QCnfP8T9VBJMnsfr`)

**FRONT**

How does the OS hide hardware complexity?


**BACK**

It provides a **user-friendly interface** through **GUIs**, and uses **device drivers** to handle communication with specific hardware, so users do not need to know technical commands.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 21 — fill_in_the_blanks (`fl_bpZJtFP2ZDjtdzxR`)

**FRONT**

A GUI makes tasks like file transfers easy, for example <u>**                          **</u> instead of the command line.


**BACK**

A GUI makes tasks like file transfers easy, for example **drag-and-drop** instead of the command line.


*Blanks: 1 — answers: []*

Spec links: `spcpt_CsXnJscqXWtXVj5V`

Flags: blank_answer_mismatch


## Card 22 — question_and_answer (`fl_JTYptCjnxjp3jsmn`)

**FRONT**

Which is faster, a laser printer or a hard disk?


**BACK**

A **hard disk**, at around **100 Mbps**, against around **1 Mbps** for a laser printer.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 23 — question_and_answer (`fl_WQYdsvw9RcmTNyw2`)

**FRONT**

Which techniques manage the input/output resource?


**BACK**

**Interrupts**, **DMA**, **buffering** and **driver management**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 24 — question_and_answer (`fl_CyhvzPNvcgbstYWP`)

**FRONT**

Which techniques manage the storage resource?


**BACK**

**File system management**, and read/write optimisation via **caching and buffering**.


Spec links: `spcpt_CsXnJscqXWtXVj5V`


## Card 25 — keyword_definition (`fl_J6Zmbqj8q7vNQmvy`)

**FRONT**

Define **multitasking**.


**BACK**

Multitasking is the operating system **managing system resources** so that the user has the impression that **multiple programs are running at the same time**.


Spec links: `spcpt_GMyF3qVHqNnkQ5Gv`


## Card 26 — question_and_answer (`fl_dQn8ZZxSt9Z2xrKx`)

**FRONT**

How many instructions can a CPU execute at a time?


**BACK**

**One.** It processes billions per second and switches between tasks so quickly that it gives the **illusion** of programs running simultaneously.


Spec links: `spcpt_GMyF3qVHqNnkQ5Gv`


## Card 27 — fill_in_the_blanks (`fl_99RrqYPsyyqvxn5W`)

**FRONT**

The OS splits tasks and allocates system resources based on a <u>**                **</u>.


**BACK**

The OS splits tasks and allocates system resources based on a **priority**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_GMyF3qVHqNnkQ5Gv`

Flags: blank_answer_mismatch


## Card 28 — keyword_definition (`fl_sj57wGzF9xBS5mK9`)

**FRONT**

Define **process**.


**BACK**

A process is a **program in execution**, including the **program code**, **current data**, **register values** and **memory space**.


Spec links: `spcpt_GMyF3qVHqNnkQ5Gv`


## Card 29 — question_and_answer (`fl_bjk4xmsY6SZ4bs5b`)

**FRONT**

How does the OS treat each running application?


**BACK**

As a **separate process**.


Spec links: `spcpt_GMyF3qVHqNnkQ5Gv`


## Card 30 — question_and_answer (`fl_qxTMZDKZtN4WwZmt`)

**FRONT**

Name the three process states.


**BACK**

**Running**, **ready** and **blocked**.


Spec links: `spcpt_GMyF3qVHqNnkQ5Gv`


## Card 31 — question_and_answer (`fl_jV2nsVGDtz2dxJ4n`)

**FRONT**

What does the running state mean?


**BACK**

The process is **actively being executed by the CPU**.


Spec links: `spcpt_GMyF3qVHqNnkQ5Gv`


## Card 32 — question_and_answer (`fl_q3rmv6pZgqTkVcCJ`)

**FRONT**

What does the ready state mean?


**BACK**

The process is **prepared to run but is waiting for the CPU** to be available.


Spec links: `spcpt_GMyF3qVHqNnkQ5Gv`


## Card 33 — question_and_answer (`fl_qny7cv7tVWkDXfwd`)

**FRONT**

What does the blocked state mean?


**BACK**

The process is **waiting for an event or resource**, such as I/O completion.


Spec links: `spcpt_GMyF3qVHqNnkQ5Gv`


## Card 34 — keyword_definition (`fl_2RXFzvB7w5DSdNMG`)

**FRONT**

Define **scheduling**.


**BACK**

Scheduling is deciding **which tasks to process, for how long, and in what order**.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 35 — question_and_answer (`fl_nrjzvvnt4nffczrd`)

**FRONT**

What is the difference between pre-emptive and non-pre-emptive scheduling?


**BACK**

**Pre-emptive** allocates the CPU for **time-limited slots** and allows processes to be interrupted. **Non-pre-emptive** allocates the CPU for **unlimited time slots**, and a process cannot be interrupted until it completes or reaches its burst time.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 36 — question_and_answer (`fl_yDqgNGDByZHR87sQ`)

**FRONT**

Name two pre-emptive scheduling algorithms.


**BACK**

**Round Robin** and **Shortest Remaining Time First**.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 37 — question_and_answer (`fl_xqMhWfvjqNm5zSZ6`)

**FRONT**

Name two non-pre-emptive scheduling algorithms.


**BACK**

**First Come First Serve** and **Shortest Job First**.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 38 — question_and_answer (`fl_bvkHCJwPNN56j6Vd`)

**FRONT**

What is the risk of pre-emptive scheduling?


**BACK**

**Low-priority processes can be neglected** if high-priority processes arrive frequently.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 39 — question_and_answer (`fl_qjztgvJtpXNndg7v`)

**FRONT**

What is the risk of non-pre-emptive scheduling?


**BACK**

If a process with a **long burst time** is running, **shorter processes are neglected**.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 40 — keyword_definition (`fl_k72SPnG36y2rs4tk`)

**FRONT**

Define **Round Robin** scheduling.


**BACK**

A pre-emptive algorithm that **distributes processor time equally**, giving each process a **time quantum**. A process not finished by the end of its quantum moves to the **back of the queue**.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 41 — keyword_definition (`fl_dsXBzpdJcKWqxK7P`)

**FRONT**

Define **First-Come-First-Served** scheduling.


**BACK**

A non-pre-emptive algorithm that **prioritises processes that arrive at the queue first**. The current process blocks all others until it completes.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 42 — keyword_definition (`fl_R7zZmBYGSGg9MNKg`)

**FRONT**

Define **Multi-Level Feedback Queue** scheduling.


**BACK**

A pre-emptive priority algorithm using **multiple queues** so tasks of equal size are grouped together. Processes start in the highest priority queue and **trickle down** if they exceed the time quantum.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 43 — keyword_definition (`fl_5VxTb5M8Gyht6Zkr`)

**FRONT**

Define **Shortest Job First** scheduling.


**BACK**

A non-pre-emptive algorithm where processes are **continuously sorted by burst time**, shortest to longest, with shorter jobs at the front of the queue.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 44 — keyword_definition (`fl_BsdvwndYDgCQNJY5`)

**FRONT**

Define **Shortest Remaining Time First** scheduling.


**BACK**

A **pre-emptive version of Shortest Job First**, where processes with the **shortest remaining time** have higher priority.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 45 — question_and_answer (`fl_RV6sJQPRHswRbpwb`)

**FRONT**

Give a benefit and a drawback of Round Robin.


**BACK**

**Benefit:** all processes get a fair share of the CPU, and it is predictable. **Drawback:** choosing the right time quantum is difficult, and long processes get high turnaround and waiting times.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 46 — question_and_answer (`fl_pSnKQDDCGFrjcB5w`)

**FRONT**

What do both Shortest Job First and Shortest Remaining Time First require?


**BACK**

**Knowing the burst time of processes in advance**.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 47 — true_or_false (`fl_bxDf4J2Xtf6Qg4zd`)

**FRONT**

**True or False?**

A drawback of one scheduling algorithm is always a drawback.


**BACK**

**False.**

Suitability depends on the **specific scenario and system requirements**. A drawback in one scenario may not be a drawback in another.


Spec links: `spcpt_NCSN5NHRmwzRpzNk`


## Card 48 — question_and_answer (`fl_hk69x8w7PqGnWWMN`)

**FRONT**

What are the five steps of interrupt handling?


**BACK**

An **interrupt signal occurs**; the **current process is paused and its state saved**; the kernel identifies the **source and priority**; the appropriate **Interrupt Service Routine (ISR)** is called; the original process is **restored and resumed**.


Spec links: `spcpt_C3mgT4G7C6jMqGSq`


## Card 49 — question_and_answer (`fl_m9mgG6HVbDShnMy4`)

**FRONT**

What is saved when a process is paused for an interrupt?


**BACK**

Its **state**, including the **registers** and the **program counter**.


Spec links: `spcpt_C3mgT4G7C6jMqGSq`


## Card 50 — keyword_definition (`fl_KWQ3HZ5FBkdRPYjW`)

**FRONT**

Define **Interrupt Service Routine (ISR)**.


**BACK**

The routine that is called to handle a particular interrupt, once the kernel has identified its source and priority.


Spec links: `spcpt_C3mgT4G7C6jMqGSq`


## Card 51 — true_or_false (`fl_xfvjrDw6y76M7Bc7`)

**FRONT**

**True or False?**

After an interrupt has been handled, the original process is discarded.


**BACK**

**False.**

The original process is **restored and resumed**.


Spec links: `spcpt_C3mgT4G7C6jMqGSq`


## Card 52 — question_and_answer (`fl_qHhkT75kvK8HXdHB`)

**FRONT**

What do timer interrupts do?


**BACK**

They **trigger a context switch** between processes, supporting **pre-emptive multitasking**.


Spec links: `spcpt_C3mgT4G7C6jMqGSq`


## Card 53 — question_and_answer (`fl_8mYjcFPgTjJ3tTbx`)

**FRONT**

What do I/O interrupts signal?


**BACK**

That an **I/O task has finished**, such as a file write or printer job, which **unblocks waiting processes**.


Spec links: `spcpt_C3mgT4G7C6jMqGSq`


## Card 54 — question_and_answer (`fl_5rnpQr8TZzzqbtPs`)

**FRONT**

What do hardware interrupts respond to?


**BACK**

**Urgent external events**, such as a power failure or mouse input.


Spec links: `spcpt_C3mgT4G7C6jMqGSq`


## Card 55 — question_and_answer (`fl_vRhNVQtMmnP3fjg5`)

**FRONT**

What do software interrupts do?


**BACK**

They are **generated by programs to request system-level services**, such as memory allocation.


Spec links: `spcpt_C3mgT4G7C6jMqGSq`


## Card 56 — fill_in_the_blanks (`fl_45jJbZFdZw3dx9M9`)

**FRONT**

The <u>**                  **</u>, which is part of the kernel, uses interrupts to decide which process should run next.


**BACK**

The **scheduler**, which is part of the kernel, uses interrupts to decide which process should run next.


*Blanks: 1 — answers: []*

Spec links: `spcpt_C3mgT4G7C6jMqGSq`

Flags: blank_answer_mismatch


## Card 57 — keyword_definition (`fl_2zy4cPSkfXnG9ykv`)

**FRONT**

Define **memory management**.


**BACK**

Memory management is a fundamental role of the operating system, dealing with the **allocation and deallocation of the computer's primary memory**.


Spec links: `spcpt_4BtYyv8hgvms2CFG`


## Card 58 — question_and_answer (`fl_bw9V3W6mqb3kN55w`)

**FRONT**

What happens when a user opens an application?


**BACK**

Its **data is loaded from storage into active memory** so that it can run smoothly.


Spec links: `spcpt_4BtYyv8hgvms2CFG`


## Card 59 — question_and_answer (`fl_kRn9T7Ps77V5Yb6d`)

**FRONT**

Why does primary memory need careful management?


**BACK**

It is a **limited resource** in the system.


Spec links: `spcpt_4BtYyv8hgvms2CFG`


## Card 60 — question_and_answer (`fl_rxhBMqK9R5BJ2C5s`)

**FRONT**

Name two benefits of memory management.


**BACK**

Efficient allocation **enables multitasking**, and it **maintains security** by not letting programs access memory reserved for other programs.


Spec links: `spcpt_4BtYyv8hgvms2CFG`


## Card 61 — fill_in_the_blanks (`fl_cckyFRNJ5Syzt5yH`)

**FRONT**

Memory management maintains <u>**                **</u> by stopping programs accessing memory reserved for others.


**BACK**

Memory management maintains **security** by stopping programs accessing memory reserved for others.


*Blanks: 1 — answers: []*

Spec links: `spcpt_4BtYyv8hgvms2CFG`

Flags: blank_answer_mismatch


## Card 62 — question_and_answer (`fl_Bph7vSsr7gnzB4sH`)

**FRONT**

Name the three memory management techniques.


**BACK**

**Paging**, **segmentation** and **virtual memory**.


Spec links: `spcpt_4BtYyv8hgvms2CFG`


## Card 63 — keyword_definition (`fl_VVKrNc9xhsxx28Cz`)

**FRONT**

Define **paging**.


**BACK**

Paging is a method of **chunking primary memory into equal-sized blocks**.


Spec links: `spcpt_75hmrd2yg9xz7V8W`


## Card 64 — true_or_false (`fl_zZncGpcfnvHQbgvX`)

**FRONT**

**True or False?**

Pages are variable in size.


**BACK**

**False.**

Paging divides memory into **fixed, equal-sized blocks**. It is **segmentation** that uses variable sizes.


Spec links: `spcpt_75hmrd2yg9xz7V8W`


## Card 65 — question_and_answer (`fl_yYT7cy66NynQv3jn`)

**FRONT**

What happens to pages as users switch between applications?


**BACK**

Memory is **dynamically allocated**. Pages are taken away from applications not in active use and granted to applications that are in active use.


Spec links: `spcpt_75hmrd2yg9xz7V8W`


## Card 66 — keyword_definition (`fl_5sng2Kd5GFb6xVyx`)

**FRONT**

Define **internal fragmentation**.


**BACK**

Internal fragmentation is the wasted space that builds up **inside pages** over time, because unused space in a page cannot hold other unrelated data.


Spec links: `spcpt_75hmrd2yg9xz7V8W`


## Card 67 — question_and_answer (`fl_4ymGPk4gBKdFN5kj`)

**FRONT**

A 200KB file is divided into four 64KB pages.

How much of the last page is used?


**BACK**

The first three pages hold 192KB, so the fourth page has **8KB used** and **56KB unused**.


Spec links: `spcpt_75hmrd2yg9xz7V8W`


## Card 68 — question_and_answer (`fl_PKq629JnB7sCF3TM`)

**FRONT**

Why is unused space in a page wasteful?


**BACK**

Because **other unrelated data cannot be stored in that page**.


Spec links: `spcpt_75hmrd2yg9xz7V8W`


## Card 69 — question_and_answer (`fl_sxvDXvBRh3W6T5hZ`)

**FRONT**

Give one benefit and one drawback of paging.


**BACK**

**Benefit:** it facilitates efficient memory management and enables the use of virtual memory. **Drawback:** it can lead to **internal fragmentation**.


Spec links: `spcpt_75hmrd2yg9xz7V8W`


## Card 70 — keyword_definition (`fl_hfWqyRy3qRqxrPsv`)

**FRONT**

Define **segmentation**.


**BACK**

Segmentation is a method of **chunking memory into blocks that correspond to different types of data** needed by an application.


Spec links: `spcpt_ztV4XcxXGcRJ9KRK`


## Card 71 — question_and_answer (`fl_RsFtRTzj9R825N2q`)

**FRONT**

Are segments all the same size?


**BACK**

**No.** They are **sized depending on their allocated data**.


Spec links: `spcpt_ztV4XcxXGcRJ9KRK`


## Card 72 — question_and_answer (`fl_46Y28zFcNVc9Gg8J`)

**FRONT**

Give an example of segments in an application.


**BACK**

A video editing application may have a segment for **video data**, **audio data** and **special effects**.


Spec links: `spcpt_ztV4XcxXGcRJ9KRK`


## Card 73 — keyword_definition (`fl_ZxhcHYY9z2Gqydts`)

**FRONT**

Define **external fragmentation**.


**BACK**

As segments fill up the memory, **physical gaps reduce the maximum size of new segments** that can be allocated.


Spec links: `spcpt_ztV4XcxXGcRJ9KRK`


## Card 74 — question_and_answer (`fl_py5gRH9kh67rTvTT`)

**FRONT**

Give one benefit and one drawback of segmentation.


**BACK**

**Benefit:** it allows intuitive and efficient memory access, allocating only the space an application needs. **Drawback:** it can result in **external fragmentation**.


Spec links: `spcpt_ztV4XcxXGcRJ9KRK`


## Card 75 — keyword_definition (`fl_THCPHNyFm5F2rxTp`)

**FRONT**

Define **virtual memory**.


**BACK**

When a computer is running low on primary memory, **secondary storage acts as an extension of the main memory**.


Spec links: `spcpt_y7VT64ymwJ6m4GnB`


## Card 76 — question_and_answer (`fl_yCmMvFFDGRDVr3gH`)

**FRONT**

What does virtual memory create?


**BACK**

An **illusion of a larger memory**, which enables applications to continue to multitask.


Spec links: `spcpt_y7VT64ymwJ6m4GnB`


## Card 77 — fill_in_the_blanks (`fl_NkGGGdYqxHkWXj9N`)

**FRONT**

Virtual memory is created <u>**                      **</u>.


**BACK**

Virtual memory is created **temporarily**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_y7VT64ymwJ6m4GnB`

Flags: blank_answer_mismatch


## Card 78 — question_and_answer (`fl_HGdVkfBYYKZwHFGd`)

**FRONT**

How does virtual memory compare with RAM for speed?


**BACK**

Accessing data in virtual memory is **considerably slower** than RAM. Solid-state drives are faster than hard-disk drives, but **neither is as fast as RAM**.


Spec links: `spcpt_y7VT64ymwJ6m4GnB`


## Card 79 — true_or_false (`fl_nRJCCZfVMdqNSFgk`)

**FRONT**

**True or False?**

Virtual memory is as fast as RAM.


**BACK**

**False.**

It is **considerably slower**. Neither solid-state drives nor hard disks are as fast as RAM.


Spec links: `spcpt_y7VT64ymwJ6m4GnB`


## Card 80 — question_and_answer (`fl_RHjHRGFRvPdzW3mx`)

**FRONT**

What is the risk of over-relying on virtual memory?


**BACK**

**Performance issues**.


Spec links: `spcpt_y7VT64ymwJ6m4GnB`


## Card 81 — question_and_answer (`fl_DQZnPxt8SWn3wF3f`)

**FRONT**

Explain what is meant by virtual memory, for 3 marks.


**BACK**

**Disk or secondary storage is used to extend the RAM available**, so the CPU **appears able to access more memory than the available RAM**. Only the data in use needs to be in main memory, so data can be **swapped between RAM and virtual memory** as necessary.


Spec links: `spcpt_y7VT64ymwJ6m4GnB`


## Card 82 — question_and_answer (`fl_wV3N84bVJWCH4Vyc`)

**FRONT**

State one difference between paging and segmentation in how memory is divided.


**BACK**

**Paging** divides memory into **fixed size blocks**. **Segmentation** divides memory into **variable sized blocks**.


Spec links: `spcpt_y7VT64ymwJ6m4GnB`


## Card 83 — question_and_answer (`fl_FFn8ngBghFrz2dkG`)

**FRONT**

Who decides the size, for paging and for segmentation?


**BACK**

The **operating system** divides the memory into pages. The **compiler** is responsible for calculating the segment size.


Spec links: `spcpt_y7VT64ymwJ6m4GnB`


## Card 84 — question_and_answer (`fl_8254kGnbgwPWhrMh`)

**FRONT**

Which has faster access times, paging or segmentation?


**BACK**

**Paging**.


Spec links: `spcpt_y7VT64ymwJ6m4GnB`

