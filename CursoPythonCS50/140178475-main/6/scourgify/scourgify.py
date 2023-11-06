import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too much command-line arguments")
    else:
        students = get_dic()
        write_dic(students)


def get_dic():
    students = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"].strip('"')
                name = name.strip(" ")
                last, first = name.split(",")
                students.append({"first": first.strip(), "last": last.strip(), "house": row["house"].strip()})
    except FileNotFoundError:
        sys.exit("Could not read " + sys.argv[1])
    else:
        return students


def write_dic(students):
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader() #escribir encabezados
        for row in students:
            writer.writerow(row)

if __name__ == "__main__":
    main()