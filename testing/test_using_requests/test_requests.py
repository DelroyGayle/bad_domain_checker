"""
Test URL validation using requests
"""

import requests

urls = [
    # VALID FORMED URLS
    'https://www.google.com/',
    'https://www.biblehub.com/',
    'http://www.stackoverflow.com',
    'https://www.stackoverflow.com',
    'https://www.example.com/',
    'https://123.12.34.56:1234',
    'http://10.0.0.1',
    'https://www.python.org/',
    'https://api.github.com',
    'http://localhost:8080',
    'http://google.fr',
    'http://notexist.kc',
    # INVALID FORMED URLS
    'http://google.frhttp://notexist.kc',
    'not a valid url',
    'http://google',
    'www.python.org',
    'http://foo.example.org/',
    ''
]

for url in urls:
    try:
        response = requests.head(url, timeout = 0.5, allow_redirects=True)
    except requests.exceptions.Timeout:
        print('Regarding', url)
        print('Timed out.\n')
    except requests.exceptions.ConnectionError:
        print('Regarding', url)
        print('The server could not connect with this url.\n')
    except requests.exceptions.MissingSchema:
        print('Regarding', url)
        print('Badly formed url - There is no Schema.\n')
    else:
        print('Regarding', url)
        print('Website is working fine.\n')
