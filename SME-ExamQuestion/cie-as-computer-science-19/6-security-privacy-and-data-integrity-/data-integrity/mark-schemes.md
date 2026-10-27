# Mark Schemes — Data Integrity
**6. Security, Privacy & Data Integrity** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (6 questions)


### Q1
> **[mark-scheme]**
> (i) **MP1** A message cannot contain a zero-length data field
> 
> **MP2** … so a blank line cannot be sent // there is no way to send a blank line
> 
> (ii) **MP1 **Append a (special) character to the start of the message text
> 
> **MP2 **interpret the new field data as a blank line
> 
> ALTERNATIVE
> 
> **MP1 **Change the message protocol and use an additional field to act as an indicator
> 
> **MP2 **Interpret the new field data

### Q2
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - Validation // a validation method named or described
> - …protects the data by ensuring that the data is reasonable / sensible and within specified bounds.

### Q3
> **[mark-scheme]**
> 1 mark for each bullet point.
> 
> - The administrator completes a visual check / checks by eye
> - …that the tutor identifier input matches the tutor identifier on the **original** document
> - Double entry check // the administrator (or a second person) enters the number a second time
> - …and the **system **compares it with the first entry

### Q4
> **[mark-scheme]**
> **1 mark** for each correct method and
> 
> **1 mark** for corresponding description to **max 4**:
> 
> | Method | Description |
> |---|---|
> | Parity byte | An additional bit is added to make the number of 1s in the byte odd or even to match the parity. If a byte with an odd number of 1 bits is received when even parity is used, there is an error. |
> | Parity block | Parity is calculated horizontally and vertically. A parity byte is created from the bits produced by the vertical parity check. This is sent with the data. The parity is re-checked when received and the position of an incorrect bit can be determined. |
> | Checksum | A calculation is made from the data and the result transmitted with the data. The receiver repeats the calculation and compares the result with the value received. If the two are different, there is an error. |

### Q5
> **[mark-scheme]**
> **1 mark** for each correctly completed term:
> 
> - odd or even
> - 7-bits
> - odd
> - block
> - byte
> 
> Computer A and Computer B agree on whether to use **odd or even** parity. Computer A divides the data into groups of **7-bits**. The number of 1s in each group is counted. If the agreed parity is **odd** and the group has an even number of 1s a parity bit of 1 is appended, otherwise a parity bit of 0 is appended.
> 
> In a parity **block **check the bytes are grouped together, for example in a grid. The number of 1s in each column (bit position) is counted. A bit is assigned to each column to make the column match the parity. These parity bits are transmitted with the data as a parity **byte**.

### Q6
**1 mark** for each bullet point each (**max 3**)

- Referential integrity is enforced
- … such as cascade update/delete // if the data is changed in one place it is updated in every other place
- ... and ensures each foreign key has a corresponding primary key
