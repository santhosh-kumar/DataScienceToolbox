"""
This module defines string utilities
"""


class StringUtils(object):
    """
    A Utility class for strings
    """

    @staticmethod
    def str_to_boolean(string_value):
        """Returns boolean of the input string
        Args:
            string_value - input boolean string
        Raises:
            None
        """
        return string_value.lower() in ("yes", "true", "t", "1")

    @staticmethod
    def to_str(bytes_or_str):
        """Returns an instance of str
        Args:
            bytes_or_str - bytes or str
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
        """Returns an instance of bytes
        Args:
            bytes_or_str - instance of bytes
        Raises:
            None
        """
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode('utf-8')
        else:
            value = bytes_or_str
        return value
