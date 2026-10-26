---
note_id: "rn_zmNM9QRRPr4XWgNk"
title: "Program libraries"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/5-system-software-/operating-systems/program-libraries
path: 5-system-software-/operating-systems/program-libraries
updated_at: "2025-06-03T10:29:35.793Z"
spec_point_ids: ["spcpt_g6TNRdCzR526mkHk"]
spec_point_codes: []
guided_study: false
---

# Program libraries

## Program libraries

> **Spec point** — `spcpt_g6TNRdCzR526mkHk`

## Program libraries

### What is a program library?

- A program library is a **collection of pre-written code** (called **library routines**) that programmers can **reuse** in their own software
- These routines can **perform common tasks** such as:

  - **Sorting**
  - **Displaying graphics**
  - **Playing sounds**
  - **Managing data**
- Advantages of using program libraries includes:

| **Advantage** | **Explanation** |
|---|---|
| **Saves development time** | Pre-written routines can be reused, so programmers don’t need to write common functions from scratch |
| **Promotes code reuse** | Well-tested routines can be used in multiple programs, reducing duplication |
| **Improves reliability** | Library routines are usually thoroughly tested and debugged, reducing the chance of errors |
| **Easier maintenance** | Updates to a library routine automatically benefit all programs that use it (especially with **DLLs**) |
| **Efficient memory usage** | **Dynamic link libraries (DLLs)** are only loaded when needed at runtime, saving system resources |
| **Standardisation** | Promotes consistency in how common tasks (e.g. file handling, sorting) are implemented |

### What is a DLL?

- A **Dynamic Link Library (DLL)** is a file that contains **pre-written code**, such as **functions or routines**, that can be **used by multiple programs** at **runtime**

| **Aspect** | **Advantages** | **Disadvantages** |
|---|---|---|
| **Program Size** | Reduces program size by keeping reusable code separate | - |
| **Memory Usage** | Saves memory by sharing DLLs between programs | - |
| **Code Reuse** | Encourages reuse of common routines (e.g. sorting, sound) | - |
| **Modularity** | Supports modular design for easier development and maintenance | - |
| **Ease of Updates** | Update a DLL once to improve all programs that use it | Can cause **version conflicts** if newer DLLs aren’t compatible |
| **Dependencies** | External DLLs can be reused by many applications | Program may **fail to run** if a required DLL is **missing** |
| **Security** | - | Malicious or altered DLLs can pose **security risks** |
| **Debugging** | - | Errors in DLLs can be **hard to trace** across multiple programs |

> **Worked Example**
> Jennifer is writing a computer program for her A Level homework.
> 
> Jennifer uses a program library to help her write her computer program.
> 
> Describe how a program library can be used while writing a computer program. **[2]**
> 
> **Final answer:** **Answer**
> 
> - Program libraries store pre-written functions and routines **[1 mark]**
> - The program library can be referenced/imported **[1 mark]**
> - The functions/routines can be called in her own program **[1 mark]**
