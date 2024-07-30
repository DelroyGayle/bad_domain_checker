Regarding https://www.google.com/
Website is working fine
Regarding https://www.biblehub.com/
Website is working fine
Regarding http://www.stackoverflow.com
The server couldn't fulfill the request.
Error code:  403
Regarding https://www.stackoverflow.com
The server couldn't fulfill the request.
Error code:  403
Regarding https://www.example.com/
Website is working fine
Regarding https://123.12.34.56:1234
We failed to reach a server.
Reason:  timed out
Regarding http://10.0.0.1
We failed to reach a server.
Reason:  timed out
Regarding not a valid url
Not a valid url.
Reason:  unknown url type: 'not a valid url'
Regarding http://google
We failed to reach a server.
Reason:  [Errno -5] No address associated with hostname


SECOND TEST WITH SOME MORE URLS:

Regarding https://www.google.com/
Website is working fine
Regarding https://www.biblehub.com/
Website is working fine
Regarding http://www.stackoverflow.com
The server couldn't fulfill the request.
*Error code:  403*
Regarding https://www.stackoverflow.com
The server couldn't fulfill the request.
*Error code:  403*
Regarding https://www.example.com/
Website is working fine
Regarding https://123.12.34.56:1234
We failed to reach a server.
*Reason:  timed out*
Regarding http://10.0.0.1
We failed to reach a server.
*Reason:  timed out*
Regarding https://www.python.org/
Website is working fine
Regarding https://api.github.com
Website is working fine

# SAMPLE FAILURES:
Regarding http://localhost:8080
*We failed to reach a server.*
Reason:  [Errno 111] Connection refused
```Regarding not a valid url```
*Not a valid url.
Reason:  unknown url type: 'not a valid url'*
```Regarding http://google```
We failed to reach a server.
Reason:  [Errno -5] No address associated with hostname
```Regarding www.python.org```
Not a valid url.
Reason:  unknown url type: 'www.python.org'
```Regarding http://foo.example.org/```
We failed to reach a server.
Reason:  [Errno -2] Name or service not known