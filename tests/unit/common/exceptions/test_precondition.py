"""
Unit Test for arg_parser
"""
from unittest import TestCase

from exceptions.precondition import Precondition
from exceptions.exceptions import PreconditionException


class TestPrecondition(TestCase):
    """
    Unit test for precondition
    """

    def test_is_methods_go_right(self):
        """Test is_* methods

        Args:
            self - TestAssertion
        Raises:
            None
        """
        Precondition.is_true(True, 'Test for boolean failed')
        Precondition.is_string('Test', 'Test for string failed')
        Precondition.is_integer(1, 'Test for integer failed')
        Precondition.is_positive_integer(1, 'Test for positive integer failed')
        Precondition.is_non_negative_integer(0, 'Test for positive integer failed')
        Precondition.is_array([1, 3], 'Test for array failed')
        Precondition.is_dict({'a': 'test'}, 'Test for message failed')

    def test_is_methods_exceptions(self):
        """Test is_* methods exceptions

        Args:
            self - TestAssertion
        Raises:
            None
        """
        # is_true
        with self.assertRaises(PreconditionException) as context:
            Precondition.is_true(False, 'Test for boolean failed')

        self.assertTrue('Test for boolean failed' in str(context.exception))

        # is_string
        with self.assertRaises(PreconditionException) as context:
            Precondition.is_string(1, 'Test for string failed')
        self.assertTrue('Test for string failed' in str(context.exception))

        # is_integer
        with self.assertRaises(PreconditionException) as context:
            Precondition.is_integer('not integer', 'Test for integer failed')
        self.assertTrue('Test for integer failed' in str(context.exception))

        # is_positive_integer
        with self.assertRaises(PreconditionException) as context:
            Precondition.is_positive_integer(0, 'Test for positive integer failed')
        self.assertTrue('Test for positive integer failed' in str(context.exception))

        # is_non_negative_integer
        with self.assertRaises(PreconditionException) as context:
            Precondition.is_non_negative_integer(-1, 'Test for non-negative integer failed')
        self.assertTrue('Test for non-negative integer failed' in str(context.exception))

        # is_array
        with self.assertRaises(PreconditionException) as context:
            Precondition.is_array(0, 'Test for array failed')
        self.assertTrue('Test for array failed' in str(context.exception))

        # is_dict
        with self.assertRaises(PreconditionException) as context:
            Precondition.is_dict([1, 2], 'Test for dict failed')
        self.assertTrue('Test for dict failed' in str(context.exception))
