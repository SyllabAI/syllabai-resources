---
note_id: "rn_W4TGSGFpGkGcmQhb"
title: "Error Checking"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/2-data-transmission/methods-of-error-detection/error-checking
path: 2-data-transmission/methods-of-error-detection/error-checking
updated_at: "2024-04-11T14:08:53.985Z"
spec_point_ids: ["spcpt_rYGQnC9SrgGvXqrb"]
spec_point_codes: []
guided_study: false
---

# Error Checking

## Why Errors Occur

> **Spec point** — `spcpt_rYGQnC9SrgGvXqrb` · "1 Understand the need to check for errors after
data transmission and how these errors can occur"

## Why Errors Occur

### Why do errors occur?

- Errors can occur using wired or wireless technology due to** interference**
- Examples of interference include wire ***degradation***** **or electrical fields changing the signal
- Results of interference include:

  - **Data loss** - data is lost in transmission
  - **Data gain** - additional data is received
  - **Data change** - some bits have been changed or flipped
- Wireless technology uses **radio signals **or** other electromagnetic signals** to transmit data

  - These signals can be blocked by **physical barriers** such as buildings, walls, cars or other objects
  - Interference can be caused by **bad weather** such as rain or clouds, or by other **wireless signals** or **electromagnetic radiation**
- Wired technology carries** more chance of causing an error** as physical components can be **damaged**, **degrade **or **receive interference** from outside signals

  - **Data loss** can also occur from **interruptions **to data transmission such as a blocked signal or if the transmission is *intermittent*

### Why check for errors?

- Computers expect data in certain formats

  - A **format** is a way of **arranging the data** so that it can be easily understood by people and by computers
  - People agree to certain formats so that systems work more **efficiently** and there is little chance of misunderstanding each other
- An example of a format is **date and time**
- Date and time can have multiple formats such as:

  - **13/04/14 (DD/MM/YY)**
  - **12/31/2020 (MM/DD/YYYY)**
  - **Jul-04-16 (MMM/DD/YY)**
- If data is not as expected, things can go wrong
- For example, if a receiver expected to receive a date in format DD/MM/YY as 03/04/17 but received 04/03/17, did the sender mean 3rd April 2017 or 4th March 2017?
- An **error or corruption** occurs when data received is **not as expected** and therefore is **difficult or impossible to process**

> **Worked Example**
> Alex receives an email over a wireless connection from a work colleague containing an important document.
> 
> **Identify **what interference Alex could experience when sending this email and **identify** the outcomes of interference.
> 
> Further **explain why** Alex should check to make sure the document contains no errors.
> 
> **[4]**
> 
> **Answer**
> 
> - **Weather conditions or physical barriers such as building can affect signals, for example bits could be flipped in the document making it hard to understand the original meaning ****[1]**
> - **Alex should be aware that interference can cause wirelessly received data to contain errors or corruption ****[1]**
> - **Data could be lost, additional data could be gained or data could be changed ****[1]**
> - **As Alex received an important work document they need to check for errors so that their work is unaffected and they do not receive incorrect information ****[1]**
