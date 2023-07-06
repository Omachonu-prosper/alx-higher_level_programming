#!/usr/bin/python3
"""Python script that
takes in a URL
sends a request to the URL
displays the value of the X-Request-Id in the header of the response
"""

import urllib.request as re
import sys


def fetch(url):
    """Fetch function
    """
    with re.urlopen(url) as res:
        headers = res.getheaders()
        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])


if __name__ == '__main__':
    url = sys.argv[1]
    fetch(url)
