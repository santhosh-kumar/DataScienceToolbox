"""
This module defines dataset abstraction
"""
from abc import ABCMeta, abstractmethod

import numpy as np


class Dataset:
    """
    Abstraction for dataset
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def load(self, dataset_file_path, delimiter=','):
        """Loads the input dataset

        Args:
            dataset_path: absolute path to the dataset file
            delimiter: delimited (default ',')

        Returns:
            None

        Raises:
            None
        """
        pass

    @abstractmethod
    def get_field_names(self):
        """Get fields names

        Args:

        Returns:
            A list Field names in the dataset.

        Raises:
            None
        """
        pass

    @abstractmethod
    def get_field(self, field_name, field_dtype=np.str_):
        """Get a field from the data_array and convert to specified data_type
        Args:
            field_name: name of the field to be returned
            field_dtype: datatype to be used

        Returns:
            An NP array of field values for the given field name

        Raises:
            None
        """
        pass
