from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def check_input(birth_date):
    pattern = r"^([0-9]{4})-([0-1]{1}[0-9]{1})-([0-3]{1}[0-9]{1})$"
    matches = re.search(pattern, birth_date)
    if matches:
        year, month, day = birth_date.split("-")
        if(0 < int(month) < 13):
            return year, month, day


def main():
    birth_date = input("Date of Birth: ")
    try:
       year, month, day = check_input(birth_date)
    except TypeError:
        sys.exit("Invalid Date")
    else:
        date_of_birth = date(int(year), int(month), int(day))
        date_of_today = date.today()
        diff = date_of_today - date_of_birth
        total = diff.days *24*60
        output = p.number_to_words(total, andword= "")
        print(output.capitalize()+ " minutes")



if __name__ == "__main__":
    main()