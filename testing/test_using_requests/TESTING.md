Note: When testing 'www.python.org' using <br>
```response = requests.head(url, timeout = 0.5, allow_redirects=True)```
<br>I received the following error message:<br>

```
 requests.exceptions.MissingSchema: 
    Invalid URL 'www.python.org': No scheme supplied. 
    Perhaps you meant https://www.python.org?
```

# The test
I updated the exceptions according and tested the following urls:

```
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
```

Note: the last example is a null string

```python testing/test_using_requests/test_requests.py```

# The Output
```
Regarding https://www.google.com/
Website is working fine.

Regarding https://www.biblehub.com/
Website is working fine.

Regarding http://www.stackoverflow.com
Website is working fine.

Regarding https://www.stackoverflow.com
Website is working fine.

Regarding https://www.example.com/
Website is working fine.

Regarding https://123.12.34.56:1234
Timed out.

Regarding http://10.0.0.1
Timed out.

Regarding https://www.python.org/
Website is working fine.

Regarding https://api.github.com
Website is working fine.

Regarding http://localhost:8080
The server could not connect with this url.

Regarding http://google.fr
Website is working fine.

Regarding http://notexist.kc
The server could not connect with this url.

Regarding http://google.frhttp://notexist.kc
The server could not connect with this url.

Regarding not a valid url
Badly formed url - There is no Schema.

Regarding http://google
The server could not connect with this url.

Regarding www.python.org
Badly formed url - There is no Schema.

Regarding http://foo.example.org/
The server could not connect with this url.

Regarding 
Badly formed url - There is no Schema.

```