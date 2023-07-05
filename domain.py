import json
import logging
import sys
import requests

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stderr))
logger.setLevel(logging.DEBUG)

r = {}

def check_domains_alive(*domains):
    for i in domains:
        r[i] = False
        for j in range(3):
            try:
                res = requests.get("https://%s" % i, timeout=3)
                logger.debug("Checked %s, result %s" % (i, res))
            
                if res.status_code == 200:
                    r[i] = True
                    break
            except BaseException as exc:
                logger.debug("Checked %s, exception %s" % (i, exc))
                continue

    return r

print(json.dumps(check_domains_alive(*sys.argv[1:]), indent=4))