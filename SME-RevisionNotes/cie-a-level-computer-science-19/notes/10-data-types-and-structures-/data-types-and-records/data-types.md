---
note_id: "rn_9wJrGNS9nfcYKf7N"
title: "Data Types"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/10-data-types-and-structures-/data-types-and-records/data-types
path: 10-data-types-and-structures-/data-types-and-records/data-types
updated_at: "2025-04-30T09:11:22.925Z"
spec_point_ids: ["spcpt_6n4XbSGGc38X55SY"]
spec_point_codes: []
guided_study: false
---

# Data Types

## Primitive data types

> **Spec point** — `spcpt_6n4XbSGGc38X55SY`

## Primitive data types

### What are data types?

- A data type is a classification of data into groups according to the **kind of data they represent**
- Computers use different data types to represent different types of data in a program
- The basic data types include:

  - **Integer**: used to represent **whole numbers**, either positive or negative
  
    - Examples: 10, -5, 0
  - **Real**: used to represent **numbers with a fractional part**, either positive or negative
  
    - Examples: 3.14, -2.5, 0.0
  - **Char**: used to represent a **single character** such as a letter, digit or symbol
  
    - Examples: 'a', 'B', '5', '\$'
  - **String**: used to represent a **sequence of alphanumerical characters**
  
    - Examples: "Hello World", "1234", "@#\$%"
  - **Boolean**: used to represent **true or false** values
  
    - Examples: True, False
  - **Date**: used to store a **calendar date**
  
    - Example: DD/MM/YY
- It is important to choose the **correct data type for a given situation** to ensure accuracy and efficiency in the program
- In pseudocode and some other programming languages, **data types must be declared** before they can be used

  - The data types are declared with each **data item** to be used
  - Each data item is given a **unique **name called an **identifier**
  - `DECLARE <identifier> : <data type>`

| **Data Type** | **Example Value** | **Pseudocode** | **Python** | **Java** | **VB.NET** |
|---|---|---|---|---|---|
| **Integer** | `10` | `DECLARE Age : INTEGER`<br>`Age ← 10` | `age = 10` | `int age = 10;` | `Dim age As Integer = 10` |
| **Real** | `3.14` | `DECLARE Temp : REAL`<br>`Temp ← 3.14` | `temp = 3.14` | `double temp = 3.14;` | `Dim temp As Double = 3.14` |
| **Char** | `'A'` | `DECLARE Grade : CHAR`<br>`Grade ← 'A'` | `grade = 'A'` | `char grade = 'A';` | `Dim grade As Char = "A"c` |
| **String** | `"Hello"` | `DECLARE Name : STRING`<br>`Name ← "Hello"` | `name = "Hello"` | `String name = "Hello";` | `Dim name As String = "Hello"` |
| **Boolean** | `TRUE` | `DECLARE LoggedIn : BOOLEAN`<br>`LoggedIn ← TRUE` | `logged_in = True` | `boolean loggedIn = true;` | `Dim loggedIn As Boolean = True` |
| **Date** | `24/04/2025` | `DECLARE DOB : DATE`<br>`DOB ← "24/04/2025"` | `dob = "24/04/2025"` (string or `datetime`) | `LocalDate dob = LocalDate.of(2025, 4, 24);` | `Dim dob As Date = #24/04/2025#` |
