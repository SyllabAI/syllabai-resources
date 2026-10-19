---
note_id: "rn_jrR4gMKy8RymvhC6"
title: "Operating Systems"
source: https://www.savemyexams.com/igcse/ict/edexcel/17/revision-notes/1-digital-devices/software/operating-systems
path: 1-digital-devices/software/operating-systems
updated_at: "2024-05-31T10:23:41.092Z"
spec_point_ids: ["spcpt_gQpvmRN9WNnK4JG3"]
spec_point_codes: []
guided_study: false
---

# Operating Systems

## Role & function of an operating system

> **Spec point** — `spcpt_gQpvmRN9WNnK4JG3`

## Role & function of an operating system

### What is an operating system?

- An operating system (**OS**) is software that **provides an interface between the user and the hardware** in a computer system
- An operating system **hides the complexities of the hardware** from the user, for example:

  - A user does not need to know 'where' on secondary storage data is kept, just that it is saved for when they want it again
- There are two main types of operating systems:

  - **Single User Operating System**
  - **Network Operating Systems (NOS)**
- An operating system has many functions, this includes:

  - **Memory management**
  - **Resource management**
  - **Security**
  - **Print spooling**

#### Single user and network operating systems

| Single user | Network |
|---|---|
| Allow for a** single general user** | Provide access to** network storage** and **shared resources** |
| **No option to customise** user interface for different users | **Server is sent requests** when users log in with usernames and passwords |
| Typically used in a **household appliances** | **User accounts are kept separate** to ensure users cannot access each other's files |

#### Resource management

- **Memory**

  - Memory management is a process carried out by the operating system **allocating main memory (RAM) between different programs** that are **open at the same time**
  - The OS is responsible for **copying programs and data from secondary to primary storage** as it is needed
  - **Programs and data require different amounts of RAM** to operate efficiently and the OS manages this process
  - **RAM is allocated** based on **priority and fairness**, for example, system applications (essential) may have a higher priority than user applications
  - The OS **dynamically manages the memory**, adjusting allocation as needed to maintain optimal system performance
  - Memory management makes **multitasking **possible
- **Processor**

  - Processor management is a process carried out by the operating system **dividing time** (time slicing) in to small chunks and **allocating them to different programs**
  - The CPU can only execute **one instruction at a time**, it can can execute **billions of them in one second.**
  - The OS **decides **what programs get access to the CPU to give a user the perception of being able to use multiple programs at the same time (**multitasking**)
- **Inputs & outputs**

  - Input/output (**I/O**) management is a process carried out by the operating system **managing the way** input and output devices** interact with software**
  - The OS **allocates system resources** to inputs/outputs to ensure** efficient operation**
  - I/O management makes** plug-and-play** (PnP) functionality possible, **automatically detecting and configuring new inputs/outputs **without the need for manually installing device drivers or power cycling the system
- **Files**

  - File management is a process carried out by the operating system** creating, organising, manipulating and accessing files and folders on a computer system**
  - The OS **manages where data is stored** in both** primary and secondary** **storage**
  - File management gives the user the ability to:
  
    - **Create files/folders**
    - **Name files/folders**
    - **Rename files/folders**
    - **Copy files/folders**
    - **Move files/folders**
    - **Delete files/folders**
  - The OS allows users to control who can access, modify and delete files/folders (**permissions**)
  - The OS provides a **search facility** to find specific files based on various criteria

#### Security

- Security management is a process carried out by the operating system **enabling different users to log onto a computer**
- A system administrator is able to **allocate **different ***access rights*** for different users on a network
- The OS is able to **maintain settings** for individual users, such as desktop backgrounds, icons and colour schemes
- The OS **audits **(keeps a log of) files created by users, accesses, edits and deletes
- Operating systems can provide **software firewalls **

#### Print spooling

- Print spooling is a process carried out by the operating system** when printing is required**
- The spooler creates a **temporary holding area** (**queue**) for the print job
- Queuing pages** increases efficiency**

> **Worked Example**
> Explain one reason an administrator would use a network operating system to manage users.
> 
> **[2]**
> 
> **Answer**
> 
> > *A linked explanation such as:*
> 
> - Multiple people can use the same computer **[1]** because users can be added/deleted **[1]**
> - Only specific users can securely access their storage space **[1]** because user permissions can be edited **[1]**
> - Only certain users can install programs / access certain files **[1]** because user permissions can be enforced **[1]**
> - The limited storage on the machine can be shared **[1]** because the amount of resources/storage each user can access can be controlled **[1]**
> 
> > *Marks can be awarded across mark points*
