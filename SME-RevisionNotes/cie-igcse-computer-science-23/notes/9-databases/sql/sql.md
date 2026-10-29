---
note_id: "rn_vjxqj4hgq9crZdbF"
title: "SQL"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/9-databases/sql/sql
path: 9-databases/sql/sql
updated_at: "2025-05-21T09:21:45.860Z"
spec_point_ids: ["spcpt_6nMNqQB7kkqFzt6H"]
spec_point_codes: []
guided_study: false
---

# SQL

## SQL

> **Spec point** — `spcpt_6nMNqQB7kkqFzt6H` · "4 Read, understand and complete structured query
language (SQL) scripts to query data stored in a
single database table"

## SQL

### What is SQL?

- **SQL **(Structured Query Language) is a programming language used to interact with a ***DBMS***.
- The use of SQL allows a user to:

  - **Select data **
  - **Order data**
  - **Sum data**
  - **Count data**

### Selecting data commands

| **Command** | **Description** | **Example** |
|---|---|---|
| **SELECT** | Retrieves data from a database table | **SELECT *** **FROM **users;<br>(retrieves all data from the 'users' table)<br><br>**SELECT **name, age<br>**FROM **users<br>(retrieves names and ages from the 'users' table) |
| **FROM** | Specifies the tables to retrieve data from | **SELECT **name, age **FROM **users;<br>(retrieves names and ages from the 'users' table) |
| **WHERE** | Filters the data based on a specified condition | **SELECT *** **FROM **users<br>**WHERE **age > 30;<br>(Retrieves users older than 30) |
| **AND** | Combines multiple conditions in a **WHERE **clause | **SELECT *** **FROM **users<br>**WHERE **age > 18 **AND **city = 'New York';<br>(retrieves users older than 18 and from New York) |
| **OR** | Retrieves data when at least one of the conditions is true | **SELECT *** **FROM **users<br>**WHERE **age < 18 **OR **city = 'New York';<br>(retrieves users younger than 18 or from New York) |
| **WILDCARDS** | '*****' and '**%**' symbols are used for searching and matching data<br>'*****' used to select all columns in a table<br>'**%**' used as a wildcard character in the LIKE operator | **SELECT** * **FROM** users;<br>(retrieves all columns for the 'users' table)<br><br>**SELECT *** **FROM **users **WHERE **name **LIKE **'J%';<br>(retrieves users whose names start with 'J') |
| **ORDER BY** | How data is organised (sorted) when it is retrieved | **SELECT **Forename, Lastname** FROM **Students<br>**WHERE **StudentID < 10<br>**ORDER BY **Lastname, Forename** ASC**<br><br>(retrieves only the *forename* and *lastname* of all students from the *students* table who have a *studentID* of less than 10 and displays in ascending order by *lastname* and *forename*) |
| **SUM** | Adds up and outputs the sum of a field | **SELECT SUM**(Salary) **FROM** tbl_people; |
| **COUNT** | Counts the number of rows which match the set criteria | **SELECT COUNT**(*)<br><br>**FROM **tbl_people<br><br>**WHERE **Salary > 50000; |

### Examples

- Select all the fields from the Customers table

**Command:**

| **SELECT *** **FROM **Customers; |
|---|

**Output:**

| **ID** | **Name** | **Age** | **City** | **Country** |
|---|---|---|---|---|
| 1 | John Doe | 30 | New York | USA |
| 2 | Jane Doe | 25 | London | UK |
| 3 | Peter Lee | 40 | Paris | France |

- Select the ID, name & age of customers who are older than 25

**Command:**

| **SELECT **ID, name, age <br>**FROM **Customers<br>**WHERE **Age > 25; |
|---|

**Output:**

| **ID** | **Name** | **Age** |
|---|---|---|
| 1 | John Doe | 30 |
| 3 | Peter Lee | 40 |

- Select the name and country of customers who are from a country that begins with 'U'

**Command:**

| **SELECT **Name, Country<br>**FROM **Customers<br>**WHERE **Country **LIKE** 'U%'; |
|---|

**Output:**

| **Name** | **Country** |
|---|---|
| John Doe | USA |
| Jane Doe | UK |

- Select all fields of customers who are from 'London' or 'Paris'

**Command:**

| **SELECT ***<br>**FROM **Customers<br>**WHERE **City = 'London' **OR** City = 'Paris'; |
|---|

**Output:**

| **ID** | **Name** | **Age** | **City** | **Country** |
|---|---|---|---|---|
| 2 | Jane Doe | 25 | London | UK |
| 3 | Peter Lee | 40 | Paris | France |

> **Worked Example**
> Below is a table of animals called ***tbl_animals***
> 
> | **Animal** | **Breeding** | **Number of Young ** |
> |---|---|---|
> | Red Fox | Yes | 4-6 |
> | Rabbit | Yes | 4-12 |
> | African Elephant | Yes | 1 |
> | Blue Whale | No | 1 |
> | Orangutan | Yes | 1 |
> | Polar Bear | Yes | 1-3 |
> | Dolphin | Yes | 1 |
> | Kangaroo | Yes | 1 |
> | Lion | Yes | 1-6 |
> | Penguin | Yes | 1 |
> 
> Complete this SQL statement to display all of the animal breeds that are currently breeding and there was only one young born this year **[3]**
> 
> SELECT  .................................................
> 
> FROM  .................................................
> 
> WHERE .................................................
> 
> **Final answer:** **Answer**
> 
> **SELECT **** ****Animal**** [1]**
> 
> **FROM  ****tbl_animals **** [1]**
> 
> **WHERE ****Breeding = "Yes" AND**** ****Number of Young = 1 **** [1]**
