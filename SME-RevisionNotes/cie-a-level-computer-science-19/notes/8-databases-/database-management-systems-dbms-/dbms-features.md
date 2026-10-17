---
note_id: "rn_6h3gsW5xG5TSr2Vm"
title: "DBMS Features"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/8-databases-/database-management-systems-dbms-/dbms-features
path: 8-databases-/database-management-systems-dbms-/dbms-features
updated_at: "2026-01-12T10:12:25.871Z"
spec_point_ids: ["spcpt_bxsBsBSGhJ5VdwYJ", "spcpt_5XKWt64PcsV2w3K2"]
spec_point_codes: []
guided_study: false
---

# DBMS Features

## DBMS vs file-based systems

> **Spec point** — `spcpt_bxsBsBSGhJ5VdwYJ`

## DBMS vs file-based systems

### What is a DBMS?

- A DBMS (Database Management System) is **software** that is used to **create, manage, and interact with databases**
- A DBMS provides several **key features**, including:

  - Defines a **logical schema** – the overall logical design of the database (tables, fields, relationships, and constraints), showing how data is organised independently of how it is physically stored
  - Provides **data security** and **access control** to keep data safe
  - Maintains **data integrity** by enforcing rules and constraints, e.g.
  
    - If the data is changed in one place it is updated in every other place
    - Ensures each foreign key has a corresponding primary key
  - Supports **concurrency control** so multiple users can access the database at the same time without errors
  - Ensures **data independence** so changes to storage methods do not affect how data is used
  - Offers **backup and recovery** tools to protect against data loss
- It addresses the [limitations of file-based systems](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/8-databases-/database-concepts/database-models/) by:

| **Area** | **Limitation in file-based systems** | **How a DBMS solves it** |
|---|---|---|
| **Data redundancy** | Same data is stored in multiple files, wasting space and causing confusion | A DBMS **centralises data**, so it is stored once and referenced when needed |
| **Data inconsistency** | Data may differ between files if one is updated but others are not | A DBMS ensures **data consistency** by updating a single source of truth |
| **Data management** | Each application stores and manages its own data | A DBMS provides a **data dictionary** that defines all data elements across the system (field/table names, data types) |
| **Data modelling** | No structured way to represent or link data | A DBMS uses **data modelling tools** (e.g. ER diagrams) to define entities and relationships |
| **Logical schema** | The overall logical design of the database (tables, fields, relationships, and constraints) | Shows how data is **organised and used**, independently of how it is physically stored |
| **Data integrity** | Difficult to enforce validation rules across different files | A DBMS uses **constraints** (e.g. primary keys, foreign keys) to enforce integrity |
| **Data security** | Poor control over who can access or change data | A DBMS supports **user accounts, access rights, and permissions** for individuals/groups |
| **Backup procedures** | Often manual and inconsistent | A DBMS includes **automated backup and recovery tools** to reduce risk of data loss |

## DBMS tools

> **Spec point** — `spcpt_5XKWt64PcsV2w3K2`

## DBMS tools

### Developer interface

- The developer interface allows developers to **write database queries** using **Structured Query Language (SQL)**
- This is more flexible than using **query-by-example** tools, which are visual and simplified
- Using SQL allows the developer to create **more complex and precise queries** to search, update, or manage data

### Query processor

- The query processor is responsible for **handling and executing SQL queries**
- It has several key components:

| **Component** | **Function** |
|---|---|
| **DDL interpreter** | Interprets **Data Definition Language (DDL)** commands like `CREATE`, `ALTER`, and `DROP` and updates the **data dictionary** |
| **DML compiler** | Compiles **Data Manipulation Language (DML)** statements (e.g. `SELECT`, `INSERT`, `UPDATE`) into low-level instructions and **optimises** the query |
| **Query evaluation engine** | Executes the compiled instructions to **retrieve or manipulate** the actual data in the database |

- Together, these components make sure that any query written by the developer is **interpreted, optimised**, and **executed efficiently**

> **Worked Example**
> State what is meant by a data dictionary and give one example of an item typically found in a data dictionary. **[2]**
> 
> **Final answer:** **Answer**
> 
> - A data dictionary is data about the data structure in the database **[1 mark]**
> - Example: field name, data type, or table name** [1 mark]**
