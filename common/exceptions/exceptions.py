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
            self     - PreconditionException
            message  - message
        Raises:
            None
        """
        self.message = message

    def __str__(self):
        """To String
        Args:
            self - PreconditionException
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
            self     - AssertionException
            message  - message
        Raises:
            None
        """
        self.message = message

    def __str__(self):
        """To String
        Args:
            self - AssertionException
        Raises:
            None
        """
        return self.message
