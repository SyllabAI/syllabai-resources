# Circuit Switching, Packet Switching

Course: cie-a-level-computer-science-19 · Section: 14. Communication & internet technologies

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/14-communication-and-internet-technologies-/circuit-switching-packet-switching/


## Card 1 — keyword_definition (`fl_Sf2wZyyJ3RvGzf8h`)

**FRONT**

Define **packetising**.


**BACK**

Packetising is the process of **dividing a large message into smaller, manageable units called packets**, each of which can be transmitted individually.


Spec links: `spcpt_pSnZ8RGQhrg33tZQ`


## Card 2 — question_and_answer (`fl_w6WpYdjkmFTVdVBd`)

**FRONT**

Name the three parts of a packet.


**BACK**

**Header**, **payload** and **footer (trailer)**.


Spec links: `spcpt_pSnZ8RGQhrg33tZQ`


## Card 3 — keyword_definition (`fl_nnNTVJxh8yYxbkvm`)

**FRONT**

Define **payload**.


**BACK**

The payload is the **actual data being sent**.


Spec links: `spcpt_pSnZ8RGQhrg33tZQ`


## Card 4 — question_and_answer (`fl_X3XtMykkNKy3SRTB`)

**FRONT**

Name four items found in a packet header.


**BACK**

**Source IP address**, **destination IP address**, **sequence number**, **protocol**, **packet length** and **checksum**.


Spec links: `spcpt_pSnZ8RGQhrg33tZQ`


## Card 5 — fill_in_the_blanks (`fl_QjcsVyGGc4mWH2GH`)

**FRONT**

The packet header contains the <u>**            **</u> IP address, showing who sent the packet.


**BACK**

The packet header contains the **source** IP address, showing who sent the packet.


*Blanks: 1 — answers: []*

Spec links: `spcpt_pSnZ8RGQhrg33tZQ`

Flags: blank_answer_mismatch


## Card 6 — question_and_answer (`fl_Ns9R342r2ppkmYsB`)

**FRONT**

What is the sequence number in a packet header used for?


**BACK**

To **reassemble the packets in the correct order** at the destination.


Spec links: `spcpt_pSnZ8RGQhrg33tZQ`


## Card 7 — question_and_answer (`fl_nR8HFpcvC6z5D6yC`)

**FRONT**

What is the checksum in a packet header used for?


**BACK**

**Error checking**.


Spec links: `spcpt_pSnZ8RGQhrg33tZQ`


## Card 8 — question_and_answer (`fl_bZxYSFst7jNpp59D`)

**FRONT**

What may a packet footer contain?


**BACK**

Extra **error-checking or control information**.


Spec links: `spcpt_pSnZ8RGQhrg33tZQ`


## Card 9 — question_and_answer (`fl_dJ6nNn7qsNby65vq`)

**FRONT**

How do packets travel across a network?


**BACK**

**Independently**, and they may travel along **different routes** through the network.


Spec links: `spcpt_pSnZ8RGQhrg33tZQ`


## Card 10 — question_and_answer (`fl_3BRbtzYwBhRT6mFH`)

**FRONT**

How is the original message recovered?


**BACK**

The packets are **reassembled** at the destination using their **sequence numbers**.


Spec links: `spcpt_pSnZ8RGQhrg33tZQ`


## Card 11 — keyword_definition (`fl_jm92pCqbcPWYHhdW`)

**FRONT**

Define **packet switching**.


**BACK**

Packet switching is a communication method where **data is broken into packets** and sent across a **shared network**, with each packet possibly taking a different path and reassembled on arrival.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 12 — keyword_definition (`fl_NWsRhhGdq7wXCjTC`)

**FRONT**

Define **circuit switching**.


**BACK**

Circuit switching sets up a **dedicated communication path** between two devices for the duration of a session.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 13 — fill_in_the_blanks (`fl_GjnzzqKM9kCq22KN`)

**FRONT**

Circuit switching works like a traditional <u>**          **</u> call.


**BACK**

Circuit switching works like a traditional **phone** call.


*Blanks: 1 — answers: []*

Spec links: `spcpt_wbXgB3cVXN6Y87Ts`

Flags: blank_answer_mismatch


## Card 14 — true_or_false (`fl_4WXNbp8b8Vk4V7fD`)

**FRONT**

**True or False?**

Packet switching sends data as a continuous stream.


**BACK**

**False.**

Packet switching sends data in **individual packets**. It is **circuit switching** that sends a continuous stream.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 15 — question_and_answer (`fl_7f7dSnQCNtcM2cSf`)

**FRONT**

Name three benefits of packet switching.


**BACK**

**Efficient use of network bandwidth**, **more reliable** because only lost or corrupted packets need resending, and **lower cost** because network resources are shared.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 16 — question_and_answer (`fl_x5wdqfxCPGgNGhzD`)

**FRONT**

Name three drawbacks of packet switching.


**BACK**

**Not ideal for real-time applications**, packets can **arrive out of order** and need reassembly, and network congestion may cause **packet delay or loss**.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 17 — question_and_answer (`fl_2Cjj3zxsFR5Fmq7m`)

**FRONT**

Name three benefits of circuit switching.


**BACK**

It is ideal for **real-time communication** with a steady continuous flow, there are **no delays** once the circuit is established, and data **arrives in order**.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 18 — question_and_answer (`fl_y43PcgFfp7NsZzFf`)

**FRONT**

Name three drawbacks of circuit switching.


**BACK**

It is **less efficient** because resources stay reserved when not in use, it has a **higher cost** due to dedicated lines, and it is **less scalable**.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 19 — true_or_false (`fl_cDKyJHZkyDxxZWT6`)

**FRONT**

**True or False?**

In circuit switching, resources are freed when the line is idle.


**BACK**

**False.**

Resources **remain reserved even when not in use**, which is what makes circuit switching less efficient.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 20 — question_and_answer (`fl_pTwVCWqVjv4m9CP2`)

**FRONT**

How does data order differ between the two switching methods?


**BACK**

With **packet switching**, data **may arrive out of order** and requires reassembly. With **circuit switching**, data **always arrives in order**.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 21 — question_and_answer (`fl_8hxHV5gxP4xRpHyM`)

**FRONT**

Which switching method is more robust to failure, and why?


**BACK**

**Packet switching**, because packets can be **rerouted** if a failure occurs. In circuit switching, if the path fails the call is **dropped and must be re-established**.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 22 — question_and_answer (`fl_8zQ8P73YMYFGTdxm`)

**FRONT**

Which switching method is more scalable?


**BACK**

**Packet switching**, which handles large volumes of data and users. Circuit switching needs **more physical paths** as more users are added.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 23 — question_and_answer (`fl_QqvRpj8tjDstpNSF`)

**FRONT**

What is packet switching best used for?


**BACK**

**Emails, web pages and file downloads**.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`


## Card 24 — question_and_answer (`fl_4BPNPChDCgzw4mBb`)

**FRONT**

What is circuit switching best used for?


**BACK**

**Real-time communication**, such as voice calls and video conferencing.


Spec links: `spcpt_wbXgB3cVXN6Y87Ts`

