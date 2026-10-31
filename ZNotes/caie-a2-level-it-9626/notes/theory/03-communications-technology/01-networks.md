# Communication Technologies

## Networks

### Types of Networks

1. **Local Area Network (LAN)**

   * It is an internal network covering a small geographical area (home, office, school).

   * Restricted to an organisation; access limited to authorised users.

   * **Characteristics:**

     * Covers a small area (usually only a few km).

     * Uses Ethernet (wired) or Wi-Fi (wireless).

     * Operates mainly at OSI layers 1 & 2 (physical & data link).

     * High data transfer speeds (can exceed hundreds of Gbps, though reduced by protocol overhead, collisions, etc.).

     * Installation & maintenance are relatively easy and low-cost.

     * Scalable—devices can be added quickly.

     * Can be extended across buildings via VPNs or combined into a MAN.

   * **Uses**

     * Connects computers, mobile devices, and peripherals.

     * Enables file sharing and resource sharing (printers, storage).

     * Supports sharing of teaching materials, submitting work, and central data access.

     * Businesses can share documents, templates, and applications.

     * Allows centralised storage and easier updates, backups, and security management.

     * Enables internal email, messaging, and monitored internet access.

     * Home LANs support smart homes, shared internet access, and wireless mobility.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Reduces number of peripherals required → lower purchase & running costs

     |
     
     Extending a LAN (e.g., via WAN/VPN links) increases complexity & cost

     ||
     ||
     
     Shared access to a range of printers/devices

     |
     
     Requires a network administrator, raising operational costs & privacy concerns

     ||
     ||
     
     Easy file & data sharing

     |
     
     Malware spreads easily between connected devices

     ||
     ||
     
     Centralised storage → better security, backups, and access control

     |
     
     Storing data on removable devices for privacy defeats LAN benefits & risks of introducing malware

     ||
     ||
     
     Application servers simplify maintenance & updating

     |
     
     ​

     ||
     ||
     
     Internal communication (email) saves time/cost

     |
     
     ​

     ||
     ||
     
     Shared internet connection reduces the number of required public IP addresses

     |
     
     ​

     ||
     ||
     
     Centralised IT management reduces maintenance time and cost

     |
     
     ​

     ||
     ||
     
     Home LANs enable shared internet, smart devices, and Wi-Fi mobility

     |
     
     ​

     ||
     |#
     

2. **Wide Area Networks (WAN)**

   * It connects networks over large geographical distances (cities, countries). Uses public telecommunications systems.

   * **Characteristics of WANs**

     * Uses public or leased telecom lines not owned by the organisation.

     * Covers *much larger* areas than LANs.

     * Operates at OSI layers 1, 2 & 3.

     * Uses long-distance communication media: copper, fibre-optic, microwave, and satellite.

     * Uses routing and switching across multiple nodes (store-and-forward).

     * Less secure than LANs → encryption recommended.

     * Higher chance of transmission errors due to distance & public infrastructure.

   * **Uses of WANs**

     * Connects remote offices across cities/countries.

     * Used by businesses, governments, and educational institutions for global data exchange.

     * The internet is an example of a WAN.

     * Supports email, web platforms, and file sharing worldwide.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Centralises company data/resources → easier backups, updates, and archiving

     |
     
     Very high initial setup costs (distance, specialised technicians)

     ||
     ||
     
     Leased lines/VPNs keep company data private

     |
     
     Remote locations may have fewer resources/security → more vulnerable

     ||
     ||
     
     Supports VoIP, reducing phone costs

     |
     
     Maintenance is more difficult and costly

     ||
     ||
     
     Supports conference calls and video/web conferencing within the organisation

     |
     
     Centralised data centres must run 24/7 (different time zones)

     ||
     ||
     
     ​

     |
     
     Leased line fees & telecom maintenance increase ongoing costs

     ||
     |#
     

3. **Client-server**

   * A network where clients (PCs, laptops, smartphones) request services.

   * Servers provide services such as email, databases, websites, file storage, and printing.

   * Operates using the request–response model. Both client and server must use the same protocols at the application layer (Layer 7).

   * **Characteristics**

     * The client sends a request, and the server sends a response.

     * Clients do not share resources; servers share processing, storage, and applications.

     * The server does not initiate communication; it waits for client requests.

     * Servers can support many clients, prioritising requests with scheduling.

     * Data between client and server may be encrypted.

     * More efficient use of server time because connections are opened only when needed.

     * Not the same as terminals connected to a mainframe, where a persistent connection is maintained.

   * **Uses**

     * Web browsing (web servers send pages to browsers).

     * Email services (the client requests messages from the mail server).

     * Printing through a print server.

     * Uploading/downloading files from file servers.

     * Social media uploads.

     * Accessing corporate databases.

     * Streaming and content-delivery services.

     * Accessing telephony and VPN tunnel services.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Centralised storage of files and applications

     |
     
     Server failure stops services for all clients

     ||
     ||
     
     Only one copy needs updating; easier maintenance

     |
     
     It can be expensive to install and maintain servers

     ||
     ||
     
     Supports many clients at once

     |
     
     Heavy loads can cause slow responses or DoS conditions

     ||
     ||
     
     Better security through authentication and access rights

     |
     
     Requires specialist staff (network admins).

     ||
     ||
     
     Scalable servers can be upgraded without affecting clients

     |
     
     ​

     ||
     ||
     
     Disaster recovery is easier with server backups

     |
     
     ​

     ||
     ||
     
     Can share data across different platforms and mobile devices

     |
     
     ​

     ||
     ||
     
     SQL/DBMS queries can be run consistently from any corporate device

     |
     
     ​

     ||
     ||
     
     Mirroring servers can improve performance

     |
     
     ​

     ||
     |#
     

4. **Peer-to-peer**

   * Connects nodes on an equal basis. No central server; each node can act as both client and server.

   * Resources (storage, bandwidth, and processing power) are shared directly between nodes.

   * Considered a form of distributed computing because nodes share the workload.

   * **Characteristics**

     * Most P2P networks are unstructured.

     * Nodes connect as and when needed (ad hoc).

     * Very robust—nodes can join and leave without causing significant errors.

     * Easy and quick to set up.

     * Nodes organised into a specific topology.

     * Each node maintains a database of nearby nodes and routing information.

     * Uses Distributed Hash Tables (DHTs) for efficient lookup of nodes and resources.

     * When nodes join/leave, disruption occurs until tables are updated.

     * Architecture

       * Decentralised: no server controlling resource sharing.

       * Each node has equal status and shares its own resources.

       * Nodes route data to each other according to the topology (especially in structured systems).

     * Topologies

       * Unstructured topology: random connections between nodes.

       * Structured topology: nodes organised using DHTs or systematic routing tables.

     * P2P protocols allow nodes to query, locate, and transfer files between each other.

     * BitTorrent is the key protocol for large file sharing.

     * Descriptor files, cryptographic hashes, and node-to-node transfers are used.

   * **Uses**

     * Sharing and distributing digital media (eBooks, music, videos, games).

     * File sharing between devices (e.g., AirDrop).

     * Software companies may distribute operating systems via P2P.

     * Searching, locating, and downloading files from multiple nodes.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     No central server; reduced cost and administrative overhead

     |
     
     Security risks: each device must secure itself

     ||
     ||
     
     Quick setup; nodes can be added or removed easily

     |
     
     No central storage: backups must be done individually

     ||
     ||
     
     Robust; node failure rarely disrupts others

     |
     
     Difficult to monitor or prevent illegal file sharing

     ||
     ||
     
     Fast file exchange between devices (e.g., AirDrop)

     |
     
     High network traffic from multiple search and file requests

     ||
     ||
     
     Privacy: no central record of users or activities

     |
     
     Nodes require more processing to handle requests; searches may fail

     ||
     ||
     
     Capacity increases as more nodes share files

     |
     
     File integrity can be compromised — files may be altered by nodes or infected with malware

     ||
     |#
     

5. **Virtual Private Networks**

   * It is a private logical network created over a public telecommunications system such as the internet.

   * It allows users or entire LANs to communicate as if directly connected to the private LAN, regardless of physical location.

   * **Characteristics:**

     * **Topology (Physical & Logical)**

       * Physically uses public networks (mainly the internet).

       * Logically creates a point-to-point private tunnel between two nodes or between a remote device and a LAN.

       * It appears as if the LAN is extended across a public network.

     * **Architecture**

       * Client–server structure: the user device (client) connects to a VPN server/gateway.

       * User IP address and data appear to originate from the VPN server.

       * Requires authentication (username/password, biometrics, dongle, two-factor, digital certificates).

       * Uses encryption and integrity checking to keep data secure.

       * Can connect multiple LANs to form a WAN.

       * Basic VPNs may not support all LAN protocols; commercial VPNs usually do.

   * **Uses**

     * Remote employees access company files, databases, and shared drives as if inside the office LAN.

     * Allows centralisation of organisational resources in data centres.

     * Remote users can access printers, servers, VoIP equipment, and other LAN-based peripherals.

     * Provides secure data transfer between home networks and corporate LANs.

     * Used to transmit sensitive/confidential information securely.

     * VPNs hide user identity and prevent ISP throttling, improving P2P file transfer speeds.

     * May help avoid ISP monitoring (though this can raise legal/ethical issues).

     * Encrypts all data in transit; protects privacy when using public Wi-Fi.

     * Masks or changes the IP address; allows anonymous browsing.

     * Blocks tracking from ISPs and other entities.

     * Can block advertisements to improve user experience and reduce data usage.

     * Allows secure transmission of data across public networks.

     * Enables the use of unsupported protocols (e.g. IPv6 over IPv4 networks).

     * Can bypass firewall rules by encapsulating traffic.

     * Provides secure VoIP calls.

     * Employees can use corporate VoIP systems from anywhere.

     * Can bypass geo-restrictions to access region-locked content and news.

     * Can bypass censorship in countries with restricted internet.

     * Avoids ISP bandwidth throttling, improving quality of media streams.

     * Some providers block VPNs to enforce copyright compliance.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Encryption protects data during transmission

     |
     
     May be illegal in some countries; users risk prosecution

     ||
     ||
     
     Ensures privacy of browsing history and online activity

     |
     
     Reduced performance due to encryption overhead and routing through VPN servers

     ||
     ||
     
     Hides/changes IP address → anonymous use of the internet

     |
     
     Some VPNs are complex to set up, requiring technical expertise

     ||
     ||
     
     Prevents ISP inspection and bandwidth throttling

     |
     
     Compatibility issues may arise across different devices/OS versions

     ||
     ||
     
     Allows employees to securely access company LANs remotely (cheaper than leased lines)

     |
     
     Older or legacy systems may not support VPN technology

     ||
     ||
     
     Enables access to geo-restricted content and services

     |
     
     Free VPN providers may log or sell user data → privacy not guaranteed

     ||
     ||
     
     Provides secure use of public Wi-Fi

     |
     
     Some streaming/content services block VPN traffic and may disable user accounts

     ||
     ||
     
     Supports secure VoIP communication

     |
     
     VPN server outages or changes can cause loss of access

     ||
     ||
     
     Centralises organisational resources → reduced maintenance and improved security

     |
     
     ​

     ||
     |#
     

6. **Mobile Networks**

   * These are wireless networks made up of multiple radio base stations, each covering a small geographical area called a cell.

   * They allow mobile devices (phones, tablets, IoT, etc.) to communicate and access services while moving.

   * **Characteristics**

     * Topologies (Physical and Logical)

       * Cells arranged to provide coverage (often drawn as hexagons).

       * Base stations mounted on towers, buildings, poles.

       * Urban areas → small cells; rural areas → large cells.

       * Directional antennae used to target specific areas.

       * Devices connect wirelessly to the nearest base station.

       * Seamless handoff between cells as the user moves.

       * Frequency reuse: adjacent cells use different frequencies to prevent interference.

     * Architecture

       * Base stations link to the public telecommunications network for voice calls.

       * A packet-switched network carries mobile data to and from the internet.

       * Switching systems manage movement between cells and free frequencies.

       * Uses spread-spectrum techniques and frequency hopping to avoid interference.

       * Multiplexing lets multiple calls/data streams share the same channel.

       * Cell size and performance depend on frequency:

         * Low frequencies → long range, low capacity (good for rural).

         * High frequencies → short range, high capacity (good for cities).

   * **Uses**

     * Employees can remotely access company resources, cloud storage, emails and files.

     * Delivery companies can share tracking data with central systems.

     * Access to corporate peripherals (e.g., VoIP phones, remote software, ticketing systems) via mobile connectivity.

     * Mobile users can send/receive data, messages, emails, cloud updates.

     * Devices automatically switch between cells without losing sessions.

     * Users can access P2P services via mobile data (subject to provider policies).

     * Higher frequencies and 5G support high-capacity data exchange.

     * Mobile internet for browsing, social media, cloud services.

     * Allows use while travelling (cars, buses, trains).

     * Enables GPS navigation to receive traffic and weather updates via mobile data.

     * Mobile networks may use packet tunnelling internally when moving data between cells or through intermediate systems.

     * Used for switching between base stations and managing congestion.

     * Voice calls, SMS, MMS delivered over circuit-switched or VoIP systems.

     * Seamless roaming across cells enables uninterrupted call movement.

     * Streaming video/music, downloading software, app updates.

     * 5G supports UHD video on demand, real-time cloud gaming, and other high-bandwidth services.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Allows calls, messaging, and internet access while on the move

     |
     
     Wireless signals can be intercepted → must encrypt sensitive data

     ||
     ||
     
     No need for a fixed physical connection

     |
     
     Many apps (social media, email) may not encrypt data securely

     ||
     ||
     
     Contactless payment possible (e.g., mobile card readers, NFC)

     |
     
     Costs can be high depending on tariffs (data, calls, texts)

     ||
     ||
     
     Employees can work remotely, travel, or work from hotels

     |
     
     Coverage Issues:

     * Buildings, tunnels, and certain materials block signals

     * Rural and low-population areas may have poor or no signal

     * Hills/terrain cause interference

     ||
     ||
     
     GPS devices and delivery trackers can send location data back through mobile networks

     |
     
     Identity, tracking, and cyber-attack risks increase with more connectivity

     ||
     ||
     
     Low-latency communication (for robotics, self-driving cars)

     |
     
     5G Specific Disadvantages:

     * Requires more cell towers, increasing cost

     * Radio frequencies may be crowded or interfere with existing uses

     * Many devices do not support 5G, requiring upgrades

     * High infrastructure costs and technician training needed

     * More devices connected → larger attack surface

     ||
     ||
     
     High bandwidth for dense urban areas

     |
     
     ​

     ||
     ||
     
     Potential replacement for land-line internet

     |
     
     ​

     ||
     |#
     
