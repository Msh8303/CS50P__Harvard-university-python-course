from datetime import date
import inflect
import sys
import operator

p = inflect.engine()



def main ():
    try:
        date_ = input("Date of Birth: ")
        age = operator.sub(date.today(), date.fromisoformat(date_))
        print(convert(age.days))
    except ValueError:
        sys.exit("Invalid date")
def convert(days):
    minute = days * 60 * 24
    return f"{(p.number_to_words(minute,andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()
