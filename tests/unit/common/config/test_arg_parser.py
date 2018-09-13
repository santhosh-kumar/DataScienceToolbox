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
            self: TestArgParser

        Returns:
            None

        Raises:
            None
        """
        arg_parser = ArgParser(['--config', 'test_config.cfg'])
        self.assertEqual(arg_parser.get_arguments().config, 'test_config.cfg')
