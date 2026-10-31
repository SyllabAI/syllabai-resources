# Software

## Types of Software and Interrupts

### **Types of Software**

1. **System Software** e.g. Operating System, Utility programs and device drivers
2. **Application Software** e.g. spreadsheet, word processor, etc.

### **System Software:**

* these are a set of programs which control and manage the operations of hardware
* gives a platform for other software to run
* it is required to allow hardware and software to run without problems
* provides a human-computer interface (HCI) to the user
* controls the allocation and usage of hardware resources

### **Application Software:**

* allows a user to perform specific tasks using the computer’s resources
* maybe a single program (for example, NotePad) or a suite of programs (for example, Microsoft Office)
* user can execute the software when they require, and it is mostly not automatic

### **Examples**

**System Software:**

* Compiler: Translates high-level language into machine code, allowing for direct use by a computer to perform tasks without re-compilation.
* Linker: Combines object files produced by a compiler into a single program, allowing the use of separately written code modules in the final program.
* Device driver: Software that enables hardware devices to communicate with a computer's operating system, without which a device like a printer would be unable to work.
* Operating system: Software that manages basic computer functions such as input/output operations, program loading and running, and security management, making computers more user-friendly.
* Utility programs: Software that manages, maintains, and controls computer resources by carrying out specific tasks, such as virus checking, disk repair and analysis, file management, and security.

**Application Software:**

* Word Processor: Software used for manipulating text documents, including creating, editing, and formatting text with tools for copying, deleting, spell-checking, and importing images.
* Spreadsheet: Organizes and manipulates numerical data using a grid of lettered columns and numbered rows, with each cell identified using a unique combination of columns and rows. It can calculate using formulas, produce graphs, and do modelling and "what if" calculations.
* Database: Software used to organize, analyze, and manipulate data consisting of one or more tables that hold records and fields. It provides the ability to query and report on data and add, delete, and modify records in a table.
* Control and Measuring Software: A program designed to interface with sensors and allow a computer or microprocessor to measure physical quantities and control applications by comparing sensor data with stored data and altering process parameters accordingly.
* Apps: Software designed to run on mobile phones or tablets, downloaded from an "App Store" and ranging from games to sophisticated software such as phone banking. Common examples include video and music streaming, GPS, and camera facilities.
* Photo and Video Editing Software: Software that allows users to manipulate digital photographs or videos, including changing colour, brightness, and contrast, applying filters and other enhancements, and creating transitions between clips.
* Graphics Manipulation Software: Software that allows the manipulation of bitmap and vector images, with bitmap graphics editors changing pixels to produce a different image, while vector graphics editors manipulate lines, curves, and text to alter the stored image as required.

### **Interrupts**

An interrupt is a signal sent to the microprocessor, either from a device or software, prompting the microprocessor to pause its ongoing tasks and handle the interrupt temporarily. Various factors can trigger interrupts, including:

* **Timing signals:** Scheduled signals prompt the microprocessor to pause and handle tasks at specific intervals.
* **Input/Output processes:** Events such as a disk drive or printer requiring additional data cause an interruption in the microprocessor's activities.
* **Hardware faults:** Issues like a paper jam in a printer, signalling the microprocessor to halt its operations and address the hardware problem.
* **User interaction:** Instances like a user pressing specific keys on a keyboard (e.g., <CTRL><ALT><BREAK>), leading to an interrupt in the system's operation.
* **Software errors:** Problems such as missing .exe files needed to initiate a program, conflicts like two processes accessing the exact memory location, or attempts to divide by zero. These errors trigger interrupts, prompting the microprocessor to handle the issues.

![](../../../assets/3d4fb71d225e-64560919b4157e4f2217296414060b3df227a3d06ea8cf73.22)`Source: Cambridge IGCSE and O Level Computer Science - Second Edition (Hodder Education)`