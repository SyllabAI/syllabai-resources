## Data Transmission across Networks

* **Bandwidth**

  * The maximum capacity or rate of data transfer over a communication channel.

  * It is the theoretical limit of how much data a medium can move.

* **Bit Rate**

  * The actual number of bits transferred along a communication channel in a single unit of time (usually 1 second).

  * Notation: Measured in bits per second (bit/s or bps). Note: 1 kilobit = 1000 bits (metric 'k').

  * Measurement Method: Start a video stream of a known file size, use software to capture traffic over a set period (e.g., minutes), and calculate bits per second.

#|
||

Media Type

|

Key Characteristics

|

Typical Bandwidth / Performance

||
||

Fibre Optic

|

Uses light pulses (lasers/LEDs) through glass/plastic. Uses Total Internal Reflection.

|

High: 20–40 Gbit/s (Commercial) to 100\+ Tbit/s (Tests).

||
||

Twisted Pair

|

Copper cores twisted to reduce EMI and crosstalk. Categories like Cat5e/Cat6.

|

Medium: 100 Mbit/s to 1 Gbit/s (if all 4 pairs used).

||
||

Coaxial

|

Central copper core with metal braid shield. Twisted pair has mostly superseded coaxial cable in LANs.

|

Low: 10 Mbit/s (10Base 2). Used for cable TV and downlinks.

||
||

Wireless (Wi-Fi)

|

Radio waves are restricted by distance, walls, and the location of the WAP.

|

Variable: 11 Mbit/s to 1 Gbit/s (modern standards).

||
||

Mobile (4G/5G)

|

Cellular radio frequencies; 5G uses higher frequencies for ultra-low latency.

|

High: 100 Mbit/s (4G) to 10 Gbit/s\+ (5G).

||
||

Lasers (FSO)

|

Free-space optics require a clear line of sight and accurate alignment.

|

High: 1 Gbit/s to 10 Gbit/s (in space/vacuum).

||
|#

### Advantages and Disadvantages of Transmission Methods

1. Fibre Optic

   #|
   ||
   
   Advantages

   |
   
   Disadvantages

   ||
   ||
   
   Immune to electromagnetic interference (EMI) and corrosion

   |
   
   Expensive installation; requires specialised tools and skilled technicians

   ||
   ||
   
   Harder to "tap" into (more secure)

   |
   
   Fragile (glass cores can snap if bent sharply)

   ||
   ||
   
   Low signal loss over long distances (2km\+)

   |
   
   ​

   ||
   |#
   

2. Copper (Ethernet/Twisted Pair)

   #|
   ||
   
   Advantages

   |
   
   Disadvantages

   ||
   ||
   
   PoE (Power over Ethernet): Can transmit electrical power to devices

   |
   
   Susceptible to EMI; must be kept away from mains power

   ||
   ||
   
   Flexible and simple to install around corners

   |
   
   Lower bandwidth and shorter distance (maximum 100m) compared to fibre

   ||
   ||
   
   There is cheaper hardware (NICs and cables) than fibre

   |
   
   ​

   ||
   |#
   

3. Lasers (Free Space)

   #|
   ||
   
   Advantages

   |
   
   Disadvantages

   ||
   ||
   
   No physical medium required; ideal for spacecraft/satellite communication

   |
   
   Rain, fog, or dust disrupt beams in the atmosphere

   ||
   ||
   
   Higher bandwidth than radio waves in a vacuum

   |
   
   Requires near-perfect alignment; beams cannot pass around corners

   ||
   |#
   

### Data Streaming

* **Real-time (Live) Streaming**

  * The source is a live event (e.g., sports, music concert).

  * Content is captured, encoded, and distributed immediately.

  * Cannot be paused or rewound as it happens (unless recorded locally).

* **On-demand Streaming**

  * The source is a pre-recorded file (e.g., Netflix, YouTube).

  * It can be streamed at any time; allows user control (pause, fast-forward).

**Impact of Bit Rate on Streaming Quality**

* **General Rule:** High bit rate = high quality but requires higher bandwidth.

* **Audio quality:** low bit rates cause "warbling," "bubbling," or "stuttering" artefacts.

  * High quality: 192–320 kbit/s.

* **Video Quality**

  * Low bit rate/bandwidth leads to pixelation, jerky motion, and buffering (the player waits to fill memory before resuming).

  * Resolution vs. Motion: In low-bandwidth video conferencing, prioritise resolution for documents/slides and motion for presentations.

### Effects on Available Bandwidth

The actual speed you experience is rarely the maximum bandwidth due to the following:

1. **Overheads:** Addressing data (headers), error-correction data (adding bits to the frame), and retransmission requests.

2. **Modulation:** The method used to convert digital bits into signals (e.g., laser phase modulation).

3. **Network Traffic:** Collisions and processing delays at nodes (routers/switches).

4. **Signal-to-Noise Ratio (SNR):** Higher noise levels reduce the effective bit rate.