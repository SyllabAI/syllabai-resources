# Exam Questions — Purposes of an Operating System (OS)
**16. System Software** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 24 questions across 1 sets


## Exam Questions (24 questions)


### Q1 — hard — 5 marks

**Q1** [5 marks]

A computer uses virtual memory stored on a hard disk drive. A technician records how the computer spends its time as more programs are opened.

| Number of programs open | Percentage of time spent processing data | Percentage of time spent swapping pages |
|---|---|---|
| 2 | 95 | 5 |
| 4 | 88 | 12 |
| 6 | 70 | 30 |
| 8 | 45 | 55 |
| 10 | 10 | 90 |

(i) Using the table, state the smallest number of programs open at which the computer has reached the thrash point. Give a reason for your answer.

(2)

(ii) Explain why the percentage of time spent swapping pages increases as more programs are opened.

(3)

### Q2 — medium — 3 marks

**Q2** [3 marks]

A computer uses paging and virtual memory. The RAM is full. A running program needs a page that is currently held in virtual memory.

Describe how the operating system replaces a page in RAM so that the program can use the page it needs.

### Q3 — easy — 2 marks

**Q3** [2 marks]

Describe what is meant by **virtual memory**.

### Q4 — hard — 4 marks

**Q4** [4 marks]

A computer has 8 GiB of RAM. A user starts a program that needs 12 GiB of memory for its code and data. The operating system uses segmentation and virtual memory.

Explain how segmentation and virtual memory allow this program to run on the computer.

### Q5 — medium — 3 marks

**Q5** [3 marks]

Paging and segmentation are both used in memory management.

Complete the table to show **one** difference between paging and segmentation for each feature.

| Feature | Paging | Segmentation |
|---|---|---|
| Size of each block of memory |   |   |
| What calculates the size of the blocks |   |   |
| Speed of access |   |   |

### Q6 — easy — 2 marks

**Q6** [2 marks]

A computer uses segmentation for memory management.

Identify the **two** values that make up an address in a program's logical address space when segmentation is used.

### Q7 — hard — 4 marks

**Q7** [4 marks]

Four processes are waiting in the queue for the processor. They joined the queue in the order shown. No other processes join the queue.

| Process | Order of joining the queue | Processor time needed (ms) |
|---|---|---|
| P | 1 | 45 |
| Q | 2 | 5 |
| R | 3 | 20 |
| S | 4 | 10 |

Throughput is the number of processes completed in a given amount of time.

Use the information in the table to explain why shortest job first scheduling gives a higher throughput than first come first served scheduling for these processes.

### Q8 — hard — 3 marks

**Q8** [3 marks]

A computer uses paging. The table shows eight blocks of main memory. All the blocks are the same size.

| Block | Status |
|---|---|
| 1 | In use |
| 2 | Free |
| 3 | In use |
| 4 | Free |
| 5 | In use |
| 6 | In use |
| 7 | Free |
| 8 | In use |

A running program needs three more of its pages to be loaded from secondary storage. There is no area of main memory where three free blocks are next to each other.

Explain how paging allows all three pages to be loaded into main memory.

### Q9 — medium — 3 marks

**Q9** [3 marks]

A program is stored on secondary storage. The operating system uses paging when the program is run.

Describe how paging is used to manage main memory while the program is running.

### Q10 — easy — 2 marks

**Q10** [2 marks]

Paging is one of the techniques an operating system uses for memory management.

Describe what is meant by **paging**.

### Q11 — medium — 3 marks

**Q11** [3 marks]

A computer is used for two tasks at once. A user is typing a report in a word processor. At the same time, a video-editing program is producing a long video file, which needs a lot of processor time. The video-editing process joined the queue for the processor first.

Explain why round robin scheduling is more suitable than first come first served scheduling in this situation.

### Q12 — medium — 3 marks

**Q12** [3 marks]

A computer is running several programs at the same time, including a web browser, a word processor and a music player.

Explain why the operating system needs to carry out memory management while these programs are running.

### Q13 — easy — 2 marks

**Q13** [2 marks]

A file server has a single processor. Its operating system has many processes to run.

Give two reasons why the operating system needs to schedule these processes.

### Q14 — hard — 4 marks

**Q14** [4 marks]

A student's computer has a processor with a single core. The student has a web browser, a music player and a spreadsheet open at the same time. The student also sends a long document to a printer.

Explain how the Operating System (OS) maximises the use of the computer's resources in this situation.

Your answer must refer to the processor, main memory **and** the printer.

### Q15 — hard — 4 marks

**Q15** [4 marks]

A computer has a single processor. A user has three programs open at the same time:

- a music player
- a word processor
- a program that is copying a large file to a USB flash drive.

The user believes that all three programs are running at the same time.

Explain how the operating system uses the running, ready and blocked process states to make it appear that all three programs are running at the same time.

### Q16 — medium — 3 marks

**Q16** [3 marks]

A process is in the running state. It needs to read data from a file stored on a hard disk before it can continue.

Describe the changes of process state that happen from this point until the process is executed by the processor again.

### Q17 — easy — 2 marks

**Q17** [2 marks]

An operating system (OS) gives every process a process state.

Complete the table by writing the name of the process state that matches each description. The first row has been done for you.

| Description | Process state |
|---|---|
| The process is being executed by the processor. | Running |
| The process could be executed, but it is waiting for the processor to become available. |   |
| The process cannot continue until an event happens, such as an input/output operation finishing. |   |

### Q18 — hard — 4 marks

**Q18** [4 marks]

An operating system uses interrupt handling to manage low-level scheduling.

Process A is in the running state and process B is in the ready state. An interrupt is generated. The interrupt has a higher priority than process A.

Explain how the kernel handles this interrupt so that process A stops running and can later continue from the point at which it stopped.

### Q19 — easy — 2 marks

**Q19** [2 marks]

A student copies a photo from the hard disk of a computer to a USB flash drive. The student does this by dragging the icon for the photo onto the icon for the flash drive.

The user interface hides the complexities of the hardware from the student.

Identify **two** complexities of the hardware that are hidden from the student during this task.

### Q20 — easy — 2 marks

**Q20** [2 marks]

An operating system receives an interrupt that has a higher priority than the process that is currently running.

Identify:

- the mode that the system enters to handle the interrupt
- the table that is consulted to find the Interrupt Service Routine (ISR) for this type of interrupt.

### Q21 — medium — 5 marks

**Q21** [2 marks]

The kernel is the central component of an Operating System (OS).

Outline how the kernel of an OS acts as an interrupt handler.

*Source: Nov 2024 9618/32 Q9A*


**Q21** [3 marks]

(i) State what is meant by the term **multi‑tasking** in an Operating System.

(1)

(ii) Describe how multi‑tasking is implemented in an Operating System.

(2)

*Source: Nov 2024 9618/32 Q9B*


### Q22 — medium — 7 marks

**Q22** [4 marks]

Describe the process of **segmentation **for memory management.

*Source: Nov 2024 9618/31 Q8A*


**Q22** [3 marks]

Explain what is meant by **disk thrashing.**

*Source: Nov 2024 9618/31 Q8B*


### Q23 — medium — 5 marks

**Q23** [2 marks]

Outline the reasons why an operating system may need to use virtual memory.

*Source: November 2023 9618/32 Q5A*


**Q23** [3 marks]

Explain the circumstances in which disk thrashing could occur.

*Source: November 2023 9618/32 Q5B*


### Q24 — medium — 5 marks

**Q24** [2 marks]

A student buys a new computer.

State one benefit to the student of a user interface and give an example.

Benefit

Example

*Source: November 2023 9618/31 Q7A*


**Q24** [1 mark]

Two of the process states are the running state and the ready state.

Identify one other process state.

*Source: November 2023 9618/31 Q7B*


**Q24** [2 marks]

Outline conditions under which a process could change from the running state to the ready state.

*Source: November 2023 9618/31 Q7C*

