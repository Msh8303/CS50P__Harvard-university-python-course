
def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

symbols = [" ", ",", ".","!", ";", "?"]

def is_valid(s):

    validated_string =""
    count_num = 0
    #vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if (len(s)>=2 and len(s)<=6):
        if s[0].isalpha() and s[1].isalpha():
            for char in s:
                if char not in symbols:
                    if char.isnumeric() and count_num == 0 and char != '0':
                        count_num += 1
                        validated_string += char
                    elif char.isnumeric() and count_num > 0:
                        count_num += 1
                        validated_string += char
                    elif char.isalpha() and count_num == 0:
                        validated_string += char





    if validated_string == s:
        return True

    else:
        return False


if __name__ == '__main__':
    main()
