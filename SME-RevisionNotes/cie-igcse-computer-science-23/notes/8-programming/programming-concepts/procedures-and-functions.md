---
note_id: "rn_kqRBGvjZfcfxbn7b"
title: "Procedures & Functions"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/8-programming/programming-concepts/procedures-and-functions
path: 8-programming/programming-concepts/procedures-and-functions
updated_at: "2025-05-07T14:00:49.935Z"
spec_point_ids: ["spcpt_q8mspQC3BH7dbMCc", "spcpt_XzGmRvsfmkYJB6MF"]
spec_point_codes: []
guided_study: true
---

# Procedures & Functions

## What are functions and procedures?

> **Exam Hint**
> *IGCSE 0478 Paper 2 assesses your ability to define, use, and explain ****functions****, ****procedures****, and ****parameters**** using both ****pseudocode and Python****. This page shows only examinable structures, phrasing, and examples—no fluff.*

- Functions and procedures** **are a type of **sub program**, a **sequence of instructions** that** perform a specific task** or **set of tasks**
- Procedures and functions are **defined at the start of the code**
- Sub programs are often used to **simplify **a program by** breaking it into smaller, more manageable parts**
- Sub programs can be used to:

  - **Avoid duplicating code** and can be reused throughout a program
  - **Improve **the **readability **and **maintainability** of code
  - Perform **calculations**, to **retrieve data**, or to **make decisions** based on input
- **Parameters **are **values** that are **passed into a sub program**

  - Parameters can be variables or values and they are located **in brackets** after the name of the sub program
  - Example: `FUNCTION TaxCalculator(pay,taxcode)` **OR  **`PROCEDURE TaxCalculator(pay,taxcode)`
- Sub programs **can have multiple parameters**
- To use a sub program you '**call**' it from the main program

### What's the difference between a function and procedure?

- A **Function returns a value** whereas a procedure does not

## Procedures

> **Spec point** — `spcpt_q8mspQC3BH7dbMCc` · "6 (a) Understand what is meant by procedures,
functions and parameters
(b) Define and use procedures and functions,
with or without parameters"

## Procedures

- Procedures are defined using the **PROCEDURE **keyword in pseudocode or **def **keyword in Python
- A procedure can be written as: **PROCEDURE <identifier>**
**    <statements>**
**ENDPROCEDURE**
- Or if parameters are being used:

**PROCEDURE <identifier>(<param1>:<data type>, <param2>:<data type>...)**
**    <statements>**
**ENDPROCEDURE**

| **Creating a procedure** |
|---|
| **Pseudocode** |
|   |
| **Python** |
|   |

- To call a procedure, it can be written as: **CALL <identifier>**
**CALL <identifier>(Value1,Value2...)**

| **Calling a procedure** |
|---|
| **Pseudocode** |
|   |
| **Python** |
|   |

#### Examples

- A Python program using procedures to **display a menu** and **navigate **between them
- **Procedures **are **defined at the start of the program** and the main program calls the first procedure to start
- In this example, no parameters are needed

| Procedures |
|---|
|   |

## Functions

> **Spec point** — `spcpt_XzGmRvsfmkYJB6MF` · "6 (a) Understand what is meant by procedures,
functions and parameters
(b) Define and use procedures and functions,
with or without parameters"

## Functions

- Functions are defined using the **FUNCTION **keyword in pseudocode or **def **keyword in Python
- Functions **always return a value** so they do not use the CALL function, instead they are called **within an expression**
- A function can be written as: **FUNCTION <identifier> RETURNS <data type>**
**    <statements>**
**ENDFUNCTION**
- Or if parameters are being used:

**FUNCTION <identifier>(<param1>:<data type>, <param2>:<data type>...) RETURNS <data type>**
**    <statements>**
**ENDFUNCTION**

> **Exam Hint**
> *In pseudocode, never write *`CALL calculate_area()`* for a function.*
> *Functions are ****called in expressions**** like:*
> `OUTPUT calculate_area(5,3)`
> *Use *`CALL`* only with ****procedures**** that do not return a value.*

| **Creating and using a function** |
|---|
| **Pseudocode** |
|   |
| **Python** |
|   |

#### Examples

- A Python program using a **function to calculate area** and return the result
- Two options for main program are shown, one which **outputs the result** (# 1) and one which **stores the result** so that it can be used at a later time (# 2)

| Functions |
|---|
|   |

> **Worked Example**
> An economy-class airline ticket costs £199. A first-class airline ticket costs £595.
> 
> (**A**) Create a function,` flightCost(),` that takes the number of passengers and the type of ticket as parameters, calculates and returns the price to pay.
> 
> You do **not **have to validate these parameters
> 
> You must use :
> 
> - a high-level programming language that you have studied **[4]**
> 
> (**B**) Write program code, that uses `flightCost()`, to output the price of 3 passengers flying economy.
> 
> You must use :
> 
> - a high-level programming language that you have studied **[3]**
> 
> **How do I answer this question?**
> 
> (**A**)
> 
> - Define the function, what parameters are needed? where do they go?
> - How do you calculate the price?
> - Return the result
> 
> (**B**)
> 
> - How do you call a function?
> - What parameters does the function need to return the result?
> 
> **Answers**
> 
> | **Part** | **Python** |
> |---|---|
> | **A** |   |
> | **B** | `print(flightCost("economy", 3)`<br><br>**OR**<br><br>`x = flightCost("economy", 3)`<br><br>`print(x)` |

> **Exam Hint**
> *in pseudocode, you can get marks just for using the correct structure:*
> 
> - *Starts with *`FUNCTION`* or *`PROCEDURE`* ***[1 mark]**
> - *Correct use of parameters and *`RETURN`* (functions) or *`OUTPUT`* (procedures) ***[1 mark]**
> - *Called correctly from main program ***[1 mark]**
