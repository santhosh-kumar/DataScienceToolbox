"""
Unit Test for base_analysis
"""
import os

from unittest import TestCase

from analysis.base_analysis import BaseAnalysis
from exceptions.exceptions import PreconditionException


class DummyBaseAnalysis(BaseAnalysis):
    """
    A Derived class for BaseAnalysis
    """
    ANALYSIS_NAME = 'dummy_base_analysis'

    def __init__(self,
                 output_folder_path,
                 log_file_path):
        """Test Analysis
        Args:
            output_folder_path      - output folder path
            log_file_path           - path to the log file
        Raises:
            None
        """
        BaseAnalysis.__init__(self, self.ANALYSIS_NAME, log_file_path, output_folder_path)

    def execute(self, should_show):
        """Executes the Test

        Args:
            should_show - should plot results
        Raises:
            None
        """
        pass


class TestBaseAnalysis(TestCase):
    """
    Unit test for analysis
    """
    TEST_OUTPUT_FOLDER_PATH = 'output/test_analysis'
    TEST_LOG_FILE_PATH = 'logs/log.txt'

    def setUp(self):
        """setUp

        Args:
            self - TestBaseAnalysis
        Raises:
            None
        """
        pass

    def tearDown(self):
        """tearDown

        Args:
            self - TestBaseAnalysis
        Raises:
            None
        """
        if os.path.exists(self.TEST_OUTPUT_FOLDER_PATH):
            os.removedirs(self.TEST_OUTPUT_FOLDER_PATH)

        if os.path.exists(self.TEST_LOG_FILE_PATH):
            os.remove(self.TEST_LOG_FILE_PATH)

        if os.path.exists(os.path.dirname(self.TEST_LOG_FILE_PATH)):
            os.removedirs(os.path.dirname(self.TEST_LOG_FILE_PATH))

    def test_create(self):
        """Test Create

        Args:
            self - TestBaseAnalysis
        Raises:
            None
        """
        DummyBaseAnalysis(self.TEST_OUTPUT_FOLDER_PATH, self.TEST_LOG_FILE_PATH)

    def test_precondition_output_folder(self):
        """Test Create with invalid output folder

        Args:
            self - TestBaseAnalysis
        Raises:
            None
        """
        # Boolean
        with self.assertRaises(PreconditionException) as context:
            DummyBaseAnalysis(True, self.TEST_LOG_FILE_PATH)

        self.assertTrue('Invalid output_folder_path' in str(context.exception))

        # integer
        with self.assertRaises(PreconditionException) as context:
            DummyBaseAnalysis(1, self.TEST_LOG_FILE_PATH)

        self.assertTrue('Invalid output_folder_path' in str(context.exception))

    def test_precondition_log_file_path(self):
        """Test Create with invalid log file path

        Args:
            self - TestBaseAnalysis
        Raises:
            None
        """
        # boolean
        with self.assertRaises(PreconditionException) as context:
            DummyBaseAnalysis(self.TEST_OUTPUT_FOLDER_PATH, True)

        self.assertTrue('Invalid log_file_path' in str(context.exception))

        # integer
        with self.assertRaises(PreconditionException) as context:
            DummyBaseAnalysis(self.TEST_OUTPUT_FOLDER_PATH, 1)

        self.assertTrue('Invalid log_file_path' in str(context.exception))
