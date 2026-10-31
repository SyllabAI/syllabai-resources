## Digital Certification

### Digital Certificate

1. An organization sends a request to Certificate Authority (CA).
2. They send their public key, information to prove their identity as well as any additional information required by the CA.
3. The CA then verifies their identity and then issues the certificate after encrypting it with their private key.

### Digital Signature

The message is put through a hashing algorithm to produce the digest. This is then encrypted with the sender’s private key. This is the digital signature.

When the message is received, the digital signature is then decrypted with the sender’s public key. The decrypted message is put through the same hashing function to output a digest. The two digests are compared and if they are the same then the message was not tampered with.