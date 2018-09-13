"""
This module defines string utilities
"""
from exceptions.assertion import Assertion


class StringUtils(object):
    """
    A Utility class for strings
    """

    @staticmethod
    def str_to_boolean(string_value):
        """Convert string to boolean

        Args:
            string_value: input boolean string

        Returns:
            boolean value of the given string

        Raises:
            None
        """
        Assertion.is_string(string_value, 'Invalid String Value')
        return string_value.lower() in ("yes", "true", "t", "1")

    @staticmethod
    def to_str(bytes_or_str):
        """Converts to string if the input is a byte

        Args:
            bytes_or_str: bytes or str

        Returns:
            string value of the given input

        Raises:
            None
        """
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode('utf-8')
        else:
            value = bytes_or_str
        return value

    @staticmethod
    def to_bytes(bytes_or_str):
        """Converts to bytes if the input is a string

        Args:
            bytes_or_str: instance of bytes

        Returns:
            byte value of the given input

        Raises:
            None
        """
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode('utf-8')
        else:
            value = bytes_or_str
        return value
