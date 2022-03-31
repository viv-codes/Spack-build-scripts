import json
import os
import sys

CONFIGFILE = ".DepBinSearchCfg"
filepath = None

def query():
    '''User query for first run only'''
    print("Enter the filepath for the package.py:")
    filepath=input()
    if (verifyfilepath(filepath) == True):
        initialprep(filepath)
    
def verifyfilepath(filepath):
    if filepath == "":
        print("Must provide an input filepath! Exiting!")
        exit()
    elif os.path.isdir(filepath):
        print("Must provide the filepath for the package.py! Exiting!")
        exit()
    elif os.path.isfile(filepath):
        return True

def continuitycheck():
    return os.path.exists(".depbininternal")
        
def initialprep(filepath):
    if (continuitycheck() == True):
        print("Tempfile from previous binary search found! Do you wish to overwrite this and start a new search: [y/n]:")
        choice=input()
        if (choice.lower() == "y"):
            pass
        else:
            print("Exiting!")
            exit()

    log=open(".depbsint", "w")
    with open(filepath) as package:
        lines = package.readlines()

def save(self):
    binsearchstep = None # TODO Hook here
    savefilepath = filepath
    data = {
        'binsearchstep':binsearchstep,
        'savefilepath':filepath,
    }
    with open(CONFIGFILE, 'w') as f:
        json.dump(data, f)

def load(self):
    if os.path.exists(CONFIGFILE):
        with open(CONFIGFILE, 'r') as f:
            data = json.load(f)
        binsearchstep = data['binsearchstep']
        filepath = data['savefilepath']


def main():
    if (sys.argv[0] == "" or (sys.argv[0] == "start" and sys.argv[1] == None)):
        print("Starting new binary search!")
        query()
    elif (sys.argv[0] == "start" and sys.argv[1] != None):
        filepath=sys.argv[1]
        verifyfilepath(filepath)
        initialprep(filepath)
    


if __name__ == "__main__":
    main()
