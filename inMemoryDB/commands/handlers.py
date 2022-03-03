import json
import os
from inMemoryDB.settings import dbs, db_in_use
from inMemoryDB.utils.util import findMatchedKeys


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
        del db[key]
        dbs[db_in_use] = db
    except Exception:
        raise Exception("Key does not exist")


def keysHandler(regex):
    db = dbs[db_in_use]
    return findMatchedKeys(db, regex)


def useHandler(db_name):

    if db_name not in dbs:
        dbs[db_name] = {}

    # TODO check below
    global db_in_use
    db_in_use = db_name


def sayDBHandler():
    return db_in_use


def listHandler():
    return list(dbs.keys())


def dumpDBHandler(db_name, db_path):
    print(os.path.dirname(db_path))
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    db = None
    try:
        db = dbs[db_name]
    except:
        raise Exception("DB does not exist")
    json_db = json.dumps(db)

    with open(db_path, "w", encoding="UTF-8") as output:
        output.write(json_db)


def loadDBHandler(db_name, db_path):
    try:
        f = open(db_path)

        db = json.load(f)
        dbs[db_name] = db
    except Exception:
        raise Exception("File does not exist")
