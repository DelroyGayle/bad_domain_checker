# Check if domains are alive

Example:
```sh
python3 domain.py google.com httpbin.org bad.domain microsoft.com > result.json
```
will print to `result.json`:
```json
{
    "google.com": true,
    "httpbin.org": true,
    "bad.domain": false,
    "microsoft.com": true
}
```