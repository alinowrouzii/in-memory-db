import re

def findMatchedKeys(dict, regex):
    try:
        r = re.compile(regex)
        return list(filter(r.match, dict.keys()))
    except Exception:
        raise Exception("Invalid regular expression")
