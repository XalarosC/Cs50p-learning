import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    valid_extensions = (".jpg", ".jpeg", ".png")

    if not sys.argv[1].endswith(valid_extensions) or not sys.argv[2].endswith(valid_extensions):
        sys.exit("Invalid input or output extension")

    if sys.argv[1].split('.')[-1] != sys.argv[2].split('.')[-1]:
        sys.exit("Input and output have different extensions")
    else:
        edit(sys.argv[1], sys.argv[2])

def edit(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

if __name__ == "__main__":
    main()
