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
    LEVEL_INFO = "info"
    LEVEL_WARNING = "warning"
    LEVEL_DEBUG = "debug"
    LEVEL_ERROR = "error"
    LEVEL_CRITICAL = "critical"

    def __init__(self, log_file_path, log_file_name, logger_impl):
        """Init
        Args:
            log_file_path   - absolute path to the log file
            log_file_name   - name of the log file
            logger_impl     - logger implementation object
        Raises:
            None
        """
        Precondition.is_string(log_file_path, "Invalid log_file_path")
        Precondition.is_string(log_file_name, "Invalid log_file_name")
        Precondition.is_true(logger_impl, "Invalid logger_impl")

        self.log_file_path = log_file_path
        self.log_file_name = log_file_name
        self.logger_impl = logger_impl

    def trace(self, message=None, level=None):
        """Log a message
        Args:
            message    - string to be logged
            level      - level for logging
        Raises:
            None
        """
        if level is None:
            level = self.LEVEL_INFO

        if message is not None:
            print(message)
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
    def create(log_file_path, log_file_name, level=None):
        """Creates the log file
        Args:
            log_file_path   - absolute path to the log file
            log_file_name   - name of the log file
            level           - logging level
        Raises:
            None
        """
        if level is None:
            level = logging.DEBUG

        # configure log file
        log_file_folder_path = os.path.dirname(os.path.realpath(log_file_path))
        if not os.path.exists(log_file_folder_path):
            os.makedirs(log_file_folder_path)

        logger_impl = logging.getLogger(log_file_name)

        Assertion.is_true(logger_impl, "Invalid logger_impl")

        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

        hdlr = logging.FileHandler(log_file_path)
        hdlr.setFormatter(formatter)
        logger_impl.addHandler(hdlr) 

        logger_impl.setLevel(level)

        return Logger(log_file_path, log_file_name, logger_impl)
