---
note_id: "rn_wbJRYPzKXpr4Jsqf"
title: "Imperative Programming"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/20-further-programming-/programming-paradigms/imperative-programming
path: 20-further-programming-/programming-paradigms/imperative-programming
updated_at: "2025-05-20T14:31:24.267Z"
spec_point_ids: ["spcpt_Q68DDSHt6vwXm5TT"]
spec_point_codes: []
guided_study: false
---

# Imperative Programming

## Imperative programming (Procedural)

> **Spec point** — `spcpt_Q68DDSHt6vwXm5TT`

## Imperative programming (Procedural)

### How do I write imperative (procedural) code?

- High-level languages such as **Python, Java, and Visual Basic** support the imperative style
- Imperative code can be made **more organised and readable** by using **structured programming principles**, such as dividing code into **functions and procedures**

  - Before continuing, ensure you’re confident with the [basics of programming](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/11-programming-/programming-basics/pseudocode-basics/) logic and have a good understanding of [structured programming](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/11-programming-/structured-programming/procedures-and-functions/)

### Imperative programming – pseudocode (no procedures or functions)

- **Task**: Convert a temperature to:

  - Fahrenheit from Celsius
  - Celsius from Fahrenheit
  - Kelvin from Celsius
- **Rules**:

  - No procedures or functions
  - Use only **global variables**
  - Use a top-down, sequential flow (basic imperative structure)

#### Imperative pseudocode

#### Walkthrough – What’s happening?

- All variables are **declared globally**
- The entire program is written as **one long block**
- There is **no reusability** (e.g. if you want to convert again, you'd have to rerun the whole thing)
- Changes to the program will likely lead to **code duplication** and harder maintenance

### Structured (procedural) programming – pseudocode

- **Goal**: Rewrite the above code using **procedures or functions**, **local variables**, and **modular logic**

#### Walkthrough – what’s improved?

- Logic is **divided into reusable blocks** (procedures)
- Each procedure has **local variables**
- The program is easier to **read**, **maintain**, and **extend**
- Only one global variable (`choice`) is used for communication
- Additional features (like repeating conversions or logging) can be added more easily

### Summary

| Feature | Imperative | Structured (Procedural) |
|---|---|---|
| Reusability | No reuse | Easy to reuse procedures |
| Modularity | All logic in one block | Code divided into named units |
| Readability | Can become unclear in longer code | Easier to understand each part |
| Variables | All global | Mix of global and local |
| Maintenance | Changes affect entire block | Easier to update specific parts |
| Ideal for real-world apps? | Not ideal | Industry standard approach |
