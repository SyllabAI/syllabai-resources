# Security

## Encryption

The process of converting of data into an unreadable format.

### Plain Text

Data before applying encryption.

### Cipher Text

Data after applying encryption.

### Key Encryption:

- To ensure a message is authentic.
- To ensure a message isn’t altered during transmission.
- To ensure that only the intended receiver can understand the message.
- To ensure that neither send nor receiver can deny involvement in the transmission.

### Public Key

A public key is shared. It is used to encrypt data so that it can be decrypted with its matching private key.

### Private Key

A private key is never shared. It is used to decrypt data that was encrypted with its matching public key.

### Symmetric Encryption

A single key is used for both encryption and decryption. The key is shared between the sender and the receiver.

**Disadvantages:**

- Key has to be exchanged securely.
- Once compromised, it can decrypt sent and received messages.
- Cannot ensure origin or integrity of data.

### Asymmetric Encryption

Two keys are used: public key and private key. The message is encrypted with the public key and decrypted using the matching private key.

### Symmetric VS Asymmetric


||Symmetric|Asymmetric|
|:---|:---|:---|
|Number of Keys|1 key for both|2 keys|
|Is Key Shared|Yes|Only public key|
|Security|Less secure as key needs to be shared|More secure|
|Complexity|Simple|Complex|
|Speed|Fast|Slow|
|Key Length|Short|Longer|

**Security concerns relating to a transmission:**

* Confidentiality: Only the intended recipient should be able to decrypt the message.
* Authenticity: Receiver must know who sent the ciphertext.
* Integrity: Message must not be modified during transmission.
* Non-repudiation: Neither the sender nor the receiver should be able to deny involvement in the transmission.

### Quantum Cryptography

Quantum Cryptography is used to produce a virtually unbreakable encryption system using the properties of photons.

**Advantages:**

- More secure.
- Eavesdropping can be detected.
- Longer keys can be used.
- Almost un-hackable.
- Cannot be copied and decrypted at a later time.

**Disadvantages:**
- Only works for short distances.
- High cost for maintenance and setup.
- Lacks important features like digital signature, certified mail etc.
- High error rate due to being new.
- Polarization of light may be altered during transmission.