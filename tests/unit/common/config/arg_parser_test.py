"""
Unit Test for arg_parser
"""
from unittest import TestCase

from config.arg_parser import ArgParser


class TestArgParser(TestCase):
    """
    Unit test for arg_parser
    """

    def test_create(self):
        """Test Create

        Args:
            self - TestArgParser
        Raises:
            None
        """
        arg_parser = ArgParser(['--config', 'config.cfg'])
        self.assertEqual(arg_parser.get_arguments().config, 'config.cfg')
