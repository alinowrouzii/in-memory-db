from ..settings import dbs, db_in_use
from ..config.conf import logger

def setHandler(key, value):
    db = dbs[db_in_use]
    
    # if key in db:
    #     logger("Key already exists")
    # else:
    db[key] = value