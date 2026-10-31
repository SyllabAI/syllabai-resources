## **Network Protocols**

### **Definition and Purpose**

* **Protocol:** A set of rules that governs how data is formatted, transmitted, and received across a network.

* **Necessity:** Protocols ensure that different devices (made by different manufacturers) can communicate seamlessly by providing a standardised "language."

### **Transport & Internet Protocols**

#|
||

Protocol

|

Full name

|

Purpose & Key Features

||
||

**TCP**

|

Transmission Control Protocol

|

Connection-oriented. Uses a "3-way handshake". Provides reliability via sequence numbers and retransmission of lost packets. Includes flow control (windowing) to prevent overwhelming the receiver.

||
||

**UDP**

|

User Datagram Protocol

|

Connectionless\*\*.\*\* Lightweight with no handshake. No error recovery or flow control. Best for real-time apps (gaming, VoIP, and streaming), where speed is prioritised over 100% accuracy.

||
||

**IP**

|

Internet Protocol

|

Responsible for addressing and routing packets across network boundaries. Defines the path data takes from source to destination.

||
||

**ICMP**

|

Internet Control Message Protocol

|

Used for error reporting and diagnostics (e.g., the `ping` command). It sends feedback about network connectivity or unreachable destinations.

||
||

**ARP**

|

Address Resolution Protocol

|

Maps a known IP address to a physical MAC address on a local network so a frame can be delivered to the specific NIC.

||
|#

### **Application Layer Protocols**

#|
||

Protocol

|

Purpose

|

Use Case

||
||

**HTTP/HTTPS**

|

Hypertext Transfer Protocol (Secure)

|

HTTPS uses TLS/SSL to encrypt data, ensuring privacy and integrity during web browsing.

||
||

**FTP**

|

File Transfer Protocol

|

Used for uploading/downloading large files. Supports authentication (username/password).

||
||

**SMTP**

|

Simple Mail Transfer Protocol

|

Used for sending emails from a client to a server or between servers.

||
||

**POP3**

|

Post Office Protocol v3

|

Downloads email to a local device and usually deletes it from the server. Best for single-device use.

||
||

**IMAP**

|

Internet Message Access Protocol

|

It keeps emails on the server and synchronises changes across multiple devices (ideal for smartphones).

||
||

**SSH**

|

Secure Shell

|

Provides a secure, encrypted command-line interface for remote management.

||
||

**Telnet**

|

Telecommunication Network

|

Older remote login protocol. Unsecure because data (including passwords) is sent in plain text.

||
|#

### **Network Addressing & Routing**

MAC vs. IP Addressing

* **MAC Address:** A unique 48-bit physical identifier assigned to a NIC by the manufacturer. Used for communication within a LAN.

* **IP Address:** A logical address assigned by the network.

  * **IPv4:** 32-bit (e.g., 192.168.1.1). Approximately 4.3 billion addresses.

  * **IPv6:** 128-bit (hexadecimal). Developed to solve the exhaustion of IPv4 addresses.

#### **Static vs. Dynamic Routing**

#|
||

Feature

|

Static Routing

|

Dynamic Routing

||
||

**Configuration**

|

Manually set by an administrator.

|

Automatically updated by protocols/algorithms.

||
||

**Adaptability**

|

Does not change if a link fails.

|

Adapts to congestion, outages, or link failures.

||
||

**Resources**

|

Low CPU/RAM usage.

|

Higher overhead occurs because routers must communicate with each other.

||
||

**Usage**

|

Small, simple networks.

|

Large, complex networks (the Internet).

||
|#

### **Gateway Protocols**

* **Autonomous systems (AS)**: Before understanding the protocols, you must define an autonomous system. It is a collection of connected IP routing prefixes under the control of a single administrative entity (like an ISP, a large university, or a corporation) that presents a common routing policy to the Internet.

* **Interior Gateway Protocols (IGP)**

  **Definition:** Protocols used to exchange routing information within a single Autonomous System (internal network).

  * **Primary Function:** To calculate the most efficient path between nodes inside the same network boundary.

  * **Key Metrics (Cost Factors):** IGPs determine the "best path" using metrics like bandwidth, delay, reliability, and hop count.

  * **Common Examples:**

    * **RIP (Routing Information Protocol):** Uses "hop count" as a metric (maximum 15 hops). It is simple but slow to converge (update).

    * **OSPF (Open Shortest Path First):** Uses a "link state" algorithm. It is more complex but faster at adapting to network changes than RIP.

    * **IS-IS:** Used mainly by large service providers within their infrastructure.

* **Exterior Gateway Protocols (EGP)**

  **Definition:** Protocols used to exchange routing information between different autonomous systems.

  * **Primary Function:** To allow different networks (e.g., Google’s network and Comcast’s network) to communicate and share reachable IP addresses.

  * **Focus:** While IGPs focus on speed/efficiency, EGPs focus on network reachability and administrative policies.

  * **Evolution:** The original protocol named "EGP" is now obsolete; it has been replaced entirely by BGP.

* **Border Gateway Protocol (BGP)**

  **Definition:** The current standard EGP used to exchange routing and reachability information among ASes on the internet.

  * **The "Glue" of the Internet:** BGP makes the internet work by allowing routers to look up which ISP owns which IP address range.

  * **Path-Vector Routing:** Unlike IGPs, which look at "speed," BGP looks at the path. It maintains a list of the ASes that a packet must pass through to reach a destination.

  * **Key Functions for 9626 Theory:**

    * **Loop Prevention:** By tracking the list of ASes in a path, BGP ensures a packet doesn't get stuck in an infinite loop between two providers.

    * **Policy-Based Routing:** Allows ISPs to choose routes based on business agreements or security, rather than just the shortest physical distance.

    * **Load Balancing:** Can distribute traffic across multiple paths to prevent any single link from becoming a bottleneck.

  * **Security Note:** BGP is notoriously vulnerable to "BGP hijacking," where a rogue AS claims to own an IP range that it doesn't, causing traffic to be redirected.

### **Protocol Layering: OSI against TCP/IP**

#|
||

OSI Model (7 Layers)

|

TCP/IP Model (4 Layers)

|

Key Functions

||
||

**Application, Presentation, Session**

|

**Application**

|

User interfaces, data encryption/compression, session management.

||
||

**Transport**

|

**Transport**

|

End-to-end communication (TCP/UDP), error recovery.

||
||

**Network**

|

**Internet**

|

Routing and IP addressing.

||
||

**Data Link, Physical**

|

**Network Access**

|

Physical transmission and MAC addressing.

||
|#

### **Key Differences**

1. **Complexity:** OSI is a theoretical 7-layer model; TCP/IP is a practical 4-layer model used by the Internet.

2. **Reliability:** OSI's Transport layer only provides connection-oriented links, whereas TCP/IP's Transport layer handles both (TCP and UDP).

3. **Layers:** OSI separates physical hardware (Physical) from data framing (Data Link); TCP/IP combines them.

### Switching Methods

* **Packet Switching:** Data are broken into packets with headers (IP, sequence numbers). Packets take different routes and are reassembled at the destination.

* **Circuit Switching:** A dedicated physical path is established for the duration of the connection (e.g., a traditional phone call). Guaranteed bandwidth but inefficient.

* **Message Switching:** "Store and forward." The entire message is sent to a node, stored, and then sent to the next node.

#### **Use of Firewalls**

* A firewall is a hardware device, software application, or combination of both that monitors and controls network traffic.

* It acts as a security barrier between a trusted internal network (LAN) and untrusted external networks such as the internet.

* Used to prevent unauthorised access to a network while allowing legitimate communications.

* Protects networks from cyber threats such as hacking attempts, malware, viruses, and denial-of-service attacks.

* Can monitor both incoming and outgoing traffic.

* Often used in homes, schools, businesses, and organisations to improve network security.

#### **Configuration of Firewalls**

* Firewalls operate using a set of **rules or policies** configured by a network administrator.

* Rules determine whether traffic is:

  * **Allowed (accepted)**, or

  * **Blocked (denied)**.

* Rules can be based on:

  * IP addresses (source or destination)

  * Port numbers

  * Protocols (e.g. HTTP, HTTPS, FTP)

  * Applications or services

  * User accounts or groups

#### **Methods Used by Firewalls**

* **Packet filtering**

  * Examines packet headers.

  * Checks source/destination IP addresses, ports, and protocols.

  * Allows or blocks packets according to configured rules.

* **Stateful inspection**

  * Keeps track of active connections.

  * Allows packets that belong to an established session.

  * Blocks unexpected or suspicious packets.

* **Proxy firewall**

  * Acts as an intermediary between clients and external servers.

  * Receives requests, checks them, then forwards approved requests.

  * Can filter content and hide internal IP addresses.

* **Application-layer filtering**

  * Examines the contents of network traffic.

  * Can block specific applications, websites, or services.

#### **Controlling Access to Networks**

* Restricts access to authorised users and devices only.

* Blocks access to prohibited websites or services.

* Prevents unauthorised external connections to internal devices.

* Can restrict employee or student access to certain internet resources.

* May be configured to allow remote access only through secure connections such as VPNs.

* Logs network activity for monitoring, auditing, and security investigations.

#### **Advantages**

* Improves network security.

* Reduces risk of unauthorised access.

* Helps prevent malware infections.

* Allows administrators to enforce security policies.

* Provides monitoring and logging of network traffic.

#### **Disadvantages**

* Incorrect configuration can block legitimate traffic.

* May reduce network performance due to traffic inspection.

* Requires ongoing maintenance and updates.

* Cannot protect against all threats, especially those originating from authorised users within the network.