---
note_id: "rn_7RDMpysNd4k7B8Bb"
title: "Formulae & Functions"
source: https://www.savemyexams.com/igcse/ict/edexcel/17/revision-notes/5-software-skills/spreadsheet/formulae-and-functions
path: 5-software-skills/spreadsheet/formulae-and-functions
updated_at: "2024-06-27T11:09:15.617Z"
spec_point_ids: ["spcpt_mXDvNxwqJhTR78p4", "spcpt_qkmwy23c23Vpvqkb"]
spec_point_codes: []
guided_study: false
---

# Formulae & Functions

## Formulae

> **Spec point** — `spcpt_mXDvNxwqJhTR78p4`

## Formulae

### What is a formula?

- A formula is **a statement that performs simple calculations** in a spreadsheet
- Formulas **start with a = sign**
- A formula can perform calculations using:

  - **Numbers directly (e.g. =5*2)**
  - **Referenced data held in cells (e.g. =A1*B2)**
- **Changing data** in a cell that is being referenced in a formula will cause the formula to automatically recalculate based on the new value
- This is a **core concept **of spreadsheet modelling

![Spreadsheet showing the 2023 pass rate percentage in column G, with values ranging from 72% to 82%. Column H is labeled 'Total' and is empty.](../../../assets/18f0c538b7db-42331-formulaandreplicatev2-ezgif-com-video-to-w.webp)

*Adding simple formulas to a spreadsheet*

#### Arithmetic operators

- Formulas will make use of basis arithmetic operators

| Symbol | Operation |
|---|---|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| ^ | Indices (power of) |

## Functions

> **Spec point** — `spcpt_qkmwy23c23Vpvqkb`

## Functions

### What is a function?

- A function is a** pre-defined formula** that can be used to** carry out more complex calculations**
- Functions are **built into spreadsheet software**
- Functions can **help to simplify **complex calculations
- Each function **has a specific name** that tells the software what calculation is being carried out

![Spreadsheet showing scores of subjects: Geography, French, Spanish, and Computer Science. Listed columns: subject, three different scores, a total, and average row.](../../../assets/343d3ef34338-38538-functionsandreplicatev2-ezgif-com-video-to.webp)

*Adding functions to a spreadsheet*

| Function | Operation |
|---|---|
| **SUM** | Adds all the numbers in a range of cells<br><br>**=SUM(A1:A10)** |
| **AVERAGE** | Calculates the average of a range of cells<br><br>**=AVERAGE(A1:A10)** |
| **MAX and MIN** | Finds the largest and smallest numbers in a range respectively<br><br>**=MAX(A1:A10)**<br><br>**=MIN(A1:A10)** |
| **INT** | Rounds a number down to the nearest integer<br><br>**=INT(A1)** |
| **ROUND** | Rounds a number to a specified number of digits<br><br>**=ROUND(A1,2) **- round to 2 decimal places |
| **COUNT** | Counts the number of cells in a range that contain numbers<br><br>**=COUNT(A1:A10)** |
| **COUNTA** | Counts the number of cells in a range that contain numbers and/or labels<br><br>**=COUNTA(A1:A10)** |
| **IF** | Returns one value if a condition is true and another if it's false<br><br>**=IF(condition, true, false)**<br><br>**=IF(A1 ="SME",100,B7*3)** |
| **HLOOKUP** | Performs a horizontal look up of data<br><br>**=HLOOKUP('Bananas', A2:D4, 3)** |
| **VLOOKUP** | Performs a vertical look up of data<br><br>**=VLOOKUP(100, A2:D4, 2, TRUE)** |
| **XLOOKUP** | Performs either a horizontal or vertical look up of data<br><br>**=XLOOKUP('Oranges', A1:A4, Sales Q3, "Not found")** |

![Spreadsheet with rows labeled Spanish (210), Computer Science (180), Totals (3920), Average (326.67). Highlighted cell at row 16.](../../../assets/85429b3df419-61592-maxminintegerv2-ezgif-com-video-to-webp-co.webp)

*Average, Max, Min & Int in a spreadsheet*

#### Using external data sources within functions

- Spreadsheets allow you to use **external data sources** within functions
- This could be data from another **worksheet**, **workbook**, or even a **database**

#### Using nested functions

- Nesting is using **a function within another function**
- For example:

  - =IF(A1>B1, MAX(A1:B1), MIN(A1:B1))
  
    - This checks if A1 is greater than B1, and if true, it returns the max value, else it returns the min value

> **Worked Example**
> awara school has a shop that sells items needed by pupils in school. Part of a spreadsheet with details of the items is shown.
> 
> ![spreadsheet example](assets/1044b69d826e-screenshot-2023-05-24-at-10-51-11.png)
> 
> Tax is paid on certain items sold in the shop. The tax rate that has to be paid is 20% of the selling price. If tax is to be paid on an item, then ‘Y’ is placed underneath the Tax heading.
> 
> The formula in I4 is: IF(F4=''Y'',(\$I\$1*D4*G4),'''')
> 
> Explain, in detail, what the formula does.
> 
> **[5]**
> 
> **Answer**
> 
> Five of:
> 
> **Final answer:** **If Tax is payable then//If F4 is equal to "Y" then [1]**
> **If true the tax is paid [1]**
> **Multiply the rate of tax/I1 [1]**
> **By the selling price/D4 [1]**
> **By the amount sold/G4 [1]**
> **If Tax is not payable//If F4 <>"Y"//Else//Otherwise [1]**
> **Then display a blank [1]**
> **The tax is not paid [1]**
