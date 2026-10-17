---
note_id: "rn_GFFgBfqbR5vNVq9s"
title: "Order of Operations"
source: https://www.savemyexams.com/igcse/ict/cie/21/revision-notes/11-spreadsheets/create-a-data-model/order-of-operations
path: 11-spreadsheets/create-a-data-model/order-of-operations
updated_at: "2024-05-16T10:51:19.611Z"
spec_point_ids: ["spcpt_vKqXK69gKxjF3BgZ"]
spec_point_codes: []
guided_study: false
---

# Order of Operations

## Order of Operations

> **Spec point** — `spcpt_vKqXK69gKxjF3BgZ`

## Order of Operations

### What is the order of operations?

- The order of operations is what** determines the sequence** in which **calculations are performed** within a formula
- The order of operations** ensures** the calculation is** completed correctly**
- A spreadsheet performs all calculations using a** mathematical order of operations** known as **BIDMAS**

| B | **B**rackets first |
|---|---|
| I | **I**ndices (power of and square root etc.) |
| DM | **D**ivision and **M**ultiplication (left to right) |
| AS | **A**ddition and **S**ubtraction (left to right) |

> **Case Study**
> Consider the following example spreadsheet:
> 
> |   | **A** | **B** | **C** |
> |---|---|---|---|
> | **1** | 10 | 20 |   |
> | **2** | 5 | 15 |   |
> | **3** |   | =20*2 |   |
> 
> - If you input the formula "**=A1+B3***" in cell C1, the result will be 50, because B3* is calculated first (20*2=40), and then A1 is added (10+40=50)
> - If you input the formula "**=(A1+B1)******2****" in cell C2, the result will be 60, because A1+B1 is calculated first (10+20=30), and then the result is multiplied by 2 (30**2=60)

> **Exam Hint**
> It's always a good idea to use brackets to make sure that your formulae work as expected, even if they might not be necessary
> 
> - It makes the formula easier to read and understand
> - It can prevent errors if the formula is edited in the future
