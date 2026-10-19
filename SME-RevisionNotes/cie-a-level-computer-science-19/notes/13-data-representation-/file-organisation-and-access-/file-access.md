---
note_id: "rn_9ttsrrtY9bQ7pnVC"
title: "File Access"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/13-data-representation-/file-organisation-and-access-/file-access
path: 13-data-representation-/file-organisation-and-access-/file-access
updated_at: "2026-07-02T08:50:57.377Z"
spec_point_ids: ["spcpt_Bd5rpm2XnqkVD5KP"]
spec_point_codes: []
guided_study: false
---

# File Access

### What are file access methods?

- Once a file is organised, a **file access method** is how records are **read from or located in** it
- The access methods available depend on the **file organisation** used

### Which access method works with which organisation?

| File organisation | Sequential access | Direct access |
|---|---|---|
| Serial | Yes | No |
| Sequential | Yes | Yes (using an index) |
| Random | No | Yes (using hashing) |

- **Sequential access** works on **serial and sequential** files; **direct access** works on **sequential and random** files

> **Exam Hint**
> - This matrix is a common exam trap.
> - Learn it exactly.

## File access methods

> **Spec point** — `spcpt_Bd5rpm2XnqkVD5KP`

## File access methods

### Sequential access

- Sequential access reads records **one after the other**, starting at the **physical start of the file**, and continues **until the record is found or the end of the file is reached**

#### On serial files

- Records are in **chronological order**, so **every record is checked** until the target is found or all records have been checked

#### On sequential files

- Records are in order of a **key field (or index)**, and it is the **key field that is compared**
- Checking can **stop early**: as soon as the current record's key is **greater than the target key**, the target cannot be present
- **Example**: reading student results in candidate-number order

### Direct access

- Direct access locates a **specific record without reading the records before it**
- The target is found using the **key field of the record**

#### On random files

- A **hashing algorithm** is applied to the record's **key field** to **calculate the address** of the location where the record should be
- If the record is not at that location (a collision has occurred), a resolution method such as **linear probing** or an **overflow area** is used (see [Hashing](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/13-data-representation-/file-organisation-and-access-/hashing/))
- **Example**: accessing a bank account record by account number

#### On sequential files

- An **index of all key fields** is kept
- The **index is searched** for the address of the file location where the target record is stored, and the record is then read directly

> **Exam Hint**
> - Watch the direction of the pairing: **direct access on a sequential file uses an index**, but **direct access on a random file uses a hashing algorithm**. Questions often ask you to explain both in the same part.
> - "Sequential access" and "sequential organisation" are not the same thing. Serial files also use sequential access.
