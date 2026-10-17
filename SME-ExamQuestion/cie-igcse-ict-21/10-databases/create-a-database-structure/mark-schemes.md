# Mark Schemes — Create a Database Structure
**10. Databases** · Cambridge (CIE) IGCSE ict (0417 & 0983)


## Exam Questions (11 questions)


### Q1
Characteristics of primary keys include:

Max **three **of the following:

- A primary key is unique **[1 mark]**
- A primary key helps identify the record **[1 mark]**
- A primary key cannot be a null value **[1 mark]**
- Creates relationships **[1 mark]**
- Only one primary key per table **[1 mark]**

Characteristics of foreign keys include:

Max **three **of the following:

- A foreign key can have a null value **[1 mark]**
- A foreign key is a key in a table which is a primary key in another table **[1 mark]**
- A foreign key enforces referential integrity **[1 mark]**
- Found in relational databases **[1 mark]**

### Q2
Examples of the design features that should be considered include:

Any **four **of the following:

- Navigation buttons to move to next page **[1 mark]**
- Help button to get help with filling in the form **[1 mark]**
- Auto-complete to speed up the process to add addresses **[1 mark]**
- Character boxes to make it easier to type in the data **[1 mark]**
- Good use of white space to make it easier to read **[1 mark]**
- Layout of form to make it easier to read **[1 mark]**
- Easy to understand instructions to help fill out the form correctly **[1 mark]**
- Use of radio buttons/tick boxes for gender **[1 mark]**
- Font size to make it easier to read **[1 mark]**
- Font style so it is easier to read **[1 mark]**
- Well designed layout to make it easier to fill in **[1 mark]**

### Q3
The search criteria that will produce the desired output is:

`Type_of_planet<>"Gas Giant" AND Number_of_moons >=1`
` AND First_observed >1800`

- **Only **two **ANDs **correctly placed **[1 mark]**
- `Type_of_planet` **[1 mark]**
- `<> "Gas Giant"` **[1 mark]**
- `Number_of moons`* ***[1 mark]*** *
- `>=1`* ***[1 mark]**
- `Firstobserved`  **[1 mark]**
- `>1800` **[1 mark] **

### Q4
Both relational databases and flat file databases share some similarities. They **both use a primary key** to uniquely identify records, ensuring data integrity. Additionally, both types of databases **store data in records and fields** within a table format. Another similarity is that both can **create searches and reports**, allowing users to retrieve and present data efficiently.

However, there are several differences between them. A flat file database **consists of a single table**, whereas a relational database has **multiple linked tables** that can establish relationships between different datasets. Flat file databases are simpler in structure and typically stored as plain text files, whereas relational databases **use foreign keys** to link records across tables, making them more powerful and **reducing data duplication**. Additionally, relational databases **allow searches and reports to be created across multiple tables**, providing more efficient data management and retrieval.

Overall, while both database types store and manage data, relational databases offer greater flexibility, scalability, and efficiency due to their structured relationships and ability to prevent redundancy.

> **[mark-scheme]**
> Response includes at least four similarities and four differences, ensuring a balanced comparison.
> 
> - Both use a primary key **[1 mark]**
> - Both can create searches/reports **[1 mark]**
> - Both store data in records and fields in a table **[1 mark]**
> - Flat file uses one table **[1 mark]**
> - Relational database has linked tables/relationships **[1 mark]**
> - Relational database allows searches/reports to be created over multiple tables **[1 mark]**
> - Relational database reduces duplicate data **[1 mark]**
> - Relational database uses foreign keys **[1 mark]**
> 
> **[Total marks: 8/8]**

> **[exam-tip]**
> **Five **top tips for answering this 8-mark "compare and contrast" question effectively:
> 
> 1. **Include both similarities and differences**
> 
>   1. To achieve full marks, ensure you discuss at least four points from each category.
> 2. **Clearly state how relational databases are more advanced**
> 
>   1. Example: Instead of just saying "relational databases are more powerful," write "relational databases allow for cross-referencing between tables using foreign keys, making them more efficient and reducing data duplication."
> 3. **Explain why flat file databases are limited**
> 
>   1. Example: "Flat file databases use only one table, meaning searches and reports are limited to a single dataset, whereas relational databases can retrieve data from multiple linked tables."
> 4. **Use structured comparisons**
> 
>   1. Instead of listing points separately, directly compare them:
>   2. "Both store data in tables, but flat file databases use a single table, whereas relational databases use multiple linked tables."
> 5. **Avoid vague or repetitive points**
> 
>   1. Instead of "relational databases are better," explain why: "Relational databases reduce duplicate data by using foreign keys to link tables, improving data integrity and efficiency."

### Q5
| Field name | Data type |
|---|---|
| `Number_of_moons` | **Numeric: Integer ****[1 mark]** |
| `Orbital_period` | **Numeric: Decimal ****[1 mark]** |
| `Rings` | **Boolean ****[1 mark]** |
| `Name_of_planet` | **Text ****[1 mark]** |
The names of the planets that are not gas giants but have at least one moon and were first observed after 1800 are:

- Pluto **[1 mark]**
- Haumea **[1 mark]**

### Q6
A relational database can be described as:

Any **three **of the following:

- Contains more than one table **[1 mark]**
- Tables are linked **[1 mark]**
- It uses relationships **[1 mark]**
- Removes redundancy of data **[1 mark]**
- Saves storage space **[1 mark]**
Differences between a primary key and a foreign key include:

Any **four **of the following:

- Primary key holds unique data **[1 mark]**
- Primary key identifies the record **[1 mark]**
- Primary key can be automatically indexed **[1 mark]**
- Each table has one primary key whereas a table can contain a number of foreign keys **[1 mark]**
- Foreign key is used to link with the primary key of another table **[1 mark]**
Examples of other uses of the database include:

Any **four **of the following:

- Searches/queries can be used to search details of patients **[1 mark]**
- Reports can be created about treatment carried out **[1 mark]**
- Formulas can be created to calculate the cost of treatment **[1 mark]**
- Charts can be created showing missed appointments by patients **[1 mark]**
- Images are stored of the x-rays to identify the patient/determine treatment **[1 mark]**
- Mail merge appointments that have been missed **[1 mark]**
- Any other appropriate use plus explanation **[1 mark]**

### Q7
Reasons why databases are used in certain applications rather than spreadsheets include:

Any **two **of the following:

- A database can use queries **[1 mark]**
- A database can use relationships **[1 mark]**
- Referential integrity can be enforced in a database **[1 mark]**
- Easier to create forms on a database **[1 mark]**
- Easier to create reports on a database **[1 mark]**
- Better user security **[1 mark]**
- Data is easier to manage in a database **[1 mark]**

### Q8
Reasons why flat file databases are used in certain applications is:

Any **one **of the following:

- The data is in a list **[1 mark]**
- There is only a small amount of data **[1 mark]**
- A single table is to be used **[1 mark]**

Plus **one **mark for any valid example:

- Example of a list such as name, address/CSV files **[1 mark]**

### Q9
For the books table, the most appropriate field that could be used as a primary key is:

- `Book_ID `**[1 mark]**
The most appropriate field that could be used as a foreign key is:

- `Borrower_ID `**[1 mark]**

### Q10
The most appropriate field from the table that could be used as a primary key is:

- `Serial_number` **[1 mark]**

### Q11
**Final answer:** **The correct answer is B**

- The ISBN contains letter and numbers
- Text is the only data type that will handle both types of data

**A **is incorrect as a number/integer cannot contain letters

**C **is incorrect as Boolean can only be a True/False value

**D **is incorrect as  is can only handle dates in the date format (e.g. 10/02/25)
