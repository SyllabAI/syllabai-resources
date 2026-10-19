# Exam Questions — Data Definition Language (DDL) & Data Manipulation Language (DML)
**8. Databases** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 17 questions across 1 sets


## Exam Questions (17 questions)


### Q1 — hard — 4 marks

**Q1** [4 marks]

The database `HOTEL` has two tables with the following definitions.

`GUEST(GuestID, FullName, Country, LoyaltyMember)`

`BOOKING(BookingID, GuestID, RoomNumber, CheckInDate)`

`GuestID` is the primary key of `GUEST` and a foreign key in `BOOKING`. No two guests have the same full name.

Write a Structured Query Language (SQL) script to return the full name of each guest together with the number of bookings that guest has made.

The number of bookings must be returned with the field name `NumberOfBookings`.

### Q2 — medium — 3 marks

**Q2** [3 marks]

The database `HOTEL` has the table `GUEST`, which has the following definition.

`GUEST(GuestID, FullName, Country, LoyaltyMember)`

`LoyaltyMember` is a Boolean field.

Write a Structured Query Language (SQL) script to add a new record to the table `GUEST` to store the following data.

| Attribute | Value |
|---|---|
| GuestID | G20418 |
| FullName | Amara Okafor |
| Country | Nigeria |
| LoyaltyMember | TRUE |

### Q3 — easy — 2 marks

**Q3** [2 marks]

A hotel uses a relational database called `HOTEL`. The database has the table `ROOM`, which has the following definition.

`ROOM(RoomNumber, RoomType, Floor, MaxGuests)`

`MaxGuests` stores the largest number of guests who can sleep in the room.

Write a Structured Query Language (SQL) script to return the room number of every room that can sleep four or more guests.

The room numbers must be listed in order, starting with the smallest.

### Q4 — hard — 4 marks

**Q4** [4 marks]

The database `CYCLE_HIRE` has two tables with the following definitions.

`BICYCLE(BicycleID, Model, DatePurchased, Electric)`

`HIRE(HireID, BicycleID, MemberID, StartTime)`

`BicycleID` is the primary key of `BICYCLE`. `HireID` is the primary key of `HIRE`.

(i) The table `HIRE` needs a new field, `EndTime`, to store the time at which each hire ended.

Write a Structured Query Language (SQL) script to change the definition of the table `HIRE` to add this field.

[2]

(ii) The field `BicycleID` in `HIRE` needs to be set up as a foreign key that links to `BicycleID` in `BICYCLE`.

Write an SQL script to change the definition of the table `HIRE` to add this foreign key.

[2]

### Q5 — medium — 4 marks

**Q5** [4 marks]

The database `CYCLE_HIRE` stores data about a public bicycle hire scheme.

Part of the table `BICYCLE` is shown with some sample data.

| BicycleID | Model | DatePurchased | Electric |
|---|---|---|---|
| BC0001 | Cityline 3 | 14/03/2024 | FALSE |
| BC0002 | Cityline 3 | 14/03/2024 | FALSE |
| BC0003 | Voltas E | 19/09/2025 | TRUE |
| BC0004 | Cityline 5 | 22/01/2026 | FALSE |

`BicycleID` is the primary key of `BICYCLE`. Every `BicycleID` value is exactly six characters long.

The database only supports these data types:

- character
- varchar
- Boolean
- integer
- real
- date
- time

Write a Structured Query Language (SQL) script to define the table `BICYCLE`.

### Q6 — easy — 1 marks

**Q6** [1 mark]

A city transport authority is setting up a new relational database to store data about its public bicycle hire scheme. The database will be called `CYCLE_HIRE`.

Write a Structured Query Language (SQL) script to create the database.

### Q7 — hard — 4 marks

**Q7** [4 marks]

A music school uses a relational database called `MUSIC_SCHOOL`. The database has two tables with the following definitions.

`STUDENT(StudentID, FirstName, LastName, Grade)`

`LESSON(LessonID, StudentID, LessonDate, Instrument)`

A student wants to return the number of lessons that have been taken by the student with the last name Silva.

The student writes the following Structured Query Language (SQL) script.

The script does not work.

Identify the four errors in the script.

### Q8 — medium — 3 marks

**Q8** [3 marks]

A library uses a relational database called `LIBRARY`. The database has the table `BOOK`, which has the following definition.

`BOOK(BookID, Title, Author, YearPublished, OnLoan)`

`OnLoan` is a Boolean field. It stores `TRUE` when the book is out on loan and `FALSE` when the book is on the shelf.

(i) The book with the ID `B1044` has been returned to the library.

Write a Structured Query Language (SQL) script to change the value of `OnLoan` for this book to `FALSE`.

[2]

(ii) The book with the ID `B1043` has been damaged and is no longer in the library.

Write an SQL script to remove the record for this book from the table `BOOK`.

[1]

### Q9 — easy — 2 marks

**Q9** [2 marks]

A company stores its data in a relational database. The database management system (DBMS) uses Structured Query Language (SQL).

SQL has two parts.

(i) State the name of the part of SQL that the DBMS uses to create and change the structure of a database.

[1]

(ii) State the name of the part of SQL that the DBMS uses to add, change and query the data that is stored in a database.

[1]

### Q10 — medium — 4 marks

**Q10** [4 marks]

Write the Structured Query Language (SQL) script to return the total number of courses that have started after 9 September 2023.

The value returned must have an appropriate field name.

*Source: November 2023 9618/13 Q3BII*


### Q11 — medium — 5 marks

**Q11** [5 marks]

(i) Write a Structured Query Language (SQL) script to define the database called `SHOP`.

[1]

(ii) Write the SQL script to return the total quantity of items that the customer with the ID of HJ231 has ordered.

[4]

*Source: November 2023 9618/11 Q3CI,CII*


### Q12 — medium — 8 marks

**Q12** [4 marks]

Sample data for the table `PERFORMANCE` is shown:

| **PerformanceID** | **ShowID** | **ShowDate** | **StartTime** |
|---|---|---|---|
| `0001` | `MK12` | `5/5/2025` | `13:00` |
| `0002` | `MK12` | `5/5/2025` | `19:30` |
| `0003` | `MK12` | `6/5/2025` | `19:00` |
| `0004` | `OP3` | `7/5/2025` | `18:30` |
| `0005` | `OP3` | `8/5/2025` | `18:30` |
| `0006` | `OP3` | `9/5/2025` | `13:00` |

Write a Structured Query Language (SQL) script to define the table `PERFORMANCE`.

*Source: June 2024 9618/13 Q4B*


**Q12** [4 marks]

Write an SQL script to return the number of times each show is scheduled. For example, in the sample data in part **(a)**, the show MK12 is scheduled three times.

The result needs to include the show name and a suitable field name for the number of times it is scheduled.

*Source: June 2024 9618/13 Q4C*


### Q13 — medium — 5 marks

**Q13** [3 marks]

Sample data for the table EXAM is shown:

| **ExamID** | **Subject** | **Level** | **TotalMarks** |
|---|---|---|---|
| `00956124` | `Computer Science` | `2` | `75` |
| `00956125` | `Computer Science` | `3` | `120` |
| `00956126` | `Mathematics` | `2` | `100` |
| `00956127` | `Mathematics` | `3` | `150` |
| `00956128` | `Physics` | `2` | `70` |
| `00956129` | `Physics` | `3` | `80` |

Write a Structured Query Language (SQL) script to define the table `EXAM`.

*Source: June 2024 9618/12 Q4B*


**Q13** [2 marks]

The table `EXAM_QUESTION` has been created but the foreign key has not been linked.

Write an SQL script to update `EXAM_QUESTION` and link the foreign key to `EXAM`.

*Source: June 2024 9618/12 Q4C*


### Q14 — medium — 5 marks

**Q14** [5 marks]

The company has another database, `FARMING`, for a different game.

The database `FARMING` has a table named `EVENT `which is shown with some sample data.

| **PlayerID** | **EventID** | **Category** | **Points** |
|---|---|---|---|
| `000123` | `3` | `Build` | `100` |
| `000124` | `1` | `Grow` | `36` |
| `000123` | `4` | `Grow` | `22` |
| `000123` | `7` | `Create` | `158` |
| `000125` | `3` | `Grow` | `85` |
| `000125` | `4` | `Build` | `69` |

(i) The database` FARMING` has a second table created named `PLAYER `that has the primary key `PlayerID`.

The field `PlayerID` in `EVENT` needs to be set up as a foreign key to link to `PlayerID` in `PLAYER`.

Write a Structured Query Language (SQL) script to change the table definition for EVENT to link the foreign key to `PLAYER`.

[2]

(ii) Write an SQL script to return the number of events that each player has completed.

[3]

*Source: June 2024 9618/11 Q6CI,CII*


### Q15 — medium — 8 marks

**Q15** [3 marks]

Write an SQL script to return the total quantity of ice cream sold to the customer with the ID of 0034E in the year 2023.

*Source: November 2024 9618/13 Q4B*


**Q15** [5 marks]

The table definition for `BATCH` is repeated here:

`BATCH(BatchID, Type, Flavour, Size, SellingPrice, EndDate) `

Sample data for the table `BATCH` is given:

| **BatchID** | **Type** | **Flavour** | **Size** | **SellingPrice** | **EndDate** |
|---|---|---|---|---|---|
| KlV12 | Plain | Vanilla | 1 | 2.20 | 12/12/2024 |
| RlC14 | Plain | Chocolate | 0.5 | 1.80 | 12/12/2024 |
| TYL1 | Non-dairy | Lemon | 0.5 | 2.10 | 01/02/2025 |
| FYV2 | Non-dairy | Vanilla | 0.25 | 1.50 | 02/02/2025 |
| BIV13 | Plain | Vanilla | 1 | 2.20 | 02/02/2024 |

Write an SQL script to define the table `BATCH`.

Include constraints (restrictions) on the data that can be entered into each field where appropriate.

*Source: November 2024 9618/13 Q4CI*


### Q16 — medium — 3 marks

**Q16** [3 marks]

The database also has the table `INVOICE` that stores data about each invoice that is sent to a customer.

Example data from the table `INVOICE` is given.

| **InvoiceID** | **DateSent** | **Amount** | **Paid** | **JobID** |
|---|---|---|---|---|
| 29262 | 12/12/2023 | 105.20 | Y | 221 |
| 26765 | 11/11/2023 | 200.00 | Y | 315 |
| 13290 | 02/01/2024 | 50.00 | Y | 315 |
| 34090 | 05/02/2024 | 25.95 | N | 569 |

Write a Structured Query Language (SQL) script to return the total amount of all the invoices sent in the year 2023 that have been paid.

*Source: November 2024 9618/12 Q6B*


### Q17 — medium — 8 marks

**Q17** [8 marks]

The table shows sample data for the table REPAIR_PART.

| **PartID** | **RepairNumber** | **Quantity** |
|---|---|---|
| ACD128SA | 0022 | 3 |
| PPOR543DWW | 0022 | 1 |
| TR453 | 0023 | 1 |
| PPOR543DWW | 0023 | 2 |
| WED5 | 0024 | 5 |

Write a Structured Query Language (SQL) script to define the table REPAIR_PART.

Include constraints (restrictions) on the data that can be entered into each field where appropriate.

[5]

(iii) Suppliers send invoices to the company for the parts that are used. A new table, INVOICE, stores the data about each invoice and whether it has been paid or not.

The design for the table INVOICE is shown:

INVOICE(<u>InvoiceID</u>, SupplierID, AmountDue, Paid, DatePaid)

The table shows sample data for the table INVOICE.

| InvoiceID | SupplierID | AmountDue | Paid | DatePaid |
|---|---|---|---|---|
| 000001 | JK675 | 22.50 | TRUE | 01/01/2024 |
| 000002 | WR443 | 358.99 | FALSE |   |
| 000003 | JK675 | 10.21 | FALSE |   |

Write an SQL script to return the total amount due to the supplier with the ID of JK675 for all the invoices that have **not** currently been paid.

*Source: November 2024 9618/11 Q2BII,BIII*

