---
note_id: "rn_YzvxHg8PYBGd5BHt"
title: "Procedures & Functions"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/11-programming-/structured-programming/procedures-and-functions
path: 11-programming-/structured-programming/procedures-and-functions
updated_at: "2026-10-01T11:36:50.340Z"
spec_point_ids: ["spcpt_YqckDNpBf2DVyRcM", "spcpt_VMP6ksfMD7mZPq5Y", "spcpt_hX5K6kTVmtbwrwv8"]
spec_point_codes: []
guided_study: false
---

# Procedures & Functions

## What are functions and procedures?

- Functions and procedures** **are a type of **sub program**, a **sequence of instructions** that** perform a specific task** or **set of tasks**
- Procedures and functions are **defined at the start of the code**
- Sub programs are often used to **simplify **a program by** breaking it into smaller, more manageable parts**
- Sub programs can be used to:

  - **Avoid duplicating code** and can be reused throughout a program
  - **Improve **the **readability **and **maintainability** of code
  - Perform **calculations**, to **retrieve data**, or to **make decisions** based on input
- **Parameters **are **values** that are **passed into a sub program**

  - Parameters can be variables or values and they are located **in brackets** after the name of the sub program
  - Example: `FUNCTION TaxCalculator(Pay : REAL, TaxCode : STRING) RETURNS REAL` **OR** `PROCEDURE TaxCalculator(Pay : REAL, TaxCode : STRING)`
- Sub programs **can have multiple parameters**
- To use a sub program you '**call**' it from the main program

### What's the difference between a function and procedure?

- A **Function returns a value** whereas a procedure does not

## Procedures

> **Spec point** — `spcpt_YqckDNpBf2DVyRcM`

## Procedures

- Procedures are defined using the **PROCEDURE **keyword in pseudocode
- A procedure can be written as:

| Pseudocode |   |
|---|---|
|   |   |

- The identifier is used to **call the procedure**
- To call a procedure, it can be written as:

- When parameters are used, `value1, value2...` must be of the correct data type and in the same sequence

#### Example code

- `PROCEDURE GreetUser` defines the procedure, which takes one parameter: `Name`
- The procedure prints a personalised greeting
- The main program asks for the user’s name and then **calls** the procedure using `CALL`

## Functions

> **Spec point** — `spcpt_VMP6ksfMD7mZPq5Y`

## Functions

- Functions are defined using the **FUNCTION **keyword in pseudocode or **def **keyword in Python
- Functions **always return a value** so they **do not** use the `CALL` keyword; instead they are called **as part of an expression**, e.g. `OUTPUT CalculateArea(5, 3)`
- A function can be written as:

| Pseudocode |   |
|---|---|
|   |   |

#### Example code

- Defines a **function** called `CalculateArea`
- It takes **two parameters**: `Length` and `Width`, both of type `INTEGER`, and **returns** an `INTEGER`
- A local variable `Area` is declared and assigned the result of `Length * Width`
- The function **returns** the result to wherever it was called from (here, 15 is output)

## Parameter passing

> **Spec point** — `spcpt_hX5K6kTVmtbwrwv8`

## Parameter passing

### What is parameter passing?

- Parameter passing is the method by which **values or references** are given to procedures or functions so they can **use or modify data during execution**
- When writing **procedures**, you can control how parameters are passed using:

  - `BYVAL` – pass **a copy** of the value (default behaviour)
  - `BYREF` – pass **the actual variable**, so changes inside the procedure affect the original

| **Keyword** | **What it does** |
|---|---|
| `BYVAL` | Passes a **copy** of the value (no change to original) |
| `BYREF` | Passes a **reference** to the variable (can be modified) |

- If **no keyword** is used, it is assumed to be `BYVAL`
- **Functions** should **not use **`BYREF`** parameters** – only **procedures** should

#### Example – Swapping two values (Procedure with BYREF)

- `BYREF` is written once but applies to **both** X and Y: when several parameters are passed by the same method, the keyword does not need to be repeated
- So both original variables **are** **changed** by the procedure, which is why it swaps their values
- To pass a later parameter by value, write `BYVAL` in front of it, e.g. `PROCEDURE AddOn(BYREF Total : INTEGER, BYVAL Amount : INTEGER)`

> **Worked Example**
> A video-conferencing program supports up to six users. Speech from each user is sampled and digitised (converted from analogue to digital). Digitised values are stored in array `Sample`.
> 
> The array `Sample` consists of 6 rows by 128 columns and is of type integer. Each row contains 128 digitised sound samples from one user.
> 
> The digitised sound samples from each user are to be processed to produce a single value which will be stored in a 1D array `Result` of type integer. This process will be implemented by procedure `Mix()`.
> 
> A procedure `Mix()` will:
> 
> - calculate the average of each of the 6 sound samples in a column
> - ignore sound sample values of 10 or less
> - store the average value in the corresponding position in `Result`
> - repeat for each column in array `Sample`
> 
> The diagram uses example values to illustrate the process:
> 
> ![Table with six rows and 128 columns, each filled with numbers. A row at the bottom shows the sum of selected columns, resulting in 20, 20, 35, 40, 46, 25.](assets/6d6e0145dee9-42344-2025-06-02-0p8-kleki.png)
> 
> Write pseudocode for procedure `Mix()`.
> 
> Assume `Sample` and `Result` are global. **[6]**
> 
> **Final answer:** **Answer**
> 
> - Declaration **and **initialisation before inner loop of `Count` **and **`Total `**[1 mark]**
> - Outer Loop for 128 iterations **[1 mark]**
> - Inner loop for six iterations **[1 mark]**
> - Test for sample > 10 **in a loop ****[1 mark]**
> - and if true sum `Total` and increment `Count `**[1 mark]**
> - Calculate average value and assign to `Result` array **after inner loop and within outer loop ****[1 mark]**
> - Use of `INT()/ DIV` to convert average to integer **[1 mark]**
