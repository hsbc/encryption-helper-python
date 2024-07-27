import unittest
from unittest.mock import patch, mock_open, MagicMock
from encryption_helper.utils.io import read_file


class TestReadFile(unittest.TestCase):

    @patch(
        "encryption_helper.utils.io.read_file.os.path.join",
        return_value="/fake/directory/fake_file.txt",
    )
    @patch(
        "encryption_helper.utils.io.read_file.open",
        new_callable=mock_open,
        read_data=b"test data",
    )
    @patch("encryption_helper.utils.io.read_file.context.Context.get_instance")
    @patch("encryption_helper.utils.io.read_file.checks.str_none_or_empty")
    def test_read_text_in_binary_mode(
        self, mock_str_none_or_empty, mock_get_instance, mock_open, mock_path_join
    ):
        # Mock the logger
        mock_logger = MagicMock()
        mock_get_instance.return_value.get_logger.return_value = mock_logger

        # Mock checks
        mock_str_none_or_empty.return_value = False

        # Call the function
        result = read_file.read_text_in_binary_mode("fake/directory", "fake_file.txt")

        # Assertions
        self.assertEqual(result, b"test data")
        mock_path_join.assert_called_once_with("fake/directory", "fake_file.txt")
        mock_open.assert_called_once_with("/fake/directory/fake_file.txt", "rb")
        mock_logger.info.assert_called_once_with(
            "Reading from file : /fake/directory/fake_file.txt"
        )

    @patch(
        "encryption_helper.utils.io.read_file.os.path.join",
        return_value="/fake/directory/fake_file.txt",
    )
    @patch(
        "encryption_helper.utils.io.read_file.open",
        new_callable=mock_open,
        read_data=b"test data",
    )
    @patch("encryption_helper.utils.io.read_file.context.Context.get_instance")
    @patch("encryption_helper.utils.io.read_file.checks.str_none_or_empty")
    def test_read_text_in_binary_mode_abs(
        self, mock_str_none_or_empty, mock_get_instance, mock_open, mock_path_join
    ):
        # Mock the logger
        mock_logger = MagicMock()
        mock_get_instance.return_value.get_logger.return_value = mock_logger

        # Mock checks
        mock_str_none_or_empty.return_value = False

        # Call the function
        result = read_file.read_text_in_binary_mode_abs("/fake/directory/fake_file.txt")

        # Assertions
        self.assertEqual(result, b"test data")
        mock_open.assert_called_once_with("/fake/directory/fake_file.txt", "rb")
        mock_logger.info.assert_called_once_with(
            "Reading from file : /fake/directory/fake_file.txt"
        )

    @patch("encryption_helper.utils.io.read_file.context.Context.get_instance")
    @patch(
        "encryption_helper.utils.io.read_file.checks.str_none_or_empty",
        return_value=True,
    )
    def test_read_text_in_binary_mode_empty_args(
        self, mock_str_none_or_empty, mock_get_instance
    ):
        # Mock the logger
        mock_logger = MagicMock()
        mock_get_instance.return_value.get_logger.return_value = mock_logger

        # Call the function and expect an exception
        with self.assertRaises(Exception) as context:
            read_file.read_text_in_binary_mode("fake/directory", "fake_file.txt")

        # Assertions
        self.assertEqual(str(context.exception), "One or more arguments are empty")
        mock_logger.exception.assert_called_once_with("One or more arguments are empty")

    @patch("encryption_helper.utils.io.read_file.context.Context.get_instance")
    @patch(
        "encryption_helper.utils.io.read_file.checks.str_none_or_empty",
        return_value=True,
    )
    def test_read_text_in_binary_mode_abs_empty_args(
        self, mock_str_none_or_empty, mock_get_instance
    ):
        # Mock the logger
        mock_logger = MagicMock()
        mock_get_instance.return_value.get_logger.return_value = mock_logger

        # Call the function and expect an exception
        with self.assertRaises(Exception) as context:
            read_file.read_text_in_binary_mode_abs("/fake/directory/fake_file.txt")

        # Assertions
        self.assertEqual(str(context.exception), "One or more arguments are empty")
        mock_logger.exception.assert_called_once_with("One or more arguments are empty")


if __name__ == "__main__":
    unittest.main()
