def main():
    text = input("Greeting: ")
    print(f"${value(text)}")


def value(text):
    if "Hello" in text:
        return 0
    elif text[0] == "H":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()