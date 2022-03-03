from ast import dump, literal_eval
from inMemoryDB import settings
import os
from inMemoryDB.config.conf import logger


def checkLengthValidity(arr, minLen):
    if len(arr) >= minLen:
        return True
    return False


def runner():

    while True:
        user_input = input()
        user_input = user_input.strip().split(" ")
        if user_input[0] == "set":
            # TODO move valid length of commans to one file
            if(checkLengthValidity(user_input, 3)):
                key = user_input[1]
                value = None
                try:
                    value = literal_eval(''.join(user_input[2:]))
                    setHandler(key, value)
                    logger("OK")
                except Exception as e:
                    logger("Invalid value")
            else:
                logger("Invalid command")

        elif user_input[0] == "get":
            if(checkLengthValidity(user_input, 2)):
                key = user_input[1]
                try:
                    value = getHandler(key)
                    logger(value)
                except Exception as e:
                    logger(e)
            else:
                logger("Invalid command")

        elif user_input[0] == "del":
            if(checkLengthValidity(user_input, 2)):
                key = user_input[1]
                try:
                    delHandler(key)
                    logger("OK")
                except Exception as e:
                    logger(e)
            else:
                logger("Invalid command")
        elif user_input[0] == "keys":
            if(checkLengthValidity(user_input, 2)):
                key = user_input[1]
                try:
                    matchedKeys = keysHandler(key)
                    logger(matchedKeys)
                except Exception as e:
                    logger(e)
            else:
                logger("Invalid command")
        elif user_input[0] == "use":
            if(checkLengthValidity(user_input, 2)):
                db_name = user_input[1]
                try:
                    useHandler(db_name)
                    logger('OK')
                except Exception as e:
                    logger(e)
            else:
                logger("Invalid command")

        elif user_input[0] == "list":
            if(checkLengthValidity(user_input, 1)):
                logger(listHandler())
            else:
                logger("Invalid command")
        elif user_input[0] == "db":
            if(checkLengthValidity(user_input, 1)):
                logger(sayDBHandler())
            else:
                logger("Invalid command")
        elif user_input[0] == "dump":
            if(checkLengthValidity(user_input, 3)):
                db_name = user_input[1]
                db_path = user_input[2]
                try:
                    dumpDBHandler(db_name, db_path)
                    logger("OK")
                except Exception as e:
                    logger(e)
            else:
                logger("Invalid command")
        elif user_input[0] == "load":
            if(checkLengthValidity(user_input, 3)):
                db_path = user_input[1]
                db_name = user_input[2]
                try:
                    loadDBHandler(db_name, db_path)
                    logger("OK")
                except Exception as e:
                    logger(e)
            else:
                logger("Invalid command")
        elif user_input[0] == "exit":
            break
        else:
            logger("Invalid command")


if __name__ == "__main__":
    # print(literal_eval("[1, '2', [1,2,'3']]"))
    settings.init()
    from inMemoryDB.commands.handlers import sayDBHandler, setHandler, getHandler, delHandler, keysHandler, useHandler, listHandler, dumpDBHandler, loadDBHandler
    runner()
