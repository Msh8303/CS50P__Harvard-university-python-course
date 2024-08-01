import csv
import sys
import os
import tabulate


def csv_(csv_file):
    with open(csv_file, 'r') as csv_file:
        list_ = list(csv.reader(csv_file.readlines()))
        print((tabulate.tabulate(list_, headers="firstrow", tablefmt="grid")))


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
elif not os.path.isfile(sys.argv[1]):
    print("File does not exist")
    sys.exit(1)
elif not sys.argv[1].endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)
else:
    csv_(sys.argv[1])
