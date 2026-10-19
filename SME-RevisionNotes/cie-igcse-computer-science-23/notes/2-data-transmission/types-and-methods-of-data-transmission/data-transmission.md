---
note_id: "rn_Qvg8vXCv28MMmp3k"
title: "Data Transmission"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/2-data-transmission/types-and-methods-of-data-transmission/data-transmission
path: 2-data-transmission/types-and-methods-of-data-transmission/data-transmission
updated_at: "2025-11-28T05:57:29.987Z"
spec_point_ids: ["spcpt_jk5xWZ6FcD2GKHYK", "spcpt_kSWh6RscsNv3C9kc"]
spec_point_codes: []
guided_study: false
---

# Data Transmission

## What is data transmission?

- Data transmission is the process of** transferring data from one device to another **using a **wired **or **wireless **connection
- **Wired **data transmission can be completed in two ways:

  - **Serial **
  - **Parallel**

## Serial & Parallel Transmission

> **Spec point** — `spcpt_jk5xWZ6FcD2GKHYK` · "2 (a) Describe how data is transmitted from one
device to another using different methods of
data transmission"

## Serial & Parallel Transmission

### What is serial & parallel transmission?

- Serial and parallel are **methods of transmitting data** (bits) from a **sender to a receiver**
- Each method determines** how many bits **can be **transmitted at once**

#### Serial transmission

- A stream of bits is** sent in sequence**, one after the other, **along a single wire**
- **USB **is an example of a wired serial connection

![Diagram showing serial transmission between sender and receiver ](../../../assets/0fa3d701d661-wired-connections-serial.png)

#### Parallel transmission

- Multiple bits are sent **simultaneously**, with each bit travelling on its** own separate wire**
- Parallel transmission is** usually synchronous**, using a **clock signal to keep data aligned**
- However, bits can arrive at slightly different times due to **skew** (**timing differences between wires**)
- A traditional printer cable is an example of a wired parallel connection

![Diagram showing parallel transmission between sender and reciever](../../../assets/db58732ef3a8-a-sender-sends-a-stream-of-bits-in-sequence.png)

### Advantages and disadvantages of serial & parallel transmission

| **Transmission** | **Advantages** | **Disadvantages** |
|---|---|---|
| Serial | - Reliable over longer distance<br>- Cheaper to setup<br>- Low interference | - Slow transmission speed |
| Parallel | - Very fast transmission speed | - Only used on short distances<br>- Prone to high interference |

## Simplex, Half-Duplex & Full-Duplex Transmission

> **Spec point** — `spcpt_kSWh6RscsNv3C9kc` · "(b) Explain the suitability of each method of data
transmission, for a given scenario"

## Simplex, Half-Duplex & Full-Duplex Transmission

### What is simplex, half-duplex & full-duplex transmission?

- Simplex, half-duplex and full-duplex describe the **direction** in which data can be transmitted between a sender and receiver

#### Simplex transmission

- Data travels in** only one direction**
- Sending data from a computer to a monitor is an example of simplex transmission

#### Half-duplex transmission

- Data can travel in **both directions**, but **only one direction at a time**
- A printer cable which **waits for the data to be received** before sending back a ‘low ink’ message is an example of half-duplex transmission

#### Full-duplex transmission

- Data can travel in **both directions at the same time**
- Network cables can **send and receive data at the same time** and are examples of full-duplex data transmission
- Full-duplex is used in local and wide area networks

### Advantages and disadvantages of simplex, half-duplex & full-duplex transmission

| **Transmission** | **Advantages** | **Disadvantages** |
|---|---|---|
| Simplex | - Simple and low-cost for one-way communication | - Cannot support two-way communication |
| Half-duplex | - Cheaper than full-duplex for two-way communication | - Slower due to one-direction-at-a-time |
| Full-duplex | - Fast, supports simultaneous two-way data transfer | - More expensive to implement |

- Wires can be **combinations of** serial, parallel, simplex, half-duplex and full-duplex

|   | **Simplex** | **Half-duplex** | **Full-duplex** |
|---|---|---|---|
| **Serial** | Serial-Simplex | Serial-Half-duplex | Serial-Full-duplex |
| **Parallel** | Parallel-Simplex | Parallel-Half-duplex | Parallel-Full-duplex |

- **Serial-Simplex**

  - Data is transmitted **one bit at a time** in **one direction only** on a single wire
- **Serial-Half-duplex**

  - Data is transmitted **one bit at a time**, and can flow in **both directions**, but **not at the same time**
  - This typically uses a **single shared wire**.
- **Serial-Full-duplex**

  - Data is transmitted **one bit at a time in both directions simultaneously**, but this requires **two wires**, one for each direction.
- **Parallel-Simplex**

  - Multiple bits are **transmitted simultaneously in one direction only**, using **multiple wires**
- **Parallel-Half-duplex**

  - **Multiple wires send multiple bits** of data in **both directions**, but only **one direction at a time**
- **Parallel-Full-duplex**

  - **Multiple wires send multiple bits **of data in** both directions simultaneously**

> **Worked Example**
> A company has a website that is stored on a web server
> The company uses parallel half-duplex data transmission to transmit the data for the new videos to the web server. 
> 
> **Explain** why parallel half-duplex data transmission is the most appropriate method.
> 
> **[6]**
> 
> **Answer**
> 
> - **Parallel would allow for the fastest transmission ****[1]**
> - **as large amounts of data ****[1]**
> - **can be uploaded and downloaded ****[1]**
> - **but this does not have to be at the same time ****[1]**
> - **Data is not required to travel a long distance ****[1]**
> - **Therefore, skewing is not a problem ****[1]**

> **Exam Hint**
> Any four of these points qualifies as a full answer, however make sure your answer is cohesive.
> 
> Saying “*Parallel would allow for the fastest transmission but this does not have to be at the same time*” would qualify as one mark as only the first part makes sense and follows logically
