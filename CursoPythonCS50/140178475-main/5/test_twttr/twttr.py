def main():
    txt = input("Input: ")
    print("Output: ", end = "")
    print(shorten(txt))


def shorten(word):
    output = ""
    for c in word:
        x = c.lower()
        if x != "a" and x != "e" and x != "i" and x != "o" and x != "u":
            output += c
    return output

if __name__ == "__main__":
    main()