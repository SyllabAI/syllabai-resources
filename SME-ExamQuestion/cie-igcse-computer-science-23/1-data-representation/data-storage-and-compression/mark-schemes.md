# Mark Schemes — Data Storage & Compression
**1. Data Representation** · Cambridge (CIE) IGCSE computer-science (0478 & 0984)


## Exam Questions (8 questions)


### Q1
The total number of bytes in a kibibyte are:

- 1024 **[1 mark]**

### Q2
The differences between a MB and  MIB include:

Any **two **of the following:

- A megabyte (MB) is a decimal unit of data storage **[1 mark]**
- … based on powers of 10 **[1 mark]**
- … equivalent to 1,000,000 bytes / 1000 kilobytes **[1 mark]**
- A mebibyte (MiB) is a binary unit of data storage **[1 mark]**
- … based on powers of 2 **[1 mark]**
- … equivalent to 1,048,576 bytes (2^20) / 1024 kibibytes **[1 mark]**

> **[exam-tip]**
> The command word is 'explain', so quoting numbers alone won't gain full credit — you need to make the underlying distinction clear
> 
> Quote storage in bytes (not bits) and get the exact figures right rather than rounding or approximating
The number of kibibytes in 3 gibibytes is:

- 3,145,728 KiB **[1 mark]**
- Correct working* ***[1 mark]**

  - *3 GiB = 3×1024 MiB *
  - *= 3×1024 × 1024 KiB*
  - *= 3 × 1,048,576 KiB * **OR**
  - *3 x 1024 x 1024*

### Q3
Lossless compression would compress the file by:

Any **five **of the following:

- A (compression) algorithm is used **[1 mark]**
- No data is removed in the process **OR **original file can be restored **[1 mark]**
- Repeated words/symbols (are identified) **OR **Patterns in the data (are identified) **[1 mark]**
- … and are indexed/put into a table **OR** by example **[1 mark]**
- … and are replaced with their index **OR**  by example **[1 mark]**
- … and their positions are stored (in the table) **OR** by example **[1 mark]**
- … and the number of times the word/pattern appears is stored (in the table) **OR** by example **[1 mark]**

> **[exam-tip]**
> - An example of a five mark response could be:
> 
> *Lossless compression works by using an algorithm that identifies repeated patterns in the data, such as the repeated colours in the list. These patterns are then indexed and stored in a table. For example, the word "red" might be replaced with the number "1" in the file, "green" with "2", and so on. The original positions and the number of times each colour appears are also stored in the table. This way, the file is compressed without losing any data, and the original file can be fully restored when needed.*
> 
> Describe the dictionary method here, not run-length encoding — the colours are scattered rather than consecutive.
> 
> For a 5-mark 'explain', use a worked example of the actual data to show each step clearly rather than vague 'grouping' language.

### Q4
The size of the file is:

- 30 000 bytes **[1 mark]**

*Working*

- $100\times150$
- $15000\times16OR15000\times2$
- * *$240000/8$

> **[mark-scheme]**
> - Two marks for **two** correct stages of working

### Q5
The term byte means:

Any **one** of the following:

- Unit of data/memory **[1 mark]**
- 8 bits **[1 mark]**
- Used to represent a character **[1 mark]**

### Q6
The type of compression that has been used is:

- Lossy compression **[1 mark]**

### Q7
|   | **Tick (✓) ** |
|---|---|
| Lossy compressed file | **✓** |
| Lossless compressed file |   |
| **Not **a compressed file |   |

### Q8
**Final answer:** **The correct answer is C**

- **C** is correct as less storage space is a benefit of compression **[1 mark]**
- **A, B **and** D **are incorrect as they are not benefits of compression
Methods of compression that could be used are:

- lossy **[1 mark]**
- lossless **[1 mark]**
