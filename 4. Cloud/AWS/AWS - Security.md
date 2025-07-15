What is a cryptographic key?

- Sequence of characters used in encryption algorithm, to alter a sensitive data.
- Data is called plaintext and encrypted data is ciphertext.
- Plaintext + Key = Ciphertext

---

TYPES OF ENCRYPTION

Symmetric Encryption: Same key is used for encryption and decryption

Asymmetric Encryption: Two keys - Public key and private key

---

HTTPS website:

- SSL/TLS encryption protocol used in HTTPS, uses asymmetric encrption.
- The public key is present in website's SSL certificate and private key is installed on the origin server.
- The generation of this public and private keys happens during TLS handshake when a session is created.

---

What is key rotation?

- Replacing a key by generating a new key. It is used to limit the amount of data encrypted by a single key. Something like changing password of your account after some fixed number of months.

---

Online key generation and encryption:
1] https://travistidwell.com/jsencrypt/demo/
2] https://www.javainuse.com/rsagenerator
3] https://generate-random.org/encryption-key-generator

---

What is encoding vs encrypting?
Encoding:

- Used to convinently transfer data across computers in such a format that it can be easily used by different types of systems. Convert data into some common format.
- Does not use any key. Just an encoding algorithm.
- Less secure
- Eg: ASCII, UNICODE, URL Encoding,Base64 encoding

Encrypting:

- Used to alter sensitive data in such a way that only intended system can understand it and unintended systems will find it meaningless.
- Uses keys and encryption algorithms.
- More secure
- Eg: RSA, AES 256

---

Envelop Encryption:

- For objects upto 4KB, use AWS KMS. For greater than 4 KB, use envelop encryption.

Encryption process:

1. Generate a plaintext data key.
2. Encrypt plaintext data with a data key, then encrypt the data key using CMK (Customer Master Key).
3. AWS KMS helps you protect your master keys by storing and managing them securely. Master keys stored in AWS KMS, known as customer master keys (CMKs)
4. Encrypted data key and cipher text are stored together.

Decryption process:

1. Use the Decrypt operation to decrypt the encrypted data key. The operation returns a plaintext copy of the data key.
2. Use the plaintext data key to decrypt data locally, then erase the plaintext data key from memory.

---

1. Client side encryption - Envelop encryption
2. Server side encrption: Encryption at rest

- Amazon S3 managed keys (SSE-S3)
- AWS KMS managed keys (SSE-KMS) - uses customer master keys (CMKs) to encrypt your Amazon S3 objects
- Customer Provided keys (SSE-C)

3. Encryption in transit/in flight - Use SSL/TLS - use https protocol - aws:SecureTransport

---

Headers:
SSE-KMS:

1. x-amz-server-side-encryption: "aws:kms"
2. x-amz-server-side-encryption-aws-kms-key-id: If the header is not present in the request, Amazon S3 assumes the default KMS key.

SSE-S3:

1. x-amz-server-side-encryption: "AES256"

SSE-C:

1. x-amz-server-side-encryption-customer-algorithm
2. x-amz-server-side-encryption-customer-key
3. x-amz-server-side-encryption-customer-key-MD5

---

APIs:

- GenerateDataKey - to generate a key in kms
- Plaintext field contains plaintext format of key and CiphertextBlob contains encrypted format of key
- GenerateDataKeyWithoutPlaintext - returns only encrypted format key
- CreateKey : Use to generate CMK

---

1. What is salting?

- Adding a random sequence of characters, called salt, before or after the password.
- Just like we add salt to food to enhance it's taste, we salt a password to enhance it or make it stronger.
- After salting, the password is hashed.

2. What is hashing?

- Hashing is a one-way process that converts a password to ciphertext using hash functions or algorithms.
- Hashes of passwords cannot be transformed back to the original plaintext password.
- Server never stores password, it stores hash of the password.
- While login, the server calculates hash of the entered password and compares it with hash stored on server. If both hashes are equal, user is logged in sucessfully.

3. What is Hash-based Message Authentication Code (HMAC)?

- SSE-C - Does not store the encryption key.
- It stores in a randomly salted HMAC value of the encryption key.
- The salted HMAC value cannot be used to derive the value of the encryption key or to decrypt the contents of the encrypted object.
- That means, if you lose the encryption key, you lose the object.

4. Scrambling or randomizing the data?

---
