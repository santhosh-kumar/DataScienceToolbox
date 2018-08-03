"""
This module defines analysis abstraction
"""
from abc import ABCMeta, abstractmethod
import os
import sys

from logger.logger import Logger
from exceptions.precondition import Precondition
from exceptions.exceptions import UnsupportedPythongException


class BaseAnalysis:
    """
    Abstraction for Analysis
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, analysis_name, log_file_path, output_folder_path):
        """Init
        Args:
            analysis_name       - name of the analysis
            log_file_path       - path to the log file
            output_folder_path  - output folder path
        Raises:
            None
        """
        if sys.version_info[0] < 3:
            raise UnsupportedPythongException("Python Version must be >= 3.0")

        Precondition.is_string(analysis_name, "Invalid analysis_name")
        Precondition.is_string(log_file_path, "Invalid log_file_path")
        Precondition.is_string(output_folder_path, "Invalid output_folder_path")

        self.analysis_name = analysis_name
        self.logger = Logger.create(os.path.abspath(log_file_path), self.analysis_name)
        self.output_folder_path = os.path.abspath(output_folder_path)

        # create output folder if it doesn't exist
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

    @abstractmethod
    def execute(self, should_show):
        """Executes the specified analysis
        Args:
            should_show - should plot results
        Raises:
            None
        """
        pass
