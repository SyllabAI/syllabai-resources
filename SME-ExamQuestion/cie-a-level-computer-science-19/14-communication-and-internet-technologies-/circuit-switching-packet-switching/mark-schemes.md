# Mark Schemes — Circuit Switching, Packet Switching
**14. Communication & internet technologies** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (8 questions)


### Q1
With packet switching the bandwidth can be shared, so the other traffic can use the same path at the same time as the archive file is being copied. **[1]**

If circuit switching were used, the circuit would be held for the whole of the transfer and no other traffic could use it, even while the circuit was idle. **[1]**

When one of the routes fails, the packets can be re-routed and the transfer carries on, whereas a circuit switched transmission would simply end and the circuit would have to be set up again. **[1]**

The file is not needed in real time, so the delay caused by reassembling the packets at the destination does not matter here. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for bandwidth can be shared // packets from other traffic can share the same path
> 
> **1 mark** for with circuit switching no other transmission can use the circuit while it is in use // bandwidth is wasted because the circuit is held whether or not it is being used
> 
> **1 mark** for packets can be re-routed if a route fails, so the transfer continues
> 
> **1 mark** for with circuit switching there is no alternative route, so the transmission ends // the circuit has to be set up again
> 
> **1 mark** for a lost or corrupted packet can be re-sent on its own rather than the whole file
> 
> **1 mark** for the file does not need to be live or streamed, so the time taken to reassemble the packets is acceptable
> 
> **1 mark** for packets generally travel by different routes, so the transfer is considered more secure
> 
> **1 mark** for with circuit switching all the data travels along the same route, so it is less secure // can be intercepted
> 
> Maximum 4 marks.
> 
> Accept an answer that pairs a packet switching benefit with the matching circuit switching drawback as two separate marks, as shown above.

> **[exam-tip]**
> Answers that simply list the benefits of packet switching do not fully answer a question worded like this one. Every detail in the scenario has been put there to be used: the shared connection, the route that fails, and the fact that nobody is watching the file while it copies. Take each of those in turn and say what packet switching does with it and what circuit switching would have done instead.

### Q2
Circuit switching needs a dedicated path to be set up before any data is sent, whereas packet switching needs no dedicated path. **[1]**

In circuit switching the message stays whole and travels along one route, whereas in packet switching the message is split into packets that may each take a different route. **[1]**

With circuit switching the data arrives in the order it was sent, whereas with packet switching the packets can arrive out of order and have to be reassembled at the destination. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - circuit switching uses a dedicated channel, whereas packet switching forms the data into packets
> - the dedicated path must be established before transfer can begin with circuit switching, whereas packet switching does not require one
> - the message stays intact in circuit switching, whereas in packet switching it is split into packets
> - all of the transmission follows the same path in circuit switching, whereas different packets can take different routes in packet switching
> - the message is received in the order it was sent with circuit switching, whereas packets can be received out of order and reassembled at the destination
> - circuit switching uses the whole bandwidth of the channel, whereas packet switching can share bandwidth
> - a circuit switched transmission ends if there is an error, whereas packet switching allows packets to be re-sent
> - circuit switching is a simpler process than packet switching
> 
> **[3 marks]**
> 
> Each mark requires **both** sides of the difference. A statement about only one of the two methods does not identify a difference and scores zero.
> 
> Do not accept the same difference expressed twice in different words, for example "the route is fixed" and "all the data goes the same way".

> **[exam-tip]**
> This is where most marks are dropped on this topic. A difference needs both halves, so "packets can take different routes" earns nothing on its own; you must add what circuit switching does instead. Write each answer as one sentence containing the word "whereas" and you will not be able to leave a half out by accident.

### Q3
Circuit switching. **[1]**

A dedicated circuit is held open for the whole of the meeting, so the data travels as a continuous stream and arrives in the order it was sent. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for circuit switching
> 
> **1 mark** for a reason
> 
> Accept "the whole of the bandwidth is available" // "it is suitable for real-time transmission" for the reason mark
> 
> Accept "the data travels in a continuous stream along the same route" for the reason mark.
> 
> Accept "the data is transmitted at a fixed data rate" and "there is no waiting time at switches" for the reason mark.
> 
> The reason mark is only available if circuit switching has been chosen. A reason given in support of packet switching scores zero here.

> **[exam-tip]**
> Read the scenario for the words that decide the answer. "Live", "continuous" and "for as long as a meeting lasts" all point to a real-time link that needs a path held open, which is circuit switching. The reason must then be a property of circuit switching, not a general statement that the link will work well, and it must match the scenario you were given.

### Q4
Each packet is transmitted independently, so the download is not tied to a single route. **[1]**

When a route fails, the remaining packets can be re-routed and sent by a different path to the destination. **[1]**

The receiving computer can tell that packets are missing, because the packet numbers in the headers are not all present, and it sends a re-transmission request so that those packets are sent again. **[1]**

Once every packet has arrived, the packet numbers are used to put the packets back into the order they were sent in, and the file is reassembled. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for packets are transmitted independently // packets are not all tied to one route
> 
> **1 mark** for packets can be re-routed // packets can travel by a different route to the destination when one route fails
> 
> **1 mark** for missing or corrupted packets are detected at the destination
> 
> **1 mark** for a re-transmission request is sent // the missing packets are re-sent
> 
> **1 mark** for the packets are re-ordered using the packet number or sequence number in the header
> 
> **1 mark** for the packets are reassembled into the original file at the destination
> 
> Maximum 4 marks.
> 
> Accept "sent another way" for re-routed.
> 
> Accept "the receiver asks for the packet again" for the re-transmission request mark.
> 
> Do not accept "the router repairs the broken route". A router chooses a different route for the packets; it does not fix the failed one.

> **[exam-tip]**
> Two separate things are being asked here, and weak answers only do one of them. "Complete" is about the missing packets being detected and re-sent, and "in the correct order" is about the packet numbers being used to reassemble the file. Answer both, and say explicitly that packets usually arrive out of order, because that is the point the reassembly mark depends on.

### Q5
The document is divided into packets, and every packet is made the same size. **[1]**

A packet header is attached to each packet, holding control information such as the source and destination IP addresses and the packet number. **[1]**

The packets are then transmitted independently of one another. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - the data to be transmitted is divided into equal sized packets
> - a packet header is attached to each packet
> - the header holds key information such as the source and destination IP addresses and the packet number
> - the packets are transmitted independently of each other ...
> - ... and may travel by different routes to the destination
> 
> **[3 marks]**
> 
> Accept "split", "broken up" and "divided" for dividing the message into packets.
> 
> Accept "each packet is sent separately" or "each packet is sent on its own" for the independent transmission mark.
> 
> Do not accept "the document is compressed". Compression is a separate process and is not part of dividing a message into packets.

> **[exam-tip]**
> The command word is describe, so a bare list of nouns will not score. Each mark here is a step the computer carries out, so write each one as an action: the message is divided, a header is attached, the packets are sent. Students also lose the first mark by saying only that the message is "split up" without saying what it is split into, or without the point that the packets are all the same size.

### Q6
The IP address of the computer the packet is being sent to. **[1]**

The packet number, which shows where this packet belongs in the original message. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - destination IP address
> - source IP address
> - packet number // sequence number
> 
> **[2 marks]**
> 
> Accept "the IP address of the receiver" and "the IP address of the sender" for the two address marks.
> 
> Accept "the position of the packet in the message" for the packet number mark.
> 
> Do not accept "the data" or "the message". The data being sent is carried by the packet itself, not by its header, so this does not answer the question asked.

> **[exam-tip]**
> The three items above are the ones Cambridge prints in its own mark schemes, so learn those three rather than a long list of fields from a textbook. The mark most often thrown away is the address one: writing "the IP address" on its own does not tell the examiner whether you mean the sender or the receiver, and only a clearly labelled source address or destination address is safe.

### Q7
> **[mark-scheme]**
> **One** mark per mark point **(Max 3) **
> 
> - MP1    The data to be transmitted is divided into equal sized packets
> - MP2    A packet header is attached to each packet containing key information
> - MP3    … such as source/destination IP addresses, packet number, etc
> - MP4    Packets are transmitted independently
> - MP5    … and may travel though different routes/paths to the destination
> - MP6    Routes are determined using a routing table//Packets take the optimum route depending on congestion
> - MP7    The packets usually arrive out of order
> - MP8    The packets are reassembled in the correct order at the destination // The packets are re-ordered using the sequence number/the header
> - MP9    If packets are missing/corrupted a re-transmission request is sent / packets are re-sent.
> **[mark-scheme]**
> **One **mark for each benefit **(Max 2) **
> 
> - MP1    Packets are more likely to arrive because they can be re-routed if a problem occurs with one of the routes//Packets are more likely to arrive because if a packet is lost, it can be re-transmitted
> - MP2    Bandwidth can be shared allowing packets from different messages to share the same path
> - MP3    Considered secure as the packets generally travel via different routes
> - MP4    High data transmission rate is possible
> 
> **One** mark for each drawback **(Max 2) **
> 
> - MP5    Time delay because packets need to be re-ordered/reassembled at the destination//Time delay caused by missing packets needing to be re-sent//Time delay because it has to share the bandwidth of the circuit / channel with other packets
> - MP6    Requires a complex algorithm to function
> - MP7    Needs lots of RAM to handle large amounts of data.

### Q8
> **[mark-scheme]**
> **One** mark per mark point **(Max 3) **
> 
> - MP1    A dedicated circuit / channel is required
> - MP2   The circuit is established before the transmission begins
> - MP3   The circuit lasts for the whole of the transmission // The circuit is closed at the end of the transmission
> - MP4   Data travels in a continuous stream along the same route
> - MP5   Transmission is usually bidirectional.
> **[mark-scheme]**
> **One mark** for a benefit **(Max 1) **
> 
> MP1   No need for data to be reassembled // data / frames arrive in the same order in which they were sent 
> MP2   Suitable for real time transmission // fast data transfer rate 
> MP3   The whole of the bandwidth is available
> 
> **One mark** for a drawback **(Max 1) **
> 
> MP4   No other transmission can use the same circuit when it is in use // Bandwidth can be wasted as it cannot be used by other messages 
> MP5   Not secure // Can be intercepted as all data travelling along the same route 
> MP6   If there is a problem with the route the transmission ends // No other route is available without first doing the setup 
> MP7   The circuit is always there whether or not it’s being used MP8 Can take time to set up before transmission starts.
