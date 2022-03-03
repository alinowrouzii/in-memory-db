from inMemoryDB.settings import dbs, db_in_use
from ..config.conf import logger
from ..utils.util import findMatchedKeys

def setHandler(key, value):
    db = dbs[db_in_use]

    db[key] = value

    dbs[db_in_use] = db


def getHandler(key):
    db = dbs[db_in_use]

    try:
        return db[key]
    except Exception:
        raise Exception("Key does not exist")


def delHandler(key):
    db = dbs[db_in_use]
    try:
        del db['key']
        dbs[db_in_use] = db
    except Exception:
        raise Exception("Key does not exist")

def keysHandler(regex):
    db = dbs[db_in_use]
    return findMatchedKeys(db, regex)

def useHandler(db_name):
    if db_name in dbs:
        # TODO check below
        # global db_in_use
        db_in_use = db_name
    else:
        raise Exception("DB not exists")

def sayDBHandler():
    return db_in_use

def listHandler():
    return dbs.keys()


