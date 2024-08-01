def main():
    input_ = input("Input: ")
    print(shorten(input_))



def shorten(input_):
    vowels = ['i','e','o','u','a','A','E','O','U','I']
    output_ = ''
    for char in input_:
        if char not in vowels:
            output_ += char
    return output_


if __name__ == '__main__':
    main()