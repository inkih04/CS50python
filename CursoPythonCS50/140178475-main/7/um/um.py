import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    list_match = re.findall(r"(\b\W*um\W)|^um|um$", s)
    return len(list_match)


if __name__ == "__main__":
    main()