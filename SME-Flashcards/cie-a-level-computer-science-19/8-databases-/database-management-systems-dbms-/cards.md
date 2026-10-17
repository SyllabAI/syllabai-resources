# Database Management Systems (DBMS)

Course: cie-a-level-computer-science-19 · Section: 8. Databases

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/8-databases-/database-management-systems-dbms-/


## Card 1 — keyword_definition (`fl_DQj52ZyxR2DZtdKy`)

**FRONT**

Define **DBMS**.


**BACK**

A DBMS (Database Management System) is **software used to create, manage and interact with databases**.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 2 — keyword_definition (`fl_h2GTYsymNdmM4NbP`)

**FRONT**

Define **logical schema**.


**BACK**

A logical schema is the **overall logical design of the database**, covering tables, fields, relationships and constraints, showing how data is organised **independently of how it is physically stored**.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 3 — question_and_answer (`fl_DbMZXw8TMNZFf2vz`)

**FRONT**

How does a DBMS maintain data integrity?


**BACK**

It **enforces rules and constraints**, so data changed in one place is updated everywhere, and each **foreign key has a corresponding primary key**.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 4 — fill_in_the_blanks (`fl_GXhVK3ZzpXNYKrDk`)

**FRONT**

A DBMS uses <u>**                      **</u> such as primary keys and foreign keys to enforce data integrity.


**BACK**

A DBMS uses **constraints** such as primary keys and foreign keys to enforce data integrity.


*Blanks: 1 — answers: []*

Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`

Flags: blank_answer_mismatch


## Card 5 — keyword_definition (`fl_98y47Gn67VGFjfYG`)

**FRONT**

Define **concurrency control**.


**BACK**

Concurrency control allows **multiple users to access the database at the same time without errors**.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 6 — keyword_definition (`fl_ZvwwhpFkWfKrbCJC`)

**FRONT**

Define **data independence**.


**BACK**

Data independence ensures that **changes to storage methods do not affect how the data is used**.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 7 — question_and_answer (`fl_FFnRY8gFq9cGkWQJ`)

**FRONT**

How does a DBMS solve data redundancy?


**BACK**

A DBMS **centralises data**, so it is stored **once** and referenced whenever it is needed.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 8 — question_and_answer (`fl_9MhsCfrYjtjk5KmJ`)

**FRONT**

How does a DBMS solve data inconsistency?


**BACK**

A DBMS ensures **data consistency** by updating a **single source of truth**.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 9 — keyword_definition (`fl_Gg5dSXcbKk4SKt49`)

**FRONT**

Define **data dictionary**.


**BACK**

A data dictionary **defines all the data elements across the system**, such as field names, table names and data types.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 10 — question_and_answer (`fl_KHvfP6jD4SpnDzN6`)

**FRONT**

What tools does a DBMS provide for data modelling?


**BACK**

A DBMS uses **data modelling tools**, such as **E-R diagrams**, to define entities and their relationships.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 11 — question_and_answer (`fl_Q2mCSwz6Mxg6FP6W`)

**FRONT**

How does a DBMS improve data security compared with a file-based system?


**BACK**

A DBMS supports **user accounts, access rights and permissions** for individuals and groups, whereas a file-based system has poor control over who can access or change data.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 12 — question_and_answer (`fl_GhcVzG8y6CJ2rhVj`)

**FRONT**

How does a DBMS reduce the risk of data loss?


**BACK**

A DBMS includes **automated backup and recovery tools**.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 13 — true_or_false (`fl_9HxRS2t926HQs4ph`)

**FRONT**

**True or False?**

In a file-based system, backup procedures are usually automated.


**BACK**

**False.**

In a file-based system backups are often **manual and inconsistent**. It is a **DBMS** that provides automated backup and recovery tools.


Spec links: `spcpt_bxsBsBSGhJ5VdwYJ`


## Card 14 — question_and_answer (`fl_f2wwQYdKSZDggFns`)

**FRONT**

What does the developer interface allow developers to do?


**BACK**

It allows developers to **write database queries using Structured Query Language (SQL)**.


Spec links: `spcpt_5XKWt64PcsV2w3K2`


## Card 15 — question_and_answer (`fl_xMZ3Gt9drC2CyT8c`)

**FRONT**

Why is SQL more flexible than query-by-example?


**BACK**

SQL allows developers to create **more complex and precise queries** to search, update or manage data, whereas query-by-example tools are **visual and simplified**.


Spec links: `spcpt_5XKWt64PcsV2w3K2`


## Card 16 — question_and_answer (`fl_D3JjDVj2qPwz3dWW`)

**FRONT**

What is the query processor responsible for?


**BACK**

The query processor is responsible for **handling and executing SQL queries**.


Spec links: `spcpt_5XKWt64PcsV2w3K2`


## Card 17 — question_and_answer (`fl_Gqvkq9vY86DjsPzC`)

**FRONT**

Name the three components of the query processor.


**BACK**

The **DDL interpreter**, the **DML compiler** and the **query evaluation engine**.


Spec links: `spcpt_5XKWt64PcsV2w3K2`


## Card 18 — question_and_answer (`fl_c2zy7cBXHQg86F8t`)

**FRONT**

What does the DDL interpreter do?


**BACK**

It interprets **Data Definition Language commands** such as `CREATE`, `ALTER` and `DROP`, and **updates the data dictionary**.


Spec links: `spcpt_5XKWt64PcsV2w3K2`


## Card 19 — question_and_answer (`fl_s7nmcMnjDzpNmd5Z`)

**FRONT**

What does the DML compiler do?


**BACK**

It **compiles Data Manipulation Language statements** such as `SELECT`, `INSERT` and `UPDATE` into **low-level instructions**, and **optimises** the query.


Spec links: `spcpt_5XKWt64PcsV2w3K2`


## Card 20 — question_and_answer (`fl_cD2Qq8b9x66N3JM8`)

**FRONT**

What does the query evaluation engine do?


**BACK**

It **executes the compiled instructions** to retrieve or manipulate the actual data in the database.


Spec links: `spcpt_5XKWt64PcsV2w3K2`


## Card 21 — true_or_false (`fl_z78p4NHXvR4WCNQb`)

**FRONT**

**True or False?**

The DML compiler updates the data dictionary.


**BACK**

**False.**

The **DDL interpreter** updates the data dictionary. The **DML compiler** compiles and optimises DML statements.


Spec links: `spcpt_5XKWt64PcsV2w3K2`


## Card 22 — fill_in_the_blanks (`fl_5cxYZyT87QQWsrzK`)

**FRONT**

Together, the query processor's components ensure that a query is interpreted, optimised and executed <u>**                      **</u>.


**BACK**

Together, the query processor's components ensure that a query is interpreted, optimised and executed **efficiently**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_5XKWt64PcsV2w3K2`

Flags: blank_answer_mismatch

