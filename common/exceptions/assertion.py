"""
This file defines a wrapper for Assertion
"""
from exceptions.exceptions import AssertionException


class Assertion:
    """
    Assertion Utilities are used for checking programming errors 
    """
    @staticmethod
    def is_true(statement, message=None):
        """Checks whether the statement is true, if not throws an exception

        Args:
            statement: statement to be checked
            message: message for the exception

        Returns:
            None

        Raises:
            AssertionException
        """
        if not statement:
            raise AssertionException(message)

    @staticmethod
    def is_string(variable, message=None):
        """Checks whether the variable is a string, if not throws an exception

        Args:
            variable: variable to be checked
            message: message for the exception

        Returns:
            None

        Raises:
            AssertionException
        """
        if not isinstance(variable, str):
            raise AssertionException(message)

    @staticmethod
    def is_integer(variable, message=None):
        """Checks whether the variable is an integer, if not throws an exception

        Args:
            variable: variable to be checked
            message: message for the exception

        Returns:
            None

        Raises:
            AssertionException
        """
        if not isinstance(variable, int):
            raise AssertionException(message)

    @staticmethod
    def is_positive_integer(variable, message=None):
        """Checks whether the variable is a positive integer, if not throws an exception

        Args:
            variable: variable to be checked
            message: message for the exception

        Returns:
            None

        Raises:
            AssertionException
        """
        if not (isinstance(variable, int) and variable > 0):
            raise AssertionException(message)

    @staticmethod
    def is_non_negative_integer(variable, message=None):
        """Checks whether the variable is a non-negative integer, if not throws an exception

        Args:
            variable: variable to be checked
            message: message for the exception

        Returns:
            None

        Raises:
            AssertionException
        """
        if not (isinstance(variable, int) and variable >= 0):
            raise AssertionException(message)

    @staticmethod
    def is_array(variable, message=None):
        """Checks whether the variable is an array, if not throws an exception
        Args:
            variable: variable to be checked
            message: message for the exception

        Returns:
            None

        Raises:
            AssertionException
        """
        if not isinstance(variable, list):
            raise AssertionException(message)

    @staticmethod
    def is_dict(variable, message=None):
        """Checks whether the variable is a dict, if not throws an exception

        Args:
            variable: variable to be checked
            message: message for the exception

        Returns:
            None

        Raises:
            AssertionException
        """
        if not isinstance(variable, dict):
            raise AssertionException(message)
