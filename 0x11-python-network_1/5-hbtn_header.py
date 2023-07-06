#!/usr/bin/python3
"""Python script that:
    takes in a URL
    sends a request to the URL
    displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys


def main(url):
    """Entry Point
    """
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
