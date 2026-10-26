# Exam Questions — Data Integrity
**6. Security, Privacy & Data Integrity** · Cambridge (CIE) AS computer-science (9618)
> Source: [https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/) · 6 questions across 1 sets


## Exam Questions (6 questions)


### Q1 — medium — 4 marks

**Q1** [4 marks]

A class of students are developing a program to send data between computers. Many computers are connected together to form a wired network. Serial ports are used to connect one computer to another.

Each computer:

- is assigned a unique three-digit ID
- has three ports, each identified by an integer value
- is connected to between one and three other computers.

Messages are sent between computers as a string of characters organised into fields as shown:

`<STX><DestinationID><SourceID><Data><ETX>`

| **Field number** | Field name | Description |
|---|---|---|
| **n/a** | `STX` | a single character marking the start of the message (ASCII value 02) |
| **1** | `DestinationID` | three numeric characters that identify the destination computer |
| **2** | `SourceID` | three numeric characters that identify the source computer |
| **3** | `Data` | a variable length string containing the data being sent (Minimum length is 1 character) |
| **n/a** | `ETX` | a single character marking the end of the message (ASCII value 03) |

For example, the following message contains the data "Hello Kevin" being sent from computer "101" to computer "232":

`<STX>"232101Hello Kevin"<ETX>`

Each computer will run a copy of the same program. Each program will contain a global variable, `MyID` of type string, that contains the unique ID of the computer in which the program is running.

The programmer has defined the first two program modules as follows:

| **Module** | Description |
|---|---|
| `Transmit()` <br>(already written) | - takes two parameters:<br><br>  - a string containing a message<br>  - an integer containing a port number<br>- transmits the message using the given port |
| `SendFile()` | - takes three parameters:<br><br>  - a string containing a text file name<br>  - a string containing a Destination ID<br>  - an integer containing a Port number<br>- transmits the file one line at a time<br>- transmits a final message with data string "****" |

One of the text files to be sent contains several blank lines (lines that do not contain any text).

(i) Explain why this is a problem.

(2)

(ii) Explain how the message format could be changed to allow a blank line to be sent.

(2)

*Source: Nov 2023 9618/21 Q8C*


### Q2 — medium — 2 marks

**Q2** [2 marks]

Data verification is one method of protecting the integrity of data.

Describe **one **other method of protecting the integrity of data.

*Source: Nov 2023 9618/13 Q8A*


### Q3 — medium — 4 marks

**Q3** [4 marks]

An example of a tutor ID is NK16C6.

An administrative officer enters the tutor ID into the `TUTOR `table.

Explain how data verification can be used when the tutor ID is entered.

*Source: Nov 2023 9618/13 Q3C*


### Q4 — medium — 4 marks

**Q4** [4 marks]

Robots are used to serve food and drink to customers at a restaurant.

![A humanoid robot with shelves stands in a modern café, surrounded by tables and chairs, indicating a futuristic dining setting.](assets/001-a-humanoid-robot-with-shelves-stands-in-a-modern.png)

The data from the robots is transmitted to a central computer using a wireless connection.

Complete the table by identifying **and **describing **two **methods of data verification that can be used during data transfer.

|   | Method | Description |
|---|---|---|
| 1 |   |   |
| 2 |   |   |

*Source: June 2024 9618/13 Q7F(I)*


### Q5 — medium — 5 marks

**Q5** [5 marks]

A bank allows customers to access their accounts using an application that they can download onto a device such as a smartphone.

The bank wants to protect the integrity of its data while transferring the data to other banks. Parity check is one example of data verification.

Complete the description of parity check when Computer A is transmitting data to Computer B.

Computer A and Computer B agree on whether to use ............................... parity. Computer A divides the data into groups of ............................ . The number of 1s in each group is counted. If the agreed parity is ....................... and the group has an even number of 1s, a parity bit of 1 is appended, otherwise a parity bit of 0 is appended.

In a parity ............................ check the bytes are grouped together, for example in a grid. The number of 1s in each column (bit position) is counted. A bit is assigned to each column to make the column match the parity. These parity bits are transmitted with the data as a parity ................................. .

*Source: June 2024 9618/11 Q5B*


### Q6 — medium — 3 marks

**Q6** [3 marks]

A company makes ice cream and sells it to shops.

The ice cream is made in batches: a large quantity of one type and flavour of ice cream that is then split into smaller quantities for sale.

The company’s owner has designed a relational database, ICECREAM, to store data about their ice cream and customers.

Some of the tables in the database are given. The database is not normalised.

`BATCH(BatchID, Type, Flavour, Size, SellingPrice, EndDate) CUSTOMER(CustomerID, CompanyName, EmailAddress, TelephoneNumber) SALE(SaleID, BatchID, CustomerID, Quantity, Date)`

A Database Management System (DBMS) supports data integrity.

Explain how a DBMS supports data integrity.

*Source: Nov 2024 9618/13 Q4E*

