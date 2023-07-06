#!/usr/bin/python3
"""Python script that
takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
displays the body of the response (decoded in utf-8)
"""

import urllib.request as re
import sys


def main(url, email):
    """Entry Point
    """
    request = re.Request(url, email=email)
    request.method = 'POST'
    with re.urlopen(url) as response:
        print(response)


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    main(url, email)
