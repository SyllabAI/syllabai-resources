# Data Definition Language (DDL) & Data Manipulation Language (DML)

Course: cie-a-level-computer-science-19 · Section: 8. Databases

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/8-databases-/data-definition-language-ddl-and-data-manipulation-language-dml/


## Card 1 — keyword_definition (`fl_gJPvpSqh8BfKMrGm`)

**FRONT**

Define **Data Definition Language (DDL)**.


**BACK**

DDL is used to **build and manage the structure** of a relational database, by creating and modifying tables, fields, indexes and relationships.


Spec links: `spcpt_4sNNXJzkJ6JY7QFT`


## Card 2 — keyword_definition (`fl_hwsWn4yY6PTxq2Wt`)

**FRONT**

Define **Data Manipulation Language (DML)**.


**BACK**

DML is used to **manage the data stored within** the database structures created by DDL, dealing with **adding, updating, deleting and retrieving** data.


Spec links: `spcpt_4sNNXJzkJ6JY7QFT`


## Card 3 — question_and_answer (`fl_tvcXXGbVqW34xmTS`)

**FRONT**

What is the difference between DDL and DML?


**BACK**

**DDL structures** the database, whereas **DML maintains the contents** of the database.


Spec links: `spcpt_4sNNXJzkJ6JY7QFT`


## Card 4 — question_and_answer (`fl_9mVJ8Ht43brJ2TZK`)

**FRONT**

What syntax do both DDL and DML use?


**BACK**

Both DDL and DML use **SQL syntax** to interact with the database.


Spec links: `spcpt_4sNNXJzkJ6JY7QFT`


## Card 5 — true_or_false (`fl_kRjjKjCzghWfM2ZV`)

**FRONT**

**True or False?**

A DBMS needs a different language for DDL and for DML.


**BACK**

**False.**

Most modern DBMSs use **SQL** to support **both** DDL and DML operations.


Spec links: `spcpt_4sNNXJzkJ6JY7QFT`


## Card 6 — fill_in_the_blanks (`fl_TGwYrgbRxtm5swJc`)

**FRONT**

DDL defines how data is <u>**            **</u> by creating and modifying tables, fields, indexes and relationships.


**BACK**

DDL defines how data is **stored** by creating and modifying tables, fields, indexes and relationships.


*Blanks: 1 — answers: []*

Spec links: `spcpt_4sNNXJzkJ6JY7QFT`

Flags: blank_answer_mismatch


## Card 7 — question_and_answer (`fl_8q2xdwNSmGNSrTVM`)

**FRONT**

What does `CREATE DATABASE` do?


**BACK**

`CREATE DATABASE` **creates a new database**.


Spec links: `spcpt_YvhTymvGYBsBHZVH`


## Card 8 — question_and_answer (`fl_7fwh8NWV3dJWvKBp`)

**FRONT**

What does `CREATE TABLE` do?


**BACK**

`CREATE TABLE` **creates a new table** with specified fields and data types.


Spec links: `spcpt_YvhTymvGYBsBHZVH`


## Card 9 — question_and_answer (`fl_BbKBNwNf2wKpPdJ9`)

**FRONT**

What does `ALTER TABLE` do?


**BACK**

`ALTER TABLE` **changes an existing table**, for example to add or remove fields.


Spec links: `spcpt_YvhTymvGYBsBHZVH`


## Card 10 — question_and_answer (`fl_NPNSzdnT3jqD2mJw`)

**FRONT**

Name the seven data types available for attributes.


**BACK**

`CHARACTER`, `VARCHAR(n)`, `BOOLEAN`, `INTEGER`, `REAL`, `DATE` and `TIME`.


Spec links: `spcpt_YvhTymvGYBsBHZVH`


## Card 11 — question_and_answer (`fl_W9TwxtMwzXXrnKYc`)

**FRONT**

What is the difference between `CHARACTER` and `VARCHAR(n)`?


**BACK**

`CHARACTER` stores **fixed-length text**, whereas `VARCHAR(n)` stores **variable-length text** up to a maximum length of n.


Spec links: `spcpt_YvhTymvGYBsBHZVH`


## Card 12 — question_and_answer (`fl_4XTCNX2QscPRQXY7`)

**FRONT**

Which data type stores whole numbers, and which stores decimal numbers?


**BACK**

`INTEGER` stores **whole numbers** and `REAL` stores **decimal numbers**.


Spec links: `spcpt_YvhTymvGYBsBHZVH`


## Card 13 — fill_in_the_blanks (`fl_w3jC6ZzdPFhpdQYj`)

**FRONT**

The data type <u>**              **</u> stores a True or False value.


**BACK**

The data type **BOOLEAN** stores a True or False value.


*Blanks: 1 — answers: []*

Spec links: `spcpt_YvhTymvGYBsBHZVH`

Flags: blank_answer_mismatch


## Card 14 — question_and_answer (`fl_xrvvZDmp7MJyGDrQ`)

**FRONT**

What does `PRIMARY KEY (field)` do?


**BACK**

It sets a field as the **primary key**, the unique identifier for records in that table.


Spec links: `spcpt_YvhTymvGYBsBHZVH`


## Card 15 — question_and_answer (`fl_Vx36FJkg2KhQrqtY`)

**FRONT**

Which commands can a `PRIMARY KEY` clause be used inside?


**BACK**

It can be used inside a `CREATE TABLE` command or an `ALTER TABLE` command.


Spec links: `spcpt_YvhTymvGYBsBHZVH`


## Card 16 — question_and_answer (`fl_5Mk2VwPFvKyS4tT3`)

**FRONT**

What does `FOREIGN KEY (field) REFERENCES Table(Field)` do?


**BACK**

It sets up a **foreign key relationship between two tables**.


Spec links: `spcpt_YvhTymvGYBsBHZVH`


## Card 17 — question_and_answer (`fl_VX3sCWhrfgYNS9NC`)

**FRONT**

What does `SELECT ... FROM` do?


**BACK**

`SELECT ... FROM` **retrieves specific columns** from a table.


Spec links: `spcpt_bsXwjxYjByd2Drmb`


## Card 18 — question_and_answer (`fl_cNK5NWgYB9QDxXyP`)

**FRONT**

What does `WHERE` do?


**BACK**

`WHERE` **filters the results based on a condition**.


Spec links: `spcpt_bsXwjxYjByd2Drmb`


## Card 19 — question_and_answer (`fl_BG8KHB5C8TdjmrbM`)

**FRONT**

Write an SQL statement that lists all students older than 16 from a `Students` table.


**BACK**

`SELECT * FROM Students WHERE Age > 16`


Spec links: `spcpt_bsXwjxYjByd2Drmb`


## Card 20 — question_and_answer (`fl_JKWv7rCTS6KSntj3`)

**FRONT**

What does `ORDER BY` do?


**BACK**

`ORDER BY` **sorts the results** into ascending or descending order.


Spec links: `spcpt_bsXwjxYjByd2Drmb`


## Card 21 — question_and_answer (`fl_sP2tqFV5fPg58KZ2`)

**FRONT**

What does `GROUP BY` do?


**BACK**

`GROUP BY` **groups rows that have the same value** in specified columns.


Spec links: `spcpt_bsXwjxYjByd2Drmb`


## Card 22 — question_and_answer (`fl_zNWRd8rF8Ztqj8WB`)

**FRONT**

What does `INNER JOIN` do?


**BACK**

`INNER JOIN` **combines rows from two tables where there is a matching key**.


Spec links: `spcpt_bsXwjxYjByd2Drmb`


## Card 23 — question_and_answer (`fl_WnyV6sM8swxFVWPk`)

**FRONT**

What is the difference between `SUM()` and `COUNT()`?


**BACK**

`SUM()` calculates the **total of a numeric column**, whereas `COUNT()` counts the **number of rows**, or the non-null entries in a column.


Spec links: `spcpt_bsXwjxYjByd2Drmb`


## Card 24 — question_and_answer (`fl_vFYYrh2Gdz4XP6Ch`)

**FRONT**

What does `AVG()` do?


**BACK**

`AVG()` calculates the **average value of a numeric column**.


Spec links: `spcpt_bsXwjxYjByd2Drmb`


## Card 25 — question_and_answer (`fl_8Qfxrh4GJkZX24bp`)

**FRONT**

What does `INSERT INTO` do?


**BACK**

`INSERT INTO` **adds a new record** to a table.


Spec links: `spcpt_bsXwjxYjByd2Drmb`


## Card 26 — question_and_answer (`fl_gpStnfWpThWNB2f9`)

**FRONT**

What does `DELETE FROM` do?


**BACK**

`DELETE FROM` **removes records** from a table.


Spec links: `spcpt_bsXwjxYjByd2Drmb`


## Card 27 — question_and_answer (`fl_2GXTmY5jbYyrDtjZ`)

**FRONT**

What does `UPDATE` do?


**BACK**

`UPDATE` **modifies existing data** in a table.


Spec links: `spcpt_bsXwjxYjByd2Drmb`


## Card 28 — true_or_false (`fl_txtmW5sp64xn9C3y`)

**FRONT**

**True or False?**

`UPDATE` is a DDL command.


**BACK**

**False.**

`UPDATE` is a **DML** command, because it changes the **data** in a table rather than the structure of the table.


Spec links: `spcpt_bsXwjxYjByd2Drmb`

