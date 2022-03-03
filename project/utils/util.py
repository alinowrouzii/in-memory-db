import re

def findMatchedKeys(dict, regex):
    pass
    r = re.compile(regex)
    return list(filter(r.match, dict.keys()))
