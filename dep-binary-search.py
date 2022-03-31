import os
import sys

def query():
    '''User query for first run only'''
    print("Enter the path for the package.py:")
    path=input()
    if (verifypath(path) == True):
        initialprep(path)
    
def verifypath(path):
    if path == "":
        print("Must provide an input path! Exiting!")
        exit()
    elif os.path.isdir(path):
        print("Must provide the path for the package.py! Exiting!")
        exit()
    elif os.path.isfile(path):
        return True

def continuitycheck():
    return os.path.exists(".depbininternal")
        
def initialprep(path):
    if (continuitycheck() == True):
        print("Tempfile from previous binary search found! Do you wish to overwrite this and start a new search: [y/n]:")
        choice=input()
        if (choice.lower() == "y"):
            pass
        else:
            print("Exiting!")
            exit()

    log=open(".depbsint", "w")
    with open(path) as package:
        lines = package.readlines()

def main():
    if (sys.argv[0] == "" or (sys.argv[0] == "start" and sys.argv[1] == None)): #! I need to confirm that this works as intended
        print("Starting new binary search!")
        query()
    elif (sys.argv[0] == "start" and sys.argv[1] != None):
        path=sys.argv[1]
        verifypath(path)
        initialprep(path)
    


if __name__ == "__main__":
    main()
