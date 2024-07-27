"""
Context module for the encryption_helper package.

This module provides a Context class for managing application-wide settings and logging.
It implements the Singleton pattern to ensure only one instance of the context exists.

Classes:
    Context: A singleton class for managing application context and logging.
"""

import logging
from typing import Optional


class Context:
    """
    A singleton class for managing application context and logging.

    This class provides methods for setting the application name, configuring
    logging levels, and retrieving a configured logger instance. It ensures
    that only one instance of the Context is created and used throughout the
    application.

    Attributes:
        _instance (Optional[Context]): The singleton instance of the Context class.
        name (str): The name of the application context, used for logging.
        log_level (int): The current logging level.
        logger (Optional[logging.Logger]): The logger instance for the context.

    Example:
        >>> context = Context.get_instance()
        >>> context.set_name('my_app')
        >>> context.set_log_level('DEBUG')
        >>> logger = context.get_logger()
        >>> logger.debug('This is a debug message')
    """

    _instance: Optional["Context"] = None
    name: str = ""
    log_level: int = logging.INFO
    logger: Optional[logging.Logger] = None

    def __new__(cls) -> "Context":
        """
        Create and return the singleton instance of the Context class.

        If the instance doesn't exist, it creates one and initializes it.
        If it exists, it returns the existing instance.

        Returns:
            Context: The singleton instance of the Context class.
        """
        if cls._instance is None:
            cls._instance = super(Context, cls).__new__(cls)
            cls._instance.set_name("keypy")  # Set default name
        return cls._instance

    @classmethod
    def get_instance(cls) -> "Context":
        """
        Get the singleton instance of the Context class.

        This method ensures that only one instance of Context is created and used.

        Returns:
            Context: The singleton instance of the Context class.
        """
        if cls._instance is None:
            cls()
        return cls._instance

    def set_name(self, name: str) -> None:
        """
        Set the name of the context.

        This name is used as the logger name when initializing logging.

        Args:
            name (str): The name to set for the context.
        """
        self.name = name

    def set_log_level(self, log_level: Optional[str]) -> None:
        """
        Set the logging level for the context.

        This method sets the log level to be used by the logger. If an invalid
        log level is provided, it raises a ValueError.

        Args:
            log_level (Optional[str]): The log level to set. Should be one of
                'INFO', 'DEBUG', 'WARNING', 'ERROR', or 'CRITICAL'.
                If None or empty string, it defaults to 'INFO'.

        Raises:
            ValueError: If an invalid logging level is provided.

        Example:
            >>> context = Context.get_instance()
            >>> context.set_log_level('DEBUG')
        """
        if log_level is None or log_level.strip() == "":
            self.log_level = logging.INFO
            return

        log_levels = {
            "INFO": logging.INFO,
            "DEBUG": logging.DEBUG,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }

        if log_level not in log_levels:
            raise ValueError(
                f"Invalid logging level: {log_level}. "
                f'Valid levels are: {", ".join(log_levels.keys())}'
            )

        self.log_level = log_levels[log_level]

    def init_logging(self) -> None:
        """
        Initialize the logger for the context.

        This method sets up a logger with a StreamHandler, sets the log level,
        and configures the log format. It ensures that handlers are not duplicated
        if called multiple times.
        """
        self.logger = logging.getLogger(self.name)
        console_handler = logging.StreamHandler()
        self.logger.setLevel(self.log_level)
        log_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(log_format)
        if not self.logger.handlers:
            self.logger.addHandler(console_handler)
        self.logger.info("Logging initialized")

    def get_logger(self) -> logging.Logger:
        """
        Get the logger for the context, initializing it if necessary.

        This method returns the logger instance for the context. If the logger
        hasn't been initialized yet, it calls init_logging() to set it up.

        Returns:
            logging.Logger: The configured logger instance for this context.

        Example:
            >>> context = Context.get_instance()
            >>> logger = context.get_logger()
            >>> logger.info('This is an info message')
        """
        if self.logger is None:
            self.init_logging()
        return self.logger
