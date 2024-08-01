import os
import sys
from PIL import Image, ImageOps


def check_(input_i):
    valid_suffix = ["jpg", "png", "jpeg"]
    _, suffix = input_i.split(".", maxsplit=1)
    if suffix in valid_suffix:
        return True
    else:
        return False


def same_(input_i, output_i):
    _, suffix = input_i.split(".", maxsplit=1)
    if output_i.endswith(suffix):
        return True
    else:
        return False


def shirt_(input_i, output_i):
    shirt = Image.open("shirt.png")
    input_pic = Image.open(input_i)

    x, y = shirt.size
    input_pic = ImageOps.fit(input_pic, (x, y))

    input_pic.paste(shirt, shirt)
    input_pic.save(output_i)


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif not os.path.isfile(sys.argv[1]):
    print("Input does not exist")
    sys.exit(1)
elif not check_(sys.argv[1]) and check_(sys.argv[2]):
    print("Invalid input")
    sys.exit(1)
elif not same_(sys.argv[1], sys.argv[2]):
    print("Input and output have different ")
    sys.exit(1)
else:
    shirt_(sys.argv[1], sys.argv[2])
