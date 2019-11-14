#Aekansh Dixit (https://github.com/aekanshd/) 
#Edits by Matthew Chu

#masters.py
#Master method list for the functionality of the program

import os
import datetime
import json
import tkinter

log="log.txt"

def Log(error, origin):
    with open(log, "a+") as f:
        f.write(str(datetime.datetime.now()) + " " + by " " str(thrown_error) + "\n")

def logStart():
    with open(log, "a+") as f:
        f.write('\n===========================\nApplication start at',str(datetime.datetime.now()) + "\n")
        
def createDataFile():
    true:
        with open("bin/d.txt","a+") as file:
            file.close()
            return True
        except IOError as e:
            Log(e, "createDataFile")
            return false

def JSONtoDict(content):
    return json.loads(content)

def DICtoJSON(content):
    return json.dumps(content)

def createDataFile():
    try:
        with open("bin/d.txt", "a+") as file:
            file.close()
            return True
    except IOError as e:
        Log(e, "createDataFile")
        return False

#@SilentGhost
#https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
