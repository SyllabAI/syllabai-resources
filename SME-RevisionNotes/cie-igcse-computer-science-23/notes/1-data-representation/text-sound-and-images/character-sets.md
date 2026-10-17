---
note_id: "rn_4ZcCbrXQKgJNTT4d"
title: "Character Sets"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/1-data-representation/text-sound-and-images/character-sets
path: 1-data-representation/text-sound-and-images/character-sets
updated_at: "2025-11-28T05:38:01.117Z"
spec_point_ids: ["spcpt_dqr4BcmjTs3mNfs6", "spcpt_rtdpdPGNztZq5TxN", "spcpt_9qWgbG7zBdpCdZgT"]
spec_point_codes: []
guided_study: false
---

# Character Sets

## Character Sets

> **Spec point** — `spcpt_dqr4BcmjTs3mNfs6` · "1 Understand how and why a computer represents
text and the use of character sets, including
American standard code for information
interchange (ASCII) and Unicode"

## Character Sets

### What is a character set?

- A character set is **all the characters and symbols** that can be **represented **by a computer system
- Each character is given a **unique **binary code
- Character sets are **ordered logically**, the code for ‘B’ is one more than the code for ‘A’
- A character set provides a ***standard*** for computers to communicate and send/receive information
- Without a character set, one system might interpret 01000001 differently from another
- The number of characters that can be represented is determined by the** number of bits used** by the character set
- Two common character sets are:

  - American Standard Code for Information Interchange (**ASCII**)
  - Universal Character Encoding (**UNICODE**)

## ASCII

> **Spec point** — `spcpt_rtdpdPGNztZq5TxN` · "1 Understand how and why a computer represents
text and the use of character sets, including
American standard code for information
interchange (ASCII) and Unicode"

## ASCII

### What is ASCII?

- ASCII is a character set and was an accepted standard for information interchange
- ASCII uses **7 bits**, providing 2<sup>7</sup> unique codes (128) or a maximum of **128 characters **it can represent

![ASCII character set containing character, ASCII and binary codes ](../../../assets/fce7a8eb3b39-ascii-table.png)

- ASCII only represents basic characters needed for **English**, limiting its use for other languages

#### Extended ASCII

- Extended ASCII uses **8 bits**, providing 256 unique codes (2<sup>8</sup> = 256) or a maximum of **256 characters **it can represent
- Extended ASCII provides essential characters such as mathematical operators and more recent symbols such as ©

#### Limitations of ASCII & extended ASCII

- ASCII has a **limited **number of characters which means it can only represent the **English alphabet**, **numbers **and some special characters

  - A, B, C, ………, Z
  - a, b, c ,.............,z
  - 0, 1, 2,........, 9
  - !, @, #, …..
- ASCII **cannot **represent characters from languages other than English
- ASCII **does not** include modern symbols or emojis common in today's digital communication

## UNICODE

> **Spec point** — `spcpt_9qWgbG7zBdpCdZgT` · "1 Understand how and why a computer represents
text and the use of character sets, including
American standard code for information
interchange (ASCII) and Unicode"

## UNICODE

### What is UNICODE?

- UNICODE is a **character set** and was created as a solution to the limitations of ASCII
- UNICODE uses a minimum of **16 bits**, providing 2<sup>16</sup>  unique codes (65,536) or a minimum of **65,536 characters** it can represent
- UNICODE can represent characters from **all the major languages** around the world

> **Exam Hint**
> Exam questions often ask you to compare ASCII & UNICODE, for example the number of bits, number of characters and what they store

#### ASCII vs UNICODE

|   | **ASCII** | **UNICODE** |
|---|---|---|
| **Number of bits** | 7-bits | 16-bits |
| **Number of characters** | 128 characters | 65,536 characters |
| **Uses** | Used to represent characters in the English language. | Used to represent characters across the world. |
| **Benefits** | It uses a lot less storage space than UNICODE. | It can represent more characters than ASCII.<br><br>It can support all common characters across the world.<br><br>It can represent special characters such as emoji's. |
| **Drawbacks** | It can only represent 128 characters.<br><br>It cannot store special characters such as emoji's. | It uses a lot more storage space than ASCII. |

> **Worked Example**
> The computer stores text using the ASCII character set.
> 
> Part of the ASCII character set is shown:
> 
> | **Character** | **ASCII Denary Code** |
> |---|---|
> | E | 69 |
> | F | 70 |
> | G | 71 |
> | H | 72 |
> 
> **(a) **
> 
> **Identify **the character that will be represented by the ASCII denary code 76 **[1]**
> 
> **(b) **
> 
> **Identify **a second character set **[1]**
> 
> **Answers**
> 
> **Final answer:** **(a) L (must be a capital)**
> 
> **Final answer:** **(b) UNICODE**
