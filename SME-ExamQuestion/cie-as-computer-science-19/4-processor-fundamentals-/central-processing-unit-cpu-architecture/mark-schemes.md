# Mark Schemes — Central Processing Unit (CPU) Architecture
**4. Processor Fundamentals** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (7 questions)


### Q1
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

### Q2
> **[mark-scheme]**
> **1 mark** for naming a correct port** 2 marks** for matching justification
> 
> - USB
> - …has fast data transfer speeds for data (to the headset)
> - …is a universal/popular cable // universal standard
> - HDMI
> - …allows video and audio to be transferred (on the same cable)
> - …convenience of HDMI as no need for two cables

### Q3
> **[mark-scheme]**
> **1 mark** for each bullet point (max 1)
> 
> - USB / Universal Serial Bus
> - HDMI

### Q4
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

### Q5
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

### Q6
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

### Q7
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
