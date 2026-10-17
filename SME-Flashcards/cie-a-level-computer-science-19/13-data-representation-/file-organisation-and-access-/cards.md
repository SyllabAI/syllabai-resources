# File Organisation & Access

Course: cie-a-level-computer-science-19 · Section: 13. Data Representation

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/13-data-representation-/file-organisation-and-access-/


## Card 1 — keyword_definition (`fl_ZY2nZzBNtRjXGHvZ`)

**FRONT**

Define **file organisation**.


**BACK**

File organisation is the way **records are arranged within a file**.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 2 — question_and_answer (`fl_2jz9Sf348wT3DJBc`)

**FRONT**

What does a file store, and how?


**BACK**

It stores data **permanently on secondary storage** as a **collection of records**, where each record represents one item such as a customer, transaction or product.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 3 — question_and_answer (`fl_kt5JF8cP7DxyRkTR`)

**FRONT**

Why does the choice of file organisation matter?


**BACK**

It affects how quickly records can be **searched, added, updated and deleted**, so it is chosen to suit the task.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 4 — true_or_false (`fl_Dnf5ZV4Ch7b4Vh7Y`)

**FRONT**

**True or False?**

File organisation and file access mean the same thing.


**BACK**

**False.**

**Organisation** is how records are **arranged** in the file. **Access** is how records are **read** from it.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 5 — question_and_answer (`fl_47RVY3ddNcDvc6HF`)

**FRONT**

Name the three file organisation methods.


**BACK**

**Serial**, **sequential** and **random**.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 6 — keyword_definition (`fl_FRzRmTRhXZ5xKSmN`)

**FRONT**

Define **serial file organisation**.


**BACK**

Records are stored **one after the other in the order they arrive**, in chronological order with no sorting.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 7 — fill_in_the_blanks (`fl_cVkyXGrGG3CRbDc5`)

**FRONT**

In a serial file, records are stored in <u>**                          **</u> order.


**BACK**

In a serial file, records are stored in **chronological** order.


*Blanks: 1 — answers: []*

Spec links: `spcpt_t3kQPYdsm3nhhMHb`

Flags: blank_answer_mismatch


## Card 8 — question_and_answer (`fl_sVnPpcRX7tp6HgJZ`)

**FRONT**

Where are new records added in a serial file?


**BACK**

They are **appended to the end of the file**.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 9 — question_and_answer (`fl_qZDn9H7VzMSXstkZ`)

**FRONT**

Give one drawback of serial file organisation.


**BACK**

It is **slow to search**, because there is **no order to exploit**.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 10 — question_and_answer (`fl_6mkJWFqYfs3KqdpT`)

**FRONT**

What is serial organisation best for?


**BACK**

**Unsorted or temporary transaction files** and **data logging files**, for example logging sensor readings as they arrive.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 11 — keyword_definition (`fl_ZxMPpx6GQbShJG3Y`)

**FRONT**

Define **sequential file organisation**.


**BACK**

Records are stored in **sorted order, based on a key field**.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 12 — question_and_answer (`fl_786h7qkmVQ5HRK8k`)

**FRONT**

How is a sequential file updated?


**BACK**

A **new version of the file has to be created**, because records cannot easily be inserted in place.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 13 — true_or_false (`fl_6f4n33BcWWcX4ZRX`)

**FRONT**

**True or False?**

A sequential file can be updated in place without rewriting it.


**BACK**

**False.**

A **new version of the file** must be created. It is a **random** file that can be updated directly.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 14 — question_and_answer (`fl_CcTfGyvkg7dMH9PV`)

**FRONT**

Why is a sequential file more efficient to search than a serial file?


**BACK**

A search can **stop once the key is passed**.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 15 — question_and_answer (`fl_vmcNynyh9FkpBHm4`)

**FRONT**

What is sequential organisation best for?


**BACK**

Files that are **read often but rarely updated**, such as payroll files or exam results ordered by candidate number.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 16 — keyword_definition (`fl_kmvHm7Dy5vBkrJy6`)

**FRONT**

Define **random file organisation**.


**BACK**

Records are stored in **no particular order**, with a **hashing algorithm applied to the key** to work out the address.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 17 — fill_in_the_blanks (`fl_7QJJSbrrMFPvHBCj`)

**FRONT**

In a random file there is a relationship between the record's key and its <u>**                **</u>.


**BACK**

In a random file there is a relationship between the record's key and its **location**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_t3kQPYdsm3nhhMHb`

Flags: blank_answer_mismatch


## Card 18 — question_and_answer (`fl_H8yYBHp5DrjbvFfG`)

**FRONT**

How are random files updated?


**BACK**

**Directly**, without rewriting the file.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 19 — question_and_answer (`fl_NvWq46xCxQZMqwNn`)

**FRONT**

What is random organisation best for?


**BACK**

**Fast, real-time access to individual records**, such as bank account lookup or live stock updates.


Spec links: `spcpt_t3kQPYdsm3nhhMHb`


## Card 20 — keyword_definition (`fl_TNznFqMzJ4PZ5QbD`)

**FRONT**

Define **file access method**.


**BACK**

A file access method is **how records are read from or located in** a file, once the file has been organised.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 21 — question_and_answer (`fl_9CwNrBDHZnZ97G7v`)

**FRONT**

What determines which access methods are available?


**BACK**

The **file organisation** used.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 22 — question_and_answer (`fl_c6Q8GJzX6N6TRHfp`)

**FRONT**

Which access methods work on a serial file?


**BACK**

**Sequential access only**. Direct access is not possible on a serial file.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 23 — question_and_answer (`fl_6VtbRDNXJXpvNbxr`)

**FRONT**

Which access methods work on a sequential file?


**BACK**

**Both sequential access and direct access**, with direct access using an **index**.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 24 — question_and_answer (`fl_N4ht6FMYW3CfnWmw`)

**FRONT**

Which access methods work on a random file?


**BACK**

**Direct access only**, using **hashing**. Sequential access is not possible on a random file.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 25 — true_or_false (`fl_RjdBGvDHqfPQRK9H`)

**FRONT**

**True or False?**

Direct access is possible on a serial file.


**BACK**

**False.**

A serial file supports **sequential access only**.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 26 — keyword_definition (`fl_xDrKmmhrwMXXv5db`)

**FRONT**

Define **sequential access**.


**BACK**

Sequential access reads records **one after the other**, starting at the **physical start of the file**, and continues until the record is found or the end of the file is reached.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 27 — fill_in_the_blanks (`fl_KRDVdbZHJMHN6cf9`)

**FRONT**

Sequential access starts at the <u>**                **</u> start of the file.


**BACK**

Sequential access starts at the **physical** start of the file.


*Blanks: 1 — answers: []*

Spec links: `spcpt_Bd5rpm2XnqkVD5KP`

Flags: blank_answer_mismatch


## Card 28 — question_and_answer (`fl_VPMknrwTmZ4YcqQY`)

**FRONT**

How does sequential access work on a serial file?


**BACK**

Records are in **chronological order**, so **every record is checked** until the target is found or all records have been checked.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 29 — question_and_answer (`fl_txJQYkq45wDwpj2t`)

**FRONT**

How does sequential access work on a sequential file?


**BACK**

Records are in order of a **key field or index**, and it is the **key field that is compared**.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 30 — question_and_answer (`fl_vN7ZMVHzqfYzV7wP`)

**FRONT**

Why can sequential access stop early on a sequential file?


**BACK**

As soon as the current record's key is **greater than the target key**, the target **cannot be present**.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 31 — true_or_false (`fl_C69vXRPH3fhNWKhy`)

**FRONT**

**True or False?**

Sequential access and sequential organisation are the same thing.


**BACK**

**False.**

They are different. **Serial files also use sequential access**.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 32 — keyword_definition (`fl_WmfsFQR5GmdycMps`)

**FRONT**

Define **direct access**.


**BACK**

Direct access locates a **specific record without reading the records before it**, using the **key field** of the record.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 33 — question_and_answer (`fl_f9Pb8XMpg49Pvvdq`)

**FRONT**

How does direct access work on a random file?


**BACK**

A **hashing algorithm** is applied to the record's **key field** to **calculate the address** of the location where the record should be.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 34 — fill_in_the_blanks (`fl_8Q8Zh9PD4QpXX9sF`)

**FRONT**

On a random file, if the record is not at the hashed address then a <u>**                  **</u> has occurred.


**BACK**

On a random file, if the record is not at the hashed address then a **collision** has occurred.


*Blanks: 1 — answers: []*

Spec links: `spcpt_Bd5rpm2XnqkVD5KP`

Flags: blank_answer_mismatch


## Card 35 — question_and_answer (`fl_zRG3Nfj4fbCGkjJ3`)

**FRONT**

How does direct access work on a sequential file?


**BACK**

An **index of all key fields** is kept. The **index is searched** for the address of the record, which is then read directly.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 36 — question_and_answer (`fl_MMbqD4pkSknvSfv9`)

**FRONT**

What is the key difference between direct access on a random file and on a sequential file?


**BACK**

A **random** file uses a **hashing algorithm**. A **sequential** file uses an **index**.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 37 — question_and_answer (`fl_rsGT4SgK8r4pBCxh`)

**FRONT**

Give an example of direct access in use.


**BACK**

**Accessing a bank account record by account number**.


Spec links: `spcpt_Bd5rpm2XnqkVD5KP`


## Card 38 — keyword_definition (`fl_4KZ5b9Cmxmd8Srqn`)

**FRONT**

Define **hashing algorithm**.


**BACK**

A hashing algorithm is a **mathematical formula applied to the key field of a record**, whose result gives the **address** where that record should be stored or found.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 39 — true_or_false (`fl_M9cWYjt3PXMPvRcx`)

**FRONT**

**True or False?**

A hashing algorithm scrambles the data in a record.


**BACK**

**False.**

A hashing algorithm is a **mathematical formula applied to the key field**, and its result is an **address**. It does not scramble the record's data.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 40 — fill_in_the_blanks (`fl_B7HX9XvDMp5w3shG`)

**FRONT**

Hashing gives <u>**        **</u> access to a record without searching through the file one record at a time.


**BACK**

Hashing gives **fast** access to a record without searching through the file one record at a time.


*Blanks: 1 — answers: []*

Spec links: `spcpt_XWPwvhWzsWwv4jKN`

Flags: blank_answer_mismatch


## Card 41 — question_and_answer (`fl_tdVK644MgrpmMpq4`)

**FRONT**

How is a record written using hashing?


**BACK**

**Calculate the address from the key**, then store the record at that address.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 42 — question_and_answer (`fl_tjbDSmZzNdhHdt6W`)

**FRONT**

How is a record read using hashing?


**BACK**

**Calculate the address from the same key**, then read the record from that address.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 43 — question_and_answer (`fl_wT35z5Rtfw9mGTfY`)

**FRONT**

Name the two types of hashing algorithm.


**BACK**

**Modulo division** and **folding**.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 44 — keyword_definition (`fl_D88TgtJRrw2rZwH8`)

**FRONT**

Define **modulo division** hashing.


**BACK**

The address is calculated as `Key MOD TableSize`, which is the most common hashing method.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 45 — fill_in_the_blanks (`fl_sxYR6qyfsGFh9Drs`)

**FRONT**

In hashing, `MOD` gives the <u>**                    **</u> after division.


**BACK**

In hashing, `MOD` gives the **remainder** after division.


*Blanks: 1 — answers: []*

Spec links: `spcpt_XWPwvhWzsWwv4jKN`

Flags: blank_answer_mismatch


## Card 46 — question_and_answer (`fl_Yfkb3DrpY86vVxGT`)

**FRONT**

Why does modulo division always give a valid address?


**BACK**

The remainder is always in the range **0 to TableSize minus 1**.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 47 — keyword_definition (`fl_nSK2SykTQYJpXwpX`)

**FRONT**

Define **folding**.


**BACK**

The key is **split into equal parts**, the parts are **added together**, and usually `MOD TableSize` is applied to the total.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 48 — question_and_answer (`fl_ttz4GVJyv45G3GQp`)

**FRONT**

A random file has 100 locations, addressed 0 to 99.

Where is the record with key 45217 stored under modulo division?


**BACK**

`45217 MOD 100 = 17`, so the record is stored at **address 17**.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 49 — question_and_answer (`fl_2T4hX9thJ33wMMdB`)

**FRONT**

A record with key 88317 is added to the same 100-location file.

What happens?


**BACK**

`88317 MOD 100 = 17`, which is the **same address** as key 45217, so a **collision** occurs.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 50 — keyword_definition (`fl_4btSc3C3twhfftXm`)

**FRONT**

Define **collision** in hashing.


**BACK**

A collision is when **two keys hash to the same address**.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 51 — true_or_false (`fl_88CQw88KVBHWt6z8`)

**FRONT**

**True or False?**

When two keys hash to the same address, the second record is discarded.


**BACK**

**False.**

A **collision resolution** method is used, such as **linear probing**, an **overflow area**, or **chaining**.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 52 — question_and_answer (`fl_TN5jtFYfR4dhVVB8`)

**FRONT**

Name the three collision resolution methods.


**BACK**

**Linear probing**, an **overflow area**, and **chaining**.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 53 — keyword_definition (`fl_mH2XMHKb8fcgGx8W`)

**FRONT**

Define **linear probing**.


**BACK**

Start at the hashed address and move through the following locations **in a linear fashion**, storing the record in the **first free location**.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 54 — question_and_answer (`fl_Qt3b5sMK3TrsMFbC`)

**FRONT**

Key 88317 collides at address 17.

Using linear probing, where is the record stored?


**BACK**

In the **next free location, address 18**.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 55 — question_and_answer (`fl_RxjcDcj4rQCB9fRp`)

**FRONT**

How does an overflow area resolve a collision?


**BACK**

A **separate overflow area** is set up, and the record is stored in the **next free space there**.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 56 — keyword_definition (`fl_3b7zrV5yyg5vSMmD`)

**FRONT**

Define **chaining**.


**BACK**

Each location holds a reference to a **list, or chain, of records** that hashed to it, and the new record is added to that chain.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`


## Card 57 — question_and_answer (`fl_Mz6WbnK4VXmVWqfy`)

**FRONT**

Why is it not enough to name a collision resolution method in an exam?


**BACK**

You must also **describe how it resolves the collision**, for example 'linear probing, store in the next free location'.


Spec links: `spcpt_XWPwvhWzsWwv4jKN`

