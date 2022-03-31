import json
import os
import sys

CONFIGFILE = ".DepBinSearchCfg"

# TODO THESE MAY NEED TO BE CHANGED
filepath = None
numdeps = 0
binsearchstep = 0


def query():
    """User query for first run only"""
    print("Enter the filepath for the package.py:")
    filepath = input()
    if verifyfilepath(filepath) == True:
        initialprep(filepath)


def verifyfilepath(filepath):
    """Verifies that the user provided path for the package.py exists and is a file"""
    # TODO try catch filenotexists
    if filepath == "":
        print("Must provide an input filepath! Exiting!")
        exit()
    elif os.path.isdir(filepath):
        print("Must provide the filepath for the package.py! Exiting!")
        exit()
    elif os.path.isfile(filepath):
        return True


# def continuitycheck():
#     return os.path.exists(".depbininternal")


def initialprep(filepath):
    # if continuitycheck() == True:
    #     print(
    #         "Tempfile from previous binary search found! Do you wish to overwrite this and start a new search: [y/n]:"
    #     )
    #     choice = input()
    #     if choice.lower() == "y":
    #         pass
    #     else:
    #         print("Exiting!")
    #         exit()
    parsepackage(filepath)


def parsepackage(filepath):
    """Parses the input package for numdeps and calls binary search"""
    with open(filepath) as package:
        for line in package:
            numdeps += line.count("depends_on")
    binarysearch(filepath, numdeps)


def binarysearch(filepath, numdeps):
    """Performs the binary splits and comments out lines as required"""
    if binsearchstep == 0:
        tocomment = numdeps // 2
        with open(filepath, "r") as package:
            lines = package.readlines()
            while tocomment > 0:
                for index, line in enumerate(lines):
                    if "depends_on" in line:
                        lines[index] = "#" + line
                        tocomment -= 1
                    else:
                        lines[index] = line
        with open(filepath, "w") as package:
            for line in lines:
                package.write(line)


def save(self):
    """Writes the current state of the program out to a JSON"""
    data = {"binsearchstep": binsearchstep, "filepath": filepath, "numdeps": numdeps}
    with open(CONFIGFILE, "w") as f:
        json.dump(data, f)


def load(self):
    """Loads the state of the program from a JSON"""
    if os.path.exists(CONFIGFILE):
        with open(CONFIGFILE, "r") as f:
            data = json.load(f)

        # TODO must veify that these actually override the global variables. I might have to do this differently.
        self.binsearchstep = data["binsearchstep"]
        self.filepath = data["filepath"]
        self.numdeps = data["numdeps"]


def main():
    if sys.argv[0] == "" or (sys.argv[0] == "start" and sys.argv[1] == None):
        print("Starting new binary search!")
        query()
    elif sys.argv[0] == "start" and sys.argv[1] != None:
        filepath = sys.argv[1]
        verifyfilepath(filepath)
        initialprep(filepath)


if __name__ == "__main__":
    main()
