import csv
import sys
import os


def split(name):
    parts = name.split(', ')
    firstname = parts[1].strip()
    lastname = parts[0].strip()
    return firstname, lastname


def csv_1(before, after):
    with open(before, "r") as before_file, open(after, "w") as after_file:

        reader = csv.DictReader(before_file)
        fieldnamess = ["first", "last", "house"]
        writer = csv.DictWriter(after_file, fieldnames=fieldnamess)
        writer.writeheader()
        for row in reader:
            name = row['name']
            house = row['house']
            first_n, last_n = split(name)
            writer.writerow({'first': first_n.strip(), 'last': last_n.strip(), 'house': house.strip()})


if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)
elif not os.path.isfile(sys.argv[1]):
    print(f'Could not read {sys.argv[1]}')
    sys.exit(1)
elif not sys.argv[1].endswith(".csv"):
    print(f'Could not read {sys.argv[1]}')
    sys.exit(1)
elif not sys.argv[2].endswith(".csv"):
    print(f'Could not read {sys.argv[2]}')
    sys.exit(1)
else:
    csv_1(sys.argv[1], sys.argv[2])
