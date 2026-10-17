---
note_id: "rn_jY8JBHJvJcFj4w5k"
title: "Hashing"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/13-data-representation-/file-organisation-and-access-/hashing
path: 13-data-representation-/file-organisation-and-access-/hashing
updated_at: "2026-10-01T12:36:22.373Z"
spec_point_ids: ["spcpt_XWPwvhWzsWwv4jKN"]
spec_point_codes: []
guided_study: false
---

# Hashing

### What is a hashing algorithm?

- A hashing algorithm is a **mathematical formula** applied to the **key field** of a record
- The **result of the calculation gives the address** where that record should be **stored or found**
- It is used in **direct access** on **random and sequential** files, giving **fast access** to a record without searching through the file one record at a time

## Hashing algorithms

> **Spec point** — `spcpt_XWPwvhWzsWwv4jKN`

## Hashing algorithms

### How does hashing work?

- The **record key** (e.g. a `StudentID` or account number) is passed through the hashing algorithm to produce a **hash value**, which is the address:

  - `Address ← HashFunction(Key)`
- **Writing** a record: calculate the address from the key, then store the record there
- **Reading** a record: calculate the address from the same key, then read the record from there

### Types of hashing algorithm

| Method | How it works |
|---|---|
| **Modulo division** | The record key is divided by the number of storage locations and the **remainder** is the address, e.g. `Address ← Key MOD 100` for a file with 100 locations, giving addresses 0 to 99 |

### Handling collisions

| Method | How it resolves the collision |
|---|---|
| ** Linear probing** | Start at the hashed address and move through the following locations **in a linear fashion**, storing the record in the **first free location** |
| **Overflow area** | A separate **overflow area** is set up; the record is stored in the next free space there |

> **Exam Hint**
> - When defining a hashing algorithm, use the exam's own words: a **mathematical formula / calculation applied to the key field** whose result is the **address**. "It scrambles the data" scores nothing.
> - For collision resolution, name a method **and** describe it: "linear probing, store in the next free location" earns more than "linear probing" alone.
> - Hashing questions almost always ask you to **describe** the algorithm and **handle collisions**, not to invent a hash function. Spend your revision there.

> **Worked Example**
> A random file has **100** storage locations, addressed 0 to 99. Records use a numeric key.
> 
> Show how the modulo division method stores the records with keys **45217** and **88317**.
> 
> **Answer**
> 
> - `45217 MOD 100 = 17`, so the record with key 45217 is stored at **address 17**
> - `88317 MOD 100 = 17`, so this record hashes to the **same address**, a **collision**
> - Using linear probing, it is stored in the **next free location, address 18**
