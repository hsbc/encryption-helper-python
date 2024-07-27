import unittest
from unittest.mock import patch
from io import StringIO

# Import the main function from the __main__.py module
from encryption_helper.__main__ import main


class TestMain(unittest.TestCase):

    @patch("encryption_helper.__main__.generate_rsa_key")
    def test_main_success(self, mock_generate_rsa_key):
        # Mock the generate_rsa_key function to return dummy keys
        mock_generate_rsa_key.return_value = (b"fake_public_key", b"fake_private_key")

        # Capture the output printed to the console
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()

        # Check if the expected output is in the console output
        self.assertIn("Running encryption_helper...", output)
        self.assertIn("RSA key pair generated successfully.", output)
        self.assertIn("Public key length: 15 bytes", output)
        self.assertIn("Private key length: 16 bytes", output)
        self.assertIn("The keys have been saved in the 'keys/pem' directory.", output)

    @patch(
        "encryption_helper.__main__.generate_rsa_key",
        side_effect=OSError("File write error"),
    )
    def test_main_os_error(self, mock_generate_rsa_key):
        # Capture the output printed to the console
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit) as cm:
                main()
            output = mock_stdout.getvalue()
            self.assertEqual(cm.exception.code, 1)

        # Check if the expected output is in the console output
        self.assertIn("Running encryption_helper...", output)
        self.assertIn(
            "An error occurred while writing the key files: File write error", output
        )

    @patch(
        "encryption_helper.__main__.generate_rsa_key",
        side_effect=ValueError("Invalid parameters"),
    )
    def test_main_value_error(self, mock_generate_rsa_key):
        # Capture the output printed to the console
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit) as cm:
                main()
            output = mock_stdout.getvalue()
            self.assertEqual(cm.exception.code, 1)

        # Check if the expected output is in the console output
        self.assertIn("Running encryption_helper...", output)
        self.assertIn(
            "An error occurred with the key generation parameters: Invalid parameters",
            output,
        )

    @patch(
        "encryption_helper.__main__.generate_rsa_key",
        side_effect=ImportError("Missing module"),
    )
    def test_main_import_error(self, mock_generate_rsa_key):
        # Capture the output printed to the console
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit) as cm:
                main()
            output = mock_stdout.getvalue()
            self.assertEqual(cm.exception.code, 1)

        # Check if the expected output is in the console output
        self.assertIn("Running encryption_helper...", output)
        self.assertIn(
            "An error occurred while importing required modules: Missing module", output
        )

    @patch(
        "encryption_helper.__main__.generate_rsa_key",
        side_effect=Exception("Unexpected error"),
    )
    def test_main_unexpected_error(self, mock_generate_rsa_key):
        # Capture the output printed to the console
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            with self.assertRaises(SystemExit) as cm:
                main()
            output = mock_stdout.getvalue()
            self.assertEqual(cm.exception.code, 1)

        # Check if the expected output is in the console output
        self.assertIn("Running encryption_helper...", output)
        self.assertIn("An unexpected error occurred: Unexpected error", output)
        self.assertIn("Please report this issue to the maintainers.", output)


if __name__ == "__main__":
    unittest.main()
