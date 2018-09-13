"""
Unit Test for string_utils
"""
from unittest import TestCase

from utils.string_utils import StringUtils
from exceptions.exceptions import AssertionException


class TestStringUtils(TestCase):
    """
    Unit test for string utils
    """

    def test_str_to_boolean(self):
        """Test str_to_boolean

        Args:
            self: TestStringUtils

        Returns:
            None

        Raises:
            None
        """
        self.assertTrue(StringUtils.str_to_boolean('t'))
        self.assertTrue(StringUtils.str_to_boolean('T'))
        self.assertTrue(StringUtils.str_to_boolean('yes'))
        self.assertTrue(StringUtils.str_to_boolean('YES'))
        self.assertTrue(StringUtils.str_to_boolean('1'))
        self.assertTrue(StringUtils.str_to_boolean('true'))
        self.assertTrue(StringUtils.str_to_boolean('TRUE'))

        self.assertFalse(StringUtils.str_to_boolean('0'))
        self.assertFalse(StringUtils.str_to_boolean('No'))
        self.assertFalse(StringUtils.str_to_boolean('some value'))

        with self.assertRaises(AssertionException) as context:
            self.assertFalse(StringUtils.str_to_boolean(1))
        self.assertTrue('Invalid String Value' in str(context.exception))

    def test_to_str(self):
        """Test to_str

        Args:
            self: TestStringUtils

        Returns:
            None

        Raises:
            None
        """
        self.assertEqual('test', StringUtils.to_str('test'))
        self.assertEqual('test', StringUtils.to_str(b'test'))

    def test_to_bytes(self):
        """Test to_str

        Args:
            self: TestStringUtils

        Returns:
            None

        Raises:
            None
        """
        self.assertEqual(b'test', StringUtils.to_bytes(b'test'))
        self.assertEqual(b'test', StringUtils.to_bytes('test'))
