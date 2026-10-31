## Circuit Switching, Packet Switching

### Circuit Switching

- Circuit Switching: Method of transmission in which a dedicated circuit lasts throughout the duration of the communication.
- Dedicated circuit is selected before the communication starts and is used to send all the data through this route. - Uses the whole bandwidth.
- Releases circuit once the communication ends.
- Used for live video broadcasts or calling
- Data arrives in order so it doesn’t need to be reassembled.
- Whole bandwidth is available.
- Data can’t get lost.
- Less secure as it only uses one route.
- No alternative route in case of failure.
- Bandwidth can’t be shared.

### Packet Switching

- Method of transmission where the message is broken down into packets which can be sent along independent paths
- Data is split into multiple packets and the best route is calculated for each packet.
- Each packet contain a header, which has a source IP address and destination IP address, and a payload.
- Calculates the most efficient path for each packet.
- Used when sending large files that don’t need to be live streamed or when it is necessary to be able to overcome faulty lines by rerouting like emails, text messages, sending documents, etc.
- Harder to intercept as new route is used each time.
- Packets need to be reassembled.
- If there’s a missing packet, a request is sent to retransmit the data.

**Role of Router:**

- Examines the header and finds the destination IP address.
- Decides the best route for the packet, with the help of the information from the routing table, and sends it towards the next hop.

### **Comparison**


||Circuit Switching|Packet Switching|
|:---|:---|:---|
|Nature|Dedicated channel|Data segmented into packets|
|Setup|Requires pre-established channel|No prior setup needed|
|Data handling|Message remains intact|Message gets split into packets|
|Transmission|Single Path|Path recalculated each time|
|Order|In order|May need reassembly|
|Layer|(Data) Link Layer|Network Layer|
|Bandwidth|Makes full use of bandwidth|Bandwidth can be shared|
|Error handling|Communication ends incase of an error|Allows packets to be resent|
|Complexity|Simple|More complex|
