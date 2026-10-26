---
note_id: "rn_wkH9KTSjMky8k97k"
title: "Pseudocode basics"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/11-programming-/programming-basics/pseudocode-basics
path: 11-programming-/programming-basics/pseudocode-basics
updated_at: "2026-10-01T11:29:26.217Z"
spec_point_ids: ["spcpt_wPhvFYpKRJJwwdPN", "spcpt_nxXYPdhQmhNPS4bX"]
spec_point_codes: []
guided_study: false
---

# Pseudocode basics

## Variables & Constants

> **Spec point** — `spcpt_wPhvFYpKRJJwwdPN`

## Variables & Constants

### What is a variable?

- A variable is an **identifier **that **can change** in the lifetime of a program
- Identifiers should be:

  - In **mixed case** (Pascal case)
  - Can only **contain letters** (A-Z, a-z), **digits** (0-9) and the **underscore** character (_)
  - **Start with a capital** letter and not a digit
- A variable can be** associated a datatype** when it is declared
- When a variable is declared, **memory is allocated** based on the data type indicated

| **Pseudocode** |
|---|
| `DECLARE <identifier> : <datatype>` |

- To declare a variable, use the `DECLARE` keyword followed by the **name** and **data type**:

- You can then **assign a value** using the assignment operator  `← `:

### What is a constant?

- A constant is an **identifier set once in the lifetime of a program**
- Constants are generally named in **all uppercase characters**
- Constants **aid **the **readability **and **maintainability**

| **Pseudocode** |
|---|
| `CONSTANT <identifier> = <value>` |

- To declare a constant, use the `CONSTANT` keyword:

- Constants are **not reassigned** during execution – they are fixed values used throughout the algorithm

#### Example

- You are writing a program to calculate the area of a circle using the formula:

`Area ← π × radius²`

- `π` is a **constant** (it never changes)
- `radius` and `area` are **variables** (they change depending on the input)

### Variables and constants in different languages

| **Feature** | **Python** | **VB.NET** | **Java** |
|---|---|---|---|
| **Declare variable** | Just assign it (no keyword needed) | `Dim radius As Double` | `double radius;` |
| **Assign variable** | `radius = 5` | `radius = 5` | `radius = 5;` |
| **Declare constant** | Convention: use UPPERCASE (`PI = 3.14`) (not enforced) | `Const Pi As Double = 3.14159` | `final double PI = 3.14159;` |
| **Reassign constant?** | Yes (not truly constant unless enforced) | Cannot change once set | Cannot change once set |
| **Use in calc.** | `area = PI * radius * radius` | `area = Pi * radius * radius` | `area = PI * radius * radius;` |

## Arithmetic & logical operators

> **Spec point** — `spcpt_nxXYPdhQmhNPS4bX`

## Arithmetic & logical operators

### Arithmetic operators

- Arithmetic operators are used to perform basic **maths operations** in a program
- These include adding, subtracting, multiplying and dividing values

#### Common arithmetic operators

| **Operator** | **Purpose** | **Example** | **Result** |
|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` |
| `&` | Concatenation | `"John" & " " & "Doe"` | `"John Doe"` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `3 * 5` | `15` |
| `/` | Division | `10 / 2` | `5` |
| `^` | Exponentiation (power of) | `3 ^ 3` | `27` |
| `MOD` | Modulus (remainder after division) | `10 MOD 3` | `1` |

### Operator precedence (BODMAS / BIDMAS)

- Arithmetic operators follow **operator precedence**
- Multiplication and division happen before addition and subtraction unless brackets are used

### Relational and logic operators

- **Relational operators** (also called comparison operators) are used to **compare two values**
- They return either **TRUE** or **FALSE** and are commonly used in conditions and loops
- The **logic operators** are `AND`, `OR` and `NOT`; they combine or reverse BOOLEAN values, e.g. `X < Y AND Y < 20`

#### Common relational operators

| **Operator** | **Purpose** | **Example** | **Result** |
|---|---|---|---|
| `=` | Equal to | `5 = 6` | `FALSE` |
| `<>` | Not equal to | `5 <> 7` | `TRUE` |
| `>` | Greater than | `5 > 10` | `FALSE` |
| `<` | Less than | `5 < 10` | `TRUE` |
| `>=` | Greater than or equal to | `5 >= 10` | `FALSE` |
| `<=` | Less than or equal to | `5 <= 10` | `TRUE` |

#### Example code
