import re
import sys


def main():
    print(convert(input("Hours: ")))


def format_minutes(l):
    correct = True
    if l[1] == ":" and int(l[2]) > 59:
        correct = False
    if l[5] == ":" and int(l[6]) > 59:
        correct = False
    return correct


def format_time(h, m, t):
    hour = h
    if t == "AM" and int(h) < 12:
        hour = int(h)
    elif t == "AM" and int(h) == 12:
        hour = 0
    if t == "PM" and int(h) < 12:
        hour = int(int(h) + 12)
    if not m:
        m = 0
    else:
        int(m)
    return f"{hour:02}:{m:02}"



def convert(s):
    pattern = r"^([0-9]{1,2})(:)?([0-9][0-9])?[\s]([A|P]M)[a-z\s]+([0-9]{1,2})(:)?([0-9][0-9])?[\s]([A|P]M)$"
    matches = re.search(pattern, s)
    if matches:
        hours = matches.groups()
        if int(hours[0]) > 12 or int(hours[4]) > 12 or not format_minutes(hours):
            raise ValueError
        else:
            return f"{format_time(hours[0], hours[2], hours[3])} to {format_time(hours[4], hours[6], hours[7])}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()