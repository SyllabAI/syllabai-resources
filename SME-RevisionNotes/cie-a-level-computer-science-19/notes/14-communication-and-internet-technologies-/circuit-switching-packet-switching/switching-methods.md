---
note_id: "rn_6b66HvWZZKJMnMZJ"
title: "Switching Methods"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/14-communication-and-internet-technologies-/circuit-switching-packet-switching/switching-methods
path: 14-communication-and-internet-technologies-/circuit-switching-packet-switching/switching-methods
updated_at: "2026-10-01T13:10:00.138Z"
spec_point_ids: ["spcpt_pSnZ8RGQhrg33tZQ", "spcpt_wbXgB3cVXN6Y87Ts"]
spec_point_codes: []
guided_study: false
---

# Switching Methods

## Packetising

> **Spec point** — `spcpt_pSnZ8RGQhrg33tZQ`

## Packetising

### What is packetising?

- Packetising is the process of **dividing a large message into smaller**, manageable units called **packets**
- Each packet can be** transmitted individually** across a network

#### Structure of a packet

- Each packet contains:

  - A **packet header**, which contains key information such as:
  - **Source IP address**: who sent the packet
  - **Destination IP address**: where it is going
  - **Sequence number (packet number)**: used to reassemble packets in the correct order
  - **Checksum**: used for error checking
  - **The data**: the part of the message being sent in this packet

### Packet transmission & reassembly

- Once packetised and encapsulated with headers, **packets are transmitted independently**
- They may travel along **different routes** through the network
- At the destination, packets are **reassembled** into the original message using sequence numbers

## Circuit & packet switching

> **Spec point** — `spcpt_wbXgB3cVXN6Y87Ts`

## Circuit & packet switching

## What is packet switching?

- Packet switching is a communication method where **data is broken into packets **and sent across a shared network
- Each packet may** take a different path to the destination** and is reassembled on arrival

#### Benefits:

- **Efficient **use of network **bandwidth**
- More **reliable **– only lost or corrupted packets need to be resent
- **Lower cost** – network resources are shared

#### Drawbacks:

- **Not ideal** for** real-time applications** like VoIP or video calls
- Packets can** arrive out of order** and require reassembly
- Network congestion may lead to** packet delay or loss**

### What is circuit switching?

- Circuit switching sets up a **dedicated communication path** between two devices for the duration of a session (like a traditional phone call)

#### Benefits:

- Ideal for **real-time communication** – steady and continuous data flow
- **No delays** once the circuit is established
- Data arrives **in order**

#### Drawbacks:

- **Less efficient** – resources remain reserved even when not in use
- **Higher cost** due to dedicated lines
- **Less scalable** and flexible for large networks

### Packet switching vs circuit switching

| **Feature** | **Packet switching** | **Circuit switching** |
|---|---|---|
| **Definition** | Data is split into packets and sent independently over shared routes | A dedicated path is set up for the duration of the communication |
| **Transmission** | Data is sent in individual packets | Data is sent in a continuous stream |
| **Efficiency** | High – uses bandwidth as needed, paths shared among many users | Low – resources are tied up for each communication, even when idle |
| **Reliability** | Robust – packets can be rerouted if a failure occurs | Less robust – if the path fails, the call is dropped and must be re-established |
| **Scalability** | Highly scalable – handles large volumes of data and users | Less scalable – more users require more physical paths |
| **Use Cases** | Best for emails, web pages, file downloads | Best for real-time communication (voice calls, video conferencing) |
| **Data Order** | May arrive out of order – requires reassembly | Always arrives in order |
| **Cost** | Lower – due to shared infrastructure | Higher – due to reserved bandwidth and infrastructure |

> **Exam Hint**
> Speed can earn a mark when it is stated precisely and tied to the right method. Mark schemes have accepted "fast data transfer rate" as a benefit of circuit switching and "high data transmission rate is possible" as a benefit of packet switching. Back it up with the reason: circuit switching has the whole bandwidth of the channel available, while packet switching lets packets share bandwidth and take the best route depending on congestion.
