import unittest
import logging
from encryption_helper.context.context import Context


class TestContext(unittest.TestCase):

    def setUp(self):
        # Reset the singleton instance before each test
        Context._instance = None

    def test_singleton_instance(self):
        # Test that only one instance of Context is created
        context1 = Context.get_instance()
        context2 = Context.get_instance()
        self.assertIs(context1, context2)

    def test_set_name(self):
        # Test setting the context name
        context = Context.get_instance()
        context.set_name("test_app")
        self.assertEqual(context.name, "test_app")

    def test_set_log_level_valid(self):
        # Test setting valid log levels
        context = Context.get_instance()
        context.set_log_level("DEBUG")
        self.assertEqual(context.log_level, logging.DEBUG)
        context.set_log_level("INFO")
        self.assertEqual(context.log_level, logging.INFO)
        context.set_log_level("WARNING")
        self.assertEqual(context.log_level, logging.WARNING)
        context.set_log_level("ERROR")
        self.assertEqual(context.log_level, logging.ERROR)
        context.set_log_level("CRITICAL")
        self.assertEqual(context.log_level, logging.CRITICAL)

    def test_set_log_level_invalid(self):
        # Test setting an invalid log level
        context = Context.get_instance()
        with self.assertRaises(ValueError):
            context.set_log_level("INVALID")

    def test_init_logging(self):
        # Test initializing logging
        context = Context.get_instance()
        context.set_name("test_app")
        context.set_log_level("DEBUG")
        context.init_logging()
        logger = context.get_logger()
        self.assertEqual(logger.name, "test_app")
        self.assertEqual(logger.level, logging.DEBUG)
        self.assertTrue(logger.hasHandlers())

    def test_get_logger(self):
        # Test getting the logger
        context = Context.get_instance()
        context.set_name("test_app")
        context.set_log_level("DEBUG")
        logger = context.get_logger()
        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.name, "test_app")
        self.assertEqual(logger.level, logging.DEBUG)


if __name__ == "__main__":
    unittest.main()
