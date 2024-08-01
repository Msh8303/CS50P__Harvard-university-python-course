

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

        reg = r'(?<=embed\/).*?(?=")'
        if  html := re.search(reg,s):
            return f"https://youtu.be/{html.group(0)}"
        else:
            return None


if __name__ == "__main__":
    main()


