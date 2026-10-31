## Network Servers

### Types of Network Servers

1. **File servers**

   * A computer or NAS device that centrally stores files and folders and provides access to them over a network.

   * It acts as a remote hard disc, allowing users to retrieve and store files without physical transfer of storage media.

   * Provide centralised storage for users on a LAN in schools, businesses, and organisations.

   * Enable file sharing between multiple client devices such as desktops, laptops, and tablets.

   * Improve data security, organisation, and management compared to storing files locally on individual devices.

   * Operate using a request and response model:

     * Clients send a request to access or store a file.

     * The file server authenticates the user and responds by sending or saving the requested file.

   * File servers only store and supply files; they do not process data for clients.

   * Use standard file access protocols such as SMB, NFS, and AFP to present files as network drives.

   * Often use authentication and access rights to control who can access specific files.

   * Reliability is increased using RAID, which protects data against disc failures.

   * In large organisations, file servers may be part of server farms to provide high capacity, continuous operation, and ease of administration.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Centralised storage simplifies backup, security, and administration

     |
     
     Dependence on the server means failure can disrupt access for all users

     ||
     ||
     
     Users can access files from any networked device

     |
     
     High-capacity, reliable servers can be expensive to purchase and maintain

     ||
     ||
     
     Large storage capacity at a low cost per gigabyte using magnetic hard discs

     |
     
     Performance may be affected if many users access files simultaneously

     ||
     ||
     
     RAID improves data protection and reliability

     |
     
     Usually limited to access within a LAN and not accessible over the internet like cloud storage

     ||
     ||
     
     Network drives behave like local storage, making them easy to use

     |
     
     ​

     ||
     |#
     

2. **Web Server**

   * Stores websites made up of linked web pages and related resources.

   * A single web server can host multiple websites.

   * Website content can be static or dynamically generated to meet user requests.

   * Enable users to access websites over a network or the internet.

   * Respond to requests from client devices (web browsers) by delivering requested web content.

   * Allow remote configuration of devices such as printers, routers, and webcams through embedded web servers.

   * Enable users to access websites over a network or the internet.

   * Respond to requests from client devices (web browsers) by delivering requested web content.

   * Allow remote configuration of devices such as printers, routers, and webcams through embedded web servers.

   * HTTPS encrypts data between client and server; HTTP does not.

   * Server responses include:

     * A status code (e.g. 200 success, 308 redirect, 404 not found)

     * Information about the server, cookies, and resource exchange

     * The requested web content

   * In large systems, web servers operate within server farms to handle many simultaneous client requests efficiently.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Allow fast and centralised access to websites for many users

     |
     
     High traffic can reduce performance without sufficient server resources

     ||
     ||
     
     Support dynamic content, improving user experience

     |
     
     Require careful configuration to maintain security

     ||
     ||
     
     Server-side scripting improves security and speed

     |
     
     Dependence on network connectivity for access

     ||
     ||
     
     HTTPS provides secure data transmission

     |
     
     Server-side failures can make websites unavailable to users

     ||
     ||
     
     Can be embedded in devices for remote management

     |
     
     ​

     ||
     |#
     

3. **Mail Servers**

   * A network server that manages the sending, receiving, storing and forwarding of email messages.

   * Works with mail clients (email applications or web browsers) using a client–server model.

   * Consists of:

     * SMTP servers for sending outgoing emails

     * POP3 or IMAP servers for retrieving incoming emails

   * Enable users to send and receive emails across local networks and the internet.

   * Store email messages until they are collected by the recipient’s mail client.

   * Route emails between different mail servers using domain information resolved by DNS.

   * A mail client sends an email using SMTP to the sender’s mail server.

   * The server resolves the recipient’s domain using DNS and forwards the email to the recipient’s mail server.

   * The recipient’s mail server stores the message in the inbox.

   * The mail client retrieves the message using POP3 or IMAP.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Centralised handling of email communication

     |
     
     Emails stored on servers are often unencrypted, posing security risks

     ||
     ||
     
     IMAP allows access to emails from multiple devices

     |
     
     Messages may remain on intermediate servers even after deletion

     ||
     ||
     
     Mail servers can store emails for long periods

     |
     
     POP3 limits access to a single device and deletes emails from the server

     ||
     ||
     
     Efficient routing of emails using DNS and SMTP

     |
     
     Long-term storage of emails increases exposure to unauthorised access

     ||
     |#
     

4. **Application Server**

   * Software that stores, manages and delivers applications to users over a network.

   * Clients access applications using a web browser; the application runs on the server.

   * No installation of the application is required on the client device

   * Provide users with access to centrally managed applications.

   * Act as an interface between users and backend business applications or databases.

   * Allow organisations to deploy bespoke business applications securely and efficiently.

   * Often operate in the same environment as web servers for web-based applications.

   * Use the request and response model:

     * A client sends a request via a web browser.

     * The application server runs the requested application on the server.

     * The output is sent back and displayed in the client’s browser.

   * Application servers handle user interactions, data processing and communication with backend databases.

   * Support high-performance applications used by many users simultaneously.

   * In large systems, application servers operate within server farms, providing:

     * Load balancing to distribute requests

     * Failover to maintain service during failures

     * Clustering to improve reliability and performance

   * Can use multiple communication protocols, unlike web servers, which mainly use HTTP/HTTPS.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Centralised management and maintenance of applications

     |
     
     High setup and maintenance costs

     ||
     ||
     
     Increased security for applications and user data

     |
     
     Performance depends heavily on server resources

     ||
     ||
     
     No client-side installation required

     |
     
     Server failure can affect many users if redundancy is not in place

     ||
     ||
     
     High performance for applications with many simultaneous users

     |
     
     Requires reliable network connectivity for access

     ||
     ||
     
     Improved reliability through clustering and failover

     |
     
     ​

     ||
     |#
     

5. **Print Servers**

   * A server that collects print jobs from client devices and sends them to printers on a network.

   * Clients can include desktops, laptops, smartphones and other devices that support printing.

   * Can be a dedicated computer system, a small network device or a plug-in board.

   * Provide centralised management of printing for multiple users.

   * Allow efficient sharing of printers in organisations.

   * Reduce the need for printers for each user by enabling many clients to use fewer printers.

   * Manage printer access and enforce printing policies in large organisations.

   * Use the request and response model:

     * Client devices send print jobs to the print server using printing protocols.

     * The print server processes the request and forwards it to the selected printer.

   * Use protocols such as:

     * Microsoft Network Printing Protocol

     * Internet Printing Protocol (IPP)

     * Line Printer Daemon (LPD)

   * Can manage multiple printers and direct jobs to the correct one.

   * Print jobs are placed into queues and sent to printers in turn.

   * Queues can be managed to:

     * Pause or reorder jobs

     * Delete jobs

     * Enforce printing policies

     * Record printing activity for monitoring or accounting

   * Can add information such as watermarks or user details to printed documents.

   * In large organisations, print servers may be part of server-based systems managing high volumes of requests.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Efficient use of printers in large organisations

     |
     
     Users may have limited control over printer features (e.g., paper tray selection)

     ||
     ||
     
     Centralised control and monitoring of print jobs

     |
     
     Users may not receive immediate notifications if print jobs fail

     ||
     ||
     
     Supports a large number of client devices

     |
     
     Print server failure can prevent all users from printing

     ||
     ||
     
     Enables policy enforcement and job tracking

     |
     
     More complex to manage than simple printer sharing in small networks

     ||
     ||
     
     Reduces hardware costs by sharing printers

     |
     
     ​

     ||
     |#
     

6. **FTP Server**

   * Stores files and allows clients to upload and download files using FTP.

   * Can store almost any type of computer file. It may be a dedicated file storage system or software running on an existing server

   * FTP server software can run alongside other services, for example, on a web server.

   * Provide centralised file transfer services between clients and servers.

   * Allow users to share, distribute and retrieve files remotely.

   * Commonly used to distribute:

     * Operating systems and updates

     * Software applications

     * Documentation and large files

   * Can allow authenticated or anonymous access for downloading files.

   * Use a client–server, request and response model.

   * FTP works at the Application layer of the OSI model and is part of the TCP/IP suite.

   * Clients connect using FTP software and send requests to:

     * Upload files

     * Download files

     * Manage files on the server

   * Uses a control connection on port 21 to manage commands.

   * Supports:

     * Active mode

     * Passive mode, which is useful for clients behind firewalls

   * Requires users to log in using:

     * A username and password, or

     * Anonymous login

   * Once authenticated, the server opens a session for file transfer.

   * Some FTP servers support checkpoint/restart, allowing interrupted downloads to resume.

   * FTP servers respond only to FTP requests.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Efficient for transferring large files

     |
     
     Not secure by default:

     * Usernames, passwords and data are transmitted in plain text

     ||
     ||
     
     Supports resumable downloads

     |
     
     Requires additional security methods such as:

     * FTPS

     * VPN connections

     ||
     ||
     
     Allows controlled access through authentication

     |
     
     Requires users to log in, making access slower than HTTP downloads

     ||
     ||
     
     Can be used for large-scale software distribution

     |
     
     Can be difficult to use through firewalls.

     ||
     ||
     
     Anonymous access simplifies public downloads

     |
     
     ​

     ||
     |#
     

7. **Proxy Servers**

   * An intermediary server positioned between clients and other servers.

   * It intercepts client requests and forwards them to destination servers, then returns responses to clients.

   * Can operate as:

     * A forward proxy (between clients and the internet)

     * A reverse proxy (between clients and internal servers, e.g. web servers)

   * Act as a go-between for clients and servers, hiding client details from external systems.

   * Provide content filtering to control or restrict access to websites.

   * Improve security and privacy by hiding client IP addresses using NAT.

   * Speed up access by caching frequently accessed content.

   * Used widely in schools, colleges and large organisations to monitor and control internet usage.

   * Reverse proxies protect internal servers and improve performance.

   * Use a request and response communication model.

   * Client requests are:

     * Intercepted by the proxy

     * Analysed and processed

     * Forwarded to the destination server using the proxy’s IP address

   * Server responses are:

     * Returned to the proxy

     * Analysed, filtered or cached

     * Sent back to the client

   * Network administrators can configure proxies to:

     * Block inappropriate content

     * Authenticate users

     * Log web activity

     * Filter traffic using URL and DNS blacklists

   * Reverse proxies:

     * Distribute requests across multiple servers (load balancing)

     * Cache static content to reduce server load

     * Work with firewalls to protect internal servers from attacks

   * Clients are often unaware a reverse proxy is being used.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Hides client IP addresses, improving privacy and security

     |
     
     Can introduce delays, as all traffic must pass through the proxy

     ||
     ||
     
     Improves performance through caching

     |
     
     Cached content may become outdated, leading to inaccurate information

     ||
     ||
     
     Provides logging and monitoring of internet usage

     |
     
     Some services (e.g. FTP and VoIP) may not function correctly due to IP address changes

     ||
     ||
     
     Helps protect internal servers from malicious attacks

     |
     
     Firewalls may reject or drop connections because of altered IP addresses

     ||
     ||
     
     Can reduce server load and improve response times

     |
     
     Users may not be aware when cached or filtered content affects accuracy

     ||
     |#
     

8. **Virtual Servers**

   * Software-based server that runs on shared physical hardware.

   * Multiple virtual servers operate on a single high-performance physical server. Each virtual server runs its own operating system and server software.

   * Different operating systems and server applications can run simultaneously on the same machine.

   * Provide server functionality (e.g. web, file, application, print servers) without requiring separate physical machines.

   * Allow organisations to host multiple services efficiently using shared hardware.

   * Commonly used in server farms and data centres.

   * Widely used for web hosting, where many websites run on one physical server, each with its own IP address and URL.

   * Use the request and response model between clients and servers.

   * Client requests are directed to the appropriate virtual server based on IP address or service.

   * Virtual servers share physical resources such as CPU, RAM, storage and network interfaces.

   * Administration is usually performed remotely via web interfaces or terminal software.

   * Physical servers are typically rack-mounted with no local peripherals.

   * Virtual servers operate alongside others within server farms.

     #|
     ||
     
     Advantages

     |
     
     Disadvantages

     ||
     ||
     
     Reduced hardware costs by running multiple servers on one physical device

     |
     
     If the physical server fails, all virtual servers hosted on it are affected

     ||
     ||
     
     Efficient use of resources such as CPU and memory

     |
     
     Performance may degrade if too many virtual servers compete for resources

     ||
     ||
     
     Easy to deploy, manage and scale server services

     |
     
     Requires powerful hardware and skilled administration

     ||
     ||
     
     Different operating systems and applications can coexist safely

     |
     
     Security risks if one virtual server is compromised and isolation is weak

     ||
     ||
     
     Simplifies maintenance and centralised management

     |
     
     ​

     ||
     ||
     
     Ideal for web hosting and large organisations with many services

     |
     
     ​

     ||
     |#
     
