"""
This file defines a CSV Dataset processing class
"""
import csv

import numpy as np

from dataset.dataset import Dataset
from exceptions.precondition import Precondition


class CsvDataset(Dataset):
    """
    A class to load and access csv dataset and it's fields
    """
    def __init__(self, dataset_csv_file_path, logger=None, should_load=True):
        """Init
        Args:
            dataset_csv_file_path   - absolute path to the csv file
            logger                  - shared logger (could be null)
            should_load             - should the dataset (default = True)
        Raises:
            None
        """
        Precondition.is_string(dataset_csv_file_path, "Invalid dataset_csv_file_path")
        self.dataset_csv_file_path = dataset_csv_file_path
        self.logger = logger
        self.data_array = []
        if should_load:
            self.load(self.dataset_csv_file_path)

    def load(self, csv_file_path, delimiter=','):
        """Loads the input csv file
        Args:
            csv_file_path - absolute path to the csv file
            delimiter     - delimited (default ',')
        Raises:
            None
        """
        if self.logger:
            self.logger.trace("Loading dataset: {0} with a delimiter \"{1}\" ...".format(csv_file_path, delimiter))
        
        with open(csv_file_path, 'r') as csv_file:
            data_iter = csv.reader(csv_file, 
                                   delimiter=delimiter,
                                   quotechar='"')
            data = [data for data in data_iter]
        self.data_array = np.asarray(data)

    def get_field_names(self):
        """Get fields names
        Args:
        Raises:
            None
        """
        Precondition.is_true(isinstance(self.data_array, np.ndarray), "Invalid data_array")
        # find the index of the field_name in data_array        
        field_names = self.data_array[0, :].tolist()
        return field_names

    def get_field(self, field_name, field_dtype=np.str_):
        """Get a field from the data_array and convert to specified data_type
        Args:
            field_name    - name of the field to be returned
            field_dtype   - datatype to be used
        Raises:
            None
        """
        Precondition.is_true(isinstance(self.data_array, np.ndarray), "Invalid data_array")
        # find the index of the field_name in data_array
        field_list = self.get_field_names()
        field_index = field_list.index(field_name)
        field_data = self.data_array[1:, field_index]
        return field_data.astype(field_dtype)
