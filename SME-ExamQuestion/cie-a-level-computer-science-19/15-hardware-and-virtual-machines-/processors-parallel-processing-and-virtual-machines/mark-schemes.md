# Mark Schemes — Processors, Parallel Processing & Virtual Machines
**15. Hardware & Virtual Machines** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (22 questions)


### Q1
When the interrupt is detected, the status of each register is stored on the stack. **[1]**

The interrupt service routine (ISR) is then executed. **[1]**

When the ISR has finished, the register contents are restored from the stack to the status they had before the interrupt was detected, so the interrupted program continues with the next instruction in the sequence. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for when the interrupt is detected, the status or contents of each register is stored on the stack
> 
> **1 mark** for the interrupt service routine (ISR) is then executed
> 
> **1 mark** for when the ISR has finished, the register contents are restored from the stack to the status they had before the interrupt was detected
> 
> **1 mark** for the interrupted program then continues with the next instruction in the sequence
> 
> **Max 3 marks.**
> 
> Accept "pushed onto the stack" and "popped off the stack" for storing and restoring.
> 
> Accept "control is passed back to the interrupted program" for the final marking point.
> 
> Accept, as an alternative to the final marking point, that the processor first checks for any further interrupt of higher priority before it continues.
> 
> Do not accept that the interrupted program starts again from the beginning. The whole purpose of storing the register status is that the program resumes from the point it had reached.

> **[exam-tip]**
> Many students describe the first half of this process well and then stop at "the ISR runs". The marks at the end are for putting the register contents back and resuming the interrupted program, so always write the restore step.
> 
> Be careful with the word "program". The stack does not hold the program. It holds the status of the registers, which is what the processor needs in order to pick the program up again.

### Q2
The processor checks for an interrupt at the start or the end of a fetch-execute cycle. **[1]**

The status of each register is stored on the stack. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the processor checks for an interrupt at the start or the end of a fetch-execute cycle
> 
> **1 mark** for the status or contents of each register is stored on the stack
> 
> Accept, for the first marking point, "at the end of the current fetch-execute cycle", or "at the start of the next fetch-execute cycle".
> 
> Accept, for the second marking point, "the state of the current program is saved on the stack", or "the register contents are pushed onto the stack".
> 
> Do not accept that the processor stops immediately, or part-way through an instruction. The interrupt is not acted on until the current fetch-execute cycle has finished.

> **[exam-tip]**
> The most common error is writing that the processor "stops straight away". It does not. The current fetch-execute cycle is completed first, and only then is the interrupt acted on. Saying this precisely is what earns the mark.
> 
> The second mark is for the registers specifically. "The program is saved" is too vague; "the status of each register is stored on the stack" is the wording Cambridge credits.

### Q3
A CISC processor has a large instruction set, while a RISC processor has a small, reduced instruction set. **[1]**

Each CISC instruction is complex, so one CISC instruction can carry out an operation that a RISC processor needs several simple instructions to complete. **[1]**

A RISC processor uses only load and store instructions to address memory, so extra instructions are needed to move data between memory and the registers, while a CISC processor has many types of instruction that address memory directly. **[1]**

The design emphasis on a RISC processor is on the software, so the compiler has to do more of the work, while the design emphasis on a CISC processor is on the hardware. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for CISC has a large instruction set // RISC has a small or reduced instruction set
> 
> **1 mark** for CISC instructions are complex and one of them does the work of several simple RISC instructions // RISC instructions are simple and each carries out one basic operation
> 
> **1 mark** for RISC uses only load and store instructions to address memory, so extra instructions are needed to move data between memory and registers // CISC has many types of instruction that address memory directly
> 
> **1 mark** for the design emphasis on RISC is on the software // the design emphasis on CISC is on the hardware
> 
> Accept, for the second marking point, that a CISC instruction is converted into sub-instructions inside the processor, so the work is done by the hardware rather than by extra instructions in the program.
> 
> Accept, for the fourth marking point, that the compiler for a RISC processor has to do more work, or is more complex.
> 
> Do not accept "RISC is slower" or "CISC is faster". The question is about the number of instructions in the compiled program, not about speed, and neither claim appears in a mark scheme.

> **[exam-tip]**
> This question rewards the link, not the list. Writing "RISC has a small instruction set" earns one mark; writing why a small instruction set forces the compiler to produce more instructions earns the rest. Every sentence you write should contain the word "so" or "because".
> 
> Watch the direction of the argument. A RISC program needs more instructions, and that is why a RISC processor makes more use of RAM. Students often reverse this and claim RISC programs are smaller because the instructions are simpler.

### Q4
| Feature | RISC processor | CISC processor |
|---|---|---|
| Instruction length | Fixed length | **Variable length** **[1]** |
| Clock cycles needed for one instruction | One clock cycle | **More than one clock cycle** **[1]** |
| Number of general-purpose registers | Many | **Few** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for variable length
> 
> **1 mark** for more than one clock cycle
> 
> **1 mark** for few
> 
> Accept variable format, or multi-operation instructions, for the first row.
> 
> Accept multi-cycle, several clock cycles, or many clock cycles for the second row. Accept an answer that says a CISC instruction is converted into sub-instructions that each take a clock cycle.
> 
> Accept fewer, or a small number, for the third row.
> 
> Do not accept "longer instructions" for the first row on its own. CISC instructions are not all long; the point is that their length is not fixed.

> **[exam-tip]**
> Row two is where marks are lost. Students write "slower" instead of "more than one clock cycle". Speed is not the feature being asked for, and a mark scheme built on clock cycles will not credit it. Answer in the same units as the RISC column you have been given.
> 
> A useful check: read your completed row back as a single sentence. "RISC uses fixed-length instructions and CISC uses variable-length instructions" makes sense. "RISC uses fixed-length instructions and CISC is more complicated" does not, so it will not earn the mark.

### Q5
A RISC processor has a smaller instruction set, while a CISC processor has a larger instruction set. **[1]**

A RISC processor uses fixed-length instructions, while a CISC processor uses variable-length instructions. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from**, one mark for each difference:
> 
> - RISC has fewer instructions // CISC has more instructions
> - RISC instructions are simpler // CISC instructions are more complex
> - RISC uses fixed-length instructions // CISC uses variable-length instructions
> - RISC has few instruction formats // CISC has many instruction formats
> - RISC usually uses single-cycle instructions // CISC uses multi-cycle instructions
> - RISC has many general-purpose registers // CISC has few general-purpose registers
> - RISC has fewer addressing modes // CISC has more addressing modes
> - RISC requires less complex circuits // CISC requires more complex circuits
> - RISC has a hard-wired control unit // CISC has a programmable control unit
> - RISC only uses load and store instructions to address memory // CISC has many types of instruction to address memory
> - RISC makes more use of RAM // CISC makes more use of cache
> - Pipelining is straightforward to apply on RISC // pipelining is harder to apply on CISC
> - The design emphasis on RISC is on the software // the design emphasis on CISC is on the hardware
> 
> **[2 marks]**
> 
> Accept the difference written either way round, and accept it split across two sentences.
> 
> Accept a statement about one processor type where the comparison is implied, for example "RISC uses fixed-length instructions". Do not accept two statements that make the same point, one about each processor.

> **[exam-tip]**
> The mark here is for a difference. Cambridge credits one side on its own, such as "RISC uses fixed-length instructions", because the comparison with CISC is implied. Writing both halves makes the difference certain, so train yourself to write every answer as one sentence with two halves. Do not spend your two answers on one point, such as "RISC has fewer instructions" and then "CISC has more instructions".
> 
> The pair most often reversed is the registers. RISC has many general-purpose registers and CISC has few. Note also that comparisons of cost, power use, or the devices each processor is found in do not appear in Cambridge mark schemes, so keep to the architectural differences above.

### Q6
| Processor stages | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IF | **A** | **B** | **C** | **D** | **E** |   |   |   |   |   |   |
| ID |   | **A** | **B** | **C** | **D** | **E** |   |   |   |   |   |
| OF |   |   | **A** | **B** | **C** | **D** | **E** |   |   |   |   |
| IE |   |   |   | **A** | **B** | **C** | **D** | **E** |   |   |   |
| WB |   |   |   |   | **A** | **B** | **C** | **D** | **E** |   |   |

Instruction `A` enters the pipeline in clock cycle 1 and is written back in clock cycle 5. **[1]**

Each later instruction starts one clock cycle after the one before it. **[1]**

Instruction `E` is written back in clock cycle 9, so all five instructions are processed by the end of clock cycle 9. **[1]**

Clock cycles 10 and 11 are not needed and every cell in them stays empty. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for instruction `A` at stage `IF` in clock cycle 1, and no other entry anywhere in clock cycle 1
> 
> **1 mark** for instruction `A` passing through all five stages in clock cycles 1 to 5, one stage per clock cycle
> 
> **1 mark** for instructions `B`, `C`, `D` and `E` each starting one clock cycle later than the instruction before, so that every row is the row above shifted one column to the right
> 
> **1 mark** for no entries at all in clock cycles 10 and 11
> 
> Accept the numbers 1 to 5 in place of the labels `A` to `E`.
> 
> Accept the alternative form Cambridge uses, in which each cell holds the instruction number and the stage number. The first cell then reads `1.1` and the cell for clock cycle 9 on row `WB` reads `5.5`.
> 
> Do not accept a table in which two different instructions appear in the same row in the same clock cycle. One stage cannot process two instructions at once.
> 
> Do not accept a table in which the same instruction appears in two different stages in the same clock cycle.

> **[exam-tip]**
> The completed table is a staircase. Every row is the row above it shifted one column to the right. Fill in the `IF` row first, then step down and across, and the rest of the table follows without any counting.
> 
> Two errors lose marks here. The first is filling the table right to the last column. The table is deliberately wider than this program needs, so clock cycles 10 and 11 must be left empty. The second is starting all five rows in clock cycle 1, which would mean one instruction was being fetched and written back at the same moment.

### Q7
**(a)** MISD **[1]**

**(b)** The changed system uses MIMD. **[1]**

The three processors still carry out different instructions, as each one runs a different set of checks, so the instruction half of the name stays as Multiple. **[1]**

Each processor now works on a different set of data instead of all three using the same set of data, so the data half of the name changes from Single to Multiple. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for (a) MISD // Multiple Instruction, Single Data
> 
> **1 mark** for (b) MIMD // Multiple Instruction, Multiple Data
> 
> **1 mark** for (b) the processors still carry out different instructions // the instruction half of the name is unchanged // both architectures use many processors running different instructions
> 
> **1 mark** for (b) each processor now uses a different data set // the processors no longer share the same data set // the data half of the name changes from Single to Multiple
> 
> Accept "data stream" in place of "data set" throughout.
> 
> Do not accept "there are now more processors" as the reason. There are three processors in both systems, and the number of processors is not what the name records.
> 
> Do not accept SIMD for (b). The three processors carry out different sets of checks, so more than one instruction is in use.

> **[exam-tip]**
> MISD and MIMD differ in one thing only: whether the processors all work on a single shared set of data or each work on their own. You lose the last mark here if you write something that is true of both, such as "the processors work independently".
> 
> Name the thing that actually changed. Say that the set of data was shared and is now separate, and use the words Single and Multiple so the examiner can see which half of the name you mean.

### Q8
Benefit 1: If the downloaded software contains a virus, or causes a crash, only the virtual machine is affected. **[1]** The guest operating system has no effect on anything outside the virtual machine, so the host computer and the staff computers are protected. **[1]**

Benefit 2: The organisation does not need to buy extra computers to test on. **[1]** Several virtual machines can be run on the same host computer at the same time. **[1]**

Limitation: The performance of the software cannot be measured accurately inside a virtual machine. **[1]** The guest operating system shares the processor time and memory of the host computer, so the response times obtained are not those of a real machine. **[1]**

**[6 marks]**

> **[mark-scheme]**
> **Two marks for each benefit description, maximum 4. One mark for the point and one mark for the development.**
> 
> **Any two from:**
> 
> - PROTECTION: only the virtual machine is affected if the software has a virus or causes a crash (1) because the guest operating system has no effect on anything outside the virtual machine, so the host computer is protected (1)
> - COST: no extra computers or hardware need to be bought for testing (1) because several virtual machines can be run on the same host computer (1)
> - COMPATIBILITY: the software can be tried on several different operating systems (1) by running a different guest operating system in each virtual machine on the same hardware (1)
> 
> **[4 marks]**
> 
> **Two marks for the limitation description, maximum 2.**
> 
> **Any one from:**
> 
> - PERFORMANCE: the performance of the software cannot be measured accurately (1) because the guest operating system shares the processor time and memory of the host computer, so response times are not those of a real machine (1)
> - HARDWARE: some hardware cannot be emulated by a virtual machine (1) so software that needs that hardware cannot be tested, and some of the host computer's hardware cannot be accessed directly (1)
> - COMPLEXITY: the virtual machine is expensive and time consuming to set up and maintain (1) because both the host system and the virtual machine have to be maintained (1)
> 
> **[2 marks]**
> 
> Do not accept two benefits that make the same point, for example "the host is protected" and "the host is easier to recover after a crash". These are credited once only.
> 
> Do not accept "the virtual machine cannot catch a virus". A virtual machine can be infected; the point is that the infection is confined to it.

> **[exam-tip]**
> Each of the three sections here is worth two marks, not one, so a bald statement such as "the host computer is protected" scores half of what is available. Every point needs a reason attached to it, and the reason has to say something the point did not.
> 
> Watch the split as well. Two benefits and one limitation means four marks and two marks; writing three benefits wastes the time spent on the third and leaves two marks unclaimed.

### Q9
Each stage, also called a subtask, is completed during one clock cycle, so one instruction takes five clock cycles to pass through the pipeline. **[1]**

No two instructions can be at the same stage during the same clock cycle. **[1]**

So the second instruction begins `IF` in clock cycle 2, while the first instruction has already moved on to `ID`. In clock cycle 3 the third instruction begins `IF`, the second instruction is at `ID` and the first instruction is at `OF`. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - Each stage / subtask is completed during one clock cycle
> - No two instructions can be at the same stage during the same clock cycle
> - While one instruction is being decoded, the next instruction can be fetched
> - The second instruction begins in the second clock cycle, while the first instruction has moved on to its second subtask
> - The third instruction begins in the third clock cycle, while the first and second instructions have moved on to their third and second subtasks
> 
> **[3 marks]**
> 
> Accept `subtask` in place of `stage` anywhere in the answer.
> 
> Accept a correctly labelled table of stages against clock cycles in place of prose, provided the instructions are staggered by one clock cycle.
> 
> Do not accept "each instruction is completed in one clock cycle". One stage takes one clock cycle, so one instruction takes five.

> **[exam-tip]**
> This question is about timing, not about processor design. Answers that list fixed-length instructions, a small instruction set and many registers are explaining why a RISC processor pipelines well, and they score nothing here.
> 
> The single costliest error is writing that each instruction takes one clock cycle. One stage takes one clock cycle, so one instruction takes five. Tie every point to a numbered clock cycle and name which instruction is at which stage in it, and the marks follow.

### Q10
System 1: SISD **[1]**

System 2: SIMD **[1]**

System 3: MIMD **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for System 1 = SISD
> 
> **1 mark** for System 2 = SIMD
> 
> **1 mark** for System 3 = MIMD
> 
> Accept the full name in place of the abbreviation, for example Single Instruction, Multiple Data for System 2.
> 
> Do not accept MISD for System 2. System 2 uses one instruction at a time across all four processors, so the instruction half of the name must be Single.
> 
> Do not accept MISD for System 3. Each processor in System 3 has its own separate set of data, so the data half of the name must be Multiple.

> **[exam-tip]**
> Counting the processors does not give you the answer. SIMD, MISD and MIMD all have more than one processor, so "four processors" on its own never decides between them.
> 
> Work through each description twice. The first time, ask how many different instructions are being carried out at that moment. The second time, ask how many different sets of data are being used. Those two answers give you the two halves of the name, in that order.

### Q11
Pipelining allows several instructions to be processed at the same time, because each instruction in the sequence is at a different stage. **[1]**

This increases the instruction throughput, which is the number of instructions the processor completes per unit of time. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for pipelining allows several instructions to be processed simultaneously / concurrently
> 
> **1 mark** for the instruction throughput is increased // more instructions are completed per unit of time
> 
> Accept "more than one instruction is being worked on at once" for the first mark.
> 
> Accept "more instructions are finished in the same amount of time" for the second mark.
> 
> Do not accept "each instruction is completed faster". Pipelining does not shorten any single instruction. The first instruction still passes through every stage before it finishes.
> 
> Do not accept a list of RISC features such as fixed-length instructions or many general purpose registers. Those explain why a RISC processor pipelines well, not what pipelining does.

> **[exam-tip]**
> Two marks means two separate points, not one point written twice. Most answers reach "several instructions at once" and then stop, so they score one mark out of two. Always say what that overlap buys the processor: more instructions completed per unit of time.
> 
> The second common error is claiming that pipelining makes an individual instruction finish sooner. It does not. The gain comes entirely from overlapping different instructions, so the word to reach for is throughput.

### Q12
The virtual machine software emulates the hardware of the old computer system on the research centre's current computer. **[1]**

A guest operating system that the old programs are compatible with is then run inside the virtual machine. **[1]**

The programs run under that guest operating system, which reaches the real hardware of the current computer through the virtual machine and the host operating system. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the virtual machine emulates the hardware / the instruction set of the old computer system
> 
> **1 mark** for a guest operating system that the programs are compatible with runs inside the virtual machine
> 
> **1 mark** for the programs run under the guest operating system, which accesses the actual hardware through the virtual machine and the host operating system
> 
> Accept for the third mark: the host operating system keeps control of the physical resources of the current computer and runs the virtual machine software.
> 
> Accept "emulates the old computer system" for the first mark.
> 
> Do not accept "the programs are recompiled / rewritten for the new computer". No translation of the programs takes place; the old system is emulated instead.
> 
> Do not accept "the programs are stored in the cloud". Cloud computing is a separate topic and does not make incompatible programs run.

> **[exam-tip]**
> This question asks how, so a list of benefits earns nothing. If you write "it is cheaper than buying the old computer", you have answered a different question.
> 
> Build the answer as a chain: the virtual machine emulates the old hardware, a compatible guest operating system runs inside it, and the programs then run under that guest operating system. Naming both operating systems, guest and host, is what separates a three-mark answer from a one-mark answer.

### Q13
| Abbreviation | Full name |
|---|---|
| SISD | Single Instruction, Single Data |
| SIMD | Single Instruction, Multiple Data |
| MISD | **Multiple Instruction, Single Data** **[1]** |
| MIMD | **Multiple Instruction, Multiple Data** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for MISD = Multiple Instruction, Single Data
> 
> **1 mark** for MIMD = Multiple Instruction, Multiple Data
> 
> Accept the word "architecture" added to the end of either name.
> 
> Accept "stream" or "streams" added after "Data", for example Multiple Instruction, Single Data stream.
> 
> Accept the words written without the comma.
> 
> Do not accept Multiple Instruction, Multiple Data for MISD, or Multiple Instruction, Single Data for MIMD. The third letter gives the data half of the name, so the two names are not interchangeable.

> **[exam-tip]**
> Read each abbreviation as two pairs of letters. The first pair tells you how many different instructions are in use, the second pair tells you how many different sets of data are in use.
> 
> MISD is the one you are most likely to write incorrectly, because the letter M appears twice in MIMD and only once in MISD. If you write "Multiple Instruction, Multiple Data" for MISD you have described a different architecture and you score nothing, even though you clearly knew what the letters stood for.

### Q14
A virtual machine is the emulation of a complete computer system, its hardware and its software, by software running on another computer. **[1]**

The computer that the emulation runs on is the host computer system, and a guest operating system runs inside the virtual machine. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the emulation of a computer system // emulating the hardware and/or the software of a computer system
> 
> **1 mark** for the emulation runs on a host computer system // a guest operating system runs inside it / is used for the emulation
> 
> Accept "simulation of a computer system" for the first mark.
> 
> Accept "the host machine" for "the host computer system".
> 
> Do not accept a description of virtual memory, for example "part of the hard disk used as if it were RAM". Virtual memory is a memory management method and is a different idea.
> 
> Do not accept the brand name of a piece of virtual machine software on its own. The front cover of this paper states that no marks are awarded for brand names of software packages or hardware.

> **[exam-tip]**
> Two words earn the marks on this question: emulation, and host. Make sure you describe what a virtual machine is, not what it lets you do: an answer such as "it lets you run two operating systems at once" is a use, not a description.
> 
> The other frequent loss is confusing a virtual machine with virtual memory. Both are on the A Level syllabus and the names look alike, but virtual memory is about managing RAM and has nothing to do with emulating a computer system.

### Q15
The task is divided up so that the processors simultaneously perform a set of coordinated computations, with each processor handling part of the same problem. **[1]**

The processors, which may sit in separate computers, are joined together by a network infrastructure. **[1]**

They communicate across that network using a message interface, sending messages to one another so that the partial results can be brought together. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for simultaneously performing a set of coordinated computations // collaborative processing // each processor works on part of the same problem at the same time
> 
> **1 mark** for (the processors are connected by) a network infrastructure
> 
> **1 mark** for they communicate using a message interface // they communicate by sending messages
> 
> Accept "the processors pass messages between themselves" for the third mark.
> 
> Accept "the results produced by the separate processors are combined" as an alternative wording of the first mark.
> 
> Do not accept "the processors all read and write one shared block of memory" as the communication method. The credited mechanism on this syllabus is a network infrastructure with a message interface.
> 
> Do not accept "the operating system schedules the processes". Scheduling belongs to a different part of the syllabus and does not answer this question.

> **[exam-tip]**
> The credited answer here is about a network and about messages. Many students instead write that all the processors share one block of memory, which describes a single multi-core computer and earns nothing on this topic. Say that the machines are linked by a network infrastructure and pass messages to each other.
> 
> Keep this separate from the four categories of computer architecture. Naming SISD, SIMD, MISD or MIMD does not explain how a massively parallel system works, and no mark is available for it here.

### Q16
A massively parallel computer uses a large number of processors, or a large number of separate computers connected together. **[1]**

These processors simultaneously perform a set of coordinated computations, so they all work on the same problem at the same time. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for a large number of processors // a large number of separate computers connected together
> 
> **1 mark** for simultaneously performing a set of coordinated computations // collaborative processing // all the processors work on the same problem at the same time
> 
> Accept "many processors", "thousands of processors" or "several computers linked together" for the first mark. The mark is for the scale of the system, not for any particular number.
> 
> Accept "the computers are joined by a network infrastructure" or "the processors communicate by sending messages" in place of either mark point, as both are credited characteristics of these systems.
> 
> Do not accept "it is faster than a normal computer" on its own. Speed is a result of the design, not a characteristic of it.
> 
> Do not accept a description of a single computer holding two or four cores. That is not the scale this term describes.

> **[exam-tip]**
> The most common error here is describing an ordinary multi-core computer. The word massively means a very large number of processors, and in many of these systems the processors sit in separate computers joined by a network rather than inside one box.
> 
> Give the two ideas separately: how many processors there are, and the fact that they all work on one problem at the same time. An answer that only says the machine is powerful or fast earns nothing.

### Q17
> **[mark-scheme]**
> **One **mark per mark point for up to **two **benefits (**Max 2**)
> 
> MP1 COMPATIBILTY e.g. Applications that aren’t compatible with the host computer can be run on the virtual machine // It is possible to emulate old software on a new system by running a compatible guest operating system as a virtual machine // Software can be tried on different OS on the same hardware.
> 
> MP2 PROTECTION e.g. The guest operating system has no effect on anything outside the virtual machine other virtual machines or the host computer // Virtual machines are useful for testing as they will not crash the host computer if something goes wrong // Easier to recover if software causes a system crash as virtual machine software protects the host system.
> 
> MP3 COST e.g. No need to buy extra computers / hardware as multiple virtual machines can be implemented on the same hardware.
> 
> **One **mark per mark point for up to **two **limitations (**Max 2**)
> 
> MP4 PERFORMANCE e.g. The performance of the guest operating system will not be as good on a virtual machine as it would be on its own compatible machine because of the extra code / using more RAM/memory space // The performance of the VM is dependent on the capabilities of the host computer // Response times cannot be accurately measured using a virtual machine.
> 
> MP5 COMPLEXITY e.g. Building an in-house virtual machine can be expensive, time consuming and complex to maintain / set-up.
> 
> MP6 HARDWARE/SOFTWARE ISSUES e.g. Some hardware/software can’t be emulated with a virtual machine // Some of the host machine’s hardware can’t be directly accessed by the virtual machine.
> **[mark-scheme]**
> **One **mark per mark point – host operating system (**Max 2**)
> 
> MP1 The host operating system is the normal operating system for the host computer / machine.
> 
> MP2 It has control of all the resources of the host computer / machine. // It can access the physical resources of the host computer / machine.
> 
> MP3 It provides a user interface to operate the virtual machine software.
> 
> MP4 It also runs the virtual machine software.
> 
> **One **mark per mark point – guest operating system (**Max 2**)
> 
> MP5 The guest operating system runs within the virtual machine.
> 
> MP6 … it controls the virtual hardware/software during the emulation. // It accesses the actual hardware through the virtual machine and host operating system.
> 
> MP7 It provides a virtual user interface for the emulated hardware/software.
> 
> MP8 The guest operating system runs under the control of the host operating system.

### Q18
> **[mark-scheme]**
> **One **mark per mark point **(Max 2**)
> 
> MP1 Uses **hard-wired code/control units**
> 
> MP2 Uses relatively few instructions / simple instructions
> 
> MP3 Uses relatively few addressing modes
> 
> MP4 Makes use of a single-cycle for each instruction
> 
> MP5 Makes use of fixed length / fixed format instructions
> 
> MP6 Makes use of general-purpose registers
> 
> MP7 Pipelining is **straightforward to apply**
> 
> MP8 The design emphasis is on the **software**
> 
> MP9 Processor chips require few transistors.
> **[mark-scheme]**
> **One **mark per mark point (**Max 3**)
> 
> MP1 Once the processor detects an interrupt at the start/end of the fetch-execute cycle
> 
> MP2 … the current program is temporarily stopped and the **status of each register** stored on the stack.
> 
> MP3 After the interrupt has been serviced/the Interrupt Service Routine (ISR) has been executed …
> 
> MP4 … the **registers **can be restored to its original status before the interrupt was detected // … the data can be restored **from the stack**.
> **[mark-scheme]**
> **One **mark per mark point (**Max 3**)
> 
> MP1 Pipelining adds an additional complexity // there could be a number of instructions still in the pipeline when the interrupt is received
> 
> MP2 All the instructions currently in operation are usually discarded except for the last one/the one at write back
> 
> MP3 … the interrupt handler routine is applied to the remaining instruction.
> 
> MP4 Once the interrupt has been serviced the processor can restart with the next instruction in the sequence.

### Q19
> **[mark-scheme]**
> **One **mark per mark point (**Max 4**)
> 
> MP1 many instruction formats possible
> 
> MP2 large instruction set
> 
> MP3 many addressing modes available
> 
> MP4 uses variable length/multi-operation instructions
> 
> MP5 multi-clock cycle instructions
> 
> MP6 complex decoding of instructions
> 
> MP7 uses complex circuits
> 
> MP8 makes frequent use of cache memory
> 
> MP9 uses programmable control unit // uses micro-programmed control unit // uses hardwired control unit
> 
> MP10 hardware needs to be able to handle more complex instructions convert into sub-instructions // Design emphasis is on the hardware.

### Q20
> **[mark-scheme]**
> **One **mark per mark point (**Max 4**)
> 
> MP1 low number of instruction formats // low number of instruction sets
> 
> MP2 uses single-clock cycle instructions
> 
> MP3 uses fixed length instructions
> 
> MP4 uses many general-purpose registers
> 
> MP5 works well with pipelining
> 
> MP6 hard-wired control unit
> 
> MP7 makes extensive use of RAM
> 
> MP8 uses a low number of addressing modes
> 
> MP9 the design emphasis is on the software

### Q21
> **[mark-scheme]**
> **One** mark per mark point – SIMD **(Max 2) **
> 
> - MP1 Single Instruction, Multiple Data (architecture) // Performs the same operation on multiple different data streams simultaneously.
> - MP2 The instructions can be performed sequentially, taking advantage of pipelining.
> - MP3 Parallel computers with multiple processors.
> 
> **One** mark per mark point – MISD **(Max 2) **
> 
> - MP4 Multiple Instruction, Single Data (architecture) // Performs different operations on the same data stream.
> - MP5 Each processor works on the same data stream independently.
> - MP6 Parallel computers with multiple processors.

### Q22
> **[mark-scheme]**
> **One** mark per mark point – SISD **(Max 2)**
> 
> - MP1    Single Instruction, Single Data (architecture). // Data is taken from a single source and a single instruction is performed on the data.
> - MP2    Contains one processor, a control unit and a memory unit.
> - MP3    …that executes instructions sequentially.
> 
> **One** mark per mark point – MIMD **(Max 2) **
> 
> - MP4    Multiple Instruction, Multiple Data (architecture). // At any time, any processor can execute different instructions on different sets of data.
> - MP5    Contains many processors
> - MP6    …that operate asynchronously / independently.
