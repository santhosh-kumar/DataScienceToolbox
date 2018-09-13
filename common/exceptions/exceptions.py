"""
This file defines Exception Classes
"""


class PreconditionException(Exception):
    """
    PreconditionException is thrown when the precondition 
    check fails
    """

    def __init__(self, message):
        """Init PreconditionException

        Args:
            self: PreconditionException
            message: message

        Returns:
            None

        Raises:
            None
        """
        self.message = message

    def __str__(self):
        """To String
        Args:
            self: PreconditionException

        Returns:
            None

        Raises:
            None
        """
        return self.message


class AssertionException(Exception):
    """
    AssertionException is thrown when the assertion 
    check fails
    """

    def __init__(self, message):
        """Init AssertionException

        Args:
            self: AssertionException
            message: message

        Returns:
            None

        Raises:
            None
        """
        self.message = message

    def __str__(self):
        """To String

        Args:
            self: AssertionException

        Returns:
            Exception message as a string.

        Raises:
            None
        """
        return self.message


class UnsupportedPythongException(Exception):
    """
    UnsupportedPythongException is thrown when the python version is not supported
    """

    def __init__(self, message):
        """Init UnsupportedPythongException

        Args:
            self: UnsupportedPythongException
            message: message

        Returns:
            None

        Raises:
            None
        """
        self.message = message

    def __str__(self):
        """To String

        Args:
            self: UnsupportedPythongException

        Returns:
            Exception message as a string.

        Raises:
            None
        """
        return self.message


class ArgumentParserFailureException(Exception):
    """
    ArgumentParserFailureException is thrown when argument parsing fails
    """

    def __init__(self, message):
        """Init ArgumentParserFailureException
        Args:
            self     - ArgumentParserFailureException
            message  - message
        Raises:
            None
        """
        self.message = message

    def __str__(self):
        """To String
        Args:
            self - ArgumentParserFailureException
        Raises:
            None
        """
        return self.message
