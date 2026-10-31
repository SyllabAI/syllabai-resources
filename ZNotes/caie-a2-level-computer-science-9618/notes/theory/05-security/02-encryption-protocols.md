## Encryption Protocols

### Purpose

- Allow for more security when communicating over the internet as it allows two parties identify and verify each other and communicate confidentially with integrity
- Provides encryption.

### Working

- An SSL/TLS connection is initiated between two applications.
- The one initiating it is the client. The one receiving it is the server.
- Session begins with a handshake.
- Server sends its digital certificate and public key
- Client confirms the server’s identity.
- Encryption algorithm is agreed upon and the symmetric session keys are generated.

### Use Cases

- Transmitting passwords or session cookies.
- Online shopping and banking websites.

### Transport Security Layer (TLS)

TLS is a cryptographic protocol designed to provide secure, encrypted communication and authentication over a data network (e.g., HTTPS). It operates between the Transport Layer and the Application Layer of the TCP/IP stack.

* TLS is split into two protocols to manage security

  * **The TLS Handshake protocol**: This layer handles the establishment of the secure connection before any actual application data is transmitted. Authenticates the server and the client and negotiates cryptographic algorithms

    * The client and server agree on the Cipher Suite (encryption algorithms to use).

    * The server sends its Digital Certificate containing its public key.

    * The client verifies the certificate against a trusted Certificate Authority (CA).

    * They securely exchange parameters to generate temporary, symmetric Session Keys used for data encryption.

  * **The TLS Record protocol**: This layer handles the secured transmission of the actual application data during the session. Encrypts, fragments, and verifies data packet integrity.

    * Takes data from the application layer and breaks it into manageable blocks.

    * Compresses the data (optional).

    * Applies a Message Authentication Code (MAC) or hash to ensure data integrity (prevents tampering).

    * Encrypts the block using the symmetric session key established during the Handshake.

#|
||

SSL

|

TSL

||
||

Connects directly via port numbers

|

Connects via a standard port and then upgrades to secure mode via explicit commands

||
||

Closes the connection immediately without sending warning codes

|

Uses specific, encrypted alert codes to explain network or certificate errors

||
||

Supports older, weak encryption algorithms (e.g., DES, RC4)making it vulnerable to attacks

|

Supports strong, modern cryptographic algorithms (e.g., AES, ChaCha20).

||
|#

$$
\text {Table: Differences between SSL and TSL}
$$

### Session Caching

The TLS handshake is computationally expensive and time-consuming because it uses asymmetric cryptography which requires heavy CPU processing to set up keys.

* **Session Caching:** A performance optimization mechanism where the server and client store (cache) the parameters of a recently established TLS session for a specific period of time.

* **How it works:**

  * If a user reconnects to the server shortly after disconnecting, the client passes a cached Session ID or Session Ticket back to the server.

  * If the server recognizes it, it skips the full asymmetric handshake and immediately resumes encryption using the pre-existing session keys.

* **Why it is needed:**

  * Reduces Latency:Decreases network round-trips, making page loads faster.

  * Saves CPU Resources: Minimizes the computational overhead on the server, allowing it to handle thousands of concurrent secure connections easily.