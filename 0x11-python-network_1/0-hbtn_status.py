#!/usr/bin/python3
""" Module to fetche https://alx-intranet.hbtn.io/status
"""

import urllib.request as re


def fetch():
    """ Function to fetche https://alx-intranet.hbtn.io/status
    """
    with re.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body response:')
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")


if __name__ == '__main__':
    fetch()
