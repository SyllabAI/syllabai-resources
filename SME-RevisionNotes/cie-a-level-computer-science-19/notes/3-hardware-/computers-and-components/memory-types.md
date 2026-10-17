---
note_id: "rn_CDtg87dQC5VFTm3H"
title: "Memory Types"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/3-hardware-/computers-and-components/memory-types
path: 3-hardware-/computers-and-components/memory-types
updated_at: "2025-04-22T14:17:18.695Z"
spec_point_ids: ["spcpt_ZS5HMCnYKQ27P6Bq", "spcpt_JHK46SwrfS7pz7kj", "spcpt_m5VY2BTxhZPwTcmP"]
spec_point_codes: []
guided_study: false
---

# Memory Types

## RAM vs ROM

> **Spec point** — `spcpt_ZS5HMCnYKQ27P6Bq`

## RAM vs ROM

### What is RAM?

- RAM (Random Access Memory) is **primary storage** that is directly connected to the CPU and holds the **data **and **instructions **that are **currently in use**
- RAM is **volatile **which means the contents of RAM are lost when the power is turned off
- For the CPU to access the data and instructions they must be **copied from secondary storage**
- RAM is **very fast** working memory, much faster than secondary storage
- RAM is **read/write **which means data can be read from and written to
- In comparison to ROM, it has a much **larger capacity**

### What is ROM?

- ROM (Read Only Memory) is **primary storage** that holds the **first instructions** a computer needs to **start up **(Bootstrap)
- ROM contains the **BIOS **(Basic Input Output System)
- ROM is a small **memory chip** located on the computers ***motherboard***
- ROM is **fast** memory, much faster than secondary storage but **slower than RAM**
- ROM is **non-volatile **which means the contents of ROM are not lost when the power is turned off
- ROM is **read only **which means data can only be read from
- In comparison to RAM, it has a much **smaller capacity**

## Differences between RAM & ROM

| **Feature** | **RAM** | **ROM** |
|---|---|---|
| **Speed** | Very fast | Fast (slower than RAM) |
| **Capacity** | Gigabytes (GB) | Megabytes (MB) |
| **Stores** | Programs and data in use | Bootstrap (start-up instructions) |
| **Read/Write** | Read & write | Read only |
| **Volatile/Non-volatile** | Volatile | Non-volatile |

## SRAM vs DRAM

> **Spec point** — `spcpt_JHK46SwrfS7pz7kj`

## SRAM vs DRAM

### What is SRAM?

- SRAM (Static RAM) is a form of RAM that **keeps data** as long as power is on
- SRAM is made from **flip-flops** so there is no need for constant refreshing
- SRAM is used in places where **speed** is more important than storage size
- An example of where SRAM is used is:

  - **Cache memory**, where quick access to data is most important

- **Very fast** – faster than DRAM
- **Uses less power**, good for **low-power devices**
- **Expensive** to make
- **Takes up more space** – lower storage capacity compared to DRAM

### What is DRAM?

- DRAM (Dynamic RAM) is a form of RAM that stores each bit in a **tiny capacitor**
- DRAM needs **constant refreshing** to keep the data
- DRAM is commonly used as:

  - **Main memory (RAM)**, where larger amounts of cheaper storage is required
- **Cheaper** to produce than SRAM
- **Higher capacity** – can fit **more memory in less space**
- **Slower** than SRAM, needs time to refresh data
- **Uses more power**, especially during refreshing cycles

## PROM vs EPROM vs EEPROM

> **Spec point** — `spcpt_m5VY2BTxhZPwTcmP`

## PROM vs EPROM vs EEPROM

### What is PROM, EPROM & EEPROM?

- PROM, EPROM and EEPROM are all **types of ROM** that are **programmed and reprogrammed in different ways**
- Each type has a **specific application** in difference devices

| **Feature** | **PROM** | **EPROM** | **EEPROM** |
|---|---|---|---|
| **Can be reprogrammed?** | No – programmed once only | Yes – can be erased and rewritten | Yes – can be erased and rewritten |
| **Erased using** | Cannot be erased | UV light | Electric voltage |
| **Must be removed from device?** | No | Yes – must be removed from the device | No – can be erased in place |
| **Erased all at once?** | Not applicable | Yes – entire chip is erased | No – specific parts can be erased |
| **Common use** | Permanent firmware | Reprogrammable chip development | Flash memory, BIOS chips |
| **Examples** | Remote controls, basic calculators, early model washing machines | Arcade machines (older models)<br><br>Early games consoles | BIOS chips in computers, Smart cards, remote key fobs, flash memory like USB sticks and SSDs |

> **Worked Example**
> A computer has hardware and software.
> 
> The hardware includes different types of memory.
> 
> Complete the description of computer memory. **[5]**
> 
> *Random Access Memory (RAM) and Read Only Memory (ROM) are both examples of ......................................................................... memory. *
> 
> *One item that is stored in RAM is ......................................................................... . One item that is stored in ROM is ......................................................................... . RAM can be either Static RAM (SRAM) or Dynamic RAM (DRAM). *
> 
> *SRAM uses transistors arranged as ......................................................................... . DRAM uses transistors and .....................*
> 
> **Final answer:** **Answer**
> 
> *Random Access Memory (RAM) and Read Only Memory (ROM) are both examples of ***primary*** memory. *
> 
> *One item that is stored in RAM is ***currently running software/data/part of the OS***.*
> 
> * One item that is stored in ROM is the ***start-up/boot-up instructions/BIOS***. *
> 
> *RAM can be either Static RAM (SRAM) or Dynamic RAM (DRAM). *
> 
> *SRAM uses transistors arranged as ***flip-flops***. *
> 
> *DRAM uses transistors and ***capacitors***.*
