# Database Concepts

Course: cie-a-level-computer-science-19 · Section: 8. Databases

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/8-databases-/database-concepts/


## Card 1 — keyword_definition (`fl_Qn9zdmhWKJrzvs83`)

**FRONT**

Define **file-based system**.


**BACK**

A file-based system is any system where **data is stored in separate files**, such as text files or spreadsheets.


Spec links: `spcpt_P787CgxNkKFMC6Sx`


## Card 2 — question_and_answer (`fl_D4TsG3rf23Grm5p6`)

**FRONT**

Why does a file-based system have no central control?


**BACK**

Each **application or department has its own files**, which are often standalone, so there is no shared structure.


Spec links: `spcpt_P787CgxNkKFMC6Sx`


## Card 3 — keyword_definition (`fl_ZqRgMWbwr6CbP7c3`)

**FRONT**

Define **data redundancy**.


**BACK**

Data redundancy is when the **same data is stored in multiple files**, leading to duplication.


Spec links: `spcpt_P787CgxNkKFMC6Sx`


## Card 4 — keyword_definition (`fl_3yCTgvKzHT7JJQQx`)

**FRONT**

Define **data inconsistency**.


**BACK**

Data inconsistency is when **one file is updated but others are not**, which makes the data unreliable.


Spec links: `spcpt_P787CgxNkKFMC6Sx`


## Card 5 — question_and_answer (`fl_TZfywchQ76tvZzB7`)

**FRONT**

Why are file-based systems difficult to update?


**BACK**

Changes must be made in **several places**, which increases the time taken and the risk of error.


Spec links: `spcpt_P787CgxNkKFMC6Sx`


## Card 6 — question_and_answer (`fl_VjD5jwcRwH3szZGf`)

**FRONT**

Name three limitations of a file-based system.


**BACK**

Limitations include **data redundancy**, **data inconsistency**, **lack of data integrity**, **poor security**, **difficulty updating**, **limited scalability**, **no central control** and **difficulty managing relationships**.


Spec links: `spcpt_P787CgxNkKFMC6Sx`


## Card 7 — true_or_false (`fl_S2Gwmh9T5QPG6Npz`)

**FRONT**

**True or False?**

File-based systems are suitable for large volumes of data with complex relationships.


**BACK**

**False.**

File-based systems have **limited scalability** and cannot easily link related data across files.


Spec links: `spcpt_P787CgxNkKFMC6Sx`


## Card 8 — keyword_definition (`fl_vynGNWQRQWsdtPPg`)

**FRONT**

Define **flat file database**.


**BACK**

A flat file database stores all of its data in a **single table**.


Spec links: `spcpt_WN37ppXhzxdy2v2d`


## Card 9 — keyword_definition (`fl_PnbBxmtpHkDtvxfw`)

**FRONT**

Define **relational database**.


**BACK**

A relational database organises data into **multiple tables** and uses **keys** to connect related data.


Spec links: `spcpt_WN37ppXhzxdy2v2d`


## Card 10 — question_and_answer (`fl_jG8GZX3p5szSVbBM`)

**FRONT**

What is the difference between a flat file and a relational database?


**BACK**

A **flat file** stores everything in **one table**, which causes redundancy. A **relational** database uses **multiple tables linked by keys**, which reduces redundancy and is easier to maintain.


Spec links: `spcpt_WN37ppXhzxdy2v2d`


## Card 11 — question_and_answer (`fl_7w8yJqJkWwxJNkgm`)

**FRONT**

Give one advantage of a flat file database.


**BACK**

A flat file database is **simple and easy to understand**.


Spec links: `spcpt_WN37ppXhzxdy2v2d`


## Card 12 — question_and_answer (`fl_TVfMPZm6bZJDZsg9`)

**FRONT**

How does a relational database prevent inconsistent data?


**BACK**

Each piece of data is stored **only once**, so changing it **updates it across the entire database**.


Spec links: `spcpt_WN37ppXhzxdy2v2d`


## Card 13 — fill_in_the_blanks (`fl_D739gR5sjyhsGFtX`)

**FRONT**

A relational database uses keys to connect related data, which reduces data <u>**                    **</u>.


**BACK**

A relational database uses keys to connect related data, which reduces data **redundancy**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_WN37ppXhzxdy2v2d`

Flags: blank_answer_mismatch


## Card 14 — keyword_definition (`fl_3M5W3yZNzjJH5sCK`)

**FRONT**

Define **entity**.


**BACK**

An entity is a **real-world object or concept that data is stored about**, for example a student or a book.


Spec links: `spcpt_nt6wCsbXQScDX5S8`


## Card 15 — fill_in_the_blanks (`fl_hqptm5t3yHpb6CbN`)

**FRONT**

A <u>**          **</u> is a collection of data about an entity, organised in rows and columns.


**BACK**

A **table** is a collection of data about an entity, organised in rows and columns.


*Blanks: 1 — answers: []*

Spec links: `spcpt_nt6wCsbXQScDX5S8`

Flags: blank_answer_mismatch


## Card 16 — keyword_definition (`fl_gG3VGnpbWB5mQwN2`)

**FRONT**

Define **record (tuple)**.


**BACK**

A record is a **single row in a table**, representing one instance of an entity.


Spec links: `spcpt_nt6wCsbXQScDX5S8`


## Card 17 — keyword_definition (`fl_RMyHtNHvZ24j9gg9`)

**FRONT**

Define **field (attribute)**.


**BACK**

A field is a **single column in a table**, storing one piece of data about the entity.


Spec links: `spcpt_nt6wCsbXQScDX5S8`


## Card 18 — keyword_definition (`fl_G46tGD3kgSQFSJZr`)

**FRONT**

Define **primary key**.


**BACK**

A primary key is a **unique identifier for each record** in a table.


Spec links: `spcpt_nt6wCsbXQScDX5S8`


## Card 19 — keyword_definition (`fl_MXWNk6Fz3Kx4sW92`)

**FRONT**

Define **candidate key**.


**BACK**

A candidate key is a field, or combination of fields, that **could be used as a primary key**.


Spec links: `spcpt_nt6wCsbXQScDX5S8`


## Card 20 — keyword_definition (`fl_hGKKgHDS8XFcrShf`)

**FRONT**

Define **secondary key**.


**BACK**

A secondary key is a field used for **searching or sorting**, but which is **not necessarily unique**.


Spec links: `spcpt_nt6wCsbXQScDX5S8`


## Card 21 — true_or_false (`fl_YkzvNSTQVZZGXPXy`)

**FRONT**

**True or False?**

A secondary key must be unique.


**BACK**

**False.**

A secondary key is used for searching or sorting and is **not necessarily unique**. It is the **primary key** that must uniquely identify each record.


Spec links: `spcpt_nt6wCsbXQScDX5S8`


## Card 22 — question_and_answer (`fl_mjrwtjVbZYZ2Y84r`)

**FRONT**

What is the difference between a primary key and a foreign key?


**BACK**

A **primary key** uniquely identifies each record **in its own table**. A **foreign key** links to the primary key **in another table** to create a relationship.


Spec links: `spcpt_nt6wCsbXQScDX5S8`


## Card 23 — keyword_definition (`fl_DnDPwjKNZJ3ZXnS9`)

**FRONT**

Define **referential integrity**.


**BACK**

Referential integrity ensures that **foreign keys match a primary key** in the related table, which prevents broken links.


Spec links: `spcpt_nt6wCsbXQScDX5S8`


## Card 24 — keyword_definition (`fl_zTTp5qS3V7RJ9PQv`)

**FRONT**

Define **indexing**.


**BACK**

Indexing is a technique to **speed up searching** in a table by creating an **ordered list of key fields**.


Spec links: `spcpt_nt6wCsbXQScDX5S8`


## Card 25 — question_and_answer (`fl_wkjHpdkbd3rnBTRY`)

**FRONT**

Name the three types of relationship between entities.


**BACK**

**One-to-one**, **one-to-many** and **many-to-many**.


Spec links: `spcpt_nt6wCsbXQScDX5S8`


## Card 26 — keyword_definition (`fl_cVNtKRXVDYZ5RB2X`)

**FRONT**

Define **entity-relationship (E-R) diagram**.


**BACK**

An E-R diagram is a diagram that represents the **entities (tables) that will be in a database** and the **relationships between those entities**.


Spec links: `spcpt_XdgV5kCRhdjch4fd`


## Card 27 — keyword_definition (`fl_ShDhXMW7Fd89mkYx`)

**FRONT**

Define **entity**.


**BACK**

An entity is something worthy of **capturing and storing data about**, for example students, orders, products, courses or customers.


Spec links: `spcpt_XdgV5kCRhdjch4fd`


## Card 28 — question_and_answer (`fl_BP8XrNB5hhXCZGnS`)

**FRONT**

What do entities become in a relational database?


**BACK**

Entities become **tables** in a relational database.


Spec links: `spcpt_XdgV5kCRhdjch4fd`


## Card 29 — fill_in_the_blanks (`fl_S6yQ8jp5Hxp4VCGy`)

**FRONT**

Relational databases store different entities in <u>**                **</u> tables.


**BACK**

Relational databases store different entities in **separate** tables.


*Blanks: 1 — answers: []*

Spec links: `spcpt_XdgV5kCRhdjch4fd`

Flags: blank_answer_mismatch


## Card 30 — question_and_answer (`fl_bNDKg8fHrfxp7v4m`)

**FRONT**

What determines how tables are linked in a relational database?


**BACK**

Linking tables depends on the **relationships between the entities**.


Spec links: `spcpt_XdgV5kCRhdjch4fd`


## Card 31 — question_and_answer (`fl_HSKQwbp8p59nFpg9`)

**FRONT**

What is another name for the type of a relationship?


**BACK**

The type of a relationship is sometimes called its **degree**.


Spec links: `spcpt_XdgV5kCRhdjch4fd`


## Card 32 — question_and_answer (`fl_7d6wSD3Rc3vxmbq9`)

**FRONT**

How are entities drawn on an E-R diagram?


**BACK**

Entities are drawn as **boxes**, with the **name of the entity inside** the box.


Spec links: `spcpt_XdgV5kCRhdjch4fd`


## Card 33 — question_and_answer (`fl_ZwvMyPGddsKtsrzf`)

**FRONT**

What notation is used to draw relationships on an E-R diagram?


**BACK**

Relationships are drawn using **crow's feet notation**.


Spec links: `spcpt_XdgV5kCRhdjch4fd`


## Card 34 — question_and_answer (`fl_PCbg3THQdMgr5nMP`)

**FRONT**

What is the relationship between a customer and an order?


**BACK**

It is **one-to-many**. One customer can make **many** orders, but each order relates to **one** customer.


Spec links: `spcpt_XdgV5kCRhdjch4fd`


## Card 35 — question_and_answer (`fl_jMHbftvvXPYMSrVg`)

**FRONT**

What is the relationship between an order and a product?


**BACK**

It is **many-to-many**. An order can contain **many** products, and a product can appear on **many** orders.


Spec links: `spcpt_XdgV5kCRhdjch4fd`


## Card 36 — true_or_false (`fl_nMQ2ZfNTvmZBRtKx`)

**FRONT**

**True or False?**

One-to-one relationships are common in databases.


**BACK**

**False.**

One-to-one relationships do exist, but they are **not very common** in databases.


Spec links: `spcpt_XdgV5kCRhdjch4fd`


## Card 37 — fill_in_the_blanks (`fl_7Tp7hF3TS5Z4DjS8`)

**FRONT**

The three types of relationship between entities are one-to-one, one-to-many and <u>**                        **</u>.


**BACK**

The three types of relationship between entities are one-to-one, one-to-many and **many-to-many**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_XdgV5kCRhdjch4fd`

Flags: blank_answer_mismatch


## Card 38 — keyword_definition (`fl_6NqQbnwFnrBNp8f4`)

**FRONT**

Define **normalised design**.


**BACK**

A normalised design is a database structure that **organises data efficiently**, **eliminates unnecessary duplication**, **ensures data integrity** and **supports easy updates and accurate relationships**.


Spec links: `spcpt_jw3J5d9XNpWJcJDM`


## Card 39 — question_and_answer (`fl_5zjkGM4G5H8GHG7B`)

**FRONT**

Name three things you must be able to do when producing a normalised design.


**BACK**

Identify **repeating groups or duplicated data**, break the data into **separate related tables**, assign **primary and foreign keys**, show the database in **1NF, 2NF and 3NF**, and clearly show the **relationships** between tables.


Spec links: `spcpt_jw3J5d9XNpWJcJDM`


## Card 40 — question_and_answer (`fl_NtjZ5dHgDSPdM2Wp`)

**FRONT**

What usually indicates that more than one table is needed?


**BACK**

**Repeated or duplicated values** in the fields usually indicate the need for more than one table.


Spec links: `spcpt_jw3J5d9XNpWJcJDM`


## Card 41 — question_and_answer (`fl_NGwFBpxWqSbNhNPj`)

**FRONT**

Why does every table need a primary key?


**BACK**

Every table needs a **unique identifier** for its records.


Spec links: `spcpt_jw3J5d9XNpWJcJDM`


## Card 42 — question_and_answer (`fl_wwKhVWjDfrctDtY3`)

**FRONT**

What is the purpose of a foreign key in a normalised design?


**BACK**

A foreign key **links related tables** and ensures **referential integrity**.


Spec links: `spcpt_jw3J5d9XNpWJcJDM`


## Card 43 — fill_in_the_blanks (`fl_DWJ7HHXMnSYbgwCM`)

**FRONT**

In a normalised design, a link table is used to handle a <u>**                        **</u> relationship.


**BACK**

In a normalised design, a link table is used to handle a **many-to-many** relationship.


*Blanks: 1 — answers: []*

Spec links: `spcpt_jw3J5d9XNpWJcJDM`

Flags: blank_answer_mismatch


## Card 44 — true_or_false (`fl_bBQQjmK963KvHp3C`)

**FRONT**

**True or False?**

A normalised design can only be produced from a table of unnormalised data.


**BACK**

**False.**

A normalised design may be produced from a **written description** of a system, a **table of unnormalised data**, or a set of **existing flat tables**.


Spec links: `spcpt_jw3J5d9XNpWJcJDM`


## Card 45 — question_and_answer (`fl_CCdFy95SYRdQkKN8`)

**FRONT**

What order should the normal forms be applied in?


**BACK**

Apply **1NF** first, then **2NF**, then **3NF**.


Spec links: `spcpt_jw3J5d9XNpWJcJDM`


## Card 46 — question_and_answer (`fl_WTVGbQjTccd63Db2`)

**FRONT**

What four conditions must a table meet to be in first normal form?


**BACK**

It must contain **atomic values**, have **no repeating groups**, have **unique column names**, and have a **unique identifier (primary key)**.


Spec links: `spcpt_7t9KdWBjJVFtTGQ3`


## Card 47 — keyword_definition (`fl_kP9jb7fm2t3MxP6C`)

**FRONT**

Define **atomic value**.


**BACK**

An atomic value is a **single, indivisible value** held in a column.


Spec links: `spcpt_7t9KdWBjJVFtTGQ3`


## Card 48 — question_and_answer (`fl_N4Xj7GRtJpgrtvTm`)

**FRONT**

Why is a customers table with a single 'name' field not in first normal form?


**BACK**

The whole name is stored in **one field**, so it is **not atomic**. It should be split into **forename** and **surname** fields.


Spec links: `spcpt_7t9KdWBjJVFtTGQ3`


## Card 49 — true_or_false (`fl_yC5M4mbzwXJTZb4q`)

**FRONT**

**True or False?**

A table with a column containing a list of values can be in first normal form.


**BACK**

**False.**

Columns must **not contain arrays or lists of values**, because a 1NF table must have **no repeating groups**.


Spec links: `spcpt_7t9KdWBjJVFtTGQ3`


## Card 50 — fill_in_the_blanks (`fl_TZyDQjF7mMhYNXRg`)

**FRONT**

For a table to be in first normal form, each column must have a <u>**            **</u> name within the table.


**BACK**

For a table to be in first normal form, each column must have a **unique** name within the table.


*Blanks: 1 — answers: []*

Spec links: `spcpt_7t9KdWBjJVFtTGQ3`

Flags: blank_answer_mismatch


## Card 51 — question_and_answer (`fl_fqDBWbCQDxPx4ydX`)

**FRONT**

Why must each row in a first normal form table have a unique identifier?


**BACK**

So that each row can be **distinguished from the other rows** in the table.


Spec links: `spcpt_7t9KdWBjJVFtTGQ3`


## Card 52 — question_and_answer (`fl_9yFxvtjktVf6PwxD`)

**FRONT**

What must a table satisfy to be in second normal form?


**BACK**

It must **fulfil all 1NF requirements**, have **full functional dependency**, and have **no partial dependencies**.


Spec links: `spcpt_v3by4SFDxGTZgfwP`


## Card 53 — question_and_answer (`fl_zPWz9thztxq4zr3J`)

**FRONT**

Which tables does second normal form apply to?


**BACK**

Second normal form only applies to tables that have a **compound (composite) primary key**.


Spec links: `spcpt_v3by4SFDxGTZgfwP`


## Card 54 — keyword_definition (`fl_h6THhgv5KgGrd8Vw`)

**FRONT**

Define **non-prime attribute**.


**BACK**

A non-prime attribute is an attribute that is **not part of the primary key**.


Spec links: `spcpt_v3by4SFDxGTZgfwP`


## Card 55 — keyword_definition (`fl_yyXbcjjkFVYFh448`)

**FRONT**

Define **partial dependency**.


**BACK**

A partial dependency is when a non-prime attribute depends on **only part of a composite primary key**.


Spec links: `spcpt_v3by4SFDxGTZgfwP`


## Card 56 — question_and_answer (`fl_RjdZKm3JzDZ3bbN9`)

**FRONT**

A Course table has the compound primary key (Course, Date) and also holds Course Title.

Why is this not in second normal form?


**BACK**

Course Title depends **only on the Course code**, not on the **whole key** of Course and Date, so it is a **partial dependency**.


Spec links: `spcpt_v3by4SFDxGTZgfwP`


## Card 57 — question_and_answer (`fl_h9S5fPQqy33NvsKv`)

**FRONT**

How is a partial dependency removed?


**BACK**

**Separate tables** are created for the partially dependent attributes.


Spec links: `spcpt_v3by4SFDxGTZgfwP`


## Card 58 — question_and_answer (`fl_tmrKdqKwBMhN9kWT`)

**FRONT**

What must a table satisfy to be in third normal form?


**BACK**

It must **fulfil all 2NF requirements** and have **no transitive dependencies**.


Spec links: `spcpt_YvWkT6ZkT2qFRBpN`


## Card 59 — keyword_definition (`fl_cDPFkNXJDdrdG8v9`)

**FRONT**

Define **transitive dependency**.


**BACK**

A transitive dependency is when a non-prime attribute **depends on another non-prime attribute** rather than on the primary key.


Spec links: `spcpt_YvWkT6ZkT2qFRBpN`


## Card 60 — true_or_false (`fl_prWtTS7sT4FB3mcM`)

**FRONT**

**True or False?**

In third normal form, a non-key field may depend on another non-key field.


**BACK**

**False.**

Each non-prime attribute must depend **solely on the primary key**, not on other non-prime attributes.


Spec links: `spcpt_YvWkT6ZkT2qFRBpN`


## Card 61 — question_and_answer (`fl_bx8TWJBQ3kT7mTG4`)

**FRONT**

A Film table holds FilmID, Title, Certificate and Description.

How is it put into third normal form?


**BACK**

The transitive dependency is removed by **separating Description into its own table**, so the Film table only stores fields that **directly depend on FilmID**. **Certificate** is then used as a **foreign key** to maintain the relationship.


Spec links: `spcpt_YvWkT6ZkT2qFRBpN`


## Card 62 — question_and_answer (`fl_pmNkpgnbBP44B8nN`)

**FRONT**

How are tables linked after a transitive dependency has been separated out?


**BACK**

They are linked using a **foreign key**.


Spec links: `spcpt_YvWkT6ZkT2qFRBpN`

