# Mark Schemes — File Organisation & Access
**13. Data Representation** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (16 questions)


### Q1
**(i)**

9260 modulus 7 = 6, because 9260 = (7 x 1322) + 6, so the hashing algorithm gives address 6. **[1]**

Address 6 already holds the record with record key 6089, so a collision occurs and the new record is stored in the first free location in the overflow area. **[1]**

**(ii)**

7318 modulus 7 = 3, because 7318 = (7 x 1045) + 3, so the hashing algorithm gives address 3. **[1]**

The record key stored at address 3 is 8410, which does not match 7318, so the required record is not at that address. **[1]**

The overflow area is then searched, one record after another, until the record with record key 7318 is found. **[1]**

**[5 marks]**

> **[mark-scheme]**
> Part (i)
> 
> **1 mark** for a hash value or address of 6 for record key 9260
> 
> **1 mark** for stating that address 6 is already in use by record key 6089, so the new record is written to the overflow area
> 
> Part (ii)
> 
> **1 mark** for a hash value or address of 3 for record key 7318
> 
> **1 mark** for comparing the record key held at address 3 with 7318 and finding that 8410 does not match
> 
> **1 mark** for searching the overflow area one record after another until the matching record key is found
> 
> Accept storage location, storage space or memory location in place of address throughout.
> 
> Accept linearly, in a linear fashion, one at a time or in turn, in place of one record after another.
> 
> Do not accept that the new record is stored at address 0 in part (i). Every address in the main area is already in use, and this file resolves a collision by using the overflow area, not by returning to the start of the main area.
> 
> Do not accept that the new record replaces record key 6089. A record already in the file is not overwritten by a record with a different record key.
> 
> Do not accept that the record held at address 3 is returned as the answer in part (ii). The record key stored at that address must be compared with the record key being searched for before the record is accepted.

> **[exam-tip]**
> The comparison mark in part (ii) is the one you are most likely to lose. Calculating the hash value only tells you where to look first. The record found there may belong to a different record key, so the algorithm must compare the stored record key with the one being searched for before it accepts the record.
> 
> Read the stem to see which collision method this particular file uses. Here the stem states an overflow area, so an answer describing a search through the following addresses of the main area does not fit this file, and in this case there is no free address left in the main area anyway.

### Q2
| Record key | Hash value | Address where the record is stored |
|---|---|---|
| 3142 | 0 | 0 |
| 2081 | **1** | **1** |
| 5230 | **0** | **2** |
| 4207 | **3** | **3** |

2081: 2 + 0 + 8 + 1 = 11, and 11 modulus 5 = 1. Address 1 is free, so the record is stored at address 1. **[1]**

5230: 5 + 2 + 3 + 0 = 10, and 10 modulus 5 = 0. **[1]**

Address 0 already holds record key 3142, so a collision occurs. Address 1 already holds record key 2081, so the next free address is 2. **[1]**

4207: 4 + 2 + 0 + 7 = 13, and 13 modulus 5 = 3. Address 3 is free, so the record is stored at address 3. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for record key 2081 given a hash value of 1 and an address of 1
> 
> **1 mark** for record key 5230 given a hash value of 0
> 
> **1 mark** for record key 5230 given an address of 2
> 
> **1 mark** for record key 4207 given a hash value of 3 and an address of 3
> 
> Accept the digit sum shown as working alongside the hash value, for example 11 then 1.
> 
> Do not accept an address of 0 for record key 5230. Address 0 already holds record key 3142, and two records cannot occupy the same address.
> 
> Do not accept an address of 1 for record key 5230. Address 1 is not free either, because record key 2081 was stored there first, so the search continues to address 2.
> 
> Do not accept a hash value of 2 for record key 4207. That is 4207 modulus 5, which leaves out step 1 of the algorithm.
> 
> Do not accept 11, 10 or 13 as hash values. These are the digit sums before step 2 has been carried out, and they fall outside the address range 0 to 4.

> **[exam-tip]**
> Work down the table one record at a time and write each address in as you go. The order matters: record key 5230 only ends up at address 2 because 2081 was already placed at address 1. If you calculate all four hash values first, and fill in the addresses afterwards, it is easy to forget that an earlier record is now in the way.
> 
> Keep the two steps of the algorithm separate. Adding the digits and then taking modulus 5 gives a different answer from taking modulus 5 of the record key itself, and only the first is what this question asked for.

### Q3
| Record key | Hash value |
|---|---|
| 4021 | 3 |
| 5009 | **4** |
| 6134 | **2** |

5009 = (7 x 715) + 4, so 5009 modulus 7 = 4 **[1]**

6134 = (7 x 876) + 2, so 6134 modulus 7 = 2 **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the hash value of record key 5009 given as 4
> 
> **1 mark** for the hash value of record key 6134 given as 2
> 
> Accept the value shown inside the working, for example 5009 - 5005 = 4, provided the hash value itself is clear.
> 
> Do not accept 715 for 5009, or 876 for 6134. These are the whole-number results of the division. The hash value is the remainder that is left over, not the number of times 7 divides into the record key.
> 
> Do not accept any value of 7 or more. A hash value produced by modulus 7 can only be 0, 1, 2, 3, 4, 5 or 6.

> **[exam-tip]**
> Calculators are not allowed in this paper, so do the division by hand and keep the remainder. Find the largest multiple of 7 that is not greater than the record key, then subtract it: 7 x 715 = 5005, and 5009 - 5005 = 4.
> 
> The most common mistake here is writing down the answer to the division instead of the remainder. One quick check saves the mark every time: if your hash value is bigger than 6, you have not used modulus 7.

### Q4
**(i)** 4 records are read. **[1]**

**(ii)** 6 records are read. **[1]**

Sequential access reads the records one at a time from the physical start of the file and compares the key field of each record with 147. **[1]**

The sixth record read has the key field 156, which is greater than 147. Because the file is ordered on the key field, no record after this point can hold 147, so the search stops there. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for (i) 4
> 
> **1 mark** for (ii) 6
> 
> **1 mark** for records are read one at a time from the physical start of the file and each key field is compared with the target value
> 
> **1 mark** for once a key field greater than 147 is read the record cannot appear later, because the file is ordered on the key field
> 
> Accept for (i) a list of the four values read, 104, 118, 127, 133.
> 
> Accept for the final mark "156 is past 147 in the order, so 147 is not in the file".
> 
> Do not accept 8 for (ii). Reading every record is what sequential access does on a serial file, where the records are in no key order. This file is a sequential file.
> 
> Do not accept 7 for (ii). The search stops on the record that fails the test; it does not read a further record afterwards.

> **[exam-tip]**
> Almost every mark lost here is the same mistake: answering 8 because "sequential access checks every record". That is only true when there is no key order to rely on. On a sequential file the early stop is the whole point, and CIE marks it explicitly. Count the reads by hand rather than reasoning about them, and remember to include the record that triggers the stop.

### Q5
Direct access allows the one customer record that is needed to be read without any of the other records in the file being read. **[1]**

The address of the record is worked out from the key field, the customer number, using a hashing algorithm, so the record can be read as soon as the customer number is entered. **[1]**

Sequential access would instead read records one after the other from the physical start of the file, and with 400 000 records the response would be far too slow. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - Direct access finds the required record without reading the other records in the file
> - The address of the record is obtained from the key field / the customer number
> - A hashing algorithm is applied to the key field to give the address
> - Sequential access would read records one at a time from the physical start of the file
> - The records in a random file are stored in no particular order, so a sequential search would have to continue to the end of the file before the record could be reported as missing
> - With 400 000 records the number of records read would be very large, so the response would be too slow
> 
> **[3 marks]**
> 
> Accept "calculated from the customer number" for the address point.
> 
> Do not accept an answer that only says direct access is faster. The mark is for saying why: the other records are not read.
> 
> Do not accept "an index is used to find the address". An index is how direct access works on a sequential file. This file uses random organisation.

> **[exam-tip]**
> The most common loss of marks here is writing a general comparison of the two access methods instead of answering about this file. Tie every point to the scenario: one record is wanted, it is wanted straight away, and there are 400 000 of them. A second frequent error is to describe an index. Keep the two routes apart: direct access on a sequential file uses an index of key fields, direct access on a random file uses a hashing algorithm.

### Q6
| Method of file organisation | Method of file access |
|---|---|
| Serial | **Sequential access** **[1]** |
| Random | **Direct access** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for Serial: sequential access
> 
> **1 mark** for Random: direct access
> 
> Accept "sequential" and "direct" written on their own.
> 
> Do not accept direct access for a serial file. A serial file has no key field ordering and there is no way of working out where a record is stored, so a record can only be reached by reading the records in front of it.
> 
> Do not accept sequential access for a random file. The records are stored in no particular order, so reading them one after the other is not a way of finding a target record from its key.

> **[exam-tip]**
> Students lose this mark by matching the two words that look the same. "Sequential access" and "sequential organisation" are not the same thing, and a serial file is read using sequential access even though it is not a sequential file. Learn the pairing in the form the syllabus states it: sequential access for serial and sequential files, direct access for sequential and random files.

### Q7
In a sequential file the records must stay in order of the key field, so a record cannot simply be altered where it sits. **[1]**

Every amendment therefore means writing out a new version of the whole file, and with amendments arriving continuously the file would have to be rewritten again and again. **[1]**

In a file that uses random organisation the records are stored in no particular order. **[1]**

The position of each record is fixed by its own booking reference rather than by the records around it, so an amended record can be written back directly, in place, without rewriting the file. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Sequential organisation, any two from:**
> 
> - the records in the file are ordered
> - the order is based on the key field
> - a new version of the file has to be created to update the file, which is not practical when amendments are continuous
> 
> Maximum 2 marks for sequential organisation
> 
> **1 mark** for the random layout: the records are stored in no particular order // there is no sequencing in the placement of the records
> 
> **1 mark** for the consequence: the location of a record is determined by its record key, so updates can be carried out directly
> 
> Accept "a new master file has to be produced" for the new-version point.
> 
> Accept "a hashing algorithm is applied to the booking reference to give the record's location" for the final mark on random organisation.
> 
> Do not accept "sequential files are slow to search". That is a point about file access, not about how the file is organised, and the difficulty here is updating rather than searching.
> 
> Do not accept "random files are faster" on its own. A bare speed claim earns nothing without the reason, which is that a record's position comes from its key, so that record can be rewritten on its own.

> **[exam-tip]**
> The mark is for the consequence, not the label. Writing "sequential files are hard to update" only repeats the question. Say why: the records have to stay in key order, so changing one means writing the whole file out again.
> 
> Watch the word "continuously" in the stem. It is there to tell you that batch updating is not an option, and that is the whole reason sequential organisation fails. Exam scenarios usually hide the deciding detail in one short phrase like this.

### Q8
Sequential file organisation. **[1]**

The records are held in order of the key field, which is the catalogue number, so the file is already arranged in the order the printed list needs. **[1]**

The file is only changed once a month, in a single batch, so the need to write out a new version of the file whenever it is updated is not a problem here. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for naming sequential file organisation
> 
> **1 mark** for linking the ordering to the key field: the records are stored in order of the catalogue number // the file is already held in catalogue-number order
> 
> **1 mark** for linking the cost of updating to the batch pattern: a sequential file has to be written out as a new version when records are added, and additions here happen only once a month // updates are infrequent, so rewriting the file is acceptable
> 
> Accept "sorted file" for sequential.
> 
> Do not accept serial. In a serial file the records are stored in the order they arrive, so the file would be in the order the books were bought, not in catalogue-number order.
> 
> Do not accept random. In a random file the records are stored in no particular order, so the file itself is not held in catalogue-number order.

> **[exam-tip]**
> A "choose the method" question only earns full marks if your reasons are tied to detail in the scenario. Two details do the work here: the unique catalogue number, which is the key field, and the fact that new books arrive once a month in a batch. Name them both.
> 
> The common error is to pick random organisation because it sounds faster. How quickly one record can be reached is a question about file access, not about file organisation. This file is always used as a whole list and is updated in batches, which is what sequential organisation is for.

### Q9
| Method of file organisation | How the records are placed in the file |
|---|---|
| Sequential | **The records are stored in order, and that order is set by the value of a key field** **[1]** |
| Random | **The records are stored in no particular order, and the position of each record is set by that record's key** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for sequential: the records are stored in order // the records are sorted, based on the value of a key field
> 
> **1 mark** for random: the records are stored in no particular order // there is no sequencing in the placement of the records // the location of a record is set by its record key
> 
> Accept "ordered on a record key" or "ordered on an index" for the sequential mark.
> 
> Accept "a hashing algorithm is applied to the record key to give the location" for the random mark.
> 
> Do not accept "the records are stored in the order they arrive" for sequential. That describes serial organisation, where each new record is appended to the end of the file.
> 
> Accept "the records are stored in no particular order" on its own for random; "stored randomly" may be read as the same point. Do not accept "the records are put anywhere at random, by chance".

> **[exam-tip]**
> "Random" is a misleading name. Records in a random file are not scattered by chance. Each record's position comes from its key, and that is exactly what makes the file useful. Students who write "the records are put anywhere by chance" lose the mark; "stored in no particular order" earns it.
> 
> Sequential and serial are easy to mix up because the words look alike. Serial means the order the records arrived in. Sequential means sorted on a key field. Naming the field your order is based on shows the examiner you know the difference.

### Q10
> **[mark-scheme]**
> **One **mark per mark point (**Max 2**)
> 
> MP1 A collision is when the two values / data items in the key field for two records (pass through a hashing algorithm and) result in the same hash value
> 
> MP2 …so the location identified (by the hashing algorithm) may already be in use // two records cannot occupy the same address.
> **[mark-scheme]**
> **One **mark per mark point (**Max 3**)
> 
> MP1 A process of collision resolution is used
> 
> MP2 Start at the original hashed storage space
> 
> MP3 …go through the following spaces in a linear fashion
> 
> MP4 …and **store the data item** in the first available slot.
> 
> **OR **
> 
> MP5 Search the overflow area
> 
> MP6 …go through the following spaces in a linear fashion
> 
> MP7 …and **store the data item** in the first available slot.
> 
> **OR **
> 
> MP8 Each storage space holds a reference to a collection / chain of items
> 
> MP9 …which can be searched individually.
> 
> MP10 The **data item is stored** in the first available space in this chain.

### Q11
> **[mark-scheme]**
> **One** mark per mark point – sequential (**Max 2**)
> 
> MP1 **Records **(in the file) are ordered
> 
> MP2 …based on the **key field **
> 
> MP3 A new version (of the file) has to be created to update the file
> 
> One mark per mark point – random (**Max 2**)
> 
> MP4 **Records **are stored in no particular order within the file // There is no sequencing in the placement of the **records **
> 
> MP5 There is a relationship between the key of the **record **and its location within the file // a hashing algorithm is used to find the location of the **record **
> 
> MP6 Updates to the file can be carried out directly.
> **[mark-scheme]**
> **One **mark per mark point (**Max 2**)
> 
> MP1 Start at the beginning of the file
> 
> MP2 …check records linearly
> 
> MP3 …until the desired record is found // … processing / updating records as required //… EOF found.

### Q12
> **[mark-scheme]**
> **One mark** per mark point (**Max 2**)
> 
> MP1 Direct access allows a **record **to be found in a file without other records being read.
> 
> MP2 **Records **are found by using the **key field** of the target **record **// the location of the record is found using a **hashing algorithm.**
> **[mark-scheme]**
> (i) **One mark** per mark point (**Max 2**)
> 
> MP1 In sequential files, an index of all key fields is kept
> 
> MP2 The index is **searched **for the address of the file location where the target record is stored.
> 
> (ii) **One mark** per mark point (**Max 2**)
> 
> MP1 A **hashing algorithm** is used on the **key **field of the record
> 
> MP2 … to calculate the address of the memory **location** where the target record is expected to be stored.
> 
> MP3 Method to find a record if it is not at the expected location e.g. linear probing, search overflow area etc.

### Q13
> **[mark-scheme]**
> **One** mark per mark point (**Max 2**)
> 
> MP1 Sequential access method searches for records one after the other
> 
> MP2 … from the physical start of the file until the record is found/the end of file.
> **[mark-scheme]**
> **One** mark per mark point (**Max 3**)
> 
> MP1 For serial files, records are stored in chronological order
> 
> MP2 … every record needs to be checked until the record is found, or all records have been checked.
> 
> MP3 For sequential files, records are stored in order of a key field/index, and it is the key field/index that is compared.
> 
> MP4 … every record is checked until the record is found, or the key field of the current record is greater than the key field of the target recor

### Q14
> **[mark-scheme]**
> **One **mark per mark point (**Max 2**)
> 
> MP1 Records are stored one after the other as they are collected // records are stored in chronological order 
> MP2 New records are appended to the end of the file.
> **[mark-scheme]**
> **One** mark for a use (**Max 1**)
> 
> MP1 Creating unsorted / temporary transaction files 
> MP2 Creating data logging files

### Q15
> **[mark-scheme]**
> **One mark** per mark point (**Max 3**)
> 
> MP1 A hashing algorithm is used in direct access methods on random and sequential files
> 
> MP2 It is a mathematical formula
> 
> MP3 … used to perform a calculation applied to the key field of the record being searched / stored
> 
> MP4 The result of the calculation gives the address where the record should be found / stored.
> **[mark-scheme]**
> **One mark **per mark point (**Max 2**)
> 
> MP1 The record is stored in the next free memory space after the one identified by the hashing algorithm // Use linear progression
> 
> MP2 An overflow area is set up and the record is stored in the next free memory space in the overflow area.

### Q16
> **[mark-scheme]**
> **MP1 **Method: Create a filename **suffix** which is **incremented **for each file save
> 
> **MP2 **Example: SaveFile01.txt, SaveFile02.txt
