"""
Unit Test for logger
"""
import os

from unittest import TestCase

from logger.logger import Logger
from exceptions.exceptions import PreconditionException


class TestLogger(TestCase):
    """
    Unit test for logger
    """
    TEST_LOG_FILE_PATH = 'logs/log.txt'

    def setUp(self):
        """setUp

        Args:
            self: TestLogger

        Returns:
            None

        Raises:
            None
        """
        pass

    def tearDown(self):
        """tearDown

        Args:
            self: TestLogger

        Returns:
            None

        Raises:
            None
        """
        if os.path.exists(self.TEST_LOG_FILE_PATH):
            os.remove(self.TEST_LOG_FILE_PATH)

        if os.path.exists(os.path.dirname(self.TEST_LOG_FILE_PATH)):
            os.removedirs(os.path.dirname(self.TEST_LOG_FILE_PATH))

    def test_create(self):
        """Test Create

        Args:
            self: TestLogger

        Returns:
            None

        Raises:
            None
        """
        logger = Logger.create(self.TEST_LOG_FILE_PATH)
        self.assertIsNotNone(logger)

        # test with a bad log file path
        with self.assertRaises(PreconditionException) as context:
            Logger.create(1)
        self.assertTrue('Invalid log_file_path' in str(context.exception))

    def test_trace(self):
        """Test Trace

        Args:
            self: TestLogger

        Returns:
            None

        Raises:
            None
        """
        logger = Logger.create(self.TEST_LOG_FILE_PATH)
        logger.trace('Test Info', Logger.LEVEL_INFO)
        logger.trace('Test Debug', Logger.LEVEL_DEBUG)
        logger.trace('Test Critical', Logger.LEVEL_CRITICAL)
        logger.trace('Test Error', Logger.LEVEL_ERROR)
        logger.trace('Test Warning', Logger.LEVEL_WARNING)

        for test_string in ['Test Info', 'Test Debug', 'Test Critical', 'Test Error', 'Test Warning']:
            with open(self.TEST_LOG_FILE_PATH) as log_file:
                if test_string not in log_file.read():
                    self.assertTrue(False, "test_string={} is not present".format(test_string))
