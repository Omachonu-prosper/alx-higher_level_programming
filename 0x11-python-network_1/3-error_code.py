#!/usr/bin/python3
"""Python script that:
    takes in a URL
    sends a request to the URL
    displays the body of the response (decoded in utf-8)
"""

import urllib.request as re
import urllib.error as err
import sys


def main(url):
    """Entry point
    """
    request = re.Request(url)
    try:
        with re.urlopen(request) as res:
            print(res.read().decode('utf-8'))
    except err.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
