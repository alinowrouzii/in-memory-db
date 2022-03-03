# settings.py


def init():
    global dbs
    dbs = {}
    dbs["default"] = {}
    
    global db_in_use
    db_in_use = "default"
