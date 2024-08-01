import os
import sys


def count_(python_file):
    with open(python_file, 'r') as lines:
        none_code = 0
        number_of_lines = len(lines.readlines())
        lines.seek(0)
        for line in lines:
            if (line.strip().startswith("#")
                or line.isspace()
                    or line.strip().startswith("\n")):
                none_code += 1
        return (number_of_lines - none_code)


if (len(sys.argv) < 2):
    print("Too few command-line arguments")
    sys.exit(1)
elif (len(sys.argv) > 2):
    print("Too many command-line arguments")
    sys.exit(1)
elif not os.path.isfile(sys.argv[1]):
    print("File does not exist")
    sys.exit(1)
elif not sys.argv[1].endswith(".py"):
    print("Not a Python file")
    sys.exit(1)
else:
    print(count_(sys.argv[1]))
