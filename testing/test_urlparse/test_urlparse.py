"""
Test URL validation using urlparse
"""

from urllib.parse import urlparse

urls = [
    # VALID
    'https://www.google.com/',
    'https://www.biblehub.com/',
    'http://www.stackoverflow.com',
    'https://www.example.com/',
    'https://123.12.34.56:1234',
    'http://10.0.0.1',
    # INVALID
    'not a valid url',
    'http://google'
]

for url in urls:
    print(url, urlparse(url))