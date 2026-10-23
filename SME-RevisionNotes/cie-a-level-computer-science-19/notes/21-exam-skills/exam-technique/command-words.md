---
note_id: "rn_4GhpD4WYxvh3MPBH"
title: "Command Words"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/exam-technique/command-words
path: 21-exam-skills/exam-technique/command-words
updated_at: "2026-10-16T11:56:24.870Z"
spec_point_ids: ["spcpt_P8ZkMTYGZNwrr89s", "spcpt_skpFHrV6YM89k2zm", "spcpt_9SMprrnbWcd2cXt6", "spcpt_VGydhKWGg8YRDnJk", "spcpt_r3K8KtF5rRrm8sPd"]
spec_point_codes: []
guided_study: false
---

# Command Words

## What are command words?

> **Spec point** — `spcpt_P8ZkMTYGZNwrr89s`

## What are command words?

### Why do command words matter in 9618?

- A **command word** is the instruction at the start of an exam question, such as **State**, **Describe** or **Explain**
- It tells you **what kind of answer** the examiner wants and **how much detail** to give
- Cambridge examiner reports for 9618 regularly advise students to learn the meanings of the command words and to "form their answers accordingly"
- A correct fact written in the wrong form can still lose marks; for example, a one-word answer to an **Explain** question will rarely score

## The most common command words in 9618

> **Spec point** — `spcpt_skpFHrV6YM89k2zm`

## The most common command words in 9618

- The 9618 syllabus lists 27 command words, but a small number make up most of the questions
- In recent papers, the most frequent are **Write**, **Describe**, **Complete**, **Explain**, **State** and **Identify**

  - Paper 1 uses **Describe** and **Explain** the most
  - Papers 2 and 3 use **Write** the most: in Paper 2 it usually asks for pseudocode, and in Paper 3 it also asks for Boolean expressions, Reverse Polish Notation (RPN), *declarative clauses* and floating-point values

| Command word | What it means (Cambridge definition) | What to do in 9618 | Real 9618 example |
|---|---|---|---|
| **State** | Express in clear terms | Give a short, precise answer; no explanation needed | State the purpose of the system clock and the Control Unit (CU) in a CPU |
| **Identify** | Name, select or recognise | Name the item; one word or a short phrase is often enough | Identify two differences between general purpose registers and special purpose registers |
| **Give** | Produce an answer from a given source or from memory | Give the number of points asked for, each one separate | Give two benefits of distributing software using a shareware software licence |
| **Define** | Give precise meaning | Give the exact meaning of the term, using technical vocabulary | Define cloud computing |
| **Outline** | Set out the main points | Give the main points briefly, without full detail | Outline two benefits and two limitations of a virtual machine |
| **Describe** | State the points of a topic, or give characteristics and main features | Say what something is or what happens, step by step; each step is usually a mark | Describe how the laser printer makes use of a buffer |
| **Explain** | Set out purposes or reasons, make the relationships between things clear, or say why and/or how and support with relevant evidence | Give a point **and** the reason for it, linked with "because" or "so that" | Explain what is meant by disk thrashing |
| **Write** | Write an answer in a specific way | Produce the answer in the form asked for: pseudocode, Structured Query Language (SQL), a Boolean expression | Write the Boolean expression that corresponds to the logic circuit as a *sum-of-products* |
| **Complete** | Add information to an incomplete diagram or table | Fill in every empty cell or part; do not change what is already given | Complete the trace table by dry running the procedure |
| **Calculate** | Work out from given facts, figures or information | Show each step of the working; no calculator is allowed | Calculate the normalised floating-point representation of +54.8125 in this system |

## Command words that students confuse

> **Spec point** — `spcpt_9SMprrnbWcd2cXt6`

## Command words that students confuse

### State, Describe or Explain?

- These three words ask about the same topic at three different depths

  - **State** asks *what*: one clear fact
  - **Describe** asks *what happens*: the features or the steps, in order
  - **Explain** asks *why* or *how*: each point needs a reason
- Examiners point out that an **Explain** question needs more detail than an **Identify** question
- If an **Explain** question is worth 2 marks, aim for one point and its reason, or two linked points

### Identify or Outline?

- **Identify** only needs the name of the thing; extra detail will not gain more marks
- **Outline** needs the main points of each item, briefly

  - "Outline two methods of overcoming this issue" needs a short description of how each one works
  - If the same question used Identify instead, the names of two methods would be enough

### Evaluate means "work out the value"

- In most subjects, **Evaluate** means making a judgement
- In 9618 papers, **Evaluate** is used to ask for the **value** of an expression, matching the second half of the Cambridge definition: "judge or calculate the quality, importance, amount, or value of something"

  - "Evaluate this RPN expression" means work out the numeric result
  - "Evaluate each expression in the table by using the data values shown" means work out what each expression returns (for example, `TRUE`, `FALSE` or a number)
- Write the final value clearly and, where asked, show the stack contents or working that produced it

### Compare and contrast

- **Compare** asks for similarities **and/or** differences; **Contrast** asks for differences only
- Every point must mention **both** items

  - "A linear search checks every item in turn, whereas a binary search halves the search area each time" scores
  - "A binary search halves the search area each time" on its own does not, because it says nothing about a linear search

### Draw in 9618

- The syllabus defines **Draw** as "draw a line to match a term with a description", and 9618 papers do use it this way
- 9618 papers also use **Draw** for diagrams, such as:

  - logic circuits
  - structure charts
  - syntax diagrams
  - loops around groups in a Karnaugh map
- Use a ruler, follow the symbol conventions used in the question and label everything the question asks for

> **Worked Example**
> A student sends a long document from a laptop to a printer.
> 
> (a) State what is meant by a buffer.
> 
> **[1]**
> 
> (b) Describe how a buffer is used when the document is printed.
> 
> **[3]**
> 
> (c) Explain why a buffer is needed when the document is printed.
> 
> **[2]**
> 
> **Answer**:
> 
> (a) A temporary area of memory that holds data while it is being transferred between devices **[1 mark]**
> 
> (b) Any three from:
> 
> - The laptop sends data for the document to the buffer **[1 mark]**
> - The printer takes data from the buffer at its own speed **[1 mark]**
> - When the buffer is empty, an interrupt is sent to the laptop **[1 mark]**
> - ... requesting more data to be sent **[1 mark]**
> 
> (c) The laptop sends data much faster than the printer can print it **[1 mark]**
> 
> - ... so the buffer holds the data and the processor can carry on with other tasks instead of waiting for the printer **[1 mark]**
> 
> Part (a) needs one fact, part (b) needs the steps in order, and part (c) needs a reason, so the same topic is worth 1, 3 or 2 marks depending on the command word.

> **Exam Hint**
> - Before you answer, circle the command word and check the marks: an Explain question worth 2 marks needs a point and a reason, not two separate facts
> - If a question uses Evaluate with an expression, it wants a value, so do not write a paragraph judging the expression

## Command words in programming and working-out questions

> **Spec point** — `spcpt_VGydhKWGg8YRDnJk`

## Command words in programming and working-out questions

### Write

- **Write** is the most common command word in Papers 2 and 3
- In 9618 it usually asks for an answer in a specific form:

  - "Write pseudocode for the function..."
  - "Write a Structured Query Language (SQL) script to..."
  - "Write the Boolean expression that corresponds to..."
- When **Write** asks for pseudocode, it must follow the Cambridge pseudocode conventions; marks are lost for using programming language syntax instead
- See [Writing Pseudocode in the Exam](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/21-exam-skills/key-exam-skills/writing-pseudocode-in-the-exam/) for the conventions examiners check

### Complete

- **Complete** asks you to fill in something that is partly given, such as a trace table, a truth table, an assembly language trace or a Backus-Naur Form (BNF) definition
- Use the format already in the table; for example, if a column shows values in binary, do not switch to denary
- In a trace table, write a value only when it changes; in a truth table, fill in every cell

### Show

- **Show** is not in the syllabus list, but it appears often in Papers 1 and 3

  - "Show your working" means the method earns marks, not just the answer
  - "Show the changing contents of the stack" means write out every state, not only the final one
  - "Show the result of a 2-place left logical shift" means write the resulting binary number in full

## Other command words in the 9618 syllabus

> **Spec point** — `spcpt_r3K8KtF5rRrm8sPd`

## Other command words in the 9618 syllabus

- These words are in the syllabus list but appear rarely in 9618 papers

| Command word | What it means |
|---|---|
| Analyse | Examine in detail to show meaning, identify elements and the relationship between them |
| Assess | Make an informed judgement |
| Comment | Give an informed opinion |
| Consider | Review and respond to given information |
| Demonstrate | Show how or give an example |
| Develop | Take forward to a more advanced stage or build upon given information |
| Discuss | Write about issue(s) or topic(s) in depth in a structured way |
| Examine | Investigate closely, in detail |
| Predict | Suggest what may happen based on available information |
| Sketch | Make a simple freehand drawing showing the key features, taking care over proportions |
| Suggest | Apply knowledge and understanding to situations where there is a range of valid responses, in order to make proposals or put forward considerations |
| Summarise | Select and present the main points, without detail |

- **Justify** is the exception: it is common in 9618, usually as "Justify your choice" or "justify your answer"; give a reason linked to the scenario, saying why your choice suits it better than the alternative, not just how each works
