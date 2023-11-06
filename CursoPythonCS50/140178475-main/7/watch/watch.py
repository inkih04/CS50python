import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>",s):
        if matches := re.search(r"https?://(?:www\.)?youtube\.com/embed/([\w]+)",s):
            url = matches.group(1)
            return f"https://youtu.be/{url}"


if __name__ == "__main__":
    main()