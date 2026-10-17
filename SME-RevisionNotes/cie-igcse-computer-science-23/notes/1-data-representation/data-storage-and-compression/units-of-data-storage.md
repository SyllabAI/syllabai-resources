---
note_id: "rn_8PPzSsp8NQczNxCC"
title: "Units of Data Storage"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/1-data-representation/data-storage-and-compression/units-of-data-storage
path: 1-data-representation/data-storage-and-compression/units-of-data-storage
updated_at: "2025-12-16T09:51:11.592Z"
spec_point_ids: ["spcpt_PpBvnfFP4Ms9PQZZ"]
spec_point_codes: []
guided_study: false
---

# Units of Data Storage

## Units of Data Storage

> **Spec point** — `spcpt_PpBvnfFP4Ms9PQZZ` · 1 Understand how data storage is measured

## Units of Data Storage

### What are units of data storage?

- A unit of data is a **term **given to describe** different amounts of binary digits** stored on a digital device
- These are the units you need to know for IGCSE:

| **Unit** | **Symbol** | **Value** |
|---|---|---|
| **Bit** | b | 1 or 0 |
| **Nibble** |   | 4 b |
| **Byte** | B | 8 b |
| **Kibibyte** | KiB | 1,024 B (2<sup>10</sup>) |
| **Mebibyte** | MiB | 1,024 KiB (2<sup>20</sup>) |
| **Gibibyte** | GiB | 1.024 MiB (2<sup>30</sup>) |
| **Tebibyte** | TiB | 1,024 GiB (2<sup>40</sup>) |
| **Pebibyte** | PiB | 1,024 TiB (2<sup>50</sup>) |
| **Exbibyte** | EiB | 1,024 PiB (2<sup>60</sup>) |

#### Megabyte vs Mebibyte

- 1 kibibyte (**1KiB**) = 1024 bytes (**1024 B**) - binary prefixes (to the **power of 2**)
- 1 kilobyte (**1KB**) = 1000 bytes (**1000 B**) - decimal prefixes (to the **power of 10**)

### Converting between units

- It is often a requirement of the exam to be able to **convert between different units **of data, for example bytes to mebibytes (larger) or kibibytes to bytes (smaller)
- This process involves **division**, **moving up in size** of unit and **multiplication**, **moving down in size** of unit
- When dealing with all units **bigger than a byte** we use multiples of **1024 **(2<sup>10</sup>)
- For example, 2000 kibibytes in mebibytes would be 2000 / 1024 = **1.95 MiB** and 2 tebibytes in gibibytes would be 2 * 1024 = **2048 GiB**
- When dealing with** bits and bytes** the same process is used with the value **8 **as there are 8 bits in a byte
- For example, 24 bits in bytes would be 24 / 8 =** 3 B** and 10 bytes in bits would be 10 * 8 = **80 b**
- The same multiply or divide by **1024** rule applies when converting beyond **TiB** to **PiB** and **EiB**

|   | **Unit** |   |
|---|---|---|
| **Multiply by 8 ⇑** | Bit | **Divide by 8 ⇓** |
| Byte |   |   |
| **Multiply by 1024 ⇑** | Kibibyte | **Divide by 1024 ⇓** |
| Mebibyte |   |   |
| Gibibyte |   |   |
| Tebibyte |   |   |
| Pebibyte |   |   |
| Exbibyte |   |   |

> **Worked Example**
> Convert **1 PiB** to **GiB**
> 
> **[2]**
> 
> **Answer**
> 
> - 1 PiB = 1024 TiB
> - 1 TiB = 1024 GiB
> 
> So:
> 
> - 1 PiB = 1024 × 1024 GiB **[1 mark]**
> - 1 PiB = **1,048,576 GiB ****[1 mark]**
