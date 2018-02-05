"""
This module defines string utilities
"""
class StringUtils(object):
    """
    A Utility class for strings
    """
    @staticmethod
    def string_to_boolean(string_value):
        """Returns boolean of the input string
        Args:
            string_value - input boolean string
        Raises:
            None
        """
        return string_value.lower() in ("yes", "true", "t", "1")
