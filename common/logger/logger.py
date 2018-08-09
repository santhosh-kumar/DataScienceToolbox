"""
This file defines a logger class
"""
import os
import logging

from exceptions.precondition import Precondition
from exceptions.assertion import Assertion


class Logger:
    """
    Class for Logger - a wrapper around the python logging
    """
    LEVEL_INFO = 'info'
    LEVEL_WARNING = 'warning'
    LEVEL_DEBUG = 'debug'
    LEVEL_ERROR = 'error'
    LEVEL_CRITICAL = 'critical'

    def __init__(self, log_file_path, logger_impl, logger_name=None):
        """Init
        Args:
            log_file_path   - absolute path to the log file
            logger_impl     - logger implementation object
            logger_name   - name of the log file
        Raises:
            None
        """
        Precondition.is_string(log_file_path, 'Invalid log_file_path')
        Precondition.is_true(logger_impl, 'Invalid logger_impl')

        self.log_file_path = log_file_path
        self.log_file_name = logger_name
        self.logger_impl = logger_impl

    def trace(self, message=None, level=None):
        """Log a message
        Args:
            message    - string to be logged
            level      - level for logging
        Raises:
            None
        """
        if level:
            level = self.LEVEL_INFO

        if message:
            if self.logger_impl is not None:
                if level == self.LEVEL_WARNING:
                    self.logger_impl.warning(message)
                elif level == self.LEVEL_DEBUG:
                    self.logger_impl.debug(message)
                elif level == self.LEVEL_ERROR:
                    self.logger_impl.error(message)
                elif level == self.LEVEL_CRITICAL:
                    self.logger_impl.critical(message)
                else:
                    self.logger_impl.info(message)

    @staticmethod
    def create(log_file_path, logger_name=None, level=None):
        """Creates the log file
        Args:
            log_file_path   - absolute path to the log file
            logger_name     - name of the logger
            level           - logging level
        Raises:
            None
        """
        Precondition.is_string(log_file_path, 'Invalid log_file_path')

        if level is None:
            level = logging.DEBUG

        # configure log file
        log_file_folder_path = os.path.dirname(os.path.realpath(log_file_path))
        if not os.path.exists(log_file_folder_path):
            os.makedirs(log_file_folder_path)

        logger_impl = logging.getLogger(logger_name)

        Assertion.is_true(logger_impl, 'Invalid logger_impl')

        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

        handler = logging.FileHandler(log_file_path)
        handler.setFormatter(formatter)
        logger_impl.addHandler(handler)

        logger_impl.setLevel(level)

        return Logger(log_file_path, logger_impl, logger_name)
