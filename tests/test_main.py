import unittest
from unittest.mock import patch, mock_open, MagicMock
from encryption_helper.main import generate_rsa_key
from pathlib import Path


class TestGenerateRSAKey(unittest.TestCase):

    @patch("encryption_helper.main.serialization.load_pem_private_key")
    @patch("encryption_helper.main.Path.mkdir")
    @patch("encryption_helper.main.open", new_callable=mock_open)
    @patch("encryption_helper.main.Context.get_instance")
    @patch("encryption_helper.main.rsa.generate_private_key")
    def test_generate_rsa_key(
        self,
        mock_generate_private_key,
        mock_context,
        mock_open,
        mock_mkdir,
        mock_load_pem_private_key,
    ):
        # Mock RSA key pair generation
        mock_private_key = MagicMock()
        mock_public_key = MagicMock()
        mock_private_key.private_bytes.return_value = b"fake_private_key"
        mock_public_key.public_bytes.return_value = b"fake_public_key"
        mock_private_key.public_key.return_value = mock_public_key
        mock_generate_private_key.return_value = mock_private_key

        # Mock logger
        mock_logger = MagicMock()
        mock_context.return_value.get_logger.return_value = mock_logger

        # Call the function
        public_key, private_key = generate_rsa_key()

        # Assertions to check if the keys are generated correctly
        self.assertEqual(public_key, b"fake_public_key")
        self.assertEqual(private_key, b"fake_private_key")

        # Assertions to check if the directory was created
        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)

        # Assertions to check if files were written correctly
        mock_open.assert_any_call(Path("keys/pem/private-key.pem"), "wb")
        mock_open.assert_any_call(Path("keys/pem/public-key.pem"), "wb")
        mock_open().write.assert_any_call(b"fake_private_key")
        mock_open().write.assert_any_call(b"fake_public_key")

        # Assertions to check logging
        mock_logger.debug.assert_any_call(f"Public key:\n{public_key.decode()}\n")
        mock_logger.debug.assert_any_call(f"Private key:\n{private_key.decode()}\n")

        # Assertions to check printing to console
        with patch("builtins.print") as mock_print:
            generate_rsa_key()
            mock_print.assert_any_call("Public key:")
            mock_print.assert_any_call(public_key.decode())
            mock_print.assert_any_call("\nPrivate key:")
            mock_print.assert_any_call(private_key.decode())

    @patch(
        "encryption_helper.main.rsa.generate_private_key",
        side_effect=OSError("File write error"),
    )
    @patch("encryption_helper.main.Context.get_instance")
    def test_generate_rsa_key_os_error(self, mock_context, mock_generate_private_key):
        # Mock logger
        mock_logger = MagicMock()
        mock_context.return_value.get_logger.return_value = mock_logger

        # Ensure OSError is raised
        with self.assertRaises(OSError):
            generate_rsa_key()

        # Assertions to check if error was logged
        mock_logger.error.assert_called_once_with(
            "Error writing key files: File write error"
        )

    @patch(
        "encryption_helper.main.rsa.generate_private_key",
        side_effect=Exception("Unexpected error"),
    )
    @patch("encryption_helper.main.Context.get_instance")
    def test_generate_rsa_key_unexpected_error(
        self, mock_context, mock_generate_private_key
    ):
        # Mock logger
        mock_logger = MagicMock()
        mock_context.return_value.get_logger.return_value = mock_logger

        # Ensure generic Exception is raised
        with self.assertRaises(Exception):
            generate_rsa_key()

        # Assertions to check if error was logged
        mock_logger.error.assert_called_once_with(
            "Unexpected error during key generation: Unexpected error"
        )


if __name__ == "__main__":
    unittest.main()
