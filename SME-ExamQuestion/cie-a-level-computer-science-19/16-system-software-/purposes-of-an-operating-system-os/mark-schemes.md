# Mark Schemes — Purposes of an Operating System (OS)
**16. System Software** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (24 questions)


### Q1
**(i)**

8 programs **[1]**

At 8 programs, more time is spent swapping pages (55%) than processing data (45%) **[1]**

**(ii)**

As more programs are opened, the RAM fills up **[1]**

More and more pages need to be swapped in and out of virtual memory **[1]**

This causes a very high rate of hard disk access, and moving the read/write head takes a relatively long time, so swapping uses up more and more of the computer's time **[1]**

**[5 marks]**

> **[mark-scheme]**
> **(i)**
> 
> **1 mark** for 8 (programs)
> 
> **1 mark** for more time is spent swapping pages than processing data / 55% swapping is greater than 45% processing
> 
> The reason mark can only be awarded with the answer 8
> 
> Do not accept 10, because the thrash point is reached as soon as more time is spent swapping pages than processing data, which first happens at 8 programs
> 
> **(ii)**
> 
> **Any three from:**
> 
> - As more programs are opened, the RAM / main memory fills up
> - More and more pages need to be swapped in and out of virtual memory / secondary storage
> - This leads to a very high rate of hard disk access / excessive disk head movements
> - Moving the hard disk read/write head takes a relatively long time / has a long latency
> 
> **[3 marks]**

> **[exam-tip]**
> In (i), a frequent error is to choose 10 programs because the computer has almost stopped processing. The thrash point is not the moment the computer freezes. It is the point at which more time is spent swapping pages than processing data, and at 8 programs swapping (55%) has already overtaken processing (45%).
> 
> In (ii), "the computer slows down" earns nothing on its own. Build the chain of cause and effect: the RAM fills, so pages are swapped in and out more often, and every swap needs slow hard disk access.

### Q2
A page in RAM that is not immediately needed is identified **[1]**

This page is swapped out of RAM and moved to virtual memory on secondary storage, which frees space in RAM **[1]**

The page the program needs is swapped in from virtual memory into the space in RAM **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - A page in RAM that is not immediately needed / not in use is identified
> - This page is moved / swapped out of RAM to virtual memory / secondary storage
> - This frees space in RAM
> - The needed page is moved / swapped in from virtual memory / secondary storage into RAM
> - Pages are swapped between RAM and virtual memory in this way whenever they are needed
> 
> **[3 marks]**
> 
> Accept disk / hard disk for secondary storage
> 
> Do not accept "the program waits until RAM becomes free", because the operating system makes the space itself by swapping a page out

> **[exam-tip]**
> Students often describe only half of the swap. They say the needed page is loaded into RAM but never say where the space comes from. The RAM is full, so a page that is not immediately needed must first be swapped out to virtual memory.
> 
> Past mark schemes describe replacement as pages being swapped in and out of virtual memory. They have not asked for a named method of choosing which page to remove, so spend your time describing both directions of the swap clearly.

### Q3
Virtual memory is when secondary storage, such as a hard disk, is used to extend the RAM **[1]**

This means the computer appears to be able to access more memory than the RAM it actually has **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - Secondary storage / disk is used to extend the RAM / to simulate additional main memory
> - The CPU appears to be able to access more memory than the RAM available
> - Only the data in use needs to be held in RAM
> - Data / programs not immediately needed are swapped between RAM and virtual memory as necessary
> - Virtual memory is created temporarily
> 
> **[2 marks]**
> 
> Do not accept cache memory, because cache is fast memory used by the processor, not secondary storage used to extend RAM
> 
> Do not accept a virtual machine, because a virtual machine is software that emulates a computer, which is a different idea

> **[exam-tip]**
> Do not confuse virtual memory with a virtual machine. The names are similar, but a virtual machine emulates a whole computer, while virtual memory is secondary storage being used as if it were extra main memory.
> 
> Avoid writing that virtual memory "is extra RAM". No RAM is added. The mark is for saying that secondary storage is used to extend the memory available.

### Q4
The logical address space of the program is divided into blocks of varying size called segments **[1]**

The segments are held in virtual memory, which uses secondary storage such as a hard disk to extend the RAM **[1]**

While the program runs, a segment is loaded from virtual memory into physical memory only when it is needed, so only the segments in use are in RAM **[1]**

A segment map table maps the logical addresses in the program to physical addresses in RAM **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - The logical / virtual address space is divided into variable / varying sized blocks called segments
> - Each segment has a name / number and a size
> - Segments are held in virtual memory / on secondary storage, which is used to extend the RAM available
> - During execution, segments are loaded from virtual memory into physical memory / RAM when they are needed
> - Only the segments in use need to be in RAM, so segments are swapped between RAM and virtual memory as necessary
> - A segment map table maps logical / virtual addresses to physical addresses
> - An address is given as a segment number and an offset, and the segment number is used as an index in the segment map table
> - So the CPU appears to be able to access more memory (12 GiB) than the RAM available (8 GiB)
> 
> **[4 marks]**
> 
> Accept disk / hard disk for secondary storage
> 
> Do not accept "virtual memory adds more RAM", because the RAM stays at 8 GiB and secondary storage only makes more memory appear to be available
> 
> Do not accept segments of fixed size, because fixed-size blocks are pages

> **[exam-tip]**
> A common error is to write that virtual memory increases the RAM. It does not. Secondary storage is used to extend the memory available, so the CPU only appears to have access to more memory than the RAM holds.
> 
> Students also answer about segmentation and virtual memory separately and never connect them. To reach 4 marks, show the link: the segments wait in virtual memory and are loaded into RAM only when they are needed, and the segment map table tells the computer where each segment is in physical memory.

### Q5
| Feature | Paging | Segmentation |
|---|---|---|
| Size of each block of memory | **Fixed size** | **Variable size** **[1]** |
| What calculates the size of the blocks | **The operating system** | **The compiler** **[1]** |
| Speed of access | **Faster** | **Slower** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for paging: fixed size **and** segmentation: variable size
> 
> **1 mark** for paging: the operating system **and** segmentation: the compiler
> 
> **1 mark** for paging: faster **and** segmentation: slower
> 
> Both cells in a row must be correct for the mark
> 
> Accept same size / equal size for fixed size, and varying size / different sizes for variable size
> 
> Accept OS for the operating system
> 
> Accept access times are shorter for paging and longer for segmentation
> 
> Do not accept a row that gives the same answer for paging and segmentation, because the row must show a difference

> **[exam-tip]**
> The most common error is to describe segments as "bigger" than pages, or as blocks for "different types of data". Neither is the difference that is credited. The key word is size: pages are all a fixed size, but each segment has its own variable size.
> 
> Treat every row as a two-sided comparison. A row with only one column filled in, or with a statement about only one technique, cannot earn the mark.

### Q6
Segment number / segment name **[1]**

Offset / offset value **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for segment number / segment name
> 
> **1 mark** for offset / offset value
> 
> Accept the two values in either order
> 
> Do not accept page number, because pages are the fixed-size blocks used in paging, not in segmentation
> 
> Do not accept physical address, because the address the program uses is a logical address that is mapped to a physical address

> **[exam-tip]**
> Many students mix up the vocabulary of paging and segmentation and write "page number and offset". In segmentation the blocks are called segments, so the address holds the segment number or segment name together with an offset.
> 
> Do not answer "the physical address". The program works with logical addresses. The operating system uses the segment number as an index in the segment map table, and that table maps the logical address to a physical address.

### Q7
First come first served executes the processes in the order they joined the queue, so P, the process that needs the most processor time, is executed first. **[1]**

Q, R and S need much less processor time, but they must all wait until P has finished, so no process is completed for a long time. **[1]**

Shortest job first executes the processes in ascending order of the processor time needed: Q, S, R, P. **[1]**

The short processes Q, S and R are completed first, so more processes are executed in a smaller amount of time, which is an increased throughput. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **One mark for each point (max 2) for first come first served:**
> 
> - processes are executed one by one in the order they joined the queue // in the order P, Q, R, S
> - ... so P, the longest process, is executed first // Q, R and S must all wait until P has finished // no process is completed for the first 45 ms
> 
> **One mark for each point (max 2) for shortest job first:**
> 
> - processes are executed in ascending order of the amount of processor / CPU time required // short processes are executed first and followed by longer processes // in the order Q, S, R, P
> - ... which leads to an increased throughput because more processes are executed in a smaller amount of time // Q, S and R are all completed before P would have finished under first come first served
> 
> **[4 marks]**
> 
> The answer must use the processes in the table: a description of the two routines that never refers to P, Q, R or S earns a maximum of 2 marks
> 
> Do not accept "shortest job first completes all four processes sooner": both routines finish all four processes at the same time

> **[exam-tip]**
> Shortest job first does not finish the whole set of processes any sooner, because the processor has the same total amount of work to do. The benefit is that more processes are finished early on, which is what throughput measures.
> 
> Make the table do the work. Name the long process that holds everything up under first come first served, and give the order that shortest job first uses. A general description of the two routines that could apply to any set of processes will not earn full marks.

### Q8
- Each page is the same size as a block of main memory, so a page fits exactly into any free block **[1]**
- The three pages do not need to be next to each other, so they can be loaded into blocks 2, 4 and 7 **[1]**
- The operating system keeps a record of which block each page has been loaded into, so the pages of the program can still be found **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - pages and blocks are the same (fixed) size
> - ... so any page fits exactly into any free block // there is no need to find a free area that matches the size of the data
> - the pages do not have to be stored next to each other / in one continuous area of memory
> - each page is placed in a separate free block // the pages are placed in blocks 2, 4 and 7 (in any order)
> - the operating system reads each page from secondary storage into a free block
> - the operating system records which block holds each page
> 
> **[3 marks]**
> 
> Accept "page table" or "page map table" for the record of which block holds each page.
> 
> Do not accept "the operating system moves the blocks that are in use so that the free blocks are next to each other". Paging does not need one large free area, because each page can go into a separate block.
> 
> Do not accept "a page that is not needed is removed to make room". There are already three free blocks, so no page has to be removed.

> **[exam-tip]**
> The trap is the sentence saying that no three free blocks are next to each other. Many students assume the pages must be stored together, and then suggest moving data around in memory or removing a page. Neither is needed. Every page is exactly one block in size, so each page can go into any free block, wherever that block is.
> 
> Read the table before you answer. Naming the actual free blocks (2, 4 and 7) shows the examiner that you have applied the idea to this memory, not just written a definition.

### Q9
- The operating system divides memory into fixed-size blocks, and the program is held in pages of this same size **[1]**
- Only the pages that are needed at the moment are held in main memory, while the other pages stay on secondary storage **[1]**
- When a page that is not in main memory is required, it is read from secondary storage into a free block of main memory **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - memory is divided (by the operating system) into fixed-size / same-size blocks // the program is divided into pages of the same size
> - only the pages that are currently needed are held in main memory // the other pages are kept on secondary storage
> - a page is read from secondary storage into main memory when it is required
> - a page that is no longer needed can be written / moved out to secondary storage (to free space in main memory)
> 
> **[3 marks]**
> 
> Accept "swapped in" and "swapped out" for moved between secondary storage and main memory.
> 
> Do not accept "the program is loaded into main memory" on its own. With paging, only the pages that are needed are loaded.
> 
> Do not accept "memory is divided into variable-sized blocks". This describes segmentation.

> **[exam-tip]**
> A common weak answer describes virtual memory in general, such as "the hard disk is used as extra RAM", and never mentions pages at all. That earns very little here. Describe what happens to the pages: they are all the same size, only the ones needed are in main memory, and a page is read in from secondary storage when it is required.
> 
> The question does not ask how the operating system chooses which page to remove when main memory is full, so do not spend your time on that.

### Q10
- Memory is divided by the operating system into fixed-size blocks, called pages **[1]**
- These same-size blocks of data are read from or written to secondary storage when they are required **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for memory is divided into fixed-size / same-size / equal-size blocks (called pages)
> 
> **1 mark** for pages / blocks of data are read from / written to secondary storage when required // pages are moved between secondary storage and main memory when required
> 
> Do not accept "memory is divided into blocks" without the idea that the blocks are the same size. Segmentation also divides memory into blocks.
> 
> Do not accept "memory is divided into variable-sized blocks" or "blocks sized to fit the parts of a program". These describe segmentation.

> **[exam-tip]**
> The mark for the first point depends on two words: fixed size, or same size. "Paging splits memory into blocks" is not enough, because that is also true of segmentation.
> 
> Do not confuse paging with defragmentation. Moving the blocks of a file on a disk so that they are next to each other is done by defragmentation software. Paging moves same-size blocks of data between secondary storage and main memory.

### Q11
With first come first served, the video-editing process would be executed until it had finished, because it joined the queue first. **[1]**

The word processor would then have to wait a long time for processor time, so it would not respond while the user is typing. **[1]**

With round robin, each process is given the processor for a fixed time slice in turn, so the word processor gets processor time regularly and responds while the video is still being produced. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - first come first served executes processes one by one in the order they are queued // the video-editing process runs until it has finished
> - ... so the word processor has to wait a long time for the processor // does not respond to the user's typing
> - round robin gives each process the processor for a fixed time / time slice
> - ... in turn, so every process gets processor time regularly
> - ... so the word processor responds to the user while the video is still being produced
> 
> **[3 marks]**
> 
> Do not accept "with first come first served the word processor would never run / would be starved": every process in a first-come-first-served queue eventually gets a chance to run

> **[exam-tip]**
> Do not argue that first come first served causes starvation. It does not: every process in the queue eventually runs, and the mark scheme gives "starvation does not occur" as a benefit of first come first served as well as of round robin. The real problem here is how long the word processor has to wait.
> 
> Round robin shares the processor out in fixed time slices. It does not make any process run faster, so do not claim the video is produced sooner.

### Q12
- Main memory (RAM) is limited, so the operating system must allocate blocks of RAM to each program as it needs them **[1]**
- It must prevent two programs occupying the same area of RAM at the same time, so that one program does not overwrite another program's data **[1]**
- When a program is closed, the operating system reclaims its blocks of RAM so they can be allocated to another program **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - allocates (blocks of) RAM to programs / processes // dynamic allocation of RAM to processes
> - prevents two programs / processes occupying the same area of RAM at the same time // stops the data of different programs overwriting each other
> - reclaims unused blocks of RAM (so they can be allocated again)
> - decides which processes / data should be in main memory
> - makes efficient use of (limited) memory
> - moves data from secondary storage when needed // manages paging, segmentation and virtual memory
> 
> **[3 marks]**
> 
> Accept main memory or memory for RAM throughout.
> 
> Do not accept "decides which process runs next" or "shares processor time between programs". These describe process management and scheduling, not memory management.
> 
> Do not accept paging, segmentation and virtual memory as three separate points. Naming the techniques earns one mark at most.

> **[exam-tip]**
> Many students answer about the processor instead of memory. "Decides which program runs next" is scheduling. Keep every point about RAM: which program is given which blocks, keeping programs apart so they do not overwrite each other, and freeing the blocks again when a program closes.
> 
> Listing "paging, segmentation and virtual memory" does not earn three marks. The question asks why memory management is needed, so say what it achieves.

### Q13
Scheduling allows more than one process to appear to be executed at the same time (multi-tasking). **[1]**

Scheduling ensures that every process has fair access to the processor, so no process is starved of processor time. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - allows more than one process to appear to be executed at the same time // enables multi-tasking
> - allows high priority processes to be completed first
> - keeps the processor busy all the time // ensures all processes are executed efficiently
> - ensures all processes have fair access to the processor // prevents starvation of some processes
> - reduces the time that processes wait for the processor
> 
> **[2 marks]**
> 
> "Fair access" and "prevents starvation" are the same point and earn only one mark
> 
> Do not accept "to decide which process runs next" on its own: that describes what scheduling does, not why it is needed
> 
> Do not accept "so that processes are executed at the same time": on a single processor processes only appear to be executed at the same time

> **[exam-tip]**
> Make your two reasons genuinely different. Students often write "every process gets a fair share" and then "no process is left waiting forever". These are the same point in different words, so they earn one mark, not two.

### Q14
The OS shares processor time between the web browser, the music player, the spreadsheet and the printing task. It switches between them so that they appear to run at the same time. **[1]**

This keeps the processor busy all the time instead of leaving it idle. **[1]**

The OS allocates main memory to each open program and stops the data of one program overwriting the data of another. **[1]**

The printer works much more slowly than the processor, so the OS holds the document data in a buffer for the printer. The processor can then carry on with other tasks while the document prints. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from, max 2 for each resource:**
> 
> Processor
> 
> - processor time is shared between the processes / programs // multi-tasking
> - the processor switches between processes so that they appear to run at the same time
> - the processor is kept busy all the time // is not left idle
> 
> Main memory
> 
> - main memory is allocated to each process // the data of all the running programs is held in main memory at the same time
> - the data of one process is stopped from overwriting the data of another // prevents interference between processes
> - the OS decides which processes should be in main memory
> 
> Printer
> 
> - the OS allocates the printer to the process that needs it // resolves a conflict if two processes need the printer at the same time
> - the data for the printer is held in a buffer
> - ... because the processor and the printer work at different speeds
> - ... so the processor is not held up waiting for the printer // can carry on with other tasks
> 
> **[4 marks]**
> 
> Accept "scheduling decides which process uses the processor next" for a processor mark.
> 
> Accept "virtual memory is used when main memory is full" for a main memory mark.
> 
> Do not accept "the processor runs all the programs at exactly the same time". A single-core processor carries out one process at a time, so the programs only appear to run at the same time.
> 
> Do not accept "the OS uses the resources efficiently" on its own. It repeats the question without saying how.

> **[exam-tip]**
> The most common weak answer lists management tasks, such as "memory management and process management", and stops. Naming a task does not explain how the resource is used more fully. For each resource, say what the OS actually does with it.
> 
> Watch the "max 2 for each resource" rule. A student who writes four good points about the processor alone scores only 2. The stem names three resources for a reason, so cover all three before adding detail to any one of them.

### Q15
There is only one processor, so only one process can be in the running state at any one time. **[1]**

The other processes that are able to run wait in the ready state. **[1]**

Each process is given a short amount of processor time and is then moved from the running state back to the ready state, and a process from the ready state is moved to the running state. **[1]**

While the file-copy program waits for the USB flash drive to finish writing, it is moved to the blocked state, so the processor is given to a process that is able to run. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - only one process can be in the running state at a time // there is only one processor
> - processes that are able to run wait in the ready state / in the ready queue
> - the running process is moved back to the ready state (for example when its time slice ends / when a higher priority process is ready)
> - a process from the ready state is moved to the running state / is given processor time
> - the processes are switched so quickly that they appear to run at the same time
> - a process waiting for input/output (for example the file copy waiting for the USB flash drive) is moved to the blocked state
> - ... so processor time is not wasted on a process that cannot continue // the processor is given to a ready process
> 
> **[4 marks]**
> 
> Do not accept "the processor runs all three programs at the same time": with a single processor the programs only appear to run at the same time

> **[exam-tip]**
> Many answers define the three states and stop. A list of definitions scores little here, because the question asks how the states are used. Describe the movement between states: running to ready, ready to running, and running to blocked when a process waits for a device.
> 
> Do not write that multi-tasking runs programs at the same time. On a single processor the programs take turns, and the switching is so fast that they seem to run together.

### Q16
The process moves from the running state to the blocked state, because it must wait for the data to be read from the hard disk. **[1]**

When the data has been read, the process moves from the blocked state to the ready state. **[1]**

When the operating system decides that this process is the next to run, it moves from the ready state to the running state. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for running to blocked, while it waits for the read / input/output operation to finish
> 
> **1 mark** for blocked to ready, when the read / input/output operation has finished
> 
> **1 mark** for ready to running, when the operating system selects it as the next process to run / it is given processor time / it reaches the front of the ready queue
> 
> Accept "an interrupt signals that the read has finished" as the reason for the second change
> 
> Do not accept running to ready for the first change: the process is not waiting for the processor, it is waiting for the hard disk
> 
> Do not accept a change from blocked directly to running: when the read finishes, the processor may be in use by another process, so the process must wait in the ready state first

> **[exam-tip]**
> The most common mistake is to send the process straight from blocked back to running as soon as the data arrives. The data arriving only means the process is able to run again. It still has to wait in the ready state until the operating system gives it the processor.
> 
> Give both states in every change ("from blocked to ready"). An answer that only says "it becomes ready" leaves the examiner to guess which change you mean.

### Q17
| Description | Process state |
|---|---|
| The process is being executed by the processor. | Running |
| The process could be executed, but it is waiting for the processor to become available. | **Ready** **[1]** |
| The process cannot continue until an event happens, such as an input/output operation finishing. | **Blocked** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for Ready (state) in the second row
> 
> **1 mark** for Blocked (state) in the third row
> 
> Accept "in the ready queue" for the second row
> 
> Do not accept Running in either row: it is already given in the first row, and only a process that is being executed is in the running state
> 
> Do not accept Terminated or Finished for the third row: a blocked process has not ended, it continues once the event has happened

> **[exam-tip]**
> Students often swap ready and blocked, because a process in both states is "waiting". Ask what it is waiting for. A ready process is waiting only for the processor, so it could run straight away if the processor became free. A blocked process is waiting for something else, such as data from a disk, so it could not run even if the processor were free.
> 
> Use the three state names from the syllabus: running, ready and blocked.

### Q18
The kernel receives a signal that the interrupt has been generated. It checks the priority of the interrupt, and because it is higher than the priority of process A, the system enters kernel mode. **[1]**

The state of process A, which is the contents of its registers including the Program Counter, is saved on the kernel stack. **[1]**

Process A is pre-empted, so it moves from the running state to the ready state. **[1]**

The kernel consults the interrupt dispatch table (IDT) and the Interrupt Service Routine (ISR) is executed. When the interrupt has been serviced, the scheduling routine decides which process in the ready state runs next. This could be process A or process B.

When process A is given the processor again, its saved state is restored from the kernel stack, so it continues from the instruction where it stopped. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - the kernel receives a signal when the interrupt is generated
> - the kernel checks the priority of the interrupt against process A // the system enters kernel mode because the interrupt has a higher priority than process A
> - the state of process A // the contents of the registers of process A is saved on the (kernel) stack
> - process A is pre-empted // process A moves from the running state to the ready state
> - the kernel consults the interrupt dispatch table / IDT to find the ISR, which is then executed
> - after the interrupt has been serviced, scheduling decides which process in the ready state runs next (process A or process B)
> - when process A runs again, its saved state // the contents of its registers is restored (from the kernel stack) so that it continues from where it stopped
> 
> **[4 marks]**
> 
> Accept "the kernel restores the state of process A once the interrupt has been serviced" for the last point.
> 
> Do not accept "process A moves to the blocked state". A blocked process is waiting for an event or a resource. Process A is able to run and is only waiting for the processor, so it is in the ready state.
> 
> Do not accept "process A is terminated". Its state is saved precisely so that it can continue later.
> 
> Do not credit a statement that process B always runs next. The scheduling routine makes that decision.

> **[exam-tip]**
> The most common answer here is the Paper 1 one: the interrupt is detected at the end of the fetch-execute cycle, the ISR runs, the registers are restored and the process carries on. That answer never mentions the kernel, the process states or scheduling, and it misses most of the marks. This question is about how an interrupt lets the operating system take the processor away from one process and decide what runs next.
> 
> Watch the process state. An interrupted process goes from running to ready, not to blocked. Blocked is for a process that is waiting for something such as data from a device, and process A is not waiting for anything except the processor.

### Q19
The memory locations (addresses) that the data for the photo is read from and written to. **[1]**

The buses that are used to transfer the data for the photo. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - the memory locations / addresses that the data is read from or written to // where the data is physically stored on the hard disk or flash drive
> - the buses used to transfer the data // the data bus / the address bus
> - the commands needed to control the hard disk or the flash drive
> 
> **[2 marks]**
> 
> Do not accept the icon, or dragging and dropping. These are what the user interface shows the student, not what it hides.
> 
> Do not accept "it makes the computer easier to use". This is a benefit of the user interface, not a complexity of the hardware.

> **[exam-tip]**
> This question asks what is hidden, not why hiding it is useful. Many students write a benefit, such as "the student does not need technical knowledge". That answers a different question and scores nothing here.
> 
> Name a real hardware detail that the student never sees: the memory locations the data goes to, the buses it travels along, or the commands sent to the storage device. If your answer is something the student can see on the screen, such as an icon or a file name, it is not hidden.

### Q20
Mode: kernel mode **[1]**

Table: interrupt dispatch table (IDT) **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for kernel mode
> 
> **1 mark** for interrupt dispatch table // IDT
> 
> Do not accept "interrupt register" for the table. The interrupt register holds the flag that shows an interrupt is waiting. It does not identify the ISR to run.
> 
> Do not accept "stack" or "kernel stack" for the table. The stack is where the state of the interrupted process is saved, not where the ISR is found.

> **[exam-tip]**
> Students often answer this with the Paper 1 description of interrupts and write "the interrupt register is checked". At A Level the interrupt is handled by the kernel of the operating system. The interrupt register only shows that an interrupt has been raised. The interrupt dispatch table is what the kernel uses to find the correct ISR.
> 
> Three kernel terms are easy to mix up, so learn them as a set: the system enters kernel mode, the kernel consults the interrupt dispatch table, and the state of the interrupted process is saved on the kernel stack.

### Q21
> **[mark-scheme]**
> **One **mark per mark point (**Max 2**)
> 
> MP1 the kernel receives a signal when an interrupt is generated
> 
> MP2 the kernel checks the priority and reviews the status/priority of the current interrupts
> 
> MP3 system enters kernel mode if the type of interrupt is of higher priority than the current process
> 
> MP4 the kernel consults the interrupt dispatch table / IDT
> 
> MP5 … and saves the state of the interrupted process / contents of the registers on the kernel stack
> 
> MP6 the kernel restores the process state e.g. contents of registers once the interrupt is serviced
> **[mark-scheme]**
> (i) **One **mark per mark point (**Max 1**)
> 
> MP1 multi-tasking allows computers to carry out / seem to carry out more than one process at a time
> 
> (ii) **One **mark per mark point (**Max 2**)
> 
> MP1 processor time/common hardware and resources is/are shared between tasks
> 
> MP2 scheduling is used to decide on the processes to be carried out to ensure multi-tasking operates correctly / efficiently / without clashes
> 
> MP3 one task of a higher priority can interrupt another task that is currently running

### Q22
> **[mark-scheme]**
> **One **mark per mark point (**Max 4**)
> 
> MP1 In segmented memory, the logical / virtual address space is broken into varying sized blocks called segments / sections.
> 
> MP2 Each segment has a name and size.
> 
> MP3 During execution segments from logical / virtual memory are loaded into physical memory.
> 
> MP4 The address is specified by the user
> 
> MP5 … it contains the segment name and offset value.
> 
> MP6 Segments are numbered
> 
> MP7 … and this number is used as an index in the segment map table.
> 
> MP8 The offset value determines the size of the segment.
> 
> MP9 A segment map table maps logical / virtual addresses to physical addresses / contains the segment number and offset
> **[mark-scheme]**
> **One **mark per mark point (**Max 3**)
> 
> MP1 Disk thrashing is a problem that may occur when virtual memory is being used.
> 
> MP2 As the main memory fills up, more and more pages need to be swapped in and out of virtual memory.
> 
> MP3 This swapping leads to a very high rate of hard disk access / excessive disk head movements.
> 
> MP4 Moving a hard disk read/write head takes a relatively long time / long latency time.
> 
> MP5 Eventually, more time is spent swapping pages than processing data thrash point, which can cause the program to freeze or not run.

### Q23
> **[mark-scheme]**
> **One** mark per mark point **(Max 2) **
> 
> - MP1    Virtual memory is used when RAM is running low
> - MP2    …such as when a computer is running many processes at once.
> - MP3    Virtual memory may be used for efficient use of RAM / the processor
> - MP4    …such as if data / programs are not immediately needed, they can be moved from RAM to virtual memory
> **[mark-scheme]**
> **One** mark per mark point **(Max 3) **
> 
> - MP1 Disk thrashing is a problem that may occur when frequent transfers between main memory and secondary memory take place // Disk thrashing is a problem that may occur when virtual memory is being used
> - MP2 As main memory fills up, more pages need to be swapped in and out of secondary/virtual memory
> - MP3 This swapping leads to a very high rate of hard disk head movements
> - MP4 Eventually, more time is spent swapping the pages/data than processing the data.

### Q24
> **[mark-scheme]**
> **One **mark for a benefit **(Max 1)** e.g.
> 
> - MP1    The user interface hides the complexities of the computer hardware/operating system from the user
> - MP2    It provides appropriate access systems for users with differing needs
> - MP3    Complex commands involving memory locations/buses/computer hardware/ are avoided
> 
> **One** mark for a valid example **(Max 1) **e.g.
> 
> Clicking on icon rather than writing code 
> Using a graphical user interface / icons for navigation
> **[mark-scheme]**
> Blocked (state)
> **[mark-scheme]**
> **One** mark per mark point **(Max 2) **
> 
> - MP1    When the time slice of the running process expires (round robin).
> - MP2    …and there is a process with a higher priority in the ready queue, the running process is pre-empted
> - MP3    When an interrupt arrives at the CPU, (the process running on the CPU gets pre-empted).
