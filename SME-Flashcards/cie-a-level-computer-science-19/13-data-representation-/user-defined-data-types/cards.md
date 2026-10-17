# User-defined Data Types

Course: cie-a-level-computer-science-19 · Section: 13. Data Representation

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/13-data-representation-/user-defined-data-types/


## Card 1 — keyword_definition (`fl_H2sXdrzsHt6GH9Cv`)

**FRONT**

Define **user-defined data type**.


**BACK**

A user-defined data type is a **custom data type created by the programmer**, built from existing types to match the specific needs of a program.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 2 — question_and_answer (`fl_TKBwx3dPmCs5D5zC`)

**FRONT**

Name three things user-defined types let you do.


**BACK**

Group **related data** under a single identifier, restrict a variable to a **fixed set of valid values**, and build **dynamic data structures** such as linked lists.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 3 — keyword_definition (`fl_gNq2Kw7tg7pXj9TN`)

**FRONT**

Define **non-composite data type**.


**BACK**

A non-composite data type is a type defined **without referencing another data type**.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 4 — keyword_definition (`fl_sfGQgN4fz2xWDNsr`)

**FRONT**

Define **composite data type**.


**BACK**

A composite data type is one that **references other data types** in its definition, grouped under a single identifier.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 5 — question_and_answer (`fl_CvCYfTgcHXbbNhvS`)

**FRONT**

What decides whether a type is composite or non-composite?


**BACK**

Whether the type **references other data types**, not whether it holds one value or many.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 6 — question_and_answer (`fl_sc8rJsRcfKDvWNMd`)

**FRONT**

Name the two non-composite user-defined types.


**BACK**

**Enumerated** and **pointer**.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 7 — keyword_definition (`fl_6vZYvpJB67TR2wrD`)

**FRONT**

Define **enumerated data type**.


**BACK**

An enumerated data type is a non-composite, user-defined type consisting of a list of **all possible values** the variable can take.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 8 — true_or_false (`fl_nFF34hHXWxqmtJbp`)

**FRONT**

**True or False?**

The values of an enumerated type are unordered.


**BACK**

**False.**

The values are **ordered**, with an implied sequence based on the order they are declared, so comparisons work.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 9 — question_and_answer (`fl_FCyzq8jTZM9bXTWG`)

**FRONT**

Why does the order of values matter in an enumerated type?


**BACK**

The values are **ordered** by the sequence in which they are declared, so **comparisons work**, for example Monday comes before Tuesday.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 10 — question_and_answer (`fl_KqW9X9zWmCK4hrsq`)

**FRONT**

What is the pseudocode syntax for an enumerated type?


**BACK**

`TYPE <identifier> = (value1, value2, value3, ...)`


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 11 — keyword_definition (`fl_hgr2hzPvXggGZ8Rf`)

**FRONT**

Define **pointer data type**.


**BACK**

A pointer is a non-composite, user-defined type that **stores a memory address only**, rather than the data itself.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 12 — question_and_answer (`fl_49YYNSvnrzJ2H4nG`)

**FRONT**

What does a pointer definition also indicate?


**BACK**

The **type of data stored at that memory location**.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 13 — question_and_answer (`fl_B9MpDMZz4FwHw9hK`)

**FRONT**

What is the pseudocode syntax for a pointer type?


**BACK**

`TYPE <identifier> = ^<data type>`


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 14 — fill_in_the_blanks (`fl_ThKZHTP9ZnyCZJwg`)

**FRONT**

In pseudocode, the symbol <u>**        **</u> shows that a type is a pointer.


**BACK**

In pseudocode, the symbol **^** shows that a type is a pointer.


*Blanks: 1 — answers: []*

Spec links: `spcpt_fmFd4vgJtVWcghDF`

Flags: blank_answer_mismatch


## Card 15 — question_and_answer (`fl_2JWZWtJbqtrGBSps`)

**FRONT**

What are pointers used to build?


**BACK**

**Dynamic data structures** such as linked lists.


Spec links: `spcpt_fmFd4vgJtVWcghDF`


## Card 16 — question_and_answer (`fl_vTMrw872BYtZ364H`)

**FRONT**

Name the three composite user-defined types.


**BACK**

**Record**, **set** and **class**.


Spec links: `spcpt_WsRKgbbSqqhzvS93`


## Card 17 — keyword_definition (`fl_cp37tTZPQvgfbnrW`)

**FRONT**

Define **record** as a composite type.


**BACK**

A record is a composite type that groups a **fixed number of related items (fields)**, which may be of **different data types**, into a single new type.


Spec links: `spcpt_WsRKgbbSqqhzvS93`


## Card 18 — fill_in_the_blanks (`fl_Y5RQQTYSZ9CYGMvr`)

**FRONT**

A record groups a <u>**          **</u> number of related fields under one identifier.


**BACK**

A record groups a **fixed** number of related fields under one identifier.


*Blanks: 1 — answers: []*

Spec links: `spcpt_WsRKgbbSqqhzvS93`

Flags: blank_answer_mismatch


## Card 19 — question_and_answer (`fl_Yp4ttFHQ3ScQBRGM`)

**FRONT**

How do you access a field of a record?


**BACK**

Using **dot notation**, written as `RecordName.FieldName`.


Spec links: `spcpt_WsRKgbbSqqhzvS93`


## Card 20 — keyword_definition (`fl_ntYb2YBM8kQPj4sV`)

**FRONT**

Define **set**.


**BACK**

A set is a composite type holding a list of **unordered elements**, where all elements must be of the **same data type**.


Spec links: `spcpt_WsRKgbbSqqhzvS93`


## Card 21 — true_or_false (`fl_rD7wcKBHPNkqVfnS`)

**FRONT**

**True or False?**

A set can hold elements of different data types.


**BACK**

**False.**

**All elements must be of the same data type**, and the set definition includes the data type it uses.


Spec links: `spcpt_WsRKgbbSqqhzvS93`


## Card 22 — question_and_answer (`fl_3rz2mJFQKjckcHRf`)

**FRONT**

Which operations can be applied to a set?


**BACK**

**Set theory operations** such as **union** and **intersection**.


Spec links: `spcpt_WsRKgbbSqqhzvS93`


## Card 23 — question_and_answer (`fl_zGmcTtnyzN7k2pSx`)

**FRONT**

What is the pseudocode syntax for declaring a set type?


**BACK**

`TYPE <identifier> = SET OF <data type>`


Spec links: `spcpt_WsRKgbbSqqhzvS93`


## Card 24 — question_and_answer (`fl_9R924z5msxRNpkM3`)

**FRONT**

Which keyword tests whether a value is in a set?


**BACK**

`ISIN`


Spec links: `spcpt_WsRKgbbSqqhzvS93`


## Card 25 — keyword_definition (`fl_j82TmJrZ4YnNXsYX`)

**FRONT**

Define **class** as a composite type.


**BACK**

A class is a composite type that groups together both **data (attributes)** and the **methods** that operate on that data, under a single identifier.


Spec links: `spcpt_WsRKgbbSqqhzvS93`


## Card 26 — question_and_answer (`fl_N3DMcm62dQnGSfSM`)

**FRONT**

What is a class used as?


**BACK**

A **template to create objects** in object-oriented programming.


Spec links: `spcpt_WsRKgbbSqqhzvS93`


## Card 27 — question_and_answer (`fl_3y96qzxG2hrffjsw`)

**FRONT**

Which user-defined type suits data that can only be one of a fixed, named list of values?


**BACK**

An **enumerated type**.


Spec links: `spcpt_WsRKgbbSqqhzvS93`


## Card 28 — question_and_answer (`fl_VZRYGG4xCzNzdxz8`)

**FRONT**

Which user-defined type suits an unordered collection with no duplicates?


**BACK**

A **set**.


Spec links: `spcpt_WsRKgbbSqqhzvS93`

