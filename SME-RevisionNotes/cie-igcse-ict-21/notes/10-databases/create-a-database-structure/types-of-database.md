---
note_id: "rn_rCCFzGbRgVT5jMQJ"
title: "Types of Database"
source: https://www.savemyexams.com/igcse/ict/cie/21/revision-notes/10-databases/create-a-database-structure/types-of-database
path: 10-databases/create-a-database-structure/types-of-database
updated_at: "2025-02-25T12:21:11.244Z"
spec_point_ids: ["spcpt_Tq7PWWybMFmH5WqY", "spcpt_wg5nw8GVNHqmbYPb", "spcpt_QPrxg8h52VbB8cVt"]
spec_point_codes: []
guided_study: false
---

# Types of Database

### What is a database?

- A** Database **is a structured, persistent collection of data
- It allows **easy storage, retrieval, and management** of information
- Electronic databases offer a number of key benefits:

  - **Easier to add, delete, modify and update data**
  - **Data can be backed up and copied easier**
  - **Multiple users, from multiple locations, can access the same database at the same time**
- There are two main types of database

  - **Flat file**
  - **Relational**

## Flat file

> **Spec point** — `spcpt_Tq7PWWybMFmH5WqY`

## Flat file

### What is a flat file database?

- A **flat file database** is one that stores all data in a **single table**
- It is **simple **and easy to understand but causes data ***redundancy***, **inefficient** storage and is **harder **to maintain
- Consider this example **flat file** table of students ![flat-file-table](assets/0713cd9811d6-flat-file-table.png)

  - This table has redundant data - the tutor and form room information repeats, this is inefficient
  - If a tutor changed their name we would need to find all instances of that name and change them all
  - Missing any would mean the **table **had **inconsistent data**

## Relational

> **Spec point** — `spcpt_wg5nw8GVNHqmbYPb`

## Relational

### What is a relational database?

- A **relational database** is one that organises data into multiple tables
- It uses **keys **to connect related data which **reduces data redundancy**, makes **efficient **use of storage and is **easier **to maintain
- A **relational **database solves the issues in a flat file database: ![relational-database](assets/3eafec2533e6-relational-database.png)

  - A new **table **could be created to store the tutor information and the tutor information in the student table could be moved to the new **table**
  - Then a **foreign key** in the student **table **(TutorID) could link a student to their tutor

  - Now the name of each tutor and their form room is stored** only once**
  - This means if they change only one piece of data, the data is updated in the **entire database **and ***inconsistency*** is avoided

## Tables & Records

> **Spec point** — `spcpt_QPrxg8h52VbB8cVt`

## Tables & records

### What is a table?

- A table is **a complete set of records** about the same subject/topic in a database
- An example of a database **table **named **cars** is below

***cars***

| **car_id** | **make** | **model** | **colour** | **price** |
|---|---|---|---|---|
| 1 | Peugeot | 2008 | Red | 24950 |
| 2 | Mazda | MX5 | Blue | 17995 |
| 3 | Citroen | DS4 | Black | 21450 |
| 4 | Ford | Puma | White | 19500 |

### What is a record?

- A record is **complete set of fields** on a single entity in a table (**row**)
- An example of a **record **in the cars **table below **is highlighted in green

***cars***

| **car_id** | **make** | **model** | **colour** | **price** |
|---|---|---|---|---|
| 1 | Peugeot | 2008 | Red | 24950 |
| **Final answer:** **2** | **Final answer:** **Mazda** | **Final answer:** **MX5** | **Final answer:** **Blue** | **Final answer:** **17995** |
| 3 | Citroen | DS4 | Black | 21450 |
| 4 | Ford | Puma | White | 19500 |
