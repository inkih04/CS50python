import sys
from tabulate import tabulate
import csv

def main():
    reader = get_dic()
    print(tabulate(reader[0],headers="keys",tablefmt="grid"))
    reader[1].close()




def get_dic():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        try:
            file = open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            reader = csv.DictReader(file)
            return [reader, file]


if __name__ == "__main__":
    main()