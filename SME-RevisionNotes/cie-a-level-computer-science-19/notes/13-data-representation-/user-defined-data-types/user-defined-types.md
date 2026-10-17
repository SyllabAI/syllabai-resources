---
note_id: "rn_C9tHVM7pB7hZRM5H"
title: "User-Defined Types"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/13-data-representation-/user-defined-data-types/user-defined-types
path: 13-data-representation-/user-defined-data-types/user-defined-types
updated_at: "2026-10-01T12:38:11.163Z"
spec_point_ids: ["spcpt_fmFd4vgJtVWcghDF", "spcpt_WsRKgbbSqqhzvS93"]
spec_point_codes: []
guided_study: false
---

# User-Defined Types

## What are user-defined data types?

- A user-defined data type is a **custom data type** created by the programmer, built from existing types to match the specific needs of a program
- It is built using [primitive data types](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/10-data-types-and-structures-/data-types-and-records/data-types/) such as `INTEGER`, `STRING`, `BOOLEAN`, etc

#### Why are user-defined types necessary?

- Primitive types alone cannot model many **real-world entities** (e.g. a customer, a date, a linked list)
- User-defined types let you:

  - Group **related data** under a single identifier (record)
  - Restrict a variable to a **fixed set of valid values** (enumerated)
  - Build **dynamic data structures** such as linked lists (pointer)
  - Make code more **readable**, **reusable** and **easier to validate**

| **Category** | **Definition** | **Examples** |
|---|---|---|
| **Non-composite** | A type defined **without referencing another data type** | Enumerated, pointer |
| **Composite** | A type that references **other data types** in its definition, grouped under a single identifier | Record, set, class |

## Non-composite

> **Spec point** — `spcpt_fmFd4vgJtVWcghDF`

## Non-composite

- A non-composite data type is **defined without referencing any other data type**
- It can be a **primitive type** available in the language, or a **user-defined type** (enumerated or pointer)

### What is an enumerated data type?

- An enumerated data type is a **non-composite, user-defined type** consisting of a list of **all possible values** the variable can take
- The values are **ordered**: they have an implied sequence based on the order they are declared, so comparisons work (e.g. `Monday` comes before `Tuesday`)
- Use an enumerated type to **restrict a variable to a known, fixed list**, improving readability and reducing invalid values

| Pseudocode |
|---|
| `TYPE <identifier> = (value1, value2, value3, … )` |

**Example code**

- `Today` can only hold one of the seven **ordered** values in `DayType`

### What is a pointer data type?

- A pointer is a non-composite, user-defined type that **stores a memory address only**, rather than the data itself
- Its definition also **indicates the type of data** stored at that memory location
- Pointers are used to build **dynamic data structures** such as linked lists

| Pseudocode |
|---|
| `TYPE <identifier> = ^<data type>` |

- The `^` shows the type is a pointer
- `<data type>` is the type of data stored at the address

**Example code**

## Composite

> **Spec point** — `spcpt_WsRKgbbSqqhzvS93`

## Composite

- A composite data type is a **collection of data made up of multiple elements**, of the **same or different data types**, **grouped under a single identifier**
- It **references other data types** in its definition (primitive or other user-defined types)
- The three composite user-defined types you need are **record**, **set** and **class**

### What is a record?

- A record is a **composite type** that groups together a **fixed number of related items (fields)**, which may be of **different data types**, to form a single new type
- Access a field using **dot notation**: `RecordName.FieldName`

| Pseudocode |
|---|
|   |

**Example code**

### What is a set?

- A set is a **composite type** holding a list of **unordered elements**
- **All elements must be of the same data type**, and the set definition **includes the data type it uses**
- **Set theory operations** such as **union** and **intersection** can be applied to the elements

| Pseudocode |
|---|
|   |

**Example code**

### What is a class?

- A class is a **composite type** that groups together both **data (attributes)** and the **methods** that operate on that data, under a single identifier
- It is used as a **template** to create objects in object-oriented programming
- Full detail on defining and using classes is covered in [Object-Oriented Programming](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/20-further-programming-/object-oriented-programming/classes-oop/)

### Choosing a user-defined data type

- Exam questions may ask you to **choose and design** an appropriate type for a problem
- Match the type to what the data looks like:

| **If the data...** | **Use a...** |
|---|---|
| can only be one of a fixed, named list of values | Enumerated type |
| needs to link to another item / build a dynamic structure | Pointer |
| groups several related fields of different types | Record |
| is an unordered collection with no duplicates | Set |
| combines data with the operations that act on it | Class |

> **Exam Hint**
> - Composite vs non-composite" is about **whether the type references other types**, not whether it holds one value or many. State this precisely
> - For enumerated types, remember to say the values are **ordered**, that is a mark point
> - For a "describe the set/record data type" question, include that it is **composite**, that it **references/uses other data types**, and the specific detail (set = unordered, same type, supports union/intersection; record = fixed number of related items)
