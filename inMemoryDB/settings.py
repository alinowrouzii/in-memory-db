# settings.py

DEBUG = True


def init():
    global dbs
    dbs = {}
    dbs["default"] = {}

    global db_in_use
    db_in_use = "default"

    if DEBUG:
        dbs["default"]['ali'] = 'nowrouzi'
        dbs["default"]['alii'] = '123'
        dbs["default"]['mamad'] = 444