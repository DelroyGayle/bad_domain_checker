import json
import logging
import sys
import requests

LIMIT_OF_TRIES = 3
OK_STATUS = 200
TIME_OUT_VALUE = 3

DOMAIN_ALIVE = 0
DOMAIN_DEAD = 1
DOMAIN_CHECK_FAILED = 2
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stderr))
logger.setLevel(logging.DEBUG)


def check_domains_alive(*domains):
    results = {}
    for domain in domains:
        results[domain] = DOMAIN_DEAD
        for each_try in range(LIMIT_OF_TRIES):
            try:
                result = requests.get("https://%s" % domain, timeout=TIME_OUT_VALUE)
                logger.debug("Checked %s, result %s" % (domain, result))
            
                print(result.headers)
                if result.status_code == OK_STATUS:
                    results[domain] = DOMAIN_ALIVE
                    break
            except BaseException as exc:
                logger.debug("Checked %s, exception %s" % (domain, exc))
                results[domain] = DOMAIN_CHECK_FAILED
                continue

    return results

# print(json.dumps(check_domains_alive(*sys.argv[1:]), indent=4))

res1 = check_domains_alive('google.com')
res2 = check_domains_alive('biblehub.com')
print(res2)