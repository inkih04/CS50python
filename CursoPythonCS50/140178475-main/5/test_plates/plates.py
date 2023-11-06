def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first = False
    if not s[0].isalpha() and not s[1].isalpha():
        return False
    if not s.lower().isalnum():
        return False
    if len(s) > 6 or len(s) < 2:
        return False
    for c in s:
        if c.isdigit() and not first:
            first = True
            if c == "0":
                return False

        if first and not c.isdigit():
            return False
    return True


main()

