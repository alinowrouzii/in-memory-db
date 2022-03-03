from nis import cat
from warnings import catch_warnings
from ..settings import dbs, db_in_use
from ..config.conf import logger

def getHandler(key):
    db = dbs[db_in_use]
    
    try:
        return db[key]
    except Exception:
        logger("Key does not exists")
        