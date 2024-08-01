import re
import sys


def main():
    input_ = input("IPv4 Address: ")
    print(validate(input_))
    sys.exit()


def validate(ip):

    pattern =  r"^\d+\.\d+\.\d+\.\d+$"

    if re.match(pattern, ip):
        split = ip.split('.')
        for i in split:
            if int(i) > 255 or int(i) < 0 or (i == split[0] and (int(i) > 223 or int(i) < 1)):
                return False

        return True
    else:
        return False


if __name__ == "__main__":
    main()
