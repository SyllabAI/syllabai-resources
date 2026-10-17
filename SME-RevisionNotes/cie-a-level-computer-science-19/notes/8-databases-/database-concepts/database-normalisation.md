---
note_id: "rn_TrX5TVS4KWkvKTFR"
title: "Database Normalisation"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/8-databases-/database-concepts/database-normalisation
path: 8-databases-/database-concepts/database-normalisation
updated_at: "2026-10-01T11:16:16.485Z"
spec_point_ids: ["spcpt_jw3J5d9XNpWJcJDM", "spcpt_7t9KdWBjJVFtTGQ3", "spcpt_v3by4SFDxGTZgfwP", "spcpt_YvWkT6ZkT2qFRBpN"]
spec_point_codes: []
guided_study: false
---

# Database Normalisation

## Normalised design

> **Spec point** — `spcpt_jw3J5d9XNpWJcJDM`

## Normalised design

### What is a normalised design?

- A **normalised design** is a database structure that:

  - **Organises data efficiently**
  - **Eliminates unnecessary duplication**
  - **Ensures data integrity**
  - **Supports easy updates and accurate relationships**
- You may be asked to produce a normalised design based on:

  - A **written description** of a system
  - A **table of unnormalised data**
  - A set of **existing flat tables**
- You need to be able to:

  - Identify **repeating groups** or **duplicated data**
  - Break down data into **separate related tables**
  - Assign appropriate **primary keys** and **foreign keys**
  - Show the database in **1NF, 2NF, and 3NF**
  - Clearly show **relationships** between the tables

#### Step-by-step process

| **Step** | **What to do** | **Why it matters** |
|---|---|---|
| 1 | Read the scenario or table carefully | Understand what entities (real-world things) are involved |
| 2 | Identify the fields and any repeated/duplicated values | These usually indicate the need for more than one table |
| 3 | Apply **1NF** – remove repeating groups, separate fields | Each field should hold a single value |
| 4 | Apply **2NF** – remove partial dependencies | Make sure non-key fields depend on the whole primary key |
| 5 | Apply **3NF** – remove transitive dependencies | Non-key fields should not depend on other non-key fields |
| 6 | Assign **primary keys** for each table | Every table needs a unique identifier |
| 7 | Use **foreign keys** to link related tables | Ensures relationships and referential integrity |

#### Example

- A student is enrolled on **multiple** **courses**
- Each course is taught by **a teacher**
- The table includes: `StudentName, StudentID, CourseID, CourseName, TeacherName`
- You would:

  - Identify **Entities**: Student, Course, Teacher
  - Create tables:
  
    - **Student** (`StudentID`, `StudentName`)
    - **Course** (`CourseID`, `CourseName`, `TeacherID`)
    - **Teacher** (`TeacherID`, `TeacherName`)
    - A link table: **StudentCourse** (`StudentID`, `CourseID`) – handles many-to-many

> **Exam Hint**
> - Always check for **repeating fields** or **duplicated values**
> - Watch for **composite keys** in link tables (especially many-to-many relationships)
> - Check that all fields in a table **depend only on the key, the whole key, and nothing but the key**
> - Label each stage of your work (1NF → 2NF → 3NF)

## First Normal Form (1NF)

> **Spec point** — `spcpt_7t9KdWBjJVFtTGQ3`

## First Normal Form (1NF)

### What is first normal form?

- For a ***table*** to be in first normal form it must:

  - **Contain atomic values**
  
    - Each column in a table must contain single, indivisible values
  - **Have no repeating groups**
  
    - Columns must not contain arrays or lists of values
  - **Have unique column names**
  
    - Each column must have a unique name within the table
  - **Have a unique identifier (*****primary key*****)**
  
    - Each row must have a unique identifier to distinguish it from other rows
- This customers table below has** no primary key** and the name is stored in **one field** so is not atomic
- This table is **not** in first normal form

**Table: Customers**

| name | phone | country |
|---|---|---|
| John Smith | 07373 929122 | UK |
| Iram Iravani | 07234 543422 | Iraq |
| Wu Zhang | 04563 523427 | China |
| Anne James | 09378 482894 | USA |
| Khalid Shirvani | 02343 536522 | France |

- This customers table below **has a primary key** and the name is stored in **two fields** so it is **atomic **
- This table is in **first normal form**

**Table: Customers**

| customer_id | forename | surname | phone | country |
|---|---|---|---|---|
| 1 | John | Smith | 07373 929122 | UK |
| 2 | Iram | Iravani | 07234 543422 | Iraq |
| 3 | Wu | Zhang | 04563 523427 | China |
| 4 | Anne | James | 09378 482894 | USA |
| 5 | Khalid | Shirvani | 02343 536522 | France |

## Second Normal Form (2NF)

> **Spec point** — `spcpt_v3by4SFDxGTZgfwP`

## Second Normal Form (2NF)

### What is second normal form?

- For a table to be in second normal form it must:

  - **Fulfil all 1NF requirements**
  - **Partial dependencies can only occur when the primary key is a composite key, so a 1NF table with a single-field primary key is already in 2NF**
  - **Have full functional dependency**
  
    - **All non-prime attributes (attributes not part of the primary key) must be fully dependent on the primary key**
  - **Have no partial dependencies**
  
    - Non-prime attributes must not depend on only part of the primary key (in case of a composite primary key)
    - Separate tables should be created for partially dependent attributes
- In this table below, `Course Title` **only depends on part** of the compound primary key (the course code) and not the Date so this table **is not **in second normal form

**Table: Course**

| Course | Date | Course Title | Room | Capacity | Available |
|---|---|---|---|---|---|
| SQL101 | 03/01/2020 | SQL Basics | 4A | 12 | 4 |
| DB202 | 03/01/2020 | Database Design | 7B | 14 | 7 |
| SQL101 | 04/05/2020 | SQL Basics | 7B | 14 | 10 |
| SQL101 | 15/05/2020 | SQL Basics | 12A | 8 | 8 |
| CS50 | 31/05/2020 | C Programming | 4A | 12 | 11 |

- To turn this table into second normal form we will ensure:

  - `Course Title` is moved into its own **Course** table
  - A `Session` table is created to use the full key (`Course`, `Date`) for all time-specific info
  - No **partial dependencies** remain

**Table: Course**

| Course | Course Title |
|---|---|
| SQL101 | SQL Basics |
| DB202 | Database Design |
| CS50 | C Programming |

**Table: Session**

| Course | Date | Room | Capacity | Available |
|---|---|---|---|---|
| SQL101 | 03/01/2020 | 4A | 12 | 4 |
| DB202 | 03/01/2020 | 7B | 14 | 7 |
| SQL101 | 04/05/2020 | 7B | 14 | 10 |
| SQL101 | 15/05/2020 | 12A | 8 | 8 |
| CS50 | 31/05/2020 | 4A | 12 | 11 |

## Third Normal Form (3NF)

> **Spec point** — `spcpt_YvWkT6ZkT2qFRBpN`

## Third Normal Form (3NF)

### What is third normal form?

- For a table to be in third normal form it must:

  - **Fulfil all 2NF requirements**
  - **Have no transitive dependencies**
  
    - Non-prime attributes must not depend on other non-prime attributes
  - **Have each non-prime attribute dependent solely on the primary key, not on other non-prime attributes**
  - **Have separate tables for attributes with transitive dependencies, linked using a foreign key**
- In this table below, `Description` depends on `Certificate`, which is not the primary key (`FilmID` → `Certificate` → `Description`)
- This is a **transitive dependency**, so this table is **not** in third normal form

| FilmID | Title | Certificate | Description |
|---|---|---|---|
| 12034 | Saw IV | 18 | Eighteen and over |
| 12035 | Spiderman 2 | 12A | Age 12 and over |
| 12036 | Shrek | U | Universal |

- To turn this table into third normal form we will ensure:

  - Transitive dependency removed by **separating **`Description` into its own table
  - The `Film` table only stores fields that **directly depend** on the key (`FilmID`)
  - A **foreign key** (`Certificate`) is used to maintain the relationship

**Table: Film**

| FilmID | Title | Certificate |
|---|---|---|
| 12034 | Saw IV | 18 |
| 12035 | Spiderman 2 | 12A |
| 12036 | Shrek | U |

**Table: Certificate**

| Certificate | Description |
|---|---|
| 18 | Eighteen and over |
| 12A | Age 12 and over |
| U | Universal |

> **Worked Example**
> Match each normal form to its definition:
> 
> | First Normal Form (1NF) | All fields are fully dependent on the primary key. |
> |---|---|
> | Second Normal Form (2NF) | There are no repeating groups of attributes. |
> | Third Normal Form (3NF) | There are no partial dependencies. |
> 
> **[1]**
> 
> **Final answer:** **Answer**
> 
> | First Normal Form (1NF) | **There are no repeating groups of attributes.** |
> |---|---|
> | Second Normal Form (2NF) | **There are no partial dependencies.** |
> | Third Normal Form (3NF) | **All fields are fully dependent on the primary key.** |
