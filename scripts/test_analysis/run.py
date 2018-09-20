#!/usr/bin/python
"""
This script is a template for Analysis
"""
import os
import sys
import inspect

current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
common_path = os.path.join(current_directory, '../../common')
sys.path.append(os.path.abspath(common_path))

from logger.logger import Logger
from config.config import Config
from config.arg_parser import ArgParser
from analysis.base_analysis import BaseAnalysis
from dataset.csv_dataset import CsvDataset
from plot.plot import Plot
from utils.string_utils import *


class TestAnalysis(BaseAnalysis):
    """
    TestAnalysis
    """
    ANALYSIS_NAME = 'test_analysis'

    def __init__(self,
                 dataset_csv_file_path,
                 output_folder_path,
                 log_file_path):
        """Test Analysis

        Args:
            dataset_csv_file_path: absolute path to the csv file
            output_folder_path: output folder path
            log_file_path: path to the log file

        Returns:
            None

        Raises:
            None
        """
        super(__class__, self).__init__(self.ANALYSIS_NAME, log_file_path, output_folder_path)

        self.dataset_csv_file_path = os.path.abspath(dataset_csv_file_path)
        self.dataset = CsvDataset(dataset_csv_file_path, self.logger)

        self.logger.trace('Finished Loading Test Analysis Dataset...')

    def run(self, analysis_name, should_show=True):
        """Run the analysis

        Args:
            analysis_name: name of the analysis to run
            should_show: should show the plot

        Returns:
            None

        Raises:
            None
        """
        self.logger.trace('############### Starting Analysis ##################')

        # execute the analysis
        self.execute(should_show)

        self.logger.trace('############### Done ##################')

    def execute(self, should_show):
        """Executes the Test

        Args:
            should_show: should plot results

        Returns:
            None

        Raises:
            None
        """
        pass


# main
if __name__ == "__main__":
    try:
        # argument parser
        parser = ArgParser(sys.argv[1:])

        # parse the config
        config = Config(parser.get_arguments().config)

        # set the variables from config
        dataset_csv_file_path = config.get_field('input_output_settings', 'DATASET_CSV_FILE_PATH')
        output_folder_path = config.get_field('input_output_settings', 'OUTPUT_FOLDER_PATH')
        log_file_path = config.get_field('input_output_settings', 'LOG_FILE_PATH')
        should_show_plots = StringUtils.str_to_boolean(
            config.get_field('input_output_settings', 'SHOULD_SHOW_PLOTS'))

        # create test analysis
        test_analysis = TestAnalysis(dataset_csv_file_path,
                                     output_folder_path,
                                     log_file_path)

        test_analysis.run('test_analysis', should_show_plots)

    except Exception as ex:
        print(ex)
