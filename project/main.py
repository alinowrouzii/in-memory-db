from ast import literal_eval
import settings
import os
from commands.handlers import sayDBHandler, setHandler, getHandler, delHandler, keysHandler, useHandler, listHandler
from config.conf import logger


def checkLengthValidity(arr, minLen):
    if len(arr) >= minLen:
        return True
    return False

def runner():
    
    while True:
        pass
        user_input = input()
        user_input = user_input.strip().split(" ")
        if user_input[0] =="set":
            # TODO move valid length of commans to one file
            if(checkLengthValidity(user_input, 3)):
                key = user_input[1]
                value = None
                try:
                    value = literal_eval(user_input[2])
                    setHandler(key, value)
                except Exception:
                    logger("Invalid value")
            else:
                logger("Invalid command")
        
        elif user_input[0] =="get":
            if(checkLengthValidity(user_input, 2)):
                key = user_input[1]
                try:
                    value  = getHandler(key)
                    logger(value)
                except Exception as e:
                    print(e)
                    logger("Key does not exist")
            else:
                logger("Invalid command")
        
        elif user_input[0] =="del":
            if(checkLengthValidity(user_input, 2)):
                key = user_input[1]
                try:
                    delHandler(key)
                except Exception as e:
                    print(e)
                    logger("Key does not exist")
            else:
                logger("Invalid command")
        elif user_input[0] =="keys":
            if(checkLengthValidity(user_input, 2)):
                key = user_input[1]
                matchedKeys = keysHandler(key)
                logger(matchedKeys)
            else:
                logger("Invalid command")
        elif user_input[0] =="use":
            if(checkLengthValidity(user_input, 2)):
                db_name = user_input[1]
                try:
                    useHandler(db_name)
                except Exception as e:
                    print(e)
                    logger("DB does not exist")
            else:
                logger("Invalid command")
            
        elif user_input[0] =="list":
            if(checkLengthValidity(user_input, 1)):
                listHandler()
            else:
                logger("Invalid command")
        elif user_input[0] =="db":
            if(checkLengthValidity(user_input, 1)):
                sayDBHandler()
            else:
                logger("Invalid command")
        elif user_input[0] =="dump":
            pass
        elif user_input[0] =="load":
            pass
        elif user_input[0] =="exit":
            break
        


if __name__ == "__main__":
    settings.init()
    runner()