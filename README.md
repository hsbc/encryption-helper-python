<p align="center">
  <img src="https://www.hsbc.com/-/files/hsbc/header/hsbc-logo-200x25.svg" alt="HSBC Logo" width="200" title="HSBC Logo">
</p>

**Table of Contents**

- [RSA Generation using python (Encryption Helper)](#rsa-generation-using-python-encryption-helper)
  - [Generate an RSA key pair with encryption-helper (empty password)](#generate-an-rsa-key-pair-with-encryption-helper-empty-password)

# RSA Generation using python (Encryption Helper)

![encryption-helper banner][0]

Encryption Helper (encryption-helper) is a simple python program to create a public encryption key and a private decryption key. Such key pairs are used for automating logins, single sign-on, and for authenticating hosts.

## Generate an RSA key pair with Encryption Helper (empty password)

The default and simplest comand is `python3 encryption-helper`. To ensure the key is generated with the correct requirements, we have detailled the
implementation:

```bash
    # Generate an RSA key pair with encryption-helper (empty password)
    # - Standard: OpenPGP Standard
    # - Type: RSA
    # - Size: 2048
    # - Hash algorithm: SHA-256
    # - Ciphers and key length: AES (256)

    python3 encryption-helper
```

[0]: ./assets/banner.jpg
