"""
This module defines throttle smtp stats related classes
"""
import urllib
from urllib import parse

class UrlUtils(object):
    """
    A Utility class for URL's
    """
    @staticmethod
    def url_fix_encode(url_str, charset='utf-8'):
        """Fix the url format
        Args:
            url_str - input url string
            charset - charset for encoding
        Raises:
            None
        """
        if isinstance(url_str, unicode):
            url_str = url_str.encode(charset, 'ignore')
        scheme, netloc, path, query_string, anchor = urlparse.urlsplit(url_str)
        path = urllib.quote(path, '/%')
        query_string = urllib.quote_plus(query_string, ':&=')
        return urlparse.urlunsplit((scheme, netloc, path, query_string, anchor))
