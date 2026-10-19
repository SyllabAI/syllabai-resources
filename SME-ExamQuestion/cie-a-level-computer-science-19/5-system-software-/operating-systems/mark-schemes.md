# Mark Schemes — Operating Systems
**5. System Software** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (20 questions)


### Q1
| Fault | Management task | Explanation |
|---|---|---|
| A document that the user saved yesterday cannot be found anywhere on the hard disk. | **File management** **[1]** | **The Operating System records where each file is stored on secondary storage and maintains the directory structure, so a saved file can be found again by its name.** **[1]** |
| A different person used the computer and opened the user's private documents. No user name or password was asked for. | **Security management** **[1]** | **The Operating System creates accounts and passwords and checks them before access is given, and it applies access rights so that one user cannot open another user's files.** **[1]** |
| When a second program is started, the data of the first program becomes corrupted and the first program stops responding. | **Memory management** **[1]** | **The Operating System allocates a separate block of RAM to each program and prevents one program from writing into the area of RAM that another program is using.** **[1]** |

**[6 marks]**

> **[mark-scheme]**
> **1 mark** for "File management" in row one
> 
> **1 mark** for explaining that the Operating System records where a file is stored, or maintains the directory structure, so that a file can be found again
> 
> **1 mark** for "Security management" in row two
> 
> **1 mark** for explaining that the Operating System creates accounts and passwords and checks them before access is given, or that it applies access rights so one user cannot open another user's files
> 
> **1 mark** for "Memory management" in row three
> 
> **1 mark** for explaining that the Operating System gives each program its own block of RAM and stops one program from overwriting the data of another
> 
> An explanation mark can still be awarded when the named task is wrong, as long as the explanation correctly describes the task that would cause that fault.
> 
> Do not accept "hardware management" in row one. The disk itself is working; it is the record of where the file was placed that has failed
> 
> Do not accept "process management" in row three. Process management decides which program runs next. Two programs being given the same area of RAM is a failure of memory management

> **[exam-tip]**
> Fault diagnosis is worth practising because it is the only place this topic is tested as reasoning rather than recall. Work from the symptom to the resource: a lost file points to secondary storage and therefore file management, an unlocked computer points to accounts and therefore security management, and two programs interfering with each other points to RAM and therefore memory management.
> 
> Row three is the one most often answered "process management". Ask yourself what was shared badly. If two programs were given the same space, memory was shared badly. If one program never got a turn on the processor, that would be process management.

### Q2
The Operating System creates a separate account and password for each person who uses the computer. **[1]**

It checks the user name and password when a person signs in, so that it can confirm who they are before access is given. **[1]**

It applies access rights to files, so that one person cannot open or change the documents that belong to another person. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - Creates user accounts and passwords
> - Checks the user name and password // authenticates the user before access is given
> - Applies access rights or permissions to files and folders
> - ... so one user cannot read, change or delete another user's data
> - Allows a password to be changed, or forces it to be changed after a set time
> - Keeps a log or record of which user signed in and what they did
> - Provides or updates a firewall or anti-malware software
> 
> **[3 marks]**
> 
> Accept "authentication" as an alternative to checking the user name and password.
> 
> Do not accept "it keeps the computer safe" or "it stops hackers". These are too vague to credit; the answer must name a task the Operating System actually carries out.
> 
> Do not accept "it backs up the data". Backing up protects against loss, not against unauthorised access.

> **[exam-tip]**
> Security management is the task students describe most vaguely. "It protects the computer" is a restatement, not a description, and it earns nothing. Every mark here comes from naming a concrete action: create an account, check a password, set an access right.
> 
> A useful habit is to give the reason as well as the action. "Applies access rights" is one mark; "applies access rights so that one user cannot open another user's files" gives the examiner two things to credit.

### Q3
| Description of the task | Name of the management task |
|---|---|
| Divides secondary storage into file allocation units and maintains the directory structure. | File management |
| Allocates a block of RAM to each running program and stops one program from overwriting the data of another. | **Memory management** **[1]** |
| Checks the user name and the password before access to the computer is allowed. | **Security management** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for "Memory management" in the second row
> 
> **1 mark** for "Security management" in the third row
> 
> Accept "memory" and "security" without the word "management"
> 
> Do not accept "process management" in the second row. Process management decides which program runs next; deciding where in RAM a program is placed is memory management
> 
> Do not accept "data security" or "encryption" in the third row. The task carried out by the Operating System is called security management

> **[exam-tip]**
> Row two is the row that catches students out, because "running program" makes them reach for process management. Look at the resource in the description instead. If the sentence is about RAM being given out or protected, the answer is memory management.
> 
> Learn the five names in Cambridge's own words: memory management, file management, security management, hardware management and process management. A mark scheme will not credit an invented name such as "storage management".

### Q4
Product A runs many different programs that the user chooses, installs and may run at the same time, so an Operating System is needed to share the processor, the memory and the peripherals between them. **[1]**

Product A stores many photographs and documents, so an Operating System is needed to organise them into files and directories and to find them again. **[1]**

Product A has a human user who gives commands to it, so an Operating System is needed to provide the user interface. **[1]**

Product B is dedicated to one task and runs a single fixed program on hardware that never changes, so that program can control the sensor and the fan directly and no Operating System is needed. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for each point below, to a maximum of 4. **Maximum 3 marks** for points about Product A and **maximum 3 marks** for points about Product B.
> 
> **Product A:**
> 
> - Runs many different programs, which the user can choose and install
> - ... so the Operating System must share the processor and the memory between them
> - Stores many files that must be organised and found again, which needs file management
> - Has a human user, so it needs a user interface
> - Has many different peripherals, so it needs the Operating System to manage them
> - The applications are written by other people and need a platform to run on
> 
> **Product B:**
> 
> - Is dedicated to a single task
> - Runs one fixed program held in ROM, which is not changed by the user
> - ... so that program can control its known, fixed hardware directly
> - Has no user interface and no user to interact with
> - Stores little or no data, so there are no files to manage
> - Has too little memory or processing power to run an Operating System // an Operating System would add cost for no benefit
> 
> Do not accept "Product B is too small". Size on its own is not a reason; the answer must say that the task is fixed, or that the hardware is known, or that there is no user.

> **[exam-tip]**
> Questions that compare two products are marked on both sides, and students almost always write four points about the tablet and nothing about the embedded system. Cambridge caps each side, so half of your marks are sitting in the product you skipped. Write at least one sentence about each.
> 
> Note also that "it is an embedded system so it does not need an Operating System" earns nothing. That is the fact the question gave you. The mark is for the reason behind it: one fixed task, one fixed program, and hardware that never changes.

### Q5
| Situation | Result of choosing Method B |
|---|---|
| The size of the executable file of each program | **Each executable file is smaller, because it does not contain the library routines** **[1]** |
| The number of copies of the library routines held in main memory while all three programs are running | **One copy only, because the single DLL file is loaded once and is available to all three programs** **[1]** |
| Whether the three programs must be recompiled after an error in a library routine is corrected | **No, because the DLL file is corrected independently of the programs that call it** **[1]** |
| Which of the three programs receive the correction | **All three, because the update applies to every program that uses the DLL file** **[1]** |

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for row 1: each executable file is smaller // the executable does not contain the library routines
> 
> **1 mark** for row 2: only one copy is held in main memory // the DLL is loaded once and shared by all three programs
> 
> **1 mark** for row 3: no, they do not need to be recompiled // the DLL is updated independently of the calling programs
> 
> **1 mark** for row 4: all three of them // every program that uses the DLL file
> 
> Accept the library code is stored outside the executable for row 1
> 
> Accept memory use is reduced for row 2 only if it is linked to a single shared copy
> 
> Do not accept each program keeps its own copy in memory for row 2. That is the result of Method A
> 
> Do not accept only the program that is running at the time for row 4

> **[exam-tip]**
> Check which method the table is asking about before you write anything. Most of the marks lost on comparison questions like this go to students who describe Method A in the Method B column.
> 
> The recompilation point is the one Cambridge asks for most often and it is easy to state backwards. With a DLL, the library file is the thing that changes; the programs that call it do not, so they do not need to be recompiled.

### Q6
The Operating System provides the platform on which application software runs. **[1]**

The word processor asks the Operating System to reach the hardware for it, for example to save a document to secondary storage, instead of containing its own code to control that hardware. **[1]**

The Operating System hides the complexities of the hardware from the program, so the same word processor can be used on computers built from different hardware. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - The Operating System provides a platform for application software to run on
> - The word processor uses the Operating System to reach the hardware, for example to save a file or to send data to a printer
> - ... so the program does not have to contain its own code for controlling that hardware
> - The Operating System hides the complexities of the hardware from the program and from the user
> - ... so the same word processor can run on computers built from different hardware
> - The Operating System allocates the block of RAM that the word processor needs
> - The Operating System decides when the word processor is given the use of the processor
> - The Operating System provides the user interface that the user needs in order to start the program and open a document
> 
> **[3 marks]**
> 
> Do not accept "the computer cannot work without an Operating System". This restates the question instead of answering it.
> 
> Do not accept "the Operating System runs the program" on its own. The answer must say what the Operating System provides or does for the program.

> **[exam-tip]**
> Most lost marks here come from listing the five management tasks instead of answering the question that was asked. The question is about one program and what that program cannot do for itself.
> 
> Build the answer around two ideas and you will nearly always reach three marks: the Operating System is the platform the program runs on, and the Operating System reaches the hardware on the program's behalf.

### Q7
The executable file of the program is smaller. **[1]**

This is because the executable does not contain the library routines themselves. **[1]**

The amount of main memory the program needs is also reduced, because the DLL is loaded into memory only once, or only when a routine inside it is required. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for stating that the executable file of the program is smaller
> 
> **1 mark** for the reason: the executable does not contain the library routines
> 
> **1 mark** for stating that the main memory required is reduced, because the DLL is loaded only once or only when it is required
> 
> Accept the library code is not built into the program for the second marking point.
> 
> Do not accept the DLL compresses the code. A DLL does not compress anything; the routines are simply held outside the executable file.
> 
> Do not accept the program runs faster on its own. Run speed is not what this question credits, and the DLL still has to be loaded before its routines can run.

> **[exam-tip]**
> Students often write that a DLL "saves space" and stop. That is one idea, not two marks. Say where the space is saved: on secondary storage, because the executable file no longer holds the routines, and in main memory, because the DLL is loaded only when it is needed.
> 
> Do not confuse a DLL with compression or with a back-up. It is the same library code, kept in its own file and linked to the program while the program is running.

### Q8
To hide the complexities of the hardware from the user. **[1]**

To provide a platform on which application software can run. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for hiding the complexities of the hardware from the user
> 
> **1 mark** for providing a platform for software to run
> 
> Do not accept "to provide a user interface". The stem has already given this purpose, so it cannot be given again.
> 
> Do not accept a bare list of management tasks such as "memory management, file management". Naming a task does not state what the Operating System is for.

> **[exam-tip]**
> The usual mistake here is to answer with the five management tasks, because those are the easiest part of this topic to remember. Cambridge treats a purpose and a management task as two different things. There are only three purposes: the user interface, hiding the complexities of the hardware, and providing a platform for software. Error checking and recovery is one of the management tasks, not a purpose.
> 
> The second mistake is to write down the purpose the stem has already given you. When a question says "state two other", it has taken one answer off the table.

### Q9
A program library is a collection of subroutines that have already been written and **tested**, so a developer does not have to check that they work. **[1]**

A developer can **import** the library into their own program so that its subroutines can be called. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for tested in the first gap
> 
> **1 mark** for import in the second gap
> 
> Accept compiled for the first gap.
> 
> Accept install or reference for the second gap.
> 
> Do not accept copy and paste for the second gap. The program imports or links to the library; the developer does not paste the library code into their own program.

> **[exam-tip]**
> The word library makes students think of storage, so a frequent wrong answer is that it is a place where a programmer keeps their finished programs. A program library holds subroutines, meaning procedures and functions, and the point of it is that they are already written and already tested.
> 
> Whenever you are asked what a program library is, get both ideas into the answer: the routines are pre-written, and another program can call them once it has imported the library.

### Q10
Task 1: disk contents analysis and disk repair software. **[1]**

It checks the disk, identifies the damaged areas and marks the bad sectors so they are not used again, and it restores the corrupted files so that the data is recovered. **[1]**

Task 2: file compression software. **[1]**

It reduces the size of the report files, so fewer bytes have to be sent and the transfer takes less time over the slow connection. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for naming disk contents analysis software or disk repair software for Task 1
> 
> **1 mark** for what it does in Task 1: identifies and marks bad sectors // restores corrupted files // recovers the lost data
> 
> **1 mark** for naming file compression software for Task 2
> 
> **1 mark** for what it does in Task 2: reduces the size of the files // so the transmission time is reduced
> 
> Accept disk analysis software or disk repair software on its own for Task 1.
> 
> Accept compression software or file compression for Task 2.
> 
> Do not accept defragmentation software for Task 1. Defragmentation rearranges files that are stored correctly; it does not detect or repair damaged areas of a disk.
> 
> Do not accept back-up software for Task 1. The stem states that no copy of the files exists, so there is nothing to restore from.

> **[exam-tip]**
> This kind of question tests whether you can match a symptom to the right utility, so read each symptom carefully. Errors when reading certain areas of a disk mean damaged sectors, which is a repair job. Slow loading of files that still open normally would mean fragmentation instead. Students who see the word disk and reach straight for defragmentation software lose both marks for that task.
> 
> Naming the utility is only half of each task. A name on its own earns one mark out of two, however correct it is, so always add what the software actually does.

### Q11
Saving and deleting files over a long period leaves the blocks of a single file spread across the disk, so the file is no longer stored in one continuous area. **[1]**

The defragmentation software rearranges the blocks so that each file occupies contiguous blocks, and it moves the free space together. **[1]**

The read/write head then has less movement to make, because it does not have to search for the next fragment of the file, so the file is loaded faster. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - The blocks of a file become spread across the disk // the file is fragmented // the file is not stored in contiguous blocks
> - The software rearranges the blocks of individual files so that each file is contiguous // it moves the free space together
> - There is no need to search for the next fragment or block of the file
> - Less read/write head movement is needed
> - So each file can be accessed or loaded faster
> 
> **[3 marks]**
> 
> Accept stored in one continuous area as an alternative to contiguous.
> 
> Do not accept it deletes unwanted files to make space. Defragmentation moves data; it does not delete it.
> 
> Do not accept it makes the files smaller. That is file compression, not defragmentation.

> **[exam-tip]**
> The mark scheme here is narrow and vague answers score nothing. "It tidies up the hard disk" and "it makes the computer run faster" both repeat the question instead of explaining it. The two words examiners are looking for are fragmented and contiguous.
> 
> Build the answer in three steps: what the disk looks like before, what the software does to it, and why that saves time. The link to reduced read/write head movement is the mark most students leave out.

### Q12
| Purpose | Utility software |
|---|---|
| To prepare a new hard disk for use by setting up the file system | **Disk formatter** **[1]** |
| To reduce the size of a file so that it uses less storage space | **File compression software** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for disk formatter in the first row
> 
> **1 mark** for file compression software in the second row
> 
> Accept formatter, hard disk formatter or disk formatting software for the first row
> 
> Accept compression software or file compression for the second row
> 
> Do not accept defragmentation software for the first row. Defragmentation rearranges files that are already stored on a disk; it does not set up the file system on a new disk
> 
> Do not accept back-up software for the second row. A back-up makes a copy of a file; it does not make the file smaller

> **[exam-tip]**
> Formatting and defragmenting are not the same job, and swapping them is the most common error on this topic. Formatting prepares a new disk and removes everything on it. Defragmenting rearranges files that are already stored there.
> 
> Cambridge awards no marks for brand names of software packages, so write the type of utility rather than the name of a product you have used.

### Q13
> **[mark-scheme]**
> The use of a program <u>library </u>(routines)

### Q14
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 1**)
> 
> - To hide the complexities of the hardware from the user
> - To provide a platform for software to run
> - To provide a user interface
**1 mark** for the name of the utility software

**2 marks **for the explanation

- Defragmentation software
- … because over time saving and deleting of small files fragments the disk
- ... the software makes (individual) files contiguous
- … so access time to the files is improved
- … because head movement is reduced
- Disk contents analysis/disk repair software
- … to identify and mark bad sectors
- ... to restore corrupted files
- ... to recover lost data (due to hardware failure)
- File compression
- … to reduce the size of files
- ... which saves storage and memory space // by example
- ... and reduces transmission time // by example
- Disk formatter
- … to prepare a disk for use // set up the file system
- ... to partition the disc
- ... to delete all the data from the disc

### Q15
> **[mark-scheme]**
> (i)** 1 mark** for:
> 
> Pre-written code/functions/routines that can be **imported/called** in another program
> 
> (ii) **1 mark** each to** max 4**:
> 
> - Maintenance not needed to be done by the programmer
> - ... because the DLL is separate from program
> - The calling program does not need recompilation by the programmer when a DLL file changes
> - ... because the DLL file can be updated independently of the calling program
> - … updates will apply to all programs that use the DLL file

### Q16
> **[mark-scheme]**
> **1 mark **each to **max 2**:
> 
> - Saves programming/testing time as code does not have to be written/rewritten from scratch // code does not have to be tested
> - Code is already tested so it is more robust/likely to work
> - The programmer does not need to maintain the library // library routines are updated automatically
> - Can perform complex calculations that the programmer may be unable to do
> - Makes code more easily readable

### Q17
> **[mark-scheme]**
> **1 mark** each to **max 4**
> 
> **Max 3** marks for each management task:
> 
> *Memory management*: **Max 3 marks**
> 
> - Stores data from all currently running programs concurrently in RAM
> - Stops the data from overwriting each other in RAM/primary storage
> - Decides which processes should be in main memory
> - Makes efficient use of memory
> 
> *Process management:**** *****Max 3 marks**
> 
> - Allows one process to be paused whilst another process can be actioned
> - Decides which process is to be run next
> - Switches between processes to allow them to share the use of the processor
> - Identification/description of scheduling

### Q18
> **[mark-scheme]**
> 1 mark for each bullet point (max 3)
> 
> e.g.
> 
> - Subroutines can be shared / reused
> - … between team members who are working independently
> - … without having to rewrite/re-test them which saves the programmers’ time
> - A program library provides continuity between programs/programmers
> - Individual programmers can contribute their specialisms to the library // Individual programmers can use the specialisms of others

### Q19
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 4**)
> 
> e.g.
> 
> - It manages the scheduling of processes // Decides which process is to be run next
> - Allows multi-tasking/multi-processing
> - Ensures fair access
> - Handles interrupts
> - Manages / allocates which resources the processes require
> - Facilitates the sharing and exchange of data between processes
> - Prevents interference between processes // conflict resolution

### Q20
> **[mark-scheme]**
> (i)** 1 mark** for each bullet point (**max 2**)
> 
> e.g.
> 
> - Secondary storage space is divided into file allocation units
> - Space on secondary storage is allocated to particular files
> - Maintains/creates directory structures
> - Specifies the logical method of file storage e.g. FAT or NTFS
> - Provides file naming conventions
> - Controls user access // implements access rights // implements password protection // Makes file sharing possible
> - Controls access to the file by other software
> - Specifies tasks that can be performed on a file e.g. open, close, delete, copy, create, move, etc
> - Allows searching for a file
> 
> (ii) **1 mark** for each bullet point (**max 2**)
> 
> - To allow data to be retrieved / restored when lost
> - To automatically make a duplicate copy of data…
> - …so the user does not have to remember to backup data
> - To make regular duplicate copies of data
> **[mark-scheme]**
> **1 mark **for each bullet point (**max 3**)
> 
> e.g.
> 
> - It saves development time for the student
> - … by using pre-written code
> - There is less testing to do // the routines are more likely to work correctly
> - … because they have already been tested and are error-free
> - It results in a more robust program
> - Subroutines can be used that they do not have the skill to write
> - … which enables a more complex program to be written
