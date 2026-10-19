---
note_id: "rn_9kXNGXfqM5t2VV8M"
title: "Error Detection Methods"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/2-data-transmission/methods-of-error-detection/error-detection-methods
path: 2-data-transmission/methods-of-error-detection/error-detection-methods
updated_at: "2024-10-04T10:49:10.824Z"
spec_point_ids: ["spcpt_yPdhHr5bcN8bbDKr", "spcpt_WSBqqQcqkNF2BqV4", "spcpt_t5ZMFTmJhJbqcwct", "spcpt_hB2th7BHPxc834Cf"]
spec_point_codes: []
guided_study: false
---

# Error Detection Methods

## Parity Check

> **Spec point** — `spcpt_yPdhHr5bcN8bbDKr` · "2 Describe the processes involved in each of the
following error detection methods for detecting
errors in data after transmission: parity check
(odd and even), checksum and echo check"

## Parity Check

### What is a parity check?

- A parity check determines whether **bits in a transmission** have been **corrupted**
- Every byte transmitted has **one of its bits** allocated as a** parity bit**
- The sender and receiver must **agree** before transmission whether they are using **odd **or **even parity**
- If** odd parity** is used then there must be an **odd number of 1’s in the byte**, including the parity bit
- If **even parity **is used then there must be an **even number of 1’s in the byte**, including the parity bit
- The **value of the parity bit** is determined by** counting the number of 1’s in the byte**, including the parity bit
- If the number of 1’s **does not match the agreed parity** then an** error has occurred**
- Parity checks **only check that an error has occurred**, they do not reveal where the error(s) occurred

#### Even parity

- Below is an arbitrary binary string

| **EVEN**<br>**Parity bit** | **Byte** |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| *0* | *1* | *0* | *1* | *1* | *0* | *1* | *0* |

- If an **even parity bit** is used then** all bits** in the byte, including the parity bit, must **add up to an even number**

  - There are four 1’s in the byte
  - This means the parity bit must be 0 otherwise the whole byte, including the parity bit, would add up to five which is an odd number

#### Odd parity

- Below is an arbitrary binary string

| **ODD**<br>**Parity bit** | **Byte** |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| *1* | *1* | *0* | *1* | *1* | *0* | *1* | *0* |

- If an **odd parity bit** is used then** all bits** in the byte, including the parity bit, must **add up to an odd number**

  - There are four 1’s in the byte. This means the parity bit must be a 1 otherwise the whole byte, including the parity bit, would add up to four which is an even number
- The table below shows a number of examples of the agreed parity between a sender and receiver and the parity bit used for each byte

| **Example #** | **Agreed parity** | **Parity bit** | **Main bit string** | **Total number of 1’s** |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|
| #1 | ODD | *0* | *1* | *1* | *0* | *1* | *0* | *1* | *1* | **5** |
| #2 | EVEN | *1* | *0* | *0* | *0* | *1* | *0* | *0* | *0* | **2** |
| #3 | EVEN | *1* | *0* | *1* | *0* | *1* | *1* | *1* | *1* | **6** |
| #4 | ODD | *1* | *0* | *1* | *1* | *1* | *0* | *0* | *1* | **5** |
| #5 | ODD | *1* | *1* | *0* | *1* | *0* | *1* | *0* | *1* | **5** |
| #6 | EVEN | *0* | *1* | *0* | *0* | *1* | *1* | *1* | *0* | **4** |

- Example #1: The agreed parity is **odd**. All of the 1’s in the main bit string are added** (5)**. As this number is** odd already** the **parity bit **is set to** 0** so the whole byte **stays odd**
- Example #2: The agreed parity is **even**. All of the 1’s in the main bit string are added **(1)**. As this number is **odd** the **parity bit** is set to** 1** to make the** total number of 1’s even** **(2)**
- Example #6: The agreed parity is **even**. All of the 1’s in the main bit string are added** (4)**. As this number is **even already** the **parity bit **is set to** 0** so the whole byte **stays even**

### How do errors occur?

- When using parity bits, an** error** occurs when the number of **total bits does not match the agreed parity**
- Bits can be** flipped** or **changed** due to** interference** on a wire or wirelessly due to **weather **or **other signals**

| **Example #** | **Agreed parity** | **Parity bit** | **Main bit string** | **Total number of 1’s** | **Error** |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| #1 | ODD | *1* | *1* | *1* | *0* | *1* | *0* | *1* | *1* | *6* | *Error* |
| #2 | EVEN | *1* | *0* | *0* | *0* | *1* | *0* | *0* | *0* | *2* | **Final answer:** **No error** |
| #3 | EVEN | *1* | *0* | *1* | *1* | *1* | *1* | *1* | *1* | *7* | *Error* |
| #4 | ODD | *1* | *0* | *1* | *1* | *1* | *0* | *0* | *1* | *5* | **Final answer:** **No error** |
| #5 | ODD | *1* | *1* | *0* | *1* | *0* | *1* | *1* | *1* | *6* | *Error* |
| #6 | EVEN | *0* | *1* | *0* | *0* | *0* | *1* | *1* | *0* | *3* | *Error* |

- Parity checks are **quick **and** easy to implement** but **fail to detect bit swaps** that cause the parity to remain the same

## Parity Byte & Block Check

> **Spec point** — `spcpt_WSBqqQcqkNF2BqV4` · "2 Describe the processes involved in each of the
following error detection methods for detecting
errors in data after transmission: parity check
(odd and even), checksum and echo check"

## Parity Byte & Block Check

### What are parity byte & block checks?

- Parity blocks and parity bytes can be used to **check an error has occurred** and **where the error is located**
- Parity checks on their own **do not pinpoint where errors in data exist**, only that an error has occurred
- A parity block consists of **a block of data **with the number of 1’s totalled **horizontally **and **vertically**
- A parity byte is also sent with the data which contains the **parity bits **from the **vertical parity calculation**
- Below is a parity block with a parity byte at the bottom and a parity bit column in the second column

| **ODD** | **Parity bit** | **Bit 2** | **Bit 3** | **Bit 4** | **Bit 5** | **Bit 6** | **Bit 7** | **Bit 8** |
|---|---|---|---|---|---|---|---|---|
| Byte 1 | *0* | *1* | *1* | *0* | **1** | *0* | *1* | *1* |
| Byte 2 | *0* | *0* | *0* | *0* | **1** | *0* | *0* | *0* |
| **Byte 3** | **1** | **0** | **1** | **0** | **1** | **1** | **1** | **1** |
| Byte 4 | *1* | *0* | *1* | *1* | **1** | *0* | *0* | *1* |
| Byte 5 | *1* | *1* | *0* | *1* | **0** | *1* | *0* | *1* |
| Byte 6 | *1* | *1* | *0* | *0* | **1** | *1* | *1* | *0* |
| Byte 7 | *0* | *0* | *1* | *1* | **1** | *1* | *1* | *0* |
| Byte 8 | *0* | *1* | *0* | *1* | **1** | *0* | *0* | *0* |
| **Parity byte** | *0* | *1* | *1* | *1* | **1** | *1* | *1* | *1* |

- The above table uses **odd parity**
- Each** byte row** calculates the** horizontal parity** as a parity bit **as normal**
- Each **bit column** calculates the **vertical parity** for each row, the **parity byte**
- It is **calculated before transmission** and **sent with the parity block**
- Each **parity bit tracks if a flip error** occurred in a byte while the **parity byte** calculates if an **error occurred in a bit column**
- By **cross referencing** both **horizontal and vertical** parity values the **error can be pinpointed**
- In the above example the **byte 3 / bit 5 cell** is the error and** should be a 0 instead**
- The error could be **fixed automatically or a retransmission request could be sent **to the sender

## Checksum

> **Spec point** — `spcpt_t5ZMFTmJhJbqcwct` · "2 Describe the processes involved in each of the
following error detection methods for detecting
errors in data after transmission: parity check
(odd and even), checksum and echo check"

## Checksum

### What is a checksum?

- A checksum is a value that can be used to determine if data has been** corrupted or altered **
- It indicates whether data **differs from its original form** but **does not **specify where
- Checksums are **calculated using an algorithm** and the value is **added to the transmission**
- The receiving device **re-calculates** the checksum and **compares** to the original
- If the **checksums do not match**, it is assumed an error has occurred

> **Worked Example**
> Describe the process a checksum algorithm uses to determine if an error has occurred
> 
> **[5]**
> 
> **Answer**
> 
> - **Before data is transmitted a checksum value is calculated [1]**
> - **The checksum value is transmitted with the data  [1]**
> - **The receiver calculates the checksum value using the received data  [1]**
> - **The calculated checksum is compared to the transmitted checksum [1]**
> - **If they are the same then there is no error otherwise an error has occurred [1]**

## Echo Check

> **Spec point** — `spcpt_hB2th7BHPxc834Cf` · "2 Describe the processes involved in each of the
following error detection methods for detecting
errors in data after transmission: parity check
(odd and even), checksum and echo check"

## Echo Check

### What is an echo check?

- An echo checks involve **transmitting the received data back to the sender**
- The **sender** then **checks the data** to see if any errors occurred during transmission
- This method **isn’t reliable** as an** error** could have** occurred when the sender transmits the data or when the receiver transmits the data**
- If an **error does occur** the sender will** retransmit the data**

> **Worked Example**
> Four 7-bit binary values are transmitted from one computer to another.
> 
> A parity bit is added to each binary value creating 8-bit binary values. All the binary values are transmitted and received correctly.
> 
> (**a**) Identify whether each 8-bit binary value has been sent using odd or even parity by writing odd or even in the type of parity column.
> 
> | **8-bit binary value** | **Type of parity** |
> |---|---|
> | 01100100 |   |
> | 10010001 |   |
> | 00000011 |   |
> | 10110010 |   |
> 
> **[4]**
> 
> (**b**) An error may not be detected when using a parity check.
> 
> Identify why an error may not be detected.
> 
> **[1]**
> 
> **Answers**
> 
> (**a**)
> 
> | **8-bit binary value** | **Type of parity** |
> |---|---|
> | 01100100 | **Final answer:** **Odd  [1]** |
> | 10010001 | **Final answer:** **Odd  [1]** |
> | 00000011 | **Final answer:** **Even [1] ** |
> | 10110010 | **Final answer:** **Even [1] ** |
> 
> (**b**)
> 
> Any **one **from:
> 
> - **there is a transposition of bits [1]**
> 
> - **it does not check the order of the bits (just the sum of 1s/0s) [1]**
> 
> - **even number of bits change [1]**
> 
> - **incorrect bits still add up to correct parity [1]**
