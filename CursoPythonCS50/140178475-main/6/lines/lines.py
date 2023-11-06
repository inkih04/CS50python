import sys


def main():
    file = get_file()
    lines = file.readlines()
    counter = 0
    for line in lines:
        line = line.lstrip() #elimina lineas en blanco
        if not line.startswith("#") and len(line) != 0:
            counter += 1
    print(counter)


def get_file():
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments")
    else:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")
        try:
            file = open(sys.argv[1], "r")
        except FileNotFoundError:
            sys.exit("Not a Python file")
        else:
            return file



if __name__ == "__main__":
    main()

