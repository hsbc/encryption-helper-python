import unittest
from encryption_helper.utils.checks import checks


class TestChecks(unittest.TestCase):

    def test_str_none_or_empty_all_valid(self):
        # Test case where all arguments are valid non-empty strings
        result = checks.str_none_or_empty("test", "hello", "world")
        self.assertFalse(result)

    def test_str_none_or_empty_with_none(self):
        # Test case where one of the arguments is None
        result = checks.str_none_or_empty("test", None, "world")
        self.assertTrue(result)

    def test_str_none_or_empty_with_empty_string(self):
        # Test case where one of the arguments is an empty string
        result = checks.str_none_or_empty("test", "", "world")
        self.assertTrue(result)

    def test_str_none_or_empty_with_whitespace_string(self):
        # Test case where one of the arguments is a whitespace string
        result = checks.str_none_or_empty("test", "   ", "world")
        self.assertTrue(result)

    def test_str_none_or_empty_all_empty(self):
        # Test case where all arguments are empty strings
        result = checks.str_none_or_empty("", " ", None)
        self.assertTrue(result)

    def test_str_none_or_empty_no_args(self):
        # Test case where no arguments are provided
        result = checks.str_none_or_empty()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
