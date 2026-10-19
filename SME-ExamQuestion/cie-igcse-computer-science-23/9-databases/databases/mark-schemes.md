# Mark Schemes — Databases
**9. Databases** · Cambridge (CIE) IGCSE computer-science (0478 & 0984)


## Exam Questions (14 questions)


### Q1
The field that would be suitable as  primary key is:

- **None **of the fields are likely to contain **unique **data **[1 mark]**

### Q2
Two types of validation that could be used on the `ProductCode `field are:

- Format check **[1 mark]**
- Length check **[1 mark]**

This is because:

Any **one **of the following:

- important to maintain consistency **[1 mark]**
- ensure correct data entry **[1 mark]**
- avoid errors in processing orders **[1 mark]**

### Q3
The most appropriate data types are:

`StudentID`** (integer) ****[1 mark]**

- **… **is a unique number assigned to each student and does not require decimal places **[1 mark]**

> *Accept alphanumeric / text / string for StudentID if justified by IDs containing both letters and numbers, or that no calculations are performed on the ID*

`ExamScore `**(real) ****[1 mark]**

- … exam scores may include decimal values e.g. 85.5% **[1 mark]**

`PassedExam`** (boolean) ****[1 mark]**

- **… **represents a true/false condition, e.g. it only needs to store two possible values: true (passed) or false (failed) **[1 mark]**

> **[exam-tip]**
> Name a specific data type for each field and then justify it — describing only what the field stores earns no marks
> 
> Remember a field that stores only two possibilities is boolean, and any value that could include decimals needs a real type

### Q4
The primary key fields would be:

**Customers Table:**

- `CustomerID `**[1 mark]**
- … unique for each customer and ensures that each customer record can be individually identified **[1 mark]**

**Orders Table:**

- `OrderID `**[1 mark]**
- … uniquely identifies each order and ensures that each order record is distinct **[1 mark]**
You would use the `CustomerID` field as:

- A foreign key **[1 mark]**
- … creates a link between `Orders` and `Customers`, allowing each order to be associated with the corresponding customer **[1 mark]**

> **[exam-tip]**
> Use precise technical terms — vague descriptions rarely earn the mark here
> 
> Explain how the field links the two tables, not just what it is used for

### Q5
The most appropriate field for a format check is:

- Email **[1 mark]**
- To ensure it contains an '@' symbol **[1 mark]**
The most appropriate field for a type check  is:

- StudentID **[1 mark]**
- To ensure that user does not enter text or symbols (only integers allowed) **[1 mark]**

### Q6
A field is described as:

- one piece of information relating to one person, item, or object **[1 mark]**
- e.g., "A field in a student database could be 'FirstName' which stores students' first names." **[1 mark]**

### Q7
Examples of validation checks that could be performed include:

Any **two **of the following:

- length check **[1 mark]**
- type check **[1 mark]**
- presence check **[1 mark]**
- format check **[1 mark]**

### Q8
The most appropriate field for the primary key is:

- `SongNumber `**[1 mark]**
| **Field** | **Data type** |
|---|---|
| `SongNumber` | Text/Alphanumeric |
| `Title` | Text/Alphanumeric |
| `Recorded` | Date/time |
| `Minutes` | Real |

> **[mark-scheme]**
> - **One **mark for every **two **correct data types

### Q9
The name of the field that is most suitable is:

- `TVCode `**[1 mark]**

This is because:

- Each entry in this field is a unique identifier **[1 mark]**
| **Field** | **Data type** |
|---|---|
| `TVCode` | **Text** |
| `ScreenSize` | **Integer** |
| `SmartTV` | **Boolean** |
| `Price\$` | **Real** |

> **[mark-scheme]**
> - **Two **marks for four correct answers
> - **One **mark for two or three correct answers

### Q10
The reason why the field is not required is:

- the field `Uses `already shows this information **OR** duplication of data **OR** redundant data **[1 mark]**

### Q11
The number of fields in the database is:

- 8 **[1 mark]**
The factor that must be true for a field to be a primary key is:

- must be unique/different for each record in the table **[1 mark]**

### Q12
The number of fields and records in the database is:

***Fields***:

- 5 **[1 mark]**

***Records****:*

- 8 **[1 mark]**

### Q13
The name of the field that would be used for the primary key is:

- `CatNo `**[1 mark]**
The reason for choosing the field is:

- it is a unique identifier **[1 mark]**

### Q14
The number of records in the database is:

- 20 **[1 mark]**
