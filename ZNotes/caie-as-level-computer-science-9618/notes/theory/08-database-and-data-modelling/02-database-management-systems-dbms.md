## Database Management Systems (DBMS)

- **Database:** collection of non-redundant interrelated data

- **DBMS:** Software programs that allow databases to be defined, constructed and manipulated

**Features of a DBMS:**

- **Data management:** data stored in relational databases - tables stored in secondary storage

- **Data dictionary** contains:

  - List of all files in database

  - No. of records in each file

  - Names & types of each field

- **Data modeling:** analysis of data objects used in database, identifying relationships among them

- **Logical schema:** overall view of entire database, includes entities, attributes and relationships

- **Data integrity:** entire block copied to user’s area when being changed, saved back when done

- **Data security:** handles password allocation and verification, backups database automatically, controls what certain user’s view by access rights of individuals or groups of users

**Data change clash solutions:**

- Open entire database in **exclusive mode** – impractical with several users

- **Lock all records** in the table being modified – one user changing a table, others can only read table

- **Lock record** currently being edited – as someone changes something, others can only read record

- User specifies **no locks** – software warns user of simultaneous change, resolve manually

- Deadlock**:** 2 locks at the same time, DBMS must recognize, 1 user must abort task

**Tools in a DBMS:**

- **Developer interface:** allows creating and manipulating database in SQL rather than graphically

- **Query processor:** handles high-level queries. It parses, validates, optimizes, and compiles or interprets a query which results in the query plan.