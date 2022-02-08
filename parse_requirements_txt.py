def main():
    print('Should version numbers be appended? y/[n]')
    version = input()
    if version == "":
        version = "n"
    with open("requirements.txt") as file:
        Lines = file.readlines()
        for line in Lines:
            output = line.split('==')[0]
            vernum = line.split('==')[1]
            vernum = vernum.strip()
            if version == "n":
                print("    depends_on('py-" + output +"', type=('build', 'run'))", end="\n")
            elif version == "y":
                print("    depends_on('py-" + output + "@" +vernum+"', type=('build', 'run'))", end="\n")

if __name__ == "__main__":
    main()
