# Mark Schemes — Central Processing Unit (CPU) Architecture
**4. Processor Fundamentals** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (43 questions)


### Q1
(i) Number of locations = 2 to the power of 20 **[1]**

= 1 048 576 memory locations **[1]**

(ii) 1 048 576 bytes / 1024 = 1024 kibibytes, and 1024 kibibytes / 1024 = 1 **[1]**

= 1 mebibyte **[1]**

**[4 marks]**

> **[mark-scheme]**
> (i) **1 mark** for the working: 2^20 // 2 to the power of 20
> 
> **1 mark** for the answer: 1 048 576 locations
> 
> (ii) **1 mark** for the working: 1 048 576 / 1024 / 1024
> 
> **1 mark** for the answer: 1 mebibyte
> 
> Accept 1 048 576 written as 1048576 or 1,048,576.
> 
> Do not accept 65 536 in (i). That is 2 to the power of 16 and uses the width of the data bus. It is the width of the address bus that decides how many locations can be addressed.
> 
> Do not accept 1.048576 in (ii). That is the answer in megabytes. The question asks for mebibytes, so divide by 1024 twice, not by 1000 twice.

> **[exam-tip]**
> Read carefully which bus each number belongs to. The number of addressable locations comes from the address bus width alone. The data bus width tells you how much data moves in one transfer and does not appear anywhere in this calculation, so it is there to catch you out.
> 
> Then check the unit word. A mebibyte uses a binary prefix, so you divide by 1024 twice. A megabyte uses a decimal prefix and would need division by 1000 twice, which gives a different answer.

### Q2
| Bus | What the bus carries | Effect of increasing the width of this bus |
|---|---|---|
| Data bus | Data being transferred between the processor and memory | **More bits of data can be transferred at the same time, so fewer transfers are needed and data transfer is faster** **[1]** |
| Address bus | **The address of the memory location that is to be read from or written to** **[1]** | **More memory locations can be directly addressed, so a larger amount of memory can be used** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the effect of a wider data bus: more bits of data transferred at the same time // fewer transfers needed for the same amount of data
> 
> **1 mark** for what the address bus carries: the address of the memory location that is to be read from or written to
> 
> **1 mark** for the effect of a wider address bus: more memory locations can be directly addressed // a larger amount of memory can be used
> 
> Accept for the address bus row "the address held in the Memory Address Register (MAR) is carried to memory"
> 
> Do not accept "the address bus carries data". The address bus carries addresses only, and it carries them in one direction, from the processor to memory
> 
> Do not accept "a wider address bus transfers more data at a time". That is the effect of a wider data bus

> **[exam-tip]**
> The commonest error in this whole topic is treating the two buses as one. A wider data bus moves more data in each transfer. A wider address bus moves no extra data at all; it simply lets the processor reach more memory locations.
> 
> If a question asks about "bus width" without telling you which bus, say which one you are writing about before you describe the effect.

### Q3
(i) 32 bits of data can be carried by the bus at the same time, in a single transfer. **[1]**

(ii) 64 bits can now be transferred at a time, so twice as much data is moved in each transfer and fewer transfers are needed. **[1]**

**[2 marks]**

> **[mark-scheme]**
> (i) **1 mark** for 32 bits being transferred / carried at the same time // in one transfer
> 
> (ii) **1 mark** for more data being transferred at a time // 64 bits instead of 32 bits per transfer // fewer transfers being needed for the same amount of data
> 
> Accept in (i) "the bus has 32 parallel lines, one for each bit"
> 
> Do not accept in (ii) "the computer can store more data". Bus width affects how much data is transferred at once, not how much can be stored
> 
> Do not accept in (ii) "the computer becomes twice as fast". Only the transfer of data on that bus is affected, not the whole system

> **[exam-tip]**
> Bus width is measured in bits and it describes how much data moves in one transfer. It says nothing about how much data the computer can store.
> 
> Keep the data bus and the address bus apart in your head. The width of the data bus controls how much data moves at once; the width of the address bus controls how many memory locations can be reached.

### Q4
Cache memory stores the data and instructions that are used most frequently. **[1]**

Program A uses the same instructions and data over and over, so after the first use they are already held in the cache. **[1]**

They are then read at the faster cache access speed rather than from the slower RAM, and that time is saved on every repeat. **[1]**

Program B reads each record only once, so a record is not already in the cache when it is needed and must still be fetched from RAM, which means the extra cache brings little benefit. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for each point, to a maximum of 4:
> 
> **1 mark** for cache storing the data and instructions that are used most frequently
> 
> **1 mark** for Program A reusing the same instructions / data, so they are already in the cache after the first use
> 
> **1 mark** for the consequence for Program A: they are read from cache rather than from the slower RAM, saving time on each repeat
> 
> **1 mark** for Program B reading each record only once, so a record is not in the cache when it is first needed
> 
> **1 mark** for the consequence for Program B: the record must still be fetched from RAM, so the extra cache is little used
> 
> **1 mark** for the general point: a larger cache only improves performance if the data that is needed is found in it
> 
> Accept "Program A's set of instructions is small enough to fit inside the cache".
> 
> Credit "cache is faster than RAM" as part of the consequence mark for Program A when it is linked to Program A's data being found in the cache. On its own it does not explain why the two programs are affected differently.
> 
> Do not accept "Program B's file is too large so the computer will run out of memory". The records are still read from RAM in the normal way.

> **[exam-tip]**
> The benefit of cache comes from data being found there, not from the cache existing. Data that is used once gains nothing from a bigger cache, because the slow fetch from RAM still has to happen the first time.
> 
> Before you claim an improvement, look in the stem for evidence of repeated use. Here the words "repeatedly" and "does not read any record a second time" are the whole question.

### Q5
A larger cache can hold more of the frequently used instructions and data. **[1]**

More of what the processor needs is therefore found in the cache, instead of having to be fetched from RAM. **[1]**

Cache is faster to access than RAM, so the processor spends less time waiting for data and is less likely to be left idle. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for a larger cache storing more frequently used instructions / data
> 
> **1 mark** for more of the data needed being found in the cache instead of being fetched from RAM // fewer transfers being needed between RAM and the cache
> 
> **1 mark** for the consequence: cache is faster to access than RAM, so the processor spends less time waiting // the processor is less likely to be idle
> 
> Accept "the CPU can continue working without waiting for data" for the third mark.
> 
> Do not accept "the computer can store more files". Cache memory does not increase the storage capacity of the computer.
> 
> Accept "cache is fast access memory, close to the CPU" for the third mark. Do not accept "the computer is faster" with no reference to cache access or RAM.

> **[exam-tip]**
> Most of the marks are for what changes, not for the word "faster". Say what extra thing the bigger cache now holds, say where that data would otherwise have come from, and only then say why that saves time.
> 
> The comparison the examiner is looking for is cache against RAM. If RAM is never mentioned in your answer, you have almost certainly lost a mark.

### Q6
Cache memory is fast-access memory, which is faster to access than RAM. **[1]**

It stores the data and instructions that are used most frequently. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - Cache memory is fast-access memory // it is faster to access than RAM
> - It is located inside or very close to the CPU
> - It stores frequently used data and instructions
> - It holds copies of data and instructions that have recently been used
> - It has a much smaller capacity than RAM
> 
> **[2 marks]**
> 
> Accept "cache is built into each processor core" for the location point
> 
> Do not accept "cache is where the computer stores files it is not using". That describes secondary storage, not cache memory
> 
> Do not accept "cache stores web pages you have visited". That is a browser cache, which is a different thing

> **[exam-tip]**
> A lot of students answer this question about a web browser cache, because that is the meaning of the word they meet outside the classroom. In this topic cache memory means the small, fast memory inside the processor that holds frequently used instructions and data.
> 
> Two features means two separate points. "It is fast and it is quick to get to" counts as one.

### Q7
Clock speed only states how many cycles happen each second. It does not state how much work the processor does in each cycle. **[1]**

Processors with different architectures need different numbers of clock cycles to carry out the same instruction, so Processor Q may complete an instruction in fewer cycles than Processor P. **[1]**

Clock speed is therefore only a fair comparison between processors of the same architecture. **[1]**

Processor Q may also have more cores, more cache memory or a wider data bus, and any of these can make it faster in use than Processor P. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for each point, to a maximum of 4:
> 
> **1 mark** for clock speed measuring cycles per second, not the amount of work done in each cycle
> 
> **1 mark** for processors of different architectures needing different numbers of clock cycles for the same instruction
> 
> **1 mark** for the conclusion: clock speed can only be compared meaningfully between processors of the same architecture
> 
> **1 mark** for Processor Q having more cores, so more instructions are carried out at the same time
> 
> **1 mark** for Processor Q having more cache memory, so less time is spent waiting for data from RAM
> 
> **1 mark** for Processor Q having a wider data bus, so more data is transferred in each transfer
> 
> Accept "the two processors have different instruction sets" for the second point.
> 
> Do not accept "clock speed does not matter". Clock speed does affect performance; the point is that it cannot be compared on its own across two different architectures.
> 
> Do not accept "Processor Q is a better processor", which gives no reason.

> **[exam-tip]**
> Clock speed is a fair comparison only between two processors built to the same architecture. Across different designs one processor may finish an instruction in fewer clock cycles than the other, so the processor with the lower clock speed can still do more work each second.
> 
> To reach full marks you have to leave clock speed behind and name at least one other factor from this topic. Cores, cache memory and bus width are the three the syllabus expects.

### Q8
The Immediate Access Store (IAS) holds the instructions and data that are currently in use. **[1]**

The processor can access the Immediate Access Store directly, but it cannot fetch an instruction straight from the hard disk drive. **[1]**

Access times for the Immediate Access Store are much faster than access times for a hard disk drive. **[1]**

This means the processor is not left waiting for each instruction to arrive from the hard disk drive. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the Immediate Access Store (IAS) holding the instructions and data currently in use
> 
> **1 mark** for the processor accessing the Immediate Access Store directly / not being able to fetch an instruction straight from the hard disk drive
> 
> **1 mark** for the Immediate Access Store having much faster access times than the hard disk drive
> 
> **1 mark** for the consequence: the processor is not kept waiting between instructions
> 
> Accept "the hard disk drive is much slower than the Immediate Access Store" for the third mark
> 
> Do not accept "the hard disk drive is not big enough" or "the program will not fit", because storage capacity is not the reason the instructions are copied
> 
> Do not accept "the Immediate Access Store is volatile", because volatility explains why its contents are lost when the power is switched off, not why the instructions must be copied there in order to run

> **[exam-tip]**
> This is a question about speed and direct access, not about capacity. Two answers appear again and again and neither of them answers the question: "the hard disk drive is too small", and "because the Immediate Access Store is volatile".
> 
> Build the answer in the order of the marks: what the Immediate Access Store holds, that the processor reaches it directly, that it is much faster than the drive, and what that means for the processor.

### Q9
The system clock produces a regular series of pulses. **[1]**

Each Fetch-Execute (F-E) cycle begins on a clock pulse, so one instruction is carried out on each pulse, although some instructions need more than one. **[1]**

A higher clock speed means more pulses are produced each second, so more F-E cycles, and therefore more instructions, are carried out each second. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the system clock producing a regular series of pulses / signals
> 
> **1 mark** for linking one clock pulse to one Fetch-Execute (F-E) cycle // one instruction being carried out on each clock pulse
> 
> **1 mark** for the conclusion: more pulses per second means more F-E cycles per second, so more instructions are executed per second
> 
> Accept "Fetch-Decode-Execute cycle" or "FDE cycle" in place of "Fetch-Execute cycle".
> 
> Do not accept "a higher clock speed makes the CPU work harder", which restates the question and gives no mechanism.

> **[exam-tip]**
> The mark you are most likely to drop is the middle one, because it is the only place where the Fetch-Execute cycle has to be named. Clock speed on its own is just a count of pulses; it becomes performance only once you say what happens on each pulse.
> 
> Write the chain in order: pulses, then cycles, then instructions per second.

### Q10
(i) Clock speed is the number of clock pulses the system clock produces each second. **[1]**

(ii) Hertz (Hz). **[1]**

**[2 marks]**

> **[mark-scheme]**
> (i) **1 mark** for the number of clock pulses / cycles produced each second // the number of state changes per second
> 
> (ii) **1 mark** for hertz // Hz
> 
> Accept in (ii) gigahertz / GHz, or megahertz / MHz
> 
> Do not accept in (i) "how fast the computer is", which is too vague to earn the mark
> 
> Do not accept in (ii) "bits per second", which is a measure of data transfer rate, not of clock speed

> **[exam-tip]**
> Clock speed counts pulses, not instructions. A processor with a clock speed of 2 GHz produces 2 billion clock pulses each second, but it does not necessarily complete 2 billion instructions, because some instructions need more than one clock cycle.
> 
> Getting that distinction into your answer costs one extra clause and protects you on the harder questions later in this topic.

### Q11
| Action | Component |
|---|---|
| Compares two values to decide whether they are equal | **Arithmetic and Logic Unit (ALU)** **[1]** |
| Decodes an instruction and sends signals that tell the other components what to do | **Control Unit (CU)** **[1]** |
| Produces regular pulses that the other components are synchronised to | **System clock** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for Arithmetic and Logic Unit (ALU) in row 1
> 
> **1 mark** for Control Unit (CU) in row 2
> 
> **1 mark** for system clock in row 3
> 
> Accept the abbreviations `ALU` and `CU` written on their own
> 
> Accept "clock" for the system clock
> 
> Do not accept "CPU" or "processor" in any row, because every row already describes an action taking place inside the CPU
> 
> Do not accept "Control Unit" in row 1, because comparing two values is a logic operation and is carried out by the ALU

> **[exam-tip]**
> Row 1 is the discriminator. Comparing two values is a logic operation, so it belongs to the ALU. The Control Unit decides which instruction is carried out and when, and it sends the signals that make that happen, but it does not do the arithmetic or the comparison itself.
> 
> If you mix up the ALU and the Control Unit you will lose marks across the whole of this topic, so fix the split early: the Control Unit directs, the ALU calculates and compares.

### Q12
Software has to be written so that it can use more than one core. **[1]**

If a program is not written in this way, only one core does the work and the other cores stay idle. **[1]**

Some tasks are sequential, so one step cannot start until the previous step has finished, and those parts cannot be split between cores. **[1]**

Extra processing time is also needed to divide the work between the cores and to allow the cores to communicate with each other. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for each point, to a maximum of 4:
> 
> **1 mark** for software needing to be written to make use of more than one core
> 
> **1 mark** for the consequence when it is not: one core is used and the others are left idle
> 
> **1 mark** for some tasks being sequential // a step depending on the result of the previous step
> 
> **1 mark** for the consequence: those parts of the program cannot be split between the cores
> 
> **1 mark** for the overhead of dividing the work between the cores and communicating between them
> 
> **1 mark** for performance being limited by another factor instead, for example the speed of access to RAM
> 
> Accept "the program can only run on one core" for the second point.
> 
> Do not accept "the processor is not fast enough", which makes no reference to the cores.
> 
> Do not accept "four cores use more electricity". Power consumption is not a performance factor on this syllabus.

> **[exam-tip]**
> This is the question that separates the grades in this topic. Almost every student writes "more cores means more instructions at the same time", which is the answer to a different question and earns nothing here.
> 
> The examiner wants the reasons the gain is smaller than expected. There are two big ones and you should always reach for them: the software has to be written to use several cores, and a sequential task cannot be split no matter how many cores you have.

### Q13
Arithmetic operations, for example adding two numbers together. **[1]**

Logic operations, for example comparing two values to see whether they are equal. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for arithmetic / mathematical operations
> 
> **1 mark** for logic operations / logical comparisons
> 
> Accept a named example on its own for the first mark, such as addition, subtraction or multiplication
> 
> Accept a named example on its own for the second mark, such as `AND`, `OR`, `NOT`, or comparing two values
> 
> Do not accept two arithmetic examples such as "addition" and "subtraction", because they are the same type of operation and earn one mark only
> 
> Do not accept "the ALU decodes instructions", because decoding is carried out by the Control Unit (CU)

> **[exam-tip]**
> The question asks for two types of operation, so the two answers must be different kinds. Writing "it adds numbers" and "it subtracts numbers" scores one mark, not two, because both are arithmetic. Pair one arithmetic operation with one logic operation and the second mark is safe.

### Q14
The interrupt is not acted on straight away. The processor completes the current fetch-execute cycle first, so the instruction that is part-way through is finished. **[1]**

The current contents of the registers, including the Program Counter, the accumulator and the status register, are saved onto a stack in memory. **[1]**

The address of the appropriate Interrupt Service Routine (ISR) is loaded into the Program Counter, and the ISR is executed to deal with the interrupt. **[1]**

When the ISR has finished, the saved register contents are restored from the stack into the same registers. **[1]**

The restored Program Counter holds the address of the next instruction of the interrupted program, so that program resumes from the point at which it was interrupted. **[1]**

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for stating that the interrupt is acted on at the end of the current F-E cycle, so the current instruction is allowed to finish
> 
> **1 mark** for stating that the current contents of the registers, or the state of the current process, are saved onto a stack
> 
> **1 mark** for stating that the appropriate ISR is loaded and executed
> 
> **1 mark** for stating that the saved register contents are restored from the stack once the ISR has finished
> 
> **1 mark** for stating that the restored Program Counter returns the address of the next instruction, so the interrupted program resumes at the point it was interrupted
> 
> Accept "pushed onto the stack" for saved and "popped from the stack" for restored.
> 
> Accept a named list such as PC, ACC, CIR and status register in place of "the registers".
> 
> Do not accept "the program starts again from the beginning". The Program Counter is restored, not reset.
> 
> Do not accept "the register contents are saved in the ISR". The ISR is the code that handles the interrupt; the register contents are saved onto a stack.
> 
> Do not accept an answer that saves the registers but never restores them, or restores them but never says they were saved. Each is worth its own mark and neither implies the other.

> **[exam-tip]**
> Saving and restoring are two separate marks, and it is easy for you to write only one of them. Plan the answer as a loop: finish the cycle, save, run the ISR, restore, resume. Every one of those five steps is a mark.
> 
> Say where the register contents go. "The registers are saved" is weaker than "the registers are pushed onto a stack", and the stack matters, because it is what lets a second, higher priority interrupt arrive during the first without the earlier values being lost.
> 
> The last mark is the one you are most likely to miss. Explain that restoring the Program Counter is what makes the program continue from the right instruction. Without it the answer stops one step short.

### Q15
The separate tasks can be split between the four cores. **[1]**

Each core fetches, decodes and executes its own instructions, so four instructions can be processed at the same time. **[1]**

The whole calculation is therefore finished in less time than on the single-core processor. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the tasks / sequences of instructions being split between the cores
> 
> **1 mark** for more than one instruction being carried out at the same time // the instructions being processed in parallel // more than one instruction executed per clock pulse
> 
> **1 mark** for the consequence: the total processing time is reduced // the program finishes sooner
> 
> Accept "parallel processing" for the second mark.
> 
> Do not accept "the four-core processor has a higher clock speed". The stem states the processors are of the same type, so the clock speed is not the reason.
> 
> Do not accept "four cores are faster than one core", which repeats the question without giving a mechanism.

> **[exam-tip]**
> The marks here are for the mechanism, not the outcome. Write three separate things: what is split, what happens at the same time, and what that does to the total time.
> 
> Notice that the stem tells you the tasks "can be carried out at the same time". That phrase is there deliberately. It is the condition that makes the extra cores useful, and a question where that condition is missing has a very different answer.

### Q16
Error 1: the Memory Address Register (MAR) does not store data. **[1]**

The Memory Address Register (MAR) stores the address of the memory location that is currently being read from or written to. **[1]**

Error 2: the Memory Data Register (MDR) does not store an address. **[1]**

The Memory Data Register (MDR) stores the data that has been read from the address held in the MAR, or the data that is about to be written to that address. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for identifying that the Memory Address Register (MAR) does not hold data
> 
> **1 mark** for the correct role of the MAR: it stores the address of the memory location currently being read from or written to
> 
> **1 mark** for identifying that the Memory Data Register (MDR) does not hold an address
> 
> **1 mark** for the correct role of the MDR: it stores the data read from the address held in the MAR, or the data to be written to that address
> 
> Accept "the student has swapped the two registers over" for one of the two error marks, but not for both
> 
> Accept the address of an input or output component as well as a memory address in the role of the MAR
> 
> Do not accept "the MAR stores the address of the next instruction" as the role of the MAR, because that is the role of the Program Counter (PC)
> 
> Do not accept a corrected role that repeats the name of the register without saying what it holds, for example "the MAR holds the memory address"

> **[exam-tip]**
> The MAR and the MDR are the pair students swap most often, because both names begin with the word Memory. Use the middle word to keep them apart: the Address register holds an address, the Data register holds data.
> 
> Use the full syllabus names in your answer. The 9618 syllabus and its mark schemes use Memory Data Register (MDR) only, so that is the name to learn and to write.

### Q17
A core is a processing unit inside the CPU. **[1]**

Each core can fetch, decode and execute instructions on its own, independently of the other cores. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for identifying a core as a processing unit inside the CPU // a unit within the processor that carries out instructions
> 
> **1 mark** for stating that it works independently: it can fetch, decode and execute instructions on its own // it contains its own Control Unit (CU), Arithmetic and Logic Unit (ALU) and registers
> 
> Accept "a core acts like a mini CPU" for the first mark
> 
> Do not accept "a core makes the computer faster", which describes an effect of having more cores rather than what a core is
> 
> Do not accept "a core is a CPU" on its own, because it does not say the core is part of the processor

> **[exam-tip]**
> Students very often answer this question by describing what extra cores do, not what a core is. The command word "state what is meant by" asks for a definition, so name the thing first and only then say what it can do.
> 
> The reason a core can work on its own is that it has its own Control Unit, Arithmetic and Logic Unit and registers. Saying that earns the second mark cleanly.

### Q18
The ISR is the block of program code that the processor runs in order to deal with the interrupt. **[1]**

Each type of interrupt has its own ISR, so the processor first identifies the source of the interrupt and selects the ISR that belongs to the printer. **[1]**

The address of that ISR is loaded into the Program Counter, so the ISR is executed in place of the interrupted program; it sends the next block of data to the printer before control is returned. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for stating that the ISR is a routine, program or set of instructions that is executed to handle the interrupt
> 
> **1 mark** for stating that the source or type of the interrupt is identified so that the matching ISR is selected, because each type of interrupt has its own ISR
> 
> **1 mark** for stating that the address of the ISR is loaded into the Program Counter so that the ISR is executed // for stating what this ISR does, namely send more data to the printer
> 
> Accept "interrupt service handling routine" or "interrupt handler" as names for the routine, matching the syllabus wording.
> 
> Do not accept any answer that describes the ISR as a list, a queue, a register or a store that interrupts are placed into. The ISR is the code that handles an interrupt. Interrupts that are waiting are held in an interrupt queue by the interrupt controller, which is a separate thing.
> 
> Do not accept "the ISR stops the running program". The processor suspends the running program; the ISR is the code that is then executed.
> 
> Do not accept a description of the buffer or of buffering. The marks here are for the ISR.

> **[exam-tip]**
> Be precise about what an ISR is. It is code, not storage. Answers such as "the interrupt is added to the ISR" or "the ISR holds the interrupts until they are dealt with" describe a queue and score nothing. The correct sentence is "the appropriate ISR is loaded and executed".
> 
> The word "appropriate" is worth a mark on its own if you explain it. Saying that the processor identifies which device caused the interrupt, so that the right ISR out of many is chosen, is the point examiners are looking for.

### Q19
The Index Register (IX) holds a number. **[1]**

This number is added to the address given in the instruction, which gives the address of the value that is actually read. **[1]**

The number held in the Index Register is increased each time, so the same instruction reads the next value in the list. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the Index Register (IX) storing a value or number
> 
> **1 mark** for that value being added to an address to give another address
> 
> **1 mark** for the value in the Index Register being changed / incremented so that the next location is reached
> 
> Accept "the address formed is the address of the data that is actually used" for the second mark
> 
> Accept "incremented by 1" for the third mark
> 
> Do not accept "the Index Register stores the address of the next value", because the Index Register stores a number that is added to an address, not an address on its own
> 
> Do not accept "the Index Register counts how many values have been read" on its own, because it does not say that the value is added to an address

> **[exam-tip]**
> Students very often describe the Index Register as though it held a memory address. It does not. It holds a number, and that number is added to an address that is already part of the instruction.
> 
> To score all three marks you must say what is added to what, and then say that the number changes each time. An answer that only says "it is used for indexed addressing" scores nothing, because it repeats the name of the technique instead of explaining the role of the register.

### Q20
A VGA port sends an analogue signal to the screen. **[1]**

The image is held in digital form inside the computer, so it has to be converted into an analogue signal before it is sent, and converted back before it is displayed. **[1]**

An analogue signal becomes weaker as the cable becomes longer. **[1]**

A longer cable also picks up more interference, and an analogue signal cannot be restored exactly, so the errors show as a faint picture with poor colour. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - a VGA port sends an analogue signal
> - the image is held in digital form in the computer, so it must be converted to analogue before it is sent
> - ... and converted back for the screen, and quality is lost in the conversions
> - an analogue signal becomes weaker over a longer cable
> - the longer the cable, the more interference / crosstalk the signal picks up
> - an analogue signal cannot be restored exactly, so the errors appear as a faint or discoloured picture
> - a digital connection such as HDMI is far less affected by cable length
> 
> **[4 marks]**
> 
> Accept "the signal weakens over distance" for the fourth marking point.
> 
> Do not accept "the cable is broken", because the same screen gives a clear picture on a short cable.
> 
> Do not accept "the resolution is too high", because the resolution has not changed between the two cables.
> 
> Do not accept "analogue is old" or "VGA is outdated" without saying what effect the analogue signal has on the picture.

> **[exam-tip]**
> Every mark here depends on the word analogue, so say it first and then say what an analogue signal does over distance. Answers that stop at "data is lost because the cable is long" describe the symptom and never reach the cause. The clue that the fault is the signal type, and not a broken cable, is in the question: the short cable gives a clear picture.

### Q21
(i) At the end of the current fetch-execute cycle, before the next instruction is fetched. **[1]**

(ii) The buffer of a printer becomes empty. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for (i): at the end of the current F-E cycle // just before the next fetch begins // once the current instruction has finished executing
> 
> **1 mark** for (ii), any one hardware cause:
> 
> - A key is pressed on the keyboard
> - The buffer of a printer becomes empty
> - A printer has run out of paper
> - A disk drive reports a read or write error
> - A power failure is detected
> - A hardware timer reaches zero
> 
> Do not accept for (i): "at any time", "immediately", "in the middle of an instruction", "during the decode stage". The current instruction is always allowed to finish first
> 
> Do not accept for (ii): division by zero, an invalid or illegal instruction, a program requesting an input or output operation, a buffer overflow in a program. These are software interrupts, not hardware interrupts

> **[exam-tip]**
> Read part (ii) carefully. The question asks for a hardware cause, and division by zero is the answer you are most likely to reach for first. It is a software interrupt and scores nothing here. A hardware cause comes from a physical device: a keyboard, a printer, a disk drive, the power supply.
> 
> For part (i), "when an interrupt happens" is not an answer. The signal can arrive at any moment, but the processor only looks at it at the end of the cycle it is currently in.

### Q22
Current Instruction Register (CIR): it holds the instruction that the processor is currently decoding or executing. **[1]**

Accumulator (ACC): it holds the result of a calculation carried out by the Arithmetic and Logic Unit (ALU). **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the Current Instruction Register (CIR) holding the instruction currently being decoded and/or executed
> 
> **1 mark** for the Accumulator (ACC) holding the result of a calculation / the value being worked on by the Arithmetic and Logic Unit (ALU)
> 
> Accept "stores the instruction that has just been fetched" for the CIR mark
> 
> Accept "stores a running total during a calculation" for the ACC mark
> 
> Do not accept "the CIR stores the address of the current instruction", because the CIR holds the instruction itself, not an address
> 
> Do not accept "the ACC stores data fetched from memory", because that is the role of the Memory Data Register (MDR)

> **[exam-tip]**
> The commonest slip here is writing "instruction register" instead of Current Instruction Register (CIR). The syllabus name has the word Current in it, and that word carries the meaning: the CIR holds the instruction being worked on now. The address of the next instruction is in the Program Counter (PC), which is a different register.
> 
> Learn the full name, the abbreviation and the role of every special purpose register, because a question can ask for any of the three.

### Q23
A VGA port carries video data only. **[1]**

It does not carry audio data, so no sound signal reaches the monitor through the VGA cable. **[1]**

The user must connect a separate audio cable from the audio output of the computer to the monitor. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for a VGA port carries video / image data only
> 
> **1 mark** for it does not carry audio / sound data, so no sound signal reaches the monitor
> 
> **1 mark** for connect a separate audio cable from the computer to the monitor / to the speakers
> 
> Accept "a second cable just for the sound" for the third mark.
> 
> Do not accept "the speakers are broken" or "the volume is muted", because the question is about what the VGA connection carries.
> 
> Do not accept "use an HDMI cable instead" for the third mark, because the question states that the computer has only a VGA port.

> **[exam-tip]**
> Read the scenario before reaching for the standard comparison. This computer has no HDMI port, so "use HDMI" is not a solution that is available and it earns nothing. The mark is for saying that the sound needs its own separate cable, which follows directly from the fact that VGA carries video only.

### Q24
| Register | Contents at the end of the fetch stage |
|---|---|
| Memory Address Register (MAR) | **300** **[1]** |
| Memory Data Register (MDR) | `LDD 415` [1] |
| Current Instruction Register (CIR) | `LDD 415` [1] |
| Program Counter (PC) | **301** **[1]** |

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for MAR = 300, from `MAR ← [PC]`
> 
> **1 mark** for MDR = `LDD 415`, from `MDR ← [[MAR]]`
> 
> **1 mark** for CIR = `LDD 415`, from `CIR ← [MDR]`
> 
> **1 mark** for PC = 301, from `PC ← [PC] + 1`
> 
> Accept "the instruction at address 300" or LDD 415 written without the backticks for the MDR and CIR rows
> 
> Do not accept MDR = 62. Memory location 415 is only read during the execute stage, when the operand of `LDD` is used. The fetch stage reads memory once, at the address in the MAR, which is 300
> 
> Do not accept CIR = 415 or CIR = `LDD` alone. The whole instruction, opcode and operand together, is copied into the CIR; the CIR is what splits it afterwards
> 
> Do not accept PC = 300. The PC is incremented during the fetch stage, not at the end of the cycle
> 
> Do not accept MAR = 415. The MAR holds 415 later, during the execute stage, but not at the end of the fetch stage

> **[exam-tip]**
> The trap here is the value 62. `LDD 415` will eventually load 62 into the accumulator, but that happens in the execute stage. At the end of the fetch stage the processor has read one thing from memory: the instruction itself.
> 
> The other frequent slip is leaving the PC at 300. The increment happens during the fetch, so that the PC already points at the next instruction while the current one is still being decoded and executed.

### Q25
The processor places the address of the memory location on the address bus. **[1]**

The address bus carries this address in one direction only, from the processor to main memory. **[1]**

The processor places the data value that is to be stored on the data bus. **[1]**

The control bus carries a write signal to main memory, so that main memory stores the value at that address instead of reading from it. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the address of the memory location being put on the address bus
> 
> **1 mark** for the address bus being unidirectional / carrying the address from the processor to main memory only
> 
> **1 mark** for the data value being put on the data bus
> 
> **1 mark** for the control bus carrying a write signal / a signal that tells main memory to write rather than read
> 
> Accept "the data bus is bidirectional, so the same bus carries data back to the processor during a read" in place of the second mark
> 
> Accept "the control bus also carries the timing signals produced by the system clock" in place of the fourth mark
> 
> Do not accept "the address bus carries the data value", because the address bus carries only the address of the location
> 
> Do not accept an answer that only names the three buses without saying what each one carries

> **[exam-tip]**
> Students often answer this question by describing the Memory Address Register (MAR) and the Memory Data Register (MDR) instead. Those registers hold the address and the data inside the processor. The question asks how the address and the data travel between the processor and main memory, and that is the job of the buses.
> 
> The control bus is the mark most often dropped. Without a write signal on the control bus, main memory has no way of knowing whether it is being read from or written to.

### Q26
(i) An analogue signal. **[1]**

(ii) Video data only. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for analogue
> 
> **1 mark** for video data // image data // picture data, with no audio
> 
> Accept "it carries the picture but not the sound" for the second mark.
> 
> Do not accept "digital" for part (i).
> 
> Do not accept "video and audio" or "multimedia" for part (ii), because a VGA port does not carry sound.

> **[exam-tip]**
> Fix the pair in your memory the right way round: VGA is the analogue one that carries picture only, HDMI is the digital one that carries picture and sound. Swapping them is the single commonest error on this part of the syllabus, and it costs marks on the comparison questions as well as on recall like this.

### Q27
| Item carried | Name of bus |
|---|---|
| The location in main memory that the processor is about to read from | **Address bus** **[1]** |
| An instruction copied from main memory into the processor | **Data bus** **[1]** |
| A signal telling main memory that a write operation is to take place | **Control bus** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for address bus in row 1
> 
> **1 mark** for data bus in row 2
> 
> **1 mark** for control bus in row 3
> 
> Accept "address", "data" and "control" written without the word bus
> 
> Do not accept "system bus", because it does not say which of the three buses is meant
> 
> Do not accept "memory bus" or "instruction bus", because the syllabus names only the address bus, the data bus and the control bus

> **[exam-tip]**
> Row 2 is the one students get wrong. They put the instruction on the address bus, because an instruction is fetched from an address. The address bus carries only the address of the location. Whatever is stored at that location, whether it is data or an instruction, travels on the data bus.

### Q28
HDMI carries video data and audio data along the same cable. **[1]**

A VGA port carries video only, so the sound would not reach the speakers built into the projector. **[1]**

HDMI supports a higher transfer rate than VGA, which is needed for the large amount of data in the video clips. **[1]**

HDMI is a digital interface, so the signal is not converted to analogue and back and no picture data is lost. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - HDMI carries video and audio on the same cable // only one cable is needed
> - a VGA port carries video only
> - ... so with VGA a separate audio cable would be needed to reach the projector speakers
> - HDMI supports a higher transfer rate than VGA
> - ... which is needed for the large amount of data in a video clip
> - HDMI is a digital interface, so the signal is not converted to analogue and back
> - ... so no picture data is lost in the conversion
> - HDMI is less prone to interference / crosstalk, so the picture is clearer
> 
> **[4 marks]**
> 
> Accept "only one cable is needed" for the first marking point.
> 
> Do not accept "HDMI is newer than VGA", because age on its own is not a benefit.
> 
> Do not accept "HDMI gives high definition" with no explanation of why that matters here.

> **[exam-tip]**
> Marks in a comparison question come from saying what the other port cannot do, so pair every claim about HDMI with the matching limit of VGA. The audio point is the easiest mark on this question and the one most often missed, because students picture a projector as a picture-only device and forget the question said it has built-in speakers.

### Q29
The second step should be `MDR ← [[MAR]]` **[1]**

The double square brackets mean the contents of the memory location whose address is held in the MAR, so the instruction stored at that address is copied into the MDR. **[1]**

The student's single brackets mean the contents of the MAR itself, which is an address. Their version would copy that address into the MDR instead of the instruction stored at that address. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `MDR ← [[MAR]]`
> 
> **1 mark** for stating that `[[MAR]]` means the contents of the memory location whose address is held in the MAR // the data or instruction read from memory at that address
> 
> **1 mark** for stating that `[MAR]` means the contents of the MAR, which is an address, so the MDR would receive an address instead of the instruction
> 
> Accept "the value stored at that memory address" for the second mark.
> 
> Accept "the MDR would hold 300 instead of the instruction at address 300" or any equivalent worked example for the third mark.
> 
> Do not accept "the brackets are the wrong number" on its own for the third mark. You must say what `[MAR]` would actually put into the MDR.
> 
> Do not accept `MDR ← [MAR] + 1` or any answer that changes the registers rather than the brackets.

> **[exam-tip]**
> Count the brackets. One pair means "the contents of this register". Two pairs means "go to the memory location whose address this register holds, and take what is there". `MDR ← [[MAR]]` is the only step in the fetch stage that uses two pairs, because it is the only step that reads from memory.
> 
> An explanation mark is never given for saying that something is wrong. Say what the wrong version would put into the register, and the mark follows.

### Q30
A program is held in main memory as a set of instructions, in the same memory space that holds the data the program uses. **[1]**

The instructions are then fetched from main memory and executed one at a time, in sequence. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for stating that the program instructions are stored in main memory, in the same memory space as the data
> 
> **1 mark** for stating that the instructions are fetched from main memory and carried out one at a time / in order
> 
> Accept "instructions and data are stored in the same memory space" for the first mark
> 
> Accept "the instructions are executed one after another" for the second mark
> 
> Do not accept "the program is stored on the hard disk drive", because the stored program concept describes where the program is held while it is running, not where the file is kept

> **[exam-tip]**
> Many students answer this by saying that a program is "saved on the computer". That is file storage, not the stored program concept. The two marks are for saying that the instructions sit in main memory alongside the data, and that they are then fetched and carried out one after another.

### Q31
HDMI is a digital port, so the signal it sends to the monitor is digital. **[1]**

The image is already stored in digital form inside the computer, so it does not have to be converted into an analogue signal and back again. **[1]**

No data is lost in a conversion, and a digital signal is also less affected by interference than an analogue one. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - HDMI is a digital port // HDMI carries a digital signal
> - the image data is already held in digital form in the computer, so no conversion is needed
> - the signal is not converted to analogue and then back to digital
> - ... so no data is lost in the conversion
> - a digital signal is less prone to interference / crosstalk than an analogue signal
> - HDMI supports a higher transfer rate than an analogue port such as VGA
> - ... which is needed because an image with a large number of pixels contains a large amount of data
> 
> **[3 marks]**
> 
> Accept "the signal stays digital all the way from the computer to the monitor" for the second marking point.
> 
> Do not accept "HDMI is better quality" with no reason. Accept "HDMI supports the high resolution of the monitor" as the follow-on to the transfer-rate point.
> 
> Accept "HDMI has a faster transfer rate than VGA" for the sixth marking point; the link to the large amount of image data earns the seventh. Do not accept "HDMI is faster" with no reference to data transfer.

> **[exam-tip]**
> The reason lives in the type of signal, not in the shape of the plug. Answers that say "HDMI is high definition so the picture is better" are circular and score zero. Say the word digital, then say what not converting the signal saves you.

### Q32
| Description | Register transfer notation |
|---|---|
| The contents of the Program Counter (PC) are copied to the Memory Address Register (MAR). | `MAR ← [PC]` [1] |
| The contents of the Memory Data Register (MDR) are copied into the Current Instruction Register (CIR). | `CIR ← [MDR]` [1] |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `MAR ← [PC]`
> 
> **1 mark** for `CIR ← [MDR]`
> 
> Accept register names written in lower case, and an arrow drawn or typed in any form as long as it points left, towards the register that receives the data
> 
> Do not accept `MAR ← PC` or `CIR ← MDR`. The square brackets are part of the notation and mean "the contents of". Without them the answer names the register itself rather than what is stored in it
> 
> Do not accept `PC ← [MAR]` or `MDR ← [CIR]`. The register that receives the data is always written on the left of the arrow
> 
> Do not accept `MAR ← [[PC]]`. Double brackets mean the contents of the memory location whose address is in the register, and no memory read happens at this step

> **[exam-tip]**
> The commonest way to lose these marks is to drop the square brackets. Read `[PC]` as "the contents of the PC", so `MAR ← [PC]` says "copy what is stored in the PC into the MAR".
> 
> Check the direction of the arrow before you move on. The register that receives the data goes on the left. A transfer written the wrong way round scores nothing, even when both registers are correct.

### Q33
Video data. **[1]**

Audio data. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for video data // image data // picture data
> 
> **1 mark** for audio data // sound data
> 
> Accept "vision" and "sound"
> 
> Do not accept "multimedia" on its own, because it repeats the name of the port without saying what is carried
> 
> Do not accept "power", "text" or "data" without saying which type of data

> **[exam-tip]**
> An HDMI connection carries both types of data along one cable, and that is exactly what separates it from VGA. Students who think of HDMI as simply a screen cable name only the video and lose half the marks. If a question mentions a television, a monitor with built-in speakers or a projector with speakers, the audio mark is almost always available.

### Q34
The computer detects that a device has been plugged into the USB port. **[1]**

The microphone sends a code that identifies what type of device it is. **[1]**

The operating system searches its list of device drivers for that code. **[1]**

If a matching driver is found it is loaded, so that the computer can communicate with the microphone. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - a voltage change happens at the port when the device is plugged in
> - the computer detects that a device has been connected
> - the device sends a code that identifies what type of device it is
> - the operating system searches its list of devices / installed device drivers for that code
> - the appropriate device driver is loaded
> - ... so that the computer and the microphone can communicate
> - if no suitable driver is already installed, the computer searches for a compatible one
> - ... and the user may have to download and install the driver manually
> 
> **[4 marks]**
> 
> Accept "plug and play" as the name of this process, but award no mark for the name on its own.
> 
> Do not accept "the computer installs the microphone" with no reference to a driver.
> 
> Do not accept an answer that says the driver is always downloaded from the internet, because a driver that is already stored on the computer is loaded without any download.

> **[exam-tip]**
> This question is really asking about device drivers, so the word "driver" needs to appear in your answer. "The computer recognises it and it works" describes the result rather than the process and earns nothing. The detail that separates a strong answer here is the new device: say what happens when no suitable driver is already installed, because the question tells you the microphone has never been connected before.

### Q35
Benefit: the printer is detected automatically and the correct device driver is loaded, so the user does not have to set the printer up by hand. **[1]**

Benefit: the connector fits into the port one way round only, so the cable cannot be connected incorrectly. **[1]**

Drawback: a USB cable can only be a short length, so the printer has to be placed close to the computer. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Benefits, any two from:**
> 
> - the device is detected automatically when it is plugged in
> - the correct device driver is loaded automatically
> - the connector fits the port one way round only, so an incorrect connection cannot be made
> - USB is a widely used standard, so cables, spare parts and support are easy to obtain
> - newer USB standards are backwards compatible with older USB devices
> - more than one data transfer rate is supported, so the same port suits slow and fast devices
> - USB has a fast data transfer rate
> 
> **[2 marks]**
> 
> **Drawback, any one from:**
> 
> - the cable length is limited, so USB cannot be used over a long distance
> - an older USB standard transfers data more slowly than a newer one
> - very old USB standards may stop being supported
> 
> **[1 mark]**
> 
> Accept "plug and play" for the first benefit only if the answer also says what happens, such as the device being detected or the driver being loaded.
> 
> Accept "USB has a fast data transfer rate" as a benefit. Do not accept "it is fast" with no reference to data transfer.
> 
> Do not accept a benefit of the printer, such as "it prints in colour". The question asks about the port.

> **[exam-tip]**
> The commonest way to lose the third mark here is to give a drawback of the printer or of the computer instead of a drawback of the port. Keep every point about the USB connection itself. Also watch the shape of the question: two benefits and one drawback means three separate points, so writing three benefits caps you at two marks.

### Q36
A printer. **[1]**

A mouse. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - Keyboard
> - Mouse
> - Printer
> - Scanner
> - Digital camera / video camera
> - Portable media player
> - Mobile phone
> - External hard disk drive / flash drive / memory stick
> - Network adapter
> - Headset / microphone / speakers
> - Monitor
> 
> **[2 marks]**
> 
> Accept the devices in either order
> 
> Do not accept two answers that name the same device twice, for example "printer" and "colour printer"
> 
> Do not accept a category with no device named, such as "input device", "storage device" or "peripheral"
> 
> Do not accept an internal component such as the CPU, RAM or the internal hard disk, because these are not peripheral devices connected through a port

> **[exam-tip]**
> The word "different" in the question is doing real work. Two answers that name the same device in two ways, such as "keyboard" and "wireless keyboard", earn one mark between them, not two. Name a specific device rather than a category, because "input device" is not a device and earns nothing.

### Q37
> **[mark-scheme]**
> (i)** 1 mark **for each bullet point (**max 3**).
> 
> - Control unit (CU)
> - Arithmetic and Logic Unit (ALU)
> - Immediate Access Store (IAS)
> - (System clock)
> 
> (ii) **1 mark** for each bullet point (**max 2**)
> 
> - Special purpose registers hold the status of a program whereas general purpose registers hold the temporary data while performing operations.
> - Special purpose registers are specialised for a specific use, whereas general purpose registers are used for any purpose.
> - General purpose registers can be used by most instructions, whereas special purpose can only be used by certain i
> **[mark-scheme]**
> **1 mark** for each correct answer (shaded cells)
> 
> | Step | Description |
> |---|---|
> | `PC ← [PC] + 1` | The address in PC is incremented. |
> | `MDR ← [[MAR]]` | **The **<u>**data **</u>**in the **<u>**location **</u>**pointed to by the MAR is copied to the MDR.** |
> | `MAR ← [PC]` | **The **<u>**contents**</u>** of PC are copied to the MAR.** |
> | `CIR ← [MDR]` | The contents of MDR are copied into CIR. |
**1 mark **for an appropriate example.

Examples:

- Division by zero
- Runtime error
- Out of memory bounds
- Program requesting an external device / input
- Buffer overflow
> **[mark-scheme]**
> **1 mark** for each letter in the correct position (2, 4 and 6)
> 
> **D**
> **A**
> **B**

### Q38
> **[mark-scheme]**
> **1 mark** for naming a correct port** 2 marks** for matching justification
> 
> - USB
> - …has fast data transfer speeds for data (to the headset)
> - …is a universal/popular cable // universal standard
> - HDMI
> - …allows video and audio to be transferred (on the same cable)
> - …convenience of HDMI as no need for two cables

### Q39
> **[mark-scheme]**
> **1 mark** for each bullet point (max 1)
> 
> - USB / Universal Serial Bus
> - HDMI

### Q40
> **[mark-scheme]**
> **1 mark** for identification of the register and **1 mark** for role (**max 2** for each register)
> 
> - Program Counter (PC)
> stores the <u>address</u> where the <u>next </u>instruction is to be read from
> - Memory Address Register (MAR)
> stores the address of the memory location (or an I/O component) 
> **currently being read from **or **written to**
> - Current Instruction Register (CIR)
> holds the instruction currently being decoded and/or executed
> - Status Register
> Contains bits which can be referenced individually and set or cleared depending on the operation e.g. overflow, underflow
> **[mark-scheme]**
> (i) **1 mark** for each bullet point (**max 1)**
> 
> - The CPU can now perform nearly twice as many F-E cycles per second
> - Instead of 2.1 billion F-E cycles per second, the CPU can now perform 4 billion FE cycles per second
> 
> (ii) **1 mark** for each bullet point (**max 5**)
> 
> - Multiple cores introduce additional overheads
> - …because of the need for communication between cores
> - Software may not be designed for multiple cores…
> - …so one of the cores will be left idle
> - Memory access speed may not match speed of cores…
> - …so causing delay
> - The two computers may have more differences than just the cores
> - …one may have more RAM which allows faster multitasking
> - ...one may have a GPU
> - ...etc.

### Q41
> **[mark-scheme]**
> **1 mark **for each correct purpose
> 
> | Register | Purpose |
> |---|---|
> | Program Counter (PC) | Stores the address of the next instruction to be fetched/executed |
> | Memory Address Register (MAR) | Stores the address of the memory location where data will be read from/written to |
> | Memory Data Register (MDR) | Stores the data read from the address in the MAR // stores the data to be written to the address in the MAR |
> | Index Register (IX) | Stores a number that will be added to the operand, to form the address of the data |
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 4**)
> 
> e.g.
> 
> - HDMI has faster transfer rates than VGA
> - … needed due to high resolution / large number of pixels of monitor // HDMI supports the high resolution of the monitor
> - HDMI supports video and audio transfer between computer and monitor speakers
> - … so no separate sound cable is needed unlike VGA
> - HDMI is digital interface therefore no data is lost in transfer to analogue and back
> - HDMI is less prone to error/crosstalk/external interference

### Q42
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - To store the value of flags/bits
> - … that can be changed/set/cleared after arithmetic / logical operations
> - To allow flags to be checked
> - … to change instruction sequence
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - Special purpose registers have a specified role in the machine whereas general purpose registers can be used for all purposes defined by the programmer
> - Special purpose registers hold the state of the program’s execution while general purpose registers hold the program’s data during operations

### Q43
> **[mark-scheme]**
> **1 mark** for system clock and **1 mark** for Control Unit
> 
> System clock
> 
> - To synchronise operations
> - ... by creating and transmitting timing signals on the control bus
> 
> Control Unit
> 
> - Sends/receives control signals along control bus
> - Reads an instruction from the contents of the memory location whose address is stored in PC
> - Coordinates/synchronises the activity of other components in the CPU
> - Manages the execution of instructions
> - Controls communication between the components in the CPU
> **[mark-scheme]**
> (i)** 1 mark** for the feature, **1 mark **max for the matching reason
> 
> e.g.
> 
> Feature: clock speed
> 
> - Higher clock speed means that more F-E cycles are executed per second // Higher clock speed results in more throughput
> 
> Feature: bus width
> 
> - Larger bus width means that more data transferred at the same time
> 
> (ii) 1 mark for correct port. 2 marks for explanation
> 
> Port: USB / Universal Serial Bus
> 
> Explanation:
> 
> - A voltage change occurs when the drive is plugged in
> - The computer detects this voltage change
> - The code of the device is transferred to computer
> - … the OS finds the code of the device in the list of devices
> - … and loads the appropriate device driver
