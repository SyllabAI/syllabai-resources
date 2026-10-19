---
note_id: "rn_3487S9YjFM5FPrvw"
title: "Perform Calculations"
source: https://www.savemyexams.com/igcse/ict/cie/21/revision-notes/10-databases/create-a-database-structure/perform-calculations
path: 10-databases/create-a-database-structure/perform-calculations
updated_at: "2024-06-27T09:52:30.235Z"
spec_point_ids: ["spcpt_QYqXy4Hkz2nn4QR9"]
spec_point_codes: []
guided_study: false
---

# Perform Calculations

## Perform calculations

> **Spec point** — `spcpt_QYqXy4Hkz2nn4QR9`

## Perform calculations

### How do you perform calculations in a database?

- In a database, you can use **arithmetic operations or numeric functions** to perform calculations
- Calculated fields are fields that carry out a calculation **based on other number fields in the database**

  - For example, a '*products*' table with a `stock `and` unit_price` fields
  - You could use a calculated field named `stockvalue` to calculate `unit_price` * `stock`
  - This calculation multiplies the price of each item by its quantity to find the total value of the stock

![Database window showing a table with products listed by name, brand, category, unit price, unit size, and stock. Navigation pane on the left includes Tables and Shortcuts.](../../../assets/863345dce31c-60550-database-calculations-ezgif-com-optiwebp.webp)

*Adding a calculated field to a database table*

- Calculated controls are **objects you place on forms or reports** to display the **result **of an expression

  - For example, a form in a sales database where you input the `QuantitySold` and `UnitPrice`
  - A calculated control could be used to display the `TotalSale`
  - `TotalSale = QuantitySold * UnitPrice`
  - This displays the total sale on the form without storing it in the database

#### Using formulae and functions to perform calculations

- Databases allow you to use **formulae **and **functions **to perform calculations at run time
- This can include basic arithmetic operations: addition, subtraction, multiplication, and division
- For example, you have a discount field and you want to subtract it from the total cost, you could use a subtraction operation like this:

  - `FinalCost = TotalCost - Discount`

#### Aggregate functions

- You can also use aggregate functions to** calculate statistical information** about a set of records
- Some examples include:

| **Sum** | Adds together all the numbers in a column | `SUM(TotalCost)` |
|---|---|---|
| **Average** | Computes the average of a set of numbers in a column | `AVERAGE(Price)` |
| **Maximum** | Finds the highest number in a column | `MAX(Price)` |
| **Minimum** | Finds the lowest number in a column | `MIN(Price)` |
| **Count** | Counts the number of rows in a column | `COUNT(ProductID)` |

- Remember that the actual syntax and function names might differ slightly depending on the specific database system being used.
