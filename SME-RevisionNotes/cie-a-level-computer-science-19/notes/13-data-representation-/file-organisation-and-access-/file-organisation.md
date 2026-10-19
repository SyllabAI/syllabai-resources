---
note_id: "rn_wxHq8dNrgZCjVFdR"
title: "File Organisation"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/13-data-representation-/file-organisation-and-access-/file-organisation
path: 13-data-representation-/file-organisation-and-access-/file-organisation
updated_at: "2026-07-02T08:43:30.855Z"
spec_point_ids: ["spcpt_t3kQPYdsm3nhhMHb"]
spec_point_codes: []
guided_study: false
---

# File Organisation

### What is file organisation?

- Files store data **permanently** on secondary storage as a **collection of records**, where each record represents one item (a customer, a transaction, a product)
- **File organisation** is the way those records are **arranged within the file**
- The method chosen affects how quickly records can be **searched, added, updated and deleted**, so it is picked to suit the task

#### Choosing a method

- There are three organisation methods you need: **serial**, **sequential** and **random**
- The organisation you choose also decides which **access methods** are possible (see [File Access](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/13-data-representation-/file-organisation-and-access-/file-access/))

## File organisation methods

> **Spec point** — `spcpt_t3kQPYdsm3nhhMHb`

## File organisation methods

### Serial file organisation

- Records are stored **one after the other, in the order they arrive** (chronological order, no sorting)
- New records are **appended to the end of the file**
- Simple to implement, but slow to search because there is no order to exploit

| **Best for** | **Example** |
|---|---|
| Unsorted or temporary **transaction files**<br><br>**data logging** files | Logging sensor readings as they arrive |

### Sequential file organisation

- Records are stored in **sorted order, based on a key field**
- To **update** the file, a **new version of the file has to be created** (records cannot easily be inserted in place)
- More efficient to search than serial, because a search can stop once the key is passed

| Best for | **Example** |
|---|---|
| Files **read often but rarely updated** | Payroll files, exam results ordered by candidate number |

### Random (direct) file organisation

- Records are stored in **no particular order**; there is **no sequencing** in where a record is placed
- There is a **relationship between the record's key and its location**: a **hashing algorithm** is applied to the key to work out the address
- **Updates can be carried out directly**, without rewriting the file

| **Best for** | **Example** |
|---|---|
| **Fast, real-time access** to individual records | Bank account lookup, live stock updates |

### Summary

| Method | How records are stored | Updating |
|---|---|---|
| **Serial** | Order of arrival, appended to the end | Append to end |
| **Sequential** | Sorted by key field | Create a new version of the file |
| **Random** | Location set by a hashing algorithm on the key | Direct |

> **Exam Hint**
> - For **serial**, both "records stored in the order they arrive" **and** "new records are appended to the end" are separate mark points. Give both.
> - Do not confuse **organisation** (how records are arranged) with **access** (how records are read). A question can ask about either, so keep the two ideas separate in your answer.
