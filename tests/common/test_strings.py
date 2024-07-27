import unittest
from encryption_helper.common.strings import (
    private_key_suffix,
    public_key_suffix,
    encrypted_file_suffix,
)


class TestStrings(unittest.TestCase):

    def test_private_key_suffix(self):
        # Test the private key suffix
        self.assertEqual(private_key_suffix, "private-key.pem")

    def test_public_key_suffix(self):
        # Test the public key suffix
        self.assertEqual(public_key_suffix, "public_key.pem")

    def test_encrypted_file_suffix(self):
        # Test the encrypted file suffix
        self.assertEqual(encrypted_file_suffix, ".bin")


if __name__ == "__main__":
    unittest.main()
