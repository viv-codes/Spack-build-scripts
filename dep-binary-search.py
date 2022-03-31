import os

def main():
    print("Enter the path for the package.py:")
    path=input()
    if path == "":
        print("Must provide an input path! Exiting!")
        exit()
    elif os.path.isdir(path):
        print("Must provide the path for the package.py! Exiting!")
        exit()
    elif os.path.isfile(path):
        with open(path) as package:
            lines = package.readlines()


if __name__ == "__main__":
    main()
