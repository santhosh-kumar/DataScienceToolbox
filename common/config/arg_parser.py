"""
This file defines an argument parsing class
"""
import argparse as ap

from config.config import Config
from exceptions.exceptions import ArgumentParserFailureException


class ArgParser:
    """
    Class for Argument Parsing
    """
    FLAG_RUN = "-r"
    FLAG_CONFIG = "-c"

    FLAG_RUN_VERBOSE = "--run"
    FLAG_CONFIG_VERBOSE = "--config"

    DEFAULT_RUN_VALUE = "all"

    INFO_RUN = "Analysis to Run"
    INFO_CONFIG = "Config File Path"

    def __init__(self, args=None):
        """Init
            args - Arguments passed
        """
        parser = ap.ArgumentParser()

        parser.add_argument(self.FLAG_RUN, self.FLAG_RUN_VERBOSE,
                            default=self.DEFAULT_RUN_VALUE,
                            help=self.INFO_RUN)

        parser.add_argument(self.FLAG_CONFIG, self.FLAG_CONFIG_VERBOSE,
                            default=Config.DEFAULT_CONFIG_FILE_NAME,
                            help=self.INFO_CONFIG)
        try:
            self.args = parser.parse_args(args)
        except Exception as ex:
            raise ArgumentParserFailureException(str(ex))

    def get_arguments(self):
        """Get arguments
        Args:
        Raises:
            None
        """
        return self.args
