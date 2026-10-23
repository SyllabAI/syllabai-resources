---
note_id: "rn_vFRgrhD3XT32GPhV"
title: "Paper 1: Theory Fundamentals"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/paper-guides/paper-1-theory-fundamentals
path: 21-exam-skills/paper-guides/paper-1-theory-fundamentals
updated_at: "2026-10-16T11:58:10.435Z"
spec_point_ids: ["spcpt_pfN4szScSmvDjSDN", "spcpt_kC6s9Jfz2CmDRGD2", "spcpt_yZvfddG8jCC6NRcz"]
spec_point_codes: []
guided_study: false
---

# Paper 1: Theory Fundamentals

## Paper 1 overview

> **Spec point** — `spcpt_pfN4szScSmvDjSDN`

## Paper 1 overview

### What is in 9618 Paper 1?

- Paper 1 Theory Fundamentals is a **1 hour 30 minute written paper** worth **75 marks**
- It is **50% of the AS Level** and **25% of the A Level**
- It covers syllabus sections 1 to 8:

  - information representation
  - communication
  - hardware
  - processor fundamentals
  - system software
  - security, privacy and data integrity
  - ethics and ownership
  - databases
- You answer **all** questions; there is no choice
- **Calculators are not allowed**, so every conversion and file size calculation is done by hand
- Questions range from 1-mark recall to longer answers set in a scenario, such as a company, a device or a network
- For advice that applies to every 9618 paper, see:

  - [CIE A Level Computer Science exam tips](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/exam-technique/exam-tips/)
  - [9618 command words](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/exam-technique/command-words/)

## Question types and how to answer them

> **Spec point** — `spcpt_kC6s9Jfz2CmDRGD2`

## Question types and how to answer them

### How do you answer number conversion questions?

- Typical stems include:

  - "Convert the denary number 241 to hexadecimal"
  - "Convert the two's complement binary number into denary"
  - "Subtract the denary number 10 from the denary number 100 using binary subtraction. Show your working."
- Check **which representation** the question gives you before you start

  - Examiners reported a very common wrong answer where students treated an unsigned binary integer as **Binary Coded Decimal (BCD)** and converted it directly
  - Another common error was converting a binary integer into **denary** when the question asked for **hexadecimal**
- If the question says "using binary subtraction" (or binary addition), the working **must be in binary**

  - Examiners give **no credit** for doing the calculation in denary and converting the answer to binary
  - Watch the order: 100 − 10 is not the same as 10 − 100, and examiners report this being reversed

### How do you answer file size calculations?

- Typical stems include:

  - "Calculate the file size of a bitmap image... Give your answer in kibibytes. Show your working."
  - "Calculate the file size of the recording. Give your answer in megabytes and show your working."
- Mark schemes usually award **1 mark for the working** and **1 mark for the answer**
- Follow three steps:

  - Multiply the values given (for an image: width × height × bit depth)
  - **Divide by 8** if the bit depth is in bits and the answer is in bytes; examiners report that a frequent wrong answer **missed this division**
  - Divide by 1000 or 1024 for each step up in units, depending on which unit the question asks for
- Check the unit the question asks for, as the decimal and binary prefixes are different

| Decimal unit | Size | Binary unit | Size |
|---|---|---|---|
| kilobyte (kB) | 1000 bytes | kibibyte (KiB) | 1024 bytes |
| megabyte (MB) | 1000 kB | mebibyte (MiB) | 1024 KiB |
| gigabyte (GB) | 1000 MB | gibibyte (GiB) | 1024 MiB |

- Examiners also report students confusing these units, for example swapping kibibytes and kilobytes
- Without a calculator, choose an order of working that keeps the numbers simple; for example, divide by 8 and by 1024 early when the values are powers of 2

### How do you answer bit depth, resolution and sampling questions?

- These questions usually ask about the **effect** of a change, not the definition
- Say clearly **whether the value increases or decreases**, then describe the effect on the image or the sound
- Examiners report that many answers about changing bit depth only talked about **file size** when the question asked how the **image** is affected
- Restating the definition ("increasing the bit depth increases the number of bits per pixel") is not enough; say what changes for the user, such as more colours being available

### How do you answer logic gate and truth table questions?

- Typical stems include "Draw the logic circuit for the logic expression" and "Complete the truth table for the logic expression"
- Draw each gate with the **correct shape**

  - Examiners report that OR and AND gates were often hard to tell apart, and that NOT gates were drawn **without the circle**
- Draw the circuit **exactly as the expression is written**

  - Examiners report missing NOT gates, and students replacing (NOT R) OR (NOT M) with a single NOR gate, which is a different expression
- In a truth table, list the inputs in binary counting order (000, 001, 010...) so that no row is missed

### How do you answer questions set in a scenario?

- Many Paper 1 questions describe a situation, such as a video doorbell, a laser printer or a company network, then ask you to describe or explain something about it
- Every point should link to the scenario; a textbook definition on its own often scores nothing
- For 2-mark questions, give **two different points**; examiners report answers where the same point was written twice in different words. If the answer space is numbered, only the first answer in each space is marked
- Read the scenario details carefully, as they often tell you which answer is expected (for example, a question about a bitmap image needs an answer about pixels and colours, not about text characters)

### How do you answer ethics and ownership questions?

- Typical stems include "Explain the reasons why the computer programmer needs to act ethically towards colleagues" and "Explain why it is important for a programmer to join a professional ethical body"
- Learn what a ***professional ethical body*** is (the syllabus names the British Computer Society (BCS) and the Institute of Electrical and Electronic Engineers (IEEE)); examiners report students thinking it was an employer or part of the company
- When a scenario describes someone acting unethically, explain **why** their action was unethical; examiners report that answers only saying what the person *should* have done did not answer the question

### How do you answer assembly language trace questions?

- Typical stems ask you to complete a trace table showing the contents of the Accumulator (ACC), the Index Register (IX) and memory as each instruction runs
- Work through one instruction at a time and update only the register or memory location that the instruction changes
- Examiners report three common errors:

  - **Indexed addressing** is often misunderstood; for example, `LDX 110` was wrongly treated as loading the value 110 into the accumulator
  - Storing a value from the accumulator **copies** it; the accumulator is **not** reset to zero
  - Output values are written without quotation marks; otherwise correct trace tables lost marks for putting the output in quotation marks

### How do you answer SQL questions?

- Typical stems include "Write a Structured Query Language (SQL) script to..." and "Write a Data Definition Language (DDL) script to..."
- Copy table and attribute names exactly as the question gives them; examiners report marks lost when these were copied wrongly
- If a question asks you to identify and correct errors in an SQL script, write the corrected statement as well as naming the error; examiners report answers that found the errors but gave no correction
- Use SQL data types such as `VARCHAR(n)`, `INTEGER` and `DATE`, not data types from a programming language
- Put quotation marks around text values but not around Boolean or numeric values, and use the SQL functions in the syllabus, such as `AVG`, `SUM` and `COUNT`; examiners report marks lost for quotation marks around a Boolean value in a `WHERE` clause
- Examiners report that the primary and foreign key clauses are often the hardest part, so learn `PRIMARY KEY (Field)` and `FOREIGN KEY (Field) REFERENCES Table (Field)`

## Common mistakes in Paper 1

> **Spec point** — `spcpt_yZvfddG8jCC6NRcz`

## Common mistakes in Paper 1

- Answering in denary when the question asks for hexadecimal, or the other way round
- Leaving out the "divide by 8" step in file size calculations
- Not stating whether a value goes up or down when describing the effect of a change
- Replacing a combination of gates with a single NOR gate, which changes the expression
- Writing the same point twice in different words for a 2-mark question

> **Worked Example**
> A bitmap image has a resolution of 1024 pixels wide and 512 pixels high. The bit depth is 24 bits.
> 
> Calculate the file size of the image. Give your answer in kibibytes. Show your working.
> 
> **[2]**
> 
> **Answer**:
> 
> Working: (1024 × 512 × 24) / 8 / 1024 **[1 mark]**
> 
> Answer: 1536 KiB **[1 mark]**
> 
> Dividing by 8 converts bits to bytes and dividing by 1024 converts bytes to kibibytes; dividing by 1024 first gives 512 × 24 / 8 = 512 × 3 = 1536, which is easy to work out without a calculator.

> **Exam Hint**
> - Before answering a conversion or file size question, underline the unit or number base the answer must be in, because a correct value in the wrong form loses the mark
> - When a question says "using binary subtraction" or "show your working", the working itself carries marks, so set it out in full even if you can do it in your head
