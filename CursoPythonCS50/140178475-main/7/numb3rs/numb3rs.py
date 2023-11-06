import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    if re.search(r"^[0-9]+\.+[0-9]+\.+[0-9]+\.+[0-9]+$", ip):
        list_num = ip.split(".")
        for number in list_num:
            if int(number) > 255 or int(number) < 0:
                return False
        return True
    return False


...


if __name__ == "__main__":
    main()