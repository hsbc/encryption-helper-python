from context import context

from Crypto.PublicKey import RSA


def generate_rsa_key():
    logger = context.Context.getinstance().get_logger()

    key_pair = RSA.generate(2048)  # Size: 2048

    encrypted_key = key_pair.export_key(
        format="PEM",  # The format to use for wrapping the key (PEM, DER, OpenSSH)
        # passphrase="1password", # The passphrase used for protecting the output.
        # pkcs=1,
        # protection="scryptAndAES256-CBC", # The encryption scheme to use for protecting the private key.
        # randfunc=None,
        # format="OpenSSH"
    )

    private_key = key_pair.exportKey()
    file_out = open("keys/pem/private-key.pem", "wb")
    file_out.write(encrypted_key)
    file_out.close()

    public_key = key_pair.publickey().exportKey()
    file_out = open("keys/pem/public-key.pem", "wb")
    file_out.write(public_key)
    file_out.close()

    logger.debug("Public key : {0}\n\n".format(public_key))
    logger.debug("Private key : {0}\n\n".format(private_key))

    print(public_key)
    print(private_key)


if __name__ == "__main__":
    generate_rsa_key()
