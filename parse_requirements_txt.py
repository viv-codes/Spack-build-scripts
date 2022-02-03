def main():
    with open("requirements.txt") as file:
        Lines = file.readlines()
        for line in Lines:
            output = line.split('==')[0]
            print("    depends_on('py-" + output +"', type=('build', 'run'))", end="\n")

if __name__ == "__main__":
    main()
