#!/usr/bin/python3
"""Python script that
takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
displays the body of the response (decoded in utf-8)
"""

import urllib.request as re
import urllib.parse
import sys


def main(url, email):
    """Entry Point
    """
    data = {'email': email}
    data = urllib.parse.urlencode(data).encode("ascii")
    request = re.Request(url, data)
    with re.urlopen(request) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    main(url, email)
