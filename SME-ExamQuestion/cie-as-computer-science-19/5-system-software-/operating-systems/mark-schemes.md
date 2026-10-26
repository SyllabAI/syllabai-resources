# Mark Schemes — Operating Systems
**5. System Software** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (8 questions)


### Q1
> **[mark-scheme]**
> The use of a program <u>library </u>(routines)

### Q2
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

### Q3
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

### Q4
> **[mark-scheme]**
> **1 mark **each to **max 2**:
> 
> - Saves programming/testing time as code does not have to be written/rewritten from scratch // code does not have to be tested
> - Code is already tested so it is more robust/likely to work
> - The programmer does not need to maintain the library // library routines are updated automatically
> - Can perform complex calculations that the programmer may be unable to do
> - Makes code more easily readable

### Q5
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

### Q6
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

### Q7
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

### Q8
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
