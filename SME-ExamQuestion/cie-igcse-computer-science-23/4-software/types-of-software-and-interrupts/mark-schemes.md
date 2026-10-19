# Mark Schemes — Types of Software & Interrupts
**4. Software** · Cambridge (CIE) IGCSE computer-science (0478 & 0984)


## Exam Questions (10 questions)


### Q1
The purpose of firmware is to:

Any **one **of the following:

- Permanently store instructions (in ROM) **[1 mark]**
- Stores instructions to boot up/start up the computer **[1 mark]**
- Provides the operating system with a platform to run on **[1 mark]**
- Controls/manages/allows communication with hardware **[1 mark]**
- Store instructions securely (to stop them being easily corrupted) **[1 mark]**
Examples of firmware include

Any **one **of the following:

- Bootstrap **[1 mark]**
- Bootloader **[1 mark]**
- BIOS **[1 mark]**
- Operating system (in embedded system) **[1 mark]**
- Programs (in embedded systems) **[1 mark]**
Example of utility software include

Any **two **of the following:

- Operating system **[1 mark]**
- Utility software **[1 mark]**
- Two valid examples of utility software **[1 mark]**

### Q2
> **[mark-scheme]**
> Role of peripheral management:
> 
> Any 3 from:
> 
> - Handles the way hardware peripherals interact with the software
> - … ensuring that each peripheral operates efficiently
> - … by allocating the necessary system resources
> - Managing data transfer between the computer and the peripheral device
> - Coordinating the operation of multiple peripherals simultaneously
> 
> **[3 marks]**
> 
> PnP functionality:
> 
> - Allows the operating system to automatically detect and configure new peripherals when they are connected
> 
> OR
> 
> - Users do not need to manually install device drivers or restart the system for the peripherals to work
> 
> OR
> 
> - … simplifying the setup and use of hardware **[1 mark]**
> 
> Maximum 3 marks if no mention of PnP functionality
> 
> "Explain" requires candidates to provide a reason or justification for the role of peripheral management, not just a simple statement

> **[exam-tip]**
> Make sure you address both parts of the question: the general role of peripheral management and how it facilitates plug-and-play. Many students focus only on the general role and forget to mention PnP, which limits them to a maximum of 3 marks. A good approach is to write a few points about what peripheral management does (e.g. resource allocation, coordinating devices) and then dedicate at least one clear point to how PnP works, such as automatic detection and configuration of new hardware without needing to manually install drivers.

**[4 marks]**

### Q3
The difference between a GUI and a CLI is described as:

**Graphical User Interface (GUI): **

- Allows users to interact with the computer using graphical elements like windows, icons, and buttons **[1 mark]**
- Any valid example **[1 mark]**

**Command-Line Interface (CLI): **

- Allows users to interact by typing commands into a text-based interface **[1 mark]**
- Any valid example **[1 mark]**

> **[mark-scheme]**
> - One mark for **description **and one mark for **valid example**

### Q4
An operating system is defined as:

- Software that manages computer hardware **[1 mark]** *accept: controls / operates / runs the hardware*
- Provides a platform for running application software **[1 mark]** *accept: provides an interface between the user/applications and the hardware*

> **[exam-tip]**
> For two marks you need two distinct points, so make sure you mention both managing the hardware and providing a platform or interface for applications
> 
> A vague definition on its own is unlikely to score, so state clearly that it is software
Functions of an operating system include:

Any **two **of the following:

- File management **[1 mark]**
- Handling interrupts **[1 mark]**
- User interface / HCI (human computer interaction) **[1 mark]**
- Peripheral management & device drivers **[1 mark]**
- Memory management & multitasking **[1 mark]**
- Providing a platform for running applications **[1 mark]**
- Providing system security **[1 mark]**
- User management **[1 mark]**

> *Accept a clear description of a listed function, e.g. "move files and folders" for file management*

### Q5
Examples of functions of the operating system include:

Any **two** of the following (1 mark for function name, max 2 marks per description):

**User interface ****[1 mark]**

- allows the user to communicate with the hardware **[1 mark]**
- e.g. graphical user interface (GUI) /command prompt **[1 mark]**
- allows the user to input data **[1 mark]**
- outputs data to the user **[1 mark]**

**Memory management/multitasking ****[1 mark]**

- moves data between RAM and VM / manages/allocates RAM between different programs **[1 mark]**
- gets data from RAM / prevents two programs accessing the same memory location **[1 mark]**
- stores data to RAM / enables multitasking **[1 mark]**

**Peripheral management/device drivers ****[1 mark]**

- allows the installation of drivers to communicate with the peripherals **[1 mark]**
- sends data to/from peripherals **[1 mark]**

**User management ****[1 mark]**

- allows the setting up of accounts **[1 mark]**
- security/setting of password **[1 mark]**
- set different access rights **[1 mark]**

**File management ****[1 mark]**

- creation/editing/renaming of files **[1 mark]**
- creation/editing/renaming of folders **[1 mark]**
- movement of files/folders **[1 mark]**

**Handling interrupts ****[1 mark]**

- responding to an event that requires immediate CPU attention **[1 mark]**
- ensuring smooth system operation by processing interrupts **[1 mark]**

**Platform for running applications ****[1 mark]**

- allows application software access to system resources **[1 mark]**

**Providing system security ****[1 mark]**

- offer features like password protection, firewalls, virus scanning, and file encryption** [1 mark]**

> **[exam-tip]**
> A sample six mark response could be:
> 
> *The user interface is one function of the operating system. A user interface provides the user with a graphical interface which allows them to interact with the computing, inputting and outputting data.*
> 
> *A second function of an operating system is memory management. Memory management allows data to move between the RAM and virtual memory when RAM becomes full. It also allocates space in RAM for currently in-use programs.*
> 
> - For a 'describe' question, vague statements score no marks — give specific technical detail rather than just restating the function name.
> - Use the exact function labels (e.g. peripheral management, providing system security), not loose terms like 'hardware' or 'security'.

### Q6
Examples of when interrupts would be generated include:

Any **two **of the following:

- Division by zero **[1 mark]**
- Two processes trying to access the same memory location **[1 mark]**
- A hardware device signal / input such as a key press or mouse click **[1 mark]**
- A printer jam / paper out / device requiring attention **[1 mark]**
- Any valid example of an error message (two examples can be awarded) **[1 mark]**
- Any valid example of a change of task (two examples can be awarded) **[1 mark]**

> **[exam-tip]**
> Name a specific event that triggers an interrupt, not a general type such as 'hardware' or 'a task needing attention'
> 
> Avoid vague network/external issues like WiFi problems, and make sure you give two clear examples

### Q7
**System ****[1 mark] **software provides the services that the computer requires; an example is utility software.

**Application ****[1 mark]**** **software is run on the operating system.

The **operating ****[1 mark]**** **system is run on the firmware, which is run on the **hardware ****[1 mark]**.

### Q8
The type of software that runs directly on the operating system is:

- Application software **[1 mark]**

### Q9
Examples of software that can be stored on the SSD include:

Any **two **of the following:

- Operating system **[1 mark]**
- Application software **OR** by example **[1 mark]**
- Utility software **OR** by example **[1 mark]**

> **[exam-tip]**
> Name a specific software category or example, not vague answers like 'computer programs'
> 
> Remember that files such as text documents are data, not software

### Q10
**Final answer:** **The correct answer is B**

- **B **is correct as the bootstrap contains the initial boot-up instructions for a computer **[1 mark]**
- **A **is incorrect as application software is software designed to carry out a specific task or complete a job
- **C **is incorrect as a hard disk drive is a secondary storage device
- **D **is incorrect as a MAC address is a unique identifier for a network capable device
