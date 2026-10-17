---
note_id: "rn_SJxW6CtvZPzjnF9Q"
title: "Resource Management"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/16-system-software-/purposes-of-an-operating-system-os/resource-management
path: 16-system-software-/purposes-of-an-operating-system-os/resource-management
updated_at: "2025-05-16T11:55:46.516Z"
spec_point_ids: ["spcpt_CsXnJscqXWtXVj5V"]
spec_point_codes: []
guided_study: false
---

# Resource Management

## Resource management

> **Spec point** — `spcpt_CsXnJscqXWtXVj5V`

## Resource management

### How does an operating system maximise the use of resources?

- The Operating System (OS) is responsible for **managing the computer's hardware efficiently** to ensure the system runs smoothly
- This is known as **resource management** and is vital for:

  - **Maximising performance**
  - **Reducing bottlenecks**
  - **Ensuring multitasking** works correctly

#### Start-up and system loading

- When a computer is switched on, the **BIOS** (stored in ROM) runs a **bootstrap** program
- This loads the **kernel** and essential parts of the OS from the hard disk or flash storage into **main memory (RAM)**
- On tablets and smartphones, flash memory contains a read-only section for the OS and a second section for apps and user data
- **RAM** is then used to **execute apps** and **store active data**

#### Kernel

- The kernel is the **core of the OS** responsible for managing:

| **Area** | **Responsibility** |
|---|---|
| **Process management** | Schedules processes, allocates CPU time, handles multitasking |
| **Memory management** | Allocates RAM to processes, handles virtual memory, prevents clashes |
| **Device management** | Controls input/output devices using **device drivers** |
| **Interrupt handling** | Deals with interrupts from hardware (e.g. DMA controller or I/O devices) |
| **File management** | Handles reading/writing from files and file systems |

#### CPU resource management – scheduling

- The OS maximises CPU usage through **scheduling**, which allows multiple processes to be managed efficiently

  - **Multitasking** ensures that the CPU switches rapidly between processes
  - Different **scheduling algorithms** (e.g. round-robin, priority-based) are used to share CPU time fairly

#### Memory resource management

- RAM is **allocated dynamically** to active programs and system processes
- If RAM is full, the OS may use **virtual memory** on disk to simulate extra memory
- This allows **more programs to run** than would otherwise fit in RAM

#### Input/output management and DMA

- I/O devices are **much slower** than the CPU, so the OS optimises their use:

  - I/O operations are managed through **device drivers** and **interrupts**
  - The **Direct Memory Access (DMA) controller** allows data transfer between memory and devices **without CPU involvement**
  - This** frees up the CPU **to perform other tasks while data is being moved
  - When the transfer is complete, the DMA sends an **interrupt** to the CPU

| **Device** | **Typical data rate** |
|---|---|
| Keyboard | ~50 bps |
| Mouse | ~120 bps |
| Laser printer | ~1 Mbps |
| Hard disk | ~100 Mbps |

#### Hiding hardware complexity

- The OS provides a **user-friendly interface** and handles the complexity of interacting with hardware:

  - **GUIs** make tasks like file transfers easy (e.g. drag-and-drop instead of command-line)
  - **Device drivers** handle communication with specific hardware
  - Users **don’t need to know** technical commands, the OS abstracts this complexity

#### Summary

| **Resource** | **Technique used** |
|---|---|
| **CPU** | Scheduling, multitasking, process control |
| **Memory** | Allocation, paging, virtual memory |
| **I/O** | Interrupts, DMA, buffering, driver management |
| **User interface** | Abstracts complexity through GUI and system utilities |
| **Storage** | File system management, read/write optimisation via caching and buffering |
