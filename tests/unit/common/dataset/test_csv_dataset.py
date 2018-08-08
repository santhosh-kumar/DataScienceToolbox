"""
Unit Test for arg_parser
"""
import os

from unittest import TestCase
import numpy as np

from dataset.csv_dataset import CsvDataset
from exceptions.exceptions import PreconditionException


class TestCsvDataset(TestCase):
    """
    Unit test for config
    """

    def test_create(self):
        """Test Create

        Args:
            self - TestCsvDataset
        Raises:
            None
        """
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        dataset_csv_file_path = os.path.join(__location__, 'sample_data.csv')

        CsvDataset(dataset_csv_file_path, None, False)

        # test with bad dataset_csv_file_path
        with self.assertRaises(PreconditionException) as context:
            CsvDataset(1)

        self.assertTrue('Invalid dataset_csv_file_path' in str(context.exception))

    def test_load(self):
        """Test Load

        Args:
            self - TestCsvDataset
        Raises:
            None
        """
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        dataset_csv_file_path = os.path.join(__location__, 'sample_data.csv')

        csv_dataset = CsvDataset(dataset_csv_file_path, None, False)
        csv_dataset.load(dataset_csv_file_path)

        self.assertEqual(len(csv_dataset.get_field_names()), 18)

        policy_ids = csv_dataset.get_field('policyID', np.int)
        self.assertEqual(len(policy_ids), 3)
        self.assertEqual(policy_ids[0], 119736)
        self.assertEqual(policy_ids[1], 448094)
        self.assertEqual(policy_ids[2], 206893)

        state_codes = csv_dataset.get_field('statecode')
        self.assertEqual(len(state_codes), 3)
        self.assertEqual(state_codes[0], 'FL')
        self.assertEqual(state_codes[1], 'CA')
        self.assertEqual(state_codes[2], 'FL')

        # test with bad dataset_csv_file_path
        with self.assertRaises(PreconditionException) as context:
            CsvDataset(1)

        self.assertTrue('Invalid dataset_csv_file_path' in str(context.exception))
