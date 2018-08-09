"""
Unit Test for arg_parser
"""
import os

from unittest import TestCase

from config.config import Config
from utils.string_utils import StringUtils


class TestConfig(TestCase):
    """
    Unit test for config
    """

    def test_create(self):
        """Test Create

        Args:
            self - TestConfig
        Raises:
            None
        """
        __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

        config = Config(os.path.join(__location__, 'test_config.cfg'))

        dataset_csv_file_path = config.get_field("input_output_settings", "DATASET_CSV_FILE_PATH")
        output_folder_path = config.get_field("input_output_settings", "OUTPUT_FOLDER_PATH")
        log_file_path = config.get_field("input_output_settings", "LOG_FILE_PATH")
        should_show_plots = StringUtils.str_to_boolean(
            config.get_field("input_output_settings", "SHOULD_SHOW_PLOTS"))

        self.assertEqual(dataset_csv_file_path, '../../data/test_analysis.csv')
        self.assertEqual(output_folder_path, 'output/test_analysis')
        self.assertEqual(log_file_path, 'logs/log.txt')
        self.assertEqual(should_show_plots, False)
