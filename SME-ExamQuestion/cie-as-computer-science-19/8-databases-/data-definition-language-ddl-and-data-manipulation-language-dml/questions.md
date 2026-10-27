# Exam Questions — Data Definition Language (DDL) & Data Manipulation Language (DML)
**8. Databases** · Cambridge (CIE) AS computer-science (9618)
> Source: [https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/) · 8 questions across 1 sets


## Exam Questions (8 questions)


### Q1 — medium — 4 marks

**Q1** [4 marks]

Write the Structured Query Language (SQL) script to return the total number of courses that have started after 9 September 2023.

The value returned must have an appropriate field name.

*Source: November 2023 9618/13 Q3BII*


### Q2 — medium — 5 marks

**Q2** [5 marks]

(i) Write a Structured Query Language (SQL) script to define the database called `SHOP`.

[1]

(ii) Write the SQL script to return the total quantity of items that the customer with the ID of HJ231 has ordered.

[4]

*Source: November 2023 9618/11 Q3CI,CII*


### Q3 — medium — 8 marks

**Q3** [4 marks]

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


**Q3** [4 marks]

Write an SQL script to return the number of times each show is scheduled. For example, in the sample data in part **(b)**, the show MK12 is scheduled three times.

The result needs to include the show name and a suitable field name for the number of times it is scheduled.

*Source: June 2024 9618/13 Q4C*


### Q4 — medium — 5 marks

**Q4** [3 marks]

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


**Q4** [2 marks]

The table `EXAM_QUESTION` has been created but the foreign key has not been linked.

Write an SQL script to update `EXAM_QUESTION` and link the foreign key to `EXAM`.

*Source: June 2024 9618/12 Q4C*


### Q5 — medium — 5 marks

**Q5** [5 marks]

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


### Q6 — medium — 8 marks

**Q6** [3 marks]

Write an SQL script to return the total quantity of ice cream sold to the customer with the ID of 0034E in the year 2023.

*Source: November 2024 9618/13 Q4B*


**Q6** [5 marks]

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


### Q7 — medium — 3 marks

**Q7** [3 marks]

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


### Q8 — medium — 8 marks

**Q8** [8 marks]

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

