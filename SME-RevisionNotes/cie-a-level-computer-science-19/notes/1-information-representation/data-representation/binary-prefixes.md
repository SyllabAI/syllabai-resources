---
note_id: "rn_YyDhCsxv2Tk7fjQQ"
title: "Binary Prefixes"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/1-information-representation/data-representation/binary-prefixes
path: 1-information-representation/data-representation/binary-prefixes
updated_at: "2026-05-05T10:18:51.276Z"
spec_point_ids: ["spcpt_Bknjp9TZScRHGQKg"]
spec_point_codes: []
guided_study: false
---

# Binary Prefixes

## Binary prefixes

> **Spec point** — `spcpt_Bknjp9TZScRHGQKg`

## Binary prefixes

### What is a binary prefix?

- A binary prefix is a unit *prefix* used to **indicate multiples of bytes in binary**
- Consider the word **kilobyte**, "kilo" is the **prefix**
- The **byte **is the standard unit used for measuring data storage, so there needs to be a way of expressing bytes in larger multiples

#### Denary prefixes

- A common way of expressing multiples of bytes is to use denary prefixes:

| Denary unit | Equivalent size (bytes) |
|---|---|
| 1 kilobyte (1 KB) | 1000 |
| 1 megabyte (1 MB) | 1,000,000 |
| 1 gigabyte (1 GB) | 1,000,000,000 |
| 1 terabyte (1 TB) | 1,000,000,000,000 |
| 1 petabyte (1 PB) | 1,000,000,000,000,000 |

- This system relies on the assumption that **1 kilo = 1000**
- This assumption is based on the **denary (base 10)** number system

  - **E.g. a 1 GB hard drive can store 1 x 10**<sup>**9**</sup>** bytes**

#### Binary prefixes

- However, computers use the **binary (base 2)** number system so the denary system is technically inaccurate when describing storage
- To be precise, expressing multiples of bytes is done using binary prefixes:

| Binary unit | Number of bytes (base 2) | Equivalent size (base 10) |
|---|---|---|
| 1 kibibyte (1 KiB) | 2<sup>10</sup> | 1024 |
| 1 mebibyte (1 MiB) | 2<sup>20</sup> | 1,048,576 |
| 1 gibibyte (1 GiB) | 2<sup>30</sup> | 1,073,741,824 |
| 1 tebibyte (1 TiB) | 2<sup>40</sup> | 1,099,511,627,776 |
| 1 pebibyte (1 PiB) | 2<sup>50</sup> | 1,125,899,906,842,624 |

- Notice the prefixes change depending on the system being used, e.g. **kilo** (denary) vs **kibi **(binary)

#### Why does it matter?

- The importance of the system being used depends on how **precise **you need to be
- When precision is required (e.g. identifying RAM), binary prefixes should be used

  - **E.g. 16 GiB RAM can store 16 × 2³⁰ bytes (17,179,869,184 bytes)**
- When a rough **estimate **is acceptable (e.g. describing storage device capacity), denary prefixes are commonly used

  - **E.g. a 16 GB memory stick can store 16 × 10⁹ bytes (16,000,000,000 bytes)**
