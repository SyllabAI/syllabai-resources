# Exam Questions — Create a Database Structure
**10. Databases** · Cambridge (CIE) IGCSE ict (0417 & 0983)
> Source: [https://www.savemyexams.com/igcse/ict/cie/21/topic-questions/](https://www.savemyexams.com/igcse/ict/cie/21/topic-questions/) · 11 questions across 1 sets


## Exam Questions (11 questions)


### Q1 — medium — 4 marks

**Q1** [4 marks]

A new patient is attending a medical centre. He completes a form with his details and gives this to the secretary who enters the details into a database.

**Describe **the characteristics of primary keys and foreign keys.

*Source: June 2024 0417/11 Q13D(II)*


### Q2 — medium — 4 marks

**Q2** [4 marks]

An organisation has provided laptops for its sales team to use when working at home and in the office.

The network manager of the organisation has been asked to record the details of the employees who have been provided with laptops. The network manager has decided to produce an online data capture form.

**Describe **the main design features that should be considered to make the online data capture form easy to complete accurately.

*Source: June 2024 0417/11 Q7C*


### Q3 — hard — 7 marks

**Q3** [7 marks]

Petr has set up a database for a science project on planets in the solar system. Part of the database is shown.

| `ID` | `Name_of_planet` | `Number_of_moons` | `Orbital_period` | `Rings` | `Gravity` | `Type_of_planet` | `First_observed` |
|---|---|---|---|---|---|---|---|
| 4 | Mars | 2 | 1.88 | N | 0.38 | Regular | 1610 |
| 5 | Ceres | 0 | 4.61 | N | 0.27 | Dwarf | 1801 |
| 7 | Saturn | 62 | 29 | Y | 1.16 | Gas Giant | 1610 |
| 9 | Neptune | 14 | 165 | Y | 1.21 | Gas Giant | 1846 |
| 10 | Pluto | 5 | 248 | N | 0.62 | Dwarf | 1930 |
| 11 | Haumea | 1 | 309 | N | 0.401 | Dwarf | 2004 |

Operators such as AND, OR, NOT, LIKE, >, >=, <, <=, =, <> can be used to search Petr’s planet database. The search criteria for all the gas giant planets with more than 20 moons would look like this:

`Type_of_planet = "Gas Giant" AND Number_of_moons > 20`

**Write **down the search criteria that will produce a list of planets that are not gas giants but have at least one moon and were first observed after 1800.

*Source: June 21 0417/12 Q5B*


### Q4 — hard — 8 marks

**Q4** [8 marks]

Two types of database are relational and flat file.

**Compare **and **contrast **relational databases and flat file databases.

Your answer **must **include similarities and differences.

*Source: June 2022 0417/11 Q*


### Q5 — medium — 6 marks

**Q5** [4 marks]

Petr has set up a database for a science project on planets in the solar system. Part of the database is shown.

| `ID` | `Name_of_planet` | `Number_of_moons` | `Orbital_period` | `Rings` | `Gravity` | `Type_of_planet` | `First_observed` |
|---|---|---|---|---|---|---|---|
| 4 | Mars | 2 | 1.88 | N | 0.38 | Regular | 1610 |
| 5 | Ceres | 0 | 4.61 | N | 0.27 | Dwarf | 1801 |
| 7 | Saturn | 62 | 29 | Y | 1.16 | Gas Giant | 1610 |
| 9 | Neptune | 14 | 165 | Y | 1.21 | Gas Giant | 1846 |
| 10 | Pluto | 5 | 248 | N | 0.62 | Dwarf | 1930 |
| 11 | Haumea | 1 | 309 | N | 0.401 | Dwarf | 2004 |

When Petr was designing his database, he had to set the data types for each field.

**Complete **the design table below by filling in the data types for each named field. Use the most appropriate data type.

Each data type **must **be different. For any numeric field, specify the type of number.

| Field name | Data type |
|---|---|
| `Number_of_moons` |   |
| `Orbital_period` |   |
| `Rings` |   |
| `Name_of_planet` |   |

*Source: June 2021 0417/12 Q5A*


**Q5** [2 marks]

**Write **down the names of the planets that are not gas giants but have at least one moon and were first observed after 1800.

*Source: June 2021 0417/12 Q5C*


### Q6 — medium — 11 marks

**Q6** [3 marks]

A systems analyst has created a new computer system to keep records in a medical centre. She has created a relational database to store the medical records of patients.

The database uses primary and foreign keys.

**Describe **what is meant by a relational database.

*Source: June 2021 0417/11 Q7A*


**Q6** [4 marks]

**Explain **the difference between a primary key and a foreign key.

*Source: June 2021 0417/11 Q7B*


**Q6** [4 marks]

A dentist works at the medical centre. The dentist stores the medical records of his patients

**Describe four **other uses of the database software that the dentist can use to help him in his work.

*Source: June 2021 0417/11 Q7C*


### Q7 — medium — 2 marks

**Q7** [2 marks]

A student is creating a spreadsheet of airports for a project.

![Spreadsheet listing airport codes, names, and countries. Includes London Heathrow, Rome, Paris, Milan, Shannon, Stockholm, Leeds and Bradford, and Geneva.](assets/001-spreadsheet-listing-airport-codes-names-and-coun.png)

The formula in G2 is:

=VLOOKUP(F2,A2:B9,2,0)

The completed file could have been created using a database.

**Describe two **reasons why databases are used in certain applications rather than spreadsheets.

*Source: June 2022 0417/12 Q9D*


### Q8 — medium — 2 marks

**Q8** [2 marks]

Two types of database are relational and flat file.

**Give**, using an example, **one **reason why flat file databases are used in certain applications rather than relational databases.

*Source: June 2022 0417/11 Q7B*


### Q9 — easy — 2 marks

**Q9** [1 mark]

A library system has two tables; one for borrowers and one for books. Extracts from these tables are shown.

| `Borrower_ID` | `Borrower_name` | `Contact_telephone` | `Contact_email` |
|---|---|---|---|
| 5404 | Susan Stranks | 01632 960321 | [rockit@cambridgeinternational.org](mailto:rockit@cambridgeinternational.org) |
| 9867 | Fei Hong Zhao | 07700 900222 | [tawara@cambridgeinternational.org](mailto:tawara@cambridgeinternational.org) |

**Borrowers table**

| `Book_ID` | `ISBN` | `Name_of_book` | `Author_of_book` | `Date_published` | `Borrower_ID` | `Date_due_back` |
|---|---|---|---|---|---|---|
| 1 | 0859550153 | Bird of Prey | David James | 1977 | 5404 | 27/10/2021 |
| 34 | 3301028345 | The Fifth Man | Colin Turner | 1998 | 9324 | 05/10/2021 |
| 35 | 4237681321 | A View of the Temple | Yu Yan Zhang | 2017 | 8854 | 07/10/2021 |
| 54 | 4237681321 | A View of the Temple | Yu Yan Zhang | 2017 | 5404 | 27/10/2021 |

**Books table**

For the `books` table, **name **the most appropriate field that could be used as a primary key

*Source: Nov 2021 0417/13 Q4B(I)*


**Q9** [1 mark]

The librarian has created a relationship between the `books` table and the `borrowers` table.

For the `books` table, **name **the most appropriate foreign key field that would be used to create the relationship.

*Source: Nov 2021 0417/13 Q4B(II)*


### Q10 — easy — 1 marks

**Q10** [1 mark]

The manager of a medical centre keeps the doctor’s stock records in a database. The stock for any item is not allowed to fall below 15 items and the manager keeps a maximum of 100 items in stock.

The table shows examples of the stock.

| `Name_of_item` | `Serial_number ` | `Number_in_stock` | `Name_of_supplier` | `Shelf_number` |
|---|---|---|---|---|
| Medihoney | 3081043612211 | 15 | Capimed | 0126 |
| Sodium fusidate | 1437210227870 | 60 | Brooks Medical | 0112 |
| Crepe bandage | 2541233164353 | 100 | Capimed | 0064 |
| Crepe bandage | 2834954736849 | 89 | Cams Meds | 0064 |

As data is entered it needs to be verified and validated.

**Name **the most appropriate field from the table that could be used as a primary key in the database.

*Source: June 2022 0417/11 Q14C*


### Q11 — easy — 1 marks

**Q11** [1 mark]

A book has an ISBN which is 330247204X

**Choose **the most appropriate data type for the ISBN.

*Source: June 2023 0417/11 Q1*

