# Mark Schemes — Database Management Systems (DBMS)
**8. Databases** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (7 questions)


### Q1
Anika uses the developer interface. **[1]**

The developer interface is the tool that allows a user to create items such as tables, forms and reports, which is exactly what Anika needs in order to add the new table and build the data entry screen. **[1]**

Ben uses the query processor. **[1]**

Ben does not need to change the structure of the database. He enters the criteria, in this case the month March, and the query processor finds and returns the orders that match. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for Anika uses the developer interface
> 
> **1 mark** for a reason linked to building the database, for example it allows the user to create tables, forms and reports // it is the tool used to create or change the structure of the database
> 
> **1 mark** for Ben uses the query processor
> 
> **1 mark** for a reason linked to retrieving data, for example the user enters the criteria and the tool returns the records that match // it processes and executes the query without changing the structure of the database
> 
> Accept the two members of staff in either order, provided each reason is clearly attached to the person it belongs to.
> 
> Do not accept "the developer interface, because Anika is a developer". The reason must say what the tool does, not repeat the person's job title.
> 
> Do not award a reason mark where the tool named for that person is the wrong one. The reason has to justify the tool that was actually named.

> **[exam-tip]**
> Half the marks in a question shaped like this sit in the reasons, and students routinely name both tools correctly and then stop writing. Add a second sentence for each person that says what the tool does for them.
> 
> The clue that separates the two tools is whether the structure of the database is changing. Anika is changing it, so she needs the developer interface. Ben is only reading data that is already stored, so he needs the query processor.

### Q2
The member of staff can create a new table and define the fields that the table will hold. **[1]**

The member of staff can create a form, so that other staff can type in the details of a booking without working directly on the table. **[1]**

The member of staff can create a report, which presents selected data from the database in a chosen layout, for example a list of all bookings for one month. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - Create a table and define the fields it will hold
> - Change an existing table definition, for example by adding a field
> - Create a form that other users use to enter or edit data
> - Create a report that presents or prints selected data in a chosen layout
> - Create and save a query that other users can run
> 
> **[3 marks]**
> 
> Accept "design" or "set up" for "create".
> 
> Do not accept "type in the details of a booking". Entering data through a finished form is using the database, not using the developer interface.
> 
> Do not accept "search for a customer" or "run a query". Running a search is the query processor.
> 
> Do not accept two answers that are the same task in different words, for example "create a form" and "make a data entry screen". Award one mark only.

> **[exam-tip]**
> Notice the words "the use and purpose of" in this part of the syllabus. Naming the tool is not enough here, because the question already names it. Each of your three answers has to be a task, so it needs a verb: create a table, create a form, create a report.
> 
> A very common lost mark is describing what an ordinary user does with the finished database. The developer interface is used to build the tables, forms and reports; it is not used to fill them in.

### Q3
The query processor allows the user to enter the criteria for a search, or to write a query in Structured Query Language (SQL). **[1]**

It then processes the query, finds the data that matches the criteria and returns the result to the user. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the user enters the criteria for a search // the user writes a query, for example in SQL
> 
> **1 mark** for the query processor processes or executes the query and returns the matching data // it finds and returns the appropriate result
> 
> Accept "runs", "carries out" or "executes" for "processes".
> 
> Accept "searches the database and displays the records that match".
> 
> Do not accept "it stores the queries" or "it stores data about the database". That is the data dictionary.
> 
> Do not accept "it allows the user to create tables, forms and reports". That is the developer interface.

> **[exam-tip]**
> The two software tools in a DBMS get swapped in a great many answers. The query processor finds data that is already in the database. The developer interface creates the things that hold and present that data. If your answer contains the word "create", check that you have not described the wrong tool.
> 
> Two marks means two ideas, not one idea written twice. The user supplies the criteria is the first idea; the tool returns the matching records is the second.

### Q4
The logical schema is the design of the whole database. It sets out the tables, the fields in each table and how the tables link together. **[1]**

The logical schema is not tied to one particular DBMS, so the same design can be built using whichever DBMS each of the six countries runs. **[1]**

The design can be checked, and any errors put right, before any data is stored or any programs are written. Correcting a design on paper is far cheaper than correcting a database that is already in use. **[1]**

The logical schema is then used to design the physical structure, so the developers have one agreed design to build from. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - The logical schema is the conceptual design, or overall design, of the database
> - It sets out the tables, the fields in each table and how the tables are linked
> - It is independent of any particular DBMS or platform
> - ... so the same design can be implemented on whichever DBMS a country uses
> - The design can be checked and corrected before any data is entered
> - Changing the design later, once data is stored and programs have been written, costs far more
> - It is used to design the physical structure of the database
> - It gives every developer one agreed design to work from
> 
> **[4 marks]**
> 
> Accept "views" as an example of something the logical schema defines.
> 
> Do not accept "it holds data about the data" or "it holds the field names and data types". That describes the data dictionary, which is a different DBMS feature.
> 
> Do not accept a description of how the data is stored on the disk, or which file organisation is used. The logical schema deliberately leaves the physical storage out.
> 
> Do not accept "so the database works faster". The logical schema is a design document and has no direct effect on performance.

> **[exam-tip]**
> Data dictionary and logical schema are the two DBMS features that students most often mix up, and an answer that describes the wrong one scores nothing. Hold on to the difference: the logical schema is the design of the structure, the data dictionary is the record of what is in that structure once it exists.
> 
> The word "logical" is doing real work in the name. It means the design says what the database contains and how the parts relate, and says nothing about how the data is physically stored. Any answer that mentions disks, files or storage devices has drifted away from the mark scheme.

### Q5
| Number | Item of data the data dictionary stores about the field FamilyName |
|---|---|
| 1 | **The name of the field** **[1]** |
| 2 | **The data type of the field** **[1]** |
| 3 | **The validation rule applied to the field** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - The name of the field
> - The data type of the field
> - The size, or maximum length, of the field
> - The validation rule applied to the field
> - Whether the field is a primary key, a foreign key or an indexed field
> - The name of the table that the field belongs to
> - A description of what the field holds
> 
> **[3 marks]**
> 
> Accept a correctly named example alongside an item, for example "data type: text of up to 30 characters".
> 
> Do not accept the data values themselves, such as "Okonkwo" or "Haddad". A data dictionary stores data about the data, never the data.
> 
> Do not accept the same item written twice in different words, for example "field size" and "maximum number of characters". Award one mark only.
> 
> Do not accept "metadata" on its own. It is the correct heading for all of these items, but the question asks for three specific items.

> **[exam-tip]**
> The commonest mistake here is to write down the contents of the table instead of the description of the table. The data dictionary does not know that one student is called Okonkwo. It knows that there is a field called FamilyName, that it holds text, and how long that text may be.
> 
> A quick test before you write an answer: could the data dictionary hold this item before a single student had been added to the database? If it could, it belongs in your answer.

### Q6
The DBMS carries out backup procedures, so a copy of the data is kept and the database can be restored if data is lost or damaged. **[1]**

The DBMS gives access rights to individual users or to groups of users, so a user can only see or change the data that user is allowed to. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for backup procedures // the DBMS takes backup copies of the data // the database can be restored from a backup
> 
> **1 mark** for access rights given to individuals or to groups of users // different users are given different levels of access, for example read-only or read and write
> 
> Accept "permissions" or "privileges" for access rights.
> 
> Accept "recovery" only where it is linked to a backup copy, for example "the data can be recovered from the backup".
> 
> Accept views, where the answer says that different users are shown different parts of the database. This is credited in the published mark scheme for this content even though the syllabus does not name it.
> 
> Accept encryption, where the answer says the stored data is encoded so it cannot be understood without the key.
> 
> Do not accept "a password" on its own. A password identifies the user; it is the access rights attached to that user that then control what the user may do.
> 
> Do not accept "a firewall" or "anti-virus software". Both protect the computer system rather than the data held in the database, and neither is provided by the DBMS.

> **[exam-tip]**
> Students often answer this with general computer security points such as firewalls, anti-virus software or strong passwords. The question is about what the DBMS itself provides, so answer with the things the DBMS controls: backups, access rights, and the views each user is shown.
> 
> Make sure your access rights point says what the rights actually do. "The DBMS has access rights" simply repeats the question. "Each group of users is given read-only or read and write access" earns the mark.

### Q7
> **[mark-scheme]**
> **1 mark **each to **max 2** for data dictionary and **max 2** for logical schema:
> 
> Data dictionary:
> 
> - Data about the data in the database // metadata
> - Identifies the characteristics of the data that will be stored
> - Appropriate example e.g. field names, table name, validation rules, data types, primary / foreign keys, relationships etc.
> 
> Logical schema:
> 
> - Conceptual design
> - Platform/database independent overview of the database
> - Is used to design the physical structure
> - Appropriate example e.g. Design of entities / E-R diagram / views
