#Matthew Chu
#salt.py(ap.py)

#Methods to generate and read a 5byte salt key

import os

#will change current salt in file, ONLY USE ONCE
def genSalt():
    s=os.urandom(5)
    with open('salt.txt','w+') as f:
        f.write(s)

def readSalt():
    with open('salt.txt','r') as f:
        return f.readline()
