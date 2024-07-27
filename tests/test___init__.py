import unittest

# Import the module to be tested
import encryption_helper


class TestInit(unittest.TestCase):

    def test_version(self):
        # Ensure the version is set correctly
        self.assertEqual(encryption_helper.__version__, "0.0.1")

    def test_generate_rsa_key_import(self):
        # Ensure generate_rsa_key is imported correctly
        from encryption_helper import generate_rsa_key

        self.assertIsNotNone(generate_rsa_key)

    def test_all_exports(self):
        # Ensure __all__ includes the correct exports
        self.assertIn("generate_rsa_key", encryption_helper.__all__)


if __name__ == "__main__":
    unittest.main()
