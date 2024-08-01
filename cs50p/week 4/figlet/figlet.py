from pyfiglet import Figlet

import sys


if len(sys.argv) == 1:

    figlet = Figlet()
    figlet.getFonts()
    input_ = input()
    print(figlet.renderText(input_))

elif sys.argv[1] in ["-f", "--font"]:

    figlet = Figlet()
    fonts_ = figlet.getFonts()
    if sys.argv[2] not in fonts_:
        sys.exit("Invalid usage")
    figlet.setFont(font = sys.argv[2])
    input_ = input()
    print(figlet.renderText(input_))

else:
    sys.exit("Invalid usage")