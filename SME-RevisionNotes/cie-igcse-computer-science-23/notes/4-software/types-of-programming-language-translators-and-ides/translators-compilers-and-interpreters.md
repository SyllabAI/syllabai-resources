---
note_id: "rn_tMWTqWNMZxb3kHdp"
title: "Translators, Compilers & Interpreters"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/4-software/types-of-programming-language-translators-and-ides/translators-compilers-and-interpreters
path: 4-software/types-of-programming-language-translators-and-ides/translators-compilers-and-interpreters
updated_at: "2026-04-30T14:36:42.228Z"
spec_point_ids: ["spcpt_ckpPNg4bVX7ntq5S"]
spec_point_codes: []
guided_study: false
---

# Translators, Compilers & Interpreters

## Translators, Compilers & Interpreters

> **Spec point** — `spcpt_ckpPNg4bVX7ntq5S` · "3 Describe the operation of a compiler and an
interpreter, including how high-level language is
translated by each and how errors are reported
4 Explain the advantages and disadvantages of a
compiler and an interpreter"

## Translators, Compilers & Interpreters

### What is a translator?

- A translator is a program that **translates **program **source code **into **machine code** so that it can be executed directly by a processor
- **Low-level languages** such as** assembly code** are translated using an **assembler**
- **High-level languages** such as **Python **are translated using a **compiler **or **interpreter**

### What is a compiler?

- A compiler translates high-level languages into machine code **all in one go**
- Compilers are generally used when **a program is finished** and has been checked for syntax errors
- Compiled code can be **distributed (creates an executable) **and run **without the need for translation software**
- If compiled code contains any errors, after fixing, it **will need re-compiling**

| **Advantages** | **Disadvantages** |
|---|---|
| Speed of execution | Can be memory intensive |
| Optimises the code | Difficult to debug |
| Original source code will not be seen | Changes mean it must be recompiled |
|   | It is designed solely for one specific processor |

### What is an interpreter?

- An interpreter translates high-level languages into machine code **one line at a time**
- Each line is executed after translation and if **any errors are found**, the **process stops**
- Interpreters are generally used when a program** is being written** in the development stage
- Interpreted code is more **difficult to distribute** as **translation software is needed for it to run**

| **Advantages** | **Disadvantages** |
|---|---|
| Stops when it finds a specific **syntax error** in the code | Slower execution |
| Easier to debug | Every time the program is run it has to be translated |
| Require less RAM to process the code | Executed as is, no optimisation |

> **Worked Example**
> A computer program is written in a high-level programming language.
> 
> (a) State why the computer needs to translate the code before it is executed.**[1]**
> 
> (b) Either a compiler or an interpreter can translate the code. Describe two differences between how a compiler and an interpreter would translate the code.**[2]**
> 
> **How to answer this question**
> 
> - (a) what type of language does a computer understand?
> - (b) the keyword is 'how'
> 
> **Answer**
> 
> **(a)**
> 
> - **To convert it to binary/machine code**
> - **The processor can only understand machine code**
> 
> **(b)**
> 
> - **Compiler translates all the code in one go...**
> - **...whereas an interpreter translates one line at a time**
> - **Compiler creates an executable...**
> - **...whereas an interpreter does not/executes one line at a time**
> - **Compiler reports an error at the end...**
> - **...whereas an interpreter stops when it finds an error**
