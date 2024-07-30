"""
Test URL validation using urllib.request
"""

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

urls = [
    # VALID
    'https://www.google.com/',
    'https://www.biblehub.com/',
    'http://www.stackoverflow.com',
    'https://www.stackoverflow.com',
    'https://www.example.com/',
    'https://123.12.34.56:1234',
    'http://10.0.0.1',
    # INVALID
    'not a valid url',
    'http://google'
]

for url in urls:
    try:
        request = Request(url)
    except ValueError as e:
        print('Regarding', url)
        print('Not a valid url.')
        print('Reason: ', e)
        continue
    else:
        try:
            response = urlopen(request, timeout=3)
        except HTTPError as e:
            print('Regarding', url)
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except URLError as e:
            print('Regarding', url)
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        except ValueError as e:
            print('Regarding', url)
            print('Not a valid url.')
            print('Reason: ', e)
        else:
            print('Regarding', url)
            print('Website is working fine')
