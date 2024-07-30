Regarding https://www.google.com/<br>
Website is working fine<br>
Regarding https://www.biblehub.com/<br>
Website is working fine<br>
Regarding http://www.stackoverflow.com<br>
The server couldn't fulfill the request.<br>
Error code:  403<br>
Regarding https://www.stackoverflow.com<br>
The server couldn't fulfill the request.<br>
Error code:  403<br>
Regarding https://www.example.com/<br>
Website is working fine<br>
Regarding https://123.12.34.56:1234<br>
We failed to reach a server.<br>
Reason:  timed out<br>
Regarding http://10.0.0.1<br>
We failed to reach a server.<br>
Reason:  timed out<br>
Regarding not a valid url
Not a valid url.<br>
Reason:  unknown url type: 'not a valid url'<br>
Regarding http://google
We failed to reach a server.<br>
Reason:  [Errno -5] No address associated with hostname<br>


SECOND TEST WITH SOME MORE URLS:


Regarding https://www.google.com/<br>
Website is working fine<br>
Regarding https://www.biblehub.com/<br>
Website is working fine<br>
Regarding http://www.stackoverflow.com<br>
The server couldn't fulfill the request.<br>
*Error code:  403*<br>
Regarding https://www.stackoverflow.com<br>
The server couldn't fulfill the request.<br>
*Error code:  403*<br>
Regarding https://www.example.com/<br>
Website is working fine<br>
Regarding https://123.12.34.56:1234<br>
We failed to reach a server.<br>
*Reason:  timed out*<br>
Regarding http://10.0.0.1<br>
We failed to reach a server.<br>
*Reason:  timed out*<br>
Regarding https://www.python.org/<br>
Website is working fine<br>
Regarding https://api.github.com<br>
Website is working fine<br>
<br>
# SAMPLE FAILURES:<br>
Regarding http://localhost:8080<br>
*We failed to reach a server.*<br>
Reason:  [Errno 111] Connection refused<br>
```Regarding not a valid url```<br>
*Not a valid url.<br>
Reason:  unknown url type: 'not a valid url'*<br>
```Regarding http://google```<br>
We failed to reach a server.<br>
Reason:  [Errno -5] No address associated with hostname<br>
```Regarding www.python.org```<br>
Not a valid url.<br>
Reason:  unknown url type: 'www.python.org'<br>
```Regarding http://foo.example.org/```<br>
We failed to reach a server.<br>
Reason:  [Errno -2] Name or service not known<br>