"""
This file defines a config parsing class
"""
import configparser as cp

from exceptions.precondition import Precondition
from exceptions.assertion import Assertion


class Config:
    """
    Class for Config Management
    """
    DEFAULT_CONFIG_FILE_NAME = 'config.cfg'

    def __init__(self, config_file_path=DEFAULT_CONFIG_FILE_NAME):
        """Init
        Args:
            config_file_path - absolute path to the config file
        Raises:
            None
        """
        Precondition.is_string(config_file_path, 'Invalid config_file_path')
        self.config_file_path = config_file_path
        self.config = self.load(self.config_file_path)

    def load(self, config_file_path=None):
        """Loads the input config file
        Args:
            csv_file_path - absolute path to the config file
        Raises:
            None
        """
        if config_file_path is None:
            config_file_path = self.DEFAULT_CONFIG_FILE_NAME
        try:
            with open(config_file_path, 'r') as config_file:
                config_data = config_file.read()
        except IOError:
            print('Config File: '" + config_file_path + "' does not exist.')
            raise

        Assertion.is_true(config_data, 'Invalid config_data')

        # print the config data
        print(config_data)

        # parse the config
        config = cp.RawConfigParser(allow_no_value=True)
        config.read_string(config_data)
        return config

    def get_field(self, section_name, field_name):
        """Get a field from the config
        Args:
            section_name  - name of the section for the field
            field_name    - name of the field to be returned
        Raises:
            None
        """
        return self.config.get(section_name, field_name)
