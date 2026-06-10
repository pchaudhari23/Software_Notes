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

   * Amazon S3 managed keys (SSE-S3)
   * AWS KMS managed keys (SSE-KMS) - uses customer master keys (CMKs) to encrypt your Amazon S3 objects
   * Customer Provided keys (SSE-C)
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
