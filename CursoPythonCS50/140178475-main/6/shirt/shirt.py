import sys
import os
from PIL import Image, ImageOps


def main():
    if check_comand_line_argument():
        try:
            image = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("Input does not exist")
        else:
            shirt = Image.open("shirt.png")
            size = shirt.size
            muppet = ImageOps.fit(image, size)
            muppet.paste(shirt, shirt)
            muppet.save(sys.argv[2])


def check_comand_line_argument():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too many command-line arguments ")
    else:
        extension1 = os.path.splitext(sys.argv[1])
        extension2 = os.path.splitext(sys.argv[2])
        if not check_extension(extension1[1]) or not check_extension(extension2[1]):
            sys.exit("Invalid input")
        elif extension1[1].lower() != extension2[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            return True


def check_extension(ext):
    return ext in [".jpg", ".jpeg", ".png"]


if __name__ == "__main__":
    main()