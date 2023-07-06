#!/usr/bin/python3
"""Python script that:
    takes in a URL
    sends a request to the URL
    displays the body of the response
"""

import sys
import requests


def main(url):
    """Entry Point
    """
    req = requests.get(url)
    code = req.status_code
    if code >= 400:
        print(f"Error code: {code}")
    else:
        print(req.text)


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
