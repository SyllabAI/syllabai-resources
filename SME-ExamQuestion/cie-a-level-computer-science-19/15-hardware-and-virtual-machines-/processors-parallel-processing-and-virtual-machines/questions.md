# Exam Questions — Processors, Parallel Processing & Virtual Machines
**15. Hardware & Virtual Machines** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 22 questions across 1 sets


## Exam Questions (22 questions)


### Q1 — medium — 3 marks

**Q1** [3 marks]

Interrupt handling is one application of a stack.

Describe how a processor uses a stack when it handles an interrupt, from the moment the interrupt is detected to the moment the interrupted program continues.

### Q2 — easy — 2 marks

**Q2** [2 marks]

A processor is running a program when a device sends an interrupt signal.

State when the processor checks for the interrupt, and state what the processor does with the contents of its registers before the interrupt service routine (ISR) runs.

### Q3 — hard — 4 marks

**Q3** [4 marks]

A software company writes one program. It compiles the program twice: once to run on a RISC processor and once to run on a CISC processor.

The compiled program for the RISC processor contains many more machine instructions than the compiled program for the CISC processor.

Explain why, referring to the features of the two types of processor.

### Q4 — medium — 3 marks

**Q4** [3 marks]

The table shows three features of a RISC processor.

Complete the table by giving the matching feature of a CISC processor.

| Feature | RISC processor | CISC processor |
|---|---|---|
| Instruction length | Fixed length |   |
| Clock cycles needed for one instruction | One clock cycle |   |
| Number of general-purpose registers | Many |   |

### Q5 — easy — 2 marks

**Q5** [2 marks]

Reduced Instruction Set Computers (RISC) and Complex Instruction Set Computers (CISC) are two types of processor.

State **two** differences between a RISC processor and a CISC processor.

### Q6 — hard — 4 marks

**Q6** [4 marks]

A RISC processor uses pipelining. The processing of each instruction is divided into five stages:

- instruction fetch (IF)
- instruction decode (ID)
- operand fetch (OF)
- instruction execute (IE)
- write back result (WB)

A program consists of five instructions, labelled A, B, C, D and E. The instructions enter the pipeline in that order.

Complete the table to show how the five instructions are processed. Write the label of an instruction in a cell to show that the instruction is at that stage during that clock cycle. Leave a cell empty if no instruction is at that stage during that clock cycle.

| Processor stages | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IF |   |   |   |   |   |   |   |   |   |   |   |
| ID |   |   |   |   |   |   |   |   |   |   |   |
| OF |   |   |   |   |   |   |   |   |   |   |   |
| IE |   |   |   |   |   |   |   |   |   |   |   |
| WB |   |   |   |   |   |   |   |   |   |   |   |

### Q7 — hard — 4 marks

**Q7** [4 marks]

A computer system checks one set of readings taken from a machine in a factory.

The system has three processors. All three processors work on that same set of readings at the same time. Each processor carries out a different set of checks on the readings.

**(a)** Identify the computer architecture used by this system. **[1]**

**(b)** The system is changed. Each of the three processors is now given its own separate set of readings. Each processor still carries out a different set of checks.

Explain what the computer architecture of the changed system is, and why the architecture has changed. **[3]**

### Q8 — hard — 6 marks

**Q8** [6 marks]

An organisation downloads software from sources it does not know. Before the software is installed on the computers that staff use, it is tested.

Each test is carried out inside a virtual machine on a single host computer.

Describe **two** benefits and **one** limitation of testing the software in this way.

### Q9 — medium — 3 marks

**Q9** [3 marks]

When pipelining is used, the processing of each instruction is divided into five stages:

- instruction fetch (IF)
- instruction decode (ID)
- operand fetch (OF)
- instruction execute (IE)
- write back result (WB)

Explain how these five stages are used when a RISC processor pipelines three consecutive instructions.

### Q10 — medium — 3 marks

**Q10** [3 marks]

Three computer systems are described below.

**System 1**

The system has one processor. The processor carries out the instructions of a program one after another. Each instruction works on one item of data.

**System 2**

The system has four processors. At any moment, all four processors are carrying out the same instruction. Each processor carries out that instruction on a different set of data.

**System 3**

The system has four processors. At any moment, each processor is carrying out a different instruction. Each processor works on its own separate set of data.

Identify the computer architecture used by each of the three systems.

### Q11 — easy — 2 marks

**Q11** [2 marks]

A Reduced Instruction Set Computer (RISC) processor inside a network router uses pipelining.

Describe the effect of pipelining on the way this processor handles a sequence of instructions.

### Q12 — medium — 3 marks

**Q12** [3 marks]

A research centre has a set of programs that were written many years ago. The programs were written for a computer system that is no longer manufactured. The programs will not run on the research centre's current computers.

The research centre installs virtual machine software on one of its current computers so that the programs can be used again.

Explain how the virtual machine allows these programs to run.

### Q13 — easy — 2 marks

**Q13** [2 marks]

There are four basic categories of computer architecture. Each category is known by an abbreviation.

Complete the table by writing the full name of each of the two missing categories.

| Abbreviation | Full name |
|---|---|
| SISD | Single Instruction, Single Data |
| SIMD | Single Instruction, Multiple Data |
| MISD |   |
| MIMD |   |

### Q14 — easy — 2 marks

**Q14** [2 marks]

A company installs virtual machine software on one of its computers.

Describe what is meant by a virtual machine.

### Q15 — medium — 3 marks

**Q15** [3 marks]

An organisation installs a massively parallel computer. It uses the computer to process one very large set of data.

Explain how the processors in this computer are able to work together on the single task.

### Q16 — easy — 2 marks

**Q16** [2 marks]

A massively parallel computer is one kind of high-performance computer system.

State what is meant by a massively parallel computer.

### Q17 — medium — 7 marks

**Q17** [4 marks]

Outline **two **benefits and **two **limitations of a virtual machine.

*Source: June 2024 9618/32 Q9A*


**Q17** [3 marks]

Explain the roles of the host operating system and the guest operating system as used in a computer system running a virtual machine.

*Source: June 2024 9618/32 Q9B*


### Q18 — medium — 8 marks

**Q18** [2 marks]

Reduced Instruction Set Computers (RISC) and Complex Instruction Set Computers (CISC) are two types of processor.

State **two **features of RISC processors.

*Source: June 2024 9618/31 Q11A*


**Q18** [3 marks]

Outline the process of interrupt handling as it could be applied to RISC or CISC processors.

*Source: June 2024 9618/31 Q11B*


**Q18** [3 marks]

Explain how pipelining affects interrupt handling for RISC processors.

### Q19 — medium — 4 marks

**Q19** [4 marks]

Complex Instruction Set Computer (CISC) is a type of processor.

Identify **four **features of a CISC processor.

*Source: Nov 2024 9618/32 Q8*


### Q20 — medium — 4 marks

**Q20** [4 marks]

Reduced Instruction Set Computers (RISC) is a type of processor.

Identify **four **features of a RISC processor.

*Source: Nov 2024 9618/31 Q2*


### Q21 — medium — 4 marks

**Q21** [4 marks]

Describe the features of the SIMD and MISD computer architectures.

SIMD

MISD

*Source: November 2023 9618/32 Q10*


### Q22 — medium — 4 marks

**Q22** [4 marks]

Describe the features of SISD and MIMD computer architectures.

SISD

MIMD

*Source: November 2023 9618/31 Q5*

